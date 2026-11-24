"""Tests für skills/briefing-ausgabe/scripts/briefing.py mit den fiktiven Beispielteilen."""
import contextlib, copy, glob, importlib.util, io, json, os, tempfile, unittest

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKRIPT = os.path.join(BASIS, "skills", "briefing-ausgabe", "scripts", "briefing.py")
spec = importlib.util.spec_from_file_location("briefing", SKRIPT)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def teil(nr):
    pfad = glob.glob(os.path.join(BASIS, "beispiel", "%s-*.json" % nr))[0]
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def briefing(bis="07"):
    daten = None
    for nr in ("01", "02", "03", "04", "05", "06", "07"):
        daten, _ = b.zusammenfuehren(daten, teil(nr))
        if nr == bis:
            break
    return daten


class Zusammenfuehren(unittest.TestCase):
    def test_quellen_mit_gleicher_url_werden_zusammengefuehrt(self):
        d = briefing()
        urls = [b.url_key(q["url"]) for q in d["quellen"]]
        self.assertEqual(len(urls), len(set(urls)))
        gb = [q for q in d["quellen"] if q["url"].endswith("gb-2025.pdf")]
        self.assertEqual(len(gb), 1)
        p2 = next(c for c in d["claims"] if c["id"] == "P2")
        self.assertEqual(p2["quellen"], [gb[0]["id"]])

    def test_neue_quellen_werden_fortlaufend_nummeriert(self):
        ids = [q["id"] for q in briefing()["quellen"]]
        self.assertEqual(ids, ["Q%d" % i for i in range(1, len(ids) + 1)])

    def test_doppelte_claim_id_braucht_ersetzen(self):
        d = briefing()
        neu = {"quellen": [{"id": "Q9", "url": "https://x.example/neu", "titel": "neu"}],
               "claims": [{"id": "T1", "aussage": "geändert", "ursprung": "fakt", "stufe": "A", "quellen": ["Q9"]}]}
        with self.assertRaises(b.Fehler):
            b.zusammenfuehren(copy.deepcopy(d), neu)
        d2, _ = b.zusammenfuehren(copy.deepcopy(d), neu, ersetzen=True)
        self.assertEqual(next(c for c in d2["claims"] if c["id"] == "T1")["aussage"], "geändert")

    def test_quelle_muss_im_selben_teil_stehen(self):
        with self.assertRaises(b.Fehler):
            b.zusammenfuehren(briefing(), {"claims": [{"id": "T9", "aussage": "x", "quellen": ["Q1"]}]})

    def test_erster_teil_braucht_auftrag(self):
        with self.assertRaises(b.Fehler):
            b.zusammenfuehren(None, teil("02"))

    def test_fokus_wird_nach_id_ersetzt(self):
        d = briefing()
        neu = copy.deepcopy(teil("06"))
        neu["inhalt"]["fokus"][0]["fragen"] = ["Neue Frage?"]
        d2, _ = b.zusammenfuehren(d, {"inhalt": neu["inhalt"]})
        self.assertEqual(len(d2["inhalt"]["fokus"]), 1)
        self.assertEqual(d2["inhalt"]["fokus"][0]["fragen"], ["Neue Frage?"])


class Validierung(unittest.TestCase):
    def test_beispiel_ist_gueltig(self):
        fehler, _ = b.validieren(briefing())
        self.assertEqual(fehler, [])

    def test_unbekannter_claim_im_inhalt(self):
        d = briefing()
        d["inhalt"]["portfolio"]["felder"][0]["angebote"][0]["claims"].append("P99")
        fehler, _ = b.validieren(d)
        self.assertTrue(any("P99" in f for f in fehler))

    def test_falsches_praefix_und_fehlende_quelle(self):
        d = briefing()
        d["claims"].append({"id": "X1", "aussage": "x", "ursprung": "fakt", "stufe": "A", "quellen": []})
        fehler, _ = b.validieren(d)
        self.assertTrue(any("X1" in f and "passt nicht" in f for f in fehler))
        self.assertTrue(any("X1 ohne Quelle" in f for f in fehler))

    def test_zu_viele_swot_punkte(self):
        d = briefing()
        d["interpretation"]["swot"]["staerken"] = [dict(id="S%d" % i, titel="t", aussage="a", basis=["T1"]) for i in range(10, 14)]
        fehler, _ = b.validieren(d)
        self.assertTrue(any("höchstens drei" in f for f in fehler))

    def test_hinweis_auf_nicht_geoeffnete_quelle_und_alte_timeline(self):
        d = briefing()
        d["inhalt"]["unternehmen"]["timeline"].append({"datum": "2025-01-01", "ereignis": "alt", "claims": ["T1"]})
        _, hinweise = b.validieren(d)
        self.assertTrue(any("nicht geöffnete Quelle" in h for h in hinweise))
        self.assertTrue(any("Viermonatsfenster" in h for h in hinweise))

    def test_unsichere_url_ist_fehler(self):
        d = briefing()
        d["quellen"][0]["url"] = "javascript:alert(1)"
        fehler, _ = b.validieren(d)
        self.assertTrue(any("http" in f for f in fehler))


