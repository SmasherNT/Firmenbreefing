# HTML-Ausgabe v2

## Ablauf
Neue vollständige HTML-Briefings: runs/<run_id>/input/, work/ und output.
Fakten -> Basis-Review -> Positionierung -> SWOT -> gemeinsamer Schluss-Review
-> fester Renderer. Hauptagent delegiert Fakten und Bewertungen.
Vorlage/Renderer lokal ausführen, nicht als Standard in den Modellkontext laden.
Keine zusätzliche Modellrunde für HTML. Reale Kostenersparnis später messen.
Bestehende Markdown-Modultests: legacy-html-output.md. Keine Mischläufe.
Keine Horváth-Kapitel und keine separaten Unternehmens-Deep-Dives.

## Faktenübergabe
Zusätzlich zu faktenphase.md liefern Rollen kompakte Darstellungszuordnungen.
prepare-facts übernimmt diese in module_views. Basis-Review prüft Labels/Zuordnung
semantisch; kein Label darf neue ungeprüfte Aussagen enthalten.
Tabellenzeile: id, label, claim_ids (nicht leer, vorhandene A-Fakten).
Keine kopierten Fakten-/Belegtexte pro Zeile.

| Rolle | Optionale Tabellen |
|---|---|
| context | company_facts, events, profile, topics |
| portfolio | products, regions, topics |
| cluster | topics, report_log; network bleibt eigenes Paketfeld |
| market | regions, topics, peers, observations gemäß Vergleichsvertrag |

events: zusätzlich date (YYYY-MM-DD oder null), kein Abrufdatum als Ereignisdatum.
Kurzes sachliches label, gegebenenfalls mit „angekündigt“/„laut Hersteller“/
„laut Medien“. Chronologische Zeitachse mit Datum links und klickbarer Karte
rechts; Datum unbekannt ausdrücklich zeigen und diese Einträge zuletzt führen.
Details enthalten vollständige A-Fakten, Aussageursprung, Unsicherheit und direkte
Originalquellen/Belegstellen. Kein neuer Agent oder zusätzlicher Interpretationstext.
products: domain und optional short_label nach portfolio-darstellung.md.
profile: Struktur und H-Claim-Verweise nach gespraechspartner.md; nur berufliche
Fakten der benannten Person. Snapshot/Werdegang/Fachprofil/Verantwortung offen zeigen.
regions: optional sections:[{label,claim_ids}] für Unterthemen.
topics: gleiche id wie manifest.topics[].id; Reihenfolge aus Manifest.
peers/observations nach capability-matrix.md, keine Scores in Faktenphase.
gaps/coverage/report_log: dokumentierte Grenzen, Suchstatus und offene Punkte.
Manifest topics=[{id,label}], optional person (String/Objekt) als Nutzerangabe.
Quellen tatsächlich öffnen; Nachrichtensnippet allein ist keine Tatsachenevidenz.

## Interpretation und Darstellung
positioning: section=executive_summary für 4–6 Hauptaussagen des Vollbriefings;
headline/preview/display_order und drei section=executive_highlights-I-Claims
nach executive-summary.md liefern. Keine fest vorgegebenen Finanzkennzahlen.
section=topic:<id> für Themen, weitere sections z. B. portfolio/regions/technology.
Typisierte matrix_cell-I-Claims und aktueller Plan erzeugen die Matrix:
Spalten aus Prüfauftrag, Zellen mit Methode, Begründung, Grenzen und A-Fakten.
Evidenzstufen sind ordinale Skalenanker; kein gemitteltes Gesamt-Ranking.
Portfolio-Reife nach portfolio-darstellung.md im bestehenden Positionierungsschritt.
Weitere Scores nur mit vorher definierten assessment_methods; null bei Datenlücke.
SWOT maximal drei Punkte je Quadrant; Datenlücke ist keine tatsächliche Schwäche.
Keine neue Interpretation beim Rendern erzeugen.

Feste vier Desktop-Seiten, auch wenn ein optionaler Auftragsteil leer ist:
1. Überblick: Summary, Entwicklungen, Portfolio, allgemeine Themen, Cluster,
   Capability Matrix, Einordnung, SWOT und offene Fragen. Module untereinander.
2. Beruflicher Gesprächspartner-Kontext.
3. Markt-Deep-Dive: regionale Themen, Länder/Marktzugang und regionale Einordnung.
4. Aussagen, Belegstellen und Originalquellen mit Suche.

