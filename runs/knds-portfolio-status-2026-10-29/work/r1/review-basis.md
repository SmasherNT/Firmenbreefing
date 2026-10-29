# Review

```json
{
  "schema_version": 1,
  "run_id": "knds-portfolio-status-2026-10-29",
  "company": "KNDS N.V.",
  "as_of": "2026-10-29",
  "phase": "basis",
  "status": "teilweise",
  "material_errors": [
    "Open claim corrections (26): P-02, P-03, P-05, P-SA-021, P-SA-025, P-SA-043, P-SA-050, P-SA-055, P-SB-003, P-SB-013, P-SB-024, P-SB-027, P-SB-029, P-SB-045, P-SC-003, P-SC-008, P-SC-016, P-SC-020, P-SC-022, P-SC-024, P-SC-029, P-SC-036, P-SD-012, P-SD-013, P-SD-021, P-SD-052 - see review_groups.",
    "Open cache items: P-02, P-03, P-05 have no cache snapshot for S-f78bf9f5633dc0c2, S-2190194daccd00d4, S-3e48809a6efb1a20 (owner main).",
    "Product mapping defects M1-M16 (mapping_findings) must be corrected by portfolio before release.",
    "Unresolved source conflicts (documented, not resolvable from public sources): Leopard 2 A8 handover (KNDS April 2026 vs BAAINBw 2027), RCH 155 Ukraine delivery/use, RapidFire 48 units (naval vs land), KATANA specification; SERVAL contract date resolved as outlier; SHARD date corrected to 17 Feb 2026."
  ],
  "review_scope": "Lead review (source-reviewer, claude-sonnet-5-5 medium configured; actual executed model not verifiable from the run) after 3 document jobs (sources-1..3, 218 sources, 232 claims, 278 claim/source findings). Read: all 232 findings with notes; full portfolio-facts products/module_views (52 products, 9 groups) against claims and existing-portfolio split; product identity, group, status date, event_status vs sources, Aussageursprung, order/delivery/use, variants. Targeted lead checks: EDR page for SHARD date (17 Feb 2026); web checks for Leopard 2 A8 Bundeswehr handover (none found) and RCH 155 Ukraine (no official delivery confirmation). Originals not re-read in full; document-job reading relied upon for geprüft claims. Corrections go back to portfolio/main; no analyst file changed. scope_and_mappings_checked = semantic check performed, not an acceptance of the mapping (defects listed).",
  "review_work_fingerprint": "fddc81e0a025d338d2d8d8154afeafeb092c8c4d0c71298e4a46ec9a41c39584",
  "plan_fingerprint": "125875bd1971b5fca7ca6afdf84be8b5c58fbb6c8d0d793cefac768745e4fc18",
  "source_collection_fingerprint": "105cd826f889fd21477098f35b115cd56e3679ef42be431428cf268f5689c4ba",
  "scope_and_mappings_checked": true,
  "mapping_findings": [
    {
      "id": "M1",
      "products": [
        "agm"
      ],
      "claims": [
        "P-SB-013"
      ],
      "issue": "AGM row (claim_ids and section) contains P-SB-013, the RCH 155 Ukraine delivery claim, which is also overstated; it is no AGM status evidence.",
      "action": "Remove P-SB-013 from agm; derive AGM status only from AGM-specific claims or state it via rch155 without transferring Ukraine delivery.",
      "owner": "portfolio"
    },
    {
      "id": "M2",
      "products": [
        "centurio"
      ],
      "claims": [
        "P-SC-049"
      ],
      "issue": "DROIDE framework agreement does not name CENTURIO; mapped as CENTURIO status claim.",
      "action": "Remove from centurio claim_ids (or move to a context section clearly labelled not CENTURIO-specific).",
      "owner": "portfolio"
    },
    {
      "id": "M3",
      "products": [
        "mataris-mv-100",
        "mataris-mv-25",
        "mataris-mt-10"
      ],
      "claims": [
        "P-SC-018"
      ],
      "issue": "P-SC-018 states operational service for the MX-10 only but is mapped to all four MATARIS rows.",
      "action": "Keep P-SC-018 only in mataris-mx-10 (family identity via P-14/P-SC-019).",
      "owner": "portfolio"
    },
    {
      "id": "M4",
      "products": [
        "dlbo"
      ],
      "claims": [
        "P-SD-041",
        "P-SD-042"
      ],
      "issue": "Programme-level Bundeswehr/BMVg facts without KNDS/ArGe naming and without KNDS share.",
      "action": "Keep as programme-level evidence with explicit limitation; do not use alone for a KNDS-specific series/operation stage.",
      "owner": "portfolio"
    },
    {
      "id": "M5",
      "products": [
        "rapidfire"
      ],
      "claims": [
        "P-SB-043",
        "P-SB-047",
        "P-SB-048",
        "P-SB-045"
      ],
      "issue": "Naval RAPIDFire service, ammunition order, component status and the conflicting 48-unit report are mapped to RapidFire Land.",
      "action": "Mark naval/ammunition/component claims as context sections; land status only from P-SB-044/P-SB-046; fix P-SB-045.",
      "owner": "portfolio"
    },
    {
      "id": "M6",
      "products": [
        "gepard"
      ],
      "claims": [
        "P-SB-050",
        "P-SB-051",
        "P-SB-052"
      ],
      "issue": "Transferred Bundeswehr Gepard and Rheinmetall ammunition are mapped as status claims although KNDS manufacturer/production role is undocumented.",
      "action": "Label as context; state in uncertainty that KNDS role is maintenance/repair; P-SB-051 into the existing context section only.",
      "owner": "portfolio"
    },
    {
      "id": "M7",
      "products": [
        "cbrn-mask",
        "cbrn-decon"
      ],
      "claims": [
        "P-SD-050"
      ],
      "issue": "Company-level CBRN statement mapped as identity/status for individual products.",
      "action": "Use only as context; product identity from P-SD-051/-053.",
      "owner": "portfolio"
    },
    {
      "id": "M8",
      "products": [
        "training-puma-agsp"
      ],
      "claims": [
        "P-SD-062",
        "P-SD-063"
      ],
      "issue": "AGSP developed by Rheinmetall; KNDS involvement only via PSM JV; row sits in KNDS portfolio without this being visible.",
      "action": "State PSM/Rheinmetall role in label or uncertainty, or confirm with main agent that the row is within the delegated scope.",
      "owner": "portfolio / main"
    },
    {
      "id": "M9",
      "products": [
        "flw"
      ],
      "claims": [
        "P-SB-055"
      ],
      "issue": "BMVg source does not name FLW manufacturer; FLW 200 Plus has no status evidence; row covers three variants.",
      "action": "Document KNDS attribution via P-12/P-SB-056; limit status to FLW 100/200; variant limits in uncertainty.",
      "owner": "portfolio"
    },
    {
      "id": "M10",
      "products": [
        "nerva-xx",
        "nerva-lg"
      ],
      "claims": [
        "P-SC-040"
      ],
      "issue": "Type split of \"56 NERVA robots / several hundred for foreign armies\" not stated.",
      "action": "No NERVA-XX status from P-SC-040; keep as family context.",
      "owner": "portfolio"
    },
    {
      "id": "M11",
      "products": [
        "ultro"
      ],
      "claims": [
        "P-SC-035"
      ],
      "issue": "MT-10 integration video is mapped to ULTRO as if ULTRO status evidence.",
      "action": "Context only; ULTRO status from P-SC-050/-051.",
      "owner": "portfolio"
    },
    {
      "id": "M12",
      "products": [
        "dsb",
        "mgb"
      ],
      "claims": [
        "P-SD-010",
        "P-SD-012",
        "P-SD-013",
        "P-SD-021"
      ],
      "issue": "Family-level or WFEL-named claims mapped to single-product rows without KNDS UK identity link.",
      "action": "See claim corrections P-SD-012/-013/-021; P-SD-010 jointly DSB+MGB must be labelled as such.",
      "owner": "portfolio"
    },
    {
      "id": "M13",
      "products": [
        "donar",
        "agm"
      ],
      "claims": [
        "P-SB-038",
        "P-SB-039",
        "P-SB-041",
        "P-SB-042"
      ],
      "issue": "Row donar mixes tracked ASCOD DONAR (2009 prototype) and Swiss DONAR 10x10 on Piranha IV (2026 order); agm row also receives P-SB-038/-039. Variants with different status are not split.",
      "action": "Split into variant rows or state the represented variant; one status per row.",
      "owner": "portfolio"
    },
    {
      "id": "M14",
      "products": [
        "dingo",
        "caesar",
        "leopard-2a7v"
      ],
      "claims": [
        "P-SA-056",
        "P-SA-058",
        "P-SB-003",
        "P-SB-006",
        "P-SA-009"
      ],
      "issue": "Variant mixing within rows: Dingo 2 A4.1 vs Dingo 3 (naming unresolved), CAESAR 6x6 vs Mk II/8x8 (rates not variant-specific), A7V vs A7A1.",
      "action": "Name variants in uncertainty; final reviewer must not carry variant evidence into the row stage.",
      "owner": "portfolio"
    },
    {
      "id": "M15",
      "products": [
        "all"
      ],
      "claims": [],
      "issue": "Domain \"Services and training\" differs from the delivered HTML/existing-portfolio group name \"Service and training\" (delegation: keep existing group names).",
      "action": "Use \"Service and training\" (check the HTML) for training, training-leo2-sweden, training-puma-agsp, service, service-canada, service-ukraine.",
      "owner": "portfolio"
    },
    {
      "id": "M16",
      "products": [
        "thl",
        "gepard"
      ],
      "claims": [],
      "issue": "Old bundled row \"FLW · ARX · THL / Medium calibre\" lost its Medium calibre part (cannons 20M621, 25M811, 30M781 etc. not assessed; gap recorded). Rows added beyond the old labels (leopard-2a8, dlbo, cbrn-mask, cbrn-decon, training-leo2-sweden, training-puma-agsp, service-canada, service-ukraine) should be checked against the Teilaufträge A-D scope.",
      "action": "Portfolio/main: add medium-calibre row or state exclusion in the matrix methodology; confirm the extra rows are in scope.",
      "owner": "portfolio / main"
    }
  ],
  "source_checks": [
    {
      "source_id": "S-00d6ee6495184271",
      "claim_ids": [
        "P-SA-006"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-00d6ee6495184271",
        "url": "https://defence-industry.eu/kmw-delivers-final-leopard-2a7v-tank-to-bundeswehr/",
        "content_sha256": "f5592e798c2e10b1f1e52ac2869c37c9d8392f61c6d95d89ad75741c69683ece",
        "text_sha256": "ec84d3b9c2f17ddfe24f931c9055ac816ef946e76c9f6fafd03d2a7d73710694",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-04a9c382f0bc91bf",
      "claim_ids": [
        "P-SA-018",
        "P-SA-019"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-04a9c382f0bc91bf",
        "url": "https://defence-industry.eu/dga-signs-contract-with-knds-france-to-upgrade-100-additional-leclerc-tanks/",
        "content_sha256": "c91ba9d175b52016b97bee2107288dfe58216002bc9bd5720daddbf3fd4c79d9",
        "text_sha256": "9cdc6ad5935814f674e760c7c84ba47dd44fe8d15323ef17730106f1f251017b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-06421b50be671aa0",
      "claim_ids": [
        "P-SB-003"
      ],
      "note": "Lyon Capitale-Artikel (13.07.2026) über Quellencache gelesen (Volltext, Absätze zu Nextfab/Raten und SCORPION/Caesar).",
      "snapshot": {
        "source_id": "S-06421b50be671aa0",
        "url": "https://www.lyoncapitale.fr/?p=510269",
        "content_sha256": "85d833a6b68c1d27f01615227b724f2662f449a50d766e3741651566a3fcb27f",
        "text_sha256": "8c4e6b383f45101d03e01af71849f3fe298510fa0fcd28172978845d0c7a26d1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-081455a6101c816e",
      "claim_ids": [
        "P-SB-050",
        "P-SB-051"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-081455a6101c816e",
        "url": "https://www.rheinmetall.com/en/media/news-watch/news/2025/01/2025-01-06-35mm-gepardmunition-fuer-ukr",
        "content_sha256": "5298dbaa03a66499fcb91b0402158fa0425eb37a670bb098d0909f24796cf378",
        "text_sha256": "7b72381e8ec23fd4135acb3431b97c491157236423a81301040272dd3498c188",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-08414f6312d07936",
      "claim_ids": [
        "P-SC-042"
      ],
      "note": "Defense Mirror 16.10.2024 gelesen (Absätze 1-2 und Datumszeile).",
      "snapshot": {
        "source_id": "S-08414f6312d07936",
        "url": "https://defensemirror.com/news/37931/KNDS_Exports_Multi_Mission_Robots_to_Italy",
        "content_sha256": "8e076187e8f3d5e36bab7824b349eb7a543de8d6799c5b8e3c003ffce401387e",
        "text_sha256": "cc05db5dc48e7d191fc21784c566cf5c41a1ead284a788741dcf12bd4289cdfd",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-086937648044a782",
      "claim_ids": [
        "P-11",
        "P-21"
      ],
      "note": "Gelesen: cache read (HTML-Text, http-original), Seite KNDS Deutschland Zeilen 10-60 (Portfolio-/Leistungsspektrum, Kundendienst, Wartung/Ausbildung).",
      "snapshot": {
        "source_id": "S-086937648044a782",
        "url": "https://knds.com/de/standorte/knds-deutschland",
        "content_sha256": "dcbce86b81a63df82e401e8fbd10ef528d47c8dcd452b85975a63f3df1bd1942",
        "text_sha256": "c00e50f13a141cd236658f9791e55941933912391fe9757fc1c316391659ef6a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0d0668145edf4607",
      "claim_ids": [
        "P-SB-047"
      ],
      "note": "Naval News 20.06.2025 gelesen (Absätze 1-7, Aufzählung der Einsatzsysteme).",
      "snapshot": {
        "source_id": "S-0d0668145edf4607",
        "url": "https://www.navalnews.com/naval-news/2025/06/france-orders-40mm-ammunition-rounds-for-navy-and-army/",
        "content_sha256": "6387e2e1b2eb8dad4bd99d0422b37cf1ccbdb3df678ae56ec26ad05cc0dceacb",
        "text_sha256": "0f3ffd9306e06d723cfee20b5d38e8a472689efcfad19ddf0ce85a95bced6729",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0dd13a3430574f68",
      "claim_ids": [
        "P-17",
        "P-SD-007"
      ],
      "note": "Gelesen: cache read, komplette LEGUAN-Produktseite (Zeilen 17-80: Features, 'International teaming', 'Facts about the LEGUAN LEOPARD 2').",
      "snapshot": {
        "source_id": "S-0dd13a3430574f68",
        "url": "https://knds.com/en/products/systems/bridges/leguan",
        "content_sha256": "3e05b7a2dbf0a5f318ff9b7783c59a11e6ac3d8a4decfa37ac775f13a0e1c960",
        "text_sha256": "015966a59159c750cc5d75ffd25ea344ffd2e3e0c6c619a2ebe3ad07e0151383",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0df7d1e4993cf9cd",
      "claim_ids": [
        "P-SB-018",
        "P-SB-029"
      ],
      "note": "Gelesen: cache read; Abschnitte PzH 2000 A4 (Z. 429-449), RCH 155 (Z. 450-466) sowie Dingo (Z. 304-320) im Original-Text; Metadaten dateModified 2026-10-22 im gespeicherten Original-HTML (source.bin) bestätigt.",
      "snapshot": {
        "source_id": "S-0df7d1e4993cf9cd",
        "url": "https://suv.report/beschaffungsvorhaben-des-heeres/",
        "content_sha256": "3ce2a806fdd8756308ac4a7bf62efe29bde5e74c878558d96d4a215ec5551226",
        "text_sha256": "f4bf552e1715111244547301e440744fda90fc66b1aed4d7c7b759265a4a71f6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-0ed42f15608cd2cd",
      "claim_ids": [
        "P-SB-031"
      ],
      "note": "Augen geradeaus 15.06.2022 gelesen (Absätze 1-4, Statement-Nachtrag).",
      "snapshot": {
        "source_id": "S-0ed42f15608cd2cd",
        "url": "https://augengeradeaus.net/2022/06/lambrecht-bestaetigt-bundeswehr-raketenartillerie-fuer-die-ukraine/",
        "content_sha256": "a11fce6906dfe0969202580a5603fa1d64b6432247ef3fcafac7127a242738fc",
        "text_sha256": "2c264a5fab8f7a0ced8fd1140c1cbe599fc07b93ae8d5f9ab0bd4c53b299fa8b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1076e757bfbb6481",
      "claim_ids": [
        "P-SA-033"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-1076e757bfbb6481",
        "url": "https://militaeraktuell.at/deutschland-niederlande-69-schakal/",
        "content_sha256": "5069808060cd4bd7f9de0b4aeaac378f93164e791a422b796df41ebfecec9ca4",
        "text_sha256": "d54795cfee47b9be077608dfb6946f9265112ea7ad17adf020577233825e34b1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-108999689b0d838d",
      "claim_ids": [
        "P-SD-003",
        "P-SD-065"
      ],
      "note": "KNDS-Pressemitteilung 23.07.2020 gelesen (Absätze 1-3). Seitenfuß enthält spätere Kennzahlen (2023); nicht verwendet.",
      "snapshot": {
        "source_id": "S-108999689b0d838d",
        "url": "https://knds.com/press-releases/german-army-receives-further-leguan-bridge-layer",
        "content_sha256": "eb366ca080c28e70b0231b073745cecf5dfd901a02353d0fe9e010d326537d7a",
        "text_sha256": "8df9d000ba47cb19fa12d42e1b9667c3a8078821588b82209687301b57a1945a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-10bb2db9567e98a1",
      "claim_ids": [
        "P-SB-008"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-10bb2db9567e98a1",
        "url": "https://eurointegration.com.ua/eng/news/2023/02/7/7155678",
        "content_sha256": "c6d801b6b70e01eb4aee22a09cbdf146286dc93b31ce6e64bbbcfeb796dbddfb",
        "text_sha256": "ec777a5b11e0fa2d2b927410c86ad6eee6fe4645774861d5e6a3fe155e5e4f2b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-15fc00956abaf7b7",
      "claim_ids": [
        "P-SC-037"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-15fc00956abaf7b7",
        "url": "https://www.joint-forces.com/?p=23749",
        "content_sha256": "d023e28821060b94b61062b2cd5a06c98a8d9e093fad0e6e449691c9878be786",
        "text_sha256": "93cf396b8917bbbe9c3128a1c717841c22600cfed41ffd295edc9b173c3ffa3b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1a4e06392b187ffb",
      "claim_ids": [
        "P-SA-056"
      ],
      "note": "Gelesen: cache read, Janes-Artikel vom 01.12.2023 vollständig (Zeilen 11-22 Inhalt; Rest Navigation).",
      "snapshot": {
        "source_id": "S-1a4e06392b187ffb",
        "url": "https://www.janes.com/defence-intelligence-insights/defence-news/land/bundeswehr-orders-dingo-2s-to-replace-vehicles-donated-to-ukraine",
        "content_sha256": "7a53f03863d5e8c1a49bfdb84fa5e6584614aae3d0f81aca7dfefc8a91aae52a",
        "text_sha256": "4bd4ea7a04b371757cccde57623412c3e3633226949e0fa21461db5502d46dde",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1b6c2f2ee1b05d06",
      "claim_ids": [
        "P-SA-044"
      ],
      "note": "Gelesen: cache read, SERVAL-Produktseite Zeilen 15-60 (Intro, Facts, Specifications).",
      "snapshot": {
        "source_id": "S-1b6c2f2ee1b05d06",
        "url": "https://knds.com/en/products/systems/serval",
        "content_sha256": "caf35f12cfe0fe3c775afa8c711c938f99c5890065731f0ca1bfdf5209285bce",
        "text_sha256": "de8a4281bef67a120794ac1bd81c28a4e7ef3e1b9a1e468aae69c992474131b3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1c5dd1f131f057a4",
      "claim_ids": [
        "P-SB-007"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung vom 24.01.2024 vollständig (Zeilen 11-24).",
      "snapshot": {
        "source_id": "S-1c5dd1f131f057a4",
        "url": "https://knds.com/en/press-releases/the-french-mod-orders-109-caesar-mk-ii-from-nexter-a-company-of-knds",
        "content_sha256": "727d38baf3ffcdc6623da596211e9cfad162492e0a10361a4c3f7375d308d258",
        "text_sha256": "aa139bbf4c24beed8be11d0471bb82851e832cf7697cfe3aad0336a0e32e9ad1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1d6c74253ee37970",
      "claim_ids": [
        "P-SC-041"
      ],
      "note": "Gelesen: cache read, Defense-Mirror-Artikel vom 29.11.2024 vollständig (Zeilen 73-83; Rest Navigation).",
      "snapshot": {
        "source_id": "S-1d6c74253ee37970",
        "url": "https://defensemirror.com/news/38276/U_S__Special_Forces_Order_French_NERVA_LG_Robots",
        "content_sha256": "896954fe31a3e27e6c61a4bda9a64f4188360dcb2539da4b732a6b9237fffc72",
        "text_sha256": "ebbc88d1e821d4de648dbda88efb21e21b39ebede9050f2b89faec4ea0b0efff",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1e36d6e4ba085ffa",
      "claim_ids": [
        "P-SC-036",
        "P-SC-041"
      ],
      "note": "Gelesen: cache read, Defence-Industry-Europe-Artikel vom 30.11.2024 vollständig (Zeilen 11-26).",
      "snapshot": {
        "source_id": "S-1e36d6e4ba085ffa",
        "url": "https://defence-industry.eu/u-s-special-operations-forces-purchase-nerva-lg-robots-from-french-manufacturer/",
        "content_sha256": "f54ef17c4a09a9b371378f715fcae02ba557e78c79be343b19568a218e74bbdd",
        "text_sha256": "6aaafa07254d7c66135630370a7747656091970f71656880d26b4a5d9319e80f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1fb6bc3d36a3ffa1",
      "claim_ids": [
        "P-SB-063"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-1fb6bc3d36a3ffa1",
        "url": "https://knds.com/en/products/systems/thl-30",
        "content_sha256": "c9e0eba93009859f6a461660ab63f6b0a3e9b8418ced5764d29b86aa4cf613ad",
        "text_sha256": "91feb0bd672c71c65f9effebef85fd587b2c18b9848dfd5101faeeb53ea4000b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-1fbf7e7a634158bc",
      "claim_ids": [
        "P-SB-059"
      ],
      "note": "Gelesen: cache read, ARX20-Produktseite Zeilen 14-75 (Intro, Facts, Specs, Related).",
      "snapshot": {
        "source_id": "S-1fbf7e7a634158bc",
        "url": "https://knds.com/en/products/systems/arx-20",
        "content_sha256": "82f988cf6ec7094adaa6eace9894aefd05fadde65d38ca7b1595f174a9064418",
        "text_sha256": "ab437212ce84af6f72009d0f502b9cf2633885733de4d791ffdca6cf0eba121d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-219f5e5f415564c3",
      "claim_ids": [
        "P-SA-017"
      ],
      "note": "Defence Redefined 01.12.2023 gelesen (Absätze 1-5).",
      "snapshot": {
        "source_id": "S-219f5e5f415564c3",
        "url": "https://defenceredefined.com.cy/france-first-upgraded-leclerc-xlr-delivered-to-the-army",
        "content_sha256": "c1cb32d17f3c9b5c08cd1856cef7029879321c10380189199b09fcbd67683419",
        "text_sha256": "1e7afa1278b174f92116907b652fed03c3073496d574fa25843fbdf4569e2c78",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-236a4e15250320c1",
      "claim_ids": [
        "P-SC-015"
      ],
      "note": "European Security & Defence (Artikel 29.02.2024, Seite ohne Metadatum, Datum im Text) gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-236a4e15250320c1",
        "url": "https://euro-sd.com/2024/02/major-news/36812/nexter-qualifies-shard-ammo",
        "content_sha256": "a99b3085e4c909eb56b10b1bae8e24b141c4c8fd458989bbfbc1afcb01c568c0",
        "text_sha256": "1d5e86c9c3077025bab50ce0176b407e1d58eb1e1e95a091955a45c6dd0795e7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2570c8a1f788d668",
      "claim_ids": [
        "P-SB-017"
      ],
      "note": "Gelesen: cache read, Rheinmetall-Pressemitteilung 19.12.2025 vollständig (Zeilen 9-22).",
      "snapshot": {
        "source_id": "S-2570c8a1f788d668",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/12/2025-12-19-grossauftrag-radhaubitze-rch155",
        "content_sha256": "878e64799bf1c897e1973b53ce325999370d5cb162541f1cb6e3bae16887932c",
        "text_sha256": "afbdb86f992a36e0e242e577176fd3017af4045969c4797e0ba07f67a18837a1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-26ccacf7b7f08845",
      "claim_ids": [
        "P-SA-035"
      ],
      "note": "Gelesen: cache read, DGA-Meldung vom 14.10.2024 (Zeilen 41-55) sowie Teaser-Block 'Dossier' (Z. 65-73).",
      "snapshot": {
        "source_id": "S-26ccacf7b7f08845",
        "url": "https://www.defense.gouv.fr/dga/actualites/dga-livre-100e-vehicule-griffon-larmee-terre-debut-lannee-2024",
        "content_sha256": "ea146b57c9929bb5b8dc5855063d185cb90be55b76b2412bdda7f779fa35e9a1",
        "text_sha256": "b11bcce895722e809a70dd3208ba6603fd228d26c03bd5dc971906b9a80d9bff",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2947965d6409d2ab",
      "claim_ids": [
        "P-SC-021"
      ],
      "note": "Army Recognition (2026, ohne Metadatum) gelesen (Absätze 1-3 und Planung).",
      "snapshot": {
        "source_id": "S-2947965d6409d2ab",
        "url": "https://armyrecognition.com/news/army-news/2026/french-armed-forces-receive-first-damocles-short-range-loitering-munition",
        "content_sha256": "409204f34743548cd496b2f92b4c0378c976705406d201be08d1ce3aa7405dcf",
        "text_sha256": "6c4ee8173e19dc65fd23f0c8418a6cc8fbeb5d4bbfbd49a62aa929a217def96e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2a19a44bae9c9218",
      "claim_ids": [
        "P-SC-002",
        "P-SC-003",
        "P-SC-007",
        "P-SC-009",
        "P-SC-014"
      ],
      "note": "KNDS Ammunition Catalogue 2026-2027 über Cache (pdftotext, PDF-Seiten 9, 10, 12, 17, 43, 44, 80) gelesen; Herstellerkatalog.",
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
      "source_id": "S-2b10b29533252970",
      "claim_ids": [
        "P-SA-022"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-2b10b29533252970",
        "url": "https://www.defense.gouv.fr/terre/nos-materiels/nos-equipements-terre/vehicules-larmee-terre/vehicules-chars-bataille/char-leclerc-xlr-renove",
        "content_sha256": "1a42b919046325ae3c7736d2aad01e1299609dd225165bfe87411fbfd42bf7b7",
        "text_sha256": "6878b087e0859dd108fc41ecb2adbe2af357a693a4a341b1d68647b22f71771e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2c2ab405ba99057a",
      "claim_ids": [
        "P-SD-051",
        "P-SD-053"
      ],
      "note": "Gelesen: cache read, Al-Defaiya-Wiederveröffentlichung vom 16.03.2026 vollständig (Zeilen 21-40).",
      "snapshot": {
        "source_id": "S-2c2ab405ba99057a",
        "url": "https://www.defaiya.com/news/Security/Security/2026/03/16/knds-cbrn-to-supply-new-gas-mask-decontamination-systems-to-french-dga",
        "content_sha256": "853c225166bba59193899fab8659f876fbb18dae304d28116734659f2916364b",
        "text_sha256": "09511bfb041223b274e28562956a3f310c847c061250ec6f2c406e0dfbc83281",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2cd221b99b7d9180",
      "claim_ids": [
        "P-SA-028"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung 07.08.2026 (Zeilen 11-25).",
      "snapshot": {
        "source_id": "S-2cd221b99b7d9180",
        "url": "https://knds.com/en/press-releases/additional-69-boxer-rct-30-wheeled-infantry-fighting-vehicles-for-germany-and-the-netherlands",
        "content_sha256": "bd48b77c0ea429875c3eb83d3a184f761fb65ace94f01a41a5d6c3a114f24f16",
        "text_sha256": "681251330c2a7832b8b58bf70380147096768bd45c2d0e7b5ea21395bd9940b8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2d388c04c392e1b0",
      "claim_ids": [
        "P-SB-035"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-2d388c04c392e1b0",
        "url": "https://knds.com/en/products/systems/agm",
        "content_sha256": "7db44d8e27d57d3f2aac9486be8508b9c73de34b43606c57a5e13b7a47c224e3",
        "text_sha256": "15aa710115637a06df97b1539b58febc1520ac96d0cc50f083ccd1a3927c08b5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-2ee9de3ff66befeb",
      "claim_ids": [
        "P-SA-051"
      ],
      "note": "Army Recognition Eurosatory-2026-Artikel (ohne Metadatum, Datum im Text) gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-2ee9de3ff66befeb",
        "url": "https://armyrecognition.com/archives/archives-defense-exhibitions/2026-archives-news-defense-exhibitions/eurosatory-2026/french-army-vbci-8x8-infantry-fighting-vehicle-reveals-new-battlefield-adaptations-against-drone-threats",
        "content_sha256": "430211c4911903ca5eba045c03b5e0eaed7eaa82841667d94222ad17a5f726a0",
        "text_sha256": "80937779f5c36e48efa76f31f94c44aabce539defe48f7e20eb40744563f5533",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3090eecc207ffa9a",
      "claim_ids": [
        "P-SB-005"
      ],
      "note": "PDF-Datenblatt über source-cache.py read (extrahierter PDF-Text, mehrspaltig, Spalten vermischt) gelesen: Kopfzeile und Kästen 'Maturity and long-term support'.",
      "snapshot": {
        "source_id": "S-3090eecc207ffa9a",
        "url": "https://knds.com/media/K2_V_001_CAESAR_6_X6_EN_BAT_BDEF_91a6b0aeb4.pdf",
        "content_sha256": "34236528a48e221f63ef196c3021c4d8b3c82abee0ce5923f3b118c54e6c6e0e",
        "text_sha256": "9907574bd20279a250b49e01a526c4c25b0621dd9cb3d0c656a4b91001edeee9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "pdftotext; page markers refer to PDF pages, not printed numbering."
      }
    },
    {
      "source_id": "S-314418b5ddde95dc",
      "claim_ids": [
        "P-SA-027"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-314418b5ddde95dc",
        "url": "https://militarnyi.com/en/news/bundeswehr-first-puma-ifv-from-second-batch/",
        "content_sha256": "eaeca79060a65a564402aa99ccd767c08de7a74056664d01f99159efbb09ecdf",
        "text_sha256": "bf128b22574c48ee2731bb691af02497482d26df92af242c65d14085b06b344a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-326d2a4038c68789",
      "claim_ids": [
        "P-SA-016"
      ],
      "note": "Gelesen: cache read, Europe-1-Artikel 12.01.2023 (Zeilen 59-82 vollständig).",
      "snapshot": {
        "source_id": "S-326d2a4038c68789",
        "url": "https://www.europe1.fr/node/49630",
        "content_sha256": "c46486836ca3a91c3ac1d4a38d507c417609089435b4611ca2092bbff248916e",
        "text_sha256": "8c7e7b02096ae1e0faf421dd15f79c6d4b91647bc98c7206521ef1c75cbd1434",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-34828887c7a7a16c",
      "claim_ids": [
        "P-SD-060",
        "P-SD-061"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-34828887c7a7a16c",
        "url": "https://esut.de/2024/02/meldungen/47558/das-schwedische-heer-trainiert-mit-knds-simulatoren/",
        "content_sha256": "a5bf5bdfed58702c844ddec413cccde64ab7755a12724d1a749f0c63b1669dc2",
        "text_sha256": "ddc22d0b4ddf499dac054583f2c7be958a163703380850ed13c7b1c15a3cb418",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3496e4ec33c08cb2",
      "claim_ids": [
        "P-SA-042",
        "P-SA-046"
      ],
      "note": "Army Recognition Serval-Estland-Artikel (Jahr 2024 in Seitenkopf/Pfad) gelesen (Absätze 1-5).",
      "snapshot": {
        "source_id": "S-3496e4ec33c08cb2",
        "url": "https://www.armyrecognition.com/archives/archives-land-defense/land-defense-2024/french-army-deploys-serval-armored-vehicle-on-external-theater-for-first-time-near-russian-border",
        "content_sha256": "e931516018221b44a5e73c7299684954af4849d3cbc8684ceb6c05edaee98fec",
        "text_sha256": "3317273f5a10e52089ca0782dabb86416343428ec6758db423e3052f643c1012",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-372b572774c041fa",
      "claim_ids": [
        "P-SA-037"
      ],
      "note": "Army Recognition (2025) gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-372b572774c041fa",
        "url": "https://www.armyrecognition.com/archives/archives-land-defense/defense-news-army-2025/belgiums-first-griffon-vbmr-hits-the-ground-and-redefines-mobility-and-protection",
        "content_sha256": "cfc44830171339b63ce90c7701db394eb0255b31785580fbd245446965a165fc",
        "text_sha256": "9d5f61f6a124c783a731ab8bf223121deb1fccd9d6842284810959b891c8463a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-39b29037729ef83f",
      "claim_ids": [
        "P-SC-050"
      ],
      "note": "KNDS ULTRO-Produktseite gelesen (Absätze 1-3, Kennwerte).",
      "snapshot": {
        "source_id": "S-39b29037729ef83f",
        "url": "https://knds.com/en/products/systems/ultro",
        "content_sha256": "c686e05122eb682b6bd50b22ba98c5129d2da268197705fe2f615e3a394b2a4a",
        "text_sha256": "f3f6b647372966fd253a9660adec27c45025eff952f10c71376842317c9bb3d3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-39fa72dccabdf08b",
      "claim_ids": [
        "P-SD-011"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-39fa72dccabdf08b",
        "url": "https://www.army-technology.com/projects/dry-support-bridge-dsb/",
        "content_sha256": "32e7af83ad230e51ac09dbcd0724604aadf57349599c24c6de1bbcc3d5581d55",
        "text_sha256": "3d811ca3f0e18ba556a894f91895b4a67285be19db552a4cb084ea7c7b50c25d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3a3cf5ff81f73786",
      "claim_ids": [
        "P-SC-019",
        "P-SC-027",
        "P-SC-028",
        "P-SC-029",
        "P-SC-031",
        "P-SC-033"
      ],
      "note": "Gelesen: cache read, EDR-Magazine-Artikel 24.06.2025 (Zeilen 38-60) vollständig inkl. Fußnoten [1]-[3].",
      "snapshot": {
        "source_id": "S-3a3cf5ff81f73786",
        "url": "https://www.edrmagazine.eu/pas-2025-knds-france-further-details-its-mataris-loitering-munitions-portfolio",
        "content_sha256": "df412ac2540729a2606b26f8891e6425a3c2487d0e0cf2f478a9939fcc260c80",
        "text_sha256": "8c03ef5bea8bf1cd2c6167c7198bd2fa9b12fa462b64b15083a133073d3e6364",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3b6ac7ad2710c1a9",
      "claim_ids": [
        "P-SA-038",
        "P-SA-043",
        "P-SA-048"
      ],
      "note": "EDR Magazine 03.02.2026 gelesen (Absätze 1-5).",
      "snapshot": {
        "source_id": "S-3b6ac7ad2710c1a9",
        "url": "https://www.edrmagazine.eu/the-camo-program-reaches-a-new-milestone-with-the-order-of-269-additional-vehicles",
        "content_sha256": "7a3b629fe53a59f8176ad6afb4e7455ab66abab4a3c413f2d0af9ea953b063b4",
        "text_sha256": "85563910b8633c87c621ae966b4d237b19a0005290d08ce652756d2d7ad1aea0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3d9c8d75722ab803",
      "claim_ids": [
        "P-SA-012"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-3d9c8d75722ab803",
        "url": "https://knds.com/en/press-releases/knds-and-ritek-have-opened-new-infrastructure-for-the-leopard-production-line-in-norway",
        "content_sha256": "aec721dce9b35c06588f03e6fa99f052e024f104aff9c709b562fd9aa348d003",
        "text_sha256": "49a314e5f77872d316df70134bbff75713de1a2a8f631499099898df5dab2638",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3dc1d7011297ff48",
      "claim_ids": [
        "P-SA-062"
      ],
      "note": "Gelesen: cache read, GFF-4-Produktseite Zeilen 12-60 (Overview, Facts).",
      "snapshot": {
        "source_id": "S-3dc1d7011297ff48",
        "url": "https://knds.com/en/products/systems/gff-4",
        "content_sha256": "c5f7a25a4bfa7481b90d4865f99f998e085c7c9f14d70dd59e219861c8f4079e",
        "text_sha256": "c2ec09203cca770723246b0a93cb65f5e559971de3755e3572f14817e6d44b2a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-3f82023a2b6d96d7",
      "claim_ids": [
        "P-SC-008"
      ],
      "note": "Gelesen: cache read, Defence24-Artikel (polnisch) Zeilen 22-46; Veröffentlichungsdatum im Seitentext: 27.02.2023.",
      "snapshot": {
        "source_id": "S-3f82023a2b6d96d7",
        "url": "https://defence24.pl/sily-zbrojne/najnowszy-bonus-dla-finlandii",
        "content_sha256": "ae567f96336988546d7cada7c861fe83f5d8bda5bda489a7d736f7be94836991",
        "text_sha256": "78e4b2b7af6603a5011e9e4ab9d3443bde9245479b84e142ad27d817f35f9bca",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-40d6550e6d325387",
      "claim_ids": [
        "P-SB-056"
      ],
      "note": "defence-network.com 24.01.2025 gelesen (Abschnitt FLW 100/200 und Einleitung).",
      "snapshot": {
        "source_id": "S-40d6550e6d325387",
        "url": "https://defence-network.com/fuenf-bundeswehr-beschaffungen/",
        "content_sha256": "fa9dd7a093ea8795333f51f74d9626c380a9640325f0e593fc8e3df76ed1666c",
        "text_sha256": "1c80cc1165ed7673885b2ce37bae4fddf919bb5f1feb5cdb644090b3f3e9e867",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-413ab7fe9469ddec",
      "claim_ids": [
        "P-SB-057"
      ],
      "note": "KNDS FLW-200-Produktseite gelesen (Einleitung, Spezifikation, Abschnitt KNDS Deutschland).",
      "snapshot": {
        "source_id": "S-413ab7fe9469ddec",
        "url": "https://knds.com/en/products/systems/flw-200-range/flw-200",
        "content_sha256": "e51d0656c956db934de14784bb07cc250793446a520802117e3951058cfb342e",
        "text_sha256": "8a3f75f6ac74a47944bd1ab10a124bbf2b3d3dd9377c8526ab911068289071c0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4242af39d20d3562",
      "claim_ids": [
        "P-15"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-4242af39d20d3562",
        "url": "https://knds.com/en/products/systems/nerva-lg",
        "content_sha256": "155a043b6de87427d0c08f36b6e3e3d4ab1a4445e163639e00265cc5f83a7961",
        "text_sha256": "9e9ac8db60fcb89cf73ff554d60b405b7f90f291fc841eb567f27a36556c42ed",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-42e84694be062d71",
      "claim_ids": [
        "P-SB-032"
      ],
      "note": "BMVg-Pressemitteilung 15.09.2022: Cache-Textextrakt unlesbar (gzip); Originalbytes (source.bin, SHA-256 c8e3b558…, identisch mit Snapshot) selbst per gzip dekodiert und gelesen (Absätze 1-3).",
      "snapshot": {
        "source_id": "S-42e84694be062d71",
        "url": "https://www.bmvg.de/de/presse/bundeswehr-liefert-dingo-weitere-mars-an-ukraine-5498110",
        "content_sha256": "c8e3b558c62c44fde32aa2f85680e272865773af7099e9cc920ea1ee455581e1",
        "text_sha256": "211bea76dfd3ab1c6607eadbb879132890a20714cf0076d34efb747e5b64f2b3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser. Encoding replacement detected; inspect original."
      }
    },
    {
      "source_id": "S-45496f93e428e25f",
      "claim_ids": [
        "P-SB-061"
      ],
      "note": "ESD-Artikel 12.03.2026 (BEDEX) gelesen (Absatz 3D-Schutzökosystem).",
      "snapshot": {
        "source_id": "S-45496f93e428e25f",
        "url": "https://euro-sd.com/2026/03/news/land/49878/bedex-2026-knds/",
        "content_sha256": "50e4f2aeb221228b9bc190175dba520d63c9b11c9e744e9cd540973b7ad9b306",
        "text_sha256": "a9e31e1a741b51193e0b339bc340a4b44fc6ca8bad11816030c96d011db5e316",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-459a4d4a1990b30e",
      "claim_ids": [
        "P-SC-021"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-459a4d4a1990b30e",
        "url": "https://defensemirror.com/news/41033/France_Qualifies_DAMOCLES_Short_Range_Remotely_Operated_Munition_after_Trials",
        "content_sha256": "61147cd23b4b124ad9687d4bccc37a766ec2374efe762f3e346aa5fbe53a61da",
        "text_sha256": "e007b94699c657c9ef30de5eb49f67faca9e2c04f47ffca4a21c6fdc465a59f3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-47bb621c6a3c6d4c",
      "claim_ids": [
        "P-SD-001",
        "P-SD-065"
      ],
      "note": "Gelesen: cache read, EDR-Artikel (Wiedergabe der KMW-Mitteilung) vom 10.12.2019 vollständig (Zeile 42 Haupttext).",
      "snapshot": {
        "source_id": "S-47bb621c6a3c6d4c",
        "url": "https://www.edrmagazine.eu/the-netherlands-receive-the-first-leguan-bridge-layers",
        "content_sha256": "bd88e815b6b19a91fba5418c6d91b7c6775d44da8483b809001cd5cc52b378ec",
        "text_sha256": "a60146c9167db87fbd77e603c3723ca217de8e1f35b451608a313e72cd1fc5d6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4a4602eb35f54d01",
      "claim_ids": [
        "P-SA-008"
      ],
      "note": "Gelesen: cache read, Defence24-Artikel (polnisch) vom 29.10.2019, Zeilen 22-46 vollständig.",
      "snapshot": {
        "source_id": "S-4a4602eb35f54d01",
        "url": "https://defence24.pl/sily-zbrojne/leopardy-2a7-przekazane-bundeswehrze-i-armii-danii",
        "content_sha256": "5743ebc350c7ca601bd560d0c1410abc51c1a6a5777fe1eaf3aa52d9289c5403",
        "text_sha256": "420b4b7cb1f186ee24a6ddf7f4158a3255bd7130319f473b09ee442826bc511e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4c8c6bf777afe77f",
      "claim_ids": [
        "P-SA-015"
      ],
      "note": "hartpunkt 17.12.2025 gelesen (Absätze 1-4).",
      "snapshot": {
        "source_id": "S-4c8c6bf777afe77f",
        "url": "https://www.hartpunkt.de/bundeswehr-beschaffungsamt-bestellt-44-leopard-2-a8-kampfpanzer-fuer-kroatien/",
        "content_sha256": "fe90b2ab0dead597b2ea6b6f91793a7c8ffdd704abca7d91642f893177d1c5a8",
        "text_sha256": "b05b27b1c37a1ceade628a4c2adad80864a2fd73c41dd79ceaa62d8f9c09700b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4caf2e8adadc1cdf",
      "claim_ids": [
        "P-SD-051",
        "P-SD-053"
      ],
      "note": "EDR Magazine (Pressemitteilung KNDS CBRN, Brüssel 13.03.2026) gelesen (Absätze 1-12).",
      "snapshot": {
        "source_id": "S-4caf2e8adadc1cdf",
        "url": "https://www.edrmagazine.eu/bedex-2026-three-new-orders-from-the-dga-for-knds-cbrn-subsidiary-of-knds-france-global-specialist-in-cbrn-detection-protection-and-decontamination",
        "content_sha256": "72ed70a19d4229263f0b4edbc575328bc1309705b52d61b08b5d15825fcb55dd",
        "text_sha256": "fdc53c2038b048148d793f1ec8c1598b5c1c4b51b3aee821417ec04b8a99f547",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4d6adea9226ecb34",
      "claim_ids": [
        "P-SB-057"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-4d6adea9226ecb34",
        "url": "https://knds.com/en/products/systems/flw-200-range/flw-200-plus",
        "content_sha256": "61bcbfe2a048293b5cbc866df952e8fecab0bb7127022648e19a674140183953",
        "text_sha256": "46c31cfdd841561b27e834654c27ed800633fedd4c9fb3bf12c6d7ed01a6452c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4da0f1a41c4b8354",
      "claim_ids": [
        "P-SB-042"
      ],
      "note": "Gelesen: cache read, Army-Guide-Artikel (GD ELS/KMW-Pressetext, AUSA 2009) Zeilen 33-41.",
      "snapshot": {
        "source_id": "S-4da0f1a41c4b8354",
        "url": "https://army-guide.com/eng/article/article_1443.html",
        "content_sha256": "709c8b095383fe822696ad0b78c892caebefe977fd40d72b0bdd6966b709eb55",
        "text_sha256": "3037404eb159e824d0907d5ba67f080320137fae22fbfee7cb1bd14e75d80890",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-4f97ad522106cb38",
      "claim_ids": [
        "P-09",
        "P-12",
        "P-16",
        "P-18"
      ],
      "note": "KNDS-Systemübersicht gelesen (Abschnitte Artillery, Turrets, Cannons, Bridges, Robotics).",
      "snapshot": {
        "source_id": "S-4f97ad522106cb38",
        "url": "https://knds.com/en/products/systems",
        "content_sha256": "d11bed87f650feb1bde3848854724028f52868a1b58b6121018be05e67a63e72",
        "text_sha256": "9169634371e746cadbef73b31b20be9dc7bedd14477756fab361f9de38adaefa",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-51e10c963ec834f4",
      "claim_ids": [
        "P-SA-012",
        "P-SA-013"
      ],
      "note": "Gelesen: cache read, Janes-Artikel vom 12.05.2026 vollständig (Zeilen 17-21).",
      "snapshot": {
        "source_id": "S-51e10c963ec834f4",
        "url": "https://www.janes.com/defence-intelligence-insights/defence-news/defence/norway-opens-leopard-2a8-production-line-receives-first-two-mbts",
        "content_sha256": "b2a73a2515d3a87f64d200d3b475dc0edaa2ab94a0dd136cefd0ace05cd67c0b",
        "text_sha256": "5479236c05133d3122cc766b1a29ba0837cadcfd499651d06cfe7cca195040fa",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-55e7ca27a0361c81",
      "claim_ids": [
        "P-SD-042"
      ],
      "note": "Extrakttext aus source-cache.py read war durch gzip-Bytes beschädigt (Hinweis 'Encoding replacement detected'); Original aus den gespeicherten Originalbytes (source.bin, gzip) dekodiert und Artikeltext vollständig gelesen; Veröffentlichungsdatum 16.10.2026 auf der Seite bestätigt.",
      "snapshot": {
        "source_id": "S-55e7ca27a0361c81",
        "url": "https://www.bmvg.de/de/presse/einsatzpruefung-ruestungsprogramm-d-lbo-6165388",
        "content_sha256": "f4ed76f5cc6255809a296f2d5167c57839b5419b9ee44d58face1cf0da0b5b83",
        "text_sha256": "5cb96dd36b2272c921882affe4ccdd2246890ad9d4b9b47a0f67ab8dd8bab24f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser. Encoding replacement detected; inspect original."
      }
    },
    {
      "source_id": "S-584f9f611e8055e9",
      "claim_ids": [
        "P-SB-028"
      ],
      "note": "Gelesen: cache read, ESD-Artikel vom 03.04.2024 (Zeilen 95-109) vollständig.",
      "snapshot": {
        "source_id": "S-584f9f611e8055e9",
        "url": "https://euro-sd.com/2024/04/major-news/37346/rheinmetall-pzh-2000-order/",
        "content_sha256": "1c47deed4cc4bf8e49e89cda185f107248e7aa0077d083dcbde6d64a1fdc7d52",
        "text_sha256": "1ad955501cab263d032f7a6edd40d492e4ed7cacdb93f127bc9eff387266e5d6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-59e8dbacbb32b001",
      "claim_ids": [
        "P-SC-051"
      ],
      "note": "Gelesen: cache read, auto-motor-und-sport-Artikel vom 07.04.2026 (Zeilen 31-50) vollständig.",
      "snapshot": {
        "source_id": "S-59e8dbacbb32b001",
        "url": "https://www.auto-motor-und-sport.de/verkehr/neuer-ultro-was-kann-der-bollerwagen-fuer-soldaten/",
        "content_sha256": "0895ebfc4c3191e65ec3034c53a18a92b0e98a0b92a827cba7348125c0549c7f",
        "text_sha256": "41f04a7b5cfaf911aa47f75e6cbe12a02f5cba203e12bde82a0567c5056914e6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5a6a692d962fc23f",
      "claim_ids": [
        "P-SD-013"
      ],
      "note": "Gelesen: cache read, Army-Technology-Artikel vom 08.03.2018 (Zeilen 149-180 inkl. nachgeladenem Textblock ab Z. 171).",
      "snapshot": {
        "source_id": "S-5a6a692d962fc23f",
        "url": "https://www.army-technology.com/news/wfel-delivers-first-tranche-military-bridges-adf/",
        "content_sha256": "3ee1084993682318fc7a003b36fe11ab0c50561fcee6b23c84da65902299ab9d",
        "text_sha256": "a5c8a99986d60ad69d998550c9100d5a2394ae209f416de7d9ab3f7963629f11",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5b1a551b6e9e9475",
      "claim_ids": [
        "P-SD-006"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-5b1a551b6e9e9475",
        "url": "https://ukdefencejournal.org.uk/lithuania-orders-leopard-2-bridge-layers-in-knds-deal",
        "content_sha256": "51a4972490a46ecf8d7e0b2823115aeaaa5dc0bca404e7f20948c139d03d4aa1",
        "text_sha256": "33064de4da3ca2b607eb81ed71e1334bd05b07fd18f9ad6cb7da490fd13fc15d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5d0f11d37d7d69bf",
      "claim_ids": [
        "P-SD-072"
      ],
      "note": "Army Technology 02.10.2024 gelesen (Absätze 1-12).",
      "snapshot": {
        "source_id": "S-5d0f11d37d7d69bf",
        "url": "https://www.army-technology.com/news/knds-opens-ukraine-subsidiary-to-enhance-mro-of-systems/",
        "content_sha256": "4a374dd3430b39202e457b6c497bac8ff00da47251ccb1421d0ccbed23fd0259",
        "text_sha256": "d9552a32aa7a0ceb3e59a16bdcf90d3fbdd97dfca43d15c7c7112c024246ed9a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5d64e28c5982c862",
      "claim_ids": [
        "P-SC-049"
      ],
      "note": "Defense Mirror 08.02.2025 gelesen (Absätze 1-3).",
      "snapshot": {
        "source_id": "S-5d64e28c5982c862",
        "url": "https://defensemirror.com/news/38791/KNDS__Safran_to_Develop_Land_Robotics_for_France",
        "content_sha256": "1e4dc64a6aeffda8bcf0ee10875ab29a02ed356bcbd71e8bf63ec7c01b23faf0",
        "text_sha256": "d173bbadda689799a72bc534ccf0352677ce41ad95d8a8a450cae81a4739952b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5ddece3621c9c23c",
      "claim_ids": [
        "P-SA-055"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung Zeilen 11-31; Datum im Text '06.12.2023' (Z. 14).",
      "snapshot": {
        "source_id": "S-5ddece3621c9c23c",
        "url": "https://knds.com/en/press-releases/knds-commissioned-to-supply-50-dingo-2-vehicles-to-the-bundeswehr",
        "content_sha256": "b680be0cd2873de7d8870ce8ea6f6912cf6e084b4f6fd5a6ed95596788830d2f",
        "text_sha256": "527fae6653e5a6065624c48864210bbd9f4825bef391ab75f9f93485dc8d0fa0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-5f3c57dfe3f913fd",
      "claim_ids": [
        "P-SB-012"
      ],
      "note": "Ukrinform 15.03.2026 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-5f3c57dfe3f913fd",
        "url": "https://www.ukrinform.net/rubric-ato/4101916-more-than-600-ukrainian-artillery-soldiers-finish-training-on-new-artillery-system-in-germany.html",
        "content_sha256": "b878ef43ff719250b20d799cd597b2664c57a787107758825d8b32d676db75e9",
        "text_sha256": "1ddd98c792a22e4eeaf9603bc92244b4054d19a1be99db40bfc9af980dc751e0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-612d6e55d2eb1a65",
      "claim_ids": [
        "P-SA-059"
      ],
      "note": "KNDS-Seite DINGO 3 (Deutsch) gelesen (Einleitung, Faktenabschnitt, Schlussabsatz).",
      "snapshot": {
        "source_id": "S-612d6e55d2eb1a65",
        "url": "https://www.knds.de/en/systems-products/wheeled-vehicles/dingo/",
        "content_sha256": "bdbcc8623ef3ce822c912b6268f7c893d494c285f6f4dd5c5fe9abc5eb55cbbd",
        "text_sha256": "c41ecb11a5986af158e90bf2407abf8827ddd81ab0b5f90c822604e348b3e9bc",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-615341f26bb37ce2",
      "claim_ids": [
        "P-SB-016"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung (deutsch) vom 19.12.2025 Zeilen 11-19.",
      "snapshot": {
        "source_id": "S-615341f26bb37ce2",
        "url": "https://knds.com/de/pressemitteilungen/deutschland-beschafft-radhaubitze-rch-155-von-knds",
        "content_sha256": "1903ee8db7df46b71b6616c84830ae2b39e7ba555015db760b1a779e583ef1cb",
        "text_sha256": "011cd9a1242be570c03cc3d792a760be7beb70850a1a933e25cc3486322d1f6c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-62287c49ce019261",
      "claim_ids": [
        "P-SA-047"
      ],
      "note": "Gelesen: cache read, Theatrum-Belli-Artikel vom 24.01.2026 (Zeilen 87-124) vollständig.",
      "snapshot": {
        "source_id": "S-62287c49ce019261",
        "url": "https://theatrum-belli.com/trente-premiers-serval-appui-scorpion-livres-a-larmee-de-terre/",
        "content_sha256": "47897c5d729e1fffb73540abad9d155bb27e46baddc269c0a50735a725b7191f",
        "text_sha256": "5979ffd65dd1229b4e857fdf286aefd66a26e30fb1f0cefadbdd1b88169c4b20",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-647e234dfcf4098f",
      "claim_ids": [
        "P-04"
      ],
      "note": "KNDS BOXER-RCT30-Produktseite gelesen (Einleitung, Spezifikation, Beschreibung).",
      "snapshot": {
        "source_id": "S-647e234dfcf4098f",
        "url": "https://knds.com/en/products/systems/boxer/boxer-rct-30",
        "content_sha256": "ee7a4d30b43309453e72fe2072433ab50888fc35874874c24365202836f1d452",
        "text_sha256": "2c8b1aa679c9926c2a79d8f148f2604c8ca3802fcd43772742a952fa4b79a36e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-64902f4dbe1a905a",
      "claim_ids": [
        "P-19",
        "P-SD-015"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-64902f4dbe1a905a",
        "url": "https://knds.com/en/products/equipment",
        "content_sha256": "c935cd371e60fda8d1fe08768ec7b55f7cdaeab3f1ea6c87ab0585454dcdc9c8",
        "text_sha256": "9ab5d847974fce164d94139a927b4b19b9e0371dcb50dd1146bcee96b63a3301",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-670840d28766decf",
      "claim_ids": [
        "P-SD-060",
        "P-SD-061"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung 13.02.2024 (Zeilen 13-18).",
      "snapshot": {
        "source_id": "S-670840d28766decf",
        "url": "https://knds.com/press-releases/cutting-edge-knds-simulators-for-swedish-armed-forces",
        "content_sha256": "dc6b6c5971f44bc6255b6588116afe9e5dcc44d70fc053afedd75fe40594f1c1",
        "text_sha256": "e27e5697cc014bfad50ff7ab6e5617abb14edb042b7b4776d4e50bb2a1490680",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-674182f0d8468117",
      "claim_ids": [
        "P-SC-004",
        "P-SC-005"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-674182f0d8468117",
        "url": "https://knds.com/en/press-releases/inauguration-of-a-new-155-mm-artillery-shell-production-unit-at-knds-belgium-a-major-strengthening-of-belgian-and-european-industrial-capacity",
        "content_sha256": "91dc752c2b751e1c808df65bcb31682e8351276e1c61965bbdf7e40317065741",
        "text_sha256": "a63b6b4de08bf7393b8c1e834aea739efa83e5dc1eb6d5c66f8d9605bb713eac",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-683ba892c2c8c1d5",
      "claim_ids": [
        "P-SC-026"
      ],
      "note": "KNDS MV-25-OSKAR-Produktseite gelesen (Absätze 1-3).",
      "snapshot": {
        "source_id": "S-683ba892c2c8c1d5",
        "url": "https://knds.com/en/products/ammunition/mv-25-oskar",
        "content_sha256": "38bed25071a98a402a5eea191fd218252ceb71a666b02c7c0d4a0e029db2f5fa",
        "text_sha256": "25ec8ca7eda16ec85ad66f5bf7ba7f235abf17acc754a5f831fbaeeac3845d70",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-687b84418c044515",
      "claim_ids": [
        "P-SD-002"
      ],
      "note": "Gelesen: cache read, ESUT-Meldung (03.08.2020) Zeilen 124-131 (Artikeltext vollständig, Rest Navigation/Cookie-Text).",
      "snapshot": {
        "source_id": "S-687b84418c044515",
        "url": "https://esut.de/2020/08/meldungen/22096/liefervertrag-fuer-weitere-leguan-brueckenlegesysteme/",
        "content_sha256": "7f96212202d5424cd1ad017a8c7390373c50fb32693ba55e43026f9ac5b1d769",
        "text_sha256": "576b7ad6c3d057b884249d13a363db755d1290e1337abb484fc3df6e7e47eae1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-69fd8295dce358bf",
      "claim_ids": [
        "P-SB-034"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-69fd8295dce358bf",
        "url": "https://www.defensa.com/otan-y-europa/alemania-da-gran-impulso-artilleria-lanzacohetes",
        "content_sha256": "61a420ca38ef533379ef370d1f812a3fe3b8418903c77ebe4e3c9f723b6dacc9",
        "text_sha256": "afb461a219b1d600b3bdf90c455058505bf621a7557deefdc18f5fcadbd469fe",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6bc5f70defe492d2",
      "claim_ids": [
        "P-SA-037"
      ],
      "note": "Frei sichtbarer Janes-Artikeltext (Abs. 1-4) über source-cache.py read gelesen; Janes-Zusatzmaterial hinter Abo nicht benötigt.",
      "snapshot": {
        "source_id": "S-6bc5f70defe492d2",
        "url": "https://www.janes.com/defence-intelligence-insights/defence-news/land/belgian-army-presents-griffon-vehicles",
        "content_sha256": "f34a0319141d947472414fc5f4637a5055989aae3e3b41491d1be3554e8f7520",
        "text_sha256": "8c7c56d84049e8bc45ecdf4ffde6d095adfe10d5a8d83c8ec16fa90353a0be2a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6bfb59bbe9a3dcf6",
      "claim_ids": [
        "P-SB-052"
      ],
      "note": "Gelesen: cache read, Keystone-SDA/dpa-Meldung vom 25.07.2025 (Zeilen 38-50).",
      "snapshot": {
        "source_id": "S-6bfb59bbe9a3dcf6",
        "url": "https://www.bluewin.ch/en/news/international/more-than-60-gepard-anti-aircraft-tanks-already-in-ukraine-2798943.html",
        "content_sha256": "afa7d1e88d130a304fee7b33cac8857920531e66ada20b48caa9b3751b0c17af",
        "text_sha256": "48fcdb2f3e13b09f543e5aedc791ad8137df28146540991d725c4879212b333e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6c6ee0e3fd30c937",
      "claim_ids": [
        "P-SA-018"
      ],
      "note": "Gelesen: cache read, Defense-Mirror-Artikel vom 31.01.2025 (Zeilen 72-84) vollständig.",
      "snapshot": {
        "source_id": "S-6c6ee0e3fd30c937",
        "url": "https://defensemirror.com/news/38732/French_Armament_Directorate_Orders_Renovation_of_100_Leclerc_Tanks",
        "content_sha256": "4d6646cb87c676c413fb35d57328a8f8ba5fef8965d39e4728a6ef8b9dfdb12b",
        "text_sha256": "6f5b3a2249b4a14433b474f9602dac7d01dccdf8ca22e0bc9c8434d747080799",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6c84242ff77b4c1c",
      "claim_ids": [
        "P-SC-004",
        "P-SC-005"
      ],
      "note": "Gelesen: cache read, EDR-Magazine-Wiedergabe der KNDS-Belgium-Mitteilung (Zeilen 38-46) vollständig.",
      "snapshot": {
        "source_id": "S-6c84242ff77b4c1c",
        "url": "https://www.edrmagazine.eu/inauguration-of-a-new-155-mm-artillery-shell-production-unit-at-knds-belgium-a-major-strengthening-of-belgian-and-european-industrial-capacity",
        "content_sha256": "1f7c67347219acaf8da94877143d0f3dedccdf0006795009ec86cc53831c4968",
        "text_sha256": "9ebeb7e61ac90dc37e672e5b0ca0a99c92c90d0f06cec7b3c832de29c7481aa5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6c8b3e18669d4597",
      "claim_ids": [
        "P-SB-023"
      ],
      "note": "Gelesen: cache read, Rheinmetall-Pressemitteilung vom 31.07.2026 (Zeilen 10-22) vollständig.",
      "snapshot": {
        "source_id": "S-6c8b3e18669d4597",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2026/07/2026-07-31-rheinmetall-liefert-waffenanlage-fuer-britische-radhaubitze-rch-155",
        "content_sha256": "212c4619cfd38fe7a80b65ca6f18741904375cd03444086d8a316700ccb847df",
        "text_sha256": "0c0021a67c6ad71000a4e30c0c85264ec16dafbea2dde13aa692ab699be600ce",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6e26579fbf388dc1",
      "claim_ids": [
        "P-SB-063"
      ],
      "note": "KNDS-THL20-Produktseite gelesen (Einleitung, Faktenabschnitt).",
      "snapshot": {
        "source_id": "S-6e26579fbf388dc1",
        "url": "https://knds.com/en/products/systems/thl-20",
        "content_sha256": "be6d9938bb4f0ae4deca0e7a343bb4660aa3aa6eae11f629a393fc5256071668",
        "text_sha256": "7ae63aa914e429db7283081048f8bceac48c946ce9ec36e14ddebe4a2e4f7366",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6e37c58f05fb5c88",
      "claim_ids": [
        "P-SB-058"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-6e37c58f05fb5c88",
        "url": "https://knds.com/press-releases/from-identification-to-neutralization-knds-france-unveils-the-serval-counter-uav-variant",
        "content_sha256": "5ae7d99677e6309c00267d0235b47d7f00ed4151952ffeb68b9f124b93f50765",
        "text_sha256": "563e945a3c7b300941b26ca1ecdd0a29d0f007bad36339395b6e16b3ce9a7b99",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-6efe75db8d4fd730",
      "claim_ids": [
        "P-SC-020",
        "P-SC-024",
        "P-SC-029",
        "P-SC-033"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-6efe75db8d4fd730",
        "url": "https://breakingdefense.com/2025/06/knds-mataris-loitering-munitions-finding-contracts-from-french-government/",
        "content_sha256": "47d7a59d526567e7354b00c5425533f63ac4dfec275c396975e83eaee7835ba0",
        "text_sha256": "c3e1f668f970186cfefde953adc67f9d522836842edd80ac63f243fe936d62c9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-70dc963267bd3ddf",
      "claim_ids": [
        "P-SB-049"
      ],
      "note": "defence-network.com 01.10.2024 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-70dc963267bd3ddf",
        "url": "https://defence-network.com/munition-leopard-knds-geht-in-die-ukraine/",
        "content_sha256": "ff20af4691e986cdd954cb9ee75230567ea79dcedfe6b056615c15b6528661b2",
        "text_sha256": "b71186210db9975feb0cc1abbad61904818562fbe11b479ac8599cbc2791d738",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-716eee0af365f067",
      "claim_ids": [
        "P-SC-035"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-716eee0af365f067",
        "url": "https://armyrecognition.com/news/army-news/2026/new-french-mataris-drone-could-turn-every-military-vehicle-into-an-independent-strike-unit",
        "content_sha256": "46fac07629aa598132859eb0132d7fe1b2d4c3ef0b7d2376aac05a6d9fcbd181",
        "text_sha256": "e1f321b69e4a2671f8ef404adce1be61b3312128df4616a0e28492bc5fb76bc5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-735b6d1356a73251",
      "claim_ids": [
        "P-SB-004"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung vom 16.06.2026 (Zeilen 11-27) vollständig.",
      "snapshot": {
        "source_id": "S-735b6d1356a73251",
        "url": "https://knds.com/en/press-releases/malaysia-becomes-the-15-th-caesar-customer-country-with-an-initial-order-of-18-artillery-systems",
        "content_sha256": "1a2dd7ea40987503356e38d31132e4e34d293a8ddaa4be2d31dbe1358452b02b",
        "text_sha256": "2510707e189b69dc8f80b9b1c834eaf6bb95be3a137f976802150408423c2bcd",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-736964fb687bbb29",
      "claim_ids": [
        "P-SC-043",
        "P-SC-051"
      ],
      "note": "Gelesen: cache read, Military-Aktuell-Artikel vom 26.03.2026 (Zeilen 213-241) vollständig.",
      "snapshot": {
        "source_id": "S-736964fb687bbb29",
        "url": "https://militaeraktuell.at/en/knds-expands-nerva-robot-acquisition-to-include-the-german-market/",
        "content_sha256": "cee01e98057942f9816331eac8961bed08dd99c6b85ed27145899a5ae29910ee",
        "text_sha256": "d970641e244dbf2508d9566899036b40b365787e4862cd8992bb5d3d3d0f7e35",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7455eac2de5250a1",
      "claim_ids": [
        "P-SB-039"
      ],
      "note": "Armada International 02.07.2026 gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-7455eac2de5250a1",
        "url": "https://www.armadainternational.com/2026/07/swiss-army-replacing-m109-howitzers-with-piranha-donar-foc/",
        "content_sha256": "b6884b46f8312e020af2cd0336e59d215a5c6c0bdf009db7ed4092c742587400",
        "text_sha256": "7c8b7bb08815738c577c4a8b3e1427f89beb464b813179560bb89be0917af707",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-75166609aad6b378",
      "claim_ids": [
        "P-SD-071"
      ],
      "note": "Babel 21.01.2025 gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-75166609aad6b378",
        "url": "https://babel.ua/en/news/114671-leopard-tank-manufacturer-creates-joint-venture-in-ukraine-to-help-with-equipment-repairs",
        "content_sha256": "6edbea2c82dd875340039704eef42317fae90483a69e0fdf173d8f104c04e7ee",
        "text_sha256": "0c63ecee5b1b11e55f6b3f5c52ee741adc6aef60c6c75bbc5f8dbd170044f5fb",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-762f7c6bc635d7a2",
      "claim_ids": [
        "P-SC-040"
      ],
      "note": "Al Defaiya 11.06.2021 gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-762f7c6bc635d7a2",
        "url": "https://www.defaiya.com/news/International%20News/Europe/2021/06/11/nexter-partner-of-french-army-for-first-air-land-robotics-day",
        "content_sha256": "73fa443059155a9d1342fb0ca1bf54dbd6e3916edbcb27b2a7ac9b761f0af929",
        "text_sha256": "5fac7dfde6c9a496d2c64ff0a53a3a56f478a4ef11234175dbd98feb5ab274d7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-77aababed8daf0b8",
      "claim_ids": [
        "P-SB-059"
      ],
      "note": "KNDS ARX25-Produktseite gelesen (Abschnitte 1-6).",
      "snapshot": {
        "source_id": "S-77aababed8daf0b8",
        "url": "https://knds.com/en/products/systems/arx-25",
        "content_sha256": "b082a6e21d47374532662423e64b8fa5837b5850e43a8eac0f7cb71207709838",
        "text_sha256": "966daf94f02f1df30fc20f024b25f254ab32ca36f84071f6cd9d5bb09bcf9703",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7836dc8f37af6164",
      "claim_ids": [
        "P-SB-030"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-7836dc8f37af6164",
        "url": "https://knds.com/en/products/systems/mars-ii-mlrs-evolution",
        "content_sha256": "3545373e46dac75c517f17738b5bc59b3d8917c6e3124d7c507e31bfd49ef4b8",
        "text_sha256": "391847769e491b7179822fa54c953973df83dd1afebdb4d6aaf367fccaa1da8a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7a154b749e856b87",
      "claim_ids": [
        "P-SC-011",
        "P-SC-013"
      ],
      "note": "Gelesen: cache read, Defense-Post-Artikel vom 24.06.2024 (Zeilen 33-56).",
      "snapshot": {
        "source_id": "S-7a154b749e856b87",
        "url": "https://thedefensepost.com/2024/06/24/france-knds-artillery-shell/",
        "content_sha256": "a981e6ac923c6711247b9810ce427611ad8b99fadadbd8e883a7e34834e46fdc",
        "text_sha256": "5e6de853f1379a7a6238812769b8cff7ec51a45cfebf5834ff1e72537df5ad9b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7d4e2671399627b1",
      "claim_ids": [
        "P-SB-002"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung (Amsterdam, 26.05.2026) Zeilen 11-29; Absatz zum Ramp-up Zeile 29.",
      "snapshot": {
        "source_id": "S-7d4e2671399627b1",
        "url": "https://knds.com/en/press-releases/knds-achieves-strong-revenue-growth-and-record-order-intake-in-2025",
        "content_sha256": "37889d63c6ba36ca13825b41b75f1db12b4cc8b975e4151b40ce242afb1dbf3b",
        "text_sha256": "dd5de2b5cc145db60f47497feee72d11c1841e04fcdd8420fa2a02dfd3f8d653",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7de56aec0f84a3c6",
      "claim_ids": [
        "P-SC-032"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-7de56aec0f84a3c6",
        "url": "https://knds.com/en/products/ammunition/mt-10",
        "content_sha256": "d98c5086ca4f5e67f3830c99b06c001f2a0308ac151c9b0b4ddd0fb253e3799d",
        "text_sha256": "f5ef641cdcfd583b5e7e48b4dad3520f6a18af22e39f33bf7d419458f965428d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7fa97d679979c2c6",
      "claim_ids": [
        "P-SB-009"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-7fa97d679979c2c6",
        "url": "https://defence-network.com/bundeswehr-und-british-army-erhalten-rch-155/",
        "content_sha256": "a384a10319c8860eb1604757392ec64506833068a88314ec4c86e35343808cdd",
        "text_sha256": "0ea3c10b0d81a9e4c5ddc81be8c3d1e5d4665692fb45d0b2b040a17c50693a53",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-7fcb16935538891a",
      "claim_ids": [
        "P-SA-009"
      ],
      "note": "Frei sichtbarer Janes-Artikeltext (Abs. 1-6) über source-cache.py read gelesen; Zusatzinhalte hinter Abo nicht benötigt.",
      "snapshot": {
        "source_id": "S-7fcb16935538891a",
        "url": "https://www.janes.com/defence-intelligence-insights/defence-news/land/knds-deutschland-orders-trophy-aps-for-german-armys-future-leopard-2a8-fleet",
        "content_sha256": "6eba75bb6741dbcefea95bb005de262b2914db1b575654475d52489a8d9cb005",
        "text_sha256": "9fc7166e8eb183611c6ad97d33730b7d0cb084b7e04d15ca3660ce267f801398",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-804fa628e354cfad",
      "claim_ids": [
        "P-SB-064"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-804fa628e354cfad",
        "url": "https://idrw.org/knds-thl20-turrets-selected-for-indias-new-light-combat-helicopter-program/",
        "content_sha256": "2cb52d2877726cdd73afc3dd1f388fca3b50e606018b437e41dd47e1ac4446f8",
        "text_sha256": "350483a4544be68b7bcecb3c01ef0c59a7e2194d70617f421f9304aac6640324",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-81ce428ece268924",
      "claim_ids": [
        "P-SC-048"
      ],
      "note": "Defence24 (polnisch) gelesen (Absätze zu Centurio X30 und Chronologie).",
      "snapshot": {
        "source_id": "S-81ce428ece268924",
        "url": "https://defence24.pl/polityka-obronna/idex-2025-knds-pokazuje-bezzalogowiec-ladowy-x30",
        "content_sha256": "063a5f051ff759d9634d78c9f1f3778e3984b8e74fd5d43eee06572306795c7c",
        "text_sha256": "10df15e41b9059d482f534c016a7637850f8fb4c26f3e58b665cc4a560cae4b4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-82a378b89948e5f5",
      "claim_ids": [
        "P-SA-063"
      ],
      "note": "Gelesen: cache read, Army-Technology-Projektseite GFF 4 (Zeilen 152-200); undatiert.",
      "snapshot": {
        "source_id": "S-82a378b89948e5f5",
        "url": "https://www.army-technology.com/projects/gff-4-wheeled-armoured-vehicle/",
        "content_sha256": "fb5053538bf4fb25bbc1ce91e7c352e7f967eaec2d5540ff5d44560c458cca1b",
        "text_sha256": "2482721b0cd86abb520e32e04aecf8a9c393a64fb6177ee546677e1683a21571",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8353b232dcdf4c30",
      "claim_ids": [
        "P-SD-014"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-8353b232dcdf4c30",
        "url": "https://des.mod.uk/bridging-the-gap-essential-military-bridging-contract-secures-300-uk-jobs",
        "content_sha256": "61f3d28ad5996049a20486abf0f6e3417725ba09a58879fe604ab50bddded84d",
        "text_sha256": "25976b33138c446633f83f391509fe30467fc190c3ee2090b64405abfd7dcff4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-838217822395dd4a",
      "claim_ids": [
        "P-SB-036"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-838217822395dd4a",
        "url": "https://euro-sd.com/2024/05/major-news/38218/knds-gdels-install-agm-on-hmc/",
        "content_sha256": "ad2da6e32e787ee8c1969f75eeee4f087efc21f358fd156464927ae7b7d04624",
        "text_sha256": "6e532884890ca14c8178fefa5a2d74658619b9b64c981d504c2b1023fd2a0c77",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-853f4c3e4301aa4d",
      "claim_ids": [
        "P-SD-030"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-853f4c3e4301aa4d",
        "url": "https://knds.com/en/products/bridges/hstb",
        "content_sha256": "29616f910ac4557ba86700f82ca8dbc2ed33c20bf062bf217aef96ace03074f4",
        "text_sha256": "9ba7ce1ef52967dd461a8c59f14eb1289da82debe093c8066f1358a80db530be",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-86b2f2d091553389",
      "claim_ids": [
        "P-SD-040"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung (München/Koblenz, 19.12.2024) Zeilen 13-19.",
      "snapshot": {
        "source_id": "S-86b2f2d091553389",
        "url": "https://knds.com/en/press-releases/order-worth-billions-knds-and-rheinmetall-will-equip-10-000-bundeswehr-vehicles-with-digital-radio-equipment",
        "content_sha256": "bebf3c758baed196b8606a23fc47353c72ef3003c89d64e82162d938b21d36a2",
        "text_sha256": "a344cbcc3e94a2606a7439ada4c8936d3aa6529ef7be1a8d3ab0946b90b9ac18",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-86d61336ff39d3dd",
      "claim_ids": [
        "P-SB-037"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-86d61336ff39d3dd",
        "url": "https://esut.de/en/2024/06/meldungen/51049/artillerie-geschuetz-modul-auf-boxer-und-piranha-in-direktem-vergleich/",
        "content_sha256": "db93ac129d2c13ee52c2f7e9cf3d93dba0cd2ad921eeb247eabb85e8da24caa8",
        "text_sha256": "6e57ee189574ae4aa0e9c8e5da28c08fec99525ff219868fd5b7cee40ea6df51",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-87963d9398e36190",
      "claim_ids": [
        "P-SB-014",
        "P-SB-015"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-87963d9398e36190",
        "url": "https://militarnyi.com/en/news/ukraine-receives-first-rch-155-self-propelled-howitzer-german-aid-to-ukraine/",
        "content_sha256": "898160c530e6ab718f4a3b307f2976d14b9d364924ec078c7abc76388d2612ee",
        "text_sha256": "0067f3841d72b29822a79425b2a2543339e9806c1342d0f0226b67afe7a79c0b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-88235a3b6dda2acd",
      "claim_ids": [
        "P-SC-038"
      ],
      "note": "Gelesen: cache read, EDR-Meldung (Ministerium-Mitteilung vom 20.09.2019) Zeilen 38-55.",
      "snapshot": {
        "source_id": "S-88235a3b6dda2acd",
        "url": "https://www.edrmagazine.eu/france-the-ministry-of-the-armies-will-soon-receive-reconnaissance-micro-robots",
        "content_sha256": "9df73914adaff4504212aa0b28c1182a4b8866467be2e593751839925ba167c6",
        "text_sha256": "d6f393a1debab5fdef13e45358bf3c810b997ec3ce526e6caecc17f5a8d7e571",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-89bdf6749f713790",
      "claim_ids": [
        "P-SC-018",
        "P-SC-034"
      ],
      "note": "KNDS-Pressemitteilung 18.06.2026 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-89bdf6749f713790",
        "url": "https://knds.com/en/press-releases/knds-asserts-leadership-in-loitering-munition-at-eurosatory-2026",
        "content_sha256": "398600ece39f0525d998d12247a04cd63a97a2c824f676ce2da333f8281f0243",
        "text_sha256": "36515ec54b592a21e3eba1ed20e27a8999667cbc43875576f30db474b92c55c4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-89dce88192650540",
      "claim_ids": [
        "P-SC-009"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-89dce88192650540",
        "url": "https://knds.com/en/products/ammunition/155mm-ammunition/155-katana",
        "content_sha256": "24f8ce49d682b98238a7fb7fa40095005590d9685517c4aed6e64dfb7eaa19a6",
        "text_sha256": "cad3b2cdb862d2904a3b8a9191424a0a195d9a853bfa154842d809fee5c4b732",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-89dd10c16b4f1318",
      "claim_ids": [
        "P-SA-004"
      ],
      "note": "Gelesen: cache read, Defence-Industry-Europe-Artikel vom 08.10.2023 (Zeilen 11-22).",
      "snapshot": {
        "source_id": "S-89dd10c16b4f1318",
        "url": "https://defence-industry.eu/danish-armed-forces-receive-final-leopard-2a7-tank-from-kmw/",
        "content_sha256": "40b747d73c50a9e5d7dedff0af2908418ed9e8588fed43c1fd8d5545b21fa0d9",
        "text_sha256": "3c6285830dbed2506c5fa62a943c7001482ecfdefa2343275d666e38ae593289",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8a06882d2a6a1929",
      "claim_ids": [
        "P-SB-020",
        "P-SB-022"
      ],
      "note": "esut.de 15.05.2026 gelesen (Absätze 1-14).",
      "snapshot": {
        "source_id": "S-8a06882d2a6a1929",
        "url": "https://esut.de/2026/05/meldungen/70815/die-british-army-erhaelt-72-radhaubitzen-rch-155/",
        "content_sha256": "a59bc3d38aba4006a1ec0e55d5d65151ed2d24c6fe896bb57eba0edf94cb9e31",
        "text_sha256": "b0c6da71c5c52d309af2d92ad99b6d91bd1806b06978973a974763a38562af73",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8a42e4d1ad6e2219",
      "claim_ids": [
        "P-01",
        "P-SA-001",
        "P-SA-005"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-8a42e4d1ad6e2219",
        "url": "https://knds.com/en/products/systems/leopard/leopard-2-a7",
        "content_sha256": "fa94c52386a77cada74b2a69f23743fc51a6e016899b1a291cdc0fe61fa4632c",
        "text_sha256": "c2fd99c0ebaa4a6d163fa07f69ba543f4e77cf876d5d314bf843dc6adac6212c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-8d5522a067055b85",
      "claim_ids": [
        "P-SA-047"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-8d5522a067055b85",
        "url": "https://armyrecognition.com/news/army-news/2026/french-army-fields-first-30-serval-armoured-personnel-carriers-for-high-intensity-warfare",
        "content_sha256": "5015889b7951e3101060c1f391cd755e3773559d0d8d58b6bbb6dcaaf226f0cc",
        "text_sha256": "b0a14f72ef55c42df11ce397af99b7d6d9e91c3ebd1299b624937a0c94c3f81f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-92d4e0a75a36b0f2",
      "claim_ids": [
        "P-SB-062"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung (22.06.2023) Zeilen 13-27.",
      "snapshot": {
        "source_id": "S-92d4e0a75a36b0f2",
        "url": "https://knds.com/press-releases/the-new-nexter-turret-a-knds-company-takes-off-with-the-upgraded-tiger",
        "content_sha256": "443ff6cba7980f3ba627fe39e6e3fe0ea9abb22b381ffcf9d936dba7cb7de134",
        "text_sha256": "d291e2cc424b5178632de8310c927e60044972594ebd1d3f71c54c39b6c02698",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-937ae61f03cd1731",
      "claim_ids": [
        "P-SC-025",
        "P-SC-026"
      ],
      "note": "Euromaidan Press 17.06.2025 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-937ae61f03cd1731",
        "url": "https://euromaidanpress.com/2025/06/17/ukraine-deploys-new-french-mv-25-oskar-drone-in-battlefield-use/",
        "content_sha256": "4a37d7569e9c431f4ed9ba8cd64156981f82ebecf436cf1ee0fdbbabe50f4b9c",
        "text_sha256": "483b053b15df6c3dce9d5ad24f0af2f53a86f3d2650be6a5e0a16b622707eec3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-94e524ffa416c9c1",
      "claim_ids": [
        "P-SA-049"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-94e524ffa416c9c1",
        "url": "https://knds.com/en/products/systems/vbci-mk2",
        "content_sha256": "3643b826df51e9fd64c399eabae3c9db4ab632c81eb1bda0e156e35f8dd41ac2",
        "text_sha256": "fc37025331a010bc6c30bde88c1c22393f4887afb1b6aa4023ac71609875dd31",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-985a5fe13a4cd562",
      "claim_ids": [
        "P-SB-019"
      ],
      "note": "KNDS-Pressemitteilung München 14.05.2026 gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-985a5fe13a4cd562",
        "url": "https://knds.com/en/press-releases/british-government-orders-latest-generation-artillery-system-from-knds",
        "content_sha256": "2e446fe68a6f80692eb8abe166d4789af7b031407a67ea593847a29b0855e2a3",
        "text_sha256": "3f54bb38c237a64476a4b406ce6c8a0655916c44ca4dcc6d174fdabc07604111",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-98f07af64f55666e",
      "claim_ids": [
        "P-SC-023"
      ],
      "note": "The Defense Post 16.10.2026 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-98f07af64f55666e",
        "url": "https://thedefensepost.com/2026/10/16/france-mx10-damocles-knds/",
        "content_sha256": "5c9a44d866755fe675397d6b2957611ee4421bcdeb610cc90e217e7df9220499",
        "text_sha256": "c9c91a5c156ba0d249bdc4454796f6b9eb59f02601a64b5d3ac049bc161a3c4f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-990434c1b62f333f",
      "claim_ids": [
        "P-SC-028"
      ],
      "note": "Gelesen: cache read, KNDS MV-100 VELOCE Produktseite Zeilen 15-46.",
      "snapshot": {
        "source_id": "S-990434c1b62f333f",
        "url": "https://knds.com/en/products/ammunition/mv-100-veloce",
        "content_sha256": "8cb0b9efbfbcac07ff7dc9f2ebef1cfafa2ecd410f33cb53319e87d68b93f5f8",
        "text_sha256": "74cc3341b84ecb1d26457f5cfdb37260e7d877c519cee65c79157a8f89fec67a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-991d4220bb3c40c6",
      "claim_ids": [
        "P-SA-064"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-991d4220bb3c40c6",
        "url": "https://warwheels.net/GFF4index.html",
        "content_sha256": "9ceb1ab50572b06ffd4eba8af105a4d3614215a1aa8cfba2b0f7c117a2fc0d42",
        "text_sha256": "cbe58bdbd81c38a65170ce366da009d5ecda70995a7860c4d27c776561d0ab86",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser. Encoding replacement detected; inspect original."
      }
    },
    {
      "source_id": "S-9a324c1b2ff6ef2e",
      "claim_ids": [
        "P-SA-024"
      ],
      "note": "Bundeswehr-Artikel 15.06.2023: Cache-Text unlesbar (gzip); Originalbytes selbst per gzip dekodiert und gelesen (Absätze 1-9).",
      "snapshot": {
        "source_id": "S-9a324c1b2ff6ef2e",
        "url": "https://www.bundeswehr.de/de/organisation/heer/aktuelles/bewaehrungsprobe-fuer-den-schuetzenpanzer-puma-5635552",
        "content_sha256": "c729c6992467b272c05b0fc6a2b9acaf5b89edadb721ea338028121e57f1dd8b",
        "text_sha256": "8bf5c51f509fa9abc3b7fe66ec0e39ce6349ce71241a6c6343131300c927e00e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser. Encoding replacement detected; inspect original."
      }
    },
    {
      "source_id": "S-9a994f8cc65fad0b",
      "claim_ids": [
        "P-SA-007"
      ],
      "note": "Gelesen: cache read, EDR-Wiedergabe der KMW-Mitteilung (München, 29.10.2019; EDR 30.10.2019) Zeilen 38-56 vollständig.",
      "snapshot": {
        "source_id": "S-9a994f8cc65fad0b",
        "url": "https://www.edrmagazine.eu/denmark-and-germany-receive-the-latest-versions-of-the-leopard-2",
        "content_sha256": "a7440047295f7461dd6916b18ba8d7f23d6a839f40b12752281516d67caa634c",
        "text_sha256": "0ae1e6794b5b0f009d70c4628c5e55f43054057ffb3fabbb5134eb3b24a2ba57",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-9ce97642693d7c16",
      "claim_ids": [
        "P-SA-034"
      ],
      "note": "Gelesen: cache read, KNDS-GRIFFON-Produktseite Zeilen 16-73.",
      "snapshot": {
        "source_id": "S-9ce97642693d7c16",
        "url": "https://knds.com/en/products/systems/griffon",
        "content_sha256": "172522b711b62dbb60d12a282750bb4eea09b21af13c40e7ac9178c28c504771",
        "text_sha256": "8f2a45e527a14cf385d83ff48d4ef7d0db7001d9e475799f7ea9a635d49412c4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a2e2089920633f48",
      "claim_ids": [
        "P-SA-032"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-a2e2089920633f48",
        "url": "https://www.produktion.de/ruestung-aerospace/boxer-rct-30-ist-der-neue-schuetzenpanzer-schakal-fuer-die-bundeswehr/2131353",
        "content_sha256": "8f308ac62140983dc677639270cc029fcb871def7b5e3f99dc43571f8f1009c1",
        "text_sha256": "256a96b1258e8516da2edd561988cbe6ce626235587076be3207e5b09f5a2c5c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a320eae326a26335",
      "claim_ids": [
        "P-SA-003"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-a320eae326a26335",
        "url": "https://euro-sd.com/2024/01/major-news/35902/leopard-2a7hu-mbts-handed-over/",
        "content_sha256": "6ae3de5bb79578be5fe0e7fc92a642e4246a4481f12f8840849d26ffbfb63317",
        "text_sha256": "25fb6a57d44eece484b4fb4e84d4d8ef51a382bbac11af1bb8326b9465b602cf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a43a1af456113f5d",
      "claim_ids": [
        "P-SB-060"
      ],
      "note": "Defence ReDEFiNED 10.04.2024 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-a43a1af456113f5d",
        "url": "https://defenceredefined.com.cy/optio-x20-knds-armed-multi-mission-unmanned-ground-vehicle",
        "content_sha256": "13ffaa40c51a0e078ff47325c2157d028ed84890232b0964932ef032b13c1d78",
        "text_sha256": "cd44e3d712f5ab4616fcd788397eb3faecada2d4c257824a36b6cae4cffc7c78",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a5a797cf3b776ceb",
      "claim_ids": [
        "P-SD-010"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-a5a797cf3b776ceb",
        "url": "https://knds.co.uk/?p=36",
        "content_sha256": "2828009fd038f4b8cffa51821688d7723e69a376f1bd82de1c10a5b29ab5cac6",
        "text_sha256": "fa3f4960875fe3ca43fb8d01d490fd68ef22b719bf4de143196f85b1ac641622",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a700649482832648",
      "claim_ids": [
        "P-SD-050"
      ],
      "note": "KNDS-CBRN-Unterseite gelesen (Einleitung, Produktliste).",
      "snapshot": {
        "source_id": "S-a700649482832648",
        "url": "https://knds.com/en/subsidiaries/knds-cbrn",
        "content_sha256": "778a88d6117f5abc014cc598a8d0db4f5edcc8bbd0b899f2844c4c22ca67b7fe",
        "text_sha256": "f5247fff0e1a30e0a18fea978b98534f792d00f631df9ef209f14c6b5400be4c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a757e9aba1762b82",
      "claim_ids": [
        "P-SD-020"
      ],
      "note": "Army Technology MGB-Projektprofil (undatiert) gelesen (Absätze Übersicht und Contracts).",
      "snapshot": {
        "source_id": "S-a757e9aba1762b82",
        "url": "https://www.army-technology.com/projects/medium-girder-bridge-united-kingdom/",
        "content_sha256": "ddf6b462dc52e05035db5316a881a3ecedd25219926d50d7da748735e4ae9275",
        "text_sha256": "d6a5124c049fdcfe22287b274ab9c8de8b3b721a440fdce4c2df1d0a8cc4dd16",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a956241b6fee9a37",
      "claim_ids": [
        "P-SA-061"
      ],
      "note": "Shephard 10.11.2021 gelesen (Absätze 1-9; Premium-Teaser, Artikelteil vollständig sichtbar).",
      "snapshot": {
        "source_id": "S-a956241b6fee9a37",
        "url": "https://www.shephardmedia.com/news/landwarfareintl/germany-addresses-marder-and-mungo-maintenance-req/",
        "content_sha256": "30efffcbd670857c49d8594428f9f6002d37f4511d636d887d13a4ba3ed198d0",
        "text_sha256": "601d022f4414ba31d7133f9a1a28534eee713d332f46e75edb42d2f25866b7d7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-a99fd782e733a804",
      "claim_ids": [
        "P-SA-060"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-a99fd782e733a804",
        "url": "https://knds.com/en/products/systems/mungo",
        "content_sha256": "4f42489312ca472bf658c208392ae55d4881facc6b7120371f31f24256a3e81d",
        "text_sha256": "448330f3eb15a8a1367ffc46d942e024d6bd6b74d6cfa62142b92c4484980ea4",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aa11d141db260364",
      "claim_ids": [
        "P-SD-014"
      ],
      "note": "Gelesen: cache read, Defense-Post-Artikel vom 06.02.2024 (Zeilen 7-23) vollständig.",
      "snapshot": {
        "source_id": "S-aa11d141db260364",
        "url": "https://thedefensepost.com/2024/02/06/uk-tactical-support-bridges-knds/amp/",
        "content_sha256": "b7ba310b974e82927bd00f1913973632f7c711a3029a221cc6c39e97147a218f",
        "text_sha256": "09110da25ebbb2b7afd25b65045205dbb64f3ec9b8de2fe17ac06ed84cb978ee",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-aadcb3da199c3d17",
      "claim_ids": [
        "P-SC-001"
      ],
      "note": "Gelesen: cache read, KNDS-Produktseite '155mm Ammunition' Zeilen 7-35.",
      "snapshot": {
        "source_id": "S-aadcb3da199c3d17",
        "url": "https://knds.com/en/products/ammunition/155mm-ammunition",
        "content_sha256": "16be739981fff1647a8a9f3e9047177ebaf4f37efc8753ed499ba517f3209b10",
        "text_sha256": "c27006e3c5ab030b6f1ad9806497e82d2566db7f517f614a0efa4cb4565142e6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ad189a4b9c19e1c2",
      "claim_ids": [
        "P-SA-039"
      ],
      "note": "KNDS-JAGUAR-Produktseite gelesen (Einleitung, Faktenabschnitt).",
      "snapshot": {
        "source_id": "S-ad189a4b9c19e1c2",
        "url": "https://knds.com/en/products/systems/jaguar",
        "content_sha256": "c3baff91df1e945efc78f9e413b44bb1bab8df1f578bfb4361c41fd7d6b4c835",
        "text_sha256": "23a57ad3ddaddc12a8b48ab8d714eabf7c022a79940605e8678e3eed99532f81",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-af49a45e847aebd4",
      "claim_ids": [
        "P-SA-053"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-af49a45e847aebd4",
        "url": "https://knds.com/en/products/systems/fennek",
        "content_sha256": "86b5d4ff8799e18e7e187776dc0f0056538a266434358c8d95843524db778cf9",
        "text_sha256": "78f1fd250b52507f5dd22292e80ebfcd6be1afc151e04feeb85c3d2d634cfea8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-af673b6817266e46",
      "claim_ids": [
        "P-07"
      ],
      "note": "Gelesen: cache read, KNDS-Produktseite RCH 155 Zeilen 14-81.",
      "snapshot": {
        "source_id": "S-af673b6817266e46",
        "url": "https://knds.com/en/products/systems/rch-155",
        "content_sha256": "2d2be821556e6c9277219061773035d7b0f39ff0621ba468f1246644fd7fa9e0",
        "text_sha256": "b501922467f360952d5ffee035279393bfbfa56ced1e2a9960a83e72ee462895",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b089d8c896987d3f",
      "claim_ids": [
        "P-SC-006"
      ],
      "note": "Gelesen: cache read, Artikeltext (polnisch, Live-Beitrag vom 18.06.2026) Zeilen 83-91 vollständig.",
      "snapshot": {
        "source_id": "S-b089d8c896987d3f",
        "url": "https://xyz.pl/?p=218688",
        "content_sha256": "dfab72ee80ef20688938929e18d11c6d6cce4ab24a7012e19a51a2a25694a290",
        "text_sha256": "9c18b29ec34532a43c4494b970824d855112c5dd4e37320b26a1f48fe934c64f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b1618e7ff9721cd4",
      "claim_ids": [
        "P-SD-041"
      ],
      "note": "Bundeswehr-Meldung 12.10.2026: Cache-Text unlesbar (gzip); Originalbytes der aktuellen Version (SHA-256 0894d53a…, stimmt mit Snapshot) selbst per gzip dekodiert und gelesen (Absätze 1-12). Eine ältere Cacheversion (1d76d492…) existiert; nicht verwendet.",
      "snapshot": {
        "source_id": "S-b1618e7ff9721cd4",
        "url": "https://www.bundeswehr.de/de/meldungen/digitalisierung-landbasierte-operationen/digitalisierung-zwischenbilanz-einsatzpruefung-6164064",
        "content_sha256": "0894d53a09fe0e108bd0a82b873e0e88d941576b3ed157cb42c801167167a1eb",
        "text_sha256": "e035359b562cfe05d2568dcac8f3d5d6542e0dfa349979e484856d29adf01ec9",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser. Encoding replacement detected; inspect original."
      }
    },
    {
      "source_id": "S-b30c05fe1b577a0f",
      "claim_ids": [
        "P-SA-057"
      ],
      "note": "Sicherheit & Verteidigung 19.12.2024 gelesen (Absätze 1-5).",
      "snapshot": {
        "source_id": "S-b30c05fe1b577a0f",
        "url": "https://suv.report/bundeswehr-erhaelt-65-weitere-dingo-2-a4-1/",
        "content_sha256": "3df2cde5108b9c38a47a191680fe736cb5aafad003d3f4cf8550a8d824aef5ea",
        "text_sha256": "8c106e8ce780e89bbd73617125caf1cfc121f7f41f64e7314a01892b137a8907",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b3d6ea0a4ecf3ff5",
      "claim_ids": [
        "P-SD-070"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-b3d6ea0a4ecf3ff5",
        "url": "https://canadiandefencereview.com/contract-awarded-to-knds-deutschland-gmbh-co-kg-knds-for-the-long-term-sustainment-of-the-leopard-2-family-of-vehicles/",
        "content_sha256": "bcd85083c5b42f408d1a32f1335135823ce19d963da08eb4dc59315d60e14b0c",
        "text_sha256": "0113304836cb4c6f29980e1cdd1887adeae5e45c566fe5fb8252f81a97dd0c0f",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b43dc0babc198b25",
      "claim_ids": [
        "P-SC-007"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-b43dc0babc198b25",
        "url": "https://knds.com/en/products/ammunition/155mm-ammunition/155mm-bonus",
        "content_sha256": "bf16274499e6f62df1293a65095bae4a80b7bc87505ed0562a7b8fa56ae8fb13",
        "text_sha256": "4198a13aa265b802eb337c95249eed777ec368870453d10b68c344e37333cb34",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b5d05a3c25aa13c6",
      "claim_ids": [
        "P-SC-030"
      ],
      "note": "Gelesen: cache read, SAE-Media-Group-Artikel zu EOS/Veloce 330 (Zeilen 45-63); undatiert, Ereignisse Juni 2025.",
      "snapshot": {
        "source_id": "S-b5d05a3c25aa13c6",
        "url": "https://smgconferences.com/editors-corner/5997-news--france-adopts-veloce-330-loitering-munition-to-enhance-precisionstrikes-against-armoured-targets",
        "content_sha256": "28802010019823798dd9631f9f1922b3b5a13c418512286595d170982c0ecbf8",
        "text_sha256": "7378faf0d411dca4ca9d9ccc73a2fcdc1b4df03d1ddc9d10bd9d7fb64d50efc7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b60dbc45fdcac0ac",
      "claim_ids": [
        "P-SC-023"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-b60dbc45fdcac0ac",
        "url": "https://asdnews.com/news/defense/2026/10/13/french-forces-order-more-mx10-damocles-loitering-munitions-knds-delair-consolidate-their-position-as-benchmark-field",
        "content_sha256": "b5ecb9161b5f1f113918b9b466f03fa12598e32c7ecd9fad7ba0e60f9c19b05b",
        "text_sha256": "a9d64c650503717e6461e253d6cd0ad3b9e9d3d5d014dadfb352e6c5dc8c05d0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b83a36907da809b2",
      "claim_ids": [
        "P-SB-006"
      ],
      "note": "Defence24 (polnisch) 22.05.2025 gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-b83a36907da809b2",
        "url": "https://defence24.pl/wojna-na-ukrainie-raport-specjalny-defence24/duze-wzmocnienie-ukrainskiej-artylerii-z-francji-cala-produkcja-nad-dniepr",
        "content_sha256": "9aafd311f16f87dfb4a161fab923d0cf450eae7fe49a1c7904cca48e6e2806f6",
        "text_sha256": "e38755796612445171c1c6e72240a207bbd156fba3c6d1d6cf3b21d3ed67477e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b87afeb6be3f399c",
      "claim_ids": [
        "P-SB-010",
        "P-SB-027"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-b87afeb6be3f399c",
        "url": "https://euro-sd.com/2025/01/major-news/42032/first-rch-155-for-ukraine/",
        "content_sha256": "92b77c7aa894005e79655d25867a9775ea276f9cdae9f01f8b264f9915804694",
        "text_sha256": "c1a44e38b162f8cd70e4c404d1d492f3b5ee251d7e76406170c362e1fcc003b7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b8f957ad1ccbc530",
      "claim_ids": [
        "P-SC-017"
      ],
      "note": "Gelesen: cache read, Army-Recognition-Artikel zu SHARD (Zeilen 242-255); undatiert, nennt Ankündigung 17.02.2026.",
      "snapshot": {
        "source_id": "S-b8f957ad1ccbc530",
        "url": "https://armyrecognition.com/news/army-news/2026/france-orders-shard-120mm-arrow-apfsds-to-replace-leclerc-tank-rounds-by-2030",
        "content_sha256": "319568862731e894111e566765972e54f3375da9184cb5327239c60bd727a24a",
        "text_sha256": "587c8c34f8ce3cafb448dfb81106974256f533b7b193f977e7f49adb01cf25bf",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b94028cc148d68b8",
      "claim_ids": [
        "P-SB-015"
      ],
      "note": "Business AM FR 22.07.2026 gelesen (Absätze 1-10).",
      "snapshot": {
        "source_id": "S-b94028cc148d68b8",
        "url": "https://fr.businessam.be/?p=266819",
        "content_sha256": "6564ce800a436703e690b8c34480c6b751dacdafbe4de50466efe5b37c3782a5",
        "text_sha256": "2d85e06a6b8964f5d5f9da72e2e3ac56243d60d44b8a2e26a515f4499f9f9435",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-b960b68760070182",
      "claim_ids": [
        "P-SC-011",
        "P-SC-012",
        "P-SC-013"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-b960b68760070182",
        "url": "https://knds.com/en/press-releases/the-french-procurement-agency-supports-the-development-of-the-katana-155mm-high-precision-ammunition",
        "content_sha256": "db35f3b746e8102d6c3175f733dc92553e5bfeebe2860cd56847c78489c7aff6",
        "text_sha256": "f4e454cfeeaa02cfb4e036b5ea777a12fc28ae38d10bf1cd20fb64bdc8ccb3e2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-bcc88003de5b9217",
      "claim_ids": [
        "P-SB-055"
      ],
      "note": "Gelesen: Cache-Textableitung ist unlesbar (Gzip-Bytes im Text, Hinweis 'Encoding replacement'); gespeicherte Originalbytes (source.bin, gzip, sha256 3c945092...) lokal dekomprimiert (python gzip) und HTML-Text extrahiert; BMVg-Meldung Abschnitt 'Kauf weiterer FLW 100' (Zeilen 77, 104-107 der dekodierten Fassung) gelesen. Dokumentiert, nicht im Cache gespeichert.",
      "snapshot": {
        "source_id": "S-bcc88003de5b9217",
        "url": "https://www.bmvg.de/de/aktuelles/beschaffung-moersersystem-idz-ausstattungen-tawan-richtfunknetz-5882320",
        "content_sha256": "3c94509287878cb865862272073ccfbfbd796a742f36771d0eb8fc6d7782554d",
        "text_sha256": "510809a0a0fa177b3954b31c4db9672e4ce196e771c6ad2a92951f58b8c815fc",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser. Encoding replacement detected; inspect original."
      }
    },
    {
      "source_id": "S-be3e133eccbcde11",
      "claim_ids": [
        "P-SA-058"
      ],
      "note": "Frei sichtbarer Artikelteil (Abs. 2-3) über source-cache.py read gelesen; weitere Inhalte hinter Bezahlschranke (Shephard Defence Insight) nicht lesbar.",
      "snapshot": {
        "source_id": "S-be3e133eccbcde11",
        "url": "https://www.shephardmedia.com/news/landwarfareintl/german-army-to-receive-new-generation-dingo-3s-this-year/",
        "content_sha256": "727cb143201825794f39a5acba198f969f13c4d5dffcf5a883409ed6e690a390",
        "text_sha256": "1e57f4d0d8f3ca3ed154380067b51d00b8d6ed9e962088cbf59c9ab759f869c5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-bec206fc40beea51",
      "claim_ids": [
        "P-SA-040"
      ],
      "note": "Gelesen: cache read, Ministère-des-Armées-Meldung (Besuch Roanne, 19.02.2022) Zeilen 71-91.",
      "snapshot": {
        "source_id": "S-bec206fc40beea51",
        "url": "https://www.defense.gouv.fr/actualites/commande-18-milliard-deuros-canons-vehicules-nouvelle-generation",
        "content_sha256": "1e062374a390bba51d8bdfc69e14650e45db65db1d90bf052248f7c737f3371d",
        "text_sha256": "c7531789f0f92058001046ec9272ac0501924e73b5d910cec2e6eac420801ac5",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c35f56a0525f290b",
      "claim_ids": [
        "P-SA-023"
      ],
      "note": "Extrakttext aus source-cache.py read war durch gzip-Bytes beschädigt; Original aus den gespeicherten Originalbytes (source.bin, gzip) dekodiert und Artikeltext gelesen.",
      "snapshot": {
        "source_id": "S-c35f56a0525f290b",
        "url": "https://www.bundeswehr.de/de/organisation/heer/aktuelles/neuer-puma-revier-5820268",
        "content_sha256": "dc2325b23fd8bd84ebc679cb720656d44a4a669b1f3c2cd28666277116af9ff9",
        "text_sha256": "da6964079cd37ff5c05a96f076bdedbd56a18b3b3214c31766bf38d4503e5408",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser. Encoding replacement detected; inspect original."
      }
    },
    {
      "source_id": "S-c414879d32b9e9d1",
      "claim_ids": [
        "P-SB-001",
        "P-SB-011",
        "P-SB-025"
      ],
      "note": "KNDS-Pressemitteilung 18.06.2024 gelesen (Absätze 1-9).",
      "snapshot": {
        "source_id": "S-c414879d32b9e9d1",
        "url": "https://knds.com/en/press-releases/knds-offers-the-complete-range-of-proven-artillery-systems",
        "content_sha256": "6c371ebc5e8f45cbd489a60813eb244d7de444d40953e84dd7581cf346d6a3d3",
        "text_sha256": "14628f8e4dc42c121b0d4fa022b5cd9eb09bb40d93f458f8682cb9b58e95164d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c448e86fde84d62e",
      "claim_ids": [
        "P-SD-004"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-c448e86fde84d62e",
        "url": "https://knds.com/en/press-releases/denmark-procures-knds-leguan-bridge-layers-based-on-wheeled-vehicles",
        "content_sha256": "642b745985ca53e3133ee32a87236a224166370578d2fd2c3dc63c2a1c8b4dca",
        "text_sha256": "8f5c0d3419913206f08199306ae82e3f7c70c0d920fe005845ebdfeae2d29c98",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c48aed5f6aa1dc24",
      "claim_ids": [
        "P-SA-045"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-c48aed5f6aa1dc24",
        "url": "https://defence-blog.com/french-military-receives-135th-serval-armored-vehicle/",
        "content_sha256": "4722ed75f022f3088f50fa258a124aeed9b38c2846020fa49cd70870a21a7338",
        "text_sha256": "9c7bd9183c615ec1db4492b394a148394118edb4d17f2dedc7de6c4a6721c8ba",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-c94303e94d1e46f1",
      "claim_ids": [
        "P-SC-047"
      ],
      "note": "Gelesen: cache read, KNDS-CENTURIO-Produktseite Zeilen 17-70.",
      "snapshot": {
        "source_id": "S-c94303e94d1e46f1",
        "url": "https://knds.com/products/systems/centurio",
        "content_sha256": "8d7331367502a13480f15da75f3c5120361984a297681bd39a1f5775d1f24018",
        "text_sha256": "06b0d4ff965889ae61ddcaafcae520302f1a687a84340ae19a277d9e70af3e87",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cacbe83eed4a50bb",
      "claim_ids": [
        "P-SC-010"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-cacbe83eed4a50bb",
        "url": "https://euro-sd.com/2021/01/articles/exclusive/20790/katana-guided-artillery-tests/",
        "content_sha256": "f93868d07363f24c8139e20d8a0457e16391723e7f28d908aeeac4c2b24e5a10",
        "text_sha256": "6a81f6801882b395b4fe2db4ea7448a044d5698345959c752a5f82fc8d1fc98b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cb77fab4ccd5db0b",
      "claim_ids": [
        "P-SA-036"
      ],
      "note": "Gelesen: cache read, Army-Recognition-Artikel zu ORION 26 (Zeilen 242-249); Datum aus Text 9.2.2026.",
      "snapshot": {
        "source_id": "S-cb77fab4ccd5db0b",
        "url": "https://armyrecognition.com/news/army-news/2026/france-conducts-first-amphibious-landing-of-griffon-6x6-armored-vehicle-during-orion-26-exercise",
        "content_sha256": "9ac960a420699a1773061c4f8c59b5ad6c4a05ef9f1f642ae0804a553c2dd158",
        "text_sha256": "d1d2e2f4e418329be4c5a25fc6487d33b75f0141bdbdb105b62697c7d2bb6624",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cc65bc16b7e1415b",
      "claim_ids": [
        "P-SD-012"
      ],
      "note": "ADS-Mitgliedsmeldung (WFEL) 21.09.2017 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-cc65bc16b7e1415b",
        "url": "https://www.adsgroup.org.uk/knowledge/industry-member-news/wfel-to-supply-four-more-dry-support-bridges-to-us-army/",
        "content_sha256": "51695dd54a9cbc677d5feb34b6159df3a11db54c7d8db9226c9a6caed49c3e5f",
        "text_sha256": "e6eb05eb608259d1feba7e99ba0a20f7e7dd60835807919fc64bba933825e6e0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cd4d8a27a37624e4",
      "claim_ids": [
        "P-SA-010",
        "P-SA-011",
        "P-SB-026"
      ],
      "note": "KNDS-Pressemitteilung München 19.11.2025 gelesen (Absätze 1-10).",
      "snapshot": {
        "source_id": "S-cd4d8a27a37624e4",
        "url": "https://knds.com/en/press-releases/roll-out-of-the-knds-leopard-2-a8-and-pz-h-2000-systems",
        "content_sha256": "639c9ca73bbccec067ded3df6c31f9fc896523d70af51158ba3ae568cf0f98dd",
        "text_sha256": "4f99378967c2c3740877d32ceea0acabee2670f178ad9b8338ecc75a78273977",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cdb071d12fc238e7",
      "claim_ids": [
        "P-08"
      ],
      "note": "KNDS-PzH-2000-Seite gelesen (Kennwerte, Beschreibung).",
      "snapshot": {
        "source_id": "S-cdb071d12fc238e7",
        "url": "https://knds.com/en/products/systems/pzh-2000",
        "content_sha256": "1bf6a4955d5b3a084ee3bca0921b4b1d79ad54b64c5d2677c8fe6d0867c4412c",
        "text_sha256": "bbe8600c61c3eaed375bf935ca8f4218f6fb7f5d50009b8ca10b74d0f43174b7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ce07e1ada13e6f22",
      "claim_ids": [
        "P-SD-030"
      ],
      "note": "KNDS-Bridges-Übersicht gelesen (Abschnitt „Bridge systems from KNDS are in use worldwide“, Produktliste).",
      "snapshot": {
        "source_id": "S-ce07e1ada13e6f22",
        "url": "https://knds.com/en/products/systems/bridges",
        "content_sha256": "b4b8cedc5040394747c92c0016509cc869e8e7b53fb1871b4eaf07a9c773cffd",
        "text_sha256": "5db150bf9ffaac74369ca282f427291f1282e9f43304126d6b8ab62795472d3d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ce3e22104f8c89b5",
      "claim_ids": [
        "P-13",
        "P-14"
      ],
      "note": "KNDS-Munitionsübersicht gelesen (Abschnitte Artillery, Tank, Naval, Medium caliber, MATARIS).",
      "snapshot": {
        "source_id": "S-ce3e22104f8c89b5",
        "url": "https://knds.com/en/products/ammunition",
        "content_sha256": "016a10bc700266181c04fca0125d815ea5678cbf45dd8b0865e8b2e0d73a5910",
        "text_sha256": "8c25b1799da5546531b26200ffaf1b2d34555634f7409fde75b9c0bc8c74bd50",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-cf970a56bf82bfee",
      "claim_ids": [
        "P-SC-039",
        "P-SC-045"
      ],
      "note": "Gelesen: cache read, EDR-Artikel vom 19.10.2021 (Zeilen 38-65) vollständig inkl. Schlussabsatz (Z. 62-65).",
      "snapshot": {
        "source_id": "S-cf970a56bf82bfee",
        "url": "https://www.edrmagazine.eu/nexter-unveils-the-final-configuration-of-its-nerva-xx-medium-size-multi-mission-ugv",
        "content_sha256": "d26aca8e1a3234de17b5030b60fd1009c04443fb71b6d841054d4f4da63c83f6",
        "text_sha256": "08cc24303ffa0028612a1b7370ee82ba8f2fcbadffb6f498fb56cfe08e34f0d0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d0a13e4be327c0ab",
      "claim_ids": [
        "P-SA-014"
      ],
      "note": "Gelesen: cache read, dpa-Meldung via Yahoo (19.11.2025) Zeilen 43-58.",
      "snapshot": {
        "source_id": "S-d0a13e4be327c0ab",
        "url": "https://www.yahoo.com/news/articles/germanys-bundeswehr-receive-first-generation-073122144.html",
        "content_sha256": "d19d898056eb6f7796b906767a2018f221d163cd7cb08a628901dd9a8299ea5b",
        "text_sha256": "386f9d40012ebf2a2d9df43a6483962d0cec28f9033f2e0f5afc32867d5e5980",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d34ec41e13214dfc",
      "claim_ids": [
        "P-SA-030"
      ],
      "note": "Gelesen: cache read, KNDS/KMW-Pressemitteilung Eurosatory 2022 (13.06.2022) Zeilen 13-33.",
      "snapshot": {
        "source_id": "S-d34ec41e13214dfc",
        "url": "https://knds.com/en/press-releases/eurosatory-2022-kmw-presents-a-world-debut",
        "content_sha256": "feb3429ac05dd78d04e05ba5656b5c407e1fe0d7de675fad82b294f168bbfff5",
        "text_sha256": "c53361879ed930bdb2f65c2c98de2997b1f7ec42e796964b9e11b6654a6d8787",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d3d43cc97cc81389",
      "claim_ids": [
        "P-SB-053"
      ],
      "note": "Leinetal24 (ntv) 22.09.2025 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-d3d43cc97cc81389",
        "url": "https://www.leinetal24.de/wirtschaft/neue-panzer-produktion-geparden-weiden-auf-ukrainischem-grasland-zr-93935393.html",
        "content_sha256": "abb673f7dea05c01021d00cb8cb9e1e95c96c311336140171945914f447d0fb2",
        "text_sha256": "e568bbd9b91d88a50d1f5186646f8b67ad2c0d7db7b4cb4cd7f57301f7f07210",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d47b4031096d3c20",
      "claim_ids": [
        "P-SB-043",
        "P-SB-044"
      ],
      "note": "KNDS-Pressemitteilung RAPIDFire Land (undatiert) gelesen (Absätze 1-9).",
      "snapshot": {
        "source_id": "S-d47b4031096d3c20",
        "url": "https://knds.com/en/press-releases/thales-and-knds-france-unveil-rapid-fire-land-a-land-based-variant-of-the-40-mm-rapid-fire-naval-defence-system",
        "content_sha256": "2581a38b6cd93f982722db67803a1d4562687265b540ec179b1d4a8cafc82a7c",
        "text_sha256": "459a9cf8e17bd1ce6ab61d1cf5c5a45ed547c1fafcce723189bd9721886cb6ff",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d7d7587226163f27",
      "claim_ids": [
        "P-SB-021",
        "P-SB-038"
      ],
      "note": "Gelesen: cache read, KNDS-Pressemitteilung (München/Bern, 08.06.2026) Zeilen 11-26.",
      "snapshot": {
        "source_id": "S-d7d7587226163f27",
        "url": "https://knds.com/en/press-releases/switzerland-procures-state-of-the-art-artillery-system-from-knds",
        "content_sha256": "80f709be8690df7995f053156e3cfd095abe70833d5ca9c38a8558d7a1c7773c",
        "text_sha256": "32f96fbbb222c079c539d1be5c4f03d77d66ebf00708cc8cc1ec5a8283d027a1",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d7f97d9c6b065b7f",
      "claim_ids": [
        "P-SA-014"
      ],
      "note": "Defense News 20.11.2025 gelesen (Absätze 1-12).",
      "snapshot": {
        "source_id": "S-d7f97d9c6b065b7f",
        "url": "https://www.defensenews.com/global/europe/2025/11/20/knds-unveils-the-leopard-2a8-first-new-battle-tank-build-since-1992/",
        "content_sha256": "30f37ac005f459a171279a85e4fedc35f6c1af5ece907865bcb6cdf1b6e6922c",
        "text_sha256": "d2e9fbbd91b8e6c2a2d513cf8f36532a236ba536d82d825469f0cdb8e8cbc908",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-d93ed235185f04c5",
      "claim_ids": [
        "P-20"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-d93ed235185f04c5",
        "url": "https://knds.com/de/produkte/training-und-simulation",
        "content_sha256": "11cd7d587cf617c12f96ae6c5b39d2179859bfa3dfd068251aeaa897d31de890",
        "text_sha256": "c4a0b03af83c304abce18b310f809b7e05403b37ad7219d64a528c329aa05512",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-da8fcddb92a3fdcb",
      "claim_ids": [
        "P-SA-002"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-da8fcddb92a3fdcb",
        "url": "https://knds.com/en/press-releases/knds-hands-over-the-last-of-44-leopard-2-a7-hu-main-battle-tanks-to-hungary",
        "content_sha256": "7a95811a5b45f2d384fe4e8a5434b27efda899b25ec9752b8985266ed89f9c20",
        "text_sha256": "3c5f04ac144d31b019aa9bdf534bcb2716fc4e1162e4022d7c0c46cd15e277e3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-df209e8e3de10b23",
      "claim_ids": [
        "P-SD-043"
      ],
      "note": "KNDS-Seite Command and weapon engagement systems gelesen (Abschnitt iC2).",
      "snapshot": {
        "source_id": "S-df209e8e3de10b23",
        "url": "https://knds.com/en/products/equipment/command-and-weapon-engagement-systems",
        "content_sha256": "42668ea4fbf2b6b08d6af6203fcdf7167799ecf7fc1bb2652bf37f42a9496649",
        "text_sha256": "c2700367a9eb9ee083573dd486f74beb80565caff6ca8e87ea735211c29480c8",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-df95121b822ba92f",
      "claim_ids": [
        "P-SC-050"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-df95121b822ba92f",
        "url": "https://knds.com/en/media-days/unmanned-systems",
        "content_sha256": "edb62cfb8c14faf338eca93b17b9897430258cb40bd461e3f5bcc90203fd8c58",
        "text_sha256": "20d643129f94dae79032cd0ff91870269fe18071564a95de2cd1aaac2a2dd9c7",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e21b199c143a41de",
      "claim_ids": [
        "P-10",
        "P-SB-048"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-e21b199c143a41de",
        "url": "https://knds.com/en/products/systems/rapid-fire-land",
        "content_sha256": "f0385c3530a94c73caa1e45afc599760fb856fec2c2076eabd1dedc5aa301faa",
        "text_sha256": "d2023b11196339fb5b72fe6e718f83162a9f3ed0a89a85bd83caf9d048ec5633",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e21f141dc8121dce",
      "claim_ids": [
        "P-SB-033"
      ],
      "note": "Army Recognition (2022, ohne Metadatum) gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-e21f141dc8121dce",
        "url": "https://www.armyrecognition.com/focus-analysis-conflicts/army/conflicts-in-the-world/russia-ukraine-war-2022/m270-mlrs-mars-ii-from-germany-has-arrived-in-ukraine",
        "content_sha256": "42e37c307d3d5dbddfd495a3b64f57ff019ad1d2884e640f1d28986328e46eff",
        "text_sha256": "d10e51e6734dc3765cc76cfab3a4c401403c3122da70172cde0944e174810e77",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e39570202194e479",
      "claim_ids": [
        "P-SB-040"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-e39570202194e479",
        "url": "https://stratpost.com/knds-and-leonardo-to-jointly-develop-mobile-artillery/",
        "content_sha256": "ec19b340d30397c94ae43c22f61fe3f5b8fcd5139cc03c11298ad7af24f8148b",
        "text_sha256": "a92d8a4a2091bb875aaf3d051e64e6c4f8b8233040382312823d999cef5bcb0e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e5b36faedd6ac2e1",
      "claim_ids": [
        "P-SD-071"
      ],
      "note": "Gelesen: cache read, New-Voice-of-Ukraine-Artikel vom 21.01.2025 (Zeilen 9-19).",
      "snapshot": {
        "source_id": "S-e5b36faedd6ac2e1",
        "url": "https://english.nv.ua/nation/germany-s-knds-opens-joint-venture-in-ukraine-50483525.html",
        "content_sha256": "9209301a6af5d8dfeb4e68366ba47e37ff96e5e82b799fc7ab81334e617e443d",
        "text_sha256": "91fa90617cd30259105326a0f3d17f9ebc6dda376159a59e3cf5cfef669b3ed6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e65e191e1089c866",
      "claim_ids": [
        "P-SA-052"
      ],
      "note": "Gelesen: cache read, EDR-Artikel vom 20.01.2026 (Zeilen 38-60).",
      "snapshot": {
        "source_id": "S-e65e191e1089c866",
        "url": "https://www.edrmagazine.eu/dimdex-2026-knds-france-showcases-vbci-mkii-loitering-munitions-and-a-bespoke-counter%e2%80%91drone-shield-for-qatari-forces",
        "content_sha256": "3c1ce5a6e23ba751f09ba88820792bd0243162912f82c578df48612c167fd7ea",
        "text_sha256": "ef1f67b0b976daa26fad5e8c4992290570bbfcbbb987ecdcff4f00a7045b298d",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e72bc468a97fc7d0",
      "claim_ids": [
        "P-SC-016",
        "P-SC-017"
      ],
      "note": "Calibre Defence 19.02.2026 gelesen (Absätze 1-10 und Meilensteinliste).",
      "snapshot": {
        "source_id": "S-e72bc468a97fc7d0",
        "url": "https://www.calibredefence.co.uk/france-orders-shard-apfsds-enhancing-its-armoured-firepower/",
        "content_sha256": "383830cec4247126b7262d2f81441cbf1acb68ac4cff1abd137b0b8defa3a26a",
        "text_sha256": "72b3abdb2550c5be69e23ebaddf05c6389c36dc993f37791bfd73a13cdf98e71",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e903df08d36255bb",
      "claim_ids": [
        "P-SD-001"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-e903df08d36255bb",
        "url": "https://esut.de/2019/12/meldungen/ruestung2/17319/gefechtsfeldbruecken-leguan-an-die-niederlande-uebergeben/",
        "content_sha256": "ce93a365c181d8d51c22e610a6b73967a0ec89ad6fe7e23bd45349a762d6d868",
        "text_sha256": "4c9bef198a05b132d2bbf57217b5da6e144782ff34eb96dfdc8e1ccd9fdf19b3",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-e92862a57ce9ebf6",
      "claim_ids": [
        "P-SB-054"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-e92862a57ce9ebf6",
        "url": "https://global.espreso.tv/russia-ukraine-war-ukrainian-gepard-with-upgraded-radar-will-mark-start-of-joint-projects-with-knds-deutschlandwhy-this-project-was-chosen",
        "content_sha256": "6613d5165ac73fdaca80ad4d608d1be080327dfff31301c1430283bad52c66e2",
        "text_sha256": "a91e5100db31791817675d391a261c08bca12cc312ff4e74b3caf240c7988340",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ea11e6d3f5209174",
      "claim_ids": [
        "P-SD-005"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-ea11e6d3f5209174",
        "url": "https://www.edrmagazine.eu/belgium-selects-leguan-bridge-layer-from-knds",
        "content_sha256": "53a52dd8334ae5bd6be8eae5ccffdac912f4c83451a615b305f7f702560fde57",
        "text_sha256": "4998487efc4029d390c82b469205323667b27adfcf6266819da3a5b551ac0d43",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-eacce69e02fa08ce",
      "claim_ids": [
        "P-SC-044"
      ],
      "note": "KNDS NERVA-XX-Produktseite gelesen (Absätze 1-4).",
      "snapshot": {
        "source_id": "S-eacce69e02fa08ce",
        "url": "https://knds.com/en/products/systems/nerva-xx",
        "content_sha256": "84fdf3af1433bd86514df38e8f28e8f1e2faa1ca3c41e827a0148dd22b0cc852",
        "text_sha256": "6c1dbdde9d9388e3b22fdaafbcff937c3d6c0a909b66376dd198014326f7e696",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-eb4ccecc405a5467",
      "claim_ids": [
        "P-SC-038",
        "P-SC-046"
      ],
      "note": "Gelesen: cache read, Defense-Mirror-Artikel vom 17.01.2020 (Zeilen 70-80) vollständig.",
      "snapshot": {
        "source_id": "S-eb4ccecc405a5467",
        "url": "https://defensemirror.com/news/26183/French_Army_Receives_NERVA_LG_Micro_Surveillance_Robots_from_NEXTER",
        "content_sha256": "3d5558573a8581e68647a2bed19c9b02f67a7a40e2ef319849df468d0be479a2",
        "text_sha256": "625055fb56a3bb84b666b552ab36d73429aad750fca6e29d225d56d881db7f26",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-eb5571e8d8324a23",
      "claim_ids": [
        "P-06"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-eb5571e8d8324a23",
        "url": "https://knds.com/en/products/systems/caesar-6x6",
        "content_sha256": "af8e77f0c73ad2034aafb1882fc084989127208604cd22b8ea51acdabfac51cb",
        "text_sha256": "ad41e547f584f63e1482376689d7b18a37f87d1f81f673566858022f25d0d968",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ed7414b15db0642e",
      "claim_ids": [
        "P-SA-020"
      ],
      "note": "Defense Magazine 27.04.2025 gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-ed7414b15db0642e",
        "url": "https://www.defensemagazine.com/article/the-first-french-armys-tactical-group-to-receive-51-leclerc-xlr-tanks-by-the-end-of-2025",
        "content_sha256": "2ec9322df058ddd5ed7a87069dba7a97dc1060c854f263a5fb7fcb2e34786756",
        "text_sha256": "93f18fa4e85fc0d8e61bb861b613185d25546a87eaf9ea669f4110315d3a0f8b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ee4267732f9a7094",
      "claim_ids": [
        "P-SA-054"
      ],
      "note": "Janes 29.07.2024 gelesen (Absätze 1-5).",
      "snapshot": {
        "source_id": "S-ee4267732f9a7094",
        "url": "https://www.janes.com/defence-intelligence-insights/defence-news/land/bundeswehr-upgrades-fennek-reconnaissance-vehicles",
        "content_sha256": "5788820a439fbf441fdfe946dc1ff7050f097ea73119a9d84bfb471d1ebc72f9",
        "text_sha256": "57c11aa031a4fb5a3d49f7465333db3d85ba02c018584d56950ddd6f3a5cadb6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-effee1b7a20dfb27",
      "claim_ids": [
        "P-SB-041"
      ],
      "note": "KNDS-DONAR-Produktseite gelesen (Einleitung, Beschreibung).",
      "snapshot": {
        "source_id": "S-effee1b7a20dfb27",
        "url": "https://knds.com/en/products/systems/donar",
        "content_sha256": "afc0ac8b3acf5525210b6953f6f2e1a8575978a4b03fa74088327f70e1953dbf",
        "text_sha256": "55d3a1a2fa90a953b75bdde1d7f07de7368997ebd8a5060ba520df4c97daf365",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f0b9b622bee87228",
      "claim_ids": [
        "P-SA-031"
      ],
      "note": "Gelesen: cache read, cpm-Defence-Network-Artikel vom 16.06.2024 (Zeilen 31-47).",
      "snapshot": {
        "source_id": "S-f0b9b622bee87228",
        "url": "https://defence-network.com/boxer-rct30-radschuetzenpanzer-der-bundeswehr/",
        "content_sha256": "5bdb6c391bca8929f24ab328bbb2e14189d1d4aedc702092b3b16794a95447f4",
        "text_sha256": "df9bad70758e48aba75b4671ddf49f53c5a1980dc1da39413a73bb073533326a",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f29f7e1a60049a10",
      "claim_ids": [
        "P-SB-059"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-f29f7e1a60049a10",
        "url": "https://knds.com/en/products/systems/arx-30",
        "content_sha256": "66638c392913d4f6127f818f426f4edbb792aa1587b31c2480aa9dc7376e0be9",
        "text_sha256": "8d6582c4d34a96d39783dfd90235326dcd8f1229701cc17536a0afb1051e1032",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f2d42409b1c3a92d",
      "claim_ids": [
        "P-SA-027"
      ],
      "note": "Gelesen: cache read, PSM-Meldung 'Erste Auslieferung aus dem 2. Los SPz PUMA' Zeilen 72-75; Seite ohne Datum.",
      "snapshot": {
        "source_id": "S-f2d42409b1c3a92d",
        "url": "https://www.psm-spz.de/news/detail/erste-auslieferung-aus-dem-2-los-spz-puma/",
        "content_sha256": "5a104eb51f62383f517e3b3844d6a98185cb78cb74b1bd9ebd969ba4eccc3ec9",
        "text_sha256": "de2d3fd10bcad97c09b39c022776a7821664ea3fa9a3c0ed44e056730155384b",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f33a58fa096a6070",
      "claim_ids": [
        "P-SA-029"
      ],
      "note": "Gelesen: cache read, EDR-Wiedergabe der KNDS-Mitteilung vom 13.10.2025 (Zeilen 41-45).",
      "snapshot": {
        "source_id": "S-f33a58fa096a6070",
        "url": "https://www.edrmagazine.eu/germany-and-the-netherlands-procure-222-boxer-rct-30-wheeled-infantry-fighting-vehicles",
        "content_sha256": "b304f94e540fdc3b72528fbd7af8e4708aa880e21a3ff8149229ec73c656bb75",
        "text_sha256": "8e0260a8cd3d9bf1ed5cd82c78b06b0aa8418333bd34d39b4d54aac9ac5d67ba",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f50e6574f787d1cc",
      "claim_ids": [
        "P-SD-070"
      ],
      "note": "Army Technology 19.09.2024 gelesen (Absätze 1-10).",
      "snapshot": {
        "source_id": "S-f50e6574f787d1cc",
        "url": "https://www.army-technology.com/news/knds-will-sustain-all-of-canadas-leopard-2-tanks/",
        "content_sha256": "28a524f21246f2f5900ec6637e143c7eacf2413374bb0fc91e9d87e349bebfbd",
        "text_sha256": "f16b1caafa10855bee8737c98295aaf0e72e6a657dc686c4575f80518cee5fd0",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f55f74045ea5d4f3",
      "claim_ids": [
        "P-SA-026"
      ],
      "note": "Rheinmetall-Pressemitteilung 19.12.2025 gelesen (Absätze 1-6).",
      "snapshot": {
        "source_id": "S-f55f74045ea5d4f3",
        "url": "https://www.rheinmetall.com/de/media/news-watch/news/2025/12/2025-12-19-rheinmetall-und-knds-liefern-200-schuetzenpanzer",
        "content_sha256": "89576df13bda2cb2bb42188b30f205970f7c58275300da845eed3795affe3513",
        "text_sha256": "f5fae7c2d28af908662cd54f081c8e7db557632df2cedde6d2587e09706b80cd",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f6d4aa6643f3b5ed",
      "claim_ids": [
        "P-SD-062",
        "P-SD-063"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-f6d4aa6643f3b5ed",
        "url": "https://thedefensepost.com/2026/01/12/germany-puma-simulators/amp/",
        "content_sha256": "d1c86604549e96d3711823bf04954669462e3eb44e2cc18740f2d10809cd91d0",
        "text_sha256": "d28dcd7aa37e4402429b4e2e10b460ab19b27e2c6359157c07b2b4660c524057",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-f867eabd40cee703",
      "claim_ids": [
        "P-SC-016"
      ],
      "note": "Gelesen: cache read, ESD-Artikel (KNDS-Mitteilungstext) vom 19.02.2026 Zeilen 94-112.",
      "snapshot": {
        "source_id": "S-f867eabd40cee703",
        "url": "https://euro-sd.com/2026/02/news/land/49406/dga-selects-knds-new-generation-shard-sabot-round/",
        "content_sha256": "537594d84dcd5135d5746529f66e55f7d3aed5b2770556cbd1582393c452d635",
        "text_sha256": "44bc27f55af5aa7e9570cf31f5a7d843d559fa4c6b5a62a87d5569e7256c610c",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-faf0f3da7c18e608",
      "claim_ids": [
        "P-SD-071"
      ],
      "note": "Kyiv Independent 21.01.2025 gelesen (Absätze 1-8).",
      "snapshot": {
        "source_id": "S-faf0f3da7c18e608",
        "url": "https://kyivindependent.com/germanys-knds-launches-joint-venture-with-ukraine-for-military-equipment-repair/",
        "content_sha256": "3a9a38833c43407c2648ca03b22a91877882d40bc6cd96a3e4cc5c1316a53c8b",
        "text_sha256": "9abe63203241edafd509fbe7c2fcefea0c3c8dc35e15ce76707bc8f973b275e6",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-fb0c3ce8dc87caae",
      "claim_ids": [
        "P-SB-045"
      ],
      "note": "Frei sichtbarer Janes-Artikeltext (Abs. 1-4) über source-cache.py read gelesen; Rest hinter Abo nicht lesbar.",
      "snapshot": {
        "source_id": "S-fb0c3ce8dc87caae",
        "url": "https://www.janes.com/osint-insights/defence-news/industry/paris-air-show-2025-france-orders-land-based-version-of-40-mm-rapidfire-system",
        "content_sha256": "ce2f6c2872a161964b2e74e5373e0ad17d8d9f8c40617ed91d69c0b96d74278a",
        "text_sha256": "77896b30fdfe0c6b74e2aaa511cc9792602a90690fa7863dc3a1d93928e6d314",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-fbe7bae5557bc1a3",
      "claim_ids": [
        "P-SB-046"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-fbe7bae5557bc1a3",
        "url": "https://www.edrmagazine.eu/pas-2025-knds-france-and-thales-present-the-land-based-variant-of-the-40-mm-rapidfire",
        "content_sha256": "2e00597b4c7ecc79d73480a9efa770b58be8c4e019cb3ceecbe22fdb8cfd168c",
        "text_sha256": "65106e5eadbba8e00814e30d49b4d70473d59503b98718fd855ca1f4faf9ca23",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-fd7ccc7b386def8c",
      "claim_ids": [
        "P-SC-048"
      ],
      "note": "Gelesen: cache read, Overt-Defense-Artikel vom 04.03.2025 (Zeilen 17-35).",
      "snapshot": {
        "source_id": "S-fd7ccc7b386def8c",
        "url": "https://www.overtdefense.com/2025/03/04/knds-france-unveils-centurio-x30-next-gen-combat-robot",
        "content_sha256": "83c53b3daed57553b3c5db03576bf8b401d8df7b762ae138c2b3591d5094ca30",
        "text_sha256": "4b6589f1272737e8962e2888e6df5218da28049e0b1cba7b120c5305595593eb",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-fec6c39538475055",
      "claim_ids": [
        "P-SA-041"
      ],
      "note": "EDR Magazine (KNDS-France-Pressemitteilung Versailles 23.09.2026) gelesen (Absätze 1-10).",
      "snapshot": {
        "source_id": "S-fec6c39538475055",
        "url": "https://www.edrmagazine.eu/knds-france-delivers-first-ebrc-jaguar-armored-vehicles-at-r3-standard-to-the-french-army",
        "content_sha256": "0cd02685daf91f354b77ab84eb4c3f457ff6ae4d361df26bb61f6f6f5fcce739",
        "text_sha256": "3f78fddcc392c574608faa520a18039eea6b308882ce99161641d0b448dfecd2",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    },
    {
      "source_id": "S-ff9d328558f6334a",
      "claim_ids": [
        "P-SC-019",
        "P-SC-025",
        "P-SC-026",
        "P-SC-031"
      ],
      "note": "Gespeicherter Original-/Extrakttext über source-cache.py read gelesen (Titel, Datum und Textabschnitte der zugewiesenen Claims; Navigations-/Cookie-Boilerplate übergangen); alle Claims vollständig (A) gegen die genannten Abschnitte geprüft.",
      "snapshot": {
        "source_id": "S-ff9d328558f6334a",
        "url": "https://defence-industry.eu/mataris-knds-launches-frances-first-full-range-of-loitering-munitions/",
        "content_sha256": "bc04d74b3a895ee6846022b3fd7fb151015f862b58eb8c229c343c2b17c7b554",
        "text_sha256": "e3bdee2730b35b61c1d03ca49f8585e58c5d77126b80f443990b82c310d7497e",
        "capture_kind": "http-original",
        "capture_note": null,
        "extraction_notice": "Derived HTML text; scripts/styles omitted. Original HTML retained; dynamic content may require browser."
      }
    }
  ],
  "parallel_review": {
    "plan_fingerprint": "125875bd1971b5fca7ca6afdf84be8b5c58fbb6c8d0d793cefac768745e4fc18",
    "source_collection_fingerprint": "105cd826f889fd21477098f35b115cd56e3679ef42be431428cf268f5689c4ba",
    "part_fingerprints": {
      "sources-1": "2b31d4416e7fd2b06a1ece4891b78b6ffe874a8395364acabad7f2150b55ec36",
      "sources-2": "d290f16440cba4d3849c671c58d8eb40de41786881fb2fa8522334bf59b8a21c",
      "sources-3": "80b6f21a7080f5e94141ddc709af3e5ae356457b5c8f04f4dc0f982e286f8f30"
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
      "status": "offen",
      "reason": "No cached original for S-f78bf9f5633dc0c2; document job could not read the original; the live summary is not evidence. Plausible, consistent with S-219f5e5f415564c3/S-ed7414b15db0642e, but not releasable.",
      "action": "Main agent: fetch/store the KNDS page via source-cache.py (access date 2026-10-29), rebuild review-work/split and re-run the document job; alternatively portfolio replaces the evidence by already checked sources (S-2b10b29533252970, S-219f5e5f415564c3).",
      "owner": "main",
      "id": "P-02",
      "evidence_review": "No cached original for S-f78bf9f5633dc0c2; document job could not read the original; the live summary is not evidence. Plausible, consistent with S-219f5e5f415564c3/S-ed7414b15db0642e, but not releasable.",
      "fingerprint": "56a20f6bf1e2dfac8452ea13b68f3bd940a47301d201540ae1ce98e2256c8569"
    },
    {
      "depth": "A",
      "status": "offen",
      "reason": "No cached original for S-2190194daccd00d4 (KNDS PUMA product page); document job read no stored original.",
      "action": "Main agent: fetch/store via source-cache.py, rebuild work/split, re-run document job for P-03; alternatively portfolio adds an already checked KNDS/PSM source.",
      "owner": "main",
      "id": "P-03",
      "evidence_review": "No cached original for S-2190194daccd00d4 (KNDS PUMA product page); document job read no stored original.",
      "fingerprint": "15aaf0f82115c9b590d64e7599e7073de2aecf49791e4da586c849f050aad386"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Document job: only the SCORPION production part (GRIFFON/JAGUAR with Arquus/Thales, SERVAL with Texelis) is supported; \"the portfolio also includes VBCI\" is not supported (VBCI only appears in a history timeline); additionally no cache snapshot (S-3e48809a6efb1a20). Lead concurs.",
      "action": "Portfolio: restrict claim to SCORPION production of GRIFFON/JAGUAR/SERVAL or support VBCI with a proper source (e.g. KNDS VBCI product page S-94e524ffa416c9c1 already backs P-SA-049). Main: store the page in the document cache and rebind the snapshot.",
      "owner": "portfolio / main",
      "id": "P-05",
      "evidence_review": "Document job: only the SCORPION production part (GRIFFON/JAGUAR with Arquus/Thales, SERVAL with Texelis) is supported; \"the portfolio also includes VBCI\" is not supported (VBCI only appears in a history timeline); additionally no cache snapshot (S-3e48809a6efb1a20). Lead concurs.",
      "fingerprint": "d7ea6c21003dd1d6f8a0b3fdf9c6fe097773693bd49d4da661a2a890c111a159"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "event_status \"in service (army units)\" and uncertainty \"Shows XLR tanks in army tank units\" go beyond the article: it shows an XLR with a drone cage at Eurosatory and says the cage (not the tank) is being manufactured and delivered to tank units. Lead concurs with the document job.",
      "action": "Set event_status to \"presented (Eurosatory 2026); add-on cage in production/delivery to tank units\" and fix the uncertainty; base XLR deliveries only on P-SA-016..020 (P-SA-018 count of 34 by 10 Dec 2024), not on this claim.",
      "owner": "portfolio",
      "id": "P-SA-021",
      "evidence_review": "event_status \"in service (army units)\" and uncertainty \"Shows XLR tanks in army tank units\" go beyond the article: it shows an XLR with a drone cage at Eurosatory and says the cage (not the tank) is being manufactured and delivered to tank units. Lead concurs with the document job.",
      "fingerprint": "13af9a26d9c1e2e9bb0c573bbf76b6b71f3e3f322bfc6ebc329714f6921a0e56"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "event_status \"delivered (Lot 1)\" is not supported: hartpunkt says \"procured\" (beschafft); Lot 1 vehicles are still being brought to S1 by industry. Statement text itself is supported.",
      "action": "Set event_status to \"procured (Lot 1: 350; Lot 2: 50) / ordered (further 200, delivery from 2028 planned)\"; delivery of Lot 2 only via P-SA-027.",
      "owner": "portfolio",
      "id": "P-SA-025",
      "evidence_review": "event_status \"delivered (Lot 1)\" is not supported: hartpunkt says \"procured\" (beschafft); Lot 1 vehicles are still being brought to S1 by industry. Statement text itself is supported.",
      "fingerprint": "e77b913d1f6d119aee4ec3160c4d82e72ff08d2ed59f19e45274af8ae4593a9c"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Single source (S-3b6ac7ad2710c1a9) supports only Luxembourg acquiring 38 Jaguar via the Belgian order and the GME consortium building Jaguar; the part \"CaMo covers Jaguar for Belgium\" (Belgian Jaguar order) is not in that document (document job states it needs another source).",
      "action": "Narrow the statement to the Luxembourg/consortium part or add a source for the Belgian Jaguar order (60 vehicles) as evidence_item.",
      "owner": "portfolio",
      "id": "P-SA-043",
      "evidence_review": "Single source (S-3b6ac7ad2710c1a9) supports only Luxembourg acquiring 38 Jaguar via the Belgian order and the GME consortium building Jaguar; the part \"CaMo covers Jaguar for Belgium\" (Belgian Jaguar order) is not in that document (document job states it needs another source).",
      "fingerprint": "293a2212e5a896da12dc05663a7ae16b4ddd969f8a1764f201ce3a8fba031eb4"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Statement parenthesis \"up to 550 infantry fighting vehicles and command post vehicles\" can be read as total scope and contradicts 630 ordered; source: up to 550 VCI and 150 VPC (700 conditional), 630 ordered.",
      "action": "Rephrase: up to 550 VCI and 150 VPC (700 conditional) planned, 630 ordered by Sept 2009.",
      "owner": "portfolio",
      "id": "P-SA-050",
      "evidence_review": "Statement parenthesis \"up to 550 infantry fighting vehicles and command post vehicles\" can be read as total scope and contradicts 630 ordered; source: up to 550 VCI and 150 VPC (700 conditional), 630 ordered.",
      "fingerprint": "eee43768b6837f35f60fd37dba4e54a41ea73a486547404e84c2c5e10199b409"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "\"In November 2023\" and event_date 2023-11-29 are not supported by the claim's only source (KNDS release dated 06.12.2023, no signing date); the signing date 29.11.2023 comes from Janes (S-1a4e06392b187ffb, used in P-SA-056). Uncertainty \"undated\" is outdated.",
      "action": "Either add S-1a4e06392b187ffb as evidence_item for the signing date or restate as \"announced 6 December 2023\"; fix the uncertainty.",
      "owner": "portfolio",
      "id": "P-SA-055",
      "evidence_review": "\"In November 2023\" and event_date 2023-11-29 are not supported by the claim's only source (KNDS release dated 06.12.2023, no signing date); the signing date 29.11.2023 comes from Janes (S-1a4e06392b187ffb, used in P-SA-056). Uncertainty \"undated\" is outdated.",
      "fingerprint": "dc068a505221e7b33fdc1462e553523c6df76ac94ed0c56471d00f7cea07df1e"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "kind \"Herstellerangabe\" and the uncertainty \"treated as manufacturer-side because the plant director is quoted\" are not supported: the director is quoted only for one remark; the figures are not attributed to the plant/KNDS in the article.",
      "action": "Change kind to Fakt (media report by Lyon Capitale), remove the manufacturer-side assumption from the uncertainty.",
      "owner": "portfolio",
      "id": "P-SB-003",
      "evidence_review": "kind \"Herstellerangabe\" and the uncertainty \"treated as manufacturer-side because the plant director is quoted\" are not supported: the director is quoted only for one remark; the figures are not attributed to the plant/KNDS in the article.",
      "fingerprint": "614ae1479d37b12919809c8a15141f54989c98c5ab365e3e47935728c376e547"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "event_status \"durchgeführt\" and the article title \"confirms delivery\" overstate the body: minister says Ukraine \"is receiving\"; the quote only says the first vehicle destined for Ukraine was stationed in Kassel two years ago (paraphrase says \"sent\"); number/time of handover unclear; combat use explicitly unconfirmed (Bild). Lead cross-check (RCH-155 conflict, see group note) confirms status unresolved.",
      "action": "Set event_status to \"delivery stated by minister, timing/number unclear; Ukrainian use unconfirmed\"; do not present as confirmed delivery or operation. Also remove P-SB-013 from the AGM row (see mapping findings).",
      "owner": "portfolio",
      "id": "P-SB-013",
      "evidence_review": "event_status \"durchgeführt\" and the article title \"confirms delivery\" overstate the body: minister says Ukraine \"is receiving\"; the quote only says the first vehicle destined for Ukraine was stationed in Kassel two years ago (paraphrase says \"sent\"); number/time of handover unclear; combat use explicitly unconfirmed (Bild). Lead cross-check (RCH-155 conflict, see group note) confirms status unresolved.",
      "fingerprint": "abe088cec86da89d81bfd9f7d7a82a890111312eccdd9ae32f9d70e6cec0a3ba"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "\"the first PzH 2000 ... was rolled out\" - the release does not say \"first\" for the roll-out; it says the first PzH 2000 are to be delivered from May 2026.",
      "action": "Remove \"first\" from the roll-out clause; keep delivery from May 2026 as plan.",
      "owner": "portfolio",
      "id": "P-SB-024",
      "evidence_review": "\"the first PzH 2000 ... was rolled out\" - the release does not say \"first\" for the roll-out; it says the first PzH 2000 are to be delivered from May 2026.",
      "fingerprint": "605ddd48912e6b01302721b3fef0dcff9baab1496753d8c38e2307ad8a6cbb94"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Statement says 14 + 11 + 18 \"for a total of 54\", but the source puts the 54 total after \"in addition to 11 SPHs from other countries\"; the omission makes the arithmetic misleading (43 German-provided).",
      "action": "Add that the total of 54 includes 11 systems from other countries.",
      "owner": "portfolio",
      "id": "P-SB-027",
      "evidence_review": "Statement says 14 + 11 + 18 \"for a total of 54\", but the source puts the 54 total after \"in addition to 11 SPHs from other countries\"; the omission makes the arithmetic misleading (43 German-provided).",
      "fingerprint": "30263fa8fd5509030ff16bde888e0f616d53c96b89465a1c3e4a45fb1801a69e"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "\"97 in Bundeswehr inventory\" is a field of the A4 project entry whose reference the page does not explain (probably older PzH 2000); it can be read as 97 A4 delivered. The page shows no A4 handover.",
      "action": "Rephrase: page field \"Bestand: 97\" without explanation; no delivery of new A4 vehicles shown.",
      "owner": "portfolio",
      "id": "P-SB-029",
      "evidence_review": "\"97 in Bundeswehr inventory\" is a field of the A4 project entry whose reference the page does not explain (probably older PzH 2000); it can be read as 97 A4 delivered. The page shows no A4 handover.",
      "fingerprint": "c329ed8d7826020dc65a1327f55aca70b2c1b978118d6243f98d659c28bd0d45"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Unresolved source conflict (RapidFire, 48 systems): Janes says DGA ordered \"48 land-based versions\" (citing a Thales release); KNDS/Thales release (P-SB-043/-044) and EDR (P-SB-046) say 48 RAPIDFire in total, 14 firmly ordered for the Navy, land version \"currently being developed\", two land units for the Air and Space Force \"soon\" for operational testing. event_status \"beauftragt\" therefore not established for land systems.",
      "action": "Restate as conflicting report (Janes: 48 land-based vs manufacturer/EDR: 48 total incl. Navy; land order not established) and set event_status accordingly; do not use as land order or stage basis.",
      "owner": "portfolio",
      "id": "P-SB-045",
      "evidence_review": "Unresolved source conflict (RapidFire, 48 systems): Janes says DGA ordered \"48 land-based versions\" (citing a Thales release); KNDS/Thales release (P-SB-043/-044) and EDR (P-SB-046) say 48 RAPIDFire in total, 14 firmly ordered for the Navy, land version \"currently being developed\", two land units for the Air and Space Force \"soon\" for operational testing. event_status \"beauftragt\" therefore not established for land systems.",
      "fingerprint": "646c17cd58b65d9c6ddcfbc97270b1a4ee7305eab0674cc037480cb328fb74a5"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Plural \"30x150mm rounds in the French Air Force and other forces\" generalises: the catalogue page 80 describes only the 30x150 SAPHEI round.",
      "action": "Name the SAPHEI round only.",
      "owner": "portfolio",
      "id": "P-SC-003",
      "evidence_review": "Plural \"30x150mm rounds in the French Air Force and other forces\" generalises: the catalogue page 80 describes only the 30x150 SAPHEI round.",
      "fingerprint": "0983c4c0c8937edfb9f781ab53665fe493091802de783692e8a52befc340bb9a"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "event_status \"beauftragt\" overstates: the source supports a procurement authorisation (authorised), not a signed supply contract; statement text (\"authorised\") is correct.",
      "action": "Set event_status to \"procurement authorised / announced\".",
      "owner": "portfolio",
      "id": "P-SC-008",
      "evidence_review": "event_status \"beauftragt\" overstates: the source supports a procurement authorisation (authorised), not a signed supply contract; statement text (\"authorised\") is correct.",
      "fingerprint": "2c3fb12e2614142ba8ee615051d416f2b7d5d0a9d879231ff4139350bf11fecd"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Source conflict on SHARD announcement date: claim says press release of 18 February 2026 (Calibre Defence); EDR (checked by lead, 17/02/2026 dateline) and Army Recognition give 17 February 2026; ESD article is 19 Feb. KNDS primary release not read by anyone.",
      "action": "Use 17 February 2026 (announcement per EDR/Army Recognition), mention Calibre's 18 Feb, adjust event_date; or support the date with the KNDS primary release.",
      "owner": "portfolio",
      "id": "P-SC-016",
      "evidence_review": "Source conflict on SHARD announcement date: claim says press release of 18 February 2026 (Calibre Defence); EDR (checked by lead, 17/02/2026 dateline) and Army Recognition give 17 February 2026; ESD article is 19 Feb. KNDS primary release not read by anyone.",
      "fingerprint": "14209fbdebb78618320ebcc037e2fd5fe9fcce552cd08732335714099de2e04c"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Attribution not supported: Breaking Defense paragraph names no speaker; \"citing KNDS at the Paris Air Show\" and kind Herstellerangabe are not established.",
      "action": "Change kind to Fakt (media report) or remove \"citing KNDS\"; keep the uncertainty about the 460 quantity.",
      "owner": "portfolio",
      "id": "P-SC-020",
      "evidence_review": "Attribution not supported: Breaking Defense paragraph names no speaker; \"citing KNDS at the Paris Air Show\" and kind Herstellerangabe are not established.",
      "fingerprint": "11c0a2632564ad654ad3ff8a185ffee42838d9ff9b8d291cf9ed6aa6aef95313"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Attribution \"According to KNDS\" not supported: the test-count sentence in Defense Mirror is not attributed to KNDS; event_date 2025-11 is not in the article.",
      "action": "Reattribute to Defense Mirror (kind Fakt) and mark the date as \"before qualification, date not stated\".",
      "owner": "portfolio",
      "id": "P-SC-022",
      "evidence_review": "Attribution \"According to KNDS\" not supported: the test-count sentence in Defense Mirror is not attributed to KNDS; event_date 2025-11 is not in the article.",
      "fingerprint": "09dc563c72afce93f87900b3fe93a223d3f3c2849acf8f779c088a7c9850d7da"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "event_status \"beauftragt\" not supported: Breaking Defense (Travert) only says the DGA decided after the Colibri demonstration to order industrialisation; no contract, value or quantity.",
      "action": "Set event_status to \"industrialisation decision stated by company; contract not shown\".",
      "owner": "portfolio",
      "id": "P-SC-024",
      "evidence_review": "event_status \"beauftragt\" not supported: Breaking Defense (Travert) only says the DGA decided after the Colibri demonstration to order industrialisation; no contract, value or quantity.",
      "fingerprint": "f31972f13b1bac9f754a1c17451719ec97716c7da492c88c4dac947dc49e0749"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Attribution overstated: \"as stated by KNDS and EOS\" - the 23 MV-100 total, \"DGA acquired\" and the 17/6 VELOCE/RODEUR split are EDR's own understanding; only the 17 VELOCE 330 purchase for test/training is in Breaking Defense (EOS president).",
      "action": "Reattribute: EDR reports DGA acquired 23 (17 VELOCE 330, 6 RODEUR 330 per EDR understanding); Breaking Defense: 17 VELOCE 330 procured for test/training.",
      "owner": "portfolio",
      "id": "P-SC-029",
      "evidence_review": "Attribution overstated: \"as stated by KNDS and EOS\" - the 23 MV-100 total, \"DGA acquired\" and the 17/6 VELOCE/RODEUR split are EDR's own understanding; only the 17 VELOCE 330 purchase for test/training is in Breaking Defense (EOS president).",
      "fingerprint": "07ca88429cfbc431d3be77e23c350cf99ecf5fbe23c643ce3164d5ad1626360b"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "\"According to KNDS France\" is only indirectly supported: Defence Industry Europe states the 2012 unveiling and the use since 2017 (US Navy SEALs, GIGN, CAF, Shanghai) without attributing them to KNDS.",
      "action": "Reattribute to Defence Industry Europe (kind Fakt) or add KNDS source.",
      "owner": "portfolio",
      "id": "P-SC-036",
      "evidence_review": "\"According to KNDS France\" is only indirectly supported: Defence Industry Europe states the 2012 unveiling and the use since 2017 (US Navy SEALs, GIGN, CAF, Shanghai) without attributing them to KNDS.",
      "fingerprint": "ba905321c93eeb0fbfabed40c4d28481e80ca0e73e357c787d300c1d881436b8"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Identity link missing: statement and source name WFEL only; no checked source ties WFEL to KNDS UK/KMW for this claim (P-SD-011 only says \"KMW subsidiary\" in 2016). Mapping to KNDS rows DSB relies on this.",
      "action": "Add an evidence item/claim stating WFEL is today KNDS UK (company source) or label the claim as predecessor-company evidence.",
      "owner": "portfolio",
      "id": "P-SD-012",
      "evidence_review": "Identity link missing: statement and source name WFEL only; no checked source ties WFEL to KNDS UK/KMW for this claim (P-SD-011 only says \"KMW subsidiary\" in 2016). Mapping to KNDS rows DSB relies on this.",
      "fingerprint": "f8474cad40dca48ce647f41e5d92d5953f486a89f0cb0cd9e901f577dd0a6eab"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Identity link missing: article names neither KNDS nor KMW (document job text search empty); WFEL = KNDS UK not shown; status date 2018 only. Claim is mapped to both DSB and MGB rows.",
      "action": "Add evidence linking WFEL to KNDS UK/KMW, or remove from KNDS rows; keep as historical 2018 first tranche to ADF.",
      "owner": "portfolio",
      "id": "P-SD-013",
      "evidence_review": "Identity link missing: article names neither KNDS nor KMW (document job text search empty); WFEL = KNDS UK not shown; status date 2018 only. Claim is mapped to both DSB and MGB rows.",
      "fingerprint": "636380e3ca7067efe38240122b4b9b81927cf6a317651740f572bb31d223d952"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "Page states in-service use jointly for MGB and DSB; an MGB-specific statement (British Army, U.S. Army, NATO) is not on the page. Prime-contractor part is supported.",
      "action": "Rephrase to \"MGB and DSB together\" or add an MGB-specific source; keep prime-contractor part.",
      "owner": "portfolio",
      "id": "P-SD-021",
      "evidence_review": "Page states in-service use jointly for MGB and DSB; an MGB-specific statement (British Army, U.S. Army, NATO) is not on the page. Prime-contractor part is supported.",
      "fingerprint": "6dc4b5bb393dd3b1d6ee2ac385e32befef0169f2464ac57d7f854370b807deeb"
    },
    {
      "depth": "A",
      "status": "Korrektur",
      "reason": "\"now KNDS CBRN\" not supported: the article only names NBC-Sys as a subsidiary of the Nexter Group.",
      "action": "Remove the successor wording or support it with a company source; supplier role stays a 2021 manufacturer statement.",
      "owner": "portfolio",
      "id": "P-SD-052",
      "evidence_review": "\"now KNDS CBRN\" not supported: the article only names NBC-Sys as a subsidiary of the Nexter Group.",
      "fingerprint": "9c0bd023609fff4e93c27a108d2ecb977168ce3754243fd79fdcae577ca002be"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-011",
      "evidence_review": "Leopard 2 A8 handover conflict (lead): both statements are correctly attributed and supported. KNDS (19 Nov 2025): handover to the soldiers of both nations to begin April 2026 as contractually agreed; BAAINBw/dpa and Defense News: test vehicles to the Bundeswehr in 2026, delivery to the troops from 2027, all 123 by 2030. Not reconcilable from the documents; lead web check found no report of a Bundeswehr handover by 29 Oct 2026. Treat April 2026 as a manufacturer plan, not as delivery; Bundeswehr row must not exceed roll-out/ordered. Norway handover (P-SA-012) is separate.",
      "fingerprint": "ec379062e4919314dc3dc3fbe0135923f8e6ea4643b14454c944498e2f1cbc2d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-014",
      "evidence_review": "Leopard 2 A8 handover conflict (lead): both statements are correctly attributed and supported. KNDS (19 Nov 2025): handover to the soldiers of both nations to begin April 2026 as contractually agreed; BAAINBw/dpa and Defense News: test vehicles to the Bundeswehr in 2026, delivery to the troops from 2027, all 123 by 2030. Not reconcilable from the documents; lead web check found no report of a Bundeswehr handover by 29 Oct 2026. Treat April 2026 as a manufacturer plan, not as delivery; Bundeswehr row must not exceed roll-out/ordered. Norway handover (P-SA-012) is separate.",
      "fingerprint": "f6f2e48088a0eebf6f501de616136ddd7cbb32f535a14af9b8464cbb41e6fe61"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-012",
      "evidence_review": "Norway delivery of first two A8 NO on 30 Apr 2026 is manufacturer-reported (KNDS release, repeated by Janes citing the KNDS release). Minor source differences (release 29/30 Apr vs 4 May; Levanger start \"autumn\" vs \"Q3 2026\") do not affect the delivery date; production start remains future. Lieferung laut Hersteller berichtet.",
      "fingerprint": "45272eb07891087e4afd1d77156d86ec0ad1ae5a2240586a4ace90503ef63386"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-027",
      "evidence_review": "Handover of first Lot-2 Puma (28 Aug 2026) is a PSM manufacturer statement relayed by media; vehicles go to testing at WTD 81/91, not troop use. Lieferung laut Hersteller berichtet.",
      "fingerprint": "de71ff90025e13e03110293c071e780a66636042965b509e5618770eee2a3a34"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-047",
      "evidence_review": "SERVAL contract date conflict (lead): Theatrum Belli (notified 31 Dec 2024) and KNDS France release (P-SB-058, Dec 2024) agree; Army Recognition says Feb 2025 - treated as outlier. The statement makes no contract-date assertion; uncertainty documents the divergence. Delivery of first 30 and the 21 Jan 2026 announcement are secondary to the unopened ministry release.",
      "fingerprint": "1f1409b30e90da7d1d2d37ac6593f514c7f2adba8c2c0f36ba253d462c6a2e9e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-010",
      "evidence_review": "RCH 155 / Ukraine (lead cross-check, unresolved): each claim is supported as an attributed report (ESD 13 Jan 2025: first vehicle presented, to train crews in Germany; Ukrinform 15 Mar 2026: 600 Ukrainians trained, system not yet in Bundeswehr service; esut 15 May 2026: delivery to troops imminent; Militarnyi 6 Sep 2026 citing the unofficial tracker German Aid to Ukraine: Ukraine received first; Drummond X post as reported July 2026: combat testing/combat-proven, adviser not an official statement). Together with P-SB-013 no official confirmation of vehicles delivered to or used by Ukraine exists; combat use unconfirmed; lead web check found no new official source. Matrix must not derive series/operation for RCH 155 from these claims.",
      "fingerprint": "13775a56de3eba335fc24e5ec609bc0920c439d0da935df5afa884385b70b54e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-012",
      "evidence_review": "RCH 155 / Ukraine (lead cross-check, unresolved): each claim is supported as an attributed report (ESD 13 Jan 2025: first vehicle presented, to train crews in Germany; Ukrinform 15 Mar 2026: 600 Ukrainians trained, system not yet in Bundeswehr service; esut 15 May 2026: delivery to troops imminent; Militarnyi 6 Sep 2026 citing the unofficial tracker German Aid to Ukraine: Ukraine received first; Drummond X post as reported July 2026: combat testing/combat-proven, adviser not an official statement). Together with P-SB-013 no official confirmation of vehicles delivered to or used by Ukraine exists; combat use unconfirmed; lead web check found no new official source. Matrix must not derive series/operation for RCH 155 from these claims.",
      "fingerprint": "ecf347d160838c79134e38408a8ad05eca16723b66e9628d8e446c5b0fdcb8f3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-014",
      "evidence_review": "RCH 155 / Ukraine (lead cross-check, unresolved): each claim is supported as an attributed report (ESD 13 Jan 2025: first vehicle presented, to train crews in Germany; Ukrinform 15 Mar 2026: 600 Ukrainians trained, system not yet in Bundeswehr service; esut 15 May 2026: delivery to troops imminent; Militarnyi 6 Sep 2026 citing the unofficial tracker German Aid to Ukraine: Ukraine received first; Drummond X post as reported July 2026: combat testing/combat-proven, adviser not an official statement). Together with P-SB-013 no official confirmation of vehicles delivered to or used by Ukraine exists; combat use unconfirmed; lead web check found no new official source. Matrix must not derive series/operation for RCH 155 from these claims.",
      "fingerprint": "2b98096aefd7cf2c83013fc7c3b7f02a060d04d5e77a9b69f7d7480f77cfd69e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-015",
      "evidence_review": "RCH 155 / Ukraine (lead cross-check, unresolved): each claim is supported as an attributed report (ESD 13 Jan 2025: first vehicle presented, to train crews in Germany; Ukrinform 15 Mar 2026: 600 Ukrainians trained, system not yet in Bundeswehr service; esut 15 May 2026: delivery to troops imminent; Militarnyi 6 Sep 2026 citing the unofficial tracker German Aid to Ukraine: Ukraine received first; Drummond X post as reported July 2026: combat testing/combat-proven, adviser not an official statement). Together with P-SB-013 no official confirmation of vehicles delivered to or used by Ukraine exists; combat use unconfirmed; lead web check found no new official source. Matrix must not derive series/operation for RCH 155 from these claims.",
      "fingerprint": "dedeb7824070de01c67a80e0f32e4ee0a6c55099ed01749a658a07b928867300"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-020",
      "evidence_review": "RCH 155 / Ukraine (lead cross-check, unresolved): each claim is supported as an attributed report (ESD 13 Jan 2025: first vehicle presented, to train crews in Germany; Ukrinform 15 Mar 2026: 600 Ukrainians trained, system not yet in Bundeswehr service; esut 15 May 2026: delivery to troops imminent; Militarnyi 6 Sep 2026 citing the unofficial tracker German Aid to Ukraine: Ukraine received first; Drummond X post as reported July 2026: combat testing/combat-proven, adviser not an official statement). Together with P-SB-013 no official confirmation of vehicles delivered to or used by Ukraine exists; combat use unconfirmed; lead web check found no new official source. Matrix must not derive series/operation for RCH 155 from these claims.",
      "fingerprint": "1f2ec3e4d04a5214897558b417bbcf7cb2fa41d1ff7b7faad65ed45879457965"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-043",
      "evidence_review": "RapidFire (lead): P-SB-043 and P-SB-047 describe the NAVAL RAPIDFire (in service on Jacques Chevallier; ammunition order for JAGUAR/RAPIDFire) and P-SB-048 the 40 CTAS component on other vehicles; none establishes a status for RapidFire Land. Land version: unveiled/under development (P-SB-044), two units for the Air and Space Force announced \"soon\" for operational testing (P-SB-046, June 2025), no later report. See P-SB-045 correction for the 48-unit conflict.",
      "fingerprint": "4a77e9251df96f6922594fb6e1143f2aefeb13e0208ead750b33f71164713c30"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-044",
      "evidence_review": "RapidFire (lead): P-SB-043 and P-SB-047 describe the NAVAL RAPIDFire (in service on Jacques Chevallier; ammunition order for JAGUAR/RAPIDFire) and P-SB-048 the 40 CTAS component on other vehicles; none establishes a status for RapidFire Land. Land version: unveiled/under development (P-SB-044), two units for the Air and Space Force announced \"soon\" for operational testing (P-SB-046, June 2025), no later report. See P-SB-045 correction for the 48-unit conflict.",
      "fingerprint": "801941441a94613f4d1fe2319434c2aba74cca5fab75e969b84a1be73c84d68d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-046",
      "evidence_review": "RapidFire (lead): P-SB-043 and P-SB-047 describe the NAVAL RAPIDFire (in service on Jacques Chevallier; ammunition order for JAGUAR/RAPIDFire) and P-SB-048 the 40 CTAS component on other vehicles; none establishes a status for RapidFire Land. Land version: unveiled/under development (P-SB-044), two units for the Air and Space Force announced \"soon\" for operational testing (P-SB-046, June 2025), no later report. See P-SB-045 correction for the 48-unit conflict.",
      "fingerprint": "57b002e064297605cc7c9929abe7837ca5c23fc6ff5e4c2b1f4860c9840e170e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-047",
      "evidence_review": "RapidFire (lead): P-SB-043 and P-SB-047 describe the NAVAL RAPIDFire (in service on Jacques Chevallier; ammunition order for JAGUAR/RAPIDFire) and P-SB-048 the 40 CTAS component on other vehicles; none establishes a status for RapidFire Land. Land version: unveiled/under development (P-SB-044), two units for the Air and Space Force announced \"soon\" for operational testing (P-SB-046, June 2025), no later report. See P-SB-045 correction for the 48-unit conflict.",
      "fingerprint": "e4626a2580cded448a6be9c0ebbf81f5f162141ffb810babde1bcbb8c73b7412"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-048",
      "evidence_review": "RapidFire (lead): P-SB-043 and P-SB-047 describe the NAVAL RAPIDFire (in service on Jacques Chevallier; ammunition order for JAGUAR/RAPIDFire) and P-SB-048 the 40 CTAS component on other vehicles; none establishes a status for RapidFire Land. Land version: unveiled/under development (P-SB-044), two units for the Air and Space Force announced \"soon\" for operational testing (P-SB-046, June 2025), no later report. See P-SB-045 correction for the 48-unit conflict.",
      "fingerprint": "ec78cbc65e45ffaced372ad7c148b1e91784dc3ee94e76dfd8c3b08e9af58fc9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-049",
      "evidence_review": "GEPARD (lead): claims are supported as attributed. They concern Gepard transferred from Bundeswehr stocks, KNDS maintenance (KNDS Ukraine), Rheinmetall ammunition (P-SB-051, not KNDS production) and talks/intent; KNDS role as manufacturer/producer of new Gepard is not documented. No series-production or KNDS delivery status derivable.",
      "fingerprint": "4ea9c855c3d2ec23add917cd5c0b724270ab4f2717e335efb5dffc1726ddd135"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-050",
      "evidence_review": "GEPARD (lead): claims are supported as attributed. They concern Gepard transferred from Bundeswehr stocks, KNDS maintenance (KNDS Ukraine), Rheinmetall ammunition (P-SB-051, not KNDS production) and talks/intent; KNDS role as manufacturer/producer of new Gepard is not documented. No series-production or KNDS delivery status derivable.",
      "fingerprint": "749274848e6b2351e616b521b55c7f7c42b18269e82a704a24d89ec4ad972461"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-051",
      "evidence_review": "GEPARD (lead): claims are supported as attributed. They concern Gepard transferred from Bundeswehr stocks, KNDS maintenance (KNDS Ukraine), Rheinmetall ammunition (P-SB-051, not KNDS production) and talks/intent; KNDS role as manufacturer/producer of new Gepard is not documented. No series-production or KNDS delivery status derivable.",
      "fingerprint": "d30eef9b6c85d14025c35fe1aa3ec3b0b4c1582973a7272d4244f5bface9d987"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-052",
      "evidence_review": "GEPARD (lead): claims are supported as attributed. They concern Gepard transferred from Bundeswehr stocks, KNDS maintenance (KNDS Ukraine), Rheinmetall ammunition (P-SB-051, not KNDS production) and talks/intent; KNDS role as manufacturer/producer of new Gepard is not documented. No series-production or KNDS delivery status derivable.",
      "fingerprint": "081ccfbff58f4e8c44a9acb5c05f160938b2a23974bb3d4f3180ff94cee9b200"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-053",
      "evidence_review": "GEPARD (lead): claims are supported as attributed. They concern Gepard transferred from Bundeswehr stocks, KNDS maintenance (KNDS Ukraine), Rheinmetall ammunition (P-SB-051, not KNDS production) and talks/intent; KNDS role as manufacturer/producer of new Gepard is not documented. No series-production or KNDS delivery status derivable.",
      "fingerprint": "663e4f93d972e753b38202512d1cd50bdb76d83c31b85c2a6c09eb10aaad7abf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-054",
      "evidence_review": "GEPARD (lead): claims are supported as attributed. They concern Gepard transferred from Bundeswehr stocks, KNDS maintenance (KNDS Ukraine), Rheinmetall ammunition (P-SB-051, not KNDS production) and talks/intent; KNDS role as manufacturer/producer of new Gepard is not documented. No series-production or KNDS delivery status derivable.",
      "fingerprint": "f5e1fcce5004db891f5c0fe98cc59ab25a231d279f616211eb6663ee5e3ce371"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-055",
      "evidence_review": "FLW (lead): P-SB-055 (BMVg) supports FLW 100/FLW 200 Bundeswehr use and the Jan 2025 further FLW 100 purchase but names no manufacturer; the KNDS attribution of FLW 100 rests on P-12 (KNDS catalogue) and P-SB-056 (defence-network, \"KNDS stations\") and is accepted on that basis. FLW 200 Plus has no order/delivery evidence; status of the FLW 200 Plus variant must not be inferred from FLW 100/200.",
      "fingerprint": "487cebf7a69ca305bb5d7128638142b5421cf9d7c5ac9da1e014002363b4d100"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-056",
      "evidence_review": "FLW (lead): P-SB-055 (BMVg) supports FLW 100/FLW 200 Bundeswehr use and the Jan 2025 further FLW 100 purchase but names no manufacturer; the KNDS attribution of FLW 100 rests on P-12 (KNDS catalogue) and P-SB-056 (defence-network, \"KNDS stations\") and is accepted on that basis. FLW 200 Plus has no order/delivery evidence; status of the FLW 200 Plus variant must not be inferred from FLW 100/200.",
      "fingerprint": "4df9c21be1b405e8d7907ca34bb7cb49ac035572416fcfd8e2e68081a91f9fa6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-057",
      "evidence_review": "FLW (lead): P-SB-055 (BMVg) supports FLW 100/FLW 200 Bundeswehr use and the Jan 2025 further FLW 100 purchase but names no manufacturer; the KNDS attribution of FLW 100 rests on P-12 (KNDS catalogue) and P-SB-056 (defence-network, \"KNDS stations\") and is accepted on that basis. FLW 200 Plus has no order/delivery evidence; status of the FLW 200 Plus variant must not be inferred from FLW 100/200.",
      "fingerprint": "225141e36ac8bef03c05daf80f5c64a85895a991544f35d3dc0e8661bc144317"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-12",
      "evidence_review": "FLW (lead): P-SB-055 (BMVg) supports FLW 100/FLW 200 Bundeswehr use and the Jan 2025 further FLW 100 purchase but names no manufacturer; the KNDS attribution of FLW 100 rests on P-12 (KNDS catalogue) and P-SB-056 (defence-network, \"KNDS stations\") and is accepted on that basis. FLW 200 Plus has no order/delivery evidence; status of the FLW 200 Plus variant must not be inferred from FLW 100/200.",
      "fingerprint": "d5416ba607aa1f8c38c6dbadc5fc30651dab244078a27869a3d28dfebc792ad3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-009",
      "evidence_review": "KATANA (lead): guidance mode/accuracy differ between product page (GPS/INS/semi-active laser, sub-metre, >40 km), catalogue (GNSS/inertial, decametric, >45 km) and 2024 release (accuracy \"few metres\"); recorded in the uncertainty. Supported as manufacturer statements; no series evidence.",
      "fingerprint": "1137c33a4f7e4bda302bc2b8672da6efb0ac109e8128cf1eead0cef4e9a59c6f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-012",
      "evidence_review": "KATANA (lead): guidance mode/accuracy differ between product page (GPS/INS/semi-active laser, sub-metre, >40 km), catalogue (GNSS/inertial, decametric, >45 km) and 2024 release (accuracy \"few metres\"); recorded in the uncertainty. Supported as manufacturer statements; no series evidence.",
      "fingerprint": "0e619e8f0640e428af20bb42630c6d86169c91d2043379aaf8c8c90e8e9ac395"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-001",
      "evidence_review": "KATANA/155 mm (lead): catalogue/product listing of KATANA gives no status; P-SC-013 (demonstrator TRL 6, offer within two years from June 2024) has expired by the as-of date without confirmation of qualification/order.",
      "fingerprint": "9812b469af6d89d2b348ab9455e933661612f502ab9aac6fdfd47178ac7fa000"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-013",
      "evidence_review": "KATANA/155 mm (lead): catalogue/product listing of KATANA gives no status; P-SC-013 (demonstrator TRL 6, offer within two years from June 2024) has expired by the as-of date without confirmation of qualification/order.",
      "fingerprint": "ad36450893cb38c3df12bf83ee538908c3c3dac9eb1733ac055764bcb4b56cd2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-018",
      "evidence_review": "MATARIS (lead): the operational statement (active service since Dec 2025) concerns the MX-10 only and must not be transferred to MV-100, MV-25 or MT-10 although the claim is mapped to those rows (see mapping findings).",
      "fingerprint": "beb259e9a943ffc8f267a3614d6fad0f902a6226521e7087a0ca9fb20befc836"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-049",
      "evidence_review": "CENTURIO (lead): DROIDE framework (DGA with KNDS France/Safran, 30 Dec 2024) names no CENTURIO as subject; claim states this; it must not support a CENTURIO status (see mapping findings).",
      "fingerprint": "536ffe66b6c87d9e3aee17aa2134b3ab087b4d4ed4cbf4bced2c5879593742df"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-040",
      "evidence_review": "NERVA/ULTRO (lead): P-SC-040 does not split NERVA types, so no NERVA-XX-specific status follows; P-SC-035 is a video of MT-10 integration on several platforms incl. ULTRO and is no ULTRO test/status evidence.",
      "fingerprint": "10bb5b1631608998e39e1fb26f4850ba1b4579945152c4b466f7c1ff66b3085f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-035",
      "evidence_review": "NERVA/ULTRO (lead): P-SC-040 does not split NERVA types, so no NERVA-XX-specific status follows; P-SC-035 is a video of MT-10 integration on several platforms incl. ULTRO and is no ULTRO test/status evidence.",
      "fingerprint": "4f2908b4aa1df90f3aa6a59087e6396fd5384961ae41d08911a6134062a18c67"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-039",
      "evidence_review": "Supported (EDR 2021); note that the uncertainty \"according to Nexter\" is not what the article says (editorial statement); non-blocking wording fix for the next portfolio round.",
      "fingerprint": "2d6915cdd5769efc717eb5045eb22f03dfd5c1e28a2ece0be8fca27b2fb5c619"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-041",
      "evidence_review": "D-LBO (lead): Bundeswehr/BMVg pages are programme-level, name neither KNDS nor ArGe D-LBO; conversion counts (>2,000 converted, target 2,700) cover industry as a whole, not a KNDS share; the troop-use date 1 Jan 2027 relates to the first large unit/NATO commitment. Supported as programme-level facts; the link to the KNDS-Rheinmetall ArGe rests on P-SD-040 and must be shown as programme-level in the profile.",
      "fingerprint": "671eac3ba1cb27ea2cc08486df8176ac2471e05fbad66449a92a255a0a005d00"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-042",
      "evidence_review": "D-LBO (lead): Bundeswehr/BMVg pages are programme-level, name neither KNDS nor ArGe D-LBO; conversion counts (>2,000 converted, target 2,700) cover industry as a whole, not a KNDS share; the troop-use date 1 Jan 2027 relates to the first large unit/NATO commitment. Supported as programme-level facts; the link to the KNDS-Rheinmetall ArGe rests on P-SD-040 and must be shown as programme-level in the profile.",
      "fingerprint": "c39c51431f22ddae31086e2e9a4242acfc8d50c841305b747af6c744b12f59b4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-050",
      "evidence_review": "Company/family-level statements (lead): P-SD-050 (CBRN, 70 years), P-SD-010 (MGB and DSB jointly) and P-SD-015 (over 40 armed forces) are supported as manufacturer statements but do not give product-specific status for single rows (cbrn-mask, cbrn-decon, dsb, mgb).",
      "fingerprint": "46cb15d75bfc54439147b18131175cb3df99f7e035d8b035e835dc031585042e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-010",
      "evidence_review": "Company/family-level statements (lead): P-SD-050 (CBRN, 70 years), P-SD-010 (MGB and DSB jointly) and P-SD-015 (over 40 armed forces) are supported as manufacturer statements but do not give product-specific status for single rows (cbrn-mask, cbrn-decon, dsb, mgb).",
      "fingerprint": "9a186f403514d041e793bce7e65ec020dc63d821c55f583e9c9dc94fb70c6360"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-015",
      "evidence_review": "Company/family-level statements (lead): P-SD-050 (CBRN, 70 years), P-SD-010 (MGB and DSB jointly) and P-SD-015 (over 40 armed forces) are supported as manufacturer statements but do not give product-specific status for single rows (cbrn-mask, cbrn-decon, dsb, mgb).",
      "fingerprint": "11e700cfeb9b99a6c9b84a468e3d2a5ea8146b532f54a548bd95760b134bdbba"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-062",
      "evidence_review": "Puma AGSP (lead): supported; the AGSP was developed by Rheinmetall (EUR 118.5m of 119.5m to Rheinmetall electronics); KNDS involvement is only via the PSM joint venture.",
      "fingerprint": "72ce81a0170aac9ae68e73918e667748af12499e0c9e8550a4c34a86697b1dc8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-063",
      "evidence_review": "Puma AGSP (lead): supported; the AGSP was developed by Rheinmetall (EUR 118.5m of 119.5m to Rheinmetall electronics); KNDS involvement is only via the PSM joint venture.",
      "fingerprint": "2ed45d60e1d0c8a013becd6563c45cfb3774b8e958bde4cbdfa54364b06212b6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-004",
      "evidence_review": "Malaysia: KNDS announces acquisition by the Malaysian MoD; the order was formalised between KNDS and local partner ADS; variant and delivery not stated; order only.",
      "fingerprint": "0ef0f1d478cdcfd93da4aff78cd3ff99c25a31fc29841f834364261fd9736d88"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-036",
      "evidence_review": "AGM/DONAR variants (lead): claims mix the truck-mounted AGM, AGM on Piranha HMC/DONAR 10x10 (Swiss order 2026), tracked ASCOD DONAR (2009 prototype) and AGM in RCH 155; each is supported for its own variant only; no common status for the row.",
      "fingerprint": "0cd8836009c440fb1be42b204e740e2daa093b106ccee9a0e2c302091537e2c2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-037",
      "evidence_review": "AGM/DONAR variants (lead): claims mix the truck-mounted AGM, AGM on Piranha HMC/DONAR 10x10 (Swiss order 2026), tracked ASCOD DONAR (2009 prototype) and AGM in RCH 155; each is supported for its own variant only; no common status for the row.",
      "fingerprint": "1bc1c74c6b8c0fa2cf3b40bfa9c9929843f34bf85a1c6e6eb3c36c1a83f7422b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-038",
      "evidence_review": "AGM/DONAR variants (lead): claims mix the truck-mounted AGM, AGM on Piranha HMC/DONAR 10x10 (Swiss order 2026), tracked ASCOD DONAR (2009 prototype) and AGM in RCH 155; each is supported for its own variant only; no common status for the row.",
      "fingerprint": "34ece3e5fca27e4fb0dc0dfb270b952b09c68e16ccb8abfa17d50a4b9b1f0cd8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-039",
      "evidence_review": "AGM/DONAR variants (lead): claims mix the truck-mounted AGM, AGM on Piranha HMC/DONAR 10x10 (Swiss order 2026), tracked ASCOD DONAR (2009 prototype) and AGM in RCH 155; each is supported for its own variant only; no common status for the row.",
      "fingerprint": "4209100b8b61cd856ec2324e0e42eff695c4a2461ae003bdce3856701b22e739"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-041",
      "evidence_review": "AGM/DONAR variants (lead): claims mix the truck-mounted AGM, AGM on Piranha HMC/DONAR 10x10 (Swiss order 2026), tracked ASCOD DONAR (2009 prototype) and AGM in RCH 155; each is supported for its own variant only; no common status for the row.",
      "fingerprint": "ccfc2e9fae660520f9859ffa980b152a088997ac4da3fa45201abf8130453ccc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-042",
      "evidence_review": "AGM/DONAR variants (lead): claims mix the truck-mounted AGM, AGM on Piranha HMC/DONAR 10x10 (Swiss order 2026), tracked ASCOD DONAR (2009 prototype) and AGM in RCH 155; each is supported for its own variant only; no common status for the row.",
      "fingerprint": "cf46e13fa8617b69ab96f350ac34a1b2ae94cb93c3e0081cdd50dbb21a90dda1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-064",
      "evidence_review": "GFF 4: hobby source (WarWheels.Net), hedged statement; supported only as indication, not decisive for status; prototype status rests on P-SA-063 (2008, historic).",
      "fingerprint": "f24cfb3e9b79136b6347970f220f286f2e5a5971cdd4c9331f8eee1cf077b09e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-002",
      "evidence_review": "Handover date: the release (12 Dec 2025) reports completion of delivery with a parade; the exact date of the last vehicle handover is not stated, 12 Dec 2025 is the release date.",
      "fingerprint": "0e7db897a493b47973b34193aebe67c1df523f0f36d729d87b5fd7f61c6696c9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-01",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "7b77251d6f49ba40e1aa1a3078c9065b6f655466485b303fd84c0844d86e634a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-001",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "77a38140a083f3399de5c5715f34b8a3451e8f1a9dd0c5fbd4892b1b61890230"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-003",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "65b1b0908e1df6ed38136bacd42c9ae72f7d2e4ff348f68e6df2092c364e8cf9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-004",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4dfc2eb62c2eda6e6bf9bf4878a4ba8aaff2bcfc62173f04cff41c948fdf516f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-005",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "5a137781a429da872b5a20caf0a54df116a95e6b67e507feac6a2c12bf223d77"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-006",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "12a23d6ff6ab71ec125aff7cba4d2a945d5fc48d948e5094cfd49c74ca8434d4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-007",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "19c7af90e05dbb8880f5b6f70674e5fc75bacfcbba7bbdb8cce4ed58d78b9993"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-008",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "386935ab2b01265c72c1ec1639a7736e0bdcafd2eafa2838e42fbb55fc2893bd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-009",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "8f08c4ecf827e3653c09f73a81d467ea8d3cef720cc5b4c08ba057d1f5ec46e8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-010",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "35ccb143b532d4e1eab02b6954e8cba2d0d2b446db158b5f21d83db21089f678"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-013",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "e61de5b411827d44af86b62edb9327363faaf1374bbe1cacfb49e6f0af3cd538"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-015",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4906d6a6108dcbfbd99216216c39ad2dce1f70c9629ff10f70b4eb91c73f1fa4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-016",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "05b8d0a5f022d9e892ec51073115e44ea039cc2e0820b7d527827bef6478099e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-017",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "3da17a052474185061fee7c2db76ef9f0d8f6956e4e189b012a5788e6a9a8e60"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-018",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4cbe108bd4d655322ca94e4d447b6e003fc3cc587e0444befd1deccac43f6a14"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-019",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a1b27c18fb7672c7855818f34f9fb9e897094320c154adca7056169cb36c7552"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-020",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "b9a20d95c885eb0c675d3e166d2597358d45abec40b66c7d0d09ba86db5a698f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-022",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a9217f65a411ab1788d8d66754ba443471eaf4843fbd6c2939a344ede249b25c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-023",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "6be15f2d74e23930ec1f3ca12d26f08c64f5c75f66de071029f2fb9e739c0d0b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-024",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "7d44092ba6c2832b9707e7762f988c326f085207fd89871bb5ec9252a0ae17ed"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-026",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "04faf336d258134c61333d2e1a3007c15048f9f851a913762f58158bdc6fb67f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-04",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c1ef4015cf03584a23046046875a74298e96b771b057a8c8f30bb2cf01ff787c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-028",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "6b0ea39575074aed71dce1b8aab38362679e7a247a5e19c28a7b326e9645779b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-029",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "dcd8bfc9568d19e4e185c9124a6620038f12d378bbb279a0553b3d489be9f17a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-030",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "0fd70fd6f965e29f07cba70f6500910d813405b9cafacfdc02c206ef11b87956"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-031",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "26e995a2e42ce01edfa988272373d9bc3fed470c4a9d4f3d3b0c1c240ef77942"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-032",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "7c78917724d9444cef012327ad10a85262dcabb869a4fa60e2e1510c2954ce6b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-033",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f91ad89d01cde660b7f83841041b2c4169ffa180d0078b8cf7575433e5c02ea0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-034",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a0b5e2f2aeaae4062cba69bdd0a50a23580af09c640c89109865c2ce96da7bad"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-035",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "44b560b76fded816cfcc63487d735ee18778a34cf7e0f17a5ea7d765b8f1ea69"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-036",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a807d21153c5f7d421f4bfeefef87b23aedac00c9c55848c7a8f4270c63b28ca"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-037",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c344fa103501485550235e7d32b3f81e33be5fa04ae65b8fd7d8d50afdd0a9de"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-038",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "0db15cd6485377b9221f37e5c0f650ce1c96aa535f1a88c967de43be211d36a6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-039",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "e3717fab4afff5b7fcc7804175299d195512afe10d402d75322d348828d7aa4a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-040",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "367f2d07667fb8670b0b9ffae0e6a2719f2ad4d2a8f71b512d9a31af7bae1914"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-041",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a3df91ab3a7e1f06eea4d19ca7c5bd631c6c170c6870efa7f55fc21d34987e82"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-042",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "3fc039d9c03e480085e02ac4455759e8cfde36849c26664cc396b27a2b53eced"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-044",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f3657bdbcb58e2199ec7cff16b9199fa6a9c23015df67ae9b1370d8edd5e7d48"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-045",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a57c86677c214b33c495b13750ffa4901a490d854cde524d4369ae93fcc99114"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-046",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "7bff07873001e6fe4002c5c8e35b3659c87c3f43a73b920f0db9a68270d3ad01"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-048",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "9342661239e62763eae506f97751f612db23f4140dcd379123414fe861fa9340"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-049",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c75dc7f1cb9cc3b82d40300511807610fc37bd95199d9c1697b7b6d1851060de"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-051",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "d5675f1abc27511dbb51dbd162e2ac1b8d1c391ccdc25d81570f2a4330d5611f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-052",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4ef7c19fe00f406fc37c9395368404a01239e2d0c295766ea7570d9edf2a0496"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-11",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "e286ef6514c415682c66508a97eadca4f187741b53afada1b5c147bfee28f716"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-053",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "03baeb0b75aee4866df5ce1e2562d5401ceb003ca2706a35515e67f422307128"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-054",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "e2a42b82c6310b7cf00c85593b73031c8f2c25b836723c5d232c672e01701737"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-056",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "d0a2d5636b5c0cb96b58c875e026e823973c46c8dd9b8addd0f1db2b067c9d60"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-057",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "418448689699efd6da2ccdaacb921374f1137e73826e99f970aba148d755b1e4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-058",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "156ba3a4fb2d2679203678dd9bf9c3e5a66872e1862269a1238216b66a7cf4a6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-059",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "ecb7ae429a27bd37e093b181a2487c2a576acf1626500c3de8ea17b12d219afc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-060",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "0d649f4c65151cfd26dce791bfa2df931c6d3d95ebcd84e71a30798e418715ce"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-061",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c79b713e267651d5a54d041e8d03d6e6c317635a18780797200937a716a4bbcb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-062",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "77b987c00bf70d8ccaaf9df8a7f5585db26821ac39454e2664ad05a7efd176ea"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SA-063",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "af847fa0117ffad96d9f1897da8292a79a2cf383f7562ff80220ec844468fff5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-06",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f18897394deaf59858570f258dc28ad35b57815f7482d2985f4c6254aa922144"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-07",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "59648a43fc3fc9b3a24800f8b383365c2c6d6bee75975d692c554da4fab6da6c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-08",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "550e66293664a31de304b074d47b387a17fb751cb99abf75f1f0c75d760cb47b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-09",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4ed9e89e510fc06e8c3fd8c408c396338535def51295c0408bc5482f9f3253f9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-10",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c78c1842a0753df34a500258a7f6b759504a5e1c718d9cbc6756e34779273ae9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-001",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "40a471b4277e181c1b0bdf3f2c5a070bd1e4044d96921e3ae3de96731af9acf1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-002",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "45a8c8e11094dd1901334211156a59e0ce7e67065bac2f5c864d812f6a8d56fc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-005",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4d64fa64d3a356727efa271c098c716283efd62945e32bd1302a9e67042c294e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-006",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "83f340ad240e9a4186843ea7bce152b56ce753a5f9e20fc781fd38de0678ac3a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-007",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f04d9f0de7e9ddfcf3c3b70957714b6ee9f5d654e8097722ff40122cfef9950c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-008",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f16837b4d8d5b421a808ef7e27ac06346d2430b4cc94bca116a5bf68907d6458"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-009",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "fb0458f62000c49c74f4055c7a02ab1bfc7c13eed0cd34859aa57043f2c6b724"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-011",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "93673ec6c2a147ed6925b2ecae4958f53a2b6ad4da32850d438bcc94c9b3a948"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-016",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "fe152237f6c69ed6bdc61e10c77861d1a67b33bf2705705030773d04b637536e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-017",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a2eb56c29d10257eefefe123ee2c8de1b875f377fd41bb563cb60968bbe3f751"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-018",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4003b021173e5511b4902fb70c0567a64632991e28d94145107242122d0ec2cc"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-019",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "398845f4781b51387eae632b61548352d1098579c2c429cdd978ab0175d1ea2b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-021",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "67d6ad88356cc268d3a6a265f7fc74fc35f3ebf4f178b73946df99d965f82f42"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-022",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "2872ddcf26440db503af947bf1781e573992b45f6c1ae0263b3d4aa4aa1e65f1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-023",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "9309dc2b70e7727c53aee3dc45fa722350afe83cd26334813cd4061da17973c9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-025",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "d55bdd0875fa27524d0bcd5fb5d1b45406386e4ce09b8d4629c50ebab0fa2d84"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-026",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "9e8a50d01c31976591bc22916fe99ff545e757bfed9446728a3592919a33dbb1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-028",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "90fd76fad324a2cb2e17e08b74758fc307e1906a93d049368194eea0dc82da06"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-030",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "28ddfc9f7e172814869be72dd41956805180bf63c94b0e6dc98f9097d1030926"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-031",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "cc57005685c23ccb3a58e96bf95e6d0d63f4d6351c32d48e7640edf2e9f898c4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-032",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "ee9e763ff315df3bd9f3fa49dd91d2b5866d67f62cb9ffee1a63c408bd591c87"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-033",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "cf36738bc83bdfdcd1515dc314b4d65700ab6368b433de7828bad205a22fd99e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-034",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a8be56d656e2c53c6045035d0d65695a38e50b30950ae09df8ae312c951ea8fd"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-035",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f165ea63272ca6d2a791933e6ba84d6bbb0573c3820945fa8e42042a052f70fb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-040",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "884df7cfd64db6ca2c35165664f00a00cc5d1e0dc3f066b9a8828791db043acb"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-058",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "147947539cbf1f5d06d1b7ef701b970f2f4c47b62e47e8afd65753371cbcbe85"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-059",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f3c871f55e2297be17ca988973efbac9fa1e79aa6f576d771e105129001f783f"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-060",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "e337fb6565b9ac352e061e6f251866e16585c19353f2023e8cbb7343380d2730"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-061",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a64f88f35045610e8d51d8216110e4b0c3790d118d874beaffeb523f9d49c2ab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-062",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "0101bcf02d29db97f3f88e53917fd9a683fb00ec4bd563a8d4956a16dd5af172"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-063",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f628647e3d7832432bb995e1a40d609bb44ce0231372d9f83430f35183d9f6d9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SB-064",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "1699809588419bd75cb5c6cf1f924933b29cc62bb8e18437d2662a3ccd67e2ab"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-13",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "19b4f68e1cba7165efd68e79cc7e6fc33cdf0813763ca3d2771e7d0927782831"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-14",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "559871867329357d85f787078959b9d73b99e6861e66290e5b2b07886f827108"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-15",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f98f864788749ca6b7c060ec75cd00f208b115217fb553dd2c5379c08cb3477c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-16",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "0a8c2fe089f716dcdefc3248a9f1d22ed0c74582c2082c49a98fd0061b1217ee"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-002",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "69d177b4007c172fb1ee9786caf77b751b27c8403866e5e1324ad76ef318cb17"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-004",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c057393b621aabfaaf34b0e28dc59e5c052b4d29f905f51f0cce90b5c4e2fced"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-005",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "eb2b26e46e1e83d891061e962a1692dbe4a7796a210e2a2c66c78fe48c80c1e5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-006",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c958b75cdd05fd1396125c6bcd26fab9b9f977d03d56bed57c6fa30963ebb48a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-007",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "b0cd8c075dd70831634d78a24c617daeb6cd7eab1a94519fe570d084862c44c6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-010",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "0923673d0435976b8e10084b76805a33e02afc6f2c365c55e0afc4593663d2c3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-011",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "274bc7ab14d7ecd6cad8901c50695579e45e6fcd65b795439a04db31cc8925f3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-014",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "3a225d90c0a1cd8a4280e70b63b8fe022bc7bf43e3a517c880b74eda7e24ade8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-015",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a3f378b0936e03604ded3c7fe6740653113ba5d007647d97e00336abaaf3535b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-017",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "13b632d6903206f42d03299a81fbfb75fec07d6c534056c2fe5fb39546060337"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-019",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "ef54adfc229a3348ee58b41b94fd0fb4be016fae8ef7551b4c0be93ad537dd1c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-021",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "fc33c9ceea9cdc4f50a0ecb1c2116e61d31831d3873523c12405b72b0b36a1b5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-023",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "db708998b0559a56da9851cc1f0fd37021d4323d9a3aedcb0f5a472f6111a189"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-025",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "68dca26fc82d9bc8b59fc2950eaad8c331e6898cfa2b30137820c1cb2f7b12ec"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-026",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "a06cab95059fdda2495030bb8d47d30551b29468ce95bda97d08e8304b27267e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-027",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "775562538126cec42327b96c6bb6dd9575fc3a047607c105aa9ad1e5daa38e72"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-028",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "d36e014c8c9601acfe8cce055b7b288d5504300410b46d09908b2e49e5a043c0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-030",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f9801996a61402ac171971912c4ea44731fca4e3b7d82e90afaa64a4acea4b0e"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-031",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "742df37d4d128bc47d5e633ebf2f0f6add20973de5b48dcde42977661d9f65e4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-032",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "3c0a71551293369b760082de2197d67c38d91fd45da626cfc84d192b1b46f9fe"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-033",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "653f2d2cd5c0a80181a8cbf805da46dc679baef67225c50002f17ff63cdb126d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-034",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "8fdecf176c0d5538f4b79b7d694c2a4f3ce9df16094375309573404aa964d365"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-037",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "fecf03be86fcee280bedbcaf2d280a0a6cf9174d5f7bd7f6efb5feb193ae35b9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-038",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "6cb88214e0facd3466519f8fc6fed5fb77231c04fd21da66351cd8399aab2e1c"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-041",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "5ef872c51ec0bce51276aff0d1cd6eab8f3005378aec3543dd2d661a01a1efca"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-042",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "fcd1b23f3170ccb7297fc53759131dcd7bcd0d260639d0945859024b5d55ccf8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-043",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "7ddbbcefc29ddfd8d62079bff078ef2afffaefba63e9f3dc1bca8f89e27b8fc8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-044",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "69143dfdd470dac6f9392695ec163a68632b7b53d304c9dbf3ca9ae12152dce2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-045",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "7d1b0bcf3836b9079cc7b0281c630ad0ce99bd75cd9c2acb4100d0f3f85707e2"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-046",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "aacf9971ddc3d7188f9a387162714c5d2530ad78126658014ff31ab3c6bbdc17"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-047",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "30a47b38174cf86466e8c826a11584fdda7f08cfdf98e54d36bd97b777d4711a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-048",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "9e8abebb98c7f0d1ff6d6b4bfdf3fcc16de427b1b58eb93ee5133756817878d7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-050",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "5f5eeb8b022f74b218bebef707f0ccab7febf2efce3a811089113d6c164571c0"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SC-051",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "ad8c9e15d85d225b73a6849b55826502f91953e45f3b81acfd985032b8e977e5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-17",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "9d9001b01f1a450472134be25ae55bc400dca623e9ff7b4454374eb2cbb3f9a8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-18",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "740120624098947341d990058c06272f4110cc076cc4a567e815777774c714f6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-19",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "704c0713538ee2af6ad74dc0d6f67e4f4f6a596df48b2b7bfd71fd6e39b0ccaf"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-20",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "1cac959584d56f4909534c484aa884bbdec10633a20740c31b155e579b43f2e7"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-21",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "ef7f74351b04ac1aa542deab4adf937d08822252738d1ecb7e9e9ba84af8ee82"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-001",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c6e3da01931d3278a2da52b74ba6a768aa66fea384ef9e822974a31515810379"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-002",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "3eafe436091201441357052097d151d0d0249b2029c727df0ac1b755e32ffe42"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-003",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "6a4e7d47ec0327ff257e52e382b6f20518f99029f5610cc1c93f49ccc783fcec"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-004",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "feec17057b75d0152e50aed688201e750b306f71ddf80d4a70d7f84d0552483d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-005",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f4585f538ee494d472b097164f5033e7b0cde824889f36754123245c8655e5b3"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-006",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "ae567684b97916beb64f9c55c1f3782f8bf4b0a24f3387703fe95b41531348a5"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-007",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "3edcf1a9712742a64a6a1cf388015b93d6b850bb10f88eb2929c6cdeeec7884d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-011",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "9f467ad19a84dcc485e60d77b5e51fe4e8c225a6915fc82066cb795fc1c8063a"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-014",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "d292742aac387ab873fe16e5e852de79c823b1ba03bc5e874a11e141cc0c51e6"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-020",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "1d22c348f6e70a0cb1c4bdef0e0909cf542485113f9d261e34d5ac47e55c7bb9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-030",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "c1efe4b8277be467dcc2217c169309e81fb7fbc3bcaeef5e747c269eb8a8cad1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-040",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "0f1ae4f8228891c82e38242bb8c1e41dda6b4bdda9f044d6fa467b52ed85aab4"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-043",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "f22748179d556a90dd19806b4228f39de4f4ddffa1a27e98daffbb29ea20971d"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-051",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "de3c92a60893db74d07f9d7c19008d1530a454a5a509794ab6c33809338213f9"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-053",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "4adbe7edc489cdb5565f1109ab93c99adf074a55f0375729f9909d3c94c57bd8"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-065",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "69a920d827a5ade6b2afa744a4d7c234692da1927050fcfa1bf8797465cf5fd1"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-060",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "262a775fa32c5e1be216c8fc8da78c76ddd19354e60ce5c1a9571857b0a7018b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-061",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "971b33b16ec68b0f3c40096497ce7ca9521f8adf230306466a9e3fe9d8b3011b"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-070",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "23a3bc408f5dfa607182b81ceb63820b39b0338bc824806476c93243d6173e51"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-071",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "6f69ef90cf267a14f693d723d7c8e1586faa55b99cc0b55a6492444f85603401"
    },
    {
      "depth": "A",
      "status": "geprüft",
      "id": "P-SD-072",
      "evidence_review": "Lead concurrence: all assigned document findings are A/geprüft for every source of the claim (evidence_items sub-contributions read individually; shared claims carried jointly by all sources); statement, Aussageursprung, event date/status (order vs delivery vs use, manufacturer statement kept visible) and product assignment compared with the findings; no higher status than the sources support. Remaining minor wording notes are in the document findings.",
      "fingerprint": "16bf3f9e40b460bf7a703c708ae9e01c182dc4dcd039dfa5067c749efd7e871c"
    }
  ],
  "missing_decisions": [],
  "fact_review": {},
  "input_fingerprint": "d322fd0ac16315d38c6b8d7bb6e38742e932cd82ca6790a6d5a38efd22c72a6b"
}
```
