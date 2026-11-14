import json
import shutil

with open('dashboard_data.json', 'r', encoding='utf-8') as f:
    data_json = f.read()

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rajasthan Royals • SupeRR Selector Season 2 War Room</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .rr-card {{
      background: rgba(18, 30, 58, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .rr-card:hover {{
      border-color: rgba(216, 27, 96, 0.4);
    }}
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #080e1e;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e3056;
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #d81b60;
    }}
  </style>
</head>
<body class="bg-[#080e1e] text-slate-100 min-h-screen antialiased flex flex-col selection:bg-pink-600 selection:text-white">

  <!-- Top Navigation / Banner -->
  <header class="border-b border-slate-800 bg-[#0b1426]/90 backdrop-blur sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-pink-600 to-rose-400 flex items-center justify-center font-black text-xl shadow-lg shadow-pink-600/30">
          RR
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs uppercase tracking-widest font-extrabold text-pink-500">Rajasthan Royals War Room</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-pink-500/10 text-pink-400 border border-pink-500/20">SupeRR Selector S2</span>
          </div>
          <h1 class="text-base sm:text-lg font-bold text-white tracking-tight flex items-center gap-2">
            IPL 2027 Auction Strategy: Players Under Pressure
          </h1>
        </div>
      </div>

      <!-- Action & View Links -->
      <div class="flex items-center gap-2 sm:gap-3">
        <span class="hidden md:inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"></span>
          200,999 Balls Parsed
        </span>
        <button onclick="copySubmissionDropdowns()" class="px-3 py-1.5 rounded-lg bg-pink-600 hover:bg-pink-500 text-xs font-bold text-white transition flex items-center gap-1.5 shadow-md shadow-pink-600/20">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
          <span class="hidden sm:inline">Copy Top 10 for</span> Unstop
        </button>
      </div>
    </div>
  </header>

  <!-- Hero & KPI Stats -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-4 w-full">
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="rr-card rounded-2xl p-4 flex flex-col justify-between">
        <div class="text-xs text-slate-400 font-medium">Deliveries Analyzed</div>
        <div class="mt-2 flex items-baseline gap-2">
          <span class="text-2xl sm:text-3xl font-extrabold text-white font-mono">200,999</span>
          <span class="text-xs text-emerald-400">100% T20/IPL</span>
        </div>
        <div class="mt-2 text-xs text-slate-500">883 Matches across 141 Series (2022-2026)</div>
      </div>

      <div class="rr-card rounded-2xl p-4 flex flex-col justify-between border-pink-500/30">
        <div class="text-xs text-pink-400 font-medium flex items-center justify-between">
          <span>Clutch Deliveries</span>
          <span class="w-2 h-2 rounded-full bg-pink-500 animate-ping"></span>
        </div>
        <div class="mt-2 flex items-baseline gap-2">
          <span class="text-2xl sm:text-3xl font-extrabold text-pink-400 font-mono">79,935</span>
          <span class="text-xs px-1.5 py-0.5 rounded bg-pink-500/20 text-pink-300 font-semibold">39.8%</span>
        </div>
        <div class="mt-2 text-xs text-slate-400">Death overs, High RRR & Knockouts</div>
      </div>

      <div class="rr-card rounded-2xl p-4 flex flex-col justify-between">
        <div class="text-xs text-slate-400 font-medium">Top Auction Target (Batter)</div>
        <div class="mt-2 flex items-baseline gap-2">
          <span class="text-xl sm:text-2xl font-extrabold text-white">Shashank Singh</span>
          <span class="text-xs px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono">110.2 BRS</span>
        </div>
        <div class="mt-2 text-xs text-slate-400">Press SR: <span class="text-emerald-400 font-semibold font-mono">186.72</span> | Avg: <span class="text-white font-semibold font-mono">46.56</span></div>
      </div>

      <div class="rr-card rounded-2xl p-4 flex flex-col justify-between">
        <div class="text-xs text-slate-400 font-medium">Top Auction Target (Bowler)</div>
        <div class="mt-2 flex items-baseline gap-2">
          <span class="text-xl sm:text-2xl font-extrabold text-white">Arshdeep Singh</span>
          <span class="text-xs px-2 py-0.5 rounded bg-pink-500/20 text-pink-300 font-mono">317.2 WRS</span>
        </div>
        <div class="mt-2 text-xs text-slate-400">Press Wkts: <span class="text-pink-400 font-semibold font-mono">126</span> (Econ: 9.46)</div>
      </div>
    </div>
  </section>

  <!-- Navigation Tabs -->
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full border-b border-slate-800">
    <nav class="flex space-x-2 sm:space-x-4 overflow-x-auto py-2">
      <button onclick="switchTab('warroom')" id="tab-btn-warroom" class="tab-btn active px-4 py-2 rounded-xl text-sm font-bold bg-pink-600 text-white transition flex items-center gap-2">
        🏛️ IPL 2027 RR War Room
      </button>
      <button onclick="switchTab('submission')" id="tab-btn-submission" class="tab-btn px-4 py-2 rounded-xl text-sm font-medium text-slate-400 hover:text-white hover:bg-slate-800/60 transition flex items-center gap-2">
        🏆 Unstop Top 10 Submissions
      </button>
      <button onclick="switchTab('batters')" id="tab-btn-batters" class="tab-btn px-4 py-2 rounded-xl text-sm font-medium text-slate-400 hover:text-white hover:bg-slate-800/60 transition flex items-center gap-2">
        🏏 Batters Pressure Explorer
      </button>
      <button onclick="switchTab('bowlers')" id="tab-btn-bowlers" class="tab-btn px-4 py-2 rounded-xl text-sm font-medium text-slate-400 hover:text-white hover:bg-slate-800/60 transition flex items-center gap-2">
        🎯 Bowlers Pressure Explorer
      </button>
      <button onclick="switchTab('h2h')" id="tab-btn-h2h" class="tab-btn px-4 py-2 rounded-xl text-sm font-medium text-slate-400 hover:text-white hover:bg-slate-800/60 transition flex items-center gap-2">
        ⚔️ Head-to-Head Compare
      </button>
      <button onclick="switchTab('methodology')" id="tab-btn-methodology" class="tab-btn px-4 py-2 rounded-xl text-sm font-medium text-slate-400 hover:text-white hover:bg-slate-800/60 transition flex items-center gap-2">
        📑 Methodology & Formulas
      </button>
    </nav>
  </div>

  <!-- Main Content Container -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full flex-1">

    <!-- TAB 0: IPL 2027 RR WAR ROOM & SQUAD FIT -->
    <div id="tab-warroom" class="space-y-6">

      <!-- Executive War Room Header -->
      <div class="p-5 rounded-2xl bg-gradient-to-r from-pink-950/60 via-slate-900 to-indigo-950/60 border border-pink-500/30 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded text-[10px] font-black uppercase bg-pink-500 text-white">IPL 2027 War Room</span>
            <span class="text-xs text-pink-400 font-semibold">Rajasthan Royals Proprietary Recruitment Brief</span>
          </div>
          <h2 class="text-xl font-extrabold text-white mt-1">Solving RR's Structural Bottlenecks with Pressure Analytics</h2>
          <p class="text-xs text-slate-300 mt-1 max-w-3xl leading-relaxed">
            By filtering out low-stakes accumulation and evaluating 79,935 pressure deliveries, we identify the exact domestic and overseas match-winners who mathematically elevate Rajasthan Royals into championship contenders.
          </p>
        </div>
        <div class="flex flex-col sm:flex-row gap-2 w-full md:w-auto">
          <a href="RR_SupeRR_Selector_Auction_Strategy.pptx" download class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-white transition flex items-center justify-center gap-2 border border-slate-700">
            📊 Download PPT Deck
          </a>
          <a href="RR_SupeRR_Selector_Methodology_Report.pdf" download class="px-3.5 py-2 rounded-xl bg-pink-600 hover:bg-pink-500 text-xs font-bold text-white transition flex items-center justify-center gap-2 shadow-lg shadow-pink-600/20">
            📄 Download PDF Report
          </a>
        </div>
      </div>

      <!-- 4 Strategic Target Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

        <!-- Target 1: Shashank Singh -->
        <div class="rr-card rounded-2xl p-5 border border-pink-500/30 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-400 flex items-center justify-center font-bold text-sm">#1</span>
                <div>
                  <h3 class="text-base font-bold text-white">Shashank Singh</h3>
                  <div class="text-[11px] text-pink-400 font-medium">Domestic Finisher • Target: ₹6–9 Cr</div>
                </div>
              </div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-pink-500/20 text-pink-300 font-mono">TIER 1 MUST-BUY</span>
            </div>

            <div class="grid grid-cols-3 gap-2 my-3 text-center">
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Press Strike Rate</div>
                <div class="text-sm font-mono font-bold text-emerald-400">186.72</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Press Average</div>
                <div class="text-sm font-mono font-bold text-white">46.56</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Clutch Delta</div>
                <div class="text-sm font-mono font-bold text-pink-400">+25.11 SR</div>
              </div>
            </div>

            <div class="text-xs text-slate-300 space-y-1.5 mt-2">
              <div class="font-semibold text-white">Why he strengthens Rajasthan Royals:</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Solves RR's over-reliance on Shimron Hetmyer and Dhruv Jurel at the death. When required rate climbs &ge; 10 RPO, Shashank does not panic or throw his wicket; he averages 46.56 while striking at 186.72 across 399 pressure deliveries.
              </p>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400 flex items-center justify-between">
            <span>Primary Role: Position 6 Finisher</span>
            <span class="text-emerald-400 font-medium">Saves Overseas Slot</span>
          </div>
        </div>

        <!-- Target 2: Arshdeep Singh -->
        <div class="rr-card rounded-2xl p-5 border border-indigo-500/30 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-sm">#2</span>
                <div>
                  <h3 class="text-base font-bold text-white">Arshdeep Singh</h3>
                  <div class="text-[11px] text-indigo-400 font-medium">Left-Arm Death Anchor • Target: ₹14–16 Cr</div>
                </div>
              </div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 font-mono">TIER 1 MARQUEE</span>
            </div>

            <div class="grid grid-cols-3 gap-2 my-3 text-center">
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Clutch Wickets</div>
                <div class="text-sm font-mono font-bold text-pink-400">126 Wkts</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Pressure Balls</div>
                <div class="text-sm font-mono font-bold text-white">1,754 Balls</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Dot Ball %</div>
                <div class="text-sm font-mono font-bold text-emerald-400">36.8%</div>
              </div>
            </div>

            <div class="text-xs text-slate-300 space-y-1.5 mt-2">
              <div class="font-semibold text-white">Why he strengthens Rajasthan Royals:</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Transforms RR's death bowling defense at Sawai Mansingh Stadium. While Sandeep Sharma provides knuckle-balls and wide yorkers, Arshdeep brings high-pace left-arm angles and toe-crushers in overs 18 & 20. Holds the #1 bowling score in cricket.
              </p>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400 flex items-center justify-between">
            <span>Primary Role: Overs 1–2 & 18–20</span>
            <span class="text-indigo-400 font-medium">Lethal Closing Pair w/ Sandeep</span>
          </div>
        </div>

        <!-- Target 3: Varun Chakravarthy / Ravi Bishnoi -->
        <div class="rr-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-400 flex items-center justify-center font-bold text-sm">#3</span>
                <div>
                  <h3 class="text-base font-bold text-white">Varun Chakravarthy / Ravi Bishnoi</h3>
                  <div class="text-[11px] text-teal-400 font-medium">High-Leverage Spin Enforcers • Target: ₹6–8 Cr</div>
                </div>
              </div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 font-mono">TIER 2 ENFORCERS</span>
            </div>

            <div class="grid grid-cols-3 gap-2 my-3 text-center">
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Varun Dot %</div>
                <div class="text-sm font-mono font-bold text-emerald-400">40.0%</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Varun Econ</div>
                <div class="text-sm font-mono font-bold text-white">8.66</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Bishnoi Wkts</div>
                <div class="text-sm font-mono font-bold text-pink-400">67 Wkts</div>
              </div>
            </div>

            <div class="text-xs text-slate-300 space-y-1.5 mt-2">
              <div class="font-semibold text-white">Why they strengthen Rajasthan Royals:</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Suffocates opposition acceleration in overs 10–15. Varun boasts a tournament-high 40% dot balls under pressure, starving power-hitters of momentum and forcing false shots before the death phase.
              </p>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400 flex items-center justify-between">
            <span>Primary Role: Middle-Overs Strangle</span>
            <span class="text-teal-400 font-medium">Boundary Denial Kings</span>
          </div>
        </div>

        <!-- Target 4: Naman Dhir & Emerging Steals -->
        <div class="rr-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <div class="flex items-center gap-2.5">
                <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-sm">#4</span>
                <div>
                  <h3 class="text-base font-bold text-white">Naman Dhir & Vaibhav Sooryavanshi</h3>
                  <div class="text-[11px] text-amber-400 font-medium">Dynamic High-Upside Strikers • Target: ₹2–4 Cr</div>
                </div>
              </div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 font-mono">TIER 3 HIGH VALUE</span>
            </div>

            <div class="grid grid-cols-3 gap-2 my-3 text-center">
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Naman Press SR</div>
                <div class="text-sm font-mono font-bold text-emerald-400">195.80</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Vaibhav Press SR</div>
                <div class="text-sm font-mono font-bold text-pink-400">231.93</div>
              </div>
              <div class="bg-slate-950/80 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Boundary Rate</div>
                <div class="text-sm font-mono font-bold text-white">&gt; 27%</div>
              </div>
            </div>

            <div class="text-xs text-slate-300 space-y-1.5 mt-2">
              <div class="font-semibold text-white">Why they strengthen Rajasthan Royals:</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Elite squad depth without bloating the auction budget. Naman strikes at 195.8 under pressure against express pace, offering flexible deployment as an impact sub or top/middle-order counter-attacker.
              </p>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[11px] text-slate-400 flex items-center justify-between">
            <span>Primary Role: High-Impact Floaters</span>
            <span class="text-amber-400 font-medium">Budget Efficiency Steals</span>
          </div>
        </div>

      </div>

      <!-- Optimized RR Playing XI -->
      <div class="rr-card rounded-2xl p-5 border border-slate-800">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div>
            <h3 class="text-base font-bold text-white">The Optimized Rajasthan Royals IPL 2027 Playing XI</h3>
            <span class="text-xs text-slate-400">Integrating Clutch Auction Targets into RR's Retained Core</span>
          </div>
          <span class="text-xs px-2.5 py-1 rounded bg-pink-500/20 text-pink-300 font-semibold">Championship Blueprint</span>
        </div>

        <div class="overflow-x-auto mt-4">
          <table class="w-full text-left text-xs text-slate-300">
            <thead class="bg-slate-950/80 text-slate-400 font-semibold border-b border-slate-800 uppercase tracking-wider text-[11px]">
              <tr>
                <th class="py-2.5 px-3">Pos</th>
                <th class="py-2.5 px-4">Player</th>
                <th class="py-2.5 px-3">Role</th>
                <th class="py-2.5 px-3">Pressure Archetype</th>
                <th class="py-2.5 px-4">Tactical Role in 2027 XI</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/50">
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">1</td>
                <td class="py-2.5 px-4 font-bold text-white">Yashasvi Jaiswal</td>
                <td class="py-2.5 px-3">LHB Opener</td>
                <td class="py-2.5 px-3 text-emerald-400 font-semibold">Powerplay Aggressor</td>
                <td class="py-2.5 px-4 text-slate-400">Retained Core: Sets blistering powerplay pace</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">2</td>
                <td class="py-2.5 px-4 font-bold text-white">Overseas Aggressor / Jos Buttler</td>
                <td class="py-2.5 px-3">RHB Opener/WK</td>
                <td class="py-2.5 px-3 text-slate-300">High-Stakes Rebuilder</td>
                <td class="py-2.5 px-4 text-slate-400">Experience anchor & match accelerator</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">3</td>
                <td class="py-2.5 px-4 font-bold text-white">Sanju Samson (C)</td>
                <td class="py-2.5 px-3">RHB Top Order</td>
                <td class="py-2.5 px-3 text-pink-400 font-semibold">Middle Dynamo</td>
                <td class="py-2.5 px-4 text-slate-400">Retained Core: Counter-attacks against spin</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">4</td>
                <td class="py-2.5 px-4 font-bold text-white">Riyan Parag</td>
                <td class="py-2.5 px-3">RHB Middle Order</td>
                <td class="py-2.5 px-3 text-slate-300">Phase 2 Accelerator</td>
                <td class="py-2.5 px-4 text-slate-400">Retained Core: High tempo in overs 8–15</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">5</td>
                <td class="py-2.5 px-4 font-bold text-white">Dhruv Jurel (WK)</td>
                <td class="py-2.5 px-3">RHB Finisher</td>
                <td class="py-2.5 px-3 text-emerald-400 font-semibold">Ice-Cool Floater</td>
                <td class="py-2.5 px-4 text-slate-400">Retained Core: Strike rotation & boundary acceleration</td>
              </tr>
              <tr class="bg-pink-950/30 border-l-2 border-pink-500">
                <td class="py-2.5 px-3 font-mono text-pink-400 font-bold">6</td>
                <td class="py-2.5 px-4 font-bold text-white flex items-center gap-1.5">
                  SHASHANK SINGH
                  <span class="px-1.5 py-0.2 rounded text-[9px] bg-pink-500 text-white font-black">AUCTION TARGET</span>
                </td>
                <td class="py-2.5 px-3 text-pink-300 font-semibold">RHB Finisher</td>
                <td class="py-2.5 px-3 text-emerald-400 font-bold">RANK #2 CLUTCH BATTER</td>
                <td class="py-2.5 px-4 text-slate-300 font-medium">Auction Target: 186.7 SR & 46.5 Avg in high RRR chases</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">7</td>
                <td class="py-2.5 px-4 font-bold text-white">Shimron Hetmyer / Overseas Finisher</td>
                <td class="py-2.5 px-3">LHB Power Finisher</td>
                <td class="py-2.5 px-3 text-slate-300">Death Destroyer</td>
                <td class="py-2.5 px-4 text-slate-400">Provides left-hand boundary leverage in overs 17–20</td>
              </tr>
              <tr class="bg-indigo-950/30 border-l-2 border-indigo-500">
                <td class="py-2.5 px-3 font-mono text-indigo-400 font-bold">8</td>
                <td class="py-2.5 px-4 font-bold text-white flex items-center gap-1.5">
                  RAVI BISHNOI / VARUN CHAKRAVARTHY
                  <span class="px-1.5 py-0.2 rounded text-[9px] bg-indigo-500 text-white font-black">AUCTION TARGET</span>
                </td>
                <td class="py-2.5 px-3 text-indigo-300 font-semibold">Spin Enforcer</td>
                <td class="py-2.5 px-3 text-teal-400 font-bold">RANK #3 / #5 CLUTCH BOWLER</td>
                <td class="py-2.5 px-4 text-slate-300 font-medium">Auction Target: 40% dot balls under pressure & 8.66 econ</td>
              </tr>
              <tr class="bg-pink-950/30 border-l-2 border-pink-500">
                <td class="py-2.5 px-3 font-mono text-pink-400 font-bold">9</td>
                <td class="py-2.5 px-4 font-bold text-white flex items-center gap-1.5">
                  ARSHDEEP SINGH
                  <span class="px-1.5 py-0.2 rounded text-[9px] bg-pink-500 text-white font-black">AUCTION TARGET</span>
                </td>
                <td class="py-2.5 px-3 text-pink-300 font-semibold">Left-Arm Fast</td>
                <td class="py-2.5 px-3 text-pink-400 font-bold">RANK #1 CLUTCH BOWLER</td>
                <td class="py-2.5 px-4 text-slate-300 font-medium">Auction Target: 126 clutch wickets & master of death yorkers</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">10</td>
                <td class="py-2.5 px-4 font-bold text-white">Sandeep Sharma</td>
                <td class="py-2.5 px-3">RHB Medium-Fast</td>
                <td class="py-2.5 px-3 text-emerald-400 font-semibold">Death Variation Enforcer</td>
                <td class="py-2.5 px-4 text-slate-400">Retained Core: Wide yorkers & dipping knuckle-balls</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-mono text-slate-500">11</td>
                <td class="py-2.5 px-4 font-bold text-white">Overseas Express Seamer (Nandre Burger / Archer)</td>
                <td class="py-2.5 px-3">Fast Bowler</td>
                <td class="py-2.5 px-3 text-slate-300">Powerplay Strike Seam</td>
                <td class="py-2.5 px-4 text-slate-400">Early swing, hostile bounce, and middle-over enforcer</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- TAB 1: UNSTOP SUBMISSION RANKINGS -->
    <div id="tab-submission" class="hidden space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-4 rounded-2xl bg-gradient-to-r from-pink-950/40 via-slate-900 to-indigo-950/40 border border-pink-500/20">
        <div>
          <h2 class="text-lg font-bold text-white flex items-center gap-2">
            <span>Official Round 1 Ranked Submission</span>
            <span class="px-2 py-0.5 rounded text-[11px] bg-pink-500 text-white font-black tracking-wider uppercase">Unstop Ready</span>
          </h2>
          <p class="text-xs text-slate-400 mt-1">
            Ordered 1-10 rankings for Batters and Bowlers based on the Reliability Index formulated on 200k deliveries.
          </p>
        </div>
        <div class="flex items-center gap-2">
          <label class="text-xs text-slate-400 flex items-center gap-2 cursor-pointer bg-slate-800/60 px-3 py-1.5 rounded-lg border border-slate-700">
            <input type="checkbox" id="filter-rr-only" onchange="toggleRROnly(this.checked)" class="rounded text-pink-600 focus:ring-0">
            <span class="text-xs font-semibold text-pink-400">Highlight RR Stars</span>
          </label>
        </div>
      </div>

      <!-- Top 10 Batters & Bowlers Side-by-Side -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <!-- Top 10 Batters Card -->
        <div class="rr-card rounded-2xl p-5 border border-pink-500/20 flex flex-col">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div class="flex items-center gap-2.5">
              <span class="text-xl">🏏</span>
              <div>
                <h3 class="text-base font-bold text-white">Top 10 Batters Under Pressure</h3>
                <span class="text-xs text-slate-400">Formula: Batting Reliability Score (BRS)</span>
              </div>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-pink-400 font-mono font-bold">Ranks 1 to 10</span>
          </div>

          <div class="mt-4 space-y-2.5 flex-1" id="submission-batters-list">
            <!-- Dynamically populated -->
          </div>
        </div>

        <!-- Top 10 Bowlers Card -->
        <div class="rr-card rounded-2xl p-5 border border-indigo-500/20 flex flex-col">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div class="flex items-center gap-2.5">
              <span class="text-xl">🎯</span>
              <div>
                <h3 class="text-base font-bold text-white">Top 10 Bowlers Under Pressure</h3>
                <span class="text-xs text-slate-400">Formula: Bowling Reliability Score (WRS)</span>
              </div>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-indigo-400 font-mono font-bold">Ranks 1 to 10</span>
          </div>

          <div class="mt-4 space-y-2.5 flex-1" id="submission-bowlers-list">
            <!-- Dynamically populated -->
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 2: BATTERS PRESSURE EXPLORER -->
    <div id="tab-batters" class="hidden space-y-4">
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-800">
        <div class="relative flex-1">
          <input type="text" id="batter-search" oninput="renderBattersTable()" placeholder="Search batter name..." class="w-full bg-slate-950/80 border border-slate-800 rounded-lg pl-9 pr-4 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-pink-500">
          <svg class="w-4 h-4 text-slate-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        <div class="flex items-center gap-2">
          <select id="batter-sort" onchange="renderBattersTable()" class="bg-slate-950/80 border border-slate-800 rounded-lg px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-pink-500">
            <option value="score">Sort by Clutch Score (BRS)</option>
            <option value="sr_press">Sort by Pressure Strike Rate</option>
            <option value="avg_press">Sort by Pressure Average</option>
            <option value="sr_delta">Sort by SR Delta (Clutch Boost)</option>
            <option value="balls_press">Sort by Sample Size (Balls)</option>
          </select>
        </div>
      </div>

      <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/40">
        <table class="w-full text-left text-xs text-slate-300">
          <thead class="bg-slate-950/80 uppercase tracking-wider text-[11px] font-bold text-slate-400 border-b border-slate-800">
            <tr>
              <th class="py-3 px-3">#</th>
              <th class="py-3 px-4">Player</th>
              <th class="py-3 px-3 text-right">BRS Score</th>
              <th class="py-3 px-3 text-right">Press SR</th>
              <th class="py-3 px-3 text-right">Base SR</th>
              <th class="py-3 px-3 text-right">SR Delta</th>
              <th class="py-3 px-3 text-right">Press Avg</th>
              <th class="py-3 px-3 text-right">Boundary %</th>
              <th class="py-3 px-3 text-right">Dot %</th>
              <th class="py-3 px-3 text-right">Press Balls</th>
              <th class="py-3 px-3 text-center">Format</th>
            </tr>
          </thead>
          <tbody id="batters-tbody" class="divide-y divide-slate-800/60">
            <!-- Table rows -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 3: BOWLERS PRESSURE EXPLORER -->
    <div id="tab-bowlers" class="hidden space-y-4">
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-800">
        <div class="relative flex-1">
          <input type="text" id="bowler-search" oninput="renderBowlersTable()" placeholder="Search bowler name..." class="w-full bg-slate-950/80 border border-slate-800 rounded-lg pl-9 pr-4 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500">
          <svg class="w-4 h-4 text-slate-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        <div class="flex items-center gap-2">
          <select id="bowler-sort" onchange="renderBowlersTable()" class="bg-slate-950/80 border border-slate-800 rounded-lg px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-indigo-500">
            <option value="score">Sort by Clutch Score (WRS)</option>
            <option value="econ_press">Sort by Lowest Economy</option>
            <option value="wkts_press">Sort by Pressure Wickets</option>
            <option value="dot_pct_press">Sort by Highest Dot Ball %</option>
            <option value="balls_press">Sort by Sample Size (Balls)</option>
          </select>
        </div>
      </div>

      <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/40">
        <table class="w-full text-left text-xs text-slate-300">
          <thead class="bg-slate-950/80 uppercase tracking-wider text-[11px] font-bold text-slate-400 border-b border-slate-800">
            <tr>
              <th class="py-3 px-3">#</th>
              <th class="py-3 px-4">Bowler</th>
              <th class="py-3 px-3 text-right">WRS Score</th>
              <th class="py-3 px-3 text-right">Press Econ</th>
              <th class="py-3 px-3 text-right">Base Econ</th>
              <th class="py-3 px-3 text-right">Econ Delta</th>
              <th class="py-3 px-3 text-right">Press Wkts</th>
              <th class="py-3 px-3 text-right">Dot Ball %</th>
              <th class="py-3 px-3 text-right">Wkt SR</th>
              <th class="py-3 px-3 text-right">Press Balls</th>
              <th class="py-3 px-3 text-center">Format</th>
            </tr>
          </thead>
          <tbody id="bowlers-tbody" class="divide-y divide-slate-800/60">
            <!-- Bowlers rows -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 4: HEAD TO HEAD COMPARISON TOOL -->
    <div id="tab-h2h" class="hidden space-y-6">
      <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800">
        <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <h3 class="text-base font-bold text-white">Compare Player Performance Under Pressure</h3>
            <p class="text-xs text-slate-400">Select two players to benchmark their clutch metrics vs baseline metrics.</p>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="setCompareType('batters')" id="comp-type-batters" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-pink-600 text-white">Batters</button>
            <button onclick="setCompareType('bowlers')" id="comp-type-bowlers" class="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white">Bowlers</button>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Player 1</label>
            <select id="p1-select" onchange="updateComparison()" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-pink-500"></select>
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Player 2</label>
            <select id="p2-select" onchange="updateComparison()" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-pink-500"></select>
          </div>
        </div>
      </div>

      <div id="comparison-display" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Rendered comparison cards -->
      </div>
    </div>

    <!-- TAB 5: METHODOLOGY & MODEL DETAILS -->
    <div id="tab-methodology" class="hidden space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Definition of Pressure -->
        <div class="rr-card rounded-2xl p-5 border border-slate-800">
          <div class="flex items-center gap-2 text-pink-400 font-bold text-sm uppercase tracking-wider mb-2">
            <span>01</span> Mathematical Pressure Definition
          </div>
          <h3 class="text-base font-bold text-white">Multi-Context Situational Trigger</h3>
          <p class="text-xs text-slate-400 mt-2 leading-relaxed">
            Pressure is dynamic and shifts per delivery based on game state. We classify a ball as <span class="text-pink-400 font-semibold">High Pressure</span> if any of the following 4 conditions trigger:
          </p>
          <ul class="mt-3 space-y-2 text-xs text-slate-300">
            <li class="flex items-start gap-2">
              <span class="text-pink-500 font-bold">1.</span>
              <span><strong class="text-white">Death Overs (16-20):</strong> Deliveries 91-120 where run-rate urgency spikes and fielding restrictions tighten. (44,454 balls)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-pink-500 font-bold">2.</span>
              <span><strong class="text-white">Chasing Required Run Rate &ge; 10.0:</strong> In Innings 2, or when &le; 30 balls remain with close margins, or batting side is 5+ wickets down. (32,562 balls)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-pink-500 font-bold">3.</span>
              <span><strong class="text-white">Powerplay Collapse:</strong> Overs 1-6 when 3 or more top-order wickets have already fallen. (1,897 balls)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-pink-500 font-bold">4.</span>
              <span><strong class="text-white">Knockout Crunch:</strong> Overs 12-20 in Playoff / Knockout eliminators, qualifiers, and finals. (1,022 balls)</span>
            </li>
          </ul>
        </div>

        <!-- Rating Formulas -->
        <div class="rr-card rounded-2xl p-5 border border-slate-800">
          <div class="flex items-center gap-2 text-indigo-400 font-bold text-sm uppercase tracking-wider mb-2">
            <span>02</span> Scoring Engine
          </div>
          <h3 class="text-base font-bold text-white">Reliability Indices Formulations</h3>
          <div class="mt-3 space-y-4 text-xs">
            <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800/80">
              <div class="font-bold text-pink-400">Batting Reliability Score (BRS):</div>
              <div class="font-mono text-emerald-400 mt-1 text-[11px]">
                BRS = 0.40 &times; SR_press + 0.40 &times; Avg_press + 0.35 &times; (SR_press - SR_base) + 0.50 &times; (40 - Dot%_press)
              </div>
              <p class="text-[11px] text-slate-400 mt-1">Balances strike rate acceleration under fire with wicket preservation and low dot ball waste.</p>
            </div>

            <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800/80">
              <div class="font-bold text-indigo-400">Bowling Reliability Score (WRS):</div>
              <div class="font-mono text-indigo-400 mt-1 text-[11px]">
                WRS = 7.5 &times; (12.0 - Econ_press) + 2.2 &times; Wkts_press + 0.6 &times; Dot%_press + 3.5 &times; (Econ_base - Econ_press)
              </div>
              <p class="text-[11px] text-slate-400 mt-1">Rewards bowlers who restrict death runs below 10 RPO while claiming breakthroughs and delivering dot balls.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Phase Analysis Table -->
      <div class="rr-card rounded-2xl p-5 border border-slate-800">
        <h3 class="text-sm font-bold text-white uppercase tracking-wider mb-3">T20 Phase Pressure Breakdown</h3>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs text-slate-300">
            <thead class="bg-slate-950/60 text-slate-400 border-b border-slate-800 font-semibold">
              <tr>
                <th class="py-2.5 px-3">Phase</th>
                <th class="py-2.5 px-3 text-right">Total Deliveries</th>
                <th class="py-2.5 px-3 text-right">Avg Run Rate</th>
                <th class="py-2.5 px-3 text-right">Total Wickets</th>
                <th class="py-2.5 px-3 text-right">Balls Per Wicket</th>
                <th class="py-2.5 px-3 text-right">Pressure Proportion</th>
              </tr>
            </thead>
            <tbody id="phases-tbody" class="divide-y divide-slate-800/50">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="border-t border-slate-800/80 py-4 text-center text-xs text-slate-500">
    SupeRR Selector Season 2 • Rajasthan Royals War Room Analytics • 2022-2026 Historical Dataset
  </footer>

  <!-- Notification Toast -->
  <div id="toast" class="fixed bottom-5 right-5 bg-pink-600 text-white px-4 py-2.5 rounded-xl text-xs font-bold shadow-2xl transition duration-300 transform translate-y-16 opacity-0 pointer-events-none z-50">
    Copied to clipboard!
  </div>

  <!-- Inline Data & App Logic -->
  <script>
    const DATA = {data_json};

    let currentCompareType = 'batters';
    let highlightRR = false;

    function init() {{
      renderSubmissionLists();
      renderBattersTable();
      renderBowlersTable();
      renderPhasesTable();
      populateCompareSelects();
      updateComparison();
    }}

    function switchTab(tabName) {{
      ['warroom', 'submission', 'batters', 'bowlers', 'h2h', 'methodology'].forEach(t => {{
        const el = document.getElementById(`tab-${{t}}`);
        if (el) el.classList.add('hidden');
        const btn = document.getElementById(`tab-btn-${{t}}`);
        if (btn) {{
          btn.classList.remove('bg-pink-600', 'text-white');
          btn.classList.add('text-slate-400');
        }}
      }});

      const activeTab = document.getElementById(`tab-${{tabName}}`);
      if (activeTab) activeTab.classList.remove('hidden');
      const activeBtn = document.getElementById(`tab-btn-${{tabName}}`);
      if (activeBtn) {{
        activeBtn.classList.add('bg-pink-600', 'text-white');
        activeBtn.classList.remove('text-slate-400');
      }}
    }}

    function toggleRROnly(checked) {{
      highlightRR = checked;
      renderSubmissionLists();
      renderBattersTable();
      renderBowlersTable();
    }}

    function renderSubmissionLists() {{
      const bList = document.getElementById('submission-batters-list');
      const wList = document.getElementById('submission-bowlers-list');

      // Top 10 Batters
      bList.innerHTML = DATA.top_batters.slice(0, 10).map((b, idx) => {{
        const isHighlight = highlightRR && b.is_rr;
        return `
          <div class="p-3 rounded-xl ${{isHighlight ? 'bg-pink-900/30 border border-pink-500/40' : 'bg-slate-900/60 border border-slate-800'}} flex items-center justify-between hover:border-pink-500/40 transition">
            <div class="flex items-center gap-3">
              <span class="w-6 h-6 rounded-full ${{idx === 0 ? 'bg-amber-400 text-slate-950 font-black' : (idx < 3 ? 'bg-pink-600 text-white font-bold' : 'bg-slate-800 text-slate-300')}} text-xs flex items-center justify-center font-mono">
                ${{idx + 1}}
              </span>
              <div>
                <div class="font-bold text-white text-xs sm:text-sm flex items-center gap-1.5">
                  ${{b.name}}
                  ${{b.is_rr ? '<span class="px-1.5 py-0.2 rounded text-[9px] bg-pink-500/20 text-pink-400 font-extrabold uppercase">RR</span>' : ''}}
                </div>
                <div class="text-[11px] text-slate-400 mt-0.5">
                  ${{b.runs_press}} runs (${{b.balls_press}} balls) • Avg: <span class="text-slate-200 font-medium">${{b.avg_press}}</span>
                </div>
              </div>
            </div>
            <div class="text-right">
              <div class="text-xs font-mono font-bold text-pink-400">Score: ${{b.score}}</div>
              <div class="text-[11px] text-emerald-400 font-mono mt-0.5">SR: ${{b.sr_press}} <span class="text-slate-500 text-[10px]">(${{b.sr_delta > 0 ? '+' : ''}}${{b.sr_delta}})</span></div>
            </div>
          </div>
        `;
      }}).join('');

      // Top 10 Bowlers
      wList.innerHTML = DATA.top_bowlers.slice(0, 10).map((w, idx) => {{
        const isHighlight = highlightRR && w.is_rr;
        return `
          <div class="p-3 rounded-xl ${{isHighlight ? 'bg-indigo-900/30 border border-indigo-500/40' : 'bg-slate-900/60 border border-slate-800'}} flex items-center justify-between hover:border-indigo-500/40 transition">
            <div class="flex items-center gap-3">
              <span class="w-6 h-6 rounded-full ${{idx === 0 ? 'bg-amber-400 text-slate-950 font-black' : (idx < 3 ? 'bg-indigo-600 text-white font-bold' : 'bg-slate-800 text-slate-300')}} text-xs flex items-center justify-center font-mono">
                ${{idx + 1}}
              </span>
              <div>
                <div class="font-bold text-white text-xs sm:text-sm flex items-center gap-1.5">
                  ${{w.name}}
                  ${{w.is_rr ? '<span class="px-1.5 py-0.2 rounded text-[9px] bg-pink-500/20 text-pink-400 font-extrabold uppercase">RR</span>' : ''}}
                </div>
                <div class="text-[11px] text-slate-400 mt-0.5">
                  ${{w.wkts_press}} wkts (${{w.overs_press}} ov) • Dots: <span class="text-slate-200 font-medium">${{w.dot_pct_press}}%</span>
                </div>
              </div>
            </div>
            <div class="text-right">
              <div class="text-xs font-mono font-bold text-indigo-400">Score: ${{w.score}}</div>
              <div class="text-[11px] text-emerald-400 font-mono mt-0.5">Econ: ${{w.econ_press}} <span class="text-slate-500 text-[10px]">(Base ${{w.econ_base}})</span></div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function renderBattersTable() {{
      const query = document.getElementById('batter-search').value.toLowerCase();
      const sortKey = document.getElementById('batter-sort').value;

      let list = [...DATA.top_batters];
      if (query) {{
        list = list.filter(b => b.name.toLowerCase().includes(query));
      }}

      list.sort((a, b) => b[sortKey] - a[sortKey]);

      const tbody = document.getElementById('batters-tbody');
      tbody.innerHTML = list.map((b, idx) => `
        <tr class="hover:bg-slate-800/40 transition ${{b.is_rr ? 'bg-pink-950/20' : ''}}">
          <td class="py-2.5 px-3 font-mono text-slate-500 font-bold">${{idx + 1}}</td>
          <td class="py-2.5 px-4 font-bold text-white flex items-center gap-2">
            ${{b.name}}
            ${{b.is_rr ? '<span class="px-1 py-0.5 rounded text-[9px] bg-pink-500/20 text-pink-400 font-extrabold uppercase">RR</span>' : ''}}
          </td>
          <td class="py-2.5 px-3 text-right font-mono font-extrabold text-pink-400">${{b.score}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-emerald-400 font-semibold">${{b.sr_press}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${{b.sr_base}}</td>
          <td class="py-2.5 px-3 text-right font-mono ${{b.sr_delta >= 0 ? 'text-emerald-400' : 'text-rose-400'}}">
            ${{b.sr_delta >= 0 ? '+' : ''}}${{b.sr_delta}}
          </td>
          <td class="py-2.5 px-3 text-right font-mono">${{b.avg_press}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-300">${{b.bnd_pct_press}}%</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${{b.dot_pct_press}}%</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${{b.balls_press}}</td>
          <td class="py-2.5 px-3 text-center">
            <span class="px-1.5 py-0.5 rounded text-[10px] font-mono bg-slate-800 text-slate-300">${{b.ipl_ratio}}% IPL</span>
          </td>
        </tr>
      `).join('');
    }}

    function renderBowlersTable() {{
      const query = document.getElementById('bowler-search').value.toLowerCase();
      const sortKey = document.getElementById('bowler-sort').value;

      let list = [...DATA.top_bowlers];
      if (query) {{
        list = list.filter(w => w.name.toLowerCase().includes(query));
      }}

      if (sortKey === 'econ_press') {{
        list.sort((a, b) => a.econ_press - b.econ_press);
      }} else {{
        list.sort((a, b) => b[sortKey] - a[sortKey]);
      }}

      const tbody = document.getElementById('bowlers-tbody');
      tbody.innerHTML = list.map((w, idx) => `
        <tr class="hover:bg-slate-800/40 transition ${{w.is_rr ? 'bg-indigo-950/20' : ''}}">
          <td class="py-2.5 px-3 font-mono text-slate-500 font-bold">${{idx + 1}}</td>
          <td class="py-2.5 px-4 font-bold text-white flex items-center gap-2">
            ${{w.name}}
            ${{w.is_rr ? '<span class="px-1 py-0.5 rounded text-[9px] bg-pink-500/20 text-pink-400 font-extrabold uppercase">RR</span>' : ''}}
          </td>
          <td class="py-2.5 px-3 text-right font-mono font-extrabold text-indigo-400">${{w.score}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-emerald-400 font-semibold">${{w.econ_press}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${{w.econ_base}}</td>
          <td class="py-2.5 px-3 text-right font-mono ${{w.econ_delta >= 0 ? 'text-emerald-400' : 'text-rose-400'}}">
            ${{w.econ_delta >= 0 ? '-' : '+'}}${{Math.abs(w.econ_delta)}}
          </td>
          <td class="py-2.5 px-3 text-right font-mono font-bold text-white">${{w.wkts_press}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-300">${{w.dot_pct_press}}%</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${{w.wkt_sr_press}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${{w.balls_press}}</td>
          <td class="py-2.5 px-3 text-center">
            <span class="px-1.5 py-0.5 rounded text-[10px] font-mono bg-slate-800 text-slate-300">${{w.ipl_ratio}}% IPL</span>
          </td>
        </tr>
      `).join('');
    }}

    function renderPhasesTable() {{
      const tbody = document.getElementById('phases-tbody');
      tbody.innerHTML = DATA.phases.map(p => `
        <tr class="hover:bg-slate-800/30">
          <td class="py-2.5 px-3 font-semibold text-white">${{p.phase}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-300">${{p.deliveries.toLocaleString()}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-emerald-400 font-bold">${{p.run_rate}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-white">${{p.wickets.toLocaleString()}}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-400">${{p.balls_per_wkt}} b/w</td>
          <td class="py-2.5 px-3 text-right font-mono text-pink-400 font-semibold">${{p.pressure_pct}}%</td>
        </tr>
      `).join('');
    }}

    function setCompareType(type) {{
      currentCompareType = type;
      document.getElementById('comp-type-batters').className = type === 'batters' ? 'px-3 py-1.5 rounded-lg text-xs font-bold bg-pink-600 text-white' : 'px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white';
      document.getElementById('comp-type-bowlers').className = type === 'bowlers' ? 'px-3 py-1.5 rounded-lg text-xs font-bold bg-pink-600 text-white' : 'px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white';
      populateCompareSelects();
      updateComparison();
    }}

    function populateCompareSelects() {{
      const p1 = document.getElementById('p1-select');
      const p2 = document.getElementById('p2-select');
      const list = currentCompareType === 'batters' ? DATA.top_batters : DATA.top_bowlers;

      p1.innerHTML = list.map((item, i) => `<option value="${{i}}">${{item.name}} (Rank #${{i+1}})</option>`).join('');
      p2.innerHTML = list.map((item, i) => `<option value="${{i}}" ${{i === 1 ? 'selected' : ''}}>${{item.name}} (Rank #${{i+1}})</option>`).join('');
    }}

    function updateComparison() {{
      const i1 = parseInt(document.getElementById('p1-select').value) || 0;
      const i2 = parseInt(document.getElementById('p2-select').value) || 1;
      const list = currentCompareType === 'batters' ? DATA.top_batters : DATA.top_bowlers;
      const o1 = list[i1] || list[0];
      const o2 = list[i2] || list[1];

      const container = document.getElementById('comparison-display');

      if (currentCompareType === 'batters') {{
        container.innerHTML = `
          ${{renderBatterCompCard(o1, i1 + 1)}}
          ${{renderBatterCompCard(o2, i2 + 1)}}
        `;
      }} else {{
        container.innerHTML = `
          ${{renderBowlerCompCard(o1, i1 + 1)}}
          ${{renderBowlerCompCard(o2, i2 + 1)}}
        `;
      }}
    }}

    function renderBatterCompCard(b, rank) {{
      return `
        <div class="rr-card rounded-2xl p-5 border border-slate-800">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <div class="text-xs text-pink-500 font-bold uppercase font-mono">Rank #${{rank}}</div>
              <h4 class="text-base font-bold text-white">${{b.name}}</h4>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">BRS Score</div>
              <div class="text-xl font-black font-mono text-pink-400">${{b.score}}</div>
            </div>
          </div>
          <div class="mt-4 space-y-3 text-xs">
            <div>
              <div class="flex justify-between text-slate-400 mb-1">
                <span>Pressure Strike Rate</span>
                <span class="font-mono text-white font-bold">${{b.sr_press}}</span>
              </div>
              <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full" style="width: ${{Math.min(100, (b.sr_press / 220) * 100)}}%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-slate-400 mb-1">
                <span>Pressure Average</span>
                <span class="font-mono text-white font-bold">${{b.avg_press}}</span>
              </div>
              <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div class="bg-gradient-to-r from-pink-500 to-rose-400 h-full rounded-full" style="width: ${{Math.min(100, (b.avg_press / 60) * 100)}}%"></div>
              </div>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center">
              <div class="bg-slate-950 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">SR Delta</div>
                <div class="text-xs font-mono font-bold ${{b.sr_delta >= 0 ? 'text-emerald-400' : 'text-rose-400'}}">${{b.sr_delta >= 0 ? '+' : ''}}${{b.sr_delta}}</div>
              </div>
              <div class="bg-slate-950 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Boundary %</div>
                <div class="text-xs font-mono font-bold text-pink-400">${{b.bnd_pct_press}}%</div>
              </div>
              <div class="bg-slate-950 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Press Balls</div>
                <div class="text-xs font-mono font-bold text-white">${{b.balls_press}}</div>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    function renderBowlerCompCard(w, rank) {{
      return `
        <div class="rr-card rounded-2xl p-5 border border-slate-800">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <div class="text-xs text-indigo-400 font-bold uppercase font-mono">Rank #${{rank}}</div>
              <h4 class="text-base font-bold text-white">${{w.name}}</h4>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">WRS Score</div>
              <div class="text-xl font-black font-mono text-indigo-400">${{w.score}}</div>
            </div>
          </div>
          <div class="mt-4 space-y-3 text-xs">
            <div>
              <div class="flex justify-between text-slate-400 mb-1">
                <span>Pressure Economy (Lower is Better)</span>
                <span class="font-mono text-emerald-400 font-bold">${{w.econ_press}}</span>
              </div>
              <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div class="bg-gradient-to-r from-teal-400 to-indigo-500 h-full rounded-full" style="width: ${{Math.max(10, Math.min(100, (13 - w.econ_press) * 16))}}%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-slate-400 mb-1">
                <span>Dot Ball % Under Pressure</span>
                <span class="font-mono text-white font-bold">${{w.dot_pct_press}}%</span>
              </div>
              <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div class="bg-gradient-to-r from-indigo-500 to-pink-500 h-full rounded-full" style="width: ${{w.dot_pct_press * 2}}%"></div>
              </div>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center">
              <div class="bg-slate-950 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Pressure Wkts</div>
                <div class="text-xs font-mono font-bold text-white">${{w.wkts_press}}</div>
              </div>
              <div class="bg-slate-950 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Econ Delta</div>
                <div class="text-xs font-mono font-bold ${{w.econ_delta >= 0 ? 'text-emerald-400' : 'text-rose-400'}}">${{w.econ_delta >= 0 ? '-' : '+'}}${{Math.abs(w.econ_delta)}}</div>
              </div>
              <div class="bg-slate-950 p-2 rounded-lg">
                <div class="text-[10px] text-slate-500">Press Overs</div>
                <div class="text-xs font-mono font-bold text-white">${{w.overs_press}}</div>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    function copySubmissionDropdowns() {{
      const batters = DATA.top_batters.slice(0, 10).map((b, i) => `Batter Rank ${{i+1}}: ${{b.name}}`).join('\\n');
      const bowlers = DATA.top_bowlers.slice(0, 10).map((w, i) => `Bowler Rank ${{i+1}}: ${{w.name}}`).join('\\n');
      const text = `=== TOP 10 BATTERS (UNSTOP DROPDOWN) ===\\n${{batters}}\\n\\n=== TOP 10 BOWLERS (UNSTOP DROPDOWN) ===\\n${{bowlers}}`;

      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast');
        toast.classList.remove('translate-y-16', 'opacity-0');
        setTimeout(() => {{
          toast.classList.add('translate-y-16', 'opacity-0');
        }}, 3000);
      }});
    }}

    window.onload = init;
  </script>
</body>
</html>
'''

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

shutil.copyfile('dashboard.html', r'C:\Users\HP\.gemini\antigravity\brain\04014367-f2d6-4dd0-a981-5625edbe7cc4\dashboard.html')
print("dashboard.html updated with IPL 2027 War Room tab!")
