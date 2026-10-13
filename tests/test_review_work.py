import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/file)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


WORK = load('review_work_test', 'review-work.py')
FACTS = load('review_work_facts', 'prepare-facts.py')
STAMP = load('review_work_stamp', 'stamp-review.py')


class ReviewWorkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = dict(schema_version=1, mode='facts-v2', run_id='work-test', company='Fictional Work',
                             as_of='2026-10-13', scope='Offline test', selected_roles=['portfolio'])
        self.sources = [dict(id=FACTS.source_id('https://example.org/'+str(n)), name='Fake', title='Fake '+str(n),
                            url='https://example.org/'+str(n), published_date='2026-09-01', accessed_date='2026-10-13',
                            source_kind='company', fictional=True) for n in (1, 2)]
        self.claims = [dict(id='P'+str(n), statement='Fictional statement '+str(n), kind='Herstellerangabe',
                           source_ids=[self.sources[0]['id']], evidence='Paraphrase: fictional evidence',
                           location='Section '+str(n), uncertainty='Synthetic test only') for n in (1, 2, 3)]
        self.claims[1]['source_ids'].append(self.sources[1]['id'])
        self.claims[1]['evidence_items'] = [dict(source_id=s['id'], text='Fictional evidence', mode='Paraphrase',
                                               location='Section 2') for s in self.sources]
        self.module = {**self.manifest, 'role': 'portfolio', 'status': 'vollständig', 'claims': self.claims,
                       'source_proposals': self.sources, 'gaps': [], 'coverage': [],
                       'products': [dict(id='sensor', label='Sensor', domain='Sensors', claim_ids=['P1', 'P2'])]}
        self.report, self.facts = FACTS.build(self.manifest, [self.module]); self.assertEqual(self.report['errors'], [])
        self.cache = WORK.CACHE.Cache(self.root/'cache', self.manifest)
        for s in self.sources:
            self.store(s, 'Fictional full source')
        self.work = WORK.prepare(self.manifest, self.facts, self.report, cache=self.cache)

    def store(self, source, body):
        path = self.root/'source.txt'; path.write_text(body)
        return self.cache.store(source['url'], path, 'text/plain', 'local-original', 'Synthetic complete source')

    def draft(self, work=None, ids=None):
        work = work or self.work
        return dict(schema_version=1, run_id=self.manifest['run_id'], company=self.manifest['company'],
                    as_of=self.manifest['as_of'], phase=work['phase'], status='freigegeben', material_errors=[],
                    review_scope='SIMULATED offline reviewer decisions, not real approval',
                    scope_and_mappings_checked=True,
                    review_work_fingerprint=work['fingerprint'],
                    review_groups=[dict(claim_ids=ids or list(work['items']), depth='A', status='geprüft', note='SIMULATED check')],
                    source_checks=[dict(source_id=s['id'], claim_ids=[c['id'] for c in self.claims if s['id'] in c['source_ids']],
                                        note='SIMULATED original reading') for s in self.sources] if work['phase'] == 'basis' else [])

    def base(self):
        return STAMP.stamp(self.draft(), self.report, self.work)

    def final(self, basis=None):
        basis = basis or self.base(); check = WORK.CHECK
        pc = check.prepare(self.manifest, self.facts, basis, ['P1', 'P2'])
        po = dict(schema_version=1, mode='interpret-v2', role='positioning', **WORK.CACHE.identity(self.manifest),
                  scope='Offline test', status='vollständig', input_fingerprint=pc['fingerprint'],
                  research_requests=[], shared_limitations=['Fictional'], interpretations=[
                      dict(id='I'+str(n), statement='Fictional interpretation', section='positioning', depends_on=['P'+str(n)],
                           reasoning='Test reasoning', method='Qualitative', uncertainty='Synthetic') for n in (1, 2)])
        pr = check.validate_output(self.manifest, self.facts, basis, pc, po); self.assertEqual(pr['errors'], [])
        sc = check.prepare(self.manifest, self.facts, basis, [], positioning=po, positioning_context=pc, interpretation_ids=['I1'])
        so = {**po, 'role': 'swot', 'input_fingerprint': sc['fingerprint'], 'interpretations': [
            dict(id='S1', statement='Fictional strength', section='swot', category='Strengths', depends_on=['I1'],
                 reasoning='Internal existing fictional capability', method='Qualitative', uncertainty='Synthetic')]}
        sr = check.validate_output(self.manifest, self.facts, basis, sc, so, latest_positioning=po, latest_positioning_context=pc)
        report = check.merge_reports([pr, sr]); self.assertEqual(report['errors'], [])
        rows = po['interpretations'] + so['interpretations']
        work = WORK.prepare(self.manifest, self.facts, report, rows, self.cache, basis, self.work)
        return basis, pc, po, sc, so, report, rows, work

    def test_document_bundles_include_each_source_and_core_view_A_requirements(self):
        self.assertEqual(len(self.work['source_batches']), 2)
        by_id = {b['source_id']: b for b in self.work['source_batches']}
        self.assertEqual(by_id[self.sources[0]['id']]['review_fact_ids'], ['P1', 'P2', 'P3'])
        self.assertEqual(by_id[self.sources[1]['id']]['review_fact_ids'], ['P2'])
        self.assertEqual(self.work['required_full_review_ids'], ['P1', 'P2'])

    def test_compact_success_expands_only_explicit_ids_and_local_hashes(self):
        result = self.base()
        self.assertEqual(len(result['claims']), 3)
        self.assertEqual({r['id']: r['fingerprint'] for r in result['claims']}, self.report['fingerprints'])
        self.assertEqual(len(result['source_checks']), 2)
        self.assertEqual(result['input_fingerprint'], self.report['packet_fingerprint'])
        self.assertEqual(result['review_work_fingerprint'], self.work['fingerprint'])

    def test_missing_decision_is_open_and_required_missing_blocks_release(self):
        draft = self.draft(ids=['P1', 'P3'])
        with self.assertRaisesRegex(ValueError, 'required full check missing'): STAMP.stamp(draft, self.report, self.work)
        draft['status'] = 'blockiert'
        result = STAMP.stamp(draft, self.report, self.work)
        self.assertEqual(next(r['status'] for r in result['claims'] if r['id'] == 'P2'), 'offen')
        self.assertEqual(result['missing_decisions'], ['P2'])

    def test_multiple_source_fact_needs_every_explicit_document_check(self):
        draft = self.draft(); draft['source_checks'] = draft['source_checks'][:1]
        with self.assertRaisesRegex(ValueError, 'each factual source'): STAMP.stamp(draft, self.report, self.work)

    def test_unknown_duplicate_verdicts_and_implicit_inheritance_block(self):
        for ids in (['P1', 'P1'], ['P404']):
            draft = self.draft(); draft['review_groups'][0]['claim_ids'] = ids
            with self.assertRaises((ValueError, TypeError)): STAMP.stamp(draft, self.report, self.work)
        draft = self.draft(); draft['review_groups'][0]['status'] = 'übernommen'
        with self.assertRaisesRegex(ValueError, 'unchanged fully reviewed'): STAMP.stamp(draft, self.report, self.work)

    def test_same_checked_source_and_statement_offer_explicit_reuse(self):
        prior = self.base()
        self.store(self.sources[0], 'Fictional full source')  # refreshed metadata, same original
        work = WORK.prepare(self.manifest, self.facts, self.report, cache=self.cache,
                            previous_work=self.work, previous_review=prior)
        self.assertEqual(work['reuse_candidates'], ['P1', 'P2', 'P3'])
        draft = self.draft(work); draft['review_groups'][0]['status'] = 'übernommen'; draft['source_checks'] = []
        self.assertTrue(all(r['status'] == 'übernommen' for r in STAMP.stamp(draft, self.report, work)['claims']))

    def test_no_snapshot_or_non_A_or_unreleased_review_never_inherits(self):
        for modify in ('missing', 'depth', 'blocked'):
            work = copy.deepcopy(self.work); prior = self.base()
            if modify == 'missing':
                work = WORK.prepare(self.manifest, self.facts, self.report)
                prior = STAMP.stamp(self.draft(work), self.report, work)
            elif modify == 'depth':
                prior['claims'][0]['depth'] = 'B'
            else:
                prior['status'] = 'blockiert'
            later = WORK.prepare(self.manifest, self.facts, self.report, cache=self.cache,
                                 previous_work=work, previous_review=prior)
            if modify == 'depth': self.assertNotIn(prior['claims'][0]['id'], later['reuse_candidates'])
            else: self.assertEqual(later['reuse_candidates'], [])

    def test_mapping_change_rechecks_only_relevant_rows(self):
        prior = self.base(); module = copy.deepcopy(self.module); module['products'][0]['label'] = 'Changed product'
        report, facts = FACTS.build(self.manifest, [module])
        work = WORK.prepare(self.manifest, facts, report, cache=self.cache, previous_work=self.work, previous_review=prior)
        self.assertEqual(work['reuse_candidates'], ['P3']); self.assertEqual(work['claims_to_review'], ['P1', 'P2'])

    def test_parent_fact_change_reaches_unchanged_child(self):
        module = copy.deepcopy(self.module); module['claims'][1]['depends_on'] = ['P1']
        report, facts = FACTS.build(self.manifest, [module]); first = WORK.prepare(self.manifest, facts, report, cache=self.cache)
        prior = STAMP.stamp(self.draft(first), report, first)
        module['claims'][0]['statement'] += ' changed'
        report, facts = FACTS.build(self.manifest, [module])
        later = WORK.prepare(self.manifest, facts, report, cache=self.cache, previous_work=first, previous_review=prior)
        self.assertNotIn('P2', later['reuse_candidates']); self.assertIn('P3', later['reuse_candidates'])

    def test_changed_original_invalidates_every_linked_fact_even_same_claim_hash(self):
        prior = self.base(); self.store(self.sources[0], 'Changed original')
        later = WORK.prepare(self.manifest, self.facts, self.report, cache=self.cache, previous_work=self.work, previous_review=prior)
        self.assertEqual(later['reuse_candidates'], [])
        with self.assertRaisesRegex(ValueError, 'original source snapshot changed'): STAMP.stamp(self.draft(), self.report, self.work)

    def test_work_tampering_foreign_run_phase_and_validation_rejected(self):
        work = copy.deepcopy(self.work); work['reuse_candidates'] = ['P1']
        with self.assertRaisesRegex(ValueError, 'snapshot changed'): STAMP.stamp(self.draft(work), self.report, work)
        for key, value in [('run_id', 'other'), ('as_of', '2026-10-12'), ('phase', 'final')]:
            draft = self.draft(); draft[key] = value
            with self.assertRaises(ValueError): STAMP.stamp(draft, self.report, self.work)
        report = copy.deepcopy(self.report); report['fingerprints']['P1'] = 'other'
        with self.assertRaisesRegex(ValueError, 'validation changed'): STAMP.stamp(self.draft(), report, self.work)

    def test_final_reviews_all_new_analyses_without_repeating_bound_basis_sources(self):
        basis, pc, po, sc, so, report, rows, work = self.final()
        self.assertEqual(work['facts_to_verify'], [])
        self.assertEqual(set(work['fact_reuse_candidates']), {'P1', 'P2'})
        self.assertEqual(work['claims_to_review'], ['I1', 'I2', 'S1'])
        draft = self.draft(work); draft['reuse_fact_ids'] = ['P1', 'P2']
        result = STAMP.stamp(draft, report, work)
        self.assertEqual(len(result['claims']), 3)
        self.assertTrue(all(r['status'] == 'übernommen' for r in result['fact_review'].values()))
        later = WORK.prepare(self.manifest, self.facts, report, rows, self.cache, basis, self.work, work, result)
        self.assertEqual(later['reuse_candidates'], ['I1', 'I2', 'S1'])

    def test_final_changed_source_rechecks_dependent_analyses_and_missing_facts_blocks(self):
        basis, pc, po, sc, so, report, rows, first = self.final()
        draft = self.draft(first); draft['reuse_fact_ids'] = ['P1', 'P2']; prior = STAMP.stamp(draft, report, first)
        self.store(self.sources[0], 'Changed full original')
        later = WORK.prepare(self.manifest, self.facts, report, rows, self.cache, basis, self.work, first, prior)
        self.assertEqual(later['facts_to_verify'], ['P1', 'P2']); self.assertEqual(later['reuse_candidates'], [])
        with self.assertRaisesRegex(ValueError, 'explicit checked/reused fact'): STAMP.stamp(self.draft(later), report, later)
        draft = self.draft(later); draft['fact_groups'] = [dict(claim_ids=['P1', 'P2'], depth='A', status='geprüft', note='SIMULATED fresh source review')]
        draft['source_checks'] = self.draft()['source_checks']
        self.assertEqual(STAMP.stamp(draft, report, later)['status'], 'freigegeben')

    def test_final_requires_explicit_basis_ack_and_current_packet(self):
        basis, pc, po, sc, so, report, rows, work = self.final()
        with self.assertRaisesRegex(ValueError, 'explicit checked/reused fact'): STAMP.stamp(self.draft(work), report, work)
        changed = copy.deepcopy(self.facts); changed['module_views'][0]['products'][0]['label'] = 'New mapping'
        with self.assertRaisesRegex(ValueError, 'basis packet'): WORK.prepare(self.manifest, changed, report, rows, self.cache, basis, self.work)

    def test_cli_snapshot_changed_inputs_and_legacy_compatibility(self):
        for name, data in [('manifest', self.manifest), ('facts', self.facts), ('validation', self.report)]:
            (self.root/(name+'.json')).write_text(json.dumps(data))
        args = [sys.executable, str(ROOT/'scripts/review-work.py'), 'prepare', '--manifest', str(self.root/'manifest.json'),
                '--facts', str(self.root/'facts.json'), '--validation', str(self.root/'validation.json'),
                '--cache', str(self.root/'cache'), '--out', str(self.root/'work.json')]
        result = subprocess.run(args, capture_output=True, text=True); self.assertEqual(result.returncode, 0, result.stdout)
        work = json.loads((self.root/'work.json').read_text()); draft = self.draft(work)
        (self.root/'draft.json').write_text(json.dumps(draft))
        stamp = [sys.executable, str(ROOT/'scripts/stamp-review.py'), '--draft', str(self.root/'draft.json'),
                 '--validation', str(self.root/'validation.json'), '--work', str(self.root/'work.json'), '--out', str(self.root/'review.md')]
        result = subprocess.run(stamp, capture_output=True, text=True); self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(WORK.CHECK.read(self.root/'review.md')['status'], 'freigegeben')
        (self.root/'facts.json').write_text(json.dumps({**self.facts, 'scope': 'Changed'}))
        result = subprocess.run(stamp, capture_output=True, text=True); self.assertNotEqual(result.returncode, 0)
        self.assertIn('input changed', result.stdout)
        legacy = {**self.draft(), 'claims': [dict(id='P1', depth='A', status='geprüft')]}
        legacy.pop('review_groups'); legacy.pop('source_checks')
        self.assertEqual(STAMP.stamp(legacy, self.report)['claims'][0]['status'], 'geprüft')

    def test_shared_region_scope_and_peer_labels_are_bound(self):
        facts = copy.deepcopy(self.facts)
        facts['module_views'][0]['topics'] = [dict(id='region', label='Region', countries=['Testland A'],
                                                sections=[dict(label='Status', claim_ids=['P1'])])]
        first = WORK.binding(self.manifest, facts, 'P1')
        facts['module_views'][0]['topics'][0]['countries'] = ['Testland B']
        self.assertNotEqual(first, WORK.binding(self.manifest, facts, 'P1'))
        facts['module_views'].append(dict(role='market', peers=[dict(id='peer', label='Peer A')],
                                          observations=[dict(peer_id='peer', criterion_id='test', claim_ids=['P1'])]))
        first = WORK.binding(self.manifest, facts, 'P1')
        facts['module_views'][-1]['peers'][0]['label'] = 'Peer B'
        self.assertNotEqual(first, WORK.binding(self.manifest, facts, 'P1'))

    def test_basis_release_needs_explicit_mapping_scope_decision(self):
        draft = self.draft(); draft.pop('scope_and_mappings_checked')
        with self.assertRaisesRegex(ValueError, 'scope/module mapping'): STAMP.stamp(draft, self.report, self.work)

    def test_declared_snapshot_mismatch_cannot_be_recorded_as_checked(self):
        draft = self.draft(); draft['source_checks'][0]['content_sha256'] = 'wrong'
        with self.assertRaisesRegex(ValueError, 'declared document snapshot'): STAMP.stamp(draft, self.report, self.work)


if __name__ == '__main__':
    unittest.main()
