#!/usr/bin/env python3
"""Consolidate facts-v2 modules; validate metadata, references and phase boundaries."""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROLES = {"context": ("T", "H"), "portfolio": ("P",),
         "cluster": ("C",), "market": ("M",)}
KINDS = {"Fakt", "Herstellerangabe", "Partnerangabe", "Nutzerangabe"}
STATUS = {"vollständig", "teilweise", "blockiert"}
INTERPRETATION_FIELDS = {"interpretations", "swot", "scores", "rankings", "ratings"}

def source_id(url):
    if not isinstance(url, str):
        raise ValueError("source URL must be a string")
    parts = urlsplit(url.strip())
    if parts.scheme not in {"https", "http"} or not parts.netloc:
        raise ValueError("source URL must use http(s)")
    document = urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))
    return "S-" + hashlib.sha256(document.encode()).hexdigest()[:16]

def day(value):
    try:
        return isinstance(value, str) and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)) and bool(date.fromisoformat(value))
    except ValueError:
        return False

def nonempty(value):
    return isinstance(value, str) and bool(value.strip())

def validate_plan(plan, manifest):
    errors = []
    if not isinstance(plan, dict):
        return ["comparison plan must be an object"]
    for key in ("company", "as_of", "run_id"):
        if plan.get(key) != manifest.get(key):
            errors.append("comparison plan mismatch: " + key)
    for key in ("comparison_unit", "purpose"):
        if not nonempty(plan.get(key)):
            errors.append("comparison plan missing: " + key)
    if not isinstance(plan.get("version"), int) or isinstance(plan.get("version"), bool) or plan["version"] < 1:
        errors.append("comparison plan version must be a positive integer")
    if not isinstance(plan.get("peer_groups"), list) or not plan["peer_groups"]:
        errors.append("comparison plan needs peer_groups")
    criteria = plan.get("criteria")
    if not isinstance(criteria, list) or not criteria:
        return errors + ["comparison plan needs criteria"]
    seen = set()
    for row in criteria:
        if not isinstance(row, dict):
            errors.append("criterion must be an object")
            continue
        cid = row.get("id")
        if not nonempty(cid) or cid in seen:
            errors.append("criterion id missing/duplicate")
        else:
            seen.add(cid)
        for field in ("label", "question", "evidence_required", "applicability", "rationale"):
            if not nonempty(row.get(field)):
                errors.append(str(cid) + ": missing " + field)
        if row.get("display_type") not in ("Profil", "Kennzahl", "Evidenzstufe"):
            errors.append(str(cid) + ": invalid display_type")
        if row.get("display_type") == "Kennzahl":
            for key in ("unit", "conditions"):
                if not nonempty(row.get(key)):
                    errors.append(str(cid) + ": define metric " + key)
        if row.get("display_type") == "Evidenzstufe":
            anchors = row.get("anchors")
            if not isinstance(anchors, dict) or not anchors or any(not nonempty(v) for v in anchors.values()):
                errors.append(str(cid) + ": define anchors before scoring")
    return errors

