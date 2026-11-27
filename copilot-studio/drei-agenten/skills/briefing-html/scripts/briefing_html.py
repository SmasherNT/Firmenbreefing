#!/usr/bin/env python3
"""Agent 3: erzeugt aus briefing-daten (Agent 1 oder Agent 2) eine eigenständige Briefing-HTML.

Layout wie die Briefings des Claude-Systems: Reiter Überblick, Gesprächspartner, Fokusthemen,
Quellen; Reifematrix, Unternehmensnetzwerk, Präsenzprofile, Capability Matrix. Die Bausteine
*-html.py und die Vorlagen (eingebettet in vorlagen.py) stammen aus dem Claude-System;
in den Bausteinen ist nur das Laden der Vorlagen angepasst.
Keine Modell- oder Webaufrufe; offline lesbar und druckbar.

  python3 briefing_html.py --daten briefing-daten.xlsx --out briefing.html
  (--daten nimmt .xlsx, .json oder eine frühere Briefing-HTML)
"""
import argparse, copy, html, importlib.util, json, re, sys
from datetime import date
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from vorlagen import vorlage  # noqa: E402  (eingebettete Vorlagen, erzeugt von tools/build.py)


def _modul(name, datei):
    spec = importlib.util.spec_from_file_location(name, HIER / datei)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


B = _modul("briefing_daten", "briefing.py")
PORTFOLIO = _modul("portfolio_html", "portfolio-html.py")
CLUSTER = _modul("cluster_html", "cluster-html.py")
CAPABILITY = _modul("capability_html", "capability-html.py")
PRESENCE = _modul("presence_html", "presence-html.py")
PROFILE = _modul("profile_html", "profile-html.py")
FOCUS = _modul("focus_html", "focus-html.py")
INSIGHTS = _modul("module_insights", "module-insights-html.py")

VERSION = "1.0.0"
STAGES = {str(i): t for i, t in enumerate(("Angekündigt", "Prototyp", "Test / Demo", "Kundenprogramm", "Im Betrieb", "Serie / Skala"), 1)}
ART_KIND = {"eigentuemer": "owner", "tochter": "subsidiary", "jv": "jv", "partner": "partner", "kunde": "customer",
            "zulieferer": "supplier", "projekt": "project", "institution": "institution", "person": "person", "sonstige": "other"}
BEREICH = {"kapital": "capital", "konzern": "structure", "technologie": "technology", "markt": "market"}
TYP_KATEGORIE = {"Eigentum": "owner", "Tochtergesellschaft": "subsidiary", "Joint Venture": "jv", "Kooperation": "partner",
                 "Lizenz": "partner", "Kunde": "customer", "Lieferant": "supplier", "Projekt": "project", "Mandat": "other",
                 "historisch": "other"}
TYP_KIND = {"Tochtergesellschaft": "subsidiary", "Joint Venture": "jv", "Kooperation": "partner", "Lizenz": "partner",
            "Kunde": "customer", "Lieferant": "supplier", "Projekt": "project", "Mandat": "person", "historisch": "other"}
FUNKTION_KIND = {"Büro": "office", "Produktion": "production", "Integration": "integration", "Service": "service",
                 "Entwicklung": "development", "Partner": "partner", "Kundenaktivität": "customer_activity",
                 "Zugang": "access", "Auslandsbetreuung": "foreign_support"}
BETREIBER_OP = {"eigen": "own", "partner": "partner", "jv": "jv", "kunde": "customer", "ausland": "foreign"}
KONTROLLE = {"alleinig": "sole", "gemeinsam": "joint", "keine": "none", "unbekannt": "unknown"}
FOKUS_TYP = {"marktvolumen": "market_size", "budget": "budget", "rahmenhoechstwert": "contract_ceiling", "auftrag": "firm_order",
             "lieferung": "deliveries", "kapazitaet": "capacity", "technisch": "technical", "struktur": "industry_structure",
             "sonstige": "other"}
MEDIEN_KAT = {"eigene": "own", "offiziell": "official", "medien": "media"}
KRITERIUM = {"profil": "Profil", "kennzahl": "Kennzahl", "evidenzstufe": "Evidenzstufe"}
URTEIL = {"im_original_bestaetigt": ("im Original bestätigt", "ok", "✓"), "durch_suche_gestuetzt": ("durch Suche gestützt", "such", "≈"),
          "abweichend": ("abweichend", "bad", "✗"), "nicht_belegt": ("nicht belegt", "bad", "?"),
          "nicht_erreichbar": ("Quelle nicht erreichbar", "warn", "⊘"), "nicht_einzeln_geprueft": ("nicht einzeln geprüft (Stichprobe)", "none", "·"),
          "korrigiert": ("bei Prüfung korrigiert", "ok", "✎"), "neu_aus_vertiefung": ("neu aus der Vertiefung", "such", "+"),
          "gestuetzt": ("Ableitung gestützt", "ok", "✓"), "eingeschraenkt": ("Ableitung eingeschränkt", "such", "≈"),
          "nicht_gestuetzt": ("Ableitung nicht gestützt", "bad", "✗"), "angepasst": ("Ableitung angepasst", "ok", "✎")}
ART_AENDERUNG = {"korrigiert": "korrigiert", "ergaenzt": "ergänzt", "entfernt": "entfernt", "angepasst": "angepasst"}
STIL = """<style>
.claim.pv-ok{background:#e3f3ea;color:#16734a}.claim.pv-such{background:#e8f0fd;color:#235c9b}.claim.pv-bad{background:#fde8ea;color:#b3343c;font-weight:700}
.claim.pv-warn{background:#fff3e0;color:#9b5c14}.claim.pv-none{background:#eef1f3;color:#5b6b75}
.pv-banner{border-radius:10px;padding:12px 16px;margin:0 0 18px;font-weight:600;border:1px solid #e3d3b5;background:#fbf4e6;color:#6b4b14}
.pv-banner.pv-ok{background:#edf8f1;border-color:#b9e0c8;color:#16734a}.pv-banner.pv-such{background:#eef5ff;border-color:#c5d8f3;color:#235c9b}
.pv-banner.pv-bad{background:#fff0f1;border-color:#f0c4c8;color:#b3343c}.pv-banner.pv-warn{background:#fff5e8;border-color:#f0d6b0;color:#9b5c14}
.pv-banner small{display:block;font-weight:400;margin-top:4px;color:inherit}
.pv-table{width:100%;border-collapse:collapse;font-size:13.5px;margin:10px 0}.pv-table td,.pv-table th{border-bottom:1px solid #dce7eb;padding:8px 10px;text-align:left;vertical-align:top}
.pv-table th{background:#eef4f6}.pf-brief{background:#f3f8fa;border-left:3px solid #176274;padding:8px 12px;margin:0 0 10px}
</style>"""


def esc(v):
    return html.escape("" if v is None else str(v), quote=True)


def absaetze(werte):
    return "".join("<p>" + esc(x) + "</p>" for x in werte if x)


