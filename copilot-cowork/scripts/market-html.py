"""Validate and render sourced market comparisons; no research or scoring here."""
import html
import math
import re
from datetime import date
from pathlib import Path

STAGES = {'planning': 'Planung', 'announced': 'Angekündigt / genehmigt',
          'contracted': 'Beauftragt', 'delivery': 'In Auslieferung'}
ROLES = {'dev': 'Entwicklung', 'license': 'Lizenzfertigung',
         'integration': 'Integration', 'service': 'Wartung'}
STATUSES = {'actual': 'Ist / berichtet', 'plan': 'Plan', 'forecast': 'Prognose'}
VALUE_TYPES = {'contract': 'Vertragswert', 'ceiling': 'Genehmigungsobergrenze', 'estimate': 'Schätzung'}


def esc(value):
    return html.escape(str(value), quote=True)


def number(value, digits=1):
    return f'{value:,.{digits}f}'.replace(',', '\u0000').replace('.', ',').replace('\u0000', '.')


def validate(data, require, as_of):
    """Every displayed factual row must map to known/current A claims via require."""
    def fail(message):
        raise ValueError('market_dashboard: ' + message)

    def obj(row):
        if not isinstance(row, dict):
            fail('row must be an object')
        return row

    def text(row, *keys):
        obj(row)
        for key in keys:
            if not isinstance(row.get(key), str) or not row[key].strip():
                fail('missing text ' + key)

    def refs(row):
        if not isinstance(row.get('claim_ids'), list) or not row['claim_ids'] or any(not isinstance(cid, str) for cid in row['claim_ids']):
            fail('factual row requires claim_ids')
        require(row.get('claim_ids'))

    def rows(value, name, nonempty=False):
        if not isinstance(value, list) or (nonempty and not value):
            fail(name + ' must be ' + ('a nonempty list' if nonempty else 'a list'))
        for row in value:
            obj(row)
        return value

    def indexed(value, name):
        values = rows(value, name, True)
        seen = set()
        for row in values:
            text(row, 'id', 'label')
            rid = row['id']
            if not re.fullmatch(r'[a-zA-Z][a-zA-Z0-9_-]*', rid) or rid in seen:
                fail(name + ' id invalid/duplicate')
            seen.add(rid)
        return seen

    def years(value, name, minimum=2):
        if not isinstance(value, list) or len(value) < minimum or any(type(y) is not int or not 1900 <= y <= 2200 for y in value):
            fail(name + ' needs calendar years')
        if value != list(range(value[0], value[-1] + 1)):
            fail(name + ' must be consecutive and ascending')

    def numeric(value):
        try:
            valid = type(value) in (int, float) and math.isfinite(value) and value >= 0
        except OverflowError:
            valid = False
        if not valid:
            fail('value must be a finite nonnegative number')

    def choice(value, choices):
        return isinstance(value, str) and value in choices

    def dated(row):
        try:
            valid = isinstance(row.get('status_date'), str) and bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', row['status_date'])) and date.fromisoformat(row['status_date']) <= date.fromisoformat(as_of)
        except (TypeError, ValueError):
            valid = False
        if not valid:
            fail('status_date invalid or newer than briefing')

    obj(data)
    try:
        date.fromisoformat(as_of)
    except (TypeError, ValueError):
        fail('briefing as_of invalid')
    def boundary(value):
        if isinstance(value, dict):
            if set(value) & {'score', 'scores', 'grade', 'rank', 'ranking', 'rankings', 'interpretation', 'interpretations'}:
                fail('interpretations/scores prohibited in factual dashboard')
            for item in value.values():
                boundary(item)
        elif isinstance(value, list):
            for item in value:
                boundary(item)
    boundary(data)
    if type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        fail('schema_version must be 1')
    text(data, 'title', 'scope', 'programme_scope', 'programme_method')
    years(data.get('years'), 'years', 5)
    if len(data['years']) != 5:
        fail('years needs exactly five years')
    years(data.get('timeline_years'), 'timeline_years')
    metric_ids = indexed(data.get('metrics'), 'metrics')
    function_ids = indexed(data.get('functions'), 'functions')
    indexed(data.get('countries'), 'countries')
    for metric in data['metrics']:
        text(metric, 'unit', 'currency', 'price_basis', 'definition')
        if not choice(metric.get('purpose'), {'context', 'segment'}):
            fail('metric purpose must be context/segment')
        refs(metric)
    programme_ids = set()
    for country in data['countries']:
        text(country, 'coverage_note')
        series = country.get('series')
        if not isinstance(series, dict) or set(series) != metric_ids:
            fail('country series must cover all metrics')
        for mid, values in series.items():
            rows(values, 'series', True)
            if [r.get('year') for r in values] != data['years']:
                fail('series must cover declared years in order')
            for row in values:
                if type(row.get('year')) is not int:
                    fail('series year must be an integer')
                if row.get('value') is None:
                    text(row, 'missing_reason')
                    if row.get('claim_ids'):
                        refs(row)
                    continue
                numeric(row['value'])
                if not choice(row.get('status'), STATUSES) or type(row.get('comparable')) is not bool:
                    fail('series needs status and comparable flag')
                if row['status'] == 'actual' and row['year'] > int(as_of[:4]):
                    fail('future year cannot be an actual observation')
                if not row['comparable']:
                    text(row, 'comparison_note')
                refs(row)
        for programme in rows(country.get('programmes'), 'programmes'):
            text(programme, 'id', 'label', 'customer', 'provider', 'local_role', 'next_step')
            if not re.fullmatch(r'[a-zA-Z][a-zA-Z0-9_-]*', programme['id']) or programme['id'] in programme_ids:
                fail('programme id invalid/duplicate; count a programme only once')
            programme_ids.add(programme['id'])
            if not choice(programme.get('status'), STAGES):
                fail('invalid programme status')
            dated(programme)
            refs(programme)
            value = programme.get('value')
            if value is not None:
                obj(value)
                numeric(value.get('amount'))
                text(value, 'unit', 'currency', 'period', 'price_basis')
                if not choice(value.get('type'), VALUE_TYPES):
                    fail('programme value requires contract/ceiling/estimate')
                refs(value)
            window = programme.get('window')
            if window is not None:
                obj(window)
                if any(type(window.get(k)) is not int or not 1900 <= window[k] <= 2200 for k in ('start', 'end')) or window['start'] > window['end']:
                    fail('programme window needs ordered years')
                text(window, 'label')
                refs(window)
        roles = country.get('roles')
        if not isinstance(roles, dict) or set(roles) != function_ids:
            fail('roles must cover all functions')
        for cell in roles.values():
            obj(cell)
            entries = rows(cell.get('entries'), 'role entries')
            if not entries:
                text(cell, 'gap_reason')
            for row in entries:
                text(row, 'actor', 'location', 'activity')
                if not choice(row.get('role'), ROLES):
                    fail('invalid industrial role')
                dated(row)
                refs(row)
        for row in rows(country.get('access'), 'access'):
            text(row, 'label', 'text')
            refs(row)
        for row in rows(country.get('factors'), 'factors'):
            text(row, 'label', 'text')
            if not choice(row.get('kind'), {'driver', 'constraint'}):
                fail('factor kind must be driver/constraint')
            refs(row)


