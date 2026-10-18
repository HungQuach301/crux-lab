#!/usr/bin/env python3
"""Ảnh bìa R1-AI · vòng 4 (điều phối 18/10, G3 Tập 9 câu 2): chữ ảnh khớp số của tiêu đề "Renter Ahead in 155 of 307 Months".
  EP9_ROOT=<worktree nhánh tập 9> python3 packaging/r1/ai/round4.py → packaging/r1/final/ep009-tc<1..3>.jpg + ai/checks-r4.json
Chỉ đổi CHỮ trên nền đã có (ep009-a đồng xu, ep009-b bập bênh); cùng bố cục/phép kiểm của final.py/round2.py."""
import json, os, pathlib, subprocess, sys
from PIL import Image
H = pathlib.Path(__file__).resolve().parent; F = H.parent / 'final'
sys.path.insert(0, str(H))
from final import fit, check   # noqa: E402
SET = [
 ('ep009', 'a', 'COIN FLIP?', '155–152', 'debt', 'n_renter_ahead_stocks_10y 155–152 (người thuê–người mua) (/307) — khớp tiêu đề'),
 ('ep009', 'b', 'COIN FLIP?', '155–152', 'debt', 'như trên, nền bập bênh'),
 ('ep009', 'a', 'COIN FLIP?', '49.5%', 'debt', 'share_buyer_ahead_stocks_10y — bản cũ, giữ để đo'),
]
if __name__ == '__main__':
    tmp = H / 'cand4'; tmp.mkdir(exist_ok=True); J = []; n = {}
    for ep, v, l1, num, pil, note in SET:
        n[ep] = n.get(ep, 0) + 1
        J.append(dict(id=f'{ep}-tc{n[ep]}', bg=str(H / 'raw' / f'{ep}-{v}.jpg'), out=str(tmp / f'{ep}-tc{n[ep]}.png'),
                      outBare=str(tmp / f'{ep}-tc{n[ep]}-bare.png'), cropY=80, l1=l1, l1Size=fit(l1, 96, 700),
                      numSize=fit(num, 150, 700), num=num, pillar=pil, arrow=None, bgId=f'{ep}-{v}', note=note))
    (H / 'jobs-r4.json').write_text(json.dumps(J, indent=1, ensure_ascii=False))
    subprocess.run(['node', str(H / 'compose.js'), str(H / 'jobs-r4.json')], check=True, env=dict(os.environ, NODE_PATH='/opt/node-tools/node_modules'))
    R = []
    for j in J:
        c = check(j); c.update(bg=j['bgId'], note=j['note']); R.append(c)
        Image.open(j['out']).convert('RGB').save(F / f"{j['id']}.jpg", quality=92)
        Image.open(j['out']).convert('RGB').resize((168, 94), Image.LANCZOS).save(F / 'small' / f"{j['id']}.png")
        print(c['id'], c['bg'], 'ĐẠT' if c['ok'] else 'TRƯỢT', c['texts'], c['cap_px_168'], c['contrast'], c['claim_risk'])
    (H / 'checks-r4.json').write_text(json.dumps(R, ensure_ascii=False, indent=1))
