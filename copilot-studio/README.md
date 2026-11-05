# Firmenbriefing in Microsoft Copilot Studio

Dieser Ordner beschreibt, wie das Firmenbriefing-Tool in Copilot Studio
aufgebaut wird. Er ist aus der aktuellen Fassung des Repositorys neu
strukturiert. Die fachlichen Regeln unter `references/` und die Skripte unter
`scripts/` bleiben die einzige Quelle. Hier wird nichts davon kopiert, sondern
festgelegt, wie Copilot Studio sie nutzt.

**Zielbild mit Diagrammen:** [`zielbild/zielbild.html`](zielbild/zielbild.html),
als Bilder [`ablauf-vollbriefing.png`](zielbild/ablauf-vollbriefing.png) und
[`ablauf-kurzbriefing.png`](zielbild/ablauf-kurzbriefing.png).

---

## 1. Grundprinzip

| Baustein | Aufgabe | In Copilot Studio |
|---|---|---|
| **Agenten** | Recherchieren, prüfen, bewerten. Jeder kennt nur seine Aufgabe. | 11 eigene Agenten |
| **Agent Flow** | Feste Reihenfolge, Prüftore, Rückläufe, Weitergabe der Dokumente | Workflows → Agent flows |
| **Werkstatt** | Ablage, Formatprüfung, Prüfpakete, Freigabe, HTML | Custom Connector auf ein kleines Backend |

Drei Regeln gelten immer:

1. **Kein Agent ruft einen anderen auf.** Nur der Flow ruft Agenten auf.
2. **Jeder Aufruf startet frisch.** Ein Agent kennt nur sein Eingabedokument.
3. **Die Werkstatt nutzt die vorhandenen Skripte.** Gleiche Daten ergeben die
   gleiche HTML wie heute.

## 2. Ablauf in Kürze

```
Nutzer in Teams
  └─ 00 Start-Agent ── startet ──► Agent Flow „Briefing-Lauf“
        01 Auftrag
        02 Kontext · 03 Portfolio · 04 Cluster · 05 Markt · 06 Fokus je Thema   (parallel)
        Werkstatt: zusammenführen, Format prüfen
        07 Dokumentprüfung (bis zu 3 Jobs) → 08 Leitprüfung
        Prüftor 1: nicht bestanden → Befunde zurück an das Modul
        09 Positionierung → 10 SWOT → 08 Leitprüfung (Schluss)
        Prüftor 2: nicht bestanden → zurück an 09 bzw. 10
        Werkstatt: Briefing rendern → SharePoint → Link per Teams
```

**Kurzbriefing:** nur 01, 02, 03, 07 und 08; dieselbe HTML-Vorlage ohne
Bewertungsseiten.

## 3. Inhalt des Ordners

| Pfad | Inhalt |
|---|---|
| [`zielbild/`](zielbild/) | Diagramme Voll- und Kurzbriefing zur Orientierung |
| [`agenten/`](agenten/) | je Agent: Steckbrief mit Einstellungen und fertige Anweisungen zum Einfügen |
| [`flow/briefing-lauf.md`](flow/briefing-lauf.md) | alle Schritte des Agent Flows, Unterablauf, Testpunkte |
| [`uebergaben.md`](uebergaben.md) | welches Dokument von wem zu wem geht, und warum als JSON |
| [`werkstatt/schnittstelle.md`](werkstatt/schnittstelle.md) | Aktionen des Backends und welche Skripte sie nutzen |
| [`werkstatt/openapi.yaml`](werkstatt/openapi.yaml) | Definition für den Custom Connector |

## 4. Die Agenten

| Nr. | Agent | Bisherige Rolle | Modell | Websuche | Modus |
|---|---|---|---|---|---|
| 00 | [Start-Agent](agenten/00-start.md) | – | Sonnet 5.5 | aus | beide |
| 01 | [Auftrag](agenten/01-auftrag.md) | Hauptagent (inhaltlicher Teil) | Opus 5.5 | nur Firmenidentität | beide |
| 02 | [Kontext & Person](agenten/02-kontext.md) | company-context-analyst | Sonnet 5.5 | an | beide |
| 03 | [Portfolio & Präsenz](agenten/03-portfolio.md) | portfolio-analyst | Sonnet 5.5 | an | beide |
| 04 | [Cluster & Netzwerk](agenten/04-cluster.md) | cluster-analyst | Opus 5.5 | an | voll |
| 05 | [Markt & Wettbewerb](agenten/05-markt.md) | market-facts-analyst | Opus 5.5 | an | voll |
| 06 | [Fokusthema](agenten/06-fokus.md) | focus-analyst | Sonnet 5.5 | an | voll |
| 07 | [Dokumentprüfung](agenten/07-dokumentpruefung.md) | source-document-reviewer | Sonnet 5.5 | aus | beide |
| 08 | [Leitprüfung](agenten/08-leitpruefung.md) | source-reviewer | Sonnet 5.5 | aus | beide |
| 09 | [Positionierung](agenten/09-positionierung.md) | positioning-analyst | Opus 5.5 | aus | voll |
| 10 | [SWOT](agenten/10-swot.md) | swot-analyst | Sonnet 5.5 | aus | voll |

