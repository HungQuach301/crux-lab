"""C5 Tập 2 · luồng A: data-sound events of the final picture (out/sonify-events.json, checks/CONTRACT.md) and the plan the renderer reads
(work/audio/son-plan.json). Code model: episodes/ep001/work/audio/src/events.py (Tập 1, palette S2 "minimal", sổ gu G-005 · chọn).

    python3 episodes/ep002/audio_src/events.py

Times: the anchors of the picture (animatic/src/anchors/Sxx.json: sentence + keyword of its spoken form + dt), resolved here against the CURRENT
animatic/timing.json exactly as animatic/src/build_anchors.py and the page do (so a re-timed timing.json, e.g. the S10.1 pause, moves the sounds
with the picture). Only DATA gets a sound (G-001): the rate path moving against the 9% line, the head start (start point vs the line), the
cushion jar filling and draining, coin piles / costlier blocks growing, replay frames dropping their cells, red (costlier) shares growing or
shrinking. Labels, numbers appearing as text, cards, dips and the method card do not (no sfx layer in S2).

Which beats are sonified, and how (the episode's data story, beats.md):
  * the rate crossing 9%: the variable path running across the fixed line (S01 KEY-1, S03.4) = a `line` with a wobbling slope (pitch swings above
    and below the rail's pitch); the climbs above 9% (S06.3, S07.5 left, S08.2-3 to 19.3%) = rising `line`s; the level 9% rail = a flat line;
  * the head start: every flip of the start point (KEY-2 S03, S04.4, S05.5) = a `dot` whose pitch is its height (3 points below = low,
    on the line, above the line = high);
  * the cushion: the jar filling = a growing `bar` (S06.1, S06.5, S07.5 right); the jar draining = a falling `line` (S06.3 "cost more overall",
    S08.4 "gone", S07.5 left);
  * red outcome tokens: replay frames dropping cells (S04.2 KEY-5, accelerating `roll`, pitch follows the T-bill ridge); cells flipping, red ones
    higher and louder (S05.3 KEY-3, S07.7); the red shares as `bar`s whose pitch is the share (S05.4 halves, S09 20.4% / 10.5%, S10.1 jumps
    31.3% -> 57.9% -> 72.9%, then back to 3 points); the gap opening and red columns shrinking (S09 KEY-7) = falling `line`s;
  * coin piles (interest paid) and the costlier block (S04.3, S08.6-7) = `bar`s; the S08.8 rate cap lowering = falling `line`.
One pitch scale for the film: value 0..1 -> MIDI 36..60 (bars, roll items); shares are mapped as value = 0.3 + share.
"""
import glob
import json
import math
import os
import re

EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
AN = os.path.join(EP, 'animatic')
FPS = 30
TM = json.load(open(os.path.join(AN, 'timing.json')))
SENT = {s['id']: s for sc in TM['scenes'] for s in sc['sentences']}
SCENE_END = {s['id']: s['end'] for s in TM['scenes']}
norm = lambda s: [w for w in re.sub(r"[^a-z0-9']+", ' ', s.lower().replace('’', "'")).split() if w]


def resolve(sid, at):
    s = SENT[sid]
    if at == 'start':
        return s['start']
    if at == 'end':
        return s['end']
    k, w = norm(at), [x['t'] for x in s['words']]
    hit = next((j for j in range(len(w) - len(k) + 1) if w[j:j + len(k)] == k), -1)
    if hit >= 0:
        return s['words'][hit]['start']
    j = s['text'].lower().find(at.lower())
    return s['start'] + (s['end'] - s['start']) * j / len(s['text']) if j >= 0 else s['start']


A = {}
for f in sorted(glob.glob(os.path.join(AN, 'src', 'anchors', 'S*.json'))):
    sc = os.path.basename(f)[:3]
    for i, sid, at, dt, *_ in json.load(open(f)):
        sid = sid if '.' in sid else f'{sc}.{sid}'
        A[(sc, i)] = resolve(sid, at) + dt

L, C, R = 560, 960, 1360          # screen x (1920 px): left bin / centre / right bin
share = lambda p: round(min(1.0, 0.3 + p), 3)   # red share -> one pitch scale (0..1)


