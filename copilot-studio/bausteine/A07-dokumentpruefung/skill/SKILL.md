---
name: briefing-dokumentpruefung
description: Prüft für ein Firmenbriefing ein zugewiesenes Quellenbündel gegen die zugehörigen Aussagen und liefert je Dokument und Aussage einen Befund. Erteilt keine Freigabe.
---

# Dokumentprüfung

## Anschlüsse

| | Datei |
|---|---|
| Eingang | `pruefjob-<job>.json` (Jobansicht aus W1: eigene Quellen, zugehörige Aussagen, A-Pflichten, passende Netzwerkkanten) |
| Ausgang | `befund-<job>.json` |

Nur die Quellen und Aussagen dieses Jobs prüfen. Andere Jobs und Prüfer gibt es
für diesen Baustein nicht.

## Arbeitsweise

1. Jede zugewiesene Quelle öffnen und die relevanten Abschnitte tatsächlich
   lesen; bei Zweifel weiteren Kontext lesen. Analystenparaphrase und
   Suchsnippet ersetzen das Original nie.
2. Eine Quelle für alle ihre Aussagen gemeinsam lesen, aber für jede Aussage
   einen eigenen Befund geben. Ein passender Absatz bestätigt nicht alle
   Aussagen derselben Quelle.
3. **A (vollständig):** Eigentum und Kontrolle, wesentliche Aufträge und
   Finanzierungen, zentrale Kooperationen, Personenidentität und aktuelle Rolle,
   Summary-Kennzahlen, strittige Angaben, jede eingezeichnete Netzwerkkante
   (Identitäten, Richtung, Typ, Status, Produktbezug, Quoten), regionale Präsenz,
   Fokus-Kennzahlen und alle IDs aus den A-Pflichten des Jobs.
4. **B (Stichprobe):** nur ergänzende Hintergrunddetails. Gruppen aus Modul,
   Quelle und Aussageart; je Gruppe mindestens eine Aussage, sonst etwa 20 %,
   inklusive einer Zahl oder Datumsangabe. Ein Fehler in der Stichprobe heißt:
   ganze Gruppe nach A prüfen. Nicht geprüfte als „nicht einzeln geprüft“ markieren.
5. Bei mehreren Quellen einer Aussage nur den Beitrag dieser Quelle beurteilen.
6. Fehlende Quellen, Bezahlschranken und Widersprüche ausdrücklich benennen.
   Ohne gelesenes Original kein „geprüft“.

## Ausgabedatei

Kopf aus der Jobansicht übernehmen: `run_id`, `company`, `as_of`, `phase`,
`job_id`. Format-Kennung und Prüfsummen ergänzt W2.

```json
{
  "documents": [{
    "source_id": "S-…", "original_read": true,
    "note": "tatsächlich gelesene Abschnitte und Zugriffsumfang",
    "findings": [
      {"claim_id": "P1", "depth": "A", "status": "geprüft", "note": "…"},
      {"claim_id": "P2", "depth": "A", "status": "Korrektur", "note": "…",
       "reason": "…", "action": "…", "owner": "portfolio"}
    ]
  }]
}
```

- Für jedes zugewiesene Paar aus Dokument und Aussage genau ein Befund.
- `status`: geprüft / nicht einzeln geprüft / Korrektur / offen.
- Bei Korrektur oder offen zusätzlich `reason`, `action` und `owner`
  (context, portfolio, cluster, market oder focus:&lt;id&gt;).
- Keine Freigabe, keine globalen Urteile, keine Änderung anderer Dateien.

Regeln im Detail: `quellenpruefung.md`, `parallele-quellenpruefung.md`
(im Skill-Paket unter `references/`).
