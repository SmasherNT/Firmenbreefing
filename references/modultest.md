# Gezielte Modultests

## Geltungsbereich
Nur bei ausdrücklich gewünschter Einzelmodul-Analyse, Teilanalyse oder Modultest
gilt dieser alternative Ablauf. Im Standardmodus bleibt company-briefing
unverändert verbindlich. Eine Frage zum System ist kein Rechercheauftrag.
module-contractor wählt Module und Reihenfolge; der Hauptagent führt den Plan aus.
Dadurch sind keine verschachtelten Agentenaufrufe erforderlich.

## Nummern der Ablaufgrafik
| Schritt | Rolle / Methode | Ergebnis unter <Test>/ |
|---|---|---|
| 2a | portfolio-analyst / portfolio-analysis | work/portfolio.md |
| 2b | cluster-analyst / cluster-analysis | work/cluster.md |
| 3 | Hauptagent / briefing-context | work/markt.md und/oder work/kontext.md |
| 4 | source-reviewer, Phase basis | work/review-basis.md |
| 7 | Hauptagent / briefing-output | output/briefing.html, output/abnahme.md |

Die Nummern stammen aus der erklärenden Grafik, nicht aus der achtteiligen
Liste in company-briefing: Grafikschritt 7 entspricht dort Ablaufpunkt 8.
2a, 2b und 3 sind einzeln oder kombiniert erlaubt. Fachliche Anfragen ohne
Nummern werden auf die kleinste passende Auswahl abgebildet.
Nur explizit gewünschte Schritte ausführen. Bei unklarer Folgeausgabe einen
Modultest ohne HTML liefern, statt stillschweigend 4/7 hinzuzufügen.
5 SWOT und 6 Schluss-Review werden in diesem Modus nicht ausgeführt.

## Isolierte Dateien und verbindliche Ausnahmen
Alle Laufdateien liegen in tests/<eindeutige-ID>/ mit input/, work/, output/.
In diesem Modus ersetzt der delegierte Testpfad die in Fachagenten und
Skills genannten festen input/-, work/- und output/-Pfade. Die Originalpfade
des vollständigen Briefings werden nicht verändert. Kein Test schreibt
in einen anderen Test oder übernimmt stillschweigend ältere Claims.
Der Hauptagent schreibt Auftrag und Abnahme; module-contractor nur plan.md;
die bestehenden Fachrollen schreiben ihre jeweiligen Modul-/Reviewdateien.

Nur ausgewählte Module sind Pflicht. Nicht beauftragte Dateien sind keine
fehlenden Voraussetzungen. Diese Ausnahme hat im Modultest Vorrang vor
den festen Vollständigkeits-, Reihenfolge- und Dateilisten des Standardlaufs.
Quellenstandard, Rollenverteilung und Fehlerkontrollen bleiben verbindlich.

3 kann ohne vorheriges 2a/2b laufen. Die gewählten Themen direkt in
Originalquellen recherchieren; öffentlich fehlende Grundlagen als Lücke
kennzeichnen. Es muss kein verdecktes vollständiges Portfolio entstehen.
Teilumfang von 3: Markt -> markt.md; Themen und/oder Person -> kontext.md;
alle drei -> beide Dateien. Personenprofil nur bei genannter Person.
Jedes beauftragte Thema behandeln; keine künstlichen Themen ergänzen.

4 prüft nur die im Plan benannten, vorhandenen Moduldateien.
Nicht gewählte Module als nicht beauftragt führen, nicht als Fehler.
Wesentliche Fehler durch die verantwortliche Rolle korrigieren und erneut
prüfen. Nach zwei erfolglosen Korrekturrunden blockieren.

7 liest nur Auftrag, Plan, ausgewählte Module und gegebenenfalls Basis-Review.
SWOT und Schluss-Review sind keine Voraussetzung für einen Modultest.
Nach bestandenem 4 direkt zu 7. Ohne 4 ist nur ein sichtbar ungeprüfter Entwurf
zulässig. Kein bestandenes Review erfinden; bekannte wesentliche Fehler
blockieren auch einen Entwurf. Fügt die Ausgabe neue Unternehmensbehauptungen
hinzu, müssen sie vor geprüfter Ausgabe ebenfalls durch 4 geprüft werden.

## Ausgabe und Fortsetzung
Titel und Kopf deutlich als Modultest mit Modulwahl und Prüfstatus kennzeichnen.
HTML enthält kurze Zusammenfassung (nur so viele Punkte wie belegt),
gewählte Module in Nutzerreihenfolge, relevante Lücken und Quellenregister.
Keine leeren Kapitel für nicht gewählte Module, keine SWOT-Füllpunkte.
Gestaltung, Claim-Belege und tatsächliche Link-/Mobil-/Druckkontrollen
entsprechen briefing-struktur.md; nicht ausgeführte Kontrollen ehrlich melden.
Abnahme unterscheidet bestanden, offen, nicht geprüft und nicht beauftragt.
Auch ohne HTML eine Abnahme mit bisherigem Status erstellen.

„Jetzt nur 4 und dann direkt 7“ setzt vorhandene Ergebnisse desselben Tests
voraus. Auftrag und Ergebnisse zuerst lesen. Plan ergänzen und bisherige
Schritte erhalten; nur die neue Fortsetzung ausführen. Kein Review aus einem
anderen Unternehmen, Stichtag oder geänderten Claim-Stand wiederverwenden.
Bei Wiederholung von 2a/2b/3 bisherigen Stand unter <Test>/archive/ sichern;
betroffene Reviews und bisherige HTML-Ausgabe als überholt markieren und
nicht weiter als geprüft ausgeben. Für erneute geprüfte Ausgabe 4 wiederholen.

## Beispielanfragen
- „Teste nur 2a für Quantum Systems, danach 4 und direkt 7.“
- „Teste 2a und 2b für Quantum Systems; keine Marktanalyse und keine SWOT.“
- „Nur 3: berufliches Profil von Hendrik Kramer bei Quantum Systems; dann 4 und 7.“
- „Im Test <ID> jetzt nur 4 und dann direkt 7.“

## Konfigurationsabnahme
Diese Erweiterung wurde statisch geprüft, nicht mit einer Firmenrecherche.
Ein erfolgreicher tatsächlicher Lauf bleibt nachzuweisen:
- 2a -> 4 -> 7 benötigt weder cluster.md noch markt.md noch swot.md.
- 2a + 2b darf parallel laufen; kein implizites 3.
- 3 allein verlangt keine vorherigen Portfolio-/Strukturmodule.
- Fortsetzung 4 -> 7 benötigt die benannten vorhandenen Ergebnisse.
- 7 ohne 4 ist sichtbar ungeprüft; offene Fehler blockieren.
- Normale vollständige Briefings verwenden weiter company-briefing.

## Vertiefte Cluster-Analyse in 2b
2b umfasst auch die Geschäftsbericht- und Querverbindungsprüfung gemäß
references/cluster-recherche.md. Sie bleibt innerhalb von work/cluster.md
im jeweiligen Testverzeichnis und aktiviert keine weiteren Module.
Ein Lauf 2b -> 4 -> 7 prüft und visualisiert dieses Unternehmensnetzwerk ohne
Portfolio-, Markt- oder SWOT-Pflicht. Bericht-Zugriffslücken ehrlich dokumentieren.
