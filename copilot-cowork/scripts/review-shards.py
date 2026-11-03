#!/usr/bin/env python3
"""Partition original-source checks; merge explicit verdicts without granting approval."""
import argparse
import copy
import json
from pathlib import Path
import sys
import importlib.util

_spec = importlib.util.spec_from_file_location('sharded_work', Path(__file__).with_name('review-work.py'))
WORK = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(WORK)
CHECK = WORK.CHECK
STATES = {'geprüft', 'nicht einzeln geprüft', 'Korrektur', 'offen'}


def digest_record(obj):
    return CHECK.digest({k:v for k,v in obj.items() if k != 'fingerprint'})


def current(work, facts):
    WORK.verify_current(work)
    WORK.same_identity(facts, work)
    if CHECK.digest(facts) != work['packet_fingerprint']:
        raise ValueError('facts changed; rebuild work and split plan')


def review_models():
    policy = CHECK.read(Path(__file__).resolve().parents[1] / 'references' / 'modellaufteilung.json')
    return {role: copy.deepcopy(policy['agents'][role])
            for role in ('source-document-reviewer', 'source-reviewer')}


def split(work, facts, workers=3):
    current(work, facts)
    if type(workers) is not int or not 1 <= workers <= 3:
        raise ValueError('workers must be 1, 2 or 3; default is 3')
    rows = CHECK.index(facts['claims'], 'facts')
    batches = [b for b in work['source_batches'] if b['review_fact_ids']]
    jobs = [dict(id='sources-'+str(i+1), source_ids=[], load_chars=0, **review_models()['source-document-reviewer'])
            for i in range(min(workers, len(batches)))]
    def weight(batch):
        # A deterministic load proxy, never a measured token estimate.
        return sum(len(json.dumps(rows[c], ensure_ascii=False)) for c in batch['review_fact_ids'])
    for batch in sorted(batches, key=lambda b:(-weight(b), b['source_id'])):
        job = min(jobs, key=lambda j:(j['load_chars'], j['id']))
        job['source_ids'].append(batch['source_id'])
        job['load_chars'] += weight(batch)
    for job in jobs:
        job['source_ids'].sort()
    result = dict(schema_version=1, format='review-split-v1',
        **{k:work[k] for k in ('run_id','company','as_of')}, phase=work['phase'], review_work_fingerprint=work['fingerprint'],
        workers_requested=workers, model_policy=review_models(), jobs=jobs,
        notice='Original-source checks only. Lead reviewer retains claim, scope and release decisions.')
    result['fingerprint'] = digest_record(result)
    return result


def verify_plan(plan, work, facts):
    current(work, facts)
    if plan != split(work, facts, plan.get('workers_requested')):
        raise ValueError('split plan changed or belongs to another work snapshot')


def show(plan, work, facts, job_id):
    verify_plan(plan, work, facts)
    job = next((j for j in plan['jobs'] if j['id'] == job_id), None)
    if not job:
        raise ValueError('unknown source job')
    rows = CHECK.index(facts['claims'], 'facts')
    sources = CHECK.index(facts['sources'], 'sources')
    batches = {b['source_id']:b for b in work['source_batches']}
    documents = []
    claim_ids = set()
    for sid in job['source_ids']:
        ids = batches[sid]['review_fact_ids']
        claim_ids.update(ids)
        documents.append(dict(source=sources[sid], snapshot=work['source_snapshots'][sid], review_fact_ids=ids))
    return dict(schema_version=1, **{k:work[k] for k in ('run_id','company','as_of')}, phase=work['phase'],
        job_id=job_id, model=job['model'], effort=job['effort'], review_work_fingerprint=work['fingerprint'],
        plan_fingerprint=plan['fingerprint'], cache_path=work.get('cache_path'), documents=documents,
        facts=[rows[c] for c in sorted(claim_ids)],
        required_A_ids=sorted(claim_ids & set(work['required_full_review_ids'])) if work['phase']=='basis' else sorted(claim_ids),
        network_edges=[e for e in (facts.get('network') or {}).get('edges', []) if claim_ids & set(e.get('claim_ids', []))],
        notice='Check only the assigned original for each fact. Other references remain visible but are owned by other jobs. Expand source context when needed. Global module_views, scope and inference checks belong to the lead reviewer; do not read the entire packet by default.')


