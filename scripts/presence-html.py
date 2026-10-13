"""Reviewed regional infrastructure/channel evidence and the fixed 1–5 rubric."""
import copy
import html
import re
from datetime import date
from pathlib import Path

METHOD = 'regional-presence-v1'
SECTION = 'regional_presence'
STAGES = {'1': 'Angekündigter Zugang / Betreuung aus dem Ausland',
          '2': 'Lokaler Vertriebs- / Servicepartner', '3': 'Eigene Gesellschaft / eigenes Büro',
          '4': 'Eigene Produktion / operative Serviceinfrastruktur',
          '5': 'Eigene Produktion plus Entwicklung / mehrere eigene Standorte'}
KINDS = {'access', 'foreign_support', 'partner', 'office', 'production', 'service', 'development', 'customer_activity'}
OPERATORS = {'own', 'partner', 'jv', 'customer', 'foreign'}
LOCAL = {'partner', 'office', 'production', 'service', 'development', 'customer_activity'}
OWN_SITE = {'office', 'production', 'service', 'development'}


def esc(value):
    return html.escape(str(value), quote=True)


def validate(rows, require, as_of):
    def fail(message):
        raise ValueError('regional_presence: ' + message)
    def text(row, key, limit=None):
        value = row.get(key)
        if not isinstance(value, str) or not value.strip() or (limit and len(value) > limit):
            fail('missing/invalid ' + key)
    def refs(value, empty=False):
        if not isinstance(value, list) or (not value and not empty) or any(not isinstance(c, str) for c in value) or len(set(value)) != len(value):
            fail('claim_ids must be unique factual references')
        if value:
            require(value)
    if not isinstance(rows, list):
        fail('must be a list')
    ids = set()
    forbidden = {'score', 'grade', 'method_id', 'assessment_status', 'interpretation', 'interpretations', 'rankings', 'scores'}
    for row in rows:
        if not isinstance(row, dict):
            fail('region must be an object')
        if set(row) & forbidden:
            fail('facts must not contain assessments')
        text(row, 'id'); text(row, 'label', 80)
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*', row['id']) or row['id'] in ids:
            fail('id invalid/duplicate')
        ids.add(row['id'])
        for key in ('geographic_scope', 'product_scope', 'coverage_note'):
            text(row, key)
        if type(row.get('focus', False)) is not bool:
            fail('focus must be boolean')
        countries = row.get('countries')
        if not isinstance(countries, list) or any(not isinstance(c, str) or not c.strip() for c in countries) or len(set(countries)) != len(countries):
            fail('countries must be unique evaluation-country names')
        refs(row.get('claim_ids'), empty=True)
        activities = row.get('activities')
        if not isinstance(activities, list):
            fail('activities must be a list')
        if activities or row.get('claim_ids'):
            text(row, 'presence_type', 100)
        elif row.get('presence_type'):
            fail('presence_type needs factual evidence')
        activity_ids, sites = set(), {}
        for activity in activities:
            if not isinstance(activity, dict):
                fail('activity must be an object')
            if set(activity) & forbidden:
                fail('activity must not contain assessments')
            for key in ('id', 'actor', 'country', 'location', 'product_scope', 'description'):
                text(activity, key)
            if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*', activity['id']) or activity['id'] in activity_ids:
                fail('activity id invalid/duplicate')
            activity_ids.add(activity['id'])
            kind, operator, status = activity.get('kind'), activity.get('operator'), activity.get('status')
            if not isinstance(kind, str) or kind not in KINDS or not isinstance(operator, str) or operator not in OPERATORS or status not in ('announced', 'operational'):
                fail('invalid activity kind/operator/status')
            if (kind == 'access' and status != 'announced') or (kind == 'foreign_support' and operator != 'foreign') or (kind == 'partner' and operator not in ('partner','jv')) or (kind == 'customer_activity' and operator != 'customer') or (kind in OWN_SITE and operator not in ('own','partner','jv')):
                fail('activity kind/operator/status mismatch')
            if kind in LOCAL and activity['country'] not in countries:
                fail('local activity outside evaluation countries')
            if operator == 'own' and kind in OWN_SITE:
                text(activity, 'site_id'); text(activity, 'ownership_note')
                if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*', activity['site_id']):
                    fail('site_id must be stable and safe')
                location = (activity['country'], activity['location'])
                if activity['site_id'] in sites and sites[activity['site_id']] != location:
                    fail('site_id maps to conflicting locations')
                if any(sid != activity['site_id'] and old == location for sid, old in sites.items()):
                    fail('same location cannot count as multiple own sites')
                sites[activity['site_id']] = location
            stamp = activity.get('status_date')
            if stamp is not None:
                try:
                    valid = isinstance(stamp, str) and bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', stamp)) and date.fromisoformat(stamp) <= date.fromisoformat(as_of)
                except (TypeError, ValueError):
                    valid = False
                if not valid:
                    fail('status_date invalid or newer than briefing')
            refs(activity.get('claim_ids'))
            if not set(activity['claim_ids']) <= set(row['claim_ids']):
                fail('activity references facts outside region')


