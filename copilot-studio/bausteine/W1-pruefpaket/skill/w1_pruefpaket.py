#!/usr/bin/env python3
"""W1 Prüfpaket: prüft alle Faktenmodule formal, baut das Prüfpaket und verteilt die Quellen auf Prüfjobs.

Aufruf: python3 w1_pruefpaket.py --lauf <Lauf-Ordner> --phase basis|final

Teil des Skills; nutzt die vorhandenen Skripte unter scripts/ im Skill-Paket.
Ändert keine Inhalte und trifft keine Prüfentscheidungen.
"""
# --- gemeinsam: anfang (in allen Werkzeug-Skills identisch) ---
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent
SCRIPTS = SKILL / "scripts"
# Fester Arbeitspfad: Die Prüfskripte speichern Pfade in ihren Prüfsummen.
# Jeder Werkzeug-Agent arbeitet deshalb unter demselben Pfad, egal wo der
# Lauf-Ordner liegt.
ARBEIT = Path(os.environ.get("BRIEFING_ARBEIT", "/tmp/firmenbriefing"))
PS = "_pruefstand"
KERN = ("context", "portfolio", "cluster", "market")


def lesen(pfad):
    pfad = Path(pfad)
    text = pfad.read_text(encoding="utf-8")
    if pfad.suffix == ".md":
        treffer = re.search(r"```json\s*\n(.*?)\n```", text, re.S)
        text = treffer.group(1) if treffer else text
    return json.loads(text)


