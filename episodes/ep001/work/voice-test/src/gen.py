"""VIỆC 2 (C4 · G-015): sinh V1/V2/V3 cho thử mù. Eric cjVigY5qzO86Huf0OWal, eleven_v3, không voice_settings, không speed.
V1: từng câu (tái dùng take có sẵn khi chữ gửi TTS trùng; câu mới seed 1). V2: mỗi cảnh một lần gọi. V3: V2 + thẻ cảm xúc.
Mỗi bản sinh 1 lần; sinh lại 1 lần (seed 2) chỉ khi ASR thấy mất từ khoá/số/tên. Khoá API do proxy tiêm; không đọc, không in."""
import base64, json, os, shutil, sys, time
import requests
sys.path.insert(0, '/home/user/crux-lab/checks/py')
from r_audio import key_words, match_keys  # chỉ import
sys.path.insert(0, '/home/user/crux-lab/episodes/ep001/work/v31-voice/src')
from parse import parse, to_tts
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prosody import decode, span

ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep001'; TK = f'{EP}/work/voice-test'; TAKES = f'{TK}/takes'
VOICE, MODEL = 'cjVigY5qzO86Huf0OWal', 'eleven_v3'
URL = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128'
PICK = [1, 2, 3, 4, 5, 6, 7, 8, 49, 50, 51, 52]  # số câu trong v3.1 (S01 cả cảnh, S02 cả cảnh, S10 từ "$1,133" tới "tháng 30")
# V3: thẻ cảm xúc (chỉ cảm xúc/giọng điệu; không thẻ ngắt/nghỉ/tốc độ), đặt trước câu số n
TAGS = {4: '[softly]', 7: '[curious]', 50: '[thoughtful]', 52: '[serious]'}


def rows_all():
    rows = parse()
    for i, (r, t) in enumerate(zip(rows, to_tts([r['text_plain'] for r in rows]))): r['tts_text'] = t; r['n'] = i + 1
    keys = key_words([{'text': r['text_plain']} for r in rows])
    for r, k in zip(rows, keys): r['keys'] = k
    return rows


def synth(text, path, seed, extra=None):
    if os.path.exists(path + '.json'): return json.load(open(path + '.json'))
    body = {'text': text, 'model_id': MODEL, 'seed': seed}
    if extra: body.update(extra)
    for att in range(5):
        r = requests.post(URL, json=body, timeout=300)
        if r.ok: break
        print('HTTP', r.status_code, r.text[:300], file=sys.stderr)
        if r.status_code in (400, 401, 403, 422): return {'error': r.status_code, 'body': r.text[:500], 'request': {k: v for k, v in body.items() if k != 'text'}}
        time.sleep(5 * (att + 1))
    else:
        raise SystemExit('EL failed')
    d = r.json(); open(path + '.mp3', 'wb').write(base64.b64decode(d['audio_base64']))
    meta = {'text': text, 'model': MODEL, 'voice': VOICE, 'seed': seed, 'voice_settings': None, 'speed': None, 'output_format': 'mp3_44100_128',
            'extra': extra, 'characterCost': int(r.headers.get('character-cost', 0) or 0), 'len': len(text), 'requestId': r.headers.get('request-id'),
            'alignment': d.get('alignment'), 'normalized_alignment': d.get('normalized_alignment')}
    json.dump(meta, open(path + '.json', 'w'), indent=1); return meta


_asr = None
def asr(path):
    global _asr
    from faster_whisper import WhisperModel
    if _asr is None: _asr = WhisperModel('small.en', device='cpu', compute_type='int8')
    x = decode(path, 16000); a, b = span(x, 16000)
    segs, _ = _asr.transcribe(x[int(max(0, a - 0.04) * 16000):int((b + 0.12) * 16000)].astype('float32'), word_timestamps=True, language='en', beam_size=5,
                              condition_on_previous_text=False)
    return [{'w': w.word.strip(), 'start': round(float(w.start), 3), 'end': round(float(w.end), 3), 'p': round(float(w.probability), 2)} for g in segs for w in g.words]


def scene_text(rs, tags):
    """Văn xuôi liền: câu nối bằng khoảng trắng; [beat] -> xuống đoạn (dòng trống)."""
    out = ''
    for i, r in enumerate(rs):
        t = (tags.get(r['n']) + ' ' if tags.get(r['n']) else '') + r['tts_text']
        out += t if i == 0 else ('\n\n' if r['pause_kind'] == 'beat' else ' ') + t
    return out


