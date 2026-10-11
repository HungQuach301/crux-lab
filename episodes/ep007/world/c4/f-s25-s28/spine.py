"""Tập 7 · C4 · ĐOẠN F = S25–S28 (Hồi 3 mở: the bar = lãi của chính khoản vay, trước thuế; lịch sử của nó 1991–2026). Lời + giờ = timeline của nhà máy.
  python3 episodes/ep007/world/c4/f-s25-s28/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, lặng neo S28.1, 'land')
B25 (S25, KEY-10; bản C3 s25-bar + gates/C3.md §3 #6 + C3-answer câu 5): thế giới — "dollar" tờ đô la trả thêm trong tay Tessa, bay tới cạnh nhà và CHẠM
  đúng "charged"; the bar (W3 Beam, ink-muted) trồi từ sàn ĐÚNG "charged" (C3 −0,20 s) rồi dâng tới độ cao lãi ở "rate". → ĐỒ THỊ: THANG ĐỘ CAO = vạch đo
  từ sàn tới thanh có KHẮC mỗi điểm % (7 khắc + đỉnh), không chỉ chữ; "seven" = "the bar: 7.40% a year, before taxes" (khối 1); "investment" =
  "interest no longer charged, / not an investment return" (khối 2); "other" = BÓNG đô la thứ hai (mờ, viền nét đứt) tách đầu thanh, lên xuống LIÊN
  TỤC qua cả trên lẫn dưới độ cao thanh với biên độ đủ ngay từ đầu (không bao giờ dừng ngang mép thanh, kể cả lúc mờ đi), nhãn "any other use" ĐI THEO
  bóng; "measured" = vạch nét đứt ngang độ cao thanh từ đầu thanh tới chỗ bóng (phép "đo", cue hình mới — C3 −0,30 s); "whether" = "not tested: how any
  investment compares, / once risk and taxes count" (khối 3). Không xà/cột đỡ, không "trèo qua", không lợi suất đầu tư nào.
B26 (S26): lia sang lịch sử: "moves" đường lãi 30 năm từ Aug 1991 vẽ trái → phải, một đoạn thanh ngắn CƯỠI theo đầu đường; "taken" thanh + đoạn cưỡi loé;
  "high" mốc đỉnh; "nine" = "highest: 9.25% · Nov 1994".
B27 (S27): "low" mốc đáy; "two" = "lowest: 2.65% · Jan 2021".
B28 (S28, số neo — lặng 0,75 s trong đuôi S27): "Only" vạch nét đứt ngang độ cao thanh của Tessa qua cả lịch sử, đoạn đường lãi CAO HƠN sáng, phần còn
  lại tối; "one" = "weeks with a bar this high: about 1 week in 5"; "Tessa's" thanh loé, Tessa gật."""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c4kit as K
