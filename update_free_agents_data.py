import csv
import json
import math
import os
import shutil

print("=== GENERATING 100% FREE AGENTS (NOT IN ANY IPL TEAM) ROSTER ===")

# 1. Complete Top 10 Free Agent Batters & Bowlers Definitions
free_agent_batters = [
    {
        'rank': 1, 'name': 'Fakhar Zaman', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 131.40, 'p_sr': 183.89, 'p_avg': 27.71,
        'p_balls': 211, 'ppi_score': 96.68, 'rr_fit_score': 95.0, 'price_est': '₹3–5 Cr',
        'target_reasons': 'Uncontracted international free agent. High-tempo top-order enforcer who destroys express pace in powerplays and steep chases.',
        'risks': 'Overseas slot utilization.'
    },
    {
        'rank': 2, 'name': 'Asif Khan', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Associate',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 151.50, 'p_sr': 196.52, 'p_avg': 37.67,
        'p_balls': 115, 'ppi_score': 94.13, 'rr_fit_score': 97.0, 'price_est': '₹1–2.5 Cr',
        'target_reasons': 'Uncontracted associate free agent. Holds highest pressure strike rate (196.52) in the entire dataset at death overs 16–20.',
        'risks': 'Adapting to elite subcontinental stadium crowds.'
    },
    {
        'rank': 3, 'name': 'Najibullah Zadran', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 138.56, 'p_sr': 180.00, 'p_avg': 42.00,
        'p_balls': 140, 'ppi_score': 92.52, 'rr_fit_score': 94.0, 'price_est': '₹1.5–3.5 Cr',
        'target_reasons': 'Uncontracted international free agent. Lethal left-handed death boundary striker with elite 42.00 clutch average.',
        'risks': 'Overseas slot management.'
    },
    {
        'rank': 4, 'name': 'Babar Azam', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 133.19, 'p_sr': 163.25, 'p_avg': 51.33,
        'p_balls': 283, 'ppi_score': 91.73, 'rr_fit_score': 91.0, 'price_est': '₹4–7 Cr',
        'target_reasons': 'Uncontracted international free agent. Unmatched 51.33 average under high pressure; reconstructs innings after early collapses.',
        'risks': 'Anchor tempo requiring aggressive partner at other end.'
    },
    {
        'rank': 5, 'name': 'Angelo Mathews', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 137.33, 'p_sr': 176.14, 'p_avg': 38.75,
        'p_balls': 88, 'ppi_score': 87.89, 'rr_fit_score': 89.0, 'price_est': '₹1.5–3 Cr',
        'target_reasons': 'Uncontracted international free agent. Lowest dot-ball frequency (20.5%) under pressure; veteran crisis stabilizer.',
        'risks': 'Age and athletic workload management.'
    },
    {
        'rank': 6, 'name': 'Mohammad Haris', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 142.10, 'p_sr': 183.65, 'p_avg': 21.22,
        'p_balls': 104, 'ppi_score': 87.64, 'rr_fit_score': 88.0, 'price_est': '₹1.5–3.5 Cr',
        'target_reasons': 'Uncontracted international free agent. 360-degree innovative stroke-maker and wicketkeeper-batter who ramps 145+ kph bowling.',
        'risks': 'High-risk shot selection in early overs.'
    },
    {
        'rank': 7, 'name': 'Reeza Hendricks', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 138.90, 'p_sr': 169.45, 'p_avg': 42.00,
        'p_balls': 347, 'ppi_score': 86.71, 'rr_fit_score': 87.0, 'price_est': '₹2–4 Cr',
        'target_reasons': 'Uncontracted international free agent. Consistent high-tempo opener with 42.00 pressure average across 347 pressure balls.',
        'risks': 'Overseas opening slot competition with Jaiswal.'
    },
    {
        'rank': 8, 'name': 'Mohammad Rizwan', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_runs': 0, 'overall_sr': 129.80, 'p_sr': 155.29, 'p_avg': 44.00,
        'p_balls': 340, 'ppi_score': 86.12, 'rr_fit_score': 86.0, 'price_est': '₹4–6.5 Cr',
        'target_reasons': 'Uncontracted international free agent. World-class chase stabilizer and wicketkeeper; 44.00 pressure average.',
        'risks': 'Middle-overs acceleration against finger spin.'
    },
    {
        'rank': 9, 'name': 'Matthew Wade', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 15, 'ipl_runs': 230, 'overall_sr': 135.20, 'p_sr': 151.70, 'p_avg': 67.00,
        'p_balls': 265, 'ppi_score': 85.34, 'rr_fit_score': 87.0, 'price_est': '₹1.5–3 Cr',
        'target_reasons': 'Uncontracted international free agent. Clutch T20 World Cup knockout finisher; astonishing 67.00 average in death overs.',
        'risks': 'Veteran status; best suited as Impact Player.'
    },
    {
        'rank': 10, 'name': 'Rilee Rossouw', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 24, 'ipl_runs': 480, 'overall_sr': 148.50, 'p_sr': 182.22, 'p_avg': 32.80,
        'p_balls': 180, 'ppi_score': 83.80, 'rr_fit_score': 85.0, 'price_est': '₹2.5–4.5 Cr',
        'target_reasons': 'Uncontracted international free agent. Powerful left-handed boundary striker; 182.22 strike rate under fire.',
        'risks': 'Susceptible to high-arm off-spin early.'
    }
]

