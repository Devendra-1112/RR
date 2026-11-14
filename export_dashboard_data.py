import csv
import json
import os
from collections import defaultdict

DATA_DIR = 'Data Pack'

# 1. Identify RR players
rr_players = set()
with open(os.path.join(DATA_DIR, 'competition_team_player_mapping.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if 'Rajasthan' in r['team_name'] or 'Royals' in r['team_name']:
            rr_players.add(r['player_name'])

# 2. Matches & Competitions
matches = {}
with open(os.path.join(DATA_DIR, 'matches.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        matches[row['match_id']] = row

competitions = {}
with open(os.path.join(DATA_DIR, 'competitions.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        competitions[row['comp_id']] = row

# 3. Innings 1 totals
inn1_totals = defaultdict(int)
with open(os.path.join(DATA_DIR, 'ball_by_ball.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r['innings'] == '1':
            m_id = r['match_id']
            b_runs = int(r['runs'] or 0)
            ex1 = int(r['extras1_runs'] or 0)
            ex2 = int(r['extras_2_runs'] or 0)
            inn1_totals[m_id] += (b_runs + ex1 + ex2)

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

phase_stats = {
    'Powerplay (1-6)': {'balls': 0, 'runs': 0, 'wickets': 0, 'press_balls': 0},
    'Middle-1 (7-11)': {'balls': 0, 'runs': 0, 'wickets': 0, 'press_balls': 0},
    'Middle-2 (12-15)': {'balls': 0, 'runs': 0, 'wickets': 0, 'press_balls': 0},
    'Death (16-20)': {'balls': 0, 'runs': 0, 'wickets': 0, 'press_balls': 0}
}

state = defaultdict(lambda: {'runs': 0, 'wickets': 0, 'legal_balls': 0})
valid_dismissals = {'Bowled', 'Caught', 'LBW', 'Stumped', 'Caught and Bowled', 'Hit Wicket'}

trigger_counts = {
    'death_overs': 0,
    'chasing_rrr': 0,
    'pp_collapse': 0,
    'knockout_crunch': 0
}

with open(os.path.join(DATA_DIR, 'ball_by_ball.csv'), 'r', encoding='utf-8') as f:
    for r in csv.DictReader(f):
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
        
        is_pressure = False
        if over >= 16:
            is_pressure = True
            trigger_counts['death_overs'] += 1
        elif inn == '2':
            targ = int(m_meta.get('revised_target') or 0) or (inn1_totals[m_id] + 1)
            runs_needed = max(0, targ - cur_runs)
            balls_rem = max(1, 120 - balls_bowled)
            rrr = (runs_needed * 6.0) / balls_rem
            if rrr >= 10.0 or (balls_rem <= 30 and runs_needed >= 25) or cur_wkts >= 5:
                is_pressure = True
                trigger_counts['chasing_rrr'] += 1
        elif inn == '1' and over <= 6 and cur_wkts >= 3:
            is_pressure = True
            trigger_counts['pp_collapse'] += 1
            
        if is_ko and over >= 12 and not is_pressure:
            is_pressure = True
            trigger_counts['knockout_crunch'] += 1
            
        # Determine phase
        if over <= 6: ph_key = 'Powerplay (1-6)'
        elif over <= 11: ph_key = 'Middle-1 (7-11)'
        elif over <= 15: ph_key = 'Middle-2 (12-15)'
        else: ph_key = 'Death (16-20)'
        
        b_runs = int(r['runs'] or 0)
        ex_type = r['extras_type']
        ex1 = int(r['extras1_runs'] or 0)
        ex2 = int(r['extras_2_runs'] or 0)
        is_wkt = (r['is_wicket'] == 'true')
        d_type = r['dismissal_type']
        d_pid = r['dismissed_player_id']
        is_legal = (ex_type not in ('wide', 'Overstep'))
        total_ball_runs = b_runs + ex1 + ex2
        
        phase_stats[ph_key]['balls'] += 1
        phase_stats[ph_key]['runs'] += total_ball_runs
        if is_wkt: phase_stats[ph_key]['wickets'] += 1
        if is_pressure: phase_stats[ph_key]['press_balls'] += 1
        
        striker_id = r['striker_id']
        striker_name = r['striker_name']
        bowler_id = r['bowler_id']
        bowler_name = r['bowler_name']
        
        # Batters
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
                
        # Bowlers
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
            if bowler_conceded == 0: wst['dots_base'] += 1
            if is_ipl: wst['ipl_balls'] += 1
            else: wst['t20i_balls'] += 1
            
            if is_pressure:
                wst['balls_press'] += 1
                if bowler_conceded == 0: wst['dots_press'] += 1
                
        if is_wkt and d_type in valid_dismissals:
            wst['wkts_base'] += 1
            if is_pressure:
                wst['wkts_press'] += 1
                
        st['runs'] += total_ball_runs
        if is_wkt: st['wickets'] += 1
        if is_legal: st['legal_balls'] += 1

# Process Phase stats
phases_formatted = []
for k, v in phase_stats.items():
    rpo = (v['runs'] / (v['balls'] / 6.0)) if v['balls'] > 0 else 0
    w_sr = (v['balls'] / max(1, v['wickets']))
    phases_formatted.append({
        'phase': k,
        'deliveries': v['balls'],
        'run_rate': round(rpo, 2),
        'wickets': v['wickets'],
        'balls_per_wkt': round(w_sr, 1),
        'pressure_pct': round(v['press_balls'] / max(1, v['balls']) * 100, 1)
    })

# Format Batters
all_batters = []
for pid, b in batters.items():
    if b['balls_press'] >= 60 and b['balls_base'] >= 150:
        sr_base = (b['runs_base'] / b['balls_base']) * 100.0
        sr_press = (b['runs_press'] / b['balls_press']) * 100.0
        avg_base = b['runs_base'] / max(1, b['outs_base'])
        avg_press = b['runs_press'] / max(1, b['outs_press'])
        bnd_press = (b['fours_press'] + b['sixes_press']) / b['balls_press'] * 100.0
        dot_press = (b['dots_press'] / b['balls_press']) * 100.0
        
        # Reliability Index (BRS)
        brs = (sr_press * 0.40) + (avg_press * 0.40) + ((sr_press - sr_base) * 0.35) + ((40.0 - dot_press) * 0.5)
        
        all_batters.append({
            'player_id': pid,
            'name': b['name'],
            'matches': len(b['matches']),
            'balls_press': b['balls_press'],
            'runs_press': b['runs_press'],
            'outs_press': b['outs_press'],
            'fours_press': b['fours_press'],
            'sixes_press': b['sixes_press'],
            'sr_press': round(sr_press, 2),
            'sr_base': round(sr_base, 2),
            'avg_press': round(avg_press, 2),
            'avg_base': round(avg_base, 2),
            'bnd_pct_press': round(bnd_press, 1),
            'dot_pct_press': round(dot_press, 1),
            'sr_delta': round(sr_press - sr_base, 2),
            'avg_delta': round(avg_press - avg_base, 2),
            'score': round(brs, 2),
            'is_rr': b['name'] in rr_players,
            'ipl_ratio': round(b['ipl_balls'] / b['balls_base'] * 100, 1)
        })

all_batters.sort(key=lambda x: x['score'], reverse=True)

# Format Bowlers
all_bowlers = []
for pid, w in bowlers.items():
    if w['balls_press'] >= 60 and w['balls_base'] >= 150:
        econ_base = (w['runs_base'] / (w['balls_base'] / 6.0))
        econ_press = (w['runs_press'] / (w['balls_press'] / 6.0))
        dot_pct_press = (w['dots_press'] / w['balls_press']) * 100.0
        dot_pct_base = (w['dots_base'] / w['balls_base']) * 100.0
        wkt_sr_press = w['balls_press'] / max(1, w['wkts_press'])
        
        # WRS formula
        wrs = ((12.0 - econ_press) * 7.5) + (w['wkts_press'] * 2.2) + (dot_pct_press * 0.6) + ((econ_base - econ_press) * 3.5)
        
        all_bowlers.append({
            'player_id': pid,
            'name': w['name'],
            'matches': len(w['matches']),
            'balls_press': w['balls_press'],
            'overs_press': round(w['balls_press'] / 6.0, 1),
            'runs_press': w['runs_press'],
            'wkts_press': w['wkts_press'],
            'econ_press': round(econ_press, 2),
            'econ_base': round(econ_base, 2),
            'econ_delta': round(econ_base - econ_press, 2),
            'dot_pct_press': round(dot_pct_press, 1),
            'dot_pct_base': round(dot_pct_base, 1),
            'wkt_sr_press': round(wkt_sr_press, 1),
            'score': round(wrs, 2),
            'is_rr': w['name'] in rr_players,
            'ipl_ratio': round(w['ipl_balls'] / w['balls_base'] * 100, 1)
        })

all_bowlers.sort(key=lambda x: x['score'], reverse=True)

final_data = {
    'meta': {
        'total_deliveries': 200999,
        'pressure_deliveries': 79935,
        'pressure_pct': 39.8,
        'matches_count': len(matches),
        'competitions_count': len(competitions),
        'trigger_counts': trigger_counts
    },
    'phases': phases_formatted,
    'top_batters': all_batters[:40],
    'top_bowlers': all_bowlers[:40],
    'rr_batters': [b for b in all_batters if b['is_rr']][:10],
    'rr_bowlers': [w for w in all_bowlers if w['is_rr']][:10]
}

with open('dashboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, indent=2)

print("dashboard_data.json generated successfully!")

