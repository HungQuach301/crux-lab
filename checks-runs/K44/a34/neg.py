"""K4.4b · A34 đối chứng trên âm thật Tập 7 (master 529471f0…): câu S15.3 nguyên bản, và bản THAY âm của từ "Tessa's" bằng âm của từ "stack"
lấy từ S09.3 (cùng giọng, cùng master) → tên không được nói. Cả small.en và medium.en (cùng cách giải mã của A14)
nghe hai bản; in chữ nghe được.  python3 -I checks-runs/K44/a34/neg.py <out.json>"""
import json, os, subprocess, sys, tempfile
import numpy as np, soundfile as sf
from faster_whisper import WhisperModel
SR = 48000
V = '/home/user/crux-lab/episodes/ep007/out/video.mp4'
C = json.load(open('/home/user/k44-cache/ep007/asr-529471f0f2283f4f-08fcd7fd.json'))
sc = json.load(open('/home/user/crux-lab/episodes/ep007/out/script.json'))['sentences']
s = next(x for x in sc if x['id'] == 'S15.3')
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', V, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).copy()
w = next(v for v in C if v['sentence'] == 'S15.3' and v['w'].startswith('Tesla'))
d = next(v for v in C if v['sentence'] == 'S09.3' and v['w'].startswith('stack'))
a, b = s['start'] - 0.6, s['end'] + 0.6
clip = x[int(a * SR):int(b * SR)].copy()
neg = clip.copy()
i0, i1 = int((w['start'] - a) * SR), int((w['end'] - a) * SR)
donor = x[int(d['start'] * SR):int(d['end'] * SR)]
seg = np.zeros(i1 - i0, np.float32); seg[:min(len(seg), len(donor))] = donor[:len(seg)]
neg[i0:i1] = seg
out = {'sentence': s['text'], 'replaced': [w['start'], w['end']], 'donor': [d['w'], d['start'], d['end']]}
for name, m in (('small.en', WhisperModel('small.en', device='cpu', compute_type='int8')), ('medium.en', WhisperModel('medium.en', device='cpu', compute_type='int8'))):
    for tag, y in (('original', clip), ('name-replaced', neg)):
        p = tempfile.mktemp(suffix='.wav'); sf.write(p, y, SR, subtype='FLOAT')
        segs, _ = m.transcribe(p, word_timestamps=True, beam_size=5, language='en', condition_on_previous_text=False, vad_filter=False)
        out[f'{name}/{tag}'] = ' '.join(ww.word.strip() for sg in segs for ww in (sg.words or []))
        os.unlink(p); print(name, tag, out[f'{name}/{tag}'], flush=True)
json.dump(out, open(sys.argv[1], 'w'), indent=1)