def review_validator():
    path = Path(__file__).with_name("check-review-data.py")
    spec = importlib.util.spec_from_file_location("review_metadata", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate

def build(manifest, modules, plan=None):
    errors = []
    claims, sources, networks, roles = [], {}, [], set()
    if not isinstance(manifest, dict):
        return {"errors": ["manifest must be an object"]}, None
    if manifest.get("schema_version") != 1 or manifest.get("mode") != "facts-v2":
        errors.append("manifest must be schema_version=1, mode=facts-v2")
    for key in ("run_id", "company", "scope"):
        if not nonempty(manifest.get(key)):
            errors.append("manifest missing " + key)
    if not day(manifest.get("as_of")):
        errors.append("manifest invalid as_of")
    selected = manifest.get("selected_roles")
    if not isinstance(selected, list) or not selected or any(not isinstance(r, str) or r not in ROLES for r in selected):
        errors.append("manifest invalid selected_roles")
        selected = []
    elif len(set(selected)) != len(selected):
        errors.append("manifest duplicate selected_roles")
    if plan is not None:
        errors.extend(validate_plan(plan, manifest))
    elif manifest.get("comparison_plan_path"):
        errors.append("comparison plan must be provided")

    for data in modules:
        if not isinstance(data, dict):
            errors.append("module must be an object")
            continue
        role = data.get("role")
        if not isinstance(role, str) or role not in ROLES:
            errors.append("module invalid role")
            continue
        if role in roles or role not in selected:
            errors.append("module role duplicate/unselected: " + role)
        roles.add(role)
        if data.get("schema_version") != 1 or data.get("mode") != "facts-v2":
            errors.append(role + ": wrong schema/mode")
        for key in ("run_id", "company", "as_of"):
            if data.get(key) != manifest.get(key):
                errors.append(role + ": mismatch " + key)
        if not nonempty(data.get("scope")) or data.get("status") not in STATUS:
            errors.append(role + ": scope/status missing or invalid")
        for field in ("claims", "source_proposals", "gaps", "coverage"):
            if not isinstance(data.get(field), list):
                errors.append(role + ": " + field + " must be a list")
        for field in INTERPRETATION_FIELDS:
            if field in data:
                errors.append(role + ": interpretation field prohibited: " + field)
        for src in data.get("source_proposals", []) if isinstance(data.get("source_proposals"), list) else []:
            if not isinstance(src, dict):
                errors.append(role + ": source must be an object")
                continue
            try:
                sid = source_id(src.get("url"))
            except ValueError as exc:
                errors.append(role + ": " + str(exc))
                continue
            if src.get("id") != sid:
                errors.append(role + ": use deterministic source id " + sid)
                continue
            if not nonempty(src.get("source_kind")):
                errors.append(sid + ": missing source_kind")
            old = sources.get(sid)
            if old is not None and old != src:
                errors.append(sid + ": conflicting source metadata; resolve explicitly")
            sources[sid] = src
        rows = data.get("claims", [])
        for row in rows if isinstance(rows, list) else []:
            if not isinstance(row, dict):
                errors.append(role + ": claim must be an object")
                continue
            cid = row.get("id")
            if not nonempty(cid) or not re.fullmatch(r"(" + "|".join(ROLES[role]) + r")[A-Za-z0-9_-]+", cid):
                errors.append(role + ": invalid claim id prefix")
            if row.get("kind") not in KINDS:
                errors.append(str(cid) + ": invalid factual kind")
            if row.get("kind") == "Nutzerangabe":
                errors.append(str(cid) + ": unverified user input belongs in gaps")
            for field in INTERPRETATION_FIELDS | {"score", "interpretation"}:
                if field in row:
                    errors.append(str(cid) + ": interpretation field prohibited")
            items = row.get("evidence_items")
            if items is not None:
                if not isinstance(items, list) or not items:
                    errors.append(str(cid) + ": invalid evidence_items")
                else:
                    supports = set()
                    for item in items:
                        if not isinstance(item, dict):
                            errors.append(str(cid) + ": evidence item must be an object")
                            continue
                        sid = item.get("source_id")
                        if not isinstance(sid, str) or sid not in row.get("source_ids", []):
                            errors.append(str(cid) + ": evidence item source not referenced")
                        else:
                            supports.add(sid)
                        if item.get("mode") not in ("Auszug", "Paraphrase") or not nonempty(item.get("text")) or not nonempty(item.get("location")):
                            errors.append(str(cid) + ": incomplete evidence item")
                    if supports != set(x for x in row.get("source_ids", []) if isinstance(x, str)):
                        errors.append(str(cid) + ": each source needs a mapped evidence item")
            elif isinstance(row.get("source_ids"), list) and len(row["source_ids"]) > 1:
                errors.append(str(cid) + ": multiple sources need evidence_items")
            claims.append(row)
        network = data.get("network")
        if role == "cluster" and not isinstance(network, dict):
            errors.append("cluster: network required (can contain only target)")
        if isinstance(network, dict):
            if role != "cluster":
                errors.append(role + ": only cluster owns network")
            networks.append(network)
            for edge in network.get("edges", []):
                if isinstance(edge, dict) and "interpretation" in edge:
                    errors.append("network: interpretation prohibited")
        observations = data.get("observations", [])
        if observations and (role != "market" or plan is None):
            errors.append(role + ": observations require market role and comparison plan")
        if plan is not None and role == "market":
            if data.get("comparison_plan_version") != plan.get("version"):
                errors.append("market: comparison_plan_version mismatch")
            criteria = {c["id"] for c in plan.get("criteria", []) if isinstance(c, dict) and isinstance(c.get("id"), str)}
            peers = {p["id"] for p in data.get("peers", []) if isinstance(p, dict) and isinstance(p.get("id"), str)}
            if not isinstance(observations, list):
                errors.append("market: observations must be a list")
            else:
                for row in observations:
                    if not isinstance(row, dict):
                        errors.append("market: observation must be an object")
                        continue
                    if row.get("criterion_id") not in criteria or row.get("peer_id") not in peers:
                        errors.append("market: observation references unknown peer/criterion")
                    if any(f in row for f in INTERPRETATION_FIELDS | {"score", "rating", "interpretation"}):
                        errors.append("market: observation must not contain scores")
    if set(selected) != roles:
        errors.append("missing selected modules: " + ", ".join(sorted(set(selected) - roles)))
    ids = {c.get("id") for c in claims if isinstance(c.get("id"), str)}
    for data in modules:
        if not isinstance(data, dict):
            continue
        refs = data.get("reuse_claim_ids", [])
        if not isinstance(refs, list) or any(not isinstance(c, str) or c not in ids for c in refs):
            errors.append("module: invalid reuse_claim_ids")
        for row in data.get("observations", []) if isinstance(data.get("observations", []), list) else []:
            if isinstance(row, dict):
                refs = row.get("claim_ids")
                if not isinstance(refs, list) or not refs or any(not isinstance(c, str) or c not in ids for c in refs):
                    errors.append("market: observation requires known claim_ids")
    packet = {"company": manifest.get("company"), "as_of": manifest.get("as_of"),
              "claims": claims, "sources": sorted(sources.values(), key=lambda s: s["id"]),
              "module_context": [{"role": d.get("role"), "scope": d.get("scope"),
                                  "status": d.get("status"),
                                  "shared_limitations": d.get("shared_limitations", []),
                                  "document_scope": d.get("document_scope", "")}
                                 for d in modules if isinstance(d, dict)]}
    if networks:
        packet["network"] = networks[0]
    check = review_validator()(packet)
    errors.extend(check["errors"])
    return {"errors": errors, "fingerprints": check.get("fingerprints", {}),
            "module_status": {d.get("role"): d.get("status") for d in modules if isinstance(d, dict) and isinstance(d.get("role"), str)},
            "notice": "Formal validation only; factual accuracy, coverage and source independence not verified."}, packet

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id")
    parser.add_argument("--manifest")
    parser.add_argument("--modules", nargs="+")
    parser.add_argument("--plan")
    parser.add_argument("--out")
    args = parser.parse_args()
    try:
        if args.source_id:
            print(source_id(args.source_id))
            return 0
        if not args.manifest or not args.modules:
            parser.error("--manifest and --modules are required")
        def read(path):
            return json.loads(Path(path).read_text(encoding="utf-8"))
        result, packet = build(read(args.manifest), [read(p) for p in args.modules],
                               read(args.plan) if args.plan else None)
        summary = {"errors": result["errors"],
                   "claims": len(packet["claims"]) if packet else 0,
                   "sources": len(packet["sources"]) if packet else 0,
                   "module_status": result.get("module_status", {}),
                   "notice": result.get("notice", "")}
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        if result["errors"]:
            return 1
        if args.out:
            output = Path(args.out)
            input_paths = {Path(p).resolve() for p in [args.manifest, *args.modules, *([args.plan] if args.plan else [])]}
            targets = [output / n for n in ("sources.json", "review-packet.json", "facts-validation.json")]
            if any(t.resolve() in input_paths for t in targets):
                raise ValueError("output must not overwrite an input file")
            output.mkdir(parents=True, exist_ok=True)
            for name, obj in (("sources.json", {"run_id": read(args.manifest)["run_id"], "company": packet["company"], "as_of": packet["as_of"], "sources": packet["sources"]}),
                              ("review-packet.json", packet), ("facts-validation.json", result)):
                (output / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"errors": [str(exc)]}, ensure_ascii=False))
        return 2

if __name__ == "__main__":
    sys.exit(main())
