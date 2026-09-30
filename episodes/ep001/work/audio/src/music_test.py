"""C6 blind music test (owner 30/09/2026): three ~38 s samples of the cold open + promise, one per --music-style (A, C, AC), rendered by
mix.py in sample mode (--window), loudness-matched (gain only), AAC 192k stereo 48 kHz, labels shuffled with secrets.SystemRandom.

    python3 episodes/ep001/work/audio/src/music_test.py [--scratch DIR]

Resumable: a style whose sample wav + metrics already exist in DIR is not rendered again. Writes review-c6/music-test/sample-{P,Q,R}.m4a,
key.json (the mapping: do not open before choosing), notes.md (no mapping).
"""
import json
import os
import secrets
import subprocess
import sys

import numpy as np
from scipy import signal

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mix  # noqa: E402

EP = mix.EP
OUT = os.path.join(EP, 'review-c6', 'music-test')
W0, W1 = 16.7, 55.2          # S01.3 "At the February rate..." (17.165) - 0.465 s  ..  end of S02.8 "...need a bigger cut?" (54.465) + 0.735 s
VOM_DB = 23.97               # voice over music (A07 method) in this window of the current C5 master (out/audio/stems, 30/09 03:48)
LUFS = -16.0
STYLES = ['A', 'C', 'AC']
SR = mix.SR


def tempo_est(x):
    """Onset-strength autocorrelation of the music stem (mono), 60-180 BPM."""
    mono = x.mean(1)
    f, t, Z = signal.stft(mono, SR, nperseg=2048, noverlap=2048 - 480)
    mag = np.log1p(100 * np.abs(Z))
    flux = np.maximum(0, np.diff(mag, axis=1)).sum(0)
    flux -= flux.mean()
    ac = np.correlate(flux, flux, 'full')[len(flux) - 1:]
    fps = SR / 480
    lags = np.arange(len(ac))
    bpm = 60 * fps / np.maximum(lags, 1)
    sel = (bpm >= 60) & (bpm <= 180)
    return round(float(bpm[sel][np.argmax(ac[sel])]), 1)


KS_MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
KS_MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


def key_est(x):
    """Krumhansl-Schmuckler on a chroma of the music stem (110-2000 Hz)."""
    mono = x.mean(1)
    f, t, Z = signal.stft(mono, SR, nperseg=8192)
    P = (np.abs(Z) ** 2).sum(1)
    ch = np.zeros(12)
    for fi, p in zip(f, P):
        if 110 <= fi <= 2000:   # above the bass and the low thump
            ch[int(round(12 * np.log2(fi / 440) + 69)) % 12] += p
    best = max(((np.corrcoef(np.roll(prof, k), ch)[0, 1], f'{NAMES[k]} {mode}') for k in range(12) for prof, mode in ((KS_MAJ, 'major'), (KS_MIN, 'minor'))))
    return best[1], round(float(best[0]), 3)


def lufs_of(path):
    return mix.ebur128(mix.decode(path, 2))


