"""Episode 1 storyboard (Stage 4b, script v2): one key frame per scene, drawn from the real data (composition, numbers, what
moves; not the final render). Writes preprod/storyboard/<scene>.png (1280x720), preprod/storyboard/contact-sheet.png and
preprod/storyboard.md. The animatic (preprod/animatic.py) uses the same frame functions.

    python3 episodes/ep001/preprod/storyboard.py

Nora = median (green circle, centre), Walt = small (amber triangle, left), Anjali = large (red square, right); rate line accent
blue without markers; names in ink next to the marker; ILLUSTRATIVE badge with each character's first number.
"""
import csv
import json
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(EP, 'model'))
import refi  # noqa: E402

TOK = json.load(open(os.path.join(EP, 'design', 'tokens.json')))
T = TOK['colors']
BG, INK, MUT, ACC, WARN, GRID, SURF = T['bg'], T['text'], T['muted'], T['accent'], T['warn'], T['grid'], T['surface']
CH = {'median': ('Nora', TOK['series']['median'], 'o'), 'small': ('Walt', TOK['series']['small'], '^'), 'large': ('Anjali', TOK['series']['large'], 's')}
plt.rcParams.update({'font.family': 'DejaVu Sans', 'text.color': INK, 'axes.edgecolor': MUT, 'axes.labelcolor': MUT, 'xtick.color': MUT, 'ytick.color': MUT})
C = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']}
M = json.load(open(os.path.join(EP, 'out', 'model.json')))
W = [(r['date'], float(r['rate'])) for r in csv.DictReader(open(os.path.join(EP, 'data', 'normalized', 'mortgage30_weekly.csv')))]
SC = M['scenario']
d = lambda k: C[k]['display'].replace('$', r'\$')
yr = lambda s: int(s[:4]) + (int(s[5:7]) - 1) / 12 + (int(s[8:10]) if len(s) > 8 else 15) / 365


def frame(ax):
    ax.set_facecolor(BG); ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis('off')
    ax.add_patch(Rectangle((0.8, 0.45), 14.4, 8.1, fill=False, ls=':', lw=0.6, ec=GRID))


def sub(ax, rect):
    fig, bb = ax.figure, ax.get_position()
    x0, y0, w, h = rect
    a = fig.add_axes([bb.x0 + bb.width * x0 / 16, bb.y0 + bb.height * y0 / 9, bb.width * w / 16, bb.height * h / 9])
    a.set_facecolor(BG)
    for s in ('top', 'right'):
        a.spines[s].set_visible(False)
    a.tick_params(labelsize=8)
    return a


def badge(ax, x, y):
    ax.text(x, y, 'ILLUSTRATIVE', fontsize=7, fontweight='bold', color=BG, bbox=dict(boxstyle='round,pad=0.25', fc=WARN, ec='none'))


def title(ax, t, y=8.0):
    ax.text(8, y, t, ha='center', fontsize=13, fontweight='bold', color=INK)


def rate_line(ax, start, end, marks=(), label_peak=False, one_point=False, rect=(1.4, 1.2, 13.2, 6.2)):
    a = sub(ax, rect)
    pts = [(yr(x[0]), x[1]) for x in W if start <= x[0] <= end]
    a.plot([p[0] for p in pts], [p[1] for p in pts], color=ACC, lw=1.8)
    lo, hi = min(p[1] for p in pts), max(p[1] for p in pts)
    a.set_ylim(lo - 0.4, hi + 0.6)
    a.set_ylabel('30-year fixed rate, %', fontsize=8)
    if label_peak:
        p = C['peak2023']
        a.annotate(f"{p['display']}  highest since {C['peak2023_since']['display']}", (yr(p['date']), p['value']), (yr(p['date']) - 6, p['value'] + 0.3), fontsize=9, color=INK,
                   arrowprops=dict(arrowstyle='-', color=MUT, lw=0.6))
    if one_point:
        a.axhline(SC['oldRate'] - 1, color=MUT, lw=0.8, ls=':'); a.text(pts[0][0], SC['oldRate'] - 0.93, '1-point line', fontsize=8, color=MUT)
    for when, val, txt, key in marks:
        col, shp = (CH[key][1], CH[key][2]) if key else (INK, 'o')
        a.plot([yr(when)], [val], shp, color=col, ms=9)
        a.text(yr(when), val + 0.18, txt, fontsize=9, color=INK, ha='center')
    return a


