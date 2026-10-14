"""R&D v4 · bảng giờ máy / khung theo lớp từ out/meas/measure.jsonl (light/measure.js, 1080p, trung vị 3 lần đo sau 1 lần làm nóng).
  python3 rnd-hybrid/v4/light/table.py  → in bảng Markdown + ghi out/meas/table.md
Một lớp riêng = composer (MSAA 4 + OutputPass) + lớp đó. "rim" riêng ≈ chi phí composer (shader rim chỉ thêm vài phép tính trên người)
→ composer = rim − base; lớp ròng = lớp riêng − rim riêng. Sai số đo ≈ ±0,05 s (trung vị 3 lần)."""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..', 'out', 'meas')
R = [json.loads(l) for l in open(os.path.join(P, 'measure.jsonl'))]
segs = []; [segs.append(r['seg']) for r in R if r['seg'] not in segs]
cfgs = ['base', 'hdri', 'tex', 'soft', 'rim', 'ao', 'dof', 'grade', 'full']
out = ['| Cảnh | ' + ' | '.join(cfgs) + ' | full / base |', '|---|' + '---|' * (len(cfgs) + 1)]
for s in segs:
    d = {r['cfg']: r['frame_ms'] for r in R if r['seg'] == s}
    row = [f"{d[c] / 1000:.2f}" if c in d else '—' for c in cfgs]
    out.append(f"| {os.path.basename(s)} (t={next(r['t'] for r in R if r['seg'] == s)}) | " + ' | '.join(row) + f" | {d['full'] / d['base']:.1f}× |" if 'full' in d and 'base' in d else f"| {os.path.basename(s)} | " + ' | '.join(row) + ' | — |')
out.append(''); out.append('Lớp ròng (s/khung 1080p): composer = rim − base; mỗi lớp = lớp riêng − rim riêng:')
out.append('| Cảnh | composer (MSAA + output) | hdri | tex | soft | ao | dof | grade + hạt |'); out.append('|---|---|---|---|---|---|---|---|')
for s in segs:
    d = {r['cfg']: r['frame_ms'] for r in R if r['seg'] == s}
    if 'rim' not in d: continue
    g = d['rim']; out.append(f"| {os.path.basename(s)} | {(g - d['base']) / 1000:+.2f} | " + ' | '.join(f"{(d[c] - g) / 1000:+.2f}" if c in d else '—' for c in ['hdri', 'tex', 'soft', 'ao', 'dof', 'grade']) + ' |')
t = '\n'.join(out); print(t); open(os.path.join(P, 'table.md'), 'w').write(t + '\n')
