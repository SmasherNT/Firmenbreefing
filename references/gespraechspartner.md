# Berufliches Gesprächspartnerprofil

Der bestehende company-context-Faktenagent liefert `profile` im context-facts.json.
Kein zusätzlicher Agent, keine HTML und keine strategische Personenbewertung.
Darstellung wie die freigegebene Profilvorlage: Name/Einleitung, Snapshot (bis zu
sechs Felder, drei Spalten), Werdegangstabelle, Fachprofil und Verantwortung
nebeneinander, regionaler Bezug, Quellen. Inhalte stehen offen auf Seite 2.

## Datenvertrag

`profile.name` und `profile.claim_ids` bleiben Pflicht. Alle zugeordneten Fakten
sind berufliche H-Claims derselben Person. Kompakte Texte sind quellengedeckte
Paraphrasen; Einschränkungen wie „laut Fachmedium“, „angekündigt“ oder eine nur
historisch belegte Rolle bereits im sichtbaren Kurztext erhalten.

Neue Läufe liefern folgende Strukturen; leere Listen bei fehlender Evidenz:
- `intro`: optional `{text, claim_ids}` – kurze berufliche Einleitung.
- `snapshot`: maximal sechs `{label, value, claim_ids}`. Z. B. Rolle, Unternehmen,
  weitere belegte Verantwortung, Fachthema, prägende Erfahrung, internationaler Bezug.
  Nur sinnvolle belegte Felder; keine Felder künstlich auffüllen.
- `career`: `{period, organization, role, context, claim_ids}` pro Station in
  chronologischer Reihenfolge. context beschreibt den belegten Tätigkeitskontext,
  keine erfundene strategische Relevanz. Fehlendes Datum: „Zeitraum nicht belegt“.
  Nachweisdatum ausdrücklich vom Eintrittsdatum unterscheiden.
- `expertise`, `responsibilities`: jeweils `{label, text, claim_ids}`.
  Frühere Tätigkeiten nicht als aktuelle Verantwortung darstellen.
- `regional_context`: optional `{label, text, claim_ids}`. Nur den belegten
  persönlichen Bezug zum beauftragten Markt darstellen. Unternehmenspräsenz
  allein genügt nicht. Ohne Beleg dieses Feld weglassen und Suche in gaps/coverage
  dokumentieren; der Renderer zeigt eine neutrale Lücke des Recherchepakets.

Alle claim_ids müssen in profile.claim_ids stehen. Der Renderer verlangt aktuelle
A-Prüfungen; prepare-facts prüft Struktur und Verweise vor dem Basis-Review.
Auch name, Texte, Chronologie und Zuordnungen gehören zur semantischen Basisprüfung;
Änderungen am Profil entwerten den Paket-Fingerprint. Keine automatische Freigabe.
Nicht einsortierte H-Claims bleiben unter „Weitere belegte Profilangaben“ erreichbar.
Ältere Profile ohne neue Felder bleiben nutzbar, zeigen aber explizite Datenlücken.

## Darstellung und Quellen

Die lokale Komponente scripts/profile-html.py und profile.css erzeugt das Profil.
Nummerierte Belege springen zu direkten Originalquellen; vollständige Aussagen,
Unsicherheiten und Links ins gemeinsame Claimregister bleiben am Profilende sichtbar.
Nur Code und Layout wiederverwenden, nie Personendaten des vorigen Unternehmens.
