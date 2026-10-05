"""Gán trích dẫn mất chú ý (câu 4) vào cảnh Sxx: chuỗi ≥ 5 từ liên tiếp trùng lời của cảnh (máy, theo ý đồ C2).
  python3 episodes/ep003/review-c2/attention.py rN"""
import json, os, re, sys
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(EP, 'review-c2', sys.argv[1])
norm = lambda s: re.findall(r"[a-z0-9.']+", s.lower().replace('’', "'"))
scenes = {}
for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
    m = re.match(r'^(S\d{2})\.\d+[a-z]?\s*\|\s*(.*?)\s*\|', ln)
    if m:
        scenes.setdefault(m.group(1), []).extend(norm(re.sub(r'\[[a-z\- ]+\]\s*', '', m.group(2))))
grams = {sc: {tuple(w[i:i + 5]) for i in range(len(w) - 4)} for sc, w in scenes.items()}
key = json.load(open(os.path.join(R, 'key.json')))['items']; rk = json.load(open(os.path.join(R, 'rubric-key.json')))
sc = json.load(open(os.path.join(R, 'scores.json')))
out = {}
for lab, h in rk.items():
    if key[h]['set'] != 'ep003':
        continue
    q = norm(sc[lab].get('attention', ''))
    qs = {tuple(q[i:i + 5]) for i in range(len(q) - 4)}
    hit = sorted(s for s, g in grams.items() if qs & g)
    out[lab] = hit or ([] if not q else ['?'])
cnt = {}
for v in out.values():
    for s in v:
        cnt[s] = cnt.get(s, 0) + 1
json.dump({'per_reader': out, 'count': cnt}, open(os.path.join(R, 'attention.json'), 'w'), indent=1)
print(out, cnt)
