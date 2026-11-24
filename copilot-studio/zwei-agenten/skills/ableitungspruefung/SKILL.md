---
name: ableitungspruefung
description: Prüft in einem vorhandenen Firmenbriefing Executive Summary, Keyfacts, Positionierung und SWOT gegen die geprüften Fakten. Vergibt je Interpretation ein Urteil gestützt, eingeschränkt oder nicht gestützt und markiert Ableitungen, die auf abweichenden Fakten beruhen. Keine neue Recherche.
---

# Ableitungsprüfung

Vorher briefing-standards laden. Erst nach der Quellenprüfung ausführen, weil
die Urteile der Fakten die Ableitungen bestimmen. Ergebnis ist `pruefung.ableitungen`.

## Prüffragen je Interpretation

1. **Basis:** Alle IDs in `basis` existieren und tragen die Aussage. Fakten mit
   `abweichend` oder `nicht_belegt` machen die Ableitung mindestens eingeschränkt;
   trägt der Fakt sie allein, ist sie nicht gestützt.
2. **Keine neuen Fakten:** Keine Zahl, kein Datum, kein Akteur, der nicht in der
   Basis steht.
3. **Ursprung erhalten:** Herstellerangaben nicht als unabhängige Tatsache,
   „angekündigt“ nicht als umgesetzt, Produkt nicht als Konzern.
4. **Logik:** Die Aussage folgt aus der Basis; ein Kriteriumsvorsprung wird nicht
   zum Gesamtvorsprung; eine Datenlücke wird nicht zur Schwäche.
5. **Highlights:** Einheit, Zeitraum, Bezugsobjekt und Ziel-/Ist-Kennzeichnung korrekt.
6. **Skalen:** Produktreife und regionale Präsenz nennen die höchste belegte Stufe;
   JV-Stufen nur mit Kontrollbeleg; „Geplant“ nur bei Ankündigung.
7. **SWOT:** interne Punkte bei Stärken und Schwächen, externe bei Chancen und
   Risiken; höchstens drei je Quadrant; keine Füllpunkte; Bezug zum Auftrag.

## Urteile

| Urteil | Wann |
|---|---|
| `gestuetzt` | Basis geprüft und trägt die Aussage vollständig |
| `eingeschraenkt` | trägt sie nur teilweise, z. B. nur durch Suche gestützte Basis, zu starke Formulierung |
| `nicht_gestuetzt` | Basis abweichend oder nicht belegt, oder die Aussage folgt nicht aus ihr |

Je Urteil kurze `begruendung`; bei eingeschränkt oder nicht gestützt eine
`korrektur` als Vorschlag, etwa eine vorsichtigere Formulierung.