def letter(ax, lines, hi=None, x=5.2, w=5.6):
    ax.add_patch(FancyBboxPatch((x, 1.0), w, 6.8, boxstyle='round,pad=0.05', fc='#e9e6dd', ec='none'))
    ax.text(x + 0.4, 7.2, 'Your refinance offer', fontsize=12, fontweight='bold', color=BG)
    for i, (k, v) in enumerate(lines):
        y = 6.2 - i * 0.9
        if hi == i:
            ax.add_patch(Rectangle((x + 0.2, y - 0.3), w - 0.4, 0.75, fc=WARN, alpha=0.35, ec='none'))
        ax.text(x + 0.4, y, k, fontsize=11, color=BG); ax.text(x + w - 0.4, y, v, fontsize=11, color=BG, ha='right', fontweight='bold')


OFFER = lambda: [('Current rate', d('r_old')), ('New rate', d('r_today')), ('Term', '30 years'), ('', ''), ('Loan costs', d('cost_median'))]


def ruler(ax, markers=(), cand=None, extra=''):
    ax.plot([1.8, 14.2], [4.0, 4.0], color=INK, lw=2)
    for v in (0, 0.25, 0.5, 0.75, 1, 1.25, 1.5):
        x = 1.8 + 8 * v; ax.plot([x, x], [3.8, 4.2], color=INK, lw=1.2); ax.text(x, 3.3, f'{v:g}', ha='center', fontsize=9)
    ax.plot([9.8, 9.8], [2.9, 6.6], color=MUT, lw=1, ls=':'); ax.text(9.8, 6.8, '1-point line', ha='center', fontsize=9, color=MUT)
    ax.text(8, 2.4, 'rate drop (percentage points) that pays the bill back within three years', ha='center', fontsize=9, color=MUT)
    for i, (key, v) in enumerate(markers):
        nm, col, shp = CH[key]
        x = 1.8 + 8 * v
        ax.plot([x], [4.6], shp, color=col, ms=14)
        ax.text(x, 5.2 + 0.55 * (i % 2), f'{nm}  {v:g}', ha='center', fontsize=11, color=INK, fontweight='bold')
    if cand is not None:
        x = 1.8 + 8 * cand; ax.plot([x], [4.6], 'o', color=CH['median'][1], ms=14, alpha=0.45)
    if extra:
        ax.text(8, 7.8, extra, ha='center', fontsize=12, color=INK)
    if not markers and cand is None:
        for i, key in enumerate(('small', 'median', 'large')):
            ax.plot([0.9], [5.6 - i * 0.7], CH[key][2], color=CH[key][1], ms=12)


def blocks(ax, items, base=1.4, scale=None, gap=0.4, x0=2.0, w=1.6):
    mx = max(v for _, v, _ in items)
    sc = scale or 5.5 / mx
    x = x0
    for lab, v, col in items:
        ax.add_patch(Rectangle((x, base), w, v * sc, fc=col, ec='none'))
        ax.text(x + w / 2, base + v * sc + 0.2, lab, ha='center', fontsize=10, color=INK)
        x += w + gap


