import csv
import json
import math
from collections import defaultdict

with open('ipl2027_official_teams_database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

retained = {r['player_name'].strip() for r in db['all_retained_players']}
pak_players = set()
with open('Data Pack/competition_team_player_mapping.csv', 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if 'Pakistan' in r['team_name']:
            pak_players.add(r['player_name'].strip())

retired_players = {
    'Dinesh Karthik', 'Shikhar Dhawan', 'Ambati Rayudu', 'Kedar Jadhav', 'Suresh Raina',
    'Dwayne Bravo', 'Kieron Pollard', 'Robin Uthappa', 'Murali Vijay', 'Wriddhiman Saha',
    'Eoin Morgan', 'Shane Watson', 'AB de Villiers', 'Chris Gayle'
}

ipl_teams_map = defaultdict(set)
with open('Data Pack/competition_team_player_mapping.csv', 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        p = r['player_name'].strip()
        t = r['team_name']
        if any(ipl_t in t for ipl_t in ['Chennai', 'Mumbai', 'Rajasthan', 'Punjab', 'Bengaluru', 'Delhi', 'Kolkata', 'Hyderabad', 'Gujarat', 'Lucknow']):
            ipl_teams_map[p].add(t)

matches = {}
with open('Data Pack/matches.csv', 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        matches[r['match_id']] = r

competitions = {}
with open('Data Pack/competitions.csv', 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        competitions[r['comp_id']] = r

b_stats = defaultdict(lambda: {'runs': 0, 'balls': 0, 'outs': 0, 'dots': 0, 'p_balls': 0, 'p_runs': 0, 'p_outs': 0, 'p_dots': 0, 'ipl_balls': 0, 'ipl_runs': 0})
w_stats = defaultdict(lambda: {'legal_balls': 0, 'runs': 0, 'wkts': 0, 'dots': 0, 'p_balls': 0, 'p_runs': 0, 'p_wkts': 0, 'p_dots': 0, 'ipl_balls': 0, 'ipl_wkts': 0, 'ipl_runs': 0})

valid_dismissals = {'Bowled', 'Caught', 'LBW', 'Stump', 'Hit Wicket'}

with open('Data Pack/ball_by_ball.csv', 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        m_id = r['match_id']
        inn = r['innings']
        over = int(r['overid'])
        cname = competitions.get(matches.get(m_id, {}).get('comp_id', ''), {}).get('comp_name', '')
        is_ipl = 'IPL' in cname
        
        is_pressure = (over >= 16) or (inn == '2' and over >= 12)
        
        s_name = r['striker_name']
        w_name = r['bowler_name']
        runs = int(r['runs'] or 0)
        ex_type = r['extras_type']
        ex1 = int(r['extras1_runs'] or 0)
        ex2 = int(r['extras_2_runs'] or 0)
        is_wkt = (r['is_wicket'] == 'true')
        d_type = r['dismissal_type']
        d_pid = r['dismissed_player_id']
        is_legal = (ex_type not in ('wide', 'Overstep'))
        
        if ex_type != 'wide':
            bs = b_stats[s_name]
            bs['balls'] += 1
            bs['runs'] += runs
            if runs == 0: bs['dots'] += 1
            if is_ipl:
                bs['ipl_balls'] += 1
                bs['ipl_runs'] += runs
            if is_pressure:
                bs['p_balls'] += 1
                bs['p_runs'] += runs
                if runs == 0: bs['p_dots'] += 1
                
        if is_wkt and d_pid == r['striker_id']:
            b_stats[s_name]['outs'] += 1
            if is_pressure: b_stats[s_name]['p_outs'] += 1
            
        ws = w_stats[w_name]
        runs_c = runs + (ex1 + ex2 if ex_type in ('wide', 'Overstep') else 0)
        ws['runs'] += runs_c
        if is_ipl: ws['ipl_runs'] += runs_c
        
        if is_legal:
            ws['legal_balls'] += 1
            if runs_c == 0: ws['dots'] += 1
            if is_ipl: ws['ipl_balls'] += 1
            if is_pressure:
                ws['p_balls'] += 1
                ws['p_runs'] += runs_c
                if runs_c == 0: ws['p_dots'] += 1
                
        if is_wkt and d_type in valid_dismissals:
            ws['wkts'] += 1
            if is_ipl: ws['ipl_wkts'] += 1
            if is_pressure: ws['p_wkts'] += 1

candidate_batters = []
for p, s in b_stats.items():
    if p in retained or p in pak_players or p in retired_players:
        continue
    if p not in ipl_teams_map:
        continue
    if s['ipl_balls'] < 60 or s['p_balls'] < 30:
        continue
    base_sr = (s['runs'] / s['balls']) * 100
    p_sr = (s['p_runs'] / max(1, s['p_balls'])) * 100
    p_avg = (s['p_runs'] / max(1, s['p_outs']))
    p_dot = (s['p_dots'] / max(1, s['p_balls'])) * 100
    s_factor = min(1.0, math.sqrt(s['p_balls'] / 100.0))
    raw_ppi = (0.35 * p_sr) + (0.35 * p_avg) + (0.30 * (p_sr - base_sr)) + (0.40 * max(0.0, 40.0 - p_dot))
    ppi = raw_ppi * s_factor
    candidate_batters.append({
        'name': p, 'teams': list(ipl_teams_map[p]), 'ppi': round(ppi, 2),
        'p_sr': round(p_sr, 1), 'p_avg': round(p_avg, 1), 'p_balls': s['p_balls'],
        'ipl_balls': s['ipl_balls'], 'ipl_runs': s['ipl_runs']
    })

candidate_batters.sort(key=lambda x: x['ppi'], reverse=True)
print('\n--- TOP CANDIDATE ELIGIBLE BATSMEN ---')
for idx, b in enumerate(candidate_batters[:25], 1):
    print(f"{idx}. {b['name']} ({b['teams'][0]}) - PPI: {b['ppi']} | Press SR: {b['p_sr']} | Press Avg: {b['p_avg']} | IPL Runs: {b['ipl_runs']} | Press Balls: {b['p_balls']}")

candidate_bowlers = []
for p, s in w_stats.items():
    if p in retained or p in pak_players or p in retired_players:
        continue
    if p not in ipl_teams_map:
        continue
    if s['ipl_balls'] < 60 or s['p_balls'] < 30:
        continue
    base_econ = (s['runs'] * 6.0) / max(1, s['legal_balls'])
    p_econ = (s['p_runs'] * 6.0) / max(1, s['p_balls'])
    p_wkts = s['p_wkts']
    p_dot = (s['p_dots'] / max(1, s['p_balls'])) * 100
    s_factor = min(1.0, math.sqrt(s['p_balls'] / 80.0))
    raw_ppi = (7.0 * max(0.0, 12.0 - p_econ)) + (2.0 * p_wkts) + (0.6 * p_dot) + (3.0 * (base_econ - p_econ))
    ppi = raw_ppi * s_factor
    candidate_bowlers.append({
        'name': p, 'teams': list(ipl_teams_map[p]), 'ppi': round(ppi, 2),
        'p_econ': round(p_econ, 2), 'p_wkts': p_wkts, 'p_balls': s['p_balls'],
        'ipl_balls': s['ipl_balls'], 'ipl_wkts': s['ipl_wkts']
    })

candidate_bowlers.sort(key=lambda x: x['ppi'], reverse=True)
print('\n--- TOP CANDIDATE ELIGIBLE BOWLERS ---')
for idx, w in enumerate(candidate_bowlers[:25], 1):
    print(f"{idx}. {w['name']} ({w['teams'][0]}) - PPI: {w['ppi']} | Press Econ: {w['p_econ']} | Press Wkts: {w['p_wkts']} | IPL Wkts: {w['ipl_wkts']} | Press Balls: {w['p_balls']}")
