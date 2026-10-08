"""Crux factory music mix (Mốc B): voice + music bed at the level Tập 1–3 used (mix_full.py of Tập 3):
  - music level set so voice is VOICE_OVER_MUSIC dB (20) above music, power measured over voice-active 100 ms windows (A07 method);
  - 1–4 kHz of the music ducked 13 dB while the voice is active (gate 40 ms attack, 350 ms release, 80 ms look-ahead).
  mix(voice_wav, music_wav, total, out_wav, stems_dir) → {'a07_gap_db', 'mid_duck_db'}; loudness is done after, by build.py (loudnorm 2-pass).
F-12 (C3 Tập 6, nhạc hiệu kênh A): post(stems_dir, raw_out, tl, audio, ROOT) chạy SAU khi stem đã đủ (sau music.mix và ghép đoạn thế giới
  của splice.py, nên dùng chung cho tập 2D và tập thế giới), trước loudnorm. Cả hai bước đều opt-in trong `episode.yaml audio:`;
  không khai → trả {} và không chạm file nào (tập cũ dựng lại trùng từng byte).
  - `ident: {after: S03, wav?, db?}`: IDENT_S (3 s) cuối đuôi cảnh `after` phát WAV nhạc hiệu đã duyệt (mặc định THEME_IDENT, đường dẫn
    tính từ gốc repo) thay cho thẻ im; mức = độ to lời của tập + `db` (mặc định −2 LU, như clip duyệt: ident −16 / tập −14); nhạc nền
    (stem music) về 0 trong cửa sổ (vào/ra IDENT_FADE). Lời của cảnh lấn vào cửa sổ → dừng.
  - `close_lift_db: 12` (+ `close_lift_s: 0.5`, `close_lift_delay_s: 0`): sau CHỮ CUỐI của tập (max của mốc từ cuối trong timeline và
    lúc lời thật tắt trên stem voice, cổng −45 dBFS/100 ms như A07), stem music lên +close_lift_db dB theo đường cong S trong close_lift_s
    → điểm chạm của khúc đóng nghe rõ ở thẻ cuối (clip duyệt episodes/ep006/world/music/theme_clip.py làm tay đúng phép này).
    Khi còn lời, nhạc giữ nguyên (A07 20 dB, né 1–4 kHz 13 dB); báo cáo đo lại A07 sau khi nâng.
"""
import os
import re
import subprocess
import tempfile

import numpy as np
import soundfile as sf
from scipy import signal
from scipy.ndimage import uniform_filter1d

SR = 48000
VOICE_OVER_MUSIC_DB = 20.0
MID_DUCK_DB = 13.0
IDENT_S = 3.0                       # ident của kênh (genre-spec: ≤ 3 s; checks S15)
IDENT_FADE = 0.25                   # nhạc nền ra/vào quanh cửa sổ ident (s)
IDENT_DB = -2.0                     # ident so với độ to lời của tập (LU)
VOICE_GATE_DB = -45.0               # cổng "đang có lời" (cách đo A07)
HERE = os.path.dirname(os.path.abspath(__file__))
THEME_IDENT = 'toolkit/factory/theme/ident-A.wav'   # nhạc hiệu A đã duyệt (C3 Tập 6, 08/10)


def load(p, n):
    x, sr = sf.read(p, always_2d=True)
    assert sr == SR, f'{p}: {sr} Hz'
    x = x if x.shape[1] == 2 else np.repeat(x[:, :1], 2, 1)
    out = np.zeros((n, 2))
    out[:min(n, len(x))] = x[:n]
    return out


def gate(act, att, rel, hop=48):
    a, r, g, y = np.exp(-hop / (att * SR)), np.exp(-hop / (rel * SR)), 0.0, []
    for v in act[::hop]:
        k = a if v > g else r
        g = k * g + (1 - k) * v
        y.append(g)
    return np.repeat(y, hop)[:len(act)]


