"""Episode 1 storyboard: key frames drawn from the real data (not renders of the final page; composition + data + what
moves). Writes preprod/storyboard/sb-NN.png (portrait pages for a phone, 4 frames each) and preprod/storyboard.md.

    python3 episodes/ep001/preprod/storyboard.py
"""
import csv
import json
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')
T = json.load(open(os.path.join(EP, '..', '..', 'genre-spec', 'channel', 'visual-tokens.json')))['colors']
BG, INK, MUT, ACC, WARN, POS, NEG, GRID = (T[k] for k in ('bg', 'ink', 'ink-muted', 'accent', 'warn', 'positive', 'negative', 'grid'))
plt.rcParams.update({'font.family': 'DejaVu Sans', 'text.color': INK, 'axes.edgecolor': MUT, 'axes.labelcolor': MUT, 'xtick.color': MUT, 'ytick.color': MUT})

C = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']}
M = json.load(open(os.path.join(EP, 'out', 'model.json')))
W = [(r['date'], float(r['rate'])) for r in csv.DictReader(open(os.path.join(EP, 'data', 'normalized', 'mortgage30_weekly.csv')))]
HM = list(csv.DictReader(open(os.path.join(EP, 'data', 'normalized', 'hmda_refi_costs.csv'))))
d = lambda k: C[k]['display']
yr = lambda s: int(s[:4]) + (int(s[5:7]) - 1) / 12 + (int(s[8:10]) if len(s) > 8 else 15) / 365
sys_path = os.path.join(EP, 'model')
import sys  # noqa: E402
sys.path.insert(0, sys_path)
import refi  # noqa: E402


def frame(ax, title=None):
    ax.set_facecolor(BG)
    ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis('off')
    ax.add_patch(Rectangle((0.8, 0.45), 14.4, 8.1, fill=False, ls=':', lw=0.6, ec=GRID))  # 90% safe area
    if title:
        ax.text(10.67, 6.0, title, ha='center', va='center', fontsize=17, fontweight='bold', color=INK)


def chart_in(ax, rect):
    fig = ax.figure
    bb = ax.get_position()
    x0, y0, w, h = rect
    a = fig.add_axes([bb.x0 + bb.width * x0 / 16, bb.y0 + bb.height * y0 / 9, bb.width * w / 16, bb.height * h / 9])
    a.set_facecolor(BG)
    for s in ('top', 'right'):
        a.spines[s].set_visible(False)
    a.tick_params(labelsize=7)
    return a


def badge(ax, x, y):
    ax.text(x, y, 'ILLUSTRATIVE', fontsize=6.5, fontweight='bold', color=BG, bbox=dict(boxstyle='round,pad=0.25', fc=WARN, ec='none'))


def f_bars(ax):
    frame(ax)
    for x, h, c, lab in ((5, 5.0, MUT, 'old payment'), (8, 4.1, ACC, 'new payment')):
        ax.add_patch(Rectangle((x, 1.2), 1.8, h, fc=c, ec='none'))
        ax.text(x + 0.9, 0.8, lab, ha='center', fontsize=8, color=MUT)
    ax.annotate('', (8.9, 5.3), (8.9, 6.2), arrowprops=dict(arrowstyle='->', color=POS))
    ax.text(10.67, 7.2, '(no words for the first 1.5 s)', ha='center', fontsize=8, color=MUT, style='italic')


def f_bill(ax):
    frame(ax)
    ax.add_patch(Rectangle((5, 1.2), 1.8, 5.0, fc=MUT, ec='none')); ax.add_patch(Rectangle((8, 1.2), 1.8, 4.1, fc=ACC, ec='none'))
    for i in range(6):
        ax.add_patch(FancyBboxPatch((11.2, 1.2 + i * 0.45), 1.8, 0.35, boxstyle='round,pad=0.02', fc=NEG, ec='none'))
    ax.text(12.1, 4.3, 'closing costs', ha='center', fontsize=8, color=INK)
    ax.text(12.1, 0.8, 'months: 0', ha='center', fontsize=9, color=INK)


