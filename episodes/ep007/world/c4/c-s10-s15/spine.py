"""Tập 7 · C4 · ĐOẠN C = S10–S15 (Hồi 2 mở: lãi thật mọi tuần, phương pháp, khoảng chênh, một chồng cho mỗi tuần, chỗ của Tessa). Lời + giờ = timeline
của nhà máy (c4kit.Seg, 0 ký tự EL).  python3 episodes/ep007/world/c4/c-s10-s15/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, 'land')
Trục thời gian CHUNG của đoạn (trái → phải = Aug 1991 → Oct 2026, x ∈ [X0, X1]) cho mọi vật: đường lãi, lưới V1, cột khoảng chênh, hàng chồng.
B10 (S10, KEY-5): thế giới — Tessa, nhà, the stack (như cuối đoạn b); "one" = THANH ĐỨT NÉT phẳng (ink-muted) nổi sau nhà: "one assumed rate" (tên).
  → ĐỒ THỊ: "real" thẻ "15-year loan", "thirty-year" thẻ "30-year paid in 15" (V4 adapted); "every" hai đường lãi khảo sát thật (accent) vẽ trái →
  phải QUA thanh đứt nét: "every real week: 15-year and 30-year". "priced" → "thirty-three": lưới V1 1.833 ô (cột = năm) đầy dần theo thời gian
  (một nốt mỗi 4 năm); "both" = "$320,000 priced both ways each week", "thirty-three" = "1,833 weeks · Aug 1991 to Oct 2026"; "last" ô cuối sáng
  (ink, to ×1,6) = "Tessa's week = the last · ILLUSTRATIVE"; "earlier" sóng loé chạy ngược qua mọi ô (hỏi câu của cô ở mọi tuần trước).
B11 (S11): "far" lưới tắt, hai đường về; "above" tô khoảng giữa (accent); "gap" = khoảng đó RỜI hai đường, hạ xuống trục và phóng ×11 thành 1.833 cột
  khoảng chênh (accent) — "30-year minus 15-year rate"; "zero" ngoặc ở cột nhỏ nhất, "one" ngoặc ở cột lớn nhất: "gap: 0.2 point to 1.0 point".
B12 (S12): "averaged" vạch trung bình; "zero" "average gap: 0.57 point"; "least" cột ≥ nửa điểm sáng, còn lại tối: "at least half a point: about 2 in 3
  weeks"; "eighth" chấm Tessa ở đầu phải "Tessa: 0.67 point · ILLUSTRATIVE".
B13 (S13, KEY-6): → THẾ GIỚI: "every" mỗi cột khoảng chênh THÀNH một chồng (warn, cùng thang bó của the stack — cột tuần của Tessa cao đúng bằng 15 bó),
  sóng trái → phải; "rise" chồng loé. → ĐỒ THỊ: "six" chồng thấp nhất đánh dấu "smallest: $6,097 · Dec 2008".
B14 (S14): "twenty-nine" chồng cao nhất "tallest: $29,502 · Jan 2023".
B15 (S15, KEY-7): "median" vạch trung vị; "sixteen" "median week: $16,631"; "Fewer" vạch nét đứt từ đỉnh the stack qua cả hàng, tuần cao bằng/hơn sáng,
  còn lại tối: "one" "as tall or taller: fewer than 1 in 5 weeks"; "high" "Tessa's stack: $21,622 · ILLUSTRATIVE"; S15.4 về thế giới (Tessa gật)."""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c4kit as K
