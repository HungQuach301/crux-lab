"""Tập 4 · G1: clip lời cold open (S01 + S02, ≤ 60 s) — Eric (cjVigY5qzO86Huf0OWal), eleven_v3, mặc định, mỗi cảnh một lần gọi, seed 1
(cách của table_read.py Tập 3, không sửa toolkit). Tên take theo hash chữ (chỉ sinh lại khi chữ đổi). Kiểm từ khoá ASR ngay khi sinh.
Khoá API do proxy tiêm; không đọc, không in. Không sinh giọng cho phương án móc không chọn.
    python3 episodes/ep004/story/cold_open.py --dry | (sinh)"""
import base64, hashlib, json, os, re, subprocess, sys, time
import requests
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep004'; OUT = f'{EP}/review-g1'; TAKES = f'{OUT}/takes'
sys.path.insert(0, f'{ROOT}/checks/py')
from r_audio import key_words, match_keys  # noqa: E402
VOICE, MODEL = 'cjVigY5qzO86Huf0OWal', 'eleven_v3'
URL = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/stream/with-timestamps?output_format=mp3_44100_128'
TAG = re.compile(r'^\[([a-z\- ]+)\]\s+')
SCENES = ['S01', 'S02']


def rows():
    out = []
    for ln in open(f'{EP}/story/script.md', encoding='utf-8'):
        m = re.match(r'^(S\d\d)\.(\d+) \| (.+?) \| ', ln)
        if not m or m.group(1) not in SCENES: continue
        t = m.group(3).strip(); tg = TAG.match(t)
        out.append({'scene': m.group(1), 'tag': tg.group(1) if tg else None, 'text': t[tg.end():] if tg else t})
    spoken = json.loads(subprocess.run(['node', '-e', "const n=require('%s/toolkit/voice/normalize.js');const a=JSON.parse(require('fs').readFileSync(0,'utf8'));"
                                        "process.stdout.write(JSON.stringify(a.map(x=>n.toSpoken(x))))" % ROOT],
                                       input=json.dumps([r['text'] for r in out]), capture_output=True, text=True, check=True).stdout)
    for r, s, k in zip(out, spoken, key_words([{'text': r['text']} for r in out])):
        r['tts'] = s[:1].upper() + s[1:]; r['keys'] = k
    return out


def synth(text, path):
    if os.path.exists(path + '.json'): return json.load(open(path + '.json'))
    for att in range(5):
        try:
            r = requests.post(URL, json={'text': text, 'model_id': MODEL, 'seed': 1}, timeout=300, stream=True)
            if r.ok:
                chunks = [json.loads(l) for l in r.iter_lines() if l.strip()]; break
            print('HTTP', r.status_code, r.text[:200], file=sys.stderr)
            if r.status_code in (400, 401, 403, 422): raise SystemExit(f'EL {r.status_code}')
        except requests.exceptions.RequestException as e:
            print('net', e, file=sys.stderr)
        time.sleep(2 ** (att + 1))
    else:
        raise SystemExit('EL failed')
    open(path + '.mp3', 'wb').write(b''.join(base64.b64decode(c['audio_base64']) for c in chunks if c.get('audio_base64')))
    meta = {'text': text, 'model': MODEL, 'voice': VOICE, 'seed': 1, 'characterCost': int(r.headers.get('character-cost', 0) or 0), 'len': len(text)}
    json.dump(meta, open(path + '.json', 'w'), indent=1); return meta


def main():
    rs = rows()
    texts = {sc: ' '.join((f"[{r['tag']}] " if r['tag'] else '') + r['tts'] for r in rs if r['scene'] == sc) for sc in SCENES}
    if '--dry' in sys.argv:
        for sc in SCENES: print(sc, len(texts[sc]), texts[sc])
        print('chars', sum(map(len, texts.values()))); return
    os.makedirs(TAKES, exist_ok=True)
    from faster_whisper import WhisperModel
    wm = WhisperModel('small.en', device='cpu', compute_type='int8'); files = []; rep = {}
    for sc in SCENES:
        p = f"{TAKES}/{sc}-{hashlib.sha256(texts[sc].encode()).hexdigest()[:10]}"
        meta = synth(texts[sc], p)
        segs, _ = wm.transcribe(p + '.mp3', word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
        words = [{'w': w.word.strip(), 'start': w.start, 'end': w.end} for g in segs for w in g.words]
        keys = [k for r in rs if r['scene'] == sc for k in r['keys']]
        miss = match_keys(keys, words) if keys else []
        rep[sc] = {'take': os.path.basename(p), 'chars': meta['characterCost'] or meta['len'], 'missingKeys': miss}
        files.append(p + '.mp3')
    lst = f'{TAKES}/list.txt'; open(lst, 'w').write(''.join(f"file '{f}'\n" for f in files))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c:a', 'aac', '-b:a', '128k', f'{OUT}/cold-open.m4a'], check=True)
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{OUT}/cold-open.m4a'], capture_output=True, text=True).stdout)
    rep['durationS'] = round(dur, 1); json.dump(rep, open(f'{OUT}/cold-open.json', 'w'), indent=1); print(json.dumps(rep))


if __name__ == '__main__':
    main()