def collect(plan, work, facts, parts):
    verify_plan(plan, work, facts)
    if not isinstance(parts, list):
        raise ValueError('source parts must be a list')
    jobs = {j['id']:j for j in plan['jobs']}
    batches = {b['source_id']:set(b['review_fact_ids']) for b in work['source_batches']}
    got, by_claim, checks, issues, part_hashes = set(), {}, [], [], {}
    for part in parts:
        WORK.same_identity(part, work, work['phase'])
        job_id = part.get('job_id')
        if part.get('schema_version') != 1 or part.get('format') != 'review-source-part-v1' or job_id not in jobs or job_id in got:
            raise ValueError('unknown/duplicate source part or wrong format')
        if part.get('plan_fingerprint') != plan['fingerprint'] or part.get('review_work_fingerprint') != work['fingerprint']:
            raise ValueError('source part is stale or names another split plan')
        documents = part.get('documents')
        if not isinstance(documents, list):
            raise ValueError('source part needs document findings')
        got.add(job_id); seen_docs = set()
        for doc in documents:
            sid = doc.get('source_id')
            if sid not in jobs[job_id]['source_ids'] or sid in seen_docs:
                raise ValueError('document outside job or duplicate document')
            if type(doc.get('original_read')) is not bool or not CHECK.text(doc.get('note')):
                raise ValueError('explicit original_read and document note required')
            seen_docs.add(sid)
            findings = doc.get('findings')
            if not isinstance(findings, list):
                raise ValueError('document needs per-claim findings')
            seen_claims, read_ids = set(), []
            for finding in findings:
                cid = finding.get('claim_id'); depth = finding.get('depth'); state = finding.get('status')
                if cid not in batches[sid] or cid in seen_claims:
                    raise ValueError('claim outside assigned source or duplicate finding')
                if depth not in ('A','B') or state not in STATES or not CHECK.text(finding.get('note')):
                    raise ValueError('explicit claim depth/status/note required')
                if state == 'geprüft' and doc['original_read'] is not True:
                    raise ValueError('checked finding requires original reading')
                if state in ('Korrektur','offen') and any(not CHECK.text(finding.get(k)) for k in ('reason','action','owner')):
                    raise ValueError('source issue needs reason/action/owner')
                seen_claims.add(cid)
                by_claim.setdefault(cid, []).append(dict(source_id=sid, **copy.deepcopy(finding)))
                if state == 'geprüft':
                    read_ids.append(cid)
                if state in ('Korrektur','offen'):
                    issues.append(dict(source_id=sid, **copy.deepcopy(finding)))
            if seen_claims != batches[sid]:
                raise ValueError('source part missing per-claim findings')
            if read_ids:
                checks.append(dict(source_id=sid, claim_ids=sorted(read_ids), note=doc['note']))
        if seen_docs != set(jobs[job_id]['source_ids']):
            raise ValueError('source part missing assigned documents')
        part_hashes[job_id] = CHECK.digest(part)
    if got != set(jobs):
        raise ValueError('missing source worker results')
    result = dict(schema_version=1, format='review-source-collection-v1', **{k:work[k] for k in ('run_id','company','as_of')},
        phase=work['phase'], review_work_fingerprint=work['fingerprint'], plan_fingerprint=plan['fingerprint'],
        part_fingerprints=part_hashes, source_checks=sorted(checks, key=lambda x:x['source_id']),
        findings={cid:sorted(rows, key=lambda x:x['source_id']) for cid,rows in sorted(by_claim.items())},
        issues=issues, notice='Source evidence only; no claim approval, mapping approval or release generated.')
    result['fingerprint'] = digest_record(result)
    return result


