"""C5 audio stream: data-sound events of the final picture (out/sonify-events.json, checks/CONTRACT.md) and the richer plan the renderer reads
(work/audio/son-plan.json).

    python3 episodes/ep001/work/audio/src/events.py

Source: animatic/anchors.json (146 anchored picture actions; resolved_s = time on the v3.2 narration, the same time base as the video) and the
easing windows of the scene code (animatic/src/sNN.js: ease(t, tA, tA + d)). Only data elements get a sound (cue sheet "Data sonification
plan", sổ gu G-001): a line drawn, a bar or stack growing / shrinking, a dot appearing or sliding on a scale, a counter or pile roll.
Labels, cards, the letter, cuts and camera moves do not (they are not data; no sfx layer in S2 "minimal").

Kinds written to the plan:
  line  : a drawn line or a mark sliding along a scale; samples every frame (f, slope, x); the renderer plays soft low pulses on eighth notes
          of the local music tempo, pitch following the slope (palette S2)
  bar   : a bar / stack / house / ream growing (or shrinking); f0..f1, value in [0, 1] on ONE scale for the film (bar pitch MIDI 36-60)
  dot   : a dot or marker appearing; f, y (screen px; higher on screen = higher pitch)
  roll  : n elements landing one after another (monthly piles, week ticks, clock ticks); written as n bar events
"""
import json
import os

EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
FPS = 30
A = {}
for a in json.load(open(os.path.join(EP, 'animatic', 'anchors.json')))['anchors']:
    A[(a['scene'], a['id'])] = float(a['resolved_s'])
TIMING = json.load(open(os.path.join(EP, 'animatic', 'timing.json')))
SCENE_END = {}
_sc = TIMING['scenes']
for i, s in enumerate(_sc):
    SCENE_END[s['id']] = _sc[i + 1]['start'] if i + 1 < len(_sc) else TIMING['total_s']

L, C, R = 560, 960, 1360  # screen x (1920 px): left / centre / right of the chart plane

