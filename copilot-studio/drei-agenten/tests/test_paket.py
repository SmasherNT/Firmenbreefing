"""Tests für das Datenskript (briefing-grundlagen) und den HTML-Renderer (briefing-html) mit fiktiven Beispielteilen."""
import contextlib, copy, glob, importlib.util, io, json, os, re, tempfile, unittest

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def modul(name, pfad):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASIS, pfad))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


B = modul("briefing", "skills/briefing-grundlagen/scripts/briefing.py")
H = modul("briefing_html", "skills/briefing-html/scripts/briefing_html.py")


def teil(nr):
    with open(glob.glob(os.path.join(BASIS, "beispiel", "%s-*.json" % nr))[0], encoding="utf-8") as f:
        return json.load(f)


def recherche(bis="07"):
    daten = None
    for nr in ("01", "02", "03", "04", "05", "06", "07"):
        daten, _ = B.zusammenfuehren(daten, teil(nr))
        if nr == bis:
            break
    return daten


def geprueft():
    d, _ = B.zusammenfuehren(recherche(), teil("08"), ersetzen=True, pruefer=True)
    return d


class Zusammenfuehren(unittest.TestCase):
    def test_quellen_werden_ueber_url_zusammengefuehrt(self):
        d = recherche()
        urls = [B.url_key(q["url"]) for q in d["quellen"]]
        self.assertEqual(len(urls), len(set(urls)))
        self.assertEqual([q["id"] for q in d["quellen"]], ["Q%d" % i for i in range(1, len(urls) + 1)])

    def test_quelle_muss_im_selben_teil_stehen(self):
        with self.assertRaises(B.Fehler):
            B.zusammenfuehren(recherche(), {"claims": [{"id": "T9", "aussage": "x", "quellen": ["Q1"]}]})

    def test_doppelte_claim_id_braucht_ersetzen(self):
        neu = {"quellen": [{"id": "Q9", "url": "https://x.example/neu", "titel": "neu", "typ": "medien"}],
               "claims": [{"id": "T1", "aussage": "geändert", "ursprung": "fakt", "stufe": "A", "quellen": ["Q9"]}]}
        with self.assertRaises(B.Fehler):
            B.zusammenfuehren(recherche(), neu)

    def test_portfolio_felder_einzeln(self):
        d, _ = B.zusammenfuehren(recherche(), {"inhalt": {"portfolio": {"felder": [{"name": "Neu", "angebote": []}], "luecken": ["x"]}}})
        self.assertEqual([f["name"] for f in d["inhalt"]["portfolio"]["felder"]], ["Wärmepumpen", "Service", "Neu"])

    def test_pruefer_modus_protokolliert_und_behaelt_pruefung(self):
        d = geprueft()
        arten = {(x["id"], x["art"]) for x in d["pruefung"]["aenderungen"]}
        self.assertIn(("P2", "korrigiert"), arten)
        self.assertIn(("P8", "ergaenzt"), arten)
        p8 = next(c for c in d["claims"] if c["id"] == "P8")
        self.assertEqual(p8["herkunft"], "vertiefung")
        alt = next(x for x in d["pruefung"]["aenderungen"] if x["id"] == "P2")
        self.assertIn("Serienfertigung", alt["alt"])
        self.assertIn("Pilotserie", alt["neu"])

    def test_ersteller_entfernt_veraltete_pruefung(self):
        d = geprueft()
        korrektur = {"quellen": [{"id": "Q1", "url": "https://www.example.com/gb-2025.pdf", "titel": "GB", "typ": "geschaeftsbericht"}],
                     "claims": [{"id": "T2", "aussage": "Rund 2.000 Mitarbeitende.", "ursprung": "fakt", "stufe": "A", "quellen": ["Q1"], "belegstelle": "S. 14"}]}
        d2, meldung = B.zusammenfuehren(d, korrektur, ersetzen=True)
        self.assertNotIn("pruefung", d2)
        self.assertIn("Prüfung entfernt", meldung)

    def test_entfernen_im_pruefer_modus(self):
        d = geprueft()
        d2, _ = B.zusammenfuehren(d, {"entfernen": ["T6"], "entfernen_grund": "nicht belegt",
                                      "inhalt": {"unternehmen": dict(d["inhalt"]["unternehmen"], profil=[
                                          dict(z, claims=[c for c in z["claims"] if c != "T6"]) for z in d["inhalt"]["unternehmen"]["profil"]])}}, pruefer=True)
        self.assertNotIn("T6", [c["id"] for c in d2["claims"]])
        self.assertTrue(any(x["id"] == "T6" and x["art"] == "entfernt" for x in d2["pruefung"]["aenderungen"]))
        d2["pruefung"]["claims"] = [u for u in d2["pruefung"]["claims"] if u["id"] != "T6"]
        self.assertEqual(B.validieren(d2)[0], [])


