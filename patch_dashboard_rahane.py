with open('build_ipl2027_war_room_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace remark snippet
old_remark = """3. TOP 10 VERIFIED AUCTION-ELIGIBLE BATTERS FOR RR:
1. Ajinkya Rahane (Indian | KKR | PPI: 68.88 | Press SR: 147.47 | Press Avg: 31.58 | No. 3 Anchor, replaces Samson)
2. Nitish Rana (Indian | DC | PPI: 66.60 | Press SR: 155.06 | Spin Destroyer in Overs 7–15)
3. Nehal Wadhera (Indian | PBKS | PPI: 62.32 | Press SR: 145.20 | Left-Hand Clutch Death Finisher)
4. Glenn Maxwell (Overseas | RCB | PPI: 81.61 | Press SR: 180.89 | Generational Spin Destroyer & Off-Spinner)
5. Shimron Hetmyer (Overseas | RR | PPI: 65.82 | Press SR: 155.92 | Proven RR Match-Winner Buy-back)
6. M Shahrukh Khan (Indian | GT | PPI: 75.14 | Press SR: 169.48 | Designated Indian Death Boundary Finisher)
7. Rahul Tripathi (Indian | KKR | PPI: 57.98 | Press SR: 141.74 | Aggressive Powerplay/No. 3 Intent Striker)
8. Mahipal Lomror (Indian | MI | PPI: 66.37 | Press SR: 162.03 | Southpaw Spin Muscle / SLA)
9. Abishek Porel (Indian | DC | PPI: 49.32 | Press SR: 132.88 | Dynamic Indian Backup Keeper-Batter)
10. Rachin Ravindra (Overseas | KKR | PPI: 66.38 | Press SR: 147.70 | Top-Order / SLA All-Rounder)"""

new_remark = """3. TOP 10 VERIFIED AUCTION-ELIGIBLE BATTERS FOR RR:
1. Rahul Tripathi (Indian | KKR | PPI: 77.75 | Press SR: 166.40 | No. 3 Intent Striker & Samson Replacement)
2. Nitish Rana (Indian | DC | PPI: 66.60 | Press SR: 155.06 | Spin Destroyer in Overs 7–15)
3. Nehal Wadhera (Indian | PBKS | PPI: 62.32 | Press SR: 145.20 | Left-Hand Clutch Death Finisher)
4. Glenn Maxwell (Overseas | RCB | PPI: 81.61 | Press SR: 180.89 | Generational Spin Destroyer & Off-Spinner)
5. Shimron Hetmyer (Overseas | RR | PPI: 65.82 | Press SR: 155.92 | Proven RR Match-Winner Buy-back)
6. M Shahrukh Khan (Indian | GT | PPI: 75.14 | Press SR: 169.48 | Designated Indian Death Boundary Finisher)
7. Mahipal Lomror (Indian | MI | PPI: 66.37 | Press SR: 162.03 | Southpaw Spin Muscle / SLA)
8. Abishek Porel (Indian | DC | PPI: 49.32 | Press SR: 132.88 | Dynamic Indian Backup Keeper-Batter)
9. Rachin Ravindra (Overseas | KKR | PPI: 66.38 | Press SR: 147.70 | Top-Order / SLA All-Rounder)
10. Abhinav Manohar (Indian | GT | PPI: 70.07 | Press SR: 151.50 | Middle-Overs Power Striker)"""

if old_remark in text:
    text = text.replace(old_remark, new_remark)
    print("Replaced old_remark successfully.")
else:
    print("Warning: old_remark not found.")

# Replace Rahane in budget text
text = text.replace("• P3 (No. 3 Anchor): Ajinkya Rahane (₹2.5 Cr)", "• P3 (No. 3 Striker): Rahul Tripathi (₹3.5 Cr)")
text = text.replace("₹24.0 CR SPEND • ₹3.05 CR BUFFER", "₹25.0 CR SPEND • ₹2.05 CR BUFFER")
text = text.replace("replaces Ajinkya Rahane", "replaces Rahul Tripathi")
text = text.replace("Ajinkya Rahane (No. 3 Anchor)", "Rahul Tripathi (No. 3 Striker / Anchor)")
text = text.replace("Ajinkya Rahane", "Rahul Tripathi")

with open('build_ipl2027_war_room_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated build_ipl2027_war_room_dashboard.py successfully.")
