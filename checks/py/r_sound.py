"""T rules (K1, 2026-09-28; T1 redefined and L1 added by K2): data sonification that can be heard in the voice's pauses (T1) and does not cover
the voice (L1), music that does not loop (T2), silences entered through a transition onto a room-tone floor (T3). Measured on the delivered master and stems; declared event files only say where to look."""
import subprocess

import numpy as np
from scipy import signal

from common import FPS, SR, Missing, frame_rms_db, master, metric, rule, verdict
from r_audio import silent_spans, stem_audio, stem_path

# ---- T1 (K2 redefinition, 2026-09-28): heard in the voice's pauses and where there is no voice, in the band the episode puts the data sounds ----
# PROVISIONAL thresholds (checks/README.md "Ngưỡng tạm"), calibrated on: test D round 3 (owner: "no data sounds yet" -> must FAIL) and the
# Episode 1 blind palette S2 on the m0 sample (owner's choice: "heard", "does not cover the voice" -> must PASS); S1, S3 and m0 (+10 dB) reported.
FRAME = 0.02                 # s: frame of the pause/lift measurement (5 ms hop): short enough to see the gaps between syllables
HOP = 0.005
GAP_DB = -45.0               # dBFS: a voice-stem frame below this is a pause of the voice (same level as the VAD of A07)
DIP_DB = 15.0                # dB: ... or a frame this far below the voice's own maximum within ±0.3 s (a gap between syllables or words)
DIP_SPAN = 0.3               # s
LIFT_DB = 3.0                # dB: in a pause, the data sound raises its band at least this much over everything else
SON_FLOOR_DB = -60.0         # dBFS: and it is there in the band
PRE, POST = 0.10, 0.50       # s: a slot is heard if it sounds in [t − 0.10, t + 0.50] (notes may move into the nearest syllable gap; a long gesture is a slot every 0.5 s)
LONG_STEP = 0.5              # s: a long cluster is a slot every 0.5 s
CLUSTER_GAP = 0.15           # s: events closer than this are one cluster (> ~8 events/s are heard as one gesture, DX-A1)
AUDIBLE_SHARE = 0.60         # share of slots that must be heard (provisional; S2 with the cue-sheet bands: 0.77; test D r3: 0.11)
BAND_SHARE = 0.50            # the declared bands must hold at least this share of the data stem's energy (truth check of the declaration)
STEM_MATCH_R = 0.90          # the stems must add up to the master in the band (they are the real mix)


def _bands(ctx):
    bands = ctx.cfield('sonification', 'bandsHz', kind=list)
    if not bands or not all(isinstance(b, list) and len(b) == 2 and 0 < float(b[0]) < float(b[1]) < SR / 2 for b in bands):
        raise Missing('contract.json: sonification.bandsHz ([[lo, hi], ...] in Hz)')
    return [(float(a), float(b)) for a, b in bands]


def _bandpass(x, bands):
    x = x.mean(1) if x.ndim == 2 else x
    y = np.zeros(len(x))
    for lo, hi in bands:
        sos = signal.butter(4, (lo, hi), btype='bandpass', fs=SR, output='sos')
        y += signal.sosfilt(sos, x)
    return y


