# Review

```json
{
  "schema_version": 1,
  "run_id": "2026-10-10-rheinmetall",
  "company": "Rheinmetall AG",
  "as_of": "2026-10-10",
  "phase": "final",
  "status": "freigegeben",
  "status_begruendung": "Runde 2: 26 geänderte Interpretationen gezielt geprüft, S-WEA-03 gestrichen (MF-2 erledigt); MF-1 (einheitliche Matrixregel in shared_limitations, I-MX-14/38/44 regelkonform) und MF-3 (S-OPP-03 abgeschwächt) behoben; nicht wesentliche Korrekturen (S-WEA-02, S-THR-01, I-RG-01) und Hinweise umgesetzt. 53 unveränderte Urteile übernommen. Keine offenen Fehler.",
  "pruefumfang": {
    "eingaben": [
      "work/positioning.json (68 I)",
      "work/positioning-context.json",
      "work/swot.json (12 S)",
      "work/swot-context.json",
      "work/review-basis.md (freigegeben, 176 Claims)",
      "work/review-packet.json",
      "work/comparison-plan.json",
      "work/interpretation-validation.json (errors [], 80 Fingerprints)"
    ],
    "methode": "Jede depends_on-Kette gegen das Basis-Review abgeglichen (alle Fakt-Abhängigkeiten depth=A, geprüft/übernommen – lokal kontrolliert); Ableitung, Anker/Skala, Aussageursprung, höchste belegte Stufe und Begründung der nächsthöheren, Unsicherheit und SWOT-intern/extern geprüft. Keine Neurecherche unveränderter A-Fakten.",
    "mechanisch": "interpretation-validation.json: mechanischer Pass, keine Inhaltsfreigabe.",
    "runde_2": "interpretation-validation.json (79, errors []) vs. -r1: 26 geändert, S-WEA-03 entfernt; nur geänderte Interpretationen und abhängige SWOT-Punkte geprüft (unveränderte S-STR-01/S-STR-02/S-THR-03 hängen nur an unveränderten I-Claims)."
  },
  "material_errors": [],
  "weitere_korrekturen_nicht_wesentlich": [],
  "hinweise_nicht_blockierend": [
    "Hauptagent/HTML: nicht-kumulativen Anker 5 gulf_access (Barzan I-MX-46) und Matrixregel (a)–(c) aus shared_limitations im Deep Dive anzeigen.",
    "RR-08 (EDGE C-UAS-Zielspektrum) und RR-S-04 (AGG-48-Güterumfang) offen, nicht blockierend.",
    "S-STR-03: Backlog belegt Auftragsbestand, nicht Lieferfähigkeit (Formulierung optional schärfen)."
  ],
  "besondere_pruefpunkte": {
    "I-MX-15": "Stufe 3 vertretbar, Auslegung konsistent mit NASAMS-Kuwait (Raytheon/FMS) und Rheinmetall-GDELS; aber dieselbe Auslegung muss für cuas_evidence (I-MX-14) gelten – dort inkonsistent (MF-1).",
    "I-MX-02/03/04": "Stufe 5 jeweils durch Kunden-/Behördenmaterial getragen (ukrainische Luftwaffe; katarisches MoD-Video, SPA-Foto); Herstellerangaben nur ergänzend.",
    "I-MX-46 Barzan": "Formal ankerkonform über lokale Fertigung mit Kundenbezug (Unternehmensangabe), Vorbehalt dokumentiert; Skalenhinweis an Hauptagent.",
    "I-ES-05": "Lieferroute Italien in uncertainty als Schlussfolgerung gekennzeichnet – in Ordnung.",
    "I-ES-06/S-WEA-03": "I-ES-06 sachgerecht; S-WEA-03 überzogen (MF-2).",
    "S-OPP-03": "Abschwächung nötig (MF-3); Faktenbasis belegt nur „bestimmte Güter der Luft- und Seeverteidigung“.",
    "S-STR-02/S-WEA-02": "S-STR-02 korrekt begrenzt; S-WEA-02 Zeitbezug der Vorjahreswerte (Fußnote 6) korrigieren.",
    "SWOT_intern_extern": "S/W intern, O/T extern korrekt zugeordnet; S-THR-03 (Partnerverhalten EDGE) als extern vertretbar."
  },
  "nachpruefung": "Nach Korrektur nur die geänderten I-/S-Claims und davon abhängige SWOT-Punkte (S-STR-03 bei Änderung I-MX-Regel nicht betroffen) gezielt prüfen; unveränderte 73 Urteile übernehmen.",
  "claims": [
    {
      "id": "I-ES-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "eac0dacaae35a39f9b3b99f060d9947de3968b5ec200a505fba636a9a723f622"
    },
    {
      "id": "I-ES-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "0ab380981e3bf433b8235cb0a438068b9fde22924efc0b1ce0648c638ea99c17"
    },
    {
      "id": "I-ES-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "c2309665b565c88cd179e252abd449737903898ca8b6406e0fbc5c9afcef3575"
    },
    {
      "id": "I-ES-04",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: EDGE als Soft-Kill laut CEO, Barzan als eigenes C-UAS-System – konsistent mit Matrixregel.",
      "runde": 2,
      "fingerprint": "a99e77a6808af1f8a188a744883943a4ad32aa4914219bbd1dfed76a9fb74ab7"
    },
    {
      "id": "I-ES-05",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: „bestimmte Güter der Luft- und Seeverteidigung“; Italien/Deutschland-Route als Schlussfolgerung gekennzeichnet.",
      "runde": 2,
      "fingerprint": "c2a952fd8f8c74b1e775a816c1cbff1eece15fdcfc98414256e45d3d9e3a3b5c"
    },
    {
      "id": "I-ES-06",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Geprüft: Köhne korrekt als nur fachmedial berichtet, Dürr-Abgang bestätigt (H-DUE-03), Register ohne Wechsel (H-DUE-02, Stand SHAB 07.07.2026), Bewertung als „plausibel, nicht primär bestätigt“ sachgerecht. Keine Schwächezuschreibung – passend.",
      "fingerprint": "f3790cd73e03602bb0576c6474d3420bfec6b6f5ce6647e8cf50ba82f3f1dcdf"
    },
    {
      "id": "I-FA-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "2f5d56f8def12e15f4a5c416ce8a819b702b72459f8da8e2dfab6c038251203c"
    },
    {
      "id": "I-FA-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "4e2791bf3c493553608c5711cd166b3ef5c67294ae752e5925528cb41fbc21a4"
    },
    {
      "id": "I-FA-03",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Neuss jetzt als Plan; belegte Rollen Schweiz/Italien korrekt.",
      "runde": 2,
      "fingerprint": "b288165651ff40762e2491d771f076560d3cc01f10808683fa81fd5d4cf41685"
    },
    {
      "id": "I-FA-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "e2de897fa88adc7c147c930621964cef48785bcf1e3e3beec1739a141c2d30ef"
    },
    {
      "id": "I-GS-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "37f9b194a7098da66d5f88231ae3431d0a3de88dc6564fd68de856ab6d67dd41"
    },
    {
      "id": "I-GS-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "cf40853dda00b2fd7f3051d20c3fb1538e488ac575347770226c0696d2c735e6"
    },
    {
      "id": "I-GS-03",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: „stark vertreten“, Marktanteile als nicht belegt ausgewiesen.",
      "runde": 2,
      "fingerprint": "20be88d89a1067092c239f8b4ca07a685c7545545529a9ffc9d07c5c71970033"
    },
    {
      "id": "I-GS-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "23d87de473846696d69fb33195f2b225544bd3d15cb4c204e3070d840193ff02"
    },
    {
      "id": "I-GS-05",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Kuwait als Herstellerangabe 2013 gekennzeichnet.",
      "runde": 2,
      "fingerprint": "3a20c00e24be8d5c63123273d0cebc53da823c2aa49516c5c1ca4a69af68b5bb"
    },
    {
      "id": "I-GS-06",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Zeitfolge SECO 2025 vor Bundesratsentscheid korrekt.",
      "runde": 2,
      "fingerprint": "061a1497510d69d1b4cd4a096395b3da6d605a6878560e6b14ca53b5bc2ceb62"
    },
    {
      "id": "I-PF-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "a061f3ad736577b4d301bf67e1aba3e3735f4aff7477d74df19528e28eb66811"
    },
    {
      "id": "I-TE-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "7fa6afb2e025c6d29e73e927be40e521f55a75f35570a49e341a0e82524d04c5"
    },
    {
      "id": "I-NW-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: depends_on um M-PEER-EOS-01/-02 ergänzt; keine Kooperationsableitung.",
      "runde": 2,
      "fingerprint": "b8ae4094d1a14de76606f3b99d4398a5cb5e3be674868fcc56b837286d6d08f9"
    },
    {
      "id": "I-RG-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Trendbehauptung entfernt, Europa als belegter Schwerpunkt, Golf als Unternehmenspotenzial.",
      "runde": 2,
      "fingerprint": "9d2ed53596a690a96da6e052892c81b083392848c7a42d85eaab7ec1064c5821"
    },
    {
      "id": "I-MX-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "cdac7a3a5b8b2270d2621bce9dc8aea6621535138fad9aa3b46453c67d339a70"
    },
    {
      "id": "I-MX-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Geprüft: Stufe 5 trägt allein Kunden-/Behördenmaterial (Video der ukrainischen Luftwaffe, M-RHM-CUAS-01); P-SKX-06/-08 und M-RHM-GULF-01 nur als Kontext/Gegenbefund. Oberste Stufe, Einsatz statt Wirksamkeit korrekt abgegrenzt.",
      "fingerprint": "692e2401c1df21ca7935910a4fb8c9938c829a1aee120de3b4b4c35241dd3234"
    },
    {
      "id": "I-MX-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Geprüft: Stufe 5 trägt Katar (MoD-Video, Rheinmetall-Bestätigung via Janes) und Saudi-Arabien (SPA-Foto via Janes) als mehrere staatliche Kunden; Italien/Europa ergänzend als Herstellerangaben. Peer-Zeile bündelt Skynex/Skyranger/Skyguard – Skyguard-3 zählt laut Peer-Label.",
      "fingerprint": "bf2643642f45f1fa9e864f979e10802213b65011bc096154a1aa8ae11172c96d"
    },
    {
      "id": "I-MX-04",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Geprüft: Stufe 5 über Betrieb in zwei GCC-Staaten (Katar, Saudi-Arabien) aus Behörden-/Kundenmaterial; Kuwait und 150 Systeme korrekt nur als Herstellerangabe; Hinweis auf Altbestände sachgerecht.",
      "fingerprint": "a89adfd08f9f56b50fe8aba5faaf71ed1efdfa1fe7ac65e567e54bb9368a3ba7"
    },
    {
      "id": "I-MX-05",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "dfcfc58f083dcfc7607e9674d3b55b7a311244ae4be177791939bed12c09065d"
    },
    {
      "id": "I-MX-06",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: belegte Standorte Zürich/Rom, Neuss nur als Planbestandteil – Hinweis R1 umgesetzt.",
      "runde": 2,
      "fingerprint": "44a1471b9de2194f33f14367867046b34c4ccbeee6bcaf372292fc3bdace148a"
    },
    {
      "id": "I-MX-07",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "ea830a9eab432d919defd7e10b1357df4bdcdbd9db211377a14923381b22d133"
    },
    {
      "id": "I-MX-08",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "77c3d0d623444ec207f7e2d2b486e391d92e220e7b2685f48d77aa51d24d7078"
    },
    {
      "id": "I-MX-09",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "0a5eaaabb0f9c81354280b73a7ddaee7e236eea3541322cf34c7482db37b8cac"
    },
    {
      "id": "I-MX-10",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "c6f82534dda8c4a175a43d018de501bc087c4ffb5761693da2e52843c20ee2dc"
    },
    {
      "id": "I-MX-11",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "12cf9b9e96e4adb2a84bf5c20dadb5a17a85ea649112c4020a0a6212242ecd8f"
    },
    {
      "id": "I-MX-12",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "844be1ee1c8f44d2a296693b1fbe4ec26a9f068bb9f469f61a843aafa2ca6b2b"
    },
    {
      "id": "I-MX-13",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "bdb8bbfe0b0c24e00d073ba011a510719ed2ce2d5ad0733731c0b90d88d6d82b"
    },
    {
      "id": "I-MX-14",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Stufe 1 regelkonform (Regel c): EOS-01 nennt Slinger ausdrücklich als Drohnenabwehr-Waffensystem; M-PEER-EOS-05/-07 enthalten keinen ausdrücklichen C-UAS-Beschaffungszweck, Gen5 keine belegte Streitkräftebeschaffung. MF-1 behoben.",
      "runde": 2,
      "fingerprint": "99157dd934a777a72394fd1d44bef74096c360cc0e537779a3dd96a595db9652"
    },
    {
      "id": "I-MX-15",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Stufe 3 nach Regel (a) mit Kennzeichnung (b); Regel in shared_limitations einheitlich formuliert (NASAMS/Raytheon, Rheinmetall/GDELS, EOS).",
      "runde": 2,
      "fingerprint": "7cd2feddf66d5712be3e92dce6185b7d665575c7b425f7fc7d783bd922cd6258"
    },
    {
      "id": "I-MX-16",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "d4507ce6d23aa83c0f67ffc8b0a4dbb0102b495896f172e66aa36da0aaa089d9"
    },
    {
      "id": "I-MX-17",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "79f0f609c4f36615e32943c7487ae1619b937d65bff5d04b003fdecc57a387ba"
    },
    {
      "id": "I-MX-18",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "22f394bf98853b1d9db1b43a0968fbe613049fbd4d5918de5f23284d6ca704fc"
    },
    {
      "id": "I-MX-19",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "c95c29b25cc7ae0f4cc113468d97b012e851164f110f4b3b1ea12d3818c0287c"
    },
    {
      "id": "I-MX-20",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "9c04509ea1ff560023a469a6a94ed7adac4e27cdc67d99d02090a087e25d6203"
    },
    {
      "id": "I-MX-21",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "db5c5c612b144c1efe825122f2908164459b62e2f3a86c39a214c45e891479af"
    },
    {
      "id": "I-MX-22",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "8a6db9ccfeae4e11423a4fc3a5aa1d188e5a83832661a1965fc0993b8a1daa0e"
    },
    {
      "id": "I-MX-23",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "24d099a43944d660a5e29f54e5162113bb31a40aebcdf073f23009883f2b5d1e"
    },
    {
      "id": "I-MX-24",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "644a6e8a8e932392d454df67972255582536ce94e31ed36b6975f64c8ec9edc2"
    },
    {
      "id": "I-MX-25",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "602ed26baf0bbca39a0c6ee5630fd1fe6b1543f2fcbb095cf877d06454f2d510"
    },
    {
      "id": "I-MX-26",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "8844ffdbbaacaf6c6c60a3d220d7689c8438ea00f304d5408ce7ac7ae73cb401"
    },
    {
      "id": "I-MX-27",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "32c9fca072595225a0ca50ba0a7792e21964b7624e096b6372702a00145a850f"
    },
    {
      "id": "I-MX-28",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "900a314e4fe571723eac58ad6274fcdda0247af4b6c3402d28a58177ea54148e"
    },
    {
      "id": "I-MX-29",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "beff0ffe3b6f8e640b7c0ce5fef2e2f6f0561d9d789e4dac3126f5376b18709c"
    },
    {
      "id": "I-MX-30",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "3a19d4694e39e4c7fb97e5940513e94423d47f91102cdf8c226b734b52a9a4a4"
    },
    {
      "id": "I-MX-31",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "321a79533ec1022128e7eb465ad30665522457df642e72ab93e01372cc956348"
    },
    {
      "id": "I-MX-32",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "df9b4f6c283b02d884d73d1ebb8d4f98c1dbacf72d09a573b49e0467ae025d45"
    },
    {
      "id": "I-MX-33",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "bc09cdf749db7cb0f0630ec67e02ce16ec93a8897836a39f0a2f9d9c1022ad72"
    },
    {
      "id": "I-MX-34",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "d5a2a0544dd154c1e4b836c4e7707903ed20b7011478844a34cd4111dc427ed1"
    },
    {
      "id": "I-MX-35",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "6f9bce1f72c1da148e3080ea76dde9611abeb41c696e0dbbd6b731d04090c62e"
    },
    {
      "id": "I-MX-36",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "9743cb5a11160a36656687b92f12ca30ce9ab5b0dc31e96490788f09b6ddb6f2"
    },
    {
      "id": "I-MX-37",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Profil korrekt; SKYSHIELD-Zielspektrum als nicht genannt ausgewiesen.",
      "runde": 2,
      "fingerprint": "ef2367a424709cf4f817df7ba1bf22d1021ba57c89b1249d824f981a6d027971"
    },
    {
      "id": "I-MX-38",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: „nicht öffentlich belegt“ regelkonform (M-UAE-EDGE-03 nennt Soft-Kill-Einsatz ohne ausdrückliches C-UAS-Zielspektrum), value=null, coverage_note und RR-08 vorhanden, keine Fähigkeitsaussage. MF-1 behoben.",
      "runde": 2,
      "fingerprint": "46c3aa146e07675ba6b9dea7258ac379f2a06301152101f7f4260afff8c9fcd1"
    },
    {
      "id": "I-MX-39",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Stufe 4 nach Regel (b), Herstelleraussage gekennzeichnet; konsistent zu Barzan/EOS.",
      "runde": 2,
      "fingerprint": "8911de784ba5b28637794c1644e0eedfc19f219e33d1d75aa1f49ff67b8de9ee"
    },
    {
      "id": "I-MX-40",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Stufe 4 nach Regel (b), gekennzeichnet; Stufe 5 korrekt nicht vergeben.",
      "runde": 2,
      "fingerprint": "6a75a6010810b5d475c2a2b37fcf6645dff59e9c63b4354b88e4ce7a8449acc7"
    },
    {
      "id": "I-MX-41",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "b7dbae20b34d42569f46441dcee42dd14712951f8f30b477340ca12256abaab6"
    },
    {
      "id": "I-MX-42",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "2c46f70c69e117ddca9f83f63146b342e20d762a9366f058ae3c29bd8c29213d"
    },
    {
      "id": "I-MX-43",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "14be277bb3d8cf5b4a7e1929dfeb23b2cfdb5b1fa92716248f75e5bb6a4eaa4a"
    },
    {
      "id": "I-MX-44",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Stufe 4 nach Regel (b)/(c) – ausdrücklicher C-UAS-Vertrag mit Katars Luftverteidigung laut Unternehmensangabe, gekennzeichnet; Stufe 5 korrekt ausgeschlossen.",
      "runde": 2,
      "fingerprint": "4491842caa5265163c5110619f6b3b7200d87486848c58d88b2824749c8863bd"
    },
    {
      "id": "I-MX-45",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Stufe 3, Unternehmensangabe gekennzeichnet; Stufe 4 korrekt ausgeschlossen (Auslieferung 2027 erwartet).",
      "runde": 2,
      "fingerprint": "27cd3ece6a2b994fa73f581735a72b7d2a0b409f05540d2fe2389234b11fe6b3"
    },
    {
      "id": "I-MX-46",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Stufe 5 über Ankerpfad lokale Fertigung mit Kundenbezug, Regel (b) gekennzeichnet; Vorbehalt (keine Lieferung, Heimatmarktrolle) korrekt. Skalenhinweis an Hauptagent bleibt (HTML-Erläuterung).",
      "runde": 2,
      "fingerprint": "6f31a6fbb0cbcc283519aa3cfb276c35739c61584df8a29fcac8d55798566834"
    },
    {
      "id": "I-MX-47",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "34756dc998f0cf3e9c607b7868918c10ab6e81adfeeee51e28f0e3cb7ad818cc"
    },
    {
      "id": "I-MX-48",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Ableitung gegen depends_on (A, geprüft/übernommen im Basis-Review) geprüft: Aussage, Aussageursprung, Kriterium/Anker bzw. Profil, Unsicherheit und Status sachgerecht.",
      "fingerprint": "c04001ad0cae50e4124b1190aedf4a912549afc98c6cf3b22b64dccf56b164a8"
    },
    {
      "id": "S-STR-01",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Geprüft: Bestand Katar/Saudi aus Behörden-/Kundenmaterial, Kuwait als Herstellerangabe; Ableitung Anschlussgeschäft als Interpretation erkennbar.",
      "fingerprint": "57ca498f36a625eab6cb6dc884828133cdbeba6a2923dc118ae493dcfd289481"
    },
    {
      "id": "S-STR-02",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Geprüft: Strukturen (RBAT 49 %, RADARABIA 20 %, RAST 100 %, Töchter) korrekt; Stärke ausdrücklich auf Struktur, nicht nachgewiesene Wertschöpfung begrenzt. Hinweis: RAST ohne belegten Flugabwehrbezug – nur als allgemeines Lokalisierungsvehikel nennen.",
      "fingerprint": "2bf43fec6157e461f7450829977ceb3d86f8198b5bf72bc638bf4bd87e8c583f"
    },
    {
      "id": "S-STR-03",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Fertigungsrollen Zürich/Rom belegt, Neuss als Plan; Stärke als Interpretation erkennbar (Hinweis: Backlog ist Auftragsbestand, nicht Lieferfähigkeit – nicht blockierend).",
      "runde": 2,
      "fingerprint": "aed666c11236666b7cddb3171278ae01a7353955d5df5658ce4106c510896170"
    },
    {
      "id": "S-WEA-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Angaben verschiedener Sprecher mit Datum getrennt; interne Grenze sachgerecht.",
      "runde": 2,
      "fingerprint": "611fc3c513599d7627a63897e0d1b9347a2827579a704de43c98fe26aea8f583"
    },
    {
      "id": "S-WEA-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Werte mit Vorbehalt der Berichtsperioden (Fußnote 6), keine Jahresreihe behauptet.",
      "runde": 2,
      "fingerprint": "2ec4ce832792f25f308b0f5618cb42df41590c7cb7ef92dbfdbb33d967a9754e"
    },
    {
      "id": "S-OPP-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: unverändert sachgerecht (extern, Status Lieferungen korrekt).",
      "runde": 2,
      "fingerprint": "814de2abc778f5b633ccd45585a03ba7df4afab08bf678793236ef6f0bc02e4e"
    },
    {
      "id": "S-OPP-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: unverändert sachgerecht; Übertragbarkeit als Interpretation.",
      "runde": 2,
      "fingerprint": "6603f2ab7a042ec303a9f2e1424592cd62abc91dedc6f0b775328971970ba70a"
    },
    {
      "id": "S-OPP-03",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: auf belegten Kern abgeschwächt, Erfassung von Rheinmetall-Gütern offen (RR-S-04), Italien-Prämisse entfernt. MF-3 behoben.",
      "runde": 2,
      "fingerprint": "b8db0d2fa83e232d47fb45f81cdfe8510f77d7378ec87f77f890a0a73c4d2220"
    },
    {
      "id": "S-THR-01",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: Barzan-Status (Vertrag 2023, Auslieferung 2027 erwartet) korrekt.",
      "runde": 2,
      "fingerprint": "13dd49b500b04a89c6d7ece42b83c03e03702b5f875f37201b545a894f178965"
    },
    {
      "id": "S-THR-02",
      "depth": "A",
      "status": "geprüft",
      "pruefnotiz": "R2 geprüft: unverändert sachgerecht.",
      "runde": 2,
      "fingerprint": "9e56e51a1176eafd1ae63eddf2e0af1fec072b0ad552f2b996b68d457cdbe990"
    },
    {
      "id": "S-THR-03",
      "depth": "A",
      "status": "übernommen",
      "pruefnotiz": "Unverändert (Fingerprint identisch R1); Befund R1: Geprüft: extern (Partnerverhalten); Belege M-UAE-EDGE-03, C-TI-08, P-SR30-10 korrekt eingeordnet.",
      "fingerprint": "0adc8746ce752c94bb6af3fc9ea0956aed6adf223c69d99d6d5c0bda433a3a30"
    }
  ],
  "runde": 2,
  "material_errors_r1_erledigt": [
    "MF-1",
    "MF-2 (S-WEA-03 gestrichen)",
    "MF-3"
  ]
}
```
