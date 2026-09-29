"""Voice warnings (K3, REFERENCE tier): the text sent to TTS, the silences in and between sentences, the voice model across the episode."""
import re

import numpy as np

from common import SR, Missing, frame_rms_db, load_audio, metric, rule, verdict, words
from r_audio import VAD_DB, stem_audio

# ---- A16: fake break marks in the text sent to TTS ---------------------------------------------------
# A mark that asks the TTS for a pause the written sentence does not have: ellipses, dashes used as pauses, pause tags (SSML <break>,
# bracket tags such as [pause]), doubled punctuation, and any comma, semicolon, colon or sentence-internal full stop that the spoken text
# (`spoken`) carries beyond the written text (`text`, numbers left out: "$120,000" has a comma the spoken form does not need).
FAKE_MARKS = [('ellipsis', re.compile(r'\.\s*\.\s*\.|…')),
              ('pause dash', re.compile(r'\s[—–-]{1,2}\s|—|–|--')),
              ('pause tag', re.compile(r'<\s*break\b[^>]*>|\[[^\]]*\b(?:pause|beat|silence)\b[^\]]*\]|\([^)]*\b(?:pause|beat)\b[^)]*\)', re.I)),
              ('doubled punctuation', re.compile(r'([,;:!?])\s*\1'))]
_NUM_TOKEN = re.compile(r'\S*\d\S*')
_INNER_STOP = re.compile(r'[.!?](?=\s+\S)')


_NUM_WORD_COMMA = re.compile(r'\b(thousand|million|billion|hundred),', re.I)


def _punct(s):
    s = _NUM_WORD_COMMA.sub(r'\1', _NUM_TOKEN.sub(' ', s))
    s = re.sub(r'\.\s*\.\s*\.|…', ' ', s)
    return len(re.findall(r'[,;:]', s)) + len(_INNER_STOP.findall(s))


def fake_breaks(text, spoken):
    """[(kind, snippet)] of the fake break marks in `spoken` against the written `text`."""
    out = []
    for kind, rx in FAKE_MARKS:
        for m in rx.finditer(spoken):
            if kind == 'pause dash' and rx.search(text or ''):
                continue  # the written sentence has the same dash: a real parenthesis, not a pause request
            out.append((kind, spoken[max(0, m.start() - 12):m.end() + 12]))
    extra = _punct(spoken) - _punct(text or '')
    out += [('extra punctuation', f'{extra} more , ; : or inner stop than the written text')] if extra > 0 else []
    return out


@rule('A16', 'DX-A7 (K3, cảnh báo)', 'every sentence of out/script.json: `spoken` (the text sent to TTS) against `text` (the written sentence). Fake break = a mark that asks '
      'the TTS for a pause the written sentence does not have: ellipsis (... or …), a dash used as a pause (spaced hyphen, en or em dash, --) that the written sentence '
      'does not have, a pause tag (SSML <break>, [pause]/[beat]/[silence], (pause)), doubled punctuation (",,"), and every comma, semicolon, colon or sentence-internal '
      'full stop the spoken text carries beyond the written text (tokens with digits left out)',
      '0 fake break marks (REFERENCE: reported, never fails the episode)')
def a16_fake_breaks(ctx):
    sents = ctx.sentences()
    hits = []
    for s in sents:
        fb = fake_breaks(s.get('text') or '', s.get('spoken') or s.get('text') or '')
        if fb:
            hits.append({'sentence': s.get('id'), 'marks': [f'{k}: {v}' for k, v in fb][:6], 'n': len(fb)})
    return verdict('A16', [metric('sentences', len(sents), '>=', 1), metric('fake break marks', sum(h['n'] for h in hits), '<=', 0),
                           metric('sentences with a fake break', len(hits), '<=', 0)], details=hits[:40])


# ---- A17: density of silences in and between sentences ----------------------------------------------
INNER_MIN = 0.25   # s: a pause inside a sentence
GAP_GLUED = 0.10   # s: two sentences run together


def _voiced(act, t, a, b):
    i = np.nonzero(act & (t >= a) & (t <= b))[0]
    return (t[i[0]], t[i[-1]]) if len(i) else None