def a07_gap(v, m):
    w = int(0.1 * SR)
    k = min(len(v), len(m)) // w
    pv = (v[:k * w].mean(1) ** 2).reshape(k, w).mean(1)
    pm = (m[:k * w].mean(1) ** 2).reshape(k, w).mean(1)
    a = 10 * np.log10(pv + 1e-20) > -45
    return float(10 * np.log10(pv[a].mean()) - 10 * np.log10(pm[a].mean() + 1e-20))


def mix(voice_wav, music_wav, total, out_wav, stems_dir):
    n = int(round(total * SR))
    voice, music = load(voice_wav, n), load(music_wav, n)
    vr = np.sqrt(np.maximum(uniform_filter1d(voice[:, 0] ** 2, int(0.1 * SR)), 0))
    act = (20 * np.log10(vr + 1e-12) > -45).astype(float)
    la = int(0.08 * SR)
    duck = 10 ** (-MID_DUCK_DB * gate(np.concatenate([act[la:], np.zeros(la)]), 0.04, 0.35) / 20)
    b, a = signal.butter(4, [1000, 4000], 'bandpass', fs=SR)
    for ch in range(2):
        mid = signal.filtfilt(b, a, music[:, ch])
        music[:, ch] = music[:, ch] - mid + mid * duck
    vt = act > 0
    music *= np.sqrt(np.mean(voice[vt] ** 2) / np.mean(music[vt].mean(1) ** 2)) * 10 ** (-VOICE_OVER_MUSIC_DB / 20)
    os.makedirs(stems_dir, exist_ok=True)
    sf.write(os.path.join(stems_dir, 'voice.flac'), voice, SR)
    sf.write(os.path.join(stems_dir, 'music.flac'), music, SR)
    out = voice + music
    sf.write(out_wav, out / max(1.0, np.abs(out).max() / 0.98), SR, subtype='PCM_24')
    return {'a07_gap_db': round(a07_gap(voice, music), 2), 'mid_duck_db': MID_DUCK_DB}


# ------------------------------------------------------------------ F-12: ident + nhạc lên sau chữ cuối
def ebur(path):
    """Độ to tích hợp (LUFS), đỉnh thật (dBTP), LRA — ffmpeg ebur128 (cùng cách đo của theme.py Tập 6)."""
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True)
    s = r.stderr[r.stderr.rfind('Summary:'):]
    g = lambda k: float(re.search(k + r':\s+(-?[\d.]+|-inf)', s).group(1).replace('-inf', '-120'))
    return {'I_lufs': g('I'), 'tp_dbtp': g('Peak'), 'lra_lu': g('LRA')}


def ebur_of(x):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'x.wav')
        sf.write(p, x, SR, subtype='FLOAT')
        return ebur(p)


def voice_active(voice):
    vr = np.sqrt(np.maximum(uniform_filter1d(voice.mean(1) ** 2, int(0.1 * SR)), 0))
    return 20 * np.log10(vr + 1e-12) > VOICE_GATE_DB


def last_word_end(tl, voice):
    """Giờ chữ cuối của tập: max(mốc 'e' của từ cuối trong timeline, lúc stem voice tắt hẳn dưới cổng A07)."""
    t_tl = max((w['e'] for w in tl.get('words') or []), default=0.0)
    act = np.flatnonzero(voice_active(voice))
    t_en = (act[-1] + 1) / SR if len(act) else 0.0
    return round(max(t_tl, t_en), 3), round(t_tl, 3), round(t_en, 3)


def smooth(t, a, b):
    u = np.clip((t - a) / max(b - a, 1e-9), 0, 1)
    return u * u * (3 - 2 * u)


def ident_window(tl, after):
    sc = next((s for s in tl['scenes'] if s['id'] == after), None)
    if sc is None:
        raise SystemExit(f'audio.ident.after: {after!r} không phải cảnh của tập')
    b = round(sc['start'] + sc['dur'], 4)
    return round(b - IDENT_S, 4), b


def lift_active(audio):
    return bool(float(audio.get('close_lift_db') or 0))


