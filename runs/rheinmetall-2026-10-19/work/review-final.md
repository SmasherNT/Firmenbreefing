# Review

```json
{
  "schema_version": 1,
  "run_id": "rheinmetall-2026-10-19",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-19",
  "phase": "final",
  "status": "freigegeben",
  "material_errors": [],
  "review_scope": "Leitprüfung Schluss-Review Runde 2 (interpret-v2), 0 Dokumentjobs, facts_to_verify=0. Alle 15 Korrekturen aus Runde 1 und die S-WKN-3-Auflage an den 18 geänderten Claims (inkl. abhängige S-STR-1, S-THR-1) vollständig gegen Fakten, Anker und Darstellungsfelder geprüft; Zahlen-/Datumsrückverfolgung ohne neue untraceable Werte. Übrige 108 Claims mit unveränderten Fingerprints: Runde-1-Befunde ausdrücklich übernommen. reuse_fact_ids = alle 200 referenzierten Fakten (inkl. T-E01, P-R61, M-RHM-07), im Basis-Review A-geprüft; keine Neurecherche.",
  "open_limits": [
    "Überwiegend Herstellerangaben (Rheinmetall-Mitteilungen/Investorenpräsentation), Plan- und Zielwerte keine Ist-Werte; Q3-2026-Zahlen erst 05.11.2026; Closing Power Systems offen.",
    "Matrix: RQ-01 (Rheinmetall-Reichweite je Variante/Ladung) und RQ-02 (KNDS-Jahreskapazität mit Zieljahr) bleiben dokumentierte, nicht blockierende Datenlücken; RQ-03 (RDX-Status) und RQ-06 (Produktreife Fuchs/Radare/Battlesuite) ebenso.",
    "Regionale Präsenz: RQ-04 (Rheinmetall Arabia Simulation and Training LLC, Riad laut C-STR-18) und RQ-05 (RBSL Entwurf/Betreuung) nicht in der Regionszuordnung; Golf bleibt 'nicht eindeutig bestimmbar', GB bei Stufe 4.",
    "Modelle nur als claude-sonnet-5-5/medium konfiguriert; das tatsächlich ausgeführte Modell ist aus dem Lauf nicht nachweisbar. Keine Dokumentjobs in der Schlussphase, daher keine neuen Originallektüren; Fakten-Reuse stützt sich auf das freigegebene Basis-Review."
  ],
  "non_blocking_notes": [
    "I-MI-portfolio-1 und S-STR-1: Reasoning nennt Stufe 6 bei HX/155-mm/Mittelkaliber ohne die I-PM-IDs in depends_on (inhaltlich korrekt); bei nächster Überarbeitung ergänzen.",
    "I-ES-4 Preview ohne 'laut Rheinmetall'; I-ES-1 Rundung; S-THR-1 Wortlaut 'umkehren'; S-WKN-3 keine abgeleitete Prozentzahl rendern.",
    "Übrige Hinweise aus Runde 1 (KNDS Italien/Neubau, BAE Bofors, I-PM-cuas, I-RP-sg, RQ-04 Golf) unverändert."
  ],
  "review_work_fingerprint": "bc98270aa8c1139e047b6fb64b352d427877ce2300a76ffc9348a09ce478841e",
  "plan_fingerprint": "0f06119e097f46df4747bd2318e44210cc02ce7ee29b0214e7ebe65d88421a49",
  "source_collection_fingerprint": "e88c6b41ee862d00b292b978ea1ab24db5eb1ce64b1a9eced6229263659dfe4c",
  "source_checks": [],
  "parallel_review": {
    "plan_fingerprint": "0f06119e097f46df4747bd2318e44210cc02ce7ee29b0214e7ebe65d88421a49",
    "source_collection_fingerprint": "e88c6b41ee862d00b292b978ea1ab24db5eb1ce64b1a9eced6229263659dfe4c",
    "part_fingerprints": {},
    "model_policy": {
      "source-document-reviewer": {
        "model": "claude-sonnet-5-5",
        "effort": "medium"
      },
      "source-reviewer": {
        "model": "claude-sonnet-5-5",
        "effort": "medium"
      }
    }
  },
  "claims": [
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-1",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Kennzahlen gegen T-13/T-14/T-16/T-18 geprüft: +39 %, 5.227 Mio EUR, Backlog 80,5 Mrd (inkl. erwarteter Rahmenabrufe, im Preview benannt), FCF -1.616 Mio, Prognose 13,7-14,2 Mrd, 50-Mrd-Ziel 2030 ausdrücklich als Ziel. Hersteller-Zuschreibung ('laut eigenen Zahlen') sichtbar; Rundung 5,2 bzw. -1,6 Mrd im Preview ist reine Darstellungsrundung (nicht blockierend). Kurzfelder: Headline/Preview innerhalb der Grenzen.",
      "fingerprint": "d976364be5b3e19e0e22a807f37c07270307d689ffc0765167d5dbe14a8c298c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-2",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Ableitung aus P-W10/P-W40/P-W13/M-RHM-03/-05 und den Matrixzellen (Integration 3/4, Industrial 4/4, Procurement 4/4) nachvollzogen; Ist (Unterlüß in Betrieb, Aschau 1.700 t) und Plan (RDX, 1,5 Mio bis 2030) getrennt, Herstellerziel im Preview gekennzeichnet; Litauen-Verzug laut Fachmedium über I-M-rheinmetall-industrial (M-RHM-07) gedeckt.",
      "fingerprint": "0e2a1a8889a4f9b0cc4381a411b3c0459d63312fb41585934f4017332ccb2069"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-3",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. T-04, C-STR-14, P-C01, T-E17, C-STR-38, T-16 abgeglichen: fünf Segmente, NVL-Erwerb (27.02./01.03.2026 Datumsabweichung im Faktum ausgewiesen), Power-Systems-Verkauf unterzeichnet, Closing Q4 nur angestrebt, F126 bis 300 Mio EUR Umsatz, 2.153 Mio EUR ausgebucht. Keine Überdehnung.",
      "fingerprint": "301b81945255f537308cdb252456e5f38d75e11e1aaa4eb3658ce1639e70eb64"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-4",
      "evidence_review": "Runde-2: Dominanzaussage entfernt; Statement nennt 'viele' Bundeswehr-bezogene Großaufträge neben dem Rumänien-Paket (C-MKT-06 nun in depends_on), 62 % Auslandsumsatz H1 (T-13), Arminius erwartet/nicht erteilt (P-V17/T-E30); Uncertainty benennt fehlende Rangfolge nach Volumen. Nicht blockierend: Preview nennt das Rumänien-Paket ohne 'laut Rheinmetall'.",
      "fingerprint": "78604f9004a8a14ec082b229c2643f185955d80aa63eda93f7926282a6ebbc4e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-5",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufenzählung gegen I-RP-* geprüft: Stufe 5 in genau zehn Regionen (DE, NL, CH, IT, HU, RO, Nordeuropa, US, SG, ZA), Stufe 4 u. a. UA, Litauen/Lettland nur geplant, Golf nicht bestimmbar; HU/ZA als beherrschte JV (Vollkonsolidierung) korrekt. 'Staatliche Partner' ist über HU-Regierung, UDI (C-STR-20) und State Defence Corporation (P-R95) für 'oft' getragen; Denel/EPSO-G-Status ist im Paket nicht belegt (siehe I-MI-cluster-2). Nicht blockierend: Preview 'Rumänien-Paket ... mit lokaler Wertschöpfung' sollte 'soll' (Herstellerplan, C-MKT-06) tragen.",
      "fingerprint": "23382f8edf14d0f316f52658bbdb2c530ef63b7dd8d852cc2ebb43ac1988b387"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-6",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Konsistent mit I-PM-skyranger (4), I-PM-fv014 (4), I-PM-sar (5) und T-07 (Air Defence +62 %); Medienverzug Skyranger 30 und Rheinmetall-Gegenangabe (P-A11) beide genannt; Einordnung 'SPOCK 1 im Betrieb' beruht auf Herstellerangabe (P-D30), im Reasoning/Uncertainty erkennbar.",
      "fingerprint": "018162c2ab308b0edc34d8a0669b0b97d5b705a3b08a72270c953be2b25a4847"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-HL-1",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. T-14: 80,5 Mrd EUR zum 30.06.2026 (Vj. 56,0), Definition inkl. erwarteter Rahmenvertragsabrufe im Label; Konzern/Unternehmensangabe/Stichtag korrekt, Länge der Felder innerhalb der Grenzen.",
      "fingerprint": "fec94a9264c92722928aac1242756e50c1b44dec2f6ce04339743a664589b7e3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-HL-2",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. T-16/P-S05: 13,7-14,2 Mrd EUR, Senkung um 300 Mio EUR wegen F126, Stand 06.08.2026; als Prognose ('kein Ist') in scope_label gekennzeichnet; Bezugsobjekt Konzern, Zeitraum GJ 2026 korrekt.",
      "fingerprint": "3bf84528e95b714152d4031a43bd58fe00b8a02e882f284ab5a319f712e6c4fd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-HL-3",
      "evidence_review": "Runde-2: T-E01 in depends_on, Uncertainty-Halbsatz ('bereits 2027') nun gedeckt; Wert, Bezug, Zeitbezug, Zielkennzeichnung korrekt (P-W13).",
      "fingerprint": "061b311ea98aa7e8ae3b449d817e6f4fa81bf5e9dc923f5e4a23ef0789a88364"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-rheinmetall-spectrum",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Rheinmetall-Zellen gegen Plan v1 und Fakten geprüft. Spektrum: Profil nur aus Herstellerangaben, gelenktes Geschoss als Beleglücke. Integration 3/4: Aschau (55 %, P-W40/C-STR-25) operativ, RDX Unterlüß/Várpalota und Victoria (Pulver, 2028) Planstände -> nächste Stufe korrekt begründet. Kapazität: 1,5 Mio/Jahr ist Herstellerziel (konzernweit, Zieljahr 2030), Werks-/Hochlaufwerte als Plan, Maryborough nur beauftragt; Headline kennzeichnet 'Ziel'. Beschaffung 4/4: Bundeswehr-Rahmen (bis 8,5 Mrd, Höchstwert), RDM-Rahmen, Ukraine-Auftrag; Liefer-/Einsatzangaben als Hersteller ausgewiesen. Industrial 4/4: DE/ES/ZA operativ, Baisogala im Bau (Spatenstich 04.11.2025), Verzug nur Medienangabe, Australien/Lettland nicht gezählt.",
      "fingerprint": "6b52de1892543923cc8a4b1838cb7006c80c638d0d13b5fc8259a3ea6c936a61"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-rheinmetall-integration",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Rheinmetall-Zellen gegen Plan v1 und Fakten geprüft. Spektrum: Profil nur aus Herstellerangaben, gelenktes Geschoss als Beleglücke. Integration 3/4: Aschau (55 %, P-W40/C-STR-25) operativ, RDX Unterlüß/Várpalota und Victoria (Pulver, 2028) Planstände -> nächste Stufe korrekt begründet. Kapazität: 1,5 Mio/Jahr ist Herstellerziel (konzernweit, Zieljahr 2030), Werks-/Hochlaufwerte als Plan, Maryborough nur beauftragt; Headline kennzeichnet 'Ziel'. Beschaffung 4/4: Bundeswehr-Rahmen (bis 8,5 Mrd, Höchstwert), RDM-Rahmen, Ukraine-Auftrag; Liefer-/Einsatzangaben als Hersteller ausgewiesen. Industrial 4/4: DE/ES/ZA operativ, Baisogala im Bau (Spatenstich 04.11.2025), Verzug nur Medienangabe, Australien/Lettland nicht gezählt.",
      "fingerprint": "cb51c6d1b1e82f266edab87ce345f4a9646d9236d98c3a61c5a2a5e154150aaa"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-rheinmetall-capacity",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Rheinmetall-Zellen gegen Plan v1 und Fakten geprüft. Spektrum: Profil nur aus Herstellerangaben, gelenktes Geschoss als Beleglücke. Integration 3/4: Aschau (55 %, P-W40/C-STR-25) operativ, RDX Unterlüß/Várpalota und Victoria (Pulver, 2028) Planstände -> nächste Stufe korrekt begründet. Kapazität: 1,5 Mio/Jahr ist Herstellerziel (konzernweit, Zieljahr 2030), Werks-/Hochlaufwerte als Plan, Maryborough nur beauftragt; Headline kennzeichnet 'Ziel'. Beschaffung 4/4: Bundeswehr-Rahmen (bis 8,5 Mrd, Höchstwert), RDM-Rahmen, Ukraine-Auftrag; Liefer-/Einsatzangaben als Hersteller ausgewiesen. Industrial 4/4: DE/ES/ZA operativ, Baisogala im Bau (Spatenstich 04.11.2025), Verzug nur Medienangabe, Australien/Lettland nicht gezählt.",
      "fingerprint": "9ce3288bda69570e8f8d442419432dc57764410a579dbc7dfdb0b9ea2a57637c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-rheinmetall-procurement",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Rheinmetall-Zellen gegen Plan v1 und Fakten geprüft. Spektrum: Profil nur aus Herstellerangaben, gelenktes Geschoss als Beleglücke. Integration 3/4: Aschau (55 %, P-W40/C-STR-25) operativ, RDX Unterlüß/Várpalota und Victoria (Pulver, 2028) Planstände -> nächste Stufe korrekt begründet. Kapazität: 1,5 Mio/Jahr ist Herstellerziel (konzernweit, Zieljahr 2030), Werks-/Hochlaufwerte als Plan, Maryborough nur beauftragt; Headline kennzeichnet 'Ziel'. Beschaffung 4/4: Bundeswehr-Rahmen (bis 8,5 Mrd, Höchstwert), RDM-Rahmen, Ukraine-Auftrag; Liefer-/Einsatzangaben als Hersteller ausgewiesen. Industrial 4/4: DE/ES/ZA operativ, Baisogala im Bau (Spatenstich 04.11.2025), Verzug nur Medienangabe, Australien/Lettland nicht gezählt.",
      "fingerprint": "29a522e006c9070db92012ffb744350911f8d13d903012a9022031c45ffd6a5e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-rheinmetall-industrial",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Rheinmetall-Zellen gegen Plan v1 und Fakten geprüft. Spektrum: Profil nur aus Herstellerangaben, gelenktes Geschoss als Beleglücke. Integration 3/4: Aschau (55 %, P-W40/C-STR-25) operativ, RDX Unterlüß/Várpalota und Victoria (Pulver, 2028) Planstände -> nächste Stufe korrekt begründet. Kapazität: 1,5 Mio/Jahr ist Herstellerziel (konzernweit, Zieljahr 2030), Werks-/Hochlaufwerte als Plan, Maryborough nur beauftragt; Headline kennzeichnet 'Ziel'. Beschaffung 4/4: Bundeswehr-Rahmen (bis 8,5 Mrd, Höchstwert), RDM-Rahmen, Ukraine-Auftrag; Liefer-/Einsatzangaben als Hersteller ausgewiesen. Industrial 4/4: DE/ES/ZA operativ, Baisogala im Bau (Spatenstich 04.11.2025), Verzug nur Medienangabe, Australien/Lettland nicht gezählt.",
      "fingerprint": "cfe4692706ce9d721c91bb25ce45d1e045672548bc946ede9cdf9c1b4f62933a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-rheinmetall-range",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Ermessensfrage (d) geprüft: M-RHM-02 liefert nur Testwerte 06.11.2019 (67/76/54 km, Herstellerangabe, 76 km mit nicht JBMoU-konformem Geschütz), ohne eindeutige Geschossvariante/Ladung je Schuss und ohne Datenblattwert. Der Plan verlangt Datenblatt oder dokumentierten Test mit Rohr/Ladung und trennt Test- von Datenblattwerten; 'nicht öffentlich belegt' mit Wert null ist sachgerecht, alle Testwerte stehen vollständig im coverage_note, keine Schwächenaussage ('Keine Aussage, dass die Fähigkeit fehlt'). Hinweis (nicht blockierend): BAE/KNDS-Werte sind ebenfalls ohne Ladungsangabe bewertet; tragender Unterschied bei Rheinmetall ist das Fehlen eines Datenblattwerts bzw. der Variantenzuordnung, was das coverage_note benennt.",
      "fingerprint": "ff3e09a04b05161b531613106fa56497d4c0bd85973c2a70c2f1d2648dff5549"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-nammo-spectrum",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Nammo-Zellen geprüft: Spektrum aus Produktseiten (Raketen-/Ramjet-Geschosse nur erwähnt, kein Serienstatus). Reichweite 41 km IM HE-ER Base Bleed L52 (Datenblatt, Ladung 6 DM72). Integration 3/4 (Vihtavuori/Mesa, Sprengstoff nicht konkret belegt). Kapazität: nur Medienziel 200.000/Jahr bis 2028 (NYT via DIE), als Ziel gekennzeichnet; Perry-Ladungen nicht als Geschosse gezählt. Beschaffung 3/4 konservativ, nächste Stufe mit Beleglücken begründet. Industrial 4/4 (NO/FI/US + Raufoss-Neubau); 'neun Fertigungsländer' nicht als 155-mm-Beleg gewertet.",
      "fingerprint": "2202a8cf1600d731e4b5f69b13c6988af455f019cb412c3f697d251a6ac2ff0a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-nammo-range",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Nammo-Zellen geprüft: Spektrum aus Produktseiten (Raketen-/Ramjet-Geschosse nur erwähnt, kein Serienstatus). Reichweite 41 km IM HE-ER Base Bleed L52 (Datenblatt, Ladung 6 DM72). Integration 3/4 (Vihtavuori/Mesa, Sprengstoff nicht konkret belegt). Kapazität: nur Medienziel 200.000/Jahr bis 2028 (NYT via DIE), als Ziel gekennzeichnet; Perry-Ladungen nicht als Geschosse gezählt. Beschaffung 3/4 konservativ, nächste Stufe mit Beleglücken begründet. Industrial 4/4 (NO/FI/US + Raufoss-Neubau); 'neun Fertigungsländer' nicht als 155-mm-Beleg gewertet.",
      "fingerprint": "858b7b1f0250c1eb2f5604608c392d5bd83ad5ba1ee84c8528e52b823d083665"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-nammo-integration",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Nammo-Zellen geprüft: Spektrum aus Produktseiten (Raketen-/Ramjet-Geschosse nur erwähnt, kein Serienstatus). Reichweite 41 km IM HE-ER Base Bleed L52 (Datenblatt, Ladung 6 DM72). Integration 3/4 (Vihtavuori/Mesa, Sprengstoff nicht konkret belegt). Kapazität: nur Medienziel 200.000/Jahr bis 2028 (NYT via DIE), als Ziel gekennzeichnet; Perry-Ladungen nicht als Geschosse gezählt. Beschaffung 3/4 konservativ, nächste Stufe mit Beleglücken begründet. Industrial 4/4 (NO/FI/US + Raufoss-Neubau); 'neun Fertigungsländer' nicht als 155-mm-Beleg gewertet.",
      "fingerprint": "e4292e63e40d20c3d3e7ab3c8860b9217053c322c25ced494986ea102bc9db1f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-nammo-capacity",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Nammo-Zellen geprüft: Spektrum aus Produktseiten (Raketen-/Ramjet-Geschosse nur erwähnt, kein Serienstatus). Reichweite 41 km IM HE-ER Base Bleed L52 (Datenblatt, Ladung 6 DM72). Integration 3/4 (Vihtavuori/Mesa, Sprengstoff nicht konkret belegt). Kapazität: nur Medienziel 200.000/Jahr bis 2028 (NYT via DIE), als Ziel gekennzeichnet; Perry-Ladungen nicht als Geschosse gezählt. Beschaffung 3/4 konservativ, nächste Stufe mit Beleglücken begründet. Industrial 4/4 (NO/FI/US + Raufoss-Neubau); 'neun Fertigungsländer' nicht als 155-mm-Beleg gewertet.",
      "fingerprint": "a6e8e8f841782049d6ec691117b5bd58324347fa09d2d7abaf4fd0ff4ce234e5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-nammo-procurement",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Nammo-Zellen geprüft: Spektrum aus Produktseiten (Raketen-/Ramjet-Geschosse nur erwähnt, kein Serienstatus). Reichweite 41 km IM HE-ER Base Bleed L52 (Datenblatt, Ladung 6 DM72). Integration 3/4 (Vihtavuori/Mesa, Sprengstoff nicht konkret belegt). Kapazität: nur Medienziel 200.000/Jahr bis 2028 (NYT via DIE), als Ziel gekennzeichnet; Perry-Ladungen nicht als Geschosse gezählt. Beschaffung 3/4 konservativ, nächste Stufe mit Beleglücken begründet. Industrial 4/4 (NO/FI/US + Raufoss-Neubau); 'neun Fertigungsländer' nicht als 155-mm-Beleg gewertet.",
      "fingerprint": "a060f28a18407a80cc38a95c5bf2b6870602f9449a68949f1dc6e5076bddcce4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-nammo-industrial",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Nammo-Zellen geprüft: Spektrum aus Produktseiten (Raketen-/Ramjet-Geschosse nur erwähnt, kein Serienstatus). Reichweite 41 km IM HE-ER Base Bleed L52 (Datenblatt, Ladung 6 DM72). Integration 3/4 (Vihtavuori/Mesa, Sprengstoff nicht konkret belegt). Kapazität: nur Medienziel 200.000/Jahr bis 2028 (NYT via DIE), als Ziel gekennzeichnet; Perry-Ladungen nicht als Geschosse gezählt. Beschaffung 3/4 konservativ, nächste Stufe mit Beleglücken begründet. Industrial 4/4 (NO/FI/US + Raufoss-Neubau); 'neun Fertigungsländer' nicht als 155-mm-Beleg gewertet.",
      "fingerprint": "1c8d5396712ebe645c791726793f0c820e6e742a157a13391afc054588cd88db"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-knds-spectrum",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. KNDS-Zellen geprüft: Spektrum aus Katalog 2026-27 (KATANA gelenkt, BONUS). Reichweite 40 km nur für LU 211 mit Rohrlänge; LU 220/KATANA ohne Rohr/Ladung bewusst nicht als Kennwert übernommen. Beschaffung 4/4 (NSPA-Rahmen mehrere Staaten, Bundeswehr-Auftrag für Ukraine, Einsatz laut KNDS). Industrial 4/4: FR/BE/IT; Italien stützt sich auf Katalog und großkalibrige Fertigung laut Euronews (in uncertainty offengelegt), 'Neubau' ist eine neue Linie an bestehendem Standort (offengelegt) - nicht blockierend: Wortlaut 'fertigt in Italien' bleibt an den Katalogbezug gebunden.",
      "fingerprint": "4961ca28fc9693bad34aaed17457e5321c98de1dab6ddcbd8b1a3511761eff82"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-knds-range",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. KNDS-Zellen geprüft: Spektrum aus Katalog 2026-27 (KATANA gelenkt, BONUS). Reichweite 40 km nur für LU 211 mit Rohrlänge; LU 220/KATANA ohne Rohr/Ladung bewusst nicht als Kennwert übernommen. Beschaffung 4/4 (NSPA-Rahmen mehrere Staaten, Bundeswehr-Auftrag für Ukraine, Einsatz laut KNDS). Industrial 4/4: FR/BE/IT; Italien stützt sich auf Katalog und großkalibrige Fertigung laut Euronews (in uncertainty offengelegt), 'Neubau' ist eine neue Linie an bestehendem Standort (offengelegt) - nicht blockierend: Wortlaut 'fertigt in Italien' bleibt an den Katalogbezug gebunden.",
      "fingerprint": "1a57ac270a6b94fe2cf0ed9d17f23a05a876397a0ad7a9ba4c1aaa11b0930b9a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-knds-procurement",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. KNDS-Zellen geprüft: Spektrum aus Katalog 2026-27 (KATANA gelenkt, BONUS). Reichweite 40 km nur für LU 211 mit Rohrlänge; LU 220/KATANA ohne Rohr/Ladung bewusst nicht als Kennwert übernommen. Beschaffung 4/4 (NSPA-Rahmen mehrere Staaten, Bundeswehr-Auftrag für Ukraine, Einsatz laut KNDS). Industrial 4/4: FR/BE/IT; Italien stützt sich auf Katalog und großkalibrige Fertigung laut Euronews (in uncertainty offengelegt), 'Neubau' ist eine neue Linie an bestehendem Standort (offengelegt) - nicht blockierend: Wortlaut 'fertigt in Italien' bleibt an den Katalogbezug gebunden.",
      "fingerprint": "3f44ada68981f968f9b3667bf041ff0f3dc6dc68a28349d475159b9dc759279c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-knds-industrial",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. KNDS-Zellen geprüft: Spektrum aus Katalog 2026-27 (KATANA gelenkt, BONUS). Reichweite 40 km nur für LU 211 mit Rohrlänge; LU 220/KATANA ohne Rohr/Ladung bewusst nicht als Kennwert übernommen. Beschaffung 4/4 (NSPA-Rahmen mehrere Staaten, Bundeswehr-Auftrag für Ukraine, Einsatz laut KNDS). Industrial 4/4: FR/BE/IT; Italien stützt sich auf Katalog und großkalibrige Fertigung laut Euronews (in uncertainty offengelegt), 'Neubau' ist eine neue Linie an bestehendem Standort (offengelegt) - nicht blockierend: Wortlaut 'fertigt in Italien' bleibt an den Katalogbezug gebunden.",
      "fingerprint": "9b5b699e53947e356c00d1a4d45ae098f017799923fdb7734bf4e80998b5ce82"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-knds-integration",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Ermessensfrage (d) KNDS-Kapazität: 'nicht öffentlich belegt' ist sachgerecht, weil die einzige Werkszahl (100.000/Jahr, La Chapelle-Saint-Ursin) ohne Zieljahr und nur sekundär (Le Monde via Euromaidan Press) vorliegt, Polen-180.000 ein Partnerwerk und Tarbes nur Hüllen betrifft; Plan verlangt Zieljahr und Werk/Konzern-Kennzeichnung. coverage_note nennt alle Werte, keine Schwächenaussage. Integration: keine eigene Pulver-/Sprengstofffertigung belegt, Anker 1 ausdrücklich nicht vergeben, Colleferro-Explosion nicht als Herstellung gewertet.",
      "fingerprint": "2aea8de48badc07643177ecdb9b0848021bf8632fc3b320a701f5df4e3806e69"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-knds-capacity",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Ermessensfrage (d) KNDS-Kapazität: 'nicht öffentlich belegt' ist sachgerecht, weil die einzige Werkszahl (100.000/Jahr, La Chapelle-Saint-Ursin) ohne Zieljahr und nur sekundär (Le Monde via Euromaidan Press) vorliegt, Polen-180.000 ein Partnerwerk und Tarbes nur Hüllen betrifft; Plan verlangt Zieljahr und Werk/Konzern-Kennzeichnung. coverage_note nennt alle Werte, keine Schwächenaussage. Integration: keine eigene Pulver-/Sprengstofffertigung belegt, Anker 1 ausdrücklich nicht vergeben, Colleferro-Explosion nicht als Herstellung gewertet.",
      "fingerprint": "a7a5a15bf455492137b5f93b5351c9c0ea9bd5e099bae8bf692382f4fc7f2ea4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-bae-spectrum",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. BAE-Zellen geprüft: Spektrum aus Broschüre 02/2026, Bofors/gelenkte Produkte wegen Zugriffsgrenze ausdrücklich nicht geprüft. Reichweite: XL12E1 40 km L/52 (nicht im Dienst, im Kurzfeld ausgewiesen), L15 32 km. Kapazität: Sechzehnfach-Steigerung ohne Basiswert -> null mit coverage_note. Beschaffung 3/4 (280-Mio-GBP-Auftrag im 15-Jahres-NGMS). Industrial 3/4 (UK, US-Energetik); nicht blockierend: das Bofors-Zugriffsproblem steht nur in der Spektrum-Zelle, 'drittes Fertigungsland nicht belegt' bleibt reine Belegaussage.",
      "fingerprint": "5404632d2088152d34db9b7a86c927455774d60013276f3033704227fbc3301e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-bae-range",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. BAE-Zellen geprüft: Spektrum aus Broschüre 02/2026, Bofors/gelenkte Produkte wegen Zugriffsgrenze ausdrücklich nicht geprüft. Reichweite: XL12E1 40 km L/52 (nicht im Dienst, im Kurzfeld ausgewiesen), L15 32 km. Kapazität: Sechzehnfach-Steigerung ohne Basiswert -> null mit coverage_note. Beschaffung 3/4 (280-Mio-GBP-Auftrag im 15-Jahres-NGMS). Industrial 3/4 (UK, US-Energetik); nicht blockierend: das Bofors-Zugriffsproblem steht nur in der Spektrum-Zelle, 'drittes Fertigungsland nicht belegt' bleibt reine Belegaussage.",
      "fingerprint": "fcb489e06e7d17089e375829cf0e1befe00e9db0e943c80e31ad8014e7e1fa50"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-bae-capacity",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. BAE-Zellen geprüft: Spektrum aus Broschüre 02/2026, Bofors/gelenkte Produkte wegen Zugriffsgrenze ausdrücklich nicht geprüft. Reichweite: XL12E1 40 km L/52 (nicht im Dienst, im Kurzfeld ausgewiesen), L15 32 km. Kapazität: Sechzehnfach-Steigerung ohne Basiswert -> null mit coverage_note. Beschaffung 3/4 (280-Mio-GBP-Auftrag im 15-Jahres-NGMS). Industrial 3/4 (UK, US-Energetik); nicht blockierend: das Bofors-Zugriffsproblem steht nur in der Spektrum-Zelle, 'drittes Fertigungsland nicht belegt' bleibt reine Belegaussage.",
      "fingerprint": "52d474c4668c08c8eda5e91b1c8f383e469033e515812cd5833411053f98e211"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-bae-procurement",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. BAE-Zellen geprüft: Spektrum aus Broschüre 02/2026, Bofors/gelenkte Produkte wegen Zugriffsgrenze ausdrücklich nicht geprüft. Reichweite: XL12E1 40 km L/52 (nicht im Dienst, im Kurzfeld ausgewiesen), L15 32 km. Kapazität: Sechzehnfach-Steigerung ohne Basiswert -> null mit coverage_note. Beschaffung 3/4 (280-Mio-GBP-Auftrag im 15-Jahres-NGMS). Industrial 3/4 (UK, US-Energetik); nicht blockierend: das Bofors-Zugriffsproblem steht nur in der Spektrum-Zelle, 'drittes Fertigungsland nicht belegt' bleibt reine Belegaussage.",
      "fingerprint": "9c7baf76266d0509fe4c14b848f25117a556af1dd11bf46f82fbb613a2cff118"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-bae-industrial",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. BAE-Zellen geprüft: Spektrum aus Broschüre 02/2026, Bofors/gelenkte Produkte wegen Zugriffsgrenze ausdrücklich nicht geprüft. Reichweite: XL12E1 40 km L/52 (nicht im Dienst, im Kurzfeld ausgewiesen), L15 32 km. Kapazität: Sechzehnfach-Steigerung ohne Basiswert -> null mit coverage_note. Beschaffung 3/4 (280-Mio-GBP-Auftrag im 15-Jahres-NGMS). Industrial 3/4 (UK, US-Energetik); nicht blockierend: das Bofors-Zugriffsproblem steht nur in der Spektrum-Zelle, 'drittes Fertigungsland nicht belegt' bleibt reine Belegaussage.",
      "fingerprint": "af86e88019157372e305d0d62b9911a8285f7a0ed7f2e590bfd24d5afff62294"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-bae-integration",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Ermessensfrage (b) BAE-Integration 4/4 geprüft: M-BAE-06 belegt BAE OSI als Betreiber von Holston (RDX/HMX) und Radford (Nitrozellulose, Treibmittel) und damit operative Sprengstoff- und Treibmittelfertigung; der Anker 4 sagt 'eigene operative Fertigung'. Die Einstufung ist vertretbar, weil Betreibermodell, Army-Eigentum, Interview-Herkunft und fehlender Bezug zur britischen 155-mm-Kette in Headline ('als Betreiber staatlicher US-Werke'), Preview ('UK ohne eigene Sprengstoffe'), uncertainty und next_stage_limit offengelegt sind; I-MI-market-1 relativiert korrekt ('nur über US-Betreiberwerke'). Nicht blockierend, aber die Sichtbarkeit der Einschränkung im Kurzfeld muss erhalten bleiben.",
      "fingerprint": "438056ba61336af87113e6b2894d2f22ac07d5a7ecab7efe05042dad9c04023c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-gdots-spectrum",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. GD-OTS-Zellen geprüft: Spektrum (SMArt-Fertigungsrolle offen), Reichweite 40 km M1128-I mit MCS Zone 6H aus L52 (teils Simulation, offengelegt), Integration 3/4 (Valleyfield Treibmittel, Füllung nicht als Synthese gewertet), Kapazität: Mesquite-30.000/Monat nur medial GD-OTS zugeordnet und nicht erreicht - korrekt als Beleggrenze statt Wert/Schwäche geführt, Zuordnung im Kurzfeld als 'medial' gekennzeichnet. Industrial 3/4 (US, CA); Mesquite-Probleme nur medial zugeordnet.",
      "fingerprint": "9300baf31c0b7a634ac863292309d909412534c24e8c37d7051204e6710d9d75"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-gdots-range",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. GD-OTS-Zellen geprüft: Spektrum (SMArt-Fertigungsrolle offen), Reichweite 40 km M1128-I mit MCS Zone 6H aus L52 (teils Simulation, offengelegt), Integration 3/4 (Valleyfield Treibmittel, Füllung nicht als Synthese gewertet), Kapazität: Mesquite-30.000/Monat nur medial GD-OTS zugeordnet und nicht erreicht - korrekt als Beleggrenze statt Wert/Schwäche geführt, Zuordnung im Kurzfeld als 'medial' gekennzeichnet. Industrial 3/4 (US, CA); Mesquite-Probleme nur medial zugeordnet.",
      "fingerprint": "c3ee713cee0030c775137ce2980073bad97d25d98586e696c0c49b381b199294"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-gdots-integration",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. GD-OTS-Zellen geprüft: Spektrum (SMArt-Fertigungsrolle offen), Reichweite 40 km M1128-I mit MCS Zone 6H aus L52 (teils Simulation, offengelegt), Integration 3/4 (Valleyfield Treibmittel, Füllung nicht als Synthese gewertet), Kapazität: Mesquite-30.000/Monat nur medial GD-OTS zugeordnet und nicht erreicht - korrekt als Beleggrenze statt Wert/Schwäche geführt, Zuordnung im Kurzfeld als 'medial' gekennzeichnet. Industrial 3/4 (US, CA); Mesquite-Probleme nur medial zugeordnet.",
      "fingerprint": "e9a748e21deaacd746f1b218bcedc105b8b4039e107748cf57318bc0ddc45879"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-gdots-capacity",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. GD-OTS-Zellen geprüft: Spektrum (SMArt-Fertigungsrolle offen), Reichweite 40 km M1128-I mit MCS Zone 6H aus L52 (teils Simulation, offengelegt), Integration 3/4 (Valleyfield Treibmittel, Füllung nicht als Synthese gewertet), Kapazität: Mesquite-30.000/Monat nur medial GD-OTS zugeordnet und nicht erreicht - korrekt als Beleggrenze statt Wert/Schwäche geführt, Zuordnung im Kurzfeld als 'medial' gekennzeichnet. Industrial 3/4 (US, CA); Mesquite-Probleme nur medial zugeordnet.",
      "fingerprint": "396445d86b330907fb4d6050aad04377a194d426b64df9ef061f3cba8403d0ba"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-gdots-industrial",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. GD-OTS-Zellen geprüft: Spektrum (SMArt-Fertigungsrolle offen), Reichweite 40 km M1128-I mit MCS Zone 6H aus L52 (teils Simulation, offengelegt), Integration 3/4 (Valleyfield Treibmittel, Füllung nicht als Synthese gewertet), Kapazität: Mesquite-30.000/Monat nur medial GD-OTS zugeordnet und nicht erreicht - korrekt als Beleggrenze statt Wert/Schwäche geführt, Zuordnung im Kurzfeld als 'medial' gekennzeichnet. Industrial 3/4 (US, CA); Mesquite-Probleme nur medial zugeordnet.",
      "fingerprint": "d8f51f68ab2233056c151f2177a3ef12eb40f7eafbb6feda5a84a6f780fa5e8b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-gdots-procurement",
      "evidence_review": "Runde-2: MACS nur noch als Herstellerrolle laut Produktseite (M-GDO-01), nicht als Vertrag; Stufe 2, next_stage_limit und Ermessensentscheidung unverändert tragfähig.",
      "fingerprint": "9e5c2290ad9475feabe60cc5753d24d8151e5d1b72589c0ad4a508bd99a117a4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-hanwha-spectrum",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Hanwha-Zellen geprüft: Spektrum (MCS-Exportverträge; ER-Serienstart nur laut Medien-Anrisstext), Reichweite null (keine Datenangabe), Integration 3/4 nur auf Medien/Werksbesuch (Hanwha-finanzierte Reise offengelegt), Kapazität null weil Angaben in Treibladungsmodulen (keine Umrechnung übernommen), Beschaffung 3/4 (FMV-Rahmen, BAE-Vertrag; betrifft Treibladungen, im Kurzfeld genannt), Industrial 2/4 (mehrere koreanische Werke, US-Campus nur geplant).",
      "fingerprint": "92697e404013ddcd407498a9e0f28121e3842675a20b32406304c1e656830b8a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-hanwha-range",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Hanwha-Zellen geprüft: Spektrum (MCS-Exportverträge; ER-Serienstart nur laut Medien-Anrisstext), Reichweite null (keine Datenangabe), Integration 3/4 nur auf Medien/Werksbesuch (Hanwha-finanzierte Reise offengelegt), Kapazität null weil Angaben in Treibladungsmodulen (keine Umrechnung übernommen), Beschaffung 3/4 (FMV-Rahmen, BAE-Vertrag; betrifft Treibladungen, im Kurzfeld genannt), Industrial 2/4 (mehrere koreanische Werke, US-Campus nur geplant).",
      "fingerprint": "e007fdfe0f88148811f21a48aab34d0f02207448ce739c0d4b80bc5d3c8db676"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-hanwha-integration",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Hanwha-Zellen geprüft: Spektrum (MCS-Exportverträge; ER-Serienstart nur laut Medien-Anrisstext), Reichweite null (keine Datenangabe), Integration 3/4 nur auf Medien/Werksbesuch (Hanwha-finanzierte Reise offengelegt), Kapazität null weil Angaben in Treibladungsmodulen (keine Umrechnung übernommen), Beschaffung 3/4 (FMV-Rahmen, BAE-Vertrag; betrifft Treibladungen, im Kurzfeld genannt), Industrial 2/4 (mehrere koreanische Werke, US-Campus nur geplant).",
      "fingerprint": "8670471515ddbc8afd74e3a22c25259b8c16818bbd371a4c62c9dcdb2ecbb788"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-hanwha-capacity",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Hanwha-Zellen geprüft: Spektrum (MCS-Exportverträge; ER-Serienstart nur laut Medien-Anrisstext), Reichweite null (keine Datenangabe), Integration 3/4 nur auf Medien/Werksbesuch (Hanwha-finanzierte Reise offengelegt), Kapazität null weil Angaben in Treibladungsmodulen (keine Umrechnung übernommen), Beschaffung 3/4 (FMV-Rahmen, BAE-Vertrag; betrifft Treibladungen, im Kurzfeld genannt), Industrial 2/4 (mehrere koreanische Werke, US-Campus nur geplant).",
      "fingerprint": "b23cf640c380fc1731cbe3f0e40e2e5cb928551d8c4bcbd99ecc805d2f0200fd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-hanwha-procurement",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Hanwha-Zellen geprüft: Spektrum (MCS-Exportverträge; ER-Serienstart nur laut Medien-Anrisstext), Reichweite null (keine Datenangabe), Integration 3/4 nur auf Medien/Werksbesuch (Hanwha-finanzierte Reise offengelegt), Kapazität null weil Angaben in Treibladungsmodulen (keine Umrechnung übernommen), Beschaffung 3/4 (FMV-Rahmen, BAE-Vertrag; betrifft Treibladungen, im Kurzfeld genannt), Industrial 2/4 (mehrere koreanische Werke, US-Campus nur geplant).",
      "fingerprint": "36f13870593923ed45a89d612df1fe36f8275c78c21265cf477310d0204956f2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-M-hanwha-industrial",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Hanwha-Zellen geprüft: Spektrum (MCS-Exportverträge; ER-Serienstart nur laut Medien-Anrisstext), Reichweite null (keine Datenangabe), Integration 3/4 nur auf Medien/Werksbesuch (Hanwha-finanzierte Reise offengelegt), Kapazität null weil Angaben in Treibladungsmodulen (keine Umrechnung übernommen), Beschaffung 3/4 (FMV-Rahmen, BAE-Vertrag; betrifft Treibladungen, im Kurzfeld genannt), Industrial 2/4 (mehrere koreanische Werke, US-Campus nur geplant).",
      "fingerprint": "9ec123aae17433eb898f693f93c303aed2403de5cba59ef0dcf0f0122f2d3318"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-boxer",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-V13/P-V10/P-V14/P-V11/P-V12: 100. Boxer-MIV 25.06.2026 (Herstellerangabe) trägt Stufe 6 für die Basisplattform; Schakal, RCH 155 und Schwerer Waffenträger als eigene Varianten mit abweichendem Stand (Auftrag/Verzug) getrennt, next_stage_limit begrenzt die Übertragung.",
      "fingerprint": "06ce8854574ed315fe82f22b811c19d0510d0acc0235d84d18c02fee3d8746b3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-puma",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-V21/P-V20: Übergabe des ersten Puma aus dem zweiten Los (28.08.2026, Fachmedium mit PSM-Verweis) und 200-Fahrzeug-Folgebestellung getrennt; Stufe 6 vertretbar, Sekundärquelle in uncertainty offengelegt.",
      "fingerprint": "f8d433abb97bcbf7c104a543d3355ad579584248fd00d32a4246da6ad08b76a8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-lynx",
      "evidence_review": "Runde-2: Statement auf Serienfertigungsbeginn mit erstem lokal gefertigten Fahrzeug 07/2024 laut Rheinmetall und Italien (erste vier, 01/2026) begrenzt; P-R61 in depends_on; Uncertainty zum Stand 2026 konsistent; XM30/Rumänien getrennt. Stufe 6 vertretbar.",
      "fingerprint": "299a6f38064645ee0128bf306d45bedc54a6d354e87a375f899ba8de16b9b978"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-mbt",
      "evidence_review": "Runde-2: 'ohne belegten Auftrag' (P-V41); Stufe 4 durch P-V40/P-V16/C-MKT-08 getragen.",
      "fingerprint": "968c69597b23905fcf041105dadf4ffaddb008a0ec4912ff7b62bece84d717d2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-trucks",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-V50/P-V51/P-V52: über 20.000 HX im Einsatz bzw. über 16.000 verkauft (Herstellerzahlen, Abweichung in uncertainty), Abruf von über 2.000 UTF; Stufe 6 durch tatsächlich gelieferte Skalierung getragen, Autonomie-Kits ausgeklammert.",
      "fingerprint": "c840c9a4540448599824006d4919b15b5f20e83ee717c03bcf66d93ba03621d3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-lightveh",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Vier 'nicht eindeutig bestimmbar'-Einträge: score null, coverage_note nennt die konkrete Beleggrenze (nur Portfolio-/Selbstdarstellungsangaben, Anduril-Integration nur angekündigt); Reasoning/uncertainty stellen ausdrücklich Beleglücke und nicht Unreife fest; kein SWOT hängt an diesen Einträgen.",
      "fingerprint": "1fcb7bbea30a67f7e92b161e5265850fd6b66ef0960e2b59de0db1b036d868da"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-airsensors",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Vier 'nicht eindeutig bestimmbar'-Einträge: score null, coverage_note nennt die konkrete Beleggrenze (nur Portfolio-/Selbstdarstellungsangaben, Anduril-Integration nur angekündigt); Reasoning/uncertainty stellen ausdrücklich Beleglücke und nicht Unreife fest; kein SWOT hängt an diesen Einträgen.",
      "fingerprint": "cba0581ea1f8bf6ea63414ad21e90f132773b11055bee379d5bc0f29985b720f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-battlesuite",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Vier 'nicht eindeutig bestimmbar'-Einträge: score null, coverage_note nennt die konkrete Beleggrenze (nur Portfolio-/Selbstdarstellungsangaben, Anduril-Integration nur angekündigt); Reasoning/uncertainty stellen ausdrücklich Beleglücke und nicht Unreife fest; kein SWOT hängt an diesen Einträgen.",
      "fingerprint": "dc11b10009058aa924c3cde1cec8acc403045513f5a29cae5be14ce2c560a78c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-civilrest",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Vier 'nicht eindeutig bestimmbar'-Einträge: score null, coverage_note nennt die konkrete Beleggrenze (nur Portfolio-/Selbstdarstellungsangaben, Anduril-Integration nur angekündigt); Reasoning/uncertainty stellen ausdrücklich Beleglücke und nicht Unreife fest; kein SWOT hängt an diesen Einträgen.",
      "fingerprint": "61e323faa19acab346c415d3ddf91807f565d7944d2fa84b1539e7b331eaf2ce"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-ugv",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-V70/P-V71: Wild Goose 'fully fielded' ausdrücklich als Herstellerangabe, MUSKOX/Mission Master SP als Programmauswahl, Ox im Wettbewerb; Stufe 5 mit Herstellerzuschreibung und Variantenunterschied vertretbar.",
      "fingerprint": "0847e22fb5f42d904a2ed208fd0ee1f7f16c00b6f25d663788c20cc999bf1187"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-vsvc",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-V72/P-R98/P-R130: laufende Instandhaltung (Singapur MRO, Westukraine seit 06/2024); Stufe 5 getragen, undatierte Seiten in uncertainty.",
      "fingerprint": "9d9945f3e7e02aba4b16470486aee9ee02b5918f4cc2276077b7df9226171860"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-art155",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-W10/P-W11/P-W12/P-W13: Unterlüß seit 05.09.2025 in Betrieb, laut Hersteller hunderttausende Geschosse in die Ukraine geliefert; Stufe 6 vertretbar, Herstellerangabe und Firepower-Ziel (kein Meilenstein) getrennt.",
      "fingerprint": "af7a622efd16ef5b3e2e926829d03e0acc62a6762c63ac374be6c5991bb6442b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-medcal",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-W20/P-W21/P-W02/P-W12/T-06: Lieferung 35-mm-Munition Ukraine (Hersteller), Puma-Munition abgerufen, Umsatztreiber; Albacete-Linie als Kapazitätserweiterung getrennt; Stufe 6 vertretbar.",
      "fingerprint": "6eb62db7c8df1341a3e7124bf1588709756122ff924d0a87f35a20f84fda62a8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-gunsys",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-V14/P-W30/P-W31: RCH-155-Auftrag UK (Stufe 4); Leopard-2-Kanone nur undatierte Selbstdarstellung und 130-mm/L60 in Test nach Investorenpräsentation -> Beleglücke, keine Reifeaussage; Telford-Werk als schrittweise im Betrieb.",
      "fingerprint": "c740273d85c19724c0b013947dd824de07bc7c0801913f5f380f84fac380151c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-propellant",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-W40: Aschau produziert derzeit rund 1.700 t Pulver und 300.000 Module p. a. (Herstellerangabe); Stufe 6 für Bestand, Ausbau (2027/2028) als Plan getrennt.",
      "fingerprint": "5d890e9e2ca2373f0173965d7e18f766710f06be9abd0454cfdfe90ce8e6ca60"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-mortar",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D50/P-W20: 81-mm-Mörser laut Unternehmensseite bei norwegischen Streitkräften im Einsatz (Stufe 5), Dual-Eimos-Ausbau geplant; Zuordnung zur Eimos-Familie als offen markiert.",
      "fingerprint": "59a25c3f3fc1ac4416da4e0e02bb8058288d6375611c6c6c57a5be12e0f95212"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-protect",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe-4-Einordnungen durch die konkreten Aufträge getragen (Rettungsstationen >1.056 Mio EUR; MK93 3.104 Einheiten, 20,7 Mio USD; Puma-Simulatoren 118,5 Mio EUR); heterogene Bündel bzw. offene Herkunft der 245 gelieferten MK93 in uncertainty, Lieferung/Betrieb als nicht belegt ausgewiesen.",
      "fingerprint": "9866a2656539662015dbf8243cc91f9e8b816e345cdbd8659c2a17f7ff688402"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-mount",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe-4-Einordnungen durch die konkreten Aufträge getragen (Rettungsstationen >1.056 Mio EUR; MK93 3.104 Einheiten, 20,7 Mio USD; Puma-Simulatoren 118,5 Mio EUR); heterogene Bündel bzw. offene Herkunft der 245 gelieferten MK93 in uncertainty, Lieferung/Betrieb als nicht belegt ausgewiesen.",
      "fingerprint": "41555a29c154275661efdf52f0e48eafc17bb5904a609affa36feaadf8671ac4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-defelec",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe-4-Einordnungen durch die konkreten Aufträge getragen (Rettungsstationen >1.056 Mio EUR; MK93 3.104 Einheiten, 20,7 Mio USD; Puma-Simulatoren 118,5 Mio EUR); heterogene Bündel bzw. offene Herkunft der 245 gelieferten MK93 in uncertainty, Lieferung/Betrieb als nicht belegt ausgewiesen.",
      "fingerprint": "770322f19c765dd3845e1034ae09576d1bf2d6235324316604ec145d89fbc767"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-strike",
      "evidence_review": "Runde-2: 'Gründung zum Stichtag nicht belegt' (T-E10/C-STR-36/P-W60); Stufe 1 korrekt.",
      "fingerprint": "bf8f6a671f43f8beadded4cefe30637d2506fe568cc2cbeec21bcf0a816641c1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skyranger",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-A10/P-A11/P-A12/P-A13/P-A02: Aufträge DE (19), AT (36), NL, RO (24 Skyranger 35); Prototyp an die Bundeswehr, Serienlieferung laut Medien ab Mitte 2027 gegen Rheinmetall-Angabe Februar 2028 (beide genannt); Turmkapazität 400/Jahr als Plan; Varianten 30/35 in uncertainty. Stufe 4 sachgerecht.",
      "fingerprint": "94230c5e223b8828d08d2a1062bd1ecfa8712d2ee2e263e070e505da7c61e42b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skynex",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-A14/P-A01/P-A12: erste Batterie Italien 18.12.2025 geliefert, weitere Aufträge; Stufe 4 mit Begründung, dass eine Einzellieferung keine wiederholte Auslieferung ist und Einsatz nicht recherchiert wurde.",
      "fingerprint": "0b7c4b8efa90aa711941259acf4c5f099ee1002fd6afc95a4425d4087b83b91b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-navaldef",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-A12/P-A40: Rumänien bestellte zwei Millennium Guns (Herstellerangabe), Searanger u. a. nur Angebot; Stufe 4 getragen.",
      "fingerprint": "c4576937b0268329752cd906227292e03f7fd8550817e007c18adf3a87a13be1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-cuas",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-A50: AERIE-Prototyp 07.10.2026 geliefert, Bedienerdemonstrationen erst Q4 2026; Stufe 2 vertretbar (nicht blockierend: 'funktionsfähig' im Reasoning ist eine Inferenz aus der Lieferung eines containerisierten Prototyps; Tests/Demos als nicht belegt ausgewiesen).",
      "fingerprint": "989eb616bc19261a15f47ed429fa4a5b08cf7bcb38334efc7e9799460da8ec80"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-dlbo",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D10/P-D12/P-D02/C-MKT-03/P-D11: TaWAN-Rahmenvertrag und D-LBO-Abruf (20.07.2026, ~100 Mio EUR) bzw. IdZ-ES-Abruf (~1,04 Mrd EUR brutto, Lieferung ab 11/2027) tragen Stufe 4; IdZ-ES-Quellkonflikt (1,7 vs. 3,1 Mrd EUR) in uncertainty; Einsatz/Auslieferung nicht belegt.",
      "fingerprint": "a76c682b8823f4da88bfc3e00ce94ac51a6e4d6c206f0edfbb52260c419a6e03"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-idz",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D10/P-D12/P-D02/C-MKT-03/P-D11: TaWAN-Rahmenvertrag und D-LBO-Abruf (20.07.2026, ~100 Mio EUR) bzw. IdZ-ES-Abruf (~1,04 Mrd EUR brutto, Lieferung ab 11/2027) tragen Stufe 4; IdZ-ES-Quellkonflikt (1,7 vs. 3,1 Mrd EUR) in uncertainty; Einsatz/Auslieferung nicht belegt.",
      "fingerprint": "032af20f5ff6288186405ba8f282084def2a34e32b0cf7e719e4fb7dc47a8864"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-fv014",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D20/T-E11/C-MKT-05: Rahmenvertrag 22.04.2026, Qualifikation ab Q2 2026, Lieferung ab H1 2027 (Plan); Brutto/Netto-Abweichung beim Erstabruf (300 vs. 250 Mio EUR) in uncertainty; Stufe 4 vertretbar.",
      "fingerprint": "0d040cf4299d1f7969df2637ab49b491f57d133a6ed857d68842d7b17c5a902c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-uas",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D14/P-D01/C-TEC-03: Anduril-Partnerschaft (18.06.2025) und MQ-28-Zusammenarbeit nur angekündigt, kein Prototyp/Auftrag belegt; Stufe 1, Partnerprodukte ausgeklammert.",
      "fingerprint": "2c0d338a213c1c28b984e0f43d0f908924222a879b09e45b3f013a634f1f0d41"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-sar",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D30/C-TEC-04/T-E04: Rheinmetall ICEYE betreibt die SAR-Satelliten, Bundeswehr hat laut Rheinmetall direkten Zugriff (06.10.2026); Satellitenfertigung begonnen (kein Serienbegriff). Stufe 5 für den Dienst SPOCK 1 auf Herstellerbasis, Satellitenanzahl offen - vertretbar.",
      "fingerprint": "32b704029c3228636bc49d442e8b74b16eca692530f6e85774f17de0218e418d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-airsat",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D31/T-E22: Start 01.10.2026 (Herstellerangabe) trägt Stufe 3 (durchgeführte Validierungsmission); Kundenprogramm nicht belegt.",
      "fingerprint": "297166cda4b69172184b210c2cdbb78896b7c87b882657e8550273a843084836"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-f35",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-D40/C-TEC-02: Fertigung in Weeze seit Juli 2025 im Rahmen der Industriekooperation, Auslieferungen ab 2027 vorgesehen, 400 Mittelrümpfe Planmenge; Stufe 4 mit klarer Abgrenzung zu Lieferung.",
      "fingerprint": "d862fa675a9464ad3bedbead8b957c24bd44b077ab384fb8832e5faa3c2efca6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-k130",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-N10/P-N01/P-N03: Taufe der LÜBECK (fünfte Einheit des zweiten Loses, 29.04.2026), Lieferung EMDEN/KÖLN 2026 nur Plan; Serienbau (zweites Los), Konzernzugehörigkeit erst seit 03/2026 ausgewiesen; Stufe 6 vertretbar.",
      "fingerprint": "8ebcc27bfaee710578e5c270cd08827129e054bf76db4c049c5f74ee3de6cc65"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-fdb",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-N20/P-N03/P-N01: Kiellegung drittes FDB 14.09.2026, Indienststellung ab 2029, viertes Boot nur eingeleitet; Stufe 4 getragen, MBV707-Status als nicht einzeln belegt markiert.",
      "fingerprint": "b5b8222c81e4629ef49a028c5e818ba39d3ad415438d026d54097014a3e3653a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-intlships",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-N30/P-N03/P-N31/P-N61: Rumänien vier Schiffe (920 Mio EUR in P-N03), MMPV-Konstruktion und Bau in Bulgarien, Mangalia-Übernahme noch nicht abgeschlossen, Ägypten Pipeline; Stufe 4 ohne Ablieferungsbeleg korrekt.",
      "fingerprint": "7d8c96b8999e6c011ee81046b5c1c35ae19a09f58b6ad2d1a84b8cde927bbcba"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-navservice",
      "evidence_review": "Runde-2: 39 Mio EUR als gesamter Naval-Serviceumsatz der vier Monate seit Übernahme ausgewiesen (P-N03); Stufe 5 getragen.",
      "fingerprint": "cca74c5653bd7f74a4d332633dd6249124ccc9622190ff4368b029fd75df6062"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-usv",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Ermessensfrage (a) Kraken K3 Scout Stufe 6 geprüft: Stufe 6 der festen Skala lautet 'laufende Serienproduktion, wiederholte Auslieferung oder gelieferte Skalierung'; P-N50 (Mitteilung 20.04.2026) und C-STR-13 (Naval News) melden den Serienstart bei Blohm+Voss im JV Rheinmetall Kraken GmbH. Der Wortlaut 'laufende Serienproduktion' ist erfüllt; die Skala verlangt keine vorherige Kundenprogramm-Stufe. Die Einordnung ist vertretbar, weil Hersteller-/Medienursprung, fehlende Kunden/Lieferungen und Planzahlen (200 bis 1.000/Jahr) in Statement, Reasoning, uncertainty und next_stage_limit offengelegt sind. Nicht blockierend; die Sichtbarkeit von 'ohne Kundenauftrag' im Produktprofil ist beizubehalten.",
      "fingerprint": "7b52239a9b012d632237023e77f19b3a65f3fc0eb4001e708af811e01da0c722"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-f126",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-N60/P-S05/C-STR-38: Programm Ende Juni 2026 beendet, Unterauftrag Mitte Juli 2026 aufgelöst; keine aktuelle Stufe vergeben, Skala bildet Stornierungen nicht ab - korrekt als 'nicht eindeutig bestimmbar' mit coverage_note.",
      "fingerprint": "c98fd3c84c3cca201f39976093c101a10733a84a0fabf118f64e2950cfc9df06"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-frigpipe",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-N61: F127 vorvertragliche Designstudie, F125-Upgrade ohne Vertragsbeleg -> Stufe 1 (offiziell genannte Programme), zukunftsgerichtete Investorenangabe in uncertainty.",
      "fingerprint": "32452525d7cfdacb7cb02e640eef56624a2e114ef359e3314225606b3f2a64de"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-power",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-C01/P-C02/P-S02: Umsatz 2025 rund 2 Mrd EUR, rund 6.250 Beschäftigte (Stufe 6 für das Seriengeschäft), Verkauf an AEQUITA unterzeichnet, Closing offen, 'discontinued operations' ausgewiesen; Einordnung beschreibt Reife, nicht Konzernzugehörigkeit.",
      "fingerprint": "26113f321557640edc4ea20304423570659c068d26c6be9f3340729dfa36ea6e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-de",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "8c3960409164c072b2db1179d989c3b920824356ad04264ba25967e18ebd5033"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-nl",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "34d6a6c9efdd03c4c0087a47fbc867f305892edf870cf2dc4e7efcb236d55024"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-ch",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "3e98d22c66cd8b70112fa9df1e87d3c842e92058d4f734ac60110cf4f5374bfd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-it",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "1151d48b6f1d894c00fb49e0fcabc1a9c608b420291acc69e1bdca5d637ea372"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-ro",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "3d711e4be90b82882b968912a5edf944c5758a513d18a9eb5340504ca4c2a699"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-sg",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "69b0244b578fcc87673b853900ece5b9756b54e47a96605703af8d90d07fc9e9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-us",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "8bd0469ddbfa1f29a092c29799dda28d4c05e5ae8b81691a6841f1bf826eb7d8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-za",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "6360aa0b2868bba1ab53edff542c2b58b45794c3ff63341511f1d29c6d6e7e83"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-hu",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 je Region gegen regional-presence-v2 geprüft (höchste durch A-Fakten belegte Stufe, mindestens zwei Kernfunktionsgruppen, keine Mehrfachzählung derselben Funktion, Standorte per site_id dedupliziert): DE (Produktion + Service/Werftservice), NL (Entwicklung, Produktion, Wartung Ede, 100 %), CH (Entwicklung + Fertigung Zürich), IT (Rheinmetall Italia Entwicklung + Produktion; LRMV 50:50 at-equity ohne Kontrollbeleg ausgeschlossen), RO (Automecanica 72,5 % Mehrheitstochter: Fertigung + Service; Stufe ausdrücklich nur für Spezialfahrzeuge, SAFE-Ausbau und Mangalia geplant), SG (Service + Engineering; nicht blockierend: Entwicklungsfunktion stützt sich auf die Selbstbeschreibung 'Engineering/AI & Vision', in uncertainty offengelegt, im Basis-Review als Aktivitätszuordnung freigegeben), US (Entwicklung XM30 + Fertigung MK93/Loc, 100 % laut C-STR-24; Hub Vienna nur Büro), ZA (RDM 51 % vollkonsolidiert = beherrschtes JV, Entwicklung + Fertigung, Kontrollbeleg C-STR-22 in depends_on), HU (Rheinmetall Hungary 51 % vollkonsolidiert, Entwicklung + Serienfertigung, Kontrollbeleg C-STR-19). Kundenaufträge werden nirgends als Präsenz gezählt.",
      "fingerprint": "daf1d12e2692c3f92f2f016e96cec92096d5617648319f13707c304d96032858"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-gb",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 4 je Region geprüft: GB (RBSL 55 % vollkonsolidiert = beherrscht, Boxer/Challenger-Fertigung Telford; Geschützwerk nur schrittweise im Anlauf, getrennt als geplant; Entwurf/Betreuung nicht als eigene Funktion gezählt), ES (Expal 100 %: Fertigung; zweite Kernfunktion nicht belegt), BG (Naval Technology Bulgaria: Entwicklung/Engineering; VMZ-JV angekündigt und umstritten, nicht gezählt), UA (JV 51 % vollkonsolidiert, Instandhaltung; Produktion/Entwicklung nur Plan; Kundenlieferung nur customer_activity), CA (Entwicklung autonomer Systeme; Fertigung nicht belegt), AU/NZ (Redbank-Fertigung; NIOA-JV Maryborough ohne Kontrollklassifikation nicht gezählt, Neuseeland nur Büro/Operationen). Funktionszählung und next_stage_limit konsistent.",
      "fingerprint": "84268f30e3c0f5f573a191a21dd594b2673be335b7d27ac69ae46d109b6016b3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-es",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 4 je Region geprüft: GB (RBSL 55 % vollkonsolidiert = beherrscht, Boxer/Challenger-Fertigung Telford; Geschützwerk nur schrittweise im Anlauf, getrennt als geplant; Entwurf/Betreuung nicht als eigene Funktion gezählt), ES (Expal 100 %: Fertigung; zweite Kernfunktion nicht belegt), BG (Naval Technology Bulgaria: Entwicklung/Engineering; VMZ-JV angekündigt und umstritten, nicht gezählt), UA (JV 51 % vollkonsolidiert, Instandhaltung; Produktion/Entwicklung nur Plan; Kundenlieferung nur customer_activity), CA (Entwicklung autonomer Systeme; Fertigung nicht belegt), AU/NZ (Redbank-Fertigung; NIOA-JV Maryborough ohne Kontrollklassifikation nicht gezählt, Neuseeland nur Büro/Operationen). Funktionszählung und next_stage_limit konsistent.",
      "fingerprint": "b61c7e8ff3777e28793a536be3579e586d73051353dd46ae71bf189bb6183bc5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-bg",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 4 je Region geprüft: GB (RBSL 55 % vollkonsolidiert = beherrscht, Boxer/Challenger-Fertigung Telford; Geschützwerk nur schrittweise im Anlauf, getrennt als geplant; Entwurf/Betreuung nicht als eigene Funktion gezählt), ES (Expal 100 %: Fertigung; zweite Kernfunktion nicht belegt), BG (Naval Technology Bulgaria: Entwicklung/Engineering; VMZ-JV angekündigt und umstritten, nicht gezählt), UA (JV 51 % vollkonsolidiert, Instandhaltung; Produktion/Entwicklung nur Plan; Kundenlieferung nur customer_activity), CA (Entwicklung autonomer Systeme; Fertigung nicht belegt), AU/NZ (Redbank-Fertigung; NIOA-JV Maryborough ohne Kontrollklassifikation nicht gezählt, Neuseeland nur Büro/Operationen). Funktionszählung und next_stage_limit konsistent.",
      "fingerprint": "4d3665a9b6f6673601b5d5e544ae0ee28279b761678bf37310b19aa075cf6b6a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-ua",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 4 je Region geprüft: GB (RBSL 55 % vollkonsolidiert = beherrscht, Boxer/Challenger-Fertigung Telford; Geschützwerk nur schrittweise im Anlauf, getrennt als geplant; Entwurf/Betreuung nicht als eigene Funktion gezählt), ES (Expal 100 %: Fertigung; zweite Kernfunktion nicht belegt), BG (Naval Technology Bulgaria: Entwicklung/Engineering; VMZ-JV angekündigt und umstritten, nicht gezählt), UA (JV 51 % vollkonsolidiert, Instandhaltung; Produktion/Entwicklung nur Plan; Kundenlieferung nur customer_activity), CA (Entwicklung autonomer Systeme; Fertigung nicht belegt), AU/NZ (Redbank-Fertigung; NIOA-JV Maryborough ohne Kontrollklassifikation nicht gezählt, Neuseeland nur Büro/Operationen). Funktionszählung und next_stage_limit konsistent.",
      "fingerprint": "af7db36008989a100eabb40e0e77b6d8410bed930945b4150fcf7a2ee2adac97"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-ca",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 4 je Region geprüft: GB (RBSL 55 % vollkonsolidiert = beherrscht, Boxer/Challenger-Fertigung Telford; Geschützwerk nur schrittweise im Anlauf, getrennt als geplant; Entwurf/Betreuung nicht als eigene Funktion gezählt), ES (Expal 100 %: Fertigung; zweite Kernfunktion nicht belegt), BG (Naval Technology Bulgaria: Entwicklung/Engineering; VMZ-JV angekündigt und umstritten, nicht gezählt), UA (JV 51 % vollkonsolidiert, Instandhaltung; Produktion/Entwicklung nur Plan; Kundenlieferung nur customer_activity), CA (Entwicklung autonomer Systeme; Fertigung nicht belegt), AU/NZ (Redbank-Fertigung; NIOA-JV Maryborough ohne Kontrollklassifikation nicht gezählt, Neuseeland nur Büro/Operationen). Funktionszählung und next_stage_limit konsistent.",
      "fingerprint": "dd91c11075d5e92c31674ebefa65ab88becc2b0e81cc2fd4021c4d0b6a3e2321"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-au",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 4 je Region geprüft: GB (RBSL 55 % vollkonsolidiert = beherrscht, Boxer/Challenger-Fertigung Telford; Geschützwerk nur schrittweise im Anlauf, getrennt als geplant; Entwurf/Betreuung nicht als eigene Funktion gezählt), ES (Expal 100 %: Fertigung; zweite Kernfunktion nicht belegt), BG (Naval Technology Bulgaria: Entwicklung/Engineering; VMZ-JV angekündigt und umstritten, nicht gezählt), UA (JV 51 % vollkonsolidiert, Instandhaltung; Produktion/Entwicklung nur Plan; Kundenlieferung nur customer_activity), CA (Entwicklung autonomer Systeme; Fertigung nicht belegt), AU/NZ (Redbank-Fertigung; NIOA-JV Maryborough ohne Kontrollklassifikation nicht gezählt, Neuseeland nur Büro/Operationen). Funktionszählung und next_stage_limit konsistent.",
      "fingerprint": "340d651702bdfd738b7a4c40b2c736b886e3c5b3c8266916d7ac429f049cb0e6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-pl",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 3 (Rheinmetall Polska: Verbindungsbüro Warschau, Unterstützungsstandort Gliwice bei ZMBL als Büro statt eigener Service-Infrastruktur gewertet); Munitionsaufträge zählen nicht als Infrastruktur - konservativ und belegt (P-R96, undatiert).",
      "fingerprint": "aa385b9285c58fcb4b750fd903577a722e03691a04cd893ff3de9b4f4b9f761b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-nordic",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 5 beruht ausschließlich auf Skoppum (eröffnet 01.10.2026, Entwicklung + Produktion, 100 Mitarbeitende zur Eröffnung, P-D50); Schweden nur Büro, Aggregat folgt dem stärksten belegten Land (in shared_limitations und Statement ausgewiesen); junger Standort in uncertainty.",
      "fingerprint": "2cb75f2f72e199293a80e78de5fd68d37845b40929acdd52bb81bbbe1cbaf497"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-naval-intl",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Stufe 2 für Ägypten (NVL Egypt) und Brunei (Muara Maritime Services): operative JV ohne Kontrollbeleg gemäß JV-Regel; Rijeka im Aufbau getrennt als geplant; Aggregat von drei Ländern in uncertainty, Bulgarien bewusst separat.",
      "fingerprint": "db0d5cc3b9983e19e9f07b16823ef1c3c65b89439c4f9b61638c7c12eb9be121"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-lt",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. 'Geplant' ohne operative Stufe korrekt: Litauen (Baisogala im Bau, Spatenstich 04.11.2025, JV-Kontrolle nicht belegt, Inbetriebnahme nicht bestätigt, C-STR-21) und Lettland (nur MoU 25.09.2025, P-R95/C-STR-35); score null, coverage_note mit Beleggrenze, keine operative Stufe aus Kundenbelieferung abgeleitet.",
      "fingerprint": "e1273500b1b3e7e5752e91b3dc7844b611187bbb530f124baaf5210777fdbddd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-lv",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. 'Geplant' ohne operative Stufe korrekt: Litauen (Baisogala im Bau, Spatenstich 04.11.2025, JV-Kontrolle nicht belegt, Inbetriebnahme nicht bestätigt, C-STR-21) und Lettland (nur MoU 25.09.2025, P-R95/C-STR-35); score null, coverage_note mit Beleggrenze, keine operative Stufe aus Kundenbelieferung abgeleitet.",
      "fingerprint": "16c29f2a58cd74de7a5554545de12099db88f67a37e2d028fbd82ed34b779147"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-gulf",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. 'nicht eindeutig bestimmbar' (score null) ist korrekt: P-R160 beschreibt nur strategische Märkte; coverage_note stellt klar, dass dies keine fehlende Aktivität beweist. Offene Grenze (nicht blockierend): Die laut C-STR-18 seit Juli 2026 vollständig gehaltene Rheinmetall Arabia Simulation and Training LLC (Riad) ist der Region im Faktenpaket nicht zugeordnet (RQ-04); die Stufe ist daher bewusst unbestimmt, nicht niedrig.",
      "fingerprint": "c4cb07a612936c89f4c300c6a0239d141a702b842bbe07217e0dd23413ff0d26"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-portfolio-1",
      "evidence_review": "Runde-2: Statement korrigiert (SPOCK 1 im Betrieb; Counter-UAS, Deep Strike, Luftraumsatellit Stufe 1-3), I-PM-sar in depends_on; konsistent mit I-ES-6. Nicht blockierend: Reasoning nennt Stufe 6 bei HX, 155-mm und Mittelkaliber ohne I-PM-trucks/-art155/-medcal in depends_on (inhaltlich stimmig mit diesen geprüften Einordnungen).",
      "fingerprint": "256ae08413295df381eca9982d43b44c1f48d29910669eee17382b0e9dc1df44"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-portfolio-2",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. fact_text/fact_claim_ids (P-A13, P-A11, P-V12) treffen die Quellen; Kapazitätswerte als Plan, Verzugsberichte als Medienangabe mit Rheinmetall-Gegenangabe gekennzeichnet; Insight als Auftrags-/Lieferfähigkeit getrennt formuliert und mit uncertainty begrenzt.",
      "fingerprint": "ecc117d15f993cd5c513bf618a2ac0abbbaeb6728d9ebd716548d57f58f47d6c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-portfolio-3",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. T-09/C-STR-38/P-S05/I-PM-k130 abgeglichen; Vier-Monats-Zeitraum ist im Reasoning ausgewiesen. Nicht blockierend: der Backlog 30.06.2026 (6.255 Mio EUR) enthält laut P-N60 noch die F126 (2,1 Mrd EUR), die Ausbuchung folgte im Juli; fact_text stellt beides nebeneinander, ohne dies zu sagen.",
      "fingerprint": "14cc07efd6c5e7faf69af9e55b7a40b6e3f65a2235eaafd97fde4d89585d40d7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-cluster-1",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. C-STR-06/-07/-08: ARTEC 64 % und PSM 50 % at-equity, RBSL 55 % vollkonsolidiert; 'Kapitalanteil ist nicht gleich Kontrolle' und KNDS-Doppelrolle durch I-M-knds-procurement/Cluster-Fakten gedeckt; Stimmrechtsgrenze in uncertainty.",
      "fingerprint": "0eae2289e317cbde407065fc224b435703d6a97e5beb92f9562062f1be46e2ff"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-cluster-2",
      "evidence_review": "Runde-2: Staatsstatus nur für Ungarn und UDI (laut GB 2024) behauptet, EPSO-G/Romarm-Tochter/Denel ausdrücklich ohne belegten Staatsstatus; 'reversibel' ersetzt durch 'Gründungsstatus umstritten' (C-STR-33).",
      "fingerprint": "059af7fdb4562a07240a86cf2b26ec516897b0169ff9f9a77d7377eaaaf97a1c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-cluster-3",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. C-TEC-01/-02/-03/-04/-05/-06: Statusklassen MoU/angekündigt/angelaufen unverändert übernommen (Weeze angelaufen, ICEYE betreibt SAR-Satelliten laut Rheinmetall); Insight 'Umsetzung offener Prüfpunkt' ist keine Schwächenaussage; Partnerquellen nicht geöffnet in uncertainty.",
      "fingerprint": "361d3f140f0db4aceecf12a0da514a26b8300024d4d5382eb41a922e52a3dbff"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-market-1",
      "evidence_review": "Runde-2: 'abgesichert' entfernt; Statement gibt CEO-Engpass wieder und nennt Aschau-Eigenfertigung (M-RHM-04, I-M-rheinmetall-integration); Matrixverweis korrekt.",
      "fingerprint": "02d4d65407fe36b70b89248a19b5431fc871891a7a8eca16a0cf8f8cfa3cf68b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-market-2",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. P-W13, M-NAM-05, M-MKT-03/-04 und die Zellen I-M-*-capacity abgeglichen: nur Rheinmetall und Nammo haben planbedingungskonforme Zielwerte, BAE/GD-OTS/Hanwha ohne Geschosswert, KNDS ohne Zieljahr; EU-Zahlen (Kubilius >2 Mio vs. RFE/RL ~550-600 Tsd.) mit abweichenden Zeitpunkten/Zählweisen gekennzeichnet; keine Ist-Vergleichsbehauptung.",
      "fingerprint": "7f285c2f31288148a8314dcd4e1136babb40cc76d85af2f1dcebdd73941c04fc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-market-3",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Matrixverweise stimmen (Beschaffung 4/4: Rheinmetall, KNDS; Werksnetz 4/4: Rheinmetall, KNDS, Nammo); 'kein Gesamtvorsprung' erhalten. Nicht blockierend: fact_text nennt 'Fertigung in DE, ES, ZA', wofür keine fact_claim_ids (P-W10/P-R40/P-R140) geführt sind; die Deckung liegt in I-M-rheinmetall-industrial.",
      "fingerprint": "5d3206d2bf0b8c84cb7878fae20d22b0f632f6300c75985c0967c1ef74f4ad9a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-STR-1",
      "evidence_review": "Runde-2: Ableitung aus I-PM-boxer/-puma/-lynx/-propellant, C-MKT-01 und korrigiertem I-MI-portfolio-1 tragfähig, intern. Nicht blockierend: Reasoning nennt HX, 155-mm, Mittelkaliber (Stufe 6) ohne I-PM-trucks/-art155/-medcal in depends_on.",
      "fingerprint": "4821e5a1dc8197d6f86a4b3b0812a3b5804a1d34e665a5b2a9cec8d057607381"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-STR-2",
      "evidence_review": "Runde-2: Rahmenvertrag als Obergrenze ohne Abrufgarantie, 'keine gesicherte Nachfrage', Abrufe in uncertainty nicht belegt; Matrixbezug und Nicht-Exklusivität korrekt (P-W11).",
      "fingerprint": "405e1cb56e84da868893240f656614c3933836382423ff2cc0a2663fb78f39bc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-STR-3",
      "evidence_review": "Runde-2: Staatspartner nur für Ungarn und Ukraine (UDI laut GB 2024), Denel ausdrücklich nicht belegt; Zugangswirkung als Interpretation gekennzeichnet; Quoten/Funktionen korrekt (C-STR-19/-20/-22).",
      "fingerprint": "3cec1360bbec071e8532b9ef4361aa565cfbd40eeff91ad1afba7ff2748ddaa0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-WKN-1",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. T-13/T-14: operativer FCF -1.616 Mio EUR H1 2026 (Vj. -631), Umsatz +39 %; Herstellerbegründung (verschobene Anzahlungen, Vorratsaufbau, Investitionen) im Reasoning sinngemäß wiedergegeben, Halbjahreswert und Q3-Termin in uncertainty. Interne finanzielle Grenze, keine Datenlücke.",
      "fingerprint": "2ec3a72c2643dfe115a925ed6733162937cdc8a2c7683ecda7ac943558080b2f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-WKN-2",
      "evidence_review": "Runde-2: M-RHM-07 und C-STR-21 in depends_on; 'Kapazitätsziel nicht erreicht' gestrichen; Aussage auf zwei Einzelfälle begrenzt, 'keine konzernweite Lieferschwäche', Medien-/Streitstatus in uncertainty.",
      "fingerprint": "8ef1aa2186d89519d0edebf97ee1b0e01344f34665db969de50880df6aa95a97"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-WKN-3",
      "evidence_review": "Auflage umgesetzt: keine Quote im Text, uncertainty nennt nicht abgeglichenen Umsatzbezug des Konzernanhangs und unbenannten Kunden; 'kann merklich bewegen'. Verhältnisbildung zulässig; keine abgeleitete Prozentzahl rendern.",
      "fingerprint": "8ec05d8e9bcce2a60dd8b46c7994a320a4b7d2d3759b7bc3ba2a39ce586e5053"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-OPP-1",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Extern, belegt: ASAP >500 Mio EUR (M-MKT-01), EDIP 1,5 Mrd EUR (M-MKT-06), Rumänien SAFE 5,7 Mrd EUR (C-MKT-06, Herstellerangabe), P-W11/T-14 als Ausgangsposition; Reasoning und uncertainty sagen ausdrücklich, dass Förderentscheidungen kein Auftrag an Rheinmetall sind.",
      "fingerprint": "b2ddbafb2595472b2cd10ceb15a4d58b92b901a1cabf8a0798e599ca16f0a261"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-OPP-2",
      "evidence_review": "Runde-2: Reifeaussage korrigiert (SAR Stufe 5, FV-014 Stufe 4 von 6; I-PM-sar in depends_on); Betrieb FV-014 als nicht belegt.",
      "fingerprint": "d1c5fee6f9181ee9ead36519dc250e46fe58ebe9bb1126fd27781cf038148388"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-OPP-3",
      "evidence_review": "Runde-2: Victoria als Pulver-/Treibladungskapazität (Beginn 2028, M-RHM-04), Unterlüß/Várpalota als angekündigte Sprengstoffwerke; Engpassbeleg durch Förderung + CEO-Aussage; kein Gesamtvorsprung.",
      "fingerprint": "dfc8a9df77b98524b5a1885794e5b6b6cdfdc121750ffc117f0e9b2ab5daca3f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-THR-1",
      "evidence_review": "Runde-2: Abhängigkeit I-MI-cluster-2 (korrigiert) neu geprüft; F126/Bulgarien mit Parteiensicht belegt. Nicht blockierend: 'umkehren ... zeigen' für das umstrittene Bulgarien-JV stark; Wortlaut bei Gelegenheit angleichen.",
      "fingerprint": "d984de382b8352f858d1ccf9c07b52a6dc5155540fbfbccd64812a7f79cbf958"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-THR-2",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. Extern, belegt: KNDS-Linie Belgien 11/2025 (M-KND-08 über I-M-knds-industrial), Nammo Raufoss seit 12/2024; Bezug zu Matrix (Höchststufe geteilt) und Marktkapazitätsunsicherheit korrekt, keine Marktanteilsableitung. Ableitung nicht von der Matrix überdehnt (kein Gesamtvorsprung/Ranking).",
      "fingerprint": "9b258a7002fa1e7081a87e57756cddaa228e9efe6baa2cccff3c2a0190ce9a8e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-THR-3",
      "evidence_review": "Runde 2: Fingerprint gegenüber Runde 1 unverändert, Runde-1-Befund übernommen. C-STR-07/-08 über I-MI-cluster-1: PSM 50 %, ARTEC 64 %, beide at-equity; KNDS zugleich Wettbewerber (Matrix). Als externes Partner-/Wettbewerberrisiko vertretbar eingeordnet; nicht blockierend: 'Das begrenzt Rheinmetalls Spielraum' ist laut uncertainty nicht belegt und sollte als Möglichkeit formuliert werden.",
      "fingerprint": "eb4873b60fc398846a136c521357611effca66f8eb2959db477581f6a1873ca7"
    }
  ],
  "missing_decisions": [],
  "fact_review": {
    "C-MKT-01": {
      "id": "C-MKT-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-02": {
      "id": "C-MKT-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-03": {
      "id": "C-MKT-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-04": {
      "id": "C-MKT-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-05": {
      "id": "C-MKT-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-06": {
      "id": "C-MKT-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-08": {
      "id": "C-MKT-08",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-12": {
      "id": "C-MKT-12",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-MKT-13": {
      "id": "C-MKT-13",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-06": {
      "id": "C-STR-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-07": {
      "id": "C-STR-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-08": {
      "id": "C-STR-08",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-09": {
      "id": "C-STR-09",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-11": {
      "id": "C-STR-11",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-13": {
      "id": "C-STR-13",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-14": {
      "id": "C-STR-14",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-19": {
      "id": "C-STR-19",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-20": {
      "id": "C-STR-20",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-21": {
      "id": "C-STR-21",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-22": {
      "id": "C-STR-22",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-23": {
      "id": "C-STR-23",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-24": {
      "id": "C-STR-24",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-25": {
      "id": "C-STR-25",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-27": {
      "id": "C-STR-27",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-33": {
      "id": "C-STR-33",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-34": {
      "id": "C-STR-34",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-35": {
      "id": "C-STR-35",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-36": {
      "id": "C-STR-36",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-37": {
      "id": "C-STR-37",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-STR-38": {
      "id": "C-STR-38",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-TEC-01": {
      "id": "C-TEC-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-TEC-02": {
      "id": "C-TEC-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-TEC-03": {
      "id": "C-TEC-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-TEC-04": {
      "id": "C-TEC-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-TEC-05": {
      "id": "C-TEC-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-TEC-06": {
      "id": "C-TEC-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-BAE-01": {
      "id": "M-BAE-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-BAE-02": {
      "id": "M-BAE-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-BAE-03": {
      "id": "M-BAE-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-BAE-04": {
      "id": "M-BAE-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-BAE-05": {
      "id": "M-BAE-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-BAE-06": {
      "id": "M-BAE-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-GDO-01": {
      "id": "M-GDO-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-GDO-02": {
      "id": "M-GDO-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-GDO-03": {
      "id": "M-GDO-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-GDO-04": {
      "id": "M-GDO-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-GDO-05": {
      "id": "M-GDO-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-GDO-06": {
      "id": "M-GDO-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-HAN-01": {
      "id": "M-HAN-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-HAN-02": {
      "id": "M-HAN-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-HAN-03": {
      "id": "M-HAN-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-HAN-04": {
      "id": "M-HAN-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-HAN-05": {
      "id": "M-HAN-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-HAN-06": {
      "id": "M-HAN-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-HAN-07": {
      "id": "M-HAN-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-01": {
      "id": "M-KND-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-02": {
      "id": "M-KND-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-03": {
      "id": "M-KND-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-04": {
      "id": "M-KND-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-05": {
      "id": "M-KND-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-06": {
      "id": "M-KND-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-07": {
      "id": "M-KND-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-08": {
      "id": "M-KND-08",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-KND-09": {
      "id": "M-KND-09",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-01": {
      "id": "M-MKT-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-03": {
      "id": "M-MKT-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-04": {
      "id": "M-MKT-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-06": {
      "id": "M-MKT-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-01": {
      "id": "M-NAM-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-02": {
      "id": "M-NAM-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-03": {
      "id": "M-NAM-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-04": {
      "id": "M-NAM-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-05": {
      "id": "M-NAM-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-06": {
      "id": "M-NAM-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-07": {
      "id": "M-NAM-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NAM-08": {
      "id": "M-NAM-08",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-RHM-01": {
      "id": "M-RHM-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-RHM-02": {
      "id": "M-RHM-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-RHM-03": {
      "id": "M-RHM-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-RHM-04": {
      "id": "M-RHM-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-RHM-05": {
      "id": "M-RHM-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-RHM-06": {
      "id": "M-RHM-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-RHM-07": {
      "id": "M-RHM-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A01": {
      "id": "P-A01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A02": {
      "id": "P-A02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A10": {
      "id": "P-A10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A11": {
      "id": "P-A11",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A12": {
      "id": "P-A12",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A13": {
      "id": "P-A13",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A14": {
      "id": "P-A14",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A30": {
      "id": "P-A30",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A40": {
      "id": "P-A40",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-A50": {
      "id": "P-A50",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-C01": {
      "id": "P-C01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-C02": {
      "id": "P-C02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-C03": {
      "id": "P-C03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D01": {
      "id": "P-D01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D02": {
      "id": "P-D02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D10": {
      "id": "P-D10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D11": {
      "id": "P-D11",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D12": {
      "id": "P-D12",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D13": {
      "id": "P-D13",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D14": {
      "id": "P-D14",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D20": {
      "id": "P-D20",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D30": {
      "id": "P-D30",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D31": {
      "id": "P-D31",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D40": {
      "id": "P-D40",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D50": {
      "id": "P-D50",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-D60": {
      "id": "P-D60",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N01": {
      "id": "P-N01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N03": {
      "id": "P-N03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N10": {
      "id": "P-N10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N20": {
      "id": "P-N20",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N30": {
      "id": "P-N30",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N31": {
      "id": "P-N31",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N40": {
      "id": "P-N40",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N50": {
      "id": "P-N50",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N60": {
      "id": "P-N60",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-N61": {
      "id": "P-N61",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R01": {
      "id": "P-R01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R02": {
      "id": "P-R02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R10": {
      "id": "P-R10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R100": {
      "id": "P-R100",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R110": {
      "id": "P-R110",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R120": {
      "id": "P-R120",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R130": {
      "id": "P-R130",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R140": {
      "id": "P-R140",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R150": {
      "id": "P-R150",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R160": {
      "id": "P-R160",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R20": {
      "id": "P-R20",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R30": {
      "id": "P-R30",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R40": {
      "id": "P-R40",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R50": {
      "id": "P-R50",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R60": {
      "id": "P-R60",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R61": {
      "id": "P-R61",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R70": {
      "id": "P-R70",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R72": {
      "id": "P-R72",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R80": {
      "id": "P-R80",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R90": {
      "id": "P-R90",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R95": {
      "id": "P-R95",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R96": {
      "id": "P-R96",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R97": {
      "id": "P-R97",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-R98": {
      "id": "P-R98",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-S02": {
      "id": "P-S02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-S05": {
      "id": "P-S05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V10": {
      "id": "P-V10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V11": {
      "id": "P-V11",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V12": {
      "id": "P-V12",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V13": {
      "id": "P-V13",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V14": {
      "id": "P-V14",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V15": {
      "id": "P-V15",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V16": {
      "id": "P-V16",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V17": {
      "id": "P-V17",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V20": {
      "id": "P-V20",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V21": {
      "id": "P-V21",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V30": {
      "id": "P-V30",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V31": {
      "id": "P-V31",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V32": {
      "id": "P-V32",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V34": {
      "id": "P-V34",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V35": {
      "id": "P-V35",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V40": {
      "id": "P-V40",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V41": {
      "id": "P-V41",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V50": {
      "id": "P-V50",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V51": {
      "id": "P-V51",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V52": {
      "id": "P-V52",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V60": {
      "id": "P-V60",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V70": {
      "id": "P-V70",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V71": {
      "id": "P-V71",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-V72": {
      "id": "P-V72",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W02": {
      "id": "P-W02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W10": {
      "id": "P-W10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W11": {
      "id": "P-W11",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W12": {
      "id": "P-W12",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W13": {
      "id": "P-W13",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W20": {
      "id": "P-W20",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W21": {
      "id": "P-W21",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W30": {
      "id": "P-W30",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W31": {
      "id": "P-W31",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W33": {
      "id": "P-W33",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W40": {
      "id": "P-W40",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W41": {
      "id": "P-W41",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W50": {
      "id": "P-W50",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W51": {
      "id": "P-W51",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-W60": {
      "id": "P-W60",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-04": {
      "id": "T-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-06": {
      "id": "T-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-07": {
      "id": "T-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-09": {
      "id": "T-09",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-10": {
      "id": "T-10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-13": {
      "id": "T-13",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-14": {
      "id": "T-14",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-16": {
      "id": "T-16",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-18": {
      "id": "T-18",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-E01": {
      "id": "T-E01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-E04": {
      "id": "T-E04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-E10": {
      "id": "T-E10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-E11": {
      "id": "T-E11",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-E17": {
      "id": "T-E17",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-E22": {
      "id": "T-E22",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-E30": {
      "id": "T-E30",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    }
  }
}
```
