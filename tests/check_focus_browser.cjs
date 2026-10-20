// Offline browser check of a synthetic multi-focus briefing; no source truth claims.
const assert=require('node:assert/strict'),path=require('node:path');
const {pathToFileURL}=require('node:url'),{chromium}=require('playwright-core');
(async()=>{
 assert(process.argv[2]&&process.env.BRIEFING_CHROMIUM_PATH,'Pass synthetic focus HTML and BRIEFING_CHROMIUM_PATH');
 const browser=await chromium.launch({executablePath:process.env.BRIEFING_CHROMIUM_PATH,headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--single-process']});
 try{
  const context=await browser.newContext({offline:true,viewport:{width:1440,height:1000}}),page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);
  assert.deepEqual(await page.locator('.page').evaluateAll(ns=>ns.map(n=>n.id)),['page-main','page-profile','page-focus-lkw','page-focus-drohnen','page-sources']);
  await page.locator('[data-page="page-focus-lkw"]').click();
  assert(await page.locator('#page-focus-lkw').isVisible());
  assert.equal(await page.locator('#page-focus-lkw .focus-chart').count(),3);
  assert.equal(await page.locator('#page-focus-lkw .focus-event').count(),8);
  assert.equal(await page.locator('#page-focus-lkw .focus-metric').count(),4);
  assert.equal(await page.locator('#page-focus-lkw .focus-actors tbody tr').count(),3);
  assert(await page.locator('#page-focus-lkw .focus-definition').isVisible());
  assert(await page.locator('#page-focus-lkw .focus-meeting').isVisible());
  assert.equal(await page.locator('#page-focus-lkw .focus-gaps').evaluate(n=>n.open),false);
  for(const width of [1440,1280,1024]){
   await page.setViewportSize({width,height:1000});
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'No global horizontal overflow');
  }
  const thesis=page.locator('#page-focus-lkw .focus-thesis details').first();
  await thesis.locator('summary').click();assert(await thesis.evaluate(n=>n.open));
  const states=await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open));
  await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
  assert(await page.locator('.page').evaluateAll(ns=>ns.every(n=>!n.hidden)));
  assert(await page.locator('details').evaluateAll(ns=>ns.every(n=>n.open)));
  await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
  assert.deepEqual(await page.locator('details').evaluateAll(ns=>ns.map(n=>n.open)),states);
  assert(await page.locator('#page-focus-lkw').isVisible());
  await thesis.locator('a[href^="#F_"]').first().click();
  assert(await page.locator('#page-sources').isVisible());assert(await page.locator('#F_lkw_1').evaluate(n=>n.open));
  await page.locator('[data-page="page-focus-drohnen"]').click();
  assert(await page.locator('#page-focus-drohnen').isVisible());
  await page.locator('[data-page="page-focus-lkw"]').click();
  await page.setViewportSize({width:1440,height:1000});
  if(process.argv[3])await page.screenshot({path:process.argv[3],fullPage:true});
  assert.deepEqual(errors,[]);
  const plain=await browser.newContext({javaScriptEnabled:false,offline:true});const nojs=await plain.newPage();
  await nojs.goto(pathToFileURL(path.resolve(process.argv[2])).href);
  assert(await nojs.locator('#page-focus-lkw').isVisible());
  assert(await nojs.locator('#page-focus-drohnen').isVisible());
  console.log('PASS: multi-focus navigation, graphics, source jumps, details, print restoration, desktop widths and no-JS access');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