def safe_json(wert):
    raw = json.dumps(wert, ensure_ascii=False, allow_nan=False)
    for alt, neu in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e"), (" ", "\\u2028"), (" ", "\\u2029")):
        raw = raw.replace(alt, neu)
    return raw


class Seite:
    def __init__(self, daten):
        self.d = daten
        self.a = daten.get("auftrag", {})
        self.p = daten.get("pruefung") or {}
        if self.p and not self.p.get("ergebnis"):
            kopie = copy.deepcopy(daten)
            B.auswerten(kopie)
            self.p = kopie["pruefung"]
        self.urteile = {u["id"]: u for u in self.p.get("claims", []) + self.p.get("ableitungen", [])}
        self.quellen = {}
        for q in daten.get("quellen", []):
            art = B.QUELLENTYP.get(q.get("typ"), q.get("art", ""))
            self.quellen[q["id"]] = {"id": q["id"], "name": q.get("herausgeber") or "Quelle", "title": q.get("titel") or q.get("url"),
                                     "url": q.get("url"), "published_date": q.get("datum"),
                                     "source_kind": art + ("" if q.get("geoeffnet", True) else " · nur Suchtreffer"),
                                     "accessed_date": q.get("abruf") or "", "report_year": q.get("geschaeftsjahr"),
                                     "page": q.get("seite"), "section": q.get("abschnitt")}
        self.claims = {}
        for c in daten.get("claims", []):
            self.claims[c["id"]] = {"id": c["id"], "statement": c.get("aussage", ""), "kind": B.URSPRUNG.get(c.get("ursprung"), ""),
                                    "uncertainty": c.get("unsicherheit") or "", "source_ids": list(c.get("quellen", [])),
                                    "location": c.get("belegstelle") or "nicht angegeben", "evidence": "", "stufe": c.get("stufe"),
                                    "status": c.get("status"), "herkunft": c.get("herkunft")}
        self.interp = {i["id"]: i for i in B.interpretationen(daten)}
        self.firma = self.a.get("firma", "")
        self.ziel = {self.firma, self.a.get("kurzname") or self.firma}

    # ---------------------------------------------------------- Bausteine
    def urteil(self, cid):
        u = self.urteile.get(cid, {}).get("urteil")
        if self.p and u is None and cid in self.claims and B.im_umfang(self.d, cid):
            u = "nicht_einzeln_geprueft"
        return u

    def links(self, ids):
        out = []
        for cid in ids or []:
            if not cid:
                continue
            u = self.urteil(cid)
            if u in URTEIL:
                text, klasse, zeichen = URTEIL[u]
                out.append('<a class="claim pv-%s" href="#%s" title="%s">%s %s</a>' % (klasse, esc(cid), esc(text), zeichen, esc(cid)))
            else:
                out.append('<a class="claim" href="#%s">%s</a>' % (esc(cid), esc(cid)))
        return " ".join(out)

    def quelle_html(self, s):
        extra = [s.get("published_date") or "o. D.", s.get("source_kind"), "Abruf " + s["accessed_date"] if s.get("accessed_date") else ""]
        extra += [label + " " + str(s[k]) for k, label in (("report_year", "Geschäftsjahr"), ("page", "Seite"), ("section", "Abschnitt")) if s.get(k)]
        return '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a><span class="meta"> · %s</span>' % (
            esc(s["url"]), esc(s["name"] + " · " + s["title"]), esc(" · ".join(x for x in extra if x)))

    def evidence(self, row):
        teile = []
        for sid in row["source_ids"]:
            if sid in self.quellen:
                teile.append("<li>" + self.quelle_html(self.quellen[sid]) + '<p class="meta">Belegstelle: ' + esc(row["location"]) + "</p></li>")
        u = self.urteile.get(row["id"])
        pruef = ""
        if u:
            text = URTEIL.get(u.get("urteil"), (u.get("urteil"),))[0]
            pruef = '<p class="meta">Prüfung: ' + esc(text) + (" · " + esc(u["begruendung"]) if u.get("begruendung") else "") + (
                " · Korrektur: " + esc(u["korrektur"]) if u.get("korrektur") else "") + "</p>"
        return '<ul class="evidence">' + "".join(teile) + "</ul>" + pruef

    def fakten(self, ids, tiefe=0):
        """Faktenbasis einer Interpretation, auch über Zwischen-Interpretationen."""
        out = []
        for i in ids or []:
            if i in self.claims:
                out.append(i)
            elif i in self.interp and tiefe < 4:
                out += self.fakten(self.interp[i].get("basis"), tiefe + 1)
        return list(dict.fromkeys(out))

    def fakt_details(self, ids, klasse="es-fact"):
        out = ""
        for cid in self.fakten(ids):
            f = self.claims[cid]
            out += '<details class="%s"><summary>%s</summary><p class="meta">%s</p>%s%s%s</details>' % (
                klasse, esc(f["statement"]), esc(f["kind"]), absaetze([f["uncertainty"]]), self.evidence(f), self.links([cid]))
        return out

    def detail(self, row):
        body = '<p class="es-statement">' + esc(row.get("aussage") or row.get("insight") or "") + "</p>"
        if row.get("begruendung") or row.get("methode"):
            body += "<h4>Einordnung</h4>" + absaetze([row.get("begruendung"), row.get("methode")])
        if row.get("unsicherheit") or row.get("einschraenkung"):
            body += "<h4>Grenzen der Aussage</h4>" + absaetze([row.get("unsicherheit"), row.get("einschraenkung")])
        body += self.links([row.get("id")]) + "<h4>Faktenbasis &amp; Originalquellen</h4>" + self.fakt_details(row.get("basis"))
        return '<div class="es-detail">' + body + "</div>"

    def interp_card(self, row, titel=None):
        t = titel or row.get("titel") or row.get("aussage")
        return '<details class="card" data-es-title="%s"><summary>%s</summary>%s</details>' % (esc(t), esc(t), self.detail(row))

    def view_card(self, label, ids, text=None):
        body = ("<p>" + esc(text) + "</p>" if text else "") + "".join(
            "<p>" + esc(self.claims[c]["statement"]) + "</p>" + self.evidence(self.claims[c]) for c in ids if c in self.claims) + self.links(ids)
        return '<details class="card" data-es-title="%s"><summary>%s</summary><div class="es-detail">%s</div></details>' % (esc(label), esc(label), body)

    @staticmethod
    def section(titel, body, ident=None):
        if not body:
            return ""
        return '<section class="module"%s><h2>%s</h2>%s</section>' % (' id="%s"' % esc(ident) if ident else "", esc(titel), body)

    def luecken(self, container):
        out = "".join("<p>" + esc(x) + "</p>" for x in container.get("luecken", []))
        out += "".join("<p>Ausnahme von der Mindestregel „%s“: %s</p>" % (esc(B.REGELN.get(a.get("regel"), a.get("regel"))), esc(a.get("grund")))
                       for a in container.get("ausnahmen", []))
        return out

    # ---------------------------------------------------------- Überblick
    def summary(self):
        s = self.d.get("interpretation", {}).get("summary", {})
        out = ""
        if s.get("highlights"):
            out += '<div class="es-highlights">'
            for h in s["highlights"]:
                wert = str(h.get("wert", ""))
                status = h.get("art") == "status" or not re.search(r"\d", wert)
                klasse = " es-status" if status else " es-value-compact" if len(wert) > 28 else " es-value-medium" if len(wert) > 18 else ""
                out += ('<details class="es-highlight es-entry" data-es-title="%s"><summary><span class="es-label">%s</span>'
                        '<span class="es-value%s">%s</span><span class="es-scope">%s</span><span class="es-period">%s</span>'
                        '<span class="es-arrow" aria-hidden="true">↗</span></summary>%s</details>') % (
                    esc(h.get("label")), esc(h.get("label")), klasse, esc(wert), esc(h.get("bezug")), esc(h.get("zeitraum")),
                    self.detail(dict(h, aussage="%s: %s (%s, %s)" % (h.get("label"), wert, h.get("bezug"), h.get("zeitraum")))))
            out += "</div>"
        if s.get("kernaussagen"):
            out += '<div class="es-cards" data-count="%d">' % len(s["kernaussagen"])
            for n, k in enumerate(s["kernaussagen"], 1):
                out += ('<details class="es-card es-entry" data-es-title="%s"><summary><span class="es-kicker">%02d · Kernaussage</span>'
                        '<span class="es-headline">%s</span><span class="es-preview">%s</span><span class="es-arrow" aria-hidden="true">↗</span>'
                        "</summary>%s</details>") % (esc(k.get("titel")), n, esc(k.get("titel")), esc(k.get("vorschau")), self.detail(k))
            out += "</div>"
        return self.section("Executive Summary", out, "executive-summary")

    def entwicklungen(self):
        u = self.d.get("inhalt", {}).get("unternehmen") or {}
        events = u.get("timeline", [])
        if not events:
            return ""
        start, ende = PROFILE.media_window(self.a["stichtag"])
        drin = sorted((e for e in events if B.datum(e.get("datum")) and start <= B.datum(e["datum"]) <= ende), key=lambda e: e["datum"])
        zeilen = ""
        for e in drin:
            body = '<div class="es-detail"><p class="meta">Aktuelle Entwicklungen · %s · %s</p>' % (esc(e["datum"]), esc(e.get("status")))
            for cid in e.get("claims", []):
                f = self.claims.get(cid)
                if f:
                    body += '<p class="es-statement">%s</p><p class="meta">%s</p>%s%s<h4>Originalquellen &amp; Belegstellen</h4>%s' % (
                        esc(f["statement"]), esc(f["kind"]), absaetze([f["uncertainty"]]), self.links([cid]), self.evidence(f))
            body += "</div>"
            zeilen += ('<div class="event"><time datetime="%s">%s</time><details class="card event-card" data-es-title="%s"><summary>'
                       '<span class="event-title">%s</span><span class="event-arrow" aria-hidden="true">↗</span></summary>%s</details></div>') % (
                esc(e["datum"]), esc(e["datum"]), esc(e.get("ereignis")), esc(e.get("ereignis")), body)
        hinweis = '<p class="meta">Letzte vier Monate · %s–%s</p>' % (start.strftime("%d.%m.%Y"), ende.strftime("%d.%m.%Y"))
        inhalt = '<div class="timeline">' + zeilen + "</div>" if zeilen else "<p>Keine datierten Entwicklungen im Viermonatszeitraum.</p>"
        return self.section("Aktuelle Entwicklungen", hinweis + inhalt, "current-developments")

    def unternehmen(self):
        u = self.d.get("inhalt", {}).get("unternehmen") or {}
        karten = [self.view_card("%s: %s" % (z.get("feld"), z.get("wert")), z.get("claims", [])) for z in u.get("profil", [])]
        return self.section("Unternehmen im Überblick", '<div class="cards">' + "".join(karten) + "</div>" if karten else "", "company-overview")

    def insights(self, modul):
        rows = []
        for n, k in enumerate((k for k in self.d.get("interpretation", {}).get("keyfacts", []) if k.get("modul") == modul), 1):
            rows.append({"type": "module_insight", "module": {"markt": "market"}.get(modul, modul), "display_order": n, "headline": k.get("titel"),
                         "fact_text": k.get("fakt"), "statement": k.get("insight"), "_row": k})
        if not rows:
            return ""
        ziel = rows[0]["module"]

        def detail(row):
            k = row["_row"]
            out = "<h5>Herleitung · Analysteninterpretation</h5>" + absaetze([k.get("begruendung"), k.get("methode")]) + self.links([k.get("id")])
            if k.get("unsicherheit"):
                out += "<h5>Grenzen der Aussage</h5>" + absaetze([k["unsicherheit"]])
            return out + "<h5>Faktenbasis &amp; Originalquellen</h5>" + self.fakt_details(k.get("basis"), "mi-source-fact")
        return INSIGHTS.render(ziel, rows, {"schema_version": 1, "modules": [ziel]}, detail)

    def portfolio(self):
        produkte, ids, bewertungen = [], {}, {}
        reife = {r.get("angebot"): r for r in self.d.get("interpretation", {}).get("reife", [])}
        for feld, an in B.angebote(self.d):
            pid = B.slug(an.get("id") or an["name"])
            while pid in ids.values():
                pid += "-x"
            ids[an["name"]] = pid
            produkte.append({"id": pid, "label": an["name"], "short_label": an.get("kurzname") or an["name"][:28], "domain": feld["name"],
                             "claim_ids": [c for c in an.get("claims", []) if c in self.claims],
                             "sections": [{"label": s.get("titel"), "claim_ids": [c for c in s.get("claims", []) if c in self.claims]} for s in an.get("abschnitte", [])]})
            r = reife.get(an["name"])
            if r:
                bewertungen[pid] = {"id": r["id"], "score": r.get("stufe"), "statement": r.get("aussage", ""), "reasoning": r.get("begruendung", ""),
                                    "uncertainty": r.get("unsicherheit"), "next_stage_limit": r.get("naechste_stufe"), "coverage_note": r.get("abdeckung"),
                                    "depends_on": self.fakten(r.get("basis"))}
            elif B.STATUS_STUFE.get(an.get("status_stufe")):
                stufe = B.STATUS_STUFE[an["status_stufe"]]
                bewertungen[pid] = {"id": "", "score": stufe, "statement": "Stufe aus dem belegten Status abgeleitet: " + STAGES[str(stufe)] + ".",
                                    "reasoning": an.get("status") or "", "uncertainty": "Keine gesonderte Analysteneinordnung.", "depends_on": []}
        if not produkte:
            return ""
        out = PORTFOLIO.render({"products": produkte}, bewertungen, self.claims, self.evidence, self.links, STAGES)
        for feld, an in B.angebote(self.d):
            marke = 'id="product-%s"' % esc(ids[an["name"]])
            pos = out.find(marke)
            pos = out.find("<dl>", pos) if pos >= 0 else -1
            if pos >= 0:
                kurz = '<dt>Kurzprofil</dt><dd class="pf-brief">%s</dd>' % absaetze([
                    "Anwendung: " + an["anwendung"] if an.get("anwendung") else "", "Eigenschaften: " + an["eigenschaften"] if an.get("eigenschaften") else "",
                    "Status laut Beleg: " + an["status"] if an.get("status") else ""])
                out = out[:pos + 4] + kurz + out[pos + 4:]
        return '<section class="module" id="portfolio">' + out + self.insights("portfolio") + "</section>"

    def netzwerk(self):
        cl = self.d.get("inhalt", {}).get("cluster") or {}
        if not cl.get("beziehungen"):
            return ""
        akteure = {x["name"]: x for x in cl.get("akteure", [])}
        knoten = {"target": {"id": "target", "label": self.a.get("kurzname") or self.firma, "legal_name": self.firma, "kind": "target", "cluster": "structure"}}
        namen = {n: "target" for n in self.ziel}
        produkte = {B.slug(an["name"]): an["name"] for _, an in B.angebote(self.d)}

        def knoten_id(name, typ, gegenueber_ist_ziel, ist_von):
            if name in namen:
                return namen[name]
            nid = "n-" + B.slug(name)
            while nid in knoten:
                nid += "-x"
            ak = akteure.get(name, {})
            if ak.get("art") in ART_KIND:
                kind = ART_KIND[ak["art"]]
            elif typ == "Eigentum":
                kind = "owner" if ist_von else "subsidiary"
            else:
                kind = TYP_KIND.get(typ, "other")
            node = {"id": nid, "label": name, "legal_name": ak.get("langname") or name, "kind": kind}
            if ak.get("bereich") in BEREICH:
                node["cluster"] = BEREICH[ak["bereich"]]
            else:
                node["cluster"] = CLUSTER.group(node)
            if ak.get("fokus"):
                node["focus"] = True
            knoten[nid] = node
            namen[name] = nid
            return nid

        kanten, zeilen, quellen_ids = [], [], []
        for n, b in enumerate(cl["beziehungen"], 1):
            von = knoten_id(b["von"], b.get("typ"), b["zu"] in self.ziel, True)
            zu = knoten_id(b["zu"], b.get("typ"), b["von"] in self.ziel, False)
            ids = [c for c in b.get("claims", []) if c in self.claims]
            sids = list(dict.fromkeys(s for c in ids for s in self.claims[c]["source_ids"] if s in self.quellen))
            quellen_ids += sids
            zusammenfassung = " · ".join(x for x in (b.get("gegenstand"), b.get("anteil_rolle")) if x) or b.get("typ")
            kante = {"id": "e%d" % n, "from": von, "to": zu, "type": b.get("typ"), "summary": zusammenfassung, "status": b.get("status") or "nicht angegeben",
                     "as_of": str(b.get("datum"))[:10], "categories": [TYP_KATEGORIE.get(b.get("typ"), "other")], "claim_ids": ids, "source_ids": sids,
                     "product_ids": [B.slug(p) for p in b.get("produkte", []) if B.slug(p) in produkte]}
            for k, feld in (("capital_share", "kapitalanteil"), ("voting_share", "stimmrechte"), ("control", "kontrolle"), ("uncertainty", "unsicherheit")):
                if b.get(feld):
                    kante[k] = b[feld]
            kanten.append(kante)
            detail = "<p>" + esc(zusammenfassung) + "</p>" + self.links(ids)
            for k, label in (("kapitalanteil", "Kapitalanteil"), ("stimmrechte", "Stimmrechte"), ("kontrolle", "Kontrolle"), ("unsicherheit", "Evidenzgrenze")):
                if b.get(k):
                    detail += "<p>" + esc(label + ": " + str(b[k])) + "</p>"
            if b.get("produkte"):
                detail += "<p>Produktbezug: " + esc(", ".join(b["produkte"])) + "</p>"
            zeilen.append("<tr><td>%s</td><td>%s%s</td><td>%s</td><td>%s</td></tr>" % (
                esc(knoten[von]["label"] + " → " + knoten[zu]["label"]), esc(b.get("typ")), detail,
                esc((b.get("status") or "") + " · " + str(b.get("datum"))), "<br>".join(self.quelle_html(self.quellen[s]) for s in sids)))
        benutzt = {p for k in kanten for p in k["product_ids"]}
        netz = {"schema_version": 1, "company": self.firma, "as_of": self.a.get("stichtag"), "target_id": "target",
                "nodes": list(knoten.values()), "edges": kanten,
                "products": [{"id": p, "label": produkte[p]} for p in produkte if p in benutzt],
                "sources": [self.quellen[s] for s in dict.fromkeys(quellen_ids)]}
        frag = vorlage("cluster-network.html")
        frag = frag.replace("__CLUSTER_NETWORK_JSON__", safe_json(netz))
        frag = frag.replace("<tbody></tbody>", "<tbody>" + "".join(zeilen) + "</tbody>", 1)
        frag = frag.replace("__CLUSTER_ACTOR_TABLES__", CLUSTER.actor_tables(netz), 1)
        if "tableBody.replaceChildren();" not in frag:
            frag = frag.replace("const tableBody=root.querySelector('tbody');", "const tableBody=root.querySelector('tbody');tableBody.replaceChildren();", 1)
        frag = frag.replace("window.addEventListener('beforeprint',()=>{root.querySelector('.cn-table').open=true;});", "", 1)
        return self.section("Cluster · Technologie, Industrie & Marktzugang", frag + self.insights("cluster"), "cluster-analysis")

    def praesenz(self):
        m = self.d.get("inhalt", {}).get("markt") or {}
        if not m.get("praesenz"):
            return ""
        regionen, bewertung = [], {}
        stufen = {r.get("region"): r for r in self.d.get("interpretation", {}).get("praesenz", [])}
        for reg in m["praesenz"]:
            rid = "r-" + B.slug(reg["region"])
            akt = []
            for n, x in enumerate(reg.get("aktivitaeten", []), 1):
                a = {"id": "%s-%d" % (rid, n), "actor": x.get("akteur", ""), "country": x.get("land", ""), "location": x.get("ort", ""),
                     "product_scope": x.get("produktbezug") or reg.get("produktbezug", ""), "description": x.get("beschreibung", ""),
                     "kind": FUNKTION_KIND.get(x.get("funktion"), "partner"), "operator": BETREIBER_OP.get(x.get("betreiber"), "partner"),
                     "status": "announced" if x.get("status") == "angekündigt" else "operational", "status_date": x.get("statusdatum"),
                     "claim_ids": [c for c in x.get("claims", []) if c in self.claims], "ownership_note": x.get("eigentum")}
                if a["operator"] == "jv":
                    a["control"] = KONTROLLE.get(x.get("kontrolle"), "unknown")
                    a["control_claim_ids"] = x.get("kontrollbeleg", [])
                    a["control_note"] = x.get("kontrollnotiz")
                akt.append(a)
            claim_ids = list(dict.fromkeys(c for a in akt for c in a["claim_ids"] + a.get("control_claim_ids", [])))
            typ = reg.get("praesenzart") or ", ".join(dict.fromkeys("%s (%s)" % (x.get("funktion"), x.get("betreiber")) for x in reg.get("aktivitaeten", [])))
            regionen.append({"id": rid, "label": reg["region"], "countries": reg.get("laender", []), "presence_type": typ[:100],
                             "geographic_scope": reg.get("schwerpunkt") or ", ".join(reg.get("laender", [])),
                             "product_scope": reg.get("produktbezug") or "", "focus": bool(reg.get("fokus")), "claim_ids": claim_ids,
                             "activities": akt, "coverage_note": reg.get("abdeckung") or ""})
            r = stufen.get(reg["region"])
            if r:
                bewertung[rid] = {"id": r["id"], "score": r.get("stufe"), "assessment_status": r.get("status"), "statement": r.get("aussage", ""),
                                  "reasoning": r.get("begruendung", ""), "method": r.get("methode") or "regional-presence-v2",
                                  "next_stage_limit": r.get("naechste_stufe"), "coverage_note": r.get("abdeckung"), "uncertainty": r.get("unsicherheit")}

        def detail(region, row):
            out = "<h4>Wie vertreten?</h4>"
            for a in region["activities"]:
                zustand = "angekündigt" if a["status"] == "announced" else "operativ dokumentiert"
                out += '<div class="rp-activity"><strong>%s</strong><p>%s</p><p class="meta">%s</p>%s%s</div>' % (
                    esc(a["actor"]), esc(a["description"]), esc(" · ".join(x for x in (PRESENCE.operator_label(a), a["country"], a["location"], a["product_scope"],
                                                                                     zustand, a.get("status_date") or "Statusdatum nicht belegt") if x)),
                    absaetze([a.get("ownership_note"), a.get("control_note")]), self.links(a["claim_ids"]))
            if not region["activities"]:
                out += '<p class="rp-empty">Keine konkreten Präsenzaktivitäten belegt.</p>'
            if row:
                titel = ("Warum Stufe %s?" % row["score"]) if row["score"] is not None else "Warum derzeit nur geplant?" if row.get("assessment_status") == "geplant" else "Warum nicht eindeutig bestimmbar?"
                out += "<h4>" + esc(titel) + "</h4>" + absaetze([row["statement"], row["reasoning"], row.get("method"), row.get("next_stage_limit"), row.get("coverage_note")]) + self.links([row["id"]])
            else:
                out += '<p class="rp-empty">Keine Präsenzeinstufung vorhanden.</p>'
            out += "<h4>Reichweite des Nachweises</h4>" + absaetze([region["geographic_scope"], region["product_scope"], region["coverage_note"], row.get("uncertainty") if row else None])
            out += "<h4>Originalquellen &amp; Belegstellen</h4>" + self.fakt_details(region["claim_ids"], "rp-source-fact")
            return out
        return self.section("Regionale Präsenz auf einen Blick.", PRESENCE.render(regionen, bewertung, detail, self.a["stichtag"]), "regional-presence")

    def markt(self):
        m = self.d.get("inhalt", {}).get("markt") or {}
        kennzahlen = "".join(self.view_card("%s: %s" % (k.get("kennzahl"), k.get("wert")), k.get("claims", []), k.get("definition")) for k in m.get("kennzahlen", []))
        out = "<h3>Markt im Überblick</h3><div class=\"cards\">" + kennzahlen + "</div>" if kennzahlen else ""
        v = m.get("vergleich") or {}
        if v.get("zeilen") and v.get("kriterien"):
            kriterien = []
            for k in v["kriterien"]:
                kriterien.append({"id": k["id"], "label": k.get("name"), "display_type": KRITERIUM.get(k.get("typ"), "Profil"), "unit": k.get("einheit", ""),
                                  "anchors": {str(a): t for a, t in (k.get("stufen") or {}).items()}, "question": k.get("frage", ""),
                                  "evidence_required": k.get("beleganforderung", ""), "conditions": k.get("bedingungen")})
            peers, zellen, referenz = [], {}, None
            for n, z in enumerate(v["zeilen"], 1):
                pid = "peer-%d" % n
                peers.append({"id": pid, "label": z.get("akteur", "") + (" · " + z["angebot"] if z.get("angebot") else "")})
                if z.get("referenz") or z.get("akteur") in self.ziel:
                    referenz = referenz or pid
                for k in kriterien:
                    x = (z.get("zellen") or {}).get(k["id"])
                    row = {"id": "Z%d-%s" % (n, k["id"]), "claims": (x or {}).get("claims", [])}
                    if not x:
                        row.update(cell_status="nicht öffentlich belegt", value=None, statement="Keine öffentliche Angabe gefunden.", reasoning="", uncertainty="")
                    elif x.get("nicht_anwendbar"):
                        row.update(cell_status="nicht anwendbar", value=None, statement=x.get("text") or "Nicht anwendbar.", reasoning=x.get("einordnung", ""), uncertainty=x.get("grenze", ""))
                    else:
                        wert = x.get("stufe") if k["display_type"] == "Evidenzstufe" else x.get("wert") if k["display_type"] == "Kennzahl" and x.get("wert") is not None else x.get("text")
                        row.update(cell_status="bewertet", value=wert, statement=x.get("aussage") or x.get("text", ""), reasoning=x.get("einordnung", ""), uncertainty=x.get("grenze", ""))
                    row["headline"] = (x or {}).get("titel") or ((x or {}).get("text") if k["display_type"] != "Profil" else None)
                    row["preview"] = (x or {}).get("vorschau", "")
                    zellen[pid, k["id"]] = row
            anzahl = {r["id"]: len({self.quellen[s]["url"] for c in r["claims"] if c in self.claims for s in self.claims[c]["source_ids"] if s in self.quellen}) for r in zellen.values()}

            def detail(row):
                body = '<div class="cm-detail-grid"><div class="cm-discussion"><p class="cm-statement">%s</p>' % esc(row["statement"])
                if row.get("reasoning"):
                    body += "<h4>Einordnung</h4>" + absaetze([row["reasoning"]])
                body += "</div>"
                if row.get("uncertainty"):
                    body += '<aside class="cm-limits"><h4>Grenzen der Aussage</h4>' + absaetze([row["uncertainty"]]) + "</aside>"
                body += '</div><div class="cm-facts"><h4>Faktenbasis &amp; Originalquellen</h4>' + self.fakt_details(row["claims"], "cm-fact")
                return body + "</div>"
            out += CAPABILITY.render(kriterien, peers, zellen, self.firma, detail, anzahl, referenz)
        if not out and not self.insights("markt"):
            return ""
        titel = "Capability Matrix · Wettbewerbsvergleich" + (" · " + v["einheit"] if v.get("einheit") else "")
        return self.section(titel, out + self.insights("markt"), "capability-matrix")

    def einordnung(self):
        pos = self.d.get("interpretation", {}).get("positionierung", [])
        karten = ['<div><p class="meta">%s · %s</p>%s</div>' % (esc(p.get("dimension")), esc(p.get("urteil")), self.interp_card(p, p.get("aussage"))) for p in pos]
        return self.section("Einordnung · Technologie, Industrie & Markt", '<div class="cards">' + "".join(karten) + "</div>" if karten else "")

    def swot(self):
        s = self.d.get("interpretation", {}).get("swot", {})
        if not any(s.get(q) for q in ("staerken", "schwaechen", "chancen", "risiken")):
            return ""
        teile = ""
        for q, key, titel in (("staerken", "Strengths", "Stärken"), ("schwaechen", "Weaknesses", "Schwächen"), ("chancen", "Opportunities", "Chancen"), ("risiken", "Threats", "Risiken")):
            karten = "".join(self.interp_card(p) for p in s.get(q, [])) or '<p class="meta">Keine belegte Aussage in dieser Kategorie.</p>'
            teile += '<div class="quadrant" data-swot="%s"><h3>%s</h3>%s</div>' % (key, titel, karten)
        return self.section("SWOT · Analysteninterpretation", '<div class="swot">' + teile + "</div>")

    def datenluecken(self):
        inhalt = self.d.get("inhalt", {})
        teile = ""
        for k in ("unternehmen", "portfolio", "cluster", "markt"):
            c = inhalt.get(k)
            if isinstance(c, dict):
                t = self.luecken(c)
                if k == "cluster" and c.get("berichte"):
                    t += "<h4>Ausgewertete Geschäftsberichte</h4>" + "".join(
                        '<dl class="note"><dt>Akteur</dt><dd>%s</dd><dt>Bericht</dt><dd>%s (%s)</dd><dt>Abschnitte</dt><dd>%s</dd><dt>Status</dt><dd>%s</dd></dl>' % (
                            esc(b.get("akteur")), esc(b.get("bericht")), esc(b.get("jahr")), esc(b.get("abschnitte")), esc(b.get("status"))) for b in c["berichte"])
                if t:
                    teile += "<details><summary>%s · Rechercheabdeckung und offene Punkte</summary>%s</details>" % (esc(B.KAPITEL_TITEL[k]), t)
        for p in inhalt.get("personen", []):
            t = self.luecken(p)
            if t:
                teile += "<details><summary>Gesprächspartner %s · offene Punkte</summary>%s</details>" % (esc(p.get("name")), t)
        o = self.d.get("offen", {})
        teile += absaetze(self.d.get("interpretation", {}).get("grenzen", [])) + absaetze(o.get("luecken", []))
        if o.get("fragen"):
            teile += "<h4>Fragen für das Gespräch</h4><ol>" + "".join("<li>" + esc(x) + "</li>" for x in o["fragen"]) + "</ol>"
        if not teile:
            return ""
        return ('<section class="module"><details class="data-gaps"><summary style="cursor:pointer"><h2 style="display:inline;margin:0">'
                'Datenlücken &amp; offene Fragen</h2></summary><div style="margin-top:18px">' + teile + "</div></details></section>")

    def banner(self):
        if not self.p:
            return '<div class="pv-banner pv-warn">Ungeprüfte Faktenbasis<small>Erstellt vom Recherche-Agenten. Eine unabhängige Prüfung und Vertiefung ist über den Prüf-Agenten möglich.</small></div>'
        erg = self.p.get("ergebnis")
        klasse = {"bestanden": "ok", "bestanden_mit_einschraenkungen": "such", "nicht_bestanden": "bad"}.get(erg, "warn")
        return '<div class="pv-banner pv-%s">%s<small>%s Details im Reiter Quellen unter „Prüfbericht“.</small></div>' % (
            klasse, esc(B.ERGEBNIS.get(erg, "Prüfung nicht ausgewertet")), esc(self.p.get("zusammenfassung", "")))

    # ---------------------------------------------------------- weitere Seiten
    def personen(self):
        seiten, quellen = [], ""
        for n, p in enumerate(self.d.get("inhalt", {}).get("personen", []), 1):
            ids = list(dict.fromkeys(c for c in B.alle_verweise(p, ("claims",)) if c in self.claims))
            if not ids:
                continue
            prof = {"name": p["name"], "claim_ids": ids,
                    "snapshot": [{"label": x.get("feld"), "value": x.get("wert"), "claim_ids": x.get("claims", [])} for x in p.get("snapshot", [])],
                    "career": [{"period": x.get("zeitraum"), "organization": x.get("organisation"), "role": x.get("rolle"), "context": x.get("kontext", ""), "claim_ids": x.get("claims", [])} for x in p.get("werdegang", [])],
                    "expertise": [{"label": x.get("titel"), "text": x.get("text"), "claim_ids": x.get("claims", [])} for x in p.get("fachprofil", [])],
                    "responsibilities": [{"label": x.get("titel"), "text": x.get("text"), "claim_ids": x.get("claims", [])} for x in p.get("verantwortung", [])],
                    "media": [{"id": "m%d" % i, "published_date": x["datum"], "event_date": x.get("ereignisdatum"), "category": MEDIEN_KAT.get(x.get("kategorie"), "media"),
                               "format": x.get("format") or "Beitrag", "title": x.get("titel"), "preview": x.get("vorschau") or "", "claim_ids": x.get("claims", []),
                               "access_note": x.get("zugriff") or "Zugriff nicht dokumentiert.", "quote": x.get("zitat")} for i, x in enumerate(p.get("medien", []), 1)]}
            if p.get("einleitung"):
                prof["intro"] = {"text": p["einleitung"].get("text"), "claim_ids": p["einleitung"].get("claims", [])}
            prefix = "person-" if n == 1 else "person-%d-" % n
            ns = lambda h: h.replace('id="person-', 'id="' + prefix).replace('href="#person-', 'href="#' + prefix)
            kopf = '<p class="meta">Gesprächspartner aus dem Auftrag (Nutzerangabe): %s · Verifizierung: %s</p>' % (
                esc(p.get("name") + (" · " + p["position_laut_nutzer"] if p.get("position_laut_nutzer") else "")), esc(p.get("verifizierung", "nicht verifiziert")))
            body = '<section class="module profile-module">' + kopf + ns(PROFILE.render(prof, self.claims, self.quellen, self.firma, self.a["stichtag"])) + "</section>"
            body += ns(PROFILE.render_media(prof, self.claims, self.a["stichtag"], self.quellen))
            quellen += self.section(p["name"] + " · Quellen & Evidenz", ns(PROFILE.render_sources(prof, self.claims, self.quellen)), prefix + "profile-sources")
            seiten.append(("page-profile" if n == 1 else "page-profile-%d" % n, p["name"], body))
        return seiten, quellen

    def fokus(self):
        seiten = []
        for f in self.d.get("inhalt", {}).get("fokus", []):
            def zeilen(liste, mapping, prefix):
                return [dict({"id": "%s%d" % (prefix, i)}, **mapping(x)) for i, x in enumerate(liste, 1)]
            ausn = {a.get("regel"): a.get("grund") for a in f.get("ausnahmen", [])}
            de = f.get("definition") or {}
            seite = {"id": f["id"], "label": f.get("titel", f["id"]), "briefing_type": "topic_market",
                     "overview": (f.get("ueberblick") or {}).get("text", ""), "claim_ids": (f.get("ueberblick") or {}).get("claims", []),
                     "market_definition": {"label": de.get("text", ""), "geography": de.get("region", "global"), "period": de.get("zeitraum", ""),
                                           "boundary": de.get("abgrenzung", ""), "claim_ids": de.get("claims", [])},
                     "glossary": zeilen(f.get("glossar", []), lambda x: {"label": x.get("begriff"), "definition": x.get("definition"), "claim_ids": x.get("claims", [])}, "g"),
                     "key_metrics": zeilen(f.get("kennzahlen", []), lambda x: {"label": x.get("kennzahl"), "value": x.get("wert"), "unit": x.get("einheit", ""),
                                                                              "period": x.get("zeitraum", ""), "scope": x.get("abgrenzung", ""), "definition": x.get("definition", ""),
                                                                              "metric_type": FOKUS_TYP.get(x.get("typ"), "other"), "claim_ids": x.get("claims", []),
                                                                              "qualifier": x.get("zusatz", "")}, "k"),
                     "metrics_note": ausn.get("fokus.kennzahlen"),
                     "segments": zeilen(f.get("segmente", []), lambda x: {"label": x.get("titel"), "description": x.get("text"), "claim_ids": x.get("claims", [])}, "s"),
                     "segments_note": None if f.get("segmente") else "Keine belegten Segmentangaben.",
                     "value_chain": zeilen(f.get("wertschoepfung", []), lambda x: {"label": x.get("titel"), "description": x.get("text"), "claim_ids": x.get("claims", [])}, "w"),
                     "value_chain_note": None if f.get("wertschoepfung") else "Keine belegten Angaben zur Wertschöpfung.",
                     "actors": zeilen(f.get("akteure", []), lambda x: {"label": x.get("akteur"), "role": x.get("rolle", ""), "offering": x.get("angebot", ""),
                                                                      "segment": x.get("segment", ""), "status": x.get("stand", ""), "claim_ids": x.get("claims", [])}, "a"),
                     "selection_note": f.get("auswahl") or "Auswahl nach Relevanz für das Thema; keine Vollständigkeit.",
                     "actors_note": ausn.get("fokus.akteure"),
                     "theses": zeilen(f.get("kernaussagen", []), lambda x: {"label": x.get("titel") or x.get("text"), "claim_ids": x.get("claims", [])}, "t"),
                     "coverage_note": ausn.get("fokus.kernaussagen"),
                     "charts": [], "timeline": zeilen(f.get("entwicklungen", []), lambda x: {"date": x.get("datum"), "label": x.get("ereignis"), "status": x.get("status", ""),
                                                                                           "claim_ids": x.get("claims", [])}, "e"),
                     "timeline_note": None if f.get("entwicklungen") else "Keine datierten Entwicklungen im Sechsmonatsfenster gefunden.",
                     "meeting_questions": zeilen(f.get("fragen", []), lambda x: {"label": x.get("frage"), "claim_ids": x.get("claims", [])}, "q"),
                     "gaps": list(f.get("luecken", [])) + ["Ausnahme: " + a.get("grund", "") for a in f.get("ausnahmen", [])]}

            def details(ids):
                return '<div class="focus-evidence">' + "".join("<p>" + esc(self.claims[c]["statement"]) + "</p>" + absaetze([self.claims[c]["uncertainty"]])
                                                                for c in dict.fromkeys(ids) if c in self.claims) + self.links(ids) + "</div>"
            seiten.append(("page-focus-" + B.slug(f["id"]), seite["label"], FOCUS.render(seite, details, self.a["stichtag"])))
        return seiten

    def pruefbericht(self):
        if not self.p:
            return ""
        aus = self.p.get("auswertung", {})
        zaehler = {}
        for u in self.p.get("claims", []) + self.p.get("ableitungen", []):
            zaehler[u.get("urteil")] = zaehler.get(u.get("urteil"), 0) + 1
        umfang = self.p.get("umfang") if isinstance(self.p.get("umfang"), dict) else {}
        kap = umfang.get("kapitel", "alle")
        body = "<p><b>%s.</b> %s</p>" % (esc(B.ERGEBNIS.get(self.p.get("ergebnis"), "Prüfung nicht ausgewertet")), esc(self.p.get("zusammenfassung")))
        body += '<p class="meta">Stand %s · Umfang: %s%s</p>' % (esc(self.p.get("stand")), esc("alle Kapitel" if kap == "alle" else ", ".join(B.KAPITEL_TITEL.get(k, k) for k in kap)),
                                                               " · nur A-Fakten" if umfang.get("nur_a") else "")
        body += '<table class="pv-table"><thead><tr><th>Urteil</th><th>Anzahl</th></tr></thead><tbody>' + "".join(
            "<tr><td>%s</td><td>%d</td></tr>" % (esc(URTEIL.get(k, (k,))[0]), v) for k, v in sorted(zaehler.items(), key=lambda x: str(x[0]))) + "</tbody></table>"
        for titel, ids in (("Nicht bestanden wegen", aus.get("nicht_bestanden_wegen")), ("Noch offen", aus.get("offen")), ("Mit Einschränkung", aus.get("eingeschraenkt")),
                           ("Betroffene Ableitungen", aus.get("betroffene_ableitungen"))):
            if ids:
                body += "<p><b>%s:</b> %s</p>" % (titel, self.links(ids))
        if self.p.get("aenderungen"):
            body += '<h3>Änderungsprotokoll</h3><table class="pv-table"><thead><tr><th>ID</th><th>Änderung</th><th>Vorher</th><th>Nachher</th><th>Grund</th></tr></thead><tbody>' + "".join(
                "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (self.links([x.get("id")]) if x.get("id") in self.claims else esc(x.get("id")),
                                                                                    esc(ART_AENDERUNG.get(x.get("art"), x.get("art"))), esc(x.get("alt")), esc(x.get("neu")), esc(x.get("grund")))
                for x in self.p["aenderungen"]) + "</tbody></table>"
        befunde = [u for u in self.p.get("claims", []) + self.p.get("ableitungen", []) if u.get("korrektur") or u.get("urteil") in ("abweichend", "nicht_belegt", "nicht_gestuetzt", "eingeschraenkt")]
        if befunde:
            body += '<h3>Befunde</h3><table class="pv-table"><thead><tr><th>ID</th><th>Urteil</th><th>Befund</th><th>Korrektur / Vorschlag</th></tr></thead><tbody>' + "".join(
                "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (self.links([u["id"]]), esc(URTEIL.get(u.get("urteil"), ("",))[0]), esc(u.get("begruendung")), esc(u.get("korrektur")))
                for u in befunde) + "</tbody></table>"
        if self.p.get("vertiefung"):
            body += "<h3>Vertiefung</h3><ul>" + "".join("<li><b>%s:</b> %s</li>" % (esc(x.get("bereich")), esc(x.get("ergebnis"))) for x in self.p["vertiefung"]) + "</ul>"
        if self.p.get("stichprobe"):
            body += "<h3>Stichproben</h3><ul>" + "".join("<li>%s · %s · %s</li>" % (esc(x.get("gruppe")), esc(x.get("auswahl")), esc(x.get("ergebnis"))) for x in self.p["stichprobe"]) + "</ul>"
        if self.p.get("hinweise"):
            body += "<h3>Hinweise</h3><ul>" + "".join("<li>" + esc(x) + "</li>" for x in self.p["hinweise"]) + "</ul>"
        return self.section("Prüfbericht", body, "pruefbericht")

    def register(self):
        out = '<label class="source-search">Quellen und Aussagen durchsuchen<input id="source-search-input" type="search" placeholder="Stichwort, Claim oder Quelle"></label>'
        for cid, f in self.claims.items():
            u = self.urteil(cid)
            status = URTEIL[u][0] if u in URTEIL else "ohne unabhängige Prüfung"
            herkunft = " · aus der Vertiefung" if f.get("herkunft") == "vertiefung" else ""
            out += '<details class="claim-detail" id="%s"><summary>%s</summary><p class="meta">%s</p>%s%s</details>' % (
                esc(cid), esc(cid + " · " + f["statement"]), esc("%s · Prüfstufe %s · %s%s · %s" % (f["kind"], f.get("stufe"), f.get("status") or "", herkunft, status)),
                absaetze([f["uncertainty"]]), self.evidence(f))
        for iid, row in self.interp.items():
            u = self.urteile.get(iid, {}).get("urteil")
            status = URTEIL[u][0] if u in URTEIL else ("nicht geprüft" if self.p else "ohne unabhängige Prüfung")
            text = row.get("aussage") or row.get("insight") or "%s: %s" % (row.get("label"), row.get("wert"))
            out += '<details class="claim-detail" id="%s"><summary>%s</summary><p class="meta">Analysteninterpretation · %s</p>%s%s</details>' % (
                esc(iid), esc(iid + " · " + str(text)), esc(status), absaetze([row.get("begruendung"), row.get("methode"), row.get("unsicherheit"), row.get("naechste_stufe")]),
                self.links(row.get("basis")))
        out += "<h3>Dokumente</h3>" + "".join("<p>" + self.quelle_html(s) + "</p>" for s in self.quellen.values())
        return self.section("Aussagen, Belegstellen & Originalquellen", out, "sources-register")

    def abnahme(self, hinweise, seiten):
        qs = self.d.get("quellen", [])
        punkte = ["Stichtag: %s" % self.a.get("stichtag"), "Modus: %s" % self.a.get("modus"), "Seiten: %s" % ", ".join(t for _, t, _ in seiten),
                  "Claims: %d, davon A: %d" % (len(self.claims), sum(1 for c in self.claims.values() if c.get("stufe") == "A")),
                  "Quellen: %d, geöffnet: %d, nur Suchtreffer: %d" % (len(qs), sum(1 for q in qs if q.get("geoeffnet")), sum(1 for q in qs if not q.get("geoeffnet"))),
                  "Begründete Ausnahmen von Mindestregeln: %d" % len(list(B.alle_ausnahmen(self.d))),
                  B.ERGEBNIS.get(self.p.get("ergebnis"), "") if self.p else "Ohne unabhängige Prüfung erstellt.",
                  "Gerendert mit briefing_html.py %s und briefing.py %s" % (VERSION, B.VERSION)]
        body = "<ul>" + "".join("<li>" + esc(x) + "</li>" for x in punkte if x) + "</ul>"
        if hinweise:
            body += "<details><summary>Technische Hinweise der Validierung (%d)</summary><ul>%s</ul></details>" % (len(hinweise), "".join("<li>" + esc(h) + "</li>" for h in hinweise))
        return self.section("Abnahme", body, "abnahme")

    # ---------------------------------------------------------- Zusammenbau
    def bauen(self, hinweise):
        main = self.banner() + self.summary() + self.entwicklungen() + self.unternehmen() + self.portfolio() + self.netzwerk() + self.praesenz() + \
            self.markt() + self.einordnung() + self.swot() + self.datenluecken()
        seiten = [("page-main", "Überblick", main)]
        personen, personen_quellen = self.personen()
        seiten += personen
        seiten += self.fokus()
        quellen = self.pruefbericht() + self.register() + personen_quellen
        seiten.append(("page-sources", "Quellen", quellen))
        seiten[-1] = ("page-sources", "Quellen", quellen + self.abnahme(hinweise, seiten))
        tabs = "".join('<button type="button" role="tab" id="tab-%s" data-page="%s" aria-controls="%s">%d · %s</button>' % (i, i, i, n, esc(t)) for n, (i, t, _) in enumerate(seiten, 1))
        inhalt = "".join('<div class="page" role="tabpanel" aria-labelledby="tab-%s" id="%s"><p class="page-kicker">%02d / %02d · %s</p>%s</div>' % (
            i, i, n, len(seiten), esc(t), body) for n, (i, t, body) in enumerate(seiten, 1))
        inhalt = STIL + (FOCUS.css() if self.d.get("inhalt", {}).get("fokus") else "") + INSIGHTS.css() + inhalt
        teile = []
        if self.a.get("modus") == "modul":
            teile.append("Modulauftrag: " + ", ".join(B.MODULE.get(m, m) for m in self.a.get("module", [])))
        if self.a.get("fokus"):
            teile.append("Fokus: " + ", ".join(f.get("titel", "") for f in self.a["fokus"]))
        if self.a.get("personen"):
            teile.append("Gesprächspartner: " + "; ".join(p.get("name", "") + (" · " + p["position_laut_nutzer"] if p.get("position_laut_nutzer") else "") for p in self.a["personen"]))
        badge = "Ungeprüfte Faktenbasis & Analysteninterpretation" if not self.p else B.ERGEBNIS.get(self.p.get("ergebnis"), "Geprüft") + " · Fakten & Analysteninterpretation"
        werte = {"TITLE": esc(self.firma), "DATE": esc(self.a.get("stichtag")), "SCOPE": esc(" · ".join(teile)), "BADGE": esc(badge), "TABS": tabs, "CONTENT": inhalt}
        rahmen = vorlage("briefing.html")
        seite = re.sub(r"__([A-Z]+)__", lambda m: werte.get(m[1], m[0]), rahmen)
        block = '<script type="application/json" id="briefing-daten">' + B.datenblock(self.d) + "</script>"
        return seite.replace("</body>", block + "</body>", 1) if "</body>" in seite else seite + block


def rendern(daten):
    fehler, hinweise = B.validieren(daten)
    if fehler:
        raise B.Fehler("Validierung fehlgeschlagen, keine HTML erzeugt:\n- " + "\n- ".join(fehler))
    return Seite(daten).bauen(hinweise)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Briefing-HTML im festen Layout erzeugen")
    ap.add_argument("--daten", required=True, help=".xlsx, .json oder frühere Briefing-HTML")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    try:
        text = rendern(B.einlesen(a.daten))
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("geschrieben: %s (%d Zeichen)" % (a.out, len(text)))
        return 0
    except B.Fehler as x:
        print("FEHLER:", x, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
