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
2. Fehler gezielt an zuständige Fakten-/Interpretations-/Prüfrolle geben;
   keine fremden Dateien korrigieren oder Prüfbarrieren umgehen.
   Keine finale HTML bei Materialfehlern, veralteten Reviews, blockierenden Fragen.
   Ältere Erfolgsdatei nach Fehlern nicht als aktuellen Erfolg ausgeben.
3. HTML prüfen: interne/Quellenlinks, Netzwerk/Filter/Details, Mobil und Druck.
   Nicht ausführbare Prüfung als offen nennen. Keine neue Behauptung beim Rendern.
4. output/abnahme.md: tatsächliche Agenten/Dateien/Reviews, formale Prüfungen,
   Inhaltsreview, Abdeckung, visuelle Kontrollen und offene Punkte unterscheiden.
   Mechanischer Pass ist keine Freigabe; Konfigurationstest ist kein Firmenlauf.

Neue Firma/Lauf bedeutet neue Daten. Nur Code/Layout wiederverwenden. Keine
Langberichte oder Quellenvolltexte als Standard-Ausgabeprüfkontext, keine weitere
LLM-Runde für HTML/Quellenformatierung. Rückgabe mit Pfad und Status.
