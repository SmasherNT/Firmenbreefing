# Review

```json
{
  "schema_version": 1,
  "run_id": "20261013-rheinmetall-flugabwehr",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-13",
  "phase": "basis",
  "status": "freigegeben",
  "review_work_fingerprint": "a7cb153b1a35f00af1e0a1dc62551f0285690fa216eb973750eda371896c7ad2",
  "material_errors": [],
  "scope_and_mappings_checked": true,
  "review_scope": {
    "summary": "Runde 4 gezielt: nur C-032 und die Kanten e47/e48 sowie die zugehörigen relationships geändert (Paketvergleich mit review-packet-r3.json: keine weiteren Claim-, Quellen-, module_views- oder Netzänderungen). GB-2025-Snapshot unverändert. 223 Übernahmekandidaten ausdrücklich übernommen. Keine Webabrufe."
  },
  "source_checks": [
    {
      "source_id": "S-f4730b21412bb02a",
      "claim_ids": [
        "C-032"
      ],
      "content_sha256": "138727c9936e18cce3a3e85772863f35c22cc8d842ec9baee46b5cbf5035bd6d",
      "capture_kind": "http-original",
      "note": "GB 2025, Strategie S. 39 (PDF-Seite 39) erneut gelesen: Team Lynx mit den Phasen 3/4 des XM30 beauftragt, Mitglieder und rund 650 Mio. EUR bestätigt; im Abschnitt nur „Im Jahr 2025“, kein Vergabemonat.",
      "snapshot": {
        "source_id": "S-f4730b21412bb02a",
        "url": "https://www.rheinmetall.com/Rheinmetall%20Group/Investor%20Relations/Ver%C3%B6ffentlichungen/2026/GB/Rheinmetall-Geschaeftsbericht-2025.pdf",
        "content_sha256": "138727c9936e18cce3a3e85772863f35c22cc8d842ec9baee46b5cbf5035bd6d",
        "text_sha256": "770480588acc0f7d1b5c644315270d9e6425c27c7363c930590e51a72afefe76",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    }
  ],
  "claims": [
    {
      "depth": "A",
      "status": "geprüft",
      "id": "C-032",
      "evidence_review": "Aussage unverändert und belegt. Ein Ereignisdatum fehlt zu Recht; event_status „beauftragt laut GB 2025, Stand 31.12.2025 (Vergabedatum nicht angegeben)“ und die ergänzte Unsicherheit sind korrekt. Kanten e47 (ard→teamlynx) und e48 (anduril→teamlynx): Richtung, Typ Projektteilnahme, Status „beauftragt (Stand GB 2025)“ und as_of/known_as_of 2025-12-31 als Bezugsstand des Berichts (kein Ereignisdatum) semantisch korrekt; keine bilaterale Beziehung unterstellt.",
      "fingerprint": "03554794793f7b2c77c18f230e34eef81b19651f9fda15956f8f2f34985837ca"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-001",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "1e8487c12bc4a509f3841a69e8978f9cd49d36d1fd60677a675cb8bb6b666898"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-002",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "18a6d23bd19eca13027cfd1ea505be4c0ed7a92fc1f8845d65bf5d99ef3df594"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-003",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3fc0254f214242b3c8bb2dfcd661c44e44218c50384d2fec4953034db8523874"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-004",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fbf609616f5366c375c7a61b08b463ec9b90350c06e9a4651a3f175f107017fd"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-005",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b124b80e5a31ebf8a70de7c1d3a9f1439d2264f90ba8e38c7099e166a2a4a256"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-006",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "11806b590b1e6d4048e25fd4fcc78d9bcbc02c369d8cff62bbe35e53a50f5ef2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-007",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3c944a2e91ca19602ad7b564cf1eb1415a8fa4136ec2a15874d7699a2d95c791"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-008",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "76d46cbf40b0196bc85a5dee8c22327f19489a9d88d32495584b9854bbef5f05"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-009",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "d507b169d1af3e607216d515bd3d1683f4f1b13133f78cc2c009a889d5e4db2f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-010",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ddcbd55dafe8e54acdc6ac5ad0f06815515d8c3da6e4d167daa3c2153efabb2b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-011",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "d98f5011df71cd2c01b0a60b37a43e7370b47349d21a841a34a3d3dfd59152a6"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-012",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0ec04e3f7c8a0fd7ddc08f39417d23d95754f9b0282ccb4d4e1ccb0aef968f02"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-013",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3da76b0b3eceea10934f250f52f272602d24de7c8f50acae3fc092f3929c2448"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-014",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "d43f70ddad509e73fdc7317f41aa7872803565eade8455b8fec5e16d43506d96"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-015",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "5fb41a31c24febb2c8184341b0da9cb13265c69b6e9a073ee58bca44f336f29c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-016",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "92485a8471326d9a84e5c5a1df2988b8878a28ba76aca2f9072ea4947068e5a8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-017",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "44ee0d3f68679de4a7867a2e1864dc9a5b2f32a6af3d24a570ea30854fb1cf80"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-018",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3dd818a8efa696e6f00acd5ff4e00e73813bd35e25090d47d337422c9e34c71d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-019",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "277794f5f511651bbf260b75dfc90240a83cfea5716b14cac632040311ccc7fb"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-020",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6b0c75f155c0fa44acaed756a0c4dcd5e90f2170620e28d62a838ced1abc6535"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-021",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6c467fd5a70f110d8d428180c4ce4ce21ee077fd9ca247905d7f5f32ee78db13"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-022",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a957ba33690181c333b8875d92b9e23382aadd74bb21f5f2f748e737689c7139"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-023",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "1235c111204920482d06d582b32133ab830053c214b8df2570b11af6755938fe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-024",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "cfdf11a6f3b933aa69aa56b7afb68f400ebc2db91bf0e58931a590590450491d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-025",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "009394b9fbf93f82b48910e918675967a34fa30446f8b4a5b860544bf7075b02"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-026",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "053e449b74d7923d5d1ae785e514fe87c2f6f9f3d61445bd57660af7f409b0b0"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-027",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6d72426512248dfa12c286f565cd4d0f0532b459df4923f42a33400f2f26f2b1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-028",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "cf2c8feebe57e94b285e280f73086407b8b1a873b1f01508879edeb06c8cc3e6"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-029",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0ce4e19f79c1c474f971022d2a10aaa926fdf74cbc1bd260028da7c053665c09"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-030",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "68dcb878ca401b69f61780bea5583c75b677b61b2860537ddaab265533d23e01"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-031",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "26268ff19bf1814e75affc337a1ee4de13131343561d9d487ec4019672bea9a4"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-033",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0615487d5b266c966f85f6b63361771f8950011c43b746f3901cfa5bd2a72ae9"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-034",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b382081b7dad29b2e2b9ab6c32e54f6f247502cd63e158193424a61f04265e67"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-035",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "9383faf9c9710af7378b0406fb8fd320ad3f42aa01b51f8bb9811d4d6758552c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-036",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "181a77ba439706c4e40f1deaeb4a84b48fe741953258d7234b9d0815070cd123"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-037",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "87d29e095cd889e2f8d0ca2a81b28b77d88402929a78aceb5e4f08e7265068cd"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-038",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6583e6116fb2821bd868f87f96c0e18f8fdef8f6b05f9b18610bdf5acb7c982f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-039",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "942d8894a19dc19a7827eb58f39155c79be6e115a3cc873640a01f692b08579a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-040",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b34df12bc76ed0806855f01f50c3bfae2cb844b67003f69161a8afb400e246d1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-041",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "489079e6185ba11b828826dededafba5a6c41973e91e99da9f501fd6007da148"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-042",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "cc0ae31feb2e76a8ff04736afd830d1ac12ef5ab2baf881f132c51857cf3a415"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-043",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "c39c49caed65a6e2ff73d1c098c6b9a6eb2c35b667adf9b72c5a20d41b9d830c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-044",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "430ae6c74d5b5d3e13085ed6b2f570f5aece84dd28376b606dfd233a7b163660"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-045",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "10fd79d115297e80cbf2d6a03daa343914dd020c4c261fe4a6ae2d5c962472cc"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-046",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b4a8b0c68c30eebfa1065fb4e65829e5b0e1e52916669affc3ba0cc91fdee2e7"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-047",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "04321b618146c900df8623358b4a09586dd67d0f0651fd933124a4dd1bd3e05e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-048",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "58855f891563274112043968ca6d1274e59e22631651665752c4ce58023e39fe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-049",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "849b4f005369288be43aa3ea19d19844d2076b21595788b87e5c1b22e42f162c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-050",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "425d2adf02c0ad2b8d9fb07ab6ce40e4c9ab3f7b5cfd6329d2fe572c52fd0ced"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-051",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "c2c6e8d3a97b125dff73a12387786950d2aad24d8c6082e6e8738ea688a4be39"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-052",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b7a89c2d18bc03d92fcd663b0db7d1ce30959024a686c50bb860eca405e3cbea"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-053",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a4fcdb604c8141bf8bca96044ddd42a7b6b25b2034ba967a09e9925a1d9216c3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "C-054",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "65d53cea440129e8cac705e43884c8f774cecd5e8d754792bbbf9348213d72e8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0dfe33f3afe9be9bc502408ef03a435eac56de47b97e6db2ddb72adbb00e1934"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "566dc0fd8b0ffbc3316b9e2c136ee78b26097d28b1a8f0bc57a889e374808d44"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "68560c7436b02c6e158f44abd40d522f5d248e848022529d745d54a13f6e5070"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "afc0c4f3a2365f9e38be765bf6a188e97d8eb05a28ac4da3a3cff47416856c50"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "14abbb4b216e2f1cf9cc8eb39e2ffe8a3f2ac0318715302367a9c1f2b945d16e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "5e04a9e5e80e7cca02b753d0af45b8e757a293075230104e761d752cfc968792"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6dfa9c66164b9540070ff6de09977d0eccc299edf85283e66e881436185915a1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-08",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fff1562d351a839d31e5b111b641ba5605eff183e5d6db0ae8d40895c39eabac"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "H-PP-09",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "26be39ff271d2e4c2c7ed7e6316dbc94a6c332378d6be8a40be713a75954463e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-AT-ESSI-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "f96ee5c27ee8ed8e78569be546dc35d9b7b3418491dfc1264016a6e4fa548f3b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-AT-SKR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "8dd0444aeed53b191155f4ad14c9f38e5b22da014daa502b77d3d438361ac0a1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-AT-SKR-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "99fa6e35b6545f356ba070cc68a08f4345688fec14a28621490074402d85c0ae"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-CZ-MSH-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "356510e9545151bd9027551757a28d8e90bd66c36df411bc2e8df1a96920068a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DE-ARM-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "77fbf74c16a188b60f5734c24739ff84f5cad2ec811347eb1750935c40b5c3ad"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DE-IRIS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "780c3ac7a7b0fa23b667c9c3288e33cdd33b30b6d1361d6412aa6ee9a4789142"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DE-IRIS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "4e43dba38bd8b59530d474487cc3b0231e28d7633761cdbb785a9b9cbef985d9"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DE-NNBS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6b1c0380dd53633d2f57d5a6014cc0e54f4b92015bf5b76c0c2c1bbd91ddf981"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DE-SKR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "2c80e285582399a55599c2ea7ca7905be31f5684686461aaeb0364723b59d3d6"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DE-SKR-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "76f5e999ff3f8b0aeb2165baef7741f628de2d6da858fd35e039b61253f4cd7c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DIEHL-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "2c048502b17962c7a3a09ed4cfc6f30ad596087bda9e8e2961bc0cf236d2710d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DK-GBAD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0b657e535e24119840a11ad437cc6f88d1a05308ebb635f0539c16d1e70c0bc5"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DK-IRIS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "985b51347132f6cf9a78273c57190f3306bdce973f321d452e334405831b6654"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DK-SAMPT-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "469c82f68be002509d9baecd61c1b63ea40a8db44deb0c80b7d299ded2a66579"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DK-SKR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7811d962e34cf7693eed0a02dcde826d0bf8e220e8fb2ce742de48675d16f37b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-DK-VLM-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "8bf61462d780618aece24688a6d14d36311b18cab095fc455d59ea37b2cd607e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-EU-EDIP-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "d2ac312fdb21466623ca262cf20f0a67107590fc96e4908016c93fbdb8b671d8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-EU-SAFE-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "068d269ece228361992285b8ab0edc0573ed18b5d2f9142ad88256e0d8562eef"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-EU-SAFE-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0b4dee56da302265ffee51536194aac20bc59dc75db30f94aa5da2551dd48104"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-EU-SAFE-UK-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "91281ca1829f3f213b3842a89d17173c030f865f5d0487a3dbac2d9e493f4fd0"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-IT-A2CS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "8bb6a42f1dce39af556f1821191da8cd4175ef3b6f033d44e6712c32a1ff4c3d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-LT-MSH-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "8481c3a02e66d2764bfbd1f78a938084c96116d9944c51e20e9efbb89009719c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-00",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7ad9b826bf23aa31ea7c0692a06158aebcb1c6e4c02284a6bc10cbb21999bb60"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-AT",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "34d66cc747879d5dba01caf99ddaa6d9c36f9de2b2fd280a56e1945f8a2d0676"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-DE",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "20796278a30401d07ec778e9eb91cf6e5c45f81c4cdc32d8974482352b0aa5ca"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-DK",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "964141de9d449cfadab6f2b34e40ea7b1abdbd46f2548b67e4fb3df49c97ff5d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-IT",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a376851a3a4248e20c2f15578ee4d6c952b2036479af454393236d07f86fe1a3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-NL",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "34c04d837a63163ab3cac1009748c61685655463a69ff2638208c4754e837aea"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-PL",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ed31338551d3f3d17bdfb187d017e971fded8e677880ab702a9517f6501ba014"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-RO",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "56402cc836ea93a4a0c54e84e913341aba080fa0bb13a382517bdf79d26b48cc"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-SE",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a1b8d38dc36f03ee5a5a4c92eb2a9c5d074bcb7d76d9e84212d72dab7282a2f3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-MKT-SIPRI-UK",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ed66f1e814433d8c9fa27420e8dd0a4e40c084a49833caff8bbfe4a02ba1268c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-NL-SKR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fde8e052b40a24e71490baa835579529aafdd4928a7f76447224382d87438f42"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-PL-NAREW-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "f30ddad37bbc0480a52341a7b92dee4b4d1c07abe4ce23aa5b675ad8387331fb"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-PL-PIL-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a22e4678ecfe33a603c859508db9aec82cdcbec294b529d027851b50da60cca5"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-PL-PIL-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "f498906f684e2ca883b4269afefda3d1cac4431dc3fd45305090d8c99466b613"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-SAAB-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "e68dc45ccfbcfbf2981a4e02443b3cbb3a6ad9951fd16f1c17d34f516fef0fbf"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-SE-IRIS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "15c1b174f0077d9391629910af8a428205aa0c0ee74427456cdaac603c0551fc"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-SE-RBS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ad1cc94f584d9ab65ec17083e2903dcfd14a657b75757381c4423c8b582e1f26"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-SE-TRI-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "353cc67f8c3b7d87893c4aff1f0047c444007b83ae7dce1bd0b4363f46e12e24"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-SKR30-ARCH-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "f6a736d6fd6ea93a4d703fbf2f772c1b2d69601abf8c3ff9c98f3dbba700e55e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-THA-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "35175efd16ccda666155364433bde58f767946dc0b81fee2050706af3bdf462b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-THA-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b82633af397157721e74a8fbee5c33e44cb6cec4a38fcc6b987d83b1a107d214"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "M-UK-SHORAD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "5cd6f2e747356589d8fdce630313a7663eda589642e309cc0d6b1f3ddcf13aa1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3c4f834253eef4048d9cd7aba8aa214b320ea0d5998025fecff6a715aada7c1e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ec0a02db36aa0fe4950b47c8e7e10593aa56cc524813a1fb18a48ab44258e380"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "5fea3ac2f9f1ddd3e8c5c64c16ca28b6a34784a3e202b309b083a79b75c98196"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "09c2f3eef07eff56b71306816ccd6abdf579befe48feb5f084e2ebfc990139a9"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b2eec33f595f04f0fb39a2522a662717e569c5f5549d960994d2e13cdbed73da"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "8fdd9d8cafa1fac21c9a361e332f2593f3e91c090760dbc2713e74c88a0ff1b4"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "1c5d202e5c0e30114ea3c97c547e55a12ee90284758b54f8e626f79dd89e5c53"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-08",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fe7599ccb8bc8ecfacf9b432dd01540ab6cbbf45b51bcdd09fa09744c80824bd"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AD-09",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "e13c00c58b19b89a55815c07644883daa478a2df743c5707e153e9ec51b1f32a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-AHD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "2e731752af69e11ee87a213bc3867480289747989419210cd91fceeca9c920ae"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-CUAS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "d98c6e7b59e15bb11cf5bf1a15a240ec5576218777fc1480640f7e1ba2265550"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-CUAS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "69f0f3bcd5ea885eb74b1bbbfbc8f1ba70765cc25460275f1b089e0c380a51cb"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-CUAS-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "58f02fb6a1c04aeca7480e81728d3fbb41b87fc636e11624b3d515ea5287222e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "12f8b1f4910b2546545067156e1514e86ba81a85aa0d5b51e315c3b3c649cefe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "e2c99d0a71085bd93210a01bfc1b0438c2e93bb8396530b68dd5e083b9f5519b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3fa4d22abea5d2143e5e8da18851c8f5908e44f0b813dd34b2bf1d4877632416"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "014ab2c9c6c94b79bf3c5bb629c49c7a0ca21e40ea21f407eaff45d0c25352d9"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-DS-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "9d4bc81edea898ac503c39b57611767797e704212a591b3a2b94422b5f012609"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-HEL-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3a970dcc5f699d68f20e68ed06c54783fb236cc6f4e6bfec95cb3af1fedd6d10"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-NAV-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "c579588abd6ce587133eb294277e5f2fbf41430a8f461a31d5285807c126d692"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-NS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "5bc456aebecec4030472a816fd5239648bba263ffd7fd0559e70d1d0e64e886b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-NS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "e6ac077c7a58558480434af130f3dc778139a6d622664a3b927ecaba6e95d9ac"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-NS-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0635012dae87fb0afc82e286aedc4c0c6106b372257f7b5eb6a0c721746b4cc7"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-PS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "cf2966c219dc62bf55e6109d25331f8afea8e760d160c14b5002e20d24bf1a8d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-AU-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "4d2a0747e33b8ca61d434831f2160f3f444aa03328b0ed661c2d03c8b59ca806"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-CA-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fc149584bc1a969451889a5c577ab610df0cc8639256e54469804db134d50c00"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-CH-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "607aa486a103b258828a87aae6a75e2f1cd6c2189488364b611d2b8a18dd9ac8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-DE-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a7cace17f7e3e6694e88e27e8922a37935a19a0020635a534ed2839fc91bab5f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-ES-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6bed1537c6b457baeced10072bae2eb965f0ef1773dff12d77fbf1107d2382fb"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-EU-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a76894cf67a8bcd58af9495aeeebe1c910c13e78254ee1fc7bdc021b23ccc40c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-HR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "f602d151d78faa1ed2c592d5bcc502ac51b0bad8479a35818040f7a602265715"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-HU-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "80b93753b0cb2c985bbf3a5f6cfb90295a4f84ef12b8dcc11bcf59accc5e1f2e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-IN-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "e25cbb4f0a1f8b74df00802b2001e95aa2cba62b4aabbcd4be84b1b97ec54880"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-IT-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ad96ba8ffa3cdf2131e92dbd1f468379f94d9df2c558443ddc203656f180d0c8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-JV-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a081ff6a53760a393f599a1bc64f8d32ec00a2766ef2d7d9b67069ab6547b963"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-LT-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "995ac2925d2461aaa20e2631472874b61f8f99f65c5d898dc636747edda1b986"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-ME-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7091713ad0fd062a7ce41251f9c8c97f5513cee7b6ab6455b9bed2d70e1c4596"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-NO-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7aad3aad6159f033cf6bf244e05cb879f12599f5ca1616c3d9b2420811e981b5"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-NORD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "cf5550faa11277fe2142d111b200706829366b64f2cc0b9d911108d1ab1bdd50"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-OWN-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "33b494039fe48ca3ea7fe95b5c8015ae1b296f21aea05b2a415ad7711471bcb1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-PL-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "e3d1c665174f2d0790f81a4934daf2c7f9dc4ffe903111a901e73ac8224ee873"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-RO-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "1f289af9ab6526ccd6c80e284c8f88093218d2138390f0977832b1785850132e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-SEE-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "aba4ac85ea50349f172246ce2fe3336a768d056be4f15718d649aafc35281432"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-SG-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "94b3d3e05a6871ed70802610fc0637777d640a0f81bf7aea5a40dcca27a946cd"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-UA-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "5934e4346f9c9fedfd771e2dedde2c2db1107bfbab496ce9871f96e27009f515"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-UK-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "1ba5de8f29368123d99c1fd82bf782c60cf955d34f80325b6a23b08ec56a192c"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-US-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "c3834231748d7b27d639be3818a4731b1c0627d8926c8529565a75107b20470a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-REG-ZA-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b89c4d1d6d245189a4b9fa0c37f71588a68367562736dadb18601125604b92c1"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-RGM-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "137f868659841ee90df1a91b4a1640b4518b8d8427d148d835c0b6b8c8c83f1f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKM-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b8cab3e5e281a8e20c41293c9f8af344a93617eb600db4bc196ed4ff537076c7"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKN-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b287318e5d8c89433a3eeec9689fe38f9218dbe806b66f60817803c76617eb02"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a4212a20f73506b5955b76abe2ea3241bde5ebf6132eba2594179201c902a3b2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "772386cf360018302791a619ce922fd4671c23e72a9457c940f926a801c8deb7"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "dc290785830b9fdb37b5c40ae4d057487850dad111596458e2a5799f75b1a595"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "41e2fc4713ff676f83c9884bc6d3ed17123ecd4c3b0c442063c24f45fc3be8fe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "d451cacc1ed6cc4284942d782dac3474826167399370e4f942c788d1a0ce1c4a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b4ccfaf9632179f2cbc016ef60503c2984e081695d25ad72149c199a32c9c2e8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKR-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "be1a030b8de9cb2bdd819d5dd889d151183f4df776d6e505fb15760f325b5d90"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKX-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "411c6e3ca8d9c4e568bb1f91d4d595f60c9467ee909986ee75b12033c49ddc1a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKX-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "9e7895c78978513b8333ac685516057281398b678b106c699db2fffdf2bbada2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKX-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "132ff68b1d5b0b34697a3da64fd7b86c522dbb332c0d19444761bd84a9e76a82"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKX-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0488a84a42ac90e6982e6307e4db0a4b0b02d0f55d3bcf5cd77e31f4d59c0e86"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SKX-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "69f063777c59f5c71af18ee703a1e549ef32547a8393c53b9231aee8eaf3362b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SNS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a6718568316653dd0d4bf650cb85de18f5f16f021bf58cffe14c38370a76ee66"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SNS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a07c98bf86b7849afaa75b64375d62e54c8bcf8ca3743cc64c79d8470e2466eb"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-STAT-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b36cf4f75f391b1e41a6c1ada9c1fb361b61b8d2ca16f647754754282206a146"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-STR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ad913fd118789a94ec1dd47a00662d02cf1daee80db368185b14f28045bb1473"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-STR-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "5d95222b9cc9f2c7c4330a01c7ecba7fee0d3e0afdf4e53211a679798a2fcc94"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-STR-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "2c6c98f8bcde859dfeb0120eeb5a73d689ab13197523b87d413627b58096bab2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-SVC-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "cc03a78696e0d0937aada649f299dc5ebe100d07b3cd4c474069acf34fa084af"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "464bbc97bc5dfa75ead183cbe1cc17eb8f35f5a658bdb88c55a3058b144f1c26"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "9f864e5611bfff50507d0b9c801e0078cdd9ac7e7d225e88d5220b8fa403d15e"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "4674ef019e738e913a70a88bc2019a0198fb0d860e1d0efde0f7a4752ba79917"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b51f1b8f8f1495b292f76fc16aa24e804722c87da0e27fba56ffa21401eb15a7"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-VS-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7e75ca057211ee06ea48afd8e18e3000750a1972698e58a9b20a2de120780f37"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-WA-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "71cb73c01eb67f41cf91bedb98f24e9e3658f65d1694abb789d68f9b76ca081a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-WA-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0af97a013db7cf662386673dcf87ded6fa8edfeade4da297c7bb89bc17fd23f5"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "P-WA-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "60e667105bab0774ab565c72c7e231956970e977f6941f714e31b4d79d41f1ff"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "2f69b45ecb09b62def2526be7dae92ba1d75cd82c39bf524b47524e85d33afa2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "9b08ee326db29507f5ed83afb4cd1cc9188d32ef2497fe1908ca89cfea3bb2ae"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "bd2615bad1c23658fb2b006d6515303f9c613a5c911233bf10697d1b74ab217d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "85741148a829ca2adf94bb005b6d0fe8268e959ecde5d072e3c90ab0355903f0"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ce2974a285cda0ae79af78c50a35fbba344c2e4a71124b740ac2540906d83ef0"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0ec35e3a5ba38fe46698e3f5726a6809b3faf580960e6996f126fee02e71d14d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-AD-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "134134509f919b43e1978c789fd0917e401448172254311fcf17619a3b6e4bda"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EMP-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a653c6a0dfdc593044df64ccd490e82b4998c4161fb156932df06fd525fb260d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EMP-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7efeb58cb1e1f33fda7b16fd1992389b81a0117d7dcce84860b7628c04e31dae"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EMP-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "bfd34ec5e307499b6b0a6086ce4a5cb980cea39aa01aac4e83f98e633c50b5c2"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "a5219c00d8b231173b7e803653e15c53c93b08243d96d3667ba7f60665a26b5b"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fd3bd94303fee711ca976591cdc85a6da199490201883645b9db297844da9db3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "0c6a147fdfe4c6fd602f415db36115b35d8ccd41f13aacd298ac24ac7e003aa3"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "3817eff30deabdaff5a4fbb6d686d1089900023483c6b92a0112eff94445500f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ea61d5a8f7e627c3337b6a5d82cd1b0d40167de732c5084577565b6a0643a913"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "84bbfb36b44130fc9a5394a25a6fdbdbb5a8c42acb47b304cf3049f2ee981193"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "afb910d18bc191204a1a79a46f4890373db2621014b54c276d0b2a2ba1c127ca"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-08",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "e1f84d32c6f22c814be9c2770b760c96c3108e3ac0110b5dbd0fbdb1bdc47cab"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-09",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "1397a5b717f85ba014b7ffc87dcf240120db08bb6f32a0518dd23e20611e98b6"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-10",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "6ce77fe7867781840472ed384e4adb9516558ca01f931dee7d75694cda905819"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-EV-11",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "17e04365265023a19d8651b718ae365bd75279217a183eac931bcd16f6c5539f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fc5478d380571f7df518c12c77d6726c3681f910d81d2009bad10a2ab8f16a65"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "499190c3680f6c6891c0f18b0403b29186bf5aacdf8ceacf867d8d1a897bc14d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "4609966bf84891dd6038138520548defa654f945e75eec4a9d49703be2f2a71a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "b88321dad0b2deef0496b58e5ac338e5624a0ae4f415be9b33ee0257d391f85d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "f06080d8fa8f2eb06186999711e2b792ca24e60074ccc680acf7c0afe66c4e2a"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "387e98337a5e8b4522d8b477f689e0ae34a58de7d1bd32ed78db4ec96a6c277f"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-07",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7bb6f7158c10e44bcac97871d55fe1409548f079d37a9b882ff28c4fd4afa4fe"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-08",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "ab57a4ecca2ea2fa2cb5e45b54bc7518b618ac6947eb6c210c298f842cd5f2cf"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-FIN-09",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "7d90805721c81581ce2c5a605ee93b492abeaf5b3e79894fdd18b20353b2e452"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "84258608cc799b979fb1a101af028e5a6925d92075b2a3341a538beceaaffd89"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "d43b44c50eaaf8f8d2c5c291b9650ff9c0b40ed87e3a9d65bc930016817c837d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-03",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "64d2ef894b30be1839f5a64f9d0cd7f5d80e160cf7167ad17674b34c34ac2f95"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-04",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "1bdd36d5309b47c95d8b3361b967a9cd423445de0e7251de7a83cf51f7173693"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-05",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "046ca03ba39a6b4ce2dd609dad9e02b0710ec58cf77c3ff599fca44846614ab8"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-ID-06",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "475a52df373c20b7b0329c7ca3206d03c60b237dfbf30b3afea12574b413d448"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-SEG-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "fe1f5ab7541968e13d784bcad0ecbe42b789851dc4d070fa8c9f0bd95dc95515"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-SEG-02",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "62ce8338f027723ed64962f1293587f77a368f66152fd9f628de2e369f43ac0d"
    },
    {
      "depth": "A",
      "status": "übernommen",
      "id": "T-STR-01",
      "evidence_review": "Ausdrücklich übernommen: Aussage, Quellenmetadaten, Snapshot und Zuordnung unverändert gegenüber dem freigegebenen Basis-Review r3; dortiger A-Befund gilt.",
      "fingerprint": "f6cf3217b9bd8109e2004456f5f29e0419d9bc09d63a79379fedd15dde3672c6"
    }
  ],
  "missing_decisions": [],
  "fact_review": {},
  "input_fingerprint": "44c1c4993eb57f110a4ac0b8abb65d7a4e07bb175b61db3c322ad0fd22e93233"
}
```