def main():
    a = sys.argv[1:]
    scratch = a[a.index('--scratch') + 1] if '--scratch' in a else os.path.join(EP, 'work', 'audio', 'cache', 'music-test')
    os.makedirs(scratch, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    res = {}
    for s in STYLES:
        wav, met = os.path.join(scratch, s + '.wav'), os.path.join(scratch, s + '.json')
        if not (os.path.exists(wav) and os.path.exists(met)):
            subprocess.run([sys.executable, os.path.join(HERE, 'mix.py'), '--music-style', s, '--window', str(W0), str(W1), '--vom-db', str(VOM_DB),
                            '--lufs', str(LUFS), '--out', wav, '--metrics', met], check=True)
        m = json.load(open(met))
        mus = np.load(met + '.music.npy').astype(np.float64)
        mix.STYLE = s
        tl = mix.TL(17739 / 30)
        _, bars, bpms = mix.tempo_grid(tl)
        m['tempoMapBpm'] = {'S01': bpms['S01'], 'S02': bpms['S02']}
        m['tempoMeasuredBpm'] = tempo_est(mus)
        m['keyDeclared'] = mix.key_of('S01')
        m['keyEstimated'], m['keyEstimateR'] = key_est(mus)
        m['chords'] = [f"{mix.CHORDS[k][c][0]}{mix.CHORDS[k][c][1]}" for b, (k, c) in zip(bars, mix.harmony(bars)) if b['t1'] > W0 and b['t0'] < W1]
        res[s] = m
    labels = ['P', 'Q', 'R']
    order = STYLES[:]
    secrets.SystemRandom().shuffle(order)
    key = {'_': 'GIẢI MÃ — không mở trước khi chọn.', 'window_s': [W0, W1],
           'common': {'segment': 'S01.3 "At the February rate…" → hết S02.8 "…need a bigger cut?" (cold open + câu hứa)',
                      'voice': 'review-c4/narration-v32.m4a (cố định)', 'sonification': 'S2 minimal, luật cũ', 'voiceOverMusicTargetDb': VOM_DB,
                      'masterChain': '-14 LUFS, TP -1.5 dBTP như C5, rồi chỉ chỉnh gain về -16 LUFS', 'lufsTarget': LUFS,
                      'codec': 'AAC 192k stereo 48 kHz',
                      'measures': 'voiceOverMusicDb_A07 = A07 on the window stems; tempoMapBpm = the engine grid (cuts on downbeats); tempoMeasuredBpm = onset autocorrelation of the music stem, 60-180 BPM (rough: a syncopated figure can lock to a sub-multiple); keyEstimated = Krumhansl-Schmuckler on a 110-2000 Hz chroma of the music stem (D dorian shares its notes with A minor / C major)', 'generator': 'episodes/ep001/work/audio/src/mix.py --music-style (music_test.py)'},
           'samples': {}}
    rows = []
    for lab, s in zip(labels, order):
        dst = os.path.join(OUT, f'sample-{lab}.m4a')
        subprocess.run([mix.FFMPEG, '-y', '-v', 'error', '-i', os.path.join(scratch, s + '.wav'), '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
                        '-map_metadata', '-1', '-fflags', '+bitexact', '-flags:a', '+bitexact', dst], check=True)
        L = lufs_of(dst)
        m = res[s]
        key['samples'][lab] = {'style': s, 'desc': {'A': 'tò mò, sáng, giọng trưởng, nhịp vừa', 'C': 'năng động, nhịp nhanh hơn rõ',
                                                    'AC': 'sáng như A, nhịp nhanh như C'}[s],
                               'voiceOverMusicDb_A07': m['voiceOverMusicDb_A07'], 'tempoMapBpm': m['tempoMapBpm'], 'tempoMeasuredBpm': m['tempoMeasuredBpm'],
                               'keyDeclared': m['keyDeclared'], 'keyEstimated': m['keyEstimated'], 'chordsInWindow': m['chords'],
                               'lufsM4a': L['I'], 'truePeakM4a': L['TP']}
        rows.append((lab, m['voiceOverMusicDb_A07'], L['I'], L['TP']))
    json.dump(key, open(os.path.join(OUT, 'key.json'), 'w'), indent=1, ensure_ascii=False)
    fmt = lambda v: f'{v:.1f}'.replace('.', ',').replace('-', '−')
    notes = f"""# Thử mù nhạc nền · C6 (30/09/2026)

Ba bản thử ~38 s, cùng một đoạn: **cold open + câu hứa**, {fmt(W0)} → {fmt(W1)} s của tập (từ ngay trước S01.3 "At the February rate…" tới sau S02.8
"…need a bigger cut?"). Nghe `sample-P.m4a`, `sample-Q.m4a`, `sample-R.m4a`, chọn một bản. **Đừng mở `key.json` trước khi chọn** (khoá giải mã).

Nhãn P/Q/R xáo bằng `secrets.SystemRandom().shuffle`; thứ tự chữ cái không mang nghĩa.

## Giữ nguyên giữa ba bản
- Lời: `review-c4/narration-v32.m4a` (cố định, không đụng).
- Tiếng dữ liệu: bảng S2 "minimal", cùng luật (−16 dB dưới lời, side-chain −8 dB, bỏ 1–4 kHz khi có lời, dời vào khe âm tiết; không nâng mức).
- Mức nhạc dưới lời: bằng mức của bản mix hiện tại ở đúng đoạn này ({fmt(VOM_DB)} dB lời trên nhạc, cách đo A07); không nâng nhạc.
- Duck 1–4 kHz dưới lời, nhạc nhường dải dữ liệu, khoảng lặng [beat] (nhả τ 90 ms, không nốt mới 1,3 s trước khoảng lặng), nhấn ở cú cắt.
- Chuỗi master như C5 (−14 LUFS, TP −1,5 dBTP), rồi chỉ chỉnh gain để ba bản cùng {fmt(LUFS)} LUFS tích hợp; vào 0,25 s, ra 0,6 s.
- Cùng bộ máy nhạc (`mix.py --music-style`), tổng hợp bằng numpy, không mẫu âm thanh; hợp âm Markov không lặp cửa sổ 4 ô nhịp trong 24 ô.
- AAC 192 kb/s, stereo, 48 kHz.

## Số đo từng bản
| Bản | Lời trên nhạc (dB, A07) | LUFS tích hợp (m4a) | True peak (dBTP) |
|---|---|---|---|
""" + ''.join(f'| {l} | {fmt(v)} | {fmt(i)} | {fmt(tp)} |\n' for l, v, i, tp in sorted(rows)) + """
Sau khi chọn: sinh lại nhạc cả tập theo bản chọn, mix lại, chạy lại luật âm thanh; không render lại hình.
"""
    open(os.path.join(OUT, 'notes.md'), 'w').write(notes)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
