with open('build_ipl2027_war_room_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

bad_func = """    function renderAuditTab() {
      // 1. Render Change Report
      const chgBody = document.getElementById('audit-change-table-body');
      if (chgBody) {
        chgBody.innerHTML = '';
        changeReportData.forEach(chg => {
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="py-2.5 px-3 font-bold text-rose-400">${chg.removed_player}</td>
            <td class="py-2.5 px-3 text-slate-300">${chg.list}</td>
            <td class="py-2.5 px-3 text-slate-400 text-[10px] leading-tight">${chg.reason_for_removal}</td>
            <td class="py-2.5 px-3">
              <span class="font-bold text-emerald-400">${chg.replacement_player}</span>
              <span class="ml-1 px-1.5 py-0.5 rounded text-[9px] bg-emerald-500/20 text-emerald-300">VERIFIED</span>
            </td>
            <td class="py-2.5 px-3 text-slate-300 text-[10px] leading-tight">${chg.why_replacement_better}</td>
          `;
          chgBody.appendChild(tr);
        });
      }

      // 2. Render Retired Players
      const retBody = document.getElementById('audit-retired-table-body');
      if (retBody) {
        retBody.innerHTML = '';
        retiredPlayersData.forEach(r => {
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="py-2.5 px-3 font-bold text-white">${r.player_name}</td>
            <td class="py-2.5 px-3 text-slate-400">${r.nationality}</td>
            <td class="py-2.5 px-3 text-slate-300">${r.retirement_type}</td>
            <td class="py-2.5 px-3 text-amber-400">${r.announcement_date}</td>
            <td class="py-2.5 px-3 text-slate-400 text-[10px]">${r.official_source}</td>
            <td class="py-2.5 px-3">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30">RETIRED FROM IPL</span>
            </td>
          `;
          retBody.appendChild(tr);
        });
      }

      // 3. Render Pakistani Players
      const pakBody = document.getElementById('audit-pak-table-body');
      if (pakBody) {
        pakBody.innerHTML = '';
        pakistaniPlayersData.forEach(p => {
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="py-2.5 px-3 font-bold text-white">${p.player_name}</td>
            <td class="py-2.5 px-3 text-slate-400">${p.role}</td>
            <td class="py-2.5 px-3 text-slate-400">${p.nationality}</td>
            <td class="py-2.5 px-3 text-slate-400 text-[10px]">${p.governing_rule}</td>
            <td class="py-2.5 px-3">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">NOT ELIGIBLE</span>
            </td>
          `;
          pakBody.appendChild(tr);
        });
      }
    }"""

good_func = """    function renderAuditTab() {{
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
    }}"""

if bad_func in text:
    text = text.replace(bad_func, good_func)
    print("Replaced bad_func with good_func successfully.")
else:
    print("Warning: bad_func not found!")

with open('build_ipl2027_war_room_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(text)