def balance(ax, key='median', upto=48, mark=None):
    c = M['characters'][key]; P, r0, k, r1 = c['loan'], SC['oldRate'], SC['paymentsMade'], SC['todayRate']
    ms = list(range(0, upto + 1))
    old = [refi.balance_after(P, r0, 360, k + m) / 1000 for m in ms]; new = [refi.balance_after(c['balance'], r1, 360, m) / 1000 for m in ms]
    a = sub(ax, (1.8, 1.3, 12.4, 6.0))
    a.plot(ms, old, color=MUT, lw=2, label='old loan: what she still owes'); a.plot(ms, new, color=ACC, lw=2, label='new loan: what she still owes')
    a.set_xlabel('months after refinancing', fontsize=8); a.set_ylabel('$ thousand', fontsize=8); a.legend(fontsize=8, frameon=False)
    if mark:
        a.fill_between(ms[:mark + 1], old[:mark + 1], new[:mark + 1], color=MUT, alpha=0.35, hatch='//')
        a.annotate(d('gap24'), (mark, (old[mark] + new[mark]) / 2), (mark + 5, new[mark] + 4), fontsize=11, color=INK, arrowprops=dict(arrowstyle='-', color=MUT))
    return a


def counter(ax, n, lab, sub_=''):
    ax.text(8, 5.0, str(n), ha='center', fontsize=64, fontweight='bold', color=INK)
    ax.text(8, 3.4, lab, ha='center', fontsize=13, color=MUT)
    if sub_:
        ax.text(8, 2.4, sub_, ha='center', fontsize=11, color=MUT)


def person(ax, key, lines):
    nm, col, shp = CH[key]
    x = {'small': 1.6, 'median': 5.9, 'large': 10.2}[key]
    ax.add_patch(FancyBboxPatch((x, 2.0), 4.2, 4.6, boxstyle='round,pad=0.1', fc=SURF, ec=col, lw=1.5))
    ax.plot([x + 0.5], [6.0], shp, color=col, ms=16); ax.text(x + 1.0, 5.85, nm, fontsize=15, fontweight='bold', color=INK)
    for i, l in enumerate(lines):
        ax.text(x + 0.4, 5.0 - i * 0.7, l, fontsize=11, color=INK)
    badge(ax, x + 0.3, 2.3)


def net_timeline(ax, key, years):
    nm, col, shp = CH[key]
    c = M['characters'][key]
    ax.plot([2, 14], [3.0, 3.0], color=INK, lw=1.5)
    for y in range(0, 8):
        x = 2 + 12 * y / 7; ax.plot([x, x], [2.8, 3.2], color=INK); ax.text(x, 2.3, f'year {y}', ha='center', fontsize=8, color=MUT)
    for y in years:
        v = c['net36'] if y == 3 else c['net84']
        x = 2 + 12 * y / 7
        h = v / 3000
        ax.add_patch(Rectangle((x - 0.35, 3.0 if h > 0 else 3.0 + h), 0.7, abs(h), fc=col if v > 0 else MUT, hatch=None if v > 0 else '//', ec='none'))
        ax.text(x, 3.0 + h + (0.3 if h > 0 else -0.5), ('+' if v > 0 else '-') + '\\$' + f'{abs(v):,.0f}', ha='center', fontsize=12, color=INK, fontweight='bold')
    ax.plot([1.4], [7.4], shp, color=col, ms=14); ax.text(1.9, 7.25, nm + ': ahead or behind after selling', fontsize=12, color=INK)


def textcard(ax, head, rows, size=10):
    ax.text(1.3, 7.6, head, fontsize=15, fontweight='bold')
    import textwrap
    y = 6.9
    for r in rows:
        for j, l in enumerate(textwrap.wrap(r, 105)):
            ax.text(1.3, y, l, fontsize=size); y -= 0.45
        y -= 0.25


def F(fn):
    def g(ax):
        frame(ax); fn(ax)
    return g


def f_houses(ax):
    for i in range(10):
        x = 1.6 + i * 1.3
        lit = i in (3, 6, 8)
        ax.add_patch(Rectangle((x, 3.0), 1.0, 1.0, fc=WARN if lit else SURF, ec=MUT))
        ax.plot([x, x + 0.5, x + 1.0], [4.0, 4.6, 4.0], color=WARN if lit else MUT)
    ax.text(8, 6.3, f"{C['purch23_words']['display']} home-purchase loans in 2023 at {C['ge7_threshold']['display']} or more", ha='center', fontsize=13)
    ax.text(8, 1.8, 'HMDA 2023, 30-year first-lien purchase loans', ha='center', fontsize=9, color=MUT)


