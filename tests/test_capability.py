import unittest
import test_interpretation as fixtures

CAPABILITY = fixtures.load('capability', 'capability-html.py')


class CapabilityTests(unittest.TestCase):
    def test_nonstandard_evidence_anchors_keep_actual_value_and_ceiling(self):
        shown = CAPABILITY.display(dict(cell_status='bewertet', value=3),
            dict(display_type='Evidenzstufe', anchors={'1': 'offered', '3': 'tested', '8': 'in use'}))
        self.assertEqual((shown['grade'], shown['ceiling'], shown['value']), ('3', '8', 'tested'))

    def test_profile_and_metric_do_not_get_evidence_scores(self):
        profile = CAPABILITY.display(dict(cell_status='bewertet', value='Open architecture'),
                                     dict(display_type='Profil'))
        metric = CAPABILITY.display(dict(cell_status='bewertet', value=120),
                                    dict(display_type='Kennzahl', unit='units/year'))
        self.assertIsNone(profile['level'])
        self.assertIsNone(metric['level'])
        self.assertEqual(metric['value'], '120 units/year')

    def test_missing_evidence_is_distinct_from_inapplicability_and_zero(self):
        for state, kind in [('nicht öffentlich belegt', 'missing'), ('nicht anwendbar', 'na')]:
            shown = CAPABILITY.display(dict(cell_status=state, value=None), dict(display_type='Evidenzstufe'))
            self.assertEqual(shown['value'], state)
            self.assertEqual(shown['kind'], kind)
            self.assertEqual(shown['grade'], '')
            self.assertIsNone(shown['level'])

    def test_static_evaluations_preserve_full_values_sources_and_escaping(self):
        value = 'Full description with important qualifier ' * 4
        row = dict(id='I1', cell_status='bewertet', value=value, headline='<script>attack()</script>', preview='Manufacturer only')
        body = CAPABILITY.render([dict(id='profile', label='Integration', display_type='Profil',
            question='Which model?', evidence_required='Product document')],
            [dict(id='target', label='Example · Specific product')], {('target', 'profile'): row},
            'Example', lambda r: '<p>Complete assessment</p><a href="https://example.org/report">Original source</a>', {'I1': 1})
        self.assertIn(value.strip(), body)
        self.assertIn('https://example.org/report', body)
        self.assertIn('cm-eval-I1', body)
        self.assertIn('Specific product', body)
        self.assertIn('Referenzunternehmen', body)
        self.assertNotIn('<script>attack()</script>', body)
        self.assertIn('&lt;script&gt;attack()&lt;/script&gt;', body)
