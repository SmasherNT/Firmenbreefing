import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

CHECK = load('interpretation', 'check-interpretation.py')
STAMP = load('stamp', 'stamp-review.py')
REVIEW = load('review', 'check-review-data.py')

class InterpretationTests(unittest.TestCase):
    def setUp(self):
        self.manifest = dict(schema_version=1, mode='facts-v2', run_id='fixture',
                             company='Example', as_of='2026-10-09', scope='Inspection',
                             selected_roles=['market'])
        self.facts = {k: v for k, v in self.manifest.items() if k != 'selected_roles'}
        self.facts.update(sources=[], claims=[])
        for n in (1, 2):
            self.facts['sources'].append(dict(id=f'S{n}', name='Example', title=f'Report {n}',
                url=f'https://example.org/{n}', published_date=None, accessed_date='2026-10-09'))
            self.facts['claims'].append(dict(id=f'M{n}', statement=f'Manufacturer reports test {n}',
                kind='Herstellerangabe', source_ids=[f'S{n}'], evidence='Paraphrase: test reported',
                location='Tests section', uncertainty='Manufacturer report'))
        self.review = self.make_review()
        self.plan = dict(run_id='fixture', company='Example', as_of='2026-10-09',
            comparison_unit='Inspection', purpose='Compare validation', version=1,
            peer_groups=['Direct peers'], criteria=[dict(id='validation', label='Validation',
                question='What test is reported?', evidence_required='Test report',
                display_type='Evidenzstufe', anchors={'1': 'offered', '2': 'test reported'},
                applicability='Inspection', rationale='Requested validation')])
        self.market = {k: v for k, v in self.manifest.items() if k != 'selected_roles'}
        self.market.update(comparison_plan_version=1, peers=[dict(id='example', label='Example')],
            observations=[dict(peer_id='example', criterion_id='validation', claim_ids=['M1'])])

    def make_review(self):
        result = REVIEW.validate(self.facts)
        return dict(schema_version=1, run_id='fixture', company='Example', as_of='2026-10-09',
            phase='basis', status='freigegeben', material_errors=[], claims=[
                dict(id=cid, depth='A', status='geprüft', fingerprint=fp)
                for cid, fp in result['fingerprints'].items()])

    def context(self, matrix=False):
        return CHECK.prepare(self.manifest, self.facts, self.review, ['M1'],
                             self.plan if matrix else None, self.market if matrix else None)

    def output(self, ctx, matrix=False, role='positioning'):
        row = dict(id='I1' if role == 'positioning' else 'S1', statement='Interpretation',
                   section='Positioning', depends_on=['M1'], reasoning='Reasoned from test',
                   method='Qualitative', uncertainty='Manufacturer only')
        if role == 'swot':
            row['category'] = 'Strengths'
        if matrix:
            row.update(type='matrix_cell', peer_id='example', criterion_id='validation',
                       cell_status='bewertet', value=2, next_stage_limit='Highest defined anchor')
        out = dict(schema_version=1, mode='interpret-v2', role=role, run_id='fixture',
                   company='Example', as_of='2026-10-09', scope='Inspection', status='vollständig',
                   input_fingerprint=ctx['fingerprint'], interpretations=[row],
                   research_requests=[], shared_limitations=[])
        if matrix:
            out['plan_fingerprint'] = ctx['plan_fingerprint']
        return out

    def check(self, ctx, out, **kwargs):
        return CHECK.validate_output(self.manifest, self.facts, self.review, ctx, out, **kwargs)

    def test_selective_context_and_valid_interpretation(self):
        ctx = self.context()
        self.assertEqual([r['id'] for r in ctx['facts']], ['M1'])
        self.assertEqual([r['id'] for r in ctx['sources']], ['S1'])
        result = self.check(ctx, self.output(ctx))
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['fact_dependencies']['I1'], ['M1'])

    def test_no_implicit_all_facts(self):
        with self.assertRaisesRegex(ValueError, 'select relevant'):
            CHECK.prepare(self.manifest, self.facts, self.review, [])

    def test_identity_and_material_error_gates(self):
        for key in ('run_id', 'company', 'as_of'):
            review = copy.deepcopy(self.review)
            review[key] = 'other'
            with self.assertRaises(ValueError):
                CHECK.prepare(self.manifest, self.facts, review, ['M1'])
        for key, value in (('status', 'teilweise'), ('material_errors', ['Wrong fact'])):
            review = {**self.review, key: value}
            with self.assertRaises(ValueError):
                CHECK.prepare(self.manifest, self.facts, review, ['M1'])

    def test_background_review_cannot_support_rating(self):
        self.review['claims'][0]['depth'] = 'B'
        ctx = self.context()
        self.assertIn('M1', ctx['pending_checks'])
        self.assertTrue(self.check(ctx, self.output(ctx))['errors'])

    def test_stale_review_and_changed_fact_rejected(self):
        ctx = self.context()
        self.facts['claims'][0]['statement'] += ' changed'
        result = self.check(ctx, self.output(ctx))
        self.assertTrue(any('changed fact' in e for e in result['errors']))
        self.assertTrue(any('veraltet' in e for e in result['errors']))

    def test_changed_source_rejected(self):
        ctx = self.context()
        self.facts['sources'][0]['title'] = 'Revised report'
        self.assertTrue(self.check(ctx, self.output(ctx))['errors'])

    def test_unused_changed_fact_does_not_invalidate(self):
        ctx = self.context()
        self.facts['claims'][1]['statement'] += ' changed'
        self.assertEqual(self.check(ctx, self.output(ctx))['errors'], [])

    def test_context_tampering_detected_even_with_new_outer_hash(self):
        ctx = self.context()
        ctx['facts'][0]['statement'] = 'Tampered'
        ctx['fingerprint'] = CHECK.digest({k: v for k, v in ctx.items() if k != 'fingerprint'})
        with self.assertRaisesRegex(ValueError, 'snapshot'):
            self.check(ctx, self.output(ctx))

    def test_fact_dependency_closure_requires_a(self):
        self.facts['claims'][0]['depends_on'] = ['M2']
        self.review = self.make_review()
        self.review['claims'][1]['depth'] = 'B'
        ctx = self.context()
        self.assertEqual(len(ctx['facts']), 2)
        result = self.check(ctx, self.output(ctx))
        self.assertTrue(result['errors'])
        self.assertEqual(result['fact_dependencies']['I1'], ['M1', 'M2'])

    def test_fact_cycle_rejected(self):
        self.facts['claims'][0]['depends_on'] = ['M2']
        self.facts['claims'][1]['depends_on'] = ['M1']
        self.review = self.make_review()
        ctx = self.context()
        self.assertTrue(any('cyclic fact' in e for e in self.check(ctx, self.output(ctx))['errors']))

    def test_unknown_dependencies_and_input_snapshot_rejected(self):
        ctx = self.context()
        out = self.output(ctx)
        out['interpretations'][0]['depends_on'] = ['missing']
        self.assertTrue(self.check(ctx, out)['errors'])
        out = self.output(ctx)
        out['input_fingerprint'] = 'old'
        self.assertTrue(self.check(ctx, out)['errors'])

    def test_matrix_anchors_and_complete_pairs(self):
        ctx = self.context(True)
        out = self.output(ctx, True)
        self.assertEqual(self.check(ctx, out, latest_plan=self.plan)['errors'], [])
        out['interpretations'][0]['value'] = 5
        self.assertTrue(self.check(ctx, out, latest_plan=self.plan)['errors'])
        out['interpretations'] = []
        self.assertTrue(self.check(ctx, out, latest_plan=self.plan)['errors'])

    def test_current_plan_required_and_changes_detected(self):
        ctx = self.context(True)
        out = self.output(ctx, True)
        with self.assertRaisesRegex(ValueError, 'current comparison plan'):
            self.check(ctx, out)
        changed = copy.deepcopy(self.plan)
        changed['version'] = 2
        self.assertTrue(self.check(ctx, out, latest_plan=changed)['errors'])

    def test_unrated_cell_uses_null_and_cannot_support_swot(self):
        ctx = self.context(True)
        out = self.output(ctx, True)
        row = out['interpretations'][0]
        row.update(cell_status='nicht öffentlich belegt', value=None, depends_on=[],
                   coverage_note='No test in supplied documents')
        self.assertEqual(self.check(ctx, out, latest_plan=self.plan)['errors'], [])
        with self.assertRaisesRegex(ValueError, 'unrated'):
            CHECK.prepare(self.manifest, self.facts, self.review, [], self.plan,
                          positioning=out, positioning_context=ctx, interpretation_ids=['I1'])
        row['value'] = 0
        self.assertTrue(self.check(ctx, out, latest_plan=self.plan)['errors'])

    def test_inapplicability_needs_fact_basis(self):
        ctx = self.context(True)
        out = self.output(ctx, True)
        out['interpretations'][0].update(cell_status='nicht anwendbar', value=None,
                                        depends_on=[], coverage_note='Not applicable')
        self.assertTrue(self.check(ctx, out, latest_plan=self.plan)['errors'])

    def test_no_total_ranking_or_unplanned_score(self):
        ctx = self.context()
        out = self.output(ctx)
        out['total_score'] = 4
        self.assertTrue(self.check(ctx, out)['errors'])
        del out['total_score']
        out['interpretations'][0]['score'] = 4
        self.assertTrue(self.check(ctx, out)['errors'])

    def test_typed_additional_score_matches_method(self):
        self.plan['assessment_methods'] = [dict(id='maturity', assessment_type='product_maturity',
            applicability='Inspection', anchors={'1': 'offered', '2': 'test reported'})]
        ctx = CHECK.prepare(self.manifest, self.facts, self.review, ['M1'], self.plan)
        out = self.output(ctx)
        out['plan_fingerprint'] = ctx['plan_fingerprint']
        row = out['interpretations'][0]
        row.update(type='product_maturity', method_id='maturity', score=2, subject='Inspection product')
        self.assertEqual(self.check(ctx, out, latest_plan=self.plan)['errors'], [])
        row['method_id'] = 'other'
        self.assertTrue(self.check(ctx, out, latest_plan=self.plan)['errors'])

    def test_swot_uses_current_positioning_and_fingerprints(self):
        pc = self.context(True)
        po = self.output(pc, True)
        sc = CHECK.prepare(self.manifest, self.facts, self.review, [], self.plan,
                           positioning=po, positioning_context=pc, interpretation_ids=['I1'])
        self.assertNotIn('plan', sc)
        so = self.output(sc, role='swot')
        so['interpretations'][0]['depends_on'] = ['I1']
        args = dict(latest_positioning=po, latest_positioning_context=pc, latest_plan=self.plan)
        result = self.check(sc, so, **args)
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['fingerprints']['I1'], self.check(pc, po, latest_plan=self.plan)['fingerprints']['I1'])
        self.assertEqual(result['required_full_review_ids'], ['I1', 'S1'])
        changed = copy.deepcopy(po)
        changed['interpretations'][0]['reasoning'] = 'Updated conclusion'
        self.assertTrue(self.check(sc, so, **{**args, 'latest_positioning': changed})['errors'])
        with self.assertRaisesRegex(ValueError, 'current positioning'):
            self.check(sc, so)

    def test_swot_quadrants_limit_and_no_chained_swot(self):
        ctx = self.context()
        out = self.output(ctx, role='swot')
        self.assertEqual(self.check(ctx, out)['errors'], [])
        out['interpretations'] = [{**out['interpretations'][0], 'id': f'S{n}'} for n in range(4)]
        self.assertTrue(self.check(ctx, out)['errors'])
        out['interpretations'] = out['interpretations'][:2]
        out['interpretations'][1]['depends_on'] = ['S0']
        self.assertTrue(self.check(ctx, out)['errors'])

    def test_blocking_question_conflicts_with_complete(self):
        ctx = self.context()
        out = self.output(ctx)
        out['research_requests'] = [dict(id='R1', target_role='market', question='Clarify test',
                                       blocking=True, related_claim_ids=['M1'])]
        self.assertTrue(self.check(ctx, out)['errors'])
        out['status'] = 'teilweise'
        self.assertEqual(self.check(ctx, out)['errors'], [])

    def test_merge_reports_rejects_conflict_and_other_run(self):
        ctx = self.context()
        report = self.check(ctx, self.output(ctx))
        self.assertEqual(CHECK.merge_reports([report, report])['required_full_review_ids'], ['I1'])
        changed = copy.deepcopy(report)
        changed['fingerprints']['I1'] = 'other'
        with self.assertRaises(ValueError):
            CHECK.merge_reports([report, changed])
        changed = {**report, 'run_id': 'other'}
        with self.assertRaises(ValueError):
            CHECK.merge_reports([report, changed])

    def test_stamp_preserves_decisions_and_adds_hash(self):
        ctx = self.context()
        report = self.check(ctx, self.output(ctx))
        draft = {**self.review, 'phase': 'final', 'claims': [dict(id='I1', depth='A',
                  status='geprüft', evidence_review='Offline supplied test only')]}
        stamped = STAMP.stamp(draft, report)
        self.assertEqual(stamped['claims'][0]['status'], 'geprüft')
        self.assertEqual(stamped['claims'][0]['fingerprint'], report['fingerprints']['I1'])
        self.assertNotIn('fingerprint', draft['claims'][0])

    def test_stamp_cannot_release_missing_unchecked_or_foreign_claim(self):
        ctx = self.context()
        report = self.check(ctx, self.output(ctx))
        draft = {**self.review, 'phase': 'final', 'claims': []}
        with self.assertRaises(ValueError):
            STAMP.stamp(draft, report)
        draft['claims'] = [dict(id='I1', depth='A', status='offen')]
        with self.assertRaises(ValueError):
            STAMP.stamp(draft, report)
        draft['claims'][0]['status'] = 'geprüft'
        with self.assertRaises(ValueError):
            STAMP.stamp({**draft, 'run_id': 'other'}, report)
        with self.assertRaises(ValueError):
            STAMP.stamp(draft, {**report, 'errors': ['Invalid basis']})

    def test_cli_and_review_markdown_roundtrip(self):
        ctx = self.context()
        out = self.output(ctx)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name, data in (('manifest', self.manifest), ('facts', self.facts),
                               ('review', self.review), ('context', ctx), ('output', out)):
                (root / f'{name}.json').write_text(json.dumps(data))
            args = [sys.executable, str(ROOT / 'scripts/check-interpretation.py')]
            for name in ('manifest', 'facts', 'review', 'context', 'output'):
                args += ['--' + name, str(root / f'{name}.json')]
            args += ['--out', str(root / 'validation.json')]
            run = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout)
            validation = json.loads((root / 'validation.json').read_text())
            draft = {**self.review, 'phase': 'final', 'claims': [dict(id='I1', depth='A', status='geprüft')]}
            (root / 'draft.json').write_text(json.dumps(draft))
            run = subprocess.run([sys.executable, str(ROOT / 'scripts/stamp-review.py'),
                '--draft', str(root / 'draft.json'), '--validation', str(root / 'validation.json'),
                '--out', str(root / 'review.md')], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout)
            self.assertEqual(CHECK.read(root / 'review.md')['claims'][0]['fingerprint'], validation['fingerprints']['I1'])
            out['interpretations'][0]['depends_on'] = ['missing']
            (root / 'output.json').write_text(json.dumps(out))
            args[-1] = str(root / 'invalid-validation.json')
            run = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(run.returncode, 1, run.stdout)
            self.assertFalse((root / 'invalid-validation.json').exists())

if __name__ == '__main__':
    unittest.main()
