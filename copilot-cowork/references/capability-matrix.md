# Capability Matrix: Vergleichsplan aus dem Auftrag
Darstellung wie Referenz-HTML: Unternehmen/konkretes Angebot in Zeilen, Kriterien
in Spalten, jede Zelle mit späterem Deep Dive zu Begründung, Evidenz und Quellen.
Scores zeigen öffentliche Evidenzreife, keine gemessene technische Überlegenheit.

## Technische Systemvergleiche priorisieren
Bei Produkt-/Systemvergleichen überwiegend technische Kriterien wählen. Als
Richtwert drei bis fünf technische Dimensionen plus die ergänzenden Kriterien
„Belegter Beschaffungs- und Einsatzstand“ und „Industrielle Fertigungs- und
Lieferfähigkeit“. Für andere Aufgaben fachlich begründet anpassen; keine festen
Flugabwehrspalten in branchenfremde Aufträge übernehmen. Kundenzahl, lokale
Wertschöpfung und Partnerschaften ergänzen die Details, ersetzen keine Technik.

Für Flugabwehr bietet sich an: Wirkmittel/Kaliber, Bekämpfungsentfernung/-höhe,
Sensorik/Zielverfolgung, Führung/Vernetzung, Mobilität/Systemarchitektur. Wo
belastbar verfügbar, technische Details wie Kadenz, Bereitschaftsmunition,
Bekämpfungskanäle, Reaktionszeit, Ziel-/Störbedingungen und Schnittstellen aufnehmen.
Fehlende Daten nicht durch Beschaffungsvolumen oder einen Reifegrad ersetzen.
Technische Daten als Profil oder Kennzahl, Beschaffung/Industrie mit eigenen
Evidenzmaßstäben. Ein hoher Reifegrad bedeutet keine höhere technische Leistung.

Vorgehen im bestehenden Ablauf, ohne zusätzliche Agenten-/Prüfrunde:
1. Vergleichseinheiten und Rüststände vor Recherche festlegen; Turm, Batterie,
   Flugkörpervariante und Gesamtverbund unterscheiden. Nach vergleichbarer Rolle
   gruppieren, alle ursprünglich relevanten Angebote sichtbar halten.
2. Auftragsspezifische technische Kriterien im comparison-plan definieren; je
   Messwert Einheit, Definition und Bedingungen festhalten. „Bis zu“/instrumentierte
   Reichweite, Herstellerangabe, Medienangabe, Test oder Einsatznachweis trennen.
3. Marktrolle erfasst pro System/Kriterium Fakten mit direkten Belegen und IDs;
   vorhandene Portfolio-/Cluster-Claims wiederverwenden. Angaben anderer Varianten
   nicht übertragen: z. B. SLM-Radar nicht für SLS, Skyranger-35-Reichweite nicht
   für Skynex. Radarreichweite ist keine Bekämpfungsentfernung. Geplante Integration
   nicht als verfügbaren Serienstand ausgeben.
4. Quellenreview prüft technische Messwerte, Variante, Rahmenbedingungen und
   Vergleichbarkeit vollständig A. Positionierung verdichtet erst danach; keine
   Sieger-/Summenscores über Kanonen-, Hybrid- und Flugkörpersysteme bilden.
5. Renderer zeigt technische Spalten zuerst, Beschaffung/Industrie anschließend.
   Die anfängliche Detailansicht folgt dem ersten Kriterium des Vergleichsplans,
   statt automatisch eine Evidenzstufe vorzuziehen.
   Zellen und Spaltenköpfe öffnen weiterhin vollständige Fakten/Quellen und den
   Kriterienvergleich. Markt-/Industrieprofile als ergänzende Details erhalten.
   Fehlende öffentliche Daten und nicht anwendbare Kriterien weiterhin trennen.

Bestehenden Vergleichsplan bei dieser Umstellung neu versionieren und alle
betroffenen Beobachtungen/Interpretationen neu prüfen; alte I-Scores nicht in
technische Leistungswerte umbenennen. Bei einer ausdrücklich nur aus bestehender
HTML beauftragten Neudarstellung sind neue Technikprofile quellengebundene Auszüge,
keine neue Freigabe: Stichtag erhalten, „im vorliegenden Briefing nicht angegeben“
von allgemein fehlender öffentlicher Evidenz unterscheiden, originale Bewertungen
und Quellen unverändert zugänglich halten. Keine neuen Leistungsdaten ergänzen.

## Vor der Wettbewerbsrecherche
Hauptagent erstellt comparison-plan.json mit company, as_of, run_id,
comparison_unit, purpose, peer_groups, criteria und version.
Vergleichseinheit aus Nutzerthemen bestimmen: Produkt/System/Dienstleistung
und Einsatzkontext, nicht pauschal gesamter Konzern. Frühe Firmen-/Produktfakten
dürfen die Identität klären; Kriterien nicht nach gewünschten Ergebnissen wählen.
Bei allgemeinem Auftrag passende Kerngeschäftseinheit begründet wählen.
Etwa 5–7 Kriterien als Richtwert; weniger oder mehr nur bei fachlichem Bedarf.
Keine feste Bodenautonomie-Matrix für andere Firmen/Branchen übernehmen.

