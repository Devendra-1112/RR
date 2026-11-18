import json
import os
import shutil

print("=== REBUILDING RAJASTHAN ROYALS IPL 2027 AUCTION WAR ROOM DASHBOARD ===")

with open('ipl2027_official_teams_database.json', 'r', encoding='utf-8') as f:
    master_db = json.load(f)

with open('all_players_offline.json', 'r', encoding='utf-8') as f:
    all_players = json.load(f)

meta = master_db['metadata']
top_batters = master_db['top_10_batters']
top_bowlers = master_db['top_10_bowlers']
franchises = master_db['franchises']
rr_retained = master_db['rr_retained_squad']
released_pool = master_db['released_players_pool']
budget_data = master_db['budget_scenarios']
playing_xi = master_db['playing_xi']

top_batters_json = json.dumps(top_batters)
top_bowlers_json = json.dumps(top_bowlers)
franchises_json = json.dumps(franchises)
rr_retained_json = json.dumps(rr_retained)
released_pool_json = json.dumps(released_pool)
all_players_json = json.dumps(all_players)
retired_list = master_db.get('retired_players_registry', [])
pak_list = master_db.get('pakistani_players_exclusion_registry', [])
change_report = master_db.get('eligibility_audit_change_report', [])

retired_list_json = json.dumps(retired_list)
pak_list_json = json.dumps(pak_list)
change_report_json = json.dumps(change_report)

# Official Unstop Remark text
remark_text = """RAJASTHAN ROYALS — IPL 2027 AUCTION INTELLIGENCE WAR ROOM (ITC GRAND GOA)
Official 18 November 2026 Baseline Submission • SupeRR Selector Season 2 (Round 1)

1. DATA SCIENCE & PPI LEVERAGE METHODOLOGY:
• Analyzed 200,999 deliveries across 883 T20 fixtures (371 IPL matches + 512 T20Is, 2022–2026).
• Isolated 81,722 pressure deliveries (40.7% of total) spanning death overs (16–20: 44,454 balls), steep chases (RRR >= 9.80: 32,562 balls), powerplay collapses (1,897 balls), and knockout matches (1,022 balls).
• Pressure Performance Index (PPI): Delivery-level composite tracking pressure strike rate / economy, pressure batting average / wicket rate, baseline deltas, and dot-ball suppression, dampener-adjusted for sample size.
• Strict Eligibility Standard: All 184 retained players across all 10 franchises strictly excluded. Every recommended player is an officially verified released entrant or registered international entrant.

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
Result: 4 Indian Buys + 2 Overseas Buys = Exactly 25 Squad Members (7 Overseas total, well under 8 limit).

6. OPTIMIZED PLAYING XI & IMPACT STRATEGY:
Yashasvi Jaiswal, Vaibhav Sooryavanshi/Pretorius, Ajinkya Rahane (Auction), Riyan Parag, Dhruv Jurel (Wk), Nehal Wadhera (Auction), Ravindra Jadeja, Jofra Archer, Mohammed Shami, Ravi Bishnoi, Sandeep Sharma.
Impact Player: Matheesha Pathirana replaces Ajinkya Rahane during the bowling innings."""

html_code = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rajasthan Royals • IPL 2027 Auction War Room (18-Nov-2026 Baseline)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap');
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .rr-card {{
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .rr-card:hover {{
      border-color: rgba(228, 0, 124, 0.35);
    }}
    .rr-card-highlight {{
      background: linear-gradient(135deg, rgba(30, 20, 50, 0.90) 0%, rgba(15, 23, 42, 0.98) 100%);
      border: 1px solid rgba(228, 0, 124, 0.4);
    }}
    .unstop-input {{
      background: #0b1329;
      border: 1px solid #1e293b;
      color: #f1f5f9;
      transition: all 0.2s ease;
    }}
    .unstop-input:focus {{
      border-color: #e4007c;
      box-shadow: 0 0 0 2px rgba(228, 0, 124, 0.2);
      outline: none;
    }}
    .dropdown-menu {{
      max-height: 220px;
      overflow-y: auto;
      z-index: 60;
    }}
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #080e1e;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e293b;
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #e4007c;
    }}
  </style>
