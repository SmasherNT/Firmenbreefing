---
name: briefing-output
description: Erzeuge aus freigegebenen facts-v2/interpret-v2-Dateien eine kompakte eigenständige HTML mit Matrix, Cluster-Netz, Details und Quellen; unterstütze bestehende Legacy-Modultests.
---

Lies Auftrag und references/ausgabe-html-v2.md. Delegation nennt Lauf, Manifest,
Paket, Reviews, vorhandene Interpretationen samt Kontexten und aktuellem Plan.
Explizite Markdown-Modultests nach references/legacy-html-output.md durchführen.
1. V2-Dateien desselben Laufs an scripts/render-briefing.py übergeben.
   Vollständiges Firmenbriefing: --full. Aufruf in der Referenz.
   Vorlage und JavaScript nicht als Standard in den Modellkontext laden.
   Feste vier Seiten und Portfolio nach references/portfolio-darstellung.md;
   Portfolio-Detailprofile standardmäßig vollständig eingeklappt. Keine firmenspezifische Vorlage.
   Cluster nach references/netzwerk-html.md: vier Bereichsfelder im 2×2-Raster,
   gleich große Knoten, Farbe/Form je Kategorie, Namen darunter, keine Score-Badges;
   gebogene Linien mit Pfeilen ohne Endpunktkreise, Details rechts, Seite scrollbar.
   Gesprächspartner offen nach references/gespraechspartner.md auf Seite 2.
   Capability Matrix nach references/capability-matrix.md: gleich hohe Kurztextzellen,
   tatsächliche Evidenzskalen, Einzelbewertung darunter und alle Peers per Spaltenkopf
   vergleichen. Vollständige Fakten/Quellen auch im Druck und ohne JavaScript.
   Markt-Deep-Dive nach references/markt-deepdive.md: Kennzahlen/CAGR, Programme
   und industrielle Rollen mit Länderdetails darunter. Nur aktuelles freigegebenes
   market_dashboard verwenden; fehlende Daten offen lassen, keine Musterwerte.
   Unter Portfolio, Cluster und Markt/Matrix auf Seite 1 kompakte Keyfacts/Insights
   nach references/modul-keyfacts.md aus geprüften module_insight-I-Claims zeigen.
   Fakt/Insight trennen, Herleitung und Quellen per Klick; keine Texte selbst erzeugen.
   Regionale Präsenz nach references/regionale-praesenz.md auf Seite 1 unmittelbar
   vor Markt/Capability Matrix: Regionszeilen, fünf Kreise/n/5, Fokus gold,
   native Regionsprofile mit Scope/Methodik/Quellen. Nur freigegebene I-Stufen.
2. Fehler gezielt an zuständige Fakten-/Interpretations-/Prüfrolle geben;
   keine fremden Dateien korrigieren oder Prüfbarrieren umgehen.
   Keine finale HTML bei Materialfehlern, veralteten Reviews, blockierenden Fragen.
   Ältere Erfolgsdatei nach Fehlern nicht als aktuellen Erfolg ausgeben.
3. Desktop-Webansicht prüfen: interne/Quellenlinks, Netzwerk/Filter/Details und Druck.
   Nicht ausführbare Prüfung als offen nennen. Keine neue Behauptung beim Rendern.
4. output/abnahme.md: tatsächliche Agenten/Dateien/Reviews, formale Prüfungen,
   Inhaltsreview, Abdeckung, visuelle Kontrollen und offene Punkte unterscheiden.
   Mechanischer Pass ist keine Freigabe; Konfigurationstest ist kein Firmenlauf.

Neue Firma/Lauf bedeutet neue Daten. Nur Code/Layout wiederverwenden. Keine
Langberichte oder Quellenvolltexte als Standard-Ausgabeprüfkontext, keine weitere
LLM-Runde für HTML/Quellenformatierung. Rückgabe mit Pfad und Status.

Themenkarten und SWOT-Farben nach references/themen-darstellung.md lokal rendern.
Keine LLM-Runde für Farben, Raster oder lokale Kurztext-Fallbacks.
