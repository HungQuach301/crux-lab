"""Tập 5 · F-3 — nghe thử nhạc theo bản đồ căng + số đo. 0 ký tự ElevenLabs (lời = take đã có trong voice-takes/).
  python3 episodes/ep005/world/music/audition.py
1. Lời cả tập từ take (giờ cảnh = wlib.episode_offsets(), như SPINE-PLAN) → work/factory/music-audition/voice.wav
2. Nhạc: bed.py (bản đồ căng) → work/factory/music-audition/bed.wav (+ .json: lưới phách, ô nhịp)
3. Trộn bằng đúng hàm của nhà máy: toolkit/factory/music.py mix() (20 dB dưới lời theo A07, 1–4 kHz né 13 dB) → stems
4. Đo: A07 (cả tập + từng đoạn), mức né 1–4 kHz đo thật, LUFS ngắn hạn (EBU R128 S, 3 s) của stem nhạc theo đoạn, khoảng lặng MR1,
   tự tương đồng (toolkit/audio/d_music_selfsim.py, G-002)
5. Ra review-c4/music-audition.m4a (≈ 80 s: calm → MR1 → phát lại dâng → đỉnh → chốt "removed"; loudnorm −14 LUFS),
   review-c4/tension-map.png, review-c4/music-report.json
"""
import json
import os
import re
import subprocess
import sys

import numpy as np
import soundfile as sf
from scipy import signal

HERE = os.path.dirname(os.path.abspath(__file__))
WORLD = os.path.dirname(HERE)
EP = os.path.dirname(WORLD)
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(0, WORLD)
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
sys.dont_write_bytecode = True
import bed as BED  # noqa: E402
import tension as TM  # noqa: E402
import music as MUSIC  # noqa: E402  (toolkit/factory/music.py — mức + né của nhà máy)
import wlib  # noqa: E402

SR = 48000
WORK = os.path.join(EP, 'work', 'factory', 'music-audition')   # khác audio.music của episode.yaml: nhà máy tự sinh theo timeline thật
REV = os.path.join(EP, 'review-c4')
EXCERPT = [   # (nhãn, câu đầu, câu cuối) — cắt ở khe giữa câu
    ('calm · Hồi 1', 'S04.3', 'S04.5'),
    ('MR1 → phát lại vào', 'S09.4', 'S10.2'),
    ('phát lại dâng', 'S10.4', 'S11.1'),
    ('đỉnh · đuôi chậm', 'S13.2', 'S14.1'),
    ('chốt "removed"', 'S20.1', 'S20.3'),
]
XF = 0.25


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def voice_track(A, total, path):
    N = int(round(total * SR))
    v = np.zeros(N)
    for sc, t0 in A['scene_start'].items():
        _, mp3, _, _ = wlib.scene_take(sc)
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp3, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
        x = np.frombuffer(raw, np.float32).astype(np.float64)
        i0 = int(round(t0 * SR)); n = min(len(x), N - i0); v[i0:i0 + n] += x[:n]
    sf.write(path, np.stack([v, v], 1), SR, subtype='PCM_24')


def lufs_s(path):
    """EBU R128 short-term loudness (3 s) mỗi 0,1 s — ffmpeg ebur128."""
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-v', 'verbose', '-i', path, '-af', 'ebur128=framelog=verbose', '-f', 'null', '-'],
                       capture_output=True, text=True)
    t, s = [], []
    for m in re.finditer(r't:\s*([\d.]+)\s+TARGET.*?S:\s*(-?[\d.]+|-inf)', r.stderr):
        t.append(float(m.group(1))); s.append(float(m.group(2)) if m.group(2) != '-inf' else np.nan)
    s = np.array(s); s[s < -70] = np.nan
    return np.array(t), s


def band_power(x, lo=1000, hi=4000):
    sos = signal.butter(4, [lo, hi], 'band', fs=SR, output='sos')
    return signal.sosfiltfilt(sos, x.mean(1)) ** 2


def win_mean(p, w):
    k = len(p) // w
    return p[:k * w].reshape(k, w).mean(1)