def f_payment(ax):
    c = M['characters']['median']; old = refi.payment(c['loan'], SC['oldRate'], 360); new = old - c['monthlySavings']
    blocks(ax, [(f'old \\${old:,.0f}', old, MUT), (f'new \\${new:,.0f}', new, ACC), (d('sav_median') + ' less', c['monthlySavings'], CH['median'][1])], x0=4.0, w=2.2)
    ax.text(8, 7.8, f"cut {C['cut_today']['display']} percentage point  ·  percentage point ≠ points", ha='center', fontsize=11, color=MUT)


FR = {
    'S01': F(lambda ax: rate_line(ax, '2000-01-01', '2023-12-31', label_peak=True, one_point=True)),
    'S02': F(lambda ax: (letter(ax, OFFER(), hi=4), ax.text(11.2, 1.3, 'nominal $', fontsize=9, color=MUT), badge(ax, 11.2, 2.0))),
    'S03': F(lambda ax: ax.text(8, 4.4, 'CRUX', ha='center', fontsize=54, fontweight='bold', color=INK)),
    'S04': F(lambda ax: ruler(ax, extra='One decision, three households: the drop that pays the bill back within three years')),
    'S05': F(lambda ax: rate_line(ax, '2019-06-01', '2023-12-31', marks=[(C['low_date']['value'], C['low']['value'], f"{C['low']['display']}  week ending January 7, 2021", None)])),
    'S06': F(f_houses),
    'S07': F(lambda ax: (rate_line(ax, '2022-01-01', '2023-12-31', marks=[('2023-10-15', SC['oldRate'], f"Nora {d('r_old')}  ·  {d('loan_median')}", 'median')]), badge(ax, 12.0, 7.9))),
    'S08': F(lambda ax: rate_line(ax, '2023-06-01', SC['todayWeek'], marks=[('2023-10-15', SC['oldRate'], f"Nora {d('r_old')}", 'median'),
                                                                          (SC['todayWeek'], SC['todayRate'], f"week ending September 24, 2026: {d('r_today')}", None)])),
    'S09': F(f_payment),
    'S10': F(lambda ax: (blocks(ax, [('bill ' + d('cost_median'), C['cost_median']['value'], MUT), (d('sav_median') + ' a month', C['sav_median']['value'], CH['median'][1])], x0=5.0, w=2.6),
                         ax.text(8, 8.0, f"real 2025 medians from {C['n31_approx']['display']} refinances", ha='center', fontsize=11, color=MUT))),
    'S11': F(lambda ax: (letter(ax, OFFER(), x=5.6, w=4.8), [ax.add_patch(Rectangle((x, 3.0), 3.4, 2.4, fill=False, ec=MUT, ls='--')) for x in (1.2, 11.4)],
                         ax.text(2.9, 4.1, '?', ha='center', fontsize=26, color=MUT), ax.text(13.1, 4.1, '?', ha='center', fontsize=26, color=MUT))),
    'S12': F(lambda ax: (ax.plot([8, 8], [1, 8], color=GRID), ax.plot([1.5, 7.0], [5.5, 5.5], color=MUT, ls=':'), ax.text(4.2, 5.8, '1-point line (test value)', ha='center', fontsize=10, color=MUT),
                         ax.plot([4.2], [4.3], 'o', color=CH['median'][1], ms=14), ax.text(4.2, 3.5, f"Nora: {C['cut_today']['display']}", ha='center', fontsize=11),
                         ax.text(12, 5.0, '24', ha='center', fontsize=54, fontweight='bold'), ax.text(12, 3.6, d('cost_median') + ' / ' + d('sav_median') + ' = months', ha='center', fontsize=11, color=MUT))),
    'S13': F(lambda ax: letter(ax, OFFER()[:3] + [('? ? ?', '')] + OFFER()[4:], hi=3)),
    'S14': F(lambda ax: (blocks(ax, [(f'{m}', C['sav_median']['value'] * m, CH['median'][1]) for m in (1, 6, 12, 18, 24)], scale=5.5 / C['cost_median']['value'], x0=2.5, w=1.4, gap=0.6),
                         ax.axhline(1.4 + 5.5, xmin=0.12, xmax=0.9, color=MUT, lw=1.2), ax.text(14.2, 7.0, 'bill ' + d('cost_median'), fontsize=10, color=MUT),
                         ax.text(8, 0.8, 'months of savings stacked', ha='center', fontsize=10, color=MUT))),
    'S15': F(lambda ax: (balance(ax), ax.text(8, 8.1, f"{C['k35']['display']} payments made; a new loan restarts the {C['term30']['display']}-year clock", ha='center', fontsize=11))),
    'S16': F(lambda ax: balance(ax, mark=24)),
    'S17': F(lambda ax: counter(ax, C['be_bal_median']['display'], 'months, with the gap counted', 'not 24')),
    'S18': F(lambda ax: counter(ax, C['be_simple_025']['display'], 'months by division, at a quarter-point drop')),
    'S19': F(lambda ax: counter(ax, '—', 'with the balance counted: not before the old loan would have been paid off')),
    'S20': F(lambda ax: ruler(ax, cand=1.0, extra=f"a full point: {C['be_bal_10']['display']} months")),
    'S21': F(lambda ax: ruler(ax, [('median', float(C['cut36_median']['value']))], extra=f"half a point: exactly {C['be_bal_05']['display']} months")),
    'S22': F(lambda ax: person(ax, 'small', ['same month as Nora', 'loan ' + d('loan_small'), 'bill ' + d('cost_small')])),
    'S23': F(lambda ax: (blocks(ax, [('Walt loan', 115, CH['small'][1]), ('bill', 3.667 * 10, MUT), ('Nora loan', 375, CH['median'][1]), ('bill', 5.124 * 10, MUT),
                                     ('Anjali loan', 655, CH['large'][1]), ('bill', 5.514 * 10, MUT)], x0=1.6, w=1.6, gap=0.6),
                         ax.text(8, 8.1, f"bill as a share of the loan: Walt {C['share_walt']['display']}; bills drawn 10x", ha='center', fontsize=10, color=MUT))),
    'S24': F(lambda ax: counter(ax, C['be_bal_small']['display'], f"months for Walt ({d('sav_small')} a month saved)")),
    'S25': F(lambda ax: net_timeline(ax, 'small', [3])),
    'S26': F(lambda ax: ruler(ax, [('median', float(C['cut36_median']['value'])), ('small', float(C['cut36_small']['value']))])),
    'S27': F(lambda ax: person(ax, 'large', ['same month, larger home', 'loan ' + d('loan_large'), 'bill ' + d('cost_large'), 'under the conforming limit'])),
    'S28': F(lambda ax: ruler(ax, [('large', float(C['cut36_large']['value'])), ('median', float(C['cut36_median']['value'])), ('small', float(C['cut36_small']['value']))],
                              extra=f"Anjali at three years: +{d('net36_large')}")),
    'S29': F(lambda ax: ruler(ax, [('large', float(C['cut36_large']['value'])), ('median', float(C['cut36_median']['value'])), ('small', float(C['cut36_small']['value']))],
                              extra='The one-point line fits none of them')),
    'S30': F(lambda ax: net_timeline(ax, 'median', [3])),
    'S31': F(lambda ax: net_timeline(ax, 'median', [3, 7])),
    'S32': F(lambda ax: textcard(ax, 'How we built these numbers', [r['card'] if r.get('card') else r['text'] for r in json.load(open(os.path.join(EP, 'out', 'script-draft.json')))['sentences']
                                                                     if r['scene'] == 'S32' and r['kind'] in ('line', 'card')], size=9)),
    'S33': F(lambda ax: (textcard(ax, 'History', [next(r['text'] for r in json.load(open(os.path.join(EP, 'out', 'script-draft.json')))['sentences'] if r['id'] == 'S33.1')]),
                         [ax.add_patch(Rectangle((1.5 + i * 1.0, 2.0), 0.7, (e['cases'][1].get('breakEvenMonths') or 0) * 0.12,
                                                 fc=WARN if e['cases'][1].get('beforeBreakEvenAnotherDrop') else MUT, ec='none')) for i, e in enumerate(M['history'])])),
    'S34': F(lambda ax: (ax.text(8, 6.5, 'Nora: her loan, her bill, how long she stays', ha='center', fontsize=13), ax.add_patch(Rectangle((1.5, 1.2), 5.5, 3.2, fill=False, ec=GRID, ls='--')),
                         ax.add_patch(Rectangle((9.0, 1.2), 5.5, 3.2, fill=False, ec=GRID, ls='--')), ax.text(8, 0.8, 'end-screen space (20 s)', ha='center', fontsize=9, color=MUT))),
}


