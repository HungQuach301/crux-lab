"""Tập 6 · C3 · s29-three (B29, KEY-9) — lời thật S29.1–S29.3 (cả cảnh).
  python3 episodes/ep006/world/c3/s29-three/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: ba người không mặt (Edna, Ruth, Carl — ILLUSTRATIVE), mỗi người sau hàng 10 thùng sáng đủ (khoản đầu). Theo lời S29.1: "Edna" hàng
loé, vẫn đủ 10; "Ruth" hàng mờ tới 0,904; "Carl" hàng mờ qua năm 5/10/15/20 tới 0,431. → ĐỒ THỊ trước "crates" (số chỉ ở đồ thị):
"crates at year 20 · same 2% raise"; "full" = "10" trên hàng Edna, "nine" = "about 9" trên hàng Ruth, "four" = "about 4" trên hàng Carl;
nhãn tên + tháng bắt đầu; "month" = dòng tháng bắt đầu sáng lên (điều khác nhau duy nhất)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c3kit as K     # wlib + spine v2 + khung khoá hàng thùng
SV, wlib = K.SV, K.wlib
words, takes, lines, end = wlib.clip_voice([['S29.1', 'S29.2', 'S29.3']], lead=0.4)
A = SV.Anchors(words)
B = [
 ('d0', 'S29.1', 'world', 'Cùng khoản tăng, cùng luật: Edna theo kịp, Ruth hụt muộn, Carl hụt xa.', 'ba người + ba hàng 10 thùng; theo tên: Edna đủ 10, Ruth mờ tới 0,904, Carl mờ tới 0,431.',
  {'edna': '@S29.1:Edna', 'ruth': '@S29.1:Ruth', 'carl': '@S29.1:Carl'}, ['tick ở Edna', 'nốt dữ liệu khi hàng mờ'], 0.35, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('d1', 'S29.2', 'chart', 'Tính bằng thùng ở năm 20: Edna đủ 10, Ruth khoảng 9, Carl khoảng 4.', 'nhãn từng hàng 10 · about 9 · about 4.',
  {'crates': '@S29.2:crates', 'full': '@S29.2:full', 'nine': '@S29.2:nine', 'four': '@S29.2:four'}, ['tick mỗi nhãn'], 0.45, 'hiểu', '—'),
 ('d2', 'S29.3', 'chart', 'Điều khác nhau là tháng mỗi người bắt đầu và giá sau đó.', 'dòng tháng bắt đầu sáng lên ở "month".',
  {'month': '@S29.3:month'}, ['tick nhẹ'], 0.35, 'suy nghĩ', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('push', 'wThree0', 'wThree', 0.0, cue['d0']['edna'], 1.6, 'mở đoạn: máy lại gần ba người và ba hàng thùng trước tên đầu tiên', 'whoosh_air', {}),
    ('mode', 'wThree', 'cThree', cue['d0']['carl'] + 1.15, cue['d1']['crates'], 0.9,
     'lời S29.2 đặt số thùng ở năm 20 (10 · about 9 · about 4): số chỉ ở chế độ đồ thị (quy tắc 1) → đồ thị', 'whoosh_mode', {'start': 5.0})])
Pr, Pc = K.P['ruth'], K.P['carl']
rk, ev = K.step_row([cue['d0']['ruth']], [Pr[-1]], ramp=0.6, v0=1.0)
ct = K.spread(cue['d0']['carl'], cue['d0']['carl'] + 0.9, 4)
ck, ev2 = K.step_row(ct, [Pc[5], Pc[10], Pc[15], Pc[20]], ramp=0.22, v0=1.0)
ev += ev2 + [{'t': cue['d0']['edna'], 'kind': 'tick', 'v': 0.5}, {'t': cue['d1']['full'], 'kind': 'tick', 'v': 0.6}, {'t': cue['d1']['nine'], 'kind': 'tick', 'v': 0.5},
             {'t': cue['d1']['four'], 'kind': 'tick', 'v': 0.35}, {'t': cue['d2']['month'], 'kind': 'tick', 'v': 0.4}]
K.finish(HERE, 'ep006 C3 · s29-three (S29)', words, takes, lines, end, beats, moves, ev,
         {'rows': {'edna': [[0, 1.0]], 'ruth': rk, 'carl': ck},
          'label_cues': {'d1.crates': 'crates at year 20 · same 2% raise', 'd1.full': '10', 'd1.nine': 'about 9', 'd1.four': 'about 4'},
          'visual_cues': ['d0.edna', 'd0.ruth', 'd0.carl', 'd1.full', 'd1.nine', 'd1.four', 'd2.month']},
         [cue['d0']['carl'], cue['d1']['four']])
