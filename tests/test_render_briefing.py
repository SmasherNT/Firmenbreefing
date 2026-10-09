import copy
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import test_interpretation as fixtures

RENDER = fixtures.load('render', 'render-briefing.py')
ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.anchors = [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.anchors.append(attrs['href'][1:])


def bundle():
    f = fixtures.InterpretationTests()
    f.setUp()
    for s in f.facts['sources']:
        s['fictional'] = True
    f.facts['module_views'] = [dict(role='market', peers=f.market['peers'],
        observations=f.market['observations'], company_facts=[dict(id='business',
        label='Synthetic inspection example', claim_ids=['M1'])], gaps=[], coverage=[])]
    f.facts['module_context'] = [dict(role='market', status='vollständig',
        document_scope='Fictional supplied documents only; URLs not opened')]
    f.review = f.make_review()
    f.review['input_fingerprint'] = fixtures.CHECK.digest(f.facts)
    ctx = f.context(True)
    out = f.output(ctx, True)
    check = f.check(ctx, out, latest_plan=f.plan)
    final = fixtures.STAMP.stamp({**f.review, 'phase': 'final', 'claims': [
        dict(id='I1', depth='A', status='geprüft', evidence_review='Simulated offline decision only')]}, check)
    return dict(manifest=f.manifest, facts=f.facts, basis=f.review,
        positioning=out, positioning_context=ctx, final=final, plan=f.plan)


def refresh_basis(b):
    check = fixtures.REVIEW.validate(b['facts'])
    b['basis']['claims'] = [dict(id=k, depth='A', status='geprüft', fingerprint=v)
                          for k, v in check['fingerprints'].items()]
    b['basis']['input_fingerprint'] = fixtures.CHECK.digest(b['facts'])


def facts_only(b):
    return {k: v for k, v in b.items() if k in ('manifest', 'facts', 'basis')}


def add_network(b):
    b['manifest']['selected_roles'].append('cluster')
    b['facts']['claims'].append({**b['facts']['claims'][0], 'id': 'C1',
        'statement': 'Fictional supplier relationship'})
    b['facts']['module_views'].append(dict(role='cluster', gaps=[], coverage=[]))
    s = b['facts']['sources'][0]
    b['facts']['network'] = dict(schema_version=1, company='Example', as_of='2026-10-09',
        target_id='target', nodes=[dict(id='target', kind='target', label='Example'),
            dict(id='supplier', kind='supplier', cluster='technology', label='Synthetic supplier')],
        products=[dict(id='inspection', label='Inspection system')], sources=[s], edges=[dict(
            id='e1', **{'from': 'supplier', 'to': 'target'}, type='Supply',
            summary='Fictional components', categories=['supplier'], product_ids=['inspection'],
            source_ids=[s['id']], claim_ids=['C1'], status='announced', as_of='2026-10',
            capital_share='not applicable', voting_share='not applicable',
            uncertainty='Synthetic fixture only', control='No control claim')])
    refresh_basis(b)


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.b = bundle()

    def test_matrix_details_sources_and_all_internal_links(self):
        body = RENDER.build(**self.b)
        self.assertIn('Capability Matrix', body)
        self.assertIn('Validation', body)
        self.assertIn('test reported', body)
        self.assertIn('Tests section', body)
        self.assertIn('Fiktive Testdaten', body)
        links = Links(); links.feed(body)
        self.assertEqual(len(links.ids), len(set(links.ids)))
        self.assertTrue(set(links.anchors) <= set(links.ids))
        self.assertNotIn('<script src=', body)

    def test_mapping_snapshot_rejects_unchanged_claims(self):
        self.b['facts']['module_views'][0]['company_facts'][0]['label'] = 'Changed label'
        with self.assertRaisesRegex(ValueError, 'snapshot'):
            RENDER.build(**self.b)

    def test_background_claim_not_allowed_in_core_view(self):
        b = facts_only(self.b)
        b['basis']['claims'][0]['depth'] = 'B'
        with self.assertRaisesRegex(ValueError, 'Vollprüfung'):
            RENDER.build(**b)

    def test_missing_or_stale_final_review_rejected(self):
        for final in (None, {**self.b['final'], 'status': 'blockiert'}):
            with self.assertRaises(ValueError):
                RENDER.build(**{**self.b, 'final': final})
        self.b['final']['claims'][0]['fingerprint'] = 'old'
        with self.assertRaisesRegex(ValueError, 'stale'):
            RENDER.build(**self.b)

    def test_foreign_review_or_blocked_module_rejected(self):
        with self.assertRaises(ValueError):
            RENDER.build(**{**self.b, 'final': {**self.b['final'], 'company': 'Other'}})
        self.b['facts']['module_context'][0]['status'] = 'blockiert'
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError, 'blocked factual'):
            RENDER.build(**self.b)

    def test_matrix_mapping_must_equal_reviewed_market(self):
        ctx = self.b['positioning_context']
        ctx['matrix']['peers'][0]['label'] = 'Unreviewed replacement'
        ctx['fingerprint'] = fixtures.CHECK.digest({k: v for k, v in ctx.items() if k != 'fingerprint'})
        self.b['positioning']['input_fingerprint'] = ctx['fingerprint']
        with self.assertRaisesRegex(ValueError, 'mapping'):
            RENDER.build(**self.b)

    def test_blocking_request_stops_output(self):
        self.b['positioning']['status'] = 'teilweise'
        self.b['positioning']['research_requests'] = [dict(id='R1', target_role='market',
            question='Verify test', related_claim_ids=['M1'], blocking=True)]
        with self.assertRaisesRegex(ValueError, 'blocking'):
            RENDER.build(**self.b)

    def test_event_date_and_unknown_view_claim_rejected(self):
        b = facts_only(self.b)
        b['facts']['module_views'][0]['events'] = [dict(id='event', label='Test',
                                                      date='2026-02-30', claim_ids=['M1'])]
        refresh_basis(b)
        with self.assertRaises(ValueError):
            RENDER.build(**b)
        b['facts']['module_views'][0]['events'][0].update(date=None, claim_ids=['M404'])
        refresh_basis(b)
        with self.assertRaises(ValueError):
            RENDER.build(**b)

    def test_network_static_fallback_preserves_optional_details(self):
        b = facts_only(self.b); add_network(b)
        body = RENDER.build(**b)
        before_script = body.split('<script type="application/json"')[0]
        for text in ('Kapitalanteil', 'Stimmrechte', 'No control claim', 'Synthetic fixture only', 'Inspection system'):
            self.assertIn(text, before_script)
        self.assertIn('tableBody.replaceChildren()', body)
        self.assertIn('Cluster · Technologie, Industrie &amp; Marktzugang', body)

    def test_invalid_network_categories_rejected(self):
        b = facts_only(self.b); add_network(b)
        b['facts']['network']['edges'][0]['categories'] = ['invented']
        refresh_basis(b)
        with self.assertRaisesRegex(ValueError, 'categories'):
            RENDER.build(**b)

    def test_profile_is_optional_and_requires_h_facts(self):
        b = facts_only(self.b)
        self.assertNotIn('page-profile', RENDER.build(**b))
        b['manifest']['person'] = 'Alex Example'
        self.assertIn('öffentlich nicht verifiziert', RENDER.build(**b))
        b['manifest']['person'] = dict(name='Alex Example', position='Integration Lead')
        self.assertIn('Alex Example · Integration Lead', RENDER.build(**b))
        b['facts']['module_views'][0]['profile'] = dict(name='Alex', claim_ids=['M1'])
        refresh_basis(b)
        with self.assertRaises(ValueError):
            RENDER.build(**b)

    def test_script_injection_and_literal_template_tokens_are_safe(self):
        b = facts_only(self.b); add_network(b)
        b['facts']['network']['nodes'][1]['label'] = '</script><script>attack()</script> __TITLE__'
        refresh_basis(b)
        body = RENDER.build(**b)
        self.assertNotIn('<script>attack()', body)
        self.assertIn('\\u003c/script\\u003e', body)
        self.assertIn('__TITLE__', body)

    def test_cli_success_failure_and_input_overwrite_protection(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); b = facts_only(self.b)
            for key, data in b.items():
                (root / (key + '.json')).write_text(json.dumps(data))
            cmd = [sys.executable, str(ROOT / 'scripts/render-briefing.py')]
            for flag, key in (('manifest', 'manifest'), ('facts', 'facts'), ('basis-review', 'basis')):
                cmd += ['--' + flag, str(root / (key + '.json'))]
            target = root / 'briefing.html'
            run = subprocess.run(cmd + ['--out', str(target)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout)
            run = subprocess.run(cmd + ['--full', '--out', str(root / 'blocked.html')], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertFalse((root / 'blocked.html').exists())
            original = (root / 'facts.json').read_text()
            run = subprocess.run(cmd + ['--out', str(root / 'facts.json')], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertEqual((root / 'facts.json').read_text(), original)


if __name__ == '__main__':
    unittest.main()
