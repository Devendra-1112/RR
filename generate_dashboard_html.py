import json
import os
import shutil

with open('ipl2027_official_teams_database.json', 'r', encoding='utf-8') as f:
    master_db = json.load(f)

meta = master_db['metadata']
top_batters = master_db['top_10_batters']
top_bowlers = master_db['top_10_bowlers']
franchises = master_db['franchises']
rr_retained = master_db['rr_retained_squad']
released_pool = master_db['released_players_pool']
all_players = master_db['all_retained_players']
budget_scenarios = master_db['budget_scenarios']
playing_xi = master_db['playing_xi']
retired_list = master_db.get('retired_players_registry', [])
pak_list = master_db.get('pakistani_players_exclusion_registry', [])
change_report = master_db.get('eligibility_audit_change_report', [])

top_batters_json = json.dumps(top_batters)
top_bowlers_json = json.dumps(top_bowlers)
franchises_json = json.dumps(franchises)
rr_retained_json = json.dumps(rr_retained)
released_pool_json = json.dumps(released_pool)
all_players_json = json.dumps(all_players)
retired_list_json = json.dumps(retired_list)
pak_list_json = json.dumps(pak_list)
change_report_json = json.dumps(change_report)

remark_text = """RAJASTHAN ROYALS — IPL 2027 AUCTION INTELLIGENCE WAR ROOM (ITC GRAND GOA)
Official 18 November 2026 Baseline Submission • SupeRR Selector Season 2 (Round 1)

1. DATA SCIENCE & PPI LEVERAGE METHODOLOGY:
• Analyzed 200,999 deliveries across 883 T20 fixtures (371 IPL matches + 512 T20Is, 2022–2026).
• Isolated 81,722 pressure deliveries (40.7% of total) spanning death overs (16–20: 44,454 balls), steep chases (RRR >= 9.80: 32,562 balls), powerplay collapses (1,897 balls), and knockout matches (1,022 balls).
• Pressure Performance Index (PPI): Delivery-level composite tracking pressure strike rate / economy, pressure batting average / wicket rate, baseline deltas, and dot-ball suppression, dampener-adjusted for sample size.
• Strict Regulatory Eligibility Audit: All 184 retained players across 10 franchises strictly excluded. Pakistani players excluded under standing BCCI policy. Retired IPL players audited and excluded. 100% of shortlisted players are VERIFIED AUCTION ELIGIBLE.

2. RAJASTHAN ROYALS RETENTION CONTEXT & SQUAD GAPS:
• Retained Squad (19 Players • ₹27.05 Cr Purse Remaining • 6 Open Slots, Max 3 Overseas):
  Includes landmark incoming trades for Ravindra Jadeja (from CSK) and Mohammed Shami (from SRH/LSG), alongside core pillars Yashasvi Jaiswal, Riyan Parag, Dhruv Jurel, Jofra Archer, Sandeep Sharma, and Ravi Bishnoi.
• Core Tactical Gaps:
  1. No. 3 Top-Order Anchor: Replacing traded former captain Sanju Samson.
  2. Middle-Order Spin Destroyer & Death Finisher: Replacing released Shimron Hetmyer.
  3. Death Seam Spearhead: World-class execution partner for Sandeep Sharma in overs 18 & 20.
  4. Domestic Indian Depth & Wicketkeeper Backup: 3 to 4 Indian buys required to respect 8-overseas maximum.

3. TOP 10 VERIFIED AUCTION-ELIGIBLE BATTERS FOR RR:
1. Ajinkya Rahane (Indian | KKR | PPI: 68.88 | Press SR: 147.47 | Press Avg: 31.58 | No. 3 Anchor, replaces Samson)
2. Nitish Rana (Indian | DC | PPI: 66.60 | Press SR: 155.06 | Spin Destroyer in Overs 7–15)
3. Nehal Wadhera (Indian | PBKS | PPI: 62.32 | Press SR: 145.20 | Left-Hand Clutch Death Finisher)
4. Glenn Maxwell (Overseas | RCB | PPI: 81.61 | Press SR: 180.89 | Generational Spin Destroyer & Off-Spinner)
5. Shimron Hetmyer (Overseas | RR | PPI: 65.82 | Press SR: 155.92 | Proven RR Match-Winner Buy-back)
6. M Shahrukh Khan (Indian | GT | PPI: 75.14 | Press SR: 169.48 | Designated Indian Death Boundary Finisher)
7. Rahul Tripathi (Indian | KKR | PPI: 57.98 | Press SR: 141.74 | Aggressive Powerplay/No. 3 Intent Striker)
8. Mahipal Lomror (Indian | MI | PPI: 66.37 | Press SR: 162.03 | Southpaw Spin Muscle / SLA)
9. Abishek Porel (Indian | DC | PPI: 49.32 | Press SR: 132.88 | Dynamic Indian Backup Keeper-Batter)
10. Rachin Ravindra (Overseas | KKR | PPI: 66.38 | Press SR: 147.70 | Top-Order / SLA All-Rounder)

4. TOP 10 VERIFIED AUCTION-ELIGIBLE BOWLERS FOR RR:
1. Matheesha Pathirana (Overseas | KKR | PPI: 176.17 | 61 Clutch Wkts | 7.90 Press Econ | Generational Death Specialist)
2. Trent Boult (Overseas | MI | PPI: 128.22 | 40 Clutch Wkts | 8.45 Press Econ | Powerplay Swing Icon Returning)
3. Avesh Khan (Indian | LSG | PPI: 148.58 | 57 Clutch Wkts | 9.76 Press Econ | 145+ kph Indian Death Seamer)
4. Mustafizur Rahman (Overseas | KKR | PPI: 147.76 | 48 Clutch Wkts | 7.87 Press Econ | Cutter & Change of Pace)
5. Wanindu Hasaranga (Overseas | LSG | PPI: 158.35 | 53 Clutch Wkts | 8.76 Press Econ | Mystery Spin All-Rounder)
6. Prasidh Krishna (Indian | GT | PPI: 111.63 | 37 Clutch Wkts | 9.62 Press Econ | 145+ kph Frontline Seamer, Ex-RR)
7. Deepak Chahar (Indian | MI | PPI: 85.53 | 8.72 Press Econ | Powerplay Swing Spearhead)
8. Maheesh Theekshana (Overseas | CSK | PPI: 132.17 | 40 Clutch Wkts | 7.94 Press Econ | Carrom Mystery Spinner)
9. Tushar Deshpande (Indian | RR | PPI: 114.22 | 41 Clutch Wkts | Domestic Seam Reserve)
10. Akash Deep (Indian | KKR | PPI: 25.74 | Hit-the-Deck Seam Reinforcement)

5. OPTIMAL BUDGET ALLOCATION (SCENARIO A • ₹24.0 CR SPEND • ₹3.05 CR BUFFER):
• P1 (Death Specialist): Matheesha Pathirana (₹9.5 Cr) • P2 (Finisher): Nehal Wadhera (₹5.5 Cr)
• P3 (No. 3 Anchor): Ajinkya Rahane (₹2.5 Cr) • P4 (Spin Destructor): Mahipal Lomror (₹2.5 Cr)
• P5 (Backup Keeper): Abishek Porel (₹2.5 Cr) • P6 (Finisher Depth): M Shahrukh Khan (₹1.5 Cr)

6. OPTIMIZED PLAYING XI & IMPACT PLAYER:
• Batting First XI: Jaiswal, Sooryavanshi, Rahane, Parag, Jurel (Wk), Maxwell, Wadhera, Jadeja, Archer, Shami, Bishnoi.
• Bowling First Impact Sub: Matheesha Pathirana replaces Ajinkya Rahane, giving RR an impenetrable 6-bowler attack."""

print("Loaded all data and prepared Remark text.")
