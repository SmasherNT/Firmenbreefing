# Firmenbriefing in Copilot Studio · schlanke Variante ohne Prüfagenten

**4 Agenten statt 15, 11 Aufrufe statt 21.** Es gibt keine Prüfagenten. Die
Rechercheagenten prüfen sich selbst, und Code prüft die Formate. Das Ergebnis
ist ein **sichtbar gekennzeichneter ungeprüfter Entwurf**.

Funktioniert wie die vollständige Variante in [`../copilot-studio/`](../copilot-studio/):
nur Agenten und Skills hochladen, kein Backend, kein Hilfsskript, du schaltest
die Aufrufe selbst in Reihe.

**Schaltplan mit allen Ein- und Ausgabedateien:** [`schaltplan.html`](schaltplan.html),
als Bild [`schaltplan.png`](schaltplan.png).

---

## 1. Die vier Agenten

| ID | Agent | Parameter | Aufgaben | Modell | Websuche |
|---|---|---|---|---|---|
| [R1](bausteine/R1-recherche/agent.md) | Recherche | `modul`: `context`, `portfolio`, `focus:<id>` | Kontext & Person, Portfolio & Präsenz, je Fokusthema | Sonnet 5.5 | an |
| [R2](bausteine/R2-tiefenrecherche/agent.md) | Tiefenrecherche | `modul`: `auftrag`, `cluster`, `market` | Auftrag & Vergleichsplan, Cluster & Netzwerk, Markt & Wettbewerb | Opus 5.5 | an |
| [B1](bausteine/B1-bewertung/agent.md) | Bewertung | `schritt`: `positioning`, `swot` | Positionierung, danach SWOT | Opus 5.5 | aus |
| [W1](bausteine/W1-werkzeug/agent.md) | Werkzeug | `schritt`: `fakten`, `swot`, `abschluss` | Formatprüfung, Prüfpaket, Kontexte, HTML | klein | aus |

Derselbe Agent wird mit unterschiedlichem Parameter mehrfach aufgerufen. Jeder
Aufruf startet trotzdem frisch und kennt nur seine Eingangsdateien.

## 2. Ablauf

```
anfrage.txt
  → R2 auftrag
  → R1 context · R1 portfolio · R2 cluster · R2 market · R1 focus je Thema
  → W1 fakten        Formattor 1
  → B1 positioning
  → W1 swot          Formattor 2
  → B1 swot
  → W1 abschluss     Formattor 3 → briefing.html (ungeprüfter Entwurf)
```

**Kurzbriefing:** `anfrage.txt` beginnt mit `modus: kurz`, dann nur
R2 auftrag → R1 context · R1 portfolio → W1 fakten → W1 abschluss.

**Formattore:** `pruefergebnis.json` meldet nur Formatfehler und Rückfragen,
keine inhaltliche Prüfung.

| owner in `rueckgabe` | erneut aufrufen | danach weiter mit |
|---|---|---|
| `auftrag` | R2 `modul: auftrag` | Schritt 2 |
| `context`, `portfolio` | R1 mit diesem `modul` | W1 `fakten` |
| `focus:<id>` | R1 `modul: focus:<id>` | W1 `fakten` |
| `cluster`, `market` | R2 mit diesem `modul` | W1 `fakten` |
| `positioning` | B1 `schritt: positioning` | W1 `swot` |
| `swot` | B1 `schritt: swot` | W1 `abschluss` |
| `werkzeug` | keiner, technischer Fehler | Meldung lesen, Schritt wiederholen |

## 3. Was ohne Prüfagenten wegfällt und was bleibt

| | Vollständige Variante | Schlanke Variante |
|---|---|---|
| Unabhängige Quellenprüfung je Aussage | Dokumentprüfung und Leitprüfung | **keine** |
| Prüfung der Bewertung (Schlussprüfung) | Leitprüfung final | **keine** |
| Formatprüfung, Quellen-IDs, Prüfsummen | Werkzeug-Agenten | gleich, durch W1 |
| Selbstprüfung der Recherche | Teil der Arbeitsweise | ausdrücklich im Skill vorgeschrieben |
| HTML-Vorlage und Inhalt | gleich | gleich |
| Kennzeichnung | „Geprüfte Fakten“ | „Ungeprüfter Entwurf · ohne unabhängige Quellenprüfung“ |
| Agenten / Aufrufe (Voll) | 15 / 21 | 4 / 11 |
| Geeignet für | Top-Management, belastbare Entscheidungsvorlage | schneller Überblick, interne Vorbereitung |

Die Review-Dateien `review-basis.md` und `review-final.md` entstehen trotzdem,
weil der Renderer sie braucht. Sie vermerken ausdrücklich „keine unabhängige
Prüfung“ und „ohne unabhängige Quellenprüfung aus der Recherche übernommen“.
Im Briefing stehen oben ein Hinweis und im Kopf das Kennzeichen
„Ungeprüfter Entwurf“. Im Quellenverzeichnis steht „nicht unabhängig geprüft“.

