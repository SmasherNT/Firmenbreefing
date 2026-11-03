#!/usr/bin/env python3
"""Document batches, conservative change detection and explicit compact verdicts."""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


def helper(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


CHECK = helper('work_check', 'check-interpretation.py')
CACHE = helper('work_cache', 'source-cache.py')
ACCEPTED = {'geprüft', 'übernommen'}
STATES = ACCEPTED | {'nicht einzeln geprüft', 'Korrektur', 'offen'}


def same_identity(obj, manifest, phase=None):
    if any(obj.get(k) != manifest.get(k) for k in ('run_id', 'company', 'as_of')):
        raise ValueError('review work run/company/as_of mismatch')
    if phase is not None and obj.get('phase') != phase:
        raise ValueError('review work phase mismatch')


def refs(value):
    result = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key == 'claim_ids' and isinstance(child, list):
                result.update(c for c in child if isinstance(c, str))
            else:
                result.update(refs(child))
    elif isinstance(value, list):
        for child in value: result.update(refs(child))
    return result


def relevant(value, cid):
    """Keep referenced rows and their ancestor scope, never unrelated siblings."""
    if isinstance(value, dict):
        if cid in value.get('claim_ids', []):
            return value
        children = {k: found for k, v in value.items() if isinstance(v, (dict, list))
                    and (found := relevant(v, cid)) is not None}
        if children:
            context = {k: v for k, v in value.items() if not isinstance(v, (dict, list)) or
                       isinstance(v, list) and all(not isinstance(x, (dict, list)) for x in v)}
            return {**context, **children}
    elif isinstance(value, list):
        found = [r for v in value if (r := relevant(v, cid)) is not None]
        if found: return found
    return None


def binding(manifest, facts, cid):
    views = [v for view in facts.get('module_views', []) if (v := relevant(view, cid)) is not None]
    roles = {v.get('role') for v in views}
    roles.add({'P': 'portfolio', 'C': 'cluster', 'M': 'market', 'T': 'context', 'H': 'context'}.get(cid[:1]))
    network = facts.get('network', {})
    edges = [e for e in network.get('edges', []) if cid in e.get('claim_ids', [])]
    nodes = {n for e in edges for n in (e['from'], e['to'])}
    products = {p for e in edges for p in e.get('product_ids', [])}
    shared = []
    for view in facts.get('module_views', []):
        if cid in refs(view.get('market_dashboard', {})):
            shared.append({'market_dashboard': view['market_dashboard']})
        if cid in refs(view.get('observations', [])):
            shared.append({'peers': view.get('peers', [])})
    return CHECK.digest({'manifest': manifest, 'views': views,
                         'shared': shared,
                         'context': [m for m in facts.get('module_context', []) if m.get('role') in roles],
                         'network': {'edges': edges, 'nodes': [n for n in network.get('nodes', []) if n['id'] in nodes],
                                     'products': [p for p in network.get('products', []) if p['id'] in products]}})


def snapshot(cache, sid):
    if cache is None: return None
    try:
        row = cache.load(sid)
    except FileNotFoundError:
        return None
    return {k: row.get(k) for k in ('source_id', 'url', 'content_sha256', 'text_sha256',
                                   'capture_kind', 'capture_note', 'extraction_notice')}


def verify_work(work):
    if work.get('schema_version') != 1 or work.get('format') != 'review-work-v1':
        raise ValueError('review-work-v1 required')
    if work.get('fingerprint') != CHECK.digest({k: v for k, v in work.items() if k != 'fingerprint'}):
        raise ValueError('review work snapshot changed')


def reviewed(work, review, manifest, phase):
    if work is None and review is None: return {}
    if work is None or review is None:
        raise ValueError('previous work and its explicit review required together')
    verify_work(work); same_identity(work, manifest, phase); same_identity(review, manifest, phase)
    if review.get('review_work_fingerprint') != work['fingerprint']:
        raise ValueError('previous review is not bound to its work snapshot')
    if review.get('status') != 'freigegeben' or review.get('material_errors') != []:
        return {}
    if phase == 'basis' and review.get('scope_and_mappings_checked') is not True:
        return {}
    return {r['id']: r for r in review.get('claims', []) if r.get('depth') == 'A'
            and r.get('status') in ACCEPTED and r.get('fingerprint') == work['items'].get(r.get('id'), {}).get('fingerprint')}


def stable(state):
    return all(s is not None for s in state.get('sources', {}).values())


def prepare(manifest, facts, validation, interpretations=None, cache=None,
            basis_review=None, basis_work=None, previous_work=None, previous_review=None):
    CACHE.identity(manifest)
    phase = validation.get('phase'); same_identity(facts, manifest); same_identity(validation, manifest)
    if phase not in ('basis', 'final') or validation.get('errors') != []:
        raise ValueError('successful basis/final validation required')
    checked = CHECK.helper('work_review', 'check-review-data.py').validate(facts)
    if checked['errors']: raise ValueError('; '.join(checked['errors']))
    fact_rows = CHECK.index(facts['claims'], 'facts')
    if phase == 'basis' and (validation.get('fingerprints') != checked['fingerprints'] or
                            validation.get('packet_fingerprint') != CHECK.digest(facts)):
        raise ValueError('facts validation is stale')
    snapshots = {s['id']: snapshot(cache, s['id']) for s in facts['sources']}
    fact_states = {cid: dict(fingerprint=checked['fingerprints'][cid], mapping=binding(manifest, facts, cid),
                            sources={s: snapshots[s] for s in row['source_ids']}) for cid, row in fact_rows.items()}

    def closure(cid, trail=()):
        if cid not in fact_rows or cid in trail: raise ValueError('unknown/cyclic fact dependency')
        result = {cid}
        for parent in fact_rows[cid].get('depends_on', []): result.update(closure(parent, (*trail, cid)))
        return result

    prior = reviewed(previous_work, previous_review, manifest, phase)
    base = reviewed(basis_work, basis_review, manifest, 'basis') if basis_work is not None else {}
    if basis_work is None and basis_review is not None:
        same_identity(basis_review, manifest, 'basis')
        if basis_review.get('review_work_fingerprint'):
            raise ValueError('bound basis review requires its basis work')
    required = set(validation.get('required_full_review_ids', []))
    if phase == 'basis':
        for cid in refs(facts.get('module_views', [])) | refs(facts.get('network', {})):
            required.update(closure(cid))
        rows = fact_rows
        dependencies = {cid: sorted(closure(cid)) for cid in fact_rows}
    else:
        if basis_review is None: raise ValueError('final work requires released basis review')
        CHECK.env(manifest, facts, basis_review)
        if basis_review.get('input_fingerprint') is not None and basis_review['input_fingerprint'] != CHECK.digest(facts):
            raise ValueError('basis packet/mapping changed; renew basis review first')
        rows = CHECK.index(interpretations or [], 'interpretations')
        if set(rows) != set(validation.get('fingerprints', {})):
            raise ValueError('interpretations do not match final validation')
        dependencies = validation.get('fact_dependencies', {})
        if set(dependencies) != set(rows): raise ValueError('final fact dependencies required')
        if required != set(rows): raise ValueError('every final interpretation requires full review')
    items = {}
    for cid, row in rows.items():
        deps = set(dependencies[cid])
        if not deps <= set(fact_rows): raise ValueError('unknown interpretation fact dependency')
        items[cid] = {'fingerprint': validation['fingerprints'][cid], 'row_fingerprint': CHECK.digest(row),
                      'facts': {fid: fact_states[fid] for fid in sorted(deps)}}
    candidates = [cid for cid, state in items.items() if cid in prior and all(stable(s) for s in state['facts'].values())
                  and previous_work['items'].get(cid) == state]
    used_facts = set().union(*(set(d) for d in dependencies.values())) if dependencies else set()
    fact_reuse = {}
    if phase == 'final':
        for cid in sorted(used_facts):
            state = fact_states[cid]
            if CHECK.ready(cid, CHECK.index(basis_review.get('claims', []), 'basis review'), checked['fingerprints']):
                raise ValueError('final work uses fact without current A-review: ' + cid)
            if cid in base and stable(state) and basis_work['fact_states'].get(cid) == state:
                fact_reuse[cid] = 'basis'
            elif previous_work is not None and previous_review.get('status') == 'freigegeben' and previous_review.get('material_errors') == [] and cid in previous_review.get('fact_review', {}) and stable(state):
                verdict = previous_review['fact_review'][cid]
                if verdict.get('depth') == 'A' and verdict.get('status') in ACCEPTED and previous_work['fact_states'].get(cid) == state:
                    fact_reuse[cid] = 'previous-final'
        # An interpretation cannot inherit an unconfirmed changed original.
        candidates = [cid for cid in candidates if set(dependencies[cid]) <= set(fact_reuse)]
    fact_queue = sorted(used_facts - set(fact_reuse)) if phase == 'final' else sorted(set(rows) - set(candidates))
    batches = []
    for source in facts['sources']:
        sid = source['id']
        ids = [cid for cid, row in fact_rows.items() if sid in row['source_ids']]
        queued = sorted(set(ids) & set(fact_queue))
        batches.append({'source_id': sid, 'fact_ids': sorted(ids), 'review_fact_ids': queued})
    work = {'schema_version': 1, 'format': 'review-work-v1', **CACHE.identity(manifest), 'phase': phase,
            'packet_fingerprint': CHECK.digest(facts), 'items': items, 'fact_states': fact_states,
            'source_snapshots': snapshots, 'required_full_review_ids': sorted(required),
            'reuse_candidates': sorted(candidates), 'claims_to_review': sorted(set(rows) - set(candidates)),
            'fact_reuse_candidates': fact_reuse, 'facts_to_verify': fact_queue if phase == 'final' else [],
            'source_batches': batches, 'removed_ids': sorted(set((previous_work or {}).get('items', {})) - set(items)),
            'inputs': [], 'cache_path': str(cache.root) if cache else None,
            'notice': 'Work order only. No approval generated; explicit reviewer decisions required.'}
    work['fingerprint'] = CHECK.digest(work)
    return work


def verify_current(work):
    verify_work(work)
    for row in work['inputs']:
        if hashlib.sha256(Path(row['path']).read_bytes()).hexdigest() != row['sha256']:
            raise ValueError('review input changed; rebuild work: ' + row['path'])
    cache = CACHE.Cache(work['cache_path'], {'schema_version': 1, 'mode': 'facts-v2', **work}) if work['cache_path'] else None
    for sid, expected in work['source_snapshots'].items():
        if snapshot(cache, sid) != expected:
            raise ValueError('original source snapshot changed; rebuild work: ' + sid)


def expand(draft, validation, work):
    verify_current(work); same_identity(draft, work, work['phase']); same_identity(validation, work, work['phase'])
    if draft.get('review_work_fingerprint') != work['fingerprint']:
        raise ValueError('compact review must name current review_work_fingerprint')
    if 'claims' in draft or not isinstance(draft.get('review_groups'), list):
        raise ValueError('compact review_groups required; do not mix claims format')
    if validation.get('errors') != [] or validation.get('fingerprints') != {cid: s['fingerprint'] for cid, s in work['items'].items()}:
        raise ValueError('compact review validation changed')
    seen_sources = {}
    source_checks = draft.get('source_checks', [])
    if not isinstance(source_checks, list): raise ValueError('source_checks must be a list')
    for row in source_checks:
        sid = row.get('source_id')
        ids = row.get('claim_ids')
        if sid not in work['source_snapshots'] or not isinstance(ids, list) or not ids or len(set(ids)) != len(ids) or not CHECK.text(row.get('note')):
            raise ValueError('explicit document check source/claim_ids/note required')
        expected = work['source_snapshots'][sid]
        for key in ('content_sha256', 'capture_kind'):
            if key in row and (expected is None or row[key] != expected.get(key)):
                raise ValueError('declared document snapshot does not match current work')
        for cid in ids:
            if cid not in work['fact_states'] or sid not in work['fact_states'][cid]['sources']:
                raise ValueError('source check is not mapped to this fact')
            pair = (sid, cid)
            if pair in seen_sources: raise ValueError('duplicate source/claim check')
            seen_sources[pair] = row['note']

    def groups(records, known, candidates, factual=False):
        result = {}
        if not isinstance(records, list): raise ValueError('review groups must be a list')
        for group in records:
            ids = group.get('claim_ids'); status = group.get('status'); depth = group.get('depth')
            if not isinstance(ids, list) or not ids or len(set(ids)) != len(ids) or status not in STATES or depth not in ('A', 'B') or not CHECK.text(group.get('note')):
                raise ValueError('explicit claim_ids/depth/status/note required')
            if status in ('Korrektur', 'offen') and any(not CHECK.text(group.get(k)) for k in ('reason', 'action', 'owner')):
                raise ValueError('issue needs reason/action/owner')
            for cid in ids:
                if cid not in known or cid in result: raise ValueError('unknown/duplicate verdict id')
                if status == 'übernommen' and (depth != 'A' or cid not in candidates):
                    raise ValueError('inheritance requires an unchanged fully reviewed candidate: ' + cid)
                if factual and status == 'geprüft':
                    if any((sid, cid) not in seen_sources for sid in work['fact_states'][cid]['sources']):
                        raise ValueError('each factual source requires explicit document check: ' + cid)
                result[cid] = {**{k: group[k] for k in ('depth', 'status', 'reason', 'action', 'owner') if k in group},
                               'id': cid, 'evidence_review': group['note']}
        return result

    verdicts = groups(draft['review_groups'], work['items'], set(work['reuse_candidates']), work['phase'] == 'basis')
    missing = sorted(set(work['items']) - set(verdicts))
    for cid in missing:
        verdicts[cid] = {'id': cid, 'depth': 'A' if cid in work['required_full_review_ids'] else 'B',
                         'status': 'offen', 'decision_origin': 'missing-reviewer-decision'}
    factual = {}
    if work['phase'] == 'final':
        factual = groups(draft.get('fact_groups', []), set(work['facts_to_verify']), set(), True)
        acknowledged = draft.get('reuse_fact_ids', [])
        if not isinstance(acknowledged, list) or len(set(acknowledged)) != len(acknowledged) or not set(acknowledged) <= set(work['fact_reuse_candidates']):
            raise ValueError('reuse_fact_ids must explicitly name unchanged checked facts')
        for cid in acknowledged:
            factual[cid] = dict(id=cid, depth='A', status='übernommen', evidence_review='Explicit reuse from ' + work['fact_reuse_candidates'][cid])
        used = set(work['facts_to_verify']) | set(work['fact_reuse_candidates'])
        for cid in used - set(factual):
            factual[cid] = dict(id=cid, depth='A', status='offen', decision_origin='missing-reviewer-decision')
        if draft.get('status') == 'freigegeben' and any(r['depth'] != 'A' or r['status'] not in ACCEPTED for r in factual.values()):
            raise ValueError('final release needs explicit checked/reused fact decisions')
    if draft.get('status') == 'freigegeben':
        if work['phase'] == 'basis' and draft.get('scope_and_mappings_checked') is not True:
            raise ValueError('basis release needs explicit scope/module mapping decision')
        for cid in work['required_full_review_ids']:
            row = verdicts.get(cid, {})
            if row.get('depth') != 'A' or row.get('status') not in ACCEPTED:
                raise ValueError('required full check missing: ' + cid)
    result = {k: copy.deepcopy(v) for k, v in draft.items() if k not in ('review_groups', 'fact_groups', 'reuse_fact_ids')}
    result.update(claims=list(verdicts.values()), missing_decisions=missing, fact_review=factual)
    result['source_checks'] = [{**row, 'snapshot': work['source_snapshots'][row['source_id']]} for row in source_checks]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prep = sub.add_parser('prepare')
    for key in ('manifest', 'facts', 'validation', 'out'): prep.add_argument('--' + key, required=True)
    for key in ('cache', 'basis-review', 'basis-work', 'previous-work', 'previous-review',
                'positioning', 'positioning-context', 'swot', 'swot-context', 'plan'):
        prep.add_argument('--' + key)
    show = sub.add_parser('show'); show.add_argument('--work', required=True)
    show.add_argument('--source-id'); show.add_argument('--claim-ids', nargs='*')
    args = parser.parse_args()
    try:
        if args.command == 'show':
            work = CHECK.read(args.work); verify_current(work)
            paths = {r['name']: r['path'] for r in work['inputs']}
            facts = CHECK.read(paths['facts']); fact_rows = CHECK.index(facts['claims'], 'facts')
            if args.source_id:
                batch = next((b for b in work['source_batches'] if b['source_id'] == args.source_id), None)
                if batch is None: raise ValueError('unknown document batch')
                source = next(s for s in facts['sources'] if s['id'] == args.source_id)
                cache = CACHE.Cache(work['cache_path'], CHECK.read(paths['manifest'])) if work['cache_path'] else None
                result = {**batch, 'source': source, 'cached_document': cache.load(args.source_id) if cache and work['source_snapshots'][args.source_id] else None,
                          'facts': [fact_rows[c] for c in batch['review_fact_ids']]}
            elif args.claim_ids:
                rows = {}
                for key in ('positioning', 'swot', 'positioning_context', 'swot_context'):
                    if key in paths:
                        rows.update({r['id']: r for r in CHECK.read(paths[key]).get('interpretations', [])})
                if not set(args.claim_ids) <= set(rows): raise ValueError('unknown interpretation id')
                result = {'interpretations': [rows[c] for c in args.claim_ids],
                          'facts': [fact_rows[c] for c in sorted({f for cid in args.claim_ids for f in work['items'][cid]['facts']})]}
            else:
                result = {k: work[k] for k in ('phase', 'fingerprint', 'claims_to_review', 'reuse_candidates',
                                               'facts_to_verify', 'fact_reuse_candidates', 'source_batches', 'removed_ids')}
            print(json.dumps(result, ensure_ascii=False, indent=2)); return 0
        values = {k: CHECK.read(getattr(args, k)) for k in ('manifest', 'facts', 'validation')}
        optional = ('basis_review', 'basis_work', 'previous_work', 'previous_review', 'positioning',
                    'positioning_context', 'swot', 'swot_context', 'plan')
        values.update({k: CHECK.read(getattr(args, k)) if getattr(args, k) else None for k in optional})
        outputs = []
        if values['validation']['phase'] == 'final':
            for role in ('positioning', 'swot'):
                output, context = values[role], values[role + '_context']
                if output is not None:
                    if context is None: raise ValueError('current interpretation context required')
                    report = CHECK.validate_output(values['manifest'], values['facts'], values['basis_review'], context, output,
                        latest_positioning=values['positioning'] if role == 'swot' else None,
                        latest_positioning_context=values['positioning_context'] if role == 'swot' else None, latest_plan=values['plan'])
                    if report['errors']: raise ValueError('; '.join(report['errors']))
                    outputs.append(report)
            current = CHECK.merge_reports(outputs)
            given = values['validation']; requested = set(given.get('fingerprints', {}))
            if not requested <= set(current['fingerprints']) or any(given.get(k) != current[k] for k in ('run_id', 'company', 'as_of', 'phase', 'errors')) or given.get('fingerprints') != {c: current['fingerprints'][c] for c in requested} or given.get('fact_dependencies') != {c: current['fact_dependencies'][c] for c in requested} or given.get('required_full_review_ids') != sorted(requested):
                raise ValueError('final validation/output/context changed')
        rows = {}
        for key in ('positioning', 'swot', 'positioning_context', 'swot_context'):
            if values[key]: rows.update({r['id']: r for r in values[key].get('interpretations', [])})
        if values['validation']['phase'] == 'final': rows = {c: r for c, r in rows.items() if c in values['validation']['fingerprints']}
        work = prepare(values['manifest'], values['facts'], values['validation'], list(rows.values()),
                       CACHE.Cache(args.cache, values['manifest']) if args.cache else None,
                       values['basis_review'], values['basis_work'], values['previous_work'], values['previous_review'])
        inputs = [k for k in ('manifest', 'facts', 'validation', *optional) if getattr(args, k)]
        target = Path(args.out).resolve()
        if target in {Path(getattr(args, k)).resolve() for k in inputs}: raise ValueError('work must not overwrite inputs')
        for key in inputs:
            path = Path(getattr(args, key)).resolve(); body = path.read_bytes()
            if CHECK.read(path) != values[key]: raise ValueError('review input changed during preparation; retry')
            work['inputs'].append({'name': key, 'path': str(path), 'sha256': hashlib.sha256(body).hexdigest()})
        work['fingerprint'] = CHECK.digest({k: v for k, v in work.items() if k != 'fingerprint'})
        CACHE.write_json(target, work)
        print(json.dumps({'work': str(target), 'documents': len(work['source_batches']),
                          'new_or_changed': len(work['claims_to_review']), 'reuse_candidates': len(work['reuse_candidates']),
                          'facts_to_verify': len(work['facts_to_verify']), 'notice': work['notice']}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({'errors': [str(error)]}, ensure_ascii=False)); return 1


if __name__ == '__main__':
    sys.exit(main())
