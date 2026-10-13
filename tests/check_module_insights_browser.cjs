// Offline desktop QA for sourced module cards in the synthetic full briefing.
const assert=require('node:assert/strict'),path=require('node:path');
const {pathToFileURL}=require('node:url'),{chromium}=require('playwright-core');
(async()=>{
 assert(process.argv[2]&&process.env.BRIEFING_CHROMIUM_PATH,'Pass HTML and set BRIEFING_CHROMIUM_PATH');
 const browser=await chromium.launch({executablePath:process.env.BRIEFING_CHROMIUM_PATH,headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});const errors=[];
 try{
  const context=await browser.newContext({offline:true,viewport:{width:1440,height:1000}}),page=await context.newPage();
  page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
  await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);
  const groups=[['portfolio','portfolio',3],['cluster','cluster-analysis',2],['market','capability-matrix',2]];
  for(const [module,parent,count] of groups){const root=page.locator('#insights-'+module);assert.equal(await root.locator('.mi-card').count(),count);assert.equal(await root.evaluate(n=>n.closest('.module').id),parent);assert.equal(await root.evaluate(n=>n.closest('.page').id),'page-main');assert.equal(await root.locator('.mi-detail[open]').count(),0);assert.equal(await root.evaluate(n=>n.parentElement.lastElementChild===n),true,'Cards directly after their module body');}
  for(const width of [1440,1280,1024]){
   await page.setViewportSize({width,height:1000});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'No page overflow');
   for(const [module] of groups){const boxes=await page.locator('#insights-'+module+' .mi-card').evaluateAll(ns=>ns.map(n=>({height:n.getBoundingClientRect().height,y:n.getBoundingClientRect().y,clipped:n.scrollHeight>n.clientHeight+1})));assert(boxes.every(b=>b.height===boxes[0].height&&b.y===boxes[0].y&&!b.clipped),'Equal heights, complete text in one row');}
  }
  await page.setViewportSize({width:1440,height:1000});const portfolio=page.locator('#insights-portfolio');
  await portfolio.locator('.mi-detail>summary').first().focus();await page.keyboard.press('Enter');assert(await portfolio.locator('.mi-detail').first().evaluate(n=>n.open));assert.equal(await page.locator('dialog[open]').count(),0);
  await portfolio.locator('.mi-source-fact>summary').first().click();assert(await portfolio.locator('.evidence a').first().isVisible());assert((await portfolio.locator('.mi-detail-body').first().innerText()).includes('Herleitung'));assert((await portfolio.locator('.mi-detail-body').first().innerText()).includes('Synthetischer Offline-Test'));
  await portfolio.locator('a.claim').first().click();assert(await page.locator('#page-sources').isVisible());await page.locator('[data-page=page-main]').click();assert(await portfolio.locator('.mi-detail').first().evaluate(n=>n.open));
  await portfolio.locator('.mi-detail>summary').first().click();const before=await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open));
  await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));await page.emulateMedia({media:'print'});
  assert.equal(await page.locator('.mi-detail[open]').count(),7);assert(await page.locator('.mi-source-fact').evaluateAll(ns=>ns.every(n=>n.open)));assert.equal(await page.locator('.mi-card:visible').count(),7);
  await page.emulateMedia({media:'screen'});await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));assert.deepEqual(await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open)),before);
  if(process.env.BRIEFING_QA_DIR){for(const [module] of groups)await page.locator('#insights-'+module).screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'insights-'+module+'.png')});}
  await context.close();const fallback=await browser.newContext({offline:true,javaScriptEnabled:false,viewport:{width:1280,height:1000}}),fp=await fallback.newPage();await fp.goto(pathToFileURL(path.resolve(process.argv[2])).href);assert.equal(await fp.locator('.mi-card:visible').count(),7);await fp.locator('#insights-cluster .mi-detail>summary').first().click();await fp.locator('#insights-cluster .mi-source-fact>summary').first().click();assert(await fp.locator('#insights-cluster .evidence a').first().isVisible());await fallback.close();assert.deepEqual(errors,[]);
  console.log(JSON.stringify({groups:3,cards:7,widths:[1440,1280,1024],placement:'passed',sources:'passed',keyboard:'passed',print:'passed',noJavaScript:'passed',errors}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
