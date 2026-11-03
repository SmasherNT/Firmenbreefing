#!/usr/bin/env python3
"""Build reproducible, self-contained Cowork skill uploads; never install or publish."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MAX_COMPANIONS = 20


def archive(files):
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as package:
        for name, body in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            package.writestr(info, body)
    return output.getvalue()


BOOTSTRAP = '''#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

EXPECTED = "__SHA256__"

def extract(bundle, workspace):
    if hashlib.sha256(bundle.read_bytes()).hexdigest() != EXPECTED:
        raise ValueError('Runtime archive checksum mismatch')
    target = workspace.resolve() / ('firmenbriefing-' + EXPECTED[:16])
    with zipfile.ZipFile(bundle) as package:
        for item in package.infolist():
            path = PurePosixPath(item.filename)
            if (path.is_absolute() or '..' in path.parts or not path.parts
                    or any(p.startswith('.') for p in path.parts)
                    or '\\\\' in item.filename or stat.S_ISLNK(item.external_attr >> 16)):
                raise ValueError('Unsafe runtime member: ' + item.filename)
            destination = target.joinpath(*path.parts)
            if destination.resolve() != destination or not destination.resolve().is_relative_to(target):
                raise ValueError('Unsafe extraction destination')
            body = package.read(item)
            if destination.exists() and destination.read_bytes() != body:
                raise ValueError('Existing runtime was modified: ' + str(destination))
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(body)
    return target

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prepare the versioned project workspace; no agents are installed.')
    parser.add_argument('--workspace', type=Path, required=True)
    args = parser.parse_args()
    project = extract(Path(__file__).with_name('runtime.zip'), args.workspace)
    print(json.dumps({'project_root': str(project), 'sha256': EXPECTED,
                      'next': 'Read AGENTS.md and references/cowork-betrieb.md, then execute preflight.'}))
'''


def build(output):
    files = {'AGENTS.md': (ROOT/'AGENTS.md').read_bytes()}
    for folder in ('roles', 'skills', 'scripts', 'runtime', 'references'):
        for path in sorted((ROOT/folder).rglob('*')):
            if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
                continue
            if any(part.startswith('.') for part in path.relative_to(ROOT).parts):
                raise ValueError('Hidden runtime path: ' + str(path))
            # Historical development reports are not current operating instructions.
            if path.name.endswith('-abnahme.md') or path.name == 'build-cowork-skills.py':
                continue
            files[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    runtime = archive(files)
    if len(runtime) > 5 * 1024 * 1024:
        raise ValueError('Runtime companion exceeds 5 MB')
    digest = hashlib.sha256(runtime).hexdigest()
    bootstrap = BOOTSTRAP.replace('__SHA256__', digest).encode()
    output.mkdir(parents=True, exist_ok=True)
    records = []
    for path in sorted((ROOT/'skills').glob('*/SKILL.md')):
        name = path.parent.name
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            raise ValueError('Invalid skill name')
        _, frontmatter, _ = path.read_text().split('---', 2)
        if f'name: {name}\n' not in frontmatter:
            raise ValueError('Skill folder/name mismatch')
        body = f'''---{frontmatter}---

Lade diese Firmenbriefing-Methode aus der mitgelieferten Projektlaufzeit.
1. Lies die Begleitdatei resources/bootstrap.py und führe sie mit Python aus:
   python3 <Skillordner>/resources/bootstrap.py --workspace <beschreibbarer_Arbeitsbereich>
   Verwende ausschließlich den zurückgegebenen project_root; dort liegen alle
   relativen Projektpfade. Alle zwölf Uploads enthalten dieselbe Laufzeitversion.
2. Lies project_root/AGENTS.md, references/cowork-betrieb.md und
   skills/{name}/SKILL.md aus diesem Projektstamm.
3. Führe die echten Hostproben aus references/cowork-betrieb.md durch, speichere
   beobachtete Ergebnisse und führe scripts/cowork-preflight.py --strict
   --host-evidence <Nachweisdatei> aus. Ohne Nachweis bleibt der Lauf blockiert.
   Registriere keine roles-Dateien als angeblich native Subagenten. Fehlen Python,
   getrennte Rollenkontexte oder Quellenzugriffe, melde den Lauf als blockiert.
4. Bearbeite erst danach den tatsächlichen Nutzerauftrag nach der geladenen Methode.

Begleitdateien: resources/bootstrap.py und resources/runtime.zip.
Das geprüfte Archiv enthält Rollenverträge, Referenzen, Renderer, Methoden und
Vorlagen. Es installiert keine Agenten und führt beim Entpacken keine Recherche aus.
'''
        members = {'SKILL.md': body.encode(), 'resources/bootstrap.py': bootstrap,
                   'resources/runtime.zip': runtime}
        companions = len(members) - 1
        if companions > MAX_COMPANIONS or sum(map(len, members.values())) > 10*1024*1024:
            raise ValueError('Skill upload limits exceeded')
        data = archive(members)
        target = output/(name+'.skill')
        target.write_bytes(data)
        records.append(dict(name=name, path=target.name, companions=companions,
                            bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
    result = dict(schema_version=1, runtime_sha256=digest, runtime_files=len(files), skills=records,
                  notice='Built and locally checked; not imported into Cowork or executed there.')
    (output/'build-report.json').write_text(json.dumps(result, indent=2)+'\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    print(json.dumps(build(parser.parse_args().out), indent=2))
