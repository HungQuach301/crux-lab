"""C5 audio stream (Tập 1): music bed + data sonification (palette S2 "minimal") + mix + master, on the time base of the video.

    python3 episodes/ep001/work/audio/src/mix.py [--total 591.7333] [--stage all|music|sonify|mix]

Fixed inputs (never regenerated, re-timed or stretched): review-c4/narration-v32.m4a (final voice, owner-approved at C4), animatic/timing.json
(sentences, [beat] pauses, scene cuts), out/sonify-events.json + work/audio/son-plan.json (events.py).

Writes
  out/audio/stems/{voice,music,sfx,whoosh,room,sonify}.wav   48 kHz stereo 24-bit, same time base as the video, at mix level:
                                                              the sum of the stems IS the master (master gain and limiter gain applied to every stem)
  out/audio/master.wav                                        -14 LUFS integrated, true peak <= -1.5 dBTP before AAC (A01, A02)
  out/tempo-map.json, out/cues.json, out/sfx-events.json      (checks/CONTRACT.md schemas)
  out/audio/manifest.json                                     SHA-256 + size of every wav (the wavs are not committed)
  work/audio/report.json                                      levels, silences, sonification stats
Cache (resumable stages): work/audio/cache/*.npy (not committed).

Every sound is synthesised here with numpy (no samples, no third-party audio; RIGHTS: A-MUSIC). Seeds fixed.

Music = the cue sheet's plan (preprod/cue-sheet.md), re-timed to the 20 scenes of v3.2: D minor through the break-even story (S01-S13),
F major for Walt and Anjali and the answer (S14-S20); pad, soft pulse, Nora's motif (electric piano), Walt (low plucks), Anjali (high bells),
one reverb space. Tempo per scene fitted so every cut is a downbeat. Chords come from a seeded Markov walk that never repeats a 4-bar window
within 24 bars (sổ gu G-002: no audible loop).
Silences (sổ gu G-003): the 13 script [beat] pauses and the 2 ad-break scene gaps (out/adbreaks.json, S14; music only, no accent on those cuts): the bed releases like a reverb tail (tau 90 ms), room tone rises 8 dB as a floor, return 200 ms.
Data sounds (G-001, G-005 · chọn S2, G-006): toolkit/audio/sonify_palettes.py instruments `pulse` + `tick` (palette minimal), level -16 dB under
the voice before the side-chain, -8 dB side-chain and 1-4 kHz removed while the voice sounds, notes moved into syllable gaps; never raised.
The music makes room for them instead: -10 dB in the data bands (60-270 Hz, 4.5-7 kHz) while a data sound plays.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time

import numpy as np
from scipy import signal
from scipy.ndimage import maximum_filter1d, minimum_filter1d, uniform_filter1d

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REPO = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'toolkit', 'audio'))
import sonify_palettes as S2  # noqa: E402  (palette "minimal" instruments, the owner's pick)

SR = 48000
FFMPEG = os.environ.get('FFMPEG', 'ffmpeg')
CACHE = os.path.join(EP, 'work', 'audio', 'cache')
RNG = np.random.default_rng(20260929)
NOTE = {'C': 0, 'Db': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'Gb': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}
hz = lambda m: 440.0 * 2 ** ((np.asarray(m, float) - 69) / 12)
SON_BANDS = [(60.0, 270.0), (4500.0, 7000.0)]
MASTER_LUFS = -14.0
TP_CEIL_DB = -1.5
VOICE_OVER_MUSIC_DB = 20.0      # A07 window: 18-22 dB
SON_UNDER_VOICE_DB = 16.0       # palette rule: -16 dB under the voice's active RMS, before the side-chain
ROOM_DBFS = -66.0               # room tone floor (post-master), +8 dB inside the silences


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def J(rel):
    return json.load(open(os.path.join(EP, rel)))


def decode(path, ch=1):
    raw = subprocess.run([FFMPEG, '-v', 'error', '-i', path, '-map', '0:a:0', '-f', 'f32le', '-ac', str(ch), '-ar', str(SR), '-'],
                         check=True, capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, ch).astype(np.float64)


def write_wav(path, x, bits=24):
    import soundfile as sf
    sf.write(path, np.clip(x, -1, 1), SR, subtype='PCM_24' if bits == 24 else 'FLOAT')


def ebur128(x):
    with tempfile.TemporaryDirectory() as d:
        w = os.path.join(d, 'm.wav')
        write_wav(w, x, bits=32)
        o = subprocess.run([FFMPEG, '-nostats', '-v', 'info', '-i', w, '-af', 'ebur128=peak=true:framelog=quiet', '-f', 'null', '-'],
                           capture_output=True, text=True).stderr
    txt = o[o.rfind('Summary:'):]
    g = lambda k: float(re.search(k + r':\s+(-?[\d.inf]+)', txt).group(1))
    return {'I': g('I'), 'LRA': g('LRA'), 'TP': g('Peak')}


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def cached(name, fn):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, name + '.npy')
    if os.path.exists(p):
        log('cache', name)
        return np.load(p)
    x = fn()
    np.save(p + '.tmp.npy', x)
    os.replace(p + '.tmp.npy', p)
    return x


def smooth_gate(target, att, rel, hop=48):
    """One-pole attack/release follower of a 0..1 target, computed per hop samples (fast), interpolated back."""
    n = len(target)
    blocks = target[: (n // hop) * hop].reshape(-1, hop).max(1)
    out = np.zeros(len(blocks))
    aa, ar = np.exp(-hop / (att * SR)), np.exp(-hop / (rel * SR))
    cur = 0.0
    for i, t in enumerate(blocks):
        c = aa if t > cur else ar
        cur = t + (cur - t) * c
        out[i] = cur
    g = np.repeat(out, hop)
    return np.concatenate([g, np.full(n - len(g), g[-1] if len(g) else 0.0)])


def bandpass(x, lo, hi, order=4, zero_phase=True):
    sos = signal.butter(order, [lo, hi], 'band', fs=SR, output='sos')
    return signal.sosfiltfilt(sos, x, axis=0) if zero_phase else signal.sosfilt(sos, x, axis=0)


# ================================================================== timeline
class TL:
    def __init__(self, total):
        t = J('animatic/timing.json')
        self.total = total
        self.N = int(round(total * SR))
        self.scenes = []
        sc = t['scenes']
        for i, s in enumerate(sc):
            end = sc[i + 1]['start'] if i + 1 < len(sc) else total
            self.scenes.append({'id': s['id'], 'start': float(s['start']), 'end': float(end), 'sentences': s['sentences']})
        self.sentences = [x for s in sc for x in s['sentences']]
        self.beats_pauses = [p for p in t['pauses'] if p['kind'] == 'beat']
        self.scene_gaps = [p for p in t['pauses'] if p['kind'] == 'scene']
        # ad breaks (out/adbreaks.json, stream D): each sits in a scene-cut voice gap; the bed goes silent there as in a [beat] pause (S14: the master
        # needs >= 1 s <= -40 dBFS around the break). Voice untouched; the new act's music comes back 200 ms before its first sentence.
        br = [b['t'] if isinstance(b, dict) else b for b in J('out/adbreaks.json')['breaks']]
        self.ad_gaps = []
        for b in br:
            g = [p for p in self.scene_gaps if p['start'] <= b <= p['end']]
            assert g, f'ad break {b} is not inside a scene-cut voice gap'
            self.ad_gaps.append(dict(g[0], adBreak=b))


SECTION = {'S01': 'cold', 'S02': 'promise', 'S03': 'curious', 'S04': 'curious', 'S05': 'curious', 'S06': 'curious', 'S07': 'curious',
           'S08': 'build1', 'S09': 'build1', 'S10': 'build2', 'S11': 'build2', 'S12': 'release', 'S13': 'answer',
           'S14': 'walt', 'S15': 'walt', 'S16': 'walt', 'S17': 'anjali', 'S18': 'anjali', 'S19': 'thin', 'S20': 'resolve'}
BPM = {'cold': 72, 'promise': 76, 'curious': 84, 'build1': 88, 'build2': 92, 'release': 92, 'answer': 84, 'walt': 88, 'anjali': 88, 'thin': 70, 'resolve': 76}
FUNCTION = {'cold': 'suspense under the open question: pad and a slow low pulse, no melody',
            'promise': "the offer and the promise: pad, soft pulse, first statement of Nora's motif",
            'curious': "curious, light pulse; Nora's motif (electric piano)",
            'build1': 'build through the break-even and the balance gap: eighth-note pulse, bass on each bar',
            'build2': 'build to the climax ("Never", the quarter point): fuller pad, pulse and bass, crescendo',
            'release': 'release on the full point (18 months): open pad',
            'answer': "the half-point answer: warm, Nora's motif resolved",
            'walt': 'Walt: F major, low plucked motif, light pulse',
            'anjali': 'Anjali: high bells, light pulse; resolves on the three-mark ruler',
            'thin': 'what the numbers do not say: thin pad only',
            'resolve': 'resolved: three motifs together, sparse; tail into the end'}
GAIN_DB = {'cold': -2.0, 'promise': -1.5, 'curious': -0.5, 'build1': 0.5, 'build2': 1.5, 'release': 1.0, 'answer': 0.0, 'walt': 0.0, 'anjali': 0.5,
           'thin': -1.0, 'resolve': -1.0}


def key_of(sid):
    return 'D minor' if int(sid[1:]) <= 13 else 'F major'


def tempo_grid(tl):
    """Per scene: beats from the cut to the next cut; an integer number of 4-beat bars when the tempo stays within 8% of the section's,
    else an integer number of beats (the scene's last bar is short). Returns beats, bars [(t0, t1, scene, index in scene, beats in bar)], per-scene bpm."""
    beats, bars, bpms = [], [], {}
    for s in tl.scenes:
        D = s['end'] - s['start']
        target = BPM[SECTION[s['id']]]
        nb_bar = max(1, round(D / (240.0 / target)))
        bpm = 240.0 * nb_bar / D
        if abs(bpm / target - 1) <= 0.08:
            nbeats = 4 * nb_bar
        else:
            nbeats = max(1, round(D / (60.0 / target)))
            bpm = 60.0 * nbeats / D
        bpms[s['id']] = round(bpm, 3)
        bt = [s['start'] + k * 60.0 / bpm for k in range(nbeats)]
        beats += bt
        k = 0
        i = 0
        while k < nbeats:
            nb = min(4, nbeats - k)
            t0 = bt[k]
            t1 = bt[k + nb] if k + nb < nbeats else s['end']
            bars.append({'t0': t0, 't1': t1, 'scene': s['id'], 'i': i, 'beats': nb, 'bpm': bpm})
            k += nb
            i += 1
    return beats, bars, bpms


# ================================================================== harmony
CHORDS = {
    'D minor': {'i': ('D', 'm'), 'VI': ('Bb', ''), 'III': ('F', ''), 'VII': ('C', ''), 'iv': ('G', 'm'), 'v': ('A', 'm'), 'i7': ('D', 'm7'), 'VIsus': ('Bb', 'add9')},
    'F major': {'I': ('F', ''), 'V': ('C', ''), 'vi': ('D', 'm'), 'IV': ('Bb', ''), 'ii': ('G', 'm'), 'iii': ('A', 'm'), 'Iadd9': ('F', 'add9'), 'IVmaj7': ('Bb', 'maj7')},
}
MARKOV = {
    'D minor': {'i': ['VI', 'VII', 'iv', 'III', 'v', 'VIsus'], 'i7': ['iv', 'VI', 'VII'], 'VI': ['VII', 'III', 'iv', 'i', 'i7'], 'VIsus': ['VII', 'i', 'III'],
                'III': ['VII', 'VI', 'iv', 'i'], 'VII': ['i', 'III', 'VI', 'i7', 'v'], 'iv': ['i', 'VI', 'VII', 'v', 'i7'], 'v': ['VI', 'i', 'iv']},
    'F major': {'I': ['IV', 'vi', 'V', 'ii', 'iii', 'IVmaj7'], 'Iadd9': ['vi', 'IV', 'ii'], 'IV': ['I', 'V', 'ii', 'Iadd9', 'vi'], 'IVmaj7': ['V', 'I', 'iii'],
                'V': ['I', 'vi', 'IV', 'Iadd9'], 'vi': ['IV', 'ii', 'V', 'IVmaj7'], 'ii': ['V', 'I', 'IV'], 'iii': ['vi', 'IV', 'ii']},
}
TONIC = {'D minor': ['i', 'i7', 'VI'], 'F major': ['I', 'Iadd9', 'IV']}


def chord_pcs(root, q):
    r = NOTE[root]
    iv = {'m': [0, 3, 7], '': [0, 4, 7], 'm7': [0, 3, 7, 10], 'add9': [0, 4, 7, 14], 'maj7': [0, 4, 7, 11]}[q]
    return r, [(r + i) for i in iv]


def harmony(bars):
    rng = np.random.default_rng(7)
    seq = []
    for b in bars:
        key = key_of(b['scene'])
        for attempt in range(200):
            if b['i'] == 0:
                c = TONIC[key][rng.integers(0, len(TONIC[key]))] if seq else TONIC[key][0]
                if b['scene'] in ('S14',):
                    c = 'I'
            else:
                prev = seq[-1][1] if seq and seq[-1][0] == key else TONIC[key][0]
                opts = MARKOV[key][prev]
                c = opts[rng.integers(0, len(opts))]
            cand = [s[1] for s in seq] + [c]
            if len(cand) >= 4:
                w = cand[-4:]
                hist = [s[1] for s in seq[-24:]]
                if any(hist[j:j + 4] == w for j in range(0, max(0, len(hist) - 3))):
                    continue
            if seq and seq[-1][1] == c and attempt < 150:
                continue
            break
        seq.append((key, c))
    return seq


# ================================================================== instruments (numpy synthesis)
def onepole_lp(x, fc):
    a = np.exp(-2 * np.pi * fc / SR)
    return signal.lfilter([1 - a], [1, -a], x)


def pad(freqs, dur, vel, bright):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for f in freqs:
        for det in (-0.0045, 0.0, 0.0052):
            x += 2 * ((f * (1 + det) * t + RNG.uniform(0, 1)) % 1.0) - 1
    x /= 3 * len(freqs)
    # low-pass whose cutoff opens a little through the bar (two passes of a one-pole, slowly varying in 1024-sample steps)
    cut = bright * (0.65 + 0.35 * np.minimum(1, t / max(0.5 * dur, 1e-3)))
    y = np.zeros(n)
    z1 = z2 = 0.0
    for i in range(0, n, 1024):
        a = np.exp(-2 * np.pi * cut[i] / SR)
        seg, zf = signal.lfilter([1 - a], [1, -a], x[i:i + 1024], zi=[z1])
        z1 = zf[0]
        seg2, zf2 = signal.lfilter([1 - a], [1, -a], seg, zi=[z2])
        z2 = zf2[0]
        y[i:i + 1024] = seg2
    env = np.minimum(1, t / 0.45) * np.minimum(1, np.maximum(0, dur - t) / 0.5)
    return y * env * vel


def pluck(f, dur=0.45, vel=1.0, lp=2200):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t) + 0.15 * np.sin(6 * np.pi * f * t)
    env = np.minimum(1, t / 0.004) * np.exp(-t / 0.13)
    return onepole_lp(x * env, lp) * vel


