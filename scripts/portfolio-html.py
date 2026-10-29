"""Render the approved portfolio style from reviewed product/interpretation records.

portfolio-status-v2: one column per product (highest documented stage); a '*'
marks a still-active previous stage and is explained in the product profile.
portfolio-maturity-v1 (six milestones) stays renderable for older runs.
"""
import html
from pathlib import Path

COLORS = ("#176e91", "#4d7852", "#7960a0", "#196a79", "#9a563e", "#ad8429")
V2 = "portfolio-status-v2"

LABELS = {
    "num": "01 / PORTFOLIO & PRODUKTSTATUS",
    "num_v1": "01 / PORTFOLIO & PRODUKTREIFE",
    "title": "Ein Portfolio. Eine transparente Skala.",
    "map": "Status-Matrix", "map_v1": "Reife-Matrix", "table": "Tabelle",
    "intro": "Zeile und Farbe kennzeichnen die Produktgruppe. Jedes Produkt steht in der höchsten öffentlich belegten Stufe. Produkt anklicken, Begründung lesen, Originalquelle öffnen.",
    "intro_v1": "Zeile und Farbe kennzeichnen die Produktgruppe. Die Position zeigt die öffentlich belegte Reife. Produkt anklicken, Begründung lesen, Originalquelle öffnen.",
    "star_legend": "* Zusätzlich aktuell noch in der vorherigen Stufe (z. B. im Betrieb und weiterhin in Serienproduktion). Details im Produktprofil.",
    "search": "Suche", "search_ph": "Produkt oder Anwendung", "group": "Produktgruppe", "all_groups": "Alle Produktgruppen",
    "status": "Status", "status_v1": "Reifestufe", "all_status": "Alle Stufen", "star_only": "Nur mit * (vorherige Stufe noch aktiv)",
    "origin": "Aussageursprung", "all_origins": "Alle Belegarten", "reset": "Zurücksetzen",
    "unknown": "Nicht eindeutig bestimmbar", "open": "offen", "unassessed": "Noch nicht eingeordnet",
    "unknown_note": "Keine freigegebene Stufe. Eine Beleglücke ist kein Nachweis niedriger Reife.",
    "unknown_v1": "Keine freigegebene Reifestufe. Eine Beleglücke ist kein Nachweis niedriger Reife.",
    "col_product": "Produkt", "col_group": "Gruppe", "col_stage": "Stufe", "col_reason": "Begründung",
    "fact_view": "Reine Faktenansicht; keine freigegebene Bewertung.",
    "empty": "Keine Produkte entsprechen den Filtern.",
    "method_num": "02 / METHODIK", "method_title": "Die vier Statusstufen", "method_title_v1": "Die sechs Reifestufen",
    "rubric": ("Konkretes Produkt oder Programm offiziell angekündigt; kein funktionsfähiger Prototyp belegt.",
               "Funktionsfähiger Prototyp oder Demonstrator, inklusive durchgeführter Tests/Qualifizierung; Konzeptbild oder Messemodell reicht nicht.",
               "Laufende Serienfertigung oder wiederholte Auslieferung belegt; Auftrag oder Kapazitätsziel allein reicht nicht.",
               "Tatsächlicher Einsatz bei mindestens einem Kunden in einer relevanten Aufgabe belegt."),
    "method_text": "Das Produkt steht in der höchsten konkret belegten Stufe. Ein * zeigt, dass die direkt vorherige Stufe heute zusätzlich noch aktiv und eigens belegt ist (Im Betrieb* = weiterhin in Serienproduktion; Serienproduktion* = Prototypen-/Qualifizierungsphase läuft parallel). Ohne * ist das Ende der Vorstufe nicht behauptet. Aufträge, Ankündigungen und Kapazitätsziele sind keine erreichte Stufe. Die Skala bewertet keine technische Überlegenheit oder Marktattraktivität.",
    "method_text_v1": "Die höchste konkret gestützte Stufe zählt. Ankündigungen, Kapazitätsziele und Bestellungen sind keine erfolgte Serienlieferung. Varianten und Entwicklungsprogramme werden getrennt betrachtet. Die Skala bewertet keine technische Überlegenheit oder Marktattraktivität.",
    "rubric_v1": ('Konkretes Produkt oder Programm öffentlich angekündigt.',
                  'Funktionsfähiger Prototyp belegt; Konzeptbilder reichen nicht.',
                  'Tatsächlich durchgeführte Tests oder Demonstrationen belegt.',
                  'Konkretes Kundenprogramm, Pilot oder beauftragte Validierung belegt.',
                  'Tatsächliche operative Nutzung in einer relevanten Kundenaufgabe belegt.',
                  'Laufende Serienfertigung, wiederholte Auslieferung oder gelieferte Skalierung belegt.'),
    "profiles_num": "03 / DETAILPROFILE & EVIDENZ", "profiles_title": "Von der Position zur Begründung.",
    "profiles_hint": "Ein Produkt öffnen, um Fakten, Einordnung und Originalbelege zu lesen.", "open_all": "Alle Profile öffnen", "close_all": "Alle Profile schließen",
    "count_of": "von", "count_entries": "Einträgen",
    "dt_status": "Status", "dt_also": "* Zusätzlich", "dt_facts": "Geprüfte Fakten", "dt_assessment": "Analysteneinordnung",
    "dt_limits": "Evidenzgrenze", "dt_sources": "Originalquellen & Belegstellen", "dt_none": "Einordnung",
    "none": "Keine freigegebene Reifebewertung in dieser Faktenansicht.", "also": "zusätzlich",
}


