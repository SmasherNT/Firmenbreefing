# Ableitungsprüfung

Erst nach Quellenprüfung, Korrekturen und Vertiefung ausführen, weil die
Fakten die Ableitungen bestimmen. Ergebnis ist `pruefung.ableitungen`.

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
| `angepasst` | du hast die Interpretation an korrigierte oder neue Fakten angepasst |

Je Urteil kurze `begruendung`.

## Anpassen statt nur bemängeln

Folgt eine Interpretation nach Korrektur oder Vertiefung nicht mehr aus den
Fakten, passe sie an: gleiche ID, neue Aussage, Stufe oder Formulierung, neue
`basis`. Teil mit `interpretation` zusammenführen (`--pruefer`), Urteil
`angepasst`. Regeln dafür stehen im Skill interpretation. Kannst du sie nicht
sauber anpassen, Urteil `nicht_gestuetzt` mit Vorschlag in `korrektur`.

Auch Matrixstufen (`evidenzstufe`) gegen die Stufendefinition des Kriteriums
prüfen; Abweichungen korrigieren und in `pruefung.hinweise` nennen.
