#!/usr/bin/env python3
"""Render reviewed facts-v2/interpret-v2 into one offline HTML; no model or web calls."""
import argparse
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("interpretation", Path(__file__).with_name("check-interpretation.py"))
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)

KINDS = {"target", "partner", "customer", "jv", "owner", "supplier", "subsidiary",
         "project", "person", "institution", "other"}
CATEGORIES = {"partner", "customer", "jv", "owner", "supplier", "subsidiary", "project", "other"}
FIELDS = ("company_facts", "events", "products", "regions", "topics")


def esc(value):
    return html.escape(str(value), quote=True)


def safe_json(value):
    raw = json.dumps(value, ensure_ascii=False, allow_nan=False)
    for old, new in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e"),
                     ("\u2028", "\\u2028"), ("\u2029", "\\u2029")):
        raw = raw.replace(old, new)
    return raw


def paragraphs(values):
    return "".join("<p>" + esc(x) + "</p>" for x in values if x)


def build(manifest, facts, basis, positioning=None, positioning_context=None,
          swot=None, swot_context=None, final=None, plan=None, full=False):
    claims, reviews, hashes = CHECK.env(manifest, facts, basis)
    if basis.get("input_fingerprint") != CHECK.digest(facts):
        raise ValueError("basis review packet snapshot missing/stale; review module mappings then stamp again")
    selected = manifest.get("selected_roles")
    if not isinstance(selected, list) or not selected or len(set(selected)) != len(selected):
        raise ValueError("manifest selected_roles invalid")
    views = CHECK.index([dict(id=v.get("role"), **v) for v in facts.get("module_views", [])], "module_views")
    if set(views) != set(selected) or not set(views) <= {"context", "portfolio", "cluster", "market"}:
        raise ValueError("module_views must match selected_roles")
    contexts = facts.get("module_context", [])
    if any(c.get("status") == "blockiert" for c in contexts):
        raise ValueError("blocked factual module")
    sources = CHECK.index(facts["sources"], "sources")
    interpreted, validations = {}, []
    for role, output, context in (("positioning", positioning, positioning_context), ("swot", swot, swot_context)):
        if (output is None) != (context is None):
            raise ValueError(role + ": output and context required together")
        if output is None:
            continue
        if output.get("role") != role or output.get("status") == "blockiert":
            raise ValueError(role + ": wrong role or blocked output")
        if any(r.get("blocking") for r in output.get("research_requests", [])):
            raise ValueError(role + ": blocking research request")
        report = CHECK.validate_output(manifest, facts, basis, context, output,
            latest_positioning=positioning if role == "swot" else None,
            latest_positioning_context=positioning_context if role == "swot" else None, latest_plan=plan)
        if report["errors"]:
            raise ValueError("; ".join(report["errors"]))
        if context.get("matrix") is not None:
            market = views.get("market", {})
            for key in ("peers", "observations", "gaps", "coverage"):
                if context["matrix"].get(key, []) != market.get(key, []):
                    raise ValueError("matrix mapping differs from reviewed current market: " + key)
        validations.append(report)
        for row in output["interpretations"]:
            if row["id"] in interpreted:
                raise ValueError("duplicate interpretation")
            if row.get("cell_status") == "weitere Faktenprüfung nötig":
                raise ValueError("matrix has pending full fact check")
            interpreted[row["id"]] = row
    if validations:
        report = CHECK.merge_reports(validations)
        if not isinstance(final, dict) or final.get("schema_version") != 1 or final.get("phase") != "final" or final.get("status") != "freigegeben" or final.get("material_errors") != []:
            raise ValueError("final interpretation review not released")
        if any(final.get(k) != manifest.get(k) for k in ("run_id", "company", "as_of")):
            raise ValueError("final review identity mismatch")
        final_rows = CHECK.index(final.get("claims"), "final review")
        for cid, fp in report["fingerprints"].items():
            if CHECK.ready(cid, final_rows, report["fingerprints"]):
                raise ValueError("final full review missing/stale: " + cid)
    elif final is not None:
        raise ValueError("final review supplied without interpretations")
    summary_rows = [r for r in interpreted.values() if r["section"] == "executive_summary"]
    if full and (set(selected) != {"context", "portfolio", "cluster", "market"} or
                 positioning is None or swot is None or not 4 <= len(summary_rows) <= 6):
        raise ValueError("full briefing requires four facts roles, positioning, SWOT and 4–6 summary claims")

    def require(ids, trail=()):
        if not isinstance(ids, list) or not ids:
            raise ValueError("view row needs claim_ids")
        for cid in ids:
            if cid not in claims or cid in trail:
                raise ValueError("unknown/cyclic view fact: " + str(cid))
            reason = CHECK.ready(cid, reviews, hashes)
            if reason:
                raise ValueError(cid + ": " + reason)
            parents = claims[cid].get("depends_on", [])
            if parents:
                require(parents, (*trail, cid))

    topics = manifest.get("topics", [])
    if not isinstance(topics, list):
        raise ValueError("topics must be ordered id/label rows")
    topic_index = CHECK.index(topics, "topics")
    if any(not CHECK.text(t.get("label")) for t in topics):
        raise ValueError("topic label required")
    for row in interpreted.values():
        if row['section'].startswith('topic:') and row['section'][6:] not in topic_index:
            raise ValueError('interpretation references unknown requested topic')
    for role, view in views.items():
        for field in FIELDS:
            rows = view.get(field, [])
            CHECK.index(rows, role + ": " + field)
            for row in rows:
                if not CHECK.text(row.get("label")):
                    raise ValueError("view label required")
                require(row.get("claim_ids"))
                if field == "topics" and row["id"] not in topic_index:
                    raise ValueError("unknown requested topic")
                if field == "events" and row.get("date") is not None:
                    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(row["date"])):
                        raise ValueError("event date invalid")
                    date.fromisoformat(row["date"])
                sections = row.get("sections", [])
                if not isinstance(sections, list):
                    raise ValueError("region sections must be a list")
                for section in sections:
                    if not CHECK.text(section.get("label")):
                        raise ValueError("region section label missing")
                    require(section.get("claim_ids"))
        profile = view.get("profile")
        if profile is not None:
            if role != "context" or not manifest.get("person") or not CHECK.text(profile.get("name")):
                raise ValueError("profile needs named person and context role")
            require(profile.get("claim_ids"))
            if any(not cid.startswith("H") for cid in profile["claim_ids"]):
                raise ValueError("profile uses non-professional-person claims")

    network = facts.get("network")
    if "cluster" in selected and not isinstance(network, dict):
        raise ValueError("cluster requires current network, even if target only")
    if network is not None:
        if "cluster" not in selected or network.get("schema_version") != 1:
            raise ValueError("network role/schema mismatch")
        for node in network["nodes"]:
            if node.get("kind") not in KINDS or not CHECK.text(node.get("label")):
                raise ValueError("invalid network node")
            if node.get("cluster", "capital") not in {"capital", "structure", "technology", "market"}:
                raise ValueError("invalid network cluster")
            if "focus" in node and not isinstance(node["focus"], bool):
                raise ValueError("network focus must be boolean")
        for product in network["products"]:
            if not CHECK.text(product.get("label")):
                raise ValueError("network product label missing")
        for edge in network["edges"]:
            for field in ("type", "summary", "status"):
                if not CHECK.text(edge.get(field)):
                    raise ValueError("invalid network edge " + field)
            if not re.fullmatch(r"\d{4}-\d{2}(?:-\d{2})?", str(edge.get("as_of"))):
                raise ValueError("invalid network event date")
            date.fromisoformat(edge["as_of"] + ("-01" if len(edge["as_of"]) == 7 else ""))
            cats = edge.get("categories")
            if not isinstance(cats, list) or not cats or any(c not in CATEGORIES for c in cats):
                raise ValueError("invalid network categories")
            if "interpretation" in edge or any(not c.startswith("C") for c in edge["claim_ids"]):
                raise ValueError("network only contains factual C-claims")
            if not set(edge["source_ids"]) <= {s for c in edge["claim_ids"] for s in claims[c]["source_ids"]}:
                raise ValueError("network evidence not in referenced claims")
            require(edge["claim_ids"])

    def links(ids):
        return " ".join('<a class="claim" href="#' + esc(cid) + '">' + esc(cid) + '</a>' for cid in ids)

    def source_html(src):
        extras = [src.get("published_date") or "o. D.", src.get("source_kind"),
                  "Abruf " + src["accessed_date"]]
        extras += [label + " " + str(src[key]) for key, label in
                   (("report_year", "Geschäftsjahr"), ("page", "Seite"), ("section", "Abschnitt")) if src.get(key)]
        return '<a href="' + esc(src["url"]) + '" target="_blank" rel="noopener noreferrer">' + esc(src["name"] + " · " + src["title"]) + '</a><span class="meta"> · ' + esc(" · ".join(x for x in extras if x)) + '</span>'

    def evidence(row):
        parts = []
        mapped = {i["source_id"]: i for i in row.get("evidence_items", [])}
        for sid in row["source_ids"]:
            item = mapped.get(sid)
            text = (item["mode"] + ": " + item["text"]) if item else row["evidence"]
            location = item["location"] if item else row["location"]
            parts.append('<li>' + source_html(sources[sid]) + '<p>' + esc(text) + '</p><p class="meta">Belegstelle: ' + esc(location) + '</p></li>')
        return '<ul class="evidence">' + "".join(parts) + '</ul>'

    def fact_card(row, title=None):
        return '<details class="card"><summary>' + esc(title or row["statement"]) + '</summary><p>' + esc(row["statement"]) + '</p>' + links([row["id"]]) + '</details>'

    def view_card(row):
        body = "".join('<p>' + esc(claims[c]["statement"]) + '</p>' for c in row["claim_ids"])
        body += links(row["claim_ids"])
        for section in row.get("sections", []):
            body += '<h4>' + esc(section["label"]) + '</h4>' + "".join('<p>' + esc(claims[c]["statement"]) + '</p>' for c in section["claim_ids"]) + links(section["claim_ids"])
        return '<details class="card"><summary>' + esc(row["label"]) + '</summary>' + body + '</details>'

    def interp_card(row):
        return '<details class="card"><summary>' + esc(row["statement"]) + '</summary><p class="meta">Analysteninterpretation</p>' + paragraphs([row["reasoning"], row["uncertainty"]]) + links([row["id"]]) + '</details>'

    def section(title, body, ident=None):
        return '<section class="module"' + (' id="' + esc(ident) + '"' if ident else '') + '><h2>' + esc(title) + '</h2>' + body + '</section>' if body else ''

    def grid(items):
        return '<div class="cards">' + "".join(items) + '</div>' if items else ''

    def note_rows(rows):
        out = []
        for row in rows:
            if isinstance(row, dict):
                body = ''
                for key, value in row.items():
                    if isinstance(value, list):
                        value = "; ".join(str(v) if not isinstance(v, dict) else " · ".join(str(x) for x in v.values()) for v in value)
                    elif isinstance(value, dict):
                        value = " · ".join(str(x) for x in value.values())
                    body += '<dt>' + esc(key.replace('_', ' ')) + '</dt><dd>' + esc(value) + '</dd>'
                out.append('<dl class="note">' + body + '</dl>')
            else:
                out.append('<p>' + esc(row) + '</p>')
        return "".join(out)

    fictional = any(s.get("fictional") for s in sources.values())
    main = section("Executive Summary", grid([interp_card(r) for r in summary_rows]))
    if not summary_rows:
        main += section("Unternehmen im Überblick", grid([view_card(r) for v in views.values() for r in v.get("company_facts", [])]))
    for index, topic in enumerate(topics):
        cards = [view_card(r) for v in views.values() for r in v.get("topics", []) if r["id"] == topic["id"]]
        cards += [interp_card(r) for r in interpreted.values() if r["section"] == "topic:" + topic["id"]]
        main += section(topic["label"], grid(cards) or '<p>Keine freigegebenen Befunde für dieses Thema.</p>', 'topic-' + str(index))
    events = [r for v in views.values() for r in v.get("events", [])]
    main += section("Aktuelle Entwicklungen", '<div class="timeline">' + "".join('<div class="event"><time>' + esc(r.get("date") or 'Datum öffentlich nicht belegt') + '</time>' + view_card(r) + '</div>' for r in events) + '</div>' if events else '')
    if network:
        nodes = CHECK.index(network["nodes"], "nodes")
        products = CHECK.index(network["products"], "products")
        rows = []
        for e in network["edges"]:
            detail = '<p>' + esc(e["summary"]) + '</p>' + links(e["claim_ids"])
            for key, label in (("capital_share", "Kapitalanteil"), ("voting_share", "Stimmrechte"), ("control", "Kontrolle"), ("uncertainty", "Evidenzgrenze")):
                if e.get(key) is not None:
                    detail += '<p>' + esc(label + ': ' + str(e[key])) + '</p>'
            if e["product_ids"]:
                detail += '<p>Produktbezug: ' + esc(', '.join(products[p]["label"] for p in e["product_ids"])) + '</p>'
            rows.append('<tr><td>' + esc(nodes[e["from"]]["label"] + ' → ' + nodes[e["to"]]["label"]) + '</td><td>' + esc(e["type"]) + detail + '</td><td>' + esc(e["status"] + ' · ' + e["as_of"]) + '</td><td>' + '<br>'.join(source_html(sources[s]) for s in e["source_ids"]) + '</td></tr>')
        fragment = (ROOT / 'references/templates/cluster-network.html').read_text(encoding='utf-8')
        fragment = fragment.replace('__CLUSTER_NETWORK_JSON__', safe_json(network))
        fragment = fragment.replace('<tbody></tbody>', '<tbody>' + ''.join(rows) + '</tbody>', 1)
        fragment = fragment.replace("const tableBody=root.querySelector('tbody');", "const tableBody=root.querySelector('tbody');tableBody.replaceChildren();", 1)
        fragment = fragment.replace("window.addEventListener('beforeprint',()=>{root.querySelector('.cn-table').open=true;});", "", 1)
        main += section("Cluster · Technologie, Industrie & Marktzugang", fragment)
    main += section("Portfolio & Produktreife", grid([view_card(r) for v in views.values() for r in v.get("products", [])]))
    if positioning_context and positioning_context.get("matrix"):
        criteria = plan["criteria"]
        cells = {(r["peer_id"], r["criterion_id"]): r for r in positioning["interpretations"] if r.get("type") == "matrix_cell"}
        head = '<tr><th>Akteur</th>' + ''.join('<th>' + esc(c['label']) + '<small>' + esc(c['display_type']) + '</small></th>' for c in criteria) + '</tr>'
        rows = []
        for peer in positioning_context['matrix']['peers']:
            line = '<th scope="row">' + esc(peer['label']) + '</th>'
            for c in criteria:
                r = cells[peer['id'], c['id']]
                value = r['value'] if r['cell_status'] == 'bewertet' else r['cell_status']
                bar = ''
                if r['cell_status'] == 'bewertet' and c['display_type'] == 'Evidenzstufe':
                    anchors = sorted(c['anchors'], key=lambda k: float(k))
                    key = str(int(r['value'])) if isinstance(r['value'], float) and r['value'].is_integer() else str(r['value'])
                    value = c['anchors'][key]
                    bar = '<span class="steps" aria-hidden="true">' + ''.join('<i class="' + ('on' if n <= anchors.index(key) else '') + '"></i>' for n in range(len(anchors))) + '</span>'
                if r['cell_status'] == 'bewertet' and c['display_type'] == 'Kennzahl':
                    value = str(value) + ' ' + c['unit']
                line += '<td><a class="cell" href="#' + esc(r['id']) + '">' + esc(value) + bar + '</a></td>'
            rows.append('<tr>' + line + '</tr>')
        rubric = ''.join('<h4>' + esc(c['label']) + '</h4>' + paragraphs([c['question'], c['evidence_required'], c.get('conditions')]) + (note_rows(c.get('anchors', {}).values()) if c.get('anchors') else '') for c in criteria)
        title = 'Capability Matrix · fiktiver Beispieldatensatz' if fictional else 'Capability Matrix · öffentlich belegte Reife'
        main += section(title, '<p>Zellen öffnen Begründung, Evidenz und Grenzen. Stufen gelten je Kriterium; kein Gesamt-Ranking.</p><div class="table-wrap"><table>' + head + ''.join(rows) + '</table></div><details><summary>Kriterien und Skalen</summary>' + rubric + '</details>')
    extra = [r for r in interpreted.values() if r['id'].startswith('I') and r['section'] != 'executive_summary' and not r['section'].startswith('topic:') and r.get('type') != 'matrix_cell']
    scored = []
    for r in extra:
        if 'score' in r:
            method = next(m for m in plan['assessment_methods'] if m['id'] == r['method_id'])
            anchors = sorted(method['anchors'], key=lambda k: float(k))
            bar = '<span class="steps" aria-hidden="true">' + ''.join('<i class="' + ('on' if n <= anchors.index(str(r['score'])) else '') + '"></i>' for n in range(len(anchors))) + '</span>'
            scored.append('<div><p class="meta">' + esc(r['subject']) + ' · ' + esc(method['anchors'][str(r['score'])]) + '</p>' + bar + interp_card(r) + '</div>')
        else:
            scored.append(interp_card(r))
    main += section('Einordnung · Technologie, Industrie & Markt', grid(scored))
    if swot:
        quadrants = []
        for key, title in (('Strengths', 'Stärken'), ('Weaknesses', 'Schwächen'), ('Opportunities', 'Chancen'), ('Threats', 'Risiken')):
            cards = [interp_card(r) for r in swot['interpretations'] if r['category'] == key]
            quadrants.append('<div class="quadrant"><h3>' + title + '</h3>' + (''.join(cards) or '<p class="meta">Keine freigegebene Aussage in dieser Kategorie.</p>') + '</div>')
        main += section('SWOT · Analysteninterpretation', '<div class="swot">' + ''.join(quadrants) + '</div>')
    limits = ''.join('<details><summary>' + esc(v['role']) + ' · Rechercheabdeckung und offene Punkte</summary>' + note_rows(v.get('gaps', [])) + note_rows(v.get('coverage', [])) + note_rows(v.get('report_log', [])) + '</details>' for v in views.values())
    limits += ''.join(paragraphs(c.get('shared_limitations', [])) + paragraphs([c.get('document_scope')]) for c in contexts)
    for o in (positioning, swot):
        if o:
            limits += paragraphs(o.get('shared_limitations', [])) + note_rows(o.get('research_requests', []))
    main += section('Datenlücken & offene Fragen', limits)
    pages = [('page-main', 'Überblick', main)]
    if manifest.get('person'):
        profile = views.get('context', {}).get('profile')
        person = manifest['person']
        if isinstance(person, dict):
            if not CHECK.text(person.get('name')):
                raise ValueError('person object requires name')
            role = person.get('position') or person.get('role')
            if role is not None and not CHECK.text(role):
                raise ValueError('person role must be text')
            person = person['name'] + (' · ' + role if role else '')
        if not CHECK.text(person):
            raise ValueError('person must be text or name/role object')
        body = '<p class="meta">Gesprächspartner aus dem Auftrag (Nutzerangabe): ' + esc(person) + '</p>'
        if profile:
            body += grid([fact_card(claims[c]) for c in profile['claim_ids']])
        else:
            body += '<p>Berufliches Profil öffentlich nicht verifiziert.</p>'
        pages.append(('page-profile', 'Gesprächspartner', section('Beruflicher Gesprächspartner-Kontext', body)))
    regions = []
    for role, v in views.items():
        if v.get('regions'):
            regions.append(section('Unternehmenspräsenz' if role == 'portfolio' else 'Markt & Industrie', grid([view_card(r) for r in v['regions']])))
    if regions:
        pages.append(('page-regions', 'Regionen & Märkte', ''.join(regions)))
    register = ''
    for cid, row in claims.items():
        status = reviews.get(cid, {}).get('status', 'nicht einzeln geprüft')
        depth = reviews.get(cid, {}).get('depth', 'nicht geprüft')
        if CHECK.ready(cid, reviews, hashes) and status in CHECK.ACCEPTED:
            status = 'Prüfbefund veraltet'
        register += '<details class="claim-detail" id="' + esc(cid) + '"><summary>' + esc(cid + ' · ' + row['statement']) + '</summary><p class="meta">' + esc(row['kind'] + ' · Prüftiefe ' + depth + ' · ' + status) + '</p>' + paragraphs([row['uncertainty']]) + evidence(row) + '</details>'
    for cid, row in interpreted.items():
        register += '<details class="claim-detail" id="' + esc(cid) + '"><summary>' + esc(cid + ' · ' + row['statement']) + '</summary><p class="meta">Analysteninterpretation · vollständig geprüft im Schluss-Review</p>' + paragraphs([row['reasoning'], row['method'], row['uncertainty'], row.get('next_stage_limit'), row.get('coverage_note')]) + links(row['depends_on']) + '</details>'
    register += '<h3>Dokumente</h3>' + ''.join('<p>' + source_html(s) + '</p>' for s in sources.values())
    pages.append(('page-sources', 'Details & Quellen', section('Aussagen, Belegstellen & Originalquellen', register)))
    tabs = ''.join('<button type="button" data-page="' + ident + '" aria-controls="' + ident + '">' + label + '</button>' for ident, label, _ in pages)
    content = ''.join('<div class="page" id="' + ident + '">' + body + '</div>' for ident, _, body in pages)
    template = (ROOT / 'references/templates/briefing.html').read_text(encoding='utf-8')
    values = {'TITLE': esc(manifest['company']), 'DATE': esc(manifest['as_of']), 'SCOPE': esc(manifest.get('scope', '')),
              'BADGE': 'Fiktive Testdaten · keine reale Firmenanalyse' if fictional else 'Geprüfte Fakten & Analysteninterpretation',
              'TABS': tabs, 'CONTENT': content}
    # One-pass substitution: user text containing template tokens must remain literal.
    return re.sub(r'__([A-Z]+)__', lambda m: values[m[1]], template)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('manifest', 'facts', 'basis-review', 'positioning', 'positioning-context',
                'swot', 'swot-context', 'final-review', 'plan', 'out'):
        p.add_argument('--' + key, required=key in {'manifest', 'facts', 'basis-review', 'out'})
    p.add_argument('--full', action='store_true')
    args = p.parse_args()
    paths = [v for k, v in vars(args).items() if k not in {'out', 'full'} and v]
    try:
        target = Path(args.out)
        if target.resolve() in {Path(x).resolve() for x in paths}:
            raise ValueError('output must not overwrite inputs')
        values = {k: CHECK.read(v) if v else None for k, v in vars(args).items() if k not in {'out', 'full'}}
        result = build(values['manifest'], values['facts'], values['basis_review'], values['positioning'],
            values['positioning_context'], values['swot'], values['swot_context'], values['final_review'], values['plan'], args.full)
        target.parent.mkdir(parents=True, exist_ok=True)
        temp = target.with_name(target.name + '.tmp')
        temp.write_text(result, encoding='utf-8')
        temp.replace(target)
        print(json.dumps({'output': str(target), 'bytes': len(result.encode()), 'status': 'rendered'}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(json.dumps({'errors': [str(error)]}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    sys.exit(main())
