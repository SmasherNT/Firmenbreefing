#!/usr/bin/env python3
"""Werkzeug der schlanken Variante (ohne Prüfagenten).

Aufruf: python3 werkzeug.py --lauf <Lauf-Ordner> --schritt fakten|swot|abschluss

Nutzt die vorhandenen Skripte unter scripts/ im Skill-Paket. Es gibt keine
unabhängige Prüfung: Review-Dateien vermerken das ausdrücklich, und die HTML
wird sichtbar als ungeprüfter Entwurf gekennzeichnet.
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
        if self.arbeit == self.ordner:
            return False
        for rel in self.entfernt:
            ziel = self.ordner / rel
            if ziel.exists():
                ziel.unlink()
        for quelle in self.arbeit.rglob("*"):
            if quelle.is_file():
                ziel = self.ordner / quelle.relative_to(self.arbeit)
                if not ziel.exists() or ziel.read_bytes() != quelle.read_bytes():
                    ziel.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(quelle, ziel)
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


# --- Werkzeug der schlanken Variante ---
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



OHNE_PRUEFUNG = "Ohne unabhängige Quellenprüfung aus der Recherche übernommen (Variante ohne Prüfagenten)."
BADGE_ALT = "Geprüfte Fakten &amp; Analysteninterpretation"
KENNZEICHNUNG = [
    (BADGE_ALT, "Ungeprüfter Entwurf · ohne unabhängige Quellenprüfung"),
    ("Geprüfte Fakten & Analysteninterpretation", "Ungeprüfter Entwurf · ohne unabhängige Quellenprüfung"),
    ("Prüftiefe A · übernommen", "nicht unabhängig geprüft"),
    ("Analysteninterpretation · vollständig geprüft im Schluss-Review", "Analysteninterpretation · nicht unabhängig geprüft"),
    ("<dt>Geprüfte Fakten</dt>", "<dt>Belegte Fakten (ungeprüft)</dt>"),
]
HINWEIS = ('<div role="note" style="margin:16px auto;max-width:1200px;padding:12px 16px;border:2px solid #b45309;'
           'border-radius:8px;background:#fff7ed;color:#7c2d12;font:600 15px/1.45 system-ui,sans-serif">'
           'Ungeprüfter Entwurf: Dieses Briefing wurde ohne unabhängige Quellenprüfung erstellt. '
           'Aussagen vor der Verwendung selbst anhand der verlinkten Quellen prüfen.</div>')


def check_modul():
    spec = importlib.util.spec_from_file_location("check_interpretation", SCRIPTS / "check-interpretation.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def ohne_pruefung_stempeln(a, validierung, phase, ziel):
    """Review-Datei mit ehrlichem Vermerk: übernommen, nicht unabhängig geprüft."""
    v = lesen(a / validierung)
    entwurf = dict(schema_version=1, run_id=v["run_id"], company=v["company"], as_of=v["as_of"], phase=phase,
                   status="freigegeben", material_errors=[], pruefart="keine unabhängige Prüfung",
                   review_scope=OHNE_PRUEFUNG,
                   claims=[dict(id=cid, depth="A", status="übernommen", evidence_review=OHNE_PRUEFUNG)
                           for cid in sorted(v["fingerprints"])])
    schreiben(a / PS / f"review-{phase}-entwurf.json", entwurf)
    return skript("stamp-review.py", "--draft", f"{PS}/review-{phase}-entwurf.json",
                  "--validation", validierung, "--out", ziel, cwd=a)


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
    return daten


def fakten(lauf):
    a = lauf.arbeit
    manifest = lesen(a / "facts-run.json")
    facts = facts_modul()
    dateien, fehlend, quellen_owner = module_vereinheitlichen(a, manifest, facts)
    if fehlend:
        return pruefergebnis(a, "fakten", rueckgabe=fehlend)
    argumente = ["--manifest", "facts-run.json", "--modules", *dateien, "--out", PS]
    plan = ["--plan", "comparison-plan.json"] if (a / "comparison-plan.json").exists() else []
    if "market" in manifest.get("selected_roles", []):
        argumente += plan
    ok, daten, text = skript("prepare-facts.py", *argumente, cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "fakten", rueckgabe=fehler_zuordnen(fehler, quellen_owner), fehler=fehler)
    (a / "review-packet.json").write_bytes((a / PS / "review-packet.json").read_bytes())
    ok, daten, text = ohne_pruefung_stempeln(a, f"{PS}/facts-validation.json", "basis", "review-basis.md")
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "fakten", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    if set(manifest.get("selected_roles", [])) == set(KERN):
        optionen = ["--prepare", "--portfolio", "--module-insights"]
        if "regional_presence" in lesen(a / "portfolio-facts.json"):
            optionen.append("--presence")
        kern = sorted(c["id"] for c in lesen(a / "review-packet.json")["claims"] if owner_von_id(c["id"]) in KERN)
        ok, daten, text = skript("check-interpretation.py", *optionen, "--manifest", "facts-run.json",
                                 "--facts", "review-packet.json", "--review", "review-basis.md", *plan,
                                 "--market", "market-facts.json", "--claim-ids", *kern,
                                 "--out", "positioning-context.json", cwd=a)
        if not ok:
            fehler = daten.get("errors") or [text]
            return pruefergebnis(a, "fakten", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    return pruefergebnis(a, "fakten", bestanden=True)


def swot(lauf):
    a = lauf.arbeit
    manifest = lesen(a / "facts-run.json")
    if not (a / "positioning.json").exists():
        print("Fehlende Eingangsdatei: positioning.json")
        return 1
    positionierung = bewertung_vervollstaendigen(a, "positioning", manifest)
    gemeinsam = ["--manifest", "facts-run.json", "--facts", "review-packet.json", "--review", "review-basis.md"]
    plan = ["--plan", "comparison-plan.json"] if (a / "comparison-plan.json").exists() else []
    ok, daten, text = skript("check-interpretation.py", *gemeinsam, "--context", "positioning-context.json",
                             "--output", "positioning.json", *plan, "--out", f"{PS}/positioning-validation.json", cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "swot", rueckgabe={"positioning": [dict(ids=[], reason=f, action="Fehler beheben") for f in fehler]}, fehler=fehler)
    fragen = {}
    for frage in positionierung.get("research_requests", []):
        if frage.get("blocking"):
            fragen.setdefault(frage.get("target_role") or "werkzeug", []).append(
                dict(ids=frage.get("related_claim_ids", []), reason="Rückfrage aus der Positionierung",
                     action="gezielt recherchieren und ergänzen", frage=frage.get("question", "")))
    if fragen:
        return pruefergebnis(a, "swot", rueckgabe=fragen)
    unbewertet = check_modul().unassessed
    i_ids = [z["id"] for z in positionierung.get("interpretations", []) if not unbewertet(z)]
    ok, daten, text = skript("check-interpretation.py", "--prepare", *gemeinsam, "--positioning", "positioning.json",
                             "--positioning-context", "positioning-context.json", *plan,
                             "--interpretation-ids", *i_ids, "--out", "swot-context.json", cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "swot", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    return pruefergebnis(a, "swot", bestanden=True)


def kennzeichnen(html):
    for alt, neu in KENNZEICHNUNG:
        html = html.replace(alt, neu)
    return html.replace("<main>", "<main>" + HINWEIS, 1)


def abschluss(lauf):
    a = lauf.arbeit
    manifest = lesen(a / "facts-run.json")
    voll = set(manifest.get("selected_roles", [])) == set(KERN)
    argumente = ["--manifest", "facts-run.json", "--facts", "review-packet.json", "--basis-review", "review-basis.md"]
    if voll:
        if not (a / "swot.json").exists():
            print("Fehlende Eingangsdatei: swot.json")
            return 1
        bewertung_vervollstaendigen(a, "swot", manifest)
        gemeinsam = ["--manifest", "facts-run.json", "--facts", "review-packet.json", "--review", "review-basis.md"]
        plan = ["--plan", "comparison-plan.json"] if (a / "comparison-plan.json").exists() else []
        for rolle, extra in (("positioning", []),
                             ("swot", ["--positioning", "positioning.json", "--positioning-context", "positioning-context.json"])):
            ok, daten, text = skript("check-interpretation.py", *gemeinsam, "--context", f"{rolle}-context.json",
                                     "--output", f"{rolle}.json", *extra, *plan,
                                     "--out", f"{PS}/{rolle}-validation.json", cwd=a)
            if not ok:
                fehler = daten.get("errors") or [text]
                return pruefergebnis(a, "abschluss", rueckgabe={rolle: [dict(ids=[], reason=f, action="Fehler beheben") for f in fehler]}, fehler=fehler)
        ok, daten, text = skript("check-interpretation.py", "--merge-validation", f"{PS}/positioning-validation.json",
                                 f"{PS}/swot-validation.json", "--out", f"{PS}/interpretation-validation.json", cwd=a)
        if ok:
            ok, daten, text = ohne_pruefung_stempeln(a, f"{PS}/interpretation-validation.json", "final", "review-final.md")
        if not ok:
            fehler = daten.get("errors") or [text]
            return pruefergebnis(a, "abschluss", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
        argumente += ["--positioning", "positioning.json", "--positioning-context", "positioning-context.json",
                      "--swot", "swot.json", "--swot-context", "swot-context.json",
                      "--final-review", "review-final.md", *plan, "--full"]
    ok, daten, text = skript("render-briefing.py", *argumente, "--out", f"{PS}/briefing-roh.html", cwd=a)
    if not ok:
        fehler = daten.get("errors") or [text]
        return pruefergebnis(a, "abschluss", rueckgabe=fehler_zuordnen(fehler), fehler=fehler)
    html = kennzeichnen((a / PS / "briefing-roh.html").read_text(encoding="utf-8"))
    (a / "briefing.html").write_text(html, encoding="utf-8")
    return pruefergebnis(a, "abschluss", bestanden=True)


def main():
    parser = argparse.ArgumentParser(description="Werkzeug der schlanken Variante")
    parser.add_argument("--lauf", required=True)
    parser.add_argument("--schritt", choices=("fakten", "swot", "abschluss"), required=True)
    args = parser.parse_args()
    with Lauf(args.lauf) as lauf:
        return {"fakten": fakten, "swot": swot, "abschluss": abschluss}[args.schritt](lauf)


if __name__ == "__main__":
    sys.exit(main())
