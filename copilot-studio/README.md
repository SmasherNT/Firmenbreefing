# Firmenbriefing in Microsoft Copilot Studio

Das Firmenbriefing besteht in Copilot Studio nur aus **Agenten mit Skills**.
Jeder Agent ist ein Baustein mit festen Eingangs- und Ausgangsdateien, läuft
auch für sich allein und kennt keine anderen Agenten. **Du steckst die Bausteine
selbst zusammen**, im Agent Flow oder von Hand.

Dieser Ordner ist aus der aktuellen Fassung des Repositorys neu strukturiert.
Die fachlichen Regeln (`references/`) und die Skripte (`scripts/`) bleiben die
einzige Quelle. Sie werden erst beim Bauen der Skill-Pakete eingepackt, nicht
in diesen Ordner kopiert.

**Zielbild mit Diagrammen:** [`zielbild/zielbild.html`](zielbild/zielbild.html),
als Bilder [`ablauf-vollbriefing.png`](zielbild/ablauf-vollbriefing.png) und
[`ablauf-kurzbriefing.png`](zielbild/ablauf-kurzbriefing.png).

---

## 1. Grundprinzip

| | Denk-Agenten (A01–A10) | Werkzeug-Agenten (W1–W5) |
|---|---|---|
| Aufgabe | recherchieren, prüfen, bewerten | Formate prüfen, Prüfpakete bauen, freigeben, rendern |
| Skill enthält | Arbeitsweise, Dateiformat, Fachregeln aus `references/` | ein eigenes Startskript plus die vorhandenen Skripte aus `scripts/` |
| Pro Aufruf | eigene Arbeit des Modells | genau ein Befehl, z. B. `python3 w5_rendern.py --lauf <Ordner>` |
| Modell | Opus 5.5 oder Sonnet 5.5 nach heutiger Zuordnung | kleines Modell genügt, es führt nur aus |

Für alle Bausteine gilt:

1. **Feste Anschlüsse:** Ein Baustein liest nur seine Eingangsdateien und
   schreibt nur seine Ausgangsdateien im Lauf-Ordner.
2. **Frischer Start:** Jeder Aufruf beginnt ohne Vorwissen.
3. **Kein Baustein ruft einen anderen auf.** Die Reihenfolge legst du fest.
4. **Gleiches Ergebnis wie heute:** Die Werkzeug-Agenten nutzen die vorhandenen
   Prüf- und Renderskripte unverändert. Der Test unten zeigt: Mit den Demodaten
   entsteht über W1–W5 byte-genau dieselbe HTML wie im heutigen Ablauf.
5. **Nur Agenten und Skills:** Es gibt kein Backend und kein Hilfsskript
   außerhalb der Skills. Jeder Skill enthält alles, was er braucht.

## 2. Die Bausteine

