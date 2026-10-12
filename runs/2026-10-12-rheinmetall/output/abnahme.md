# Abnahme – Rheinmetall · Flugabwehr & Golfstaaten (Lauf 2026-10-12-rheinmetall)

Stichtag 2026-10-12 · Modus facts-v2 → interpret-v2 → v2-Renderer (`--full`)
Ausgabe: `runs/2026-10-12-rheinmetall/output/briefing.html` (offline, 1,8 MB, vier Seiten)

## 1. Tatsächlich ausgeführte Rollen
| Schritt | Rolle/Agent | Ergebnis | Status |
|---|---|---|---|
| Fakten | company-context-analyst | work/context-facts.json – 28 Claims (T-, H-), Personenprofil | teilweise |
| Fakten | portfolio-analyst | work/portfolio-facts.json – 59 P-Claims, 22 Produkte | vollständig |
| Fakten | cluster-analyst | work/cluster-facts.json – 43 C-Claims, Netzwerk 43 Knoten / 54 Kanten, report_log | teilweise |
| Fakten | market-facts-analyst | work/market-facts.json – 51 M-Claims, 7 Peers, 33 Matrixbeobachtungen (Plan v1) | teilweise |
| Basis-Review | source-reviewer (Phase basis) | work/review-basis.md – 181/181 Claims A „geprüft“, freigegeben | freigegeben |
| Positionierung | positioning-analyst | work/positioning.json – 83 I-Claims (35 Matrixzellen, 22 Reifeeinordnungen, 6 Kernaussagen, 3 Highlights, Themen, Regionen) | vollständig |
| SWOT | swot-analyst | work/swot.json – 11 S-Claims (3/2/3/3) | vollständig |
| Schluss-Review | source-reviewer (Phase final) | work/review-final.md – 94/94 I-/S-Claims A „geprüft“, freigegeben | freigegeben |
| Ausgabe | Hauptagent, scripts/render-briefing.py | output/briefing.html | gerendert |

„teilweise“ bei Faktenmodulen bedeutet dokumentierte offene Suchwege bzw. nicht zugängliche Quellen (siehe gaps/coverage), keine ungeprüften Claims.

## 2. Korrekturrunden
- Formal: 12 Quellen-Metadatenkonflikte zwischen Modulen von den Eigentümerrollen angeglichen.
- Basis-Review Runde 1: 2 Materialfehler (C-024 Gültigkeit AGG 48 → verlängert bis 15.09.2027; M-SAAB-001 RBS 70 vs. RBS 70 NG) und 5 Korrekturen (T-05, T-27/Event-Datum, Toolbox-Zuordnung, Cluster-Sektion C-026, MBDA-MICA) → behoben, neu T-13 (Air Defence 2025 pro forma 769 Mio. EUR). Gezielte Nachprüfung.
- Hochstufung: 37 in Ansichten verwendete B-Claims nach A; P-SNX-10 korrigiert und nachgeprüft.
- Positionierung: I-AD-05 nannte zunächst Dürr als Leiter (Kontext ohne H-Claims) → Kontext mit H-Claims neu erzeugt, korrigiert (Köhne).
- Schluss-Review Runde 1: 1 Materialfehler (I-ES-02 Headline Ziel/Ist) + 10 Korrekturen → behoben; Runde 2: I-PM-skyguard → behoben. Abhängige S-Claims gegen neuen I-Wortlaut geprüft.

## 3. Gesprächspartner
Roman Köhne – CEO der Division Air Defence (Sitz Zürich) seit Oktober 2026 laut Rheinmetall-Karriereseite; Übernahme zum 01.10.2026 als Nachfolger von Oliver Dürr laut ES&T (04.09.2026). Grenzen: keine datierte Rheinmetall-Pressemitteilung; Organfunktion bei der Rheinmetall Air Defence AG im Handelsregister nicht belegt (letzter Stand 07.07.2026); frühere Stationen ohne Jahreszahlen; kein belegter persönlicher Golfbezug.

