"""Tập 9 · M2/M3 · tiện ích chung (spine.grey = CRUX_GREY=1: animatic xám M2) cho các ĐOẠN THẾ GIỚI CỦA TẬP (spine v2, D-010) — mọi đoạn dựng từ timeline của nhà máy, không gõ tay giờ.
Mẫu: episodes/ep006/world/c4kit.py (Seg, music_plan, music_db, finish) + episodes/ep009/world/c3kit.py (khung khoá + nốt dữ liệu của C3 đã duyệt).
  Seg(scenes)          → words (đầu từ chỉnh theo năng lượng, onset.refine qua wlib.scene_words), takes, lines, t0 (giờ tập), total, start/end/last
                         cảnh. Giờ cảnh = out/factory/timeline.json (CRUX_TIMELINE khi build.py gọi): take ĐÚNG như nhà máy đặt (0 ký tự EL).
  music_plan(seg)      → {'bed': lát nhạc nền F-3 của tập [t0, t0 + total]} (episode.yaml audio.music; không nhạc riêng của đoạn)
  music_db(seg)        → mức nhạc dưới lời của đoạn sao cho MỌI đoạn dùng CÙNG một hệ số nhạc nền (như Tập 5–6)
  steps / spread       → khung khoá [[t, v]] + nốt dữ liệu mỗi lần vật đổi trạng thái (= c3kit.steps)
  moves_of(specs)      → động tác máy (cửa sổ giữa hai từ khoá ± PAD) có id / lý do / âm
  midroll(S, k)        → giờ mid-roll k trong đoạn + khoảng lặng của bản trộn tới hết đoạn (kiểm: sau chữ cuối, ≥ 1 s)
  finish(…)            → ghép spine.json (+ inputs.json), tự kiểm quy tắc 2/3/7, lặng trước số neo / mid-roll không có sfx/động tác,
                         không 'land' ngoài chạm đổi chế độ; in tóm tắt; thoát 1 nếu vi phạm
  stub(here, scenes)   → spine khung tối thiểu của đoạn CHƯA dựng (lượt 2): một nhịp thế giới mỗi câu, không động tác (đủ cho spec/build_seg)
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory', 'world'))
sys.dont_write_bytecode = True
import wlib  # noqa: E402
import spine as SV  # noqa: E402

BED = 'episodes/ep009/work/factory/music/bed.wav'
MUSIC_BASE_DB = 16.0     # như Tập 5–6: mức nhạc dưới lời TRƯỚC né (audio.py duck −4 dB + khoét 1–4 kHz) → A07 ≈ 20 dB trên stem
PAD = 0.25
ANCHOR_SIL = 0.75        # = world/music/bed.py ANCHOR_SIL
MR_SIL = 0.65            # lặng của bản trộn bắt đầu MR_SIL s trước mid-roll (bed.py MR_HOLD 0,6 + nhả)
CLAIMS = json.load(open(os.path.join(HERE, 'claims.json')))
G = CLAIMS['_geom']
INPUTS = ['episodes/ep009/world/claims.json', 'episodes/ep009/world/w9.js', 'episodes/ep009/world/grade9.js', 'episodes/ep009/world/data.json']


def timeline():
    p = os.environ.get('CRUX_TIMELINE') or os.path.join(EP, 'out', 'factory', 'timeline.json')
    if not os.path.exists(p):
        raise SystemExit(f'{p} chưa có — chạy `python3 episodes/ep009/prod/build_inputs.py --timeline` trước (timeline khô, 0 ký tự EL)')
    return json.load(open(p))


def scenes(default):
    """Tập 9 M3: đoạn con (cine trên cảnh đinh) chạy spine.py của đoạn chương với CRUX_SCENES='S04' — chỉ các cảnh đó."""
    v = os.environ.get('CRUX_SCENES')
    return [x for x in default if x in v.split(',')] if v else list(default)


class Cue(dict):
    """cue[beat][key] → giờ; nhịp không có trong đoạn con → None (động tác/sự kiện dùng nó bị bỏ)."""
    def __missing__(self, k):
        return _NoCue()


class _NoCue(dict):
    def __missing__(self, k):
        return None


def cues(beats):
    return Cue({b['id']: b['cues'] for b in beats})


def beats_in(B, S):
    return [b for b in B if b[1][:3] in S.scenes]


class Seg:
    def __init__(self, scenes):
        tl = timeline()
        sc = [s for s in tl['scenes'] if s['id'] in scenes]
        if [s['id'] for s in sc] != list(scenes):
            raise SystemExit(f'cảnh {scenes} không liền / không có trong timeline')
        self.scenes, self.t0 = list(scenes), sc[0]['start']
        self.total = round(sc[-1]['start'] + sc[-1]['dur'] - self.t0, 4)
        self.start = {s['id']: round(s['start'] - self.t0, 4) for s in sc}
        self.end = {s['id']: round(s['start'] + s['dur'] - self.t0, 4) for s in sc}
        self.words, self.takes, self.lines = [], [], {}
        for s in sc:
            W = wlib.scene_words(s['id'])
            vw = [w for w in tl['words'] if w['sid'].startswith(s['id'] + '.')]
            if len(vw) != len(W['words']) or any(abs((a['s'] - s['start']) - b['s_tts']) > 0.002 for a, b in zip(vw, W['words'])):
                raise SystemExit(f"{s['id']}: take của nhà máy khác take {W['hash']} (review-g1/voice-scenes.json) — dừng")
            off = self.start[s['id']]
            self.words += [{'w': w['w'], 's': round(float(w['s']) + off, 3), 'e': round(float(w['e']) + off, 3), 'sid': w['sid'],
                            's_tts': round(float(w['s_tts']) + off, 3)} for w in W['words']]
            self.takes.append({'mp3': W['mp3'], 't': off, 'take': W['hash']})
            self.lines.update(W['lines'])
        self.A = SV.Anchors(self.words)
        self.last = {s: max(w['e'] for w in self.words if w['sid'].startswith(s + '.')) for s in self.scenes}

    def at(self, ref):
        return self.A.at(ref)


def music_plan(S, accents=()):
    return {'bed': {'wav': BED, 'offset': S.t0, 'fade': 0.0}, 'stop': S.total, 'release': S.total, 'accents': list(accents)}


def _venv(x):
    k = 240
    m = np.abs(x[:len(x) // k * k]).reshape(-1, k).max(1)
    from scipy.ndimage import maximum_filter1d
    return maximum_filter1d(m, 3)


def _rms_active(x, act):
    a = np.repeat(act, 240)[:len(x)]
    a = np.pad(a, (0, len(x) - len(a)))
    return float(np.sqrt(np.mean(x[a.astype(bool)] ** 2) + 1e-12))


_EPI = {}


def _episode_audio():
    if 'v' in _EPI:
        return _EPI['v'], _EPI['m']
    import subprocess
    tl = timeline(); SR = 48000; N = int(tl['total'] * SR)
    v = np.zeros(N)
    for s in tl['scenes']:
        W = wlib.scene_take(s['id'])
        r = subprocess.run(['ffmpeg', '-v', 'error', '-i', W[1], '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
        x = np.frombuffer(r.stdout, np.float32).astype(float); i0 = int(round(s['start'] * SR)); n = min(len(x), N - i0); v[i0:i0 + n] += x[:n]
    bed = os.path.join(ROOT, BED)
    if not os.path.exists(bed):
        raise SystemExit(f'{BED} chưa có — chạy `python3 episodes/ep009/prod/build_inputs.py --timeline` trước (nhạc nền của tập)')
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', bed, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
    m = np.frombuffer(r.stdout, np.float32).astype(float)[:N]; m = np.pad(m, (0, N - len(m)))
    _EPI['v'], _EPI['m'] = v, m
    return v, m


def music_db(S):
    """music_db của đoạn = MUSIC_BASE_DB + (mức lời đoạn − lời tập) − (mức nhạc đoạn − nhạc tập), cách đo của audio.py (RMS lúc có lời)."""
    v, m = _episode_audio()
    SR = 48000
    act = (_venv(v) > 10 ** (-38 / 20)).astype(float)
    i0, i1 = int(S.t0 * SR), int((S.t0 + S.total) * SR)
    vs, ms = v[i0:i1], m[i0:i1]
    acts = (_venv(vs) > 10 ** (-38 / 20)).astype(float)
    dv = 20 * np.log10(_rms_active(vs, acts) / _rms_active(v, act))
    dm = 20 * np.log10(_rms_active(ms, acts) / _rms_active(m, act))
    r = MUSIC_BASE_DB + dv - dm
    return round(r, 2) if np.isfinite(r) else MUSIC_BASE_DB   # M2 take khô (im lặng): không đo được → mức gốc


# ---------------------------------------------------------------- khung khoá + nốt dữ liệu (= c3kit.steps, C3 đã duyệt)
def steps(times, values, ramp=0.25, v0=None, pitch=lambda v: v, over=False):
    """Khung khoá [[t, v]] + nốt dữ liệu: tại times[i] giá trị đi từ giá trị trước tới values[i] trong ramp s."""
    prev = values[0] if v0 is None else v0
    kf, ev = [[0.0, prev]], []
    for t, v in zip(times, values):
        kf += [[round(t, 3), prev], [round(t + ramp, 3), v]]
        ev.append({'t': round(t, 3), 'kind': 'data', 'v': round(min(1.0, max(0.0, pitch(v))), 3), **({'over': True} if over else {})})
        prev = v
    return kf, ev


def spread(a, b, n):
    return [a + (b - a) * i / max(1, n - 1) for i in range(n)]


HOLD_PUSH = {'world': [0.008, 0.08], 'chart': [0.005, 0.025], 'breathe': True, 'caps': {'cStacks': 0.012}}   # M5 vòng nhịp 1–2 (w9.js setup): máy tiến chậm khi đứng — [tốc độ/s, trần]; vòng 2: đồ thị thở 0 ↔ trần


def moves_of(specs, eps=0.01):
    """specs: (id, verb, from, to, after, before, dur, lý do, âm, {late|start}) → động tác (cửa sổ của spine.window)."""
    out = []
    for sp in specs:
        if sp is None or sp[4] is None or sp[5] is None:   # đoạn con: động tác của nhịp ngoài đoạn
            continue
        mid, verb, a, b, after, before, dur, reason, snd, kw = sp
        kw = dict(kw); ch = kw.pop('change', None)   # M5 vòng nhịp 1: cú đẩy/lùi ở từ mở ý khai change: major (F-14 (b))
        t0, t1 = SV.window(after, before, dur, PAD, eps=eps, **kw)
        out.append({'id': mid, 'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd, **({'change': ch} if ch else {})})
    return out


def reframe(S, beats, mid, verb, a, b, word, reason, dur=1.2, snd='whoosh_soft'):
    """M5 vòng nhịp 1: cú đẩy/lùi (change: major) bắt đầu ở từ MỞ ý `word` (@Sxx.n:w), xong trước từ khoá kế (quy tắc 2: ±PAD quanh cue)."""
    if word[:3] not in S.scenes:
        return None
    t = S.at('@' + word)
    nxt = min([c for b_ in beats for c in b_['cues'].values() if c > t + 0.05] + [S.total + PAD])
    return (mid, verb, a, b, t - PAD, nxt, dur, reason, snd, {'start': t, 'change': 'major'})


def anchor_windows(S, sids):
    """Lặng trước số neo (giờ của đoạn): [đầu câu − ANCHOR_SIL − 0,05; đầu câu − 0,05] — cùng cửa sổ nhạc nền về 0 của bed.py; phải nằm sau chữ cuối
    của câu trước (trong đuôi của cảnh trước)."""
    out = []
    for sid in sids:
        t = S.at('@' + sid)
        a = round(t - ANCHOR_SIL - 0.05, 3)
        prev = max((w['e'] for w in S.words if w['e'] <= t - 0.01 and not w['w'].startswith('[')), default=-1.0)   # thẻ cảm xúc eleven_v3 không phải lời
        if a < prev + 0.05:
            raise SystemExit(f'số neo {sid}: lặng {a} lấn vào lời trước (hết {prev})')
        out.append([a, round(t - 0.05, 3)])
    return out


def midroll(S, k):
    """Mid-roll thứ k (0-based) của episode.yaml nếu nằm trong đoạn: (giờ trong đoạn, [lặng từ MR − MR_SIL tới hết đoạn])."""
    import yaml
    mr = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))['midrolls'][k]
    t = float(mr['t']) - S.t0
    last = S.last[mr['scene']]
    if not (t - MR_SIL > last + 0.05 and S.total - t <= 1.0 and S.total - (t - MR_SIL) >= 1.0):
        raise SystemExit(f"MR{k + 1} {mr['t']}: lặng [{t - MR_SIL:.3f}; {S.total}] phải sau chữ cuối {last} và ≥ 1 s tới hết đoạn")
    return round(t, 3), [round(t - MR_SIL, 3), S.total]


def finish(here, S, name, beats, moves, events, extra, label_cues, visual_cues, accents=(), anchors=(), silences=(), inputs=()):
    """Ghép spine.json, tự kiểm quy tắc 2/3/7 (mọi đoạn: verify đòi 5 s đầu thế giới), không sfx/whoosh trong lặng (neo, mid-roll), không 'land'
    ngoài chạm đổi chế độ (episode.md §5b), ghi inputs.json; thoát 1 nếu vi phạm."""
    events = [e for e in events if e.get('t') is not None]
    moves = [m for m in moves if m]
    if os.environ.get('CRUX_SCENES'):   # đoạn con: cắt từ spine ĐỦ của đoạn chương; nhịp/động tác đủ (dời giờ) đi kèm ở `ghost` cho scene.js
        S, beats, moves, events, extra, label_cues, visual_cues, anchors, silences, inputs = _subset(S, beats, moves, events, extra, label_cues, visual_cues,
                                                                                                  anchors, silences, inputs)
    ev = sorted(events + SV.move_sounds(moves, lambda m: {'mode': 0.6, 'pan': 0.8, 'push': 0.7, 'pull': 0.9}[m['verb']]), key=lambda e: e['t'])
    errs = SV.check_rules(beats, moves, PAD, episode_t0=S.t0)   # F-14 (c): quy tắc 7 chỉ 5 s đầu TẬP (episode.yaml f14: true)
    aw = anchor_windows(S, anchors)
    for b in beats:
        if b['sid'] in anchors:
            b['anchor'] = True
    for a, z in aw + [list(x) for x in silences]:
        bad = [e for e in ev if a - 0.4 <= e['t'] <= z and e['kind'] != 'data' or (e['kind'] == 'data' and a - 0.3 <= e['t'] <= z)]   # tiếng vang (nốt ≈ 0,3 s, sfx ≈ 0,4 s) không lấn vào lặng
        bad += [m for m in moves if m['t0'] < z and m['t1'] > a]
        if bad: errs.append(f'lặng [{a}, {z}]: có âm/động tác trong khoảng lặng: {bad[:3]}')
    if any(e['t'] > S.total for e in ev): errs.append('sự kiện âm sau cuối đoạn')
    cues = sorted(t for b in beats for t in b['cues'].values())
    for e in ev:
        if e['kind'] == 'land' and not e.get('mode'):
            errs.append(f"'land' không phải chạm đổi chế độ @{e['t']} (episode.md §5b: bỏ land đè từ khoá)")
        if e['kind'] == 'land' and any(e['t'] - 0.05 < c < e['t'] + 0.3 for c in cues):   # F-2: tiếng chạm (0,3 s) không đè đầu từ khoá
            errs.append(f"'land' @{e['t']} đè đầu một từ khoá (episode.md §5b)")
    TEN = {b['id']: b['music'] for b in beats}
    tension = [[0, 0.2]] + [[b['t0'], 0.2 + 0.6 * TEN[b['id']]] for b in beats] + [[S.total, 0.1]]
    spine = {'segment': name, 'version': 8, 'grey': os.environ.get('CRUX_GREY') == '1', 'total': S.total, 'fps': 30, 'pad': PAD, 'episode_t0': S.t0, 'scenes': S.scenes, 'takes': S.takes,
             'words': S.words, 'beats': beats, 'moves': moves, 'events': ev, 'tension': tension, 'shots': SV.shots_for(moves, S.total),
             'music_plan': music_plan(S, accents), 'mix': {'music_db': music_db(S), 'data_db': 34.0,   # Tập 9 (chủ dự án G3 Tập 8, T8-1): data_db 34 để L1 ≥ 20 dB
                     'silences': [list(x) for x in silences]},
             'anchor_silences': aw, 'start': S.start, 'end': S.end, 'last': {k: round(v, 3) for k, v in S.last.items()},
             'f14': True, 'hold_push': HOLD_PUSH, 'changes': {k: 'major' for k in visual_cues}, **extra, 'label_cues': label_cues, 'visual_cues': visual_cues, 'checks': {'rule2_rule3_rule7': errs or 'OK'}}
    m3(spine, S)
    json.dump(spine, open(os.path.join(here, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(INPUTS + list(inputs), open(os.path.join(here, 'inputs.json'), 'w'))
    sfx = [e['t'] for e in ev if e['kind'] != 'data']
    n_sfx, win = len(sfx), max((sum(1 for u in sfx if t <= u < t + 10) for t in sfx), default=0)   # F-2 (sfx_labels.py): > 6 trong 10 s = WARN
    print('total', S.total, '· moves', [(m['id'], m['t0'], m['t1']) for m in moves])
    print('events', len(ev), f'(sfx {n_sfx}, {60 * n_sfx / S.total:.1f}/phút, tối đa {win} trong 10 s) · music_db', spine['mix']['music_db'], '· anchors', aw, '· silences', list(silences))
    print('checks', errs or 'OK')
    sys.exit(1 if errs else 0)


def stub(here, scenes, name):
    """Đoạn CHƯA dựng (lượt 2): thế giới đứng yên (Tessa + nhà, lớp bắt buộc), một nhịp thế giới mỗi câu, không động tác, không âm — chỉ để
    spec.py / build_seg.py chạy được cả tập; scene.js của đoạn = c4kit.js stubScene."""
    S = Seg(scenes)
    B = [(f"s{i}", sid, 'world', '(lượt 2)', '(lượt 2: chưa dựng)', {}, [], 0.3, '—', '—') for i, sid in enumerate(sorted(S.lines, key=lambda x: S.at('@' + x)))]
    beats = SV.beats_from(B, S.A, S.lines)
    finish(here, S, name + ' · KHUNG (lượt 2)', beats, [], [], {'stub': True}, {}, [])


# ---------------------------------------------------------------- Tập 9 M3–M4 (lệnh chặng 15/10): J/L-cut 7 chuyển · `cine` 5 cảnh đinh · SFX ghi âm thật
# Khoá theo CẢNH ĐẦU của đoạn (đoạn vào). J/L: splice.py (F-18), chuyển hồi offset ≤ 0,5 s. cine (F-17): chỉ 1080p; S01–S02 (H1), S04 (H2), S14–S15
# (H3 + H4), S25 (H6) ≈ 25 % thời lượng (≤ 30 %). SFX thật: sfx_labels.thin_events + plan_real (kho CC0 RIGHTS §G1), nhãn theo cảnh (TAM-NHIN §7).
CUTS = {'S05': {'cut': 'L', 'offset': 0.4}, 'S08': {'cut': 'J', 'offset': 0.4}, 'S14': {'cut': 'J', 'offset': 0.4}, 'S16': {'cut': 'L', 'offset': 0.4},
        'S19': {'cut': 'J', 'offset': 0.4}, 'S22': {'cut': 'J', 'offset': 0.4}, 'S25': {'cut': 'L', 'offset': 0.4}}
CINE = {'S01': {'look': 'dusk'}, 'S04': {'look': 'afternoon'}, 'S14': {'look': 'afternoon', 'shots': {}}, 'S25': {'look': 'dusk'}}
SFX_LABELS = {'S01': ['go-nhe'], 'S02': ['giay'], 'S03': ['giay', 'cua'], 'S04': ['giay', 'cua'], 'S05': ['giay'], 'S06': ['may-chu'], 'S08': ['tien-xu'],
              'S09': ['cua', 'go-nhe'], 'S10': ['cua'], 'S11': ['cua'], 'S12': ['cua'], 'S13': ['giay', 'cua'], 'S14': ['giay'], 'S15': ['cua'],
              'S16': ['cua'], 'S17': ['cua'], 'S18': ['cua'], 'S19': ['giay'], 'S20': ['giay'], 'S21': ['giay'], 'S22': ['tien-xu'], 'S23': ['va-mem'],
              'S24': ['may-chu'], 'S25': ['tien-xu', 'va-mem']}
USED = os.path.join(EP, 'work', 'factory', 'sfx-used.json')


def m3(spine, S):
    first = S.scenes[0]
    if first in CUTS:
        spine['cuts'] = {first: CUTS[first]}
    if first in CINE and os.environ.get('CRUX_GREY') != '1':
        spine['cine'] = CINE[first]
    import sfx_labels as SL
    man = json.load(open(os.path.join(ROOT, 'toolkit', 'factory', 'world', 'sfx', 'manifest.json')))
    used = {} if first == 'S01' or not os.path.exists(USED) else json.load(open(USED))
    sp = SL.thin_events(spine)
    sp = SL.plan_real(sp, {k: v for k, v in SFX_LABELS.items() if k in S.scenes}, man, used=used)
    os.makedirs(os.path.dirname(USED), exist_ok=True); json.dump(used, open(USED, 'w'))
    spine.clear(); spine.update(sp)


def _subset(S, beats, moves, events, extra, label_cues, visual_cues, anchors, silences, inputs):
    sub = os.environ['CRUX_SCENES'].split(',')
    S2 = Seg([x for x in S.scenes if x in sub]); off, T = round(S2.t0 - S.t0, 4), S2.total
    sh = lambda t: round(t - off, 4)
    inn = lambda t: -1e-6 <= t - off <= T + 1e-6
    shb = lambda b: {**b, 't0': sh(b['t0']), 't1': sh(b['t1']), 'cues': {k: sh(v) for k, v in b['cues'].items()}}
    shm = lambda m: {**m, 't0': sh(m['t0']), 't1': sh(m['t1'])}
    ghost = {'beats': [shb(b) for b in beats], 'moves': [shm(m) for m in moves], 'parent_t0': S.t0}
    keep = {b['id'] for b in beats if b['sid'][:3] in S2.scenes}
    x = dict(extra)
    for k in ('chapter',):
        if k in x: x[k] = [sh(x[k][0]), x[k][1]] if inn(x[k][0]) else [-99, '']
    for k in ('ident', 'card'):
        if k in x: x[k] = [sh(x[k][0]), sh(x[k][1])] if inn(x[k][1]) else [1e9, 1e9]
    if 'midroll' in x:
        x['midroll'] = sh(x['midroll']) if inn(x['midroll']) else None
        if x['midroll'] is None: x.pop('midroll')
    x['ghost'] = ghost
    par = os.environ.get('CRUX_PARENT')
    return (S2, [shb(b) for b in beats if b['id'] in keep], [shm(m) for m in moves if inn(m['t0']) and inn(m['t1'])],
            [{**e, 't': sh(e['t'])} for e in events if inn(e['t'])], x, {k: v for k, v in label_cues.items() if k.split('.')[0] in keep},
            [k for k in visual_cues if k.split('.')[0] in keep], [a for a in anchors if a[:3] in S2.scenes],
            [[sh(a), sh(b)] for a, b in silences if inn(a) and inn(b)], list(inputs) + ([par] if par else []))
