"""Tập 7 · C4 · ĐOẠN B = S04–S09 (Hồi 1: hai khoản trả, đường lui, the stack, lãi hai khoản; kết ở MR1). Lời + giờ = timeline của nhà máy (0 ký tự EL).
  python3 episodes/ep007/world/c4/b-s04-s09/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, lặng neo/MR1, 'land')
B04 (S04): Tessa, nhà (tấm giấy vay loé ở "three"), "fifteen-year" thanh khoản 15 năm (ink) dâng (thế giới) → ĐỒ THỊ từ 5,0 s: "15-year: $2,828 a
month"; "thirty-year" thanh 30 năm dâng tới mức bắt buộc, rõ thấp hơn; "30-year required: $2,216 a month". Tessa nghiêng về phía thanh.
B05 (S05, V6 có nhãn): "gap" = hộp cushion trong suốt lấp khoảng giữa đỉnh thanh 30 năm và mức 15 năm + ngoặc; "fallback: about $613 a month lower",
"the least the 30-year asks"; về thế giới (S05.2 đời Tessa): "squeeze" thanh 15 năm loé; "house" Tessa giơ tay về nhà; "short" = bóng mờ thanh 30
năm tới mức trả trong 15 năm (chưa số). Lặng 0,75 s trước số neo S06.1.
B06 (S06, bản C3 s06-stack + hàng chờ C4 §3 #3): "finishing" vạch mức 15 năm (ink-muted, đứng yên) → đồ thị sớm (47,45 s) thấy "required: $2,216";
thanh 30 năm dâng sao cho ĐỈNH QUA VẠCH trước "forty" 0,08 s → "30-year paid in 15: $2,948 a month" đúng "forty"; ĐẨY MÁY vào đỉnh hai thanh (lát
warn ~23 px ở 540p, trước ~8); "one" lát loé + "+$120 a month"; "same" = lát TÁCH khỏi đỉnh thanh, lơ lửng (đúng từ); lùi máy; CHỒNG CHỈ DỰNG từ
"Over" (S06.3): lát lơ lửng là bó đầu, 14 lát nữa tách khỏi đỉnh thanh mỗi 0,16 s, chồng đủ 15 bó trước "twenty-one" → "the stack: $21,622 extra
paid over 15 years". Thang: thanh 1/980 USD/tháng (đỉnh 3,01) — chồng 15 bó cao 2,55, THẤP HƠN đỉnh thanh, đứng cách 1,15 về bên trái, nhãn riêng.
B07 (S07): thế giới: "stack" chồng loé + "the stack = the price of the fallback"; → đồ thị V3: hai đường lãi khảo sát 104 tuần tới tuần 8/10/2026
(accent, trục từ 0), "higher" tô khoảng giữa, "October" mốc cuối, "zero" ngoặc "30-year rate 0.67 point higher".
B08 (S08, W2 ×2): tháp lãi xếp bằng ĐÚNG bó của the stack (mệnh giá cố định $1,441.47 = một năm của $120/tháng), mỗi tầng 3 × 3 bó: tháp lãi 30
năm theo lịch riêng ($477,622 = 331 bó, 37 tầng) dâng ở "thirty-year" tới "four"; tháp 30 năm trả trong 15 năm ($210,691 = 146 bó) ở "fifteen" tới "two".
B09 (S09): tháp lãi 15 năm ($189,069 = 131 bó) ở "fifteen-year"; đẩy máy vào đỉnh hai tháp; "difference" = 15 bó trên cùng của tháp 30-trong-15
(phần cao hơn tháp 15 năm, vạch nét đứt từ đỉnh tháp 15 năm) hoá warn + ngoặc; "stack" = "difference = the stack: $21,622"; 15 bó đó RỜI THÁP từng
bó, máy về thế giới theo chúng, đáp đúng từng chỗ của 15 bó the stack cạnh nhà (cùng bó: chính là chồng); "plus" Tessa gật; "normal" = hàng chồng mờ của các tuần khác mọc sau nhà (xem trước hồi 2); "unusual" chồng
loé; giữ → MR1 (cả bản trộn lặng từ MR1 − 0,65 s tới hết đoạn)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c4kit as K
SV, G = K.SV, K.G
M = json.load(open(os.path.join(K.EP, 'out', 'model.json')))
Q = {k: v['value'] for k, v in M['quantities'].items()}
S = K.Seg(['S04', 'S05', 'S06', 'S07', 'S08', 'S09'])
B = [
 ('b0', 'S04.1', 'world', 'Điều Tessa đang cân nhắc.', 'Tessa, nhà, tấm giấy vay.', {'weighing': '@S04.1:weighing'}, [], 0.24, 'bình thản', '—'),
 ('b1', 'S04.2', 'chart', 'Vay $320,000: khoản 15 năm trả $2,828 mỗi tháng.', 'thanh 15 năm dâng (thế giới) → đồ thị: nhãn.',
  {'three': '@S04.2:three', 'fifteen': '@S04.2:fifteen-year', 'two': '@S04.2:two'}, ['tick', 'nốt dữ liệu', 'tick'], 0.26, 'bình thản', '—'),
 ('b2', 'S04.3', 'chart', 'Khoản 30 năm chỉ đòi $2,216.', 'thanh 30 năm dâng, thấp hơn; nhãn.',
  {'thirty': '@S04.3:thirty-year', 'two': '@S04.3:two'}, ['nốt dữ liệu', 'tick'], 0.28, 'bình thản', '—'),
 ('b3', 'S05.1', 'chart', 'Khoảng chênh ~$613/tháng là đường lui: mức thấp nhất khoản 30 năm đòi.', 'hộp cushion + ngoặc; hai nhãn.',
  {'gap': '@S05.1:gap', 'six': '@S05.1:six', 'least': '@S05.1:least'}, ['nốt dữ liệu', 'tick', 'tick'], 0.32, 'hiểu', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('b4', 'S05.2', 'world', 'Khoản lớn vừa đủ với ngân sách hôm nay; mất việc, sửa nhà có thể làm nó chật.', 'thanh 15 năm loé ("squeeze").',
  {'budget': '@S05.2:budget', 'squeeze': '@S05.2:squeeze'}, ['tick'], 0.3, 'lo', '—'),
 ('b5', 'S05.3', 'world', 'Cô muốn trả xong nhà trong 15 năm: khoản 30 năm phải trả như khoản ngắn.', 'Tessa giơ tay về nhà; bóng mờ thanh 30 năm.',
  {'house': '@S05.3:house', 'short': '@S05.3:short'}, ['tick'], 0.32, 'quyết', '(số neo S06.1: lặng 0,75 s)'),
 ('b6', 'S06.1', 'world', 'Ở 7,4 %, trả xong trong 15 năm cần $2,948 mỗi tháng.', 'vạch mức 15 năm; đồ thị: required; thanh 30 năm dâng qua vạch; nhãn đúng "forty".',
  {'finishing': '@S06.1:finishing', 'forty': '@S06.1:forty-eight'}, ['tick', 'rise', 'nốt dữ liệu'], 0.36, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b7', 'S06.2', 'chart', 'Hơn khoản 15 năm $120 mỗi tháng, cùng nhà, cùng 15 năm.', 'đẩy máy vào đỉnh thanh; lát loé "+$120 a month"; "same": lát tách, lơ lửng.',
  {'one': '@S06.2:one', 'same': '@S06.2:same'}, ['nốt dữ liệu', 'nốt dữ liệu'], 0.44, 'hiểu', 'lùi máy'),
 ('b8', 'S06.3', 'chart', 'Qua 15 năm, phần thêm thành $21,622.', 'chồng dựng từ "Over" (15 bó); nhãn chồng.',
  {'over': '@S06.3:Over', 'twenty': '@S06.3:twenty-one'}, ['nốt dữ liệu mỗi bó chạm', 'tick'], 0.62, 'nặng', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('b9', 'S07.1', 'world', 'Trong thế giới của Tessa, giá đó là chồng tiền cạnh nhà: the stack.', 'chồng loé + "the stack = the price of the fallback".',
  {'world': '@S07.1:world', 'stack': '@S07.1:stack', 'costs': '@S07.1:costs'}, ['tick'], 0.48, 'hiểu', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c0', 'S07.2', 'chart', 'Nó có vì khoản 30 năm lãi cao hơn: tuần 8/10 cao hơn 0,67 điểm.', 'hai đường lãi khảo sát; khoảng giữa; ngoặc + nhãn.',
  {'thirty': '@S07.2:thirty-year', 'higher': '@S07.2:higher', 'october': '@S07.2:October', 'zero': '@S07.2:zero'}, ['nốt dữ liệu ×2', 'tick', 'tick', 'nốt dữ liệu'], 0.48, 'hiểu', 'lùi máy'),
 ('c1', 'S08.1', 'chart', 'Trả theo lịch 30 năm: $477,622 tiền lãi.', 'tháp lãi rất cao (cùng mệnh giá bó).',
  {'thirty': '@S08.1:thirty-year', 'four': '@S08.1:four'}, ['rise', 'nốt dữ liệu'], 0.44, 'ngạc nhiên', '—'),
 ('c2', 'S08.2', 'chart', 'Trả trong 15 năm: $210,691.', 'tháp thấp hơn nhiều.',
  {'fifteen': '@S08.2:fifteen', 'two': '@S08.2:two'}, ['rise', 'nốt dữ liệu'], 0.44, 'hiểu', '—'),
 ('c3', 'S09.1', 'chart', 'Khoản 15 năm: $189,069; chênh giữa hai tổng cuối = đúng the stack.', 'tháp 15 năm; đẩy máy vào đỉnh; phần chênh hoá warn; nhãn.',
  {'fifteen': '@S09.1:fifteen-year', 'one': '@S09.1:one', 'difference': '@S09.1:difference', 'stack': '@S09.1:stack'}, ['rise', 'nốt dữ liệu', 'nốt dữ liệu', 'tick'], 0.5, 'hiểu', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('c4', 'S09.2', 'world', '30 năm trả trong 15 = 15 năm + đường lui, và đường lui có giá.', 'phần chênh đáp lên the stack; Tessa giơ tay; chồng loé.',
  {'plus': '@S09.2:plus', 'price': '@S09.2:price'}, ['nốt dữ liệu khi đáp', 'tick'], 0.58, 'hiểu', '—'),
 ('c5', 'S09.3', 'world', 'Chồng của Tessa có phải giá bình thường, hay tuần 8/10 khác thường?', 'hàng chồng mờ các tuần khác mọc sau nhà; chồng của Tessa loé.',
  {'normal': '@S09.3:normal', 'unusual': '@S09.3:unusual'}, ['rise', 'tick'], 0.52, 'tò mò', 'MR1'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
MR, SIL = K.midroll(S, 0)
# S06: thanh 30 năm dâng tuyến tính pay30 → pay30on15 trong RISE s; đỉnh qua vạch 15 năm ở phần (pay15 − pay30)/(pay30on15 − pay30) của cú dâng,
# đặt mốc qua vạch = "forty" − 0,08 s → nhãn $2,948 (hiện đúng "forty") luôn thấy đỉnh đã qua vạch
RISE = 1.2
xfrac = (G['pay15'] - G['pay30']) / (G['pay30on15'] - G['pay30'])
r0 = cue['b6']['forty'] - 0.08 - xfrac * RISE
moves = K.moves_of([
    ('m_push0', 'push', 'wB0', 'wB1', cue['b0']['weighing'], cue['b1']['three'], 0.9, 'lời S04.1 "what Tessa is weighing": máy lại gần Tessa và nhà', 'whoosh_air', {}),
    ('m_c1', 'mode', 'wB1', 'cB', cue['b1']['fifteen'], cue['b1']['two'], 1.2, 'lời S04.2 đặt số tiền mỗi tháng: số chỉ ở đồ thị (quy tắc 1), sau 5 s thế giới (quy tắc 7)', 'whoosh_mode', {'start': 5.0}),
    ('m_w5', 'mode', 'cB', 'wB5', cue['b3']['least'], cue['b4']['budget'], 1.3, 'lời S05.2 nói về đời Tessa (ngân sách, mất việc, sửa nhà), không số: về thế giới', 'whoosh_mode', {'start': cue['b3']['least'] + 1.85}),
    ('m_c6', 'mode', 'wB5', 'cB', cue['b6']['finishing'], cue['b6']['forty'], 1.0,
     'lời S06.1 đặt số $2,948: đồ thị SỚM (sau vạch mức 15 năm) để thấy thanh 30 năm ở mức bắt buộc có nhãn TRƯỚC khi dâng', 'whoosh_mode', {'start': cue['b6']['finishing'] + 0.58}),
    ('m_top', 'push', 'cB', 'cTop', cue['b6']['forty'], cue['b7']['one'], 1.2, 'lời S06.2 "$120 a month more": đẩy máy vào đỉnh hai thanh để lát phần dôi đọc được trên điện thoại', 'whoosh_push', {}),
    ('m_back', 'pull', 'cTop', 'cB', cue['b7']['same'], cue['b8']['over'], 1.4, 'lời S06.3 "over those 15 years": lùi máy cho chỗ the stack dựng cạnh nhà', 'whoosh_soft', {}),
    ('m_w7', 'mode', 'cB', 'wStack', cue['b8']['twenty'], cue['b9']['world'], 1.2, 'lời S07.1 "in Tessa\'s world … beside her house": về thế giới, chồng cạnh nhà', 'whoosh_mode', {'start': cue['b9']['world'] - 1.75}),
    ('m_c7', 'mode', 'wStack', 'cRates', cue['b9']['costs'], cue['c0']['thirty'], 1.6, 'lời S07.2 so lãi hai khoản trong tuần 8/10 (số): đồ thị hai đường lãi khảo sát', 'whoosh_mode', {}),
    ('m_out8', 'pull', 'cRates', 'cTowers', S.at('@S07.2$'), cue['c1']['thirty'], 1.6, 'lời S08 so hai tổng tiền lãi rất lớn: lùi xa cho chỗ hai tháp lãi', 'whoosh_soft', {}),
    ('m_tops', 'push', 'cTowers', 'cTops', cue['c3']['one'], cue['c3']['difference'], 1.6, 'lời S09.1 "the difference between those last two totals": đẩy máy vào đỉnh hai tháp gần bằng nhau', 'whoosh_push', {'late': True}),
    ('m_w9', 'mode', 'cTops', 'wHouse', cue['c3']['stack'], cue['c4']['plus'], 2.4, 'lời S09.2 "the 15-year plus a fallback": phần chênh rời tháp về cạnh nhà, máy theo nó về thế giới', 'whoosh_mode', {'start': cue['c3']['stack'] + 1.9}),
])
MV = {m['id']: m for m in moves}
assert MV['m_c1']['t0'] >= 5.0
# the stack (S06.3): lát lơ lửng từ "same" = bó đầu; mỗi bó rời đỉnh thanh 30 năm FLY s trước khi chạm; 15 bó, nhịp DT, bó cuối chạm trước "twenty-one"
FLY, DT = 0.6, 0.16
leave = [cue['b8']['over'] + DT * k for k in range(15)]
drops = [t + FLY for t in leave]
assert drops[-1] <= cue['b8']['twenty'] - 0.05, (drops[-1], cue['b8']['twenty'])
stack, ev = K.steps(drops, [G['bundle_usd'] * (k + 1) for k in range(15)], ramp=0.08, v0=0.0, pitch=lambda v: 0.2 + 0.6 * v / G['stack_total'])
# tháp lãi (W2, cùng mệnh giá bó với the stack): dâng tuyến tính tới tổng ở từ số
towers = {'full': [cue['c1']['thirty'], cue['c1']['four'], Q['interest_30full_now']], 'on15': [cue['c2']['fifteen'], cue['c2']['two'], Q['interest_30on15_now']],
          'y15': [cue['c3']['fifteen'], cue['c3']['one'], Q['interest_15_now']]}
LAND9 = round(MV['m_w9']['t1'] + 0.2, 3)          # phần chênh đáp lên the stack sau khi máy về thế giới
ghosts_i = [int(round(i * (len(M['series']['extra_total']) - 1) / 13)) for i in range(1, 13)]   # 12 tuần rải đều 1991 → 2026 (không gồm tuần của Tessa)
ev += [{'t': cue['b1']['three'], 'kind': 'tick', 'v': 0.3}, {'t': cue['b1']['fifteen'], 'kind': 'data', 'v': G['pay15'] / 3000},
       {'t': cue['b1']['two'], 'kind': 'tick', 'v': 0.45}, {'t': cue['b2']['thirty'], 'kind': 'data', 'v': G['pay30'] / 3000}, {'t': cue['b2']['two'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['b3']['gap'], 'kind': 'data', 'v': 0.3}, {'t': cue['b3']['six'], 'kind': 'tick', 'v': 0.45}, {'t': cue['b3']['least'], 'kind': 'tick', 'v': 0.35},
       {'t': cue['b4']['squeeze'], 'kind': 'tick', 'v': 0.3}, {'t': cue['b5']['short'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['b6']['finishing'], 'kind': 'tick', 'v': 0.35}, {'t': round(r0, 3), 'kind': 'rise', 'dur': RISE},
       {'t': cue['b6']['forty'], 'kind': 'data', 'v': G['pay30on15'] / 3000, 'over': True},
       {'t': cue['b7']['one'], 'kind': 'data', 'v': 0.4, 'over': True}, {'t': cue['b7']['same'], 'kind': 'data', 'v': 0.45, 'over': True},
       {'t': cue['b8']['twenty'], 'kind': 'tick', 'v': 0.7}, {'t': cue['b9']['stack'], 'kind': 'tick', 'v': 0.5},
       {'t': cue['c0']['thirty'], 'kind': 'data', 'v': Q['r30_now'] / 10}, {'t': round(cue['c0']['thirty'] + 0.3, 3), 'kind': 'data', 'v': Q['r15_now'] / 10},
       {'t': cue['c0']['higher'], 'kind': 'tick', 'v': 0.4}, {'t': cue['c0']['october'], 'kind': 'tick', 'v': 0.45}, {'t': cue['c0']['zero'], 'kind': 'data', 'v': 0.25},
       {'t': cue['c4']['price'], 'kind': 'tick', 'v': 0.5}, {'t': cue['c5']['normal'], 'kind': 'rise', 'dur': 1.2}, {'t': cue['c5']['unusual'], 'kind': 'tick', 'v': 0.55}]
for k, (a, z, usd) in towers.items():
    ev += [{'t': round(a, 3), 'kind': 'rise', 'dur': round(z - a, 3)}, {'t': round(z, 3), 'kind': 'data', 'v': round(usd / 500000, 3)}]
ev += [{'t': cue['c3']['difference'], 'kind': 'data', 'v': 0.6, 'over': True}, {'t': cue['c3']['stack'], 'kind': 'tick', 'v': 0.6},
       {'t': LAND9, 'kind': 'data', 'v': 0.62}]
X = {'house': -3.3, 'stack': -1.6, 'bar15': 1.2, 'bar30': 2.4, 'full': 5.5, 'on15': 8.6, 'y15': 11.7, 'towers': 8.6, 'rates': [16.0, 20.4]}
gestures = [{'t': cue['b2']['thirty'], 'kind': 'lean', 'to': X['bar30'], 'hold': 1.2},       # thanh 30 năm dâng (đồ thị)
            {'t': cue['b3']['gap'], 'kind': 'arm', 'to': X['bar30'], 'hold': 1.2},          # khoảng đường lui lấp (đồ thị)
            {'t': cue['b4']['budget'], 'kind': 'nod', 'hold': 0.5},
            {'t': cue['b5']['house'], 'kind': 'arm', 'to': X['house'], 'hold': 1.4},
            {'t': cue['b6']['forty'], 'kind': 'lean', 'to': X['bar30'], 'hold': 1.4},       # thanh 30 năm dâng qua vạch (đồ thị)
            {'t': cue['b8']['over'], 'kind': 'arm', 'to': X['stack'], 'hold': 3.0},         # chồng dựng (đồ thị)
            {'t': S.at('@S07.1:beside'), 'kind': 'arm', 'to': X['stack'], 'hold': 1.2},
            {'t': cue['c1']['four'], 'kind': 'lean', 'to': X['towers'], 'hold': 1.4}, {'t': cue['c2']['two'], 'kind': 'lean', 'to': X['towers'], 'hold': 1.2},
            {'t': LAND9, 'kind': 'arm', 'to': X['stack'], 'hold': 1.4}, {'t': cue['c4']['plus'], 'kind': 'nod', 'hold': 0.5},
            {'t': cue['c5']['unusual'], 'kind': 'lean', 'to': X['stack'], 'hold': 1.3}]
N_RATE = 104
K.finish(HERE, S, 'ep007 C4 · B = S04–S09 (Hồi 1: hai khoản trả, đường lui, the stack, lãi hai khoản) + MR1', beats, moves, ev,
         {'stack': stack, 'leave': [round(t, 3) for t in leave], 'fly': FLY, 'rise30': [[0.0, G['pay30']], [round(r0, 3), G['pay30']], [round(r0 + RISE, 3), G['pay30on15']]],
          'level_t': cue['b6']['finishing'], 'towers': {k: [round(a, 3), round(z, 3), u] for k, (a, z, u) in towers.items()}, 'land9': LAND9, 'mr1': MR,
          'lift_dt': 0.05, 'land_dt': 0.06,
          'x': X, 'gestures': gestures, 'ghosts': [M['series']['extra_total'][i] for i in ghosts_i],
          'rates': {'r30': M['series']['r30'][-N_RATE:], 'r15': M['series']['r15'][-N_RATE:], 'weeks': [M['series']['weeks'][-N_RATE], M['series']['weeks'][-1]]}},
         {'b1.two': '15-year: $2,828 a month', 'b2.two': '30-year required:', 'b3.six': 'fallback: about $613 a month lower',
          'b3.least': 'the least the 30-year asks', 'b6.forty': '30-year paid in 15: $2,948 a month', 'b7.one': '+$120 a month',
          'b8.twenty': 'the stack: $21,622', 'b9.stack': 'the stack = the price of the fallback',
          'c0.october': '30-year: 7.40%', 'c0.zero': '30-year rate 0.67 point higher', 'c1.four': '$477,622 interest', 'c2.two': '30-year paid in 15: $210,691',
          'c3.one': '15-year: $189,069 interest', 'c3.stack': 'difference = the stack: $21,622'},
         ['b1.three', 'b1.fifteen', 'b1.two', 'b2.thirty', 'b2.two', 'b3.gap', 'b3.six', 'b3.least', 'b4.squeeze', 'b5.house', 'b5.short', 'b6.finishing', 'b6.forty',
          'b7.one', 'b7.same', 'b8.over', 'b8.twenty', 'b9.stack', 'c0.thirty', 'c0.higher', 'c0.october', 'c0.zero', 'c1.thirty', 'c1.four', 'c2.fifteen', 'c2.two',
          'c3.fifteen', 'c3.one', 'c3.difference', 'c3.stack', 'c4.plus', 'c4.price', 'c5.normal', 'c5.unusual'],
         accents=[cue['b6']['forty'], cue['b8']['twenty']], anchors=['S06.1'], silences=[SIL])
