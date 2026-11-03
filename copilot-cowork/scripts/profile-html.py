"""Source-linked professional profile. No inferred career or hard-coded person."""
from html import escape
from pathlib import Path
from datetime import date
import calendar

ESC = lambda value: escape(str(value), quote=True)
FIELDS = ('snapshot', 'career', 'expertise', 'responsibilities')


def validate(profile, require, as_of=None, claims=None):
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

    media = profile.get('media', [])
    if not isinstance(media, list):
        raise ValueError('profile media must be a list')
    seen = set()
    for entry in media:
        row(entry, ('id','published_date','category','format','title','preview','access_note'))
        if entry['id'] in seen or entry['category'] not in MEDIA_CATEGORIES:
            raise ValueError('duplicate media id or invalid category')
        seen.add(entry['id'])
        try:
            published = date.fromisoformat(entry['published_date'])
            event = date.fromisoformat(entry['event_date']) if entry.get('event_date') else None
        except (ValueError, TypeError):
            raise ValueError('invalid media date')
        if as_of and not media_window(as_of)[0] <= published <= date.fromisoformat(as_of):
            raise ValueError('media publication outside four-month window')
        if event and event > published:
            raise ValueError('media event later than publication')
        if entry.get('quote'):
            if not isinstance(entry['quote'], str) or len(entry['quote'].split()) > 25:
                raise ValueError('media quote must be short')
            if not entry.get('quote_source_id') or not entry.get('quote_location'):
                raise ValueError('media quote requires source and location')
            if claims and entry['quote_source_id'] not in {sid for cid in entry['claim_ids'] for sid in claims[cid]['source_ids']}:
                raise ValueError('media quote source outside referenced claims')


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
    used.update(cid for entry in profile.get('media', []) for cid in entry['claim_ids'])
    remaining=[c for c in profile['claim_ids'] if c not in used]
    if remaining:
        body+=block('Weitere belegte Profilangaben',''.join('<p>'+ESC(claims[c]['statement'])+refs([c])+'</p>' for c in remaining),'05')
    css=(Path(__file__).resolve().parents[1]/'references/templates/profile.css').read_text()
    return '<style>'+css+'</style><article class="person-profile">'+body+'</article>'


def render_sources(profile, claims, sources):
    """Full evidence is rendered on the sources page only."""
    source_order = list(dict.fromkeys(s for cid in profile['claim_ids'] for s in claims[cid]['source_ids']))
    source_numbers = {sid:i+1 for i,sid in enumerate(source_order)}
    body = ''
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
    return '<div class="person-profile">'+body+'</div>'


MEDIA_CATEGORIES = {'own':'Eigene Äußerungen', 'official':'Offizielle Verlautbarungen', 'media':'Artikel über die Person'}

def media_window(as_of):
    end = date.fromisoformat(as_of)
    month = end.year * 12 + end.month - 1 - 4
    year, zero_month = divmod(month, 12)
    start = date(year, zero_month+1, min(end.day, calendar.monthrange(year, zero_month+1)[1]))
    return start, end

def render_media(profile, claims, as_of, sources=None):
    entries = sorted(profile.get('media', []), key=lambda x:x['published_date'], reverse=True)
    start, end = media_window(as_of)
    labels = {**MEDIA_CATEGORIES, 'media':'Artikel über '+profile['name']}
    out = ['<section class="module profile-media" id="person-media"><h2>Aktuelle Äußerungen &amp; Medienpräsenz der letzten vier Monate</h2>',
        '<div class="pm-head"><p class="pm-window">'+start.strftime('%d.%m.%Y')+'–'+end.strftime('%d.%m.%Y')+' · Nach Veröffentlichung sortiert</p><div class="pm-legend" aria-label="Kategorien">']
    out += ['<span class="pm-tag pm-'+key+'">'+ESC(label)+'</span>' for key,label in labels.items()]
    out += ['</div></div><div class="timeline pm-timeline">']
    for index, entry in enumerate(entries, 1):
        publishers = list(dict.fromkeys(sources[sid]['name'] for cid in entry['claim_ids'] for sid in claims[cid]['source_ids'])) if sources else []
        publisher = '<span class="pm-publisher">'+ESC(' · '.join(publishers))+'</span>' if publishers else ''
        published = date.fromisoformat(entry['published_date'])
        out += ['<div class="event pm-event"><time datetime="'+entry['published_date']+'">'+published.strftime('%d.%m.%Y')+'</time><details class="pm-entry pm-'+entry['category']+'" id="person-media-'+str(index)+'"><summary><span class="pm-kicker">'+ESC(labels[entry['category']]+' · '+entry['format'])+'</span><span class="pm-title">'+ESC(entry['title'])+'</span><span class="pm-preview">'+ESC(entry['preview'])+'</span>'+publisher+'<span class="pm-arrow" aria-hidden="true">⌄</span></summary><div class="pm-body">']
        out += ['<p>'+ESC(claims[cid]['statement'])+'</p>' for cid in entry['claim_ids']]
        if entry.get('quote'):
            out += ['<blockquote>„'+ESC(entry['quote'])+'“</blockquote>']
        if entry.get('event_date'):
            out += ['<p class="meta">Ereignisdatum: '+ESC(entry['event_date'])+' · Veröffentlichung: '+ESC(entry['published_date'])+'</p>']
        out += ['<p class="pm-limit"><strong>Einordnung &amp; Prüfgrenze:</strong> '+ESC(entry['access_note'])+'</p>']
        out += ['<p class="pm-source-refs">Quellen und Evidenz: '+', '.join('<a href="#'+ESC(cid)+'">'+ESC(cid)+'</a>' for cid in entry['claim_ids'])+'</p></div></details></div>']
    if not entries:
        out += ['<p class="meta">Keine freigegebenen Beiträge im Viermonatsfenster vorhanden. Daraus folgt nicht, dass keine veröffentlicht wurden.</p>']
    out += ['</div><p class="pm-note">Auswahl beruflich relevanter Beiträge; keine vollständige Medienauswertung. Gleichlautende Beiträge zum selben Ereignis zusammenfassen.</p></section>']
    return ''.join(out)
