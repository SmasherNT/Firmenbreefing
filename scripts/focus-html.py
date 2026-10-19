"""Compact factual focus pages: validation and offline charts; no model calls."""
import calendar
from datetime import date
from html import escape
import math
import re


def esc(value):
    return escape(str(value), quote=True)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def rows(value, name):
    if not isinstance(value, list) or any(not isinstance(r, dict) for r in value):
        raise ValueError('focus: ' + name + ' must be object rows')
    ids = [r.get('id') for r in value]
    if any(not isinstance(i, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', i) for i in ids) or len(ids) != len(set(ids)):
        raise ValueError('focus: ' + name + ' needs unique safe ids')
    return value


def six_months_before(as_of):
    end = date.fromisoformat(as_of)
    index = end.year * 12 + end.month - 1 - 6
    year, month = divmod(index, 12)
    return date(year, month + 1, min(end.day, calendar.monthrange(year, month + 1)[1]))


def validate(requests, pages, require, as_of):
    requests = rows(requests, 'manifest focus_pages')
    pages = rows(pages, 'focus_pages')
    if any(not text(r.get('label')) for r in requests):
        raise ValueError('focus: requested label missing')
    if [r['id'] for r in pages] != [r['id'] for r in requests]:
        raise ValueError('focus: pages must match requested order and ids')
    start, end = six_months_before(as_of), date.fromisoformat(as_of)

    def mapped(row, field='label'):
        if not text(row.get(field)):
            raise ValueError('focus: missing ' + field)
        require(row.get('claim_ids'))

    for request, page in zip(requests, pages):
        if page.get('label') != request['label']:
            raise ValueError('focus: label differs from request')
        mapped(page, 'overview')
        theses = rows(page.get('theses'), 'theses')
        if not 1 <= len(theses) <= 5 or len(theses) < 3 and not text(page.get('coverage_note')):
            raise ValueError('focus: 3–5 theses; sparse evidence needs coverage_note')
        for thesis in theses:
            mapped(thesis)
        charts = rows(page.get('charts'), 'charts')
        if not charts and not text(page.get('visualization_note')):
            raise ValueError('focus: missing graphics needs visualization_note')
        for chart in charts:
            mapped(chart, 'title')
            kind = chart.get('type')
            if kind not in {'bars', 'matrix', 'structure'}:
                raise ValueError('focus: unsupported chart type')
            if kind == 'structure':
                groups = rows(chart.get('groups'), 'groups')
                if not groups:
                    raise ValueError('focus: structure needs groups')
                for group in groups:
                    mapped(group)
                    items = rows(group.get('items'), 'structure items')
                    if not items:
                        raise ValueError('focus: structure group needs items')
                    for item in items:
                        mapped(item)
            else:
                data = rows(chart.get('rows'), 'chart rows')
                if not data:
                    raise ValueError('focus: chart needs rows')
                if kind == 'matrix':
                    columns = rows(chart.get('columns'), 'columns')
                    if not columns or any(not text(c.get('label')) for c in columns):
                        raise ValueError('focus: matrix needs named columns')
                    for row in data:
                        mapped(row)
                        cells = rows(row.get('cells'), 'matrix cells')
                        if [c['id'] for c in cells] != [c['id'] for c in columns]:
                            raise ValueError('focus: matrix cells must match columns')
                        for cell in cells:
                            mapped(cell, 'value')
                else:
                    for key in ('unit', 'period', 'scope', 'metric'):
                        if not text(chart.get(key)):
                            raise ValueError('focus: comparable bars need ' + key)
                    for row in data:
                        mapped(row)
                        value = row.get('value')
                        if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                            raise ValueError('focus: bars need finite nonnegative values')
        events = rows(page.get('timeline'), 'timeline')
        if not events and not text(page.get('timeline_note')):
            raise ValueError('focus: empty timeline needs timeline_note')
        for event in events:
            mapped(event)
            if not text(event.get('status')) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(event.get('date', ''))):
                raise ValueError('focus: timeline date/status required')
            if not start <= date.fromisoformat(event['date']) <= end:
                raise ValueError('focus: timeline outside last six months')
        if not isinstance(page.get('gaps'), list) or any(not text(g) for g in page['gaps']):
            raise ValueError('focus: gaps must be text rows')


def render(page, details, as_of):
    def tile(row, body=''):
        return '<details class="focus-tile"><summary>' + esc(row.get('label', row.get('value', ''))) + '</summary>' + body + details(row['claim_ids']) + '</details>'
    def proof(ids):
        return '<details class="focus-proof"><summary>Fakten &amp; Belege</summary>' + details(ids) + '</details>'
    body = '<section class="module focus-intro"><p class="meta">Fokus · Faktenüberblick</p><h2>' + esc(page['label']) + '</h2><p>' + esc(page['overview']) + '</p>' + proof(page['claim_ids']) + '</section>'
    body += '<section class="module"><h2>Kernaussagen</h2><div class="focus-theses">' + ''.join('<div class="focus-thesis"><span class="focus-number">' + str(i) + '</span>' + tile(row) + '</div>' for i, row in enumerate(page['theses'], 1)) + '</div>'
    if page.get('coverage_note'):
        body += '<p class="meta">' + esc(page['coverage_note']) + '</p>'
    body += '</section>'
    for chart in page['charts']:
        body += '<section class="module focus-chart"><h2>' + esc(chart['title']) + '</h2>'
        if chart.get('caption'):
            body += '<p class="meta">' + esc(chart['caption']) + '</p>'
        if chart['type'] == 'bars':
            body += '<p class="meta">' + esc(' · '.join(chart[k] for k in ('metric', 'unit', 'period', 'scope'))) + '</p><div class="focus-bars">'
            maximum = max(row['value'] for row in chart['rows']) or 1
            for row in chart['rows']:
                graphic = '<div class="focus-bar-track"><span style="width:' + str(round(row['value'] / maximum * 100, 3)) + '%"></span></div><p class="focus-value">' + esc(format(row['value'], 'g')) + ' ' + esc(chart['unit']) + '</p>'
                body += '<div class="focus-bar-row">' + tile(row) + graphic + '</div>'
            body += '</div>'
        elif chart['type'] == 'matrix':
            body += '<div class="focus-table-wrap"><table class="focus-matrix"><thead><tr><th scope="col">Akteur / Bereich</th>' + ''.join('<th scope="col">' + esc(c['label']) + '</th>' for c in chart['columns']) + '</tr></thead><tbody>'
            for row in chart['rows']:
                body += '<tr><th scope="row">' + tile(row) + '</th>' + ''.join('<td>' + tile(cell) + '</td>' for cell in row['cells']) + '</tr>'
            body += '</tbody></table></div>'
        else:
            body += '<div class="focus-structure">'
            for group in chart['groups']:
                body += '<div class="focus-group">' + tile(group) + ''.join(tile(item) for item in group['items']) + '</div>'
            body += '</div>'
        body += proof(chart['claim_ids']) + '</section>'
    if page.get('visualization_note'):
        body += '<p class="meta">' + esc(page['visualization_note']) + '</p>'
    body += '<section class="module"><h2>Entwicklungen der letzten sechs Monate</h2><p class="meta">' + six_months_before(as_of).strftime('%d.%m.%Y') + '–' + date.fromisoformat(as_of).strftime('%d.%m.%Y') + '</p><div class="focus-timeline">'
    for event in sorted(page['timeline'], key=lambda e: (e['date'], e['id']), reverse=True):
        body += '<div class="focus-event"><time datetime="' + esc(event['date']) + '">' + date.fromisoformat(event['date']).strftime('%d.%m.%Y') + '</time><div><span class="focus-status">' + esc(event['status']) + '</span>' + tile(event) + '</div></div>'
    body += '</div>'
    if page.get('timeline_note'):
        body += '<p class="meta">' + esc(page['timeline_note']) + '</p>'
    body += '</section><section class="module"><details class="focus-gaps"><summary>Datenlücken &amp; Recherchegrenzen</summary>' + ''.join('<p>' + esc(g) + '</p>' for g in page['gaps']) + '</details></section>'
    return body


def css():
    return '''<style>
.focus-theses{display:grid;align-items:start;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.focus-thesis{border:1px solid #d7e4ea;border-top:3px solid #176274;border-radius:10px;padding:14px;background:#f3f8fa}.focus-number{font-size:25px;font-weight:700;color:#176274}.focus-tile{padding:9px 0}.focus-tile>summary{font-weight:600;cursor:pointer;overflow-wrap:anywhere}.focus-evidence{font-size:13px;color:#607887;padding:8px 0}.focus-evidence p{margin:7px 0}.focus-proof{font-size:12px;color:#607887;margin-top:12px}.focus-proof>summary{cursor:pointer}.focus-bars{display:grid;gap:12px}.focus-bar-row{padding:10px 14px;border:1px solid #d7e4ea;border-radius:8px}.focus-bar-track{height:14px;background:#e5edf1;border-radius:4px;overflow:hidden}.focus-bar-track>span{height:100%;display:block;background:#176274}.focus-value{font-size:13px;font-weight:700;margin:5px 0}.focus-table-wrap{overflow:auto}.focus-matrix{width:100%;border-collapse:collapse}.focus-matrix th,.focus-matrix td{text-align:left;padding:10px;min-width:150px;border:1px solid #d7e4ea;vertical-align:top}.focus-matrix thead{background:#edf4f7}.focus-structure{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}.focus-group{border:1px solid #d7e4ea;border-top:4px solid #176274;border-radius:8px;padding:10px 15px;background:#f3f8fa}.focus-group>.focus-tile:first-child{color:#176274;font-size:18px}.focus-event{display:grid;grid-template-columns:110px minmax(0,1fr);gap:15px;padding:10px 0;border-bottom:1px solid #d7e4ea}.focus-event time{font-size:13px;color:#607887;padding-top:6px}.focus-status{font-size:11px;font-weight:600;color:#176274;background:#e8f2f5;border-radius:4px;padding:3px 7px}.focus-gaps>summary{cursor:pointer;font-weight:600}.focus-chart>.focus-evidence{border-top:1px solid #d7e4ea;margin-top:12px}
@media print{.focus-theses,.focus-structure{display:block}.focus-thesis,.focus-group,.focus-event{break-inside:avoid;margin-bottom:10px}.focus-table-wrap{overflow:visible}.focus-matrix th,.focus-matrix td{min-width:0}.focus-bar-track{print-color-adjust:exact}.focus-bar-track>span{print-color-adjust:exact}}
</style>'''