# (scene, anchor, kind, params) — offsets in s from the anchor; durations from the scene code's easing windows
PLAN = [
    # S01 cold open: the weekly rate falls to the 2026 low, then climbs back above 7%
    ('S01', 'draw', 'line', dict(t1=('S01', 'low'), slope=-0.6, x0=260, x1=1100, what='weekly rate 2025-26 drawn down to the low')),
    ('S01', 'low', 'dot', dict(y=820, x=1100, what='the low: 5.98%')),
    ('S01', 'lift', 'bar', dict(dur=0.7, v=0.15, x=C, what='$459 tile lifts off the payment stack')),
    ('S01', 'chart', 'line', dict(dt=0.2, t1=('S01', 'above7'), slope=0.8, x0=1100, x1=1500, what='rate climbs back')),
    ('S01', 'above7', 'line', dict(dur=2.2, slope=0.3, x0=1500, x1=1700, what='rate crosses 7% and keeps going')),
    # S02 the letter; three model houses (size = loan)
    ('S02', 'pull', 'bar', dict(dt=0.4, dur=0.8, v=0.2, x=L, what='small house grows')),
    ('S02', 'pull', 'bar', dict(dt=0.9, dur=0.8, v=0.45, x=C, what="Nora's house grows")),
    ('S02', 'pull', 'bar', dict(dt=1.4, dur=0.9, v=0.7, x=R, what='large house grows')),
    # S03 2023 rate line up to the peak; three houses in ten light up
    ('S03', 'draw', 'line', dict(t1=('S03', 'peak'), t1dt=0.8, slope=0.7, x0=260, x1=1400, what='weekly rate 2023 drawn up')),
    ('S03', 'nora', 'dot', dict(y=520, x=900, what="Nora's dot: October 2023")),
    ('S03', 'three', 'roll', dict(n=3, dur=0.9, v0=0.3, v1=0.4, x=C, what='three houses in ten light up')),
    # S05 the window
    ('S05', 'draw', 'line', dict(dur=3.5, slope=-0.3, x0=200, x1=1330, what='weekly rate 2025-26 drawn')),
    ('S05', 'line', 'line', dict(dur=1.4, slope=-0.8, x0=C, x1=C, what='test line slides 1 point below Nora')),
    ('S05', 'weeks', 'roll', dict(n=29, dur=2.2, v0=0.3, v1=0.3, x0=500, x1=1300, what='29 weeks of 2026 light up in order')),
    ('S05', 'gap', 'bar', dict(dur=0.9, v=0.55, x=900, what='gap at the low grows: 1.64 points')),
    # S06 the offer: the 0.59-point gap; the 1-point ruler; the $221 tile
    ('S06', 'gap', 'bar', dict(dur=0.8, v=0.3, x=C, what='gap 7.62 -> 7.03 grows: 0.59 point')),
    ('S06', 'unit', 'bar', dict(dur=1.0, v=0.45, x=1200, what='1-point ruler set beside the gap')),
    ('S06', 'lift', 'bar', dict(dur=0.7, v=0.1, x=C, what='$221 tile lifts off the stack')),
    # S07 the bill
    ('S07', 'ream', 'bar', dict(dur=1.2, v=0.6, x=1200, what='$5,124 ream grows beside the $221 tile')),
    ('S07', 'median', 'line', dict(dur=1.5, slope=0.2, x0=600, x1=1000, what='$5,124 dot slides to the median')),
    # S08 two answers
    ('S08', 'worth', 'bar', dict(dur=1.0, v=0.35, x=800, what='"fees paid back" bracket grows')),
    ('S08', 'stay', 'line', dict(dur=1.4, slope=0.0, x0=900, x1=1300, what='the flag slides to 3 years')),
    ('S08', 'short', 'line', dict(dur=1.4, slope=0.4, x0=300, x1=650, what="Nora's dot slides to 0.59, stops short of 1")),
    ('S08', 'div24', 'roll', dict(dt=-0.4, n=6, dur=0.5, v0=0.3, v1=0.4, x=1400, what='calendar flips to 24')),
    # S09 break-even, first try
    ('S09', 'letter', 'bar', dict(dt=1.0, dur=1.0, v=0.6, x=700, what='the $5,124 fee ream grows')),
    ('S09', 'stack', 'roll', dict(n=24, t1=('S09', 'm24'), v0=0.05, v1=0.6, x0=900, x1=1300, what='a $221 pile lands each month, 24 months')),
    ('S09', 'owes', 'bar', dict(dur=1.5, v=0.4, x=C, what='two "balance paid off" stacks appear')),
    # S10 the clock runs again
    ('S10', 'k35', 'roll', dict(dt=-1.2, n=12, dur=1.2, v0=0.1, v1=0.35, x=C, what='clock hand sweeps 35 monthly ticks')),
    ('S10', 'each', 'bar', dict(dur=0.8, v=0.3, x=C, what='one payment bar: interest | principal')),
    ('S10', 'reset', 'line', dict(dur=1.2, slope=-0.9, x0=C, x1=C, what='hand runs back to 0')),
    ('S10', 'interest', 'bar', dict(dur=0.8, v=0.35, x=C, what="new loan's payment bar: more interest")),
    ('S10', 'slow', 'line', dict(dur=3.0, slope=0.25, x0=700, x1=1200, what='two balance stacks grow month by month, new one lower')),
    ('S10', 'gap', 'bar', dict(dur=0.8, v=0.25, x=1100, what='striped $1,133 = the gap')),
    ('S10', 'move', 'line', dict(dur=1.2, slope=0.6, x0=1100, x1=800, what='striped tile flies onto the fee ream')),
    ('S10', 'more', 'roll', dict(n=6, t1=('S10', 'be30'), t1dt=-0.3, v0=0.62, v1=0.7, x0=900, x1=1200, what='piles for months 25-30')),
    # S11 a quarter point: never
    ('S11', 'smaller', 'line', dict(dt=0.3, t1=('S11', 'q'), t1dt=0.2, slope=-0.3, x0=900, x1=500, what="Nora's dot slides left from 0.59 to 0.25")),
    ('S11', 'q', 'dot', dict(y=700, x=500, what='dot stops at 0.25')),
    ('S11', 'd38', 'line', dict(dt=-1.0, dur=1.3, slope=0.8, x0=300, x1=1100, what='"division" line drawn, crosses the fee line at month 38')),
    ('S11', 'curve', 'line', dict(t1=('S11', 'never'), t1dt=-0.6, slope=0.35, x0=300, x1=1400, what='"savings minus what she still owes" rises, never reaches')),
    ('S11', 'never', 'line', dict(dt=-0.6, dur=1.4, slope=-0.9, x0=1400, x1=1750, what='axis extends to the last payment; the line falls')),
    # S12 one point
    ('S12', 'full', 'line', dict(dt=-0.4, dur=0.9, slope=0.2, x0=500, x1=1000, what='dot slides to the 1-point mark')),
    ('S12', 'full', 'line', dict(dt=0.5, t1=('S12', 'm18'), t1dt=0.2, slope=0.9, x0=300, x1=900, id_='S12.full.line', what='the 1-point line drawn')),
    ('S12', 'm18', 'dot', dict(y=520, x=900, what='crosses the fee line at month 18')),
    # S13 half a point
    ('S13', 'between', 'line', dict(t1=('S13', 'half'), t1dt=-0.3, slope=0.0, wobble=True, x0=500, x1=1000, what='dot swings between 0.25 and 1')),
    ('S13', 'half', 'line', dict(t1=('S13', 'm36'), t1dt=0.2, slope=0.6, x0=300, x1=1300, what='the 0.5 line drawn')),
    ('S13', 'm36', 'dot', dict(y=520, x=1300, what='crosses the fee line at month 36')),
    ('S13', 'real', 'dot', dict(y=600, x=1150, what='the real 0.59 dot appears, clears it')),
    ('S13', 'pays', 'line', dict(dur=1.4, slope=0.7, x0=300, x1=1200, what='the 0.59 line crosses the fee line before 3 years')),
    # S14 Walt
    ('S14', 'walt', 'bar', dict(dur=0.8, v=0.2, x=L, what="Walt's small house grows")),
    ('S14', 'bill', 'bar', dict(dur=0.8, v=0.5, x=1200, what='$3,667 fee ream grows beside $5,124')),
    # S15 the bill does not shrink
    ('S15', 'grow', 'bar', dict(dt=0.4, dur=1.4, v=0.2, x=C, what="loan row: Walt's bar shrinks to $115,000")),
    ('S15', 'bills', 'bar', dict(dur=2.4, v=0.5, x=C, what="bill row: Walt's bar shrinks a little")),
    ('S15', 'sav', 'bar', dict(dur=1.4, v=0.08, x=C, what="monthly savings row: Walt's bar shrinks a lot")),
    ('S15', 'stack', 'roll', dict(dt=0.4, n=15, t1=('S15', 'm75'), t1dt=0.2, v0=0.03, v1=0.55, x0=800, x1=1200, what='$68 piles stack slowly to month 75')),
    ('S15', 'm75', 'dot', dict(y=450, x=1200, what='break-even: month 75')),
    # S16 Walt sells after 3 years
    ('S16', 'sell', 'roll', dict(n=18, t1=('S16', 'short'), t1dt=-0.3, v0=0.03, v1=0.35, x0=700, x1=1200, what='36 piles of $68 beside the fees')),
    ('S16', 'short', 'bar', dict(dur=0.4, v=0.3, x=1200, what='the red gap: $1,777 short')),
    ('S16', 'cut', 'line', dict(dur=1.6, slope=0.5, x0=500, x1=1300, what='triangle slides past 1 point to 1.12')),
    ('S16', 'more', 'bar', dict(dur=0.6, v=0.12, x=1300, what='segment 1 -> 1.12 filled')),
    ('S16', 'fees', 'bar', dict(dur=0.5, v=0.5, x=C, what='bill row: Walt close to Nora')),
    ('S16', 'savings', 'bar', dict(dur=0.5, v=0.1, x=C, what='savings row: Walt much smaller')),
    # S17 Anjali
    ('S17', 'anj', 'bar', dict(dur=0.9, v=0.85, x=R, what="Anjali's large house grows")),
    ('S17', 'bill', 'bar', dict(dur=0.5, v=0.62, x=1200, what='$5,514 fee ream grows beside $5,124')),
    ('S17', 'stack', 'roll', dict(n=18, t1=('S17', 'ahead'), t1dt=-0.3, v0=0.1, v1=0.8, x0=800, x1=1300, what='$387 piles rise fast, past the fees at month 18')),
    ('S17', 'third', 'line', dict(dur=1.4, slope=-0.4, x0=1100, x1=500, what='square slides to about a third of a point')),
    # S18 the three-mark ruler
    ('S18', 'size', 'roll', dict(dt=0.2, n=3, dur=0.75, v0=0.2, v1=0.85, x0=500, x1=1400, what='three houses on the loan-size axis')),
    ('S18', 'walt', 'bar', dict(dur=0.9, v=1.0, x=500, what='triangle column 1.12 points')),
    ('S18', 'nora', 'bar', dict(dur=0.9, v=0.45, x=C, what='circle column 0.5 point')),
    ('S18', 'anj', 'bar', dict(dur=0.9, v=0.3, x=1400, what='square column about a third of a point')),
    ('S18', 'one', 'line', dict(dur=1.6, slope=0.0, x0=400, x1=1500, what='1-point rule of thumb sweeps across the three columns')),
    # S19 what this does not say
    ('S19', 'p25', 'dot', dict(y=640, x=700, what='bill scale: $3,443 mark')),
    ('S19', 'p75', 'dot', dict(y=560, x=1250, what='$8,270 mark; band filled, $5,124 dot in the middle')),
    ('S19', 'p75', 'dot', dict(dt=0.6, y=600, x=960, id_='S19.median.dot', what='$5,124 dot in the middle of the band')),
    # S20 the question stays
    ('S20', 'stay', 'line', dict(t1=('S20', 'y3'), slope=0.1, x0=400, x1=900, step=1.0, what='time marker runs along the path to year 3')),
    ('S20', 'y3', 'bar', dict(dt=-0.2, dur=0.6, v=0.25, x=900, what='surplus pile: +$1,039 ahead')),
    ('S20', 'y3', 'line', dict(dt=0.6, t1=('S20', 'y7'), slope=0.15, x0=900, x1=1300, step=1.0, id_='S20.to7.line', what='marker runs on to year 7')),
    ('S20', 'y7', 'bar', dict(dt=-0.2, dur=0.6, v=0.6, x=1300, what='surplus pile grows: +$8,093 ahead')),
]


