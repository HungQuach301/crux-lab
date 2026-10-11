"""Tập 7 · C3 · sau khi dựng năm đoạn (build_seg.py): spans.json (cổng gốc), dải 6 khung tắt tiếng, clip duyệt có thẻ tiêu đề, đo loudness.
  python3 episodes/ep007/world/c3/review.py [--strips-dir episodes/ep007/review-c3/strips-r1]
spans.json theo mẫu Tập 6: span = [0, total] của clip đoạn; times = tâm 6 lát (toolkit/blind/strips.py frame_times); muted_read = cột
"muted read (type 1)" của story/beats.md, chép NGUYÊN VĂN (đọc thẳng từ bảng); narration = câu kịch bản hiện tại của cảnh.
Clip duyệt: thẻ tiêu đề 1,2 s (lặng) trước mỗi đoạn, nối theo thứ tự, 540p H.264 + AAC; loudnorm 2 lượt về −14 LUFS / −2,0 dBTP (AAC đẩy đỉnh ~+0,8 dB: −1,5 → −0,7 đo được);
đo lại (ebur128) và ghi review-c3/c3-clip.json."""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(HERE)
sys.path.insert(0, W7)
import wlib            # noqa: E402
ROOT, EP = wlib.ROOT, wlib.EP
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'blind'))
import strips as STR   # noqa: E402

SEGS = [('s01-stack', 'B01', 'S01', 'S01 · The stack'), ('s06-stack', 'B06', 'S06', 'S06 · The stack fills'),
        ('s21-track', 'B21', 'S21', 'S21 · Month track'), ('s23-track', 'B23', 'S23', 'S23 · Month track, once a year'),
        ('s25-bar', 'B25', 'S25', 'S25 · The bar')]
REV = os.path.join(EP, 'review-c3')
SDIR = os.path.join(ROOT, sys.argv[sys.argv.index('--strips-dir') + 1]) if '--strips-dir' in sys.argv else os.path.join(REV, 'strips-r1')
rel = lambda p: os.path.relpath(p, ROOT)


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def muted_reads():
    out = {}
    for ln in open(os.path.join(EP, 'story', 'beats.md'), encoding='utf-8'):
        m = re.match(r'^\| (B\d\d)\b[^|]*\|', ln)
        if m: out[m.group(1)] = [c.strip() for c in ln.strip().strip('|').split('|')][5]
    return out


def dur(p):
    return float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).stdout)


def ebur(p):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', p, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    tail = r[r.rfind('Summary:'):]
    I = float(re.search(r'I:\s+(-?[\d.]+) LUFS', tail).group(1)); tp = float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', tail).group(1))
    return I, tp


MR = muted_reads()
lines = {r['id']: r['text'] for r in wlib.script_rows()}
spans = {'note': 'C3 cổng gốc Tập 7 (gates/C3-root-intent.md): mỗi đoạn một clip 540p riêng (episodes/ep007/world/c3/out/<đoạn>.mp4, dựng bằng '
                 'build_seg.py); span = [0, total] giây của clip; times = tâm 6 lát bằng nhau (toolkit/blind/strips.py frame_times); muted_read = cột '
                 '"muted read (type 1)" của story/beats.md, chép nguyên văn; dải TẮT TIẾNG, GIỮ chữ/số.', 'strips': {}}
os.makedirs(SDIR, exist_ok=True)
for seg, beat, sc, _ in SEGS:
    clip = os.path.join(HERE, 'out', seg + '.mp4'); sp = json.load(open(os.path.join(HERE, seg, 'spine.json')))
    total = sp['total']; d = dur(clip)
    assert abs(d - total) < 0.1, f'{seg}: clip {d} s ≠ spine {total} s'
    name = f'N1-{seg}'
    spans['strips'][name] = {'clip': rel(clip), 'segment': rel(os.path.join(HERE, seg)), 'beat': beat, 'scene': sc, 'type': 1, 'span': [0.0, total],
                             'times': STR.frame_times(0.0, total), 'narration': [f'{k} {v}' for k, v in lines.items() if k.startswith(sc + '.')],
                             'muted_read': MR[beat]}
    one = os.path.join(SDIR, name + '.spans.json'); json.dump({name: [0.0, total]}, open(one, 'w'))
    run([sys.executable, os.path.join(ROOT, 'toolkit/blind/strips.py'), clip, one, SDIR])
    os.replace(os.path.join(SDIR, 'strips.json'), os.path.join(SDIR, name + '.strips.json'))
json.dump(spans, open(os.path.join(HERE, 'spans.json'), 'w'), indent=1, ensure_ascii=False)

# ---------------- clip duyệt: thẻ 1,2 s + đoạn, nối, loudnorm 2 lượt
font = STR._font(); work = os.path.join(EP, 'work', 'review-c3'); os.makedirs(work, exist_ok=True)
V = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', '30']
A = ['-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2']
parts = []
for seg, beat, sc, title in SEGS:
    card = os.path.join(work, f'card-{seg}.mkv')
    dt = f"drawtext=fontfile='{font}':text='{title}':fontsize=56:fontcolor=0xF2F4F7:x=(w-text_w)/2:y=(h-text_h)/2" if font else 'null'
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'color=c=0x0E1116:s=960x540:r=30:d=1.2', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
         '-t', '1.2', '-vf', dt, *V, *A, card])
    body = os.path.join(work, f'body-{seg}.mkv')
    run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(HERE, 'out', seg + '.mp4'), '-vf', 'scale=960:540,setsar=1', *V, *A, body])
    parts += [card, body]
lst = os.path.join(work, 'list.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
raw = os.path.join(work, 'c3-raw.mkv')
run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', raw])
m = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', raw, '-af', 'loudnorm=I=-14:TP=-2.0:LRA=11:print_format=json', '-f', 'null', '-'],
                   capture_output=True, text=True).stderr
ms = json.loads(m[m.rfind('{'):m.rfind('}') + 1])
ln = (f"loudnorm=I=-14:TP=-2.0:LRA=11:measured_I={ms['input_i']}:measured_TP={ms['input_tp']}:measured_LRA={ms['input_lra']}:"
      f"measured_thresh={ms['input_thresh']}:offset={ms['target_offset']}:linear=true")
os.makedirs(REV, exist_ok=True); out = os.path.join(REV, 'c3-clip.mp4')
run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af', ln + ',aresample=48000', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])
I, tp = ebur(out)
rep = {'clip': rel(out), 'duration_s': round(dur(out), 2), 'lufs_integrated': I, 'true_peak_dbtp': tp,
       'pass': {'lufs_-14_pm1': abs(I + 14) <= 1, 'tp_le_-1': tp <= -1.0}, 'order': [s[0] for s in SEGS], 'title_card_s': 1.2,
       'segments_s': {s[0]: json.load(open(os.path.join(HERE, s[0], 'spine.json')))['total'] for s in SEGS}}
json.dump(rep, open(os.path.join(REV, 'c3-clip.json'), 'w'), indent=1, ensure_ascii=False)
print(json.dumps(rep, ensure_ascii=False))