class Mindestregeln(unittest.TestCase):
    def fehler(self, d):
        return b.validieren(d)[0]

    def test_division_als_einziges_angebot_ist_fehler(self):
        d = briefing()
        d["inhalt"]["portfolio"]["felder"][0]["angebote"] = d["inhalt"]["portfolio"]["felder"][0]["angebote"][:1]
        self.assertTrue(any("portfolio.angebote_je_feld" in f for f in self.fehler(d)))

    def test_begruendete_ausnahme_hebt_fehler_auf(self):
        d = briefing()
        d["inhalt"]["portfolio"]["felder"][0]["angebote"] = d["inhalt"]["portfolio"]["felder"][0]["angebote"][:1]
        d["inhalt"]["portfolio"]["ausnahmen"] = [{"regel": "portfolio.angebote_je_feld",
            "grund": "Das Geschäftsfeld umfasst laut Geschäftsbericht und Produktseite nur ein einziges Produkt."}]
        self.assertEqual(self.fehler(d), [])
        self.assertIn("Ausnahme von der Mindestregel", b.rendern(d))

    def test_ausnahme_ohne_konkreten_grund_ist_fehler(self):
        d = briefing()
        d["inhalt"]["portfolio"]["ausnahmen"] = [{"regel": "portfolio.medien", "grund": "nichts gefunden"}]
        self.assertTrue(any("konkreten Grund" in f for f in self.fehler(d)))

    def test_unbekannte_regel_ist_fehler(self):
        d = briefing()
        d["inhalt"]["portfolio"]["ausnahmen"] = [{"regel": "portfolio.egal", "grund": "x" * 50}]
        self.assertTrue(any("unbekannte Regel" in f for f in self.fehler(d)))

    def test_fehlender_geschaeftsbericht_und_medien(self):
        d = briefing()
        for q in d["quellen"]:
            if q["typ"] in ("geschaeftsbericht", "medien", "fachmedien"):
                q["typ"] = "produktseite"
        f = self.fehler(d)
        for regel in ("portfolio.geschaeftsbericht", "portfolio.medien", "cluster.medien", "unternehmen.medien"):
            self.assertTrue(any(regel in x for x in f), regel)

    def test_status_stufe_pflicht_und_liste(self):
        d = briefing()
        d["inhalt"]["portfolio"]["felder"][0]["angebote"][0]["status_stufe"] = "aktuelles Portfolio"
        self.assertTrue(any("status_stufe" in f for f in self.fehler(d)))

    def test_zu_viele_angebote_ohne_status(self):
        d = briefing()
        for f in d["inhalt"]["portfolio"]["felder"]:
            for a in f["angebote"]:
                a["status_stufe"] = "nicht_belegt"
        self.assertTrue(any("portfolio.status" in f for f in self.fehler(d)))

    def test_zeile_nur_mit_b_claims_ist_fehler(self):
        d = briefing()
        d["inhalt"]["portfolio"]["felder"][1]["angebote"][0]["claims"] = ["P4"]
        self.assertTrue(any("nur auf B-Claims" in f for f in self.fehler(d)))

    def test_quellentyp_pflicht(self):
        d = briefing()
        d["quellen"][0].pop("typ")
        self.assertTrue(any("typ muss" in f for f in self.fehler(d)))

    def test_cluster_und_markt_mindestumfang(self):
        d = briefing()
        d["inhalt"]["cluster"]["beziehungen"] = d["inhalt"]["cluster"]["beziehungen"][:2]
        d["inhalt"]["markt"]["vergleich"]["zeilen"] = d["inhalt"]["markt"]["vergleich"]["zeilen"][:2]
        f = self.fehler(d)
        self.assertTrue(any("cluster.beziehungen" in x for x in f))
        self.assertTrue(any("markt.vergleich" in x for x in f))

    def test_ungueltige_beziehung_und_praesenz(self):
        d = briefing()
        d["inhalt"]["cluster"]["beziehungen"][0]["typ"] = "Freundschaft"
        d["inhalt"]["markt"]["praesenz"][0]["aktivitaeten"][0]["status"] = "operativ laut Medien"
        f = self.fehler(d)
        self.assertTrue(any("Beziehung" in x and "typ muss" in x for x in f))
        self.assertTrue(any("Präsenz" in x for x in f))

    def test_fokus_mindestumfang_und_beispielausnahme(self):
        d = briefing()
        self.assertEqual(self.fehler(d), [])
        d["inhalt"]["fokus"][0]["ausnahmen"] = []
        self.assertTrue(any("fokus.kennzahlen" in x for x in self.fehler(d)))

    def test_portfolio_felder_werden_einzeln_ergaenzt(self):
        d = briefing()
        neu = {"inhalt": {"portfolio": {"felder": [{"name": "Neues Feld", "angebote": []}], "luecken": ["neu"]}}}
        d2, _ = b.zusammenfuehren(d, neu)
        namen = [f["name"] for f in d2["inhalt"]["portfolio"]["felder"]]
        self.assertEqual(namen, ["Wärmepumpen", "Service", "Neues Feld"])
        self.assertIn("neu", d2["inhalt"]["portfolio"]["luecken"])

    def test_kopf_zeigt_modulauftrag(self):
        d = briefing(bis="03")
        d["auftrag"]["modus"] = "modul"
        d["auftrag"]["module"] = ["portfolio"]
        self.assertIn("Modulauftrag: Portfolio", b.rendern(d))