## 4. Mechanische Prüfungen
- prepare-facts.py: 0 Fehler (181 Claims, 162 Quellen); check-review-data.py: Exit 0.
- stamp-review.py basis/final: Fingerprints ergänzt; keine Inhaltsfreigabe durch das Skript.
- check-interpretation.py positioning/swot/merge: 0 Fehler (94 Interpretationen).
- render-briefing.py --full: erfolgreich (alle Ansichten nur aus aktuellen A-Fakten).
- `python3 -m unittest discover -s tests`: 77 Tests OK (Repository-Code unverändert).

## 5. Desktop-Browserprüfung (Chromium headless, offline)
Ausgeführt mit einer laufbezogenen, datengetriebenen Variante von tests/check_design_browser.cjs (Scratchpad), da das Repo-Skript feste Zählwerte des fiktiven Demos erwartet (2 Produkte) und daher hier nicht anwendbar ist.
- Bestanden: vier Seiten (Überblick, Gesprächspartner, Markt-Deep-Dive Golfstaaten, Quellen); kein horizontales Scrollen bei 1440/1280/1024 px; Module untereinander; Portfolio 22 Produkte, Filter/Tabelle/Reset, Profile geschlossen, Produktklick öffnet Profil mit Quellenlink; Netzwerk 43 Knoten, 53 Akteurspaar-Linien = 54 Kanten, gerade Linien, Detailspalte rechts, Tastaturauswahl, Suche; Matrix 35 Zellen mit Dialog; Personenprofil mit Belegsprung; Quellensuche (275 Claim-Details, 402 externe Links); keine kaputten internen Anker; Druck öffnet alle Details und stellt Zustand wieder her; ohne JavaScript 4 Seiten und Netzwerktabelle; keine JS-Fehler; keine externen Netzabrufe.
- tests/check_executive_browser.cjs (Repo): bestanden (6 Karten, 1440/1280/1024, Dialog, Quellen, Ereignisse, Druck, ohne JS).
- Nicht geprüft: Erreichbarkeit der externen Quellenlinks zum Ausgabezeitpunkt, echter Papierdruck, Mobilansicht (nicht vorgesehen).

## 6. Offene Lücken und nicht blockierende Fragen
- Kein öffentlich benannter GCC-Flugabwehrauftrag Rheinmetalls 2024–2026; Kunde des Skynex-Auftrags vom 02.07.2026 nicht genannt.
- Umsetzungs-/Betriebsstand RADARABIA (Saudi-Arabien) und RBAT (Katar) nicht belegt.
- Schweizer Exportpraxis gegenüber Golfstaaten nach Bundesratsentscheid 20.03.2026 amtlich offen; Güterumfang/Punkt 6.6 der AGG 48 nicht im Volltext geprüft.
- Skynex-Ukraine-Vertragswert widersprüchlich (160 vs. 182 Mio. EUR), nicht als gesichert verwendet; X-TAR3D-Reichweite 50/55 km je Herstellerseite.
- Primärbelege für Serienauslieferung Skyranger 30/35 fehlen; Medienberichte zu Skyranger-Verzögerungen (03/2026) nicht im Paket.
- Kapazitätsangaben Saab/NASAMS nicht öffentlich belegt (Matrixzellen „nicht öffentlich belegt“).
- Nicht zugänglich: Bloomberg (05/2026), militaeraktuell, Originalseiten EDGE/WAM, Handelsblatt/Forbes; Vergabeportale (TED) und Geschäftsberichte von EDGE, MAZ, Barzan, Lockheed, MBDA, Anduril nicht geprüft.
- research_requests: positioning RR-01, RR-02, RR-04–RR-06; swot RR-S-01–RR-S-05 (alle nicht blockierend).

Keine öffentliche Veröffentlichung erfolgt. Datenlücken sind keine Belege für Schwächen.
