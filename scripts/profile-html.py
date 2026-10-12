"""Source-linked professional profile. No inferred career or hard-coded person."""
from html import escape
from pathlib import Path

ESC = lambda value: escape(str(value), quote=True)
FIELDS = ('snapshot', 'career', 'expertise', 'responsibilities')


def validate(profile, require):
    if not isinstance(profile, dict) or not isinstance(profile.get('name'), str) or not profile['name'].strip():
        raise ValueError('profile needs a name')
    refs = profile.get('claim_ids')
    require(refs)
    if any(not cid.startswith('H') for cid in refs):
        raise ValueError('profile uses non-professional-person claims')
    allowed = set(refs)
    def row(item, keys):
        if not isinstance(item, dict):
            raise ValueError('profile row must be an object')
        for key in keys:
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValueError('profile row requires ' + key)
        require(item.get('claim_ids'))
        if not set(item['claim_ids']) <= allowed:
            raise ValueError('profile row references facts outside profile')
    for field in ('intro', 'regional_context'):
        if field in profile:
            row(profile[field], ('text',) if field == 'intro' else ('label', 'text'))
    required = {'snapshot': ('label','value'), 'career': ('period','organization','role','context'),
                'expertise': ('label','text'), 'responsibilities': ('label','text')}
    for field in FIELDS:
        rows = profile.get(field, [])
        if not isinstance(rows, list):
            raise ValueError('profile ' + field + ' must be a list')
        if field == 'snapshot' and len(rows) > 6:
            raise ValueError('profile snapshot allows at most six facts')
        for item in rows:
            row(item, required[field])


def render(profile, claims, sources, company, as_of):
    """Caller validates review status and profile mappings before rendering."""
    source_order = list(dict.fromkeys(s for cid in profile['claim_ids'] for s in claims[cid]['source_ids']))
    source_numbers = {sid: i+1 for i,sid in enumerate(source_order)}
    used = set()
    def refs(ids):
        used.update(ids)
        ids = list(dict.fromkeys(sid for cid in ids for sid in claims[cid]['source_ids']))
        return '<sup>'+' '.join('<a href="#person-source-'+str(source_numbers[s])+'">['+str(source_numbers[s])+']</a>' for s in ids)+'</sup>'
    def block(title, body, number, klass=''):
        return '<section class="pp-block '+klass+'"><h3><span class="pp-num">'+number+'</span>'+ESC(title)+'</h3>'+body+'</section>'
    def missing():
        return '<p class="pp-empty">Hierzu liegen keine freigegebenen Angaben im Recherchepaket vor.</p>'
    body='<div class="pp-head"><div><p class="pp-tag">Gesprächspartnerprofil</p><h2>'+ESC(profile['name'])+'</h2></div><p class="pp-meta">'+ESC(company)+'<br>Stand: '+ESC(as_of)+'</p></div>'
    intro=profile.get('intro')
    if intro:body+='<p class="pp-intro">'+ESC(intro['text'])+refs(intro['claim_ids'])+'</p>'
    items=profile.get('snapshot',[])
    snapshot='<dl>'+''.join('<div><dt>'+ESC(r['label'])+'</dt><dd>'+ESC(r['value'])+refs(r['claim_ids'])+'</dd></div>' for r in items)+'</dl>' if items else missing()
    body+=block('Executive Snapshot',snapshot,'01','pp-snapshot')
    career=profile.get('career',[])
    table='<div class="pp-table"><table><thead><tr><th>Zeitraum</th><th>Organisation</th><th>Position / Rolle</th><th>Kontext</th></tr></thead><tbody>'+''.join('<tr><td>'+ESC(r['period'])+'</td><td>'+ESC(r['organization'])+'</td><td>'+ESC(r['role'])+'</td><td>'+ESC(r['context'])+refs(r['claim_ids'])+'</td></tr>' for r in career)+'</tbody></table></div>' if career else missing()
    body+=block('Werdegang und prägende Stationen',table,'02')
    body+='<div class="pp-cols">'
    for field,title,number in [('expertise','Fachliches Profil','03'),('responsibilities','Aktuelle Verantwortung','04')]:
        rows=profile.get(field,[])
        content='<ul>'+''.join('<li><strong>'+ESC(r['label'])+':</strong> '+ESC(r['text'])+refs(r['claim_ids'])+'</li>' for r in rows)+'</ul>' if rows else missing()
        body+=block(title,content,number)
    body+='</div>'
    region=profile.get('regional_context')
    if region:
        body+='<aside class="pp-note"><strong>'+ESC(region['label'])+'</strong><p>'+ESC(region['text'])+refs(region['claim_ids'])+'</p></aside>'
    else:
        body+='<aside class="pp-note"><strong>Regionaler Bezug</strong><p>Kein freigegebener regionaler Personenbezug im Recherchepaket. Unternehmenspräsenz allein belegt keine persönliche Zuständigkeit.</p></aside>'
    remaining=[c for c in profile['claim_ids'] if c not in used]
    if remaining:
        body+=block('Weitere belegte Profilangaben',''.join('<p>'+ESC(claims[c]['statement'])+refs([c])+'</p>' for c in remaining),'05')
    body+='<div class="pp-sources"><h3>Quellen &amp; Evidenz</h3>'
    for sid in source_order:
        s=sources[sid];n=source_numbers[sid]
        body+='<p id="person-source-'+str(n)+'">['+str(n)+'] '+ESC(s['name'])+' · <a href="'+ESC(s['url'])+'" target="_blank" rel="noopener noreferrer">'+ESC(s['title'])+'</a> · '+ESC(s.get('published_date') or 'o. D.')+'</p>'
    # Exact claims and uncertainty remain visible and do not become hidden behind a dialog.
    body+='<div class="pp-evidence">'
    for cid in profile['claim_ids']:
        c=claims[cid]
        body+='<p><a class="claim" href="#'+ESC(cid)+'">'+ESC(cid)+'</a> '+ESC(c['statement'])
        if c.get('uncertainty'):body+=' <em>Grenze: '+ESC(c['uncertainty'])+'</em>'
        body+='</p>'
    body+='</div></div>'
    css=(Path(__file__).resolve().parents[1]/'references/templates/profile.css').read_text()
    return '<style>'+css+'</style><article class="person-profile">'+body+'</article>'
