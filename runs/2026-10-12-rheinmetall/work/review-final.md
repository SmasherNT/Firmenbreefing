# Review

```json
{
  "schema_version": 1,
  "run_id": "2026-10-12-rheinmetall",
  "company": "Rheinmetall",
  "as_of": "2026-10-12",
  "phase": "final",
  "status": "freigegeben",
  "material_errors": [],
  "review_scope": {
    "method": "references/quellenpruefung.md, interpretationsphase.md, executive-summary.md, portfolio-darstellung.md, capability-matrix.md",
    "inputs": [
      "input/auftrag.md",
      "work/positioning.json (83 I-Claims)",
      "work/swot.json (11 S-Claims)",
      "work/interpretation-validation.json (94 required_full_review_ids, errors=[])",
      "work/review-basis.md (freigegeben, 181 A geprüft)",
      "work/comparison-plan.json v1",
      "work/review-packet.json (nur depends_on-Fakten gelesen)",
      "work/positioning-context.json (nur Portfolio-Produktzuordnung)"
    ],
    "actually_checked": "Alle 94 I-/S-Ableitungen inhaltlich (A) gegen ihre depends_on-Fakten bzw. I-Claims geprüft: Anker-/Stufenanwendung inkl. Grenze zur nächsten Stufe (35 Matrixzellen), portfolio-maturity-v1 (22 Produkte, Varianten/Demonstrator, Herstellerangabe, Plan ≠ Stufe), Highlights/Headlines/Previews (Einheit, Zeitraum, Bezugsobjekt, Herkunft, Ziel/Ist), SWOT (intern/extern, Datenlücke ≠ Schwäche, Zeitbezug). Keine neuen Webabrufe.",
    "reused": "Unveränderte A-Fakten aus review-basis.md desselben Laufes/Stichtags übernommen, nicht erneut recherchiert. Basis-Hinweise geprüft: Skynex 160/182 Mio. und X-TAR3D 50/55 km nirgends als Wert verwendet; E37 (SADM/MBDA) → Korrektur I-MX-mbda-effector_mix; E34 (NNbS–Skyranger nur Vernetzung) in I-MX-diehl-integration/I-MX-rheinmetall-integration korrekt; Quellen-Duplikate nicht als Zweitbeleg herangezogen.",
    "positioner_questions": "revolver_gun_mk3/x_tar3d Stufe 6: zulässig (Auslieferung an zwei benannte Kunden = wiederholte Auslieferung), x_tar3d-reasoning korrigieren. millennium_gun Stufe 6: zulässig mit sichtbarer Sekundärherkunft. hel_naval Stufe 4: zulässig (Entwicklungsvertrag = Kundenauftrag, Demonstrator getrennt). EDGE/Diehl Stufe 5: zulässig, Anker 'berichtet', Herkunft sichtbar.",
    "formal_check": "scripts/stamp-review.py nur als Probe ins Scratchpad; mechanischer Pass ist keine Inhaltsfreigabe.",
    "non_blocking_hints": [
      "S-W1: Basis-Hinweis Skyranger-Verzögerungsberichte (03/2026) nicht im Paket; optional an portfolio (vgl. RR-04)."
    ],
    "release_readiness": "Alle 94 I-/S-Claims A geprüft; keine offenen Korrekturen oder wesentlichen Fehler. Inhaltlich freigegeben; Fingerprints per stamp-review durch den Hauptagenten ergänzen.",
    "correction_round_1": "22 IDs mit geändertem Fingerprint gezielt gegen neuen Wortlaut und depends_on geprüft (abgleich alter Probe-Fingerprints: genau diese 22 geändert; Validierung errors=[]). 21 freigegeben, MEF-1 behoben; I-PM-skyguard statement nicht korrigiert → bleibt Korrektur. 72 übrige Urteile unverändert übernommen.",
    "correction_round_2": "Nur I-PM-skyguard geändert (Fingerprint-Abgleich gegen Probe der Runde 1 bestätigt; Validierung errors=[]); gegen depends_on geprüft und freigegeben. 93 übrige Urteile übernommen."
  },
  "claims": [
    {
      "id": "I-AD-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (P-AD-01, C-043, P-SR30-01/-03, C-029, M-RHM-003, T-26); LIG nur vereinbart, Partnerplan ohne benannte Partner offengelegt.",
      "fingerprint": "868223f364ee74f458e52aefbe83b8439965acaca7b487852431ece5ac69fbb4"
    },
    {
      "id": "I-AD-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: P-SR30-06 und P-SR35-02 ergänzt, Ungarn als Entwicklungsauftrag und Ukraine ohne belegtes Lieferfenster korrekt qualifiziert.",
      "fingerprint": "639eab9208cd93f6191a14c63308843d1fd238f13ea4d489d496793f9a965603"
    },
    {
      "id": "I-AD-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Bezug 'Skynex' ergänzt; Vergleich der Evidenzstufen ohne Ranking korrekt.",
      "fingerprint": "0bce46efff85e52386aef46dceb80dc9763bb4116244f54b554c29321a3a542d"
    },
    {
      "id": "I-AD-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (C-027, C-038, C-039, C-041, T-26, C-042); Vertrag vs. MoU korrekt getrennt.",
      "fingerprint": "cfb1d57b6683f85445b1a5b51f0face65009bbc362c66bd08ff6dc33be262b15"
    },
    {
      "id": "I-AD-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Personenidentität/aktuelle Rolle gedeckt: Köhne laut Rheinmetall-Karriereseite seit Oktober 2026 CEO Division Air Defence (H-01, Basis A geprüft); Vorrollen H-02/H-03, Schwerpunkte H-05 als Unternehmensdarstellung; Eintrittsdatum 01.10. nur laut ES&T und fehlende RAD-AG-Organfunktion offengelegt; Medienankündigung nicht als alleiniger Beleg verwendet.",
      "fingerprint": "cbbf9cc7d84f78d318421a94df5a7be0eb2102d1cac4b16ecef28d7f648fd0bc"
    },
    {
      "id": "I-ES-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Headline/Preview/Statement gedeckt (C-001, T-02, T-09, T-13); 4,2 Mrd. = 4.218 Mio. gerundet; Backlog inkl. Rahmenverträgen und Prognose (Stand März 2026) gekennzeichnet.",
      "fingerprint": "e5dd76af3f440851d2cc330fd9e6ee3d3ed44bdc4c3f4d02826104ce4179b36d"
    },
    {
      "id": "I-ES-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Neue Headline 'Skynex geliefert, laut Ukraine im Einsatz; Skyranger vor Serienlieferung' (71 Zeichen) gibt Ziel/Ist und Herkunft korrekt wieder (I-PM-skyranger_30 Stufe 4, M-RHM-004); Preview/Statement unverändert gedeckt. MEF-1 behoben.",
      "fingerprint": "9a5623481f73fdf4fdcb8509966a3c42bbfe54f0617b45f654fb99027a86ac5f"
    },
    {
      "id": "I-ES-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (I-MX-rheinmetall-gulf_access, C-006, C-007, P-SNX-06); CEO-Aussagen T-25 nur als Medienwiedergabe; fehlender Auftragsbeleg als Datenlücke formuliert.",
      "fingerprint": "1cadcb73322dc58401441043ffe766a03621a1cbf5b7106931d44c8fb697fee5"
    },
    {
      "id": "I-ES-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Zeitbezug 'seit Ende Februar/Anfang März 2026' entspricht M-GCC-001/-002; übriger Inhalt unverändert gedeckt.",
      "fingerprint": "0fb89c0aa67d6397c38d17502c506294be72cf46adf8c7d602bb685961eddb5f"
    },
    {
      "id": "I-ES-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Headline 'Deutschland erleichtert' präzise (M-EXP-001/-002); sonst unverändert gedeckt.",
      "fingerprint": "c88d1ef59cd3d4421212973509e9b997ec0f2275ed4e46ea099632c2bc773134"
    },
    {
      "id": "I-ES-06",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (M-GCC-005, M-SA-001/-002, M-AE-001, M-QA-002, M-RHM-003); Regierungsziel vs. Ist-Wert getrennt; fehlende Quoten KW/BH/OM in uncertainty.",
      "fingerprint": "c1ae94c76dd2cf1516317efaba347adbfb828ad02078bc7c9b0d7a840a7cc7be"
    },
    {
      "id": "I-GM-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Zeitbezug korrigiert (M-GCC-001/-002); Ableitung unverändert gedeckt.",
      "fingerprint": "206f0ce6b316d7d98f83ee75994f3a343c62357756b4bfd8dcd1dda4223bde25"
    },
    {
      "id": "I-GM-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: KM-SAM/NASAMS jetzt Mittelstrecke (M-SA-003, M-NAS-001), C-UAS-Anbieter getrennt – korrekt.",
      "fingerprint": "a40409e77842bdc97fa0dbed3c4bd7db0af1e56149fb24afbfdc0ef5293abee5"
    },
    {
      "id": "I-GM-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (C-010, C-011, C-012, C-018, C-019, P-SNX-10, P-SNX-06, T-23, T-25, P-GULF-01); CEO-Aussagen ohne Länderangabe korrekt nicht als Länderbeleg; RAST Digital Systems korrekt.",
      "fingerprint": "ca24124c30e261923aaa26d02b4d0e47d3b574750b6c80cd22169bb50caaf278"
    },
    {
      "id": "I-GM-04",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (M-EXP-001…006, C-024, C-025, C-017); Anwendung Schweiz als Datenlücke.",
      "fingerprint": "6997aaaaf877dee5523fb7ac2e4d02bdefdbaf0befd2781b23e4602ed237f8f3"
    },
    {
      "id": "I-GM-05",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (M-SA-001/-002, M-AE-001, M-QA-002, C-009, M-SAAB-003, M-AE-003); Umsetzung RADARABIA/RBAT als nicht belegt.",
      "fingerprint": "5cd9f8641ec2db3677acfa8dbf014235206b6e93070ac3b16eab7a9969c3724d"
    },
    {
      "id": "I-GM-06",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (M-RHM-003, C-021, C-020, M-AE-004, M-QA-004, M-DIE-003, M-AE-003).",
      "fingerprint": "129d3f99d14c05139960c7f4862d68b37b5416610c63c84674529ac7ace6eb51"
    },
    {
      "id": "I-HL-01",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Zahl, Einheit, Bezugsobjekt (Segment Air Defence), Zeitraum H1 2026 und Pro-forma-Vorjahr korrekt aus T-09/P-AD-03; Herkunft 'laut Rheinmetall', ungeprüfte Halbjahreszahlen offengelegt.",
      "fingerprint": "fd607aedf34265b26f2cf13ad46e706457ed6753843ec65832b1e5412cc8fb81"
    },
    {
      "id": "I-HL-02",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Werte 49 %/20 %, 'indirekt', at equity und Stichtag 31.12.2025 korrekt aus C-007; Kapitalanteil ≠ Kontrolle offengelegt.",
      "fingerprint": "6e8a2ddd9103213588b807319970a8f3c7ced9486c58ca5a54bd43de2d101cfd"
    },
    {
      "id": "I-HL-03",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Status, Datum 10.09.2026, Geltung bis 15.09.2027 und Länderkreis korrekt aus M-EXP-001/-002 (BAFA).",
      "fingerprint": "25cf30f61c7cb35ced4ddde91c48e7d5168c136045383b069a1e542f35ac19ce"
    },
    {
      "id": "I-MX-diehl-customer_status",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 durch Lieferung an Ukraine (M-DIE-001), Stufe 5 durch vom Hersteller weitergegebene Kundenangabe zu Gefechtseinsatz; Herkunft sichtbar, Trefferquote nicht als Leistungsbeleg genutzt. Offene Frage Positionierer: Stufe 5 zulässig (Anker 'berichtet'), Herkunftskennzeichnung ausreichend.",
      "fingerprint": "221dc8c616a1c5517aa50949477c4eea97c18588ab3f67265a1e66771c1e6a29"
    },
    {
      "id": "I-MX-diehl-effector_mix",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Ungedeckte Schichtzuordnung entfernt; Statement durch M-DIE-001 gedeckt, Reichweite als nicht beziffert ausgewiesen.",
      "fingerprint": "94e499acc4713b15fe7c7b8d01e6a382c7165ac2a1a4fab15394326745c3eada"
    },
    {
      "id": "I-MX-diehl-gulf_access",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 2 korrekt (MoU EDGE, M-DIE-003/C-022); Grenze zu 3 als Datenlücke formuliert.",
      "fingerprint": "1a1855f30f2268b457f270bf53ec6496a53748b10b2c545698b32b3ada03dd6b"
    },
    {
      "id": "I-MX-diehl-industrial_capacity",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-DIE-002; Konzernbezug der 1,5 Mrd. EUR offengelegt.",
      "fingerprint": "de09e6657d50c8bd102d95a7fd20a335246756b6c1a047310420e6d4725933dd"
    },
    {
      "id": "I-MX-diehl-integration",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt: GU/Systemintegrator mit Hensoldt-Radar/Airbus-FC (M-DIE-001), NNbS-Vernetzung 'vorgesehen' (C-027).",
      "fingerprint": "1e46d1bb69e89193fb34ff1dd88e72fc74c21d90df717f1cd67e1715466d9ecd"
    },
    {
      "id": "I-MX-edge-customer_status",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 5 nach Anker 'Einsatz berichtet' durch M-AE-004 getragen; ausschließlich Unternehmensangabe sichtbar in statement/uncertainty; Abgrenzung SkyKnight korrekt. Offene Frage Positionierer: zulässig, da Anker 'berichtet' verlangt, Herkunft offen.",
      "fingerprint": "37d9c81364ff7d89d761df21b830cac943d98a864ec293b8175224f7dbd8d554"
    },
    {
      "id": "I-MX-edge-effector_mix",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-AE-004 (Soft-Kill, CEO-Angabe) und M-RHM-003/P-SNX-08 (SkyKnight in Erprobung); Herkunft Unternehmensangabe sichtbar.",
      "fingerprint": "37eb7187ef9a55253e43197448c77a0bc215ab47062a8c6fbebbf57639ff8afd"
    },
    {
      "id": "I-MX-edge-gulf_access",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 5 gedeckt: nationale Industriebasis (M-AE-002, M-AE-004 'national gebaut'), Kunden VAE (M-AE-004) und Kuwait-Programm als GU (C-020); Einschränkung maritim/Inländerstatus offengelegt.",
      "fingerprint": "86708458a84380860d43e233622b57a498cb252de3a1fdbdec0c6d1e826520c1"
    },
    {
      "id": "I-MX-edge-industrial_capacity",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt: ITA-Schätzungen (M-AE-002) als Schätzung, SkyKnight-Produktionsanlauf als CEO-Aussage (M-RHM-003).",
      "fingerprint": "b71d34eb213cc4bbf33e5f64bdf8cad4cce5cb90056929b2ebd5cde9a9971dd0"
    },
    {
      "id": "I-MX-edge-integration",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt: SkyKnight-Skynex gemeinsame Entwicklung (M-RHM-003), Barzan-Vereinbarung nur EDGE-Darstellung (M-QA-004), Hanwha-Term-Sheet unverbindlich (M-AE-003).",
      "fingerprint": "98239688448ceef4686e45f1514c059ba435c0f755839e19c49804262ae9cb29"
    },
    {
      "id": "I-MX-kongsberg_rtx-customer_status",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 5 gedeckt durch M-NAS-002 (Einsatz Ukraine, Unterstützerangabe), Verträge Oman/Katar (M-OM-001, M-QA-001).",
      "fingerprint": "5da43ede0b572afa4d22b4f723ae910ce64ebcd8dfdd64d7906717738cfc7301"
    },
    {
      "id": "I-MX-kongsberg_rtx-effector_mix",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-NAS-001; Schichtzuordnung durch Fakt-Unsicherheit ('Mittelstrecke an der Obergrenze') gestützt (Formulierung 'laut Plan' unpräzise, nicht sinnverändernd).",
      "fingerprint": "6597faecc074b09c855c6d60b458408629c5f40f4a5e030d2b4b2d8cb6a62df4"
    },
    {
      "id": "I-MX-kongsberg_rtx-gulf_access",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 3 gedeckt (Oman 2014, Katar 2019 DCS; Kuwait 2026 über Raytheon/FMS, offengelegt); Grenze zu 4 als Datenlücke.",
      "fingerprint": "bbc0fa1f873976ae2df8ab0c6fcec67b84341f0bf60b65a936214396c897d08f"
    },
    {
      "id": "I-MX-kongsberg_rtx-industrial_capacity",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "'nicht öffentlich belegt' korrekt mit coverage_note (Kongsberg-Seite 403); keine Schwächeaussage.",
      "fingerprint": "66ad230a4d0a0ea32b09618d988c98f044e3a4a039548628d5ac9063576bed38"
    },
    {
      "id": "I-MX-kongsberg_rtx-integration",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-NAS-001 und M-KW-001; Herstellerangaben gekennzeichnet.",
      "fingerprint": "c425c2f4710c6bdf43983800584b1ea05f092e0a0aeee1b69c0cb009f2ef8620"
    },
    {
      "id": "I-MX-mbda-customer_status",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 gedeckt durch M-MBDA-002 (Kundenfoto SANG, keine MBDA-Bestätigung offengelegt); Mistral-Österreich korrekt nur 'vorgesehen'.",
      "fingerprint": "5387b560063d0d765c966553056a9182c51dcc9db92a6dc56fc377aaa4b3f266"
    },
    {
      "id": "I-MX-mbda-effector_mix",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: 'vorgesehen' statt 'liefert'; Mistral-Lieferbeginn unbestätigt (P-SR30-03) und DefendAir/SADM gebilligte Finanzierung ohne Auftragnehmer (C-029, E37) korrekt.",
      "fingerprint": "7c65babe304810f28221a6c1417cfb546c429ccaaf1d406e38c0fab00cf32c79"
    },
    {
      "id": "I-MX-mbda-gulf_access",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 3 vertretbar (berichteter Erwerb durch SANG, M-MBDA-002); kein offizieller Vertrag offengelegt; Grenze zu 4 korrekt.",
      "fingerprint": "90bf7014b86aed038b6afdb072fc62c904fb648f721f678af3e1409881720258"
    },
    {
      "id": "I-MX-mbda-industrial_capacity",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-MBDA-003; Plan/Medienwiedergabe und MICA-Luft-Luft-Abgrenzung (Basis-Korrektur) übernommen.",
      "fingerprint": "ea8a6e090781f88df6693df7e3e889a5f0681cc6b7d7caef890f2bde5b1b065b"
    },
    {
      "id": "I-MX-mbda-integration",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-MBDA-001; Herstellerangabe gekennzeichnet.",
      "fingerprint": "1004d8d590645de532029cbe96f4745ee9b691bd6b5fc472d57f84c23a263e0d"
    },
    {
      "id": "I-MX-rheinmetall-customer_status",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Statement nun 'berichtet', Ukraine-Lieferung als Herstellerangabe (P-SNX-03) gekennzeichnet; Stufe 5 unverändert korrekt.",
      "fingerprint": "f8698b6121f54a25b92589235861fbaedf5b3e2105fed6b47e2e4b294a27bc4d"
    },
    {
      "id": "I-MX-rheinmetall-effector_mix",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Profil gedeckt: eigene Rohreffektoren/AHEAD (P-SR-01, M-RHM-002), Partner-Flugkörper Stinger/Mistral/DefendAir (P-SR30-01/-03/-08), SkyKnight in Erprobung (M-RHM-003), HEL nur Demonstrator/Entwicklung (P-SR30HEL-01, P-HEL-03); Reichweiten als Herstellerangabe gekennzeichnet; X-TAR3D-Reichweite nicht verwendet.",
      "fingerprint": "44bc3ab6885a164e8a3f78334a72d51efbf888f4024fd6085f3b1165def3b0ae"
    },
    {
      "id": "I-MX-rheinmetall-gulf_access",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt: 100-%-Golf-Töchter (C-006) und at-equity RBAT 49 %/RADARABIA 20 % (C-007) erfüllen Anker 4; Stufe 3 über Katar-Lieferung (M-QA-005) und Kuwait-MASS (C-020, außerhalb Vergleichseinheit offengelegt). Grenze zu 5 korrekt: lokale Fertigung nur angekündigt (C-009, C-015).",
      "fingerprint": "d9c332a2a9401011a9f6f0a7c88bcb2f65465af3b4f54c8ef47bf45a65c89f28"
    },
    {
      "id": "I-MX-rheinmetall-industrial_capacity",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: value 'Fertigung in CH, DE, IT und NL' korrekt; reasoning 'bewilligtes Exportvolumen' (M-EXP-006) korrekt.",
      "fingerprint": "24b42a3cef704473ec6f6071b6825de4551922b061b180225964b1f748f105ac"
    },
    {
      "id": "I-MX-rheinmetall-integration",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Profil gedeckt: Kette X-TAR3D–Skymaster–Revolver Gun (M-RHM-002), Plattformen Boxer/Pandur/Lynx (P-SR30-01/-03, P-SR35-03); Twinvis nur Übung (P-SNX-07), NNbS nur 'vorgesehen' (E34-Hinweis beachtet); Offenheit als Herstellerangabe.",
      "fingerprint": "db23f0f7c99c702e7c0e1c14f98291f8ac080f1b19142be490b4b494a23eb354"
    },
    {
      "id": "I-MX-saab-customer_status",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 vertretbar: Nutzung RBS 70 durch brasilianisches Heer und NG-Schießen 2019 laut Saab (M-SAAB-001); Herkunft und fehlender NG-Lieferzeitpunkt offengelegt; ME-2-Korrektur der Basis berücksichtigt.",
      "fingerprint": "cec4eac7e11bb5d8a0cfd16247aeb0bb14b99980e5a620056e1ed98100245d65"
    },
    {
      "id": "I-MX-saab-effector_mix",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-SAAB-001/-002; Herstellerwerte gekennzeichnet.",
      "fingerprint": "7b2d921636b12537fb75708506908110cc776a35768b9f5d8d86becd9343516c"
    },
    {
      "id": "I-MX-saab-gulf_access",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 gedeckt: GlobalEye-Verträge VAE (M-SAAB-004, Stufe 3), Saab Ltd/JV laut Saab (M-SAAB-003, Stufe 4); kein SHORAD-Bezug offengelegt; Grenze zu 5 korrekt.",
      "fingerprint": "e5ea0ca44a7fb0dffbdd86b19c4e3e44426c42ca437c4e7ea8f0908115e81a83"
    },
    {
      "id": "I-MX-saab-industrial_capacity",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Zelle 'nicht öffentlich belegt' korrekt: value=null, coverage_note vorhanden, keine Aussage über tatsächliche Lieferfähigkeit.",
      "fingerprint": "33ab94d19242a0531feeff56ac10432ce686fab9a20c40e79e3e63bba0062a30"
    },
    {
      "id": "I-MX-saab-integration",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-SAAB-001/-002; Grenze (übergeordnete Führung nicht beschrieben) korrekt.",
      "fingerprint": "673c3d2a5da80122951d299969e12310c0ab413a201a7020b63f49b7e2bf647a"
    },
    {
      "id": "I-MX-thales-customer_status",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 5 gedeckt durch M-THA-002 (LMM-Einsatz Ukraine, Fachmedium); Beschränkung auf Effektor LMM korrekt ausgewiesen.",
      "fingerprint": "ac21b250245be1612b3dc2c7555a6a258c4c9220199aaf6b0d9f0e9f7ef5bd57"
    },
    {
      "id": "I-MX-thales-effector_mix",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-THA-001/-002.",
      "fingerprint": "ddfdd6627cea3456119cd480313b2545f46cc4af9aab3a438c0f014ed0b05e79"
    },
    {
      "id": "I-MX-thales-gulf_access",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 3 gedeckt durch M-QA-003 (Radarauftrag QEAF laut Thales); lokale Vorarbeiten korrekt nicht als Stufe 4 gewertet.",
      "fingerprint": "4b0eb1ed90195f0d9d92da97fcc648514bf78605f52217e492d90da49cd0cf60"
    },
    {
      "id": "I-MX-thales-industrial_capacity",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-THA-002; LMM-Bezug und Stand März 2025 offengelegt.",
      "fingerprint": "4966a9c66d113f236e52ad0b37876589fdb4734b7d4286591c39cf998b8484cc"
    },
    {
      "id": "I-MX-thales-integration",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt durch M-THA-001.",
      "fingerprint": "8004857b9a6eedf401d4a6c182dbd3f2c8ef2dc6fe83b65b0461fc4b8a39b280"
    },
    {
      "id": "I-PM-aerie",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 2 korrekt: Prototyp laut Mitteilung, Demonstrationen erst geplant; Titel-Überzeichnung ('liefern') offengelegt (P-CUAS-04).",
      "fingerprint": "7505e89ee6283ecfefbc33412a2981ed073c33c077b448f1a8a0b56129b4edce"
    },
    {
      "id": "I-PM-ahead_35",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt und konservativ (P-AH-02, P-SG-02); Beleglücke zu Lieferung nicht als Unreife formuliert.",
      "fingerprint": "e5d5509d03eba2b856574981d071ec001121d525eb2b3367aa2d532a4523c44f"
    },
    {
      "id": "I-PM-drone_defence_toolbox",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 1 korrekt; Produktzuordnung nur P-CUAS-01 (Basis-Korrektur umgesetzt).",
      "fingerprint": "09225c3bc78eb0505ab49a8160d7afc412b062ce6d01820e9151256915c7d87b"
    },
    {
      "id": "I-PM-gepard_ammo_35",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt (P-GP-01; erste Charge laut Hersteller, keine wiederholte Auslieferung belegt).",
      "fingerprint": "4520445a099bd7a569c69fe5a18e4612025914d4a06b3a8f2b50b75871431656"
    },
    {
      "id": "I-PM-hel_naval",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 vertretbar: Demonstrator (Stufe 3, P-HEL-01/-02) und künftiges Marinesystem (Entwicklungsvertrag BAAINBw, P-HEL-03 = konkreter Kundenauftrag) im statement getrennt; Einsatzbereitschaft 2029 als Ziel, JV nicht bestätigt. Offene Frage Positionierer: Stufe 4 zulässig, kein Übertrag auf Stufe 5.",
      "fingerprint": "83106441828424851913e725b84868d0f2d7b03025b51cefbe0f4d6abbc295b8"
    },
    {
      "id": "I-PM-hermelin_cuas",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 1 korrekt (Messeexponat, P-CUAS-03).",
      "fingerprint": "af36da9873be96bfc9762104fd5089002c4d19366c1f834219834a97bf123cb6"
    },
    {
      "id": "I-PM-mass",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt (P-MASS-01/C-020); Softkill-Abgrenzung und Wertunschärfe offengelegt.",
      "fingerprint": "cb2acc3af9f48b5ce3dc5e2458f1f16709e85a74c1961596b39f5176cef80546"
    },
    {
      "id": "I-PM-millennium_gun",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 6 vertretbar: eigenständiger Fachmedienbericht (ESD, P-MG-02, Basis A geprüft) nennt fünf Marinen; Sekundärherkunft im statement ('laut Fachmedium') und uncertainty sichtbar. Offene Frage Positionierer: zulässig mit sichtbarer Einschränkung.",
      "fingerprint": "dc947ed2b70e7e7ec900afdffb972085321aa9abe8f6ab462548209f23d6b7db"
    },
    {
      "id": "I-PM-msu",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 1 korrekt (P-MSU-01).",
      "fingerprint": "6387551fd308b0602a9d0250f1b578eea919e0d81c3a137c2f702bc98772df44"
    },
    {
      "id": "I-PM-rcws320_cuas",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 1 korrekt (P-CUAS-02).",
      "fingerprint": "509a6ecb8a9c5a4e46b9e735c231931e1285804d790c2d48db0bf4be5fbb3941"
    },
    {
      "id": "I-PM-revolver_gun_mk3",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: M-QA-005 ergänzt; Stufe 6 (Auslieferung an zwei benannte Kunden) weiterhin getragen.",
      "fingerprint": "a68d5f6c3408e2ae46f14dde7e3db5ea0920f7721642472e018b543bd286fdcb"
    },
    {
      "id": "I-PM-skyguard",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 2 (neuer Fingerprint) gezielt geprüft: statement nun mit Zeitbezug und Herkunft – Al-Jubail seit Juni/Juli 2019 laut Medien-/Bildauswertung (P-SG-05), Kuwait laut Bericht 2013, Variante nicht genannt (C-019), Skyguard NG seit 12/2023 beauftragt (P-SG-02); Stufe 5 vertretbar, Grenze zu 6 korrekt.",
      "fingerprint": "47e0579e2df8c5af8ac7cc6ed79b4dceb0600eeabf90d801738ad75a8f20a69c"
    },
    {
      "id": "I-PM-skymaster",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt: Italien-Batterie/Kundenprogramme; Plattformreife Skynex nicht übertragen.",
      "fingerprint": "0c6ccf36916a08e36ec8db9ba4507ce01607cb7d48d8a47d1e560687b1aafd86"
    },
    {
      "id": "I-PM-skynex",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 6 gedeckt: Auslieferungen Katar (M-QA-005 Rheinmetall-Bestätigung, P-SNX-09), Italien (P-SNX-05, M-RHM-002) und Ukraine (P-SNX-03, Herstellerangabe) = wiederholte Auslieferung; Einsatzbericht M-RHM-004 mit Herkunft; 160/182-Mio.-Widerspruch nicht verwendet.",
      "fingerprint": "d169fb9253f7ee9fb5e6d74e53b480d89e5bb9e544c55848cb85899073f9d3db"
    },
    {
      "id": "I-PM-skynex_skyknight",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 3 korrekt (Testschüsse laut Janes, M-RHM-003); Grenze zu 4 korrekt (kein Auftrag; VAE-Erstkunde 2021 nur vorgesehen, C-021).",
      "fingerprint": "44f45014757e0c0a82567fe912dcafeb5299beafd08d41a350119bcd638a7717"
    },
    {
      "id": "I-PM-skyranger_30",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt: Aufträge DE/AT/DK/NL (P-SR30-01/-03/-04/-05), Nachweismuster-Übergabe; Serienlieferungen und Kapazitätsziel korrekt nicht als Stufe gewertet.",
      "fingerprint": "af0287231a02169103f9442be23144748826fe83e80caee603f87cb97ef9c2e3"
    },
    {
      "id": "I-PM-skyranger_30_hel",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 1 korrekt: Komponenten-/Technologiemustertests nicht auf Hybridkonfiguration übertragen (P-SR30HEL-01).",
      "fingerprint": "f2f6fbbc0fa7863c76c1c8bca331d5f6e7b8efa0e267fa551292cf3dac48b31a"
    },
    {
      "id": "I-PM-skyranger_35",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt (P-SR35-02/-03); Lieferung/Einsatz Ukraine nicht belegt, Rumänien 2028+ Plan.",
      "fingerprint": "b2081fa3841ee67282c385cb6f38a63d9ecb459cc8507c4a24d85e3d315357ce"
    },
    {
      "id": "I-PM-skyranger_762",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 1 korrekt: Messeexponat reicht nicht für Stufe 2 (P-SR762-01).",
      "fingerprint": "3694dc25a913dd90c36394a3af2ca9e3f1e05c1160315cba168342564485eb2a"
    },
    {
      "id": "I-PM-skyshield",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 4 korrekt (P-SS-01, Kunde ungenannt offengelegt).",
      "fingerprint": "7f7312e82417801c75c7c0cfc41efbff0e630e6e7d7d588dcecb4f453bdeeedb"
    },
    {
      "id": "I-PM-skyspotter",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Stufe 3 korrekt (Demonstration GBAD Demo Days, P-SSP-02; Herstellerangabe).",
      "fingerprint": "2ae09b24c04693d9738e08a02fe5a679abc330eab41a06f05abbd3239c813cf2"
    },
    {
      "id": "I-PM-x_tar3d",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Stufe 6 nur auf Auslieferungen Katar/Italien gestützt; Aufträge (P-SG-03, P-SNX-11 jetzt in depends_on) ausdrücklich kein Stufe-6-Beleg – korrekt.",
      "fingerprint": "121c1cf045d50a141acf7414bf34f5442493f4e904f6c135f30ca2d951d0feda"
    },
    {
      "id": "I-RG-AE",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: M-GCC-006 für KM-SAM-Verweis ergänzt – gedeckt.",
      "fingerprint": "026b5e0f857be0dff619eea071fe71f33f16a9aa727f2569d9be3bad83195dbc"
    },
    {
      "id": "I-RG-BH",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (M-BH-001, M-GCC-005, P-SG-05); Eigentümer Skyguard-Foto unklar, Datenlücke korrekt.",
      "fingerprint": "d86f426c82b08cc1bb723dc3c139879cd5c2126b1c0695cb141eec50c5460ab2"
    },
    {
      "id": "I-RG-KW",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (C-019 historisch, C-020 MASS als Softkill, M-KW-001/-002).",
      "fingerprint": "dc3e25329081c768c414f5986387945c566a47f58a920262b66a90863d233c51"
    },
    {
      "id": "I-RG-OM",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (M-OM-001, M-GCC-009, M-GCC-004); fehlender Rheinmetall-Bezug als Datenlücke.",
      "fingerprint": "83371803153150331d4f6532068c771dfbed6f26447c102ea79b341b1c6fd014"
    },
    {
      "id": "I-RG-QA",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Gedeckt (M-QA-005, P-SNX-09/-10, C-007, M-QA-006, M-QA-001, M-QA-003); 'stärkste belegte Position' als belegbezogene Einordnung vertretbar; RBAT-Status offen.",
      "fingerprint": "2aaef2f2cb011b374db82310a9177c53ec01e6fb13f4b7a261591598eb3d8938"
    },
    {
      "id": "I-RG-SA",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Kein GCC-Budgetvergleich mehr; Datenlücke VAE/Katar/Bahrain (M-GCC-009) offengelegt; M-MBDA-002 ergänzt – gedeckt.",
      "fingerprint": "2a76f025be2074081724a1ad4863d117fae9c1aca40d0b6fe63ebe23558f0841"
    },
    {
      "id": "S-O1",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Zeitbezug an I-GM-01/I-ES-04 angepasst; extern, Ableitung gedeckt.",
      "fingerprint": "ae9e2c66b628e16baf5d3a5cbbcaa92ad75d044ec79691d9d50a9f240714b312"
    },
    {
      "id": "S-O2",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Gegen neue I-ES-05-Headline geprüft: Ableitung unverändert gedeckt; extern korrekt.",
      "fingerprint": "b842e734b33430847301c6e7ce62a6d4942b00aaa545a3a1c1e9d458ecbebfa3"
    },
    {
      "id": "S-O3",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Extern korrekt; M-SA-001/-002, M-QA-002, C-007; JV-Umsetzung als 'bei Umsetzung' bedingt formuliert.",
      "fingerprint": "84d4342f7f159b1c50b4af2c07c8bf2e9c1aa125feb04eb84dfb2544b2c26a8b"
    },
    {
      "id": "S-S1",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Gegen neuen Wortlaut von I-MX-rheinmetall-customer_status geprüft: 'mehrfach geliefert' trägt weiterhin (Stufe 6 I-PM-skynex), Einsatzherkunft sichtbar; intern korrekt.",
      "fingerprint": "257294f140c1d5e1a9845ea7f45b4a8b4a09ac1a67893cc97bd540e7d6db9f08"
    },
    {
      "id": "S-S2",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Intern korrekt; C-006 (vier Golf-Gesellschaften), C-007, P-SNX-10, I-MX-rheinmetall-gulf_access; Umsetzung lokaler Fertigung als Datenlücke, nicht als Stärke behauptet.",
      "fingerprint": "3afc03beb2280c5c7c139477d9f6df7ebc5c44e77ac289fbde63a50e3c2bffad"
    },
    {
      "id": "S-S3",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Intern korrekt; Kennzahlen und Zeitpunkt aus T-09/C-001 korrekt; Backlog inkl. Rahmenverträge offengelegt.",
      "fingerprint": "d0ebf092daba37c139dc55349c5b8f32d71cdbc3f9054d420e9083e1d4763608"
    },
    {
      "id": "S-T1",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Schichtzuordnung an korrigiertes I-GM-02 angepasst (Patriot/NASAMS/KM-SAM obere/mittlere Schicht; Slinger/Anduril/Skyhammer Nächstbereich/C-UAS); extern korrekt, Anduril ohne Vertrag offengelegt.",
      "fingerprint": "32be62a1f8474b76488641944dcb76cde02fb595c5ab69e281c1d94fff0680c4"
    },
    {
      "id": "S-T2",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Gegen neue I-ES-05-Fassung geprüft: Ableitung unverändert gedeckt; Datenlücke nicht als Verweigerung; extern korrekt.",
      "fingerprint": "edd1815e47d5ac3f93d0ac5afaab76bb27a8096a02119838243e6b5d324208bd"
    },
    {
      "id": "S-T3",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Extern korrekt; I-GM-06, I-MX-edge-gulf_access (Stufe 5), M-AE-001/-003/-004; EDGE-Angaben und Term-Sheet-Unverbindlichkeit offengelegt.",
      "fingerprint": "64bd3a09f8dd9be16246d1f4f366b8fe1747ab7bcc122db68404fdf2d35c5ae7"
    },
    {
      "id": "S-W1",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Korrekturrunde 1 (neuer Fingerprint) gezielt geprüft: Gegen neuen Wortlaut von I-AD-02 und I-MX-rheinmetall-industrial_capacity geprüft: Aussage unverändert gedeckt; CEO-Wiedergabe (T-25) sichtbar; intern korrekt.",
      "fingerprint": "895c12621cdef9875a0fbc94ae3479d6b85e4695e4fe2873a2a44e8ca02e5c4c"
    },
    {
      "id": "S-W2",
      "depth": "A",
      "status": "geprüft",
      "evidence_review": "Intern korrekt: Partnerabhängigkeit bei Flugkörpern belegt (I-AD-01, I-MX-rheinmetall-effector_mix, C-043, I-PM-skynex_skyknight); keine Datenlücke als Schwäche umgedeutet.",
      "fingerprint": "eb52ddd66606d6b78f6c15a356e31ae9c322a15cf1d088f8c23dc3cf0caf85ee"
    }
  ]
}
```