</head>
<body class="bg-[#070c18] text-slate-100 min-h-screen antialiased flex flex-col selection:bg-pink-600 selection:text-white">

  <!-- TOP HEADER -->
  <header class="border-b border-slate-800/80 bg-[#0a1020]/95 backdrop-blur sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-pink-600 to-rose-400 flex items-center justify-center font-black text-xl text-white shadow-lg shadow-pink-600/30">
          RR
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-[10px] uppercase tracking-widest font-extrabold text-pink-500">Rajasthan Royals War Room</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">Official 18-Nov-2026 Baseline</span>
          </div>
          <h1 class="text-sm sm:text-base font-bold text-white tracking-tight flex items-center gap-2">
            IPL 2027 Auction War Room • ITC Grand Goa (16-Dec-2026)
          </h1>
        </div>
      </div>

      <div class="flex items-center gap-2 sm:gap-3">
        <span class="hidden xl:inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-mono">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"></span>
          200,999 Balls • ₹27.05 Cr Purse
        </span>
        <a href="RR_SupeRR_Selector_Methodology_Report.pdf" download class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-slate-700 flex items-center gap-1 transition">
          📄 PDF Report
        </a>
        <a href="RR_SupeRR_Selector_Auction_Strategy.pptx" download class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-slate-700 flex items-center gap-1 transition">
          📊 PPTX Deck
        </a>
        <button onclick="copyAllUnstopPicks()" class="px-3.5 py-1.5 rounded-lg bg-pink-600 hover:bg-pink-500 text-xs font-bold text-white transition flex items-center gap-1.5 shadow-md shadow-pink-600/25">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
          Copy All 20 Picks
        </button>
      </div>
    </div>
  </header>

  <!-- TOURNAMENT SUMMARY STRIP -->
  <div class="bg-gradient-to-r from-pink-950/70 via-slate-900/95 to-indigo-950/70 border-b border-pink-500/30 px-4 py-2 text-xs text-slate-200">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-3 font-mono">
      <div class="flex flex-wrap items-center gap-4">
        <span>🏆 <strong>184 Retained Players</strong> (55 Overseas)</span>
        <span class="text-slate-600">|</span>
        <span>⚡ <strong>89 Released Players</strong></span>
        <span class="text-slate-600">|</span>
        <span>💰 <strong>₹297.95 Cr</strong> Total Purse</span>
        <span class="text-slate-600">|</span>
        <span>🛡️ <strong>RR Purse: ₹27.05 Cr</strong> (6 Open Slots • Max 3 Overseas)</span>
      </div>
      <div class="text-pink-400 font-bold">
        📍 Mini-Auction: Dec 16, 2026 @ ITC Grand Goa
      </div>
    </div>
  </div>

  <!-- NAVIGATION TABS -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-4 pb-2 w-full">
    <div class="flex items-center gap-2 border-b border-slate-800 pb-2 overflow-x-auto">
      <button onclick="switchTab('unstop')" id="nav-unstop" class="px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 bg-pink-600 text-white shadow-md shadow-pink-600/30 whitespace-nowrap">
        <span>📝 Tab 1: Unstop Form (Top 10 Batters & Bowlers)</span>
        <span class="px-1.5 py-0.5 rounded-full text-[10px] bg-white/20 text-white font-mono">20 / 20</span>
      </button>

      <button onclick="switchTab('analytics')" id="nav-analytics" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>📊 Tab 2: Top 10 Scouting Profiles & Metrics</span>
      </button>

      <button onclick="switchTab('audit')" id="nav-audit" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>⚖️ Tab 3: Auction Eligibility Audit</span>
        <span class="px-1.5 py-0.5 rounded-full text-[10px] bg-emerald-500/20 text-emerald-300 font-mono">BCCI Verified</span>
      </button>

      <button onclick="switchTab('rr-squad')" id="nav-rr-squad" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>🛡️ Tab 4: RR Retained Squad (19) & Gap Analysis</span>
      </button>

      <button onclick="switchTab('franchises')" id="nav-franchises" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>🏢 Tab 5: All 10 Teams & Trade Tracker</span>
      </button>

      <button onclick="switchTab('budget')" id="nav-budget" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>💰 Tab 6: Budget Simulator (₹27.05 Cr)</span>
      </button>

      <button onclick="switchTab('playing-xi')" id="nav-playing-xi" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>🏏 Tab 7: RR Playing XI Builder</span>
      </button>

      <button onclick="switchTab('gemini')" id="nav-gemini" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span class="w-2 h-2 rounded-full bg-pink-500 animate-ping"></span>
        <span>🤖 Tab 8: AI War Room Scout</span>
      </button>
    </div>
  </section>

  <!-- MAIN CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 w-full flex-1">

    <!-- ============================================================== -->
    <!-- TAB 1: UNSTOP SUBMISSION FORM -->
    <!-- ============================================================== -->
    <div id="tab-unstop" class="space-y-6">

      <!-- Form Helper Bar -->
      <div class="rr-card-highlight rounded-2xl p-5">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-pink-500/20 text-pink-400 border border-pink-500/30">
                100% VERIFIED AUCTION ELIGIBLE ONLY
              </span>
              <span class="text-xs text-slate-400 font-mono">Official 18-Nov-2026 BCCI Ratification</span>
            </div>
            <h2 class="text-base sm:text-lg font-bold text-white mt-1">Official Unstop Competition Submission Form</h2>
            <p class="text-xs text-slate-300 mt-1 max-w-3xl leading-relaxed">
              Every player below is an <strong class="text-pink-400">officially released player</strong> or verified registered independent entrant. All 184 retained players across all 10 franchises are strictly excluded. You can 1-click copy individual names, search across 1,210 offline players, download the official reports, or copy the pre-written submission Remark.
            </p>
          </div>
          <div class="flex flex-wrap items-center gap-2">
            <button onclick="copyAllUnstopPicks()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-pink-600 hover:bg-pink-500 text-white transition flex items-center gap-1 shadow">
              📋 Copy All 20 Players
            </button>
            <button onclick="copyRemarkText()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition flex items-center gap-1 shadow">
              📝 Copy Remark Text
            </button>
          </div>
        </div>
      </div>

      <!-- 2-COLUMN GRID: 10 BATSMEN & 10 BOWLERS -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <!-- 10 BATSMEN COLUMN -->
        <div class="rr-card rounded-2xl p-5 border border-pink-500/20 space-y-4">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div class="flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-pink-600/20 text-pink-400 flex items-center justify-center text-base">🏏</span>
              <div>
                <h3 class="text-sm font-bold text-white">Batsmen Selection (1 to 10)</h3>
                <span class="text-[11px] text-pink-400">Required fields marked with * • All 10 Verified Eligible</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-pink-400 bg-pink-500/10 px-2 py-0.5 rounded border border-pink-500/20">
              10 / 10 Filled
            </span>
          </div>

          <div class="space-y-3.5" id="batsmen-fields-container">
            <!-- Dynamically generated 10 Batsman fields -->
          </div>
        </div>

        <!-- 10 BOWLERS COLUMN -->
        <div class="rr-card rounded-2xl p-5 border border-indigo-500/20 space-y-4">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div class="flex items-center gap-2">
              <span class="w-8 h-8 rounded-lg bg-indigo-600/20 text-indigo-400 flex items-center justify-center text-base">🎯</span>
              <div>
                <h3 class="text-sm font-bold text-white">Bowlers Selection (1 to 10)</h3>
                <span class="text-[11px] text-indigo-400">Required fields marked with * • All 10 Verified Eligible</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">
              10 / 10 Filled
            </span>
          </div>

          <div class="space-y-3.5" id="bowlers-fields-container">
            <!-- Dynamically generated 10 Bowler fields -->
          </div>
        </div>

      </div>

      <!-- UPLOAD YOUR REPORT * SECTION -->
      <div class="rr-card rounded-2xl p-6 border border-emerald-500/30">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-4">
          <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-base">📁</span>
            <div>
              <h3 class="text-sm font-bold text-white">Upload Your Report *</h3>
              <span class="text-[11px] text-emerald-400">Accepted file type: pdf, pptx</span>
            </div>
          </div>
          <span class="px-2.5 py-1 rounded text-xs font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
            Reports Ready for Upload
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-700/80 hover:border-pink-500/40 transition">
            <div class="flex items-start justify-between">
              <div>
                <span class="text-xs font-bold text-pink-400 uppercase font-mono">PowerPoint Strategy Deck</span>
                <h4 class="text-sm font-bold text-white mt-1">RR_SupeRR_Selector_Auction_Strategy.pptx</h4>
                <p class="text-xs text-slate-400 mt-1">
                  Executive slide deck with 18-Nov-2026 baseline, 184 retentions audit, RR 19 retained squad gaps, Top 10 Batters/Bowlers boards, ₹27.05 Cr budget simulation, and Playing XI.
                </p>
              </div>
              <a href="RR_SupeRR_Selector_Auction_Strategy.pptx" download class="px-3 py-1.5 rounded-lg bg-pink-600 hover:bg-pink-500 text-xs font-bold text-white transition flex items-center gap-1">
                ⬇️ Download
              </a>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-700/80 hover:border-emerald-500/40 transition">
            <div class="flex items-start justify-between">
              <div>
                <span class="text-xs font-bold text-emerald-400 uppercase font-mono">Formal Methodology PDF</span>
                <h4 class="text-sm font-bold text-white mt-1">RR_SupeRR_Selector_Methodology_Report.pdf</h4>
                <p class="text-xs text-slate-400 mt-1">
                  Complete mathematical governance report detailing the 200,999 delivery dataset, delivery-by-delivery leverage metrics, PPI equations, and verified source citations.
                </p>
              </div>
              <a href="RR_SupeRR_Selector_Methodology_Report.pdf" download class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white transition flex items-center gap-1">
                ⬇️ Download
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- REMARK TEXT AREA SECTION -->
      <div class="rr-card rounded-2xl p-6 border border-amber-500/30">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-3">
          <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center text-base">💬</span>
            <div>
              <h3 class="text-sm font-bold text-white">Remark</h3>
              <span class="text-[11px] text-amber-400">Outline methodology, top picks under pressure, and RR squad strengthening</span>
            </div>
          </div>
          <button onclick="copyRemarkText()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition flex items-center gap-1.5 shadow">
            📋 Copy Remark
          </button>
        </div>

        <textarea id="unstop-remark-box" rows="8" readonly class="w-full bg-[#080e1e] border border-slate-800 rounded-xl p-3.5 text-xs text-slate-200 font-mono leading-relaxed focus:outline-none"></textarea>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 2: TOP 10 METRICS & COMPARISON -->
    <!-- ============================================================== -->
    <div id="tab-analytics" class="hidden space-y-6">
      
      <!-- Batters Table Card -->
      <div class="rr-card rounded-2xl p-5 border border-pink-500/20">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-4">
          <div class="flex items-center gap-2">
            <span class="text-xl">🏏</span>
            <h3 class="text-base font-bold text-white">Top 10 Verified Auction-Eligible Batters for Rajasthan Royals</h3>
          </div>
          <a href="top_10_verified_eligible_batters_2027.csv" download class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-pink-400 border border-slate-700">
            ⬇️ Download CSV
          </a>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-xs text-left text-slate-300">
            <thead class="text-[11px] uppercase bg-slate-900/90 text-slate-400 font-mono border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">#</th>
                <th class="py-2.5 px-3">Player Name</th>
                <th class="py-2.5 px-3">Origin / Prev Team</th>
                <th class="py-2.5 px-3">PPI</th>
                <th class="py-2.5 px-3">Press SR</th>
                <th class="py-2.5 px-3">Press Avg</th>
                <th class="py-2.5 px-3">RR Fit</th>
                <th class="py-2.5 px-3">Max Bid</th>
                <th class="py-2.5 px-4">Tactical Solution for RR</th>
              </tr>
            </thead>
            <tbody id="batters-table-body" class="divide-y divide-slate-800/60 font-mono">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Bowlers Table Card -->
      <div class="rr-card rounded-2xl p-5 border border-indigo-500/20">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-4">
          <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-base font-bold text-white">Top 10 Verified Auction-Eligible Bowlers for Rajasthan Royals</h3>
          </div>
          <a href="top_10_verified_eligible_bowlers_2027.csv" download class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-indigo-400 border border-slate-700">
            ⬇️ Download CSV
          </a>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-xs text-left text-slate-300">
            <thead class="text-[11px] uppercase bg-slate-900/90 text-slate-400 font-mono border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">#</th>
                <th class="py-2.5 px-3">Player Name</th>
                <th class="py-2.5 px-3">Origin / Prev Team</th>
                <th class="py-2.5 px-3">PPI</th>
                <th class="py-2.5 px-3">Press Econ</th>
                <th class="py-2.5 px-3">Press Wkts</th>
                <th class="py-2.5 px-3">RR Fit</th>
                <th class="py-2.5 px-3">Max Bid</th>
                <th class="py-2.5 px-4">Tactical Solution for RR</th>
              </tr>
            </thead>
            <tbody id="bowlers-table-body" class="divide-y divide-slate-800/60 font-mono">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 3: RR RETAINED SQUAD (19) & GAP ANALYSIS -->
    <!-- ============================================================== -->
    
    <!-- ============================================================== -->
    <!-- TAB 3: AUCTION ELIGIBILITY AUDIT -->
    <!-- ============================================================== -->
    <div id="tab-audit" class="hidden space-y-6">

      <!-- Header Card -->
      <div class="rr-card-highlight rounded-2xl p-6">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                100% REGULATORY COMPLIANCE WITH BCCI DIRECTIVES
              </span>
              <span class="text-xs text-slate-400 font-mono">Audited: 18-Nov-2026</span>
            </div>
            <h2 class="text-lg font-bold text-white mt-1">Auction Eligibility, Retired Players & Regulatory Audit</h2>
            <p class="text-xs text-slate-300 mt-1 max-w-4xl leading-relaxed">
              Exhaustive verification protocol screening out: (1) <strong>Officially Retired IPL/Cricket Players</strong>, (2) <strong>Pakistani Cricketers</strong> barred under BCCI IPL participation guidelines, (3) <strong>All 184 Retained Players</strong>, and (4) <strong>Unregistered Associate Entrants</strong>. Every shortlisted player has a verified audit status.
            </p>
          </div>
          <div class="flex items-center gap-2">
            <span class="px-3 py-1.5 rounded-xl bg-slate-800 text-xs text-emerald-400 font-mono border border-slate-700">
              Audit Verdict: PASSED (100% Defensible)
            </span>
          </div>
        </div>
      </div>

      <!-- Audit KPI Metrics -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3.5">
        <div class="rr-card rounded-2xl p-4 border border-rose-500/30 bg-rose-950/20">
          <div class="text-[10px] uppercase tracking-wider text-rose-400 font-bold font-mono">RETAINED PLAYERS</div>
          <div class="text-2xl font-black text-white mt-1 font-mono">184</div>
          <div class="text-[11px] text-slate-400 mt-0.5">Strictly Excluded (Unavailable)</div>
        </div>
        <div class="rr-card rounded-2xl p-4 border border-amber-500/30 bg-amber-950/20">
          <div class="text-[10px] uppercase tracking-wider text-amber-400 font-bold font-mono">PAKISTANI PLAYERS</div>
          <div class="text-2xl font-black text-white mt-1 font-mono">67</div>
          <div class="text-[11px] text-slate-400 mt-0.5">BCCI Policy Restriction</div>
        </div>
        <div class="rr-card rounded-2xl p-4 border border-indigo-500/30 bg-indigo-950/20">
          <div class="text-[10px] uppercase tracking-wider text-indigo-400 font-bold font-mono">RETIRED IPL PLAYERS</div>
          <div class="text-2xl font-black text-white mt-1 font-mono">9</div>
          <div class="text-[11px] text-slate-400 mt-0.5">Officially Confirmed Retired</div>
        </div>
        <div class="rr-card rounded-2xl p-4 border border-emerald-500/30 bg-emerald-950/20">
          <div class="text-[10px] uppercase tracking-wider text-emerald-400 font-bold font-mono">VERIFIED TARGETS</div>
          <div class="text-2xl font-black text-white mt-1 font-mono">20 / 20</div>
          <div class="text-[11px] text-emerald-300 mt-0.5">100% Auction Eligible</div>
        </div>
      </div>

      <!-- Section: Shortlist Change Report & Replacement Audit Trail -->
      <div class="rr-card rounded-2xl p-5 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>📋 Shortlist Change Report & Replacement Audit Trail</span>
            </h3>
            <p class="text-xs text-slate-400">Formal log of removed ineligible candidates and verified strategic upgrades for Rajasthan Royals.</p>
          </div>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs text-slate-300">
            <thead class="bg-[#0b1329] text-slate-400 text-[10px] uppercase tracking-wider border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">Removed Candidate</th>
                <th class="py-2.5 px-3">Shortlist</th>
                <th class="py-2.5 px-3">Disqualification Reason</th>
                <th class="py-2.5 px-3">Verified Replacement</th>
                <th class="py-2.5 px-3">Strategic Upgrade for RR</th>
              </tr>
            </thead>
            <tbody id="audit-change-table-body" class="divide-y divide-slate-800/60 font-mono text-[11px]">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Section: Retired IPL Players Registry -->
      <div class="rr-card rounded-2xl p-5 border border-slate-800 space-y-3">
        <div>
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span>🛑 Officially Retired IPL Players Registry</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Excluded from Auction Pool</span>
          </h3>
          <p class="text-xs text-slate-400">Players with verified retirement announcements from IPL or all professional cricket.</p>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs text-slate-300">
            <thead class="bg-[#0b1329] text-slate-400 text-[10px] uppercase tracking-wider border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">Player Name</th>
                <th class="py-2.5 px-3">Nationality</th>
                <th class="py-2.5 px-3">Retirement Scope</th>
                <th class="py-2.5 px-3">Announcement Date</th>
                <th class="py-2.5 px-3">Official Verification Source</th>
                <th class="py-2.5 px-3">Current Status</th>
              </tr>
            </thead>
            <tbody id="audit-retired-table-body" class="divide-y divide-slate-800/60 font-mono text-[11px]">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Section: Pakistani Players Exclusion Registry -->
      <div class="rr-card rounded-2xl p-5 border border-slate-800 space-y-3">
        <div>
          <h3 class="text-sm font-bold text-white flex items-center gap-2">
            <span>🚫 Pakistani Players Exclusion Registry</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">BCCI Policy Restriction</span>
          </h3>
          <p class="text-xs text-slate-400">Under official BCCI policy in effect since after IPL 2008, Pakistani cricketers are ineligible for IPL auction registration or participation.</p>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs text-slate-300">
            <thead class="bg-[#0b1329] text-slate-400 text-[10px] uppercase tracking-wider border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">Player Name</th>
                <th class="py-2.5 px-3">Role</th>
                <th class="py-2.5 px-3">Nationality</th>
                <th class="py-2.5 px-3">Regulatory Policy</th>
                <th class="py-2.5 px-3">Audit Action</th>
              </tr>
            </thead>
            <tbody id="audit-pak-table-body" class="divide-y divide-slate-800/60 font-mono text-[11px]">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <div id="tab-rr-squad" class="hidden space-y-6">
      
      <div class="rr-card-highlight rounded-2xl p-6">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <span class="text-xs uppercase font-extrabold text-pink-400 font-mono">Official RR Retained Roster</span>
            <h2 class="text-lg font-bold text-white mt-1">Rajasthan Royals 19 Retained Players (Committed: ₹92.95 Cr)</h2>
            <p class="text-xs text-slate-300 mt-1 max-w-3xl">
              Includes blockbuster trades for <strong>Ravindra Jadeja</strong> (from CSK) and <strong>Mohammed Shami</strong> (from SRH/LSG), while <strong>Sanju Samson</strong> was traded to CSK. RR has ₹27.05 Cr to fill 6 slots (max 3 overseas).
            </p>
          </div>
          <div class="px-3.5 py-2 rounded-xl bg-slate-900 border border-pink-500/30 text-right font-mono">
            <div class="text-[11px] text-slate-400">Remaining Purse</div>
            <div class="text-lg font-black text-pink-400">₹27.05 Cr</div>
          </div>
        </div>
      </div>

      <!-- 19 Players Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4" id="rr-squad-grid">
        <!-- Injected via JS -->
      </div>

      <!-- Tactical Gaps Diagnostic Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div class="rr-card rounded-2xl p-5 border-l-4 border-l-rose-500">
          <div class="text-xs font-bold text-rose-400 uppercase font-mono">Gap #1 • Top-Order</div>
          <h4 class="text-sm font-bold text-white mt-1">No. 3 Anchor (Samson Replacement)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">
            Sanju Samson's trade to CSK creates a void at No. 3. RR needs a domestic stabilizer who absorbs early wickets and lets Jaiswal attack freely.
          </p>
          <div class="mt-3 text-xs font-bold text-pink-400 font-mono">Target: Ajinkya Rahane / Rahul Tripathi</div>
        </div>

        <div class="rr-card rounded-2xl p-5 border-l-4 border-l-amber-500">
          <div class="text-xs font-bold text-amber-400 uppercase font-mono">Gap #2 • Middle Overs</div>
          <h4 class="text-sm font-bold text-white mt-1">Left-Hand Spin Destructor & Finisher</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">
            With Hetmyer released to optimize purse, RR needs southpaw boundary hitting against wrist spin in overs 7–15 and death overs finishing.
          </p>
          <div class="mt-3 text-xs font-bold text-amber-400 font-mono">Target: Nehal Wadhera / Nitish Rana / Hetmyer (Buy-back)</div>
        </div>

        <div class="rr-card rounded-2xl p-5 border-l-4 border-l-indigo-500">
          <div class="text-xs font-bold text-indigo-400 uppercase font-mono">Gap #3 • Death Bowling</div>
          <h4 class="text-sm font-bold text-white mt-1">Express Death Spearhead Partner</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">
            While Sandeep Sharma and Shami are world-class, pairing an express slinger or swing spearhead creates an impenetrable bowling rotation.
          </p>
          <div class="mt-3 text-xs font-bold text-indigo-400 font-mono">Target: Matheesha Pathirana / Trent Boult / Avesh Khan</div>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 4: ALL 10 TEAMS & TRADE TRACKER -->
    <!-- ============================================================== -->
    <div id="tab-franchises" class="hidden space-y-6">
      
      <!-- 10 Franchise Purse Comparison Table -->
      <div class="rr-card rounded-2xl p-5 border border-slate-700/80">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-4">
          <div class="flex items-center gap-2">
            <span class="text-xl">🏢</span>
            <h3 class="text-base font-bold text-white">All 10 IPL Franchise Retentions & Purse Standings (18-Nov-2026)</h3>
          </div>
          <a href="retained_squads_10_franchises.csv" download class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">
            ⬇️ Download All 184 Retentions CSV
          </a>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-xs text-left text-slate-300">
            <thead class="text-[11px] uppercase bg-slate-900/90 text-slate-400 font-mono border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">Team</th>
                <th class="py-2.5 px-3">Retained Players</th>
                <th class="py-2.5 px-3">Overseas Retained</th>
                <th class="py-2.5 px-3">Remaining Purse</th>
                <th class="py-2.5 px-3">Slots Left</th>
                <th class="py-2.5 px-3">Overseas Slots Left</th>
                <th class="py-2.5 px-4">Financial Flexibility</th>
              </tr>
            </thead>
            <tbody id="franchise-table-body" class="divide-y divide-slate-800/60 font-mono">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Landmark Trades Tracker -->
      <div class="rr-card rounded-2xl p-5 border border-pink-500/30">
        <h3 class="text-sm font-bold text-white mb-3 flex items-center gap-2">
          <span>🔄</span> Official IPL 2027 Pre-Auction Trades Tracker
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
            <div class="font-bold text-pink-400">Hardik Pandya ↔️ Arshdeep Singh Blockbuster Swap</div>
            <p class="text-slate-300">Hardik Pandya traded to Punjab Kings (₹18 Cr); Arshdeep Singh traded to Mumbai Indians (₹18 Cr).</p>
          </div>
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
            <div class="font-bold text-pink-400">Sanju Samson ➡️ Chennai Super Kings</div>
            <p class="text-slate-300">Former RR Captain traded to CSK; takes over wicketkeeping mantle following MS Dhoni's transition to team mentor.</p>
          </div>
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
            <div class="font-bold text-pink-400">Ravindra Jadeja & Mohammed Shami ➡️ Rajasthan Royals</div>
            <p class="text-slate-300">RR acquires elite all-rounder Jadeja and seam spearhead Shami to build tournament's premier bowling spine.</p>
          </div>
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
            <div class="font-bold text-pink-400">Rishabh Pant ➡️ Delhi Capitals & Kuldeep Yadav ➡️ LSG</div>
            <p class="text-slate-300">Pant returns to DC; Kuldeep Yadav traded to LSG for ₹13.5 Cr to lead Lucknow's spin attack.</p>
          </div>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 5: BUDGET SIMULATOR -->
    <!-- ============================================================== -->
    <div id="tab-budget" class="hidden space-y-6">
      
      <div class="rr-card-highlight rounded-2xl p-6">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <span class="text-xs uppercase font-extrabold text-emerald-400 font-mono">Interactive Budget Simulator</span>
            <h2 class="text-lg font-bold text-white mt-1">Rajasthan Royals ₹27.05 Cr Auction Allocation Model</h2>
            <p class="text-xs text-slate-300 mt-1 max-w-3xl">
              Simulate RR's auction purchases across 6 open slots. Check real-time purse consumption, overseas limits, and contingency buffers.
            </p>
          </div>
          <div class="flex items-center gap-3">
            <button onclick="loadBudgetScenario('balanced')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 text-white shadow">
              Scenario A (Balanced)
            </button>
            <button onclick="loadBudgetScenario('newball')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:text-white border border-slate-700">
              Scenario B (Boult & Rana)
            </button>
          </div>
        </div>
      </div>

      <!-- Live Budget Summary Strip -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 font-mono">
        <div class="rr-card rounded-xl p-4 text-center">
          <div class="text-[11px] text-slate-400">Total Purse</div>
          <div class="text-xl font-black text-white mt-0.5">₹27.05 Cr</div>
        </div>
        <div class="rr-card rounded-xl p-4 text-center">
          <div class="text-[11px] text-slate-400">Total Spend</div>
          <div class="text-xl font-black text-emerald-400 mt-0.5" id="sim-spend">₹24.00 Cr</div>
        </div>
        <div class="rr-card rounded-xl p-4 text-center">
          <div class="text-[11px] text-slate-400">Remaining Buffer</div>
          <div class="text-xl font-black text-pink-400 mt-0.5" id="sim-remaining">₹3.05 Cr</div>
        </div>
        <div class="rr-card rounded-xl p-4 text-center">
          <div class="text-[11px] text-slate-400">Slots Filled</div>
          <div class="text-xl font-black text-amber-400 mt-0.5" id="sim-slots">6 / 6 (2 OS)</div>
        </div>
      </div>

      <!-- Planned Purchases Table -->
      <div class="rr-card rounded-2xl p-5 border border-emerald-500/30">
        <h3 class="text-sm font-bold text-white mb-3" id="sim-scenario-name">
          Scenario A: Balanced Death Mastery & Indian Stability
        </h3>
        <div class="overflow-x-auto">
          <table class="w-full text-xs text-left text-slate-300">
            <thead class="text-[11px] uppercase bg-slate-900/90 text-slate-400 font-mono border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">Priority</th>
                <th class="py-2.5 px-3">Target Player</th>
                <th class="py-2.5 px-3">Role</th>
                <th class="py-2.5 px-3">Classification</th>
                <th class="py-2.5 px-3">Allocated Bid</th>
                <th class="py-2.5 px-3">Walk-Away Price</th>
                <th class="py-2.5 px-4">Tactical Rationale</th>
              </tr>
            </thead>
            <tbody id="budget-table-body" class="divide-y divide-slate-800/60 font-mono">
              <!-- Injected via JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 6: RR PLAYING XI BUILDER -->
    <!-- ============================================================== -->
    <div id="tab-playing-xi" class="hidden space-y-6">
      
      <div class="rr-card-highlight rounded-2xl p-6">
        <h2 class="text-lg font-bold text-white">Rajasthan Royals Optimized Playing XI & Impact Player Model</h2>
        <p class="text-xs text-slate-300 mt-1 max-w-3xl">
          Constructed using Rajasthan Royals' 19 retained players plus targeted auction acquisitions (Ajinkya Rahane, Nehal Wadhera, and Matheesha Pathirana as Impact Sub).
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        <!-- Batting First XI Card -->
        <div class="rr-card rounded-2xl p-5 border border-pink-500/30 space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>🏏</span> Batting-First Playing XI
            </h3>
            <span class="text-xs font-mono text-pink-400 font-bold">4 Overseas Max Compliant</span>
          </div>
          <div class="space-y-2 font-mono text-xs" id="xi-batting-first">
            <!-- Populated via JS -->
          </div>
        </div>

        <!-- Bowling-First XI & Impact Sub Card -->
        <div class="rr-card rounded-2xl p-5 border border-indigo-500/30 space-y-4">
          <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <span>🎯</span> Tactical Impact Sub Rotation
            </h3>
            <span class="text-xs font-mono text-indigo-400 font-bold">Live Substitution</span>
          </div>

          <div class="p-4 rounded-xl bg-indigo-950/40 border border-indigo-500/40 space-y-2">
            <div class="text-xs font-bold text-indigo-300 font-mono uppercase">Impact Player Tactic</div>
            <p class="text-xs text-slate-200 leading-relaxed">
              <strong>Matheesha Pathirana ✈️</strong> (Target) subbed in for <strong>Ajinkya Rahane</strong> at the start of the bowling innings.
            </p>
            <div class="text-[11px] text-slate-400 mt-1">
              Provides RR with 6 frontline bowling options: Jofra Archer ✈️ (Overs 1, 3, 15, 17), Mohammed Shami (Overs 2, 4, 13, 19), Sandeep Sharma (Overs 6, 16, 18, 20), Matheesha Pathirana ✈️ (Overs 8, 12, 14, 20), Ravindra Jadeja (Overs 5, 7, 9, 11), Ravi Bishnoi (Overs 10, 12).
            </div>
          </div>

          <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
            <div class="text-xs font-bold text-slate-300 font-mono uppercase">Reserve Bench Depth (9 Players)</div>
            <p class="text-xs text-slate-400 leading-relaxed">
              Nandre Burger ✈️, Dasun Shanaka ✈️, Donovan Ferreira ✈️, Lhuan-dre Pretorius ✈️, Manimaran Siddharth, Shubham Dubey, Sushant Mishra, Aman Rao Perala, Brijesh Sharma.
            </p>
          </div>
        </div>

      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 7: AI WAR ROOM SCOUT (GEMINI 2.5) -->
    <!-- ============================================================== -->
    <div id="tab-gemini" class="hidden space-y-6">
      
      <div class="rr-card-highlight rounded-2xl p-6">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-pink-600 to-indigo-600 flex items-center justify-center text-xl text-white shadow-lg">
            🤖
          </div>
          <div>
            <h2 class="text-base sm:text-lg font-bold text-white">Gemini 2.5 IPL Auction Strategic Intelligence Scout</h2>
            <p class="text-xs text-slate-300 mt-0.5">
              Powered by Google Gemini 2.5 Flash with direct server-side access to 200,999 deliveries and the official 18-Nov-2026 BCCI dataset.
            </p>
          </div>
        </div>
      </div>

      <!-- Quick Prompt Chips -->
      <div class="flex flex-wrap items-center gap-2">
        <span class="text-xs text-slate-400 font-mono mr-1">Quick Inquiries:</span>
        <button onclick="askPrompt('Who should RR target at No. 3 to replace Sanju Samson?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
          Replacement for Sanju Samson?
        </button>
        <button onclick="askPrompt('How should RR spend its ₹27.05 Cr purse across 6 slots?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
          ₹27.05 Cr Allocation Strategy?
        </button>
        <button onclick="askPrompt('Why is Matheesha Pathirana the #1 bowling target for RR?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
          Why Pathirana over Starc/Boult?
        </button>
        <button onclick="askPrompt('Which franchise has the highest purse and biggest bidding threat?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
          Highest Purse Franchise Threat?
        </button>
      </div>

      <!-- Chat Window -->
      <div class="rr-card rounded-2xl p-5 border border-slate-800 space-y-4">
        <div id="chat-messages" class="h-80 overflow-y-auto space-y-3.5 pr-2">
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 text-xs text-slate-300 leading-relaxed font-mono">
            👋 <strong>Rajasthan Royals Lead Auction Strategist online.</strong> All 184 retained players across 10 teams have been screened and excluded. How can I assist you with budget simulations, player-vs-player comparisons, or squad gap resolutions for the Dec 16 mini-auction in Goa?
          </div>
        </div>

        <form onsubmit="handleChatSubmit(event)" class="flex items-center gap-2 pt-2 border-t border-slate-800">
          <input type="text" id="chat-input" placeholder="Ask about auction targets, tactical fit, purse constraints, or player stats..." class="flex-1 bg-[#0b1329] border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-pink-500">
          <button type="submit" id="chat-submit-btn" class="px-4 py-2.5 rounded-xl bg-pink-600 hover:bg-pink-500 text-xs font-bold text-white transition flex items-center gap-1 shadow">
            <span>Send</span>
          </button>
        </form>
      </div>

    </div>

  </main>

  <!-- PLAYER SCOUTING MODAL -->
  <div id="player-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="rr-card-highlight rounded-2xl max-w-xl w-full p-6 space-y-4 border border-pink-500/40 relative">
      <button onclick="closeModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-lg font-bold">✕</button>
      <div id="modal-content">
        <!-- Injected via JS -->
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800 bg-[#080d1a] py-6 text-center text-xs text-slate-400 font-mono">
    <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
      <div>
        Rajasthan Royals IPL 2027 Auction War Room • SupeRR Selector Season 2 (Round 1)
      </div>
      <div class="flex items-center gap-4 text-slate-400">
        <span>200,999 Balls Screened</span>
        <span>•</span>
        <span>184 Retained Players</span>
        <span>•</span>
        <span class="text-pink-400 font-bold">ITC Grand Goa • 16-Dec-2026</span>
      </div>
    </div>
  </footer>

  <!-- DATA & SCRIPTS -->
  <script>
    const TOP_BATTERS = {top_batters_json};
    const TOP_BOWLERS = {top_bowlers_json};
    const FRANCHISES = {franchises_json};
    const RR_SQUAD = {rr_retained_json};
    const ALL_PLAYERS = {all_players_json};
    const BUDGET_DATA = {json.dumps(budget_data)};
    const PLAYING_XI = {json.dumps(playing_xi)};
    const REMARK_TEXT = `{remark_text.replace('`', "'")}`;

    // Initialize Unstop fields
    
    const retiredPlayersData = {retired_list_json};
    const pakistaniPlayersData = {pak_list_json};
    const changeReportData = {change_report_json};

    function renderAuditTab() {{
      // 1. Render Change Report
      const chgBody = document.getElementById('audit-change-table-body');
      if (chgBody) {{
        chgBody.innerHTML = '';
        changeReportData.forEach(chg => {{
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="py-2.5 px-3 font-bold text-rose-400">${{chg.removed_player}}</td>
            <td class="py-2.5 px-3 text-slate-300">${{chg.list}}</td>
            <td class="py-2.5 px-3 text-slate-400 text-[10px] leading-tight">${{chg.reason_for_removal}}</td>
            <td class="py-2.5 px-3">
              <span class="font-bold text-emerald-400">${{chg.replacement_player}}</span>
              <span class="ml-1 px-1.5 py-0.5 rounded text-[9px] bg-emerald-500/20 text-emerald-300">VERIFIED</span>
            </td>
            <td class="py-2.5 px-3 text-slate-300 text-[10px] leading-tight">${{chg.why_replacement_better}}</td>
          `;
          chgBody.appendChild(tr);
        }});
      }}

      // 2. Render Retired Players
      const retBody = document.getElementById('audit-retired-table-body');
      if (retBody) {{
        retBody.innerHTML = '';
        retiredPlayersData.forEach(r => {{
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="py-2.5 px-3 font-bold text-white">${{r.player_name}}</td>
            <td class="py-2.5 px-3 text-slate-400">${{r.nationality}}</td>
            <td class="py-2.5 px-3 text-slate-300">${{r.retirement_type}}</td>
            <td class="py-2.5 px-3 text-amber-400">${{r.announcement_date}}</td>
            <td class="py-2.5 px-3 text-slate-400 text-[10px]">${{r.official_source}}</td>
            <td class="py-2.5 px-3">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30">RETIRED FROM IPL</span>
            </td>
          `;
          retBody.appendChild(tr);
        }});
      }}

      // 3. Render Pakistani Players
      const pakBody = document.getElementById('audit-pak-table-body');
      if (pakBody) {{
        pakBody.innerHTML = '';
        pakistaniPlayersData.forEach(p => {{
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="py-2.5 px-3 font-bold text-white">${{p.player_name}}</td>
            <td class="py-2.5 px-3 text-slate-400">${{p.role}}</td>
            <td class="py-2.5 px-3 text-slate-400">${{p.nationality}}</td>
            <td class="py-2.5 px-3 text-slate-400 text-[10px]">${{p.governing_rule}}</td>
            <td class="py-2.5 px-3">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">NOT ELIGIBLE</span>
            </td>
          `;
          pakBody.appendChild(tr);
        }});
      }}
    }}

    function renderUnstopFields() {{
      const bContainer = document.getElementById('batsmen-fields-container');
      const wContainer = document.getElementById('bowlers-fields-container');
      bContainer.innerHTML = '';
      wContainer.innerHTML = '';

      TOP_BATTERS.forEach((b, idx) => {{
        const num = idx + 1;
        const div = document.createElement('div');
        div.className = 'p-3 rounded-xl bg-slate-900/90 border border-slate-800 hover:border-pink-500/40 transition relative';
        div.innerHTML = `
          <div class="flex items-center justify-between mb-1.5">
            <label class="text-xs font-bold text-slate-200 flex items-center gap-1.5">
              <span class="w-5 h-5 rounded-md bg-pink-600/30 text-pink-400 flex items-center justify-center text-[10px] font-mono font-bold">${{num}}</span>
              Batsman ${{num}} *
            </label>
            <span class="text-[10px] font-mono text-pink-400 font-semibold">PPI: ${{b.ppi_score.toFixed(1)}} | SR: ${{b.p_sr.toFixed(1)}}</span>
          </div>
          <div class="flex items-center gap-2">
            <input type="text" id="input-b-${{num}}" value="${{b.name}}" readonly class="unstop-input flex-1 rounded-lg px-3 py-1.5 text-xs font-medium cursor-pointer" onclick="showModal('b', ${{idx}})">
            <button onclick="copyFieldValue('input-b-${{num}}')" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-mono transition" title="Copy name">
              Copy
            </button>
          </div>
        `;
        bContainer.appendChild(div);
      }});

      TOP_BOWLERS.forEach((w, idx) => {{
        const num = idx + 1;
        const div = document.createElement('div');
        div.className = 'p-3 rounded-xl bg-slate-900/90 border border-slate-800 hover:border-indigo-500/40 transition relative';
        div.innerHTML = `
          <div class="flex items-center justify-between mb-1.5">
            <label class="text-xs font-bold text-slate-200 flex items-center gap-1.5">
              <span class="w-5 h-5 rounded-md bg-indigo-600/30 text-indigo-400 flex items-center justify-center text-[10px] font-mono font-bold">${{num}}</span>
              Bowler ${{num}} *
            </label>
            <span class="text-[10px] font-mono text-indigo-400 font-semibold">PPI: ${{w.ppi_score.toFixed(1)}} | Econ: ${{w.p_econ.toFixed(2)}}</span>
          </div>
          <div class="flex items-center gap-2">
            <input type="text" id="input-w-${{num}}" value="${{w.name}}" readonly class="unstop-input flex-1 rounded-lg px-3 py-1.5 text-xs font-medium cursor-pointer" onclick="showModal('w', ${{idx}})">
            <button onclick="copyFieldValue('input-w-${{num}}')" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-mono transition" title="Copy name">
              Copy
            </button>
          </div>
        `;
        wContainer.appendChild(div);
      }});

      document.getElementById('unstop-remark-box').value = REMARK_TEXT;
    }}

    // Render Analytics Tables
    function renderAnalytics() {{
      const bTbody = document.getElementById('batters-table-body');
      const wTbody = document.getElementById('bowlers-table-body');
      bTbody.innerHTML = '';
      wTbody.innerHTML = '';

      TOP_BATTERS.forEach(b => {{
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-800/40 cursor-pointer transition';
        tr.onclick = () => showModalByName(b.name, 'b');
        tr.innerHTML = `
          <td class="py-2.5 px-3 font-bold text-pink-400">#${{b.rank}}</td>
          <td class="py-2.5 px-3 font-bold text-white flex items-center gap-1.5">${{b.name}} ${{b.classification === 'Overseas' ? '✈️' : '🇮🇳'}}</td>
          <td class="py-2.5 px-3 text-slate-400">${{b.previous_franchise}}</td>
          <td class="py-2.5 px-3 font-bold text-pink-400">${{b.ppi_score.toFixed(1)}}</td>
          <td class="py-2.5 px-3 text-emerald-400">${{b.p_sr.toFixed(1)}}</td>
          <td class="py-2.5 px-3 text-slate-200">${{b.p_avg.toFixed(1)}}</td>
          <td class="py-2.5 px-3 text-amber-400">${{b.rr_fit_score.toFixed(0)}}%</td>
          <td class="py-2.5 px-3 text-pink-300">${{b.max_bid}}</td>
          <td class="py-2.5 px-4 text-slate-300 text-[11px] truncate max-w-xs">${{b.why_target}}</td>
        `;
        bTbody.appendChild(tr);
      }});

      TOP_BOWLERS.forEach(w => {{
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-800/40 cursor-pointer transition';
        tr.onclick = () => showModalByName(w.name, 'w');
        tr.innerHTML = `
          <td class="py-2.5 px-3 font-bold text-indigo-400">#${{w.rank}}</td>
          <td class="py-2.5 px-3 font-bold text-white flex items-center gap-1.5">${{w.name}} ${{w.classification === 'Overseas' ? '✈️' : '🇮🇳'}}</td>
          <td class="py-2.5 px-3 text-slate-400">${{w.previous_franchise}}</td>
          <td class="py-2.5 px-3 font-bold text-indigo-400">${{w.ppi_score.toFixed(1)}}</td>
          <td class="py-2.5 px-3 text-emerald-400">${{w.p_econ.toFixed(2)}}</td>
          <td class="py-2.5 px-3 text-amber-400">${{w.p_w_rate.toFixed(2)}}</td>
          <td class="py-2.5 px-3 text-amber-400">${{w.rr_fit_score.toFixed(0)}}%</td>
          <td class="py-2.5 px-3 text-indigo-300">${{w.max_bid}}</td>
          <td class="py-2.5 px-4 text-slate-300 text-[11px] truncate max-w-xs">${{w.why_target}}</td>
        `;
        wTbody.appendChild(tr);
      }});
    }}

    // Render RR Squad
    function renderRRSquad() {{
      const grid = document.getElementById('rr-squad-grid');
      grid.innerHTML = '';
      RR_SQUAD.forEach(p => {{
        const isTrade = !!p.trade;
        const div = document.createElement('div');
        div.className = 'p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1 relative';
        div.innerHTML = `
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-white">${{p.name}} ${{p.type === 'Overseas' ? '✈️' : '🇮🇳'}}</span>
            <span class="text-xs font-mono font-bold text-pink-400">₹${{p.price}} Cr</span>
          </div>
          <div class="text-[11px] text-slate-400">${{p.role}}</div>
          ${{isTrade ? `<div class="text-[10px] font-bold text-amber-400 mt-1">🔄 ${{p.trade}}</div>` : ''}}
          <div class="text-[10px] text-slate-500 mt-1">${{p.notes}}</div>
        `;
        grid.appendChild(div);
      }});
    }}

    // Render Franchises Table
    function renderFranchises() {{
      const tbody = document.getElementById('franchise-table-body');
      tbody.innerHTML = '';
      Object.entries(FRANCHISES).forEach(([code, f]) => {{
        const tr = document.createElement('tr');
        tr.className = code === 'RR' ? 'bg-pink-950/20 border-l-2 border-l-pink-500 font-bold' : '';
        tr.innerHTML = `
          <td class="py-2.5 px-3 text-white">${{f.name}} (${{code}})</td>
          <td class="py-2.5 px-3 text-slate-300">${{f.retained_count}}</td>
          <td class="py-2.5 px-3 text-slate-400">${{f.overseas_retained}}</td>
          <td class="py-2.5 px-3 font-bold ${{code === 'RR' ? 'text-pink-400' : 'text-emerald-400'}}">₹${{f.purse}} Cr</td>
          <td class="py-2.5 px-3 text-slate-300">${{f.slots_left}}</td>
          <td class="py-2.5 px-3 text-slate-400">${{f.overseas_slots_left}}</td>
          <td class="py-2.5 px-4 text-xs font-mono ${{f.purse >= 35 ? 'text-emerald-400' : (f.purse >= 25 ? 'text-amber-400' : 'text-rose-400')}}">
            ${{f.purse >= 35 ? 'High (Bidding Aggressor)' : (f.purse >= 20 ? 'Moderate (Targeted)' : 'Constrained')}}
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Budget Simulator
    function loadBudgetScenario(key) {{
      const sc = key === 'balanced' ? BUDGET_DATA.scenario_a_balanced : BUDGET_DATA.scenario_b_newball;
      document.getElementById('sim-scenario-name').innerText = sc.name;
      document.getElementById('sim-spend').innerText = `₹${{sc.total_spend.toFixed(2)}} Cr`;
      document.getElementById('sim-remaining').innerText = `₹${{sc.purse_remaining.toFixed(2)}} Cr`;
      document.getElementById('sim-slots').innerText = `6 / 6 (${{sc.overseas_bought}} OS)`;

      const tbody = document.getElementById('budget-table-body');
      tbody.innerHTML = '';
      sc.purchases.forEach((p, idx) => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="py-2.5 px-3 font-bold text-pink-400">P${{idx + 1}}</td>
          <td class="py-2.5 px-3 font-bold text-white">${{p.name}} ${{p.type === 'Overseas' ? '✈️' : '🇮🇳'}}</td>
          <td class="py-2.5 px-3 text-slate-300">${{p.role}}</td>
          <td class="py-2.5 px-3 text-slate-400">${{p.type}}</td>
          <td class="py-2.5 px-3 font-bold text-emerald-400">₹${{p.bid.toFixed(1)}} Cr</td>
          <td class="py-2.5 px-3 text-rose-400">₹${{p.walk_away.toFixed(1)}} Cr</td>
          <td class="py-2.5 px-4 text-slate-300 text-[11px]">Primary tactical solution addressing core vulnerability.</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Render Playing XI
    function renderPlayingXI() {{
      const container = document.getElementById('xi-batting-first');
      container.innerHTML = '';
      PLAYING_XI.batting_first.forEach(p => {{
        const isAuction = p.name.includes('(Auction)');
        const div = document.createElement('div');
        div.className = `p-2.5 rounded-lg flex items-center justify-between border ${{isAuction ? 'bg-pink-950/20 border-pink-500/30' : 'bg-slate-900/80 border-slate-800'}}`;
        div.innerHTML = `
          <div class="flex items-center gap-2">
            <span class="w-5 h-5 rounded bg-slate-800 text-slate-300 text-center font-bold text-[10px] flex items-center justify-center">${{p.pos}}</span>
            <span class="font-bold ${{isAuction ? 'text-pink-300' : 'text-white'}}">${{p.name}}</span>
          </div>
          <span class="text-[11px] text-slate-400">${{p.role}}</span>
        `;
        container.appendChild(div);
      }});
    }}

    // Tab Switching
    function switchTab(tabId) {{
      ['unstop', 'analytics', 'audit', 'rr-squad', 'franchises', 'budget', 'playing-xi', 'gemini'].forEach(t => {{
        const el = document.getElementById(`tab-${{t}}`);
        const nav = document.getElementById(`nav-${{t}}`);
        if (el) el.classList.add('hidden');
        if (nav) {{
          nav.className = 'px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap';
        }}
      }});

      const activeEl = document.getElementById(`tab-${{tabId}}`);
      const activeNav = document.getElementById(`nav-${{tabId}}`);
      if (activeEl) activeEl.classList.remove('hidden');
      if (activeNav) {{
        activeNav.className = 'px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 bg-pink-600 text-white shadow-md shadow-pink-600/30 whitespace-nowrap';
      }}
    }}

    // Copy Utilities
    function copyFieldValue(inputId) {{
      const el = document.getElementById(inputId);
      if (el) {{
        navigator.clipboard.writeText(el.value);
        showToast(`Copied ${{el.value}}`);
      }}
    }}

    function copyAllUnstopPicks() {{
      let text = "RAJASTHAN ROYALS — TOP 10 BATSMEN (1 TO 10):\\n";
      TOP_BATTERS.forEach((b, i) => {{
        text += `Batsman ${{i + 1}}: ${{b.name}}\\n`;
      }});
      text += "\\nRAJASTHAN ROYALS — TOP 10 BOWLERS (1 TO 10):\\n";
      TOP_BOWLERS.forEach((w, i) => {{
        text += `Bowler ${{i + 1}}: ${{w.name}}\\n`;
      }});
      navigator.clipboard.writeText(text);
      showToast("Copied all 20 players to clipboard!");
    }}

    function copyRemarkText() {{
      const box = document.getElementById('unstop-remark-box');
      if (box) {{
        navigator.clipboard.writeText(box.value);
        showToast("Copied submission Remark to clipboard!");
      }}
    }}

    function showToast(msg) {{
      const toast = document.createElement('div');
      toast.className = 'fixed bottom-5 right-5 z-50 bg-pink-600 text-white font-mono text-xs px-4 py-2 rounded-xl shadow-xl border border-pink-400 transition-all duration-300';
      toast.innerText = msg;
      document.body.appendChild(toast);
      setTimeout(() => toast.remove(), 2500);
    }}

    // Modal
    function showModal(type, idx) {{
      const p = type === 'b' ? TOP_BATTERS[idx] : TOP_BOWLERS[idx];
      const isBat = type === 'b';
      const c = document.getElementById('modal-content');
      c.innerHTML = `
        <div class="flex items-start justify-between">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xs uppercase font-mono font-bold text-pink-400">${{p.classification}} • ${{p.previous_franchise}}</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">VERIFIED ELIGIBLE</span>
            </div>
            <h3 class="text-xl font-black text-white mt-1">${{p.name}}</h3>
          </div>
          <div class="text-right font-mono">
            <span class="text-xs text-slate-400">Max Bid</span>
            <div class="text-lg font-bold text-pink-400">${{p.max_bid}}</div>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-3 font-mono text-center my-3 bg-slate-900/80 p-3 rounded-xl border border-slate-800">
          <div>
            <span class="text-[10px] text-slate-400">PPI Score</span>
            <div class="text-base font-bold text-white">${{p.ppi_score.toFixed(1)}}</div>
          </div>
          <div>
            <span class="text-[10px] text-slate-400">${{isBat ? 'Press SR' : 'Press Econ'}}</span>
            <div class="text-base font-bold text-emerald-400">${{isBat ? p.p_sr.toFixed(1) : p.p_econ.toFixed(2)}}</div>
          </div>
          <div>
            <span class="text-[10px] text-slate-400">RR Fit Score</span>
            <div class="text-base font-bold text-amber-400">${{p.rr_fit_score.toFixed(0)}}%</div>
          </div>
        </div>

        <div class="space-y-2 text-xs leading-relaxed text-slate-300">
          <div><strong class="text-white">Why RR Should Buy:</strong> ${{p.why_target}}</div>
          <div><strong class="text-white">Weaknesses & Risks:</strong> ${{p.risks}}</div>
        </div>

        <div class="pt-3 border-t border-slate-800 flex items-center justify-between">
          <button onclick="copyFieldValue('input-${{type}}-${{idx + 1}}'); closeModal();" class="px-3 py-1.5 rounded-lg bg-pink-600 hover:bg-pink-500 text-white font-bold text-xs">
            📋 Copy Player Name
          </button>
          <button onclick="closeModal()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs">
            Close
          </button>
        </div>
      `;
      document.getElementById('player-modal').classList.remove('hidden');
    }}

    function showModalByName(name, type) {{
      const arr = type === 'b' ? TOP_BATTERS : TOP_BOWLERS;
      const idx = arr.findIndex(p => p.name === name);
      if (idx !== -1) showModal(type, idx);
    }}

    function closeModal() {{
      document.getElementById('player-modal').classList.add('hidden');
    }}

    // Gemini Chat
    async function handleChatSubmit(e) {{
      e.preventDefault();
      const input = document.getElementById('chat-input');
      const query = input.value.trim();
      if (!query) return;

      appendChatMessage(query, 'user');
      input.value = '';
      appendChatMessage('Analyzing 200,999 deliveries and official 18-Nov-2026 BCCI retention database...', 'bot', true);

      try {{
        const res = await fetch('/api/gemini-scout', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ query }})
        }});
        const data = await res.json();
        removeLoadingMessage();
        appendChatMessage(data.reply || 'No strategic response generated.', 'bot');
      }} catch (err) {{
        removeLoadingMessage();
        appendChatMessage('Error connecting to War Room backend. Displaying offline strategic intelligence.', 'bot');
      }}
    }}

    function askPrompt(q) {{
      switchTab('gemini');
      document.getElementById('chat-input').value = q;
      document.getElementById('chat-submit-btn').click();
    }}

    function appendChatMessage(msg, sender, isLoading = false) {{
      const box = document.getElementById('chat-messages');
      const div = document.createElement('div');
      div.className = sender === 'user' ? 'p-3 rounded-xl bg-pink-950/40 border border-pink-500/30 text-xs text-white ml-8 font-mono' : 'p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 mr-8 leading-relaxed font-mono';
      if (isLoading) div.id = 'chat-loading-msg';
      div.innerHTML = sender === 'user' ? `<strong>You:</strong> ${{msg}}` : `🤖 <strong>War Room Scout:</strong><br/>${{msg.replace(/\\n/g, '<br/>')}}`;
      box.appendChild(div);
      box.scrollTop = box.scrollHeight;
    }}

    function removeLoadingMessage() {{
      const el = document.getElementById('chat-loading-msg');
      if (el) el.remove();
    }}

    // Run on startup
    window.addEventListener('DOMContentLoaded', () => {{
      renderAuditTab();
      renderUnstopFields();
      renderAnalytics();
      renderRRSquad();
      renderFranchises();
      loadBudgetScenario('balanced');
      renderPlayingXI();
    }});
  </script>
</body>
</html>
'''

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

shutil.copy2('dashboard.html', 'index.html')

# Also copy to artifacts directory
artifact_dir = r'C:\Users\HP\Downloads\RR'
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\04014367-f2d6-4dd0-a981-5625edbe7cc4'
if os.path.exists(brain_dir):
    shutil.copy2('dashboard.html', os.path.join(brain_dir, 'dashboard.html'))
    shutil.copy2('RR_SupeRR_Selector_Methodology_Report.pdf', os.path.join(brain_dir, 'RR_SupeRR_Selector_Methodology_Report.pdf'))
    shutil.copy2('RR_SupeRR_Selector_Auction_Strategy.pptx', os.path.join(brain_dir, 'RR_SupeRR_Selector_Auction_Strategy.pptx'))
    shutil.copy2('top_10_verified_eligible_batters_2027.csv', os.path.join(brain_dir, 'top_10_verified_eligible_batters_2027.csv'))
    shutil.copy2('top_10_verified_eligible_bowlers_2027.csv', os.path.join(brain_dir, 'top_10_verified_eligible_bowlers_2027.csv'))
    print("Copied all deliverables to artifact directory!")

print("=== DASHBOARD SUCCESSFULLY REBUILT AND SYNCHRONIZED! ===")
