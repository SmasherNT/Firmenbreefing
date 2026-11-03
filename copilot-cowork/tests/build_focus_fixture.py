"""Build a synthetic offline browser fixture, never a real company briefing."""
from pathlib import Path
import sys
import test_render_briefing as render
from test_focus import neutral_page


def build(target):
    bundle = render.bundle()
    pages = [neutral_page(), neutral_page('drohnen')]
    bundle['manifest']['focus_pages'] = [{k:p[k] for k in ('id','label','briefing_type')} for p in pages]
    bundle['manifest']['person'] = 'Synthetischer Gesprächspartner'
    for focus in pages:
        bundle['facts']['claims'].append({**bundle['facts']['claims'][0], 'id':'F_' + focus['id'] + '_1'})
        bundle['facts']['module_views'].append(dict(role='focus:' + focus['id'], focus_pages=[focus], gaps=[], coverage=[]))
    render.refresh_basis(bundle)
    Path(target).write_text(render.RENDER.build(**render.facts_only(bundle)), encoding='utf-8')


if __name__ == '__main__':
    build(sys.argv[1])
