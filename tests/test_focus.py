"""Independent focus ownership, reviewed graphics and dynamic offline navigation."""
import copy
import json
import contextlib
import importlib.util
import io
import tempfile
from pathlib import Path
import unittest
import test_prepare_facts as facts_fixture
import test_render_briefing as render_fixture
import test_resume_run as resume_fixture

FACTS = facts_fixture.FACTS
RENDER = render_fixture.RENDER
FOCUS = RENDER.FOCUS
ROOT = Path(__file__).resolve().parents[1]


def page(fid='lkw', cid=None):
    cid = cid or 'F_' + fid + '_1'
    mapped = lambda **kw: dict(claim_ids=[cid], **kw)
    return dict(id=fid, label='Fokus ' + fid, overview='Synthetischer Überblick, keine reale Marktanalyse.', claim_ids=[cid],
        theses=[mapped(id='t' + str(i), label='Belegte Kernaussage ' + str(i)) for i in range(3)],
        charts=[mapped(id='volumen', type='bars', title='Synthetische Mengen', metric='Testmenge', unit='Stück', period='2025', scope='Testgrenze',
                       rows=[mapped(id='a', label='Anbieter A', value=12), mapped(id='b', label='Anbieter B', value=8)]),
                mapped(id='segmente', type='matrix', title='Synthetische Segmentübersicht', columns=[dict(id='x', label='Segment')],
                       rows=[mapped(id='a', label='Anbieter A', cells=[mapped(id='x', value='Aktiv')])]),
                mapped(id='rollen', type='structure', title='Synthetische Rollen', groups=[mapped(id='oem', label='OEM', items=[mapped(id='a', label='Anbieter A')])])],
        timeline=[mapped(id='e' + str(i), date='2026-09-' + str(i + 1).zfill(2), label='Synthetisches Ereignis ' + str(i), status='Angekündigt') for i in range(8)],
        gaps=['Keine realen Quellen geprüft: rein synthetische Testdaten.'])


def module(manifest, p, source):
    return {**{k:manifest[k] for k in ('run_id', 'company', 'as_of')},
        'schema_version':1, 'mode':'facts-v2', 'role':'focus', 'focus_id':p['id'],
        'scope':p['label'], 'status':'vollständig', 'claims':[dict(id='F_' + p['id'] + '_1',
        statement='Synthetische Testaussage', kind='Fakt', source_ids=[source['id']],
        evidence='Paraphrase: synthetischer Beleg', location='Testabschnitt', uncertainty='Keine reale Recherche')],
        'source_proposals':[source], 'gaps':[], 'coverage':[], 'focus_pages':[p]}


