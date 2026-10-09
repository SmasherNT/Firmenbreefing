#!/usr/bin/env python3
"""Synthetic offline demo: no URLs opened; all reviewer decisions simulated."""
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / file)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


FACTS = load('facts', 'prepare-facts.py')
CHECK = load('check', 'check-interpretation.py')
STAMP = load('stamp', 'stamp-review.py')
RENDER = load('render', 'render-briefing.py')


def generate(destination):
    root = Path(destination); root.mkdir(parents=True, exist_ok=True)
    manifest = dict(schema_version=1, mode='facts-v2', run_id='synthetic-inspection',
        company='Example Inspection', as_of='2026-10-09',
        scope='Fiktiver Offline-Test · Industrieinspektion, keine reale Firmenanalyse',
        selected_roles=['context', 'portfolio', 'cluster', 'market'],
        topics=[dict(id='industry', label='Technologie & industrielle Integration')],
        person='Alex Example · Integration Lead (fiktiv)')
    sources = [dict(id=FACTS.source_id('https://example.org/' + p),
        name='Fiktive Testquelle', title=t, url='https://example.org/' + p,
        published_date='2026-08-01', accessed_date='2026-10-09',
        source_kind='Herstellerangabe' if p == 'company' else 'Partnerangabe', fictional=True)
        for p, t in [('company', 'Fiktives Produktdokument'),
                     ('partner', 'Fiktive Partneraktivitäten'), ('market', 'Fiktiver Marktvergleich')]]
    rows = [
        ('T1', 'Example Inspection bietet im Testdatensatz industrielle Inspektionssoftware an.', 0),
        ('T2', 'Eine neue Integrationsschnittstelle wurde im Testdatensatz am 01.08.2026 vorgestellt.', 0),
        ('H1', 'Alex Example verantwortet laut fiktivem Profil die industrielle Integration.', 0),
        ('P1', 'Das fiktive Inspection Kit wird als Softwaremodul angeboten.', 0),
        ('P2', 'Example Inspection ist laut Testdatensatz in Europa über einen Integrationspartner vertreten.', 1),
        ('M1', 'Das Zielsystem wird laut fiktivem Produktdokument über eine API integriert.', 0),
        ('M2', 'Für das Zielsystem ist im Testdatensatz ein Labortest dokumentiert.', 0),
        ('M3', 'Für das Zielsystem ist im Testdatensatz ein Pilot vorgesehen; seine Umsetzung ist nicht belegt.', 0),
        ('M4', 'Der fiktive Wettbewerber TestPeer dokumentiert einen benannten Kundenpiloten.', 2),
        ('M5', 'Ein fiktives europäisches Programm unterstützt Inspektionspiloten bei Industriekunden.', 2),
        ('M6', 'TestPeer integriert laut Testdatensatz ein eigenes Komplettsystem.', 2),
        ('C1', 'Test Capital hält laut fiktiver Quelle 40 Prozent Kapitalanteile am Zielunternehmen.', 1),
        ('C2', 'Example Inspection und Example JV sind laut Testdatensatz über ein Joint Venture verbunden.', 1),
        ('C3', 'Test Sensor liefert laut Testdatensatz ein Sensormodul für die industrielle Integration.', 1),
        ('C4', 'Test Customer führt laut Testdatensatz einen angekündigten Inspektionspiloten durch.', 1),
        ('C5', 'Example JV und Test Sensor dokumentieren im Testdatensatz eine Integrationskooperation.', 1),
        ('C6', 'Für das fiktive Joint Venture wird im Testdatensatz industrielle Integration als Gegenstand genannt.', 1)]
    claims = [dict(id=cid, statement=statement,
        kind='Herstellerangabe' if n == 0 else 'Partnerangabe', source_ids=[sources[n]['id']],
        evidence='Paraphrase: ' + statement, location='Fiktiver Abschnitt ' + cid,
        uncertainty='Synthetischer Test; keine öffentlich recherchierte Aussage') for cid, statement, n in rows]
    by = {r['id']: r for r in claims}
    modules = []
    for role, prefix in [('context', 'TH'), ('portfolio', 'P'), ('cluster', 'C'), ('market', 'M')]:
        chosen = [r for r in claims if r['id'][0] in prefix]
        sids = {sid for r in chosen for sid in r['source_ids']}
        module = {k: v for k, v in manifest.items() if k not in {'selected_roles', 'topics', 'person'}}
        module.update(role=role, status='vollständig', claims=chosen,
            source_proposals=[s for s in sources if s['id'] in sids], gaps=[],
            coverage=[dict(topic=role, status='synthetischer Offline-Datensatz',
                finding='Nur bereitgestellte Testdokumente; keine URL geöffnet')],
            document_scope='Fiktiver Testdatensatz; keine reale Recherche oder Quellenfreigabe')
        modules.append(module)
    context, portfolio, cluster, market = modules
    context.update(company_facts=[dict(id='business', label='Industrielle Inspektionssoftware', claim_ids=['T1'])],
        events=[dict(id='launch', label='Integrationsschnittstelle vorgestellt', date='2026-08-01', claim_ids=['T2'])],
        profile=dict(name='Alex Example', claim_ids=['H1']))
    portfolio.update(products=[dict(id='kit', label='Inspection Kit', claim_ids=['P1'])],
        regions=[dict(id='europe', label='Europa · Partnerpräsenz', claim_ids=['P2'])],
        topics=[dict(id='industry', label='Produktintegration', claim_ids=['P1'])])
    cluster.update(topics=[dict(id='industry', label='Industrie- und Integrationspartner', claim_ids=['C3', 'C6'])],
        report_log=[dict(actor='Example Inspection', status='synthetischer Offline-Test',
                        finding='Keine echten Geschäftsberichte gesucht oder geöffnet')])
    cluster['network'] = dict(schema_version=1, company=manifest['company'], as_of=manifest['as_of'],
        target_id='target', nodes=[dict(id='target', label=manifest['company'], kind='target'),
            dict(id='owner', label='Test Capital', kind='owner', cluster='capital', focus=True),
            dict(id='jv', label='Example JV', kind='jv', cluster='structure', focus=True),
            dict(id='sensor', label='Test Sensor', kind='supplier', cluster='technology', focus=True),
            dict(id='customer', label='Test Customer', kind='customer', cluster='market', focus=True)],
        products=[dict(id='kit', label='Inspection Kit')], sources=[sources[1]], edges=[])
    for cid, a, b, category, description in [('C1', 'owner', 'target', 'owner', 'Kapitalbeteiligung'),
            ('C2', 'target', 'jv', 'jv', 'Joint Venture'), ('C3', 'sensor', 'target', 'supplier', 'Sensormodul'),
            ('C4', 'target', 'customer', 'customer', 'Angekündigter Kundenpilot'),
            ('C5', 'jv', 'sensor', 'partner', 'Integrationskooperation')]:
        edge = dict(id='e' + cid, **{'from': a, 'to': b}, type=description, summary=by[cid]['statement'],
            categories=[category], product_ids=['kit'] if cid in {'C3', 'C4', 'C5'} else [],
            source_ids=[sources[1]['id']], claim_ids=[cid], status='im Testdatensatz berichtet',
            as_of='2026-08', uncertainty='Fiktiver Datensatz')
        if cid == 'C1':
            edge.update(capital_share='40 % (fiktiv)', voting_share='öffentlich nicht verifiziert',
                        control='Keine Kontrollaussage aus Kapitalanteil abgeleitet')
        cluster['network']['edges'].append(edge)
    plan = {k: manifest[k] for k in ('run_id', 'company', 'as_of')}
    plan.update(version=1, comparison_unit='Industrielle Inspektionssoftware',
        purpose='Auftragsbezogene Integration und öffentlich belegte Erprobung vergleichen',
        peer_groups=['Direkte Vergleichsangebote'], criteria=[dict(id='integration', label='Integrationsmodell',
            display_type='Profil', question='Wie wird das Angebot industriell integriert?',
            evidence_required='Dokumentierte Schnittstelle und Rollenverteilung', applicability='Inspektionssysteme',
            rationale='Nutzerthema Industrieintegration'), dict(id='validation', label='Belegte Erprobung',
            display_type='Evidenzstufe', question='Welche Erprobung ist belegt?', evidence_required='Test-/Pilotbeleg',
            applicability='Inspektionssysteme', rationale='Angebot von Umsetzung unterscheiden',
            anchors={'1': 'Angebot dokumentiert', '2': 'Labortest dokumentiert', '3': 'Benannter Kundenpilot dokumentiert'})],
        assessment_methods=[dict(id='maturity', assessment_type='product_maturity', applicability='Inspection Kit',
            anchors={'1': 'Angeboten', '2': 'Im Labor erprobt', '3': 'Benannter Kundenpilot'}),
            dict(id='presence', assessment_type='regional_presence', applicability='Europäische Präsenz',
            anchors={'1': 'Partnerpräsenz', '2': 'Kundenpilot', '3': 'Fertigungsstandort'})])
    market.update(comparison_plan_version=1, peers=[dict(id='target', label='Example Inspection'),
        dict(id='peer', label='TestPeer')], observations=[dict(peer_id=p, criterion_id=c, claim_ids=ids)
        for p, c, ids in [('target', 'integration', ['M1']), ('target', 'validation', ['M2', 'M3']),
                         ('peer', 'integration', ['M6']), ('peer', 'validation', ['M4'])]],
        regions=[dict(id='europe', label='Europa · Industrie- und Pilotprogramme', claim_ids=['M5'])])
    validation, facts = FACTS.build(manifest, modules, plan)
    if validation['errors']:
        raise ValueError(validation['errors'])
    review_base = {k: manifest[k] for k in ('run_id', 'company', 'as_of')}
    review_base.update(schema_version=1, phase='basis', status='freigegeben', material_errors=[],
        review_scope='SIMULIERT: bereitgestellte fiktive Daten; keine öffentliche Quellenprüfung',
        claims=[dict(id=cid, depth='A', status='geprüft', evidence_review='SIMULIERTE Offline-Entscheidung') for cid in by])
    basis = STAMP.stamp(review_base, validation)
    pos_context = CHECK.prepare(manifest, facts, basis, ['P1', 'P2', 'C3', 'M5'], plan, market)
    interpretations = []
    for n, (p, c, ids, value) in enumerate([('target', 'integration', ['M1'], 'API-Integration'),
        ('target', 'validation', ['M2', 'M3'], 2), ('peer', 'integration', ['M6'], 'Komplettsystem'),
        ('peer', 'validation', ['M4'], 3)], 1):
        interpretations.append(dict(id='I' + str(n), statement='Einordnung des fiktiven Integrations-/Erprobungsbefunds',
            section='competition', depends_on=ids, reasoning='Ableitung ausschließlich aus den genannten fiktiven Belegen.',
            method='Fixierter Vergleichsplan', uncertainty='Synthetischer Test', type='matrix_cell',
            peer_id=p, criterion_id=c, cell_status='bewertet', value=value,
            next_stage_limit='Nächsthöhere Stufe nicht im Datensatz belegt' if value != 3 else 'Höchster definierter Skalenanker'))
    for n, cid, statement in [(10, 'M1', 'API-Integration bildet den technischen Ansatz des fiktiven Angebots.'),
        (11, 'P1', 'Das Inspection Kit ist im Testdatensatz als Softwaremodul dokumentiert.'),
        (12, 'C3', 'Der fiktive Sensorpartner ist für die industrielle Integration relevant.'),
        (13, 'M5', 'Europäische Pilotprogramme bieten im Beispieldatensatz einen möglichen Marktzugang.')]:
        interpretations.append(dict(id='I' + str(n), statement=statement, section='executive_summary',
            depends_on=[cid], reasoning='Qualitative Einordnung des genannten fiktiven Befunds.',
            method='Auftragsbezogene Synthese', uncertainty='Keine reale Unternehmensbewertung'))
    for n, kind, method, subject, score, ids, section in [(20, 'product_maturity', 'maturity', 'Inspection Kit', 2, ['M2', 'P1'], 'portfolio'),
        (21, 'regional_presence', 'presence', 'Europa', 1, ['P2'], 'regions')]:
        interpretations.append(dict(id='I' + str(n), type=kind, method_id=method, subject=subject, score=score,
            statement='Belegte Stufe für ' + subject + ' im fiktiven Datensatz', section=section,
            depends_on=ids, reasoning='Die genannte Stufe folgt aus den bereitgestellten fiktiven Belegen.',
            method='Vorab definierte Skalenanker', uncertainty='Kein realer Reife-/Präsenznachweis'))
    positioning = dict(schema_version=1, mode='interpret-v2', role='positioning', run_id=manifest['run_id'],
        company=manifest['company'], as_of=manifest['as_of'], scope=manifest['scope'], status='vollständig',
        input_fingerprint=pos_context['fingerprint'], plan_fingerprint=pos_context['plan_fingerprint'],
        interpretations=interpretations, research_requests=[], shared_limitations=['Fiktiver Offline-Test'])
    pos_report = CHECK.validate_output(manifest, facts, basis, pos_context, positioning, latest_plan=plan)
    swot_context = CHECK.prepare(manifest, facts, basis, ['M5'], plan, positioning=positioning,
        positioning_context=pos_context, interpretation_ids=['I20'])
    swot = {k: v for k, v in positioning.items() if k != 'plan_fingerprint'}
    swot.update(role='swot', input_fingerprint=swot_context['fingerprint'], interpretations=[
        dict(id='S1', category='Strengths', statement='Dokumentierte Labortests unterstützen die technische Vorprüfung des fiktiven Moduls.',
            section='swot', depends_on=['I20'], reasoning='Bereits vorhandene Testevidenz ist eine interne Fähigkeit im Testdatensatz.',
            method='Interne bestehende Fähigkeit', uncertainty='Keine reale Stärke nachgewiesen'),
        dict(id='S2', category='Opportunities', statement='Europäische Inspektionspilotprogramme könnten Zugang zu neuen Kunden eröffnen.',
            section='swot', depends_on=['M5'], reasoning='Das externe fiktive Programm unterstützt passende Inspektionspiloten.',
            method='Externe zukünftige Chance', uncertainty='Teilnahme/Erfolg nicht belegt')])
    swot_report = CHECK.validate_output(manifest, facts, basis, swot_context, swot,
        latest_positioning=positioning, latest_positioning_context=pos_context, latest_plan=plan)
    final_validation = CHECK.merge_reports([pos_report, swot_report])
    draft = {**review_base, 'phase': 'final', 'claims': [dict(id=cid, depth='A', status='geprüft',
        evidence_review='SIMULIERTE Offline-Ableitungsprüfung') for cid in final_validation['fingerprints']]}
    final = STAMP.stamp(draft, final_validation)
    files = {'facts-run.json': manifest, 'review-packet.json': facts, 'review-basis.json': basis,
        'positioning-context.json': pos_context, 'positioning.json': positioning,
        'swot-context.json': swot_context, 'swot.json': swot, 'review-final.json': final,
        'comparison-plan.json': plan}
    for name, data in files.items():
        (root / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    body = RENDER.build(manifest, facts, basis, positioning, pos_context, swot, swot_context, final, plan, full=True)
    (root / 'briefing-demo.html').write_text(body, encoding='utf-8')
    print(json.dumps({'output': str(root / 'briefing-demo.html'), 'facts': len(claims),
        'interpretations': len(interpretations) + len(swot['interpretations']), 'notice': 'All data/reviews synthetic; no URL opened'}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True)
    generate(parser.parse_args().out)