def run(log):
    rows = {r['n']: r for r in rows_all()}
    sel = [rows[n] for n in PICK]
    v31 = {s['n']: s for s in json.load(open(f'{EP}/out/voice-v31/sentences.json'))['sentences']}
    res = {'V1': [], 'V2': [], 'V3': []}; cost = {'V1': 0, 'V2': 0, 'V3': 0}; sent = {'V1': 0, 'V2': 0, 'V3': 0}
    # V1
    for r in sel:
        old = v31[r['n']]
        if old['tts_text'] == r['tts_text']:
            src = f'{ROOT}/{old["take_file"]}'; name = f'V1.n{r["n"]:02d}.reuse-{os.path.basename(src)}'
            shutil.copyfile(src, f'{TAKES}/{name}'); shutil.copyfile(src[:-4] + '.json', f'{TAKES}/{name[:-4]}.json')
            tk = [{'file': name, 'seed': old['seed'], 'source': old['source'], 'from': old['take_file']}]
        else:
            p = f'{TAKES}/V1.n{r["n"]:02d}.seed1'; m = synth(r['tts_text'], p, 1); cost['V1'] += m['characterCost']; sent['V1'] += m['len']
            tk = [{'file': os.path.basename(p) + '.mp3', 'seed': 1, 'source': 'new', 'characterCost': m['characterCost'], 'len': m['len']}]
        w = asr(f'{TAKES}/{tk[0]["file"]}'); tk[0].update(asr=' '.join(x['w'] for x in w), missing=match_keys(r['keys'], w))
        if tk[0]['missing'] and tk[0]['source'] == 'new':
            p = f'{TAKES}/V1.n{r["n"]:02d}.seed2'; m = synth(r['tts_text'], p, 2); cost['V1'] += m['characterCost']; sent['V1'] += m['len']
            w = asr(p + '.mp3'); tk.append({'file': os.path.basename(p) + '.mp3', 'seed': 2, 'source': 'new', 'characterCost': m['characterCost'], 'len': m['len'],
                                           'asr': ' '.join(x['w'] for x in w), 'missing': match_keys(r['keys'], w)})
        best = min(tk, key=lambda t: len(t['missing']))
        res['V1'].append({'n': r['n'], 'scene': r['scene'], 'pause_kind': r['pause_kind'], 'tts_text': r['tts_text'], 'takes': tk, 'use': best['file']})
        print('V1', r['n'], [(t['source'], t['missing']) for t in tk], '|', best['asr'], flush=True)
    # V2, V3
    for v, tags in (('V2', {}), ('V3', TAGS)):
        for sc in ('S01', 'S02', 'S10'):
            rs = [r for r in sel if r['scene'] == sc]; text = scene_text(rs, tags)
            keys = [k for r in rs for k in r['keys']]
            p = f'{TAKES}/{v}.{sc}.seed1'; m = synth(text, p, 1); cost[v] += m['characterCost']; sent[v] += m['len']
            w = asr(p + '.mp3'); tk = [{'file': os.path.basename(p) + '.mp3', 'seed': 1, 'characterCost': m['characterCost'], 'len': m['len'],
                                         'asr': ' '.join(x['w'] for x in w), 'missing': match_keys(keys, w)}]
            if tk[0]['missing']:
                p = f'{TAKES}/{v}.{sc}.seed2'; m = synth(text, p, 2); cost[v] += m['characterCost']; sent[v] += m['len']
                w = asr(p + '.mp3'); tk.append({'file': os.path.basename(p) + '.mp3', 'seed': 2, 'characterCost': m['characterCost'], 'len': m['len'],
                                                 'asr': ' '.join(x['w'] for x in w), 'missing': match_keys(keys, w)})
            best = min(tk, key=lambda t: len(t['missing']))
            res[v].append({'scene': sc, 'n': [r['n'] for r in rs], 'text_sent': text, 'sentences': [r['tts_text'] for r in rs], 'takes': tk, 'use': best['file']})
            print(v, sc, len(text), [t['missing'] for t in tk], '|', best['asr'], flush=True)
    json.dump({'result': res, 'el_characters_charged': cost, 'el_characters_sent': sent, 'tags_v3': {str(k): v for k, v in TAGS.items()}},
              open(f'{TK}/gen-result.json', 'w'), indent=1, ensure_ascii=False)
    print('charged', cost, 'sent', sent)


if __name__ == '__main__':
    run(None)
