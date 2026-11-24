#!/usr/bin/env python3
"""Firmenbriefing: Teile zusammenführen, validieren, HTML rendern, Daten zurücklesen.

Nur Python-Standardbibliothek; die Excel-Befehle brauchen zusätzlich openpyxl.

  python3 briefing.py zusammenfuehren --daten briefing-daten.json --teil teil.json [--ersetzen]
  python3 briefing.py validieren --daten briefing-daten.json
  python3 briefing.py auswerten --daten briefing-daten.json
  python3 briefing.py rendern --daten briefing-daten.json --out briefing.html
  python3 briefing.py extrahieren --html briefing.html --out briefing-daten.json
  python3 briefing.py excel --daten briefing-daten.json --out briefing-daten.xlsx
  python3 briefing.py aus-excel --xlsx briefing-daten.xlsx --out briefing-daten.json
  python3 briefing.py version
"""
import argparse, calendar, datetime, html, json, os, re, sys

VERSION = "1.1.0"
SCHEMA = "firmenbriefing/1"
FACT_RE = re.compile(r"^(T|H|P|C|M|F_[A-Za-z0-9-]+_)\d+$")
INTERP_RE = re.compile(r"^[IS][A-Za-z0-9_-]*$")
SRC_RE = re.compile(r"^Q\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URSPRUNG = {"fakt": "Fakt", "hersteller": "Herstellerangabe", "partner": "Partnerangabe",
            "medien": "Medienbericht", "nutzer": "Nutzerangabe"}
KAPITEL = {"T": "unternehmen", "H": "personen", "P": "portfolio", "C": "cluster", "M": "markt"}
KAPITEL_TITEL = {"unternehmen": "Unternehmen", "personen": "Gesprächspartner", "portfolio": "Portfolio",
                 "cluster": "Struktur & Partner", "markt": "Markt & Wettbewerb", "fokus": "Fokusthemen",
                 "interpretation": "Interpretation"}
MODULE = {"firmenbasis": "Firmenbasis", "person": "Gesprächspartner", "portfolio": "Portfolio", "cluster": "Struktur, Partner und Kunden",
          "markt": "Markt und Wettbewerb", "fokus": "Fokusthemen", "interpretation": "Interpretation"}
URTEIL = {"im_original_bestaetigt": ("im Original bestätigt", "ok", "✓"),
          "durch_suche_gestuetzt": ("durch Suche gestützt", "such", "≈"),
          "abweichend": ("abweichend", "bad", "✗"), "nicht_belegt": ("nicht belegt", "bad", "?"),
          "nicht_erreichbar": ("nicht erreichbar", "warn", "⊘"),
          "nicht_einzeln_geprueft": ("nicht einzeln geprüft (Stichprobe)", "none", "·"),
          "gestuetzt": ("Ableitung gestützt", "ok", "✓"), "eingeschraenkt": ("Ableitung eingeschränkt", "such", "≈"),
          "nicht_gestuetzt": ("Ableitung nicht gestützt", "bad", "✗")}
ERGEBNIS = {"bestanden": "Prüfung bestanden",
            "bestanden_mit_einschraenkungen": "Prüfung bestanden mit Einschränkungen",
            "unvollstaendig": "Prüfung unvollständig", "nicht_bestanden": "Prüfung nicht bestanden"}


STATUS_STUFE = {"angekuendigt": "Angekündigt", "prototyp": "Prototyp", "test": "Test / Demo",
                "kundenauftrag": "Kundenauftrag / Pilot", "im_einsatz": "Im Einsatz", "serie": "Serie / Skala",
                "eingestellt": "Eingestellt", "nicht_belegt": "Status nicht belegt"}
QUELLENTYP = {"geschaeftsbericht": "Geschäftsbericht", "investor": "Investorenunterlage", "produktseite": "Produktseite",
              "datenblatt": "Datenblatt", "pressemitteilung": "Pressemitteilung", "register": "Register",
              "behoerde": "Behörde", "vergabe": "Vergabe", "verband": "Verband", "statistik": "Statistik",
              "medien": "Nachrichtenmedium", "fachmedien": "Fachmedium", "sonstiges": "Sonstiges"}
MEDIEN = {"medien", "fachmedien"}
BERICHTE = {"geschaeftsbericht", "investor"}
BEZIEHUNG = {"Eigentum", "Joint Venture", "Kooperation", "Kunde", "Lieferant", "Projekt", "Lizenz", "Mandat", "historisch"}
BEZIEHUNG_ART = {"direkt", "indirekt", "Überschneidung"}
BETREIBER = {"eigen", "partner", "jv", "kunde", "ausland"}
PRAESENZ_STATUS = {"operativ", "angekündigt"}
REGELN = {
    "unternehmen.profil": "Das Profil hat mindestens vier belegte Zeilen.",
    "unternehmen.medien": "Firmenbasis nutzt mindestens zwei Nachrichten- oder Fachmedien.",
    "personen.quellen": "Je Person mindestens zwei verschiedene Quellen.",
    "portfolio.angebote_je_feld": "Jedes Geschäftsfeld hat mindestens zwei Angebote (Produktfamilien oder Systeme).",
    "portfolio.geschaeftsbericht": "Das Portfolio stützt sich auf mindestens einen Geschäftsbericht oder eine Investorenunterlage.",
    "portfolio.medien": "Das Portfolio nutzt mindestens zwei Nachrichten- oder Fachmedien zur Gegenrecherche.",
    "portfolio.status": "Höchstens die Hälfte der Angebote hat den Status „nicht_belegt“.",
    "cluster.beziehungen": "Mindestens drei belegte Beziehungen.",
    "cluster.bericht": "Mindestens ein ausgewerteter Geschäftsbericht ist protokolliert.",
    "cluster.medien": "Das Cluster nutzt mindestens zwei Nachrichten- oder Fachmedien.",
    "markt.kennzahlen": "Mindestens zwei Marktkennzahlen mit Definition.",
    "markt.vergleich": "Der Vergleich hat mindestens drei Zeilen und drei Kriterien.",
    "markt.medien": "Markt und Wettbewerb nutzen mindestens zwei Nachrichten- oder Fachmedien.",
    "fokus.kennzahlen": "Je Fokusthema mindestens vier Kennzahlen.",
    "fokus.akteure": "Je Fokusthema mindestens drei Akteure.",
    "fokus.kernaussagen": "Je Fokusthema drei bis fünf Kernaussagen.",
}


class Fehler(Exception):
    pass


def lade(pfad):
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def speichere(pfad, daten):
    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=1)
        f.write("\n")


def kapitel_von(cid):
    cid = str(cid)
    if cid.startswith("F_"):
        return "fokus"
    if INTERP_RE.match(cid):
        return "interpretation"
    return KAPITEL.get(cid[:1], "sonstige")


