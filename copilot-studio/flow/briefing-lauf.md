# Agent Flow „Briefing-Lauf“

Der Flow ist das Fließband. Er ruft die Agenten in fester Reihenfolge auf,
reicht die Dokumente über die Werkstatt weiter und setzt die Prüftore durch.
Kein Agent ruft einen anderen Agenten auf.

**Anlegen:** Copilot Studio → Workflows → New workflow → More create options →
Agent flows.

## Bausteine im Flow

| Kurzname | Aktion in Copilot Studio |
|---|---|
| **Werkstatt: X** | Aktion des Custom Connectors „Briefing-Werkstatt“ (siehe `../werkstatt/`) |
| **Agent: X** | Aktion „Agent aufrufen“ mit dem Agenten aus `../agenten/` |
| **Bis bestanden** | Schleife „Do until“ mit Bedingung auf das Ergebnis der Werkstatt |
| **Je Eintrag** | Schleife „Apply to each“ |
| **Parallel** | parallele Zweige, falls verfügbar; sonst nacheinander |

Jeder Agentenaufruf bekommt genau ein Eingabedokument von der Werkstatt und
gibt genau ein JSON-Ergebnis zurück. Der Flow speichert dieses Ergebnis sofort
über die Werkstatt. Agenten lesen und schreiben keine Dateien selbst.

## Auslöser

1. **Auslöser „Wenn ein Agent den Flow aufruft“** mit den Eingaben `anfrage`,
   `modus` und `nutzer` vom Start-Agenten.
2. **„Dem Agenten antworten“** sofort mit „gestartet“. Danach läuft der Flow
   weiter. Ein Agent wartet höchstens rund zwei Minuten auf einen Flow; das
   Briefing selbst dauert länger. Muss im Test bestätigt werden (Testpunkt T1).

Ausweichweg, falls das nicht geht: Der Start-Agent legt einen Eintrag in der
SharePoint-Liste „Briefing-Aufträge“ an, und der Flow startet mit dem Auslöser
„Wenn ein Element erstellt wird“. Am restlichen Ablauf ändert sich nichts.

## Ablauf Vollbriefing

### A · Lauf anlegen

| # | Schritt | Ergebnis |
|---|---|---|
| A1 | Werkstatt: `laufAnlegen` (anfrage, modus) | `run_id`, `stichtag` |

### B · Auftrag

| # | Schritt | Ergebnis |
|---|---|---|
| B1 | **Bis bestanden:** | |
| B2 | Agent: **01 Auftrag** mit anfrage, modus, stichtag, ggf. `rueckgabe` | Auftrag, Manifest, Vergleichsplan |
| B3 | Werkstatt: `auftragSpeichern` | `ok`, `fehler` → bei Fehler als `rueckgabe` zurück zu B2 |
| B4 | | Liste der Rollen und Fokusthemen |

### C · Fakten (Phase 1)

Für jede Rolle der Unterablauf **„Modul erstellen“** (siehe unten).

| # | Schritt | Agent |
|---|---|---|
| C1 | **Parallel:** Rolle `context` | 02 Kontext & Person |
| C2 | Rolle `portfolio` | 03 Portfolio & Präsenz |
| C3 | Rolle `cluster` | 04 Cluster & Netzwerk |
| C4 | Rolle `market` | 05 Markt & Wettbewerb |
| C5 | **Je Fokusthema:** Rolle `focus:<id>` | 06 Fokusthema, ein Aufruf je Thema |

### D · Prüftor 1 (Basis)

| # | Schritt | Ergebnis |
|---|---|---|
| D1 | **Bis bestanden:** | |
| D2 | Werkstatt: `pruefungVorbereiten` (phase = basis) | `formatfehler` je Modul oder `jobs` (bis zu 3) |
| D3 | Bei `formatfehler`: **je Modul** „Modul erstellen“ mit `rueckgabe`, dann zurück zu D2 | |
| D4 | **Je Job:** Agent **07 Dokumentprüfung** mit dem Jobdokument | Befunde |
| D5 | Werkstatt: `befundSpeichern` (basis, job_id) | |
| D6 | Werkstatt: `leitpruefungEingabe` (basis) | Eingabedokument |
| D7 | Agent: **08 Leitprüfung** | Leitentscheidungen |
| D8 | Werkstatt: `pruefungAbschliessen` (basis) | `bestanden`, `rueckgabe` je Modul |
| D9 | Nicht bestanden: **je Modul in `rueckgabe`** „Modul erstellen“ mit den Befunden, dann zurück zu D2 | |