def f_question(ax):
    frame(ax)
    ax.text(8, 5.4, 'How far do rates have to fall\nbefore a refinance pays for itself?', ha='center', va='center', fontsize=15, fontweight='bold')
    ax.add_patch(Rectangle((3, 2.3), 10, 0.25, fc=GRID, ec='none')); ax.text(8, 1.6, 'months: 0', ha='center', fontsize=9)


def f_ruler(ax, answer=False):
    frame(ax)
    ax.plot([2, 14], [4.2, 4.2], color=INK, lw=2)
    for i, v in enumerate([0, 0.5, 1, 1.5, 2]):
        x = 2 + 6 * v
        ax.plot([x, x], [4.0, 4.4], color=INK, lw=1.5); ax.text(x, 3.4, f'{v:g}', ha='center', fontsize=9)
    ax.text(8, 2.7, 'rate cut (percentage points)', ha='center', fontsize=8, color=MUT)
    for k in range(13):
        ax.plot(2.3 + k * 0.9, 1.4, 'o', ms=3, color=MUT)
    ax.text(8, 0.85, f"{d('n_eps')} drops since {d('y1971')}", ha='center', fontsize=7, color=MUT)
    if answer:
        x = 2 + 6 * float(C['sp36_mid']['value'])
        ax.plot([x], [4.9], marker='v', ms=12, color=WARN)
        ax.text(x, 5.6, d('sp36_mid') + ' points', ha='center', fontsize=13, fontweight='bold', color=WARN)
    else:  # the rehook does not give the answer away: the marker sweeps the whole ruler, one "?" over it
        ax.plot([2, 14], [4.9, 4.9], color=WARN, lw=1, ls=':')
        ax.text(8, 5.4, '?', ha='center', fontsize=22, fontweight='bold', color=WARN)
        x = 8
    ax.text(x, 6.6, f"pays back within {d('hold36')} months", ha='center', fontsize=9, color=INK)
    badge(ax, x + 2.6, 6.45)


def f_line(ax, mark=None):
    frame(ax)
    a = chart_in(ax, (1.4, 1.2, 13.4, 5.8))
    a.plot([yr(x[0]) for x in W], [x[1] for x in W], color=ACC, lw=1)
    a.set_ylim(0, 20); a.set_xlim(1971, 2027)
    a.set_xticks([1971, 2026]); a.set_yticks([])
    a.spines['left'].set_visible(False)
    if mark == 'peak':
        a.plot([yr('1981-10-09')], [18.63], 'o', color=WARN); a.text(1983, 18.3, f"{d('peak')} in {d('y1981')}", fontsize=9, color=INK)
    if mark == 'episodes':
        for e in M['history']:
            a.axvspan(yr(e['peak'] + '-15'), yr(e['trough'] + '-15'), color=WARN, alpha=0.18, lw=0)
        a.text(1972, 18.5, f"{d('n_eps')} drops of at least 1 point", fontsize=9, color=INK)


def f_hist(ax):
    frame(ax)
    lo, med, hi = (float(C[k]['value']) for k in ('cost_p25', 'cost_med', 'cost_p75'))
    a = chart_in(ax, (2, 2.2, 12, 3.2))
    a.barh([0], [hi - lo], left=[lo], color=GRID, height=0.5); a.plot([med, med], [-0.35, 0.35], color=INK, lw=3)
    a.set_xlim(0, 12000); a.set_yticks([]); a.set_xticks([])
    a.spines['left'].set_visible(False)
    ax.text(2 + 12 * med / 12000, 6.2, d('cost_med'), ha='center', fontsize=15, fontweight='bold')
    ax.text(2 + 12 * lo / 12000, 1.6, d('cost_p25'), ha='center', fontsize=9); ax.text(2 + 12 * hi / 12000, 1.6, d('cost_p75'), ha='center', fontsize=9)
    ax.text(8, 7.3, f"median total loan costs, {d('y2025')}, nominal", ha='center', fontsize=8, color=MUT)