def ridge(u):
    """Shape of the 3-month T-bill over 1954..2016 (u = 0..1): waves up to the 1981 peak (u ~ 0.44), down to ~0 by 2009, flat after."""
    if u <= 0.44:
        f = (u / 0.44) ** 1.4 + 0.08 * math.sin(2 * math.pi * u * 5)
    elif u <= 0.88:
        f = 1 - ((u - 0.44) / 0.44) ** 0.8 + 0.06 * math.sin(2 * math.pi * u * 4)
    else:
        f = 0.02
    return 0.15 + 0.6 * max(0.0, min(1.0, f))


def cells(n, red_left, red_right):
    """n cells left -> right under the ridge; red ones (costlier) one fifth of the scale higher. Deterministic red pattern by share."""
    out = []
    for k in range(n):
        u = k / max(1, n - 1)
        p = red_left if u < 0.44 else red_right
        red = (int((k + 1) * p) - int(k * p)) > 0
        out.append(round(ridge(u) * 0.6 + (0.35 if red else 0.0), 3))
    return out


# (scene, anchor, kind, params) — offsets in s from the anchor
PLAN = [
    # S01 KEY-1: the 9% rail drawn, the variable start below it, the path runs across the rail many times
    ('S01', 'k1fixed', 'line', dict(dur=0.8, slope=0.0, x0=300, x1=1600, what='the 9% fixed line draws across both cards (level)')),
    ('S01', 'k1var', 'dot', dict(y=640, x=1100, what="the variable start appears below the line (7.5%)")),
    ('S01', 'k1path', 'line', dict(t1=('S01', 'k1risk'), wobble=True, x0=500, x1=1500, what='variable path runs, crossing the 9% line many times')),
    # S02: program cost vs the federal block; the private-lender rest lights
    ('S02', 'bar', 'bar', dict(dur=0.8, v=0.6, x=C, what='program-cost outline with the federal block at its base')),
    ('S02', 'rest', 'bar', dict(dur=0.7, v=0.4, x=C, what='the part above the federal block lights: private lender')),
    # S03: K1 again, then KEY-2 head start flips (pitch = height of the start point)
    ('S03', 'k1var', 'dot', dict(y=640, x=1100, what='variable start below the line')),
    ('S03', 'k1run', 'line', dict(t1=('S03', 'k1end'), wobble=True, x0=500, x1=1500, what='variable path runs (real replay)')),
    ('S03', 'k2big', 'dot', dict(y=780, x=1100, what='start 3 points below the line')),
    ('S03', 'k2leah', 'dot', dict(y=690, x=1100, what="flip: Leah's 1.5 points below")),
    ('S03', 'k2zero', 'dot', dict(y=560, x=1100, what='flip: start on the line (no head start)')),
    ('S03', 'k2neg', 'dot', dict(y=470, x=1100, what='flip: start above the line (reversed)')),
    # S04 KEY-5: first frame rides the ridge, then frames step right faster and faster, dropping a cell each
    ('S04', 'k5ride', 'line', dict(t1=('S04', 'k5tb'), slope=0.3, x0=260, x1=520, what='first 10-year frame: the bead copies the T-bill steps')),
    ('S04', 'k5tb', 'roll', dict(t1=('S04', 'k5only'), n=30, accel=True, vfun='ridge', x0=300, x1=1620, what='frames step right, faster and faster, each dropping a cell')),
    ('S04', 'piles', 'bar', dict(dur=1.0, v=0.5, x=700, what='interest pile (fixed) rises')),
    ('S04', 'piles', 'bar', dict(dt=0.15, dur=1.0, v=0.5, x=1200, id_='S04.piles.bar2', what='interest pile (variable) rises to the same height')),
    ('S04', 'worst', 'bar', dict(dur=0.9, v=0.72, x=1200, what='a costlier (red) block grows on the variable pile')),
    ('S04', 'k2a', 'dot', dict(y=780, x=1100, what='start 3 points below')),
    ('S04', 'k2b', 'dot', dict(y=690, x=1100, what='flip: 1.5 points below')),
    ('S04', 'k2c', 'dot', dict(y=560, x=1100, what='flip: on the line')),
    ('S04', 'k2d', 'dot', dict(y=470, x=1100, what='flip: above the line')),
    # S05 KEY-3: the scan (amber almost everywhere), cells flip (few red), the two halves, the worst cell
    ('S05', 'k3scan', 'roll', dict(t1=('S05', 'k3above'), n=16, vfun='ridge', x0=300, x1=1620, what='a frame scans the ridge; the amber tally fills almost everywhere')),
    ('S05', 'k3cost', 'roll', dict(t1=('S05', 'k3all'), t1dt=0.4, n=22, red=(0.284, 0.035), x0=300, x1=1620, what='cells flip left to right: only some turn red (14.2%)')),
    ('S05', 'k3early', 'bar', dict(dur=0.6, v=share(0.284), x=L, what='left half (1954-1980): 28.4% red')),
    ('S05', 'k3late', 'bar', dict(dur=0.6, v=share(0.035), x=R, what='right half (1981 on): 3.5% red')),
    ('S05', 'worst', 'dot', dict(y=720, x=640, what='ring on the worst cell (April 1977)')),
    ('S05', 'cutHS', 'dot', dict(dt=0.3, y=690, x=1100, what="K2 at Leah's 1.5-point head start")),
    # S06 KEY-4: the cushion fills, the rate climbs above 9%, the cushion drains dry, the costlier block grows; a falling stretch keeps filling it
    ('S06', 'fill0', 'bar', dict(t1=('S06', 'full'), v=0.85, x=1300, what='jar fills from the gap under the 9% line (fastest on the biggest balance)')),
    ('S06', 'climb', 'line', dict(dur=1.8, slope=0.7, x0=900, x1=1200, what='the rate climbs above 9% (amber)')),
    ('S06', 'climb', 'line', dict(dt=2.0, t1=('S06', 'dry'), slope=-0.8, x0=1300, x1=1300, id_='S06.drain.line', what='the jar drains while the rate stays above 9%')),
    ('S06', 'years', 'bar', dict(dur=0.8, v=0.55, x=1300, what='the costlier block under the jar grows')),
    ('S06', 'cutFall', 'line', dict(dt=0.4, dur=2.2, slope=-0.4, x0=700, x1=1200, what='falling stretch (Aug 1981): the bead stays under the line')),
    ('S06', 'cutFall', 'bar', dict(dt=2.4, dur=1.4, v=0.9, x=1300, id_='S06.fall.jar', what='the jar keeps filling')),
    # S07: the ridge, its peak, the two rides, the best start, the 753 cells
    ('S07', 'ridge', 'line', dict(dur=2.4, slope=0.4, x0=200, x1=1720, what='the whole T-bill ridge (1954 to today)')),
    ('S07', 'peak', 'dot', dict(y=240, x=880, what='the summit: 16.3%, May 1981')),
    ('S07', 'rideL', 'line', dict(dur=2.6, slope=0.7, x0=400, x1=800, what='left frame: the bead climbs above the rail (amber)')),
    ('S07', 'rideL', 'line', dict(dt=2.8, dur=1.6, slope=-0.7, x0=600, x1=600, id_='S07.drainL.line', what='its jar drains')),
    ('S07', 'rideL', 'bar', dict(dt=4.5, dur=0.7, v=0.55, x=600, id_='S07.blockL.bar', what='a costlier block grows under it')),
    ('S07', 'rideR', 'line', dict(dur=2.4, slope=-0.5, x0=1150, x1=1500, what='right frame: the bead sinks under the rail')),
    ('S07', 'rideR', 'bar', dict(dt=2.4, dur=1.2, v=0.85, x=1350, id_='S07.jarR.bar', what='its jar fills high')),
    ('S07', 'best', 'dot', dict(y=420, x=1300, what='August 1981 (best start): the jar full')),
    ('S07', 'cells', 'roll', dict(dur=2.2, n=24, red=(0.284, 0.035), x0=300, x1=1620, what='the 753 start cells appear under the ridge (red = costlier)')),
    ('S07', 'worst', 'dot', dict(y=720, x=640, what='ring moves to the worst cell (left half)')),
    # S08 KEY-6: the worst ride, the cushion gone, the coin piles and the 43% block, the cap lowering
    ('S08', 'ride', 'line', dict(t1=('S08', 'grows'), t1dt=0.4, slope=0.4, x0=400, x1=700, what='the bead starts riding the steep climb; the jar fills a little')),
    ('S08', 'grows', 'line', dict(dt=0.6, t1=('S08', 'peak'), slope=0.9, x0=700, x1=1300, what='the rate climbs to 19.3%, years above the rail')),
    ('S08', 'peak', 'dot', dict(y=160, x=1300, what='19.3% at the top')),
    ('S08', 'peak', 'line', dict(dt=1.5, t1=('S08', 'gone'), t1dt=-0.5, slope=-0.75, x0=1500, x1=1500, step=0.5, id_='S08.drain.line', what='the jar empties')),
    ('S08', 'coins', 'bar', dict(dur=1.0, v=0.55, x=700, what='interest pile (fixed) rises: $26,005')),
    ('S08', 'coins', 'bar', dict(dt=0.2, dur=1.0, v=0.55, x=1200, id_='S08.coins.bar2', what='interest pile (variable) rises')),
    ('S08', 'extra', 'bar', dict(dur=0.9, v=0.8, x=1200, what='a red block grows on the variable pile: 43% of the fixed pile')),
    ('S08', 'cap', 'line', dict(dur=2.0, slope=-0.5, x0=1200, x1=1200, what='the rate cap lowers; the red block shrinks (15%, then 12% cap)')),
    # S09 KEY-7: the gap opens, red columns shorten; 2 points (right empty, 20.4% left); 3 points (10.5% left)
    ('S09', 'hold', 'line', dict(t1=('S09', 'moving'), slope=-0.4, x0=960, x1=960, what='the head-start gap opens 0 -> 1 point; red columns shorten')),
    ('S09', 'leah', 'line', dict(dur=0.6, slope=-0.3, x0=960, x1=960, what='gap opens to 1.5 points (Leah)')),
    ('S09', 'two', 'line', dict(dur=0.6, slope=-0.6, x0=1100, x1=1360, what='gap 2 points: the right column empties')),
    ('S09', 'early20', 'bar', dict(dur=0.5, v=share(0.204), x=L, what='left column (1954-1980) at 2 points: 20.4% red')),
    ('S09', 'three', 'line', dict(dur=1.2, slope=-0.4, x0=960, x1=960, what='gap 2 -> 3 points: left column shrinks')),
    ('S09', 'tenfive', 'bar', dict(dur=0.5, v=share(0.105), x=L, what='left column at 3 points: 10.5% red')),
    # S10.1: the start point jumps 1 -> 0 -> -1 point, the red columns jump up (one share each, held); S10.2 jumps back to 3 points
    ('S10', 'j1', 'bar', dict(dur=0.35, v=share(0.313), x=C, what='1 point: red columns jump up, 31.3% of all starts')),
    ('S10', 'j0', 'bar', dict(dur=0.35, v=share(0.579), x=C, what='0 points: 57.9% of all starts')),
    ('S10', 'jm', 'bar', dict(dur=0.35, v=share(0.729), x=C, what='-1 point (reversed): 72.9% of all starts')),
    ('S10', 'back', 'bar', dict(dur=0.35, v=share(0.045), x=C, what='jump back to 3 points: red columns drop')),
    ('S10', 'april', 'dot', dict(y=720, x=L, what='ring on the left red layer: April 1977')),
    ('S10', 'early', 'line', dict(dur=1.6, slope=-0.3, x0=L, x1=L, what='2 -> 3 points: left column shrinks but keeps red')),
    # S12: K7 at Leah's 1.5 points
    ('S12', 'leah', 'dot', dict(dt=0.3, y=690, x=C, what="K7 at Leah's 1.5 points")),
]


