"""T rules (K1, 2026-09-28): data sonification that can be heard (T1), music that does not loop (T2), silences entered through a
transition onto a room-tone floor (T3). Measured on the delivered master and stems; declared event files only say where to look."""
import json
import subprocess

import numpy as np
from scipy import signal

from common import FPS, SR, Missing, asr_join, canon_matches, frame_rms_db, master, metric, numbers_in_text, rule, spoken_numbers, verdict
from r_audio import asr_master, silent_spans, stem_audio, stem_path

BAND = (1500.0, 8000.0)      # Hz: where the data sounds must stand out (above most of the voice's energy, below air)
LIFT_DB = 3.0                # dB: the sonification raises the band at least this much (its band power ≥ that of everything else)
LIFT_NUM_DB = 1.0            # dB: inside a spoken-number window, where DX-A6 lowers music and effects (replacement criterion, not an exemption)
SON_FLOOR_DB = -60.0         # dBFS: the data sound itself must be there in the band
CLUSTER_GAP = 0.15           # s: events closer than this are one cluster (> ~8 events/s are heard as one gesture, DX-A1)
WIN = 0.15                   # s: measurement window from an onset
LONG_STEP = 0.5              # s: a long cluster is measured again every 0.5 s
STEM_MATCH_R = 0.90          # the stems must add up to the master in the band (they are the real mix)


def _band(x):
    sos = signal.butter(4, BAND, btype='bandpass', fs=SR, output='sos')
    return signal.sosfilt(sos, x.mean(1) if x.ndim == 2 else x)


def _pow_db(p):
    return 10 * np.log10(p + 1e-20)


def son_stem_name(ctx):
    try:
        stem_path(ctx, 'sonify')
        return 'sonify'
    except Missing:
        return 'sfx'


def declared_events(ctx):
    """out/sonify-events.json (the builder's events: bar {f0}, line samples {f, id}, dot {f}; fps). A line draw = consecutive samples of one id."""
    d = ctx.json('out/sonify-events.json')
    fps = float(d.get('fps', FPS))
    ev = [(b['f0'] / fps, 'bar', b.get('id')) for b in d.get('bar', [])]
    ev += [(x['f'] / fps, 'dot', x.get('id')) for x in d.get('dot', [])]
    last = {}
    for x in sorted(d.get('line', []), key=lambda x: (x.get('id'), x['f'])):
        k = x.get('id')
        if k not in last or x['f'] - last[k] > 2:
            ev.append((x['f'] / fps, 'line', k))
        last[k] = x['f']
    return ev


def detected_events(ctx):
    """Chart events the page sampler saw with the camera frozen (out/checks/page.json chartEvents: a data shape appears or its box changes
    within [t, t + 0.1 s]). Consecutive samples of one shape (0.1 s apart) are one event at the first."""
    ce = ctx.json('out/checks/page.json').get('chartEvents')
    if ce is None:
        raise Missing('out/checks/page.json chartEvents')
    ev, last = [], {}
    for x in sorted(ce, key=lambda x: (x['id'], x['t'])):
        if x['id'] not in last or x['t'] - last[x['id']] > 0.15:
            ev.append((float(x['t']), x.get('kind'), x['id']))
        last[x['id']] = x['t']
    return ev


def clusters(times):
    out = []
    for t in sorted(times):
        if out and t - out[-1][1] <= CLUSTER_GAP:
            out[-1][1] = t
        else:
            out.append([t, t])
    return out


def number_windows(ctx):
    """[onset − 0.5 s, end + 1.6 s] around every number the narration says (own ASR), the windows where DX-A6 lowers music and effects."""
    from r_page import number_run
    asr = asr_master(ctx)
    wins = []
    for s in ctx.sentences():
        nums = [c for c, _ in numbers_in_text(s['text'])]
        if not nums:
            continue
        ws = [w for w in asr if s['start'] - 1 <= w['start'] <= s['end'] + 1]
        for n in dict.fromkeys(nums):
            r = number_run(ws, n)
            if r:
                wins.append((ws[r[0]]['start'] - 0.5, ws[r[1]]['end'] + 1.6))
    return wins