def _frames_pow(x, win=FRAME, hop=HOP):
    x = x.mean(1) if x.ndim == 2 else x
    w, h = int(win * SR), int(hop * SR)
    n = max(0, 1 + (len(x) - w) // h)
    c = np.concatenate([[0.0], np.cumsum(x.astype(np.float64) ** 2)])
    st = np.arange(n) * h
    return (st + w / 2) / SR, (c[st + w] - c[st]) / w


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
    ev += [(x['f'] / fps, 'line', x.get('id')) for x in d.get('line', [])]  # every sample of a draw (K2): the draw is one cluster, a slot every 0.5 s
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


def _events(ctx):
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
    return evs, src


def _rest_names(sname):
    return ['voice', 'music', 'whoosh', 'room'] + (['sfx'] if sname == 'sonify' else [])


def _sum_stems(ctx, names):
    tot = None
    for n in names:
        x = stem_audio(ctx, n)
        tot = x.copy() if tot is None else tot[: len(x)] + x[: len(tot)]
    return tot


@rule('T1', 'DX-A1 (sổ gu G-001, G-006)', 'K2 redefinition. Events = union of the declared out/sonify-events.json (bar f0, dot f, start of each line draw) and the chart events '
      'the page sampler measured with the camera frozen (every declared line sample is an event, so a line draw is one cluster); events closer than 0.15 s form one cluster; '
      'a slot = the onset of a cluster and every 0.5 s to its end. '
      'Band = the bands the episode puts its data sounds in (contract.json sonification.bandsHz, from the cue sheet; 4th-order Butterworth each, summed). '
      'Frames of 20 ms (5 ms hop). A pause of the voice = a frame where the voice stem is below −45 dBFS or ≥ 15 dB below its own maximum within ±0.3 s (gaps between syllables '
      'and words, between sentences, and where there is no voice). A slot is heard when, in some pause frame of [t − 0.10 s, t + 0.50 s], lift = 10·log10((P_son + P_rest) / P_rest) ≥ 3 dB and the data-sound band level ≥ −60 dBFS '
      '(P_son = band power of the data-sound stem "sonify", P_rest = band power of the sum of the other stems). Nothing is asked of the data sounds while the voice is sounding '
      '(L1 judges that). Truth checks: the declared bands hold ≥ 50% of the data stem\'s energy; the stems add up to the master in the band. Without a sonify stem the sfx stem is '
      'measured (reported) but the rule cannot pass. Contract without sonification.bandsHz = MISSING',
      'PROVISIONAL: ≥ 60% of slots heard; ≥ 1 slot; declared bands ≥ 50% of the data stem energy; stems ~ master r ≥ 0.90; sonify stem delivered')
def t1_sonification(ctx):
    bands = _bands(ctx)
    evs, src = _events(ctx)
    sname = son_stem_name(ctx)
    son_full = stem_audio(ctx, sname)
    son = _bandpass(son_full, bands)
    rest = _bandpass(_sum_stems(ctx, _rest_names(sname)), bands)
    voice = stem_audio(ctx, 'voice')
    m = _bandpass(master(ctx), bands)
    n = min(len(son), len(rest), len(m), len(voice))  # the master's encoder padding and the stems' lengths differ by a few hundred samples
    son, rest, m = son[:n], rest[:n], m[:n]
    mix = son + rest
    r_mix = float(np.dot(m, mix) / np.sqrt(np.dot(m, m) * np.dot(mix, mix) + 1e-20))
    sf_ = son_full[:n].mean(1) if son_full.ndim == 2 else son_full[:n]
    share = float(np.sum(son ** 2) / (np.sum(sf_ ** 2) + 1e-20))
    ft, ps = _frames_pow(son)
    _, pr_ = _frames_pow(rest)
    _, pv = _frames_pow(voice[:n])
    from scipy.ndimage import maximum_filter1d
    vdb = _pow_db(pv)
    gap = (vdb < GAP_DB) | (vdb < maximum_filter1d(vdb, size=2 * int(DIP_SPAN / HOP) + 1) - DIP_DB)
    lift = _pow_db(ps + pr_) - _pow_db(pr_)
    ok_f = gap & (lift >= LIFT_DB) & (_pow_db(ps) >= SON_FLOOR_DB)
    rows = []
    for a, b in clusters([e[0] for e in evs]):
        for t in [a] + list(np.arange(a + LONG_STEP, b + 1e-9, LONG_STEP)):
            sel = (ft >= t - PRE) & (ft <= t + POST)
            if not sel.any():
                continue
            g = sel & gap
            best = float(lift[g].max()) if g.any() else None
            rows.append({'t': round(float(t), 2), 'pauseFrames': int(g.sum()), 'bestLiftInPause': None if best is None else round(best, 2),
                         'heard': bool((sel & ok_f).any())})
    heard = sum(r['heard'] for r in rows)
    sh = heard / len(rows) if rows else None
    return verdict('T1', [metric('slots measured', len(rows), '>=', 1), metric('share of slots heard in a pause', sh, '>=', AUDIBLE_SHARE),
                          metric('declared bands share of data-stem energy', share, '>=', BAND_SHARE), metric('stems ~ master in band r', r_mix, '>=', STEM_MATCH_R),
                          metric('data sounds delivered as their own stem (sonify)', sname == 'sonify', '==', True)],
                   details=[{'events': src, 'dataStem': sname, 'bandsHz': bands, 'slots': len(rows), 'heard': heard,
                             'slotsWithoutPause': sum(1 for r in rows if not r['pauseFrames'])}, *[r for r in rows if not r['heard']][:15]])


# ---- L1 (K2, sổ gu G-006): the data sounds do not cover the voice --------------------------------------------
SPEECH_BAND = (1000.0, 4000.0)  # Hz: consonants and upper formants, where masking costs intelligibility
L1_WIN = 0.1                    # s: windows where the voice is active (voice stem RMS > −45 dBFS, as A07)
L1_PRESENT_DB = -80.0           # dBFS: a window "has a data sound" when the data stem's 1–4 kHz level is above this
L1_RATIO_DB = 20.0              # dB: PROVISIONAL, voice over data sound in 1–4 kHz, 10th percentile of the windows that have a data sound
L1_PCT = 10


def _asr_audio(ctx, x, tag):
    """Own ASR of a stem mix, cut sentence by sentence exactly as asr_master (same clips, same model, same two-pass rule); cached by the audio's SHA-256."""
    import hashlib
    import json
    import os
    from common import words, write_wav_tmp
    from r_audio import asr_key, choose_pass, sentence_clips
    sents = sorted(ctx.sentences(), key=lambda s: s['start'])
    mono = (x.mean(1) if x.ndim == 2 else x).astype(np.float32)
    h = hashlib.sha256(mono.tobytes()).hexdigest()[:16]
    cp = os.path.join(ctx.cache_dir, f'asr-{tag}-{h}-{asr_key(sents)}.json')
    if os.path.exists(cp):
        return json.load(open(cp))
    from common import whisper
    mdl = whisper()
    dur = len(mono) / SR
    ws = []
    for s, (a, b, lo, hi) in zip(sents, sentence_clips(sents, dur)):
        if b - a < 0.2:
            continue
        p = write_wav_tmp(mono[int(a * SR): int(b * SR)])
        try:
            def decode(vad):
                segs, _ = mdl.transcribe(p, word_timestamps=True, beam_size=5, language='en', condition_on_previous_text=False, vad_filter=vad)
                return [{'w': w.word.strip(), 'start': round(a + w.start, 3), 'end': round(a + w.end, 3), 'sentence': s.get('id')}
                        for sg in segs for w in (sg.words or []) if lo <= (2 * a + w.start + w.end) / 2 < hi]
            ws += choose_pass(decode(False), lambda: decode(True), len(words(s.get('spoken') or s['text'])))
        finally:
            os.unlink(p)
    ws.sort(key=lambda w: w['start'])
    json.dump(ws, open(cp, 'w'))
    return ws


@rule('L1', 'DX-A1, DX-A9 (sổ gu G-006)', 'the data sounds do not cover the voice. (a) Energy: 100 ms windows where the voice stem is active (RMS > −45 dBFS); '
      '1–4 kHz band (4th-order Butterworth) of the voice stem and of the data-sound stem "sonify"; ratio = 10·log10(P_voice / P_son) per window, over the windows where the data '
      'sound is present in the band (≥ −80 dBFS); the 10th percentile of those ratios. (b) Words: own ASR (as asr_master: sentence clips, small.en, two-pass) of the sum of all stems '
      'and of the sum of all stems but sonify; key words of each sentence as A14 (numbers, names, defined terms + out/terms.json); a key word heard without the data sounds and '
      'missed with them is lost. Needs the sonify stem (MISSING without it: the data sounds must be separable to be judged)',
      'PROVISIONAL: 10th-percentile voice/data ratio in 1–4 kHz ≥ 20 dB (no window with a data sound = pass); 0 key words lost to the data sounds')
def l1_not_over_voice(ctx):
    from r_audio import key_words, match_keys
    son = stem_audio(ctx, 'sonify')
    voice = stem_audio(ctx, 'voice')
    n = min(len(son), len(voice))
    bp = lambda x: _bandpass(x[:n], [SPEECH_BAND])
    _, pv_full = _frames_pow(voice[:n], L1_WIN, L1_WIN)
    _, pv = _frames_pow(bp(voice), L1_WIN, L1_WIN)
    _, ps = _frames_pow(bp(son), L1_WIN, L1_WIN)
    act = _pow_db(pv_full) > GAP_DB
    pres = act & (_pow_db(ps) >= L1_PRESENT_DB)
    ratio = _pow_db(pv[pres]) - _pow_db(ps[pres])
    p10 = float(np.percentile(ratio, L1_PCT)) if pres.any() else None
    others = [x for x in _rest_names('sonify')]
    clean = _sum_stems(ctx, others)
    m_ = min(len(clean), len(son))
    full = clean[:m_] + son[:m_]
    sents = ctx.sentences()
    extra = ctx.json('out/terms.json').get('terms', []) if ctx.has('out/terms.json') else []
    keys = key_words(sents, extra)
    a_clean, a_full = _asr_audio(ctx, clean[:m_], 'clean'), _asr_audio(ctx, full, 'withdata')
    lost = []
    for s, k in zip(sents, keys):
        if not k:
            continue
        win = lambda asr: [w for w in asr if s['start'] - 1.5 <= w['start'] <= s['end'] + 1.5]
        miss_c, miss_f = set(match_keys(k, win(a_clean))), match_keys(k, win(a_full))
        gone = [w for w in miss_f if w not in miss_c]
        if gone:
            lost.append({'sentence': s.get('id'), 't': s['start'], 'lost': gone})
    ms = [metric('voice-active windows', int(act.sum()), '>=', 1),
          metric('voice/data 1–4 kHz ratio, 10th percentile (dB)', p10 if p10 is not None else float('inf'), '>=', L1_RATIO_DB, 'dB'),
          metric('key words lost to the data sounds', sum(len(x['lost']) for x in lost), '<=', 0)]
    return verdict('L1', ms, details=[{'windowsWithDataSound': int(pres.sum()), 'medianRatioDb': round(float(np.median(ratio)), 1) if pres.any() else None,
                                       'minRatioDb': round(float(ratio.min()), 1) if pres.any() else None, 'keyWords': sum(len(k) for k in keys)}, *lost[:15]])


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
QUIET_BED = 20.0         # dB: a bed whose median inside the silence stays within this of its level before did not go silent (a quiet passage)


@rule('T3', 'DX-R6 (sổ gu G-003)', 'intentional silences = master spans ≤ −40 dBFS (50 ms RMS, 10 ms hop) of 0.8–1.5 s (as A09). Bed = music + sfx + whoosh (+ sonify) stems summed, '
      '20 ms RMS, 5 ms hop. Reference = 90th percentile of the bed in [start − 0.8, start − 0.1]. Entry = from the last instant the bed is within 3 dB of the reference '
      '(searched in [start − 1.0, start + 0.3]) to the first instant after it the bed is 30 dB below the reference (or below −70 dBFS). Reported, not judged: a bed already below '
      '−60 dBFS before the silence (nothing to release), and a bed whose median inside the silence stays within 20 dB of the reference (a quiet passage, no cut to judge; A09 still counts it). Floor: master 50 ms RMS minimum inside the silence (edges 0.1 s excluded) and the room stem mean level there',
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
        inb = (bt >= a + 0.1) & (bt <= b - 0.1)
        row['bedInside'] = round(float(np.median(bdb[inb])), 1) if inb.any() else None
        if ref < -60 or (row['bedInside'] is not None and row['bedInside'] > ref - QUIET_BED):
            row['entry'] = None  # nothing to release (bed already silent), or the bed does not fall: a quiet passage, not a cut into silence
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
        row['judged'] = not (ref < -60 or (row['bedInside'] is not None and row['bedInside'] > ref - QUIET_BED))
        row['entryOk'] = not row['judged'] or (row['entry'] is not None and ENTRY[0] <= row['entry'] <= ENTRY[1])
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
