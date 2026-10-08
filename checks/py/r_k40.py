"""K4.0 (lô checks-appeal nhóm 2, chỉ thêm luật; D-008 §2). Mỗi luật ghi mục khiếu nại nguồn (checks-appeal A13–A26).
Không luật cũ nào đọc file này; luật ở đây không đổi định nghĩa, ngưỡng hay cấp của luật cũ."""
import re

from common import Missing, canon, canon_matches, metric, numbers_in_text, rule, spoken_numbers, verdict


def _claim_usd(c):
    """Canonical $ values a claim stands for: its display (numbers_in_text) and, for a numeric value, usd:<value>."""
    out = [x for x, _ in numbers_in_text(str(c.get('display', '')))]
    v = c.get('value')
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        out.append(canon(v, 'usd'))
    return out


def _amounts(text, spoken=False):
    """Dollar amounts in a text: '$150', '$1.2 million' (digits) or 'a hundred fifty dollars' (spoken words)."""
    if spoken:
        return [(c, c) for c in spoken_numbers(text) if c.startswith('usd:')]
    out = [(c, s) for c, s in numbers_in_text(text) if c.startswith('usd:')]
    out += [(canon(float(m.group(1).replace(',', '')), 'usd'), m.group(0)) for m in re.finditer(r'(?<![$\d])(\d[\d,]*(?:\.\d+)?)\s+dollars?\b', text, re.I)]
    return out


def _page_texts(ctx):
    """Visible texts per page sample from the page sampler's text track (opacity > 0.5, on frame): [(t, scene, [text, …])]."""
    tt = ctx.json('out/checks/page.json').get('textTrack')
    if tt is None:
        raise Missing('out/checks/page.json: textTrack')
    return [(e['t'], e.get('scene'), [i.get('text') or '' for i in e.get('items', [])]) for e in tt]


# ---- A20 → S19 ------------------------------------------------------------------------------------------------------------------
@rule('S19', 'DX-H1, DX-H4 (claim-risk), checks-appeal A20', 'contract.json claims.forbiddenAmounts[{id, terms[], window?: "sentence"|"frame"|"both"}] (default both): '
      'amounts the episode has no source for (Tập 5: the PMI premium). A unit is one narration sentence (out/script.json text, and spoken read as words) or one '
      'page sample (every visible text together, page sampler text track). A unit violates when it holds a term (word match, case-insensitive) and a dollar amount '
      '($ digits or "<n> dollars") that equals no claim of out/claims.json with a source (display or value). No forbiddenAmounts declared = nothing to check',
      '0 units with a term and an unsourced dollar amount')
def s19_forbidden_amounts(ctx):
    fa = ctx.contract().get('claims', {}) or {}
    fa = fa.get('forbiddenAmounts') if isinstance(fa, dict) else None
    if not fa:
        return verdict('S19', [metric('units with an unsourced forbidden amount', 0, '<=', 0)], note='contract.json declares no claims.forbiddenAmounts: nothing to check')
    sourced = [x for c in ctx.claims() if c.get('source') for x in _claim_usd(c)]
    bad, units = [], 0
    for f in fa:
        terms = [re.compile(r'\b' + re.escape(t) + r'\b', re.I) for t in f.get('terms') or []]
        if not terms:
            raise Missing(f'contract.json: claims.forbiddenAmounts[{f.get("id")}].terms')
        win = f.get('window') or 'both'
        cand = []
        if win in ('sentence', 'both'):
            for s in ctx.sentences():
                cand.append(('sentence', s.get('id'), s.get('text') or '', _amounts(s.get('text') or '')))
                if s.get('spoken'):
                    cand.append(('sentence', s.get('id'), s['spoken'], _amounts(re.sub(r'\[[^\]]*\]', ' ', s['spoken']), spoken=True)))
        if win in ('frame', 'both'):
            for t, sc, texts in _page_texts(ctx):
                joined = ' · '.join(texts)
                cand.append(('frame', f'{t:.1f}s {sc}', joined, [a for tx in texts for a in _amounts(tx)]))
        for kind, uid, text, amts in cand:
            if not any(r.search(text) for r in terms):
                continue
            units += 1
            orphan = [s for c, s in amts if not canon_matches(c, sourced)]
            if orphan:
                bad.append({'id': f.get('id'), 'unit': kind, 'where': uid, 'amounts': orphan, 'text': text[:140]})
    # one sentence read twice (text + spoken) or one label over many samples is one finding
    seen, uniq = set(), []
    for b in bad:
        k = (b['id'], b['unit'], b['where'] if b['unit'] == 'sentence' else b['text'])
        if k not in seen:
            seen.add(k)
            uniq.append(b)
    return verdict('S19', [metric('units with an unsourced forbidden amount', len(uniq), '<=', 0)],
                   details=[{'unitsWithTerm': units}, *uniq[:20]])