| ID | Baustein | Eingänge | Ausgänge | Modell |
|---|---|---|---|---|
| [A01](bausteine/A01-auftrag/agent.md) | Auftrag | `anfrage.txt` | `auftrag.md`, `facts-run.json`, `comparison-plan.json` | Opus 5.5 |
| [A02](bausteine/A02-kontext/agent.md) | Kontext & Person | `auftrag.md`, `facts-run.json` | `context-facts.json` | Sonnet 5.5 |
| [A03](bausteine/A03-portfolio/agent.md) | Portfolio & Präsenz | `auftrag.md`, `facts-run.json` | `portfolio-facts.json` | Sonnet 5.5 |
| [A04](bausteine/A04-cluster/agent.md) | Cluster & Netzwerk | `auftrag.md`, `facts-run.json` | `cluster-facts.json` | Opus 5.5 |
| [A05](bausteine/A05-markt/agent.md) | Markt & Wettbewerb | + `comparison-plan.json` | `market-facts.json` | Opus 5.5 |
| [A06](bausteine/A06-fokus/agent.md) | Fokusthema (je Thema) | `auftrag.md`, `facts-run.json`, `focus_id` | `focus-<id>-facts.json` | Sonnet 5.5 |
| [W1](bausteine/W1-pruefpaket/agent.md) | Prüfpaket | alle `*-facts.json` | `review-packet.json`, `pruefjob-<n>.json`, `pruefergebnis.json` | klein |
| [A07](bausteine/A07-dokumentpruefung/agent.md) | Dokumentprüfung (je Job) | `pruefjob-<n>.json` | `befund-<n>.json` | Sonnet 5.5 |
| [W2](bausteine/W2-befunde/agent.md) | Befunde bündeln | `befund-*.json` | `leitpruefung-eingabe.json` | klein |
| [A08](bausteine/A08-leitpruefung/agent.md) | Leitprüfung | `leitpruefung-eingabe.json` | `leitentscheid.json` | Sonnet 5.5 |
| [W3](bausteine/W3-freigabe/agent.md) | Freigabe | `leitentscheid.json`, Befunde | `review-basis.md` / `review-final.md`, `pruefergebnis.json` | klein |
| [W4](bausteine/W4-bewertungskontext/agent.md) | Bewertungskontext | Prüfpaket, Review, ggf. `positioning.json` | `positioning-context.json` / `swot-context.json`, `pruefergebnis.json` | klein |
| [A09](bausteine/A09-positionierung/agent.md) | Positionierung | `positioning-context.json` | `positioning.json` | Opus 5.5 |
| [A10](bausteine/A10-swot/agent.md) | SWOT | `swot-context.json` | `swot.json` | Sonnet 5.5 |
| [W5](bausteine/W5-rendern/agent.md) | Briefing rendern | alle freigegebenen Dateien | `briefing.html` | klein |

Die Modelle der Denk-Agenten entsprechen `references/modellaufteilung.json`.
Den Effort (medium/high) kann man in Copilot Studio nach heutigem Stand nicht
je Agent einstellen.

## 3. Ablauf

```
anfrage.txt
  → A01
  → A02 · A03 · A04 · A05 · A06 je Thema
  → W1 (basis) → A07 je Job → W2 → A08 → W3        Prüftor 1
       nicht bestanden: zuständiger Baustein korrigiert → W1
  → W4 (positioning) → A09 → W4 (swot) → A10
  → W1 (final) → A07 je Job → W2 → A08 → W3        Prüftor 2
       nicht bestanden: A09 bzw. A10 korrigiert
  → W5 → briefing.html
```

**Kurzbriefing:** A01 → A02 · A03 → W1 → A07 → W2 → A08 → W3 → W5.

Genaue Rezepte, Prüftore und die Zuordnung „Rückgabe an welchen Baustein“:
[`verknuepfung.md`](verknuepfung.md). Alle Dateien und wer sie liest und
schreibt: [`dateien.md`](dateien.md).

## 4. Inhalt des Ordners

| Pfad | Inhalt |
|---|---|
| `bausteine/<ID>/agent.md` | Steckbrief: Einstellungen, Anschlüsse, Anweisungstext zum Einfügen |
| `bausteine/<ID>/skill/` | Skill: `SKILL.md`, bei W1–W5 zusätzlich das Startskript `w<n>_….py` |
| `bausteine.json` | alle Bausteine als Daten: Anschlüsse, Modell, Paketinhalt |
| `skills-bauen.py` | baut je Baustein ein Skill-Paket (`.zip`) aus dem Repository |
| `steckbriefe-bauen.py` | erzeugt alle `agent.md` aus `bausteine.json` |
| `verknuepfung.md` | wie du die Bausteine im Flow verknüpfst, Rezepte, Testpunkte |
| `dateien.md` | Dateivertrag des Lauf-Ordners |
| `tests/test_bausteine.py` | Durchlauf W1–W5 mit Demodaten aus den gebauten Paketen |
| `zielbild/` | Diagramme |

