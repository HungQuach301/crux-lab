"""Tập 7 · C4 · ĐOẠN D = S16–S20 (Hồi 2: theo thập kỷ — lãi thấp hơn mà đường lui đắt hơn; khoảng chênh giải thích). Lời + giờ = timeline của nhà máy.
  python3 episodes/ep007/world/c4/d-s16-s20/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, lặng neo S18.1, 'land')
Tiếp hàng chồng theo tuần của đoạn c (cùng trục, cùng thang bó; the stack cạnh nhà). Trước mỗi nhóm thập kỷ một CHỒNG ĐIỂN HÌNH (W2, bó của the
stack, cao = trung vị extra_total của thập kỷ); đường lãi 30 năm (accent) chạy qua hàng.
B16 (S16): thế giới — "decade" hàng TÁCH thành bốn nhóm (1991–1999 · 2000s · 2010s · 2020s). → ĐỒ THỊ: "typical" nhóm 1990s sáng, chồng điển hình
  dâng; "fifteen" = "1991 to 1999: rate near 7.73%" / "typical stack $15,118" (+ thẻ "1991 to 1999 · $15,118" trên chồng, giữ tới hết).
B17 (S17): "2000s" nhóm 2000s sáng, chồng dâng (≈ bằng); "fourteen" = "2000s: rate near 6.18%" / "typical stack $14,210".
B18 (S18, KEY-8, số neo — lặng 0,75 s trong đuôi S17): "2010s" nhóm sáng, chồng dâng CAO HƠN; "far" đoạn đường lãi 2010s loé (thấp hẳn); "more" vạch
  nét đứt từ đỉnh chồng 1990s qua tới 2010s (chồng 2010s vượt vạch); "twenty" = "2010s: rate near 4.03%" / "typical stack $20,374".
B19 (S19): "gap" bốn ngoặc V6 (accent) cạnh bốn chồng, cao = khoảng chênh trung vị của thập kỷ × cùng thang cột khoảng chênh của đoạn c; "seven"
  ngoặc 2010s + 2020s "0.72 point" "0.70 point", "four" ngoặc 1990s + 2000s "0.46 point" "0.45 point" — ngoặc khớp chồng, không khớp đường lãi;
  "lower" đường lãi loé; "wider" ngoặc + chồng loé cùng nhau.
B20 (S20): "twenty" nhóm 2020s sáng, chồng 2020s; "twenty-one" = "2020s: typical stack $21,345"; "Tessa's" vạch nét đứt từ đỉnh the stack sang chồng
  2020s (gần ngang) + "Tessa's stack · ILLUSTRATIVE"; "history" dòng góc "history, not a forecast" gạch chân; "moved" ngoặc rung; về thế giới."""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c4kit as K