# ---- A17 → S20 ------------------------------------------------------------------------------------------------------------------
# Same definition as the factory's gate (toolkit/factory/numbers_said.py, Mốc V B+2), re-written here: checks/ imports nothing from the builder.
_UNITS = r'(percent|years?|months?|dollars?|times|quarters?|points?|basis points)'
_NUMW = (r'(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|'
         r'twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|point|and|a|half|\d[\d,.]*)')
_SAID = re.compile(r'\b((?:' + _NUMW + r')(?:[\s-]+' + _NUMW + r')*)\s+' + _UNITS + r'\b', re.I)


def said_numbers(spoken):
    """Quantities WITH a unit in a normalised spoken line: [(value words, unit)]. Unit-less counts ("three buyers") and calendar years do not count."""
    out = []
    for m in _SAID.finditer(spoken):
        val = re.sub(r'^(?:(?:a|and)\s+)+', '', m.group(1).strip().lower())
        if not re.search(r'\d|zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|teen|ty|hundred|thousand|million|half', val):
            continue
        out.append((val, re.sub(r's$', '', m.group(2).lower()), f'{val} {m.group(2).lower()}'))
    return out


@rule('S20', 'DX-S7 (lời mang số), checks-appeal A17', 'out/script.json sentences in order, `spoken` (the normalised line sent to TTS; delivery tags [..] removed; '
      'text when no spoken). A said number = a quantity with a unit (percent, year, month, dollar, times, quarter, point, basis point); new = its (value, unit) '
      'pair not said in any earlier sentence of the episode. Count new said numbers per scene', '≤ 2 new said numbers in every scene')
def s20_said_per_scene(ctx):
    said, per = set(), {}
    for s in ctx.sentences():
        line = re.sub(r'\[[^\]]*\]\s*', '', s.get('spoken') or s.get('text') or '')
        r = per.setdefault(s.get('scene'), [])
        for val, unit, txt in said_numbers(line):
            if (val, unit) not in said:
                r.append({'said': txt, 'sentence': s.get('id')})
            said.add((val, unit))
    over = {sc: v for sc, v in per.items() if len(v) > 2}
    return verdict('S20', [metric('scenes with > 2 new said numbers', len(over), '<=', 0)],
                   details=[{'scene': sc, 'new': v} for sc, v in over.items()] + [{'perScene': {sc: len(v) for sc, v in per.items() if v}}])


# ---- world segments (D-010: episodes built as 3D world segments with a spine) --------------------------------------------------------
def world_segments(ctx):
    """[(id, spine, t0)] of the episode's world segments, times of the episode = spine time + t0. Declared in contract.json `world`
    [{id, spine, t0?}] or, failing that, in the builder's episode.yaml `world` [{id, dir}] (spine = <dir>/spine.json) with t0 from
    out/factory/splice.json segments (one segment without a splice file: t0 = 0). An episode without world segments = [] (rule not applicable)."""
    def get():
        import json
        import os
        decl = None
        try:
            decl = ctx.contract().get('world')
        except Missing:
            decl = None
        if not decl and ctx.has('episode.yaml'):
            import yaml
            y = yaml.safe_load(open(ctx.path('episode.yaml'), encoding='utf-8')) or {}
            decl = [{'id': w['id'], 'spine': os.path.join(w['dir'], 'spine.json')} for w in y.get('world') or [] if isinstance(w, dict) and w.get('dir')]
        if not decl:
            return []
        splice = {s['id']: s for s in ctx.json('out/factory/splice.json')['segments']} if ctx.has('out/factory/splice.json') else {}
        out = []
        for w in decl:
            t0 = w.get('t0')
            if t0 is None:
                if w['id'] in splice:
                    t0 = splice[w['id']]['t0']
                elif len(decl) == 1:
                    t0 = 0.0
                else:
                    raise Missing(f"t0 of world segment {w['id']} (contract.json world[].t0 or out/factory/splice.json)")
            out.append((w['id'], ctx.json(w['spine']), float(t0)))
        return out
    return ctx.memo(('world',), get)