@rule('T1', 'DX-A1 (sổ gu G-001)', 'events = union of the declared out/sonify-events.json (bar f0, dot f, start of each line draw) and the chart events the page sampler measured '
      'with the camera frozen (a bar, series, mark or character shape appears or changes); events closer than 0.15 s form one cluster, measured at its onset and every 0.5 s '
      'to its end. Band 1.5–8 kHz (4th-order Butterworth), window [t, t + 0.15 s]: lift = 10·log10((P_son + P_rest) / P_rest), P_son = band power of the data-sound stem '
      '("sonify", or "sfx" when the data sounds are mixed into it), P_rest = band power of the sum of the other stems (voice, music, whoosh, room [, sfx]). '
      'Inside a spoken-number window [onset − 0.5 s, end + 1.6 s] (own ASR), where DX-A6 lowers effects, the lift needed is 1 dB. Truth check: the stems add up to the '
      'master in the band (correlation of the band signals). Without a sonify stem the sfx stem is measured (reported) but the rule cannot pass: other effects would count as data sounds',
      'every measured window: lift ≥ 3 dB (≥ 1 dB in a spoken-number window) and data-sound band level ≥ −60 dBFS; stems ~ master r ≥ 0.90; ≥ 1 cluster; sonify stem delivered')
def t1_sonification(ctx):
    evs, src = [], []
    for name, fn in (('declared', declared_events), ('page', detected_events)):
        try:
            e = fn(ctx)
            evs += e
            src.append(f'{name}: {len(e)}')
        except Missing:
            pass
    if not src:
        raise Missing('out/sonify-events.json or out/checks/page.json chartEvents')
    sname = son_stem_name(ctx)
    rest_names = ['voice', 'music', 'whoosh', 'room'] + (['sfx'] if sname == 'sonify' else [])
    son = _band(stem_audio(ctx, sname))
    rest = None
    for n in rest_names:
        x = stem_audio(ctx, n)
        rest = x.copy() if rest is None else rest[: len(x)] + x[: len(rest)]
    rest = _band(rest)
    n = min(len(son), len(rest))
    son, rest = son[:n], rest[:n]
    m = _band(master(ctx))[:n]
    mix = son + rest
    r_mix = float(np.dot(m, mix) / np.sqrt(np.dot(m, m) * np.dot(mix, mix) + 1e-20))
    numw = number_windows(ctx)
    innum = lambda t: any(a <= t <= b for a, b in numw)
    rows = []
    for a, b in clusters([e[0] for e in evs]):
        ts = [a] + list(np.arange(a + LONG_STEP, b + 1e-9, LONG_STEP))
        for t in ts:
            i, j = int(t * SR), int((t + WIN) * SR)
            if j > n or i < 0:
                continue
            ps, pr_ = float(np.mean(son[i:j] ** 2)), float(np.mean(rest[i:j] ** 2))
            lift = 10 * np.log10((ps + pr_ + 1e-20) / (pr_ + 1e-20))
            need = LIFT_NUM_DB if innum(t) else LIFT_DB
            rows.append({'t': round(float(t), 2), 'lift': round(float(lift), 2), 'son_dB': round(float(_pow_db(ps)), 1), 'rest_dB': round(float(_pow_db(pr_)), 1),
                         'need': need, 'ok': bool(lift >= need and _pow_db(ps) >= SON_FLOOR_DB)})
    bad = [r for r in rows if not r['ok']]
    lifts = [r['lift'] for r in rows]
    return verdict('T1', [metric('event clusters', len(clusters([e[0] for e in evs])), '>=', 1), metric('windows measured', len(rows), '>=', 1),
                          metric('windows not audible', len(bad), '<=', 0), metric('stems ~ master in band r', r_mix, '>=', STEM_MATCH_R),
                          metric('data sounds delivered as their own stem (sonify)', sname == 'sonify', '==', True)],
                   details=[{'events': src, 'dataStem': sname, 'medianLiftDb': round(float(np.median(lifts)), 2) if lifts else None,
                             'p90LiftDb': round(float(np.percentile(lifts, 90)), 2) if lifts else None, 'inNumberWindows': sum(1 for r in rows if r['need'] == LIFT_NUM_DB),
                             'audible': len(rows) - len(bad)}, *sorted(bad, key=lambda r: r['lift'])[:15]])


