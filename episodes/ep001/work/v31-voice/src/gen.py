"""Tập 1 · lời đọc v3.1 (C4). Eric cjVigY5qzO86Huf0OWal, eleven_v3, voice_settings mặc định (không gửi), không speed.
Câu có chữ gửi TTS trùng take C2 -> tái dùng take đó. Câu mới: seed 1; ASR mất từ khoá -> sinh lại 1 lần seed 2.
Khoá API do proxy môi trường tiêm (xi-api-key); không đọc, không in."""
import base64, json, os, shutil, sys, time
import numpy as np, requests
sys.path.insert(0, '/home/user/crux-lab/checks/py')
from r_audio import key_words, match_keys  # chỉ import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse import EP, ROOT, parse, to_tts
import av

VOICE, MODEL = 'cjVigY5qzO86Huf0OWal', 'eleven_v3'
URL = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128'
TK = f'{EP}/work/v31-voice'


def synth(text, path, seed):
    if os.path.exists(path + '.json'): return json.load(open(path + '.json'))
    body = {'text': text, 'model_id': MODEL, 'seed': seed}
    for att in range(5):
        r = requests.post(URL, json=body, timeout=180)
        if r.ok: break
        print('HTTP', r.status_code, r.text[:300], file=sys.stderr)
        if r.status_code in (401, 403, 422): raise SystemExit(1)
        time.sleep(5 * (att + 1))
    else:
        raise SystemExit('EL failed')
    d = r.json(); open(path + '.mp3', 'wb').write(base64.b64decode(d['audio_base64']))
    meta = {'text': text, 'model': MODEL, 'voice': VOICE, 'seed': seed, 'voice_settings': None, 'characterCost': int(r.headers.get('character-cost', 0) or 0),
            'len': len(text), 'requestId': r.headers.get('request-id')}
    json.dump(meta, open(path + '.json', 'w'), indent=1); return meta


def decode(path, sr):
    c = av.open(path); rs = av.AudioResampler(format='flt', layout='mono', rate=sr); out = []
    for f in c.decode(audio=0):
        for g in rs.resample(f): out.append(g.to_ndarray().reshape(-1))
    for g in rs.resample(None): out.append(g.to_ndarray().reshape(-1))
    c.close(); return np.concatenate(out).astype(np.float64)


def span(x, sr, thr=-50.0, win=0.01):
    w = int(win * sr); n = len(x) // w
    db = 20 * np.log10(np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(axis=1) + 1e-12)); on = np.where(db > thr)[0]
    return (on[0] * win, (on[-1] + 1) * win) if len(on) else (0.0, len(x) / sr)


_asr = None
def asr(path):
    global _asr
    from faster_whisper import WhisperModel
    if _asr is None: _asr = WhisperModel('small.en', device='cpu', compute_type='int8')
    x = decode(path, 16000); a, b = span(x, 16000)
    segs, _ = _asr.transcribe(x[int(max(0, a - 0.04) * 16000):int((b + 0.12) * 16000)].astype('float32'), word_timestamps=True, language='en', beam_size=5,
                              condition_on_previous_text=False)
    return [{'w': w.word.strip(), 'start': round(float(w.start), 3), 'end': round(float(w.end), 3), 'p': round(float(w.probability), 2)} for g in segs for w in g.words]


def main():
    rows = parse()
    for r, t in zip(rows, to_tts([r['text_plain'] for r in rows])): r['tts_text'] = t
    c2 = {r['tts_text']: r for r in json.load(open(f'{EP}/review-c2/table-read.json'))['rows']}
    keys = key_words([{'text': r['text_plain']} for r in rows])
    cost = sent = calls = 0
    for i, r in enumerate(rows):
        r['n'] = i + 1; r['keys'] = [k['text'] for k in keys[i]]
        m = c2.get(r['tts_text'])
        takes = []
        if m:
            src = os.path.join(ROOT, m['take_file']); name = f'v{i + 1:03d}.c2-{os.path.basename(src)}'
            shutil.copyfile(src, f'{TK}/{name}'); shutil.copyfile(src[:-4] + '.json', f'{TK}/{name[:-4]}.json')
            r.update(source='reused_c2', c2_n=m['n'], c2_take=m['take_file'], seed=m['seed'])
            takes.append({'file': name, 'seed': m['seed']})
        else:
            r['source'] = 'new'
            meta = synth(r['tts_text'], f'{TK}/v{i + 1:03d}.s1', 1); cost += meta['characterCost']; sent += meta['len']; calls += 1
            takes.append({'file': f'v{i + 1:03d}.s1.mp3', 'seed': 1, 'characterCost': meta['characterCost']})
        w = asr(f'{TK}/{takes[0]["file"]}'); takes[0].update(asr=' '.join(x['w'] for x in w), words=w, missing=match_keys(keys[i], w))
        if takes[0]['missing']:
            p = f'{TK}/v{i + 1:03d}.s2'
            meta = synth(r['tts_text'], p, 2); cost += meta['characterCost']; sent += meta['len']; calls += 1
            w = asr(p + '.mp3'); takes.append({'file': f'v{i + 1:03d}.s2.mp3', 'seed': 2, 'characterCost': meta['characterCost'], 'asr': ' '.join(x['w'] for x in w), 'words': w,
                                                'missing': match_keys(keys[i], w)})
        best = min(takes, key=lambda t: len(t['missing']))  # sinh lại chỉ thay khi bớt mất từ khoá
        r.update(takes=takes, take_file=f'episodes/ep001/work/v31-voice/{best["file"]}', seed=best['seed'], regenerated=len(takes) > 1,
                 missing_keys_first_take=takes[0]['missing'], missing_keys_final=best['missing'], asr_text=best['asr'], asr_words=best['words'])
        print(r['n'], r['scene'], r['source'], [t['missing'] for t in takes], '|', best['asr'], flush=True)
    json.dump({'rows': rows, 'el_characters_charged': cost, 'el_characters_sent': sent, 'el_calls': calls}, open(f'{TK}/gen-result.json', 'w'), indent=1)
    print('EL charged', cost, 'sent', sent, 'calls', calls)


if __name__ == '__main__':
    main()