def at(ref, dt=0.0):
    return A[ref] + dt


def main():
    plan, ev = [], {'fps': FPS, 'bar': [], 'line': [], 'dot': []}
    for sc, aid, kind, p in PLAN:
        t0 = at((sc, aid), p.get('dt', 0.0))
        if 't1' in p:
            t1 = at(p['t1'], p.get('t1dt', 0.0))
        else:
            t1 = t0 + p.get('dur', 0.0)
        t1 = min(t1, SCENE_END[sc] - 0.05)
        eid = p.get('id_') or f'{sc}.{aid}.{kind}'
        row = {'id': eid, 'scene': sc, 'anchor': aid, 'kind': kind, 't0': round(t0, 3), 't1': round(max(t1, t0), 3), 'what': p['what']}
        if kind == 'line':
            f0, f1 = int(round(t0 * FPS)), max(int(round(t1 * FPS)), int(round(t0 * FPS)) + 2)
            row.update(slope=p['slope'], x0=p['x0'], x1=p['x1'], wobble=bool(p.get('wobble')), step=p.get('step'))
            for f in range(f0, f1):
                u = (f - f0) / max(1, f1 - f0 - 1)
                s = p['slope']
                if p.get('wobble'):
                    import math
                    s = 0.8 * math.sin(2 * math.pi * u * 2.5)
                ev['line'].append({'f': f, 'id': eid, 'slope': round(s, 3), 'x': round(p['x0'] + u * (p['x1'] - p['x0']), 1)})
        elif kind == 'bar':
            row.update(v=p['v'], x=p['x'])
            ev['bar'].append({'id': eid, 'f0': int(round(t0 * FPS)), 'f1': int(round(t1 * FPS)), 'value': p['v'], 'x': p['x']})
        elif kind == 'dot':
            row.update(y=p['y'], x=p['x'])
            ev['dot'].append({'f': int(round(t0 * FPS)), 'id': eid, 'y': p['y'], 'x': p['x']})
        elif kind == 'roll':
            n = p['n']
            row.update(n=n, v0=p['v0'], v1=p['v1'])
            items = []
            for k in range(n):
                u = k / max(1, n - 1)
                tk = t0 + (t1 - t0) * (k + 1) / n if n > 1 else t0
                x = p.get('x', (p.get('x0', C) + u * (p.get('x1', C) - p.get('x0', C))))
                v = p['v0'] + u * (p['v1'] - p['v0'])
                items.append({'t': round(tk, 3), 'v': round(v, 3), 'x': round(x, 1)})
                ev['bar'].append({'id': f'{eid}.{k + 1}', 'f0': int(round(tk * FPS)), 'f1': int(round(tk * FPS)) + 3, 'value': round(v, 3), 'x': round(x, 1)})
            row['items'] = items
        plan.append(row)
    for k in ('bar', 'line', 'dot'):
        ev[k].sort(key=lambda e: e.get('f0', e.get('f')))
    ev['_about'] = ('Data-sound events of the C5 picture (frame at 30 fps where each sound starts), from animatic/anchors.json + the scene code easing windows '
                    '(work/audio/src/events.py). bar: f0..f1 growth, value = one pitch scale for the film (0..1 -> MIDI 36..60); line: every frame of a draw or a '
                    'slide (slope at the tip); dot: frame it appears, y on screen. Palette S2 "minimal" (sổ gu G-005 · chọn).')
    json.dump(ev, open(os.path.join(EP, 'out', 'sonify-events.json'), 'w'), indent=1)
    os.makedirs(os.path.join(EP, 'work', 'audio'), exist_ok=True)
    json.dump({'_about': 'Sonification plan (renderer input), one row per data action; see events.py', 'rows': plan},
              open(os.path.join(EP, 'work', 'audio', 'son-plan.json'), 'w'), indent=1, ensure_ascii=False)
    print(len(plan), 'actions;', {k: len(ev[k]) for k in ('bar', 'line', 'dot')})


if __name__ == '__main__':
    main()
