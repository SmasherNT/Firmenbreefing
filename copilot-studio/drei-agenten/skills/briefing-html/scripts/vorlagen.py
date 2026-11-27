"""Eingebettete Vorlagen für briefing_html.py und die Bausteine *-html.py.

Automatisch erzeugt von tools/build.py aus html-vorlagen/. Nicht von Hand ändern.
Der Agent Builder nimmt in Skills keine .css-Dateien an; deshalb liegen alle Vorlagen hier.
"""

VORLAGEN = {
    'briefing.html': (
        '<!doctype html>\n'
        '<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__ · Firmenbriefing</title>\n'
        '<style>\n'
        '*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:85px}body{margin:0;background:#eef2f5;color:#193445;font:15px/1.55 Arial,Helvetica,sans-serif}a{color:#154c61;text-underline-offset:3px}button,input,select{font:inherit}button,summary{cursor:pointer}a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid #c3872d;outline-offset:3px}[hidden]{display:none!important}.mast{background:#132d40;color:#fff}.mast>div{max-width:1520px;margin:auto;padding:25px 32px}.mast h1{margin:4px 0;font-size:30px}.mast p{margin:5px 0}.badge{font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:#e7c690}.tabs{position:sticky;top:0;background:white;border-bottom:1px solid #cfdce2;padding:10px 24px;z-index:3;display:flex;gap:8px;overflow:auto}.tabs button{background:#f0f5f7;border:1px solid #d6e1e6;border-radius:7px;padding:9px 16px;color:#154c61;white-space:nowrap}.tabs button[aria-selected="true"]{background:#154c61;color:#fff}main{max-width:1520px;margin:auto;padding:22px 28px}.module{background:white;border:1px solid #dbe4e8;border-radius:12px;padding:20px 24px;margin:0 0 20px;box-shadow:0 3px 10px #19344505}.module h2{font-size:21px;margin:0 0 14px;padding-bottom:9px;border-bottom:2px solid #dce8eb}.module h3{font-size:17px;margin:8px 0}.module h4{font-size:15px}p{margin:8px 0}.meta,small{color:#607887;font-size:12px}small{display:block}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,270px),1fr));gap:12px}.card{background:#f7fafb;border:1px solid #dbe7eb;border-radius:9px;padding:12px 15px;align-self:start}.card summary{font-weight:600}.card[open]{border-left:3px solid #c3872d}.card p{margin:10px 0}.claim{display:inline-block;margin:3px 4px 3px 0;padding:2px 7px;border-radius:5px;background:#e6eff2;font-size:12px}.claim-detail{border:1px solid #dbe5e9;border-radius:7px;padding:12px;margin:10px 0;scroll-margin-top:85px}.claim-detail summary{font-weight:600}.claim-detail:target{border-left:4px solid #c3872d}.table-wrap{overflow-x:auto;border:1px solid #dbe5e9;border-radius:8px;margin:12px 0}table{border-collapse:collapse;width:100%;font-size:14px}td,th{text-align:left;vertical-align:top;padding:12px;border-bottom:1px solid #dce7eb;min-width:150px}th{background:#eef4f6}tbody tr:last-child td{border-bottom:0}.cell{display:block;text-decoration:none;padding:7px;background:#f4f8f9;border-radius:6px}.cell:hover{background:#e6eef1}.steps{display:flex;gap:4px;margin-top:8px}.steps i{display:block;width:20px;height:7px;background:#dbe3e8;border-radius:2px}.steps .on{background:#154c61}.timeline{border-left:2px solid #d3e2e8;padding-left:18px}.event{display:grid;grid-template-columns:125px 1fr;gap:14px;margin-bottom:12px}time{font-weight:600;color:#154c61;padding-top:12px}.swot{display:grid;grid-template-columns:1fr 1fr;gap:14px}.quadrant{border:1px solid #dce6ea;padding:14px;border-radius:9px;background:#fbfcfd}.quadrant .card{margin:8px 0}.note{display:grid;grid-template-columns:minmax(110px,180px) 1fr;gap:4px 12px;border-bottom:1px solid #e1e9ed;padding:10px 0}.note dt{font-weight:600;font-size:12px;color:#607887}.note dd{margin:0}.evidence{padding-left:22px}.evidence li{padding:8px 0;overflow-wrap:anywhere}.module>details{margin-top:12px}.module>details>summary{font-weight:600;color:#154c61}footer{max-width:1520px;margin:0 auto;padding:0 30px 25px;color:#607887;font-size:12px}body #briefing-company-network{color-scheme:light;--cn-bg:#fff;--cn-target:#154c61;--cn-soft:#f3f7f9;--cn-fg:#193445}.page{overflow-wrap:anywhere}\n'
        '.es-highlights{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:16px}.es-cards{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}.es-card{grid-column:span 2}.es-cards[data-count="4"]>.es-card,.es-cards[data-count="5"]>.es-card:nth-child(n+4){grid-column:span 3}.es-entry{min-width:0;border:1px solid #d8e4e9;border-radius:10px;background:#f7fafb;overflow:hidden}.es-entry:hover{border-color:#84a7b6;background:#f0f6f8}.es-entry>summary{position:relative;list-style:none;padding:17px 38px 17px 18px;cursor:pointer}.es-entry>summary::-webkit-details-marker{display:none}.es-highlight{background:#edf4f7}.es-highlight>summary{height:100%;min-height:112px}.es-value{display:block;font-size:30px;font-weight:700;line-height:1.2;color:#154c61;font-variant-numeric:tabular-nums;overflow-wrap:anywhere}.es-status{font-size:23px}.es-label{display:block;font-weight:600;margin-top:5px}.es-meta{display:block;color:#607887;font-size:12px;margin-top:5px;line-height:1.45}.es-card>summary{height:100%;min-height:126px}.es-kicker{display:block;font-size:10px;text-transform:uppercase;letter-spacing:.07em;color:#956621;font-weight:700;margin-bottom:7px}.es-headline{display:block;font-weight:700;font-size:17px;line-height:1.3}.es-preview{display:block;color:#607887;font-size:13px;line-height:1.5;margin-top:7px}.es-arrow{position:absolute;right:15px;top:17px;color:#154c61;font-size:18px}.es-entry[open]>summary{height:auto}.es-entry[open]{grid-column:1/-1}.es-detail{padding:4px 18px 18px;font-size:15px}.es-statement{background:#edf4f7;border-left:3px solid #c3872d;padding:13px 16px;font-weight:600}.es-detail h4{font-size:14px;margin:18px 0 7px}.es-fact{border-top:1px solid #dce6eb;padding:12px 0}.es-fact>summary{font-size:14px;font-weight:600}.es-dialog{width:min(880px,calc(100vw - 32px));max-height:calc(100dvh - 48px);padding:0;border:1px solid #d6e3e8;border-radius:14px;color:#193445;background:#fff;box-shadow:0 24px 90px #132d4060}.es-dialog::backdrop{background:#132d4090}.es-dialog-head{position:sticky;top:0;display:flex;align-items:center;gap:15px;justify-content:space-between;background:white;border-bottom:1px solid #dce6eb;padding:17px 22px;z-index:1}.es-dialog-head h3{margin:0;font-size:20px;line-height:1.35}.es-dialog-close{flex:none;width:36px;height:36px;border:1px solid #d5e2e8;border-radius:8px;color:#154c61;background:#f3f7f9;font-size:24px;cursor:pointer}.es-dialog-body{padding:12px 6px}.es-dialog a{overflow-wrap:anywhere}\n'
        '.timeline{border-left-color:#b9d0dc}.event{grid-template-columns:115px minmax(0,1fr);margin-bottom:9px}.event time{font-size:12px}.event-card{padding:0;min-width:0}.event-card>summary{position:relative;list-style:none;padding:11px 35px 11px 14px;font-size:14px;line-height:1.5}.event-card>summary::-webkit-details-marker{display:none}.event-card>summary:hover{background:#edf4f7}.event-title{display:block}.event-arrow{position:absolute;right:13px;top:10px;color:#154c61;font-size:18px}\n'
        '@media(min-width:761px) and (max-width:1100px){.es-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.es-cards>.es-card,.es-cards[data-count="4"]>.es-card,.es-cards[data-count="5"]>.es-card:nth-child(n+4){grid-column:span 1}.es-cards[data-count="5"]>.es-card:last-child{grid-column:1/-1}}\n'
        '\n'
        '@media print{.es-dialog{display:none!important}.es-highlights,.es-cards{display:block}.es-entry{break-inside:avoid;margin-bottom:12px}.es-arrow{display:none}.es-entry>summary{min-height:0;height:auto}.es-value{font-size:22px}.es-headline{font-size:15px}}\n'
        '@media print{body{background:white;font-size:10pt}.tabs{display:none}.mast>div{padding:10px 0}.mast{background:white;color:#193445}main{padding:0;max-width:none}.page[hidden]{display:block!important}.module{box-shadow:none;padding:10px 0;border:0;border-bottom:1px solid #ddd;break-inside:auto}.card,.claim-detail{break-inside:avoid}.swot{display:block}.table-wrap{overflow:visible}td,th{min-width:0}#briefing-company-network .cn-table{display:block}#briefing-company-network .cn-table-wrap{overflow:visible}a{overflow-wrap:anywhere}}\n'
        '\n'
        "body{background:#f3f6f8;color:#173345}.page-kicker{color:#a16e28;font-size:11px;font-weight:700;letter-spacing:.1em;margin:0 0 17px;text-transform:uppercase}.module{border-radius:13px;box-shadow:0 4px 16px #17334504;margin-bottom:24px}.module h2{font-size:24px;line-height:1.3}.card>summary{list-style:none;position:relative;line-height:1.5;padding-right:20px}.card>summary::-webkit-details-marker{display:none}.card>summary::after{content:'↗';position:absolute;right:0;color:#154c61}.event-card>summary::after{display:none}.source-search{display:grid;gap:7px;font-size:12px;color:#607180;max-width:560px;margin:0 0 20px}.source-search input{padding:11px 14px;border:1px solid #cedee6;border-radius:8px;background:white}.capability-wrap{position:relative}.capability-wrap table{min-width:950px;table-layout:fixed}.capability-wrap th,.capability-wrap td{min-width:0;padding:10px;font-size:12px}.capability-wrap th:first-child{position:sticky;left:0;width:180px;background:#f3f7f9;z-index:1}.capability-wrap td{vertical-align:middle}.cell{border:1px solid #dde7ec;min-height:82px;display:flex;flex-direction:column;justify-content:center;gap:7px}.cell-value{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;line-height:1.45}.cell-open{font-size:10px;color:#607180}.steps{margin-top:0}.swot .quadrant{padding:18px;background:#f8fbfc}.quadrant h3{font-size:13px;color:#154c61;text-transform:uppercase;letter-spacing:.06em}.es-dialog-body .es-detail{font-size:14px}.es-dialog-body .es-fact{border-top:1px solid #dce6eb}.es-dialog-body .es-fact>summary{font-size:13px}.es-dialog-body:focus{outline:none}\n"
        '@media print{.source-search,.page-kicker{display:none}.capability-wrap table{min-width:0;table-layout:auto}.capability-wrap th:first-child{position:static;width:auto}.cell-value{-webkit-line-clamp:unset}.cell-open{display:none}}\n'
        '\n'
        '.topic-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.topic-card summary{position:relative;list-style:none;padding:17px 40px 19px 18px;min-height:138px}.topic-card summary::-webkit-details-marker{display:none}.topic-card{align-self:start}.topic-card:hover{border-color:#94b4c2;background:#f0f6f8}.topic-card[open]{grid-column:1/-1}.topic-grid .es-headline{font-size:17px}.topic-grid .es-preview{font-size:13px}.quadrant[data-swot]{--swot-accent:#154c61;--swot-bg:#f4f8fa;border:1px solid color-mix(in srgb,var(--swot-accent) 30%,white);border-top:4px solid var(--swot-accent);background:var(--swot-bg)}.quadrant[data-swot="Strengths"]{--swot-accent:#16734a;--swot-bg:#edf8f1}.quadrant[data-swot="Weaknesses"]{--swot-accent:#b3343c;--swot-bg:#fff0f1}.quadrant[data-swot="Opportunities"]{--swot-accent:#235c9b;--swot-bg:#eef5ff}.quadrant[data-swot="Threats"]{--swot-accent:#9b5c14;--swot-bg:#fff5e8}.quadrant>h3{color:var(--swot-accent)}.quadrant .card{background:#ffffffbd;border-color:color-mix(in srgb,var(--swot-accent) 20%,white)}.quadrant .card[open]{border-left-color:var(--swot-accent)}@media print{.quadrant{print-color-adjust:exact}.topic-card[open]{grid-column:auto}}\n'
        '\n'
        '/* Shared highlight hierarchy: label, value, scope and period. */\n'
        '.es-highlights{gap:14px;align-items:stretch}.es-highlight{background:#f2f7f9;border-top:3px solid #176274}.es-highlight>summary{display:grid;grid-template-rows:38px 76px minmax(36px,1fr) 32px;gap:8px;padding:17px 20px 15px;min-height:242px;height:100%}.es-highlight .es-label{margin:0;padding-right:22px;font-size:13px;line-height:18px;font-weight:700;color:#365562}.es-highlight .es-value{font-size:34px;line-height:1.12;letter-spacing:-.7px;align-self:center;text-wrap:balance;overflow-wrap:normal;word-break:normal}.es-highlight .es-value-medium{font-size:27px;letter-spacing:-.4px}.es-highlight .es-value-compact{font-size:23px;letter-spacing:-.25px}.es-highlight .es-status{font-size:24px;letter-spacing:-.25px}.es-highlight .es-scope{font-size:12px;line-height:17px;color:#607887;align-self:start}.es-highlight .es-period{align-self:end;border-top:1px solid #d5e2e8;padding-top:8px;font-size:11px;line-height:15px;font-weight:600;color:#365562}.es-highlight .es-arrow{top:16px;right:16px;font-size:15px}.es-highlight[open]>summary{height:auto}.es-highlight:focus-within{border-color:#176274}\n'
        '/* Executive Summary: gleiche Informationen, kompaktere Karten. */\n'
        '#executive-summary{padding:16px 20px}\n'
        '#executive-summary>h2{font-size:21px;margin-bottom:11px;padding-bottom:7px}\n'
        '#executive-summary .es-highlights{gap:10px;margin-bottom:10px}\n'
        '#executive-summary .es-highlight>summary{grid-template-rows:auto auto 1fr auto;gap:5px;min-height:0;padding:11px 15px 10px}\n'
        '#executive-summary .es-highlight .es-label{font-size:12px;line-height:1.35;padding-right:18px}\n'
        '#executive-summary .es-highlight .es-value{font-size:28px;line-height:1.15;letter-spacing:-.4px;align-self:start}\n'
        '#executive-summary .es-highlight .es-value-medium{font-size:23px}\n'
        '#executive-summary .es-highlight .es-status{font-size:21px}\n'
        '#executive-summary .es-highlight .es-scope{font-size:11px;line-height:1.4}\n'
        '#executive-summary .es-highlight .es-period{font-size:10px;line-height:1.35;padding-top:5px;margin-top:2px}\n'
        '#executive-summary .es-highlight .es-arrow{top:10px;right:11px;font-size:13px}\n'
        '#executive-summary .es-cards{gap:10px;align-items:stretch}\n'
        '#executive-summary .es-card>summary{min-height:0;padding:11px 28px 12px 13px}\n'
        '#executive-summary .es-kicker{font-size:9px;margin-bottom:4px;letter-spacing:.04em}\n'
        '#executive-summary .es-headline{font-size:15px;line-height:1.3}\n'
        '#executive-summary .es-preview{font-size:12px;line-height:1.4;margin-top:5px}\n'
        '#executive-summary .es-card .es-arrow{top:10px;right:10px;font-size:14px}\n'
        '@media(max-width:760px){#executive-summary .es-highlights{grid-template-columns:1fr}#executive-summary .es-cards{grid-template-columns:1fr}#executive-summary .es-cards>.es-card{grid-column:1/-1}}\n'
        '\n'
        '</style></head><body><header class="mast"><div><div class="badge">__BADGE__</div><h1>__TITLE__</h1><p>__SCOPE__</p><p>Stand __DATE__</p></div></header><nav class="tabs" aria-label="Briefing-Seiten" role="tablist">__TABS__</nav><main>__CONTENT__</main><footer>Fakten und Analysteninterpretation getrennt · Details und Belegstellen per Klick · Quellenstand des jeweiligen Laufs</footer>\n'
        '<dialog class="es-dialog" id="es-dialog" aria-labelledby="es-dialog-title"><div class="es-dialog-head"><h3 id="es-dialog-title"></h3><button type="button" class="es-dialog-close" aria-label="Details schließen">×</button></div><div class="es-dialog-body"></div></dialog>\n'
        '<script>\n'
        '(()=>{\n'
        " const pages=[...document.querySelectorAll('.page')],tabs=[...document.querySelectorAll('[data-page]')];\n"
        " function show(id){pages.forEach(p=>p.hidden=p.id!==id);tabs.forEach(t=>(t.setAttribute('aria-selected',String(t.dataset.page===id)),t.tabIndex=t.dataset.page===id?0:-1));}\n"
        " function reveal(hash,scroll=true){if(!hash)return;let id;try{id=decodeURIComponent(hash.slice(1));}catch{return;}const node=document.getElementById(id);if(!node)return;const page=node.closest('.page');if(page)show(page.id);if(page?.id==='page-sources'){const search=document.getElementById('source-search-input');search.value='';document.querySelectorAll('#page-sources .claim-detail').forEach(n=>n.hidden=false);}for(let p=node;p;p=p.parentElement)if(p.tagName==='DETAILS')p.open=true;if(scroll)node.scrollIntoView({block:'start'});}\n"
        " tabs.forEach(t=>t.addEventListener('click',()=>{show(t.dataset.page);window.scrollTo({top:0,behavior:'instant'});}));show(pages[0].id);\n"
        ' document.addEventListener(\'click\',e=>{const link=e.target.closest(\'a[href^="#"]\');if(link)reveal(link.getAttribute(\'href\'));});\n'
        " window.addEventListener('hashchange',()=>reveal(location.hash));reveal(location.hash);\n"
        ' let printState=null;\n'
        " window.addEventListener('beforeprint',()=>{if(printState)return;printState={pages:pages.map(p=>p.hidden),details:[...document.querySelectorAll('details')].map(d=>[d,d.open])};pages.forEach(p=>p.hidden=false);printState.details.forEach(([d])=>d.open=true);});\n"
        " window.addEventListener('afterprint',()=>{if(!printState)return;pages.forEach((p,i)=>p.hidden=printState.pages[i]);printState.details.forEach(([d,open])=>d.open=open);printState=null;});\n"
        '})();\n'
        '(()=>{\n'
        " const dialog=document.getElementById('es-dialog');\n"
        " if(!dialog||typeof dialog.showModal!=='function')return;\n"
        " const title=dialog.querySelector('#es-dialog-title'),body=dialog.querySelector('.es-dialog-body');\n"
        " document.addEventListener('click',e=>{\n"
        "  const summary=e.target.closest('.es-entry>summary,.card>summary');\n"
        "  if(summary&&!summary.closest('dialog')){e.preventDefault();const entry=summary.parentElement;title.textContent=entry.dataset.esTitle;body.replaceChildren(entry.querySelector('.es-detail').cloneNode(true));dialog.showModal();return;}\n"
        "  const cell=e.target.closest('a.cell');if(cell&&!cell.closest('dialog')){e.preventDefault();e.stopPropagation();title.textContent=cell.dataset.esTitle;body.replaceChildren(cell.nextElementSibling.content.cloneNode(true));dialog.showModal();return;}\n"
        '  if(e.target.closest(\'a[href^="#"]\')){if(dialog.open)dialog.close();}\n'
        ' },true);\n'
        " dialog.querySelector('.es-dialog-close').addEventListener('click',()=>dialog.close());\n"
        " dialog.addEventListener('click',e=>{if(e.target!==dialog)return;const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();});\n"
        " dialog.addEventListener('close',()=>body.replaceChildren());\n"
        " window.addEventListener('beforeprint',()=>{if(dialog.open)dialog.close();});\n"
        '})();\n'
        '\n'
        '(()=>{\n'
        " const input=document.getElementById('source-search-input');\n"
        " input?.addEventListener('input',()=>{const q=input.value.trim().toLocaleLowerCase();document.querySelectorAll('#page-sources .claim-detail').forEach(row=>row.hidden=Boolean(q&&!row.textContent.toLocaleLowerCase().includes(q)));});\n"
        " const tabs=document.querySelector('.tabs');tabs.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;const buttons=[...tabs.querySelectorAll('button')],i=buttons.indexOf(document.activeElement);if(i<0)return;e.preventDefault();const n=e.key==='Home'?0:e.key==='End'?buttons.length-1:(i+(e.key==='ArrowRight'?1:-1)+buttons.length)%buttons.length;buttons[n].click();buttons[n].focus();});\n"
        '})();\n'
        '</script></body></html>\n'
    ),
    'capability.css': (
        '#briefing-capability-matrix{--cm-ink:#193445;--cm-muted:#526a79;--cm-brand:#154c61;--cm-accent:#aa7629;--cm-line:#dce5ea;color:var(--cm-ink);font:14px/1.5 Arial,Helvetica,sans-serif;min-width:0}\n'
        '#briefing-capability-matrix [hidden]{display:none!important}\n'
        '#briefing-capability-matrix .cm-scroll{overflow-x:auto;max-width:100%;margin:8px 0}\n'
        '#briefing-capability-matrix .cm-matrix{width:100%;min-width:var(--cm-table-width,930px);table-layout:fixed;border-collapse:separate;border-spacing:5px}\n'
        '#briefing-capability-matrix .cm-matrix th,#briefing-capability-matrix .cm-matrix td{min-width:0;border:0;padding:0;vertical-align:top}\n'
        '#briefing-capability-matrix .cm-matrix thead th{padding:0 2px 8px;text-align:left;vertical-align:bottom;background:white}\n'
        '#briefing-capability-matrix .cm-matrix th:first-child{position:sticky;left:0;width:172px;z-index:1;background:#eef3f7}\n'
        '#briefing-capability-matrix .cm-matrix thead th:first-child{background:white;padding:10px;font-size:13px}\n'
        '#briefing-capability-matrix .cm-column{border:0;background:none;display:block;width:100%;padding:0;color:var(--cm-brand);font-size:13px;font-weight:700;text-align:left;min-height:52px;overflow-wrap:anywhere}\n'
        '#briefing-capability-matrix .cm-column small{color:var(--cm-muted);font-size:11px;font-weight:400;margin-top:3px}\n'
        '#briefing-capability-matrix .cm-column[disabled]{opacity:1;color:var(--cm-brand);cursor:default}\n'
        '#briefing-capability-matrix .cm-column[disabled] .cm-arrow{display:none}\n'
        '#briefing-capability-matrix .cm-column[aria-pressed=true]{color:var(--cm-accent)}\n'
        '#briefing-capability-matrix .cm-matrix tbody th{background:#eef3f7;border-radius:6px;text-align:left;padding:13px 12px;vertical-align:middle}\n'
        '#briefing-capability-matrix .cm-actor{font-size:14px;line-height:1.3;display:block;font-weight:700;overflow-wrap:anywhere}\n'
        '#briefing-capability-matrix .cm-system{color:var(--cm-muted);font-size:11px;line-height:1.4;font-weight:400;margin-top:6px;overflow-wrap:anywhere}\n'
        '#briefing-capability-matrix .cm-reference th{border-left:4px solid var(--cm-brand)}\n'
        '#briefing-capability-matrix .cm-reference-label{display:block;color:var(--cm-brand);font-size:11px;font-weight:700;letter-spacing:.2px;text-transform:uppercase;margin-top:8px}\n'
        '#briefing-capability-matrix .cm-cell{width:100%;min-height:136px;height:var(--cm-cell-height,auto);border:1px solid transparent;border-radius:6px;padding:11px 10px;display:flex;flex-direction:column;align-items:flex-start;text-align:left;text-decoration:none;background:#eef3f7;color:var(--cm-ink);overflow-wrap:anywhere}\n'
        '#briefing-capability-matrix .cm-cell:hover{outline:2px solid var(--cm-brand);outline-offset:0}\n'
        '#briefing-capability-matrix .cm-cell[aria-pressed=true]{outline:2px solid var(--cm-accent);outline-offset:0}\n'
        '#briefing-capability-matrix .cm-s1{background:#f2f4f6}\n'
        '#briefing-capability-matrix .cm-s2{background:#e7eff4}\n'
        '#briefing-capability-matrix .cm-s3{background:#d6e8ed}\n'
        '#briefing-capability-matrix .cm-s4{background:#b8dbe0}\n'
        '#briefing-capability-matrix .cm-s5{background:#236775;color:white}\n'
        '#briefing-capability-matrix .cm-missing{background:#f2f4f6;background-image:repeating-linear-gradient(135deg,transparent,transparent 8px,#526a7912 8px,#526a7912 9px)}\n'
        '#briefing-capability-matrix .cm-na{background:#f2f4f6;color:#526a79}\n'
        '#briefing-capability-matrix .cm-cell-top{display:flex;align-items:center;justify-content:space-between;gap:4px;width:100%;margin-bottom:5px;flex-wrap:wrap}\n'
        '#briefing-capability-matrix .cm-score{font-size:23px;line-height:1.1;font-weight:700;white-space:nowrap;font-variant-numeric:tabular-nums}\n'
        '#briefing-capability-matrix .cm-score small{display:inline;color:inherit;font-size:12px;font-weight:400}\n'
        '#briefing-capability-matrix .cm-kind{font-size:11px;letter-spacing:.3px;text-transform:uppercase;font-weight:700;opacity:.8}\n'
        '#briefing-capability-matrix .cm-count{font-size:11px;white-space:nowrap;opacity:.85}\n'
        '#briefing-capability-matrix .cm-cell-title{font-size:13px;line-height:1.35;font-weight:700;display:block}\n'
        '#briefing-capability-matrix .cm-cell-preview{font-size:12px;line-height:1.35;margin-top:5px;display:block}\n'
        '#briefing-capability-matrix .cm-legend{display:flex;gap:10px 16px;flex-wrap:wrap;align-items:center;font-size:11px;color:var(--cm-muted);padding:13px 5px 10px}\n'
        '#briefing-capability-matrix .cm-legend>span{display:inline-flex;gap:6px;align-items:center}\n'
        '#briefing-capability-matrix .cm-legend i{width:12px;height:12px;border-radius:2px;display:inline-block;flex:none}\n'
        '#briefing-capability-matrix .cm-key-evidence{background:#236775}\n'
        '#briefing-capability-matrix .cm-key-profile{background:#eef3f7}\n'
        '#briefing-capability-matrix .cm-key-missing{background:#f2f4f6;border:1px dashed var(--cm-muted)}\n'
        '#briefing-capability-matrix .cm-method{font-size:12px;color:var(--cm-muted);border-top:1px solid var(--cm-line);padding:11px 5px 0}\n'
        '#briefing-capability-matrix .cm-method>summary{color:var(--cm-brand);font-weight:600}\n'
        '#briefing-capability-matrix .cm-method-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:15px 22px;margin-top:14px}\n'
        '#briefing-capability-matrix .cm-method h4{color:var(--cm-ink);margin:0 0 8px;font-size:13px}\n'
        '#briefing-capability-matrix .cm-method dl{display:grid;grid-template-columns:30px 1fr;gap:5px;margin:8px 0}\n'
        '#briefing-capability-matrix .cm-method dt{font-weight:700}\n'
        '#briefing-capability-matrix .cm-method dd{margin:0}\n'
        '#briefing-capability-matrix .cm-detail{margin-top:18px;border-top:3px solid var(--cm-brand);padding-top:20px;scroll-margin-top:85px}\n'
        '#briefing-capability-matrix .cm-detail-head{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-bottom:18px}\n'
        '#briefing-capability-matrix .cm-kicker{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:var(--cm-muted);margin-bottom:5px}\n'
        '#briefing-capability-matrix .cm-detail h3{font-size:19px;line-height:1.3;margin:0}\n'
        '#briefing-capability-matrix .cm-action{background:white;border:1px solid var(--cm-line);padding:7px 11px;border-radius:5px;font-size:12px;max-width:100%;overflow-wrap:anywhere}\n'
        '#briefing-capability-matrix .cm-detail-grid{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:22px}\n'
        '#briefing-capability-matrix .cm-discussion:only-child{grid-column:1/-1}\n'
        '#briefing-capability-matrix .cm-record-body p{margin:8px 0 14px;font-size:13px;line-height:1.6}\n'
        '#briefing-capability-matrix .cm-record-body h4{font-size:13px;margin:20px 0 7px;color:var(--cm-brand)}\n'
        '#briefing-capability-matrix .cm-full-value{font-size:16px!important;font-weight:700;margin:0 0 14px!important}\n'
        '#briefing-capability-matrix .cm-outcome-grade{display:block;font-size:12px;font-weight:700;color:var(--cm-brand);margin-bottom:7px;font-variant-numeric:tabular-nums}\n'
        '#briefing-capability-matrix .cm-limits{background:#faf5ec;border-left:3px solid var(--cm-accent);padding:13px 16px;border-radius:4px;align-self:start}\n'
        '#briefing-capability-matrix .cm-limits h4:first-child{margin:0 0 7px;color:var(--cm-ink)}\n'
        '#briefing-capability-matrix .cm-limits p:last-child{margin-bottom:0}\n'
        '#briefing-capability-matrix .cm-facts{margin-top:15px;border-top:1px solid var(--cm-line);padding-top:15px}\n'
        '#briefing-capability-matrix .cm-fact{border-bottom:1px solid var(--cm-line);padding:13px 0}\n'
        '#briefing-capability-matrix .cm-fact>summary{font-size:13px;font-weight:700;line-height:1.55}\n'
        '#briefing-capability-matrix .cm-fact .evidence{margin:12px 0;padding-left:20px}\n'
        '#briefing-capability-matrix .cm-fact .evidence li{padding:10px 12px;margin:10px 0;background:#f5f8fa;border-left:2px solid var(--cm-line)}\n'
        '#briefing-capability-matrix .cm-fact .evidence a{color:var(--cm-brand);font-size:12px;font-weight:700}\n'
        '#briefing-capability-matrix .cm-fact .evidence p{font-size:12px;margin:7px 0}\n'
        '#briefing-capability-matrix .cm-record{border-bottom:1px solid var(--cm-line);padding:14px 0;scroll-margin-top:85px}\n'
        '#briefing-capability-matrix .cm-record>summary{font-weight:700;color:var(--cm-brand)}\n'
        '#briefing-capability-matrix .cm-record>.cm-record-body{padding-top:15px}\n'
        '#briefing-capability-matrix.cm-enhanced .cm-fallback{display:none}\n'
        '#briefing-capability-matrix .cm-comparison{border-collapse:collapse;width:100%;table-layout:fixed;min-width:760px}\n'
        '#briefing-capability-matrix .cm-comparison th{background:#eef3f7;font-size:12px;padding:11px;text-align:left;vertical-align:top;min-width:0}\n'
        '#briefing-capability-matrix .cm-comparison td{padding:16px 11px;border-bottom:1px solid var(--cm-line);vertical-align:top;font-size:13px;line-height:1.6;min-width:0;overflow-wrap:anywhere}\n'
        '#briefing-capability-matrix .cm-comparison th:first-child{width:18%}\n'
        '#briefing-capability-matrix .cm-comparison th:nth-child(2){width:23%}\n'
        '#briefing-capability-matrix .cm-comparison th:nth-child(3){width:59%}\n'
        '#briefing-capability-matrix .cm-compare-company{font-weight:700;font-size:14px;line-height:1.4}\n'
        '#briefing-capability-matrix .cm-comparison .cm-detail-grid{display:block}\n'
        '#briefing-capability-matrix .cm-comparison .cm-limits{margin-top:12px}\n'
        '#briefing-capability-matrix .cm-comparison .cm-full-value{font-size:13px!important;font-weight:400}\n'
        '#briefing-capability-matrix .cm-compare-facts{margin-top:10px}\n'
        '#briefing-capability-matrix .cm-compare-facts>summary{color:var(--cm-brand);font-weight:700;font-size:12px}\n'
        '@media print{\n'
        ' #briefing-capability-matrix .cm-scroll{overflow:visible}\n'
        ' #briefing-capability-matrix .cm-matrix{min-width:0!important;table-layout:auto;border-spacing:3px}\n'
        ' #briefing-capability-matrix .cm-matrix th:first-child{position:static;width:auto}\n'
        ' #briefing-capability-matrix .cm-column{min-height:0}\n'
        ' #briefing-capability-matrix .cm-arrow,#briefing-capability-matrix .cm-detail{display:none!important}\n'
        ' #briefing-capability-matrix .cm-cell{height:auto!important;min-height:0;padding:7px;print-color-adjust:exact;-webkit-print-color-adjust:exact}\n'
        ' #briefing-capability-matrix.cm-enhanced .cm-fallback{display:block!important}\n'
        ' #briefing-capability-matrix .cm-detail-grid{display:block}\n'
        ' #briefing-capability-matrix .cm-record{break-before:auto}\n'
        ' #briefing-capability-matrix .cm-limits{margin-top:12px}\n'
        '}\n'
    ),
    'capability.js': (
        '(()=>{\n'
        " const root=document.getElementById('briefing-capability-matrix');\n"
        ' if(!root)return;\n'
        " const cells=[...root.querySelectorAll('.cm-cell')],columns=[...root.querySelectorAll('.cm-column')],\n"
        "       records=new Map([...root.querySelectorAll('.cm-record')].map(n=>[n.id,n])),detail=root.querySelector('.cm-detail');\n"
        ' if(!cells.length||cells.some(c=>!records.has(c.dataset.cmRecord)))return;\n'
        ' // Keep the static evaluations in the document for sources, print and no-JS use.\n'
        ' let active=null,compare=false;\n'
        ' function el(tag,parent,text,cls){const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;if(parent)parent.appendChild(n);return n;}\n'
        " function copyBody(cell){return records.get(cell.dataset.cmRecord).querySelector('.cm-record-body').cloneNode(true);}\n"
        ' function pick(cell,all=false){\n'
        '  active=cell;compare=all;const record=records.get(cell.dataset.cmRecord),col=cell.dataset.cmCol;\n'
        '  detail.hidden=false;detail.replaceChildren();\n'
        "  const head=el('div',detail,undefined,'cm-detail-head'),title=el('div',head);\n"
        "  el('span',title,compare?'Vergleich nach gemeinsamem Kriterium':'Bewertung im Detail','cm-kicker');\n"
        "  const criterion=columns[+col].querySelector('span').firstChild.textContent.trim();\n"
        "  el('h3',title,compare?criterion:record.dataset.cmName+' · '+criterion);\n"
        "  if(!compare&&record.dataset.cmOffer)el('small',title,record.dataset.cmOffer,'cm-system');\n"
        "  const button=el('button',head,compare?'Einzelbewertung öffnen':'Alle Wettbewerber vergleichen','cm-action');button.type='button';button.addEventListener('click',()=>pick(active,!compare));\n"
        "  cells.forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.cmCol===col&&(compare||c===cell))));\n"
        "  columns.forEach((b,i)=>b.setAttribute('aria-pressed',String(compare&&String(i)===col)));\n"
        '  if(!compare){detail.appendChild(copyBody(cell));return;}\n'
        "  const scroll=el('div',detail,undefined,'cm-scroll'),table=el('table',scroll,undefined,'cm-comparison');\n"
        "  table.setAttribute('aria-label',columns[+col].getAttribute('aria-label'));\n"
        "  const headings=el('tr',el('thead',table));['Unternehmen','Öffentlicher Nachweis','Einordnung, Grenzen & Quellen'].forEach(text=>el('th',headings,text));\n"
        "  const tbody=el('tbody',table);\n"
        '  cells.filter(c=>c.dataset.cmCol===col).forEach(c=>{\n'
        "   const r=records.get(c.dataset.cmRecord),tr=el('tr',tbody),actor=el('td',tr),select=el('button',actor,r.dataset.cmName,'cm-action cm-compare-company');select.type='button';select.addEventListener('click',()=>pick(c));\n"
        "   if(r.dataset.cmOffer)el('small',actor,r.dataset.cmOffer,'cm-system');\n"
        "   if(c.closest('.cm-reference'))el('span',actor,'Referenz','cm-reference-label');\n"
        "   const copy=copyBody(c),outcome=copy.querySelector('.cm-outcome');el('td',tr).appendChild(outcome);const context=el('td',tr);\n"
        "   const facts=copy.querySelector('.cm-facts');facts.remove();context.appendChild(copy);\n"
        "   const disclosure=el('details',context,undefined,'cm-compare-facts'),count=Number(r.dataset.cmSourceCount);\n"
        "   el('summary',disclosure,'Faktenbasis'+(count?' · '+count+(count===1?' Quelle':' Quellen'):''));disclosure.appendChild(facts);\n"
        '  });\n'
        ' }\n'
        " root.addEventListener('click',event=>{\n"
        "  const cell=event.target.closest('.cm-cell');if(!cell||!root.contains(cell))return;\n"
        '  event.preventDefault();event.stopPropagation();pick(cell);\n'
        ' });\n'
        " cells.forEach(cell=>cell.setAttribute('role','button'));\n"
        " root.addEventListener('keydown',event=>{const cell=event.target.closest('.cm-cell');if(cell&&event.key===' '){event.preventDefault();pick(cell);}});\n"
        " columns.forEach((b,i)=>{b.disabled=false;b.addEventListener('click',()=>pick(cells.find(c=>c.dataset.cmCol===String(i)&&c.dataset.cmRow===active.dataset.cmRow),true));});\n"
        " root.style.setProperty('--cm-table-width',Math.max(760,172+columns.length*155)+'px');\n"
        " const reference=cells.filter(c=>c.closest('.cm-reference')),initial=reference[0]||cells[0];\n"
        " pick(initial);root.classList.add('cm-enhanced');\n"
        ' // Measure complete text at the available column width; never clamp the summaries.\n'
        ' let lastWidth=0;\n'
        " function fit(){const width=root.querySelector('.cm-matrix').getBoundingClientRect().width;if(Math.abs(width-lastWidth)<1)return;lastWidth=width;root.style.removeProperty('--cm-cell-height');const height=Math.ceil(Math.max(136,...cells.map(c=>c.getBoundingClientRect().height)));root.style.setProperty('--cm-cell-height',height+'px');}\n"
        " fit();if(typeof ResizeObserver!=='undefined')new ResizeObserver(fit).observe(root.querySelector('.cm-scroll'));\n"
        '})();\n'
    ),
    'cluster-network.html': (
        '<!-- Datensatz und Akteurstabellen werden je Auftrag aus geprüften Daten eingesetzt. -->\n'
        '<section id="briefing-company-network" aria-label="Unternehmensnetzwerk">\n'
        '  <div class="cnt-heading"><h3>Unternehmensnetzwerk</h3><div class="cnt-tabs" role="tablist" aria-label="Ansicht der Clusteranalyse"><button type="button" role="tab" id="cnt-tab-tables" aria-selected="true" aria-controls="cnt-view-tables">Tabellen</button><button type="button" role="tab" id="cnt-tab-graph" aria-selected="false" aria-controls="cnt-view-graph" tabindex="-1">Grafik</button></div></div>\n'
        '__CLUSTER_ACTOR_TABLES__<div id="cnt-view-graph" role="tabpanel" aria-labelledby="cnt-tab-graph" tabindex="0" hidden>\n'
        '  <div class="cn-filters" aria-label="Beziehungen filtern"></div>\n'
        '  <label class="cn-product-label">Produktbezug <select class="cn-product"><option value="all">Alle Produkte</option></select></label>\n'
        '  <div class="cn-toolbar"><label>Suche <input type="search" class="cn-search" placeholder="Akteur oder Beziehung"></label><label>Status <select class="cn-status"><option value="all">Alle Status</option></select></label><label><input type="checkbox" class="cn-cross"> Querverbindungen</label><button type="button" class="cn-expand">Alle Cluster aufklappen</button><button type="button" class="cn-reset">Zurücksetzen</button></div>\n'
        '  <div class="cn-grid"><div class="cn-board"><div class="cn-clusters"></div><div class="cn-plot"><svg class="cn-svg" role="img" aria-label="Unternehmensnetzwerk mit dem Zielunternehmen im Zentrum"></svg></div>\n'
        '  <div class="cn-legend" aria-label="Farben und Formen der Akteurstypen"></div>\n'
        '  <div class="cn-count" aria-live="polite"></div>\n'
        '  <details class="cn-access"><summary>Verbindungen per Tastatur auswählen</summary><div class="cn-keyboard"></div></details></div><aside class="cn-sidebar" aria-labelledby="network-panel-title"><div class="cn-details" aria-live="polite"><div class="cn-detail-head"><h4 id="network-panel-title"></h4><button type="button" class="cn-close">Zurücksetzen</button></div><div class="cn-detail-content"></div></div></aside></div>\n'
        '  <p class="cn-error" hidden role="alert"></p>\n'
        '  <details class="cn-table"><summary>Beziehungen und Originalquellen</summary><div class="cn-table-wrap"><table><thead><tr><th>Von → Zu</th><th>Beziehung</th><th>Status</th><th>Originalquellen</th></tr></thead><tbody></tbody></table></div></details>\n'
        '  </div>\n'
        '  <script type="application/json" class="cn-data">__CLUSTER_NETWORK_JSON__</script>\n'
        '</section>\n'
        '<noscript><style>#briefing-company-network .cnt-tabs,#briefing-company-network .cnt-tools{display:none!important}#briefing-company-network #cnt-view-graph[hidden]{display:block!important}</style></noscript>\n'
        '<style>\n'
        '#briefing-company-network{--cn-fg:light-dark(#20252d,#edf0f5);--cn-bg:light-dark(#fff,#15181e);--cn-muted:light-dark(#636b77,#aab3c1);--cn-line:light-dark(#bcc3cd,#626c7b);--cn-ring:light-dark(#2563eb,#86b0ff);--cn-target:light-dark(#273447,#e0e8f4);--cn-target-text:light-dark(#fff,#182335);color-scheme:light dark;color:var(--cn-fg);width:100%}\n'
        '#briefing-company-network .cn-filters,#briefing-company-network .cn-legend{display:flex;flex-wrap:wrap;gap:8px 16px}\n'
        '#briefing-company-network .cn-filters label,#briefing-company-network .cn-legend span{display:inline-flex;gap:6px;align-items:center}\n'
        '#briefing-company-network .cn-product-label{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:12px 0}\n'
        '#briefing-company-network button,#briefing-company-network select{font:inherit;color:var(--cn-fg);background:var(--cn-bg);border:1px solid var(--cn-line);border-radius:6px;padding:6px 9px}\n'
        '#briefing-company-network .cn-dot{width:10px;height:10px;border-radius:50%;display:inline-block;flex-shrink:0}\n'
        '#briefing-company-network .cn-plot{position:relative;width:100%}\n'
        '#briefing-company-network .cn-svg{display:block;width:100%}\n'
        '#briefing-company-network .cn-keyboard{position:absolute;inset:0;pointer-events:none}\n'
        '#briefing-company-network .cn-key{position:absolute;width:32px;height:32px;transform:translate(-50%,-50%);border:0;background:transparent;padding:0;pointer-events:none}\n'
        '#briefing-company-network .cn-key:focus-visible{outline:2px solid var(--cn-ring);background:var(--cn-bg)}\n'
        '#briefing-company-network .cn-line{stroke:var(--cn-line);stroke-width:1.5;fill:none}\n'
        '#briefing-company-network .cn-line-selected{stroke:var(--cn-fg);stroke-width:2.5}\n'
        '#briefing-company-network .cn-hit{stroke:transparent;stroke-width:24;fill:none;pointer-events:stroke;cursor:pointer}\n'
        '#briefing-company-network .cn-svg text{font:12px sans-serif;fill:var(--cn-fg)}\n'
        '#briefing-company-network .cn-node-label{paint-order:stroke;stroke:var(--cn-bg);stroke-width:5px;stroke-linejoin:round}\n'
        '#briefing-company-network .cn-count{color:var(--cn-muted);margin:10px 0;font-size:12px}\n'
        '#briefing-company-network .cn-detail-head{display:flex;gap:12px;align-items:center;justify-content:space-between}\n'
        '#briefing-company-network .cn-detail-head h4{margin:0}\n'
        '#briefing-company-network .cn-details{border-top:1px solid var(--cn-line);padding:14px 0}\n'
        '#briefing-company-network .cn-details p{margin:8px 0;overflow-wrap:anywhere}\n'
        '#briefing-company-network a{color:var(--cn-ring);overflow-wrap:anywhere}\n'
        '#briefing-company-network .cn-table-wrap{overflow-x:auto}\n'
        '#briefing-company-network table{width:100%;border-collapse:collapse;font-size:13px}\n'
        '#briefing-company-network th,#briefing-company-network td{padding:8px;text-align:left;vertical-align:top;border-bottom:1px solid var(--cn-line);overflow-wrap:anywhere}\n'
        '#briefing-company-network .cn-error{color:var(--cn-fg)}\n'
        '@media(pointer:coarse){#briefing-company-network .cn-hit{stroke-width:36}#briefing-company-network button,#briefing-company-network select{min-height:44px}}\n'
        '@media print{#briefing-company-network .cn-filters,#briefing-company-network .cn-product-label,#briefing-company-network .cn-close,#briefing-company-network .cn-keyboard{display:none}#briefing-company-network .cn-table{display:block}#briefing-company-network .cn-table-wrap{overflow:visible}#briefing-company-network .cn-table summary{display:none}#briefing-company-network .cn-table>*:not(summary){display:block!important}#briefing-company-network .cn-svg{break-inside:avoid}}\n'
        '\n'
        '#briefing-company-network{--cn-soft:light-dark(#f5f8fa,#202833)}\n'
        '#briefing-company-network .cn-grid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:16px;align-items:start}\n'
        '#briefing-company-network .cn-board{border:1px solid var(--cn-line);border-radius:8px;min-width:0;background:var(--cn-bg)}\n'
        '#briefing-company-network .cn-toolbar,#briefing-company-network .cn-clusters{display:flex;gap:8px;flex-wrap:wrap;align-items:center;padding:10px 0}\n'
        '#briefing-company-network .cn-toolbar label{display:flex;gap:6px;align-items:center;flex-wrap:wrap}\n'
        '#briefing-company-network .cn-toolbar input,#briefing-company-network .cn-toolbar select{font:inherit;color:var(--cn-fg);background:var(--cn-bg);max-width:100%}\n'
        '#briefing-company-network .cn-clusters{padding:10px;border-bottom:1px solid var(--cn-line)}\n'
        '#briefing-company-network .cn-clusters button[aria-pressed=true]{background:var(--cn-target);color:var(--cn-target-text)}\n'
        '#briefing-company-network .cn-plot{overflow-x:auto}#briefing-company-network .cn-keyboard{position:static;pointer-events:auto}\n'
        '#briefing-company-network .cn-edge-button{margin:4px;text-align:left}#briefing-company-network .cn-node{cursor:pointer}\n'
        '#briefing-company-network .cn-node:focus-visible{outline:3px solid var(--cn-ring)}\n'
        '#briefing-company-network .cn-line{opacity:.35}#briefing-company-network .cn-line-selected{opacity:1}\n'
        '#briefing-company-network .cn-svg .cn-cluster-title{font-size:16px;font-weight:600}\n'
        '#briefing-company-network .cn-details{border:1px solid var(--cn-line);border-radius:8px;padding:16px;background:var(--cn-bg);min-width:0}\n'
        '#briefing-company-network .cn-relation{display:block;width:100%;text-align:left;margin-top:8px}\n'
        '#briefing-company-network .cn-count,#briefing-company-network .cn-legend,#briefing-company-network .cn-access{padding:8px 12px}\n'
        '@media print{#briefing-company-network .cn-grid{display:block}#briefing-company-network .cn-toolbar,#briefing-company-network .cn-clusters,#briefing-company-network .cn-details,#briefing-company-network .cn-access{display:none!important}#briefing-company-network .cn-plot{overflow:visible}}\n'
        '#briefing-company-network{--cn-fg:#193445;--cn-bg:#fff;--cn-muted:#647b88;--cn-line:#cedde5;--cn-ring:#c3872d;--cn-target:#154c61;--cn-target-text:#fff;--cn-soft:#f8fafb;color-scheme:light}#briefing-company-network .cn-board{border-color:#dce6eb;border-radius:10px}#briefing-company-network .cn-filters{gap:7px;margin:12px 0}#briefing-company-network .cn-filters label{font-size:11px;border:1px solid #d9e5eb;border-radius:6px;padding:6px 9px;background:#f4f8fa;gap:6px}#briefing-company-network .cn-filters label:has(input:not(:checked)){background:#fff;color:#93a4ae}#briefing-company-network .cn-filters input{accent-color:#154c61}#briefing-company-network .cn-toolbar{padding:0;gap:12px}#briefing-company-network .cn-toolbar label{font-size:11px}#briefing-company-network input.cn-search{border:1px solid #cedee6;border-radius:6px;padding:7px 9px;width:230px}#briefing-company-network .cn-toolbar select{max-width:270px}#briefing-company-network button,#briefing-company-network select{font-size:11px;border-color:#cedee6;padding:7px 10px}#briefing-company-network .cn-product-label{font-size:11px;margin:0}#briefing-company-network .cn-product{max-width:330px}.network-tools{border:1px solid #e1e9ee;border-radius:8px;padding:10px 13px;margin-bottom:12px;background:#fbfcfd}.network-tools>summary{font-size:11px;font-weight:600;color:var(--teal)}.network-tools[open]>summary{margin-bottom:12px}.network-tools .cn-product-label{margin-bottom:10px!important}#briefing-company-network .cn-clusters{gap:7px;padding:10px}#briefing-company-network .cn-clusters button{background:#fff;font-size:10px}#briefing-company-network .cn-plot{padding:0 5px;background:#fff}#briefing-company-network .cn-svg text{font-family:inherit;font-size:11px}#briefing-company-network .cn-svg .cn-cluster-title{font-size:12px;font-weight:700}#briefing-company-network .cn-line{stroke:#b6cbd6;stroke-width:1.25;opacity:.65}#briefing-company-network .cn-line-selected{stroke:#154c61;stroke-width:2.8;opacity:1}#briefing-company-network .cn-svg.has-selection .cn-line:not(.cn-line-selected){opacity:.16}#briefing-company-network .cn-node:hover rect{stroke:#c3872d;stroke-width:2}#briefing-company-network .cn-node-label{stroke-width:0}#briefing-company-network .cn-legend{padding:12px 15px 7px;gap:7px 15px;font-size:10px;border-top:1px solid #e1e9ee}#briefing-company-network .cn-count{font-size:10px;padding:6px 15px 10px;color:#607180}#briefing-company-network .cn-access{font-size:11px;padding:0 15px 12px}#briefing-company-network .cn-table{font-size:11px;margin-top:15px}#briefing-company-network .cn-table td{font-size:11px}\n'
        '\n'
        '#briefing-company-network .cn-grid{display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:18px;align-items:start}\n'
        '#briefing-company-network .cn-sidebar{position:sticky;top:82px;min-width:0}\n'
        '#briefing-company-network .cn-details{padding:0;border:1px solid #dce6eb;border-radius:10px;overflow:hidden;background:#fff}\n'
        '#briefing-company-network .cn-detail-head{padding:18px 17px;background:#f4f8fa;border-bottom:1px solid #dce6eb;align-items:flex-start}\n'
        '#briefing-company-network .cn-detail-head h4{font-size:16px;line-height:1.4;overflow-wrap:anywhere}\n'
        '#briefing-company-network .cn-detail-head button{font-size:10px;padding:5px 7px;flex-shrink:0}\n'
        '#briefing-company-network .cn-detail-content{padding:12px 18px 22px;min-height:230px;max-height:calc(100vh - 205px);overflow-y:auto;font-size:12px;line-height:1.65}\n'
        '#briefing-company-network .cn-detail-content a{color:#176274}\n'
        '#briefing-company-network .cn-detail-content p+p{margin-top:13px}\n'
        '#briefing-company-network .cn-detail-content .cn-relation{font-size:11px;line-height:1.5;padding:10px 12px}\n'
        '#briefing-company-network .cn-line-cross{stroke:#176274;opacity:.8;stroke-width:1.7}\n'
        '#briefing-company-network .cn-line-selected{stroke:#c3872d;opacity:1;stroke-width:2.4}\n'
        '@media print{#briefing-company-network .cn-grid{display:block}#briefing-company-network .cn-sidebar{display:none}}\n'
        '\n'
        '#briefing-company-network .cn-svg{touch-action:auto}#briefing-company-network .cn-plot{overflow:auto;overscroll-behavior:auto}#briefing-company-network .cn-kind-icon{flex:none;overflow:visible}#briefing-company-network .cn-node-label{paint-order:stroke;stroke:white;stroke-width:3px;pointer-events:none}#briefing-company-network .cn-target-label{pointer-events:none}#briefing-company-network .cn-node:hover .cn-symbol,#briefing-company-network .cn-node:focus-visible .cn-symbol{stroke:#c3872d;stroke-width:4}#briefing-company-network .cn-svg .cn-cluster-title{font-size:14px}#briefing-company-network .cn-svg.has-selection .cn-line:not(.cn-line-selected){opacity:.2}#briefing-company-network .cn-line{stroke:var(--cn-edge-color,#466372);opacity:.4;stroke-width:1.4}#briefing-company-network .cn-line-cross{opacity:.55}#briefing-company-network .cn-line-selected{stroke:#c3872d;opacity:1;stroke-width:2.7}\n'
        '\n'
        '/* Zwei lokale Ansichten der Clusteranalyse. */\n'
        '#briefing-company-network [hidden]{display:none!important}\n'
        '#briefing-company-network .cnt-heading{display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;margin-bottom:18px}\n'
        '#briefing-company-network .cnt-heading h3{margin:0}\n'
        '#briefing-company-network .cnt-tabs{display:flex;gap:4px;padding:4px;border:1px solid #c9d5df;border-radius:10px;background:#edf2f6}\n'
        '#briefing-company-network .cnt-tabs button{border:0;border-radius:7px;background:transparent;color:#36536a;padding:9px 20px;font:inherit;font-weight:650;cursor:pointer}\n'
        '#briefing-company-network .cnt-tabs button[aria-selected="true"]{background:#163047;color:white;box-shadow:0 2px 5px #16304722}\n'
        '#briefing-company-network .cnt-tools{display:flex;align-items:end;gap:12px;flex-wrap:wrap;padding:16px;border:1px solid #d7e1e8;border-radius:10px;background:#f6f8fa}\n'
        '#briefing-company-network .cnt-tools label{display:grid;gap:5px;font-size:13px;color:#36536a}\n'
        '#briefing-company-network .cnt-tools input[type="search"],#briefing-company-network .cnt-tools select{font:inherit;padding:9px 10px;border:1px solid #b6c8d5;border-radius:6px;background:white;min-height:40px;max-width:100%}\n'
        '#briefing-company-network .cnt-tools .cnt-direct-label{display:flex;align-items:center;gap:7px;min-height:40px}\n'
        '#briefing-company-network .cnt-reset{font:inherit;border:1px solid #b6c8d5;border-radius:6px;background:white;padding:9px 12px;min-height:40px;cursor:pointer}\n'
        '#briefing-company-network .cnt-count{font-size:13px;color:#52697a;margin:12px 0 20px}\n'
        '#briefing-company-network .cnt-group{margin:22px 0 28px}\n'
        '#briefing-company-network .cnt-group h4{font-size:17px;margin:0 0 12px;color:#163047}\n'
        '#briefing-company-network .cnt-table-scroll{overflow-x:auto;border:1px solid #d7e1e8;border-radius:9px}\n'
        '#briefing-company-network .cnt-group table{width:100%;border-collapse:collapse;table-layout:fixed;margin:0;font-size:13px}\n'
        '#briefing-company-network .cnt-group th{background:#edf2f6;text-align:left;color:#254358;padding:12px;vertical-align:top}\n'
        '#briefing-company-network .cnt-group td{padding:12px;vertical-align:top;border-top:1px solid #e1e8ee;overflow-wrap:anywhere;line-height:1.5}\n'
        '#briefing-company-network .cnt-group th:nth-child(1),#briefing-company-network .cnt-group th:nth-child(2){width:18%}\n'
        '#briefing-company-network .cnt-group th:nth-child(3){width:23%}\n'
        '#briefing-company-network .cnt-group th:nth-child(4){width:16%}\n'
        '#briefing-company-network .cnt-group details{margin:0;background:transparent;border:0;padding:0}\n'
        '#briefing-company-network .cnt-group summary{cursor:pointer;color:#235d83;font-weight:650}\n'
        '#briefing-company-network .cnt-group details p{font-size:12px;line-height:1.55;margin:10px 0}\n'
        '#briefing-company-network .cnt-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}\n'
        '#briefing-company-network .cnt-tabs button:focus-visible,#briefing-company-network .cnt-tools :focus-visible{outline:3px solid #c3872d;outline-offset:3px}\n'
        '@media(max-width:700px){#briefing-company-network .cnt-heading{align-items:flex-start}#briefing-company-network .cnt-group table{min-width:700px}#briefing-company-network .cnt-tools>label{max-width:100%}}\n'
        '@media print{#briefing-company-network .cnt-tabs,#briefing-company-network #cnt-view-tables{display:none!important}#briefing-company-network #cnt-view-graph[hidden]{display:block!important}}\n'
        '\n'
        '/* Kompakte, farbcodierte Beziehungsliste mit Details auf Klick. */\n'
        '#briefing-company-network .cnt-group{margin:24px 0}\n'
        '#briefing-company-network .cnt-group h4{font-size:15px;letter-spacing:.015em;margin:0 0 10px}\n'
        '#briefing-company-network .cnt-list{border:1px solid #d9e2e9;border-radius:10px;overflow:hidden;background:#fff}\n'
        '#briefing-company-network .cnt-group .cnt-entry{display:block;margin:0;padding:0;border:0;border-bottom:1px solid #e5ebf0;border-radius:0;background:#fff}\n'
        '#briefing-company-network .cnt-entry:last-child{border-bottom:0}\n'
        '#briefing-company-network .cnt-group .cnt-entry>summary{display:grid;grid-template-columns:minmax(0,1fr) minmax(130px,230px) 100px 12px;align-items:center;gap:16px;list-style:none;padding:15px 17px;cursor:pointer;color:#243e52;font-size:13px;font-weight:500;line-height:1.45;transition:background .15s}\n'
        '#briefing-company-network .cnt-entry>summary::-webkit-details-marker{display:none}\n'
        '#briefing-company-network .cnt-entry>summary:hover{background:#f5f8fa}\n'
        '#briefing-company-network .cnt-entry>summary:focus-visible{outline:3px solid #c3872d;outline-offset:-3px}\n'
        '#briefing-company-network .cnt-entry[open]>summary{background:#edf3f7}\n'
        '#briefing-company-network .cnt-pair{display:flex;align-items:center;gap:10px;flex-wrap:wrap;min-width:0}\n'
        '#briefing-company-network .cnt-actor{display:inline-flex;align-items:center;gap:7px;min-width:0;font-weight:650;overflow-wrap:anywhere}\n'
        '#briefing-company-network .cnt-dot{width:8px;height:8px;border-radius:50%;display:inline-block;flex:0 0 8px;background:#686b75}\n'
        '#briefing-company-network .cnt-kind-target{background:#273447}#briefing-company-network .cnt-kind-partner{background:#2563eb}#briefing-company-network .cnt-kind-customer{background:#198761}#briefing-company-network .cnt-kind-jv{background:#8550b8}#briefing-company-network .cnt-kind-owner{background:#bd6a17}#briefing-company-network .cnt-kind-supplier{background:#bf405a}#briefing-company-network .cnt-kind-subsidiary{background:#127d90}#briefing-company-network .cnt-kind-project{background:#8b7920}#briefing-company-network .cnt-kind-institution{background:#526580}#briefing-company-network .cnt-kind-person{background:#b14ea1}\n'
        '#briefing-company-network .cnt-arrow{color:#8c9aa6;font-size:15px}\n'
        '#briefing-company-network .cnt-type{justify-self:start;padding:4px 9px;border-radius:5px;font-size:11px;font-weight:650;line-height:1.4;background:#f0f2f5;color:#515b6b}\n'
        '#briefing-company-network .cnt-type-partner{background:#eaf1ff;color:#2456ab}#briefing-company-network .cnt-type-customer{background:#e9f6ef;color:#186344}#briefing-company-network .cnt-type-jv{background:#f2ecf9;color:#714298}#briefing-company-network .cnt-type-owner{background:#fff2e3;color:#925010}#briefing-company-network .cnt-type-supplier{background:#fcecf0;color:#a33750}#briefing-company-network .cnt-type-subsidiary{background:#e7f5f7;color:#116b7b}#briefing-company-network .cnt-type-project{background:#f7f4e3;color:#756216}\n'
        '#briefing-company-network .cnt-state{font-size:11px;color:#687b89}\n'
        '#briefing-company-network .cnt-chevron{display:block;width:7px;height:7px;border-right:1.5px solid #687b89;border-bottom:1.5px solid #687b89;transform:rotate(45deg);transition:transform .15s}\n'
        '#briefing-company-network .cnt-entry[open] .cnt-chevron{transform:rotate(225deg)}\n'
        '#briefing-company-network .cnt-expanded{padding:4px 20px 16px;border-top:1px solid #e0e8ee;max-width:100%;background:#f9fbfc}\n'
        '#briefing-company-network .cnt-meta{display:flex;flex-wrap:wrap;gap:8px 24px;padding:13px 0 3px;font-size:11px;color:#627787}\n'
        '#briefing-company-network .cnt-meta strong{font-weight:600;color:#324e62;margin-right:5px}\n'
        '#briefing-company-network .cnt-group .cnt-expanded p{font-size:13px;line-height:1.65;overflow-wrap:anywhere}\n'
        '#briefing-company-network .cnt-expanded small{font-size:11px;color:#6a7c89}\n'
        '@media(max-width:800px){#briefing-company-network .cnt-group .cnt-entry>summary{grid-template-columns:minmax(0,1fr) 12px;gap:8px 12px;padding:13px}.cnt-pair{grid-column:1}.cnt-type{grid-column:1}.cnt-state{grid-column:1}#briefing-company-network .cnt-chevron{grid-column:2;grid-row:1/4}#briefing-company-network .cnt-expanded{padding:4px 13px 13px}}\n'
        '\n'
        '/* Einzelakteure in vier nebeneinander angeordneten Clustertabellen. */\n'
        '#briefing-company-network .cnt-actor-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;align-items:start}\n'
        '#briefing-company-network .cnt-actor-grid .cnt-group{margin:0;border:1px solid #dce5eb;border-radius:10px;overflow:hidden;background:#fff;border-top:3px solid var(--cnt-accent)}\n'
        '#briefing-company-network .cnt-cluster-capital{--cnt-accent:#285e7b}#briefing-company-network .cnt-cluster-structure{--cnt-accent:#ac7734}#briefing-company-network .cnt-cluster-technology{--cnt-accent:#287b70}#briefing-company-network .cnt-cluster-market{--cnt-accent:#68648e}\n'
        '#briefing-company-network .cnt-actor-grid h4{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:14px 13px;margin:0;font-size:13px;line-height:1.45;min-height:65px;background:#f5f8fa;color:var(--cnt-accent);border-bottom:1px solid #e1e8ed}\n'
        '#briefing-company-network .cnt-group-count{font-size:11px;flex:none;border-radius:20px;padding:2px 7px;background:white;border:1px solid #dce5eb}\n'
        '#briefing-company-network .cnt-group .cnt-actor-table{min-width:0;width:100%;table-layout:fixed;border-collapse:collapse;margin:0}\n'
        '#briefing-company-network .cnt-group .cnt-actor-table td{padding:0;border:0;border-bottom:1px solid #e6ecf0}\n'
        '#briefing-company-network .cnt-actor-table tr:last-child td{border-bottom:0}\n'
        '#briefing-company-network .cnt-group .cnt-actor-entry{padding:0;margin:0;border:0;border-radius:0;background:transparent}\n'
        '#briefing-company-network .cnt-group .cnt-actor-entry>summary{display:flex;justify-content:space-between;align-items:center;gap:10px;list-style:none;padding:13px;font-size:12px;line-height:1.5;color:#243e52;min-height:48px;cursor:pointer}\n'
        '#briefing-company-network .cnt-actor-entry>summary::-webkit-details-marker{display:none}\n'
        '#briefing-company-network .cnt-actor-entry>summary:hover,#briefing-company-network .cnt-actor-entry[open]>summary{background:#edf3f7}\n'
        '#briefing-company-network .cnt-actor-entry>summary:focus-visible{outline:3px solid #c3872d;outline-offset:-3px}\n'
        '#briefing-company-network .cnt-actor-entry[open] .cnt-chevron{transform:rotate(225deg)}\n'
        '#briefing-company-network .cnt-actor-entry .cnt-chevron{flex:0 0 7px}\n'
        '#briefing-company-network .cnt-actor-entry .cnt-expanded{padding:4px 13px 13px}\n'
        '#briefing-company-network .cnt-group .cnt-actor-entry .cnt-expanded p{font-size:12px}\n'
        '#briefing-company-network .cnt-source-title{font-weight:700;color:#36536a;padding-top:8px}\n'
        '#briefing-company-network .cn-grid{grid-template-columns:minmax(0,1fr)}\n'
        '#briefing-company-network .cn-sidebar{position:static}\n'
        '#briefing-company-network .cn-detail-content{min-height:0;max-height:380px}\n'
        '@media(min-width:1750px){#briefing-company-network .cn-grid{grid-template-columns:minmax(0,1fr) 300px}#briefing-company-network .cn-sidebar{position:sticky}}\n'
        '@media(max-width:1050px){#briefing-company-network .cnt-actor-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}\n'
        '@media(max-width:560px){#briefing-company-network .cnt-actor-grid{grid-template-columns:minmax(0,1fr)}}\n'
        '\n'
        '#briefing-company-network .cnt-overview{display:flex;align-items:center;flex-wrap:wrap;gap:10px 24px;margin:13px 0 20px}\n'
        '#briefing-company-network .cnt-overview .cnt-count{margin:0;flex:none;font-size:12px;font-weight:600}\n'
        '#briefing-company-network .cnt-legend{display:flex;align-items:center;flex-wrap:wrap;gap:7px 14px;font-size:11px;line-height:1.5;color:#52697a}\n'
        '#briefing-company-network .cnt-legend-title{font-weight:650;color:#36536a}\n'
        '#briefing-company-network .cnt-legend-item{display:inline-flex;align-items:center;gap:6px;white-space:nowrap}\n'
        '</style>\n'
        '<script>\n'
        '(()=>{\n'
        " const root=document.getElementById('briefing-company-network');\n"
        ' if(!root)return;\n'
        " const kinds={target:['Zielunternehmen','#273447','#e0e8f4'],partner:['Partner','#2563eb','#83b1ff'],customer:['Kunde','#198761','#63d4a6'],jv:['Joint Venture','#8550b8','#c6a0fb'],owner:['Eigentümer','#bd6a17','#f2b46c'],supplier:['Zulieferer','#bf405a','#ff92aa'],subsidiary:['Tochtergesellschaft','#127d90','#71d3e7'],project:['Projektpartner','#8b7920','#dace77'],person:['Mandatsträger','#b14ea1','#efa1dd'],institution:['Institution','#526580','#abc0dd'],other:['Weitere Akteure','#686b75','#b7bbc8']};\n"
        " const categories={partner:'Partner',customer:'Kunden',jv:'Joint Ventures',owner:'Eigentum',supplier:'Zulieferer',subsidiary:'Tochtergesellschaften',project:'Projekte',other:'Weitere Beziehungen'};\n"
        " const svg=root.querySelector('.cn-svg'),plot=root.querySelector('.cn-plot'),keyboard=root.querySelector('.cn-keyboard'),detail=root.querySelector('.cn-details');\n"
        " const ns='http://www.w3.org/2000/svg';\n"
        ' function dom(tag,parent,text){const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(parent)parent.appendChild(e);return e;}\n'
        ' function mark(tag,attrs,parent){const e=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));parent.appendChild(e);return e;}\n'
        " function safeURL(value){const u=new URL(value);if(!['http:','https:'].includes(u.protocol))throw Error('Unzulässiger Quellenlink');return u.href;}\n"
        ' function color(kind){return kinds[kind][1];}\n'
        '\n'
        ' const nodeRadius=14;\n'
        " const shapes={target:'circle',partner:'circle',subsidiary:'square',jv:'hexagon',owner:'octagon',supplier:'diamond',customer:'triangle',project:'pentagon',institution:'capsule',person:'star',other:'ellipse'};\n"
        " function polygon(kind,r){const shape=shapes[kind];if(shape==='square'||shape==='capsule')return [[-r,-r],[r,-r],[r,r],[-r,r]];if(shape==='diamond')return [[0,-r],[r,0],[0,r],[-r,0]];if(shape==='triangle')return [[0,-r],[r,r],[-r,r]];if(shape==='hexagon')return [[-r/2,-r],[r/2,-r],[r,0],[r/2,r],[-r/2,r],[-r,0]];if(['octagon','pentagon','star'].includes(shape)){const count=shape==='octagon'?8:shape==='pentagon'?5:10;return Array.from({length:count},(_,i)=>{const radius=shape==='star'&&i%2?r*.5:r,angle=-Math.PI/2+i*2*Math.PI/count;return [radius*Math.cos(angle),radius*Math.sin(angle)]});}return null;}\n"
        " function symbol(kind,r,parent,active=false){const shape=shapes[kind],attrs={class:'cn-symbol',fill:kind==='target'?'#163047':color(kind),stroke:active?'#c3872d':'white','stroke-width':active?4:2.5};if(shape==='square'||shape==='capsule')return mark('rect',{...attrs,x:-r,y:-r,width:2*r,height:2*r,rx:shape==='capsule'?r*.65:6},parent);if(shape==='ellipse')return mark('ellipse',{...attrs,cx:0,cy:0,rx:r,ry:r*.75},parent);const points=polygon(kind,r);if(points)return mark('polygon',{...attrs,points:points.map(p=>p.join(',')).join(' ')},parent);return mark('circle',{...attrs,cx:0,cy:0,r},parent);}\n"
        " function anchor(p,q,extra=0){const dx=q.x-p.x,dy=q.y-p.y,r=nodeRadius,points=polygon(p.kind,r);let t;if(points){t=Infinity;for(let i=0;i<points.length;i++){const [ax,ay]=points[i],[bx,by]=points[(i+1)%points.length],ex=bx-ax,ey=by-ay,den=dx*ey-dy*ex;if(Math.abs(den)<1e-9)continue;const k=(ax*ey-ay*ex)/den,u=(ax*dy-ay*dx)/den;if(k>=0&&u>=0&&u<=1)t=Math.min(t,k);}}else{const ry=shapes[p.kind]==='ellipse'?r*.75:r;t=1/Math.sqrt(dx*dx/(r*r)+dy*dy/(ry*ry));}const length=Math.hypot(dx,dy)||1;return {x:p.x+dx*t+dx/length*extra,y:p.y+dy*t+dy/length*extra};}\n"
        " function validDate(v,month=false){if(typeof v!=='string'||!(month?/^\\d{4}-\\d{2}(?:-\\d{2})?$/:/^\\d{4}-\\d{2}-\\d{2}$/).test(v))return false;const a=v.split('-').map(Number);return a[1]>=1&&a[1]<=12&&(a.length===2||a[2]>=1&&a[2]<=new Date(Date.UTC(a[0],a[1],0)).getUTCDate());}\n"
        ' try{\n'
        "  const data=JSON.parse(root.querySelector('.cn-data').textContent);\n"
        "  if(data.schema_version!==1||typeof data.company!=='string'||!data.company.trim()||!validDate(data.as_of)||![data.nodes,data.edges,data.sources,data.products].every(Array.isArray))throw Error('Ungültiges Netzwerkformat oder Firmenbezug');\n"
        "  function index(items){const m=new Map();items.forEach(x=>{if(!x.id||m.has(x.id))throw Error('Fehlende oder doppelte ID');m.set(x.id,x);});return m;}\n"
        '  const nodes=index(data.nodes),sources=index(data.sources),products=index(data.products),edgeIndex=index(data.edges);\n'
        "  if(!nodes.has(data.target_id)||data.nodes.filter(n=>n.kind==='target').length!==1||nodes.get(data.target_id).kind!=='target')throw Error('Zielunternehmen fehlt');\n"
        "  data.nodes.forEach(n=>{if(!kinds[n.kind]||typeof n.label!=='string'||!n.label.trim()||n.cluster&&!['capital','structure','technology','market'].includes(n.cluster))throw Error('Ungültiger Knoten');});\n"
        "  data.products.forEach(p=>{if(typeof p.label!=='string')throw Error('Ungültiges Produkt');});\n"
        "  data.sources.forEach(s=>{if(typeof s.title!=='string'||!s.title||typeof s.name!=='string'||!s.name||!Object.hasOwn(s,'published_date')||!Object.hasOwn(s,'accessed_date')||s.published_date!==null&&!validDate(s.published_date)||!validDate(s.accessed_date))throw Error('Quellenmetadaten fehlen');safeURL(s.url);});\n"
        "  data.edges.forEach(e=>{if(!nodes.has(e.from)||!nodes.has(e.to)||e.from===e.to||!Array.isArray(e.categories)||!e.categories.length||e.categories.some(c=>!categories[c])||!Array.isArray(e.product_ids)||e.product_ids.some(p=>!products.has(p))||!Array.isArray(e.source_ids)||!e.source_ids.length||e.source_ids.some(s=>!sources.has(s))||!Array.isArray(e.claim_ids)||!e.claim_ids.length||e.claim_ids.some(c=>typeof c!=='string'||!c.trim())||typeof e.type!=='string'||!e.type||typeof e.summary!=='string'||!e.summary||typeof e.status!=='string'||!e.status||!validDate(e.as_of,true))throw Error('Unvollständige Beziehung oder Belege');});\n"
        "  function openNetwork(){detail.hidden=false;detail.querySelector('.cn-detail-content').scrollTop=0;}\n"
        '  let selected=null;\n'
        '  const available=[...new Set(data.edges.flatMap(e=>e.categories))];\n'
        "  available.forEach(c=>{const label=dom('label',root.querySelector('.cn-filters'));const input=dom('input',label);input.type='checkbox';input.value=c;input.checked=true;dom('span',label,categories[c]);input.addEventListener('change',()=>{clear();draw();});});\n"
        "  data.products.forEach(p=>{const option=dom('option',root.querySelector('.cn-product'),p.label);option.value=p.id;});\n"
        "  root.querySelector('.cn-product-label').hidden=!data.products.length;\n"
        "  [...new Set(data.nodes.map(n=>n.kind))].forEach(k=>{const label=dom('span',root.querySelector('.cn-legend'));const icon=document.createElementNS(ns,'svg');icon.setAttribute('width','20');icon.setAttribute('height','20');icon.setAttribute('viewBox','-10 -10 20 20');icon.setAttribute('aria-hidden','true');icon.classList.add('cn-kind-icon');label.appendChild(icon);symbol(k,8,icon);dom('span',label,kinds[k][0]);});\n"
        "  function sourceList(ids,parent){ids.forEach(id=>{const s=sources.get(id);const p=dom('p',parent);const a=dom('a',p,s.name+' · '+s.title);a.href=safeURL(s.url);a.target='_blank';a.rel='noopener noreferrer';dom('span',p,' · '+(s.published_date||'o. D.')+(s.source_kind?' · '+s.source_kind:'')+(s.report_year?' · Geschäftsjahr '+s.report_year:'')+(s.page?' · Seite '+s.page:'')+(s.section?' · '+s.section:'')+(s.accessed_date?' · Abruf '+s.accessed_date:''));});}\n"
        "  function selectEdge(id){selected=id;const e=edgeIndex.get(id);detail.hidden=false;detail.querySelector('h4').textContent=nodes.get(e.from).label+' → '+nodes.get(e.to).label;const body=detail.querySelector('.cn-detail-content');body.replaceChildren();dom('p',body,e.type+' · '+e.status+' · Stand '+e.as_of);dom('p',body,e.summary);if(e.interpretation)dom('p',body,'Analysteninterpretation: '+e.interpretation);if(e.capital_share!==undefined&&e.capital_share!==null)dom('p',body,'Kapitalanteil: '+e.capital_share);if(e.voting_share!==undefined&&e.voting_share!==null)dom('p',body,'Stimmrechte: '+e.voting_share);if(e.control)dom('p',body,'Kontrolle: '+e.control);if(e.product_ids.length)dom('p',body,'Produktbezug: '+e.product_ids.map(p=>products.get(p).label).join(', '));if(e.uncertainty)dom('p',body,'Unsicherheit: '+e.uncertainty);const cp=dom('p',body,'Belegdetails: ');claimLinks(e.claim_ids,cp);sourceList(e.source_ids,body);draw();openNetwork();}\n"
        "  function claimLinks(ids,parent){ids.forEach((id,i)=>{if(i)dom('span',parent,', ');const a=dom('a',parent,id);a.href='#'+encodeURIComponent(id);});}\n"
        "  const tableBody=root.querySelector('.cn-table tbody');tableBody.replaceChildren();\n"
        "  data.edges.forEach(e=>{const tr=dom('tr',tableBody);dom('td',tr,nodes.get(e.from).label+' → '+nodes.get(e.to).label);const rel=dom('td',tr,e.type+' · '+e.summary);claimLinks(e.claim_ids,dom('p',rel,'Belegdetails: '));for(const [k,label]of [['capital_share','Kapitalanteil'],['voting_share','Stimmrechte'],['control','Kontrolle'],['uncertainty','Evidenzgrenze'],['interpretation','Analysteninterpretation']])if(e[k]!==undefined&&e[k]!==null&&e[k]!=='')dom('p',rel,label+': '+e[k]);if(e.product_ids.length)dom('p',rel,'Produkt: '+e.product_ids.map(id=>products.get(id).label).join(', '));dom('td',tr,e.status+' · '+e.as_of);sourceList(e.source_ids,dom('td',tr));});\n"
        "  const clusterDefs=[['capital','Kapital & Investoren'],['structure','Konzern & Joint Ventures'],['technology','Technologie & Industrie'],['market','Kunden & Marktzugang']];\n"
        "  let expanded=new Set(clusterDefs.map(c=>c[0])),activeNode=null;root.querySelector('.cn-cross').checked=true;\n"
        "  function group(n){return n.cluster||({owner:'capital',subsidiary:'structure',jv:'structure',customer:'market',institution:'market'}[n.kind]||'technology');}\n"
        '  const grouped=new Map(clusterDefs.map(([id])=>[id,data.nodes.filter(n=>n.id!==data.target_id&&group(n)===id)]));\n'
        '  const first=new Set();grouped.forEach(list=>[...list.filter(n=>n.focus===true),...list.filter(n=>n.focus!==true)].slice(0,6).forEach(n=>first.add(n.id)));\n'
        "  clusterDefs.forEach(([id,label])=>{const b=dom('button',root.querySelector('.cn-clusters'),label+' +');b.type='button';b.dataset.cluster=id;b.setAttribute('aria-pressed','false');b.addEventListener('click',()=>{expanded.has(id)?expanded.delete(id):expanded.add(id);draw();});});\n"
        "  [...new Set(data.edges.map(e=>e.status))].forEach(s=>{const o=dom('option',root.querySelector('.cn-status'),s);o.value=s;});\n"
        "  function clear(){selected=null;activeNode=null;detail.hidden=false;detail.querySelector('h4').textContent='Beziehungen & Quellen';const body=detail.querySelector('.cn-detail-content');body.replaceChildren();dom('p',body,'Wähle einen Akteur oder eine Verbindung im Netzwerk. Hier erscheinen die zugehörigen Inhalte und Originalquellen.');}\n"
        "  function selectNode(id){activeNode=id;selected=null;detail.hidden=false;detail.querySelector('h4').textContent=nodes.get(id).legal_name||nodes.get(id).label;const body=detail.querySelector('.cn-detail-content');body.replaceChildren();dom('p',body,kinds[nodes.get(id).kind][0]+' · Eine Organisation, mehrere Rollen möglich.');data.edges.filter(e=>e.from===id||e.to===id).forEach(e=>{const b=dom('button',body,nodes.get(e.from).label+' → '+nodes.get(e.to).label+' · '+e.type+' · '+e.status);b.className='cn-relation';b.type='button';b.addEventListener('click',()=>{activeNode=null;selectEdge(e.id);});});draw();openNetwork();}\n"
        "  function selectBundle(ids){if(ids.length===1){activeNode=null;selectEdge(ids[0]);return;}const first=edgeIndex.get(ids[0]);selected=ids[0];activeNode=null;detail.hidden=false;detail.querySelector('h4').textContent=nodes.get(first.from).label+' ↔ '+nodes.get(first.to).label;const body=detail.querySelector('.cn-detail-content');body.replaceChildren();dom('p',body,ids.length+' belegte Beziehungen zwischen diesen Akteuren. Eine Beziehung wählen, um Status und Originalquellen zu lesen.');ids.forEach(id=>{const e=edgeIndex.get(id),b=dom('button',body,e.type+' · '+e.status+' · '+e.as_of);b.type='button';b.className='cn-relation';b.addEventListener('click',()=>selectEdge(id));});draw();openNetwork();}\n"
        '  function draw(){\n'
        "   const enabled=new Set([...root.querySelectorAll('.cn-filters input:checked')].map(x=>x.value)),product=root.querySelector('.cn-product').value,status=root.querySelector('.cn-status').value,query=root.querySelector('.cn-search').value.toLocaleLowerCase().trim(),restrict=query||product!=='all'||status!=='all'||enabled.size!==available.length;\n"
        "   const eligible=data.edges.filter(e=>e.categories.some(c=>enabled.has(c))&&(product==='all'||e.product_ids.includes(product))&&(status==='all'||e.status===status)&&(!query||[nodes.get(e.from).label,nodes.get(e.to).label,e.type,e.summary].join(' ').toLocaleLowerCase().includes(query)));\n"
        '   if(selected&&!eligible.some(e=>e.id===selected)){clear();}\n'
        '   const names=new Set([data.target_id]);if(restrict)eligible.forEach(e=>{names.add(e.from);names.add(e.to);});else grouped.forEach((list,id)=>list.filter(n=>expanded.has(id)||first.has(n.id)).forEach(n=>names.add(n.id)));\n'
        '   if(activeNode)eligible.filter(e=>e.from===activeNode||e.to===activeNode).forEach(e=>{names.add(e.from);names.add(e.to);});\n'
        '   if(selected){const e=edgeIndex.get(selected);names.add(e.from);names.add(e.to);}\n'
        '   // Retain the participants and actual partial edges of a visible joint venture.\n'
        "   eligible.filter(e=>e.categories.includes('jv')&&(names.has(e.from)||names.has(e.to))).forEach(e=>{names.add(e.from);names.add(e.to);});\n"
        "   eligible.filter(e=>e.from!==data.target_id&&e.to!==data.target_id&&(names.has(e.from)||names.has(e.to))).forEach(e=>{if(nodes.get(e.from).kind==='subsidiary')names.add(e.from);if(nodes.get(e.to).kind==='subsidiary')names.add(e.to);});\n"
        "   const cross=root.querySelector('.cn-cross').checked;\n"
        "   const visible=eligible.filter(e=>names.has(e.from)&&names.has(e.to)&&(cross||e.from===data.target_id||e.to===data.target_id||nodes.get(e.from).kind==='subsidiary'||nodes.get(e.to).kind==='subsidiary'||e.categories.includes('jv')||e.id===selected||activeNode&&(e.from===activeNode||e.to===activeNode)));\n"
        '   const connected=new Set([data.target_id,...visible.flatMap(e=>[e.from,e.to])]);for(const id of names)if(!connected.has(id))names.delete(id);\n'
        '\n'
        '   const w=Math.max(640,(plot.clientWidth||960)-10),pad=16,gutter=28,panelW=(w-2*pad-gutter)/2,columns=5,cellW=(panelW-32)/columns,rowStep=94;\n'
        '   const groups=clusterDefs.map(([id])=>({id,all:grouped.get(id),shown:grouped.get(id).filter(n=>names.has(n.id))}));\n'
        '   const get=id=>groups.find(g=>g.id===id),needed=id=>62+Math.max(1,Math.ceil(get(id).shown.length/columns))*rowStep;\n'
        "   const topH=Math.max(needed('capital'),needed('structure')),bottomH=Math.max(needed('technology'),needed('market')),centerGap=128,h=2*pad+topH+centerGap+bottomH;\n"
        "   const panelH=id=>['capital','structure'].includes(id)?topH:bottomH,areaColors={capital:'#285e7b',structure:'#ac7734',technology:'#287b70',market:'#68648e'};\n"
        "   const cx=w/2,cy=pad+topH+centerGap/2,positions=new Map([[data.target_id,{x:cx,y:cy,kind:'target'}]]);\n"
        "   svg.setAttribute('viewBox','0 0 '+w+' '+h);svg.style.minWidth='0';svg.style.height='auto';svg.replaceChildren();keyboard.replaceChildren();svg.classList.toggle('has-selection',Boolean(selected||activeNode));\n"
        "   mark('title',{},svg).textContent=data.company+' im Mittelpunkt. Gleich große Knoten, Formen und Farben je Akteurstyp, Namen darunter; Quellen rechts.';\n"
        "   const placements=[['capital',pad,pad],['structure',pad+panelW+gutter,pad],['technology',pad,pad+topH+centerGap],['market',pad+panelW+gutter,pad+topH+centerGap]];\n"
        '   placements.forEach(([id,x,y])=>{\n'
        '    const g=get(id),label=clusterDefs.find(d=>d[0]===id)[1],area=areaColors[id];\n'
        "    mark('rect',{x,y,width:panelW,height:panelH(id),rx:14,fill:area,'fill-opacity':.035,stroke:area,'stroke-opacity':.22,class:'cn-area','data-cluster-area':id},svg);\n"
        "    mark('text',{x:x+18,y:y+27,class:'cn-cluster-title'},svg).textContent=label;\n"
        "    mark('text',{x:x+18,y:y+46,style:'fill:#7a919d;font-size:10px'},svg).textContent=g.shown.length+' von '+g.all.length+' Akteuren';\n"
        "    if(!g.shown.length)mark('text',{x:x+18,y:y+86,style:'fill:#7a919d;font-size:11px'},svg).textContent='Keine Verbindung in dieser Auswahl';\n"
        '    g.shown.forEach((n,i)=>positions.set(n.id,{x:x+16+(i%columns+.5)*cellW,y:y+90+Math.floor(i/columns)*rowStep,kind:n.kind}));\n'
        '    const b=root.querySelector(\'[data-cluster="\'+id+\'"]\');b.textContent=label+(expanded.has(id)?\' −\':\' +\');b.setAttribute(\'aria-pressed\',String(expanded.has(id)));\n'
        '   });\n'
        "   const defs=mark('defs',{},svg),marker=mark('marker',{id:'cn-arrow',viewBox:'0 0 10 10',refX:9,refY:5,markerWidth:5,markerHeight:5,orient:'auto-start-reverse'},defs);mark('path',{d:'M 0 0 L 10 5 L 0 10 Z',fill:'#466372'},marker);\n"
        "   const lines=mark('g',{},svg),hits=mark('g',{},svg),nlayer=mark('g',{},svg);\n"
        "   const pairs=new Map();visible.forEach(e=>{const key=[e.from,e.to].sort().join('|');if(!pairs.has(key))pairs.set(key,[]);pairs.get(key).push(e);});\n"
        '\n'
        '   let pairNumber=0;\n'
        '   pairs.forEach(relations=>{\n'
        '    const e=relations[0],a=positions.get(e.from),b=positions.get(e.to);if(!a||!b)return;\n'
        '    const aa=anchor(a,b,3),bb=anchor(b,a,7),dx=bb.x-aa.x,dy=bb.y-aa.y,length=Math.hypot(dx,dy)||1,cross=e.from!==data.target_id&&e.to!==data.target_id;\n'
        '    const bend=cross?Math.min(52,length*.1):((pairNumber++%3)-1)*12,mx=(aa.x+bb.x)/2-dy/length*bend,my=(aa.y+bb.y)/2+dx/length*bend;\n'
        "    const d='M '+aa.x+' '+aa.y+' Q '+mx+' '+my+' '+bb.x+' '+bb.y;\n"
        '    const active=relations.some(r=>r.id===selected||activeNode&&(r.from===activeNode||r.to===activeNode)),reverse=relations.some(r=>r.from===e.to&&r.to===e.from);\n'
        "    const dash=relations.every(r=>r.historical||/historisch/i.test(r.status))?'2 5':relations.every(r=>/angekündigt|geplant|announced/i.test(r.status))?'7 5':'none';\n"
        "    const attrs={d,class:'cn-line'+(cross?' cn-line-cross':'')+(active?' cn-line-selected':''),'data-edge':e.id,'data-relations':relations.map(r=>r.id).join(','),'stroke-dasharray':dash,style:'--cn-edge-color:'+(cross?'#24485d':areaColors[group(nodes.get(e.to))]||'#466372'),'marker-end':'url(#cn-arrow)'};if(reverse)attrs['marker-start']='url(#cn-arrow)';mark('path',attrs,lines);\n"
        "    const hit=mark('path',{d,class:'cn-hit','aria-hidden':'true','data-edge':e.id},hits);hit.addEventListener('click',()=>selectBundle(relations.map(r=>r.id)));\n"
        "    const button=dom('button',keyboard,nodes.get(e.from).label+' ↔ '+nodes.get(e.to).label+(relations.length>1?' · '+relations.length+' Beziehungen':' · '+e.type));button.type='button';button.className='cn-edge-button';button.addEventListener('click',()=>selectBundle(relations.map(r=>r.id)));\n"
        '   });\n'
        "   function wrap(label,max=32){const words=label.split(/\\s+/).flatMap(word=>Array.from({length:Math.ceil(word.length/max)},(_,i)=>word.slice(i*max,(i+1)*max))),out=[];let line='';words.forEach(word=>{if((line+' '+word).trim().length>max&&line){out.push(line);line=word;}else line=(line+' '+word).trim();});if(line)out.push(line);return out;}\n"
        '\n'
        '   data.nodes.filter(n=>positions.has(n.id)).forEach(n=>{\n'
        "    const p=positions.get(n.id),target=n.id===data.target_id,g=mark('g',{transform:'translate('+p.x+' '+p.y+')',class:'cn-node',role:'button',tabindex:0,'aria-label':n.legal_name||n.label,'data-node':n.id,'data-kind':n.kind,'data-radius':nodeRadius},nlayer);\n"
        '    symbol(n.kind,nodeRadius,g,activeNode===n.id);\n'
        "    const label=wrap(n.label,target?12:Math.max(6,Math.floor((cellW-12)/7))),shown=label.slice(0,3);if(label.length>3)shown[2]=shown[2].slice(0,-1)+'…';\n"
        '    const start=nodeRadius+17;\n'
        "    shown.forEach((line,i)=>mark('text',{x:0,y:start+i*(target?12:14),'text-anchor':'middle',class:target?'cn-target-label':'cn-node-label',style:'fill:'+'#193445'+';font-size:'+(target?'10px':'11px')+';font-weight:'+(target?'700':'600')},g).textContent=line);\n"
        "    mark('title',{},g).textContent=(n.legal_name||n.label)+' · '+kinds[n.kind][0];\n"
        "    g.addEventListener('click',()=>selectNode(n.id));g.addEventListener('keydown',ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();selectNode(n.id);}});\n"
        '   });\n'
        "   root.querySelector('.cn-count').textContent=(positions.size-1)+' / '+(data.nodes.length-1)+' Akteure · '+visible.length+' / '+data.edges.length+' Beziehungen · '+(cross?'Querverbindungen eingeblendet':'Weitere Querverbindungen per Filter oder Auswahl');root.querySelector('.cn-expand').textContent=expanded.size===4?'Kompakte Auswahl':'Alle Akteure zeigen';\n"
        '\n'
        '  }\n'
        "  root.querySelector('.cn-expand').addEventListener('click',()=>{expanded=expanded.size===4?new Set():new Set(clusterDefs.map(c=>c[0]));root.querySelector('.cn-cross').checked=expanded.size===4;draw();});root.querySelector('.cn-reset').addEventListener('click',()=>{root.querySelector('.cn-search').value='';root.querySelector('.cn-status').value='all';root.querySelector('.cn-product').value='all';root.querySelector('.cn-cross').checked=true;root.querySelectorAll('.cn-filters input').forEach(i=>i.checked=true);expanded.clear();clear();draw();});root.querySelector('.cn-search').addEventListener('input',()=>{clear();draw();});['.cn-status','.cn-cross'].forEach(s=>root.querySelector(s).addEventListener('change',()=>{clear();draw();}));\n"
        "  root.querySelector('.cn-close').addEventListener('click',()=>{clear();draw();});root.querySelector('.cn-product').addEventListener('change',()=>{clear();draw();});root.addEventListener('cn:viewchange',draw);new ResizeObserver(draw).observe(plot);clear();draw();\n"
        '\n'
        " }catch(error){const warning=root.querySelector('.cn-error');warning.hidden=false;warning.textContent='Netzwerkdaten sind unvollständig oder ungültig. Bitte die Cluster-Übergabe prüfen.';console.error('Cluster network:',error.message);}\n"
        '})();\n'
        '</script>\n'
        '<script>\n'
        '(()=>{\n'
        " const root=document.getElementById('briefing-company-network');if(!root)return;\n"
        ' const tabs=[...root.querySelectorAll(\'.cnt-tabs [role="tab"]\')],rows=[...root.querySelectorAll(\'[data-cnt-node]\')],search=root.querySelector(\'.cnt-search\'),category=root.querySelector(\'.cnt-category\');\n'
        " function activate(tab,focus=false){tabs.forEach(t=>{const active=t===tab;t.setAttribute('aria-selected',String(active));t.tabIndex=active?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!active;});if(focus)tab.focus();root.dispatchEvent(new CustomEvent('cn:viewchange'));}\n"
        " tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>activate(tab));tab.addEventListener('keydown',e=>{let next;if(e.key==='ArrowRight')next=(i+1)%tabs.length;else if(e.key==='ArrowLeft')next=(i+tabs.length-1)%tabs.length;else if(e.key==='Home')next=0;else if(e.key==='End')next=tabs.length-1;else return;e.preventDefault();activate(tabs[next],true);});});\n"
        " function filter(){const q=search.value.trim().toLocaleLowerCase(),cat=category.value;let visible=0;rows.forEach(row=>{row.hidden=(cat!=='all'&&row.dataset.kind!==cat)||(q&&!row.dataset.search.includes(q));if(!row.hidden)visible++;});root.querySelectorAll('.cnt-group').forEach(g=>{const count=[...g.querySelectorAll('[data-cnt-node]')].filter(r=>!r.hidden).length;g.hidden=count===0;g.querySelector('.cnt-group-count').textContent=count;});root.querySelector('.cnt-empty').hidden=visible!==0;root.querySelector('.cnt-count').textContent=visible+' von '+rows.length+' Akteuren';}\n"
        " search.addEventListener('input',filter);category.addEventListener('change',filter);root.querySelector('.cnt-reset').addEventListener('click',()=>{search.value='';category.value='all';filter();});filter();\n"
        '})();\n'
        '</script>\n'
    ),
    'module-insights.css': (
        '.module-insights{margin-top:24px;border-top:1px solid #dce5ea;padding-top:20px;color:#193445;min-width:0}\n'
        '.module-insights>h3{font-size:17px;margin:0 0 14px!important}\n'
        '.module-insights .mi-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;align-items:stretch}\n'
        '.module-insights .mi-grid[data-count="1"]{grid-template-columns:minmax(0,1fr)}\n'
        '.module-insights .mi-grid[data-count="2"]{grid-template-columns:repeat(2,minmax(0,1fr))}\n'
        '.module-insights .mi-grid:has(.mi-detail[open]){align-items:start}\n'
        '.module-insights .mi-card{border:1px solid #dce5ea;border-top:3px solid #154c61;border-radius:8px;background:#f3f7f9;padding:16px;min-width:0;display:grid;grid-template-rows:auto auto 1fr auto;gap:12px;align-content:start;overflow-wrap:anywhere}\n'
        '.module-insights .mi-card>h4{font-size:15px;line-height:1.35;margin:0;color:#193445}\n'
        '.module-insights .mi-label{display:block;font-size:11px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:#526a79;margin-bottom:4px}\n'
        '.module-insights .mi-card p{font-size:13px;line-height:1.55;margin:0}\n'
        '.module-insights .mi-insight{border-top:1px solid #dce5ea;padding-top:11px}\n'
        '.module-insights .mi-insight>.mi-label{color:#956621}\n'
        '.module-insights .mi-detail{font-size:12px;min-width:0}\n'
        '.module-insights .mi-detail>summary{color:#154c61;font-size:12px;font-weight:600;line-height:1.5}\n'
        '.module-insights .mi-detail-body{margin-top:13px;padding-top:12px;border-top:1px solid #dce5ea}\n'
        '.module-insights .mi-detail-body h5{font-size:13px;color:#154c61;margin:14px 0 7px}\n'
        '.module-insights .mi-detail-body p{margin:7px 0 12px;font-size:12px}\n'
        '.module-insights .mi-source-fact{padding:10px 0;border-top:1px solid #dce5ea}\n'
        '.module-insights .mi-source-fact>summary{font-size:12px;font-weight:600;line-height:1.5;color:#154c61}\n'
        '.module-insights .mi-source-fact .evidence{padding-left:18px;margin:10px 0}\n'
        '.module-insights .mi-source-fact .evidence li{font-size:12px;padding:8px 10px;margin:8px 0;background:white;border-left:2px solid #dce5ea}\n'
        '.module-insights .mi-source-fact .evidence a{font-size:12px;font-weight:600;overflow-wrap:anywhere}\n'
        '.module-insights .mi-empty{font-size:12px;color:#526a79;margin:0;background:#f3f7f9;padding:12px 15px;border-radius:5px}\n'
        '@media print{\n'
        ' .module-insights .mi-grid{display:block}\n'
        ' .module-insights .mi-card{display:block;margin:12px 0;break-inside:avoid;print-color-adjust:exact;-webkit-print-color-adjust:exact}\n'
        ' .module-insights .mi-card>div,.module-insights .mi-card>details{margin-top:12px}\n'
        '}\n'
    ),
    'portfolio.css': (
        '.pf-root{--pf-brand:#154c61;--pf-line:#dce4e8;--pf-muted:#607180;color:#173345}.pf-root h2{font-size:26px!important;line-height:1.2;border:0!important;padding:0!important;margin:6px 0 0!important}.pf-head{display:flex;justify-content:space-between;align-items:center;gap:22px;padding:22px 0}.pf-num{display:block;color:#a16e28;font-size:11px;font-weight:700;letter-spacing:.1em}.pf-intro{color:var(--pf-muted);max-width:920px;margin:0 0 20px}.pf-root button,.pf-root input,.pf-root select{border:1px solid #d4dfe5;border-radius:6px;background:white;color:#173345;padding:9px 12px;font:inherit}.pf-views{display:flex;gap:6px}.pf-views button[aria-pressed=true]{color:white;background:var(--pf-brand);border-color:var(--pf-brand)}.pf-filters{display:grid;grid-template-columns:1.6fr 1.2fr 1.2fr 1.1fr auto;gap:12px;align-items:end;padding:16px;background:#f3f6f8;border:1px solid var(--pf-line);border-radius:9px}.pf-filters label{display:grid;gap:5px;font-size:12px;font-weight:600;min-width:0}.pf-filters input,.pf-filters select{width:100%}.pf-count{color:var(--pf-muted);font-size:12px}.pf-table-wrap{overflow:auto;border:1px solid var(--pf-line);border-radius:9px}.pf-root table{border-collapse:collapse;width:100%;font-size:13px}.pf-root th,.pf-root td{min-width:0;padding:12px;border-bottom:1px solid #dce4e8;text-align:left;vertical-align:top}.pf-maturity-map{table-layout:fixed;min-width:860px}.pf-maturity-map thead th{background:#154c61;color:#fff;border-right:1px solid #376779;font-size:11px;line-height:1.45}.pf-maturity-map thead th:first-child{width:164px;vertical-align:middle}.pf-maturity-map thead b{font-size:22px;display:block;margin-bottom:4px}.pf-maturity-map thead span{display:block}.pf-maturity-map tbody th{background:#f0f4f6;font-size:12px;font-weight:700;position:sticky;left:0;z-index:1}.pf-maturity-map td{border-right:1px solid #e3ebef;background:#fbfdfe;height:80px}.pf-maturity-map tbody tr:nth-child(even) td{background:#f3f8fa}.pf-domain-mark{width:9px;height:9px;border-radius:50%;display:inline-block;margin-right:7px}.pf-map-item{display:flex;align-items:center;gap:6px;margin:4px 0 8px;padding:6px 7px;text-decoration:none!important;color:#173345!important;font-size:12px;line-height:1.35;border:1px solid #dce5ea;border-left:3px solid var(--pf-domain);border-radius:5px;background:white}.pf-map-item:hover{box-shadow:0 2px 7px #17334518;border-color:var(--pf-domain)}.pf-map-item small{font-size:9px;margin-left:auto;background:#edf3f5;border-radius:3px;padding:1px 4px;flex:none}.pf-dot{width:6px;height:6px;border-radius:50%;background:var(--pf-domain);flex:none}.pf-unknown{background:#fff8ee;border:1px solid #ead8b7;border-radius:8px;padding:14px;margin-top:16px}.pf-unknown p{color:var(--pf-muted);font-size:13px}.pf-unknown .pf-map-item{display:inline-flex;margin:5px 8px 0 0}.pf-results{min-width:790px}.pf-results thead th{background:#154c61;color:white}.pf-results td:nth-child(4){width:45%}.pf-method{border:1px solid var(--pf-line);border-radius:9px;padding:16px;margin:22px 0}.pf-method>summary{font-size:18px;font-weight:700}.pf-method>summary .pf-num{margin-bottom:6px}.pf-method-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:18px}.pf-method-grid>div{padding:13px;border:1px solid var(--pf-line);border-radius:7px;background:#f7fafb}.pf-method p{font-size:13px;color:var(--pf-muted)}.pf-profiles-disclosure{border:1px solid var(--pf-line);border-radius:12px;background:white;margin:26px 0 0}.pf-profiles-disclosure>.pf-head{padding:24px;list-style:none;cursor:pointer}.pf-profiles-disclosure>.pf-head::-webkit-details-marker{display:none}.pf-chevron{font-size:30px;color:var(--pf-brand);flex:none}.pf-profiles-disclosure[open]>.pf-head{border-bottom:1px solid var(--pf-line)}.pf-profiles-disclosure[open] .pf-chevron{transform:rotate(45deg)}.pf-profiles-body{padding:20px 24px}.pf-profile-toolbar{display:flex;justify-content:space-between;align-items:center;gap:12px;font-size:13px;color:var(--pf-muted);margin-bottom:16px}.pf-profile{border:1px solid var(--pf-line);border-radius:9px;margin:12px 0;scroll-margin-top:90px}.pf-profile>summary{display:flex;gap:14px;align-items:center;list-style:none;padding:16px;cursor:pointer}.pf-profile>summary::-webkit-details-marker{display:none}.pf-grade{display:flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:7px;background:#e8f1f5;color:#154c61;font-size:23px;font-weight:700;flex:none}.pf-profile strong{font-size:16px}.pf-profile small{margin-top:4px;font-size:12px;color:var(--pf-muted)}.pf-plus{margin-left:auto;color:#154c61;font-size:24px}.pf-profile[open] .pf-plus{transform:rotate(45deg)}.pf-profile[open]{border-color:#97b4c2}.pf-profile-content{padding:4px 20px 20px}.pf-profile-content dl{display:grid;grid-template-columns:175px minmax(0,1fr);gap:0 20px;margin:0}.pf-profile-content dt,.pf-profile-content dd{margin:0;padding:14px 0;border-top:1px solid var(--pf-line)}.pf-profile-content dt{font-size:12px;font-weight:700;color:var(--pf-muted)}.pf-profile-content dd{font-size:14px}.pf-evidence{padding:10px 0;border-bottom:1px solid var(--pf-line)}.pf-evidence>summary{font-size:13px;font-weight:600}.pf-empty{background:#f3f6f8;padding:14px;border-radius:8px}@media print{.pf-filters,.pf-views,.pf-reset,.pf-expand,.pf-count,.pf-chevron,.pf-plus{display:none!important}.pf-table-wrap{overflow:visible}.pf-maturity-map,.pf-results{min-width:0}.pf-profile{break-inside:avoid}.pf-root th,.pf-root td{padding:6px}.pf-profiles-body{padding:8px}.pf-profile-content dl{grid-template-columns:140px 1fr}}\n'
    ),
    'portfolio.js': (
        '(()=>{\n'
        " const root=document.getElementById('briefing-portfolio');if(!root)return;\n"
        " const rows=[...root.querySelectorAll('[data-pf-result]')],items=[...root.querySelectorAll('[data-pf-item]')],profiles=[...root.querySelectorAll('.pf-profile')];\n"
        " const query=root.querySelector('[data-pf-filter=query]'),domain=root.querySelector('[data-pf-filter=domain]'),grade=root.querySelector('[data-pf-filter=grade]'),origin=root.querySelector('[data-pf-filter=origin]');\n"
        " root.querySelector('.pf-filters').hidden=false;root.querySelector('.pf-views').hidden=false;root.querySelector('.pf-expand').hidden=false;\n"
        " function filter(){const q=query.value.trim().toLocaleLowerCase(),visible=new Set();rows.forEach(row=>{const cells=row.querySelectorAll('td'),g=cells[2].textContent.split(' · ')[0];row.hidden=Boolean(q&&!row.textContent.toLocaleLowerCase().includes(q)||domain.value&&cells[1].textContent!==domain.value||grade.value&&(grade.value==='unknown'?g!=='Nicht eindeutig bestimmbar':g!==grade.value)||origin.value&&!row.dataset.pfOrigin.split('|').includes(origin.value));if(!row.hidden)visible.add(row.dataset.pfResult);});items.forEach(i=>i.hidden=!visible.has(i.dataset.pfItem));root.querySelectorAll('[data-pf-group]').forEach(row=>row.hidden=![...row.querySelectorAll('[data-pf-item]')].some(i=>!i.hidden));const unknown=root.querySelector('.pf-unknown');unknown.hidden=![...unknown.querySelectorAll('[data-pf-item]')].some(i=>!i.hidden);root.querySelector('.pf-count').textContent=visible.size+' von '+rows.length+' Einträgen';root.querySelector('.pf-empty').hidden=visible.size!==0;}\n"
        " [query,domain,grade,origin].forEach(f=>f.addEventListener(f===query?'input':'change',filter));root.querySelector('.pf-reset').addEventListener('click',()=>{query.value=domain.value=grade.value=origin.value='';filter();});\n"
        " root.querySelectorAll('[data-pf-view]').forEach(b=>b.addEventListener('click',()=>{const map=b.dataset.pfView==='map';root.querySelector('.pf-map-view').hidden=!map;root.querySelector('.pf-result-view').hidden=map;root.querySelectorAll('[data-pf-view]').forEach(v=>v.setAttribute('aria-pressed',String(v===b)));}));\n"
        " const expand=root.querySelector('.pf-expand');expand.addEventListener('click',()=>{const open=profiles.some(p=>!p.open);profiles.forEach(p=>p.open=open);expand.textContent=open?'Alle Profile schließen':'Alle Profile öffnen';});filter();\n"
        " let printHidden=null;window.addEventListener('beforeprint',()=>{if(printHidden)return;printHidden=[...root.querySelectorAll('[data-pf-item],[data-pf-group],.pf-unknown,.pf-map-view,.pf-result-view,.pf-empty')].map(n=>[n,n.hidden]);root.querySelectorAll('[data-pf-item],[data-pf-group],.pf-map-view').forEach(n=>n.hidden=false);root.querySelector('.pf-unknown').hidden=!root.querySelector('.pf-unknown [data-pf-item]');root.querySelector('.pf-result-view').hidden=true;root.querySelector('.pf-empty').hidden=true;});window.addEventListener('afterprint',()=>{if(!printHidden)return;printHidden.forEach(([n,hidden])=>n.hidden=hidden);filter();printHidden=null;});\n"
        ' // Global hash navigation opens both disclosure levels, even on repeated clicks.\n'
        '})();\n'
    ),
    'presence.css': (
        '#briefing-regional-presence{color:#193445;min-width:0}\n'
        '#briefing-regional-presence .rp-intro,#briefing-regional-presence .rp-caption{font-size:12px;color:#526a79;margin:0 0 14px}\n'
        '#briefing-regional-presence .rp-row{display:grid;grid-template-columns:minmax(180px,1.1fr) minmax(180px,1.5fr) 220px;align-items:center;gap:20px;padding:13px 10px;border-bottom:1px solid #dce5ea;color:#193445;text-decoration:none;font-size:14px}\n'
        '#briefing-regional-presence .rp-row:hover,#briefing-regional-presence .rp-row[aria-current=true]{background:#edf3f6}\n'
        '#briefing-regional-presence .rp-row.rp-focus{background:#fff6e8;border-left:3px solid #c3872d;padding-left:7px}\n'
        '#briefing-regional-presence .rp-row strong{line-height:1.4;overflow-wrap:anywhere}\n'
        '#briefing-regional-presence .rp-type{color:#526a79;font-size:13px;overflow-wrap:anywhere}\n'
        '#briefing-regional-presence .rp-type small{font-size:11px;line-height:1.45;margin-top:4px;color:#526a79}\n'
        '#briefing-regional-presence .rp-score{display:flex;gap:13px;align-items:center;justify-content:flex-end}\n'
        '#briefing-regional-presence .rp-dots{display:flex;gap:7px}\n'
        '#briefing-regional-presence .rp-dot{display:block;width:16px;height:16px;border:1px solid #a9bbc4;border-radius:50%;background:transparent;flex:none}\n'
        '#briefing-regional-presence .rp-dot.rp-filled{background:#154c61;border-color:#154c61}\n'
        '#briefing-regional-presence .rp-focus .rp-filled{background:#c3872d;border-color:#c3872d}\n'
        '#briefing-regional-presence .rp-score b{font-size:13px;white-space:nowrap;font-variant-numeric:tabular-nums}\n'
        '#briefing-regional-presence .rp-score>span:last-child{color:#526a79}\n'
        '#briefing-regional-presence .rp-caption{margin:13px 0 18px}\n'
        '#briefing-regional-presence .rp-method{font-size:12px;color:#526a79;margin-bottom:22px}\n'
        '#briefing-regional-presence .rp-method>summary{color:#154c61;font-weight:600}\n'
        '#briefing-regional-presence .rp-method ol{padding-left:24px}\n'
        '#briefing-regional-presence .rp-method li{padding:5px 0}\n'
        '#briefing-regional-presence .rp-profiles h3{font-size:17px;margin:0 0 12px}\n'
        '#briefing-regional-presence .rp-profile{border:1px solid #dce5ea;border-radius:8px;margin:10px 0;scroll-margin-top:85px}\n'
        '#briefing-regional-presence .rp-profile>summary{display:flex;justify-content:space-between;gap:14px;align-items:center;padding:12px 15px;color:#154c61;font-size:13px;line-height:1.5}\n'
        '#briefing-regional-presence .rp-profile>summary>span{font-size:12px;color:#526a79}\n'
        "#briefing-regional-presence .rp-profile>summary::after{content:'⌄';color:#154c61}\n"
        '#briefing-regional-presence .rp-profile[open]{border-left:3px solid #c3872d}\n'
        '#briefing-regional-presence .rp-profile-body{padding:4px 16px 16px;font-size:13px;line-height:1.55}\n'
        '#briefing-regional-presence .rp-profile-body h4{font-size:14px;color:#154c61;margin:16px 0 8px}\n'
        '#briefing-regional-presence .rp-activity{background:#f3f7f9;border-left:2px solid #dce5ea;padding:11px 13px;margin:10px 0}\n'
        '#briefing-regional-presence .rp-activity p{margin:5px 0}\n'
        '#briefing-regional-presence .rp-source-fact{border-top:1px solid #dce5ea;padding:11px 0;font-size:12px}\n'
        '#briefing-regional-presence .rp-source-fact>summary{font-weight:600;line-height:1.5;color:#154c61}\n'
        '#briefing-regional-presence .rp-source-fact .evidence{padding-left:20px}\n'
        '#briefing-regional-presence .rp-source-fact .evidence li{background:#f3f7f9;padding:10px 12px;margin:8px 0}\n'
        '#briefing-regional-presence .rp-source-fact p{font-size:12px;margin:7px 0}\n'
        '#briefing-regional-presence .rp-empty{font-size:12px;color:#526a79}\n'
        '@media print{\n'
        ' #briefing-regional-presence .rp-row{grid-template-columns:1.1fr 1.5fr 160px;gap:10px;padding:8px 5px;break-inside:avoid}\n'
        ' #briefing-regional-presence .rp-dot{width:12px;height:12px;print-color-adjust:exact;-webkit-print-color-adjust:exact}\n'
        ' #briefing-regional-presence .rp-dots{gap:4px}\n'
        ' #briefing-regional-presence .rp-profile{break-inside:auto}\n'
        '}\n'
    ),
    'presence.js': (
        '(()=>{\n'
        " const root=document.getElementById('briefing-regional-presence');if(!root)return;\n"
        " const links=[...root.querySelectorAll('.rp-row')],profiles=[...root.querySelectorAll('.rp-profile')];\n"
        " root.addEventListener('click',event=>{\n"
        "  const link=event.target.closest('.rp-row');if(!link||!root.contains(link))return;\n"
        "  const target=document.getElementById(link.getAttribute('href').slice(1));if(!target)return;\n"
        '  event.preventDefault();event.stopPropagation();profiles.forEach(profile=>profile.open=profile===target);\n'
        "  links.forEach(row=>{if(row===link)row.setAttribute('aria-current','true');else row.removeAttribute('aria-current');});\n"
        "  target.scrollIntoView({block:'start',behavior:'smooth'});\n"
        ' });\n'
        '})();\n'
    ),
    'profile.css': (
        '.person-profile{--pp-ink:#172d3b;--pp-muted:#617380;--pp-line:#dce5e9;--pp-accent:#176274;color:var(--pp-ink);font:14px/1.55 Arial,Helvetica,sans-serif}\n'
        '\n'
        '/* Use the shared briefing hierarchy inside each professional profile module. */\n'
        '.profile-module .person-profile{--pp-ink:#173345;--pp-muted:#607887;--pp-line:#dbe4e8;--pp-accent:#154c61;font:inherit}\n'
        '.profile-module .person-profile h2{font-size:24px;line-height:1.3}\n'
        '.profile-module .person-profile h3{font-size:17px;line-height:1.4;margin-bottom:14px}\n'
        '.profile-module .pp-tag{font-size:11px;letter-spacing:.07em}\n'
        '.profile-module .pp-meta{font-size:12px}\n'
        '.profile-module .person-profile .pp-intro{margin:16px 0 20px;max-width:none;line-height:1.55}\n'
        '.profile-module .pp-head{padding-bottom:14px}\n'
        '.profile-module .pp-block{margin-top:24px}\n'
        '.profile-module .pp-snapshot{padding:16px 18px;border:1px solid var(--pp-line);border-left:3px solid var(--pp-accent);border-radius:9px;background:#f7fafb}\n'
        '.profile-module .pp-snapshot dl>div{padding:12px 16px 12px 0;min-height:0}\n'
        '.profile-module .pp-snapshot dt{font-size:11px;letter-spacing:.04em}\n'
        '.profile-module .pp-snapshot dd{font-size:14px;line-height:1.5}\n'
        '.profile-module .pp-table{border-radius:8px}\n'
        '.profile-module .person-profile table{font-size:14px}\n'
        '.profile-module .person-profile th{font-size:12px;text-transform:none;letter-spacing:0;background:#eef4f6;padding:12px}\n'
        '.profile-module .person-profile td{padding:12px}\n'
        '.profile-module .pp-cols{gap:14px}\n'
        '.profile-module .pp-cols .pp-block{padding:16px 18px;border-radius:9px;background:#f7fafb}\n'
        '.profile-module .person-profile li{font-size:14px;line-height:1.55}\n'
        '.profile-module .pp-empty{font-size:13px}\n'
        '.person-profile *{box-sizing:border-box}.person-profile p{margin:0}.person-profile h2{border:0;font-size:26px;margin:0}.person-profile h3{font-size:15px;margin:0 0 15px}.pp-head{display:flex;justify-content:space-between;gap:20px;border-bottom:1px solid var(--pp-line);padding-bottom:17px}.pp-tag{font-size:10px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:var(--pp-accent);margin-bottom:6px!important}.pp-meta{text-align:right;font-size:11px;color:var(--pp-muted)}.person-profile .pp-intro{margin:19px 0 23px;max-width:1050px;line-height:1.65}.pp-block{margin-top:25px}.pp-num{display:inline-flex;align-items:center;justify-content:center;background:var(--pp-accent);color:#fff;font-size:10px;width:21px;height:21px;border-radius:3px;margin-right:8px}.pp-snapshot{padding:19px 22px 16px;border:1px solid #cfdee4;border-left:4px solid var(--pp-accent);background:#f2f6f7;border-radius:0 5px 5px 0}.pp-snapshot dl{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:0;gap:0}.pp-snapshot dl>div{padding:11px 15px 11px 0;min-height:72px}.pp-snapshot dl>div:nth-child(n+4){border-top:1px solid #d5e1e5}.pp-snapshot dt{font-size:10px;color:var(--pp-muted);text-transform:uppercase;letter-spacing:.6px;margin-bottom:5px}.pp-snapshot dd{font-size:13px;font-weight:600;margin:0;overflow-wrap:anywhere}.pp-table{overflow-x:auto;border:1px solid var(--pp-line);border-radius:5px}.person-profile table{width:100%;border-collapse:collapse;text-align:left;table-layout:fixed;font-size:12px}.person-profile th{background:#f2f6f7;color:var(--pp-muted);font-size:9px;text-transform:uppercase;letter-spacing:.65px;padding:9px 12px}.person-profile td{padding:11px 12px;vertical-align:top;border-top:1px solid var(--pp-line);overflow-wrap:anywhere}.person-profile th:first-child{width:16%}.person-profile th:nth-child(2){width:23%}.person-profile th:nth-child(3){width:25%}.person-profile td:first-child{border-left:2px solid #bed2d9;color:var(--pp-accent);font-weight:700}.person-profile td:nth-child(2){font-weight:700}.pp-cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}.pp-cols .pp-block{padding:19px 20px 16px;border:1px solid var(--pp-line);border-radius:5px}.person-profile ul{list-style:none;margin:0;padding:0}.person-profile li{padding:10px 0;border-top:1px solid var(--pp-line);font-size:12px}.person-profile li:first-child{border:0;padding-top:0}.person-profile li strong{color:var(--pp-accent)}.person-profile a{color:var(--pp-accent);text-decoration:none}.person-profile a:hover{text-decoration:underline}.person-profile sup{font-size:9px;margin-left:3px;white-space:nowrap}.pp-note{padding:13px 17px;background:#f7f5ef;border:1px solid #e7e0d2;border-left:3px solid #a38a57;border-radius:0 4px 4px 0;margin-top:23px;font-size:12px}.pp-note>strong{font-size:10px;text-transform:uppercase;color:#79643e}.pp-empty{color:var(--pp-muted);font-size:12px}.pp-sources{margin-top:25px;padding-top:15px;border-top:1px solid var(--pp-line);font-size:10px;color:var(--pp-muted)}.pp-sources p{margin:0 0 9px}.pp-evidence{margin-top:18px;border-top:1px solid var(--pp-line);padding-top:14px}.person-profile [id]{scroll-margin-top:90px}.person-profile :target{background:#fff3cf}.person-profile a:focus-visible{outline:2px solid var(--pp-accent);outline-offset:3px}@media print{.pp-snapshot,.pp-note,.pp-cols .pp-block,.person-profile tr{break-inside:avoid}.pp-num{print-color-adjust:exact}}\n'
        '\n'
        '.profile-media .pm-head{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:15px}\n'
        '.profile-media .pm-window{font-size:12px;color:#607887;margin:0}\n'
        '.profile-media .pm-legend{display:flex;gap:7px;flex-wrap:wrap}\n'
        '.profile-media .pm-tag{font-size:10px;font-weight:650;padding:4px 8px;border-radius:5px;background:var(--pm-bg);color:var(--pm-color)}\n'
        '.profile-media .pm-own{--pm-color:#245c9a;--pm-bg:#eef5ff}\n'
        '.profile-media .pm-official{--pm-color:#197456;--pm-bg:#ecf7f0}\n'
        '.profile-media .pm-media{--pm-color:#8053a3;--pm-bg:#f4eef9}\n'
        '.profile-media .pm-entry{width:100%;min-width:0;border:1px solid #dce5eb;border-left:3px solid var(--pm-color);border-radius:8px;background:#fff;overflow:hidden}\n'
        '.profile-media .pm-entry>summary{position:relative;display:block;list-style:none;padding:11px 34px 11px 14px;cursor:pointer}\n'
        '.profile-media .pm-entry>summary::-webkit-details-marker{display:none}\n'
        '.profile-media .pm-entry>summary:hover,.profile-media .pm-entry[open]>summary{background:var(--pm-bg)}\n'
        '.profile-media .pm-kicker{display:block;color:var(--pm-color);font-size:10px;font-weight:700;margin-bottom:4px}\n'
        '.profile-media .pm-title{display:block;font-size:14px;line-height:1.4;font-weight:700}\n'
        '.profile-media .pm-preview{display:block;font-size:12px;color:#526d7c;margin-top:4px;line-height:1.45}\n'
        '.profile-media .pm-publisher{display:block;font-size:10px;color:#7a8c96;margin-top:5px}\n'
        '.profile-media .pm-arrow{position:absolute;right:13px;top:13px;color:var(--pm-color)}\n'
        '.profile-media .pm-entry[open] .pm-arrow{transform:rotate(180deg)}\n'
        '.profile-media .pm-body{border-top:1px solid #dce5eb;padding:8px 16px 15px;font-size:13px;line-height:1.6}\n'
        '.profile-media .pm-body h4{font-size:12px;margin:14px 0 6px}\n'
        '.profile-media blockquote{margin:12px 0;padding:9px 13px;border-left:3px solid var(--pm-color);background:var(--pm-bg);color:#304c60}\n'
        '.profile-media .pm-limit{font-size:12px;color:#607887}\n'
        '.profile-media .pm-note{font-size:11px;color:#708491;margin-top:13px}\n'
        '@media(max-width:650px){.profile-media .pm-event{grid-template-columns:1fr;gap:5px}.profile-media .pm-event time{padding-top:0}.profile-media .pm-timeline{padding-left:12px}}\n'
        '@media print{.profile-media .pm-entry{break-inside:avoid}}\n'
    ),
}


def vorlage(name):
    """Text einer Vorlage, z. B. vorlage("portfolio.css")."""
    return VORLAGEN[name]
