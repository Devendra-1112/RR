# Rajasthan Royals • IPL 2027 Auction War Room
## SupeRR Selector Season 2 • Round 1: Identify the Most Reliable Players Under Pressure

An advanced, data-driven Auction Intelligence War Room and Decision-Support System engineered for **Rajasthan Royals (RR)** for the IPL 2027 Auction.

---

## 🏆 Unstop Submission Top Picks

### Top 10 Batsmen Under Pressure
1. **Naman Dhir** (`Mumbai Indians`) — PPI: **92.41** | Pressure SR: **194.44** *(Tier 1 Domestic 360° Finisher; preserves overseas slot)*
2. **Shreyas Iyer** (`Punjab Kings`) — PPI: **90.57** | Pressure SR: **179.20** *(Marquee Middle-Order Anchor & Playmaker)*
3. **Rishabh Pant** (`Lucknow Super Giants`) — PPI: **89.68** | Pressure SR: **180.54** *(Explosive Left-Hand Wicketkeeper-Batter)*
4. **Fakhar Zaman** (`Released / Free Agent`) — PPI: **96.68** | Pressure SR: **183.89** *(High-Tempo Top-Order Enforcer)*
5. **Asif Khan** (`Released / Free Agent`) — PPI: **94.13** | Pressure SR: **196.52** *(Highest Pressure Strike Rate in Dataset)*
6. **Najibullah Zadran** (`Released / Free Agent`) — PPI: **92.52** | Pressure SR: **180.00** *(Left-Hand Death Boundary Specialist)*
7. **Babar Azam** (`Released / Free Agent`) — PPI: **91.73** | Pressure Avg: **51.33** *(Elite Collapse Recovery Anchor)*
8. **Phil Salt** (`Royal Challengers Bengaluru`) — PPI: **90.93** | Pressure SR: **187.27** *(Powerplay & Death Boundary Striker)*
9. **Tim David** (`Royal Challengers Bengaluru`) — PPI: **90.60** | Pressure SR: **194.85** *(Heavy Boundary Lever for Overs 17–20)*
10. **Angelo Mathews** (`Released / Free Agent`) — PPI: **87.89** | Dot %: **20.5%** *(Ice-Cool Veteran Crisis Finisher)*

