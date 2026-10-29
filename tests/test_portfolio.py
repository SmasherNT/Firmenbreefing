"""Portfolio boundaries: facts first, reviewed status later, no invented stages."""
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
            section='portfolio', statement='Prototype test is reported', reasoning='Supplied test evidence',
            method='Highest documented stage', uncertainty='Manufacturer only',
            method_id=CHECK.PORTFOLIO_METHOD, depends_on=['M1'], stage='prototype', stage_basis=['M1'],
            assessment_status='bewertet', next_stage_limit='No series production documented'),
            dict(id='IP2', type='product_maturity', product_id='service', section='portfolio',
            statement='Status cannot be determined', reasoning='No documented status',
            method='Evidence boundary', uncertainty='', method_id=CHECK.PORTFOLIO_METHOD,
            depends_on=[], stage=None, assessment_status='nicht eindeutig bestimmbar',
            coverage_note='Status not documented in supplied material')]

    def starred(self):
        out = copy.deepcopy(self.out)
        out['interpretations'][0].update(stage='operation', next_stage_limit='',
            also_previous=dict(stage='series', basis=['M1'], note='Series production continues'))
        return out

    def check(self, out=None):
        return self.f.check(self.ctx, out or self.out)

    def test_compact_context_and_valid_unknown(self):
        self.assertEqual(self.check()['errors'], [])
        self.assertEqual([p['id'] for p in self.ctx['portfolio']['products']], ['kit', 'service'])
        self.assertNotIn('matrix', self.ctx)
        self.assertNotIn('portfolio', CHECK.prepare(self.f.manifest, self.f.facts, self.f.review, ['M1']))

    def test_invalid_stages_and_unknown_with_stage_rejected(self):
        for stage in (None, 'unknown', 'serie', 3, 'test'):
            out = copy.deepcopy(self.out); out['interpretations'][0]['stage'] = stage
            self.assertTrue(self.check(out)['errors'], stage)
        for change in ('score', 'basis-empty', 'basis-foreign', 'limit'):
            out = copy.deepcopy(self.out); row = out['interpretations'][0]
            if change == 'score': row['score'] = 2
            if change == 'basis-empty': row['stage_basis'] = []
            if change == 'basis-foreign': row['stage_basis'] = ['M2']
            if change == 'limit': row['next_stage_limit'] = ''
            self.assertTrue(self.check(out)['errors'], change)
        out = copy.deepcopy(self.out); out['interpretations'][1]['stage'] = 'series'
        self.assertTrue(self.check(out)['errors'])

    def test_star_only_for_still_active_direct_previous_stage(self):
        self.assertEqual(self.check(self.starred())['errors'], [])
        for change in ('on-prototype', 'skip-stage', 'no-note', 'no-basis', 'basis-outside', 'on-unknown'):
            out = self.starred(); row = out['interpretations'][0]; extra = row['also_previous']
            if change == 'on-prototype': row.update(stage='prototype', next_stage_limit='x'); extra['stage'] = 'announced'
            if change == 'skip-stage': extra['stage'] = 'prototype'
            if change == 'no-note': extra['note'] = ''
            if change == 'no-basis': extra['basis'] = []
            if change == 'basis-outside': extra['basis'] = ['M2']
            if change == 'on-unknown': out['interpretations'][1]['also_previous'] = dict(stage='series', basis=['M1'], note='x')
            self.assertTrue(self.check(out)['errors'], change)

    def test_legacy_six_stage_context_still_validates(self):
        ctx = copy.deepcopy(self.ctx)
        ctx['portfolio'] = CHECK.portfolio_context(self.f.facts, CHECK.LEGACY_PORTFOLIO_METHOD)
        ctx['fingerprint'] = CHECK.digest({k: v for k, v in ctx.items() if k != 'fingerprint'})
        out = copy.deepcopy(self.out); out['input_fingerprint'] = ctx['fingerprint']
        for row in out['interpretations']:
            for key in ('stage', 'stage_basis'): row.pop(key, None)
            row['method_id'] = CHECK.LEGACY_PORTFOLIO_METHOD
        out['interpretations'][0]['score'] = 3; out['interpretations'][1]['score'] = None
        self.assertEqual(self.f.check(ctx, out)['errors'], [])
        out['interpretations'][0]['score'] = 7
        self.assertTrue(self.f.check(ctx, out)['errors'])

    def test_status_matrix_places_highest_stage_and_explains_star(self):
        claims = {c: dict(statement='Fact ' + c, kind='Fakt', uncertainty='') for c in ('M1', 'M2')}
        rows = {r['product_id']: r for r in self.starred()['interpretations']}
        body = RENDER.PORTFOLIO.render(self.ctx['portfolio'], rows, claims, lambda c: '', lambda ids: '')
        header = body.split('<tbody>', 1)[1].split('</tbody>', 1)[0]
        kit_row = header.split('data-pf-group="Software"', 1)[1].split('</tr>', 1)[0]
        cells = kit_row.split('<td')[1:]
        self.assertEqual(len(cells), 5)
        self.assertIn('data-pf-item="kit"', cells[3])
        self.assertIn('pf-star', cells[3])
        service_row = header.split('data-pf-group="Services"', 1)[1].split('</tr>', 1)[0]
        self.assertIn('data-pf-item="service"', service_row.split('<td')[5])
        profile = body.split('id="product-kit"', 1)[1].split('</details>', 1)[0]
        self.assertIn('* Zusätzlich: Serienproduktion', profile)
        self.assertIn('Series production continues', profile)
        self.assertIn('value="star"', body)
        self.assertIn('Die vier Statusstufen', body)
        legacy = dict(self.ctx['portfolio'], method_id=CHECK.LEGACY_PORTFOLIO_METHOD, stages=CHECK.LEGACY_PORTFOLIO_STAGES)
        old = RENDER.PORTFOLIO.render(legacy, {'kit': dict(self.out['interpretations'][0], score=3)}, claims, lambda c: '', lambda ids: '')
        self.assertIn('Die sechs Reifestufen', old)
        self.assertNotIn('class="pf-star"', old)

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
        self.assertIn('Noch nicht eingeordnet', body)
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
        self.assertIn('Noch nicht eingeordnet', RENDER.build(**b))

if __name__ == '__main__': unittest.main()
