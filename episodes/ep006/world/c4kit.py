"""Tập 6 · C4 · tiện ích chung cho các ĐOẠN THẾ GIỚI CỦA TẬP (spine v2, D-010) — mọi đoạn dựng từ timeline của nhà máy, không gõ tay giờ.
Mẫu: episodes/ep005/world/c4kit.py (Seg, music_plan, music_db) + episodes/ep006/world/c3kit.py (khung khoá hàng thùng / séc).
  Seg(scenes)          → words (đầu từ chỉnh theo năng lượng, onset.refine qua wlib.scene_words), takes, lines, t0 (giờ tập), total, start/end cảnh
                         Giờ cảnh = out/factory/timeline.json (CRUX_TIMELINE khi build.py gọi): take ĐÚNG như nhà máy đặt (0 ký tự EL).
  music_plan(seg)      → {'bed': lát nhạc nền F-3 của tập [t0, t0 + total]} (episode.yaml audio.music; không nhạc riêng của đoạn)
  music_db(seg)        → mức nhạc dưới lời của đoạn sao cho MỌI đoạn dùng CÙNG một hệ số nhạc nền (như Tập 5)
  step_row / step_check / spread → khung khoá hàng thùng (sức mua) + tấm séc (×1,02 mỗi kỷ niệm), như C3
  moves_of(specs)      → động tác máy (cửa sổ giữa hai từ khoá ± PAD) có id / lý do / âm
  quiet(S, …)          → lặng của bản trộn (MR1) + kiểm KHÔNG sfx trong lặng trước số neo (episode.md §5b) và trong lặng MR1
  finish(…)            → ghép spine.json (+ inputs.json), tự kiểm quy tắc 2/3/7 (mọi đoạn), in tóm tắt; thoát 1 nếu vi phạm
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

BED = 'episodes/ep006/work/factory/music/bed.wav'
MUSIC_BASE_DB = 16.0     # như Tập 5: mức nhạc dưới lời TRƯỚC né (audio.py duck −4 dB + khoét 1–4 kHz) → A07 ≈ 20 dB trên stem
PAD = 0.25
ANCHOR_SIL = 0.75        # = world/music/bed.py ANCHOR_SIL
CLAIMS = json.load(open(os.path.join(HERE, 'claims.json')))
GRID = json.load(open(os.path.join(HERE, 'grid.json')))
P = {k: [v / 100 for v in CLAIMS['paths'][k]] for k in ('ruth', 'carl', 'edna')}   # sức mua theo năm k = 0..20 (phần của khoản đầu)


def timeline():
    p = os.environ.get('CRUX_TIMELINE') or os.path.join(EP, 'out', 'factory', 'timeline.json')
    return json.load(open(p))


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
                raise SystemExit(f"{s['id']}: take của nhà máy khác take {W['hash']} (voice-scenes.json) — dừng")
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
        raise SystemExit(f'{BED} chưa có — chạy `python3 episodes/ep006/c4/build_inputs.py --timeline` trước (nhạc nền của tập)')
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
    return round(MUSIC_BASE_DB + dv - dm, 2)


# ---------------------------------------------------------------- hàng thùng / séc (C3, c3kit.py)
def step_row(times, values, ramp=0.3, v0=None, notes=True):
    """Khung khoá [[t, v]] + nốt dữ liệu: tại times[i] hàng đi từ giá trị trước tới values[i] trong ramp s (nốt chỉ khi hàng thật sự đổi, trần 10)."""
    kf, ev, prev = [], [], values[0] if v0 is None else v0
    kf.append([0.0, prev])
    for t, v in zip(times, values):
        kf += [[round(t, 3), prev], [round(t + ramp, 3), v]]
        if notes and abs(min(1, v) - min(1, prev)) >= 0.004:
            ev.append({'t': round(t, 3), 'kind': 'data', 'v': round(min(1.0, v), 3)})
        prev = v
    return kf, ev


def step_check(times, k0=0, ramp=0.12):
    kf = [[0.0, k0]]
    for i, t in enumerate(times):
        kf += [[round(t, 3), k0 + i], [round(t + ramp, 3), k0 + i + 1]]
    return kf


def spread(a, b, n):
    return [a + (b - a) * i / max(1, n - 1) for i in range(n)]


def moves_of(specs, eps=0.01):
    """specs: (id, verb, from, to, after, before, dur, lý do, âm, {late|start}) → động tác (cửa sổ của spine.window)."""
    out = []
    for mid, verb, a, b, after, before, dur, reason, snd, kw in specs:
        t0, t1 = SV.window(after, before, dur, PAD, eps=eps, **kw)
        out.append({'id': mid, 'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd})
    return out


def anchor_windows(S, sids):
    """Lặng trước số neo (giờ của đoạn): [đầu câu − ANCHOR_SIL − 0,05; đầu câu − 0,05] — cùng cửa sổ nhạc nền về 0 của bed.py."""
    out = []
    for sid in sids:
        t = S.at('@' + sid)
        out.append([round(t - ANCHOR_SIL - 0.05, 3), round(t - 0.05, 3)])
    return out


def finish(here, S, name, beats, moves, events, extra, label_cues, visual_cues, accents=(), anchors=(), silences=(), rule7=False, inputs=()):
    """Ghép spine.json, tự kiểm quy tắc 2/3/7 (mọi đoạn: verify đòi 5 s đầu thế giới), không sfx/whoosh trong lặng (neo, MR1), ghi inputs.json; thoát 1 nếu vi phạm."""
    ev = sorted(events + SV.move_sounds(moves, lambda m: {'mode': 0.6, 'pan': 0.8, 'push': 0.7, 'pull': 0.9}[m['verb']]), key=lambda e: e['t'])
    # quy tắc 7 (5 s đầu ở thế giới) kiểm ở MỌI đoạn: build_seg verify đòi first_5s_world cho từng đoạn. rule7 nay chỉ đặt tên khoá
    # 'checks' (đoạn cũ giữ tên cũ → spine.json đã render không đổi byte → cache render_shots, vốn băm spine.json, vẫn trúng)
    errs = SV.check_rules(beats, moves, PAD)
    aw = anchor_windows(S, anchors)
    for b in beats:
        if b['sid'] in anchors:
            b['anchor'] = True
    for a, z in aw + [list(x) for x in silences]:
        bad = [e for e in ev if a - 0.4 <= e['t'] <= z and e['kind'] != 'data' or (e['kind'] == 'data' and a - 0.3 <= e['t'] <= z)]   # tiếng vang (nốt dữ liệu ≈ 0,3 s, sfx ≈ 0,4 s) không lấn vào lặng
        bad += [m for m in moves if m['t0'] < z and m['t1'] > a]
        if bad: errs.append(f'lặng [{a}, {z}]: có âm/động tác trong khoảng lặng: {bad[:3]}')
    if any(e['t'] > S.total for e in ev): errs.append('sự kiện âm sau cuối đoạn')
    for e in ev:
        if e['kind'] == 'land' and not e.get('mode'):
            errs.append(f"'land' không phải chạm đổi chế độ @{e['t']} (episode.md §5b: bỏ land đè từ khoá)")
    TEN = {b['id']: b['music'] for b in beats}
    tension = [[0, 0.2]] + [[b['t0'], 0.2 + 0.6 * TEN[b['id']]] for b in beats] + [[S.total, 0.1]]
    spine = {'segment': name, 'version': 6, 'total': S.total, 'fps': 30, 'pad': PAD, 'episode_t0': S.t0, 'scenes': S.scenes, 'takes': S.takes,
             'words': S.words, 'beats': beats, 'moves': moves, 'events': ev, 'tension': tension, 'shots': SV.shots_for(moves, S.total),
             'music_plan': music_plan(S, accents), 'mix': {'music_db': music_db(S), 'data_db': 25.0, 'silences': [list(x) for x in silences]},
             'anchor_silences': aw, **extra, 'label_cues': label_cues, 'visual_cues': visual_cues,
             'checks': {'rule2_rule3' + ('_rule7' if rule7 else ''): errs or 'OK'}}
    json.dump(spine, open(os.path.join(here, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(['episodes/ep006/world/claims.json', 'episodes/ep006/world/grid.json', 'episodes/ep006/world/c4kit.js', *inputs],
              open(os.path.join(here, 'inputs.json'), 'w'))
    n_sfx = sum(1 for e in ev if e['kind'] != 'data')
    print('total', S.total, '· moves', [(m['id'], m['t0'], m['t1']) for m in moves])
    print('events', len(ev), f'(sfx {n_sfx}, {60 * n_sfx / S.total:.1f}/phút) · music_db', spine['mix']['music_db'], '· anchors', aw, '· silences', list(silences))
    print('checks', errs or 'OK')
    sys.exit(1 if errs else 0)