def eligible_stage(region, dependencies=None):
    """Only the verified subset used by an I-claim can satisfy the rubric."""
    allowed = set(region['claim_ids'] if dependencies is None else dependencies)
    activities = [a for a in region['activities'] if set(a['claim_ids']) <= allowed]
    own = [a for a in activities if a['operator'] == 'own' and a['status'] == 'operational' and a['kind'] in OWN_SITE]
    kinds = {a['kind'] for a in own}
    sites = {a['site_id'] for a in own}
    if 'production' in kinds and ('development' in kinds or len(sites) >= 2):
        return 5
    if kinds & {'production', 'service'}:
        return 4
    if kinds & {'office', 'development'}:
        return 3
    if any(a['operator'] in {'partner','jv'} and a['status'] == 'operational' and a['kind'] in LOCAL - {'customer_activity'} for a in activities):
        return 2
    if any(a['kind'] != 'customer_activity' and (a['status'] == 'announced' or a['kind'] == 'foreign_support') for a in activities):
        return 1
    return None


def is_assessment(row):
    return row.get('type') == 'regional_presence' and 'region_id' in row


def context(facts, require, as_of):
    views = [v for v in facts.get('module_views', []) if v.get('role') == 'portfolio']
    rows = views[0].get('regional_presence', []) if views else []
    validate(rows, require, as_of)
    return dict(method_id=METHOD, stages=STAGES, regions=copy.deepcopy(rows))


def assessment_errors(row, regions):
    errors = []
    cid = str(row.get('id'))
    region = next((r for r in regions if r['id'] == row.get('region_id')), None)
    if not region:
        return [cid + ': presence assessment needs a delegated region']
    if row.get('method_id') != METHOD or row.get('section') != SECTION:
        errors.append(cid + ': presence needs canonical method/section')
    deps = row.get('depends_on')
    if not isinstance(deps, list) or any(not isinstance(c, str) or c not in region['claim_ids'] for c in deps):
        return errors + [cid + ': presence depends_on must use this region facts directly']
    expected = eligible_stage(region)
    score, state = row.get('score'), row.get('assessment_status')
    if expected is None:
        if score is not None or state != 'nicht eindeutig bestimmbar' or not isinstance(row.get('coverage_note'), str) or not row['coverage_note'].strip():
            errors.append(cid + ': presence gap needs null score, unassessed status and coverage_note')
    else:
        if state != 'bewertet' or type(score) is not int or score != expected:
            errors.append(cid + ': presence score must match highest supported stage ' + str(expected))
        if eligible_stage(region, deps) != expected:
            errors.append(cid + ': presence dependencies do not support the selected stage')
        if not isinstance(row.get('next_stage_limit'), str) or not row['next_stage_limit'].strip():
            errors.append(cid + ': presence needs next-stage evidence limit')
    return errors