class FocusTests(unittest.TestCase):
    def setUp(self):
        self.fixture = facts_fixture.FactsTests(); self.fixture.setUp()
        self.pages = [page(), page('drohnen')]
        self.manifest = {**self.fixture.manifest, 'focus_pages':[{k:p[k] for k in ('id','label')} for p in self.pages]}
        self.modules = [self.fixture.module] + [module(self.manifest,p,self.fixture.source) for p in self.pages]

    def build(self):
        return FACTS.build(self.manifest, self.modules)

    def test_separate_jobs_keep_ownership_and_require_full_review(self):
        report, packet = self.build()
        self.assertEqual(report['errors'], [])
        self.assertEqual([v['role'] for v in packet['module_views']], ['portfolio','focus:lkw','focus:drohnen'])
        self.assertEqual(report['required_full_review_ids'], ['F_drohnen_1','F_lkw_1'])
        index = render_fixture.fixtures.load('focus_index_test', 'fact-index.py').build_index(self.manifest,self.modules)
        self.assertEqual({r['role'] for r in index['entries']}, {'portfolio','focus:lkw','focus:drohnen'})
        self.assertEqual(index['missing_roles'], [])

    def test_missing_duplicate_foreign_or_cross_owned_job_fails(self):
        for mutation in (lambda: self.modules.pop(), lambda: self.modules.append(copy.deepcopy(self.modules[-1])),
                         lambda: self.modules[-1].update(focus_id='foreign'),
                         lambda: self.modules[-1]['claims'][0].update(id='F_lkw_2'),
                         lambda: self.modules[-1].update(role='context')):
            self.setUp(); mutation()
            self.assertTrue(self.build()[0]['errors'])

    def test_unlimited_timeline_and_multiple_chart_types(self):
        checked = set()
        FOCUS.validate(self.manifest['focus_pages'], self.pages, lambda ids: checked.update(ids), self.manifest['as_of'])
        rendered = FOCUS.render(self.pages[0], lambda ids: '<a href="#' + ids[0] + '">Beleg</a>', self.manifest['as_of'])
        self.assertEqual(rendered.count('module focus-chart'), 3)
        self.assertEqual(rendered.count('class="focus-event"'), 8)
        self.assertLess(rendered.index('2026-09-08'), rendered.index('2026-09-01'))
        self.assertIn('focus-matrix', rendered)
        self.assertIn('focus-structure', rendered)
        self.assertNotIn('open>', rendered)

    def test_invalid_graphics_and_dates_are_blocked(self):
        mutations = [lambda p:p['charts'][0]['rows'][0].update(value=float('nan')),
                     lambda p:p['charts'][0]['rows'][0].update(value=-1),
                     lambda p:p['charts'][0].pop('period'),
                     lambda p:p['charts'][1]['rows'][0]['cells'][0].update(id='wrong'),
                     lambda p:p['timeline'][0].update(date='2026-04-08'),
                     lambda p:p['timeline'][0].update(date='2026-10-10'),
                     lambda p:p['timeline'][0].update(date=None),
                     lambda p:p['charts'][0]['rows'][0].update(claim_ids=['unknown'])]
        def require(ids):
            if not ids or any(c not in {'F_lkw_1','F_drohnen_1'} for c in ids): raise ValueError('unknown refs')
        for mutation in mutations:
            pages = copy.deepcopy(self.pages);mutation(pages[0])
            with self.assertRaises(ValueError): FOCUS.validate(self.manifest['focus_pages'], pages, require, self.manifest['as_of'])
        self.assertEqual(str(FOCUS.six_months_before('2026-08-31')), '2026-02-28')
        self.assertEqual(str(FOCUS.six_months_before('2024-08-31')), '2024-02-29')

    def test_dynamic_pages_order_sources_and_no_placeholder(self):
        b = render_fixture.bundle()
        b['manifest']['focus_pages'] = [{k:p[k] for k in ('id','label')} for p in self.pages]
        for p in self.pages:
            b['facts']['claims'].append({**b['facts']['claims'][0], 'id':'F_' + p['id'] + '_1'})
            b['facts']['module_views'].append(dict(role='focus:' + p['id'], focus_pages=[p], gaps=[], coverage=[]))
        render_fixture.refresh_basis(b)
        output = RENDER.build(**render_fixture.facts_only(b))
        parser = render_fixture.Links();parser.feed(output)
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        self.assertTrue(set(parser.anchors) <= set(parser.ids))
        self.assertLess(output.index('id="page-focus-lkw"'), output.index('id="page-focus-drohnen"'))
        self.assertLess(output.index('id="page-focus-drohnen"'), output.index('id="page-sources"'))
        self.assertNotIn('id="page-regions"', output)
        self.assertNotIn('id="page-profile"', output)
        self.assertIn('04 / 04', output)
        b['manifest']['person'] = 'Synthetische Person'
        output = RENDER.build(**render_fixture.facts_only(b))
        self.assertLess(output.index('id="page-profile"'), output.index('id="page-focus-lkw"'))
        self.assertIn('05 / 05', output)
        b['manifest']['focus_pages'] = []
        b['facts']['module_views'] = [b['facts']['module_views'][0]]
        render_fixture.refresh_basis(b)
        output = RENDER.build(**render_fixture.facts_only(b))
        self.assertNotIn('page-focus-', output)
        self.assertNotIn('page-regions', output)
        self.assertIn('03 / 03', output)

    def test_stale_mapping_unreviewed_fact_and_missing_page_fail(self):
        b = render_fixture.bundle(); p = page(cid='M1')
        b['manifest']['focus_pages'] = [{k:p[k] for k in ('id','label')}]
        b['facts']['module_views'].append(dict(role='focus:lkw', focus_pages=[p]))
        render_fixture.refresh_basis(b)
        b['facts']['module_views'][-1]['focus_pages'][0]['charts'][0]['title'] += ' Changed'
        with self.assertRaisesRegex(ValueError,'snapshot'): RENDER.build(**render_fixture.facts_only(b))
        render_fixture.refresh_basis(b)
        b['basis']['claims'] = []
        with self.assertRaises(ValueError): RENDER.build(**render_fixture.facts_only(b))
        render_fixture.refresh_basis(b); b['facts']['module_views'].pop()
        render_fixture.refresh_basis(b)
        with self.assertRaisesRegex(ValueError,'module_views'): RENDER.build(**render_fixture.facts_only(b))

    def test_focus_jobs_have_individual_resume_stages_and_dependencies(self):
        fixture = resume_fixture.ResumeRunTests(); fixture.setUp(); self.addCleanup(fixture.doCleanups)
        manifest = json.loads(fixture.manifest.read_text())
        manifest['focus_pages'] = self.manifest['focus_pages']
        fixture.put('manifest', manifest)
        fixture.state.unlink()
        resume_fixture.RESUME.init(fixture.manifest, fixture.request, fixture.cache.root, fixture.state)
        self.assertIn('focus:lkw', fixture.status()['stages'])
        self.assertIn('focus:drohnen', fixture.status()['stages'])
        fixture.save('portfolio', {}, {'module':fixture.module})
        focus_modules = [module(manifest, p, fixture.fixture.sources[0]) for p in self.pages]
        focus_paths = {m['focus_id']:fixture.put('focus-' + m['focus_id'], m) for m in focus_modules}
        fixture.save('focus:lkw', {}, {'module':focus_paths['lkw']})
        self.assertEqual(fixture.status()['stages']['focus:lkw']['status'], 'reusable')
        self.assertEqual(fixture.status()['stages']['focus:drohnen']['status'], 'pending')
        fixture.save('focus:drohnen', {}, {'module':focus_paths['drohnen']})
        report, packet = FACTS.build(manifest, [fixture.fixture.module] + focus_modules)
        self.assertEqual(report['errors'], [])
        fixture.put('facts', packet); fixture.put('validation', report)
        inputs = {'portfolio':fixture.module, **{'focus:' + k:v for k,v in focus_paths.items()}}
        fixture.save('facts', inputs, {'facts':fixture.facts, 'validation':fixture.validation})
        self.assertEqual(fixture.status()['stages']['facts']['status'], 'reusable')
        focus_modules[0]['focus_pages'][0]['overview'] += ' Changed'
        fixture.put('focus-lkw', focus_modules[0])
        status = fixture.status()['stages']
        self.assertNotEqual(status['focus:lkw']['status'], 'reusable')
        self.assertEqual(status['focus:drohnen']['status'], 'reusable')
        self.assertNotEqual(status['facts']['status'], 'reusable')

    def test_focus_facts_cannot_be_sent_to_opus_interpretation(self):
        b = render_fixture.bundle(); p = page()
        b['facts']['claims'].append({**b['facts']['claims'][0], 'id':'F_lkw_1'})
        render_fixture.refresh_basis(b)
        with self.assertRaisesRegex(ValueError,'outside positioning'):
            RENDER.CHECK.prepare(b['manifest'], b['facts'], b['basis'], ['F_lkw_1'])

    def test_full_briefing_preserves_company_interpretations_with_focus_pages(self):
        spec = importlib.util.spec_from_file_location('focus_full_fixture', ROOT/'examples/build-demo.py')
        demo = importlib.util.module_from_spec(spec); spec.loader.exec_module(demo)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with contextlib.redirect_stdout(io.StringIO()): demo.generate(root)
            def read(name): return json.loads((root/(name + '.json')).read_text())
            b = dict(manifest=read('facts-run'), facts=read('review-packet'), basis=read('review-basis'),
                positioning=read('positioning'), positioning_context=read('positioning-context'),
                swot=read('swot'), swot_context=read('swot-context'), final=read('review-final'), plan=read('comparison-plan'), full=True)
            b['manifest']['focus_pages'] = self.manifest['focus_pages']
            for topic in b['manifest'].get('topics', []): topic['page'] = 'main'
            for view in b['facts']['module_views']: view.pop('market_dashboard', None)
            for focus in self.pages:
                job = module(b['manifest'], focus, b['facts']['sources'][0])
                b['facts']['claims'].extend(job['claims'])
                b['facts']['module_views'].append(dict(role='focus:' + focus['id'], focus_pages=[focus]))
                b['facts']['module_context'].append(dict(role='focus:' + focus['id'], status='vollständig'))
            render_fixture.refresh_basis(b)
            html = RENDER.build(**b)
            self.assertIn('page-focus-lkw', html)
            self.assertIn('page-focus-drohnen', html)
            self.assertIn('SWOT', html)
            self.assertNotIn('id="page-regions"', html)
