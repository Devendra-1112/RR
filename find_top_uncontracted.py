import csv
import json
import math
from collections import defaultdict

# 1. Load competitions & matches
competitions = {}
with open('Data Pack/competitions.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        competitions[r['comp_id']] = r

matches = {}
with open('Data Pack/matches.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        matches[r['match_id']] = r

# 2. IPL 2026 player set
ipl_2026_players = set()
with open('Data Pack/competition_team_player_mapping.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r['comp_id'] == '3298':
            ipl_2026_players.add(r['player_name'])

print("Total IPL 2026 contracted players:", len(ipl_2026_players))

# Also check retired players
retired_players = {'Shikhar Dhawan', 'Dinesh Karthik'}

# Innings 1 totals
inn1_totals = defaultdict(int)
with open('Data Pack/ball_by_ball.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r['innings'] == '1':
            inn1_totals[r['match_id']] += int(r['runs'] or 0) + int(r['extras1_runs'] or 0) + int(r['extras_2_runs'] or 0)

# Stats collectors
batters = defaultdict(lambda: {'balls': 0, 'runs': 0, 'outs': 0, 'p_balls': 0, 'p_runs': 0, 'p_outs': 0, 'p_dots': 0, 'p_fours': 0, 'p_sixes': 0})
bowlers = defaultdict(lambda: {'legal_balls': 0, 'runs_conceded': 0, 'wickets': 0, 'p_balls': 0, 'p_runs': 0, 'p_wickets': 0, 'p_dots': 0})
valid_dismissals = {'Bowled', 'Caught', 'LBW', 'Stumped', 'Caught and Bowled', 'Hit Wicket'}
state = defaultdict(lambda: {'runs': 0, 'wickets': 0, 'legal_balls': 0})

with open('Data Pack/ball_by_ball.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        m_id = r['match_id']
        inn = r['innings']
        over = int(r['overid'])
        m_meta = matches.get(m_id, {})
        is_ko = m_meta.get('knock_out') == '1'
        
        st = state[(m_id, inn)]
        cur_runs = st['runs']
        cur_wkts = st['wickets']
        balls_bowled = st['legal_balls']
        
        is_pressure = False
        if over >= 16:
            if inn == '1': is_pressure = True
            elif inn == '2':
                targ = int(m_meta.get('revised_target') or 0) or (inn1_totals[m_id] + 1)
                runs_needed = max(0, targ - cur_runs)
                if runs_needed > 5 and cur_wkts < 10: is_pressure = True
        elif inn == '2':
            targ = int(m_meta.get('revised_target') or 0) or (inn1_totals[m_id] + 1)
            runs_needed = max(0, targ - cur_runs)
            balls_rem = max(1, 120 - balls_bowled)
            rrr = (runs_needed * 6.0) / balls_rem
            if (rrr >= 9.8) or (balls_rem <= 36 and runs_needed >= 35) or (cur_wkts >= 5 and runs_needed > 20):
                is_pressure = True
        elif inn == '1' and over <= 6 and cur_wkts >= 3:
            is_pressure = True
        if is_ko and over >= 12:
            is_pressure = True
            
        striker = r['striker_name']
        bowler = r['bowler_name']
        b_runs = int(r['runs'] or 0)
        ex_type = r['extras_type']
        ex1 = int(r['extras1_runs'] or 0)
        ex2 = int(r['extras_2_runs'] or 0)
        is_wkt = (r['is_wicket'] == 'true')
        d_type = r['dismissal_type']
        d_pid = r['dismissed_player_id']
        is_legal = (ex_type not in ('wide', 'Overstep'))
        total_ball_runs = b_runs + ex1 + ex2
        
        bst = batters[striker]
        if ex_type != 'wide':
            bst['balls'] += 1
            bst['runs'] += b_runs
            if is_pressure:
                bst['p_balls'] += 1
                bst['p_runs'] += b_runs
                if b_runs == 0: bst['p_dots'] += 1
                if r['is_four'] == 'true': bst['p_fours'] += 1
                if r['is_six'] == 'true': bst['p_sixes'] += 1
        if is_wkt and d_pid == r['striker_id']:
            bst['outs'] += 1
            if is_pressure: bst['p_outs'] += 1
            
        wst = bowlers[bowler]
        runs_charged = b_runs + (ex1 + ex2 if ex_type in ('wide', 'Overstep', 'other', 'Penalty') else 0)
        wst['runs_conceded'] += runs_charged
        if is_legal:
            wst['legal_balls'] += 1
            if is_pressure:
                wst['p_balls'] += 1
                wst['p_runs'] += runs_charged
                if runs_charged == 0: wst['p_dots'] += 1
        if is_wkt and d_type in valid_dismissals:
            wst['wickets'] += 1
            if is_pressure: wst['p_wickets'] += 1
            
        st['runs'] += total_ball_runs
        if is_wkt: st['wickets'] += 1
        if is_legal: st['legal_balls'] += 1

# Filter uncontracted batters (not in ipl_2026_players and not retired)
uncontracted_batters = []
for pname, b in batters.items():
    if pname not in ipl_2026_players and pname not in retired_players and b['balls'] >= 80 and b['p_balls'] >= 25 and b['runs'] >= 150:
        sr_overall = (b['runs'] / b['balls']) * 100.0
        avg_overall = b['runs'] / max(1, b['outs'])
        sr_press = (b['p_runs'] / b['p_balls']) * 100.0
        avg_press = b['p_runs'] / max(1, b['p_outs'])
        sr_delta = sr_press - sr_overall
        dot_pct_press = (b['p_dots'] / b['p_balls']) * 100.0
        
        # Ensure genuine batting ability
        if sr_press >= 130.0 or avg_press >= 20.0:
            sample_factor = min(1.0, math.sqrt(b['p_balls'] / 180.0))
            raw_ppi = (sr_press * 0.35) + (avg_press * 0.35) + (sr_delta * 0.35) + ((40.0 - dot_pct_press) * 0.40)
            ppi_score = round(raw_ppi * (0.7 + 0.3 * sample_factor), 2)
            uncontracted_batters.append({
                'name': pname, 'ppi': ppi_score, 'p_sr': round(sr_press, 2), 'p_avg': round(avg_press, 2),
                'p_balls': b['p_balls'], 'p_runs': b['p_runs'], 'dot_pct': round(dot_pct_press, 1)
            })

uncontracted_batters.sort(key=lambda x: x['ppi'], reverse=True)
print("\n=== TOP 15 UNCONTRACTED BATTERS (NOT IN ANY IPL TEAM) ===")
for i, b in enumerate(uncontracted_batters[:15], 1):
    print(f"{i}. {b['name']} | PPI: {b['ppi']} | SR: {b['p_sr']} | Avg: {b['p_avg']} | Balls: {b['p_balls']}")

# Filter uncontracted bowlers (not in ipl_2026_players and not retired)
uncontracted_bowlers = []
for pname, w in bowlers.items():
    if pname not in ipl_2026_players and pname not in retired_players and w['legal_balls'] >= 80 and w['p_balls'] >= 25 and w['p_wickets'] >= 3:
        econ_overall = (w['runs_conceded'] / (w['legal_balls'] / 6.0))
        econ_press = (w['p_runs'] / (w['p_balls'] / 6.0))
        econ_delta = econ_overall - econ_press
        dot_pct_press = (w['p_dots'] / w['p_balls']) * 100.0
        
        sample_factor = min(1.0, math.sqrt(w['p_balls'] / 180.0))
        raw_ppi = ((12.0 - econ_press) * 7.0) + (w['p_wickets'] * 2.0) + (dot_pct_press * 0.6) + (econ_delta * 3.0)
        ppi_score = round(raw_ppi * (0.7 + 0.3 * sample_factor), 2)
        uncontracted_bowlers.append({
            'name': pname, 'ppi': ppi_score, 'p_econ': round(econ_press, 2), 'p_wkts': w['p_wickets'],
            'p_balls': w['p_balls'], 'dot_pct': round(dot_pct_press, 1)
        })

uncontracted_bowlers.sort(key=lambda x: x['ppi'], reverse=True)
print("\n=== TOP 15 UNCONTRACTED BOWLERS (NOT IN ANY IPL TEAM) ===")
for i, w in enumerate(uncontracted_bowlers[:15], 1):
    print(f"{i}. {w['name']} | PPI: {w['ppi']} | Econ: {w['p_econ']} | Wkts: {w['p_wkts']} | Balls: {w['p_balls']}")
