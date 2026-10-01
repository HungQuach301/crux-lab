"""C5 Tập 2 · luồng A: voice track + music bed (style C, sổ gu G-016 · chọn) + data sonification (palette S2 "minimal", G-005 · chọn) + mix +
master, on the time base of the video (animatic/timing.json). Code model: episodes/ep001/work/audio/src/mix.py (Tập 1 C5/C6), reused as code:
the same engine, instruments, silence gates, side-chains, ducking, master chain; only the episode's time base, sections and plan change.

    python3 episodes/ep002/audio_src/events.py && python3 episodes/ep002/audio_src/mix.py [--total 584.4] [--keep-cache]

Fixed inputs: review-c2/takes/*.mp3 (the 13 C2 takes, out/voice/takes.json; gain only, never stretched), animatic/timing.json (scene starts,
sentences with word times, the S10.1 inserted pause), animatic/src/anchors (climax), work/audio/son-plan.json (events.py), out/adbreaks.json if present.

Voice: each take decoded at 48 kHz and placed at its scene start; where timing.json inserts a pause (S10.1: 2.0 s at 9.59 s of the take) the take is
split there and the rest moved later, exactly as make_timing.py builds the animatic narration. Mono voice on both channels, unity gain before the master.

Music = Tập 1's style C (G-016 · chọn): energetic, ~1.5x the C5 tempo, D dorian (minor tonic, major IV, no sad bVI) through the problem and the
history (S01-S08), F major from the line and the answer on (S09-S13); 16th-note muted-pluck ostinato, bass on eighths, soft low thump on the
beats; pad; Leah's motif (electric piano; Tập 1's first motif, re-used); tempo fitted per scene so every cut is a downbeat; Markov chords with no
repeated 4-bar window within 24 bars (G-002); one reverb space. Level: 20 dB under the voice over voice-active windows (A07 method), as Tập 1.
Silences (G-003): chosen voice gaps at the turns of the story (+ ad-break gaps of out/adbreaks.json when present): the bed releases like a reverb
tail (tau 90 ms), room tone +8 dB as a floor, return 200 ms before the next sentence; no new note 1.3 s before. Other scene cuts: +3 dB swell.
Data sounds (G-001, G-005 · chọn S2, G-006): toolkit/audio/sonify_palettes.py `pulse` + `tick`, -16 dB under the voice's active RMS before the
side-chain, -8 dB side-chain and 1-4 kHz removed (95%) while the voice sounds, notes moved into syllable gaps; never raised. The music makes room
for them: -10 dB in the data bands (60-270 Hz, 4.5-7 kHz) while a data sound plays. Music 1-4 kHz ducked 13 dB under the voice (80 ms look-ahead).
Master: -14 LUFS integrated, true peak <= -1.5 dBTP (4x oversampled look-ahead gain), applied to every stem (the stems sum to the master).

Writes out/audio/stems/{voice,music,sonify,room,sfx,whoosh}.wav (48 kHz stereo PCM 24; sfx/whoosh silent: S2 has no sfx layer), out/audio/master.wav,
out/tempo-map.json, out/cues.json, out/sfx-events.json, out/audio/manifest.json, work/audio/report.json. Cache: work/audio/cache (deleted at the end
unless --keep-cache). Every sound is synthesised here with numpy (no samples, no third-party audio). Seeds fixed.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

import numpy as np
from scipy import signal
from scipy.ndimage import maximum_filter1d, minimum_filter1d, uniform_filter1d

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '..'))
REPO = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'toolkit', 'audio'))
sys.path.insert(0, HERE)
import sonify_palettes as S2  # noqa: E402  (palette "minimal" instruments, the owner's pick)
import events as EV  # noqa: E402  (anchors resolved on the current timing.json)

SR = 48000


def _ffmpeg():
    if os.environ.get('FFMPEG'):
        return os.environ['FFMPEG']
    if shutil.which('ffmpeg'):
        return 'ffmpeg'
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


FFMPEG = _ffmpeg()
CACHE = os.path.join(EP, 'work', 'audio', 'cache')
RNG = np.random.default_rng(20261001)
NOTE = {'C': 0, 'Db': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'Gb': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}
hz = lambda m: 440.0 * 2 ** ((np.asarray(m, float) - 69) / 12)
SON_BANDS = [(60.0, 270.0), (4500.0, 7000.0)]
MASTER_LUFS = -14.0
TP_CEIL_DB = -1.5
VOICE_OVER_MUSIC_DB = 20.0      # A07 window 18-22 dB; Tập 1 level kept (G-016: "mức dưới lời giữ nguyên")
SON_UNDER_VOICE_DB = 16.0
ROOM_DBFS = -66.0

# Silences at the turns of the story (sentence before -> sentence after); each must be a voice gap of >= 0.8 s
BEAT_SILENCES = [
    ('S01.3', 'S02.1', 'after the cold-open question (title card)'),
    ('S04.6', 'S05.1', 'after "history, not a forecast", before the first results'),
    ('S07.7', 'S08.1', 'before the worst stretch'),
    ('S08.8', 'S09.1', 'after the worst stretch, before the line'),
    ('S10.7', 'S11.1', 'after the answer, before "How we know this"'),
    ('S12.4', 'S12.5', 'before the last line, "History, not a forecast"'),
]


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


def bandpass(x, lo, hi, order=4):
    sos = signal.butter(order, [lo, hi], 'band', fs=SR, output='sos')
    return signal.sosfiltfilt(sos, x, axis=0)


# ================================================================== timeline
class TL:
    def __init__(self, total):
        t = json.load(open(EV.TIMING))
        self.timing = t
        self.total = total
        self.N = int(round(total * SR))
        self.scenes = [{'id': s['id'], 'start': float(s['start']), 'end': float(s['end']), 'sentences': s['sentences'], 'take': s['take'],
                        'inserted': s.get('inserted') or []} for s in t['scenes']]
        self.sentences = [x for s in self.scenes for x in s['sentences']]
        self.sid = {x['id']: x for x in self.sentences}

    def voice_gaps(self, voice):
        """Voice-free spans (20 ms RMS < -45 dBFS) between consecutive sentences: [{'a','b','start','end'}] (start = voice end, end = next onset)."""
        w = int(0.02 * SR)
        e = 20 * np.log10(np.sqrt(np.maximum(uniform_filter1d(voice ** 2, w), 0)) + 1e-12)
        act = e > -45
        out = []
        for a, b in zip(self.sentences, self.sentences[1:]):
            i0, i1 = int((a['end'] - 0.4) * SR), int((b['start'] + 0.4) * SR)
            seg = ~act[i0:i1]
            # longest inactive run in the window
            d = np.diff(np.concatenate([[0], seg.astype(np.int8), [0]]))
            st, en = np.where(d == 1)[0], np.where(d == -1)[0]
            if not len(st):
                continue
            k = int(np.argmax(en - st))
            out.append({'a': a['id'], 'b': b['id'], 'start': (i0 + st[k]) / SR, 'end': (i0 + en[k]) / SR,
                        'sceneCut': a['id'].split('.')[0] != b['id'].split('.')[0]})
        return out


SECTION = {'S01': 'cold', 'S02': 'promise', 'S03': 'curious', 'S04': 'curious', 'S05': 'build1', 'S06': 'build1', 'S07': 'build1',
           'S08': 'build2', 'S09': 'release', 'S10': 'answer', 'S11': 'thin', 'S12': 'resolve', 'S13': 'resolve'}
FUNCTION = {'cold': 'cold open: the dated change and the open question; drive held back (thump on 1 and 3), no melody',
            'promise': 'why private loans: light drive, first statement of Leah\'s motif',
            'curious': "Leah's loan, the head start and the promise of the replay: full drive, Leah's motif (electric piano)",
            'build1': 'the contradiction, the cushion and the two kinds of history: drive, bass on eighths',
            'build2': 'the worst stretch (April 1977): fullest drive, crescendo to "43% more"',
            'release': 'the line: F major, the drive returns lighter as the head start widens',
            'answer': 'the answer in two halves: F major, steady',
            'thin': '"How we know this" (method card): thin pad only',
            'resolve': 'warm close and end screen: sparse, Leah\'s motif, tail'}
BPM = {'cold': 108, 'promise': 114, 'curious': 120, 'build1': 126, 'build2': 132, 'release': 126, 'answer': 120, 'thin': 100, 'resolve': 108}
GAIN_DB = {'cold': -2.0, 'promise': -1.5, 'curious': -0.5, 'build1': 0.5, 'build2': 1.5, 'release': 1.0, 'answer': 0.0, 'thin': -1.0, 'resolve': -1.0}
KEYS = ('D dorian', 'F major')
LAST_MINOR = 8          # S01-S08 D dorian, S09-S13 F major


def key_of(sid):
    return KEYS[0] if int(sid[1:]) <= LAST_MINOR else KEYS[1]


def picture_cuts(tl):
    """Cuts inside scenes (dips to another picture): out/transitions.json when present, else the anchors whose id starts with 'cut'."""
    if os.path.exists(os.path.join(EP, 'out', 'transitions.json')):
        # the dips of out/transitions.json ('Sxx/<anchor>'), re-resolved on the current timing through their anchors
        ts = [EV.A[tuple(c['to'].split('/'))] for c in J('out/transitions.json')['cuts'] if '/' in c['to']]
    else:
        ts = [t for (sc, i), t in EV.A.items() if i.startswith('cut')]
    return sorted(t for t in ts if not any(abs(t - s['start']) < 0.05 for s in tl.scenes))


def tempo_grid(tl):
    """Per scene, per segment between picture cuts (scene cut + dips inside the scene, >= 2.5 s apart): beats from the cut to the next cut, an
    integer number of 4-beat bars when the tempo stays within 8% of the section's, else an integer number of beats (the last bar is short).
    Every cut is a downbeat (R04, A12). bpm per scene = the segment tempi weighted by duration."""
    beats, bars, bpms = [], [], {}
    inner = picture_cuts(tl)
    for s in tl.scenes:
        target = BPM[SECTION[s['id']]]
        cuts = [s['start']]
        for t in inner:
            if s['start'] + 2.5 <= t <= s['end'] - 2.5 and t - cuts[-1] >= 2.5:
                cuts.append(t)
        edges = cuts + [s['end']]
        i = 0
        wsum = 0.0
        for a, z in zip(edges, edges[1:]):
            D = z - a
            nb_bar = max(1, round(D / (240.0 / target)))
            bpm = 240.0 * nb_bar / D
            if abs(bpm / target - 1) <= 0.08:
                nbeats = 4 * nb_bar
            else:
                nbeats = max(1, round(D / (60.0 / target)))
                bpm = 60.0 * nbeats / D
            wsum += bpm * D
            bt = [a + k * 60.0 / bpm for k in range(nbeats)]
            beats += bt
            k = 0
            while k < nbeats:
                nb = min(4, nbeats - k)
                t1 = bt[k + nb] if k + nb < nbeats else z
                bars.append({'t0': bt[k], 't1': t1, 'scene': s['id'], 'i': i, 'beats': nb, 'bpm': bpm, 'segStart': k == 0})
                k += nb
                i += 1
        bpms[s['id']] = round(wsum / (s['end'] - s['start']), 3)
    return beats, bars, bpms


# ================================================================== harmony (Tập 1 tables)
CHORDS = {
    'F major': {'I': ('F', ''), 'V': ('C', ''), 'vi': ('D', 'm'), 'IV': ('Bb', ''), 'ii': ('G', 'm'), 'iii': ('A', 'm'), 'Iadd9': ('F', 'add9'), 'IVmaj7': ('Bb', 'maj7')},
    'D dorian': {'i': ('D', 'm'), 'i7': ('D', 'm7'), 'IV': ('G', ''), 'IVadd9': ('G', 'add9'), 'VII': ('C', ''), 'III': ('F', ''), 'v': ('A', 'm'), 'ii': ('E', 'm')},
}
MARKOV = {
    'F major': {'I': ['IV', 'vi', 'V', 'ii', 'iii', 'IVmaj7'], 'Iadd9': ['vi', 'IV', 'ii'], 'IV': ['I', 'V', 'ii', 'Iadd9', 'vi'], 'IVmaj7': ['V', 'I', 'iii'],
                'V': ['I', 'vi', 'IV', 'Iadd9'], 'vi': ['IV', 'ii', 'V', 'IVmaj7'], 'ii': ['V', 'I', 'IV'], 'iii': ['vi', 'IV', 'ii']},
    'D dorian': {'i': ['IV', 'VII', 'III', 'IVadd9', 'v'], 'i7': ['IV', 'VII', 'ii'], 'IV': ['i', 'VII', 'i7', 'III', 'v'], 'IVadd9': ['i', 'VII', 'III'],
                 'VII': ['IV', 'i', 'III', 'i7'], 'III': ['IV', 'VII', 'i', 'ii'], 'v': ['IV', 'VII', 'i'], 'ii': ['IV', 'i7', 'v']},
}
TONIC = {'F major': ['I', 'Iadd9', 'IV'], 'D dorian': ['i', 'i7', 'IV']}


def chord_pcs(root, q):
    r = NOTE[root]
    iv = {'m': [0, 3, 7], '': [0, 4, 7], 'm7': [0, 3, 7, 10], 'add9': [0, 4, 7, 14], 'maj7': [0, 4, 7, 11]}[q]
    return r, [(r + i) for i in iv]


def harmony(bars):
    rng = np.random.default_rng(7)
    seq = []
    first_major = f'S{LAST_MINOR + 1:02d}'
    for b in bars:
        key = key_of(b['scene'])
        for attempt in range(200):
            if b['i'] == 0:
                c = TONIC[key][rng.integers(0, len(TONIC[key]))] if seq else TONIC[key][0]
                if b['scene'] == first_major:
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


# ================================================================== instruments (numpy synthesis, Tập 1)
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


def soft_bass(f, dur, vel):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.12 * np.sin(4 * np.pi * f * t)
    env = np.minimum(1, t / 0.06) * np.exp(-t / max(0.6, 0.5 * dur)) * np.minimum(1, np.maximum(0, dur - t) / 0.2)
    return x * env * vel


def felt(f, vel):
    n = int(0.9 * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.08)
    return onepole_lp(x * np.minimum(1, t / 0.003) * np.exp(-t / 0.28), 1500) * vel


def bass_pluck(f, dur, vel):
    n = int(max(dur, 0.12) * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.18 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.05)
    env = np.minimum(1, t / 0.006) * np.exp(-t / 0.16) * np.minimum(1, np.maximum(0, n / SR - t) / 0.03)
    return x * env * vel


def thump(vel):
    n = int(0.3 * SR)
    t = np.arange(n) / SR
    f = 48 + 57 * np.exp(-t / 0.035)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR)
    return onepole_lp(x * np.minimum(1, t / 0.002) * np.exp(-t / 0.11), 260) * vel


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
    R = 0.8 * L + 0.6 * r.standard_normal(n) * env
    L[: int(0.012 * SR)] = 0
    R[: int(0.017 * SR)] = 0
    lp = signal.butter(2, 5500, 'low', fs=SR, output='sos')
    L, R = signal.sosfilt(lp, L), signal.sosfilt(lp, R)
    return L / np.sqrt(np.sum(L ** 2)), R / np.sqrt(np.sum(R ** 2))


# ================================================================== music: style C (Tập 1 render_music_styled, drive=True, bright=False)
LEAH = {'D dorian': [[62, 65, 69, 67], [62, 65, 67, 69], [69, 67, 65, 62], [62, 65, 69, 72], [65, 69, 67, 65]],
        'F major': [[65, 69, 72, 70], [65, 67, 69, 72], [72, 69, 67, 65]]}
RH = [[0, 1, 2, 3], [0, 1, 2, 2.5], [0, 0.5, 1, 2], [0, 1.5, 2, 3], [0, 1, 1.5, 3], [0, 2, 2.5, 3]]
OST16 = [[0, 2, 3, 6, 8, 10, 11, 14], [0, 3, 6, 8, 9, 11, 14, 15], [0, 2, 3, 6, 8, 11, 12, 14], [0, 3, 4, 6, 8, 10, 12, 14],
         [0, 2, 3, 5, 6, 8, 11, 14]]
ACC16 = {0, 3, 6, 8, 11, 14}
SHAPES = ['up', 'down', 'updown', 'broken', 'pedal']


def _contour(shape, tones, k):
    m = len(tones)
    if shape == 'up':
        return tones[k % m]
    if shape == 'down':
        return tones[-1 - k % m]
    if shape == 'updown':
        c = k % (2 * m - 2)
        return tones[c if c < m else 2 * m - 2 - c]
    if shape == 'broken':
        return tones[[0, 2, 1, 3, 2, 4, 3, 1][k % 8] % m]
    return tones[0] if k % 2 == 0 else tones[1 + (k // 2) % (m - 1)]


def render_music(tl, bars, seq, pauses, no_accent):
    N = tl.N
    dry = np.zeros((N, 2), np.float32)
    rng = np.random.default_rng(11)
    blocked = lambda t, pre=1.3: any(p['start'] - pre <= t <= p['end'] - 0.05 for p in pauses)
    motif_k = 0
    prev_voicing = None
    prev_fig = None
    v_lo, v_hi, v_top = 50, 61, 72
    for bi, (b, (key, cname)) in enumerate(zip(bars, seq)):
        sec = SECTION[b['scene']]
        root, q = CHORDS[key][cname]
        r, pcs = chord_pcs(root, q)
        pcl = [p % 12 for p in pcs]
        cands = []
        for inv in range(len(pcl)):
            order = pcl[inv:] + pcl[:inv]
            for low in range(v_lo, v_hi):
                if low % 12 != order[0]:
                    continue
                v = [low]
                for pc in order[1:]:
                    n_ = v[-1] + 1
                    while n_ % 12 != pc:
                        n_ += 1
                    v.append(n_)
                if v[-1] <= v_top:
                    cands.append(v)
        vo = min(cands, key=lambda v: sum(min(abs(a - c) for c in prev_voicing) for a in v) + 0.3 * rng.random()) if prev_voicing else cands[0]
        prev_voicing = vo
        dur = b['t1'] - b['t0']
        beat = 60.0 / b['bpm']
        bright = {'cold': 520, 'promise': 650, 'curious': 900, 'build1': 1000, 'build2': 1250, 'release': 1400, 'answer': 1000, 'thin': 600,
                  'resolve': 900}[sec] * 1.25
        pv = {'thin': 0.16, 'cold': 0.18}.get(sec, 0.2) * 0.8 * rng.uniform(0.92, 1.06)
        add(dry, b['t0'], pad(hz(vo if sec != 'thin' else vo[:3]), dur + 0.7, pv, bright), 0.0)
        lift = {'cold': 0.8, 'thin': 0.6, 'resolve': 0.75, 'build1': 1.1, 'build2': 1.2, 'release': 1.05}.get(sec, 1.0)
        broot = 36 + (r % 12) + (12 if (r % 12) < 2 else 0)
        if sec != 'thin':
            if sec != 'resolve':
                for e in range(2 * b['beats']):
                    t = b['t0'] + e * beat / 2
                    if blocked(t):
                        continue
                    add(dry, t, bass_pluck(hz(broot + (12 if e % 2 else 0)), 0.45 * beat, (0.2 if e % 2 == 0 else 0.12) * lift * rng.uniform(0.9, 1.05)), 0.0)
            else:
                add(dry, b['t0'], soft_bass(hz(broot), dur + 0.2, 0.14 * rng.uniform(0.9, 1.05)), 0.0)
        # accent on the cut (A12): the scene's first downbeat, none on a cut inside a silence
        if b['i'] == 0 and b['t0'] not in no_accent:
            add(dry, b['t0'], felt(hz(48 + r % 12), 0.35), 0.0)
            add(dry, b['t0'], felt(hz(55 + r % 12), 0.18), 0.1)
        if sec not in ('thin', 'resolve'):
            for k in range(b['beats']):
                t = b['t0'] + k * beat
                if (sec == 'cold' and k % 2) or blocked(t):
                    continue
                add(dry, t, thump((0.5 if k == 0 else 0.38) * lift * rng.uniform(0.9, 1.05)), 0.0)
        if sec != 'thin':
            tones = [n_ for n_ in range(57, 57 + 17) if n_ % 12 in pcl]
            for _ in range(20):
                shp = SHAPES[rng.integers(0, len(SHAPES))]
                msk_i = int(rng.integers(0, len(OST16)))
                if (shp, msk_i) != prev_fig:
                    break
            prev_fig = (shp, msk_i)
            hits = [h for h in OST16[msk_i] if h < 4 * b['beats']]
            if sec in ('cold', 'resolve'):
                hits = [h for h in hits if h % 2 == 0 or h in ACC16]
            for j, h in enumerate(hits):
                t = b['t0'] + h * beat / 4
                if blocked(t):
                    continue
                f = hz(_contour(shp, tones, j))
                v = (0.17 if h in ACC16 else 0.1) * lift * rng.uniform(0.88, 1.08)
                add(dry, t, pluck(f, 0.2, v, lp=1700), 0.22 if j % 2 else -0.22)
        # Leah's motif (electric piano)
        leah = (lambda i: LEAH['D dorian'][i % 5]) if key == 'D dorian' else (lambda i: LEAH['F major'][i % 3])

        def state(notes, vel, pan, rhythm):
            for n_, off in zip(notes, rhythm):
                tt = b['t0'] + off * beat
                if tt >= b['t1'] + 1.5 * beat or blocked(tt, 2.0):
                    continue
                add(dry, tt, epiano(hz(n_), vel=vel * rng.uniform(0.88, 1.05)), pan)
        if sec == 'promise' and b['i'] == 2:
            state(leah(0), 0.16, -0.25, RH[0])
        if sec in ('curious', 'build1', 'build2') and b['i'] % 4 == 1:
            state(leah(motif_k), 0.14, -0.25, RH[motif_k % 6])
            motif_k += 1
        if sec in ('release', 'answer') and b['i'] % 3 == 0:
            state(leah(motif_k), 0.15, -0.2, RH[motif_k % 6])
            motif_k += 1
        if sec == 'resolve' and b['i'] % 3 == 0:
            state(leah(b['i'] // 3), 0.13, -0.25, RH[b['i'] % 6])
    return dry


def music_dynamics(tl, gaps_swell, climax):
    N = tl.N
    t = np.arange(0, N, 480) / SR
    g = np.zeros(len(t))
    for s in tl.scenes:
        g[(t >= s['start']) & (t < s['end'])] = GAIN_DB[SECTION[s['id']]]
    up = np.clip((t - (climax - 20)) / 20, 0, 1) * (t <= climax)
    down = (t > climax) * np.interp(t, [climax, climax + 4, climax + 10], [3.0, -1.0, 0.0])
    g += 3.0 * up ** 2 + down
    for p in gaps_swell:
        g += 3.0 * np.clip(np.minimum((t - p['start']) / 0.3, (p['end'] - t) / 0.3), 0, 1)
    g = uniform_filter1d(g, 30)
    last = tl.sentences[-1]['end']
    g += 20 * np.log10(np.clip(t / 0.6, 1e-4, 1))
    tail = np.clip(1 - (t - (last + 0.1)) / max(0.3, tl.total - last - 0.1), 1e-4, 1)
    g += 20 * np.log10(tail)
    return np.interp(np.arange(N) / SR, t, 10 ** (g / 20))


# ================================================================== sonification (palette S2 "minimal", Tập 1)
def sonify_notes(plan, bars):
    bpm_at = lambda t: next((b['bpm'] for b in bars if b['t0'] <= t < b['t1']), 120.0)
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
                if rate > 8:
                    pv = 0.7 if (j % 3 == 0 or j == len(items) - 1) else 0.0
                    notes.append((it['t'], q(36 + 24 * it['v']), pan, pv, 0.45))
                elif rate > 4:
                    notes.append((it['t'], q(36 + 24 * it['v']), pan, 0.75 if j % 2 == 0 or j == len(items) - 1 else 0.45, 0.5))
                else:
                    notes.append((it['t'], q(36 + 24 * it['v']), pan, 0.85, 0.6))
        elif k == 'line':
            step = r.get('step') or 60.0 / bpm_at(r['t0']) / 2
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
    env = 20 * np.log10(np.sqrt(np.maximum(uniform_filter1d(voice ** 2, int(0.01 * SR)), 0)) + 1e-9)
    active = env > -40
    shifts = []
    for t, m, pan, vel, tv in notes:
        i = int(t * SR)
        if 0 <= i < N and active[i]:
            a, b = max(0, i - int(0.06 * SR)), min(N, i + int(0.12 * SR))
            j = a + int(np.argmin(env[a:b]))
            shifts.append(round((j - i) / SR * 1000, 1))
            t = j / SR
        x = S2.pulse(S2.hz(m), vel) if vel > 0 else np.zeros(int(0.45 * SR))
        tk = S2.tick(tv)
        x[:len(tk)] += tk
        S2.add(out, t, S2.pan(x, pan))
    return out, {'notes': len(notes), 'shiftedIntoGaps': len(shifts), 'medianShiftMs': float(np.median(shifts)) if shifts else 0.0}


def son_process(son, voice, gate_v):
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


# ================================================================== silences (Tập 1)
def silence_gates(tl, gaps):
    N = tl.N
    g = np.ones(N)
    lift = np.zeros(N)
    tt = np.arange(N) / SR
    rows = []
    for p in gaps:
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
        rows.append({'t': round(t0, 3), 'end': round(t1, 3), 'dur': round(t1 - t0, 3), 'after': p['a'], 'before': p['b'], 'why': p.get('why', ''),
                     'release': 'exp tau 90 ms', 'return': '200 ms', **({'adBreak': p['adBreak']} if 'adBreak' in p else {})})
    return g, lift, rows


# ================================================================== master (Tập 1)
def true_peak_gain(mix, ceil_db):
    N = len(mix)
    ceil = 10 ** (ceil_db / 20)
    pk = np.zeros(N, np.float32)
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
    gmin = minimum_filter1d(need, 2 * la + 1)
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


def a07_gap(v, m):
    w = int(0.1 * SR)
    k = min(len(v), len(m)) // w
    pv = (v[: k * w].mean(1) ** 2).reshape(k, w).mean(1)
    pm = (m[: k * w].mean(1) ** 2).reshape(k, w).mean(1)
    a = 10 * np.log10(pv + 1e-20) > -45
    return float(10 * np.log10(pv[a].mean()) - 10 * np.log10(pm[a].mean() + 1e-20))


# ================================================================== voice
def build_voice(tl):
    out = np.zeros(tl.N)
    rows = []
    for s in tl.scenes:
        v = decode(os.path.join(EP, 'review-c2', 'takes', s['take']))[:, 0]
        i0 = int(round(s['start'] * SR))
        if s['inserted']:
            ins = s['inserted'][0]
            c = int(round(ins['at_take_s'] * SR))
            P = int(round(ins['pause_s'] * SR))
            v = np.concatenate([v[:c], np.zeros(P), v[c:]])
        end = int(round(s['end'] * SR))
        n = min(len(v), end - i0, tl.N - i0)
        assert len(v) <= end - i0 + int(0.05 * SR), (s['id'], len(v) / SR, s['end'] - s['start'])
        out[i0:i0 + n] = v[:n]
        rows.append({'scene': s['id'], 'take': s['take'], 'at': s['start'], 'takeS': round(len(v) / SR, 3), 'inserted': s['inserted']})
    return out, rows


# ================================================================== main
def main():
    args = sys.argv[1:]
    tm = json.load(open(EV.TIMING))
    total = float(args[args.index('--total') + 1]) if '--total' in args else float(tm['total_s'])
    tl = TL(total)
    N = tl.N
    log('total', total, 'samples', N)
    beats, bars, bpms = tempo_grid(tl)
    seq = harmony(bars)

    voice, vrows = build_voice(tl)
    gaps = tl.voice_gaps(voice)
    gi = {(g['a'], g['b']): g for g in gaps}
    sil = []
    for a, b, why in BEAT_SILENCES:
        g = dict(gi[(a, b)], why=why)
        assert g['end'] - g['start'] >= 0.8, (a, b, g)
        sil.append(g)
    ad = []
    if os.path.exists(os.path.join(EP, 'out', 'adbreaks.json')):
        for br in J('out/adbreaks.json')['breaks']:
            t = br['t'] if isinstance(br, dict) else br
            g = [x for x in gaps if x['start'] - 0.05 <= t <= x['end'] + 0.05]
            if not g:
                log(f'WARNING ad break {t} is not inside a voice gap of this timing: ignored (out/adbreaks.json not re-timed yet?)')
                continue
            if not any(s['a'] == g[0]['a'] for s in sil):
                ad.append(dict(g[0], adBreak=t, why='ad break (out/adbreaks.json)'))
            else:
                next(s for s in sil if s['a'] == g[0]['a'])['adBreak'] = t
    silences_all = sorted(sil + ad, key=lambda p: p['start'])
    log('silences', [(round(p['start'], 2), round(p['end'] - p['start'], 2)) for p in silences_all])
    silent_cuts = [s['start'] for s in tl.scenes if any(p['start'] - 0.05 <= s['start'] <= p['end'] + 0.05 for p in silences_all)]
    swell = [g for g in gaps if g['sceneCut'] and not any(g['a'] == p['a'] for p in silences_all)]

    vr = np.sqrt(np.maximum(uniform_filter1d(voice ** 2, int(0.1 * SR)), 0))
    act = (20 * np.log10(vr + 1e-12) > -45).astype(float)
    la = int(0.08 * SR)
    gate_v_duck = smooth_gate(np.concatenate([act[la:], np.zeros(la)]), 0.04, 0.35)
    e10 = 20 * np.log10(np.sqrt(np.maximum(uniform_filter1d(voice ** 2, int(0.01 * SR)), 0)) + 1e-9)
    act_s = maximum_filter1d((e10 > -40).astype(float), int(0.06 * SR))
    gate_v_son = smooth_gate(act_s, 0.02, 0.25)
    del e10, act_s, vr

    climax = EV.A[('S08', 'more')]

    def _music():
        log('music: arrangement', len(bars), 'bars')
        dry = render_music(tl, bars, seq, silences_all, set(silent_cuts))
        log('music: reverb')
        irL, irR = reverb_ir()
        wetL = signal.oaconvolve(dry[:, 0], irL)[:N]
        wetR = signal.oaconvolve(dry[:, 1], irR)[:N]
        m = dry + 0.24 * np.stack([wetL, wetR], 1)
        m *= music_dynamics(tl, swell, climax)[:, None]
        return m.astype(np.float32)
    music = cached('music', _music).astype(np.float64)

    plan = J('work/audio/son-plan.json')['rows']
    notes = sonify_notes(plan, bars)
    log('sonify:', len(notes), 'notes')
    son, son_stats = render_sonify(tl, notes, voice)
    son = son_process(son, voice, gate_v_son)

    log('mix')
    bed_gate, room_lift, silences = silence_gates(tl, silences_all)
    duck_mid = 10 ** (-13 * gate_v_duck / 20)
    for ch in range(2):
        mid = bandpass(music[:, ch], 1000, 4000)
        music[:, ch] = music[:, ch] - mid + mid * duck_mid
    del duck_mid, mid
    senv = maximum_filter1d(np.abs(son).max(1), int(0.03 * SR))
    thr = 0.1 * np.percentile(senv[senv > 1e-7], 95) if (senv > 1e-7).any() else 1.0
    dip = 10 ** (-10 * smooth_gate(np.clip(senv / thr, 0, 1), 0.015, 0.25) / 20)
    del senv
    for ch in range(2):
        for lo, hi in SON_BANDS:
            b = bandpass(music[:, ch], lo * 0.85, hi * 1.15)
            music[:, ch] = music[:, ch] - b + b * dip
    del dip, b
    music *= bed_gate[:, None]
    son *= bed_gate[:, None]
    vt = act > 0
    pv = np.mean(voice[vt] ** 2)
    pm = np.mean(music[vt].mean(1) ** 2)
    music *= np.sqrt(pv / pm) * 10 ** (-VOICE_OVER_MUSIC_DB / 20)
    wn = RNG.standard_normal(N)
    pink = signal.lfilter([0.049922035, -0.095993537, 0.050612699, -0.004408786], [1, -2.494956002, 2.017265875, -0.522189400], wn)
    del wn
    pink = onepole_lp(pink, 3500)
    pink = pink / np.sqrt(np.mean(pink ** 2))
    room = np.stack([pink, 0.85 * np.roll(pink, 480) + 0.15 * pink], 1)
    del pink
    room *= (1 + (10 ** (8 / 20) - 1) * room_lift)[:, None]
    voice2 = np.stack([voice, voice], 1)
    stems = {'voice': voice2, 'music': music, 'sonify': son}
    I0 = ebur128(voice2 + music + son)['I']
    gain = 10 ** ((MASTER_LUFS - I0) / 20)
    for k in ('voice', 'music', 'sonify'):
        stems[k] *= gain
    stems['room'] = room * 10 ** (ROOM_DBFS / 20)
    del room
    mix = sum(stems.values())
    I1 = ebur128(mix)['I']
    g2 = 10 ** ((MASTER_LUFS - I1) / 20)
    mix *= g2
    log('limiter')
    gl = true_peak_gain(mix, TP_CEIL_DB) * g2
    del mix
    for k in stems:
        stems[k] *= gl[:, None]
    master = sum(stems.values())
    m = ebur128(master)
    log('master', m)

    sd = os.path.join(EP, 'out', 'audio', 'stems')
    os.makedirs(sd, exist_ok=True)
    files = {}
    zeros = np.zeros((N, 2))
    for k, v in list(stems.items()) + [('sfx', zeros), ('whoosh', zeros)]:
        p = os.path.join(sd, k + '.wav')
        write_wav(p + '.tmp.wav', v)
        os.replace(p + '.tmp.wav', p)
        files[f'out/audio/stems/{k}.wav'] = p
    del zeros
    mp = os.path.join(EP, 'out', 'audio', 'master.wav')
    write_wav(mp + '.tmp.wav', master)
    os.replace(mp + '.tmp.wav', mp)
    files['out/audio/master.wav'] = mp

    accents = [round(s['start'], 3) for s in tl.scenes[1:] if s['start'] not in silent_cuts]
    json.dump({'_about': 'Music tempo map of Tập 2 (audio_src/mix.py, style C): beats from each scene cut to the next, tempo fitted per scene so every '
                         'cut is a downbeat (dips inside a scene from out/transitions.json split the scene into segments, each fitted the same way); accents = the scene cuts (a soft felt-piano downbeat), except cuts inside a chosen silence (bed silent there). '
                         'bpm = median of the per-scene tempi.',
               'bpm': round(float(np.median(list(bpms.values()))), 2), 'bpmByScene': bpms, 'beats': [round(b, 4) for b in beats], 'accents': accents,
               'bars': [{'t': round(b['t0'], 4), 'scene': b['scene'], 'beats': b['beats'], 'chord': c[1], 'key': c[0]} for b, c in zip(bars, seq)]},
              open(os.path.join(EP, 'out', 'tempo-map.json'), 'w'), indent=1)
    cues = []
    for s in tl.scenes:
        sec = SECTION[s['id']]
        cues.append({'t': round(s['start'], 3), 'end': round(s['end'], 3), 'scene': s['id'], 'function': FUNCTION[sec], 'key': key_of(s['id']),
                     'tempo': bpms[s['id']], 'layer': 'music', 'section': sec, 'levelDb': GAIN_DB[sec]})
    cues.append({'t': 0.0, 'end': round(total, 3), 'function': 'data sonification, palette S2 "minimal" (sổ gu G-005 · chọn): soft low pulse MIDI 36-62 + '
                 'filtered tick 4.5-7 kHz; bands 60-270 Hz + 4.5-7 kHz; events out/sonify-events.json', 'key': 'D minor pentatonic (= F major pentatonic)',
                 'tempo': None, 'layer': 'sonify'})
    cues.append({'t': 0.0, 'end': round(total, 3), 'function': 'room tone floor (pink noise, one space); +8 dB inside the silences', 'key': None,
                 'tempo': None, 'layer': 'room'})
    json.dump({'_about': 'Cue sheet of the Tập 2 C5 mix (audio_src/mix.py). Music = Tập 1 style C (G-016 · chọn) on the 13 scenes of script v5. '
                         'Silences = chosen voice gaps at the turns of the story (sổ gu G-003; the script has no [beat] marks) + ad-break gaps (adBreak).',
               'cues': cues, 'silences': silences}, open(os.path.join(EP, 'out', 'cues.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'_about': 'Sound effects: none. Palette S2 "minimal" has no sfx layer (sfx and whoosh stems are silent). Data sounds are their own stem '
                         '(sonify): out/sonify-events.json.', 'events': []}, open(os.path.join(EP, 'out', 'sfx-events.json'), 'w'), indent=1)

    def band_share(x):
        mono = x.mean(1)
        tot = np.sum(mono ** 2) + 1e-20
        return float(sum(np.sum(bandpass(mono, lo, hi) ** 2) for lo, hi in SON_BANDS) / tot)
    rep = {'total_s': total, 'samples': N, 'master': m, 'limiterMinGainDb': round(float(20 * np.log10(gl.min() / g2)), 2),
           'limiterGainBelow1dBShare': round(float((gl / g2 < 10 ** (-1 / 20)).mean()), 5), 'preGainLUFS': I0,
           'voiceOverMusicDb_A07': round(a07_gap(stems['voice'], stems['music']), 2), 'voiceOverMusicTargetDb': VOICE_OVER_MUSIC_DB,
           'sonUnderVoiceDb': SON_UNDER_VOICE_DB, 'sonification': son_stats, 'sonBandShare': band_share(stems['sonify']),
           'silences': silences, 'swellCuts': [round(g['start'], 3) for g in swell], 'bpmByScene': bpms, 'bars': len(bars), 'voice': vrows,
           'stemLevelsDbfs': {k: round(float(10 * np.log10(np.mean(v ** 2) + 1e-20)), 2) for k, v in stems.items()},
           'sumMinusMasterMax': float(np.abs(sum(stems.values()) - master).max())}
    json.dump(rep, open(os.path.join(EP, 'work', 'audio', 'report.json'), 'w'), indent=1)
    man = {'_about': 'Audio files of the Tập 2 C5 mix; this manifest records them (SHA-256, size). Rebuild: python3 episodes/ep002/audio_src/events.py && '
                     'python3 episodes/ep002/audio_src/mix.py (deterministic seeds). Stems: 48 kHz stereo PCM 24-bit, same time base as out/video.mp4 '
                     '(animatic/timing.json), at mix level: their sum is the master.',
           'generator': 'episodes/ep002/audio_src/mix.py', 'timing': {'path': os.path.relpath(EV.TIMING, EP), 'total_s': total, 'sha256': sha256(EV.TIMING)},
           'sampleRate': SR, 'files': {rel: {'sha256': sha256(p), 'bytes': os.path.getsize(p)} for rel, p in files.items()},
           'master': {'integratedLUFS': m['I'], 'truePeakDbtp': m['TP'], 'LRA': m['LRA']}}
    json.dump(man, open(os.path.join(EP, 'out', 'audio', 'manifest.json'), 'w'), indent=1)
    if '--keep-cache' not in args:
        shutil.rmtree(CACHE, ignore_errors=True)
    log('done', json.dumps({k: rep[k] for k in ('master', 'limiterMinGainDb', 'voiceOverMusicDb_A07', 'sonBandShare', 'stemLevelsDbfs')}))


if __name__ == '__main__':
    main()
