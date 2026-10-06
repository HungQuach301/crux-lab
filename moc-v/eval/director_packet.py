"""Mốc V · gói cho LƯỢT ĐẠO DIỄN (agent độc lập "xem bản có tiếng").
  python3 moc-v/eval/director_packet.py <video.mp4> <out_dir> [--stems <dir>]
Ra: sheet-1.png, sheet-2.png (mỗi 0,5 s một khung, có mốc giờ), audio.png (đường mức từng lớp + phổ), transcript.txt (ASR có mốc từ),
events.txt (sự kiện âm theo spine nếu có stems)."""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
video, out = sys.argv[1:3]; os.makedirs(out, exist_ok=True)
stems = sys.argv[sys.argv.index('--stems') + 1] if '--stems' in sys.argv else None
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', video], capture_output=True, text=True).stdout)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', 'fps=2,scale=320:180', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 180, 320, 3)
half = (len(fr) + 1) // 2
for k, part in enumerate((fr[:half], fr[half:])):
    cols = 7; rows = (len(part) + cols - 1) // cols
    sh = Image.new('RGB', (cols * 320, rows * 205), (30, 30, 30)); d = ImageDraw.Draw(sh)
    for i, f in enumerate(part):
        x, y = (i % cols) * 320, (i // cols) * 205; sh.paste(Image.fromarray(f), (x, y + 25))
        d.text((x + 4, y + 3), f"{(k * half + i) / 2:.1f}s", fill=(255, 255, 0), font=font)
    sh.save(os.path.join(out, f'sheet-{k + 1}.png'))
# âm: mức (dBFS, 50 ms) từng lớp
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
def lvl(p):
    x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '8000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    n = 400; x = x[:len(x) // n * n].reshape(-1, n); return np.arange(len(x)) * n / 8000, 20 * np.log10(np.sqrt((x ** 2).mean(1)) + 1e-6)
fig, ax = plt.subplots(2, 1, figsize=(22, 8), sharex=True)
layers = [('mix', video)] + ([(n, os.path.join(stems, n + '.wav')) for n in ('voice', 'music', 'data', 'sfx', 'room')] if stems else [])
for n, p in layers:
    t, v = lvl(p); ax[0].plot(t, v, label=n, lw=1.2 if n != 'mix' else 0.6)
ax[0].set_ylim(-80, 0); ax[0].legend(loc='upper right'); ax[0].set_ylabel('dBFS (50 ms)'); ax[0].grid(alpha=.3); ax[0].set_xticks(np.arange(0, dur + 1, 2))
x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
ax[1].specgram(x, NFFT=1024, Fs=16000, noverlap=768, cmap='magma', vmin=-120); ax[1].set_ylabel('Hz'); ax[1].set_xlabel('s')
plt.tight_layout(); plt.savefig(os.path.join(out, 'audio.png'), dpi=60)
from faster_whisper import WhisperModel
m = WhisperModel('small.en', device='cpu', compute_type='int8')
segs, _ = m.transcribe(x, word_timestamps=True, language='en')
with open(os.path.join(out, 'transcript.txt'), 'w') as f:
    for s in segs:
        f.write(f"[{s.start:6.2f}–{s.end:6.2f}] " + ' '.join(f"{w.word.strip()}@{w.start:.2f}" for w in s.words) + '\n')
if stems:
    sp = json.load(open(os.path.join(ROOT, 'moc-v/proto/spine.json')))
    with open(os.path.join(out, 'events.txt'), 'w') as f:
        for e in sp['events']:
            if e['kind'] != 'data': f.write(f"{e['t']:6.2f}s {e['kind']}\n")
        f.write(f"data notes (sonification): {sum(e['kind'] == 'data' for e in sp['events'])} notes, {min(e['t'] for e in sp['events'] if e['kind']=='data'):.1f}–{max(e['t'] for e in sp['events'] if e['kind']=='data'):.1f}s\n")
        f.write('music tension map [t, 0..1]: ' + json.dumps(sp['tension']) + '\n')
print(out)
