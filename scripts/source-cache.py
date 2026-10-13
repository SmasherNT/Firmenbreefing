#!/usr/bin/env python3
"""Run-scoped source snapshots. Stores evidence, never approves or summarizes it."""
import argparse
from contextlib import contextmanager
from datetime import date, datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

MAX_BYTES = 128 * 1024 * 1024


def digest(body):
    return hashlib.sha256(body).hexdigest()


def canonical_url(url):
    parts = urlsplit(url.strip())
    if parts.scheme not in ('http', 'https') or not parts.netloc or parts.username or parts.password:
        raise ValueError('public http(s) document URL required')
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ''))


def source_id(url):
    return 'S-' + digest(canonical_url(url).encode())[:16]


def identity(manifest):
    if manifest.get('schema_version') != 1 or manifest.get('mode') != 'facts-v2':
        raise ValueError('facts-v2 manifest required')
    result = {k: manifest.get(k) for k in ('run_id', 'company', 'as_of')}
    if any(not isinstance(v, str) or not v.strip() for v in result.values()):
        raise ValueError('run/company/as_of required')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', result['as_of']):
        raise ValueError('as_of must be YYYY-MM-DD')
    date.fromisoformat(result['as_of'])
    return result


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def atomic(path, body):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.write-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as handle:
            handle.write(body)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json(path, data):
    atomic(path, (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode())


@contextmanager
def lock(path, timeout=30):
    """Per-document mkdir lock: works with concurrent agents and on Windows."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + timeout
    while True:
        try:
            path.mkdir()
            break
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise ValueError('cache lock busy: ' + str(path))
            time.sleep(.05)
    try:
        yield
    finally:
        path.rmdir()


class VisibleText(HTMLParser):
    ignored = {'script', 'style', 'noscript', 'template'}
    blocks = {'p', 'div', 'section', 'article', 'header', 'footer', 'li', 'tr', 'td',
              'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'hr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.hidden = [], []

    def handle_starttag(self, tag, attrs):
        if tag in self.ignored:
            self.hidden.append(tag)
        elif tag in self.blocks and not self.hidden:
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if self.hidden:
            if tag == self.hidden[-1]:
                self.hidden.pop()
        elif tag in self.blocks:
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

    def text(self):
        return '\n'.join(line for raw in ''.join(self.parts).splitlines()
                         if (line := re.sub(r'\s+', ' ', raw).strip())) + '\n'


def extract(body, content_type):
    """Derived full text; raw bytes remain available for independent review."""
    mime = content_type.split(';')[0].strip().lower()
    if body.startswith(b'%PDF-') or mime == 'application/pdf':
        executable = shutil.which('pdftotext')
        if not executable:
            return None, 'PDF original retained; pdftotext unavailable. Open original PDF.'
        with tempfile.TemporaryDirectory() as directory:
            raw, target = Path(directory)/'source.pdf', Path(directory)/'text.txt'
            raw.write_bytes(body)
            try:
                result = subprocess.run([executable, '-layout', str(raw), str(target)],
                                        capture_output=True, timeout=60)
            except subprocess.TimeoutExpired:
                return None, 'PDF text extraction timed out; open original PDF.'
            if result.returncode != 0:
                return None, 'PDF text extraction failed; open original PDF.'
            pages = target.read_text(encoding='utf-8').split('\f')
            text = '\n'.join('[PDF-Seite ' + str(i+1) + ']\n' + p for i, p in enumerate(pages) if p.strip())
            if not text.strip():
                return None, 'PDF has no extractable text; open original PDF (OCR if needed).'
            return text + '\n', 'pdftotext; page markers refer to PDF pages, not printed numbering.'
    if not (mime.startswith('text/') or mime in ('application/json', 'application/xml', 'application/xhtml+xml')):
        return None, 'Unsupported text extraction; original bytes retained.'
    charset = re.search(r'charset=["\s]*([^;"\s]+)', content_type, re.I)
    try:
        text = body.decode(charset.group(1) if charset else 'utf-8', errors='replace')
    except LookupError:
        text = body.decode('utf-8', errors='replace')
    notice = 'Decoded full text; verify original if encoding or layout matters.'
    if mime in ('text/html', 'application/xhtml+xml'):
        parser = VisibleText(); parser.feed(text); parser.close()
        text = parser.text()
        if not text.strip():
            return None, 'HTML has no visible extracted text; inspect original and use browser/WebFetch for dynamic content.'
        notice = 'Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser.'
    if '\ufffd' in text:
        notice += ' Encoding replacement detected; inspect original.'
    return text, notice


class Cache:
    def __init__(self, root, manifest):
        self.root, self.identity = Path(root).resolve(), identity(manifest)
        self.root.mkdir(parents=True, exist_ok=True)
        with lock(self.root/'.identity-lock'):
            target = self.root/'identity.json'
            if target.exists():
                if json.loads(target.read_text()) != self.identity:
                    raise ValueError('cache belongs to another run/company/as_of; use a new cache')
            else:
                write_json(target, self.identity)

    def _directory(self, sid):
        if not isinstance(sid, str) or not re.fullmatch(r'S-[0-9a-f]{16}', sid):
            raise ValueError('invalid source_id')
        return self.root/'documents'/sid

    def load(self, sid):
        directory = self._directory(sid)
        record = json.loads((directory/'current.json').read_text(encoding='utf-8'))
        if record.get('identity') != self.identity or record.get('source_id') != sid or source_id(record['url']) != sid:
            raise ValueError('cache metadata identity mismatch')
        version = record.get('content_sha256', '')
        if not re.fullmatch(r'[0-9a-f]{64}', version):
            raise ValueError('invalid cache snapshot hash')
        folder = directory/'versions'/version
        raw = folder/'source.bin'
        if digest(raw.read_bytes()) != version:
            raise ValueError('cached original changed; restore original or use a new cache')
        expected = record.get('text_sha256')
        if expected is not None and not re.fullmatch(r'[0-9a-f]{64}', expected):
            raise ValueError('invalid cache text hash')
        text = folder/('text-' + expected + '.txt') if expected else None
        if expected and (not text.exists() or digest(text.read_bytes()) != expected):
            raise ValueError('cached extracted text changed; restore text or use a new cache')
        return {**record, 'original_path': str(raw), 'text_path': str(text) if expected else None,
                'notice': 'Snapshot available, not a content review or factual approval.'}

    def _save(self, url, body, content_type, capture_kind, previous=None, **metadata):
        if not body or len(body) > MAX_BYTES:
            raise ValueError('empty or oversized document')
        sid, version = source_id(url), digest(body)
        directory = self._directory(sid); folder = directory/'versions'/version
        text, notice = extract(body, content_type)
        raw = folder/'source.bin'
        # Content-addressed originals are retained across refreshes.
        if not raw.exists():
            atomic(raw, body)
        elif raw.read_bytes() != body:
            raise ValueError('corrupt original at existing snapshot hash')
        if text is not None:
            text_path = folder/('text-' + digest(text.encode()) + '.txt')
            if not text_path.exists():
                atomic(text_path, text.encode())
            elif text_path.read_bytes() != text.encode():
                raise ValueError('corrupt text at existing snapshot hash')
        record = dict(identity=self.identity, source_id=sid, url=canonical_url(url),
                      content_sha256=version, text_sha256=digest(text.encode()) if text is not None else None,
                      content_type=content_type, capture_kind=capture_kind, bytes=len(body),
                      fetched_at=now(), checked_at=now(), extraction_notice=notice,
                      downloads=(previous or {}).get('downloads', 0) + (capture_kind == 'http-original'),
                      cache_hits=(previous or {}).get('cache_hits', 0),
                      imports=(previous or {}).get('imports', 0) + (capture_kind != 'http-original'),
                      revalidations=(previous or {}).get('revalidations', 0), **metadata)
        capture_id = digest(json.dumps(record, sort_keys=True, ensure_ascii=False).encode())
        write_json(folder/'captures'/(capture_id + '.json'), record)
        write_json(directory/'current.json', {**record, 'capture_id': capture_id})
        return self.load(sid)

    def fetch(self, url, refresh=False, timeout=20):
        url = canonical_url(url); sid = source_id(url); directory = self._directory(sid)
        with lock(directory/'.fetch-lock'):
            previous = self.load(sid) if (directory/'current.json').exists() else None
            if previous and not refresh:
                write_json(directory/'current.json', {**previous, 'cache_hits': previous['cache_hits'] + 1})
                return {**self.load(sid), 'cache_hit': True}
            headers = {'User-Agent': 'Firmenbriefing-SourceCache/1.0', 'Accept-Encoding': 'identity'}
            if previous and previous.get('capture_kind') == 'http-original':
                if previous.get('etag'): headers['If-None-Match'] = previous['etag']
                if previous.get('last_modified'): headers['If-Modified-Since'] = previous['last_modified']
            # Persist before network I/O: failed/interrupted refresh is not proof of freshness.
            pending = directory/'revalidation.json'
            write_json(pending, {'status': 'pending', 'started_at': now(), 'url': url})
            try:
                with urlopen(Request(url, headers=headers), timeout=timeout) as response:
                    body = response.read(MAX_BYTES + 1)
                    result = self._save(url, body, response.headers.get('Content-Type', 'application/octet-stream'),
                                        'http-original', previous, final_url=response.geturl(),
                                        etag=response.headers.get('ETag'), last_modified=response.headers.get('Last-Modified'))
            except HTTPError as error:
                if error.code != 304 or previous is None:
                    raise
                write_json(directory/'current.json', {**previous, 'checked_at': now(),
                           'revalidations': previous['revalidations'] + 1})
                result = self.load(sid)
            pending.unlink(missing_ok=True)
            return {**result, 'cache_hit': False,
                    'content_changed': bool(previous and previous['content_sha256'] != result['content_sha256'])}

    def store(self, url, path, content_type, capture_kind, capture_note):
        if capture_kind not in ('local-original', 'opened-tool-text') or not capture_note.strip():
            raise ValueError('capture kind and provenance note required; no summaries')
        sid = source_id(url); directory = self._directory(sid)
        with lock(directory/'.fetch-lock'):
            old = self.load(sid) if (directory/'current.json').exists() else None
            result = self._save(url, Path(path).read_bytes(), content_type, capture_kind,
                                old, capture_note=capture_note)
            (directory/'revalidation.json').unlink(missing_ok=True)
            return result

    def listing(self):
        return [self.load(p.parent.name) for p in sorted((self.root/'documents').glob('S-*/current.json'))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--cache', required=True)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('init'); commands.add_parser('list'); commands.add_parser('stats')
    fetch = commands.add_parser('fetch'); fetch.add_argument('--url', required=True)
    fetch.add_argument('--refresh', action='store_true')
    store = commands.add_parser('store'); store.add_argument('--url', required=True)
    store.add_argument('--input', required=True); store.add_argument('--content-type', required=True)
    store.add_argument('--capture-kind', required=True, choices=['local-original', 'opened-tool-text'])
    store.add_argument('--capture-note', required=True)
    show = commands.add_parser('show'); show.add_argument('--source-id', required=True)
    read = commands.add_parser('read'); read.add_argument('--source-id', required=True)
    read.add_argument('--start-line', type=int, default=1); read.add_argument('--end-line', type=int)
    args = parser.parse_args()
    try:
        cache = Cache(args.cache, json.loads(Path(args.manifest).read_text(encoding='utf-8')))
        if args.command == 'init':
            result = {'cache': str(cache.root), **cache.identity}
        elif args.command == 'fetch':
            result = cache.fetch(args.url, args.refresh)
        elif args.command == 'store':
            result = cache.store(args.url, args.input, args.content_type, args.capture_kind, args.capture_note)
        elif args.command == 'show':
            result = cache.load(args.source_id)
        elif args.command == 'read':
            record = cache.load(args.source_id)
            if not record['text_path']:
                raise ValueError(record['extraction_notice'])
            lines = Path(record['text_path']).read_text(encoding='utf-8').splitlines()
            end = args.end_line if args.end_line is not None else len(lines)
            if args.start_line < 1 or end < args.start_line:
                raise ValueError('invalid line range')
            print('\n'.join(str(i+1) + ': ' + lines[i] for i in range(args.start_line-1, min(end, len(lines)))))
            return 0
        else:
            records = cache.listing()
            if args.command == 'stats':
                result = {'documents': len(records), **{k: sum(r[k] for r in records) for k in
                          ('downloads', 'cache_hits', 'imports', 'revalidations')},
                          'notice': 'Document operations only; not measured model tokens or cost savings.'}
            else:
                result = [{k: r.get(k) for k in ('source_id', 'url', 'content_sha256', 'capture_kind',
                           'fetched_at', 'original_path', 'text_path', 'extraction_notice')} for r in records]
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, TypeError, KeyError, subprocess.SubprocessError) as error:
        print(json.dumps({'errors': [str(error)]}, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    sys.exit(main())