### Top 10 Bowlers Under Pressure
1. **Arshdeep Singh** (`Punjab Kings`) — PPI: **306.82** | **131 Clutch Wickets** | Econ: **8.89** *(#1 Domestic Death Seamer)*
2. **Bhuvneshwar Kumar** (`Royal Challengers Bengaluru`) — PPI: **177.25** | **68 Clutch Wickets** | Econ: **8.87** *(Powerplay Swing & Death Yorker Mastery)*
3. **Yuzvendra Chahal** (`Punjab Kings`) — PPI: **180.78** | **71 Clutch Wickets** | Econ: **8.91** *(Attacking Middle-Overs Leg-Spinner)*
4. **Harshal Patel** (`Sunrisers Hyderabad`) — PPI: **163.53** | **64 Clutch Wickets** | Econ: **9.54** *(Slower Dipper Specialist on SMS Pitch)*
5. **Jason Holder** (`Gujarat Titans`) — PPI: **160.93** | **63 Clutch Wickets** | Econ: **9.50** *(Steep Bounce Pace All-Rounder)*
6. **Mohammed Siraj** (`Gujarat Titans`) — PPI: **140.08** | **47 Clutch Wickets** | Dot %: **41.7%** *(Aggressive Breakthrough Seamer)*
7. **Haris Rauf** (`Released / Free Agent`) — PPI: **132.24** | **43 Clutch Wickets** | Econ: **8.76** *(150+ kph Express Tearaway)*
8. **Maheesh Theekshana** (`Released / Free Agent`) — PPI: **128.17** | **40 Clutch Wickets** | Econ: **7.94** *(Carrom-Ball Mystery Spinner for Middle Overs 7–15)*
9. **Mohammad Nawaz** (`Released / Free Agent`) — PPI: **128.08** | **28 Clutch Wickets** | Econ: **5.87** *(Best Defensive Pressure Economy)*
10. **Trent Boult** (`Mumbai Indians`) — PPI: **128.22** | **40 Clutch Wickets** | Econ: **8.45** *(Elite Left-Arm Powerplay Wicket-Taker)*

---

## 📊 Methodology & Pressure Performance Index (PPI)

* **Dataset:** 200,999 legal deliveries across 883 matches (371 IPL matches from 2022 to 2026 + 512 T20Is).
* **Pressure Isolation:** 81,722 high-leverage deliveries (40.7% of total) analyzed across four critical leverage phases:
  * Death Overs (Overs 16–20 in both innings: 44,454 balls).
  * High Required Run Rate Chases (RRR ≥ 9.80, or ≤ 36 balls with ≥ 35 runs needed: 32,562 balls).
  * Powerplay Collapse Rescue (Overs 1–6 with ≥ 3 wickets down: 1,897 balls).
  * High-Stakes Knockout Context (Overs 12–20 in playoffs & finals: 1,022 balls).
* **Governance Standard:** Strict exclusion of contractually retained marquee cores (Bumrah ₹18 Cr, Kohli ₹21 Cr, Klaasen ₹23 Cr, Rashid Khan ₹18 Cr, etc.) and officially retired players (Dhawan, Karthik). Only purchasable auction targets are recommended.

---

## 🚀 How to Run the War Room Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Devendra-1112/RR.git
   cd RR
   ```

2. (Optional) Set up your Gemini API key:
   ```bash
   copy .env.example .env
   # Add your GEMINI_API_KEY inside .env
   ```

3. Launch the War Room Server:
   ```bash
   python server.py
   ```

4. Open the interactive dashboard in your browser:
   ```
   http://127.0.0.1:8088/dashboard.html
   ```

---

## 📁 Repository Deliverables

| Deliverable | File Path | Description |
|:---|:---|:---|
| **Interactive Dashboard** | [`dashboard.html`](dashboard.html) | Full War Room UI with Unstop form inputs, metrics tables, and Gemini AI Scout |
| **Offline Player DB** | [`all_players_offline.json`](all_players_offline.json) | 1,210 indexed players with offline search & autocomplete |
| **Methodology Report (PDF)** | [`RR_SupeRR_Selector_Methodology_Report.pdf`](RR_SupeRR_Selector_Methodology_Report.pdf) | Comprehensive PDF submission report |
| **Auction Strategy Deck (PPTX)** | [`RR_SupeRR_Selector_Auction_Strategy.pptx`](RR_SupeRR_Selector_Auction_Strategy.pptx) | 10-slide executive presentation deck |
| **Top 10 Batters CSV** | [`top_10_available_batters.csv`](top_10_available_batters.csv) | Full 18-column analytics export for Batters |
| **Top 10 Bowlers CSV** | [`top_10_available_bowlers.csv`](top_10_available_bowlers.csv) | Full 18-column analytics export for Bowlers |
| **Strictly Verified Batters CSV** | [`verified_auction_eligible_batters.csv`](verified_auction_eligible_batters.csv) | Free agent eligible batters audit |
| **Strictly Verified Bowlers CSV** | [`verified_auction_eligible_bowlers.csv`](verified_auction_eligible_bowlers.csv) | Free agent eligible bowlers audit |
| **Backend & AI Server** | [`server.py`](server.py) | Python HTTP server with Gemini 2.5 Flash scouting assistant |
| **Strict Verification Engine** | [`strict_verification_engine.py`](strict_verification_engine.py) | 200,999-ball audit and verification pipeline |

---

*Prepared for Rajasthan Royals IPL 2027 Auction War Room • SupeRR Selector Season 2.*
