// Optional real-browser QA. Requires playwright-core and BRIEFING_CHROMIUM_PATH.
const assert = require('node:assert/strict');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright-core');

(async()=>{
 const files=process.argv.slice(2);
 assert(files.length,'Pass one or more generated HTML paths');
 assert(process.env.BRIEFING_CHROMIUM_PATH,'Set BRIEFING_CHROMIUM_PATH');
 const browser=await chromium.launch({executablePath:process.env.BRIEFING_CHROMIUM_PATH,headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
 const errors=[],results=[];
 try{
  for(const file of files){
   const context=await browser.newContext({offline:true,viewport:{width:1440,height:1000}});
   const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
   await page.goto(pathToFileURL(path.resolve(file)).href);
   await page.addStyleTag({content:'html{scroll-behavior:auto!important}'});
   const count=await page.locator('.es-card').count();assert(count>=4&&count<=6);
   assert.equal(await page.locator('.es-highlight').count(),3);
   for(const width of [1440,1024,390]){
    await page.setViewportSize({width,height:1000});
    const boxes=await page.locator('.es-card').evaluateAll(nodes=>nodes.map(n=>{const r=n.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,right:r.right};}));
    assert(boxes.every(r=>r.x>=0&&r.right<=width+1),'Summary card outside viewport');
    if(width===1440){
     const first=boxes.filter(b=>Math.abs(b.y-boxes[0].y)<1).length;
     assert.equal(first,count===4?2:3,'Desktop row distribution');
     if(count===5)assert(Math.abs(boxes[3].w-boxes[4].w)<1,'Balanced final two cards');
    }
    if(width===390)assert(boxes.every((r,i)=>!i||r.y>boxes[i-1].y),'Mobile cards stacked');
   }
   await page.setViewportSize({width:1440,height:1000});
   const first=page.locator('.es-highlight>summary').first();await first.focus();await page.keyboard.press('Enter');
   await page.waitForFunction(()=>document.getElementById('es-dialog').open);
   assert(await page.locator('.es-dialog .es-statement').isVisible(),'Keyboard detail opening');
   await page.locator('.es-dialog .es-fact>summary').first().click();
   assert((await page.locator('.es-dialog .evidence a').first().getAttribute('href')).startsWith('https://'),'Direct original source');
   await page.keyboard.press('Escape');await page.waitForFunction(()=>!document.getElementById('es-dialog').open);
   await page.locator('.es-card>summary').first().click();
   const claim=(await page.locator('.es-dialog a.claim').first().getAttribute('href')).slice(1);
   await page.locator('.es-dialog a.claim').first().click();
   await page.waitForFunction(()=>!document.getElementById('es-dialog').open);
   assert(await page.evaluate(id=>document.getElementById(id).open,claim),'Claim record opens');
   assert(await page.locator('#page-sources').isVisible(),'Source page visible');
   await page.locator('[data-page="page-main"]').click();
   await page.locator('.es-card>summary').first().click();
   await page.locator('.es-dialog-close').click();
   await page.locator('.es-card>summary').first().click();await page.mouse.click(2,2);
   await page.waitForFunction(()=>!document.getElementById('es-dialog').open);
   await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
   assert(await page.locator('.es-entry').evaluateAll(nodes=>nodes.every(n=>n.open)),'Print expands Summary');
   await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
   assert(await page.locator('.es-entry').evaluateAll(nodes=>nodes.every(n=>!n.open)),'Print restores Summary');
   if(process.env.BRIEFING_QA_DIR)await page.locator('#executive-summary').screenshot({path:path.join(process.env.BRIEFING_QA_DIR,'summary-'+count+'.png')});
   results.push({cards:count,widths:[1440,1024,390],dialog:'passed',sources:'passed',printState:'passed'});
   await context.close();
   const fallback=await browser.newContext({offline:true,javaScriptEnabled:false,viewport:{width:390,height:1000}});
   const fp=await fallback.newPage();await fp.goto(pathToFileURL(path.resolve(file)).href);
   await fp.locator('.es-card>summary').first().click();
   assert(await fp.locator('.es-card').first().evaluate(n=>n.open),'Native no-JS fallback');
   await fallback.close();
  }
  assert.deepEqual(errors,[],'Browser JS errors');console.log(JSON.stringify({results,errors,noJavaScript:'passed'}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