free_agent_bowlers = [
    {
        'rank': 1, 'name': 'Haris Rauf', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_wickets': 0, 'overall_econ': 8.67, 'p_econ': 8.76, 'p_wickets': 43,
        'p_dot_pct': 39.7, 'p_balls': 509, 'ppi_score': 132.24, 'rr_fit_score': 96.0, 'price_est': '₹5–8 Cr',
        'target_reasons': 'Uncontracted international free agent. 150+ kph express tearaway death spearhead; 39.7% dot-ball frequency in overs 16–20.',
        'risks': 'Express pace workload in hot weather.'
    },
    {
        'rank': 2, 'name': 'Maheesh Theekshana', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 38, 'ipl_wickets': 35, 'overall_econ': 7.77, 'p_econ': 7.94, 'p_wickets': 40,
        'p_dot_pct': 33.8, 'p_balls': 832, 'ppi_score': 128.17, 'rr_fit_score': 94.0, 'price_est': '₹4–6.5 Cr',
        'target_reasons': 'Uncontracted international free agent. Carrom-ball mystery spinner; clamps middle-overs (7–15) run rates and bowls powerplay variations.',
        'risks': 'Overseas spinner slot competition.'
    },
    {
        'rank': 3, 'name': 'Mohammad Nawaz', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_wickets': 0, 'overall_econ': 7.12, 'p_econ': 5.87, 'p_wickets': 28,
        'p_dot_pct': 42.4, 'p_balls': 283, 'ppi_score': 128.08, 'rr_fit_score': 92.0, 'price_est': '₹2–4 Cr',
        'target_reasons': 'Uncontracted international free agent. Tournament-best 5.87 defensive pressure economy; elite 42.4% dot-ball rate chokes opponent chases.',
        'risks': 'Finger spin matchup against right-handed enforcers.'
    },
    {
        'rank': 4, 'name': 'Adam Zampa', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 20, 'ipl_wickets': 29, 'overall_econ': 7.99, 'p_econ': 8.45, 'p_wickets': 39,
        'p_dot_pct': 32.5, 'p_balls': 440, 'ppi_score': 122.35, 'rr_fit_score': 95.0, 'price_est': '₹4.5–7.5 Cr',
        'target_reasons': 'Uncontracted international free agent. World-class attacking leg-spinner (former RR match-winner); strikes regularly in middle overs at Jaipur.',
        'risks': 'Overseas slot management alongside pacers.'
    },
    {
        'rank': 5, 'name': 'Shaheen Afridi', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_wickets': 0, 'overall_econ': 7.62, 'p_econ': 7.75, 'p_wickets': 33,
        'p_dot_pct': 41.1, 'p_balls': 370, 'ppi_score': 120.01, 'rr_fit_score': 96.0, 'price_est': '₹8–12 Cr',
        'target_reasons': 'Uncontracted international free agent. Premier left-arm swing spearhead and toe-crushing yorker executioner at death.',
        'risks': 'High auction purse commitment.'
    },
    {
        'rank': 6, 'name': 'Sufiyan Muqeem', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Associate/Emerging',
        'ipl_matches': 0, 'ipl_wickets': 0, 'overall_econ': 6.20, 'p_econ': 5.13, 'p_wickets': 17,
        'p_dot_pct': 45.3, 'p_balls': 234, 'ppi_score': 118.82, 'rr_fit_score': 90.0, 'price_est': '₹1–2.5 Cr',
        'target_reasons': 'Uncontracted emerging prodigy. Left-arm wrist-spin mystery; sensational 5.13 economy in pressure overs with 45.3% dot balls.',
        'risks': 'Young talent adapting to high-pressure tournament formats.'
    },
    {
        'rank': 7, 'name': 'Abrar Ahmed', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_wickets': 0, 'overall_econ': 6.55, 'p_econ': 5.92, 'p_wickets': 23,
        'p_dot_pct': 43.2, 'p_balls': 296, 'ppi_score': 118.43, 'rr_fit_score': 89.0, 'price_est': '₹1.5–3 Cr',
        'target_reasons': 'Uncontracted international free agent. Mystery leg-cutter and googly specialist; 5.92 pressure economy on gripping surfaces.',
        'risks': 'Boundary defense on very small grounds.'
    },
    {
        'rank': 8, 'name': 'Adil Rashid', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 2, 'ipl_wickets': 1, 'overall_econ': 7.42, 'p_econ': 8.59, 'p_wickets': 35,
        'p_dot_pct': 32.8, 'p_balls': 530, 'ppi_score': 113.54, 'rr_fit_score': 90.0, 'price_est': '₹2.5–4.5 Cr',
        'target_reasons': 'Uncontracted international free agent. Master veteran wrist spinner; World Cup champion with disguised googlies in middle overs.',
        'risks': 'Age profile.'
    },
    {
        'rank': 9, 'name': 'Tim Southee', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 54, 'ipl_wickets': 47, 'overall_econ': 8.67, 'p_econ': 8.47, 'p_wickets': 31,
        'p_dot_pct': 34.2, 'p_balls': 406, 'ppi_score': 108.28, 'rr_fit_score': 88.0, 'price_est': '₹1.5–3 Cr',
        'target_reasons': 'Uncontracted international free agent. Veteran death seam master; executes wide yorkers, knuckle-balls, and defensive field sets.',
        'risks': 'High pace decline; relies heavily on variations.'
    },
    {
        'rank': 10, 'name': 'Taskin Ahmed', 'current_ipl_franchise': 'Free Agent (Not in Any Team)',
        'availability_status': 'CONFIRMED FREE AGENT', 'pool': 'Free Agent', 'classification': 'Overseas',
        'ipl_matches': 0, 'ipl_wickets': 0, 'overall_econ': 8.12, 'p_econ': 8.46, 'p_wickets': 29,
        'p_dot_pct': 36.7, 'p_balls': 354, 'ppi_score': 103.63, 'rr_fit_score': 87.0, 'price_est': '₹2–4 Cr',
        'target_reasons': 'Uncontracted international free agent. 145+ kph hit-the-deck pace bowler; extracts bounce and bowls hard lengths.',
        'risks': 'Injury history.'
    }
]

# Export CSVs for the 100% Free Agents
with open('uncontracted_free_agents_top10_batters.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(free_agent_batters[0].keys()))
    w.writeheader()
    w.writerows(free_agent_batters)

with open('uncontracted_free_agents_top10_bowlers.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(free_agent_bowlers[0].keys()))
    w.writeheader()
    w.writerows(free_agent_bowlers)

print("Exported uncontracted_free_agents_top10_batters.csv & uncontracted_free_agents_top10_bowlers.csv!")

# Update war_room_data.json with these Free Agents
with open('war_room_data.json', 'r', encoding='utf-8') as f:
    wdata = json.load(f)

wdata['free_agent_batters_10'] = free_agent_batters
wdata['free_agent_bowlers_10'] = free_agent_bowlers

with open('war_room_data.json', 'w', encoding='utf-8') as f:
    json.dump(wdata, f, indent=2)

print("war_room_data.json updated successfully!")

