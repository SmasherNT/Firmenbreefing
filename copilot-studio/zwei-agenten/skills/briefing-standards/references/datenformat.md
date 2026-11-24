# Datenformat briefing-daten.json (Schema firmenbriefing/1)

Alle Texte auf Deutsch. Leere Listen sind erlaubt. Felder, die es nicht gibt,
weglassen. Jede Zeile mit `claims` braucht mindestens eine Claim-ID; eine Zeile
ohne Beleg gehört als Text in `luecken`.

## Oberste Ebene

```json
{
 "schema": "firmenbriefing/1",
 "auftrag": {},
 "phasen": {"auftrag": "fertig", "firmenbasis": "fertig", "portfolio": "offen"},
 "quellen": [],
 "claims": [],
 "inhalt": {},
 "interpretation": {},
 "offen": {"luecken": [], "fragen": []},
 "pruefung": {}
}
```

`pruefung` schreibt nur der Prüfagent. `phasen` zeigt, was fertig ist; Werte
`fertig`, `teilweise` oder `offen`.

## auftrag

| Feld | Inhalt |
|---|---|
| firma | Name wie offiziell geführt |
| website | offizielle Website |
| stichtag | heutiges Datum JJJJ-MM-TT |
| nachricht | Originalnachricht des Nutzers unverändert |
| modus | `voll` oder `modul` |
| module | beauftragte Module, z. B. `["portfolio"]` |
| fokus | `[{"id": "kurz-ohne-leerzeichen", "titel": "…"}]` in Nutzerreihenfolge |
| personen | `[{"name": "…", "position_laut_nutzer": "…"}]` |

## quellen

```json
{"id": "Q1", "titel": "Geschäftsbericht 2025", "herausgeber": "Firma AG",
 "datum": "2026-03-20", "url": "https://…", "abruf": "2026-11-24",
 "art": "original", "typ": "geschaeftsbericht", "geoeffnet": true}
```

`art`: `original`, `medien`, `register`, `datenbank` oder `sonstige`.
`typ` (Pflicht): `geschaeftsbericht`, `investor`, `produktseite`, `datenblatt`,
`pressemitteilung`, `register`, `behoerde`, `vergabe`, `verband`, `statistik`,
`medien`, `fachmedien`, `sonstiges`.
`url` beginnt mit http:// oder https://. `geoeffnet: false` heißt nur Suchtreffer.

## claims

```json
{"id": "P3", "aussage": "Ein vollständiger Satz mit Bezugsobjekt und Zeitraum.",
 "ursprung": "hersteller", "status": "Serie laut Hersteller", "datum": "2026-05-02",
 "quellen": ["Q1"], "belegstelle": "S. 22, Abschnitt Produkte",
 "unsicherheit": "Nur Herstellerangabe.", "stufe": "A"}
```

Pflicht: id, aussage, ursprung, quellen, stufe. Bei A immer `belegstelle`
(Seite, Abschnitt, Tabelle oder kurzes Zitat). PDF: gedruckte Seite und
PDF-Seite unterscheiden, wenn sie abweichen.

## inhalt

