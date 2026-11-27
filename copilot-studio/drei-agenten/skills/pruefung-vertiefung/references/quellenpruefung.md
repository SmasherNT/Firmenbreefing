# Quellenprüfung

Ergebnis ist der Block `pruefung.claims` und `pruefung.stichprobe`. Neue Fakten
entstehen nur in der Vertiefung (vertiefung.md), nicht in der Quellenprüfung.

## Umfang festlegen

Aus der Nachricht des Nutzers: „prüfen“ heißt alle Kapitel; „nur Portfolio
prüfen“ heißt `{"kapitel": ["portfolio"]}`; „nur A-Fakten“ heißt `nur_a: true`.
Den Umfang in `pruefung.umfang` eintragen.

## Prüftiefe

- **A vollständig:** jeder A-Claim im Umfang wird einzeln gegen die Belegstelle
  geprüft. Dazu gehören immer Summary-Kennzahlen, Eigentum und Kontrolle, jede
  Cluster-Beziehung (Identitäten, Richtung, Typ, Status, Zeitraum, Quote,
  Kontrolle), Person und Rolle, Vergleichswerte, regionale Präsenz, Fokus-Fakten
  und jede Grundlage einer Interpretation, auch wenn sie als B markiert ist.
- **B als Stichprobe:** Gruppen nach Kapitel, Quelle und Aussageart. Je Gruppe
  mindestens ein Claim, bei mehreren etwa 20 Prozent aufgerundet, möglichst mit
  einer Zahl oder einem Datum. Ein Fehler in der Stichprobe führt zur Prüfung der
  ganzen Gruppe. Nicht geprüfte B-Claims ausdrücklich `nicht_einzeln_geprueft`.
  Auswahl in `pruefung.stichprobe` dokumentieren.

## Vorgehen

1. Claims nach Quelle gruppieren; jede Quelle einmal öffnen, alle zugehörigen
   Claims dort prüfen. Ein Treffer für einen Claim gilt nicht automatisch für
   alle Claims derselben Quelle.
2. Prüfen: Identität von Firma, Produkt, Variante und Person; Zahl, Einheit,
   Währung und Zeitraum; Status (angekündigt, beauftragt, geliefert …);
   Ursprung (Hersteller, Partner, Medien); Datum; Belegstelle.
3. Lässt sich das Original nicht öffnen: unabhängige Quelle suchen. Kopierte
   Pressemitteilungen zählen nicht als unabhängig.
4. Nie aus eigenem Wissen bestätigen. Ein Suchsnippet ist keine Originalprüfung.
5. **Ausnahmen kontrollieren:** Für jede begründete Ausnahme im Umfang kurz
   gezielt suchen. Findest du doch belastbare Quellen, schreibe einen Hinweis in
   `pruefung.hinweise` mit Regel-ID und Fundstelle. Prüfe auch, ob Quellentyp und
   Statusstufe zum Beleg passen; Abweichungen als `abweichend` beim betroffenen Claim.

## Urteile

| Urteil | Wann |
|---|---|
| `im_original_bestaetigt` | Belegstelle im geöffneten Original stützt die Aussage vollständig |
| `durch_suche_gestuetzt` | Original nicht geöffnet, aber eine unabhängige gelesene Quelle stützt die Aussage |
| `abweichend` | Quelle sagt etwas anderes, z. B. andere Zahl, anderer Status, anderer Ursprung |
| `nicht_belegt` | weder Original noch unabhängige Quelle stützen die Aussage |
| `nicht_erreichbar` | Quelle nicht abrufbar und keine unabhängige Quelle gefunden |
| `nicht_einzeln_geprueft` | B-Claim außerhalb der Stichprobe |
| `korrigiert` | du hast den Claim nach dem geöffneten Original korrigiert (siehe unten) |
| `neu_aus_vertiefung` | der Claim stammt aus deiner Vertiefung |

Je Urteil `beleg` (URL und Stelle, die du gelesen hast) und kurze `begruendung`.

## Korrigieren

- **Abweichend:** Hast du das Original geöffnet und die richtige Angabe gelesen,
  korrigiere den Claim direkt: gleiche ID, neue `aussage`, `status`, `belegstelle`,
  dazu `korrekturgrund`. Zusammenführen mit `--ersetzen --pruefer`; das Skript
  protokolliert alt und neu. Urteil `korrigiert`. Ohne geöffnetes Original nicht
  korrigieren, sondern `abweichend` mit Vorschlag in `korrektur` lassen.
- **Nicht belegt:** Claim entfernen (`"entfernen": ["P7"]`, `"entfernen_grund"`)
  oder durch einen belegten Claim ersetzen. Alle Zeilen, die ihn nutzen, anpassen.
- Nach jeder Korrektur alle abhängigen Inhalte nachziehen: Portfolio-Zeile und
  `status_stufe`, Matrixzellen, Präsenz, Netzwerkbeziehung, Summary, Keyfacts,
  Reife, Präsenzstufe, Positionierung, SWOT.

## Abschluss

Ableitungen prüfst du danach nach ableitungspruefung.md.
