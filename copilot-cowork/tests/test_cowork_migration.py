"""Standalone upload, isolation and checkpoint regression tests; no host claims."""
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILD = load('cowork_build_tests', 'build-cowork-skills.py')
PREFLIGHT = load('cowork_preflight_tests', 'cowork-preflight.py')
RESUME = load('cowork_resume_tests', 'resume-run.py')


class CoworkMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.output = Path(cls.temp.name)/'uploads'
        cls.report = BUILD.build(cls.output)
        with zipfile.ZipFile(cls.output/'company-briefing.skill') as archive:
            cls.bootstrap_text = archive.read('resources/bootstrap.py')
            cls.runtime = archive.read('resources/runtime.zip')

    def setUp(self):
        self.work = tempfile.TemporaryDirectory()
        self.addCleanup(self.work.cleanup)
        self.workspace = Path(self.work.name)
        self.bundle = self.workspace/'runtime.zip'
        self.bundle.write_bytes(self.runtime)
        self.bootstrap = {'__name__': 'bootstrap_test'}
        exec(compile(self.bootstrap_text, 'bootstrap.py', 'exec'), self.bootstrap)

    def test_uploads_are_reproducible_and_within_documented_limits(self):
        names = {p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')}
        self.assertEqual({r['name'] for r in self.report['skills']}, names)
        self.assertEqual(len(names), 12)
        second = BUILD.build(self.workspace/'second')
        self.assertEqual(second, self.report)
        for record in self.report['skills']:
            data = (self.output/record['path']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), record['sha256'])
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                self.assertEqual(set(archive.namelist()),
                                 {'SKILL.md', 'resources/bootstrap.py', 'resources/runtime.zip'})
                self.assertIn('name: '+record['name']+'\n', archive.read('SKILL.md').decode())
                self.assertTrue(all(r.file_size <= 5*1024*1024 for r in archive.infolist()))
                self.assertEqual(archive.read('resources/runtime.zip'), self.runtime)

    def test_extracted_runtime_loads_without_repository_parent(self):
        project = self.bootstrap['extract'](self.bundle, self.workspace/'isolated')
        with zipfile.ZipFile(io.BytesIO(self.runtime)) as archive:
            self.assertEqual(len(archive.namelist()), self.report['runtime_files'])
        self.assertTrue((project/'AGENTS.md').is_file())
        self.assertEqual(len(list((project/'roles').glob('*.md'))), 10)
        self.assertFalse((project/'.claude').exists())
        self.assertFalse((project/'CLAUDE.md').exists())
        for name in ('prepare-facts.py', 'render-briefing.py', 'resume-run.py'):
            spec = importlib.util.spec_from_file_location('isolated_'+name, project/'scripts'/name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.assertEqual(Path(module.__file__).resolve().parents[1], project)
            if hasattr(module, 'ROOT'):
                self.assertEqual(module.ROOT, project)
        self.assertEqual(self.bootstrap['extract'](self.bundle, self.workspace/'isolated'), project)

    def test_tampered_bundle_is_rejected(self):
        self.bundle.write_bytes(self.runtime+b'tampered')
        with self.assertRaisesRegex(ValueError, 'checksum'):
            self.bootstrap['extract'](self.bundle, self.workspace/'isolated')

    def test_modified_runtime_is_never_overwritten(self):
        project = self.bootstrap['extract'](self.bundle, self.workspace/'isolated')
        (project/'AGENTS.md').write_text('Modified runtime')
        with self.assertRaisesRegex(ValueError, 'modified'):
            self.bootstrap['extract'](self.bundle, self.workspace/'isolated')
        self.assertEqual((project/'AGENTS.md').read_text(), 'Modified runtime')

    def test_archive_path_traversal_is_rejected_even_with_valid_checksum(self):
        for member in ('../escaped.txt', '/absolute.txt', '.hidden.txt', 'a\\b.txt'):
            data = BUILD.archive({member: b'bad'})
            self.bundle.write_bytes(data)
            self.bootstrap['EXPECTED'] = hashlib.sha256(data).hexdigest()
            with self.subTest(member=member), self.assertRaisesRegex(ValueError, 'Unsafe'):
                self.bootstrap['extract'](self.bundle, self.workspace/'isolated')
        self.assertFalse((self.workspace/'escaped.txt').exists())

    def test_runtime_and_reviewer_methods_are_bound_to_checkpoints(self):
        for stage, method in [('portfolio', 'portfolio-analysis'), ('cluster', 'cluster-analysis'),
                              ('market', 'market-facts'), ('positioning', 'positioning-analysis')]:
            bindings = RESUME.code_files(stage)
            self.assertIn('AGENTS.md', bindings)
            self.assertIn('runtime/settings.json', bindings)
            self.assertIn('references/modellaufteilung.json', bindings)
            self.assertIn('skills/'+method+'/SKILL.md', bindings)
            self.assertFalse(any('.claude' in p or p == 'CLAUDE.md' for p in bindings))
        for stage in ('basis-review', 'final-review'):
            self.assertIn('roles/source-document-reviewer.md', RESUME.code_files(stage))
            self.assertIn('roles/source-reviewer.md', RESUME.code_files(stage))

    def test_missing_role_contract_cannot_silently_reuse_checkpoint(self):
        project = self.bootstrap['extract'](self.bundle, self.workspace/'isolated')
        (project/'roles/portfolio-analyst.md').unlink()
        with patch.object(RESUME, 'ROOT', project), self.assertRaisesRegex(ValueError, 'missing runtime'):
            RESUME.code_files('portfolio')

    def test_dependency_probes_do_not_assert_unobserved_host_execution(self):
        report = PREFLIGHT.probe()
        self.assertEqual(report['status'], 'blocked')
        self.assertIn('independent_contexts', report['blocked'])
        self.assertIn('web_search_fetch', report['blocked'])
        self.assertEqual(PREFLIGHT.probe({'independent_contexts': {'tested': True}})
                         ['checks']['independent_contexts']['status'], 'not_checked')


if __name__ == '__main__':
    unittest.main()
