# Abnahme – Rheinmetall AG, Lauf 2026-10-10-rheinmetall

Stichtag 2026-10-10 · Modus facts-v2 → interpret-v2 → Renderer v2 (`--full`)
Ausgabe: `output/briefing.html` (720 KB, offline, keine externen Assets)

## Auftrag
Themen (Nutzerreihenfolge): 1. Flugabwehr, 2. Markt und Marktzugang in den Golfstaaten.
Gesprächspartner: „aktueller Hauptverantwortlicher für Rheinmetalls Flugabwehrgeschäft“
(Nutzerangabe als Rolle). Ermittelt: **Roman Köhne**, laut Fachmedium (esut.de, 04.09.2026)
seit 01.10.2026 CEO der Division Air Defence – **angekündigt, nicht primär bestätigt**
(keine Rheinmetall-PM, kein Registereintrag). Vorgänger Oliver Dürr (PM 24.06.2026 primär
belegt, Abgang laut NZZ 10.10.2026). Governance-Ebene: CEO Armin Papperger ist VR-Präsident
der Rheinmetall Air Defence AG. Profil enthält nur berufliche H-Claims.

## Tatsächlich ausgeführte Rollen
| Schritt | Rolle | Ergebnis |
|---|---|---|
| Fakten | company-context-analyst | context-facts.json (36 Claims), Status teilweise |
| Fakten | portfolio-analyst | portfolio-facts.json (43 Claims), Status teilweise |
| Fakten | cluster-analyst | cluster-facts.json (40 Claims, Netzwerk 38 Knoten / 47 Kanten), teilweise |
| Fakten | market-facts-analyst | market-facts.json (57 Claims, 8 Peers, Vergleichsplan v1), teilweise |
| Basis-Review | source-reviewer | 4 Runden; Runde 1: 6 Materialfehler (RAST-Anteil, Schwer historisch, Golf-Bestandszahl, Aussageursprung Skynex/Ukraine, RPDC-Vorjahresbeleg, Revolverkanone 30/35 mm) → von den Rollen korrigiert; Runde 2–4 freigegeben |
| Gezielte Nachrecherche | market (RR-02) | 4 neue EOS-Slinger-Claims, in Runde 3 geprüft |
| Positionierung | positioning-analyst | 68 I-Claims (6 Executive Summary, 48 Matrixzellen: 39 bewertet, 9 nicht öffentlich belegt) |
| SWOT | swot-analyst | 11 S-Claims (3/2/3/3) |
| Schluss-Review | source-reviewer | Runde 1: 3 Materialfehler (uneinheitliche C-UAS-Matrixregel, Führungswechsel als Schwäche, unbelegte AGG-48-Prämissen) → korrigiert; Runde 2 freigegeben (79 Interpretationen, alle A) |
| Rendern | Hauptagent, scripts/render-briefing.py | keine eigenen Fakten/Interpretationen, keine LLM-HTML |

Zwei Korrekturrunden wurden je Phase nicht überschritten; keine offenen Materialfehler.

## Prüfstatus
- **Inhaltsprüfung Basis:** 176 Claims, alle Prüftiefe A (39 in letzter Runde geprüft,
  137 aus Vorrunden übernommen). Alle 47 Netzwerkkanten im Originalbeleg geprüft.
  Die 34 ursprünglichen B-Claims der Kernansicht wurden vor dem Rendern vom Prüfer
  nach A hochgestuft (8 davon gezielt nachgeprüft). Kein Claim „nicht einzeln geprüft“.
- **Inhaltsprüfung final:** 79 I-/S-Interpretationen gegen depends_on geprüft.
- **Mechanisch:** prepare-facts 0 Fehler (176 Claims, 143 Quellen); check-interpretation
  0 Fehler; stamp-review für Basis und final. Mechanischer Pass ist keine Inhaltsfreigabe.
- **HTML:** 50 unittest-Tests OK; DOM-Laufzeittest (Kopie mit an echte IDs angepassten
  Fixture-Assertions) bestanden; Chromium/Playwright: keine JS-/Konsolenfehler (Desktop
  1366 px, Mobil 390 px), keine horizontale Überbreite mobil, 0 defekte interne Anker,
  446 externe Quellenlinks (nicht einzeln angeklickt), Druck-PDF erzeugt (174 Seiten,
  Details ausgeklappt).
- **Layoutkorrektur:** Mobil lief der Netzwerk-Statusfilter wegen langer Statuslabels
  136 px über; CSS in `references/templates/cluster-network.html` (min-width:0 für
  Toolbar-Label/Select) korrigiert, danach 0 px Überbreite.

## Öffentliche Datenlücken (im Briefing sichtbar)
- Köhnes Amtsantritt nur über Fachmedien belegt (RR-01).
- Kunden der Skynex-Aufträge 2019 und Q2-2026 offiziell ungenannt; Katar-Zuordnung
  nur laut Janes/Messebericht; Golf-Lieferungen ab 08/2026 nur Herstellerangabe (RR-04).
- Rund 150 kanonenbasierte Systeme in der Golfregion: CEO-Angabe (Q1-Call), nicht unabhängig.
- Betriebsstatus RADARABIA (Dschidda) und RBAT (Katar) unbelegt (RR-05).
- Schweizer Einstufung der Golfstaaten / Bewilligungen für Rheinmetall Air Defence AG offen (RR-06).
- Ob Rheinmetall-Flugabwehrgüter unter die deutsche AGG 48 fallen, offen (RR-S-04).
- Korkut-Golfverträge nur anonym berichtet (RR-03); NASAMS-Status Katar/Oman (RR-07);
  C-UAS-Rolle EDGE SKYSHIELD (RR-08). Alle nicht blockierend.
- Kein Geschäftsbericht öffentlich gefunden für Denel, EDGE, Barzan, SAMI/MAZ.

## Bekannte kleine Restpunkte (nicht blockierend, vom Prüfer benannt)
- M-SAU-RHM-01: Unsicherheit nennt „Times Aerospace“ als m²-Quelle; im Paket ist die
  zweite m²-Quelle Aviation Week.
- S-STR-03: Backlog belegt Aufträge, nicht Lieferfähigkeit (Formulierung optional schärfbar).
- Matrix Barzan/gulf_access Stufe 5 wird über den Ankerpfad „lokale Fertigung mit
  Kundenbezug“ ohne Stufe-4-Lieferung erreicht (in der Zellbegründung erläutert).

## Nicht geprüft
Externe Quellen-URLs im HTML nicht automatisiert auf Erreichbarkeit geprüft; Touch-
Bedienung nicht getestet; keine reale Token-/Kostenmessung. Paywall-Inhalte (Bloomberg,
NZZ, Tactical Report, Janes-Teile) nur soweit frei sichtbar verwendet.
