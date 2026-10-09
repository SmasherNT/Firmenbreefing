---
name: briefing-output
description: Verdichtet geprüfte Firmen-, Themen- und Personenmodule zu einem HTML-Briefing.
---

Der Hauptagent verwendet diese Methode.
Lies input/auftrag.md, CLAUDE.md und alle references-Vorlagen sowie
work/portfolio.md, work/cluster.md, work/markt.md, work/kontext.md,
work/swot.md, work/review-basis.md und work/review-final.md.
Keine finale HTML bei offenen wesentlichen Fehlern erstellen.
Nur geprüfte Claims verwenden; keine neue Unternehmensbehauptung hinzufügen.
Erstelle output/briefing.html exakt nach references/briefing-struktur.md.
Priorisierte Nutzerthemen stehen vor der kompakten allgemeinen Firmenbasis.
Berufliches Personenprofil nur falls beauftragt; Nutzerrolle von verifizierter
Rolle trennen. Status, Datum und Unsicherheit auch beim Kürzen erhalten.
Jede Kernaussage auf Claim und Originalquelle verlinken. Lesbarkeit,
interne Links, mobile Darstellung und Druckansicht tatsächlich prüfen;
nicht ausführbare Kontrollen in der Abnahme als nicht geprüft kennzeichnen.
Erstelle output/abnahme.md gemäß Strukturvorlage. Dateipfade und Cloud-
Ausgabemöglichkeiten nennen. Keine öffentliche Veröffentlichung automatisch.

## Ausnahme für ausdrücklich beauftragte Modultests
Bei Modus modultest lies references/modultest.md. Die Delegation nennt
Testauftrag, Auswahl, Eingaben und Zielpfad. Diese Pfade ersetzen die festen
input/work/output-Pfade oben. Nicht gewählte Module sind keine Pflicht.
Im Standardlauf bleiben die obigen Regeln unverändert.

Im Modultest nur ausgewählte Kapitel rendern. Nach fehlerfreiem Basis-Review
ist kein SWOT-/Schluss-Review nötig. Ohne Basis-Review nur sichtbar ungeprüfter
Entwurf; bekannte wesentliche Fehler blockieren jede HTML-Ausgabe.

## Unternehmensnetzwerk darstellen
Wenn Cluster beauftragt ist, lies references/cluster-recherche.md und übernimm
seine geprüften Knoten/Kanten und Querverbindungen in eine kompakte anklickbare
Netzwerkübersicht. Zielunternehmen zentral und umliegende Akteure als Netz anordnen. Linien
bleiben zunächst unbeschriftet; Typ, Richtung, Status, Quoten und Originalquellen
erscheinen erst beim Anklicken im Detailfeld. Indirekte Pfade im Detail erklären.
Keine neuen Beziehungen beim Zeichnen ableiten. Beschriftete Beziehungstabelle
als zugängliche und druckbare Alternative anbieten. Geschäftsbericht-Abdeckung
und wesentliche öffentliche Lücken sichtbar halten. Gilt auch für 2b-Modultests.

## Wiederverwendbare Netzwerkkomponente in Schritt 7
Lies references/netzwerk-html.md und references/templates/cluster-network.html.
Übernimm das geprüfte network-data-JSON aus der Cluster-Datei in diese lokale
HTML/CSS/JavaScript-Komponente. Platzhalter sicher ersetzen, Schema/Claim-
Referenzen prüfen. Kein neues Netzwerk recherchieren oder aus Tabellen erfinden.
Knotenarten unterschiedlich färben, Beziehungskategorien kombinierbar filtern
und belegten Produktbezug filterbar machen. Originalquellen mit Titel/Datum und
Bericht-Seite direkt im ausgewählten Verbindungsdetail verlinken.
Die Vorlage in die finale briefing.html einbetten; kein separater Grafik-Link
als Ersatz. Quellenregister und druckbare Tabelle mit denselben Belegen füllen.
Interaktionen, Responsivität, Druck und Links tatsächlich nach der Abnahme in
netzwerk-html.md prüfen; nicht ausführbare Kontrollen ehrlich kennzeichnen.

Bei jedem neuen Auftrag die Vorlage mit dem vollständig neuen Netzwerk dieser
Firma befüllen. company/as_of und Zielknoten mit dem aktuellen Auftrag abgleichen.
Nur den Renderer wiederverwenden, niemals den Datensatz der vorigen Firma.
