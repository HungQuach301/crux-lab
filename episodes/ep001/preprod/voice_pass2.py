"""Stage 4b voice, pass 2: per-sentence fallback takes on eleven_multilingual_v2 with a slower `speed` (no time stretching).

Pass 1 (toolkit/voice/d_el_voice.py, EL_MAX_TAKES=2) showed that Eric on eleven_v3 reads at ~190-230 wpm on the clean take
and ignores voice_settings.speed (tested: speed 0.7 -> 260 wpm; stability 1.0 -> 230 wpm). eleven_multilingual_v2 follows
`speed` (0.75 -> 170 wpm). So every sentence whose best eleven_v3 take is outside 120-190 wpm, misses a key word, or is faster than
172 wpm (act means must land in 150-160) gets up to 3 eleven_multilingual_v2 takes: speed 0.72 first, then scaled by the measured
pace toward 156 wpm (API range 0.7-1.2); stop at the first take with every key word and 144-168 wpm.

    EP_ROOT=episodes/ep001 EL_BUDGET=38000 python3 episodes/ep001/preprod/voice_pass2.py            # pass 2
    EP_ROOT=episodes/ep001 EL_BUDGET=38000 python3 episodes/ep001/preprod/voice_pass2.py --breaks   # pass 3

Pass 3 (--breaks): at speed 0.7 (the API floor) eleven_multilingual_v2 still read short and mid sentences at 170-250 wpm. For
every sentence whose chosen take is still faster than 165 wpm or outside 120-190, up to 2 more eleven_multilingual_v2 takes at
speed 0.7 with ElevenLabs pause tags (<break time="x s" />) at the sentence's phrase boundaries (after a comma/colon, else before a
conjunction or preposition near the middle), x sized to bring the take to ~156 wpm (0.15-0.45 s per pause). The words are
unchanged; only the TTS input carries the pause tags (`ttsText` in el-takes.json).
then re-run toolkit/voice/d_el_voice.py (cached takes, no new calls) to choose takes and write the final clips.
Key: injected by the proxy; never read or printed. Cost: Character-Cost header (el/<take>.json characterCost).
"""
import json
import os
import sys
import tempfile

import numpy as np
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'toolkit', 'voice'))
sys.argv_all = list(sys.argv)
sys.argv = sys.argv[:1]
import d_el_voice as V  # noqa: E402

AIM, FAST = 156.0, 172.0


SPLIT = {'and', 'but', 'so', 'that', 'before', 'with', 'for', 'by', 'when', 'while', 'than', 'from', 'not', 'is', 'was', 'comes', 'needs', 'has', 'had', 'would', 'could', 'says', 'if'}


