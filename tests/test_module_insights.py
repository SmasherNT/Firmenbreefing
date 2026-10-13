"""Module card limits, reviewed fact/insight fields, placement and fallbacks."""
import copy
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest

from test_executive_summary import DEMO, RENDER, check_positioning, simulate_final_review
from test_render_briefing import Links, bundle


class ModuleInsightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as temp:
            with redirect_stdout(io.StringIO()):DEMO.generate(temp)
            names=dict(manifest='facts-run',facts='review-packet',basis='review-basis',positioning='positioning',
                positioning_context='positioning-context',swot='swot',swot_context='swot-context',final='review-final',plan='comparison-plan')
            cls.original={k:json.loads((Path(temp)/(v+'.json')).read_text()) for k,v in names.items()}

    def setUp(self):self.b=copy.deepcopy(self.original)

    def cards(self,module=None):
        return [r for r in self.b['positioning']['interpretations'] if r.get('type')=='module_insight' and (module is None or r['module']==module)]

    def test_all_modules_and_internal_links_have_full_reviewed_content(self):
        body=RENDER.build(**self.b,full=True)
        self.assertEqual(body.count('class="module-insights"'),3)
        self.assertEqual(body.count('class="mi-card"'),7)
        self.assertIn('Insight · Analysteninterpretation',body)
        self.assertIn('Herleitung · Analysteninterpretation',body)
        self.assertIn('https://example.org/partner',body)
        self.assertIn('Belegstelle:',body)
        for module in ('portfolio','cluster','market'):
            self.assertIn('id="insights-'+module+'"',body)
        links=Links();links.feed(body)
        self.assertEqual(len(links.ids),len(set(links.ids)))
        self.assertTrue(set(links.anchors)<=set(links.ids))
        before_regions=body.split('id="page-regions"',1)[0]
        self.assertEqual(before_regions.count('class="mi-card"'),7)

    def test_one_two_three_cards_do_not_pad(self):
        for count in (1,2,3):
            self.setUp()
            remove=self.cards('portfolio')[count:]
            self.b['positioning']['interpretations']=[r for r in self.b['positioning']['interpretations'] if r not in remove]
            simulate_final_review(self.b)
            body=RENDER.build(**self.b,full=True)
            self.assertEqual(body.count('class="mi-card"'),count+4)
            self.assertIn('id="insights-portfolio" data-insight-module="portfolio"><h3>Keyfacts &amp; Insights</h3><div class="mi-grid" data-count="'+str(count)+'"',body)

    def test_four_cards_or_invalid_order_rejected(self):
        row=self.cards('portfolio')[0]
        self.b['positioning']['interpretations'].append({**row,'id':'I-MI-extra','display_order':4})
        self.assertTrue(any('three' in e for e in check_positioning(self.b)['errors']))
        for order in (True,0,2,4,[],None):
            self.setUp();self.cards('portfolio')[0]['display_order']=order
            self.assertTrue(any('order' in e for e in check_positioning(self.b)['errors']))

    def test_fact_references_are_direct_unique_and_in_dependencies(self):
        for refs in ([],['I20'],['UNKNOWN'],['P4','P4'],['P3'],[{}]):
            self.setUp();self.cards('portfolio')[0]['fact_claim_ids']=refs
            self.assertTrue(any('fact_claim_ids' in e for e in check_positioning(self.b)['errors']),refs)

    def test_background_fact_and_stale_source_block_cards(self):
        next(r for r in self.b['basis']['claims'] if r['id']=='C1')['depth']='B'
        self.assertTrue(any('Vollprüfung A' in e for e in check_positioning(self.b)['errors']))
        self.setUp();self.b['facts']['sources'][0]['title']+=' changed'
        self.assertTrue(check_positioning(self.b)['errors'])

    def test_changed_visible_card_fields_and_mapping_require_review(self):
        for field in ('headline','fact_text','statement'):
            self.setUp();self.cards('portfolio')[0][field]+=' changed'
            with self.assertRaisesRegex(ValueError,'review missing/stale'):RENDER.build(**self.b,full=True)
        self.setUp();row=self.cards('portfolio')[-1];row['module']='cluster';row['display_order']=3
        with self.assertRaisesRegex(ValueError,'review missing/stale'):RENDER.build(**self.b,full=True)
        self.setUp();row=self.cards('portfolio')[0];row['depends_on'].append('P1');row['fact_claim_ids'].append('P1')
        with self.assertRaisesRegex(ValueError,'review missing/stale'):RENDER.build(**self.b,full=True)

    def test_invalid_fields_types_and_module_are_rejected(self):
        for field,value in [('headline',''),('fact_text','x'*181),('statement','x'*181),
                ('module',[]),('module','context'),('section',None),('section','portfolio'),
                ('type','matrix_cell'),('score',3)]:
            self.setUp();self.cards('portfolio')[0][field]=value
            self.assertTrue(check_positioning(self.b)['errors'],(field,value))

    def test_explicit_gap_is_required_and_displays_only_system_note(self):
        self.b['positioning']['interpretations']=[r for r in self.b['positioning']['interpretations'] if r not in self.cards('portfolio')]
        self.assertTrue(any('explicit insight gap' in e for e in check_positioning(self.b)['errors']))
        self.b['positioning']['module_insight_gaps']=[dict(module='portfolio',reason='INTERNAL REVIEW REASON; NOT A DISPLAYED COMPANY CLAIM')]
        simulate_final_review(self.b)
        body=RENDER.build(**self.b,full=True)
        self.assertEqual(body.count('class="mi-card"'),4)
        self.assertIn('keine freigegebenen zusätzlichen Keyfacts',body)
        self.assertNotIn('INTERNAL REVIEW REASON',body)
        self.b['positioning']['module_insight_gaps'].append(dict(module='portfolio',reason='duplicate'))
        self.assertTrue(any('duplicate' in e for e in check_positioning(self.b)['errors']))

    def test_gap_and_cards_cannot_coexist(self):
        self.b['positioning']['module_insight_gaps']=[dict(module='portfolio',reason='gap')]
        self.assertTrue(any('coexist' in e for e in check_positioning(self.b)['errors']))

    def test_no_duplicate_general_interpretation_cards_or_scripts(self):
        body=RENDER.build(**self.b,full=True)
        heading='Einordnung · Technologie, Industrie &amp; Markt'
        if heading in body:
            extra=body.split(heading,1)[1].split('SWOT',1)[0]
            self.assertNotIn('I-MI-',extra)
        self.assertEqual(body.count('id="insights-market"'),1)
        self.assertNotIn('<script src=',body)

    def test_legacy_context_remains_usable_without_invented_cards(self):
        body=RENDER.build(**bundle())
        self.assertNotIn('class="module-insights"',body)
        with self.assertRaisesRegex(ValueError,'delegated context'):
            b=self.b;b['positioning_context'].pop('module_insights');b['positioning_context']['fingerprint']=RENDER.CHECK.digest({k:v for k,v in b['positioning_context'].items() if k!='fingerprint'});b['positioning']['input_fingerprint']=b['positioning_context']['fingerprint'];RENDER.build(**b)

    def test_context_flag_is_selective_and_not_for_swot(self):
        b=bundle()
        context=RENDER.CHECK.prepare(b['manifest'],b['facts'],b['basis'],['M1'],include_module_insights=True)
        self.assertEqual(context['module_insights']['modules'],['market'])
        self.assertEqual([r['id'] for r in context['facts']],['M1'])
        with self.assertRaisesRegex(ValueError,'not SWOT'):
            RENDER.CHECK.prepare(b['manifest'],b['facts'],b['basis'],['M1'],positioning=b['positioning'],include_module_insights=True)

    def test_markup_is_escaped(self):
        row=self.cards('portfolio')[0];row['headline']='<script>alert(1)</script>';row['fact_text']='<img src=x>';row['statement']='Insight <b>text</b>'
        simulate_final_review(self.b);body=RENDER.build(**self.b,full=True)
        self.assertNotIn('<img src=x>',body);self.assertNotIn('<script>alert(1)</script>',body)
        self.assertIn('&lt;img src=x&gt;',body);self.assertIn('Insight &lt;b&gt;text&lt;/b&gt;',body)

    def test_market_without_matrix_has_a_first_page_card_section(self):
        b=bundle()
        context=RENDER.CHECK.prepare(b['manifest'],b['facts'],b['basis'],['M1'],include_module_insights=True)
        row=dict(id='I-MI-only',type='module_insight',section='module_insights',module='market',display_order=1,
            headline='Synthetic market point',fact_text='Manufacturer reports test 1.',fact_claim_ids=['M1'],
            statement='The supplied test report supports a documented test, not a customer deployment.',depends_on=['M1'],
            reasoning='Bounded interpretation of the supplied synthetic test evidence.',method='Qualitative',uncertainty='Synthetic fixture only')
        output={**b['positioning'],'input_fingerprint':context['fingerprint'],'interpretations':[row]}
        output.pop('plan_fingerprint',None)
        report=RENDER.CHECK.validate_output(b['manifest'],b['facts'],b['basis'],context,output)
        self.assertEqual(report['errors'],[])
        draft={k:b['manifest'][k] for k in ('run_id','company','as_of')}
        draft.update(schema_version=1,phase='final',status='freigegeben',material_errors=[],claims=[dict(id=row['id'],depth='A',status='geprüft')])
        final=DEMO.STAMP.stamp(draft,report)
        body=RENDER.build(manifest=b['manifest'],facts=b['facts'],basis=b['basis'],positioning=output,positioning_context=context,final=final)
        self.assertIn('id="market-overview"',body)
        self.assertIn('id="insights-market"',body)
        self.assertNotIn('id="capability-matrix"',body)


if __name__=='__main__':unittest.main()