```json
{
 "unternehmen": {
  "profil": [{"feld": "Umsatz 2025", "wert": "412 Mio. EUR (Konzern)", "claims": ["T1"]}],
  "timeline": [{"datum": "2026-09-02", "ereignis": "…", "status": "laut Fachmedium", "claims": ["T3"]}],
  "luecken": ["…"]
 },
 "personen": [{
  "name": "…", "position_laut_nutzer": "…",
  "verifizierung": "bestätigt | abweichend: … | nicht verifiziert",
  "einleitung": {"text": "…", "claims": ["H1"]},
  "snapshot": [{"feld": "Rolle", "wert": "…", "claims": ["H1"]}],
  "werdegang": [{"zeitraum": "2019–2023 oder Zeitraum nicht belegt", "organisation": "…", "rolle": "…", "kontext": "…", "claims": ["H2"]}],
  "fachprofil": [{"titel": "…", "text": "…", "claims": ["H3"]}],
  "verantwortung": [{"titel": "…", "text": "…", "claims": ["H1"]}],
  "medien": [{"datum": "2026-10-05", "kategorie": "eigene | offiziell | medien", "titel": "…", "claims": ["H4"]}],
  "luecken": ["…"]
 }],
 "portfolio": {
  "felder": [{"name": "Geschäftsfeld", "angebote": [
   {"name": "Produktfamilie oder System, nie die Division", "anwendung": "…", "eigenschaften": "… (Herstellerangabe)",
    "status_stufe": "angekuendigt | prototyp | test | kundenauftrag | im_einsatz | serie | eingestellt | nicht_belegt",
    "status": "Kurztext mit Ursprung, Quelle und Datum", "claims": ["P1", "P2"]}]}],
  "luecken": ["…"],
  "ausnahmen": [{"regel": "portfolio.medien", "grund": "Suchwege und Ergebnis, mindestens 40 Zeichen"}]
 },
 "cluster": {
  "beziehungen": [{"von": "…", "zu": "…", "typ": "genau einer: Eigentum, Joint Venture, Kooperation, Kunde, Lieferant, Projekt, Lizenz, Mandat, historisch",
   "gegenstand": "…", "anteil_rolle": "…", "art": "genau einer: direkt, indirekt, Überschneidung", "status": "…", "datum": "…", "claims": ["C1"]}],
  "berichte": [{"akteur": "…", "bericht": "…", "jahr": "2025", "abschnitte": "S. 80–84", "status": "analysiert | nicht gefunden | nicht zugänglich | teilweise lesbar"}],
  "luecken": ["…"]
 },
 "markt": {
  "kennzahlen": [{"kennzahl": "…", "wert": "…", "definition": "Region, Jahr, Abgrenzung, Währung", "claims": ["M1"]}],
  "vergleich": {"einheit": "verglichene Angebotsart",
   "kriterien": [{"id": "k1", "name": "…", "definition": "Einheit, Bedingungen"}],
   "zeilen": [{"akteur": "…", "angebot": "…", "zellen": {"k1": {"text": "…", "claims": ["P1"]}}}]},
  "praesenz": [{"region": "…", "aktivitaeten": [
   {"akteur": "Rechtsträger", "standort": "Ort, Land", "funktion": "Büro | Produktion | Integration | Service | Entwicklung | Partner | Kundenaktivität",
    "betreiber": "genau einer: eigen, partner, jv, kunde, ausland", "status": "genau einer: operativ, angekündigt", "claims": ["M5"]}]}],
  "luecken": ["…"]
 },
 "fokus": [{
  "id": "gleich wie im Auftrag", "titel": "…",
  "definition": {"text": "…", "claims": ["F_x_1"]},
  "kennzahlen": [{"kennzahl": "…", "wert": "…", "definition": "Typ, Zeitraum, Abgrenzung", "claims": ["F_x_2"]}],
  "segmente": [{"titel": "…", "text": "…", "claims": ["F_x_3"]}],
  "akteure": [{"akteur": "…", "rolle": "…", "angebot": "…", "claims": ["F_x_4"]}],
  "kernaussagen": [{"titel": "…", "text": "…", "claims": ["F_x_5"]}],
  "entwicklungen": [{"datum": "2026-08-15", "ereignis": "…", "status": "…", "claims": ["F_x_6"]}],
  "fragen": ["…"],
  "luecken": ["…"]
 }]
}
```

`unternehmen`, `portfolio`, `cluster`, `markt`, jede Person und jedes Fokusthema
können `ausnahmen` enthalten, siehe Mindestregeln unten.

In einer Vergleichszeile fehlt eine Zelle, wenn nichts öffentlich belegt ist;
die Ausgabe zeigt dann „nicht öffentlich belegt“. Nicht anwendbar als Text
„nicht anwendbar: Grund“ mit Beleg.

## interpretation

Jedes Objekt hat eine eindeutige `id` (I… oder S…) und `basis` mit Claim- oder
Interpretations-IDs. Keine neuen Zahlen oder Fakten, die nicht in der Basis stehen.