def with_breaks(text, n_words, span, aim=AIM):
    """Pause tags at phrase boundaries so that the take lasts about n_words * 60 / aim seconds."""
    need = max(0.0, n_words * 60 / aim - span)
    toks = text.split()
    cand = [i for i, t in enumerate(toks[:-1]) if t.endswith((',', ':', ';'))]
    if not cand:
        mid = len(toks) / 2
        opts = [i - 1 for i, t in enumerate(toks) if 0 < i < len(toks) - 1 and t.lower().strip(',.') in SPLIT]
        cand = sorted(opts, key=lambda i: abs(i - mid))[:1] or [max(0, len(toks) // 2 - 1)]
    cand = sorted(cand)[:3]
    per = min(0.4, max(0.15, need / len(cand)))
    for i in reversed(cand):
        toks.insert(i + 1, f'<break time="{per:.2f}s" />')
    return ' '.join(toks), per


def main():
    if '--breaks' in sys.argv_all:
        return breaks()
    from faster_whisper import WhisperModel
    asr = WhisperModel('small.en', device='cpu', compute_type='int8')
    sents = json.load(open(os.path.join(V.VDIR, 'sentences.json')))['sentences']
    keys = dict(zip([s['id'] for s in sents], V.key_words([{'text': s['text']} for s in sents])))
    rp = os.path.join(V.VDIR, 'el-takes.json')
    recs = json.load(open(rp))
    for r in recs.values():  # key words re-matched with the current matcher (initialisms "U .S." = "US")
        r['missing'] = V.match_keys(keys[r['sid']], r['words'])
    ok = lambda r: not r['missing'] and r['wpm'] and 120 <= r['wpm'] <= 190
    todo = []
    for s in sents:
        v3 = [r for r in recs.values() if r['sid'] == s['id'] and r['model'] == V.MAIN and ok(r)]
        if not v3 or min(r['wpm'] for r in v3) > FAST:
            todo.append(s)
    print(len(todo), 'sentences get multilingual_v2 takes', flush=True)
    for s in todo:
        speed = 0.72
        for k in range(3):
            name = f"{s['id']}.p2t{k}.{V.FALLBACK}"
            path = os.path.join(V.EDIR, name + '.mp3')
            meta = V.synth(s['spoken'], V.FALLBACK, k, path, speed)
            sr, x = V.decode(path)
            a, b = V.speech_span(x, sr)
            with tempfile.NamedTemporaryFile(suffix='.wav') as tf:
                wavfile.write(tf.name, sr, (np.clip(x[int(a * sr):int(b * sr)], -1, 1) * 32767).astype(np.int16))
                segs, _ = asr.transcribe(tf.name, word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
                words = [{'w': w.word.strip(), 'start': round(float(w.start), 3), 'end': round(float(w.end), 3)} for g in segs for w in g.words]
            n = len([w for w in s['spoken'].replace('...', ' ').split() if any(c.isalnum() for c in w)])
            span = (words[-1]['end'] - words[0]['start']) if words else 0
            r = {'name': name, 'sid': s['id'], 'model': V.FALLBACK, 'take': 10 + k, 'seed': meta['seed'], 'speed': speed, 'file': os.path.relpath(path, V.ROOT),
                 'speech': [round(float(a), 3), round(float(b), 3)], 'duration': round(len(x) / sr, 3), 'words': words, 'text': ' '.join(w['w'] for w in words),
                 'spokenWords': n, 'asrSpan': round(span, 3), 'wpm': round(60 * n / span, 1) if span > 0 else None,
                 'missing': V.match_keys(keys[s['id']], words), 'characterCost': meta['characterCost'], 'pass': 2}
            recs[name] = r
            print(f"{s['id']} p2t{k} speed {speed:.2f}: {r['wpm']} wpm, missing {r['missing']}", flush=True)
            if not r['missing'] and r['wpm'] and abs(r['wpm'] - AIM) <= 12:
                break
            if r['wpm']:
                speed = float(min(1.2, max(0.7, speed * AIM / r['wpm'])))
                if speed == 0.7 and k >= 1 and r['wpm'] > AIM:
                    break  # already at the slowest speed the API allows
        json.dump(recs, open(rp, 'w'))
    json.dump(recs, open(rp, 'w'))
    spent = sum(r.get('characterCost', 0) for r in recs.values())
    print('all takes character cost', spent)


def take(asr, s, keys, name, model, k, path, speed, tts=None):
    meta = V.synth(tts or s['spoken'], model, k, path, speed)
    sr, x = V.decode(path)
    a, b = V.speech_span(x, sr)
    with tempfile.NamedTemporaryFile(suffix='.wav') as tf:
        wavfile.write(tf.name, sr, (np.clip(x[int(a * sr):int(b * sr)], -1, 1) * 32767).astype(np.int16))
        segs, _ = asr.transcribe(tf.name, word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
        words = [{'w': w.word.strip(), 'start': round(float(w.start), 3), 'end': round(float(w.end), 3)} for g in segs for w in g.words]
    n = len([w for w in s['spoken'].replace('...', ' ').split() if any(c.isalnum() for c in w)])
    span = (words[-1]['end'] - words[0]['start']) if words else 0
    return {'name': name, 'sid': s['id'], 'model': model, 'take': 20 + k, 'seed': meta['seed'], 'speed': speed, 'file': os.path.relpath(path, V.ROOT),
            'speech': [round(float(a), 3), round(float(b), 3)], 'duration': round(len(x) / sr, 3), 'words': words, 'text': ' '.join(w['w'] for w in words),
            'spokenWords': n, 'asrSpan': round(span, 3), 'wpm': round(60 * n / span, 1) if span > 0 else None,
            'missing': V.match_keys(keys[s['id']], words), 'characterCost': meta['characterCost'], 'ttsText': tts}


def breaks():
    from faster_whisper import WhisperModel
    asr = WhisperModel('small.en', device='cpu', compute_type='int8')
    sents = json.load(open(os.path.join(V.VDIR, 'sentences.json')))['sentences']
    keys = dict(zip([s['id'] for s in sents], V.key_words([{'text': s['text']} for s in sents])))
    rp = os.path.join(V.VDIR, 'el-takes.json')
    recs = json.load(open(rp))
    chosen = {r['id']: r['chosen'] for r in json.load(open(os.path.join(V.VDIR, 'choice-report.json')))['sentences']}
    todo = [s for s in sents if chosen[s['id']]['wpm'] and (chosen[s['id']]['wpm'] > 165 or chosen[s['id']]['wpm'] < 120 or chosen[s['id']]['missing'])]
    print(len(todo), 'sentences get pause-tag takes', flush=True)
    for s in todo:
        best = min((r for r in recs.values() if r['sid'] == s['id'] and r['wpm']), key=lambda r: abs(r['wpm'] - AIM))
        span = best['asrSpan']
        for k in range(2):
            tts, per = with_breaks(s['spoken'], best['spokenWords'], span)
            name = f"{s['id']}.p3t{k}.{V.FALLBACK}"
            r = take(asr, s, keys, name, V.FALLBACK, k, os.path.join(V.EDIR, name + '.mp3'), 0.7, tts)
            r['pass'] = 3
            recs[name] = r
            print(f"{s['id']} p3t{k} pause {per:.2f}s: {r['wpm']} wpm, missing {r['missing']} | {tts}", flush=True)
            if not r['missing'] and r['wpm'] and abs(r['wpm'] - AIM) <= 10:
                break
            if not r['wpm']:
                break
            span = r['asrSpan']  # next take: size the pauses from this one
        json.dump(recs, open(rp, 'w'))
    print('all takes character cost', sum(r.get('characterCost', 0) for r in recs.values()))


if __name__ == '__main__':
    main()
