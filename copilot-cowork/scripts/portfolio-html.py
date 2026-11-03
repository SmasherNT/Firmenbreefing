"""Render the approved portfolio style from reviewed product/interpretation records."""
import html
from pathlib import Path

COLORS = ("#176e91", "#4d7852", "#7960a0", "#196a79", "#9a563e", "#ad8429")

def esc(value):
    return html.escape(str(value), quote=True)

def render(inventory, assessments, claims, evidence, links, stages):
    products = inventory["products"]
    if not products:
        return ""
    groups = list(dict.fromkeys(p["domain"] for p in products))
    origins = {p['id']: sorted({claims[c]['kind'] for c in p['claim_ids']}) for p in products}
    colors = {g: COLORS[i % len(COLORS)] for i, g in enumerate(groups)}
    entries = []
    for p in products:
        assessment = assessments.get(p["id"])
        grade = assessment.get("score") if assessment else None
        ids = list(dict.fromkeys([*p["claim_ids"], *(c for group in p.get('sections', []) for c in group['claim_ids']), *(assessment.get("depends_on", []) if assessment else [])]))
        entries.append((p, assessment, grade, ids))

    def product_link(p, grade):
        return '<a class="pf-map-item" data-pf-item="' + esc(p["id"]) + '" href="#product-' + esc(p["id"]) + '" style="--pf-domain:' + colors[p["domain"]] + '"><span class="pf-dot"></span><span>' + esc(p["short_label"]) + '</span><small>' + (str(grade) if grade else 'offen') + '</small></a>'

    out = '<div id="briefing-portfolio" class="pf-root">'
    out += '<div class="pf-head"><div><span class="pf-num">01 / PORTFOLIO & PRODUKTREIFE</span><h2>Ein Portfolio. Eine transparente Skala.</h2></div><div class="pf-views" hidden><button type="button" data-pf-view="map" aria-pressed="true">Reife-Matrix</button><button type="button" data-pf-view="table" aria-pressed="false">Tabelle</button></div></div>'
    out += '<p class="pf-intro">Zeile und Farbe kennzeichnen die Produktgruppe. Die Position zeigt die öffentlich belegte Reife. Produkt anklicken, Begründung lesen, Originalquelle öffnen.</p>'
    out += '<div class="pf-filters" hidden><label>Suche<input type="search" data-pf-filter="query" placeholder="Produkt oder Anwendung"></label><label>Produktgruppe<select data-pf-filter="domain"><option value="">Alle Produktgruppen</option>' + ''.join('<option>' + esc(g) + '</option>' for g in groups) + '</select></label><label>Reifestufe<select data-pf-filter="grade"><option value="">Alle Stufen</option>' + ''.join('<option value="' + k + '">' + k + ' · ' + esc(v) + '</option>' for k, v in stages.items()) + '<option value="unknown">Nicht eindeutig bestimmbar</option></select></label><label>Aussageursprung<select data-pf-filter="origin"><option value="">Alle Belegarten</option>' + ''.join('<option>' + esc(k) + '</option>' for k in sorted({k for kinds in origins.values() for k in kinds})) + '</select></label><button type="button" class="pf-reset">Zurücksetzen</button></div><p class="pf-count" aria-live="polite"></p>'
    out += '<div class="pf-map-view"><div class="pf-table-wrap"><table class="pf-maturity-map"><thead><tr><th>Produktgruppe</th>' + ''.join('<th><b>' + k + '</b><span>' + esc(v) + '</span></th>' for k, v in stages.items()) + '</tr></thead><tbody>'
    for g in groups:
        out += '<tr data-pf-group="' + esc(g) + '"><th scope="row"><span class="pf-domain-mark" style="background:' + colors[g] + '"></span>' + esc(g) + '</th>'
        for n in range(1, 7):
            out += '<td>' + ''.join(product_link(p, grade) for p, _, grade, _ in entries if p["domain"] == g and grade == n) + '</td>'
        out += '</tr>'
    out += '</tbody></table></div>'
    unknown = [(p, g) for p, _, g, _ in entries if g is None]
    out += '<aside class="pf-unknown"' + ('' if unknown else ' hidden') + '><h3>Nicht eindeutig bestimmbar</h3><p>Keine freigegebene Reifestufe. Eine Beleglücke ist kein Nachweis niedriger Reife.</p>' + ''.join(product_link(p, g) for p, g in unknown) + '</aside></div>'
    out += '<div class="pf-result-view" hidden><div class="pf-table-wrap"><table class="pf-results"><thead><tr><th>Produkt</th><th>Gruppe</th><th>Stufe</th><th>Begründung</th></tr></thead><tbody>'
    for p, a, grade, ids in entries:
        out += '<tr data-pf-result="' + esc(p["id"]) + '" data-pf-origin="' + esc('|'.join(origins[p['id']])) + '"><td><a href="#product-' + esc(p["id"]) + '">' + esc(p["label"]) + '</a></td><td>' + esc(p["domain"]) + '</td><td>' + (str(grade) + ' · ' + esc(stages[str(grade)]) if grade else 'Nicht eindeutig bestimmbar') + '</td><td>' + esc(a["reasoning"] if a else 'Reine Faktenansicht; keine freigegebene Bewertung.') + '</td></tr>'
    out += '</tbody></table></div></div><p class="pf-empty" hidden>Keine Produkte entsprechen den Filtern.</p>'
    rubric = (
        'Konkretes Produkt oder Programm öffentlich angekündigt.',
        'Funktionsfähiger Prototyp belegt; Konzeptbilder reichen nicht.',
        'Tatsächlich durchgeführte Tests oder Demonstrationen belegt.',
        'Konkretes Kundenprogramm, Pilot oder beauftragte Validierung belegt.',
        'Tatsächliche operative Nutzung in einer relevanten Kundenaufgabe belegt.',
        'Laufende Serienfertigung, wiederholte Auslieferung oder gelieferte Skalierung belegt.')
    out += '<details class="pf-method"><summary><span class="pf-num">02 / METHODIK</span>Die sechs Reifestufen</summary><div class="pf-method-grid">' + ''.join('<div><b>' + str(i) + ' · ' + esc(stages[str(i)]) + '</b><p>' + esc(text) + '</p></div>' for i, text in enumerate(rubric, 1)) + '</div><p>Die höchste konkret gestützte Stufe zählt. Ankündigungen, Kapazitätsziele und Bestellungen sind keine erfolgte Serienlieferung. Varianten und Entwicklungsprogramme werden getrennt betrachtet. Die Skala bewertet keine technische Überlegenheit oder Marktattraktivität.</p></details>'
    out += '<details class="pf-profiles-disclosure" id="portfolio-profiles"><summary class="pf-head"><div><span class="pf-num">03 / DETAILPROFILE & EVIDENZ</span><h2>Von der Position zur Begründung.</h2></div><span class="pf-chevron" aria-hidden="true">+</span></summary><div class="pf-profiles-body"><div class="pf-profile-toolbar"><p>Ein Produkt öffnen, um Fakten, Einordnung und Originalbelege zu lesen.</p><button type="button" class="pf-expand" hidden>Alle Profile öffnen</button></div>'
    for p, a, grade, ids in entries:
        out += '<details class="pf-profile" id="product-' + esc(p["id"]) + '"><summary><span class="pf-grade">' + (str(grade) if grade else '?') + '</span><span><strong>' + esc(p["label"]) + '</strong><small>' + esc(p["domain"]) + ' · ' + (esc(stages[str(grade)]) if grade else 'Nicht eindeutig bestimmbar') + '</small></span><span class="pf-plus" aria-hidden="true">+</span></summary><div class="pf-profile-content"><dl><dt>Geprüfte Fakten</dt><dd>' + ''.join('<p>' + esc(claims[c]["statement"]) + '</p>' for c in p["claim_ids"]) + '</dd>'
        for group in p.get('sections', []):
            out += '<dt>' + esc(group['label']) + '</dt><dd>' + ''.join('<p>' + esc(claims[c]['statement']) + '</p>' for c in group['claim_ids']) + '</dd>'
        if a:
            out += '<dt>Analysteneinordnung</dt><dd><p>' + esc(a["statement"]) + '</p><p>' + esc(a["reasoning"]) + '</p>' + links([a["id"]]) + '</dd><dt>Evidenzgrenze</dt><dd>' + ''.join('<p>' + esc(v) + '</p>' for v in (a.get("uncertainty"), a.get("next_stage_limit"), a.get("coverage_note")) if v) + '</dd>'
        else:
            out += '<dt>Einordnung</dt><dd>Keine freigegebene Reifebewertung in dieser Faktenansicht.</dd>'
        out += '<dt>Originalquellen & Belegstellen</dt><dd>'
        for cid in ids:
            out += '<details class="pf-evidence"><summary>' + esc(claims[cid]["statement"]) + '</summary><p class="meta">' + esc(claims[cid]["kind"]) + '</p><p>' + esc(claims[cid]["uncertainty"]) + '</p>' + evidence(claims[cid]) + links([cid]) + '</details>'
        out += '</dd></dl></div></details>'
    out += '</div></details></div>'
    assets = Path(__file__).resolve().parents[1] / 'references/templates'
    return '<style>' + (assets / 'portfolio.css').read_text(encoding='utf-8') + '</style>' + out + '<script>' + (assets / 'portfolio.js').read_text(encoding='utf-8') + '</script>'