def frame_diffs(ctx, w=320, h=180, fps=30, cut=False):
    """Change between consecutive frames of the master (scaled to 320×180 grey, 30 fps); index i = frame i (0 for frame 0). cut=False: mean absolute
    luma change; cut=True: share of pixels changing by > 25 levels (a hard cut is a share > 0.45). Both cached by video SHA."""
    import os
    import subprocess
    import numpy as np
    from common import sha256_file

    def get():
        cp = os.path.join(ctx.cache_dir, f'diff-{sha256_file(ctx.video())[:16]}-{w}x{h}-{fps}.npz')
        if os.path.exists(cp):
            z = np.load(cp)
            return z['mean'], z['cut']
        p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', ctx.video(), '-vf', f'fps={fps},scale={w}:{h},format=gray', '-f', 'rawvideo', '-'], stdout=subprocess.PIPE)
        mean, share, prev, n = [0.0], [0.0], None, w * h
        while True:
            b = p.stdout.read(n)
            if len(b) < n:
                break
            fr = np.frombuffer(b, np.uint8).astype(np.int16)
            if prev is not None:
                a = np.abs(fr - prev)
                mean.append(float(a.mean()))
                share.append(float((a > 25).mean()))
            prev = fr
        p.wait()
        z = (np.array(mean), np.array(share))
        np.savez(cp, mean=z[0], cut=z[1])
        return z
    return ctx.memo(('diffs', w, h, fps), get)[1 if cut else 0]


def _norm(w):
    return re.sub(r'[^\w]', '', str(w)).lower()


# ---- A14 → R07 ------------------------------------------------------------------------------------------------------------------
@rule('R07', 'DX-R (đồng bộ hình–lời), D-010 §6, checks-appeal A14', 'world segments (contract.json world / episode.yaml world + out/factory/splice.json). '
      'Picture: every spine visual cue (spine.visual_cues → beats[].cues, episode time = cue + t0) is located on the master: a label cue (spine.label_cues) at the first '
      'page sample from cue − 1 s where that label text is visible (page sampler text track); any other cue (or a label cue without a text track) at the first frame in '
      '[cue − 0.3 s, cue + 0.8 s] (window cut at camera moves of spine.moves) whose whole-frame luma change (320×180, 30 fps) rises past half of the window peak over the '
      'median of [cue − 0.7, cue − 0.15] s; a peak < 0.08 above it = not detected. Offset = located − cue. Voice: own ASR of the master (asr_master) matched in order to '
      'spine.words (next 6 tokens); offset = heard − aligned start. Toolkit/factory/world/sync_audit.py measured the same, without page ROIs (the checker has none)',
      '≥ 92% of visual cues within ±0.2 s (undetected = outside); |median voice offset| ≤ 0.2 s; no world segment = nothing to check')
