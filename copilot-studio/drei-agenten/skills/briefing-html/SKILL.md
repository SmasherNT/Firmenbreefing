---
name: briefing-html
description: Erzeugt aus briefing-daten.xlsx oder briefing-daten-geprueft.xlsx eine eigenständige Firmenbriefing-HTML im festen Layout mit Reitern, Executive Summary, Reifematrix, Unternehmensnetzwerk, Präsenzprofilen, Capability Matrix, Gesprächspartner- und Fokusseiten und Quellenregister. Verwenden, wenn eine Briefing-Excel in eine HTML umgewandelt werden soll.
---

# Briefing-HTML

Die HTML entsteht ausschließlich durch das Skript `scripts/briefing_html.py`.
Es nutzt eine feste Vorlage und feste Bausteine: die Skripte `*-html.py` und
`vorlagen.py` im selben Ordner. Alle Skripte müssen zusammen in `scripts/` liegen.
Schreibe oder ändere nie selbst HTML, CSS oder JavaScript, und erfinde keine
Inhalte. Alles, was in der HTML steht, kommt aus der Datei des Nutzers.

## Ablauf

1. Hochgeladene Datei finden: `briefing-daten.xlsx` vom Recherche-Agenten oder
   `briefing-daten-geprueft.xlsx` vom Prüf-Agenten. Eine frühere Briefing-HTML
   oder eine JSON-Datei geht auch.
2. Skript mit vollständigem Pfad im Skillordner aufrufen; ist der Pfad unklar,
   `briefing_html.py` im Dateisystem suchen:

   ```bash
   python3 scripts/briefing_html.py --daten briefing-daten-geprueft.xlsx --out briefing.html
   ```

3. Meldet das Skript Fehler, keine HTML ausgeben. Die Fehler kurz und
   verständlich nennen und sagen, welcher Agent sie beheben muss: inhaltliche
   Fehler der Recherche-Agent, Prüffehler der Prüf-Agent.
4. Sonst genau eine Datei ausgeben: `briefing.html`.

## Antwort im Chat

Kurz: Firma, Stichtag, Prüfstatus (ungeprüft oder Ergebnis der Prüfung), welche
Reiter die HTML hat, und die Zahl der technischen Hinweise aus der Abnahme.
Keine Inhalte aus dem Briefing nacherzählen, keine eigenen Bewertungen ergänzen.

## Was die HTML enthält

| Reiter | Inhalt |
|---|---|
| Überblick | Prüfstatus, Executive Summary, aktuelle Entwicklungen, Unternehmen im Überblick, Portfolio mit Reifematrix, Unternehmensnetzwerk, regionale Präsenz, Capability Matrix, Einordnung, SWOT, Datenlücken |
| je Gesprächspartner | Profil, Werdegang, Fachprofil, Medien der letzten vier Monate |
| je Fokusthema | Themen- und Marktbriefing mit Kennzahlen, Akteuren, Entwicklungen und Fragen |
| Quellen | Prüfbericht mit Änderungsprotokoll (nach Prüfung), Fakten- und Interpretationsregister, Dokumente, Abnahme |

Kapitel ohne Daten entfallen automatisch. Die Daten stecken zusätzlich unsichtbar
in der HTML, damit sie später wieder eingelesen werden können.
