"""Tập 6 · C3 · s07-ruth (B07, KEY-4) — lời thật S07.1 + S07.2 (cả cảnh).
  python3 episodes/ep006/world/c3/s07-ruth/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Ruth (không mặt, ILLUSTRATIVE) đứng sau hàng 10 thùng sáng đủ = những gì khoản đầu mua; "less" → hàng mờ tới 0,904
(9 thùng sáng + thùng thứ 10 sáng 4 %, mờ liên tục). → ĐỒ THỊ (S07.2 đặt số: "about 9" chỉ ở chế độ đồ thị, quy tắc 1):
"ten" = ngoặc ink-muted trên cả 10 chỗ thùng "first check: 10 crates"; "nine" = ngoặc ink trên phần còn sáng + nhãn "today: about 9 in 10 crates (90.4%)"."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c3kit as K     # wlib + spine v2 + khung khoá hàng thùng
SV, wlib = K.SV, K.wlib
words, takes, lines, end = wlib.clip_voice([['S07.1', 'S07.2']], lead=0.4)
A = SV.Anchors(words)
B = [
 ('a0', 'S07.1', 'world', 'Khoản trả của Ruth có tăng, nhưng giá tăng nhanh hơn: hôm nay nó mua ít hơn khoản đầu.', 'Ruth sau hàng 10 thùng sáng đủ; "less": hàng mờ dần tới 0,904 (thùng thứ 10 gần tắt).',
  {'today': '@S07.1:today', 'less': '@S07.1:less'}, ['nốt dữ liệu khi hàng mờ (cao độ = sức mua)'], 0.3, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S07.2', 'chart', 'Tính bằng thùng: khoản đầu mua 10, hôm nay mua khoảng 9.', 'chính diện: ngoặc 10 chỗ ("ten"), ngoặc phần sáng + nhãn about 9 in 10 (90.4%) ("nine").',
  {'ten': '@S07.2:ten', 'nine': '@S07.2:nine'}, ['tick khi ngoặc hiện'], 0.45, 'hiểu', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('push', 'wRuth0', 'wRuth', 0.0, cue['a0']['today'], 2.4, 'mở đoạn: máy lại gần Ruth và hàng thùng trước "today" (đặt vật để thấy đổi trạng thái)', 'whoosh_air', {}),
    ('mode', 'wRuth', 'cRuth', cue['a0']['less'], cue['a1']['ten'], 1.2,
     'lời S07.2 đặt số ("about nine" của 10): số chỉ ở chế độ đồ thị (quy tắc 1) → đồ thị, sau câu S07.1', 'whoosh_mode', {'start': 5.0})])
v_end = K.P['ruth'][-1]
rk, ev = K.step_row([cue['a0']['less']], [v_end], ramp=0.9, v0=1.0)
ev += [{'t': cue['a1']['ten'], 'kind': 'tick', 'v': 0.45}, {'t': cue['a1']['nine'], 'kind': 'tick', 'v': 0.6}]
K.finish(HERE, 'ep006 C3 · s07-ruth (S07)', words, takes, lines, end, beats, moves, ev,
         {'rows': {'ruth': rk}, 'label_cues': {'a1.ten': 'first check: 10 crates', 'a1.nine': 'today: about 9 in 10 crates (90.4%)'},
          'visual_cues': ['a0.less', 'a1.ten', 'a1.nine']}, [cue['a0']['less'], cue['a1']['nine']])
