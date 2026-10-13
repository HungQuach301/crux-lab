"""Tập 7 · C3 · s25-bar (B25, KEY-10) — lời thật S25.1–S25.5 (cả cảnh).
  python3 episodes/ep007/world/c3/s25-bar/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Tessa cạnh nhà; "dollar" = một tờ đô la trả thêm hiện trong tay Tessa, "stops" → trước "charged" bay tới chỗ cạnh nhà; vòng 3: sàn trống
trước đó (không có thanh nằm bẹp), thanh (W3 Beam, ink-muted) TRỒI từ dưới sàn lên đúng lúc tờ đô la tới, rồi "charged" → "rate" DÂNG lên độ cao lãi
khoản vay mang theo tờ đô la. → ĐỒ THỊ (số, quy tắc 1): "seven" = "the bar: 7.40% a year, before taxes"; "investment" = "interest no longer
charged, not an investment return"; "other" = BÓNG đô la thứ hai (mờ, viền nét đứt, cùng cỡ) hiện TÁCH khỏi đầu thanh, cạnh thanh, + nhãn
"any other use" dưới nó; bóng lên xuống nhẹ quanh độ cao thanh, biên độ lớn dần tới "measured" rồi giữ tới hết đoạn — độ cao để mở, không dừng trên hay dưới
(REVIEW-C3 CHÍNH-3: tờ áp vào đầu thanh bị đọc thành "kéo dài thanh / đã vượt"); "Whether" = "not tested: how any investment compares, / once
risk and taxes count" (hai dòng, dưới hai dòng "interest…"). Không hiện lợi suất đầu tư nào. Giữ."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c3kit as K
SV, wlib, G = K.SV, K.wlib, K.G
words, takes, lines, end = wlib.clip_voice([['S25.1', 'S25.2', 'S25.3', 'S25.4', 'S25.5']], lead=0.6)
A = SV.Anchors(words)
B = [
 ('a0', 'S25.1', 'world', 'Mỗi đô la gốc trả thêm thôi bị tính lãi ở chính lãi khoản vay.', 'đô la trong tay Tessa → đặt lên thanh; thanh dâng tới độ cao lãi.',
  {'dollar': '@S25.1:dollar', 'stops': '@S25.1:stops', 'charged': '@S25.1:charged', 'rate': '@S25.1:rate'}, ['nốt dữ liệu khi đô la hiện / thanh tới đỉnh', 'rise khi thanh dâng'], 0.3, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S25.2', 'chart', 'Với Tessa: 7.40% một năm, trước thuế.', 'nhãn "the bar: 7.40% a year, before taxes".',
  {'seven': '@S25.2:seven'}, ['tick khi nhãn hiện'], 0.4, 'rõ', '(liền)'),
 ('a2', 'S25.3', 'chart', 'Không phải lợi suất đầu tư; là lãi không còn phải trả.', 'nhãn "interest no longer charged, not an investment return".',
  {'investment': '@S25.3:investment'}, ['tick khi nhãn hiện'], 0.4, 'rõ', '(liền)'),
 ('a3', 'S25.4', 'chart', 'Lãi đó là mốc để so mọi cách dùng khác của đồng đô la, trước thuế.', 'bóng đô la thứ hai "any other use" đứng tách đầu thanh, lên xuống quanh độ cao thanh (để mở).',
  {'other': '@S25.4:other', 'measured': '@S25.4:measured'}, ['nốt dữ liệu khi đô la thứ hai áp vào thanh'], 0.45, 'cân nhắc', '(liền)'),
 ('a4', 'S25.5', 'chart', 'Đầu tư so ra sao khi tính rủi ro và thuế: không kiểm ở đây.', 'nhãn "not tested: how any investment compares, once risk and taxes count". Giữ.',
  {'whether': '@S25.5:whether'}, ['tick khi nhãn hiện'], 0.35, 'thận trọng', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('mode', 'wB', 'cB', cue['a0']['rate'], cue['a1']['seven'], 1.3,
     'S25.2 đặt lãi; số chỉ ở chế độ đồ thị (quy tắc 1) → chính diện vào độ cao thanh, sau khi thanh dâng xong (≥ 5 s thế giới)', 'whoosh_mode', {})])
c = cue
pitch = lambda r: 0.15 + 0.07 * r     # cao độ nốt = độ cao thanh (lãi %/năm): 7.40 → 0,67
ev = [{'t': c['a0']['dollar'], 'kind': 'data', 'v': 0.25}, {'t': c['a0']['rate'], 'kind': 'data', 'v': round(pitch(G['bar']), 3)},
      {'t': c['a3']['measured'], 'kind': 'data', 'v': round(pitch(G['bar']), 3)},
      {'t': c['a0']['charged'], 'kind': 'rise', 'dur': round(c['a0']['rate'] - c['a0']['charged'], 3)},
      {'t': c['a1']['seven'], 'kind': 'tick', 'v': 0.5}, {'t': c['a2']['investment'], 'kind': 'tick', 'v': 0.45},
      {'t': c['a3']['other'], 'kind': 'tick', 'v': 0.4}, {'t': c['a4']['whether'], 'kind': 'tick', 'v': 0.45}]
bar = [[0.0, 0.0], [round(c['a0']['charged'], 3), 0.0], [round(c['a0']['rate'], 3), G['bar']]]
K.finish(HERE, 'ep007 C3 · s25-bar (S25)', words, takes, lines, end, beats, moves, ev,
         {'bar': bar, 'dollar1': {'appear': c['a0']['dollar'], 'place': [c['a0']['stops'], c['a0']['charged'] - 0.15]},
          'dollar2': {'appear': c['a3']['other'], 'hold': [c['a3']['other'] + 0.3, c['a3']['measured']]},
          'label_cues': {'a1.seven': 'the bar: 7.40% a year, before taxes', 'a2.investment': 'interest no longer charged,',
                         'a3.other': 'any other use', 'a4.whether': 'not tested: how any investment compares,'},
          'visual_cues': ['a0.dollar', 'a0.charged', 'a1.seven', 'a2.investment', 'a3.other', 'a3.measured', 'a4.whether']},
         [c['a0']['rate'], c['a1']['seven'], c['a3']['measured']], hold=1.2)