Die Modelle entsprechen `references/modellaufteilung.json`. Der Effort
(medium/high) lässt sich in Copilot Studio nach heutigem Stand nicht je Agent
einstellen. Die mechanische Arbeit des bisherigen Hauptagenten übernimmt die
Werkstatt.

**Jede Agentendatei enthält:**

- **Steckbrief:** Modell, Websuche, Tools, hochzuladendes Wissen, Gedächtnis.
- **Eingabe und Ausgabe:** was der Flow übergibt und was zurückkommt.
- **Anweisungen:** Textblock, der unverändert in das Anweisungsfeld kommt.

**Wissen hochladen** heißt: die genannten Dateien aus `references/` direkt aus
dem Repository als Wissensquelle des Agenten hochladen. Die Anweisungen
enthalten die Pflichtregeln; das Wissen liefert die Details.

## 5. Aufbau Schritt für Schritt

| Stufe | Was tun | Fertig, wenn |
|---|---|---|
| **0 Voraussetzungen** | Power-Platform-Umgebung, Copilot Credits mit Budget, Claude-Modelle und Websuche durch die Administration freigeben, SharePoint-Bibliothek „Briefings“ | ein Test-Agent mit Claude Sonnet 5.5 antwortet |
| **1 Machbarkeit** | Testpunkte T1 bis T8 aus [`flow/briefing-lauf.md`](flow/briefing-lauf.md) mit einem Mini-Flow und zwei Test-Agenten klären | alle Testpunkte beantwortet |
| **2 Werkstatt** | Backend nach [`werkstatt/schnittstelle.md`](werkstatt/schnittstelle.md) bauen und als Custom Connector anlegen | Demo-Daten ergeben byte-gleiche HTML wie `examples/build-demo.py` |
| **3 Agenten einzeln** | Agenten 01 bis 08 anlegen, jeden einzeln im Testbereich mit einem Beispieldokument prüfen | jedes Ergebnis besteht die Formatprüfung der Werkstatt |
| **4 Fließband Kurz** | Flow mit Start-Agent, Zweig „kurz“ und Prüftor 1 | ein echtes Kurzbriefing landet in SharePoint, ein absichtlich falscher Fakt geht zurück und wird korrigiert |
| **5 Fließband Voll** | Agenten 09 und 10, Fokus-Schleife, Prüftor 2 | ein Vollbriefing mit zwei Fokusthemen entspricht inhaltlich einem heutigen Lauf |
| **6 Freigabe für alle** | Start-Agent in Teams veröffentlichen, Verbrauch beobachten, Kurzanleitung | Pilot mit drei Nutzern und drei Firmen |

## 6. Wie das Ergebnis gleich bleibt

| Risiko in Copilot Studio | Gegenmaßnahme |
|---|---|
| Lange Regeln passen nicht in eine Anweisung | Pflichtregeln in der Anweisung, Details als Wissen aus `references/` |
| Wissen wird nur auszugsweise durchsucht | Die Werkstatt prüft jedes Ergebnis mit den vorhandenen Skripten und gibt Fehler an den Agenten zurück |
| Websuche liefert nur Snippets | Tool „Quelle abrufen“ öffnet Seiten und PDFs vollständig (`source-cache.py`) |
| Zitate gehen zwischen Agenten verloren | Quellen stehen als Datenfelder im Ergebnis, nicht als Zitat |
| Agenten schreiben Prüfsummen falsch ab | Die Werkstatt ergänzt Kopf, Quellen-IDs und Prüfsummen |
| Prüfung soll unabhängig sein | Prüfer sind eigene Agenten ohne Verlauf; Autoren und Prüfer teilen nie einen Kontext |
| Ein Agent wartet höchstens rund 2 Minuten auf einen Flow | Der Flow meldet sofort „gestartet“ und läuft danach weiter (Testpunkt T1) |

## 7. Pflege

- **Fachliche Änderung** (z. B. eine neue Regel zur Quellenprüfung):
  in `references/` ändern, das Wissen des betroffenen Agenten neu hochladen.
  Betrifft sie eine Pflichtregel, auch den Anweisungsblock in `agenten/` anpassen.
- **Darstellungsänderung:** in `scripts/` und `references/templates/` ändern.
  Die Werkstatt nutzt sie automatisch.
- **Modelländerung:** in `references/modellaufteilung.json` und im Steckbrief
  des Agenten anpassen.

## 8. Offen und bewusst noch nicht gebaut

- **Werkstatt-Code:** Die Schnittstelle steht, der Code noch nicht. Er wird eine
  dünne Hülle um `scripts/`.
- **Auswahl für die Bewertung:** In der ersten Version bekommt die
  Positionierung alle A-geprüften Kernfakten. Eine engere Auswahl spart später
  Token.
- **Testpunkte T1 bis T8:** müssen im eigenen Mandanten beantwortet werden,
  bevor der Flow gebaut wird.
- **Effort je Agent:** in Copilot Studio nicht einstellbar; die Modellwahl
  bleibt.