# ---- T2 music self-similarity ----------------------------------------------------------------------------
SIM_SR = 12000
SIM_NEAR = 0.90   # a phrase this similar to a recent one is heard as the same phrase again
SIM_SHARE = 5.0   # % of phrases allowed to be such a repeat (a motif may come back; a loop may not)
SIM_RUN = 1       # consecutive repeated phrases allowed (two in a row = the same 4 bars three times: a loop)
LAGS = (1, 2, 3, 4)


def phrase_features(x, beats, sr=SIM_SR):
    """Per 4-beat bar: 12-bin chroma (STFT magnitude folded to pitch classes, 55–2000 Hz) + 16-step onset pattern (spectral flux), both
    unit-normalised (onsets weighted 0.7); a phrase = 4 bars concatenated, unit-normalised. Bars whose music is below −50 dBFS are None
    (a quiet phrase is not a loop). Same features as the D tool toolkit/audio/d_music_selfsim.py."""
    f, t, Z = signal.stft(x, sr, nperseg=2048, noverlap=1536)
    M = np.abs(Z)
    keep = (f >= 55) & (f <= 2000)
    pc = (np.round(12 * np.log2(f[keep] / 440.0)) % 12).astype(int)
    chroma = np.zeros((12, M.shape[1]))
    for k in range(12):
        chroma[k] = M[keep][pc == k].sum(0)
    flux = np.maximum(0, np.diff(M, axis=1, prepend=M[:, :1])).sum(0)
    bars = beats[::4]
    feats = []
    for i in range(len(bars) - 1):
        a, b = np.searchsorted(t, bars[i]), np.searchsorted(t, bars[i + 1])
        seg = x[int(bars[i] * sr): int(bars[i + 1] * sr)]
        if b - a < 4 or not len(seg) or 10 * np.log10(np.mean(seg ** 2) + 1e-20) < -50:
            feats.append(None)
            continue
        c = chroma[:, a:b].mean(1)
        c = c / (np.linalg.norm(c) + 1e-12)
        fl = flux[a:b]
        on = np.array([fl[int(j * (b - a) / 16):int((j + 1) * (b - a) / 16) or 1].mean() for j in range(16)])
        on = on / (np.linalg.norm(on) + 1e-12)
        feats.append(np.concatenate([c, 0.7 * on]))
    ph = []
    for i in range(0, len(feats) - 3, 4):
        blk = feats[i:i + 4]
        if any(v is None for v in blk):
            ph.append(None)
            continue
        v = np.concatenate(blk)
        ph.append((bars[i], v / np.linalg.norm(v)))
    return ph


def load_mono(path, sr=SIM_SR):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


@rule('T2', 'DX-A2 (sổ gu G-002)', 'music stem; bars of 4 beats from out/tempo-map.json beats (A12 checks those beats against the music\'s onsets); 4-bar phrases of chroma + onset '
      'pattern (phrase_features). For each phrase: the highest cosine similarity with the 1, 2, 3 and 4 phrases before it (a loop of 1–4 phrases repeats at one of these lags). '
      'A repeat = similarity ≥ 0.90. Quiet phrases (< −50 dBFS) are left out',
      '≥ 8 phrases measured; repeats ≤ 5% of phrases; never 2 repeated phrases in a row')
def t2_music_loops(ctx):
    beats = ctx.json('out/tempo-map.json').get('beats', [])
    x = ctx.memo(('music12k',), lambda: load_mono(ctx.path(stem_path(ctx, 'music'))))
    ph = phrase_features(x, beats)
    rows = []
    for i, p in enumerate(ph):
        if p is None:
            continue
        prev = [(L, float(p[1] @ ph[i - L][1])) for L in LAGS if i - L >= 0 and ph[i - L] is not None]
        if prev:
            L, s = max(prev, key=lambda z: z[1])
            rows.append((round(p[0], 2), L, round(s, 4)))
    rep = [r for r in rows if r[2] >= SIM_NEAR]
    run, best = 0, 0
    for r in rows:
        run = run + 1 if r[2] >= SIM_NEAR else 0
        best = max(best, run)
    share = 100 * len(rep) / len(rows) if rows else None
    sims = [r[2] for r in rows]
    return verdict('T2', [metric('phrases measured', len(rows), '>=', 8), metric('repeated phrases (%)', share, '<=', SIM_SHARE, '%'),
                          metric('longest run of repeated phrases', best, '<=', SIM_RUN)],
                   details=[{'medianSimilarity': round(float(np.median(sims)), 4) if sims else None, 'maxSimilarity': max(sims, default=None),
                             'repeats': rep[:15]}])


