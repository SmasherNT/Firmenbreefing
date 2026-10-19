# Flexible Fokusseiten statt separatem Markt-Deep-Dive

Neue vollständige Briefings verwenden immer manifest.focus_pages, auch als [].
Pro im Prompt genanntem Fokus genau eine eigenständige Seite nach dem optionalen
Gesprächspartner; Quellen folgen zuletzt. Beispiele: Lkw-OEMs, ein Land, Drohnen,
ein spezifischer Markt, Technologie oder anderes frei benanntes Thema. Die
Unternehmensanalyse einschließlich allgemeinem Markt/Wettbewerb bleibt auf Seite 1.
Keine feste dritte Marktseite und keine leere Fokus-Platzhalterseite.

## Delegation und Aufwand

**Genau ein separater focus-analyst-Aufruf je Fokusthema**, ausschließlich
claude-sonnet-5-5 mit effort: medium. Zwei Themen = zwei getrennte Agentenkontexte
und zwei Dateien, auch wenn dieselbe Agentendefinition verwendet wird. Nicht an
company-context-analyst, market-facts-analyst oder positioning-analyst routen.
Hauptagent übernimmt nur Auftragsnormalisierung, lokale Zusammenführung und Rendern.
Unabhängige Jobs können parallel laufen, schreiben aber nie dieselbe Datei.
Keine Fokusrecherche/Interpretation durch Opus und keine zusätzliche SWOT-Runde.
Bestehende Dokument-/Basis-/Schlussprüfer verwenden ebenfalls Sonnet 5.5 Medium.

Begrenze die Analysetiefe statt Timeline-/Grafikanzahl: Orientierung, wesentliche
Akteure/Segmente, klar belegte Kernaussagen und jüngste relevante Entwicklungen.
Keine vollständige Marktstudie, rekursiven Unteranalysen, feste Quellenquote oder
Suche nach künstlicher Vollständigkeit. Bestehende Fakten/Originalcache gezielt
wiederverwenden; nur nötigen Kontext übergeben, nicht ganze Briefings/Quelltexte.
3–5 Kernaussagen mit wenigen kurzen Belegfakten. Bei dünner Evidenz weniger mit
coverage_note; keine Füllthesen. Umfangreiche Details bleiben per Klick erreichbar.

## Manifest und Ergebnisvertrag

```json
"focus_pages": [
  {"id": "lkw", "label": "Europäische Lkw-OEMs"},
  {"id": "drohnen", "label": "Drohnenmarkt in Deutschland"}
]
```

Reihenfolge aus dem Prompt erhalten. IDs nur A–Z/a–z/0–9/_/-; je Lauf eindeutig.
Prompt „Fokusseiten: …“ ist eindeutig. Auch gewünschte separate Markt-/Länder-/
Themenüberblicke auf diesen generischen Vertrag routen. Allgemeine fachliche
Unternehmensthemen auf Seite 1 bleiben topics mit page=main. Explizite Nutzervorgaben
haben Vorrang; keine alten page=market/market_dashboard-Strukturen für neue Läufe.

Je Job work/focus-<id>-facts.json mit Standard-Faktenmetadaten nach faktenphase.md:
role=focus, focus_id=<id>, Claim-Präfix F_<id>_, claims/source_proposals/gaps/coverage.
focus_pages enthält genau eine Seite mit derselben ID/Bezeichnung wie im Manifest.
Eigene Quellenmetadaten vollständig liefern; gemeinsame Quellen konsistent halten.

Seitenfelder:
- id, label, overview (ein Orientierungssatz), claim_ids für overview.
- theses: 3–5 Zeilen mit id, label (belegte Kernaussage), claim_ids. Unter drei
  zusätzlich coverage_note. Keine unbelegten eigenen Schlussfolgerungen.
- charts: Liste mit id, type, title, claim_ids, optional caption. So viele fachlich
  sinnvolle Grafiken wie nötig, keine starre Begrenzung. Bei null Grafiken
  visualization_note mit konkreter Evidenzgrenze. Jeder sichtbare Text wird mitgeprüft.