## 5. Einen Baustein in Copilot Studio anlegen

1. Skill-Pakete bauen (aus dem Repository-Stamm):

   ```bash
   python3 copilot-studio/skills-bauen.py --out dist/skills
   ```

2. In Copilot Studio einen neuen Agenten anlegen, Name wie im Steckbrief.
3. Modell und Websuche laut Steckbrief einstellen.
4. Skill-Paket `<skill>.zip` hochladen und dem Agenten zuordnen.
5. Tools hinzufügen: SharePoint (Datei lesen, Datei schreiben), bei Werkzeug-
   Agenten die Code-Ausführung.
6. Den Anweisungstext aus `agent.md` in das Anweisungsfeld kopieren.
7. Einzeln testen: im Chat „Lauf-Ordner: …“ schreiben und die Dateien prüfen.

## 6. Aufbau Schritt für Schritt

| Stufe | Was tun | Fertig, wenn |
|---|---|---|
| **0 Voraussetzungen** | Umgebung, Copilot Credits, Claude-Modelle, Websuche, SharePoint-Bibliothek „Briefings“ | ein Test-Agent mit Claude antwortet |
| **1 Machbarkeit** | Testpunkte T1–T10 aus [`verknuepfung.md`](verknuepfung.md) klären, vor allem T1 (Skripte in der Sandbox) und T3 (SharePoint-Dateien) | alle Testpunkte beantwortet |
| **2 Pakete bauen** | `skills-bauen.py` ausführen, Test laufen lassen | Test grün (lokal bereits erfüllt) |
| **3 Bausteine einzeln** | A01–A08 und W1–W3, W5 anlegen und einzeln testen | jeder Baustein schreibt gültige Dateien |
| **4 Kurzbriefing** | Rezept Kurz im Agent Flow verknüpfen | ein echtes Kurzbriefing; ein falscher Fakt geht zurück und wird korrigiert |
| **5 Vollbriefing** | A09, A10, W4 dazu, Rezept Voll | Vollbriefing mit zwei Fokusthemen, inhaltlich wie ein heutiger Lauf |
| **6 Freigabe für alle** | Einstieg für Nutzer (z. B. Teams), Verbrauch beobachten | Pilot mit drei Nutzern und drei Firmen |

## 7. Pflege

- **Fachregel ändern:** in `references/` ändern, Skill-Pakete neu bauen und
  hochladen. Betrifft es eine Pflichtregel, auch `SKILL.md` anpassen.
- **Darstellung ändern:** in `scripts/` und `references/templates/`; die
  Werkzeug-Pakete neu bauen und den Test laufen lassen.
- **Baustein ändern:** zuerst `bausteine.json`, dann `steckbriefe-bauen.py`
  ausführen und `SKILL.md` anpassen.
- **Startskripte W1–W5:** Der Block zwischen `# --- gemeinsam: anfang` und
  `# --- gemeinsam: ende` ist in allen fünf gleich; der Test prüft das.

Test (aus dem Repository-Stamm):

```bash
python3 -m unittest discover -s copilot-studio/tests -p 'test_*.py'
```

## 8. Noch offen

- **Testpunkte T1–T10** im eigenen Mandanten, vor allem T1 (führt ein Agent das
  Python-Startskript aus seinem Skill aus?) und T3 (Dateien im
  SharePoint-Lauf-Ordner lesen und schreiben).
- **Quellenabruf in der Sandbox (T2):** Ohne Internet lädt W1 keine Originale
  in den Cache; die Prüfung läuft trotzdem, A07 öffnet die Quellen dann selbst.
- **Faktenauswahl für die Bewertung:** Version 1 nimmt alle A-geprüften
  Kernfakten. Eine engere Auswahl spart später Token.
- **Einstieg für alle Nutzer:** Wer den Lauf-Ordner anlegt und den Flow startet,
  wird nach dem Pilot festgelegt.