SV, G = K.SV, K.G
M = json.load(open(os.path.join(K.EP, 'out', 'model.json')))
Q = {k: v['value'] for k, v in M['quantities'].items()}
SE = M['series']
S = K.Seg(['S25', 'S26', 'S27', 'S28'])
B = [
 ('a0', 'S25.1', 'world', 'Mỗi đô la gốc trả thêm thôi bị tính lãi ở chính lãi khoản vay.', 'đô la trong tay Tessa → chạm chỗ cạnh nhà; thanh trồi từ sàn, dâng tới độ cao lãi.',
  {'dollar': '@S25.1:dollar', 'charged': '@S25.1:charged', 'rate': '@S25.1:rate'}, ['nốt dữ liệu', 'rise', 'nốt dữ liệu'], 0.3, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S25.2', 'chart', 'Với Tessa: 7.40% một năm, trước thuế.', 'thang độ cao có khắc; nhãn the bar.',
  {'seven': '@S25.2:seven'}, ['tick'], 0.4, 'rõ', '(liền)'),
 ('a2', 'S25.3', 'chart', 'Không phải lợi suất đầu tư; là lãi không còn phải trả.', 'khối chữ 2.',
  {'investment': '@S25.3:investment'}, ['tick'], 0.4, 'rõ', '(liền)'),
 ('a3', 'S25.4', 'chart', 'Lãi đó là mốc để so mọi cách dùng khác của đồng đô la, trước thuế.', 'bóng đô la thứ hai lên xuống liên tục; nhãn đi theo; vạch đo ngang.',
  {'bar': '@S25.4:bar', 'other': '@S25.4:other', 'measured': '@S25.4:measured'}, ['tick', 'tick', 'nốt dữ liệu'], 0.45, 'cân nhắc', '(liền)'),
 ('a4', 'S25.5', 'chart', 'Đầu tư so ra sao khi tính rủi ro và thuế: không kiểm ở đây.', 'khối chữ 3.',
  {'whether': '@S25.5:whether'}, ['tick'], 0.36, 'thận trọng', 'lia sang lịch sử'),
 ('b0', 'S26.1', 'chart', 'The bar đi theo lãi lúc vay.', 'đường lãi 30 năm vẽ, đoạn thanh cưỡi theo.',
  {'moves': '@S26.1:moves', 'taken': '@S26.1:taken'}, ['rise', 'tick'], 0.42, 'hiểu', '—'),
 ('b1', 'S26.2', 'chart', 'Từ 1991 cao nhất 9.25%.', 'mốc đỉnh + nhãn.',
  {'high': '@S26.2:high', 'nine': '@S26.2:nine'}, ['tick', 'nốt dữ liệu cao'], 0.46, 'ngạc nhiên', '—'),
 ('b2', 'S27.1', 'chart', 'Và thấp nhất 2.65%.', 'mốc đáy + nhãn.',
  {'low': '@S27.1:low', 'two': '@S27.1:two'}, ['tick', 'nốt dữ liệu thấp'], 0.46, 'ngạc nhiên', '(số neo S28.1: lặng 0,75 s)'),
 ('b3', 'S28.1', 'chart', 'Chỉ khoảng 1/5 số tuần có the bar cao như của Tessa.', 'vạch ngang độ cao thanh qua lịch sử; đoạn cao hơn sáng; nhãn.',
  {'only': '@S28.1:Only', 'one': '@S28.1:one', 'tessa': '@S28.1:Tessa'}, ['rise', 'tick', 'nốt dữ liệu'], 0.6, 'nghiêm', '(hết đoạn)'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c25', 'mode', 'wB', 'cB', cue['a0']['rate'], cue['a1']['seven'], 1.3,
     'S25.2 đặt lãi (số chỉ ở đồ thị, quy tắc 1) → chính diện vào độ cao thanh, sau khi thanh dâng xong (≥ 5 s thế giới)', 'whoosh_mode', {}),
    ('m_pan', 'pan', 'cB', 'cH', cue['a4']['whether'], cue['b0']['moves'], 1.6,
     'lời S26 "the bar moves with the rate": lia sang phải, chỗ lịch sử lãi 30 năm 1991–2026 cùng thang với thanh', 'whoosh_soft', {'late': True}),
])
MV = {m['id']: m for m in moves}
r30 = np.array(SE['r30']); N = len(r30)
i_max, i_min = int(np.argmax(r30)), int(np.argmin(r30))
assert SE['weeks'][i_max] == Q['r30_max_week'] and SE['weeks'][i_min] == Q['r30_min_week'] and r30[i_max] == Q['r30_max'] and r30[i_min] == Q['r30_min']
assert abs((r30 >= Q['r30_now']).mean() - Q['share_r30_ge_now']) < 0.005
c = cue
pitch = lambda r: round(0.15 + 0.07 * r, 3)     # cao độ = độ cao thanh (lãi %/năm)
ev = [{'t': c['a0']['dollar'], 'kind': 'data', 'v': 0.25}, {'t': c['a0']['charged'], 'kind': 'rise', 'dur': round(c['a0']['rate'] - c['a0']['charged'], 3)},
      {'t': c['a0']['rate'], 'kind': 'data', 'v': pitch(G['bar'])},
      {'t': c['a1']['seven'], 'kind': 'tick', 'v': 0.5}, {'t': c['a2']['investment'], 'kind': 'tick', 'v': 0.45},
      {'t': c['a3']['bar'], 'kind': 'tick', 'v': 0.3}, {'t': c['a3']['other'], 'kind': 'tick', 'v': 0.4}, {'t': c['a3']['measured'], 'kind': 'data', 'v': pitch(G['bar'])},
      {'t': c['a4']['whether'], 'kind': 'tick', 'v': 0.45},
      {'t': c['b0']['moves'], 'kind': 'rise', 'dur': 1.4}, {'t': c['b0']['taken'], 'kind': 'tick', 'v': 0.4},
      {'t': c['b1']['high'], 'kind': 'tick', 'v': 0.4}, {'t': c['b1']['nine'], 'kind': 'data', 'v': pitch(Q['r30_max'])},
      {'t': c['b2']['low'], 'kind': 'tick', 'v': 0.35}, {'t': c['b2']['two'], 'kind': 'data', 'v': pitch(Q['r30_min'])},
      {'t': c['b3']['only'], 'kind': 'rise', 'dur': 0.6}, {'t': c['b3']['one'], 'kind': 'tick', 'v': 0.55}, {'t': c['b3']['tessa'], 'kind': 'data', 'v': pitch(G['bar']), 'over': True}]