class Validierung(unittest.TestCase):
    def fehler(self, d):
        return B.validieren(d)[0]

    def test_beispiele_gueltig(self):
        self.assertEqual(self.fehler(recherche()), [])
        self.assertEqual(self.fehler(geprueft()), [])

    def test_mindestregel_und_ausnahme(self):
        d = recherche()
        d["inhalt"]["portfolio"]["felder"][0]["angebote"] = d["inhalt"]["portfolio"]["felder"][0]["angebote"][:1]
        d["interpretation"]["reife"] = [r for r in d["interpretation"]["reife"] if r["angebot"] != "HT-200"]
        self.assertTrue(any("portfolio.angebote_je_feld" in f for f in self.fehler(d)))
        d["inhalt"]["portfolio"]["ausnahmen"] = [{"regel": "portfolio.angebote_je_feld", "grund": "Das Geschäftsfeld umfasst laut Geschäftsbericht nur ein Produkt."}]
        self.assertEqual(self.fehler(d), [])

    def test_kurze_ausnahme_und_unbekannte_regel(self):
        d = recherche()
        d["inhalt"]["portfolio"]["ausnahmen"] = [{"regel": "portfolio.medien", "grund": "nichts"}, {"regel": "egal", "grund": "x" * 50}]
        f = self.fehler(d)
        self.assertTrue(any("konkreten Grund" in x for x in f))
        self.assertTrue(any("unbekannte Regel" in x for x in f))

    def test_b_zeile_status_quellentyp(self):
        d = recherche()
        d["inhalt"]["portfolio"]["felder"][1]["angebote"][0]["claims"] = ["P4"]
        d["inhalt"]["portfolio"]["felder"][0]["angebote"][0]["status_stufe"] = "aktuelles Portfolio"
        d["quellen"][0].pop("typ")
        f = self.fehler(d)
        self.assertTrue(any("nur auf B-Claims" in x for x in f))
        self.assertTrue(any("status_stufe" in x for x in f))
        self.assertTrue(any("typ muss" in x for x in f))

    def test_netzwerk_regeln(self):
        d = recherche()
        b = d["inhalt"]["cluster"]["beziehungen"]
        b[0]["datum"] = "laufend"
        b[1]["typ"] = "Freundschaft"
        b[2]["produkte"] = ["Gibt es nicht"]
        f = self.fehler(d)
        self.assertTrue(any("JJJJ-MM" in x for x in f))
        self.assertTrue(any("typ muss" in x and "Beziehung" in x for x in f))
        self.assertTrue(any("kein Angebot" in x for x in f))

    def test_matrix_regeln(self):
        d = recherche()
        z = d["inhalt"]["markt"]["vergleich"]["zeilen"]
        z[0]["zellen"]["temp"]["wert"] = "150"
        z[1]["zellen"]["einsatz"]["stufe"] = 9
        f = self.fehler(d)
        self.assertTrue(any("Zahlenwert" in x for x in f))
        self.assertTrue(any("definierten Stufen" in x for x in f))

    def test_praesenz_und_jv_kontrolle(self):
        d = recherche()
        akt = d["inhalt"]["markt"]["praesenz"][0]["aktivitaeten"][0]
        akt.update(betreiber="jv", kontrolle="gemeinsam")
        self.assertTrue(any("kontrollbeleg" in x for x in self.fehler(d)))
        akt["funktion"] = "Lager"
        self.assertTrue(any("funktion" in x for x in self.fehler(d)))

    def test_fokus_regeln(self):
        d = recherche()
        f = d["inhalt"]["fokus"][0]
        f["kennzahlen"][0]["wert"] = "1.200"
        f["fragen"] = ["nur Text"]
        f["ausnahmen"] = []
        fehler = self.fehler(d)
        self.assertTrue(any("Zahlenwert" in x for x in fehler))
        self.assertTrue(any("fragen müssen Objekte" in x for x in fehler))
        self.assertTrue(any("fokus.kennzahlen" in x for x in fehler))

    def test_reife_und_praesenzstufen(self):
        d = recherche()
        d["interpretation"]["reife"][0]["angebot"] = "Unbekannt"
        d["interpretation"]["praesenz"][0]["stufe"] = 7
        f = self.fehler(d)
        self.assertTrue(any("kein Angebot im Portfolio" in x for x in f))
        self.assertTrue(any("1 bis 5" in x for x in f))


