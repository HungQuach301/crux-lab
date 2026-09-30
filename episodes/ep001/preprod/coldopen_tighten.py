"""Stage 4c: tighten the cold open toward the approved ~20 s (amendment E1-A1) without changing its words or time-stretching.

    EP_ROOT=episodes/ep001 EL_BUDGET=<n> python3 episodes/ep001/preprod/coldopen_tighten.py [--new-takes]
    (run after toolkit/voice/d_el_voice.py; then preprod/edit.py)

For every cold-open sentence: choose the FASTEST take that has every key word and stays inside 120-188 wpm (the per-sentence
120-190 range with a 2 wpm margin), instead of the take nearest 156 wpm. With --new-takes, first draw 2 more eleven_v3 takes
(new seeds) for the cold-open sentences whose fastest passing take is under 175 wpm, to give the choice more room.
Final clip = the raw take trimmed to its speech span (+-20 ms instead of +-30 ms); no stretching.
Updates out/voice/final/<sid>.flac, takes.json, choice-report.json, asr-takes.json. Pauses between the sentences: preprod/edit.py.
"""
import json
import os
import subprocess
import sys
import tempfile

import numpy as np
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
new_takes = '--new-takes' in sys.argv
import voice_pass2 as P  # noqa: E402  (loads toolkit/voice/d_el_voice as P.V)

V = P.V
HI = 188.0


def main():
    sents = [s for s in json.load(open(os.path.join(V.VDIR, 'sentences.json')))['sentences'] if s['act'] == 'cold-open']
    allk = json.load(open(os.path.join(V.VDIR, 'sentences.json')))['sentences']
    keys = dict(zip([s['id'] for s in allk], V.key_words([{'text': s['text']} for s in allk])))
    rp = os.path.join(V.VDIR, 'el-takes.json')
    recs = json.load(open(rp))
    ok = lambda r: not r['missing'] and r['wpm'] and 120 <= r['wpm'] <= HI
    if new_takes:
        from faster_whisper import WhisperModel
        asr = WhisperModel('small.en', device='cpu', compute_type='int8')
        for s in sents:
            best = max((r['wpm'] for r in recs.values() if r['sid'] == s['id'] and ok(r)), default=0)
            if best >= 175:
                continue
            for k in range(2):
                name = f"{s['id']}.c4t{k}.{V.MAIN}"
                r = P.take(asr, s, keys, name, V.MAIN, 30 + k, os.path.join(V.EDIR, name + '.mp3'), None)
                r['pass'] = '4c-coldopen'
                recs[name] = r
                print(f"{s['id']} c4t{k}: {r['wpm']} wpm, missing {r['missing']}", flush=True)
        json.dump(recs, open(rp, 'w'))
    tk = json.load(open(os.path.join(V.VDIR, 'takes.json')))
    rep = json.load(open(os.path.join(V.VDIR, 'choice-report.json')))
    at = json.load(open(os.path.join(V.VDIR, 'asr-takes.json')))
    out = {}
    for s in sents:
        c = max((r for r in recs.values() if r['sid'] == s['id'] and ok(r)), key=lambda r: r['wpm'])
        sr, x = V.decode(os.path.join(V.ROOT, c['file']))
        a, b = c['speech']
        seg = x[max(0, int((a - 0.02) * sr)): int((b + 0.02) * sr)]
        fp = os.path.join(V.FDIR, s['id'] + '.flac')
        with tempfile.TemporaryDirectory() as t:
            w = os.path.join(t, 'a.wav')
            wavfile.write(w, sr, (np.clip(seg, -1, 1) * 32767).astype(np.int16))
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', w, fp], check=True)
        for t_ in tk['takes']:
            if t_['id'] == s['id']:
                t_.update({'raw': c['file'], 'final': os.path.relpath(fp, V.ROOT), 'model': c['model'], 'take': c['take']})
        for r_ in rep['sentences']:
            if r_['id'] == s['id']:
                r_['chosen'] = {'take': c['take'], 'model': c['model'], 'wpm': c['wpm'], 'wpmAfter': c['wpm'], 'stretch': 1.0, 'missing': c['missing'], 'heard': c['text'],
                                'coldOpenFastest': True}
        at[f"{s['id']}.t0"] = c
        out[s['id']] = {'take': c['name'], 'wpm': c['wpm'], 'clip': round(len(seg) / sr, 3)}
    n = sum(r['words'] for r in rep['sentences'] if r['act'] == 'cold-open')
    span = sum(next(x for x in recs.values() if x['name'] == at[f"{s['id']}.t0"]['name'])['asrSpan'] for s in sents)
    rep['acts']['cold-open'] = {'rawWpm': round(60 * n / span, 1), 'afterStretchWpm': round(60 * n / span, 1), 'note': 'Stage 4c: fastest passing take per sentence (approved ~20 s cold open)'}
    json.dump(tk, open(os.path.join(V.VDIR, 'takes.json'), 'w'), indent=1)
    json.dump(rep, open(os.path.join(V.VDIR, 'choice-report.json'), 'w'), indent=1)
    json.dump(at, open(os.path.join(V.VDIR, 'asr-takes.json'), 'w'))
    print(json.dumps({'chosen': out, 'speech': round(sum(v['clip'] for v in out.values()), 2), 'coldOpenWpm': rep['acts']['cold-open']['rawWpm'],
                      'allTakesCharacterCost': sum(r.get('characterCost', 0) for r in recs.values())}, indent=1))


if __name__ == '__main__':
    main()
