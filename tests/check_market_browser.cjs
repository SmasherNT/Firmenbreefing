// Offline desktop checks for the synthetic market dataset; no source research.
const assert=require('node:assert/strict'),path=require('node:path');
const {pathToFileURL}=require('node:url'),{chromium}=require('playwright-core');
(async()=>{
 assert(process.argv[2]&&process.env.BRIEFING_CHROMIUM_PATH,'Pass HTML and set BRIEFING_CHROMIUM_PATH');
 const browser=await chromium.launch({executablePath:process.env.BRIEFING_CHROMIUM_PATH,headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
 const errors=[];
 try{
  const context=await browser.newContext({offline:true,viewport:{width:1440,height:1100}}),page=await context.newPage();
  page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
  await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);await page.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  await page.locator('[data-page=page-regions]').click();const root=page.locator('#briefing-market');
  assert(await root.isVisible());assert.equal(await root.locator('.mk-panel').count(),4);
  assert.equal(await root.locator('.mk-industry .mk-role').count(),9);assert.equal(await root.locator('.mk-country-record').count(),3);
  assert.equal(await root.locator('.mk-pipeline .mk-bar-row').count(),3);
  assert.deepEqual(await root.locator('[data-mk-chart=value] .mk-value').allTextContents(),['30,0Ist / berichtet','10,0Ist / berichtet','—']);
  assert.deepEqual(await root.locator('[data-mk-chart=growth] .mk-value').allTextContents(),['10,7 %','-9,6 %','—']);
  assert.deepEqual(await root.locator('.mk-pipeline .mk-value').allTextContents(),['4','2','—']);
  const north=root.locator('.mk-pipeline [data-mk-country=north]');assert.deepEqual(await north.locator('.mk-segment').allTextContents(),['1','1','1','1']);
  const negative=root.locator('.mk-growth-negative');assert(await negative.evaluate(n=>{const left=parseFloat(n.style.left),width=parseFloat(n.style.width),zero=parseFloat(n.parentElement.querySelector('.mk-zero').style.left);return left<zero&&width>0&&Math.abs(left+width-zero)<0.001;}));
  for(const width of [1440,1280,1024]){
   await page.setViewportSize({width,height:1100});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Only local horizontal scrolling');
   const panels=await root.locator('.mk-panel').evaluateAll(ns=>ns.map(n=>{const r=n.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width};}));
   assert.equal(panels[0].y,panels[1].y);assert.equal(panels[0].w,panels[1].w);assert(panels[1].x>panels[0].x);assert(panels[2].w>panels[0].w);
   assert(await root.locator('.mk-role').evaluateAll(ns=>ns.every(n=>n.scrollHeight<=n.clientHeight+1)),'No clipped role labels');
  }
  await page.setViewportSize({width:1440,height:1100});
  await root.locator('[data-mk-chart=value] [data-mk-country=south]').focus();await page.keyboard.press('Enter');
  assert.equal(await page.locator('dialog[open]').count(),0);assert.equal(await root.locator('.mk-detail h3').innerText(),'Testland Süd');
  assert.equal(await root.locator('.mk-detail .mk-program').count(),2);
  await root.locator('.mk-detail .mk-program>summary').first().click();await root.locator('.mk-detail .mk-program .mk-fact>summary').first().click();
  assert(await root.locator('.mk-detail .mk-program .evidence a').first().isVisible());
  assert((await root.locator('.mk-detail .mk-program[open]').innerText()).includes('Genehmigungsobergrenze: 0,6'));
  const window=root.locator('.mk-detail .mk-window-bar').first();assert.deepEqual(await window.evaluate(n=>[parseFloat(n.style.left),parseFloat(n.style.width)]),[0,60]);
  await root.locator('[data-mk-country=north][data-mk-function=integration]').click();
  assert.equal(await root.locator('.mk-tab[aria-selected=true]').innerText(),'Industrie & Marktzugang');
  assert.equal(await root.locator('.mk-function.mk-selected').count(),1);assert((await root.locator('.mk-function.mk-selected').innerText()).includes('Lizenzfertigung'));
  await root.locator('.mk-detail [data-mk-tab=data]').click();assert.equal(await root.locator('.mk-detail .mk-data-table tbody tr').count(),5);
  await root.locator('.mk-detail .mk-data-table .mk-fact>summary').first().click();assert(await root.locator('.mk-detail .mk-data-table .evidence a').first().isVisible());
  await root.locator('.mk-detail .mk-data-table a.claim').first().click();assert(await page.locator('#page-sources').isVisible());
  await page.locator('[data-page=page-regions]').click();assert.equal(await root.locator('.mk-tab[aria-selected=true]').innerText(),'Werte, Methode & Quellen');
  await root.locator('.mk-detail [data-mk-select=east]').click();assert((await root.locator('.mk-detail .mk-data-table').innerText()).includes('Im fiktiven Datensatz nicht belegt'));
  await root.locator('.mk-detail [data-mk-tab=industry]').focus();await page.keyboard.press('Home');assert.equal(await root.locator('.mk-tab[aria-selected=true]').getAttribute('data-mk-tab'),'programmes');
  assert((await root.locator('.mk-detail').innerText()).includes('Keine freigegebenen Programme'));
  await root.locator('[data-mk-country=east][data-mk-function=sensors]').focus();await page.keyboard.press('Space');assert((await root.locator('.mk-function.mk-selected').innerText()).includes('Beleg offen'));
  await page.waitForTimeout(350);assert(await page.evaluate(()=>window.scrollY>0),'Drilldown scrolls to detail');
  const before=await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open));
  await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));await page.emulateMedia({media:'print'});
  assert(await root.locator('.mk-fallback').isVisible());assert.equal(await root.locator('.mk-country-record:visible').count(),3);
  assert.equal(await root.locator('.mk-fallback .mk-program[open]').count(),6);assert.equal(await root.locator('.mk-detail:visible').count(),0);
  await page.emulateMedia({media:'screen'});await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
  assert.deepEqual(await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open)),before);
  assert.equal(await root.locator('.mk-detail h3').innerText(),'Testland Ost');assert.equal(await root.locator('.mk-fallback:visible').count(),0);
  if(process.env.BRIEFING_QA_DIR){await page.locator('[data-page=page-regions]').click();await page.screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'market-overview.png'),fullPage:true});await root.locator('.mk-detail [data-mk-select=north]').click();await root.locator('.mk-detail [data-mk-tab=programmes]').click();await root.locator('.mk-detail').screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'market-detail.png')});}
  await context.close();
  const fallback=await browser.newContext({offline:true,javaScriptEnabled:false,viewport:{width:1280,height:1000}}),fp=await fallback.newPage();await fp.goto(pathToFileURL(path.resolve(process.argv[2])).href);
  assert.equal(await fp.locator('.page:visible').count(),4);assert.equal(await fp.locator('#briefing-market .mk-country-record:visible').count(),3);
  await fp.locator('#market-country-north .mk-program>summary').first().click();await fp.locator('#market-country-north .mk-program .mk-fact>summary').first().click();
  assert(await fp.locator('#market-country-north .mk-program .evidence a').first().isVisible());await fallback.close();
  assert.deepEqual(errors,[]);console.log(JSON.stringify({countries:3,programmes:6,functions:3,widths:[1440,1280,1024],comparison:'passed',drilldown:'passed',keyboard:'passed',sources:'passed',print:'passed',noJavaScript:'passed',errors}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
