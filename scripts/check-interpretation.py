#!/usr/bin/env python3
"""Prepare selective reviewed contexts and validate interpretation references/snapshots."""
import argparse
import copy
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ACCEPTED = {"geprüft", "übernommen"}
CELL_STATUS = {"bewertet", "nicht öffentlich belegt", "nicht anwendbar",
               "weitere Faktenprüfung nötig"}
ROLES = {"context", "portfolio", "cluster", "market", "source-reviewer"}
SUMMARY_SECTION = "executive_summary"
HIGHLIGHT_SECTION = "executive_highlights"
PORTFOLIO_METHOD = "portfolio-maturity-v1"
PORTFOLIO_STAGES = {str(i): label for i, label in enumerate(
    ("Angekündigt", "Prototyp", "Test / Demo", "Kundenprogramm", "Im Betrieb", "Serie / Skala"), 1)}

def portfolio_context(facts):
    """Compact reviewed inventory; maturity remains exclusively interpretation data."""
    products = []
    for view in facts.get("module_views", []):
        if view.get("role") != "portfolio":
            continue
        for row in view.get("products", []):
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", str(row.get("id", ""))):
                raise ValueError("portfolio product needs a safe, stable id")
            if not text(row.get("label")) or not isinstance(row.get("claim_ids"), list) or not row["claim_ids"]:
                raise ValueError("portfolio product needs label and claim_ids")
            domain = row.get("domain", "Produkte / Lösungen")
            short = row.get("short_label", row["label"])
            if not text(domain) or not text(short):
                raise ValueError("portfolio domain/short_label must be text")
            products.append({"id": row["id"], "label": row["label"], "short_label": short,
                             "domain": domain, "claim_ids": row["claim_ids"]})
            if row.get('sections'):
                products[-1]['sections'] = copy.deepcopy(row['sections'])
    index(products, "portfolio products")
    return {"method_id": PORTFOLIO_METHOD, "stages": PORTFOLIO_STAGES, "products": products}

def product_assessment(row):
    return row.get("type") == "product_maturity" and "product_id" in row

def unassessed(row):
    return (row.get("type") == "matrix_cell" and row.get("cell_status") != "bewertet") or (
        product_assessment(row) and row.get("assessment_status") != "bewertet")

def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":"), allow_nan=False).encode()).hexdigest()

def text(value):
    return isinstance(value, str) and bool(value.strip())

def read(path):
    raw = Path(path).read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        blocks = re.findall(r"```json\s*\n(.*?)\n```", raw, re.S)
        if len(blocks) != 1:
            raise ValueError("review must contain exactly one JSON block")
        return json.loads(blocks[0])

def index(rows, label):
    if not isinstance(rows, list):
        raise ValueError(label + " must be a list")
    result = {}
    for row in rows:
        if not isinstance(row, dict) or not text(row.get("id")) or row["id"] in result:
            raise ValueError(label + ": invalid/duplicate id")
        result[row["id"]] = row
    return result

