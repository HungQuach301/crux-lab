"""Tập 7 · C3 · s06-stack (B06, KEY-3) — lời thật S06.1–S06.3 (cả cảnh).
  python3 episodes/ep007/world/c3/s06-stack/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: Tessa, nhà, the stack (trống) và hai thanh khoản trả tháng (ink): 15 năm và 30 năm (mức bắt buộc, NGẮN hơn). "finishing" → vạch mức
15 năm (ink-muted, đứng yên) kéo qua cả hai thanh. → ĐỒ THỊ (số, quy tắc 1) với trạng thái TRƯỚC khi nâng: "$2,828 a month" ở vạch mức 15 năm,
"required: $2,216 a month" trên thanh 30 năm. "forty" = thanh 30 năm DÂNG lên $2,948 (âm rise), vượt vạch một lát mỏng (warn); nhãn đổi thành
"30-year paid in 15: $2,948 a month"; "one" = "+$120 a month" cạnh lát. "same" → "twenty": mỗi nhịp lát dôi TÁCH khỏi đỉnh thanh 30 năm, bay sang
chồng (15 lần; mỗi bó = một năm của $120/tháng; mỗi lần chạm một nốt dữ liệu); "twenty" = "the stack: $21,622 extra paid over 15 years". Giữ."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c3kit as K
SV, wlib, G = K.SV, K.wlib, K.G
words, takes, lines, end = wlib.clip_voice([['S06.1', 'S06.2', 'S06.3']], lead=0.6)
A = SV.Anchors(words)
B = [
 ('a0', 'S06.1', 'world', 'Trả khoản 30 năm xong trong 15 năm cần $2,948 mỗi tháng.', 'vạch mức 15 năm; đồ thị: hai thanh trước khi nâng có nhãn; "forty": thanh 30 năm dâng qua vạch; nhãn $2,948.',
  {'finishing': '@S06.1:finishing', 'takes': '@S06.1:takes', 'forty': '@S06.1:forty-eight'}, ['tick khi vạch hiện', 'rise khi thanh dâng', 'tick khi nhãn hiện'], 0.3, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S06.2', 'chart', 'Hơn khoản 15 năm $120 mỗi tháng.', 'nhãn "+$120 a month" cạnh lát warn; "same": lát tách khỏi đỉnh thanh 30 năm, bay sang chồng.',
  {'one': '@S06.2:one', 'same': '@S06.2:same'}, ['nốt dữ liệu mỗi bó chạm chồng'], 0.4, 'hiểu', '(liền)'),
 ('a2', 'S06.3', 'chart', 'Qua 15 năm: $21,622 trả thêm.', 'chồng tới đủ chiều cao; nhãn "the stack: $21,622 extra paid over 15 years". Giữ.',
  {'twenty': '@S06.3:twenty-one'}, ['tick khi nhãn hiện'], 0.5, 'nặng', '(hết) giữ ≥ 1,2 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_from([
    ('mode', 'wS', 'cS', cue['a0']['takes'], cue['a0']['forty'], 1.0,
     'lời S06.1 đặt số tiền mỗi tháng; số chỉ ở chế độ đồ thị (quy tắc 1) → đồ thị SỚM (ngay sau "takes") để hai thanh trước khi nâng đọc được có nhãn',
     'whoosh_mode', {'start': cue['a0']['takes'] + K.PAD + 0.01})])
f0, f48 = cue['a0']['finishing'], cue['a0']['forty']
RISE = 1.4                                                                              # dâng chậm, thấy được (vòng 1: người đọc không thấy nâng)
rise = [[0.0, G['pay30']], [round(f48, 3), G['pay30']], [round(f48 + RISE, 3), G['pay30on15']]]
FLY = 0.8                                                                               # lát tách khỏi đỉnh thanh → chạm chồng
drops = K.spread(cue['a1']['same'] + FLY, cue['a2']['twenty'] - 0.05, 15)               # lát đầu rời thanh đúng "same"; bó 15 chạm trước "twenty"
sk, ev = K.steps(drops, [G['bundle_usd'] * (k + 1) for k in range(15)], ramp=0.12, v0=0.0, pitch=lambda v: 0.2 + 0.6 * v / G['stack_total'])
ev += [{'t': round(f0, 3), 'kind': 'tick', 'v': 0.35}, {'t': round(f48, 3), 'kind': 'rise', 'dur': RISE}, {'t': round(f48, 3), 'kind': 'tick', 'v': 0.45},
       {'t': cue['a1']['one'], 'kind': 'tick', 'v': 0.55}, {'t': cue['a2']['twenty'], 'kind': 'tick', 'v': 0.7}]
K.finish(HERE, 'ep007 C3 · s06-stack (S06)', words, takes, lines, end, beats, moves, ev,
         {'bar30': rise, 'stack': sk, 'drops': [round(t, 3) for t in drops], 'drop_dur': FLY, 'level_t': round(f0, 3),
          'label_cues': {'a0.forty': '30-year paid in 15: $2,948 a month', 'a1.one': '+$120 a month', 'a2.twenty': 'the stack: $21,622 extra paid over 15 years'},
          'visual_cues': ['a0.finishing', 'a0.forty', 'a1.one', 'a1.same', 'a2.twenty']}, [f0, cue['a1']['one'], cue['a2']['twenty']], hold=1.2)
