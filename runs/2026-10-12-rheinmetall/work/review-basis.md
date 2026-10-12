# Review

```json
{
  "schema_version": 1,
  "run_id": "2026-10-12-rheinmetall",
  "company": "Rheinmetall",
  "as_of": "2026-10-12",
  "phase": "basis",
  "status": "freigegeben",
  "material_errors": [],
  "review_scope": {
    "method": "references/quellenpruefung.md (verbindlich), cluster-recherche.md, cluster-quellenkatalog.md, netzwerk-html.md, gespraechspartner.md, ausgabe-html-v2.md, faktenphase.md",
    "formal_check": "python3 scripts/check-review-data.py runs/2026-10-12-rheinmetall/work/review-packet.json → Exit 0, errors=[] (nur formal; keine Inhaltsprüfung). scripts/__pycache__ entfernt.",
    "inputs": [
      "input/auftrag.md",
      "input/facts-run.json",
      "work/review-packet.json (180 Claims, 162 Quellen, module_views, module_context, network 43 Knoten/54 Kanten)",
      "work/facts-validation.json (required_full_review_ids: 37)",
      "work/comparison-plan.json"
    ],
    "actually_checked": "Alle 162 Quellen im aktuellen Lauf geöffnet (159 per curl/Textextraktion, 3 per WebFetch nach HTTP 403/406: S-34516b5032f5dad2, S-95cc0ee12b8ad9b8, S-b798e8edef2944e7); 8 PDFs lokal mit pdftotext seitengenau ausgewertet (GB 2025, GB 2024, H1-Bericht 2026, Jahresabschluss 2025, SIPRI, Diehl-GB 2025, Hensoldt-AR-Kopie, EOS-ASX). Jeder Claim gegen die Belegstelle im Original abgeglichen; alle 37 required_full_review_ids und alle 54 Netzwerkkanten mit A geprüft. Auch die 37 B-Claims wurden im gemeinsamen Quellenabruf vollständig gegengelesen (keine nur nicht-einzeln-geprüften Restclaims).",
    "depth_decisions": "Vorschläge der Rollen übernommen; hochgestuft auf A: C-013, C-014, C-018, C-022, C-040 (Netzwerkkanten/required) und M-EXP-006 (trägt Matrix-Beobachtung rheinmetall/industrial_capacity). Ergebnis: 143 A, 37 B. Korrekturrunde 1: T-13 neu (A) → 144 A, 37 B. Hochstufungsrunde: alle 37 B → A (181 A, 0 B).",
    "targeted_additional_checks": [
      "Personen-Aktualität: WebSearch 'Roman Köhne Rheinmetall Air Defence CEO Oktober 2026' – keine widersprechenden Meldungen; WOZ 01.10.2026 nennt Dürr 'scheidender CEO' (konsistent).",
      "Bundeswehr-Skyranger-Zahlen: WebSearch nach abgeschlossenem Großauftrag 2026 – kein unterzeichneter Folgevertrag gefunden; Bundeswehr-Zahlen in Claims konsistent (1 Prototyp + 18 Serie = 19)."
    ],
    "not_accessible": "Keine Prüfquelle endgültig unzugänglich. Janes S-210cf4ad91a0bf63/S-3b004b2cc914ddc4 nur bis Paywall lesbar; die tragenden Sätze (Katar-Bestätigung, Sprecher 13.12., 182 Mio.) sind im frei lesbaren Teil enthalten."
  },
  "source_groups": [
    {
      "group": "Rheinmetall Geschäftsberichte/Abschlüsse",
      "source_ids": [
        "S-a3c9838c6400c810",
        "S-d164f147051d7af2",
        "S-a57c168b042d9b28",
        "S-3ace92799f3780ea"
      ],
      "pages": "GB25 S.15,27,38,39,50,65,91,259,262–266; GB24 S.21,34,47,48,49,62,244–248; H1 S.10,17,38,43; JA25 S.9,26,30 (PDF-S. = gedr. S.)",
      "claims": "T-01,T-05,T-11,C-001,C-002,C-005,C-006,C-007,C-012,C-025–C-028,C-030–C-035,C-038–C-043"
    },
    {
      "group": "Rheinmetall Finanz-PMs",
      "source_ids": [
        "S-170bd0a173a148bf",
        "S-c6f02c948a96ecdf"
      ],
      "claims": "T-02,T-06–T-10,P-AD-03"
    },
    {
      "group": "Rheinmetall Unternehmens-/Produktseiten (o. D.)",
      "source_ids": [
        "S-001a4ac74ab4feec",
        "S-18ce19a1fbbec148",
        "S-5741e59d6038c1c0",
        "S-928f8de516fc152d",
        "S-e687ba029a397767",
        "S-6e95f2aa9d8c5d60",
        "S-c54a714d4e512ca1",
        "S-caf1328d1364fda8",
        "S-69738b1972b9a1ed",
        "S-11300cfdaf427560",
        "S-0775fadde4aeaf05",
        "S-b4a0be56edf21cf2",
        "S-81ee1216c407e8d6",
        "S-37f835c7c1c07fd6",
        "S-c7786baa0a315e17",
        "S-3b238e0c480e757b"
      ],
      "claims": "T-01–T-04,T-11,H-01,H-02,H-04,H-05,P-AD-01,P-AD-02,P-SR-01,P-SNX-01,P-SNX-08,P-RG-01,P-XTAR-01,P-MSU-01,P-SM-01,P-SG-01,P-AH-01,P-MG-01,P-CUAS-01,P-CUAS-02,C-003"
    },
    {
      "group": "Rheinmetall Pressemitteilungen 2018–2026",
      "source_ids": [
        "S-c46af79f314a32d2",
        "S-b8a3496f93a22c8c",
        "S-585f6266c676c138",
        "S-d1aafc1c9b0f1a75",
        "S-562f0f3f359a746b",
        "S-60677f3d57da054d",
        "S-09c52404c1b93824",
        "S-d2ef86f50f08a3d3",
        "S-afe1512f0f6979bd",
        "S-c0d13e5db6387716",
        "S-d2d239c37b99eddf",
        "S-6282cce4ae4b577f",
        "S-724f79dd7eacb957",
        "S-ccfa2e88d8a2c995",
        "S-eadffcced857ac38",
        "S-6bdb338d23c29e11",
        "S-cede873d57924937",
        "S-24a17414294b663e",
        "S-17c0358578e526e5",
        "S-3b27cf3712ca73d2",
        "S-081455a6101c816e",
        "S-3e41dec11fd4d5d0",
        "S-b003618b3ae9eba2",
        "S-6c44e0c111e6d686",
        "S-dfcb101880f585b3",
        "S-ef6817f0a0493313",
        "S-a03195f784728b13",
        "S-b935cdad4fdfc9f0",
        "S-f3ed5e1e0c0ea213",
        "S-7f40b1791bf978ab",
        "S-c5774e615432a4d1",
        "S-06ea7a8a3f2ad0cd",
        "S-16115aa2a8137b37",
        "S-3e6da2e4a874f72c",
        "S-3373659fa8b66b85",
        "S-a9b919fffe9bdf37",
        "S-faa22e3546ff37b9",
        "S-8be20dfde7cdb9e0",
        "S-f562ccee195198fd",
        "S-a831015ab01561c0",
        "S-601e38253a77d205",
        "S-3094767eb36c7a05",
        "S-ed85256fd87c2a74",
        "S-1a558a92449e8e86",
        "S-3997375c416bfffe",
        "S-6ceae77f0e11c121",
        "S-50513344d04758cf",
        "S-aa06566f7d1b93c7",
        "S-2da1e8991e862e88"
      ],
      "claims": "P-SR30-*, P-SR35-*, P-SNX-02/04/05/06/07/11, P-SG-02/03/04, P-SS-01, P-AH-02, P-GP-01, P-HEL-*, P-NNBS-01, P-MASS-01, P-GULF-01, P-CUAS-03/04/05, P-SSP-*, T-12, T-20–T-22, T-27–T-29, H-02, C-020, C-026–C-032, C-034, C-035, C-038"
    },
    {
      "group": "Register/Behörden",
      "source_ids": [
        "S-7a58ddb6fbab572c",
        "S-19429e5ec4910a16",
        "S-20d85ac40b61c709",
        "S-02f2d309d4be9a72",
        "S-c99327dbed7f6de5",
        "S-66afb03f29f245ab",
        "S-34516b5032f5dad2",
        "S-d1be5243ec1023a0",
        "S-3dd2c405657f77d5",
        "S-869ac7412d8eadfb",
        "S-ee64de417a6b1930",
        "S-ec51f3cf697afaa7",
        "S-c07effa3f3662a94"
      ],
      "claims": "T-11,T-12,C-024,C-029,M-EXP-001,M-EXP-002,M-EXP-004–M-EXP-006,M-SA-001,M-SA-002,M-AE-001,M-AE-002,M-GCC-007–M-GCC-009"
    },
    {
      "group": "Fachmedien/Nachrichten zu Rheinmetall (Sekundärquellen)",
      "source_ids": [
        "S-5a9d049f8f71abd3",
        "S-5a9f539c26c5885f",
        "S-d6967131447345e6",
        "S-aaa18763ca399ee7",
        "S-eec5e9e91d4acc36",
        "S-f69359ba57ec833a",
        "S-957ebff673ab8d20",
        "S-945cfdd5c97e17d9",
        "S-210cf4ad91a0bf63",
        "S-3b004b2cc914ddc4",
        "S-6cd5701123f00a73",
        "S-57816f4227585f45",
        "S-d5c3acd69d302e6f",
        "S-a51eb8534c24e129",
        "S-7dbdfac4d40d7b07",
        "S-d401a7e147a6b2d4",
        "S-878ff498269f6714",
        "S-26fb2a0ffb0e98b0",
        "S-05ab0d04fb7863ad",
        "S-4423d24b37b6b642",
        "S-4adb7d30df595768",
        "S-3c0b72dcdb4a669f",
        "S-e57c1d4455df01c5",
        "S-9d63edda09166afa",
        "S-faf804b35f3ff96a",
        "S-829071fd179d4705",
        "S-9eaea886238f7319",
        "S-f0cdb46723f6b4ca",
        "S-4b451685af5fc6ea",
        "S-f4ef6013df2b2aa2",
        "S-cf2d60fe50bbfd35",
        "S-77582115dd4f5802",
        "S-c7e039b1d7fdfd1f",
        "S-0111976d9a6dd789",
        "S-81d777c3c4bafa8b",
        "S-ef86c664e3ccb75b",
        "S-700b6f4c30b3a0d5",
        "S-b798e8edef2944e7",
        "S-68b567498c55dacc",
        "S-c84be580187f30d9",
        "S-1107b2b74890bec4",
        "S-d56f666031f40a66"
      ],
      "claims": "H-01–H-03,T-02,T-12,T-23–T-26,P-SNX-03,P-SNX-08–P-SNX-10,P-SG-05,P-SG-06,P-MG-02,P-GULF-02,C-004,C-008–C-011,C-013–C-019,C-021,C-023,C-024,C-029,C-032,C-036,C-037,M-QA-002,M-QA-005,M-QA-006,M-RHM-002–M-RHM-005,M-EXP-006"
    },
    {
      "group": "Partner-/Wettbewerberquellen",
      "source_ids": [
        "S-e07bb2a244b7af05",
        "S-97f46b755db97ab6",
        "S-2fab023367922b5c",
        "S-f59c80c54f1ce7fb",
        "S-2c2db8b1343f6d8d",
        "S-a150acd33ca7df5e",
        "S-126278ae64b82aa8",
        "S-a6638d78307df741",
        "S-cfb8279414c9ce40",
        "S-2b4d367d62244e1f",
        "S-b88f838de8142eaa",
        "S-9616ea0e0b0b5d61",
        "S-3d92fa89ab4d601e",
        "S-e9905dfc7de8c5b0",
        "S-dd897c36830d9e37",
        "S-ffd46967200270d4",
        "S-9bba6057c1bcc3e4",
        "S-95cc0ee12b8ad9b8",
        "S-346bbac409450892",
        "S-0ee334ddc9eec2c2"
      ],
      "claims": "C-022,C-027,C-042,M-DIE-*,M-SAAB-*,M-NAS-*,M-MBDA-*,M-THA-*,M-KW-001,M-AE-005"
    },
    {
      "group": "Golfmarkt-Lage/Programme (Medien/Think Tanks)",
      "source_ids": [
        "S-b5639af6f764d7b0",
        "S-f3212d207bf9215c",
        "S-87aa29a929aef01b",
        "S-f4577b793d766942",
        "S-4abfdb5bf72ddb30",
        "S-e2b088f5052623c8",
        "S-1bc2890891ce328b",
        "S-e290230878030bca",
        "S-7a92bf0944771ac1",
        "S-39c1d048e95b3b30",
        "S-aed841da179552fb",
        "S-7a89b412faeaf6ce",
        "S-ed279402fe3a4403",
        "S-c0be679988afecf7",
        "S-cf83d408678767c7",
        "S-8200e1151b66ded4"
      ],
      "claims": "M-GCC-001–M-GCC-006,M-SA-003,M-AE-003,M-AE-004,M-QA-001,M-QA-003,M-QA-004,M-KW-002,M-BH-001,M-OM-001,M-EXP-003,M-RHM-003"
    }
  ],
  "samples": {
    "approach": "Gruppen nach Modul/Quelle/Aussageart gebildet; da alle Quellen ohnehin für A-Claims geöffnet wurden, wurden alle 37 B-Claims vollständig gegengelesen (Stichprobe = 100 %). Ergebnis B: 36 bestätigt, 1 Korrektur (T-27 Ereignisdatum) → abhängige Aussagen geprüft (Event ev_2026_romania; P-SR35-03/C-035 korrekt datiert).",
    "groups": [
      {
        "group": "context/Rheinmetall-PM/Auftragsmeldungen",
        "claim_ids": [
          "T-20",
          "T-21",
          "T-22",
          "T-27",
          "T-28",
          "T-29"
        ],
        "result": "5 bestätigt, T-27 Datumskorrektur"
      },
      {
        "group": "context/Medienwiedergaben CEO/Partner",
        "claim_ids": [
          "T-24",
          "T-26"
        ],
        "result": "bestätigt"
      },
      {
        "group": "context/Unternehmenswebsite",
        "claim_ids": [
          "T-01",
          "H-04"
        ],
        "result": "bestätigt"
      },
      {
        "group": "portfolio/Herstellerseiten und Messe-PMs",
        "claim_ids": [
          "P-SR30-09",
          "P-SR762-01",
          "P-SNX-04",
          "P-SG-01",
          "P-SG-04",
          "P-SS-01",
          "P-MSU-01",
          "P-SSP-01",
          "P-SSP-02",
          "P-CUAS-01",
          "P-CUAS-02",
          "P-CUAS-03",
          "P-CUAS-05"
        ],
        "result": "bestätigt"
      },
      {
        "group": "portfolio/Sekundär/Drittanbieter-Kopie",
        "claim_ids": [
          "P-SNX-10",
          "P-GULF-02"
        ],
        "result": "bestätigt (Quellenart korrekt)"
      },
      {
        "group": "cluster/GB und PM ohne Netzwerkkante",
        "claim_ids": [
          "C-023",
          "C-025",
          "C-026",
          "C-043"
        ],
        "result": "bestätigt"
      },
      {
        "group": "market/Hintergrund",
        "claim_ids": [
          "M-GCC-006",
          "M-GCC-007",
          "M-SA-003",
          "M-AE-002",
          "M-AE-005",
          "M-QA-004",
          "M-BH-001",
          "M-SAAB-004"
        ],
        "result": "bestätigt"
      }
    ],
    "not_individually_checked": []
  },
  "contradictions_resolved": [
    {
      "topic": "AGG 48 Gültigkeit",
      "claim_ids": [
        "C-024",
        "M-EXP-001",
        "M-EXP-002"
      ],
      "finding": "Amtlich verlängert bis 15.09.2027 (BAFA, Bekanntgabe 10.09.2026); C-024 veraltet → ME-1."
    },
    {
      "topic": "Skynex Ukraine 160 vs. 182 Mio. EUR",
      "claim_ids": [
        "P-SNX-02",
        "P-SNX-03",
        "C-037"
      ],
      "finding": "Beide Werte in den jeweiligen Quellen korrekt wiedergegeben (PM 09.12.2022/Defense Post/Janes: 182 Mio. + 12 Mio. HX; Defense News/Ercolani: ~160 Mio.). Widerspruch bleibt offen und ist transparent; kein Wert als gesicherter Vertragswert verwenden."
    },
    {
      "topic": "X-TAR3D 50 vs. 55 km",
      "claim_ids": [
        "P-XTAR-01",
        "P-SNX-05",
        "M-RHM-002"
      ],
      "finding": "Skynex-Seite 25/35/50 km, Stationary-Seite 25/35/55 km, Italien-PM 'bis zu 50 km' – Herstellerinkonsistenz korrekt offengelegt."
    },
    {
      "topic": "Bundeswehr-Skyranger-Zahlen",
      "claim_ids": [
        "T-20",
        "P-SR30-01",
        "P-SR30-02",
        "P-SR30-08",
        "C-028",
        "M-RHM-005"
      ],
      "finding": "Konsistent: 1 Prototyp + 18 Serie (=19 Fahrzeuge), Option 30, 595 Mio. brutto; kein abgeschlossener Großauftrag (~600) belegt; Serienlieferung ab 2027 laut CEO. Medienberichte über Verzögerung (März 2026) nicht Teil der geöffneten Belege."
    },
    {
      "topic": "T-25 Bloomberg-Wiedergabe",
      "claim_ids": [
        "T-25"
      ],
      "finding": "Wiedergabe korrekt; Bloomberg-Datum 08.05.2026 über Link im geöffneten Artikel belegt; Zahleninkonsistenz (Verdopplung von ~150 vs. Gesamt ~400) korrekt offengelegt; nur als Medienwiedergabe einer Unternehmensaussage nutzbar."
    },
    {
      "topic": "Leitung Air Defence Dürr → Köhne",
      "claim_ids": [
        "H-01",
        "T-12"
      ],
      "finding": "Dürr am 24.06.2026 noch Head of Division (PM), ES&T 04.09.2026 Wechsel zum 01.10., WOZ 01.10.2026 Dürr 'scheidend', Rheinmetall-Karriereseite: Köhne seit Oktober 2026 CEO Division Air Defence (Sitz Zürich). Identität und aktuelle Rolle bestätigt; Organfunktion RAD AG nicht belegt (Registerstand 07.07.2026)."
    }
  ],
  "network_review": {
    "identity": "company=Rheinmetall, as_of=2026-10-12, target_id=rheinmetall (genau ein target) – passend zum Auftrag; keine Knoten/Kanten aus Fremdfirmenlauf erkennbar.",
    "edges_checked": "Alle 54 Kanten (E01–E54) mit Richtung, Typ, Kategorie, Status/as_of, Produktbezug und Quoten gegen Originalbelege geprüft; Kapitalanteil, Stimmrechte und Kontrolle getrennt korrekt (u. a. E11 49 % direkt/Kontrolle via Stimmrechtsmehrheit; E13/E22 at equity 20/49 % indirekt; E19 100 % Anteile und Stimmrechte ab 07/2026; E31/E48 Joint Operations 33/50 %). Indirekte Pfade (z. B. Rheinmetall→RAD AG→RADARABIA←MAZ; EDGE→HALCON→Rheinmetall; ARGE-Teilkanten) einzeln belegt. Überschneidungen (E27 EDGE–Kuwait, E30 Diehl–EDGE) korrekt als overlap ohne bilaterale Rheinmetall-Kooperation.",
    "notes_non_blocking": [
      "E37 (MBDA→BAAINBw, customer): BMVg nennt keinen Auftragnehmer, Defense News nennt MBDA als Hersteller; Status 'Finanzierung gebilligt' und Unsicherheit sichtbar halten (nicht als unterzeichneten Vertrag darstellen).",
      "E34 Produktbezug 'sr30': Quelle belegt Vernetzung LVS NNbS mit Skyranger 30, keine Skyranger-Lieferung im NNbS-Vertrag – im Detail als Vernetzungsbezug kennzeichnen.",
      "E03 as_of 2004-03-04 ist Stand des Lexikonartikels; Ereignisjahr 1999 bleibt im Detail sichtbar.",
      "Quellen-Duplikate (gleiches Dokument, abweichende URL): S-210cf4ad91a0bf63 = S-3b004b2cc914ddc4 (Janes), S-57816f4227585f45 = S-d5c3acd69d302e6f (Janes), S-a831015ab01561c0 = S-601e38253a77d205 (MASS-PM), S-5741e59d6038c1c0 = S-928f8de516fc152d (RAD About us). Nicht als unabhängige Zweitbelege zählen."
    ],
    "coverage": "Abdeckungsmatrix/Coverage dokumentiert breite Nachrichten-/Fachmediensuche (Janes, Aviation Week, Defense News, Breaking Defense, Gulf Times, Arab News, Argaam, Beobachter, ESUT, Army Recognition u. a.) und Hinweisverfolgung (u. a. Army Recognition 11/2025 Saudi-Skyranger-Interesse, Burkan, The National) – keine reine PM-Suche. Grenzen (TED/CORDIS nicht direkt, EDGE/MAZ/Barzan-Berichte nicht analysiert) offen ausgewiesen; Status 'teilweise' angemessen. cluster/focus plausibel, keine vollständige Füllung verlangt."
  },
  "module_views_review": {
    "context": {
      "result": "weitgehend korrekt",
      "corrections": [
        {
          "item": "events.ev_2026_romania",
          "owner": "context",
          "reason": "Datum 2026-06-24 = Veröffentlichungsdatum der Detail-PM; Vergabe am 29.05.2026 (H1-Bericht S.10, PM 02.06.2026).",
          "action": "Datum auf 2026-05-29 setzen oder Label als Meldung kennzeichnen (vgl. T-27)."
        }
      ],
      "checked": "company_facts (10), events (14) inkl. Datumslogik (unbekannte Daten zuletzt, 'angekündigt'/'laut Medien'), topics, gaps, profile. Profil Roman Köhne: Name, intro, snapshot (5), career (6, chronologisch, Nachweis- vs. Eintrittsdatum getrennt), expertise, responsibilities (Organfunktion RAD AG als nicht belegt), regional_context korrekt weggelassen (gap_regional_context). Keine Label-Aussage ohne Deckung."
    },
    "portfolio": {
      "result": "weitgehend korrekt",
      "corrections": [
        {
          "item": "products.drone_defence_toolbox",
          "owner": "portfolio",
          "reason": "P-CUAS-05 (Telekom-Absichtserklärung) belegt keinen Bezug zur Drohnenabwehr-Toolbox; Produktzuordnung ungedeckt.",
          "action": "P-CUAS-05 aus der Produktzeile entfernen bzw. als eigene Sektion 'Kooperation (Absicht)' ohne Produktbezug führen."
        }
      ],
      "checked": "products (22) mit domain/short_label/sections, regions gcc (Länderabgrenzung Katar/Saudi-Arabien/Kuwait/VAE; MASS korrekt als Marine-Softkill außerhalb Flugabwehrgeschütz), topics, gaps."
    },
    "cluster": {
      "result": "weitgehend korrekt",
      "corrections": [
        {
          "item": "topics.air_defence.sections['Kunden Europa und Ukraine']",
          "owner": "cluster",
          "reason": "Enthält C-026 (nicht benannter internationaler Kunde) – Label deckt Zuordnung nicht.",
          "action": "C-026 in eigene Sektion 'Nicht benannte Kunden' verschieben."
        },
        {
          "item": "gaps.G04 / coverage Exportrahmen",
          "owner": "cluster",
          "reason": "Siehe ME-1 (AGG 48 verlängert bis 15.09.2027).",
          "action": "aktualisieren"
        }
      ],
      "checked": "topics/sections, gaps G01–G08, coverage, report_log R01–R08 (Geschäftsjahr, Veröffentlichung, Seiten; GB-Seiten am PDF bestätigt)."
    },
    "market": {
      "result": "teilweise korrekt",
      "corrections": [
        {
          "item": "observations saab/customer_status",
          "owner": "market",
          "reason": "Siehe ME-2.",
          "action": "korrigieren"
        },
        {
          "item": "observations mbda/gulf_access",
          "owner": "market",
          "reason": "M-MBDA-003 bezieht Nahost-Nachfrage auf MICA als 'multi-mission air-to-air missile system', nicht auf VL MICA (GBAD).",
          "action": "Beschreibung präzisieren ('MICA-Nachfrage laut MBDA, Systemvariante nicht spezifiziert/Luft-Luft')."
        }
      ],
      "checked": "regions (9) inkl. Länderzuordnung und getrennter Rheinmetall-Präsenz-Sektion, topics, peers (7) mit role_note, observations (32) gegen Claim-Inhalte, gaps/coverage. M-EXP-006 auf A hochgestuft (industrial_capacity). Hinweis: rheinmetall/gulf_access nutzt keine C-Claims; Golf-Gesellschaften/JV-Beteiligungen (C-006, C-007, C-015) sind geprüfte A-Fakten und können vom Positionierungsplan herangezogen werden."
    }
  },
  "non_blocking_hints": [
    {
      "owner": "cluster",
      "claim_ids": [
        "C-017"
      ],
      "text": "Beobachter-Artikel trägt im Quelltext datePublished 2021-06-03; Quellenregister published_date ggf. ergänzen."
    },
    {
      "owner": "cluster/portfolio",
      "claim_ids": [
        "P-SNX-03"
      ],
      "text": "Geöffnete Defense-News-Quelle (26.01.2024) enthält Hinweis von Rheinmetall Italia auf bevorstehende Skynex-Verträge mit 'a Middle East state' – als Fundhinweis für Golfmarkt dokumentieren, nicht als Beziehung."
    },
    {
      "owner": "market",
      "claim_ids": [
        "M-EXP-006"
      ],
      "text": "WOZ 01.10.2026 zitiert Dürr (SRF): Lieferung nach Saudi-Arabien bei Exportbewilligung – möglicher Fundhinweis, kein Fakt zu Aufträgen."
    },
    {
      "owner": "portfolio",
      "claim_ids": [
        "P-SR30-02"
      ],
      "text": "Medienberichte (März 2026) zu Verzögerung der Skyranger-30-Serienlieferung nicht im Paket; Planstatus ist korrekt datiert. Nur bei späterer Bewertung der Lieferfähigkeit gezielt prüfen."
    },
    {
      "owner": "market",
      "claim_ids": [
        "M-GCC-006",
        "M-SA-003"
      ],
      "text": "Datierung saudischer KM-SAM-Deal: AGSI '2024' vs. MoD 'Nov 2023 (Offenlegung Feb 2024)'."
    }
  ],
  "release_readiness": "181 A-Claims, alle geprüft; keine material_errors, keine offenen Korrekturen. Faktenbasis freigegeben; nicht blockierende Hinweise (Skynex 160/182 Mio., X-TAR3D 50/55 km, E37/E34-Einschränkungen, Quellen-Duplikate nicht als Zweitbeleg) bei Bewertung beachten.",
  "claims": [
    {
      "id": "T-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Management-Seite + Jahresabschluss 2025 PDF S.30 geöffnet: Vorstand, Bestellungen bis 31.12.2029/2027, Saal ab 1.9.2025 bestätigt.",
      "fingerprint": "29afb04bbda07ce8762ffca6c82b0aa760406a1c7b27677b181f02e734ff7f74"
    },
    {
      "id": "T-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Bilanz-PM 11.03.2026 (Auszug + Fn.[1] wörtlich), Divisionsseite (Power Systems discontinued) und ESUT 13.03.2026 geöffnet; bestätigt.",
      "fingerprint": "e76afbf71bab8211652facdad6c3eb82da9e881e9ab4b6527f84a0c8686a05fb"
    },
    {
      "id": "T-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Divisionsseite Air Defence geöffnet: Business Units, Standorte Zürich/Rom/Neuss wörtlich bestätigt.",
      "fingerprint": "12beb7e3034b5485413f2b006c4d93cd8d7e8fbdd7b81e5f323a2c52aa2be53b"
    },
    {
      "id": "T-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "RAD-Seite Über uns (DE) geöffnet: Bündelungsaussage, Umfirmierung 1.1.2009, >40 Länder wörtlich; als Herstellerangabe korrekt gekennzeichnet.",
      "fingerprint": "5540e74cbb34228e720a21ce46ea656f4f16b2a902181618b95c9503a847b894"
    },
    {
      "id": "T-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1: neuer Wortlaut gegen JA 2025 PDF S.9/S.26 geprüft – 107.439 TEUR RAD AG, 100.000 TEUR Expal, 34.986 TEUR RMMV wörtlich bestätigt; Fehler behoben.",
      "fingerprint": "651cfcc643dbcd74c06d473f6a17a5b700ddfa9df11ac4824717784d1f59a9eb"
    },
    {
      "id": "T-06",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Bilanz-PM 11.03.2026: 9.935 Mio., 1.841 Mio., 18,5 %, Backlog 63,8 Mrd. inkl. Rahmenverträge wörtlich bestätigt.",
      "fingerprint": "f84417b745c3e9330d8aa16cadd0a3c06a4450277a4985cccf9f28a13abd26c1"
    },
    {
      "id": "T-07",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1: nur Unsicherheitstext geändert (Verweis T-13); Inhalt unverändert bestätigt (Bilanz-PM 11.03.2026).",
      "fingerprint": "28648278890cafcdec75b500d47c17bbfaab930b8910020fbdfeaee4253a6221"
    },
    {
      "id": "T-13",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Neu (Korrekturrunde 1): GB 2025 EN PDF S.91 (Report on expected developments) wörtlich bestätigt – Pro-forma-Umsatz Air Defence 2025 769 Mio. EUR, Marge 17,4 %, Prognose 2026 0,9–1,0 Mrd. EUR, ~19 %. Unsicherheit (Stand März 2026, Pro forma) zutreffend.",
      "fingerprint": "c1d6a337dcc418fc080e994390d17f079413d5c619504a9ea77b242642198651"
    },
    {
      "id": "T-08",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "H1-PM 06.08.2026 + H1-Bericht: 5.227 Mio. (+39 %), OE 786 Mio., Backlog 80,5 Mrd., Prognose 13,7–14,2 Mrd. nach F126 wörtlich bestätigt.",
      "fingerprint": "6638b1f5e42944331272fbd01e59bd331fb4a6a7011b3c5d8a8b1ec4f5cd419c"
    },
    {
      "id": "T-09",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "H1-PM Abschnitt Air Defence + H1-Bericht S.17: 478/295 Mio., +62 %, Nomination 1.534 Mio. (+517 %), Backlog 4.218/2.349 Mio., OE 76 Mio., Marge 16,0 %, ein europäischer + ein internationaler Kunde wörtlich bestätigt.",
      "fingerprint": "4a1d05932fab8681b08e6c113d213b89b5f7927c7803c9e7387f26b6a13c842e"
    },
    {
      "id": "T-10",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "H1-PM Abschnitt Digital Systems: Zitat zu short- and very short-range air defence projects wörtlich bestätigt.",
      "fingerprint": "344ae3087360806f3ee055485dac3658d397920292b7d88ad73640b80305699a"
    },
    {
      "id": "T-11",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Zefix-JSON (SHAB 18.07.2024 Publ. 1006087689; 07.07.2026 Publ. 1006699256), Management-Seite, JA 2025 S.30 geöffnet; bestätigt. Letzte SHAB-Publikation zum Abruf weiterhin 07.07.2026.",
      "fingerprint": "86d7f3d54bd61a985692508042e7c239fb6782450c468fb2c01b3d4dcf539a83"
    },
    {
      "id": "T-12",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Zefix SHAB 14.10.2021 (Publ. 1005312089), DK-PM 30.09.2024 („Leiter … Electronic Solutions Division“), RO-PM 24.06.2026 („Head of Rheinmetall’s Air Defence Division“), ES&T 04.09.2026 (eigener Wunsch) geöffnet; bestätigt. Zusätzlich WOZ 01.10.2026: Dürr „scheidender CEO“ (konsistent).",
      "fingerprint": "e94f6e7329f7a3b3a244be973c4973124359d8f7dd2ecd5c8ffcbdbc3e84770e"
    },
    {
      "id": "T-20",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): DE-PM 27.02.2024 Keyfacts: 595 Mio. brutto, 1+18, Option 30, NNbS-Komponente bestätigt.",
      "fingerprint": "a6e3e8d55312196c0b4c45413244b88fd04af69d408c9ed4690ac41e41400527"
    },
    {
      "id": "T-21",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): DE-PM 30.09.2024 Keyfacts: 16 Türme, niedriger dreistelliger Mio.-Bereich, 2027/2028 bestätigt.",
      "fingerprint": "e26c232a9534707142f4ac6efa13a3f0f30115016195d05bb5fbe4055c6cc47e"
    },
    {
      "id": "T-22",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 05.01.2026: geplantes JV (GmbH dt. Rechts) für Q1 2026, maritime Laser, Weiterentwicklung landgestützt bestätigt.",
      "fingerprint": "80bf591a19e0fff5177ab8ef6c64d1242c8b4aeb0af9be3337e22ac91fc06781"
    },
    {
      "id": "T-23",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "defence-network.com 11.03.2026 geöffnet: Papperger-Zitat „weit über 100 Drohnen … über das Wochenende in Middle East“, Länder nicht genannt; Systeme genannt. Bestätigt als Medienwiedergabe einer Unternehmensaussage.",
      "fingerprint": "242de9a9420b880bc2c967b496a72bc296ff672c81106d64c6de8f9c4cbf66e6"
    },
    {
      "id": "T-24",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Eurasia Review (EurActiv-Republikation, 21.03.2026) geöffnet: Zitat „empty or nearly empty“ bestätigt; CNBC-Original nicht geöffnet (im Claim offengelegt).",
      "fingerprint": "5d7ac72bca86f07a3b3006c48de77c08835d9e2d603ceaefedafc917d0cfbb45"
    },
    {
      "id": "T-25",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "BusinessAM 10.05.2026 geöffnet: ~150 Skyranger/Skynex in Region, ~10 an Golfstaaten 2026, Verdopplung bis Ende 2027, total ~400; Link auf Bloomberg-Artikel 2026-05-08 im Quelltext vorhanden (Datum damit belegt). Interne Inkonsistenz korrekt offengelegt; nur Sekundärwiedergabe.",
      "fingerprint": "33a7238acbb91006c17c5be60aae70f3507ee7c380050225141f72d6bea43dde"
    },
    {
      "id": "T-26",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Korea Times 16.06.2026 (Article-Body im Quelltext) geöffnet: Partnerschaft, JV-Gespräche, gemeinsame Entwicklung eines neuen Kurzstrecken-FK, Dürr als CEO RAD, Sonntag/Montag-Widerspruch bestätigt.",
      "fingerprint": "8ef897964652a3371dc64919068ef96f6f5e2b27b0ce3e69367ba21618442a91"
    },
    {
      "id": "T-27",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Korrekturrunde 1: PM 24.06.2026 (Umfang) und H1-Bericht PDF S.10 (Vergabe 29.05.2026, SAFE) geprüft; event_date 2026-05-29 korrekt; Fehler behoben.",
      "fingerprint": "b105779d5d27e669f865918c0a4c0866fad1f7c035ca9072773c1055be249cb4"
    },
    {
      "id": "T-28",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 02.07.2026: vier Skynex, mehrere hundert Mio., Q2 2026, Erstkunde, Rheinmetall Italia GU bestätigt.",
      "fingerprint": "3e1b96729d8514206faf218d78be865e18d46362212075d190465df0488d316d"
    },
    {
      "id": "T-29",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 07.10.2026 (EN/DE): Prototyp in 12 Monaten, Demonstrator, Arrow/Hadrian bestätigt; kein Kundenauftrag.",
      "fingerprint": "62686257bffb7615829489778b427e60b5078686035eb216975b741b366da1d2"
    },
    {
      "id": "H-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Rheinmetall-Karriereseite (o. D.) geöffnet: „Starting in October 2026, … serves as CEO of the Air Defence division, headquartered in Zurich“ wörtlich; ES&T 04.09.2026: zum 1. Oktober Nachfolge Dürr. Identität/Rolle bestätigt; Gegencheck: RO-PM 24.06.2026 Dürr noch Head of Division, WOZ 01.10.2026 Dürr „scheidender CEO“, Zefix ohne Köhne-Eintrag (Registerstand 07.07.2026). Amtsantritt durch Unternehmensseite gedeckt; Datum 01.10. nur laut Fachmedium (korrekt gekennzeichnet).",
      "fingerprint": "631be6edc081a0f31ad1fb4b0792aaad85377efc7d8c6332ba2db8d6fc968425"
    },
    {
      "id": "H-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Karriereseite („Previously … CEO of the Weapons and Ammunition division in Unterlüß“), ES&T (2025 Übernahme) und PM 05.01.2026 (Zitat „Head of Rheinmetall’s Weapons and Munitions division“) geöffnet; bestätigt. Nachweisdatum vs. Eintrittsdatum korrekt getrennt.",
      "fingerprint": "b48b72e36b27aa0f43b65c5d6179e18a9c1fecd55389fd611824ce9443428611"
    },
    {
      "id": "H-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "ES&T 04.09.2026 Werdegangsabsatz wörtlich bestätigt; nur Sekundärquelle, keine Jahreszahlen (korrekt offengelegt).",
      "fingerprint": "37453d39a295748a14669136c5968ccd48c38c9450a20636c70c6983e3a91f7a"
    },
    {
      "id": "H-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Karriereseite: „track record of success in Germany, South Africa, and Spain“ bestätigt.",
      "fingerprint": "8c7223fb3a63480e84a2d90e7d87b80623cd4dec9b5e0d0a458e1c411ca244ce"
    },
    {
      "id": "H-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Karriereseite: Besuche Zürich/Rom/Neuss, Fokus Kapazitätsausbau und bodengebundene Luftverteidigung wörtlich bestätigt (Herstellerangabe).",
      "fingerprint": "0bb6d70e06420c6bbe3fa8487d2f906cb49dbb0486dbdd176425d5b409d81382"
    },
    {
      "id": "P-AD-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Divisionsseite: Standorte und Produktlisten je Business Unit bestätigt.",
      "fingerprint": "bc1226fd711ca009e4ec63650e0ac968fe4d322e5d0fc81cb5e08c270d2b4636"
    },
    {
      "id": "P-AD-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "RAD About-us (EN): 2009 Umbenennung, Marke Oerlikon, >40 Nationen, Ochsenboden bestätigt.",
      "fingerprint": "3b20ebe596b7e5bd614fd4846f2604be1d75df6608872a267cdcd66d1fc14725"
    },
    {
      "id": "P-AD-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "H1-PM: Air-Defence-Werte und Begründungssatz wörtlich bestätigt (gemeinsam mit T-09).",
      "fingerprint": "e53db1debd4b91ce4da85ec77d63d9a55e44cbfa8f5ffb45c2b621ab9a1bb7d8"
    },
    {
      "id": "P-SR-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Produktseite Skyranger: 35 mm C-RAM bis 4.000 m, 30 mm bis 3.000 m, FK-Turm, HEL/C-PGM „being explored“ wörtlich bestätigt.",
      "fingerprint": "c7fca91be932129292e83e432cd5ea0bca6707efa243f939cb31d1910e137ce3"
    },
    {
      "id": "P-SR30-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 27.02.2024 EN: 595 Mio. inkl. MwSt., 1+18, Option 30, Stinger, NNbS bestätigt.",
      "fingerprint": "1137e6a31d45435d2a1ca14697e4b2a5be67c0a1e24e1b015f2f7a4c3128f133"
    },
    {
      "id": "P-SR30-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 05.02.2025: Nachweismuster Ende Jan 2025, Zulassungserprobung Frühjahr 2025, Serie überwiegend 2027/Anfang 2028, Stinger → Drohnenabwehr-FK bestätigt. Hinweis: Medien (u. a. Stern via Sekundärdienst, März 2026, nicht geöffnet) berichten Verzögerung; Planstatus bleibt korrekt datiert.",
      "fingerprint": "afd31773e14ec6713412eb7b53bae7136428f0a654c5c05d82a125727876b62a"
    },
    {
      "id": "P-SR30-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 23.02.2024: 36 Skyranger 30 auf Pandur EVO, Unterauftragnehmer GDELS, Mistral, Lieferbeginn 2026, erster Serienauftrag bestätigt.",
      "fingerprint": "0e7d915880d71f6ce59ae5deba4378f41790bfb68dc0258ea5b1e4ceff67bed4"
    },
    {
      "id": "P-SR30-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 30.09.2024 EN: 16 Türme + Integration 8x8, Munition, Prototyp Ende 2026, Serie 2027–2028 bestätigt.",
      "fingerprint": "760cb8906a11fc78001b88257213c434922705546e912f9d6f08cf1a7a0b23ca"
    },
    {
      "id": "P-SR30-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 12.12.2025 (zweistellige Zahl, hoher dreistelliger Mio.-Bereich, Ende 2028–Ende 2029, Führungsknoten, Hakenlift) und PM 05.02.2025 (Ankündigung 22 Systeme Jan 2025) bestätigt.",
      "fingerprint": "cab52b2a7ab70e00aa03d3391a07fdd4279246f00f19136003f0c16fd2834650"
    },
    {
      "id": "P-SR30-06",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 20.12.2023: Vertrag 15.12.2023 Budapest, knapp 30 Mio., Mistral/Stinger/Chiron bestätigt.",
      "fingerprint": "398af4be4822688a549a48a6cd7a12020bf65879aadd41e00623be56547bd918"
    },
    {
      "id": "P-SR30-07",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 11.01.2024: A1-Testkampagne Dez 2023 Ochsenboden, A3-Qualifikation Mitte 2024 geplant bestätigt.",
      "fingerprint": "f4ee9b909f60495bc426eee68e7d98bde5d0fd7ad9bc3fab8c8e3903d5126866"
    },
    {
      "id": "P-SR30-08",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM ILA 10.06.2026 und Eurosatory 15.06.2026: DefendAir auf Boxer, Lynx-Präsentation, 70–100 Türme/Jahr → bis 400, Deutschland 19 Fahrzeuge bestätigt. Bundeswehr-Zahlen konsistent (1 Prototyp + 18 Serie = 19, vgl. P-SR30-01/C-028); kein abgeschlossener Großauftrag belegt.",
      "fingerprint": "4120a69cc0bbf7fd529c33753e2d9783ab8c0e951bae980a215abdd36cd3c293"
    },
    {
      "id": "P-SR30-09",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 05.06.2024: LOI Rheinmetall Electronics/MBDA Deutschland zu SADM bestätigt.",
      "fingerprint": "5f8d2a76c3961aea376be76858861702238b8bb8ef68ebc8448faa797393ccf0"
    },
    {
      "id": "P-SR30HEL-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 04.02.2022: 20 kW Technologiemuster, 20–50 kW geplant, armasuisse Bure bestätigt.",
      "fingerprint": "e934e76af9126716412915778b261649dfba0736f7d4838f16f3b1c019e7f01a"
    },
    {
      "id": "P-SR35-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 09.09.2025: KDG 35/1000, 1.000 Schuss/min, 4.000 m, Gleichteiligkeit Mk3, AHEAD, DSEI-Erstpräsentation bestätigt.",
      "fingerprint": "4eb4b62b72f0ca37d3e847351c6c0bb9d0e457e95dbfb8fdff4345193be18538"
    },
    {
      "id": "P-SR35-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 10.10.2025: Leopard-1-Skyranger-35, dreistelliger Mio.-Bereich, EU-Land/eingefrorene russische Vermögen, Rheinmetall Italia Rom bestätigt.",
      "fingerprint": "d3e4dbb42c238fbee9414a0057e92150d4042d1fc3a88656dc256e0f40070da9"
    },
    {
      "id": "P-SR35-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 24.06.2026 (24 SR35, 7 Skynex, 2 Millennium) + PM 02.06.2026 (29.05.2026, SAFE, 2028–2030, Gepard) bestätigt.",
      "fingerprint": "735cfb65ce345dca9ca4e20f781dc4277f1bbe820a4e2570ccc9cc3fd1dc55c3"
    },
    {
      "id": "P-SR762-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 09.09.2025: U-SHORAD-RWS, M134D 7,62x51, Skymaster-Anbindung bestätigt.",
      "fingerprint": "e96e9fba4d0dc1cf2e817087140b188440088c4fb8b573ecfa82cd62d9e2976d"
    },
    {
      "id": "P-SNX-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Produktseite Skynex: Skymaster als Kern, Effektoren, Fremdsensoren, Skyguard/Skyshield-Anbindung wörtlich bestätigt.",
      "fingerprint": "40d76053062aad9343c4e302fa82bb0ce809f49889a4f7266fa91e0cfa6fdb08"
    },
    {
      "id": "P-SNX-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 09.12.2022: zwei Skynex, ~182 Mio., Lieferung Anfang 2024, HX-MoU ~12 Mio. bestätigt.",
      "fingerprint": "721883e44c309012847534ea2782787e6cb6fcff8d4fad3bfe1ac3df5b5b3044"
    },
    {
      "id": "P-SNX-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Defense News 26.01.2024 (Ercolani: Lieferung 31.12.; ~160 Mio., Dez 2022), PM 23.12.2025 und PM 06.01.2025 (Ukraine mit Skynex beliefert) geöffnet; bestätigt. Widerspruch 160 vs. 182 Mio. (P-SNX-02/C-037) besteht in den Quellen fort und ist korrekt offengelegt; Wert nicht als Fakt für Bewertung nutzen.",
      "fingerprint": "1087016901cf9eb574b46dfe2440ebc9804e0bda772bee5acc2f8a97f51f2202"
    },
    {
      "id": "P-SNX-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 01.03.2024: europäischer Kunde, unterer dreistelliger Mio.-Bereich, Lieferung 2025 bestätigt. Zusätzlich: Lieferung 2025 inkl. HX-Lkw bestätigt.",
      "fingerprint": "dc969c88aaa14e835a8948414584c113b7dcc28929dd9e6134ee3873e17279cb"
    },
    {
      "id": "P-SNX-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 23.12.2025: Übergabe 18.12.2025 Sabaudia, 73/204 Mio., X-TAR3D bis 50 km bestätigt.",
      "fingerprint": "c2409f726642d8089ef55d092919dc76e0fbb01cde87ded3efe8291363d2d9bc"
    },
    {
      "id": "P-SNX-06",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 02.07.2026: 4 Systeme, 39/21 Monate, GU Rheinmetall Italia, beteiligte Gesellschaften bestätigt.",
      "fingerprint": "7b73ee265835b6477dbc02776d866aebba7b57c50146459672ed43930773b066"
    },
    {
      "id": "P-SNX-07",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 19.08.2026: Twinvis in Skymaster, Timber Express Manching, Link 16 bestätigt.",
      "fingerprint": "27fe973143a82ed0346efde89fc475188e250d1c677f7b9621c139cf8d38d68e"
    },
    {
      "id": "P-SNX-08",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Skynex-Produktseite (SkyKnight Missile Launcher Unit, 10 km, bis 60 FK/Werfer) und EDR 08.03.2021 (Halcon/EDGE, Integration in Skynex) bestätigt.",
      "fingerprint": "4533fffa7a075a5814f819860e7933b5fb82d25a162c2e058014c8667f542abf"
    },
    {
      "id": "P-SNX-09",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 14.10.2022: QEADF, Video 13.10., acht Revolver Gun Mk3, ein X-TAR3D, „Shield 6 (Skynex)“, 2019er 210-Mio.-Hinweis bestätigt (Komponenten laut Janes auch Skyguard/Skyshield-fähig).",
      "fingerprint": "cf140a8f6ae6c1065ec3bacfbc55abba0b55c4f4160a1a136eec6847846e22f4"
    },
    {
      "id": "P-SNX-10",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gezielte Nachprüfung: Army Recognition 20.01.2026 – „At the Qatar Emiri Air Defence Forces booth … a Rheinmetall Oerlikon Skynex configuration centered on the 35 mm gun effector“ wörtlich bestätigt; Skymaster/X-TAR3D-Standaussage entfernt, Unsicherheit zutreffend. Korrektur behoben.",
      "fingerprint": "f6dd8a0cc753ad805569395339fa067e95477909b8df025b4a3e58c08cecc160"
    },
    {
      "id": "P-SNX-11",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 30.10.2019: ~210 Mio., Skymaster/X-TAR3D/Mk3/AHEAD, Lieferung bis 2022 bestätigt.",
      "fingerprint": "2ccec9586e25b2d6558079dbeb94f13ca8de2ecea04d8229c6941a66bd78796a"
    },
    {
      "id": "P-SG-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Produktseite Stationary air defence: Skyguard 3 bis 4 Effektoren, Skyshield bestätigt.",
      "fingerprint": "a00532b26f4e8e16bf44d6d605fe042975c4ab1252ec81e069b0ae4a8507813c"
    },
    {
      "id": "P-SG-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 12.12.2023: 532 Mio. ohne MwSt., 48 Monate ab Feb 2024, 7 Einheiten à 4 Geschütze, 28 Bestandsgeschütze, AHEAD, Werk Zürich bestätigt.",
      "fingerprint": "684994d6d39d479f8002f11d3daf0f1396958d0143100c3aa950dcc574b784c9"
    },
    {
      "id": "P-SG-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 22.12.2023: GDF 103, ~328 Mio., vier Systeme bestätigt.",
      "fingerprint": "6ee45dae8aa767994c7f852e05fc1e8adc98dfd627c2c0d9af9ccf3a8dbfab60"
    },
    {
      "id": "P-SG-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 09.12.2019: ~120 Mio., Drohnenabwehr, Lieferbeginn Q3 2020 bestätigt.",
      "fingerprint": "2ae621bd57f879e2518b5ed0e1de17313ba37447eb47ecf21f7fd413917f449d"
    },
    {
      "id": "P-SG-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 26.02.2020 (gleicher Artikel wie S-57816f4227585f45): SPA-Foto, Satellitenbilder Juni–Juli 2019, BDF-Foto 2019, ältere Skyguard-Betreiber bestätigt.",
      "fingerprint": "857c56a4c709db8c16ef795847bcc14a386a1c0e3349d74cae888c06bea008b4"
    },
    {
      "id": "P-SG-06",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 07.03.2022: Radarabia, WDS 06.03., 25.000 sq ft Jeddah, MRO Skyguard RSADF, 60 % Lokalisierung bestätigt.",
      "fingerprint": "77f52ef223a4bec9ecff0705e91d525ec7eaccfde670b7537f62aa8c61fe583e"
    },
    {
      "id": "P-SS-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 23.04.2018: asiatischer Kunde, >100 Mio., Wettbewerb bestätigt. Zusätzlich: Sensoren, 35-mm-Feuereinheiten, Führung, Logistik/Ausbildung bestätigt.",
      "fingerprint": "6312b7613052b054f23c9258819dba919fcb1e6eb73cf88402e04f4f25996905"
    },
    {
      "id": "P-RG-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Skynex-Seite (Mk3: X-Band-Folgeradar, 6x6) und Seite Medium calibre cannons (STANAG 4516, Einbauten) bestätigt.",
      "fingerprint": "be1569211d2914e16b2b557e74f9bcfabc7a31a9acd23f654de8a996cabc083e"
    },
    {
      "id": "P-XTAR-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Skynex-Seite „25, 35 and 50 km instrumented range“ und Stationary-Seite „25, 35 and 55 km“ wörtlich bestätigt; Widerspruch 50/55 km liegt in Herstellerquellen selbst vor und ist korrekt offengelegt; Reichweite nicht als eindeutigen Wert verwenden.",
      "fingerprint": "062f0c1289fc1ef56506d3ce30545dd944c5b06c6197fe905e34e2116821eeac"
    },
    {
      "id": "P-MSU-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Skynex-Seite: 30 km (1 m² RCS), Schnittstelle Skymaster bestätigt. Zusätzlich: nicht rotierende 3D-AESA 360°, panoramische EO-Sensoren bestätigt.",
      "fingerprint": "dee351f3d2f2919d9919e51e2957c5da24f91cf0d31067582bd9ca4e4aa0b35f"
    },
    {
      "id": "P-SM-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Skymaster-Seite (taktische/operative Netze, Multi-Spektrum) und Toolbox-Seite (Fusion) bestätigt.",
      "fingerprint": "c988ab06aaf35814df3d2771b5a523e1f68715d61146131afe4418e4795d8d3f"
    },
    {
      "id": "P-SSP-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 15.06.2026: Multisensor-Frühwarnsystem, Flughäfen bestätigt. Zusätzlich: Erkennung, Identifikation, Verfolgung wörtlich bestätigt.",
      "fingerprint": "d786b06cac426c9787cd2e6f0676c105237d4ddabf336011743cffa3120c2e29"
    },
    {
      "id": "P-SSP-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 16.12.2025: Lohtaja, HX-Variante, PEL, C2-Shelter, 30 mm in Konzeptphase bestätigt. Zusätzlich: Einladung durch finnischen Flugabwehrinspekteur, KETF-Munition bestätigt.",
      "fingerprint": "c7918d511d0a707b9eedf796a2cb8f3eb002fdcfb2b89c0d5741323a7942fef5"
    },
    {
      "id": "P-AH-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Produktseite Medium calibre ammunition: 152 Subprojektile, ABM 30x173/35x228 bestätigt.",
      "fingerprint": "c822a1b6e93d792d1b4a1096e1d07bab9f73c0006c90011f89bc5fb17971734d"
    },
    {
      "id": "P-AH-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 28.05.2024: europäisches Kundenland, niedriger dreistelliger Mio.-Bereich, sechsstellige Patronenzahl, Skynex bestätigt.",
      "fingerprint": "96dfff3bacd3302838a622457a66d8f3b44c6ce46e8c10db37a529af31da91d7"
    },
    {
      "id": "P-GP-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 05.09.2023 (300.000 Schuss, erste Lieferung) und PM 06.01.2025 (180.000 HEI-T, Dez 2024, hoher zweistelliger Mio.-Bereich, finanziert durch Deutschland, Lieferbeginn 2026) bestätigt.",
      "fingerprint": "25f105b89a658965c30adbbb0aa18ba1b793966c1564fdd2f6e5476d16b8ee5f"
    },
    {
      "id": "P-HEL-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 27.10.2022: Einsatz 30.08.2022 Sachsen, Arbeitsteilung MBDA/Rheinmetall wörtlich bestätigt.",
      "fingerprint": "fab9c45cb3312317281647699987020ea9b3ccf2b49f3d823d4d6396266704bd"
    },
    {
      "id": "P-HEL-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 22.09.2023 (6 Kampagnen, >100 Schuss) und PM 28.10.2025 (WTD 91 Meppen, landgestützte Drohnenabwehrtests) bestätigt.",
      "fingerprint": "9d90acfb697be855eb09a8503912b8cf73ee0a022616bd1a7d9166edd7ad6e6f"
    },
    {
      "id": "P-HEL-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 09.07.2026 (EN) und PM 05.01.2026 bestätigt; JV „currently forming“.",
      "fingerprint": "c83bf68447a6c7b9d24149980441c05c1c7f14f8ab65d038c2d8a97ed4584369"
    },
    {
      "id": "P-CUAS-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Toolbox-Seite: Sensoren, Skymaster, Jammer verfügbar, Fangdrohnen künftig bestätigt.",
      "fingerprint": "e3fdeb890ebfc47da4f958df66dc2cdbad9b5d8a7fa9c0e1db7c9ee0be6bd1cb"
    },
    {
      "id": "P-CUAS-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Produktseite RCWS320C-UAS (NGVA, SEOSS, UGV, Container) und PM 23.02.2026 (Dillon Aero M134D, Enforce Tac) bestätigt.",
      "fingerprint": "f7726375543d99f9cd8fb14fee1de75095aa41ec1adc8523f5a1707e516b128f"
    },
    {
      "id": "P-CUAS-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 15.06.2026: Hermelin, Path-Kit, FN DeFNder Medium M3M bestätigt. Zusätzlich: 6x6, mit/ohne Besatzung bestätigt.",
      "fingerprint": "6b31e9ef328cedfc6999e1bd0d484004195c85eec0e0bc837f54506468763984"
    },
    {
      "id": "P-CUAS-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 07.10.2026 (DE): Container, >20 Abfang-FK, Arrow/Hadrian, Prototyp 12 Monate bestätigt.",
      "fingerprint": "8e09f683acc1592f84c460fe8cd30f2d735dab3eb70a9ef1ec3df6fe07c48a7f"
    },
    {
      "id": "P-CUAS-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Gemeinsame PM 11.05.2026: Absicht gemeinsamer Abwehrschirm, Details später bestätigt.",
      "fingerprint": "dedc512ae8aa80f1ddaf8b6c441075d4bad4d9832993bc9bdf8e1e93b4a6809b"
    },
    {
      "id": "P-NNBS-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 25.01.2024 EN: ~1,2 Mrd. inkl. MwSt., 607/339/284, IRIS-T SLM und Skyranger 30 bestätigt.",
      "fingerprint": "5412face2d0238b1d2374e36da604754b195d6e9981ea9808780e5511f9b158f"
    },
    {
      "id": "P-MG-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Produktseite Naval air defence: 252 Schuss, 1.000/min, land-C-RAM, TRL 9, Searanger/Seaguard bestätigt.",
      "fingerprint": "966fcde9c4c8a2da0247c1c50e986d5a6c55b89985d20cc71a584764a1cb98c2"
    },
    {
      "id": "P-MG-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "ESD 16.10.2023: Iver Huitfeldt/Absalon, Indonesien, Al-Jubail (Royal Saudi Navy), Venezuela, SIGMA 10514 bestätigt (Sekundärquelle ohne Einzelnachweis, korrekt gekennzeichnet).",
      "fingerprint": "6bc5383322be26c5b8dd3c1b861f4370dc0c4d1336a2fff70db7ac4c3554d0ce"
    },
    {
      "id": "P-MASS-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 10.07.2026: Kuwait erstmals MASS, 8 Boote Al Dorra, ADSB für EDGE als GU, Omnitrap, Q2 2026–Q2 2029, Wertangaben (niedrig zweistellig + hoch einstellig = mittel zweistellig gesamt) bestätigt.",
      "fingerprint": "4ffdaf66677c80d4d07c0897cde2a4ad44e60e957213eb361a528a4c6f5bbca3"
    },
    {
      "id": "P-GULF-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 11.05.2026: „Effectors … currently in use in Ukraine and the Middle East“ wörtlich bestätigt.",
      "fingerprint": "7e5ae4fd33f331e76de07e6d4eb2746ea392ce4c572e698c24df36fb4f80e96b"
    },
    {
      "id": "P-GULF-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Soldier Systems Daily 15.02.2019 (Drittanbieter-Kopie, Rubrik Press Release): Skynex mit Mk3 auf HX77, X-TAR3D, Cheetah, HEL bestätigt.",
      "fingerprint": "d09f1e8032489fbfc02790f867d7a028405127cdf70d3b8de804d7c973cfad09"
    },
    {
      "id": "C-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2025 PDF S.259 (Anhang 41) und S.91, H1-Bericht S.38 geöffnet; Aufteilung zum 01.01.2026 bestätigt.",
      "fingerprint": "f019d239d1315f473d5a7fe1d5247cde6c8fc27b3eef97f42c76f88a8df357f1"
    },
    {
      "id": "C-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2025 PDF S.262: RAD AG 100 direkt (EK 386.181, Erg. 117.135), RAD Germany 100 indirekt; GB 2024 S.246 RAD AG 100 direkt bestätigt.",
      "fingerprint": "db396b946e1e18d3a7508da80ae01e3f4ba325ff768c1b0cfc56cf784dad45d6"
    },
    {
      "id": "C-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "RAD About-us (EN): Bündelung, Umbenennung 2009, Marke Oerlikon bestätigt (Herstellerangabe, Abgleichhinweis korrekt).",
      "fingerprint": "82f5c15ec52ed980feadaa5496efee4a30e90ceffdc04a21210e72be9dcae694"
    },
    {
      "id": "C-004",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "HLS-Artikel „Contraves“: „1999 veräusserte die Oerlikon-Bührle den Rüstungsbereich der C. an die dt. Rheinmetall-Gruppe“ wörtlich bestätigt.",
      "fingerprint": "a8b8fd143c009f64b922f5156ef9e264bb113694f7062c9ef9301d0c406798b0"
    },
    {
      "id": "C-005",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2025 PDF S.263–265: Canada 100 direkt, RDM 51 indirekt, Electronics 100 direkt, Italia 100 indirekt (S.264), Waffe Munition 100 direkt (S.265) bestätigt.",
      "fingerprint": "1137f61aa6bc914f4b5926464af77f0a4ec2e0a1559eb7ae9d7207aff6961552"
    },
    {
      "id": "C-006",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2025 PDF S.264 (Riad 100 ind., Abu Dhabi Services 100 ind., RPDC 49 direkt mit Fn.(2), Sharjah 100 ind.) und Fn.2 S.266 „majority of voting rights“; GB 2024 S.244–246 alle vier enthalten. Kapital vs. Stimmrechtskontrolle korrekt getrennt.",
      "fingerprint": "1dcb38ff7ead20a40eb718c5831198c7e398589e72eebfc4c57893f9b527639b"
    },
    {
      "id": "C-007",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2025 PDF S.265–266 (at equity): RADARABIA 20 ind., RAST 40 ind. (Fn.5 JV), RBAT 49 ind.; GB 2024 S.248 identisch bestätigt.",
      "fingerprint": "9036cf8ae2a304ca26defb680045a77e157d1d9d2b1c491c4ff1094378981bad"
    },
    {
      "id": "C-008",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Aviation Week 07.03.2022 (JV RADARABIA, 25.000 m², Produktliste) und Argaam (RAD Arabia, Jeddah, 25.000 m²) geöffnet; bestätigt.",
      "fingerprint": "09b7b156e0daded04743522eea047528f22e0f549ff13a3d30ecb612e5346b03"
    },
    {
      "id": "C-009",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 07.03.2022 (25.000 sq ft, MRO Skyguard RSADF, 60 %, künftige Arbeiten) und Aviation Week (25.000 m²) bestätigt; Widerspruch Flächenangabe korrekt offengelegt.",
      "fingerprint": "08518545303840a90952a60b7b229903e4786112e4395e0579d08d23279117af"
    },
    {
      "id": "C-010",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 26.02.2020: Erwerb durch SPA-Foto bestätigt, Installation Juni–Juli 2019 bestätigt.",
      "fingerprint": "0b0206e1e0a7bcf00e3abb4419c65cbb1e4269d8aff1e36aa5000128c4db68f9"
    },
    {
      "id": "C-011",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Defence Industry Europe 18.12.2024: Red Sands III Sept 2024, Shamal 2, Fieldranger Multi/Mission Master XT, USARCENT + saudische Streitkräfte bestätigt.",
      "fingerprint": "a3c0078cfa796107d970eeab916d58718faf3c9ae8dafd1008ab569d1dc697f6"
    },
    {
      "id": "C-012",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "H1-Bericht PDF S.43: weitere 60 % Anfang Juli 2026, 100 % Anteile und Stimmrechte, 81 Mio. EUR, Digital Systems bestätigt.",
      "fingerprint": "b7dd5cd7467c5d2f062d1b970476f0656e8842eeef625b7f35d1856becbe43b6"
    },
    {
      "id": "C-013",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Arab News 08.02.2024: Vereinbarungen u. a. mit RAST und Rheinmetall Expal bestätigt; Inhalt nicht genannt (Netzwerkkante → A).",
      "fingerprint": "f8e1632297b134db94b6ec7885eac05f84151867bad9e9983d978909d77edf5e"
    },
    {
      "id": "C-014",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Defense News 06.04.2016: RDM und SAMIC eröffnen Werk Al-Kharj; Produktspektrum bestätigt (Quelle spricht von „joint weapons factory“; historische Kante, Status korrekt).",
      "fingerprint": "ce458c401ae29073f965305bcc191679f7d60b996595a17db3336d93d073ceb4"
    },
    {
      "id": "C-015",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gulf Times 15.03.2018: RBAT = JV Barzan Holdings/Rheinmetall AG, Notice to proceed Munitionswerk, Vereinbarung QENF Infrastrukturschutz bestätigt.",
      "fingerprint": "7a75fbb49ca151f1f50ce1644ecc12244f5827127b83c4ad1283a59e1f4617e2"
    },
    {
      "id": "C-016",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 15.12.2022 (frei lesbarer Teil): „Rheinmetall has confirmed that the first Skynex systems it supplied were for Qatar“ bestätigt.",
      "fingerprint": "e699481852b4a93a1296bc8d618b7fec36f966e0aed4e4de64ba93a4f7d17911"
    },
    {
      "id": "C-017",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Beobachter (JSON-LD datePublished 2021-06-03) geöffnet: Fertigung Zürich-Oerlikon, zwei Flugabwehrsysteme nach Katar, ~200 Mio. Franken, EDA-Einschätzung, Ausnahmeregel KMV 2014 bestätigt. Hinweis: Veröffentlichungsdatum ist im Quelltext ermittelbar (Registereintrag null).",
      "fingerprint": "711f8a365978585db9ee14b93a719269b0a559083e9c9cf91033e1f6e9f7939a"
    },
    {
      "id": "C-018",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Army Recognition 20.01.2026: QEADF-Stand DIMDEX 2026, Okt-2022-Enthüllung bestätigt (Netzwerkkante E24 → A).",
      "fingerprint": "80a3198bf6f02286a1fe44665142f7cd293b2bdbd2f272be1db160efa0166258"
    },
    {
      "id": "C-019",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "australiandefence.com.au 23.01.2013 (Wiedergabe): Kuwait setzt seit Jahren 35-mm-Skyguard ein, Ausbildungsauftrag, ~280 Mio. für drei Länder bestätigt.",
      "fingerprint": "42683a53dc370bd2945f9b1c9ebdfa517c82d9b034d72ebdc12789d133ffa2f4"
    },
    {
      "id": "C-020",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 10.07.2026 (rheinmetall.com ohne www; identisch mit S-a831015ab01561c0): Kuwaiti Naval Forces, MASS, Omnitrap, Al Dorra, ADSB/EDGE GU, Q2 2026–Q2 2029 bestätigt.",
      "fingerprint": "2ca2d172c2e489fefc78ba031a4eda76a41778af4fca82289a7c245cff397c74"
    },
    {
      "id": "C-021",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gulf News 23.02.2021 (Lieferung an Rheinmetall, gemeinsames C-RAM-Angebot) und Breaking Defense 24.02.2021 (Integration durch Rheinmetall, Demonstrator ~3 Jahre, VAE erster Kunde) bestätigt.",
      "fingerprint": "b75cb76ecad48f6dfd5f15220f6c8d9af8e7d69cfdce067f2224fe7c535fe903"
    },
    {
      "id": "C-022",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Diehl-PM 19.02.2025 und Diehl-GB 2025 PDF-S.22 geöffnet: MoU Diehl Defence–EDGE bestätigt; keine Rheinmetall-Beteiligung (Überschneidung) korrekt (Netzwerkkante → A).",
      "fingerprint": "9c3a12169b24c3c955247cc1c7f6260e21ce9ff94856e0d9551d851be9988ee4"
    },
    {
      "id": "C-023",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Arab News 21.02.2023: 15,5-Mio.-USD-Vertrag mit Rheinmetall (Gefechtssimulation) bestätigt.",
      "fingerprint": "35589e565b9684bcd92609b031a1b477c13300b9c4237c991065b610b13ba559"
    },
    {
      "id": "C-024",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1: hib 491/2026, Heuking 26.03.2026 und BAFA-Seite AGG 48 (Bekanntgabe 10.09.2026, gültig bis 15.09.2027) geprüft; event_status/Unsicherheit, depends_on M-EXP-002, G04 und Coverage konsistent; Widerspruch behoben.",
      "fingerprint": "a5983aaef646b1d5a14eb7970096e8dcf5571c9406fedea7cf7582658a7bf7d0"
    },
    {
      "id": "C-025",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): GB 2025 PDF S.27: Endverbleib, Reexportvorbehalt, Post-Shipment-Controls bestätigt.",
      "fingerprint": "7da9f69851ac8c7050bda82174f9404468231d269155f1b2504a090144449233"
    },
    {
      "id": "C-026",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): PM 02.07.2026 und H1-Bericht S.17 bestätigt.",
      "fingerprint": "c7492ac1f5900fbfddf09b410537ea0438de42521c48eff45b5a44e5f08abe18"
    },
    {
      "id": "C-027",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 25.01.2024 (DE), GB 2025 S.266 (ARGE NNbS 33, Joint Operations), GB 2024 S.62, Hensoldt-AR 2025 Kopie PDF-S.32 geöffnet; bestätigt.",
      "fingerprint": "7933787cdd80d104253ebe75c4a8db9699aee1d892185666378dc4b9b6f7a288"
    },
    {
      "id": "C-028",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "DE-PM 27.02.2024 und GB 2024 S.48 bestätigt.",
      "fingerprint": "b14dc6739619d993093fb8d8f4e03870058b378d4a3f7f13088af475f1b7669d"
    },
    {
      "id": "C-029",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "BMVg 06.11.2025 (Rahmenvereinbarung mit Festbeauftragung SADM für Skyranger 30, bis 2032) und Defense News 06.11.2025 (Produktion durch MBDA/DefendAir, Werfer im Turm, 9–12 FK) bestätigt.",
      "fingerprint": "c107f1a32cc76cf61585ce81c23222cc67e3e4fb4aa79a47d9b37e0af3cdc427"
    },
    {
      "id": "C-030",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 23.02.2024 und GB 2024 S.48 bestätigt.",
      "fingerprint": "c2bf4281ba91b2212e2eb869f382600781e8e5afcef5f164fd1ea9ccdcd6d0a2"
    },
    {
      "id": "C-031",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2024 S.49 wörtlich bestätigt.",
      "fingerprint": "dac01f95b41ed81f40c275e2100ea87384b2b07e9a4af48de781ab6b7adef0d5"
    },
    {
      "id": "C-032",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 12.12.2025, ESUT 12.12.2025 (Bestellung 11.12., ACSV/FFG, drei Prototypen Rheinmetall Schweiz, Ede) und GB 2025 S.39 bestätigt.",
      "fingerprint": "5f13d44b60a1460903bdb167fff5a33e92bf0572ed44094535aca57d041cc9f3"
    },
    {
      "id": "C-033",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2024 S.21 wörtlich bestätigt.",
      "fingerprint": "6ce31245b539ddc0ec1b11d2910ccb8ae88cf047b16e193d81e62d7fc0459492"
    },
    {
      "id": "C-034",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 15.01.2025 und GB 2025 S.39 („introduced in Italy“) bestätigt.",
      "fingerprint": "c64e9a889c7462befa2fe88fb370db2677bc0840399b37eb2c3ddd612cbad23e"
    },
    {
      "id": "C-035",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 24.06.2026 und H1-Bericht PDF S.10 (29.05.2026, SAFE, 5,7 Mrd. Nomination) bestätigt.",
      "fingerprint": "9c7cb9c629a4dc39075a1f22eb8ccab8d034ccaa05a376aaee12a9a0737f5258"
    },
    {
      "id": "C-036",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "ESUT 10.10.2025: Vertrag geschlossen, dreistelliger Mio.-Betrag, EU-Mitglied, „Windfall Profit Mechanism“, Rheinmetall Italia Rom bestätigt. Hinweis: ESUT erläutert Mechanismus als Energie-Übergewinne, Rheinmetall-PM (P-SR35-02) als Erlöse eingefrorener russischer Vermögen – Finanzierungsmechanismus nicht als Fakt zuspitzen.",
      "fingerprint": "19c4d544ca3c5e9f54c68bf235e415807622dec3265835eb79d342c1e5a75760"
    },
    {
      "id": "C-037",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "The Defense Post 16.12.2022 (Deutschland beauftragt, 182 Mio., Handelsblatt) und Janes 15.12.2022 (Sprecher 13.12. ohne Bestätigung aus vertraglichen Gründen) bestätigt.",
      "fingerprint": "8badd8465d81986df05dedadcd9c4ce66a1e22761f5884bbeab84c6fd7d2bd12"
    },
    {
      "id": "C-038",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "PM 09.07.2026 (DE), GB 2025 S.266 (ARGE HEL-Waffensystem 50, Joint Operations), GB 2024 S.47 bestätigt.",
      "fingerprint": "9b680d6abefd16a8890995bb4ff0c60d0de4a904122b50d994583ca413d04ef9"
    },
    {
      "id": "C-039",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2024 S.34 wörtlich bestätigt.",
      "fingerprint": "07b105a563b94071705b0e37800bae16a16b44972a95a22e4cdb4ad9f3c00ec3"
    },
    {
      "id": "C-040",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2025 S.50 wörtlich bestätigt (Netzwerkkante → A).",
      "fingerprint": "dc9f72d05a0bfa90583878d4c462e5fcbab976b1a06a6108b78e9421f65b78ce"
    },
    {
      "id": "C-041",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2024 S.34 („Andruil“ in Quelle) bestätigt.",
      "fingerprint": "ab75353bb01d3f8fbf51258b436371d0e463089a8812cc4c37d3632aee28e00e"
    },
    {
      "id": "C-042",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GB 2025 S.15 und S.65 sowie Diehl-GB 2025 PDF-S.11/23 bestätigt.",
      "fingerprint": "f450aeb290d08f5fc5a5748e4b0cb7dab435706ad6006776002fb439b1faa37f"
    },
    {
      "id": "C-043",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): GB 2025 S.38 wörtlich bestätigt.",
      "fingerprint": "038d599457b8745ec3d7f97dc6c2a9f11dbb469280f92ddd2ab462e0dbfe7ac0"
    },
    {
      "id": "M-GCC-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Al Jazeera 07.03.2026 und 31.08.2026 geöffnet: saudische/katarische/VAE-Abfangmeldungen, Kriegsbeginn Ende Februar bestätigt.",
      "fingerprint": "25191cac5b93521f79c818e8c2716eb9dcca18978b98afa2c6f45f701558f26d"
    },
    {
      "id": "M-GCC-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Fox News 02.03.2026: Länderzahlen VAE/Kuwait/Bahrain/Katar bestätigt.",
      "fingerprint": "4bfd61913d4861b584bc372c4f9435829c1abb1ca363bc5c2792eecd3977addc"
    },
    {
      "id": "M-GCC-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Middle East Eye 11.03.2026: CBS-Bericht, Knappheit, ~600 PAC-3/Jahr bestätigt.",
      "fingerprint": "4e17b028a5787ccf13a7b58148edcf52a64d33b91369c3358d0b2c84689b7582"
    },
    {
      "id": "M-GCC-004",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Al Jazeera 12.07.2026 (Länderabsätze, Oman/Musandam/Al Wusta) und 31.08.2026 (erstmals seit Juli) bestätigt.",
      "fingerprint": "0706063badcab43a35c48c97a55e38d3e029eaeeac2d961b16bd92b04ba7190c"
    },
    {
      "id": "M-GCC-005",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "AGSI 28.04.2026: SIPRI-Anteile 77/48/62/42 %, Patriot fünf Staaten, THAAD SA/VAE, NASAMS Katar wörtlich bestätigt.",
      "fingerprint": "b59d2b83f752def6e340348920cee3d5d7e7524d58255c2ef6d9717be979bed1"
    },
    {
      "id": "M-GCC-006",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): AGSI 28.04.2026: KM-SAM VAE (IISS), Saudi-Beschleunigung, ukrainische Abfangdrohnen bestätigt. Hinweis: AGSI datiert den saudischen KM-SAM-Deal auf 2024, M-SA-003 auf Nov 2023 (Offenlegung Feb 2024). Zusätzlich: Sky Sabre Anfang April in Saudi-Arabien (laut Berichten) bestätigt.",
      "fingerprint": "4f10d6fc654ea7c8aea4de8a4e4b9c1f57cec83879cad6d494947cebfc628424"
    },
    {
      "id": "M-GCC-007",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): GOV.UK 10.04.2026: Skyhammer, 30 km, 700 km/h, Gulf partners, subject to contract, erste Lieferung Mai bestätigt.",
      "fingerprint": "e86fe2a0fb21c2d9fdc0d73362a0e7a37c3a97ea85ecdd68fac423bd10459350"
    },
    {
      "id": "M-GCC-008",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "SIPRI Fact Sheet April 2026 PDF S.2 Tabelle: Saudi-Arabien [83.2], Rang 8, 1.4/12, [6.5] bestätigt.",
      "fingerprint": "3e55e244455dcbcd1d0666f90248eea1bf7fa708348c71bbc6a28f53ee4f3e0c"
    },
    {
      "id": "M-GCC-009",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "SIPRI Fact Sheet S.2 (Kuwait 8.1, Rang 35, 4.7), S.6 (Middle East g (218), Fn. g ohne VAE), S.10 Abb. 3 (Oman 5.7 %) bestätigt.",
      "fingerprint": "89781c23ada56d11f339c78870cc6e92532e400711ee407cb8e667aeb42e1350"
    },
    {
      "id": "M-SA-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GAMI Strategy: >50 % bis 2030, Industrial Participation Program wörtlich bestätigt.",
      "fingerprint": "1463c6de4ac18d2cdadd8bfddcc2345c3f4c5732b0a02aad26f8a4e3e8b342cf"
    },
    {
      "id": "M-SA-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "GAMI-Meldung 10.11.2025: 24,89 % Ende 2024 wörtlich bestätigt.",
      "fingerprint": "7e63f59287654e98d8a5d106efe763435fe751f15c430e487a6e9c997035d448"
    },
    {
      "id": "M-SA-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Korea Times 06.02.2024: 3,2 Mrd. USD M-SAM II laut Verteidigungsministerium bestätigt. Zusätzlich: Vertrag November (2023), DAPA–MoD-MoU zu gemeinsamer F&E bestätigt.",
      "fingerprint": "3cdd32cfa293de3c5c323b3c86d2cc275a65f32e03bb13bd01a8c889d0330575"
    },
    {
      "id": "M-AE-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "ITA Country Commercial Guide (Stand 25.08.2025): Tawazun Feb 2021, Offset-Leitlinien 2019, Schwelle 10 Mio. USD bestätigt (Quelle nennt zusätzlich Fall <10 Mio. bei bestehenden Offset-Pflichten).",
      "fingerprint": "9d1c022dfac3c33039e8c1420d681a4e4f12cd1033089df373fed7f553cb0d93"
    },
    {
      "id": "M-AE-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): ITA: EDGE 2019, >25 Einheiten, ~5 Mrd. USD, ~8.000 Beschäftigte bestätigt.",
      "fingerprint": "320a8895f9102c5b5a54ecc02850936e329a4a64a35825b76cd78006c3e36870"
    },
    {
      "id": "M-AE-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "EDR (Wiedergabe Unternehmensmitteilung 16.09.2026): Term Sheet EDGE–Hanwha, L-SAM/M-SAM/Chunmoo, JV vorbehaltlich Genehmigungen bestätigt.",
      "fingerprint": "bd66bcc94295863b3ffd3c60908f0ea3e962eb92974e9e7a763a7e6468013c17"
    },
    {
      "id": "M-AE-004",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Breaking Defense Interview 11.05.2026: SKYSHIELD/NAVCONTROL, 80–85 % lokale Lösungen (Chairman, nicht notwendig EDGE) bestätigt.",
      "fingerprint": "8203e842662769e4ff399362395200e78207a7edce24ff1e6701d5cc194be4f5"
    },
    {
      "id": "M-AE-005",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): EOS ASX-Mitteilung 19.06.2026 PDF: 124 Mio. USD, Gen5, Fertigung AUS/VAE, 2027–2028, Exportgenehmigungen bestätigt. Zusätzlich: bedingte JV-Vereinbarung mit Gen5 für HEL/RWS im ASX-PDF bestätigt.",
      "fingerprint": "5ac96c6209d831ba05f05a94fd4d7905394684bec9aaf5e148be44c758ca65af"
    },
    {
      "id": "M-QA-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Shephard 12.07.2019: zwei DCS-Verträge ~2,2 Mrd. USD (NASAMS, AMRAAM-ER, Patriot) bestätigt.",
      "fingerprint": "1d46da12270141667420071cc97918178dfb301b435b34139d0a90a6b8d08dab"
    },
    {
      "id": "M-QA-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "OBG Qatar 2026 (Investmentarm MoD, Mandat JV/Technologietransfer) und Global Business Press 05.03.2024 (JV-Priorität) bestätigt.",
      "fingerprint": "5f345e6a38bb08aaf2626c337beaa46212981ef47fb3a6ba3a723f3cb9796980"
    },
    {
      "id": "M-QA-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "The Defense Post 29.01.2026: GM200 MM/A und GM400α für QEAF, lokale Arbeiten bis 2036 bestätigt.",
      "fingerprint": "968d0db97e9a4ff2600af0ab67fde8a68ad15d98b8c2f6407e66a6f8a1eb6fd5"
    },
    {
      "id": "M-QA-004",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Breaking Defense 11.05.2026: Barzan-Vereinbarung DIMDEX, kombinierter Katalog, EDGE-Sensoren bestätigt (Monatsangabe „February“ im Interview).",
      "fingerprint": "9f0cefc0d4b8372ef688ae5b6bd2da78c6e37a460a23b6915022970c0f35fab7"
    },
    {
      "id": "M-QA-005",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 15.12.2022 (gleicher Artikel wie S-210cf4ad91a0bf63, andere URL – kein unabhängiger Zweitbeleg): Katar-Bestätigung bestätigt.",
      "fingerprint": "2fb725a39810e0943fa6a79ad128fe08af5433fa091318039896bd1cabab8627"
    },
    {
      "id": "M-QA-006",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Global Business Press 05.03.2024 (RBAT als JV mit Rheinmetall, C-UAS) und Unmanned Airspace 19.03.2021 (Drittanbieter-Integration, Qatari C2, PoC) bestätigt.",
      "fingerprint": "5a47469d887c4415b606fe82166cb65b802fbb36d1438cb161ccf08bad1ee135"
    },
    {
      "id": "M-KW-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "inderes-Kopie der Kongsberg-Börsenmitteilung 30.06.2026: Raytheon, FMS, ~400 Mio. USD, layered architecture bestätigt (Drittanbieter-Kopie).",
      "fingerprint": "5fb5183d9af15eee80a74677f11a746586aaac35f3fd2f2eb0cbd5cf1b404885"
    },
    {
      "id": "M-KW-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Breaking Defense 08.06.2026: mögliche FMS 1,98 Mrd. USD, State Dept 05.06., Komponenten, Flughafenangriff bestätigt.",
      "fingerprint": "7e97ece4f38db167d73a738e5d4fd1eb3b73aa6e26412cadffd8ec88be63745a"
    },
    {
      "id": "M-BH-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Al-Monitor (Reuters-Exklusiv) 21.03.2026 und Aletihad 21.07.2026 (BNA) bestätigt. Zusätzlich: Sitra, 9. März, 32 Verletzte, Erklärung vom 21.03. (Reuters via Al-Monitor) bestätigt.",
      "fingerprint": "4162f5b8a8aa37209e115a94ab1867f3ffc202aa3f42f168d6bfa0bd6141ce20"
    },
    {
      "id": "M-OM-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Shephard 24.01.2014: 1,28 Mrd. USD DCS, siebter Kunde, erster am Golf, Kongsberg Partner/Subunternehmer bestätigt.",
      "fingerprint": "d69d2db8a0e81558fa889403519ff27e6038af162abec16c3829a9e8456addce"
    },
    {
      "id": "M-EXP-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "BAFA-Kurzmeldung 20.03.2026: Länder, Luft-/maritime Verteidigung, befristet bis 15.09.2026, Registrierung 30 Tage, monatliche Meldung wörtlich bestätigt (Ursprungsstand).",
      "fingerprint": "8d9ffc2233608b36c849bd1e04e28470d6bb6f6dfe8a748bcc80b17e3af54e19"
    },
    {
      "id": "M-EXP-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "BAFA-Seite Allgemeine Genehmigungen: „Mit Bekanntgabe vom 10. September 2026 wird die AGG Nr. 48 verlängert. Sie ist nunmehr zeitlich befristet bis zum 15. September 2027 gültig“, Punkt 6.6 neu wörtlich bestätigt. Maßgeblicher Stand zum Stichtag.",
      "fingerprint": "987016722e99653b87c0748ff2f221ff133e189c5e10313c536cd3c5b667bdc0"
    },
    {
      "id": "M-EXP-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Breaking Defense 08.01.2024: Baerbock, Kanzler teilt Einschätzung, frühere Verweigerungen (Jemen, Khashoggi) bestätigt.",
      "fingerprint": "917738c10cefe19708641c49e7cede99b4e3e7926fb983b6c3c0245ba2d3561a"
    },
    {
      "id": "M-EXP-004",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "SBFI/admin.ch Medienmitteilung 20.03.2026 und admin.ch 10.03.2026 (per WebFetch; curl 403) geöffnet: Ausschluss Art. 22a Abs. 2 lit. a, USA/Israel/Iran, bestehende Bewilligungen weiter nutzbar bestätigt.",
      "fingerprint": "75ea9c1c41bf49f735c7855a8866cf3ded77547702eb7cd0ce93cd705dbfb0a6"
    },
    {
      "id": "M-EXP-005",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "SECO-Abstimmungsseite: Parlamentsbeschluss 19.12.2025, Partnerstaaten Anhang 2 (36 Länder), Abstimmung 29.11.2026 bestätigt.",
      "fingerprint": "7f756853cefb79a0f9e241b552a420264e56c870b0c00d68cd50615a2292cac1"
    },
    {
      "id": "M-EXP-006",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "WOZ 01.10.2026 (2,77 Mrd., 1,96 Mrd./71 %, RAD >1,6 Mrd. CHF Bewilligungen) und admin.ch 10.03.2026 (948,2 Mio. CHF, 64 Länder, Asien 3,26 %) bestätigt; auf A hochgestuft, da in Matrix-Beobachtung industrial_capacity verwendet. Bewilligung ≠ Ausfuhr korrekt getrennt.",
      "fingerprint": "e03d7960e6b77c0a5caa4bde5b4d098daf9ee08ca7e003698135b0f6dfb9ecc1"
    },
    {
      "id": "M-RHM-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 07.01.2026: Batteriezusammensetzung, X-TAR3D bis 50 km, Mk3 1.000/min, 4 km bestätigt.",
      "fingerprint": "80e0b3f0319ea0f1f8434b533a0db6b78abd2b2077851987f061027afc980a11"
    },
    {
      "id": "M-RHM-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 24.02.2025 (mit RAD entwickelt, Integration in Skynex, Testschüsse, Qualifikation Ende 2026) und Breaking Defense 11.05.2026 (nicht im Dienst, geht in Produktion) bestätigt.",
      "fingerprint": "04ff3736609a15f48b138526a817b794b283f859dc7286dc3db4482c87b8d8fc"
    },
    {
      "id": "M-RHM-004",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "UNITED24 05.07.2026: Air Command West, Skynex, Kh-101 bestätigt (Staatsmedium, korrekt gekennzeichnet).",
      "fingerprint": "2930393dcb5f3c67ba8fb1dbf3f2702a0667ac2010b9fe113474a05f2b041d66"
    },
    {
      "id": "M-RHM-005",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Euronews 17.09.2026 (per WebFetch; curl 406): „From the end of next year we will build, or be able to build, up to 400 a year“; „Under the contract, we have to start series deliveries of the Skyranger in 2027“ bestätigt.",
      "fingerprint": "515402d5f66cca5414a0495fdd5082ecb3c855638bb09e0bf416e55748f6ddf7"
    },
    {
      "id": "M-DIE-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "ESUT 26.05.2023: Rollen Diehl/Hensoldt/Airbus, zweite Feuereinheit, 100 % laut Kundenaussage bestätigt.",
      "fingerprint": "b122516bd633df720fd214964812553a7b34f8f4e99b3d1c1a1341b5b3d59739"
    },
    {
      "id": "M-DIE-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Diehl-PM 23.01.2026: 3.400 m², Lenkflugkörperintegration IRIS-T, ~1,5 Mrd. EUR bestätigt.",
      "fingerprint": "42db93912e056ecd9cb6e6b3945cb5fa3ddf26c4c8672806873fb1ec664700c2"
    },
    {
      "id": "M-DIE-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Diehl-PM 19.02.2025: MoU EDGE (TRUST), Unterzeichner, IRIS-T-SLM-Modelle bestätigt.",
      "fingerprint": "5b1a32758e74518d06bc79c55271bb56263ac80d77336f8d2558a9a303deaf94"
    },
    {
      "id": "M-SAAB-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1: Saab-Produktseite geprüft – RBS 70 seit 2014 beim brasilianischen Heer, erste RBS-70-NG-Schießen 2019; Claim und Beobachtung saab/customer_status korrekt; Fehler behoben.",
      "fingerprint": "937a1c3e81e9a0313009e526218131eea41346f90bac3e6c6a6669331f309cba"
    },
    {
      "id": "M-SAAB-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "The Defense Post 19.03.2025: Loke, 84 Tage, Giraffe 1X, Trackfire, SHORAD-C2 bestätigt.",
      "fingerprint": "759db76f5d0cb061f2a7ebdd0c54b5bfbd004e905d73cfa96897cc6a27241ed9"
    },
    {
      "id": "M-SAAB-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Saab-Länderseite VAE: Saab Ltd 2018, Tawazun Industrial Park, JV GACO 51/Saab 49, fünf GlobalEye bestätigt.",
      "fingerprint": "c693a6279632123f9402577e8e1103018038c930c79f0a0ffed708d07fc83843"
    },
    {
      "id": "M-SAAB-004",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Hochstufung A (Vollprüfung im Originalbeleg): Defense News 04.01.2021 und Saab-PM 27.07.2026 (zwei GlobalEye, 10,1 Mrd. SEK, 2030, Nahost-Land) bestätigt. Zusätzlich: Erweiterung des 2015er Vertrags über drei Flugzeuge bestätigt.",
      "fingerprint": "1c8d2c8927b19f83f67374bc33b50eee26f2bc23cbb9deddb1b76357f1a358e8"
    },
    {
      "id": "M-NAS-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "RTX-Produktseite: Komponenten, offene Architektur, 16 Staaten bestätigt.",
      "fingerprint": "bd680edd8548f34b2b17eb89ea0fd74fa3113dfaab0bf1b92aac4879a37b5373"
    },
    {
      "id": "M-NAS-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Defence Industry Europe 25.02.2025: seit Nov 2022, ~900 Ziele, 94 %, Trøite/Aftenposten bestätigt.",
      "fingerprint": "d2f1513e9cda25008cbfbb686431f90391f330ed7cb134f53786385b5f1b689a"
    },
    {
      "id": "M-MBDA-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "MBDA-Produktseite VL MICA: TOC/PCP, separates 3D-Radar, 3–6 Starter, MICA RF/IR, höhere Führung bestätigt.",
      "fingerprint": "b1fff26e038160a3c6c1a9223265c6da76bfbe865e616f2d48ed5eb147513f93"
    },
    {
      "id": "M-MBDA-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Janes 11.11.2021: SANG-Foto 09.11., MPCV/Mistral, keine Bestätigung MBDA/Frankreich, La Tribune 150 Mio. bestätigt.",
      "fingerprint": "20db6e6e071444b01b6ee49d3b314ee9aaee468761ffab2ccda4bc77c24935c3"
    },
    {
      "id": "M-MBDA-003",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1: Breaking Defense 27.03.2026 geprüft; MICA als „multi-mission air-to-air missile system“ korrekt präzisiert; Claim aus mbda/gulf_access entfernt (dort nur M-MBDA-002), industrial_capacity unverändert zutreffend.",
      "fingerprint": "c2099ecd673d4e1d29ae0d34ea152973a4ec7996b96a4f56de01de42ceb28d9e"
    },
    {
      "id": "M-THA-001",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "EDR 18.11.2024: NSPA-Vertrag ForceShield Compact, GM200, ControlView, Terminals, RapidRanger mit StarStreak und LMM bestätigt.",
      "fingerprint": "c7d2fd4b8beef130872e7dc80e24c45ecbb1fbf028dd84e801960d00e2e71dc6"
    },
    {
      "id": "M-THA-002",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Airforce Technology 03.03.2025 (per WebFetch; curl 403): >5.000 LMM, 1,16 Mrd. GBP + bis 500 Mio., Verdreifachung Belfast, 200 Stellen, LMM in UA-Luftverteidigung bestätigt.",
      "fingerprint": "b665b796ba2af8bb3b4eeac6f47e10d81962322dd6d074df53de1b4a1b9db5df"
    }
  ],
  "correction_round_1": {
    "changed_checked": [
      "T-05",
      "T-07",
      "T-13",
      "T-27",
      "C-024",
      "M-SAAB-001",
      "M-MBDA-003"
    ],
    "module_views_checked": [
      "context.company_facts.cf_ad2025_proforma (T-13) gedeckt",
      "context.events.ev_2026_romania Datum 2026-05-29, Label „vergibt Auftrag (laut Hersteller)“ gedeckt",
      "portfolio.products.drone_defence_toolbox nur P-CUAS-01; P-CUAS-05 im Topic air_defence – korrekt",
      "cluster.topics Sektion „Nicht benannte Kunden“ mit C-026 – korrekt",
      "cluster.gaps.G04 und Coverage Exportrahmen – konsistent mit M-EXP-002",
      "market.observations saab/customer_status korrigiert; mbda/gulf_access nur M-MBDA-002 – korrekt"
    ],
    "resolved": [
      "ME-1",
      "ME-2",
      "T-05",
      "T-27",
      "Produktzuordnung P-CUAS-05",
      "Sektion C-026",
      "Beobachtung mbda/gulf_access"
    ],
    "reused": "Alle übrigen 174 Claims unverändert (Stichprobe Fingerprints T-01, C-002, M-GCC-001 identisch); Urteile aus Basis-Review desselben Laufes/Stichtags übernommen. Netzwerk unverändert, Kantenprüfung übernommen.",
    "formal_check": "check-review-data.py auf neuem Paket Exit 0; facts-validation errors=[]; 181 Claims."
  },
  "upgrade_round": {
    "upgraded_to_A": 36,
    "exceptions": [],
    "note": "37 vormalige B-Claims auf Wunsch des Hauptagenten (Verwendung in module_views/Kernansicht) vollständig nach A geprüft; Belege aus demselben Lauf, gezielte Nachlesen der noch nicht ausdrücklich kontrollierten Teilaussagen. Paket unverändert.",
    "p_snx_10": "Korrigiert und nachgeprüft (Paket neu, nur P-SNX-10-Fingerprint geändert)."
  },
  "input_fingerprint": "b4e2b32169d066fec0e51c5b2f9034009c079eb6cede0cfba0789c6bf271c060"
}
```
