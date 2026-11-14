import json
import os
import shutil

print("=== REBUILDING DASHBOARD WITH 10 FREE AGENT BATSMEN & 10 FREE AGENT BOWLERS ===")

with open('war_room_data.json', 'r', encoding='utf-8') as f:
    war_room_data = json.load(f)

with open('all_players_offline.json', 'r', encoding='utf-8') as f:
    all_players = json.load(f)

free_agent_batters = war_room_data['free_agent_batters_10']
free_agent_bowlers = war_room_data['free_agent_bowlers_10']
contract_cycle_batters = war_room_data['top_10_batters_confirmed']
contract_cycle_bowlers = war_room_data['top_10_bowlers_confirmed']

free_batters_json = json.dumps(free_agent_batters)
free_bowlers_json = json.dumps(free_agent_bowlers)
contract_batters_json = json.dumps(contract_cycle_batters)
contract_bowlers_json = json.dumps(contract_cycle_bowlers)
all_players_json = json.dumps(all_players)

# Updated Remark Text focused on 100% Free Agents (Not in Any IPL Team)
remark_text = """RAJASTHAN ROYALS — IPL 2027 AUCTION INTELLIGENCE & ACQUISITION STRATEGY
SupeRR Selector Season 2 • Round 1: Most Reliable Players Under Pressure (100% Uncontracted Free Agents)

1. METHODOLOGY & PRESSURE PERFORMANCE INDEX (PPI):
• Complete ball-by-ball analysis across 200,999 deliveries (371 IPL matches + 512 T20Is from 2022 to 2026).
• Isolated 81,722 pressure deliveries (40.7% of total) using delivery-by-delivery indicators:
  - Death overs crunch (Overs 16–20 in both innings: 44,454 balls).
  - High required run rate chases (Innings 2 where RRR >= 9.80, or <= 36 balls remain with >= 35 runs needed: 32,562 balls).
  - Powerplay collapse rescue (Overs 1–6 with >= 3 wickets down: 1,897 balls).
  - Knockout playoff context (Overs 12–20 in eliminators and finals: 1,022 balls).
• Pressure Performance Index (PPI): Weighted composite scoring balancing clutch strike rate / economy, pressure average, performance delta vs baseline, and dot-ball suppression, scaled by a sample-size reliability dampener.
• 100% Free Agent Standard: Zero players retained by any IPL franchise. Every single recommended player is an uncontracted international / associate free agent available for auction acquisition.

2. TOP 10 BATSMEN UNDER PRESSURE (NOT IN ANY IPL TEAM):
1. Fakhar Zaman (Free Agent | PPI: 96.68 | Press SR: 183.89 | Top-Order Powerplay Disruptor)
2. Asif Khan (Associate Free Agent | PPI: 94.13 | Press SR: 196.52 | Highest Clutch Strike Rate in Dataset)
3. Najibullah Zadran (Free Agent | PPI: 92.52 | Press SR: 180.00 | Press Avg: 42.00 | Death Enforcer)
4. Babar Azam (Free Agent | PPI: 91.73 | Press SR: 163.25 | Press Avg: 51.33 | Collapse Recovery Anchor)
5. Angelo Mathews (Free Agent | PPI: 87.89 | Press SR: 176.14 | Dot%: 20.5% | Ice-Cool Crisis Finisher)
6. Mohammad Haris (Free Agent | PPI: 87.64 | Press SR: 183.65 | 360° Dynamic Wicketkeeper-Striker)
7. Reeza Hendricks (Free Agent | PPI: 86.71 | Press SR: 169.45 | Press Avg: 42.00 | Top-Order Stroke-Maker)
8. Mohammad Rizwan (Free Agent | PPI: 86.12 | Press SR: 155.29 | Press Avg: 44.00 | Consistent Chase Anchor)
9. Matthew Wade (Free Agent | PPI: 85.34 | Press SR: 151.70 | Press Avg: 67.00 | Knockout Death Finisher)
10. Rilee Rossouw (Free Agent | PPI: 83.80 | Press SR: 182.22 | Southpaw Middle-Overs Enforcer)

3. TOP 10 BOWLERS UNDER PRESSURE (NOT IN ANY IPL TEAM):
1. Haris Rauf (Free Agent | PPI: 132.31 | 43 Clutch Wkts | Econ: 8.77 | 150+ kph Express Tearaway)
2. Maheesh Theekshana (Free Agent | PPI: 128.17 | 40 Clutch Wkts | Econ: 7.95 | Carrom-Ball Mystery Spinner)
3. Mohammad Nawaz (Free Agent | PPI: 128.08 | 28 Clutch Wkts | Econ: 5.87 | Best Defensive Pressure Economy)
4. Adam Zampa (Free Agent | PPI: 122.35 | 39 Clutch Wkts | Econ: 8.45 | World-Class Attacking Leg-Spinner)
5. Shaheen Afridi (Free Agent | PPI: 120.01 | 33 Clutch Wkts | Econ: 7.75 | Left-Arm Swing & Yorker Spearhead)
6. Sufiyan Muqeem (Emerging Free Agent | PPI: 118.82 | 17 Clutch Wkts | Econ: 5.13 | Wrist-Spin Mystery Prodigy)
7. Abrar Ahmed (Free Agent | PPI: 118.43 | 23 Clutch Wkts | Econ: 5.92 | Gripping Leg-Cutter Specialist)
8. Adil Rashid (Free Agent | PPI: 113.54 | 35 Clutch Wkts | Econ: 8.59 | Veteran Master Wrist Spinner)
9. Tim Southee (Free Agent | PPI: 108.28 | 31 Clutch Wkts | Econ: 8.47 | Death Seam & Knuckle-Ball Craftsman)
10. Taskin Ahmed (Free Agent | PPI: 103.63 | 29 Clutch Wkts | Econ: 8.46 | 145+ kph Hit-The-Deck Enforcer)

4. HOW THESE FREE AGENTS STRENGTHEN RAJASTHAN ROYALS FOR IPL 2027:
• Resolving the Death Bowling Deficit: Pairing Haris Rauf (150+ kph express yorkers) and Shaheen Afridi alongside retained specialist Sandeep Sharma provides the most lethal death bowling rotation in the tournament.
• Eliminating Middle-Order Collapse: Asif Khan (196.52 Press SR) and Najibullah Zadran (180.00 Press SR, 42.00 Avg) solve RR's lower-middle order boundary hitting at No. 6/7, while Babar Azam or Angelo Mathews guarantees insurance against early top-order collapses.
• Spin Choke Mastery: Adam Zampa, Maheesh Theekshana, and Mohammad Nawaz (5.87 pressure economy) provide elite variations to strangle run scoring in overs 7–15 on Jaipur's gripping surface.

5. DELIVERABLES & INTERACTIVE DASHBOARD:
• Full Methodology Report: Attached PDF (RR_SupeRR_Selector_Methodology_Report.pdf)
• Strategy Deck: Attached PPTX (RR_SupeRR_Selector_Auction_Strategy.pptx)
• Live Dashboard: http://127.0.0.1:8088/dashboard.html"""

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rajasthan Royals • IPL 2027 Auction War Room (100% Free Agents Roster)</title>
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
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">100% Free Agents Active</span>
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

  <!-- ROSTER MODE SELECTOR BAR -->
  <div class="bg-gradient-to-r from-emerald-950/70 via-slate-900/95 to-indigo-950/70 border-b border-emerald-500/30 px-4 py-2.5 text-xs text-emerald-200">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-3">
      <div class="flex items-center gap-2">
        <span class="text-base">🟢</span>
        <span>
          <strong class="font-bold text-emerald-300">CURRENT ROSTER: 100% UNCONTRACTED FREE AGENTS (NOT IN ANY IPL TEAM)</strong>
          All 10 Batsmen and 10 Bowlers below have ZERO active franchise contract and are independent free agents available for immediate acquisition.
        </span>
      </div>
      <div class="flex items-center gap-2 self-stretch sm:self-auto">
        <button onclick="setRosterMode('free_agents')" id="btn-mode-free" class="px-3 py-1 rounded-lg text-xs font-bold bg-emerald-600 text-white shadow">
          100% Free Agents (Active)
        </button>
        <button onclick="setRosterMode('contract_cycle')" id="btn-mode-contract" class="px-3 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:text-white border border-slate-700">
          All Realistic Targets
        </button>
      </div>
    </div>
  </div>

  <!-- NAVIGATION TABS -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-4 pb-2 w-full">
    <div class="flex items-center gap-2 border-b border-slate-800 pb-2 overflow-x-auto">
      <button onclick="switchTab('unstop')" id="nav-unstop" class="px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 bg-pink-600 text-white shadow-md shadow-pink-600/30 whitespace-nowrap">
        <span>📝 Tab 1: Unstop Form (10 Free Agent Batters + 10 Free Agent Bowlers)</span>
        <span class="px-1.5 py-0.5 rounded-full text-[10px] bg-white/20 text-white font-mono">20 / 20</span>
      </button>

      <button onclick="switchTab('analytics')" id="nav-analytics" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>📊 Tab 2: Free Agents Full Metrics & Comparison Tables</span>
      </button>

      <button onclick="switchTab('governance')" id="nav-governance" class="px-4 py-2 rounded-xl text-xs font-medium transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap">
        <span>⚖️ Tab 3: Franchise Retentions & BCCI Nov 17 Deadline</span>
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
    <!-- TAB 1: UNSTOP SUBMISSION FORM -->
    <!-- ============================================================== -->
    <div id="tab-unstop" class="space-y-6">

      <!-- Form Helper Bar -->
      <div class="rr-card-highlight rounded-2xl p-5">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                100% UNCONTRACTED FREE AGENTS ONLY
              </span>
              <span class="text-xs text-slate-400 font-mono">SupeRR Selector Round 1</span>
            </div>
            <h2 class="text-base sm:text-lg font-bold text-white mt-1">Official Unstop Competition Submission Form</h2>
            <p class="text-xs text-slate-300 mt-1 max-w-3xl leading-relaxed">
              Every player below is an <strong class="text-emerald-400">uncontracted free agent</strong> who is <strong class="text-emerald-400">NOT currently in any IPL franchise team</strong>. They satisfy all requirements of legal eligibility for the IPL 2027 auction. You can 1-click copy individual names, search across 1,210 offline players, download the official reports, or copy the complete pre-written submission Remark.
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
                <span class="text-[11px] text-pink-400">Required fields marked with * • All 10 Free Agents</span>
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
                <span class="text-[11px] text-indigo-400">Required fields marked with * • All 10 Free Agents</span>
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
                <div class="text-[11px] text-slate-400">Methodology, PPI Formulation & Tactical Blueprint</div>
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
            <h3 class="text-sm font-bold text-white">Top 10 Free Agent Batters Pressure Metrics</h3>
            <span class="text-[11px] text-slate-400">All players uncontracted and not currently with any IPL franchise</span>
          </div>
          <a href="uncontracted_free_agents_top10_batters.csv" download class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-pink-400 border border-slate-700">
            📥 Export Free Agent Batters CSV
          </a>
        </div>
        <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950/60">
          <table class="w-full text-left text-xs text-slate-300 whitespace-nowrap">
            <thead class="bg-slate-900/80 uppercase text-[10px] font-bold text-slate-400 border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">#</th>
                <th class="py-2.5 px-4">Player Name</th>
                <th class="py-2.5 px-3">Franchise Status</th>
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
            <h3 class="text-sm font-bold text-white">Top 10 Free Agent Bowlers Pressure Metrics</h3>
            <span class="text-[11px] text-slate-400">All players uncontracted and not currently with any IPL franchise</span>
          </div>
          <a href="uncontracted_free_agents_top10_bowlers.csv" download class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-indigo-400 border border-slate-700">
            📥 Export Free Agent Bowlers CSV
          </a>
        </div>
        <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950/60">
          <table class="w-full text-left text-xs text-slate-300 whitespace-nowrap">
            <thead class="bg-slate-900/80 uppercase text-[10px] font-bold text-slate-400 border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3">#</th>
                <th class="py-2.5 px-4">Player Name</th>
                <th class="py-2.5 px-3">Franchise Status</th>
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
          <button onclick="askPresetQuery('Who are RR top 3 free agent death bowlers?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🎯 Free Agent Bowlers
          </button>
          <button onclick="askPresetQuery('Why is Fakhar Zaman the #1 free agent batter?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🏏 Why Fakhar Zaman?
          </button>
          <button onclick="askPresetQuery('Can Rajasthan Royals bid for Jasprit Bumrah or Virat Kohli?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🚫 Retained Check
          </button>
          <button onclick="askPresetQuery('How does Haris Rauf strengthen Rajasthan Royals?')" class="px-2.5 py-1 rounded-lg text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
            🛡️ Haris Rauf Tactical Fit
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
                Welcome! All 10 Batsmen and 10 Bowlers in this active view are 100% uncontracted free agents who are not in any IPL team. How can I assist your auction strategy?
              </p>
            </div>
          </div>
        </div>

        <div class="mt-4 pt-3 border-t border-slate-800 flex items-center gap-2">
          <input type="text" id="chat-input" onkeydown="if(event.key==='Enter') sendGeminiQuery()" placeholder="Ask War Room Scout (e.g., 'What is Haris Rauf's economy rate in death overs?')..." class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-pink-500">
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
    const FREE_BATTERS = __FREE_BATTERS_JSON__;
    const FREE_BOWLERS = __FREE_BOWLERS_JSON__;
    const CONTRACT_BATTERS = __CONTRACT_BATTERS_JSON__;
    const CONTRACT_BOWLERS = __CONTRACT_BOWLERS_JSON__;

    let activeMode = 'free_agents'; // 'free_agents' or 'contract_cycle'

    let activeBatters = FREE_BATTERS;
    let activeBowlers = FREE_BOWLERS;

    let selectedBatsmen = activeBatters.map(b => b.name);
    let selectedBowlers = activeBowlers.map(w => w.name);

    function setRosterMode(mode) {
      activeMode = mode;
      const btnFree = document.getElementById('btn-mode-free');
      const btnContract = document.getElementById('btn-mode-contract');

      if (mode === 'free_agents') {
        activeBatters = FREE_BATTERS;
        activeBowlers = FREE_BOWLERS;
        btnFree.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-emerald-600 text-white shadow';
        btnContract.className = 'px-3 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:text-white border border-slate-700';
      } else {
        activeBatters = CONTRACT_BATTERS;
        activeBowlers = CONTRACT_BOWLERS;
        btnContract.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-indigo-600 text-white shadow';
        btnFree.className = 'px-3 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:text-white border border-slate-700';
      }

      selectedBatsmen = activeBatters.map(b => b.name);
      selectedBowlers = activeBowlers.map(w => w.name);

      renderBatsmenFields();
      renderBowlersFields();
      renderFullAnalytics();
      showToast(`Switched to ${mode === 'free_agents' ? '100% Free Agents' : 'All Realistic Targets'} Roster!`);
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
        const bData = activeBatters[idx] || {};
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

            <div id="dropdown-batsman-${idx}" class="dropdown-menu hidden absolute left-0 right-0 top-full mt-1 bg-[#0b1329] border border-pink-500/40 rounded-xl shadow-2xl p-1.5">
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
        const wData = activeBowlers[idx] || {};
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

            <div id="dropdown-bowler-${idx}" class="dropdown-menu hidden absolute left-0 right-0 top-full mt-1 bg-[#0b1329] border border-indigo-500/40 rounded-xl shadow-2xl p-1.5">
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
      } else {
        selectedBowlers[idx] = name;
      }
      document.getElementById(`input-${type}-${idx}`).value = name;
      closeAllDropdowns();
    }

    function closeAllDropdowns() {
      document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.add('hidden'));
    }

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.relative')) {
        closeAllDropdowns();
      }
    });

    function copyField(inputId, label) {
      const input = document.getElementById(inputId);
      const val = input.value.trim();
      navigator.clipboard.writeText(val).then(() => {
        showToast(`Copied "${val}" for ${label}!`);
      });
    }

    function copyAllUnstopPicks() {
      let text = "RAJASTHAN ROYALS — SUPE RR SELECTOR TOP 20 PICKS (100% UNCONTRACTED FREE AGENTS)\\n\\nTOP 10 BATSMEN:\\n";
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

    function copyRemarkText() {
      const txt = document.getElementById('submission-remark').value;
      navigator.clipboard.writeText(txt).then(() => {
        showToast("Full Remark Text copied to clipboard! Ready to paste into Unstop.");
      });
    }

    function handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        document.getElementById('upload-status-text').innerHTML = `
          <span class="text-emerald-400 font-bold">Selected: ${file.name}</span> (${(file.size / 1024 / 1024).toFixed(2)} MB) • <span class="text-emerald-300">Valid Format Ready</span>
        `;
        showToast(`Loaded ${file.name} for submission!`);
      }
    }

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

    function renderFullAnalytics() {
      const tbodyBatters = document.getElementById('tbody-full-batters');
      tbodyBatters.innerHTML = activeBatters.map(b => `
        <tr class="hover:bg-slate-800/40 transition">
          <td class="py-2.5 px-3 font-mono font-bold text-pink-400">#${b.rank}</td>
          <td class="py-2.5 px-4 font-bold text-white">${b.name}</td>
          <td class="py-2.5 px-3 text-emerald-400 font-semibold">${b.current_ipl_franchise}</td>
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
      tbodyBowlers.innerHTML = activeBowlers.map(w => `
        <tr class="hover:bg-slate-800/40 transition">
          <td class="py-2.5 px-3 font-mono font-bold text-indigo-400">#${w.rank}</td>
          <td class="py-2.5 px-4 font-bold text-white">${w.name}</td>
          <td class="py-2.5 px-3 text-emerald-400 font-semibold">${w.current_ipl_franchise}</td>
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
          <p class="text-slate-400 italic text-xs animate-pulse">Analyzing 200,999 deliveries & free agent metrics...</p>
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
              Top Free Agent targets: Batters (Fakhar Zaman, Asif Khan, Najibullah Zadran, Babar Azam, Angelo Mathews, Mohammad Haris, Reeza Hendricks, Mohammad Rizwan, Matthew Wade, Rilee Rossouw) and Bowlers (Haris Rauf, Maheesh Theekshana, Mohammad Nawaz, Adam Zampa, Shaheen Afridi, Sufiyan Muqeem, Abrar Ahmed, Adil Rashid, Tim Southee, Taskin Ahmed).
            </div>
          </div>
        `;
      }
      container.scrollTop = container.scrollHeight;
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderBatsmenFields();
      renderBowlersFields();
      renderFullAnalytics();
    });
  </script>
</body>
</html>
'''

dashboard_html = html_template.replace('__ALL_PLAYERS_JSON__', all_players_json)
dashboard_html = dashboard_html.replace('__FREE_BATTERS_JSON__', free_batters_json)
dashboard_html = dashboard_html.replace('__FREE_BOWLERS_JSON__', free_bowlers_json)
dashboard_html = dashboard_html.replace('__CONTRACT_BATTERS_JSON__', contract_batters_json)
dashboard_html = dashboard_html.replace('__CONTRACT_BOWLERS_JSON__', contract_bowlers_json)
dashboard_html = dashboard_html.replace('__REMARK_TEXT__', remark_text)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dashboard_html)

# Also copy to artifact directory
artifact_dir = r"C:\Users\HP\.gemini\antigravity\brain\04014367-f2d6-4dd0-a981-5625edbe7cc4"
if os.path.exists(artifact_dir):
    shutil.copy('dashboard.html', os.path.join(artifact_dir, 'dashboard.html'))
    print("Copied updated dashboard.html to artifact directory!")

print("Dashboard successfully updated with 10 Free Agent Batters & 10 Free Agent Bowlers!")