Je Kriterium: id, label, question, evidence_required, display_type,
applicability, rationale. display_type: Profil / Kennzahl / Evidenzstufe.
Evidenzstufe: zusätzlich vorab definierte anchors (z. B. 1–5); gleiche
Stufen und Bezugsgrößen für alle vergleichbaren Angebote. Noch keine Scores vergeben.
Kennzahl: gemeinsame Einheit und Einsatz-/Messbedingungen definieren.
Im JSON dafür unit und conditions angeben.
Profil: qualitative Beschreibung ohne Rangfolge, z. B. Integrationsmodell.
peer_groups: Gruppen nach vergleichbarer Rolle, keine Rangliste und keine
vorgegebene Anzahl. Markt-Agent schlägt konkrete Peers mit nachvollziehbarem
Produkt-/Funktionsbezug vor; Hauptagent bestätigt Scope und Gruppen.

Kriterien aus Fragestellung ableiten und kurz begründen:
OEM-Integration -> Integrationsmodell/Schnittstellen;
industrielle Skalierung -> relevante Fertigung/Lieferfähigkeit;
Marktzugang -> Kundenprogramme/regionale Partner/Zulassungen;
missionskritische Autonomie -> passende Tests/Einsatz/Resilienz.
Diese Beispiele sind keine Pflichtspalten. Branchenfremde Kriterien weglassen.
Markt-Agent sammelt Beobachtungen und Claim-IDs je peer_id/criterion_id.
Markt-Modul nennt comparison_plan_version; geänderte Kriterien nicht mit alten
Beobachtungen mischen.
Peer- und Produktidentität, Kriterienversion und Beleggrenzen erhalten.
Portfolio-/Cluster-Fakten der Zielgruppe referenzieren; keine parallele Zweitrecherche.

## Nach der Faktenprüfung
Positionierung vergibt erst dann Bewertungen nach anchors/Methode.
Nicht öffentlich belegt und nicht anwendbar getrennt kennzeichnen.
Herstellerangaben ausdrücklich ausweisen; höchster vollständig belegter
Evidenzstand, keine vermutete technische Schwäche bei fehlender Veröffentlichung.
Ordinale Scores nicht automatisch addieren/mitteln oder als Gesamt-Ranking ausgeben.
Kriterienänderung: Auftrag/Scope-Grund, neue version und alle betroffenen
Beobachtungen/Bewertungen aktualisieren; keine selektive Anpassung eines Peers.
Positionierung liefert diese Bewertungen und Zellbegründungen nach
interpretationsphase.md; Markt-Fakten allein sind noch keine bewertete Matrix.
Der HTML-Anschluss der Zell-Deep-Dives folgt im Ausgabeschritt.

## Verbindliche Darstellung (bestätigter Quantum-Systems-Stil)
Gleichmäßiges Raster: Unternehmen/konkretes Angebot in Zeilen, auftragsbezogene
Kriterien in Spalten. Referenzunternehmen sichtbar hervorheben; Reihenfolge aus
dem geprüften Vergleichsplan erhalten. Keine firmenspezifischen Inhalte in der Vorlage.
Alle Zellen gleich hoch, lesbare Schrift und kurze Kernaussagen. Zellhöhe lokal
an vollständige Kurztexte anpassen, keine abgeschnittenen Texte oder Schriftverkleinerung.
Breite Matrizen nur innerhalb der Tabelle horizontal scrollen; Akteursspalte bleibt stehen.

Große Evidenzstufe mit tatsächlichem Skalenmaximum des Kriteriums darstellen,
z. B. 2/3 oder 4/5; keine pauschale Fünferskala. Türkisabstufung nach der Position
im vorab festgelegten Kriterienmaßstab. Profile und Kennzahlen neutral, ohne
künstlichen Evidenzscore. „Nicht öffentlich belegt“ und „nicht anwendbar“ getrennt
und ohne Nullwertung anzeigen. Quellenanzahl aus tatsächlich referenzierten
Original-URLs zählen; Zahl bedeutet keine unabhängige Bestätigung.

Positionierung liefert je Matrixzelle zusätzlich kurze headline (Richtwert 40,
maximal 48 Zeichen) und preview (Richtwert 60, maximal 80 Zeichen) im bestehenden
Bewertungsschritt. Diese Felder verdichten nur die geprüfte Bewertung; Status,
Hersteller-/Medienangaben und wichtige Beleggrenzen erhalten. Beide sind Teil
derselben I-Interpretation und des Schluss-Review-Fingerprints. Ältere Datensätze
ohne Kurzfelder bleiben renderbar: rein lokale Kürzung des vorhandenen Werts,
vollständige Aussage im zugänglichen Detail. Keine zusätzliche Modell-/Recherche-Runde.

Zellklick zeigt unter der Matrix die vollständige Einzelbewertung mit Einordnung,
Grenzen, nächster Evidenzstufe bzw. coverage_note sowie A-Fakten und direkten
Originalquellen. Spaltenkopfklick öffnet alle Wettbewerber für dasselbe Kriterium
nebeneinander in einer Vergleichstabelle mit identischer Gliederung; jede
Einzelbewertung bleibt erreichbar. Kein Dialog, keine Gesamt-Rangliste.
Alle Inhalte statisch als native Details erhalten: ohne JavaScript erreichbar,
beim Drucken vollständig geöffnet, vorheriger Bildschirmzustand danach wiederhergestellt.
Renderer: scripts/capability-html.py und references/templates/capability.css/.js.

Andere beauftragte Scores nur mit zusätzlicher assessment_methods-Liste im Plan:
je Methode id, assessment_type, applicability und anchors mit erklärten Stufen.
Positionierung nennt method_id, subject und score; ohne Methode qualitative
Einordnung. Keine Pflichtscores oder festen Skalen für jede Branche hinzufügen.
