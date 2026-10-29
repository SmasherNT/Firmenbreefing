// Desktop/offline QA with synthetic data. Requires playwright-core and Chromium.
const assert=require('node:assert/strict'),path=require('node:path');
const {pathToFileURL}=require('node:url'),{chromium}=require('playwright-core');
(async()=>{
 assert(process.argv[2]&&process.env.BRIEFING_CHROMIUM_PATH,'Pass HTML and set BRIEFING_CHROMIUM_PATH');
 const browser=await chromium.launch({executablePath:process.env.BRIEFING_CHROMIUM_PATH,headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});const errors=[];
 try{
  const context=await browser.newContext({offline:true,viewport:{width:1440,height:1000}});
  const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
  await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);await page.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  assert.deepEqual(await page.locator('.page').evaluateAll(n=>n.map(p=>p.id)),['page-main','page-profile','page-regions','page-sources']);
  for(const width of [1440,1280,1024]){
   await page.setViewportSize({width,height:1000});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Only local scrolling');
   const boxes=await page.locator('#page-main>.module').evaluateAll(ns=>ns.map(n=>{const r=n.getBoundingClientRect();return {left:r.left,top:r.top,bottom:r.bottom};}));
   assert(boxes.every((b,i)=>i===0||b.top>=boxes[i-1].bottom),'Modules vertically stacked');assert(boxes.every(b=>Math.abs(b.left-boxes[0].left)<1),'Full-width alignment');
   assert.equal(await page.locator('#portfolio-profiles').evaluate(n=>n.open),false);assert.equal(await page.locator('.pf-profile-content:visible').count(),0);
  }
  await page.setViewportSize({width:1440,height:1000});assert.equal(await page.locator('.pf-maturity-map thead th').count(),6);assert.equal(await page.locator('.pf-maturity-map .pf-map-item').count(),3);assert.equal(await page.locator('.pf-unknown-cell .pf-map-item').count(),1);assert.equal(await page.locator('.pf-unknown .pf-map-item').count(),0);
  await page.locator('[data-pf-filter=query]').fill('sensor');assert.equal(await page.locator('.pf-map-item:visible').count(),1);await page.locator('.pf-reset').click();
  await page.locator('[data-pf-filter=grade]').selectOption('unknown');assert.equal(await page.locator('.pf-map-item:visible').count(),1);assert.equal(await page.locator('.pf-unknown-cell .pf-map-item:visible').count(),1);await page.locator('.pf-reset').click();
  await page.locator('[data-pf-filter=origin]').selectOption('Partnerangabe');assert.equal(await page.locator('.pf-map-item:visible').count(),1);await page.locator('.pf-reset').click();
  await page.locator('[data-pf-view=table]').click();assert.equal(await page.locator('[data-pf-result]:visible').count(),3);await page.locator('[data-pf-view=map]').click();
  await page.locator('.pf-map-item[href="#product-kit"]').click();await page.waitForFunction(()=>document.getElementById('product-kit').open);assert(await page.locator('#portfolio-profiles').evaluate(n=>n.open));assert((await page.locator('#product-kit .evidence a').first().getAttribute('href')).startsWith('https://'));
  await page.locator('#portfolio-profiles>.pf-head').click();await page.locator('.pf-map-item[href="#product-kit"]').click();await page.waitForFunction(()=>document.getElementById('portfolio-profiles').open);
  await page.locator('.pf-expand').click();assert(await page.locator('.pf-profile').evaluateAll(ns=>ns.every(n=>n.open)));await page.locator('.pf-expand').click();await page.locator('#portfolio-profiles>.pf-head').click();
  const network=page.locator('#briefing-company-network');assert(await network.locator('#cnt-view-tables').isVisible());assert.equal(await network.locator('.cnt-actor-table').count(),4);await network.locator('#cnt-tab-graph').click();const expected=await network.locator('.cn-data').evaluate(n=>JSON.parse(n.textContent));
  assert.equal(await network.locator('.cn-node').count(),expected.nodes.length);assert.equal(await network.locator('.cn-hit').count(),new Set(expected.edges.map(e=>[e.from,e.to].sort().join('|'))).size);assert.equal(await network.locator('.cn-table tbody tr').count(),expected.edges.length);
  const board=await network.locator('.cn-board').boundingBox(),sidebar=await network.locator('.cn-sidebar').boundingBox();assert(sidebar.y>=board.y+board.height||sidebar.x>=board.x+board.width);
  assert(await network.locator('.cn-line').evaluateAll(ns=>ns.every(n=>/^M [-.\d]+ [-.\d]+ Q [-.\d]+ [-.\d]+ [-.\d]+ [-.\d]+$/.test(n.getAttribute('d'))&&n.getAttribute('marker-end')==='url(#cn-arrow)')),'Curved connections with arrows');
  assert.equal(await network.locator('.cn-svg circle:not(.cn-node circle)').count(),0);
  const areas=await network.locator('.cn-area').evaluateAll(ns=>ns.map(n=>({id:n.dataset.clusterArea,x:+n.getAttribute('x'),y:+n.getAttribute('y'),height:+n.getAttribute('height')})));
  assert.deepEqual(areas.map(a=>a.id),['capital','structure','technology','market']);assert.equal(areas[0].y,areas[1].y);assert.equal(areas[2].y,areas[3].y);assert.equal(areas[0].height,areas[1].height);assert.equal(areas[2].height,areas[3].height);assert(areas[0].x<areas[1].x&&areas[2].x<areas[3].x&&areas[0].y<areas[2].y);
  assert(await network.locator('.cn-node').evaluateAll(ns=>ns.every(n=>n.dataset.radius==='14'&&n.querySelectorAll('.cn-symbol').length===1)),'Uniform node size, one categorical symbol');
  assert(await network.locator('.cn-node circle').evaluateAll(ns=>ns.every(n=>n.getAttribute('r')==='14')),'All circles have the same radius');
  for(const width of [1440,1280,1024]){
   await page.setViewportSize({width,height:1000});
   await page.waitForFunction(()=>{const s=document.querySelector('.cn-svg'),p=document.querySelector('.cn-plot');return Math.abs(s.viewBox.baseVal.width-Math.max(640,p.clientWidth-10))<1;});
   assert(await network.locator('.cn-svg').evaluate(s=>s.getBoundingClientRect().width<=s.parentElement.clientWidth+1),'Graph fits its field');
   assert(await network.locator('.cn-svg').evaluate(s=>{
    const areas=[...s.querySelectorAll('.cn-area')].map(a=>a.getBBox());
    return [...s.querySelectorAll('.cn-node:not([data-kind="target"])')].every(n=>{
     const b=n.getBBox(),t=n.transform.baseVal.consolidate().matrix;
     return areas.some(a=>b.x+t.e>=a.x&&b.y+t.f>=a.y&&b.x+t.e+b.width<=a.x+a.width&&b.y+t.f+b.height<=a.y+a.height);
    });
   }),'Symbols and labels stay inside cluster fields');
  }
  await page.setViewportSize({width:1440,height:1000});
  assert.equal(await network.locator('.cn-node[data-kind=owner] polygon').count(),1);assert.equal(await network.locator('.cn-node[data-kind=jv] polygon').count(),1);assert.equal(await network.locator('.cn-node[data-kind=supplier] polygon').count(),1);assert.equal(await network.locator('.cn-node[data-kind=customer] polygon').count(),1);
  assert(await network.locator('.cn-node:not([data-kind=target]) text').evaluateAll(ns=>ns.every(n=>+n.getAttribute('y')>22)),'Names below symbols');
  const grid=await network.locator('.cn-node:not([data-kind=target])').evaluateAll(ns=>ns.map(n=>({id:n.dataset.node,position:n.getAttribute('transform')})));
  assert(grid.every(n=>/^translate\([\d.]+ [\d.]+\)$/.test(n.position)),'Cluster positions are finite');
  assert(await network.locator('.cn-node text').evaluateAll(ns=>ns.every(n=>!/^\d+$/.test(n.textContent.trim()))),'No numeric score badges');
  assert((await network.locator('.cn-line').evaluateAll(ns=>new Set(ns.map(n=>getComputedStyle(n).stroke)).size))>1,'Connection colors remain visible');
  await page.evaluate(()=>window.scrollTo(0,0));await page.mouse.move(600,300);await page.mouse.wheel(0,500);await page.waitForFunction(()=>window.scrollY>100);assert(await page.evaluate(()=>!['hidden','clip'].includes(getComputedStyle(document.documentElement).overflowY)),'Normal page scrolling');
  await network.locator('.cn-node').first().focus();await page.keyboard.press('Enter');assert(await network.locator('.cn-sidebar').isVisible());await network.locator('.cn-relation').first().click();assert(await network.locator('.cn-detail-content a[href^="https:"]').count());assert.equal(await page.locator('dialog[open]').count(),0);
  await network.locator('.cn-hit[data-edge=eC2]').evaluate(n=>n.dispatchEvent(new MouseEvent('click',{bubbles:true})));assert.equal(await network.locator('.cn-relation').count(),2);await network.locator('.cn-relation').last().click();assert((await network.locator('.cn-detail-content').innerText()).includes('Integrationsgegenstand'));
  await network.locator('.cn-search').fill('no such actor');assert.equal(await network.locator('.cn-hit').count(),0);assert((await network.locator('.cn-detail-content').innerText()).includes('Wähle'));await network.locator('.cn-reset').click();
  await page.locator('#topic-0 .topic-card>summary').first().click();assert(await page.locator('#es-dialog').evaluate(n=>n.open));assert(await page.locator('#es-dialog .evidence a').count());await page.keyboard.press('Escape');
  const colors=await page.locator('.quadrant').evaluateAll(ns=>ns.map(n=>getComputedStyle(n).backgroundColor));assert.equal(new Set(colors).size,4);assert.deepEqual(await page.locator('.quadrant').evaluateAll(ns=>ns.map(n=>n.dataset.swot)),['Strengths','Weaknesses','Opportunities','Threats']);
  const matrix=page.locator('#briefing-capability-matrix');assert.equal(await matrix.locator('.cm-cell').count(),4);assert.equal(await matrix.locator('.cm-record').count(),4);
  for(const width of [1440,1280,1024]){
   await page.setViewportSize({width,height:1000});await page.waitForTimeout(80);
   const sizes=await matrix.locator('.cm-cell').evaluateAll(ns=>ns.map(n=>({height:n.getBoundingClientRect().height,clipped:n.scrollHeight>n.clientHeight+2})));
   assert(sizes.every(s=>s.height===sizes[0].height&&!s.clipped),'Equal-height cells with complete summaries');assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  }
  await page.setViewportSize({width:1440,height:1000});await matrix.locator('.cm-cell').first().focus();await page.keyboard.press('Enter');assert.equal(await page.locator('dialog[open]').count(),0);assert(await matrix.locator('.cm-detail').isVisible());await matrix.locator('.cm-detail .cm-fact>summary').first().click();assert(await matrix.locator('.cm-detail .evidence a').first().isVisible());assert(await page.locator('#page-main').isVisible());await matrix.locator('.cm-cell').nth(1).focus();await page.keyboard.press('Space');assert.equal(await matrix.locator('.cm-cell').nth(1).getAttribute('aria-pressed'),'true');
  await matrix.locator('[data-cm-column="1"]').click();assert.equal(await matrix.locator('.cm-comparison tbody tr').count(),2);assert.equal(await matrix.locator('.cm-cell[aria-pressed=true]').count(),2);assert((await matrix.locator('.cm-comparison').innerText()).includes('2 / 3'));assert((await matrix.locator('.cm-comparison').innerText()).includes('3 / 3'));assert((await matrix.locator('.cm-comparison').innerText()).includes('Nächsthöhere Stufe'));
  await matrix.locator('.cm-compare-facts>summary').first().click();await matrix.locator('.cm-compare-facts .cm-fact>summary').first().click();assert(await matrix.locator('.cm-comparison .evidence a').first().isVisible());await matrix.locator('.cm-compare-company').last().click();assert((await matrix.locator('.cm-detail h3').innerText()).includes('TestPeer'));assert.equal(await matrix.locator('.cm-cell[aria-pressed=true]').count(),1);
  await matrix.locator('.cm-detail a.claim').first().click();assert(await page.locator('#page-sources').isVisible());await page.locator('[data-page=page-main]').click();assert((await matrix.locator('.cm-detail h3').innerText()).includes('TestPeer'));
  await page.locator('[data-page=page-profile]').click();assert(await page.locator('#page-profile .person-profile').isVisible());assert(await page.locator('.pp-snapshot').isVisible());assert((await page.locator('.pp-empty').first().innerText()).includes('keine freigegebenen'));await page.locator('.pp-snapshot sup a').first().click();assert(await page.locator('.pp-sources').isVisible());
  await page.locator('[data-page=page-regions]').click();assert(await page.locator('#page-regions #topic-1').isVisible());assert.equal(await page.locator('#page-main #topic-1').count(),0);
  await page.locator('[data-page=page-sources]').click();await page.locator('#source-search-input').fill('no such evidence');assert.equal(await page.locator('#page-sources .claim-detail:visible').count(),0);
  await page.locator('[data-page=page-main]').click();await page.locator('.es-card>summary').first().click();const id=(await page.locator('#es-dialog a.claim').first().getAttribute('href')).slice(1);await page.locator('#es-dialog a.claim').first().click();assert.equal(await page.locator('#source-search-input').inputValue(),'');assert(await page.locator('#'+id).isVisible());
  await page.locator('[data-page=page-main]').click();await page.locator('[data-pf-filter=query]').fill('sensor');await page.locator('[data-pf-view=table]').click();const before=await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open));
  await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));assert(await page.locator('details').evaluateAll(ns=>ns.every(n=>n.open)));assert(await page.locator('.pf-map-view').isVisible());assert.equal(await page.locator('.pf-map-item:visible').count(),3);
  await page.emulateMedia({media:'print'});assert(await matrix.locator('.cm-fallback').isVisible());assert.equal(await matrix.locator('.cm-fallback .cm-record[open]').count(),4);assert.equal(await matrix.locator('.cm-detail:visible').count(),0);await page.emulateMedia({media:'screen'});
  await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));assert.deepEqual(await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open)),before);assert(await page.locator('.pf-result-view').isVisible());assert.equal(await page.locator('[data-pf-result]:visible').count(),1);
  await page.locator('.pf-reset').click();await page.locator('[data-pf-view=map]').click();await page.locator('[data-page=page-main]').focus();await page.keyboard.press('End');assert.equal(await page.locator('.tabs [aria-selected=true]').getAttribute('data-page'),'page-sources');
  if(process.env.BRIEFING_QA_DIR){await page.locator('[data-page=page-main]').click();await page.locator('#portfolio').screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'portfolio.png')});await network.screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'network.png')});await matrix.screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'matrix.png')});}
  await context.close();const fallback=await browser.newContext({offline:true,javaScriptEnabled:false,viewport:{width:1280,height:1000}});const fp=await fallback.newPage();await fp.goto(pathToFileURL(path.resolve(process.argv[2])).href);assert.equal(await fp.locator('.page:visible').count(),4);
  await fp.locator('#portfolio-profiles>.pf-head').click();await fp.locator('#product-kit>summary').click();assert(await fp.locator('#product-kit .pf-profile-content').isVisible());await fp.locator('.cn-table>summary').click();assert.equal(await fp.locator('.cn-table tbody tr').count(),expected.edges.length);
  assert(await fp.locator('.cm-fallback').isVisible());assert.equal(await fp.locator('.cm-record').count(),4);await fp.locator('#cm-eval-I1>summary').click();await fp.locator('#cm-eval-I1 .cm-fact>summary').first().click();assert(await fp.locator('#cm-eval-I1 .evidence a').first().isVisible());await fallback.close();assert.deepEqual(errors,[]);
  console.log(JSON.stringify({pages:4,widths:[1440,1280,1024],portfolio:'passed',network:'passed',matrix:'passed',routing:'passed',print:'passed',noJavaScript:'passed',errors}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
