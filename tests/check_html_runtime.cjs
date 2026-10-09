// Run generated inline JS against a small DOM. This is not a browser/CSS test.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(process.argv[2],'utf8');
const decode=s=>s.replace(/&(amp|lt|gt|quot|#x27|#39);/g,(_,x)=>({amp:'&',lt:'<',gt:'>',quot:'"','#x27':"'",'#39':"'"}[x]));
class Element{
 constructor(tag,attrs={}){this.tagName=tag.toUpperCase();this.attrs=attrs;this.children=[];this.parentElement=null;this.listeners={};this.style={};this.dataset=new Proxy({},{set:(obj,key,val)=>{obj[key]=val;this.attrs["data-"+key]=String(val);return true;}});this.hidden='hidden'in attrs;this.open='open'in attrs;this.checked='checked'in attrs;this.value=attrs.value||'';this._text='';for(const [k,v]of Object.entries(attrs))if(k.startsWith('data-'))this.dataset[k.slice(5)]=v;}
 get id(){return this.attrs.id||'';}set id(v){this.attrs.id=v;}
 get className(){return this.attrs.class||'';}set className(v){this.attrs.class=v;}
 get href(){return this.attrs.href||'';}set href(v){this.attrs.href=v;}
 set textContent(v){this.children=[];this._text=String(v);}get textContent(){return this._text+this.children.map(c=>c.textContent).join('');}
 setAttribute(k,v){this.attrs[k]=String(v);}getAttribute(k){return this.attrs[k]??null;}
 appendChild(c){c.parentElement=this;this.children.push(c);if(this.tagName==='SELECT'&&this.children.length===1)this.value=c.value;return c;}
 replaceChildren(...items){this.children=[];this._text='';items.forEach(i=>this.appendChild(i));}
 addEventListener(k,fn){(this.listeners[k]??=[]).push(fn);}emit(k,event={}){for(const f of this.listeners[k]||[])f({target:this,preventDefault(){},...event});}
 matches(selector){let checked=selector.endsWith(':checked');if(checked){selector=selector.slice(0,-8);if(!this.checked)return false;}
  const compound=selector.match(/^([a-z]+)(\[.*\])$/);if(compound)return this.matches(compound[1])&&this.matches(compound[2]);
  if(selector.startsWith('.'))return this.className.split(/\s+/).includes(selector.slice(1));
  if(selector.startsWith('[')){const m=selector.match(/^\[([^=\^\]]+)(\^?=)?["']?([^"'\]]*)["']?\]$/);if(!m)return false;const val=this.attrs[m[1]];return m[2]==='^='?val?.startsWith(m[3]):m[2]==='='?val===m[3]:val!==undefined;}
  return this.tagName===selector.toUpperCase();}
 querySelectorAll(selector){const parts=selector.split(' ');const result=[];const walk=node=>{for(const c of node.children){if(c.matches(parts.at(-1))){let p=c.parentElement,ok=true;for(let i=parts.length-2;i>=0;i--){while(p&&!p.matches(parts[i]))p=p.parentElement;if(!p){ok=false;break;}p=p.parentElement;}if(ok)result.push(c);}walk(c);}};walk(this);return result;}
 querySelector(s){return this.querySelectorAll(s)[0]||null;}closest(s){for(let n=this;n;n=n.parentElement)if(n.matches(s))return n;return null;}
 scrollIntoView(){this.scrolled=true;}get clientWidth(){return 960;}
}
const document=new Element('document'),stack=[document],scripts=[];
const token=/<script\b[^>]*>[\s\S]*?<\/script>|<style\b[^>]*>[\s\S]*?<\/style>|<!--[\s\S]*?-->|<[^>]+>|[^<]+/gi;
for(const match of html.matchAll(token)){
 const raw=match[0];if(raw.startsWith('<!--')||raw.startsWith('<!'))continue;
 if(!raw.startsWith('<')){stack.at(-1)._text+=decode(raw);continue;}
 if(raw.startsWith('</')){stack.pop();continue;}
 const tag=raw.match(/^<([\w-]+)/)[1],attrs={};const start=raw.match(/^<[^>]+>/)[0];
 for(const a of start.matchAll(/\s([\w-]+)(?:=(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?/g))attrs[a[1]]=decode(a[2]??a[3]??a[4]??'');
 const el=new Element(tag,attrs);stack.at(-1).appendChild(el);
 if(tag==='script'||tag==='style'){el.textContent=raw.slice(start.length,raw.lastIndexOf('</'));if(tag==='script'&&attrs.type!=='application/json')scripts.push(el.textContent);continue;}
 if(!['meta','input','br','hr','img','link'].includes(tag))stack.push(el);
}
document.getElementById=id=>{const find=n=>n.id===id?n:n.children.map(find).find(Boolean);return find(document);};
document.createElement=t=>new Element(t);document.createElementNS=(_,t)=>new Element(t);
const errors=[],window=new Element('window'),location={hash:''};
const context={document,window,location,URL,console:{error:(...x)=>errors.push(x.join(' '))},ResizeObserver:class{constructor(f){this.f=f;}observe(){this.f();}}};
for(const code of scripts){new vm.Script(code).runInNewContext(context);}
assert.deepEqual(errors,[],'inline JS errors');assert.equal(scripts.length,2,'network and navigation scripts');
const root=document.getElementById('briefing-company-network'),data=JSON.parse(root.querySelector('.cn-data').textContent);
assert.equal(root.querySelector('tbody').children.length,data.edges.length,'fallback table rows not duplicated');
root.querySelector('.cn-expand').emit('click');root.querySelector('.cn-cross').checked=true;root.querySelector('.cn-cross').emit('change');
assert.equal(root.querySelectorAll('.cn-node').length,data.nodes.length,'all nodes accessible');
assert.equal(root.querySelectorAll('.cn-hit').length,data.edges.length,'cross relationships rendered');
root.querySelector('.cn-hit').emit('click');assert.equal(root.querySelector('.cn-details').hidden,false);
assert(root.querySelector('.cn-detail-content').textContent.includes('Fiktive Testquelle'),'direct source metadata in selected edge');
root.querySelector('.cn-search').value='no such company';root.querySelector('.cn-search').emit('input');
assert.equal(root.querySelectorAll('.cn-hit').length,0,'search filters edges');assert.equal(root.querySelector('.cn-details').hidden,true,'stale details cleared');
root.querySelector('.cn-reset').emit('click');assert.equal(root.querySelector('.cn-search').value,'');
const node=root.querySelector('.cn-node');node.emit('keydown',{key:'Enter'});assert.equal(root.querySelector('.cn-details').hidden,false,'keyboard node details');
const pages=document.querySelectorAll('.page'),target=document.getElementById('I1');
document.emit('click',{target:new Element('a',{href:'#I1'})});assert.equal(target.open,true);assert.equal(target.closest('.page').hidden,false);
const details=document.querySelectorAll('details'),state=details.map(d=>d.open),hidden=pages.map(p=>p.hidden);
window.emit('beforeprint');assert(details.every(d=>d.open));assert(pages.every(p=>!p.hidden));
window.emit('afterprint');assert.deepEqual(details.map(d=>d.open),state,'print restores detail state');assert.deepEqual(pages.map(p=>p.hidden),hidden,'print restores page state');
console.log(JSON.stringify({inlineScripts:scripts.length,nodes:data.nodes.length,edges:data.edges.length,checks:'minimal DOM passed',browserLayout:'not checked'}));