def _inner_pauses(act, t, a, b, hop):
    sel = (t >= a) & (t <= b)
    runs, cur = [], 0
    for on in act[sel]:
        if not on:
            cur += 1
        elif cur:
            runs.append(cur * hop)
            cur = 0
    return [r for r in runs if r >= INNER_MIN]


def silence_profile(v, sents, hop=0.01):
    """Voice stem v (mono), sentences sorted by start -> per sentence (voiced span, inner pauses) and the gaps between consecutive sentences
    of a scene, measured on the voice (20 ms RMS, 10 ms hop, active above VAD_DB)."""
    t, db = frame_rms_db(v, win=0.02, hop=hop)
    act = db > VAD_DB
    rows = []
    for s in sents:
        sp = _voiced(act, t, s['start'] - 0.3, s['end'] + 0.3)
        rows.append({'id': s.get('id'), 'scene': s.get('scene'), 'span': sp, 'words': len(words(s.get('spoken') or s.get('text') or '')),
                     'inner': _inner_pauses(act, t, sp[0], sp[1], hop) if sp else []})
    gaps = []
    for a, b in zip(rows, rows[1:]):
        if a['span'] and b['span'] and a['scene'] == b['scene']:
            gaps.append({'after': a['id'], 'gap': round(max(0.0, b['span'][0] - a['span'][1]), 3)})
    return rows, gaps


@rule('A17', 'DX-A7, DX-R6 (K3, cảnh báo)', 'voice stem, 20 ms RMS, 10 ms hop, active above −45 dBFS; each sentence of out/script.json: its voiced span (first to last active '
      'frame within [start − 0.3, end + 0.3]) and its inner pauses (inactive runs ≥ 0.25 s inside the span); gap = silence between the voiced spans of two consecutive '
      'sentences of the same scene; G = the episode\'s median gap. Abnormal sentence: inner pauses > 20% of its voiced span, or ≥ 1 inner pause per 5 words. Abnormal '
      'gap: < 0.10 s (sentences run together) or > max(3·G, G + 1.0 s)',
      'PROVISIONAL: abnormal sentences ≤ 10%; abnormal gaps ≤ 10%; ≥ 1 sentence voiced (REFERENCE: reported, never fails the episode)')
def a17_silence_density(ctx):
    sents = sorted(ctx.sentences(), key=lambda s: s['start'])
    v = stem_audio(ctx, 'voice').mean(1)
    rows, gaps = silence_profile(v, sents)
    voiced = [r for r in rows if r['span']]
    bad_s = []
    for r in voiced:
        span = r['span'][1] - r['span'][0]
        share = sum(r['inner']) / span if span > 0 else 0.0
        if share > 0.20 or (r['inner'] and len(r['inner']) >= max(1, r['words']) / 5):
            bad_s.append({'sentence': r['id'], 'innerPauses': [round(p, 2) for p in r['inner']], 'share': round(float(share), 3), 'words': r['words']})
    g = [x['gap'] for x in gaps]
    med = float(np.median(g)) if g else 0.0
    hi = max(3 * med, med + 1.0)
    bad_g = [x for x in gaps if x['gap'] < GAP_GLUED or x['gap'] > hi]
    return verdict('A17', [metric('voiced sentences', len(voiced), '>=', 1),
                           metric('abnormal sentences share', len(bad_s) / len(voiced) if voiced else 1.0, '<=', 0.10),
                           metric('abnormal gaps share', len(bad_g) / len(gaps) if gaps else 0.0, '<=', 0.10)],
                   details=[{'medianGap': round(med, 3), 'gapHigh': round(hi, 3), 'gaps': len(gaps)}, {'abnormalSentences': bad_s[:30]}, {'abnormalGaps': bad_g[:30]}])


# ---- A18: voice model changed within the episode -----------------------------------------------------
LTAS_BANDS = [100 * 2 ** (k / 3) for k in range(0, 20)]  # 1/3-octave edges 100 Hz … ≈ 8 kHz


