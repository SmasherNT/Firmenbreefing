"""Market schema, derived comparisons and current A-review boundaries."""
import copy
import unittest

import test_prepare_facts as prep
import test_render_briefing as render
import test_interpretation as fixtures

MARKET = fixtures.load('market', 'market-html.py')
DEMO = fixtures.load('market_demo', '../examples/build-demo.py')


class MarketTests(unittest.TestCase):
    def setUp(self):
        self.data, self.rows = DEMO.market_example()
        self.ids = {cid for cid, _, _ in self.rows}
        self.used = set()

    def require(self, ids):
        if not isinstance(ids, list) or not ids or not set(ids) <= self.ids:
            raise ValueError('unknown claim')
        self.used.update(ids)

    def validate(self):
        MARKET.validate(self.data, self.require, '2026-10-09')

    def bundle(self):
        b = render.facts_only(render.bundle())
        first = b['facts']['claims'][0]
        b['facts']['claims'].extend({**copy.deepcopy(first), 'id': cid, 'statement': statement} for cid, statement, _ in self.rows)
        b['facts']['module_views'][0]['market_dashboard'] = self.data
        render.refresh_basis(b)
        return b

    def test_valid_data_derives_growth_and_counts(self):
        self.validate()
        countries = self.data['countries']
        self.assertAlmostEqual(MARKET.cagr(countries[0]['series']['investment']), (1.5**0.25-1)*100)
        self.assertLess(MARKET.cagr(countries[1]['series']['investment']), 0)
        self.assertIsNone(MARKET.cagr(countries[2]['series']['investment']))
        self.assertEqual(MARKET.programme_counts(countries[0]), dict(planning=1, announced=1, contracted=1, delivery=1))
        self.assertEqual(self.used, self.ids)

    def test_plans_forecasts_incompatible_and_zero_start_no_cagr(self):
        series = self.data['countries'][0]['series']['investment']
        for field, value in [('status','plan'), ('status','forecast'), ('comparable',False), ('value',None), ('value',0)]:
            test = copy.deepcopy(series);test[0][field] = value
            self.assertIsNone(MARKET.cagr(test), (field, value))

    def test_programme_unique_ids_and_status(self):
        for edit in ('duplicate', 'invalid'):
            self.setUp()
            programme = self.data['countries'][0]['programmes'][0]
            if edit == 'duplicate':
                self.data['countries'][1]['programmes'].append(copy.deepcopy(programme))
            else:
                programme['status'] = 'approved-contract'
            with self.assertRaisesRegex(ValueError, 'duplicate|status'):
                self.validate()

    def test_numbers_missing_years_and_comparison_metadata(self):
        mutations = [lambda d:d.update(years=[2021,2022,2022,2024,2025]),
            lambda d:d['countries'][0]['series']['investment'][0].update(value=float('nan')),
            lambda d:d['countries'][0]['series']['investment'][0].update(value=float('inf')),
            lambda d:d['countries'][0]['series']['investment'][0].update(value=-1),
            lambda d:d['countries'][0]['series']['investment'][0].update(value=True),
            lambda d:d['countries'][0]['series']['investment'][0].update(comparable=False),
            lambda d:d['countries'][2]['series']['investment'][0].update(missing_reason=''),
            lambda d:d['metrics'][0].update(price_basis='')]
        for mutation in mutations:
            self.setUp();mutation(self.data)
            with self.assertRaises(ValueError):self.validate()

    def test_roles_references_dates_and_boundaries(self):
        mutations = [lambda d:d['countries'][0]['roles'].pop('sensors'),
            lambda d:d['countries'][0]['roles']['sensors']['entries'][0].update(role='strong'),
            lambda d:d['countries'][0]['programmes'][0].update(status_date='2026-12-01'),
            lambda d:d['countries'][0]['programmes'][0].update(status_date='2026-02-30'),
            lambda d:d['countries'][0]['programmes'][0]['window'].update(start=2030,end=2026),
            lambda d:d['countries'][0]['programmes'][0].update(claim_ids=['UNKNOWN']),
            lambda d:d['countries'][0]['roles']['sensors']['entries'][0].update(score=5)]
        for mutation in mutations:
            self.setUp();mutation(self.data)
            with self.assertRaises(ValueError):self.validate()

    def test_malformed_rows_fail_cleanly(self):
        for key, value in [('countries',[None]), ('functions',{}), ('metrics',[]), ('timeline_years',True), ('years',None)]:
            self.setUp();self.data[key]=value
            with self.assertRaises(ValueError):self.validate()
        for mutation in [lambda d:d['metrics'][0].update(purpose=[]),
                lambda d:d['countries'][0]['programmes'][0].update(status={}),
                lambda d:d['countries'][0]['roles']['sensors']['entries'][0].update(role=[]),
                lambda d:d['countries'][0]['series']['investment'][0].update(year=2021.0)]:
            self.setUp();mutation(self.data)
            with self.assertRaises(ValueError):self.validate()

    def test_packet_includes_dashboard_and_all_full_review_ids(self):
        f=prep.FactsTests();f.setUp()
        manifest={**f.manifest,'selected_roles':['market']}
        module={**f.module,'role':'market','market_dashboard':self.data,
            'claims':[{**f.claim,'id':cid,'statement':statement} for cid,statement,_ in self.rows]}
        report, packet=prep.FACTS.build(manifest,[module])
        self.assertEqual(report['errors'],[])
        self.assertEqual(set(report['required_full_review_ids']),self.ids)
        self.assertEqual(packet['module_views'][0]['market_dashboard'],self.data)
        old=report['packet_fingerprint']
        self.data['countries'][0]['label']='Changed country mapping'
        self.assertNotEqual(prep.FACTS.build(manifest,[module])[0]['packet_fingerprint'],old)
        module['role']='portfolio'
        self.assertTrue(any('belongs to market' in e for e in prep.FACTS.build(f.manifest,[module])[0]['errors']))

    def test_review_snapshot_and_a_requirement_for_every_dashboard_claim(self):
        b=self.bundle();body=render.RENDER.build(**b)
        self.assertIn('briefing-market',body)
        self.data['countries'][0]['series']['investment'][0]['value']=21
        with self.assertRaisesRegex(ValueError,'snapshot'):render.RENDER.build(**b)
        render.refresh_basis(b)
        review=next(r for r in b['basis']['claims'] if r['id']=='M-D-north-w0')
        review['depth']='B'
        with self.assertRaisesRegex(ValueError,'Vollprüfung'):render.RENDER.build(**b)

    def test_static_details_direct_sources_internal_links_and_escaping(self):
        self.data['title']='<script>alert(1)</script>'
        self.data['countries'][0]['label']='Nord </script><img src=x>'
        body=render.RENDER.build(**self.bundle())
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;',body)
        self.assertNotIn('<img src=x>',body)
        self.assertIn('Genehmigungsobergrenze: 0,6',body)
        self.assertIn('Vertragswert: 0,4',body)
        self.assertIn('mk-growth-negative',body)
        self.assertIn('Beleg offen',body)
        self.assertIn('Quelle',body)
        anchors=render.Links();anchors.feed(body)
        self.assertEqual(len(anchors.ids),len(set(anchors.ids)))
        self.assertTrue(set(anchors.anchors)<=set(anchors.ids))

    def test_optional_segment_metric_no_invented_budget_substitute(self):
        second={**self.data['metrics'][0],'id':'segment','label':'Belegtes Segmentvolumen','purpose':'segment'}
        self.data['metrics'].append(second)
        for country in self.data['countries']:
            country['series']['segment']=copy.deepcopy(country['series']['investment'])
        self.validate()
        body=render.RENDER.build(**self.bundle())
        self.assertEqual(body.count('data-mk-chart="value"'),2)
        self.assertIn('Volumen im betrachteten Segment',body)

    def test_missing_comparison_has_no_invented_scale_and_real_zero_survives(self):
        for country in self.data['countries']:
            for row in country['series']['investment']:
                row.update(value=None,missing_reason='Keine Testdaten',claim_ids=[])
        body=render.RENDER.build(**self.bundle())
        self.assertEqual(body.count('Keine vergleichbaren Ist-Werte für diesen Vergleich im Paket.'),2)
        self.setUp()
        row=self.data['countries'][0]['series']['investment'][-1]
        row['value']=0
        self.assertEqual(MARKET.cagr(self.data['countries'][0]['series']['investment']),-100)
        self.assertIn('<span class="mk-value">0,0<small>Ist / berichtet',render.RENDER.build(**self.bundle()))

    def test_nonfinite_packet_is_reported_and_cannot_be_stamped(self):
        f=prep.FactsTests();f.setUp()
        manifest={**f.manifest,'selected_roles':['market']}
        module={**f.module,'role':'market','market_dashboard':self.data,
            'claims':[{**f.claim,'id':cid,'statement':statement} for cid,statement,_ in self.rows]}
        self.data['countries'][0]['series']['investment'][0]['value']=float('nan')
        report,_=prep.FACTS.build(manifest,[module])
        self.assertTrue(any('finite' in e for e in report['errors']))
        self.assertIsNone(report['packet_fingerprint'])


if __name__=='__main__':unittest.main()
