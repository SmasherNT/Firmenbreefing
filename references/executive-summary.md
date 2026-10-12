# Executive Summary: feste Gestaltung, auftragsbezogene Inhalte

## Auswahl im bestehenden Positionierungsschritt
Für ein Vollbriefing drei Highlights und weiterhin 4–6 Kernaussagen liefern.
Nur geprüfte A-Fakten im delegierten Kontext verwenden; keine zusätzliche
Recherche, keine neue Rolle und keine HTML-Erzeugung für dieses Modul.
Der Hauptagent nimmt relevante Kennzahl-/Statuskandidaten aus der vorhandenen
Faktenbasis in den selektiven Positionierungskontext auf, statt alle Fakten zu laden.

Highlights nach Auftragsbezug, Aussagekraft, Aktualität und unterschiedlichen
Perspektiven auswählen. Keine feste Umsatz/Wachstum/Backlog-Liste. Je nach Auftrag
kommen etwa Kapazität, Auslieferungen, Investitionen, benannte Kundenländer oder
regionale Aufträge infrage. Große Zahlen sind nicht automatisch relevant.
Möglichst verschiedene Aspekte zeigen; ähnliche Finanzzahlen nur bei passendem
Auftrag. Sind weniger als drei geeignete Zahlen belegt, belegte Statusangaben
verwenden. Fehlen auch dafür Fakten, weniger Highlights und status=teilweise
liefern; Vollausgabe bleibt gesperrt. Keine Füllwerte, Scores oder Nachrecherche
allein für eine optisch vollständige Reihe.

Zahl, Einheit, Bezugsobjekt und Zeitraum aus den Fakten erhalten. Konzern,
Segment, Produkt und Region unterscheiden. Herstellerziel, Prognose, Obergrenze
oder angekündigte Kapazität schon im sichtbaren label bzw. value kennzeichnen.
Keine eigenen Zählungen, Schätzungen oder Umrechnungen: nötige neue Fakten
müssen zuerst in die Faktenphase und das Basis-Review zurück.

Kernaussagen nach Bedeutung für den Auftrag ordnen, ohne starre Themenkategorien.
Jede Karte erhält eine kurze Überschrift und einen Vorschausatz. Verkürzung darf
Unsicherheit, Aussageursprung und Ziel-/Ist-Unterschied nicht verschleiern.
Keine generischen Füllpunkte bei begrenzter Evidenz; die 4–6-Regel des
Vollbriefings bleibt bestehen.

## Datenvertrag innerhalb positioning.interpretations
Beide Gruppen bleiben reguläre I-Claims mit id, statement, depends_on, reasoning,
method und uncertainty nach interpretationsphase.md. Keine parallele Textkopie
oder ungeprüfte Darstellung außerhalb dieser Claims.

| Gruppe | Zusätzliche Felder |
|---|---|
| Kernaussage | section=executive_summary; headline (max. 72 Zeichen); preview (max. 160); display_order |
| Highlight | section=executive_highlights; type=summary_highlight; highlight_kind=metric/status; label (max. 60); value (String, max. 40, Zahl mit Einheit oder kurzer Status); scope_label (max. 80); period (max. 60); display_order |

display_order je Gruppe eindeutig und lückenlos ab 1; bestimmt die Reihenfolge.
Highlights verweisen mit depends_on direkt auf aktuelle A-Fakten, nicht auf
andere Interpretationen. reasoning erklärt die Auswahl knapp, normalerweise in
einem Satz; statement erhält die vollständige belegte Aussage. Keine Quellen-
Volltexte oder allgemeine Disclaimer kopieren. Kernaussagen behalten ihre
fachlich notwendige Begründung und konkrete Unsicherheit.

## Review und Darstellung
Das vorhandene Schluss-Review prüft auch sichtbare Titel, Vorschausätze und
Highlights auf Auftragsbezug, korrekte Verkürzung, Einheit, Zeitraum, Bezugsobjekt,
Status und Herkunft. Unveränderte A-Urteile übernehmen; keine neue Prüfschleife.
Alle Darstellungsfelder und display_order sind Teil des jeweiligen I-Fingerprints.
Änderungen benötigen aktualisierte Validierung und gezieltes Schluss-Review.

Der lokale Renderer zeigt drei Highlight-Karten und 4–6 Kernaussagen:
vier als 2×2, sechs als 3×2, fünf als drei plus zwei gleichmäßig breite Karten.
Gestaltung und Abnahme für die Desktop-Webansicht. Klick bzw. Tastatur öffnet Details mit vollständiger Aussage,
Einordnung, Grenzen, Faktenbasis und direkten Originalquellen. Ohne JavaScript
bleiben native details bedienbar; Druck zeigt die Inhalte ausgeklappt.
Der Renderer wählt keine Zahlen aus und erzeugt keine neuen Aussagen.

Bestehende Läufe mit altem Summary-Format benötigen neue Darstellungsfelder und
Highlights aus ihrer geprüften Basis sowie ein gezieltes Schluss-Review. Fakten
nicht allein wegen der Layoutumstellung neu recherchieren.

## Highlight-Zeile
Drei gleich hohe Karten: Bezeichnung oben, Wert/Status im gemeinsamen Wertebereich,
Bezugsbereich darunter, Zeitraum in einer abgesetzten unteren Zeile. Lange Werte
erhalten lokal passende Schriftgrößen. Inhalte und Review-Bindung bleiben unverändert.