# ---- T3 entering a silence ---------------------------------------------------------------------------------
ENTRY = (0.150, 0.400)   # s: the bed releases into the silence over this long (DX-R6: about 300 ms; not a hard cut, not a slow fade)
BED_DROP = 30.0          # dB below the bed's level before the silence = released
FLOOR_DB = -80.0         # dBFS: the master never falls below this inside a silence (room tone floor, never digital silence)
ROOM_DB = -75.0          # dBFS: the room stem is present through the silence


@rule('T3', 'DX-R6 (sổ gu G-003)', 'intentional silences = master spans ≤ −40 dBFS (50 ms RMS, 10 ms hop) of 0.8–1.5 s (as A09). Bed = music + sfx + whoosh (+ sonify) stems summed, '
      '20 ms RMS, 5 ms hop. Reference = 90th percentile of the bed in [start − 0.8, start − 0.1]. Entry = from the last instant the bed is within 3 dB of the reference '
      '(searched in [start − 1.0, start + 0.3]) to the first instant after it the bed is 30 dB below the reference (or below −70 dBFS). A bed already below −60 dBFS before the '
      'silence has nothing to release and is reported, not judged. Floor: master 50 ms RMS minimum inside the silence (edges 0.1 s excluded) and the room stem mean level there',
      'every entry 150–400 ms; master ≥ −80 dBFS and room stem ≥ −75 dBFS through every silence; ≥ 1 silence')
def t3_silence_entry(ctx):
    x = master(ctx)
    dur = len(x) / SR
    spans = [(a, b) for a, b in silent_spans(x) if a > 2 and b < dur - 2 and 0.8 <= b - a <= 1.5]
    names = ['music', 'sfx', 'whoosh'] + (['sonify'] if _has(ctx, 'sonify') else [])
    bed = None
    for n in names:
        s = stem_audio(ctx, n)
        bed = s.copy() if bed is None else bed[: len(s)] + s[: len(bed)]
    bt, bdb = frame_rms_db(bed, win=0.02, hop=0.005)
    mt, mdb = frame_rms_db(x, win=0.05, hop=0.01)
    rt, rdb = frame_rms_db(stem_audio(ctx, 'room'), win=0.05, hop=0.01)
    rows = []
    for a, b in spans:
        pre = (bt >= a - 0.8) & (bt <= a - 0.1)
        ref = float(np.percentile(bdb[pre], 90)) if pre.any() else -120.0
        row = {'start': round(a, 2), 'dur': round(b - a, 2), 'bedRef': round(ref, 1)}
        if ref < -60:
            row['entry'] = None
        else:
            sel = np.flatnonzero((bt >= a - 1.0) & (bt <= a + 0.3) & (bdb >= ref - 3))
            if not len(sel):
                row['entry'] = 0.0
            else:
                i = sel[-1]
                tgt = max(ref - BED_DROP, -70.0)
                k = next((j for j in range(i + 1, len(bdb)) if bdb[j] <= tgt), None)
                row['entry'] = round(float(bt[k] - bt[i]), 3) if k is not None else None
        inside = (mt >= a + 0.1) & (mt <= b - 0.1)
        row['masterMin'] = round(float(mdb[inside].min()), 1) if inside.any() else None
        rin = (rt >= a + 0.1) & (rt <= b - 0.1)
        row['room'] = round(float(10 * np.log10(np.mean(10 ** (rdb[rin] / 10)))), 1) if rin.any() else None
        row['entryOk'] = row['entry'] is None and ref < -60 or (row['entry'] is not None and ENTRY[0] <= row['entry'] <= ENTRY[1])
        row['floorOk'] = row['masterMin'] is not None and row['masterMin'] >= FLOOR_DB and row['room'] is not None and row['room'] >= ROOM_DB
        rows.append(row)
    return verdict('T3', [metric('silences measured', len(rows), '>=', 1), metric('entries outside 150–400 ms', sum(not r['entryOk'] for r in rows), '<=', 0),
                          metric('silences without a room-tone floor', sum(not r['floorOk'] for r in rows), '<=', 0)], details=rows[:20])


def _has(ctx, name):
    try:
        stem_path(ctx, name)
        return True
    except Missing:
        return False
