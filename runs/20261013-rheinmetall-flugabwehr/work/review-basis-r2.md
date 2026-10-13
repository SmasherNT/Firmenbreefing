# Review

```json
{
  "schema_version": 1,
  "run_id": "20261013-rheinmetall-flugabwehr",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-13",
  "phase": "basis",
  "status": "freigegeben",
  "review_work_fingerprint": "1929162068b0eb81c08c8552ecf192cdcf65bf33f24ec4fcbb39c77024453c78",
  "material_errors": [],
  "scope_and_mappings_checked": true,
  "review_scope": {
    "summary": "Runde 2: 11 geänderte und 1 neuer Claim (M-DE-ARM-01) gezielt am Original neu geprüft, neue Quelle S-d2d239c37b99eddf gelesen; alle geänderten module_views (events, topics, products, regional_presence, observations, market_dashboard) und Netzkanten e02/e04/e29/e30/e47 semantisch geprüft; 209 unveränderte Claims mit unverändertem Snapshot ausdrücklich aus Runde-1-Befund bestätigt. Alle Runde-1-Korrekturen und material_errors sind behoben.",
    "cache_state": "137 Registerquellen im Laufcache; kein Snapshot gegenüber r1 geändert; neue Registerquelle S-d2d239c37b99eddf entspricht dem in Runde 1 gelesenen Snapshot (c718b1a9…). Keine neuen Webabrufe.",
    "formal_checks": "check-review-data.py review-packet.json: Exit 0; facts-validation errors=[]. Formal ist keine Inhaltsfreigabe.",
    "remaining_nonblocking": [
      "A-CH-OCH.description endet mit „;“ (kosmetisch, portfolio).",
      "Portfolio-Preview „BAAINBw Mitte 2027“ ohne Zusatz „laut Capital/dpa“ – im Detail T-AD-06 korrekt zugeschrieben (optional, portfolio).",
      "e30-Zusammenfassung nennt 225 Pandur EVO aus Kantenquelle ORF, nicht aus C-019-Text (optional, cluster).",
      "Cluster-Modulstatus „teilweise“: Lücken (Stern-Original, Partnerberichte, Golf-Beteiligungen, Lieferkette) sichtbar führen; kein Hinderungsgrund."
    ],
    "open_limits": "Capital/Stern/BAAINBw-Originale nicht geöffnet (Verzug strittig dargestellt); Köhne-Wechsel nur als Ankündigung; Bundeswehr-Großauftrag nicht belegt (kein Negativbeweis); Lieferstände teils nur laut Hersteller."
  },
  "source_checks": [
    {
      "source_id": "S-00676d9d1d5efc0a",
      "claim_ids": [
        "M-DE-NNBS-01"
      ],
      "content_sha256": "e7dcae6a0fd1c869f3e35d1c45595d0840e7eeb37c2b1e28d5fe64aca7fe20fe",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt e7dcae6a0fd1); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-00676d9d1d5efc0a",
        "url": "https://esut.de/2026/09/fachbeitraege/streitkraefte-fachbeitraege/75313/beschaffungsvorlagen/",
        "content_sha256": "e7dcae6a0fd1c869f3e35d1c45595d0840e7eeb37c2b1e28d5fe64aca7fe20fe",
        "text_sha256": "1b4e4bd836cbb49bf04fa52a29ac6d5c116455ee5fae4220966dad7012381540",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-01c26a442587afa5",
      "claim_ids": [
        "C-001",
        "C-048",
        "C-049"
      ],
      "content_sha256": "9e66083297ceb9d0b276aa8b3ae49f41142e0dd59d0950f08d5e6bdb03371710",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 9e66083297ce); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-01c26a442587afa5",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2026/GB/Rheinmetall-AG-Jahresabschluss-2025.pdf",
        "content_sha256": "9e66083297ceb9d0b276aa8b3ae49f41142e0dd59d0950f08d5e6bdb03371710",
        "text_sha256": "fe5cb7c726414657e2af21db2dc407b8d2217f3723fe1104f66e4f078ca1cf15",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-042b26990fdc2a9d",
      "claim_ids": [
        "T-EV-03"
      ],
      "content_sha256": "5c6775c76e8ce02c7a95fadbce270372929e9b1d6f96db4be5ac474ec9893611",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 5c6775c76e8c); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-042b26990fdc2a9d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/03/2026-03-02-rheinmetall-takes-over-nvl",
        "content_sha256": "5c6775c76e8ce02c7a95fadbce270372929e9b1d6f96db4be5ac474ec9893611",
        "text_sha256": "c797a52e2a6b5fc6c0a9f722be4359e14aa8c9b7e6a8f62cb0d3cfb2f6a45cea",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-04cc080af88f833d",
      "claim_ids": [
        "C-042"
      ],
      "content_sha256": "0cb20930a867136f90fc70ad5e0e860cb32bfec16b7bc3c746bf5a162503dbc6",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 0cb20930a867); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-04cc080af88f833d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-06-rheinmetall-iceye-space-solutions-provides-the-bundeswehr-with-access-to-sar-satellites",
        "content_sha256": "0cb20930a867136f90fc70ad5e0e860cb32bfec16b7bc3c746bf5a162503dbc6",
        "text_sha256": "31c5c6079dd2352625c4eda1d55fbb088a1072b8876e6a6c6df0a1944fb0535d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-057484ce43bd0f28",
      "claim_ids": [
        "M-EU-SAFE-01"
      ],
      "content_sha256": "9ef48da0000d3c08f8700e9c22d3a50cf70aa2b991d750c3af59c2359e1130dc",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 9ef48da0000d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-057484ce43bd0f28",
        "url": "https://www.osw.waw.pl/en/publikacje/analyses/2025-05-28/imperfect-balance-eus-defence-loan-mechanism-safe",
        "content_sha256": "9ef48da0000d3c08f8700e9c22d3a50cf70aa2b991d750c3af59c2359e1130dc",
        "text_sha256": "e612b6b0c8a698e73bfcfdb810c5c74d1e54d8d4a9f1a9f1ae0efc8454bcac44",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-081455a6101c816e",
      "claim_ids": [
        "C-027"
      ],
      "content_sha256": "ac9fd7aa4dfc3c9a59eb293063d026112c6d20217d3ad791a9ce1681fb1d7937",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt ac9fd7aa4dfc); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-081455a6101c816e",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/01/2025-01-06-35mm-gepardmunition-fuer-ukr",
        "content_sha256": "ac9fd7aa4dfc3c9a59eb293063d026112c6d20217d3ad791a9ce1681fb1d7937",
        "text_sha256": "caa6e31215c8b9061f1d5b053ae7ef69ddb0da41ad2b484827b3b9f967efd531",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-09c52404c1b93824",
      "claim_ids": [
        "C-015"
      ],
      "content_sha256": "0c6382753b8c40aa9a34035d3ffba584ed87c5c4501b7ef2d220a18692e960de",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 0c6382753b8c); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-09c52404c1b93824",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/02/2025-02-05-rheinmetall-hands-over-verification-model-of-skyranger-30-to-the-bundeswehr",
        "content_sha256": "0c6382753b8c40aa9a34035d3ffba584ed87c5c4501b7ef2d220a18692e960de",
        "text_sha256": "91f319850e78f11511c3025b7bf0acddf8f98939a8265498ca13b56bba2e465d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0b3ae3c34f44afc0",
      "claim_ids": [
        "T-EV-11"
      ],
      "content_sha256": "a845e5b798a1a2b245750a46a6703a09c5e73bf8e3785f23d038e591f38df2bc",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt a845e5b798a1); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-0b3ae3c34f44afc0",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/10/2026-10-08-rheinmetall-verdoppelt-syndizierte-kreditlinie.pdf",
        "content_sha256": "a845e5b798a1a2b245750a46a6703a09c5e73bf8e3785f23d038e591f38df2bc",
        "text_sha256": "13eb9ddb92f207e5ba028e6a029740b98bfe0dd921b20c7945a38c964ab6dbdc",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-0d1aacb2a960fe0b",
      "claim_ids": [
        "M-DK-SAMPT-01"
      ],
      "content_sha256": "92c8dd0ca921d34f3422c85662aa51734cdbcb049268d814b1a09e1e87f93a65",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 92c8dd0ca921); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-0d1aacb2a960fe0b",
        "url": "https://defence24.com/industry/denmark-breaks-with-america-sampt-ng-instead-of-patriot",
        "content_sha256": "92c8dd0ca921d34f3422c85662aa51734cdbcb049268d814b1a09e1e87f93a65",
        "text_sha256": "7b42e1aaf5dcfc72c26dc96a3f59b934530de51875ba7e93bb9f3c13ebd02688",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-10079a15b0d54839",
      "claim_ids": [
        "C-040"
      ],
      "content_sha256": "27e36f8dbedd27c146c5e394a32ca2c15973ef7ec7d1018a6a65d705bd7b3dbd",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 27e36f8dbedd); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-10079a15b0d54839",
        "url": "https://www.leonardo.com/en/press-release-detail/-/detail/05-11-2025-leonardo-and-rheinmetall-first-contract-to-supply-armoured-vehicles-for-the-italian-army",
        "content_sha256": "27e36f8dbedd27c146c5e394a32ca2c15973ef7ec7d1018a6a65d705bd7b3dbd",
        "text_sha256": "883fb9f1d80f0868c1013b479d10c426c7a954f0c1a58c3110d0879413fff223",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-12a6733e8d06cf75",
      "claim_ids": [
        "M-DE-IRIS-02"
      ],
      "content_sha256": "a3b300c6ccd38e74fea7fb7fce04b66bbdc68accc6919525a0308e85d4944c16",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt a3b300c6ccd3); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-12a6733e8d06cf75",
        "url": "https://esut.de/2026/02/meldungen/67674/bundeswehr-bestellt-iris-t-flugkoerper-fuer-luft-luft-und-boden-luft-anwendungen/",
        "content_sha256": "a3b300c6ccd38e74fea7fb7fce04b66bbdc68accc6919525a0308e85d4944c16",
        "text_sha256": "c0b1e85f702ec003aca210bc97f65d2d461bf4974a7a5a338eef66e975aa020e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-12e946370fcf4e20",
      "claim_ids": [
        "M-CZ-MSH-01"
      ],
      "content_sha256": "a5a073334c2865bfebad08eac3903df4c7c00b415bdf86893033726c8cb24597",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt a5a073334c28); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-12e946370fcf4e20",
        "url": "https://defence-industry.eu/czech-republic-orders-saabs-mshorad-system-with-rbs-70-ng-in-e155-million-deal/",
        "content_sha256": "a5a073334c2865bfebad08eac3903df4c7c00b415bdf86893033726c8cb24597",
        "text_sha256": "397ea8e5cdcbf721476720a67956f9ec4dcd8a4e2841a6425ad7e4a6da48c1fe",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-168108fb27118dde",
      "claim_ids": [
        "C-053"
      ],
      "content_sha256": "c465304cc0c0e99d7ff586364461c2de53b20c0baf4345dd0eb99c863cd239d6",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt c465304cc0c0); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-168108fb27118dde",
        "url": "https://defence-network.com/deutsche-skyranger-produktion-kommt-nach-neuss/",
        "content_sha256": "c465304cc0c0e99d7ff586364461c2de53b20c0baf4345dd0eb99c863cd239d6",
        "text_sha256": "a030005c94e6f995448aaf9d93540517a2ea9c0f46cd829391f8ee51921c5427",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-16d1e80677f1a6b8",
      "claim_ids": [
        "T-AD-06"
      ],
      "content_sha256": "65813cd8e4095e9c4f16b288d605edb2cada9c002a8ca6f4c3af69c2523bf95e",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 65813cd8e409); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-16d1e80677f1a6b8",
        "url": "https://www.finanzen.net/nachricht/aktien/in-der-kritik-rheinmetall-aktie-in-rot-bundeswehr-ruegt-verzoegerungen-so-reagieren-renk-hensoldt-und-tkms-00-15892493",
        "content_sha256": "65813cd8e4095e9c4f16b288d605edb2cada9c002a8ca6f4c3af69c2523bf95e",
        "text_sha256": "27e79e18072b43db3787422fa076815375a29aee425640759fd511ad1756626f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-18ce19a1fbbec148",
      "claim_ids": [
        "P-REG-CH-01",
        "P-STAT-01"
      ],
      "content_sha256": "2f906ae59a3a1cf38a73cd1fe15081b43928ee1c191ac267523516f2f07823fa",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 2f906ae59a3a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-18ce19a1fbbec148",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-air-defence/ueber-uns",
        "content_sha256": "2f906ae59a3a1cf38a73cd1fe15081b43928ee1c191ac267523516f2f07823fa",
        "text_sha256": "a89279937b29ce4d3cb173f371e5c49065f5f0e8c71cc78dff87801308cc1419",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-19e53c95b8305269",
      "claim_ids": [
        "P-REG-SG-01"
      ],
      "content_sha256": "a3611b312a1d937db4fc4e8c3ee7fa9a2b406cf495407763b6f96fbcd7a4b0fe",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt a3611b312a1d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-19e53c95b8305269",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-electronics-singapore",
        "content_sha256": "a3611b312a1d937db4fc4e8c3ee7fa9a2b406cf495407763b6f96fbcd7a4b0fe",
        "text_sha256": "35f1f1dbdb27e1c0447ab2bffe85034b2dae92194ec7b1c3396469126e4c0e28",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1ee3bed35c316be7",
      "claim_ids": [
        "M-DE-IRIS-01"
      ],
      "content_sha256": "30f738322b6da7a3dd7e10ca9eeb6121c3ade62018cb38b9f64a23d4fd4701d7",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 30f738322b6d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-1ee3bed35c316be7",
        "url": "https://esut.de/2023/06/meldungen/42792/beschaffung-von-sechs-luftverteidigungssystemen-iris-t-slm-unter-vertrag/",
        "content_sha256": "30f738322b6da7a3dd7e10ca9eeb6121c3ade62018cb38b9f64a23d4fd4701d7",
        "text_sha256": "23b3a179e843d5a1c6ab07d4fa3276e07fac37f015e52283a0028bcb468379d1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1f76748059d5008c",
      "claim_ids": [
        "P-REG-ZA-01"
      ],
      "content_sha256": "bcb93cee876ab196daa76d4d1a85c9fe330d71c45ccd02790009e45c8743e01f",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt bcb93cee876a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-1f76748059d5008c",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-denel-munition",
        "content_sha256": "bcb93cee876ab196daa76d4d1a85c9fe330d71c45ccd02790009e45c8743e01f",
        "text_sha256": "bc8c2eedbbc7c9bdbd5c0dc66f81b5be09c4309de716f0476b7e9074657afd81",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2185a7a52eb76e0d",
      "claim_ids": [
        "C-029"
      ],
      "content_sha256": "70de1e9d55e2401b18dc30fb5e32645669792920e848807c8bdc425c0fad79c1",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 70de1e9d55e2); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-2185a7a52eb76e0d",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/08/2026-08-19-rheinmetall-und-hensoldt-demonstrieren-erfolgreiche-integration-passiver-sensortechnologie",
        "content_sha256": "70de1e9d55e2401b18dc30fb5e32645669792920e848807c8bdc425c0fad79c1",
        "text_sha256": "329f7fc8839ac0289de9d772d76deaf4da0672244c38ce52e6455acd67f6aa05",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-29616d5aef4d2b76",
      "claim_ids": [
        "C-019"
      ],
      "content_sha256": "1ac21497b758330a1e05e9e0a04fe8ffe56e782e4c7c51d39c49f41da8c47b9f",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 1ac21497b758); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-29616d5aef4d2b76",
        "url": "https://esut.de/2024/09/meldungen/52961/pandur-evo-mit-skyranger-30-erstmals-oeffentlich-vorgestellt/",
        "content_sha256": "1ac21497b758330a1e05e9e0a04fe8ffe56e782e4c7c51d39c49f41da8c47b9f",
        "text_sha256": "dd9165bf63a6ab83c3f1e5dd8372094712b38e63f4a0819298d1efa8e2dfb3a5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2b24723c99b5458a",
      "claim_ids": [
        "P-WA-01"
      ],
      "content_sha256": "2b01db7ec69d5df0e3f515fbe3901a317c9dd7d87ae63a974bba92f28fef2817",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 2b01db7ec69d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-2b24723c99b5458a",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/weapon-and-ammunition",
        "content_sha256": "2b01db7ec69d5df0e3f515fbe3901a317c9dd7d87ae63a974bba92f28fef2817",
        "text_sha256": "aaa544feacf5ada0c9f21ef4df9e570ce583acc28f5cb8d8ad2e15f0b5ab8ce3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2d3cddf7945e1791",
      "claim_ids": [
        "C-021"
      ],
      "content_sha256": "34e5e6ef8d958b7ae64cf942b9af2324c13aa903fd94793f0ce1a9956ebad395",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 34e5e6ef8d95); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-2d3cddf7945e1791",
        "url": "https://euro-sd.com/2024/09/major-news/40568/denmark-orders-16-skyranger-30",
        "content_sha256": "34e5e6ef8d958b7ae64cf942b9af2324c13aa903fd94793f0ce1a9956ebad395",
        "text_sha256": "d7d5fc70b7b8c9af3f932aab988c84c172172617fc5326093af57485f5440e5e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2f18768b2b3d8649",
      "claim_ids": [
        "P-REG-UA-01"
      ],
      "content_sha256": "fcbe2971cae7bdb08a47c62c9c2e5e467cd5914d6350010604ec6a942a085a4b",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt fcbe2971cae7); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-2f18768b2b3d8649",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-ukrainian-defense-industry",
        "content_sha256": "fcbe2971cae7bdb08a47c62c9c2e5e467cd5914d6350010604ec6a942a085a4b",
        "text_sha256": "3f99f57f31cb923d558a073f2aac4e2fcab4ad0c3f80838345ffe689e2389d79",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-310ddb82949667f5",
      "claim_ids": [
        "P-NAV-01"
      ],
      "content_sha256": "ceff33aee9d03660f1fd8501e126d5feff013596f0c75441a32a67f8b38782dd",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt ceff33aee9d0); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-310ddb82949667f5",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/marinegestuetzte-flugabwehr",
        "content_sha256": "ceff33aee9d03660f1fd8501e126d5feff013596f0c75441a32a67f8b38782dd",
        "text_sha256": "b758b260cbc42b07477da646d589a0a363fde19c6c47a7ef527e35606f219be8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-31c2ac5b48b0cde3",
      "claim_ids": [
        "P-RGM-01",
        "P-SKN-01",
        "P-SKX-01",
        "P-SNS-01",
        "P-SNS-02"
      ],
      "content_sha256": "040b1332986379c86ebba6a68c76630e6cce3e34cd664b4ed384a7dafe621cad",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 040b13329863); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-31c2ac5b48b0cde3",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/vernetzte-flugabwehr-skynex",
        "content_sha256": "040b1332986379c86ebba6a68c76630e6cce3e34cd664b4ed384a7dafe621cad",
        "text_sha256": "c0d00b18c104a83ad2311fd59cfc0ca8dfe97b8202b3295e9f9cf256055d457c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-39222fba59e057e4",
      "claim_ids": [
        "C-016"
      ],
      "content_sha256": "f35f392c6fd1a8e50be14e968d9c95a84551ccc23e2e40ee61af7704366507e3",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt f35f392c6fd1); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-39222fba59e057e4",
        "url": "https://defence-network.com/der-skyranger-kommt-nur-nicht-in-deutschland/",
        "content_sha256": "f35f392c6fd1a8e50be14e968d9c95a84551ccc23e2e40ee61af7704366507e3",
        "text_sha256": "02ff770ae24c054480fe78ac085009cf8a634cd98be5e5a12ea4187135dd8c32",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-397e8414020bdb92",
      "claim_ids": [
        "M-DE-SKR-02",
        "M-DK-SKR-01",
        "M-IT-A2CS-01",
        "M-NL-SKR-01",
        "M-SKR30-ARCH-01"
      ],
      "content_sha256": "30f7d4fb7b61fb9c18d9b3979bd65565ce664806abde674764da4b7f241d0ddc",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 30f7d4fb7b61); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-397e8414020bdb92",
        "url": "https://suv.report/skyranger-30-technische-daten-bestellungen-und-interessenten/",
        "content_sha256": "30f7d4fb7b61fb9c18d9b3979bd65565ce664806abde674764da4b7f241d0ddc",
        "text_sha256": "7a88c3650d476017e467a811c9bdde8d541358cbf1c5e4d1c0796a6057d8b4ea",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3b27cf3712ca73d2",
      "claim_ids": [
        "C-025",
        "T-EV-05"
      ],
      "content_sha256": "821dd1bce62ab04d8157be99c29450da5556efcc67fc7b38407839e821c3f0ca",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 821dd1bce62a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3b27cf3712ca73d2",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-23-rheinmetall-hands-over-first-skynex-system-to-italy",
        "content_sha256": "821dd1bce62ab04d8157be99c29450da5556efcc67fc7b38407839e821c3f0ca",
        "text_sha256": "4c774276e64a0a8e6bd28963eb41e972ace886a1cde7f9f37f5e3b262cc18ae6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3b33c5118cdc79d2",
      "claim_ids": [
        "T-EV-08"
      ],
      "content_sha256": "c6d13e5f66762ec7446f9af512c82714dd3b81e3f5df0dcd8d40d187dc6a0e59",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt c6d13e5f6676); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
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
      "source_id": "S-3ba304da81a26074",
      "claim_ids": [
        "T-ID-05"
      ],
      "content_sha256": "79103aee21cd71e01a3ab7052b868fcba5b18d067aacda35929cbc374bfe1ee0",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 79103aee21cd); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3ba304da81a26074",
        "url": "https://www.rheinmetall.com/de/investor-relations/aktie/kurs",
        "content_sha256": "79103aee21cd71e01a3ab7052b868fcba5b18d067aacda35929cbc374bfe1ee0",
        "text_sha256": "cfa0ce05669d21e22536853a8030901aee18b23868322ee7eab434abdb5205ca",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3c0148ccd2c8eee9",
      "claim_ids": [
        "C-039"
      ],
      "content_sha256": "a38fae985fd6e10cc0a4d7a001a3cc6acc07b39c2d4138bcd702bc28c7d27623",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt a38fae985fd6); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3c0148ccd2c8eee9",
        "url": "https://www.leonardo.com/documents/15646808/30043445/Integrated+Report+2025.pdf/fcf56c7d-8f61-780c-5fb8-b130d6aeacf8?t=1773421399076",
        "content_sha256": "a38fae985fd6e10cc0a4d7a001a3cc6acc07b39c2d4138bcd702bc28c7d27623",
        "text_sha256": "f8a51240f805329dde4d9cc99b75362c906cbcdc6fce7c713819afb869a7fba6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-3c3ad4b4354adf5e",
      "claim_ids": [
        "C-019"
      ],
      "content_sha256": "b76cd63e3f826ac2f387b8fd227cfb3de495e20e5e7b3c412a8946e1c9b86dc3",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt b76cd63e3f82); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3c3ad4b4354adf5e",
        "url": "https://orf.at/stories/3349582/",
        "content_sha256": "b76cd63e3f826ac2f387b8fd227cfb3de495e20e5e7b3c412a8946e1c9b86dc3",
        "text_sha256": "f4240b2ddd221e5b249efbc0c131e4af6a362fd55d9df39f83a2378ac460a1cf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3cb560602baefeec",
      "claim_ids": [
        "P-REG-AU-01"
      ],
      "content_sha256": "36ac5a680eba2d8faf1ddbe6118a69c5fe9cf7730cac9fbe7a84df0b58d15331",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 36ac5a680eba); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3cb560602baefeec",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-defence-australia",
        "content_sha256": "36ac5a680eba2d8faf1ddbe6118a69c5fe9cf7730cac9fbe7a84df0b58d15331",
        "text_sha256": "a0f58cd86ea1598b3c65b9a9e76e66ea3c7a7bd7f8b3c77ddf85038692eb090a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3d1ac94ea50adfec",
      "claim_ids": [
        "M-DK-IRIS-01",
        "M-SE-IRIS-01"
      ],
      "content_sha256": "b9d93b1676f97ccd53128fa79788cf48972764e6c6b7e3a97d6234e2f4600cc9",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt b9d93b1676f9); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3d1ac94ea50adfec",
        "url": "https://euro-sd.com/2025/12/major-news/48184/sweden-orders-more-iris-t-sls/",
        "content_sha256": "b9d93b1676f97ccd53128fa79788cf48972764e6c6b7e3a97d6234e2f4600cc9",
        "text_sha256": "dc8a8362d1216b9506fa8b49424255bb11a18c0f27860df585b2519b478b01c7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3dad8b811c925694",
      "claim_ids": [
        "C-003",
        "C-011",
        "C-024",
        "C-043",
        "C-044",
        "C-046",
        "P-AD-07",
        "P-DS-03",
        "P-NS-02",
        "P-REG-HR-01",
        "P-REG-RO-01",
        "P-STR-02",
        "P-STR-03",
        "T-EMP-02",
        "T-EV-03"
      ],
      "content_sha256": "214decfe1cd910eedff5de83482a93f410fb63d3e92a852c34d543790d07098c",
      "capture_kind": "http-original",
      "note": "Halbjahresfinanzbericht 2026 (PDF) gelesen: Kennzahlenübersicht Personal S. 2, Wesentliche Ereignisse S. 8–11 (NVL-Erwerb 27.02.2026, Zivilverkauf AEQH40, DOK-ING, Kraken, FV-014, Puma, Rumänien), Segment Air Defence S. 17. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
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
      "source_id": "S-3ef169e9e35e0c9a",
      "claim_ids": [
        "P-AD-01",
        "P-AD-02",
        "P-AD-03"
      ],
      "content_sha256": "4afebd8d605d7dddf8a91ce5c4d77c879d33fc533d4bc91208e62498ee36fa99",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 4afebd8d605d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3ef169e9e35e0c9a",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/air-defence",
        "content_sha256": "4afebd8d605d7dddf8a91ce5c4d77c879d33fc533d4bc91208e62498ee36fa99",
        "text_sha256": "52e7c3078393c018b6cc17c1aaaf2684665672866e7852e041d69a261faa3fbf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3f67bc2e13a1b02e",
      "claim_ids": [
        "C-007",
        "C-026",
        "C-027"
      ],
      "content_sha256": "04017585d62b62721a4c169ad3f827deab78403327cb45e8b6b7feb0164c4894",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 04017585d62b); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-3f67bc2e13a1b02e",
        "url": "https://www.rheinmetall.com/en/media/stories/2026/rheinmetall-a-powerful-partner-at-ukraine-side",
        "content_sha256": "04017585d62b62721a4c169ad3f827deab78403327cb45e8b6b7feb0164c4894",
        "text_sha256": "ef98bb3e368dda0afa8b2ef50087d18c607c2a2fbe58b52141569000a9d1afc8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-47771a7dd8c927d5",
      "claim_ids": [
        "P-REG-US-01",
        "P-VS-04",
        "P-VS-05"
      ],
      "content_sha256": "b913794ff36558b9b142e371b234b86dc393c9a53b345d13e9f69f5cbab00d86",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt b913794ff365); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-47771a7dd8c927d5",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/10/2026-10-12-american-rheinmetall-auf-der-ausa-2026",
        "content_sha256": "b913794ff36558b9b142e371b234b86dc393c9a53b345d13e9f69f5cbab00d86",
        "text_sha256": "3a37873207d32b068f0f74131f42b1fffcee809e984c0b081eff4fc34951b5d9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4789a4ac6acb59aa",
      "claim_ids": [
        "T-AD-04",
        "T-EV-04"
      ],
      "content_sha256": "69985ee16ab480477ab94ad0f7bf1d2a0291b44639496c2beaac645481be03dc",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 69985ee16ab4); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-4789a4ac6acb59aa",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/12/2025-12-12-rheinmetall-liefert-skyranger-30-fuer-die-niederlaendischen-streitkraefte",
        "content_sha256": "69985ee16ab480477ab94ad0f7bf1d2a0291b44639496c2beaac645481be03dc",
        "text_sha256": "e1b32dadc21850aff57693081213be2e3491384c6a876aa17bdb8d8df1eb6503",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-479bad9fdf088fc9",
      "claim_ids": [
        "P-REG-HU-01"
      ],
      "content_sha256": "80da10dcc2ec390fff9eacb003c122b68b8dc8648ab6bc576632e5a493403f77",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 80da10dcc2ec); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-479bad9fdf088fc9",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-hungary-zrt",
        "content_sha256": "80da10dcc2ec390fff9eacb003c122b68b8dc8648ab6bc576632e5a493403f77",
        "text_sha256": "22a15ae374d2e75c0a59891b934886f9b3f35922eb90ba442711c6bde78b67a0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4a13b2786b5cc66a",
      "claim_ids": [
        "C-054",
        "M-DE-ARM-01",
        "P-VS-04"
      ],
      "content_sha256": "3d373c4b9a1cf63deb198ce8b1ca271b99a8cfb187c10744ac4ba53b9df1a301",
      "capture_kind": "http-original",
      "note": "Q3-Recap 05.10.2026 gelesen: XM30-Prototypen September, Arminius-Festvertrag bis Jahresende erwartet, Q3-Termin 05.11.2026, Investitionsschwerpunkte. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-4a13b2786b5cc66a",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2026/Q3/2026-10-05-Rheinmetall-Q3-Analyst-and-Investor-Recap-Document.pdf",
        "content_sha256": "3d373c4b9a1cf63deb198ce8b1ca271b99a8cfb187c10744ac4ba53b9df1a301",
        "text_sha256": "a47a318dc251a31720857c2324d943f22df48bda2dad6bb72a100bedd44311a3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-4d0e53f502fb320c",
      "claim_ids": [
        "P-REG-DE-01",
        "P-STR-01"
      ],
      "content_sha256": "6d21580346dad51ccc38482d41f787c9e90783704c776018d63b2b0d0eca5923",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 6d21580346da); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-4d0e53f502fb320c",
        "url": "https://www.rheinmetall.com/de/unternehmen",
        "content_sha256": "6d21580346dad51ccc38482d41f787c9e90783704c776018d63b2b0d0eca5923",
        "text_sha256": "f40cc178fd92cbda0f529683dad7ec1dc96bd7a1f3355230e5b598f74bb68d03",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4e85b953fe46a8de",
      "claim_ids": [
        "M-PL-PIL-02"
      ],
      "content_sha256": "dd5daa36815d203d68b6bae088d924d18cb91d8a5104be978506967a926002db",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt dd5daa36815d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-4e85b953fe46a8de",
        "url": "https://militarnyi.com/en/news/poland-receives-first-short-range-air-defense-system-under-pilica-program/",
        "content_sha256": "dd5daa36815d203d68b6bae088d924d18cb91d8a5104be978506967a926002db",
        "text_sha256": "cbdcc1a2a2c6c6b6c27b4ae3a5d3b6d09a35968c898d33a20763ec9e615a6139",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4f9807383dbfe574",
      "claim_ids": [
        "P-REG-CA-01"
      ],
      "content_sha256": "e7da0e621a8a87cfafe80f56f8a81ec418ec8cc10938bb8c4152402714bc8ac9",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt e7da0e621a8a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-4f9807383dbfe574",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-canada/ueber-uns",
        "content_sha256": "e7da0e621a8a87cfafe80f56f8a81ec418ec8cc10938bb8c4152402714bc8ac9",
        "text_sha256": "c31572edc271f13a5a719734d1a86d9c513c27fb101919e357413281fc1cc6b1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4faa3a733781f031",
      "claim_ids": [
        "P-SKM-01"
      ],
      "content_sha256": "b1f44c4b967d5ebb494ad76ed8a125a0671f964dd3b1f183bf5743cc06bde661",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt b1f44c4b967d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-4faa3a733781f031",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/fuehrungssysteme-skymaster",
        "content_sha256": "b1f44c4b967d5ebb494ad76ed8a125a0671f964dd3b1f183bf5743cc06bde661",
        "text_sha256": "2a13145aed9fe1143f5c2c4ac0bed1b9c6aea2900a0f53a0592eb749e929b776",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-502271d8acddfb1e",
      "claim_ids": [
        "C-030"
      ],
      "content_sha256": "ced56c7b4fc2e29998f97d7cbc28cc99410794c08a6de22f818a14b90db9f2f4",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt ced56c7b4fc2); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-502271d8acddfb1e",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/06/2024-06-19-rad-and-anduril-industries-sign-mou",
        "content_sha256": "ced56c7b4fc2e29998f97d7cbc28cc99410794c08a6de22f818a14b90db9f2f4",
        "text_sha256": "90af2ee4b5445ea0d061b3e52d71b109fc7d341d83098240394e12d4b63ae55b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-504b2773565ae51b",
      "claim_ids": [
        "M-DIEHL-01"
      ],
      "content_sha256": "51ab350e5085c623f4fa7ed5f77eb571c779a8b738ae8164524ae819a833607c",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 51ab350e5085); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-504b2773565ae51b",
        "url": "https://euro-sd.com/2026/01/major-news/48772/new-diehl-production-site/",
        "content_sha256": "51ab350e5085c623f4fa7ed5f77eb571c779a8b738ae8164524ae819a833607c",
        "text_sha256": "e3596b73d13ba857a440449b2a62437812a697ab2951d71d6da81b3429f024be",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-513daa2ae2be3e14",
      "claim_ids": [
        "P-AHD-01",
        "P-SKR-06",
        "P-SKX-04"
      ],
      "content_sha256": "a67590ae0f4f8979eefb6d93b145a2440c14e0d24cc971d8201444bbfa96a4bf",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt a67590ae0f4f); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-513daa2ae2be3e14",
        "url": "https://www.rheinmetall.com/de/media/stories/2026/rheinmetall-ein-starker-partner-an-der-seite-der-ukraine",
        "content_sha256": "a67590ae0f4f8979eefb6d93b145a2440c14e0d24cc971d8201444bbfa96a4bf",
        "text_sha256": "6328672f740e7faa85995c54f8b29d40d85eff7d317b2ee7b7d2215665409dec",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-51d8de61559f69f0",
      "claim_ids": [
        "M-EU-SAFE-UK-01"
      ],
      "content_sha256": "0993d44f976cda3ff3852b093b0e68ad9f05e3dd93b0323fe54faa1348a3d91c",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 0993d44f976c); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-51d8de61559f69f0",
        "url": "https://defenceleaders.com/news/uk-eu-defence-fund-talks-collapse/",
        "content_sha256": "0993d44f976cda3ff3852b093b0e68ad9f05e3dd93b0323fe54faa1348a3d91c",
        "text_sha256": "27821d39d0bb66eadf9109e853bd3ea9ea1457cf04a4f2a37ba4804b09b71506",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5366eb8816ff2cea",
      "claim_ids": [
        "C-031"
      ],
      "content_sha256": "75cf397990ec8ca99b2381b5c09f6238019ce78b3b1f7a628308c8a29003328c",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 75cf397990ec); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-5366eb8816ff2cea",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/06/2025-06-18-strategic-partnership",
        "content_sha256": "75cf397990ec8ca99b2381b5c09f6238019ce78b3b1f7a628308c8a29003328c",
        "text_sha256": "2c2f35931551109dfe04dcb9a3e7202be60568a0dded652ed6e91f837ee00a76",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5a9d049f8f71abd3",
      "claim_ids": [
        "C-050"
      ],
      "content_sha256": "46169a0ab9c3e0d3c5986cccf5395588ac96fc50cfbf191d4eb29a7531f36f9a",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 46169a0ab9c3); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-5a9d049f8f71abd3",
        "url": "https://esut.de/2026/09/meldungen/74575/roman-koehne-ceo-rheinmetall-air/",
        "content_sha256": "46169a0ab9c3e0d3c5986cccf5395588ac96fc50cfbf191d4eb29a7531f36f9a",
        "text_sha256": "32e3643ab7c41c4581d5de07f61b38ed4deb734c47a6e568351d229abdcfde66",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5ae98f51c19ce9e2",
      "claim_ids": [
        "P-SKR-01"
      ],
      "content_sha256": "518dfd21f82f3eba8bdf70ef8834f87a13cbfc29dbe330d42443fa5514c51f03",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 518dfd21f82f); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-5ae98f51c19ce9e2",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/mobile-flugabwehr-skyranger",
        "content_sha256": "518dfd21f82f3eba8bdf70ef8834f87a13cbfc29dbe330d42443fa5514c51f03",
        "text_sha256": "c6c6a4d0cb3faa4ec989b604ba5e10e0ebb3a79066346af6a7bbc458f50bcb1e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5b8b39f37cd6b51d",
      "claim_ids": [
        "P-SVC-01"
      ],
      "content_sha256": "cd16054e8bfec77b10ee93b6b7c014530ce55382065ba4770326c0b067c3a07e",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt cd16054e8bfe); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-5b8b39f37cd6b51d",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme",
        "content_sha256": "cd16054e8bfec77b10ee93b6b7c014530ce55382065ba4770326c0b067c3a07e",
        "text_sha256": "bd474cb6b650ed57c6e6848641f439d237867fada04bd7878c24263196db88b2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5ba566671c688dae",
      "claim_ids": [
        "M-DK-VLM-01"
      ],
      "content_sha256": "efcfae13d46ac47938affea6458afe357293c79d82c07be76dd0fee76b39e8f9",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt efcfae13d46a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-5ba566671c688dae",
        "url": "https://thedefensepost.com/2025/07/28/denmark-vl-mica-procurement/",
        "content_sha256": "efcfae13d46ac47938affea6458afe357293c79d82c07be76dd0fee76b39e8f9",
        "text_sha256": "f1db615b969f269290a922246ec7af2da10c26fd834353620b5820804c47e9fb",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5bb9a49af968005c",
      "claim_ids": [
        "H-PP-06"
      ],
      "content_sha256": "5e564f3c06bae5e913389f3df705505950ade6c96a7b7b89a4af6841ee6a65af",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 5e564f3c06ba); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-5bb9a49af968005c",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/11/2024-11-06-umbildung-des-rheinmetall-vorstands",
        "content_sha256": "5e564f3c06bae5e913389f3df705505950ade6c96a7b7b89a4af6841ee6a65af",
        "text_sha256": "b521064ba386fd35ac843474a7002f67abb8468864b3578448bd09cf83db2b96",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5dad3a27cd832a61",
      "claim_ids": [
        "P-REG-LT-01"
      ],
      "content_sha256": "52992260fe4717756ef8269eefc7d84fe293002a425b9fee2ad1c7d1fea23e36",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 52992260fe47); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-5dad3a27cd832a61",
        "url": "https://investlithuania.com/news/groundbreaking-ceremony-in-baisogala-rheinmetall-and-lithuania-build-artillery-ammunition-plant-on-natos-eastern-flank/",
        "content_sha256": "52992260fe4717756ef8269eefc7d84fe293002a425b9fee2ad1c7d1fea23e36",
        "text_sha256": "c3876559a998b611c18b0402657418ad35ea31ee9d884d85cc65d0f2b8e54436",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5f102cfea2da2738",
      "claim_ids": [
        "H-PP-01",
        "P-AD-07",
        "P-NS-03",
        "P-REG-UK-01",
        "P-VS-03",
        "T-AD-01",
        "T-EV-03",
        "T-EV-09",
        "T-FIN-04",
        "T-FIN-05",
        "T-FIN-06",
        "T-FIN-07",
        "T-FIN-08",
        "T-FIN-09",
        "T-SEG-01"
      ],
      "content_sha256": "70b17f8f578df934e3a6d2bf8631acf980f14b940352268a45f613d3e8ca2113",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 70b17f8f578d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
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
      "source_id": "S-60677f3d57da054d",
      "claim_ids": [
        "C-022"
      ],
      "content_sha256": "f75985927db8167f44b7231cc35b89d0a5844ea7535d7d9eabafc36c2dc18e66",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt f75985927db8); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-60677f3d57da054d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-12-rheinmetall-to-supply-skyranger-30-for-the-dutch-armed-forces",
        "content_sha256": "f75985927db8167f44b7231cc35b89d0a5844ea7535d7d9eabafc36c2dc18e66",
        "text_sha256": "3cf6f93016c17d8c81bf364fab7ed21f1d7fee1ebf3bce32ae9137bdd6c67098",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6282cce4ae4b577f",
      "claim_ids": [
        "C-017"
      ],
      "content_sha256": "00421d7b86b7f0166d9ff9dff27d5f69492417cd49d4ab64fbf34c4677c02463",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 00421d7b86b7); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-6282cce4ae4b577f",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/06/2024-06-05-rheinmetall-mbda-small-anti-drone-missile",
        "content_sha256": "00421d7b86b7f0166d9ff9dff27d5f69492417cd49d4ab64fbf34c4677c02463",
        "text_sha256": "01dda3028f6509e01338118e4968d8ecda394419c22eb3bc4c7fe28656b8d2e3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-63ef3755ffe55169",
      "claim_ids": [
        "M-MKT-SIPRI-00"
      ],
      "content_sha256": "ad34fa9059b3e22ed4d2a9f1a53b23b2defe4d4e5ac7536b683c8aa868e51cb4",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt ad34fa9059b3); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-63ef3755ffe55169",
        "url": "https://www.sipri.org/databases/milex",
        "content_sha256": "ad34fa9059b3e22ed4d2a9f1a53b23b2defe4d4e5ac7536b683c8aa868e51cb4",
        "text_sha256": "db02b58ab0ba7892c390471b5dca1085ee56a584606723c70e724644d13617ab",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6410acb24c745d46",
      "claim_ids": [
        "P-SKR-03",
        "P-SKR-04"
      ],
      "content_sha256": "8524f2971bcdf584338fb4bed72387433033effc99ee88385eeef9c9c536054e",
      "capture_kind": "http-original",
      "note": "S&V 15.06.2026 vollständig gelesen (Beschaffung im Detail, Gründe der Verzögerung, Zwischenlösung). Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-6410acb24c745d46",
        "url": "https://suv.report/skyranger-30-auslieferung-ab-q4-2027/",
        "content_sha256": "8524f2971bcdf584338fb4bed72387433033effc99ee88385eeef9c9c536054e",
        "text_sha256": "5559dc779e1a9fd9b2a59339f4f1355d4daa3bc4e1480167ec5b08c37f6d1658",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6a3c2e1e456f2080",
      "claim_ids": [
        "M-EU-SAFE-02"
      ],
      "content_sha256": "600bbe33f593976e06df929b670a5597fcc64c47e0bced6edfc504fb89633ab2",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 600bbe33f593); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-6a3c2e1e456f2080",
        "url": "https://www.aoshearman.com/en/insights/safe-update-financial-assistance-tentative-allocation",
        "content_sha256": "600bbe33f593976e06df929b670a5597fcc64c47e0bced6edfc504fb89633ab2",
        "text_sha256": "fc80979482d94bb91197f0eb8966db39184d501563b8355ee5f03f5cdf08a990",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6af38e87216bc1d2",
      "claim_ids": [
        "C-033"
      ],
      "content_sha256": "f6b4c9243cf766edb3cb6eb5793f430934d6752cf346c2d77e468e142a26f35a",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt f6b4c9243cf7); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-6af38e87216bc1d2",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/04/lockheed-martin-and-rheinmetall-to-join-forces-on-centre-of-excellence-for-european-security",
        "content_sha256": "f6b4c9243cf766edb3cb6eb5793f430934d6752cf346c2d77e468e142a26f35a",
        "text_sha256": "f526b4ef05b1cff84c3c10ed164fdaec7814016759a1bab30c11c1b7d28cfc48",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6bdb338d23c29e11",
      "claim_ids": [
        "C-024",
        "T-AD-04",
        "T-EV-07"
      ],
      "content_sha256": "a1f7e7677f9f28ad89c100b24bf6841d199f090f7eaac446a154c9573551adc1",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt a1f7e7677f9f); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-6bdb338d23c29e11",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-24-romania-orders-skyranger-35-air-defence-systems-from-rheinmetall",
        "content_sha256": "a1f7e7677f9f28ad89c100b24bf6841d199f090f7eaac446a154c9573551adc1",
        "text_sha256": "36a80477eeee22ffbe069b4468e9a652625ae107190bdbb222f5ab9904d14e4b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6ceae77f0e11c121",
      "claim_ids": [
        "C-028",
        "P-CUAS-02"
      ],
      "content_sha256": "23ace4714ef858ecd6f2245de5d8f35bfc8599d111a647b70d28cb8183f3c1c5",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 23ace4714ef8); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-6ceae77f0e11c121",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-16-rheinmetall-demonstrates-drone-defence-capabilities-in-finland",
        "content_sha256": "23ace4714ef858ecd6f2245de5d8f35bfc8599d111a647b70d28cb8183f3c1c5",
        "text_sha256": "a63616902cef972feae74feb4343115bd094e9e9c8b21a0af903b6a2dc15ab51",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6d57eca962a765ae",
      "claim_ids": [
        "C-034"
      ],
      "content_sha256": "950bc29ce9003aff894195078cfd3b58338fe701861df7d7acd8f011431c5a2d",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 950bc29ce900); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-6d57eca962a765ae",
        "url": "https://news.lockheedmartin.com/2026-07-07-Lockheed-Martin-and-Rheinmetall-Move-Forward-with-ATACMS-Co-Production-in-Europe",
        "content_sha256": "950bc29ce9003aff894195078cfd3b58338fe701861df7d7acd8f011431c5a2d",
        "text_sha256": "c379f7233aa5f4aa30bd83809009c8fdfe9b195231431267237a6ce3b8228d53",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7066a889ca7eaad4",
      "claim_ids": [
        "C-009"
      ],
      "content_sha256": "865da018ab2643a8718341a6ffaafc3f596c01fcdb128098a6e537c6bd4b425f",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 865da018ab26); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-7066a889ca7eaad4",
        "url": "https://investors.hensoldt.net/media/document/1e6664b4-3343-4297-837a-3924a62fd59c/assets/DE000HAG0005-JA-2025-EQ-D-00.pdf",
        "content_sha256": "865da018ab2643a8718341a6ffaafc3f596c01fcdb128098a6e537c6bd4b425f",
        "text_sha256": "6148364d536233399972c4f78098268bd2f66bb4067622367bbd5b265b26e52b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-747870b3bc879dff",
      "claim_ids": [
        "P-PS-01"
      ],
      "content_sha256": "cb1d3a52c7834601cc165cde1d07b47535aabc57a5dcadc93315b6ca182b483f",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt cb1d3a52c783); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-747870b3bc879dff",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/power-systems",
        "content_sha256": "cb1d3a52c7834601cc165cde1d07b47535aabc57a5dcadc93315b6ca182b483f",
        "text_sha256": "59bd225aa877fa350166c27abdbd0fe9ff79926daa73898397415b3282bd418c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-764b0868c9a4f470",
      "claim_ids": [
        "M-DK-SAMPT-01"
      ],
      "content_sha256": "3438ab3e7e4770d93ab45fa13feeb18a2d2e0ae01e8725457c4ce27609bf60be",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 3438ab3e7e47); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-764b0868c9a4f470",
        "url": "https://www.army-technology.com/news/denmark-samp-t-ng-defence-contract/",
        "content_sha256": "3438ab3e7e4770d93ab45fa13feeb18a2d2e0ae01e8725457c4ce27609bf60be",
        "text_sha256": "8acff946e6ff1ae6354a82d8f494324157bd038d97afee1b5e3ecb734e5e9b88",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-76d1cd6d4bfaa83c",
      "claim_ids": [
        "H-PP-09",
        "T-AD-02",
        "T-AD-03",
        "T-STR-01"
      ],
      "content_sha256": "c7e6d1442db883fc57fd0376aa962d8ebe202cbe0cb04844ba59f57eee1a1420",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt c7e6d1442db8); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-76d1cd6d4bfaa83c",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Termine/Capital%20Markets%20Day/2025/Rheinmetall-CMD-2025-Presentation.pdf",
        "content_sha256": "c7e6d1442db883fc57fd0376aa962d8ebe202cbe0cb04844ba59f57eee1a1420",
        "text_sha256": "7a48752d4efc34af4b873f8a34db5f879042fd7bab8b878279272a4d35e008a6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-77116a48034eea1f",
      "claim_ids": [
        "M-DK-SKR-01"
      ],
      "content_sha256": "4f36a1499507aad5e7d66b6ca8986eb0df0895a1fa50b3e6c0f1d57c97dd2050",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 4f36a1499507); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-77116a48034eea1f",
        "url": "https://esut.de/2024/09/meldungen/53536/ergaenzung-zur-daenischen-bestellung-von-skyranger-30/",
        "content_sha256": "4f36a1499507aad5e7d66b6ca8986eb0df0895a1fa50b3e6c0f1d57c97dd2050",
        "text_sha256": "6ad004ef3f318bf88b46a5f92d53775d6c0f3510de1ad8f80e212f6c785bdd68",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7730735b980263ed",
      "claim_ids": [
        "M-MKT-SIPRI-00",
        "M-MKT-SIPRI-AT",
        "M-MKT-SIPRI-DE",
        "M-MKT-SIPRI-DK",
        "M-MKT-SIPRI-IT",
        "M-MKT-SIPRI-NL",
        "M-MKT-SIPRI-PL",
        "M-MKT-SIPRI-RO",
        "M-MKT-SIPRI-SE",
        "M-MKT-SIPRI-UK"
      ],
      "content_sha256": "6cc3a30b1064f9f02e60236667eef82e08cad42910ce630909d004ad2c398a9d",
      "capture_kind": "http-original",
      "note": "SIPRI-XLSX v1.2 als Original mit openpyxl ausgewertet (Werte, Schriftfarbe, Fußnotenblatt). Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-7730735b980263ed",
        "url": "https://www.sipri.org/sites/default/files/SIPRI-Milex-data-1949-2025_v1.2.xlsx",
        "content_sha256": "6cc3a30b1064f9f02e60236667eef82e08cad42910ce630909d004ad2c398a9d",
        "text_sha256": null,
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Unsupported text extraction; original bytes retained."
      }
    },
    {
      "source_id": "S-7b3ad8192958d374",
      "claim_ids": [
        "C-041",
        "C-042"
      ],
      "content_sha256": "cc39e0e7a65a5f8c0b064c80b1d0eb6408c78fe62c7379e3b65ffd591dca1880",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt cc39e0e7a65a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-7b3ad8192958d374",
        "url": "https://www.iceye.com/newsroom/press-releases/iceye-and-rheinmetall-win-major-contract-worth-billions-for-space-reconnaissance",
        "content_sha256": "cc39e0e7a65a5f8c0b064c80b1d0eb6408c78fe62c7379e3b65ffd591dca1880",
        "text_sha256": "a05f94a884eeb8a3b5bbd960c17b40f0580a62c0b0f7ae274ade1d9b7850b6a7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7c3ae12304f6c154",
      "claim_ids": [
        "C-019",
        "M-AT-SKR-02"
      ],
      "content_sha256": "6443f41f5ba7379ab67d969c4e37510b4e73fd74ce27848a1ad199d959f20abd",
      "capture_kind": "http-original",
      "note": "PM 23.02.2024 gelesen: Rheinmetall Unterauftragnehmer von GDELS, 36 Systeme, Mistral, Skyguard NG (Dez. 2023) – relevant auch für C-019/Netz. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-7c3ae12304f6c154",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/02/2024-02-23-rheinmetall-liefert-skyranger-30-an-oesterreich",
        "content_sha256": "6443f41f5ba7379ab67d969c4e37510b4e73fd74ce27848a1ad199d959f20abd",
        "text_sha256": "5cfabee3c90a70c1e7ea8405ab570b7ed08525a5306e1ce50d6342d83c116e37",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7d3cceefdfc28f58",
      "claim_ids": [
        "P-REG-ES-01"
      ],
      "content_sha256": "96e9e274cf308f658e4fa7daf41fe7c3f844cd09920101e0dcdaa0ff8726fc89",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 96e9e274cf30); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-7d3cceefdfc28f58",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-expal-munitions",
        "content_sha256": "96e9e274cf308f658e4fa7daf41fe7c3f844cd09920101e0dcdaa0ff8726fc89",
        "text_sha256": "3671bf9b2bedd20cc67ca04f2def0e5c6e62695aaa0f5bb53ecf08c189464cc7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8004062626d5c0ad",
      "claim_ids": [
        "P-DS-01",
        "P-REG-ME-01"
      ],
      "content_sha256": "22d7a94163c36b61f25ff63ecec507bb565c42590eb88b4306dbcc5cab3f07c6",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 22d7a94163c3); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-8004062626d5c0ad",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/digital-systems",
        "content_sha256": "22d7a94163c36b61f25ff63ecec507bb565c42590eb88b4306dbcc5cab3f07c6",
        "text_sha256": "97784dba5d5252da32f80a873ef84bf487a58258c1c5b9fc460bce8c9944b706",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8119028d88f698cb",
      "claim_ids": [
        "C-018"
      ],
      "content_sha256": "149e01c8c15c7a371a996f4a3e72c0aa5dfdcabb9983cf10a8b878f6cac4acc0",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 149e01c8c15c); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-8119028d88f698cb",
        "url": "https://esut.de/2025/11/meldungen/65265/neue-distanzwirkung-im-nahbereich-defendair-kommt/",
        "content_sha256": "149e01c8c15c7a371a996f4a3e72c0aa5dfdcabb9983cf10a8b878f6cac4acc0",
        "text_sha256": "2b63a20d9bef16bfc2fadac0d627b8b8953dcae0af09c5f3d92b186aa833aae3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-827c64d441de8f6e",
      "claim_ids": [
        "P-REG-NORD-01",
        "T-FIN-01",
        "T-FIN-02",
        "T-FIN-03",
        "T-FIN-04",
        "T-FIN-08",
        "T-SEG-01"
      ],
      "content_sha256": "4b2645d68352518aed6f3f683e7b87dc3c4493ebc65153223fd9c45d20939f49",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 4b2645d68352); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-827c64d441de8f6e",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/03/2026-03-11-Rheinmetall-Bilanzvorlage-Geschaeftsjahr-2025.pdf",
        "content_sha256": "4b2645d68352518aed6f3f683e7b87dc3c4493ebc65153223fd9c45d20939f49",
        "text_sha256": "9772d758abafc585b115b484b9f68777582e0b6daec998886faf3917e7f7938c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-829c43465e63a592",
      "claim_ids": [
        "M-EU-EDIP-01"
      ],
      "content_sha256": "6007e13e6c0b195a6887afb6d331c9fbed95aa13402cfea0d2f9e663f3b9c68b",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 6007e13e6c0b); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-829c43465e63a592",
        "url": "https://www.eeas.europa.eu/delegations/ukraine/european-defence-industry-programme-council-gives-final-approval_en",
        "content_sha256": "6007e13e6c0b195a6887afb6d331c9fbed95aa13402cfea0d2f9e663f3b9c68b",
        "text_sha256": "6303967fe8bd14f89f4ba44b60974026cfd76ce7ea21bad74371205de0c6f7a9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-84a5e99e7ff45dc4",
      "claim_ids": [
        "M-AT-SKR-01"
      ],
      "content_sha256": "95b4201e2875233806879c80d56b7a627429a641d9a24143911ba5c8f4fb9dde",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 95b4201e2875); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-84a5e99e7ff45dc4",
        "url": "https://militaeraktuell.at/en/pandur-evolution-with-skyranger-for-the-anti-aircraft-batteries/",
        "content_sha256": "95b4201e2875233806879c80d56b7a627429a641d9a24143911ba5c8f4fb9dde",
        "text_sha256": "ecfc20a98b7e2471ac90b7d6d72a45fd15e288c66abb48be5ba8dd8127e57921",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-860fb5a5ec516912",
      "claim_ids": [
        "P-CUAS-01",
        "P-SKM-01"
      ],
      "content_sha256": "68e577e87fa19b4c6098d406ddbc9297ea2d3a3cb5466b1f8825d63c07a98176",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 68e577e87fa1); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-860fb5a5ec516912",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/drohnenabwehr-toolbox",
        "content_sha256": "68e577e87fa19b4c6098d406ddbc9297ea2d3a3cb5466b1f8825d63c07a98176",
        "text_sha256": "449a35754dab144b73af4ded2a35c67583ae8ca720389a5109060a198f8f1078",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-879737fc228c4bec",
      "claim_ids": [
        "M-DE-NNBS-01"
      ],
      "content_sha256": "043d07181531c75b46c0feae11587e3f3294067886fdca2cf4cc33cc403ab7cf",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 043d07181531); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-879737fc228c4bec",
        "url": "https://esut.de/2026/09/meldungen/streitkraefte/75038/zwoelf-25-mio-bundeswehr/",
        "content_sha256": "043d07181531c75b46c0feae11587e3f3294067886fdca2cf4cc33cc403ab7cf",
        "text_sha256": "be842f2609f566f14624abed03c02f522470051420842424ed440cc205648163",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-92d7be3f0dda7317",
      "claim_ids": [
        "P-HEL-01"
      ],
      "content_sha256": "21c3a52cb14e3496586952b615ab0616922480ec6cc37cca903bee9796ccdb84",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 21c3a52cb14e); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-92d7be3f0dda7317",
        "url": "https://esut.de/2026/07/meldungen/72696/rheinmetall-und-mbda-realisieren-das-laserwaffensystem-fuer-die-deutsche-marine/",
        "content_sha256": "21c3a52cb14e3496586952b615ab0616922480ec6cc37cca903bee9796ccdb84",
        "text_sha256": "214558e7f2f3539b022885e9d2db5af075b275b94012bb1e42ec2bd29c028a8c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-931d769d72f5fc8d",
      "claim_ids": [
        "T-EV-09"
      ],
      "content_sha256": "037c66f74678ae8d4339ec137141cb37aefa5487868f1127457d26f9f4100a47",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 037c66f74678); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-931d769d72f5fc8d",
        "url": "https://www.euronews.com/business/2026/06/24/rheinmetall-sinks-as-germany-axes-mega-warship-project-after-spending-2bn",
        "content_sha256": "037c66f74678ae8d4339ec137141cb37aefa5487868f1127457d26f9f4100a47",
        "text_sha256": "3008590aa48add899a86781e48b48bf61d5a79ee15756e028c7f5fa5852fd086",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-93a2ee05910f4b53",
      "claim_ids": [
        "P-NS-01"
      ],
      "content_sha256": "86904b8007dd17cd63afd9a77b63208003920601188250edb982e26e00a61593",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 86904b8007dd); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-93a2ee05910f4b53",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/naval-systems",
        "content_sha256": "86904b8007dd17cd63afd9a77b63208003920601188250edb982e26e00a61593",
        "text_sha256": "67a758f6f8148c57ca300f7bba0d7742aa599b6edd0f2295835facf9e4e5fcc4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-957ebff673ab8d20",
      "claim_ids": [
        "P-AHD-01",
        "P-SKX-02"
      ],
      "content_sha256": "65297495bd253d1cc33bf462991791e37d5de03a7f4d0ed3196ecbf11224109b",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 65297495bd25); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-957ebff673ab8d20",
        "url": "https://www.defensenews.com/global/europe/2024/01/26/rheinmetall-italia-touts-ukraine-deployment-of-skynex-air-defense-gun/",
        "content_sha256": "65297495bd253d1cc33bf462991791e37d5de03a7f4d0ed3196ecbf11224109b",
        "text_sha256": "a24cf5eaef73be9032cdfb7f1d2866f6217fff6b07c783321603f141cd881a33",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-96bd500dc205c229",
      "claim_ids": [
        "C-016"
      ],
      "content_sha256": "4b74fd9eeb5484c4a2359f96202b36658cffa396ab72a53a770e2ce1df82ab1f",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 4b74fd9eeb54); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-96bd500dc205c229",
        "url": "https://www.grosswald.org/skyranger-30-programme-slips-16-months-bundeswehr-rejects-rheinmetalls-bridge-solution/",
        "content_sha256": "4b74fd9eeb5484c4a2359f96202b36658cffa396ab72a53a770e2ce1df82ab1f",
        "text_sha256": "7ac25f867acef5822c04dce01b19b5a5b66811b3b657af42dd8540439e3f0a21",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-9bba6057c1bcc3e4",
      "claim_ids": [
        "M-THA-01"
      ],
      "content_sha256": "aa7cec407ca948528252296abf599ad09d6e535f6482fb945cf8290d9f2c5522",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt aa7cec407ca9); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-9bba6057c1bcc3e4",
        "url": "https://www.edrmagazine.eu/thales-strengthens-portugals-very-short-range-air-defence-capabilities-with-forceshield-system",
        "content_sha256": "aa7cec407ca948528252296abf599ad09d6e535f6482fb945cf8290d9f2c5522",
        "text_sha256": "2595f413829939fb8fbeafa4ea69154d3e8a5fcb845a0ec39731d753a11bc1c5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-9d01bc5d2a34d23a",
      "claim_ids": [
        "C-035"
      ],
      "content_sha256": "e17901caa037648d7c6e79a7be8f1f979589df1383d6b0f6eafaab7f97400ab4",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt e17901caa037); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-9d01bc5d2a34d23a",
        "url": "https://thedefensepost.com/2026/07/09/lockheed-rheinmetall-atacms-europe/",
        "content_sha256": "e17901caa037648d7c6e79a7be8f1f979589df1383d6b0f6eafaab7f97400ab4",
        "text_sha256": "a9d5d8d1ac7cec70957fcb2f7b2a1293241aa3b3fc97787f57e57e6939eac2e4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-9dd1c8db93851703",
      "claim_ids": [
        "C-035"
      ],
      "content_sha256": "c1313f0eaecd0c6b3cea453c7f326429fae36b88d971c5ae4c92e953a1772919",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt c1313f0eaecd); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-9dd1c8db93851703",
        "url": "https://www.defensenews.com/global/europe/2026/09/23/germany-wants-to-manufacture-american-pac-3-interceptors-to-help-meet-global-demand/",
        "content_sha256": "c1313f0eaecd0c6b3cea453c7f326429fae36b88d971c5ae4c92e953a1772919",
        "text_sha256": "48a7c6d2472050a91b67735c1dff456f32da37ec103d7db537094b46b793662b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a21018e8e5b5c677",
      "claim_ids": [
        "M-DK-GBAD-01"
      ],
      "content_sha256": "aef1ebaddc20d23b3696e1a97f538ffc72b5d86ed6370292de0f88a4d239f408",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt aef1ebaddc20); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-a21018e8e5b5c677",
        "url": "https://defensenews.com/global/europe/2025/09/12/denmark-picks-french-italian-sampt-air-defense-system-over-patriot",
        "content_sha256": "aef1ebaddc20d23b3696e1a97f538ffc72b5d86ed6370292de0f88a4d239f408",
        "text_sha256": "79d08ff2b6804090a1775e3ef6f59ad305f3a4b3c55c2f853d4bd9de386a4e87",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a4d54f5d3aa32d9d",
      "claim_ids": [
        "P-STR-01"
      ],
      "content_sha256": "67ed8d1b7033734487634c56d70951c5cc7ae821afa6a2499f570f6a81eb1572",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 67ed8d1b7033); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-a4d54f5d3aa32d9d",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen",
        "content_sha256": "67ed8d1b7033734487634c56d70951c5cc7ae821afa6a2499f570f6a81eb1572",
        "text_sha256": "6077af7f48a4b8faa8a783cba187f6ef43b1eda6d30120036a726a0e3a0b5a5d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a71e6718503ae138",
      "claim_ids": [
        "C-012"
      ],
      "content_sha256": "ccf6c43401d26e732c3cbae83a89d17eb412ca9f312028ca628d157b26496b76",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt ccf6c43401d2); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-a71e6718503ae138",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2026/Q1/Rheinmetall-Quartalsmitteilung-2026-Q1.pdf",
        "content_sha256": "ccf6c43401d26e732c3cbae83a89d17eb412ca9f312028ca628d157b26496b76",
        "text_sha256": "062375f509c3f6e06c8e31ac8221c6cc30a26a18bb0c5cbae1f1a296b6c21372",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-a8887f614647359f",
      "claim_ids": [
        "H-PP-01",
        "H-PP-02",
        "H-PP-03",
        "H-PP-04",
        "H-PP-05",
        "H-PP-07"
      ],
      "content_sha256": "090df9ef146d917fb9a3e89bd0b925cc23ef56cd9ab926bf8be38b9b27b7f129",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 090df9ef146d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-a8887f614647359f",
        "url": "https://www.rheinmetall.com/de/unternehmen/gremien/vorstand/vorstand-uebersicht",
        "content_sha256": "090df9ef146d917fb9a3e89bd0b925cc23ef56cd9ab926bf8be38b9b27b7f129",
        "text_sha256": "f96421969ed3507fe0fdfd22cdd718e73be32f310011efc45f3954d681128986",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aa0faa4814b4b297",
      "claim_ids": [
        "M-SE-IRIS-01"
      ],
      "content_sha256": "3c35204db80b4f868de7336fa95c8141f13da430a51457d0e3b77cb292a4a062",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 3c35204db80b); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-aa0faa4814b4b297",
        "url": "https://new.diehl.com/defence/en/press-media/news/sweden-procures-further-iris-t-sls-systems",
        "content_sha256": "3c35204db80b4f868de7336fa95c8141f13da430a51457d0e3b77cb292a4a062",
        "text_sha256": "a99e857aef3498732665031635d2a1055d000f43a827b1ea8cbdc8e3211a73f8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ace6606b74478d86",
      "claim_ids": [
        "T-AD-07"
      ],
      "content_sha256": "97c73797c1e25207985ce518b50c3719c552e2bda9c7a02bfe4b471a4318b1b1",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 97c73797c1e2); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-ace6606b74478d86",
        "url": "https://www.hartpunkt.de/flugabwehrkanonenpanzer-skyranger-rheinmetall-erwartet-noch-dieses-jahr-milliardenauftrag-von-der-bundeswehr/",
        "content_sha256": "97c73797c1e25207985ce518b50c3719c552e2bda9c7a02bfe4b471a4318b1b1",
        "text_sha256": "830024741eae6183046d9f0c037f385517683de4eeeda1fe016fe7b3c56cf2de",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b003618b3ae9eba2",
      "claim_ids": [
        "P-REG-IT-01",
        "T-EV-10"
      ],
      "content_sha256": "480efd8f260c11c26beb0fd4ce50a972a2843eda3dfe6383ce8782644c5e1a59",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 480efd8f260c); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-b003618b3ae9eba2",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-02-rheinmetall-is-supplying-four-skynex-systems-to-an-international-customer",
        "content_sha256": "480efd8f260c11c26beb0fd4ce50a972a2843eda3dfe6383ce8782644c5e1a59",
        "text_sha256": "eba55636148b0da38d70b5f9e731a5cec0909a5b0b4c9c1bcd9c6993de7f0893",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b77a4ef54de1562f",
      "claim_ids": [
        "H-PP-08"
      ],
      "content_sha256": "474596ab2d7cf1d0e717a4417d17392f9352d64420b2e90a8e6819fcaac430eb",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 474596ab2d7c); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-b77a4ef54de1562f",
        "url": "https://www.bdsv.eu/%C3%BCber-uns/vorstand.html",
        "content_sha256": "474596ab2d7cf1d0e717a4417d17392f9352d64420b2e90a8e6819fcaac430eb",
        "text_sha256": "90101ac17bc25c847425266d9cf983287ae37a925f1513cbe92e557895431815",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b8a3496f93a22c8c",
      "claim_ids": [
        "C-014",
        "P-SKR-02"
      ],
      "content_sha256": "fe23763867f99983d10e21c20d235bfa1f025d0e4d5e49cab3037405ed14a0e4",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt fe23763867f9); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-b8a3496f93a22c8c",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/02/2024-02-27-bundeswehr-ordered-skyranger-30-mobile-air-defence-system",
        "content_sha256": "fe23763867f99983d10e21c20d235bfa1f025d0e4d5e49cab3037405ed14a0e4",
        "text_sha256": "fb065892a93e71c95e0ab5e0deb9755a9013c66efcd5cea9c9df94d6f7126962",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b99b85b72dbd1baf",
      "claim_ids": [
        "M-DE-SKR-01"
      ],
      "content_sha256": "b5b3ba7b89a38476485a0b66a259eeceef88b6a3491d3d65d65756f60e0d492e",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt b5b3ba7b89a3); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-b99b85b72dbd1baf",
        "url": "https://www.hartpunkt.de/lieferverzoegerung-von-skyranger-flakpanzern-fuer-die-bundeswehr-erwartet/",
        "content_sha256": "b5b3ba7b89a38476485a0b66a259eeceef88b6a3491d3d65d65756f60e0d492e",
        "text_sha256": "3a9054a416ab85098ca48fe6d80834827cfa46325494e8cb060d0bc23b4622a7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-bf3aaa0b85ea54a2",
      "claim_ids": [
        "M-SAAB-01"
      ],
      "content_sha256": "befdd4071f9a36dbda8d6aea0115ad742db2d857ecbd5919c987ccc5e814693f",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt befdd4071f9a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-bf3aaa0b85ea54a2",
        "url": "https://www.edrmagazine.eu/saab-bolide-2-more-punch-for-the-rbs-70-ng",
        "content_sha256": "befdd4071f9a36dbda8d6aea0115ad742db2d857ecbd5919c987ccc5e814693f",
        "text_sha256": "5b9d729b70300e770d50c5e9000e44e03a1d6398f90024c43921cff17ed94530",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c0d13e5db6387716",
      "claim_ids": [
        "C-015",
        "C-017",
        "C-019",
        "C-053",
        "P-AD-08",
        "P-SKR-02",
        "P-SKR-07",
        "T-AD-03",
        "T-AD-05"
      ],
      "content_sha256": "bda9e63c53b386b913ed880b221234fcf804221975e133e669d5acc95c373689",
      "capture_kind": "http-original",
      "note": "ILA-PM 10.06.2026 vollständig gelesen (Nutzerbasis-Abschnitt, Kapazitätsabsatz); enthält keinen Eurosatory-Hinweis. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-c0d13e5db6387716",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-10-rheinmetall-showcases-its-cutting-edge-skyranger-air-defence-system-at-ila-2026",
        "content_sha256": "bda9e63c53b386b913ed880b221234fcf804221975e133e669d5acc95c373689",
        "text_sha256": "813efc6f692b68b4b0593dc8e06abaa72178f8694962b2b96db2709e8354a02d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c1dbe305c223e7e4",
      "claim_ids": [
        "T-EV-02"
      ],
      "content_sha256": "52e2fbbf1dd9fe9b342124674b6dd402b7f2e5c62efa3b39b0ebe5b3baea48d7",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 52e2fbbf1dd9); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-c1dbe305c223e7e4",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/09/2025-09-15-rheinmetall-einigt-sich-mit-luerssen-ueber-erwerb-der-naval-vessels-luerssen-nvl",
        "content_sha256": "52e2fbbf1dd9fe9b342124674b6dd402b7f2e5c62efa3b39b0ebe5b3baea48d7",
        "text_sha256": "566b84063669cc643dbb4a708145e89ad7fe033fb3c869519b7a0c490235c833",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cbdf02d668299f56",
      "claim_ids": [
        "T-EV-03"
      ],
      "content_sha256": "3993c83f361db3ee56d0522dbaa00546fb745c094df850b9a5b4f2b51e968ed3",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 3993c83f361d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-cbdf02d668299f56",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Presse/News/Documents/2026/05/2026-05-07-Rheinmetall-Pressemitteilung-Quartalsmitteilung-Q1.pdf",
        "content_sha256": "3993c83f361db3ee56d0522dbaa00546fb745c094df850b9a5b4f2b51e968ed3",
        "text_sha256": "6b71117594d575b4d80056f4f28dc975129aaa1e661b7743a3fe2bf27c2ff697",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-cc9cf45c8609a0d1",
      "claim_ids": [
        "P-VS-01"
      ],
      "content_sha256": "1803ae733594933a314c35f38817cf2f01ca14acff2b7d3c69f52b37fdb3c4b5",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 1803ae733594); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-cc9cf45c8609a0d1",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/vehicle-systems",
        "content_sha256": "1803ae733594933a314c35f38817cf2f01ca14acff2b7d3c69f52b37fdb3c4b5",
        "text_sha256": "84eca0cfa55c3d30dbb36af71a9c98e0cd83a6fafa69acb5b5f93d141b7957ff",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cd51559c12c6bc2e",
      "claim_ids": [
        "T-EMP-03",
        "T-ID-01"
      ],
      "content_sha256": "2ba36ea5ff5f726309e8be23ba56a71f164ce7332ac9101fd6659d9048d58b18",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 2ba36ea5ff5f); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-cd51559c12c6bc2e",
        "url": "https://www.rheinmetall.com/de/investor-relations",
        "content_sha256": "2ba36ea5ff5f726309e8be23ba56a71f164ce7332ac9101fd6659d9048d58b18",
        "text_sha256": "754a7197fb21bd75f3fb9d7d6e32a666b94387784c3d0dd1fdf36325bda0a738",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cede873d57924937",
      "claim_ids": [
        "P-REG-RO-01",
        "T-EV-06"
      ],
      "content_sha256": "b04dced028a2813443dea3659eb30d36a0354477ba11fb49bcecfb3ee5eb9bdf",
      "capture_kind": "http-original",
      "note": "PM 02.06.2026 gelesen: Vergabe 29.05.2026, SAFE, 5,7 Mrd. EUR, Verträge unterzeichnet, Lieferung 2028–2030; enthält zudem die in P-REG-RO-01 fehlend belegten Aussagen (Heimatmarkt, Automecanica, mehrere hundert Mio. EUR). Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-cede873d57924937",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-02-major-historic-contract-in-romania-worth-5-7-billion",
        "content_sha256": "b04dced028a2813443dea3659eb30d36a0354477ba11fb49bcecfb3ee5eb9bdf",
        "text_sha256": "56b7a7218788aff53f4bc86283d702ff90cb046866c51e5dbe107efcb8c1873e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cf7e773278387ae1",
      "claim_ids": [
        "P-REG-UK-01"
      ],
      "content_sha256": "93f2dfaef8e04d966822fa20a11a5cc3b695fa97376f24bc87f151dc55eb8205",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 93f2dfaef8e0); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-cf7e773278387ae1",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-bae-systems-land-limited",
        "content_sha256": "93f2dfaef8e04d966822fa20a11a5cc3b695fa97376f24bc87f151dc55eb8205",
        "text_sha256": "cdfc758339419a83db7d6821136164598363770cebec58e355c4a03fa389ba44",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d1aafc1c9b0f1a75",
      "claim_ids": [
        "C-020",
        "P-SKR-05"
      ],
      "content_sha256": "67976f09be6a7b09df5e57a9ad59f693e4f082547346efce05584553d8be1316",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 67976f09be6a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-d1aafc1c9b0f1a75",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/09/2024-09-30-rheinmetall-supplies-skyranger-30-for-denmark-s-mobile-air-defense-system",
        "content_sha256": "67976f09be6a7b09df5e57a9ad59f693e4f082547346efce05584553d8be1316",
        "text_sha256": "ec7bfcdb1ecaa72c3058897b13e6cbe842080be9b68b81ad30f3cb33809eab4f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d2d239c37b99eddf",
      "claim_ids": [
        "P-SKR-07"
      ],
      "content_sha256": "c718b1a995e3dfb1796880be8be7e9e985608fbb1610d568ed8cf17414fa97b2",
      "capture_kind": "http-original",
      "note": "PM 15.06.2026 (Eurosatory-Ankündigung) gelesen, Absatz 1: Skyranger 30 auf Lynx KF41 „will present“ – nur Ankündigung.",
      "snapshot": {
        "source_id": "S-d2d239c37b99eddf",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-15-rheinmetall-at-eurosatory-to-showcase-its-cutting-edge-skyranger-air-defence-system",
        "content_sha256": "c718b1a995e3dfb1796880be8be7e9e985608fbb1610d568ed8cf17414fa97b2",
        "text_sha256": "00ba7b809e96383cd29c1068b200c1ab879637bc82fac19c669b0160a02c0843",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d2ef86f50f08a3d3",
      "claim_ids": [
        "C-023"
      ],
      "content_sha256": "31a26606d4f29e2a0907edd63cb46d92117d4a0aeab593f2b365e1c1ecd525d4",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 31a26606d4f2); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-d2ef86f50f08a3d3",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2023/12/2023-12-20-lynx-with-skyranger-30-for-hungary",
        "content_sha256": "31a26606d4f29e2a0907edd63cb46d92117d4a0aeab593f2b365e1c1ecd525d4",
        "text_sha256": "8e959ccb73675b2d2d638b5ca4f1b33bf7dde93138d610309e615637fa10d72b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d32c73540389046f",
      "claim_ids": [
        "T-AD-06"
      ],
      "content_sha256": "49b8163f8936c624cc40957aa436cdceb8fdd755b2c12e63b93a38fe7f320abc",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 49b8163f8936); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-d32c73540389046f",
        "url": "https://www.boerse-online.de/dpa-afx/capital-ausruestung-fuer-das-heer-kommt-spaeter-546388.html",
        "content_sha256": "49b8163f8936c624cc40957aa436cdceb8fdd755b2c12e63b93a38fe7f320abc",
        "text_sha256": "d648dd19f5a06e5ecdad056958551b59cfa9de449ebc694337cbaaa6f52e5aaa",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d5ab9c70470a478d",
      "claim_ids": [
        "P-STAT-01"
      ],
      "content_sha256": "204133353423418055f7c7194310e77bc2cd103a5cfef182f51fe314ae9d789b",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 204133353423); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-d5ab9c70470a478d",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/stationaere-flugabwehr",
        "content_sha256": "204133353423418055f7c7194310e77bc2cd103a5cfef182f51fe314ae9d789b",
        "text_sha256": "7669f43f15c598e1b2e457fa4c7f24b1b81d176d03982bcb24c033f97ffa7431",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d776dc827ba55608",
      "claim_ids": [
        "P-REG-US-01"
      ],
      "content_sha256": "fe864fda4016aabd62860dfd9a5cad123d8e8fea4755018c2383424a04ff49b0",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt fe864fda4016); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-d776dc827ba55608",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/09/2026-09-30-american-rheinmetall-liefert-mk93-lafetten-an-die-us-army",
        "content_sha256": "fe864fda4016aabd62860dfd9a5cad123d8e8fea4755018c2383424a04ff49b0",
        "text_sha256": "9a29d9f5ea5d32f8ee077fab573367cc8562f18349ac95064251f99e2fd18bae",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d7c2de50db0d079d",
      "claim_ids": [
        "P-SKX-03"
      ],
      "content_sha256": "ba29fab0c319373f2d87deafd67ecd4ff488df94d785f40ee7f9aa7ddcf9ec99",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt ba29fab0c319); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-d7c2de50db0d079d",
        "url": "https://www.berliner-zeitung.de/article/rheinmetall-chef-flugabwehrsystem-erfolgreich-im-ukraine-krieg-doch-handfeste-belege-fehlen-10004755",
        "content_sha256": "ba29fab0c319373f2d87deafd67ecd4ff488df94d785f40ee7f9aa7ddcf9ec99",
        "text_sha256": "4e7a59307a360aa317c8c29bdd7e63c08444eb263f61cc85e36b92566c7a928b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ddb1d21cd09da6cf",
      "claim_ids": [
        "P-REG-NO-01"
      ],
      "content_sha256": "f7573d469364a165b4bfe0063195a23cfa0a5e5db233e2827f5bd0eeea9a66e7",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt f7573d469364); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-ddb1d21cd09da6cf",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/10/2026-10-01-rheinmetall-nordic-eroeffnet-neuen-standort",
        "content_sha256": "f7573d469364a165b4bfe0063195a23cfa0a5e5db233e2827f5bd0eeea9a66e7",
        "text_sha256": "3644b01fec41a33ca0c1f5b49315688d051304c98e8261c65d455c1aa83c33a5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ddd98359e4352c31",
      "claim_ids": [
        "M-SE-TRI-01"
      ],
      "content_sha256": "e74527e72bf464862f8862cff203776a496d9dc925ce984517c6a97a054d313e",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt e74527e72bf4); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-ddd98359e4352c31",
        "url": "https://militaeraktuell.at/en/bae-systems-sweden-buys-tridon-mk2-air-defense-system/",
        "content_sha256": "e74527e72bf464862f8862cff203776a496d9dc925ce984517c6a97a054d313e",
        "text_sha256": "c8a22ec1435e75b00a798bbe79f9f012345de964e7e826e8e59adeebed6c5dd1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-dffd12785279e32f",
      "claim_ids": [
        "M-LT-MSH-01"
      ],
      "content_sha256": "fbbd972c7db89024c9cabf21688bcf118bd716d637c92c053b1c4691c49033de",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt fbbd972c7db8); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-dffd12785279e32f",
        "url": "https://euro-sd.com/2024/07/major-news/39225/lithuanian-mshorad-order/",
        "content_sha256": "fbbd972c7db89024c9cabf21688bcf118bd716d637c92c053b1c4691c49033de",
        "text_sha256": "3fc1841903be0bde2f46189f044419afe3e41ab5492d34b1cff0c3f042743cdd",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e4c101cb061aafcf",
      "claim_ids": [
        "C-051"
      ],
      "content_sha256": "304ecfd117af28d304e67b7d9da8228a487c685d9c20a4403ae88d55d8fbbb67",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 304ecfd117af); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-e4c101cb061aafcf",
        "url": "https://www.rheinmetall.com/de/investor-relations/veroeffentlichungen/stimmrechtsmitteilungen",
        "content_sha256": "304ecfd117af28d304e67b7d9da8228a487c685d9c20a4403ae88d55d8fbbb67",
        "text_sha256": "aa7f9a40b777bf10b0a92b2224147705ceb00cf4929e5b230f1f1ec39ff17c50",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e6e94711a0973745",
      "claim_ids": [
        "M-PL-PIL-01"
      ],
      "content_sha256": "fedb124de4ba003c0da0ba6c8bdbf12639ad9ec24aebd7d4b60207b0c35ac9a1",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt fedb124de4ba); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-e6e94711a0973745",
        "url": "https://defence24.com/armed-forces/poland-concludes-a-massive-shorad-contracts-with-camm-missiles",
        "content_sha256": "fedb124de4ba003c0da0ba6c8bdbf12639ad9ec24aebd7d4b60207b0c35ac9a1",
        "text_sha256": "2f8f57d2a162cff04d190a26791c40b908c44d6f22f176eab902c8bd6b1f8054",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e6f358904e19e4e8",
      "claim_ids": [
        "P-AD-08",
        "P-AD-09",
        "P-DS-04",
        "P-DS-05",
        "P-REG-DE-01",
        "P-REG-EU-01",
        "P-SKX-05",
        "P-VS-02",
        "P-WA-02"
      ],
      "content_sha256": "24eb1efde161bb5cdaa637eb444a3bb9dae4c14e94535b0a4b40281b8ff76202",
      "capture_kind": "http-original",
      "note": "Investor-Foliensatz Sept. 2026 (PDF) gelesen: Folien 8 (Europakarte zusätzlich als Bild gerendert, Poland hellblau = potential), 25, 34–35, 38–41, 48–53; Kapazitätsfolie weiterhin „under installment“. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-e6f358904e19e4e8",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2026/Q2/Rheinmetall-Investor-Presentation-2026-September.pdf",
        "content_sha256": "24eb1efde161bb5cdaa637eb444a3bb9dae4c14e94535b0a4b40281b8ff76202",
        "text_sha256": "0c1fb589050b8edc19765a2565579fa99fec495fbc7ddde3267df72e8f2844a2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-ea6a47ff86b90b1c",
      "claim_ids": [
        "C-052",
        "T-ID-06"
      ],
      "content_sha256": "adfeab575b4d591f9e689a4acd81165e6aca68b35b9e419c0e17e74569f69c0a",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt adfeab575b4d); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-ea6a47ff86b90b1c",
        "url": "https://www.rheinmetall.com/de/investor-relations/aktie/aktionaersstruktur",
        "content_sha256": "adfeab575b4d591f9e689a4acd81165e6aca68b35b9e419c0e17e74569f69c0a",
        "text_sha256": "d28003bbf79cafe0a90da2020ad86903f533ffc23a2b1474c293d13eca067a60",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-eadffcced857ac38",
      "claim_ids": [
        "C-026",
        "P-SKR-06"
      ],
      "content_sha256": "cf19f41aafe536ddd72727f1fa865b17b127b472270358e70d9ac712712151a8",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt cf19f41aafe5); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-eadffcced857ac38",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/10/2025-10-10-rheinmetall-skyranger-35-ukraine",
        "content_sha256": "cf19f41aafe536ddd72727f1fa865b17b127b472270358e70d9ac712712151a8",
        "text_sha256": "915d90a2f14c5f408279c874e9a5c6b4e2601b66d097224f05ab9d7d6753db8f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-eb7f63760aba3e64",
      "claim_ids": [
        "M-THA-02"
      ],
      "content_sha256": "de77500835c0dc3b70addc4c8bcd59b9389560bc0f0b6c18a1b013e19a5296fd",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt de77500835c0); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-eb7f63760aba3e64",
        "url": "https://euro-sd.com/2025/03/major-news/42935/over-5000-lmm-for-ukraine/",
        "content_sha256": "de77500835c0dc3b70addc4c8bcd59b9389560bc0f0b6c18a1b013e19a5296fd",
        "text_sha256": "4b46f77c6641b00cd5507b15ab02fdcbaa24cc6012d1d51014cdedff031aef85",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ed85256fd87c2a74",
      "claim_ids": [
        "P-CUAS-03"
      ],
      "content_sha256": "957f427d0f9852e64f2ecfed7312d6b008621595e4cadcb9829cc5962b077c38",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 957f427d0f98); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-ed85256fd87c2a74",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/10/2026-10-07-rheinmetall-und-praetorian-aeronautics-liefern-containerisiertes-drohnenabwehrsystem-aerie",
        "content_sha256": "957f427d0f9852e64f2ecfed7312d6b008621595e4cadcb9829cc5962b077c38",
        "text_sha256": "506c9e0478e2f3b60c349910f7843e319af39e81733e265f2c67ef53080edf7b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-eddf31ac6c75fbe9",
      "claim_ids": [
        "M-SE-TRI-01"
      ],
      "content_sha256": "9a2205d18f53d07ee49b89641ac9fe19704874602b3e692291cf44db93b43cff",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 9a2205d18f53); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-eddf31ac6c75fbe9",
        "url": "https://thedefensepost.com/2026/04/06/sweden-bae-saab-deals/",
        "content_sha256": "9a2205d18f53d07ee49b89641ac9fe19704874602b3e692291cf44db93b43cff",
        "text_sha256": "ecd035d1ebf3245c73a6ff398272a7ba40a3369619776aa6fd782f2805e514f9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f129b4e8889709a9",
      "claim_ids": [
        "M-UK-SHORAD-01"
      ],
      "content_sha256": "e78f5f76c76e94dc40b670dab2707c09dd407ad05b97cd0aa60694cf1b979010",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt e78f5f76c76e); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-f129b4e8889709a9",
        "url": "https://www.calibredefence.co.uk/?p=6167",
        "content_sha256": "e78f5f76c76e94dc40b670dab2707c09dd407ad05b97cd0aa60694cf1b979010",
        "text_sha256": "2a6de984169574b08009df2f7a6a8a7ed99982617e0630a3251d115dda18ab50",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f3c15f4b90f4bfc8",
      "claim_ids": [
        "M-AT-ESSI-01"
      ],
      "content_sha256": "ba13e17ae5d425181670f8564fe61a939c910f5aa224e453ac2567fc2306053c",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt ba13e17ae5d4); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-f3c15f4b90f4bfc8",
        "url": "https://militaeraktuell.at/oesterreich-ist-der-sky-shield-initiative-beigetreten/",
        "content_sha256": "ba13e17ae5d425181670f8564fe61a939c910f5aa224e453ac2567fc2306053c",
        "text_sha256": "23a41d41969549926be83b572f182f669ffd88bf4e39414795715b58617f6bd8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f4643db24ca2fc22",
      "claim_ids": [
        "T-EV-01"
      ],
      "content_sha256": "f574d9d92e7c0ea71ebebbe7cec6632da80c5a28d1964538b674e2b5522e7210",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt f574d9d92e7c); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-f4643db24ca2fc22",
        "url": "https://esut.de/2025/08/meldungen/62886/rheinmetall-eroeffnet-groesstes-munitionswerk-in-europa/",
        "content_sha256": "f574d9d92e7c0ea71ebebbe7cec6632da80c5a28d1964538b674e2b5522e7210",
        "text_sha256": "2cc0a25f63fd89aac590a480a6a4c90d176de9d986316ca3599b493ff55b222b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f4730b21412bb02a",
      "claim_ids": [
        "C-001",
        "C-002",
        "C-003",
        "C-004",
        "C-005",
        "C-006",
        "C-007",
        "C-008",
        "C-010",
        "C-013",
        "C-032",
        "C-033",
        "C-036",
        "C-037",
        "C-038",
        "C-039",
        "C-041",
        "C-042",
        "C-043",
        "C-045",
        "C-046",
        "C-047",
        "C-048",
        "P-AD-04",
        "P-AD-05",
        "P-AD-06",
        "P-DS-02",
        "P-DS-04",
        "P-REG-IN-01",
        "P-REG-JV-01",
        "P-REG-OWN-01",
        "P-REG-PL-01",
        "P-REG-SEE-01",
        "P-WA-03",
        "T-EMP-01",
        "T-EV-03",
        "T-ID-02",
        "T-ID-03",
        "T-ID-04",
        "T-SEG-02"
      ],
      "content_sha256": "138727c9936e18cce3a3e85772863f35c22cc8d842ec9baee46b5cbf5035bd6d",
      "capture_kind": "http-original",
      "note": "Geschäftsbericht 2025 (PDF, pdftotext zweispaltig) gezielt je Belegstelle gelesen: Struktur S. 22, Strategie S. 34/39, F&E S. 31, Wesentliche Ereignisse S. 49–53, Prognose, Personal S. 56, Anhang (39) Befreiung S. 264, Nachtragsbericht, Anteilsbesitzliste S. 267–271 (Zeilenzuordnung bei zweispaltiger Extraktion je Gesellschaft einzeln geprüft). Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
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
      "source_id": "S-f562ccee195198fd",
      "claim_ids": [
        "C-009"
      ],
      "content_sha256": "b68ad3b7aa9771506aecf95699b8fdfaf23b937fc479c0edb6a47ba6ec2f691d",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt b68ad3b7aa97); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-f562ccee195198fd",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/01/2024-01-25-startschuss-fuer-luftverteidigungssystem-nnbs",
        "content_sha256": "b68ad3b7aa9771506aecf95699b8fdfaf23b937fc479c0edb6a47ba6ec2f691d",
        "text_sha256": "8e7115dff4f070bd084343925dda04b427dda7bab4539001e10f7cec8aeb91a3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f8577da3c9c0698e",
      "claim_ids": [
        "C-025"
      ],
      "content_sha256": "7bdbe7b4f4086d2ecd8621ecec9ee09fca31cc14a034429a2814fd4b9e4a1cf8",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 7bdbe7b4f408); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-f8577da3c9c0698e",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/01/2025-01-15-italien-beschafft-skynex-flugabwehrsystem",
        "content_sha256": "7bdbe7b4f4086d2ecd8621ecec9ee09fca31cc14a034429a2814fd4b9e4a1cf8",
        "text_sha256": "e258b830ce18a8f37af797c3bf8a0e0fd28963fa8fa65fc41048496348a740c9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f927b29c83eb84ce",
      "claim_ids": [
        "P-REG-IT-01",
        "P-SNS-01"
      ],
      "content_sha256": "3c2724dffafcf9adbc54e8bc0fe9b3120d80a5476131aef61d591e4a26c784e5",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 3c2724dffafc); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-f927b29c83eb84ce",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-italia",
        "content_sha256": "3c2724dffafcf9adbc54e8bc0fe9b3120d80a5476131aef61d591e4a26c784e5",
        "text_sha256": "e3f1c8ef468707c6afab835471f39f8fc13e186c568b99b83253e3f2e5d3be42",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-faeb7be1bb92f0b5",
      "claim_ids": [
        "M-PL-NAREW-01"
      ],
      "content_sha256": "70f80f31097ad14d884f5a4058d6e64da4a069b555801dd1d941a7efe86dbf4e",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt 70f80f31097a); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-faeb7be1bb92f0b5",
        "url": "https://www.gov.uk/government/news/4-billion-uk-poland-air-defence-deal-strengthens-european-security",
        "content_sha256": "70f80f31097ad14d884f5a4058d6e64da4a069b555801dd1d941a7efe86dbf4e",
        "text_sha256": "28658535c690180a7f5c012fa665d8e221889feab99f790063b10d5596d2c9af",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-fce8c647daaea30b",
      "claim_ids": [
        "M-SE-RBS-01"
      ],
      "content_sha256": "fb2741c9a4ca492c8ab8e868d526534a40cbf13d8ed5ae6bb071bf0c4fa4b988",
      "capture_kind": "http-original",
      "note": "Original über source-cache gelesen (http-original, Inhalt fb2741c9a4ca); Belegstellen der zugeordneten Claims einzeln abgeglichen. Snapshot gegenüber Runde 1 unverändert; Befund bestätigt.",
      "snapshot": {
        "source_id": "S-fce8c647daaea30b",
        "url": "https://www.saab.com/newsroom/press-releases/2025/saab-receives-order-for-ground-based-air-defence-from-sweden",
        "content_sha256": "fb2741c9a4ca492c8ab8e868d526534a40cbf13d8ed5ae6bb071bf0c4fa4b988",
        "text_sha256": "47a7be5dc37842228f5e6f82ee8b05406d7307f4bb571e6683aeb28b273d58e7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    }
  ],
  "claims": [
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-03",
      "evidence_review": "Unsicherheit korrigiert („vor NVL-Closing am 27.02.2026“); Zahlen im GB 2025 S. 22 unverändert bestätigt.",
      "fingerprint": "64d2ef894b30be1839f5a64f9d0cd7f5d80e160cf7167ad17674b34c34ac2f95"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-04",
      "evidence_review": "Neu formuliert als historische Angabe (Stand Juni 2026) mit Verweis auf angekündigten Wechsel (C-050); beide Zitatabsätze erneut bestätigt. Topic-Abschnitt trägt Zeitgrenze im Label.",
      "fingerprint": "85741148a829ca2adf94bb005b6d0fe8268e959ecde5d072e3c90ab0355903f0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-03",
      "evidence_review": "Neu gegen GB 2025 (Anhang (41)/Nachtragsbericht: Erwerb 27.02.2026), HJFB 2026 (Wesentliche Ereignisse), PM 02.03.2026 (Übergang 1.3.2026), Q1-PM (5,5 Mrd. EUR) und H1-PM geprüft; Closing- vs. Übergangsdatum korrekt getrennt; event_date und Ereignis ev-nvl-closing (2026-02-27) stimmig.",
      "fingerprint": "0c6a147fdfe4c6fd602f415db36115b35d8ccd41f13aacd298ac24ac7e003aa3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-VS-02",
      "evidence_review": "Marder jetzt als gemeinsames Programm gekennzeichnet; entspricht Folie 25 (Bild/Text) des Investor-Foliensatzes.",
      "fingerprint": "9f864e5611bfff50507d0b9c801e0078cdd9ac7e7d225e88d5220b8fa403d15e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-07",
      "evidence_review": "ILA-Teil unverändert belegt; Eurosatory jetzt korrekt als Ankündigung aus S-d2d239c37b99eddf (PM 15.06.2026, Absatz 1: „will present … based on the Lynx KF41“) gelesen und bestätigt.",
      "fingerprint": "be1a030b8de9cb2bdd819d5dd889d151183f4df776d6e505fb15760f325b5d90"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-LT-01",
      "evidence_review": "„bereits für 2026 geplant“, Linienqualifikation bis Ende 2026, Hochlauf ab 2027 entspricht Invest Lithuania; Präsenzaktivität A-LT-BAI angepasst, A-LT-JON ohne unbelegte KNDS-Angabe.",
      "fingerprint": "995ac2925d2461aaa20e2631472874b61f8f99f65c5d898dc636747edda1b986"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-RO-01",
      "evidence_review": "Zusätzlicher Beleg S-cede873d57924937 (Heimatmarkt, Automecanica Medias, mehrere hundert Mio. EUR) wörtlich bestätigt; HJFB-Teil unverändert.",
      "fingerprint": "1f289af9ab6526ccd6c80e284c8f88093218d2138390f0977832b1785850132e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-009",
      "evidence_review": "Partneranteile 607/339/284 Mio. EUR wörtlich in PM 25.01.2024 bestätigt; Unsicherheit jetzt korrekt; Kanten e13–e16 unverändert belegt.",
      "fingerprint": "d507b169d1af3e607216d515bd3d1683f4f1b13133f78cc2c009a889d5e4db2f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-019",
      "evidence_review": "Unterauftrag Rheinmetall→GDELS aus PM 23.02.2024 wörtlich bestätigt und als Herstellerangabe gekennzeichnet; Kanten e29 (rhm→gdels, Unterauftrag) und e30 (gdels→at, Generalunternehmer) jetzt richtungs- und typgerecht. Die 225 Pandur EVO in e30 stehen in der Kantenquelle ORF (23.02.2024), nicht im C-019-Text (unkritisch).",
      "fingerprint": "277794f5f511651bbf260b75dfc90240a83cfea5716b14cac632040311ccc7fb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-050",
      "evidence_review": "Jetzt als Ankündigung laut esut (04.09.2026) mit ausdrücklich fehlender Originalbestätigung formuliert; event_status „angekündigt (Fachmedium)“ korrekt.",
      "fingerprint": "425d2adf02c0ad2b8d9fb07ab6ce40e4c9ab3f7b5cfd6329d2fe572c52fd0ced"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-EU-EDIP-01",
      "evidence_review": "Seitendatum 09.12.2025 und Inhalte auf der EEAS-Seite bestätigt; Abweichung zum Mediendatum 08.12.2025 korrekt offen gekennzeichnet.",
      "fingerprint": "d2ac312fdb21466623ca262cf20f0a67107590fc96e4908016c93fbdb8b671d8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-ARM-01",
      "evidence_review": "Neu: Q3-Recap 05.10.2026, Abschnitt „Update Arminius“ wörtlich bestätigt (Festvertrag bis Jahresende erwartet, Anzahlung bis 30 %, Haushaltsausschuss Anfang Dezember). Dokument nennt kein Produkt; Claim ordnet zu Recht nicht Skyranger zu; Herstellerangabe/Erwartung korrekt.",
      "fingerprint": "77fbf74c16a188b60f5734c24739ff84f5cad2ec811347eb1750935c40b5c3ad"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-001",
      "evidence_review": "Kapitalanteil unverändert bestätigt; Runde-1-Korrektur erledigt: Kante e02 ohne unbelegte Produktzuordnung.",
      "fingerprint": "1e8487c12bc4a509f3841a69e8978f9cd49d36d1fd60677a675cb8bb6b666898"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-004",
      "evidence_review": "Kapitalanteil unverändert bestätigt; Runde-1-Korrektur erledigt: Kante e04 ohne unbelegte Produktzuordnung.",
      "fingerprint": "fbf609616f5366c375c7a61b08b463ec9b90350c06e9a4651a3f175f107017fd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-032",
      "evidence_review": "Claim unverändert bestätigt; Runde-1-Korrektur erledigt: Kante e47 ohne unbelegte Führungsrolle.",
      "fingerprint": "14474db091afbab99af948fd6d7c333326a069f6725a2a98e305ea4f469eccc2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "84258608cc799b979fb1a101af028e5a6925d92075b2a3341a538beceaaffd89"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "d43b44c50eaaf8f8d2c5c291b9650ff9c0b40ed87e3a9d65bc930016817c837d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "1bdd36d5309b47c95d8b3361b967a9cd423445de0e7251de7a83cf51f7173693"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "046ca03ba39a6b4ce2dd609dad9e02b0710ec58cf77c3ff599fca44846614ab8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-06",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "475a52df373c20b7b0329c7ca3206d03c60b237dfbf30b3afea12574b413d448"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-SEG-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "fe1f5ab7541968e13d784bcad0ecbe42b789851dc4d070fa8c9f0bd95dc95515"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-SEG-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "62ce8338f027723ed64962f1293587f77a368f66152fd9f628de2e369f43ac0d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-08",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "e1f84d32c6f22c814be9c2770b760c96c3108e3ac0110b5dbd0fbdb1bdc47cab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "fc5478d380571f7df518c12c77d6726c3681f910d81d2009bad10a2ab8f16a65"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "499190c3680f6c6891c0f18b0403b29186bf5aacdf8ceacf867d8d1a897bc14d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "4609966bf84891dd6038138520548defa654f945e75eec4a9d49703be2f2a71a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b88321dad0b2deef0496b58e5ac338e5624a0ae4f415be9b33ee0257d391f85d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "f06080d8fa8f2eb06186999711e2b792ca24e60074ccc680acf7c0afe66c4e2a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-06",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "387e98337a5e8b4522d8b477f689e0ae34a58de7d1bd32ed78db4ec96a6c277f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-07",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7bb6f7158c10e44bcac97871d55fe1409548f079d37a9b882ff28c4fd4afa4fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-08",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ab57a4ecca2ea2fa2cb5e45b54bc7518b618ac6947eb6c210c298f842cd5f2cf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-FIN-09",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7d90805721c81581ce2c5a605ee93b492abeaf5b3e79894fdd18b20353b2e452"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EMP-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a653c6a0dfdc593044df64ccd490e82b4998c4161fb156932df06fd525fb260d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EMP-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7efeb58cb1e1f33fda7b16fd1992389b81a0117d7dcce84860b7628c04e31dae"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EMP-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "bfd34ec5e307499b6b0a6086ce4a5cb980cea39aa01aac4e83f98e633c50b5c2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-STR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "f6cf3217b9bd8109e2004456f5f29e0419d9bc09d63a79379fedd15dde3672c6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "2f69b45ecb09b62def2526be7dae92ba1d75cd82c39bf524b47524e85d33afa2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "9b08ee326db29507f5ed83afb4cd1cc9188d32ef2497fe1908ca89cfea3bb2ae"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "bd2615bad1c23658fb2b006d6515303f9c613a5c911233bf10697d1b74ab217d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ce2974a285cda0ae79af78c50a35fbba344c2e4a71124b740ac2540906d83ef0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-06",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0ec35e3a5ba38fe46698e3f5726a6809b3faf580960e6996f126fee02e71d14d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-07",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "134134509f919b43e1978c789fd0917e401448172254311fcf17619a3b6e4bda"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a5219c00d8b231173b7e803653e15c53c93b08243d96d3667ba7f60665a26b5b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "fd3bd94303fee711ca976591cdc85a6da199490201883645b9db297844da9db3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3817eff30deabdaff5a4fbb6d686d1089900023483c6b92a0112eff94445500f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ea61d5a8f7e627c3337b6a5d82cd1b0d40167de732c5084577565b6a0643a913"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-06",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "84bbfb36b44130fc9a5394a25a6fdbdbb5a8c42acb47b304cf3049f2ee981193"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-07",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "afb910d18bc191204a1a79a46f4890373db2621014b54c276d0b2a2ba1c127ca"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-09",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "1397a5b717f85ba014b7ffc87dcf240120db08bb6f32a0518dd23e20611e98b6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-10",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6ce77fe7867781840472ed384e4adb9516558ca01f931dee7d75694cda905819"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-11",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "17e04365265023a19d8651b718ae365bd75279217a183eac931bcd16f6c5539f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0dfe33f3afe9be9bc502408ef03a435eac56de47b97e6db2ddb72adbb00e1934"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "566dc0fd8b0ffbc3316b9e2c136ee78b26097d28b1a8f0bc57a889e374808d44"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "68560c7436b02c6e158f44abd40d522f5d248e848022529d745d54a13f6e5070"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "afc0c4f3a2365f9e38be765bf6a188e97d8eb05a28ac4da3a3cff47416856c50"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "14abbb4b216e2f1cf9cc8eb39e2ffe8a3f2ac0318715302367a9c1f2b945d16e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-06",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "5e04a9e5e80e7cca02b753d0af45b8e757a293075230104e761d752cfc968792"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-07",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6dfa9c66164b9540070ff6de09977d0eccc299edf85283e66e881436185915a1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-08",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "fff1562d351a839d31e5b111b641ba5605eff183e5d6db0ae8d40895c39eabac"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-09",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "26be39ff271d2e4c2c7ed7e6316dbc94a6c332378d6be8a40be713a75954463e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-STR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ad913fd118789a94ec1dd47a00662d02cf1daee80db368185b14f28045bb1473"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-STR-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "5d95222b9cc9f2c7c4330a01c7ecba7fee0d3e0afdf4e53211a679798a2fcc94"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-STR-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "2c6c98f8bcde859dfeb0120eeb5a73d689ab13197523b87d413627b58096bab2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-PS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "cf2966c219dc62bf55e6109d25331f8afea8e760d160c14b5002e20d24bf1a8d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-VS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "464bbc97bc5dfa75ead183cbe1cc17eb8f35f5a658bdb88c55a3058b144f1c26"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-VS-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "4674ef019e738e913a70a88bc2019a0198fb0d860e1d0efde0f7a4752ba79917"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-VS-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b51f1b8f8f1495b292f76fc16aa24e804722c87da0e27fba56ffa21401eb15a7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-VS-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7e75ca057211ee06ea48afd8e18e3000750a1972698e58a9b20a2de120780f37"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-WA-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "71cb73c01eb67f41cf91bedb98f24e9e3658f65d1694abb789d68f9b76ca081a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-WA-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0af97a013db7cf662386673dcf87ded6fa8edfeade4da297c7bb89bc17fd23f5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-WA-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "60e667105bab0774ab565c72c7e231956970e977f6941f714e31b4d79d41f1ff"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-DS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "12f8b1f4910b2546545067156e1514e86ba81a85aa0d5b51e315c3b3c649cefe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-DS-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "e2c99d0a71085bd93210a01bfc1b0438c2e93bb8396530b68dd5e083b9f5519b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-DS-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3fa4d22abea5d2143e5e8da18851c8f5908e44f0b813dd34b2bf1d4877632416"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-DS-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "014ab2c9c6c94b79bf3c5bb629c49c7a0ca21e40ea21f407eaff45d0c25352d9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-DS-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "9d4bc81edea898ac503c39b57611767797e704212a591b3a2b94422b5f012609"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-NS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "5bc456aebecec4030472a816fd5239648bba263ffd7fd0559e70d1d0e64e886b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-NS-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "e6ac077c7a58558480434af130f3dc778139a6d622664a3b927ecaba6e95d9ac"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-NS-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0635012dae87fb0afc82e286aedc4c0c6106b372257f7b5eb6a0c721746b4cc7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3c4f834253eef4048d9cd7aba8aa214b320ea0d5998025fecff6a715aada7c1e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ec0a02db36aa0fe4950b47c8e7e10593aa56cc524813a1fb18a48ab44258e380"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "5fea3ac2f9f1ddd3e8c5c64c16ca28b6a34784a3e202b309b083a79b75c98196"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "09c2f3eef07eff56b71306816ccd6abdf579befe48feb5f084e2ebfc990139a9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b2eec33f595f04f0fb39a2522a662717e569c5f5549d960994d2e13cdbed73da"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-06",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "8fdd9d8cafa1fac21c9a361e332f2593f3e91c090760dbc2713e74c88a0ff1b4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-07",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "1c5d202e5c0e30114ea3c97c547e55a12ee90284758b54f8e626f79dd89e5c53"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-08",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "fe7599ccb8bc8ecfacf9b432dd01540ab6cbbf45b51bcdd09fa09744c80824bd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-09",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "e13c00c58b19b89a55815c07644883daa478a2df743c5707e153e9ec51b1f32a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a4212a20f73506b5955b76abe2ea3241bde5ebf6132eba2594179201c902a3b2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "772386cf360018302791a619ce922fd4671c23e72a9457c940f926a801c8deb7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "dc290785830b9fdb37b5c40ae4d057487850dad111596458e2a5799f75b1a595"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "41e2fc4713ff676f83c9884bc6d3ed17123ecd4c3b0c442063c24f45fc3be8fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "d451cacc1ed6cc4284942d782dac3474826167399370e4f942c788d1a0ce1c4a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-06",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b4ccfaf9632179f2cbc016ef60503c2984e081695d25ad72149c199a32c9c2e8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "411c6e3ca8d9c4e568bb1f91d4d595f60c9467ee909986ee75b12033c49ddc1a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "9e7895c78978513b8333ac685516057281398b678b106c699db2fffdf2bbada2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "132ff68b1d5b0b34697a3da64fd7b86c522dbb332c0d19444761bd84a9e76a82"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-04",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0488a84a42ac90e6982e6307e4db0a4b0b02d0f55d3bcf5cd77e31f4d59c0e86"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-05",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "69f063777c59f5c71af18ee703a1e549ef32547a8393c53b9231aee8eaf3362b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-RGM-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "137f868659841ee90df1a91b4a1640b4518b8d8427d148d835c0b6b8c8c83f1f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AHD-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "2e731752af69e11ee87a213bc3867480289747989419210cd91fceeca9c920ae"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SNS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a6718568316653dd0d4bf650cb85de18f5f16f021bf58cffe14c38370a76ee66"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SNS-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a07c98bf86b7849afaa75b64375d62e54c8bcf8ca3743cc64c79d8470e2466eb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKN-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b287318e5d8c89433a3eeec9689fe38f9218dbe806b66f60817803c76617eb02"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKM-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b8cab3e5e281a8e20c41293c9f8af344a93617eb600db4bc196ed4ff537076c7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-CUAS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "d98c6e7b59e15bb11cf5bf1a15a240ec5576218777fc1480640f7e1ba2265550"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-CUAS-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "69f0f3bcd5ea885eb74b1bbbfbc8f1ba70765cc25460275f1b089e0c380a51cb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-CUAS-03",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "58f02fb6a1c04aeca7480e81728d3fbb41b87fc636e11624b3d515ea5287222e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-STAT-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b36cf4f75f391b1e41a6c1ada9c1fb361b61b8d2ca16f647754754282206a146"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-NAV-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "c579588abd6ce587133eb294277e5f2fbf41430a8f461a31d5285807c126d692"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-HEL-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3a970dcc5f699d68f20e68ed06c54783fb236cc6f4e6bfec95cb3af1fedd6d10"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SVC-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "cc03a78696e0d0937aada649f299dc5ebe100d07b3cd4c474069acf34fa084af"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-EU-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a76894cf67a8bcd58af9495aeeebe1c910c13e78254ee1fc7bdc021b23ccc40c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-DE-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a7cace17f7e3e6694e88e27e8922a37935a19a0020635a534ed2839fc91bab5f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-OWN-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "33b494039fe48ca3ea7fe95b5c8015ae1b296f21aea05b2a415ad7711471bcb1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-JV-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a081ff6a53760a393f599a1bc64f8d32ec00a2766ef2d7d9b67069ab6547b963"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-CH-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "607aa486a103b258828a87aae6a75e2f1cd6c2189488364b611d2b8a18dd9ac8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-IT-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ad96ba8ffa3cdf2131e92dbd1f468379f94d9df2c558443ddc203656f180d0c8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-UK-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "1ba5de8f29368123d99c1fd82bf782c60cf955d34f80325b6a23b08ec56a192c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-ES-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6bed1537c6b457baeced10072bae2eb965f0ef1773dff12d77fbf1107d2382fb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-NO-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7aad3aad6159f033cf6bf244e05cb879f12599f5ca1616c3d9b2420811e981b5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-NORD-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "cf5550faa11277fe2142d111b200706829366b64f2cc0b9d911108d1ab1bdd50"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-HU-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "80b93753b0cb2c985bbf3a5f6cfb90295a4f84ef12b8dcc11bcf59accc5e1f2e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-SEE-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "aba4ac85ea50349f172246ce2fe3336a768d056be4f15718d649aafc35281432"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-HR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "f602d151d78faa1ed2c592d5bcc502ac51b0bad8479a35818040f7a602265715"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-PL-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "e3d1c665174f2d0790f81a4934daf2c7f9dc4ffe903111a901e73ac8224ee873"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-UA-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "5934e4346f9c9fedfd771e2dedde2c2db1107bfbab496ce9871f96e27009f515"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-US-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "c3834231748d7b27d639be3818a4731b1c0627d8926c8529565a75107b20470a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-CA-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "fc149584bc1a969451889a5c577ab610df0cc8639256e54469804db134d50c00"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-AU-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "4d2a0747e33b8ca61d434831f2160f3f444aa03328b0ed661c2d03c8b59ca806"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-ZA-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b89c4d1d6d245189a4b9fa0c37f71588a68367562736dadb18601125604b92c1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-ME-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7091713ad0fd062a7ce41251f9c8c97f5513cee7b6ab6455b9bed2d70e1c4596"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-SG-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "94b3d3e05a6871ed70802610fc0637777d640a0f81bf7aea5a40dcca27a946cd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-IN-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "e25cbb4f0a1f8b74df00802b2001e95aa2cba62b4aabbcd4be84b1b97ec54880"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-002",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "18a6d23bd19eca13027cfd1ea505be4c0ed7a92fc1f8845d65bf5d99ef3df594"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-003",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3fc0254f214242b3c8bb2dfcd661c44e44218c50384d2fec4953034db8523874"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-005",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b124b80e5a31ebf8a70de7c1d3a9f1439d2264f90ba8e38c7099e166a2a4a256"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-006",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "11806b590b1e6d4048e25fd4fcc78d9bcbc02c369d8cff62bbe35e53a50f5ef2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-007",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3c944a2e91ca19602ad7b564cf1eb1415a8fa4136ec2a15874d7699a2d95c791"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-008",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "76d46cbf40b0196bc85a5dee8c22327f19489a9d88d32495584b9854bbef5f05"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-010",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ddcbd55dafe8e54acdc6ac5ad0f06815515d8c3da6e4d167daa3c2153efabb2b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-011",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "d98f5011df71cd2c01b0a60b37a43e7370b47349d21a841a34a3d3dfd59152a6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-012",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0ec04e3f7c8a0fd7ddc08f39417d23d95754f9b0282ccb4d4e1ccb0aef968f02"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-013",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3da76b0b3eceea10934f250f52f272602d24de7c8f50acae3fc092f3929c2448"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-014",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "d43f70ddad509e73fdc7317f41aa7872803565eade8455b8fec5e16d43506d96"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-015",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "5fb41a31c24febb2c8184341b0da9cb13265c69b6e9a073ee58bca44f336f29c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-016",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "92485a8471326d9a84e5c5a1df2988b8878a28ba76aca2f9072ea4947068e5a8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-017",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "44ee0d3f68679de4a7867a2e1864dc9a5b2f32a6af3d24a570ea30854fb1cf80"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-018",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "3dd818a8efa696e6f00acd5ff4e00e73813bd35e25090d47d337422c9e34c71d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-020",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6b0c75f155c0fa44acaed756a0c4dcd5e90f2170620e28d62a838ced1abc6535"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-021",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6c467fd5a70f110d8d428180c4ce4ce21ee077fd9ca247905d7f5f32ee78db13"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-022",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a957ba33690181c333b8875d92b9e23382aadd74bb21f5f2f748e737689c7139"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-023",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "1235c111204920482d06d582b32133ab830053c214b8df2570b11af6755938fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-024",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "cfdf11a6f3b933aa69aa56b7afb68f400ebc2db91bf0e58931a590590450491d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-025",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "009394b9fbf93f82b48910e918675967a34fa30446f8b4a5b860544bf7075b02"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-026",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "053e449b74d7923d5d1ae785e514fe87c2f6f9f3d61445bd57660af7f409b0b0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-027",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6d72426512248dfa12c286f565cd4d0f0532b459df4923f42a33400f2f26f2b1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-028",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "cf2c8feebe57e94b285e280f73086407b8b1a873b1f01508879edeb06c8cc3e6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-029",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0ce4e19f79c1c474f971022d2a10aaa926fdf74cbc1bd260028da7c053665c09"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-030",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "68dcb878ca401b69f61780bea5583c75b677b61b2860537ddaab265533d23e01"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-031",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "26268ff19bf1814e75affc337a1ee4de13131343561d9d487ec4019672bea9a4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-033",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0615487d5b266c966f85f6b63361771f8950011c43b746f3901cfa5bd2a72ae9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-034",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b382081b7dad29b2e2b9ab6c32e54f6f247502cd63e158193424a61f04265e67"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-035",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "9383faf9c9710af7378b0406fb8fd320ad3f42aa01b51f8bb9811d4d6758552c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-036",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "181a77ba439706c4e40f1deaeb4a84b48fe741953258d7234b9d0815070cd123"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-037",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "87d29e095cd889e2f8d0ca2a81b28b77d88402929a78aceb5e4f08e7265068cd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-038",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6583e6116fb2821bd868f87f96c0e18f8fdef8f6b05f9b18610bdf5acb7c982f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-039",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "942d8894a19dc19a7827eb58f39155c79be6e115a3cc873640a01f692b08579a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-040",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b34df12bc76ed0806855f01f50c3bfae2cb844b67003f69161a8afb400e246d1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-041",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "489079e6185ba11b828826dededafba5a6c41973e91e99da9f501fd6007da148"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-042",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "cc0ae31feb2e76a8ff04736afd830d1ac12ef5ab2baf881f132c51857cf3a415"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-043",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "c39c49caed65a6e2ff73d1c098c6b9a6eb2c35b667adf9b72c5a20d41b9d830c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-044",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "430ae6c74d5b5d3e13085ed6b2f570f5aece84dd28376b606dfd233a7b163660"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-045",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "10fd79d115297e80cbf2d6a03daa343914dd020c4c261fe4a6ae2d5c962472cc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-046",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b4a8b0c68c30eebfa1065fb4e65829e5b0e1e52916669affc3ba0cc91fdee2e7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-047",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "04321b618146c900df8623358b4a09586dd67d0f0651fd933124a4dd1bd3e05e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-048",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "58855f891563274112043968ca6d1274e59e22631651665752c4ce58023e39fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-049",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "849b4f005369288be43aa3ea19d19844d2076b21595788b87e5c1b22e42f162c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-051",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "c2c6e8d3a97b125dff73a12387786950d2aad24d8c6082e6e8738ea688a4be39"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-052",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b7a89c2d18bc03d92fcd663b0db7d1ce30959024a686c50bb860eca405e3cbea"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-053",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a4fcdb604c8141bf8bca96044ddd42a7b6b25b2034ba967a09e9925a1d9216c3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-054",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "65d53cea440129e8cac705e43884c8f774cecd5e8d754792bbbf9348213d72e8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-NNBS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "6b1c0380dd53633d2f57d5a6014cc0e54f4b92015bf5b76c0c2c1bbd91ddf981"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-SKR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "2c80e285582399a55599c2ea7ca7905be31f5684686461aaeb0364723b59d3d6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-SKR-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "76f5e999ff3f8b0aeb2165baef7741f628de2d6da858fd35e039b61253f4cd7c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NL-SKR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "fde8e052b40a24e71490baa835579529aafdd4928a7f76447224382d87438f42"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-SKR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7811d962e34cf7693eed0a02dcde826d0bf8e220e8fb2ce742de48675d16f37b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-AT-SKR-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "8dd0444aeed53b191155f4ad14c9f38e5b22da014daa502b77d3d438361ac0a1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-AT-SKR-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "99fa6e35b6545f356ba070cc68a08f4345688fec14a28621490074402d85c0ae"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-AT-ESSI-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "f96ee5c27ee8ed8e78569be546dc35d9b7b3418491dfc1264016a6e4fa548f3b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-VLM-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "8bf61462d780618aece24688a6d14d36311b18cab095fc455d59ea37b2cd607e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-GBAD-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0b657e535e24119840a11ad437cc6f88d1a05308ebb635f0539c16d1e70c0bc5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-SAMPT-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "469c82f68be002509d9baecd61c1b63ea40a8db44deb0c80b7d299ded2a66579"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-IRIS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "985b51347132f6cf9a78273c57190f3306bdce973f321d452e334405831b6654"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SE-IRIS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "15c1b174f0077d9391629910af8a428205aa0c0ee74427456cdaac603c0551fc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DIEHL-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "2c048502b17962c7a3a09ed4cfc6f30ad596087bda9e8e2961bc0cf236d2710d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SE-RBS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ad1cc94f584d9ab65ec17083e2903dcfd14a657b75757381c4423c8b582e1f26"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SAAB-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "e68dc45ccfbcfbf2981a4e02443b3cbb3a6ad9951fd16f1c17d34f516fef0fbf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-CZ-MSH-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "356510e9545151bd9027551757a28d8e90bd66c36df411bc2e8df1a96920068a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-LT-MSH-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "8481c3a02e66d2764bfbd1f78a938084c96116d9944c51e20e9efbb89009719c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SE-TRI-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "353cc67f8c3b7d87893c4aff1f0047c444007b83ae7dce1bd0b4363f46e12e24"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-PL-PIL-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a22e4678ecfe33a603c859508db9aec82cdcbec294b529d027851b50da60cca5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-PL-PIL-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "f498906f684e2ca883b4269afefda3d1cac4431dc3fd45305090d8c99466b613"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-THA-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "35175efd16ccda666155364433bde58f767946dc0b81fee2050706af3bdf462b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-THA-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "b82633af397157721e74a8fbee5c33e44cb6cec4a38fcc6b987d83b1a107d214"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-UK-SHORAD-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "5cd6f2e747356589d8fdce630313a7663eda589642e309cc0d6b1f3ddcf13aa1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-EU-SAFE-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "068d269ece228361992285b8ab0edc0573ed18b5d2f9142ad88256e0d8562eef"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-EU-SAFE-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "0b4dee56da302265ffee51536194aac20bc59dc75db30f94aa5da2551dd48104"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-EU-SAFE-UK-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "91281ca1829f3f213b3842a89d17173c030f865f5d0487a3dbac2d9e493f4fd0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-00",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "7ad9b826bf23aa31ea7c0692a06158aebcb1c6e4c02284a6bc10cbb21999bb60"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-DE",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "20796278a30401d07ec778e9eb91cf6e5c45f81c4cdc32d8974482352b0aa5ca"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-PL",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ed31338551d3f3d17bdfb187d017e971fded8e677880ab702a9517f6501ba014"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-NL",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "34c04d837a63163ab3cac1009748c61685655463a69ff2638208c4754e837aea"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-DK",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "964141de9d449cfadab6f2b34e40ea7b1abdbd46f2548b67e4fb3df49c97ff5d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-RO",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "56402cc836ea93a4a0c54e84e913341aba080fa0bb13a382517bdf79d26b48cc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-IT",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a376851a3a4248e20c2f15578ee4d6c952b2036479af454393236d07f86fe1a3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-AT",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "34d66cc747879d5dba01caf99ddaa6d9c36f9de2b2fd280a56e1945f8a2d0676"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-UK",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "ed66f1e814433d8c9fa27420e8dd0a4e40c084a49833caff8bbfe4a02ba1268c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-SE",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "a1b8d38dc36f03ee5a5a4c92eb2a9c5d074bcb7d76d9e84212d72dab7282a2f3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-PL-NAREW-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "f30ddad37bbc0480a52341a7b92dee4b4d1c07abe4ce23aa5b675ad8387331fb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-IRIS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "780c3ac7a7b0fa23b667c9c3288e33cdd33b30b6d1361d6412aa6ee9a4789142"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-IRIS-02",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "4e43dba38bd8b59530d474487cc3b0231e28d7633761cdbb785a9b9cbef985d9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SKR30-ARCH-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "f6a736d6fd6ea93a4d703fbf2f772c1b2d69601abf8c3ff9c98f3dbba700e55e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-IT-A2CS-01",
      "evidence_review": "Runde-1-Inhaltsbefund ausdrücklich bestätigt: Aussage, Quellenmetadaten und Original-Snapshot (content_sha256) gegenüber r1 unverändert; Einzelbefunde siehe review-basis-draft-r1.json. Nur die Paket-Zuordnungs-Fingerprints änderten sich durch die geprüften module_views-Korrekturen; die neuen Zuordnungen wurden semantisch kontrolliert.",
      "fingerprint": "8bb6a42f1dce39af556f1821191da8cd4175ef3b6f033d44e6712c32a1ff4c3d"
    }
  ],
  "missing_decisions": [],
  "fact_review": {},
  "input_fingerprint": "8218317d37be847977d11a0a2a71ce121f1a736d429a8483bacdf959200e9bd4"
}
```
