from pathlib import Path
import json,re,html,importlib.util
B=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('portfolio_html',B/'scripts/portfolio-html.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
facts=json.loads((B/'work/portfolio-reviewed.json').read_text())
pos=json.loads((B/'work/positioning-portfolio.json').read_text())
source_data=facts['sources']
sources={s['id']:s for s in source_data} if isinstance(source_data,list) else source_data
assessments={x['product_id']:x for x in pos['interpretations']}
# Preserve the original background-source register alongside reviewed status sources.
for line in (B/'work/portfolio.md').read_text().splitlines():
 m=re.match(r'\| (Q\d+) \| \[([^\]]+)\]\((https://[^)]+)\) \| ([^|]+)',line)
 if m and m[1] not in sources:sources[m[1]]={'id':m[1],'title':m[2],'url':m[3],'date':m[4].strip()}
claims={};products=[]
raw=(B/'work/portfolio.md').read_text()
original={}
for block in re.split(r'\n\s*\n',raw):
 m=re.search(r'\[(P-\d{3});',block)
 if m and block.startswith('**'):original[m[1]]=block

def plain(t):
 t=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',t)
 return t.replace('**','').replace('*','')

for p in facts['products']:
 pid=p['id'];sid=p['claim_ids'][0];did='D-'+pid
 evidence=p.get('status_evidence') or p.get('statement','')
 if not isinstance(evidence,str):evidence=json.dumps(evidence,ensure_ascii=False)
 claims[sid]={'id':sid,'statement':evidence,'kind':p.get('origin','Herstellerangabe'),'uncertainty':p.get('uncertainty',''),'source_ids':p.get('source_ids',[]),'location':p.get('evidence_location','')}
 old=original.get(p.get('original_claim_id',''),'')
 old_sources=list(dict.fromkeys(re.findall(r'\bQ\d+\b',old)))
 sections=[]
 if old:
  claims[did]={'id':did,'statement':plain(old),'kind':'Herstellerbeschreibung – technische Hintergrunddetails ohne separate Vollprüfung','uncertainty':'Die Reifebewertung stützt sich auf die gesondert geprüften Statusbelege. Die ursprüngliche Produktbeschreibung kann mehrere Varianten zusammenfassend behandeln.','source_ids':old_sources,'location':'Ursprüngliches Detailprofil '+p.get('original_claim_id','')}
  sections=[{'label':'Merkmale & Anwendung','claim_ids':[did]}]
 products.append({'id':pid,'label':p['label'],'short_label':p.get('short_label',p['label']),'domain':p['domain'],'claim_ids':[sid],'sections':sections})


def esc(t):return html.escape(str(t),quote=True)
def evidence(c):
 out='<p class="meta">Belegstelle: '+esc(c.get('location',''))+'</p>'
 for q in c.get('source_ids',[]):
  s=sources.get(q,{})
  out+='<p><a href="'+esc(s.get('url','#'))+'" target="_blank" rel="noopener noreferrer">'+esc(q+' · '+s.get('title',q))+'</a></p>'
 return out

def links(ids):
 return ''.join('<span class="claim" id="evidence-'+esc(i)+'">'+esc(i)+'</span>' for i in ids)
stages={'1':'Angekündigt','2':'Prototyp','3':'Test / Demo','4':'Kundenprogramm','5':'Im Betrieb','6':'Serie / Skala'}
portfolio=mod.render({'products':products},assessments,claims,evidence,links,stages)
# Place the original, unmodified repository portfolio renderer inside its original page shell.
source_html=''
for q,s in sources.items():
 source_html+='<details class="claim-detail" id="source-'+esc(q)+'"><summary>'+esc(q+' · '+s.get('title',q))+'</summary><p><a target="_blank" rel="noopener noreferrer" href="'+esc(s.get('url','#'))+'">Originalquelle öffnen</a></p><p class="meta">'+esc(s.get('date',s.get('published_date','o. D.')))+'</p></details>'
limits=pos.get('shared_limitations',[])
limit_html=''.join('<p>'+esc(x)+'</p>' for x in limits)
content='<div class="page" id="page-portfolio"><p class="page-kicker">Rheinmetall · Portfolioanalyse</p><section class="module">'+portfolio+'</section><section class="module"><details><summary>Umfang, Bewertungsgrenzen & Portfoliokontext</summary><p>Gliederung nach den sieben Website-Kategorien. Die Skala beschreibt öffentlich belegte Meilensteine, keine technische Leistungsfähigkeit, Marktattraktivität oder Gesamtbewertung des Konzerns.</p>'+limit_html+'<p>Zivile Mobilitäts- und Industrieprodukte werden entsprechend der Website-Struktur berücksichtigt; der am 3. Juni 2026 vereinbarte Power-Systems-Verkauf an AEQUITA ist von einem belegten Vollzug zu unterscheiden. NVL gehört seit dem Übergang zum 1. März 2026 zum maritimen Portfolio.</p></details></section></div>'
content+='<div class="page" id="page-sources"><section class="module"><p class="page-kicker">02 / Quellen & Evidenz</p><h2>Quellenregister</h2><p class="meta">Abruf: 19. Oktober 2026. Herstellerangaben bleiben als solche ausgewiesen. Die Statusprüfung und Bewertung sind getrennt von technischen Hintergrundbeschreibungen.</p><label class="source-search">Quellen durchsuchen<input id="source-search-input" type="search" placeholder="Titel oder Quelle …"></label>'+source_html+'</section></div>'
tabs='<button role="tab" aria-controls="page-portfolio" data-page="page-portfolio">01 · Portfolio & Produktreife</button><button role="tab" aria-controls="page-sources" data-page="page-sources">02 · Quellen</button>'
tpl=(B/'references/templates/briefing.html').read_text()
for k,v in {'__TITLE__':'Rheinmetall · Portfolioanalyse','__BADGE__':'PORTFOLIO & PRODUKTREIFE','__SCOPE__':'Land · Luft · See · Digitalisierung · Mobilität · Industrie · Ausbildung & Service','__DATE__':'19. Oktober 2026','__TABS__':tabs,'__CONTENT__':content}.items():tpl=tpl.replace(k,v)
(B/'output/Rheinmetall_Portfolioanalyse.html').write_text(tpl)
print(json.dumps({'products':len(products),'assessments':len(assessments),'sources':len(sources),'stages':{k:sum(a.get('score')==int(k) for a in assessments.values()) for k in stages},'unbestimmbar':sum(a.get('score') is None for a in assessments.values())},ensure_ascii=False))
