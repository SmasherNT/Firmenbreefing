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
PORTFOLIO = CHECK.helper("portfolio_html", "portfolio-html.py")
PROFILE = CHECK.helper("profile_html", "profile-html.py")
CAPABILITY = CHECK.helper("capability_html", "capability-html.py")
MARKET = CHECK.helper("market_html", "market-html.py")
FOCUS = CHECK.helper("focus_html", "focus-html.py")
MODULE_INSIGHTS = CHECK.MODULE_INSIGHTS
PRESENCE = CHECK.PRESENCE
CLUSTER = CHECK.helper("cluster_html", "cluster-html.py")

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
    expected_views = set(selected) | {"focus:" + str(r.get("id")) for r in manifest.get("focus_pages", [])}
    if set(views) != expected_views or not set(selected) <= {"context", "portfolio", "cluster", "market"}:
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
    summary_rows = sorted((r for r in interpreted.values() if r["section"] == CHECK.SUMMARY_SECTION), key=lambda r: r["display_order"])
    highlight_rows = sorted((r for r in interpreted.values() if r["section"] == CHECK.HIGHLIGHT_SECTION), key=lambda r: r["display_order"])
    if full and (set(selected) != {"context", "portfolio", "cluster", "market"} or
                 positioning is None or swot is None or not 4 <= len(summary_rows) <= 6 or len(highlight_rows) != 3):
        raise ValueError("full briefing requires four facts roles, positioning, SWOT, 4–6 summary claims and three reviewed highlights")
    inventory = CHECK.portfolio_context(facts)
    product_assessments = {r['product_id']: r for r in interpreted.values() if CHECK.product_assessment(r)}
    if full and (positioning_context.get('portfolio') != inventory or
                 set(product_assessments) != {p['id'] for p in inventory['products']}):
        raise ValueError('full briefing requires current portfolio context and one reviewed assessment per product')
    presence_rows = views.get('portfolio', {}).get('regional_presence')
    presence_assessments = {r['region_id']: r for r in interpreted.values() if PRESENCE.is_assessment(r)}
    if full and presence_rows is not None and positioning_context.get('regional_presence') is None:
        raise ValueError('full briefing requires current reviewed regional presence context')

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

    focus_layout = 'focus_pages' in manifest
    focus_pages = [page for r in manifest.get('focus_pages', []) for page in views.get('focus:' + r['id'], {}).get('focus_pages', [])]
    if any('focus_pages' in v and not role.startswith('focus:') for role, v in views.items()):
        raise ValueError('focus_pages belongs to separate focus-analyst jobs')
    if not focus_layout and focus_pages:
        raise ValueError('focus pages require explicit manifest request')
    if focus_layout:
        FOCUS.validate(manifest['focus_pages'], focus_pages, require, manifest['as_of'])
        if views.get('market', {}).get('market_dashboard') is not None or any(t.get('page') == 'market' for t in manifest.get('topics', [])):
            raise ValueError('new focus layout replaces market_dashboard / page=market')
    topics = manifest.get("topics", [])
    if not isinstance(topics, list):
        raise ValueError("topics must be ordered id/label rows")
    topic_index = CHECK.index(topics, "topics")
    if any(not CHECK.text(t.get("label")) or t.get("page", "main") not in {"main", "market"} for t in topics):
        raise ValueError("topic label required")
    if manifest.get('market_title') is not None and not CHECK.text(manifest['market_title']):
        raise ValueError('market_title must be text')
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
                if field == "topics":
                    for key, limit in (("headline", 72), ("preview", 160)):
                        if key in row and (not CHECK.text(row[key]) or len(row[key]) > limit):
                            raise ValueError("topic " + key + " invalid")
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
            PROFILE.validate(profile, require, manifest["as_of"], claims)
        if view.get('market_dashboard') is not None:
            if role != 'market':
                raise ValueError('market_dashboard belongs to market role')
            MARKET.validate(view['market_dashboard'], require, manifest['as_of'])
        if view.get('regional_presence') is not None:
            if role != 'portfolio':
                raise ValueError('regional_presence belongs to portfolio role')
            PRESENCE.validate(view['regional_presence'], require, manifest['as_of'])

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
        return '<details class="card" data-es-title="' + esc(title or row["statement"]) + '"><summary>' + esc(title or row["statement"]) + '</summary><div class="es-detail"><p>' + esc(row["statement"]) + '</p>' + paragraphs([row['uncertainty']]) + evidence(row) + links([row["id"]]) + '</div></details>'

    def view_card(row):
        body = "".join('<p>' + esc(claims[c]["statement"]) + '</p>' + evidence(claims[c]) for c in row["claim_ids"])
        body += links(row["claim_ids"])
        for section in row.get("sections", []):
            body += '<h4>' + esc(section["label"]) + '</h4>' + "".join('<p>' + esc(claims[c]["statement"]) + '</p>' + evidence(claims[c]) for c in section["claim_ids"]) + links(section["claim_ids"])
        return '<details class="card" data-es-title="' + esc(row["label"]) + '"><summary>' + esc(row["label"]) + '</summary><div class="es-detail">' + body + '</div></details>'

    def module_insights(module):
        requested = positioning_context.get('module_insights') if positioning_context else None
        rows = positioning.get('interpretations', []) if positioning else []

        def detail(row):
            out = '<h5>Herleitung · Analysteninterpretation</h5>' + paragraphs([row['reasoning'], row['method']]) + links([row['id']])
            if row['uncertainty']:
                out += '<h5>Grenzen der Aussage</h5>' + paragraphs([row['uncertainty']])
            fact_ids = list(dict.fromkeys(row['fact_claim_ids'] + sorted({cid for report in validations for cid in report['fact_dependencies'].get(row['id'], [])})))
            out += '<h5>Faktenbasis &amp; Originalquellen</h5>'
            for cid in fact_ids:
                fact = claims[cid]
                out += '<details class="mi-source-fact"><summary>' + esc(cid + ' · ' + ('Faktgrundlage' if cid in row['fact_claim_ids'] else 'Weitere Grundlage der Einordnung')) + '</summary><p>' + esc(fact['statement']) + '</p><p class="meta">' + esc(fact['kind']) + '</p>' + paragraphs([fact['uncertainty']]) + evidence(fact) + links([cid]) + '</details>'
            return out

        return MODULE_INSIGHTS.render(module, rows, requested, detail)

    def short_text(value, limit=160):
        value = " ".join(value.split())
        return value if len(value) <= limit else value[:limit-1].rsplit(" ", 1)[0] + "…"

    def compact_card(title, preview, detail, kind):
        return '<details class="es-entry topic-card" data-es-title="' + esc(title) + '"><summary>' + \
            '<span class="es-kicker">' + esc(kind) + '</span><span class="es-headline">' + esc(title) + \
            '</span><span class="es-preview">' + esc(preview) + \
            '</span><span class="es-arrow" aria-hidden="true">↗</span></summary>' + detail + '</details>'

    def topic_card(row, role, topic):
        labels = {"context": "Geschäftsfeld & Entwicklung", "portfolio": "Systeme & industrielle Basis",
                  "cluster": "Industrie & Partnerschaften", "market": "Markt & Anforderungen"}
        title = row.get("headline") or (labels[role] if row["label"] == topic["label"] else short_text(row["label"], 72))
        preview = row.get("preview") or short_text(claims[row["claim_ids"][0]]["statement"])
        full = view_card(row)
        detail = full[full.index('<div class="es-detail">'):full.rindex('</details>')]
        return compact_card(title, preview, detail, "Faktenbasis")

    def interp_card(row):
        return '<details class="card" data-es-title="' + esc(row["statement"]) + '"><summary>' + esc(row["statement"]) + '</summary>' + executive_detail(row) + '</details>'

    def event_card(row):
        when = row.get("date") or 'Datum öffentlich nicht belegt'
        body = '<div class="es-detail"><p class="meta">Aktuelle Entwicklungen · ' + esc(when) + '</p>'
        groups = [{"claim_ids": row["claim_ids"]}, *row.get("sections", [])]
        for group in groups:
            if group.get("label"):
                body += '<h4>' + esc(group["label"]) + '</h4>'
            for cid in group["claim_ids"]:
                fact = claims[cid]
                body += '<p class="es-statement">' + esc(fact["statement"]) + '</p>'
                body += '<p class="meta">' + esc(fact["kind"]) + '</p>'
                body += paragraphs([fact["uncertainty"]]) + links([cid])
                body += '<h4>Originalquellen &amp; Belegstellen</h4>' + evidence(fact)
        body += '</div>'
        return '<details class="card event-card" data-es-title="' + esc(row["label"]) + '"><summary>' + \
            '<span class="event-title">' + esc(row["label"]) + '</span><span class="event-arrow" aria-hidden="true">↗</span></summary>' + body + '</details>'

    def executive_detail(row):
        body = '<p class="es-statement">' + esc(row["statement"]) + '</p>'
        body += '<h4>Einordnung</h4>' + paragraphs([row["reasoning"]])
        if row["uncertainty"]:
            body += '<h4>Grenzen der Aussage</h4>' + paragraphs([row["uncertainty"]])
        body += links([row["id"]]) + '<h4>Faktenbasis &amp; Originalquellen</h4>'
        fact_ids = sorted({cid for report in validations for cid in report["fact_dependencies"].get(row["id"], [])})
        for cid in fact_ids:
            fact = claims[cid]
            body += '<details class="es-fact"><summary>' + esc(fact["statement"]) + '</summary>'
            body += '<p class="meta">' + esc(fact["kind"]) + '</p>' + paragraphs([fact["uncertainty"]]) + evidence(fact) + links([cid]) + '</details>'
        return '<div class="es-detail">' + body + '</div>'

    def executive_card(row):
        return '<details class="es-card es-entry" data-es-title="' + esc(row["headline"]) + '"><summary>' + \
            '<span class="es-kicker">' + str(row["display_order"]).zfill(2) + ' · Kernaussage</span>' + \
            '<span class="es-headline">' + esc(row["headline"]) + '</span><span class="es-preview">' + \
            esc(row["preview"]) + '</span><span class="es-arrow" aria-hidden="true">↗</span></summary>' + executive_detail(row) + '</details>'

    def highlight_card(row):
        value_class = ' es-status' if row['highlight_kind'] == 'status' else ' es-value-compact' if len(row['value']) > 28 else ' es-value-medium' if len(row['value']) > 18 else ''
        return '<details class="es-highlight es-entry" data-es-title="' + esc(row["label"]) + '"><summary>' + \
            '<span class="es-label">' + esc(row["label"]) + '</span>' + \
            '<span class="es-value' + value_class + '">' + esc(row["value"]) + '</span>' + \
            '<span class="es-scope">' + esc(row["scope_label"]) + '</span>' + \
            '<span class="es-period">' + esc(row["period"]) + '</span>' + \
            '<span class="es-arrow" aria-hidden="true">↗</span></summary>' + executive_detail(row) + '</details>'

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
    executive = '<div class="es-highlights">' + ''.join(highlight_card(r) for r in highlight_rows) + '</div>' if highlight_rows else ''
    if summary_rows:
        executive += '<div class="es-cards" data-count="' + str(len(summary_rows)) + '">' + ''.join(executive_card(r) for r in summary_rows) + '</div>'
    main = section("Executive Summary", executive, 'executive-summary')
    if not summary_rows:
        main += section("Unternehmen im Überblick", grid([view_card(r) for v in views.values() for r in v.get("company_facts", [])]))
    topic_pages = {'main': '', 'market': ''}
    for index, topic in enumerate(topics):
        cards = [topic_card(r, role, topic) for role, v in views.items() for r in v.get("topics", []) if r["id"] == topic["id"]]
        for number, row in enumerate((r for r in interpreted.values() if r["section"] == "topic:" + topic["id"]), 1):
            cards.append(compact_card(row.get("headline") or "Einordnung " + str(number).zfill(2),
                row.get("preview") or short_text(row["statement"]), executive_detail(row), "Analysteneinordnung"))
        topic_pages[topic.get('page', 'main')] += section(topic["label"], '<div class="topic-grid">' + ''.join(cards) + '</div>' if cards else '<p>Keine freigegebenen Befunde für dieses Thema.</p>', 'topic-' + str(index))
    events = [r for v in views.values() for r in v.get("events", [])]
    events.sort(key=lambda r: (r.get("date") is None, r.get("date") or ''))
    timeline = ''
    for row in events:
        dated = ' datetime="' + esc(row["date"]) + '"' if row.get("date") else ''
        timeline += '<div class="event"><time' + dated + '>' + esc(row.get("date") or 'Datum öffentlich nicht belegt') + '</time>' + event_card(row) + '</div>'
    main += section("Aktuelle Entwicklungen", '<div class="timeline">' + timeline + '</div>' if timeline else '', 'current-developments')
    portfolio_html = PORTFOLIO.render(inventory, product_assessments, claims, evidence, links, CHECK.PORTFOLIO_STAGES)
    portfolio_cards = module_insights('portfolio')
    if portfolio_html or portfolio_cards:
        main += '<section class="module" id="portfolio">' + (portfolio_html or '<h2>Portfolio</h2>') + portfolio_cards + '</section>'
    main += topic_pages['main']
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
        fragment = fragment.replace('__CLUSTER_ACTOR_TABLES__', CLUSTER.actor_tables(network), 1)
        if 'tableBody.replaceChildren();' not in fragment:
            fragment = fragment.replace("const tableBody=root.querySelector('tbody');", "const tableBody=root.querySelector('tbody');tableBody.replaceChildren();", 1)
        fragment = fragment.replace("window.addEventListener('beforeprint',()=>{root.querySelector('.cn-table').open=true;});", "", 1)
        main += section("Cluster · Technologie, Industrie & Marktzugang", fragment + module_insights('cluster'), 'cluster-analysis')
    if presence_rows is not None:
        def presence_detail(region, row):
            out = '<h4>Wie vertreten?</h4>'
            for activity in region['activities']:
                state = 'angekündigt' if activity['status'] == 'announced' else 'operativ dokumentiert'
                out += '<div class="rp-activity"><strong>' + esc(activity['actor']) + '</strong><p>' + esc(activity['description']) + '</p><p class="meta">' + esc(PRESENCE.operator_label(activity) + ' · ' + activity['country'] + ' · ' + activity['location'] + ' · ' + activity['product_scope'] + ' · ' + state + ' · ' + (activity.get('status_date') or 'Statusdatum nicht belegt')) + '</p>' + paragraphs([activity.get('ownership_note'), activity.get('control_note')]) + links(activity['claim_ids']) + '</div>'
            if not region['activities']:
                out += '<p class="rp-empty">Keine freigegebenen konkreten Präsenzaktivitäten im Paket.</p>'
            if row:
                title = 'Warum Stufe ' + str(row['score']) + '?' if row['score'] is not None else 'Warum derzeit nur geplant?' if row.get('assessment_status') == 'geplant' else 'Warum nicht eindeutig bestimmbar?'
                out += '<h4>' + esc(title) + '</h4>' + paragraphs([row['statement'], row['reasoning'], row['method'], row.get('next_stage_limit'), row.get('coverage_note')]) + links([row['id']])
            else:
                out += '<p class="rp-empty">Faktenansicht: keine freigegebene Präsenzbewertung.</p>'
            out += '<h4>Reichweite des Nachweises</h4>' + paragraphs([region['geographic_scope'], region['product_scope'], region['coverage_note'], row.get('uncertainty') if row else None])
            out += '<h4>Originalquellen &amp; Belegstellen</h4>'
            for cid in region['claim_ids']:
                fact = claims[cid]
                out += '<details class="rp-source-fact"><summary>' + esc(cid + ' · ' + fact['kind']) + '</summary><p>' + esc(fact['statement']) + '</p>' + paragraphs([fact['uncertainty']]) + evidence(fact) + links([cid]) + '</details>'
            return out
        presence_body = PRESENCE.render(presence_rows, presence_assessments, presence_detail, manifest['as_of'])
        covered = {cid for region in presence_rows for cid in region['claim_ids']}
        supplementary = [r for r in views.get('portfolio', {}).get('regions', []) if not {cid for ids in [r['claim_ids']] + [s['claim_ids'] for s in r.get('sections', [])] for cid in ids} <= covered]
        if supplementary:
            presence_body += '<h3>Weitere belegte regionale Aktivitäten</h3>' + grid([view_card(r) for r in supplementary])
        main += section('Regionale Präsenz auf einen Blick.', presence_body, 'regional-presence')
    market_cards = module_insights('market')
    if positioning_context and positioning_context.get("matrix"):
        criteria = plan["criteria"]
        cells = {(r["peer_id"], r["criterion_id"]): r for r in positioning["interpretations"] if r.get("type") == "matrix_cell"}

        def matrix_detail(row):
            body = '<div class="cm-detail-grid"><div class="cm-discussion"><p class="cm-statement">' + esc(row['statement']) + '</p><h4>Einordnung</h4>' + paragraphs([row['reasoning']]) + links([row['id']]) + '</div>'
            limits = [(label, row.get(key)) for key, label in (
                ('uncertainty', 'Grenzen der Aussage'), ('next_stage_limit', 'Nächste Evidenzstufe'),
                ('coverage_note', 'Recherche- und Beleggrenze')) if row.get(key)]
            if limits:
                body += '<aside class="cm-limits">' + ''.join('<h4>' + label + '</h4>' + paragraphs([value]) for label, value in limits) + '</aside>'
            body += '</div><div class="cm-facts"><h4>Faktenbasis &amp; Originalquellen</h4>'
            fact_ids = sorted({cid for report in validations for cid in report['fact_dependencies'].get(row['id'], [])})
            for cid in fact_ids:
                fact = claims[cid]
                body += '<details class="cm-fact"><summary>' + esc(fact['statement']) + '</summary><p class="meta">' + esc(fact['kind']) + '</p>' + paragraphs([fact['uncertainty']]) + evidence(fact) + links([cid]) + '</details>'
            return body + '</div>'

        counts = {r['id']: len({sources[s]['url'] for report in validations
            for cid in report['fact_dependencies'].get(r['id'], []) for s in claims[cid]['source_ids']}) for r in cells.values()}
        matrix = CAPABILITY.render(criteria, positioning_context['matrix']['peers'], cells,
            manifest['company'], matrix_detail, counts, network['target_id'] if network else None)
        title = 'Capability Matrix · fiktiver Beispieldatensatz' if fictional else 'Capability Matrix · öffentlich belegte Reife'
        main += section(title, matrix + market_cards, 'capability-matrix')
    elif market_cards:
        main += section('Markt & Wettbewerb', market_cards, 'market-overview')
    extra = [r for r in interpreted.values() if r['id'].startswith('I') and r['section'] not in {CHECK.SUMMARY_SECTION, CHECK.HIGHLIGHT_SECTION, MODULE_INSIGHTS.SECTION, 'regions'} and not r['section'].startswith('topic:') and r.get('type') != 'matrix_cell' and not CHECK.product_assessment(r) and not PRESENCE.is_assessment(r)]
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
            quadrants.append('<div class="quadrant" data-swot="' + key + '"><h3>' + title + '</h3>' + (''.join(cards) or '<p class="meta">Keine freigegebene Aussage in dieser Kategorie.</p>') + '</div>')
        main += section('SWOT · Analysteninterpretation', '<div class="swot">' + ''.join(quadrants) + '</div>')
    limits = ''.join('<details><summary>' + esc(v['role']) + ' · Rechercheabdeckung und offene Punkte</summary>' + note_rows(v.get('gaps', [])) + note_rows(v.get('coverage', [])) + note_rows(v.get('report_log', [])) + '</details>' for v in views.values())
    limits += ''.join(paragraphs(c.get('shared_limitations', [])) + paragraphs([c.get('document_scope')]) for c in contexts)
    for o in (positioning, swot):
        if o:
            limits += paragraphs(o.get('shared_limitations', [])) + note_rows(o.get('research_requests', []))
    main += '<section class="module"><details class="data-gaps"><summary style="cursor:pointer"><h2 style="display:inline;margin:0">Datenlücken &amp; offene Fragen</h2></summary><div style="margin-top:18px">' + limits + '</div></details></section>'
    profile_body = '<p>Kein Gesprächspartner im Auftrag angegeben.</p>'
    person_sources = ''
    person_media = ''
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
            body = PROFILE.render(profile, claims, sources, manifest['company'], manifest['as_of'])
            person_sources = section('Gesprächspartner · Quellen & Evidenz', PROFILE.render_sources(profile, claims, sources), 'person-profile-sources')
            person_media = PROFILE.render_media(profile, claims, manifest['as_of'], sources)
        else:
            body += '<p>Berufliches Profil öffentlich nicht verifiziert.</p>'
        profile_body = body
    def market_facts(ids):
        return ''.join('<details class="mk-fact"><summary>Beleg · ' + esc(cid) + '</summary><p>' + esc(claims[cid]['statement']) + '</p><p class="meta">' + esc(claims[cid]['kind']) + '</p>' + paragraphs([claims[cid]['uncertainty']]) + evidence(claims[cid]) + links([cid]) + '</details>' for cid in dict.fromkeys(ids))

    dashboard = views.get('market', {}).get('market_dashboard')
    regions = [section(dashboard['title'], MARKET.render(dashboard, market_facts))] if dashboard else []
    regions.append(topic_pages['market'])
    for role, v in views.items():
        if v.get('regions'):
            if role == 'portfolio' and presence_rows is not None:
                continue
            regions.append(section('Unternehmenspräsenz' if role == 'portfolio' else 'Markt & Industrie', grid([view_card(r) for r in v['regions']])))
    region_interpretations = [interp_card(r) for r in interpreted.values() if r.get('section') == 'regions']
    if region_interpretations:
        regions.append(section('Einordnung · Marktzugang', grid(region_interpretations)))
    if focus_layout:
        # General company/market regional facts stay in the company overview.
        regional = []
        for role, view in views.items():
            if view.get('regions') and not (role == 'portfolio' and presence_rows is not None):
                regional.append(section('Unternehmenspräsenz' if role == 'portfolio' else 'Markt & Industrie', grid([view_card(r) for r in view['regions']])))
        if region_interpretations:
            regional.append(section('Einordnung · Marktzugang', grid(region_interpretations)))
        main += ''.join(regional)
        pages = [('page-main', 'Überblick', main)]
        if manifest.get('person'):
            pages.append(('page-profile', 'Gesprächspartner', section('Gesprächspartner', profile_body) + person_media))
        def focus_details(ids):
            return '<div class="focus-evidence">' + ''.join('<p>' + esc(claims[c]['statement']) + '</p>' + paragraphs([claims[c].get('uncertainty')]) for c in dict.fromkeys(ids)) + links(ids) + '</div>'
        for page in focus_pages:
            pages.append(('page-focus-' + page['id'], page['label'], FOCUS.render(page, focus_details, manifest['as_of'])))
    else:
        # Explicit compatibility for reviewed historical runs only.
        market_label = 'Markt-Deep-Dive' + (' · ' + manifest['market_title'] if manifest.get('market_title') else '')
        pages = [('page-main', 'Überblick', main), ('page-profile', 'Gesprächspartner', section('Gesprächspartner', profile_body) + person_media),
                 ('page-regions', market_label, ''.join(regions) or section(market_label, '<p>Keine freigegebenen regionalen Befunde für diesen Auftrag.</p>'))]
    register = '<label class="source-search">Quellen und Aussagen durchsuchen<input id="source-search-input" type="search" placeholder="Stichwort, Claim oder Quelle"></label>'
    for cid, row in claims.items():
        status = reviews.get(cid, {}).get('status', 'nicht einzeln geprüft')
        depth = reviews.get(cid, {}).get('depth', 'nicht geprüft')
        if CHECK.ready(cid, reviews, hashes) and status in CHECK.ACCEPTED:
            status = 'Prüfbefund veraltet'
        register += '<details class="claim-detail" id="' + esc(cid) + '"><summary>' + esc(cid + ' · ' + row['statement']) + '</summary><p class="meta">' + esc(row['kind'] + ' · Prüftiefe ' + depth + ' · ' + status) + '</p>' + paragraphs([row['uncertainty']]) + evidence(row) + '</details>'
    for cid, row in interpreted.items():
        register += '<details class="claim-detail" id="' + esc(cid) + '"><summary>' + esc(cid + ' · ' + row['statement']) + '</summary><p class="meta">Analysteninterpretation · vollständig geprüft im Schluss-Review</p>' + paragraphs([row['reasoning'], row['method'], row['uncertainty'], row.get('next_stage_limit'), row.get('coverage_note')]) + links(row['depends_on']) + '</details>'
    register += '<h3>Dokumente</h3>' + ''.join('<p>' + source_html(s) + '</p>' for s in sources.values())
    pages.append(('page-sources', 'Quellen', section('Aussagen, Belegstellen & Originalquellen', register) + person_sources))
    tabs = ''.join('<button type="button" role="tab" id="tab-' + ident + '" data-page="' + ident + '" aria-controls="' + ident + '">' + str(i) + ' · ' + esc(label) + '</button>' for i, (ident, label, _) in enumerate(pages, 1))
    content = ''.join('<div class="page" role="tabpanel" aria-labelledby="tab-' + ident + '" id="' + ident + '"><p class="page-kicker">' + str(i).zfill(2) + ' / ' + str(len(pages)).zfill(2) + ' · ' + esc(label) + '</p>' + body + '</div>' for i, (ident, label, body) in enumerate(pages, 1))
    if focus_pages:
        content = FOCUS.css() + content
    if positioning_context and positioning_context.get('module_insights'):
        content = MODULE_INSIGHTS.css() + content
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
