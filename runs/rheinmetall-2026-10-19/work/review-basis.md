# Review

```json
{
  "schema_version": 1,
  "run_id": "rheinmetall-2026-10-19",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-19",
  "phase": "basis",
  "status": "freigegeben",
  "material_errors": [],
  "review_scope": "Leitprüfung Basis Runde 3: 297 Claims, Dokumentbefunde aller 3 Jobs ohne Korrektur/offen; Umsetzung der vier Runde-2-Korrekturen (P-R51, P-R100, M-KND-01, P-R60/P-R61) samt Folgeänderungen (it-lrmv, us-hub/us-hq, hu-zala-dev, O-knds-spectrum) gegen Paket und Originale geprüft; gesamte module_views, Netzwerk, coverage/gaps und Auftragsabdeckung erneut semantisch bestätigt.",
  "open_limits": [
    "Ausgewiesene, nicht auflösbare Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken-Datum, NVL-Datum, CMD-Datum); Bezahlschranken nur im Teaserumfang (H-M01, H-M08, M-HAN-06); überwiegend Herstellerangaben, keine Behörden-/Vergabedaten; Cluster: Software/KI und Vergabeportale nicht geprüft; Portfolio: Beleglücken (Kassel/Kiel/Bremen/München, Battlesuite/Gladius/MQ-28, Golfstaaten); Modelle nur als sonnet-5-5/medium konfiguriert."
  ],
  "non_blocking": [
    "Siehe Claim-Notizen: M-KND-01 location/HB-Kürzel, P-R100 Vienna nur AUSA-Quelle, C-STR-37 Datum, C-STR-21 \"litauische\", C-CAP-04 Auszug, P-D11 Querverweis, it-lrmv kind/status großzügig.",
    "Weiter aus Runde 2: T-E07 Kaufpreis-Unsicherheit abgleichen; P-R90, P-N10, T-E09/T-E13, C-STR-35 Datumsbasis; Region us Virginia im coverage_note; M-MKT-01..07 in keiner module_view."
  ],
  "non_blocking_notes": [
    "Siehe Claim-Notizen: M-KND-01 location/HB-Kürzel, P-R100 Vienna nur AUSA-Quelle, C-STR-37 Datum, C-STR-21 \"litauische\", C-CAP-04 Auszug, P-D11 Querverweis, it-lrmv kind/status großzügig.",
    "Weiter aus Runde 2: T-E07 Kaufpreis-Unsicherheit abgleichen; P-R90, P-N10, T-E09/T-E13, C-STR-35 Datumsbasis; Region us Virginia im coverage_note; M-MKT-01..07 in keiner module_view."
  ],
  "view_findings": {
    "all": "Alle vier module_views, Profil/Medien-Timeline, Events, 39 Produkte, 21 Regionen, Netzwerk (68 Knoten/83 Kanten), 36 Marktbeobachtungen, coverage/gaps und shared_limitations bestätigt; keine wesentliche Abweichung offen."
  },
  "review_work_fingerprint": "c3898a724d2c55bc1d52895dd4efe377f62dfe2ec29f09fd8bb6ef89e270caa1",
  "plan_fingerprint": "da10258b7ec6256e20eb86c78d3bdc96f05f736f1741533f5204a4fcc8f347e0",
  "source_collection_fingerprint": "04779e4a0d7c98e567157de197d57e126b3b92d1ed7950fd6edfe208ca9747df",
  "scope_and_mappings_checked": true,
  "source_checks": [
    {
      "source_id": "S-001a4ac74ab4feec",
      "claim_ids": [
        "P-A01",
        "P-R30"
      ],
      "note": "Zugewiesenes Original gelesen: P-A01, P-R30 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-001a4ac74ab4feec",
        "url": "https://www.rheinmetall.com/en/company/divisions/air-defence",
        "content_sha256": "04027b31a264fdac19cae63fbe67d5e0857b596aed96fe0abcd3b3d71aca8744",
        "text_sha256": "2921266bdc8a9097b3005df21bd7dacc8aa14e1e2a8f3aba3e8501ad5e9ae733",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-042b26990fdc2a9d",
      "claim_ids": [
        "C-STR-14",
        "C-STR-15",
        "P-N02",
        "T-E07"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-042b26990fdc2a9d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/03/2026-03-02-rheinmetall-takes-over-nvl",
        "content_sha256": "48ccff518a15a6fdd3e21462b4c643552cbc03bf4f35394e40d75fbd46a9fc70",
        "text_sha256": "24749e80c36c79f614050d1019e086f13e06f3d9450681cfa9defacf217e4290",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-04b4522db1cf4f65",
      "claim_ids": [
        "T-E09"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-04b4522db1cf4f65",
        "url": "https://militarnyi.com/en/news/rheinmetall-apologizes-for-ceo-s-comments-about-ukrainian-housewives-with-3d-printers/",
        "content_sha256": "0e960196b5fcbc97429b7bdbaeb2550c9c231a552a1177cf43aba33d642cb94a",
        "text_sha256": "0797263644c493417d19e03e65f237ca967e8a5205d689373637cb51bad8a873",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-04cc080af88f833d",
      "claim_ids": [
        "C-TEC-04",
        "H-M06",
        "P-D30",
        "T-E24"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-04cc080af88f833d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-06-rheinmetall-iceye-space-solutions-provides-the-bundeswehr-with-access-to-sar-satellites",
        "content_sha256": "be998ef3f2f260fc290f20565c2e9f22f67e28306832fccf8e97dd7f6bd33b72",
        "text_sha256": "442b06303382b93c7fafdadc0ed3428b8eb3921d2c4ba73d49f4d3e80b67ed3f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-04d78beb73ec03e5",
      "claim_ids": [
        "P-C02",
        "P-R01",
        "P-S02"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-04d78beb73ec03e5",
        "url": "https://www.rheinmetall.com/en/company/divisions",
        "content_sha256": "6b497215704bb02cf4d390b0c4c50bab938d28ff892e21b7d2062da95cef421f",
        "text_sha256": "19c0561cae101d9b6903dc931394cf5bd7c18d58eea5c9a8fd27629f4f4dc447",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-052e7d1e29545a63",
      "claim_ids": [
        "M-NAM-07"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 4c6e4ac9d02b...",
      "snapshot": {
        "source_id": "S-052e7d1e29545a63",
        "url": "https://www.nammo.com/locations/mesa-arizona/",
        "content_sha256": "4c6e4ac9d02bc501a55458484e75e974e7f43beef02890c0ba0144f813831f10",
        "text_sha256": "26f8e8de695afc987f32b5f47d615de592ab52f8e5a718d4cac577cc6b57b771",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-05d2ba4a7ea0433c",
      "claim_ids": [
        "M-MKT-04"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-05d2ba4a7ea0433c",
        "url": "https://en.interfax.com.ua/news/general/1147530.html",
        "content_sha256": "75ed5e114ced95c42e3b0957992fc4b8f9d202cd927197a31d1a2c65c6e2f922",
        "text_sha256": "bea33632c5d74a5641cbd2e2e52a7c87d9956f150636ff9b6662027ae37309b3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0720809d463a2525",
      "claim_ids": [
        "M-RHM-05"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-0720809d463a2525",
        "url": "https://www.edrmagazine.eu/rheinmetall-wins-triple-digit-million-euro-contract-for-explosives-factory-in-varpalota-hungary",
        "content_sha256": "0d61eb6409cf700cb19170b4be232f33a4507c80f8cb824cd601debb70ce8167",
        "text_sha256": "afc1fca3160af94b4dc1d82f774bb5efc31cb76e84a9ff5b48eab96ef4ec26b8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-078c6e124a0a035b",
      "claim_ids": [
        "T-E19"
      ],
      "note": "Rheinmetall-Meldung 03.08.2026 (PDF, Zweispaltenlayout) Z. 7-29 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-078c6e124a0a035b",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/08/2026-08-03-rheinmetall-presents-the-gmf140-the-next-generation-frigate.pdf",
        "content_sha256": "628cb8c7dafffbb276bcc43eb712c0f2f0dc3141b324a25d1bbc5385867e1636",
        "text_sha256": "a70332694e724b8d18958832c71cf9aad2d4464325191298f5bf95714ffcc41b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-088d08dcf25c1d20",
      "claim_ids": [
        "P-D20"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 5ed8b49da826...",
      "snapshot": {
        "source_id": "S-088d08dcf25c1d20",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/04/2026-04-22-rheinmetall-receives-major-contract-in-the-drone-sector",
        "content_sha256": "5ed8b49da826dbc7946b9d0f08a1932a1cdb836e07160a5569f335aa27303916",
        "text_sha256": "879de2216573ae0201fa89d5b0e790f297ca747bc907a145f6728ee4a353d1a3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0aa94a6db6481400",
      "claim_ids": [
        "M-NAM-02"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 8d43cfa90050...",
      "snapshot": {
        "source_id": "S-0aa94a6db6481400",
        "url": "https://www.nammo.com/products/ammunition/large-caliber-ammunition/155-mm-series/155-mm-im-high-explosive-extended-range/",
        "content_sha256": "8d43cfa9005087b260a39d6232cd323425b092e3e19596cc0158ae400a2a3523",
        "text_sha256": "b068d2fe22f63167762aa11462f1decdea36dd155ada5e065011c9b3077696ec",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0b6a8c7f7a47ed28",
      "claim_ids": [
        "H-09",
        "T-E02"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 8fdb7b926db3...",
      "snapshot": {
        "source_id": "S-0b6a8c7f7a47ed28",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/09/2025-09-15-rheinmetall-reaches-agreement-with-luerssen-on-acquisition-of-naval-vessels-luerssen-nvl",
        "content_sha256": "8fdb7b926db37c0bc136216bd79db2ae36ba1134628f9e61c9698b79ed98a56d",
        "text_sha256": "e5fe2be60d46b80f055f71d9ce8a00e2072bd322d0674159ea803668e7481d7b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0bd71507c5c59e04",
      "claim_ids": [
        "T-11",
        "T-20",
        "T-E28",
        "T-E29"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-0bd71507c5c59e04",
        "url": "https://www.rheinmetall.com/en/investor-relations/calendar-and-events/financial-calendar",
        "content_sha256": "e2acb4ed216c7fe25c6636f1c59c8573abf4cfa201cbb270b9e359c24e5cc05c",
        "text_sha256": "d21a0d0b7a9a52fd43c58b85174cb3008d38ca3cceeec3eb3af90809e0e13be3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0bf21d6b5d52b9d5",
      "claim_ids": [
        "C-STR-38",
        "P-N60",
        "P-S05",
        "T-E17"
      ],
      "note": "Breaking-Defense-Artikel 06.08.2026 Z. 40-72 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-0bf21d6b5d52b9d5",
        "url": "https://breakingdefense.com/2026/08/rheinmetall-projects-346-million-naval-loss-after-f126-frigate-cancellation/",
        "content_sha256": "05dbf5852d794d697bfe6442f3102b6d92a48294d25bf07994ada37d17d9c41b",
        "text_sha256": "44c3720f5ec604a381ee69b87ac500467c54681d729b1cf436c8ddac8a4c792f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0f3e4291120ca045",
      "claim_ids": [
        "M-MKT-06"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-0f3e4291120ca045",
        "url": "https://euneighbourseast.eu/news/latest-news/european-defence-industry-programme-eu-gives-final-approval/",
        "content_sha256": "92c30dcc054e60d1421e7110a35a90bbfc522fa9eabdd546f03841c1b7718399",
        "text_sha256": "fbfce9abe85dbf11538368bad006c312a8b203ff33c1705c22adb12c3c24acba",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-110cc749cec119a4",
      "claim_ids": [
        "P-V20",
        "T-E05"
      ],
      "note": "Zugewiesenes Original gelesen: P-V20, T-E05 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-110cc749cec119a4",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-19-rheinmetall-and-knds-to-supply-200-armoured-fighting-vehicles",
        "content_sha256": "d49f08c843010f768eeb0f71755bac7c77b18c30a5872042e308f6375dd792be",
        "text_sha256": "6a9c68cde70198858e4b5bb12539f3c58a7419d7523382b279cecd58470d55f7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-11207e9f835a9f20",
      "claim_ids": [
        "M-HAN-06"
      ],
      "note": "GBP (Login/Bezahlschranke): nur Überschrift und Teaser gelesen; Volltext nicht zugänglich. Snapshot http-original, content_sha256 89300d2df823...",
      "snapshot": {
        "source_id": "S-11207e9f835a9f20",
        "url": "https://gbp.com.sg/stories/hanwha-ramps-up-extended-range-shell-production-for-global-markets/",
        "content_sha256": "89300d2df8230190cde0ea5802976025920161c1cab7ae262fe461ad1068f44e",
        "text_sha256": "ad8d54654adf1a0386f65f326f5d04fdfdaf87c9f062ce9cb28067ad2863e642",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-11a2bf8c21d08244",
      "claim_ids": [
        "M-BAE-04"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 bb0ca5b73c3d...",
      "snapshot": {
        "source_id": "S-11a2bf8c21d08244",
        "url": "https://ukdefencejournal.org.uk/bae-unveils-new-tech-to-boost-uk-ammo-output-sixteen-fold/",
        "content_sha256": "bb0ca5b73c3d73438032501a990f276d0b2d7970eccbba759724c4c41ecf59f9",
        "text_sha256": "59db8969c0c98b774cad182966a2bed0f2b9e236905aab14fd6c453cc13a1a25",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-126b43514d72258d",
      "claim_ids": [
        "P-V51"
      ],
      "note": "Englische Pressemitteilung UTF-Trucks 28.05.2026 Z. 14-21 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-126b43514d72258d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/05/2026-05-28-rheinmetall-is-supplying-more-than-2-000-utf-trucks-to-the-bundeswehr",
        "content_sha256": "5e3c1ec17dc0140f02c47d12572e1d40e98eac544325952a46f300dbc99d53eb",
        "text_sha256": "79479014699a68439af0d6f1d6fbffe1760b6c290cb5ac09a109c0e14e9fd675",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-182f1bf64398f3d4",
      "claim_ids": [
        "M-GDO-01"
      ],
      "note": "GD-OTS-Seite Artillery Propelling Charges (UBX, M119A2, MACS) vollständig gelesen; die Seite enthält keine Geschoss-/Zünderprodukte. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-182f1bf64398f3d4",
        "url": "https://www.gdots.com/propellant-and-propulsion/howitzer-propelling-charges/",
        "content_sha256": "b25d82e34281afdec923a17c4c16f66b19a13c3154b283ff36f218ce9b7d2c17",
        "text_sha256": "208f6060843b4ddb02902a596632551b38c415378c3121ff17ffac90120b28f0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-19990f4210d9f4d3",
      "claim_ids": [
        "P-W10"
      ],
      "note": "Pressemitteilung 05.09.2025 Z. 9-35 (Key Facts, Absätze 1-8, Standortbox) gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-19990f4210d9f4d3",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/09/2025-09-05-factory-opening-in-unterluess",
        "content_sha256": "63c1418d8884585a3b509cfc3a13eaceb3fac4067ee8db6f89b2c77fec524e07",
        "text_sha256": "79615494cd9613c734d2396ceaacffd45f12caf4547e9a0eae40437d217b8538",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1a21add65a752dbe",
      "claim_ids": [
        "P-N10"
      ],
      "note": "Pressemitteilung Taufe Korvette LÜBECK (29.04.2026) Z. 12-24 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-1a21add65a752dbe",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/04/2026-04-29-rheinmetall-celebrates-first-ship-christening",
        "content_sha256": "43ed2edc7be5f855c61b77bbfe74dd5a9ceaef6cc68e385cd1d8d7a4f9eef1fc",
        "text_sha256": "1e93e9ea86d21612c152d3ce49dc68bada9dca7054c798acd59900aa8c96db8b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1a44c417ab617faa",
      "claim_ids": [
        "P-D10"
      ],
      "note": "Zugewiesenes Original gelesen: P-D10 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-1a44c417ab617faa",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-20-rheinmetall-books-a-call-off-of-eur-100-million-under-the-d-lbo-framework-agreement",
        "content_sha256": "c34079d36c7a3096008d976e30b327732aa922bc86f61538b8ff85b5081e14e4",
        "text_sha256": "987291ca388d10e80633dd295ed96cfeb86ad1362bce8e861c0a4b726d524c8b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1a558a92449e8e86",
      "claim_ids": [
        "P-A50"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-1a558a92449e8e86",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-07-rheinmetall-and-praetorian-aeronautics-deliver-containerised-aerie-counter-uncrewed-aircraft-system",
        "content_sha256": "66e20bdf0a6d5bea45ee0d59778abbed8f3526e52aac3157c7a9019291b0d7a6",
        "text_sha256": "f04e4985faa8b51b92f1d3b99838e5044019ec242cf5435a047f2cdb80633377",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1db9c54bc6663d61",
      "claim_ids": [
        "T-E03"
      ],
      "note": "PDF-Pressemitteilung Muni Berka (10.12.2025) Seiten 1-2 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-1db9c54bc6663d61",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2025/12/2025-12-10_rheinmetall-erwirbt-muni-berka.pdf",
        "content_sha256": "373cf3cbe60c7b6f43be010adae7ef79be8d51d945a0377d67d67463327c76c3",
        "text_sha256": "cd3168704af750cdaba7774ca7c78989bf9d22ed6b91d415db9b6669fd9a4507",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-1e501c0b6e3d8fb8",
      "claim_ids": [
        "M-BAE-03"
      ],
      "note": "UKDJ-Artikel Z. 48-68 gelesen (Kommentarbereich nicht als Beleg genutzt). Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-1e501c0b6e3d8fb8",
        "url": "https://ukdefencejournal.org.uk/uk-places-280m-order-for-frontline-battlefield-munitions/",
        "content_sha256": "b8a88a37705ab8f60bcd59b791d1c6ed84a0169e4f837aaaa87e5769c9c2d362",
        "text_sha256": "5b7cd07d616dd890798b7ba0d8384d47a807a1a3f12df64eaf45eb5edf0ade5a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1e5add6204530ccc",
      "claim_ids": [
        "H-M01"
      ],
      "note": "Handelsblatt (Bezahlinhalt): nur frei lesbarer Kopf/Anreißer/Eingangsfrage gelesen; Rest hinter Bezahlschranke nicht geprüft. Snapshot http-original, content_sha256 1d9d70fd0696...",
      "snapshot": {
        "source_id": "S-1e5add6204530ccc",
        "url": "https://www.handelsblatt.com/unternehmen/industrie/ruestung-rheinmetall-waechst-schlafen-sie-noch-herr-papperger/100252952.html",
        "content_sha256": "1d9d70fd06962416f60ec6f798d81d1cff245371e16147d0bff0e68c6c5658cc",
        "text_sha256": "94fbc5973606218e1b4aa51ec7b0665d9f26bc27e77dd8ab059127b0d106a29c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1eae2dae5ac99788",
      "claim_ids": [
        "M-GDO-06"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 07f385e76e80...",
      "snapshot": {
        "source_id": "S-1eae2dae5ac99788",
        "url": "https://www.gdotscanada.com/product/energetic-materials/",
        "content_sha256": "07f385e76e8043be463180a200552d7d8a649d91c71b02a2078e5c7c304b3a31",
        "text_sha256": "be329f1fa03e34f41e9fed2ca38aeb7138d82ef09bf41a819d71890b2c0973cc",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1f76748059d5008c",
      "claim_ids": [
        "C-STR-22"
      ],
      "note": "Unternehmensseite RDM Abschnitte Über uns, Historie, Produkte (Z. 10-30) gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-1f76748059d5008c",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-denel-munition",
        "content_sha256": "3e3d6eed85c7c2927323f8eb35d2deb4903f5a969bca62b648a1b02454d1b0f8",
        "text_sha256": "bc8c2eedbbc7c9bdbd5c0dc66f81b5be09c4309de716f0476b7e9074657afd81",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1f77cb6f898210ce",
      "claim_ids": [
        "T-19"
      ],
      "note": "Investorenpräsentation September 2026 (PDF), Folien 5, 10, 22, 29, 38",
      "snapshot": {
        "source_id": "S-1f77cb6f898210ce",
        "url": "https://ir.rheinmetall.com/media/document/4ce7ca35-7088-4365-88d6-b43a0aa5cde6/assets/Rheinmetall_AG_2026_Investor_Presentation_September.pdf",
        "content_sha256": "24eb1efde161bb5cdaa637eb444a3bb9dae4c14e94535b0a4b40281b8ff76202",
        "text_sha256": "0c1fb589050b8edc19765a2565579fa99fec495fbc7ddde3267df72e8f2844a2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-1fcfbe98a40fffd8",
      "claim_ids": [
        "M-HAN-05",
        "M-MKT-07"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 9fafab332449...",
      "snapshot": {
        "source_id": "S-1fcfbe98a40fffd8",
        "url": "https://manufacturingdigital.com/news/how-hanwhas-2-2bn-arkansas-campus-boosts-us-artillery",
        "content_sha256": "9fafab332449c883e8bad3a7c0220daef88d439b9bbe543da57bdf91febc676e",
        "text_sha256": "590a29bb2fb7665d3079aa6190c8eafb6d975b91a4bc1e6f7d078139763e3d5a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2002ef0c3dd21d04",
      "claim_ids": [
        "C-TEC-03"
      ],
      "note": "PDF-Pressemitteilung Rheinmetall/Anduril 18.06.2025 Z. 1-40 gelesen; Web-Fassung S-5366... parallel eingesehen (identischer Inhalt). Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-2002ef0c3dd21d04",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2025/06/2025-06-18-Rheinmetall-Anduril%20Teaming-EN.pdf",
        "content_sha256": "617b004d6d444f0787bfe299ae5c98b38c87177bb1e1512650f9e2596ffacac7",
        "text_sha256": "cfdea233fd473448920f1aee59b7c064419d6a90c9a0af42d2e688cb49ec0cf5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-202cf065062fc9bb",
      "claim_ids": [
        "C-MKT-04"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 cdcd5a4d4603...",
      "snapshot": {
        "source_id": "S-202cf065062fc9bb",
        "url": "https://euro-sd.com/2025/12/major-news/48281/bundeswehr-sar-imagery-deal/",
        "content_sha256": "cdcd5a4d4603903e486c617e412e4ad29e71ec6a9200bcb621dd2be723f227bb",
        "text_sha256": "9c0d48bb5f33d85c217fc8be2c6562bfddc428cda1867fe9ddfda74ff1c3a44d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-213a79eb466923da",
      "claim_ids": [
        "M-BAE-01",
        "M-BAE-02"
      ],
      "note": "Herstellerbroschüre (PDF): Text der Seiten 2-5 gelesen, Datentabellen Seite 3 zusätzlich als Bild gegengeprüft. Snapshot local-original, content_sha256 623ac3e5c6a5...",
      "snapshot": {
        "source_id": "S-213a79eb466923da",
        "url": "https://www.baesystems.com/dam/jcr:2b61caee-8578-43ab-9899-33e6312a642f/155mm_brochure_February_2026.pdf",
        "content_sha256": "623ac3e5c6a5b5c7054a4ec73b2be2a952cc7e7d698817b65c3ba0e610197748",
        "text_sha256": "36d2fa319f4a76715d15916eac0c6152602d443c51c4a6bec25e068c9a85991a",
        "capture_kind": "local-original",
        "capture_note": "WebFetch-Binärdownload des Original-PDF am 2026-10-19 (direkter Cache-Abruf 403 durch Incapsula)",
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-22b4e8c338d5fc31",
      "claim_ids": [
        "M-BAE-05",
        "M-RHM-07"
      ],
      "note": "Calibre-Defence-Artikel 04.08.2026 Z. 35-52 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-22b4e8c338d5fc31",
        "url": "https://www.calibredefence.co.uk/mod-funds-22-firms-uk-munitions-factory-sites/",
        "content_sha256": "c9e0e35474199a0c7fd741ddfd437c6888932c8a892ea8a2d4d5563dac95d2c4",
        "text_sha256": "280fc7023f704fc81e3c9d78f1b3ccde7943e04822fd7e58c79d048fe35867d2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-250325098e8c729a",
      "claim_ids": [
        "H-M09"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 417dc8990a85...",
      "snapshot": {
        "source_id": "S-250325098e8c729a",
        "url": "https://stock3.com/news/rheinmetall-entscheidung-aus-berlin-machte-papperger-fassungslos-17134598",
        "content_sha256": "417dc8990a85b4347f2b44e43de6cea193eb7be25dc460fa9d70ffb03166ba92",
        "text_sha256": "88a22e77fd1e4f9da43780078d79b288a74c75eea25820e992dc8ea8725b3d3d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2572b016501230b4",
      "claim_ids": [
        "M-RHM-03"
      ],
      "note": "Pressemitteilung Spatenstich Werk Niedersachsen (12.02.2024) Z. 10-25 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-2572b016501230b4",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/02/2024-02-12-rheinmetall-baut-neue-munitionsfabrik-in-unterluess-spatenstich-mit-bundeskanzler-scholz",
        "content_sha256": "93e1cc92350d42f58fd132f1f70340143403756ebf900f305d124bc092f543d7",
        "text_sha256": "296bd4fe53f6525a3aa2e5fb61a2f1fd288f9edf7e57421db4b31a4f0fb994ec",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-25aa458cd8d5079c",
      "claim_ids": [
        "M-HAN-02"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 f3eaec906ef3...",
      "snapshot": {
        "source_id": "S-25aa458cd8d5079c",
        "url": "https://www.koreajoongangdaily.com/business/hanwha-aerospace-bae-systems-ink-130m-artillery-propellant-deal/10918959",
        "content_sha256": "f3eaec906ef33475c35d4c8efd7be5df68bd502235e3c80c7766e7ed5b377580",
        "text_sha256": "e7144ecfa9ed65f83557c65cc6a81a3f769ddc3df2bc1af904ef6d8c6c01ad0d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-265b6ce2d616b964",
      "claim_ids": [
        "C-STR-06"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-265b6ce2d616b964",
        "url": "https://ukdefencejournal.org.uk/rheinmetall-and-bae-create-uk-based-land-systems-joint-venture/",
        "content_sha256": "d8c5f44fac5d4b78817a8d22a32bbcb4a49dbb71ffb1098faf7b85c1a43da8e4",
        "text_sha256": "db05164929ac19a618ead6436061a77c0cf30fbb01e39fff05badf0bbcd0691a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2706942fb5928fec",
      "claim_ids": [
        "M-BAE-06"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-2706942fb5928fec",
        "url": "https://www.edrmagazine.eu/bae-systems-ordnance-systems-inc-more-and-improved-ammunition-and-energetics-for-the-us-and-its-allies",
        "content_sha256": "2257cec586c7a42c90247ea71310b279cffd153d631b88d3cc0f76faacd88678",
        "text_sha256": "af4f24ddaca8e2dd6c82b633c0b4dd9e2735060b8b838be2f980bbc1f67bcd88",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2706c2d0310324c4",
      "claim_ids": [
        "C-STR-37"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 5aa095448f52...",
      "snapshot": {
        "source_id": "S-2706c2d0310324c4",
        "url": "https://maritime-executive.com/article/germany-s-rheinmetall-acquires-romania-s-mangalia-shipyard",
        "content_sha256": "5aa095448f525bbfe0c63d47a8feb778c67e141337aa45edace6d5d4d84df016",
        "text_sha256": "a7b568dfc5abe9b6732d1139cb0d6a83e628dbe17a65035185ff8fac09ecff17",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2851734a3f197c02",
      "claim_ids": [
        "P-V01",
        "P-V50",
        "P-V72"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 4531564e281d...",
      "snapshot": {
        "source_id": "S-2851734a3f197c02",
        "url": "https://www.rheinmetall.com/en/company/divisions/vehicle-systems",
        "content_sha256": "4531564e281db4d7ca4d978ccca9dacd1f57d56198199fcb96348a5b2ea5f3dc",
        "text_sha256": "c49034a68202a9bf0908f3877f7aeb8963a3d67e13891a0ef4fc3633ba440abc",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-287cebfc8cf393ef",
      "claim_ids": [
        "C-MKT-08"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 5393b875f426...",
      "snapshot": {
        "source_id": "S-287cebfc8cf393ef",
        "url": "https://www.rbsl.com/",
        "content_sha256": "5393b875f42638f697aeaf473409f53634b7f1a59ab7389cf8ef343689b21b07",
        "text_sha256": "7a6535b48edf464cd7bfcbe3410080f249820263471d7e31a4208cd7d04e18cc",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2a19a44bae9c9218",
      "claim_ids": [
        "M-KND-01",
        "M-KND-02"
      ],
      "note": "KNDS Ammunition Catalogue 2026-2027 (PDF, Cache-Text): Seiten 2 und 7-19 (155 mm Artillery) gelesen; übrige Katalogseiten nicht geprüft. Snapshot http-original, content_sha256 1d0f80f9ae2c...",
      "snapshot": {
        "source_id": "S-2a19a44bae9c9218",
        "url": "https://knds.com/media/knds_ammunition_2026_2027_a5b0dd631b.pdf",
        "content_sha256": "1d0f80f9ae2c6e5385fd5968f723a560281f73ea122e997163472c3f5182efa1",
        "text_sha256": "7090f082badb82d9f31b76cb9f39b21ea763848f43eb46e3878216d64d3736d9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-2a52354ff7d7f7f4",
      "claim_ids": [
        "T-18"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 2f6627099eb5...",
      "snapshot": {
        "source_id": "S-2a52354ff7d7f7f4",
        "url": "https://www.boersen-zeitung.de/unternehmen-branchen/rheinmetall-strebt-position-als-rundumanbieter-mit-50-mrd-euro-umsatz-an",
        "content_sha256": "2f6627099eb570beeec912cd1a246adc3900909c224dd08a922e64a80fd36633",
        "text_sha256": "63a05c101218d34cb54e48a5ccb2d65f016ff8b50ea938b9a4e132d008757f3d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2c823bb34ce62b61",
      "claim_ids": [
        "P-N50"
      ],
      "note": "Pressemitteilung Rheinmetall Kraken (20.04.2026) Z. 10-20 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-2c823bb34ce62b61",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/04/2026-04-20-rheinmetall-kraken-gmbh-is-launching-series-production-of-unmanned-maritime-systems-in-hamburg",
        "content_sha256": "790b7017afd03f192f63076c0c1285727499a367878c1776ebbd94e2ad79a9c7",
        "text_sha256": "6723865c23ac44126806e4b4607774a8b6e8dc394d1b3fd71f902d33bd8b4b35",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2ca5b026170c9735",
      "claim_ids": [
        "C-STR-14"
      ],
      "note": "defence-network.com 02.03.2026 Z. 31-41 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-2ca5b026170c9735",
        "url": "https://defence-network.com/9jx3",
        "content_sha256": "ac35dbc17ec147c0c2170a9c32daa66f28fa9d01a930477a9ab4f0000d2ce591",
        "text_sha256": "4f2cc5a185fe0e804ece0bfa0b2dafe6daa5e53683915c0203f8c38624e1e9f5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2dacbdde62e913a1",
      "claim_ids": [
        "M-KND-04"
      ],
      "note": "ESD-Artikel 01.09.2025 Z. 95-110 gelesen (Absätze zu KNDS-Angebot, LU211). Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-2dacbdde62e913a1",
        "url": "https://euro-sd.com/2025/09/major-news/46244/knds-france-polish-shell-plan/",
        "content_sha256": "1eab50300643657be0f0bfe55bd5eae7258207eb8467395f0d20f49ba19f054f",
        "text_sha256": "4b63676be1f89c72c1eab2cb4fe0cd1485b0a16c210796be0e41ce1f30042857",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2e979d6255b023ee",
      "claim_ids": [
        "M-NAM-06"
      ],
      "note": "Defence-Industry-Europe-Artikel 29.10.2024 Z. 17-21 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-2e979d6255b023ee",
        "url": "https://defence-industry.eu/nammo-opens-new-u-s-facility-for-155mm-artillery-components-production/",
        "content_sha256": "6ef2ca6cdb32c083354b6022efa0800e4cd04e9f597662e6f60523bbc2190d6d",
        "text_sha256": "a558776417f784f9e451c13999fdf0925c85288ca3e61143c77e5a916c6b7cd2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-30ebc6ec93f292af",
      "claim_ids": [
        "C-STR-33"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-30ebc6ec93f292af",
        "url": "https://www.intellinews.com/bulgaria-rheinmetall-to-restart-talks-on-planned-munitions-plant-456631/",
        "content_sha256": "2c44a0f7a65e099b4e70cb125ffaf88338c667adbe2758426180562526390d4f",
        "text_sha256": "176ce74eb2e766640b563ddc8cb694d98a57626820d09c194052e93b29d3e848",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-314418b5ddde95dc",
      "claim_ids": [
        "P-V21"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 4db5e8330071...",
      "snapshot": {
        "source_id": "S-314418b5ddde95dc",
        "url": "https://militarnyi.com/en/news/bundeswehr-first-puma-ifv-from-second-batch/",
        "content_sha256": "4db5e8330071f6a127e861afac31ff1d1c7e5ff0bf0d2635f5fbaeb0971a4693",
        "text_sha256": "e94ccac701fd33435ac848e4142f23a08fcd6a135835165f5fd80db3657842f7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-358fde57439e652d",
      "claim_ids": [
        "C-STR-16"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 1cfc10d7148e...",
      "snapshot": {
        "source_id": "S-358fde57439e652d",
        "url": "https://euro-sd.com/2026/06/news/industry-news/51100/rheinmetall-divests-its-civilian-division-and-focuses-on-its-defence-business/",
        "content_sha256": "1cfc10d7148e8ccf1ecb68f6a11e4a27efde44bf3f38a2016aa38676a3320307",
        "text_sha256": "ddc66b194f369c6cbc7100b05da3e0a22dd0a730cf326269cc86597abd336621",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-35e0db80122396e5",
      "claim_ids": [
        "M-RHM-01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 f709a6875f9c...",
      "snapshot": {
        "source_id": "S-35e0db80122396e5",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2022/2022-12-19_major-order-from-a-nato-customer",
        "content_sha256": "f709a6875f9cff6b13fe6dcc39409374a0ae2d762dfc396f81af98040eb66dac",
        "text_sha256": "955580892261846ed63d7ca217d21506b9ad1fa1e5415e73a4ffaf2e7ddaa8f9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-36991926ddfe11a9",
      "claim_ids": [
        "P-R96"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-36991926ddfe11a9",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-polska",
        "content_sha256": "da73bde61dd35d331028d555c79a79d8de59dc93e2db712c26d05a0f49cf23f2",
        "text_sha256": "70a2240fe369b2c996f811998e8a287aadfec4cd688d4478f006d96ee532bc0a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3828eee11ecc6273",
      "claim_ids": [
        "M-KND-03"
      ],
      "note": "Zugewiesenes Original gelesen: M-KND-03 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-3828eee11ecc6273",
        "url": "https://esut.de/2024/01/meldungen/47024/nspa-beschafft-155mm-artilleriemunition-fuer-11-milliarden-euro/",
        "content_sha256": "8ff61340f886b5fc7e56fb65bcf1c97e5d87dc4fb37fd5015278a408f1539870",
        "text_sha256": "4f93dc4abadb183ba90ced4023bd49f687a257218b7548ae3d04be963da26116",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3ab860d4e2d076b2",
      "claim_ids": [
        "T-E01"
      ],
      "note": "Zugewiesenes Original gelesen: T-E01 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-3ab860d4e2d076b2",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2025/09/2025-09-05-werkseroeffnung-in-unterluess.pdf",
        "content_sha256": "e0166a4660ffa8e646d5958c2e400d31d7b1a27dafa10f42e24fd6d6e7c0de53",
        "text_sha256": "f754cfb5a317d7d940d267dc1dc3f13f09dfb9f49a84a5df3ea98d4f6f191725",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-3b27cf3712ca73d2",
      "claim_ids": [
        "P-A14"
      ],
      "note": "Zugewiesenes Original gelesen: P-A14 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-3b27cf3712ca73d2",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-23-rheinmetall-hands-over-first-skynex-system-to-italy",
        "content_sha256": "6dbea4197385509c087cffa0b592907a1ee9d8f02778e1c3ce47e3ec94211fa0",
        "text_sha256": "4c774276e64a0a8e6bd28963eb41e972ace886a1cde7f9f37f5e3b262cc18ae6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3b33c5118cdc79d2",
      "claim_ids": [
        "C-STR-16",
        "T-02",
        "T-E16"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-3b33c5118cdc79d2",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/06/2026-06-03-verkauf-besiegelt-rheinmetall-trennt-sich-von-ziviler-sparte.pdf",
        "content_sha256": "c6d13e5f66762ec7446f9af512c82714dd3b81e3f5df0dcd8d40d187dc6a0e59",
        "text_sha256": "8ef6c0720864df93e9b4956fe205ff15cc9867e4fadcc4efab385cd6637c5c51",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-3baecfc3362bcad9",
      "claim_ids": [
        "C-STR-21",
        "P-R90"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 fdfdd501a0d7...",
      "snapshot": {
        "source_id": "S-3baecfc3362bcad9",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/11/2025-11-04-groundbreaking-ceremony-for-munitions-factory-in-lithuania",
        "content_sha256": "fdfdd501a0d7426f7450e637be54d1f79de2c2eb15dc18aa1717db76c376c235",
        "text_sha256": "343fc5c8c44996ff9075144c96ac9506666ff0de92045aefaf196136163a3dd4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3c816a672098cdd2",
      "claim_ids": [
        "C-STR-09"
      ],
      "note": "Leonardo-Pressemitteilung 15.10.2024 Z. 52-60 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-3c816a672098cdd2",
        "url": "https://www.leonardo.com/en/press-release-detail/-/detail/15-10-2024-new-player-in-european-tank-production-leonardo-and-rheinmetall-establish-joint-venture",
        "content_sha256": "73f0505888ce1a1ab70a98ce64dd18a295f4267491645bd825ce0d39e62d4222",
        "text_sha256": "e8e5d10e14b37537653b9eee89038201e74f748d442e2c7a50f81614ea9be962",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3cbff65e7dd3e5a1",
      "claim_ids": [
        "P-N20"
      ],
      "note": "Pressemitteilung 14.09.2026 Z. 9-23 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-3cbff65e7dd3e5a1",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/09/2026-09-14-federal-minister-of-defence-pistorius-charts-the-course-for-a-fourth-fleet-intelligence-vessel-at-rheinmetalls-shipyard-wolgast",
        "content_sha256": "c8607a2b5e086280e9f5b63b0c9aa2d333f79b89cfdc74d6e05be2663b0046a6",
        "text_sha256": "f9cc117a5c249be1392d1ba7d3079a2571bbcac7856f397d63a7681204256c5a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3dad8b811c925694",
      "claim_ids": [
        "C-CAP-05",
        "C-MKT-01",
        "C-MKT-05",
        "C-MKT-06",
        "C-MKT-14",
        "C-STR-02",
        "C-STR-03",
        "C-STR-12",
        "C-STR-13",
        "C-STR-14",
        "C-STR-16",
        "C-STR-17",
        "C-STR-18",
        "C-STR-31",
        "C-STR-32",
        "C-STR-38",
        "C-TEC-08",
        "T-04",
        "T-E07"
      ],
      "note": "Halbjahresbericht H1 2026 als PDF-Original seitenweise gelesen (PDF-S. 8-11, 33, 42-43)",
      "snapshot": {
        "source_id": "S-3dad8b811c925694",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2026/Q2/Rheinmetall-Halbjahresfinanzbericht-2026.pdf",
        "content_sha256": "214decfe1cd910eedff5de83482a93f410fb63d3e92a852c34d543790d07098c",
        "text_sha256": "81050c484e68e1792956cbb723d122779ed58e1fd2c8970251c3d66ccd41854a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-3f67bc2e13a1b02e",
      "claim_ids": [
        "P-W12"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-3f67bc2e13a1b02e",
        "url": "https://www.rheinmetall.com/en/media/stories/2026/rheinmetall-a-powerful-partner-at-ukraine-side",
        "content_sha256": "509b242aaf986558cddf32a337bf4d84df31ccd3d7483f1dc5bdfb53d97ada9b",
        "text_sha256": "46278e4a638f508309334a6399f6fa7d7fdc455c9899c6697bc7a838f2a34ba5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3ffdec73e87f03c2",
      "claim_ids": [
        "P-R10",
        "P-V40"
      ],
      "note": "Unternehmensseite RBSL (About us, Systems & Products) Z. 8-45 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-3ffdec73e87f03c2",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-bae-systems-land-limited",
        "content_sha256": "5e8a14368b5bf3921d6668e116af8b0649d8bc4127ec9db5ccb8d253ab154cda",
        "text_sha256": "b69c84cdb2c111228cc9b302e69a014a71404af3e50a38b948062fecc84218a1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-438937e9317397d7",
      "claim_ids": [
        "T-E11"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 b19facb72424...",
      "snapshot": {
        "source_id": "S-438937e9317397d7",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/04/2026-04-22-rheinmetall-gewinnt-grossauftrag-im-drohnenbereich",
        "content_sha256": "b19facb724249b0e85d7bf3bd3a34cc2b8941987a3a9ae3ec250c25bc5f1ba63",
        "text_sha256": "bd72e5f0c01eb0249348acf14b9743b35132e965ca7af77b3a9645923a913ddb",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-46b937ed4712bcf6",
      "claim_ids": [
        "P-A10"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 df754d05e218...",
      "snapshot": {
        "source_id": "S-46b937ed4712bcf6",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2025/12/2025-12-12-rheinmetall-to-supply-skyranger-30-for-the-dutch-armed-forces.pdf",
        "content_sha256": "df754d05e21816f1d56fd5585814b458f1cb0259c9271edabfc655174469eb53",
        "text_sha256": "8776d8dc4e43a00019e961b809690c94398834f3ec46a69e4cfa04c37f476a0a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-486bb87d545a7e5d",
      "claim_ids": [
        "M-GDO-02"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-486bb87d545a7e5d",
        "url": "https://www.gdots.com/wp-content/uploads/2026/06/400007037-155ERA-HE-Brochure-2026-06-2.pdf",
        "content_sha256": "d188ca35541698f0f554de7e3712eab5b9d23c6f010f3c46f026935605013453",
        "text_sha256": "e415e9d87cc8f979780ad7136c70073b932223d9f3fffab44ad9c4c7fd970916",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-495b6b686aece696",
      "claim_ids": [
        "P-R100"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 b8a147c27ce3...",
      "snapshot": {
        "source_id": "S-495b6b686aece696",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/american-rheinmetall",
        "content_sha256": "b8a147c27ce37e66fe8ce7c612d5aa1fffbfd594cebefa54c9d799f31f5cd618",
        "text_sha256": "18f796777319a9d030d69e0402465c83b4935e3e636aad79187145770c6fb5a9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4990a0c7872510f8",
      "claim_ids": [
        "M-HAN-04",
        "M-MKT-07"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-4990a0c7872510f8",
        "url": "https://www.army-technology.com/news/ausa-2025-hanwha-try-to-revive-munitions-production-across-the-west/",
        "content_sha256": "9bacc74ce10c99ac6126c791c0bb77a647ee6318397f2b3b9a928f9cb7c7e9fe",
        "text_sha256": "4adab09d5058df90c656ce975147dd9a43f5c80ff341bc06ae6875aa4bee9e21",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4b09bbfe7f335ab2",
      "claim_ids": [
        "C-MKT-09",
        "P-V34"
      ],
      "note": "CRS In Focus IF12094 (Stand 15.10.2026) Z. 7-45 gelesen (Drittanbieter-Kopie). Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-4b09bbfe7f335ab2",
        "url": "https://www.everycrsreport.com/files/2026-10-15_IF12094_54ac7be20cc6496ce7659b2d40028d56ae7277bd.html",
        "content_sha256": "ed3dd1b8834cddcb3276fc9fcd800c95be8d95d0893bb83908f83024f2e1b75d",
        "text_sha256": "91d71cdb9ea09d769d7a72c7fa6e253254b19221e598f3708eb7f497c0bfb377",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4c4ea5a84abeab0f",
      "claim_ids": [
        "M-GDO-04"
      ],
      "note": "GD-OTS-Meldung 29.05.2024 Z. 48-53 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-4c4ea5a84abeab0f",
        "url": "https://www.gdots.com/new-artillery-projectile-metal-parts-facility-in-mesquite/",
        "content_sha256": "e13e390218cd12e4d45b16036df71a8ede059444f2f3d97e96be4678fd2d6dad",
        "text_sha256": "986f02542b78509d0793ce243a5a19df454ceffc77b9a7864dbcdaef29910439",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4c90fb7e038d3c0e",
      "claim_ids": [
        "C-STR-13"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 222a27043c1f...",
      "snapshot": {
        "source_id": "S-4c90fb7e038d3c0e",
        "url": "https://www.navalnews.com/naval-news/2026/04/rheinmetall-kraken-gmbh-launches-series-production-of-usv-in-hamburg/",
        "content_sha256": "222a27043c1facb82338153dbcb5d0dd8926614e38aaa8cdf6478e66355da642",
        "text_sha256": "749b28fe04313b44911c4074883a458653a95166953a1bdc070918c60a517a77",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4f9807383dbfe574",
      "claim_ids": [
        "P-R110"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 19edc4ae0263...",
      "snapshot": {
        "source_id": "S-4f9807383dbfe574",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-canada/ueber-uns",
        "content_sha256": "19edc4ae0263b4366970a282516b56135f112f8af25f67f3b1ab351e2d5d1b96",
        "text_sha256": "c31572edc271f13a5a719734d1a86d9c513c27fb101919e357413281fc1cc6b1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5366eb8816ff2cea",
      "claim_ids": [
        "P-D14"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-5366eb8816ff2cea",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/06/2025-06-18-strategic-partnership",
        "content_sha256": "b22e2acf0c994b991323a599e765772f1a640d5fd3bc5fe09cc612661566a3eb",
        "text_sha256": "bfe48629645a8f70e55a9612f769c20db149191035ec06cf82090ca3bceb5daa",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-544652c53afaff87",
      "claim_ids": [
        "M-RHM-02"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-544652c53afaff87",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2019/2019-11-27_rheinmetall-sets-three-new-distance-records-for-indirect-fire-in-south-africa",
        "content_sha256": "28f20f60acbf6fb31052bf1720e18a77cb418905cc9207ea7fdf506b1736ee3a",
        "text_sha256": "67e262f029af343468d97d28e2b7469a3e034e52af2a483913f7e667dd16a6bd",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-553789c22ec26699",
      "claim_ids": [
        "P-W21",
        "T-E06"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-553789c22ec26699",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/01/2026-01-05-rheinmetall-receives-major-order-from-the-bundeswehr-for-puma-ammunition",
        "content_sha256": "8892c74c14a6ed54776aa7cbf8240a13677be0d1f1a453e9d0730a03b69e844b",
        "text_sha256": "34a6b7e58be6c67668b2d9985fbc07a58825511d798a7a9475139823727a2855",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5590349d6f29de4e",
      "claim_ids": [
        "M-GDO-05"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 c0ad780b9ac7...",
      "snapshot": {
        "source_id": "S-5590349d6f29de4e",
        "url": "https://taskandpurpose.com/news/texas-ammo-factory-zero-shells/",
        "content_sha256": "c0ad780b9ac7037ad44f4ed194ffa8facaf7aae071136d8ca8d09def88d6181b",
        "text_sha256": "5205f4fdd3613752cdb040828b7e1de21a4e07a7acaca76c84ad0791b3d6531d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-559e0ac19cabd1d0",
      "claim_ids": [
        "P-D12",
        "P-S01",
        "P-S03",
        "P-V16",
        "P-W51",
        "T-04",
        "T-10",
        "T-11",
        "T-15",
        "T-E08"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-559e0ac19cabd1d0",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/03/2026-03-11-rheinmetall-presents-annual-report-for-2025",
        "content_sha256": "7e3db873b5df5a92827fec19729e7d2b5b0ac6eaec22c17ed9f20b8d73a96cef",
        "text_sha256": "0ec37d2f55de8a9c547cf2dbfe1bb4a5b1290a5df49008ff8ba84dc96ea5114f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-56fc0186af26e860",
      "claim_ids": [
        "T-E13"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-56fc0186af26e860",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/05/2026-05-28-rheinmetall-issues-a-500-million-bond",
        "content_sha256": "06e96c9385f55b4e9a0229ec8b1ae99c24ccd4ab60e33369301259a8a6c65d50",
        "text_sha256": "7558cc81b8a004c5bfc0565fb9cf2e3b1ab114d3a7cacf5eb1f140ac15cdc73e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-57b3617f24a7d47b",
      "claim_ids": [
        "P-N01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 23f58991e4af...",
      "snapshot": {
        "source_id": "S-57b3617f24a7d47b",
        "url": "https://www.rheinmetall.com/en/company/divisions/naval-systems",
        "content_sha256": "23f58991e4af7a009eaf592325cac54f89213bffa35701d96d6c2a67de4ecedb",
        "text_sha256": "7a76ac7b3ac9e049e67c80e38d61f9e478b071c98fdaf1e877b01855cc9c9cd7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5b640196f4e87dad",
      "claim_ids": [
        "C-MKT-06",
        "C-MKT-10",
        "C-MKT-11",
        "C-MKT-15",
        "H-M05",
        "T-04",
        "T-05",
        "T-06",
        "T-07",
        "T-08",
        "T-09",
        "T-13",
        "T-14",
        "T-16",
        "T-E17",
        "T-E20"
      ],
      "note": "Rheinmetall-Pressemitteilung Halbjahresfinanzbericht 06.08.2026 (HTML) Z. 8-70 vollständig gelesen: Keyfacts, Konzern, alle fünf Segmente, Ausblick. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-5b640196f4e87dad",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/08/2026-08-06-rheinmetall-pressemitteilung-halbjahresfinanzbericht-h1",
        "content_sha256": "cf8878be08ef2530410ffc52aed9b3ae41a31f8b487ab9dee22eb4652d56eab7",
        "text_sha256": "9129f4bb5b65c304529a6064915b400b92c78372f8e3e4e97ec81141f1719ad5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5d054e98a93f597d",
      "claim_ids": [
        "M-HAN-03"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-5d054e98a93f597d",
        "url": "https://www.koreatimes.co.kr/business/companies/20251015/hanwha-aerospace-signs-110-mil-deal-with-sweden-to-supply-modular-charge-system",
        "content_sha256": "750733f0afee541bff8cd65a4c5d7cc89f688a6b94ae3eb78714435f3e85374f",
        "text_sha256": "a757aa1f33649a3b16c45313a59da944f3a9551efda67ef0ef8850b1b017a293",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5f102cfea2da2738",
      "claim_ids": [
        "P-A02",
        "P-D02",
        "P-N02",
        "P-N03",
        "P-N60",
        "P-S01",
        "P-S04",
        "P-S05",
        "P-V02",
        "P-W02"
      ],
      "note": "PDF-Fassung der Halbjahres-Pressemitteilung 06.08.2026: Seite 1 und Segmentabschnitte (Seiten 2-5) gelesen; Zahlen gegen Zeilenstellen abgeglichen; Inhalt deckt sich mit HTML-Fassung. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-5f102cfea2da2738",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/08/2026-08-06-Rheinmetall-Pressemitteilung-Halbjahresfinanzbericht-H1.pdf",
        "content_sha256": "70b17f8f578df934e3a6d2bf8631acf980f14b940352268a45f613d3e8ca2113",
        "text_sha256": "81f60aad3132af7b7cc2c7410dd2b91067f0d26ddf9a6a8c5a08aeb2ba272438",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-60aeccc43d93c8df",
      "claim_ids": [
        "P-A30",
        "P-C03"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 791b61076e7d...",
      "snapshot": {
        "source_id": "S-60aeccc43d93c8df",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-italia",
        "content_sha256": "791b61076e7d04da582a9982709ea9862d6e33f32c3c765588bcdc535d7ab093",
        "text_sha256": "d6a154997a56380e11dd3a11928a748834fa7b26bc77a54375f14161bc9637c4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-645fb750545d0e57",
      "claim_ids": [
        "P-R40"
      ],
      "note": "Zugewiesenes Original gelesen: P-R40 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-645fb750545d0e57",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-expal-munitions",
        "content_sha256": "8444256be03e06e77260348a2ab42de4b46a18d4446b315ba36214031f308e3c",
        "text_sha256": "cce91b2718727a8c62576cb9b64139dfbabb83da7cc958258056465bc52c7301",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-64b8fa1a98bafd6e",
      "claim_ids": [
        "C-STR-28"
      ],
      "note": "4iG-Pressemitteilung Budapest 25.11.2021 Z. 143-216 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-64b8fa1a98bafd6e",
        "url": "https://4ig.hu/rheinmetall-to-become-a-strategic-investor-in-4ig-",
        "content_sha256": "96cb4da7e90283849e0bdf2f20447acdbed3511fbac6d3431648dd5c7b5983d1",
        "text_sha256": "04ca25b74da9027d6b3027eb6514073487b264c28dae3f315d91f0bdee4a3c1a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-65384ba645706eba",
      "claim_ids": [
        "H-M07",
        "P-W13",
        "P-W20",
        "T-E26"
      ],
      "note": "Pressemitteilung Albacete (16.10.2026) Z. 9-32 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-65384ba645706eba",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-16-rheinmetall-opens-modern-medium-calibre-production-facility-in-albacete",
        "content_sha256": "f11973824a31b4e37429ffc9a4988019dd6a43f8cbd812df502f03b7bd664bc9",
        "text_sha256": "0bb784453190868474056de68147d56f669bda048e2b4af64e6b21fdbada8dd2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-66c989d68bed493a",
      "claim_ids": [
        "M-GDO-02"
      ],
      "note": "Zugewiesenes Original gelesen: M-GDO-02 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-66c989d68bed493a",
        "url": "https://www.gdots.com/wp-content/uploads/2026/06/400007048-M1128-I-Product-Brochure-2026-06.pdf",
        "content_sha256": "b7a943273c78ba3e48970dbc4e4b8adc10003905b340dceaa64e0382ec08bab6",
        "text_sha256": "fad9b069e1c5faa5a1cd97eec7960e61c908229e185608ef1c15e84826beba32",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-6724ed6c8698ea5b",
      "claim_ids": [
        "P-A13",
        "P-D40",
        "P-N60",
        "P-N61",
        "P-R03",
        "P-R160",
        "P-V17",
        "P-V41",
        "P-W31",
        "P-W60"
      ],
      "note": "Investorenpräsentation September 2026 (PDF): Folien 8, 23, 27, 30, 35-36, 39, 41-42, 47-50, 57-58 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-6724ed6c8698ea5b",
        "url": "https://ir.rheinmetall.com/media/document/665a6b2c-002f-4a04-b53d-ec42608b83a7/assets/Rheinmetall_AG_2026_Investor_Presentation_September.pdf",
        "content_sha256": "24eb1efde161bb5cdaa637eb444a3bb9dae4c14e94535b0a4b40281b8ff76202",
        "text_sha256": "0c1fb589050b8edc19765a2565579fa99fec495fbc7ddde3267df72e8f2844a2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-6797a3b3e68d3be1",
      "claim_ids": [
        "P-R100",
        "P-V35",
        "P-V50",
        "P-V70"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-6797a3b3e68d3be1",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-12-american-rheinmetall-at-ausa-2026",
        "content_sha256": "1903aa8a83bc28a579bb61fa30dd31357565c13e0139d0d7ae6fc5604faf42c8",
        "text_sha256": "1a0afcea1fa00f5b7ab6d4130933707c248d81548e6ca55116f6bd58f8cf1753",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-69f3ca71ad940e6e",
      "claim_ids": [
        "M-HAN-01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 76c13b346b64...",
      "snapshot": {
        "source_id": "S-69f3ca71ad940e6e",
        "url": "https://breakingdefense.com/2025/12/hanwha-plans-to-build-us-facility-to-manufacture-modular-155mm-howitzer-charges/",
        "content_sha256": "76c13b346b6486d7f9213a4bd26a3d9cf65a12e077f43f892a2c070c77031ba3",
        "text_sha256": "9a697557000fa188f8376791a783e8fdc7875dac3d2cbd9424ca91df66799d80",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6bdb338d23c29e11",
      "claim_ids": [
        "P-A12"
      ],
      "note": "Zugewiesenes Original gelesen: P-A12 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-6bdb338d23c29e11",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-24-romania-orders-skyranger-35-air-defence-systems-from-rheinmetall",
        "content_sha256": "b2bf12e5632c444d2b969bd7099a1b27f83149504fc5a36554050ff5007cf6e2",
        "text_sha256": "841e2df5713cce7f7fe28a88b426179daa60c44193b3ce90a375c63fa228fd34",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6c35892360c66d5a",
      "claim_ids": [
        "M-BAE-03"
      ],
      "note": "Defense-News-Artikel 11.07.2023 Z. 50-72 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-6c35892360c66d5a",
        "url": "https://www.defensenews.com/industry/2023/07/11/bae-systems-wins-order-for-munitions-as-uk-rebuilds-stocks/",
        "content_sha256": "37bb288fc429ac0b8f20367d900879d6f8a5cb2c15febdbba9f73485946d8d60",
        "text_sha256": "60146f2b29fbabb9ca5c60ac752af6dd218e18d534257310eac1957ecb0c5640",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6c84242ff77b4c1c",
      "claim_ids": [
        "M-KND-08"
      ],
      "note": "EDR-Artikel 04.11.2025 Z. 41-46 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-6c84242ff77b4c1c",
        "url": "https://www.edrmagazine.eu/inauguration-of-a-new-155-mm-artillery-shell-production-unit-at-knds-belgium-a-major-strengthening-of-belgian-and-european-industrial-capacity",
        "content_sha256": "bf6bb7af06302e7666de4ca9be743083d7e5a3528fa217cd624bbbfbf9c55eba",
        "text_sha256": "4a02ccd1420aa793539a51c55feb1d61f27a9826c2ce8bb6588991a39b9b1e34",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6d2c1c75db9e7ad4",
      "claim_ids": [
        "P-C03",
        "P-R130",
        "P-V72"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-6d2c1c75db9e7ad4",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-singapore",
        "content_sha256": "20c5b6f5340a07023d8a582ec7d264711a4c5f489ee7f14514473d8e8789dde4",
        "text_sha256": "a90dd70869c6cf523f041de12bd6892653cc245ec8b07a7f309ce7a7f6ef5275",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6dec578278539c53",
      "claim_ids": [
        "M-NAM-01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 b0899eb70099...",
      "snapshot": {
        "source_id": "S-6dec578278539c53",
        "url": "https://www.nammo.com/products/ammunition/large-caliber-ammunition/155-mm-series/",
        "content_sha256": "b0899eb7009955fc919388759a3c653883260262efb39781cbfab2c7a9c7401a",
        "text_sha256": "ae3d683e679daf39bcf0e58969b4dfba159f35b3827e33e07fe188267f323a9d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6e6c0340ee9c8a72",
      "claim_ids": [
        "P-W33"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 935b5fab413d...",
      "snapshot": {
        "source_id": "S-6e6c0340ee9c8a72",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/09/2026-09-30-american-rheinmetall-supplies-mk93-mounts-to-the-us-army",
        "content_sha256": "935b5fab413d3b7170cc101d0b3cc65f4228c2fb34677c9e51c5f4f3c9605ff3",
        "text_sha256": "83f69adfe643c56cd1572d8c6041d95eb2998d3f1ae383f8a923abbf33425746",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-700febb47c6229bf",
      "claim_ids": [
        "P-D60"
      ],
      "note": "Zugewiesenes Original gelesen: P-D60 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-700febb47c6229bf",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/01/2026-01-09-new-agsp-simulators-for-the-puma-infantry-fighting-vehicle",
        "content_sha256": "d2adf82135a28ad117cab64774973e3a943629b3146aeba85f169e13189d9133",
        "text_sha256": "2820e21069de173a352a74c5c67ee5f731259f5d6b349af91e7fcedfe8813045",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-71883fd06cc70f3c",
      "claim_ids": [
        "P-C01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 f16c29b73b68...",
      "snapshot": {
        "source_id": "S-71883fd06cc70f3c",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/06/2026-06-03-deal-finalised-rheinmetall-divests-its-civilian-division.pdf",
        "content_sha256": "f16c29b73b688c29c2532b02a3fe1eb4ee8d5a823d4785fb9d9f406fc9ef5a19",
        "text_sha256": "1bf902e2c76dae35520e090b8ca0a2868aa8161c37a5a69593babd743d078798",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-71e68b86d52a8a03",
      "claim_ids": [
        "M-RHM-04"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 ef98e72d3d74...",
      "snapshot": {
        "source_id": "S-71e68b86d52a8a03",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/11/2025-11-03-rheinmetall-and-romania-jointly-produce-propellant-powder",
        "content_sha256": "ef98e72d3d74b864d87d1d16d3a375cc5f50d7c9f85d467c628c9a4f3923914e",
        "text_sha256": "3e760f3e56c710340a37ec5eb74f3dfc21817cc968dfdfc9dac71baecad8ccf3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-71f7b9c8df6bf2dd",
      "claim_ids": [
        "P-C03",
        "P-R02",
        "P-R150"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 e9f4f0f038dd...",
      "snapshot": {
        "source_id": "S-71f7b9c8df6bf2dd",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/nvl-b-v-co-kg",
        "content_sha256": "e9f4f0f038dd25b4f335f5141c2d8c2ca95dbe006e32ee44586cf089001b7881",
        "text_sha256": "95cead0b65cd4a56bbd29232fe7814646ebcb51348b42fd1ca2177ee90ef7369",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7211720721aa7d4b",
      "claim_ids": [
        "P-W40"
      ],
      "note": "Pressemitteilung Aschau 23.07.2026 Z. 9-30 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-7211720721aa7d4b",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-23-rheinmetall-foundation-laying-ceremony-aschau-powder-plant",
        "content_sha256": "66007149e9035397133d1c0a55a09063caa3ba5538616c6314e1ae097dc98667",
        "text_sha256": "28371a25bd4fb4c9620940452ebc5e52b1fee7bd06706eaf74afaedf50bf8ee1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-726b04b00a65e55c",
      "claim_ids": [
        "C-STR-05"
      ],
      "note": "TRATON-Geschäftsbericht 2025 (Kopie im Lobbyregister, Cache-Text): Konzernanhang PDF-S. 192 gelesen; übrige Teile nicht geprüft. Snapshot http-original, content_sha256 496284ea9847...",
      "snapshot": {
        "source_id": "S-726b04b00a65e55c",
        "url": "https://www.lobbyregister.bundestag.de/media/35/ec/785097/Traton_Geschaeftsbericht_2025.pdf",
        "content_sha256": "496284ea9847425fc717b2c36efaa8c2e1db112b75fb17813de40a717448dd20",
        "text_sha256": "9de3a8bba1636b6660368b8a3953494ffcef839cbfbaf39b9aa247baefe4b19f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-73cf7c9497cad059",
      "claim_ids": [
        "P-W30"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-73cf7c9497cad059",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-waffe-munition",
        "content_sha256": "41d8972594fa0fd5aea5c3476360395bae6da51647fb991640001c659b0ead93",
        "text_sha256": "6df3a31ca99e66393ac3f6da3ca48f2cf72cafcadb67cd8299ed94c8dd7ffd81",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-749ebb1bb3cf3947",
      "claim_ids": [
        "T-E18"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-749ebb1bb3cf3947",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/07/2026-07-01-rheinmetall-uebernimmt-mehrheitsbeteiligung-an-dok-ing",
        "content_sha256": "21ba33ff8836401b85ff15dab979302522ef9bbc3edd890604cd1d99bbd9c263",
        "text_sha256": "2490e2e5390d0e01ffc37f5470744fa33abdfeb040a28e3e16131026fa2baefc",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-75731f2457a30bcf",
      "claim_ids": [
        "C-MKT-06"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-75731f2457a30bcf",
        "url": "https://soldiersystems.net/2026/06/04/major-historic-international-contract-for-rheinmetall-romania-orders-lynx-combat-vehicles-vessels-and-air-defence-systems-worth-a-total-of-e5-7-billion/",
        "content_sha256": "c743d16c4dccbdf0c292c6e071f9a8ce7010bc3641e6962239add85ba54e0467",
        "text_sha256": "28fde4adcceb14bd764023456a6a762468da9144e9b0484b3bd7b48594eb2caf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7a7a5f5d433c1776",
      "claim_ids": [
        "C-MKT-02",
        "P-V10"
      ],
      "note": "Pressemitteilung Schakal (20.10.2025) Z. 10-21 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-7a7a5f5d433c1776",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/10/2025-10-20-infantry-fighting-vehicle-222-jackals-schakal-for-germany-and-the-netherlands",
        "content_sha256": "8b6b12945cda5b45b5a1800c70b7a903b8854d198fe818e1720f4f94eeed10a0",
        "text_sha256": "2b2ca582b0d44224894941c9593792b6299a3ad7a93f4faac2c799449ff7b71d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7c51e921c055e64c",
      "claim_ids": [
        "T-E15"
      ],
      "note": "Zugewiesenes Original gelesen: T-E15 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-7c51e921c055e64c",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/06/2026-06-02-major-historic-contract-in-romania-worth-5-7-billion.pdf",
        "content_sha256": "b0c2d8a8d402b8eef3d210ed419fa3ec8d46484889ac5b4736b1f2299f49caa1",
        "text_sha256": "4c06d68fa186c6616f4c811222103ce752aa18695bc0a8c92a07c5b6ad5b171a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-7f0bea0216cf289e",
      "claim_ids": [
        "P-R150"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-7f0bea0216cf289e",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/nvl/international-operations",
        "content_sha256": "7f07f6577f041ce8e7ef84cd57cedd26803b331772e334c0d975947965216ecd",
        "text_sha256": "22472f27ab17bb625dec7a47277edc1f566714d1832617bea7078b6e44a034e4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7f6de13c77cb340f",
      "claim_ids": [
        "T-E23"
      ],
      "note": "Zugewiesenes Original gelesen: T-E23 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-7f6de13c77cb340f",
        "url": "https://www.hessenschau.de/wirtschaft/rheinmetall-uebernimmt-lok-werk-von-alstom-in-kassel-v1,alstom-rheinmetall-100.html",
        "content_sha256": "e32e32f6337a183d53a526cc2d6476dd27c594833704aac399179f6e4978acca",
        "text_sha256": "bf60cffaa94afbd5be0f6548d6ef3a15dba7d21ad249c8230c28373658ff88fd",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-818ac8c5a1a773b5",
      "claim_ids": [
        "P-N40"
      ],
      "note": "Pressemitteilung 23.09.2026 Z. 9-23 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-818ac8c5a1a773b5",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/09/2026-09-23-rheinmetall-awarded-maintenance-contract-for-customs-vessels",
        "content_sha256": "15b3ca9b484073e3b801199e48d261ae0c5890f2129e79075e6f662941e984dc",
        "text_sha256": "1f6aa814d5bfa3fb7b6cbcc4d59bce7f77e35db9828f443568029c44e2011b85",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-81a27e8c4bbffb44",
      "claim_ids": [
        "P-V71"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-81a27e8c4bbffb44",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/05/2026-05-26-rheinmetall-at-cansec.pdf",
        "content_sha256": "81fa09a4ae6c2541157ce9735cd9179533e8be4ca07f1339fce95a926fdf28fd",
        "text_sha256": "1ccbae0d1f403b6e4abbb6bc592a99ec6d2caa019b8c05f842076c7184dd9969",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-823a7eb256c6141a",
      "claim_ids": [
        "C-TEC-07"
      ],
      "note": "Zugewiesenes Original gelesen: C-TEC-07 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-823a7eb256c6141a",
        "url": "https://esut.de/2024/01/meldungen/47058/luftverteidigungssystem-nah-und-naechstbereichsschutz-wird-entwickelt/",
        "content_sha256": "6f3a10eea0a916ed05a78832495d853b96aa8bbb79c973b3b929e921f860909b",
        "text_sha256": "63451853e6845e2e8facd9799e6aa29f547bd7431837a0cc97193a771a9390be",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-84620b98214b90e5",
      "claim_ids": [
        "M-MKT-02"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 4a2a0040fc60...",
      "snapshot": {
        "source_id": "S-84620b98214b90e5",
        "url": "https://www.eurointegration.com.ua/eng/news/2024/03/15/7181800/",
        "content_sha256": "4a2a0040fc603f819cecf7bfced2c22b9008fbc782cdff2d1ed9bb22050fc740",
        "text_sha256": "860118cee234ede10a38e7c1a33bd278a7ff988839aafbe1670ad9b3a084df59",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8570241741649c2a",
      "claim_ids": [
        "C-MKT-03",
        "P-D11"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 e658d51b4954...",
      "snapshot": {
        "source_id": "S-8570241741649c2a",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/04/2026-04-27-bundeswehr-orders-idz-es-soldier-systems-from-rheinmetall",
        "content_sha256": "e658d51b4954fca8abf9ce1bba5a8d7bcd397d32381336573a574ba93bf34511",
        "text_sha256": "91f9db208e7ef4a605cff5f2079e68c51f015167e57a4ca7cc930a728686aa64",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-862e33c032d029f6",
      "claim_ids": [
        "C-MKT-08"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-862e33c032d029f6",
        "url": "https://www.gov.uk/government/news/british-army-to-possess-most-lethal-tank-in-europe",
        "content_sha256": "15f1773d496f038141cac71505501d734f231886edb135b6e4e6f5e797c933e7",
        "text_sha256": "d12f51d40c3694ea11f47391af7cc8dcd011f3e2e11f2a0aa0b5cdb14cc77ccb",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-86b532adf4a3d541",
      "claim_ids": [
        "C-STR-15"
      ],
      "note": "Zugewiesenes Original gelesen: C-STR-15 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-86b532adf4a3d541",
        "url": "https://en.lider.media/2025/09/18/lurssen-group-confirms-sale-of-nvl-to-rheinmetall",
        "content_sha256": "3328c6162f698fed1c49c0b79755eed0964adb009ad7b993bc08d332aac18fb3",
        "text_sha256": "95c765b1bc39fd1af8a2323c6d5ce57330011af7f0cd0c5ee47a1c0c493e5086",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-89bc6e8457e5ef24",
      "claim_ids": [
        "P-R95"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 67d617bad347...",
      "snapshot": {
        "source_id": "S-89bc6e8457e5ef24",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/09/2025-09-25-lettland-bestellt-munitionsfabrik-von-rheinmetall",
        "content_sha256": "67d617bad347a5430d0b8ba18180897fd3672c52819b0bac1b592e75dacfbb1f",
        "text_sha256": "49843dfb40a46a6ba93bc558e823300b9bd2510546ff934a832c28bad0683854",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-89c6e4ce6f0b8dab",
      "claim_ids": [
        "M-GDO-01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 1d0099044389...",
      "snapshot": {
        "source_id": "S-89c6e4ce6f0b8dab",
        "url": "https://www.gdots.com/munitions/artillery/",
        "content_sha256": "1d0099044389a72d9e2ae329ba4c23587796e12087e134ab5492c158f707056a",
        "text_sha256": "ac46c4b30ac2b7442f8e1da297830969a0821d89c12a6c251d49c534dc7738bf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8b46f20a7a35fb19",
      "claim_ids": [
        "M-NAM-08"
      ],
      "note": "Zugewiesenes Original gelesen: M-NAM-08 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-8b46f20a7a35fb19",
        "url": "https://www.nammo.com/locations/raufoss/",
        "content_sha256": "75c7d560cf515d002ce654443e87154d34ec051edc61308321ff5a6738ae3923",
        "text_sha256": "e397d85a6cc2f4e9e6e22bea1dc186bff7539e0312c3bc6c159f92f7183edd35",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8d249b1db35129b2",
      "claim_ids": [
        "C-TEC-02"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-8d249b1db35129b2",
        "url": "https://euro-sd.com/2023/07/news/32688/rheinmetall-announces-it-will-produce-f-35-fuselage-sections-at-weeze/",
        "content_sha256": "b01c199e8ce2f6ca641e56f0ca07b50bd50ae6a4fd089d11211fc63cd534bcae",
        "text_sha256": "d9a3c40cc7b4e342b0bf74abe5d3564890785314d1c8f4e7201447b0d8998100",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8f1fd53628424ca7",
      "claim_ids": [
        "P-A11",
        "P-V12"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-8f1fd53628424ca7",
        "url": "https://defence-blog.com/bundeswehr-faults-rheinmetall-on-two-key-weapons-programs/",
        "content_sha256": "5f9c44b997a256d86e3af0706fa8e1ac6bc491f71dfe1174f14fac2caac17044",
        "text_sha256": "83960ec896463063e00fad1439600963744597c2f70cc8b3c9f3f5ce32f1f961",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8f63be7e3308f827",
      "claim_ids": [
        "T-E14"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-8f63be7e3308f827",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/05/2026-05-28-rheinmetall-liefert-mehr-als-2-000-utf-lkw-an-die-bundeswehr",
        "content_sha256": "32077c14b93a7ff8e5a196e9481de088aac245ae9880248e495fdf02428bb456",
        "text_sha256": "7123f2cefbd8ac392188c79b9523e6955f728d5729870ec9050edc5ba4d48440",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-91be1f9c04508de5",
      "claim_ids": [
        "C-STR-37",
        "P-N31",
        "T-E27"
      ],
      "note": "Rheinmetall-Pressemitteilung Mangalia 19.10.2026 Z. 9-22 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-91be1f9c04508de5",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-19-rheinmetall-acquires-the-mangalia-shipyard-in-romania",
        "content_sha256": "bc8a5ae658973e3e9f34944603ab4d874adb61bb3dff00fb1c1297e67207623d",
        "text_sha256": "7d91070071c0e8757694c37e4a8f59a21bd594ea4fd86f584ed048606398f169",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-91c7451596d6b416",
      "claim_ids": [
        "P-A40",
        "P-R30"
      ],
      "note": "Zugewiesenes Original gelesen: P-A40, P-R30 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-91c7451596d6b416",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-air-defence",
        "content_sha256": "d4b187e9e45eecc0195cfa5b6abce3967dc9db7dc4b4267e32d43f4ae2e7e2e7",
        "text_sha256": "df9ae39591d58fd87b4a799624ba4685238a83f9de335469105ec17348580b71",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-943f5a439ab01032",
      "claim_ids": [
        "P-V14"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-943f5a439ab01032",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-31-rheinmetall-delivers-weapon-systems-for-british-rch-155-wheeled-howitzer",
        "content_sha256": "f387fba96a250a43034ec8e93f56d9dfcc9bde6485df16613f0f81dabcb054be",
        "text_sha256": "ca96683b0580cdef49397a2b52ab91df819d22c3e08ad6f24eb7d68a5f550967",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-9779449a4b003eae",
      "claim_ids": [
        "P-W01",
        "P-W41",
        "P-W50"
      ],
      "note": "Divisionsseite Weapon and Ammunition Z. 8-48 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-9779449a4b003eae",
        "url": "https://www.rheinmetall.com/en/company/divisions/weapon-and-ammunition",
        "content_sha256": "212f01959064b7a8771babe7ffb315cb5f6503d1d456f523aa8868aa9cf214e3",
        "text_sha256": "2e1a012505625cb7d22dc5302588146053c5b47637981f6f74d04e0fefcf2318",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-97aa5b20a4a51ea0",
      "claim_ids": [
        "M-NAM-07",
        "M-NAM-08"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-97aa5b20a4a51ea0",
        "url": "https://www.nammo.com/about-us/locations/",
        "content_sha256": "949ab435530de75ef1dbc762eb66112fb895871a23b47b39ff9b36f7e6723ce0",
        "text_sha256": "0ee66b7ee7c67637bb076fc2410cab776107ac1ea0417b9f3fbc2d383db345a1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-98082c5c6a5443c4",
      "claim_ids": [
        "T-01",
        "T-03"
      ],
      "note": "Rheinmetall-Startseite gelesen; Kennzahlenleiste zusätzlich im Original-HTML (source.bin, eingebetteter Datensatz) geprüft.",
      "snapshot": {
        "source_id": "S-98082c5c6a5443c4",
        "url": "https://www.rheinmetall.com",
        "content_sha256": "fdcc11200a1b74249427219fb0f718524801927d7bd26d46c623a3440f880ee4",
        "text_sha256": "c34340b18d439f875bd3736348fdaf005efcaa63d8fb2e302c2a593f841a4f57",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-9ae1f8e16f1f1d76",
      "claim_ids": [
        "M-RHM-06"
      ],
      "note": "Zugewiesenes Original gelesen: M-RHM-06 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-9ae1f8e16f1f1d76",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/06/2026-06-30-grossauftrag-rheinmetall-liefert-artilleriemunition-an-ukraine",
        "content_sha256": "6fe7d51fa5a785908fb9c26cb700235ec44698297de68a62547a0170f09e6484",
        "text_sha256": "97c43583f99c82510cf426b24227cd04a8bb3471b470ae4eddf850fc8e4e095c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-9dbd280720401c1f",
      "claim_ids": [
        "M-KND-05"
      ],
      "note": "Bankier.pl/PAP-Meldung 18.06.2026 Z. 177-187 vollständig gelesen (Polnisch). Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-9dbd280720401c1f",
        "url": "https://www.bankier.pl/wiadomosc/Niewiadow-PGM-ma-umowe-o-strategicznej-wspolpracy-z-KNDS-9153641.html",
        "content_sha256": "3d3f4c9315781c6533a4ebada7a7435b701c00cc24238124df3a087a410a6ee1",
        "text_sha256": "5b725724f5af1b0c886655ffe8cdb501ad0b29cd1a1acfff1d02648b1248d94a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a0a52d4597ffc995",
      "claim_ids": [
        "P-R98",
        "P-V72"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-a0a52d4597ffc995",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-ukrainian-defense-industry",
        "content_sha256": "4f98929c0e1fbc0bbcca8f3e7f476be618df0eefb34dd75c7ddb338dd6b32db3",
        "text_sha256": "bdb730930999b2465561082961d236cb9abf6ba7d86b86e96b1c761e7cf2db3e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a103a3f44e96a221",
      "claim_ids": [
        "C-STR-12"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 c2e769eee5f6...",
      "snapshot": {
        "source_id": "S-a103a3f44e96a221",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/06/2026-06-11-ohb-and-rheinmetall-establish-joint-venture-ohb-rheinmetall-space-networks-gmbh.pdf",
        "content_sha256": "c2e769eee5f620c6708faae4a3dafb990b0ecab058f29f3de89f611faaeedbea",
        "text_sha256": "39c889998ce50e6091f1e139e2f1760b9b3a1fd64efeaacd4c4b7f5a1fcbc598",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-a3892fe72afc70a4",
      "claim_ids": [
        "T-E10"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 70badfa2231c...",
      "snapshot": {
        "source_id": "S-a3892fe72afc70a4",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/04/2026-04-13-rheinmetall-und-destinus-gruenden-joint-venture-fuer-raketensysteme",
        "content_sha256": "70badfa2231cef6e2004de66ccc343ffa193d3266a0d140adf97234f8fd34c7c",
        "text_sha256": "6dbba273e41132b208afd719147486eda8764f9729c84da2fb9547c705ce8cdf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a412156de9747510",
      "claim_ids": [
        "P-V33"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-a412156de9747510",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/01/2026-01-12-rheinmetall-supplies-lynx-to-ukraine",
        "content_sha256": "8a6542ac10bfd7b3af779abbf6cc11cf5102954f445a3556b100cfd20f1eb7e4",
        "text_sha256": "abb6e18fe37ab1ce8425f27b478c3df20b7d975fffd8706374f7c690b5fe0aa8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a4432a86aaf146f5",
      "claim_ids": [
        "M-MKT-01"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-a4432a86aaf146f5",
        "url": "https://defence-industry-space.ec.europa.eu/eu-defence-industry/asap-boosting-defence-production_en",
        "content_sha256": "f707d54596cab7cdc7ad71e3df53cb482a1e3842bbe96c6b41dc4f12e7f3fa17",
        "text_sha256": "7b3d7ecb2ba6405bff31123b84c91f38235aa3a92cfad662620eedd0ddae0c1e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a54a5988eef2046e",
      "claim_ids": [
        "M-NAM-03"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 59274400d422...",
      "snapshot": {
        "source_id": "S-a54a5988eef2046e",
        "url": "https://www.nammo.com/norwegian-artillery-contract-signed/",
        "content_sha256": "59274400d422908b34a56985f43ded21db04a148e2bf2ec55018562f7f709023",
        "text_sha256": "a364f375a7a0780a7308c8ea0e62bd84bc6d20deeb5482b053cbc5b812f8bb21",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a5a55ae4e279062f",
      "claim_ids": [
        "M-KND-04"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-a5a55ae4e279062f",
        "url": "https://knds.com/en/press-releases/up-to-200-000-shells-per-year-a-new-ambition-for-the-polish-defence-industry",
        "content_sha256": "fae6ad97ac99721e1dd14c5e5a59cee62d372efbf3aaee2c1403b7bdb9e39ae7",
        "text_sha256": "9b02ccad57cc6aced165a6ba3254a2cab961964634e572f57c5d2a8201d9143c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a6309db699669326",
      "claim_ids": [
        "T-20",
        "T-E29"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-a6309db699669326",
        "url": "https://www.rheinmetall.com/en/investor-relations/calendar-and-events/capital-markets-day",
        "content_sha256": "87997daa2ae1523a98b291dc8afd9b27e23e6f8742471377e7ee0db9b1def6cf",
        "text_sha256": "9f2c121de9813a1d008e9557f3c493f99000e2c394e28c79046708397042a019",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a6bde625685f0047",
      "claim_ids": [
        "M-KND-03"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 58c977ff0914...",
      "snapshot": {
        "source_id": "S-a6bde625685f0047",
        "url": "https://www.edrmagazine.eu/nspa-supports-a-coalition-of-nato-nations-with-1-1-beur-multinational-contracts-for-155mm-ammunition",
        "content_sha256": "58c977ff0914c0dbc4a2ddf75dfe9b57790295f03de3092f2af7b89fa64104aa",
        "text_sha256": "f9beb6f9674496d0fff344e3411dc8242a750f513c8538a1813a7d5fab46a8df",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a6d23e590b4f0f19",
      "claim_ids": [
        "C-STR-36",
        "C-TEC-01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 2e4e61a09a4c...",
      "snapshot": {
        "source_id": "S-a6d23e590b4f0f19",
        "url": "https://esut.de/2026/04/meldungen/69857/rheinmetall-vergroessert-mit-destinus-die-basis-fuer-raketensysteme/",
        "content_sha256": "2e4e61a09a4c06e21a35998922d4e3ca4139ac772c087e4b7fbebaad13fd3666",
        "text_sha256": "14e1d2ce0b8e75efcdc1c5d8e338cfa1006b0a0cbb7be79c92014f92ca60959a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a6f316c0deb5a97a",
      "claim_ids": [
        "P-D31",
        "T-E22"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 dd8508cbc783...",
      "snapshot": {
        "source_id": "S-a6f316c0deb5a97a",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-02-rheinmetall-and-argotec-launch-their-first-satellite-into-space-with-spacex",
        "content_sha256": "dd8508cbc783629e851f11fa129d6400c59d21bae2268e0aff020430b58d5900",
        "text_sha256": "5e88d12e0c58fb568fd1fd2444ec77ee4abfc41f41e883be3f690a2d92a3cd33",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a7836c43ad7f552f",
      "claim_ids": [
        "M-NAM-05"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-a7836c43ad7f552f",
        "url": "https://defence-industry.eu/finland-to-double-artillery-ammunition-production-amid-growing-demand/",
        "content_sha256": "1dd608b96b2cd51903236cacc89467df86ad115fd2104da37bad7bcf71640c32",
        "text_sha256": "20a91090a9ed7c397d8cf38fc200ea39cd151f1084ed16e5e169f8c680f3cf09",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a8887f614647359f",
      "claim_ids": [
        "H-01",
        "H-02",
        "H-03",
        "H-04",
        "H-05",
        "H-06",
        "H-07",
        "H-08",
        "T-21"
      ],
      "note": "Seite Vorstand der Rheinmetall AG vollständig gelesen (Z. 9-86, inkl. Mandate). Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-a8887f614647359f",
        "url": "https://www.rheinmetall.com/de/unternehmen/gremien/vorstand/vorstand-uebersicht",
        "content_sha256": "e1f0fee6a052ccaba93ad0fc37eb511d62ada5df82bce7a1daf8ddf4dd98b2b8",
        "text_sha256": "f96421969ed3507fe0fdfd22cdd718e73be32f310011efc45f3954d681128986",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a8a9832464019483",
      "claim_ids": [
        "P-V40"
      ],
      "note": "Pressemitteilung 20.01.2026 Z. 9-30 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-a8a9832464019483",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/01/2026-01-20-challenger-3-schliesst-erste-schiessversuche-mit-besatzung-ab",
        "content_sha256": "5a8cd00112c24fa97d1b91b803af8eba4e13e103117cfda181ff279e66e43644",
        "text_sha256": "9d85d224ef464a292c189c72c330fb9ddc1b8092501fd796befe60cdf6b87bd6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aa0e041164bf4895",
      "claim_ids": [
        "P-V52"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 078c081eb69b...",
      "snapshot": {
        "source_id": "S-aa0e041164bf4895",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-27-rheinmetall-is-supplying-elephant-heavy-duty-transporters-to-the-bundeswehr",
        "content_sha256": "078c081eb69ba0518238faf18cdb4f54856dc5a3ef94062b423ac86ea428e463",
        "text_sha256": "51cf4e61bed42286b7a1ef162c6015f0fc01e2e03c3fdee5b762e17ea4fc5aba",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aa0ff06d95479d16",
      "claim_ids": [
        "M-KND-09"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-aa0ff06d95479d16",
        "url": "https://de.euronews.com/2026/08/13/riesige-explosion-munitionsfabrik-colleferro-italien-rom",
        "content_sha256": "4fa6f82835332eb8843cccc41078de2672b5251755f01927c71529198eac088b",
        "text_sha256": "21c78fa991ce9614e76cc35db7c5de446805af8401af9e269280646fc8d020e6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aa782bd6fedfefb7",
      "claim_ids": [
        "C-MKT-04",
        "T-E04"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-aa782bd6fedfefb7",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-18-rheinmetall-and-iceye-win-billion-euro-contract-for-space-reconnaissance",
        "content_sha256": "ee898c3afdf9fc6fd171d8f54ed53744150e9399cf2c5a6050cfd81abb3a723d",
        "text_sha256": "11495193d48839922eca7d5a6f516bc5c081d91d779c63e1e09224947245661f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aaaf59c399a65ff2",
      "claim_ids": [
        "H-02",
        "H-M02"
      ],
      "note": "Euronews-Interview 17.09.2026 Z. 266-325 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-aaaf59c399a65ff2",
        "url": "https://www.euronews.com/business/2026/09/17/rheinmetall-chief-papperger-robots-are-coming",
        "content_sha256": "5264396b9aa09ce5aedfa57ca4b1a55dee1bb315ea73416788ba3c8e60c4303b",
        "text_sha256": "c2c0a5d992938608e677431ff6bf6da7d442c8c159744cda74b5ac3f43c46577",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aadcb3da199c3d17",
      "claim_ids": [
        "M-KND-01"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-aadcb3da199c3d17",
        "url": "https://knds.com/en/products/ammunition/155mm-ammunition",
        "content_sha256": "84011b34cf3bb0cb7d05186e67c68c5ec5353cf83c2698fd2b4fc8be2ae9db72",
        "text_sha256": "c27006e3c5ab030b6f1ad9806497e82d2566db7f517f614a0efa4cb4565142e6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ab4fcd39ea28045a",
      "claim_ids": [
        "P-R20",
        "P-V60"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-ab4fcd39ea28045a",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-defence-nederland",
        "content_sha256": "8ff0da4a4569cb76ca3e3088ee292534ae76a67f4b1ea2ae6c4666ccb6982521",
        "text_sha256": "e009172c7bff49658802aa1f78cef0a30fcddf9d30f96be63610b899e652d806",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ae3e82623d92513c",
      "claim_ids": [
        "C-MKT-12",
        "C-STR-23"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 9e3d1212d5ae...",
      "snapshot": {
        "source_id": "S-ae3e82623d92513c",
        "url": "https://www.australiandefence.com.au/defence/land/rheinmetall-nioa-munitions-to-manufacture-m795",
        "content_sha256": "9e3d1212d5aec3e0ca41cf9a7eb85980bec6071ad52a650c3fbbfdd5c57e5366",
        "text_sha256": "82677689fe939d3f7011033ce60f05f4020ab473283aa3dba4ac93843cb4d654",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ae6533fe6378a611",
      "claim_ids": [
        "M-NAM-08"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-ae6533fe6378a611",
        "url": "https://www.nammo.com/annual-report-2025/",
        "content_sha256": "2fd2a0ff12bb7d6f97f4a254cf8bcd90986df70da7c99b3f4504f1a51a68572b",
        "text_sha256": "3ffab3d10f9f3362f9beb2a2bb10e307f065d64b87dc855a09415dccf16d746f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ae7a06352c503d15",
      "claim_ids": [
        "M-GDO-06"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-ae7a06352c503d15",
        "url": "https://www.ccc.ca/en/announcements/ccc-u-s-army-sign-agreement-for-ramp-up-in-ammunition-production/",
        "content_sha256": "19fd860a42f11bc05adcd7ab2757e71ecd03e9be4babeb7661e3b435a9cce99d",
        "text_sha256": "b59cdb73cf63e1379a9ac764a05ec89f9153814575dae4bd0949f7977c782d0b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b003618b3ae9eba2",
      "claim_ids": [
        "P-A14"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-b003618b3ae9eba2",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-02-rheinmetall-is-supplying-four-skynex-systems-to-an-international-customer",
        "content_sha256": "6c6ddd6170cc82f989cbe12b81bedd66be80b49351753df8d1326b6c389c23cb",
        "text_sha256": "eba55636148b0da38d70b5f9e731a5cec0909a5b0b4c9c1bcd9c6993de7f0893",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b04118fa6c556f66",
      "claim_ids": [
        "P-R51"
      ],
      "note": "Zugewiesenes Original gelesen: P-R51 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-b04118fa6c556f66",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/leonardo-rheinmetall-military-vehicles",
        "content_sha256": "64d004ca1d1770e7a75e10a9ec90066e193cc2bf7c1f8828a5f616f6af24e085",
        "text_sha256": "522998b1a3ca7bec951f1d084d7c8203ecf2a746b791b9a7d5e2f701eda77fb3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b0798e89d3ef051f",
      "claim_ids": [
        "C-STR-33"
      ],
      "note": "Pressemitteilung VMZ (EN, 28.10.2025) Z. 16-24 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-b0798e89d3ef051f",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/10/2025-10-28-rheinmetall-and-vmz-establish-joint-venture-cooperation-with-bulgaria",
        "content_sha256": "8c6568fd4b7b27954199bdcd6b6209a2da4edf82a6d94bfe01a5878bb4782b20",
        "text_sha256": "5b05504c4900a769285ab24dfb51c860c3329afa1705da212fdae4461f3a210e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b159a0c9329835a7",
      "claim_ids": [
        "C-MKT-11",
        "C-STR-20",
        "C-STR-30"
      ],
      "note": "Geschäftsbericht 2024 als PDF-Original gelesen (PDF-S. 21, 31, 158)",
      "snapshot": {
        "source_id": "S-b159a0c9329835a7",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2025/GB/Rheinmetall-Geschaeftsbericht-2024.pdf",
        "content_sha256": "97e93f7c491bc55405a7d5f01ffabe2947742785654b8edb59c93c819a6ebdab",
        "text_sha256": "9e92df52f5dd7d8dd8410735430af20e91ec35cee11c980e4f4329a69d147c48",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-b51615fe3bffe105",
      "claim_ids": [
        "P-R80"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-b51615fe3bffe105",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/10/2025-10-28-rheinmetall-und-vmz-gruenden-joint-venture-zusammenarbeit-mit-bulgarien",
        "content_sha256": "1569b869318855bd5875ccd6a871d76663754de91f94687e90e77622e6206548",
        "text_sha256": "26829b13494142e1b238ba4dd4f0baef5ba64e18bf69684d46344e4f08018b7c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b5266898eb6af45b",
      "claim_ids": [
        "P-V15"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 205ceb886324...",
      "snapshot": {
        "source_id": "S-b5266898eb6af45b",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-06-rheinmetall-integrates-human-machine-teaming-into-armoured-vehicles",
        "content_sha256": "205ceb886324b78f219f13eb68e3f645f440d265d7a230a8ab0287cd52e08c0d",
        "text_sha256": "43c9c5dc274d19ef791457999685e37f72363301e3be5d8b60a897653372430d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b64e5959eefe9394",
      "claim_ids": [
        "P-R120"
      ],
      "note": "Zugewiesenes Original gelesen: P-R120 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-b64e5959eefe9394",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-defence-australia",
        "content_sha256": "f5717fe29910ba4f1598d307270a588a7b6732eb1f9b5ad5e403db85f6b6ac00",
        "text_sha256": "3e63bd2118298666908c531641466bac2801aea22df661d12908c455ca57d862",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ba345071cf3244b4",
      "claim_ids": [
        "M-KND-06"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 30346a862804...",
      "snapshot": {
        "source_id": "S-ba345071cf3244b4",
        "url": "https://euromaidanpress.com/2025/04/22/le-monde-90-of-caesar-cannon-barrels-produced-by-knds-are-being-sent-to-ukraine/",
        "content_sha256": "30346a8628043ab2071edd00f3a0756c2d271c83c6c8741fb2da66fb1eccca4f",
        "text_sha256": "f6a6ec32e08a65325e4108fa7082d4e205f0485ce51374dd77ebb0330c7e2081",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-be6a33c1caf2a631",
      "claim_ids": [
        "T-E25"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 10e625bf4e3f...",
      "snapshot": {
        "source_id": "S-be6a33c1caf2a631",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-08-rheinmetall-doubles-its-syndicated-credit-facility",
        "content_sha256": "10e625bf4e3f23222ac547cd27f022390eb8de5fa327d1ee91895d4b5b131c60",
        "text_sha256": "9ae1f06604a14bdc46a80bd65f03b3ff709117a54d67f911b56953587da63daf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-be9afa65076fd992",
      "claim_ids": [
        "T-12",
        "T-E12"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-be9afa65076fd992",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/05/2026-05-07-rheinmetall-news-quarterly-statement-q1",
        "content_sha256": "1ee00d8af1b623deefd0eab95632d89b3d67b735e09fedba3ec9c3875b4f5a2e",
        "text_sha256": "9fb33f9a9e7c07253b8d834ad0242686caea34aa670beaba02bf279fb87187d0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c0d13e5db6387716",
      "claim_ids": [
        "P-A10",
        "P-A13"
      ],
      "note": "Pressemitteilung ILA 2026 (10.06.2026) Z. 9-40 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-c0d13e5db6387716",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-10-rheinmetall-showcases-its-cutting-edge-skyranger-air-defence-system-at-ila-2026",
        "content_sha256": "ca4de3e91bf637607eeccffa8a1b588ad33ff8e422b4ab8479a5165f4f1f1be8",
        "text_sha256": "99cf4bb953f2ec864d8f864ba6b386c39e94ff6ea98e1f37416ad15d91a71c38",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c2d3f808da3970cb",
      "claim_ids": [
        "H-M08"
      ],
      "note": "Handelsblatt-Analyse 04.09.2026: nur Anreißer (Z. 10-11) frei lesbar. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-c2d3f808da3970cb",
        "url": "https://www.handelsblatt.com/unternehmen/industrie/ruestung-wie-armin-papperger-bei-rheinmetall-an-seine-grenzen-stoesst/100251097.html",
        "content_sha256": "fce5739bd4b41accf1c468c451b398433cd58c3a17c1c3703c1e217f4607db78",
        "text_sha256": "7be8bce561c97cf1052639e16187af5b05fb5752f85293c5bc8893e8e55e8a43",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c36a781afbd14e05",
      "claim_ids": [
        "P-R60"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-c36a781afbd14e05",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2023/8/2023-08-18-rheinmetall-opens-lynx-infantry-fighting-vehicle-factory-in-zalaegerszeg-hungary",
        "content_sha256": "b738dd1a78f25ce789e4736c41376ccb0478c11ddc2626a37d8a0a8b26d42a5b",
        "text_sha256": "8b1e035e845b1b60d83778cae1c2b3db266ca3d7cebd73fa5d44aea5e9015a0d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c3ea3c18a3447ce4",
      "claim_ids": [
        "M-NAM-07"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-c3ea3c18a3447ce4",
        "url": "https://www.nammo.com/locations/vihtavuori/",
        "content_sha256": "2748ead728492f1b9421768d4de31fdd2ebb95d5955ce6a424d9de0448cae17e",
        "text_sha256": "e506daa3d66e10a67d192585a61a958e6b1e49727aeba8db4343922467dd30d2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c4cf8d872c93d230",
      "claim_ids": [
        "M-KND-07"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-c4cf8d872c93d230",
        "url": "https://defence-blog.com/knds-france-signs-multi-year-shell-supply-deal/",
        "content_sha256": "66a761e27c9959f70beb638f60ab01f52555f0449bfe88739eab2d55596f1d59",
        "text_sha256": "0e1cdc7fc2a8ebbab04febc03c22f0206549ffd09e50f7fbfb1ea9bb5b090ca5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c5cf7a0840515beb",
      "claim_ids": [
        "P-V11"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 1bb01d6a263b...",
      "snapshot": {
        "source_id": "S-c5cf7a0840515beb",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/03/2024-03-21-rheinmetall-contract-heavy-weapon-carrier",
        "content_sha256": "1bb01d6a263b7926994e9cbb8a58db124fc32b5145951438e5811545b05f1af1",
        "text_sha256": "c864a2a526902ebc82279ffcf83630ecf988ab40b3dfce8bc9a4d8d93d51f6ae",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c72d2f16b02e496c",
      "claim_ids": [
        "T-11"
      ],
      "note": "Zugewiesenes Original gelesen: T-11 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-c72d2f16b02e496c",
        "url": "https://www.rheinmetall.com/en/investor-relations/share/dividend",
        "content_sha256": "b3777b18fe7a91c4d700e43db651ea0df1e48280fb1bf3a73477e9c60d3daa2c",
        "text_sha256": "3137b95a92bf9d90831def8286c09638f47a29a0b2a7d847beaa1b0346b9cc13",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c85fbd35697b1263",
      "claim_ids": [
        "T-E17"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 2b1ed7f6ed61...",
      "snapshot": {
        "source_id": "S-c85fbd35697b1263",
        "url": "https://gcaptain.com/germany-ditches-delayed-frigate-program-in-major-blow-to-rheinmetall/",
        "content_sha256": "2b1ed7f6ed6129f312b508b6cc15dfb73b18b919ab66d80e4d39553ae4deeca8",
        "text_sha256": "dcfb7d1e7b2efb94d272c9afa1d73bdca3025f31c6568a0077770dd56980c9c5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ca2ef615f2c38313",
      "claim_ids": [
        "P-R140"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-ca2ef615f2c38313",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-denel-munition",
        "content_sha256": "2f34d27ba44d7fe707086915cb42cb51deaec64ccd7439ba7550e2e725d3c750",
        "text_sha256": "0cda419a9df39ac1dbf93d8d177f80ec92bbd559bb646795804c4737d060a27c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cb779c0fc1dc604f",
      "claim_ids": [
        "P-C03",
        "P-R70"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-cb779c0fc1dc604f",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-automecanica",
        "content_sha256": "7612b4614d2fa55317e3e253182c565ac452c6405a8b9b1b25696991cc445318",
        "text_sha256": "dbf08a4712c7eecf81bbe981dd9a5bd59fc9c7094a22c213772fc76b909e0ac2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cba7c69a4b9f251e",
      "claim_ids": [
        "H-M04"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-cba7c69a4b9f251e",
        "url": "https://www.scmp.com/news/world/europe/article/3363426/german-arms-giant-boss-says-no-chickening-out-amid-alleged-russian-threats",
        "content_sha256": "74f8dfb2442738230d6119c1920bb75a4ba2ff797c7b61a420ce79ebdfd4e2ae",
        "text_sha256": "fe3ae90d7be121c3d3f8c4ffd8230473b7eea32b2fe966c41f426619af75ca13",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cd90025f003c456d",
      "claim_ids": [
        "P-D50",
        "P-R97"
      ],
      "note": "Unternehmensseite Rheinmetall Nordic Z. 8-100 gelesen; Meldung zur Standorteröffnung 01.10.2026 steht nicht auf dieser Seite. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-cd90025f003c456d",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/rheinmetall-nordic",
        "content_sha256": "79a63e42ca9f8bbdde7bb7ae6ca49d40bc558efe689e29da0863c14e0005ac00",
        "text_sha256": "c806b423e5b2d1b7aa707bb7366520b6c526eb6c312a4f9b9624c46b726ebcbf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cede873d57924937",
      "claim_ids": [
        "P-R72",
        "P-V30"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-cede873d57924937",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-02-major-historic-contract-in-romania-worth-5-7-billion",
        "content_sha256": "a15eeaeeefcb0d7af7b6c950440635be539ccce545c534d9c113a5fb2884e1b9",
        "text_sha256": "df3c1fe3255cb2b6821a588d7c83334b275d90cac5a1ce855f1f6191e6c146ec",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cf746dc76f173082",
      "claim_ids": [
        "M-HAN-07"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-cf746dc76f173082",
        "url": "https://thedefensepost.com/2026/02/01/hanwha-artillery-ammunition-us/",
        "content_sha256": "9fce58dc7a9c63c0d2d8ed1192b2819718a0518774240732c83ca2b1aa74eefa",
        "text_sha256": "178def6f76411b73021f2b0dafb64d3e0f47a338c017ee67aa64800a2dd02898",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d15683e7fcc1068b",
      "claim_ids": [
        "C-MKT-09"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 59b226349d5d...",
      "snapshot": {
        "source_id": "S-d15683e7fcc1068b",
        "url": "https://www.stripes.com/theaters/us/2026-09-01/army-receives-prototype-replace-bradley-22720127.html",
        "content_sha256": "59b226349d5dd44b956aab575038363d10e5fac37ff637e1d2f30b1f40273388",
        "text_sha256": "d58ed27b044ad510639c7bcdf805e093e2900a52419f36f48e2c51f551c93b19",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d195b923c24e0507",
      "claim_ids": [
        "P-R100"
      ],
      "note": "Zugewiesenes Original gelesen: P-R100 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-d195b923c24e0507",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries",
        "content_sha256": "59686382193946d7b4a2515d9a1ec6e40d343f8a9d7405b893dbeb3d14914f42",
        "text_sha256": "a750b2bb22d5e34afa7d0aac94c52f7e643171e1c0271c9ed12a2be2a268566e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d32c73540389046f",
      "claim_ids": [
        "P-A11",
        "P-V12"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 d76d100d5847...",
      "snapshot": {
        "source_id": "S-d32c73540389046f",
        "url": "https://www.boerse-online.de/dpa-afx/capital-ausruestung-fuer-das-heer-kommt-spaeter-546388.html",
        "content_sha256": "d76d100d5847b2cacbc6ccc9c4dbb5be2e94964f720639d6969498712efd11dd",
        "text_sha256": "dfea3b8097662b82b016d6cc99808a7c92bc1d2a098ccc89bab1f0d73c65b4ff",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d3fa58c55d18b853",
      "claim_ids": [
        "P-V13"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 2cbc33d04286...",
      "snapshot": {
        "source_id": "S-d3fa58c55d18b853",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-25-rheinmetall-rbsl-team-boxer-uk-delivers-100th-boxer-vehicle-for-the-british-army",
        "content_sha256": "2cbc33d04286035065f8c14452d2fe4214aedd11bef69970786825ec1f115e0d",
        "text_sha256": "41d0416af22b1c0043acc9bbd5706da690c10df33a8bbea4759f5b5543689dec",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d4c67e98e04fa64b",
      "claim_ids": [
        "P-D01",
        "P-D10",
        "P-D13",
        "P-D40",
        "P-D60",
        "P-R160"
      ],
      "note": "Divisionsseite Digital Systems (undatiert) Z. 8-54 vollständig gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-d4c67e98e04fa64b",
        "url": "https://www.rheinmetall.com/en/company/divisions/digital-systems",
        "content_sha256": "c5ec5d782962c10159a115b5f977a9c19ed09c4cf247f97adb7bed2b322c08f4",
        "text_sha256": "96a600a006422070f9f49977b22c850a366937bf5a1cf5ae7b9ae82ed057ac43",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d5770c619bc98981",
      "claim_ids": [
        "P-V31"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 837d9253d1fc...",
      "snapshot": {
        "source_id": "S-d5770c619bc98981",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/01/2026-01-27-leonardo-and-rheinmetall-hand-over-first-lynx-infantry-fighting-vehicles-to-italy",
        "content_sha256": "837d9253d1fcadc09b34657e1dcbbfe6d5bf15438f9455fa71f35d301fbc6863",
        "text_sha256": "1e4359b06885f91d2f2ecfbc1cc80ad960c41f556b1c41e765f8b427977d498e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d660e9d6543050f7",
      "claim_ids": [
        "P-R50",
        "P-V41"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 d5a817f24e5b...",
      "snapshot": {
        "source_id": "S-d660e9d6543050f7",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/10/2024-10-15-leonardo-and-rheinmetall-establish-joint-venture",
        "content_sha256": "d5a817f24e5b924956ab3b374d182df9f68ebf44557dc73d17fc73e34845f2ff",
        "text_sha256": "339253f005d21d5de6d49590b356e07432d08ba3de6faaaffcc45b161bc38789",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d803328fd1670795",
      "claim_ids": [
        "M-KND-02"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 f359526cc504...",
      "snapshot": {
        "source_id": "S-d803328fd1670795",
        "url": "https://knds.com/en/press-releases/knds-at-mspo-2026-showcasing-comprehensive-mission-solutions-for-regional-defense-sovereignty-1",
        "content_sha256": "f359526cc504a5e8fd0ca33ef0f916fe8558c9e80f5ad6d53672415770cbc842",
        "text_sha256": "2193edac3dbb61c86c4a835673284387743519ca27e07f444d132f7d91437c1c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-de8e49377d100ea9",
      "claim_ids": [
        "P-W11"
      ],
      "note": "Pressemitteilung 155-mm-Rahmenvertrag (20.06.2024) Z. 11-22 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-de8e49377d100ea9",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/06/2024-06-20-rheinmetall-receives-framework-contract-for-155mm-ammunition",
        "content_sha256": "c30c294eed2a17bba286d0faff6494bba9d60879910b49e00cc47895323a661c",
        "text_sha256": "7bdeb6da2f13aaaf0437c8f45cac4f11e62cb67ae00fca2299f59996382b149e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-df4cbdd63bde02d6",
      "claim_ids": [
        "C-MKT-10",
        "C-STR-19",
        "P-R61",
        "P-V32"
      ],
      "note": "Pressemitteilung erstes ungarisches Lynx (26.07.2024) Z. 16-26 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original. Runde 3 ergänzt: weitere Abschnitte des gespeicherten Originals gelesen.",
      "snapshot": {
        "source_id": "S-df4cbdd63bde02d6",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/07/2024-07-26-rheinmetall-hands-over-the-first-lynx-from-hungarian-production",
        "content_sha256": "1dca0777e70818f6625367fdac577ef70ec0d60d1eeaad3fd6c484debf6d5fac",
        "text_sha256": "e10a90fb57cbe99b9b570b22d326b4d14251cc70d22a75b978a1e2db51f00b49",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-dff299ab3ecf3cd9",
      "claim_ids": [
        "P-D50"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 fc5d7553fe15...",
      "snapshot": {
        "source_id": "S-dff299ab3ecf3cd9",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-01-rheinmetall-nordic-opens-a-new-location",
        "content_sha256": "fc5d7553fe15eb824a1ed1fab009daad244d9fbacfe59dd7e3d8976fba75c675",
        "text_sha256": "6672ec244df6653d8116a7ed18afc9463a20d6431d2692a7038cce071e0f3628",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e1f0237821c9aae3",
      "claim_ids": [
        "C-MKT-07"
      ],
      "note": "EDR-Artikel 28.01.2026 Z. 42-47 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-e1f0237821c9aae3",
        "url": "https://www.edrmagazine.eu/the-delivery-of-four-lynx-as-is-marks-the-real-start-of-the-italian-army-a2cs-programme",
        "content_sha256": "72e1223c5065300dfdb3637cf4ebab9ba36383680c78c9174361be1bc155faf0",
        "text_sha256": "a7322d641d176b6c675112e0681c21b29d75140cf501b6bf707b9c423d8239f2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e40dbc076868eb5c",
      "claim_ids": [
        "P-N30"
      ],
      "note": "Zugewiesenes Original gelesen: P-N30 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-e40dbc076868eb5c",
        "url": "https://www.rheinmetall.com/en/company/subsidiaries/nvl/international-operations/naval-technology-bulgaria",
        "content_sha256": "ce4741acb78901f7fca574ab304da1a5d6a73abaacdfe2384a0ffffd9ae8f129",
        "text_sha256": "77bcf85a36d3160e5ff9f5c3965dce05fbb262c5a8f592d26508d9189a5cb232",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e48eee025a306fad",
      "claim_ids": [
        "C-STR-29"
      ],
      "note": "Zugewiesenes Original gelesen: C-STR-29 an den genannten Belegstellen im gespeicherten Original geprüft.",
      "snapshot": {
        "source_id": "S-e48eee025a306fad",
        "url": "https://www.edrmagazine.eu/%e2%96%ba-digitalisation-of-the-armed-forces-rheinmetall-4ig-and-hm-ei-to-set-up-a-joint-venture-in-hungary",
        "content_sha256": "b1c56b89a74c46e2b439efc2b40baa20c42a5d4fe1a9cc2d9639826beb154bee",
        "text_sha256": "2e86ef35ea8af6a75784b268d1c94b79bf3ad946edd1af4a0e02affbcb9092db",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e4c101cb061aafcf",
      "claim_ids": [
        "C-CAP-02",
        "C-CAP-03"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-e4c101cb061aafcf",
        "url": "https://www.rheinmetall.com/de/investor-relations/veroeffentlichungen/stimmrechtsmitteilungen",
        "content_sha256": "ea677ac5161f764c1c4520afdb9b0d72f8e91404ebf4d6b4a3325a75e5e387b3",
        "text_sha256": "aa7f9a40b777bf10b0a92b2224147705ceb00cf4929e5b230f1f1ec39ff17c50",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e8d99b5c0a3aebdf",
      "claim_ids": [
        "M-MKT-05"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-e8d99b5c0a3aebdf",
        "url": "https://www.polskieradio.pl/395/7786/Artykul/3605551",
        "content_sha256": "49f895c55690215be2dad53ea32caa1e630734764ce32c2d378ca80e24cf1777",
        "text_sha256": "d67e50a9f2b1ae306ca0eb0dceef2623e7c98ec49cd5931923cdf6b930853cca",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ea5f61dc37c5379a",
      "claim_ids": [
        "M-MKT-03"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-ea5f61dc37c5379a",
        "url": "https://www.rferl.org/a/33025300.html",
        "content_sha256": "c6f65cce8f7e78601ae53dc7ee086661f2cbba2f4c03f555d8918b1c8970968e",
        "text_sha256": "f1c9e74debb9af0f494ea0d5fa621915158402e13d99d3e76bccd3c966b212c3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ea6a47ff86b90b1c",
      "claim_ids": [
        "C-CAP-01"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 f646e82769d0...",
      "snapshot": {
        "source_id": "S-ea6a47ff86b90b1c",
        "url": "https://www.rheinmetall.com/de/investor-relations/aktie/aktionaersstruktur",
        "content_sha256": "f646e82769d08d4cc1339a914e272e2bd96fe100808dc6fa15ddd24363d194c8",
        "text_sha256": "d28003bbf79cafe0a90da2020ad86903f533ffc23a2b1474c293d13eca067a60",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ed8c444ff9f73ed3",
      "claim_ids": [
        "C-MKT-02",
        "C-STR-08",
        "C-TEC-09"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 f07b7888c0ab...",
      "snapshot": {
        "source_id": "S-ed8c444ff9f73ed3",
        "url": "https://euro-sd.com/2025/10/major-news/47322/artec-to-produce-222-schakals/",
        "content_sha256": "f07b7888c0ab97c758081052ec3016821fa04f34fa4392b6d93cb74b6bb6bd0a",
        "text_sha256": "0078f2672f3f8fe34812fe31e49ed2b4fb7d86c2df2a7389ab904a8249b0b8c9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-eeb74caefc3275d0",
      "claim_ids": [
        "M-GDO-03"
      ],
      "note": "GD-OTS-Meldung 27.04.2023 Z. 49-50 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original (Text bzw. bei S-98082c5c6a5443c4 zusätzlich Original-HTML).",
      "snapshot": {
        "source_id": "S-eeb74caefc3275d0",
        "url": "https://www.gdots.com/gd-ots-recieves-217m-task-order-to-increase-155mm-artillery/",
        "content_sha256": "7b3ba3aad7f53d41edcc87d311d1de6ca181c57aecd4ec356ef42c60108fab04",
        "text_sha256": "2f4e10a4517533b0a22bc6fe5ffc85129a66301707bb14d9d74b602930e75e56",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f4730b21412bb02a",
      "claim_ids": [
        "C-CAP-03",
        "C-CAP-04",
        "C-MKT-01",
        "C-MKT-02",
        "C-MKT-03",
        "C-MKT-04",
        "C-MKT-13",
        "C-STR-01",
        "C-STR-03",
        "C-STR-04",
        "C-STR-06",
        "C-STR-07",
        "C-STR-08",
        "C-STR-09",
        "C-STR-10",
        "C-STR-11",
        "C-STR-14",
        "C-STR-18",
        "C-STR-19",
        "C-STR-20",
        "C-STR-21",
        "C-STR-22",
        "C-STR-23",
        "C-STR-24",
        "C-STR-25",
        "C-STR-26",
        "C-STR-27",
        "C-STR-28",
        "C-STR-29",
        "C-STR-30",
        "C-STR-31",
        "C-STR-32",
        "C-STR-33",
        "C-STR-34",
        "C-STR-35",
        "C-TEC-01",
        "C-TEC-02",
        "C-TEC-05",
        "C-TEC-06",
        "C-TEC-07"
      ],
      "note": "Geschäftsbericht 2025 (Original-PDF, 13,9 MB; Cache-Text mit Seitenmarken, ergänzend Original-PDF per pdftotext in Lesereihenfolge und gerenderte Seitenbilder). Eigene Originallektüre der Belegseiten PDF-S. 22, 49-53, 163, 171, 252, 260-261, 263, 265 und der Anteilsbesitzliste PDF-S. 267-271. Kein Volltext-Durchlauf; nicht gelesene Berichtsteile sind nicht geprüft. Alle zugewiesenen Claims einzeln gegen die Belegstelle geprüft. Snapshot http-original, content_sha256 138727c9936e...",
      "snapshot": {
        "source_id": "S-f4730b21412bb02a",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2026/GB/Rheinmetall-Geschaeftsbericht-2025.pdf",
        "content_sha256": "138727c9936e18cce3a3e85772863f35c22cc8d842ec9baee46b5cbf5035bd6d",
        "text_sha256": "770480588acc0f7d1b5c644315270d9e6425c27c7363c930590e51a72afefe76",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-f550c79e68fc9c76",
      "claim_ids": [
        "M-NAM-04"
      ],
      "note": "Gespeichertes Original-Snapshot (http-original) per source-cache read im Textteil gelesen; Belegstellen je Befund; Seitentext als Daten, keine Anweisungen. Snapshot http-original, content_sha256 f091391af06a...",
      "snapshot": {
        "source_id": "S-f550c79e68fc9c76",
        "url": "https://militarnyi.com/en/news/construction-of-a-new-ammunition-plant-begins-in-norway/",
        "content_sha256": "f091391af06abc2377d13b8d37bb77f52d2275a73027a6e49b1098e01792269d",
        "text_sha256": "9b3d4443f885254a2b380618062c7dda5d1c0824aebe523eb3b67b2e719705d9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f55f74045ea5d4f3",
      "claim_ids": [
        "C-MKT-01",
        "C-STR-07"
      ],
      "note": "Pressemitteilung Puma 200 (19.12.2025) Z. 10-16 gelesen. Vollständige Originale sind im Dokumentcache erreichbar; Prüfung gegen gespeichertes Original.",
      "snapshot": {
        "source_id": "S-f55f74045ea5d4f3",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/12/2025-12-19-rheinmetall-und-knds-liefern-200-schuetzenpanzer",
        "content_sha256": "2cc69e03f914214c0ccc960c3a8c18390d508d5d92a2edaf93cd5bbd69b26754",
        "text_sha256": "db816c9d206c7dcc2137e9abd02038e84b028903fd73707e290d05d58da6c9a9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f562ccee195198fd",
      "claim_ids": [
        "C-TEC-07"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-f562ccee195198fd",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/01/2024-01-25-startschuss-fuer-luftverteidigungssystem-nnbs",
        "content_sha256": "957b3782f9ab4f9c7d9f2f467fa60d183a1158af569aa736bd7a2e335f28b333",
        "text_sha256": "9da7f1ae06d0720edfc4bd681f96e9c963f40c502309ca272e8d78d7a67dd2eb",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f67a3aa803cc0e9f",
      "claim_ids": [
        "T-17"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-f67a3aa803cc0e9f",
        "url": "https://www.rheinmetall.com/de/investor-relations/aktie/basisdaten",
        "content_sha256": "913908bad120ea43f33044f5b84e5ee3712c6672a86d0df160d79b41a6f387e1",
        "text_sha256": "4130c5264d734743841a7c294e489ce4ce2e5224c53219209d47b9e570509dc9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-fa3be73251a7e9c6",
      "claim_ids": [
        "H-M03",
        "T-E21",
        "T-E30"
      ],
      "note": "Gespeichertes Original (document-cache, http-original) per source-cache.py read gelesen; zugeordnete Passagen gegen die Claims geprüft; Navigations-/Cookie-/Werbeteile ignoriert.",
      "snapshot": {
        "source_id": "S-fa3be73251a7e9c6",
        "url": "https://www.boersen-zeitung.de/unternehmen-branchen/rheinmetall-will-kassel-zum-groessten-panzerwerk-europas-ausbauen",
        "content_sha256": "89a50cd8fb909875082586a7b81438bcf25272e808da6680540bdbe1b36d54ae",
        "text_sha256": "5dc2f7daa6c72510935936b44f655959a1802496c523c00e51ab37e7cc4c29f4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    }
  ],
  "parallel_review": {
    "plan_fingerprint": "da10258b7ec6256e20eb86c78d3bdc96f05f736f1741533f5204a4fcc8f347e0",
    "source_collection_fingerprint": "04779e4a0d7c98e567157de197d57e126b3b92d1ed7950fd6edfe208ca9747df",
    "part_fingerprints": {
      "sources-1": "22254134447c8f9098093b12062ae68f0b5d26bd5bf3e5c0882e755b5dfba984",
      "sources-2": "2213667f306ba4f104b5432792b6007d6733f4fed3c1a0570a3c9eee73920270",
      "sources-3": "2a14c69ce6ea10da39df67a70f4f4a442f6cd3ea3566eaf26112d16ee8506331"
    },
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
      "id": "P-R51",
      "evidence_review": "Runde-2-Korrektur umgesetzt: Seite S-b04118fa6c556f66 zuordnet Wannenfertigung/weitere Varianten Rheinmetall, Missionssysteme/Elektronik/Antrieb Leonardo; Statement und Unsicherheit (Foliengestaltung, kein JV-Fertigungsnachweis) korrekt. Folge it-lrmv: Beschreibung auf belegte Übergabe 27.01.2026 begrenzt, Endmontage/Zulassungstests/Logistik als Plan, P-R51 aus claim_ids entfernt. Nicht blockierend: kind \"integration\"/status operational für die reine Übergabe großzügig, Einstufung bleibt wegen control unknown Stufe 2.",
      "fingerprint": "a69bf03fecb654d17ae813f62998a5d28048e993e44c4c979bd72f775956984d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R60",
      "evidence_review": "Runde-2-Korrektur umgesetzt: nur Werkseröffnung 18.08.2023, Sitz, Entwicklung/Fertigung; Testzentrum laut PM 2023 im Bau (Unsicherheit).",
      "fingerprint": "3d19d59ebdf6dacdf899eb7cb7115a693114cdedc9cd5ed87ee9e19a1a84dfd9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R61",
      "evidence_review": "PM 26.07.2024 gelesen: JV 51/49 und Testzentrum mit Schießtunnel am Standort belegt; hu-zala-dev-Beschreibung (Testzentrum laut Mitteilung 07/2024) konsistent.",
      "fingerprint": "95f5eda9105e49c727817e7663068e768cd6f41b3ddd796b1ed4b6ce157c2aaa"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R100",
      "evidence_review": "Runde-2-Korrektur umgesetzt: Evidenz 3 korrekt (American Rheinmetall und ARD Inc. unter Vehicle Systems, ARD Inc. zusätzlich Hubs, ARV nicht in der Liste, ARV LLC über DBA-Fußnote und C-STR-24); us-hub/us-hq ownership_notes angeglichen. Nicht blockierend: Vienna VA nur in AUSA-Quelle S-6797a3b3e68d3be1 (im Claim so zugeschrieben); Region us coverage_note nennt Virginia nur als Gesamtangabe.",
      "fingerprint": "f8895b7ca19c019f3d33093212aaaa4a4ed84b6aa66ea97da9293e4da9d7f38f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-01",
      "evidence_review": "Runde-2-Korrektur umgesetzt: \"Hollow Base\" gestrichen; Archer über Produktseite gedeckt. Nicht blockierend: location \"PDF-S. 8-16\" zu knapp (Produkte S. 9-19); \"HB\" in O-knds-spectrum (\"LU 211 HB/BB\") ist Variantenkürzel des Katalogs.",
      "fingerprint": "2834a7e618623e3c371146f5640673e9e25b1be99c4ce2dfe788885ec39b3ce2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-37",
      "evidence_review": "Quellen gelesen. Nicht blockierend: Datum 09.10.2026 der Maritime-Executive-Quelle stammt aus Metadaten, Seitenkopf nennt 15.10.2026.",
      "fingerprint": "f9ceada490d5cf350bbf6dd5fd50e1f2fe627a367e256a4c8f7ae7ce27c72770"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-21",
      "evidence_review": "Teilbeiträge geprüft. Nicht blockierend: \"die litauische EPSO-G\" nicht der Rheinmetall-Zuschreibung zuordnen.",
      "fingerprint": "5dc57d7cc9f7220e84d48e866aae4ab18e22c79da196a5429fec493ebcf88fcd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-CAP-04",
      "evidence_review": "GB S. 263 gelesen; Claim erhebt keinen Vollständigkeitsanspruch (BlackRock/FMR durch C-CAP-02/-03 abgedeckt). Nicht blockierend: als Auszug kennzeichnen.",
      "fingerprint": "c4196ca4d84d47c7de35442c84a3fe04251a441927db0e2cb3ada1e71f22eda0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D11",
      "evidence_review": "PM wörtlich belegt; Quellkonflikt in C-MKT-03 ausgewiesen. Nicht blockierend: Querverweis ergänzen.",
      "fingerprint": "da05a59c94994af9cfae6572c39d2b501c6bb70448ddedf0f5a336a179b5cba3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M01",
      "evidence_review": "Bezahlschranke: nur Teaser geprüft/freigegeben; Aussagen auf Teaserumfang begrenzt.",
      "fingerprint": "f9d915e47e3cdfeca589c74ee448f9ad18c668ca6f8a620879167f0e66a171ed"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M08",
      "evidence_review": "Bezahlschranke: nur Teaser geprüft/freigegeben; Aussagen auf Teaserumfang begrenzt.",
      "fingerprint": "469bca4f5f4f448c01851413fb4707658b4a2031cfc6047c79f7dc21eeefd56a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-HAN-06",
      "evidence_review": "Bezahlschranke: nur Teaser geprüft/freigegeben (Unsicherheit im Claim).",
      "fingerprint": "bc1a9daeb4f8e282b5216f92655cdcc44cbe46c2ac9f34b902130c30177be4e9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-31",
      "evidence_review": "Teilbeiträge GB Ziffer (36)/S. 171 und Halbjahresbericht Ziffer 12 geprüft. Related-Party-Offenlegung des Unternehmens mit Geschäftsbezug, beruflich zulässig, keine privaten Personendaten; Darstellung nur als nahestehendes Unternehmen mit Rheinmetall-Aussagen, ohne Wertung.",
      "fingerprint": "5f37dcadd92ca0772f42f928e143e78dd15f55464557afcc529768caaa0a0b3c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-CAP-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e0ddb82f6ee76158f498d4eb989dbed2029b05ac1304ea7b58b64a4ce8a9d91e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-CAP-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "15b58cf37b6f72602299b19a9168c2095a1d986d4b7ed96ead4fc0f4a9ff5086"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-CAP-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f23fc11246e3a9661c59cb23817cbb7bbbd3f822dcfdeeb0300f20aeb8341969"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4d5bab957e9d174e8db308c85fa0857f976c7250b8ada401532fa36a05647412"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "9c82ad869272f4ecdf97ae28aac46988a846bd0c33a57b045caa3d83cac78af8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "56dfebc94117dc1852016c4e509e64d0226e70e23b612e894abb63fd7bb105dc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "be148eb37438867f034193b86b54114a73e9dca6698f6c9bb23f54c9f8459852"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "24b6f48d3ea38a7e50683f9730591daa9236e27d93751853ef2df208d154674a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d9ffec9603cffe8245ad348fcb56e08b15b43406e099da73baab6861fa162ab4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4084ee48e613d5f5aaca3d2ad7d82298b38e5383cdc01a07768146a2c96a11d7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "809e1f42228e713ae8c358f7d393399efc4f98ea68d66fcb3610a0ee036c9c5c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "90fb5123e505ddaf54bde5aca1c4e90420e4e5d74d81c3ad0ceb734ade238678"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a9af7822a6f54d25dc7ab3c2b345f161965240ccba158ed5014c36734f20e234"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-11",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "5fef60606ecb83637c8fc0fefd9326181a5fd924544d3d7b9cfc8d6e48d3f0f8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a21cc82f90953855392d4038d789d45da942f3d6ad5d57d85697aed9713227b1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "055e13cfac490c9f59684bb25287c2bbff1d0b3aa4cd4d39432e0674112d6f61"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-MKT-15",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "9da66702357017ff808d4b550b8389229a591d8e54d96eaaa0cab868d25aecc2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e4cbdd1f805abc63f4df1e1052a9aec7f922efaaf73ca71777a683d8aa223e8f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4c9c8390dac4c1d5f8d45595f810e2a42bed958ec585ce1388a0195bbd0c01ee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0a85959bc80da43a67db356aae3c86055c9956b316c3924f570203ab99854a1f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e48a9c04257e8a8b39b03cd14b0f684ecdc0b896c805f1b2d0232dfb077b6cf3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "ab579b82e6c56273fe70235111cdeb19e53635e080f1364329466e7d19415818"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "895579139a2de9d5c58d6aae61550fa435c93fa828da68aced638624afdec6ee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f0950465ef69dff20ebfc768528f06562023697fada117a64acb686cd4cfb722"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7835db227474b551fe8387b77ef63650e680db7066ae55ba60cb0503813bcacd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "357b78502f4d1c7ab51830980648e343a15f06818f5a398ba685c81481fb33a6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3ad8eee5b501fdebc4adc1fc7bd564bca127bf638c95f463932a9d5d4e9cffab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-11",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8af3459fb410e3f60d1fef8b30d07809c11047dd2406be2c60399ac8111b805e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7ac92ca215821e573b4946b1a1194f5f03798c471839aee78a0fef00ef9e6bb2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "19ec78e56d648b224e96683ffb5686685c5c310a11e7b47f4444980c668b5ab2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-14",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "5739b8f4354a9fb523f14c0698eb27e77a6905c0027e60acf653f5718b2425f1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-15",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "fd9c2dc1eef26048851b6b284bc328bd57a1c92d50bfa959ae0fad097fd909ef"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-16",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b06f224a70bd057b3c39ca4d0d1a63ec930704be64afd8e96e7043f22b50038b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-17",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d6acd92e41f4c8f025ba1acac135fd0629e745020cf604cb8c51cdf4ec6840ab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-18",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0f0a3ec3bb27f410abfb4af7139076bb583058adb25a7f4d62a29d0262783ddf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-19",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f47033e4e261a154fedf22eb1a2c954be7f8fae83fd3aeb72659f5b59d214338"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "21e0e82508308b39e284f4af4df56a860222a41908e6182836b33a94071f28a2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-22",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "cf7c6b17dd009a22eeae4b536ccbc02f45159f2dfe26b8ba2b905f08e6749c7c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-23",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "2b373c644dce0dc295db9d5d71a6f97a90fb1c6850e058c185411c00e8f412a2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-24",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "ab15eeaf4fa926240b01133f8d28eb888e6f5f4788398eca66c9090f7c2da7f4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-25",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "544211755911d37c99532d4c63ef3c88c3a47dc775e00aa5fa9ee7850521c5cb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-26",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0e0fa37a83ecadc6cbfb6ba4cb941707648820bd0c9407a9f2c1d6ef22c82d1e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-27",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "bb2bd59cfdfb9a35dc62261f2228e5e47ad4b06bf7dbe66a2887a68059023664"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-28",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "354ca3f40ad88fb537d35ffdb911eee1f705815661dc337d9b0b254c41c6b25f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-29",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1f687397ab9bdb7faa45a59c1bcf3199804af43aef7f579cc836f361e0c7ba69"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f1f9bbe56517cae7809018f9aedf2c478fc42ac3fabc2d8303c2de2c1de352a6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-33",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7a093aa2cb82a992859cf8ba0bde3b8d1f4f09949930f6e005941a74b4b17342"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-34",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d2ad1b73b35862a8c667bba9d2c8a00f8ecbf8a598955dd3e75daa701fd54be1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-35",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "ceca0867ca68a014e41b7b3863f9f9b9c0db2df02a02f236b8f704e4313ba90c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-36",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7dac007f2ec978b913ba1781a21723b6591b8a41fdb2d8b570faf6bd9db21ce4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-STR-38",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6a39ebb8b4ed877f85e180deea26ea35cecd6178a97ed1e1b88d52c69f47caf7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "87dacfc33ca3577b8f830472a19f68d03befcc154be7639b4fb84bfced5fc8ad"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f193bfa23e969a4ff9cbeaeaf85f3276d4e45bc95bd5e58dca1f929d2c0c1688"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f53a8f777d39ac581aeb554b6674a1b87977d5f1051747c5f40ad7bcbf09c265"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "2b713b962d96000e9dc85bcadc02f6206901c08822ce8bb24289ea8ac7d01feb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "517554c12e0ebbc968e91aecf5e4771aa44e90f9f4d003b83e0ee0e9a26ae9fc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a5fa7cfc42cccf8e33cc4ea985bef09a3ce5ce18b98bbdf867c07a89cb3d2615"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e855238b18bfa135e286cdaa28eea49660ee41f75c065030e59a47b6c9f8e3bc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "04df4b9a6df5d1eedb214d9fd741a9086d52818964ec6a29c35544b1cc5bfd7b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-TEC-09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "53c533c395b9e2d63f929098628577cfc96431209b5ee9bb51bdbbfc58d84707"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c81a29f7cd9d3b3121f5e9709d616541a835249f9715ad2ab9c758183db75f00"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f37c3f53563b74295c64a47a10783a842118ab8db80a75ffa71decd1cf257545"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "661105b718c1dd64368c3347042d6b8f5178ef50d301439e8f8efd5e34b18d40"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "adfc1e6a2bf09fd85d5fea684e9defb7e470c6f0700b4e6a85cbac72fed20ce7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7920b632903608450a09dea15bfe238a1b9c04e2f5858de9e7a0aff2563d3b2e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "13b3a8c99f562ea0f38b40a8360aa6772966b601ab8b7c08c13b576630458871"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e07ef0d67db5e3a91f093feb9ab15fc99f3cc739a0a7ab04e57c572c184a16f1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c280bbac891640fa7851e93df9811bcc4e90cf25720974c503fb13c48fa7559e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6eeed95c4bf633627c3c21bd0e507995b3347568709ce63840ec4df7006abad9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "de525721fd35fe8edd8b1b97a4dcce32e1712aa9461d1bda2e55dbce309081b5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "113708394686d72e72378702570f77894900388603f236beea682f3f46fa38b6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "bc250e79af17df98d68b94b2c1ada820e0d0fbfe288bdb22dfd155638f4c5ff7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d520a99d879fcc2c63642560736fbfd2c5f926872ee841b84762c8ba860729b3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b8bfd935155b0afdd1a513993bc0c14b672460561956317ef236687199784b33"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "aefac91d6bbc1cf226a6a710e639258afc6c42bde38066332b33917c688c348a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-M09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4fcffff6cbbb784b752f2f292bf4f56d5eb813353902efdf7ee8b581ba13057c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-BAE-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "123b0020f40b820d98c558ca4d7fe4266620efce1a558ea72cb7d271671443d1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-BAE-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "665cd3c7333cb2b2158d5c38eaa436d35da207a7ffa5d79d47025151646c3c22"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-BAE-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7106264840231bd10e8333012e1e75ed498d796efd7de973658a0cf9601b949f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-BAE-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e4fab237f28d6abcbaf0339ed95236238c0bae1ce0c2bf8f96d95b42883c8f0f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-BAE-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "048a5decf797bbf831eed247dabe269762cb48287c3ec681e8b6f010626c0811"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-BAE-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0e5ab7c658e84364889d9456402525001b033021b2b3424365e17436fb3cc6ea"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-GDO-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1eac430bf25798c2bba281fd31100d16d19ac99c1804e45ac3b403fd68c4cfe4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-GDO-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0e1314dc544704720dd8ac467b119bf1a15e402383b8995dd13c682563750aba"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-GDO-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c026fe2e4b24f57e2f4429ca3a0b8e5292ed76692eb42ae8203cff42a323aca8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-GDO-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "fe4b446e0ef147e289fed12a0e0fd07676714d808055150d56aff0c2a9687689"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-GDO-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a00c31c8339ced21913e1d482a0a92392977068ea12340f05dd9f1949cd64025"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-GDO-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "658e3913586d67d154705d9492a8699644a6d8783894c36103daf1d82fcc0a4e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-HAN-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "821f6d325d2c0dfbaed980fac6fed300bd4485c44711f05f74b3a8e73c6d5494"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-HAN-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8f3bc771b8c14d19a71e8af6f3a81f70b636b5281653ee83926caf293b469f11"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-HAN-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "752df7d77b3784aaeb7c1425a677f6bfbcf88205249af727c96a278617b7dda4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-HAN-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "be7ee953f08b533cdc4db4545090e3e5fb285ebf146e617c7b021b5d26f2d175"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-HAN-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6c5b2e2274c7ad7ecc6560d254a7e581d4e61fc095bf6981bc1bd5b12f78e1a6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-HAN-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "79d6be7238d5339c7f9c637d132f1e7a8f54ae99ff9fb48427b55bfc99599a32"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c853fe20171f9eba9843711062f178bc16c07aeb07c9626d073268b7b1a55148"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3de872175ff4840881481b25adef6b3763543672ea6bfae71e943263d11feabc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "295fc2725763faf405314da2d84391deacff142c4a56711a95574163ba721afc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "db44e1ca2cd83831130e4e70a4e0d00745ddb67323e09edbb508feeecbe1def6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c37434b460e52fe687803a48df15043fc957954940137defb01772d8fbf16610"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "41f61cb55a3cb8e25268168241336c17d88167488f6d30244bb41d3b7b3feb2a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8078b13ade9094971614b24a90756703b2cb2d0e6780273b470f09d161f64817"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-KND-09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "913f49276bcc147304d35c100ee28d84ae25a468b274902a65a1bb62383b8a6d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "850a9de7e750fa0610764faae5ba0fb2a6a753e0e84dac434cf327b6d3734523"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3a4efc4fd0e817ef75a3cbfff34bc6adac73354962e4648527a899c2a6413797"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "adbc3a30cc40ac53db2f835863d1bdc769be0dab4d3aa9ecdf251184e746c9bd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "655f7bf92fa5baa716f66f674adf6dc2385879b3d0517ba23e3b71ab8c91e1db"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e3dd0c74c6b5f571a15773977549886492cd691aa279ddd533634c460b99c44e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "93d857dbcdc810bccc95581bb449c5f4c0d46b8439dbfdc732179bd05eed9962"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b76a5de197bd4feea5ca5b09e655c5e11a9e02708e487c4088ea87f412c8d09c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b2017fd36e6cee959a99a44f648ad37fc8ebf7c8a43cfcb0e5dc5a373598d404"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "61e78f2f491b14258deb7adc7d0de1d8ab6bf09744cac2c6b4bcc27d989aee8c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b92032ef5e9119a06de79c7a05fd5548f72db418e318171bd67f5b00d2494c53"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e435a63d4517c2182d11eddb19565ed5d3ece977c36267702bb831d567f7cf58"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4ed9982bd122a738f984efe4ffcc469b6ecc43910ba0aef5011175edcd801b39"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "2c138aa7b5d16f1cb753ff193441c5150e3c6aa2080201a782d4ee6e2437fa94"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NAM-08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b5a98fa772b2b57b01fc48b30e1f1de1bc59cd9509d746e45e6995b2cc9eb8ec"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-RHM-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c4c452295e89b405a0c358ea31de04d94cf0514f7575a7c0c0275120d876165a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-RHM-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a447eca2b13c04628140baa221478ee0d13f632b1787394a822e57285d873a45"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-RHM-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1e8f6ce5d7653409ec379a41ca6543aa3da28ecb17c9722e9943d9faac023113"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-RHM-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "06963c914230260d6d8042bd5b4b2af51c621bf48e620678d92dc3ad9e593394"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-RHM-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "dcdd1feca4871dfa23b4ae38e6f3c4c55381606fee6cb95625ce14e3bad0a509"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-RHM-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c52bbbf88e663d7e8524bc70627a48f7b2ad96b649825a958a8e06553a62bdbb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-RHM-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a9e08111df3cab7a55e6715c002d5f630a8c78a585182182fe792f80b6573258"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "732ef528ab4059d172a51fc8a2f6cd5e223e60bdff0c622ed887a335729b63b6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "28bf1b83284b659a789abd093c050af1da75b0b1f665f40121f1ecb019799cc4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "442a221645225f5079aeddd474656ae2fa45ad8312bd16f6b67a0deb4187cbee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A11",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b299392aea3af6d5da520e2344ecc281613ee8d6687e06ce568b6239fddfbb8b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "851feddcf1d4dd9c2f3e309614ac349938ee3db8e1191e86665ccc4b9b24133d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "688408eff0c8ac837c971a521dc4ace27a718469c0a78a70e0f494d1ced2521f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A14",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "5584aaeaf41b83fc96500669210d1bebb7cbc0b00164cce34e64378a9ca1aebc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "813f95def4dee5eba0e5f2c2d71a9ee4d8604eae03862b1a1643b66ab9f7bf64"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A40",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "5480b0781552fc64dd5cbc245a1ea9d841a1d9210c0e6aec9122140cfa3eb167"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-A50",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0a3f78e08540ef31c1f822174655d0bed53aced475597f59c22a0b34cd6b8bb3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-C01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e24f0f50017bd9ff9019e4407989950ee936297b99625db245e68a1b8ddea121"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-C02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c46da5ca1f02c094f54c671bd023b685a06a8933073baa8cc6302412821d3a86"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-C03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e7234b72d4fa68cd8cc4e216ab42b21acaa12d03af79820846b83d3d89e6283a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8dbeb062f1db5f427b6f2916aa30629fa1c00334982037c95a8f36e5e9f919de"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "fd2563be7abde18071513146d6b6ff2b0f17cf374ce37102c7d36f313519ac15"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1ea5d34ecbd813a552c9283ac7c7541c4ee28ae537b232caad4f2eeaa9dd648d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d0d907ebd185b7811819ef478c385fd1ca71f25f7ffcba94f5621de960afa3f6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "85fbcf9c7e9cd19fba7d93f66015f5400487f9000051ed4ead19a9e38583ecbd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D14",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d7d0dff85dd7bbec8d2ed668963135438014a1a3e285f3f06a89f319a00397cb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "edb0938e1b57a5b2c5ccd6358af02b4a74b277e74342784056a143991d8e5ed3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "522052b5b638c9a387a1db1159bc9aa3a05ab6d7e6ef625d0b39c75b9a06c0da"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D31",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "442a1e6e3b2c4e548e7e7633403f9bf40af77bf3c10f7e1227d95736d46b9f90"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D40",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "88fd21466106b7292cea2e1a1098ac1acd6c19b7c0d91b1bff8e7382d5b07ba8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D50",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "552dcbc509eaec9af8dc47afe1d22b8b441e43d04b9c3f059f5a3b69f1585454"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-D60",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f331843e23a1666523d12e42eda2799ed801dfc50d9a4d19e9f041b9b707322e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e881f4bac48759ba88975f7ae360502d1a778c05edfc0b47afd45a6022fad085"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4b0ee65632c0fb13c555838818379830ea1d87aa20202f3aab4b07cee49c042d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d9c6a8116e404f8448fc1e44b0ced6f1e2fc236f4a0f947f4e42ccb869cd8c64"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "405df3a16b2744c9bb794e9131b4943e5b1ebc23af6662c7cead680ecb0dd499"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6d6535ddf57b9953f7478d2c4f286e23a9ee98753f7ff686527a4a55f286aacb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c453ba71e16c7e9cbd8c9cf317f8cee9a284b77432cb6a9eb8b33426802d31b2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N31",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8af7f4efce18820a60cdfca11db5247aad71a467d6ba1986019bc355fadd703a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N40",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8700087fae6fbd6f3d9769f8b7a3d330471bd9bf3fdf09fe66be85b23cc9f935"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N50",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "39a27fcd492091f4a2284f45454b665d346f1b202366bfe6092cf56ecf03483e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N60",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "ce244df2b747612f6a77deef927c83c8562c6a3b4403b5dbcef06d0dda448033"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-N61",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "46171068547413b550a9d881a4706902437654afd627d4b0b2262b5fb470dc05"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d8b2043af4348177c3fc445e9b68d7089827283d0e6b9a63716faab112541b62"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "541e78c211a78bc65c7885edee0f0f5fccf5da374c1c3b93b80478395280139b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6fefd4b7454fc0b8ecf054b6077c9a97baec975867aefedaff794924c344dc3b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "aa9d5c6141394874d78f6ef7bc648e8cc07d32ecf3c9cffe15773b58dc005939"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R110",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "01c0dd8909dd73c8555d8ac05972288fe088e93078b26a36414b174f99f01191"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R120",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "31f23c05c15c6a590adc1d9829bea11d2d8b311f04649346835a3e729851b837"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R130",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "9b3ee98a40ff45a5444a6c09acc9339eefe78c243a4c1151bdc307abf3b1c5a5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R140",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e1932512192e36d3e697d7314c7fbd260c66cc23bcc87a217ea9e58dc30226bb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R150",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "ffa0420a5fdca0f79382091d6b95244b38333107f7182abeb92d90c42ad2ad0a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R160",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "93a4bc91cd08d3329b6814d17c1616301ac87c8b9ba1c1346113b8c98d51660c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "33a15de2023ef4b83065e7285f6887fcbbe68561ce393ccbc649c1ba078d68e1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b73341e47daa428f5836470421eefedeaf0eddbb326649ea67451146a0961f0c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R40",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3938c0c39f23880bd49a8a74ae49bbc5a5ce52c421bca2cee27d733447f2bb14"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R50",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4d48d0761033a22cc6491cae4d0b43e23098098d764de7b1c2a3115ba030f84f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R70",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "06868e8b96fa2db1ebec22377691249ea48a8b2905479a9c4e2bab1f6a31e103"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R72",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "5bfe50aee1ca9e7938f68ee6a7cdd98f906f50382e647721cb612da0f1f2cb97"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R80",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e429d91cd90dd121b5fdd68ee8ef7593b826d4f7f73b857227bc13b157046b96"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R90",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "386cf1e843fc57e1ebfb1d1750ee2e915f32cb5cf6a5fd417df4c793a9659b4b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R95",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3bd17dab3fbcdf6a4525a37e4710d8270b705bdfff76c4fe59b9ace44b1340f8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R96",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "fe01bad5849f069a18460c67a604e2341669000298ed81cdd57e65563a8724bf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R97",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "fe9eb82ef18e86e8c73931d657b42810ca06259eb9ca50796ae09d667b5b2f8e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-R98",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "dd4ce262021017b5849bf68855f430817a1d5e8cdc4299809cf21d9c93441c7f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-S01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6d09356103072bf6e43d720d42233a61554931cd8935ed0bd62de201e3631f9c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-S02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b012efa3e0d58e55e1f1ff05394407f01be54f4f018374adeb5878996109621a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-S04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3be53d2ff69bc38a4314082933b52e8a893952fe5694abc834efde5ec4d362dc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-S05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "400dd92140017000f8aed9aed8e2c4ade14b5b757c6294f30266187769fd8b0f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6dfabf92d44786d3f648906d95bf8bcbc75bd7c33a0aa153fbb6779d5109401b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4642c31622e05ad04e61315bd8e75353446769ac6636ded68aeda58af000f63a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "68ef65d0f2c65dffd7461dfaab9ad722e52447519f3ba6cb17f093615c2d4b1e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V11",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3f3990d8d7fcef9ebe1cf7a887f7cec956a85790c1190f706dd11afe6f79a39b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "bc06a895ff80e713ed7b22deed5e31ec13ccdddc8ee6d77b4cd5f1a9dcadf8ee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a43497a33719aa404332664ce39c3fa944bc535946376186b9003ce30ff7b4cd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V14",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1d1e9aa2a3c8e1a04a6307e333ee697759d58d1f3c8581bed0bee7fddf83f391"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V15",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "32a2e75a7f650f29656dbbfad309a00f38106d47f42f31ae35396b40ffc089fd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V16",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "35896075d4483ae90fd2520a4733fbe455603a8395ce3eb4b05c166352c296e4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V17",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7e9cd17f5de9feaca1a4b2892f3f656ed03f8be5c902f31c91f61deff512b9b8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "13e93781ccf1e6a81a41584f7a52121e5c80930c56f7b85422d0bb2df4a7d70e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V21",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "ab5478fef5240edefefc41c4c3b3a6ae4eb5d01706f236f629b546db5ce2cc4d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b9564f422b8f43211be241586e6eb58fc00ddbe4931d11dc1fb42c3857efe2a9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V31",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7cace4476f0d6b3505338d545dfd06846a2273f31f01753ebdd08aa87b23a772"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V32",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "2035bd3774aa73195f5867db267480fbf1e823ef3eaf3253f2431842d51b4745"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V33",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "be4cbe2421fed71deb10f38ff2099722f9118c2218b875431487485d38d5324a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V34",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "65fe420663cc86a47527b7a4c6bac168138b89bb1f733852bdb1567c4017fd91"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V35",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "70191c7f197f3986e01b1953dc567bd0dd92cb86dfa3c001eebbaecbd8da9d72"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V40",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "14603ce9387df837cc3dce64c721d8a8905954c62ce0f0ea1ce9d28786f36aee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V41",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1b385f40b6cefbdbfd540eb11fce1da452c07a6b9cacae33bc9e7306f2092f2e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V50",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "531398091b7fa82ef36d5755b342a8c9594d36eb79846f8aada9cc9388aa00a1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V51",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1dd3cd30b092f564392c251398ce3c4a3fa349023052f7d386c147c912c60200"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V52",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0bf11dc4cf70ca0dc8a17fa30602ec5d67dea34b695ed069975e1d3c25412c18"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V60",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6d836970391123df7f1f3fb34be05ca013af5cc3a9d8899d04ca2d58063d6137"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V70",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8a848ed5057a6c6bdba35ddf3d8e2d38e93e978ae34574d06950aeb8da4f7253"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V71",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1b536e364671cc8e78a43ce524c04822d1cb47c6a5e541453b8c03911ab0a4c1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-V72",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a04223431a46dd39f88c95c2be524ac3464ca0238c8d96dfb5384aab34a8eeee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "46e93fa5bc21894cdf887cce4bbd62e86b0b65320cf53cc42242a80d59103fba"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "9bd731db7f18dc63510425bd56e7b49666636a001d8b0e1b17ebf03bd8def683"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "91affcf81625b76f269c60c24d1efc05f4821b2ee563457436dc4d223a07f2c2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W11",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "dd3f550ec94cd4ffc4b923d49ec610ab1ce8bc4dc124891d5bc261d26a220a70"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a127528141849b9282a68a9156c7079dd5a0289752f08a669c55a4624c15b842"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c35eefe91e412883bdc19cf57c86281ce1d8e2ca1684bd2e8cf6cb221383e24a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6e515f134f7649a72fd52d9bd59c413c5ab653697871e687ae4bff01427319a6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W21",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d361a9c9157e73df8d6bcc1be41ee8999afeb712588ebc2985a5aa7450d516d1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a1bff11815d594a5816bf288b1c6bf3b36c722c7571a643f973b468294c1f2ce"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W31",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "23fc3b40a59e13462ea770f90b268a650e8aa22a4d5f2d0d557a9bd5a9f678dc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W33",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1c077e5c82b3ab1e090649962952e1cbeb743aa91ea944c7a13a0ad85ff0c50b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W40",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "909325e35fa32ea79863818367b712c198062ec4bf2a3e698ee6d744a27ab010"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W41",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d22e7817ab2e356b92456bdae6505dfee57065b5bae5601ceb0c345653ea33ab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W50",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d17f6e967fc86ff1d344f182597216185bc6e65065eb0b3bbbdb95d647af4743"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W51",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "cd59e13cacb77fc57a2ba510e3ee41c8bf7b2b44beffcc29cc6b29ede0f92aa1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-W60",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d2abbe645315d7ab8845ad33f43baf618383e47ac254672735bc1b2d8c7a30a0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "020b7cf4775510c23cb7004747aae09a8948447e5b31b1b143c9e5a744588a5f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "77ef82ea1b5c38ff4ca7327e86af02e34ddfd333b125721f86b63335be813c33"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6a8986d3076fb30574acf15e2a2d05a828b539a5b15c40a4657d3808e1b07244"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0f059fb583dbb81201b20231425264d834acceab9c46d341a6eea466fe0747a0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "66a9eacc0707dd8f1a7b747db149ce355e07b33eaac67cb7140763818e4e94b5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "72d25b33fa8805b9ce6a8624e2ad05879292ee1e427affebe042e46150233f88"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8a006dfec5952f8b0fc590f5045c90c91d877f4718179651e84fa39cbc0c1cf1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "84e2576a050357fe72ac0a33f41e62a025ad938f6a5468e408f14290789be295"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f1eac2ec3d78a4aa4b766296b2aae669b29a77297cf0339b855c4d35b40468c4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "589e51c8558c6512e6f15341266f4dfcfdbc49d9c84ce5fd2b2612904428981c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-11",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6d0a0baf3de3a566a0d8dc0081de7134283239cfc7b7e7fc59bfcdfbc4c4788b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "df277d076d3b2de8deb85a2abc231bf9159b728666d666b1abaf3795020446e6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0b4d2abadeb53e3828abea20c199f30ba3688fdf47d8f4d68872a6b28d0cee46"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-14",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "736d16d6979a01761538678198b5592c729e9688604619d811d4d6805ae48f8b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-15",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "c196e6a090fba980192b2ce5b4648594fc231581ec749576c42b7490dba60ced"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-16",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "e873a2805681bd804aaa2aa3ac97f4a260e93d343fcd6fc05e2d077b192e5dcc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-17",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "f5bdca79dea18c9c64a3ed5e639e473a95eae8383fdc5e6590199b13224cb0eb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-18",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "29915599a24abce3044bff282b0e670c53a6b5d85f7f9f87ba374ce826a726b6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-19",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8e172938b12f2a3dcae0cb44dfadea3bd1d7a12b67800873ddfa40127aed3d43"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "9947f2c6e5dcec8d99adeb65c8f9c13c8cab5eaa3b5f64d64edde4a50375e948"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-21",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "dd9a92361311c20b5ae42abcbeceb7ac48e8a7f19163015e2f54ee6d1c63481d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E01",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b9f561fbd195c714b9ff2ace5e5397e6c74482f8bea55d570a81a7b685cdde8b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E02",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "d33a46449e5ff4d97b38535f46679c41168af12b09a1c52085aab7f91983a876"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1f136538980d9942f1b6a63292dc7075beb669b986bbefc7ce86bd82de360ab0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E04",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "63459d8cf40d6b133ecb3b3d65a4bac628b8ee605a3dfe804bd226c48626b1d9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "df345cdbc318776b25696a9dbfafc96a9366ffdac2a634609d62376e13555e0c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E06",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "cc7451d796f007e0af15d805c8589dcd028f0b6d7052b1775b4e3606f980da3a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E07",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "dd50ae9713fd2934511d61a39445ec60610e9b50986fd8ef0096b76e3567eb5d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E08",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "0929f4a3caf98cabd35840a606e0fe79f362f9a6b9cf6478f56af9fe597c37da"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E09",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "9c274c9bf4ec81b98273e3081273b5eebff525b69de9d7d3dff3cb62cd7aa810"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E10",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "cde1997b27cc7680920a8c7b33d2099536a8a444d2042f3d64f8d0f2090653f2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E11",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "38a10cd883fbafd7c5a877603fe43e79cdfd140eee526ea384582866cedbb652"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E12",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "dc8da64a9fbada99d6ef90d67d0b3cc5efe830363275963aaa7e80dd40ade3c2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E13",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "a1479bf9fbffeb8faad7c6a158fe888dc1f1f75a78c9b028d9dc50f7355e13e8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E14",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "df91467a40c0031163f8a1f255f7445f7cb2d4df4ae5998cdabf4a77d2adcadc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E15",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "4b791a4ecc8ff08dbf911169b13f3026f4249a202708affecaaa9c44734d85e2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E16",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "9d56a3ffafdb64be4b8b553400972d6ce70a2bc65244c5535df44717499d918d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E17",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "493c743b95eee99b27b5f70a6bb9eaf83d29352d8c8fe9a2464ac577e95053f8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E18",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3fc4e360dfd7e25fbe1092df26990217c3bceb8d14c6759936809cf376abac86"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E19",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6517dcd84d1b43afe79d04b0c0c89086584ccb111fb580e09057f6e19289bef0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E20",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b4e64dd84cdd5565dbfca2d1d9335a50227a24a26eccf807734224cd745d432b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E21",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "336dd90eb6499b9c9acbca1cecec9755d274ea179b39df21be3fe295925761a2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E22",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "1f9934545e9a5c76282446145e35d64dd22d3097c69c24b0acde00175665b3d4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E23",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "535077b21251d249a56649822544891052fd0e956c6dbe986a09fdd99bb8f4cb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E24",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "171d0ceb759a8f9c5918518adc87fa563051bba4838083db281b9844a7b671af"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E25",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "088878a203c52807e0f8a3148ecf8191e5a2b1bb0650bdfaaf379de0ad73dd9f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E26",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "8a49abaac56e472bd7dc4f08c17cc4c931ab927fdf7db95c6738ed3e54cccd82"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E27",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "2356157542065425d379b6cd4aa83b602897faa4852f43a9f132a8372127fd89"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E28",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "ffecac925e1c16e26f792a0609dc0512b14529a3a3c29651bc24b9ec0ed489c1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E29",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "7ab83d0685f60fa9b9f8ee67a4e5322552400c988281a059e0b608b2ae0532bb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-E30",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "3adf968bfced90d0fb1eddedaa37f6a5e5e417b99d9d205a892058cb589d6132"
    },
    {
      "depth": "B",
      "status": "geprüft",
      "id": "C-CAP-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6796f0288c53ca6245d50769d2372adf6a3d21cd15ed3c6d8f3d57edf49b7097"
    },
    {
      "depth": "B",
      "status": "geprüft",
      "id": "C-MKT-14",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "5ec559153a34486e4c2554c1da948bfe594f8620d3a029a9ed340a00b5bd6010"
    },
    {
      "depth": "B",
      "status": "geprüft",
      "id": "C-STR-32",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "b081e7348a9c6d8a1432013a7dd6ae97a1a8b1f08f5907fea4ed404b11378008"
    },
    {
      "depth": "B",
      "status": "geprüft",
      "id": "M-MKT-05",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "6918de3b25594820f26a8a64854c0d50a98f2c9f6fa7a79f30a71514d0c1dfc6"
    },
    {
      "depth": "B",
      "status": "geprüft",
      "id": "P-S03",
      "evidence_review": "Aussage, Zeitbezug, Aussageursprung und Status gegen alle zugeordneten Originalquellen durch Dokumentjobs geprüft (Originalbelegstelle gelesen, kein Quellenproblem); Leitprüfung: Quellenbefunde vollständig, Teilbeiträge tragen das Statement gemeinsam, Runde-1/2-Korrekturen (soweit betroffen) sachgerecht umgesetzt, Quellkonflikte (IdZ-ES, Schakal, Puma-Anteil, VMZ, Kraken, NVL-Datum, CMD) im Claim ausgewiesen, Hersteller-/Medienangaben und Planwerte gekennzeichnet, Zuordnung in module_views geprüft.",
      "fingerprint": "25f4e10b024a8a6fe38eafd8ffcab56e00074a92a238e5ca276c6be9fbdab4ae"
    }
  ],
  "missing_decisions": [],
  "fact_review": {},
  "input_fingerprint": "0361e8579024466b5ebf69a04a1191733685a427437d9a75717db7546d7bd4d0"
}
```