class Rendern(unittest.TestCase):
    def test_ungeprueft_enthaelt_hinweis_und_kapitel(self):
        html = b.rendern(briefing())
        self.assertIn("Ungeprüfte Faktenbasis", html)
        for anker in ("summary", "unternehmen", "portfolio", "cluster", "markt", "positionierung", "swot",
                      "person-1", "fokus-waermepumpen", "belege", "quellen", "abnahme"):
            self.assertIn('id="%s"' % anker, html)
        self.assertNotIn('id="pruefbericht"', html)

    def test_text_wird_escaped_und_datenblock_bleibt_intakt(self):
        d = briefing()
        d["claims"][0]["aussage"] = "Böse </script><script>alert(1)</script> & Co"
        html = b.rendern(d)
        self.assertNotIn("<script>alert(1)</script>", html)
        self.assertEqual(html.count("</script>"), 1)
        self.assertEqual(b.extrahieren(html), d)

    def test_rundreise_ohne_verlust(self):
        d = briefing()
        self.assertEqual(b.extrahieren(b.rendern(d)), d)

    def test_fehlerhafte_daten_werden_nicht_gerendert(self):
        d = briefing()
        d["auftrag"]["stichtag"] = "gestern"
        with self.assertRaises(b.Fehler):
            b.rendern(d)

    def test_modul_ohne_interpretation(self):
        d = briefing(bis="03")
        d["auftrag"]["modus"] = "modul"
        html = b.rendern(d)
        self.assertIn('id="portfolio"', html)
        self.assertNotIn('id="swot"', html)
        self.assertNotIn('id="summary"', html)


class Pruefung(unittest.TestCase):
    def geprueft(self):
        d, _ = b.zusammenfuehren(briefing(), teil("08"))
        return d

    def test_abweichender_a_claim_laesst_pruefung_scheitern(self):
        d = self.geprueft()
        ergebnis, aus = b.auswerten(d)
        self.assertEqual(ergebnis, "nicht_bestanden")
        self.assertIn("P2", aus["nicht_bestanden_wegen"])
        self.assertEqual(aus["betroffene_ableitungen"], ["I8", "I9"])
        self.assertIn("H1", aus["offen"])

    def test_ohne_fehler_aber_mit_offenem_a_claim_unvollstaendig(self):
        d = self.geprueft()
        for u in d["pruefung"]["claims"]:
            if u["id"] == "P2":
                u["urteil"] = "im_original_bestaetigt"
        for u in d["pruefung"]["ableitungen"]:
            u["urteil"] = "gestuetzt"
        self.assertEqual(b.auswerten(d)[0], "unvollstaendig")

    def test_alles_im_original_bestaetigt(self):
        d = self.geprueft()
        d["pruefung"]["claims"] = [{"id": c["id"], "urteil": "im_original_bestaetigt"} for c in d["claims"]]
        d["pruefung"]["ableitungen"] = [{"id": i["id"], "urteil": "gestuetzt"} for i in b.interpretationen(d)]
        self.assertEqual(b.auswerten(d)[0], "bestanden")

    def test_teilpruefung_ist_hoechstens_mit_einschraenkungen(self):
        d = self.geprueft()
        d["pruefung"]["umfang"] = {"kapitel": ["portfolio"], "nur_a": True}
        d["pruefung"]["claims"] = [{"id": c["id"], "urteil": "im_original_bestaetigt"} for c in d["claims"]
                                   if c["id"].startswith("P") and c["stufe"] == "A"]
        d["pruefung"]["ableitungen"] = []
        self.assertEqual(b.auswerten(d)[0], "bestanden_mit_einschraenkungen")

    def test_geprueftes_html_zeigt_bericht_und_urteile(self):
        d = self.geprueft()
        b.auswerten(d)
        html = b.rendern(d)
        self.assertIn('id="pruefbericht"', html)
        self.assertIn("Prüfung nicht bestanden", html)
        self.assertIn('class="chip bad"', html)
        self.assertIn("Status auf &#x27;Pilotserie laut Hersteller&#x27; ändern.", html)