def post(stems_dir, raw_out, tl, audio, root):
    """F-12: ident + nhạc lên sau chữ cuối trên stem của tập; raw_out = tổng các stem. Không khai gì → {} (không chạm file)."""
    ident, lift = audio.get('ident'), lift_active(audio)
    if not ident and not lift:
        return {}
    files = {f[:-5]: os.path.join(stems_dir, f) for f in sorted(os.listdir(stems_dir)) if f.endswith('.flac')}
    if 'voice' not in files:
        raise SystemExit(f'music.post: thiếu stem voice trong {stems_dir}')
    N = int(round(tl['total'] * SR))
    S = {k: load(p, N) for k, p in files.items()}
    S.setdefault('music', np.zeros((N, 2)))
    t = np.arange(N) / SR
    info = {}
    if ident:
        a, b = ident_window(tl, ident['after'])
        late = [w for w in tl.get('words') or [] if a - 0.05 < w['e'] <= b + 0.05]
        if late:
            raise SystemExit(f"audio.ident: lời lấn vào cửa sổ ident [{a}, {b}] s (từ {late[-1]['w']!r} hết ở {late[-1]['e']} s) — tăng tail của {ident['after']}")
        src = os.path.join(root, ident.get('wav') or THEME_IDENT)
        x, sr = sf.read(src, always_2d=True)
        if sr != SR:
            raise SystemExit(f'audio.ident: {src}: {sr} Hz (cần {SR})')
        if len(x) > int(round(IDENT_S * SR)) + SR // 30:
            raise SystemExit(f'audio.ident: {src} dài {len(x) / SR:.3f} s > IDENT_S {IDENT_S} s')
        x = x if x.shape[1] == 2 else np.repeat(x[:, :1], 2, 1)
        m_id, m_v = ebur(src), ebur_of(S['voice'])
        db = float(ident.get('db', IDENT_DB))
        g_db = m_v['I_lufs'] + db - m_id['I_lufs']
        bed = np.clip(np.maximum((a - t) / IDENT_FADE, (t - b) / IDENT_FADE), 0, 1)   # nhạc nền nhường chỗ cho ident
        S['music'] *= bed[:, None]
        i0 = int(round(a * SR))
        n = min(len(x), N - i0)
        S['music'][i0:i0 + n] += x[:n] * 10 ** (g_db / 20)
        info['ident'] = {'wav': os.path.relpath(src, root), 'after': ident['after'], 't0': a, 't1': b, 'gain_db': round(g_db, 2),
                         'voice_lufs': m_v['I_lufs'], 'ident_file_lufs': m_id['I_lufs'], 'rel_db': db}
    if lift:
        db, ramp = float(audio['close_lift_db']), float(audio.get('close_lift_s', 0.5))
        t_end, t_tl, t_en = last_word_end(tl, S['voice'])
        t0 = t_end + float(audio.get('close_lift_delay_s', 0.0))
        before = S['music'].copy()
        S['music'] *= (10 ** (db * smooth(t, t0, t0 + ramp) / 20))[:, None]
        va = voice_active(S['voice'])
        info['close_lift'] = {'db': db, 'ramp_s': ramp, 't_last_word': t_end, 't_last_word_timeline': t_tl, 't_voice_off': t_en,
                              't0': round(t0, 3), 't_full': round(t0 + ramp, 3),
                              'a07_gap_db_before': round(a07_gap(S['voice'], before), 2), 'a07_gap_db': round(a07_gap(S['voice'], S['music']), 2),
                              'music_changed_while_voice': bool(np.abs(S['music'][va] - before[va]).max() > 1e-9) if va.any() else False}
    mix = sum(S.values())
    pk = float(np.abs(mix).max())
    sc = 0.98 / pk if pk > 0.98 else 1.0   # một hệ số cho mọi stem → tổng stem vẫn = mix-raw (như splice.merge_audio)
    for k, x in S.items():
        if k == 'music' or sc != 1.0:
            sf.write(os.path.join(stems_dir, k + '.flac'), x * sc, SR, subtype='PCM_24')
    sf.write(raw_out, mix * sc, SR, subtype='PCM_24')
    info['post_peak_scale'] = round(sc, 4)
    return info
