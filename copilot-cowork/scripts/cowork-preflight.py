#!/usr/bin/env python3
"""Probe local dependencies and report separately attested host capabilities."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def probe(host_evidence=None):
    result = dict(schema_version=1, host='microsoft-copilot-cowork', checks={},
                  notice='Local dependency probes and externally attested host tests; not a research or source review.')
    checks = result['checks']
    checks['python'] = dict(status='available', detail=sys.version.split()[0])
    checks['file_read_write'] = dict(status='not_checked', detail='Run in the intended writable project workspace.')
    try:
        import tempfile
        with tempfile.TemporaryDirectory(prefix='preflight-', dir=ROOT) as temp:
            path = Path(temp)/'probe.txt'; path.write_text('probe')
            if path.read_text() == 'probe':
                checks['file_read_write'] = dict(status='available', detail='Project workspace read/write probe passed.')
    except OSError as error:
        checks['file_read_write'] = dict(status='missing', detail=str(error))
    checks['posix_locking'] = dict(status='available' if importlib.util.find_spec('fcntl') else 'missing',
                                 detail='resume-run.py requires fcntl; use a POSIX worker if unavailable.')
    node = shutil.which('node')
    checks['node'] = dict(status='available' if node else 'missing', detail=node or 'Node.js absent')
    available = False
    if node:
        test = subprocess.run([node, '-e', "require('playwright-core')"], cwd=ROOT,
                              capture_output=True, timeout=15)
        available = test.returncode == 0
    checks['playwright'] = dict(status='available' if available else 'missing', detail='Node resolution of playwright-core')
    browser = os.environ.get('BRIEFING_CHROMIUM_PATH') or shutil.which('chromium') or shutil.which('chromium-browser')
    browser_ok = bool(browser and Path(browser).is_file() and os.access(browser, os.X_OK))
    checks['chromium'] = dict(status='available' if browser_ok else 'missing', detail=browser or 'Set BRIEFING_CHROMIUM_PATH')
    checks['pdftotext'] = dict(status='available' if shutil.which('pdftotext') else 'optional_missing',
                              detail='Optional PDF text extraction; original reading remains mandatory.')
    evidence = host_evidence or {}
    for capability in ('web_search_fetch', 'independent_contexts'):
        row = evidence.get(capability, {})
        valid = row.get('tested') is True and all(isinstance(row.get(k), str) and row[k].strip()
                                                for k in ('evidence', 'tested_at', 'host'))
        checks[capability] = dict(status='externally_attested' if valid else 'not_checked',
                                  detail=row if valid else 'Actual host/adapter probe required; configuration is not evidence.')
    required = ('python', 'file_read_write', 'posix_locking', 'web_search_fetch', 'independent_contexts')
    allowed = {'available', 'externally_attested'}
    result['blocked'] = [key for key in required if checks[key]['status'] not in allowed]
    result['qa_open'] = [key for key in ('node', 'playwright', 'chromium') if checks[key]['status'] != 'available']
    result['status'] = 'blocked' if result['blocked'] else 'ready_for_host_pilot'
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host-evidence', type=Path)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--strict', action='store_true')
    args = parser.parse_args()
    result = probe(json.loads(args.host_evidence.read_text()) if args.host_evidence else None)
    body = json.dumps(result, indent=2, ensure_ascii=False)+'\n'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(body)
    print(body, end='')
    sys.exit(2 if args.strict and (result['blocked'] or result['qa_open']) else 0)
