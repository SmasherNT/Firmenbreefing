"""Compact module facts/insights from reviewed positioning claims."""
import html
from pathlib import Path

MODULES = ('portfolio', 'cluster', 'market')
SECTION = 'module_insights'


def request(manifest):
    modules = [m for m in MODULES if m in manifest.get('selected_roles', [])]
    if not modules:
        raise ValueError('module insights require portfolio, cluster or market')
    return dict(schema_version=1, modules=modules)


def validate(rows, gaps, delegated, manifest, claims):
    """Only card texts are factual/analytical; gap reasons stay in review input."""
    errors = []
    cards = [r for r in rows if r.get('type') == 'module_insight' or r.get('section') == SECTION]
    if delegated is None:
        return ['module insights require delegated context'] if cards or gaps else []
    if delegated != request(manifest):
        return ['module insights context differs from selected modules']
    targets = delegated['modules']
    groups = {m: [] for m in targets}
    for row in cards:
        cid = str(row.get('id'))
        if row.get('type') != 'module_insight' or row.get('section') != SECTION:
            errors.append(cid + ': module_insight requires module_insights section')
        module = row.get('module')
        if not isinstance(module, str) or module not in groups:
            errors.append(cid + ': unknown/unselected insight module')
            continue
        groups[module].append(row)
        for field, limit in (('headline', 72), ('fact_text', 180), ('statement', 180)):
            value = row.get(field)
            if not isinstance(value, str) or not value.strip() or len(value) > limit:
                errors.append(cid + ': ' + field + ' required, at most ' + str(limit) + ' characters')
        order = row.get('display_order')
        if type(order) is not int or order < 1:
            errors.append(cid + ': module display_order must be a positive integer')
        refs = row.get('fact_claim_ids')
        deps = row.get('depends_on')
        if not isinstance(refs, list) or not refs or any(not isinstance(c, str) or c not in claims for c in refs):
            errors.append(cid + ': fact_claim_ids must reference facts directly')
        elif len(set(refs)) != len(refs) or not isinstance(deps, list) or any(c not in deps for c in refs):
            errors.append(cid + ': fact_claim_ids must be unique and included in depends_on')
        if 'score' in row or 'value' in row:
            errors.append(cid + ': module cards are not scores or ratings')
    gap_modules = set()
    if not isinstance(gaps, list):
        errors.append('module_insight_gaps must be a list')
        gaps = []
    for gap in gaps:
        if not isinstance(gap, dict) or not isinstance(gap.get('module'), str) or gap['module'] not in groups:
            errors.append('module insight gap must reference a selected module')
            continue
        module = gap['module']
        if module in gap_modules:
            errors.append(module + ': duplicate module insight gap')
        gap_modules.add(module)
        if not isinstance(gap.get('reason'), str) or not gap['reason'].strip():
            errors.append(module + ': gap reason required for reviewer')
    for module, group in groups.items():
        if group and module in gap_modules:
            errors.append(module + ': cards and gap cannot coexist')
        if not group and module not in gap_modules:
            errors.append(module + ': provide 1–3 cards or an explicit insight gap')
        if len(group) > 3:
            errors.append(module + ': at most three module insights')
        orders = [r.get('display_order') for r in group]
        if any(type(n) is not int for n in orders) or set(orders) != set(range(1, len(group) + 1)):
            errors.append(module + ': module order must be unique and contiguous from 1')
    return errors


def render(module, rows, requested, detail):
    if not requested or module not in requested['modules']:
        return ''
    esc = lambda value: html.escape(str(value), quote=True)
    cards = sorted((r for r in rows if r.get('type') == 'module_insight' and r.get('module') == module), key=lambda r: r['display_order'])
    out = '<div class="module-insights" id="insights-' + module + '" data-insight-module="' + module + '"><h3>Keyfacts &amp; Insights</h3>'
    if not cards:
        # This reports the supplied approved-card state, not a company weakness.
        out += '<p class="mi-empty">Für dieses Modul liegen keine freigegebenen zusätzlichen Keyfacts &amp; Insights vor.</p>'
    else:
        out += '<div class="mi-grid" data-count="' + str(len(cards)) + '">'
        for row in cards:
            out += '<article class="mi-card"><h4>' + esc(row['headline']) + '</h4><div class="mi-fact"><span class="mi-label">Fakt</span><p>' + esc(row['fact_text']) + '</p></div><div class="mi-insight"><span class="mi-label">Insight · Analysteninterpretation</span><p>' + esc(row['statement']) + '</p></div><details class="mi-detail"><summary>Faktenbasis &amp; Einordnung</summary><div class="mi-detail-body">' + detail(row) + '</div></details></article>'
        out += '</div>'
    return out + '</div>'


def css():
    return '<style>' + (Path(__file__).resolve().parents[1]/'references/templates/module-insights.css').read_text(encoding='utf-8') + '</style>'
