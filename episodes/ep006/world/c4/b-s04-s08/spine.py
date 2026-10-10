"""Tập 6 · C4 · ĐOẠN B = S04–S08 (Hồi 1: hai séc, sức mua, hai mươi năm của Ruth). Lời + giờ = timeline của nhà máy (c4kit.Seg, 0 ký tự EL).
  python3 episodes/ep006/world/c4/b-s04-s08/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3)
B04 (S04): Ruth đứng giữa hai tấm séc (W10b): séc ĐỀU cao hơn (ink-muted, không đổi) ở "bigger", séc tăng thấp hơn ở "smaller", "rises" = séc bước lên
rồi về cỡ đầu; → ĐỒ THỊ: nhãn hai séc, "starts" = khoảng chênh cỡ đầu tô xám + "?", "model" = "how much smaller: not modeled"; "dollars" =
"dollars paid out: not compared"; lùi máy, "each" = mỗi séc trượt về đầu hàng 10 thùng của nó (sức mua so với séc đầu CỦA NÓ).
B05 (S05): Ruth sang cạnh séc tăng (đẩy máy), séc đều + hàng của nó mờ; "Ruth · Aug 2006, age 65"; "prices go up, her check goes up".
B06 (S06): lia sang hai thanh cùng gốc: séc (ink) +48,6 % ở "forty", giá (accent) +64,3 % ở "sixty" — vượt séc; "national" = nhãn chỉ số.
B07 (S07, port C3 s07-ruth đã duyệt): thế giới, séc lớn lên 20 kỷ niệm, hàng tối tới 0,904 ("less"); → đồ thị: 10 thùng / about 9 in 10 (90.4%).
B08 (S08): lùi máy thấy cả hai hàng: hàng của séc đều tối theo đường mức của Ruth tới 0,609 ở "six" ("about 6 in 10 (60.9%)"); "own" = đối trọng
"Each check vs its own first check · not dollars"; "bigger" = hai cỡ đầu + "?" "starting sizes: not modeled"."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c4kit as K
SV = K.SV
import json
RAW = json.load(open(os.path.join(K.EP, 'out', 'model.json')))['raw']
S = K.Seg(['S04', 'S05', 'S06', 'S07', 'S08'])
B = [
 ('b0', 'S04.1', 'world', 'Niên kim trả séc lớn không đổi, hoặc séc nhỏ tăng đều mỗi năm.', 'Ruth giữa hai séc: đều (cao, xám), tăng (thấp, bước lên).',
  {'bigger': '@S04.1:bigger', 'never': '@S04.1:never', 'smaller': '@S04.1:smaller', 'rises': '@S04.1:rises', 'year': '@S04.1:year'}, ['tick', 'rise'], 0.25, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b1', 'S04.2', 'chart', 'Nhỏ hơn bao nhiêu tuỳ công ty; video không mô hình hoá.', 'khoảng chênh cỡ đầu tô xám + "?"; "not modeled".',
  {'smaller': '@S04.2:smaller', 'starts': '@S04.2:starts', 'model': '@S04.2:model'}, ['tick'], 0.25, 'thận trọng', '—'),
 ('b2', 'S04.3', 'chart', 'Nên không so tiền hai séc trả cả đời.', '"dollars paid out: not compared".',
  {'dollars': '@S04.3:dollars'}, [], 0.22, 'thận trọng', 'lùi máy'),
 ('b3', 'S04.4', 'chart', 'Đo sức mua: mỗi séc mua được gì so với séc đầu CỦA NÓ.', 'mỗi séc về đầu hàng 10 thùng của nó.',
  {'buying': '@S04.4:buying', 'each': '@S04.4:each', 'own': '@S04.4:own'}, ['rise'], 0.3, 'hiểu', 'đẩy máy'),
 ('b4', 'S05.1', 'chart', 'Ruth nhận séc tăng đầu tiên tháng 8/2006.', 'Ruth sang cạnh séc tăng; séc đều mờ; nhãn ngày + tuổi.',
  {'took': '@S05.1:took', 'august': '@S05.1:August'}, ['tick'], 0.3, 'ấm', '—'),
 ('b5', 'S05.2', 'chart', 'Lý lẽ: giá lên thì séc cũng lên.', 'nhãn "prices go up, her check goes up".',
  {'prices': '@S05.2:prices', 'check': '@S05.2:check'}, [], 0.3, 'tự tin', '—'),
 ('b6', 'S05.3', 'chart', 'Tăng 2 %/năm cộng lại thành bao nhiêu?', 'nhãn +2% a year trên séc.',
  {'two': '@S05.3:two'}, ['tick'], 0.35, 'tò mò', 'lia → hai thanh'),
 ('b7', 'S06.1', 'chart', '20 lần tăng: séc lớn hơn 48,6 %.', 'thanh séc mọc tới +48.6%.',
  {'twenty': '@S06.1:twenty', 'forty': '@S06.1:forty-eight'}, ['rise'], 0.35, 'ổn', '—'),
 ('b8', 'S06.2', 'chart', 'Trong 20 năm của Ruth, chỉ số giá tăng 64,3 %.', 'thanh giá mọc qua thanh séc tới +64.3%.',
  {'ruths': '@S06.2:Ruth', 'sixty': '@S06.2:sixty-four'}, ['rise'], 0.45, 'lo', '—'),
 ('b9', 'S06.3', 'chart', 'Chỉ số là trung bình quốc gia, không phải giỏ riêng của ai.', 'nhãn "a national average · not one person\'s basket".',
  {'national': '@S06.3:national', 'own': '@S06.3:not'}, [], 0.35, 'thận trọng', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('c0', 'S07.1', 'world', 'Séc lớn lên nhưng giá lên nhiều hơn: hôm nay mua ít hơn séc đầu.', 'séc bước lên 20 kỷ niệm, hàng tối tới 0,904 ("less").',
  {'grew': '@S07.1:grew', 'less': '@S07.1:less'}, ['nốt dữ liệu mỗi kỷ niệm'], 0.4, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c1', 'S07.2', 'chart', 'Tính bằng thùng: séc đầu mua 10, hôm nay khoảng 9.', 'ngoặc 10 chỗ; ngoặc phần sáng + about 9 in 10 (90.4%).',
  {'check': '@S07.2:check', 'ten': '@S07.2:ten', 'nine': '@S07.2:nine'}, ['tick'], 0.46, 'hiểu', 'lùi máy'),
 ('c2', 'S08.1', 'chart', 'Séc đều (so với séc đầu của nó) hôm nay mua khoảng 6/10.', 'hàng của séc đều tối tới 0,609 ở "six".',
  {'first': '@S08.1:first', 'level': '@S08.1:level', 'six': '@S08.1:six'}, ['nốt dữ liệu'], 0.42, 'nặng', '—'),
 ('c3', 'S08.2', 'chart', 'Mức tăng làm chậm phần mất.', 'hàng của séc tăng loé.',
  {'slowed': '@S08.2:slowed'}, [], 0.4, 'hiểu', '—'),
 ('c4', 'S08.3', 'chart', 'Mỗi séc so với khởi điểm của nó; séc đều khởi điểm lớn hơn, không mô hình hoá.', 'đối trọng; hai cỡ đầu + "?".',
  {'own': '@S08.3:own', 'bigger': '@S08.3:bigger', 'model': '@S08.3:model'}, [], 0.36, 'thận trọng', '(hết)'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c1', 'mode', 'wFig0', 'cCards', cue['b0']['year'], S.at('@S04.2'), 1.0, 'lời S04.2 so cỡ đầu hai séc: so sánh chỉ ở đồ thị chính diện', 'whoosh_mode', {}),
    ('m_pull', 'pull', 'cCards', 'cCols', cue['b2']['dollars'], cue['b3']['buying'], 1.2, 'lời S04.4 "each check … its own first check": lùi máy cho chỗ hai hàng thùng', 'whoosh_soft', {}),
    ('m_push', 'push', 'cCols', 'cRise', S.at('@S04.4$'), cue['b4']['took'], 1.1, 'lời S05.1 "Ruth took her first rising check": đẩy vào séc tăng của bà', 'whoosh_push', {}),
    ('m_pan', 'pan', 'cRise', 'cBars', S.at('@S05.3$'), cue['b7']['twenty'], 1.1, 'lời S06 so hai mức tăng (séc, giá) trên cùng gốc: lia sang hai thanh', 'whoosh_soft', {}),
    ('m_w', 'mode', 'cBars', 'wRise', cue['b9']['own'], cue['c0']['grew'], 1.2, 'lời S07.1 "her check grew … buys less": về séc và hàng thùng của bà (thế giới)', 'whoosh_mode', {'late': True}),
    ('m_c7', 'mode', 'wRise', 'cRise2', cue['c0']['less'], S.at('@S07.2:first'), 1.2, 'lời S07.2 đặt số (10, about 9): số chỉ ở đồ thị (quy tắc 1)', 'whoosh_mode', {}),
    ('m_pull8', 'pull', 'cRise2', 'cCols', cue['c1']['nine'], S.at('@S08.1'), 1.0, 'lời S08.1 đưa séc đều trở lại: lùi máy thấy cả hai hàng', 'whoosh_soft', {}),
])
Pr, Lr = K.P['ruth'], [v / 100 for v in K.GRID['ruth_level']]
yrs7 = K.spread(cue['c0']['grew'], cue['c0']['less'] + 0.3, 20)               # S07.1: kỷ niệm 1 … 20 từ "grew", năm 16 (cú rơi) quanh "less"
rk, ev = K.step_row(yrs7, Pr[1:], ramp=0.14, v0=1.0)
yrs8 = K.spread(cue['c2']['level'], cue['c2']['six'] - 0.25, 20)              # S08.1: hàng của séc đều tối theo đường mức của Ruth tới 0,609
lk, ev2 = K.step_row(yrs8, Lr[1:], ramp=0.12, v0=1.0)
grow4 = K.spread(cue['b0']['rises'], cue['b0']['year'], 10)                   # S04.1 "rises": séc bước lên (minh hoạ phép tăng) rồi về cỡ đầu ở "starts"
# vòng sửa 2 (B04): bước lên tới k = 6 (×1,13, nhích nhẹ) — séc tăng vẫn rõ nhỏ hơn séc đều khi so cỡ đầu
ev += ev2 + [{'t': cue['b0']['bigger'], 'kind': 'tick', 'v': 0.35}, {'t': cue['b0']['rises'], 'kind': 'rise', 'dur': 1.4},
             {'t': cue['b1']['starts'], 'kind': 'tick', 'v': 0.4}, {'t': cue['b3']['each'], 'kind': 'rise', 'dur': 0.8},
             {'t': cue['b4']['august'], 'kind': 'tick', 'v': 0.45}, {'t': cue['b6']['two'], 'kind': 'tick', 'v': 0.5},
             {'t': cue['b7']['forty'], 'kind': 'data', 'v': 0.75}, {'t': cue['b8']['sixty'], 'kind': 'data', 'v': 0.95},
             {'t': cue['c1']['ten'], 'kind': 'tick', 'v': 0.45}, {'t': cue['c1']['nine'], 'kind': 'tick', 'v': 0.6}]
K.finish(HERE, S, 'ep006 C4 · B = S04–S08 (Hồi 1: hai séc, sức mua)', beats, moves, ev,
         {'rows': {'rise': rk, 'level': lk}, 'cards': {'rise': [[0, 0]] + [[round(t, 3), round((i + 1) * 0.6, 1)] for i, t in enumerate(grow4)] + [[round(cue['b1']['starts'] - 0.3, 3), 6], [round(cue['b1']['starts'], 3), 0]]
                                                    + K.step_check(yrs7, ramp=0.1)[1:]},
          'years7': [round(t, 3) for t in yrs7], 'years8': [round(t, 3) for t in yrs8],
          'ruth_path': Pr, 'growth': {'check': RAW['two_pct_growth_20y_pct'] / 100, 'prices': RAW['latest_window_price_rise_pct'] / 100}},
         {'b0.never': 'level check: never changes', 'b0.rises': 'rising check: +2% a year', 'b1.model': 'how much smaller: not modeled',
          'b2.dollars': 'dollars paid out: not compared', 'b3.buying': 'measured: buying power vs its own first check',
          'b4.august': 'Ruth · Aug 2006, age 65', 'b5.prices': 'prices go up, her check goes up', 'b6.two': 'check: +2% a year',
          'b7.forty': '20 raises of 2%: +48.6%', 'b8.sixty': 'prices: +64.3%', 'b8.ruths': 'Aug 2006 → Aug 2026', 'b9.national': 'consumer prices: a national average',
          'b9.own': "not one retiree's own basket", 'c1.ten': 'first check: 10 crates', 'c1.nine': 'today: about 9 in 10 crates (90.4%)',
          'c2.rising': 'rising check: about 9 in 10 (90.4%)', 'c2.first': 'its own first check: 10 crates',
          'c2.six': 'level check today: about 6 in 10 (60.9%)', 'c4.own': 'Each check vs its own first check · not dollars',
          'c4.model': 'starting sizes: not modeled'},
         ['b0.bigger', 'b0.smaller', 'b0.rises', 'b1.starts', 'b1.model', 'b2.dollars', 'b3.each', 'b4.took', 'b4.august', 'b5.prices', 'b6.two', 'b7.forty',
          'b8.sixty', 'b9.national', 'c0.grew', 'c0.less', 'c1.ten', 'c1.nine', 'c2.level', 'c2.six', 'c3.slowed', 'c4.own', 'c4.bigger', 'c4.model'],
         accents=[cue['b8']['sixty'], cue['c1']['nine']], inputs=['episodes/ep006/world/c4/checklook.js'])
