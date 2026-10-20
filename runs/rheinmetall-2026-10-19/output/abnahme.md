# Abnahme · Firmenbriefing Rheinmetall AG (Lauf rheinmetall-2026-10-19)

Stichtag 2026-10-19 · Gesprächspartner Armin Papperger · keine Nutzerthemen (allgemeines Briefing)
Ausgabe: `output/briefing.html` (Renderer `scripts/render-briefing.py --full`, keine LLM-HTML)

## Prüfstatus (kurz)
| Prüfung | Ergebnis |
|---|---|
| Basis-Review (Fakten) | **freigegeben** in Runde 3; 297/297 Claims A „geprüft“, keine material_errors (`work/review-basis.md`) |
| Schluss-Review (Interpretation) | **freigegeben** in Runde 2; 126/126 I-/S-Claims A „geprüft“, 200 Fakten ausdrücklich übernommen (`work/review-final.md`) |
| Mechanik | prepare-facts, check-interpretation, review-shards merge, stamp-review, render: fehlerfrei |
| Lauf-Checkpoints | alle 11 Schritte `reusable`, `ready_for_visual_qa=true` |
| HTML-Struktur | 0 doppelte IDs, 0 kaputte interne Anker, 204 Original-Quelllinks, keine externen Assets |
| Desktop-Browser (Chromium, offline, 1440 px) | 0 JS-/Konsolenfehler, 0 Netzabfragen; Reiter, Portfolio-Profil, Matrix-Zelle/-Spalte, Cluster-Grafik, Regionszeilen, Summary-Dialog, Quellensuche funktionieren |
| Druck | beforeprint öffnet alle Details, alle 3 Seiten sichtbar, PDF-Ausgabe erzeugt, Ansicht danach wiederhergestellt |
| Ohne JavaScript | 1.391 native Details und 9 Tabellen (inkl. statischer Netzwerktabelle) erreichbar |

## Nutzerabweichung: Seite 3 entfällt
Auf ausdrücklichen Wunsch fehlen die separate Markt-Deep-Dive-Seite und ihr Reiter.
Umsetzung im Renderer per Manifest `omit_pages=["market"]` (Commit „Allow omitting the
market deep-dive page…“, Tests ergänzt, 214/214 Tests grün). Seitenzähler 01/03–03/03.
Der Renderer bricht ab, falls dadurch freigegebene Inhalte verloren gingen; hier gab es keine
Seite-3-Inhalte (kein regionaler Deep-Dive beauftragt). Alles Übrige (Summary, Entwicklungen,
Portfolio, Cluster, regionale Präsenz, Capability Matrix, SWOT, offene Fragen, Profil, Quellen)
ist enthalten.

## Tatsächlich ausgeführte Rollen
| Schritt | Rolle (konfiguriert) | Ergebnis |
|---|---|---|
| Kontext/Person | company-context-analyst (Sonnet 5.5 medium) | 69 T-/H-Claims, Profil + Medien-Timeline (9 Einträge) |
| Portfolio | portfolio-analyst (Sonnet 5.5 medium) | 39 Produkte, 21 Regionen regional_presence |
| Cluster | cluster-analyst (Opus 5.5 high) | 67 C-Claims, Netzwerk 68 Akteure / 83 Kanten, GB 2025 + HJ 2026 |
| Markt | market-facts-analyst (Opus 5.5 high) | 6 Peers × 6 Kriterien (155-mm-Munition), 36 Beobachtungen |
| Dokumentprüfung | 3 × source-document-reviewer (Sonnet 5.5 medium), 3 Runden | je ~65–70 Quellen, alle Originale im Cache gelesen |
| Leitprüfung Basis | source-reviewer (Sonnet 5.5 medium), 3 Runden | R1: 23 Korrekturen · R2: 4 · R3: freigegeben |
| Positionierung | positioning-analyst (Opus 5.5 high) | 114 I-Claims: 6 Kernaussagen, 3 Highlights, 36 Matrixzellen, 39 Reifegrade, 21 Präsenzstufen, 9 Keyfacts |
| SWOT | swot-analyst (Sonnet 5.5 medium) | 12 S-Claims (3 je Quadrant) |
| Schluss-Review | source-reviewer (Sonnet 5.5 medium), 2 Runden, 0 Dokumentjobs | R1: 15 Korrekturen · R2: freigegeben |

Modell/Effort sind die konfigurierten Werte (Agentendateien/Splitplan); das tatsächlich
ausgeführte Modell ist damit nicht nachgewiesen. Mehrere Agentenläufe wurden durch
Nutzungslimits unterbrochen und anschließend mit gespeichertem Stand fortgesetzt.

## Korrekturrunden
Basis: zwei Korrekturrunden (Grenze laut CLAUDE.md eingehalten), danach Freigabe ohne
material_errors. Schluss-Review: eine Korrekturrunde. Zwei Matrixzellen
(Rheinmetall-Reichweite, KNDS-Kapazität) stehen auf „nicht öffentlich belegt“, nicht auf
„weitere Faktenprüfung nötig“; keine Nachrecherche in diesem Lauf.

## Offene Grenzen (nicht blockierend, im Briefing ausgewiesen)
- Ungelöste Quellkonflikte werden nur ausgewiesen: IdZ-ES-Volumen (1,7 vs. 3,1 Mrd EUR), Schakal-Wert,
  Puma-Anteil, Bulgarien-JV (VMZ) umstritten, Kraken-JV-Datum, NVL-/Naval-Systems-Datum, CMD-Datum.
- Bezahlschranken: Handelsblatt (H-M01, H-M08) und GBP (M-HAN-06) nur im frei lesbaren Teil geprüft.
- Viele Ereignisse/Kennzahlen beruhen auf Rheinmetall-Angaben (als Herstellerangabe gekennzeichnet);
  wenige Behörden-/Vergabedaten; Vergabeportale und Software-/KI-Partner im Cluster nicht geprüft.
- Matrix: keine Datenblatt-Reichweite Rheinmetall, keine Ist-Kapazitäten in Geschossen bei den Peers;
  RDX-Fertigung Rheinmetall nur angekündigt. Datenlücken sind keine nachgewiesenen Schwächen.
- Golfstaaten „nicht eindeutig bestimmbar“ (RAST Riad nicht der Region zugeordnet).
- Q3-Zahlen (05.11.2026) lagen zum Stichtag nicht vor.
- Nicht blockierende Reviewer-Hinweise (Seitenangaben, fehlende I-PM-Querverweise in zwei
  Begründungen, Formulierungsdetails) stehen in den Review-Entwürfen unter non_blocking.

## Nicht geprüft
Keine Mobilansicht (laut Vertrag nicht vorgesehen), keine manuelle Sichtprüfung des Druck-PDFs
über die automatische Erzeugung hinaus. Dokumentcache: 237 Dokumente, 236 Downloads, 25
Cache-Treffer, 1 Import (Dokumentoperationen, keine Token-/Kostenmessung); Cache nicht committet.