def url_key(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u.split("#")[0].rstrip("/")


# ---------------------------------------------------------------- Zusammenführen
def leer():
    return {"schema": SCHEMA, "auftrag": {}, "phasen": {}, "quellen": [], "claims": [],
            "inhalt": {}, "interpretation": {}, "offen": {"luecken": [], "fragen": []}}


def zusammenfuehren(haupt, teil, ersetzen=False):
    if haupt is None:
        if "auftrag" not in teil:
            raise Fehler("Neue Daten brauchen im ersten Teil den Block 'auftrag'.")
        haupt = leer()
    for k, v in leer().items():
        haupt.setdefault(k, v)
    haupt["schema"] = SCHEMA
    haupt["auftrag"].update(teil.get("auftrag", {}))
    # Quellen: gleiche URL wird zusammengeführt, neue Quellen werden fortlaufend nummeriert.
    nach_url = {url_key(q.get("url")): q for q in haupt["quellen"] if q.get("url")}
    nummern = [int(q["id"][1:]) for q in haupt["quellen"] if SRC_RE.match(str(q.get("id", "")))]
    naechste = max(nummern + [0]) + 1
    umbenennen, neu_q, alt_q = {}, 0, 0
    for q in teil.get("quellen", []):
        q = dict(q)
        alt = q.get("id")
        vorhanden = nach_url.get(url_key(q.get("url"))) if q.get("url") else None
        if vorhanden:
            umbenennen[alt] = vorhanden["id"]
            vorhanden["geoeffnet"] = bool(vorhanden.get("geoeffnet") or q.get("geoeffnet"))
            for feld in ("titel", "herausgeber", "datum", "abruf", "art"):
                if not vorhanden.get(feld) and q.get(feld):
                    vorhanden[feld] = q[feld]
            alt_q += 1
            continue
        q["id"] = "Q%d" % naechste
        naechste += 1
        umbenennen[alt] = q["id"]
        haupt["quellen"].append(q)
        if q.get("url"):
            nach_url[url_key(q["url"])] = q
        neu_q += 1
    claim_index = {c["id"]: i for i, c in enumerate(haupt["claims"])}
    doppelt, neu_c, ersetzt = [], 0, 0
    for c in teil.get("claims", []):
        c = dict(c)
        fehlend = [s for s in c.get("quellen", []) if s not in umbenennen]
        if fehlend:
            raise Fehler("Claim %s verweist auf Quellen, die nicht im selben Teil stehen: %s"
                         % (c.get("id"), ", ".join(map(str, fehlend))))
        c["quellen"] = [umbenennen[s] for s in c.get("quellen", [])]
        if c.get("id") in claim_index:
            i = claim_index[c["id"]]
            if haupt["claims"][i] == c:
                continue
            if not ersetzen:
                doppelt.append(c["id"])
                continue
            haupt["claims"][i] = c
            ersetzt += 1
        else:
            claim_index[c.get("id")] = len(haupt["claims"])
            haupt["claims"].append(c)
            neu_c += 1
    if doppelt:
        raise Fehler("Claim-IDs schon vorhanden (mit --ersetzen überschreiben): " + ", ".join(doppelt))
    for k, v in teil.get("inhalt", {}).items():
        if k in ("fokus", "personen") and isinstance(v, list):
            schluessel = "id" if k == "fokus" else "name"
            liste = haupt["inhalt"].setdefault(k, [])
            for eintrag in v:
                treffer = [i for i, x in enumerate(liste) if x.get(schluessel) == eintrag.get(schluessel)]
                if treffer:
                    liste[treffer[0]] = eintrag
                else:
                    liste.append(eintrag)
        elif k == "portfolio" and isinstance(v, dict) and isinstance(haupt["inhalt"].get(k), dict):
            alt = haupt["inhalt"][k]
            felder = alt.setdefault("felder", [])
            for feld in v.get("felder", []):
                treffer = [i for i, x in enumerate(felder) if x.get("name") == feld.get("name")]
                if treffer:
                    felder[treffer[0]] = feld
                else:
                    felder.append(feld)
            for liste in ("luecken", "ausnahmen"):
                for x in v.get(liste, []):
                    if x not in alt.setdefault(liste, []):
                        alt[liste].append(x)
        else:
            haupt["inhalt"][k] = v
    for k, v in teil.get("interpretation", {}).items():
        haupt["interpretation"][k] = v
    for k in ("luecken", "fragen"):
        for x in teil.get("offen", {}).get(k, []):
            if x not in haupt["offen"].setdefault(k, []):
                haupt["offen"][k].append(x)
    haupt["phasen"].update(teil.get("phasen", {}))
    meldung = "%d Quellen neu, %d mit vorhandenen zusammengeführt, %d Claims neu, %d ersetzt" % (
        neu_q, alt_q, neu_c, ersetzt)
    # Eine vorhandene Prüfung veraltet, sobald sich Fakten oder Inhalte ändern.
    if haupt.get("pruefung") and any(teil.get(k) for k in ("quellen", "claims", "inhalt", "interpretation")):
        haupt.pop("pruefung")
        meldung += "; vorhandene Prüfung entfernt, weil sich Inhalte geändert haben – bitte erneut prüfen lassen"
    if "pruefung" in teil:
        neu = teil["pruefung"]
        if neu is None:
            haupt.pop("pruefung", None)
        elif not haupt.get("pruefung"):
            haupt["pruefung"] = neu
        else:
            alt = haupt["pruefung"]
            for k, v in neu.items():
                if k in ("claims", "ableitungen"):
                    index = {u.get("id"): i for i, u in enumerate(alt.setdefault(k, []))}
                    for u in v:
                        if u.get("id") in index:
                            alt[k][index[u.get("id")]] = u
                        else:
                            alt[k].append(u)
                elif k in ("stichprobe", "hinweise"):
                    alt.setdefault(k, []).extend(x for x in v if x not in alt.get(k, []))
                else:
                    alt[k] = v
            alt.pop("ergebnis", None)
            alt.pop("auswertung", None)
        meldung += "; Prüfdaten übernommen"
    return haupt, meldung


# ---------------------------------------------------------------- Validierung
def alle_verweise(obj, schluessel=("claims", "basis")):
    """Liefert alle Claim-/Basis-Verweise in einer beliebig verschachtelten Struktur."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in schluessel and isinstance(v, list):
                for x in v:
                    yield x
            else:
                yield from alle_verweise(v, schluessel)
    elif isinstance(obj, list):
        for x in obj:
            yield from alle_verweise(x, schluessel)


def zeilen_mit_claims(obj, pfad="inhalt"):
    """Findet Inhaltszeilen mit claims-Liste."""
    if isinstance(obj, dict):
        if isinstance(obj.get("claims"), list):
            yield pfad, next((str(v)[:60] for k, v in obj.items() if k != "claims" and isinstance(v, str) and v), ""), obj["claims"]
        for k, v in obj.items():
            if k != "claims":
                yield from zeilen_mit_claims(v, pfad + "." + k)
    elif isinstance(obj, list):
        for i, x in enumerate(obj):
            yield from zeilen_mit_claims(x, "%s[%d]" % (pfad, i))


def zeilen_ohne_beleg(obj, pfad="inhalt"):
    """Findet Inhaltszeilen mit leerer claims-Liste."""
    if isinstance(obj, dict):
        if "claims" in obj and not obj["claims"]:
            yield pfad, next((str(v)[:60] for k, v in obj.items() if k != "claims" and isinstance(v, str) and v), "")
        for k, v in obj.items():
            if k != "claims":
                yield from zeilen_ohne_beleg(v, pfad + "." + k)
    elif isinstance(obj, list):
        for i, x in enumerate(obj):
            yield from zeilen_ohne_beleg(x, "%s[%d]" % (pfad, i))


def quellen_von(daten, obj):
    """Quellen aller Claims, auf die ein Inhaltsobjekt verweist."""
    claims = {c["id"]: c for c in daten.get("claims", [])}
    quellen = {q["id"]: q for q in daten.get("quellen", [])}
    out = {}
    for cid in alle_verweise(obj, ("claims",)):
        for s in claims.get(cid, {}).get("quellen", []):
            if s in quellen:
                out[s] = quellen[s]
    return out


def anzahl_medien(daten, obj):
    return sum(1 for q in quellen_von(daten, obj).values() if q.get("typ") in MEDIEN or (not q.get("typ") and q.get("art") == "medien"))


def mindestregeln(daten):
    """Liefert (regel, ort, ausnahmen) für jede nicht erfüllte Mindestregel."""
    inhalt = daten.get("inhalt", {})
    out = []

    def pruefe(bedingung, regel, ort, container):
        if not bedingung:
            out.append((regel, ort, container.get("ausnahmen", [])))

    u = inhalt.get("unternehmen")
    if isinstance(u, dict):
        pruefe(len(u.get("profil", [])) >= 4, "unternehmen.profil", "Unternehmen", u)
        pruefe(anzahl_medien(daten, u) >= 2, "unternehmen.medien", "Unternehmen", u)
    for p in inhalt.get("personen", []):
        pruefe(len(quellen_von(daten, p)) >= 2, "personen.quellen", "Person %s" % p.get("name"), p)
    pf = inhalt.get("portfolio")
    if isinstance(pf, dict):
        angebote = []
        for f in pf.get("felder", []):
            pruefe(len(f.get("angebote", [])) >= 2, "portfolio.angebote_je_feld", "Geschäftsfeld %s" % f.get("name"), pf)
            angebote += f.get("angebote", [])
        pruefe(any(q.get("typ") in BERICHTE for q in quellen_von(daten, pf).values()), "portfolio.geschaeftsbericht", "Portfolio", pf)
        pruefe(anzahl_medien(daten, pf) >= 2, "portfolio.medien", "Portfolio", pf)
        offen = sum(1 for a in angebote if a.get("status_stufe") == "nicht_belegt")
        pruefe(not angebote or offen * 2 <= len(angebote), "portfolio.status", "Portfolio", pf)
    cl = inhalt.get("cluster")
    if isinstance(cl, dict):
        pruefe(len(cl.get("beziehungen", [])) >= 3, "cluster.beziehungen", "Cluster", cl)
        pruefe(any(b.get("status") == "analysiert" for b in cl.get("berichte", [])), "cluster.bericht", "Cluster", cl)
        pruefe(anzahl_medien(daten, cl) >= 2, "cluster.medien", "Cluster", cl)
    m = inhalt.get("markt")
    if isinstance(m, dict):
        pruefe(len([k for k in m.get("kennzahlen", []) if k.get("definition")]) >= 2, "markt.kennzahlen", "Markt", m)
        v = m.get("vergleich") or {}
        pruefe(len(v.get("zeilen", [])) >= 3 and len(v.get("kriterien", [])) >= 3, "markt.vergleich", "Markt", m)
        pruefe(anzahl_medien(daten, m) >= 2, "markt.medien", "Markt", m)
    for f in inhalt.get("fokus", []):
        ort = "Fokus %s" % f.get("id")
        pruefe(len(f.get("kennzahlen", [])) >= 4, "fokus.kennzahlen", ort, f)
        pruefe(len(f.get("akteure", [])) >= 3, "fokus.akteure", ort, f)
        pruefe(3 <= len(f.get("kernaussagen", [])) <= 5, "fokus.kernaussagen", ort, f)
    return out


def alle_ausnahmen(daten):
    inhalt = daten.get("inhalt", {})
    for k in ("unternehmen", "portfolio", "cluster", "markt"):
        if isinstance(inhalt.get(k), dict):
            for a in inhalt[k].get("ausnahmen", []):
                yield KAPITEL_TITEL.get(k, k), a
    for p in inhalt.get("personen", []):
        for a in p.get("ausnahmen", []):
            yield "Person %s" % p.get("name"), a
    for f in inhalt.get("fokus", []):
        for a in f.get("ausnahmen", []):
            yield "Fokus %s" % f.get("id"), a


def interpretationen(daten):
    """Alle Interpretationsobjekte mit ID (Summary, Keyfacts, Positionierung, SWOT)."""
    ip = daten.get("interpretation", {})
    out = []
    summ = ip.get("summary", {})
    out += summ.get("highlights", []) + summ.get("kernaussagen", [])
    out += ip.get("keyfacts", []) + ip.get("positionierung", [])
    for q in ("staerken", "schwaechen", "chancen", "risiken"):
        out += ip.get("swot", {}).get(q, [])
    return out


def monate_zurueck(stichtag, monate):
    """Stichtag minus n Kalendermonate, taggenau; Monatsende wird begrenzt."""
    j, m = stichtag.year, stichtag.month - monate
    while m <= 0:
        m += 12
        j -= 1
    return datetime.date(j, m, min(stichtag.day, calendar.monthrange(j, m)[1]))


def validieren(daten):
    fehler, hinweise = [], []
    if daten.get("schema") != SCHEMA:
        fehler.append("schema muss '%s' sein" % SCHEMA)
    a = daten.get("auftrag", {})
    if not a.get("firma"):
        fehler.append("auftrag.firma fehlt")
    stichtag = None
    if not DATE_RE.match(str(a.get("stichtag", ""))):
        fehler.append("auftrag.stichtag fehlt oder ist nicht JJJJ-MM-TT")
    else:
        stichtag = datetime.date.fromisoformat(a["stichtag"])
    if a.get("modus") not in ("voll", "modul"):
        fehler.append("auftrag.modus muss 'voll' oder 'modul' sein")
    qids = [q.get("id") for q in daten.get("quellen", [])]
    for q in daten.get("quellen", []):
        if not SRC_RE.match(str(q.get("id", ""))):
            fehler.append("Quelle mit ungültiger ID: %r" % q.get("id"))
        if not str(q.get("url", "")).startswith(("http://", "https://")):
            fehler.append("Quelle %s: url muss mit http:// oder https:// beginnen" % q.get("id"))
        if not q.get("titel"):
            hinweise.append("Quelle %s ohne Titel" % q.get("id"))
    if len(set(qids)) != len(qids):
        fehler.append("Doppelte Quellen-IDs")
    quellen = {q.get("id"): q for q in daten.get("quellen", [])}
    cids = [c.get("id") for c in daten.get("claims", [])]
    if len(set(cids)) != len(cids):
        fehler.append("Doppelte Claim-IDs: " + ", ".join(sorted({x for x in cids if cids.count(x) > 1})))
    for c in daten.get("claims", []):
        cid = c.get("id")
        if not FACT_RE.match(str(cid)):
            fehler.append("Claim-ID %r passt nicht zu T/H/P/C/M/F_<thema>_ plus Nummer" % cid)
        if not c.get("aussage"):
            fehler.append("Claim %s ohne aussage" % cid)
        if c.get("ursprung") not in URSPRUNG:
            fehler.append("Claim %s: ursprung muss einer von %s sein" % (cid, ", ".join(URSPRUNG)))
        if c.get("stufe") not in ("A", "B"):
            fehler.append("Claim %s: stufe muss A oder B sein" % cid)
        if not c.get("quellen"):
            fehler.append("Claim %s ohne Quelle" % cid)
        for s in c.get("quellen", []):
            if s not in quellen:
                fehler.append("Claim %s verweist auf unbekannte Quelle %s" % (cid, s))
            elif c.get("stufe") == "A" and quellen[s].get("geoeffnet") is False:
                hinweise.append("A-Claim %s stützt sich auf nicht geöffnete Quelle %s" % (cid, s))
        if c.get("stufe") == "A" and not c.get("belegstelle"):
            hinweise.append("A-Claim %s ohne belegstelle" % cid)
        d = c.get("datum")
        if d and DATE_RE.match(str(d)) and stichtag and datetime.date.fromisoformat(d) > stichtag:
            hinweise.append("Claim %s: datum %s liegt nach dem Stichtag" % (cid, d))
    claimset = set(cids)
    ips = interpretationen(daten)
    iids = [i.get("id") for i in ips]
    for i in ips:
        if not INTERP_RE.match(str(i.get("id", ""))):
            fehler.append("Interpretation mit ungültiger ID %r (I… oder S…)" % i.get("id"))
        if not i.get("basis"):
            fehler.append("Interpretation %s ohne basis" % i.get("id"))
    if len(set(iids)) != len(iids):
        fehler.append("Doppelte Interpretations-IDs")
    bekannt = claimset | set(iids)
    for x in set(alle_verweise(daten.get("inhalt", {}))) - claimset:
        fehler.append("Inhalt verweist auf unbekannten Claim %s" % x)
    for x in set(alle_verweise(daten.get("interpretation", {}))) - bekannt:
        fehler.append("Interpretation verweist auf unbekannte ID %s" % x)
    for pfad, zeile in zeilen_ohne_beleg(daten.get("inhalt", {})):
        hinweise.append("Eintrag ohne Beleg in %s: %s" % (pfad, zeile))
    stufe_von = {c.get("id"): c.get("stufe") for c in daten.get("claims", [])}
    for pfad, zeile, ids in zeilen_mit_claims(daten.get("inhalt", {})):
        if ids and all(stufe_von.get(i) == "B" for i in ids):
            fehler.append("Zeile stützt sich nur auf B-Claims (%s) in %s: %s – mindestens ein A-Claim nötig" % (", ".join(ids), pfad, zeile))
    for q in daten.get("quellen", []):
        if q.get("typ") not in QUELLENTYP:
            fehler.append("Quelle %s: typ muss einer von %s sein" % (q.get("id"), ", ".join(QUELLENTYP)))
    for c in daten.get("claims", []):
        if len(str(c.get("aussage", ""))) > 350:
            hinweise.append("Claim %s ist sehr lang; ein Claim soll genau eine Aussage enthalten" % c.get("id"))
    inhalt = daten.get("inhalt", {})
    for f in (inhalt.get("portfolio") or {}).get("felder", []):
        for an in f.get("angebote", []):
            if an.get("status_stufe") not in STATUS_STUFE:
                fehler.append("Angebot %s: status_stufe muss einer von %s sein" % (an.get("name"), ", ".join(STATUS_STUFE)))
            elif an.get("status_stufe") not in ("nicht_belegt",) and not any(
                    next((c for c in daten.get("claims", []) if c.get("id") == i), {}).get("datum") for i in an.get("claims", [])):
                hinweise.append("Angebot %s: Status ohne datierten Beleg" % an.get("name"))
    for b in (inhalt.get("cluster") or {}).get("beziehungen", []):
        if b.get("typ") not in BEZIEHUNG:
            fehler.append("Beziehung %s–%s: typ muss einer von %s sein" % (b.get("von"), b.get("zu"), ", ".join(sorted(BEZIEHUNG))))
        if b.get("art") not in BEZIEHUNG_ART:
            fehler.append("Beziehung %s–%s: art muss direkt, indirekt oder Überschneidung sein" % (b.get("von"), b.get("zu")))
    for reg in (inhalt.get("markt") or {}).get("praesenz", []):
        for akt in reg.get("aktivitaeten", []):
            if akt.get("betreiber") not in BETREIBER or akt.get("status") not in PRAESENZ_STATUS:
                fehler.append("Präsenz %s/%s: betreiber muss eigen, partner, jv, kunde oder ausland sein, status operativ oder angekündigt" % (
                    reg.get("region"), akt.get("standort")))
    for ort, aus in alle_ausnahmen(daten):
        if aus.get("regel") not in REGELN:
            fehler.append("%s: Ausnahme für unbekannte Regel %r" % (ort, aus.get("regel")))
        elif len(str(aus.get("grund", ""))) < 40:
            fehler.append("%s: Ausnahme %s braucht einen konkreten Grund mit Suchumfang (mindestens 40 Zeichen)" % (ort, aus.get("regel")))
    for regel, ort, ausnahmen in mindestregeln(daten):
        if not any(x.get("regel") == regel for x in ausnahmen):
            fehler.append("Mindestregel %s nicht erfüllt (%s): %s Weiter recherchieren; nur wenn öffentlich nichts zu finden ist, "
                          "eine Ausnahme mit konkretem Grund eintragen." % (regel, ort, REGELN[regel]))
    genutzt = set(alle_verweise(daten.get("inhalt", {}))) | set(alle_verweise(daten.get("interpretation", {})))
    for c in sorted(claimset - genutzt):
        hinweise.append("Claim %s wird nur im Faktenregister gezeigt" % c)
    for s in sorted(set(quellen) - {s for c in daten.get("claims", []) for s in c.get("quellen", [])}):
        hinweise.append("Quelle %s wird von keinem Claim genutzt" % s)
    ip = daten.get("interpretation", {})
    for q in ("staerken", "schwaechen", "chancen", "risiken"):
        if len(ip.get("swot", {}).get(q, [])) > 3:
            fehler.append("SWOT %s: höchstens drei Punkte" % q)
    if a.get("modus") == "voll" and ip:
        n = len(ip.get("summary", {}).get("kernaussagen", []))
        if not 4 <= n <= 6:
            hinweise.append("Executive Summary hat %d Kernaussagen, vorgesehen sind 4 bis 6" % n)
        if len(ip.get("summary", {}).get("highlights", [])) > 3:
            fehler.append("Executive Summary: höchstens drei Highlights")
    fokus_ids = {f.get("id") for f in a.get("fokus", [])}
    for f in daten.get("inhalt", {}).get("fokus", []):
        if f.get("id") not in fokus_ids:
            hinweise.append("Fokusthema %s steht nicht im Auftrag" % f.get("id"))
        for x in alle_verweise(f):
            if not str(x).startswith("F_%s_" % f.get("id")):
                hinweise.append("Fokus %s nutzt Claim %s ohne Präfix F_%s_" % (f.get("id"), x, f.get("id")))
    if stichtag:
        grenze4, grenze6 = monate_zurueck(stichtag, 4), monate_zurueck(stichtag, 6)
        for t in daten.get("inhalt", {}).get("unternehmen", {}).get("timeline", []):
            if not DATE_RE.match(str(t.get("datum", ""))):
                hinweise.append("Timeline-Eintrag ohne gültiges Datum: %s" % t.get("ereignis"))
            elif datetime.date.fromisoformat(t["datum"]) < grenze4:
                hinweise.append("Timeline-Eintrag %s liegt vor dem Viermonatsfenster" % t["datum"])
            elif datetime.date.fromisoformat(t["datum"]) > stichtag:
                hinweise.append("Timeline-Eintrag %s liegt nach dem Stichtag" % t["datum"])
        for f in daten.get("inhalt", {}).get("fokus", []):
            for t in f.get("entwicklungen", []):
                if DATE_RE.match(str(t.get("datum", ""))) and datetime.date.fromisoformat(t["datum"]) < grenze6:
                    hinweise.append("Fokus %s: Entwicklung %s liegt vor dem Sechsmonatsfenster" % (f.get("id"), t["datum"]))
    p = daten.get("pruefung")
    if p:
        for u in p.get("claims", []):
            if u.get("id") not in claimset:
                fehler.append("Prüfurteil für unbekannten Claim %s" % u.get("id"))
            if u.get("urteil") not in ("im_original_bestaetigt", "durch_suche_gestuetzt", "abweichend",
                                       "nicht_belegt", "nicht_erreichbar", "nicht_einzeln_geprueft"):
                fehler.append("Prüfurteil für %s ungültig: %r" % (u.get("id"), u.get("urteil")))
        for u in p.get("ableitungen", []):
            if u.get("id") not in set(iids):
                fehler.append("Ableitungsurteil für unbekannte Interpretation %s" % u.get("id"))
            if u.get("urteil") not in ("gestuetzt", "eingeschraenkt", "nicht_gestuetzt"):
                fehler.append("Ableitungsurteil für %s ungültig: %r" % (u.get("id"), u.get("urteil")))
    return fehler, hinweise


# ---------------------------------------------------------------- Prüfung auswerten
def im_umfang(daten, cid):
    umfang = daten.get("pruefung", {}).get("umfang", {})
    kap = umfang.get("kapitel", "alle") if isinstance(umfang, dict) else "alle"
    return kap == "alle" or kapitel_von(cid) in kap


def auswerten(daten):
    p = daten.get("pruefung")
    if not p:
        raise Fehler("Keine Prüfdaten vorhanden.")
    nur_a = isinstance(p.get("umfang"), dict) and p["umfang"].get("nur_a")
    urteile = {u["id"]: u for u in p.get("claims", [])}
    abl = {u["id"]: u for u in p.get("ableitungen", [])}
    stufe = {c["id"]: c.get("stufe") for c in daten.get("claims", [])}
    offen, schlecht, einschr = [], [], []
    for c in daten.get("claims", []):
        cid = c["id"]
        if not im_umfang(daten, cid) or (nur_a and c.get("stufe") != "A"):
            continue
        u = urteile.get(cid, {}).get("urteil")
        if c.get("stufe") == "A":
            if u in (None, "nicht_einzeln_geprueft", "nicht_erreichbar"):
                offen.append(cid)
            elif u in ("abweichend", "nicht_belegt"):
                schlecht.append(cid)
            elif u == "durch_suche_gestuetzt":
                einschr.append(cid)
        elif u in ("abweichend", "nicht_belegt"):
            einschr.append(cid)
    for i in interpretationen(daten):
        iid = i["id"]
        if not im_umfang(daten, iid):
            continue
        u = abl.get(iid, {}).get("urteil")
        if u is None:
            offen.append(iid)
        elif u == "nicht_gestuetzt":
            schlecht.append(iid)
        elif u == "eingeschraenkt":
            einschr.append(iid)
    falsch = {cid for cid, u in urteile.items() if u.get("urteil") in ("abweichend", "nicht_belegt")}
    betroffen = sorted({i["id"] for i in interpretationen(daten) if falsch & set(i.get("basis", []))})
    if schlecht:
        ergebnis = "nicht_bestanden"
    elif offen:
        ergebnis = "unvollstaendig"
    elif einschr or (isinstance(p.get("umfang"), dict) and (p["umfang"].get("kapitel", "alle") != "alle" or nur_a)):
        ergebnis = "bestanden_mit_einschraenkungen"
    else:
        ergebnis = "bestanden"
    p["ergebnis"] = ergebnis
    p["auswertung"] = {"nicht_bestanden_wegen": schlecht, "offen": offen, "eingeschraenkt": einschr,
                       "betroffene_ableitungen": betroffen, "a_claims": sum(1 for v in stufe.values() if v == "A")}
    return ergebnis, p["auswertung"]


# ---------------------------------------------------------------- HTML
CSS = """
*{box-sizing:border-box}body{margin:0;background:#f3f6f8;color:#173345;font:15px/1.55 Arial,Helvetica,sans-serif}
a{color:#154c61;text-underline-offset:3px}.mast{background:#132d40;color:#fff}.mast>div{max-width:1200px;margin:auto;padding:22px 30px}
.mast h1{margin:4px 0;font-size:28px}.mast p{margin:4px 0}.badge{font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:#e7c690}
.banner{display:inline-block;margin-top:8px;padding:5px 11px;border-radius:6px;font-size:13px;font-weight:700;color:#fff;background:#c3872d}
.banner.ok{background:#16734a}.banner.such{background:#235c9b}.banner.bad{background:#b3343c}.banner.warn{background:#9b5c14}
nav{position:sticky;top:0;background:#fff;border-bottom:1px solid #cfdce2;padding:9px 22px;display:flex;gap:7px;overflow:auto;z-index:2}
nav a{background:#f0f5f7;border:1px solid #d6e1e6;border-radius:7px;padding:6px 12px;text-decoration:none;white-space:nowrap;font-size:13px}
main{max-width:1200px;margin:auto;padding:20px 26px}section{background:#fff;border:1px solid #dbe4e8;border-radius:12px;padding:18px 22px;margin:0 0 18px;scroll-margin-top:64px}
h2{font-size:21px;margin:0 0 12px;padding-bottom:8px;border-bottom:2px solid #dce8eb}h3{font-size:16px;margin:16px 0 6px}
.meta,small{color:#607887;font-size:12px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px}
.hl{background:#f2f7f9;border-top:3px solid #176274;border-radius:9px;padding:11px 14px}.hl .l{font-size:12px;font-weight:700;color:#365562}
.hl .w{font-size:25px;font-weight:700;color:#154c61;margin:3px 0}.hl .b{font-size:12px;color:#607887}
details.k{background:#f7fafb;border:1px solid #dbe7eb;border-radius:9px;padding:9px 13px;margin:7px 0}details.k[open]{border-left:3px solid #c3872d}
details.k summary{font-weight:600;cursor:pointer}details.k p{margin:7px 0}
.chip{display:inline-block;margin:1px 3px 1px 0;padding:0 6px;border-radius:5px;background:#e6eff2;font-size:11.5px;text-decoration:none;white-space:nowrap}
.chip.ok{background:#e3f3ea;color:#16734a}.chip.such{background:#e8f0fd;color:#235c9b}.chip.bad{background:#fde8ea;color:#b3343c;font-weight:700}
.chip.warn{background:#fff3e0;color:#9b5c14}.chip.none{background:#eef1f3;color:#5b6b75}
.o{display:inline-block;padding:0 6px;border-radius:5px;font-size:11px;font-weight:700;margin-right:4px}
.o.fakt{background:#e3f3ea;color:#16734a}.o.hersteller,.o.partner{background:#fff3e0;color:#9b5c14}.o.medien{background:#eef5ff;color:#235c9b}
.o.nutzer{background:#eef1f3;color:#5b6b75}.o.interpretation{background:#f1e9ff;color:#6b3fa0}
.tw{overflow-x:auto;border:1px solid #dbe5e9;border-radius:8px;margin:10px 0}table{border-collapse:collapse;width:100%;font-size:13.5px}
td,th{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid #dce7eb}th{background:#eef4f6}tbody tr:last-child td{border-bottom:0}
.tl{border-left:2px solid #b9d0dc;padding-left:15px}.ev{display:grid;grid-template-columns:105px 1fr;gap:12px;margin-bottom:8px}
.ev time{font-weight:600;color:#154c61;font-size:12px;padding-top:2px}.swot{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.q{border:1px solid #dce6ea;border-top:4px solid var(--a);border-radius:9px;padding:12px;background:var(--b)}
.q h3{margin:0 0 6px;color:var(--a);font-size:13px;text-transform:uppercase;letter-spacing:.06em}
.qs{--a:#16734a;--b:#edf8f1}.qw{--a:#b3343c;--b:#fff0f1}.qo{--a:#235c9b;--b:#eef5ff}.qt{--a:#9b5c14;--b:#fff5e8}
.lu{border-left:3px solid #b3343c;padding-left:10px;color:#6b2a2f;margin:5px 0}.beleg{border-bottom:1px solid #e3ebef;padding:8px 0;scroll-margin-top:64px}
.beleg:target{background:#fff8ea}.u{font-size:12px;margin-top:3px}footer{max-width:1200px;margin:0 auto;padding:0 28px 24px;color:#607887;font-size:12px}
@media(max-width:760px){.swot{grid-template-columns:1fr}.ev{grid-template-columns:1fr}}
@media print{body{background:#fff;font-size:10pt}nav{display:none}.mast{background:#fff;color:#173345}section{border:0;border-bottom:1px solid #ddd;break-inside:auto}
details.k{break-inside:avoid}details:not([open])>*:not(summary){display:block}.q{print-color-adjust:exact}}
"""


def e(x):
    return html.escape("" if x is None else str(x), quote=True)


def sichere_url(u):
    return u if str(u).startswith(("http://", "https://")) else "#"


class Ausgabe:
    def __init__(self, daten):
        self.d = daten
        self.p = daten.get("pruefung") or {}
        self.urteil = {u["id"]: u for u in self.p.get("claims", [])}
        self.urteil.update({u["id"]: u for u in self.p.get("ableitungen", [])})
        self.claims = {c["id"]: c for c in daten.get("claims", [])}
        self.quellen = {q["id"]: q for q in daten.get("quellen", [])}
        self.nav = []

    def chips(self, ids):
        out = []
        for i in ids or []:
            ziel = "#c-" if i in self.claims else "#i-"
            u = self.urteil.get(i, {}).get("urteil")
            if self.p and u is None and i in self.claims and im_umfang(self.d, i):
                u = "nicht_einzeln_geprueft"
            if u in URTEIL:
                text, klasse, zeichen = URTEIL[u]
                out.append('<a class="chip %s" href="%s%s" title="%s">%s %s</a>' % (klasse, ziel, e(i), e(text), zeichen, e(i)))
            else:
                out.append('<a class="chip" href="%s%s">%s</a>' % (ziel, e(i), e(i)))
        return "".join(out)

    def tabelle(self, spalten, zeilen, claims="claims"):
        if not zeilen:
            return ""
        kopf = "".join("<th>%s</th>" % e(t) for _, t in spalten) + ("<th>Belege</th>" if claims else "")
        rumpf = []
        for z in zeilen:
            zellen = "".join("<td>%s</td>" % e(", ".join(z[k]) if isinstance(z.get(k), list) else z.get(k, "")) for k, _ in spalten)
            if claims:
                zellen += "<td>%s</td>" % self.chips(z.get(claims))
            rumpf.append("<tr>%s</tr>" % zellen)
        return '<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (kopf, "".join(rumpf))

    def luecken(self, liste, ausnahmen=None):
        out = "".join('<p class="lu">Lücke: %s</p>' % e(x) for x in liste or [])
        return out + "".join('<p class="lu">Ausnahme von der Mindestregel „%s“: %s</p>' % (
            e(REGELN.get(a.get("regel"), a.get("regel"))), e(a.get("grund"))) for a in ausnahmen or [])

    def zeitleiste(self, eintraege):
        if not eintraege:
            return ""
        rows = sorted(eintraege, key=lambda t: str(t.get("datum", "")), reverse=True)
        return '<div class="tl">%s</div>' % "".join(
            '<div class="ev"><time>%s</time><div>%s%s %s</div></div>' % (
                e(t.get("datum")), e(t.get("ereignis") or t.get("titel")),
                (" · <small>%s</small>" % e(t.get("status") or t.get("kategorie"))) if (t.get("status") or t.get("kategorie")) else "",
                self.chips(t.get("claims"))) for t in rows)

    def karte(self, i, titel, text, felder=()):
        teile = ['<p><span class="o interpretation">Interpretation</span>%s</p>' % e(text)]
        for k, t in felder:
            if i.get(k):
                teile.append("<p><b>%s:</b> %s</p>" % (e(t), e(i[k])))
        teile.append("<p><small>Basis:</small> %s</p>" % self.chips(i.get("basis")))
        return '<details class="k" id="i-%s"><summary>%s %s</summary>%s</details>' % (
            e(i.get("id")), e(titel), self.chips([i.get("id")]) if self.p else "", "".join(teile))

    def keyfacts(self, modul):
        kf = [k for k in self.d.get("interpretation", {}).get("keyfacts", []) if k.get("modul") == modul]
        if not kf:
            return ""
        return "<h3>Keyfacts &amp; Insights</h3>" + "".join(
            self.karte(k, k.get("titel"), k.get("insight"), (("fakt", "Fakt"), ("unsicherheit", "Unsicherheit"))) for k in kf)

    def abschnitt(self, aid, titel, rumpf):
        if not rumpf.strip():
            return ""
        self.nav.append((aid, titel))
        return '<section id="%s"><h2>%s</h2>%s</section>' % (e(aid), e(titel), rumpf)

    # -- Kapitel
    def summary(self):
        s = self.d.get("interpretation", {}).get("summary", {})
        hl = "".join('<div class="hl" id="i-%s"><div class="l">%s</div><div class="w">%s</div><div class="b">%s · %s</div><div>%s</div></div>' % (
            e(h.get("id")), e(h.get("label")), e(h.get("wert")), e(h.get("bezug")), e(h.get("zeitraum")),
            self.chips([h.get("id")] if self.p else []) + self.chips(h.get("basis"))) for h in s.get("highlights", []))
        ka = "".join(self.karte(k, k.get("titel"), k.get("aussage"), (("vorschau", "Kurzfassung"), ("begruendung", "Begründung"),
                                                                   ("unsicherheit", "Unsicherheit"))) for k in s.get("kernaussagen", []))
        return self.abschnitt("summary", "Executive Summary", ('<div class="grid">%s</div>' % hl if hl else "") + ka)

    def unternehmen(self):
        u = self.d.get("inhalt", {}).get("unternehmen", {})
        r = self.tabelle([("feld", "Merkmal"), ("wert", "Angabe")], u.get("profil"))
        if u.get("timeline"):
            r += "<h3>Entwicklungen der letzten vier Monate</h3>" + self.zeitleiste(u["timeline"])
        return self.abschnitt("unternehmen", "Unternehmen und aktuelle Entwicklungen", r + self.luecken(u.get("luecken"), u.get("ausnahmen")))

    def portfolio(self):
        p = self.d.get("inhalt", {}).get("portfolio", {})
        r = ""
        for f in p.get("felder", []):
            zeilen = [dict(a, stufe=STATUS_STUFE.get(a.get("status_stufe"), "")) for a in f.get("angebote", [])]
            r += "<h3>%s</h3>" % e(f.get("name")) + self.tabelle(
                [("name", "Angebot"), ("anwendung", "Anwendung"), ("eigenschaften", "Belegte Eigenschaften"), ("stufe", "Stufe"), ("status", "Status laut Beleg")], zeilen)
        if r or p.get("luecken"):
            r += self.keyfacts("portfolio")
        return self.abschnitt("portfolio", "Portfolio", r + self.luecken(p.get("luecken"), p.get("ausnahmen")))

    def cluster(self):
        c = self.d.get("inhalt", {}).get("cluster", {})
        r = self.tabelle([("von", "Von"), ("zu", "Zu"), ("typ", "Beziehung"), ("gegenstand", "Gegenstand"),
                          ("anteil_rolle", "Anteil / Rolle"), ("art", "direkt / indirekt"), ("status", "Status"), ("datum", "Datum")], c.get("beziehungen"))
        if c.get("berichte"):
            r += "<h3>Ausgewertete Geschäftsberichte</h3>" + self.tabelle(
                [("akteur", "Akteur"), ("bericht", "Bericht"), ("jahr", "Geschäftsjahr"), ("abschnitte", "Geprüfte Abschnitte"), ("status", "Status")],
                c["berichte"], claims=None)
        if r:
            r += self.keyfacts("cluster")
        return self.abschnitt("cluster", "Struktur, Partner und Kunden", r + self.luecken(c.get("luecken"), c.get("ausnahmen")))

    def markt(self):
        m = self.d.get("inhalt", {}).get("markt", {})
        r = self.tabelle([("kennzahl", "Kennzahl"), ("wert", "Wert"), ("definition", "Definition / Jahr")], m.get("kennzahlen"))
        v = m.get("vergleich") or {}
        if v.get("zeilen"):
            krit = v.get("kriterien", [])
            kopf = "<th>Unternehmen / Angebot</th>" + "".join('<th title="%s">%s</th>' % (e(k.get("definition")), e(k.get("name"))) for k in krit)
            zeilen = ""
            for z in v["zeilen"]:
                zellen = ""
                for k in krit:
                    zelle = (z.get("zellen") or {}).get(k.get("id")) or {}
                    zellen += "<td>%s %s</td>" % (e(zelle.get("text") or "nicht öffentlich belegt"), self.chips(zelle.get("claims")))
                zeilen += "<tr><th>%s<br><small>%s</small></th>%s</tr>" % (e(z.get("akteur")), e(z.get("angebot")), zellen)
            r += "<h3>Vergleich%s</h3>" % (" · " + e(v["einheit"]) if v.get("einheit") else "")
            r += '<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (kopf, zeilen)
            r += '<p class="meta">„nicht öffentlich belegt“ beschreibt eine Datenlücke, keine Schwäche.</p>'
        praesenz = []
        for reg in m.get("praesenz", []):
            for akt in reg.get("aktivitaeten", []):
                praesenz.append(dict(akt, region=reg.get("region")))
        if praesenz:
            r += "<h3>Regionale Präsenz</h3>" + self.tabelle([("region", "Region"), ("akteur", "Rechtsträger / Akteur"), ("standort", "Standort"),
                                                              ("funktion", "Funktion"), ("betreiber", "Rolle"), ("status", "Status")], praesenz)
        if r:
            r += self.keyfacts("markt")
        return self.abschnitt("markt", "Markt und Wettbewerb", r + self.luecken(m.get("luecken"), m.get("ausnahmen")))

    def positionierung(self):
        pos = self.d.get("interpretation", {}).get("positionierung", [])
        r = "".join(self.karte(p, "%s: %s" % (p.get("dimension", ""), p.get("urteil", "")), p.get("aussage"),
                               (("methode", "Methode"), ("begruendung", "Begründung"), ("unsicherheit", "Unsicherheit"))) for p in pos)
        g = self.d.get("interpretation", {}).get("grenzen", [])
        if r and g:
            r += "<h3>Gemeinsame Grenzen</h3><ul>%s</ul>" % "".join("<li>%s</li>" % e(x) for x in g)
        return self.abschnitt("positionierung", "Positionierung", r)

    def swot(self):
        s = self.d.get("interpretation", {}).get("swot", {})
        if not any(s.get(q) for q in ("staerken", "schwaechen", "chancen", "risiken")):
            return ""
        teile = ""
        for q, t, k in (("staerken", "Stärken", "qs"), ("schwaechen", "Schwächen", "qw"), ("chancen", "Chancen", "qo"), ("risiken", "Risiken", "qt")):
            teile += '<div class="q %s"><h3>%s</h3>%s</div>' % (k, t, "".join(
                self.karte(p, p.get("titel"), p.get("aussage"), (("begruendung", "Begründung"), ("einschraenkung", "Einschränkung"))) for p in s.get(q, []))
                or "<p class='meta'>Kein belegter Punkt.</p>")
        return self.abschnitt("swot", "SWOT (themenbezogen)", '<div class="swot">%s</div>' % teile)

    def personen(self):
        out = ""
        for n, p in enumerate(self.d.get("inhalt", {}).get("personen", []), 1):
            r = '<p class="meta">Position laut Nutzer: %s · Verifizierung: %s</p>' % (e(p.get("position_laut_nutzer")), e(p.get("verifizierung", "nicht verifiziert")))
            if p.get("einleitung"):
                r += "<p>%s %s</p>" % (e(p["einleitung"].get("text")), self.chips(p["einleitung"].get("claims")))
            r += self.tabelle([("feld", "Merkmal"), ("wert", "Angabe")], p.get("snapshot"))
            if p.get("werdegang"):
                r += "<h3>Werdegang</h3>" + self.tabelle([("zeitraum", "Zeitraum"), ("organisation", "Organisation"), ("rolle", "Rolle"), ("kontext", "Kontext")], p["werdegang"])
            for k, t in (("fachprofil", "Fachprofil"), ("verantwortung", "Verantwortung")):
                if p.get(k):
                    r += "<h3>%s</h3><ul>%s</ul>" % (t, "".join("<li><b>%s:</b> %s %s</li>" % (e(x.get("titel")), e(x.get("text")), self.chips(x.get("claims"))) for x in p[k]))
            if p.get("medien"):
                r += "<h3>Äußerungen und Medienpräsenz der letzten vier Monate</h3>" + self.zeitleiste(p["medien"])
            out += self.abschnitt("person-%d" % n, "Gesprächspartner: %s" % p.get("name", ""), r + self.luecken(p.get("luecken"), p.get("ausnahmen")))
        return out

    def fokus(self):
        out = ""
        for f in self.d.get("inhalt", {}).get("fokus", []):
            r = ""
            if f.get("definition"):
                r += "<h3>Thema verstehen</h3><p>%s %s</p>" % (e(f["definition"].get("text")), self.chips(f["definition"].get("claims")))
            if f.get("kennzahlen"):
                r += "<h3>Zahlen</h3>" + self.tabelle([("kennzahl", "Kennzahl"), ("wert", "Wert"), ("definition", "Definition / Zeitraum / Abgrenzung")], f["kennzahlen"])
            if f.get("segmente"):
                r += "<h3>Segmente und Wertschöpfung</h3>" + self.tabelle([("titel", "Segment / Stufe"), ("text", "Beschreibung")], f["segmente"])
            if f.get("akteure"):
                r += "<h3>Akteure</h3>" + self.tabelle([("akteur", "Akteur"), ("rolle", "Rolle"), ("angebot", "Belegte Aktivität")], f["akteure"])
            if f.get("kernaussagen"):
                r += "<h3>Kernaussagen</h3>" + "".join('<details class="k"><summary>%s</summary><p><span class="o fakt">Fakt</span>%s %s</p></details>' % (
                    e(k.get("titel")), e(k.get("text")), self.chips(k.get("claims"))) for k in f["kernaussagen"])
            if f.get("entwicklungen"):
                r += "<h3>Entwicklungen der letzten sechs Monate</h3>" + self.zeitleiste(f["entwicklungen"])
            if f.get("fragen"):
                r += "<h3>Fragen für das Gespräch</h3><ol>%s</ol>" % "".join("<li>%s</li>" % e(x) for x in f["fragen"])
            out += self.abschnitt("fokus-%s" % f.get("id"), "Fokus: %s" % f.get("titel", ""), r + self.luecken(f.get("luecken"), f.get("ausnahmen")))
        return out

    def offen(self):
        o = self.d.get("offen", {})
        r = self.luecken(o.get("luecken"))
        if o.get("fragen"):
            r += "<h3>Fragen für das Gespräch</h3><ol>%s</ol>" % "".join("<li>%s</li>" % e(x) for x in o["fragen"])
        return self.abschnitt("offen", "Offene Punkte und Gesprächsfragen", r)

    def pruefbericht(self):
        if not self.p:
            return ""
        a = self.p.get("auswertung", {})
        zaehler = {}
        for u in self.p.get("claims", []) + self.p.get("ableitungen", []):
            zaehler[u.get("urteil")] = zaehler.get(u.get("urteil"), 0) + 1
        r = "<p><b>%s.</b> %s</p>" % (e(ERGEBNIS.get(self.p.get("ergebnis"), "Prüfung nicht ausgewertet")), e(self.p.get("zusammenfassung")))
        u = self.p.get("umfang") if isinstance(self.p.get("umfang"), dict) else {}
        kap = u.get("kapitel", "alle")
        umfang = "alle Kapitel" if kap == "alle" else ", ".join(KAPITEL_TITEL.get(k, k) for k in kap)
        r += '<p class="meta">Stand %s · Umfang: %s%s</p>' % (e(self.p.get("stand")), e(umfang), " · nur A-Fakten" if u.get("nur_a") else "")
        r += self.tabelle([("u", "Urteil"), ("n", "Anzahl")], [{"u": URTEIL.get(k, (k,))[0], "n": v} for k, v in sorted(zaehler.items(), key=lambda x: str(x[0]))], claims=None)
        for titel, ids in (("Nicht bestanden wegen", a.get("nicht_bestanden_wegen")), ("Noch offen", a.get("offen")),
                           ("Mit Einschränkung", a.get("eingeschraenkt")), ("Betroffene Ableitungen", a.get("betroffene_ableitungen"))):
            if ids:
                r += "<p><b>%s:</b> %s</p>" % (titel, self.chips(ids))
        befunde = [u for u in self.p.get("claims", []) + self.p.get("ableitungen", []) if u.get("korrektur") or u.get("urteil") in ("abweichend", "nicht_belegt", "nicht_gestuetzt")]
        if befunde:
            r += "<h3>Befunde und Korrekturvorschläge</h3>" + self.tabelle(
                [("id", "ID"), ("u", "Urteil"), ("begruendung", "Befund"), ("korrektur", "Korrekturvorschlag")],
                [dict(b, u=URTEIL.get(b.get("urteil"), ("",))[0]) for b in befunde], claims=None)
        if self.p.get("stichprobe"):
            r += "<h3>Stichproben</h3>" + self.tabelle([("gruppe", "Gruppe"), ("auswahl", "Auswahl"), ("ergebnis", "Ergebnis")], self.p["stichprobe"], claims=None)
        if self.p.get("hinweise"):
            r += "<h3>Hinweise</h3><ul>%s</ul>" % "".join("<li>%s</li>" % e(x) for x in self.p["hinweise"])
        return self.abschnitt("pruefbericht", "Prüfbericht", r)

    def belege(self):
        gruppen = {}
        for c in self.d.get("claims", []):
            gruppen.setdefault(kapitel_von(c["id"]), []).append(c)
        r = ""
        for kap in ("unternehmen", "personen", "portfolio", "cluster", "markt", "fokus", "sonstige"):
            if kap not in gruppen:
                continue
            r += "<h3>%s</h3>" % e(KAPITEL_TITEL.get(kap, "Sonstige"))
            for c in gruppen[kap]:
                q = "; ".join('<a href="#q-%s">[%s]</a> <a href="%s" rel="noopener">%s</a>' % (
                    e(s), e(s), e(sichere_url(self.quellen.get(s, {}).get("url", "#"))), e(self.quellen.get(s, {}).get("titel", s))) for s in c.get("quellen", []))
                meta = " · ".join(e(x) for x in (c.get("status"), c.get("datum"), "Stufe " + str(c.get("stufe", ""))) if x)
                u = self.urteil.get(c["id"])
                pr = ""
                if u:
                    pr = '<div class="u">%s %s%s</div>' % (self.chips([c["id"]]), e(u.get("begruendung")),
                                                           (" · <b>Korrektur:</b> " + e(u["korrektur"])) if u.get("korrektur") else "")
                r += '<div class="beleg" id="c-%s"><b>%s</b> <span class="o %s">%s</span>%s<div class="meta">%s · Belegstelle: %s%s</div><div class="u">%s</div>%s</div>' % (
                    e(c["id"]), e(c["id"]), e(c.get("ursprung")), e(URSPRUNG.get(c.get("ursprung"), c.get("ursprung"))), e(c.get("aussage")), meta,
                    e(c.get("belegstelle") or "nicht angegeben"), (" · Unsicherheit: " + e(c["unsicherheit"])) if c.get("unsicherheit") else "", q, pr)
        return self.abschnitt("belege", "Faktenregister", r)

    def quellenregister(self):
        nutzung = {}
        for c in self.d.get("claims", []):
            for s in c.get("quellen", []):
                nutzung.setdefault(s, []).append(c["id"])
        zeilen = "".join('<tr id="q-%s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href="%s" rel="noopener">%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
            e(q["id"]), e(q["id"]), e(q.get("titel")), e(q.get("herausgeber")), e(q.get("datum")), e(sichere_url(q.get("url", "#"))),
            e(re.sub(r"^https?://(www\.)?", "", q.get("url", ""))[:60]), e(q.get("abruf")), e(QUELLENTYP.get(q.get("typ"), q.get("art"))),
            "geöffnet" if q.get("geoeffnet") else "nicht geöffnet, nur Suchtreffer", self.chips(nutzung.get(q["id"]))) for q in self.d.get("quellen", []))
        if not zeilen:
            return ""
        return self.abschnitt("quellen", "Quellenregister", '<div class="tw"><table><thead><tr><th>Nr.</th><th>Titel</th><th>Herausgeber</th><th>Datum</th><th>Link</th><th>Abruf</th><th>Typ</th><th>Status</th><th>Claims</th></tr></thead><tbody>%s</tbody></table></div>' % zeilen)

    def abnahme(self, hinweise):
        qs = self.d.get("quellen", [])
        punkte = ["Stichtag: %s" % self.d.get("auftrag", {}).get("stichtag"),
                  "Modus: %s" % self.d.get("auftrag", {}).get("modus"),
                  "Kapitel: %s" % ", ".join(t for _, t in self.nav),
                  "Claims: %d, davon A: %d" % (len(self.d.get("claims", [])), sum(1 for c in self.d.get("claims", []) if c.get("stufe") == "A")),
                  "Quellen: %d, geöffnet: %d, nur Suchtreffer: %d" % (len(qs), sum(1 for q in qs if q.get("geoeffnet")), sum(1 for q in qs if not q.get("geoeffnet"))),
                  "Phasen: %s" % (", ".join("%s=%s" % kv for kv in self.d.get("phasen", {}).items()) or "nicht angegeben"),
                  "Begründete Ausnahmen von Mindestregeln: %d" % len(list(alle_ausnahmen(self.d))),
                  ERGEBNIS.get(self.p.get("ergebnis"), "Prüfung nicht ausgewertet") if self.p else "Ohne unabhängige Quellenprüfung erstellt.",
                  "Gerendert mit briefing.py %s" % VERSION]
        r = "<ul>%s</ul>" % "".join("<li>%s</li>" % e(x) for x in punkte)
        if hinweise:
            r += "<details class='k'><summary>Technische Hinweise der Validierung (%d)</summary><ul>%s</ul></details>" % (
                len(hinweise), "".join("<li>%s</li>" % e(h) for h in hinweise))
        return self.abschnitt("abnahme", "Abnahme", r)

    def seite(self, hinweise):
        a = self.d.get("auftrag", {})
        rumpf = (self.summary() + self.unternehmen() + self.portfolio() + self.cluster() + self.markt() + self.positionierung()
                 + self.swot() + self.personen() + self.fokus() + self.offen() + self.pruefbericht() + self.belege() + self.quellenregister())
        rumpf += self.abnahme(hinweise)
        if self.p:
            erg = self.p.get("ergebnis")
            klasse = {"bestanden": "ok", "bestanden_mit_einschraenkungen": "such", "nicht_bestanden": "bad"}.get(erg, "warn")
            banner = '<span class="banner %s">%s – Details im Prüfbericht.</span>' % (klasse, e(ERGEBNIS.get(erg, "Prüfung nicht ausgewertet")))
        else:
            banner = '<span class="banner">Ungeprüfte Faktenbasis. Quellen vor Verwendung prüfen oder Prüfung anfordern.</span>'
        personen = "; ".join("%s (%s, %s)" % (p.get("name"), p.get("position_laut_nutzer") or "Position offen", p.get("verifizierung", "laut Nutzer, nicht verifiziert"))
                             for p in a.get("personen", []))
        kopf = '<header class="mast"><div><div class="badge">Firmenbriefing · Gesprächsvorbereitung</div><h1>%s</h1>' % e(a.get("firma"))
        if a.get("modus") == "modul":
            kopf += "<p>Modulauftrag: %s</p>" % e(", ".join(MODULE.get(m, m) for m in a.get("module", [])) or "nicht angegeben")
        if a.get("fokus"):
            kopf += "<p>Fokus: %s</p>" % e(", ".join(f.get("titel", "") for f in a["fokus"]))
        if personen:
            kopf += "<p>Gesprächspartner: %s</p>" % e(personen)
        kopf += "<p>Stand %s%s</p>%s</div></header>" % (e(a.get("stichtag")), (" · " + e(a["website"])) if a.get("website") else "", banner)
        nav = "<nav>%s</nav>" % "".join('<a href="#%s">%s</a>' % (e(i), e(t)) for i, t in self.nav)
        daten = json.dumps(self.d, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
        return ('<!DOCTYPE html>\n<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
                '<title>Briefing %s – %s</title><style>%s</style></head><body>%s%s<main>%s</main>'
                '<footer>Fakten und Interpretation getrennt · Belege per Klick · Quellenstand %s</footer>'
                '<script type="application/json" id="briefing-daten">%s</script></body></html>\n') % (
            e(a.get("firma")), e(a.get("stichtag")), CSS, kopf, nav, rumpf, e(a.get("stichtag")), daten)


def rendern(daten):
    fehler, hinweise = validieren(daten)
    if fehler:
        raise Fehler("Validierung fehlgeschlagen, keine HTML erzeugt:\n- " + "\n- ".join(fehler))
    return Ausgabe(daten).seite(hinweise)


def extrahieren(text):
    m = re.search(r'<script type="application/json" id="briefing-daten">(.*?)</script>', text, re.S)
    if not m:
        raise Fehler("Kein Datenblock 'briefing-daten' in der HTML gefunden.")
    return json.loads(m.group(1))


# ---------------------------------------------------------------- Excel (Ersatzweg)
def excel(daten, pfad):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Claims"
    urteile = {u["id"]: u for u in (daten.get("pruefung") or {}).get("claims", [])}
    ws.append(["ID", "Kapitel", "Aussage", "Ursprung", "Status", "Datum", "Quellen", "Belegstelle", "Unsicherheit", "Stufe", "Urteil", "Befund", "Korrektur"])
    for c in daten.get("claims", []):
        u = urteile.get(c["id"], {})
        ws.append([c["id"], kapitel_von(c["id"]), c.get("aussage"), c.get("ursprung"), c.get("status"), c.get("datum"), ", ".join(c.get("quellen", [])),
                   c.get("belegstelle"), c.get("unsicherheit"), c.get("stufe"), u.get("urteil"), u.get("begruendung"), u.get("korrektur")])
    wq = wb.create_sheet("Quellen")
    wq.append(["ID", "Titel", "Herausgeber", "Datum", "URL", "Abruf", "Art", "Typ", "Geöffnet"])
    for q in daten.get("quellen", []):
        wq.append([q.get("id"), q.get("titel"), q.get("herausgeber"), q.get("datum"), q.get("url"), q.get("abruf"), q.get("art"), q.get("typ"), "ja" if q.get("geoeffnet") else "nein"])
    wi = wb.create_sheet("Interpretationen")
    wi.append(["ID", "Titel", "Aussage", "Basis"])
    for i in interpretationen(daten):
        wi.append([i.get("id"), i.get("titel") or i.get("label") or i.get("dimension"), i.get("aussage") or i.get("insight") or i.get("wert"), ", ".join(i.get("basis", []))])
    wd = wb.create_sheet("_daten")
    wd.append(["Maschinenlesbare Daten. Nicht bearbeiten; Änderungen in anderen Blättern werden nicht übernommen."])
    text = json.dumps(daten, ensure_ascii=False)
    for i in range(0, len(text), 30000):
        wd.append([text[i:i + 30000]])
    wb.save(pfad)


def aus_excel(pfad):
    from openpyxl import load_workbook
    wb = load_workbook(pfad, read_only=True)
    if "_daten" not in wb.sheetnames:
        raise Fehler("Blatt '_daten' fehlt.")
    zeilen = [r[0] for r in wb["_daten"].iter_rows(min_row=2, values_only=True) if r and r[0]]
    return json.loads("".join(zeilen))


# ---------------------------------------------------------------- Kommandozeile
def main(argv=None):
    ap = argparse.ArgumentParser(description="Firmenbriefing-Daten verarbeiten")
    sub = ap.add_subparsers(dest="befehl", required=True)
    s = sub.add_parser("zusammenfuehren"); s.add_argument("--daten", required=True); s.add_argument("--teil", required=True); s.add_argument("--ersetzen", action="store_true")
    s = sub.add_parser("validieren"); s.add_argument("--daten", required=True)
    s = sub.add_parser("auswerten"); s.add_argument("--daten", required=True)
    s = sub.add_parser("rendern"); s.add_argument("--daten", required=True); s.add_argument("--out", required=True)
    s = sub.add_parser("extrahieren"); s.add_argument("--html", required=True); s.add_argument("--out", required=True)
    s = sub.add_parser("excel"); s.add_argument("--daten", required=True); s.add_argument("--out", required=True)
    s = sub.add_parser("aus-excel"); s.add_argument("--xlsx", required=True); s.add_argument("--out", required=True)
    sub.add_parser("version")
    sub.add_parser("regeln")
    a = ap.parse_args(argv)
    try:
        if a.befehl == "version":
            print("briefing.py %s, Schema %s" % (VERSION, SCHEMA))
        elif a.befehl == "regeln":
            for k, v in REGELN.items():
                print("%-28s %s" % (k, v))
        elif a.befehl == "zusammenfuehren":
            haupt = lade(a.daten) if os.path.exists(a.daten) else None
            haupt, meldung = zusammenfuehren(haupt, lade(a.teil), a.ersetzen)
            speichere(a.daten, haupt)
            print(meldung)
        elif a.befehl == "validieren":
            fehler, hinweise = validieren(lade(a.daten))
            for f in fehler:
                print("FEHLER:", f)
            for h in hinweise:
                print("HINWEIS:", h)
            print("%d Fehler, %d Hinweise" % (len(fehler), len(hinweise)))
            return 1 if fehler else 0
        elif a.befehl == "auswerten":
            daten = lade(a.daten)
            ergebnis, aus = auswerten(daten)
            speichere(a.daten, daten)
            print(ERGEBNIS[ergebnis])
            for k, v in aus.items():
                if v:
                    print("%s: %s" % (k, v if isinstance(v, int) else ", ".join(v)))
        elif a.befehl == "rendern":
            text = rendern(lade(a.daten))
            with open(a.out, "w", encoding="utf-8") as f:
                f.write(text)
            print("geschrieben: %s (%d Zeichen)" % (a.out, len(text)))
        elif a.befehl == "extrahieren":
            with open(a.html, encoding="utf-8") as f:
                speichere(a.out, extrahieren(f.read()))
            print("geschrieben:", a.out)
        elif a.befehl == "excel":
            excel(lade(a.daten), a.out)
            print("geschrieben:", a.out)
        elif a.befehl == "aus-excel":
            speichere(a.out, aus_excel(a.xlsx))
            print("geschrieben:", a.out)
    except Fehler as x:
        print("FEHLER:", x, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