### E · Bewertung und Prüftor 2 (Schluss)

| # | Schritt | Ergebnis |
|---|---|---|
| E1 | **Bis bestanden:** | |
| E2 | Werkstatt: `bewertungEingabe` (positioning) → Agent **09 Positionierung** → Werkstatt: `bewertungSpeichern` | bei Formatfehlern zurück zu 09 |
| E3 | Werkstatt: `bewertungEingabe` (swot) → Agent **10 SWOT** → Werkstatt: `bewertungSpeichern` | bei Formatfehlern zurück zu 10 |
| E4 | Melden 09 oder 10 blockierende Rückfragen an Faktenrollen: je Rolle „Modul erstellen“ mit der Frage, danach zurück zu **D** | |
| E5 | Werkstatt: `pruefungVorbereiten` (phase = final) | `jobs` nur für neu zu prüfende Fakten, oft keine |
| E6 | **Je Job:** Agent 07 → Werkstatt: `befundSpeichern` (final) | |
| E7 | Werkstatt: `leitpruefungEingabe` (final) → Agent **08 Leitprüfung** → Werkstatt: `pruefungAbschliessen` (final) | `bestanden`, `rueckgabe` |
| E8 | Nicht bestanden: `rueckgabe` an `positioning` oder `swot` → zurück zu E2/E3 mit Befunden; an eine Faktenrolle → „Modul erstellen“, dann zurück zu **D** | |

### F · Ausgabe

| # | Schritt | Ergebnis |
|---|---|---|
| F1 | Werkstatt: `briefingRendern` (modus) | HTML und Dateiname |
| F2 | SharePoint: „Datei erstellen“ in `Briefings/<run_id>/` | Link |
| F3 | Optional Werkstatt: `laufArchiv` → SharePoint | ZIP mit allen Übergabedokumenten und Prüfungen |
| F4 | Teams: Nachricht an `nutzer` mit dem Link | |

## Ablauf Kurzbriefing

Gleicher Flow, Zweig nach `modus = kurz`:

- **A** und **B** wie oben. Der Auftrags-Agent setzt die Rollen auf `context` und
  `portfolio`, keine Fokusthemen, keinen Vergleichsplan.
- **C** nur C1 und C2.
- **D** wie oben.
- **E** entfällt.
- **F** mit `modus = kurz`: gleiche HTML-Vorlage, ohne Bewertungsseiten.

## Unterablauf „Modul erstellen“

Wird für jede Faktenrolle verwendet, für die Erstellung und für jede Korrektur.

| # | Schritt |
|---|---|
| M1 | **Bis bestanden:** |
| M2 | Werkstatt: `eingabeHolen` (rolle, ggf. `rueckgabe`). Das Dokument enthält Auftrag, Manifest, Stichtag, bei Markt den Vergleichsplan, bei Korrektur das bisherige Modul und die Befunde. |
| M3 | Agent der Rolle mit diesem Dokument |
| M4 | Werkstatt: `modulSpeichern` (rolle, Ergebnis) → bei Formatfehlern zurück zu M2 mit den Fehlern |

Falls Copilot Studio wiederverwendbare Unterabläufe (Child Flows) anbietet,
diesen Block einmal anlegen. Sonst je Rolle kopieren.

## Was vor dem Bau getestet werden muss

| Nr. | Frage | Warum wichtig |
|---|---|---|
| T1 | Läuft der Flow nach „Dem Agenten antworten“ weiter? | sonst Ausweichweg über die SharePoint-Liste |
| T2 | Wartet „Agent aufrufen“ auch bei Recherchen von mehreren Minuten? | Grundlage des ganzen Fließbands |
| T3 | Startet jeder Agentenaufruf ohne Verlauf? | Unabhängigkeit der Rollen |
| T4 | Wie groß darf das Eingabedokument eines Agentenaufrufs sein? | Prüfpakete und Kontexte können groß werden |
| T5 | Laufen parallele Zweige mit Agentenaufrufen? | sonst nacheinander, dauert länger |
| T6 | Welche Höchstzahl gilt für „Do until“? | Rückläufe bis zum Bestehen |
| T7 | Sind Claude Opus 5.5 und Sonnet 5.5 im Mandanten produktiv freigegeben? | Modellzuordnung |
| T8 | Was kostet ein Lauf in Copilot Credits? | Budget für den Rollout |
