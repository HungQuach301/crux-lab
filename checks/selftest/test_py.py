"""Self-test of every Python rule: for each rule a small fixture it MUST fail and one it MUST pass.

    python3 checks/selftest/test_py.py [--only F01,A07] [--keep]

Fixtures are synthetic (ffmpeg lavfi / numpy). Rules that listen to speech get a fixed transcript through the ASR cache
(out/checks/cache/asr-<video sha>.json): the rule logic is under test, not the speech recogniser. Frame rules are tested end-to-end in test_page.js;
here their Python verdicts are fed a page.json directly."""
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf
from scipy import signal

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'py'))
import common  # noqa: E402
import run as runner  # noqa: E402,F401  (registers every rule)

SR = 48000
RULES = {fn.rid: fn for fn in common.RULES}


class F:
    def __init__(self, name):
        self.root = tempfile.mkdtemp(prefix=f'kpy-{name}-')

    def p(self, rel):
        p = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        return p

    def json(self, rel, obj):
        json.dump(obj, open(self.p(rel), 'w'))

    def text(self, rel, s):
        open(self.p(rel), 'w').write(s)

    def wav(self, rel, x, sr=SR):
        sf.write(self.p(rel), np.asarray(x, np.float32), sr, subtype='FLOAT')

    def ff(self, *args):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', *args], check=True)

    def video(self, rel='out/video.mp4', size='320x180', rate=30, dur=1.0, src='testsrc2', vargs=None, audio=None, aargs=None, tags=True, extra_in=None):
        """lavfi video (+ optional numpy stereo audio muxed as AAC 320k 48k)."""
        args = ['-f', 'lavfi', '-i', f'{src}=size={size}:rate={rate}:duration={dur}']
        if audio is not None:
            ap = self.p('tmp/audio.wav')
            sf.write(ap, audio, SR, subtype='FLOAT')
            args += ['-i', ap]
        args += ['-map', '0:v']
        if audio is not None:
            args += ['-map', '1:a', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-ac', '2'] + (aargs or [])
        v = vargs if vargs is not None else ['-c:v', 'libx264', '-preset', 'ultrafast', '-profile:v', 'high', '-pix_fmt', 'yuv420p']
        if tags:
            v = v + ['-vf', 'scale=out_color_matrix=bt709:out_range=tv', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-color_range', 'tv']
        self.ff(*args, *v, '-shortest', self.p(rel))

    def raw_video(self, frames, rel='out/video.mp4', fps=30, crf='12', gray=True):
        """frames: iterable of uint8 arrays (h, w) luma or (h, w, 3) rgb."""
        frames = list(frames)
        h, w = frames[0].shape[:2]
        pix = 'gray' if frames[0].ndim == 2 else 'rgb24'
        p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', pix, '-s', f'{w}x{h}', '-r', str(fps), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast',
                              '-crf', crf, '-pix_fmt', 'yuv420p', self.p(rel)], stdin=subprocess.PIPE)
        for fr in frames:
            p.stdin.write(np.ascontiguousarray(fr, np.uint8).tobytes())
        p.stdin.close()
        p.wait()

    def asr(self, words):
        """Fixed transcript through the ASR cache (key: video SHA-256 + the sentence windows of out/script.json, written before)."""
        import r_audio
        h = common.sha256_file(self.p('out/video.mp4'))[:16]
        sents = json.load(open(self.p('out/script.json')))['sentences'] if os.path.exists(self.p('out/script.json')) else []
        self.json(f'out/checks/cache/asr-{h}-{r_audio.asr_key(sorted(sents, key=lambda s: s["start"]))}.json', words)

    def asr_stems(self, clean, full):
        """Fixed transcripts for L1's two stem mixes (all stems but sonify / all stems), keyed as r_sound._asr_audio keys them."""
        import r_audio
        import r_sound
        ctx = common.Ctx(self.root)
        sents = sorted(ctx.sentences(), key=lambda s: s['start'])
        c = r_sound._sum_stems(ctx, r_sound._rest_names('sonify'))
        s_ = r_audio.stem_audio(ctx, 'sonify')
        m = min(len(c), len(s_))
        for tag, x, ws in (('clean', c[:m], clean), ('withdata', c[:m] + s_[:m], full)):
            mono = x.mean(1).astype(np.float32)
            h = hashlib.sha256(mono.tobytes()).hexdigest()[:16]
            self.json(f'out/checks/cache/asr-{tag}-{h}-{r_audio.asr_key(sents)}.json', ws)

    def contract(self, **kw):
        """Episode contract (K2): contract.json at the fixture root."""
        self.json('contract.json', {'episode': 'fixture', **kw})

    def run(self, rid):
        return common.safe(RULES[rid], common.Ctx(self.root))

    def close(self):
        shutil.rmtree(self.root, ignore_errors=True)


# ---- signal helpers --------------------------------------------------------------------------------
rng = np.random.default_rng(7)


def noise(sec, lo=100, hi=6000):
    x = rng.standard_normal(int(sec * SR))
    sos = signal.butter(4, [lo, hi], btype='bandpass', fs=SR, output='sos')
    y = signal.sosfilt(sos, x)
    return y / np.sqrt(np.mean(y ** 2))


def db(x):
    return 10 ** (x / 20)


