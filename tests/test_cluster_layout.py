"""Actor overview is distinct from the graph and uses only the current data."""
import unittest
import test_render_briefing as fixtures

class ClusterLayoutTests(unittest.TestCase):
    def test_actor_overview_is_single_actor_and_source_preserving(self):
        b = fixtures.facts_only(fixtures.bundle())
        fixtures.add_network(b)
        node = b['facts']['network']['nodes'][1]
        node['label'] = '<Actor & Co>'
        fixtures.refresh_basis(b)
        output = fixtures.RENDER.build(**b)
        actor_part = output.split('id="cnt-view-tables"',1)[1].split('id="cnt-view-graph"',1)[0]
        self.assertEqual(actor_part.count('data-cnt-node='),1)
        self.assertEqual(actor_part.count('class="cnt-actor-table"'),4)
        self.assertIn('&lt;Actor &amp; Co&gt;',actor_part)
        self.assertIn('Originalquellen',actor_part)
        self.assertIn('Legende der Akteursfarben',actor_part)
        self.assertNotIn('data-cnt-edge',actor_part)
        self.assertNotIn('Von → Zu',actor_part)
        self.assertIn('columns=5',output)
        self.assertIn('const nodeRadius=14',output)
        self.assertIn('class="data-gaps"><summary',output)
        self.assertNotIn('__CLUSTER_ACTOR_TABLES__',output)

if __name__=='__main__':
    unittest.main()