def esc(value):
    return html.escape(str(value), quote=True)


def render(inventory, assessments, claims, evidence, links, labels=None):
    products = inventory["products"]
    if not products:
        return ""
    L = {**LABELS, **(labels or {})}
    v2 = inventory.get("method_id", V2) == V2
    stages = inventory["stages"]
    stage_label = {**stages, "unknown": L["unknown"], "unassessed": L["unassessed"]}
    groups = list(dict.fromkeys(p["domain"] for p in products))
    origins = {p['id']: sorted({claims[c]['kind'] for c in p['claim_ids']}) for p in products}
    colors = {g: COLORS[i % len(COLORS)] for i, g in enumerate(groups)}
    entries = []
    for p in products:
        a = assessments.get(p["id"])
        if v2:
            stage = (a.get("stage") or "unknown") if a else "unassessed"
        else:
            stage = str(a["score"]) if a and a.get("score") else None
        star = (a or {}).get("also_previous") if v2 and stage else None
        ids = list(dict.fromkeys([*p["claim_ids"], *(c for group in p.get('sections', []) for c in group['claim_ids']), *(a.get("depends_on", []) if a else [])]))
        entries.append(dict(p=p, a=a, stage=stage or "unknown", star=star, ids=ids))

    def mark(e):
        return '<span class="pf-star" aria-hidden="true">*</span>' if e["star"] else ''

    def stage_text(e):
        text = stage_label[e["stage"]] if v2 or e["stage"] in ("unknown", "unassessed") else e["stage"] + ' · ' + stages[e["stage"]]
        if e["star"]:
            text += ' * (' + L["also"] + ': ' + stages[e["star"]["stage"]] + ')'
        return text

    def product_link(e):
        p = e["p"]
        aria = p["label"] + ' · ' + stage_text(e)
        badge = '' if v2 else '<small>' + (e["stage"] if e["stage"] != "unknown" else L["open"]) + '</small>'
        return ('<a class="pf-map-item" data-pf-item="' + esc(p["id"]) + '" href="#product-' + esc(p["id"]) + '" style="--pf-domain:' + colors[p["domain"]]
                + '" title="' + esc(aria) + '" aria-label="' + esc(aria) + '"><span class="pf-dot"></span><span>' + esc(p.get("short_label", p["label"])) + mark(e) + '</span>' + badge + '</a>')

    data = ' data-pf-of="' + esc(L["count_of"]) + '" data-pf-entries="' + esc(L["count_entries"]) + '" data-pf-open="' + esc(L["open_all"]) + '" data-pf-close="' + esc(L["close_all"]) + '"'
    out = '<div id="briefing-portfolio" class="pf-root' + (' pf-v2' if v2 else '') + '"' + data + '>'
    out += '<div class="pf-head"><div><span class="pf-num">' + esc(L["num"] if v2 else L["num_v1"]) + '</span><h2>' + esc(L["title"]) + '</h2></div><div class="pf-views" hidden><button type="button" data-pf-view="map" aria-pressed="true">' + esc(L["map"] if v2 else L["map_v1"]) + '</button><button type="button" data-pf-view="table" aria-pressed="false">' + esc(L["table"]) + '</button></div></div>'
    out += '<p class="pf-intro">' + esc(L["intro"] if v2 else L["intro_v1"]) + '</p>'
    stage_options = ''.join('<option value="' + esc(k) + '">' + (esc(v) if v2 else k + ' · ' + esc(v)) + '</option>' for k, v in stages.items())
    stage_options += '<option value="unknown">' + esc(L["unknown"]) + '</option>' + ('<option value="star">' + esc(L["star_only"]) + '</option>' if v2 else '')
    out += ('<div class="pf-filters" hidden><label>' + esc(L["search"]) + '<input type="search" data-pf-filter="query" placeholder="' + esc(L["search_ph"]) + '"></label><label>' + esc(L["group"])
            + '<select data-pf-filter="domain"><option value="">' + esc(L["all_groups"]) + '</option>' + ''.join('<option>' + esc(g) + '</option>' for g in groups)
            + '</select></label><label>' + esc(L["status"] if v2 else L["status_v1"]) + '<select data-pf-filter="grade"><option value="">' + esc(L["all_status"]) + '</option>' + stage_options
            + '</select></label><label>' + esc(L["origin"]) + '<select data-pf-filter="origin"><option value="">' + esc(L["all_origins"]) + '</option>'
            + ''.join('<option>' + esc(k) + '</option>' for k in sorted({k for kinds in origins.values() for k in kinds}))
            + '</select></label><button type="button" class="pf-reset">' + esc(L["reset"]) + '</button></div><p class="pf-count" aria-live="polite"></p>')
    columns = list(stages) + (["unknown"] if v2 else [])
    out += '<div class="pf-map-view"><div class="pf-table-wrap"><table class="pf-maturity-map"><thead><tr><th>' + esc(L["group"]) + '</th>'
    for k in columns:
        if k == "unknown":
            out += '<th scope="col" class="pf-unknown-header"><span>' + esc(L["unknown"]) + '</span></th>'
        else:
            out += '<th scope="col">' + ('' if v2 else '<b>' + k + '</b>') + '<span>' + esc(stages[k]) + '</span></th>'
    out += '</tr></thead><tbody>'
    for g in groups:
        out += '<tr data-pf-group="' + esc(g) + '"><th scope="row"><span class="pf-domain-mark" style="background:' + colors[g] + '"></span>' + esc(g) + '</th>'
        for k in columns:
            cls = ' class="pf-unknown-cell"' if k == "unknown" else ''
            out += '<td' + cls + '>' + ''.join(product_link(e) for e in entries if e["p"]["domain"] == g and e["stage"] == k) + '</td>'
        out += '</tr>'
    out += '</tbody></table></div>'
    if v2:
        out += '<p class="pf-star-legend">' + esc(L["star_legend"]) + '</p>'
        pending = [e for e in entries if e["stage"] == "unassessed"]
        out += '<aside class="pf-unknown"' + ('' if pending else ' hidden') + '><h3>' + esc(L["unassessed"]) + '</h3><p>' + esc(L["fact_view"]) + '</p>' + ''.join(product_link(e) for e in pending) + '</aside></div>'
    else:
        unknown = [e for e in entries if e["stage"] == "unknown"]
        out += '<aside class="pf-unknown"' + ('' if unknown else ' hidden') + '><h3>' + esc(L["unknown"]) + '</h3><p>' + esc(L["unknown_v1"]) + '</p>' + ''.join(product_link(e) for e in unknown) + '</aside></div>'
    out += '<div class="pf-result-view" hidden><div class="pf-table-wrap"><table class="pf-results"><thead><tr><th>' + esc(L["col_product"]) + '</th><th>' + esc(L["col_group"]) + '</th><th>' + esc(L["col_stage"]) + '</th><th>' + esc(L["col_reason"]) + '</th></tr></thead><tbody>'
    for e in entries:
        p, a = e["p"], e["a"]
        out += ('<tr data-pf-result="' + esc(p["id"]) + '" data-pf-domain="' + esc(p["domain"]) + '" data-pf-stage="' + esc(e["stage"]) + '" data-pf-star="' + ('1' if e["star"] else '')
                + '" data-pf-origin="' + esc('|'.join(origins[p['id']])) + '"><td><a href="#product-' + esc(p["id"]) + '">' + esc(p["label"]) + mark(e) + '</a></td><td>' + esc(p["domain"])
                + '</td><td>' + esc(stage_text(e)) + '</td><td>' + esc(a["reasoning"] if a else L["fact_view"]) + '</td></tr>')
    out += '</tbody></table></div></div><p class="pf-empty" hidden>' + esc(L["empty"]) + '</p>'
    rubric = L["rubric"] if v2 else L["rubric_v1"]
    out += ('<details class="pf-method"><summary><span class="pf-num">' + esc(L["method_num"]) + '</span>' + esc(L["method_title"] if v2 else L["method_title_v1"])
            + '</summary><div class="pf-method-grid">' + ''.join('<div><b>' + ('' if v2 else k + ' · ') + esc(stages[k]) + '</b><p>' + esc(t) + '</p></div>' for k, t in zip(stages, rubric))
            + '</div><p>' + esc(L["method_text"] if v2 else L["method_text_v1"]) + '</p></details>')
    out += ('<details class="pf-profiles-disclosure" id="portfolio-profiles"><summary class="pf-head"><div><span class="pf-num">' + esc(L["profiles_num"]) + '</span><h2>' + esc(L["profiles_title"])
            + '</h2></div><span class="pf-chevron" aria-hidden="true">+</span></summary><div class="pf-profiles-body"><div class="pf-profile-toolbar"><p>' + esc(L["profiles_hint"])
            + '</p><button type="button" class="pf-expand" hidden>' + esc(L["open_all"]) + '</button></div>')

    def statements(ids):
        return ''.join('<p>' + esc(claims[c]["statement"]) + '</p>' for c in ids)

    for e in entries:
        p, a = e["p"], e["a"]
        badge = (esc(stage_label[e["stage"]]) + mark(e)) if v2 else (e["stage"] if e["stage"] != "unknown" else '?')
        out += ('<details class="pf-profile" id="product-' + esc(p["id"]) + '"><summary><span class="pf-grade' + (' pf-stage-' + esc(e["stage"]) if v2 else '') + '">' + badge
                + '</span><span><strong>' + esc(p["label"]) + mark(e) + '</strong><small>' + esc(p["domain"]) + ' · ' + esc(stage_text(e))
                + '</small></span><span class="pf-plus" aria-hidden="true">+</span></summary><div class="pf-profile-content"><dl>')
        if v2 and a and e["stage"] != "unknown":
            out += '<dt>' + esc(L["dt_status"]) + '</dt><dd><p><b>' + esc(stages[e["stage"]]) + '</b></p>' + statements(a.get("stage_basis", [])) + links(a.get("stage_basis", [])) + '</dd>'
            if e["star"]:
                out += ('<dt class="pf-also">' + esc(L["dt_also"]) + ': ' + esc(stages[e["star"]["stage"]]) + '</dt><dd class="pf-also"><p>' + esc(e["star"]["note"]) + '</p>'
                        + statements(e["star"]["basis"]) + links(e["star"]["basis"]) + '</dd>')
        shown = set(a.get("stage_basis", []) + (e["star"]["basis"] if e["star"] else [])) if v2 and a else set()
        rest = [c for c in p["claim_ids"] if c not in shown]
        if rest:
            out += '<dt>' + esc(L["dt_facts"]) + '</dt><dd>' + statements(rest) + '</dd>'
        for group in p.get('sections', []):
            out += '<dt>' + esc(group['label']) + '</dt><dd>' + statements(group['claim_ids']) + '</dd>'
        if a:
            out += ('<dt>' + esc(L["dt_assessment"]) + '</dt><dd><p>' + esc(a["statement"]) + '</p><p>' + esc(a["reasoning"]) + '</p>' + links([a["id"]]) + '</dd><dt>' + esc(L["dt_limits"])
                    + '</dt><dd>' + ''.join('<p>' + esc(v) + '</p>' for v in (a.get("uncertainty"), a.get("next_stage_limit"), a.get("coverage_note")) if v) + '</dd>')
        else:
            out += '<dt>' + esc(L["dt_none"]) + '</dt><dd>' + esc(L["none"]) + '</dd>'
        out += '<dt>' + esc(L["dt_sources"]) + '</dt><dd>'
        for cid in e["ids"]:
            out += '<details class="pf-evidence"><summary>' + esc(claims[cid]["statement"]) + '</summary><p class="meta">' + esc(claims[cid]["kind"]) + '</p><p>' + esc(claims[cid]["uncertainty"]) + '</p>' + evidence(claims[cid]) + links([cid]) + '</details>'
        out += '</dd></dl></div></details>'
    out += '</div></details></div>'
    assets = Path(__file__).resolve().parents[1] / 'references/templates'
    return '<style>' + (assets / 'portfolio.css').read_text(encoding='utf-8') + '</style>' + out + '<script>' + (assets / 'portfolio.js').read_text(encoding='utf-8') + '</script>'
