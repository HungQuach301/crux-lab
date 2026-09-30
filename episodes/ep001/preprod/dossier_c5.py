"""Episode 1 (C5, stream D): release dossier from the final script and timing. Never edits a number: every figure comes from
out/script.json (preprod/script_from_v32.py) and out/claims.json (build.py).

    python3 episodes/ep001/preprod/dossier_c5.py [--method-card START END] [--end-screen START END]

Writes out/timeline.json, out/captions.srt, out/adbreaks.json, out/transitions.json, out/tension-map.json + .png, preprod/shotlist.json,
out/package/description.md. Thumbnails: preprod/thumbs_c5.js (Playwright). Re-run after:
  - the final render (P): in-scene cuts come from animatic/anchors.json ("cắt H1→H3" actions); if P adds a method card / end screen after
    S20, pass its window (--method-card, --end-screen): the acts then become act3 = S14–S20, method = card, outro = end screen;
  - the final mix (A): musicLevel / audioDensity of the tension map are measured from out/audio/stems/*.wav when they exist
    (otherwise planned from the tension curve and the script, marked "planned").

Acts (beats-v3.md sequences; checks/CONTRACT.md order cold-open, ident, act1, act2, act3, method, outro):
  cold-open S01–S02 · act1 S03–S08 · act2 S09–S13 · act3 S14–S18 · method S19 (limits: national averages, median bills, made-up
  borrowers, what changes the math) · outro S20 (the question for the viewer, 29 s). The video has no ident (C4: none rendered);
  the timeline does not invent one.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, '..'))
P = lambda *p: os.path.join(EP, *p)
J = lambda *p: json.load(open(P(*p), encoding='utf-8'))


def dump(obj, *p):
    os.makedirs(os.path.dirname(P(*p)), exist_ok=True)
    json.dump(obj, open(P(*p), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


# per scene: layout family/variant, shot size, chart, camera (2.5D), from the animatic README table and design/c3/final/system.md §7
SCENE = {
    'S01': ('line/window-low', 'wide', 'line', 'H3→H1→H3', 'The week rates bottomed'),
    'S02': ('letter/offer', 'close', 'letter', 'H1', 'The letter, and the promise'),
    'S03': ('line/peak-2023', 'wide', 'line', 'H3→H1', 'Near the top'),
    'S04': ('object/loan-file', 'medium', 'card', 'H1', 'Nora'),
    'S05': ('line/window', 'wide', 'line', 'H3', 'The window, and the one-point line'),
    'S06': ('letter/new-rate', 'close', 'ruler', 'H1→H3→H1', 'The offer'),
    'S07': ('letter/bill', 'close', 'scatter', 'H1→H3', 'The bill'),
    'S08': ('split/two-answers', 'wide', 'ruler', 'H3', 'Two answers'),
    'S09': ('stack/break-even', 'medium', 'stack', 'H1', 'What break-even means'),
    'S10': ('stack/balance-gap', 'medium', 'stack', 'H3→H1', 'Starting the clock over'),
    'S11': ('plot/never', 'wide', 'line', 'H3', 'A quarter point'),
    'S12': ('plot/full-point', 'wide', 'line', 'H3', 'A full point'),
    'S13': ('ruler/half-point', 'wide', 'ruler', 'H3', 'Half a point'),
    'S14': ('house/walt', 'medium', 'stack', 'H1', 'Walt'),
    'S15': ('bars/bill-shrinks', 'medium', 'bar', 'H3→H1', 'The bill barely shrinks'),
    'S16': ('stack/walt-3y', 'medium', 'ruler', 'H1→H3', 'If Walt sells after three years'),
    'S17': ('house/anjali', 'medium', 'stack', 'H1→H3', 'Anjali'),
    'S18': ('ruler/three-marks', 'wide', 'bar', 'H1→H3', 'A line for each loan size'),
    'S19': ('band/fee-range', 'wide', 'band', 'H3', 'What this does not tell you'),
    'S20': ('house/horizon', 'wide', 'stack', 'H1', 'The question that stays with you'),
}
ACT = {**{s: 'cold-open' for s in ('S01', 'S02')}, **{f'S{i:02d}': 'act1' for i in range(3, 9)}, **{f'S{i:02d}': 'act2' for i in range(9, 14)},
       **{f'S{i:02d}': 'act3' for i in range(14, 19)}, 'S19': 'method', 'S20': 'outro'}
# scene cut -> how it joins (for out/transitions.json: match and reason)
JOIN = {
    'S02': ('semantic', 'rate back above 7% -> the letter it brings'),
    'S03': ('semantic', 'the promise -> how Nora got here: the 2023 rate line'),
    'S04': ('semantic', 'one of the lit houses on the street -> Nora\'s house'),
    'S05': ('semantic', 'her loan file -> the rate line since she borrowed'),
    'S06': ('semantic', 'the window closed -> the letter arrives in a different world'),
    'S07': ('geometric', 'same letter, camera continues down to the last line'),
    'S08': ('semantic', 'the bill -> the question: is it worth paying?'),
    'S09': ('semantic', 'act boundary (ad break): back to the letter'),
    'S10': ('geometric', 'same stack of savings; the clock and balances join it'),
    'S11': ('semantic', 'the gap matters more for a smaller cut -> a quarter point'),
    'S12': ('geometric', 'same plot; the marker slides to a full point'),
    'S13': ('geometric', 'same scale; the marker slides to half a point'),
    'S14': ('semantic', 'act boundary (ad break): is half a point the line for everyone? -> Walt'),
    'S15': ('semantic', 'his bill is only a little smaller -> loans and bills side by side'),
    'S16': ('semantic', 'break-even in month 75 -> what if he sells after three years'),
    'S17': ('semantic', 'the small end -> the other end: Anjali'),
    'S18': ('semantic', 'the three borrowers -> back to the letter and the answer'),
    'S19': ('geometric', 'same frame; the three columns recede into the band of real bills'),
    'S20': ('semantic', 'the limits -> the one number only the viewer knows'),
}
# planned tension per scene (beats-v3.md emotional line), with the three act climaxes as peaks
TENSION = {'S01': 0.55, 'S02': 0.62, 'S03': 0.42, 'S04': 0.30, 'S05': 0.50, 'S06': 0.36, 'S07': 0.50, 'S08': 0.62, 'S09': 0.34,
           'S10': 0.62, 'S11': 0.78, 'S12': 0.42, 'S13': 0.55, 'S14': 0.46, 'S15': 0.60, 'S16': 0.72, 'S17': 0.44, 'S18': 0.62,
           'S19': 0.40, 'S20': 0.34}
CLIMAX = {'act1': ('S08', 'Neither is quite right.', 0.86), 'act2': ('S11', 'Counting it, the fees never come back', 0.95),
          'act3': ('S16', 'So that is why a smaller mortgage needs a bigger rate cut.', 0.90)}
TURNS = [('S05', 'After the week ending', 'the one-point window closed (history, US only)'),
         ('S08', 'Neither is quite right.', 'act 1 turn: neither quick answer is right'),
         ('S10', 'Count it, and break-even moves', 'act 2 turn: counting what she still owes moves break-even from 24 to 30 months'),
         ('S11', 'Counting it, the fees never come back', 'act 2 climax: at a quarter point the fees never come back'),
         ('S13', 'So for Nora, the answer is half a point', 'answer for Nora: half a point'),
         ('S15', 'In the 2025 data, refinance bills grow', 'act 3 turn: the bill barely shrinks with the loan'),
         ('S16', 'So that is why a smaller mortgage', 'answer to the promise: a smaller mortgage needs a bigger cut'),
         ('S18', 'It depends on the size of the loan.', 'the answer: a line for each loan size'),
         ('S20', 'How long do you picture yourself', 'the question left with the viewer')]


def fmt_t(t):
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    ms = int(round((s - int(s)) * 1000))
    s = int(s)
    if ms == 1000:
        s, ms = s + 1, 0
    return f'{int(h):02d}:{int(m):02d}:{s:02d},{ms:03d}'


def sentence_at(sents, scene, prefix):
    return next(s for s in sents if s['scene'] == scene and s['text'].startswith(prefix))


def captions(sents):
    """Cues of <= 2 lines x <= 42 chars, 1.0-7.0 s, no overlap; text joined = script text (F09). Splits at spaces only."""
    def lines_of(words):
        out, cur = [], ''
        for w in words:
            if cur and len(cur) + 1 + len(w) > 42:
                out.append(cur)
                cur = w
            else:
                cur = (cur + ' ' + w).strip()
        out.append(cur)
        return out

    cues = []
    for s in sents:
        words = s['text'].split()
        dur = s['end'] - s['start']
        total_c = len(s['text'])

        def split(k):
            # k chunks of balanced length (greedy on cumulative characters), splitting at spaces only
            out, cur, acc = [], [], 0
            for i, w in enumerate(words):
                cur.append(w)
                acc += len(w) + 1
                goal = total_c * (len(out) + 1) / k
                soft = w[-1] in ',:;—' and acc >= 0.75 * goal and len(' '.join(cur)) <= 84  # prefer a break at punctuation
                if len(out) < k - 1 and (acc >= goal or soft) and len(words) - i - 1 >= k - 1 - len(out):
                    out.append(cur)
                    cur = []
            out.append(cur)
            return [c for c in out if c]

        k = 1
        while True:
            chunks = split(k)
            n = sum(len(' '.join(c)) for c in chunks)
            ok = all(len(lines_of(c)) <= 2 for c in chunks) and all(dur * len(' '.join(c)) / n <= 7.0 for c in chunks)
            if ok or k >= len(words):
                break
            k += 1
        t = s['start']
        for c in chunks:
            d = dur * len(' '.join(c)) / n
            cues.append({'start': t, 'end': t + d, 'lines': lines_of(c), 'sid': s['id']})
            t += d
    # durations: split cues longer than 7 s at a line break, extend cues shorter than 1 s into free time
    out = []
    for c in cues:
        if c['end'] - c['start'] > 7.0 and len(c['lines']) == 2:
            a, b = c['lines']
            m = c['start'] + (c['end'] - c['start']) * len(a) / (len(a) + len(b))
            out += [{**c, 'end': m, 'lines': [a]}, {**c, 'start': m, 'lines': [b]}]
        else:
            out.append(c)
    for i, c in enumerate(out):
        if c['end'] - c['start'] < 1.0:
            nxt = out[i + 1]['start'] if i + 1 < len(out) else c['start'] + 10
            c['end'] = min(c['start'] + 1.0, nxt)
            if c['end'] - c['start'] < 1.0:
                prv = out[i - 1]['end'] if i else 0.0
                c['start'] = max(prv, c['end'] - 1.0)
    for a, b in zip(out, out[1:]):
        assert b['start'] >= a['end'] - 1e-6, (a, b)
    for c in out:
        assert 1.0 - 1e-6 <= c['end'] - c['start'] <= 7.0 + 1e-6, c
        assert len(c['lines']) <= 2 and all(len(l) <= 42 for l in c['lines']), c
    return out


def main():
    args = sys.argv[1:]
    win = lambda k: (float(args[args.index(k) + 1]), float(args[args.index(k) + 2])) if k in args else None
    card, endscr = win('--method-card'), win('--end-screen')
    T = J('animatic', 'timing.json')
    sents = J('out', 'script.json')['sentences']
    fps = T['fps']
    scenes = [{'id': s['id'], 'start': s['start'], 'end': s['end']} for s in T['scenes']]
    total = scenes[-1]['end']
    act = dict(ACT)
    extra = []
    if card:
        for k in ('S19', 'S20'):
            act[k] = 'act3'
        extra.append({'id': 'S21', 'start': card[0], 'end': card[1], 'act': 'method', 'layout': 'card/method', 'shot': 'wide', 'chart': 'card', 'look': 'H3',
                      'title': 'Method card'})
        total = card[1]
    if endscr:
        extra.append({'id': 'S22', 'start': endscr[0], 'end': endscr[1], 'act': 'outro', 'layout': 'card/end-screen', 'shot': 'wide', 'chart': 'card', 'look': 'H3',
                      'title': 'End screen'})
        total = endscr[1]
    # ---- in-scene hard cuts (H1 <-> H3) from the anchor table the render reads
    anchors = J('animatic', 'anchors.json')['anchors']
    inner = [(a['scene'], a['resolved_s'], a['action']) for a in anchors if a['action'].startswith('cắt')]
    sc_start = {s['id']: s['start'] for s in scenes}
    inner = [(sc, t, a) for sc, t, a in inner if t - sc_start[sc] > 0.5]
    # ---- timeline
    rows = []
    for s in scenes:
        lay, shot, chart, look, title = SCENE[s['id']]
        rows.append({'id': s['id'], 'act': act[s['id']], 'start': s['start'], 'dur': round(s['end'] - s['start'], 3), 'layout': lay, 'shot': shot, 'panels': ['*'],
                     'chart': chart, 'move': 0.0 if look == 'H3' else 2.0, 'look': look, 'title': title})
    for e in extra:
        rows.append({'id': e['id'], 'act': e['act'], 'start': e['start'], 'dur': round(e['end'] - e['start'], 3), 'layout': e['layout'], 'shot': e['shot'], 'panels': ['*'],
                     'chart': e['chart'], 'move': 0.0, 'look': e['look'], 'title': e['title']})
    acts = []
    for r in rows:
        if acts and acts[-1]['id'] == r['act']:
            acts[-1]['end'] = round(r['start'] + r['dur'], 3)
        else:
            acts.append({'id': r['act'], 'start': r['start'], 'end': round(r['start'] + r['dur'], 3)})
    for a in acts:
        if a['id'] in CLIMAX:
            sc, pre, _ = CLIMAX[a['id']]
            a['climax'] = sentence_at(sents, sc, pre)['start']
    turns = [{'t': sentence_at(sents, sc, pre)['start'], 'scene': sc, 'what': what} for sc, pre, what in TURNS]
    dump({'fps': fps, 'total': total, 'acts': acts, 'scenes': rows, 'turns': turns,
          'source': 'animatic/timing.json (final sentence times, 591.72 s narration) + preprod/dossier_c5.py; scenes cut 0.35 s before their first sentence',
          'note': 'no ident in the render (none at C4); move = seconds of camera push at the start (H1 slow push <= 20 px/s, H3 static); out/camera.json (P) overrides it'},
         'out', 'timeline.json')
    # ---- ad breaks: the two act boundaries of beats-v3.md (after S08, after S13), inside the silence between the scenes
    br = [next(a['start'] for a in acts if a['id'] == 'act2'), next(a['start'] for a in acts if a['id'] == 'act3')]
    for b in br:
        prev = max(s['end'] for s in sents if s['end'] <= b)
        nxt = min(s['start'] for s in sents if s['start'] >= b)
        assert nxt - prev >= 1.0, (b, prev, nxt)
    dump({'breaks': br, 'why': 'act boundaries of beats-v3.md: end of act 1 (after S08 "And the division leaves something out.") and end of act 2 (after S13 '
                               '"Is half a point the line for everyone?"); each sits in the >= 1.4 s voice gap at the scene cut. The mix must leave >= 1 s under -40 dBFS there (S14)'},
         'out', 'adbreaks.json')
    # ---- transitions
    cuts = []
    for s in scenes[1:]:
        m, why = JOIN[s['id']]
        prev = [x for x in scenes if x['end'] == s['start']][0]['id']
        cuts.append({'t': s['start'], 'from': prev, 'to': s['id'], 'type': 'cut', 'match': m, 'audio': None, 'reason': why})
    for sc, t, a in inner:
        frm, to = ('H1', 'H3') if 'H1→H3' in a else ('H3', 'H1')
        cuts.append({'t': round(t, 3), 'from': f'{sc}/{frm}', 'to': f'{sc}/{to}', 'type': 'cut', 'match': 'semantic', 'audio': None,
                     'reason': 'change of scale inside the scene (market <-> one household), design/c3/final/system.md "cắt"'})
    for e in extra:
        cuts.append({'t': e['start'], 'from': 'S20' if e['id'] == 'S21' else 'S21', 'to': e['id'], 'type': 'dissolve', 'match': None, 'audio': None,
                     'reason': 'story ends; text card follows'})
    cuts.sort(key=lambda c: c['t'])
    dump({'cuts': cuts, 'source': 'scene cuts from animatic/timing.json; in-scene H1<->H3 cuts from animatic/anchors.json (actions "cắt"). audio = null: '
                                  'J/L cuts are the mix\'s (stream A) and are not claimed here'}, 'out', 'transitions.json')
    # ---- captions
    cues = captions(sents)
    with open(P('out', 'captions.srt'), 'w', encoding='utf-8') as f:
        for i, c in enumerate(cues, 1):
            f.write(f"{i}\n{fmt_t(c['start'])} --> {fmt_t(c['end'])}\n" + '\n'.join(c['lines']) + '\n\n')
    # ---- tension map
    tension_map(rows, acts, sents, cuts, total)
    # ---- shot list
    shotlist(rows, inner)
    # ---- description + chapters
    description(rows, total)
    print(f'timeline: {len(rows)} scenes, acts {[a["id"] for a in acts]}; {len(cuts)} cuts; {len(cues)} caption cues; breaks {br}; total {total}')


def tension_map(rows, acts, sents, cuts, total):
    import numpy as np
    pts = []
    for r in rows:
        v = TENSION.get(r['id'], 0.3)
        pts.append((r['start'] + 0.5 * r['dur'], v))
    peaks, valleys = [], []
    for a in acts:
        if a.get('climax') is not None:
            v = CLIMAX[a['id']][2]
            pts.append((a['climax'], v))
            peaks.append(a['climax'])
    pts.sort()
    # valleys: the lowest control point within 45 s after each peak
    for p in peaks:
        after = [(t, v) for t, v in pts if p < t <= p + 45]
        valleys.append(min(after, key=lambda x: x[1])[0])
    ts = np.arange(0.0, math.floor(total) + 1.0, 1.0)
    ten = np.interp(ts, [0.0] + [t for t, _ in pts] + [total], [pts[0][1]] + [v for _, v in pts] + [pts[-1][1]])
    # snap peaks/valleys to the sample grid maxima/minima
    peaks = [float(ts[np.argmin(abs(ts - p))]) for p in peaks]
    valleys = [float(ts[np.argmin(abs(ts - v))]) for v in valleys]
    ct = np.array([c['t'] for c in cuts])
    cut_rate = [int(np.sum((ct > t - 5) & (ct <= t + 5))) for t in ts]
    # audio: measured from the stems when the mix exists, else planned
    stems = {n: P('out', 'audio', 'stems', f'{n}.wav') for n in ('voice', 'music', 'sfx', 'whoosh')}
    measured = all(os.path.exists(p) for p in stems.values())
    if measured:
        import soundfile as sf
        lv = {}
        for n, p in stems.items():
            x, sr = sf.read(p, always_2d=True)
            x = x.mean(axis=1)
            lv[n] = np.array([20 * np.log10(np.sqrt(np.mean(x[int(max(0, t - 0.5) * sr):int((t + 0.5) * sr)] ** 2)) + 1e-9) for t in ts])
        music = lv['music']
        act_n = sum((lv[n] > -45).astype(float) for n in lv)
        dens = np.convolve(act_n, np.ones(5) / 5, mode='same')
    else:
        speaking = np.array([any(s['start'] <= t <= s['end'] for s in sents) for t in ts], float)
        music = -34.0 + 14.0 * ten
        dens = np.convolve(1.0 + speaking + (ten > 0.5), np.ones(5) / 5, mode='same')
    samples = [{'t': float(t), 'cutRate': c, 'audioDensity': round(float(d), 3), 'musicLevel': round(float(m), 2), 'tension': round(float(v), 3)}
               for t, c, d, m, v in zip(ts, cut_rate, dens, music, ten)]
    dump({'samples': samples, 'peaks': [{'t': p} for p in peaks], 'valleys': [{'t': v} for v in valleys],
          'audio': 'measured from out/audio/stems (1 s RMS dB; stems above -45 dBFS, 5 s mean)' if measured else
                   'planned (no stems yet): musicLevel = -34 + 14 x tension dB, audioDensity = voice + music + 1 when tension > 0.5; re-run after the mix (stream A)',
          'tension': 'planned: beats-v3.md emotional line per scene (midpoints) + act climaxes (timeline acts[].climax); linear between points',
          'cutRate': 'cuts per 10 s window from out/transitions.json'}, 'out', 'tension-map.json')
    # png
    from PIL import Image, ImageDraw
    W, H, L, R, TOP, BOT = 1600, 500, 60, 20, 30, 60
    im = Image.new('RGB', (W, H), '#0e1116')
    d = ImageDraw.Draw(im)
    X = lambda t: L + (W - L - R) * t / total
    Y = lambda v: TOP + (H - TOP - BOT) * (1 - v)
    for a in acts:
        d.line([(X(a['start']), TOP), (X(a['start']), H - BOT)], fill='#2a303b', width=1)
        d.text((X(a['start']) + 4, H - BOT + 8), a['id'], fill='#9aa4b2')
    cmax = max(cut_rate) or 1
    d.line([(X(t), Y(c / cmax * 0.3)) for t, c in zip(ts, cut_rate)], fill='#2a303b', width=2)
    mm = (music - music.min()) / (music.max() - music.min() + 1e-9)
    d.line([(X(t), Y(0.1 + 0.8 * m)) for t, m in zip(ts, mm)], fill='#4c8dff', width=1)
    d.line([(X(t), Y(v)) for t, v in zip(ts, ten)], fill='#f2f4f7', width=3)
    for p in peaks:
        v = float(np.interp(p, ts, ten))
        d.ellipse([X(p) - 6, Y(v) - 6, X(p) + 6, Y(v) + 6], fill='#e5484d')
    for p in valleys:
        v = float(np.interp(p, ts, ten))
        d.ellipse([X(p) - 6, Y(v) - 6, X(p) + 6, Y(v) + 6], fill='#3fbf7f')
    for m in range(0, int(total) + 1, 60):
        d.text((X(m) - 8, H - 24), f'{m // 60}:00', fill='#9aa4b2')
    d.text((L, 6), 'Tension (white), music level (blue, ' + ('measured' if measured else 'planned') + '), cut rate (grey); peaks red, valleys green', fill='#f2f4f7')
    im.save(P('out', 'tension-map.png'))


def shotlist(rows, inner):
    shots = []
    for r in rows:
        cuts = sorted(t for sc, t, a in inner if sc == r['id'])
        looks = r['look'].split('→')
        bounds = [r['start']] + cuts + [r['start'] + r['dur']]
        for k in range(len(bounds) - 1):
            look = looks[min(k, len(looks) - 1)]
            h1 = look == 'H1'
            shots.append({'id': f'sh{len(shots) + 1:03d}', 'scene': r['id'], 'act': r['act'], 'start': round(bounds[k], 3), 'dur': round(bounds[k + 1] - bounds[k], 3),
                          'look': look, 'layout': r['layout'], 'size': r['shot'] if k == 0 or not h1 else 'medium',
                          'move': 'slow push-in' if h1 else 'static',
                          'moveReason': ('a slow push toward the object that carries the number keeps attention on it without a new shot' if h1 else
                                         'the chart is read against its fixed scale, so the frame holds still while the marks move')})
    dump({'source': 'out/timeline.json + animatic/anchors.json (in-scene H1<->H3 cuts); 2.5D: no simulated focal length, no 3D camera angle',
          'shots': shots}, 'preprod', 'shotlist.json')


def description(rows, total):
    # chapters: scene starts (floored to the second), grouped so every chapter >= 10 s; titles are working titles (owner picks the wording)
    CH = [('S01', 'The week rates bottomed'), ('S03', 'How Nora got here'), ('S06', 'The offer and the bill'), ('S08', 'Two quick answers'),
          ('S09', 'The 30-year clock'), ('S11', 'A quarter point, a full point, half a point'), ('S14', 'Walt: a smaller loan'), ('S17', 'Anjali: a bigger loan'),
          ('S18', 'A line for each loan size'), ('S19', 'What this does not tell you'), ('S20', 'How long will you stay?')]
    start = {r['id']: r['start'] for r in rows}
    ch = [(0 if sc == 'S01' else int(math.floor(start[sc])), t) for sc, t in CH]
    lens = [b[0] - a[0] for a, b in zip(ch, ch[1:])] + [total - ch[-1][0]]
    assert ch[0][0] == 0 and min(lens) >= 10, lens
    chap = '\n'.join(f'{s // 60}:{s % 60:02d} {t}' for s, t in ch)
    text = f"""<!-- out/package/description.md · generated by preprod/dossier_c5.py (stream D, C5). Title and wording are working drafts: the owner picks (see options.md). -->