def helper(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

MODULE_INSIGHTS = helper('module_insights', 'module-insights-html.py')

def env(manifest, facts, review):
    if manifest.get("schema_version") != 1 or manifest.get("mode") != "facts-v2":
        raise ValueError("manifest must be facts-v2 schema_version=1")
    for obj, label in ((facts, "facts"), (review, "review")):
        if not isinstance(obj, dict):
            raise ValueError(label + " must be an object")
        for key in ("run_id", "company", "as_of"):
            if obj.get(key) != manifest.get(key) or not text(manifest.get(key)):
                raise ValueError(label + " mismatch: " + key)
    if facts.get("schema_version") != 1 or facts.get("mode") != "facts-v2" or review.get("schema_version") != 1:
        raise ValueError("facts/review schema mismatch")
    if review.get("phase") != "basis" or review.get("status") != "freigegeben" or review.get("material_errors") != []:
        raise ValueError("basis review is not released or has material errors")
    result = helper("review", "check-review-data.py").validate(facts)
    if result["errors"]:
        raise ValueError("invalid facts: " + "; ".join(result["errors"]))
    for row in facts["claims"]:
        if row.get("kind") not in {"Fakt", "Herstellerangabe", "Partnerangabe"} or not re.fullmatch(r"[PCMTH][A-Za-z0-9_-]+", row["id"]):
            raise ValueError("interpretations require factual claims, not user input/ratings")
    return index(facts["claims"], "facts"), index(review.get("claims"), "review"), result["fingerprints"]

def ready(cid, reviews, fingerprints):
    row = reviews.get(cid, {})
    if row.get("depth") != "A" or row.get("status") not in ACCEPTED:
        return "Vollprüfung A erforderlich"
    if row.get("fingerprint") != fingerprints.get(cid):
        return "Prüfbefund veraltet"
    return None

def context_valid(context, manifest):
    if not isinstance(context, dict):
        raise ValueError("context must be an object")
    for key in ("run_id", "company", "as_of"):
        if context.get(key) != manifest.get(key):
            raise ValueError("context mismatch: " + key)
    body = {k: v for k, v in context.items() if k != "fingerprint"}
    if context.get("fingerprint") != digest(body):
        raise ValueError("context fingerprint mismatch")
    check = helper("context_review", "check-review-data.py").validate(
        {"company": context["company"], "as_of": context["as_of"],
         "claims": context.get("facts"), "sources": context.get("sources")})
    if check["errors"] or check["fingerprints"] != context.get("fact_fingerprints"):
        raise ValueError("context fact/source snapshot is inconsistent")

def plan_check(plan, manifest):
    errors = helper("prepare", "prepare-facts.py").validate_plan(plan, manifest)
    methods = plan.get("assessment_methods", [])
    if not isinstance(methods, list):
        errors.append("assessment_methods must be a list")
    else:
        seen = set()
        for row in methods:
            if not isinstance(row, dict) or not text(row.get("id")) or row["id"] in seen:
                errors.append("assessment method id invalid/duplicate")
                continue
            seen.add(row["id"])
            if not text(row.get("assessment_type")) or not text(row.get("applicability")):
                errors.append("assessment method needs type/applicability")
            if not isinstance(row.get("anchors"), dict) or not row["anchors"] or any(not text(v) for v in row["anchors"].values()):
                errors.append("assessment method needs anchors")
    if errors:
        raise ValueError("; ".join(errors))

def prepare(manifest, facts, review, claim_ids, plan=None, market=None,
            positioning=None, positioning_context=None, interpretation_ids=None,
            include_portfolio=False, include_module_insights=False):
    claims, reviews, fingerprints = env(manifest, facts, review)
    selected = set(claim_ids or [])
    inventory = portfolio_context(facts) if include_portfolio else None
    if include_portfolio and positioning is not None:
        raise ValueError("portfolio inventory belongs to positioning, not SWOT context")
    if include_module_insights and positioning is not None:
        raise ValueError('module insights belong to positioning, not SWOT context')
    if inventory:
        selected.update(c for p in inventory["products"] for c in p["claim_ids"])
    selected_interpretations = {}
    interpretation_fingerprints = {}
    upstream_plan_fingerprints = {}
    if positioning is not None:
        if positioning_context is None:
            raise ValueError("positioning context required")
        check = validate_output(manifest, facts, review, positioning_context, positioning,
                                latest_plan=plan)
        if check["errors"]:
            raise ValueError("invalid positioning: " + "; ".join(check["errors"]))
        known = index(positioning["interpretations"], "positioning")
        needed = list(interpretation_ids or [])
        while needed:
            cid = needed.pop()
            if cid not in known:
                raise ValueError("unknown positioning id: " + cid)
            if cid in selected_interpretations:
                continue
            row = known[cid]
            if unassessed(row):
                raise ValueError("unrated matrix cell or product is not a SWOT basis")
            selected_interpretations[cid] = row
            interpretation_fingerprints[cid] = check["fingerprints"][cid]
            upstream_plan_fingerprints[cid] = positioning_context.get("plan_fingerprint")
            selected.update(check["fact_dependencies"][cid])
            needed.extend(d for d in row["depends_on"] if d in known)
    matrix = None
    if plan is not None and (market is not None or positioning is None):
        plan_check(plan, manifest)
        if market is not None:
            for key in ("run_id", "company", "as_of"):
                if market.get(key) != manifest.get(key):
                    raise ValueError("market mismatch: " + key)
            if market.get("comparison_plan_version") != plan.get("version"):
                raise ValueError("market plan version mismatch")
            peers = index(market.get("peers"), "peers")
            criteria = index(plan["criteria"], "criteria")
            observations = market.get("observations", [])
            for row in observations:
                if row.get("peer_id") not in peers or row.get("criterion_id") not in criteria:
                    raise ValueError("observation references unknown peer/criterion")
                selected.update(row.get("claim_ids", []))
            matrix = {"peers": list(peers.values()), "observations": observations,
                      "gaps": market.get("gaps", []), "coverage": market.get("coverage", [])}
    todo = list(selected)
    while todo:
        cid = todo.pop()
        if cid not in claims:
            raise ValueError("unknown fact id: " + str(cid))
        for parent in claims[cid].get("depends_on", []):
            if parent not in selected:
                selected.add(parent)
                todo.append(parent)
    if not selected and matrix is None:
        raise ValueError("select relevant fact or interpretation ids")
    selected_sources = {sid for cid in selected for sid in claims[cid]["source_ids"]}
    body = {"schema_version": 1, "run_id": manifest["run_id"], "company": manifest["company"],
            "as_of": manifest["as_of"], "scope": manifest.get("scope", ""),
            "facts": [claims[c] for c in sorted(selected)],
            "sources": [s for s in facts["sources"] if s["id"] in selected_sources],
            "fact_fingerprints": {c: fingerprints[c] for c in sorted(selected)},
            "pending_checks": {c: reason for c in sorted(selected)
                               if (reason := ready(c, reviews, fingerprints)) is not None},
            "interpretations": list(selected_interpretations.values()),
            "interpretation_fingerprints": interpretation_fingerprints,
            "upstream_plan_fingerprints": upstream_plan_fingerprints,
            "module_context": facts.get("module_context", [])}
    if plan is not None and (market is not None or positioning is None):
        body["plan"] = plan
        body["plan_fingerprint"] = digest(plan)
    if matrix is not None:
        body["matrix"] = matrix
    if inventory is not None:
        body["portfolio"] = inventory
    if include_module_insights:
        body['module_insights'] = MODULE_INSIGHTS.request(manifest)
    return copy.deepcopy({**body, "fingerprint": digest(body)})

def validate_output(manifest, facts, review, context, output,
                    latest_positioning=None, latest_positioning_context=None,
                    latest_plan=None):
    errors, output_fingerprints, fact_dependencies = [], {}, {}
    claims, reviews, current_fingerprints = env(manifest, facts, review)
    context_valid(context, manifest)
    if not isinstance(output, dict):
        raise ValueError("output must be an object")
    for key in ("run_id", "company", "as_of"):
        if output.get(key) != manifest.get(key):
            errors.append("output mismatch: " + key)
    if output.get("schema_version") != 1 or output.get("mode") != "interpret-v2":
        errors.append("output must use schema_version=1, mode=interpret-v2")
    if output.get("role") not in {"positioning", "swot"}:
        errors.append("invalid interpretation role")
    if output.get("input_fingerprint") != context.get("fingerprint"):
        errors.append("output uses different input snapshot")
    if output.get("status") not in {"vollständig", "teilweise", "blockiert"} or not text(output.get("scope")):
        errors.append("missing scope/status")
    for field in ("total_score", "rankings", "weighted_score", "claims", "source_proposals"):
        if field in output:
            errors.append("prohibited output field: " + field)
    rows = index(output.get("interpretations"), "interpretations")
    delegated_insights = context.get('module_insights')
    if output.get('role') != 'positioning' and (delegated_insights is not None or output.get('module_insight_gaps') or any(r.get('type') == 'module_insight' or r.get('section') == MODULE_INSIGHTS.SECTION for r in rows.values())):
        errors.append('module insights belong to positioning')
    errors.extend(MODULE_INSIGHTS.validate(list(rows.values()), output.get('module_insight_gaps', []), delegated_insights, manifest, claims))
    upstream = index(context.get("interpretations", []), "context interpretations")
    if upstream:
        if latest_positioning is None or latest_positioning_context is None:
            raise ValueError("current positioning and its context required")
        latest = validate_output(manifest, facts, review, latest_positioning_context,
                                 latest_positioning, latest_plan=latest_plan)
        if latest["errors"]:
            raise ValueError("current positioning invalid: " + "; ".join(latest["errors"]))
        for cid in upstream:
            if latest["fingerprints"].get(cid) != context.get("interpretation_fingerprints", {}).get(cid):
                errors.append("upstream positioning changed: " + cid)
    prefix = "I" if output.get("role") == "positioning" else "S"
    methods, criteria, peers = {}, {}, {}
    plan = context.get("plan")
    if plan is not None:
        plan_check(plan, manifest)
        if latest_plan is None:
            raise ValueError("current comparison plan required")
        plan_check(latest_plan, manifest)
        if digest(latest_plan) != digest(plan):
            errors.append("comparison plan changed")
        criteria = index(plan["criteria"], "criteria")
        methods = index(plan.get("assessment_methods", []), "assessment methods")
        if context.get("plan_fingerprint") != digest(plan) or output.get("plan_fingerprint") != digest(plan):
            errors.append("plan fingerprint mismatch")
    matrix = context.get("matrix")
    inventory = context.get("portfolio")
    product_ids = set()
    if inventory is not None:
        if inventory != portfolio_context(facts):
            errors.append("portfolio inventory changed")
        product_ids = {p["id"] for p in inventory.get("products", [])}
    assessed_products = set()
    if matrix is not None:
        peers = index(matrix["peers"], "peers")
    pairs, visiting = set(), set()

    def checked_facts(cid, trail=None):
        trail = set() if trail is None else trail
        if cid in trail:
            errors.append("cyclic fact dependency: " + cid)
            return set()
        if cid not in context.get("fact_fingerprints", {}):
            errors.append("fact not in delegated context: " + cid)
        elif context["fact_fingerprints"][cid] != current_fingerprints[cid]:
            errors.append("changed fact: " + cid)
        reason = ready(cid, reviews, current_fingerprints)
        if reason:
            errors.append(cid + ": " + reason)
        found = {cid}
        for parent in claims[cid].get("depends_on", []):
            found.update(checked_facts(parent, trail | {cid}))
        return found

    def dependencies(cid):
        if cid in fact_dependencies:
            return fact_dependencies[cid]
        if cid in visiting:
            errors.append("cyclic interpretation dependency: " + cid)
            return set()
        visiting.add(cid)
        row = rows.get(cid) or upstream.get(cid)
        if row is None:
            errors.append("unknown interpretation: " + cid)
            visiting.discard(cid)
            return set()
        deps = row.get("depends_on")
        if not isinstance(deps, list) or any(not isinstance(d, str) for d in deps):
            errors.append(cid + ": depends_on must be a list of ids")
            deps = []
        found = set()
        parent_hashes = {}
        for dep in deps:
            if dep in claims:
                basis = checked_facts(dep)
                found.update(basis)
                parent_hashes.update({f: current_fingerprints[f] for f in basis})
            elif dep in rows or dep in upstream:
                parent = rows.get(dep) or upstream[dep]
                if unassessed(parent):
                    errors.append(cid + ": unassessed matrix cell or product cannot support a conclusion")
                if dep in rows and output.get("role") == "swot":
                    errors.append(cid + ": SWOT claims cannot support other SWOT claims")
                found.update(dependencies(dep))
                parent_hashes[dep] = output_fingerprints.get(dep)
                if dep in upstream and context.get("interpretation_fingerprints", {}).get(dep) != output_fingerprints.get(dep):
                    errors.append(cid + ": changed upstream interpretation: " + dep)
            else:
                errors.append(cid + ": unknown dependency: " + dep)
        fact_dependencies[cid] = found
        output_fingerprints[cid] = digest({"claim": row, "dependencies": parent_hashes,
                                          "plan": context.get("upstream_plan_fingerprints", {}).get(cid)
                                          if cid in upstream else context.get("plan_fingerprint")})
        visiting.discard(cid)
        return found

    categories = {"Strengths": 0, "Weaknesses": 0, "Opportunities": 0, "Threats": 0}
    summary_groups = {SUMMARY_SECTION: [], HIGHLIGHT_SECTION: []}
    for cid, row in rows.items():
        if not re.fullmatch(prefix + r"[A-Za-z0-9_-]+", cid):
            errors.append(cid + ": invalid claim prefix")
        for field in ("statement", "section", "reasoning", "method"):
            if not text(row.get(field)):
                errors.append(cid + ": missing " + field)
        if not isinstance(row.get("uncertainty"), str):
            errors.append(cid + ": uncertainty must be a string")
        section = row.get("section") if text(row.get("section")) else None
        if section in summary_groups:
            summary_groups[section].append(row)
            if output.get("role") != "positioning":
                errors.append(cid + ": executive content belongs to positioning")
            order = row.get("display_order")
            if not isinstance(order, int) or isinstance(order, bool) or order < 1:
                errors.append(cid + ": display_order must be a positive integer")
            limits = {"headline": 72, "preview": 160} if section == SUMMARY_SECTION else {
                "label": 60, "value": 40, "scope_label": 80, "period": 60}
            for field, limit in limits.items():
                if not text(row.get(field)) or len(row[field]) > limit:
                    errors.append(cid + ": " + field + " required, at most " + str(limit) + " characters")
            if section == HIGHLIGHT_SECTION:
                if row.get("type") != "summary_highlight" or row.get("highlight_kind") not in {"metric", "status"}:
                    errors.append(cid + ": highlight needs summary_highlight type and metric/status kind")
                if row.get("highlight_kind") == "metric" and (not text(row.get("value")) or not re.search(r"\d", row["value"])):
                    errors.append(cid + ": metric highlight needs a numeric display value including its unit")
                deps = row.get("depends_on")
                if not isinstance(deps, list) or not deps or any(not isinstance(d, str) or d not in claims for d in deps):
                    errors.append(cid + ": highlight must reference checked facts directly")
            elif row.get("type") in {"summary_highlight", "matrix_cell"}:
                errors.append(cid + ": main statement cannot be a highlight or matrix cell")
        elif row.get("type") == "summary_highlight":
            errors.append(cid + ": summary_highlight requires executive_highlights section")
        if section and section.startswith("topic:"):
            for field, limit in (("headline", 72), ("preview", 160)):
                if field in row and (not text(row[field]) or len(row[field]) > limit):
                    errors.append(cid + ": compact " + field + " invalid")
        found = dependencies(cid)
        is_cell = row.get("type") == "matrix_cell"
        if is_cell:
            for field, limit in (("headline", 48), ("preview", 80)):
                if field in row and (not text(row[field]) or len(row[field]) > limit):
                    errors.append(cid + ": matrix " + field + " invalid")
            if output.get("role") != "positioning" or row.get("peer_id") not in peers or row.get("criterion_id") not in criteria:
                errors.append(cid + ": invalid matrix peer/criterion")
                continue
            pair = (row["peer_id"], row["criterion_id"])
            if pair in pairs:
                errors.append(cid + ": duplicate matrix cell")
            pairs.add(pair)
            state = row.get("cell_status")
            if state not in CELL_STATUS:
                errors.append(cid + ": invalid cell_status")
            criterion = criteria[row["criterion_id"]]
            value = row.get("value")
            if state == "bewertet":
                if not found:
                    errors.append(cid + ": assessment has no checked fact basis")
                kind = criterion["display_type"]
                if kind == "Profil" and not text(value):
                    errors.append(cid + ": profile must be descriptive text")
                if kind == "Kennzahl" and (not isinstance(value, (int, float)) or isinstance(value, bool)):
                    errors.append(cid + ": metric must be numeric")
                if kind == "Evidenzstufe":
                    key = str(int(value)) if isinstance(value, float) and value.is_integer() else str(value)
                    if isinstance(value, bool) or key not in criterion["anchors"]:
                        errors.append(cid + ": score outside predefined anchors")
                    if not text(row.get("next_stage_limit")):
                        errors.append(cid + ": explain next-stage evidence limit")
            else:
                if value is not None:
                    errors.append(cid + ": unrated cell must use null value")
                if not text(row.get("coverage_note")):
                    errors.append(cid + ": unrated cell needs coverage_note")
                if state == "nicht anwendbar" and not found:
                    errors.append(cid + ": inapplicability needs checked fact basis")
        elif product_assessment(row):
            pid = row.get("product_id")
            if output.get("role") != "positioning" or inventory is None or pid not in product_ids:
                errors.append(cid + ": product assessment needs delegated portfolio product")
            if pid in assessed_products:
                errors.append(cid + ": duplicate product assessment")
            assessed_products.add(pid)
            if row.get("method_id") != PORTFOLIO_METHOD or row.get("section") != "portfolio":
                errors.append(cid + ": product assessment needs canonical portfolio method/section")
            if any(d not in claims for d in row.get("depends_on", [])):
                errors.append(cid + ": product maturity must reference checked facts directly")
            score, state = row.get("score"), row.get("assessment_status")
            if state == "bewertet":
                if not isinstance(score, int) or isinstance(score, bool) or str(score) not in PORTFOLIO_STAGES:
                    errors.append(cid + ": product maturity must be an integer from 1 to 6")
                if not found or not text(row.get("next_stage_limit")):
                    errors.append(cid + ": rated product needs fact basis and next-stage limit")
                product = next((p for p in inventory.get('products', []) if p['id'] == pid), None) if inventory else None
                if product and not set(row.get('depends_on', [])) & set(product['claim_ids']):
                    errors.append(cid + ": rated product must reference its own product facts")
            elif state == "nicht eindeutig bestimmbar":
                if score is not None or not text(row.get("coverage_note")):
                    errors.append(cid + ": unassessed product needs null score and coverage_note")
            else:
                errors.append(cid + ": invalid product assessment_status")
        elif not found:
            errors.append(cid + ": interpretation has no checked fact basis")
        if "score" in row and not product_assessment(row):
            method = methods.get(row.get("method_id"))
            key = str(row["score"])
            if method is None or key not in method["anchors"] or row.get("type") != method["assessment_type"] or not text(row.get("subject")):
                errors.append(cid + ": additional score needs matching method/subject")
        if output.get("role") == "swot":
            if row.get("category") not in categories:
                errors.append(cid + ": invalid SWOT category")
            else:
                categories[row["category"]] += 1
    for section, group in summary_groups.items():
        orders = [r.get("display_order") for r in group]
        if any(not isinstance(n, int) or isinstance(n, bool) for n in orders) or set(orders) != set(range(1, len(group) + 1)):
            errors.append(section + ": display_order must be unique and contiguous from 1")
        if len(group) > (6 if section == SUMMARY_SECTION else 3):
            errors.append(section + ": too many entries")
    highlights = summary_groups[HIGHLIGHT_SECTION]
    labels = [tuple(str(r.get(k)) for k in ("label", "scope_label", "period")) for r in highlights]
    if len(set(labels)) != len(labels):
        errors.append("executive_highlights: duplicate metric/status label, scope and period")
    if matrix is not None and output.get("role") == "positioning":
        expected = {(p, c) for p in peers for c in criteria}
        if pairs != expected:
            errors.append("matrix must cover each peer/criterion exactly once")
    if inventory is not None and output.get("role") == "positioning" and assessed_products != product_ids:
        errors.append("portfolio must cover each product exactly once")
    if any(n > 3 for n in categories.values()):
        errors.append("SWOT permits at most three points per quadrant")
    requests = output.get("research_requests")
    if not isinstance(requests, list):
        errors.append("research_requests must be a list")
    else:
        for row in requests:
            if not isinstance(row, dict) or not text(row.get("id")) or row.get("target_role") not in ROLES or not text(row.get("question")) or not isinstance(row.get("blocking"), bool) or not isinstance(row.get("related_claim_ids"), list):
                errors.append("invalid research request")
            elif row["blocking"] and output.get("status") == "vollständig":
                errors.append("blocking research request conflicts with complete status")
    if not isinstance(output.get("shared_limitations"), list):
        errors.append("shared_limitations must be a list")
    return {"run_id": manifest["run_id"], "company": manifest["company"],
            "as_of": manifest["as_of"], "phase": "final",
            "required_full_review_ids": sorted(output_fingerprints),
            "errors": errors, "fingerprints": output_fingerprints,
            "fact_dependencies": {k: sorted(v) for k, v in fact_dependencies.items()},
            "notice": "Mechanical references/snapshots only; interpretation correctness requires final source review."}

def merge_reports(reports):
    if not reports:
        raise ValueError("validation reports required")
    result = {k: reports[0].get(k) for k in ("run_id", "company", "as_of", "phase")}
    result.update(errors=[], fingerprints={}, fact_dependencies={}, required_full_review_ids=[])
    for report in reports:
        if report.get("errors") != [] or report.get("phase") != "final" or any(report.get(k) != result[k] for k in ("run_id", "company", "as_of", "phase")):
            raise ValueError("cannot merge invalid/mismatched interpretation reports")
        for cid, fp in report["fingerprints"].items():
            if cid in result["fingerprints"] and result["fingerprints"][cid] != fp:
                raise ValueError("conflicting interpretation fingerprint: " + cid)
            result["fingerprints"][cid] = fp
        result["fact_dependencies"].update(report.get("fact_dependencies", {}))
        result["required_full_review_ids"].extend(report.get("required_full_review_ids", []))
    result["required_full_review_ids"] = sorted(set(result["required_full_review_ids"]))
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--portfolio", action="store_true", help="Include compact product inventory in positioning context")
    parser.add_argument("--module-insights", action="store_true", help="Request 1–3 fact/insight cards per selected portfolio/cluster/market module")
    parser.add_argument("--merge-validation", nargs="+")
    for name in ("manifest", "facts", "review", "context", "output", "plan", "market",
                 "positioning", "positioning-context", "out"):
        parser.add_argument("--" + name)
    parser.add_argument("--claim-ids", nargs="*", default=[])
    parser.add_argument("--interpretation-ids", nargs="*", default=[])
    args = parser.parse_args()
    try:
        if args.merge_validation:
            result = merge_reports([read(p) for p in args.merge_validation])
            summary = {"errors": result["errors"], "interpretations": len(result["fingerprints"])}
        else:
            if not args.manifest or not args.facts or not args.review:
                parser.error("--manifest, --facts and --review are required")
            manifest, facts, review = read(args.manifest), read(args.facts), read(args.review)
        if not args.merge_validation and args.prepare:
            result = prepare(manifest, facts, review, args.claim_ids,
                             read(args.plan) if args.plan else None,
                             read(args.market) if args.market else None,
                             read(args.positioning) if args.positioning else None,
                             read(args.positioning_context) if args.positioning_context else None,
                             args.interpretation_ids, include_portfolio=args.portfolio,
                             include_module_insights=args.module_insights)
            summary = {"prepared_claims": len(result["facts"]),
                       "prepared_interpretations": len(result["interpretations"]),
                       "pending_checks": result["pending_checks"]}
        elif not args.merge_validation:
            if not args.context or not args.output:
                parser.error("validation requires --context and --output")
            result = validate_output(manifest, facts, review, read(args.context), read(args.output),
                                     read(args.positioning) if args.positioning else None,
                                     read(args.positioning_context) if args.positioning_context else None,
                                     read(args.plan) if args.plan else None)
            summary = {"errors": result["errors"], "interpretations": len(result["fingerprints"])}
        if args.out and not result.get("errors"):
            output_path = Path(args.out).resolve()
            inputs = [args.manifest, args.facts, args.review, args.context, args.output,
                      args.plan, args.market, args.positioning, args.positioning_context]
            inputs.extend(args.merge_validation or [])
            if output_path in {Path(p).resolve() for p in inputs if p}:
                raise ValueError("output may not overwrite input")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 1 if result.get("errors") else 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"errors": [str(exc)]}, ensure_ascii=False))
        return 2

if __name__ == "__main__":
    sys.exit(main())
