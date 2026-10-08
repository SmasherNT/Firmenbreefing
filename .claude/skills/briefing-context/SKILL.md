---
name: briefing-context
description: Recherchiert Nutzerthemen, beruflichen Gesprächspartner und Marktkontext eines Firmenbriefings.
---

Der Hauptagent wendet diese Methode selbst an.
Lies input/auftrag.md, CLAUDE.md und alle references-Vorlagen (inkl. quellenzugang.md) sowie
work/portfolio.md und work/cluster.md. Fehlende Eingaben konkret melden.
1. Markt: relevante Kundengruppen, Nachfrage, Wettbewerb und externe
   Eintrittshürden recherchieren. Verknüpfe Faktoren mit realen Angeboten.
   M-Claims nach uebergabe.md in work/markt.md erfassen.
2. Themen: jedes Nutzerthema separat bearbeiten, kein Thema überspringen.
   T-Claims und Übersicht je Thema in work/kontext.md schreiben.
   Kooperationen mit Fahrzeugherstellern: konkrete Hersteller/Partner,
   Produkt/Integration, Zweck, angekündigt/erprobt/beauftragt/ausgeliefert,
   belegtes Datum und Quelle; Zulieferer nicht automatisch als OEM einordnen.
   Business Development Middle East: pro belegtem Land Aktivitäten, Partner,
   Kunden, Präsenz, Projekte und Status trennen. Middle East nicht pauschal
   mit GCC gleichsetzen. Keine Geschäftspräsenz aus Exportfähigkeit ableiten.
   Länderabgrenzung transparent angeben. Chancen als Interpretation markieren.
   Sonstige Themen mit gleichwertiger Beleg- und Statusprüfung behandeln.
3. Person falls genannt: offizielle Firmenbiografie und aktuelle berufliche
   Primärquellen suchen (Firmen-Newsroom per tools/quellenabruf.py news --suche
   <Name>). Zusätzlich öffentliche berufliche Profile: Referenten-/Programmseiten
   von Konferenzen, Preise/Auszeichnungen mit Vita, Hochschul-/Alumni-Seiten,
   Handelsregistermeldungen, Gründungs-/Übernahmemitteilungen.
   Werdegang als Zeitleiste (Zeitraum, Organisation, Rolle, Quelle, H-Claim).
   Identität je Station belegen: gleiche Person nur, wenn eine Quelle die
   Verbindung herstellt (z. B. Firma + Name + Rolle); sonst als Interpretation.
   Ein Rollennachweis belegt den Nachweiszeitpunkt, kein Eintrittsdatum.
   Position laut Nutzer mit bestätigter Rolle abgleichen, Abweichungen nennen.
   Keine privaten Daten (Wohnort, Familie, private Kontakte), keine erfundenen
   Regionalbeziehungen; LinkedIn nur, wenn öffentlich ohne Login abrufbar.
4. Verbindung Person/Thema nur bei Beleg; sonst „öffentlich nicht belegt“.
Beide Dateien mit gemeinsamen Modulkopf, Claims, Lücken und Status liefern.
Keine SWOT vorwegnehmen und keine Marktgröße ohne belegte Abgrenzung nennen.
