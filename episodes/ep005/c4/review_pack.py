"""Tập 5 · C4 · gói cổng gốc tắt tiếng + bản xem (chủ dự án chạy kiểm mù, phiên dựng không chạy):
  python3 episodes/ep005/c4/review_pack.py
Ra (episodes/ep005/review-c4/):
  animatic-540p.mp4      bản sao master 540p (out/video.mp4)
  spans.json             mỗi nhịp loại 1 (beats.md, + N1/S06, N2/S13): span (giờ master), cảnh, lời nguyên văn (script.md), muted_read
  strips/<id>.png        6 khung TẮT TIẾNG mỗi span (toolkit/blind/strips.py, tâm 6 lát bằng nhau) + strips/strips.json
  highlights.mp4         clip nổi bật ≤ 3 phút (cold open + nhịp đỉnh mỗi hồi), cắt từ master
Span = đầu câu đầu → cuối câu cuối + 0,5 s của cảnh (giờ trong out/factory/timeline.json), không gồm ident."""
import json, os, re, shutil, subprocess, sys
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
RV = os.path.join(EP, 'review-c4')
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{\w+\}\s+)?(.+?)\s*<!--')
BEAT = re.compile(r'^\| (B\d\d)[^|]*\| (S\d\d)[^|]*\|[^|]*\|[^|]*\| (\d) \| ([^|]*)\|')

lines = {}
for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
    m = LINE.match(ln)
    if m:
        lines.setdefault(m[1], []).append(f'{m[1]}.{m[2]} {m[3].strip()}')
muted = {}
for ln in open(os.path.join(EP, 'story', 'beats.md'), encoding='utf-8'):
    m = BEAT.match(ln)
    if m:
        muted[m[2]] = (m[1], int(m[3]), m[4].strip().strip('"'))
c3 = json.load(open(os.path.join(EP, 'review-c3', 'spans.json')))['strips']
tl = json.load(open(os.path.join(EP, 'out', 'factory', 'timeline.json')))
sents = {s['id']: s for s in tl['sentences']}
spans = {}
for sc, (bid, typ, read) in sorted(muted.items()):
    extra = {'S06': ('N1-S06', c3['N1-calendar']['muted_read'])}.get(sc)
    if typ != 1 and not extra:
        continue
    ids = [l.split()[0] for l in lines[sc]]
    t0, t1 = sents[ids[0]]['start'], sents[ids[-1]]['end'] + 0.5
    key = extra[0] if extra else f'{bid}-{sc}'
    if sc == 'S13':
        key = f'{bid}-{sc}-N2'
    note = 'type 2 in beats.md; N1 calendar (C3) in context — C3-answer: no-voice blind check of S06 must show 0 advice' if extra else ''
    if sc == 'S13':
        note = 'N2 bars (C3) in context — C3-answer: blind check of S13 must show 0 advice'
    if sc == 'S03':
        note = 'S03.3 B+2 label on screen: "Fannie Mae: wait ≥ 2 years · loan ≤ 75%" (claims value_removal_seasoning_years, value_removal_ltv_early)'
    spans[key] = {'span': [round(t0, 3), round(t1, 3)], 'scene': sc, 'beat': bid, 'type': typ, 'narration': lines[sc],
                  'muted_read': extra[1] if extra else read, **({'note': note} if note else {})}
os.makedirs(RV, exist_ok=True)
vid = os.path.join(RV, 'animatic-540p.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(EP, 'out', 'video.mp4'), '-c:v', 'libx264', '-crf', '20', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                '-c:a', 'copy', '-movflags', '+faststart', vid], check=True)   # master 540p (CBR 17M ≈ 1 GB) → bản xem cùng khung, CRF 20
json.dump({'video': os.path.relpath(vid, ROOT), 'note': 'span = [t0, t1] in master seconds (out/factory/timeline.json); strips are MUTED frames; muted_read = beats.md type-1 column (S06: C3 N1 read)',
           'spans': spans}, open(os.path.join(RV, 'spans.json'), 'w'), indent=1, ensure_ascii=False)
sp = os.path.join(RV, 'strips', '_spans.json'); os.makedirs(os.path.dirname(sp), exist_ok=True)
json.dump({k: v['span'] for k, v in spans.items()}, open(sp, 'w'))
subprocess.run([sys.executable, os.path.join(ROOT, 'toolkit', 'blind', 'strips.py'), vid, sp, os.path.join(RV, 'strips')], check=True)
os.remove(sp)
# highlights ≤ 3 phút: cold open, S08 (đỉnh hồi 1), S11 + S12.3–S12.4 (đỉnh hồi 2 + đối trọng), S13, S17 (đỉnh hồi 3)
sc = {s['id']: s for s in tl['scenes']}
cuts = [(0.0, sc['S03']['start'] + sc['S03']['dur'] - 3.0), (sc['S08']['start'], sc['S08']['start'] + sc['S08']['dur']),
        (sc['S11']['start'], sc['S11']['start'] + sc['S11']['dur']), (sents['S12.3']['start'] - 0.3, sc['S12']['start'] + sc['S12']['dur']),
        (sc['S13']['start'], sc['S13']['start'] + sc['S13']['dur']), (sc['S17']['start'], sc['S17']['start'] + sc['S17']['dur'])]
assert sum(b - a for a, b in cuts) <= 180, sum(b - a for a, b in cuts)
parts = []
for i, (a, b) in enumerate(cuts):
    pp = os.path.join(RV, f'_h{i}.mp4'); parts.append(pp)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{a:.3f}', '-t', f'{b - a:.3f}', '-i', vid, '-af', f'afade=t=in:d=0.05,afade=t=out:st={b - a - 0.1:.3f}:d=0.1',
                    '-c:v', 'libx264', '-crf', '20', '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', pp], check=True)
lst = os.path.join(RV, '_h.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', '-movflags', '+faststart', os.path.join(RV, 'highlights.mp4')], check=True)
for p in parts + [lst]:
    os.remove(p)
print('spans', len(spans), list(spans), '· highlights', round(sum(b - a for a, b in cuts), 1), 's')