SV, G = K.SV, K.G
M = json.load(open(os.path.join(K.EP, 'out', 'model.json')))
Q = {k: v['value'] for k, v in M['quantities'].items()}
SE = M['series']
S = K.Seg(['S10', 'S11', 'S12', 'S13', 'S14', 'S15'])
B = [
 ('c0', 'S10.1', 'world', 'Nhiều video dùng một mức lãi giả định, coi trả sớm là thắng hiển nhiên.', 'thanh đứt nét phẳng sau nhà: "one assumed rate".',
  {'one': '@S10.1:one', 'assumed': '@S10.1:assumed'}, ['nốt dữ liệu', 'tick'], 0.3, 'nghi', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c1', 'S10.2', 'chart', 'Ở đây: khoản 15 năm thật cạnh khoản 30 năm trả trong 15, ở lãi thật mọi tuần từ 1991.', 'hai thẻ; hai đường lãi thật vẽ qua thanh đứt nét.',
  {'real': '@S10.2:real', 'thirty': '@S10.2:thirty-year', 'every': '@S10.2:every'}, ['tick', 'tick', 'rise'], 0.34, 'chắc', '—'),
 ('c2', 'S10.3', 'chart', 'Định giá cùng $320,000 cả hai cách ở mỗi tuần trong 1.833 tuần.', 'lưới V1 đầy dần; hai nhãn.',
  {'priced': '@S10.3:priced', 'both': '@S10.3:both', 'thirty': '@S10.3:thirty-three'}, ['nốt dữ liệu mỗi 4 năm', 'tick', 'tick'], 0.38, 'chắc', '—'),
 ('c3', 'S10.4', 'chart', 'Tuần của Tessa là tuần cuối; ở mọi tuần trước, hỏi câu của cô.', 'ô cuối sáng + nhãn; sóng loé chạy ngược qua lưới.',
  {'last': '@S10.4:last', 'earlier': '@S10.4:earlier'}, ['nốt dữ liệu sáng', 'rise'], 0.42, 'tò mò', '—'),
 ('c4', 'S11.1', 'chart', 'Tất cả quy về một thứ: lãi 30 năm cao hơn lãi 15 năm bao nhiêu.', 'lưới tắt, hai đường về; tô khoảng giữa.',
  {'far': '@S11.1:far', 'above': '@S11.1:above'}, ['tick', 'nốt dữ liệu'], 0.4, 'hiểu', '—'),
 ('c5', 'S11.2', 'chart', 'Từ 1991 khoảng chênh chạy từ 0,2 tới 1,0 điểm.', 'khoảng rời hai đường, phóng thành cột khoảng chênh; ngoặc nhỏ nhất / lớn nhất.',
  {'gap': '@S11.2:gap', 'zero': '@S11.2:zero', 'one': '@S11.2:one'}, ['rise', 'nốt dữ liệu thấp', 'nốt dữ liệu cao'], 0.46, 'ngạc nhiên', '—'),
 ('c6', 'S12.1', 'chart', 'Trung bình 0,57 điểm; ít nhất nửa điểm ở khoảng 2/3 số tuần.', 'vạch trung bình; cột ≥ nửa điểm sáng.',
  {'averaged': '@S12.1:averaged', 'zero': '@S12.1:zero', 'least': '@S12.1:least', 'two': '@S12.1:two'}, ['tick', 'nốt dữ liệu', 'tick'], 0.44, 'hiểu', '—'),
 ('c7', 'S12.2', 'chart', 'Khoảng chênh của Tessa hơi trên trung bình.', 'chấm Tessa ở đầu phải + nhãn.',
  {'eighth': '@S12.2:eighth', 'above': '@S12.2:above'}, ['nốt dữ liệu'], 0.46, 'hiểu', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('c8', 'S13.1', 'world', 'Mỗi tuần một chồng; chồng lên xuống theo khoảng chênh.', 'mỗi cột khoảng chênh thành một chồng (warn), sóng trái → phải.',
  {'every': '@S13.1:every', 'rise': '@S13.1:rise'}, ['rise', 'tick'], 0.5, 'hé lộ', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c9', 'S13.2', 'chart', 'Chồng nhỏ nhất: $6,097.', 'đánh dấu chồng thấp nhất + nhãn.',
  {'six': '@S13.2:six'}, ['nốt dữ liệu thấp'], 0.5, 'ngạc nhiên', '—'),
 ('d0', 'S14.1', 'chart', 'Chồng cao nhất: $29,502.', 'đánh dấu chồng cao nhất + nhãn.',
  {'twenty': '@S14.1:twenty-nine'}, ['nốt dữ liệu cao'], 0.54, 'ngạc nhiên', '—'),
 ('d1', 'S15.1', 'chart', 'Tuần điển hình (trung vị): $16,631.', 'vạch trung vị + nhãn.',
  {'median': '@S15.1:median', 'sixteen': '@S15.1:sixteen'}, ['tick', 'tick'], 0.56, 'hiểu', '—'),
 ('d2', 'S15.2', 'chart', 'Chưa tới 1/5 số tuần từ 1991 có giá cao thế (đỉnh hồi 2).', 'vạch từ đỉnh the stack qua hàng; tuần cao bằng/hơn sáng; nhãn.',
  {'fewer': '@S15.2:Fewer', 'one': '@S15.2:one', 'high': '@S15.2:high'}, ['rise', 'tick', 'nốt dữ liệu sáng'], 0.72, 'nghiêm', '—'),
 ('d3', 'S15.3', 'chart', 'Đường lui của Tessa đắt so với lịch sử.', 'the stack loé.',
  {'expensive': '@S15.3:expensive'}, ['tick'], 0.6, 'nghiêm', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('d4', 'S15.4', 'world', 'Khoản trả thấp đáng giá bao nhiêu trong tháng khó: phép phát lại không đo được.', 'Tessa cạnh nhà, gật.',
  {'worth': '@S15.4:worth', 'measure': '@S15.4:measure'}, ['tick'], 0.4, 'cân nhắc', '(hết đoạn)'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c10', 'mode', 'wC0', 'cC', cue['c0']['assumed'], cue['c1']['real'], 1.4,
     'lời S10.2–S10.3 đặt lãi thật + số tuần (số): đồ thị sau 5 s thế giới (quy tắc 7), trục thời gian chung chính diện', 'whoosh_mode', {'start': 5.0}),
    ('m_w13', 'mode', 'cC', 'wRow', cue['c7']['above'], cue['c8']['every'], 1.5,
     'lời S13.1 "stand a stack beside every week": về thế giới, nhìn dọc hàng từ chỗ Tessa để thấy chồng mọc', 'whoosh_mode', {}),
    ('m_c13', 'mode', 'wRow', 'cC', cue['c8']['rise'], cue['c9']['six'], 1.3, 'lời S13.2 đặt số chồng nhỏ nhất: đồ thị chính diện cả hàng', 'whoosh_mode', {}),
    ('m_w15', 'mode', 'cC', 'wEnd', cue['d3']['expensive'], cue['d4']['worth'], 1.4,
     'lời S15.4 nói về tháng khó của Tessa (không số): về thế giới, lại gần Tessa và nhà', 'whoosh_mode', {}),
])
MV = {m['id']: m for m in moves}
assert MV['m_c10']['t0'] >= 5.0
weeks, r30, r15, ext = SE['weeks'], np.array(SE['r30']), np.array(SE['r15']), np.array(SE['extra_total'])
sp = np.round(r30 - r15, 2)
i_spmin, i_spmax = int(np.argmin(sp)), int(np.argmax(sp))
i_min, i_max, N = int(np.argmin(ext)), int(np.argmax(ext)), len(weeks)
assert weeks[i_min] == Q['extra_total_min_week'] and weeks[i_max] == Q['extra_total_max_week'] and ext[i_min] == Q['extra_total_min'] and ext[-1] == Q['extra_vs15_total_now']
assert abs(sp.min() - Q['spread_min']) < 1e-9 and abs(sp.max() - Q['spread_max']) < 1e-9 and abs(sp[-1] - Q['spread_now']) < 1e-9
assert abs((ext >= Q['extra_vs15_total_now']).mean() - Q['share_extra_ge_now']) < 0.001 and abs((sp >= 0.5).mean() - Q['share_spread_ge_050']) < 0.006
# lưới V1 đầy theo thời gian: 9 nhịp (mỗi 4 năm một nốt: cuối 1994, 1998, … , tuần cuối), từ "priced" tới trước "thirty-three"
ends = [max(i for i, w in enumerate(weeks) if int(w[:4]) <= y) + 1 for y in range(1994, 2026, 4)] + [N]
ft = K.spread(cue['c2']['priced'] + 0.25, cue['c2']['thirty'] - 0.3, len(ends))
fill, ev = K.steps(ft, ends, ramp=(ft[1] - ft[0]) * 0.95, v0=0, pitch=lambda v: 0.25 + 0.5 * v / N)
ev += [{'t': cue['c0']['one'], 'kind': 'data', 'v': 0.5}, {'t': cue['c0']['assumed'], 'kind': 'tick', 'v': 0.3},
       {'t': cue['c1']['real'], 'kind': 'tick', 'v': 0.4}, {'t': cue['c1']['thirty'], 'kind': 'tick', 'v': 0.45}, {'t': cue['c1']['every'], 'kind': 'rise', 'dur': 1.5},
       {'t': cue['c2']['both'], 'kind': 'tick', 'v': 0.4}, {'t': cue['c2']['thirty'], 'kind': 'tick', 'v': 0.5},
       {'t': cue['c3']['last'], 'kind': 'data', 'v': 0.9, 'over': True}, {'t': cue['c3']['earlier'], 'kind': 'rise', 'dur': 1.6},
       {'t': cue['c4']['far'], 'kind': 'tick', 'v': 0.35}, {'t': cue['c4']['above'], 'kind': 'data', 'v': round(float(sp[-1]), 3)},
       {'t': cue['c5']['gap'], 'kind': 'rise', 'dur': 1.0}, {'t': cue['c5']['zero'], 'kind': 'data', 'v': 0.2}, {'t': cue['c5']['one'], 'kind': 'data', 'v': 1.0},
       {'t': cue['c6']['zero'], 'kind': 'tick', 'v': 0.45}, {'t': cue['c6']['least'], 'kind': 'data', 'v': 0.5}, {'t': cue['c6']['two'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['c7']['eighth'], 'kind': 'data', 'v': round(float(sp[-1]), 3), 'over': True},
       {'t': cue['c8']['every'], 'kind': 'rise', 'dur': 1.6}, {'t': cue['c8']['rise'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['c9']['six'], 'kind': 'data', 'v': round(float(ext[i_min] / ext[i_max]), 3)}, {'t': cue['d0']['twenty'], 'kind': 'data', 'v': 1.0},
       {'t': cue['d1']['median'], 'kind': 'tick', 'v': 0.35}, {'t': cue['d1']['sixteen'], 'kind': 'tick', 'v': 0.5},
       {'t': cue['d2']['fewer'], 'kind': 'rise', 'dur': 0.8}, {'t': cue['d2']['one'], 'kind': 'tick', 'v': 0.55},
       {'t': cue['d2']['high'], 'kind': 'data', 'v': round(float(ext[-1] / ext[i_max]), 3), 'over': True},
       {'t': cue['d3']['expensive'], 'kind': 'tick', 'v': 0.45}, {'t': cue['d4']['measure'], 'kind': 'tick', 'v': 0.3}]
X = {'house': -3.3, 'stack': -1.6, 'x0': -0.85, 'x1': 9.75, 'cards': [0.9, 4.7]}
xw = lambda i: X['x0'] + (i + 0.5) * (X['x1'] - X['x0']) / N
gestures = [{'t': cue['c0']['one'], 'kind': 'lean', 'to': 2.0, 'hold': 1.2},                  # thanh giả định hiện (thế giới)
            {'t': cue['c1']['thirty'], 'kind': 'arm', 'to': X['cards'][1], 'hold': 1.2},       # thẻ 30 năm (đồ thị)
            {'t': cue['c1']['every'], 'kind': 'lean', 'to': X['x1'], 'hold': 1.4},             # hai đường lãi vẽ
            {'t': cue['c3']['last'], 'kind': 'arm', 'to': X['x1'], 'hold': 1.6},               # ô của cô sáng
            {'t': cue['c5']['gap'], 'kind': 'lean', 'to': 4.0, 'hold': 1.2},                   # khoảng chênh hạ xuống
            {'t': cue['c7']['eighth'], 'kind': 'arm', 'to': X['x1'], 'hold': 1.4},             # chấm của cô
            {'t': cue['c8']['every'], 'kind': 'arm', 'to': X['x1'], 'hold': 1.8},              # chồng mọc (thế giới)
            {'t': cue['d0']['twenty'], 'kind': 'lean', 'to': xw(i_max), 'hold': 1.2},
            {'t': cue['d2']['high'], 'kind': 'arm', 'to': X['stack'], 'hold': 1.6},            # the stack của cô cao hơn gần hết
            {'t': cue['d4']['worth'], 'kind': 'nod', 'hold': 0.6}]
K.finish(HERE, S, 'ep007 C4 · C = S10–S15 (Hồi 2: lãi thật mọi tuần, lưới V1, khoảng chênh, hàng chồng theo tuần, chỗ của Tessa)', beats, moves, ev,
         {'x': X, 'gestures': gestures, 'fill': fill, 'weeks': weeks, 'r30': SE['r30'], 'r15': SE['r15'], 'extra': SE['extra_total'],
          'i': {'spmin': i_spmin, 'spmax': i_spmax, 'min': i_min, 'max': i_max}, 'assumed_rate': round(float(np.median(r30)), 2),
          'spread_mean': Q['spread_mean'], 'median': Q['extra_total_median']},
         {'c0.assumed': 'one assumed rate', 'c1.real': '15-year loan', 'c1.thirty': '30-year paid in 15', 'c1.every': 'every real week: 15-year and 30-year',
          'c2.both': '$320,000 priced both ways each week', 'c2.thirty': '1,833 weeks · Aug 1991 to Oct 2026', 'c3.last': "Tessa's week = the last · ILLUSTRATIVE",
          'c5.gap': '30-year minus 15-year rate', 'c5.one': 'gap: 0.2 point to 1.0 point', 'c6.zero': 'average gap: 0.57 point',
          'c6.two': 'at least half a point: about 2 in 3 weeks', 'c7.eighth': 'Tessa: 0.67 point · ILLUSTRATIVE', 'c9.six': 'smallest: $6,097 · Dec 2008',
          'd0.twenty': 'tallest: $29,502 · Jan 2023', 'd1.sixteen': 'median week: $16,631', 'd2.one': 'as tall or taller: fewer than 1 in 5 weeks',
          'd2.high': "Tessa's stack: $21,622 · ILLUSTRATIVE"},
         ['c0.one', 'c0.assumed', 'c1.real', 'c1.thirty', 'c1.every', 'c2.priced', 'c2.both', 'c2.thirty', 'c3.last', 'c3.earlier', 'c4.far', 'c4.above',
          'c5.gap', 'c5.zero', 'c5.one', 'c6.averaged', 'c6.zero', 'c6.least', 'c6.two', 'c7.eighth', 'c8.every', 'c8.rise', 'c9.six', 'd0.twenty',
          'd1.median', 'd1.sixteen', 'd2.fewer', 'd2.one', 'd2.high', 'd3.expensive'],
         accents=[cue['d2']['fewer']])