def f_bands(ax):
    frame(ax)
    rows = [r for r in HM if r['year'] == str(C['y2025']['value']) and r['purpose'].startswith('refinance (31)') and r['loanSize'] != 'all sizes']
    order = ['under $150k', '$150k-$300k', '$300k-$450k', '$450k-$750k', '$750k and over']
    rows = sorted(rows, key=lambda r: order.index(r['loanSize']))
    for i, r in enumerate(rows):
        v = float(r['cost_p50_pct'])
        c = WARN if i == 0 else ACC if i == 4 else MUT
        ax.add_patch(Rectangle((2 + i * 2.5, 1.3), 1.6, v * 1.1, fc=c, ec='none', hatch='//' if i == 4 else None))
        ax.text(2.8 + i * 2.5, 1.3 + v * 1.1 + 0.25, f'{v:.1f}%', ha='center', fontsize=9)
        ax.text(2.8 + i * 2.5, 0.8, r['loanSize'].replace('$', r'\$'), ha='center', fontsize=6.5, color=MUT)
    ax.text(8, 7.6, 'closing costs as a share of the loan', ha='center', fontsize=9, color=INK)


def f_curve(ax, cross=False):
    frame(ax)
    a = chart_in(ax, (1.8, 1.3, 12.6, 6.0))
    L, R0, CO = M['loan'], M['oldRate'], M['cost']
    xs = [i / 100 for i in range(10, 201)]
    a.plot(xs, [refi.refi(L, R0, 360, R0 - x, CO)['breakEvenMonths'] for x in xs], color=INK, lw=2)
    for k in ('025', '05', '10', '20'):
        a.plot([C['s' + k]['value']], [C['be' + k]['value']], 'o', color=INK)
        a.text(C['s' + k]['value'] + 0.04, C['be' + k]['value'] + 4, str(C['be' + k]['value']), fontsize=8, color=INK)
    a.set_ylim(0, 120); a.set_xlim(0, 2.05); a.set_xticks([0.25, 0.5, 1, 2]); a.set_yticks([])
    a.set_xlabel('rate cut (points)', fontsize=7); a.spines['left'].set_visible(False)
    if cross:
        a.axhline(36, color=WARN, lw=1, ls='--')
        for key, col, ls in (('small', WARN, '-'), ('big', ACC, '--')):
            band = {'small': 'under $150k', 'big': '$750k and over'}[key]
            r = next(x for x in HM if x['year'] == str(C['y2025']['value']) and x['purpose'].startswith('refinance (31)') and x['loanSize'] == band)
            a.plot(xs, [refi.refi(float(r['loan_p50_usd']), R0, 360, R0 - x, float(r['cost_p50_usd']))['breakEvenMonths'] or 999 for x in xs], color=col, lw=1.5, ls=ls)
        badge(ax, 11.8, 3.2)


def f_episodes(ax):
    frame(ax)
    rows = [(e['peak'][:4], next(c for c in e['cases'] if c['spread'] == 1.0)) for e in M['history']]
    for i, (y, c) in enumerate(rows):
        h = c['breakEvenMonths'] * 0.22
        ax.add_patch(Rectangle((1.4 + i * 1.03, 1.4), 0.7, h, fc=MUT if c['costIllustrative'] else ACC, ec='none'))
        if c['beforeBreakEvenAnotherDrop']:
            ax.plot(1.75 + i * 1.03, 1.4 + h + 0.35, 'v', color=NEG, ms=6)
        ax.text(1.75 + i * 1.03, 0.9, y, ha='center', fontsize=6, color=MUT, rotation=0)
    ax.text(8, 7.6, 'months to break even at a 1-point cut, every drop', ha='center', fontsize=9)
    ax.text(8, 7.0, 'red mark: the next full point came before break-even', ha='center', fontsize=7, color=NEG)
    badge(ax, 1.4, 6.3)


def f_card(ax):
    frame(ax)
    ax.text(1.3, 7.4, 'Method', fontsize=14, fontweight='bold')
    for i, t in enumerate(['Rates: Freddie Mac PMMS via FRED (MORTGAGE30US), weekly 1971-2026', 'Check: Optimal Blue OBMMIC30YF since 2017',
                           'Costs: HMDA 2018-2025, originated refinances, first lien, 360 months', 'Cash closing costs; no taxes; no discounting']):
        ax.text(1.3, 6.2 - i * 0.9, t, fontsize=8.5)


