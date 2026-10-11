"""Tập 7 · C3 · s01-stack (B01, KEY-1) — lời thật S01.1 + S01.2 (cả cảnh; S01.2 bản hiện tại, không "this week").
  python3 episodes/ep007/world/c3/s01-stack/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Tessa (không mặt, ILLUSTRATIVE) cạnh nhà; the stack (W2, bó warn = một năm của khoản dự phòng) hiện cạnh nhà và thêm MỘT bó ở mỗi
nhịp lời ("costs", "month", "three", "dollars", "city", "bill"; mỗi bó một nốt dữ liệu, cao độ = chiều cao chồng). → ĐỒ THỊ sau 5 s (số chỉ ở
chế độ đồ thị, quy tắc 1): "three" = giá mỗi tháng "$120 a month" trên chồng; "payment" = "$320,000 loan · week of Oct 8, 2026" trên nhà."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c3kit as K     # wlib + spine v2 + khung khoá
SV, wlib = K.SV, K.wlib
words, takes, lines, end = wlib.clip_voice([['S01.1', 'S01.2']], lead=1.4)
A = SV.Anchors(words)
B = [
 ('a0', 'S01.1', 'world', 'Khoản dự phòng của Tessa có giá mỗi tháng.', 'Tessa cạnh nhà; chồng tiền mỏng hiện cạnh nhà, thêm một bó mỗi nhịp.',
  {'costs': '@S01.1:costs', 'month': '@S01.1:month'}, ['nốt dữ liệu mỗi bó (cao độ = chiều cao)'], 0.3, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S01.2', 'chart', 'Khoản vay $320,000, tuần 8/10/2026; giá $120 mỗi tháng.', 'chính diện: "$120 a month" trên chồng ("three"), nhãn khoản vay trên nhà ("payment").',
  {'three': '@S01.2:three', 'payment': '@S01.2:payment'}, ['tick khi nhãn hiện'], 0.45, 'tò mò', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('push', 'wS0', 'wS', 0.0, cue['a0']['costs'], 2.0, 'mở đoạn: máy lại gần Tessa và chỗ trống cạnh nhà trước bó đầu ("costs")', 'whoosh_air', {}),
    ('mode', 'wS', 'cS', cue['a0']['month'], cue['a1']['three'], 1.2,
     'lời S01.2 đặt số tiền khoản vay; số chỉ ở chế độ đồ thị (quy tắc 1) → đồ thị sau 5 s thế giới (quy tắc 7)', 'whoosh_mode', {'start': 5.0})])
beat_t = [cue['a0']['costs'], cue['a0']['month'], cue['a1']['three'], A.at('@S01.2:dollars'), A.at('@S01.2:city'), A.at('@S01.2:bill')]
nb = len(beat_t)
sk, ev = K.steps(beat_t, [K.G['bundle_usd'] * (i + 1) for i in range(nb)], ramp=0.22, v0=0.0, pitch=lambda v: 0.25 + 0.5 * v / (K.G['bundle_usd'] * nb))
ev += [{'t': cue['a1']['three'], 'kind': 'tick', 'v': 0.45}, {'t': cue['a1']['payment'], 'kind': 'tick', 'v': 0.55}]
K.finish(HERE, 'ep007 C3 · s01-stack (S01)', words, takes, lines, end, beats, moves, ev,
         {'stack': sk, 'label_cues': {'a1.three': '$120 a month', 'a1.payment': '$320,000 loan · week of Oct 8, 2026'},
          'visual_cues': ['a0.costs', 'a0.month', 'a1.three', 'a1.payment']}, [cue['a0']['costs'], cue['a1']['three']], hold=1.2)
