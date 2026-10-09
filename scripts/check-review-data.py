#!/usr/bin/env python3
"""Validate a compact review packet; never verifies source truth or reachability."""
import argparse
import hashlib
import json
import re
import sys
from datetime import date
from urllib.parse import urlparse

def validate(data):
    errors = []
    fingerprints = {}
    def fail(message):
        errors.append(message)
    def day(value, nullable=False):
        if value is None:
            return nullable
        if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return False
        try:
            date.fromisoformat(value)
            return True
        except ValueError:
            return False
    def index(rows, label):
        found = {}
        if not isinstance(rows, list):
            fail(label + ": list required")
            return found
        for row in rows:
            if not isinstance(row, dict):
                fail(label + ": object required")
                continue
            ident = row.get("id")
            if not isinstance(ident, str) or not ident.strip():
                fail(label + ": missing id")
            elif ident in found:
                fail(label + ": duplicate id " + ident)
            else:
                found[ident] = row
        return found
    def refs(row, field, known, label, required=True):
        values = row.get(field)
        if not isinstance(values, list) or (required and not values):
            fail(label + ": invalid " + field)
            return []
        for value in values:
            if not isinstance(value, str) or value not in known:
                fail(label + ": unknown " + field + " " + repr(value))
        return [v for v in values if isinstance(v, str) and v in known]
    if not isinstance(data, dict):
        return {"errors": ["packet: object required"], "fingerprints": {}}
    if not isinstance(data.get("company"), str) or not data["company"].strip():
        fail("packet: missing company")
    if not day(data.get("as_of")):
        fail("packet: invalid as_of")
    sources = index(data.get("sources"), "sources")
    claims = index(data.get("claims"), "claims")
    for ident, source in sources.items():
        for field in ("name", "title", "url"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                fail(ident + ": missing " + field)
        try:
            url = urlparse(source.get("url", ""))
            if url.scheme not in ("http", "https") or not url.netloc:
                fail(ident + ": invalid url")
        except (ValueError, TypeError):
            fail(ident + ": invalid url")
        if "published_date" not in source or not day(source.get("published_date"), True):
            fail(ident + ": invalid published_date (use null for unknown)")
        if not day(source.get("accessed_date")):
            fail(ident + ": invalid accessed_date")
    for ident, claim in claims.items():
        for field in ("statement", "evidence", "location"):
            if not isinstance(claim.get(field), str) or not claim[field].strip():
                fail(ident + ": missing " + field)
        if not isinstance(claim.get("uncertainty"), str):
            fail(ident + ": uncertainty required (empty string allowed)")
        source_ids = refs(claim, "source_ids", sources, ident)
        if "depends_on" in claim:
            refs(claim, "depends_on", claims, ident, required=False)
        canonical = {"company": data.get("company"), "as_of": data.get("as_of"),
                     "claim": claim, "sources": {s: sources[s] for s in sorted(set(source_ids))}}
        fingerprints[ident] = hashlib.sha256(json.dumps(
            canonical, sort_keys=True, ensure_ascii=False, separators=(",", ":")
        ).encode()).hexdigest()
    network = data.get("network")
    if network is not None:
        if not isinstance(network, dict):
            fail("network: object required")
        else:
            if network.get("company") != data.get("company") or network.get("as_of") != data.get("as_of"):
                fail("network: company/as_of mismatch")
            nodes = index(network.get("nodes"), "network nodes")
            edges = index(network.get("edges"), "network edges")
            net_sources = index(network.get("sources"), "network sources")
            products = index(network.get("products"), "network products")
            target = network.get("target_id")
            targets = [n for n, row in nodes.items() if row.get("kind") == "target"]
            if not isinstance(target, str) or target not in nodes or targets != [target]:
                fail("network: exactly one matching target required")
            for ident, source in net_sources.items():
                if ident not in sources or source != sources[ident]:
                    fail("network source " + ident + ": missing or inconsistent packet source")
            for ident, edge in edges.items():
                for field in ("from", "to"):
                    if not isinstance(edge.get(field), str) or edge[field] not in nodes:
                        fail(ident + ": unknown " + field + " node")
                if edge.get("from") == edge.get("to"):
                    fail(ident + ": self edge")
                refs(edge, "source_ids", net_sources, ident)
                refs(edge, "claim_ids", claims, ident)
                refs(edge, "product_ids", products, ident, required=False)
    return {"errors": errors, "fingerprints": fingerprints,
            "notice": "Formal validation only; source content and truth not checked."}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet")
    args = parser.parse_args()
    try:
        with open(args.packet, encoding="utf-8") as handle:
            result = validate(json.load(handle))
    except (OSError, ValueError) as exc:
        print(json.dumps({"errors": [str(exc)]}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0

if __name__ == "__main__":
    sys.exit(main())
