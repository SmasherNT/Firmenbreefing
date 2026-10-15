# Review

```json
{
  "schema_version": 1,
  "run_id": "20261013-rheinmetall-flugabwehr",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-13",
  "phase": "final",
  "status": "freigegeben",
  "review_work_fingerprint": "81896b15ee8d34cf8349dae32063ab1e28707493e25aa5554105cffa24daac64",
  "material_errors": [],
  "review_scope": {
    "summary": "Runde 2: Alle 136 Ableitungen ausdrücklich entschieden. 13 geänderte I-/S-Claims vollständig neu geprüft, S-WE-03 gestrichen (Weaknesses jetzt 2 Punkte, zulässig). Die übrigen 123 per Feldvergleich mit positioning-r1/swot-r1 als inhaltlich unverändert bestätigt und mit dem r1-Ableitungsbefund übernommen. Alle Korrekturen und material_errors aus r1 sind behoben. 147 Fakten explizit aus Basis-Review r3 (freigegeben) übernommen; keine Neuprüfung von Fakten, keine Webabrufe.",
    "nonblocking_notes": [
      "I-ES-05/S-WE-01: Die Formulierung „eigene SkyKnight-Lenkwaffe“ wäre als „im Rheinmetall-Katalog angebotene SkyKnight-Lenkwaffe (Herkunft nicht belegt)“ präziser.",
      "I-TAD-01: allgemeines „Flugkörper von Partnern“ optional auf Skyranger-Konfigurationen eingrenzen (Konsistenz mit I-ES-05).",
      "A-NORD-WA (Fakten, portfolio): country „Schweden“ für eine Mehrländeraktivität ist kosmetisch."
    ],
    "open_limits": "Strittiger Skyranger-Verzug und nicht belegter Bundeswehr-Großauftrag sind durchgängig als strittig bzw. als Beleggrenze dargestellt; Ukraine-Einsatzwirkung bleibt Herstellerangabe mit Gegenrecherche."
  },
  "source_checks": [],
  "claims": [
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-02",
      "evidence_review": "Begründung jetzt vollständig: Skynex 5, Skyranger 35 (laut Hersteller), Pilica+ und IRIS-T SLS je 4 vor Skyranger 30 (3); deckt sich mit den Matrixzellen in depends_on.",
      "fingerprint": "b52125b4c93a053179d8d8af4fe1e8e7a8dbcdfb6580c7caca1965f21c306fc2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-05",
      "evidence_review": "r1-Korrektur umgesetzt: auf belegte Skyranger-Konfigurationen begrenzt, SkyKnight-Beleggrenze (P-SKN-01) genannt, Lockheed-Kooperation als Raketen/ATACMS ohne SHORAD-Bezug. Hinweis: „eigene SkyKnight-Lenkwaffe“ heißt hier „im Rheinmetall-Katalog“; die Herkunft bleibt laut P-SKN-01 offen (nicht blockierend).",
      "fingerprint": "4e2dfbd1e1789bd62eed020270c9514974e85b07cac26ee7fbde7dc02f3c114f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TAD-02",
      "evidence_review": "r1-Korrektur umgesetzt: Kapazität als Herstellerziel, Neuss als Fachmedium-Angabe; Verzugsursachen Rheinmetall (via S&V/dpa) zugeschrieben, BAAINBw-Kritik via Capital/dpa-AFX und S&V-Engpässe (M-DE-SKR-02) getrennt; als strittig gekennzeichnet.",
      "fingerprint": "8c0e876bc33f8e5982271bc933958b81066c68c98470a4819d04d797dd695ec7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TEU-04",
      "evidence_review": "r1-Korrektur umgesetzt: als Kundenforderung nur die dänischen Offsets, Polen als Konsortialmodell, NL/RO als Herstellerangabe; keine Kausalbehauptung.",
      "fingerprint": "83e64a934c30512be7ceadd23e1c0da3c741762787261f3a27dbb0f320dfa4b4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skynex",
      "evidence_review": "Italien-Übergabe im statement jetzt als Herstellerangabe gekennzeichnet; Stufe 6 unverändert tragfähig.",
      "fingerprint": "41b97699307bcda42109608d4024c3a6c6e43c85f0f92cdf26e6dbaeec00be34"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-nnbs",
      "evidence_review": "r1-Korrektur umgesetzt: Änderungsvertrag nur parlamentarisch gebilligt, Unterzeichnung nicht belegt; Stufe 4 durch Entwicklungsvertrag 2024 getragen.",
      "fingerprint": "d486988ca16804262289337d06bd635c902a6f370851413df01048d83d4c5ef6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-CLU-01",
      "evidence_review": "r1-Korrektur umgesetzt: Stinger nur ursprünglich vorgesehen, jetzt DefendAir (ab 2029 laut S&V); P-SKR-03 in fact_claim_ids/depends_on; Insight korrekt zugeschrieben.",
      "fingerprint": "8bb1183d630a7eb53eff1801978f7fba0059b9f7218655b2beb292a339109794"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-MKT-01",
      "evidence_review": "Lieferstand-Vergleich jetzt vollständig und durch die zusätzlich referenzierten Matrixzellen gedeckt; Vorsprung ausdrücklich auf ein Kriterium begrenzt.",
      "fingerprint": "30174bbc3f18e5236e118265fa26e2c8c3eddea02de31f0d9b53ee4a40706f9c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-MKT-02",
      "evidence_review": "r1-Korrektur umgesetzt: DK-Pflicht, PL-Konsortium und NL/RO-Herstellerangabe getrennt; kein Kausalzusammenhang.",
      "fingerprint": "5cda25a4356aa0571a32a65220599729b2b92391138f454f0e1e6d56ae83c9c3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-NORD",
      "evidence_review": "Nach Basis-Review r3 (A-NO-SKO-DEV, gleiche site_id) erfüllen eigene Produktion und Entwicklung am selben Standort Skoppum Stufe 5 nach regional-presence-v1; Kundenaktivitäten heben die Stufe korrekt nicht an; Unsicherheit nennt Herstellerangabe und Elektrooptik-Schwerpunkt.",
      "fingerprint": "92c2265c79500801acdeedb14ae944582cd101d2debfe7ecac9c659a4a7b8691"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-WE-01",
      "evidence_review": "r1-Korrektur umgesetzt: Schwäche auf belegte Skyranger-Konfigurationen begrenzt, SkyKnight-Beleggrenze und Lockheed-Abgrenzung genannt; die Wirkung auf Zeitpläne ist korrekt Rheinmetall zugeschrieben (P-SKR-03); interne Einordnung vertretbar.",
      "fingerprint": "0f748350d67a192c6e299e3e54ac86e732e6853df1dbabb924bcd1c419b234fa"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-OP-03",
      "evidence_review": "r1-Korrektur umgesetzt: nur Billigung des Änderungsvertrags belegt; Arminius als Unternehmenserwartung ohne Produktzuordnung; externe Chance mit offenem Zeitpunkt.",
      "fingerprint": "47bb24e20d3daf56242abee6a80274d4cf9a93f9a5ba8427ef337df429004dd0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-TH-02",
      "evidence_review": "r1-Korrektur umgesetzt: externe Bedrohung auf belegte Beschaffungsfakten (DK-Offsets, PL-Konsortium) gestützt; NL/RO als Herstellerangabe abgegrenzt; Margenwirkung als unbelegt gekennzeichnet.",
      "fingerprint": "4e34edc97cca4e1b8d28e4152d8d5fe23394f3e82deb3825337242a7b9eb9d39"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TAD-01",
      "evidence_review": "Gegenüber r1 unverändert, gegen depends_on erneut geprüft. „Flugkörper von Partnern“ ist für die belegten Skyranger-Konfigurationen korrekt; Laser/C-PGM als Forschung bzw. Entwicklung gekennzeichnet. Für volle Konsistenz mit I-ES-05 wäre „für Skyranger belegte Flugkörper von Partnern; SkyKnight ohne Lieferbeleg“ präziser (optional, nicht blockierend).",
      "fingerprint": "1d1227a86835a34149aa43da202ccb03432249d947a2764360a825f0519c46d8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-EH-01",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Highlights direkt auf A-Fakten; Wert, Einheit, Bezugsobjekt (Segment/Produkt), Zeitraum und Ziel-/Medienkennzeichnung korrekt (Backlog 30.06.2026; 93 Systeme laut S&V Jan. 2026; 400 p. a. als Herstellerziel).",
      "fingerprint": "9fa622ff4d06632b7df11463a225ccd4a81811f9e48c6aa1827aa46b5526e249"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-EH-02",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Highlights direkt auf A-Fakten; Wert, Einheit, Bezugsobjekt (Segment/Produkt), Zeitraum und Ziel-/Medienkennzeichnung korrekt (Backlog 30.06.2026; 93 Systeme laut S&V Jan. 2026; 400 p. a. als Herstellerziel).",
      "fingerprint": "a25cb3a16d594f0d6520c01440da80b547cab3a426e896dc1589b755f9a77a8f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-EH-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Highlights direkt auf A-Fakten; Wert, Einheit, Bezugsobjekt (Segment/Produkt), Zeitraum und Ziel-/Medienkennzeichnung korrekt (Backlog 30.06.2026; 93 Systeme laut S&V Jan. 2026; 400 p. a. als Herstellerziel).",
      "fingerprint": "1823c6d6dad1ed2d3456d59f6a45b7cffdde4e9f9099bef0bf33c087bb654756"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-01",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Kernaussagen gegen depends_on geprüft; Zahlen/Einheiten/Zeitraum (H1 2026, Stichtag), Zuschreibung (Hersteller/Medien/BAAINBw) und strittige Punkte (Verzug, nicht belegter Großauftrag) korrekt; headline/preview ohne neue Aussagen.",
      "fingerprint": "dc27268091368b911abb2211f5a1f019f9b8a52dfaf1aea6760e4705a652a6db"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Kernaussagen gegen depends_on geprüft; Zahlen/Einheiten/Zeitraum (H1 2026, Stichtag), Zuschreibung (Hersteller/Medien/BAAINBw) und strittige Punkte (Verzug, nicht belegter Großauftrag) korrekt; headline/preview ohne neue Aussagen.",
      "fingerprint": "13652da66a35e3a8278af416078249214cd2f50ca422fbb457d607a3912edb53"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-04",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Kernaussagen gegen depends_on geprüft; Zahlen/Einheiten/Zeitraum (H1 2026, Stichtag), Zuschreibung (Hersteller/Medien/BAAINBw) und strittige Punkte (Verzug, nicht belegter Großauftrag) korrekt; headline/preview ohne neue Aussagen.",
      "fingerprint": "918a11359a41460506a39a93df266d333d6111c91ed01a69029ece068ea68741"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-ES-06",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Kernaussagen gegen depends_on geprüft; Zahlen/Einheiten/Zeitraum (H1 2026, Stichtag), Zuschreibung (Hersteller/Medien/BAAINBw) und strittige Punkte (Verzug, nicht belegter Großauftrag) korrekt; headline/preview ohne neue Aussagen.",
      "fingerprint": "00183372ef369e200a1add0e6eebd7bde74b8316c3a2d46c35a6911c1c692bb0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-CLU-02",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Modul-Keyfact gegen fact_claim_ids und depends_on geprüft; Faktverdichtung ohne neue Aussage, Insight als Interpretation erkennbar, Modulzuordnung und Reihenfolge korrekt.",
      "fingerprint": "03f627980caa25180fb1b8ee55957130885dfc9003caf739dda2e5adbab6ab9a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-CLU-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Modul-Keyfact gegen fact_claim_ids und depends_on geprüft; Faktverdichtung ohne neue Aussage, Insight als Interpretation erkennbar, Modulzuordnung und Reihenfolge korrekt.",
      "fingerprint": "d60005ec5a93a54903b0d78bf6ac57086221813cd50ad2cff5863a0bde2cba23"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-MKT-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Modul-Keyfact gegen fact_claim_ids und depends_on geprüft; Faktverdichtung ohne neue Aussage, Insight als Interpretation erkennbar, Modulzuordnung und Reihenfolge korrekt.",
      "fingerprint": "ffe868b3c9e46925af135bd187c31642169c64a10444296241e2b81748dbd61b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-POR-01",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Modul-Keyfact gegen fact_claim_ids und depends_on geprüft; Faktverdichtung ohne neue Aussage, Insight als Interpretation erkennbar, Modulzuordnung und Reihenfolge korrekt.",
      "fingerprint": "87f007b30e8039814b4509c587144250ace88f3aa0897ac49434c4ee5b7a1f90"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-POR-02",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Modul-Keyfact gegen fact_claim_ids und depends_on geprüft; Faktverdichtung ohne neue Aussage, Insight als Interpretation erkennbar, Modulzuordnung und Reihenfolge korrekt.",
      "fingerprint": "02fa4c3782ef8c2a48178c5e83c24ec783ac534d2a69df8aec0add58791e78a8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MI-POR-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Modul-Keyfact gegen fact_claim_ids und depends_on geprüft; Faktverdichtung ohne neue Aussage, Insight als Interpretation erkennbar, Modulzuordnung und Reihenfolge korrekt.",
      "fingerprint": "de0d7f6e4e1c0651306d079293347b03986b9bcdf2bdedf8cc2893d485221601"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-bae_tridon-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "511dc1ca7848a281ac8a51dace47a465d1c101325a2b13d9df0ccf483615ca48"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-bae_tridon-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "bd33313f8c6f79736603b47a938ecea35e0a763b3a37ea51b5deb4b0933b3cca"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-bae_tridon-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "2fccfd934e938a419cd2c29720a8cfa98791311515bd7ca2f6759d5aa4c75526"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-bae_tridon-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "681be343989437cac32e84058e98134d9bed8301fec3d9f910ee6f4fd5523f68"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-bae_tridon-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "0f009458dae2ebc9c760f491c43b5da0aff90bce488c6ce7f6d285c56768a77e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-bae_tridon-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "79e2a37689aa55c24b08fd3e5c7b551fd2669708baf62bd5b3682856e9231036"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-diehl_irist_sls-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "10938b7fb346d7450a0bf635dfb2b7f37ef43d5ce17c1afffbe5e33f6cf1eeab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-diehl_irist_sls-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "913860dd0e27f41c62d7e396cddb52d3c8c71dfe7c5bddc1d6aff83106ed022c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-diehl_irist_sls-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "4c95cf0808e372c48fe36a52c08bb5f2e3791beb0f60e751852c2e8a3989b190"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-diehl_irist_sls-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "9dda0ea45fac816c86e034bdb574c4e273e065c1fd35abb5989972df981651e4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-diehl_irist_sls-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "45c097e6b5eaf3d19d2c52f5219126555b8944765d7a03ffe3e6389d5b42e705"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-diehl_irist_sls-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "42fb0704f820eb0a6d899ec47bca04f2be63f9001c110c650943bd4ad1c0b4a1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-mbda_vlmica-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "c6ae3982078a829a3f3ac4f0d63fcafd1dd5349536cf8584bdaae5068f22f8ab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-mbda_vlmica-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "e5209d435b602a6f3010544d59fdf5ec76ebf3457735caa1e262336e500b33d9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-mbda_vlmica-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "3fa3f953d8adc1f5013628738eb37202262d785175ecb78519bff0ff48127835"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-mbda_vlmica-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "26b4b75b9ec1bb09e89c9d3b80611c3d4a433e542de6e3ae3b95465ba929ccfc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-mbda_vlmica-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "0fd962e56b71ac0b0ddc1f34f66eff5b48df02d95bb035cda4e77f9e0eedbbe2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-mbda_vlmica-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "a75c98f38c5ae4fe29bfc5cd4a4615910f4fdc493f2afa342380eb83ff456e0b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-pgz_pilica-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "cdfb84166a3deeb5b58767e28925eac18965226787c0655dac03d84d7b71ea49"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-pgz_pilica-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "b8ab8d2ea92e87d868d127137cf7796685eb2d2095623f5683bebc6688478260"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-pgz_pilica-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "3790f03d6f40993eaea31994f71debfaf641eaafafaf2ddcd43301ab64c3bdb7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-pgz_pilica-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "0b06f95cef1f1fa216d85e69dfe9a156e1d676613de348f6c294c8bb7279536b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-pgz_pilica-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "1b639c99b200374295a0cb013fcc028975160af47772fa96b72331ecacf93338"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-pgz_pilica-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "301e6b5e59c342f882aa978fa3e520220ecb25abad06f1bafacf1de5ad4d4730"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skynex-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "1fe7359ebf021c303c143b0974a6c08ed4a2110493b4677e3d1538c49225a607"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skynex-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "685a58648e1bf913725c6b7ac5218eca815bab283606a986627b46406fa27e0b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skynex-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "73999b3bdcbd4600661fe79bb5fa2418cc48c70a139e0527805d63bdc8e87bc4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skynex-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "c572f65fae33cca95d3f94e6e23556763a4a69c038288a659d9d56e781501237"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skynex-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "a5a7789cbdb651eb5a44a8c23f5860e67b120afc3a79dd4d0080cb2b223640d3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skynex-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "367e84a0d1912af6b1ebb50a5b6159b62a645f20ae3ae5e598fc0f202e345b2b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger30-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "c1193f428d1b8bc190bf322480b7c9710baedecd1a40ee17232dd93327d8461f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger30-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "13b7ac814ce94bf474f272cdb1e7dd751d5b3d3e220898af57c436bdb1e4693d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger30-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "7d17201f71b676a9ff4e977298f37f972ab22d2db79701a937f51d88d6784e79"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger30-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "79a6eb376fdc3ce56e25e2d8f40e5d2c4e770158cadb3f1b8851eb68429a1085"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger30-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "75292406b76174dcbb939be0c0fba63286746e5b5bddc219386f83b3a031a09e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger30-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "3a119af17845c69253fa87b27c705cd166aac8ea574f3910eb6f2e47dc0529e7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger35-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "c23354ac92bcb8a97d1d64de39e8cce26a497c64a72c91e089b3d1b1b5279707"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger35-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "5f3c6ba1985ab05f664f8fbd21d71ebe864391885ed1b43fd64f58825bcac499"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger35-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "c74cf713a9c9a4aa8bc992f4aaee728dea789ef111381c1850efc3aa43cc5341"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger35-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "9c25cc09fa308bce3a6a5cbdc5bd5a4eeb92c14f42022e7fb5912491413f5c90"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger35-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "c6d81036ff1b6c34fc052142cf3298ef0c504dbcc75b1af0f6d04cfc26bda740"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-rhm_skyranger35-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "59f27def0ac1079e82bec1eb3eb174d155a880e7784557a3c1a479b6f77a21d7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-saab_rbs70_mshorad-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "d35c49028a70399a5e039602110f8ed586a5f1c91bbadc2c6979c93e7301ba1a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-saab_rbs70_mshorad-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "8a3cf3aa0de474f8903340547681b7a29c82d25c1aa9f0030bb1338a3d8680a4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-saab_rbs70_mshorad-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "a2526000f22eb5d7c2954b2d85a4abb1159748a4f7b7a0ca0c6df9b88f694e5b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-saab_rbs70_mshorad-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "1f56cf573d886354d0bbe8e69f9584046a77e949d1dd54614dd7ba937ac1aaee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-saab_rbs70_mshorad-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "0e8784c6a8e48cd89bddf370d3ebe54659c7ebda0076f35fd998311628bd6a4d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-saab_rbs70_mshorad-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "5ad3ee3367a033a8b099a0148a3da0862f6fc5b748f4df188585658107c5a44e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-thales_forceshield-architecture",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "539aac123d816dd5d12b0a1d1e868f93a29db8ad4cbe11a39262725de5ff4cfd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-thales_forceshield-eu_customers",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "4bbd55566dc6da71b33a1a85d4df22cc643ceca068a51376fd06fb72d90659db"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-thales_forceshield-integration",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "18251643ef6840111bd2432df07898f7d4aeee7c7831863a3be741b262bade94"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-thales_forceshield-local_industry",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "5bd20b59d3294cedf47079e75f9f651bad81140124c4942528e39a2346199825"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-thales_forceshield-procurement_status",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "7bcea40e0c6c9a410677dd9f675edb2eaa2dfe4fbe2476c2f93a6ec88908523d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-MX-thales_forceshield-production",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Matrixzelle gegen Planankers (comparison-plan v1) und depends_on geprüft: höchste vollständig belegte Stufe, Begründung der nächsthöheren Stufe, Zählregel und Kurztexte (headline/preview) ohne neue Aussagen; Lücken als „nicht öffentlich belegt“ ohne Schwächenaussage. Abwägungen geprüft: Skyranger 30 procurement=3 (Verifikationsmuster als Prototyp, methodisch begründet und dokumentiert); Thales/Saab konsistent auf Systemebene (Familie/Komponente nicht übertragen); Tridon eu_customers=1 mit dokumentierter Alternativauslegung.",
      "fingerprint": "398bbf1f8e1391e90313ff97d9d64c9fc8b657cf746bc3a16992d14507048e05"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-aerie",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "dbc20b5a4b67687e4ecd7882618c3e8b9aee64e0bd693642549f44007accd56f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-ahead",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "b3c42cc2a268d84c0c3ab3d0eae5309cfead005b5431c818afffa29446482c34"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-artillery_ammo",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "1a806427fc567063d762bb6127767da984b25b27375de9695b5158e5ee911ff2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-cuas_toolbox",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "711f98267b767db4d8b49fd8fd841507ac91b506da68c4dc97826d71dcf945bb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-defence_electronics",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "d24103f78f859b7068e2c00b4aba8bd1312bf26f52302b09f6b64965d6a70dff"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-digitalization",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "2e3e1b298cfc481426d1ecd380e662c09423eb6168f96514ca2071e526b59d37"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-f35_fuselage",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "9d518567be5243bc012ffe8cd408d4dfd082583d2a525ee008612b4243f8669c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-hel_naval",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "5aba940b3b59013c05cb545bf6525cdf7bb10dde318fe31172061d63b3413962"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-logistic",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "6c24e71d7340f263d9a1b3f1ea427f75e4473950145b3233425b48ffd83e91c8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-loitering",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "370ac00c8547731116dfcc38f21a8543b2c986fb721aa1ec08e8ce0f00734b63"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-msu",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "990ee772173d19e6acd0d1420ad1a2fab6145aad990506903dc5e3b456029bc1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-naval_ad",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "91985b98ced6069fcffb5c36e6cdc3c777f3f2fe565b33eafeb8ca5e9ff90055"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-naval_ships",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "2f4766cc86a8e34ecc3a978f0ae19729526bb3fb03919ea79d38e0ec7f69f1a7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-power_systems",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "ddc3e37265de1db609c863cdd10fd0e6830d0dcf5a75cd5e419d7549e960e09b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-protection",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "a2603cc38687eb6cce9bae311100822882defd57963da9d0f99e9892102e7ea2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-revolver_gun_mk3",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "8cd0ec229074f1ec660311a55c611b0bff57195b45c0947c4bd62004fb09e1aa"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skyguard_skyshield",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "cfd1346ec2cdd6536b3695cf9c99d4fadf1d96fd2ba7eedf14dbb40e76f00976"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skyknight",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "d8ea487b41375f6cefb066b5541b72b6c40a98ba800b677badae017486fd457c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skymaster",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "86d912cb79399d39f91a314a70a938acfea5861f279c6c4264a80e025ad2df72"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skyranger30",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "141ce7410bf8a997d533e6574aefd1319678afa794d6dcf4373ad42005cd63fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-skyranger35",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "4c17ef5751ba08732e03ae855b207fe1931f915a6ed5ab040903a2345ea269f0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-space_sar",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "28fdb4bd1c131b0af5012ae6ce872312bd4b634d35b160406fb94fe14bb5e02c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-tracked_ifv",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "89733624941d3d82079fc61caa3d2ac594b610ad9477c4cd8e63e3acf0bf57f6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-ugv",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "90e9882fe713f1b5156fc864fe6c7434fa3761db5fff63217e46a9718b69a90f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-weapons",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "297b0567556ed6b067b1e77acf0e4e2c09b79b91c816a250df262fd02dc74eaf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-wheeled",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "b8201f950f1baec05eb2d89d00c1d05ae20a62fcebd86c1b8e4fb2f3c86ed60e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-PM-xtar3d",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Reifeeinordnung nach portfolio-maturity-v1 geprüft: höchster konkret belegter Meilenstein, nächsthöhere Stufe begründet, Herstellerangaben gekennzeichnet; unbestimmbare Produkte ohne Unreifeaussage. Skynex 6: Anker „wiederholte Auslieferung“ formal erfüllt (UA offiziell zwei, IT eine Batterie), kleine Stückzahl und Herstellerangaben in uncertainty transparent. UGV 4: GOAT-Teilnahme/Vorauswahl als Pilot/Validierung laut Hersteller gekennzeichnet, kein Serienauftrag.",
      "fingerprint": "b55a5097b22aa4fed0ef01546ca2e1947d32ea73029738a6e0072489020342ff"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-ASIA",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "6f72992ab3199524b3a2840021b4c0d31ca1087a0c17f712f4c5980b331d40c2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-AU",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "7951d77d30712f881b4343ddca10c5db02c8f2332f38023aad15eb459e9aae19"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-CA",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "8e2a819bdc31b04ab1842babbff851a05c09b25b56351c5d8341cdc75c6f16cf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-CEE",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "e1e7840bb57319c57e1906618b7dc196b9103f3405f99d704344ddf7996c938d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-CH",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "d97ab5bc9c8788814ca973dc2357e351b1805ceac9a9578b09b802b99c49ac87"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-DE",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "1b61bd17eaa5c230b38171b8098cdc9ed34a400423222c01d28b7b3609a45226"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-IT",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "0386c8fb2ad39fbe8f4b7c25fd693553ab116ed22466ee8fed4895758d65ae2a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-ME",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "ee03fb3a432939923fb037bcd8fcfd29a086e28c44b2612801f9acb109455462"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-UA",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "3b81a73d30042d3cea2116aa0a5c44001632b76aa74048d4df3a5d66ca50cefc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-UK",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "6611d7adde5c2ed08a301e0f0ca3892b5732f20223a0d795a83838a4c154b998"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-US",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "db8909984bd13764cb5e3feaa8aa08f8c77476dfacb4d80cefdee7a944d4f827"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-WEU",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "3855dc0f322567e2ec0cc32382444653dc2170ae46fcefe005cc0df0231292fa"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-RP-R-ZA",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Präsenzstufe nach regional-presence-v1 geprüft: Eigen-/JV-/Kundenrolle, Status und Standortzählung; JV-Werke nicht als own, Kundenaktivität hebt Stufe nicht; höchste erfüllte Stufe korrekt.",
      "fingerprint": "09113ad7b512d143f3766a457c0bc84ab8ca1cdfd262c6cd0709363d26547cc0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TAD-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Themenkarten gegen Fakten geprüft; Herstellerangaben und Gegenrecherche (Ukraine) korrekt getrennt; kein Gesamtranking.",
      "fingerprint": "de874230b20e3dfd17bb0ed08ba0d610796d6cf79046bd8f4c373f36843479b0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TAD-04",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Themenkarten gegen Fakten geprüft; Herstellerangaben und Gegenrecherche (Ukraine) korrekt getrennt; kein Gesamtranking.",
      "fingerprint": "aa12f92cd62c9e0c5359174429e0e9715d80257ed36e9b632bc07ad6945f111f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TEU-01",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Marktthemen gegen M-Fakten geprüft; SIPRI als Budgetkontext ohne Segmentvolumen, SAFE/EDIP-Regeln und Zuteilungen korrekt.",
      "fingerprint": "549f15f3c0fc3fba9312802d2ee3b5c0a0bb288fa79f5a91f6a435fe93af9a37"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TEU-02",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Marktthemen gegen M-Fakten geprüft; SIPRI als Budgetkontext ohne Segmentvolumen, SAFE/EDIP-Regeln und Zuteilungen korrekt.",
      "fingerprint": "e2cc4b24490909eee0bfb02ec792a63f5de45405031d77bd373bddcceb77344c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TEU-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Marktthemen gegen M-Fakten geprüft; SIPRI als Budgetkontext ohne Segmentvolumen, SAFE/EDIP-Regeln und Zuteilungen korrekt.",
      "fingerprint": "5db183bc2fb57100d801ca90fac8b1bb3637210a3c06ffe3aa96f779414ebd12"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TEU-05",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Marktthemen gegen M-Fakten geprüft; SIPRI als Budgetkontext ohne Segmentvolumen, SAFE/EDIP-Regeln und Zuteilungen korrekt.",
      "fingerprint": "13e0e2c4939f858bdb76b8c65c22a88ee25a59fe7ee7d5966c636fce606abd5f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "I-TEU-06",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: Marktthemen gegen M-Fakten geprüft; SIPRI als Budgetkontext ohne Segmentvolumen, SAFE/EDIP-Regeln und Zuteilungen korrekt.",
      "fingerprint": "30000dd577c46402fc662e9444496a1ae4a6b90edac73737898dce3aeecbdd43"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-OP-01",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "5612dd29cdd43f08595f7540d96710c2d6f587db7f1b738559a6610e923885fc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-OP-02",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "f757c7d05f1e5b37e30309bcb4b4d37188da8ff946dfef30ae4164e97900579d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-ST-01",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "1997bd1426edce2b31141c6061c4d44b158973c2621aa30e11e83265ff245e45"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-ST-02",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "321d70102b8c404018b476842a96a8a63069aace92c2f419d196a2199c2f5544"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-ST-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "028fdfbe7cae6270e2b1a32594fc8d60743889c4ad4adcc83c0bb1d88907d995"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-TH-01",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "68c4bfa587d3d571a7a2a2a9cc934b1974af8b333f0c4ea6a14b8ed9017decbc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-TH-03",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "0fb5372c2197957fe26489e7e1931430b15d4ec85ad4de9abd28b43cab50ac80"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "S-WE-02",
      "evidence_review": "Gegenüber positioning-r1/swot-r1 inhaltlich unverändert (Feldvergleich); Abhängigkeiten im neuen Kontext unverändert A-geprüft (Basis-Review r3). r1-Befund ausdrücklich bestätigt: SWOT-Punkt gegen I-/A-Abhängigkeiten geprüft; Zuordnung intern/extern korrekt, keine Datenlücke als Schwäche, Status und Zeitbezug erhalten. S-ST-02 bleibt auf Einzelkriterien begrenzt (uncertainty: kein Gesamtvorsprung) und ist so ausgewogen.",
      "fingerprint": "4b9113a9ecbebcaa96ab7e82e59802500aabda6e368e39b4c042e3c0a67239ae"
    }
  ],
  "missing_decisions": [],
  "fact_review": {
    "C-003": {
      "id": "C-003",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-004": {
      "id": "C-004",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-005": {
      "id": "C-005",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-007": {
      "id": "C-007",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-008": {
      "id": "C-008",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-009": {
      "id": "C-009",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-010": {
      "id": "C-010",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-011": {
      "id": "C-011",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-013": {
      "id": "C-013",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-014": {
      "id": "C-014",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-015": {
      "id": "C-015",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-016": {
      "id": "C-016",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-017": {
      "id": "C-017",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-018": {
      "id": "C-018",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-019": {
      "id": "C-019",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-020": {
      "id": "C-020",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-021": {
      "id": "C-021",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-022": {
      "id": "C-022",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-023": {
      "id": "C-023",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-024": {
      "id": "C-024",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-025": {
      "id": "C-025",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-026": {
      "id": "C-026",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-027": {
      "id": "C-027",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-028": {
      "id": "C-028",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-029": {
      "id": "C-029",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-033": {
      "id": "C-033",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-034": {
      "id": "C-034",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-037": {
      "id": "C-037",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-042": {
      "id": "C-042",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "C-053": {
      "id": "C-053",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-AT-ESSI-01": {
      "id": "M-AT-ESSI-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-AT-SKR-01": {
      "id": "M-AT-SKR-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-AT-SKR-02": {
      "id": "M-AT-SKR-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-CZ-MSH-01": {
      "id": "M-CZ-MSH-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DE-ARM-01": {
      "id": "M-DE-ARM-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DE-IRIS-01": {
      "id": "M-DE-IRIS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DE-IRIS-02": {
      "id": "M-DE-IRIS-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DE-NNBS-01": {
      "id": "M-DE-NNBS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DE-SKR-01": {
      "id": "M-DE-SKR-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DE-SKR-02": {
      "id": "M-DE-SKR-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DIEHL-01": {
      "id": "M-DIEHL-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DK-GBAD-01": {
      "id": "M-DK-GBAD-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DK-IRIS-01": {
      "id": "M-DK-IRIS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DK-SAMPT-01": {
      "id": "M-DK-SAMPT-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-DK-VLM-01": {
      "id": "M-DK-VLM-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-EU-EDIP-01": {
      "id": "M-EU-EDIP-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-EU-SAFE-01": {
      "id": "M-EU-SAFE-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-EU-SAFE-02": {
      "id": "M-EU-SAFE-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-EU-SAFE-UK-01": {
      "id": "M-EU-SAFE-UK-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-IT-A2CS-01": {
      "id": "M-IT-A2CS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-LT-MSH-01": {
      "id": "M-LT-MSH-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-SIPRI-00": {
      "id": "M-MKT-SIPRI-00",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-SIPRI-DE": {
      "id": "M-MKT-SIPRI-DE",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-SIPRI-DK": {
      "id": "M-MKT-SIPRI-DK",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-MKT-SIPRI-PL": {
      "id": "M-MKT-SIPRI-PL",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-NL-SKR-01": {
      "id": "M-NL-SKR-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-PL-NAREW-01": {
      "id": "M-PL-NAREW-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-PL-PIL-01": {
      "id": "M-PL-PIL-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-PL-PIL-02": {
      "id": "M-PL-PIL-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-SAAB-01": {
      "id": "M-SAAB-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-SE-IRIS-01": {
      "id": "M-SE-IRIS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-SE-RBS-01": {
      "id": "M-SE-RBS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-SE-TRI-01": {
      "id": "M-SE-TRI-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-SKR30-ARCH-01": {
      "id": "M-SKR30-ARCH-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-THA-01": {
      "id": "M-THA-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-THA-02": {
      "id": "M-THA-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "M-UK-SHORAD-01": {
      "id": "M-UK-SHORAD-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-AD-01": {
      "id": "P-AD-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-AD-07": {
      "id": "P-AD-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-AD-08": {
      "id": "P-AD-08",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-AD-09": {
      "id": "P-AD-09",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-AHD-01": {
      "id": "P-AHD-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-CUAS-01": {
      "id": "P-CUAS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-CUAS-02": {
      "id": "P-CUAS-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-CUAS-03": {
      "id": "P-CUAS-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-DS-01": {
      "id": "P-DS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-DS-02": {
      "id": "P-DS-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-DS-03": {
      "id": "P-DS-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-DS-04": {
      "id": "P-DS-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-DS-05": {
      "id": "P-DS-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-HEL-01": {
      "id": "P-HEL-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-NAV-01": {
      "id": "P-NAV-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-NS-01": {
      "id": "P-NS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-NS-02": {
      "id": "P-NS-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-NS-03": {
      "id": "P-NS-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-PS-01": {
      "id": "P-PS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-AU-01": {
      "id": "P-REG-AU-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-CA-01": {
      "id": "P-REG-CA-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-CH-01": {
      "id": "P-REG-CH-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-DE-01": {
      "id": "P-REG-DE-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-ES-01": {
      "id": "P-REG-ES-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-EU-01": {
      "id": "P-REG-EU-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-HR-01": {
      "id": "P-REG-HR-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-HU-01": {
      "id": "P-REG-HU-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-IT-01": {
      "id": "P-REG-IT-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-JV-01": {
      "id": "P-REG-JV-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-NO-01": {
      "id": "P-REG-NO-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-OWN-01": {
      "id": "P-REG-OWN-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-PL-01": {
      "id": "P-REG-PL-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-RO-01": {
      "id": "P-REG-RO-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-SG-01": {
      "id": "P-REG-SG-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-UA-01": {
      "id": "P-REG-UA-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-UK-01": {
      "id": "P-REG-UK-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-US-01": {
      "id": "P-REG-US-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-REG-ZA-01": {
      "id": "P-REG-ZA-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-RGM-01": {
      "id": "P-RGM-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKM-01": {
      "id": "P-SKM-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKN-01": {
      "id": "P-SKN-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKR-01": {
      "id": "P-SKR-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKR-02": {
      "id": "P-SKR-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKR-03": {
      "id": "P-SKR-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKR-04": {
      "id": "P-SKR-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKR-05": {
      "id": "P-SKR-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKR-06": {
      "id": "P-SKR-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKR-07": {
      "id": "P-SKR-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKX-01": {
      "id": "P-SKX-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKX-02": {
      "id": "P-SKX-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKX-03": {
      "id": "P-SKX-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SKX-04": {
      "id": "P-SKX-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SNS-01": {
      "id": "P-SNS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SNS-02": {
      "id": "P-SNS-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-STAT-01": {
      "id": "P-STAT-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-STR-03": {
      "id": "P-STR-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-SVC-01": {
      "id": "P-SVC-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-VS-01": {
      "id": "P-VS-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-VS-03": {
      "id": "P-VS-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-VS-04": {
      "id": "P-VS-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-VS-05": {
      "id": "P-VS-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-WA-01": {
      "id": "P-WA-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-WA-02": {
      "id": "P-WA-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "P-WA-03": {
      "id": "P-WA-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-AD-01": {
      "id": "T-AD-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-AD-02": {
      "id": "T-AD-02",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-AD-03": {
      "id": "T-AD-03",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-AD-05": {
      "id": "T-AD-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-AD-06": {
      "id": "T-AD-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-AD-07": {
      "id": "T-AD-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-01": {
      "id": "T-EV-01",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-04": {
      "id": "T-EV-04",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-05": {
      "id": "T-EV-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-06": {
      "id": "T-EV-06",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-07": {
      "id": "T-EV-07",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-08": {
      "id": "T-EV-08",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-09": {
      "id": "T-EV-09",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-EV-10": {
      "id": "T-EV-10",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-FIN-05": {
      "id": "T-FIN-05",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    },
    "T-FIN-09": {
      "id": "T-FIN-09",
      "depth": "A",
      "status": "übernommen",
      "evidence_review": "Explicit reuse from basis"
    }
  }
}
```