class PruefungZusammenfuehren(unittest.TestCase):
    def test_pruefung_wird_in_runden_ergaenzt(self):
        d = briefing()
        d, _ = b.zusammenfuehren(d, {"pruefung": {"stand": "2026-11-21", "claims": [{"id": "T1", "urteil": "abweichend"}]}})
        d, _ = b.zusammenfuehren(d, {"pruefung": {"claims": [{"id": "T1", "urteil": "im_original_bestaetigt"}, {"id": "P1", "urteil": "nicht_belegt"}]}})
        urteile = {u["id"]: u["urteil"] for u in d["pruefung"]["claims"]}
        self.assertEqual(urteile, {"T1": "im_original_bestaetigt", "P1": "nicht_belegt"})
        self.assertEqual(d["pruefung"]["stand"], "2026-11-21")

    def test_geaenderte_fakten_entfernen_veraltete_pruefung(self):
        d, _ = b.zusammenfuehren(briefing(), teil("08"))
        korrektur = {"quellen": [{"id": "Q1", "url": "https://www.example.com/gb-2025.pdf", "titel": "GB"}],
                     "claims": [{"id": "P2", "aussage": "Pilotserie laut Hersteller.", "ursprung": "hersteller", "stufe": "A", "quellen": ["Q1"], "belegstelle": "S. 22"}]}
        d2, meldung = b.zusammenfuehren(d, korrektur, ersetzen=True)
        self.assertNotIn("pruefung", d2)
        self.assertIn("Prüfung entfernt", meldung)

    def test_pruefung_null_entfernt_pruefung(self):
        d, _ = b.zusammenfuehren(briefing(), teil("08"))
        d2, _ = b.zusammenfuehren(d, {"pruefung": None})
        self.assertNotIn("pruefung", d2)


class Kommandozeile(unittest.TestCase):
    def test_ablauf_ueber_befehle(self):
        with tempfile.TemporaryDirectory() as t, contextlib.redirect_stdout(io.StringIO()):
            daten = os.path.join(t, "d.json")
            for nr in ("01", "02", "03", "04", "05", "06", "07"):
                pfad = glob.glob(os.path.join(BASIS, "beispiel", "%s-*.json" % nr))[0]
                self.assertEqual(b.main(["zusammenfuehren", "--daten", daten, "--teil", pfad]), 0)
            self.assertEqual(b.main(["validieren", "--daten", daten]), 0)
            out = os.path.join(t, "briefing.html")
            self.assertEqual(b.main(["rendern", "--daten", daten, "--out", out]), 0)
            zurueck = os.path.join(t, "x.json")
            self.assertEqual(b.main(["extrahieren", "--html", out, "--out", zurueck]), 0)
            with open(daten, encoding="utf-8") as f1, open(zurueck, encoding="utf-8") as f2:
                self.assertEqual(json.load(f1), json.load(f2))

    @unittest.skipUnless(importlib.util.find_spec("openpyxl"), "openpyxl nicht installiert")
    def test_excel_rundreise(self):
        d = briefing()
        with tempfile.TemporaryDirectory() as t:
            pfad = os.path.join(t, "d.xlsx")
            b.excel(d, pfad)
            self.assertEqual(b.aus_excel(pfad), d)


if __name__ == "__main__":
    unittest.main()