def epiano(f, dur=1.4, vel=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    mod = 1.3 * np.exp(-t / 0.3) * np.sin(2 * np.pi * f * t)
    x = np.sin(2 * np.pi * f * t + mod)
    env = np.minimum(1, t / 0.008) * np.exp(-t / 0.65)
    return x * env * vel


def bell(f, dur=1.8, vel=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    mod = 1.8 * np.exp(-t / 0.5) * np.sin(2 * np.pi * f * 3.5 * t)
    x = np.sin(2 * np.pi * f * t + mod)
    env = np.minimum(1, t / 0.005) * np.exp(-t / 0.9)
    return onepole_lp(x * env, 5000) * vel


def soft_bass(f, dur, vel):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.12 * np.sin(4 * np.pi * f * t)
    env = np.minimum(1, t / 0.06) * np.exp(-t / max(0.6, 0.5 * dur)) * np.minimum(1, np.maximum(0, dur - t) / 0.2)
    return x * env * vel


def felt(f, vel):
    """A soft felt-piano note for the cut downbeats (the accents): muted, short, low-passed."""
    n = int(0.9 * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.08)
    return onepole_lp(x * np.minimum(1, t / 0.003) * np.exp(-t / 0.28), 1500) * vel


def add(buf, t, sig, pan=0.0, g=1.0):
    i0 = int(round(t * SR))
    if i0 >= len(buf) or i0 + len(sig) <= 0:
        return
    s0 = max(0, -i0)
    i0 = max(0, i0)
    n = min(len(sig) - s0, len(buf) - i0)
    a = (np.clip(pan, -1, 1) + 1) * np.pi / 4
    buf[i0:i0 + n, 0] += sig[s0:s0 + n] * np.cos(a) * g * np.sqrt(2)
    buf[i0:i0 + n, 1] += sig[s0:s0 + n] * np.sin(a) * g * np.sqrt(2)


def reverb_ir(rt60=1.9, seed=7):
    n = int(rt60 * SR)
    t = np.arange(n) / SR
    env = np.exp(-6.9 * t / rt60)
    r = np.random.default_rng(seed)
    L = r.standard_normal(n) * env
    R = 0.8 * L + 0.6 * r.standard_normal(n) * env  # correlated room: mono-safe (A05, A06)
    L[: int(0.012 * SR)] = 0
    R[: int(0.017 * SR)] = 0
    lp = signal.butter(2, 5500, 'low', fs=SR, output='sos')
    L, R = signal.sosfilt(lp, L), signal.sosfilt(lp, R)
    return L / np.sqrt(np.sum(L ** 2)), R / np.sqrt(np.sum(R ** 2))


# ================================================================== music
NORA = {'D minor': [[62, 65, 69, 67], [62, 65, 67, 69], [69, 67, 65, 62], [62, 65, 69, 72], [65, 69, 67, 65]],
        'F major': [[65, 69, 72, 70], [65, 67, 69, 72], [72, 69, 67, 65]]}
WALT = [[41, 48, 53, 45], [41, 45, 48, 53], [48, 45, 41, 43], [41, 48, 45, 48]]
ANJ = [[84, 81, 77, 79], [81, 84, 86, 84], [77, 81, 84, 81], [84, 79, 81, 77]]
RH = [[0, 1, 2, 3], [0, 1, 2, 2.5], [0, 0.5, 1, 2], [0, 1.5, 2, 3], [0, 1, 1.5, 3], [0, 2, 2.5, 3]]


def render_music(tl, bars, seq, pauses):
    N = tl.N
    dry = np.zeros((N, 2), np.float32)
    rng = np.random.default_rng(11)
    # no new pulse note in the 1.3 s before a silence, no motif note in the 2.0 s before it: the pad alone carries into the silence, so the
    # release is heard as one gesture (sổ gu G-003), not as a pluck dying out
    blocked = lambda t, pre=1.3: any(p['start'] - pre <= t <= p['end'] - 0.05 for p in pauses)
    motif_k = {'nora': 0, 'walt': 0, 'anj': 0}
    prev_voicing = None
    for bi, (b, (key, cname)) in enumerate(zip(bars, seq)):
        sec = SECTION[b['scene']]
        root, q = CHORDS[key][cname]
        r, pcs = chord_pcs(root, q)
        # voicing: chord tones stacked upwards from a low note in MIDI 50-60 (each inversion), top <= 72; the one nearest to the previous
        # voicing is kept (smooth voice leading; re-voiced every bar)
        pcl = [p % 12 for p in pcs]
        cands = []
        for inv in range(len(pcl)):
            order = pcl[inv:] + pcl[:inv]
            for low in range(50, 61):
                if low % 12 != order[0]:
                    continue
                v = [low]
                for pc in order[1:]:
                    n_ = v[-1] + 1
                    while n_ % 12 != pc:
                        n_ += 1
                    v.append(n_)
                if v[-1] <= 72:
                    cands.append(v)
        if prev_voicing:
            vo = min(cands, key=lambda v: sum(min(abs(a - c) for c in prev_voicing) for a in v) + 0.3 * rng.random())
        else:
            vo = cands[0]
        prev_voicing = vo
        dur = b['t1'] - b['t0']
        beat = 60.0 / b['bpm']
        bright = {'cold': 520, 'promise': 650, 'curious': 900, 'build1': 1000, 'build2': 1250, 'release': 1400, 'answer': 1000, 'walt': 950,
                  'anjali': 1100, 'thin': 600, 'resolve': 900}[sec]
        pv = {'thin': 0.16, 'cold': 0.18}.get(sec, 0.2) * rng.uniform(0.92, 1.06)
        voices = vo if sec != 'thin' else vo[:3]
        add(dry, b['t0'], pad(hz(voices), dur + 0.7, pv, bright), 0.0)
        # bass: a soft sustained root on the bar (not in the thin section)
        if sec not in ('thin',):
            bv = {'cold': 0.16, 'build1': 0.22, 'build2': 0.26, 'release': 0.2}.get(sec, 0.17)
            add(dry, b['t0'], soft_bass(hz(36 + (r % 12) + (12 if (r % 12) < 2 else 0)), dur + 0.2, bv * rng.uniform(0.9, 1.05)), 0.0)
        # accent on the cut: the scene's first downbeat (A12: accents land on cuts)
        if b['i'] == 0 and not any(a['start'] <= b['t0'] <= a['end'] for a in tl.ad_gaps):  # none on an ad-break cut (bed silent there)
            add(dry, b['t0'], felt(hz(48 + r % 12), 0.35), 0.0)
            add(dry, b['t0'], felt(hz(55 + r % 12 + (0 if 'm' in q else 0)), 0.18), 0.1)
        # pulse
        pat = (bi // 4 + (1 if b['scene'] in ('S06', 'S10', 'S15', 'S18') else 0)) % 3
        for k in range(b['beats']):
            t = b['t0'] + k * beat
            if sec in ('cold', 'thin', 'resolve'):
                if sec == 'cold' and k in (0, 2) and not blocked(t):  # slow low pulse, no melody (cue sheet)
                    add(dry, t, pluck(hz(48 + (r % 12 if r % 12 < 7 else r % 12 - 12)), 0.6, 0.22 if k == 0 else 0.14, lp=900), 0.0)
                continue
            if blocked(t):
                continue
            offs = {'promise': [[0.0], [0.0], [0.0, 0.5]][pat] if k in (0, 2) else [],
                    'curious': [[0.0], [0.0, 0.5], [0.0]][pat] if not (pat == 2 and k == 3) else [0.5],
                    'build1': [[0.0, 0.5], [0.0, 0.75], [0.5]][pat],
                    'build2': [[0.0, 0.5], [0.0, 0.5, 0.75], [0.0, 0.25, 0.5]][pat],
                    'release': [0.0],
                    'answer': [[0.0], [0.0, 0.5], [0.5]][pat] if k != 3 else [],
                    'walt': [[0.0], [0.5], [0.0, 0.5]][pat],
                    'anjali': [[0.0, 0.5], [0.5], [0.0, 0.75]][pat]}[sec]
            for o in offs:
                tt = t + o * beat
                if blocked(tt):
                    continue
                deg = [0, 7, 12, 7, 3 if 'm' in q else 4][(k * 2 + int(o * 2) + bi) % 5]
                f = hz(60 + (r % 12) + deg - (12 if (r % 12) + deg > 12 else 0))
                v = (0.3 if (k == 0 and o == 0) else 0.2) * rng.uniform(0.85, 1.1) * (1.15 if sec == 'build2' else 1.0)
                add(dry, tt, pluck(f, 0.4, v, lp=1800 if sec != 'build2' else 2400), 0.18 if (k + int(o * 2)) % 2 else -0.18)
        # motifs
        def state(kind, notes, inst, vel, pan, rhythm):
            for n_, off in zip(notes, rhythm):
                tt = b['t0'] + off * beat
                if tt >= b['t1'] + 1.5 * beat or blocked(tt, 2.0):
                    continue
                add(dry, tt, inst(hz(n_), vel=vel * rng.uniform(0.88, 1.05)), pan)
        if sec in ('promise',) and b['i'] == 2:
            state('nora', NORA['D minor'][0], epiano, 0.16, -0.25, RH[0])
        if sec in ('curious', 'build1') and b['i'] % 4 == 1:
            k_ = motif_k['nora']
            motif_k['nora'] += 1
            state('nora', NORA['D minor'][k_ % 5], epiano, 0.15 if sec == 'curious' else 0.13, -0.25, RH[k_ % 6])
        if sec == 'build2' and b['i'] % 4 == 1:
            k_ = motif_k['nora']
            motif_k['nora'] += 1
            nn = [n_ - 12 if k_ % 2 else n_ for n_ in NORA['D minor'][k_ % 5]]
            state('nora', nn, epiano, 0.12, -0.25, RH[(k_ + 2) % 6])
        if sec in ('release', 'answer') and b['i'] % 3 == 0:
            k_ = motif_k['nora']
            motif_k['nora'] += 1
            state('nora', NORA['D minor'][3 if sec == 'answer' else 1], epiano, 0.16, -0.2, RH[k_ % 6])
        if sec == 'walt' and b['i'] % 2 == 1:
            k_ = motif_k['walt']
            motif_k['walt'] += 1
            state('walt', WALT[k_ % 4], lambda f, vel: pluck(f, 0.7, vel, lp=1200), 0.32, -0.35, RH[k_ % 6])
        if sec == 'anjali' and b['i'] % 2 == 1:
            k_ = motif_k['anj']
            motif_k['anj'] += 1
            state('anj', ANJ[k_ % 4], bell, 0.075, 0.35, RH[(k_ + 1) % 6])
        if sec == 'anjali' and b['scene'] == 'S18' and b['i'] % 4 == 2:
            k_ = motif_k['walt']
            motif_k['walt'] += 1
            state('walt', WALT[k_ % 4], lambda f, vel: pluck(f, 0.7, vel, lp=1200), 0.26, -0.35, RH[k_ % 6])
        if sec == 'resolve':
            which = b['i'] % 3
            k_ = b['i']
            if which == 0:
                state('nora', NORA['F major'][k_ % 3], epiano, 0.14, -0.25, RH[k_ % 6])
            elif which == 1:
                state('walt', WALT[k_ % 4], lambda f, vel: pluck(f, 0.7, vel, lp=1200), 0.26, -0.35, RH[(k_ + 3) % 6])
            else:
                state('anj', ANJ[k_ % 4], bell, 0.06, 0.35, RH[(k_ + 1) % 6])
    return dry


def music_dynamics(tl, bars):
    """Section levels (dB), a crescendo into the climax ("Never", S11) and a swell of +3 dB in the gaps between scenes (the transition)."""
    N = tl.N
    t = np.arange(0, N, 480) / SR  # 10 ms control rate
    g = np.zeros(len(t))
    for s in tl.scenes:
        sel = (t >= s['start']) & (t < s['end'])
        g[sel] = GAIN_DB[SECTION[s['id']]]
    A = {(a['scene'], a['id']): a['resolved_s'] for a in J('animatic/anchors.json')['anchors']}
    climax = A[('S11', 'never')]
    up = np.clip((t - (climax - 20)) / 20, 0, 1) * (t <= climax)
    down = (t > climax) * np.interp(t, [climax, climax + 4, climax + 10], [3.0, -1.0, 0.0])
    g += 3.0 * up ** 2 + down
    for p in tl.scene_gaps:
        if any(p['start'] == a['start'] for a in tl.ad_gaps):
            continue  # ad break: the bed goes silent instead of swelling
        g += 3.0 * np.clip(np.minimum((t - p['start']) / 0.3, (p['end'] - t) / 0.3), 0, 1)
    g = uniform_filter1d(g, 30)
    # fade in at the head (0.6 s), tail: out over the last 1.8 s after the last sentence
    last = tl.sentences[-1]['end']
    g += 20 * np.log10(np.clip(t / 0.6, 1e-4, 1))
    tail = np.clip(1 - (t - (last + 0.1)) / max(0.3, tl.total - last - 0.1), 1e-4, 1)
    g += 20 * np.log10(tail)
    return np.interp(np.arange(N) / SR, t, 10 ** (g / 20))


# ================================================================== sonification (palette S2 "minimal")
def sonify_notes(plan, bars):
    """Plan rows -> notes (t, midi, pan, vel, tick_vel)."""
    bpm_at = lambda t: next((b['bpm'] for b in bars if b['t0'] <= t < b['t1']), 84.0)
    notes = []
    q = S2.qpenta
    for r in plan:
        k = r['kind']
        if k == 'bar':
            p_end = q(36 + 24 * r['v'])
            pan = np.clip((r['x'] - 960) / 960, -0.7, 0.7)
            d = r['t1'] - r['t0']
            if d <= 0.35:
                notes.append((r['t0'], p_end, pan, 1.0, 0.8))
            else:
                n = max(2, int(round(d / 0.25)) + 1)
                p0 = q(36 + 24 * r['v'] * 0.35)
                for j in range(n):
                    u = j / (n - 1)
                    notes.append((r['t0'] + u * d, q(p0 + u * (p_end - p0)), pan, 1.0 if j in (0, n - 1) else 0.62, 0.8 if j in (0, n - 1) else 0.3))
        elif k == 'dot':
            notes.append((r['t0'], q(38 + 24 * (1 - np.clip(r['y'], 0, 1080) / 1080)), np.clip((r['x'] - 960) / 960, -0.7, 0.7), 1.0, 0.8))
        elif k == 'roll':
            items = r['items']
            rate = len(items) / max(1e-3, r['t1'] - r['t0'])
            for j, it in enumerate(items):
                pan = np.clip((it['x'] - 960) / 960, -0.7, 0.7)
                if rate > 8:  # the cue sheet: above 8 events/s the ticks merge into a soft roll; pulses on every 3rd item and the last
                    pv = 0.7 if (j % 3 == 0 or j == len(items) - 1) else 0.0
                    notes.append((it['t'], q(36 + 24 * it['v']), pan, pv, 0.45))
                elif rate > 4:
                    notes.append((it['t'], q(36 + 24 * it['v']), pan, 0.75 if j % 2 == 0 or j == len(items) - 1 else 0.45, 0.5))
                else:
                    notes.append((it['t'], q(36 + 24 * it['v']), pan, 0.85, 0.6))
        elif k == 'line':
            step = r.get('step') or 60.0 / bpm_at(r['t0']) / 2  # eighth notes of the music (palette rule)
            t = r['t0']
            d = max(r['t1'] - r['t0'], 0.05)
            while t <= r['t1'] + 1e-6:
                u = (t - r['t0']) / d
                s = 0.8 * np.sin(2 * np.pi * u * 2.5) if r.get('wobble') else r['slope']
                x = r['x0'] + u * (r['x1'] - r['x0'])
                notes.append((t, q(43 + 7 * np.tanh(1.2 * s)), np.clip((x - 960) / 960, -0.7, 0.7), 0.7, 0.35))
                t += step
    notes.sort(key=lambda n: n[0])
    return notes


def render_sonify(tl, notes, voice):
    N = tl.N
    out = np.zeros((N, 2))
    env = 20 * np.log10(np.sqrt(uniform_filter1d(voice ** 2, int(0.01 * SR))) + 1e-9)
    active = env > -40
    shifts = []
    placed = []
    for t, m, pan, vel, tv in notes:
        i = int(t * SR)
        if 0 <= i < N and active[i]:  # into the nearest syllable gap, -60..+120 ms (palette rule)
            a, b = max(0, i - int(0.06 * SR)), min(N, i + int(0.12 * SR))
            j = a + int(np.argmin(env[a:b]))
            shifts.append(round((j - i) / SR * 1000, 1))
            t = j / SR
        x = S2.pulse(S2.hz(m), vel) if vel > 0 else np.zeros(int(0.45 * SR))
        tk = S2.tick(tv)
        x[:len(tk)] += tk
        S2.add(out, t, S2.pan(x, pan))
        placed.append(round(t, 3))
    return out, {'notes': len(notes), 'shiftedIntoGaps': len(shifts), 'medianShiftMs': float(np.median(shifts)) if shifts else 0.0}, placed


def son_process(son, voice, gate_v):
    """Palette rules: level -16 dB under the voice's active RMS; while the voice is active: -8 dB side-chain and 1-4 kHz removed (95%)."""
    va = voice[np.abs(voice) > 1e-4]
    sm = np.abs(son).max(1)
    sa = son[sm > 1e-5]
    target = np.sqrt(np.mean(va ** 2)) * 10 ** (-SON_UNDER_VOICE_DB / 20)
    son = son * (target / (np.sqrt(np.mean(sa ** 2)) + 1e-12))
    duck = 10 ** (-8 * gate_v / 20)
    for ch in range(2):
        mid = bandpass(son[:, ch], 1000, 4000)
        son[:, ch] = (son[:, ch] - mid + mid * (1 - 0.95 * gate_v)) * duck
    return son


# ================================================================== silences
def silence_gates(tl, gaps=None):
    """Script [beat] pauses: bed release like a reverb tail (exp, tau 90 ms) from the end of the sentence, room tone +8 dB over 250 ms, return in 200 ms
    just before the next sentence. Returns (bed gain, room lift 0..1, list of silences)."""
    N = tl.N
    g = np.ones(N)
    lift = np.zeros(N)
    tt = np.arange(N) / SR
    rows = []
    for p in (tl.beats_pauses if gaps is None else gaps):
        t0, t1 = p['start'], p['end']
        i0, i1 = int(t0 * SR), int((t1 - 0.2) * SR)
        if i1 <= i0 + int(0.2 * SR):
            i1 = int((t1 - 0.1) * SR)
        seg = tt[i0:i1] - t0
        g[i0:i1] = np.minimum(g[i0:i1], np.exp(-seg / 0.09))
        r = int(0.2 * SR)
        g[i1:i1 + r] = np.minimum(g[i1:i1 + r], np.exp(-(tt[i1] - t0) / 0.09) + (1 - np.exp(-(tt[i1] - t0) / 0.09)) * (np.linspace(0, 1, r) ** 2))
        k0, k1 = int((t0 - 0.05) * SR), int((t0 + 0.2) * SR)
        lift[k0:k1] = np.maximum(lift[k0:k1], np.linspace(0, 1, k1 - k0))
        lift[k1:i1] = 1
        lift[i1:i1 + r] = np.maximum(lift[i1:i1 + r], np.linspace(1, 0, r))
        rows.append({'t': round(t0, 3), 'end': round(t1, 3), 'dur': round(t1 - t0, 3), 'beforeSentence': p['before_n'], 'release': 'exp tau 90 ms', 'return': '200 ms',
                     **({'adBreak': p['adBreak']} if 'adBreak' in p else {})})
    return g, lift, rows


# ================================================================== master
def true_peak_gain(mix, ceil_db):
    N = len(mix)
    ceil = 10 ** (ceil_db / 20)
    pk = np.zeros(N)
    CH, OV = SR * 20, 512
    for i0 in range(0, N, CH):
        a0, a1 = max(0, i0 - OV), min(N, i0 + CH + OV)
        up = signal.resample_poly(mix[a0:a1], 4, 1, axis=0)
        p_ = np.abs(up).max(1)
        p_ = p_[: (len(p_) // 4) * 4].reshape(-1, 4).max(1)
        n = min(CH, N - i0)
        pk[i0:i0 + n] = p_[i0 - a0:i0 - a0 + n]
    need = np.minimum(1, ceil / np.maximum(pk, 1e-9))
    la = int(0.005 * SR)
    gmin = minimum_filter1d(need, 2 * la + 1)  # 5 ms look-ahead (centred window)
    # release: 80 ms one-pole back towards 1, computed on 1 ms blocks, never above the instantaneous need
    hop = 48
    nb = N // hop
    blk = gmin[: nb * hop].reshape(nb, hop).min(1)
    out = np.empty(nb)
    a = np.exp(-hop / (0.08 * SR))
    cur = 1.0
    for i in range(nb):
        cur = min(blk[i], 1 - (1 - cur) * a)
        out[i] = cur
    g = np.interp(np.arange(N), np.arange(nb) * hop + hop / 2, out)
    g = np.minimum(uniform_filter1d(g, int(0.002 * SR)), gmin)
    return g


# ================================================================== main
def main():
    args = sys.argv[1:]
    total = float(args[args.index('--total') + 1]) if '--total' in args else 17739 / 30  # video: 17 739 frames at 30 fps (S18 sửa 30/09; trước: 17 752)
    tl = TL(total)
    N = tl.N
    log('total', total, 'samples', N)
    beats, bars, bpms = tempo_grid(tl)
    seq = harmony(bars)
    pauses = tl.beats_pauses + tl.ad_gaps  # render_music: no new pulse/motif note running into a silence

    # ---- voice (the approved narration, decoded; gain only)
    def _voice():
        v = decode(os.path.join(EP, 'review-c4', 'narration-v32.m4a'))[:, 0]
        out = np.zeros(N)
        n = min(len(v), N)
        out[:n] = v[:n]
        return out
    voice = cached('voice', _voice)
    vr = np.sqrt(np.maximum(uniform_filter1d(voice ** 2, int(0.1 * SR)), 0))
    act = (20 * np.log10(vr + 1e-12) > -45).astype(float)
    la = int(0.08 * SR)                               # music 1-4 kHz duck: 80 ms look-ahead (the dip is in place when the first consonant lands)
    gate_v_duck = smooth_gate(np.concatenate([act[la:], np.zeros(la)]), 0.04, 0.35)
    e10 = 20 * np.log10(np.sqrt(uniform_filter1d(voice ** 2, int(0.01 * SR))) + 1e-9)
    act_s = maximum_filter1d((e10 > -40).astype(float), int(0.06 * SR))
    gate_v_son = smooth_gate(act_s, 0.02, 0.25)      # palette side-chain

    # ---- music (dry arrangement + one reverb space)
    def _music():
        log('music: arrangement', len(bars), 'bars')
        dry = render_music(tl, bars, seq, pauses)
        log('music: reverb')
        irL, irR = reverb_ir()
        wetL = signal.oaconvolve(dry[:, 0], irL)[:N]
        wetR = signal.oaconvolve(dry[:, 1], irR)[:N]
        m = dry + 0.24 * np.stack([wetL, wetR], 1)
        m *= music_dynamics(tl, bars)[:, None]
        return m.astype(np.float32)
    music = cached('music', _music).astype(np.float64)

    # ---- sonification
    plan = J('work/audio/son-plan.json')['rows']
    notes = sonify_notes(plan, bars)

    def _son():
        log('sonify:', len(notes), 'notes')
        s, st, placed = render_sonify(tl, notes, voice)
        json.dump({'stats': st, 'placed': placed}, open(os.path.join(CACHE, 'son-stats.json'), 'w'))
        return s.astype(np.float32)
    son = cached('sonify_raw', _son).astype(np.float64)
    son_stats = json.load(open(os.path.join(CACHE, 'son-stats.json')))['stats']
    son = son_process(son, voice, gate_v_son)

    # ---- mix moves
    log('mix')
    bed_gate, room_lift, silences = silence_gates(tl)
    ad_gate, ad_lift, ad_rows = silence_gates(tl, tl.ad_gaps)  # ad breaks: music (and room lift) only; a data sound starting at the cut stays whole
    silences = sorted(silences + ad_rows, key=lambda r: r['t'])
    # music: 1-4 kHz ducked 13 dB under the voice (band-limited dip, A08)
    duck_mid = 10 ** (-13 * gate_v_duck / 20)
    for ch in range(2):
        mid = bandpass(music[:, ch], 1000, 4000)
        music[:, ch] = music[:, ch] - mid + mid * duck_mid
    # music makes room for the data sounds in their bands (-10 dB while a data sound plays)
    senv = maximum_filter1d(np.abs(son).max(1), int(0.03 * SR))
    thr = 0.1 * np.percentile(senv[senv > 1e-7], 95) if (senv > 1e-7).any() else 1.0
    sact = np.clip(senv / thr, 0, 1)
    dip = 10 ** (-10 * smooth_gate(sact, 0.015, 0.25) / 20)
    for ch in range(2):
        for lo, hi in SON_BANDS:
            b = bandpass(music[:, ch], lo * 0.85, hi * 1.15)
            music[:, ch] = music[:, ch] - b + b * dip
    # silences
    music *= (bed_gate * ad_gate)[:, None]
    son *= bed_gate[:, None]
    # level: music VOICE_OVER_MUSIC_DB under the voice over voice-active windows (as A07 measures it)
    vt = act > 0
    pv = np.mean(voice[vt] ** 2)
    pm = np.mean(music[vt].mean(1) ** 2)
    music *= np.sqrt(pv / pm) * 10 ** (-VOICE_OVER_MUSIC_DB / 20)
    # room tone: quiet pink noise, one space
    wn = RNG.standard_normal(N)
    pink = signal.lfilter([0.049922035, -0.095993537, 0.050612699, -0.004408786], [1, -2.494956002, 2.017265875, -0.522189400], wn)
    pink = onepole_lp(pink, 3500)
    pink = pink / np.sqrt(np.mean(pink ** 2))
    room = np.stack([pink, 0.85 * np.roll(pink, 480) + 0.15 * pink], 1)
    room *= (1 + (10 ** (8 / 20) - 1) * np.maximum(room_lift, ad_lift))[:, None]
    voice2 = np.stack([voice, voice], 1)
    zeros = np.zeros((N, 2))
    stems = {'voice': voice2, 'music': music, 'sfx': zeros, 'whoosh': zeros.copy(), 'room': room * 0.0, 'sonify': son}
    # loudness (room tone set after the gain so its absolute level is known)
    mix = voice2 + music + son
    I0 = ebur128(mix)['I']
    gain = 10 ** ((MASTER_LUFS - I0) / 20)
    for k in ('voice', 'music', 'sonify'):
        stems[k] = stems[k] * gain
    stems['room'] = room * 10 ** (ROOM_DBFS / 20)
    mix = sum(stems.values())
    I1 = ebur128(mix)['I']
    g2 = 10 ** ((MASTER_LUFS - I1) / 20)
    for k in stems:
        stems[k] = stems[k] * g2
    mix = mix * g2
    log('limiter')
    gl = true_peak_gain(mix, TP_CEIL_DB)
    for k in stems:
        stems[k] = stems[k] * gl[:, None]
    master = sum(stems.values())
    m = ebur128(master)
    log('master', m)

    # ---- write
    sd = os.path.join(EP, 'out', 'audio', 'stems')
    os.makedirs(sd, exist_ok=True)
    files = {}
    for k, v in stems.items():
        p = os.path.join(sd, k + '.wav')
        write_wav(p + '.tmp.wav', v)
        os.replace(p + '.tmp.wav', p)
        files[f'out/audio/stems/{k}.wav'] = p
    mp = os.path.join(EP, 'out', 'audio', 'master.wav')
    write_wav(mp + '.tmp.wav', master)
    os.replace(mp + '.tmp.wav', mp)
    files['out/audio/master.wav'] = mp

    # ---- declared files
    accents = [round(s['start'], 3) for s in tl.scenes[1:] if not any(a['start'] <= s['start'] <= a['end'] for a in tl.ad_gaps)]
    json.dump({'_about': 'Music tempo map (work/audio/src/mix.py): beats from each cut to the next, tempo fitted per scene so every cut is a downbeat; '
                         'accents = the cuts (a soft felt-piano downbeat), except the two ad-break cuts (out/adbreaks.json), where the bed is silent. bpm = the section tempo per scene.',
               'bpm': round(float(np.median(list(bpms.values()))), 2), 'bpmByScene': bpms, 'beats': [round(b, 4) for b in beats], 'accents': accents,
               'bars': [{'t': round(b['t0'], 4), 'scene': b['scene'], 'beats': b['beats'], 'chord': c[1], 'key': c[0]} for b, c in zip(bars, seq)]},
              open(os.path.join(EP, 'out', 'tempo-map.json'), 'w'), indent=1)
    cues = []
    for s in tl.scenes:
        sec = SECTION[s['id']]
        cues.append({'t': round(s['start'], 3), 'end': round(s['end'], 3), 'scene': s['id'], 'function': FUNCTION[sec], 'key': key_of(s['id']),
                     'tempo': bpms[s['id']], 'layer': 'music', 'section': sec, 'levelDb': GAIN_DB[sec]})
    cues.append({'t': 0.0, 'end': round(total, 3), 'function': 'data sonification, palette S2 "minimal" (sổ gu G-005 · chọn): soft low pulse MIDI 36-62 + filtered tick 4.5-7 kHz; '
                 'bands for T1 60-270 Hz + 4.5-7 kHz', 'key': 'D minor pentatonic (= F major pentatonic)', 'tempo': None, 'layer': 'sonify'})
    cues.append({'t': 0.0, 'end': round(total, 3), 'function': 'room tone floor (pink noise, one space); +8 dB inside the silences', 'key': None, 'tempo': None, 'layer': 'room'})
    json.dump({'_about': 'Cue sheet of the C5 mix (work/audio/src/mix.py). Music follows preprod/cue-sheet.md re-timed to the 20 scenes of v3.2. '
                         'Silences = the script [beat] pauses (sổ gu G-003) + the two ad-break scene gaps (adBreak; music only).', 'cues': cues, 'silences': silences},
              open(os.path.join(EP, 'out', 'cues.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'_about': 'Sound effects: none. Palette S2 "minimal" has no sfx layer and the picture has no sound-effect events (whoosh and sfx stems are '
                         'silent). Data sounds are their own stem (sonify): out/sonify-events.json.', 'events': []},
              open(os.path.join(EP, 'out', 'sfx-events.json'), 'w'), indent=1)

    # ---- report + manifest
    def band_share(x):
        mono = x.mean(1)
        tot = np.sum(mono ** 2) + 1e-20
        return float(sum(np.sum(bandpass(mono, lo, hi) ** 2) for lo, hi in SON_BANDS) / tot)
    rep = {'total_s': total, 'samples': N, 'master': m, 'limiterMinGainDb': round(float(20 * np.log10(gl.min())), 2),
           'limiterGainBelow1dBShare': round(float((gl < 10 ** (-1 / 20)).mean()), 5), 'preGainLUFS': I0,
           'voiceOverMusicDb': VOICE_OVER_MUSIC_DB, 'sonUnderVoiceDb': SON_UNDER_VOICE_DB, 'sonification': son_stats,
           'sonBandShare': band_share(stems['sonify']), 'silences': silences, 'bpmByScene': bpms, 'bars': len(bars),
           'stemLevelsDbfs': {k: round(float(10 * np.log10(np.mean(v ** 2) + 1e-20)), 2) for k, v in stems.items()},
           'sumMinusMasterMax': float(np.abs(sum(stems.values()) - master).max())}
    json.dump(rep, open(os.path.join(EP, 'work', 'audio', 'report.json'), 'w'), indent=1)
    man = {'_about': 'Audio files of the C5 mix are not committed (size); this manifest records them. Rebuild: python3 episodes/ep001/work/audio/src/events.py && '
                     'python3 episodes/ep001/work/audio/src/mix.py (deterministic seeds). Stems: 48 kHz stereo PCM 24-bit, same time base as out/video.mp4, '
                     'at mix level: their sum is the master.',
           'generator': 'episodes/ep001/work/audio/src/mix.py', 'total_s': total, 'sampleRate': SR,
           'files': {rel: {'sha256': sha256(p), 'bytes': os.path.getsize(p)} for rel, p in files.items()},
           'master': {'integratedLUFS': m['I'], 'truePeakDbtp': m['TP'], 'LRA': m['LRA']}}
    json.dump(man, open(os.path.join(EP, 'out', 'audio', 'manifest.json'), 'w'), indent=1)
    log('done', json.dumps({k: rep[k] for k in ('master', 'limiterMinGainDb', 'sonBandShare', 'stemLevelsDbfs')}))


if __name__ == '__main__':
    main()