def binding(context, row):
    upstream = context.get('upstream_presence_contexts', {})
    if row['id'] in upstream:
        return upstream[row['id']]
    data = context.get('regional_presence') or {}
    return dict(method_id=data.get('method_id'), stages=data.get('stages'),
                region=next((r for r in data.get('regions', []) if r['id'] == row.get('region_id')), None))


def render(regions, assessments, detail, as_of):
    if not regions:
        return '<p class="rp-empty">Keine freigegebenen regionalen Präsenzbefunde für diesen Auftrag.</p>'
    out = '<div id="briefing-regional-presence" class="rp-root"><p class="rp-intro">Öffentlich belegte Infrastruktur und Vertriebszugang · feste Präsenzskala 1–5</p><div class="rp-chart" role="group" aria-label="Regionale Unternehmenspräsenz">'
    for region in regions:
        row = assessments.get(region['id'])
        score = row['score'] if row else None
        state = str(score) + '/5' if score is not None else '—'
        desc = region.get('presence_type') or 'Öffentlich nicht eindeutig bestimmbar'
        if row is None:
            state = 'Unbewertet'
        dots = ''.join('<i class="rp-dot' + (' rp-filled' if score is not None and i <= score else '') + '"></i>' for i in range(1,6))
        label = region['label'] + ': ' + (str(score) + ' von 5' if score is not None else state + ' · keine Präsenzstufe bestimmt') + ' · ' + desc + ' · Details'
        out += '<a class="rp-row' + (' rp-focus' if region.get('focus') else '') + '" href="#presence-region-' + esc(region['id']) + '" aria-label="' + esc(label) + '"><strong>' + esc(region['label']) + '</strong><span class="rp-type">' + esc(desc) + '<small>' + esc(region['product_scope']) + '</small></span><span class="rp-score"><span class="rp-dots" aria-hidden="true">' + dots + '</span><b>' + esc(state) + '</b><span aria-hidden="true">↗</span></span></a>'
    out += '</div><p class="rp-caption">Region anklicken → Begründung, Details und Quellen. Keine Messung von Umsatz oder Marktanteil. Regionale Aggregate zeigen den belegten Schwerpunkt. Stand: ' + esc(as_of) + '.</p><details class="rp-method"><summary>Wie die Skala 1–5 definiert ist</summary><ol>'
    for score, label in STAGES.items():
        out += '<li><strong>Stufe ' + score + '</strong> — ' + esc(label) + '</li>'
    out += '</ol><p>Die höchste konkret belegte Stufe zählt. Geplante Standorte sind kein laufender Betrieb; Partner/JV-Infrastruktur ist ohne belegte eigene Kontrolle kein eigener Standort. Die Stufen sind ordinal und unabhängig von der Produktreife 1–6. Fehlende Evidenz ist kein Beweis fehlender Aktivität.</p></details><div class="rp-profiles"><h3>Regionale Deep Dives</h3>'
    for region in regions:
        row = assessments.get(region['id'])
        score = row['score'] if row else None
        state = str(score) + '/5' if score is not None else 'Nicht eindeutig bestimmbar' if row else 'Noch nicht bewertet'
        out += '<details class="rp-profile" id="presence-region-' + esc(region['id']) + '"><summary><strong>' + esc(region['label']) + '</strong><span>' + esc(state) + ' · Deep Dive</span></summary><div class="rp-profile-body">' + detail(region, row) + '</div></details>'
    out += '</div></div>'
    assets = Path(__file__).resolve().parents[1]/'references/templates'
    return '<style>' + (assets/'presence.css').read_text(encoding='utf-8') + '</style>' + out + '<script>' + (assets/'presence.js').read_text(encoding='utf-8') + '</script>'
