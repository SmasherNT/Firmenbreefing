"""Render the approved capability layout from reviewed, task-specific records."""
import html
from pathlib import Path


def esc(value):
    return html.escape(str(value), quote=True)


def compact(value, limit=48):
    value = " ".join(str(value).split())
    if len(value) <= limit:
        return value
    cut = value[:limit - 1]
    return (cut.rsplit(" ", 1)[0] if " " in cut else cut) + "…"


def display(row, criterion):
    """Keep profiles, quantitative metrics and ordinal evidence distinct."""
    state = row['cell_status']
    if state != 'bewertet':
        return dict(value=state, grade='', level=None, kind='missing' if state == 'nicht öffentlich belegt' else 'na')
    kind = criterion['display_type']
    if kind == 'Evidenzstufe':
        anchors = sorted(criterion['anchors'], key=float)
        value = row['value']
        key = str(int(value)) if isinstance(value, float) and value.is_integer() else str(value)
        # Color reflects position in this criterion's own rubric, not a new score.
        index = anchors.index(key)
        level = round(index * 4 / (len(anchors) - 1)) + 1 if len(anchors) > 1 else 5
        return dict(value=criterion['anchors'][key], grade=key, ceiling=anchors[-1], level=level, kind='evidence')
    if kind == 'Kennzahl':
        return dict(value=str(row['value']) + ' ' + criterion['unit'], grade=str(row['value']), level=None, kind='metric')
    return dict(value=row['value'], grade='', level=None, kind='profile')


def render(criteria, peers, cells, company, detail, source_counts, reference_id=None):
    """detail(row) supplies escaped reviewed content, never source-provided markup."""
    out = '<div id="briefing-capability-matrix" class="cm-root">'
    out += '<div class="cm-scroll"><table class="cm-matrix"><thead><tr><th>Unternehmen / Angebot</th>'
    for j, criterion in enumerate(criteria):
        out += '<th scope="col"><button type="button" class="cm-column" data-cm-column="' + str(j) + '" disabled aria-pressed="false" aria-label="' + esc(criterion['label'] + ' · alle Wettbewerber vergleichen') + '"><span>' + esc(criterion['label']) + ' <span class="cm-arrow" aria-hidden="true">↗</span></span><small>' + esc(criterion['display_type']) + '</small></button></th>'
    out += '</tr></thead><tbody>'
    records = []
    for i, peer in enumerate(peers):
        name, _, offer = peer['label'].partition(' · ')
        reference = peer['id'] == reference_id or name.casefold() == company.casefold()
        out += '<tr' + (' class="cm-reference"' if reference else '') + '><th scope="row"><span class="cm-actor">' + esc(name) + '</span>'
        if offer:
            out += '<small class="cm-system">' + esc(offer) + '</small>'
        if reference:
            out += '<span class="cm-reference-label" aria-label="Referenzunternehmen">Referenz</span>'
        out += '</th>'
        for j, criterion in enumerate(criteria):
            row = cells[peer['id'], criterion['id']]
            shown = display(row, criterion)
            title = row.get('headline') or compact(shown['value'])
            preview = row.get('preview', '')
            count = source_counts[row['id']]
            meta = 'Profil' if shown['kind'] == 'profile' else 'Kennzahl' if shown['kind'] == 'metric' else 'Evidenzlücke' if shown['kind'] == 'missing' else 'Nicht anwendbar'
            cls = 'cm-cell cm-' + shown['kind'] + (' cm-s' + str(shown['level']) if shown['level'] else '')
            attrs = ' data-cm-row="' + str(i) + '" data-cm-col="' + str(j) + '" data-cm-peer="' + esc(peer['id']) + '" data-cm-criterion="' + esc(criterion['id']) + '" data-cm-record="cm-eval-' + esc(row['id']) + '"'
            accessible = peer['label'] + ' · ' + criterion['label'] + ' · ' + (shown['grade'] + ' / ' + shown['ceiling'] + ' · ' if shown['kind'] == 'evidence' else '') + shown['value'] + ' · Details'
            out += '<td><a class="' + cls + '" href="#cm-eval-' + esc(row['id']) + '"' + attrs + ' data-cm-kind="' + shown['kind'] + '" aria-pressed="false" aria-label="' + esc(accessible) + '" title="' + esc(shown['value']) + '"><span class="cm-cell-top">'
            if shown['kind'] == 'evidence':
                out += '<span class="cm-score">' + esc(shown['grade']) + '<small> / ' + esc(shown['ceiling']) + '</small></span>'
            else:
                out += '<span class="cm-kind">' + meta + '</span>'
            if count:
                out += '<span class="cm-count">' + str(count) + (' Quelle' if count == 1 else ' Quellen') + '</span>'
            out += '</span><span class="cm-cell-title">' + esc(title) + '</span>'
            if preview:
                out += '<span class="cm-cell-preview">' + esc(preview) + '</span>'
            out += '</a></td>'
            outcome = '<div class="cm-outcome">'
            if shown['kind'] == 'evidence':
                outcome += '<span class="cm-outcome-grade">Evidenzstufe ' + esc(shown['grade']) + ' / ' + esc(shown['ceiling']) + '</span>'
            outcome += '<p class="cm-full-value">' + esc(shown['value']) + '</p></div>'
            records.append('<details class="cm-record" id="cm-eval-' + esc(row['id']) + '"' + ' data-cm-row="' + str(i) + '" data-cm-col="' + str(j) + '" data-cm-name="' + esc(name) + '" data-cm-offer="' + esc(offer) + '" data-cm-title="' + esc(peer['label'] + ' · ' + criterion['label']) + '" data-cm-source-count="' + str(count) + '"><summary>' + esc(peer['label'] + ' · ' + criterion['label']) + '</summary><div class="cm-record-body">' + outcome + detail(row) + '</div></details>')
        out += '</tr>'
    out += '</tbody></table></div><div class="cm-legend"><span><i class="cm-key-evidence"></i>Evidenzstufen nach Kriterienmaßstab</span><span><i class="cm-key-profile"></i>Profil / Kennzahl ohne Rangwertung</span><span><i class="cm-key-missing"></i>Öffentliche Evidenz fehlt</span><span>Kein Gesamtranking</span></div>'
    out += '<details class="cm-method"><summary>Kriterien und Maßstab</summary><div class="cm-method-grid">'
    for criterion in criteria:
        out += '<div><h4>' + esc(criterion['label']) + '</h4><p>' + esc(criterion['question']) + '</p><p>' + esc(criterion['evidence_required']) + '</p>'
        if criterion.get('conditions'):
            out += '<p>' + esc(criterion['conditions']) + '</p>'
        if criterion.get('anchors'):
            out += '<dl>' + ''.join('<dt>' + esc(k) + '</dt><dd>' + esc(v) + '</dd>' for k, v in sorted(criterion['anchors'].items(), key=lambda p: float(p[0]))) + '</dl>'
        out += '</div>'
    out += '</div></details><section class="cm-detail" aria-live="polite" hidden></section>'
    out += '<div class="cm-fallback"><h3>Vollständige Bewertungen &amp; Originalquellen</h3>' + ''.join(records) + '</div></div>'
    assets = Path(__file__).resolve().parents[1] / 'references/templates'
    return '<style>' + (assets / 'capability.css').read_text(encoding='utf-8') + '</style>' + out + '<script>' + (assets / 'capability.js').read_text(encoding='utf-8') + '</script>'
