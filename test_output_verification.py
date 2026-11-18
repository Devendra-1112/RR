import json

with open('ipl2027_official_teams_database.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== VERIFIED AUCTION-ELIGIBLE TOP 10 BATTERS ===")
for b in d['top_10_batters']:
    print(f"#{b['rank']} {b['name']} ({b['classification']} | {b['previous_franchise']}) - PPI: {b['ppi_score']} | Press SR: {b['p_sr']} | Press Avg: {b['p_avg']} | Max Bid: {b['max_bid']}")

print("\n=== VERIFIED AUCTION-ELIGIBLE TOP 10 BOWLERS ===")
for w in d['top_10_bowlers']:
    print(f"#{w['rank']} {w['name']} ({w['classification']} | {w['previous_franchise']}) - PPI: {w['ppi_score']} | Press Econ: {w['p_econ']} | Press Wkt Rate: {w['p_w_rate']} | Max Bid: {w['max_bid']}")

print("\n=== FRANCHISE PURSE & RETENTION SUMMARY ===")
for code, f_meta in d['franchises'].items():
    print(f"{code} ({f_meta['name']}): Retained: {f_meta['retained_count']} | Remaining Purse: ₹{f_meta['purse']} Cr | Slots Left: {f_meta['slots_left']}")

print("\n=== RR SQUAD (19 RETAINED) ===")
for p in d['rr_retained_squad']:
    trade = f" [{p['trade']}]" if 'trade' in p else ""
    print(f"• {p['name']} ({p['type']} - {p['role']}) - ₹{p['price']} Cr{trade}")