SV, G = K.SV, K.G
M = json.load(open(os.path.join(K.EP, 'out', 'model.json')))
Q = {k: v['value'] for k, v in M['quantities'].items()}
SE = M['series']
S = K.Seg(['S16', 'S17', 'S18', 'S19', 'S20'])
B = [
 ('e0', 'S16.1', 'world', 'Xếp các tuần theo thập kỷ: kết quả không như người ta nghĩ.', 'hàng chồng tách thành bốn nhóm.',
  {'decade': '@S16.1:decade'}, ['rise'], 0.4, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('e1', 'S16.2', 'chart', 'Thập niên 1990: đường lui điển hình $15,118.', 'nhóm 1990s sáng, chồng điển hình dâng; nhãn.',
  {'typical': '@S16.2:typical', 'fifteen': '@S16.2:fifteen'}, ['rise', 'nốt dữ liệu'], 0.42, 'bình thản', '—'),
 ('e2', 'S17.1', 'chart', 'Thập niên 2000, lãi thấp hơn: gần như bằng, $14,210.', 'nhóm 2000s sáng, chồng dâng; nhãn.',
  {'y2000s': '@S17.1:2000s', 'fourteen': '@S17.1:fourteen'}, ['rise', 'nốt dữ liệu'], 0.42, 'bình thản', '(số neo S18.1: lặng 0,75 s)'),
 ('e3', 'S18.1', 'chart', 'Thập niên 2010, lãi thấp hẳn mà đường lui đắt hơn: $20,374.', 'đoạn đường lãi 2010s loé thấp; chồng 2010s vượt vạch đỉnh 1990s; nhãn.',
  {'y2010s': '@S18.1:2010s', 'far': '@S18.1:far', 'more': '@S18.1:more', 'twenty': '@S18.1:twenty'}, ['rise', 'nốt dữ liệu', 'tick', 'nốt dữ liệu'], 0.62, 'ngạc nhiên', '—'),
 ('e4', 'S19.1', 'chart', 'Lý do là khoảng chênh: ~0,7 điểm ở 2010s, 2020s so với ~0,45 ở 1990s, 2000s.', 'bốn ngoặc V6 cạnh bốn chồng + nhãn.',
  {'gap': '@S19.1:gap', 'seven': '@S19.1:seven', 'four': '@S19.1:four'}, ['tick', 'nốt dữ liệu ×2', 'nốt dữ liệu ×2'], 0.56, 'hiểu', '—'),
 ('e5', 'S19.2', 'chart', 'Lãi thấp không có nghĩa đường lui rẻ; chênh rộng thì đường lui đắt.', 'đường lãi loé; ngoặc + chồng loé cùng nhau.',
  {'lower': '@S19.2:lower', 'wider': '@S19.2:wider'}, ['tick', 'nốt dữ liệu'], 0.6, 'hiểu', '—'),
 ('e6', 'S20.1', 'chart', 'Từ 2020 tuần điển hình: $21,345, gần bằng chồng của Tessa.', 'nhóm 2020s; vạch từ đỉnh the stack; hai nhãn.',
  {'twenty': '@S20.1:twenty', 'one': '@S20.1:twenty-one', 'tessa': '@S20.1:Tessa'}, ['tick', 'nốt dữ liệu', 'tick'], 0.5, 'hiểu', '—'),
 ('e7', 'S20.2', 'chart', 'Đó là lịch sử, không phải dự báo: khoảng chênh từng thay đổi.', 'dòng góc gạch chân; ngoặc rung.',
  {'history': '@S20.2:history', 'moved': '@S20.2:moved'}, ['tick', 'tick'], 0.36, 'thận trọng', 'CHUYỂN CHẾ ĐỘ → thế giới'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c16', 'mode', 'wD0', 'cD', cue['e0']['decade'], cue['e1']['typical'], 0.78,
     'lời S16.2–S20.1 đặt lãi và giá theo thập kỷ (số): đồ thị chính diện cả hàng, sau 5 s thế giới (quy tắc 7)', 'whoosh_mode', {'start': 5.0}),
    ('m_w20', 'mode', 'cD', 'wEnd', cue['e7']['moved'], S.at('@S20.2$'), 1.4,
     'lời S20.2 "nothing here says where it goes" (không số): về thế giới, Tessa và the stack cạnh nhà trước khi cô tự thử khoản vay', 'whoosh_mode', {}),
])
MV = {m['id']: m for m in moves}
assert MV['m_c16']['t0'] >= 5.0
weeks = SE['weeks']
ER = M['eras']
rng = [[weeks.index(e['from']) if e['from'] in weeks else next(i for i, w in enumerate(weeks) if w >= e['from']),
        max(i for i, w in enumerate(weeks) if w <= e['to']) + 1] for e in ER]
assert rng[0][0] == 0 and rng[-1][1] == len(weeks) and all(a[1] == b[0] for a, b in zip(rng, rng[1:]))
for k, e in enumerate(['era1991', 'era2000', 'era2010', 'era2020']):
    assert ER[k]['median_extra_total'] == Q[e + '_median_extra_total'] and abs(ER[k]['median_spread'] - Q[e + '_median_spread']) < 1e-9
med = [ER[k]['median_extra_total'] for k in range(4)]
spd = [ER[k]['median_spread'] for k in range(4)]
# chồng điển hình dâng ở từ khoá (1,1 s); một nốt khi đủ cao (cao độ = giá)
up = [cue['e1']['typical'], cue['e2']['y2000s'], cue['e3']['y2010s'], cue['e6']['twenty']]
pitch = lambda v: round(0.2 + 0.6 * v / 22000, 3)
ev = [{'t': cue['e0']['decade'], 'kind': 'rise', 'dur': 1.0}]
for k in range(4):
    ev += [{'t': round(up[k], 3), 'kind': 'rise', 'dur': 1.1}, {'t': round(up[k] + 1.1, 3), 'kind': 'data', 'v': pitch(med[k])}]
