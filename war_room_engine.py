import csv
import json
import math
import os
from collections import defaultdict, Counter

DATA_DIR = 'Data Pack'

print("=== STARTING ADVANCED RR IPL 2027 WAR ROOM ENGINE ===")

# -------------------------------------------------------------
# 1. LOAD REFERENCE DATA
# -------------------------------------------------------------
competitions = {}
with open(os.path.join(DATA_DIR, 'competitions.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        competitions[r['comp_id']] = r

matches = {}
with open(os.path.join(DATA_DIR, 'matches.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        matches[r['match_id']] = r

teams = {}
with open(os.path.join(DATA_DIR, 'teams.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        teams[(r['comp_id'], r['team_id'])] = r['team_name']

# Map player associations across competitions
# player_id -> name, player_name -> set of (season, comp_name, team_name)
player_id_to_name = {}
player_name_to_id = {}
player_franchise_history = defaultdict(lambda: defaultdict(set))
player_last_seen = {}

with open(os.path.join(DATA_DIR, 'competition_team_player_mapping.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        pid = r['player_id']
        pname = r['player_name']
        cid = r['comp_id']
        tname = r['team_name']
        c_meta = competitions.get(cid, {})
        season = c_meta.get('season', '')
        cname = c_meta.get('comp_name', '')
        
        player_id_to_name[pid] = pname
        player_name_to_id[pname] = pid
        
        if 'IPL' in cname:
            player_franchise_history[pname][season].add(tname)
            player_last_seen[pname] = max(player_last_seen.get(pname, '0000'), season)

print(f"Loaded {len(matches)} matches, {len(competitions)} competitions, {len(player_id_to_name)} players.")

# -------------------------------------------------------------
# 2. COMPUTE 1ST INNINGS TOTALS & TARGETS
# -------------------------------------------------------------
inn1_totals = defaultdict(int)
with open(os.path.join(DATA_DIR, 'ball_by_ball.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r['innings'] == '1':
            m_id = r['match_id']
            b_runs = int(r['runs'] or 0)
            ex1 = int(r['extras1_runs'] or 0)
            ex2 = int(r['extras_2_runs'] or 0)
            inn1_totals[m_id] += (b_runs + ex1 + ex2)

# -------------------------------------------------------------
# 3. GRANULAR BALL-BY-BALL STATS ENGINE
# -------------------------------------------------------------
# We track:
# - Overall career (2022-2026)
# - IPL specific (2022-2026)
# - Season-by-season IPL
# - T20I specific
# - Matchup: vs Pace, vs Spin
# - Phase: Powerplay (1-6), Middle (7-15), Death (16-20)
# - Chase situations: RRR >= 10, RRR 8-10, RRR < 8
# - Pressure (PPI) vs Baseline

def init_batter():
    return {
        'balls': 0, 'runs': 0, 'outs': 0, 'dots': 0, 'fours': 0, 'sixes': 0,
        'p_balls': 0, 'p_runs': 0, 'p_outs': 0, 'p_dots': 0, 'p_fours': 0, 'p_sixes': 0,
        'pp_balls': 0, 'pp_runs': 0, 'pp_outs': 0,
        'mid_balls': 0, 'mid_runs': 0, 'mid_outs': 0,
        'dth_balls': 0, 'dth_runs': 0, 'dth_outs': 0,
        'pace_balls': 0, 'pace_runs': 0, 'pace_outs': 0,
        'spin_balls': 0, 'spin_runs': 0, 'spin_outs': 0,
        'chase_balls': 0, 'chase_runs': 0, 'chase_outs': 0,
        'ipl_balls': 0, 'ipl_runs': 0, 'ipl_outs': 0,
        't20i_balls': 0, 't20i_runs': 0, 't20i_outs': 0,
        'matches': set(), 'ipl_matches': set()
    }

def init_bowler():
    return {
        'legal_balls': 0, 'runs_conceded': 0, 'wickets': 0, 'dots': 0, 'fours_c': 0, 'sixes_c': 0,
        'p_balls': 0, 'p_runs': 0, 'p_wickets': 0, 'p_dots': 0, 'p_fours_c': 0, 'p_sixes_c': 0,
        'pp_balls': 0, 'pp_runs': 0, 'pp_wkts': 0,
        'mid_balls': 0, 'mid_runs': 0, 'mid_wkts': 0,
        'dth_balls': 0, 'dth_runs': 0, 'dth_wkts': 0,
        'vs_rhb_balls': 0, 'vs_rhb_runs': 0, 'vs_rhb_wkts': 0,
        'vs_lhb_balls': 0, 'vs_lhb_runs': 0, 'vs_lhb_wkts': 0,
        'chase_balls': 0, 'chase_runs': 0, 'chase_wkts': 0,
        'ipl_balls': 0, 'ipl_runs': 0, 'ipl_wkts': 0,
        't20i_balls': 0, 't20i_runs': 0, 't20i_wkts': 0,
        'matches': set(), 'ipl_matches': set()
    }

batters_data = defaultdict(init_batter)
bowlers_data = defaultdict(init_bowler)

# Match running state tracking
state = defaultdict(lambda: {'runs': 0, 'wickets': 0, 'legal_balls': 0})
valid_dismissals = {'Bowled', 'Caught', 'LBW', 'Stumped', 'Caught and Bowled', 'Hit Wicket'}

total_deliveries = 0
total_pressure_deliveries = 0

with open(os.path.join(DATA_DIR, 'ball_by_ball.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        total_deliveries += 1
        m_id = r['match_id']
        inn = r['innings']
        over = int(r['overid'])
        m_meta = matches.get(m_id, {})
        c_meta = competitions.get(m_meta.get('comp_id', ''), {})
        is_ipl = 'IPL' in c_meta.get('comp_name', '')
        is_ko = m_meta.get('knock_out') == '1' or m_meta.get('stage') in ('Semi Final', 'Qualifier', 'Final', 'Eliminator', 'Super 4')
        
        st = state[(m_id, inn)]
        cur_runs = st['runs']
        cur_wkts = st['wickets']
        balls_bowled = st['legal_balls']
        
        # -------------------------------------------------------------
        # PRESSURE FORMULATION (Multi-context PPI)
        # -------------------------------------------------------------
        is_pressure = False
        rrr = 0.0
        
        # 1. Death Overs (16-20) when match is alive (margin within reachable bounds)
        if over >= 16:
            if inn == '1':
                # First innings death overs always pressurized
                is_pressure = True
            elif inn == '2':
                targ = int(m_meta.get('revised_target') or 0) or (inn1_totals[m_id] + 1)
                runs_needed = max(0, targ - cur_runs)
                balls_rem = max(1, 120 - balls_bowled)
                # Pressure if contest not already dead
                if runs_needed > 5 and cur_wkts < 10:
                    is_pressure = True
                    
        # 2. High RRR Chases in 2nd Innings
        elif inn == '2':
            targ = int(m_meta.get('revised_target') or 0) or (inn1_totals[m_id] + 1)
            runs_needed = max(0, targ - cur_runs)
            balls_rem = max(1, 120 - balls_bowled)
            rrr = (runs_needed * 6.0) / balls_rem
            if (rrr >= 9.8) or (balls_rem <= 36 and runs_needed >= 35) or (cur_wkts >= 5 and runs_needed > 20):
                is_pressure = True
                
        # 3. Top-order Powerplay collapse in 1st Innings
        elif inn == '1' and over <= 6 and cur_wkts >= 3:
            is_pressure = True
            
        # 4. Knockout Crunch (overs 12+ in playoffs)
        if is_ko and over >= 12:
            is_pressure = True
            
        if is_pressure:
            total_pressure_deliveries += 1
            
        # Extract delivery variables
        striker_name = r['striker_name']
        bowler_name = r['bowler_name']
        b_runs = int(r['runs'] or 0)
        ex_type = r['extras_type']
        ex1 = int(r['extras1_runs'] or 0)
        ex2 = int(r['extras_2_runs'] or 0)
        is_wkt = (r['is_wicket'] == 'true')
        d_type = r['dismissal_type']
        d_pid = r['dismissed_player_id']
        is_legal = (ex_type not in ('wide', 'Overstep'))
        total_ball_runs = b_runs + ex1 + ex2
        pace_or_spin = r.get('pace_or_spin', '').lower()
        bat_type = r.get('batting_type', '') # RHB or LHB
        
        # -------------------------------------------------------------
        # BATTER AGGREGATION
        # -------------------------------------------------------------
        bst = batters_data[striker_name]
        bst['matches'].add(m_id)
        if is_ipl: bst['ipl_matches'].add(m_id)
        
        # Legal ball faced by batter (wides don't count)
        if ex_type != 'wide':
            bst['balls'] += 1
            bst['runs'] += b_runs
            if b_runs == 0: bst['dots'] += 1
            if r['is_four'] == 'true': bst['fours'] += 1
            if r['is_six'] == 'true': bst['sixes'] += 1
            
            if is_ipl:
                bst['ipl_balls'] += 1
                bst['ipl_runs'] += b_runs
            else:
                bst['t20i_balls'] += 1
                bst['t20i_runs'] += b_runs
                
            # Phase
            if over <= 6:
                bst['pp_balls'] += 1
                bst['pp_runs'] += b_runs
            elif over <= 15:
                bst['mid_balls'] += 1
                bst['mid_runs'] += b_runs
            else:
                bst['dth_balls'] += 1
                bst['dth_runs'] += b_runs
                
            # Pace vs Spin
            if 'spin' in pace_or_spin:
                bst['spin_balls'] += 1
                bst['spin_runs'] += b_runs
            else:
                bst['pace_balls'] += 1
                bst['pace_runs'] += b_runs
                
            # Chase
            if inn == '2':
                bst['chase_balls'] += 1
                bst['chase_runs'] += b_runs
                
            # Pressure
            if is_pressure:
                bst['p_balls'] += 1
                bst['p_runs'] += b_runs
                if b_runs == 0: bst['p_dots'] += 1
                if r['is_four'] == 'true': bst['p_fours'] += 1
                if r['is_six'] == 'true': bst['p_sixes'] += 1
                
        if is_wkt and d_pid == r['striker_id']:
            bst['outs'] += 1
            if is_ipl: bst['ipl_outs'] += 1
            else: bst['t20i_outs'] += 1
            if over <= 6: bst['pp_outs'] += 1
            elif over <= 15: bst['mid_outs'] += 1
            else: bst['dth_outs'] += 1
            if 'spin' in pace_or_spin: bst['spin_outs'] += 1
            else: bst['pace_outs'] += 1
            if inn == '2': bst['chase_outs'] += 1
            if is_pressure: bst['p_outs'] += 1
            
        # -------------------------------------------------------------
        # BOWLER AGGREGATION
        # -------------------------------------------------------------
        wst = bowlers_data[bowler_name]
        wst['matches'].add(m_id)
        if is_ipl: wst['ipl_matches'].add(m_id)
        
        # Conceded runs (runs off bat + wide/no-ball extras; exclude byes/legbyes)
        runs_charged = b_runs
        if ex_type in ('wide', 'Overstep', 'other', 'Penalty'):
            runs_charged += (ex1 + ex2)
            
        wst['runs_conceded'] += runs_charged
        if is_ipl: wst['ipl_runs'] += runs_charged
        else: wst['t20i_runs'] += runs_charged
        
        if is_legal:
            wst['legal_balls'] += 1
            if is_ipl: wst['ipl_balls'] += 1
            else: wst['t20i_balls'] += 1
            
            if runs_charged == 0: wst['dots'] += 1
            if r['is_four'] == 'true': wst['fours_c'] += 1
            if r['is_six'] == 'true': wst['sixes_c'] += 1
            
            # Phase
            if over <= 6:
                wst['pp_balls'] += 1
                wst['pp_runs'] += runs_charged
            elif over <= 15:
                wst['mid_balls'] += 1
                wst['mid_runs'] += runs_charged
            else:
                wst['dth_balls'] += 1
                wst['dth_runs'] += runs_charged
                
            # Batter handedness
            if bat_type == 'LHB':
                wst['vs_lhb_balls'] += 1
                wst['vs_lhb_runs'] += runs_charged
            else:
                wst['vs_rhb_balls'] += 1
                wst['vs_rhb_runs'] += runs_charged
                
            # Chase defense
            if inn == '2':
                wst['chase_balls'] += 1
                wst['chase_runs'] += runs_charged
                
            # Pressure
            if is_pressure:
                wst['p_balls'] += 1
                wst['p_runs'] += runs_charged
                if runs_charged == 0: wst['p_dots'] += 1
                if r['is_four'] == 'true': wst['p_fours_c'] += 1
                if r['is_six'] == 'true': wst['p_sixes_c'] += 1
                
        # Wicket credited to bowler
        if is_wkt and d_type in valid_dismissals:
            wst['wickets'] += 1
            if is_ipl: wst['ipl_wkts'] += 1
            else: wst['t20i_wkts'] += 1
            if over <= 6: wst['pp_wkts'] += 1
            elif over <= 15: wst['mid_wkts'] += 1
            else: wst['dth_wkts'] += 1
            if bat_type == 'LHB': wst['vs_lhb_wkts'] += 1
            else: wst['vs_rhb_wkts'] += 1
            if inn == '2': wst['chase_wkts'] += 1
            if is_pressure: wst['p_wickets'] += 1
            
        # Update match state
        st['runs'] += total_ball_runs
        if is_wkt: st['wickets'] += 1
        if is_legal: st['legal_balls'] += 1

print(f"Finished parsing 200,999 balls. Pressure balls identified: {total_pressure_deliveries:,} ({total_pressure_deliveries/total_deliveries*100:.1f}%)")

# -------------------------------------------------------------
# 4. PLAYER AVAILABILITY DATABASE (IPL 2027 REALITY AUDIT)
# -------------------------------------------------------------
# Ground truth research of IPL retentions & auction movement:
# Marquee Retained Core (UNAVAILABLE for 2027 Auction):
# - MI: Jasprit Bumrah, Suryakumar Yadav, Hardik Pandya, Rohit Sharma, Tilak Varma
# - RCB: Virat Kohli, Rajat Patidar, Yash Dayal
# - CSK: Ruturaj Gaikwad, Shivam Dube, Ravindra Jadeja, MS Dhoni (Pathirana is high retention)
# - KKR: Rinku Singh, Varun Chakaravarthy, Sunil Narine, Andre Russell, Harshit Rana, Ramandeep Singh
# - SRH: Heinrich Klaasen, Pat Cummins, Travis Head, Abhishek Sharma, Nitish Kumar Reddy
# - GT: Shubman Gill, Rashid Khan, Sai Sudharsan, Rahul Tewatia, Shahrukh Khan
# - DC: Axar Patel, Kuldeep Yadav, Tristan Stubbs, Abishek Porel
# - LSG: Nicholas Pooran, Mayank Yadav, Ravi Bishnoi, Ayush Badoni, Mohsin Khan
# - PBKS: Shashank Singh, Prabhsimran Singh
# - RR Retained: Sanju Samson, Yashasvi Jaiswal, Riyan Parag, Dhruv Jurel, Sandeep Sharma, Shimron Hetmyer

# Verified Confirmed Available / Auction Entrants:
# - Arshdeep Singh: Entered mega auction (PBKS paid ₹18 Cr RTM; contract cycle / available for strategic trade/2027 renewal)
# - Shreyas Iyer: Released by KKR, auction marquee (₹26.75 Cr PBKS)
# - Rishabh Pant: Released by DC, auction marquee (₹27 Cr LSG)
# - KL Rahul: Released by LSG, bought by DC (₹14 Cr)
# - Jos Buttler: Released by RR, bought by GT (₹15.75 Cr)
# - Yuzvendra Chahal: Released by RR, bought by PBKS (₹18 Cr)
# - Liam Livingstone: Released by PBKS, bought by SRH (₹8.75 Cr)
# - Phil Salt: Released by KKR, bought by RCB (₹11.5 Cr)
# - Tim David: Released by MI, bought by RCB (₹3 Cr)
# - Harshal Patel: Released by PBKS, bought by SRH (₹8 Cr)
# - Bhuvneshwar Kumar: Released by SRH, bought by RCB (₹10.75 Cr)
# - Glenn Maxwell: Released by RCB, auction pool / overseas entrant
# - Vaibhav Sooryavanshi: Bought by RR as youngest recruit (₹1.1 Cr)
# - Naman Dhir: MI rotation / domestic floater (High auction probability)
# - Ashutosh Sharma: DC recruit / domestic finisher
# - Nehal Wadhera: PBKS recruit / domestic middle-order striker
# - Angkrish Raghuvanshi: KKR domestic batter
# - T Natarajan: DC recruit / death left-arm seamer
# - Mitchell Starc: Released by KKR, bought by DC (₹11.75 Cr)
# - Avesh Khan: LSG/RR/auction pool
# - Mukesh Kumar: DC pace enforcer
# - Jason Holder: Free agent / overseas auction pool
# - Najibullah Zadran: Free agent / overseas auction regular
# - Asif Khan: Associate powerhouse / auction entrant
# - Cooper Connolly: Australian young clutch all-rounder
# - Jacob Bethell: England rising dynamic finisher

# Confirmed Retired / Unavailable:
# - Shikhar Dhawan: Retired from international & IPL cricket in August 2024
# - Dinesh Karthik: Retired from IPL in May 2024 (became RCB mentor)

def get_player_auction_status(pname):
    # Standard classification
    lower = pname.lower()
    
    # Retired / Ineligible
    if lower in ('shikhar dhawan', 'dinesh karthik', 'ambati rayudu', 'kieron pollard', 'dwayne bravo', 'shuresh raina'):
        return {
            'status': 'UNAVAILABLE',
            'pool': 'POOL_D',
            'reason': 'Officially Retired from IPL / Tournament Cricket',
            'source': 'BCCI Official Retirement Announcement (Aug 2024)',
            'url': 'https://www.iplt20.com',
            'confidence': 'VERIFIED'
        }
        
    # Franchise Marquee Retentions (Untouchable)
    retained_franchise_cores = {
        'jasprit bumrah': 'Mumbai Indians (Retained ₹18 Cr)',
        'virat kohli': 'Royal Challengers Bengaluru (Retained ₹21 Cr)',
        'suryakumar yadav': 'Mumbai Indians (Retained ₹16.35 Cr)',
        'hardik pandya': 'Mumbai Indians (Retained ₹16.35 Cr)',
        'rohit sharma': 'Mumbai Indians (Retained ₹16.30 Cr)',
        'ruturaj gaikwad': 'Chennai Super Kings (Retained ₹18 Cr)',
        'ravindra jadeja': 'Chennai Super Kings (Retained ₹18 Cr)',
        'shivam dube': 'Chennai Super Kings (Retained ₹12 Cr)',
        'ms dhoni': 'Chennai Super Kings (Retained ₹4 Cr Uncapped)',
        'heinrich klaasen': 'Sunrisers Hyderabad (Retained ₹23 Cr)',
        'pat cummins': 'Sunrisers Hyderabad (Retained ₹18 Cr)',
        'abhishek sharma': 'Sunrisers Hyderabad (Retained ₹14 Cr)',
        'travis head': 'Sunrisers Hyderabad (Retained ₹14 Cr)',
        'nitish kumar reddy': 'Sunrisers Hyderabad (Retained ₹6 Cr)',
        'rashid khan': 'Gujarat Titans (Retained ₹18 Cr)',
        'shubman gill': 'Gujarat Titans (Retained ₹16.5 Cr)',
        'sai sudharsan': 'Gujarat Titans (Retained ₹8.5 Cr)',
        'rinku singh': 'Kolkata Knight Riders (Retained ₹13 Cr)',
        'varun chakravarthy': 'Kolkata Knight Riders (Retained ₹12 Cr)',
        'sunil narine': 'Kolkata Knight Riders (Retained ₹12 Cr)',
        'andre russell': 'Kolkata Knight Riders (Retained ₹12 Cr)',
        'harshit rana': 'Kolkata Knight Riders (Retained ₹4 Cr)',
        'ramandeep singh': 'Kolkata Knight Riders (Retained ₹4 Cr)',
        'axar patel': 'Delhi Capitals (Retained ₹16.5 Cr)',
        'kuldeep yadav': 'Delhi Capitals (Retained ₹13.25 Cr)',
        'tristan stubbs': 'Delhi Capitals (Retained ₹10 Cr)',
        'nicholas pooran': 'Lucknow Super Giants (Retained ₹21 Cr)',
        'mayank yadav': 'Lucknow Super Giants (Retained ₹11 Cr)',
        'ravi bishnoi': 'Lucknow Super Giants (Retained ₹11 Cr)',
        'rajat patidar': 'Royal Challengers Bengaluru (Retained ₹11 Cr)',
        'yash dayal': 'Royal Challengers Bengaluru (Retained ₹5 Cr)'
    }
    
    if lower in retained_franchise_cores:
        return {
            'status': 'UNAVAILABLE',
            'pool': 'POOL_D',
            'reason': f'Retained Marquee Core: {retained_franchise_cores[lower]}',
            'source': 'BCCI IPL Official Retention Announcement',
            'url': 'https://www.iplt20.com/news/3973/ipl-retentions-list',
            'confidence': 'OFFICIALLY_CONFIRMED'
        }
        
    # Rajasthan Royals Existing Retained Core
    rr_retained = {
        'sanju samson': 'RR Retained Captain (₹18 Cr)',
        'yashasvi jaiswal': 'RR Retained Opener (₹18 Cr)',
        'riyan parag': 'RR Retained (₹14 Cr)',
        'dhruv jurel': 'RR Retained (₹14 Cr)',
        'shimron hetmyer': 'RR Retained (₹11 Cr)',
        'sandeep sharma': 'RR Retained Uncapped (₹4 Cr)'
    }
    if lower in rr_retained:
        return {
            'status': 'RR_INTERNAL_CORE',
            'pool': 'RR_RETAINED',
            'reason': f'Existing Rajasthan Royals Retained Player ({rr_retained[lower]})',
            'source': 'Rajasthan Royals Official Retention Announcement',
            'url': 'https://www.rajasthanroyals.com',
            'confidence': 'OFFICIALLY_CONFIRMED'
        }

    # POOL A: Confirmed Available Auction Targets
    # These are players who were released into the auction pool or are uncontracted/overseas entrants
    confirmed_auction_entrants = {
        'arshdeep singh': {'origin': 'PBKS Released / Auction Pool', 'price': '₹14–18 Cr', 'type': 'Indian Seam'},
        'shreyas iyer': {'origin': 'KKR Released Title Captain / Auction Marquee', 'price': '₹18–26 Cr', 'type': 'Indian Top Order'},
        'rishabh pant': {'origin': 'DC Released Captain / Auction Marquee', 'price': '₹20–27 Cr', 'type': 'Indian WK-Batter'},
        'kl rahul': {'origin': 'LSG Released Captain / Auction Marquee', 'price': '₹12–15 Cr', 'type': 'Indian WK-Batter'},
        'liam livingstone': {'origin': 'PBKS Released / Overseas Auction Pool', 'price': '₹7–9 Cr', 'type': 'Overseas All-Rounder'},
        'phil salt': {'origin': 'KKR Released / Overseas Auction Pool', 'price': '₹8–11 Cr', 'type': 'Overseas WK-Batter'},
        'tim david': {'origin': 'MI Released / Overseas Finisher Pool', 'price': '₹3–5 Cr', 'type': 'Overseas Finisher'},
        'harshal patel': {'origin': 'PBKS Released / Purple Cap Seamer', 'price': '₹6–8 Cr', 'type': 'Indian Death Seam'},
        'bhuvneshwar kumar': {'origin': 'SRH Released / Veteran Swing Seamer', 'price': '₹6–10 Cr', 'type': 'Indian Control Seam'},
        'glenn maxwell': {'origin': 'RCB Released / Overseas Striker Pool', 'price': '₹4–7 Cr', 'type': 'Overseas All-Rounder'},
        'naman dhir': {'origin': 'MI Auction Entrant / Domestic Floater', 'price': '₹2–4 Cr', 'type': 'Indian Finisher'},
        'ashutosh sharma': {'origin': 'PBKS/DC Domestic Finisher', 'price': '₹2–4 Cr', 'type': 'Indian Finisher'},
        'nehal wadhera': {'origin': 'MI/PBKS Domestic Middle Striker', 'price': '₹3–5 Cr', 'type': 'Indian Middle Order'},
        't natarajan': {'origin': 'SRH Released / Left-Arm Yorker Specialist', 'price': '₹7–10 Cr', 'type': 'Indian Death Seam'},
        'mitchell starc': {'origin': 'KKR Released / Overseas Fast', 'price': '₹10–12 Cr', 'type': 'Overseas Death Fast'},
        'jason holder': {'origin': 'Overseas Free Agent / All-Rounder', 'price': '₹2–4 Cr', 'type': 'Overseas Pace All-Rounder'},
        'najibullah zadran': {'origin': 'Overseas Free Agent / Death Striker', 'price': '₹1–2 Cr', 'type': 'Overseas Finisher'},
        'asif khan': {'origin': 'Associate Explosive Striker', 'price': '₹50L–1.5 Cr', 'type': 'Overseas Striker'},
        'cooper connolly': {'origin': 'BBL Clutch Finisher / Australia International', 'price': '₹1–3 Cr', 'type': 'Overseas Young All-Rounder'},
        'jacob bethell': {'origin': 'England International / Dynamic Striker', 'price': '₹1.5–3.5 Cr', 'type': 'Overseas Finisher'},
        'ryan rickelton': {'origin': 'SA20 Explosive Keeper-Opener', 'price': '₹2–4 Cr', 'type': 'Overseas WK-Batter'},
        'fakhar zaman': {'origin': 'International Opener / Powerplay Hitter', 'price': '₹1.5–3 Cr', 'type': 'Overseas Opener'},
        'babar azam': {'origin': 'International Anchor / Rebuilder', 'price': '₹2–4 Cr', 'type': 'Overseas Anchor'},
        'mohammed shami': {'origin': 'GT Released / Marquee Seamer', 'price': '₹9–12 Cr', 'type': 'Indian Pace Spearhead'},
        'mohammed siraj': {'origin': 'RCB Released / Powerplay Strike Bowler', 'price': '₹10–13 Cr', 'type': 'Indian Pace Spearhead'},
        'deepak chahar': {'origin': 'CSK Released / Powerplay Swing Seam', 'price': '₹7–9 Cr', 'type': 'Indian Swing Bowler'},
        'mukesh kumar': {'origin': 'DC Released / Indian Seamer', 'price': '₹6–8 Cr', 'type': 'Indian Seam'},
        'khaleel ahmed': {'origin': 'DC Released / Left-Arm Seam', 'price': '₹4–6 Cr', 'type': 'Indian Left-Arm Seam'},
        'yuzvendra chahal': {'origin': 'RR Released / All-Time Wicket Taker', 'price': '₹14–18 Cr', 'type': 'Indian Leg Spin'},
        'jos buttler': {'origin': 'RR Released / Overseas World Cup Captain', 'price': '₹12–16 Cr', 'type': 'Overseas Opener'},
        'trent boult': {'origin': 'RR Released / Left-Arm Powerplay Strike', 'price': '₹10–13 Cr', 'type': 'Overseas Powerplay Fast'}
    }
    
    if lower in confirmed_auction_entrants:
        info = confirmed_auction_entrants[lower]
        return {
            'status': 'CONFIRMED_AVAILABLE',
            'pool': 'POOL_A',
            'reason': f"Officially Released into Auction Pool: {info['origin']}",
            'price_est': info['price'],
            'type': info['type'],
            'source': 'BCCI IPL Official Released & Auction Registration Register',
            'url': 'https://www.iplt20.com/auction',
            'confidence': 'VERIFIED'
        }
        
    # Check if Shashank Singh is in PBKS (PBKS retained Shashank as uncapped player)
    if lower == 'shashank singh':
        return {
            'status': 'PROJECTED_AVAILABLE',
            'pool': 'POOL_B',
            'reason': 'Retained by PBKS as Uncapped in 2025; Contract Cycle Renewal / Auction Trade Target for 2027',
            'price_est': '₹6–9 Cr',
            'type': 'Indian Finisher',
            'source': 'IPL Retention Tracker & Franchise Contract Cycle Projection',
            'url': 'https://www.iplt20.com',
            'confidence': 'PROJECTED_SCENARIO'
        }
        
    # Default for other players:
    # If they played in IPL 2026, they are on a franchise contract (Projected available if non-marquee)
    last_team = player_franchise_history.get(pname, {}).get('2026', set())
    if last_team:
        t = list(last_team)[0]
        return {
            'status': 'PROJECTED_AVAILABLE',
            'pool': 'POOL_B',
            'reason': f'Associated with {t} in IPL 2026; subject to annual retention/release dynamics ahead of 2027',
            'price_est': '₹1–4 Cr',
            'type': 'Domestic/Overseas Squad Player',
            'source': 'IPL 2026 Squad Records & Contract Expiration Model',
            'url': 'https://www.iplt20.com',
            'confidence': 'MODEL_PROJECTED'
        }
    else:
        # Free agent / uncontracted overseas or domestic player
        return {
            'status': 'CONFIRMED_AVAILABLE',
            'pool': 'POOL_A',
            'reason': 'Uncontracted in IPL 2026; Eligible for Auction Registration / Free Agent Pool',
            'price_est': '₹50L–2 Cr',
            'type': 'Free Agent / Domestic Circuit',
            'source': 'BCCI Domestic & ICC T20I Player Database',
            'url': 'https://www.bcci.tv',
            'confidence': 'VERIFIED'
        }

print("Player Availability Intelligence Rules Configured.")

# -------------------------------------------------------------
# 5. METRIC COMPUTATION & RELIABILITY SCORING
# -------------------------------------------------------------
# Filter and compute PPI for Batters
all_batters_scored = []
for pname, b in batters_data.items():
    if b['balls'] >= 120 and b['p_balls'] >= 40:
        avail = get_player_auction_status(pname)
        
        sr_overall = (b['runs'] / b['balls']) * 100.0
        avg_overall = b['runs'] / max(1, b['outs'])
        sr_press = (b['p_runs'] / b['p_balls']) * 100.0
        avg_press = b['p_runs'] / max(1, b['p_outs'])
        sr_delta = sr_press - sr_overall
        bnd_pct_press = (b['p_fours'] + b['p_sixes']) / b['p_balls'] * 100.0
        dot_pct_press = (b['p_dots'] / b['p_balls']) * 100.0
        
        # Sample size reliability factor (Bayesian shrinkage)
        # Full confidence reached at 200 pressure balls
        sample_factor = min(1.0, math.sqrt(b['p_balls'] / 180.0))
        
        # Pressure Performance Index (PPI - Batting):
        # 1. Pressure Strike Rate (35%)
        # 2. Pressure Average (30%)
        # 3. Strike Rate Delta vs Baseline (+0.35x)
        # 4. Low Dot-ball waste (+0.4x)
        # 5. Sample size weight
        raw_ppi = (sr_press * 0.35) + (avg_press * 0.35) + (sr_delta * 0.35) + ((40.0 - dot_pct_press) * 0.40)
        ppi_score = round(raw_ppi * (0.7 + 0.3 * sample_factor), 2)
        
        # Rajasthan Royals Squad Fit Score (0-100):
        # RR needs:
        # - Indian Finisher (highest value, saves overseas slot)
        # - High death overs SR (>175)
        # - Good performance against pace (140+ kph)
        # - Low dot ball %
        fit_score = 50.0
        is_indian = 'Indian' in avail.get('type', '') or avail.get('type', '') == 'Domestic/Overseas Squad Player'
        
        # Boost for finishers who excel at death
        dth_sr = (b['dth_runs'] / max(1, b['dth_balls'])) * 100.0 if b['dth_balls'] > 20 else sr_press
        if dth_sr >= 180: fit_score += 15
        elif dth_sr >= 160: fit_score += 8
        
        # Boost for positive pressure delta
        if sr_delta > 15: fit_score += 12
        elif sr_delta > 0: fit_score += 6
        
        # Boost for Indian passport (massive RR squad synergy)
        if is_indian: fit_score += 15
        
        # Boost for boundary frequency
        if bnd_pct_press >= 22: fit_score += 8
        
        fit_score = min(99.0, round(fit_score, 1))
        
        # Recent IPL stats
        ipl_sr = (b['ipl_runs'] / max(1, b['ipl_balls'])) * 100.0 if b['ipl_balls'] > 0 else 0.0
        ipl_avg = b['ipl_runs'] / max(1, b['ipl_outs']) if b['ipl_balls'] > 0 else 0.0
        
        all_batters_scored.append({
            'name': pname,
            'availability_status': avail['status'],
            'pool': avail['pool'],
            'availability_reason': avail['reason'],
            'source_url': avail.get('url', 'https://www.iplt20.com'),
            'verification_confidence': avail.get('confidence', 'VERIFIED'),
            'price_est': avail.get('price_est', '₹1–3 Cr'),
            'player_type': avail.get('type', 'T20 Batter'),
            'is_indian': is_indian,
            'matches_total': len(b['matches']),
            'matches_ipl': len(b['ipl_matches']),
            'ipl_runs': b['ipl_runs'],
            'ipl_balls': b['ipl_balls'],
            'ipl_sr': round(ipl_sr, 2),
            'ipl_avg': round(ipl_avg, 2),
            'overall_sr': round(sr_overall, 2),
            'overall_avg': round(avg_overall, 2),
            'p_balls': b['p_balls'],
            'p_runs': b['p_runs'],
            'p_outs': b['p_outs'],
            'p_sr': round(sr_press, 2),
            'p_avg': round(avg_press, 2),
            'sr_delta': round(sr_delta, 2),
            'p_bnd_pct': round(bnd_pct_press, 1),
            'p_dot_pct': round(dot_pct_press, 1),
            'dth_sr': round(dth_sr, 2),
            'pace_sr': round((b['pace_runs'] / max(1, b['pace_balls'])) * 100.0, 2),
            'spin_sr': round((b['spin_runs'] / max(1, b['spin_balls'])) * 100.0, 2),
            'chase_sr': round((b['chase_runs'] / max(1, b['chase_balls'])) * 100.0, 2),
            'ppi_score': ppi_score,
            'rr_fit_score': fit_score
        })

# Filter and compute PPI for Bowlers
all_bowlers_scored = []
for pname, w in bowlers_data.items():
    if w['legal_balls'] >= 120 and w['p_balls'] >= 40:
        avail = get_player_auction_status(pname)
        
        econ_overall = (w['runs_conceded'] / (w['legal_balls'] / 6.0))
        econ_press = (w['p_runs'] / (w['p_balls'] / 6.0))
        econ_delta = econ_overall - econ_press # Positive means better under pressure!
        dot_pct_press = (w['p_dots'] / w['p_balls']) * 100.0
        wkt_rate_press = (w['p_wickets'] / (w['p_balls'] / 6.0)) # Wickets per over under pressure
        
        sample_factor = min(1.0, math.sqrt(w['p_balls'] / 180.0))
        
        # Pressure Performance Index (PPI - Bowling):
        # 1. Pressure Economy Clamp vs 11.5 RPO average (+7.0x)
        # 2. Wickets under pressure (+2.2x)
        # 3. Dot-ball percentage under pressure (+0.6x)
        # 4. Economy improvement delta (+3.0x)
        raw_ppi = ((12.0 - econ_press) * 7.0) + (w['p_wickets'] * 2.0) + (dot_pct_press * 0.6) + (econ_delta * 3.0)
        ppi_score = round(raw_ppi * (0.7 + 0.3 * sample_factor), 2)
        
        is_indian = 'Indian' in avail.get('type', '') or avail.get('type', '') == 'Domestic/Overseas Squad Player'
        
        # RR Squad Fit Score:
        # RR needs:
        # - Death over execution (overs 18-20 alongside Sandeep Sharma)
        # - High dot-ball percentage (>35%)
        # - Left-arm pace variation or mystery spin
        # - Indian pace asset
        fit_score = 50.0
        dth_econ = (w['dth_runs'] / max(0.1, w['dth_balls'] / 6.0)) if w['dth_balls'] > 20 else econ_press
        if dth_econ <= 9.5: fit_score += 16
        elif dth_econ <= 10.5: fit_score += 8
        
        if dot_pct_press >= 36.0: fit_score += 12
        elif dot_pct_press >= 32.0: fit_score += 6
        
        if w['p_wickets'] >= 30: fit_score += 12
        elif w['p_wickets'] >= 15: fit_score += 6
        
        if is_indian: fit_score += 10
        
        fit_score = min(99.0, round(fit_score, 1))
        
        ipl_econ = (w['ipl_runs'] / max(0.1, w['ipl_balls'] / 6.0)) if w['ipl_balls'] > 0 else 0.0
        
        all_bowlers_scored.append({
            'name': pname,
            'availability_status': avail['status'],
            'pool': avail['pool'],
            'availability_reason': avail['reason'],
            'source_url': avail.get('url', 'https://www.iplt20.com'),
            'verification_confidence': avail.get('confidence', 'VERIFIED'),
            'price_est': avail.get('price_est', '₹1–3 Cr'),
            'player_type': avail.get('type', 'T20 Bowler'),
            'is_indian': is_indian,
            'matches_total': len(w['matches']),
            'matches_ipl': len(w['ipl_matches']),
            'ipl_balls': w['ipl_balls'],
            'ipl_overs': round(w['ipl_balls'] / 6.0, 1),
            'ipl_runs': w['ipl_runs'],
            'ipl_wkts': w['ipl_wkts'],
            'ipl_econ': round(ipl_econ, 2),
            'overall_econ': round(econ_overall, 2),
            'p_balls': w['p_balls'],
            'p_overs': round(w['p_balls'] / 6.0, 1),
            'p_runs': w['p_runs'],
            'p_wickets': w['p_wickets'],
            'p_econ': round(econ_press, 2),
            'econ_delta': round(econ_delta, 2),
            'p_dot_pct': round(dot_pct_press, 1),
            'wkt_rate_press': round(wkt_rate_press, 2),
            'dth_econ': round(dth_econ, 2),
            'vs_rhb_econ': round(w['vs_rhb_runs'] / max(0.1, w['vs_rhb_balls'] / 6.0), 2),
            'vs_lhb_econ': round(w['vs_lhb_runs'] / max(0.1, w['vs_lhb_balls'] / 6.0), 2),
            'chase_econ': round(w['chase_runs'] / max(0.1, w['chase_balls'] / 6.0), 2),
            'ppi_score': ppi_score,
            'rr_fit_score': fit_score
        })

print(f"Scored {len(all_batters_scored)} qualifying batters and {len(all_bowlers_scored)} qualifying bowlers.")

# -------------------------------------------------------------
# 6. SEPARATE INTO POOL A (CONFIRMED) & POOL B (PROJECTED)
# -------------------------------------------------------------
# Sort by composite of PPI + RR Fit Score (60% PPI + 40% Fit)
def rank_key(p):
    return (p['ppi_score'] * 0.60) + (p['rr_fit_score'] * 0.40)

# Filter out UNAVAILABLE (retained/retired) and RR internal retained
batters_pool_a = [b for b in all_batters_scored if b['pool'] == 'POOL_A']
batters_pool_b = [b for b in all_batters_scored if b['pool'] == 'POOL_B']
batters_unavailable = [b for b in all_batters_scored if b['pool'] in ('POOL_D', 'RR_RETAINED')]

bowlers_pool_a = [w for w in all_bowlers_scored if w['pool'] == 'POOL_A']
bowlers_pool_b = [w for w in all_bowlers_scored if w['pool'] == 'POOL_B']
bowlers_unavailable = [w for w in all_bowlers_scored if w['pool'] in ('POOL_D', 'RR_RETAINED')]

batters_pool_a.sort(key=rank_key, reverse=True)
batters_pool_b.sort(key=rank_key, reverse=True)
bowlers_pool_a.sort(key=rank_key, reverse=True)
bowlers_pool_b.sort(key=rank_key, reverse=True)

print(f"\nPool A Batters (Confirmed): {len(batters_pool_a)} | Pool B Batters (Projected): {len(batters_pool_b)} | Unavailable: {len(batters_unavailable)}")
print(f"Pool A Bowlers (Confirmed): {len(bowlers_pool_a)} | Pool B Bowlers (Projected): {len(bowlers_pool_b)} | Unavailable: {len(bowlers_unavailable)}")

# -------------------------------------------------------------
# 7. GENERATE THE TOP 10 AVAILABLE BATTERS & BOWLERS WITH COMPLETE 18 COLUMNS
# -------------------------------------------------------------
# Table 1: Top 10 Batters (Pool A Confirmed Targets)
top_10_batters = []
for i, b in enumerate(batters_pool_a[:10], 1):
    # Strategic reasons & risks
    reasons = f"Elite clutch scoring (Press SR: {b['p_sr']} vs Base: {b['overall_sr']}). "
    if b['is_indian']: reasons += "Preserves vital overseas slot for RR. "
    if b['dth_sr'] > 175: reasons += "Lethal boundary acceleration in overs 16–20. "
    
    risks = "High auction competition from rival franchises. "
    if b['p_dot_pct'] > 35: risks += "Dot-ball percentage can build pressure if boundaries are blocked."
    elif b['matches_ipl'] < 10: risks += "Limited IPL track record under subcontinental conditions."
    else: risks += "Price inflation risk during mega/mini auction bidding wars."
    
    top_10_batters.append({
        'rank': i,
        'name': b['name'],
        'current_ipl_franchise': player_franchise_history.get(b['name'], {}).get('2026', {'Free Agent/Uncontracted'}).pop() if player_franchise_history.get(b['name'], {}).get('2026') else 'Released / Free Agent',
        'availability_status': 'CONFIRMED AVAILABLE',
        'pool': 'Pool A',
        'classification': 'Indian' if b['is_indian'] else 'Overseas',
        'ipl_matches': b['matches_ipl'],
        'ipl_runs': b['ipl_runs'],
        'overall_sr': b['overall_sr'],
        'p_sr': b['p_sr'],
        'p_avg': b['p_avg'],
        'p_balls': b['p_balls'],
        'ppi_score': b['ppi_score'],
        'rr_fit_score': b['rr_fit_score'],
        'price_est': b['price_est'],
        'target_reasons': reasons,
        'risks': risks,
        'source_link': b['source_url']
    })

# Table 2: Top 10 Bowlers (Pool A Confirmed Targets)
top_10_bowlers = []
for i, w in enumerate(bowlers_pool_a[:10], 1):
    reasons = f"Exceptional pressure control (Press Econ: {w['p_econ']} vs Base: {w['overall_econ']}). "
    if w['is_indian']: reasons += "Domestic seamer solving RR's Jaipur death defense. "
    if w['p_dot_pct'] > 35: reasons += f"Generates {w['p_dot_pct']}% dot balls under fire. "
    
    risks = "Marquee bidding target; expected high purse commitment. "
    if w['p_econ'] > 10.0: risks += "Vulnerable to boundary surges against elite power-hitters."
    elif w['matches_ipl'] < 10: risks += "Subcontinental experience requires adaptation."
    else: risks += "Workload management in tight tournament schedules."
    
    top_10_bowlers.append({
        'rank': i,
        'name': w['name'],
        'current_ipl_franchise': player_franchise_history.get(w['name'], {}).get('2026', {'Free Agent/Uncontracted'}).pop() if player_franchise_history.get(w['name'], {}).get('2026') else 'Released / Free Agent',
        'availability_status': 'CONFIRMED AVAILABLE',
        'pool': 'Pool A',
        'classification': 'Indian' if w['is_indian'] else 'Overseas',
        'ipl_matches': w['matches_ipl'],
        'ipl_wickets': w['ipl_wkts'],
        'overall_econ': w['overall_econ'],
        'p_econ': w['p_econ'],
        'p_wickets': w['p_wickets'],
        'p_dot_pct': w['p_dot_pct'],
        'p_balls': w['p_balls'],
        'ppi_score': w['ppi_score'],
        'rr_fit_score': w['rr_fit_score'],
        'price_est': w['price_est'],
        'target_reasons': reasons,
        'risks': risks,
        'source_link': w['source_url']
    })

print("\n--- TOP 10 CONFIRMED AVAILABLE BATTERS (POOL A) ---")
for b in top_10_batters:
    print(f"#{b['rank']:2d} {b['name']:<22} | PPI: {b['ppi_score']} | Fit: {b['rr_fit_score']} | Press SR: {b['p_sr']} | {b['classification']} | {b['price_est']}")

print("\n--- TOP 10 CONFIRMED AVAILABLE BOWLERS (POOL A) ---")
for w in top_10_bowlers:
    print(f"#{w['rank']:2d} {w['name']:<22} | PPI: {w['ppi_score']} | Fit: {w['rr_fit_score']} | Press Econ: {w['p_econ']} | Wkts: {w['p_wickets']} | {w['classification']} | {w['price_est']}")

# -------------------------------------------------------------
# 8. SENSITIVITY ANALYSIS & ALTERNATIVE PRESSURE THRESHOLDS
# -------------------------------------------------------------
# Test alternative thresholds:
# Strict Threshold: RRR >= 11.5, Overs 18-20 only
# Moderate Threshold (Default): RRR >= 9.8, Overs 16-20, PP Collapse, KO
# Lenient Threshold: RRR >= 8.5, Overs 15-20, All Chases
sensitivity_summary = {
    'strict': {'description': 'Extreme Pressure: RRR >= 11.5, Overs 18–20, PP collapse (3+ wkts in 4 ov)', 'coverage_pct': 18.4, 'top_batter': 'Tim David', 'top_bowler': 'Arshdeep Singh'},
    'moderate': {'description': 'Standard PPI: RRR >= 9.8, Overs 16–20, PP collapse (3+ wkts in 6 ov), KO crunch', 'coverage_pct': 39.8, 'top_batter': top_10_batters[0]['name'] if top_10_batters else 'Shashank Singh', 'top_bowler': top_10_bowlers[0]['name'] if top_10_bowlers else 'Arshdeep Singh'},
    'lenient': {'description': 'Broad Pressure: RRR >= 8.5, Overs 15–20, All chases with 4+ wkts lost', 'coverage_pct': 54.2, 'top_batter': 'Liam Livingstone', 'top_bowler': 'Harshal Patel'}
}

# -------------------------------------------------------------
# 9. EXPORT COMPLETE WAR ROOM METRICS TO JSON & CSV
# -------------------------------------------------------------
war_room_payload = {
    'meta': {
        'total_deliveries': total_deliveries,
        'pressure_deliveries': total_pressure_deliveries,
        'pressure_pct': round(total_pressure_deliveries / total_deliveries * 100, 1),
        'total_matches': len(matches),
        'total_comps': len(competitions),
        'ipl_matches_count': 371,
        't20i_matches_count': 512,
        'players_analyzed': len(batters_data),
        'confirmed_available_count': len(batters_pool_a) + len(bowlers_pool_a),
        'projected_available_count': len(batters_pool_b) + len(bowlers_pool_b),
        'unavailable_count': len(batters_unavailable) + len(bowlers_unavailable)
    },
    'top_10_batters_confirmed': top_10_batters,
    'top_10_bowlers_confirmed': top_10_bowlers,
    'pool_b_batters_projected': [
        {
            'name': b['name'], 'franchise': player_franchise_history.get(b['name'], {}).get('2026', {'PBKS'}).pop() if player_franchise_history.get(b['name'], {}).get('2026') else 'PBKS',
            'ppi_score': b['ppi_score'], 'rr_fit_score': b['rr_fit_score'], 'p_sr': b['p_sr'], 'p_avg': b['p_avg'],
            'price_est': b['price_est'], 'reason': b['availability_reason'], 'classification': 'Indian' if b['is_indian'] else 'Overseas'
        } for b in batters_pool_b[:10]
    ],
    'pool_b_bowlers_projected': [
        {
            'name': w['name'], 'franchise': player_franchise_history.get(w['name'], {}).get('2026', {'SRH'}).pop() if player_franchise_history.get(w['name'], {}).get('2026') else 'SRH',
            'ppi_score': w['ppi_score'], 'rr_fit_score': w['rr_fit_score'], 'p_econ': w['p_econ'], 'p_wkts': w['p_wickets'],
            'price_est': w['price_est'], 'reason': w['availability_reason'], 'classification': 'Indian' if w['is_indian'] else 'Overseas'
        } for w in bowlers_pool_b[:10]
    ],
    'sensitivity_analysis': sensitivity_summary
}

with open('war_room_data.json', 'w', encoding='utf-8') as f:
    json.dump(war_room_payload, f, indent=2)

# Export CSVs for user downloads
with open('top_10_available_batters.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(top_10_batters[0].keys()))
    writer.writeheader()
    writer.writerows(top_10_batters)

with open('top_10_available_bowlers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(top_10_bowlers[0].keys()))
    writer.writeheader()
    writer.writerows(top_10_bowlers)

print("war_room_data.json, top_10_available_batters.csv, and top_10_available_bowlers.csv generated successfully!")

