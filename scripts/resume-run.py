#!/usr/bin/env python3
"""Validate explicit run checkpoints; never runs agents or creates reviewer decisions."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import fcntl
import hashlib
import json
from pathlib import Path
import sys
import time
import uuid

import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def helper(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/filename)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


WORK = helper('resume_work', 'review-work.py')
CHECK, CACHE = WORK.CHECK, WORK.CACHE
FACTS = helper('resume_facts', 'prepare-facts.py')
STAMP = helper('resume_stamp', 'stamp-review.py')
RENDER = helper('resume_render', 'render-briefing.py')
ROLES = ('context', 'portfolio', 'cluster', 'market')
AGENTS = dict(context='company-context-analyst', portfolio='portfolio-analyst',
              cluster='cluster-analyst', market='market-facts-analyst',
              positioning='positioning-analyst', swot='swot-analyst')
MAX_SOURCE_AGE = timedelta(hours=24)


def require(condition, message):
    if not condition: raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def seal(obj):
    return {**obj, 'fingerprint': CHECK.digest({k: v for k, v in obj.items() if k != 'fingerprint'})}


def verified(obj):
    require(isinstance(obj, dict) and obj.get('fingerprint') == seal(obj)['fingerprint'],
            'checkpoint state corrupt or incomplete; do not reuse it')
    return obj


@contextmanager
def state_lock(path):
    """OS-owned lock releases even after process termination; atomic state replacement."""
    target = Path(str(Path(path).resolve()) + '.lock')
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('a+b') as handle:
        deadline = time.monotonic() + 5
        while True:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB); break
            except BlockingIOError:
                if time.monotonic() >= deadline: raise ValueError('checkpoint state busy; retry')
                time.sleep(.05)
        try: yield
        finally: fcntl.flock(handle, fcntl.LOCK_UN)


def init(manifest_path, request_path, cache_path, state_path, target='html',
         interpretation_roles=('positioning', 'swot'), full=False, with_plan=False):
    manifest = CHECK.read(manifest_path); identity = CACHE.identity(manifest)
    selected = manifest.get('selected_roles')
    require(isinstance(selected, list) and selected and len(set(selected)) == len(selected)
            and set(selected) <= set(ROLES), 'valid selected_roles required')
    require(CHECK.text(manifest.get('scope')) and Path(request_path).read_text().strip(), 'scope/original request required')
    require(target in {'facts', 'interpretation', 'html'}, 'invalid checkpoint target')
    require(interpretation_roles and len(set(interpretation_roles)) == len(interpretation_roles)
            and set(interpretation_roles) <= {'positioning', 'swot'}, 'invalid interpretation roles')
    require(not full or target == 'html' and set(selected) == set(ROLES)
            and set(interpretation_roles) == {'positioning', 'swot'}, 'full briefing requires all roles')
    roots = [Path(p).resolve() for p in (manifest_path, request_path)]
    require(Path(state_path).resolve() not in roots, 'state may not overwrite inputs')
    require(not Path(state_path).exists(), 'state exists; resume explicitly instead of resetting it')
    CACHE.Cache(cache_path, manifest)
    stages = [r for r in ROLES if r in selected]
    if full or with_plan or manifest.get('comparison_plan_path'): stages.insert(stages.index('market') if 'market' in stages else len(stages), 'plan')
    focus = FACTS.focus_requests(manifest)
    stages += ['focus:' + r['id'] for r in focus]
    stages += ['facts', 'basis-review']
    if target != 'facts': stages += [r for r in ('positioning', 'swot') if r in interpretation_roles] + ['final-review']
    if target == 'html': stages += ['html']
    state = seal(dict(schema_version=1, format='run-checkpoints-v1', **identity,
                      manifest=record(manifest_path), request=record(request_path),
                      cache_path=str(Path(cache_path).resolve()), target=target, full=full,
                      stages=stages, checkpoints={}, created_at=CACHE.now(),
                      notice='Local completion records only; content approval and visual QA remain separate.'))
    CACHE.write_json(state_path, state)
    return state


def load(state_path):
    state = verified(CHECK.read(state_path))
    require(state.get('schema_version') == 1 and state.get('format') == 'run-checkpoints-v1', 'run-checkpoints-v1 required')
    for key in ('manifest', 'request'):
        require(sha(state[key]['path']) == state[key]['sha256'],
                'original task/manifest changed; use a new run (including company, scope and as_of)')
    manifest = CHECK.read(state['manifest']['path'])
    require(CACHE.identity(manifest) == {k: state[k] for k in ('run_id', 'company', 'as_of')}, 'run identity mismatch')
    cache_root = Path(state['cache_path'])
    require((cache_root/'identity.json').is_file(), 'source cache missing; do not recreate it as proof')
    require(CHECK.read(cache_root/'identity.json') == CACHE.identity(manifest), 'source cache identity mismatch')
    return state, manifest, CACHE.Cache(cache_root, manifest)


def code_files(stage):
    """Separate presentation changes from research; bind actual policies and validators."""
    files = [ROOT/'CLAUDE.md', ROOT/'scripts/resume-run.py', ROOT/'scripts/source-cache.py']
    files += [p for p in (ROOT/'references').glob('*.md') if not p.name.endswith('-abnahme.md')]
    if stage.startswith('focus:'):
        files += [ROOT/'.claude/agents/focus-analyst.md', ROOT/'scripts/focus-html.py', ROOT/'scripts/prepare-facts.py']
    if stage in AGENTS:
        files += [ROOT/'.claude/agents'/(AGENTS[stage]+'.md')]
    if stage in ROLES or stage in {'facts', 'plan'}:
        files += [ROOT/'scripts/prepare-facts.py', ROOT/'scripts/check-review-data.py',
                  ROOT/'.claude/skills/facts-briefing/SKILL.md']
    elif stage in {'basis-review', 'final-review'}:
        files += [ROOT/'.claude/agents/source-reviewer.md', ROOT/'scripts/review-work.py', ROOT/'scripts/stamp-review.py']
        files += list((ROOT/'scripts').glob('*.py'))
    else:
        files += list((ROOT/'scripts').glob('*.py'))
        files += [ROOT/'.claude/skills/interpretation-briefing/SKILL.md']
    if stage == 'html':
        files += list((ROOT/'references/templates').glob('*'))
        files += [ROOT/'.claude/skills/briefing-output/SKILL.md']
    return {str(p.relative_to(ROOT)): sha(p) for p in sorted(set(files)) if p.is_file()}


def paths(records):
    return {name: row['path'] for name, row in records.items()}


def expected_link(state, supplied, name, stage, output):
    require(stage in state['checkpoints'], 'missing dependency checkpoint: '+stage)
    expected = state['checkpoints'][stage]['outputs'][output]['path']
    require(name in supplied and str(Path(supplied[name]).resolve()) == expected,
            name+' must use the checkpoint output of '+stage)
    return stage


def dependencies(state, stage, inputs):
    deps = set()
    def link(name, parent, output): deps.add(expected_link(state, inputs, name, parent, output))
    if stage in ROLES or stage.startswith('focus:'):
        if stage == 'market' and 'plan' in state['stages']: link('plan', 'plan', 'plan')
    elif stage == 'facts':
        for role in ROLES:
            if role in state['stages']: link(role, role, 'module')
        for focus_stage in state['stages']:
            if focus_stage.startswith('focus:'): link(focus_stage, focus_stage, 'module')
        if 'plan' in state['stages']: link('plan', 'plan', 'plan')
    elif stage != 'plan':
        link('facts', 'facts', 'facts')
        if stage == 'basis-review': link('validation', 'facts', 'validation')
        else: link('basis-review', 'basis-review', 'review')
        if 'plan' in state['stages']: link('plan', 'plan', 'plan')
        if stage == 'swot' and 'positioning' in state['stages']:
            link('positioning', 'positioning', 'output'); link('positioning-context', 'positioning', 'context')
        if stage in {'final-review', 'html'}:
            for role in ('positioning', 'swot'):
                if role in state['stages']:
                    link(role, role, 'output'); link(role+'-context', role, 'context')
        if stage == 'html': link('final-review', 'final-review', 'review')
    # Explicit extra inputs bind ordering when they reference an existing stage output.
    prior = state['checkpoints'].get(stage)
    prior_paths = {r['path'] for r in prior.get('inputs', {}).values()} if prior else set()
    for parent, checkpoint in state['checkpoints'].items():
        matches = set(inputs.values()) & {r['path'] for r in checkpoint['outputs'].values()}
        if parent != stage and matches:
            # Inputs captured before their producer was checkpointed retain their file binding.
            # Do not retroactively add an ordering edge and create a cycle on revalidation.
            if prior and parent not in prior['dependencies'] and matches <= prior_paths: continue
            deps.add(parent)
    return deps


def checked_report(report):
    require(report.get('errors') == [], '; '.join(report.get('errors', [])) or 'successful formal validation required')
    return report


def validate_stage(state, manifest, cache, stage, inputs, outputs):
    """Invoke existing gates, retaining contexts, full data and explicit reviewer decisions."""
    def read(name, output=False):
        source = outputs if output else inputs
        require(name in source, 'missing '+('output: ' if output else 'input: ')+name)
        return CHECK.read(source[name])
    plan = read('plan') if 'plan' in inputs else None
    source_ids = set()
    if stage in ROLES or stage.startswith('focus:'):
        require(set(outputs) == {'module'}, 'fact role output must be module')
        module = read('module', True)
        require(FACTS.module_key(module) == stage and module.get('status') in {'vollständig', 'teilweise'}, 'wrong/blocked fact role')
        # Referenced sibling modules must be explicit inputs; never ignore dangling IDs.
        modules = [module]
        for role in ROLES:
            if role in inputs:
                require(role != stage and read(role).get('role') == role, 'wrong sibling module input')
                modules.append(read(role))
        partial_manifest = {**manifest, 'selected_roles': [m['role'] for m in modules if m['role'] != 'focus']}
        if 'focus_pages' in manifest:
            partial_manifest['focus_pages'] = [r for r in manifest['focus_pages'] if stage == 'focus:' + r['id']]
        if 'market' not in partial_manifest['selected_roles']: partial_manifest.pop('comparison_plan_path', None)
        report, packet = FACTS.build(partial_manifest, modules, plan)
        checked_report(report)
        require(WORK.refs(module) <= {c['id'] for c in packet['claims']},
                'module view references unknown claims; supply referenced sibling modules')
        source_ids = {s['id'] for s in packet['sources']}
    elif stage == 'plan':
        require(set(outputs) == {'plan'}, 'plan output required')
        require(not FACTS.validate_plan(read('plan', True), manifest), 'invalid comparison plan')
    elif stage == 'facts':
        require(set(outputs) == {'facts', 'validation'}, 'facts/validation outputs required')
        report, packet = FACTS.build(manifest, [read(r) for r in ROLES if r in manifest['selected_roles']] + [read(s) for s in state['stages'] if s.startswith('focus:')], plan)
        checked_report(report)
        require(read('facts', True) == packet and read('validation', True) == report, 'packet/validation differs from current modules')
        source_ids = {s['id'] for s in packet['sources']}
    elif stage in {'basis-review', 'final-review'}:
        require(set(outputs) == {'review'}, 'review output required')
        facts, validation, work = read('facts'), read('validation'), read('work')
        phase = 'basis' if stage == 'basis-review' else 'final'
        checked_report(validation); WORK.same_identity(work, manifest, phase); WORK.verify_current(work)
        require(work.get('cache_path') == str(cache.root), 'review must bind the same run cache')
        rows = []
        if phase == 'final':
            reports = []
            for role in ('positioning', 'swot'):
                if role not in state['stages']: continue
                output, context = read(role), read(role+'-context'); rows += output['interpretations']
                reports.append(checked_report(CHECK.validate_output(manifest, facts, read('basis-review'), context, output,
                    read('positioning') if role == 'swot' and 'positioning' in inputs else None,
                    read('positioning-context') if role == 'swot' and 'positioning-context' in inputs else None, plan)))
            require(validation == CHECK.merge_reports(reports), 'final validation differs from current interpretations')
        current = WORK.prepare(manifest, facts, validation, rows, cache,
                               read('basis-review') if phase == 'final' else None,
                               read('basis-work') if phase == 'final' else None)
        for key in ('items', 'fact_states', 'source_snapshots', 'required_full_review_ids', 'packet_fingerprint'):
            require(work.get(key) == current[key], 'review work differs from current data: '+key)
        result = STAMP.stamp(read('draft'), validation, work)
        require(result.get('status') == 'freigegeben' and result.get('material_errors') == [], 'review not released')
        require(read('review', True) == result, 'review differs from explicit draft/work; no inherited approval')
        source_ids = set(work['source_snapshots'])
    elif stage in {'positioning', 'swot'}:
        require(set(outputs) == {'output', 'context', 'validation'}, 'interpretation output/context/validation required')
        output, context = read('output', True), read('context', True)
        require(output.get('role') == stage and output.get('status') in {'vollständig', 'teilweise'}, 'wrong/blocked interpretation role')
        require(not any(r.get('blocking') for r in output.get('research_requests', [])), 'blocking research question')
        report = checked_report(CHECK.validate_output(manifest, read('facts'), read('basis-review'), context, output,
            read('positioning') if stage == 'swot' and 'positioning' in inputs else None,
            read('positioning-context') if stage == 'swot' and 'positioning-context' in inputs else None, plan))
        require(read('validation', True) == report, 'interpretation validation differs from current output/context')
        source_ids = {s['id'] for s in read('facts')['sources']}
    elif stage == 'html':
        require(set(outputs) == {'html'}, 'HTML output required')
        body = RENDER.build(manifest, read('facts'), read('basis-review'),
            read('positioning') if 'positioning' in inputs else None, read('positioning-context') if 'positioning-context' in inputs else None,
            read('swot') if 'swot' in inputs else None, read('swot-context') if 'swot-context' in inputs else None,
            read('final-review'), plan, state['full'])
        require(Path(outputs['html']).read_bytes() == body.encode(), 'HTML differs from current released inputs/template')
        source_ids = {s['id'] for s in read('facts')['sources']}
    else: raise ValueError('unknown checkpoint stage')
    snapshots = {sid: WORK.snapshot(cache, sid) for sid in sorted(source_ids)}
    require(all(v is not None for v in snapshots.values()), 'complete originals missing; no reusable checkpoint')
    return snapshots


def fresh_sources(cache, sources, now=None):
    now = now or datetime.now(timezone.utc)
    stale = []
    for sid in sources:
        require(not (cache._directory(sid)/'revalidation.json').exists(),
                'source refresh incomplete/failed; retry actual refresh/reopen: '+sid)
        checked = datetime.fromisoformat(cache.load(sid)['checked_at'])
        require(checked.tzinfo is not None and checked <= now + timedelta(minutes=1), 'invalid source check time')
        if now - checked > MAX_SOURCE_AGE: stale.append(sid)
    require(not stale, 'source refresh/reopen required (older than 24h): '+', '.join(stale))


def inspect(state, manifest, cache):
    results = {}
    visiting = set()
    def check(stage):
        if stage in results: return results[stage]
        require(stage not in visiting, 'checkpoint dependency cycle')
        visiting.add(stage)
        cp = state['checkpoints'].get(stage)
        status, reasons = 'pending', []
        if cp:
            status = 'reusable'
            try:
                verified(cp)
                require(not cp.get('invalidated'), cp.get('invalidated', 'checkpoint invalidated'))
                for parent, fp in cp['dependencies'].items():
                    require(parent in state['stages'], 'unknown dependency')
                    require(check(parent)['status'] == 'reusable', 'dependency requires work: '+parent)
                    require(state['checkpoints'][parent]['fingerprint'] == fp, 'dependency checkpoint changed: '+parent)
                require(cp['code'] == code_files(stage), 'validator/policy/template changed; revalidate stage')
                for row in [*cp['inputs'].values(), *cp['outputs'].values()]:
                    require(sha(row['path']) == row['sha256'], 'file missing/changed: '+row['path'])
                current = validate_stage(state, manifest, cache, stage, paths(cp['inputs']), paths(cp['outputs']))
                require(current == cp['sources'], 'original source snapshot changed; recheck affected data')
                fresh_sources(cache, current)
            except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
                status, reasons = 'invalid', [str(exc)]
        visiting.remove(stage)
        results[stage] = dict(status=status, reasons=reasons)
        return results[stage]
    for stage in state['stages']: check(stage)
    next_stage = next((s for s in state['stages'] if results[s]['status'] != 'reusable'), None)
    return dict(run_id=state['run_id'], company=state['company'], as_of=state['as_of'],
                stages={s: results[s] for s in state['stages']}, next_stage=next_stage,
                ready_for_visual_qa=next_stage is None and state['target'] == 'html',
                notice='Reuse only reusable stages. Existing files are not completion proof. Visual QA/acceptance remains mandatory.')


def checkpoint(state_path, stage, inputs, outputs, extra_dependencies=()):
    state, manifest, cache = load(state_path)
    require(stage in state['stages'], 'stage not selected for this run')
    inputs = {k: str(Path(v).resolve()) for k, v in inputs.items()}
    outputs = {k: str(Path(v).resolve()) for k, v in outputs.items()}
    require(len(set(outputs.values())) == len(outputs), 'duplicate output paths')
    protected = {str(Path(state_path).resolve()), state['manifest']['path'], state['request']['path']}
    require(not set(inputs.values()) & {str(Path(state_path).resolve())}, 'state cannot be a stage input')
    require(not set(outputs.values()) & (set(inputs.values()) | protected), 'outputs may not overwrite inputs/state')
    deps = dependencies(state, stage, inputs) | set(extra_dependencies)
    require(stage not in deps and deps <= set(state['stages']), 'invalid/self dependency')
    def ancestors(parent, seen=None):
        seen = set() if seen is None else seen
        require(parent not in seen, 'checkpoint dependency cycle')
        children = state['checkpoints'].get(parent, {}).get('dependencies', {})
        return set(children) | {a for child in children for a in ancestors(child, seen | {parent})}
    require(not any(stage in ancestors(parent) for parent in deps), 'checkpoint dependency cycle')
    prior = inspect(state, manifest, cache)
    require(all(prior['stages'][p]['status'] == 'reusable' for p in deps), 'dependencies not reusable: '+', '.join(sorted(deps)))
    # No two roles/stages may claim the same output file.
    other_outputs = {r['path'] for s, cp in state['checkpoints'].items() if s != stage for r in cp['outputs'].values()}
    require(not set(outputs.values()) & other_outputs, 'output belongs to another checkpoint stage')
    before = dict(inputs={k: record(v) for k, v in inputs.items()}, outputs={k: record(v) for k, v in outputs.items()})
    code = code_files(stage)
    sources = validate_stage(state, manifest, cache, stage, inputs, outputs); fresh_sources(cache, sources)
    after = dict(inputs={k: record(v) for k, v in inputs.items()}, outputs={k: record(v) for k, v in outputs.items()})
    require(before == after and code == code_files(stage), 'files/code changed while checking; retry')
    require(sources == {sid: WORK.snapshot(cache, sid) for sid in sources}, 'sources changed while checking; retry')
    require(sha(state['manifest']['path']) == state['manifest']['sha256'] and sha(state['request']['path']) == state['request']['sha256'], 'task changed while checking')
    latest = inspect(state, manifest, cache)
    require(all(latest['stages'][p]['status'] == 'reusable' for p in deps), 'dependencies changed while checking; retry')
    cp = seal(dict(stage=stage, checkpoint_id=uuid.uuid4().hex, **before, code=code, sources=sources,
                   dependencies={p: state['checkpoints'][p]['fingerprint'] for p in sorted(deps)}, checked_at=CACHE.now()))
    state['checkpoints'][stage] = cp
    CACHE.write_json(state_path, seal(state))
    return dict(stage=stage, checkpoint=cp['fingerprint'], notice='Validated checkpoint saved; no content decision generated.')


def named_paths(rows):
    result = {}
    for row in rows:
        name, separator, path = row.partition('=')
        require(separator and name and path and name not in result, 'use unique name=path arguments')
        result[name] = path
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', required=True)
    sub = parser.add_subparsers(dest='command', required=True)
    create = sub.add_parser('init')
    for key in ('manifest', 'request', 'cache'): create.add_argument('--'+key, required=True)
    create.add_argument('--target', choices=['facts', 'interpretation', 'html'], default='html')
    create.add_argument('--interpretation-roles', nargs='+', choices=['positioning', 'swot'], default=['positioning', 'swot'])
    create.add_argument('--full', action='store_true'); create.add_argument('--with-plan', action='store_true')
    sub.add_parser('resume')
    save = sub.add_parser('checkpoint'); save.add_argument('--stage', required=True)
    save.add_argument('--input', nargs='*', default=[]); save.add_argument('--output', nargs='+', required=True)
    save.add_argument('--depends-on', nargs='*', default=[])
    invalidate = sub.add_parser('invalidate'); invalidate.add_argument('--stage', required=True); invalidate.add_argument('--reason', required=True)
    args = parser.parse_args()
    try:
        with state_lock(args.state):
            if args.command == 'init':
                state = init(args.manifest, args.request, args.cache, args.state, args.target, args.interpretation_roles, args.full, args.with_plan)
                result = dict(state=str(Path(args.state).resolve()), stages=state['stages'])
            elif args.command == 'checkpoint':
                result = checkpoint(args.state, args.stage, named_paths(args.input), named_paths(args.output), args.depends_on)
            else:
                state, manifest, cache = load(args.state)
                if args.command == 'invalidate':
                    require(args.stage in state['checkpoints'] and args.reason.strip(), 'existing checkpoint and reason required')
                    state['checkpoints'][args.stage] = seal({**state['checkpoints'][args.stage], 'invalidated': args.reason})
                    CACHE.write_json(args.state, seal(state))
                result = inspect(state, manifest, cache)
        print(json.dumps(result, ensure_ascii=False, indent=2)); return 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        print(json.dumps({'errors': [str(exc)], 'notice': 'No checkpoint reuse permitted after this error.'}, ensure_ascii=False)); return 1


if __name__ == '__main__':
    sys.exit(main())
