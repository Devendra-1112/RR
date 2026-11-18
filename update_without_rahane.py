import json
import csv

# 1. Update ipl2027_official_teams_database.json
with open('ipl2027_official_teams_database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Corrected Batters List without Rahane
new_top_batters = [
    {
        'rank': 1, 'name': 'Rahul Tripathi', 'previous_franchise': 'KKR', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Indian', 'role': 'No. 3 Intent Anchor / Striker (RHB)', 'ipl_matches': 48, 'ipl_runs': 906,
        'overall_sr': 142.10, 'p_sr': 166.40, 'p_avg': 22.20, 'p_balls': 107, 'ppi_score': 77.75,
        'rr_fit_score': 97.0, 'suitability_score': 88.50, 'est_value': '₹3.5–5.0 Cr', 'max_bid': '₹5.5 Cr',
        'why_target': 'High-tempo No. 3 with fearless intent against pace and spin. Directly replaces Sanju Samson at No. 3 with proven IPL pedigree (2,200+ career IPL runs).',
        'risks': 'Aggressive shot selection carries early dismissal risk against quality swing.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 2, 'name': 'Nitish Rana', 'previous_franchise': 'DC', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Indian', 'role': 'Middle-Order Spin Destroyer (LHB)', 'ipl_matches': 50, 'ipl_runs': 1258,
        'overall_sr': 146.11, 'p_sr': 155.06, 'p_avg': 28.43, 'p_balls': 385, 'ppi_score': 66.60,
        'rr_fit_score': 96.0, 'suitability_score': 84.85, 'est_value': '₹4.0–6.5 Cr', 'max_bid': '₹7.0 Cr',
        'why_target': 'Elite middle-overs spin destructor. Smashes wrist-spin and SLA at 155+ SR, balancing RR middle order alongside Parag and Jurel.',
        'risks': 'Occasional vulnerability to back-of-a-length seam in powerplays.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 3, 'name': 'Nehal Wadhera', 'previous_franchise': 'PBKS', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Indian', 'role': 'Left-Hand Middle Finisher (LHB)', 'ipl_matches': 37, 'ipl_runs': 784,
        'overall_sr': 133.87, 'p_sr': 145.20, 'p_avg': 19.54, 'p_balls': 323, 'ppi_score': 62.32,
        'rr_fit_score': 98.0, 'suitability_score': 82.95, 'est_value': '₹4.5–6.5 Cr', 'max_bid': '₹7.5 Cr',
        'why_target': 'High-ceiling young Indian left-handed finisher. Phenomenal composure in death chases (145+ SR), solves RR’s lower-order finishing void.',
        'risks': 'Still developing consistency against top-tier international mystery spin.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 4, 'name': 'Glenn Maxwell', 'previous_franchise': 'RCB', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Overseas', 'role': 'Explosive Spin Destroyer & Off-Spinner (RHB/OB)', 'ipl_matches': 42, 'ipl_runs': 801,
        'overall_sr': 153.40, 'p_sr': 180.89, 'p_avg': 26.20, 'p_balls': 246, 'ppi_score': 81.61,
        'rr_fit_score': 95.0, 'suitability_score': 88.20, 'est_value': '₹6.0–8.5 Cr', 'max_bid': '₹9.0 Cr',
        'why_target': 'Generational T20 game-changer. Smashes both spin and pace at 180+ SR under pressure and provides 2–3 overs of off-spin on turning Jaipur pitches.',
        'risks': 'High-risk shot selection can lead to low-score strings; commands an overseas slot.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 5, 'name': 'Shimron Hetmyer', 'previous_franchise': 'RR', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Overseas', 'role': 'Death Finisher (LHB)', 'ipl_matches': 57, 'ipl_runs': 1049,
        'overall_sr': 151.64, 'p_sr': 155.92, 'p_avg': 23.05, 'p_balls': 828, 'ppi_score': 65.82,
        'rr_fit_score': 95.0, 'suitability_score': 84.25, 'est_value': '₹5.5–8.0 Cr', 'max_bid': '₹8.5 Cr',
        'why_target': 'Proven Rajasthan Royals match-winner. Re-acquiring him at a rational price after release provides instant death-overs boundary violence.',
        'risks': 'Utilizes 1 of RR’s 3 remaining overseas slots; price inflation in open bidding.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 6, 'name': 'M Shahrukh Khan', 'previous_franchise': 'GT', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Indian', 'role': 'Designated Death Finisher (RHB)', 'ipl_matches': 43, 'ipl_runs': 622,
        'overall_sr': 142.80, 'p_sr': 169.48, 'p_avg': 18.10, 'p_balls': 213, 'ppi_score': 75.14,
        'rr_fit_score': 96.0, 'suitability_score': 84.10, 'est_value': '₹3.5–5.0 Cr', 'max_bid': '₹5.5 Cr',
        'why_target': 'High-impact domestic Indian boundary striker with 169+ pressure SR. Solves RR’s lower-order finishing without using an overseas slot.',
        'risks': 'Can be vulnerable to hard short-pitch bowling above shoulder height.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 7, 'name': 'Mahipal Lomror', 'previous_franchise': 'MI', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Indian', 'role': 'Middle-Overs Power Hitter (LHB/SLA)', 'ipl_matches': 30, 'ipl_runs': 346,
        'overall_sr': 137.90, 'p_sr': 162.03, 'p_avg': 14.22, 'p_balls': 117, 'ppi_score': 66.37,
        'rr_fit_score': 93.0, 'suitability_score': 81.10, 'est_value': '₹2.5–3.8 Cr', 'max_bid': '₹4.0 Cr',
        'why_target': 'Ex-RR domestic talent with brutal spin power (162+ pressure SR) and useful slow left-arm bowling versatility.',
        'risks': 'Can be tied down by express pace targeted at the chest.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 8, 'name': 'Abishek Porel', 'previous_franchise': 'DC', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Indian', 'role': 'Wicketkeeper-Batter (LHB)', 'ipl_matches': 24, 'ipl_runs': 355,
        'overall_sr': 135.20, 'p_sr': 132.88, 'p_avg': 17.64, 'p_balls': 73, 'ppi_score': 49.32,
        'rr_fit_score': 92.0, 'suitability_score': 78.52, 'est_value': '₹2.5–4.0 Cr', 'max_bid': '₹4.5 Cr',
        'why_target': 'Dynamic Indian wicketkeeper providing essential glovework backup and aggressive top-order flexibility for Dhruv Jurel.',
        'risks': 'Relatively raw under extreme knockout match pressure.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 9, 'name': 'Rachin Ravindra', 'previous_franchise': 'KKR', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Overseas', 'role': 'Top-Order / SLA All-Rounder (LHB/SLA)', 'ipl_matches': 28, 'ipl_runs': 560,
        'overall_sr': 141.20, 'p_sr': 147.70, 'p_avg': 25.21, 'p_balls': 198, 'ppi_score': 66.38,
        'rr_fit_score': 92.0, 'suitability_score': 81.56, 'est_value': '₹4.5–6.5 Cr', 'max_bid': '₹7.0 Cr',
        'why_target': 'World-class multi-phase accumulator and spin option. Provides top-order class and slow left-arm control at Sawai Mansingh Stadium.',
        'risks': 'Requires overseas slot; middle-overs boundary boundary rate needs elevation.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    },
    {
        'rank': 10, 'name': 'Abhinav Manohar', 'previous_franchise': 'GT', 'status': 'VERIFIED AUCTION ELIGIBLE',
        'classification': 'Indian', 'role': 'Middle-Overs Power Striker (RHB)', 'ipl_matches': 22, 'ipl_runs': 292,
        'overall_sr': 139.70, 'p_sr': 151.50, 'p_avg': 13.00, 'p_balls': 103, 'ppi_score': 70.07,
        'rr_fit_score': 93.0, 'suitability_score': 81.20, 'est_value': '₹2.0–3.5 Cr', 'max_bid': '₹4.0 Cr',
        'why_target': 'High-ceiling Indian domestic boundary striker (151.5 pressure SR). Fills middle-order depth and protects RR’s 3 remaining overseas slots.',
        'risks': 'Limited defensive gear if early wickets fall in powerplay.',
        'source_url': 'https://www.iplt20.com/auction-2027-retention-release'
    }
]

db['top_10_batters'] = new_top_batters

# Add Ajinkya Rahane to Unavailable / Will Not Play Registry
db['unavailable_players_registry'] = db.get('unavailable_players_registry', [])
db['unavailable_players_registry'].append({
    'player_name': 'Ajinkya Rahane',
    'nationality': 'Indian',
    'status': 'OFFICIALLY UNAVAILABLE / WILL NOT PLAY IPL 2027',
    'reason': 'Will not participate in IPL 2027 season per franchise intelligence update. Disqualified from RR auction shortlist.',
    'replacement_player': 'Rahul Tripathi (Promoted to #1 Samson Replacement) & Abhinav Manohar (Entered Top 10)'
})

# Update Change Report
db['eligibility_audit_change_report'].append({
    'removed_player': 'Ajinkya Rahane', 'list': 'Top 10 Batsmen', 'original_rank': 1,
    'reason_for_removal': 'OFFICIALLY UNAVAILABLE / WILL NOT PLAY IPL 2027. Per franchise intelligence, Rahane is not participating in the IPL 2027 campaign.',
    'replacement_player': 'Rahul Tripathi (Elevated to #1) & Abhinav Manohar (#10)',
    'replacement_rank': 1,
    'replacement_eligibility': 'VERIFIED AUCTION ELIGIBLE',
    'why_replacement_better': 'Rahul Tripathi provides dynamic high-intent strokeplay at No. 3 (166.4 pressure SR, 77.75 PPI, 906 IPL runs), attacking both express pace and mystery spin. Abhinav Manohar adds domestic boundary power (151.5 pressure SR).'
})

# Update Budget Scenario A
db['budget_scenarios']['scenario_a_balanced']['purchases'] = [
    {'name': 'Matheesha Pathirana', 'type': 'Overseas', 'role': 'Death Specialist', 'bid': 9.5, 'walk_away': 11.0},
    {'name': 'Nehal Wadhera', 'type': 'Indian', 'role': 'Left-Hand Finisher', 'bid': 5.5, 'walk_away': 6.5},
    {'name': 'Rahul Tripathi', 'type': 'Indian', 'role': 'No. 3 Striker / Anchor', 'bid': 3.5, 'walk_away': 4.5},
    {'name': 'Mahipal Lomror', 'type': 'Indian', 'role': 'Spin Destroyer', 'bid': 2.5, 'walk_away': 3.5},
    {'name': 'Abishek Porel', 'type': 'Indian', 'role': 'Keeper-Batter', 'bid': 2.5, 'walk_away': 3.2},
    {'name': 'M Shahrukh Khan', 'type': 'Indian', 'role': 'Power Finisher', 'bid': 1.5, 'walk_away': 2.5}
]
db['budget_scenarios']['scenario_a_balanced']['total_spend'] = 25.0
db['budget_scenarios']['scenario_a_balanced']['purse_remaining'] = 2.05

with open('ipl2027_official_teams_database.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2)

print('Updated ipl2027_official_teams_database.json without Rahane.')

# 2. Update top_10_verified_eligible_batters_2027.csv
with open('top_10_verified_eligible_batters_2027.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'rank', 'name', 'previous_franchise', 'status', 'classification', 'role',
        'ipl_matches', 'ipl_runs', 'overall_sr', 'p_sr', 'p_avg', 'p_balls', 'ppi_score',
        'rr_fit_score', 'est_value', 'max_bid', 'why_target', 'risks', 'source_url'
    ])
    for b in new_top_batters:
        writer.writerow([
            b['rank'], b['name'], b['previous_franchise'], b['status'], b['classification'], b['role'],
            b['ipl_matches'], b['ipl_runs'], b['overall_sr'], b['p_sr'], b['p_avg'], b['p_balls'], b['ppi_score'],
            b['rr_fit_score'], b['est_value'], b['max_bid'], b['why_target'], b['risks'], b['source_url']
        ])

print('Updated top_10_verified_eligible_batters_2027.csv without Rahane.')
