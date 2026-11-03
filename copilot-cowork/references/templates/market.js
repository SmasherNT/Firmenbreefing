(()=>{
 const root=document.getElementById('briefing-market');if(!root)return;
 const records=new Map([...root.querySelectorAll('.mk-country-record')].map(n=>[n.id.replace('market-country-',''),n]));
 const picks=[...root.querySelectorAll('.mk-pick')],detail=root.querySelector('.mk-detail');
 if(!records.size||picks.some(n=>!records.has(n.dataset.mkCountry)))return;
 const sections=[['programmes','Programme & Zeitfenster'],['industry','Industrie & Marktzugang'],['data','Werte, Methode & Quellen']];
 let country=records.keys().next().value,tab='programmes',selectedFunction=null;
 function el(tag,parent,text,cls){const node=document.createElement(tag);if(text!==undefined)node.textContent=text;if(cls)node.className=cls;parent.appendChild(node);return node;}
 function activate(id,focus=false){
  tab=id;detail.querySelectorAll('.mk-tab').forEach(b=>{b.setAttribute('aria-selected',String(b.dataset.mkTab===tab));b.tabIndex=b.dataset.mkTab===tab?0:-1;});
  detail.querySelectorAll('.mk-tab-body').forEach(n=>n.hidden=n.dataset.mkSection!==tab);
  if(focus)detail.querySelector('[data-mk-tab="'+tab+'"]').focus();
 }
 function select(id,section=tab,functionId=null,scroll=false){
  country=id;tab=section;selectedFunction=functionId;const record=records.get(id);
  detail.replaceChildren();detail.hidden=false;
  const head=el('div',detail,undefined,'mk-detail-header'),title=el('div',head);
  el('span',title,'Land im Detail','mk-kicker');el('h3',title,record.dataset.mkLabel);
  const nav=el('div',detail,undefined,'mk-country-nav');nav.setAttribute('aria-label','Land auswählen');
  records.forEach((r,key)=>{const b=el('button',nav,r.dataset.mkLabel,'mk-country-button');b.type='button';b.dataset.mkSelect=key;b.setAttribute('aria-pressed',String(key===country));});
  detail.appendChild(record.querySelector('.mk-coverage').cloneNode(true));
  const tabs=el('div',detail,undefined,'mk-tabs');tabs.setAttribute('role','tablist');tabs.setAttribute('aria-label','Länderdetails');
  sections.forEach(([key,label])=>{const b=el('button',tabs,label,'mk-tab');b.type='button';b.dataset.mkTab=key;b.id='mk-tab-'+key;b.setAttribute('role','tab');b.setAttribute('aria-controls','mk-panel-'+key);});
  record.querySelectorAll('.mk-tab-body').forEach(n=>{const copy=n.cloneNode(true);copy.id='mk-panel-'+copy.dataset.mkSection;copy.setAttribute('role','tabpanel');copy.setAttribute('aria-labelledby','mk-tab-'+copy.dataset.mkSection);copy.querySelectorAll('[data-mk-function-detail]').forEach(f=>f.classList.toggle('mk-selected',f.dataset.mkFunctionDetail===selectedFunction));detail.appendChild(copy);});
  picks.forEach(n=>n.setAttribute('aria-pressed',String(n.dataset.mkCountry===country&&(!n.dataset.mkFunction||n.dataset.mkFunction===selectedFunction))));
  activate(tab);
  if(scroll)detail.scrollIntoView({block:'start',behavior:'smooth'});
 }
 root.addEventListener('click',event=>{
  const pick=event.target.closest('.mk-pick');if(pick&&root.contains(pick)){event.preventDefault();event.stopPropagation();select(pick.dataset.mkCountry,pick.dataset.mkFunction?'industry':'programmes',pick.dataset.mkFunction||null,true);return;}
  const countryButton=event.target.closest('[data-mk-select]');if(countryButton){select(countryButton.dataset.mkSelect);return;}
  const tabButton=event.target.closest('[data-mk-tab]');if(tabButton)activate(tabButton.dataset.mkTab);
 });
 root.addEventListener('keydown',event=>{
  const pick=event.target.closest('.mk-pick');if(pick&&event.key===' '){event.preventDefault();select(pick.dataset.mkCountry,pick.dataset.mkFunction?'industry':'programmes',pick.dataset.mkFunction||null,true);return;}
  const button=event.target.closest('[data-mk-tab]');if(!button||!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;
  event.preventDefault();const keys=sections.map(s=>s[0]),i=keys.indexOf(tab);activate(keys[event.key==='Home'?0:event.key==='End'?keys.length-1:(i+(event.key==='ArrowRight'?1:-1)+keys.length)%keys.length],true);
 });
 picks.forEach(n=>n.setAttribute('role','button'));select(country);root.classList.add('mk-enhanced');
})();