# ILLUSTRATIVE badge with the analyst-choice numbers (Gate B review, NẶNG #1): ge7_threshold (S06), s10 (S12), s025 (S18), s05 (S21)
for _sc, _xy in {'S06': (11.4, 6.2), 'S12': (1.6, 5.9), 'S18': (10.3, 3.3), 'S21': (11.0, 7.7)}.items():
    FR[_sc] = (lambda f, xy: (lambda ax: (f(ax), badge(ax, *xy))))(FR[_sc], _xy)


def draw(scene, path=None, caption=None, size=(12.8, 7.2)):
    fig = plt.figure(figsize=size, dpi=100, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    FR[scene](ax)
    if caption:
        fig.text(0.01, 0.985, caption, fontsize=10, color=WARN, va='top')
    if path:
        fig.savefig(path, facecolor=BG); plt.close(fig)
    return fig


def main():
    out = os.path.join(HERE, 'storyboard')
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(os.path.join(out, f))
    shots = json.load(open(os.path.join(HERE, 'shotlist.json')))['shots']
    md = ['# Episode 1 — storyboard (Stage 4b, script v2)', '', 'One key frame per scene, drawn from the data by `preprod/storyboard.py`; not the final render. '
          'Dotted rectangle = 90% safe area. Contact sheet: `storyboard/contact-sheet.png`. Shots: `shotlist.md`.', '']
    for s in shots:
        draw(s['scene'], os.path.join(out, f"{s['scene']}.png"), f"{s['scene']} · {s['act']} · {s['size']} · {s['move']}")
        md.append(f"## {s['scene']} ({s['act']}) — {s['size']}, {s['move']}\n\n![{s['scene']}](storyboard/{s['scene']}.png)\n\n{s['picture']}\n\nMove: {s['moveReason']}.\n")
    # contact sheet: 5 columns
    import matplotlib.image as mpimg
    cols, n = 5, len(shots)
    rows = (n + cols - 1) // cols
    fig = plt.figure(figsize=(cols * 3.2, rows * 2.0), dpi=100, facecolor=BG)
    for i, s in enumerate(shots):
        a = fig.add_axes([(i % cols) / cols + 0.003, 1 - (i // cols + 1) / rows + 0.01, 1 / cols - 0.006, 1 / rows - 0.02])
        a.imshow(mpimg.imread(os.path.join(out, f"{s['scene']}.png"))); a.axis('off')
    fig.savefig(os.path.join(out, 'contact-sheet.png'), facecolor=BG); plt.close(fig)
    open(os.path.join(HERE, 'storyboard.md'), 'w').write('\n'.join(md) + '\n')
    print(n, 'frames + contact sheet')


if __name__ == '__main__':
    main()
