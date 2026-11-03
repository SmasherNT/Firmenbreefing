"""Regional evidence, highest fixed stage, snapshot binding and first-page output."""
import copy
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest

from test_executive_summary import DEMO, RENDER, check_positioning, simulate_final_review
from test_render_briefing import Links, facts_only, refresh_basis, bundle
import test_prepare_facts as prep

PRESENCE=RENDER.CHECK.PRESENCE


class PresenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as temp:
            with redirect_stdout(io.StringIO()):DEMO.generate(temp)
            names=dict(manifest='facts-run',facts='review-packet',basis='review-basis',positioning='positioning',positioning_context='positioning-context',swot='swot',swot_context='swot-context',final='review-final',plan='comparison-plan')
            cls.original={k:json.loads((Path(temp)/(v+'.json')).read_text()) for k,v in names.items()}

    def setUp(self):
        self.b=copy.deepcopy(self.original)
        self.regions=next(v for v in self.b['facts']['module_views'] if v['role']=='portfolio')['regional_presence']

    def validate(self,regions=None):
        PRESENCE.validate(self.regions if regions is None else regions,lambda ids:None,self.b['manifest']['as_of'])

    def assessment(self,key='north'):
        return next(r for r in self.b['positioning']['interpretations'] if PRESENCE.is_assessment(r) and r['region_id']==key)

    def test_all_five_stages_and_unknown(self):
        self.validate()
        self.assertEqual([PRESENCE.eligible_stage(r) for r in self.regions],[5,4,3,2,1,None])
        self.assertEqual(check_positioning(self.b)['errors'],[])

    def test_own_sites_functions_and_production_requirements(self):
        region=copy.deepcopy(self.regions[0]);production,development=region['activities']
        development['kind']='office'
        self.assertEqual(PRESENCE.eligible_stage(region),4,'Same site is not two sites')
        development['site_id']='site-second';development['location']='Second own office'
        self.assertEqual(PRESENCE.eligible_stage(region),4, 'Another office does not add an operative function')
        production['kind']='office'
        self.assertEqual(PRESENCE.eligible_stage(region),3,'Multiple offices alone do not qualify for 5')

    def test_announcements_partners_jvs_customers_and_foreign_coverage(self):
        region=copy.deepcopy(self.regions[1]);activity=region['activities'][0]
        activity['status']='announced'
        self.assertIsNone(PRESENCE.eligible_stage(region))
        self.assertTrue(PRESENCE.planned_only(region))
        for operator in ('partner','jv'):
            activity.update(status='operational',operator=operator)
            self.assertEqual(PRESENCE.eligible_stage(region),2)
        activity.update(kind='customer_activity',operator='customer')
        self.assertEqual(PRESENCE.eligible_stage(region),1)
        self.assertEqual(PRESENCE.eligible_stage(self.regions[4]),1)

    def test_unfinished_development_does_not_upgrade_production(self):
        region=copy.deepcopy(self.regions[0]);region['activities'][1]['status']='announced'
        self.assertEqual(PRESENCE.eligible_stage(region),4)

    def test_highest_stage_and_sufficient_direct_dependencies_required(self):
        for score in (True,0,4,6,None):
            self.setUp();self.assessment()['score']=score
            self.assertTrue(any('highest supported stage' in e for e in check_positioning(self.b)['errors']))
        self.setUp();self.assessment()['depends_on']=self.regions[0]['activities'][0]['claim_ids']
        self.assertTrue(any('dependencies do not support' in e for e in check_positioning(self.b)['errors']))
        self.setUp();self.assessment()['depends_on']=['I20']
        self.assertTrue(any('facts directly' in e for e in check_positioning(self.b)['errors']))

    def test_each_region_once_and_canonical_method(self):
        for field,value in [('method_id','wrong'),('section','regions'),('region_id','missing'),('type','other')]:
            self.setUp();self.assessment()[field]=value
            self.assertTrue(check_positioning(self.b)['errors'])
        self.setUp();self.b['positioning']['interpretations'].append({**self.assessment(),'id':'I-RP-duplicate'})
        self.assertTrue(any('duplicate' in e for e in check_positioning(self.b)['errors']))
        self.setUp();self.b['positioning']['interpretations'].remove(self.assessment())
        self.assertTrue(any('each region exactly once' in e for e in check_positioning(self.b)['errors']))

    def test_null_gap_and_non_swot_basis(self):
        row=self.assessment('east');self.assertIsNone(row['score']);self.assertTrue(RENDER.CHECK.unassessed(row))
        row['coverage_note']=''
        self.assertTrue(check_positioning(self.b)['errors'])
        self.setUp()
        with self.assertRaisesRegex(ValueError,'not a SWOT basis'):
            RENDER.CHECK.prepare(self.b['manifest'],self.b['facts'],self.b['basis'],[],self.b['plan'],positioning=self.b['positioning'],positioning_context=self.b['positioning_context'],interpretation_ids=['I-RP-east'])

    def test_site_identity_dates_references_roles_and_invalid_rows(self):
        mutations=[lambda r:r[0]['activities'][1].update(location='Conflicting place'),
            lambda r:r[0]['activities'][1].update(site_id='duplicate-physical-place'),
            lambda r:r[0]['activities'][0].update(ownership_note=''),
            lambda r:r[0]['activities'][0].update(country='Outside region'),
            lambda r:r[0]['activities'][0].update(status_date='2027-01-01'),
            lambda r:r[0]['activities'][0].update(status_date='2026-02-30'),
            lambda r:r[0]['activities'][0].update(claim_ids=['UNKNOWN']),
            lambda r:r[0].update(score=5),lambda r:r[0].update(focus='yes'),
            lambda r:r[0]['activities'][0].update(operator='customer'),
            lambda r:r[0].update(countries={}),lambda r:r[0].update(activities=[None])]
        for mutation in mutations:
            self.setUp();mutation(self.regions)
            with self.assertRaises(ValueError):self.validate()

    def test_packet_mapping_and_required_review_ids(self):
        f=prep.FactsTests();f.setUp()
        region=copy.deepcopy(self.regions[3]);region['claim_ids']=['P001'];region['activities'][0]['claim_ids']=['P001']
        f.module['regional_presence']=[region]
        report,packet=prep.FACTS.build(f.manifest,[f.module]);self.assertEqual(report['errors'],[])
        self.assertIn('P001',report['required_full_review_ids']);self.assertEqual(packet['module_views'][0]['regional_presence'],[region])
        old=report['packet_fingerprint'];region['product_scope']='Changed scope'
        self.assertNotEqual(prep.FACTS.build(f.manifest,[f.module])[0]['packet_fingerprint'],old)
        manifest,module=f.market();module['regional_presence']=[region]
        self.assertTrue(any('belongs to portfolio' in e for e in prep.FACTS.build(manifest,[module],f.plan)[0]['errors']))

    def test_review_and_context_snapshots_block_changes(self):
        self.assessment()['reasoning']+=' changed'
        with self.assertRaisesRegex(ValueError,'review missing/stale'):RENDER.build(**self.b,full=True)
        self.setUp();self.regions[0]['product_scope']='Changed factual scope'
        with self.assertRaisesRegex(ValueError,'snapshot'):RENDER.build(**self.b,full=True)
        refresh_basis(self.b)
        with self.assertRaisesRegex(ValueError,'inventory/method changed'):check_positioning(self.b)

    def test_region_mapping_bound_in_i_fingerprint_and_upstream_swot(self):
        before=check_positioning(self.b)['fingerprints']['I-RP-north']
        self.regions[0]['label']='Changed reviewed name';refresh_basis(self.b)
        self.b['positioning_context']=RENDER.CHECK.prepare(self.b['manifest'],self.b['facts'],self.b['basis'],[r['id'] for r in self.b['positioning_context']['facts']],self.b['plan'],next(v for v in self.b['facts']['module_views'] if v['role']=='market')|{k:self.b['manifest'][k] for k in ('run_id','company','as_of')}|{'comparison_plan_version':1},include_portfolio=True,include_module_insights=True,include_presence=True)
        self.b['positioning']['input_fingerprint']=self.b['positioning_context']['fingerprint']
        after=check_positioning(self.b)['fingerprints']['I-RP-north'];self.assertNotEqual(before,after)
        context=RENDER.CHECK.prepare(self.b['manifest'],self.b['facts'],self.b['basis'],[],self.b['plan'],positioning=self.b['positioning'],positioning_context=self.b['positioning_context'],interpretation_ids=['I-RP-north'])
        swot={**self.b['swot'],'input_fingerprint':context['fingerprint'],'interpretations':[dict(id='S-RP',statement='Synthetic existing infrastructure',section='swot',category='Strengths',depends_on=['I-RP-north'],reasoning='Synthetic test of upstream dependency binding.',method='Qualitative',uncertainty='Synthetic only')]}
        report=RENDER.CHECK.validate_output(self.b['manifest'],self.b['facts'],self.b['basis'],context,swot,latest_positioning=self.b['positioning'],latest_positioning_context=self.b['positioning_context'],latest_plan=self.b['plan'])
        self.assertEqual(report['errors'],[])

    def test_sources_internal_links_placement_and_legacy_supplement(self):
        body=RENDER.build(**self.b,full=True)
        self.assertLess(body.index('id="cluster-analysis"'),body.index('id="regional-presence"'))
        self.assertLess(body.index('id="regional-presence"'),body.index('id="capability-matrix"'))
        self.assertEqual(body.count('class="rp-dot"')+body.count('class="rp-dot rp-filled"'),30)
        self.assertEqual(body.count('class="rp-profile"'),6)
        self.assertIn('Weitere belegte regionale Aktivitäten',body)
        self.assertIn('Europa · Partnerpräsenz',body.split('id="regional-presence"',1)[1].split('id="capability-matrix"',1)[0])
        self.assertNotIn('Unternehmenspräsenz',body.split('id="page-regions"',1)[1].split('id="page-sources"',1)[0])
        links=Links();links.feed(body);self.assertEqual(len(links.ids),len(set(links.ids)));self.assertTrue(set(links.anchors)<=set(links.ids))

    def test_facts_only_never_fabricates_a_stage_and_old_context_still_works(self):
        body=RENDER.build(**facts_only(self.b));self.assertIn('Unbewertet',body)
        self.assertNotIn('class="rp-dot rp-filled"',body)
        self.assertNotIn('id="regional-presence"',RENDER.build(**bundle()))

    def test_markup_in_regions_and_activities_escaped(self):
        self.regions[0]['label']='<img src=x>';self.regions[0]['activities'][0]['description']='<script>alert(1)</script>'
        refresh_basis(self.b);body=RENDER.build(**facts_only(self.b))
        self.assertNotIn('<img src=x>',body);self.assertNotIn('<script>alert(1)</script>',body)
        self.assertIn('&lt;img src=x&gt;',body);self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;',body)

    def test_development_service_and_integration_are_core_functions(self):
        region=copy.deepcopy(self.regions[0])
        region['activities'][0]['kind']='service'
        self.assertEqual(PRESENCE.eligible_stage(region),5, 'Development and service need no factory')
        region['activities']=region['activities'][1:]
        self.assertEqual(PRESENCE.eligible_stage(region),4, 'Own development is operative value creation')
        region=copy.deepcopy(self.regions[0]);region['activities'][1]['kind']='integration'
        self.assertEqual(PRESENCE.eligible_stage(region),4, 'Production plus integration is one function group')
        self.validate([region])

    def test_joint_and_sole_control_require_explicit_evidence(self):
        region=copy.deepcopy(self.regions[0])
        for activity in region['activities']:
            activity.update(operator='jv',control='unknown')
        self.assertEqual(PRESENCE.eligible_stage(region),2)
        for control in ('joint','sole'):
            for activity in region['activities']:
                activity.update(control=control,control_note='Synthetic contractual control rights',control_claim_ids=activity['claim_ids'])
            self.validate([region])
            self.assertEqual(PRESENCE.eligible_stage(region),5)
            self.assertIn('JV',PRESENCE.operator_label(region['activities'][0]))
        region['activities'][0]['control_claim_ids']=[]
        with self.assertRaises(ValueError):self.validate([region])
        region['activities'][0]['control_claim_ids']=['UNKNOWN']
        with self.assertRaises(ValueError):self.validate([region])

    def test_planned_only_has_no_operational_score(self):
        region=copy.deepcopy(self.regions[1]);region['activities'][0]['status']='announced'
        row=dict(id='I-planned',type='regional_presence',region_id=region['id'],section=PRESENCE.SECTION,
            method_id=PRESENCE.METHOD,depends_on=region['claim_ids'],score=None,assessment_status='geplant',coverage_note='Operational start not evidenced')
        self.assertEqual(PRESENCE.assessment_errors(row,[region]),[])
        row['score']=1
        self.assertTrue(PRESENCE.assessment_errors(row,[region]))
        row['score']=None;row['method_id']='regional-presence-v1'
        self.assertTrue(PRESENCE.assessment_errors(row,[region]))

    def test_method_explanation_includes_jv_and_planning(self):
        body=RENDER.build(**self.b,full=True)
        self.assertIn('Methodik v2',body)
        self.assertIn('vertraglich belegte gemeinsame Kontrolle',body)
        self.assertIn('50 Prozent',body)
        self.assertIn('Produktion und Integration',body)


if __name__=='__main__':unittest.main()
