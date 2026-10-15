# Review

```json
{
  "schema_version": 1,
  "run_id": "20261013-rheinmetall-flugabwehr",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-13",
  "phase": "basis",
  "status": "freigegeben",
  "review_work_fingerprint": "b27ac6a1642d22f083c59309891803b9d585d691a37f300d98b34e1eab9ee06b",
  "material_errors": [],
  "scope_and_mappings_checked": true,
  "review_scope": {
    "summary": "Runde 3: 120 Claims mit geändertem Snapshot bzw. geänderter Zuordnung gezielt geprüft (je Beleg alter vs. neuer Originaltext; große Diffs wörtlich gelesen), 104 Übernahmekandidaten ausdrücklich übernommen. Neue Präsenzaktivität A-NO-SKO-DEV und geänderte Cluster-coverage/report_log (SEC-10-K nur noch Suchweg) semantisch geprüft. Keine Webabrufe durch den Prüfer.",
    "refresh_state": "Refresh-Protokoll gesichtet: 78 Textänderungen überwiegend Datumsformat/Seitenrauschen. Die Incapsula-Sperrseiten (S-23f40ac8c2701e11, S-280bd40a5e5bf16d, S-71d29e036dae7d32) und S-55faca3b1d80c836 stützen keinen Claim und liegen nicht im Quellenregister des Pakets. Kurze bzw. textlose Snapshots wie in Runde 2: S-3ba304da81a26074 (T-ID-05) und SIPRI-XLSX S-7730735b980263ed (Snapshot unverändert, Werte per openpyxl belegt). Kein Rückgriff auf ältere Snapshots nötig.",
    "nonblocking_notes": [
      "A-NORD-WA führt country=\"Schweden\" für eine Aktivität über vier nordische Länder (aus früheren Runden unverändert; kosmetisch, portfolio).",
      "Das Positionierungs-/Schluss-Review muss wegen der geänderten Präsenzzuordnung R-NORD (I-RP-R-NORD) und der neuen Paket-Fingerprints neu vorbereitet werden."
    ]
  },
  "source_checks": [
    {
      "source_id": "S-00676d9d1d5efc0a",
      "claim_ids": [
        "M-DE-NNBS-01"
      ],
      "content_sha256": "5c6903465df1ef51fe4840b889767a278548f73d0ae4f153beff38b709da6521",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 5c6903465df1 (vorher e7dcae6a0fd1) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-00676d9d1d5efc0a",
        "url": "https://esut.de/2026/09/fachbeitraege/streitkraefte-fachbeitraege/75313/beschaffungsvorlagen/",
        "content_sha256": "5c6903465df1ef51fe4840b889767a278548f73d0ae4f153beff38b709da6521",
        "text_sha256": "1b4e4bd836cbb49bf04fa52a29ac6d5c116455ee5fae4220966dad7012381540",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-042b26990fdc2a9d",
      "claim_ids": [
        "T-EV-03"
      ],
      "content_sha256": "a6d89615b127601e09c6f56b95a8ae404ae05db4420338fa6e1521cbc32ea7d4",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot a6d89615b127 (vorher 5c6775c76e8c) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-042b26990fdc2a9d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/03/2026-03-02-rheinmetall-takes-over-nvl",
        "content_sha256": "a6d89615b127601e09c6f56b95a8ae404ae05db4420338fa6e1521cbc32ea7d4",
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
      "content_sha256": "44a4d1667244d7139c098d837eadf20b21a15e2910ea88f4b1b2f2844ffeb2a4",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 44a4d1667244 (vorher 0cb20930a867) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-04cc080af88f833d",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/10/2026-10-06-rheinmetall-iceye-space-solutions-provides-the-bundeswehr-with-access-to-sar-satellites",
        "content_sha256": "44a4d1667244d7139c098d837eadf20b21a15e2910ea88f4b1b2f2844ffeb2a4",
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
      "content_sha256": "6545caca63cb7406170cbac7d7aecdba711d973714046d131f041b25898173ae",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 6545caca63cb (vorher 9ef48da0000d) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-057484ce43bd0f28",
        "url": "https://www.osw.waw.pl/en/publikacje/analyses/2025-05-28/imperfect-balance-eus-defence-loan-mechanism-safe",
        "content_sha256": "6545caca63cb7406170cbac7d7aecdba711d973714046d131f041b25898173ae",
        "text_sha256": "a2a0be66ba9698af4b34c4b3d7c9e138f0999b3c19bccfc2e8070aaa441d89c8",
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
      "content_sha256": "8bf96eaef7705073acc2d7c376363c688b44de0251960da97d4d23b2197a9097",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 8bf96eaef770 (vorher ac9fd7aa4dfc) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-081455a6101c816e",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/01/2025-01-06-35mm-gepardmunition-fuer-ukr",
        "content_sha256": "8bf96eaef7705073acc2d7c376363c688b44de0251960da97d4d23b2197a9097",
        "text_sha256": "7b72381e8ec23fd4135acb3431b97c491157236423a81301040272dd3498c188",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "source_id": "S-0d1aacb2a960fe0b",
      "claim_ids": [
        "M-DK-SAMPT-01"
      ],
      "content_sha256": "ce2944a09e26731bfe014edaea13a6c6901ff8afc965ba9f8a85b6cd97f4c8b7",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot ce2944a09e26 (vorher 92c8dd0ca921) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-0d1aacb2a960fe0b",
        "url": "https://defence24.com/industry/denmark-breaks-with-america-sampt-ng-instead-of-patriot",
        "content_sha256": "ce2944a09e26731bfe014edaea13a6c6901ff8afc965ba9f8a85b6cd97f4c8b7",
        "text_sha256": "d2dd561c931a9ff125bb1198f2bcd92bda0848b2458a068bf245065aec5e6a7d",
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
      "content_sha256": "170e35d743d513d9b555273c96b5083b543ebd567c114a4bd96f1f90d9ee5f00",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 170e35d743d5 (vorher 27e36f8dbedd) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-10079a15b0d54839",
        "url": "https://www.leonardo.com/en/press-release-detail/-/detail/05-11-2025-leonardo-and-rheinmetall-first-contract-to-supply-armoured-vehicles-for-the-italian-army",
        "content_sha256": "170e35d743d513d9b555273c96b5083b543ebd567c114a4bd96f1f90d9ee5f00",
        "text_sha256": "30db575999081c60fae91373a3b1587147e5409d1b83dd2d555274d625e3db8e",
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
      "content_sha256": "1cb0a770b67d1b10f1f926931100938675f977d33ea69c1074f31bc874db370f",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 1cb0a770b67d (vorher a3b300c6ccd3) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-12a6733e8d06cf75",
        "url": "https://esut.de/2026/02/meldungen/67674/bundeswehr-bestellt-iris-t-flugkoerper-fuer-luft-luft-und-boden-luft-anwendungen/",
        "content_sha256": "1cb0a770b67d1b10f1f926931100938675f977d33ea69c1074f31bc874db370f",
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
      "content_sha256": "7c3ca0ac467db232125458712d84fd09357de0449f647ad6e2886f24eae6c0da",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 7c3ca0ac467d (vorher a5a073334c28) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-12e946370fcf4e20",
        "url": "https://defence-industry.eu/czech-republic-orders-saabs-mshorad-system-with-rbs-70-ng-in-e155-million-deal/",
        "content_sha256": "7c3ca0ac467db232125458712d84fd09357de0449f647ad6e2886f24eae6c0da",
        "text_sha256": "cd776451f11d9b87e151b5ec0ccc9d0e0b06a8554afa174847904e0d419e920a",
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
      "content_sha256": "a9a987664d4e3ae457dd83dac36e468aedc07ddfe7b477e78f0911aead91eead",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot a9a987664d4e (vorher c465304cc0c0) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-168108fb27118dde",
        "url": "https://defence-network.com/deutsche-skyranger-produktion-kommt-nach-neuss/",
        "content_sha256": "a9a987664d4e3ae457dd83dac36e468aedc07ddfe7b477e78f0911aead91eead",
        "text_sha256": "0bf22b59877f0ba137a5186a424d9eb40c6a025f735dc53edc50369445533fb1",
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
      "content_sha256": "d1cfd9b57f8af43d49e2429fb3b0868f109dece5a95acea51938e28076df6b0c",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot d1cfd9b57f8a (vorher 65813cd8e409) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-16d1e80677f1a6b8",
        "url": "https://www.finanzen.net/nachricht/aktien/in-der-kritik-rheinmetall-aktie-in-rot-bundeswehr-ruegt-verzoegerungen-so-reagieren-renk-hensoldt-und-tkms-00-15892493",
        "content_sha256": "d1cfd9b57f8af43d49e2429fb3b0868f109dece5a95acea51938e28076df6b0c",
        "text_sha256": "974f2c329d5ebf1c1d839c6e55aad662c77dda899ffbf3ce3e2f90e3950e00aa",
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
      "content_sha256": "b321bda1f699af159d0d984f15f4b373f6f69fd489974c276339f32c15f0e8ac",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot b321bda1f699 (vorher 2f906ae59a3a) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-18ce19a1fbbec148",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-air-defence/ueber-uns",
        "content_sha256": "b321bda1f699af159d0d984f15f4b373f6f69fd489974c276339f32c15f0e8ac",
        "text_sha256": "a89279937b29ce4d3cb173f371e5c49065f5f0e8c71cc78dff87801308cc1419",
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
      "content_sha256": "04a558b8f37635e13079960e22dc3c5ef61c059d075d9528e29c359a5fd03cab",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 04a558b8f376 (vorher 30f738322b6d) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-1ee3bed35c316be7",
        "url": "https://esut.de/2023/06/meldungen/42792/beschaffung-von-sechs-luftverteidigungssystemen-iris-t-slm-unter-vertrag/",
        "content_sha256": "04a558b8f37635e13079960e22dc3c5ef61c059d075d9528e29c359a5fd03cab",
        "text_sha256": "23b3a179e843d5a1c6ab07d4fa3276e07fac37f015e52283a0028bcb468379d1",
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
      "content_sha256": "a47cbe6f53b952baceab38a5682fcad9a51d29a9635c91b3462825bfd5799bab",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot a47cbe6f53b9 (vorher 70de1e9d55e2) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-2185a7a52eb76e0d",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/08/2026-08-19-rheinmetall-und-hensoldt-demonstrieren-erfolgreiche-integration-passiver-sensortechnologie",
        "content_sha256": "a47cbe6f53b952baceab38a5682fcad9a51d29a9635c91b3462825bfd5799bab",
        "text_sha256": "663e43c045d5679c50fab8f0e77a0844ed275f9e403529e7aaafe1b945017455",
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
      "content_sha256": "2ec43d5810ff2accf90dab6f9c0d077f5651ab1434869d2e26a68568e744da73",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 2ec43d5810ff (vorher 1ac21497b758) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-29616d5aef4d2b76",
        "url": "https://esut.de/2024/09/meldungen/52961/pandur-evo-mit-skyranger-30-erstmals-oeffentlich-vorgestellt/",
        "content_sha256": "2ec43d5810ff2accf90dab6f9c0d077f5651ab1434869d2e26a68568e744da73",
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
      "content_sha256": "f83efb24743995ef933621f43f1d478e62f39ab4b8d0b2219b8a4c3601ca56d2",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot f83efb247439 (vorher 2b01db7ec69d) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-2b24723c99b5458a",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/weapon-and-ammunition",
        "content_sha256": "f83efb24743995ef933621f43f1d478e62f39ab4b8d0b2219b8a4c3601ca56d2",
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
      "content_sha256": "dff1dc374f685817a985f0df1b8ea39ddea8857aed845859ee49472d7540bd4c",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot dff1dc374f68 (vorher 34e5e6ef8d95) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-2d3cddf7945e1791",
        "url": "https://euro-sd.com/2024/09/major-news/40568/denmark-orders-16-skyranger-30",
        "content_sha256": "dff1dc374f685817a985f0df1b8ea39ddea8857aed845859ee49472d7540bd4c",
        "text_sha256": "9907a022f730f89a4448449aa33897e58ca6731b3097450ab571cceef5f4bc53",
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
      "content_sha256": "e505b2f7d7dcb691e6f202d0deedada6f593aba3fc95b6e80c357f74a4fffb3a",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e505b2f7d7dc (vorher ceff33aee9d0) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-310ddb82949667f5",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/marinegestuetzte-flugabwehr",
        "content_sha256": "e505b2f7d7dcb691e6f202d0deedada6f593aba3fc95b6e80c357f74a4fffb3a",
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
      "content_sha256": "dffb5636890a0a8b420c4530f268b212a762507dbdcaa50312aa669d14bc6053",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot dffb5636890a (vorher 040b13329863) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-31c2ac5b48b0cde3",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/vernetzte-flugabwehr-skynex",
        "content_sha256": "dffb5636890a0a8b420c4530f268b212a762507dbdcaa50312aa669d14bc6053",
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
      "content_sha256": "eb97330e3c8ea57b9f9740f416eb8a081ce1e310dbf9e6d04742e8f75d44321a",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot eb97330e3c8e (vorher f35f392c6fd1) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-39222fba59e057e4",
        "url": "https://defence-network.com/der-skyranger-kommt-nur-nicht-in-deutschland/",
        "content_sha256": "eb97330e3c8ea57b9f9740f416eb8a081ce1e310dbf9e6d04742e8f75d44321a",
        "text_sha256": "10017bb1640a498702502c949b7c032a9943cb6b0911a4c94f5970a12680533c",
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
      "content_sha256": "fd13218365ff0a5265528723ee9f655218b681ebba1ee941def6114f370e24c1",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot fd13218365ff (vorher 30f7d4fb7b61) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-397e8414020bdb92",
        "url": "https://suv.report/skyranger-30-technische-daten-bestellungen-und-interessenten/",
        "content_sha256": "fd13218365ff0a5265528723ee9f655218b681ebba1ee941def6114f370e24c1",
        "text_sha256": "17f9702fc289ef5829a02e79749a51f21634b62b81627c5a656d0632082c0a78",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3b27cf3712ca73d2",
      "claim_ids": [
        "C-025"
      ],
      "content_sha256": "821dd1bce62ab04d8157be99c29450da5556efcc67fc7b38407839e821c3f0ca",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "source_id": "S-3c3ad4b4354adf5e",
      "claim_ids": [
        "C-019"
      ],
      "content_sha256": "e1b31846edb395a4cc573986dc72d00827dcc2f4c1bc6abd33afc397f78fdfb8",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e1b31846edb3 (vorher b76cd63e3f82) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-3c3ad4b4354adf5e",
        "url": "https://orf.at/stories/3349582/",
        "content_sha256": "e1b31846edb395a4cc573986dc72d00827dcc2f4c1bc6abd33afc397f78fdfb8",
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
      "content_sha256": "54c6af7ca0efd769b10eec3cfeab582c85cde12b9b7d04d7f47b2a1c619a5680",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 54c6af7ca0ef (vorher 36ac5a680eba) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-3cb560602baefeec",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-defence-australia",
        "content_sha256": "54c6af7ca0efd769b10eec3cfeab582c85cde12b9b7d04d7f47b2a1c619a5680",
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
      "content_sha256": "a1bfa09115d6895e8938d244edabe28f932831f5bd85b8aed861df186d4920e1",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot a1bfa09115d6 (vorher b9d93b1676f9) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-3d1ac94ea50adfec",
        "url": "https://euro-sd.com/2025/12/major-news/48184/sweden-orders-more-iris-t-sls/",
        "content_sha256": "a1bfa09115d6895e8938d244edabe28f932831f5bd85b8aed861df186d4920e1",
        "text_sha256": "d699370505629841f71d836fb84f40f8b877fdbd48bd2768a66b88649353c714",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3dad8b811c925694",
      "claim_ids": [
        "C-024",
        "P-REG-RO-01",
        "T-EV-03"
      ],
      "content_sha256": "214decfe1cd910eedff5de83482a93f410fb63d3e92a852c34d543790d07098c",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
        "C-007",
        "C-026",
        "C-027"
      ],
      "content_sha256": "c11beae5fad77f523517e80ce37652a372d2cfaa8ca144cc2213913108aae7d7",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot c11beae5fad7 (vorher 04017585d62b) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-3f67bc2e13a1b02e",
        "url": "https://www.rheinmetall.com/en/media/stories/2026/rheinmetall-a-powerful-partner-at-ukraine-side",
        "content_sha256": "c11beae5fad77f523517e80ce37652a372d2cfaa8ca144cc2213913108aae7d7",
        "text_sha256": "87cea3e94beb1ac017e472b3118789cfb310c62a08912506c09116294fa6f985",
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
      "content_sha256": "129834744f9e172d6feae5497bad9dd8d8692f9d8bf38018432b3efdcaad0aee",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 129834744f9e (vorher b913794ff365) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-47771a7dd8c927d5",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/10/2026-10-12-american-rheinmetall-auf-der-ausa-2026",
        "content_sha256": "129834744f9e172d6feae5497bad9dd8d8692f9d8bf38018432b3efdcaad0aee",
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
      "content_sha256": "0757328e55970f7f5670dbe1de819a490098ae4cfa62c52df9467c1bf2c444bd",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 0757328e5597 (vorher 69985ee16ab4) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-4789a4ac6acb59aa",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/12/2025-12-12-rheinmetall-liefert-skyranger-30-fuer-die-niederlaendischen-streitkraefte",
        "content_sha256": "0757328e55970f7f5670dbe1de819a490098ae4cfa62c52df9467c1bf2c444bd",
        "text_sha256": "42702b14ad1b63075ce2d4be5b035117ee7fc9abebf1fd6d2d81ebebbceaa524",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4a13b2786b5cc66a",
      "claim_ids": [
        "P-VS-04"
      ],
      "content_sha256": "3d373c4b9a1cf63deb198ce8b1ca271b99a8cfb187c10744ac4ba53b9df1a301",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "8713939cb3a19571200fdf9ea2df86f75e608d6137396740db8e594b0c0475d7",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 8713939cb3a1 (vorher 6d21580346da) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-4d0e53f502fb320c",
        "url": "https://www.rheinmetall.com/de/unternehmen",
        "content_sha256": "8713939cb3a19571200fdf9ea2df86f75e608d6137396740db8e594b0c0475d7",
        "text_sha256": "b5116ece10ad1ad5dfd2da5416b20950dfe90e0a24bc4e45b9f81caeaecef783",
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
      "content_sha256": "ebbc5bc07b79426abce867690ecb23e38483c789e89d9ede85f0fd23be69c4c8",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot ebbc5bc07b79 (vorher dd5daa36815d) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-4e85b953fe46a8de",
        "url": "https://militarnyi.com/en/news/poland-receives-first-short-range-air-defense-system-under-pilica-program/",
        "content_sha256": "ebbc5bc07b79426abce867690ecb23e38483c789e89d9ede85f0fd23be69c4c8",
        "text_sha256": "e1ae60a73ea14612d648fea5a917083986380776c511c3ada301d80abbc2941b",
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
      "content_sha256": "f0b28b2a0225fbe556f00bdf3b075a2c49402447a1beca70fcc1ae52abf9fcd9",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot f0b28b2a0225 (vorher e7da0e621a8a) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-4f9807383dbfe574",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-canada/ueber-uns",
        "content_sha256": "f0b28b2a0225fbe556f00bdf3b075a2c49402447a1beca70fcc1ae52abf9fcd9",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "62b47d1e358336f6bbbacf799f3a6bad351659299f4fdd33815f93502b4b9a56",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 62b47d1e3583 (vorher ced56c7b4fc2) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-502271d8acddfb1e",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/06/2024-06-19-rad-and-anduril-industries-sign-mou",
        "content_sha256": "62b47d1e358336f6bbbacf799f3a6bad351659299f4fdd33815f93502b4b9a56",
        "text_sha256": "8e922057d76a1f57edd8251f92761049e4136ffab9bca3a8ba6436e594675f59",
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
      "content_sha256": "48d82976e885c0c3162c983b9e5f5bae441e6758aa0de9e125a32f5adeb02435",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 48d82976e885 (vorher 51ab350e5085) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-504b2773565ae51b",
        "url": "https://euro-sd.com/2026/01/major-news/48772/new-diehl-production-site/",
        "content_sha256": "48d82976e885c0c3162c983b9e5f5bae441e6758aa0de9e125a32f5adeb02435",
        "text_sha256": "d9ae4d46624b02b28db16a0dde47dd550db629c8f3a9af51253121a1ea2f473e",
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
      "content_sha256": "854c32c953a40724545adaf89efb43e50f9059019aecc42775bb1d8423f167fb",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 854c32c953a4 (vorher a67590ae0f4f) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-513daa2ae2be3e14",
        "url": "https://www.rheinmetall.com/de/media/stories/2026/rheinmetall-ein-starker-partner-an-der-seite-der-ukraine",
        "content_sha256": "854c32c953a40724545adaf89efb43e50f9059019aecc42775bb1d8423f167fb",
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
      "content_sha256": "87f17fabed589a3dcec5fa287c6486b63f5a639994b5616f5ac331a5cf401854",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 87f17fabed58 (vorher 0993d44f976c) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-51d8de61559f69f0",
        "url": "https://defenceleaders.com/news/uk-eu-defence-fund-talks-collapse/",
        "content_sha256": "87f17fabed589a3dcec5fa287c6486b63f5a639994b5616f5ac331a5cf401854",
        "text_sha256": "c2b9bcc0383e07a500faaaad37356262fd0e87f115b77cfbff7ee0fb8f335145",
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
      "content_sha256": "5c6bc2c92ecc6ff78d7115dfc1601e704c0a7de5db67e9872dadebd835a20fa7",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 5c6bc2c92ecc (vorher 75cf397990ec) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-5366eb8816ff2cea",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/06/2025-06-18-strategic-partnership",
        "content_sha256": "5c6bc2c92ecc6ff78d7115dfc1601e704c0a7de5db67e9872dadebd835a20fa7",
        "text_sha256": "bfe48629645a8f70e55a9612f769c20db149191035ec06cf82090ca3bceb5daa",
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
      "content_sha256": "ac7a0daaa3be2417a688adc85de93e94df564bc8aa1231d3397ec01676069795",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot ac7a0daaa3be (vorher 46169a0ab9c3) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-5a9d049f8f71abd3",
        "url": "https://esut.de/2026/09/meldungen/74575/roman-koehne-ceo-rheinmetall-air/",
        "content_sha256": "ac7a0daaa3be2417a688adc85de93e94df564bc8aa1231d3397ec01676069795",
        "text_sha256": "32e3643ab7c41c4581d5de07f61b38ed4deb734c47a6e568351d229abdcfde66",
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
      "content_sha256": "52f183e6413e66ac53e0f672309263822fcce79f3499fafdeffbe5062292f0ce",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 52f183e6413e (vorher cd16054e8bfe) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-5b8b39f37cd6b51d",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme",
        "content_sha256": "52f183e6413e66ac53e0f672309263822fcce79f3499fafdeffbe5062292f0ce",
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
      "content_sha256": "53d7e8bdf34c61d6e6963c0af9211cd67b2eb50f4a426a8dab62f1c0ae08fd48",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 53d7e8bdf34c (vorher efcfae13d46a) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-5ba566671c688dae",
        "url": "https://thedefensepost.com/2025/07/28/denmark-vl-mica-procurement/",
        "content_sha256": "53d7e8bdf34c61d6e6963c0af9211cd67b2eb50f4a426a8dab62f1c0ae08fd48",
        "text_sha256": "bc64a6d728cbe918f785de3d72f6dd032ade1ec704503e12dca80c949338b7e5",
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
      "content_sha256": "1136b2ddeaac3550055310f89fa40db509500f3c7435c1f4785ef2f8fdb1014f",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 1136b2ddeaac (vorher 5e564f3c06ba) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-5bb9a49af968005c",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/11/2024-11-06-umbildung-des-rheinmetall-vorstands",
        "content_sha256": "1136b2ddeaac3550055310f89fa40db509500f3c7435c1f4785ef2f8fdb1014f",
        "text_sha256": "1e0ff76e5f707ba31e19862574fa4c54cb7fce45da39b05a1ab6ed32937ce573",
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
      "content_sha256": "ef7b35c2a8b33c8d99f16836dc0859fa0fb4bc7841ae679e7a5da5fed7313217",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot ef7b35c2a8b3 (vorher 52992260fe47) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-5dad3a27cd832a61",
        "url": "https://investlithuania.com/news/groundbreaking-ceremony-in-baisogala-rheinmetall-and-lithuania-build-artillery-ammunition-plant-on-natos-eastern-flank/",
        "content_sha256": "ef7b35c2a8b33c8d99f16836dc0859fa0fb4bc7841ae679e7a5da5fed7313217",
        "text_sha256": "c3876559a998b611c18b0402657418ad35ea31ee9d884d85cc65d0f2b8e54436",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5f102cfea2da2738",
      "claim_ids": [
        "T-EV-03",
        "T-EV-09"
      ],
      "content_sha256": "70b17f8f578df934e3a6d2bf8631acf980f14b940352268a45f613d3e8ca2113",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "source_id": "S-6282cce4ae4b577f",
      "claim_ids": [
        "C-017"
      ],
      "content_sha256": "00421d7b86b7f0166d9ff9dff27d5f69492417cd49d4ab64fbf34c4677c02463",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "7809766cb866cc92a8079817306b31e976b6b4af5fc5c3f2a1ac7568aef4435d",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 7809766cb866 (vorher ad34fa9059b3) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-63ef3755ffe55169",
        "url": "https://www.sipri.org/databases/milex",
        "content_sha256": "7809766cb866cc92a8079817306b31e976b6b4af5fc5c3f2a1ac7568aef4435d",
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
      "content_sha256": "8aff1dac23e1acf83cafd48e6fe2015588d6efb53727c67ee0d6989db4ae8d58",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 8aff1dac23e1 (vorher 8524f2971bcd) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-6410acb24c745d46",
        "url": "https://suv.report/skyranger-30-auslieferung-ab-q4-2027/",
        "content_sha256": "8aff1dac23e1acf83cafd48e6fe2015588d6efb53727c67ee0d6989db4ae8d58",
        "text_sha256": "2e94f19ccb0a88febaa80ca3c7e26d5f3ce78123bc8b4c17442177fda91220f2",
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
      "content_sha256": "958feaff71fa70ff87190bd89df11dedcba8263c04256b8f46d45f015e4cddd2",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 958feaff71fa (vorher 600bbe33f593) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-6a3c2e1e456f2080",
        "url": "https://www.aoshearman.com/en/insights/safe-update-financial-assistance-tentative-allocation",
        "content_sha256": "958feaff71fa70ff87190bd89df11dedcba8263c04256b8f46d45f015e4cddd2",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "dc046ada7de1b74a83d324e30825f6b19098181974570f7f4666315717fdaa7f",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot dc046ada7de1 (vorher a1f7e7677f9f) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-6bdb338d23c29e11",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-24-romania-orders-skyranger-35-air-defence-systems-from-rheinmetall",
        "content_sha256": "dc046ada7de1b74a83d324e30825f6b19098181974570f7f4666315717fdaa7f",
        "text_sha256": "841e2df5713cce7f7fe28a88b426179daa60c44193b3ce90a375c63fa228fd34",
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
      "content_sha256": "cc4edb4b83eeed7034abcf730db6e75c5e1ba649ff07098f996b9d6bfddc07a0",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot cc4edb4b83ee (vorher 23ace4714ef8) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-6ceae77f0e11c121",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/12/2025-12-16-rheinmetall-demonstrates-drone-defence-capabilities-in-finland",
        "content_sha256": "cc4edb4b83eeed7034abcf730db6e75c5e1ba649ff07098f996b9d6bfddc07a0",
        "text_sha256": "675e4c0c6ee83bafdb9f1b4e7dd412f973933fd63dcfb8a7e8170f4bc3488637",
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
      "content_sha256": "e3a8a1e4c3e588617222d5cab22930e44d0f7a82534c20561cb06ec01f569016",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e3a8a1e4c3e5 (vorher 950bc29ce900) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-6d57eca962a765ae",
        "url": "https://news.lockheedmartin.com/2026-07-07-Lockheed-Martin-and-Rheinmetall-Move-Forward-with-ATACMS-Co-Production-in-Europe",
        "content_sha256": "e3a8a1e4c3e588617222d5cab22930e44d0f7a82534c20561cb06ec01f569016",
        "text_sha256": "8d48de5bd9dd293c2b88840227d88fcb7bc6d9dc6dbbfcadd7730d0d62c65cbf",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "bd2789ca676e5a95ddd1b9bb976cb8b42281758a8dac8ceff46dec28e212bc9a",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot bd2789ca676e (vorher cb1d3a52c783) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-747870b3bc879dff",
        "url": "https://www.rheinmetall.com/de/unternehmen/divisionen/power-systems",
        "content_sha256": "bd2789ca676e5a95ddd1b9bb976cb8b42281758a8dac8ceff46dec28e212bc9a",
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
      "content_sha256": "b4be96a2281c4c928fd55c2322251b2ef29a225f98e024f8b9ea32ebec834d9d",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot b4be96a2281c (vorher 3438ab3e7e47) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-764b0868c9a4f470",
        "url": "https://www.army-technology.com/news/denmark-samp-t-ng-defence-contract/",
        "content_sha256": "b4be96a2281c4c928fd55c2322251b2ef29a225f98e024f8b9ea32ebec834d9d",
        "text_sha256": "3187f8a60999bb68767b730e16181e0ecfe46d16057302cf798bd2f7a438c4e2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-76d1cd6d4bfaa83c",
      "claim_ids": [
        "T-AD-03"
      ],
      "content_sha256": "c7e6d1442db883fc57fd0376aa962d8ebe202cbe0cb04844ba59f57eee1a1420",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "7dfb80098d90e047a23449ac46dc40260d202843363a3ab2b9dffa437e49bd88",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 7dfb80098d90 (vorher 4f36a1499507) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-77116a48034eea1f",
        "url": "https://esut.de/2024/09/meldungen/53536/ergaenzung-zur-daenischen-bestellung-von-skyranger-30/",
        "content_sha256": "7dfb80098d90e047a23449ac46dc40260d202843363a3ab2b9dffa437e49bd88",
        "text_sha256": "6ad004ef3f318bf88b46a5f92d53775d6c0f3510de1ad8f80e212f6c785bdd68",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7730735b980263ed",
      "claim_ids": [
        "M-MKT-SIPRI-00"
      ],
      "content_sha256": "6cc3a30b1064f9f02e60236667eef82e08cad42910ce630909d004ad2c398a9d",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "e27a0830059503756c7a962f0244e55ea54fe1770c3483354d81cfdc6b70245f",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e27a08300595 (vorher cc39e0e7a65a) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-7b3ad8192958d374",
        "url": "https://www.iceye.com/newsroom/press-releases/iceye-and-rheinmetall-win-major-contract-worth-billions-for-space-reconnaissance",
        "content_sha256": "e27a0830059503756c7a962f0244e55ea54fe1770c3483354d81cfdc6b70245f",
        "text_sha256": "0723468c4325f3e842ec12d96d963fed6de531fd88f09515451438e0a5a0789f",
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
      "content_sha256": "fbc747acb29f614fbd00aa84a5b0b53930a46eb5644e2866c8f44bc39aa31270",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot fbc747acb29f (vorher 6443f41f5ba7) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-7c3ae12304f6c154",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/02/2024-02-23-rheinmetall-liefert-skyranger-30-an-oesterreich",
        "content_sha256": "fbc747acb29f614fbd00aa84a5b0b53930a46eb5644e2866c8f44bc39aa31270",
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
      "content_sha256": "43fa21c9efbee9aa8180218374cecfdb64729ce336978b4f443f6e86dafc0512",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 43fa21c9efbe (vorher 96e9e274cf30) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-7d3cceefdfc28f58",
        "url": "https://www.rheinmetall.com/de/unternehmen/tochtergesellschaften/rheinmetall-expal-munitions",
        "content_sha256": "43fa21c9efbee9aa8180218374cecfdb64729ce336978b4f443f6e86dafc0512",
        "text_sha256": "3671bf9b2bedd20cc67ca04f2def0e5c6e62695aaa0f5bb53ecf08c189464cc7",
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
      "content_sha256": "122f26e11cb9b766937970f952e822c0a56cfdefe7839fa597ca7e1a71fa09c9",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 122f26e11cb9 (vorher 149e01c8c15c) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-8119028d88f698cb",
        "url": "https://esut.de/2025/11/meldungen/65265/neue-distanzwirkung-im-nahbereich-defendair-kommt/",
        "content_sha256": "122f26e11cb9b766937970f952e822c0a56cfdefe7839fa597ca7e1a71fa09c9",
        "text_sha256": "2b63a20d9bef16bfc2fadac0d627b8b8953dcae0af09c5f3d92b186aa833aae3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-827c64d441de8f6e",
      "claim_ids": [
        "P-REG-NORD-01"
      ],
      "content_sha256": "4b2645d68352518aed6f3f683e7b87dc3c4493ebc65153223fd9c45d20939f49",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "source_id": "S-84a5e99e7ff45dc4",
      "claim_ids": [
        "M-AT-SKR-01"
      ],
      "content_sha256": "350e9304c263f7df6cc9330ecb9e800bb7c3ab4b13aa26ff8dd26ed340c319aa",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 350e9304c263 (vorher 95b4201e2875) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-84a5e99e7ff45dc4",
        "url": "https://militaeraktuell.at/en/pandur-evolution-with-skyranger-for-the-anti-aircraft-batteries/",
        "content_sha256": "350e9304c263f7df6cc9330ecb9e800bb7c3ab4b13aa26ff8dd26ed340c319aa",
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
      "content_sha256": "7d69bd453b61989a46ce1ee3f13619235323a2d781bb1f8ebbfe4fcfdd453aae",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 7d69bd453b61 (vorher 68e577e87fa1) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-860fb5a5ec516912",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/drohnenabwehr-toolbox",
        "content_sha256": "7d69bd453b61989a46ce1ee3f13619235323a2d781bb1f8ebbfe4fcfdd453aae",
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
      "content_sha256": "c9ad5950b3906c9261c0b1c4a092fd5bacd8fc3352e082adcc3c8b0feff66880",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot c9ad5950b390 (vorher 043d07181531) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-879737fc228c4bec",
        "url": "https://esut.de/2026/09/meldungen/streitkraefte/75038/zwoelf-25-mio-bundeswehr/",
        "content_sha256": "c9ad5950b3906c9261c0b1c4a092fd5bacd8fc3352e082adcc3c8b0feff66880",
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
      "content_sha256": "f0d7344c838c2842c8e71099e286d62ede05a2195e41275ec1cc522e91ec9c16",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot f0d7344c838c (vorher 21c3a52cb14e) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-92d7be3f0dda7317",
        "url": "https://esut.de/2026/07/meldungen/72696/rheinmetall-und-mbda-realisieren-das-laserwaffensystem-fuer-die-deutsche-marine/",
        "content_sha256": "f0d7344c838c2842c8e71099e286d62ede05a2195e41275ec1cc522e91ec9c16",
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
      "content_sha256": "d7a899e51a5ed4fcc6dac923bfedecef955fba24bceda99b96613d96c37162ba",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot d7a899e51a5e (vorher 037c66f74678) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-931d769d72f5fc8d",
        "url": "https://www.euronews.com/business/2026/06/24/rheinmetall-sinks-as-germany-axes-mega-warship-project-after-spending-2bn",
        "content_sha256": "d7a899e51a5ed4fcc6dac923bfedecef955fba24bceda99b96613d96c37162ba",
        "text_sha256": "734c6375a34acf9faa8dc7b69f5c0a919b269742c19f6809f1d289f4bddd78c7",
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
      "content_sha256": "db07f482444ef2d8c307e3d05467883320819b8d41e5047cca5f14a056f08952",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot db07f482444e (vorher 65297495bd25) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-957ebff673ab8d20",
        "url": "https://www.defensenews.com/global/europe/2024/01/26/rheinmetall-italia-touts-ukraine-deployment-of-skynex-air-defense-gun/",
        "content_sha256": "db07f482444ef2d8c307e3d05467883320819b8d41e5047cca5f14a056f08952",
        "text_sha256": "a585926a18057c8a8b097f7b23410c570bdd2f0ebd8832a5d430b09e09fcb53c",
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
      "content_sha256": "2ad1b583f0ef795057c24b9f20a8dfed6491aa5f982b3f2816b942fd698f35e2",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 2ad1b583f0ef (vorher 4b74fd9eeb54) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-96bd500dc205c229",
        "url": "https://www.grosswald.org/skyranger-30-programme-slips-16-months-bundeswehr-rejects-rheinmetalls-bridge-solution/",
        "content_sha256": "2ad1b583f0ef795057c24b9f20a8dfed6491aa5f982b3f2816b942fd698f35e2",
        "text_sha256": "a245ac74f1b87c8090431d2a6375f147db80065b43289e1bce3b4e95137df06d",
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
      "content_sha256": "f1c6b0022367a5c3cf6ba8e5c0559c537667b55c2bcb0b5434117ae72c1f2816",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot f1c6b0022367 (vorher aa7cec407ca9) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-9bba6057c1bcc3e4",
        "url": "https://www.edrmagazine.eu/thales-strengthens-portugals-very-short-range-air-defence-capabilities-with-forceshield-system",
        "content_sha256": "f1c6b0022367a5c3cf6ba8e5c0559c537667b55c2bcb0b5434117ae72c1f2816",
        "text_sha256": "4aa16b0af3746e06165a971cde1f801da43f0c1608700b21ee10d220c7f00d85",
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
      "content_sha256": "42fdacb7591b73bfbf6fcf9f1c59eb3989529186e0b2c1ad561a09b82fbfc758",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 42fdacb7591b (vorher e17901caa037) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-9d01bc5d2a34d23a",
        "url": "https://thedefensepost.com/2026/07/09/lockheed-rheinmetall-atacms-europe/",
        "content_sha256": "42fdacb7591b73bfbf6fcf9f1c59eb3989529186e0b2c1ad561a09b82fbfc758",
        "text_sha256": "61310e6825ab2b09c536f6d026c1c1e6126ee1bde2bbc981f03fd06972f591b1",
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
      "content_sha256": "ee9bd8cb1555457baa0716619011060aabfb7a55f964754bee144c171afefe84",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot ee9bd8cb1555 (vorher c1313f0eaecd) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-9dd1c8db93851703",
        "url": "https://www.defensenews.com/global/europe/2026/09/23/germany-wants-to-manufacture-american-pac-3-interceptors-to-help-meet-global-demand/",
        "content_sha256": "ee9bd8cb1555457baa0716619011060aabfb7a55f964754bee144c171afefe84",
        "text_sha256": "b60d5b050e7d0d38d944d292386322399836981ce096dee804a2107b0c2eea62",
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
      "content_sha256": "d24115c1d3224b8e5183d7fd36b9c747d778f209764d83cf756be25eec39e37f",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot d24115c1d322 (vorher aef1ebaddc20) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-a21018e8e5b5c677",
        "url": "https://defensenews.com/global/europe/2025/09/12/denmark-picks-french-italian-sampt-air-defense-system-over-patriot",
        "content_sha256": "d24115c1d3224b8e5183d7fd36b9c747d778f209764d83cf756be25eec39e37f",
        "text_sha256": "13ac3f74eb82f6b60bc3623cad0446cf3d8b017bb6f9f51a2d2c5a22646caed2",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "source_id": "S-aa0faa4814b4b297",
      "claim_ids": [
        "M-SE-IRIS-01"
      ],
      "content_sha256": "1531bd8a709c0df487735068c27af17a767ec70517065bcfab1ccefb579c7246",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 1531bd8a709c (vorher 3c35204db80b) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-aa0faa4814b4b297",
        "url": "https://new.diehl.com/defence/en/press-media/news/sweden-procures-further-iris-t-sls-systems",
        "content_sha256": "1531bd8a709c0df487735068c27af17a767ec70517065bcfab1ccefb579c7246",
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
      "content_sha256": "ce1d0fb4e59a317e9492c3949a793475424e6043ec7198523bc05f6fa3aaa44a",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot ce1d0fb4e59a (vorher 97c73797c1e2) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-ace6606b74478d86",
        "url": "https://www.hartpunkt.de/flugabwehrkanonenpanzer-skyranger-rheinmetall-erwartet-noch-dieses-jahr-milliardenauftrag-von-der-bundeswehr/",
        "content_sha256": "ce1d0fb4e59a317e9492c3949a793475424e6043ec7198523bc05f6fa3aaa44a",
        "text_sha256": "ec81d729c8e3e0402ec770d727fd713a559c904d881c2065298f67972427a767",
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
      "content_sha256": "8426ce56780d9b2738c85f652359b2cd1e7b6c18627db12ca9dae7b328c9777c",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 8426ce56780d (vorher 480efd8f260c) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-b003618b3ae9eba2",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-02-rheinmetall-is-supplying-four-skynex-systems-to-an-international-customer",
        "content_sha256": "8426ce56780d9b2738c85f652359b2cd1e7b6c18627db12ca9dae7b328c9777c",
        "text_sha256": "fc389c8026a1273a5786c8c9d3664cfa54f2cf8b7ac522b694f2b77dfe19035f",
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
      "content_sha256": "cb97ed7e37f54970c4c4e587be60d6f8f8398aa96463ba69a435c56ed07e2f79",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot cb97ed7e37f5 (vorher fe23763867f9) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-b8a3496f93a22c8c",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/02/2024-02-27-bundeswehr-ordered-skyranger-30-mobile-air-defence-system",
        "content_sha256": "cb97ed7e37f54970c4c4e587be60d6f8f8398aa96463ba69a435c56ed07e2f79",
        "text_sha256": "332773cb6076bab9e35ab4480703da5c350b912b895766dc952886e95ec122aa",
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
      "content_sha256": "00b1abbde1e0bcc936e004c83527690f5e960f59e24e6bdf344cd3d2a0fbbb15",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 00b1abbde1e0 (vorher b5b3ba7b89a3) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-b99b85b72dbd1baf",
        "url": "https://www.hartpunkt.de/lieferverzoegerung-von-skyranger-flakpanzern-fuer-die-bundeswehr-erwartet/",
        "content_sha256": "00b1abbde1e0bcc936e004c83527690f5e960f59e24e6bdf344cd3d2a0fbbb15",
        "text_sha256": "341282a38394acd10803cf50ade188e5d78dd1aa39170fa968ae8f772d0df523",
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
      "content_sha256": "91d1c11792d4e62a8b1890f9b31b0b71ebc881ded7a24c98485aa349a40874df",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 91d1c11792d4 (vorher befdd4071f9a) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-bf3aaa0b85ea54a2",
        "url": "https://www.edrmagazine.eu/saab-bolide-2-more-punch-for-the-rbs-70-ng",
        "content_sha256": "91d1c11792d4e62a8b1890f9b31b0b71ebc881ded7a24c98485aa349a40874df",
        "text_sha256": "b994e612ddcdf91a54a24863a469f4349b17cace0fd530668d8e57f958c181a9",
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
      "content_sha256": "e07b66462d69233cdae27f8c621b4ead9e5846296436838ca23399c5c3abaab9",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e07b66462d69 (vorher bda9e63c53b3) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-c0d13e5db6387716",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-10-rheinmetall-showcases-its-cutting-edge-skyranger-air-defence-system-at-ila-2026",
        "content_sha256": "e07b66462d69233cdae27f8c621b4ead9e5846296436838ca23399c5c3abaab9",
        "text_sha256": "99cf4bb953f2ec864d8f864ba6b386c39e94ff6ea98e1f37416ad15d91a71c38",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "source_id": "S-cd51559c12c6bc2e",
      "claim_ids": [
        "T-EMP-03",
        "T-ID-01"
      ],
      "content_sha256": "1371db1ac5fc2cc0d53cac75d5795acb1f277d43ecefc2e378d33f2cd0b44fea",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 1371db1ac5fc (vorher 2ba36ea5ff5f) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-cd51559c12c6bc2e",
        "url": "https://www.rheinmetall.com/de/investor-relations",
        "content_sha256": "1371db1ac5fc2cc0d53cac75d5795acb1f277d43ecefc2e378d33f2cd0b44fea",
        "text_sha256": "ac5da61d99b6bbbcb07609b67ebdf3e7534e54ac538f1afe1b3d06cab6692701",
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
      "content_sha256": "7ed5454c04d604e788730a03b1ce57762cc64ab338cf30dfb7ff7c3c54a3381e",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 7ed5454c04d6 (vorher b04dced028a2) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-cede873d57924937",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-02-major-historic-contract-in-romania-worth-5-7-billion",
        "content_sha256": "7ed5454c04d604e788730a03b1ce57762cc64ab338cf30dfb7ff7c3c54a3381e",
        "text_sha256": "df3c1fe3255cb2b6821a588d7c83334b275d90cac5a1ce855f1f6191e6c146ec",
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
      "content_sha256": "c96e0f91fc53c42d0d2d32b02b3d1c2f7434967d7f256419e4db0412b1fd6bc5",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot c96e0f91fc53 (vorher 67976f09be6a) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-d1aafc1c9b0f1a75",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2024/09/2024-09-30-rheinmetall-supplies-skyranger-30-for-denmark-s-mobile-air-defense-system",
        "content_sha256": "c96e0f91fc53c42d0d2d32b02b3d1c2f7434967d7f256419e4db0412b1fd6bc5",
        "text_sha256": "2b8a49a9e1287f6fddb2c26de514204af6b3a80e885aa6215ac5638c091ca106",
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
      "content_sha256": "2582e9fc165d464df0ad0affc6ed2e3be1fe66ec7d98c1afd4a4b9b58d76f94b",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 2582e9fc165d (vorher c718b1a995e3) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-d2d239c37b99eddf",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2026/06/2026-06-15-rheinmetall-at-eurosatory-to-showcase-its-cutting-edge-skyranger-air-defence-system",
        "content_sha256": "2582e9fc165d464df0ad0affc6ed2e3be1fe66ec7d98c1afd4a4b9b58d76f94b",
        "text_sha256": "9fe75d53ae34c383577cb43f2fa18429c7478c1166bd4c5f4e530a27f1ff3dd6",
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
      "content_sha256": "d076d2512e8653dbbe0e13160a892709d9d3681212c67b99be8d9bb1aa47a4bd",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot d076d2512e86 (vorher 31a26606d4f2) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-d2ef86f50f08a3d3",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2023/12/2023-12-20-lynx-with-skyranger-30-for-hungary",
        "content_sha256": "d076d2512e8653dbbe0e13160a892709d9d3681212c67b99be8d9bb1aa47a4bd",
        "text_sha256": "413bb2266d480e01a77687898ae973fe5e17346e867689dd092623c2a1736210",
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
      "content_sha256": "d51e0e80538d0df8ad56557f480b63ea673216c327ed164b5622f5eae546f05b",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot d51e0e80538d (vorher 49b8163f8936) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-d32c73540389046f",
        "url": "https://www.boerse-online.de/dpa-afx/capital-ausruestung-fuer-das-heer-kommt-spaeter-546388.html",
        "content_sha256": "d51e0e80538d0df8ad56557f480b63ea673216c327ed164b5622f5eae546f05b",
        "text_sha256": "0f02d40456fee946bffecaf9856e27e27cacb48d1d4f25b74f4bcf8f4adf0e9a",
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
      "content_sha256": "4f0345d698a62d6a1dd8b803d6128313309801350d380c4141fc635fa5002a86",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 4f0345d698a6 (vorher 204133353423) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-d5ab9c70470a478d",
        "url": "https://www.rheinmetall.com/de/produkte/flugabwehrsysteme/stationaere-flugabwehr",
        "content_sha256": "4f0345d698a62d6a1dd8b803d6128313309801350d380c4141fc635fa5002a86",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "f190a19ec8c03470d43433c9c9db8af636e9eefc6de5f72eb6d0c1a9ed0d8b08",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot f190a19ec8c0 (vorher ba29fab0c319) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-d7c2de50db0d079d",
        "url": "https://www.berliner-zeitung.de/article/rheinmetall-chef-flugabwehrsystem-erfolgreich-im-ukraine-krieg-doch-handfeste-belege-fehlen-10004755",
        "content_sha256": "f190a19ec8c03470d43433c9c9db8af636e9eefc6de5f72eb6d0c1a9ed0d8b08",
        "text_sha256": "29bc24073135ab3eccde6f073c39e828539e2804d263df2d4e7612e137adeda0",
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
      "content_sha256": "6fc31d20b8a16c3dfb7fd172c3040031f5b9712ac9eba869c037db37fc271354",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 6fc31d20b8a1 (vorher f7573d469364) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-ddb1d21cd09da6cf",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/10/2026-10-01-rheinmetall-nordic-eroeffnet-neuen-standort",
        "content_sha256": "6fc31d20b8a16c3dfb7fd172c3040031f5b9712ac9eba869c037db37fc271354",
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
      "content_sha256": "a7f3eeaa3d7c14a540a5c61df358bf7710c7efb8e0b463a71fcaacf595789935",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot a7f3eeaa3d7c (vorher e74527e72bf4) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-ddd98359e4352c31",
        "url": "https://militaeraktuell.at/en/bae-systems-sweden-buys-tridon-mk2-air-defense-system/",
        "content_sha256": "a7f3eeaa3d7c14a540a5c61df358bf7710c7efb8e0b463a71fcaacf595789935",
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
      "content_sha256": "5bc95757cd3ed9c2470aa341d92be01be4fd22f1c1afb95f02abf65b37058507",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 5bc95757cd3e (vorher fbbd972c7db8) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-dffd12785279e32f",
        "url": "https://euro-sd.com/2024/07/major-news/39225/lithuanian-mshorad-order/",
        "content_sha256": "5bc95757cd3ed9c2470aa341d92be01be4fd22f1c1afb95f02abf65b37058507",
        "text_sha256": "d569379bfabebf4018578ef7e31d1afe29f866a935ff6d8b5326db64a7c5e25a",
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
      "content_sha256": "6240476cd4af036d4587b70a0d5677f576723da74bcf93b51a26b115138c6a97",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 6240476cd4af (vorher 304ecfd117af) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-e4c101cb061aafcf",
        "url": "https://www.rheinmetall.com/de/investor-relations/veroeffentlichungen/stimmrechtsmitteilungen",
        "content_sha256": "6240476cd4af036d4587b70a0d5677f576723da74bcf93b51a26b115138c6a97",
        "text_sha256": "201f3c16fbd2113e8597d751b41e13afa0c0067a12ea5cc3842c7ffdda166ae5",
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
      "content_sha256": "45f9adab83562b80329fb1583d74c9a42e564d6bb89d38d3a5dc455fe9a9c193",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 45f9adab8356 (vorher fedb124de4ba) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-e6e94711a0973745",
        "url": "https://defence24.com/armed-forces/poland-concludes-a-massive-shorad-contracts-with-camm-missiles",
        "content_sha256": "45f9adab83562b80329fb1583d74c9a42e564d6bb89d38d3a5dc455fe9a9c193",
        "text_sha256": "b9ff2054d58229187fc1dc8daf0e4ee70a757c040ec49823ad606e3c0660fc24",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e6f358904e19e4e8",
      "claim_ids": [
        "P-AD-08",
        "P-REG-DE-01"
      ],
      "content_sha256": "24eb1efde161bb5cdaa637eb444a3bb9dae4c14e94535b0a4b40281b8ff76202",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "22a4582ac1775ee3e3e7ecd534b11cbd6855bd98aba9ccda34146472a762d8e4",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 22a4582ac177 (vorher adfeab575b4d) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-ea6a47ff86b90b1c",
        "url": "https://www.rheinmetall.com/de/investor-relations/aktie/aktionaersstruktur",
        "content_sha256": "22a4582ac1775ee3e3e7ecd534b11cbd6855bd98aba9ccda34146472a762d8e4",
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
      "content_sha256": "f95b77552ce8b42b06530e58cff44b11ece99dacd84ebaa17dbbded837cf7bc9",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot f95b77552ce8 (vorher cf19f41aafe5) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-eadffcced857ac38",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/10/2025-10-10-rheinmetall-skyranger-35-ukraine",
        "content_sha256": "f95b77552ce8b42b06530e58cff44b11ece99dacd84ebaa17dbbded837cf7bc9",
        "text_sha256": "915775679f6b57a4e67e4e309024259d9a3f7b1b209da2c635acb8d624eb85a7",
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
      "content_sha256": "940f6446ef9560cfeb8d7f213c7131fe3bb82f48ae10e22980fb71cabb4cbc0b",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 940f6446ef95 (vorher de77500835c0) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-eb7f63760aba3e64",
        "url": "https://euro-sd.com/2025/03/major-news/42935/over-5000-lmm-for-ukraine/",
        "content_sha256": "940f6446ef9560cfeb8d7f213c7131fe3bb82f48ae10e22980fb71cabb4cbc0b",
        "text_sha256": "a82a16caa1dbe34dfed15348effc7a6de014bafbefcd955f01521bfd913b284e",
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
      "content_sha256": "e3c271f9d6b045b386aea15948d75061086843d6d0d9de8b511005c88a576193",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e3c271f9d6b0 (vorher 957f427d0f98) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-ed85256fd87c2a74",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/10/2026-10-07-rheinmetall-und-praetorian-aeronautics-liefern-containerisiertes-drohnenabwehrsystem-aerie",
        "content_sha256": "e3c271f9d6b045b386aea15948d75061086843d6d0d9de8b511005c88a576193",
        "text_sha256": "68a7ee9921560fa6e059e1b48cad35b8adc4b31ce70977bcaa7226be6f6311c5",
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
      "content_sha256": "6e642a1b5085dbaabd9db4e06e778069b763781583254f5192051936a9198161",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 6e642a1b5085 (vorher 9a2205d18f53) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-eddf31ac6c75fbe9",
        "url": "https://thedefensepost.com/2026/04/06/sweden-bae-saab-deals/",
        "content_sha256": "6e642a1b5085dbaabd9db4e06e778069b763781583254f5192051936a9198161",
        "text_sha256": "1471cadc2c8d933d5917ec38d28ff200884446d3046f88ee4e06b443339b5494",
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
      "content_sha256": "1a37c9ee18af8613b2615404df0aa5135b1bdbad6bbc364de68b9ab82592ee42",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 1a37c9ee18af (vorher e78f5f76c76e) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-f129b4e8889709a9",
        "url": "https://www.calibredefence.co.uk/?p=6167",
        "content_sha256": "1a37c9ee18af8613b2615404df0aa5135b1bdbad6bbc364de68b9ab82592ee42",
        "text_sha256": "7d13d7b8610b2b14e67dafc9bf99e84fb9ad68112dcc422886a397c5197fdb6e",
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
      "content_sha256": "95be688d5c402eb106b8e05b5b0b275706140d45f4ddfa25baf28f275abcd821",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 95be688d5c40 (vorher ba13e17ae5d4) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-f3c15f4b90f4bfc8",
        "url": "https://militaeraktuell.at/oesterreich-ist-der-sky-shield-initiative-beigetreten/",
        "content_sha256": "95be688d5c402eb106b8e05b5b0b275706140d45f4ddfa25baf28f275abcd821",
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
      "content_sha256": "a34e8b679a34a63f2af4e1b2a374ff1af7f71e1a4682ade899c97efb79f51219",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot a34e8b679a34 (vorher f574d9d92e7c) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-f4643db24ca2fc22",
        "url": "https://esut.de/2025/08/meldungen/62886/rheinmetall-eroeffnet-groesstes-munitionswerk-in-europa/",
        "content_sha256": "a34e8b679a34a63f2af4e1b2a374ff1af7f71e1a4682ade899c97efb79f51219",
        "text_sha256": "2cc0a25f63fd89aac590a480a6a4c90d176de9d986316ca3599b493ff55b222b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f4730b21412bb02a",
      "claim_ids": [
        "C-007",
        "C-033",
        "C-036",
        "C-041",
        "C-042",
        "P-REG-OWN-01",
        "T-EV-03"
      ],
      "content_sha256": "138727c9936e18cce3a3e85772863f35c22cc8d842ec9baee46b5cbf5035bd6d",
      "capture_kind": "http-original",
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "e17070b19ca32d9e5a320d3780ddf93e7418970962404d8bfd3964a8facec880",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e17070b19ca3 (vorher b68ad3b7aa97) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-f562ccee195198fd",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2024/01/2024-01-25-startschuss-fuer-luftverteidigungssystem-nnbs",
        "content_sha256": "e17070b19ca32d9e5a320d3780ddf93e7418970962404d8bfd3964a8facec880",
        "text_sha256": "9da7f1ae06d0720edfc4bd681f96e9c963f40c502309ca272e8d78d7a67dd2eb",
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
      "content_sha256": "5d4a47f165fca11c9fabbbe8f26e59e954ef148b03bd73135c020ca7ec36409e",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 5d4a47f165fc (vorher 7bdbe7b4f408) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-f8577da3c9c0698e",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/01/2025-01-15-italien-beschafft-skynex-flugabwehrsystem",
        "content_sha256": "5d4a47f165fca11c9fabbbe8f26e59e954ef148b03bd73135c020ca7ec36409e",
        "text_sha256": "6705e1a28054b7dadf28a729c392bc7fccb5a9daf69ab32e99381e9af268fe83",
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
      "note": "Snapshot unverändert; Belegstellen aus Runde 2 bestätigt.",
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
      "content_sha256": "4c4ab1e0c51d85dcdb3bd5b56a720af4040e85cf94873789c3879f6e295b56f6",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot 4c4ab1e0c51d (vorher 70f80f31097a) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-faeb7be1bb92f0b5",
        "url": "https://www.gov.uk/government/news/4-billion-uk-poland-air-defence-deal-strengthens-european-security",
        "content_sha256": "4c4ab1e0c51d85dcdb3bd5b56a720af4040e85cf94873789c3879f6e295b56f6",
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
      "content_sha256": "e58817482e151a429a366f8daf8567ec830454e53ec89dd93b81e3a7da549db8",
      "capture_kind": "http-original",
      "note": "Neuer Snapshot e58817482e15 (vorher fb2741c9a4ca) gelesen; Belegstellen der zugeordneten Claims unverändert vorhanden.",
      "snapshot": {
        "source_id": "S-fce8c647daaea30b",
        "url": "https://www.saab.com/newsroom/press-releases/2025/saab-receives-order-for-ground-based-air-defence-from-sweden",
        "content_sha256": "e58817482e151a429a366f8daf8567ec830454e53ec89dd93b81e3a7da549db8",
        "text_sha256": "a0b0e78bef39c162dbe54cda7b485edab746852bf653b717ec8b7605b6c1778b",
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
      "id": "C-033",
      "evidence_review": "Nur Zuordnung geändert (Cluster-coverage/report_log ohne SEC-Quelle); Claim und Belege (GB 2025, PM 30.04.2025) unverändert, Runde-2-Befund bestätigt.",
      "fingerprint": "0615487d5b266c966f85f6b63361771f8950011c43b746f3901cfa5bd2a72ae9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-036",
      "evidence_review": "Nur Zuordnung geändert (coverage-Eintrag Lockheed ohne SEC-Quelle); Claim und GB-Beleg unverändert, Runde-2-Befund bestätigt.",
      "fingerprint": "181a77ba439706c4e40f1deaeb4a84b48fe741953258d7234b9d0815070cd123"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-051",
      "evidence_review": "Neuer Snapshot der Stimmrechts-Seite: nur Datumsformat geändert (04/03/2026 → 04.03.2026 usw.); alle Meldungen und Quoten (BlackRock 7,33 %, Goldman 4,06 %, Morgan Stanley 4,37 %, BofA 4,64 %, UBS 3,83 %, FMR 2,78 % am 25.09.2026) unverändert bestätigt.",
      "fingerprint": "c2c6e8d3a97b125dff73a12387786950d2aad24d8c6082e6e8738ea688a4be39"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-SKR-02",
      "evidence_review": "Neuer S&V-Snapshot (21.01.2026): 93 Systeme von vier Staaten, 18 Monate/ab 2028, Vertragsumfang unverändert vorhanden.",
      "fingerprint": "76f5e999ff3f8b0aeb2165baef7741f628de2d6da858fd35e039b61253f4cd7c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-NO-01",
      "evidence_review": "Neuer Snapshot der PM 01.10.2026: Eröffnung 1.10.2026, Entwicklung/Produktion/Systemintegration/Logistik/Kundenbetreuung, 4.579 m², 100 Mitarbeitende unverändert. Neue Präsenzaktivität A-NO-SKO-DEV (development, own, operational, gleiche site_id S-NO-SKO, Ownership 100 %) ist durch diesen Claim semantisch gedeckt; keine Doppelzählung des Standorts.",
      "fingerprint": "7aad3aad6159f033cf6bf244e05cb879f12599f5ca1616c3d9b2420811e981b5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-NORD-01",
      "evidence_review": "Nur Zuordnung der Region R-NORD geändert; Claim/Quelle/Snapshot unverändert, Runde-2-Befund bestätigt.",
      "fingerprint": "cf5550faa11277fe2142d111b200706829366b64f2cc0b9d911108d1ab1bdd50"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-OWN-01",
      "evidence_review": "Nur Zuordnung geändert (neue Aktivität A-NO-SKO-DEV referenziert den Claim); Claim/Quelle/Snapshot unverändert, Runde-2-Befund bestätigt.",
      "fingerprint": "33b494039fe48ca3ea7fe95b5c8015ae1b296f21aea05b2a415ad7711471bcb1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-06",
      "evidence_review": "Neue Snapshots Börse Online/dpa-AFX und finanzen.net: Zitate BAAINBw („ab Mitte 2027 … Mitte 2026“), „Performance … stark verbesserungswürdig“ und Rheinmetall-Gegenangabe (fünf Monate, 2027/2028) unverändert vorhanden; Änderungen nur Kurs-/Werbeblöcke.",
      "fingerprint": "0ec35e3a5ba38fe46698e3f5726a6809b3faf580960e6996f126fee02e71d14d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-007",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "3c944a2e91ca19602ad7b564cf1eb1415a8fa4136ec2a15874d7699a2d95c791"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-009",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "d507b169d1af3e607216d515bd3d1683f4f1b13133f78cc2c009a889d5e4db2f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-014",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "d43f70ddad509e73fdc7317f41aa7872803565eade8455b8fec5e16d43506d96"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-015",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "5fb41a31c24febb2c8184341b0da9cb13265c69b6e9a073ee58bca44f336f29c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-016",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "92485a8471326d9a84e5c5a1df2988b8878a28ba76aca2f9072ea4947068e5a8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-017",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "44ee0d3f68679de4a7867a2e1864dc9a5b2f32a6af3d24a570ea30854fb1cf80"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-018",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "3dd818a8efa696e6f00acd5ff4e00e73813bd35e25090d47d337422c9e34c71d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-019",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "277794f5f511651bbf260b75dfc90240a83cfea5716b14cac632040311ccc7fb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-020",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "6b0c75f155c0fa44acaed756a0c4dcd5e90f2170620e28d62a838ced1abc6535"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-021",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "6c467fd5a70f110d8d428180c4ce4ce21ee077fd9ca247905d7f5f32ee78db13"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-023",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "1235c111204920482d06d582b32133ab830053c214b8df2570b11af6755938fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-024",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "cfdf11a6f3b933aa69aa56b7afb68f400ebc2db91bf0e58931a590590450491d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-025",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "009394b9fbf93f82b48910e918675967a34fa30446f8b4a5b860544bf7075b02"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-026",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "053e449b74d7923d5d1ae785e514fe87c2f6f9f3d61445bd57660af7f409b0b0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-027",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "6d72426512248dfa12c286f565cd4d0f0532b459df4923f42a33400f2f26f2b1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-028",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "cf2c8feebe57e94b285e280f73086407b8b1a873b1f01508879edeb06c8cc3e6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-029",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "0ce4e19f79c1c474f971022d2a10aaa926fdf74cbc1bd260028da7c053665c09"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-030",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "68dcb878ca401b69f61780bea5583c75b677b61b2860537ddaab265533d23e01"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-031",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "26268ff19bf1814e75affc337a1ee4de13131343561d9d487ec4019672bea9a4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-034",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b382081b7dad29b2e2b9ab6c32e54f6f247502cd63e158193424a61f04265e67"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-035",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "9383faf9c9710af7378b0406fb8fd320ad3f42aa01b51f8bb9811d4d6758552c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-040",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b34df12bc76ed0806855f01f50c3bfae2cb844b67003f69161a8afb400e246d1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-041",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "489079e6185ba11b828826dededafba5a6c41973e91e99da9f501fd6007da148"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-042",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "cc0ae31feb2e76a8ff04736afd830d1ac12ef5ab2baf881f132c51857cf3a415"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-050",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "425d2adf02c0ad2b8d9fb07ab6ce40e4c9ab3f7b5cfd6329d2fe572c52fd0ced"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-052",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b7a89c2d18bc03d92fcd663b0db7d1ce30959024a686c50bb860eca405e3cbea"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-053",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "a4fcdb604c8141bf8bca96044ddd42a7b6b25b2034ba967a09e9925a1d9216c3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "H-PP-06",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "5e04a9e5e80e7cca02b753d0af45b8e757a293075230104e761d752cfc968792"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-AT-ESSI-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "f96ee5c27ee8ed8e78569be546dc35d9b7b3418491dfc1264016a6e4fa548f3b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-AT-SKR-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "8dd0444aeed53b191155f4ad14c9f38e5b22da014daa502b77d3d438361ac0a1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-AT-SKR-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "99fa6e35b6545f356ba070cc68a08f4345688fec14a28621490074402d85c0ae"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-CZ-MSH-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "356510e9545151bd9027551757a28d8e90bd66c36df411bc2e8df1a96920068a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-IRIS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "780c3ac7a7b0fa23b667c9c3288e33cdd33b30b6d1361d6412aa6ee9a4789142"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-IRIS-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "4e43dba38bd8b59530d474487cc3b0231e28d7633761cdbb785a9b9cbef985d9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-NNBS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "6b1c0380dd53633d2f57d5a6014cc0e54f4b92015bf5b76c0c2c1bbd91ddf981"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DE-SKR-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "2c80e285582399a55599c2ea7ca7905be31f5684686461aaeb0364723b59d3d6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DIEHL-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "2c048502b17962c7a3a09ed4cfc6f30ad596087bda9e8e2961bc0cf236d2710d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-GBAD-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "0b657e535e24119840a11ad437cc6f88d1a05308ebb635f0539c16d1e70c0bc5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-IRIS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "985b51347132f6cf9a78273c57190f3306bdce973f321d452e334405831b6654"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-SAMPT-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "469c82f68be002509d9baecd61c1b63ea40a8db44deb0c80b7d299ded2a66579"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-SKR-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "7811d962e34cf7693eed0a02dcde826d0bf8e220e8fb2ce742de48675d16f37b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-DK-VLM-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "8bf61462d780618aece24688a6d14d36311b18cab095fc455d59ea37b2cd607e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-EU-SAFE-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "068d269ece228361992285b8ab0edc0573ed18b5d2f9142ad88256e0d8562eef"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-EU-SAFE-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "0b4dee56da302265ffee51536194aac20bc59dc75db30f94aa5da2551dd48104"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-EU-SAFE-UK-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "91281ca1829f3f213b3842a89d17173c030f865f5d0487a3dbac2d9e493f4fd0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-IT-A2CS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "8bb6a42f1dce39af556f1821191da8cd4175ef3b6f033d44e6712c32a1ff4c3d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-LT-MSH-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "8481c3a02e66d2764bfbd1f78a938084c96116d9944c51e20e9efbb89009719c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-MKT-SIPRI-00",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "7ad9b826bf23aa31ea7c0692a06158aebcb1c6e4c02284a6bc10cbb21999bb60"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-NL-SKR-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "fde8e052b40a24e71490baa835579529aafdd4928a7f76447224382d87438f42"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-PL-NAREW-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "f30ddad37bbc0480a52341a7b92dee4b4d1c07abe4ce23aa5b675ad8387331fb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-PL-PIL-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "a22e4678ecfe33a603c859508db9aec82cdcbec294b529d027851b50da60cca5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-PL-PIL-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "f498906f684e2ca883b4269afefda3d1cac4431dc3fd45305090d8c99466b613"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SAAB-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "e68dc45ccfbcfbf2981a4e02443b3cbb3a6ad9951fd16f1c17d34f516fef0fbf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SE-IRIS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "15c1b174f0077d9391629910af8a428205aa0c0ee74427456cdaac603c0551fc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SE-RBS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "ad1cc94f584d9ab65ec17083e2903dcfd14a657b75757381c4423c8b582e1f26"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SE-TRI-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "353cc67f8c3b7d87893c4aff1f0047c444007b83ae7dce1bd0b4363f46e12e24"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-SKR30-ARCH-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "f6a736d6fd6ea93a4d703fbf2f772c1b2d69601abf8c3ff9c98f3dbba700e55e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-THA-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "35175efd16ccda666155364433bde58f767946dc0b81fee2050706af3bdf462b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-THA-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b82633af397157721e74a8fbee5c33e44cb6cec4a38fcc6b987d83b1a107d214"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "M-UK-SHORAD-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "5cd6f2e747356589d8fdce630313a7663eda589642e309cc0d6b1f3ddcf13aa1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AD-08",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "fe7599ccb8bc8ecfacf9b432dd01540ab6cbbf45b51bcdd09fa09744c80824bd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-AHD-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "2e731752af69e11ee87a213bc3867480289747989419210cd91fceeca9c920ae"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-CUAS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "d98c6e7b59e15bb11cf5bf1a15a240ec5576218777fc1480640f7e1ba2265550"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-CUAS-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "69f0f3bcd5ea885eb74b1bbbfbc8f1ba70765cc25460275f1b089e0c380a51cb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-CUAS-03",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "58f02fb6a1c04aeca7480e81728d3fbb41b87fc636e11624b3d515ea5287222e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-HEL-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "3a970dcc5f699d68f20e68ed06c54783fb236cc6f4e6bfec95cb3af1fedd6d10"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-NAV-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "c579588abd6ce587133eb294277e5f2fbf41430a8f461a31d5285807c126d692"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-PS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "cf2966c219dc62bf55e6109d25331f8afea8e760d160c14b5002e20d24bf1a8d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-AU-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "4d2a0747e33b8ca61d434831f2160f3f444aa03328b0ed661c2d03c8b59ca806"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-CA-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "fc149584bc1a969451889a5c577ab610df0cc8639256e54469804db134d50c00"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-CH-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "607aa486a103b258828a87aae6a75e2f1cd6c2189488364b611d2b8a18dd9ac8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-DE-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "a7cace17f7e3e6694e88e27e8922a37935a19a0020635a534ed2839fc91bab5f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-ES-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "6bed1537c6b457baeced10072bae2eb965f0ef1773dff12d77fbf1107d2382fb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-IT-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "ad96ba8ffa3cdf2131e92dbd1f468379f94d9df2c558443ddc203656f180d0c8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-LT-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "995ac2925d2461aaa20e2631472874b61f8f99f65c5d898dc636747edda1b986"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-RO-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "1f289af9ab6526ccd6c80e284c8f88093218d2138390f0977832b1785850132e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-REG-US-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "c3834231748d7b27d639be3818a4731b1c0627d8926c8529565a75107b20470a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-RGM-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "137f868659841ee90df1a91b4a1640b4518b8d8427d148d835c0b6b8c8c83f1f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKM-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b8cab3e5e281a8e20c41293c9f8af344a93617eb600db4bc196ed4ff537076c7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKN-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b287318e5d8c89433a3eeec9689fe38f9218dbe806b66f60817803c76617eb02"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "772386cf360018302791a619ce922fd4671c23e72a9457c940f926a801c8deb7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-03",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "dc290785830b9fdb37b5c40ae4d057487850dad111596458e2a5799f75b1a595"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-04",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "41e2fc4713ff676f83c9884bc6d3ed17123ecd4c3b0c442063c24f45fc3be8fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-05",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "d451cacc1ed6cc4284942d782dac3474826167399370e4f942c788d1a0ce1c4a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-06",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b4ccfaf9632179f2cbc016ef60503c2984e081695d25ad72149c199a32c9c2e8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKR-07",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "be1a030b8de9cb2bdd819d5dd889d151183f4df776d6e505fb15760f325b5d90"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "411c6e3ca8d9c4e568bb1f91d4d595f60c9467ee909986ee75b12033c49ddc1a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "9e7895c78978513b8333ac685516057281398b678b106c699db2fffdf2bbada2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-03",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "132ff68b1d5b0b34697a3da64fd7b86c522dbb332c0d19444761bd84a9e76a82"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SKX-04",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "0488a84a42ac90e6982e6307e4db0a4b0b02d0f55d3bcf5cd77e31f4d59c0e86"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SNS-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "a6718568316653dd0d4bf650cb85de18f5f16f021bf58cffe14c38370a76ee66"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SNS-02",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "a07c98bf86b7849afaa75b64375d62e54c8bcf8ca3743cc64c79d8470e2466eb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-STAT-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b36cf4f75f391b1e41a6c1ada9c1fb361b61b8d2ca16f647754754282206a146"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-STR-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "ad913fd118789a94ec1dd47a00662d02cf1daee80db368185b14f28045bb1473"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SVC-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "cc03a78696e0d0937aada649f299dc5ebe100d07b3cd4c474069acf34fa084af"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-VS-04",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "b51f1b8f8f1495b292f76fc16aa24e804722c87da0e27fba56ffa21401eb15a7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-VS-05",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "7e75ca057211ee06ea48afd8e18e3000750a1972698e58a9b20a2de120780f37"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-WA-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "71cb73c01eb67f41cf91bedb98f24e9e3658f65d1694abb789d68f9b76ca081a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-03",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "bd2615bad1c23658fb2b006d6515303f9c613a5c911233bf10697d1b74ab217d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-04",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "85741148a829ca2adf94bb005b6d0fe8268e959ecde5d072e3c90ab0355903f0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-05",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "ce2974a285cda0ae79af78c50a35fbba344c2e4a71124b740ac2540906d83ef0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-AD-07",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "134134509f919b43e1978c789fd0917e401448172254311fcf17619a3b6e4bda"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EMP-03",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "bfd34ec5e307499b6b0a6086ce4a5cb980cea39aa01aac4e83f98e633c50b5c2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "a5219c00d8b231173b7e803653e15c53c93b08243d96d3667ba7f60665a26b5b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-03",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "0c6a147fdfe4c6fd602f415db36115b35d8ccd41f13aacd298ac24ac7e003aa3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-04",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "3817eff30deabdaff5a4fbb6d686d1089900023483c6b92a0112eff94445500f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-06",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "84bbfb36b44130fc9a5394a25a6fdbdbb5a8c42acb47b304cf3049f2ee981193"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-07",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "afb910d18bc191204a1a79a46f4890373db2621014b54c276d0b2a2ba1c127ca"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-09",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "1397a5b717f85ba014b7ffc87dcf240120db08bb6f32a0518dd23e20611e98b6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-EV-10",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "6ce77fe7867781840472ed384e4adb9516558ca01f931dee7d75694cda905819"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-01",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "84258608cc799b979fb1a101af028e5a6925d92075b2a3341a538beceaaffd89"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "T-ID-06",
      "evidence_review": "Geänderter Original-Snapshot nach Refresh im neuen Original gelesen: Belegstellen und alle Zahlen/Daten der Aussage unverändert vorhanden; Änderungen betreffen nur Datumsformat, Seitenrauschen oder Navigation (Abgleich alter/neuer Text pro Beleg, ausgewählte Passagen wörtlich gelesen). Runde-2-Inhaltsbefund trägt unverändert.",
      "fingerprint": "475a52df373c20b7b0329c7ca3206d03c60b237dfbf30b3afea12574b413d448"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-001",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "1e8487c12bc4a509f3841a69e8978f9cd49d36d1fd60677a675cb8bb6b666898"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-002",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "18a6d23bd19eca13027cfd1ea505be4c0ed7a92fc1f8845d65bf5d99ef3df594"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-003",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "3fc0254f214242b3c8bb2dfcd661c44e44218c50384d2fec4953034db8523874"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-004",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "fbf609616f5366c375c7a61b08b463ec9b90350c06e9a4651a3f175f107017fd"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-005",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "b124b80e5a31ebf8a70de7c1d3a9f1439d2264f90ba8e38c7099e166a2a4a256"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-006",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "11806b590b1e6d4048e25fd4fcc78d9bcbc02c369d8cff62bbe35e53a50f5ef2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-008",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "76d46cbf40b0196bc85a5dee8c22327f19489a9d88d32495584b9854bbef5f05"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-010",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "ddcbd55dafe8e54acdc6ac5ad0f06815515d8c3da6e4d167daa3c2153efabb2b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-011",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "d98f5011df71cd2c01b0a60b37a43e7370b47349d21a841a34a3d3dfd59152a6"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-012",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "0ec04e3f7c8a0fd7ddc08f39417d23d95754f9b0282ccb4d4e1ccb0aef968f02"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-013",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "3da76b0b3eceea10934f250f52f272602d24de7c8f50acae3fc092f3929c2448"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-022",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "a957ba33690181c333b8875d92b9e23382aadd74bb21f5f2f748e737689c7139"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-032",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "14474db091afbab99af948fd6d7c333326a069f6725a2a98e305ea4f469eccc2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-037",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "87d29e095cd889e2f8d0ca2a81b28b77d88402929a78aceb5e4f08e7265068cd"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-038",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "6583e6116fb2821bd868f87f96c0e18f8fdef8f6b05f9b18610bdf5acb7c982f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-039",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "942d8894a19dc19a7827eb58f39155c79be6e115a3cc873640a01f692b08579a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-043",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "c39c49caed65a6e2ff73d1c098c6b9a6eb2c35b667adf9b72c5a20d41b9d830c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-044",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "430ae6c74d5b5d3e13085ed6b2f570f5aece84dd28376b606dfd233a7b163660"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-045",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "10fd79d115297e80cbf2d6a03daa343914dd020c4c261fe4a6ae2d5c962472cc"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-046",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "b4a8b0c68c30eebfa1065fb4e65829e5b0e1e52916669affc3ba0cc91fdee2e7"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-047",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "04321b618146c900df8623358b4a09586dd67d0f0651fd933124a4dd1bd3e05e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-048",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "58855f891563274112043968ca6d1274e59e22631651665752c4ce58023e39fe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-049",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "849b4f005369288be43aa3ea19d19844d2076b21595788b87e5c1b22e42f162c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-054",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "65d53cea440129e8cac705e43884c8f774cecd5e8d754792bbbf9348213d72e8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "0dfe33f3afe9be9bc502408ef03a435eac56de47b97e6db2ddb72adbb00e1934"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "566dc0fd8b0ffbc3316b9e2c136ee78b26097d28b1a8f0bc57a889e374808d44"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "68560c7436b02c6e158f44abd40d522f5d248e848022529d745d54a13f6e5070"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "afc0c4f3a2365f9e38be765bf6a188e97d8eb05a28ac4da3a3cff47416856c50"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "14abbb4b216e2f1cf9cc8eb39e2ffe8a3f2ac0318715302367a9c1f2b945d16e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "6dfa9c66164b9540070ff6de09977d0eccc299edf85283e66e881436185915a1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-08",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "fff1562d351a839d31e5b111b641ba5605eff183e5d6db0ae8d40895c39eabac"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-09",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "26be39ff271d2e4c2c7ed7e6316dbc94a6c332378d6be8a40be713a75954463e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DE-ARM-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "77fbf74c16a188b60f5734c24739ff84f5cad2ec811347eb1750935c40b5c3ad"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-EU-EDIP-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "d2ac312fdb21466623ca262cf20f0a67107590fc96e4908016c93fbdb8b671d8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-AT",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "34d66cc747879d5dba01caf99ddaa6d9c36f9de2b2fd280a56e1945f8a2d0676"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-DE",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "20796278a30401d07ec778e9eb91cf6e5c45f81c4cdc32d8974482352b0aa5ca"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-DK",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "964141de9d449cfadab6f2b34e40ea7b1abdbd46f2548b67e4fb3df49c97ff5d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-IT",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "a376851a3a4248e20c2f15578ee4d6c952b2036479af454393236d07f86fe1a3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-NL",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "34c04d837a63163ab3cac1009748c61685655463a69ff2638208c4754e837aea"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-PL",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "ed31338551d3f3d17bdfb187d017e971fded8e677880ab702a9517f6501ba014"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-RO",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "56402cc836ea93a4a0c54e84e913341aba080fa0bb13a382517bdf79d26b48cc"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-SE",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "a1b8d38dc36f03ee5a5a4c92eb2a9c5d074bcb7d76d9e84212d72dab7282a2f3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-UK",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "ed66f1e814433d8c9fa27420e8dd0a4e40c084a49833caff8bbfe4a02ba1268c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "3c4f834253eef4048d9cd7aba8aa214b320ea0d5998025fecff6a715aada7c1e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "ec0a02db36aa0fe4950b47c8e7e10593aa56cc524813a1fb18a48ab44258e380"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "5fea3ac2f9f1ddd3e8c5c64c16ca28b6a34784a3e202b309b083a79b75c98196"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "09c2f3eef07eff56b71306816ccd6abdf579befe48feb5f084e2ebfc990139a9"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "b2eec33f595f04f0fb39a2522a662717e569c5f5549d960994d2e13cdbed73da"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "8fdd9d8cafa1fac21c9a361e332f2593f3e91c090760dbc2713e74c88a0ff1b4"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "1c5d202e5c0e30114ea3c97c547e55a12ee90284758b54f8e626f79dd89e5c53"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-09",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "e13c00c58b19b89a55815c07644883daa478a2df743c5707e153e9ec51b1f32a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "12f8b1f4910b2546545067156e1514e86ba81a85aa0d5b51e315c3b3c649cefe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "e2c99d0a71085bd93210a01bfc1b0438c2e93bb8396530b68dd5e083b9f5519b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "3fa4d22abea5d2143e5e8da18851c8f5908e44f0b813dd34b2bf1d4877632416"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "014ab2c9c6c94b79bf3c5bb629c49c7a0ca21e40ea21f407eaff45d0c25352d9"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "9d4bc81edea898ac503c39b57611767797e704212a591b3a2b94422b5f012609"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-NS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "5bc456aebecec4030472a816fd5239648bba263ffd7fd0559e70d1d0e64e886b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-NS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "e6ac077c7a58558480434af130f3dc778139a6d622664a3b927ecaba6e95d9ac"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-NS-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "0635012dae87fb0afc82e286aedc4c0c6106b372257f7b5eb6a0c721746b4cc7"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-EU-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "a76894cf67a8bcd58af9495aeeebe1c910c13e78254ee1fc7bdc021b23ccc40c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-HR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "f602d151d78faa1ed2c592d5bcc502ac51b0bad8479a35818040f7a602265715"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-HU-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "80b93753b0cb2c985bbf3a5f6cfb90295a4f84ef12b8dcc11bcf59accc5e1f2e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-IN-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "e25cbb4f0a1f8b74df00802b2001e95aa2cba62b4aabbcd4be84b1b97ec54880"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-JV-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "a081ff6a53760a393f599a1bc64f8d32ec00a2766ef2d7d9b67069ab6547b963"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-ME-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "7091713ad0fd062a7ce41251f9c8c97f5513cee7b6ab6455b9bed2d70e1c4596"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-PL-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "e3d1c665174f2d0790f81a4934daf2c7f9dc4ffe903111a901e73ac8224ee873"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-SEE-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "aba4ac85ea50349f172246ce2fe3336a768d056be4f15718d649aafc35281432"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-SG-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "94b3d3e05a6871ed70802610fc0637777d640a0f81bf7aea5a40dcca27a946cd"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-UA-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "5934e4346f9c9fedfd771e2dedde2c2db1107bfbab496ce9871f96e27009f515"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-UK-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "1ba5de8f29368123d99c1fd82bf782c60cf955d34f80325b6a23b08ec56a192c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-ZA-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "b89c4d1d6d245189a4b9fa0c37f71588a68367562736dadb18601125604b92c1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "a4212a20f73506b5955b76abe2ea3241bde5ebf6132eba2594179201c902a3b2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKX-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "69f063777c59f5c71af18ee703a1e549ef32547a8393c53b9231aee8eaf3362b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-STR-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "5d95222b9cc9f2c7c4330a01c7ecba7fee0d3e0afdf4e53211a679798a2fcc94"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-STR-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "2c6c98f8bcde859dfeb0120eeb5a73d689ab13197523b87d413627b58096bab2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "464bbc97bc5dfa75ead183cbe1cc17eb8f35f5a658bdb88c55a3058b144f1c26"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "9f864e5611bfff50507d0b9c801e0078cdd9ac7e7d225e88d5220b8fa403d15e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "4674ef019e738e913a70a88bc2019a0198fb0d860e1d0efde0f7a4752ba79917"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-WA-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "0af97a013db7cf662386673dcf87ded6fa8edfeade4da297c7bb89bc17fd23f5"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-WA-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "60e667105bab0774ab565c72c7e231956970e977f6941f714e31b4d79d41f1ff"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "2f69b45ecb09b62def2526be7dae92ba1d75cd82c39bf524b47524e85d33afa2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "9b08ee326db29507f5ed83afb4cd1cc9188d32ef2497fe1908ca89cfea3bb2ae"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EMP-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "a653c6a0dfdc593044df64ccd490e82b4998c4161fb156932df06fd525fb260d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EMP-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "7efeb58cb1e1f33fda7b16fd1992389b81a0117d7dcce84860b7628c04e31dae"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "fd3bd94303fee711ca976591cdc85a6da199490201883645b9db297844da9db3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "ea61d5a8f7e627c3337b6a5d82cd1b0d40167de732c5084577565b6a0643a913"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-08",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "e1f84d32c6f22c814be9c2770b760c96c3108e3ac0110b5dbd0fbdb1bdc47cab"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-11",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "17e04365265023a19d8651b718ae365bd75279217a183eac931bcd16f6c5539f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "fc5478d380571f7df518c12c77d6726c3681f910d81d2009bad10a2ab8f16a65"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "499190c3680f6c6891c0f18b0403b29186bf5aacdf8ceacf867d8d1a897bc14d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "4609966bf84891dd6038138520548defa654f945e75eec4a9d49703be2f2a71a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "b88321dad0b2deef0496b58e5ac338e5624a0ae4f415be9b33ee0257d391f85d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "f06080d8fa8f2eb06186999711e2b792ca24e60074ccc680acf7c0afe66c4e2a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "387e98337a5e8b4522d8b477f689e0ae34a58de7d1bd32ed78db4ec96a6c277f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "7bb6f7158c10e44bcac97871d55fe1409548f079d37a9b882ff28c4fd4afa4fe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-08",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "ab57a4ecca2ea2fa2cb5e45b54bc7518b618ac6947eb6c210c298f842cd5f2cf"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-09",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "7d90805721c81581ce2c5a605ee93b492abeaf5b3e79894fdd18b20353b2e452"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "d43b44c50eaaf8f8d2c5c291b9650ff9c0b40ed87e3a9d65bc930016817c837d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "64d2ef894b30be1839f5a64f9d0cd7f5d80e160cf7167ad17674b34c34ac2f95"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "1bdd36d5309b47c95d8b3361b967a9cd423445de0e7251de7a83cf51f7173693"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "046ca03ba39a6b4ce2dd609dad9e02b0710ec58cf77c3ff599fca44846614ab8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-SEG-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "fe1f5ab7541968e13d784bcad0ecbe42b789851dc4d070fa8c9f0bd95dc95515"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-SEG-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "62ce8338f027723ed64962f1293587f77a368f66152fd9f628de2e369f43ac0d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-STR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Original-Snapshot und Zuordnung unverändert gegenüber freigegebenem review-basis-r2.md; dortiger A-Befund gilt.",
      "fingerprint": "f6cf3217b9bd8109e2004456f5f29e0419d9bc09d63a79379fedd15dde3672c6"
    }
  ],
  "missing_decisions": [],
  "fact_review": {},
  "input_fingerprint": "dbb747cee1a75b11d29c24d3c6ca54b1c4d3f2cce127bc287c94c396fdf1bbfb"
}
```