def f_end(ax):
    frame(ax)
    ax.add_patch(Rectangle((9.3, 3.2), 5.2, 2.9, fill=False, ec=MUT, ls='--')); ax.text(11.9, 4.6, 'end screen', ha='center', fontsize=8, color=MUT)
    ax.add_patch(Rectangle((1.5, 3.2), 5.2, 2.9, fill=False, ec=MUT, ls='--')); ax.text(4.1, 4.6, 'end screen', ha='center', fontsize=8, color=MUT)
    ax.text(8, 1.6, 'sources in the description', ha='center', fontsize=9)


FRAMES = [
    ('co-bars', 'Cold open: picture first. Old vs new monthly payment; the new bar drops.', f_bars),
    ('co-bill', 'The price arrives: the closing-cost bill lands; a month counter waits at 0.', f_bill),
    ('co-question', 'Open question (answered in act 3 on the same ruler).', f_question),
    ('a1-rehook', 'Rehook 0:30-0:45, ONE object: the rate-cut ruler; a marker sweeps it and one "?" hangs over it (the answer is not placed until act 3). 13 ticks = every drop since 1971.', lambda a: f_ruler(a, False)),
    ('a1-peak', 'Act 1: the rate line draws (line sound); the peak dot lands on "18.63%" (dot sound).', lambda a: f_line(a, 'peak')),
    ('a1-median', 'The bill: median total loan costs and the middle half (HMDA 2025, rate-and-term refinances).', f_hist),
    ('a1-small', 'Turn: cost as a share of the loan by size band. SMALL (amber, solid, left) vs LARGE (blue, hatched/dashed, right).', f_bands),
    ('a2-s025', 'Act 2: break-even months against the rate cut; points land as each cut is named (bar + dot sounds).', lambda a: f_curve(a, False)),
    ('a2-mid', 'Turn 2: the 36-month line (ILLUSTRATIVE) crosses the MEDIAN, SMALL and LARGE curves at different cuts.', lambda a: f_curve(a, True)),
    ('a3-all', 'Act 3: every drop of at least 1 point since 1971, shaded on the rate line.', lambda a: f_line(a, 'episodes')),
    ('a3-range', 'All 13 cases (DX-H6): months to break even at a 1-point cut; grey = fixed pre-HMDA cost share (ILLUSTRATIVE), blue = HMDA year; red marks where the next point came first.', f_episodes),
    ('a3-answer2', 'Answer: the rehook ruler returns; the marker lands on the answer.', lambda a: f_ruler(a, True)),
    ('m-rates', 'Method card (static, readable).', f_card),
    ('o-sources', 'Outro >= 20 s with end-screen space.', f_end),
]


def main():
    out = os.path.join(HERE, 'storyboard')
    os.makedirs(out, exist_ok=True)
    md = ['# Episode 1 — storyboard (key frames)', '', 'Drawn from the data by `preprod/storyboard.py`: composition, numbers and what moves; not the final render. '
          'Dotted rectangle = 90% safe area. Full shot-by-shot list: `shotlist.json` / `shotlist.md`.', '']
    per = 3
    fh = 0.92 * 9 / 16 * 10.8 / 19.2
    for p in range(0, len(FRAMES), per):
        chunk = FRAMES[p:p + per]
        fig = plt.figure(figsize=(10.8, 19.2), dpi=100, facecolor=BG)
        for i, (sc, cap, fn) in enumerate(chunk):
            top = 1 - i / per - 0.01
            ax = fig.add_axes([0.04, top - 0.03 - fh, 0.92, fh])
            fn(ax)
            fig.text(0.04, top - 0.02, f'{p + i + 1:02d}  {sc}', fontsize=12, fontweight='bold', color=WARN, va='center')
            fig.text(0.04, top - 0.035 - fh, cap, fontsize=10, color=INK, va='top', wrap=True)
        name = f'sb-{p // per + 1:02d}.png'
        fig.savefig(os.path.join(out, name), facecolor=BG)
        plt.close(fig)
        md.append(f'![{name}](storyboard/{name})')
        md += [f'- **{p + i + 1:02d} `{sc}`** {cap}' for i, (sc, cap, _) in enumerate(chunk)] + ['']
    open(os.path.join(HERE, 'storyboard.md'), 'w').write('\n'.join(md) + '\n')
    print('pages', (len(FRAMES) + per - 1) // per)


if __name__ == '__main__':
    main()
