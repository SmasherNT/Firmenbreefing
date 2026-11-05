# Upload-Paket Firmenbriefing für Copilot Studio

Alles, was in Copilot Studio hochgeladen wird: 15 Agenten-Steckbriefe, 15
Skill-Pakete und der Schaltplan. Sonst wird nichts installiert.

| Inhalt | Zweck |
|---|---|
| `schaltplan.png` | Reihenfolge der 21 Aufrufe mit allen Ein- und Ausgabedateien und den Prüftoren |
| `agenten/` | je Agent: Einstellungen, Anschlüsse und Anweisungstext zum Einfügen |
| `skills/` | je Agent ein Skill-Paket (`.zip`) zum Hochladen |

## Zuordnung

| ID | Agent | Steckbrief | Skill-Paket | Modell | Tools |
|---|---|---|---|---|---|
| A01 | Auftrag | [`agenten/A01-auftrag.md`](agenten/A01-auftrag.md) | `skills/briefing-auftrag.zip` | Opus 5.5 | Websuche, Lauf-Ordner lesen/schreiben |
| A02 | Kontext & Person | [`agenten/A02-kontext.md`](agenten/A02-kontext.md) | `skills/briefing-kontext.zip` | Sonnet 5.5 | Websuche, Lauf-Ordner lesen/schreiben |
| A03 | Portfolio & Präsenz | [`agenten/A03-portfolio.md`](agenten/A03-portfolio.md) | `skills/briefing-portfolio.zip` | Sonnet 5.5 | Websuche, Lauf-Ordner lesen/schreiben |
| A04 | Cluster & Netzwerk | [`agenten/A04-cluster.md`](agenten/A04-cluster.md) | `skills/briefing-cluster.zip` | Opus 5.5 | Websuche, Lauf-Ordner lesen/schreiben |
| A05 | Markt & Wettbewerb | [`agenten/A05-markt.md`](agenten/A05-markt.md) | `skills/briefing-markt.zip` | Opus 5.5 | Websuche, Lauf-Ordner lesen/schreiben |
| A06 | Fokusthema | [`agenten/A06-fokus.md`](agenten/A06-fokus.md) | `skills/briefing-fokus.zip` | Sonnet 5.5 | Websuche, Lauf-Ordner lesen/schreiben |
| A07 | Dokumentprüfung | [`agenten/A07-dokumentpruefung.md`](agenten/A07-dokumentpruefung.md) | `skills/briefing-dokumentpruefung.zip` | Sonnet 5.5 | Lauf-Ordner lesen/schreiben |
| A08 | Leitprüfung | [`agenten/A08-leitpruefung.md`](agenten/A08-leitpruefung.md) | `skills/briefing-leitpruefung.zip` | Sonnet 5.5 | Lauf-Ordner lesen/schreiben |
| A09 | Positionierung | [`agenten/A09-positionierung.md`](agenten/A09-positionierung.md) | `skills/briefing-positionierung.zip` | Opus 5.5 | Lauf-Ordner lesen/schreiben |
| A10 | SWOT | [`agenten/A10-swot.md`](agenten/A10-swot.md) | `skills/briefing-swot.zip` | Sonnet 5.5 | Lauf-Ordner lesen/schreiben |
| W1 | Prüfpaket | [`agenten/W1-pruefpaket.md`](agenten/W1-pruefpaket.md) | `skills/werkzeug-pruefpaket.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, Lauf-Ordner lesen/schreiben |
| W2 | Befunde bündeln | [`agenten/W2-befunde.md`](agenten/W2-befunde.md) | `skills/werkzeug-befunde.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, Lauf-Ordner lesen/schreiben |
| W3 | Freigabe | [`agenten/W3-freigabe.md`](agenten/W3-freigabe.md) | `skills/werkzeug-freigabe.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, Lauf-Ordner lesen/schreiben |
| W4 | Bewertungskontext | [`agenten/W4-bewertungskontext.md`](agenten/W4-bewertungskontext.md) | `skills/werkzeug-bewertungskontext.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, Lauf-Ordner lesen/schreiben |
| W5 | Briefing rendern | [`agenten/W5-rendern.md`](agenten/W5-rendern.md) | `skills/werkzeug-rendern.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, Lauf-Ordner lesen/schreiben |

## Je Agent in Copilot Studio

1. Agent anlegen, Name wie im Steckbrief.
2. Modell und Websuche laut Steckbrief einstellen.
3. Skill-Paket aus `skills/` hochladen und dem Agenten zuordnen.
4. Tools laut Tabelle hinzufügen.
5. Anweisungstext aus dem Steckbrief (Abschnitt „Anweisungen“) einfügen.
6. Einzeln testen: im Chat `Lauf-Ordner: <Pfad>` schreiben und die Dateien prüfen.

Danach die Agenten nach `schaltplan.png` im Agent Flow in Reihe schalten.
Kurzbriefing: nur die Schritte mit Punkt.

## Vor dem ersten Lauf testen

- **T1:** Führt ein Werkzeug-Agent (z. B. W5) das Python-Startskript aus seinem Skill aus?
- **T3:** Liest und schreibt ein Agent Dateien im Lauf-Ordner?

## Herkunft und Neubau

Dieser Ordner wird erzeugt, nicht von Hand gepflegt. Quelle sind
`copilot-studio/` (Agenten, Skills, Schaltplan) sowie `references/` und
`scripts/`. Nach Änderungen neu bauen (aus dem Repository-Stamm):

```bash
python3 copilot-studio/skills-bauen.py --upload copilot-studio-upload
```

Gleicher Inhalt ergibt bitgleiche Pakete. Ausführliche Erklärung:
[`copilot-studio/README.md`](../copilot-studio/README.md).
