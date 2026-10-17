#!/usr/bin/env python3
"""Tờ duyệt R1-AI (D-015): packaging/r1/DUYET-AI.md — mỗi video: tiêu đề T1 đã duyệt + 3 ảnh AI đã chọn + 1 đối chứng mã, ở cỡ thật (bấm mở 1280×720),
điện thoại 360 px và 168×94, kèm điểm Claude chấm (ai/selection.json) và kiểm máy (ai/checks.json, checks.json).  python3 packaging/r1/sheet_ai.py"""
import json, pathlib
from PIL import Image
H = pathlib.Path(__file__).resolve().parent; F = H / 'final'; (F / 'small').mkdir(exist_ok=True)
T = json.loads((H / 'titles.json').read_text()); SEL = json.loads((H / 'ai/selection.json').read_text())
CA = {c['id']: c for c in json.loads((H / 'ai/checks.json').read_text())}; CM = {c['id']: c for c in json.loads((H / 'checks.json').read_text())}
NAME = {'ep005': 'Tập 5 · PMI', 'ep008': 'Tập 8 · rent vs buy', 'ep009': 'Tập 9 · rent & invest (sắp đăng)', 'ep001': 'Tập 1 · refi',
        'ep002': 'Tập 2 · vay học', 'ep006': 'Tập 6 · annuity', 'ep007': 'Tập 7 · 15 vs 30'}
o = ['# Tờ duyệt ảnh bìa R1-AI (D-015)', '',
     'Mỗi video: **chọn 1 ảnh mặc định**; 3 ảnh vào **Test & Compare** (đề nghị: #1, #2, #3; đổi #3 lấy đối chứng mã #0 nếu muốn thử AI vs mã). '
     'Tiêu đề = **T1 đã duyệt 17/10**. Phần hình #1–#3: OpenAI `gpt-image-1` (không chữ, `RIGHTS.md` §H); chữ, số, logo: ghép bằng mã. '
     'Điểm /10 = Claude chấm bằng mắt ở 360 px và 168×94 (rõ chủ thể 4 + khớp video 4 + chữ không đè chủ thể 2). '
     'Kiểm máy 168×94: chữ hoa ≥ 9 px, tương phản ≥ 4,5:1 (chữ trắng / chữ màu trụ). Tập 3: giữ nguyên làm đối chứng tới 01/11 — không có ở tờ này.', '',
     'Loại (3/video) và lý do: `ai/selection.json`; cả 42 nền: `ai/raw/`.', '']
for ep in ['ep005', 'ep008', 'ep009', 'ep001', 'ep002', 'ep006', 'ep007']:
    s = SEL[ep]; t = T[ep]
    o += [f'## {NAME[ep]} — `{t["video"]}`', '', f'**T1:** {t["titles"][0]} ({len(t["titles"][0])} ký tự)', '',
          '| # | cỡ thật (bấm mở 1280×720) | điện thoại 360 px | 168×94 | điểm Claude | kiểm máy |', '|---|---|---|---|---|---|']
    items = [(i + 1, f'{ep}-{i + 1}-ai{v}.jpg', s['scores'][v], CA[f'{ep}-{v}']) for i, v in enumerate(s['keep'])]
    items.append((0, f'{ep}-0-ma{s["control"][-1]}.jpg', [None, f'đối chứng dựng bằng mã R1 ({s["control"]}, khung phim)'], CM[s['control']]))
    for n, fn, (sc, why), c in items:
        Image.open(F / fn).resize((168, 94), Image.LANCZOS).save(F / 'small' / fn.replace('.jpg', '.png'))
        if 'contrast' in c:
            ok = c['ok']; m = f"chữ {c['cap_px_168'][0]}/{c['cap_px_168'][1]} px · {c['contrast'][0]}:1 / {c['contrast'][1]}:1 · \"{' '.join(c['texts'])}\""
        else:
            ok = c['ok'] and not c['claim_risk']; m = f"chữ {c['cap_px_168']} px · {c['contrast_ink']}:1 / {c['contrast_accent']}:1 · \"{' / '.join(c['texts'])}\""
        o.append(f'| **#{n}**{" mã" if n == 0 else ""} | <a href="final/{fn}"><img src="final/{fn}" width="480"></a> | <img src="final/{fn}" width="360"> | '
                 f'<img src="final/small/{fn.replace(".jpg", ".png")}" width="168" height="94"> | {"—" if sc is None else sc}: {why} | {"ĐẠT" if ok else "**TRƯỢT**"}: {m} |')
    o.append('')
