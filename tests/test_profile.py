"""Profile mapping boundaries and source integrity."""
import copy
import unittest
import test_executive_summary as summary_fixtures
from test_render_briefing import RENDER, facts_only, refresh_basis, Links

class ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        summary_fixtures.ExecutiveSummaryTests.setUpClass()
        cls.original=summary_fixtures.ExecutiveSummaryTests.original
    def setUp(self):
        self.b=facts_only(copy.deepcopy(self.original))
        self.profile=self.b['facts']['module_views'][0]['profile']
    def test_profile_mapping_change_requires_new_basis_review(self):
        self.profile['snapshot'][0]['value']='Changed responsibility'
        with self.assertRaisesRegex(ValueError,'snapshot missing/stale'):
            RENDER.build(**self.b)
    def test_cannot_reference_unlisted_or_nonperson_claims(self):
        for ids in [['M1'],['unknown'],[]]:
            self.profile['snapshot'][0]['claim_ids']=ids
            refresh_basis(self.b)
            with self.assertRaises(ValueError):RENDER.build(**self.b)
    def test_missing_career_is_not_inferred_and_legacy_claims_retained(self):
        self.profile.clear();self.profile.update(name='Alex Example',claim_ids=['H1'])
        refresh_basis(self.b);body=RENDER.build(**self.b)
        self.assertIn('Weitere belegte Profilangaben',body)
        self.assertIn('keine freigegebenen Angaben',body)
        self.assertIn('Alex Example verantwortet',body)
        self.assertIn('https://example.org/company',body)
    def test_escaped_text_source_and_claim_links(self):
        self.profile['intro']['text']='<script>bad()</script>'
        refresh_basis(self.b);body=RENDER.build(**self.b)
        self.assertNotIn('<script>bad()',body)
        self.assertIn('&lt;script&gt;bad()',body)
        links=Links();links.feed(body)
        self.assertEqual(len(links.ids),len(set(links.ids)))
        self.assertTrue(set(links.anchors)<=set(links.ids))
    def test_empty_career_cells_rejected(self):
        self.profile['career']=[dict(period='',organization='Org',role='Lead',context='Context',claim_ids=['H1'])]
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError,'requires period'):RENDER.build(**self.b)

if __name__=='__main__':unittest.main()
