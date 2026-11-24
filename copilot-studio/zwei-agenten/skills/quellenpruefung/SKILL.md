---
name: quellenpruefung
description: Prüft die Fakten eines vorhandenen Firmenbriefings gegen ihre Quellen. Liest briefing-daten.json aus der hochgeladenen Briefing-HTML oder Excel, öffnet jede Quelle, vergleicht jeden Claim mit der Belegstelle und vergibt je Claim ein Urteil. Fügt keine neuen Fakten hinzu und ändert keine Claims.
---

# Quellenprüfung

Vorher briefing-standards und briefing-ausgabe laden. Du prüfst, du recherchierst
nicht neu. Ergebnis ist der Block `pruefung.claims` und `pruefung.stichprobe`.

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

## Urteile

| Urteil | Wann |
|---|---|
| `im_original_bestaetigt` | Belegstelle im geöffneten Original stützt die Aussage vollständig |
| `durch_suche_gestuetzt` | Original nicht geöffnet, aber eine unabhängige gelesene Quelle stützt die Aussage |
| `abweichend` | Quelle sagt etwas anderes, z. B. andere Zahl, anderer Status, anderer Ursprung |
| `nicht_belegt` | weder Original noch unabhängige Quelle stützen die Aussage |
| `nicht_erreichbar` | Quelle nicht abrufbar und keine unabhängige Quelle gefunden |
| `nicht_einzeln_geprueft` | B-Claim außerhalb der Stichprobe |

Je Urteil `beleg` (URL und Stelle, die du gelesen hast), kurze `begruendung`,
bei `abweichend` oder `nicht_belegt` eine `korrektur` als Vorschlag. Die Claims
selbst bleiben unverändert; Korrekturen macht der Nutzer oder der Ersteller.

## Abschluss

Ableitungen prüft der Skill ableitungspruefung. Danach den Teil
`{"pruefung": {…}}` zusammenführen und mit briefing-ausgabe auswerten und rendern.
