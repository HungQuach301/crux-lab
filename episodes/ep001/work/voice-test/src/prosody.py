"""Đo prosody (C4 · G-015). F0 bằng pyworld Harvest (khung 5 ms, 60–300 Hz), semitone so với 100 Hz.
Năng lượng RMS khung 10 ms. Không sửa âm thanh — chỉ đo."""
import numpy as np, av, pyworld as pw

SR = 16000


def decode(path, sr=SR):
    c = av.open(path); rs = av.AudioResampler(format='flt', layout='mono', rate=sr); out = []
    for f in c.decode(audio=0):
        for g in rs.resample(f): out.append(g.to_ndarray().reshape(-1))
    for g in rs.resample(None): out.append(g.to_ndarray().reshape(-1))
    c.close(); return np.concatenate(out).astype(np.float64)


def frames_db(x, sr=SR, win=0.01):
    w = int(win * sr); n = len(x) // w
    return 20 * np.log10(np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(axis=1) + 1e-12))


def span(x, sr=SR, thr=-50.0, win=0.01):
    db = frames_db(x, sr, win); on = np.where(db > thr)[0]
    return (on[0] * win, (on[-1] + 1) * win) if len(on) else (0.0, len(x) / sr)


def f0(x, sr=SR):
    f, t = pw.harvest(x.astype(np.float64), sr, f0_floor=60.0, f0_ceil=300.0, frame_period=5.0)
    return t, f


def st(f):
    return 12 * np.log2(f / 100.0)


def sentence(x, words, sr=SR):
    """x: clip một câu đã cắt đầu/đuôi im lặng."""
    t, f = f0(x, sr); v = f > 0; s = st(f[v]); tv = t[v]
    dur = len(x) / sr
    db = frames_db(x, sr); sp = db[db > db.max() - 35]
    out = {'dur_s': round(dur, 3), 'words': words, 'wpm': round(60 * words / dur, 1)}
    if len(s) < 20:
        return out
    out.update(f0_median_hz=round(float(np.median(f[v])), 1), st_range_p5_p95=round(float(np.percentile(s, 95) - np.percentile(s, 5)), 2),
               st_sd=round(float(np.std(s)), 2), st_mean=round(float(np.mean(s)), 2),
               energy_sd_db=round(float(np.std(sp)), 2), energy_range_p10_p90=round(float(np.percentile(sp, 90) - np.percentile(sp, 10)), 2))
    # đầu câu: 300 ms hữu thanh đầu
    out['st_onset'] = round(float(np.median(s[tv <= tv[0] + 0.3])), 2)
    # cuối câu: 250 ms hữu thanh cuối so với 250–750 ms trước đó
    end = tv[-1]; a = s[tv >= end - 0.25]; b = s[(tv < end - 0.25) & (tv >= end - 0.75)]
    d = float(np.median(a) - np.median(b)) if len(a) > 3 and len(b) > 3 else 0.0
    out['final_delta_st'] = round(d, 2); out['final'] = 'lên' if d > 1.0 else ('xuống' if d < -1.0 else 'ngang')
    # độ dốc (declination) st/s
    out['slope_st_per_s'] = round(float(np.polyfit(tv, s, 1)[0]), 2)
    # đường nét 50 điểm (trừ trung bình) để đo "khuôn chung"
    grid = np.linspace(tv[0], tv[-1], 50); out['_contour'] = (np.interp(grid, tv, s) - np.mean(s)).tolist()
    out['_st'] = s.tolist()
    return out


def passage(sents):
    ok = [s for s in sents if 'st_sd' in s]
    allst = np.concatenate([np.array(s['_st']) for s in ok])
    C = np.array([s['_contour'] for s in ok]); n = len(C)
    cc = [np.corrcoef(C[i], C[j])[0, 1] for i in range(n) for j in range(i + 1, n)]
    words = sum(s['words'] for s in sents); talk = sum(s['dur_s'] for s in sents)
    finals = [s['final'] for s in ok]
    return {'n_sentences': len(sents), 'st_sd_all': round(float(np.std(allst)), 2),
            'st_range_all_p5_p95': round(float(np.percentile(allst, 95) - np.percentile(allst, 5)), 2),
            'st_range_sentence_mean': round(float(np.mean([s['st_range_p5_p95'] for s in ok])), 2),
            'st_sd_sentence_mean': round(float(np.mean([s['st_sd'] for s in ok])), 2),
            'sd_of_sentence_means_st': round(float(np.std([s['st_mean'] for s in ok])), 2),
            'sd_of_onsets_st': round(float(np.std([s['st_onset'] for s in ok])), 2),
            'energy_sd_db_mean': round(float(np.mean([s['energy_sd_db'] for s in ok])), 2),
            'contour_corr_mean': round(float(np.mean(cc)), 3) if cc else None,
            'finals': {k: finals.count(k) for k in ('lên', 'ngang', 'xuống')},
            'final_delta_mean_st': round(float(np.mean([s['final_delta_st'] for s in ok])), 2),
            'wpm_talk': round(60 * words / talk, 1), 'wpm_sd_across_sentences': round(float(np.std([s['wpm'] for s in sents])), 1),
            'wpm_cv': round(float(np.std([s['wpm'] for s in sents]) / np.mean([s['wpm'] for s in sents])), 3)}


def pauses(x, sr=SR, min_s=0.12, rel=40.0, win=0.01):
    """Khoảng lặng ≥ min_s trong file (bỏ đầu/cuối file). Ngưỡng: p95 khung − rel dB."""
    db = frames_db(x, sr, win); thr = np.percentile(db, 95) - rel; sil = db < thr
    runs = []; i = 0; n = len(sil)
    while i < n:
        if sil[i]:
            j = i
            while j < n and sil[j]: j += 1
            if i > 0 and j < n and (j - i) * win >= min_s: runs.append(round((j - i) * win, 3))
            i = j
        else: i += 1
    r = np.array(runs) if runs else np.array([0.0])
    return {'count': len(runs), 'mean_s': round(float(r.mean()), 3), 'sd_s': round(float(r.std()), 3), 'cv': round(float(r.std() / r.mean()), 3) if r.mean() else None,
            'min_s': round(float(r.min()), 3), 'max_s': round(float(r.max()), 3), 'p25_p50_p75': [round(float(v), 3) for v in np.percentile(r, [25, 50, 75])], 'all_s': runs}


def strip(d):
    return {k: v for k, v in d.items() if not k.startswith('_')}