def r07_sync(ctx):
    import numpy as np
    segs = world_segments(ctx)
    if not segs:
        return verdict('R07', [metric('visual cues within ±0.2 s (%)', 100.0, '>=', 92.0, '%')], note='no world segments: nothing to check')
    d = frame_diffs(ctx)
    tt = None
    if ctx.has('out/checks/page.json'):
        tt = ctx.json('out/checks/page.json').get('textTrack')
    from r_audio import asr_master
    heard = [(_norm(w['w']), w['start']) for w in asr_master(ctx)]
    vis, voice = [], []
    for sid, sp, t0 in segs:
        cues = {f"{b['id']}.{k}": t for b in sp.get('beats', []) for k, t in b.get('cues', {}).items()}
        moves = [(m['t0'] + t0, m['t1'] + t0) for m in sp.get('moves', [])]
        labels = sp.get('label_cues') or {}
        for name in sp.get('visual_cues') or []:
            if name not in cues:
                vis.append({'segment': sid, 'cue': name, 'offset': None, 'how': 'cue not in beats'})
                continue
            t = cues[name] + t0
            if name in labels and tt:
                first = next((e['t'] for e in tt if e['t'] >= t - 1.0 and any(i.get('text') == labels[name] for i in e.get('items', []))), None)
                vis.append({'segment': sid, 'cue': name, 't': round(t, 3), 'offset': None if first is None else round(first - t, 3), 'how': 'label'})
                continue
            end, st = t + 0.8, t - 0.3
            for a, b in moves:
                if t < a < end:
                    end = a
                if st < b <= t:
                    st = b + 1 / 30
            base = float(np.median(d[max(0, int((t - 0.7) * 30)):max(1, int((t - 0.15) * 30))]))
            i0, i1 = int(st * 30), int(end * 30)
            seg = d[i0:i1]
            if len(seg) == 0 or seg.max() - base < 0.08:
                vis.append({'segment': sid, 'cue': name, 't': round(t, 3), 'offset': None, 'how': 'motion'})
                continue
            on = int(np.argmax(seg > base + 0.5 * (seg.max() - base)))
            vis.append({'segment': sid, 'cue': name, 't': round(t, 3), 'offset': round(i0 / 30 + on / 30 - t, 3), 'how': 'motion'})
        ref = [(_norm(w['w']), w['s'] + t0) for w in sp.get('words', []) if not str(w['w']).startswith('[')]
        j = next((k for k, h in enumerate(heard) if h[1] >= t0 - 1.0), len(heard))
        for word, t in ref:
            for k in range(j, min(j + 6, len(heard))):
                if heard[k][0] == word:
                    voice.append(heard[k][1] - t)
                    j = k + 1
                    break
    ok = [v for v in vis if v['offset'] is not None and abs(v['offset']) <= 0.2]
    share = 100.0 * len(ok) / len(vis) if vis else 100.0
    med = float(np.median(voice)) if voice else None
    return verdict('R07', [metric('visual cues within ±0.2 s (%)', share, '>=', 92.0, '%'),
                           metric('|median voice offset| s', None if med is None else abs(med), '<=', 0.2)],
                   details=[{'cues': len(vis), 'within': len(ok), 'voiceWordsMatched': len(voice), 'voiceMedian': med,
                             'voiceP90abs': float(np.percentile(np.abs(voice), 90)) if voice else None},
                            *[v for v in vis if v['offset'] is None or abs(v['offset']) > 0.2][:20]])


# ---- A18 → V14 ------------------------------------------------------------------------------------------------------------------
@rule('V14', 'D-010 quy tắc 1/2/3/7 (đoạn thế giới), checks-appeal A18', 'world segments (as R07), the four checks of toolkit/factory/world/verify_seg.py that need no page '
      'log: (rule 2) no spine keyword (beats[].cues) strictly inside a camera move widened by spine.pad (spine.moves (t0 − pad, t1 + pad)); (rule 3) every move has a reason and a sound whose kind '
      'is among spine.events; (cuts) hard cuts on the master = consecutive frames (320×180 grey, 30 fps) with > 45% of pixels changing by > 25 levels; (first 5 s) '
      'the beats of the episode\'s first 5 s are in mode "world". Rule 1 (number/compare texts only in chart mode, chartW ≥ 0.95) needs the page log\'s chartW, which '
      'the page sampler does not record: not measured here (reported by the builder\'s verify_seg)',
      '0 keywords during a move; 0 moves without reason or sound; 0 hard cuts; first 5 s in the world; no world segment = nothing to check')
