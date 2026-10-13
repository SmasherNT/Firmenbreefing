#!/usr/bin/env python3
"""Find reusable complete facts in the current run; never merges or approves them."""
import argparse
from collections import defaultdict
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


def helper(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


FACTS = helper('index_facts', 'prepare-facts.py')
CACHE = helper('index_cache', 'source-cache.py')


def build_index(manifest, modules, module_paths=None):
    ident = CACHE.identity(manifest)
    selected = manifest.get('selected_roles', [])
    if not isinstance(selected, list) or not selected or any(r not in FACTS.ROLES for r in selected):
        raise ValueError('selected_roles required')
    sources, rows, owners, roles = {}, [], {}, set()
    for i, module in enumerate(modules):
        if not isinstance(module, dict) or CACHE.identity(module) != ident:
            raise ValueError('module run/company/as_of mismatch')
        role = module.get('role')
        if role not in selected or role in roles:
            raise ValueError('unselected or duplicate module role')
        roles.add(role)
        if module.get('status') not in FACTS.STATUS:
            raise ValueError('completed module status required')
        if not isinstance(module.get('claims'), list) or not isinstance(module.get('source_proposals'), list):
            raise ValueError('module claims/source_proposals required')
        for source in module['source_proposals']:
            if not isinstance(source, dict) or source.get('id') != FACTS.source_id(source.get('url')):
                raise ValueError('source identity mismatch')
            sid = source['id']
            if sid in sources and sources[sid] != source:
                raise ValueError('conflicting source metadata: ' + sid)
            sources[sid] = source
        for claim in module['claims']:
            if not isinstance(claim, dict) or not isinstance(claim.get('id'), str):
                raise ValueError('claim id required')
            cid = claim['id']
            if not re.fullmatch('(' + '|'.join(FACTS.ROLES[role]) + ')[A-Za-z0-9_-]+', cid):
                raise ValueError('claim id does not belong to role')
            if cid in owners:
                raise ValueError('duplicate claim id: ' + cid)
            if claim.get('kind') not in FACTS.KINDS - {'Nutzerangabe'} or set(claim) & (FACTS.INTERPRETATION_FIELDS | {'score', 'interpretation'}):
                raise ValueError('only factual claims may be indexed')
            owners[cid] = role
            rows.append(claim)
    checked = FACTS.review_validator()({'company': ident['company'], 'as_of': ident['as_of'],
                                        'claims': rows, 'sources': list(sources.values())})
    if checked['errors']:
        raise ValueError('; '.join(checked['errors']))
    groups = defaultdict(list)
    for claim in rows:
        # Candidate grouping only: no fuzzy matching, deletion or silent merging.
        key = json.dumps([re.sub(r'\s+', ' ', claim['statement']).strip().casefold(),
                          claim['kind'], sorted(claim['source_ids']), claim.get('event_date')],
                         ensure_ascii=False, sort_keys=True)
        groups[key].append(claim['id'])
    inputs = []
    if module_paths is not None:
        if len(module_paths) != len(modules):
            raise ValueError('module path count mismatch')
        for path, module in zip(module_paths, modules):
            target = Path(path).resolve()
            body = target.read_bytes()
            if json.loads(body) != module:
                raise ValueError('module changed during index build; retry: ' + str(target))
            inputs.append({'path': str(target), 'sha256': hashlib.sha256(body).hexdigest()})
    result = {'schema_version': 1, **ident, 'status': 'unreviewed-index',
              'available_roles': sorted(roles), 'missing_roles': sorted(set(selected) - roles),
              'inputs': inputs, 'sources': sorted(sources.values(), key=lambda s: s['id']),
              'entries': [{'role': owners[c['id']], 'claim': copy.deepcopy(c),
                           'fingerprint': checked['fingerprints'][c['id']]} for c in rows],
              'duplicate_candidates': [ids for ids in groups.values() if len(ids) > 1],
              'notice': 'Discovery/reuse index only. Claims retain original ownership; no content approval or automatic merge.'}
    return result


def find(index, manifest, query='', claim_ids=None):
    ident = CACHE.identity(manifest)
    if index.get('status') != 'unreviewed-index' or any(index.get(k) != v for k, v in ident.items()):
        raise ValueError('index run/company/as_of mismatch')
    for record in index.get('inputs', []):
        if hashlib.sha256(Path(record['path']).read_bytes()).hexdigest() != record['sha256']:
            raise ValueError('indexed module changed; rebuild index: ' + record['path'])
    wanted, words = set(claim_ids or []), query.casefold().split()
    result = []
    for entry in index['entries']:
        claim = entry['claim']
        text = json.dumps(claim, ensure_ascii=False).casefold()
        if (not wanted or claim['id'] in wanted) and all(w in text for w in words):
            result.append(entry)
    if wanted - {e['claim']['id'] for e in result}:
        raise ValueError('requested claim not found in current index')
    return {'status': 'unreviewed-index', 'entries': result,
            'notice': index['notice'], 'missing_roles': index['missing_roles']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', required=True)
    sub = parser.add_subparsers(dest='command', required=True)
    build = sub.add_parser('build'); build.add_argument('--modules', nargs='+', required=True)
    build.add_argument('--out', required=True)
    search = sub.add_parser('find'); search.add_argument('--index', required=True)
    search.add_argument('--query', default=''); search.add_argument('--claim-ids', nargs='*')
    args = parser.parse_args()
    try:
        def read(path):
            return json.loads(Path(path).read_text(encoding='utf-8'))
        manifest = read(args.manifest)
        if args.command == 'build':
            target = Path(args.out).resolve()
            if target in {Path(p).resolve() for p in [args.manifest, *args.modules]}:
                raise ValueError('index must not overwrite inputs')
            index = build_index(manifest, [read(p) for p in args.modules], args.modules)
            CACHE.write_json(target, index)
            result = {'index': str(target), 'claims': len(index['entries']),
                      'duplicate_candidates': index['duplicate_candidates'], 'missing_roles': index['missing_roles'],
                      'notice': index['notice']}
        else:
            result = find(read(args.index), manifest, args.query, args.claim_ids)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(json.dumps({'errors': [str(error)]}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    sys.exit(main())
