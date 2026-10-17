"""Offline actor overview from the reviewed network; no inferred relationships."""
import html
from urllib.parse import urlsplit

KINDS = {'partner':'Partner', 'customer':'Kunde', 'jv':'Joint Venture',
         'owner':'Eigentümer', 'supplier':'Zulieferer', 'subsidiary':'Tochtergesellschaft',
         'project':'Projektpartner', 'institution':'Institution',
         'person':'Mandatsträger', 'other':'Weitere Akteure'}
GROUPS = [('capital','Kapital & Investoren'), ('structure','Konzern & Joint Ventures'),
          ('technology','Technologie & Industrie'), ('market','Kunden & Marktzugang')]

def esc(value):
    return html.escape(str(value), quote=True)

def group(node):
    return node.get('cluster') or {'owner':'capital','subsidiary':'structure',
        'jv':'structure','customer':'market','institution':'market'}.get(node['kind'], 'technology')

def actor_tables(network):
    actors = [n for n in network['nodes'] if n['id'] != network['target_id']]
    sources = {s['id']:s for s in network['sources']}
    products = {p['id']:p for p in network['products']}
    used = {n['kind'] for n in actors}
    out = ['<div id="cnt-view-tables" role="tabpanel" aria-labelledby="cnt-tab-tables" tabindex="0">',
        '<p class="cnt-intro">Akteure im Unternehmensumfeld, nach Clustern geordnet. Einzelne Einträge anklicken, um Angaben und Originalquellen zu öffnen.</p>',
        '<div class="cnt-tools"><label>Suche <input class="cnt-search" type="search" placeholder="Akteur suchen"></label>',
        '<label>Akteurstyp <select class="cnt-category"><option value="all">Alle Akteurstypen</option>']
    out += ['<option value="'+k+'">'+v+'</option>' for k,v in KINDS.items() if k in used]
    out += ['</select></label><button type="button" class="cnt-reset">Zurücksetzen</button></div>',
        '<div class="cnt-overview"><p class="cnt-count" role="status" aria-live="polite">'+str(len(actors))+' von '+str(len(actors))+' Akteuren</p>',
        '<div class="cnt-legend" role="group" aria-label="Legende der Akteursfarben"><span class="cnt-legend-title">Farben:</span>']
    out += ['<span class="cnt-legend-item"><i class="cnt-dot cnt-kind-'+k+'" aria-hidden="true"></i>'+v+'</span>' for k,v in KINDS.items() if k in used]
    out += ['</div></div><p class="cnt-empty" hidden>Keine Akteure für diese Auswahl.</p><div class="cnt-actor-grid">']
    for gid,label in GROUPS:
        nodes = [n for n in actors if group(n)==gid]
        out += ['<section class="cnt-group cnt-cluster-'+gid+'"'+(' hidden' if not nodes else '')+'><h4>'+label+' <span class="cnt-group-count">'+str(len(nodes))+'</span></h4><table class="cnt-actor-table"><caption class="cnt-sr">'+label+'</caption><tbody>']
        for node in nodes:
            related = [e for e in network['edges'] if node['id'] in (e['from'],e['to'])]
            source_ids = list(dict.fromkeys(s for e in related for s in e['source_ids']))
            product_ids = list(dict.fromkeys(p for e in related for p in e['product_ids']))
            out += ['<tr data-cnt-node="'+esc(node['id'])+'" data-kind="'+esc(node['kind'])+'" data-search="'+esc((node['label']+' '+(node.get('legal_name') or '')).lower())+'"><td><details class="cnt-actor-entry"><summary><span class="cnt-actor"><i class="cnt-dot cnt-kind-'+esc(node['kind'])+'" aria-hidden="true"></i><span>'+esc(node['label'])+'</span></span><span class="cnt-chevron" aria-hidden="true"></span></summary><div class="cnt-expanded">',
                '<p><strong>Vollständiger Name:</strong> '+esc(node.get('legal_name') or node['label'])+'</p><p><strong>Akteurstyp:</strong> '+esc(KINDS[node['kind']])+'</p>']
            if product_ids:
                out += ['<p><strong>Produktbezug im Briefing:</strong> '+esc(', '.join(products[p]['label'] for p in product_ids))+'</p>']
            out += ['<p class="cnt-source-title">Originalquellen</p>']
            for sid in source_ids:
                source = sources[sid]
                if urlsplit(source['url']).scheme not in ('http','https'):
                    raise ValueError('Unzulässiger Quellenlink')
                meta = [source.get('published_date') or 'o. D.', source.get('source_kind'),
                    'Geschäftsjahr '+str(source['report_year']) if source.get('report_year') else '',
                    'Seite '+str(source['page']) if source.get('page') else '', source.get('section'),
                    'Abruf '+source['accessed_date']]
                out += ['<p><a href="'+esc(source['url'])+'" target="_blank" rel="noopener noreferrer">'+esc(source['name']+' · '+source['title'])+'</a><br><small>'+esc(' · '.join(str(x) for x in meta if x))+'</small></p>']
            out += ['</div></details></td></tr>']
        out += ['</tbody></table></section>']
    return ''.join(out + ['</div></div>'])
