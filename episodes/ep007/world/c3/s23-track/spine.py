"""Tập 7 · C3 · s23-track (B23) — lời thật S23.1–S23.3 (cả cảnh; S23.2 bản hiện tại không nói "$8,792": số đó chỉ ở chữ trên hình).
  python3 episodes/ep007/world/c3/s23-track/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: tiếp trạng thái cuối s21-track — đường tháng 180 ô, mỗi ô một lớp trả thêm mỏng (cushion), vạch 15 năm. "once" = cột-năm đầu gom
12 lớp mỏng thành MỘT khối trên ô thứ 12 (cùng thể tích). → ĐỒ THỊ: "one" → "extra" 14 cột còn lại gom lần lượt (mỗi cột một nốt dữ liệu);
"one" = "$8,792 once a year" trên hàng ô thứ 12; "ends" → 4 ô warn quá vạch (nốt bội âm sáng); "four" = "ends in 184 months: 4 months later". Giữ."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c3kit as K
SV, wlib, G = K.SV, K.wlib, K.G
words, takes, lines, end = wlib.clip_voice([['S23.1', 'S23.2', 'S23.3']], lead=0.6)
A = SV.Anchors(words)
B = [
 ('a0', 'S23.1', 'world', 'Trả phần thêm mỗi năm một lần thay vì mỗi tháng?', 'đường tháng có lớp mỏng mỗi ô; "once": cột-năm đầu gom 12 lớp thành một khối.',
  {'send': '@S23.1:send', 'once': '@S23.1:once'}, ['nốt dữ liệu khi cột gom'], 0.3, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S23.2', 'chart', 'Một khoản mỗi năm, cùng tổng.', 'các cột còn lại gom thành khối trên ô thứ 12; nhãn "$8,792 once a year".',
  {'one': '@S23.2:one', 'extra': '@S23.2:extra'}, ['nốt dữ liệu mỗi cột', 'tick khi nhãn hiện'], 0.4, 'hiểu', '(liền)'),
 ('a2', 'S23.3', 'chart', 'Trả kiểu đó, khoản vay xong muộn 4 tháng.', '4 ô warn quá vạch; nhãn "ends in 184 months: 4 months later". Giữ.',
  {'ends': '@S23.3:ends', 'four': '@S23.3:four'}, ['nốt dữ liệu sáng mỗi ô trễ', 'tick khi nhãn hiện'], 0.5, 'bình thản', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('push', 'wT0', 'wT', 0.0, cue['a0']['send'], 2.4, 'mở đoạn: máy lại gần đường tháng (lớp trả thêm trên từng ô) trước khi phần thêm đổi cách đến ("send")', 'whoosh_air', {}),
    ('mode', 'wT', 'cT', cue['a0']['once'], cue['a1']['one'], 1.2,
     'S23.2–S23.3 đặt số tiền và số tháng; số chỉ ở chế độ đồ thị (quy tắc 1) → nhìn xuống lưới đếm khối năm và ô trễ', 'whoosh_mode', {'start': 5.0})])
gt = [cue['a0']['once']] + K.spread(cue['a1']['one'], cue['a1']['extra'], 14)
gk, ev = K.steps(gt, [k + 1 for k in range(15)], ramp=0.25, v0=0, pitch=lambda v: 0.3 + 0.35 * v / 15)
LL = G['lump_late_months']
lt = K.spread(cue['a2']['ends'] + 0.02, cue['a2']['four'] - 0.1, LL)
late, e2 = K.steps(lt, [k + 1 for k in range(LL)], ramp=0.07, v0=0, pitch=lambda v: 0.65 + 0.1 * v, over=True)
ev += e2 + [{'t': cue['a1']['one'], 'kind': 'tick', 'v': 0.5}, {'t': cue['a2']['four'], 'kind': 'tick', 'v': 0.35}]
K.finish(HERE, 'ep007 C3 · s23-track (S23)', words, takes, lines, end, beats, moves, ev,
         {'gathered': gk, 'late': late,
          'label_cues': {'a1.one': '$8,792 once a year', 'a2.four': 'ends in 184 months: 4 months later'},
          'visual_cues': ['a0.once', 'a1.one', 'a1.extra', 'a2.ends', 'a2.four']},
         [cue['a0']['once'], cue['a1']['one'], cue['a2']['four']], hold=1.2)
