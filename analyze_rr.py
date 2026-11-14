import csv
import json
import os
from collections import defaultdict

DATA_DIR = 'Data Pack'

# 1. Load competitions
competitions = {}
with open(os.path.join(DATA_DIR, 'competitions.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        competitions[row['comp_id']] = row

# 2. Load matches
matches = {}
with open(os.path.join(DATA_DIR, 'matches.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        matches[row['match_id']] = row

# 3. Calculate 1st innings total per match to determine target
inn1_totals = defaultdict(int)
with open(os.path.join(DATA_DIR, 'ball_by_ball.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r['innings'] == '1':
            m_id = r['match_id']
            b_runs = int(r['runs'] or 0)
            ex1 = int(r['extras1_runs'] or 0)
            ex2 = int(r['extras_2_runs'] or 0)
            inn1_totals[m_id] += (b_runs + ex1 + ex2)

print(f"Loaded {len(matches)} matches across {len(competitions)} competitions.")

# 4. Aggregators
batters = defaultdict(lambda: {
    'name': '',
    'balls_base': 0, 'runs_base': 0, 'outs_base': 0, 'fours_base': 0, 'sixes_base': 0, 'dots_base': 0,
    'balls_press': 0, 'runs_press': 0, 'outs_press': 0, 'fours_press': 0, 'sixes_press': 0, 'dots_press': 0,
    'matches': set(), 'ipl_balls': 0, 't20i_balls': 0
})

bowlers = defaultdict(lambda: {
    'name': '',
    'balls_base': 0, 'runs_base': 0, 'wkts_base': 0, 'dots_base': 0,
    'balls_press': 0, 'runs_press': 0, 'wkts_press': 0, 'dots_press': 0,
    'matches': set(), 'ipl_balls': 0, 't20i_balls': 0
})

state = defaultdict(lambda: {'runs': 0, 'wickets': 0, 'legal_balls': 0})
valid_dismissals = {'Bowled', 'Caught', 'LBW', 'Stumped', 'Caught and Bowled', 'Hit Wicket'}

total_deliveries = 0
pressure_deliveries = 0

with open(os.path.join(DATA_DIR, 'ball_by_ball.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        total_deliveries += 1
        m_id = r['match_id']
        inn = r['innings']
        over = int(r['overid'])
        m_meta = matches.get(m_id, {})
        c_meta = competitions.get(m_meta.get('comp_id', ''), {})
        is_ipl = 'IPL' in c_meta.get('comp_name', '')
        is_ko = m_meta.get('knock_out') == '1' or m_meta.get('stage') in ('Semi Final', 'Qualifier', 'Final', 'Eliminator')
        
        st = state[(m_id, inn)]
        cur_runs = st['runs']
        cur_wkts = st['wickets']
        balls_bowled = st['legal_balls']
        
        # High Pressure Criteria:
        # 1. Death Overs (16-20)
        # 2. 2nd Innings Chasing: RRR >= 10.0 OR (balls_remaining <= 30 and runs_needed > 25) OR wickets >= 5
        # 3. 1st Innings Collapse: Over <= 6 with >= 3 wickets lost
        # 4. Knockout Crunch: Over >= 12 in knockout match
        is_pressure = False
        if over >= 16:
            is_pressure = True
        elif inn == '2':
            targ = int(m_meta.get('revised_target') or 0) or (inn1_totals[m_id] + 1)
            runs_needed = max(0, targ - cur_runs)
            balls_rem = max(1, 120 - balls_bowled)
            rrr = (runs_needed * 6.0) / balls_rem
            if rrr >= 10.0 or (balls_rem <= 30 and runs_needed >= 25) or cur_wkts >= 5:
                is_pressure = True
        elif inn == '1' and over <= 6 and cur_wkts >= 3:
            is_pressure = True
            
        if is_ko and over >= 12:
            is_pressure = True
            
        if is_pressure:
            pressure_deliveries += 1
            
        striker_id = r['striker_id']
        striker_name = r['striker_name']
        bowler_id = r['bowler_id']
        bowler_name = r['bowler_name']
        
        b_runs = int(r['runs'] or 0)
        ex_type = r['extras_type']
        ex1 = int(r['extras1_runs'] or 0)
        ex2 = int(r['extras_2_runs'] or 0)
        is_wkt = (r['is_wicket'] == 'true')
        d_type = r['dismissal_type']
        d_pid = r['dismissed_player_id']
        is_legal = (ex_type not in ('wide', 'Overstep'))
        
        # Batter Stats
        bst = batters[striker_id]
        bst['name'] = striker_name
        bst['matches'].add(m_id)
        if ex_type != 'wide':
            bst['balls_base'] += 1
            bst['runs_base'] += b_runs
            if b_runs == 0: bst['dots_base'] += 1
            if r['is_four'] == 'true': bst['fours_base'] += 1
            if r['is_six'] == 'true': bst['sixes_base'] += 1
            if is_ipl: bst['ipl_balls'] += 1
            else: bst['t20i_balls'] += 1
            
            if is_pressure:
                bst['balls_press'] += 1
                bst['runs_press'] += b_runs
                if b_runs == 0: bst['dots_press'] += 1
                if r['is_four'] == 'true': bst['fours_press'] += 1
                if r['is_six'] == 'true': bst['sixes_press'] += 1
                
        if is_wkt and d_pid == striker_id:
            bst['outs_base'] += 1
            if is_pressure:
                bst['outs_press'] += 1
                
        # Bowler Stats
        wst = bowlers[bowler_id]
        wst['name'] = bowler_name
        wst['matches'].add(m_id)
        bowler_conceded = b_runs
        if ex_type in ('wide', 'Overstep', 'other', 'Penalty'):
            bowler_conceded += (ex1 + ex2)
            
        wst['runs_base'] += bowler_conceded
        if is_pressure:
            wst['runs_press'] += bowler_conceded
            
        if is_legal:
            wst['balls_base'] += 1
            if bowler_conceded == 0:
                wst['dots_base'] += 1
            if is_ipl: wst['ipl_balls'] += 1
            else: wst['t20i_balls'] += 1
            
            if is_pressure:
                wst['balls_press'] += 1
                if bowler_conceded == 0:
                    wst['dots_press'] += 1
                    
        if is_wkt and d_type in valid_dismissals:
            wst['wkts_base'] += 1
            if is_pressure:
                wst['wkts_press'] += 1
                
        # State update
        st['runs'] += (b_runs + ex1 + ex2)
        if is_wkt: st['wickets'] += 1
        if is_legal: st['legal_balls'] += 1

print(f"Processed {total_deliveries} deliveries. Pressure deliveries: {pressure_deliveries} ({pressure_deliveries/total_deliveries*100:.1f}%)")

# Filter and calculate rankings
# Minimum sample sizes:
# Batters: >= 120 pressure balls, >= 250 base balls
# Bowlers: >= 120 pressure balls, >= 250 base balls

batter_rankings = []
for pid, b in batters.items():
    if b['balls_press'] >= 100 and b['balls_base'] >= 200:
        sr_base = (b['runs_base'] / b['balls_base']) * 100.0
        sr_press = (b['runs_press'] / b['balls_press']) * 100.0
        avg_base = b['runs_base'] / max(1, b['outs_base'])
        avg_press = b['runs_press'] / max(1, b['outs_press'])
        bnd_press = (b['fours_press'] + b['sixes_press']) / b['balls_press'] * 100.0
        dot_press = (b['dots_press'] / b['balls_press']) * 100.0
        
        # Reliability Index (BRS - Batting Reliability Score):
        # 1. High Strike Rate under pressure (40%)
        # 2. Avg under pressure / survivability (25%)
        # 3. Strike Rate delta vs baseline (SR_press - SR_base) (20%)
        # 4. Low dot ball % under pressure (15%)
        brs = (sr_press * 0.40) + (avg_press * 0.40) + ((sr_press - sr_base) * 0.35) + ((40.0 - dot_press) * 0.5)
        
        batter_rankings.append({
            'player_id': pid,
            'name': b['name'],
            'matches': len(b['matches']),
            'balls_press': b['balls_press'],
            'runs_press': b['runs_press'],
            'outs_press': b['outs_press'],
            'sr_press': round(sr_press, 2),
            'sr_base': round(sr_base, 2),
            'avg_press': round(avg_press, 2),
            'avg_base': round(avg_base, 2),
            'bnd_pct_press': round(bnd_press, 1),
            'dot_pct_press': round(dot_press, 1),
            'sr_delta': round(sr_press - sr_base, 2),
            'score': round(brs, 2),
            'ipl_ratio': round(b['ipl_balls'] / b['balls_base'] * 100, 1)
        })

batter_rankings.sort(key=lambda x: x['score'], reverse=True)

bowler_rankings = []
for pid, w in bowlers.items():
    if w['balls_press'] >= 100 and w['balls_base'] >= 200:
        econ_base = (w['runs_base'] / (w['balls_base'] / 6.0))
        econ_press = (w['runs_press'] / (w['balls_press'] / 6.0))
        dot_pct_press = (w['dots_press'] / w['balls_press']) * 100.0
        dot_pct_base = (w['dots_base'] / w['balls_base']) * 100.0
        wkt_sr_press = w['balls_press'] / max(1, w['wkts_press'])
        wkt_per_over = (w['wkts_press'] / (w['balls_press'] / 6.0))
        
        # Bowling Reliability Score (WRS):
        # Average pressure T20 economy is ~10.5. Delivering lower economy is huge.
        # WRS considers:
        # 1. Economy under pressure (e.g., 12.0 - econ_press) * 8
        # 2. Economy improvement over typical pressure baseline
        # 3. Wickets taken under pressure (wkts * 3.0)
        # 4. Dot ball % under pressure (dot_pct * 0.7)
        # 5. Delta economy vs bowler's base
        wrs = ((12.0 - econ_press) * 7.5) + (w['wkts_press'] * 2.2) + (dot_pct_press * 0.6) + ((econ_base - econ_press) * 3.5)
        
        bowler_rankings.append({
            'player_id': pid,
            'name': w['name'],
            'matches': len(w['matches']),
            'balls_press': w['balls_press'],
            'runs_press': w['runs_press'],
            'wkts_press': w['wkts_press'],
            'econ_press': round(econ_press, 2),
            'econ_base': round(econ_base, 2),
            'dot_pct_press': round(dot_pct_press, 1),
            'dot_pct_base': round(dot_pct_base, 1),
            'wkt_sr_press': round(wkt_sr_press, 1),
            'econ_delta': round(econ_base - econ_press, 2),
            'score': round(wrs, 2),
            'ipl_ratio': round(w['ipl_balls'] / w['balls_base'] * 100, 1)
        })

bowler_rankings.sort(key=lambda x: x['score'], reverse=True)

# Save result to json
summary = {
    'total_deliveries': total_deliveries,
    'pressure_deliveries': pressure_deliveries,
    'total_matches': len(matches),
    'top_batters': batter_rankings[:25],
    'top_bowlers': bowler_rankings[:25],
    'all_qualified_batters_count': len(batter_rankings),
    'all_qualified_bowlers_count': len(bowler_rankings)
}

with open('pressure_metrics.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)

print("\n=== TOP 10 BATTERS UNDER PRESSURE ===")
for i, b in enumerate(batter_rankings[:10], 1):
    print(f"{i:2d}. {b['name']:<22} | Score: {b['score']:6.2f} | Press SR: {b['sr_press']:6.2f} (Base: {b['sr_base']:6.2f}) | Press Avg: {b['avg_press']:5.2f} | Balls: {b['balls_press']}")

print("\n=== TOP 10 BOWLERS UNDER PRESSURE ===")
for i, w in enumerate(bowler_rankings[:10], 1):
    print(f"{i:2d}. {w['name']:<22} | Score: {w['score']:6.2f} | Press Econ: {w['econ_press']:5.2f} (Base: {w['econ_base']:5.2f}) | Wkts: {w['wkts_press']:2d} | Dot%: {w['dot_pct_press']:4.1f}% | Balls: {w['balls_press']}")

