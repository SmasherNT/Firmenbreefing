import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest import mock
from datetime import datetime, timedelta, timezone

import test_review_work as fixtures

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('resume_tests', ROOT/'scripts/resume-run.py')
RESUME = importlib.util.module_from_spec(spec); spec.loader.exec_module(RESUME)


class ResumeRunTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ReviewWorkTests(); self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.cache = self.fixture.root, self.fixture.cache
        self.state = self.root/'checkpoints.json'
        self.manifest = self.put('manifest', self.fixture.manifest)
        self.request = self.root/'auftrag.md'; self.request.write_text('Fictional Work: offline synthetic test')
        self.module = self.put('portfolio', self.fixture.module)
        self.facts = self.put('facts', self.fixture.facts)
        self.validation = self.put('validation', self.fixture.report)
        self.work = self.put('work', self.fixture.work)
        self.draft = self.put('draft', self.fixture.draft())
        self.review = self.put('review', self.fixture.base())
        RESUME.init(self.manifest, self.request, self.cache.root, self.state)

    def put(self, name, obj):
        path = self.root/(name+'.json'); RESUME.CACHE.write_json(path, obj); return path

    def status(self):
        return RESUME.inspect(*RESUME.load(self.state))

    def save(self, stage, inputs, outputs, deps=()):
        return RESUME.checkpoint(self.state, stage, inputs, outputs, deps)

    def basis(self):
        self.save('portfolio', {}, {'module': self.module})
        self.save('facts', {'portfolio': self.module}, {'facts': self.facts, 'validation': self.validation})
        self.save('basis-review', {'facts': self.facts, 'validation': self.validation, 'work': self.work, 'draft': self.draft}, {'review': self.review})

    def final(self):
        self.basis()
        basis, pc, po, sc, so, report, rows, work = self.fixture.final()
        self.pc = self.put('pc', pc); self.po = self.put('po', po)
        self.sc = self.put('sc', sc); self.so = self.put('so', so)
        pr = fixtures.WORK.CHECK.validate_output(self.fixture.manifest, self.fixture.facts, basis, pc, po)
        sr = fixtures.WORK.CHECK.validate_output(self.fixture.manifest, self.fixture.facts, basis, sc, so,
                                                latest_positioning=po, latest_positioning_context=pc)
        self.pv = self.put('pv', pr); self.sv = self.put('sv', sr)
        self.save('positioning', {'facts': self.facts, 'basis-review': self.review},
                  {'output': self.po, 'context': self.pc, 'validation': self.pv})
        self.save('swot', {'facts': self.facts, 'basis-review': self.review, 'positioning': self.po, 'positioning-context': self.pc},
                  {'output': self.so, 'context': self.sc, 'validation': self.sv})
        self.fv = self.put('fv', report); self.fw = self.put('fw', work)
        draft = self.fixture.draft(work); draft['reuse_fact_ids'] = ['P1', 'P2']
        self.fd = self.put('fd', draft); self.fr = self.put('fr', fixtures.STAMP.stamp(draft, report, work))
        inputs = {'facts': self.facts, 'basis-review': self.review, 'basis-work': self.work,
                  'validation': self.fv, 'work': self.fw, 'draft': self.fd,
                  'positioning': self.po, 'positioning-context': self.pc, 'swot': self.so, 'swot-context': self.sc}
        self.save('final-review', inputs, {'review': self.fr})
        return inputs

    def test_interruption_keeps_finished_role_and_existing_files_are_not_checkpoints(self):
        self.assertEqual(self.status()['next_stage'], 'portfolio')
        self.save('portfolio', {}, {'module': self.module})
        state = self.status()
        self.assertEqual(state['next_stage'], 'facts')
        self.assertEqual(state['stages']['portfolio']['status'], 'reusable')
        self.assertEqual(state['stages']['basis-review']['status'], 'pending')
        self.assertFalse(state['ready_for_visual_qa'])

    def test_existing_state_cannot_be_reset_or_overwrite_request(self):
        with self.assertRaisesRegex(ValueError, 'state exists'):
            RESUME.init(self.manifest, self.request, self.cache.root, self.state)
        with self.assertRaisesRegex(ValueError, 'overwrite inputs'):
            RESUME.init(self.manifest, self.request, self.cache.root, self.request)

    def test_changed_company_date_scope_topics_or_original_request_reject_entire_reuse(self):
        original = self.manifest.read_bytes()
        for key, value in [('company', 'Other'), ('as_of', '2026-10-14'), ('scope', 'Different task'),
                           ('topics', [{'id': 'new', 'label': 'New'}]), ('run_id', 'other')]:
            with self.subTest(key=key):
                self.put('manifest', {**self.fixture.manifest, key: value})
                with self.assertRaisesRegex(ValueError, 'task/manifest changed'): self.status()
                self.manifest.write_bytes(original)
        self.request.write_text('Different company research')
        with self.assertRaisesRegex(ValueError, 'task/manifest changed'): self.status()

    def test_partial_blocked_or_wrong_role_outputs_cannot_be_completed(self):
        for change in ({'status': 'blockiert'}, {'role': 'cluster'}, {'claims': []}, {'mode': 'interpret-v2'}):
            path = self.put('bad', {**self.fixture.module, **change})
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.save('portfolio', {}, {'module': path})
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'pending')

    def test_fact_edit_invalidates_dependent_reviews_but_keeps_earlier_completed_stages(self):
        self.basis()
        data = json.loads(self.facts.read_text()); data['claims'][0]['statement'] += ' changed'
        self.put('facts', data)
        state = self.status()
        self.assertEqual(state['stages']['portfolio']['status'], 'reusable')
        self.assertEqual(state['stages']['facts']['status'], 'invalid')
        self.assertEqual(state['stages']['basis-review']['status'], 'invalid')
        self.assertEqual(state['next_stage'], 'facts')

    def test_original_change_and_corruption_invalidate_even_unchanged_claim_files(self):
        self.basis(); self.fixture.store(self.fixture.sources[0], 'Changed original source')
        state = self.status()
        self.assertTrue(all(state['stages'][s]['status'] == 'invalid' for s in ('portfolio', 'facts', 'basis-review')))
        raw = Path(self.cache.load(self.fixture.sources[0]['id'])['original_path']); raw.write_bytes(b'corrupt')
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'invalid')

    def test_missing_original_or_cache_identity_is_never_proof(self):
        self.save('portfolio', {}, {'module': self.module})
        raw = Path(self.cache.load(self.fixture.sources[0]['id'])['original_path']); raw.unlink()
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'invalid')
        (self.cache.root/'identity.json').unlink()
        with self.assertRaisesRegex(ValueError, 'cache missing'): self.status()
        self.assertFalse((self.cache.root/'identity.json').exists())

    def test_stale_originals_require_refresh_and_identical_refreshed_content_keeps_reviews(self):
        self.basis()
        for source in self.fixture.sources:
            path = self.cache._directory(source['id'])/'current.json'; data = json.loads(path.read_text())
            data['checked_at'] = (datetime.now(timezone.utc)-timedelta(hours=25)).isoformat()
            RESUME.CACHE.write_json(path, data)
        self.assertIn('refresh/reopen', self.status()['stages']['portfolio']['reasons'][0])
        for source in self.fixture.sources: self.fixture.store(source, 'Fictional full source')
        self.assertTrue(all(self.status()['stages'][s]['status'] == 'reusable' for s in ('portfolio', 'facts', 'basis-review')))

    def test_failed_refresh_blocks_old_fresh_snapshot_until_actual_success(self):
        self.basis()
        source = self.fixture.sources[0]
        with mock.patch.object(fixtures.WORK.CACHE, 'urlopen', side_effect=OSError('Network unavailable')):
            with self.assertRaises(OSError): self.cache.fetch(source['url'], refresh=True)
        state = self.status()
        self.assertIn('refresh incomplete/failed', state['stages']['portfolio']['reasons'][0])
        self.cache.fetch(source['url'])  # cache hit must not erase a failed refresh
        self.assertEqual(self.status()['stages']['basis-review']['status'], 'invalid')
        self.fixture.store(source, 'Fictional full source')  # simulated reopened complete original
        self.assertEqual(self.status()['stages']['basis-review']['status'], 'reusable')

    def test_file_deletion_or_partial_json_marks_role_invalid(self):
        self.save('portfolio', {}, {'module': self.module}); self.module.write_text('{"claims":')
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'invalid')
        self.module.unlink()
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'invalid')

    def test_state_corruption_fails_closed(self):
        data = json.loads(self.state.read_text()); data['checkpoints']['portfolio'] = {'status': 'complete'}
        RESUME.CACHE.write_json(self.state, data)
        with self.assertRaisesRegex(ValueError, 'state corrupt'): self.status()
        self.state.write_text('{"checkpoints":')
        with self.assertRaises(ValueError): self.status()

    def test_bound_explicit_review_cannot_be_inferred_or_relabelled(self):
        self.basis()
        data = json.loads(self.review.read_text()); data['claims'][0]['status'] = 'übernommen'
        self.put('review', data)
        self.assertEqual(self.status()['stages']['basis-review']['status'], 'invalid')
        with self.assertRaisesRegex(ValueError, 'explicit draft/work'):
            self.save('basis-review', {'facts': self.facts, 'validation': self.validation, 'work': self.work, 'draft': self.draft}, {'review': self.review})

    def test_new_checkpoint_requires_dependent_stage_confirmation_even_if_bytes_identical(self):
        self.basis()
        before = json.loads(self.state.read_text())['checkpoints']['portfolio']['fingerprint']
        self.save('portfolio', {}, {'module': self.module})
        after = json.loads(self.state.read_text())['checkpoints']['portfolio']['fingerprint']
        self.assertNotEqual(before, after)
        self.assertEqual(self.status()['stages']['facts']['status'], 'invalid')
        self.assertEqual(self.status()['stages']['basis-review']['status'], 'invalid')

    def test_dependency_cycle_and_wrong_role_checkpoint_link_rejected(self):
        self.basis()
        with self.assertRaisesRegex(ValueError, 'cycle'):
            self.save('portfolio', {}, {'module': self.module}, ['facts'])
        duplicate = self.put('duplicate', self.fixture.module)
        with self.assertRaisesRegex(ValueError, 'checkpoint output'):
            self.save('facts', {'portfolio': duplicate}, {'facts': self.facts, 'validation': self.validation})

    def test_additional_input_change_invalidates_stage(self):
        extra = self.root/'delegation.md'; extra.write_text('Original relevant input')
        self.save('portfolio', {'delegation': extra}, {'module': self.module})
        extra.write_text('Changed input')
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'invalid')

    def test_atomic_write_failure_preserves_previous_valid_state(self):
        original = self.state.read_bytes()
        with mock.patch.object(RESUME.CACHE.os, 'replace', side_effect=OSError('Interrupted write')):
            with self.assertRaises(OSError): self.save('portfolio', {}, {'module': self.module})
        self.assertEqual(self.state.read_bytes(), original)
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'pending')

    def test_terminated_lock_owner_does_not_block_resume(self):
        code = "import importlib.util,sys,time; s=importlib.util.spec_from_file_location('r',sys.argv[1]); r=importlib.util.module_from_spec(s); s.loader.exec_module(r)\nwith r.state_lock(sys.argv[2]):\n print('locked',flush=True)\n time.sleep(30)"
        process = subprocess.Popen([sys.executable, '-c', code, str(ROOT/'scripts/resume-run.py'), str(self.state)], stdout=subprocess.PIPE, text=True)
        self.addCleanup(lambda: process.kill() if process.poll() is None else None)
        self.assertEqual(process.stdout.readline().strip(), 'locked')
        process.kill(); process.wait(); process.stdout.close()
        result = subprocess.run([sys.executable, str(ROOT/'scripts/resume-run.py'), '--state', str(self.state), 'resume'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_final_reviews_and_full_contexts_survive_interruption_without_regeneration(self):
        self.final()
        before = {p: p.read_bytes() for p in (self.pc, self.po, self.sc, self.so, self.review, self.fr)}
        state = self.status()
        self.assertTrue(all(state['stages'][s]['status'] == 'reusable' for s in ('portfolio', 'facts', 'basis-review', 'positioning', 'swot', 'final-review')))
        self.assertEqual(state['next_stage'], 'html')
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_changed_context_or_final_review_blocks_downstream_completion(self):
        self.final(); self.pc.write_text(self.pc.read_text()+'\n')
        state = self.status()
        self.assertEqual(state['stages']['basis-review']['status'], 'reusable')
        self.assertTrue(all(state['stages'][s]['status'] == 'invalid' for s in ('positioning', 'swot', 'final-review')))

    def test_rendered_html_is_reused_byte_identically_but_still_requires_visual_qa(self):
        inputs = self.final()
        body = RESUME.RENDER.build(self.fixture.manifest, self.fixture.facts, self.fixture.base(),
                                  RESUME.CHECK.read(self.po), RESUME.CHECK.read(self.pc),
                                  RESUME.CHECK.read(self.so), RESUME.CHECK.read(self.sc), RESUME.CHECK.read(self.fr))
        html = self.root/'briefing.html'; html.write_bytes(body.encode())
        inputs = {k: v for k, v in inputs.items() if k not in {'work', 'draft', 'validation', 'basis-work'}}
        inputs['final-review'] = self.fr
        self.save('html', inputs, {'html': html})
        original = html.read_bytes(); state = self.status()
        self.assertIsNone(state['next_stage']); self.assertTrue(state['ready_for_visual_qa'])
        self.assertEqual(html.read_bytes(), original)
        html.write_bytes(original+b'<!-- stale edit -->')
        self.assertEqual(self.status()['stages']['html']['status'], 'invalid')
        with self.assertRaisesRegex(ValueError, 'HTML differs'):
            self.save('html', inputs, {'html': html})

    def test_output_mutation_during_check_cannot_create_checkpoint(self):
        real = RESUME.validate_stage
        def mutating(*args):
            result = real(*args)
            self.module.write_text(self.module.read_text()+'\n')
            return result
        with mock.patch.object(RESUME, 'validate_stage', side_effect=mutating):
            with self.assertRaisesRegex(ValueError, 'changed while checking'):
                self.save('portfolio', {}, {'module': self.module})
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'pending')

    def test_fact_phase_target_and_required_comparison_plan_are_preserved(self):
        other = self.root/'fact-state.json'
        state = RESUME.init(self.manifest, self.request, self.cache.root, other, target='facts', with_plan=True)
        self.assertEqual(state['stages'], ['portfolio', 'plan', 'facts', 'basis-review'])
        self.assertNotIn('positioning', state['stages'])
        RESUME.checkpoint(other, 'portfolio', {}, {'module': self.module})
        with self.assertRaisesRegex(ValueError, 'dependency checkpoint: plan'):
            RESUME.checkpoint(other, 'facts', {'portfolio': self.module}, {'facts': self.facts, 'validation': self.validation})

    def test_full_briefing_requires_plan_before_market_without_optional_flag(self):
        manifest = {**self.fixture.manifest, 'selected_roles': list(RESUME.ROLES)}
        mp = self.put('full-manifest', manifest); other = self.root/'full-state.json'
        state = RESUME.init(mp, self.request, self.cache.root, other, full=True)
        self.assertIn('plan', state['stages'])
        self.assertLess(state['stages'].index('plan'), state['stages'].index('market'))

    def test_revalidation_preserves_earlier_file_bindings_without_retroactive_cycle(self):
        manifest = {**self.fixture.manifest, 'selected_roles': ['context', 'portfolio']}
        mp = self.put('cross-manifest', manifest); other = self.root/'cross-state.json'
        context = {**self.fixture.module, 'role': 'context', 'products': [], 'claims': [
            {**self.fixture.claims[2], 'id': 'T1', 'source_ids': [self.fixture.sources[1]['id']]}],
            'source_proposals': [self.fixture.sources[1]],
            'company_facts': [{'label': 'Existing product fact', 'claim_ids': ['P1']}]}
        cp = self.put('cross-context', context)
        RESUME.init(mp, self.request, self.cache.root, other)
        RESUME.checkpoint(other, 'context', {'portfolio': self.module}, {'module': cp})
        RESUME.checkpoint(other, 'portfolio', {'context': cp}, {'module': self.module})
        RESUME.checkpoint(other, 'context', {'portfolio': self.module}, {'module': cp})
        state, _, _ = RESUME.load(other)
        self.assertEqual(state['checkpoints']['context']['dependencies'], {})
        status = RESUME.inspect(*RESUME.load(other))
        self.assertEqual(status['stages']['context']['status'], 'reusable')
        self.assertEqual(status['stages']['portfolio']['status'], 'invalid')
        RESUME.checkpoint(other, 'portfolio', {'context': cp}, {'module': self.module})
        self.module.write_text(self.module.read_text()+'\n')
        self.assertEqual(RESUME.inspect(*RESUME.load(other))['stages']['context']['status'], 'invalid')

    def test_independent_roles_survive_failure_in_another_branch(self):
        manifest = {**self.fixture.manifest, 'selected_roles': ['context', 'portfolio']}
        mp = self.put('parallel-manifest', manifest); other = self.root/'parallel-state.json'
        context = {**self.fixture.module, 'role': 'context', 'products': [], 'claims': [
            {**self.fixture.claims[2], 'id': 'T1', 'source_ids': [self.fixture.sources[1]['id']]}],
            'source_proposals': [self.fixture.sources[1]]}
        cp = self.put('context', context)
        RESUME.init(mp, self.request, self.cache.root, other)
        RESUME.checkpoint(other, 'context', {}, {'module': cp})
        RESUME.checkpoint(other, 'portfolio', {}, {'module': self.module})
        self.module.write_text(self.module.read_text()+'\n')
        state = RESUME.inspect(*RESUME.load(other))
        self.assertEqual(state['stages']['context']['status'], 'reusable')
        self.assertEqual(state['stages']['portfolio']['status'], 'invalid')

    def test_review_requires_original_binding_and_released_decisions(self):
        self.save('portfolio', {}, {'module': self.module})
        self.save('facts', {'portfolio': self.module}, {'facts': self.facts, 'validation': self.validation})
        data = json.loads(self.draft.read_text()); data['status'] = 'blockiert'; self.put('draft', data)
        with self.assertRaisesRegex(ValueError, 'not released'):
            self.save('basis-review', {'facts': self.facts, 'validation': self.validation, 'work': self.work, 'draft': self.draft}, {'review': self.review})
        self.assertEqual(self.status()['stages']['basis-review']['status'], 'pending')

    def test_validator_changes_require_revalidation_and_manual_invalidation_propagates(self):
        self.basis()
        real = RESUME.code_files
        with mock.patch.object(RESUME, 'code_files', side_effect=lambda s: {**real(s), 'new-rule': 'changed'}):
            self.assertEqual(self.status()['stages']['portfolio']['status'], 'invalid')
        result = subprocess.run([sys.executable, str(ROOT/'scripts/resume-run.py'), '--state', str(self.state), 'invalidate',
                                 '--stage', 'portfolio', '--reason', 'New factual contradiction'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.status()['stages']['portfolio']['status'], 'invalid')
        self.assertEqual(self.status()['stages']['basis-review']['status'], 'invalid')


if __name__ == '__main__': unittest.main()
