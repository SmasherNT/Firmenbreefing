"""Compact topic cards preserve evidence and bind display text to reviews."""
import copy
import unittest
import test_executive_summary as fixtures
from test_render_briefing import RENDER, facts_only, refresh_basis, Links

class TopicDesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixtures.ExecutiveSummaryTests.setUpClass()
        cls.original=fixtures.ExecutiveSummaryTests.original
    def setUp(self):
        self.b=facts_only(copy.deepcopy(self.original))
        self.row=next(v for v in self.b['facts']['module_views'] if v['role']=='portfolio')['topics'][0]
    def test_cards_retain_full_claims_and_direct_sources(self):
        body=RENDER.build(**self.b)
        self.assertIn('class="es-entry topic-card"',body)
        self.assertIn('Integration als Softwaremodul',body)
        self.assertIn('Das fiktive Inspection Kit wird als Softwaremodul angeboten.',body)
        self.assertIn('https://example.org/company',body)
        links=Links();links.feed(body)
        self.assertTrue(set(links.anchors)<=set(links.ids))
        self.assertEqual(len(links.ids),len(set(links.ids)))
    def test_changed_preview_invalidates_basis_review(self):
        self.row['preview']='Unreviewed changed preview'
        with self.assertRaisesRegex(ValueError,'snapshot missing/stale'):RENDER.build(**self.b)
    def test_long_or_empty_compact_fields_rejected(self):
        for key,value in [('headline','x'*73),('preview','x'*161),('preview','')]:
            b=copy.deepcopy(self.b);r=next(v for v in b['facts']['module_views'] if v['role']=='portfolio')['topics'][0];r[key]=value;refresh_basis(b)
            with self.assertRaisesRegex(ValueError,'topic '+key+' invalid'):RENDER.build(**b)
    def test_swot_categories_have_semantic_color_hooks(self):
        body=RENDER.build(**self.original,full=True)
        for key in ['Strengths','Weaknesses','Opportunities','Threats']:
            self.assertIn('data-swot="'+key+'"><h3>',body)

if __name__=='__main__':unittest.main()
