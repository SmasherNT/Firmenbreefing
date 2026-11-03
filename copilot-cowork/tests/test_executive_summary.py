"""Summary contract, review binding and 4–6-card full output using synthetic data."""
import copy
import importlib.util
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest

from test_render_briefing import Links, RENDER

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('summary_demo', ROOT / 'examples/build-demo.py')
DEMO = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DEMO)


def check_positioning(b):
    return RENDER.CHECK.validate_output(b['manifest'], b['facts'], b['basis'],
        b['positioning_context'], b['positioning'], latest_plan=b['plan'])


def simulate_final_review(b):
    reports = [check_positioning(b), RENDER.CHECK.validate_output(b['manifest'], b['facts'],
        b['basis'], b['swot_context'], b['swot'], latest_positioning=b['positioning'],
        latest_positioning_context=b['positioning_context'], latest_plan=b['plan'])]
    report = RENDER.CHECK.merge_reports(reports)
    draft = {k: b['manifest'][k] for k in ('run_id', 'company', 'as_of')}
    draft.update(schema_version=1, phase='final', status='freigegeben', material_errors=[],
        review_scope='SIMULATED offline fixture only', claims=[dict(id=cid, depth='A', status='geprüft',
        evidence_review='SIMULATED offline fixture only') for cid in report['fingerprints']])
    b['final'] = DEMO.STAMP.stamp(draft, report)


class ExecutiveSummaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as temp:
            with redirect_stdout(io.StringIO()):
                DEMO.generate(temp)
            mapping = dict(manifest='facts-run', facts='review-packet', basis='review-basis',
                positioning='positioning', positioning_context='positioning-context',
                swot='swot', swot_context='swot-context', final='review-final', plan='comparison-plan')
            cls.original = {key: json.loads((Path(temp) / (name + '.json')).read_text())
                            for key, name in mapping.items()}

    def setUp(self):
        self.b = copy.deepcopy(self.original)

    def row(self, section):
        return next(r for r in self.b['positioning']['interpretations'] if r['section'] == section)

    def test_full_output_uses_nonfinancial_highlights_and_direct_sources(self):
        body = RENDER.build(**self.b, full=True)
        self.assertIn('240 Kits/Jahr', body)
        self.assertIn('2 Länder', body)
        self.assertIn('Labortest', body)
        self.assertEqual(body.count('class="es-highlight es-entry"'), 3)
        self.assertEqual(body.count('class="es-card es-entry"'), 4)
        self.assertIn('Kapazität laut Hersteller', body)
        self.assertIn('Faktenbasis &amp; Originalquellen', body)
        self.assertIn('https://example.org/company', body)
        links = Links(); links.feed(body)
        self.assertEqual(len(links.ids), len(set(links.ids)))
        self.assertTrue(set(links.anchors) <= set(links.ids))

    def test_four_five_six_main_statements_render_without_padding(self):
        for count in (4, 5, 6):
            with self.subTest(count=count):
                b = copy.deepcopy(self.original)
                template = next(r for r in b['positioning']['interpretations'] if r['section'] == 'executive_summary')
                for order in range(5, count + 1):
                    b['positioning']['interpretations'].append({**template, 'id': 'I-ES-' + str(order),
                        'display_order': order, 'headline': 'Weitere Einordnung ' + str(order)})
                simulate_final_review(b)
                body = RENDER.build(**b, full=True)
                self.assertEqual(body.count('class="es-card es-entry"'), count)
                self.assertIn('data-count="' + str(count) + '"', body)

    def test_full_output_rejects_three_statements_and_two_highlights(self):
        for section in ('executive_summary', 'executive_highlights'):
            with self.subTest(section=section):
                b = copy.deepcopy(self.original)
                group = [r for r in b['positioning']['interpretations'] if r['section'] == section]
                b['positioning']['interpretations'].remove(group[-1])
                simulate_final_review(b)
                with self.assertRaisesRegex(ValueError, '4–6 summary claims and three reviewed highlights'):
                    RENDER.build(**b, full=True)

    def test_short_fields_and_numeric_metric_value_are_required(self):
        for section, field, value in [('executive_summary', 'headline', ''),
                ('executive_summary', 'preview', 'x' * 161),
                ('executive_highlights', 'period', ''),
                ('executive_highlights', 'scope_label', ''),
                ('executive_highlights', 'value', 'No numeric figure')]:
            with self.subTest(section=section, field=field):
                self.b = copy.deepcopy(self.original)
                self.row(section)[field] = value
                self.assertTrue(check_positioning(self.b)['errors'])

    def test_every_visible_highlight_field_and_headline_requires_new_review(self):
        for section, field in [('executive_summary', 'headline'), ('executive_summary', 'preview'),
                ('executive_highlights', 'label'), ('executive_highlights', 'value'),
                ('executive_highlights', 'period'), ('executive_highlights', 'scope_label')]:
            with self.subTest(section=section, field=field):
                self.b = copy.deepcopy(self.original)
                self.row(section)[field] += ' changed'
                with self.assertRaisesRegex(ValueError, 'review missing/stale'):
                    RENDER.build(**self.b, full=True)

    def test_reordering_requires_review_but_array_order_does_not_change_layout(self):
        def summary(body):
            return body.split('<section class="module" id="executive-summary">', 1)[1].split('<section class="module"', 1)[0]
        body = summary(RENDER.build(**self.b, full=True))
        self.b['positioning']['interpretations'].reverse()
        self.assertEqual(summary(RENDER.build(**self.b, full=True)), body)
        rows = [r for r in self.b['positioning']['interpretations'] if r['section'] == 'executive_highlights']
        rows[0]['display_order'], rows[1]['display_order'] = rows[1]['display_order'], rows[0]['display_order']
        with self.assertRaisesRegex(ValueError, 'review missing/stale'):
            RENDER.build(**self.b, full=True)

    def test_highlight_cannot_use_interpretation_or_background_fact(self):
        self.row('executive_highlights')['depends_on'] = ['I10']
        self.assertTrue(any('directly' in e for e in check_positioning(self.b)['errors']))
        self.b = copy.deepcopy(self.original)
        next(r for r in self.b['basis']['claims'] if r['id'] == 'P3')['depth'] = 'B'
        self.assertTrue(any('Vollprüfung A' in e for e in check_positioning(self.b)['errors']))

    def test_duplicate_or_invalid_display_order_rejected(self):
        for value in (True, 0, 2, 10, []):
            with self.subTest(value=value):
                self.b = copy.deepcopy(self.original)
                self.row('executive_highlights')['display_order'] = value
                self.assertTrue(check_positioning(self.b)['errors'])

    def test_html_in_titles_and_values_is_escaped(self):
        self.row('executive_summary')['headline'] = '<script>alert(1)</script>'
        self.row('executive_highlights')['value'] = '240 <img src=x>'
        simulate_final_review(self.b)
        body = RENDER.build(**self.b, full=True)
        self.assertNotIn('<script>alert(1)</script>', body)
        self.assertNotIn('<img src=x>', body)
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;', body)


if __name__ == '__main__':
    unittest.main()
