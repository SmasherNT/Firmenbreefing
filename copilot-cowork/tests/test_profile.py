"""Profile mapping boundaries and source integrity."""
import copy
import json
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


class MultipleProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ProfileTests.setUpClass()
        cls.original = ProfileTests.original

    def setUp(self):
        PersonMediaTests.setUp(self)
        self.extra = json.loads(json.dumps(self.profile).replace('H1', 'H2').replace('Alex Example', 'Blair Example'))
        context = self.b['facts']['module_views'][0]
        context['additional_profiles'] = [self.extra]
        first_claim = next(c for c in self.b['facts']['claims'] if c['id'] == 'H1')
        self.b['facts']['claims'].append({**first_claim, 'id': 'H2',
            'statement': 'Blair Example leitet laut fiktivem Profil die Entwicklung.'})
        self.b['manifest']['person'] = 'Alex Example; Blair Example'
        refresh_basis(self.b)

    def test_separate_pages_share_module_frames_and_keep_independent_links(self):
        for dynamic in (False, True):
            with self.subTest(dynamic=dynamic):
                b = copy.deepcopy(self.b)
                if dynamic:
                    b['manifest']['focus_pages'] = []
                    for topic in b['manifest']['topics']:
                        topic['page'] = 'main'
                    for view in b['facts']['module_views']:
                        view.pop('market_dashboard', None)
                    refresh_basis(b)
                body = RENDER.build(**b)
                first = body.split('id="page-profile"', 1)[1].split('id="page-profile-2"', 1)[0]
                second = body.split('id="page-profile-2"', 1)[1].split('id="page-regions"' if not dynamic else 'id="page-sources"', 1)[0]
                for html, name, prefix in ((first, 'Alex Example', 'person-'), (second, 'Blair Example', 'person-2-')):
                    self.assertIn('<h2>' + name + '</h2>', html)
                    self.assertEqual(html.count('<section class="module profile-module">'), 1)
                    self.assertEqual(html.count('<section class="module profile-media"'), 1)
                    self.assertIn('</article></section><section class="module profile-media"', html)
                    self.assertIn('href="#' + prefix + 'source-1"', html)
                    self.assertIn('id="' + prefix + 'media-1"', html)
                    self.assertNotIn('class="pp-sources"', html)
                self.assertNotIn('<h2>Blair Example</h2>', first)
                self.assertNotIn('<h2>Alex Example</h2>', second)
                links = Links(); links.feed(body)
                self.assertEqual(len(links.ids), len(set(links.ids)))
                self.assertTrue(set(links.anchors) <= set(links.ids))
                sources = body.split('id="page-sources"', 1)[1]
                for prefix in ('person-', 'person-2-'):
                    self.assertIn('id="' + prefix + 'source-1"', sources)

    def test_additional_profile_changes_require_new_basis_review(self):
        self.extra['snapshot'][0]['value'] = 'Geänderte Verantwortung'
        with self.assertRaisesRegex(ValueError, 'snapshot missing/stale'):
            RENDER.build(**self.b)

    def test_additional_profile_requires_own_valid_person_claims(self):
        self.extra['claim_ids'] = ['M1']
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError, 'non-professional-person'):
            RENDER.build(**self.b)

    def test_duplicate_names_and_nonlist_additional_profiles_rejected(self):
        for value, error in (([{**self.extra, 'name': ' alex EXAMPLE '}], 'duplicate professional'),
                             ({'name': 'Blair Example'}, 'must be a list')):
            with self.subTest(value=value):
                self.b['facts']['module_views'][0]['additional_profiles'] = value
                refresh_basis(self.b)
                with self.assertRaisesRegex(ValueError, error):
                    RENDER.build(**self.b)

    def test_additional_profiles_without_primary_rejected(self):
        del self.b['facts']['module_views'][0]['profile']
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError, 'requires a primary profile'):
            RENDER.build(**self.b)
