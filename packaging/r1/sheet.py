#!/usr/bin/env python3
"""Tờ duyệt R1: packaging/r1/DUYET.md (GitHub hiển thị) — mỗi tập 3 tiêu đề (đã xếp hạng) cạnh 3 ảnh bìa: cỡ thật (bấm mở PNG 1280×720),
cỡ điện thoại (360 px, lưới trang chủ di động) và 168×94 (cột đề xuất), kèm kết quả kiểm máy từ checks.json.  python3 packaging/r1/sheet.py"""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
T = json.loads((H / 'titles.json').read_text()); C = {c['id']: c for c in json.loads((H / 'checks.json').read_text())}
NAME = {'ep001': 'Tập 1 · refi', 'ep002': 'Tập 2 · vay học', 'ep003': 'Tập 3 · EE vs T-bill', 'ep005': 'Tập 5 · PMI', 'ep006': 'Tập 6 · annuity',
        'ep007': 'Tập 7 · 15 vs 30', 'ep008': 'Tập 8 · rent vs buy', 'ep009': 'Tập 9 · rent & invest (sắp đăng)'}
o = ['# Tờ duyệt đóng gói R1', '', 'Chọn mỗi tập **1 tiêu đề (T1–T3) + 1 ảnh mặc định (A–C)**; hai ảnh còn lại vào Test & Compare. Thứ tự tiêu đề = xếp hạng đề nghị (lý do: `R1.md` §1). '
     'Ảnh: bấm để mở cỡ thật 1280×720. Kiểm máy ở 168×94: chữ hoa ≥ 9 px và tương phản WCAG ≥ 4,5:1 (chữ trắng và chữ màu trụ, so với nền sáng nhất 10 % sau chữ).', '']
for ep, t in T.items():
    o += [f'## {NAME[ep]} — `{t["video"]}`', '', f'Hiện tại: *{t["now"]}*', '']
    o += [f'- **T{i + 1}** ({len(x)} ký tự): {x}' for i, x in enumerate(t['titles'])] + ['']
    o += ['| | cỡ thật (thu nhỏ để xem, bấm mở 1280×720) | điện thoại 360 px | 168×94 | kiểm máy |', '|---|---|---|---|---|']
    for v in 'ABC':
        c = C[f'{ep}-{v}']; ok = 'ĐẠT' if c['ok'] and not c['claim_risk'] else '**TRƯỢT**'
        o.append(f'| **{v}** · {" / ".join(c["texts"])} | <a href="{ep}-{v}.png"><img src="{ep}-{v}.png" width="480"></a> | <img src="{ep}-{v}.png" width="360"> | '
                 f'<img src="small/{ep}-{v}.png" width="168" height="94"> | {ok}: chữ {c["cap_px_168"]} px · {c["contrast_ink"]}:1 / {c["contrast_accent"]}:1'
                 f'{" · claim-risk: " + "; ".join(c["claim_risk"]) if c["claim_risk"] else ""} |')
    o.append('')
(H / 'DUYET.md').write_text('\n'.join(o))
print('DUYET.md', len(T), 'tập')