```json
{
 "summary": {
  "highlights": [{"id": "I1", "label": "max. 60 Zeichen", "wert": "Zahl mit Einheit oder kurzer Status", "bezug": "Konzern, Segment, Produkt oder Region", "zeitraum": "…", "basis": ["T1"]}],
  "kernaussagen": [{"id": "I4", "titel": "max. 72 Zeichen", "vorschau": "max. 160 Zeichen", "aussage": "…", "begruendung": "…", "unsicherheit": "…", "basis": ["P1", "M2"]}]
 },
 "keyfacts": [{"id": "I10", "modul": "portfolio | cluster | markt", "titel": "…", "fakt": "…", "insight": "…", "unsicherheit": "…", "basis": ["P2"]}],
 "positionierung": [{"id": "I20", "dimension": "…", "urteil": "kurz, z. B. Stufe 4 Kundenprogramm", "aussage": "…", "methode": "…", "begruendung": "…", "unsicherheit": "…", "basis": ["P2"]}],
 "swot": {
  "staerken": [{"id": "S1", "titel": "…", "aussage": "…", "begruendung": "…", "einschraenkung": "…", "basis": ["I4"]}],
  "schwaechen": [], "chancen": [], "risiken": []
 },
 "grenzen": ["gemeinsame Grenze einmal nennen"]
}
```

## offen

`luecken`: wichtige Datenlücken und Widersprüche. `fragen`: neutrale
Gesprächsfragen, keine Behauptungen über die Firma.

## Mindestregeln

Das Skript meldet einen Fehler, wenn eine Regel nicht erfüllt ist und im
Kapitel keine begründete Ausnahme mit derselben Regel-ID steht.

| Regel-ID | Anforderung |
|---|---|
| unternehmen.profil | Profil mit mindestens vier belegten Zeilen |
| unternehmen.medien | mindestens zwei Nachrichten- oder Fachmedien |
| personen.quellen | je Person mindestens zwei verschiedene Quellen |
| portfolio.angebote_je_feld | je Geschäftsfeld mindestens zwei Angebote |
| portfolio.geschaeftsbericht | mindestens ein Geschäftsbericht oder eine Investorenunterlage |
| portfolio.medien | mindestens zwei Nachrichten- oder Fachmedien |
| portfolio.status | höchstens die Hälfte der Angebote `nicht_belegt` |
| cluster.beziehungen | mindestens drei Beziehungen |
| cluster.bericht | mindestens ein Bericht mit Status „analysiert“ |
| cluster.medien | mindestens zwei Nachrichten- oder Fachmedien |
| markt.kennzahlen | mindestens zwei Kennzahlen mit Definition |
| markt.vergleich | mindestens drei Zeilen und drei Kriterien |
| markt.medien | mindestens zwei Nachrichten- oder Fachmedien |
| fokus.kennzahlen | je Fokus mindestens vier Kennzahlen |
| fokus.akteure | je Fokus mindestens drei Akteure |
| fokus.kernaussagen | je Fokus drei bis fünf Kernaussagen |

Weitere harte Prüfungen: Quellentyp, Statusstufe, erlaubte Werte bei Beziehungen
und Präsenz, keine Zeile nur mit B-Claims.

## pruefung (nur Prüfagent)

```json
{
 "stand": "2026-11-25",
 "umfang": {"kapitel": "alle", "nur_a": false},
 "zusammenfassung": "Ein bis zwei Sätze.",
 "claims": [{"id": "P2", "urteil": "abweichend", "stufe": "A", "beleg": "URL und Stelle", "begruendung": "…", "korrektur": "Vorschlag"}],
 "ableitungen": [{"id": "I9", "urteil": "nicht_gestuetzt", "begruendung": "…", "korrektur": "…"}],
 "stichprobe": [{"gruppe": "Kapitel, Quelle, Aussageart", "auswahl": "IDs", "ergebnis": "…"}],
 "hinweise": ["…"]
}
```

`umfang.kapitel`: `"alle"` oder Liste aus `unternehmen`, `personen`, `portfolio`,
`cluster`, `markt`, `fokus`, `interpretation`.
Urteile für Fakten: `im_original_bestaetigt`, `durch_suche_gestuetzt`,
`abweichend`, `nicht_belegt`, `nicht_erreichbar`, `nicht_einzeln_geprueft`.
Urteile für Ableitungen: `gestuetzt`, `eingeschraenkt`, `nicht_gestuetzt`.
`ergebnis` und `auswertung` setzt das Skript mit `auswerten`, nie von Hand.