def ltas(x, sr=SR):
    """Level-normalised long-term spectrum of the voiced frames: dB per 1/3-octave band 100 Hz–8 kHz, mean removed."""
    x = x.reshape(-1) if x.ndim == 1 or x.shape[1] == 1 else x.mean(1)
    _, db = frame_rms_db(x, win=0.02, hop=0.01)
    n = int(0.02 * sr)
    h = int(0.01 * sr)
    idx = [i for i, d in enumerate(db) if d > VAD_DB]
    if len(idx) < 20:
        return None
    win = np.hanning(n)
    spec = np.zeros(n // 2 + 1)
    for i in idx:
        seg = x[i * h:i * h + n]
        if len(seg) == n:
            spec += np.abs(np.fft.rfft(seg * win)) ** 2
    f = np.fft.rfftfreq(n, 1 / sr)
    b = np.array([10 * np.log10(spec[(f >= lo) & (f < hi)].sum() + 1e-20) for lo, hi in zip(LTAS_BANDS, LTAS_BANDS[1:])])
    return b - b.mean()


def _rms(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))


def group_distance(main, other, seed=0, draws=2000):
    """Distance between the mean spectrum of `other` takes and of `main` takes, and the 99th percentile of the same distance for random
    subsets of `main` of the same size (what chance alone gives). ep001 (K3 calibration): 5 eleven_multilingual_v2 takes vs 78 eleven_v3 takes of
    one voice = 2.44 dB against a chance p99 of 1.69 dB; one take alone does not separate (the v2 takes sit inside the v3 spread)."""
    m = np.stack(main)
    mm = m.mean(0)
    d = _rms(np.mean(other, 0), mm)
    k = len(other)
    if len(m) <= k:
        return d, None
    rng = np.random.default_rng(seed)
    null = [_rms(m[rng.choice(len(m), k, replace=False)].mean(0), mm) for _ in range(draws)]
    return d, float(np.percentile(null, 99))


def _take_voice(tk, voice):
    return tuple(str(tk.get(k) or voice.get(k) or '') for k in ('provider', 'voiceId', 'model'))


@rule('A18', 'DX-A8 (K3, cảnh báo)', 'out/voice/takes.json: the voice of each take = (provider, voiceId, model), per take or else from the file\'s "voice" block (no model '
      'anywhere = MISSING); distinct voices across the takes. Truth check on the take files (final, else raw): long-term spectrum of the voiced frames (20 ms, above '
      '−45 dBFS) in 1/3-octave bands 100 Hz–8 kHz, level-normalised; for each declared voice other than the main one with ≥ 3 measured takes, the distance between its '
      'mean spectrum and the main voice\'s, against the 99th percentile of the same distance for random sets of main-voice takes (reported: one take alone does not '
      'separate two models, so the check reads the declared voice and measures a group)',
      'PROVISIONAL: 1 voice (provider, voiceId, model) for the whole episode (REFERENCE: reported, never fails the episode)')
def a18_voice_model(ctx):
    doc = ctx.json('out/voice/takes.json')
    takes, voice = doc.get('takes') or [], doc.get('voice') or {}
    if not takes:
        raise Missing('out/voice/takes.json: takes[]')
    if any(not (tk.get('model') or voice.get('model')) for tk in takes):
        raise Missing('out/voice/takes.json: takes[].model or voice.model')
    ids = {}
    for tk in takes:
        ids.setdefault(_take_voice(tk, voice), []).append(tk)
    main = max(ids, key=lambda k: len(ids[k]))

    def prof(tks):
        out = []
        for tk in tks:
            p = tk.get('final') if tk.get('final') and ctx.has(tk['final']) else tk.get('raw')
            if p and ctx.has(p):
                s = ltas(load_audio(ctx, p, channels=1))
                if s is not None:
                    out.append(s)
        return out
    measured = []
    if len(ids) > 1:
        pm = prof(ids[main])
        for k, tks in ids.items():
            if k == main:
                continue
            po = prof(tks)
            if len(po) >= 3 and len(pm) > len(po):
                d, p99 = group_distance(pm, po)
                measured.append({'voice': ' / '.join(k), 'takes': len(po), 'distanceDb': round(d, 2), 'chanceP99Db': round(p99, 2), 'measuredDifferent': d > p99})
            else:
                measured.append({'voice': ' / '.join(k), 'takes': len(po), 'note': 'too few measured takes to compare'})
    return verdict('A18', [metric('takes', len(takes), '>=', 1), metric('distinct voices (provider, voiceId, model)', len(ids), '<=', 1)],
                   details=[{'main': ' / '.join(main), 'mainTakes': len(ids[main]),
                             'others': {' / '.join(k): [t.get('id') for t in v][:20] for k, v in ids.items() if k != main}}, {'measured': measured}])