bar = [[0.0, 0.0], [round(c['a0']['charged'], 3), 0.0], [round(c['a0']['rate'], 3), G['bar']]]
X = {'house': -2.0, 'bx': 0.6, 'bl': 3.0, 'h0': 3.4, 'h1': 11.4}
gestures = [{'t': c['a0']['dollar'], 'kind': 'arm', 'to': X['bx'], 'hold': 2.2},          # tờ đô la trong tay, đưa đi
            {'t': c['a0']['rate'], 'kind': 'lean', 'to': X['bx'], 'hold': 1.2},           # thanh dâng tới độ cao lãi
            {'t': c['a3']['other'], 'kind': 'lean', 'to': X['bx'] + 3.0, 'hold': 1.4},     # bóng "any other use"
            {'t': c['b0']['moves'], 'kind': 'arm', 'to': X['h1'], 'hold': 1.6},            # lịch sử vẽ ra
            {'t': c['b1']['nine'], 'kind': 'lean', 'to': X['h0'], 'hold': 1.2},
            {'t': c['b2']['low'], 'kind': 'lean', 'to': X['h1'], 'hold': 1.2},
            {'t': c['b3']['tessa'], 'kind': 'nod', 'hold': 0.6}]
K.finish(HERE, S, 'ep007 C4 · F = S25–S28 (the bar + lịch sử lãi 30 năm)', beats, moves, ev,
         {'bar': bar, 'dollar1': {'appear': c['a0']['dollar'], 'place': [round(c['a0']['dollar'] + 0.5, 3), c['a0']['charged']]},
          'dollar2': {'appear': c['a3']['other']}, 'x': X, 'gestures': gestures, 'r30': SE['r30'], 'i': {'max': i_max, 'min': i_min}},
         {'a1.seven': 'the bar: 7.40% a year, before taxes', 'a2.investment': 'interest no longer charged,', 'a3.other': 'any other use',
          'a4.whether': 'not tested: how any investment compares,', 'b1.nine': 'highest: 9.25% · Nov 1994', 'b2.two': 'lowest: 2.65% · Jan 2021',
          'b3.one': 'weeks with a bar this high: about 1 week in 5'},
         ['a0.dollar', 'a0.charged', 'a1.seven', 'a2.investment', 'a3.bar', 'a3.other', 'a3.measured', 'a4.whether', 'b0.moves', 'b0.taken', 'b1.high', 'b1.nine',
          'b2.low', 'b2.two', 'b3.only', 'b3.one', 'b3.tessa'],
         accents=[c['a1']['seven']], anchors=['S28.1'])
