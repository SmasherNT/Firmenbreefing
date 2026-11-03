import concurrent.futures
import copy
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/file)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


CACHE = load('source_cache_test', 'source-cache.py')
FACTS = load('source_cache_facts', 'prepare-facts.py')


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = dict(schema_version=1, mode='facts-v2', run_id='cache-test',
                             company='Fictional Test', as_of='2026-10-13', selected_roles=['portfolio'])
        self.cache = CACHE.Cache(self.root/'cache', self.manifest)

    def server(self):
        state = dict(requests=0, body=b'<h1>Factory</h1><p>Operational, not planned.</p>', etag='"v1"', fail=False)

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                state['requests'] += 1
                if state['fail']:
                    self.send_error(503); return
                if self.headers.get('If-None-Match') == state['etag']:
                    self.send_response(304); self.end_headers(); return
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('ETag', state['etag']); self.end_headers()
                self.wfile.write(state['body'])

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        self.addCleanup(server.server_close); self.addCleanup(server.shutdown)
        return 'http://127.0.0.1:' + str(server.server_port) + '/document', state

    def test_parallel_agents_fetch_once_and_reuse_same_snapshot(self):
        url, state = self.server()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            rows = list(executor.map(lambda _: self.cache.fetch(url), range(4)))
        self.assertEqual(state['requests'], 1)
        self.assertEqual(sum(r['cache_hit'] for r in rows), 3)
        self.assertEqual(len({r['content_sha256'] for r in rows}), 1)
        record = self.cache.load(CACHE.source_id(url))
        self.assertEqual(record['cache_hits'], 3)
        self.assertEqual(Path(record['original_path']).read_bytes(), state['body'])
        self.assertIn('Operational, not planned.', Path(record['text_path']).read_text())

    def test_refresh_304_changed_version_and_old_original_retained(self):
        url, state = self.server(); first = self.cache.fetch(url)
        same = self.cache.fetch(url, refresh=True)
        self.assertEqual(same['content_sha256'], first['content_sha256'])
        self.assertFalse(same['content_changed']); self.assertEqual(same['revalidations'], 1)
        state.update(body=b'<p>New source status: production announced.</p>', etag='"v2"')
        changed = self.cache.fetch(url, refresh=True)
        self.assertTrue(changed['content_changed'])
        self.assertNotEqual(changed['content_sha256'], first['content_sha256'])
        self.assertTrue(Path(first['original_path']).exists())
        self.assertTrue(Path(first['text_path']).exists())
        self.assertEqual(changed['downloads'], 2)

    def test_refresh_failure_is_not_reported_as_current_approval(self):
        url, state = self.server(); first = self.cache.fetch(url); state['fail'] = True
        with self.assertRaises(OSError): self.cache.fetch(url, refresh=True)
        self.assertEqual(self.cache.load(first['source_id'])['checked_at'], first['checked_at'])

    def test_raw_and_text_corruption_block_cache_reuse(self):
        url, _ = self.server(); first = self.cache.fetch(url)
        raw = Path(first['original_path']); original = raw.read_bytes()
        raw.write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'original changed'): self.cache.fetch(url)
        raw.write_bytes(original); Path(first['text_path']).write_text('changed')
        with self.assertRaisesRegex(ValueError, 'text changed'): self.cache.load(first['source_id'])

    def test_run_company_date_isolation(self):
        for key in ('run_id', 'company', 'as_of'):
            other = copy.deepcopy(self.manifest)
            other[key] = '2026-10-12' if key == 'as_of' else 'different'
            with self.assertRaisesRegex(ValueError, 'another run'): CACHE.Cache(self.root/'cache', other)

    def test_source_identity_fragments_queries_and_credentials(self):
        for url in ('https://example.org/document', 'https://example.org/document?lang=de#p=2'):
            self.assertEqual(CACHE.source_id(url), FACTS.source_id(url))
        self.assertEqual(CACHE.source_id('https://example.org/a#p=2'), CACHE.source_id('https://example.org/a'))
        self.assertNotEqual(CACHE.source_id('https://example.org/a?q=1'), CACHE.source_id('https://example.org/a?q=2'))
        for url in ('file:///tmp/source', 'https://user:password@example.org/a'):
            with self.assertRaises(ValueError): CACHE.canonical_url(url)

    def test_text_is_full_derived_content_with_limits_visible(self):
        body = b'<script>advert</script><h2>Status</h2><p>Own &amp; partner</p><p>Not yet operational</p>'
        text, note = CACHE.extract(body, 'text/html')
        self.assertNotIn('advert', text)
        self.assertIn('Not yet operational', text); self.assertIn('Own & partner', text)
        self.assertIn('dynamic content', note)
        with patch.object(CACHE.shutil, 'which', return_value=None):
            text, note = CACHE.extract(b'%PDF-fixture', 'application/pdf')
            self.assertIsNone(text); self.assertIn('original retained', note)

    def test_tool_capture_and_cli_read_preserve_provenance(self):
        source = self.root/'opened.txt'; source.write_text('Entire opened source\nAnnounced, not operating.\n')
        row = self.cache.store('https://example.org/source', source, 'text/plain', 'opened-tool-text',
                               'Fictional offline fixture, full text supplied')
        self.assertEqual(row['capture_kind'], 'opened-tool-text')
        self.assertEqual(Path(row['original_path']).read_bytes(), source.read_bytes())
        manifest = self.root/'manifest.json'; manifest.write_text(json.dumps(self.manifest))
        base = [sys.executable, str(ROOT/'scripts/source-cache.py'), '--manifest', str(manifest),
                '--cache', str(self.root/'cache')]
        read = subprocess.run([*base, 'read', '--source-id', row['source_id']], capture_output=True, text=True)
        self.assertEqual(read.returncode, 0, read.stdout)
        self.assertIn('2: Announced, not operating.', read.stdout)
        stats = subprocess.run([*base, 'stats'], capture_output=True, text=True)
        data = json.loads(stats.stdout); self.assertEqual(data['imports'], 1)
        self.assertEqual(data['downloads'], 0)
        self.assertIn('not measured model tokens', data['notice'])

    def test_dynamic_page_retains_original_and_requires_fallback(self):
        source = self.root/'dynamic.html'; source.write_text('<html><script>renderApp()</script></html>')
        row = self.cache.store('https://example.org/dynamic', source, 'text/html', 'local-original',
                               'Fictional dynamic HTML fixture')
        self.assertIsNone(row['text_path'])
        self.assertTrue(Path(row['original_path']).exists())
        self.assertIn('browser/WebFetch', row['extraction_notice'])

    def test_failed_download_does_not_create_document_snapshot(self):
        url, state = self.server(); state['fail'] = True
        with self.assertRaises(OSError): self.cache.fetch(url)
        self.assertEqual(self.cache.listing(), [])


if __name__ == '__main__':
    unittest.main()