Manifest topics=[{id,label,page}], page=main/market (Standard main);
market_title optional aus dem Auftrag, z. B. Golfstaaten. Reihenfolge je Seite
entspricht dem Auftrag. Unternehmenspräsenz vom allgemeinen Markt getrennt zeigen.
Portfolio nach portfolio-darstellung.md: sechs Stufen, farbige Produktgruppen,
Filter/Tabelle und ein vollständig geschlossener Detailblock. Produktklick öffnet
Block und Profil; keine firmenspezifischen Bewertungen in der Vorlage.
Cluster: Ziel in der Mitte, vier Gruppen einzeln klickbarer Akteure, kompakte
Auswahl, Filter/Querverbindungen und feste rechte Detailspalte. Vier Bereiche im
2×2-Raster in der bestehenden Reihenfolge; gleiche Höhe pro Zeile, abhängig von
der Anzahl. Einheitliche Knotengröße, Form und Farbe je Akteurskategorie, Namen
unter den Formen und keine Zahlen-/Score-Badges. Gebogene Linien mit Pfeilen,
ohne Endpunktkreise; normales Seitenscrollen. Details in netzwerk-html.md.
Mehrere Vorgänge je Akteurspaar über eine gemeinsame Linie
auswählen; sämtliche Einzelbelege erhalten. Matrix nach capability-matrix.md:
Spalten folgen dem Auftrag, einheitlich hohe Kurztextzellen, große Evidenzstufen
mit tatsächlichem Skalenmaximum, lokale Scrollfläche und feste Akteursspalte.
Zellklick zeigt vollständige Bewertung unter der Matrix; Spaltenkopfklick vergleicht
alle Wettbewerber im selben Kriterium. Native Details bewahren sämtliche Quellen
ohne JavaScript und im Druck. Andere Karten öffnen den gemeinsamen Dialog.
Statische zugängliche Netzwerktabelle auch ohne JavaScript. Druck öffnet Details
und stellt anschließend die vorherige Ansicht wieder her.
Keine externen Assets, Laufzeit-Netzabfragen oder zusätzliche LLM-Designrunde.
Keine gesonderte Mobilansicht/-abnahme. Spezielle Landkarten/Zeitreihen sind kein
Pflichtbestandteil der generischen Darstellung.

## Prüfbarrieren
Basis-Review input_fingerprint aus facts-validation.packet_fingerprint bindet
auch Tabellenlabels/Zuordnungen und Netzwerk. Nach Änderung Paket neu erzeugen,
geänderte Inhalte/Zuordnungen gezielt prüfen und stamp-review erneut ausführen.
Unveränderte A-Claim-Urteile bleiben wiederverwendbar.
Aktuelle I-/S-Kontexte und Schluss-Review-Fingerprints notwendig.
Kernansicht, Netzwerk und Interpretationen nur aus aktuellen A-Fakten;
B-Hintergrunddetails mit tatsächlichem Prüfstatus im Register.
Blockierte Module, Materialfehler, blockierende Fragen und pending Matrix-Prüfung
verhindern finale HTML. Formaler Pass prüft keine Quellenwahrheit.
Bei Fehlern keine neue HTML; frühere Erfolgsdatei nicht als aktuell ausgeben.

## Aufruf
Pfade aus delegiertem Lauf; keine festen Firmendaten.

```bash
python3 scripts/render-briefing.py --manifest <facts-run.json> --facts <review-packet.json> --basis-review <review-basis.md> --positioning <positioning.json> --positioning-context <positioning-context.json> --swot <swot.json> --swot-context <swot-context.json> --final-review <review-final.md> --plan <comparison-plan.json> --full --out <Lauf>/output/briefing.html
```

Ohne Vergleich --plan weglassen. Explizite reine Fakten-HTML: Interpretationsargumente
und --full weglassen; Basis-Review bleibt erforderlich.
Ältere Reviews ohne Paket-Snapshot vor Ausgabe um Zuordnungsprüfung ergänzen.
stamp-review erteilt keine Freigabe.
Abnahme: Agentenprotokoll/Review, Mechanik, Links/JS und Desktop-Browser/Druck/Filter
getrennt prüfen. Fehlende Werkzeuge als nicht geprüft benennen.
Testbeispiele sind keine öffentliche Unternehmensrecherche.


Auftragsbezogene Themenkarten mit headline/preview sowie unternehmensweite
Portfolioabdeckung folgen themen-darstellung.md. SWOT-Kategorien farbig darstellen.
