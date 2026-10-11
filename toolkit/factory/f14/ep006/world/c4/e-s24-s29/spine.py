"""Tập 6 · C4 · ĐOẠN E = S24–S29 (Hồi 3: cùng mức tăng, ba tháng bắt đầu). Lời + giờ = timeline của nhà máy (c4kit.Seg, 0 ký tự EL).
  python3 episodes/ep006/world/c4/e-s24-s29/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3, có âm trong lặng)
Một thế giới, ba cột [người][séc][hàng 10 thùng] đứng như C3 s29 (Edna −5,6 · Ruth 0,4 · Carl 6,4); cột không nói tới thì mờ.
S24 (port C3 s24-carl, đã duyệt) + lượt đạo diễn C3: lia Ruth → Carl đi qua hàng của Ruth (không khung trống); "fastest" = thanh GIÁ (accent) mọc
×1,0638^20 cạnh hàng của Carl suốt S24.3 (vật chuyển động gắn "fastest price rise"); "every" = bộ đếm 1 → 20, hàng mờ mỗi năm tới 0,431; ô nhỏ
đường của Ruth: năm 1–15 đậm, cuối mờ; "never" = hàng Carl loé + ô Ruth/Carl so cạnh.
S25 (SỐ NEO, lặng 0,75 s trước câu): "forty" = "rising check: 43.1%"; lia, "level" = hàng của séc đều của Carl tối tới 0,29 ("level check: 29.0%");
"half" = vạch nửa hàng (5 thùng). S26: dải nhỏ 715 quãng, thập niên 1960 sáng, thanh của Carl (màu Carl); "1960s starts, typical: 44.3%".
S27 (port C3 s27-edna) + lượt đạo diễn: Edna hiện sẵn (lia từ đồ thị về thế giới trước tên); "Twenty" = bộ đếm 1 → 20 (thùng thứ 10 chập chờn năm
2–5 rồi sáng lại, trần 10); lùi máy: hai thanh 20 năm trên một trục CÓ MỐC NĂM 1949 / 1966 / 1969 / 1986, phần chồng tô màu nhấn (accent = giá);
"end" = hàng Edna năm 18 → 20 vẫn 10; "start" = hàng Carl (về khởi điểm) năm 1 → 3, thùng thứ 10 mờ đi (loé).
S28: Ruth ở 85: hai thanh một năm (giá +3.4% accent · mức tăng của bà +2% ink); đối trọng "One year of history, not a forecast".
S29 (port C3 s29-three, ngoại lệ S29 (a)) + lượt đạo diễn: máy gần hơn; ba séc cùng lớn lên ("Same raise"); hàng mờ theo tên; đồ thị: 10 · about 9 ·
about 4; "month" = ba tháng bắt đầu sáng + loé (điều khác nhau duy nhất)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c4kit as K
SV = K.SV
import json
YOY = json.load(open(os.path.join(K.EP, 'out', 'model.json')))['raw']['cpi_yoy_latest_pct']
S = K.Seg(['S24', 'S25', 'S26', 'S27', 'S28', 'S29'])
B = [
 ('b0', 'S24.1', 'world', 'Ruth không phải trường hợp tệ nhất, cũng không phải tốt nhất.', 'Ruth sau hàng của bà (≈ 9 sáng).',
  {'ruth': '@S24.1:Ruth', 'best': '@S24.1:best'}, ['tick'], 0.3, 'bình thản', 'lia sang Carl'),
 ('b1', 'S24.2', 'world', 'Carl (minh hoạ) nhận cùng loại séc tăng từ 1/1966.', 'Carl + hàng 10 thùng mọc ở "Carl".',
  {'carl': '@S24.2:Carl', 'january': '@S24.2:January'}, ['tick'], 0.35, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b2', 'S24.3', 'chart', '20 năm của Carl có giá tăng nhanh nhất: 6,38 %/năm.', 'nhãn giá; thanh giá (accent) mọc.',
  {'fastest': '@S24.3:fastest', 'year': '@S24.3:year'}, ['rise'], 0.5, 'nghiêm', '—'),
 ('b3', 'S24.4', 'chart', 'Séc đầu của Carl cũng mua 10 thùng.', 'ngoặc 10 chỗ; check +2% a year.',
  {'first': '@S24.4:first', 'check': '@S24.4:check'}, ['tick'], 0.5, 'hiểu', '—'),
 ('b4', 'S24.5', 'chart', 'Cả 20 kỷ niệm, séc của Carl mua ít hơn năm trước.', 'bộ đếm 1 → 20, hàng mờ dần tới 0,431.',
  {'every': '@S24.5:every', 'before': '@S24.5:before'}, ['nốt dữ liệu mỗi kỷ niệm'], 0.66, 'nặng', '—'),
 ('b5', 'S24.6', 'chart', 'Ruth lên lại những năm đầu; Carl thì không.', 'ô nhỏ đường của Ruth (năm 1–15 đậm); hàng Carl loé ở "never".',
  {'ruths': '@S24.6:Ruth', 'never': '@S24.6:never'}, ['tick'], 0.6, 'suy nghĩ', '—'),
 ('c0', 'S25.1', 'chart', 'Sau 20 lần tăng, séc của Carl mua 43,1 % séc đầu.', 'rising check: 43.1%.',
  {'forty': '@S25.1:forty-three'}, ['tick'], 0.85, 'nặng', 'lia'),
 ('c1', 'S25.2', 'chart', 'Séc đều trong quãng của ông: 29 %.', 'hàng séc đều của Carl tối tới 0,29.',
  {'level': '@S25.2:level', 'twenty': '@S25.2:twenty-nine'}, ['data'], 0.78, 'nặng', '—'),
 ('c2', 'S25.3', 'chart', 'Mức tăng có giúp, vẫn còn chưa tới một nửa.', 'vạch nửa hàng.',
  {'helped': '@S25.3:helped', 'half': '@S25.3:half'}, [], 0.7, 'trầm', '—'),
 ('c3', 'S26.1', 'chart', 'Các quãng bắt đầu thập niên 1960 điển hình kết thúc ở 44,3 %.', 'dải nhỏ 715 quãng, 1960s sáng.',
  {'alone': '@S26.1:alone', 'sixties': '@S26.1:1960s', 'forty': '@S26.1:forty-four'}, ['tick'], 0.58, 'hiểu', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('d0', 'S27.1', 'world', 'Edna (minh hoạ) bắt đầu 1/1949 — tháng cuối cùng mức tăng 2 % theo kịp.', 'Edna + hàng 10 thùng; đồ thị trước "kept".',
  {'edna': '@S27.1:Edna', 'last': '@S27.1:last', 'kept': '@S27.1:kept'}, ['tick'], 0.5, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('d1', 'S27.2', 'chart', '20 năm sau séc của bà vẫn mua ít nhất bằng séc đầu.', 'bộ đếm 1 → 20, trần 10.',
  {'twenty': '@S27.2:Twenty', 'check': '@S27.2:check', 'least': '@S27.2:least'}, ['data'], 0.52, 'nhẹ', '—'),
 ('d2', 'S27.3', 'chart', 'Bà thuộc nhóm nhỏ đầu; không ai sau bà có câu trả lời đó.', 'lùi máy; thanh 20 năm của Edna.',
  {'handful': '@S27.3:handful', 'answer': '@S27.3:answer'}, ['tick'], 0.54, 'suy nghĩ', 'lùi máy'),
 ('d3', 'S27.4', 'chart', '20 năm của bà kết thúc vài năm sau khi của Carl bắt đầu.', 'thanh của Carl; mốc năm.',
  {'her': '@S27.4:Her', 'carl': '@S27.4:Carl'}, ['tick'], 0.56, 'chú ý', '—'),
 ('d4', 'S27.5', 'chart', 'Cùng mấy năm giá: cuối quãng của bà (10 thùng sáng), đầu quãng của ông.', 'phần chồng tô accent; Edna 18 → 20 vẫn 10; Carl 1 → 3 mờ.',
  {'same': '@S27.5:same', 'end': '@S27.5:end', 'lit': '@S27.5:lit', 'start': '@S27.5:start'}, ['tick', 'data'], 0.62, 'hiểu', 'lia → Ruth'),
 ('e0', 'S28.1', 'chart', 'Ruth, 85 tuổi, vẫn đang mất dần.', 'Ruth · age 85.',
  {'ruth': '@S28.1:Ruth', 'eighty': '@S28.1:eighty-five', 'losing': '@S28.1:losing'}, [], 0.46, 'trầm', '—'),
 ('e1', 'S28.2', 'chart', 'Năm tới tháng 8 này giá tăng 3,4 %, hơn mức tăng 2 % của bà.', 'hai thanh một năm.',
  {'august': '@S28.2:August', 'three': '@S28.2:three', 'two': '@S28.2:two'}, ['tick'], 0.5, 'nghiêm', '—'),
 ('e2', 'S28.3', 'chart', 'Một năm lịch sử, không phải dự báo.', 'đối trọng.',
  {'history': '@S28.3:history'}, [], 0.46, 'thận trọng', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('f0', 'S29.1', 'world', 'Cùng mức tăng, cùng luật: Edna theo kịp, Ruth hụt muộn, Carl hụt xa.', 'ba séc cùng lớn lên; hàng mờ theo tên.',
  {'same': '@S29.1:Same', 'rule': '@S29.1:rule', 'edna': '@S29.1:Edna', 'ruth': '@S29.1:Ruth', 'carl': '@S29.1:Carl'}, ['tick', 'data'], 0.6, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('f1', 'S29.2', 'chart', 'Năm 20: Edna đủ 10, Ruth khoảng 9, Carl khoảng 4.', '10 · about 9 · about 4.',
  {'crates': '@S29.2:crates', 'full': '@S29.2:full', 'nine': '@S29.2:nine', 'four': '@S29.2:four'}, ['tick'], 0.68, 'hiểu', '—'),
 ('f2', 'S29.3', 'chart', 'Khác nhau là tháng bắt đầu và giá sau đó.', 'ba tháng bắt đầu sáng + loé.',
  {'month': '@S29.3:month'}, ['tick'], 0.52, 'suy nghĩ', '(hết)'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_pan24', 'pan', 'wRuth', 'wCarl', cue['b0']['best'], cue['b1']['carl'], 0.75, 'lời S24.2 chuyển sang Carl: lia qua hàng của Ruth sang chỗ hàng của Carl', 'whoosh_soft', {}),
    ('m_c24', 'mode', 'wCarl', 'cCarl', cue['b1']['january'], cue['b2']['fastest'], 1.2, 'lời S24.2–S24.3 đặt số (1966, 6.38%): số chỉ ở đồ thị (quy tắc 1)', 'whoosh_mode', {}),
    ('m_pan25', 'pan', 'cCarl', 'cCarl2', cue['c0']['forty'], cue['c1']['level'], 1.2, 'lời S25.2 "a level check, in his stretch": lia cho chỗ hàng séc đều của Carl', 'whoosh_soft', {}),
    ('m_w27', 'mode', 'cCarl2', 'wEdna', cue['c3']['forty'], cue['d0']['edna'], 1.0, 'lời S27.1 giới thiệu Edna: về thế giới, người và hàng thùng của bà (hiện sẵn trước tên)', 'whoosh_mode', {}),
    ('m_c27', 'mode', 'wEdna', 'cEdna', cue['d0']['last'], cue['d0']['kept'], 1.1, 'lời S27.1 đặt ngày (1949) + "kept up": số và so sánh chỉ ở đồ thị', 'whoosh_mode', {}),
    ('m_pull27', 'pull', 'cEdna', 'cBoth', cue['d2']['handful'], cue['d2']['answer'], 1.4, 'lời S27.4 đặt Edna cạnh Carl trên một trục thời gian: lùi máy', 'whoosh_soft', {}),
    ('m_pan28', 'pan', 'cBoth', 'cRuth', S.at('@S27.5$'), cue['e0']['ruth'], 0.9, 'lời S28.1 "And Ruth, at eighty-five": lia về Ruth', 'whoosh_soft', {}),
    ('m_w29', 'mode', 'cRuth', 'wThree', cue['e2']['history'], cue['f0']['same'], 1.0, 'lời S29.1 "Same raise, same rule": ba người cùng một thế giới', 'whoosh_mode', {}),
    ('m_c29', 'mode', 'wThree', 'cThree', cue['f0']['carl'] + 1.15, cue['f1']['crates'], 0.9, 'lời S29.2 đặt số thùng năm 20: số chỉ ở đồ thị (quy tắc 1)', 'whoosh_mode', {}),
])
M = {m['id']: m for m in moves}
Pr, Pc, Pe = K.P['ruth'], K.P['carl'], K.P['edna']
# S24.5: 20 kỷ niệm của Carl
yc = K.spread(cue['b4']['every'], cue['b4']['before'] + 0.35, 20)
ck, ev = K.step_row(yc, Pc[1:], ramp=0.2, v0=1.0)
# S25.2: hàng séc đều của Carl tối tới 0,290
cl, ev2 = K.step_row([cue['c1']['level'] + 0.3], [0.2901459854014599], ramp=1.6, v0=1.0)
# S27: Edna năm 1 → 20 (trần 10), chạy lại 18–20 ở "end"; Carl về khởi điểm ở "Carl" (S27.4) rồi năm 1 → 3 ở "start"
ye = K.spread(cue['d1']['twenty'], cue['d1']['least'] + 0.9, 20)
ek, ev3 = K.step_row(ye, Pe[1:], ramp=0.15, v0=1.0)
rep = K.spread(cue['d4']['end'], cue['d4']['end'] + 0.9, 3)
ek2, ev4 = K.step_row(rep, Pe[18:21], ramp=0.15, v0=Pe[17], notes=False)
cy = K.spread(cue['d4']['start'] + 0.05, cue['d4']['start'] + 1.0, 3)
ck27, ev5 = K.step_row(cy, Pc[1:4], ramp=0.18, v0=1.0)
# S29: mọi hàng về đầy + mọi séc về k = 0 trong cú chuyển về thế giới; ba séc cùng lớn lên ở "Same raise"; hàng mờ theo tên
reset = round(M['m_w29']['t0'] + 0.1, 3)
y29 = K.spread(cue['f0']['same'], cue['f0']['rule'] + 0.3, 20)
rk29, ev6 = K.step_row([cue['f0']['ruth']], [Pr[-1]], ramp=0.6, v0=1.0)
ct29 = K.spread(cue['f0']['carl'], cue['f0']['carl'] + 0.9, 4)
ck29, ev7 = K.step_row(ct29, [Pc[5], Pc[10], Pc[15], Pc[20]], ramp=0.22, v0=1.0)
shift = lambda kf, dt: [[round(t + dt, 3), v] for t, v in kf]
rows = {
    'ruth': [[0, Pr[-1]], [reset, Pr[-1]], [reset + 0.3, 1.0]] + [x for x in rk29[1:]],
    'carl': ck + [[round(cue['d3']['carl'] - 0.05, 3), Pc[-1]], [round(cue['d3']['carl'] + 0.5, 3), 1.0]] + ck27[1:]
            + [[reset, Pc[3]], [reset + 0.3, 1.0]] + ck29[1:],
    'carlLevel': cl,
    'edna': ek + ek2[1:] + [[reset, Pe[20]], [reset + 0.3, 1.0]],
}
for k, v in rows.items():
    assert all(b[0] >= a[0] for a, b in zip(v, v[1:])), (k, v)
cards = {
    'ruth': [[0, 20], [reset, 20], [reset + 0.3, 0]] + K.step_check(y29, ramp=0.06)[1:],
    'carl': K.step_check(yc, ramp=0.15) + [[round(cue['d3']['carl'] - 0.05, 3), 20], [round(cue['d3']['carl'] + 0.5, 3), 0]]
            + K.step_check(cy, ramp=0.12)[1:] + [[reset, 3], [reset + 0.3, 0]] + K.step_check(y29, ramp=0.06)[1:],
    'edna': K.step_check(ye) + [[reset, 20], [reset + 0.3, 0]] + K.step_check(y29, ramp=0.06)[1:],
}
for k, v in cards.items():
    assert all(b[0] >= a[0] for a, b in zip(v, v[1:])), (k, v)
ev += ev2 + ev3 + ev5 + ev6 + ev7
ev += [{'t': cue['b0']['ruth'], 'kind': 'tick', 'v': 0.4}, {'t': cue['b1']['carl'], 'kind': 'tick', 'v': 0.5}, {'t': cue['b2']['fastest'], 'kind': 'rise', 'dur': 4.0},
       {'t': cue['b3']['first'], 'kind': 'tick', 'v': 0.25}, {'t': round(cue['b5']['ruths'] - 0.17, 3), 'kind': 'tick', 'v': 0.55}, {'t': cue['b5']['never'], 'kind': 'tick', 'v': 0.3},
       {'t': cue['c0']['forty'], 'kind': 'tick', 'v': 0.4}, {'t': cue['c3']['sixties'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['d0']['edna'], 'kind': 'tick', 'v': 0.45}, {'t': cue['d0']['kept'], 'kind': 'tick', 'v': 0.5}, {'t': cue['d2']['answer'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['d3']['carl'], 'kind': 'tick', 'v': 0.5}, {'t': cue['d4']['same'], 'kind': 'tick', 'v': 0.55},
       {'t': cue['e1']['three'], 'kind': 'tick', 'v': 0.5}, {'t': cue['f0']['edna'], 'kind': 'tick', 'v': 0.5}, {'t': cue['f1']['full'], 'kind': 'tick', 'v': 0.6},
       {'t': cue['f1']['nine'], 'kind': 'tick', 'v': 0.5}, {'t': cue['f1']['four'], 'kind': 'tick', 'v': 0.35}, {'t': cue['f2']['month'], 'kind': 'tick', 'v': 0.4}]
K.finish(HERE, S, 'ep006 C4 · E = S24–S29 (Hồi 3: Carl, Edna, Ruth, ba tháng bắt đầu)', beats, moves, ev,
         {'rows': rows, 'cards': cards, 'years': {'carl': [round(t, 3) for t in yc], 'edna': [round(t, 3) for t in ye], 'edna_rep': [round(t, 3) for t in rep],
          'carl27': [round(t, 3) for t in cy]}, 'reset': reset, 'ruth_path': Pr, 'yoy': K.CLAIMS.get('cpi_yoy_latest_pct', {}).get('value') or YOY, 'price_growth': (1 + K.CLAIMS['raise_needed_all_20y_pct']['value'] / 100) ** 20},
         {'b2.fastest': 'prices: 6.38% a year, the fastest stretch', 'b1.january': 'Carl · ILLUSTRATIVE · Jan 1966', 'b3.first': 'first check: 10 crates',
          'b3.check': 'check: +2% a year', 'b4.before': 'less buying power on 20 of 20 anniversaries', 'b4.y20': 'year 20: about 4 of 10 crates',
          'b5.ruths': 'Ruth · ILLUSTRATIVE: back above in early years', 'c0.forty': 'rising check: 43.1%', 'c1.twenty': 'level check: 29.0%',
          'c2.half': 'less than half', 'c3.forty': '1960s starts, typical: 44.3%', 'd0.kept': 'kept up: the last start month that did',
          'd0.edna': 'Edna · ILLUSTRATIVE · Jan 1949', 'd1.check': 'check: +2% a year', 'd1.y20': 'year 20: all 10 still lit',
          'd3.carl': 'Carl · ILLUSTRATIVE · from Jan 1966', 'd4.same': 'same years of prices: her last, his first', 'd4.lit': 'all 10 crates still lit',
          'e0.eighty': 'Ruth · ILLUSTRATIVE · age 85', 'e1.three': '12 months to Aug 2026: prices +3.4%', 'e1.two': 'her raise: +2%',
          'e2.history': 'One year of history, not a forecast', 'f1.crates': 'crates at year 20 · same 2% raise', 'f1.full': '10', 'f1.nine': 'about 9',
          'f1.four': 'about 4', 'ax1949': '1949', 'ax1966': '1966', 'ax1969': '1969', 'ax1986': '1986'},
         ['b0.ruth', 'b1.carl', 'b2.fastest', 'b3.first', 'b3.check', 'b4.every', 'b4.before', 'b5.ruths', 'b5.never', 'c0.forty', 'c1.level', 'c1.twenty', 'c2.half',
          'c3.sixties', 'd0.edna', 'd0.kept', 'd1.twenty', 'd1.check', 'd2.answer', 'd3.carl', 'd4.same', 'd4.end', 'd4.start', 'e0.eighty', 'e1.three', 'e1.two',
          'e2.history', 'f0.edna', 'f0.ruth', 'f0.carl', 'f1.full', 'f1.nine', 'f1.four', 'f2.month'],
         accents=[cue['b4']['every'], cue['c0']['forty'], cue['f1']['four']], anchors=['S25.1'])