In February 2026 the average 30-year mortgage rate in the US fell to 5.98%. By late September it was back above 7%. If a refinance offer has reached you since, this video walks through the math behind it with three illustrative borrowers, Nora, Walt and Anjali, built from typical 2025 figures.

How big a rate cut makes a refinance pay back its fees? The usual answers are a one-point rule of thumb, or dividing the fees by the monthly saving. We count one more thing: a new 30-year loan pays down what you owe more slowly than the old one would have. With that counted, the cut needed depends on the size of the loan.

Chapters
{chap}

What this is and is not
- History, not a forecast. US only. Not advice: the borrowers are illustrative, and a real rate, a real bill and a real balance will be different.
- Every dollar amount is in dollars of the day (not adjusted for inflation).
- Assumptions: the offer matches the national average rate for the week ending September 24, 2026; the old loan was taken out at the October 2023 average; fees are the 2025 median bill and are paid in cash at closing; the new loan is a 30-year fixed; "worth it" means the fees come back within three years (a test we chose, not a rule).

Sources
- Mortgage rates: Freddie Mac Primary Mortgage Market Survey, 30-year fixed, weekly (MORTGAGE30US). Source: Freddie Mac via FRED, Federal Reserve Bank of St. Louis. https://fred.stlouisfed.org/series/MORTGAGE30US
- Refinance bills and loan sizes: Home Mortgage Disclosure Act data, 2025 (total loan costs of rate-and-term refinances). Source: CFPB HMDA. https://ffiec.cfpb.gov/data-browser/
- Conforming loan limits: FHFA.

Music and data sounds are generated in code for this video. Narration: synthetic voice (ElevenLabs).
"""
    os.makedirs(P('out', 'package'), exist_ok=True)
    open(P('out', 'package', 'description.md'), 'w', encoding='utf-8').write(text)


if __name__ == '__main__':
    main()
