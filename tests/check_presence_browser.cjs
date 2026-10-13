// Offline desktop QA for the regional company-presence component.
const assert=require('node:assert/strict'),path=require('node:path');
const {pathToFileURL}=require('node:url'),{chromium}=require('playwright-core');
(async()=>{
 assert(process.argv[2]&&process.env.BRIEFING_CHROMIUM_PATH,'Pass HTML and set BRIEFING_CHROMIUM_PATH');
 const browser=await chromium.launch({executablePath:process.env.BRIEFING_CHROMIUM_PATH,headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});const errors=[];
 try{
  const context=await browser.newContext({offline:true,viewport:{width:1440,height:1100}}),page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
  await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);await page.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  const root=page.locator('#briefing-regional-presence');assert.equal(await root.evaluate(n=>n.closest('.page').id),'page-main');
  const sequence=await page.locator('#page-main>.module').evaluateAll(ns=>ns.map(n=>n.id));assert(sequence.indexOf('cluster-analysis')<sequence.indexOf('regional-presence'));assert.equal(sequence[sequence.indexOf('regional-presence')+1],'capability-matrix');
  assert.equal(await root.locator('.rp-row').count(),6);assert.equal(await root.locator('.rp-dot').count(),30);assert.equal(await root.locator('.rp-filled').count(),15);
  assert.deepEqual(await root.locator('.rp-score b').allTextContents(),['5/5','4/5','3/5','2/5','1/5','—']);assert.equal(await root.locator('.rp-profile[open]').count(),0);
  assert.equal(await root.locator('.rp-focus').count(),1);assert.equal(await root.locator('.rp-focus .rp-filled').count(),2);
  assert.notEqual(await root.locator('.rp-focus .rp-filled').first().evaluate(n=>getComputedStyle(n).backgroundColor),await root.locator('.rp-row:not(.rp-focus) .rp-filled').first().evaluate(n=>getComputedStyle(n).backgroundColor));
  for(const width of [1440,1280,1024]){await page.setViewportSize({width,height:1100});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'No page overflow');assert(await root.locator('.rp-dot').evaluateAll(ns=>ns.every(n=>{const r=n.getBoundingClientRect();return r.width===16&&r.height===16;})));assert(await root.locator('.rp-row').evaluateAll(ns=>ns.every(n=>n.scrollHeight<=n.clientHeight+1)),'Complete row labels');}
  await page.setViewportSize({width:1440,height:1100});await root.locator('.rp-row[href="#presence-region-north"]').focus();await page.keyboard.press('Enter');assert(await root.locator('#presence-region-north').evaluate(n=>n.open));assert.equal(await root.locator('.rp-profile[open]').count(),1);assert.equal(await page.locator('dialog[open]').count(),0);
  assert((await root.locator('#presence-region-north').innerText()).includes('Warum Stufe 5?'));assert((await root.locator('#presence-region-north').innerText()).includes('Reichweite des Nachweises'));
  await root.locator('#presence-region-north .rp-source-fact>summary').first().click();assert(await root.locator('#presence-region-north .evidence a').first().isVisible());
  await root.locator('.rp-row[href="#presence-region-south"]').click();assert.equal(await root.locator('.rp-profile[open]').count(),1);assert.equal(await root.locator('.rp-row[aria-current=true]').getAttribute('href'),'#presence-region-south');
  await root.locator('#presence-region-south a.claim').first().click();assert(await page.locator('#page-sources').isVisible());await page.locator('[data-page=page-main]').click();assert(await root.locator('#presence-region-south').evaluate(n=>n.open));
  await root.locator('.rp-row[href="#presence-region-east"]').click();assert((await root.locator('#presence-region-east').innerText()).includes('Warum nicht eindeutig bestimmbar?'));assert.equal(await root.locator('.rp-row[href="#presence-region-east"] .rp-filled').count(),0);
  await root.locator('.rp-method>summary').click();assert.equal(await root.locator('.rp-method li').count(),5);
  const before=await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open));await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));await page.emulateMedia({media:'print'});assert.equal(await root.locator('.rp-profile[open]').count(),6);assert(await root.locator('.rp-source-fact').evaluateAll(ns=>ns.every(n=>n.open)));assert.equal(await root.locator('.rp-row:visible').count(),6);
  await page.emulateMedia({media:'screen'});await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));assert.deepEqual(await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open)),before);
  await root.locator('.rp-row[href="#presence-region-north"]').click();if(process.env.BRIEFING_QA_DIR){await root.screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'presence-detail.png')});await root.locator('.rp-profile[open]>summary').click();await root.locator('.rp-method>summary').click();await root.screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'presence-overview.png')});}
  await context.close();const fallback=await browser.newContext({offline:true,javaScriptEnabled:false,viewport:{width:1280,height:1000}}),fp=await fallback.newPage();await fp.goto(pathToFileURL(path.resolve(process.argv[2])).href);assert.equal(await fp.locator('#briefing-regional-presence .rp-row:visible').count(),6);await fp.locator('#presence-region-west>summary').click();await fp.locator('#presence-region-west .rp-source-fact>summary').first().click();assert(await fp.locator('#presence-region-west .evidence a').first().isVisible());await fallback.close();assert.deepEqual(errors,[]);
  console.log(JSON.stringify({regions:6,stages:[5,4,3,2,1,null],widths:[1440,1280,1024],placement:'passed',selection:'passed',sources:'passed',keyboard:'passed',print:'passed',noJavaScript:'passed',errors}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
