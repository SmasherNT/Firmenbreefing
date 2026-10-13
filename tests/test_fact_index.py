import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('index_test', ROOT/'scripts/fact-index.py')
INDEX = importlib.util.module_from_spec(spec); spec.loader.exec_module(INDEX)


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.manifest = dict(schema_version=1, mode='facts-v2', run_id='index-test',
                             company='Fictional Test', as_of='2026-10-13', scope='Fictional index test', selected_roles=['portfolio', 'market'])
        self.source = dict(id=INDEX.FACTS.source_id('https://example.org/source'), name='Test', title='Test source',
                           url='https://example.org/source', published_date='2026-09-01', accessed_date='2026-10-13',
                           source_kind='company')
        claim = dict(id='P-site', kind='Herstellerangabe', statement='Own factory announced.',
                     evidence='Paraphrase: factory planned.', location='Factory paragraph', uncertainty='Not operating.',
                     source_ids=[self.source['id']], event_date='2026-09-01')
        self.portfolio = {**self.manifest, 'role': 'portfolio', 'scope': 'Portfolio', 'status': 'vollständig',
                          'claims': [claim], 'source_proposals': [self.source], 'gaps': [], 'coverage': []}
        self.market = copy.deepcopy(self.portfolio); self.market.update(role='market', scope='Market')
        self.market['claims'][0]['id'] = 'M-site'

    def test_full_original_claims_ownership_and_candidate_only(self):
        before = copy.deepcopy([self.portfolio, self.market])
        index = INDEX.build_index(self.manifest, before)
        self.assertEqual(index['status'], 'unreviewed-index')
        self.assertEqual(index['duplicate_candidates'], [['P-site', 'M-site']])
        self.assertEqual(index['entries'][0]['claim'], self.portfolio['claims'][0])
        self.assertEqual(before, [self.portfolio, self.market])
        self.assertEqual(index['missing_roles'], [])
        found = INDEX.find(index, self.manifest, query='factory announced')
        self.assertEqual(len(found['entries']), 2)
        self.assertIn('no content approval', found['notice'])

    def test_partial_index_missing_roles_and_no_unrelated_scope_merge(self):
        partial = INDEX.build_index(self.manifest, [self.portfolio])
        self.assertEqual(partial['missing_roles'], ['market'])
        other = copy.deepcopy(self.market)
        other['claims'][0]['statement'] = 'Partner factory operating.'
        self.assertEqual(INDEX.build_index(self.manifest, [self.portfolio, other])['duplicate_candidates'], [])

    def test_foreign_identity_duplicate_ids_conflicting_sources_and_unverified_input_rejected(self):
        for key in ('company', 'run_id', 'as_of'):
            other = copy.deepcopy(self.portfolio); other[key] = '2026-10-12' if key == 'as_of' else 'Other'
            with self.assertRaises(ValueError): INDEX.build_index(self.manifest, [other])
        for mutate in (
            lambda m: m['claims'][0].update(kind='Nutzerangabe'),
            lambda m: m['claims'][0].update(score=3),
            lambda m: m['claims'][0].update(source_ids=['missing']),
            lambda m: m['claims'].append(copy.deepcopy(m['claims'][0])),
        ):
            other = copy.deepcopy(self.portfolio); mutate(other)
            with self.assertRaises(ValueError): INDEX.build_index(self.manifest, [other])
        other = copy.deepcopy(self.market); other['source_proposals'][0]['title'] = 'Different title'
        with self.assertRaisesRegex(ValueError, 'conflicting source'): INDEX.build_index(self.manifest, [self.portfolio, other])

    def test_module_change_and_foreign_lookup_block_reuse(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'portfolio.json'; path.write_text(json.dumps(self.portfolio))
            index = INDEX.build_index(self.manifest, [self.portfolio], [path])
            self.assertEqual(len(INDEX.find(index, self.manifest, claim_ids=['P-site'])['entries']), 1)
            with self.assertRaises(ValueError): INDEX.find(index, {**self.manifest, 'run_id': 'other'})
            with self.assertRaisesRegex(ValueError, 'not found'): INDEX.find(index, self.manifest, claim_ids=['P-missing'])
            path.write_text(json.dumps({**self.portfolio, 'scope': 'Changed'}))
            with self.assertRaisesRegex(ValueError, 'module changed'): INDEX.find(index, self.manifest)

    def test_prepare_cli_adds_index_without_changing_packet_or_snapshots(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); manifest = {**self.manifest, 'selected_roles': ['portfolio']}
            for name, value in [('manifest.json', manifest), ('portfolio.json', self.portfolio)]:
                (root/name).write_text(json.dumps(value))
            report, packet = INDEX.FACTS.build(manifest, [self.portfolio])
            self.assertEqual(report['errors'], [])
            result = subprocess.run([sys.executable, str(ROOT/'scripts/prepare-facts.py'), '--manifest',
                      str(root/'manifest.json'), '--modules', str(root/'portfolio.json'), '--out', str(root/'work')],
                      capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertEqual(json.loads((root/'work/review-packet.json').read_text()), packet)
            self.assertEqual(json.loads((root/'work/facts-validation.json').read_text()), report)
            self.assertTrue((root/'work/facts-index.json').exists())
            lookup = subprocess.run([sys.executable, str(ROOT/'scripts/fact-index.py'), '--manifest',
                     str(root/'manifest.json'), 'find', '--index', str(root/'work/facts-index.json'),
                     '--claim-ids', 'P-site'], capture_output=True, text=True)
            self.assertEqual(lookup.returncode, 0, lookup.stdout)
            self.assertEqual(json.loads(lookup.stdout)['entries'][0]['claim'], self.portfolio['claims'][0])

    def test_changed_file_during_build_cannot_get_a_current_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/'portfolio.json'
            target.write_text(json.dumps({**self.portfolio, 'scope': 'New scope'}))
            with self.assertRaisesRegex(ValueError, 'changed during index build'):
                INDEX.build_index(self.manifest, [self.portfolio], [target])


if __name__ == '__main__':
    unittest.main()
