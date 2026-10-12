(()=>{
 const root=document.getElementById('briefing-capability-matrix');
 if(!root)return;
 const cells=[...root.querySelectorAll('.cm-cell')],columns=[...root.querySelectorAll('.cm-column')],
       records=new Map([...root.querySelectorAll('.cm-record')].map(n=>[n.id,n])),detail=root.querySelector('.cm-detail');
 if(!cells.length||cells.some(c=>!records.has(c.dataset.cmRecord)))return;
 // Keep the static evaluations in the document for sources, print and no-JS use.
 let active=null,compare=false;
 function el(tag,parent,text,cls){const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;if(parent)parent.appendChild(n);return n;}
 function copyBody(cell){return records.get(cell.dataset.cmRecord).querySelector('.cm-record-body').cloneNode(true);}
 function pick(cell,all=false){
  active=cell;compare=all;const record=records.get(cell.dataset.cmRecord),col=cell.dataset.cmCol;
  detail.hidden=false;detail.replaceChildren();
  const head=el('div',detail,undefined,'cm-detail-head'),title=el('div',head);
  el('span',title,compare?'Vergleich nach gemeinsamem Kriterium':'Bewertung im Detail','cm-kicker');
  const criterion=columns[+col].querySelector('span').firstChild.textContent.trim();
  el('h3',title,compare?criterion:record.dataset.cmName+' · '+criterion);
  if(!compare&&record.dataset.cmOffer)el('small',title,record.dataset.cmOffer,'cm-system');
  const button=el('button',head,compare?'Einzelbewertung öffnen':'Alle Wettbewerber vergleichen','cm-action');button.type='button';button.addEventListener('click',()=>pick(active,!compare));
  cells.forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.cmCol===col&&(compare||c===cell))));
  columns.forEach((b,i)=>b.setAttribute('aria-pressed',String(compare&&String(i)===col)));
  if(!compare){detail.appendChild(copyBody(cell));return;}
  const scroll=el('div',detail,undefined,'cm-scroll'),table=el('table',scroll,undefined,'cm-comparison');
  table.setAttribute('aria-label',columns[+col].getAttribute('aria-label'));
  const headings=el('tr',el('thead',table));['Unternehmen','Öffentlicher Nachweis','Einordnung, Grenzen & Quellen'].forEach(text=>el('th',headings,text));
  const tbody=el('tbody',table);
  cells.filter(c=>c.dataset.cmCol===col).forEach(c=>{
   const r=records.get(c.dataset.cmRecord),tr=el('tr',tbody),actor=el('td',tr),select=el('button',actor,r.dataset.cmName,'cm-action cm-compare-company');select.type='button';select.addEventListener('click',()=>pick(c));
   if(r.dataset.cmOffer)el('small',actor,r.dataset.cmOffer,'cm-system');
   if(c.closest('.cm-reference'))el('span',actor,'Referenz','cm-reference-label');
   const copy=copyBody(c),outcome=copy.querySelector('.cm-outcome');el('td',tr).appendChild(outcome);const context=el('td',tr);
   const facts=copy.querySelector('.cm-facts');facts.remove();context.appendChild(copy);
   const disclosure=el('details',context,undefined,'cm-compare-facts'),count=Number(r.dataset.cmSourceCount);
   el('summary',disclosure,'Faktenbasis'+(count?' · '+count+(count===1?' Quelle':' Quellen'):''));disclosure.appendChild(facts);
  });
 }
 root.addEventListener('click',event=>{
  const cell=event.target.closest('.cm-cell');if(!cell||!root.contains(cell))return;
  event.preventDefault();event.stopPropagation();pick(cell);
 });
 cells.forEach(cell=>cell.setAttribute('role','button'));
 root.addEventListener('keydown',event=>{const cell=event.target.closest('.cm-cell');if(cell&&event.key===' '){event.preventDefault();pick(cell);}});
 columns.forEach((b,i)=>{b.disabled=false;b.addEventListener('click',()=>pick(cells.find(c=>c.dataset.cmCol===String(i)&&c.dataset.cmRow===active.dataset.cmRow),true));});
 root.style.setProperty('--cm-table-width',Math.max(760,172+columns.length*155)+'px');
 const reference=cells.filter(c=>c.closest('.cm-reference')),initial=reference.find(c=>c.dataset.cmKind==='evidence')||reference[0]||cells.find(c=>c.dataset.cmKind==='evidence')||cells[0];
 pick(initial);root.classList.add('cm-enhanced');
 // Measure complete text at the available column width; never clamp the summaries.
 let lastWidth=0;
 function fit(){const width=root.querySelector('.cm-matrix').getBoundingClientRect().width;if(Math.abs(width-lastWidth)<1)return;lastWidth=width;root.style.removeProperty('--cm-cell-height');const height=Math.ceil(Math.max(136,...cells.map(c=>c.getBoundingClientRect().height)));root.style.setProperty('--cm-cell-height',height+'px');}
 fit();if(typeof ResizeObserver!=='undefined')new ResizeObserver(fit).observe(root.querySelector('.cm-scroll'));
})();
