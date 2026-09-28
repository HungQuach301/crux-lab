"""Episode 1 storyboard (M1b): key frames drawn from the real data (composition + numbers + what moves; not the final
render). Writes preprod/storyboard/sb-NN.png (portrait pages for a phone, 3 frames each) and preprod/storyboard.md.

    python3 episodes/ep001/preprod/storyboard.py
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

T = json.load(open(os.path.join(EP, '..', '..', 'genre-spec', 'channel', 'visual-tokens.json')))['colors']
BG, INK, MUT, ACC, WARN, POS, NEG, GRID = (T[k] for k in ('bg', 'ink', 'ink-muted', 'accent', 'warn', 'positive', 'negative', 'grid'))
plt.rcParams.update({'font.family': 'DejaVu Sans', 'text.color': INK, 'axes.edgecolor': MUT, 'axes.labelcolor': MUT, 'xtick.color': MUT, 'ytick.color': MUT})
C = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']}
M = json.load(open(os.path.join(EP, 'out', 'model.json')))
W = [(r['date'], float(r['rate'])) for r in csv.DictReader(open(os.path.join(EP, 'data', 'normalized', 'mortgage30_weekly.csv')))]
d = lambda k: C[k]['display'].replace('$', r'\$')
yr = lambda s: int(s[:4]) + (int(s[5:7]) - 1) / 12 + (int(s[8:10]) if len(s) > 8 else 15) / 365
SC = M['scenario']
COL = {'dan': WARN, 'maya': INK, 'priya': ACC}


def frame(ax):
    ax.set_facecolor(BG); ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis('off')
    ax.add_patch(Rectangle((0.8, 0.45), 14.4, 8.1, fill=False, ls=':', lw=0.6, ec=GRID))


def chart_in(ax, rect):
    fig, bb = ax.figure, ax.get_position()
    x0, y0, w, h = rect
    a = fig.add_axes([bb.x0 + bb.width * x0 / 16, bb.y0 + bb.height * y0 / 9, bb.width * w / 16, bb.height * h / 9])
    a.set_facecolor(BG)
    for s in ('top', 'right'):
        a.spines[s].set_visible(False)
    a.tick_params(labelsize=7)
    return a


def badge(ax, x, y):
    ax.text(x, y, 'ILLUSTRATIVE', fontsize=6.5, fontweight='bold', color=BG, bbox=dict(boxstyle='round,pad=0.25', fc=WARN, ec='none'))


def card(ax, x, y, name, lines, col, w=4.2):
    ax.add_patch(FancyBboxPatch((x, y - 0.4), w, 3.0, boxstyle='round,pad=0.1', fc=T['surface'], ec=col, lw=1.5))
    ax.text(x + 0.3, y + 2.1, name, fontsize=13, fontweight='bold', color=col)
    for i, l in enumerate(lines):
        ax.text(x + 0.3, y + 1.5 - i * 0.5, l, fontsize=9, color=INK)


def f_maya(ax):
    frame(ax)
    card(ax, 5.8, 3.2, 'Maya', ['borrowed ' + d('loan_maya'), 'rate ' + d('r_old') + '  (lands on the word)'], INK)  # October 2023 is said in act 1 (<= 2 new numbers per scene)
    badge(ax, 10.2, 5.6)
    ax.text(8, 1.6, '(picture first: 1.2 s before the first word)', ha='center', fontsize=8, color=MUT, style='italic')


def f_today(ax):
    frame(ax)
    a = chart_in(ax, (1.6, 1.4, 12.8, 5.6))
    pts = [(yr(x[0]), x[1]) for x in W if x[0] >= '2023-06']
    a.plot([p[0] for p in pts], [p[1] for p in pts], color=ACC, lw=1.5)
    a.plot([yr('2023-10-15')], [SC['oldRate']], 'o', color=INK); a.plot([pts[-1][0]], [pts[-1][1]], 'o', color=WARN)
    a.text(yr('2023-10-15'), SC['oldRate'] + 0.12, f"Maya {C['r_old']['display']}", fontsize=9, color=INK)
    a.text(pts[-1][0] - 0.9, pts[-1][1] + 0.18, f"this week {C['r_today']['display']}", fontsize=9, color=WARN)
    a.set_ylim(5.5, 8.2); a.set_yticks([]); a.spines['left'].set_visible(False)
    a.set_xticks([2024, 2025, 2026]); a.set_xticklabels(['2024', '2025', '2026'])


def f_bill(ax):
    frame(ax)
    card(ax, 2.0, 3.2, 'Maya', ['balance ' + '\\$' + f"{M['characters']['maya']['balance']:,.0f}", 'rate ' + d('r_old'), 'today ' + d('r_today')], INK)
    for i in range(6):
        ax.add_patch(FancyBboxPatch((9.5, 2.3 + i * 0.45), 2.4, 0.35, boxstyle='round,pad=0.02', fc=NEG, ec='none'))
    ax.text(10.7, 5.3, 'closing costs ' + d('cost_maya'), ha='center', fontsize=10)
    ax.text(8, 1.2, 'When does that money come back?   months: 0', ha='center', fontsize=11, fontweight='bold')


def f_ruler(ax, stage):
    frame(ax)
    ax.plot([2, 14], [4.2, 4.2], color=INK, lw=2)
    for v in (0, 0.5, 1, 1.5, 2):
        x = 2 + 6 * v; ax.plot([x, x], [4.0, 4.4], color=INK, lw=1.5); ax.text(x, 3.4, f'{v:g}', ha='center', fontsize=9)
    ax.text(8, 2.7, 'rate cut (percentage points) that pays back within 36 months, counting what is still owed', ha='center', fontsize=8, color=MUT)
    for k in range(13):
        ax.plot(2.3 + k * 0.9, 1.4, 'o', ms=3, color=MUT)
    ax.text(8, 0.85, f"{C['n_eps']['display']} drops since {C['y1971']['display']}", ha='center', fontsize=7, color=MUT)
    ax.text(1.2, 6.9, 'Maya', fontsize=10, fontweight='bold', color=INK)
    if stage == 'rehook':
        ax.plot([2, 14], [4.9, 4.9], color=WARN, lw=1, ls=':'); ax.text(8, 5.4, '?', ha='center', fontsize=22, fontweight='bold', color=WARN)
    else:
        for key, col, dy in (('maya', INK, 0), ('dan', WARN, 0.9), ('priya', ACC, 1.8)):
            x = 2 + 6 * float(C['cut36_' + key]['value'])
            ax.plot([x], [4.9 + dy * 0.0], marker='v', ms=11, color=col)
            ax.text(x, 5.4 + dy, f"{key.title()} {C['cut36_' + key]['display']}", ha='center', fontsize=10, fontweight='bold', color=col)
        x = 2 + 6 * float(C['cut_today']['value'])
        ax.plot([x, x], [3.9, 4.5], color=POS, lw=3); ax.text(x + 0.2, 3.0, f"today {C['cut_today']['display']}", fontsize=8, color=POS)
    badge(ax, 11.6, 7.4)


def f_balance(ax):
    frame(ax)
    c = M['characters']['maya']; P, r0, k, r1 = c['loan'], SC['oldRate'], SC['paymentsMade'], SC['todayRate']
    B = c['balance']
    ms = list(range(0, 61))
    old = [refi.balance_after(P, r0, 360, k + m) for m in ms]; new = [refi.balance_after(B, r1, 360, m) for m in ms]
    a = chart_in(ax, (1.6, 1.4, 6.0, 5.6))
    a.plot(ms, [x / 1000 for x in old], color=MUT, lw=2, label='old loan'); a.plot(ms, [x / 1000 for x in new], color=ACC, lw=2, label='new loan')
    a.axvline(c['simple'], color=WARN, lw=0.8, ls=':'); a.legend(fontsize=7, frameon=False)
    a.set_title('balance still owed ($000)', fontsize=8, color=INK); a.set_xlabel('months after refinancing', fontsize=7)
    b = chart_in(ax, (8.8, 1.4, 6.0, 5.6))
    sav = [c['monthlySavings'] * m for m in ms]; tot = [s_ + (o - n) for s_, o, n in zip(sav, old, new)]
    b.plot(ms, sav, color=MUT, lw=1.5, ls='--', label='savings only'); b.plot(ms, tot, color=INK, lw=2, label='savings + balance gap')
    b.axhline(c['cost'], color=NEG, lw=1); b.text(1, c['cost'] + 250, 'bill ' + d('cost_maya'), fontsize=8, color=NEG)
    b.axvline(c['simple'], color=WARN, lw=0.8, ls=':'); b.axvline(c['withBalance'], color=POS, lw=1)
    b.text(c['simple'] - 7, 200, f"{c['simple']}", fontsize=9, color=WARN); b.text(c['withBalance'] + 1, 200, f"{c['withBalance']}", fontsize=9, color=POS)
    b.set_xlim(0, 48); b.set_ylim(0, 12000); b.legend(fontsize=7, frameon=False, loc='upper left'); b.set_xlabel('months', fontsize=7)


def f_curves(ax):
    frame(ax)
    c = M['characters']['maya']; P, r0, k = c['loan'], SC['oldRate'], SC['paymentsMade']
    xs = [i / 100 for i in range(15, 201, 2)]
    simple, bal = [], []
    for x in xs:
        b = refi.both(P, r0, k, r0 - x, c['cost']); simple.append(b['simple']); bal.append(b['withBalance'] or 400)
    a = chart_in(ax, (1.8, 1.3, 12.6, 6.0))
    a.plot(xs, simple, color=MUT, lw=1.5, ls='--', label='most calculators (cost / monthly saving)')
    a.plot(xs, bal, color=INK, lw=2, label='counting what is still owed')
    a.axvline(float(C['cut_today']['value']), color=POS, lw=0.8); a.text(float(C['cut_today']['value']) + 0.03, 110, 'today', fontsize=8, color=POS)
    a.set_ylim(0, 120); a.set_xlim(0.15, 2.05); a.set_xlabel('rate cut (points)', fontsize=7); a.set_ylabel('months to break even', fontsize=7)
    a.legend(fontsize=7, frameon=False); a.text(0.2, 112, 'never', fontsize=8, color=INK)


def f_three(ax):
    frame(ax)
    for i, key in enumerate(('dan', 'maya', 'priya')):
        c = M['characters'][key]
        card(ax, 1.3 + i * 4.6, 3.6, key.title(), ['loan \\$' + f"{c['loan']:,.0f}", 'bill \\$' + f"{c['cost']:,.0f}",
                                                   f"break-even {c['withBalance'] or 'never'} mo", f"3 yr: {'+' if c['net36'] >= 0 else '-'}\\${abs(c['net36']):,.0f}"], COL[key], w=4.2)
    badge(ax, 1.3, 7.1)
    ax.text(8, 1.6, 'same month, same rate: size of the loan, its age, and the time kept decide', ha='center', fontsize=9, color=MUT)


def f_episodes(ax):
    frame(ax)
    rows = [(e['peak'][:4], next(c for c in e['cases'] if c['spread'] == 1.0)) for e in M['history']]
    for i, (y, c) in enumerate(rows):
        h = (c['breakEvenMonths'] or 0) * 0.22
        ax.add_patch(Rectangle((1.4 + i * 1.03, 1.4), 0.7, h, fc=MUT if c['costIllustrative'] else ACC, ec='none'))
        ax.plot([1.35 + i * 1.03, 2.15 + i * 1.03], [1.4 + c['breakEvenSimple'] * 0.22] * 2, color=INK, lw=1.2)
        if c['beforeBreakEvenAnotherDrop']:
            ax.plot(1.75 + i * 1.03, 1.4 + h + 0.35, 'v', color=NEG, ms=6)
        ax.text(1.75 + i * 1.03, 0.9, y, ha='center', fontsize=6, color=MUT)
    ax.text(8, 7.6, 'months to break even at a 1-point cut, every drop: bar = counting the balance, line = simple division', ha='center', fontsize=8.5)
    ax.text(8, 7.0, 'grey = fixed pre-2018 cost share (ILLUSTRATIVE); red mark: the next full point came first', ha='center', fontsize=7, color=MUT)


def f_card(ax):
    frame(ax)
    ax.text(1.3, 7.4, 'Method', fontsize=14, fontweight='bold')
    for i, t in enumerate(['Rates: Freddie Mac PMMS via FRED (MORTGAGE30US), weekly 1971-2026', 'Check: Optimal Blue OBMMIC30YF since 2017',
                           'Costs: HMDA 2018-2025, originated refinances, first lien, 360 months', 'Break-even: savings + balance difference >= bill; cash closing costs; no taxes',
                           'Maya, Dan, Priya: ILLUSTRATIVE, medians for their loan size']):
        ax.text(1.3, 6.3 - i * 0.85, t, fontsize=8.5)


FRAMES = [
    ('co-maya', 'Cold open (G-007): one person, one moment. Maya, October 2023: her loan and her rate.', f_maya),
    ('co-today', 'Her rate against this week\'s average on the same line.', f_today),
    ('co-cost', 'The lender\'s offer: the closing-cost bill lands; the question and an empty month counter.', f_bill),
    ('a1-rehook', 'Rehook 0:30-0:45, ONE object: the rate-cut ruler with Maya at its end; the marker sweeps, one "?" (no answer yet).', lambda a: f_ruler(a, 'rehook')),
    ('a1-turn', 'Act 1 turn: the bill hits Dan, Maya and Priya differently (cards, their medians, ILLUSTRATIVE).', f_three),
    ('a2-real', 'Act 2 thesis: balance still owed on both loans (left); savings alone vs savings + balance gap against the bill (right): 24 becomes 30.', f_balance),
    ('a2-cliff', 'The two answers across every cut: the simple division (dashed) and counting what is owed (solid, "never" below 0.25).', f_curves),
    ('a3-range', 'Act 3: every drop since 1971 (DX-H6), both answers per drop.', f_episodes),
    ('a3-answer2', 'Answer: the rehook ruler returns; Maya 0.5, Dan 1.12, Priya 0.2; today\'s cut 0.59 marked.', lambda a: f_ruler(a, 'answer')),
    ('m-assume', 'Method card (static, readable).', f_card),
]


def main():
    out = os.path.join(HERE, 'storyboard')
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(os.path.join(out, f))
    md = ['# Episode 1 — storyboard M1b (key frames)', '', 'Drawn from the data by `preprod/storyboard.py`; not the final render. Dotted rectangle = 90% safe area. '
          'Every shot: `shotlist.md`.', '']
    per, fh = 3, 0.92 * 9 / 16 * 10.8 / 19.2
    for p in range(0, len(FRAMES), per):
        chunk = FRAMES[p:p + per]
        fig = plt.figure(figsize=(10.8, 19.2), dpi=100, facecolor=BG)
        for i, (sc, cap, fn) in enumerate(chunk):
            top = 1 - i / per - 0.01
            ax = fig.add_axes([0.04, top - 0.03 - fh, 0.92, fh]); fn(ax)
            fig.text(0.04, top - 0.02, f'{p + i + 1:02d}  {sc}', fontsize=12, fontweight='bold', color=WARN, va='center')
            fig.text(0.04, top - 0.035 - fh, cap, fontsize=10, color=INK, va='top', wrap=True)
        name = f'sb-{p // per + 1:02d}.png'
        fig.savefig(os.path.join(out, name), facecolor=BG); plt.close(fig)
        md.append(f'![{name}](storyboard/{name})')
        md += [f'- **{p + i + 1:02d} `{sc}`** {cap}' for i, (sc, cap, _) in enumerate(chunk)] + ['']
    open(os.path.join(HERE, 'storyboard.md'), 'w').write('\n'.join(md) + '\n')
    print('pages', (len(FRAMES) + per - 1) // per)


if __name__ == '__main__':
    main()
