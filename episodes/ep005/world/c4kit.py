"""Tập 5 · C4 · tiện ích chung cho các ĐOẠN THẾ GIỚI CỦA TẬP (spine v2, D-010) — mọi đoạn dựng từ timeline của nhà máy, không gõ tay giờ.
  seg(scenes)          → Seg: words (đầu từ chỉnh theo năng lượng, onset.refine qua wlib.scene_words), takes, lines, t0 (giờ tập), total
                         Giờ cảnh = out/factory/timeline.json (CRUX_TIMELINE khi build.py gọi): take ĐÚNG như nhà máy đặt (0 ký tự EL).
  music_plan(seg)      → {'bed': lát nhạc nền F-3 của tập [t0, t0 + total]} (episode.yaml audio.music; không nhạc riêng của đoạn)
  music_db(seg)        → mức nhạc dưới lời của đoạn sao cho MỌI đoạn dùng CÙNG một hệ số nhạc nền (đường căng F-3 giữ nguyên giữa các đoạn):
                         audio.py chuẩn hoá nhạc từng đoạn theo lời của đoạn → bù bằng tỉ lệ (lời đoạn / lời tập) ÷ (nhạc đoạn / nhạc tập)
  fly(moves, via)      → F-1: mọi động tác 'mode' kiểu 'fly' với tư thế 'via' riêng; FALLBACK = {move id} → giữ hoà tan (ghi lý do)
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

def _override_takes():
    """C4 r2: take của cảnh theo voice_overrides (episode.yaml) như NHÀ MÁY chọn — voice-scenes.json (G1) còn ghi take cũ cho S04/S15.
    Cảnh có {seed: N}: take trong voice-takes/ có cùng seed + cùng chữ/giọng/model/thiết lập với take G1 của cảnh; {take: h}: đúng file đó.
    Thiếu take → dừng (không sinh giọng). Không có override → voice-scenes.json nguyên như trước."""
    import yaml, glob, subprocess
    vs = _VS0()
    ov = (yaml.safe_load(open(os.path.join(EP, 'episode.yaml'))) or {}).get('voice_overrides') or {}
    for sc, o in ov.items():
        if sc not in vs:
            continue
        old = json.load(open(os.path.join(wlib.TAKES, vs[sc]['take'].replace('.mp3', '.json'))))
        if o.get('take'):
            h = o['take']
        else:
            hit = [os.path.basename(p)[:-5] for p in glob.glob(os.path.join(wlib.TAKES, '*.json'))
                   if (lambda m: m.get('seed') == o.get('seed', old['seed']) and all(m.get(k) == old.get(k) for k in ('text', 'voice', 'model', 'settings')))(json.load(open(p)))]
            if len(hit) != 1:
                raise SystemExit(f'{sc}: voice_overrides {o} → {len(hit)} take trong voice-takes/ — dừng')
            h = hit[0]
        if h + '.mp3' != vs[sc]['take']:
            mp3 = os.path.join(wlib.TAKES, h + '.mp3')
            dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp3], capture_output=True, text=True, check=True).stdout)
            vs[sc] = {**vs[sc], 'take': h + '.mp3', 'duration': round(dur, 2), 'override': o}
    return vs


_VS0 = wlib.voice_scenes
_VS = {}
wlib.voice_scenes = lambda: _VS.setdefault('v', _override_takes())


BED = 'episodes/ep005/work/factory/music/bed.wav'
MUSIC_BASE_DB = 16.0     # mức nhạc dưới lời TRƯỚC né (audio.py duck −4 dB + khoét 1–4 kHz) → A07 đo trên stem ≈ 20 dB (hiệu chỉnh ở C4)
PAD = 0.25


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

    def at(self, ref):
        return self.A.at(ref)


def music_plan(S, accents=()):
    return {'bed': {'wav': BED, 'offset': S.t0, 'fade': 0.0}, 'stop': S.total, 'release': S.total, 'accents': list(accents)}


def _venv(x):
    k = 240                                          # 200 Hz như audio.py env200
    m = np.abs(x[:len(x) // k * k]).reshape(-1, k).max(1)
    from scipy.ndimage import maximum_filter1d
    return maximum_filter1d(m, 3)


def _rms_active(x, act):
    a = np.repeat(act, 240)[:len(x)]
    a = np.pad(a, (0, len(x) - len(a)))
    return float(np.sqrt(np.mean(x[a.astype(bool)] ** 2) + 1e-12))


_EPI = {}


def _episode_audio():
    """Lời của cả tập (take đặt theo timeline) + nhạc nền (mono), 48 kHz — cache trong tiến trình."""
    if 'v' in _EPI:
        return _EPI['v'], _EPI['m']
    import subprocess
    tl = timeline(); SR = 48000; N = int(tl['total'] * SR)
    v = np.zeros(N)
    for s in tl['scenes']:
        W = wlib.scene_take(s['id'])
        r = subprocess.run(['ffmpeg', '-v', 'error', '-i', W[1], '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
        x = np.frombuffer(r.stdout, np.float32).astype(float); i0 = int(round(s['start'] * SR)); n = min(len(x), N - i0); v[i0:i0 + n] += x[:n]
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(ROOT, BED), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
    m = np.frombuffer(r.stdout, np.float32).astype(float)[:N]; m = np.pad(m, (0, N - len(m)))
    _EPI['v'], _EPI['m'] = v, m
    return v, m


def music_db(S):
    """music_db của đoạn = MUSIC_BASE_DB + (mức lời đoạn − lời tập) − (mức nhạc đoạn − nhạc tập), cùng cách đo của audio.py (RMS lúc có lời)."""
    v, m = _episode_audio()
    SR = 48000
    act = (_venv(v) > 10 ** (-38 / 20)).astype(float)
    i0, i1 = int(S.t0 * SR), int((S.t0 + S.total) * SR)
    vs, ms = v[i0:i1], m[i0:i1]
    acts = (_venv(vs) > 10 ** (-38 / 20)).astype(float)
    dv = 20 * np.log10(_rms_active(vs, acts) / _rms_active(v, act))
    dm = 20 * np.log10(_rms_active(ms, acts) / _rms_active(m, act))
    return round(MUSIC_BASE_DB + dv - dm, 2)


def window(after, before, dur, late=False, start=None):
    return SV.window(after, before, dur, PAD, late, start=start, eps=0.01)


def fly(moves, fallback=()):
    """F-1 cho mọi lần đổi chế độ: style 'fly' + via = move['via'] (tư thế khai trong scene.js). fallback: id giữ hoà tan."""
    out = []
    for m in moves:
        if m['verb'] == 'mode' and m['id'] not in fallback:
            out.append(SV.with_style({k: v for k, v in m.items() if k != 'via'}, 'fly', m['via']))
        else:
            out.append({k: v for k, v in m.items() if k != 'via'})
    return out


def write(here, spine, inputs):
    json.dump(spine, open(os.path.join(here, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(inputs, open(os.path.join(here, 'inputs.json'), 'w'))