def v14_world(ctx):
    segs = world_segments(ctx)
    if not segs:
        return verdict('V14', [metric('hard cuts', 0, '<=', 0)], note='no world segments: nothing to check')
    kw_moving, no_reason, first = [], [], []
    for sid, sp, t0 in segs:
        pad = float(sp.get('pad', 0.25))
        moves = sp.get('moves', [])
        for b in sp.get('beats', []):
            for k, t in b.get('cues', {}).items():
                if any(m['t0'] - pad < t < m['t1'] + pad for m in moves):
                    kw_moving.append({'segment': sid, 'cue': f"{b['id']}.{k}", 't': round(t + t0, 3)})
            if b.get('t0', 0) + t0 < 5.0 and b.get('mode') not in (None, 'world'):
                first.append({'segment': sid, 'beat': b['id'], 'mode': b.get('mode'), 't0': round(b.get('t0', 0) + t0, 3)})
        kinds = {e.get('kind') for e in sp.get('events', [])}
        no_reason += [{'segment': sid, 'move': f"{m.get('verb')} {m.get('from')}→{m.get('to')}", 't0': round(m['t0'] + t0, 3)}
                      for m in moves if not m.get('reason') or m.get('sound') not in kinds]
    share = frame_diffs(ctx, cut=True)
    cuts = [round(i / 30, 2) for i, v in enumerate(share) if v > 0.45]
    return verdict('V14', [metric('keywords during a camera move', len(kw_moving), '<=', 0), metric('moves without reason or sound', len(no_reason), '<=', 0),
                           metric('hard cuts', len(cuts), '<=', 0), metric('first-5 s beats not in the world', len(first), '<=', 0)],
                   details=[{'segments': len(segs), 'keywords': sum(len(b.get('cues', {})) for _, sp, _ in segs for b in sp.get('beats', [])),
                             'moves': sum(len(sp.get('moves', [])) for _, sp, _ in segs), 'rule1': 'not measured (no chartW in page.json)'},
                            {'keywordsDuringMove': kw_moving[:10]}, {'movesWithoutReasonOrSound': no_reason[:10]}, {'hardCuts': cuts[:20]}, {'first5s': first}])


def _runs(track, key, total):
    """[(t0, t1, value)] from a change track [{t, <key>}] (value holds until the next entry; the last until `total`)."""
    out = []
    for i, e in enumerate(track):
        t1 = track[i + 1]['t'] if i + 1 < len(track) else total
        if t1 > e['t']:
            out.append((e['t'], t1, e[key]))
    return out


# ---- A13 → V15 ------------------------------------------------------------------------------------------------------------------
@rule('V15', 'D-010 quy tắc 5 (không quay lại thẻ chữ), checks-appeal A13', 'page sampler text-only track (K4.0; every 0.1 s): a sample is text-only when a text is '
      'visible and no visible non-text object other than role bg/card is on frame; on a world page (window.CHECKS.segments, the 3D world is a canvas the objects() '
      'contract does not list) only when a bg/card object (opacity > 0.5) also covers ≥ 60% of the frame. Share = text-only time / out/timeline.json total',
      'text-only time ≤ 15% of the episode')
def v15_text_only(ctx):
    p = ctx.json('out/checks/page.json')
    if 'textOnlyTrack' not in p:
        raise Missing('out/checks/page.json: textOnlyTrack (page sampler before K4.0)')
    total = ctx.total()
    runs = [(a, b) for a, b, v in _runs(p['textOnlyTrack'] or [], 'textOnly', total) if v]
    share = 100.0 * sum(b - a for a, b in runs) / total if total else 0.0
    return verdict('V15', [metric('text-only time (%)', share, '<=', 15.0, '%')],
                   details=[{'runs': len(runs), 'longest': sorted(([round(a, 2), round(b, 2)] for a, b in runs), key=lambda r: r[0] - r[1])[:10]}])


# ---- A19 → T4 -------------------------------------------------------------------------------------------------------------------
SFX_BEDS = {'drone_on'}
SFX_DUR = {'tick': 0.15, 'land': 0.3, 'chime': 1.0, 'impact': 1.0, 'thud': 0.6, 'gather': 1.6}


@rule('T4', 'D-010 §6 (lượt đạo diễn: sfx dày), checks-appeal A19', 'world segments (as R07): spine.events except kind "data" (data sound, own layer) and continuous '
      'beds (drone_on), episode time = t + t0; spine.words (no [tags]). Per segment: events per minute of the segment, most events in a sliding 10 s window, share of '
      'events starting inside a spoken word that is not a keyword (beats[].cues). The definition of the builder\'s F-2 meter (toolkit/factory/world/sfx_labels.py), '
      'without its keyword-masking SNR (voice clarity is L1/A14) and without its label part (text over text or line: V11)',
      'every segment ≤ 30 events/min, ≤ 6 events in any 10 s, ≤ 50% of events on plain spoken words; no world segment = nothing to check')
