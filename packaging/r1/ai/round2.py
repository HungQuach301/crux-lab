#!/usr/bin/env python3
"""Ảnh bìa R1-AI · vòng 2 (chủ dự án 17/10, rà khớp khán giả): chỉ đổi CHỮ trên nền đã có (+ 1 nền Tập 6 nghiêm/thực tế) → bộ 3 ảnh T&C mới mỗi video.
  EP9_ROOT=… python3 packaging/r1/ai/round2.py → packaging/r1/final/<tập>-tc<1..3>.jpg + ai/checks-r2.json
Cùng bố cục/phép kiểm của final.py (168×94: chữ hoa ≥ 9 px, tương phản ≥ 4,5:1; claim-risk 0; ≤ 4 từ)."""
import json, os, pathlib, subprocess, sys
from PIL import Image
H = pathlib.Path(__file__).resolve().parent; F = H.parent / 'final'
sys.path.insert(0, str(H))
from final import fit, check   # noqa: E402

# (tập, nền, dòng ngữ cảnh, số, trụ, ghi chú claim). Bộ T&C = 3 dòng đầu mỗi tập theo thứ tự.
SET = [
 ('ep005', 'a', 'PMI FOR', '8 YEARS?', 'debt', 'lịch luật: xin huỷ ở payment 99 ≈ 8 năm (lời 0:10 "about 8 years") — khớp tiêu đề T1'),
 ('ep005', 'd', 'PMI FOR', '8 YEARS?', 'debt', 'như trên'),
 ('ep005', 'a', 'ON PAPER?', '23 MONTHS', 'debt', 'medianB_months_to80 — giữ 1 bản để đo'),
 ('ep008', 'b', 'RENT =', 'WASTED?', 'debt', 'câu hỏi của Nina (0:26) = tiêu đề T1; chữ màu là chữ, không thêm số (75.6 % đứng một mình dễ đọc thành "75.6 % lãng phí")'),
 ('ep008', 'b', 'WORST CASE', '-$82,385', 'debt', 'adv_2006-06 — giữ để đo'),
 ('ep008', 'a', 'RENT =', 'WASTED?', 'debt', 'như dòng 1, nền phố'),
 ('ep001', 'c', 'RATE DROP', 'NEEDED: 1.12', 'debt', 'vòng 3 (chủ dự án 17/10): Walt $115,000 cần lãi giảm 1.12 điểm để hoàn phí trong 3 năm (lời 7:10) — khớp tiêu đề T1'),
 ('ep001', 'a', 'WORTH IT?', '$5,124 IN FEES', 'debt', 'vòng 3: hoá đơn refi của Nora $5,124 (median HMDA 2025, lời 0:33); 5 từ — chữ chủ dự án chỉ định, vượt luật ≤ 4 từ'),
 ('ep001', 'c', 'FEES BACK?', 'MONTH 30', 'debt', 'bản cũ — giữ để đo'),
 ('ep007', 'a', '15 OR 30?', '', 'debt', 'số đã ở tiêu đề; câu hỏi của Tessa (0:11)'),
 ('ep007', 'd', '15 OR 30?', '', 'debt', 'như trên'),
 ('ep007', 'b', '15 OR 30?', '', 'debt', 'như trên'),
 ('ep006', 'c', 'BUYING POWER', 'LOSES 19%?', 'retire', '100 − 80.7 (median_real_value_2pct_payment_after_20y_pct) = 19.3 % sức mua mất ở mốc 20 năm, trung vị 715 giai đoạn; điều kiện ở dòng 1 mô tả'),
 ('ep006', 'g', 'BUYING POWER', 'LOSES 19%?', 'retire', 'như trên — nền nghiêm/thực tế (séc + giỏ hàng, không người)'),
 ('ep006', 'c', 'STILL BUYS', '80.7%', 'retire', 'bản cũ — giữ để đo'),
]

if __name__ == '__main__':
    tmp = H / 'cand2'; tmp.mkdir(exist_ok=True); J = []; n = {}
    for ep, v, l1, num, pil, note in SET:
        n[ep] = n.get(ep, 0) + 1
        J.append(dict(id=f'{ep}-tc{n[ep]}', bg=str(H / 'raw' / f'{ep}-{v}.jpg'), out=str(tmp / f'{ep}-tc{n[ep]}.png'),
                      outBare=str(tmp / f'{ep}-tc{n[ep]}-bare.png'), cropY=80, l1=l1, l1Size=fit(l1, 96, 760 if l1 == 'BUYING POWER' else 700) if num else fit(l1, 130, 760), num=num,
                      numSize=fit(num, 150, 780 if num == '$5,124 IN FEES' else 620) if num else 1, pillar=pil, arrow=None, bgId=f'{ep}-{v}', note=note))
    (H / 'jobs-r2.json').write_text(json.dumps(J, indent=1, ensure_ascii=False))
    subprocess.run(['node', str(H / 'compose.js'), str(H / 'jobs-r2.json')], check=True, env=dict(os.environ, NODE_PATH='/opt/node-tools/node_modules'))
    R = []
    for j in J:
        c = check(j); c.update(bg=j['bgId'], note=j['note']); R.append(c)
        Image.open(j['out']).convert('RGB').save(F / f"{j['id']}.jpg", quality=92)
        print(c['id'], c['bg'], 'ĐẠT' if c['ok'] else 'TRƯỢT', c['texts'], c['cap_px_168'], c['contrast'], c['claim_risk'])
    (H / 'checks-r2.json').write_text(json.dumps(R, ensure_ascii=False, indent=1))