def cagr(series):
    """Observed growth only; never mix plans, forecasts or incompatible bases."""
    if any(r.get('value') is None or r.get('status') != 'actual' or not r.get('comparable') for r in series):
        return None
    first, last = series[0], series[-1]
    if first['value'] <= 0:
        return None
    result = (math.pow(last['value'] / first['value'], 1 / (last['year'] - first['year'])) - 1) * 100
    return result if math.isfinite(result) else None


def programme_counts(country):
    return {stage: sum(p['status'] == stage for p in country['programmes']) for stage in STAGES}


def render(data, fact_detail):
    """Pure rendering of a validated/reviewed dashboard, including static fallback."""
    years = data['years']
    countries = data['countries']

    def facts(row):
        return fact_detail(row.get('claim_ids', []))

    def country_link(country, body, kind='', function=None):
        return '<a class="mk-pick ' + kind + '" href="#market-country-' + esc(country['id']) + '" data-mk-country="' + esc(country['id']) + '"' + (' data-mk-function="' + esc(function) + '"' if function else '') + ' aria-pressed="false">' + body + '</a>'

    def ticks(lo, hi, digits=1):
        marks = sorted(set([lo, 0, hi]))
        return '<div class="mk-axis"><span></span><div class="mk-ticks-positioned">' + ''.join('<span style="left:' + str((v-lo)/(hi-lo)*100) + '%;transform:translateX(' + ('0' if v == lo else '-100%' if v == hi else '-50%') + ')">' + esc(number(v, digits)) + '</span>' for v in marks) + '</div><span></span></div>'

    def chart(metric, growth=False):
        mid = metric['id']
        values = []
        for country in countries:
            series = country['series'][mid]
            latest = series[-1]
            values.append(cagr(series) if growth else latest.get('value') if latest.get('comparable') and latest.get('status') == 'actual' else None)
        available = [v for v in values if v is not None]
        lo = min(0, min(available, default=0)) if growth else 0
        hi = max(0, max(available, default=1)) or 1
        if lo == hi:
            hi = lo + 1
        # Rounded common axes keep exact figures visible alongside each bar.
        step = 10 ** math.floor(math.log10(max(hi-lo, 0.01)))
        lo = math.floor(lo/step)*step
        hi = max(lo + step, math.ceil(hi/step)*step)
        out = ticks(lo, hi) if available else '<p class="mk-empty">Keine vergleichbaren Ist-Werte für diesen Vergleich im Paket.</p>'
        for country, value in zip(countries, values):
            row = country['series'][mid][-1]
            missing = 'Keine vergleichbare Ist-Zeitreihe' if growth else row.get('missing_reason') or row.get('comparison_note') or 'Kein vergleichbarer Ist-Wert'
            status = '' if growth or value is None else '<small>' + esc(STATUSES[row['status']]) + '</small>'
            bar = '<span class="mk-missing">' + esc(missing) + '</span>' if value is None else '<span class="mk-bar' + (' mk-growth-negative' if value < 0 else ' mk-growth' if growth else '') + '" style="left:' + str((min(0,value)-lo)/(hi-lo)*100) + '%;width:' + str(abs(value)/(hi-lo)*100) + '%"></span>'
            zero = '<i class="mk-zero" style="left:' + str(-lo/(hi-lo)*100) + '%"></i>' if growth else ''
            label = '—' if value is None else number(value) + (' %' if growth else '')
            out += country_link(country, '<span class="mk-country">' + esc(country['label']) + '</span><span class="mk-bar-space">' + bar + zero + '</span><span class="mk-value">' + esc(label) + status + '</span>', 'mk-bar-row')
        return '<div class="mk-chart" data-mk-metric="' + esc(mid) + '" data-mk-chart="' + ('growth' if growth else 'value') + '">' + out + '</div>'

    def panel(title, caption, body, wide=False):
        return '<section class="mk-panel' + (' mk-panel-wide' if wide else '') + '"><h3>' + esc(title) + '</h3><p class="mk-caption">' + esc(caption) + '</p>' + body + '</section>'

    def definition(metric):
        return '<dl class="mk-data-dl">' + ''.join('<dt>' + esc(label) + '</dt><dd>' + esc(metric[key]) + '</dd>' for key, label in [('definition','Messgröße'), ('unit','Einheit'), ('currency','Währung'), ('price_basis','Preis- / Umrechnungsbasis')]) + '</dl>'

    out = '<div id="briefing-market" class="mk-app"><p class="mk-scope">' + esc(data['scope']) + '</p><div class="mk-panels">'
    for metric in data['metrics']:
        caption = metric['label'] + ' ' + str(years[-1]) + ' · ' + metric['unit'] + ' ' + metric['currency'] + ' · ' + metric['price_basis']
        purpose = 'Budget- / Größenkontext' if metric['purpose'] == 'context' else 'Volumen im betrachteten Segment'
        note = ('Kontextgröße; kein Marktvolumen des Zielsegments.' if metric['purpose'] == 'context' else metric['definition']) + ' Vergleich zeigt nur vergleichbare Ist-Werte; Plan und Prognose im Datenblatt.'
        out += panel(purpose, caption, chart(metric) + '<p class="mk-definition">' + esc(note) + '</p>')
        out += panel('Wachstum im selben Zeitraum', metric['label'] + ' · ' + str(years[0]) + '–' + str(years[-1]) + ' · CAGR pro Jahr', chart(metric, True) + '<p class="mk-definition">Nur vergleichbare Ist-Werte. Plan, Prognose und Datenlücken werden nicht als beobachtetes Wachstum dargestellt.</p>')
    counts = [programme_counts(c) for c in countries]
    maximum = max(1, max(sum(v.values()) for v in counts))
    bars = '<div class="mk-chart mk-pipeline">' + ticks(0, maximum, 0)
    for country, count in zip(countries, counts):
        total = sum(count.values())
        stack = ''.join('<span class="mk-segment" data-stage="' + s + '" style="width:' + str(count[s]/maximum*100) + '%" title="' + esc(STAGES[s]) + ': ' + str(count[s]) + '">' + str(count[s]) + '</span>' for s in STAGES if count[s])
        bars += country_link(country, '<span class="mk-country">' + esc(country['label']) + '</span><span class="mk-bar-space"><span class="mk-stack">' + stack + '</span></span><span class="mk-value">' + (str(total) if total else '—') + '</span>', 'mk-bar-row')
    legend = '<div class="mk-legend">' + ''.join('<span><i class="mk-swatch" data-stage="' + s + '"></i>' + esc(label) + '</span>' for s, label in STAGES.items()) + '</div>'
    out += panel('Beschaffungen im betrachteten Segment', data['programme_scope'] + ' · dokumentierte Programme nach aktuellem Status', bars + '</div>' + legend + '<p class="mk-definition">' + esc(data['programme_method']) + ' Genehmigung ist kein Auftrag. Programmwerte sind kein jährliches Marktvolumen; keine Programme im Paket bedeutet keine Aussage über den gesamten Markt.</p>', True)
    matrix = '<div class="mk-scroll"><table class="mk-industry"><thead><tr><th scope="col">Land</th>' + ''.join('<th scope="col">' + esc(f['label']) + '</th>' for f in data['functions']) + '</tr></thead><tbody>'
    for country in countries:
        matrix += '<tr><th scope="row">' + esc(country['label']) + '</th>'
        for function in data['functions']:
            entries = country['roles'][function['id']]['entries']
            roles = list(dict.fromkeys(r['role'] for r in entries))
            chips = ''.join('<span class="mk-role-chip" data-role="' + r + '">' + esc(ROLES[r]) + '</span>' for r in roles) or '<span class="mk-role-chip" data-role="gap">Beleg offen</span>'
            matrix += '<td>' + country_link(country, chips, 'mk-role', function['id']) + '</td>'
        matrix += '</tr>'
    matrix += '</tbody></table></div><p class="mk-definition">Farben unterscheiden Rollen, keine Rangfolge oder nationale Vollständigkeit. Beleg offen ist keine nachgewiesene Fähigkeitslücke. Zelle wählen, um Akteure und Belege zu sehen.</p>'
    out += panel('Industrielle Rollen nach Funktion', 'Konkrete Akteure, Tätigkeiten und Standorte im beauftragten Segment', matrix, True)
    out += '</div><section class="mk-detail" aria-live="polite" hidden></section><div class="mk-fallback"><h3>Länderdetails · Programme, Industrie &amp; Quellen</h3>'
    for country in countries:
        cid = country['id']
        record = '<section class="mk-country-record" id="market-country-' + esc(cid) + '" data-mk-label="' + esc(country['label']) + '"><h3>' + esc(country['label']) + '</h3><p class="mk-coverage">' + esc(country['coverage_note']) + '</p><section class="mk-tab-body" data-mk-section="programmes"><h4>Programme &amp; Zeitfenster</h4>'
        timeline = data['timeline_years']
        record += '<div class="mk-timeline"><div class="mk-window-axis" style="--mk-years:' + str(len(timeline)) + '">' + ''.join('<span>' + str(y) + '</span>' for y in timeline) + '</div>'
        for programme in country['programmes']:
            window = programme.get('window')
            if window:
                start, end = max(window['start'], timeline[0]), min(window['end'], timeline[-1])
                bar = '<span class="mk-window-bar" style="left:' + str((start-timeline[0])/len(timeline)*100) + '%;width:' + str((end-start+1)/len(timeline)*100) + '%">' + esc(str(window['start']) + '–' + str(window['end'])) + '</span>' if start <= end else '<span class="mk-missing">Außerhalb des Ausschnitts</span>'
                record += '<div class="mk-window-row"><span class="mk-window-label">' + esc(programme['label']) + '<small>' + esc(window['label']) + '</small></span><span class="mk-window">' + bar + '</span></div>'
            else:
                record += '<p class="mk-definition">' + esc(programme['label']) + ': kein belegtes Zeitfenster im Paket.</p>'
        record += '</div><div class="mk-programs">'
        for programme in country['programmes']:
            record += '<details class="mk-program"><summary><span>' + esc(programme['label']) + '</span><span class="mk-stage" data-stage="' + programme['status'] + '">' + esc(STAGES[programme['status']]) + '</span></summary><dl class="mk-data-dl">'
            for key, label in [('status_date','Status belegt am'), ('customer','Auftraggeber'), ('provider','Anbieter'), ('local_role','Lokale Rolle'), ('next_step','Nächster dokumentierter Schritt / offene Frage')]:
                record += '<dt>' + esc(label) + '</dt><dd>' + esc(programme[key]) + '</dd>'
            value = programme.get('value')
            label = 'Wert öffentlich nicht belegt'
            if value:
                label = VALUE_TYPES[value['type']] + ': ' + number(value['amount']) + ' ' + value['unit'] + ' ' + value['currency'] + ' · ' + value['period'] + ' · ' + value['price_basis']
            record += '<dt>Programmwert</dt><dd>' + esc(label) + '</dd></dl>' + facts(programme)
            if value:
                record += facts(value)
            if programme.get('window'):
                record += facts(programme['window'])
            record += '</details>'
        if not country['programmes']:
            record += '<p class="mk-empty">Keine freigegebenen Programme im Paket; kein Nachweis fehlender Nachfrage.</p>'
        record += '</div></section><section class="mk-tab-body" data-mk-section="industry"><h4>Industrie &amp; Marktzugang</h4><div class="mk-detail-grid"><div class="mk-role-list">'
        for function in data['functions']:
            cell = country['roles'][function['id']]
            record += '<section class="mk-function" data-mk-function-detail="' + esc(function['id']) + '"><h4>' + esc(function['label']) + '</h4>'
            for row in cell['entries']:
                record += '<p><span class="mk-role-chip" data-role="' + row['role'] + '">' + esc(ROLES[row['role']]) + '</span> <strong>' + esc(row['actor']) + '</strong></p><p>' + esc(row['activity']) + '</p><p class="mk-caption">' + esc(row['location']) + ' · Stand ' + esc(row['status_date']) + '</p>' + facts(row)
            if not cell['entries']:
                record += '<p class="mk-empty">Beleg offen: ' + esc(cell['gap_reason']) + '</p>'
            record += '</section>'
        record += '</div><div><h4>Beschaffung &amp; Zugang</h4>'
        for row in country['access']:
            record += '<section class="mk-access"><h4>' + esc(row['label']) + '</h4><p>' + esc(row['text']) + '</p>' + facts(row) + '</section>'
        if not country['access']:
            record += '<p class="mk-empty">Keine freigegebenen Zugangsvoraussetzungen im Paket.</p>'
        for row in country['factors']:
            record += '<section class="mk-access"><small>' + ('Dokumentierter Treiber' if row['kind'] == 'driver' else 'Dokumentierte Rahmenbedingung / Begrenzung') + '</small><h4>' + esc(row['label']) + '</h4><p>' + esc(row['text']) + '</p>' + facts(row) + '</section>'
        record += '</div></div></section><section class="mk-tab-body" data-mk-section="data"><h4>Werte, Methode &amp; Quellen</h4>'
        for metric in data['metrics']:
            series = country['series'][metric['id']]
            growth = cagr(series)
            record += '<h4>' + esc(metric['label']) + '</h4>' + definition(metric) + facts(metric) + '<div class="mk-scroll"><table class="mk-data-table"><thead><tr><th>Jahr</th><th>Wert</th><th>Einordnung</th><th>Belege</th></tr></thead><tbody>'
            for row in series:
                known = row.get('value') is not None
                desc = (STATUSES[row['status']] + (' · vergleichbar' if row['comparable'] else ' · ' + row['comparison_note'])) if known else row['missing_reason']
                record += '<tr><th scope="row">' + str(row['year']) + '</th><td>' + (esc(number(row['value']) + ' ' + metric['unit'] + ' ' + metric['currency']) if known else '—') + '</td><td>' + esc(desc) + '</td><td>' + facts(row) + '</td></tr>'
            record += '</tbody></table></div><p class="mk-definition">CAGR ' + str(years[0]) + '–' + str(years[-1]) + ': ' + (esc(number(growth) + ' % pro Jahr') if growth is not None else 'nicht berechenbar aus vergleichbaren Ist-Werten') + '. Formel: (Endwert / Anfangswert)^(1 / ' + str(years[-1]-years[0]) + ') − 1. Kein Segmentvolumen aus einer Kontextgröße abgeleitet.</p>'
        record += '<h4>Zählweise &amp; Grenzen</h4><p>' + esc(data['programme_method']) + '</p><p>' + esc(country['coverage_note']) + '</p></section></section>'
        out += record
    out += '</div></div>'
    assets = Path(__file__).resolve().parents[1] / 'references/templates'
    return '<style>' + (assets/'market.css').read_text(encoding='utf-8') + '</style>' + out + '<script>' + (assets/'market.js').read_text(encoding='utf-8') + '</script>'