def t4_sfx_density(ctx):
    segs = world_segments(ctx)
    if not segs:
        return verdict('T4', [metric('segments over a density limit', 0, '<=', 0)], note='no world segments: nothing to check')
    rows = []
    for sid, sp, t0 in segs:
        ev = sorted(float(e['t']) for e in sp.get('events', []) if e.get('kind') != 'data' and e.get('kind') not in SFX_BEDS)
        W = [w for w in sp.get('words', []) if not str(w['w']).startswith('[') and w['e'] > w['s']]
        kw = {round(t, 3) for b in sp.get('beats', []) for t in b.get('cues', {}).values()}
        total = float(sp.get('total') or 0) or max(ev + [w['e'] for w in W] + [1e-9])
        per_min = len(ev) / (total / 60) if total else 0.0
        win = max((sum(1 for x in ev if t <= x < t + 10.0) for t in ev), default=0)
        plain = sum(1 for t in ev if any(w['s'] <= t < w['e'] and not any(abs(w['s'] - k) <= 0.02 or w['s'] <= k < w['e'] for k in kw) for w in W))
        rows.append({'segment': sid, 't0': round(t0, 2), 'events': len(ev), 'perMin': round(per_min, 1), 'max10s': win,
                     'onPlainWords': plain, 'onPlainShare': round(100.0 * plain / len(ev), 1) if ev else 0.0})
    over = [r for r in rows if r['perMin'] > 30 or r['max10s'] > 6 or r['onPlainShare'] > 50]
    return verdict('T4', [metric('segments over a density limit', len(over), '<=', 0),
                          metric('highest events/min', max(r['perMin'] for r in rows), '<=', 30.0),
                          metric('most events in 10 s', max(r['max10s'] for r in rows), '<=', 6),
                          metric('highest share on plain words (%)', max(r['onPlainShare'] for r in rows), '<=', 50.0, '%')], details=rows)


# ---- A24 → V17 ------------------------------------------------------------------------------------------------------------------
def label_words(text):
    """Words of a label: whitespace tokens holding a letter or digit (lone symbols ≥ · % → are not words)."""
    return [w for w in str(text).split() if re.search(r'[A-Za-z0-9]', w)]


@rule('V17', 'DX-V (đọc kịp), lessons T5-2, checks-appeal A24', 'page sampler text track (every 0.1 s, texts with opacity > 0.5 on frame): each text\'s visible runs '
      '(by tid; gaps ≤ 0.2 s joined; a run still on at the end of the timeline counts to the end). Words = whitespace tokens holding a letter or digit. Texts without a '
      'letter (counters, bare numbers) are not labels. A label needs ceil(words / 3) s on screen; its longest run is compared',
      'every label on screen ≥ 1 s per 3 words (rounded up); 0 labels too short')
def v17_label_time(ctx):
    import math
    tt = ctx.json('out/checks/page.json').get('textTrack')
    if tt is None:
        raise Missing('out/checks/page.json: textTrack')
    total = ctx.total()
    runs, text_of, open_ = {}, {}, {}
    for i, e in enumerate(tt):
        now = {it['tid']: it.get('text') or '' for it in e.get('items', [])}
        for tid, txt in now.items():
            text_of[tid] = txt
            if tid not in open_:
                rs = runs.setdefault(tid, [])
                if rs and e['t'] - rs[-1][1] <= 0.2 + 1e-9:
                    open_[tid] = rs.pop()[0]
                else:
                    open_[tid] = e['t']
        for tid in [k for k in open_ if k not in now]:
            runs.setdefault(tid, []).append((open_.pop(tid), e['t']))
    for tid, t0 in open_.items():
        runs.setdefault(tid, []).append((t0, total))
    short, n = [], 0
    for tid, rs in runs.items():
        txt = text_of[tid]
        if not re.search(r'[A-Za-z]', txt):
            continue
        n += 1
        need = math.ceil(len(label_words(txt)) / 3)
        got = max(b - a for a, b in rs)
        if got + 1e-6 < need:
            short.append({'text': txt[:80], 'words': len(label_words(txt)), 'needS': need, 'longestS': round(got, 2), 'at': round(max(rs, key=lambda r: r[1] - r[0])[0], 2)})
    short.sort(key=lambda x: x['longestS'] - x['needS'])
    return verdict('V17', [metric('labels on screen too short to read', len(short), '<=', 0)], details=[{'labels': n}, *short[:30]])
