"""Portfolio boundaries: facts first, reviewed maturity later, no invented grades."""
import copy
import unittest
from html.parser import HTMLParser
import test_interpretation as fixtures
from test_render_briefing import Links, RENDER

CHECK = fixtures.CHECK

class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.InterpretationTests(); self.f.setUp()
        self.f.manifest['selected_roles'] = ['portfolio']
        self.f.facts['module_views'] = [dict(role='portfolio', products=[
            dict(id='kit', label='Test Kit', domain='Software', claim_ids=['M1']),
            dict(id='service', label='Test Service', domain='Services', claim_ids=['M2'])])]
        self.f.review['input_fingerprint'] = CHECK.digest(self.f.facts)
        self.ctx = CHECK.prepare(self.f.manifest, self.f.facts, self.f.review, [], include_portfolio=True)
        self.out = self.f.output(self.ctx)
        self.out['interpretations'] = [dict(id='IP1', type='product_maturity', product_id='kit',
            section='portfolio', statement='Test is reported', reasoning='Supplied test evidence',
            method='Highest documented milestone', uncertainty='Manufacturer only',
            method_id=CHECK.PORTFOLIO_METHOD, depends_on=['M1'], score=3,
            assessment_status='bewertet', next_stage_limit='No customer program documented'),
            dict(id='IP2', type='product_maturity', product_id='service', section='portfolio',
            statement='Maturity cannot be determined', reasoning='No documented milestone',
            method='Evidence boundary', uncertainty='', method_id=CHECK.PORTFOLIO_METHOD,
            depends_on=[], score=None, assessment_status='nicht eindeutig bestimmbar',
            coverage_note='Status not documented in supplied material')]

    def check(self, out=None):
        return self.f.check(self.ctx, out or self.out)

    def test_compact_context_and_valid_unknown(self):
        self.assertEqual(self.check()['errors'], [])
        self.assertEqual([p['id'] for p in self.ctx['portfolio']['products']], ['kit', 'service'])
        self.assertNotIn('matrix', self.ctx)
        self.assertNotIn('portfolio', CHECK.prepare(self.f.manifest, self.f.facts, self.f.review, ['M1']))

    def test_invalid_scores_and_unknown_with_number_rejected(self):
        for score in (0, 7, True, 3.5, '3', None):
            out = copy.deepcopy(self.out); out['interpretations'][0]['score'] = score
            self.assertTrue(self.check(out)['errors'], score)
        out = copy.deepcopy(self.out); out['interpretations'][1]['score'] = 1
        self.assertTrue(self.check(out)['errors'])

    def test_missing_duplicate_foreign_product_and_wrong_method_rejected(self):
        for change in ('missing', 'duplicate', 'foreign', 'method', 'wrong-facts'):
            out = copy.deepcopy(self.out)
            if change == 'missing': out['interpretations'].pop()
            if change == 'duplicate': out['interpretations'].append({**out['interpretations'][0], 'id': 'IP3'})
            if change == 'foreign': out['interpretations'][0]['product_id'] = 'other'
            if change == 'method': out['interpretations'][0]['method_id'] = 'invented'
            if change == 'wrong-facts': out['interpretations'][0]['depends_on'] = ['M2']
            self.assertTrue(self.check(out)['errors'], change)

    def test_inventory_change_invalidates_context(self):
        self.f.facts['module_views'][0]['products'][0]['domain'] = 'Unreviewed new domain'
        self.assertIn('portfolio inventory changed', self.check()['errors'])

    def test_unknown_product_cannot_support_swot(self):
        with self.assertRaisesRegex(ValueError, 'not a SWOT basis'):
            CHECK.prepare(self.f.manifest, self.f.facts, self.f.review, [],
                positioning=self.out, positioning_context=self.ctx, interpretation_ids=['IP2'])
        ctx = CHECK.prepare(self.f.manifest, self.f.facts, self.f.review, [],
                positioning=self.out, positioning_context=self.ctx, interpretation_ids=['IP1'])
        self.assertNotIn('portfolio', ctx)
        self.assertEqual([r['id'] for r in ctx['facts']], ['M1'])

    def test_factual_view_never_infers_maturity_and_preserves_sources(self):
        body = RENDER.build(self.f.manifest, self.f.facts, self.f.review)
        self.assertIn('Nicht eindeutig bestimmbar', body)
        matrix = body.split('<table class="pf-maturity-map">', 1)[1].split('</table>', 1)[0]
        self.assertNotIn('data-pf-item=', matrix)
        self.assertIn('https://example.org/1', body)
        links = Links(); links.feed(body)
        self.assertEqual(len(links.ids), len(set(links.ids)))
        self.assertTrue(set(links.anchors) <= set(links.ids))
        class Details(HTMLParser):
            def __init__(self): super().__init__(); self.rows=[]
            def handle_starttag(self, tag, attrs):
                if tag == 'details': self.rows.append(dict(attrs))
        parser=Details(); parser.feed(body)
        selected=[d for d in parser.rows if d.get('id') in {'portfolio-profiles', 'product-kit', 'product-service'}]
        self.assertEqual(len(selected),3)
        self.assertTrue(all('open' not in d for d in selected))

    def test_market_topics_on_third_page_and_fixed_four_pages(self):
        self.f.manifest['topics']=[dict(id='gcc', label='Gulf market', page='market')]
        self.f.manifest['market_title']='Golfstaaten'
        self.f.facts['module_views'][0]['topics']=[dict(id='gcc', label='Market fact', claim_ids=['M1'])]
        self.f.review['input_fingerprint']=CHECK.digest(self.f.facts)
        body=RENDER.build(self.f.manifest,self.f.facts,self.f.review)
        main=body.split('id="page-main"',1)[1].split('id="page-profile"',1)[0]
        market=body.split('id="page-regions"',1)[1].split('id="page-sources"',1)[0]
        self.assertNotIn('id="topic-0"',main)
        self.assertIn('id="topic-0"',market)
        self.assertIn('Markt-Deep-Dive · Golfstaaten',body)
        self.assertEqual(body.count('role="tabpanel"'),4)

class FullPortfolioTests(unittest.TestCase):
    def test_full_output_requires_portfolio_context_even_with_other_reviews(self):
        from test_executive_summary import ExecutiveSummaryTests, simulate_final_review
        ExecutiveSummaryTests.setUpClass()
        b = copy.deepcopy(ExecutiveSummaryTests.original)
        b['positioning_context'].pop('portfolio')
        b['positioning_context']['fingerprint'] = CHECK.digest({k: v for k, v in b['positioning_context'].items() if k != 'fingerprint'})
        b['positioning']['input_fingerprint'] = b['positioning_context']['fingerprint']
        b['positioning']['interpretations'] = [r for r in b['positioning']['interpretations'] if not CHECK.product_assessment(r)]
        b['swot_context'] = CHECK.prepare(b['manifest'], b['facts'], b['basis'], ['M5'])
        b['swot']['input_fingerprint'] = b['swot_context']['fingerprint']
        b['swot']['interpretations'] = [r for r in b['swot']['interpretations'] if r['id'] == 'S2']
        simulate_final_review(b)
        with self.assertRaisesRegex(ValueError, 'requires current portfolio context'):
            RENDER.build(**b, full=True)
        self.assertIn('Keine freigegebene Reifestufe', RENDER.build(**b))

if __name__ == '__main__': unittest.main()
