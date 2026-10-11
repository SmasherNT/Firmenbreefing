# Review

```json
{
  "schema_version": 1,
  "run_id": "2026-10-10-rheinmetall",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-10",
  "phase": "basis",
  "status": "freigegeben",
  "status_begruendung": "Runde 2: Alle 6 wesentlichen Fehler aus R1 (ME-1 bis ME-6) und die nicht wesentlichen Korrekturen sind behoben; alle 20 geänderten und 2 neuen Claims sowie die geänderten Kanten (E18, E19, E34, E46, E47) und module_views gezielt geprüft. Alle 172 Claims geprüft bzw. unverändert übernommen; keine offenen A-Claims. Verbleibende Punkte sind nicht blockierende Hinweise und transparente Datenlücken.",
  "reviewer": "source-reviewer (Phase basis, mode=facts-v2)",
  "pruefumfang": {
    "eingaben": [
      "runs/2026-10-10-rheinmetall/input/auftrag.md",
      "runs/2026-10-10-rheinmetall/input/facts-run.json",
      "work/review-packet.json (170 Claims, 139 Quellen, network 37 Knoten/46 Kanten, module_views)",
      "work/facts-validation.json (required_full_review_ids: 31)",
      "work/comparison-plan.json",
      "Abdeckung/gaps/report_log gezielt aus work/cluster-facts.json"
    ],
    "formale_kontrolle": "python3 scripts/check-review-data.py work/review-packet.json -> Exit 0, errors [], 170 Fingerprints (nur formal; kein Inhaltsurteil).",
    "inhaltspruefung": "Alle 31 Netzwerk-Pflicht-Claims (required_full_review_ids) sowie alle 46 Kanten (Identität, Richtung, Typ, Status/Zeitraum, Produktbezug, Quote/Kontrolle) gegen Originalbelege geprüft. Alle A-Claims (130 nach Hochstufung) im geöffneten Originaldokument bzw. redaktionellen Artikel geprüft; PDFs (GB 2025/2024, H1-Bericht/-PM, FY-PM, Transkripte FY2025/Q1-2026, Präsentationen, Diehl-/HENSOLDT-GB, CRS, SIPRI, SECO, EOS-ASX, Revolver-Gun-Broschüre) lokal heruntergeladen und per Textextraktion an den angegebenen Seiten geprüft.",
    "hochstufungen_nach_A": "C-STR-02, C-STR-08 (Netzwerkkanten); M-QAT-RHM-03, M-SAU-RHM-02, M-RHM-CAP-01, M-PEER-EOS-02, M-PEER-EOS-03, M-PEER-MICA-01, M-QAT-PROG-01 (tragen Marktbeobachtungen); T-CTX-03, T-CTX-09 (Kennzahlen laut Auftrag); T-CTX-26, C-GCC-04, C-GCC-09, C-GCC-12, C-EX-03, P-SKX-04 (Golf-Schwerpunkt).",
    "nicht_einzeln_gepruefte_claims": [],
    "zugriffsgrenzen": [
      "Army Technology (S-c6b8e3a389de878f): HTTP 403 – P-SKN-01 über inhaltsgleiche Quellen geprüft",
      "Teknisk Ukeblad (S-1e47bb01c749039c): nur frei sichtbarer Teil – AMRAAM-ER-Detail in M-QAT-PROG-02 offen",
      "Stern-Original (P-SKX-08) und Bloomberg 08.05.2026 (M-RHM-GULF-02) wie von den Analysten angegeben nicht geöffnet",
      "militaeraktuell.at (zusätzlicher Sekundärbericht zum Führungswechsel, nicht im Paket): HTTP 403"
    ],
    "runde_2": {
      "eingaben": "work/review-packet.json (172 Claims, 136 Quellen, 38 Knoten/47 Kanten), work/facts-validation.json (32 required_full_review_ids, errors []), Vergleich gegen work/facts-validation-r1.json",
      "geaenderte_claims": [
        "C-EX-01",
        "C-GCC-07",
        "C-GCC-08",
        "C-GCC-09",
        "C-STR-05",
        "C-STR-08",
        "H-KOE-01",
        "M-DEU-EXPORT-02",
        "M-QAT-BARZAN-01",
        "M-QAT-PROG-02",
        "M-RHM-GULF-02",
        "M-UAE-ACCESS-01",
        "M-UAE-EDGE-02",
        "P-RG-02",
        "P-SKN-01",
        "P-SKX-02",
        "P-SKX-06",
        "P-SR30-08",
        "P-SR30-09",
        "T-CTX-21"
      ],
      "neue_claims": [
        "C-GCC-14",
        "H-DUE-05"
      ],
      "methode": "Fingerprint-Diff R1/R2; nur geänderte/neue Claims, deren neue Quellen (S-05ec117bf73653de, S-09155eae505dd047, S-51a58a4ed460b294 geöffnet) sowie betroffene Kanten und Views geprüft; unveränderte Claims mit identischem Fingerprint als \"übernommen\" (gleicher Auftrag/Stichtag).",
      "formale_kontrolle": "facts-validation.json errors [] (vom Hauptagenten erzeugt); kein Inhaltsurteil."
    }
  },
  "material_errors": [],
  "weitere_korrekturen_nicht_wesentlich": [],
  "konsistenzpruefung_schwerpunkte": {
    "H-KOE_Koehne": "Identität konsistent (Rheinmetall-PMs 05.01./17.06./18.06.2026 als Leiter/CEO Weapon and Ammunition; RWM-Geschäftsführer 2020). Neue Rolle CEO Division Air Defence ab 01.10.2026 nur sekundär (esut 04.09.2026 'nach unternehmensinternen Informationen'; Inside Paradeplatz ohne Namen; zusätzlich militaeraktuell.at, nicht zugänglich). Keine Rheinmetall-Primärquelle und kein Zefix-Eintrag gefunden (Divisions-/Tochterseiten nennen keine Leitung). Zeitlich konsistent: PM 15.06.2026 'CEO Rheinmetall Division Air Defence' Dürr, PM 24.06.2026 'Head of Rheinmetall's Air Defence Division' Dürr – beide vor dem 01.10.2026; NZZ 10.10.2026 bestätigt Dürrs Abgang. H-KOE-01 geprüft als 'angekündigt laut Fachmedium'; im Briefing zwingend als nicht primär bestätigt kennzeichnen (offene Datenlücke, kein Fehler).",
    "H-DUE_H-PAP_H-GAN": "Zefix/SHAB und Vorstandsseite bestätigen Dürr (RAD AG seit 2021), Papperger (Präsident VR seit SHAB 18.07.2024), Gansauge (VR 01/2026, Vizepräsident 07/2026). Dürr-Abgang strittig dargestellt (H-DUE-03 Selbstdarstellung vs. H-DUE-04 anonyme Quellen) – beide korrekt attribuiert.",
    "Kennzahlen_T-CTX": "T-CTX-01..03 und 08..11 in FY-PM, H1-PM, H1-Bericht (S. 8, 17, 22, 30, 38) und Sept.-Präsentation bestätigt.",
    "P-SKX-07_vs_P-SKX-08": "Kein Fehler: Herstellerangabe (Bewährung in Ukraine) und berichtete interne ukrainische Bewertung (via Stern/Defense Express) sind getrennt attribuiert. Nicht auflösen; Matrix/SWOT dürfen keinen der beiden als gesicherte Leistungsaussage nutzen.",
    "AGG_48": "Kein Widerspruch: Erstfassung bis 15.09.2026 (BAFA-Kurzmeldung, Handelsblatt), Verlängerung per Bekanntgabe 10.09.2026 bis 15.09.2027 (BAFA-Übersicht primär, AWA sekundär). Siehe Korrektur C-EX-01; M-DEU-EXPORT-02 sollte BAFA-Übersicht als Primärbeleg aufnehmen.",
    "RADARABIA_Flaeche": "Echter Quellenwiderspruch: 25.000 m² (Aviation Week mit RADARABIA-Chairman-Zitat; Argaam) vs. 25,000 sq ft (Janes). In C-GCC-02 korrekt offen; M-SAU-RHM-01 nennt nur 25.000 m² und sollte auf den Widerspruch verweisen (Hinweis an market, nicht blockierend).",
    "M-GCC-TUR-01": "Korrekt als nur durch zwei anonyme türkische Branchenquellen berichtet gekennzeichnet; Kuwait-Protokoll als berichtete Ministerunterzeichnung. Darf nicht als belegter Korkut-Vertrag in Matrix/SWOT verwendet werden; Marktbeobachtung formuliert das korrekt.",
    "Ueberschneidung_M-RHM_P": "M-RHM-CUAS-01 konsistent mit P-SKX-07 (Gegenbefund P-SKX-08 separat). M-RHM-CAP-01 und P-SR30-08 sind dasselbe Euronews-Interview unter zwei Quellen-IDs (S-aaaf59c399a65ff2/S-5201e1820b86a0c3) – kein Zweitbeleg; Kapazitätsangaben konsistent mit P-CAP-01. M-RHM-ORDER-01 ist Wiedergabe der PM 02.07.2026 (P-SKX-11/C-GCC-13/T-CTX-24), konsistent.",
    "Quellen-Duplikate": "Gleiche Dokumente unter mehreren Quellen-IDs (keine unabhängigen Zweitbelege): Janes 14.10.2022 (S-6cd5701123f00a73/S-18fa7e4158bdc58b), Janes 15.12.2022 (S-3b004b2cc914ddc4/S-f71c0348db6067c4), Janes 01.11.2019 (S-e1e08a6e0206896f/S-eb780da12d4e3349), Gulf News 23.02.2021 (S-9d63edda09166afa/S-e59dc842147cf65f), Army Recognition 17.11.2025 (S-0bc97ad481ad67e4/S-f06315f4acc363fb), Euronews 17.09.2026 (S-aaaf59c399a65ff2/S-5201e1820b86a0c3). Registry bereinigen (Hauptagent/zuständige Rollen).",
    "SkyKnight_Status": "Janes 02/2025 'Qualifikation Ende 2026' (C-TI-05, M-UAE-EDGE-02) ist durch HALCON 11/2025 'late 2027' (P-SKN-03) und EDGE-CEO 05/2026 'not in service, going into production' (M-UAE-EDGE-03) überholt; Claims korrekt datiert, aber Beobachtung/Kante müssen den neueren Stand zeigen."
  },
  "netzwerk_pruefung": {
    "metadaten": "company 'Rheinmetall AG', as_of 2026-10-10, target_id 'rheinmetall' passen zum Auftrag; kein alter Firmendatensatz erkennbar (alle Quellen am 10.10.2026 abgerufen, Kanten-IDs/Claims laufbezogen).",
    "kanten_geprueft": 47,
    "kanten_mit_fehler": [],
    "hinweise_nicht_blockierend": [
      "E27 HALCON→RAD: Status um 'Qualifikation laut HALCON late 2027 erwartet (11/2025)' ergänzen (P-SKN-03).",
      "E14 Rheinmetall→RSADF: Kundenbeziehung beruht auf allgemeiner Herstelleraussage 'Kingdom' plus Janes-Betreiberhinweis; Unsicherheit korrekt angegeben.",
      "E11 RAD→RADARABIA: Gründung durch RAD laut Aviation Week; über welche Gesellschaft die 20 % (indirekt) gehalten werden, ist im GB nicht ausgewiesen – keine Kapitalquote an E11 hängen (derzeit korrekt)."
    ],
    "richtung_identitaet": "Alle übrigen Kanten: Akteursidentitäten, Richtung (Lieferant→Kunde, Eigentümer→Beteiligung), Kapitalanteil vs. Stimmrechte (E08: 49 % Kapital, Vollkonsolidierung wegen Stimmrechtsmehrheit; E10/E15 at-equity ohne JV-Fußnote), Historienflags (E29, E30, E43, E44, E45) und Produktzuordnungen (skynex, skyranger30/35, skyguard, skyknight, spexer, sadm, mass, millennium) gegen Belege bestätigt. Überschneidung E41 korrekt als overlap ohne bilateralen Vertrag.",
    "runde_2": "E19 (rh_electronics→rast, 100 % Kapital/Stimmrechte, vollkonsolidiert ab 07/2026, 40 % historisch), E46 (historisch 2018–04/2020), E47 neu (schwer→eos, overlap, Stand 24.08.2026, keine Kooperationsbehauptung), E34 (gdels→austria; Rheinmetall-Rolle über E33 Unterauftrag, keine direkte Vertragsbeziehung behauptet), E18 (Quellen-IDs vereinheitlicht) gegen Belege geprüft – korrekt. company/as_of/target_id unverändert passend. Knoten eos (Electro Optic Systems Holdings Ltd, Canberra) korrekt identifiziert."
  },
  "module_views_pruefung": {
    "context": "ev-bilanz-golf neu gelabelt (\"CEO-Aussagen (Earnings Call) ...\", 2026-03-11, T-CTX-21/22) – korrekt.",
    "portfolio": "Golfstaaten-Sections korrigiert: P-SKX-02 unter \"GCC übergreifend (... Auftrag 2019 mit ungenanntem Kunden)\", Katar-Section \"Zuordnung laut Janes bzw. Messebericht\" – Länderabgrenzung jetzt belegt. Übrige Views unverändert.",
    "cluster": "report_log GB 2024 korrigiert; Golf-Sektion \"Historische Bezüge und personelle Querverbindungen\" mit C-GCC-07/C-GCC-14 korrekt; RAST in Gesellschaftssektion mit aktuellem Status.",
    "market": "gulf_access und production_capacity (rheinmetall) auf Primärwortlaut umgestellt, Skyranger im GCC als nicht belegt; edge procurement_status zeigt late 2027 (HALCON) und \"going into production\" (CEO 05/2026) – korrekt. Hinweis claim_ids siehe hinweise_nicht_blockierend."
  },
  "stichproben_B": {
    "methode": "Gruppen nach Modul × Quelle × Aussageart gebildet; da die Quellen für A-Claims ohnehin geöffnet wurden, wurde die Stichprobe in allen Gruppen auf Vollprüfung ausgeweitet. Kein inhaltlicher Fehler in B-Claims gefunden; keine B-Claims als 'nicht einzeln geprüft' verblieben.",
    "gruppen": [
      {
        "gruppe": "context|Rheinmetall-Website/PM/Bericht|Struktur-/Ereignis-Hintergrund",
        "ids": [
          "T-CTX-07",
          "T-CTX-13",
          "T-CTX-20",
          "T-CTX-23"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "context|Zefix|Registerdaten",
        "ids": [
          "T-CTX-14"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "context|Rheinmetall-PM/Fachmedien|frühere Funktionen Köhne",
        "ids": [
          "H-KOE-04",
          "H-KOE-05",
          "H-KOE-06",
          "H-KOE-07"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "portfolio|Produktseiten/Broschüre|technische Herstellerangaben",
        "ids": [
          "P-SKX-01",
          "P-SKN-02",
          "P-RG-01",
          "P-MIL-01",
          "P-SR30-01"
        ],
        "geprueft": "alle (inkl. Zahlenangaben 25/35/50 km, 4.000 m, 252 Schuss, 1.000 Schuss/min, 3.000 m)"
      },
      {
        "gruppe": "portfolio|Rheinmetall-PM|ältere Aufträge ohne Kundennennung",
        "ids": [
          "P-SR30-07",
          "P-SG-02",
          "P-SG-03"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "portfolio|Fachmedien/Interview|Hintergrund",
        "ids": [
          "P-RG-02",
          "P-SG-04",
          "P-SR30-08"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "portfolio|Transkript Q1-2026|Ankündigungen",
        "ids": [
          "P-CUAS-02",
          "P-AMMO-01"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "market|Lagemedien|Bedrohungshintergrund",
        "ids": [
          "M-GCC-THREAT-03",
          "M-KWT-THREAT-01",
          "M-SAU-THREAT-01",
          "M-GCC-THREAT-05"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "market|SIPRI/Argaam|Budgetkennzahlen",
        "ids": [
          "M-KWT-BUDGET-01",
          "M-OMN-BUDGET-01",
          "M-UAE-BUDGET-01",
          "M-SAU-BUDGET-02"
        ],
        "geprueft": "alle"
      },
      {
        "gruppe": "market|Fachmedien/CRS|Programme Dritter",
        "ids": [
          "M-KWT-PROG-01",
          "M-SAU-PROG-01",
          "M-BHR-PROG-01",
          "M-RHM-ORDER-01"
        ],
        "geprueft": "alle"
      }
    ]
  },
  "quellenabrufgruppen": [
    "Rheinmetall-Geschäftsberichte 2025/2024 (Download, pdftotext; S. 15, 39, 65, 234, 240, 265, 268-271 bzw. 252-256): C-STR-01/03/04/05/06/07/08/09, C-TI-01/07, C-KD-04",
    "Rheinmetall H1-PM, H1-Bericht, FY2025-PM, Sept.-Präsentation: T-CTX-01..05/08..13/20/25",
    "Transkripte/Präsentationen FY2025 & Q1-2026: P-GCC-01..03, P-CAP-01, P-CUAS-02, P-AMMO-01, Abgleich M-RHM-GULF-01/02, T-CTX-21",
    "Rheinmetall-PMs/Produktseiten (19 Dokumente): P-*, C-KD-01..03, C-TI-09, C-GCC-11/13, H-KOE-02/04/06, H-DUE-01, T-CTX-23/24/26",
    "Zefix-JSON + Vorstandsseite: T-CTX-06/14, H-DUE-02, H-PAP-01/02, H-GAN-01",
    "Personen-Medien (esut, Inside Paradeplatz, NZZ 11.03./20.03./10.10.2026 per Direktabruf) + Primärquellensuche Köhne: H-KOE-01/03, H-DUE-03/04, T-CTX-22, C-KD-05, C-GCC-12",
    "Golf-Cluster-Medien (Janes ×5, Aviation Week, Argaam, Gulf Times ×2, Qatar Tribune, Defense News, PMG, Gulf News ×2, Arab News, SRF, Breaking Defense, EDR ×3): C-GCC-*, C-TI-05/06, M-QAT-RHM-*, M-SAU-RHM-*, M-UAE-EDGE-01/02, P-SKN-*",
    "Zusatzrecherche nur zur Klärung wesentlicher Punkte: Asharq Al-Awsat 25.04.2020 (SAMI-CEO-Wechsel), EOS-ASX 24.08.2026 (Schwer CEO), Websuche Köhne-Primärquelle",
    "Partner/Technologie: HENSOLDT-PM und -GB 2025, Diehl-GB 2025, Rheinmetall-PM NNbS, EDR ILA 2024, Defense Post: C-TI-01..04/07/08",
    "Exportrahmen: BAFA-Kurzmeldung + Übersicht, AWA, Handelsblatt, WBF, SECO-Seite + Statistik 2025, SRF: C-EX-*, M-DEU-EXPORT-*, M-CHE-EXPORT-*, C-GCC-10",
    "Markt/Peers (Al Jazeera ×2, Gulf News ×2, Asharq, CRS, SIPRI, Arab News, trade.gov, Defense News, Unmanned Airspace, inderes/Kongsberg, TU, Army Recognition ×3, Breaking Defense ×3, Quwa, EOS-ASX, DIE ×2, Janes, TWZ, MBDA, GovCon Wire, Korea Times, Argaam, MEE ×2, The National, Militarnyi, Defense Post, Gabelli, Business AM, Euronews): M-*"
  ],
  "wiederverwendete_pruefergebnisse": "150 unveränderte Claims aus R1 (identischer Fingerprint, gleicher Auftrag/Stichtag) als \"übernommen\".",
  "offene_datenluecken_transparent": [
    "Köhne-Amtsantritt 01.10.2026 nicht primär bestätigt (nur Fachmedien).",
    "Kunden der Skynex-Aufträge 2019 und Q2-2026 offiziell unbenannt; Golf-Zuordnung unbestätigt.",
    "Betriebsstatus RADARABIA- und RBAT-Werke nach Gründung nicht belegt; RADARABIA-Fläche widersprüchlich.",
    "Einstufung von GCC-Staaten als konfliktbeteiligt durch die Schweiz nicht öffentlich festgelegt.",
    "Rheinmetall-Aussagen zu Golf-Einsätzen (P-GCC-01/03, T-CTX-21/22) sind Herstelleraussagen ohne Länder-/Systemzuordnung; kein unabhängiger Einsatznachweis 2026."
  ],
  "ausgabereife": "Faktenbasis inhaltlich freigegeben für interpret-v2 (Positionierung/SWOT). Nicht blockierende Hinweise vor HTML-Ausgabe einarbeiten; transparente Datenlücken (u. a. Köhne-Amtsantritt nicht primär bestätigt, Golf-Kunden der Skynex-Aufträge unbenannt, Herstelleraussagen zu Golf-Einsätzen ohne unabhängigen Nachweis) sichtbar lassen. Gesamtausgabe erst nach Schluss-Review.",
  "claims": [
    {
      "id": "T-CTX-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-9610b6cf1ddab64f); Belegstelle \"S. 1, Abschnitt 'Fiscal year 2025' und Hinweis zu discontinued operations\" inhaltlich bestätigt.",
      "fingerprint": "de86a8eee2e5080c8bda5a75c19cbb6982c698b63ed189eb4cf90f5d41f31d0c"
    },
    {
      "id": "T-CTX-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-1131fc174fb33fc5); Belegstelle \"S. 1-2, Abschnitte 'Key facts' und 'Rheinmetall Group: sales growth of 39%'\" inhaltlich bestätigt.",
      "fingerprint": "ee72ce08618c3c27f04578408eb391cc09535c831fdcf7e0ef5bb0d2e00d6591"
    },
    {
      "id": "T-CTX-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-1131fc174fb33fc5); Belegstelle \"S. 1 und S. 4, Abschnitt 'Outlook: annual sales guidance adjusted slightly'\" inhaltlich bestätigt.",
      "hochstufung": "Kennzahl Management-Zusammenfassung (Auftrag T-CTX-01..03)",
      "fingerprint": "b9964211ae5c85b963b5d6d71f0bd5f15690ddc2179aa1155615744a79b14701"
    },
    {
      "id": "T-CTX-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a57c168b042d9b28, S-9610b6cf1ddab64f, S-5a9f539c26c5885f); Belegstelle \"Rheinmetall AG (Halbjahresfinanzbericht): PDF-S. 8, Abschnitt 'Changes to the structure of the Group'; Rheinmetall AG (Pressemitteilung): S. 4, Abschnitt 'Rhein\" inhaltlich bestätigt.",
      "fingerprint": "c71e464b12d49d55cde8b06cbc88197410638fb7b95984bb7e428e8a1e166e30"
    },
    {
      "id": "T-CTX-05",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a57c168b042d9b28); Belegstelle \"PDF-S. 38 (Anhang, Segmentberichterstattung) und PDF-S. 8\" inhaltlich bestätigt.",
      "fingerprint": "77ed156734a233a406b8c35526de14ae1f6caa53108dfebadb89d95b64a6a318"
    },
    {
      "id": "T-CTX-06",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a8887f614647359f); Belegstelle \"Seite 'Der Vorstand der Rheinmetall AG', Personenabschnitte\" inhaltlich bestätigt.",
      "fingerprint": "ca820c4f40dc6b084575872a420462b7557d645036da8e44319e81615bce7079"
    },
    {
      "id": "T-CTX-07",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-3ef169e9e35e0c9a); Belegstelle \"Divisionsseite Air Defence, Abschnitte Einleitung und 'Standorte'\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "fe7d6df40d07e4d0cfc9039911c2b8588af1debc4ef696d990b3df55ff3f9162"
    },
    {
      "id": "T-CTX-08",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-1131fc174fb33fc5, S-a57c168b042d9b28); Belegstelle \"Rheinmetall AG (Pressemitteilung): S. 3, Abschnitt 'Air Defence: Rheinmetall Nomination increases sixfold'; Rheinmetall AG (Halbjahresfinanzbericht): PDF-S. 17,\" inhaltlich bestätigt.",
      "fingerprint": "27b7bc2eff0c31977d28b55e07fd584edaff5cbc08fbc0a9500593459b880d94"
    },
    {
      "id": "T-CTX-09",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a57c168b042d9b28); Belegstelle \"PDF-S. 30, Segmentbericht, Zeile 'Employees 30/6 (FTE)'\" inhaltlich bestätigt.",
      "hochstufung": "Kennzahl Air Defence (Auftrag T-CTX-08..11)",
      "fingerprint": "cca9479db9b80bd48d98280f17d7c61412dd5e5d47c9e544ada6f2588942eb9d"
    },
    {
      "id": "T-CTX-10",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a57c168b042d9b28); Belegstelle \"PDF-S. 22, Abschnitt 'Current annual guidance', Tabelle\" inhaltlich bestätigt.",
      "fingerprint": "9ac1f8d2251d2dc8b4a68a1cc39c387c822ccdbb13486cda9d0cad76d8f8f6e3"
    },
    {
      "id": "T-CTX-11",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: September-Präsentation PDF-S. 38 (2030 Sales potential €3-4bn), S. 39 (Top Projects inkl. \"Large replacement projects in MENA region\"), S. 42 (\"Superior cost efficiency proven in Ukraine and Gulf states\") bestätigt.",
      "fingerprint": "282ae3402afc8e2c9008099320ba2e344e045bd22cf6c0b40ac9fd43d951c7a3"
    },
    {
      "id": "T-CTX-12",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: H1-PM S. 3 \"ramp-up of the short- and very short-range air defence projects\" bestätigt.",
      "fingerprint": "1cfdc3fe00456ac5324ca70159af1d616dfa7910fa71bae751531037fb942857"
    },
    {
      "id": "T-CTX-13",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-9610b6cf1ddab64f); Belegstelle \"S. 3, Abschnitt 'Electronic Solutions: Further increase in sales'\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "0139994d40b3c94e1d504ce8adf89763cc7b2bc54ad2c241eb21232340d6c176"
    },
    {
      "id": "T-CTX-14",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-7a58ddb6fbab572c); Belegstelle \"Zefix-Datensatz, Felder name/uid/legalSeat/status/purpose\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "ef78da06dc4290387672a0f7e0cbd7bbee912d9be4d4d636a2f481d9716887ac"
    },
    {
      "id": "T-CTX-20",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a57c168b042d9b28); Belegstelle \"PDF-S. 7, Abschnitt 'Global economy with weak momentum'\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "e40a29a8e3b8da907ff163f35f87f582ac58c49973559f9b24d256f192cba5f2"
    },
    {
      "id": "T-CTX-21",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Statement stützt sich jetzt auf Primärtranskript FY2025 (PDF-S. 3, Zitat wortgleich bestätigt) und führt defence-network ausdrücklich als abweichende Sekundärwiedergabe (30 mm/Skyranger, >100 Drohnen nur sekundär). ME-6 behoben.",
      "runde": 2,
      "fingerprint": "a2eb3ee22c9272f05ef379feddb333386f1d5d0724b1d8943a07161cbb6a46ff"
    },
    {
      "id": "T-CTX-22",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: NZZ 11.03.2026 (datePublished 2026-03-11) per Direktabruf geöffnet: Frage/Antwort Golfstaaten wortgleich; ARIVA 11.03.2026 bestätigt Paraphrase. Inhalt konsistent mit Primärtranskript P-GCC-01.",
      "fingerprint": "ab964c42394631a8fbb942d2e46b5a015a46273c7e11312b2890512022f4de89"
    },
    {
      "id": "T-CTX-23",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-2eda3f58ea36842d); Belegstelle \"Pressemitteilung vom 15.6.2026, Key facts und Absatz 1\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "3b4c635bb3318fdd9f72881f75653621221199f53c0566c2f684042784be4a9b"
    },
    {
      "id": "T-CTX-24",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-b003618b3ae9eba2); Belegstelle \"Pressemitteilung vom 2.7.2026, Key facts und Absätze 1-3\" inhaltlich bestätigt.",
      "fingerprint": "b46277b85dc47715faa795b5e6a80fb9f24f9b6449ddb0d445337ac2ab834781"
    },
    {
      "id": "T-CTX-25",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a57c168b042d9b28); Belegstelle \"PDF-S. 43, Anhang, 'Rheinmetall Electronics acquires further shares in Rheinmetall Arabia Simulation and Training'\" inhaltlich bestätigt.",
      "fingerprint": "ef20fd070dbc8d22197303d1fd333bcbf990bea6bf67a21ba0bca30a99e24563"
    },
    {
      "id": "T-CTX-26",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a831015ab01561c0); Belegstelle \"Pressemitteilung vom 10.7.2026, Key facts und Absatz 1\" inhaltlich bestätigt.",
      "hochstufung": "Golf-Auftrag, gleiche Quelle wie Netzwerkkante C-GCC-11",
      "fingerprint": "8089c179e7203dd97042c8054dc6fde24afb6784a7d33e895342924087bb6ee8"
    },
    {
      "id": "H-KOE-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Belege unverändert (esut 04.09.2026 Abs. 1; Inside Paradeplatz 26.08.2026), Kennzeichnung \"angekündigt; nicht primär bestätigt\" und Verweis auf H-DUE-01/H-DUE-05 korrekt. Formulierungshinweis (nicht blockierend): esut berichtete am 4.9. im Futur (\"wird ... zum 1. Oktober\"); im Briefing \"sollte laut esut zum 1.10.2026 ... übernehmen\" statt \"ist seit\" verwenden. Keine Rheinmetall-Primärbestätigung (Datenlücke bleibt sichtbar).",
      "runde": 2,
      "fingerprint": "eabd48a86675b0d0ab3bb9713b796bec93c0134bc5ebf74e286227cb2fa993c2"
    },
    {
      "id": "H-KOE-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 05.01.2026 (\"Head of Rheinmetall's Weapons and Munitions division\"), PM 17.06.2026 (\"Head of Division Weapon and Ammunition\") und PDF-PM 18.06.2026 (\"CEO of Rheinmetall's Weapon and Ammunition Division\") geöffnet; esut Abs. 2 \"2025 übernahm er die Führung\" bestätigt.",
      "fingerprint": "71321c40a4368e2368c9bc3c74b9df74f3be787e0f62083706603317f2da7ac5"
    },
    {
      "id": "H-KOE-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-5a9d049f8f71abd3); Belegstelle \"Artikel vom 4.9.2026, Absatz 2\" inhaltlich bestätigt.",
      "fingerprint": "abff20d42fa4fbc0927d9647c875f46a57d3b315bf47e3ce14fa4dcbbdd863a9"
    },
    {
      "id": "H-KOE-04",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a9b0fc98036cb816); Belegstelle \"Pressemitteilung vom 24.9.2020, Absatz 3\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "288d029edbca1a9682ba4edfc1faf13e99c0dc653e03c4413b3558885bc27852"
    },
    {
      "id": "H-KOE-05",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-65fc5577a5b55116); Belegstelle \"Artikel vom 3.5.2023, Bildunterschrift und Absatz 1\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "f8eabd95e619e6e421da3a05f1deefbd2285ffe747c351a3a06e39329724c887"
    },
    {
      "id": "H-KOE-06",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-faa22e3546ff37b9, S-63879230d36c7828, S-d33dad308bfc2b33); Belegstelle \"Rheinmetall AG (Pressemitteilung): Pressemitteilung vom 5.1.2026, Zitat Köhne; Rheinmetall AG (Pressemitteilung): Pressemitteilung vom 17.6.2026, Zitat Köhne; R\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "af1fa2bcbe25bc04891e0350eafefd5d9b0264cea17a0372b39fd7fe03bf8f01"
    },
    {
      "id": "H-KOE-07",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-b9c5d3865d4b34f0); Belegstelle \"Videobeschreibung/Artikeltext, Absätze 1-5\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "72c6c161637503917f1d876e669ed8a209193301433a4b5cf5aeb4feec80d2f5"
    },
    {
      "id": "H-DUE-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-2eda3f58ea36842d); Belegstelle \"Pressemitteilung vom 15.6.2026, Zitatabsatz\" inhaltlich bestätigt.",
      "fingerprint": "6fc213eec85e83965fb2db8a29e9f4f3544b20b3f51237652e789cc4366043df"
    },
    {
      "id": "H-DUE-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Zefix-JSON (CHE-101.403.861) abgerufen: SHAB 2021-10-14 Eintrag Dürr (Delegierter VR, Direktor, Vorsitzender GL), Ochsner ausgeschieden; jüngste Publikation 2026-07-07 ohne Dürr/Köhne.",
      "fingerprint": "5b15b560e4245da07b12d3cba58168731f30e3a3eb9756f663f17d9c8bbd8c42"
    },
    {
      "id": "H-DUE-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: esut 04.09.2026 Abs. 1 und NZZ-Interview 10.10.2026 (datePublished 2026-10-10) geöffnet; Kündigung bei Papperger, fünf Jahre RAD AG, knapp drei Jahre Sparte bestätigt.",
      "fingerprint": "4487895d69dba1757d99764811c0d003dec282ccd07c989fa99b083a928cb88b"
    },
    {
      "id": "H-DUE-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Inside Paradeplatz 26.08.2026 geöffnet: Unterzeile \"abgesetzt\", \"Gestern hat die Zentrale ... verabschiedet\", mehrere anonyme Quellen bestätigt.",
      "fingerprint": "c236736c1a3d5fb3c2e6b9d69a96c7b62b992071f99478e2e4f3970072837952"
    },
    {
      "id": "H-PAP-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a8887f614647359f); Belegstelle \"Vorstandsseite, Abschnitt Armin Papperger\" inhaltlich bestätigt.",
      "fingerprint": "c71034778c35b203a60ea464c2ebceda5aa9ee8f4e8ae31e74b6851d59afd83b"
    },
    {
      "id": "H-PAP-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Vorstandsseite (Mandat \"Präsident des Verwaltungsrats\" RAD AG) und Zefix SHAB 2024-07-18 (Sagel aus, Papperger Präsident VR) bestätigt.",
      "fingerprint": "67d7b1902ec32ee6e05e95de0ea3a903be0bef0b4f46758125fe781f37f55ee4"
    },
    {
      "id": "H-GAN-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Zefix SHAB 2026-01-12 (Gansauge Mitglied VR) und 2026-07-07 (Vizepräsident VR, Krüger ausgeschieden) sowie Vorstandsseite (CEO W&A 04/2023-12/2024) bestätigt.",
      "fingerprint": "eb86b1507565f2b496ff2ccd78ee45f64c8564e0e2786d6faed032997488b84c"
    },
    {
      "id": "H-DUE-05",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu: PM 24.06.2026 (S-6bdb338d23c29e11) geöffnet, Zitat \"Oliver Dürr, Head of Rheinmetall's Air Defence Division\" bestätigt; Schluss \"primär bis mindestens Ende Juni 2026\" zulässig.",
      "runde": 2,
      "fingerprint": "d46cdd4d4b3bb74f3e0ce7ef99a97ae19f88ff435b8da7e05a86d21f25f10576"
    },
    {
      "id": "P-SKX-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-69738b1972b9a1ed); Belegstelle \"Produktseite Skynex, Abschnitte Skymaster, X-TAR3D, Revolver Gun Mk3, TREO, Effektoren\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "d570ea9d04c397464148ec68f5822f106f2b580b153d34225033bdcf1979544b"
    },
    {
      "id": "P-RG-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-4f3b5ef3636a54d6); Belegstelle \"Broschüre D712e0222, S. 1 (Main Features) und Tabelle Technical Characteristics\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "95fada33f8c0b3239347858cb4560e2a0bb69f60485f99ba676a29c50a8fcdc5"
    },
    {
      "id": "P-RG-02",
      "depth": "B",
      "status": "geprüft",
      "pruefnotiz": "R2: nur Quellen-ID-Vereinheitlichung (S-eb780da12d4e3349); \"first export contract ... MANTIS\" R1-geprüft.",
      "runde": 2,
      "fingerprint": "ba1321d7af0362e5f8c8a0d97dbec7d487cd0a1aae4478af98f37bc4448d05e8"
    },
    {
      "id": "P-SKX-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2: nur Quellen-ID-Vereinheitlichung (Janes 01.11.2019 unter S-eb780da12d4e3349); PM 30.10.2019 und Janes-Zitat R1-geprüft. Portfolio-Section jetzt \"GCC übergreifend ... ungenannter Kunde\" – Länderzuordnung korrigiert.",
      "runde": 2,
      "fingerprint": "78bc5732dd3ed3be5d51cb6526e4c74d18762d71df90947e0e43b987bc23431f"
    },
    {
      "id": "P-SKX-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Janes 14.10.2022 (MoD-Video 13.10., \"Shield 6 (Skynex)\", acht Revolver Gun Mk3, ein X-TAR3D) und Janes 15.12.2022 (\"first Skynex systems it supplied were for Qatar\") bestätigt. Hinweis: S-6cd5701123f00a73/S-18fa7e4158bdc58b sowie S-3b004b2cc914ddc4/S-f71c0348db6067c4 sind jeweils derselbe Janes-Artikel unter zwei URLs – kein unabhängiger Zweitbeleg.",
      "fingerprint": "83e78b128b45677a897bf1ebde1c3384cda3febc3e008a473a1992327f2a339d"
    },
    {
      "id": "P-SKX-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-3c0b72dcdb4a669f); Belegstelle \"Army Recognition, 20.01.2026, Artikeltext\" inhaltlich bestätigt.",
      "hochstufung": "Katar-Bezug (Schwerpunkt Golf)",
      "fingerprint": "e478048a6fc4e25f1d492df57cd840ca1955b816234e8d9cc6d3df059920ae50"
    },
    {
      "id": "P-SKX-05",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-3b004b2cc914ddc4); Belegstelle \"Janes, 15.12.2022, Absätze 2–5\" inhaltlich bestätigt.",
      "fingerprint": "8a170d1fabf6f309930f31209af39d1c9642991a9e93f7a54ea243880a87bccf"
    },
    {
      "id": "P-SKX-06",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Aussageursprung jetzt korrekt (Papperger: vier Skynex im Einsatz, Westukraine/Kraftwerke; Vollständigkeit der Lieferung als GAU-Schluss). ME-4 behoben.",
      "runde": 2,
      "fingerprint": "e5fe81fbabee65de5a38d14aa3a4bcda4be0ad6e494c75bed1987476de28e10d"
    },
    {
      "id": "P-SKX-07",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 15.01.2025 letzter Absatz bestätigt. Gegensatz zu P-SKX-08 ist korrekt als Herstellerangabe vs. berichtete interne Bewertung getrennt; beide attribuiert lassen, nicht auflösen.",
      "fingerprint": "f2d898b14061ab01abb53ef2a42690463882dd88196c38aba7d5f1d3d795b2de"
    },
    {
      "id": "P-SKX-08",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Defense Express 03.07.2026 geöffnet: Stern-Bezug, 01.04.2026, zwei Batterien/acht Geschützmodule, drei ausgefallen, Rheinmetall-Stellungnahme, Regierungsvertreter \"too few\" bestätigt. Stern-Original nicht geöffnet (wie angegeben).",
      "fingerprint": "e5397d696fa1c579beb3632b451d29a0fa0ab7f18b286613439bd0a36d036b9c"
    },
    {
      "id": "P-SKX-09",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-2da1e8991e862e88); Belegstelle \"Pressemitteilung 15.01.2025, Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "bd8793925d3b03e588620a67d53bf366c7b8b8c28109cf79c83dc1e61b9bc540"
    },
    {
      "id": "P-SKX-10",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-fa8494e2dc43316e); Belegstelle \"Joint Forces News, 23.12.2025 (Dateline 'Press Release, Düsseldorf')\" inhaltlich bestätigt.",
      "fingerprint": "ddb89eb52733eb79b7e66e2dcec0b3057ba9c6d0ed9cabb92978460bd8e2c1ee"
    },
    {
      "id": "P-SKX-11",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-b003618b3ae9eba2); Belegstelle \"Pressemitteilung 02.07.2026, Absätze 1–4\" inhaltlich bestätigt.",
      "fingerprint": "2a204b2c505a71505a9cdfbe5c986931f9c37c5e5fb14b3e7cc2cef9968497d6"
    },
    {
      "id": "P-RO-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-6bdb338d23c29e11); Belegstelle \"Pressemitteilung 24.06.2026, Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "b2037588028786261f0a32ff45dc8af4d818316f13d6f535fd432293e0881326"
    },
    {
      "id": "P-SKN-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2: Quellen-ID vereinheitlicht (Gulf News S-e59dc842147cf65f, R1-geprüft). Army-Technology-Teil weiterhin für Prüfer nicht zugänglich (403), inhaltsgleich durch EDR 08.03.2021 und Rheinmetall-Produktseite bestätigt.",
      "runde": 2,
      "fingerprint": "8bdafbd122805e3b48e3619caa0a99475aeedac4942afb40d05bf49590a0c7e6"
    },
    {
      "id": "P-SKN-02",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-69738b1972b9a1ed); Belegstelle \"Produktseite Skynex, Abschnitt SkyKnight\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "36d373d011e86f7777a111a81ae47287638c9f69afad935a8c3b905a95c8787b"
    },
    {
      "id": "P-SKN-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: EDR 20.11.2025 bestätigt Zitate Al Shamsi (Qualifikation \"late 2027\", Radar/Kanonen von Rheinmetall Italia, \"joint development\"). \"nähert sich dem Ende der Entwicklung\" ist Autorformulierung. Neuerer Stand als Janes 02/2025 (Ende 2026) – maßgeblich für Status.",
      "fingerprint": "5357e01a55e1f069c3277994a625d5dee92e85f271188f758266e2065b0b7c60"
    },
    {
      "id": "P-SR30-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-c0d13e5db6387716, S-d2d239c37b99eddf); Belegstelle \"Pressemitteilung 10.06.2026, Absätze 2–4 | Pressemitteilung 15.06.2026, Absatz 3\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "442cb928b2f500f26ab7ed590b850827bc68ff8bbb3577ccdf882ec49d20ab3d"
    },
    {
      "id": "P-SR30-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-9df26a722e63e113); Belegstelle \"ESuT, 27.02.2024, Absätze 1–4\" inhaltlich bestätigt.",
      "fingerprint": "35f06e3fd2605c91c93a886972f6ad178582aa64e0d24f9e1e80e3b3c36c0024"
    },
    {
      "id": "P-SR30-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-d2d239c37b99eddf); Belegstelle \"Pressemitteilung 15.06.2026, Abschnitt Kunden\" inhaltlich bestätigt.",
      "fingerprint": "77baf11d7b62e5a2e589a1f86a1903399504635aafb175d21639ee12d04f5a6d"
    },
    {
      "id": "P-SR30-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-562f0f3f359a746b); Belegstelle \"Pressemitteilung 23.02.2024, Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "9c9de235646a3d30b2352c29a56869ea2d68f4526e9de8207580981a8e19f2a2"
    },
    {
      "id": "P-SR30-05",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-d1aafc1c9b0f1a75); Belegstelle \"Pressemitteilung 30.09.2024, Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "0f8d27b24f7db182d2ac489951cae700a0bbb2223e3b4f5a659a1f9bd6d6bac4"
    },
    {
      "id": "P-SR30-06",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-60677f3d57da054d); Belegstelle \"Pressemitteilung 12.12.2025, Absätze 1–4\" inhaltlich bestätigt.",
      "fingerprint": "edf7f11dc5418b04a9b4cb301cb09b8d81b22ca2863725573d6cec482e9af2da"
    },
    {
      "id": "P-SR30-07",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-d2ef86f50f08a3d3); Belegstelle \"Pressemitteilung 20.12.2023, Absätze 1–3\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "eb2edad86dc59a6dbe74a2215d884e2872d81a4a37805623d9d2d348de25f8e3"
    },
    {
      "id": "P-SR30-08",
      "depth": "B",
      "status": "geprüft",
      "pruefnotiz": "R2: Quellen-ID vereinheitlicht (Euronews S-aaaf59c399a65ff2, R1-geprüft; Zitate bestätigt).",
      "runde": 2,
      "fingerprint": "f7f70f49e069eed628d5ffd382d8f3eaa94076246d60256559cb9dbed47814cf"
    },
    {
      "id": "P-SR30-09",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2: Quellen-ID vereinheitlicht (Army Recognition S-f06315f4acc363fb, R1-geprüft: \"not yet signed\", SAMI-Delegation Kassel, Tactical Report 12.11.2025).",
      "runde": 2,
      "fingerprint": "ab524aebb9a3f528f6197c779d22e50baffb7412722d177279d58ee35382195f"
    },
    {
      "id": "P-SR30-10",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-30ec1ea5187557fe); Belegstelle \"Tactical Report, 26.12.2025, frei sichtbarer Teaser\" inhaltlich bestätigt.",
      "fingerprint": "8266f98738a47059cc5bfb94679dc47363686e41c627a940368ad55342d00d2a"
    },
    {
      "id": "P-SR35-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-eadffcced857ac38); Belegstelle \"Pressemitteilung 10.10.2025, Absätze 1–4\" inhaltlich bestätigt.",
      "fingerprint": "83c9e7d616549edbc252475a1f0ffe7548e3498baa738599993e8c9a2b1c4f40"
    },
    {
      "id": "P-SR35-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-1363f14540d03428, S-d4ee756cc068980b); Belegstelle \"Shephard, 20.11.2025, Absätze 1–2 | Army Recognition, 03.09.2026, Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "a3adc8fb28dff689b8158aeed0447912312225638c16c20edc178b7d346d231d"
    },
    {
      "id": "P-SG-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-ef6817f0a0493313); Belegstelle \"Pressemitteilung 12.12.2023, Absätze 1–4\" inhaltlich bestätigt.",
      "fingerprint": "ee79b99d640e016768731754dce72aa7b48483e8f7760996a1a27941cab510de"
    },
    {
      "id": "P-SG-02",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a04eb741cdb51fb3); Belegstelle \"Pressemitteilung 05.07.2022, Absätze 1–2\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "c58e44e5ba7690f3b08fa52dd3fc2b7997e1b75423f51104d5d1b7cf0c008100"
    },
    {
      "id": "P-SG-03",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-f7338d89b12509f0); Belegstelle \"Pressemitteilung 10.01.2023, Absätze 1–2\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "cb9d3e99e03dc9cc64a5de973c5ae8e62d6f81e8181389d51749c05f6c6142d7"
    },
    {
      "id": "P-SG-04",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-96f74711ef265339); Belegstelle \"Shephard, 04.03.2014, Absätze 1–2\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "1859d6529fdef244956a6484b139d7720bd7de203c8fe232990898f82c0e5368"
    },
    {
      "id": "P-GCC-KW-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-72a1f85efa81bc7e); Belegstelle \"Army Recognition, 21.01.2013, Abschnitt Kuwait\" inhaltlich bestätigt.",
      "fingerprint": "2317147a376c146880628d52230e2718815455a69e52e8d7b385e5afb64fe114"
    },
    {
      "id": "P-GCC-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Transkript FY2025 PDF-S. 3 und Präsentation 11.03.2026 Folie 5 (\"Rheinmetall products in use\", \"used to fight incoming Iranian threats\") bestätigt.",
      "fingerprint": "4dd8d50bb37a86add33ba4d49e902883d28cf8d906a9be39e5d1a3aef0cfdf02"
    },
    {
      "id": "P-GCC-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Transkript FY2025 PDF-S. 9-10 bestätigt (negotiations, deliver in August, \"you need the contract and not the negotiations\").",
      "fingerprint": "30ad63d71baf24c6ecfccdfc30b13ddfda639b76c8d5a0fb979f13bb015b2386"
    },
    {
      "id": "P-GCC-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Transkript Q1-2026 PDF-S. 5 (\"about 150 systems in the whole Gulf region, gun-based\", \"more than 10 systems in 2026\") und Folie 10 (\"up to 10 systems for delivery in 2026\") bestätigt; Abweichung korrekt in uncertainty. Maßgebliche Primärquelle gegenüber M-RHM-GULF-02.",
      "fingerprint": "e9b9cc7ca72297812e94c1ccb5d9b8548123337667816412d9801af612bd4303"
    },
    {
      "id": "P-CUAS-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-5e9132be8a87d292); Belegstelle \"Pressemitteilung 18.12.2024, Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "be41718c162a1f29653d73244a93c3643ac473486c5362d2df1a94bd18b7a9da"
    },
    {
      "id": "P-CUAS-02",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-1587b1c751c31b9a); Belegstelle \"Transkript Q1-2026-Call, PDF-S. 23\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "bfe70be64a4fc0974a61b5dea1b1c9beab52c93a3bcaf1a69fc7c7a8ea4d5087"
    },
    {
      "id": "P-CAP-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-d2d239c37b99eddf, S-9c6ec027d4d1de66); Belegstelle \"Pressemitteilung 15.06.2026, Schlussabsatz | Transkript FY2025-Call, PDF-S. 4\" inhaltlich bestätigt.",
      "fingerprint": "a3e37f2cd9d220dcf4bcaca4a158251b7c9a07aa7259b2d5fa80157c7c20b101"
    },
    {
      "id": "P-AMMO-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-1587b1c751c31b9a); Belegstelle \"Transkript Q1-2026-Call, PDF-S. 22\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "5bed8899961fc945ae2d011a18d328d30b5c01ae9520505a812722af01dcca2c"
    },
    {
      "id": "P-HEL-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-3373659fa8b66b85); Belegstelle \"Pressemitteilung 09.07.2026, Absätze 1–4\" inhaltlich bestätigt.",
      "fingerprint": "92dee3bbbfbd7772b8eef181a019e67e3548163641c957e8335d17c90de53f80"
    },
    {
      "id": "P-MIL-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-c7786baa0a315e17); Belegstelle \"Produktseite Naval air defence, Abschnitt Millennium Gun\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "a872ecece1db12c9d446fe4d53f8d9e9fd544544a7c70d2ad69fa086374e13d8"
    },
    {
      "id": "C-STR-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 PDF-S. 268 (RAD AG 100 direkt, EK 386.181, Erg. 117.135 TEUR) und GB 2024 PDF-S. 254 (EK 373.980) per Download/Textextraktion bestätigt.",
      "fingerprint": "dabcf7db36699d640439f3a24c507878a01f9bf0abaae8ee4dc0c0d43189be21"
    },
    {
      "id": "C-STR-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Unternehmensseite RAD \"Über uns\" bestätigt (Bündelung sämtlicher Flugabwehraktivitäten, Umfirmierung 1.1.2009, Produktlinien, >40 Länder). Hochgestuft A (trägt Kante E01).",
      "hochstufung": "Netzwerkkante (required_full_review_ids)",
      "fingerprint": "1c36577c9e3ddf40553adc85a7ddbc0ad684cff69bca756c53d4d4a5220e7bbb"
    },
    {
      "id": "C-STR-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 S. 265 bestätigt.",
      "fingerprint": "690fb2c3b4c5d6182cf99a02088ae14b61c740107e8a13a88d4dc77c8d677049"
    },
    {
      "id": "C-STR-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 S. 268 (RDM 51 indirekt, EK 228.146) und S. 240 (Fremdanteil 49 %) sowie RDM-Unternehmensseite (RWM 51 %, Denel 49 %, gegründet 1.9.2008) bestätigt.",
      "fingerprint": "acc25fcdd6a68f1cc5c1ce9c8436181df2eaccec55779d0a848bc5fe2c0359fd"
    },
    {
      "id": "C-STR-05",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Vorjahresparaphrase jetzt korrekt (RPDC im GB 2024 S. 254, Fußnote 2, 49 % direkt); report_log korrigiert. ME-5 behoben.",
      "runde": 2,
      "fingerprint": "898c5ac3976924a8bfe0d53ac89cd73ad23773e66f49672ae57665128e2c001d"
    },
    {
      "id": "C-STR-06",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 S. 270 At-Equity-Abschnitt (20 %, −4.392/−4.159) und GB 2024 S. 256 (Fußnote 6, −459/−933) bestätigt; ohne JV-Fußnote, daher assoziiert.",
      "fingerprint": "8444efdec9cdc4879f78386a8fb6f3db3745c79e94acfd9a01c3b0c4aee81112"
    },
    {
      "id": "C-STR-07",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 S. 271 (49 %, 14.545/1.553, ohne Fußnote 5) und GB 2024 S. 256 (49, 14.799, −2.839) bestätigt.",
      "fingerprint": "41e0baceb937301910538550ec970294dea24a48f0e322c496c2f37b22176c34"
    },
    {
      "id": "C-STR-08",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: H1-Bericht PDF-S. 43 (100 % Anteile und Stimmrechte, Vollkonsolidierung Digital Systems ab Juli 2026) und GB 2025 S. 271 (40 %, Fußnote 5, historisch) bestätigt; Kante E19 rh_electronics→rast korrekt (100 %, Stimmrechte 100 %, as_of 2026-07). ME-1 behoben.",
      "runde": 2,
      "fingerprint": "b1dad25b137f877c934f6a8efc271f9e1ec6d97a98d6f37e8e1f13a52e638f2f"
    },
    {
      "id": "C-STR-09",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 S. 268 (Electronics (1) 100 direkt) und S. 269 (Italia 100 indirekt) bestätigt.",
      "fingerprint": "065c66de21d125def55f0c7f1f9b74aca9c0cd2262f8296b0e892bbcc6a4e8f5"
    },
    {
      "id": "C-TI-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 25.01.2024 (Partner, 1,2 Mrd. brutto, 607/339/284, IRIS-T SLM/Skyranger 30, Vertragspartner ARGE), GB 2025 S. 271 (Joint Operations ARGE NNbS 33) und HENSOLDT-GB 2025 S. 32 bestätigt.",
      "fingerprint": "ec8e5c7445e2bb8be4526bc7d85c5fd3ee6d2c091189423fb15151070ceb6724"
    },
    {
      "id": "C-TI-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: HENSOLDT-PM 12.12.2025 bestätigt.",
      "fingerprint": "8d4903d3151feb49ed863c50417eeba7ccc7129948c3b6eb411cb7bb1996a09d"
    },
    {
      "id": "C-TI-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: EDR 05.06.2024 per Direktabruf bestätigt (LOI ILA 2024, SADM in Skyranger 30, Werferentwicklung/-fertigung).",
      "fingerprint": "ce9c45db3547f6edadc0469d85fce8ed99e27a9e75b1d44517a87326cbb6405d"
    },
    {
      "id": "C-TI-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: The Defense Post 13.11.2025 bestätigt (\"reportedly\" Werfer; DefendAir = SADM laut Artikel).",
      "fingerprint": "dbbab871dd20f9d9aa31acf50e5483840160dc7ff13d5e4a64f719598924b8dd"
    },
    {
      "id": "C-TI-05",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Gulf News 23.02.2021, Breaking Defense 24.02.2021 (Rheinmetall \"responsible for the integration\", VAE erster Kunde) und Janes 24.02.2025 bestätigt. Konsistenzhinweis: Qualifikationserwartung \"Ende 2026\" (Janes 02/2025) durch HALCON 11/2025 auf \"late 2027\" verschoben (P-SKN-03); EDGE-CEO 05/2026 \"not in service, going into production\" (M-UAE-EDGE-03). Kantenstatus E27 entsprechend aktualisieren (nicht blockierend).",
      "fingerprint": "7610ca23415242bb0dcddc4beeb6d695a478691cb8729d2fba1cdfe3c8a6920e"
    },
    {
      "id": "C-TI-06",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: EDR 08.03.2021 Abs. 2 bestätigt; nur eine Sekundärquelle, historisch.",
      "fingerprint": "0f4082f6b78b274344b8076d1ed268522303a0fe481808bf82c274caed92ffb5"
    },
    {
      "id": "C-TI-07",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 S. 15 (AR-Zustimmung Anfang 11/2025), S. 234 (Gewinn 46 Mio. EUR), GB 2024 (AIM 50 %) und Diehl-GB 2025 PDF-S. 23 bestätigt.",
      "fingerprint": "12453b68e7193380cabe01c4ec23293475ba3271d4e1bbb98fad5f511938359c"
    },
    {
      "id": "C-TI-08",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Diehl-GB 2025 PDF-S. 22 bestätigt; Gegenstand nicht genannt, kein Rheinmetall-Bezug – Kante E32 korrekt als Diehl–EDGE ohne Overlap-Kooperation.",
      "fingerprint": "041cecbb02ea25f72e8d8541197ec8de83eff2567b839276958174f9f80b0d28"
    },
    {
      "id": "C-TI-09",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 23.02.2024 bestätigt.",
      "fingerprint": "009afbe6a5f6e1e896e01d7801566b61114756fc9eccd589e42ae5ea1c23917a"
    },
    {
      "id": "C-GCC-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Qatar Tribune 14.03.2018 und Gulf Times 15.03.2018 (Notice to Proceed Munitionswerk, Vereinbarung QENF) bestätigt.",
      "fingerprint": "1c724819963b8fec9b5ffa298f3cc7a9ed7d4f991f78c202d5beb4a02a5b0b38"
    },
    {
      "id": "C-GCC-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Aviation Week 07.03.2022 (25.000 m², Fertigung/MRO/Ersatzteile/Ausbildung), Janes 07.03.2022 (25,000 sq ft Dschidda, Skyguard-MRO RSADF, 60 % Lokalisierung \"according to the two companies\") und Argaam 07.03.2022 (25.000 m²) bestätigt. RADARABIA-Flächenwiderspruch korrekt offen ausgewiesen; zwei Quellen (inkl. Zitat RADARABIA-Chairman) nennen m², Janes sq ft – in Ausgabe als Widerspruch führen, keine Fläche als gesichert darstellen.",
      "fingerprint": "b6d7ba3e72e967a3eee6975a0cf91b2250ffc294a3417b03c9770ce88093e942"
    },
    {
      "id": "C-GCC-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Argaam 07.03.2022 Abs. 1-3 und Janes 07.03.2022 bestätigt; \"company executive\" bezieht sich im Kontext auf Zino Hart (Bildunterschrift: board member RAD Arabia; Text: board member Rheinmetall Defense). Argaam weist auf KI-Übersetzung hin.",
      "fingerprint": "22f2076140d87c56381e9efd2583c6a9c5977e5498ebebcdcbece21d3948990d"
    },
    {
      "id": "C-GCC-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-f06315f4acc363fb); Belegstelle \"Artikel vom 17.11.2025, Absätze 2 und letzter Absatz\" inhaltlich bestätigt.",
      "hochstufung": "Golf-Marktzugang Saudi-Arabien (Schwerpunkt C-GCC-*)",
      "fingerprint": "07781e4d776380b68bc3ff559360314b54197acbba7e4c566f1ed3f26f1c0a1d"
    },
    {
      "id": "C-GCC-05",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Defense News 06.04.2016 (SPA-Bezug, Al-Kharj, RDM/SAMIC) und PMG-Antwort NW1259 (Frage 20.05.2016; kein JV, schlüsselfertig, Lieferanten-Kunden-Beziehung) bestätigt. Kante E43 als Lieferbeziehung korrekt.",
      "fingerprint": "936e25baa63e14b55874b5b06901e4714ee42370401019ba695cd67506fde04c"
    },
    {
      "id": "C-GCC-06",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Gulf News/Reuters 08.11.2018 bestätigt (1 Mrd. USD, Denels 49 % an RDM, \"a source familiar\", Schwer: \"discussions are not finalised\"). Teilkante E44 historisch korrekt; Fortbestand Denel 49 % über C-STR-04 belegt.",
      "fingerprint": "076bd724b0d670d5c7293bf54e798fae7e3f51f1a8807c46db01ed0e3861cf9f"
    },
    {
      "id": "C-GCC-07",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Arab News 25.02.2019 und Asharq Al-Awsat 25.04.2020 (S-05ec117bf73653de: \"Abukhaled will be taking over from Dr. Andreas Schwer who has served ... since January 1, 2018\") bestätigt; Kante E46 jetzt historisch (2018 bis 04/2020). ME-2 (Teil SAMI) behoben.",
      "runde": 2,
      "fingerprint": "a8d83cf25af3cdeea0c6e564a7cfd0cf0f8fc40b5557ffa305c28d2eabdba6fa"
    },
    {
      "id": "C-GCC-08",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2: nur Quellen-ID-Vereinheitlichung (S-6cd5701123f00a73, S-3b004b2cc914ddc4 = dieselben Janes-Artikel wie R1); Inhalt R1-geprüft, Kante E18 Quellen konsistent.",
      "runde": 2,
      "fingerprint": "8c0150c9706040ea70c062b2e6996b3509a0a8c275007dfb8bf9691b446c246b"
    },
    {
      "id": "C-GCC-09",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2: nur Quellen-ID-Vereinheitlichung (S-eb780da12d4e3349 = Janes 01.11.2019, inhaltsgleich mit R1-geprüftem Artikel; S-6cd5701123f00a73 = Janes 14.10.2022, letzter Absatz bestätigt).",
      "runde": 2,
      "fingerprint": "e1345264c93a9f25c4be379742c06da11a7f4fe7679e85e18b1f7624415be35b"
    },
    {
      "id": "C-GCC-10",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: SRF 12.07.2022 bestätigt (SECO-Angaben Katar, acht Kanonen, Garantien; Saudi-Arabien Ersatzteile/Munition). Kein Hersteller genannt – korrekt keine Kante.",
      "fingerprint": "72bd71b829ddb325d264863c86641e5d13a2d0bae796bdea24cdf4bd6dc71877"
    },
    {
      "id": "C-GCC-11",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 10.07.2026 bestätigt (Kuwaiti Naval Forces, acht Al-Dorra-Boote, Wert \"low double-digit\" + \"high single-digit\", Key facts \"mid double-digit\", Q2 2026, Lieferung bis Q2 2029, ADSB baut für EDGE als Prime). Vertragsrichtung offen korrekt ausgewiesen.",
      "fingerprint": "b0cfe5d6dbdf99f833e242174b9ce2165167a8322f796b58632dbae4da629fee"
    },
    {
      "id": "C-GCC-12",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: NZZ 20.03.2026 bestätigt Wortlaut. Hinweis: NZZ verdichtet Pappergers Interviewaussage (\"unsere Flugabwehrsysteme\", S-549a5efe1b3c131f) zu \"Skynex\"; Skynex-spezifische Golf-Präsenz damit nicht primär belegt.",
      "hochstufung": "Golf-Präsenzaussage (Schwerpunkt C-GCC-*)",
      "fingerprint": "818122243b07dc66121d3f40839864e65f58f03b93c7010edb0bf84ee33dc72b"
    },
    {
      "id": "C-GCC-13",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM (DE) 02.07.2026 bestätigt; Kunde/Region nicht genannt.",
      "fingerprint": "11bf3cfa018aaf53819935a6538e92d8a367370246c2f490bf4e9fc8360b6530"
    },
    {
      "id": "C-GCC-14",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu: ASX 12.12.2023 (CEO seit 01.08.2022, MD seit 11.12.2023), ASX 19.06.2026 (Gen5-Auftrag, Unterzeichner Schwer als MD/CEO) und Webull-Kopie ASX 24.08.2026 (als Drittanbieter-Kopie gekennzeichnet) bestätigt. Kante E47 schwer→eos (overlap, keine Rheinmetall-EOS-Kooperation behauptet) korrekt. Hinweis: Die ASX-Belege nennen die Rheinmetall-/SAMI-Vorgeschichte nicht; Personenidentität über Namen/Titel plus EOS-Mitteilung 2022 (eos-aus.com/?p=835: frühere Positionen u. a. \"Rheinmetall AG\", \"public sector defence industry\", wirksam 1. August 2022) gestützt – diese Quelle als Identitätsanker ergänzen empfohlen (nicht blockierend). ME-2 behoben.",
      "runde": 2,
      "fingerprint": "5014b72cc697542e69b5434a400b84501d85971113937f78c7d4c96ebe69d639"
    },
    {
      "id": "C-KD-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 27.02.2024 bestätigt.",
      "fingerprint": "3475212bb334bb4c66fbeeadf18921e97fca450c2af276b641790283ea1eda4d"
    },
    {
      "id": "C-KD-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 12.12.2025 bestätigt.",
      "fingerprint": "ffc0dbff86150e37434b56ca7979963a81af65571816347e68ad37f555cede0d"
    },
    {
      "id": "C-KD-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: PM 24.06.2026 bestätigt (verweist auf PM 02.06.2026; zitiert Dürr als Head of Air Defence Division).",
      "fingerprint": "d817626cec7809386dde23d89cc2ff2e4aed2261a6ea62025dade53a6b37e116"
    },
    {
      "id": "C-KD-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: GB 2025 S. 39 (Italien Skynex eingeführt) und S. 65 (Lieferungen an europäische Kunden; Backlog NNbS/Skyranger 30) bestätigt.",
      "fingerprint": "abf21bdad0f2196417f51e744ecade7567cb7f6f90d3e87ef63b2444b29872f9"
    },
    {
      "id": "C-KD-05",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: NZZ 20.03.2026 (32 Systeme, 800 Mio. CHF, keine verbindliche Offerte, freihändige Vergabe, ab 2028) per Direktabruf bestätigt.",
      "fingerprint": "c049b9325eeeb5b723ac7548f23f95cafcd4c4eade7755c5ae2c623cd015f2d2"
    },
    {
      "id": "C-EX-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Scheinwiderspruch entfernt; Handelsblatt 20.03.2026 und BAFA-Übersicht (Bekanntgabe 10.09.2026, bis 15.09.2027, II.6.6 neu) bestätigt.",
      "runde": 2,
      "fingerprint": "e1dca0a69a2373379e334a17e4bb44f3c212d8d6dc1a5f82c1d5da67a1b2f053"
    },
    {
      "id": "C-EX-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: WBF-Medienmitteilung 20.03.2026 bestätigt; Golfstaaten nicht genannt.",
      "fingerprint": "ed6b6e8e3441f60b9bd1e92f6f92d545a76078ad4e02aaae104690aece439b0a"
    },
    {
      "id": "C-EX-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-954b1ad2b853fa8f); Belegstelle \"Tabelle 'Ausfuhr von Kriegsmaterial: 1.1.–31.12.2025; Endempfängerstaaten', S. 1\" inhaltlich bestätigt.",
      "hochstufung": "Exportkontext (Schwerpunkt C-EX-*)",
      "fingerprint": "61696e2b0e9bd121dcfe7a32198a0e9df4710cae17ff6db45ae2fa211761ef03"
    },
    {
      "id": "M-GCC-THREAT-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-d246fbdc9c4c6b97); Belegstelle \"Artikeltext, Abschnitte zu Saudi-Arabien, VAE, Bahrain und Kriegskontext\" inhaltlich bestätigt.",
      "fingerprint": "45c65f4a1707a505707c618f2fcda21f8657fa3ec1b51e40bbe83da2edc30b2e"
    },
    {
      "id": "M-UAE-THREAT-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-2e4f786c41d7b2ee); Belegstelle \"Artikeltext, Absatz mit kumulierten Zahlen des Verteidigungsministeriums (Stand 3. April 2026)\" inhaltlich bestätigt.",
      "fingerprint": "b2374a6cb4b579dbdbde377c09af35496d0e979f3c0f82563dde0b6292733368"
    },
    {
      "id": "M-GCC-THREAT-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-00b3bb9075c00199); Belegstelle \"Artikeltext, Tally-Absatz\" inhaltlich bestätigt.",
      "fingerprint": "166a5125dd37a286125031722b9322a26e637e37ca7a008d780163eb0bf4c9d8"
    },
    {
      "id": "M-GCC-THREAT-03",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-4abfdb5bf72ddb30); Belegstelle \"Artikeltext, Länderabschnitte und Kontext zur Waffenruhe\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "2bdf6db936468cef8cbb18a51ba8c5b430a670eb57ac840aa8bbc40d5b043785"
    },
    {
      "id": "M-KWT-THREAT-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-7a89b412faeaf6ce); Belegstelle \"Artikeltext, Kontextabsatz zum Angriff\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "23063d46216f94fa584529cc531f431e1bac94269e5f04b332734bcd775b88b5"
    },
    {
      "id": "M-GCC-THREAT-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Gulf News 08.10.2026 bestätigt Huthi-Anspruch Riad (nicht verifiziert), 3 Tote/36 Verletzte, Tanker 51 sm vor Katar (UKMTO), VAE-Flughäfen in Betrieb. Formulierungshinweis: Artikel erwähnt keine direkten iranischen Angriffe auf die VAE an diesem Tag; eine ausdrückliche Feststellung \"keine Angriffe\" enthält er nicht.",
      "fingerprint": "22caca6ea57fa888b212816f660e1b32e3cbf85d01304ee4df47bc7ca26dfaab"
    },
    {
      "id": "M-SAU-THREAT-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-37ccf8b458258ca3); Belegstelle \"Artikeltext, Absätze zu Entsendung, gemeinsamer Erklärung und Quellen\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "5a14a1b63fd7d3c453c6ba8203ddd023d2e749d671e31ae99610e9b912f6bb11"
    },
    {
      "id": "M-BHR-THREAT-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-4691f9471b203297); Belegstelle \"S. 1 (Issues for Congress) und S. 3–4 (NSA Bahrain)\" inhaltlich bestätigt.",
      "fingerprint": "8fba0decb0b0eb1ba46b72773f527691c401e784b29df8f80fe7232a866f5010"
    },
    {
      "id": "M-GCC-THREAT-05",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-68cd066e40b60677); Belegstelle \"Artikeltext, Absätze zu Videos, Kosten und Shahed-Drohnen\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "3fed5ba265e2b5f09e5dfd620f5a157214a7204d9144513ca1334e8f15da901a"
    },
    {
      "id": "M-SAU-BUDGET-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-c07effa3f3662a94); Belegstelle \"Fact Sheet April 2026, Tabelle 1 (S. 2) und Abschnitt 'The Middle East' (S. 7, 11); Tabelle 2 Fußnote g\" inhaltlich bestätigt.",
      "fingerprint": "ef64526fa09a81f90d548607a84acd7ef9d17c35d6beda5630577df70a003a64"
    },
    {
      "id": "M-KWT-BUDGET-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-c07effa3f3662a94); Belegstelle \"Fact Sheet April 2026, Tabelle 1 (S. 2)\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "a3da5e2e364d62e30b7e7f1164b21329333e5a3148585a11670511301eaf0ad0"
    },
    {
      "id": "M-OMN-BUDGET-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-c07effa3f3662a94); Belegstelle \"Fact Sheet April 2026, Abbildung 3 (Militärlast nach Ländern)\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "314d8d387d314074261bc82fd930af4a695517f63a993812734306a02e864cb9"
    },
    {
      "id": "M-UAE-BUDGET-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-c07effa3f3662a94); Belegstelle \"Fact Sheet April 2026, Tabelle 2, Fußnote g; Tabelle 1\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "07d4d22b2072b25264a1a3b2fe01e36030f3e23d14357dff3a10ce8152072f2a"
    },
    {
      "id": "M-SAU-BUDGET-02",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-13ac2bcc7a8d3bc1); Belegstelle \"Artikeltext, Absatz zu Sektorausgaben Q1 2026\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "537add5dc8a2ce0e0bb045007762f24b9f861cbc5d348e3ad527be194f0bcb98"
    },
    {
      "id": "M-SAU-LOCAL-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-591cad6afbdb6208); Belegstelle \"Artikeltext, Einleitung (GAMI, erstes jährliches Sektortreffen Riad)\" inhaltlich bestätigt.",
      "fingerprint": "4655eabe715088509ddca1227dcccc41efde681491f187a3ea5ed44896cd0ff7"
    },
    {
      "id": "M-UAE-ACCESS-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: \"Raketenabwehr als erste von mehreren Beschaffungsprioritäten\" entspricht trade.gov-Wortlaut.",
      "runde": 2,
      "fingerprint": "0534b633000f14abe2ee38461ad8a300e05c22109bef0694dc2934ff5d7790d7"
    },
    {
      "id": "M-GCC-PROG-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-4c4af0e05b9558f2); Belegstelle \"Artikeltext, Auflistung der Notifizierungen\" inhaltlich bestätigt.",
      "fingerprint": "6e74cd3da4566f9fa91d664550d8ddf3412cc13cd3c4fdb436d33eaf1af13646"
    },
    {
      "id": "M-UAE-PROG-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-d7c95ccbcee5e1ba); Belegstelle \"Artikeltext, zitierte State-Department-Mitteilung\" inhaltlich bestätigt.",
      "fingerprint": "4929083ed30c114539cbc80d0dfeac7f1dba9dbe0e5226cfad53b886e07241e4"
    },
    {
      "id": "M-QAT-PROG-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-a23dcdde6a28b4bb); Belegstelle \"Artikeltext, Absätze 1–3\" inhaltlich bestätigt.",
      "hochstufung": "trägt Marktbeobachtung",
      "fingerprint": "305d3f281fb02f315c11bfc0f917e806951d52e12ef46f4f60db42f9c794bad2"
    },
    {
      "id": "M-KWT-PROG-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-7a89b412faeaf6ce); Belegstelle \"Artikeltext, Absätze 1–3\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "d2d12e10f42a54cb371e5eb9bae4442a59299a613f126d5a865c9944deb0e863"
    },
    {
      "id": "M-KWT-PROG-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-346bbac409450892); Belegstelle \"Börsenmitteilung 30.06.2026, Absätze 1–2\" inhaltlich bestätigt.",
      "fingerprint": "d36d96b283789c348b5578a207cbb814e119ac2520bf5281665ab49db6fe6106"
    },
    {
      "id": "M-QAT-PROG-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: AMRAAM-ER-Detail entfernt; verbleibende Aussagen (Raytheon Hauptlieferant, 5,6 Mrd. NOK, 11 Länder inkl. Katar/Oman) bestätigt.",
      "runde": 2,
      "fingerprint": "b2ccac90415c930b05ffcb578fff209d99a6abd9e4dbee30296bfa108dbf7e6f"
    },
    {
      "id": "M-SAU-PROG-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-1bc2890891ce328b); Belegstelle \"Artikeltext, Absätze 1–3\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "0fc30738bbbce906eb73bf191b7620fbf62efe4bf236d5916cd85d625c1d55bb"
    },
    {
      "id": "M-BHR-PROG-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-4691f9471b203297); Belegstelle \"S. 6, Tabelle 1 'Recent U.S. Foreign Military Sales to Bahrain Notified to Congress'\" inhaltlich bestätigt.",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "9c56662694ee9ad3e26c3f59eb468c867f44f6b989827fd3c9ad9f56ec067eaa"
    },
    {
      "id": "M-GCC-TUR-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: MEE 11.05.2026 bestätigt: Korkut-100/25-Verträge Saudi-Arabien/Katar nur nach \"two Turkish defence industry insiders\"; Kuwait-G2G-Protokoll vom Verteidigungsminister unterzeichnet berichtet; Oman-Interesse und US-Lieferrückstände bestätigt. Anonymität korrekt ausgewiesen; nicht als bestätigter Vertrag verwenden.",
      "fingerprint": "9e938b94a7ceff6ca66c8cf8a56f8013d0687eaa460a10eb14ccad87b664f908"
    },
    {
      "id": "M-SAU-PROG-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-873f7366346b9261); Belegstelle \"Artikeltext, Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "0982f9a558f746ed4b09aefb91556da528a3f58825d55f82d5cb589306ff1807"
    },
    {
      "id": "M-QAT-RHM-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-6cd5701123f00a73); Belegstelle \"Artikeltext (Jeremy Binnie), Absätze 1–3\" inhaltlich bestätigt.",
      "fingerprint": "3dc13871e141a3597bc0b8cd4c341a2a1f426c17e0c1d44e4e1f0e7a5642f520"
    },
    {
      "id": "M-QAT-RHM-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-3b004b2cc914ddc4); Belegstelle \"Artikeltext, Absatz zu Katar\" inhaltlich bestätigt.",
      "fingerprint": "8d0d0c07ac4adef2b9663bdb214ba42d11bad838c37a3324b2c2ba288efabc84"
    },
    {
      "id": "M-QAT-RHM-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Army Recognition DIMDEX 2026 bestätigt (QEADF-Stand, X-TAR3D 50 km, Mk3 1.000 Schuss/min, 4.000 m, 252 Schuss). Hochgestuft A (trägt Marktbeobachtung).",
      "hochstufung": "trägt Marktbeobachtung",
      "fingerprint": "3c4d80a96036007eba18a03115302f08698fbac7a13863825abd389af126021e"
    },
    {
      "id": "M-QAT-RHM-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-48538d413f65c35e); Belegstelle \"Artikeltext, Absatz zu Rheinmetall\" inhaltlich bestätigt.",
      "fingerprint": "c7aebf984bb6a1872ab989be95a1a26b5adeac64a7f8c8643b72158ab52d7464"
    },
    {
      "id": "M-QAT-BARZAN-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Liefererwartung \"within 2027\" ergänzt und als Ankündigung gekennzeichnet; bestätigt.",
      "runde": 2,
      "fingerprint": "4470c9d2ee5e3b4a84e13862887260ca41e3a8961154c12b2487662ebea5fa3b"
    },
    {
      "id": "M-SAU-RHM-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-d401a7e147a6b2d4); Belegstelle \"Artikeltext, Absätze zu RAD Arabia und Aussagen Zino Hart/Ibrahim Al-Zeer\" inhaltlich bestätigt.",
      "fingerprint": "0463f655fa354001472c6f34f8d88ca74dda1a147752995f71734eefd4857f26"
    },
    {
      "id": "M-SAU-RHM-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Janes 26.02.2020 bestätigt (SPA-Foto King Abdulaziz Naval Base, Satellitenbilder Juni-Juli 2019, zwei 35-mm-GDF + Feuerleitgerät). Hochgestuft A (trägt Marktbeobachtung).",
      "hochstufung": "trägt Marktbeobachtung",
      "fingerprint": "63e7f2b2a9ad0db181ecce7346b2358981fd83a9443e61ec430d9723e3816ffb"
    },
    {
      "id": "M-RHM-GULF-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Gabelli 27.03.2026 bestätigt Wortlaut; gegen Primärtranskript FY2025 abgeglichen (nearly all countries have Rheinmetall Air Defence systems; deliver in August; \"Air Defence, a growth rate of 25%\"). Gabelli formuliert \"would use\"; Primärtranskript als Beleg vorziehen.",
      "fingerprint": "e65aabe65d151967976218a8e1d5e7313c4e563036c0f8a982fa603f8e5296f9"
    },
    {
      "id": "M-RHM-GULF-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Business AM 10.05.2026 bestätigt Auszug (\"presque doubler le déploiement ... au Moyen-Orient d'ici fin 2027\"); abweichende Zahlen nicht mehr übernommen, Primärwortlaut P-GCC-03 maßgeblich. ME-3 behoben.",
      "runde": 2,
      "fingerprint": "cba41938222e6c5e5da56b6c81265c190155069cabfb18ae9a2770432cad036c"
    },
    {
      "id": "M-RHM-CAP-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Euronews 17.09.2026 bestätigt (400/Jahr ab Ende kommenden Jahres; Mittelkaliber <1 Mio. → 4 Mio. Schuss). Gleiches Dokument wie P-SR30-08 unter zweiter Quellen-ID (S-5201e1820b86a0c3) – zusammenführen, kein Zweitbeleg. Konsistent mit P-CAP-01 (PM 15.06.2026 \"70 to 100 turrets → up to 400\").",
      "hochstufung": "trägt Marktbeobachtung",
      "fingerprint": "403efb39ed6272f0155b887c207b73546cf75dd615b260727f555e73886bd76b"
    },
    {
      "id": "M-RHM-ORDER-01",
      "depth": "B",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: esut 03.07.2026 bestätigt; Wiedergabe der PM 02.07.2026 (P-SKX-11, C-GCC-13, T-CTX-24) – kein unabhängiger Beleg, inhaltlich konsistent (39 Monate ≈ Lieferung bis 2029).",
      "stichprobe": "einzeln geprüft (Stichprobe auf Vollprüfung ausgeweitet, gebündelter Quellenabruf)",
      "fingerprint": "8dab1d9aab977e067b8f745225087619fadddbeeddce7305b2e964b297f80f25"
    },
    {
      "id": "M-RHM-CUAS-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Militarnyi 12.07.2025 bestätigt (Video ukrainische Luftwaffe, Zitat \"flawless results\", AHEAD laut Videoauswertung). Konsistent mit P-SKX-07; Gegenbefund P-SKX-08 separat attribuiert.",
      "fingerprint": "035b2cec2a34e8fd21ac0af069affb4d6bf80c0367619a6864afeeb6c3ee07de"
    },
    {
      "id": "M-UAE-EDGE-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-829071fd179d4705); Belegstelle \"Artikeltext (Paolo Valpolini), Absätze 1–5\" inhaltlich bestätigt.",
      "fingerprint": "f1508e3eb644a432c41e4c6fee62844acca7663d5963da4f4e4fa0eb730ee1df"
    },
    {
      "id": "M-UAE-EDGE-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Janes 24.02.2025 bestätigt; uncertainty weist jetzt auf überholte Zeitangabe (HALCON 11/2025: Ende 2027, P-SKN-03) hin.",
      "runde": 2,
      "fingerprint": "b6146bbc54a87677bedc1ee136eb192d8e147986fabdf1492a6c7551442856e5"
    },
    {
      "id": "M-UAE-EDGE-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-7a92bf0944771ac1); Belegstelle \"Interviewtext (SAHA 2026), Abschnitte Iran-Konflikt und Partnerschaften\" inhaltlich bestätigt.",
      "fingerprint": "8a88628f7caca9b445c4a946fc9532b60772740ff42d4c384641361a18f626bc"
    },
    {
      "id": "M-PEER-KOR-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-c44a53b9b7fed3f5); Belegstelle \"Artikeltext, Abschnitte Konfiguration, Betreiber, Lieferungen\" inhaltlich bestätigt.",
      "fingerprint": "5f4f2d0dc468a3fe1ce9cc547ab134a71eb437907cb38ff841ccc32cf21d020b"
    },
    {
      "id": "M-PEER-EOS-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-0ee334ddc9eec2c2); Belegstelle \"ASX-Mitteilung S. 1–2\" inhaltlich bestätigt.",
      "fingerprint": "230950156a9773ebd9ec5f277c0373945e1e7683098e55055123966bea850255"
    },
    {
      "id": "M-PEER-EOS-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-16987d30779651f5); Belegstelle \"Artikeltext (Martin Chomsky), Abschnitte Vertrag/Bedingungen/Systeme\" inhaltlich bestätigt.",
      "hochstufung": "trägt Marktbeobachtung",
      "fingerprint": "d5f7e3b9c0395236404515eb45c43228086cec712076160d6bcfa4448c72f3df"
    },
    {
      "id": "M-PEER-EOS-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-0e7ad928d9638007); Belegstelle \"Artikeltext (Joe Saballa), Absätze 1–5\" inhaltlich bestätigt.",
      "hochstufung": "trägt Marktbeobachtung",
      "fingerprint": "e2d49dd010363b21987f7e3e0f0078b479a9e364e66cd328d7d0613f336323a7"
    },
    {
      "id": "M-PEER-NASAMS-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-3d92fa89ab4d601e); Belegstelle \"Artikeltext, Absätze 1–3 (Quelle Aftenposten)\" inhaltlich bestätigt.",
      "fingerprint": "0956e0ec940178121e0c6c3e8584f0693b03bfaad4710a3ed7085b0974455a18"
    },
    {
      "id": "M-PEER-MICA-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-06318d4e0dd58da5); Belegstelle \"Pressemitteilung 19.10.2020, Absätze 1–4\" inhaltlich bestätigt.",
      "hochstufung": "trägt Marktbeobachtung",
      "fingerprint": "89b66f943444a73e96199b31e6d2760de2957465aae8c9856264068b6c7e8219"
    },
    {
      "id": "M-PEER-COYOTE-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-b6faabdb5b5fbeb3); Belegstelle \"Artikeltext (Nicholas Fiorenza) und Bildunterschrift\" inhaltlich bestätigt.",
      "fingerprint": "eab0f59a6657a92e28dd6c76b8fa65759eb2d20b3e2c89015dc31c06dd2252dc"
    },
    {
      "id": "M-PEER-COYOTE-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: Beleg geöffnet (Abruf 10.10.2026, S-32a1f2cd50c3b5ae); Belegstelle \"Artikeltext, Absätze 1–4\" inhaltlich bestätigt.",
      "fingerprint": "2cf9642605de3e750fb671677d06eb6491e2e63fc451bd570ff45fdd17cc470a"
    },
    {
      "id": "M-DEU-EXPORT-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: BAFA-Kurzmeldung 20.03.2026 bestätigt (befristet bis 15.09.2026, Registrierung bis 30 Tage, monatliche Meldepflichten, Länderliste).",
      "fingerprint": "a4219f3cba65eb59be6a309724b45929c96c2bc609570edd78eb6d628e921ed0"
    },
    {
      "id": "M-DEU-EXPORT-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 neu geprüft: Primärbeleg BAFA-Übersicht ergänzt; Wortlaut (\"Mit Bekanntgabe vom 10. September 2026 ... bis zum 15. September 2027\", II.6.6) und AWA bestätigt. Hinweis (nicht blockierend): uncertainty nennt eine \"ungeklärte Abweichung\" 9./15.09.2026 – die Archivangabe bezieht sich auf die durch die Bekanntgabe vom 10.09.2026 abgelöste Fassung bzw. Genehmigungsliste, nicht auf das ursprüngliche Laufzeitende; Satz kann entfallen. Aussage selbst korrekt.",
      "runde": 2,
      "fingerprint": "dd8ab02f3288173231753746fdc76fc372493a83f2fb08e579e7cf021f582d9c"
    },
    {
      "id": "M-CHE-EXPORT-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: WBF-Medienmitteilung 20.03.2026 bestätigt inkl. \"bestehende Bewilligungen ... keine Kriegsrelevanz ... weiterhin genutzt\".",
      "fingerprint": "d1f508e856e7165b0dbe5347c50afb0edf3a3711dd7f5030b3b0adc4bdee2a06"
    },
    {
      "id": "M-CHE-EXPORT-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch mit R1); Befund R1: SECO-Seite bestätigt (Abstimmung 29.11.2026, Parlamentsbeschluss 19.12.2025, Anhang 2 seit 1. Juli 36 Länder – Liste geprüft, kein GCC-Staat, Abweichungskompetenz).",
      "fingerprint": "34a4f04d5ce7a860975260d7e6ca20281caaa42ed5fd79e2cda884245a1794a4"
    }
  ],
  "runde": 2,
  "material_errors_r1_erledigt": [
    {
      "id": "ME-1",
      "claim_ids": [
        "C-STR-08"
      ],
      "erledigt": "R2 geprüft"
    },
    {
      "id": "ME-2",
      "claim_ids": [
        "C-GCC-07"
      ],
      "erledigt": "R2 geprüft"
    },
    {
      "id": "ME-3",
      "claim_ids": [
        "M-RHM-GULF-02"
      ],
      "erledigt": "R2 geprüft"
    },
    {
      "id": "ME-4",
      "claim_ids": [
        "P-SKX-06"
      ],
      "erledigt": "R2 geprüft"
    },
    {
      "id": "ME-5",
      "claim_ids": [
        "C-STR-05"
      ],
      "erledigt": "R2 geprüft"
    },
    {
      "id": "ME-6",
      "claim_ids": [
        "T-CTX-21"
      ],
      "erledigt": "R2 geprüft"
    }
  ],
  "hinweise_nicht_blockierend": [
    {
      "owner": "cluster",
      "ids": [
        "E27",
        "C-TI-05"
      ],
      "hinweis": "Kante E27 uncertainty \"Qualifikation erwartet Ende 2026\" ist durch P-SKN-03 (HALCON 11/2025: late 2027) und M-UAE-EDGE-03 überholt; vor HTML-Ausgabe datieren/aktualisieren (Claim C-TI-05 selbst korrekt datiert)."
    },
    {
      "owner": "market",
      "ids": [
        "M-RHM-GULF-02",
        "M-UAE-EDGE-02"
      ],
      "hinweis": "Beobachtungen gulf_access/production_capacity (rheinmetall) und procurement_status (edge) zitieren P-GCC-03 bzw. P-SKN-03 im Text, führen diese IDs aber nicht in claim_ids; für die Abhängigkeitsprüfung der Interpretation P-GCC-03/P-SKN-03 in claim_ids aufnehmen, falls der Datenvertrag Fremdmodul-IDs erlaubt (Inhalt korrekt)."
    },
    {
      "owner": "market",
      "ids": [
        "M-DEU-EXPORT-02"
      ],
      "hinweis": "uncertainty-Satz zur \"ungeklärten Abweichung\" 9./15.09.2026 kann entfallen (Archivangabe betrifft abgelöste Fassung/Liste)."
    },
    {
      "owner": "context",
      "ids": [
        "H-KOE-01"
      ],
      "hinweis": "Im Briefing Futur/Ankündigung formulieren und \"nicht primär bestätigt\" sichtbar lassen."
    },
    {
      "owner": "cluster",
      "ids": [
        "C-GCC-14"
      ],
      "hinweis": "EOS-Mitteilung 2022 zur Ernennung (frühere Positionen bei Rheinmetall AG) als Identitätsanker ergänzen."
    },
    {
      "owner": "market",
      "ids": [
        "M-SAU-RHM-01"
      ],
      "hinweis": "25.000 m² mit Verweis auf den Flächenwiderspruch (Janes: sq ft, C-GCC-02) versehen."
    }
  ],
  "input_fingerprint": "6d0065a25da52fc28ec9bb8eb19f7dc21c957253d95b9e4cfb0ad647ff55657b"
}
```
