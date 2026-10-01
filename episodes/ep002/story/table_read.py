"""Tập 2 · C2 table read: Eric (cjVigY5qzO86Huf0OWal), eleven_v3, mặc định (không voice_settings, không speed), MỖI CẢNH MỘT LẦN GỌI, seed 1;
thẻ cảm xúc thưa giữ nguyên ở đầu câu (G-015 · chọn). Sinh lại tối đa 1 lần (seed 2) chỉ khi ASR mất từ khoá. Chạy tiếp được (bỏ cảnh đã có take),
thử lại khi lỗi mạng (2/4/8/16 s). Khoá API do proxy tiêm; không đọc, không in.
    python3 episodes/ep002/story/table_read.py --dry   # chữ gửi + số ký tự
    python3 episodes/ep002/story/table_read.py         # sinh, ASR, ghép review-c2/table-read.m4a
"""
import base64, json, os, re, subprocess, sys, time
import requests
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep002'; OUT = f'{EP}/review-c2'; TAKES = f'{OUT}/takes'
sys.path.insert(0, f'{ROOT}/checks/py')
from r_audio import key_words, match_keys
VOICE, MODEL = 'cjVigY5qzO86Huf0OWal', 'eleven_v3'
URL = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128'
SRC = sys.argv[sys.argv.index('--script') + 1] if '--script' in sys.argv else f'{EP}/story/script.md'
TAG = re.compile(r'^\[([a-z\- ]+)\]\s+')


def rows():
    out = []
    for ln in open(SRC, encoding='utf-8'):
        m = re.match(r'^(S\d\d)\.(\d+) \| (.+?) \| ', ln)
        if not m: continue
        t = m.group(3).strip(); tg = TAG.match(t)
        out.append({'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'tag': tg.group(1) if tg else None, 'text': t[tg.end():] if tg else t})
    MON = 'January|February|March|April|May|June|July|August|September|October|November|December'
    ORD = {1: 'first', 2: 'second', 3: 'third', 21: 'twenty-first', 22: 'twenty-second', 23: 'twenty-third', 31: 'thirty-first'}
    def ordn(d):
        return ORD.get(d) or {4:'fourth',5:'fifth',6:'sixth',7:'seventh',8:'eighth',9:'ninth',10:'tenth',11:'eleventh',12:'twelfth',13:'thirteenth',
               14:'fourteenth',15:'fifteenth',16:'sixteenth',17:'seventeenth',18:'eighteenth',19:'nineteenth',20:'twentieth'}.get(d) or f'{d}th'
    pre = [re.sub(r'\b(' + MON + r') (\d{1,2}),', lambda m: f'{m.group(1)} {ordn(int(m.group(2)))},', r['text']) for r in out]
    spoken = json.loads(subprocess.run(['node', '-e', "const n=require('%s/toolkit/voice/normalize.js');const a=JSON.parse(require('fs').readFileSync(0,'utf8'));"
                                        "process.stdout.write(JSON.stringify(a.map(x=>n.toSpoken(x))))" % ROOT],
                                       input=json.dumps(pre), capture_output=True, text=True, check=True).stdout)
    for r, s, k in zip(out, spoken, key_words([{'text': r['text']} for r in out])):
        s = s.replace('point five-point', 'point five point').replace('-point head start', ' point head start')
        r['tts'] = s[:1].upper() + s[1:]; r['keys'] = k
    return out


def scene_text(rs):
    return ' '.join((f"[{r['tag']}] " if r['tag'] else '') + r['tts'] for r in rs)


def synth(text, path, seed):
    if os.path.exists(path + '.json'): return json.load(open(path + '.json'))
    for att in range(5):
        try:
            r = requests.post(URL, json={'text': text, 'model_id': MODEL, 'seed': seed}, timeout=300)
            if r.ok: break
            print('HTTP', r.status_code, r.text[:200], file=sys.stderr)
            if r.status_code in (400, 401, 403, 422): raise SystemExit(f'EL {r.status_code}')
        except requests.exceptions.RequestException as e:
            print('net', e, file=sys.stderr)
        time.sleep(2 ** (att + 1))
    else:
        raise SystemExit('EL failed after retries')
    d = r.json(); open(path + '.mp3', 'wb').write(base64.b64decode(d['audio_base64']))
    meta = {'text': text, 'model': MODEL, 'voice': VOICE, 'seed': seed, 'voice_settings': None, 'speed': None,
            'characterCost': int(r.headers.get('character-cost', 0) or 0), 'len': len(text), 'requestId': r.headers.get('request-id')}
    json.dump(meta, open(path + '.json', 'w'), indent=1); return meta


_m = None
def asr(path):
    global _m
    from faster_whisper import WhisperModel
    if _m is None: _m = WhisperModel('small.en', device='cpu', compute_type='int8')
    segs, _ = _m.transcribe(path, word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
    return [{'w': w.word.strip(), 'start': round(w.start, 3), 'end': round(w.end, 3)} for g in segs for w in g.words]


def main():
    rs = rows(); scenes = sorted({r['scene'] for r in rs})
    texts = {sc: scene_text([r for r in rs if r['scene'] == sc]) for sc in scenes}
    if '--dry' in sys.argv:
        for sc in scenes: print(sc, len(texts[sc]), texts[sc][:140])
        print('chars', sum(map(len, texts.values())), 'tags', sum(1 for r in rs if r['tag'])); return
    os.makedirs(TAKES, exist_ok=True)
    resf = f'{OUT}/table-read.json'; res = json.load(open(resf)) if os.path.exists(resf) else {'scenes': {}}
    for sc in scenes:
        e = res['scenes'].get(sc)
        if e and e['text'] == texts[sc] and e['takes'] and (not e['takes'][-1]['missing'] or len(e['takes']) == 2): continue
        e = {'text': texts[sc], 'takes': []}
        keys = [k for r in rs if r['scene'] == sc for k in r['keys']]
        for seed in (1, 2):
            p = f'{TAKES}/{sc}.seed{seed}'; m = synth(texts[sc], p, seed); w = asr(p + '.mp3')
            e['takes'].append({'file': os.path.basename(p) + '.mp3', 'seed': seed, 'characterCost': m['characterCost'], 'len': m['len'],
                               'missing': match_keys(keys, w), 'asr': ' '.join(x['w'] for x in w)})
            if not e['takes'][-1]['missing']: break
        e['use'] = min(e['takes'], key=lambda t: len(t['missing']))['file']
        res['scenes'][sc] = e; json.dump(res, open(resf, 'w'), indent=1)   # commit từng cảnh vào file kết quả
        print(sc, [(t['seed'], t['characterCost'], len(t['missing'])) for t in e['takes']], flush=True)
    res['chars'] = sum(t['characterCost'] or t['len'] for e in res['scenes'].values() for t in e['takes'])
    json.dump(res, open(resf, 'w'), indent=1)
    lst = f'{OUT}/concat.txt'; gap = f'{OUT}/gap.wav'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', '0.8', gap], check=True)
    with open(lst, 'w') as f:
        for sc in scenes: f.write(f"file 'takes/{res['scenes'][sc]['use']}'\nfile 'gap.wav'\n")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-ac', '1', '-ar', '44100', '-c:a', 'aac', '-b:a', '128k',
                    f'{OUT}/table-read.m4a'], check=True, cwd=OUT)
    print('chars total', res['chars'])


if __name__ == '__main__':
    main()
