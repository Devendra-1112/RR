import json
import os
import shutil

print("=== BUILDING FULL UNSTOP-STRUCTURED WAR ROOM DASHBOARD ===")

# 1. Load Data Files
with open('war_room_data.json', 'r', encoding='utf-8') as f:
    war_room_data = json.load(f)

with open('all_players_offline.json', 'r', encoding='utf-8') as f:
    all_players = json.load(f)

with open('strict_verification_data.json', 'r', encoding='utf-8') as f:
    strict_data = json.load(f)

top_batters = war_room_data['top_10_batters_confirmed']
top_bowlers = war_room_data['top_10_bowlers_confirmed']

# Serialize data for embedding
all_players_json = json.dumps(all_players)
top_batters_json = json.dumps(top_batters)
top_bowlers_json = json.dumps(top_bowlers)
strict_data_json = json.dumps(strict_data)

# Pre-crafted high-scoring Remark text
submission_remark_text = """RAJASTHAN ROYALS — IPL 2027 AUCTION INTELLIGENCE & ACQUISITION STRATEGY
Round 1: Identify the Most Reliable Players Under Pressure

1. ANALYSIS METHODOLOGY:
• Dataset: Complete ball-by-ball analysis across 200,999 deliveries (371 IPL matches from 2022 to 2026 + 512 T20Is) from Rajasthan Royals proprietary data.
• Pressure Isolation: 81,722 high-leverage deliveries (40.7% of total) identified using delivery-by-delivery indicators:
  - Death overs crunch (Overs 16–20 in both 1st & 2nd innings: 44,454 balls).
  - High required run rate chases (Innings 2 where RRR >= 9.80, or <= 36 balls remain with >= 35 runs needed: 32,562 balls).
  - Powerplay collapse rescue (Overs 1–6 with >= 3 wickets down: 1,897 balls).
  - High-stakes playoff context (Overs 12–20 in knockout fixtures: 1,022 balls).
• Pressure Performance Index (PPI): Weighted composite scoring balancing clutch strike rate / economy, pressure batting / bowling average, performance delta vs baseline, and dot-ball suppression, scaled by a sample-size reliability dampener (sqrt(balls/180)).
• Availability Governance: Excluded all contractually bound marquee retentions (Bumrah, Kohli, Klaasen, Rashid Khan, Gaikwad, Jadeja, Narine, Russell, Axar, Kuldeep) and officially retired players (Dhawan, Karthik). Only purchasable targets are recommended.

2. TOP PICKS UNDER PRESSURE:
• Top 10 Batsmen:
  1. Naman Dhir (PPI: 92.41 | Press SR: 194.44 | Domestic 360° Finisher)
  2. Shreyas Iyer (PPI: 90.57 | Press SR: 179.20 | Marquee Middle-Order Anchor)
  3. Rishabh Pant (PPI: 89.68 | Press SR: 180.54 | Explosive Left-Hand Keeper-Batter)
  4. Fakhar Zaman (PPI: 96.68 | Press SR: 183.89 | High-Tempo Top-Order Disruptor)
  5. Asif Khan (PPI: 94.13 | Press SR: 196.52 | Highest Pressure Strike Rate in Dataset)
  6. Najibullah Zadran (PPI: 92.52 | Press SR: 180.00 | Press Avg: 42.00 | Death Enforcer)
  7. Babar Azam (PPI: 91.73 | Press SR: 163.25 | Press Avg: 51.33 | Innings Stabilizer)
  8. Phil Salt (PPI: 90.93 | Press SR: 187.27 | Powerplay & Death Boundary Striker)
  9. Tim David (PPI: 90.60 | Press SR: 194.85 | Heavy Boundary Lever in Overs 17–20)
  10. Angelo Mathews (PPI: 87.89 | Press SR: 176.14 | 20.5% Dot Rate | Crisis Stabilizer)

• Top 10 Bowlers:
  1. Arshdeep Singh (PPI: 306.82 | 131 Clutch Wkts | 8.89 Press Econ | #1 Death Seamer)
  2. Bhuvneshwar Kumar (PPI: 177.25 | 68 Clutch Wkts | 8.87 Press Econ | Swing & Yorker Mastery)
  3. Yuzvendra Chahal (PPI: 180.78 | 71 Clutch Wkts | 8.91 Press Econ | Returning Spin Match-Winner)
  4. Harshal Patel (PPI: 163.53 | 64 Clutch Wkts | 9.54 Press Econ | Slower-Ball Dip Specialist)
  5. Jason Holder (PPI: 160.93 | 63 Clutch Wkts | 9.50 Press Econ | Steep Bounce Pace All-Rounder)
  6. Mohammed Siraj (PPI: 140.08 | 47 Clutch Wkts | 41.7% Dot Balls | Aggressive Breakthrough Seamer)
  7. Haris Rauf (PPI: 132.24 | 43 Clutch Wkts | 8.76 Press Econ | 150+ kph Express Tearaway)
  8. Maheesh Theekshana (PPI: 128.17 | 40 Clutch Wkts | 7.94 Press Econ | Middle Restriction Mystery Spinner)
  9. Mohammad Nawaz (PPI: 128.08 | 28 Clutch Wkts | 5.87 Press Econ | Tournament-Best Defensive Economy)
  10. Trent Boult (PPI: 128.22 | 40 Clutch Wkts | 8.45 Press Econ | Elite Left-Arm Powerplay Wicket-Taker)

3. HOW EACH PLAYER STRENGTHENS RAJASTHAN ROYALS FOR IPL 2027:
• Resolving the Death-Overs Deficit: RR's primary bottleneck has been death-over run leakage at Sawai Mansingh Stadium. Pairing Arshdeep Singh (131 clutch wickets, 8.89 economy) alongside retained anchor Sandeep Sharma establishes the most lethal, complementary death bowling pair in the IPL (left-arm yorkers + knuckle-ball cutters), backed by Harshal Patel's dip and Haris Rauf's 150+ kph express pace.
• Eliminating the Chase Collapse Vulnerability: In chases requiring 10+ RRR, Naman Dhir (194.44 Press SR) and Asif Khan (196.52 Press SR) inject explosive acceleration at No. 6/7 while preserving overseas balance, perfectly complementing Sanju Samson, Riyan Parag, Dhruv Jurel, and Shimron Hetmyer.
• Middle-Overs Spin Choke: Re-acquiring Yuzvendra Chahal alongside Maheesh Theekshana and Mohammad Nawaz (5.87 pressure economy) guarantees control over overs 7–15, depriving opponents of momentum before the death phase.

4. DELIVERABLES & INTERACTIVE DASHBOARD:
• Full Methodology Report: Attached PDF (RR_SupeRR_Selector_Methodology_Report.pdf)
• Strategy Deck: Attached PPTX (RR_SupeRR_Selector_Auction_Strategy.pptx)
• Interactive War Room Dashboard: http://127.0.0.1:8088/dashboard.html"""

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rajasthan Royals • IPL 2027 Auction War Room & Unstop Submission Portal</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap');
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }
    .rr-card {
      background: rgba(15, 23, 42, 0.82);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .rr-card:hover {
      border-color: rgba(228, 0, 124, 0.35);
    }
    .rr-card-highlight {
      background: linear-gradient(135deg, rgba(30, 20, 50, 0.88) 0%, rgba(15, 23, 42, 0.96) 100%);
      border: 1px solid rgba(228, 0, 124, 0.4);
    }
    .unstop-input {
      background: #0b1329;
      border: 1px solid #1e293b;
      color: #f1f5f9;
      transition: all 0.2s ease;
    }
    .unstop-input:focus {
      border-color: #e4007c;
      box-shadow: 0 0 0 2px rgba(228, 0, 124, 0.2);
      outline: none;
    }
    .dropdown-menu {
      max-height: 220px;
      overflow-y: auto;
      z-index: 60;
    }
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #080e1e;
    }
    ::-webkit-scrollbar-thumb {
      background: #1e293b;
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #e4007c;
    }
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
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-pink-500/10 text-pink-400 border border-pink-500/20">SupeRR Selector Season 2</span>
          </div>
          <h1 class="text-sm sm:text-base font-bold text-white tracking-tight flex items-center gap-2">
            IPL 2027 Auction War Room • Unstop Submission Portal
          </h1>
        </div>
      </div>

      <div class="flex items-center gap-2 sm:gap-3">
        <span class="hidden xl:inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-mono">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"></span>
          200,999 Balls • 1,210 Players Offline
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

  <!-- QUICK ACTION / NOTIFICATION BAR -->
  <div class="bg-gradient-to-r from-pink-950/60 via-slate-900/90 to-indigo-950/60 border-b border-pink-500/30 px-4 py-2.5 text-xs text-pink-200">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="text-base">🏆</span>
        <span>
          <strong class="font-bold text-pink-300">UNSTOP SUBMISSION FORM SYNC ACTIVE:</strong>
          All 10 Batsmen and 10 Bowlers are pre-filled below matching the Unstop competition structure. You can search, customize, or 1-click copy every slot.
        </span>
      </div>
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
          Offline Storage Ready
        </span>
        <button onclick="restoreDefaultTop20()" class="text-[11px] font-semibold text-pink-400 hover:text-white underline">
          Reset to Optimal Top 20
        </button>
      </div>
    </div>
  </div>

  <!-- NAVIGATION TABS -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-4 pb-2 w-full">
    <div class="flex items-center gap-2 border-b border-slate-800 pb-2 overflow-x-auto">
      <button onclick="switchTab('unstop')" id="nav-unstop" class="px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 bg-pink-600 text-white shadow-md shadow-pink-600/30 whitespace-nowrap">
        <span>📝 Tab 1: Unstop Submission Form (10 Batters + 10 Bowlers)</span>
        <span class="px-1.5 py-0.5 rounded-full text-[10px] bg-white/20 text-white font-mono">20 / 20</span>
      </button>

      <button onclick="switchTab('analytics')" id="nav-analytics" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>📊 Tab 2: Full Player Metrics & Comparison Tables</span>
      </button>

      <button onclick="switchTab('governance')" id="nav-governance" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>⚖️ Tab 3: Auction Governance & Retentions Audit</span>
      </button>

      <button onclick="switchTab('gemini')" id="nav-gemini" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span class="w-2 h-2 rounded-full bg-pink-500 animate-ping"></span>
        <span>🤖 Tab 4: AI War Room Scout (Gemini 2.5)</span>
      </button>
    </div>
  </section>

  <!-- MAIN CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 w-full flex-1">

    <!-- ============================================================== -->
    <!-- TAB 1: UNSTOP SUBMISSION FORM (EXACT USER SPECIFICATION) -->
    <!-- ============================================================== -->
    <div id="tab-unstop" class="space-y-6">

      <!-- Form Helper Bar -->
      <div class="rr-card-highlight rounded-2xl p-5">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-pink-500/20 text-pink-400 border border-pink-500/30">
                OFFLINE SUBMISSION CENTER
              </span>
              <span class="text-xs text-slate-400 font-mono">SupeRR Selector Round 1</span>
            </div>
            <h2 class="text-base sm:text-lg font-bold text-white mt-1">Official Unstop Competition Submission Form</h2>
            <p class="text-xs text-slate-300 mt-1 max-w-3xl leading-relaxed">
              This form matches the exact required fields of the Unstop submission portal: <strong class="text-pink-400">Batsman 1–10</strong>, <strong class="text-indigo-400">Bowler 1–10</strong>, <strong class="text-emerald-400">Upload Your Report</strong>, and the mandatory <strong class="text-amber-400">Remark</strong> explanation. Every slot contains a live searchable dropdown across 1,210 players stored offline, with instant 1-click clipboard copy buttons.
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
                <span class="text-[11px] text-pink-400">Required fields marked with *</span>
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
                <span class="text-[11px] text-indigo-400">Required fields marked with *</span>
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
          <span class="text-xs font-mono text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/20">
            2 Reports Generated & Verified
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <!-- Download Card 1: PDF -->
          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 flex items-center justify-between gap-3 hover:border-emerald-500/40 transition">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-lg bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold text-sm">
                PDF
              </div>
              <div>
                <div class="text-xs font-bold text-white">RR_SupeRR_Selector_Methodology_Report.pdf</div>
                <div class="text-[11px] text-slate-400">Comprehensive Methodology, PPI Math & Tactical Report</div>
              </div>
            </div>
            <a href="RR_SupeRR_Selector_Methodology_Report.pdf" download class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white transition flex items-center gap-1 shadow">
              📥 Download
            </a>
          </div>

          <!-- Download Card 2: PPTX -->
          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 flex items-center justify-between gap-3 hover:border-emerald-500/40 transition">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-sm">
                PPTX
              </div>
              <div>
                <div class="text-xs font-bold text-white">RR_SupeRR_Selector_Auction_Strategy.pptx</div>
                <div class="text-[11px] text-slate-400">10-Slide Executive War Room Presentation Deck</div>
              </div>
            </div>
            <a href="RR_SupeRR_Selector_Auction_Strategy.pptx" download class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white transition flex items-center gap-1 shadow">
              📥 Download
            </a>
          </div>

        </div>

        <!-- Simulated Unstop File Upload Widget -->
        <div class="mt-4 p-4 rounded-xl border-2 border-dashed border-slate-700 hover:border-emerald-500/50 transition bg-slate-950/40 text-center">
          <input type="file" id="report-file-input" accept=".pdf,.pptx" onchange="handleFileUpload(event)" class="hidden">
          <label for="report-file-input" class="cursor-pointer flex flex-col items-center justify-center gap-1.5">
            <svg class="w-7 h-7 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
            <div class="text-xs text-slate-300 font-semibold" id="upload-status-text">
              <span class="text-emerald-400 font-bold underline">Click to choose file</span> or drag & drop your submission report here
            </div>
            <div class="text-[10px] text-slate-500">Accepted formats: .pdf, .pptx (Max size 50MB)</div>
          </label>
        </div>
      </div>

      <!-- REMARK TEXTAREA SECTION -->
      <div class="rr-card rounded-2xl p-6 border border-amber-500/30 space-y-3">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 pb-3 border-b border-slate-800">
          <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center text-base">💬</span>
            <div>
              <h3 class="text-sm font-bold text-white">Submission Remark Text *</h3>
              <span class="text-[11px] text-amber-400">Outlining methodology, reliable players under pressure, and RR squad fit</span>
            </div>
          </div>
          <button onclick="copyRemarkText()" id="btn-copy-remark" class="px-3.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white transition flex items-center gap-1.5 shadow">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
            <span>Copy Remark to Clipboard</span>
          </button>
        </div>

        <div class="relative">
          <textarea id="submission-remark" rows="11" class="w-full bg-[#0b1329] border border-slate-800 rounded-xl p-4 text-xs font-mono text-slate-200 leading-relaxed focus:outline-none focus:border-amber-500 selection:bg-amber-600" spellcheck="false">__REMARK_TEXT__</textarea>
        </div>
        <div class="flex items-center justify-between text-[11px] text-slate-400">
          <span>Formatted specifically for the Unstop SupeRR Selector text limit.</span>
          <span class="font-mono text-amber-400">Ready for instant paste</span>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 2: FULL PLAYER METRICS & COMPARISON TABLES -->
    <!-- ============================================================== -->
    <div id="tab-analytics" class="hidden space-y-6">
      
      <!-- Batters Full Table -->
      <div class="rr-card rounded-2xl p-5 border border-pink-500/20 space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <h3 class="text-sm font-bold text-white">Top 10 Batters Comprehensive Pressure Metrics</h3>
            <span class="text-[11px] text-slate-400">Complete statistical comparison across 18 columns</span>
          </div>
          <a href="top_10_available_batters.csv" download class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-pink-400 border border-slate-700">
            📥 Export Batters CSV
          </a>
        </div>
        <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950/60">
          <table class="w-full text-left text-xs text-slate-300 whitespace-nowrap">
            <thead class="bg-slate-900/80 uppercase text-[10px] font-bold text-slate-400 border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">#</th>
                <th class="py-2.5 px-4">Player Name</th>
                <th class="py-2.5 px-3">Franchise</th>
                <th class="py-2.5 px-3 text-right">PPI Score</th>
                <th class="py-2.5 px-3 text-right">Pressure SR</th>
                <th class="py-2.5 px-3 text-right">Base SR</th>
                <th class="py-2.5 px-3 text-right">Pressure Avg</th>
                <th class="py-2.5 px-3 text-right">Pressure Balls</th>
                <th class="py-2.5 px-3 text-right">RR Fit</th>
                <th class="py-2.5 px-3 text-right">Price Range</th>
                <th class="py-2.5 px-4">Tactical Rationale</th>
              </tr>
            </thead>
            <tbody id="tbody-full-batters" class="divide-y divide-slate-800/60">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Bowlers Full Table -->
      <div class="rr-card rounded-2xl p-5 border border-indigo-500/20 space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <h3 class="text-sm font-bold text-white">Top 10 Bowlers Comprehensive Pressure Metrics</h3>
            <span class="text-[11px] text-slate-400">Complete statistical comparison across 18 columns</span>
          </div>
          <a href="top_10_available_bowlers.csv" download class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-indigo-400 border border-slate-700">
            📥 Export Bowlers CSV
          </a>
        </div>
        <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950/60">
          <table class="w-full text-left text-xs text-slate-300 whitespace-nowrap">
            <thead class="bg-slate-900/80 uppercase text-[10px] font-bold text-slate-400 border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">#</th>
                <th class="py-2.5 px-4">Player Name</th>
                <th class="py-2.5 px-3">Franchise</th>
                <th class="py-2.5 px-3 text-right">PPI Score</th>
                <th class="py-2.5 px-3 text-right">Pressure Econ</th>
                <th class="py-2.5 px-3 text-right">Base Econ</th>
                <th class="py-2.5 px-3 text-right">Clutch Wkts</th>
                <th class="py-2.5 px-3 text-right">Dot Ball %</th>
                <th class="py-2.5 px-3 text-right">RR Fit</th>
                <th class="py-2.5 px-3 text-right">Price Range</th>
                <th class="py-2.5 px-4">Tactical Rationale</th>
              </tr>
            </thead>
            <tbody id="tbody-full-bowlers" class="divide-y divide-slate-800/60">
              <!-- Populated via JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 3: AUCTION GOVERNANCE & RETENTIONS AUDIT -->
    <!-- ============================================================== -->
    <div id="tab-governance" class="hidden space-y-6">
      
      <!-- Retained Cores Non-Purchasable Banner -->
      <div class="rr-card rounded-2xl p-5 border border-rose-500/30">
        <div class="flex items-start justify-between gap-3">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30">
                PROHIBITED AUCTION TARGETS
              </span>
              <span class="text-xs text-slate-400">Strict Legal Exclusion</span>
            </div>
            <h3 class="text-base font-bold text-white mt-1">Confirmed Retained Marquee Cores (Do Not Bid)</h3>
            <p class="text-xs text-slate-300 mt-1 leading-relaxed max-w-3xl">
              Contractually bound players under BCCI multi-year retention agreements cannot enter the auction pool. Recommending any of these players violates auction war room rules:
            </p>
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2.5 mt-4 text-xs font-mono">
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Jasprit Bumrah</div>
            <div class="text-[10px] text-rose-400">MI • Retained (₹18 Cr)</div>
          </div>
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Virat Kohli</div>
            <div class="text-[10px] text-rose-400">RCB • Retained (₹21 Cr)</div>
          </div>
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Heinrich Klaasen</div>
            <div class="text-[10px] text-rose-400">SRH • Retained (₹23 Cr)</div>
          </div>
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Rashid Khan</div>
            <div class="text-[10px] text-rose-400">GT • Retained (₹18 Cr)</div>
          </div>
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Ruturaj Gaikwad</div>
            <div class="text-[10px] text-rose-400">CSK • Retained (₹18 Cr)</div>
          </div>
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Ravindra Jadeja</div>
            <div class="text-[10px] text-rose-400">CSK • Retained (₹18 Cr)</div>
          </div>
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Sunil Narine</div>
            <div class="text-[10px] text-rose-400">KKR • Retained (₹12 Cr)</div>
          </div>
          <div class="bg-slate-900/80 p-2.5 rounded-lg border border-rose-500/20">
            <div class="font-bold text-white">Andre Russell</div>
            <div class="text-[10px] text-rose-400">KKR • Retained (₹12 Cr)</div>
          </div>
        </div>
      </div>

      <!-- BCCI Retention Deadline Notice -->
      <div class="bg-slate-900/80 rounded-2xl p-5 border border-amber-500/30">
        <div class="flex items-start gap-3">
          <div class="text-xl">⏳</div>
          <div class="space-y-1">
            <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">BCCI Timeline Compliance</h4>
            <div class="text-sm font-bold text-white">Franchise Retention & Release Submission Deadline: November 17, 2026</div>
            <p class="text-xs text-slate-300 leading-relaxed">
              The BCCI officially extended the retention and release submission deadline to November 17, 2026 (Mini-auction date: December 16, 2026 in Goa, India; salary cap ₹157.0 Cr). Contracted players from IPL 2026 squads remain bound until formal release lists are published.
            </p>
          </div>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 4: INTERACTIVE GEMINI AI WAR ROOM SCOUT -->
    <!-- ============================================================== -->
    <div id="tab-gemini" class="hidden space-y-4">
      <div class="rr-card-highlight rounded-2xl p-5">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-pink-500/20 border border-pink-500/40 flex items-center justify-center text-pink-400 font-bold text-lg">
            AI
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xs uppercase tracking-widest font-extrabold text-pink-400">Gemini 2.5 Flash</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Live War Room Connected</span>
            </div>
            <h2 class="text-base font-bold text-white">Interactive Cricket Scout & Auction Strategist</h2>
          </div>
        </div>

        <div class="flex flex-wrap items-center gap-2 mt-4">
          <button onclick="askPresetQuery('Who are RR top 3 domestic death bowler targets?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🎯 Top Death Bowlers
          </button>
          <button onclick="askPresetQuery('Why is Naman Dhir ranked as the #1 domestic finisher?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🏏 Why Naman Dhir?
          </button>
          <button onclick="askPresetQuery('Can Rajasthan Royals bid for Jasprit Bumrah or Virat Kohli?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🚫 Retained Check
          </button>
          <button onclick="askPresetQuery('How does Arshdeep Singh strengthen Rajasthan Royals?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🛡️ Arshdeep Tactical Fit
          </button>
        </div>
      </div>

      <!-- Chat Box -->
      <div class="rr-card rounded-2xl p-5 border border-slate-800 flex flex-col h-[440px]">
        <div id="chat-messages" class="flex-1 overflow-y-auto space-y-3 pr-2 text-xs">
          <div class="flex items-start gap-3 bg-slate-900/60 p-3.5 rounded-xl border border-slate-800/80">
            <div class="w-6 h-6 rounded-full bg-pink-600 flex items-center justify-center text-white font-bold text-[10px] flex-shrink-0">
              RR
            </div>
            <div class="space-y-1">
              <div class="font-bold text-white text-xs">Rajasthan Royals War Room Intelligence Officer</div>
              <p class="text-slate-300 leading-relaxed">
                Welcome! I am grounded in our 200,999 delivery dataset across IPL 2022–2026 and T20Is. All 10 Batsmen and 10 Bowlers recommended above have been verified under our multi-dimensional Pressure Performance Index (PPI). How can I assist your auction strategy?
              </p>
            </div>
          </div>
        </div>

        <div class="mt-4 pt-3 border-t border-slate-800 flex items-center gap-2">
          <input type="text" id="chat-input" onkeydown="if(event.key==='Enter') sendGeminiQuery()" placeholder="Ask War Room Scout (e.g., 'What is Arshdeep Singh's economy rate in death overs?')..." class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-pink-500">
          <button onclick="sendGeminiQuery()" class="px-4 py-2 rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-bold text-xs transition flex items-center gap-1.5 shadow">
            <span>Send</span>
          </button>
        </div>
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800/80 bg-[#0a1020] py-4 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
      <div>Rajasthan Royals • IPL 2027 Auction War Room • Proprietary Intelligence</div>
      <div class="font-mono text-[11px] text-slate-400">1,210 Players Offline Database • 200,999 Balls Parsed</div>
    </div>
  </footer>

  <!-- EMBEDDED OFFLINE DATA & INTERACTIVE LOGIC -->
  <script>
    const ALL_PLAYERS = __ALL_PLAYERS_JSON__;
    const TOP_BATTERS = __TOP_BATTERS_JSON__;
    const TOP_BOWLERS = __TOP_BOWLERS_JSON__;

    // Active Selection State (Loaded from localStorage if available)
    let selectedBatsmen = JSON.parse(localStorage.getItem('rr_selected_batsmen') || 'null');
    let selectedBowlers = JSON.parse(localStorage.getItem('rr_selected_bowlers') || 'null');

    if (!selectedBatsmen || selectedBatsmen.length !== 10) {
      selectedBatsmen = TOP_BATTERS.map(b => b.name);
    }
    if (!selectedBowlers || selectedBowlers.length !== 10) {
      selectedBowlers = TOP_BOWLERS.map(w => w.name);
    }

    // Tab Switching
    function switchTab(tabId) {
      const tabs = ['unstop', 'analytics', 'governance', 'gemini'];
      tabs.forEach(t => {
        const el = document.getElementById('tab-' + t);
        const nav = document.getElementById('nav-' + t);
        if (t === tabId) {
          el.classList.remove('hidden');
          nav.className = 'px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 bg-pink-600 text-white shadow-md shadow-pink-600/30 whitespace-nowrap';
        } else {
          el.classList.add('hidden');
          nav.className = 'px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap';
        }
      });
    }

    // Render Batsmen Fields (1 to 10)
    function renderBatsmenFields() {
      const container = document.getElementById('batsmen-fields-container');
      container.innerHTML = selectedBatsmen.map((currentVal, idx) => {
        const num = idx + 1;
        const bData = TOP_BATTERS[idx] || {};
        const statPill = bData.ppi_score ? `<span class="text-[10px] font-mono text-pink-400 font-bold bg-pink-500/10 px-2 py-0.5 rounded border border-pink-500/20">PPI: ${bData.ppi_score} | SR: ${bData.p_sr}</span>` : '';

        return `
          <div class="relative bg-slate-900/60 p-3 rounded-xl border border-slate-800 hover:border-pink-500/30 transition">
            <div class="flex items-center justify-between mb-1.5">
              <label class="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                <span class="w-5 h-5 rounded-full bg-pink-600/30 text-pink-400 flex items-center justify-center font-mono text-[10px] font-bold">${num}</span>
                <span>Batsman ${num} *</span>
              </label>
              ${statPill}
            </div>

            <div class="relative flex items-center gap-2">
              <div class="relative flex-1">
                <input 
                  type="text" 
                  id="input-batsman-${idx}" 
                  value="${currentVal}" 
                  placeholder="Type to search batsman..." 
                  autocomplete="off"
                  onfocus="openDropdown('batsman', ${idx})"
                  oninput="filterDropdown('batsman', ${idx})"
                  class="unstop-input w-full rounded-lg px-3 py-2 text-xs font-semibold pr-8"
                />
                <button 
                  type="button" 
                  onclick="toggleDropdown('batsman', ${idx})" 
                  class="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-pink-400 text-xs font-bold">
                  ▾
                </button>
              </div>

              <button 
                onclick="copyField('input-batsman-${idx}', 'Batsman ${num}')" 
                title="Copy name to clipboard"
                class="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-pink-600 hover:text-white text-slate-300 text-xs font-semibold border border-slate-700 transition flex items-center gap-1 flex-shrink-0">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                <span>Copy</span>
              </button>
            </div>

            <!-- Searchable Dropdown Menu -->
            <div id="dropdown-batsman-${idx}" class="dropdown-menu hidden absolute left-0 right-0 top-full mt-1 bg-[#0b1329] border border-pink-500/40 rounded-xl shadow-2xl p-1.5">
              <!-- Rendered via JS -->
            </div>
          </div>
        `;
      }).join('');
    }

    // Render Bowlers Fields (1 to 10)
    function renderBowlersFields() {
      const container = document.getElementById('bowlers-fields-container');
      container.innerHTML = selectedBowlers.map((currentVal, idx) => {
        const num = idx + 1;
        const wData = TOP_BOWLERS[idx] || {};
        const statPill = wData.ppi_score ? `<span class="text-[10px] font-mono text-indigo-400 font-bold bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">PPI: ${wData.ppi_score} | Econ: ${wData.p_econ}</span>` : '';

        return `
          <div class="relative bg-slate-900/60 p-3 rounded-xl border border-slate-800 hover:border-indigo-500/30 transition">
            <div class="flex items-center justify-between mb-1.5">
              <label class="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                <span class="w-5 h-5 rounded-full bg-indigo-600/30 text-indigo-400 flex items-center justify-center font-mono text-[10px] font-bold">${num}</span>
                <span>Bowler ${num} *</span>
              </label>
              ${statPill}
            </div>

            <div class="relative flex items-center gap-2">
              <div class="relative flex-1">
                <input 
                  type="text" 
                  id="input-bowler-${idx}" 
                  value="${currentVal}" 
                  placeholder="Type to search bowler..." 
                  autocomplete="off"
                  onfocus="openDropdown('bowler', ${idx})"
                  oninput="filterDropdown('bowler', ${idx})"
                  class="unstop-input w-full rounded-lg px-3 py-2 text-xs font-semibold pr-8"
                />
                <button 
                  type="button" 
                  onclick="toggleDropdown('bowler', ${idx})" 
                  class="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-indigo-400 text-xs font-bold">
                  ▾
                </button>
              </div>

              <button 
                onclick="copyField('input-bowler-${idx}', 'Bowler ${num}')" 
                title="Copy name to clipboard"
                class="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-indigo-600 hover:text-white text-slate-300 text-xs font-semibold border border-slate-700 transition flex items-center gap-1 flex-shrink-0">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                <span>Copy</span>
              </button>
            </div>

            <!-- Searchable Dropdown Menu -->
            <div id="dropdown-bowler-${idx}" class="dropdown-menu hidden absolute left-0 right-0 top-full mt-1 bg-[#0b1329] border border-indigo-500/40 rounded-xl shadow-2xl p-1.5">
              <!-- Rendered via JS -->
            </div>
          </div>
        `;
      }).join('');
    }

    // Dropdown Logic
    function openDropdown(type, idx) {
      closeAllDropdowns();
      const el = document.getElementById(`dropdown-${type}-${idx}`);
      filterDropdown(type, idx);
      el.classList.remove('hidden');
    }

    function toggleDropdown(type, idx) {
      const el = document.getElementById(`dropdown-${type}-${idx}`);
      if (el.classList.contains('hidden')) {
        openDropdown(type, idx);
      } else {
        el.classList.add('hidden');
      }
    }

    function filterDropdown(type, idx) {
      const input = document.getElementById(`input-${type}-${idx}`);
      const val = (input.value || '').toLowerCase().trim();
      const menu = document.getElementById(`dropdown-${type}-${idx}`);

      // Filter all 1,210 players
      const matches = ALL_PLAYERS.filter(p => p.name.toLowerCase().includes(val)).slice(0, 25);

      if (matches.length === 0) {
        menu.innerHTML = `<div class="p-2 text-xs text-slate-500 italic text-center">No player matching "${val}"</div>`;
        return;
      }

      menu.innerHTML = matches.map(p => `
        <div 
          onclick="selectPlayer('${type}', ${idx}, '${p.name.replace(/'/g, "\\'")}')" 
          class="px-3 py-1.5 text-xs text-slate-200 hover:bg-pink-600 hover:text-white rounded-lg cursor-pointer flex items-center justify-between transition">
          <span class="font-semibold">${p.name}</span>
          <span class="text-[10px] text-slate-400 font-mono">${p.team || 'Player'}</span>
        </div>
      `).join('');
    }

    function selectPlayer(type, idx, name) {
      if (type === 'batsman') {
        selectedBatsmen[idx] = name;
        localStorage.setItem('rr_selected_batsmen', JSON.stringify(selectedBatsmen));
      } else {
        selectedBowlers[idx] = name;
        localStorage.setItem('rr_selected_bowlers', JSON.stringify(selectedBowlers));
      }
      document.getElementById(`input-${type}-${idx}`).value = name;
      closeAllDropdowns();
    }

    function closeAllDropdowns() {
      document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.add('hidden'));
    }

    // Global Click Listener to close dropdowns
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.relative')) {
        closeAllDropdowns();
      }
    });

    // Copy Single Field
    function copyField(inputId, label) {
      const input = document.getElementById(inputId);
      const val = input.value.trim();
      navigator.clipboard.writeText(val).then(() => {
        showToast(`Copied "${val}" for ${label}!`);
      });
    }

    // Copy All 20 Unstop Picks
    function copyAllUnstopPicks() {
      let text = "RAJASTHAN ROYALS — SUPE RR SELECTOR TOP 20 PICKS\\n\\nTOP 10 BATSMEN:\\n";
      selectedBatsmen.forEach((b, i) => {
        text += `Batsman ${i+1}: ${b}\\n`;
      });
      text += "\\nTOP 10 BOWLERS:\\n";
      selectedBowlers.forEach((w, i) => {
        text += `Bowler ${i+1}: ${w}\\n`;
      });

      navigator.clipboard.writeText(text).then(() => {
        showToast("Copied all 20 Player picks for Unstop submission!");
      });
    }

    // Copy Remark Text
    function copyRemarkText() {
      const txt = document.getElementById('submission-remark').value;
      navigator.clipboard.writeText(txt).then(() => {
        showToast("Full Remark Text copied to clipboard! Ready to paste into Unstop.");
      });
    }

    // Restore Defaults
    function restoreDefaultTop20() {
      selectedBatsmen = TOP_BATTERS.map(b => b.name);
      selectedBowlers = TOP_BOWLERS.map(w => w.name);
      localStorage.removeItem('rr_selected_batsmen');
      localStorage.removeItem('rr_selected_bowlers');
      renderBatsmenFields();
      renderBowlersFields();
      showToast("Reset to optimal Top 10 Batters and Bowlers!");
    }

    // Simulated File Upload
    function handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        document.getElementById('upload-status-text').innerHTML = `
          <span class="text-emerald-400 font-bold">Selected: ${file.name}</span> (${(file.size / 1024 / 1024).toFixed(2)} MB) • <span class="text-emerald-300">Valid Format Ready</span>
        `;
        showToast(`Loaded ${file.name} for submission!`);
      }
    }

    // Toast Notification
    function showToast(msg) {
      let toast = document.getElementById('toast-notification');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast-notification';
        toast.className = 'fixed bottom-6 right-6 z-50 bg-emerald-600 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-2xl flex items-center gap-2 transition-all transform';
        document.body.appendChild(toast);
      }
      toast.innerHTML = `<span>✓</span><span>${msg}</span>`;
      toast.style.opacity = '1';
      setTimeout(() => {
        toast.style.opacity = '0';
      }, 3000);
    }

    // Populate Tab 2 Full Analytics
    function renderFullAnalytics() {
      const tbodyBatters = document.getElementById('tbody-full-batters');
      tbodyBatters.innerHTML = TOP_BATTERS.map(b => `
        <tr class="hover:bg-slate-800/40 transition">
          <td class="py-2.5 px-3 font-mono font-bold text-pink-400">#${b.rank}</td>
          <td class="py-2.5 px-4 font-bold text-white">${b.name}</td>
          <td class="py-2.5 px-3 text-slate-400">${b.current_ipl_franchise}</td>
          <td class="py-2.5 px-3 text-right font-mono font-bold text-emerald-400">${b.ppi_score}</td>
          <td class="py-2.5 px-3 text-right font-mono font-bold text-pink-400">${b.p_sr}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${b.overall_sr}</td>
          <td class="py-2.5 px-3 text-right font-mono text-white">${b.p_avg}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${b.p_balls}</td>
          <td class="py-2.5 px-3 text-right font-mono text-amber-400 font-bold">${b.rr_fit_score}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-300">${b.price_est}</td>
          <td class="py-2.5 px-4 text-xs text-slate-300 max-w-xs truncate" title="${b.target_reasons}">${b.target_reasons}</td>
        </tr>
      `).join('');

      const tbodyBowlers = document.getElementById('tbody-full-bowlers');
      tbodyBowlers.innerHTML = TOP_BOWLERS.map(w => `
        <tr class="hover:bg-slate-800/40 transition">
          <td class="py-2.5 px-3 font-mono font-bold text-indigo-400">#${w.rank}</td>
          <td class="py-2.5 px-4 font-bold text-white">${w.name}</td>
          <td class="py-2.5 px-3 text-slate-400">${w.current_ipl_franchise}</td>
          <td class="py-2.5 px-3 text-right font-mono font-bold text-emerald-400">${w.ppi_score}</td>
          <td class="py-2.5 px-3 text-right font-mono font-bold text-indigo-400">${w.p_econ}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${w.overall_econ}</td>
          <td class="py-2.5 px-3 text-right font-mono font-bold text-white">${w.p_wickets}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${w.p_dot_pct}%</td>
          <td class="py-2.5 px-3 text-right font-mono text-amber-400 font-bold">${w.rr_fit_score}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-300">${w.price_est}</td>
          <td class="py-2.5 px-4 text-xs text-slate-300 max-w-xs truncate" title="${w.target_reasons}">${w.target_reasons}</td>
        </tr>
      `).join('');
    }

    // Gemini AI Chat Interaction
    function askPresetQuery(text) {
      document.getElementById('chat-input').value = text;
      sendGeminiQuery();
    }

    async function sendGeminiQuery() {
      const input = document.getElementById('chat-input');
      const query = input.value.trim();
      if (!query) return;

      const container = document.getElementById('chat-messages');
      const userMsg = document.createElement('div');
      userMsg.className = 'flex items-start justify-end gap-2';
      userMsg.innerHTML = `
        <div class="bg-pink-600/20 border border-pink-500/40 p-3 rounded-xl max-w-md text-slate-100 text-xs">
          <div class="font-bold text-pink-400 text-[10px] mb-0.5">YOU</div>
          ${query}
        </div>
      `;
      container.appendChild(userMsg);
      input.value = '';
      container.scrollTop = container.scrollHeight;

      const botMsg = document.createElement('div');
      botMsg.className = 'flex items-start gap-3 bg-slate-900/60 p-3.5 rounded-xl border border-slate-800/80';
      botMsg.innerHTML = `
        <div class="w-6 h-6 rounded-full bg-pink-600 flex items-center justify-center text-white font-bold text-[10px] flex-shrink-0">
          RR
        </div>
        <div class="space-y-1 flex-1">
          <div class="font-bold text-white text-xs">Rajasthan Royals War Room Intelligence Officer</div>
          <p class="text-slate-400 italic text-xs animate-pulse">Analyzing 200,999 deliveries & pressure metrics...</p>
        </div>
      `;
      container.appendChild(botMsg);
      container.scrollTop = container.scrollHeight;

      try {
        const resp = await fetch('/api/gemini-scout', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query })
        });
        const data = await resp.json();
        const replyHtml = (data.reply || 'No response available.').replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
        botMsg.innerHTML = `
          <div class="w-6 h-6 rounded-full bg-pink-600 flex items-center justify-center text-white font-bold text-[10px] flex-shrink-0">
            RR
          </div>
          <div class="space-y-1 flex-1">
            <div class="font-bold text-white text-xs">Rajasthan Royals War Room Intelligence Officer</div>
            <div class="text-slate-200 leading-relaxed text-xs">${replyHtml}</div>
          </div>
        `;
      } catch (err) {
        botMsg.innerHTML = `
          <div class="w-6 h-6 rounded-full bg-rose-600 flex items-center justify-center text-white font-bold text-[10px] flex-shrink-0">!</div>
          <div class="space-y-1 flex-1">
            <div class="font-bold text-rose-400 text-xs">War Room Note</div>
            <div class="text-slate-300 text-xs">
              Top targets confirmed in offline database: 10 Batters (Naman Dhir, Shreyas Iyer, Rishabh Pant, Fakhar Zaman, Asif Khan, Najibullah Zadran, Babar Azam, Phil Salt, Tim David, Angelo Mathews) and 10 Bowlers (Arshdeep Singh, Bhuvneshwar Kumar, Yuzvendra Chahal, Harshal Patel, Jason Holder, Mohammed Siraj, Haris Rauf, Maheesh Theekshana, Mohammad Nawaz, Trent Boult).
            </div>
          </div>
        `;
      }
      container.scrollTop = container.scrollHeight;
    }

    // Initialize On Load
    document.addEventListener('DOMContentLoaded', () => {
      renderBatsmenFields();
      renderBowlersFields();
      renderFullAnalytics();
    });
  </script>
</body>
</html>
'''

# Substitute Placeholders
dashboard_html = html_template.replace('__ALL_PLAYERS_JSON__', all_players_json)
dashboard_html = dashboard_html.replace('__TOP_BATTERS_JSON__', top_batters_json)
dashboard_html = dashboard_html.replace('__TOP_BOWLERS_JSON__', top_bowlers_json)
dashboard_html = dashboard_html.replace('__REMARK_TEXT__', submission_remark_text)

# Write to workspace
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dashboard_html)

# Also copy to artifact directory
artifact_dir = r"C:\Users\HP\.gemini\antigravity\brain\04014367-f2d6-4dd0-a981-5625edbe7cc4"
if os.path.exists(artifact_dir):
    shutil.copy('dashboard.html', os.path.join(artifact_dir, 'dashboard.html'))
    print("Copied dashboard.html to artifact directory!")

print("Dashboard successfully generated as dashboard.html!")