- timeline: Zeilen id, date (YYYY-MM-DD), label, status, claim_ids. Zeitfenster:
  Stichtag minus sechs Kalendermonate bis einschließlich Stichtag. Relevante
  Ereignisse, keine starre Anzahl; beim Rendern neueste zuerst. Veröffentlichungs-
  und Ereignisdatum unterscheiden. Fehlendes Ereignisdatum als Grenze dokumentieren,
  nicht erfinden. Ankündigung, Auftrag, Pilot und Betrieb ausdrücklich unterscheiden.
  Bei leerer Liste timeline_note mit Recherchebefund/Abdeckung.
- gaps: kurze Textliste für standardmäßig eingeklappten Abschnitt.

Grafiktypen (alles lokal, offline, ohne LLM-Designrunde):

| type | Daten | Einsatz |
|---|---|---|
| matrix | columns:[{id,label}], rows:[{id,label,claim_ids,cells:[{id,value,claim_ids}]}]; Zell-IDs entsprechen exakt der Spaltenfolge | Anbieter × Segmente, Länder × Aktivitäten, Programme × Status |
| bars | metric, unit, period, scope; rows:[{id,label,value,claim_ids}] | Vergleichbare Mengen/Marktwerte/Standorte mit gleicher Definition und Periode |
| structure | groups:[{id,label,claim_ids,items:[{id,label,claim_ids}]}] | Akteurslandschaft, Rollen oder Wertschöpfungsstufen ohne behauptete Beziehungen |

Alle Zeilen-/Grafik-IDs innerhalb ihrer Liste eindeutig. Balkenwerte endlich,
nichtnegativ, belegt; keine Rangfolge aus inkompatiblen Daten. Fehlende Kennzahlen
als Datenlücke oder qualitative Matrix statt erfundener Balken. Keine Verbindung
zwischen Akteuren allein durch gemeinsame Darstellung suggerieren. Beschriftungen,
Einheiten, Zeitraum, Scope und tatsächlicher Status bleiben direkt sichtbar.
Belegfakten und interne Quellenverweise per Klick, vollständige Evidenz zentral.

## Integration und Prüfung

prepare-facts.py --modules erhält die vier bisherigen Faktenmodule und alle
focus-<id>-facts.json. selected_roles bleibt die Auswahl der vier Kernrollen;
focus_pages fordert die zusätzlichen Jobs unabhängig davon an. Im Prüfpaket
führt jede Instanz eine eigene module_view und module_context mit role=focus:<id>.
Originaldateien bleiben getrennt. Facts-Index erhält die ursprüngliche Job-Zuständigkeit.
Fehlende, doppelte, fremde oder ungeprüfte Fokusseiten verhindern die Ausgabe.
Alle sichtbaren Fokus-Claims sind A-Pflicht und gehen in das bestehende Basis-Review;
auch Diagrammwerte/-Zuordnungen und verdichtete Kernaussagen semantisch prüfen.
Keine eigene zusätzliche Reviewrunde pro Seite erzwingen. Quellenkonflikte gezielt
an genau die zuständige focus-analyst-Instanz geben. Konfiguriertes Sonnet Medium
für Dokumentprüfung und beide Leitphasen beibehalten.

Fokusfakten/-grafiken gehören nicht zum Positionierungs- oder SWOT-Auftrag und
werden nicht allein wegen der Fokusseite in deren selektive Kontexte übernommen.
Das vollständige Faktenpaket bleibt für Prüf-/Fingerprintkontrollen erreichbar.

Wiederaufnahme: resume-run.py erzeugt focus:<id> als eigenständigen Checkpoint je
Job. Nach Agentenabschluss --stage focus:<id> --output module=<Datei> checkpointen;
benötigte vorhandene Kernmodule als explizite Inputs nennen. Facts-Checkpoint erhält
zusätzlich --input focus:<id>=<Datei> für jeden Fokus. Nur reusable-Jobs überspringen.
Änderungen invalidieren den betroffenen Job und die abhängigen Fakten-/Review-/HTML-
Schritte. Fehlende Dateien sind nie ein erfolgreicher Agentenabschluss.

Alte geprüfte Manifestdateien ohne focus_pages behalten zur Wiederholbarkeit ihren
historischen Rendererpfad. Neue Aufträge schreiben focus_pages ausdrücklich und
nutzen damit ausschließlich die dynamische Seitenfolge und Seitenanzahl.