def merge(plan, work, facts, parts, lead, validation):
    report = collect(plan, work, facts, parts)
    WORK.same_identity(lead, work, work['phase'])
    if lead.get('plan_fingerprint') != plan['fingerprint'] or lead.get('source_collection_fingerprint') != report['fingerprint']:
        raise ValueError('lead must acknowledge the current plan and source findings')
    if lead.get('source_checks'):
        raise ValueError('lead must not override worker source checks; correct assigned findings first')
    # No majority vote and no automatic approval. Every original must support
    # each factual verdict accepted by the independent lead reviewer.
    factual_groups = lead.get('review_groups', []) if work['phase']=='basis' else lead.get('fact_groups', [])
    if not isinstance(factual_groups, list):
        raise ValueError('lead factual decisions must be a list')
    for group in factual_groups:
        if group.get('status') != 'geprüft':
            continue
        for cid in group.get('claim_ids', []):
            findings = report['findings'].get(cid, [])
            expected_sources = set(work['fact_states'].get(cid, {}).get('sources', {}))
            if {f['source_id'] for f in findings} != expected_sources:
                raise ValueError('accepted claim missing original-source findings: '+cid)
            if any(f['status'] != 'geprüft' or (group.get('depth')=='A' and f['depth']!='A') for f in findings):
                raise ValueError('unresolved source finding or insufficient depth blocks acceptance: '+cid)
    if report['issues'] and lead.get('status') == 'freigegeben':
        raise ValueError('unresolved source issues block release')
    result = copy.deepcopy(lead)
    result['source_checks'] = report['source_checks']
    result['parallel_review'] = dict(plan_fingerprint=plan['fingerprint'],
        source_collection_fingerprint=report['fingerprint'], part_fingerprints=report['part_fingerprints'],
        model_policy=copy.deepcopy(plan['model_policy']))
    # Existing gates still enforce all required A-claims, I/S decisions, original
    # snapshots, explicit reuse and the global scope/mapping decision.
    WORK.expand(result, validation, work)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('split','show','collect','merge'):
        cmd = sub.add_parser(name)
        for key in ('work','facts'):
            cmd.add_argument('--'+key, required=True)
        if name == 'split':
            cmd.add_argument('--workers', type=int, default=3)
        else:
            cmd.add_argument('--plan', required=True)
        if name == 'show':
            cmd.add_argument('--job', required=True)
        if name in ('collect','merge'):
            cmd.add_argument('--parts', nargs='*', required=True)
        if name == 'merge':
            cmd.add_argument('--lead', required=True); cmd.add_argument('--validation', required=True)
        if name != 'show':
            cmd.add_argument('--out', required=True)
    args = parser.parse_args()
    try:
        work, facts = CHECK.read(args.work), CHECK.read(args.facts)
        if args.command == 'split':
            result = split(work, facts, args.workers)
        else:
            plan = CHECK.read(args.plan)
            if args.command == 'show':
                result = show(plan, work, facts, args.job)
                print(json.dumps(result, ensure_ascii=False, indent=2)); return 0
            parts = [CHECK.read(p) for p in args.parts]
            if args.command == 'collect':
                result = collect(plan, work, facts, parts)
            else:
                result = merge(plan, work, facts, parts, CHECK.read(args.lead), CHECK.read(args.validation))
        target = Path(args.out).resolve()
        inputs = [args.work, args.facts] + ([args.plan] if args.command!='split' else [])
        if args.command in ('collect','merge'):
            inputs += args.parts
        if args.command == 'merge':
            inputs += [args.lead, args.validation]
        if target in {Path(p).resolve() for p in inputs}:
            raise ValueError('cannot overwrite review inputs')
        WORK.CACHE.write_json(target, result)
        print(json.dumps(dict(output=str(target), command=args.command,
            jobs=len(result.get('jobs', [])) if args.command=='split' else None,
            notice='No approval generated; explicit lead review and stamp-review remain required.'), ensure_ascii=False))
        return 0
    except (ValueError, TypeError, KeyError, AttributeError, OSError) as error:
        print(json.dumps({'errors':[str(error)]}, ensure_ascii=False)); return 1


if __name__ == '__main__':
    sys.exit(main())