Diese Variante weicht bewusst von der Regel in `CLAUDE.md` ab, nach der eine
finale Ausgabe eine Quellenprüfung voraussetzt. Deshalb die Kennzeichnung.

## 4. Inhalt des Ordners

| Pfad | Inhalt |
|---|---|
| `upload/` | **zum Hochladen:** `skills/` (4 Pakete), `agenten/` (4 Steckbriefe), `schaltplan.png` |
| `bausteine/<ID>/agent.md` | Steckbrief: Einstellungen, Anschlüsse, Anweisungstext |
| `bausteine/<ID>/skill/` | Skill: `SKILL.md`, bei W1 zusätzlich `werkzeug.py` |
| `bausteine.json` | die vier Agenten als Daten |
| `schaltplan.html`, `schaltplan.png` | Schaltplan mit allen Dateien |
| `tests/test_schlank.py` | Durchlauf Voll und Kurz mit Demodaten |

Die Skills von R1, R2 und B1 sind aus den Skills der vollständigen Variante
zusammengesetzt (A01–A06, A09, A10) und um die Selbstprüfung ergänzt. Wird dort
eine Fachregel geändert, hier ebenfalls anpassen.

## 5. Hochladen

Je Agent in Copilot Studio:

1. Agent anlegen, Name wie im Steckbrief in `upload/agenten/`.
2. Modell und Websuche laut Tabelle oben.
3. Skill-Paket aus `upload/skills/` hochladen und zuordnen.
4. Tools: die SharePoint-Aktionen laut Steckbrief (R1, R2, B1 je 4; W1 7),
   dazu Websuche bei R1 und R2 und Code-Ausführung bei W1.
5. Anweisungstext aus dem Steckbrief einfügen.

Danach nach `schaltplan.png` im Agent Flow in Reihe schalten. Vor dem ersten
Lauf testen: **T1** (W1 führt `werkzeug.py` aus) und **T3** (Agenten lesen und
schreiben Dateien im Lauf-Ordner).

## 5a. SharePoint einrichten (einmalig)

Agenten übernehmen Dateien **nur über einen gemeinsamen Lauf-Ordner in
SharePoint**. Dateien, die ein Agent im Chat als Dateikarte ausgibt, sieht der
nächste Agent nicht; einen zentralen Ablageort kann man in Copilot Studio nicht
einstellen. Deshalb liest und schreibt jeder Agent selbst über den
SharePoint-Connector.

1. **Bibliothek anlegen:** eine SharePoint-Site, darin die Dokumentbibliothek
   `Briefings`.
2. **Je Briefing einen Lauf-Ordner:** `Briefings/<firma>-<datum>/`, darin
   `anfrage.txt`. Alle weiteren Dateien schreiben die Agenten hierhin.
3. **Je Agent die SharePoint-Aktionen hinzufügen** (Tools → Add a tool →
   Connector → SharePoint), wie im Abschnitt „SharePoint-Tools einrichten“ des
   Steckbriefs. Denk-Agenten brauchen 4 Aktionen, Werkzeug-Agenten 7.
4. **Site-Adresse festlegen:** in jeder Aktion unter Inputs „Site Address“ auf
   „Custom value“ mit eurer Site-Adresse, z. B.
   `https://<firma>.sharepoint.com/sites/<site>`. Damit ist festgelegt, **wo**
   abgelegt wird. Ordnerpfad und Dateiname füllt der Agent selbst.
5. **Anmeldung:** „End user“ (jeder Nutzer braucht Schreibrechte auf
   `Briefings` und legt beim ersten Aufruf seine eigene Verbindung an) oder
   „Maker-provided“ (eine zentrale Verbindung).
6. **Aufruf:** Jeder Agent bekommt die Nachricht `Lauf-Ordner: Briefings/<ordner>`
   (plus Parameter laut Schaltplan).

Werkzeug-Agenten laden den ganzen Lauf-Ordner in ihre Sandbox, führen ihr
Skript aus und schreiben genau die Dateien zurück, die das Skript in seiner
letzten Ausgabezeile `DATEIEN` als geändert oder gelöscht meldet.

## 6. Prüfen und neu bauen

Aus dem Repository-Stamm:

```bash
python3 -m unittest discover -s copilot-studio-schlank/tests -p 'test_*.py'
```

```bash
python3 copilot-studio/steckbriefe-bauen.py copilot-studio-schlank
```

```bash
python3 copilot-studio/skills-bauen.py --quelle copilot-studio-schlank --upload copilot-studio-schlank/upload
```

Der Test zeigt: Mit den Demodaten entsteht dieselbe HTML wie im heutigen
Ablauf, nur die Prüfkennzeichnung ist durch „ungeprüft“ ersetzt. Das
Kurzbriefing läuft ebenfalls durch.
