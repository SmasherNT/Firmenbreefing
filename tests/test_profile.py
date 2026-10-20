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

class PersonMediaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ProfileTests.setUpClass()
        cls.original = ProfileTests.original
    def setUp(self):
        ProfileTests.setUp(self)
        self.profile['media']=[dict(id='sample', published_date=self.b['manifest']['as_of'],
            category='own', format='Synthetisches Interview', title='Test <Titel>',
            preview='Fiktive Vorschau', claim_ids=['H1'], access_note='Nur synthetischer Test')]
        refresh_basis(self.b)
    def test_source_page_and_no_region(self):
        body=RENDER.build(**self.b)
        profile=body.split('id="page-profile"',1)[1].split('id="page-regions"',1)[0]
        sources=body.split('id="page-sources"',1)[1]
        self.assertIn('Aktuelle Äußerungen &amp; Medienpräsenz der letzten vier Monate',profile)
        self.assertIn('Test &lt;Titel&gt;',profile)
        self.assertIn('pm-source-refs',profile)
        self.assertNotIn('<div class="pp-sources">',profile)
        self.assertNotIn('Regionaler Bezug',profile)
        self.assertIn('person-source-1',sources)
        self.assertIn('pp-evidence',sources)
    def test_old_or_future_publication_rejected(self):
        for published in ['2020-01-01','2099-01-01','2026-02-30']:
            self.profile['media'][0]['published_date']=published
            refresh_basis(self.b)
            with self.assertRaises(ValueError):RENDER.build(**self.b)
    def test_media_mapping_needs_current_review(self):
        self.profile['media'][0]['title']='Geändert'
        with self.assertRaisesRegex(ValueError,'snapshot missing/stale'):RENDER.build(**self.b)
    def test_quote_source_must_be_evidence(self):
        self.profile['media'][0].update(quote='Testzitat',quote_source_id='unknown',quote_location='Seite 1')
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError,'quote source'):RENDER.build(**self.b)


class MultiPersonTests(unittest.TestCase):
    """Several requested contacts: one profile page each, separate anchors."""
    @classmethod
    def setUpClass(cls):
        ProfileTests.setUpClass()
        cls.original = ProfileTests.original
    def setUp(self):
        ProfileTests.setUp(self)
        view = self.b['facts']['module_views'][0]
        first = view.pop('profile')
        h1 = next(c for c in self.b['facts']['claims'] if c['id'] == 'H1')
        self.b['facts']['claims'].append({**h1, 'id': 'H2', 'statement': 'Bea Example leitet den synthetischen Vertrieb.'})
        second = dict(name='Bea Example', claim_ids=['H2'], intro=dict(text='Synthetische Leitung', claim_ids=['H2']),
                      snapshot=[dict(label='Rolle', value='Vertrieb', claim_ids=['H2'])], career=[], expertise=[], responsibilities=[], media=[])
        view['profiles'] = [first, second]
        self.b['manifest']['person'] = [first['name'], 'Bea Example']
        refresh_basis(self.b)
    def test_one_page_per_person_with_unique_anchors(self):
        body = RENDER.build(**self.b)
        self.assertIn('id="page-profile-1"', body)
        self.assertIn('id="page-profile-2"', body)
        self.assertNotIn('id="page-profile"', body)
        second = body.split('id="page-profile-2"', 1)[1].split('id="page-regions"', 1)[0]
        self.assertIn('Bea Example', second)
        self.assertIn('person2-source-1', body.split('id="page-sources"', 1)[1])
        links = Links(); links.feed(body)
        self.assertEqual(len(links.ids), len(set(links.ids)))
        self.assertTrue(set(links.anchors) <= set(links.ids))
    def test_requested_person_without_profile_stays_visible(self):
        self.b['facts']['module_views'][0]['profiles'].pop()
        self.b['facts']['claims'] = [c for c in self.b['facts']['claims'] if c['id'] != 'H2']
        refresh_basis(self.b)
        second = RENDER.build(**self.b).split('id="page-profile-2"', 1)[1]
        self.assertIn('öffentlich nicht verifiziert', second.split('id="page-regions"', 1)[0])
    def test_shared_claims_and_unrequested_names_rejected(self):
        profiles = self.b['facts']['module_views'][0]['profiles']
        profiles[1]['claim_ids'].append('H1')
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError, 'share claims'):
            RENDER.build(**self.b)
        profiles[1]['claim_ids'].remove('H1'); profiles[1]['name'] = 'Unknown Person'
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError, 'not requested'):
            RENDER.build(**self.b)
    def test_profile_and_profiles_are_exclusive(self):
        view = self.b['facts']['module_views'][0]
        view['profile'] = view['profiles'][0]
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError, 'either profile or profiles'):
            RENDER.build(**self.b)
