#!/usr/bin/env python3
"""Attach mechanical fingerprints to explicit reviewer decisions; never grants approval."""
import argparse
import json
from pathlib import Path

def stamp(draft, validation):
    if draft.get("phase") not in {"basis", "final"} or draft.get("status") not in {"freigegeben", "teilweise", "blockiert"}:
        raise ValueError("explicit phase/status required")
    if draft.get("schema_version") != 1 or any(not draft.get(k) for k in ("run_id", "company", "as_of")):
        raise ValueError("review identity required")
    if not isinstance(draft.get("material_errors"), list) or not isinstance(draft.get("claims"), list):
        raise ValueError("material_errors and claims required")
    if validation.get("errors") != [] or not isinstance(validation.get("fingerprints"), dict):
        raise ValueError("successful mechanical validation required")
    if any(draft.get(k) != validation.get(k) for k in ("run_id", "company", "as_of", "phase")):
        raise ValueError("validation/review identity mismatch")
    if draft["status"] == "freigegeben" and draft["material_errors"]:
        raise ValueError("material errors block release")
    known = validation["fingerprints"]
    seen = set()
    rows = []
    for row in draft["claims"]:
        cid = row.get("id")
        if not isinstance(cid, str) or cid in seen or cid not in known:
            raise ValueError("unknown/duplicate review claim")
        if row.get("depth") not in {"A", "B"} or row.get("status") not in {"geprüft", "übernommen", "nicht einzeln geprüft", "Korrektur", "offen"}:
            raise ValueError("explicit review depth/status required")
        if draft["status"] == "freigegeben" and row["depth"] == "A" and row["status"] not in {"geprüft", "übernommen"}:
            raise ValueError("unresolved A-claim blocks release")
        rows.append({**row, "fingerprint": known[cid]})
        seen.add(cid)
    if draft["status"] == "freigegeben":
        by_id = {r["id"]: r for r in rows}
        for cid in validation.get("required_full_review_ids", []):
            row = by_id.get(cid, {})
            if row.get("depth") != "A" or row.get("status") not in {"geprüft", "übernommen"}:
                raise ValueError("required full check missing: " + cid)
    result = {**draft, "claims": rows}
    if draft["phase"] == "basis" and validation.get("packet_fingerprint"):
        result["input_fingerprint"] = validation["packet_fingerprint"]
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--draft", required=True)
    parser.add_argument("--validation", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    try:
        inputs = [Path(args.draft), Path(args.validation)]
        output = Path(args.out)
        if output.resolve() in {p.resolve() for p in inputs}:
            raise ValueError("cannot overwrite inputs")
        result = stamp(*[json.loads(p.read_text(encoding="utf-8")) for p in inputs])
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.suffix == ".md":
            body = "# Review\n\n```json\n" + json.dumps(result, ensure_ascii=False, indent=2) + "\n```\n"
        else:
            body = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        output.write_text(body, encoding="utf-8")
        print(json.dumps({"review_claims": len(result["claims"]), "status": result["status"],
                          "notice": "Reviewer decisions preserved; no content approval generated."}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(json.dumps({"errors": [str(exc)]}, ensure_ascii=False))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