class Auswertung(unittest.TestCase):
    def test_beispiel_unvollstaendig_wegen_nicht_erreichbarer_quelle(self):
        d = geprueft()
        ergebnis, aus = B.auswerten(d)
        self.assertEqual(ergebnis, "unvollstaendig")
        self.assertEqual(aus["offen"], ["H1"])
        self.assertEqual(aus["korrigiert"], ["P2"])
        self.assertEqual(aus["aus_vertiefung"], ["P8"])

    def test_abweichend_laesst_scheitern(self):
        d = geprueft()
        for u in d["pruefung"]["claims"]:
            if u["id"] == "M2":
                u["urteil"] = "abweichend"
        self.assertEqual(B.auswerten(d)[0], "nicht_bestanden")

    def test_bestanden_wenn_alles_im_original(self):
        d = geprueft()
        d["pruefung"]["claims"] = [{"id": c["id"], "urteil": "im_original_bestaetigt"} for c in d["claims"]]
        d["pruefung"]["ableitungen"] = [{"id": i["id"], "urteil": "gestuetzt"} for i in B.interpretationen(d)]
        self.assertEqual(B.auswerten(d)[0], "bestanden")

    @unittest.skipUnless(importlib.util.find_spec("openpyxl"), "openpyxl nicht installiert")
    def test_excel_rundreise(self):
        d = geprueft()
        with tempfile.TemporaryDirectory() as t:
            pfad = os.path.join(t, "d.xlsx")
            B.excel(d, pfad)
            self.assertEqual(B.einlesen(pfad), d)


class Html(unittest.TestCase):
    def test_alle_bausteine_und_reiter(self):
        s = H.rendern(recherche())
        for anker in ("executive-summary", "current-developments", "company-overview", "briefing-portfolio", "briefing-company-network",
                      "briefing-regional-presence", "briefing-capability-matrix", "page-profile", "page-focus-waermepumpen", "page-sources", "abnahme"):
            self.assertIn('id="%s"' % anker, s, anker)
        self.assertIn("Ungeprüfte Faktenbasis", s)
        self.assertNotIn('id="pruefbericht"', s)
        self.assertIsNone(re.search(r"__[A-Z_]+__", s), "Platzhalter der Vorlage nicht ersetzt")

    def test_netzwerkdaten_vollstaendig(self):
        s = H.rendern(recherche())
        roh = re.search(r'<script type="application/json" class="cn-data">(.*?)</script>', s, re.S).group(1)
        netz = json.loads(roh)
        self.assertEqual(netz["target_id"], "target")
        self.assertEqual(len(netz["edges"]), 3)
        arten = {n["label"]: n["kind"] for n in netz["nodes"]}
        self.assertEqual(arten["Muster Holding AG"], "owner")
        self.assertEqual(arten["Beispiel Kälte AG"], "jv")
        self.assertEqual(arten["Musterwerk"], "target")

    def test_geprueft_zeigt_bericht_aenderungen_und_urteile(self):
        s = H.rendern(geprueft())
        self.assertIn('id="pruefbericht"', s)
        self.assertIn("Änderungsprotokoll", s)
        self.assertIn("Prüfung unvollständig", s)
        self.assertIn('class="claim pv-ok" href="#P2"', s)
        self.assertIn("neu aus der Vertiefung", s)

    def test_datenblock_rundreise_und_escaping(self):
        d = recherche()
        d["claims"][0]["aussage"] = "Böse </script><script>alert(1)</script> & Co"
        s = H.rendern(d)
        self.assertNotIn("<script>alert(1)</script>", s)
        self.assertEqual(B.extrahieren(s), d)

    def test_kein_html_bei_fehlern(self):
        d = recherche()
        d["auftrag"]["stichtag"] = "gestern"
        with self.assertRaises(H.B.Fehler):
            H.rendern(d)

    def test_modulauftrag_nur_portfolio(self):
        d = recherche(bis="03")
        d["auftrag"].update(modus="modul", module=["portfolio"], personen=[], fokus=[])
        d["inhalt"].pop("personen")
        d["inhalt"].pop("unternehmen")
        d["claims"] = [c for c in d["claims"] if c["id"].startswith("P")]
        s = H.rendern(d)
        self.assertIn("Modulauftrag: Portfolio", s)
        self.assertIn('id="briefing-portfolio"', s)
        self.assertNotIn('id="executive-summary"', s)
        self.assertNotIn('id="page-profile"', s)

    def test_kommandozeile_mit_excel_oder_json(self):
        d = geprueft()
        with tempfile.TemporaryDirectory() as t, contextlib.redirect_stdout(io.StringIO()):
            pfad = os.path.join(t, "d.json")
            B.speichere(pfad, d)
            self.assertEqual(H.main(["--daten", pfad, "--out", os.path.join(t, "b.html")]), 0)
            self.assertEqual(B.main(["validieren", "--daten", pfad]), 0)


if __name__ == "__main__":
    unittest.main()
