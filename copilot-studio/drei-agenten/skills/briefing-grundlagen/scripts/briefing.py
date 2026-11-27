#!/usr/bin/env python3
"""Firmenbriefing-Daten: Teile zusammenführen, validieren, Prüfung auswerten, Excel lesen und schreiben.

Nur Python-Standardbibliothek; die Excel-Befehle brauchen zusätzlich openpyxl.
Die HTML erzeugt ausschließlich der Skill briefing-html (Agent 3).

  python3 briefing.py version
  python3 briefing.py regeln
  python3 briefing.py zusammenfuehren --daten briefing-daten.json --teil teil.json [--ersetzen] [--pruefer]
  python3 briefing.py validieren --daten briefing-daten.json
  python3 briefing.py auswerten --daten briefing-daten.json
  python3 briefing.py excel --daten briefing-daten.json --out briefing-daten.xlsx
  python3 briefing.py aus-excel --xlsx briefing-daten.xlsx --out briefing-daten.json
  python3 briefing.py extrahieren --html briefing.html --out briefing-daten.json
"""
import argparse, calendar, datetime, json, os, re, sys

VERSION = "2.0.0"
SCHEMA = "firmenbriefing/2"
FACT_RE = re.compile(r"^(T|H|P|C|M|F_[A-Za-z0-9-]+_)\d+$")
INTERP_RE = re.compile(r"^[IS][A-Za-z0-9_-]*$")
SRC_RE = re.compile(r"^Q\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MONTH_RE = re.compile(r"^\d{4}-\d{2}(-\d{2})?$")
URSPRUNG = {"fakt": "Fakt", "hersteller": "Herstellerangabe", "partner": "Partnerangabe",
            "medien": "Medienbericht", "nutzer": "Nutzerangabe"}
KAPITEL = {"T": "unternehmen", "H": "personen", "P": "portfolio", "C": "cluster", "M": "markt"}
KAPITEL_TITEL = {"unternehmen": "Unternehmen", "personen": "Gesprächspartner", "portfolio": "Portfolio",
                 "cluster": "Struktur & Partner", "markt": "Markt & Wettbewerb", "fokus": "Fokusthemen",
                 "interpretation": "Interpretation"}
MODULE = {"firmenbasis": "Firmenbasis", "person": "Gesprächspartner", "portfolio": "Portfolio",
          "cluster": "Struktur, Partner und Kunden", "markt": "Markt und Wettbewerb", "fokus": "Fokusthemen",
          "interpretation": "Interpretation"}
STATUS_STUFE = {"angekuendigt": 1, "prototyp": 2, "test": 3, "kundenauftrag": 4, "im_einsatz": 5, "serie": 6,
                "eingestellt": None, "nicht_belegt": None}
QUELLENTYP = {"geschaeftsbericht": "Geschäftsbericht", "investor": "Investorenunterlage", "produktseite": "Produktseite",
              "datenblatt": "Datenblatt", "pressemitteilung": "Pressemitteilung", "register": "Register",
              "behoerde": "Behörde", "vergabe": "Vergabe", "verband": "Verband", "statistik": "Statistik",
              "medien": "Nachrichtenmedium", "fachmedien": "Fachmedium", "sonstiges": "Sonstiges"}
MEDIEN = {"medien", "fachmedien"}
BERICHTE = {"geschaeftsbericht", "investor"}
BEZIEHUNG = {"Eigentum", "Tochtergesellschaft", "Joint Venture", "Kooperation", "Kunde", "Lieferant", "Projekt",
             "Lizenz", "Mandat", "historisch"}
BEZIEHUNG_ART = {"direkt", "indirekt", "Überschneidung"}
AKTEUR_ART = {"eigentuemer", "tochter", "jv", "partner", "kunde", "zulieferer", "projekt", "institution", "person", "sonstige"}
AKTEUR_BEREICH = {"kapital", "konzern", "technologie", "markt"}
FUNKTION = {"Büro", "Produktion", "Integration", "Service", "Entwicklung", "Partner", "Kundenaktivität", "Zugang",
            "Auslandsbetreuung"}
BETREIBER = {"eigen", "partner", "jv", "kunde", "ausland"}
PRAESENZ_STATUS = {"operativ", "angekündigt"}
KONTROLLE = {"alleinig", "gemeinsam", "keine", "unbekannt"}
KRITERIUM_TYP = {"profil", "kennzahl", "evidenzstufe"}
FOKUS_TYP = {"marktvolumen", "budget", "rahmenhoechstwert", "auftrag", "lieferung", "kapazitaet", "technisch",
             "struktur", "sonstige"}
MEDIEN_KATEGORIE = {"eigene", "offiziell", "medien"}
URTEIL_FAKT = {"im_original_bestaetigt", "durch_suche_gestuetzt", "abweichend", "nicht_belegt", "nicht_erreichbar",
               "nicht_einzeln_geprueft", "korrigiert", "neu_aus_vertiefung"}
URTEIL_ABLEITUNG = {"gestuetzt", "eingeschraenkt", "nicht_gestuetzt", "angepasst"}
ERGEBNIS = {"bestanden": "Prüfung bestanden",
            "bestanden_mit_einschraenkungen": "Prüfung bestanden mit Einschränkungen",
            "unvollstaendig": "Prüfung unvollständig", "nicht_bestanden": "Prüfung nicht bestanden"}
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


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")).strip("-")
    return s or "x"


def datum(wert):
    return datetime.date.fromisoformat(wert) if DATE_RE.match(str(wert or "")) else None


# ---------------------------------------------------------------- Zusammenführen
def leer():
    return {"schema": SCHEMA, "auftrag": {}, "phasen": {}, "quellen": [], "claims": [],
            "inhalt": {}, "interpretation": {}, "offen": {"luecken": [], "fragen": []}}


def protokolliere(haupt, eintrag):
    p = haupt.setdefault("pruefung", {})
    p.setdefault("aenderungen", []).append(eintrag)


def zusammenfuehren(haupt, teil, ersetzen=False, pruefer=False):
    """Führt einen Teil in die Arbeitsdaten ein.

    pruefer=True: Agent 2 korrigiert und vertieft. Die Prüfung bleibt erhalten, jede Änderung
    an Claims wird automatisch protokolliert. Ohne pruefer veraltet eine vorhandene Prüfung,
    sobald sich Inhalte ändern, und wird entfernt.
    """
    if haupt is None:
        if "auftrag" not in teil:
            raise Fehler("Neue Daten brauchen im ersten Teil den Block 'auftrag'.")
        haupt = leer()
    for k, v in leer().items():
        haupt.setdefault(k, v)
    haupt["schema"] = SCHEMA
    haupt["auftrag"].update(teil.get("auftrag", {}))
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
            for feld in ("titel", "herausgeber", "datum", "abruf", "art", "typ", "geschaeftsjahr", "seite", "abschnitt"):
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
    hatte_pruefung = bool(haupt.get("pruefung"))
    claim_index = {c["id"]: i for i, c in enumerate(haupt["claims"])}
    doppelt, neu_c, ersetzt, entfernt = [], 0, 0, 0
    for c in teil.get("claims", []):
        c = dict(c)
        fehlend = [s for s in c.get("quellen", []) if s not in umbenennen]
        if fehlend:
            raise Fehler("Claim %s verweist auf Quellen, die nicht im selben Teil stehen: %s"
                         % (c.get("id"), ", ".join(map(str, fehlend))))
        c["quellen"] = [umbenennen[s] for s in c.get("quellen", [])]
        if c.get("id") in claim_index:
            i = claim_index[c["id"]]
            alt = haupt["claims"][i]
            if alt == c:
                continue
            if not ersetzen:
                doppelt.append(c["id"])
                continue
            haupt["claims"][i] = c
            ersetzt += 1
            if pruefer:
                protokolliere(haupt, {"id": c["id"], "art": "korrigiert", "alt": alt.get("aussage"), "neu": c.get("aussage"),
                                      "beleg": ", ".join(c.get("quellen", [])), "grund": c.get("korrekturgrund", "")})
        else:
            if pruefer:
                c.setdefault("herkunft", "vertiefung")
                protokolliere(haupt, {"id": c.get("id"), "art": "ergaenzt", "alt": "", "neu": c.get("aussage"),
                                      "beleg": ", ".join(c.get("quellen", [])), "grund": c.get("korrekturgrund", "Vertiefung")})
            claim_index[c.get("id")] = len(haupt["claims"])
            haupt["claims"].append(c)
            neu_c += 1
    if doppelt:
        raise Fehler("Claim-IDs schon vorhanden (mit --ersetzen überschreiben): " + ", ".join(doppelt))
    weg = set(teil.get("entfernen", []))
    if weg:
        for c in [c for c in haupt["claims"] if c["id"] in weg]:
            if pruefer:
                protokolliere(haupt, {"id": c["id"], "art": "entfernt", "alt": c.get("aussage"), "neu": "",
                                      "beleg": "", "grund": teil.get("entfernen_grund", "nicht belegt")})
            entfernt += 1
        haupt["claims"] = [c for c in haupt["claims"] if c["id"] not in weg]
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
    meldung = "%d Quellen neu, %d mit vorhandenen zusammengeführt, %d Claims neu, %d ersetzt, %d entfernt" % (
        neu_q, alt_q, neu_c, ersetzt, entfernt)
    if hatte_pruefung and not pruefer and any(teil.get(k) for k in ("quellen", "claims", "inhalt", "interpretation", "entfernen")):
        haupt.pop("pruefung", None)
        meldung += "; vorhandene Prüfung entfernt, weil sich Inhalte geändert haben – bitte erneut prüfen lassen"
    if "pruefung" in teil:
        neu = teil["pruefung"]
        if neu is None:
            haupt.pop("pruefung", None)
        else:
            alt = haupt.setdefault("pruefung", {})
            for k, v in neu.items():
                if k in ("claims", "ableitungen"):
                    index = {u.get("id"): i for i, u in enumerate(alt.setdefault(k, []))}
                    for u in v:
                        if u.get("id") in index:
                            alt[k][index[u.get("id")]] = u
                        else:
                            index[u.get("id")] = len(alt[k])
                            alt[k].append(u)
                elif k in ("stichprobe", "hinweise", "aenderungen", "vertiefung"):
                    alt.setdefault(k, []).extend(x for x in v if x not in alt.get(k, []))
                else:
                    alt[k] = v
            alt.pop("ergebnis", None)
            alt.pop("auswertung", None)
        meldung += "; Prüfdaten übernommen"
    elif pruefer and haupt.get("pruefung"):
        haupt["pruefung"].pop("ergebnis", None)
        haupt["pruefung"].pop("auswertung", None)
    return haupt, meldung


# ---------------------------------------------------------------- Hilfen für Validierung und Darstellung
def alle_verweise(obj, schluessel=("claims", "basis", "kontrollbeleg")):
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
    if isinstance(obj, dict):
        if isinstance(obj.get("claims"), list):
            yield pfad, next((str(v)[:60] for k, v in obj.items() if k != "claims" and isinstance(v, str) and v), ""), obj["claims"]
        for k, v in obj.items():
            if k != "claims":
                yield from zeilen_mit_claims(v, pfad + "." + k)
    elif isinstance(obj, list):
        for i, x in enumerate(obj):
            yield from zeilen_mit_claims(x, "%s[%d]" % (pfad, i))


def interpretationen(daten):
    """Alle Interpretationsobjekte mit ID."""
    ip = daten.get("interpretation", {})
    summ = ip.get("summary", {})
    out = list(summ.get("highlights", [])) + list(summ.get("kernaussagen", []))
    for k in ("keyfacts", "reife", "praesenz", "positionierung"):
        out += ip.get(k, [])
    for q in ("staerken", "schwaechen", "chancen", "risiken"):
        out += ip.get("swot", {}).get(q, [])
    return out


def angebote(daten):
    for f in (daten.get("inhalt", {}).get("portfolio") or {}).get("felder", []):
        for a in f.get("angebote", []):
            yield f, a


def monate_zurueck(stichtag, monate):
    j, m = stichtag.year, stichtag.month - monate
    while m <= 0:
        m += 12
        j -= 1
    return datetime.date(j, m, min(stichtag.day, calendar.monthrange(j, m)[1]))


def quellen_von(daten, obj):
    claims = {c["id"]: c for c in daten.get("claims", [])}
    quellen = {q["id"]: q for q in daten.get("quellen", [])}
    out = {}
    for cid in alle_verweise(obj, ("claims",)):
        for s in claims.get(cid, {}).get("quellen", []):
            if s in quellen:
                out[s] = quellen[s]
    return out


def anzahl_medien(daten, obj):
    return sum(1 for q in quellen_von(daten, obj).values() if q.get("typ") in MEDIEN)


def mindestregeln(daten):
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
        alle = []
        for f in pf.get("felder", []):
            pruefe(len(f.get("angebote", [])) >= 2, "portfolio.angebote_je_feld", "Geschäftsfeld %s" % f.get("name"), pf)
            alle += f.get("angebote", [])
        pruefe(any(q.get("typ") in BERICHTE for q in quellen_von(daten, pf).values()), "portfolio.geschaeftsbericht", "Portfolio", pf)
        pruefe(anzahl_medien(daten, pf) >= 2, "portfolio.medien", "Portfolio", pf)
        offen = sum(1 for a in alle if a.get("status_stufe") == "nicht_belegt")
        pruefe(not alle or offen * 2 <= len(alle), "portfolio.status", "Portfolio", pf)
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


# ---------------------------------------------------------------- Validierung
def validieren(daten):
    fehler, hinweise = [], []
    F, H = fehler.append, hinweise.append
    if daten.get("schema") != SCHEMA:
        F("schema muss '%s' sein" % SCHEMA)
    a = daten.get("auftrag", {})
    if not a.get("firma"):
        F("auftrag.firma fehlt")
    stichtag = datum(a.get("stichtag"))
    if not stichtag:
        F("auftrag.stichtag fehlt oder ist nicht JJJJ-MM-TT")
    if a.get("modus") not in ("voll", "modul"):
        F("auftrag.modus muss 'voll' oder 'modul' sein")
    for f in a.get("fokus", []):
        if not re.fullmatch(r"[A-Za-z0-9_-]+", str(f.get("id", ""))):
            F("Fokus-ID %r nur Buchstaben, Ziffern, _ und -" % f.get("id"))
    # Quellen
    qids = [q.get("id") for q in daten.get("quellen", [])]
    if len(set(qids)) != len(qids):
        F("Doppelte Quellen-IDs")
    for q in daten.get("quellen", []):
        if not SRC_RE.match(str(q.get("id", ""))):
            F("Quelle mit ungültiger ID: %r" % q.get("id"))
        if not str(q.get("url", "")).startswith(("http://", "https://")):
            F("Quelle %s: url muss mit http:// oder https:// beginnen" % q.get("id"))
        if q.get("typ") not in QUELLENTYP:
            F("Quelle %s: typ muss einer von %s sein" % (q.get("id"), ", ".join(QUELLENTYP)))
        if not q.get("titel"):
            H("Quelle %s ohne Titel" % q.get("id"))
    quellen = {q.get("id"): q for q in daten.get("quellen", [])}
    # Claims
    cids = [c.get("id") for c in daten.get("claims", [])]
    if len(set(cids)) != len(cids):
        F("Doppelte Claim-IDs: " + ", ".join(sorted({x for x in cids if cids.count(x) > 1})))
    for c in daten.get("claims", []):
        cid = c.get("id")
        if not FACT_RE.match(str(cid)):
            F("Claim-ID %r passt nicht zu T/H/P/C/M/F_<thema>_ plus Nummer" % cid)
        if not c.get("aussage"):
            F("Claim %s ohne aussage" % cid)
        elif len(str(c["aussage"])) > 350:
            H("Claim %s ist sehr lang; ein Claim soll genau eine Aussage enthalten" % cid)
        if c.get("ursprung") not in URSPRUNG:
            F("Claim %s: ursprung muss einer von %s sein" % (cid, ", ".join(URSPRUNG)))
        if c.get("stufe") not in ("A", "B"):
            F("Claim %s: stufe muss A oder B sein" % cid)
        if not c.get("quellen"):
            F("Claim %s ohne Quelle" % cid)
        for s in c.get("quellen", []):
            if s not in quellen:
                F("Claim %s verweist auf unbekannte Quelle %s" % (cid, s))
            elif c.get("stufe") == "A" and quellen[s].get("geoeffnet") is False:
                H("A-Claim %s stützt sich auf nicht geöffnete Quelle %s" % (cid, s))
        if c.get("stufe") == "A" and not c.get("belegstelle"):
            H("A-Claim %s ohne belegstelle" % cid)
        d = datum(c.get("datum"))
        if d and stichtag and d > stichtag:
            H("Claim %s: datum %s liegt nach dem Stichtag" % (cid, c["datum"]))
    claimset = set(cids)
    stufe_von = {c.get("id"): c.get("stufe") for c in daten.get("claims", [])}
    # Interpretationen
    ips = interpretationen(daten)
    iids = [i.get("id") for i in ips]
    for i in ips:
        if not INTERP_RE.match(str(i.get("id", ""))):
            F("Interpretation mit ungültiger ID %r (I… oder S…)" % i.get("id"))
        if not i.get("basis") and not (i in daten.get("interpretation", {}).get("reife", []) + daten.get("interpretation", {}).get("praesenz", []) and i.get("stufe") is None):
            F("Interpretation %s ohne basis" % i.get("id"))
    if len(set(iids)) != len(iids):
        F("Doppelte Interpretations-IDs")
    bekannt = claimset | set(iids)
    inhalt = daten.get("inhalt", {})
    for x in sorted(set(alle_verweise(inhalt)) - claimset):
        F("Inhalt verweist auf unbekannten Claim %s" % x)
    for x in sorted(set(alle_verweise(daten.get("interpretation", {}))) - bekannt):
        F("Interpretation verweist auf unbekannte ID %s" % x)
    genutzt = set(alle_verweise(inhalt)) | set(alle_verweise(daten.get("interpretation", {})))
    for c in sorted(claimset - genutzt):
        H("Claim %s wird nur im Quellenregister gezeigt" % c)
    for s in sorted(set(quellen) - {s for c in daten.get("claims", []) for s in c.get("quellen", [])}):
        H("Quelle %s wird von keinem Claim genutzt" % s)
    for pfad, zeile, ids in zeilen_mit_claims(inhalt):
        if not ids:
            H("Eintrag ohne Beleg in %s: %s" % (pfad, zeile))
        elif all(stufe_von.get(i) == "B" for i in ids):
            F("Zeile stützt sich nur auf B-Claims (%s) in %s: %s – mindestens ein A-Claim nötig" % (", ".join(ids), pfad, zeile))
    # Portfolio
    namen = set()
    for f, an in angebote(daten):
        if an.get("status_stufe") not in STATUS_STUFE:
            F("Angebot %s: status_stufe muss einer von %s sein" % (an.get("name"), ", ".join(STATUS_STUFE)))
        if an.get("name") in namen:
            F("Angebot %s doppelt; Namen müssen eindeutig sein" % an.get("name"))
        namen.add(an.get("name"))
        if an.get("status_stufe") not in ("nicht_belegt", None) and not any(
                next((c for c in daten.get("claims", []) if c.get("id") == i), {}).get("datum") for i in an.get("claims", [])):
            H("Angebot %s: Status ohne datierten Beleg" % an.get("name"))
    # Cluster
    cl = inhalt.get("cluster") or {}
    for ak in cl.get("akteure", []):
        if ak.get("art") not in AKTEUR_ART or ak.get("bereich", "technologie") not in AKTEUR_BEREICH:
            F("Akteur %s: art muss einer von %s sein, bereich einer von %s" % (ak.get("name"), ", ".join(sorted(AKTEUR_ART)), ", ".join(sorted(AKTEUR_BEREICH))))
    ziel = {a.get("firma"), a.get("kurzname") or a.get("firma")}
    if cl.get("beziehungen") and not any(b.get("von") in ziel or b.get("zu") in ziel for b in cl["beziehungen"]):
        H("Keine Beziehung nennt das Zielunternehmen; in von/zu genau auftrag.firma oder auftrag.kurzname verwenden")
    for b in cl.get("beziehungen", []):
        ort = "Beziehung %s–%s" % (b.get("von"), b.get("zu"))
        if b.get("typ") not in BEZIEHUNG:
            F("%s: typ muss einer von %s sein" % (ort, ", ".join(sorted(BEZIEHUNG))))
        if b.get("art") not in BEZIEHUNG_ART:
            F("%s: art muss direkt, indirekt oder Überschneidung sein" % ort)
        if not MONTH_RE.match(str(b.get("datum", ""))):
            F("%s: datum muss JJJJ-MM oder JJJJ-MM-TT sein" % ort)
        if not b.get("von") or not b.get("zu") or b.get("von") == b.get("zu"):
            F("%s: von und zu müssen verschiedene Akteure nennen" % ort)
        for p in b.get("produkte", []):
            if p not in namen:
                F("%s: Produkt %s ist kein Angebot im Portfolio" % (ort, p))
    # Markt
    m = inhalt.get("markt") or {}
    v = m.get("vergleich") or {}
    kriterien = {}
    for k in v.get("kriterien", []):
        kriterien[k.get("id")] = k
        if k.get("typ") not in KRITERIUM_TYP:
            F("Kriterium %s: typ muss profil, kennzahl oder evidenzstufe sein" % k.get("id"))
        if k.get("typ") == "kennzahl" and not k.get("einheit"):
            F("Kriterium %s: kennzahl braucht einheit" % k.get("id"))
        if k.get("typ") == "evidenzstufe" and (not isinstance(k.get("stufen"), dict) or len(k["stufen"]) < 2):
            F("Kriterium %s: evidenzstufe braucht mindestens zwei definierte stufen" % k.get("id"))
        if not k.get("frage"):
            H("Kriterium %s ohne frage" % k.get("id"))
    for z in v.get("zeilen", []):
        for kid, zelle in (z.get("zellen") or {}).items():
            if kid not in kriterien:
                F("Vergleich %s: unbekanntes Kriterium %s" % (z.get("akteur"), kid))
            elif kriterien[kid].get("typ") == "evidenzstufe" and not zelle.get("nicht_anwendbar") and str(zelle.get("stufe")) not in kriterien[kid].get("stufen", {}):
                F("Vergleich %s/%s: stufe muss eine der definierten Stufen sein" % (z.get("akteur"), kid))
            if kid in kriterien and kriterien[kid].get("typ") == "kennzahl" and not zelle.get("nicht_anwendbar") and (
                    not isinstance(zelle.get("wert"), (int, float)) or isinstance(zelle.get("wert"), bool)):
                F("Vergleich %s/%s: Kennzahl-Zelle braucht einen Zahlenwert in wert" % (z.get("akteur"), kid))
            if not zelle.get("nicht_anwendbar") and not zelle.get("claims"):
                F("Vergleich %s/%s: Zelle ohne Beleg; leer lassen, wenn nichts belegt ist" % (z.get("akteur"), kid))
    regionen = set()
    for reg in m.get("praesenz", []):
        regionen.add(reg.get("region"))
        if not reg.get("laender"):
            F("Präsenz %s: laender fehlt" % reg.get("region"))
        for akt in reg.get("aktivitaeten", []):
            ort = "Präsenz %s/%s" % (reg.get("region"), akt.get("ort"))
            if akt.get("funktion") not in FUNKTION:
                F("%s: funktion muss eine von %s sein" % (ort, ", ".join(sorted(FUNKTION))))
            if akt.get("betreiber") not in BETREIBER or akt.get("status") not in PRAESENZ_STATUS:
                F("%s: betreiber muss eigen, partner, jv, kunde oder ausland sein, status operativ oder angekündigt" % ort)
            if akt.get("betreiber") == "jv" and akt.get("kontrolle", "unbekannt") not in KONTROLLE:
                F("%s: kontrolle muss alleinig, gemeinsam, keine oder unbekannt sein" % ort)
            if akt.get("kontrolle") in ("alleinig", "gemeinsam") and not akt.get("kontrollbeleg"):
                F("%s: belegte Kontrolle braucht kontrollbeleg mit Claim-IDs" % ort)
            for key in ("land", "ort", "beschreibung"):
                if not akt.get(key):
                    F("%s: %s fehlt" % (ort, key))
    # Fokus
    fokus_ids = {f.get("id") for f in a.get("fokus", [])}
    for f in inhalt.get("fokus", []):
        ort = "Fokus %s" % f.get("id")
        if f.get("id") not in fokus_ids:
            H("%s steht nicht im Auftrag" % ort)
        for key in ("ueberblick", "definition"):
            if not isinstance(f.get(key), dict) or not f[key].get("text"):
                F("%s: %s mit text und claims fehlt" % (ort, key))
        for kz in f.get("kennzahlen", []):
            if not isinstance(kz.get("wert"), (int, float)) or isinstance(kz.get("wert"), bool) or kz["wert"] < 0:
                F("%s: Kennzahl %s braucht einen Zahlenwert ab 0 in wert" % (ort, kz.get("kennzahl")))
            if kz.get("typ") not in FOKUS_TYP:
                F("%s: Kennzahl %s typ muss einer von %s sein" % (ort, kz.get("kennzahl"), ", ".join(sorted(FOKUS_TYP))))
            if not kz.get("einheit"):
                F("%s: Kennzahl %s braucht einheit" % (ort, kz.get("kennzahl")))
        for fr in f.get("fragen", []):
            if not isinstance(fr, dict) or not fr.get("frage"):
                F("%s: fragen müssen Objekte mit frage und claims sein" % ort)
        for e in f.get("entwicklungen", []):
            if not datum(e.get("datum")):
                F("%s: Entwicklung ohne gültiges Datum" % ort)
        for x in alle_verweise(f, ("claims",)):
            if not str(x).startswith("F_%s_" % f.get("id")):
                H("%s nutzt Claim %s ohne Präfix F_%s_" % (ort, x, f.get("id")))
    # Personen
    for p in inhalt.get("personen", []):
        for e in p.get("medien", []):
            if not datum(e.get("datum")) or e.get("kategorie") not in MEDIEN_KATEGORIE:
                F("Person %s: Medieneintrag braucht datum JJJJ-MM-TT und kategorie eigene, offiziell oder medien" % p.get("name"))
    # Interpretation
    ip = daten.get("interpretation", {})
    for q in ("staerken", "schwaechen", "chancen", "risiken"):
        if len(ip.get("swot", {}).get(q, [])) > 3:
            F("SWOT %s: höchstens drei Punkte" % q)
    if a.get("modus") == "voll" and ip:
        n = len(ip.get("summary", {}).get("kernaussagen", []))
        if not 4 <= n <= 6:
            H("Executive Summary hat %d Kernaussagen, vorgesehen sind 4 bis 6" % n)
    if len(ip.get("summary", {}).get("highlights", [])) > 3:
        F("Executive Summary: höchstens drei Highlights")
    for modul in ("portfolio", "cluster", "markt"):
        if sum(1 for k in ip.get("keyfacts", []) if k.get("modul") == modul) > 3:
            F("Keyfacts %s: höchstens drei" % modul)
    for k in ip.get("keyfacts", []):
        if k.get("modul") not in ("portfolio", "cluster", "markt"):
            F("Keyfact %s: modul muss portfolio, cluster oder markt sein" % k.get("id"))
    for r in ip.get("reife", []):
        if r.get("angebot") not in namen:
            F("Reife %s: angebot %r ist kein Angebot im Portfolio" % (r.get("id"), r.get("angebot")))
        if r.get("stufe") is not None and r.get("stufe") not in range(1, 7):
            F("Reife %s: stufe muss 1 bis 6 oder null sein" % r.get("id"))
        if r.get("stufe") is not None and not r.get("naechste_stufe"):
            H("Reife %s: naechste_stufe fehlt (warum die nächste Stufe nicht belegt ist)" % r.get("id"))
    for r in ip.get("praesenz", []):
        if r.get("region") not in regionen:
            F("Präsenzstufe %s: region %r fehlt in markt.praesenz" % (r.get("id"), r.get("region")))
        if r.get("stufe") is not None and r.get("stufe") not in range(1, 6):
            F("Präsenzstufe %s: stufe muss 1 bis 5 oder null sein" % r.get("id"))
        if r.get("status") not in ("bewertet", "geplant", "nicht eindeutig bestimmbar"):
            F("Präsenzstufe %s: status muss bewertet, geplant oder nicht eindeutig bestimmbar sein" % r.get("id"))
    # Zeitfenster
    if stichtag:
        g4, g6 = monate_zurueck(stichtag, 4), monate_zurueck(stichtag, 6)
        for t in (inhalt.get("unternehmen") or {}).get("timeline", []):
            d = datum(t.get("datum"))
            if not d:
                H("Timeline-Eintrag ohne gültiges Datum: %s" % t.get("ereignis"))
            elif d < g4 or d > stichtag:
                H("Timeline-Eintrag %s liegt außerhalb des Viermonatsfensters" % t["datum"])
        for f in inhalt.get("fokus", []):
            for t in f.get("entwicklungen", []):
                d = datum(t.get("datum"))
                if d and (d < g6 or d > stichtag):
                    H("Fokus %s: Entwicklung %s liegt außerhalb des Sechsmonatsfensters" % (f.get("id"), t["datum"]))
    # Ausnahmen und Mindestregeln
    for ort, aus in alle_ausnahmen(daten):
        if aus.get("regel") not in REGELN:
            F("%s: Ausnahme für unbekannte Regel %r" % (ort, aus.get("regel")))
        elif len(str(aus.get("grund", ""))) < 40:
            F("%s: Ausnahme %s braucht einen konkreten Grund mit Suchumfang (mindestens 40 Zeichen)" % (ort, aus.get("regel")))
    for regel, ort, ausnahmen in mindestregeln(daten):
        if not any(x.get("regel") == regel for x in ausnahmen):
            F("Mindestregel %s nicht erfüllt (%s): %s Weiter recherchieren; nur wenn öffentlich nichts zu finden ist, "
              "eine Ausnahme mit konkretem Grund eintragen." % (regel, ort, REGELN[regel]))
    # Prüfung
    p = daten.get("pruefung")
    if p:
        for u in p.get("claims", []):
            if u.get("id") not in claimset:
                F("Prüfurteil für unbekannten Claim %s" % u.get("id"))
            if u.get("urteil") not in URTEIL_FAKT:
                F("Prüfurteil für %s ungültig: %r" % (u.get("id"), u.get("urteil")))
        for u in p.get("ableitungen", []):
            if u.get("id") not in set(iids):
                F("Ableitungsurteil für unbekannte Interpretation %s" % u.get("id"))
            if u.get("urteil") not in URTEIL_ABLEITUNG:
                F("Ableitungsurteil für %s ungültig: %r" % (u.get("id"), u.get("urteil")))
    return fehler, hinweise


# ---------------------------------------------------------------- Prüfung auswerten
def im_umfang(daten, cid):
    umfang = (daten.get("pruefung") or {}).get("umfang", {})
    kap = umfang.get("kapitel", "alle") if isinstance(umfang, dict) else "alle"
    return kap == "alle" or kapitel_von(cid) in kap


def auswerten(daten):
    p = daten.get("pruefung")
    if not p:
        raise Fehler("Keine Prüfdaten vorhanden.")
    umfang = p.get("umfang") if isinstance(p.get("umfang"), dict) else {}
    nur_a = umfang.get("nur_a")
    urteile = {u["id"]: u for u in p.get("claims", [])}
    abl = {u["id"]: u for u in p.get("ableitungen", [])}
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
            elif u in ("durch_suche_gestuetzt", "neu_aus_vertiefung"):
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
    elif einschr or umfang.get("kapitel", "alle") != "alle" or nur_a:
        ergebnis = "bestanden_mit_einschraenkungen"
    else:
        ergebnis = "bestanden"
    p["ergebnis"] = ergebnis
    p["auswertung"] = {"nicht_bestanden_wegen": schlecht, "offen": offen, "eingeschraenkt": einschr,
                       "betroffene_ableitungen": betroffen,
                       "korrigiert": sorted(k for k, u in urteile.items() if u.get("urteil") == "korrigiert"),
                       "aus_vertiefung": sorted(k for k, u in urteile.items() if u.get("urteil") == "neu_aus_vertiefung"),
                       "aenderungen": len(p.get("aenderungen", []))}
    return ergebnis, p["auswertung"]


# ---------------------------------------------------------------- Excel und HTML-Datenblock
def excel(daten, pfad):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Claims"
    pr = daten.get("pruefung") or {}
    urteile = {u["id"]: u for u in pr.get("claims", [])}
    ws.append(["ID", "Kapitel", "Aussage", "Ursprung", "Status", "Datum", "Quellen", "Belegstelle", "Unsicherheit", "Stufe",
               "Herkunft", "Urteil", "Befund", "Korrektur"])
    for c in daten.get("claims", []):
        u = urteile.get(c["id"], {})
        ws.append([c["id"], kapitel_von(c["id"]), c.get("aussage"), c.get("ursprung"), c.get("status"), c.get("datum"),
                   ", ".join(c.get("quellen", [])), c.get("belegstelle"), c.get("unsicherheit"), c.get("stufe"),
                   c.get("herkunft", "recherche"), u.get("urteil"), u.get("begruendung"), u.get("korrektur")])
    wq = wb.create_sheet("Quellen")
    wq.append(["ID", "Titel", "Herausgeber", "Datum", "URL", "Abruf", "Art", "Typ", "Geöffnet"])
    for q in daten.get("quellen", []):
        wq.append([q.get("id"), q.get("titel"), q.get("herausgeber"), q.get("datum"), q.get("url"), q.get("abruf"),
                   q.get("art"), q.get("typ"), "ja" if q.get("geoeffnet") else "nein"])
    wi = wb.create_sheet("Interpretationen")
    wi.append(["ID", "Titel", "Aussage", "Basis"])
    for i in interpretationen(daten):
        wi.append([i.get("id"), i.get("titel") or i.get("label") or i.get("dimension") or i.get("angebot") or i.get("region"),
                   i.get("aussage") or i.get("insight") or i.get("wert"), ", ".join(i.get("basis", []))])
    if pr.get("aenderungen"):
        wa = wb.create_sheet("Änderungen")
        wa.append(["ID", "Art", "Alt", "Neu", "Beleg", "Grund"])
        for x in pr["aenderungen"]:
            wa.append([x.get("id"), x.get("art"), x.get("alt"), x.get("neu"), x.get("beleg"), x.get("grund")])
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
        raise Fehler("Blatt '_daten' fehlt; die Datei stammt nicht aus dem Firmenbriefing.")
    zeilen = [r[0] for r in wb["_daten"].iter_rows(min_row=2, values_only=True) if r and r[0]]
    return json.loads("".join(zeilen))


def datenblock(daten):
    return json.dumps(daten, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


def extrahieren(text):
    m = re.search(r'<script type="application/json" id="briefing-daten">(.*?)</script>', text, re.S)
    if not m:
        raise Fehler("Kein Datenblock 'briefing-daten' in der HTML gefunden.")
    return json.loads(m.group(1))


def einlesen(pfad):
    """Liest briefing-daten aus .json, .xlsx oder einer Briefing-HTML."""
    endung = pfad.lower().rsplit(".", 1)[-1]
    if endung == "xlsx":
        return aus_excel(pfad)
    if endung in ("html", "htm"):
        with open(pfad, encoding="utf-8") as f:
            return extrahieren(f.read())
    return lade(pfad)


# ---------------------------------------------------------------- Kommandozeile
def main(argv=None):
    ap = argparse.ArgumentParser(description="Firmenbriefing-Daten verarbeiten")
    sub = ap.add_subparsers(dest="befehl", required=True)
    s = sub.add_parser("zusammenfuehren"); s.add_argument("--daten", required=True); s.add_argument("--teil", required=True)
    s.add_argument("--ersetzen", action="store_true"); s.add_argument("--pruefer", action="store_true")
    s = sub.add_parser("validieren"); s.add_argument("--daten", required=True)
    s = sub.add_parser("auswerten"); s.add_argument("--daten", required=True)
    s = sub.add_parser("excel"); s.add_argument("--daten", required=True); s.add_argument("--out", required=True)
    s = sub.add_parser("aus-excel"); s.add_argument("--xlsx", required=True); s.add_argument("--out", required=True)
    s = sub.add_parser("extrahieren"); s.add_argument("--html", required=True); s.add_argument("--out", required=True)
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
            haupt, meldung = zusammenfuehren(haupt, lade(a.teil), a.ersetzen, a.pruefer)
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
        elif a.befehl == "excel":
            excel(lade(a.daten), a.out)
            print("geschrieben:", a.out)
        elif a.befehl == "aus-excel":
            speichere(a.out, aus_excel(a.xlsx))
            print("geschrieben:", a.out)
        elif a.befehl == "extrahieren":
            with open(a.html, encoding="utf-8") as f:
                speichere(a.out, extrahieren(f.read()))
            print("geschrieben:", a.out)
    except Fehler as x:
        print("FEHLER:", x, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