def main():
    plan, ev = [], {'fps': FPS, 'bar': [], 'line': [], 'dot': []}
    for sc, aid, kind, p in PLAN:
        t0 = A[(sc, aid)] + p.get('dt', 0.0)
        t1 = A[p['t1']] + p.get('t1dt', 0.0) if 't1' in p else t0 + p.get('dur', 0.0)
        t1 = min(t1, SCENE_END[sc] - 0.05)
        eid = p.get('id_') or f'{sc}.{aid}.{kind}'
        row = {'id': eid, 'scene': sc, 'anchor': aid, 'kind': kind, 't0': round(t0, 3), 't1': round(max(t1, t0), 3), 'what': p['what']}
        if kind == 'line':
            f0, f1 = int(round(t0 * FPS)), max(int(round(t1 * FPS)), int(round(t0 * FPS)) + 2)
            row.update(slope=p.get('slope', 0.0), x0=p['x0'], x1=p['x1'], wobble=bool(p.get('wobble')), step=p.get('step'))
            for f in range(f0, f1):
                u = (f - f0) / max(1, f1 - f0 - 1)
                s = 0.8 * math.sin(2 * math.pi * u * 2.5) if p.get('wobble') else p['slope']
                ev['line'].append({'f': f, 'id': eid, 'slope': round(s, 3), 'x': round(p['x0'] + u * (p['x1'] - p['x0']), 1)})
        elif kind == 'bar':
            row.update(v=p['v'], x=p['x'])
            ev['bar'].append({'id': eid, 'f0': int(round(t0 * FPS)), 'f1': int(round(t1 * FPS)), 'value': p['v'], 'x': p['x']})
        elif kind == 'dot':
            row.update(y=p['y'], x=p['x'])
            ev['dot'].append({'f': int(round(t0 * FPS)), 'id': eid, 'y': p['y'], 'x': p['x']})
        elif kind == 'roll':
            n = p['n']
            vs = cells(n, *p['red']) if 'red' in p else [ridge(k / max(1, n - 1)) for k in range(n)]
            row.update(n=n, accel=bool(p.get('accel')))
            items = []
            for k in range(n):
                u = k / max(1, n - 1)
                w = (k + 1) / n
                tk = t0 + (t1 - t0) * (math.sqrt(w) if p.get('accel') else w) if n > 1 else t0
                x = p.get('x', p['x0'] + u * (p['x1'] - p['x0']))
                items.append({'t': round(tk, 3), 'v': round(vs[k], 3), 'x': round(x, 1)})
                ev['bar'].append({'id': f'{eid}.{k + 1}', 'f0': int(round(tk * FPS)), 'f1': int(round(tk * FPS)) + 3, 'value': round(vs[k], 3), 'x': round(x, 1)})
            row['items'] = items
        plan.append(row)
    for k in ('bar', 'line', 'dot'):
        ev[k].sort(key=lambda e: e.get('f0', e.get('f')))
    ev['_about'] = ('Data-sound events of the C5 picture of Tập 2 (frame at 30 fps where each sound starts), from the picture anchors '
                    '(animatic/src/anchors, resolved on animatic/timing.json) by audio_src/events.py. bar: f0..f1 growth, value = one pitch scale for the film '
                    '(0..1 -> MIDI 36..60; red shares as 0.3 + share); line: every frame of a draw or a slide (slope at the tip; wobble = the variable path '
                    'crossing the 9% line); dot: frame it appears, y on screen. Palette S2 "minimal" (sổ gu G-005 · chọn), as Tập 1.')
    json.dump(ev, open(os.path.join(EP, 'out', 'sonify-events.json'), 'w'), indent=1)
    os.makedirs(os.path.join(EP, 'work', 'audio'), exist_ok=True)
    json.dump({'_about': 'Sonification plan (renderer input), one row per data action; see audio_src/events.py', 'timingTotal': TM['total_s'], 'rows': plan},
              open(os.path.join(EP, 'work', 'audio', 'son-plan.json'), 'w'), indent=1, ensure_ascii=False)
    print(len(plan), 'actions;', {k: len(ev[k]) for k in ('bar', 'line', 'dot')})


if __name__ == '__main__':
    main()
