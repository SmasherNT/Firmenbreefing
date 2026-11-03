---
name: module-briefing
description: Führt einzelne Firmenbriefing-Module oder Modultests aus, z. B. nur Portfolio, 2a und 2b, oder 3 -> 4 -> 7; umgeht den vollständigen Ablauf.
---

Arbeite vom Projektstamm dieser Cowork-Kopie aus. Lies AGENTS.md und
references/cowork-betrieb.md; wende die dortige Laufzeitprüfung vor Ausführung an.
Rollenverträge unter roles/ explizit lesen; Skillnamen registrieren keine Subagenten.


Der Hauptagent verwendet diesen Einstieg bei ausdrücklich begrenzten Modultests.
Lies AGENTS.md und references/modultest.md sowie die drei Standardvorlagen.
Einrichtungs- und Konfigurationsfragen lösen keinen Recherchelauf aus.

1. Bei neuem Test eindeutiges tests/<YYYYMMDD-HHMMSS>-<Kurzname>/ anlegen;
   bei Kollision Suffix ergänzen. Originalanfrage und normalisierten Auftrag
   nach defaults.md unter <Test>/input/auftrag.md dokumentieren.
   Modus modultest, angeforderte Schritte und Teilumfang ergänzen.
   Keine root-Dateien leeren, archivieren oder überschreiben.
   Bei Fortsetzung den eindeutig benannten Test verwenden; bei mehreren
   möglichen Tests gezielt fragen. Firma/Stichtag nicht stillschweigend ändern.
2. module-contractor mit Anfrage, Auftrag, Testpfad und vorhandenen Ergebnissen
   aufrufen. Er schreibt <Test>/plan.md. Hauptagent prüft den Plan gegen den
   Nutzerumfang und führt nur seine zulässigen Schritte aus.
3. 2a an portfolio-analyst und 2b an cluster-analyst delegieren; bei gemeinsamer
   Anforderung parallel möglich. 3 selbst mit briefing-context ausführen.
   Jede Delegation nennt Modus modultest, references/modultest.md,
   Auftragspfad, ausgewählte Module, Eingabedateien und exakten Zielpfad.
   Vorhandene relevante Module nutzen, aber keine nicht gewählten erzeugen.
4. Falls Schritt 4 angefordert: source-reviewer Phase basis prüft ausschließlich
   die tatsächlich ausgewählten Ergebnisse. Korrekturen durch die zuständige
   Rolle, geänderte Aussagen erneut prüfen; höchstens zwei Korrekturrunden.
5. Falls Schritt 7 angefordert: briefing-output im Modultest-Modus anwenden.
   Nach fehlerfreiem Basis-Review direkt ausgeben, ohne SWOT/Schluss-Review.
   Ohne angeforderte Quellenprüfung nur deutlich als ungeprüfter Modultest
   gekennzeichneten HTML-Entwurf ausgeben; keine geprüfte Ausgabe behaupten.
   Bei bekannten offenen wesentlichen Fehlern keine HTML-Ausgabe.
6. Immer <Test>/output/abnahme.md mit tatsächlichen Aufrufen und Kontrollen
   schreiben; ausgelassene Schritte als nicht beauftragt kennzeichnen.
   Testpfad, Status, Lücken und nächste mögliche Schritte zurückgeben.
   Ergebnisse im beauftragten OneDrive-/SharePoint-Ziel oder als Download sichern.
   Git-Schreibzugriffe nur bei ausdrücklichem Nutzerauftrag.

Keinen vollständigen Firmenauftrag daraus machen. Die Fachagenten und
deren Arbeitsmethoden bleiben zuständig; module-contractor plant nur.