def main():
    os.makedirs(WORK, exist_ok=True); os.makedirs(REV, exist_ok=True)
    M = TM.build()
    A = TM.anchors()
    total = M['total']
    vw, bw, mw, stems = (os.path.join(WORK, f) for f in ('voice.wav', 'bed.wav', 'mix-raw.wav', 'stems'))
    voice_track(A, total, vw)
    mus, info = BED.render(total, M)
    sf.write(bw, mus, SR, subtype='PCM_24')
    json.dump({**info, 'tension': M}, open(bw + '.json', 'w'), indent=1, ensure_ascii=False)
    mx = MUSIC.mix(vw, bw, total, mw, stems)
    voice, _ = sf.read(os.path.join(stems, 'voice.flac'), always_2d=True)
    music, _ = sf.read(os.path.join(stems, 'music.flac'), always_2d=True)
    rep = {'a07_gap_db': mx['a07_gap_db'], 'mid_duck_db_setting': mx['mid_duck_db'], 'bpm': [info['bpm'], info['bpm_act2_outro']],
           'mr1': info['mr1'], 'landing_removed_S20_2': info['landing'], 'key_change_F_major': info['key_change']}
    # né 1–4 kHz đo thật: mức dải giữa của stem nhạc so với nhạc thô (cùng hệ số chung), lúc có lời so với lúc không lời
    w = int(0.1 * SR)
    pv = win_mean(voice.mean(1) ** 2, w)
    act = 10 * np.log10(pv + 1e-20) > -45
    raw_b, mix_b = win_mean(band_power(mus[:len(music)]), w), win_mean(band_power(music), w)
    full = win_mean(mus[:len(music)].mean(1) ** 2, w)
    ok = (raw_b > 1e-12) & (mix_b > 0) & (full > 1e-12)
    scale = np.median(10 * np.log10(win_mean(music.mean(1) ** 2, w)[ok] / full[ok]))      # hệ số chung (mức dưới lời)
    band = 10 * np.log10(mix_b[ok] / raw_b[ok]) - scale                                    # dải 1–4 kHz so với phần còn lại
    a_ok = act[:len(ok)][ok]
    rep['mid_duck_db_measured'] = {'voice_active_median': round(float(-np.median(band[a_ok])), 1),
                                   'voice_active_p90': round(float(-np.percentile(band[a_ok], 10)), 1),
                                   'note': 'mức dải 1–4 kHz của stem nhạc so với nhạc thô (trừ hệ số chung), cửa sổ 100 ms có lời; '
                                           'thấp hơn 13 dB vì cổng (40 ms vào / 350 ms nhả) nhả giữa các từ'}
    # LUFS ngắn hạn của stem nhạc theo đoạn + A07 từng đoạn
    tS, S = lufs_s(os.path.join(stems, 'music.flac'))
    sec = {}
    for name, (a, b) in M['sections'].items():
        m = (tS >= a + 3) & (tS <= b)                     # S là cửa sổ 3 s kết thúc ở t
        i0, i1 = int(a * 10), int(b * 10)
        pa = pv[i0:i1]; aa = act[i0:i1]; pm = win_mean(music.mean(1) ** 2, w)[i0:i1]
        gap = 10 * np.log10(pa[aa].mean()) - 10 * np.log10(pm[aa].mean() + 1e-20) if aa.any() else None
        sec[name] = {'t': [round(a, 1), round(b, 1)], 'lufs_s_median': round(float(np.nanmedian(S[m])), 1) if m.any() else None,
                     'lufs_s_p10_p90': [round(float(np.nanpercentile(S[m], 10)), 1), round(float(np.nanpercentile(S[m], 90)), 1)] if m.any() else None,
                     'voice_over_music_db_A07': round(float(gap), 1) if gap is not None else None}
    rep['sections'] = sec
    calm, peak = sec['Hồi 1 calm S04–S06']['lufs_s_median'], sec['replay peak S13–S14']['lufs_s_median']
    rep['lufs_s_range_calm_to_peak_LU'] = round(peak - calm, 1)
    good = S[np.isfinite(S) & (tS > 5)]
    rep['lufs_s_music_stem_p5_p95'] = [round(float(np.percentile(good, 5)), 1), round(float(np.percentile(good, 95)), 1)]
    # MR1: lặng của nhạc (< −60 dBFS) và của cả bản trộn quanh MR1
    env = lambda x: 20 * np.log10(np.sqrt(win_mean(x.mean(1) ** 2, int(0.01 * SR))) + 1e-12)
    me, ve = env(music), env(voice)
    i = int(info['mr1'] * 100)
    def run(mask):
        a = b = i
        while a > 0 and mask[a - 1]: a -= 1
        while b < len(mask) - 1 and mask[b + 1]: b += 1
        return round((b - a + 1) / 100, 2) if mask[i] else 0.0
    rep['mr1_music_silence_s'] = run(me < -60)
    rep['mr1_mix_silence_s'] = run((me < -60) & (ve < -50))
    # G-002 tự tương đồng
    tm = os.path.join(WORK, 'tempo-map.json')
    json.dump({'beats': info['beats']}, open(tm, 'w'))
    ss = sh([sys.executable, os.path.join(ROOT, 'toolkit', 'audio', 'd_music_selfsim.py'), os.path.join(stems, 'music.flac'), tm, 'ep005-F3']).stdout
    try:
        rep['selfsim'] = json.loads(ss[ss.index('{'):])
    except ValueError:
        rep['selfsim'] = ss.strip()[-600:]
    # trích nghe thử
    mix = voice + music
    sent_end = {}
    for x in A['words']: sent_end[x['sid']] = x['e']
    parts, cuts = [], []
    for lab, s0, s1 in EXCERPT:
        a = A['sent'][s0] - 0.45
        b = (sent_end[s1] + 0.55) if s1 != 'S20.3' else total
        if lab.startswith('MR1'): b = sent_end[s1] + 0.55
        parts.append(mix[int(a * SR):int(b * SR)].copy()); cuts.append({'label': lab, 'from': round(a, 2), 'to': round(b, 2)})
    f = int(XF * SR); ramp = np.linspace(0, 1, f)[:, None]
    out = parts[0]
    for p in parts[1:]:
        out = np.concatenate([out[:-f], out[-f:] * (1 - ramp) + p[:f] * ramp, p[f:]])
    pre = os.path.join(WORK, 'audition-pre.wav')
    sf.write(pre, out / max(1.0, np.abs(out).max() / 0.98), SR, subtype='PCM_24')
    flt = 'loudnorm=I=-14:TP=-1.5:LRA=11'
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', pre, '-af', flt + ':print_format=json', '-f', 'null', '-'], capture_output=True, text=True)
    m = json.loads(r.stderr[r.stderr.rindex('{'):r.stderr.rindex('}') + 1])
    flt2 = (f"{flt}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
            f":offset={m['target_offset']}:linear=true")
    m4a = os.path.join(REV, 'music-audition.m4a')
    sh(['ffmpeg', '-y', '-loglevel', 'error', '-i', pre, '-af', flt2 + ',aresample=48000', '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', m4a])
    t_acc = 0.0
    for c in cuts:
        c['at_in_audition'] = round(t_acc, 2); t_acc += (c['to'] - c['from']) - XF
    rep['audition'] = {'file': os.path.relpath(m4a, ROOT), 'seconds': round(len(out) / SR, 2), 'parts': cuts,
                       'note': 'lời = take đã có (0 ký tự EL); nhạc + mức/né = đúng hàm nhà máy; nối 5 đoạn, chéo 0,25 s; loudnorm −14 LUFS'}
    TM.plot(M, os.path.join(REV, 'tension-map.png'), (tS, S))
    rep['elevenlabs_chars'] = 0
    json.dump(rep, open(os.path.join(REV, 'music-report.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in rep.items() if k != 'selfsim'}, indent=1, ensure_ascii=False))
    print('selfsim:', json.dumps(rep['selfsim'])[:800])


if __name__ == '__main__':
    main()