ev += [{'t': cue['e1']['fifteen'], 'kind': 'tick', 'v': 0.4}, {'t': cue['e2']['fourteen'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['e3']['far'], 'kind': 'data', 'v': round(Q['era2010_median_r30'] / 10, 3)}, {'t': cue['e3']['more'], 'kind': 'tick', 'v': 0.5},
       {'t': cue['e3']['twenty'], 'kind': 'tick', 'v': 0.55},
       {'t': cue['e4']['gap'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['e4']['seven'], 'kind': 'data', 'v': spd[2]}, {'t': round(cue['e4']['seven'] + 0.25, 3), 'kind': 'data', 'v': spd[3]},
       {'t': cue['e4']['four'], 'kind': 'data', 'v': spd[0]}, {'t': round(cue['e4']['four'] + 0.25, 3), 'kind': 'data', 'v': spd[1]},
       {'t': cue['e5']['lower'], 'kind': 'tick', 'v': 0.35}, {'t': cue['e5']['wider'], 'kind': 'data', 'v': 0.72},
       {'t': cue['e6']['one'], 'kind': 'tick', 'v': 0.5}, {'t': cue['e6']['tessa'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['e7']['history'], 'kind': 'tick', 'v': 0.3}, {'t': cue['e7']['moved'], 'kind': 'tick', 'v': 0.35}]
X = {'house': -3.3, 'stack': -1.6, 'x0': -0.85, 'x1': 9.75, 'split': 0.22, 'zs': 1.2}
N = len(weeks)
xc = lambda k: X['x0'] + (rng[k][0] + rng[k][1]) / 2 / N * (X['x1'] - X['x0']) + (k - 1.5) * X['split']
gestures = [{'t': cue['e0']['decade'], 'kind': 'lean', 'to': 4.0, 'hold': 1.2},
            {'t': cue['e1']['fifteen'], 'kind': 'arm', 'to': xc(0), 'hold': 1.2},
            {'t': cue['e3']['more'], 'kind': 'lean', 'to': xc(2), 'hold': 1.4},
            {'t': cue['e4']['seven'], 'kind': 'arm', 'to': xc(2), 'hold': 1.4},
            {'t': cue['e6']['tessa'], 'kind': 'arm', 'to': X['stack'], 'hold': 1.6},
            {'t': cue['e7']['history'], 'kind': 'nod', 'hold': 0.5}]
K.finish(HERE, S, 'ep007 C4 · D = S16–S20 (Hồi 2: theo thập kỷ, khoảng chênh giải thích, 2020s cạnh Tessa)', beats, moves, ev,
         {'x': X, 'gestures': gestures, 'extra': SE['extra_total'], 'r30': SE['r30'], 'weeks': weeks, 'rng': rng, 'med': med, 'spd': spd, 'up': [round(t, 3) for t in up],
          'r30_med': [ER[k]['median_r30'] for k in range(4)], 'spread_now': Q['spread_now']},
         {'e1.fifteen': '1991 to 1999: rate near 7.73%', 'e2.fourteen': '2000s: rate near 6.18%', 'e3.twenty': '2010s: rate near 4.03%',
          'e4.seven': '0.72 point', 'e4.four': '0.46 point', 'e6.one': '2020s: typical stack $21,345', 'e6.tessa': "Tessa's stack · ILLUSTRATIVE"},
         ['e0.decade', 'e1.typical', 'e1.fifteen', 'e2.y2000s', 'e2.fourteen', 'e3.y2010s', 'e3.far', 'e3.more', 'e3.twenty', 'e4.gap', 'e4.seven', 'e4.four',
          'e5.lower', 'e5.wider', 'e6.twenty', 'e6.one', 'e6.tessa', 'e7.history', 'e7.moved'],
         accents=[cue['e3']['twenty']], anchors=['S18.1'])
