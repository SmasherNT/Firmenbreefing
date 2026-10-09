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
profile: {name,claim_ids}, nur berufliche H-Claims und nur bei benannter Person.
regions: optional sections:[{label,claim_ids}] für Unterthemen.
topics: gleiche id wie manifest.topics[].id; Reihenfolge aus Manifest.
peers/observations nach capability-matrix.md, keine Scores in Faktenphase.
gaps/coverage/report_log: dokumentierte Grenzen, Suchstatus und offene Punkte.
Manifest topics=[{id,label}], optional person (String/Objekt) als Nutzerangabe.
Quellen tatsächlich öffnen; Nachrichtensnippet allein ist keine Tatsachenevidenz.

## Interpretation und Darstellung
positioning: section=executive_summary für 4–6 Hauptaussagen des Vollbriefings;
section=topic:<id> für Themen, weitere sections z. B. portfolio/regions/technology.
Typisierte matrix_cell-I-Claims und aktueller Plan erzeugen die Matrix:
Spalten aus Prüfauftrag, Zellen mit Methode, Begründung, Grenzen und A-Fakten.
Evidenzstufen sind ordinale Skalenanker; kein gemitteltes Gesamt-Ranking.
Weitere Scores nur mit vorher definierten assessment_methods; null bei Datenlücke.
SWOT maximal drei Punkte je Quadrant; Datenlücke ist keine tatsächliche Schwäche.
Keine neue Interpretation beim Rendern erzeugen.

Kompakte Hauptseite: Summary, Themen, Entwicklungen, Vier-Cluster-Netz, Portfolio,
Matrix, SWOT. Optionale Seiten für Person und Regionen/Märkte. Details & Quellen
immer vorhanden. Unternehmenspräsenz vom allgemeinen Markt getrennt beschriften.
Karten und Matrixzellen öffnen Begründung und Originalbelege. Native details,
mobile Karten, horizontale Matrix und ausgeklappte Druckansicht.
Alle Beziehungen in statischer zugänglicher Tabelle auch ohne JavaScript.
Keine externen Assets/Bibliotheken oder Laufzeit-Netzabfragen.
Spezielle regionale Zeitreihen/Landkarten/frei entworfene Grafiken sind noch
kein generischer Bestandteil; entsprechende Anforderungen gesondert umsetzen.

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
Abnahme: Agentenprotokoll/Review, Mechanik, Links/JS und Browser/Mobil/Druck/Filter
getrennt prüfen. Fehlende Werkzeuge als nicht geprüft benennen.
Testbeispiele sind keine öffentliche Unternehmensrecherche.

