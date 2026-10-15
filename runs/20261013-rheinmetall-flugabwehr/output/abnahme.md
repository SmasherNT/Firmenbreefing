# Abnahme · Rheinmetall AG · Flugabwehr / Markt Europa

Lauf `20261013-rheinmetall-flugabwehr` · Stichtag 2026-10-13 · Ausgabe `output/briefing.html`
(gerendert 2026-10-15 nach Wiederaufnahme). Status: **ausgegeben, Basis- und Schluss-Review freigegeben**.

## Auftrag
Vollständiges HTML-Firmenbriefing; Themen in Nutzerreihenfolge:
1. Flugabwehr: Technologien, industrielle Anforderungen und Wettbewerbsposition (Seite 1)
2. Markt-Deep-Dive europäische Flugabwehrindustrie (Seite 3, „Europa“)

Gesprächspartner: Armin Papperger (Seite 2; Rolle öffentlich verifiziert).

## Tatsächlich eingesetzte Rollen
| Rolle | Ergebnis | Status |
|---|---|---|
| company-context-analyst | context-facts.json, 48 T-/H-Claims | vollständig |
| portfolio-analyst | portfolio-facts.json, 78 P-Claims, 29 Produkte, 14 Präsenzregionen | vollständig |
| cluster-analyst | cluster-facts.json, 54 C-Claims, 39 Knoten / 51 Kanten, GB 2025 + HJFB 2026 | teilweise (Lücken sichtbar dokumentiert) |
| market-facts-analyst | market-facts.json, 44 M-Claims, 9 Peers, 54 Beobachtungen, Dashboard 9 Länder / 24 Programme | vollständig |
| positioning-analyst | positioning.json, 125 I-Claims (Summary, 54 Matrixzellen, 29 Reifegrade, 9 Keyfacts, 14 Präsenzstufen, Themen) | vollständig |
| swot-analyst | swot.json, 11 S-Claims (S 3 · W 2 · O 3 · T 3) | vollständig |
| source-reviewer | Basis-Review r1–r4, Schluss-Review r1–r3 | freigegeben |

Hauptagent: Auftrag/Manifest, Vergleichsplan (6 Kriterien), Paketbau, Kontexte, Stempel,
Checkpoints, Rendering. Keine eigenen Fakten-/Interpretations-JSONs, keine LLM-HTML.

## Reviews und Korrekturen
- **Basis r1:** 14 Korrekturen (u. a. NVL-Closing 27.02.2026, Österreich als GDELS-Unterauftrag,
  Köhne-Wechsel nur angekündigt, Eurosatory/Rumänien-Belege, Skyranger-Q4-2027-Zuschreibung S&V).
- **Basis r2:** freigegeben (224 Claims, alle A, alle Netzwerkkanten und Pflicht-A-Fakten vollständig).
- **Schluss r1:** 11 Korrekturen (Nordeuropa-Stufe, Stinger→DefendAir, Lokalwertschöpfung NL/RO nur
  Herstellerangabe, Verzugsursachen-Zuschreibung, Flugkörperabhängigkeit eingegrenzt, NNbS nur
  „gebilligt“, SWOT-Schwäche „Teillieferant“ gestrichen).
- **Basis r3:** nach Wiederaufnahme >24 h alle HTTP-Quellen revalidiert; 120 Claims mit
  geändertem Snapshot im neuen Original geprüft, 104 übernommen; Skoppum-Entwicklung ergänzt.
- **Schluss r2:** freigegeben (136 Ableitungen geprüft bzw. ausdrücklich bestätigt).
- **Basis r4 / Schluss r3:** Renderer verlangte YYYY-MM(-DD) für Netzwerk-as_of; e47/e48 auf
  Bezugsstand 31.12.2025 (GB 2025), C-032 ohne erfundenes Ereignisdatum; beide Reviews freigegeben,
  Interpretationen unverändert übernommen.

Korrekturrunden je Phase innerhalb der Grenze von zwei; keine offenen Materialfehler.