(H / 'DUYET-AI.md').write_text('\n'.join(o)); print('DUYET-AI.md')

# Vòng 2 (chủ dự án 17/10, rà khớp khán giả): bộ 3 ảnh T&C mới — chỉ đổi chữ (+ 1 nền Tập 6 nghiêm/thực tế); Tập 2, 9 giữ bộ vòng 1.
R2 = {c['id']: c for c in json.loads((H / 'ai/checks-r2.json').read_text())}
SC2 = {'ep005-tc1': (9, 'số khớp tiêu đề "8 Years"; khiên + đồng hồ cát'), 'ep005-tc2': (9, 'như #1, đồng hồ cát rõ nhất ở 168 px'),
       'ep005-tc3': (8.5, 'bản "23 MONTHS" giữ để đo lệch/khớp số với tiêu đề'),
       'ep008-tc1': (9, 'đúng câu hỏi tiêu đề; chữ màu lớn đọc ngay ở 168 px'), 'ep008-tc2': (8.5, 'bản cũ, có số — giữ để đo'),
       'ep008-tc3': (8, 'câu hỏi trên nền phố sáng/tối'), 'ep001-tc1': (8.5, 'vòng 3: số khớp tiêu đề T1 (1.12 điểm của Walt); đồng hồ = tháng hoàn phí'),
       'ep001-tc2': (8, 'vòng 3: "worth it" = cụm tìm kiếm; $5,124 = hoá đơn của Nora, nền thư đề nghị (0:33); 5 từ > luật 4 từ (chữ chủ dự án chỉ định)'), 'ep001-tc3': (8, 'bản cũ — giữ để đo'),
       'ep007-tc1': (8.5, 'câu hỏi đúng lựa chọn; chồng vàng = khoản dự phòng'), 'ep007-tc2': (8, 'Leo vs Tessa'), 'ep007-tc3': (7.5, 'lưới an toàn'),
       'ep006-tc1': (8, 'khung mất mát rõ; séc leo bậc thấp hơn thùng hàng'),
       'ep006-tc2': (7.5, 'nền nghiêm/thực tế cho khán giả lớn tuổi; tấm séc bị chữ che — giỏ hàng là chủ thể'), 'ep006-tc3': (7.5, 'bản cũ — giữ để đo')}
o2 = ['# Tờ duyệt ảnh bìa R1-AI — VÒNG 2 (bộ Test & Compare mới)', '',
      'Chủ dự án 17/10: rà khớp khán giả, một vòng sửa chữ (`ai/round2.py`, cùng bố cục và phép kiểm). Mỗi video: **3 ảnh = bộ Test & Compare**, #1 = đề nghị mặc định. '
      'Tập 2 và Tập 9 không đổi (bộ vòng 1 bên dưới). Kiểm 168×94: **15/15 ĐẠT**, claim-risk 0.', '']
for ep in ['ep005', 'ep008', 'ep001', 'ep007', 'ep006']:
    o2 += [f'## {NAME[ep]} — `{T[ep]["video"]}` · T1: {T[ep]["titles"][0]}', '', '| TC | cỡ thật (bấm mở) | điện thoại 360 px | 168×94 | điểm Claude | kiểm máy · nền · claim |', '|---|---|---|---|---|---|']
    for i in (1, 2, 3):
        k = f'{ep}-tc{i}'; c = R2[k]; fn = f'{k}.jpg'; sc, why = SC2[k]
        Image.open(F / fn).resize((168, 94), Image.LANCZOS).save(F / 'small' / f'{k}.png')
        o2.append(f'| **#{i}** | <a href="final/{fn}"><img src="final/{fn}" width="480"></a> | <img src="final/{fn}" width="360"> | <img src="final/small/{k}.png" width="168" height="94"> | '
                  f'{sc}: {why} | {"ĐẠT" if c["ok"] else "**TRƯỢT**"}: "{" ".join(t for t in c["texts"] if t)}" · chữ {"/".join(map(str, c["cap_px_168"]))} px · '
                  f'{" / ".join(map(str, c["contrast"]))}:1 · nền `{c["bg"]}` · {c["note"]} |')
    o2.append('')
(H / 'DUYET-AI.md').write_text('\n'.join(o2) + '\n\n---\n\n' + (H / 'DUYET-AI.md').read_text()); print('DUYET-AI.md + vòng 2')