def programme(sec=40, block=2.0, levels=(-20, -28), corr=0.9):
    """Stereo programme of alternating loud/quiet blocks; channels share most of the signal (phase correlation ≈ corr)."""
    base = noise(sec)
    side = noise(sec)
    k = int(block * SR)
    env = np.concatenate([np.full(k, db(levels[(i // k) % len(levels)])) for i in range(0, len(base), k)])[: len(base)]
    a = np.sqrt((1 + corr) / 2)
    b = np.sqrt((1 - corr) / 2)
    L = (a * base + b * side) * env
    R = (a * base - b * side) * env
    return np.stack([L, R], 1)


def tone_bursts(sec, times, dur=0.08, freq=880, level=-12):
    x = np.zeros(int(sec * SR))
    t = np.arange(int(dur * SR)) / SR
    burst = np.sin(2 * np.pi * freq * t) * np.exp(-t * 30) * db(level)
    for s in times:
        i = int(s * SR)
        x[i:i + len(burst)] += burst[: len(x) - i]
    return x


def to_lufs(F, x, target):
    """Scale a stereo signal to an integrated loudness target (two passes through ffmpeg's ebur128)."""
    for _ in range(2):
        p = F.p('tmp/l.wav')
        sf.write(p, x, SR, subtype='FLOAT')
        I = common.ebur128(p)['I']
        x = x * db(target - I)
    return x


# ---- fixtures ----------------------------------------------------------------------------------------
T = {}


def case(rid):
    def deco(fn):
        T[rid] = fn
        return fn
    return deco


V_HIGH = ['-c:v', 'libx264', '-preset', 'ultrafast', '-profile:v', 'high', '-pix_fmt', 'yuv420p']


@case('F01')
def _(f, bad):
    f.video(size='1920x1080', vargs=['-c:v', 'libx264', '-preset', 'veryfast', '-profile:v', 'main' if bad else 'high', '-pix_fmt', 'yuv420p'])


@case('F02')
def _(f, bad):
    f.video(rate=25 if bad else 30)


@case('F03')
def _(f, bad):
    v = V_HIGH + (['-fps_mode', 'passthrough'] if bad else [])
    if bad:
        f.ff('-f', 'lavfi', '-i', 'testsrc2=size=320x180:rate=30:duration=1', '-vf', "select='not(eq(n\\,10))'", *v, '-video_track_timescale', '15360', f.p('out/video.mp4'))
    else:
        f.video()


@case('F04')
def _(f, bad):
    br = '2M' if bad else '20M'
    f.video(size='1920x1080', dur=2, src='testsrc2', tags=False, vargs=['-c:v', 'libx264', '-preset', 'ultrafast', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-b:v', br,
                                                                        '-minrate', br, '-maxrate', br, '-bufsize', br, '-x264-params', 'nal-hrd=cbr'])


@case('F05')
def _(f, bad):
    f.video(tags=not bad)


@case('F06')
def _(f, bad):
    x = rng.uniform(-0.3, 0.3, (6 * SR, 2))
    f.video(dur=6, audio=x, aargs=['-ar', '44100'] if bad else None)


@case('F07')
def _(f, bad):
    f.video(size='64x36', dur=5 if bad else 600, src='color')


def gradient_frames(bad, n=4):
    h, w = 1080, 1920
    ramp = np.linspace(20, 44, w)[None, :].repeat(h, 0)
    out = []
    for k in range(n):
        if bad:
            y = np.round(ramp)
        else:
            y = np.round(ramp + rng.uniform(-1.5, 1.5, (h, w)))  # grain / dither breaks the bands
        out.append(np.clip(y, 0, 255).astype(np.uint8))
    return out


@case('F08')
def _(f, bad):
    # rgb grey ramp encoded to limited-range luma: 20–44 full-range ≈ 33–54 in Y codes, a dark gradient
    fr = [np.repeat(g[:, :, None], 3, 2) for g in gradient_frames(bad, 90)]
    f.raw_video(fr, crf='4')


SCRIPT = [{'id': 's1', 'scene': 'a', 'text': 'Two retirees start in 1966.', 'start': 0.5, 'end': 2.5},
          {'id': 's2', 'scene': 'a', 'text': 'Same average, different fate.', 'start': 3.0, 'end': 5.0}]


@case('F09')
def _(f, bad):
    f.json('out/script.json', {'sentences': SCRIPT})
    if bad:
        f.text('out/captions.srt', '1\n00:00:00,500 --> 00:00:02,500\nTwo retirees start in 1966 and this line is far too long\n\n2\n00:00:03,000 --> 00:00:03,400\nSame average, different fate.\n')
    else:
        f.text('out/captions.srt', '1\n00:00:00,500 --> 00:00:02,500\nTwo retirees start in 1966.\n\n2\n00:00:03,000 --> 00:00:05,000\nSame average, different fate.\n')


@case('F10')
def _(f, bad):
    f.video(size='64x36', dur=40, src='color')
    f.text('out/package/description.md', ('0:05' if bad else '0:00') + ' Cold open\n0:12 Two retirees\n0:25 Every start year\n')


# master audio rules -------------------------------------------------------------------------------------
def master_fixture(f, x):
    f.video(size='64x36', dur=len(x) / SR, src='color', audio=x)


@case('A01')
def _(f, bad):
    x = to_lufs(f, programme(30), -20 if bad else -14)
    master_fixture(f, np.clip(x, -0.85, 0.85))


@case('A02')
def _(f, bad):
    x = to_lufs(f, programme(30), -16)
    if bad:
        x[SR * 10:SR * 10 + 400] = 0.99 * np.sin(np.linspace(0, 40 * np.pi, 400))[:, None]
    master_fixture(f, np.clip(x, -0.99, 0.99))


@case('A03')
def _(f, bad):
    x = to_lufs(f, programme(60, block=6.0, levels=(-20, -20) if bad else (-18, -26)), -16)
    master_fixture(f, x)


@case('A04')
def _(f, bad):
    x = to_lufs(f, programme(20), -14)
    if bad:
        x = np.clip(x * 4, -1.0, 1.0)
    master_fixture(f, np.clip(x, -1, 1) if bad else np.clip(x, -0.8, 0.8))


@case('A05')
def _(f, bad):
    x = programme(20, corr=-0.6 if bad else 0.8) * 0.1
    master_fixture(f, x)


@case('A06')
def _(f, bad):
    x = programme(20, corr=0.95) * 0.1
    if bad:
        x[:, 1] = -x[:, 1]
    master_fixture(f, x)


# stems -----------------------------------------------------------------------------------------------
def voice_like(sec, spans, level=-20):
    x = np.zeros(int(sec * SR))
    for a, b in spans:
        i, j = int(a * SR), int(b * SR)
        x[i:j] = noise((j - i + 1) / SR, 200, 4000)[: j - i] * db(level)
    return x


VSPANS = [(2, 5), (7, 10), (12, 15), (17, 20)]


@case('A07')
def _(f, bad):
    v = voice_like(22, VSPANS)
    m = noise(22) * db(-26 if bad else -40)
    f.wav('out/audio/stems/voice.wav', np.stack([v, v], 1))
    f.wav('out/audio/stems/music.wav', np.stack([m, m], 1))


@case('A08')
def _(f, bad):
    v = voice_like(22, VSPANS)
    m = noise(22, 40, 12000) * db(-30)
    act = np.zeros(len(m))
    for a, b in VSPANS:
        act[int(a * SR):int(b * SR)] = 1
    if bad:
        m = m * np.where(act > 0, db(-10), 1.0)  # broadband duck: no band-limited dip
    else:
        sos = signal.butter(4, [1000, 4000], btype='bandpass', fs=SR, output='sos')
        band = signal.sosfiltfilt(sos, m)  # zero-phase, so subtracting it carves the band
        m = m - band * act * (1 - db(-12))  # carve 1–4 kHz by ≈ 12 dB while voice is on
    f.wav('out/audio/stems/voice.wav', np.stack([v, v], 1))
    f.wav('out/audio/stems/music.wav', np.stack([m, m], 1))


@case('A09')
def _(f, bad):
    x = programme(20, levels=(-20,)) * 1.0
    for s in (5, 10, 15):
        x[int(s * SR):int((s + (0.3 if bad else 1.0)) * SR)] = 0
    master_fixture(f, x * 0.5)


def cam_frames(dur, moves, fps=30):
    """moves: (t0, t1, dx) smoothstep lateral moves; returns camera.json frames (fovAxis horizontal, width 1 unit at focus 1)."""
    fr = []
    x = 0.0
    for k in range(int(dur * fps)):
        t = k / fps
        x = 0.0
        for t0, t1, dx in moves:
            u = min(1, max(0, (t - t0) / (t1 - t0)))
            x += dx * u * u * (3 - 2 * u)
        fr.append({'t': t, 'pos': [x, 0, 0], 'target': [x, 0, 0], 'focusDist': 1.0, 'fovDeg': 2 * np.degrees(np.arctan(0.5))})
    return fr


MOVES = [(1, 2, 0.3), (4, 5, 1.2), (7, 8, 0.6), (10, 11, 2.0), (13, 14, 0.9), (16, 17, 1.6)]


@case('A10')
def _(f, bad):
    f.json('out/camera.json', {'fovAxis': 'horizontal', 'frames': cam_frames(19, MOVES)})
    wh = np.zeros(19 * SR)
    for t0, t1, dx in MOVES:
        lvl = -40 + 10 * dx if not bad else -10 - 10 * dx
        seg = noise(t1 - t0 + 0.2, 300, 8000) * db(lvl) * np.hanning(int((t1 - t0 + 0.2) * SR))
        i = int((t0 - 0.1) * SR)
        wh[i:i + len(seg)] += seg
    f.wav('out/audio/stems/whoosh.wav', np.stack([wh, wh], 1))


@case('A11')
def _(f, bad):
    ev, L, R = [], np.zeros(12 * SR), np.zeros(12 * SR)
    for k, x in enumerate([100, 400, 700, 960, 1200, 1500, 1800, 300, 1650, 900]):
        t = 0.5 + k
        pan = (x - 960) / 960 * (-1 if bad else 1)
        b = tone_bursts(12, [t])
        L += b * np.sqrt((1 - pan) / 2)
        R += b * np.sqrt((1 + pan) / 2)
        ev.append({'t': t, 'x': x})
    f.json('out/sfx-events.json', {'events': ev})
    f.wav('out/audio/stems/sfx.wav', np.stack([L, R], 1))


@case('A12')
def _(f, bad):
    beats = [0.5 + 0.5 * k for k in range(36)]
    acc = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0]
    cuts = [a + (0.2 if bad else 0.0) for a in acc]
    m = tone_bursts(19, beats, freq=220, level=-20) + tone_bursts(19, acc, freq=110, level=-8) + noise(19) * db(-60)
    f.wav('out/audio/stems/music.wav', np.stack([m, m], 1))
    f.json('out/tempo-map.json', {'bpm': 120, 'beats': beats, 'accents': acc})
    f.json('out/transitions.json', {'cuts': [{'t': c} for c in cuts]})


@case('A13')
def _(f, bad):
    raw = voice_like(3.2, [(0.1, 3.1)])
    st = 1.2 if bad else 1.05
    fin = voice_like(3.2 * st, [(0.1, 0.1 + 3.0 * st)])
    f.wav('out/voice/s1.raw.wav', raw)
    f.wav('out/voice/s1.final.wav', fin)
    f.json('out/voice/takes.json', {'takes': [{'id': 's1', 'raw': 'out/voice/s1.raw.wav', 'final': 'out/voice/s1.final.wav'}]})


def asr_words(text, start, rate_wpm=155):
    ws, t = [], start
    d = 60 / rate_wpm
    for w in text.split():
        ws.append({'w': w, 'start': round(t, 3), 'end': round(t + d * 0.9, 3)})
        t += d
    return ws


KEY_SENT = [{'id': 's1', 'scene': 'a', 'text': 'Damodaran data starts in 1928.', 'spoken': 'Damodaran data starts in nineteen twenty-eight.', 'start': 1.0, 'end': 3.0},
            {'id': 's2', 'scene': 'a', 'text': 'The real balance falls by $120,000.', 'spoken': 'The real balance falls by one hundred twenty thousand dollars.', 'start': 4.0, 'end': 6.5},
            {'id': 's3', 'scene': 'a', 'text': "The retiree's stocks track the S&P 500.", 'spoken': "The retiree's stocks track the S and P five hundred.", 'start': 7.0, 'end': 9.0},
            {'id': 's4', 'scene': 'a', 'text': "That is the Standard & Poor's 500 index.", 'start': 10.0, 'end': 12.0}]


@case('A14')
def _(f, bad):
    # good: the script's possessive "retiree's" is heard as "retirees", and "S&P" comes back from Whisper as the tokens "S" "&P"
    # (audit §4.1–4.2: both were false misses); bad: a number heard wrong
    f.video(size='64x36', dur=13, src='color')
    f.json('out/script.json', {'sentences': KEY_SENT})
    f.json('out/timeline.json', {'total': 13, 'scenes': [{'id': 'a', 'act': 'act1', 'start': 0, 'dur': 13}]})
    heard2 = 'The real balance falls by $12,000.' if bad else 'The real balance falls by $120,000.'
    f.asr(asr_words('Damodaran data starts in 1928.', 1.0) + asr_words(heard2, 4.0) + asr_words('The retirees stocks track the S &P 500.', 7.0)
          + asr_words("That is the Standard &Poor's 500 index.", 10.0))


@case('A15')
def _(f, bad):
    f.video(size='64x36', dur=30, src='color')
    txt = 'We ran each thirty year window through the same simple withdrawal rule and kept every result on screen'
    sents = []
    words = []
    t = 0.5
    for k in range(6):
        ws = asr_words(txt, t, rate_wpm=190 if bad else 155)
        words += ws
        sents.append({'id': f's{k}', 'scene': 'a', 'text': txt + '.', 'start': ws[0]['start'], 'end': ws[-1]['end']})
        t = ws[-1]['end'] + 0.6
    f.json('out/script.json', {'sentences': sents})
    f.json('out/timeline.json', {'total': 30, 'scenes': [{'id': 'a', 'act': 'act1', 'start': 0, 'dur': 30}]})
    f.asr(words)


# ---- model and data ---------------------------------------------------------------------------------
YEARS = list(range(1928, 2026))


def data_fixture(f):
    r = np.random.default_rng(1)
    rows = [{'year': y, 'stocks': round(float(r.normal(0.1, 0.18)), 6), 'bonds': round(float(r.normal(0.05, 0.07)), 6), 'inflation': round(float(r.normal(0.03, 0.025)), 6)} for y in YEARS]
    with open(f.p('data/normalized/annual.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['year', 'stocks', 'bonds', 'inflation'])
        w.writeheader()
        w.writerows(rows)
    return {x['year']: x for x in rows}


def model_path(seq, init=1_000_000.0):
    """Independent re-implementation for the fixture (not the rule's code)."""
    bal, w, out_w, out_n, out_r, idx = init, 0.04 * init, [], [], [], 1.0
    dep = None
    for k, (s, b, i) in enumerate(seq):
        if k:
            w = w * (1 + seq[k - 1][2])
        if bal < w and dep is None:
            dep = k + 1
        take = w if bal >= w else bal
        bal = (bal - take) * (1 + 0.6 * s + 0.4 * b)
        idx = idx * (1 + i)
        out_w.append(take)
        out_n.append(bal)
        out_r.append(bal / idx)
    return {'withdrawals': out_w, 'endNominal': out_n, 'endReal': out_r, 'depletedYear': dep}



RET_PARAMS = {'annual': 'data/normalized/annual.csv', 'rate': 0.04, 'years': 30, 'weights': {'stocks': 0.6, 'bonds': 0.4}, 'startRange': [1928, 1996],
              'paths': {'1966': {'from': 1966}, 'mirror': {'from': 1966, 'reverse': ['returns', 'inflation']}}, 'sameGeomean': ['1966', 'mirror']}
RET_CONTRACT = {'kind': 'retirement-6040', 'output': 'out/model.json', 'params': RET_PARAMS,
                'claims': [{'where': {'kind': 'geomean', 'character': '1966'}, 'key': 'geomean:1966'}, {'where': {'kind': 'geomean', 'character': 'mirror'}, 'key': 'geomean:mirror'}]}
D_CHARS = {'1966': {'color': '#ffc857', 'shape': 'solid', 'side': 'left', 'words': ['1966']}, 'mirror': {'color': '#5a9ceb', 'shape': 'dashed', 'side': 'right', 'illustrative': True, 'words': ['mirror']}}

@case('S01')
def _(f, bad):
    f.contract(model=RET_CONTRACT)
    d = data_fixture(f)
    tup = lambda y: (d[y]['stocks'], d[y]['bonds'], d[y]['inflation'])
    base = [tup(y) for y in range(1966, 1996)]
    starts = {str(y): model_path([tup(k) for k in range(y, y + 30)]) for y in range(1928, 1997)}
    p66 = model_path(base)
    mir = model_path(base[::-1])
    if bad:
        p66['endNominal'][12] *= 1.01
    f.json('out/model.json', {'initial': 1_000_000, 'rate': 0.04, 'years': 30, 'weights': {'stocks': 0.6, 'bonds': 0.4}, 'tax': 0, 'fees': 0,
                              'paths': {'1966': p66, 'mirror': {**mir, 'reverse': ['returns', 'inflation']}}, 'starts': starts})


@case('F11')
def _(f, bad):
    import r_file
    decl = [x.replace('.*', '.wav') for x in r_file.RELEASE_FILES]
    for x in decl:
        f.text(x, 'x')
    if bad:
        os.remove(f.p('out/cues.json'))
    f.contract(artefacts={'M3': decl})


def refi_case(bad):
    """S01 kind refinance-breakeven (Episode 1, M1b). The characters' part is written from a textbook amortisation in this file (not the rule's
    code); the history part from a synthetic weekly series with two drops, laid out by hand (peaks 9.0 and 8.2, troughs 7.0 and 6.9). bad = one
    history break-even month off by one."""
    import math
    import r_model
    f = F('S01-refi')
    try:
        n, k, r0, rt = 360, 35, 7.62, 7.03
        pay = lambda P, r: P * (r / 1200) / (1 - (1 + r / 1200) ** -n)
        owed = lambda P, r, j: P * ((1 + r / 1200) ** n - (1 + r / 1200) ** j) / ((1 + r / 1200) ** n - 1)
        chars, out_c = {'maya': {'loan': 375000.0, 'cost': 5123.53}}, {}
        for name, c in chars.items():
            L, C = c['loan'], c['cost']
            B = owed(L, r0, k)
            sv = pay(L, r0) - pay(B, rt)
            net = lambda m: sv * m + owed(L, r0, k + m) - owed(B, rt, m) - C
            out_c[name] = {'loan': L, 'cost': C, 'balance': B, 'monthlySavings': sv, 'simple': math.ceil(C / sv), 'withBalance': next(m for m in range(1, n + 1) if net(m) >= 0)}
        # weekly series: monthly means 9.0 (peak, 2000-03) falling to 7.0 (2000-09), up to 8.2 (2001-03), down to 6.9 (2001-09), flat after
        path = [8.5, 8.8, 9.0, 8.7, 8.4, 8.0, 7.6, 7.3, 7.0, 7.4, 7.8, 8.0, 8.1, 8.2, 7.9, 7.5, 7.2, 7.0, 6.9, 7.1, 7.2, 7.3, 7.3, 7.3]
        with open(f.p('data/normalized/weekly.csv'), 'w') as fh:
            fh.write('date,rate\n')
            for i, r in enumerate(path):
                y, mo = 2000 + (i // 12), i % 12 + 1
                for d in (3, 10, 17, 24):
                    fh.write(f'{y}-{mo:02d}-{d:02d},{r}\n')
        with open(f.p('data/normalized/costs.csv'), 'w') as fh:
            fh.write('year,purpose,share\n2018,r,1.5\n2019,r,1.7\n')
        h = {'series': {'file': 'data/normalized/weekly.csv', 'dateColumn': 'date', 'rateColumn': 'rate'}, 'swingPoints': 1.0, 'spreads': [0.5, 1.0], 'loan': 300000,
             'termMonths': 360, 'costShares': {'file': 'data/normalized/costs.csv', 'filter': {'purpose': 'r'}, 'yearColumn': 'year', 'shareColumn': 'share'}}
        params = {'scenario': {'oldRate': r0, 'paymentsMade': k, 'todayRate': rt, 'termMonths': n}, 'characters': chars, 'history': h}
        f.contract(model={'kind': 'refinance-breakeven', 'output': 'out/model.json', 'params': params})
        hist, sh, fixed = r_model.history(common.Ctx(f.root), h)
        assert [(e['peak'], e['trough']) for e in hist] == [('2000-03', '2000-09'), ('2001-02', '2001-07')], hist
        if bad:
            hist[1]['cases'][0]['breakEvenMonths'] += 1
        f.json('out/model.json', {'scenario': {'oldRate': r0, 'paymentsMade': k, 'todayRate': rt}, 'characters': out_c,
                                  'costSharesByYear': {str(y): v for y, v in sh.items()}, 'fixedSharePre2018': fixed, 'history': hist})
        return f.run('S01')
    finally:
        f.close()


def timeline_acts(f, total=100):
    acts = [{'id': 'method', 'start': 50, 'end': 100}, {'id': 'act1', 'start': 0, 'end': 50}]
    f.json('out/timeline.json', {'total': total, 'acts': acts, 'scenes': [{'id': 'a', 'act': 'act1', 'start': 0, 'dur': 50}, {'id': 'm', 'act': 'method', 'start': 50, 'dur': 50}]})


@case('S02')
def _(f, bad):
    # K3: the assumptions come from the episode contract (test D's two, with the K1 regexes)
    import r_content
    f.contract(claims={'assumptions': [{'id': 'no-tax', 'pattern': r_content.NO_TAX.pattern}, {'id': 'no-fee', 'pattern': r_content.NO_FEE.pattern}]})
    timeline_acts(f)
    tt = [{'t': 60, 'scene': 'm', 'items': [{'text': 'No taxes. No fees.'}]}]
    if not bad:
        tt.append({'t': 10, 'scene': 'a', 'items': [{'text': 'Model: no taxes, no fees'}]})
    f.json('out/checks/page.json', {'rules': {}, 'textTrack': tt})


@case('S03')
def _(f, bad):
    f.text('data/raw/histretSP.html', 'damodaran data')
    f.text('data/raw/CPIAUCNS.csv', 'fred data')
    sha = lambda p: common.sha256_file(f.p(p))
    q = {'quote': 'This data may be used freely with attribution to the source page.', 'url': 'https://example.org/terms'}
    f.contract(data={'sources': 'data/sources.json', 'hosts': {'primary': ['stern.nyu.edu'], 'crosscheck': ['fred.stlouisfed.org']}})
    f.json('data/sources.json', {'files': [
        {'path': 'data/raw/histretSP.html', 'role': 'primary', 'url': 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html', 'sha256': sha('data/raw/histretSP.html'), 'downloaded': '2026-09-26', 'terms': q},
        {'path': 'data/raw/CPIAUCNS.csv', 'role': 'crosscheck', 'url': 'https://fred.stlouisfed.org/series/CPIAUCNS', 'sha256': '0' * 64 if bad else sha('data/raw/CPIAUCNS.csv'), 'downloaded': '2026-09-26', 'terms': q}]})


@case('S04')
def _(f, bad):
    d = data_fixture(f)
    with open(f.p('data/normalized/fred_inflation.csv'), 'w') as fh:
        fh.write('year,inflation\n')
        for y in YEARS:
            v = d[y]['inflation'] + (0.012 if bad and y == 1974 else 0.001)
            fh.write(f'{y},{v}\n')
    f.json('data/sources.json', {'files': [], 'mismatches': []})
    f.contract(data={'sources': 'data/sources.json', 'crosscheck': [{'series': 'inflation', 'tolerance': 0.3, 'used': {'from': 1928, 'to': 2025},
                                                                     'primary': {'file': 'data/normalized/annual.csv', 'key': 'year', 'column': 'inflation', 'scale': 100},
                                                                     'crosscheck': {'file': 'data/normalized/fred_inflation.csv', 'key': 'year', 'column': 'inflation', 'scale': 100}}]})


@case('S05')
def _(f, bad):
    d = data_fixture(f)
    seq = [(d[y]['stocks'], d[y]['bonds']) for y in range(1966, 1996)]
    g = (np.prod([1 + 0.6 * s + 0.4 * b for s, b in seq]) ** (1 / 30) - 1) * 100
    f.contract(model=RET_CONTRACT, characters=D_CHARS, claims={'illustrative': ['gm'], 'core': [], 'decisive': []})
    f.json('out/claims.json', {'claims': [{'claimId': 'g66', 'kind': 'geomean', 'character': '1966', 'value': round(g, 4), 'display': f'{g:.2f}%'},
                                          {'claimId': 'gm', 'kind': 'geomean', 'character': 'mirror', 'value': round(g, 4), 'display': f'{g:.2f}%', 'illustrative': not bad}]})


@case('S06')
def _(f, bad):
    timeline_acts(f)
    f.json('out/timeline.json', {'total': 100, 'acts': [{'id': 'act3', 'start': 0, 'end': 100}], 'scenes': [{'id': 'm3', 'act': 'act3', 'start': 0, 'dur': 100}]})
    years = [y for y in range(1928, 1997) if not (bad and y == 1975)]
    cases = [f'd{i}' for i in range(13) if not (bad and i == 4)]
    f.contract(coverage=[{'attribute': 'year', 'act': 'act3', 'range': [1928, 1996]}, {'attribute': 'case', 'act': 'act3', 'values': [f'd{i}' for i in range(13)]}])
    f.json('out/checks/page.json', {'rules': {}, 'yearsTrack': [{'t': 5, 'scene': 'm3', 'years': years}], 'casesTrack': [{'t': 6, 'scene': 'm3', 'cases': cases}]})


BASE_CLAIMS = [{'claimId': 'y66', 'value': 1966, 'display': '1966', 'formula': 'first year', 'source': {'id': 'damodaran'}, 'dataYear': 1966, 'shownIn': ['a']},
               {'claimId': 'bal', 'value': 120000, 'display': '$120,000', 'formula': 'end balance 1966 path', 'source': {'id': 'damodaran'}, 'dataYear': '1966-1995', 'shownIn': ['a'], 'basis': 'real'}]


@case('S07')
def _(f, bad):
    f.json('out/claims.json', {'claims': BASE_CLAIMS})
    f.json('out/checks/page.json', {'rules': {}, 'orphanNumbers': []})
    f.json('out/script.json', {'sentences': [{'id': 's1', 'scene': 'a', 'text': 'In 1966 the real balance ends at $120,000.' if not bad else 'In 1966 the balance ends at $130,000.', 'start': 0, 'end': 2}]})


@case('S08')
def _(f, bad):
    f.json('out/checks/page.json', {'rules': {'S08': {'framesWithout': 3 if bad else 0, 'maxLagFrames': 0, 'examples': []}}})


@case('S09')
def _(f, bad):
    f.json('out/claims.json', {'claims': BASE_CLAIMS})
    f.json('out/checks/page.json', {'rules': {'S09': {'framesMissing': 0, 'examples': []}}})
    f.json('out/script.json', {'sentences': [{'id': 's1', 'scene': 'a', 'text': 'It ends at $120,000.' if bad else 'In real terms, it ends at $120,000.', 'start': 0, 'end': 2}]})


S09_CLAIMS = BASE_CLAIMS + [{'claimId': 'fee', 'value': 5124, 'display': '$5,124', 'formula': 'closing costs', 'source': {'id': 'damodaran'}, 'dataYear': 2024,
                             'shownIn': ['a'], 'basis': 'nominal'}]


def s09_variant(name, lines, frames_missing=0, claims=S09_CLAIMS):
    """One S09 fixture (K3.2): lines = [(scene, text)] in episode order, claims as given, page S09 frames missing as given."""
    f = F('S09-' + name)
    try:
        f.json('out/claims.json', {'claims': claims})
        f.json('out/checks/page.json', {'rules': {'S09': {'framesMissing': frames_missing, 'examples': []}}})
        f.json('out/script.json', {'sentences': [{'id': f's{i}', 'scene': sc, 'text': t, 'start': 2 * i, 'end': 2 * i + 2} for i, (sc, t) in enumerate(lines)]})
        return f.run('S09')
    finally:
        f.close()


NOMINAL_ONLY = [c for c in S09_CLAIMS if c.get('basis') != 'real']


def s09_once_case(bad):
    """K3.2: an episode with $ numbers whose narration never says the basis must fail; the basis said once, anywhere (here after the $ numbers,
    in another scene), covers every $ sentence of the episode."""
    lines = [('a', 'Maya paid $5,124 to refinance.'), ('b', 'Closing costs were $5,124 again.'), ('c', 'Once more: $5,124.')]
    return s09_variant('once', lines + ([] if bad else [('c', 'Every dollar figure here is nominal, the dollars of the day.')]), claims=NOMINAL_ONLY)


def s09_both_case(bad):
    """K3.2: an episode using nominal and real $ claims must say both bases; bad = only 'nominal' is said must fail."""
    lines = [('a', 'In nominal dollars, Maya paid $5,124.'), ('b', 'The balance ends at $120,000.' if bad else 'In real terms, the balance ends at $120,000.')]
    return s09_variant('both', lines)


def s09_screen_case(bad):
    """K3.2 keeps the on-screen part: narration says the basis, but frames showing a $ claim without its basis label must still fail."""
    return s09_variant('screen', [('a', 'In nominal dollars, Maya paid $5,124.')], frames_missing=4 if bad else 0, claims=NOMINAL_ONLY)


def s09_unknown_case(bad):
    """A spoken $ number matching no claim has no known basis: bad = '$9,999' (no claim) must fail even though 'nominal' is said."""
    return s09_variant('unknown', [('a', 'In nominal dollars, Maya paid $5,124.'), ('a', 'Her neighbour paid $9,999.' if bad else 'Her neighbour paid $5,124.')], claims=NOMINAL_ONLY)


@case('S10')
def _(f, bad):
    s = ['We ran every start year from 1928.', 'This is history, not a forecast.', 'The rules here are US only.']
    if bad:
        s.append('You should keep your withdrawals at 4%.')
    f.json('out/script.json', {'sentences': [{'id': f's{i}', 'scene': 'a', 'text': x, 'start': i, 'end': i + 1} for i, x in enumerate(s)]})


S10_BASE = ['We ran every start year from 1928.', 'This is history, not a forecast.', 'The rules here are US only.']


def s10_variant(name, narration=(), screen=()):
    """One S10 fixture (K3.4): the required phrases plus the given narration lines and on-screen texts (page.json textTrack)."""
    f = F('S10-' + name)
    try:
        s = S10_BASE + list(narration)
        f.json('out/script.json', {'sentences': [{'id': f's{i}', 'scene': 'a', 'text': x, 'start': i, 'end': i + 1} for i, x in enumerate(s)]})
        f.json('out/checks/page.json', {'rules': {}, 'textTrack': [{'t': 1.0, 'scene': 'S11', 'items': [{'text': x} for x in screen]}]})
        return f.run('S10')
    finally:
        f.close()


def s10_never_label_case(bad):
    """K3.4: the S11 result label "Never / not before the old loan's last payment" on screen and a lone "Never" must pass; bad = the imperative
    "Never refinance before the old loan's last payment." on screen must fail."""
    screen = ["Never refinance before the old loan's last payment."] if bad else ['Never', "Never / not before the old loan's last payment"]
    return s10_variant('never-label', screen=screen)


def s10_never_narration_case(bad):
    """K3.4: "the fees never come back" in the narration is a statement, not advice (pass); bad = "Never refinance before the fees come back." fails."""
    return s10_variant('never-narration', narration=['Never refinance before the fees come back.' if bad else 'For Maya, the fees never come back.'])


def s10_should_case(bad):
    """K3.4 keeps the modal advice: bad = "You should refinance." on screen fails; good = "Maya could refinance." passes."""
    return s10_variant('should', screen=['You should refinance.' if bad else 'Maya could refinance.'])


def s10_old_advice_case(bad):
    """The pre-K3.4 advice forms still fail: imperative with a directive word ("Don't sell in a crash.", "Always lock the rate."), a bare imperative
    ("Consider the fees."); good = the same facts told as history."""
    lines = ["Don't sell in a crash.", 'Always lock the rate.', 'Consider the fees.'] if bad else ['Few sold in the crash.', 'She always paid on time.', 'The fees came to $5,124.']
    r = s10_variant('old-advice', narration=lines)
    if bad and r['status'] == 'FAIL':
        n = next(m['value'] for m in r['metrics'] if m['name'] == 'advice sentences')
        return dict(r, status='FAIL' if n == 3 else f'CAUGHT-{n}-OF-3')
    return r


@case('S11')
def _(f, bad):
    f.video(size='64x36', dur=40, src='color')
    scenes = [{'id': x, 'act': a, 'start': s, 'dur': 10} for x, a, s in (('a', 'act1', 0), ('b', 'act2', 10), ('c', 'act3', 20), ('d', 'act3', 30))]
    f.json('out/timeline.json', {'total': 40, 'scenes': scenes})
    f.json('out/claims.json', {'claims': [{'claimId': 'g', 'display': '5.6%', 'value': 5.6, 'core': True,
                                           'callbacks': [{'scene': 'a', 'meaning': 'the shared average'}, {'scene': 'b', 'meaning': 'what the average hides'}, {'scene': 'c', 'meaning': 'why the average cannot decide'}]}]})
    seen = ['a', 'b'] if bad else ['a', 'b', 'c']
    f.json('out/checks/page.json', {'rules': {}, 'claimScenes': {'g': seen}})
    f.json('out/script.json', {'sentences': []})
    f.asr([])


@case('S12')
def _(f, bad):
    f.json('out/timeline.json', {'total': 80, 'scenes': [{'id': 'a', 'start': 0, 'dur': 40}, {'id': 'b', 'start': 40, 'dur': 30}, {'id': 'c', 'start': 70, 'dur': 10}]})
    cl = [{'claimId': f'c{i}', 'display': str(10 + i)} for i in range(5)]
    first = {'c0': 1, 'c1': 20, 'c2': 41, 'c3': 60, 'c4': 75} if not bad else {'c0': 1, 'c1': 2, 'c2': 3, 'c3': 60, 'c4': 75}
    f.json('out/claims.json', {'claims': cl})
    f.json('out/script.json', {'sentences': []})
    f.json('out/checks/page.json', {'rules': {}, 'claimFirst': first, 'claimRoles': {}})


@case('S13')
def _(f, bad):
    # K2 (G-009): good = a flowing script whose long and short sentences alternate, one short sentence for emphasis;
    # bad = the same content cut into a staccato string of fragments (which would have raised the old all-sentence CV)
    good = ['Maya borrowed $375,000 in October 2023, the month the 30-year rate peaked, and she has made 35 payments since then.',
            'Rates have come down.', 'This week the average is 7.03%, so the question she faces is whether a refinance pays for itself before she moves.',
            'The bill is the closing costs, and for a loan like hers it came to $5,124.',
            'Most calculators divide that bill by the monthly saving and stop there, which is where the story starts to go wrong.',
            'Here is why.', 'A new loan starts the 30-year schedule again, and early payments are mostly interest.']
    staccato = ['Maya borrowed in 2023.', 'Rates peaked.', 'She paid 35 times.', 'Rates fell.', 'The bill: $5,124.',
                'Most calculators divide that bill by the monthly saving and stop there, which is where the story starts to go wrong.', 'Here is why.']
    s = staccato if bad else good
    f.json('out/script.json', {'sentences': [{'id': f's{i}', 'scene': 'a', 'text': t, 'start': i, 'end': i + 1} for i, t in enumerate(s)]})


@case('S14')
def _(f, bad):
    x = programme(40, levels=(-20,)) * 0.5
    x[int(20 * SR):int(21.3 * SR)] = 0
    master_fixture(f, x)
    f.json('out/timeline.json', {'total': 40, 'acts': [{'id': 'act1', 'start': 0, 'end': 20.5}, {'id': 'act2', 'start': 20.5, 'end': 30}, {'id': 'act3', 'start': 30, 'end': 40}], 'scenes': []})
    f.json('out/adbreaks.json', {'breaks': [20.6, 30.0] if bad else [20.6, 21.0]})


ORDER_ACTS = [('cold-open', 14), ('ident', 3), ('act1', 150), ('act2', 200), ('act3', 180), ('method', 40), ('outro', 25)]


@case('S15')
def _(f, bad):
    acts, t = [], 0.0
    for a, d in ORDER_ACTS:
        d = 20 if bad and a == 'cold-open' else d
        acts.append({'id': a, 'start': t, 'end': t + d})
        t += d
    f.json('out/timeline.json', {'total': t, 'acts': acts, 'scenes': [{'id': a['id'], 'act': a['id'], 'start': a['start'], 'dur': a['end'] - a['start']} for a in acts]})


# ---- rhythm ------------------------------------------------------------------------------------------
@case('R01')
def _(f, bad):
    dur = 90
    cuts = sorted([2 + 3 * k for k in range(8)] + [30 + 1.5 * k for k in range(14)] + [60 + 4 * k for k in range(7)])
    f.json('out/transitions.json', {'cuts': [{'t': c} for c in cuts]})
    lvl = np.concatenate([np.linspace(-40, -20, 30 * SR), np.linspace(-20, -45, 20 * SR), np.linspace(-45, -25, 40 * SR)])
    m = noise(dur) * db(lvl)
    for n, x in (('music', m), ('voice', voice_like(dur, [(5, 25), (40, 70)])), ('sfx', tone_bursts(dur, list(range(30, 50)))), ('whoosh', np.zeros(dur * SR))):
        f.wav(f'out/audio/stems/{n}.wav', np.stack([x, x], 1))
    f.json('out/timeline.json', {'total': dur, 'acts': [{'id': 'act1', 'start': 0, 'end': 30, 'climax': 28}, {'id': 'act2', 'start': 30, 'end': 60, 'climax': 48},
                                                        {'id': 'act3', 'start': 60, 'end': 90, 'climax': 87}], 'scenes': []})
    ctx = common.Ctx(f.root)
    import r_rhythm
    ts = np.arange(0, dur, 1.0)
    ml = r_rhythm._series(ctx, 'music', ts, 1.0)
    cr = np.array([np.sum((np.array(cuts) > t - 5) & (np.array(cuts) <= t + 5)) for t in ts], float)
    act = sum((r_rhythm._series(ctx, n, ts, 1.0) > -45).astype(float) for n in ('voice', 'music', 'sfx', 'whoosh'))
    dens = np.convolve(act, np.ones(5) / 5, mode='same')
    tension = (cr / cr.max() + (ml + 60) / 40) / 2
    tension = np.where((ts > 26) & (ts < 30), tension + 0.6, tension)
    tension = np.where((ts > 46) & (ts < 50), tension + 0.6, tension)
    tension = np.where((ts > 85) & (ts < 88), tension + 0.6, tension)
    samples = [{'t': float(t), 'cutRate': float(c if not bad else -c), 'musicLevel': float(m_), 'audioDensity': float(d_), 'tension': float(te)}
               for t, c, m_, d_, te in zip(ts, cr, ml, dens, tension)]
    f.json('out/tension-map.json', {'samples': samples, 'peaks': [{'t': 28}, {'t': 48}, {'t': 87}], 'valleys': [{'t': 52}, {'t': 33}, {'t': 89}]})
    f.text('out/tension-map.png', 'png')


@case('R02')
def _(f, bad):
    sc = [{'id': 'a', 'start': 0, 'dur': 50, 'layout': 'line/one', 'shot': 'medium'}, {'id': 'b', 'start': 50, 'dur': 30, 'layout': 'bars/two', 'shot': 'wide'},
          {'id': 'c', 'start': 80, 'dur': 40, 'layout': 'bars/three', 'shot': 'wide'}]
    f.json('out/timeline.json', {'total': 120, 'scenes': sc})
    f.json('out/cues.json', {'cues': [] if bad else [{'t': 100}]})


@case('R03')
def _(f, bad):
    # voice stem: speech through the number and its unit word, with a 0.15 s word tail after the ASR end (audit K-4: the old rule
    # took that tail for the end of the pause), then a pause of 1.3 s (good) or 0.4 s (bad), then the next sentence
    txt = 'By 1991 the balance fell to $96,829 dollars.'
    f.json('out/timeline.json', {'total': 10, 'scenes': [{'id': 'a', 'start': 0, 'dur': 10}]})
    f.json('out/claims.json', {'claims': [{'claimId': 'd', 'display': '$96,829', 'decisive': True}]})
    w = asr_words(txt, 1.0)
    e = w[-1]['end']
    gap = 0.4 if bad else 1.3
    w2 = asr_words('It never recovered.', e + gap)
    v = voice_like(10, [(1.0, e + 0.15), (e + gap, w2[-1]['end'])])
    f.wav('out/audio/stems/voice.wav', np.stack([v, v], 1))
    f.video(size='64x36', dur=10, src='color')
    f.json('out/script.json', {'sentences': [{'id': 's1', 'scene': 'a', 'text': txt, 'start': 1, 'end': e}, {'id': 's2', 'scene': 'a', 'text': 'It never recovered.', 'start': e + gap, 'end': w2[-1]['end']}]})
    f.asr(w + w2)


@case('R04')
def _(f, bad):
    beats = [0.5 * k for k in range(40)]
    cuts = [1.0, 2.5, 4.0, 5.5, 7.0, 8.5, 10.0, 11.5, 13.0, 14.5]
    if bad:
        cuts = [c + (0.2 if i % 2 else 0) for i, c in enumerate(cuts)]
    f.json('out/tempo-map.json', {'beats': beats})
    f.json('out/transitions.json', {'cuts': [{'t': c} for c in cuts]})
    f.video(size='64x36', dur=16, src='color')


@case('R05')
def _(f, bad):
    d = [2, 6, 3, 9, 4, 1.5, 8, 7, 6, 5, 3.5, 2.5, 2, 1.6, 10, 3]
    if bad:
        d[4] = 15
    sc, t = [], 0.0
    for i, x in enumerate(d):
        sc.append({'id': f's{i}', 'act': 'act2' if 5 <= i <= 13 else 'act1', 'start': t, 'dur': x})
        t += x
    a2s = sc[5]['start']
    f.json('out/timeline.json', {'total': t, 'acts': [{'id': 'act2', 'start': a2s, 'end': sc[13]['start'] + d[13], 'climax': sc[13]['start'] + d[13] - 0.1}], 'scenes': sc})


def cut_video(f, cuts, dur=6, fps=30, rel='out/video.mp4'):
    frames = []
    k = 0
    for i in range(int(dur * fps)):
        t = i / fps
        k = sum(1 for c in cuts if c <= t + 1e-9)
        img = np.full((180, 320, 3), 30, np.uint8)
        x = 40 + (k * 70) % 240
        img[60:120, x:x + 40] = [240, 180, 60] if k % 2 else [80, 140, 255]
        frames.append(img)
    f.raw_video(frames, rel=rel)


@case('R06')
def _(f, bad):
    real = [1.0, 2.0, 3.0, 4.0, 5.0]
    cut_video(f, real)
    decl = real if not bad else [1.0, 1.5, 2.5, 3.5, 4.5]
    f.json('out/transitions.json', {'cuts': [{'t': c, 'type': 'cut'} for c in decl]})


# ---- visual ------------------------------------------------------------------------------------------
@case('V01')
def _(f, bad):
    f.json('out/timeline.json', {'total': 10, 'scenes': [{'id': 'a', 'start': 0, 'dur': 5}, {'id': 'b', 'start': 5, 'dur': 5}]})
    # 2.5D shot list: no focalMm / angle; bad = a shot without a reason for its move
    shots = [{'id': 'a1', 'scene': 'a', 'size': 'wide', 'move': 'push in on the chart plane', 'moveReason': 'we close in on the shared average'},
             {'id': 'b1', 'scene': 'b', 'size': 'close', 'move': 'pan right', 'moveReason': '' if bad else 'follow the line to the year it runs out'}]
    f.json('preprod/shotlist.json', {'shots': shots})
    f.text('preprod/storyboard.md', 'x')
    f.text('preprod/color-script.json', '{}')


def move_video(f, cam, blur_sub=1, dur=None, size=(640, 360)):
    """Render a stripe pattern that slides with the camera x (1 unit = frame width). blur_sub>1 averages sub-frames (motion blur)."""
    w, h = size
    xs = np.arange(w)
    frames = []
    ts = [c['t'] for c in cam]
    px = np.array([c['pos'][0] for c in cam])
    for i, t in enumerate(ts):
        acc = np.zeros((h, w))
        for s in range(blur_sub):
            tt = t + (s / blur_sub - 0.5) / 30 if blur_sub > 1 else t
            off = np.interp(tt, ts, px) * w
            row = ((((xs + off) // 24) % 2) * 160 + 40).astype(float)
            acc += row[None, :]
        img = (acc / blur_sub).astype(np.uint8)
        img[:, :] = np.maximum(img, 0)
        img[h // 3: h // 3 + 8, :] = 220  # horizontal detail (unaffected by horizontal blur)
        img[2 * h // 3: 2 * h // 3 + 8, :] = 220
        frames.append(img)
    f.raw_video(frames)


def eased_moves(dur, moves, anticipation=0.02, overshoot=0.03, fps=30):
    fr = []
    for k in range(int(dur * fps)):
        t = k / fps
        x = 0.0
        for t0, t1, dx in moves:
            if t < t0 - 0.3:
                continue
            if t < t0:
                x += -anticipation * dx * np.sin(np.pi * (t - t0 + 0.3) / 0.3)
            elif t < t1:
                u = (t - t0) / (t1 - t0)
                e = u * u * (3 - 2 * u)
                x += dx * (e + overshoot * np.sin(np.pi * u) ** 2 * u)
            elif t < t1 + 0.4:
                v = (t - t1) / 0.4
                x += dx * (1 + overshoot * 0.6 * (1 - v) * np.cos(np.pi * v / 2))
            else:
                x += dx
        fr.append({'t': t, 'pos': [x, 0, 0], 'target': [x, 0, 0], 'focusDist': 1.0, 'fovDeg': 2 * np.degrees(np.arctan(0.5))})
    return fr


def linear_moves(dur, moves, fps=30):
    fr = []
    for k in range(int(dur * fps)):
        t = k / fps
        x = sum(dx * min(1, max(0, (t - t0) / (t1 - t0))) for t0, t1, dx in moves)
        fr.append({'t': t, 'pos': [x, 0, 0], 'target': [x, 0, 0], 'focusDist': 1.0, 'fovDeg': 2 * np.degrees(np.arctan(0.5))})
    return fr


VMOVES = [(1, 2.2, 0.4), (3.5, 4.8, -0.5), (6, 7.2, 0.6), (8.5, 9.7, -0.4), (11, 12.3, 0.5), (13.5, 14.7, -0.6)]


def to_25d(cam):
    """camera frames in frame-width units -> 2.5D {t, x, y, zoom} (x in page px of the chart plane, zoom 1)."""
    return [{'t': c['t'], 'x': c['pos'][0] * 1920, 'y': 540.0, 'zoom': 1.0} for c in cam]


@case('V05')
def _(f, bad):
    cam = linear_moves(16, VMOVES) if bad else eased_moves(16, VMOVES)
    f.json('out/camera.json', {'frames': to_25d(cam)})
    move_video(f, cam)


@case('V13')
def _(f, bad):
    # moves of 1.2 s (good) vs one 4 s pan (bad): a long move leaves the layout rules without a settled frame to judge
    moves = [(1, 2.2, 0.4), (4, 5.2, -0.4)] + ([(7, 11, 0.8)] if bad else [(8, 9.2, 0.3)])
    f.json('out/camera.json', {'frames': to_25d(eased_moves(40, moves))})
    f.json('out/timeline.json', {'total': 40, 'scenes': [{'id': 'a', 'start': 0, 'dur': 40}]})


@case('V09')
def _(f, bad):
    c = ('#E5484D', '#3FBF7F') if bad else ('#F2B441', '#4C8DFF')
    f.contract(characters={'1966': {'color': c[0], 'shape': 'solid'}, 'mirror': {'color': c[1], 'shape': 'dashed'}})
    f.json('out/checks/page.json', {'rules': {}, 'characters': {'1966': {'mainColour': c[0]}, 'mirror': {'mainColour': c[1]}}})


def match_video(f, cuts, dissolve_at=None, dur=8, fps=30):
    frames = []
    for i in range(int(dur * fps)):
        t = i / fps
        k = sum(1 for c in cuts if c <= t + 1e-9)
        img = np.full((180, 320), 25, np.uint8)
        # a bright disc that stays in place across cuts (geometric match) on a changing background texture
        img[:, :] = 25 + (k * 11) % 50
        yy, xx = np.mgrid[:180, :320]
        img[(yy - 90) ** 2 + (xx - 160) ** 2 < 30 ** 2] = 235
        img[10:30, 10 + (k * 37) % 260: 40 + (k * 37) % 260] = 120
        frames.append(img.astype(float))
    if dissolve_at is not None:
        f0 = int(dissolve_at * fps)
        A, B = frames[f0 - 8], frames[f0 + 8]
        B = 255 - B
        for j in range(f0 - 8, f0 + 9):
            a = (j - (f0 - 8)) / 16
            frames[j] = (1 - a) * A + a * B
        for j in range(f0 + 9, min(len(frames), f0 + 30)):
            frames[j] = B
    f.raw_video([np.clip(x, 0, 255).astype(np.uint8) for x in frames])


@case('V10')
def _(f, bad):
    cuts = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    match_video(f, cuts, dissolve_at=7.0 if bad else None)
    scenes = [f's{i}' for i in range(7)]
    cl = [{'t': c, 'from': scenes[i], 'to': scenes[i + 1], 'type': 'cut', 'match': 'geometric', 'audio': 'j' if i < 4 else None} for i, c in enumerate(cuts)]
    if bad:
        cl.append({'t': 7.0, 'from': 's6', 'to': 's7', 'type': 'cut'})
    f.json('out/transitions.json', {'cuts': cl})
    sents = [{'id': f'x{i}', 'scene': scenes[i + 1], 'text': 'Next part begins here.', 'start': c - 0.5, 'end': c + 0.6} for i, c in enumerate(cuts)]
    f.json('out/script.json', {'sentences': sents})
    f.asr([w for s in sents for w in asr_words(s['text'], s['start'])])


@case('C11')
def _(f, bad):
    lay = ['line/a', 'bars/b', 'line/a', 'map/c', 'line/a' if bad else 'bars/d']
    f.json('out/timeline.json', {'total': 100, 'scenes': [{'id': f's{i}', 'start': 15 * i, 'dur': 15, 'layout': l} for i, l in enumerate(lay)]})


def page_rule_case(rid, good, bad_, contract=None):
    def fn(f, bad):
        f.json('out/checks/page.json', {'rules': {rid: bad_ if bad else good}})
        if contract:
            f.contract(**contract)
    T[rid] = fn


for rid in ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C15'):
    page_rule_case(rid, {'framesFlagged': 0, 'scenes': [], 'examples': []}, {'framesFlagged': 2, 'scenes': ['a (2)'], 'examples': []})
page_rule_case('C10', {'failing': []}, {'failing': ['a (one l1 in 20%, max 2)']})
page_rule_case('C12', {'violations': []}, {'violations': [{'scene': 'a', 'start': 1, 'durationS': 1.2}]})
page_rule_case('C14', {'violations': 0, 'examples': []}, {'violations': 3, 'examples': []})
page_rule_case('V02', {'samples': 10, 'ok': 10, 'examples': []}, {'samples': 10, 'ok': 5, 'examples': []})
page_rule_case('V03', {'violations': 0, 'examples': []}, {'violations': 1, 'examples': []})
page_rule_case('V08', {'violations': 0, 'worst': {'cr': 8}, 'examples': []}, {'violations': 1, 'worst': {'cr': 2.1}, 'examples': []})
page_rule_case('V12', {'violations': 0, 'textSamples': 40, 'worst': []}, {'violations': 2, 'textSamples': 40, 'worst': [{'t': 1.0, 'tid': 'lab', 'ncc': 0.55}]})
page_rule_case('V11', {'violations': 0, 'byRole': {}, 'transientDuringMoves': 0, 'examples': []}, {'violations': 1, 'byRole': {'badge': 1}, 'transientDuringMoves': 0, 'examples': []})
CH = lambda a, b: {'1966': {'mainColour': '#f2b441', 'colourShare': a, 'mainShape': 'circle', 'shapeShare': 1}, 'mirror': {'mainColour': '#4c8dff', 'colourShare': 1, 'mainShape': b, 'shapeShare': 1}}
page_rule_case('V04', {'characters': CH(1, 'square'), 'pairs': {'1966|mirror': {'samples': 5, 'signs': {'-1': 5}}}, 'timeOrderViolations': []},
               {'characters': CH(0.8, 'circle'), 'pairs': {'1966|mirror': {'samples': 5, 'signs': {'-1': 3, '1': 2}}}, 'timeOrderViolations': []},
               contract={'characters': {'1966': {'color': '#F2B441', 'shape': 'circle', 'side': 'left'}, 'mirror': {'color': '#4C8DFF', 'shape': 'square', 'side': 'right'}}})


@case('C13')
def _(f, bad):
    f.video(size='64x36', dur=6, src='color')
    f.json('out/claims.json', {'claims': [{'claimId': 'y', 'display': '1966'}]})
    f.json('out/script.json', {'sentences': [{'id': 's1', 'scene': 'a', 'text': 'It starts in 1966.', 'start': 1.0, 'end': 3.0}]})
    w = asr_words('It starts in 1966.', 1.0)
    onset = w[3]['start']
    f.asr(w)
    f.json('out/checks/page.json', {'rules': {}, 'claimFinal': {'y|a': onset + (0.4 if bad else 0.1)}})


# ---- T rules --------------------------------------------------------------------------------------------
def mix_master(f, stems, dur):
    """Write the stems (mono arrays -> stereo wav) and a master video whose audio is their sum (the delivered mix)."""
    tot = np.zeros(int(dur * SR))
    for n, x in stems.items():
        x = np.asarray(x)[: len(tot)]
        f.wav(f'out/audio/stems/{n}.wav', np.stack([x, x], 1))
        tot[: len(x)] += x
    f.video(size='64x36', dur=dur, src='color', audio=np.stack([tot, tot], 1).astype(np.float32))


def syllabic_voice(sec, spans, level=-22, syl=0.22, gap=0.07):
    """Speech-like voice: 200–4000 Hz noise in syllables of 220 ms with 70 ms gaps inside each span (the pauses T1 listens in)."""
    x = voice_like(sec, spans, level)
    for a, b in spans:
        t = a + syl
        while t < b:
            x[int(t * SR): int((t + gap) * SR)] = 0
            t += syl + gap
    return x


def flat_bursts(sec, times, dur=0.5, freq=3000, level=-20):
    x = np.zeros(int(sec * SR))
    k = np.arange(int(dur * SR)) / SR
    b = np.sin(2 * np.pi * freq * k) * db(level)
    for t in times:
        i = int(t * SR)
        x[i:i + len(b)] += b[: len(x) - i]
    return x


@case('T1')
def _(f, bad):
    # K2: heard in the voice's pauses. The data sounds (sonify stem, 3 kHz, declared band 2.5–6 kHz) sound for 0.5 s from each event while a
    # syllabic voice runs; good: they raise the band well over music + room in the syllable gaps; bad: the same sounds 30 dB lower (masked)
    dur = 12
    ev = [2.0, 2.05, 2.1, 2.15, 4.0, 6.0, 6.5, 9.0]
    son = flat_bursts(dur, ev, level=-24 if not bad else -54)
    voice = syllabic_voice(dur, [(1.0, 5.5), (6.2, 11.0)], level=-22)
    music = noise(dur, 80, 9000) * db(-34)
    room = noise(dur, 50, 12000) * db(-62)
    mix_master(f, {'voice': voice, 'music': music, 'sfx': np.zeros(dur * SR), 'whoosh': np.zeros(dur * SR), 'room': room, 'sonify': son}, dur)
    f.json('out/sonify-events.json', {'fps': 30, 'bar': [{'id': f'b{i}', 'f0': round(t * 30)} for i, t in enumerate(ev[:4])],
                                      'dot': [{'id': 'd1', 'f': 120}, {'id': 'd2', 'f': 180}, {'id': 'd3', 'f': 195}],
                                      'line': [{'id': 'l1', 'f': 270 + k} for k in range(4)]})
    f.contract(sonification={'stem': 'sonify', 'bandsHz': [[2500, 6000]]})
    f.json('out/script.json', {'sentences': []})
    f.asr([])


@case('L1')
def _(f, bad):
    # the data sounds do not cover the voice. good: a low pulse (300 Hz) far under the voice in 1–4 kHz, and every key word still heard;
    # bad: a 2 kHz tone at the voice's level through the sentence (ratio ≈ 0 dB) and the number lost to the ASR when the data sounds play
    dur = 6
    voice = syllabic_voice(dur, [(1.0, 4.0)], level=-22)
    son = flat_bursts(dur, [1.2, 2.2, 3.2], dur=0.8, freq=2000, level=-24) if bad else flat_bursts(dur, [1.2, 2.2, 3.2], dur=0.3, freq=300, level=-40)
    music = noise(dur, 80, 9000) * db(-44)
    room = noise(dur, 50, 12000) * db(-62)
    z = np.zeros(dur * SR)
    mix_master(f, {'voice': voice, 'music': music, 'sfx': z, 'whoosh': z, 'room': room, 'sonify': son}, dur)
    f.json('out/script.json', {'sentences': [{'id': 's1', 'scene': 'a', 'text': 'The median refinance cost $5,124.', 'start': 1.0, 'end': 4.0}]})
    heard = asr_words('The median refinance cost $5,124.', 1.0)
    f.asr_stems(heard, asr_words('The median refinance cost uh.', 1.0) if bad else heard)


@case('S16')
def _(f, bad):
    # G-008: decisive numbers tied to a character or scenario the contract declares. good: both decisive sentences name one (itself or the
    # sentence before in the same scene); bad: neither does
    f.contract(characters={'median': {'color': '#ffffff', 'shape': 'solid', 'words': ['median borrower', 'median refinance']}},
               scenarios={'hold36': {'words': ['three years', '36 months']}}, claims={'decisive': ['cost_med', 'sp36'], 'core': [], 'illustrative': []})
    f.json('out/claims.json', {'claims': [{'claimId': 'cost_med', 'display': '$5,124', 'decisive': True}, {'claimId': 'sp36', 'display': '0.56'}]})
    # K2 (G-009): the name two sentences back in the same scene still ties the number (good); a name in another scene does not (bad)
    s = [{'id': 'a0', 'scene': 'w', 'text': 'Take the median borrower.' if bad else 'Rates fell this year.', 'start': -1, 'end': 0},
         {'id': 'a1', 'scene': 'x', 'text': 'Take the median borrower.' if not bad else 'Take a loan.', 'start': 0, 'end': 1},
         {'id': 'a1b', 'scene': 'x', 'text': 'It has 35 payments behind it.', 'start': 0.5, 'end': 0.9},
         {'id': 'a2', 'scene': 'x', 'text': 'Closing costs come to $5,124.', 'start': 1, 'end': 2},
         {'id': 'b1', 'scene': 'y', 'text': ('If you stay 36 months, you need a cut of 0.56 points.' if not bad else 'You need a cut of 0.56 points.'), 'start': 3, 'end': 5}]
    f.json('out/script.json', {'sentences': s})


def music_bars(n_bars, bar_s, variant, seed=3):
    """n_bars of synthetic music: each bar = a chord (3 partials of random pitch classes) + a 16-step rhythm. variant 'loop': one bar pattern
    repeated; 'varied': chord and rhythm change every bar."""
    r = np.random.default_rng(seed)
    out = []
    first = None
    for i in range(n_bars):
        if variant == 'loop' and first is not None:
            out.append(first)
            continue
        pcs = r.choice(12, 3, replace=False)
        steps = r.random(16) < 0.45
        t = np.arange(int(bar_s * SR)) / SR
        x = np.zeros_like(t)
        for pc in pcs:
            fr = 220 * 2 ** (pc / 12)
            x += 0.2 * np.sin(2 * np.pi * fr * t)
        env = np.zeros_like(t)
        for k in range(16):
            if steps[k]:
                a = int(k * len(t) / 16)
                env[a:a + int(0.08 * SR)] += np.exp(-np.arange(min(int(0.08 * SR), len(t) - a)) / (0.02 * SR))
        bar = x * (0.3 + env) * 0.2
        out.append(bar)
        first = first if first is not None else bar
    return np.concatenate(out)


@case('T2')
def _(f, bad):
    bpm, bars = 120, 56
    m = music_bars(bars, 2.0, 'loop' if bad else 'varied')
    f.wav('out/audio/stems/music.wav', np.stack([m, m], 1))
    f.json('out/tempo-map.json', {'bpm': bpm, 'beats': [0.5 * k for k in range(bars * 4 + 1)]})


@case('T3')
def _(f, bad):
    # three intentional silences of 1.1 s after speech. Good: music releases like a reverb tail (tau 90 ms), sfx fades in 150 ms, room tone
    # stays as a floor (−60 dBFS). Bad: music and sfx are hard-cut, and the room stem is cut too (digital silence).
    dur = 16
    sil = [(4.0, 5.1), (8.0, 9.1), (12.0, 13.1)]
    tt = np.arange(dur * SR) / SR
    gate_m, gate_s, gate_r = np.ones(len(tt)), np.ones(len(tt)), np.ones(len(tt))
    for a, b in sil:
        s0 = a - 0.25
        if bad:
            sel = (tt >= a - 0.02) & (tt < b)
            gate_m[sel] = 0
            gate_s[sel] = 0
            gate_r[sel] = 0
        else:
            sel = (tt >= s0) & (tt < b)
            gate_m[sel] = np.exp(-(tt[sel] - s0) / 0.09)
            gate_s[sel] = np.clip(1 - (tt[sel] - s0) / 0.15, 0, 1)
            back = (tt >= b) & (tt < b + 0.2)
            gate_m[back] = gate_s[back] = (tt[back] - b) / 0.2
    voice = voice_like(dur, [(1.0, a - 0.3) for a, _ in sil[:1]] + [(sil[i][1] + 0.3, sil[i + 1][0] - 0.3) for i in range(2)] + [(sil[2][1] + 0.3, 15.5)], level=-20)
    music = noise(dur, 80, 9000) * db(-32) * gate_m
    sfx = tone_bursts(dur, list(np.arange(0.5, 16, 0.37)), freq=1500, level=-30) * gate_s
    room = noise(dur, 50, 12000) * db(-60) * gate_r
    mix_master(f, {'voice': voice, 'music': music, 'sfx': sfx, 'whoosh': np.zeros(dur * SR), 'room': room}, dur)


def thumb(f, n, colours, bad_font=False):
    img = np.zeros((720, 1280, 3), np.uint8)
    img[:] = colours[0]
    for x in range(120, 1160, 60):  # bars stand in for heavy lettering on the background
        img[270:450, x:x + 30] = colours[1]
    img[600:680, 100:1180] = colours[2]
    raw = f.p(f'tmp/t{n}.rgb')
    img.tofile(raw)
    f.ff('-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1280x720', '-i', raw, f.p(f'out/package/thumb-{n}.png'))
    f.json(f'out/package/thumb-{n}.json', {'texts': [{'text': 'SAME AVERAGE', 'box': [100, 250, 1080, 220], 'fontPx': 60 if bad_font else 160}]})


@case('P01')
def _(f, bad):
    f.json('design/tokens.json', {'colors': {'bg': '#0E1116', 'ink': '#F2F4F7', 'warn': '#F2B441'}})
    for n in (1, 2, 3):
        cols = [(14, 17, 22), (242, 244, 247), (242, 180, 65)] if not bad else [(14, 17, 22), (200, 30, 200), (242, 180, 65)]
        thumb(f, n, cols)


def reg_case(bad):
    """REG: baseline report where F01 and A01 passed; now A01 fails (bad) or passes (good). A rule whose definition changed is not compared."""
    import run as R_
    fp = {fn.rid: fn.meta['fingerprint'] for fn in common.RULES}
    base = {'lock': 'x', 'results': [{'id': 'F01', 'status': 'PASS', 'fingerprint': fp['F01']}, {'id': 'A01', 'status': 'PASS', 'fingerprint': fp['A01']},
                                     {'id': 'A02', 'status': 'PASS', 'fingerprint': 'changed-definition'}]}
    now = [{'id': 'F01', 'status': 'PASS', 'fingerprint': fp['F01'], 'metrics': []}, {'id': 'A01', 'status': 'FAIL' if bad else 'PASS', 'fingerprint': fp['A01'], 'metrics': []},
           {'id': 'A02', 'status': 'FAIL', 'fingerprint': fp['A02'], 'metrics': []}]
    return R_.regression(now, base)


def asr_cut_case(bad):
    """ASR cut sentence by sentence: the clips cover each sentence ±0.6 s and the kept shares partition the timeline (each word kept once).
    bad = the whole-file layout (one clip, one share) must not pass as sentence-cut."""
    import r_audio
    sents = [{'id': 'a', 'start': 1.0, 'end': 3.0}, {'id': 'b', 'start': 3.2, 'end': 6.0}, {'id': 'c', 'start': 7.5, 'end': 9.0}]
    clips = [(0.0, 10.0, 0.0, 10.0)] if bad else r_audio.sentence_clips(sents, 10.0)
    ok = len(clips) == len(sents)
    ok = ok and all(a <= s['start'] - 0.6 + 1e-9 or a == 0.0 for (a, b, lo, hi), s in zip(clips, sents)) and all(b >= s['end'] + 0.6 - 1e-9 for (a, b, lo, hi), s in zip(clips, sents))
    ok = ok and clips[0][2] == 0.0 and clips[-1][3] == 10.0 and all(abs(clips[i][3] - clips[i + 1][2]) < 1e-9 for i in range(len(clips) - 1))
    return common.Result('A14', 'PASS' if ok else 'FAIL', [common.metric('sentence clips partition the timeline', ok, '==', True)])


def asr_pass_case(bad):
    """Two-pass decode: a first decode that stops half-way (4 of 9 words) is replaced by the full second decode; bad = a chooser that keeps the
    first pass must not pass. A complete first decode is kept without a second decode."""
    import r_audio
    first = [{'w': w} for w in 'returns include dividends and'.split()]
    full = [{'w': w} for w in 'returns include dividends and the portfolio is rebalanced yearly'.split()]
    chooser = (lambda a, b, n: a) if bad else r_audio.choose_pass
    got = chooser(first, lambda: full, 9)
    calls = []
    kept = chooser(full, lambda: calls.append(1) or first, 9)
    ok = got is full and kept is full and not calls
    return common.Result('A14', 'PASS' if ok else 'FAIL', [common.metric('second decode replaces a truncated first decode', ok, '==', True)])


# ---- K3: voice warnings, rights, tiers ------------------------------------------------------------------
@case('A16')
def _(f, bad):
    # good: numbers spelled out with their comma ("five thousand, one hundred"), a dash the written sentence has too
    good = [{'id': 's1', 'scene': 'a', 'text': 'Refinancing costs $5,124.', 'spoken': 'Refinancing costs five thousand, one hundred twenty-four dollars.', 'start': 0, 'end': 2},
            {'id': 's2', 'scene': 'a', 'text': 'The bill - all of it - comes due.', 'spoken': 'The bill - all of it - comes due.', 'start': 2, 'end': 4}]
    badl = [{'id': 's1', 'scene': 'a', 'text': 'So when does that money come back?', 'spoken': 'So... when does that money... come back?', 'start': 0, 'end': 2},
            {'id': 's2', 'scene': 'a', 'text': 'Rates fell fast.', 'spoken': 'Rates fell, [pause] fast.', 'start': 2, 'end': 4}]
    f.json('out/script.json', {'sentences': badl if bad else good})


def a17_voice(bad):
    """6 sentences of 2 s in one scene, 0.4 s apart; bad: every sentence carries two 0.6 s pauses (TTS asked to stop mid-sentence)."""
    spans, sents, t = [], [], 0.5
    for k in range(6):
        if bad:
            parts = [(t, t + 0.6), (t + 1.2, t + 1.8), (t + 2.4, t + 3.0)]
            end = t + 3.0
        else:
            parts = [(t, t + 2.0)]
            end = t + 2.0
        spans += parts
        sents.append({'id': f's{k}', 'scene': 'a', 'text': 'We ran every window through the same rule today.', 'start': round(t, 2), 'end': round(end, 2)})
        t = end + 0.4
    return spans, sents, t + 1


@case('A17')
def _(f, bad):
    spans, sents, dur = a17_voice(bad)
    v = voice_like(dur, spans)
    f.wav('out/audio/stems/voice.wav', np.stack([v, v], 1))
    f.json('out/script.json', {'sentences': sents})


@case('A18')
def _(f, bad):
    takes = []
    for k in range(7):
        other = bad and k >= 4
        x = noise(1.5, 1500, 7000) if other else noise(1.5, 150, 3000)
        f.wav(f'out/voice/t{k}.wav', x * db(-20))
        takes.append({'id': f't{k}', 'raw': f'out/voice/t{k}.wav', 'final': f'out/voice/t{k}.wav', 'model': 'model_b' if other else 'model_a'})
    f.json('out/voice/takes.json', {'takes': takes, 'voice': {'provider': 'P', 'voiceId': 'v1', 'model': 'model_a'}})


F12_TERMS = {'quote': 'You may use the output for commercial purposes, including monetised videos.', 'url': 'https://example.org/terms'}


def f12_page(f, requests=(), fonts=()):
    """out/checks/page.json resources as the K3.1 sampler writes them: the page document and its script (not pictures), a data: image (browser-internal)
    and the given requests / font faces."""
    base = 'file://' + os.path.realpath(f.root) + '/'
    req = [{'url': base + 'page/index.html', 'type': 'document', 'status': 200, 'contentType': 'text/html'},
           {'url': base + 'page/app.js', 'type': 'script', 'status': 200, 'contentType': 'text/javascript'},
           {'url': 'data:image/png;base64,iVBORw0KGgo=', 'type': 'image', 'status': 200, 'contentType': 'image/png'}]
    req += [dict(r, url=base + r['url']) if not r['url'].startswith(('http', 'data')) else r for r in requests]
    f.json('out/checks/page.json', {'resources': {'requests': req, 'entries': [], 'fonts': list(fonts)}})


def f12_sound(f):
    """Voice (third party, cleared) and music (made here) stems with sound; room stem silent (needs no entry)."""
    v = voice_like(4, [(0.5, 3.5)])
    m = noise(4) * db(-30)
    f.wav('out/audio/stems/voice.wav', np.stack([v, v], 1))
    f.wav('out/audio/stems/music.wav', np.stack([m, m], 1))
    f.wav('out/audio/stems/room.wav', np.zeros((4 * SR, 2)))
    f.text('toolkit/music_gen.py', '# generator')
    f.text('toolkit/texture_gen.py', '# generator')
    f12_page(f)
    voice = {'name': 'voice', 'stems': ['voice'], 'origin': 'TTS provider, premade voice', 'licence': 'provider output under the paid plan', 'thirdParty': True,
             'terms': dict(F12_TERMS), 'commercial': True}
    music = {'name': 'music', 'stems': ['music'], 'origin': 'synthesised by this project', 'licence': 'original work', 'thirdParty': False, 'generator': 'toolkit/music_gen.py'}
    return [voice, music]


F12_PHOTO = {'name': 'photo', 'visuals': ['house.jpg'], 'origin': 'stock photo library', 'licence': 'standard licence', 'thirdParty': True,
             'terms': dict(F12_TERMS), 'commercial': True}
F12_FONT = {'name': 'Inter', 'visuals': ['inter'], 'origin': 'rsms/inter via @fontsource/inter', 'licence': 'SIL Open Font License 1.1', 'thirdParty': True,
            'terms': {'quote': 'Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, '
                               'modify, redistribute, and sell modified and unmodified copies of the Font Software', 'url': 'https://openfontlicense.org/open-font-license-official-text/'},
            'commercial': True}
F12_PD = {'name': 'hmda-form', 'visuals': ['hmda-form.pdf'], 'origin': 'CFPB, HMDA filing instructions guide', 'licence': 'public domain', 'thirdParty': True,
          'publicDomain': True, 'source': {'url': 'https://ffiec.cfpb.gov/documentation/'},
          'pdBasis': '17 U.S.C. §105: a work of the United States federal government (CFPB) is not subject to copyright'}
F12_TEXTURE = {'name': 'paper', 'visuals': ['paper-texture'], 'origin': 'procedural noise made by this project', 'licence': 'original work', 'thirdParty': False,
               'generator': 'toolkit/texture_gen.py'}
F12_QUOTE = {'name': 'powell-quote', 'visuals': ['quote-powell'], 'kind': 'quote-card', 'origin': 'card drawn by this project', 'licence': 'original work',
             'thirdParty': False, 'generator': 'toolkit/texture_gen.py',
             'quoteSource': {'who': 'Jerome Powell, FOMC press conference, 2024-09-18', 'url': 'https://www.federalreserve.gov/monetarypolicy/fomcpresconf20240918.htm'}}
F12_VISUALS = [{'name': 'house.jpg', 'kind': 'image'}, {'name': 'inter', 'kind': 'font'}, {'name': 'hmda-form.pdf', 'kind': 'document'},
               {'name': 'paper-texture', 'kind': 'texture'}, {'name': 'quote-powell', 'kind': 'quote-card'}]


@case('F12')
def _(f, bad):
    """bad: the TTS voice is not cleared for commercial use (K3 case); good: sound and every picture kind covered."""
    sound = f12_sound(f)
    if bad:
        sound[0]['commercial'] = False
    f12_page(f, [{'url': 'page/img/house.jpg', 'type': 'image', 'status': 200}, {'url': 'page/docs/hmda-form.pdf', 'type': 'other', 'status': 200},
                 {'url': 'page/fonts/inter-600.woff2', 'type': 'font', 'status': 200}], [{'family': 'Inter', 'status': 'loaded'}])
    f.json('out/visual-assets.json', {'assets': F12_VISUALS})
    f.json('out/rights.json', {'assets': sound + [F12_PHOTO, F12_FONT, F12_PD, F12_TEXTURE, F12_QUOTE]})


def f12_variant(name, visuals, ledger, where='manifest', requests=(), fonts=(), generated=None, files=()):
    """One F12 fixture: sound covered, the given visual list (in out/visual-assets.json or contract.json rights.visual, or none) and ledger entries."""
    f = F('F12-' + name)
    try:
        sound = f12_sound(f)
        for rel in files:
            f.text(rel, '# generator')
        f12_page(f, requests, fonts)
        if where == 'manifest':
            f.json('out/visual-assets.json', {'assets': visuals, **({'generated': generated} if generated else {})})
        elif where == 'contract':
            f.json('contract.json', {'episode': 'x', 'rights': {'visual': visuals}})
        f.json('out/rights.json', {'assets': sound + ledger})
        return f.run('F12')
    finally:
        f.close()


def f12_photo_case(bad):
    """K3.1: a third-party photo in the build; bad = no rights entry for it must fail."""
    return f12_variant('photo', [{'name': 'house.jpg', 'kind': 'image'}], [] if bad else [F12_PHOTO])


def f12_font_case(bad):
    """K3.1: a font; bad = its entry has no terms quote/url must fail (a font is a third-party asset like any other)."""
    font = dict(F12_FONT, terms={}) if bad else F12_FONT
    return f12_variant('font', [{'name': 'inter', 'kind': 'font'}], [font], where='contract')


def f12_pd_case(bad):
    """K3.1: a federal public-domain document with its source and public-domain basis passes without terms; bad = the same without source/basis fails."""
    pd = {k: v for k, v in F12_PD.items() if k not in ('source', 'pdBasis')} if bad else F12_PD
    return f12_variant('pd', [{'name': 'hmda-form.pdf', 'kind': 'document'}], [pd])


def f12_quote_case(bad):
    """K3.1: a reconstructed quote card drawn by the project; bad = without the origin of the quote (quoteSource) fails even though its generator exists."""
    q = {k: v for k, v in F12_QUOTE.items() if k != 'quoteSource'} if bad else F12_QUOTE
    return f12_variant('quote', [{'name': 'quote-powell', 'kind': 'quote-card'}], [q])


def f12_selfmade_case(bad):
    """K3.1: a texture made by the project; bad = its generator path does not exist."""
    t = dict(F12_TEXTURE, generator='toolkit/no_such_gen.py') if bad else F12_TEXTURE
    return f12_variant('selfmade', [{'name': 'paper-texture', 'kind': 'texture'}], [t])


def f12_loaded_case(bad):
    """K3.1 (loaded resources): the page loads a photo; bad = not in the visual list (the ledger is clean otherwise) must fail;
    good = declared by its path glob passes."""
    photo = [{'name': 'house.jpg', 'kind': 'image', 'path': 'page/img/*.jpg'}]
    return f12_variant('loaded', [] if bad else photo, [] if bad else [F12_PHOTO], where='contract' if bad else 'manifest',
                       requests=[{'url': 'page/img/street.jpg', 'type': 'image', 'status': 200}])


def f12_loaded_font_case(bad):
    """K3.1 (loaded fonts): document.fonts has a family loaded (here from a data: URL, so no file request); bad = not declared fails."""
    return f12_variant('loaded-font', [{'name': 'inter', 'kind': 'font', 'family': 'Inter'}], [F12_FONT],
                       fonts=[{'family': 'Inter', 'status': 'loaded'}, {'family': '"Other Sans"' if bad else 'Inter', 'status': 'loaded'},
                              {'family': 'Unused', 'status': 'unloaded'}])


def f12_generated_case(bad):
    """K3.1: a chart texture rendered by the project's code is excluded by a generated rule {glob, generator}; bad = the generator path does not exist,
    so the rule does not hold and the loaded file is undeclared."""
    gen = [{'glob': 'out/render/*.png', 'generator': 'toolkit/missing.py' if bad else 'toolkit/render_png.py'}]
    return f12_variant('generated', [], [], generated=gen, files=['toolkit/render_png.py'],
                       requests=[{'url': 'out/render/chart-bg.png', 'type': 'image', 'status': 200}, {'url': 'page/img/gone.png', 'type': 'image', 'status': 404}])


def f12_manifest_case(bad):
    """K3.1: no visual list declared (neither contract.json rights.visual nor out/visual-assets.json) = MISSING (counted as FAIL here);
    good = an explicitly empty list in the contract (the build declares no pictures) passes."""
    r = f12_variant('manifest', [], [], where=None if bad else 'contract')
    if bad and r['status'] == 'MISSING':
        return dict(r, status='FAIL', note='MISSING: ' + (r.get('note') or ''))
    return r


def tiers_case(bad):
    """Every registered rule (and REG) has a tier among BLOCK/MAJOR/REFERENCE with a reason; bad = a registry with a rule left untiered."""
    import tiers as T_
    ids = [m['id'] for m in runner.registry()] + (['X99'] if bad else [])
    ok = all(i in T_.TIERS and T_.TIERS[i][0] in T_.LABEL and T_.TIERS[i][1] for i in ids)
    ok = ok and T_.tier('F07') == T_.MAJOR and T_.tier('A18') == T_.MAJOR  # owner's decisions at the K3 approval
    extra = [i for i in T_.TIERS if i not in ids]
    return common.Result('TIERS', 'PASS' if ok and not extra else 'FAIL', [common.metric('every rule tiered', ok, '==', True), common.metric('tiers of unknown rules', len(extra), '<=', 0)])


def verdict_case(bad):
    """Only BLOCK fails the episode; MAJOR needs an explanation (≥ 8 words); REFERENCE is measurement only.
    bad = a verdict that lets a failed BLOCK rule through, or fails the episode on REFERENCE rules, must not pass."""
    def v(rows, expl=None):
        res = [{'id': i, 'status': st, 'tier': t} for i, st, t in rows]
        return runner.episode_verdict(res, expl or {})[0]
    B, M, R = 'BLOCK', 'MAJOR', 'REFERENCE'
    got = [v([('A01', 'FAIL', B), ('A15', 'PASS', R)]), v([('A01', 'MISSING', B)]), v([('A01', 'PASS', B), ('A15', 'FAIL', R), ('T1', 'FAIL', R)]),
           v([('A01', 'PASS', B), ('V11', 'FAIL', M)]), v([('A01', 'PASS', B), ('V11', 'FAIL', M)], {'V11': 'the label touches the line for two frames while it slides in'})]
    want = ['TRƯỢT', 'TRƯỢT', 'ĐẠT', 'CHỜ GIẢI THÍCH', 'ĐẠT']
    if bad:
        got[0] = 'ĐẠT'
    ok = got == want
    return common.Result('VERDICT', 'PASS' if ok else 'FAIL', [common.metric('verdicts as the tiers say', ok, '==', True)], details=[got])


def reg_tier_case(bad):
    """REG (K3): a regression of a REFERENCE rule is listed but does not fail REG; a regression of a BLOCK rule does."""
    fp = {fn.rid: fn.meta['fingerprint'] for fn in common.RULES}
    rid = 'A02' if bad else 'A09'
    base = {'lock': 'x', 'results': [{'id': 'F01', 'status': 'PASS', 'fingerprint': fp['F01']}, {'id': rid, 'status': 'PASS', 'fingerprint': fp[rid]}]}
    now = [{'id': 'F01', 'status': 'PASS', 'fingerprint': fp['F01'], 'metrics': []}, {'id': rid, 'status': 'FAIL', 'fingerprint': fp[rid], 'metrics': []}]
    r = runner.regression(now, base)
    listed = any(isinstance(d, dict) and d.get('rule') == rid for d in r['details'])
    return r if listed else common.Result('REG', 'ERROR', note='regression not listed')


def near_case(bad):
    """±5% band: a metric just inside and one just outside its threshold are both named, one 6% away is not; bad = a band of 3% must not pass."""
    band = 0.03 if bad else 0.05
    m = [common.metric('a', 0.955, '>=', 1.0), common.metric('b', 1.045, '>=', 1.0), common.metric('c', 0.94, '>=', 1.0), common.metric('d', 21.0, 'in', [18, 22])]
    want = [True, True, False, True]
    got = [x['near'] for x in m]
    if bad:
        got = [abs(x['value'] - 1.0) <= band if x['name'] != 'd' else True for x in m]
    ok = got == want
    return common.Result('NEAR', 'PASS' if ok else 'FAIL', [common.metric('near flags', ok, '==', True)], details=[got])


def f07_long_case(bad):
    """F07 (K3): CHARTER §1 caps the length at 15:00; bad = 905 s must fail, good = 480 s (the lower edge) must pass."""
    f = F('F07-long')
    try:
        f.video(size='64x36', dur=905 if bad else 480, src='color')
        return f.run('F07')
    finally:
        f.close()


# ---- K3.5: kind float-vs-fixed-replay (Episode 2) ------------------------------------------------------------------------------------------
# Synthetic monthly index of 5 months, 2-payment loan of $1,200: every window can be worked by hand. Written from the spec text in this file (not the
# rule's code): today = last index value 2.0, margin = 6.0 − 2.0 = 4.0; window rates (month 0, month 1):
#   2000-01: 6, 4 + (2 + 12 − 1) = 17     2000-02: 6, 4 + max(0, 2 + 0.5 − 12) = 4 (floored)     2000-03: 6, 4 + (2 + 4 − 0.5) = 9.5     2000-04: 6, 4 + (2 + 2 − 4) = 4
FVF_INDEX = [('2000-01-01', 1.0), ('2000-02-01', 12.0), ('2000-03-01', 0.5), ('2000-04-01', 4.0), ('2000-05-01', 2.0)]
FVF_RATES = {'2000-01': (6, 17), '2000-02': (6, 4), '2000-03': (6, 9.5), '2000-04': (6, 4)}
FVF_PARAMS = {'index': {'file': 'data/normalized/index.csv', 'dateColumn': 'date', 'valueColumn': 'rate'}, 'principal': 1200, 'termMonths': 2,
              'fixedRate': 9.0, 'floatStartRate': 6.0, 'firstStart': '2000-01', 'indexFloor': 0, 'periodBreaks': ['2000-03'], 'spreads': [3.0]}


def fvf_two_months(P, r0, r1):
    """Two-payment loan by hand: month 0 pays the level payment over 2 months at r0; month 1 pays off what is left at r1. Returns (interest, max payment)."""
    i0 = P * r0 / 1200
    p0 = P * (r0 / 1200) / (1 - (1 + r0 / 1200) ** -2)
    B1 = P - (p0 - i0)
    i1 = B1 * r1 / 1200
    return i0 + i1, max(p0, B1 + i1)


def fvf_fixture(f, params=FVF_PARAMS, rates=FVF_RATES):
    with open(f.p('data/normalized/index.csv'), 'w') as fh:
        fh.write('date,rate\n' + ''.join(f'{d},{v}\n' for d, v in FVF_INDEX))
    P = params['principal']
    fpay = P * 0.0075 / (1 - 1.0075 ** -2)
    fint = 2 * fpay - P                          # 9%: payment 606.7584…, interest 9 + 4.5168… = 13.5168…
    assert abs(fint - 13.5168) < 1e-3, fint
    wins = []
    for s, (r0, r1) in rates.items():
        tot, mp = fvf_two_months(P, r0, r1)
        wins.append({'start': s, 'totalInterest': tot, 'difference': tot - fint, 'maxRate': max(r0, r1), 'maxPayment': mp})
    assert [w['difference'] > 0 for w in wins] == [True, False, False, False]   # only 2000-01 (17% in month 1) costs more than 9% fixed
    d = sorted(w['difference'] for w in wins)
    worst, best = max(wins, key=lambda w: w['difference']), min(wins, key=lambda w: w['difference'])
    # spread 3.0: the variable loan starts at 6.0 (as given) → the same share; computed as its own replay below for any other spread
    out = {'principal': P, 'termMonths': 2, 'fixedRate': 9.0, 'floatStartRate': 6.0, 'firstStart': '2000-01-01', 'indexFloor': 0, 'rateCap': None,
           'periodBreaks': ['2000-03-01'], 'nWindows': 4, 'firstStart_': None, 'lastStart': '2000-04-01', 'indexToday': 2.0, 'margin': 4.0,
           'fixedPayment': fpay, 'fixedTotalInterest': fint, 'shareCostlier': 25.0, 'medianDifference': (d[1] + d[2]) / 2,
           'bestDifference': best['difference'], 'bestStart': best['start'], 'worstDifference': worst['difference'], 'worstStart': worst['start'] + '-01',
           'maxRate': 17, 'maxPayment': max(w['maxPayment'] for w in wins), 'windows': wins,
           'periods': [{'from': '2000-01', 'to': '2000-02-01', 'nWindows': 2, 'shareCostlier': 50.0}, {'from': '2000-03-01', 'to': '2000-04', 'nWindows': 2, 'shareCostlier': 0.0}],
           'sensitivity': {'3': 25.0}}
    del out['firstStart_']
    assert best['start'] == '2000-02' and worst['start'] == '2000-01'           # 2000-02 and 2000-04 tie on rates; the earliest is best
    return out


def fvf_s01_case(bad):
    """S01 kind float-vs-fixed-replay: hand-worked windows pass, with dates written both as YYYY-MM and YYYY-MM-01 (normalised, topics-r2 V3);
    bad = one window's difference off by $1.00."""
    f = F('S01-fvf')
    try:
        f.contract(model={'kind': 'float-vs-fixed-replay', 'output': 'out/model.json', 'params': FVF_PARAMS})
        out = fvf_fixture(f)
        if bad:
            out['windows'][2]['difference'] += 1.0
        f.json('out/model.json', out)
        return f.run('S01')
    finally:
        f.close()


def fvf_s01_dates_case(bad):
    """S01 float-vs-fixed-replay, months: bad = worstStart "2000-01-15" (not a month: a day other than 01 is not normalised to its month) fails."""
    f = F('S01-fvf-dates')
    try:
        f.contract(model={'kind': 'float-vs-fixed-replay', 'output': 'out/model.json', 'params': FVF_PARAMS})
        out = fvf_fixture(f)
        out['worstStart'] = '2000-01-15' if bad else '2000-01'
        f.json('out/model.json', out)
        return f.run('S01')
    finally:
        f.close()


def fvf_s05_variant(name, params, claims):
    f = F('S05-fvf-' + name)
    try:
        fvf_fixture(f)
        mc = [{'where': {'claimId': cid}, 'key': key} for cid, key, _ in claims]
        f.contract(model={'kind': 'float-vs-fixed-replay', 'output': 'out/model.json', 'params': params, 'claims': mc}, characters={},
                   claims={'illustrative': [], 'core': [], 'decisive': []})
        f.json('out/claims.json', {'claims': [{'claimId': cid, 'value': v, 'display': str(v)} for cid, _, v in claims]})
        return f.run('S05')
    finally:
        f.close()


def fvf_s05_case(bad):
    """S05 float-vs-fixed-replay claims (hand values): share costlier 25% overall, 50% in 2000-01..02, 0% from 2000-03; worst start 2000-01;
    highest rate 17; sensitivity at a 3.0-point spread = 25%; at 0 points (variable starts at 9%) = 50% (2000-01 and 2000-03 cost more:
    rates 9/20 and 9/12.5 vs 9/7 and 9/7). bad = the 2000-03.. period claimed at 50%."""
    claims = [('fixed', 'fixedTotalInterest', 13.5168), ('all', 'shareCostlier', 25.0), ('p1', 'shareCostlier:2000-01', 50.0),
              ('p2', 'shareCostlier:2000-03-01', 50.0 if bad else 0.0), ('n2', 'nWindows:2000-03', 2), ('wy', 'worstStartYear', 2000),
              ('wm', 'worstStartMonth', 1), ('top', 'maxRate', 17), ('s3', 'shareCostlierAtSpread:3', 25.0), ('s0', 'shareCostlierAtSpread:0', 50.0)]
    return fvf_s05_variant('claims', FVF_PARAMS, claims)


def fvf_invariant_first_case(bad):
    """S05 float-vs-fixed-replay invariant (1): bad = rateCap 5 under the 6% start rate (month 0 is not the offered rate) fails; good = cap 20."""
    return fvf_s05_variant('first', {**FVF_PARAMS, 'rateCap': 5.0 if bad else 20.0}, [('fixed', 'fixedTotalInterest', 13.5168)])


def fvf_invariant_index_case(bad):
    """S05 float-vs-fixed-replay invariant (2): bad = indexFloor −5 lets the 2000-02 path go to 2 + 0.5 − 12 = −9.5 → floored at −5 < 0, fails."""
    return fvf_s05_variant('index', {**FVF_PARAMS, 'indexFloor': -5.0 if bad else 0.0}, [('fixed', 'fixedTotalInterest', 13.5168)])


# ---- K3.6: S05 keys of kind float-vs-fixed-replay (spec: episodes/ep002/checks-notes.md "K3.6") ---------------------------------------
# Same 5-month index and 2-payment loan as K3.5. With the variable loan starting `s` points under the 9% fixed rate (start rate 9 − s, margin 7 − s),
# the window rates (month 0, month 1) are, by hand: 2000-01: 9 − s, 20 − s   2000-02: 9 − s, 7 − s   2000-03: 9 − s, 12.5 − s   2000-04: 9 − s, 7 − s.
#   s = −1: (10, 21) (10, 8) (10, 13.5) (10, 8)   all four cost more than 9% fixed (month 0 at 10% already outweighs month 1 at 8%: 14.0166 > 13.5168)
#   s =  0: (9, 20) (9, 7) (9, 12.5) (9, 7)       2000-01 and 2000-03 cost more        → 50% in 2000-01..02, 50% from 2000-03
#   s =  1: (8, 19) (8, 6) (8, 11.5) (8, 6)       2000-01 and 2000-03 (13.7692 > 13.5168) → 50%, 50%
#   s =  2: (7, 18) (7, 5) (7, 10.5) (7, 5)       2000-01 only (2000-03: 12.2653)        → 50%, 0%
#   s =  3: the K3.5 case, 2000-01 only                                                    → 50%, 0%
# The worst window is 2000-01 at every spread.
FVF_FIX_INT = 2 * (1200 * 0.0075 / (1 - 1.0075 ** -2)) - 1200     # 13.5168…: 9% fixed, two payments


def fvf_hand_rates(s):
    return {'2000-01': (9 - s, 20 - s), '2000-02': (9 - s, 7 - s), '2000-03': (9 - s, 12.5 - s), '2000-04': (9 - s, 7 - s)}


def fvf_hand_share(s, months):
    r = fvf_hand_rates(s)
    return 100.0 * sum(1 for m in months if fvf_two_months(1200, *r[m])[0] > FVF_FIX_INT) / len(months)


P1, P2 = ('2000-01', '2000-02'), ('2000-03', '2000-04')
assert [fvf_hand_share(s, P1) for s in (-1, 0, 1, 2, 3)] == [100, 50, 50, 50, 50]
assert [fvf_hand_share(s, P2) for s in (-1, 0, 1, 2, 3)] == [100, 50, 50, 0, 0]


def fvf_worst(s):
    return fvf_two_months(1200, *fvf_hand_rates(s)['2000-01'])[0] - FVF_FIX_INT


def fvf_spread_period_case(bad):
    """S05 "shareCostlierAtSpread:<points>:<period start>" at spreads −1, 0, 1, 2, 3 (hand table above; negative and zero spreads included);
    bad = spread 2 from 2000-03 claimed at 50% (the spread-1 value)."""
    claims = [(f'g{s}{per}', f'shareCostlierAtSpread:{s}:{per}', fvf_hand_share(s, P1 if per == '2000-01' else P2)) for s in (-1, 0, 1, 2, 3) for per in ('2000-01', '2000-03-01')]
    if bad:
        claims = [(c, k, 50.0 if k == 'shareCostlierAtSpread:2:2000-03-01' else v) for c, k, v in claims]
    return fvf_s05_variant('spread-period', FVF_PARAMS, claims)


def fvf_spread_worst_case(bad):
    """S05 "worstDifferenceAtSpread:<points>" (hand: 2000-01 window at each spread minus the fixed interest) and "worstStartAtSpread:<points>"
    (month claim "2000-01-01"; Year/Month forms 2000 / 1); bad = the worst difference at spread 0 off by $1.00."""
    claims = [(f'w{s}', f'worstDifferenceAtSpread:{s}', fvf_worst(s) + (1.0 if bad and s == 0 else 0)) for s in (-1, 0, 3)]
    claims += [('ws0', 'worstStartAtSpread:0', '2000-01-01'), ('wsy', 'worstStartAtSpreadYear:-1', 2000), ('wsm', 'worstStartAtSpreadMonth:-1', 1)]
    return fvf_s05_variant('spread-worst', FVF_PARAMS, claims)


def fvf_spread_worst_start_case(bad):
    """S05 "worstStartAtSpread:<points>": bad = the worst start at spread 2 claimed "2000-03" (the window that costs more only up to spread 1)."""
    return fvf_s05_variant('spread-worst-start', FVF_PARAMS, [('ws2', 'worstStartAtSpread:2', '2000-03' if bad else '2000-01')])


def fvf_min_spreads_case(bad):
    """S05 "minShareCostlierOverSpreads:<period start>" over params.spreads −1, 0, 1, 2, 3: 50% in 2000-01..02 (100, 50, 50, 50, 50), 0% from 2000-03
    (100, 50, 50, 0, 0); bad = 50% from 2000-03 (the minimum over −1, 0, 1 only, as if the spreads 2 and 3 were left out)."""
    params = {**FVF_PARAMS, 'spreads': [-1, 0, 1, 2, 3]}
    return fvf_s05_variant('min-spreads', params, [('m1', 'minShareCostlierOverSpreads:2000-01', 50.0), ('m2', 'minShareCostlierOverSpreads:2000-03', 50.0 if bad else 0.0)])


def fvf_payments_case(bad):
    """S05 "floatFirstPayment" (level payment of $1,200 over 2 months at 6%: 1200 × 1.005² / 2.005 = 604.5037) and "firstPaymentGap"
    (fixed 606.7584 − 604.5037 = 2.2547); bad = the gap with its sign turned (floatFirstPayment − fixedPayment)."""
    ffp = 1200 * 1.005 ** 2 / 2.005
    fpay = 1200 * 0.0075 / (1 - 1.0075 ** -2)
    assert abs(ffp - 604.5037) < 1e-3 and abs(fpay - ffp - 2.2547) < 1e-3
    return fvf_s05_variant('payments', FVF_PARAMS, [('fp', 'floatFirstPayment', ffp), ('gap', 'firstPaymentGap', (ffp - fpay) if bad else (fpay - ffp))])


def fvf_window_case(bad):
    """S05 "worstWindowMaxRate" (worst window 2000-01: 17%), "shareRateAboveFixed" (2000-01 at 17% and 2000-03 at 9.5% top 9%: 50%, though only 2000-01
    costs more), "worstShareOfFixed" (100 × worst difference / fixed interest); bad = shareRateAboveFixed claimed 25% (the share costlier)."""
    claims = [('peak', 'worstWindowMaxRate', 17.0), ('above', 'shareRateAboveFixed', 25.0 if bad else 50.0), ('ofFixed', 'worstShareOfFixed', 100 * fvf_worst(3) / FVF_FIX_INT)]
    return fvf_s05_variant('window', FVF_PARAMS, claims)


def fvf_rate_above_strict_case(bad):
    """S05 "shareRateAboveFixed" is strict (> fixedRate): floatStartRate 9 = fixedRate, so every window has month 0 at exactly 9%; only 2000-01 (20%) and
    2000-03 (12.5%) go above → 50%. bad = 100% (counting the months at exactly 9%)."""
    return fvf_s05_variant('above-strict', {**FVF_PARAMS, 'floatStartRate': 9.0}, [('above', 'shareRateAboveFixed', 100.0 if bad else 50.0)])


def fvf_month_claims_case(bad):
    """S05 month claims (issue #13, proposal 1): firstStart "2000-01", lastStart "2000-04-01", worstStart "2000-01-01", bestStart "2000-02" compared after
    normalisation; bad = worstStart "2000-01-15" (a day other than 01 is not a month)."""
    claims = [('first', 'firstStart', '2000-01'), ('last', 'lastStart', '2000-04-01'), ('worst', 'worstStart', '2000-01-15' if bad else '2000-01-01'), ('best', 'bestStart', '2000-02')]
    return fvf_s05_variant('months', FVF_PARAMS, claims)


EXTRA = {'REG': reg_case, 'S01/refinance': refi_case, 'A14/asr-cut': asr_cut_case, 'A14/asr-two-pass': asr_pass_case,
         'TIERS': tiers_case, 'VERDICT': verdict_case, 'REG/tier': reg_tier_case, 'NEAR': near_case, 'F07/too-long': f07_long_case,
         'F12/photo': f12_photo_case, 'F12/font': f12_font_case, 'F12/public-domain': f12_pd_case, 'F12/quote-card': f12_quote_case,
         'F12/self-made': f12_selfmade_case, 'F12/no-manifest': f12_manifest_case,
         'F12/loaded': f12_loaded_case, 'F12/loaded-font': f12_loaded_font_case, 'F12/generated': f12_generated_case,
         'S09/said-once': s09_once_case, 'S09/every-basis': s09_both_case, 'S09/screen': s09_screen_case, 'S09/unknown-basis': s09_unknown_case,
         'S10/never-label': s10_never_label_case, 'S10/never-narration': s10_never_narration_case, 'S10/should': s10_should_case, 'S10/old-advice': s10_old_advice_case,
         'S01/float-fixed': fvf_s01_case, 'S01/float-fixed-dates': fvf_s01_dates_case, 'S05/float-fixed': fvf_s05_case,
         'S05/float-fixed-first-rate': fvf_invariant_first_case, 'S05/float-fixed-index': fvf_invariant_index_case,
         'S05/float-fixed-spread-period': fvf_spread_period_case, 'S05/float-fixed-spread-worst': fvf_spread_worst_case,
         'S05/float-fixed-spread-worst-start': fvf_spread_worst_start_case, 'S05/float-fixed-min-spreads': fvf_min_spreads_case,
         'S05/float-fixed-payments': fvf_payments_case, 'S05/float-fixed-window': fvf_window_case, 'S05/float-fixed-rate-above': fvf_rate_above_strict_case,
         'S05/float-fixed-months': fvf_month_claims_case}


def main():
    only = set(sys.argv[sys.argv.index('--only') + 1].split(',')) if '--only' in sys.argv else None
    rows = []
    for name, fn in EXTRA.items():
        if only and name.split('/')[0] not in only:
            continue
        for bad, want in ((True, 'FAIL'), (False, 'PASS')):
            try:
                r = fn(bad)
            except Exception as e:  # noqa: BLE001
                r = {'status': 'FIXTURE-ERROR', 'note': repr(e), 'metrics': []}
            ok = r['status'] == want
            rows.append({'rule': name, 'fixture': 'must fail' if bad else 'must pass', 'want': want, 'got': r['status'], 'ok': ok})
            print(f"{'ok  ' if ok else 'FAIL'} {name} {'bad ' if bad else 'good'} want {want} got {r['status']}" + ('' if ok else f"  {r.get('note') or ''} {r.get('metrics')}"), flush=True)
    missing = [r for r in RULES if r not in T and r not in EXTRA]
    for rid in sorted(T, key=lambda r: runner.key(RULES[r])):
        if only and rid not in only:
            continue
        for bad, want in ((True, 'FAIL'), (False, 'PASS')):
            f = F(rid + ('-bad' if bad else '-good'))
            try:
                T[rid](f, bad)
                r = f.run(rid)
            except Exception as e:  # fixture error
                r = {'status': 'FIXTURE-ERROR', 'note': repr(e), 'metrics': []}
            ok = r['status'] == want
            rows.append({'rule': rid, 'fixture': 'must fail' if bad else 'must pass', 'want': want, 'got': r['status'], 'ok': ok,
                         'metrics': [m for m in r.get('metrics', []) if not m['pass']] if want == 'FAIL' else [m for m in r.get('metrics', []) if not m['pass']]})
            print(f"{'ok  ' if ok else 'FAIL'} {rid} {'bad ' if bad else 'good'} want {want} got {r['status']}" + ('' if ok else f"  {r.get('note') or ''} {[(m['name'], m['value']) for m in r.get('metrics', []) if not m['pass']]}"), flush=True)
            if '--keep' not in sys.argv:
                f.close()
            else:
                print('   kept', f.root)
    bad = [r for r in rows if not r['ok']]
    out = os.environ.get('K_SELFTEST_OUT', tempfile.gettempdir())
    json.dump(rows, open(os.path.join(out, 'selftest-py.json'), 'w'), indent=1, default=str)
    print(f'python self-test: {len(rows) - len(bad)}/{len(rows)} as expected; rules without a python fixture: {sorted(missing)}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
