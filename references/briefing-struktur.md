# Verbindliche Struktur und Ausgabeabnahme
## HTML-Reihenfolge
1. Kopf: Firma, Stichtag, Themen, genannte Person/Position mit Quellenstatus.
2. Executive Summary: 4–6 belegte, für die Nutzerthemen relevante Kernaussagen.
3. Je Nutzerthema ein eigenes Kapitel, in Nutzerreihenfolge:
   belegte Lage, relevante Akteure/Produkte, Status/Datum, Bedeutung als
   Analysteninterpretation, Datenlücken und daraus abgeleitete Gesprächsfragen.
4. Beruflicher Gesprächspartner-Kontext, falls genannt: belegte aktuelle Rolle,
   Zuständigkeit und beruflicher Werdegang als Zeitleiste mit Quelle je Station.
   Nutzerangabe und verifizierte Information sichtbar unterscheiden.
5. Firmenbasis: Portfolio mit Reifegrad-Skala (Stufe 1–6, Kriterien sichtbar,
   Zählung je Stufe, H/U-Kennzeichnung), Struktur/Partnerschaften nach
   Kategorien (Töchter, Zukäufe, JVs, Investoren, Partner, Distributoren je
   Land, Kunden), Markt/Wettbewerb.
6. Themenbezogene SWOT, bis 3 Punkte je Quadrant; je Punkt aufklappbar
   Evidenz, strategische Bedeutung und positiver/negativer Beitrag.
7. Offene Punkte und Gesprächsfragen (Vorschläge, keine Firmenbehauptungen).
8. Quellenregister je Modul mit Quellentyp, Claim-Zuordnung, Titel, Datum,
   Direktlink, Abrufdatum und Evidenzhinweis; jeder Abschnitt verlinkt
   „Quellen →“ auf sein Register.

## Darstellung
Eine eigenständige HTML mit eingebettetem CSS, ohne externe Bibliotheken.
Übersicht oben, Details in details/summary, klare Typografie, responsive,
druckbar. Jede wesentliche Aussage mit Claim-ID und anklickbarem Beleg.
Keine erfundenen Logos oder dekorativen Charts mit erfundenen Zahlen.
HTML-Sonderzeichen in recherchierten Texten escapen; keine fremden Skripte.
Wesentliche Widersprüche und öffentliche Lücken auch in Kurzfassung sichtbar.

## output/abnahme.md automatisch erstellen
Tatsächlich aufgerufene Agenten und deren Dateien benennen.
Auftragsnormalisierung, Themenabdeckung, Personenstatus, Delegation,
Reihenfolge, Reviews, geschlossene Fehler, Quellenlinks, interne HTML-Links,
Mobil-/Druckansicht, Quellentypen/Datumsregeln und Nicht-Speicherung in Git
(git status: keine Auftrags-/Recherchedateien versioniert): bestanden/offen/nicht geprüft.
Konfigurationstest allein ist kein durchgeführter Agentenlauf.
Keine Prüfung als bestanden melden, die nicht tatsächlich durchgeführt wurde.
