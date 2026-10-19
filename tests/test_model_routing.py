"""Claude runtime configuration and source-plan routing must agree."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import test_review_shards as shards

ROOT = Path(__file__).resolve().parents[1]


class ModelRoutingTests(unittest.TestCase):
    def test_project_and_all_agent_headers_match_policy(self):
        policy = json.loads((ROOT / 'references/modellaufteilung.json').read_text())
        settings = json.loads((ROOT / '.claude/settings.json').read_text())
        self.assertEqual(settings, dict(model=policy['main']['model'], effortLevel=policy['main']['effort']))
        self.assertEqual(settings['model'], 'claude-opus-5-5')
        self.assertEqual(set(policy['agents']), {p.stem for p in (ROOT / '.claude/agents').glob('*.md')})
        for role, expected in policy['agents'].items():
            header = (ROOT / '.claude/agents' / (role + '.md')).read_text().split('---')[1]
            fields = dict(line.split(': ', 1) for line in header.strip().splitlines() if ': ' in line and not line.startswith(' '))
            self.assertEqual({key: fields[key] for key in ('model', 'effort')}, expected, role)
            self.assertEqual(expected['effort'], 'high' if role in {'cluster-analyst', 'market-facts-analyst', 'positioning-analyst'} else 'medium')

    def test_both_review_phases_use_sonnet_medium(self):
        expected = dict(model='claude-sonnet-5-5', effort='medium')
        self.assertEqual(shards.SHARDS.review_models(), {'source-reviewer': expected, 'source-document-reviewer': expected})
        body = (ROOT / '.claude/agents/source-reviewer.md').read_text()
        self.assertIn('Basis- und Schlussreview nutzen beide Sonnet 5.5 mit effort: medium.', body)

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