## Mechanische Prüfungen
- prepare-facts: 0 Fehler (224 Claims, 136 Quellen); check-interpretation: 0 Fehler
  (Positionierung 125, SWOT 37 inkl. Kontext-I-Claims, zusammengeführt 137).
- stamp-review: Basis 224 / Schluss 136 Claims, Status freigegeben (Stempel ist keine Inhaltsfreigabe).
- resume-run: alle Stufen context … html `reusable`, `ready_for_visual_qa=true`.
- Dokumentcache: 175 Dokumente, 328 Downloads, 30 Cache-Treffer, 20 Revalidierungen
  (Dokumentoperationen, keine Token-/Kostenmessung). Originalcache nicht committet.

## Desktop-Browserprüfung (Chromium headless, offline, 1440/1280/1024 px)
- Vier Seiten vorhanden; keine horizontale Seitenüberbreite; keine JS-/Konsolenfehler;
  keine externen Netzabfragen; keine defekten internen Anker.
- 1.839 externe Quellenlinks, alle https und in neuem Tab.
- Portfolio: 29 Produkte, Detailblock initial geschlossen, Produktklick öffnet Profil, Suchfilter wirkt.
- Netzwerk: 39 Knoten / 51 Kanten gezeichnet, statische Tabelle 51 Zeilen, Knoten- und
  Kantenauswahl füllen die rechte Detailspalte mit Belegen.
- Capability Matrix: 54 Zellen, Zellklick zeigt Einzelbewertung mit Faktenbasis.
- Regionale Präsenz: 14 Zeilen, Zeilenklick öffnet Regionsprofil.
- Druck: alle 1.412 Details geöffnet, Zustand danach wiederhergestellt; PDF-Erzeugung erfolgreich.
- Ohne JavaScript: 1.354 native Details, 1.764 Quellenlinks, Netzwerktabelle vollständig.
- Sichtprüfung per Screenshot: Executive Summary, Netzwerk, Matrix, Gesprächspartner, Markt-Deep-Dive.

Nicht geprüft: Mobil-/Touchansicht (nicht Vertragsbestandteil), Erreichbarkeit aller
1.839 Quellenlinks im Live-Netz, andere Browser.

## Offene Grenzen (inhaltlich)
- Skyranger-30-Serienverzug bleibt strittig (Rheinmetall ~5–6 Monate vs. BAAINBw/S&V/Stern bis
  18 Monate); Originale Capital/Stern/BAAINBw waren nicht zugänglich.
- Bundeswehr-Skyranger-Großauftrag bis Stichtag nicht belegt (kein Beweis der Nichtvergabe);
  „Arminius“-Festvertrag nur als Rheinmetall-Erwartung ohne Produktbezug.
- Lieferstände Dänemark/Österreich und Ukraine-Einsatzangaben überwiegend Herstellerangaben.
- Fertigungsstandorte/-raten mehrerer Wettbewerber nicht öffentlich belegt (Matrix „nicht öffentlich
  belegt“, keine Schwäche). Nicht erfasste Programme: Wisła, Patriot/Arrow, SAMP/T NG, Land GBAD.
- Cluster „teilweise“: Partner ARGE HEL, RADARABIA/Barzan/Hungary-Mitgesellschafter, Geschäftsberichte
  Diehl/MBDA/ICEYE/Anduril/GDELS nicht ausgewertet; Lockheed-JV-Details nicht primär bestätigt.
- Lockheed 10-K (SEC) nur noch als Suchweg: Neuabruf erfordert Kontaktangabe im User-Agent.
  Hinweis: Beim ersten Abruf am 2026-10-13 hatte die Clusterrolle unzulässig die Nutzer-E-Mail im
  User-Agent an sec.gov gesendet; danach in allen Delegationen untersagt, keine Speicherung im Lauf.
- Nicht blockierende Forschungsfragen der Interpretation (RR-02 bis RR-06, RR-SWOT-01/02) bleiben offen.
- Q3-Mitteilung erscheint erst am 05.11.2026 (nach Stichtag).