def schreiben(pfad, daten):
    pfad = Path(pfad)
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(json.dumps(daten, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def skript(name, *argumente, cwd):
    """Ruft ein vorhandenes Skript aus scripts/ auf; liefert (ok, json_ausgabe, text)."""
    lauf = subprocess.run([sys.executable, str(SCRIPTS / name), *map(str, argumente)],
                          cwd=cwd, capture_output=True, text=True)
    text = (lauf.stdout or "") + (lauf.stderr or "")
    try:
        daten = json.loads(lauf.stdout) if lauf.stdout.strip() else {}
    except json.JSONDecodeError:
        daten = {}
    return lauf.returncode == 0, daten, text.strip()


class Lauf:
    """Kopiert den Lauf-Ordner an den festen Arbeitspfad und schreibt Änderungen zurück."""

    def __init__(self, ordner):
        self.ordner = Path(ordner).resolve()
        if not self.ordner.is_dir():
            raise SystemExit("Lauf-Ordner nicht gefunden: " + str(ordner))
        manifest = self.ordner / "facts-run.json"
        run_id = lesen(manifest).get("run_id") if manifest.exists() else None
        self.arbeit = ARBEIT / re.sub(r"[^A-Za-z0-9_.-]", "_", run_id or self.ordner.name)
        self.entfernt = []

    def __enter__(self):
        if self.arbeit != self.ordner:
            if self.arbeit.exists():
                shutil.rmtree(self.arbeit)
            shutil.copytree(self.ordner, self.arbeit)
        return self

    def entfernen(self, muster):
        for pfad in list(self.arbeit.glob(muster)):
            pfad.unlink()
            self.entfernt.append(pfad.relative_to(self.arbeit))

    def __exit__(self, *fehler):
        geaendert, geloescht = [], sorted(str(p) for p in self.entfernt)
        if self.arbeit != self.ordner:
            for rel in self.entfernt:
                ziel = self.ordner / rel
                if ziel.exists():
                    ziel.unlink()
            for quelle in sorted(self.arbeit.rglob("*")):
                if quelle.is_file():
                    rel = quelle.relative_to(self.arbeit)
                    ziel = self.ordner / rel
                    if not ziel.exists() or ziel.read_bytes() != quelle.read_bytes():
                        ziel.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(quelle, ziel)
                        geaendert.append(rel.as_posix())
        # Liste für das Zurückschreiben in den SharePoint-Lauf-Ordner.
        print("DATEIEN " + json.dumps(dict(geaendert=geaendert, geloescht=geloescht), ensure_ascii=False))
        return False


def owner_von_id(cid):
    cid = str(cid)
    treffer = re.match(r"F_([A-Za-z0-9_-]+?)_\d", cid)
    if treffer:
        return "focus:" + treffer.group(1)
    for praefix, owner in (("T", "context"), ("H", "context"), ("P", "portfolio"), ("C", "cluster"),
                           ("M", "market"), ("I", "positioning"), ("S", "swot")):
        if re.match(praefix + r"(?![a-z])[-\w]*$", cid) and not cid.startswith("S-"):
            return owner
    return None


def fehler_zuordnen(fehler, quellen_owner=None):
    """Ordnet Fehlermeldungen der Skripte dem zuständigen Baustein zu."""
    rueckgabe = {}
    for meldung in fehler:
        meldung = str(meldung)
        kopf = meldung.split(":", 2)
        owner = None
        if kopf[0] in KERN:
            owner = kopf[0]
        elif kopf[0] == "focus" and len(kopf) > 1 and kopf[1].strip():
            owner = "focus:" + kopf[1].strip()
        elif kopf[0].startswith(("manifest", "comparison plan", "criterion")):
            owner = "auftrag"
        elif kopf[0].startswith("S-") and quellen_owner:
            for o in quellen_owner.get(kopf[0], ["werkzeug"]):
                rueckgabe.setdefault(o, []).append(dict(ids=[kopf[0]], reason=meldung, action="Quellenangabe korrigieren"))
            continue
        else:
            owner = owner_von_id(kopf[0])
        rueckgabe.setdefault(owner or "werkzeug", []).append(
            dict(ids=[kopf[0]] if owner_von_id(kopf[0]) else [], reason=meldung,
                 action="Fehler beheben und Datei vollständig neu schreiben"))
    return rueckgabe


def pruefergebnis(ordner, schritt, phase=None, bestanden=False, jobs=0, rueckgabe=None, fehler=None):
    daten = dict(schritt=schritt, phase=phase, bestanden=bool(bestanden), jobs=jobs,
                 rueckgabe=rueckgabe or {}, fehler=fehler or [])
    schreiben(Path(ordner) / "pruefergebnis.json", daten)
    print(json.dumps(daten, ensure_ascii=False, indent=2))
    return 0 if bestanden else 1
# --- gemeinsam: ende ---


# --- W1 Prüfpaket ---
import argparse
import importlib.util


def facts_modul():
    spec = importlib.util.spec_from_file_location("prepare_facts", SCRIPTS / "prepare-facts.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def erwartete_module(manifest):
    namen = {r + "-facts.json": r for r in manifest.get("selected_roles", [])}
    for seite in manifest.get("focus_pages", []):
        namen["focus-" + seite["id"] + "-facts.json"] = "focus:" + seite["id"]
    return namen


def ids_ersetzen(wert, zuordnung):
    if isinstance(wert, dict):
        neu = {}
        for k, v in wert.items():
            if k == "source_ids" and isinstance(v, list):
                neu[k] = list(dict.fromkeys(zuordnung.get(x, x) for x in v))
            elif k == "source_id" and isinstance(v, str):
                neu[k] = zuordnung.get(v, v)
            else:
                neu[k] = ids_ersetzen(v, zuordnung)
        return neu
    if isinstance(wert, list):
        return [ids_ersetzen(x, zuordnung) for x in wert]
    return wert


def quellen_vereinheitlichen(quellen, zuordnung, facts):
    ergebnis, gesehen = [], set()
    for q in quellen or []:
        if not isinstance(q, dict) or not q.get("url"):
            ergebnis.append(q)
            continue
        sid = facts.source_id(q["url"])
        if q.get("id") and q["id"] != sid:
            zuordnung[q["id"]] = sid
        if sid not in gesehen:
            gesehen.add(sid)
            ergebnis.append({**q, "id": sid})
    return ergebnis


def module_vereinheitlichen(a, manifest, facts):
    """Kopf aus dem Manifest, Quellen-IDs aus der URL. Inhalte bleiben unverändert."""
    fehlend, quellen_owner, dateien = {}, {}, []
    for name, owner in erwartete_module(manifest).items():
        pfad = a / name
        if not pfad.exists():
            fehlend.setdefault(owner, []).append(dict(ids=[], reason=name + " fehlt", action="Datei erstellen"))
            continue
        modul = lesen(pfad)
        rolle = "focus" if owner.startswith("focus:") else owner
        kopf = dict(schema_version=1, mode="facts-v2", role=rolle,
                    **{k: manifest[k] for k in ("run_id", "company", "as_of", "scope")})
        if rolle == "focus":
            kopf["focus_id"] = owner.split(":", 1)[1]
        zuordnung = {}
        modul["source_proposals"] = quellen_vereinheitlichen(modul.get("source_proposals"), zuordnung, facts)
        if isinstance(modul.get("network"), dict):
            modul["network"]["sources"] = quellen_vereinheitlichen(modul["network"].get("sources"), zuordnung, facts)
        modul = ids_ersetzen(modul, zuordnung)
        modul.update(kopf)
        schreiben(pfad, modul)
        dateien.append(name)
        for q in modul.get("source_proposals", []):
            if isinstance(q, dict) and q.get("id"):
                quellen_owner.setdefault(q["id"], []).append(owner)
    return dateien, fehlend, quellen_owner


def jobs_schreiben(lauf, phase, packet):
    a = lauf.arbeit
    ok, daten, text = skript("review-shards.py", "split", "--work", f"{PS}/review-work-{phase}.json",
                             "--facts", packet, "--workers", 3, "--out", f"{PS}/review-split-{phase}.json", cwd=a)
    if not ok:
        return None, daten.get("errors") or [text]
    lauf.entfernen("pruefjob-*.json")
    lauf.entfernen("befund-*.json")
    plan = lesen(a / PS / f"review-split-{phase}.json")
    for job in plan["jobs"]:
        ok, ansicht, text = skript("review-shards.py", "show", "--plan", f"{PS}/review-split-{phase}.json",
                                   "--work", f"{PS}/review-work-{phase}.json", "--facts", packet,
                                   "--job", job["id"], cwd=a)
        if not ok:
            return None, ansicht.get("errors") or [text]
        schreiben(a / ("pruefjob-" + job["id"].split("-")[-1] + ".json"), ansicht)
    return len(plan["jobs"]), []


def basis(lauf):
    a = lauf.arbeit
    manifest = lesen(a / "facts-run.json")
    facts = facts_modul()
    dateien, fehlend, quellen_owner = module_vereinheitlichen(a, manifest, facts)
    if fehlend:
        return pruefergebnis(a, "pruefpaket", "basis", rueckgabe=fehlend)

    # Originale laden; nicht erreichbare Quellen verhindern das Paket nicht.
    cache = f"{PS}/document-cache"
    skript("source-cache.py", "--manifest", "facts-run.json", "--cache", cache, "init", cwd=a)
    nicht_erreichbar = []
    for url in sorted({q["url"] for d in dateien for q in lesen(a / d).get("source_proposals", []) if isinstance(q, dict) and q.get("url")}):
        ok, _, text = skript("source-cache.py", "--manifest", "facts-run.json", "--cache", cache, "fetch", "--url", url, cwd=a)
        if not ok:
            nicht_erreichbar.append(url)

    argumente = ["--manifest", "facts-run.json", "--modules", *dateien, "--out", PS]
    if "market" in manifest.get("selected_roles", []) and (a / "comparison-plan.json").exists():
        argumente += ["--plan", "comparison-plan.json"]
    ok, daten, text = skript("prepare-facts.py", *argumente, cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "pruefpaket", "basis", rueckgabe=fehler_zuordnen(fehler, quellen_owner), fehler=fehler)
    (a / "review-packet.json").write_bytes((a / PS / "review-packet.json").read_bytes())

    argumente = ["prepare", "--manifest", "facts-run.json", "--facts", "review-packet.json",
                 "--validation", f"{PS}/facts-validation.json", "--cache", cache]
    vorher = a / "review-basis.md"
    if vorher.exists() and lesen(vorher).get("status") == "freigegeben" and (a / PS / "review-work-basis.json").exists():
        nummer = len(list((a / PS).glob("review-work-basis-*.json"))) + 1
        alt = a / PS / f"review-work-basis-{nummer}.json"
        (a / PS / "review-work-basis.json").rename(alt)
        alt_review = a / PS / f"review-basis-{nummer}.md"
        alt_review.write_bytes(vorher.read_bytes())
        argumente += ["--previous-work", alt.relative_to(a), "--previous-review", alt_review.relative_to(a)]
    ok, daten, text = skript("review-work.py", *argumente, "--out", f"{PS}/review-work-basis.json", cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "pruefpaket", "basis", rueckgabe=fehler_zuordnen(fehler, quellen_owner), fehler=fehler)
    jobs, fehler = jobs_schreiben(lauf, "basis", "review-packet.json")
    if fehler:
        return pruefergebnis(a, "pruefpaket", "basis", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    hinweis = ["Quelle nicht abrufbar: " + u for u in nicht_erreichbar]
    return pruefergebnis(a, "pruefpaket", "basis", bestanden=True, jobs=jobs, fehler=hinweis)


def bewertung_vervollstaendigen(a, rolle, manifest):
    kontext = lesen(a / f"{rolle}-context.json")
    daten = lesen(a / f"{rolle}.json")
    daten.update(schema_version=1, mode="interpret-v2", role=rolle,
                 **{k: manifest[k] for k in ("run_id", "company", "as_of", "scope")},
                 input_fingerprint=kontext["fingerprint"])
    if rolle == "positioning" and kontext.get("plan_fingerprint"):
        daten["plan_fingerprint"] = kontext["plan_fingerprint"]
    daten.setdefault("research_requests", [])
    daten.setdefault("shared_limitations", [])
    schreiben(a / f"{rolle}.json", daten)


def final(lauf):
    a = lauf.arbeit
    manifest = lesen(a / "facts-run.json")
    for rolle in ("positioning", "swot"):
        for name in (f"{rolle}.json", f"{rolle}-context.json"):
            if not (a / name).exists():
                return pruefergebnis(a, "pruefpaket", "final", rueckgabe={rolle: [dict(ids=[], reason=name + " fehlt", action="Datei erstellen")]})
    bewertung_vervollstaendigen(a, "swot", manifest)
    plan = ["--plan", "comparison-plan.json"] if (a / "comparison-plan.json").exists() else []
    gemeinsam = ["--manifest", "facts-run.json", "--facts", "review-packet.json", "--review", "review-basis.md"]
    for rolle, extra in (("positioning", []),
                         ("swot", ["--positioning", "positioning.json", "--positioning-context", "positioning-context.json"])):
        ok, daten, text = skript("check-interpretation.py", *gemeinsam, "--context", f"{rolle}-context.json",
                                 "--output", f"{rolle}.json", *extra, *plan, "--out", f"{PS}/{rolle}-validation.json", cwd=a)
        if not ok:
            fehler = daten.get("errors") or [text]
            return pruefergebnis(a, "pruefpaket", "final", rueckgabe={rolle: [dict(ids=[], reason=f, action="Fehler beheben") for f in fehler]}, fehler=fehler)
    ok, daten, text = skript("check-interpretation.py", "--merge-validation", f"{PS}/positioning-validation.json",
                             f"{PS}/swot-validation.json", "--out", f"{PS}/interpretation-validation.json", cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "pruefpaket", "final", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    ok, daten, text = skript("review-work.py", "prepare", "--manifest", "facts-run.json", "--facts", "review-packet.json",
                             "--validation", f"{PS}/interpretation-validation.json", "--cache", f"{PS}/document-cache",
                             "--basis-review", "review-basis.md", "--basis-work", f"{PS}/review-work-basis.json",
                             "--positioning", "positioning.json", "--positioning-context", "positioning-context.json",
                             "--swot", "swot.json", "--swot-context", "swot-context.json", *plan,
                             "--out", f"{PS}/review-work-final.json", cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "pruefpaket", "final", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    jobs, fehler = jobs_schreiben(lauf, "final", "review-packet.json")
    if fehler:
        return pruefergebnis(a, "pruefpaket", "final", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    return pruefergebnis(a, "pruefpaket", "final", bestanden=True, jobs=jobs)


def main():
    parser = argparse.ArgumentParser(description="W1 Prüfpaket")
    parser.add_argument("--lauf", required=True)
    parser.add_argument("--phase", choices=("basis", "final"), required=True)
    args = parser.parse_args()
    with Lauf(args.lauf) as lauf:
        return basis(lauf) if args.phase == "basis" else final(lauf)


if __name__ == "__main__":
    sys.exit(main())
