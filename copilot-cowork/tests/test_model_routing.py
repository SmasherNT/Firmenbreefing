"""Portable runtime configuration and source-plan routing must agree."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import test_review_shards as shards

ROOT = Path(__file__).resolve().parents[1]


class ModelRoutingTests(unittest.TestCase):
    def test_project_and_roles_match_portable_policy(self):
        policy = json.loads((ROOT / 'references/modellaufteilung.json').read_text())
        settings = json.loads((ROOT / 'runtime/settings.json').read_text())
        self.assertEqual(settings['main'], policy['main'])
        self.assertEqual(policy['schema_version'], 2)
        self.assertEqual(set(policy['agents']), {p.stem for p in (ROOT / 'roles').glob('*.md')})
        for role, expected in policy['agents'].items():
            self.assertEqual(expected['model'], 'auto')
            self.assertEqual(expected['effort'], 'high' if role in {'cluster-analyst', 'market-facts-analyst', 'positioning-analyst'} else 'medium')
            self.assertFalse((ROOT / 'roles' / (role + '.md')).read_text().startswith('---'))

    def test_both_review_phases_use_requested_portable_profile(self):
        expected = dict(model='auto', effort='medium')
        self.assertEqual(shards.SHARDS.review_models(), {'source-reviewer': expected, 'source-document-reviewer': expected})

    def test_changed_worker_or_lead_policy_invalidates_plan(self):
        fixture = shards.ReviewShardTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        for role in ('source-document-reviewer', 'source-reviewer'):
            changed = copy.deepcopy(shards.SHARDS.review_models())
            changed[role]['effort'] = 'high'
            with patch.object(shards.SHARDS, 'review_models', return_value=changed):
                with self.assertRaisesRegex(ValueError, 'split plan changed'):
                    shards.SHARDS.verify_plan(fixture.plan, fixture.work, fixture.facts)
