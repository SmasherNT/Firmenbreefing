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
| A01 | Auftrag | [`agenten/A01-auftrag.md`](agenten/A01-auftrag.md) | `skills/briefing-auftrag.zip` | Opus 5.5 | Websuche, SharePoint (4 Aktionen) |
| A02 | Kontext & Person | [`agenten/A02-kontext.md`](agenten/A02-kontext.md) | `skills/briefing-kontext.zip` | Sonnet 5.5 | Websuche, SharePoint (4 Aktionen) |
| A03 | Portfolio & Präsenz | [`agenten/A03-portfolio.md`](agenten/A03-portfolio.md) | `skills/briefing-portfolio.zip` | Sonnet 5.5 | Websuche, SharePoint (4 Aktionen) |
| A04 | Cluster & Netzwerk | [`agenten/A04-cluster.md`](agenten/A04-cluster.md) | `skills/briefing-cluster.zip` | Opus 5.5 | Websuche, SharePoint (4 Aktionen) |
| A05 | Markt & Wettbewerb | [`agenten/A05-markt.md`](agenten/A05-markt.md) | `skills/briefing-markt.zip` | Opus 5.5 | Websuche, SharePoint (4 Aktionen) |
| A06 | Fokusthema | [`agenten/A06-fokus.md`](agenten/A06-fokus.md) | `skills/briefing-fokus.zip` | Sonnet 5.5 | Websuche, SharePoint (4 Aktionen) |
| A07 | Dokumentprüfung | [`agenten/A07-dokumentpruefung.md`](agenten/A07-dokumentpruefung.md) | `skills/briefing-dokumentpruefung.zip` | Sonnet 5.5 | SharePoint (4 Aktionen) |
| A08 | Leitprüfung | [`agenten/A08-leitpruefung.md`](agenten/A08-leitpruefung.md) | `skills/briefing-leitpruefung.zip` | Sonnet 5.5 | SharePoint (4 Aktionen) |
| A09 | Positionierung | [`agenten/A09-positionierung.md`](agenten/A09-positionierung.md) | `skills/briefing-positionierung.zip` | Opus 5.5 | SharePoint (4 Aktionen) |
| A10 | SWOT | [`agenten/A10-swot.md`](agenten/A10-swot.md) | `skills/briefing-swot.zip` | Sonnet 5.5 | SharePoint (4 Aktionen) |
| W1 | Prüfpaket | [`agenten/W1-pruefpaket.md`](agenten/W1-pruefpaket.md) | `skills/werkzeug-pruefpaket.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, SharePoint (7 Aktionen) |
| W2 | Befunde bündeln | [`agenten/W2-befunde.md`](agenten/W2-befunde.md) | `skills/werkzeug-befunde.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, SharePoint (7 Aktionen) |
| W3 | Freigabe | [`agenten/W3-freigabe.md`](agenten/W3-freigabe.md) | `skills/werkzeug-freigabe.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, SharePoint (7 Aktionen) |
| W4 | Bewertungskontext | [`agenten/W4-bewertungskontext.md`](agenten/W4-bewertungskontext.md) | `skills/werkzeug-bewertungskontext.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, SharePoint (7 Aktionen) |
| W5 | Briefing rendern | [`agenten/W5-rendern.md`](agenten/W5-rendern.md) | `skills/werkzeug-rendern.zip` | Sonnet 5.5 (nur Ausführung) | Code-Ausführung, SharePoint (7 Aktionen) |

## SharePoint einrichten (einmalig)

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

## Je Agent in Copilot Studio

1. Agent anlegen, Name wie im Steckbrief.
2. Modell und Websuche laut Steckbrief einstellen.
3. Skill-Paket aus `skills/` hochladen und dem Agenten zuordnen.
4. Tools laut Tabelle hinzufügen, die SharePoint-Aktionen wie im Steckbrief unter „SharePoint-Tools einrichten“.
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
