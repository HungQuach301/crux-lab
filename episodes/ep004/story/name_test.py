"""Tập 4 · sau G1: thử tên thay "Glen" bằng ASR trước khi sửa kịch bản. Câu thật của S01.2 với tên ứng viên; Eric eleven_v3 seed 1;
faster-whisper small.en như A14. Tên đạt khi ASR ra đúng chữ ở cả 2 seed.  python3 episodes/ep004/story/name_test.py"""
import base64, json, os, sys, requests
from faster_whisper import WhisperModel
OUT = '/home/user/crux-lab/episodes/ep004/review-g1/names'
URL = 'https://api.elevenlabs.io/v1/text-to-speech/cjVigY5qzO86Huf0OWal/stream/with-timestamps?output_format=mp3_44100_128'
NAMES = ['Frank', 'Tom', 'Mark', 'Paul']
wm = WhisperModel('small.en', device='cpu', compute_type='int8'); rep = {}
for n in NAMES:
    rep[n] = []
    for seed in (1, 2):
        text = f"That's Rosa and {n}, an illustrative Phoenix couple who bought in two thousand, if their home rose like the average."
        p = f'{OUT}/{n}-s{seed}.mp3'
        if not os.path.exists(p):
            r = requests.post(URL, json={'text': text, 'model_id': 'eleven_v3', 'seed': seed}, timeout=120, stream=True); r.raise_for_status()
            open(p, 'wb').write(b''.join(base64.b64decode(json.loads(l)['audio_base64']) for l in r.iter_lines() if l.strip() and json.loads(l).get('audio_base64')))
        segs, _ = wm.transcribe(p, language='en', beam_size=5, condition_on_previous_text=False)
        t = ' '.join(s.text for s in segs); rep[n].append({'seed': seed, 'asr': t.strip(), 'ok': f' {n}' in t or f' {n},' in t})
json.dump(rep, open(f'{OUT}/result.json', 'w'), indent=1)
for n, v in rep.items(): print(n, [x['ok'] for x in v], v[0]['asr'][:70])
