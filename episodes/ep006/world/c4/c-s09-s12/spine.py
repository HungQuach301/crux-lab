"""Tập 6 · C4 · ĐOẠN C = S09–S12 (Hồi 1 · năm theo năm, cú rơi, séc đều; kết ở MR1). Lời + giờ = timeline của nhà máy (c4kit.Seg, 0 ký tự EL).
  python3 episodes/ep006/world/c4/c-s09-s12/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, có âm trong lặng)
MỞ ĐOẠN Ở THẾ GIỚI (quy tắc 7, verify first_5s_world): Ruth + séc + hàng 10 thùng (khung mở đầu, wRuth) — từ "Ruth's" séc lớn lên từng kỷ niệm,
hàng thùng theo sức mua năm đó (cùng bộ đếm năm với đường vẽ); "twelve" = hàng thùng loé; → ĐỒ THỊ từ 5,05 s, xong trước "anniversaries".
Đồ thị V3 dựng trong thế giới (dải Ribbon ở mặt phẳng z = 0,45, như đoạn a): x = kỷ niệm 0…20, y = sức mua so với séc đầu; vạch "first check" cố
định (ink-muted); mỗi kỷ niệm một chấm (cushion ≥ 100 %, warn < 100 %); hàng 10 thùng nhỏ bên phải chạy theo đầu đường (sức mua năm đang vẽ).
B09 (S09): đường vẽ năm 0 → 15 từ "Ruth's" tới "fifteen" (hiện khi vào đồ thị); "anniversaries" = "at or above: 12 of the first 15"; "slipped" = ba chấm warn (năm 2, 5, 6) loé,
"climbed" = chấm sau đó loé. B10 (S10, ĐỈNH): "August" = mốc năm 15 "Aug 2021, age 80: 100.3%"; "single" → "fell" = đoạn 15 → 16 rơi qua vạch
(warn); "caught" → "since" = năm 16 → 20 vẫn dưới vạch. B11 (S11, SỐ NEO: lặng 0,75 s trước câu): "August" = "Aug 2022, age 81: 94.5%".
B12 (S12): lùi máy + giãn trục y (đường séc đều cần chỗ); "level" = đường séc đều (ink-muted) vẽ năm 0 → 20; "five" = chấm năm 5 + vạch nét đứt ở
mức cuối của séc tăng (90,4 %) "level check: about 9 in 10 by year 5"; "twenty" = điểm cuối của séc tăng trên cùng vạch "rising check: there after
20 years"; S12.4 câu hỏi hồi 2: "?" lớn. MR1: cả bản trộn lặng từ MR1 − 0,65 s tới hết đoạn (= đầu S13), không sfx/âm dữ liệu."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c4kit as K
import yaml
SV = K.SV
S = K.Seg(['S09', 'S10', 'S11', 'S12'])
B = [
 ('d0', 'S09.1', 'world', 'Năm theo năm: 12 trong 15 kỷ niệm đầu, séc mua ít nhất bằng séc đầu.',
  'thế giới: séc lớn lên từng kỷ niệm, hàng thùng theo sức mua, "twelve" hàng loé → đồ thị: đường năm 0 → 15, chấm mỗi kỷ niệm; nhãn 12 of the first 15.',
  {'ruths': '@S09.1:Ruth', 'twelve': '@S09.1:twelve', 'anniv': '@S09.1:anniversaries'}, ['nốt dữ liệu mỗi năm'], 0.45, 'chú ý', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('d1', 'S09.2', 'chart', 'Vài năm đầu hụt xuống rồi lên lại.', 'ba chấm warn loé ("slipped"), chấm sau loé ("climbed").',
  {'slipped': '@S09.2:slipped', 'climbed': '@S09.2:climbed'}, ['tick'], 0.5, 'nhẹ nhõm', '—'),
 ('d2', 'S10.1', 'chart', 'Tháng 8/2021, 80 tuổi, séc vẫn mua nhỉnh hơn séc đầu.', 'mốc năm 15: Aug 2021, age 80: 100.3%.',
  {'august': '@S10.1:August', 'more': '@S10.1:more'}, ['tick'], 0.58, 'căng', '—'),
 ('d3', 'S10.2', 'chart', 'Rồi trong một năm, nó rơi xuống dưới và chưa lên lại.', 'đoạn 15 → 16 rơi qua vạch; năm 16 → 20 vẫn dưới.',
  {'single': '@S10.2:single', 'fell': '@S10.2:fell', 'caught': '@S10.2:caught', 'since': '@S10.2:since'}, ['data'], 0.72, 'nặng', '—'),
 ('d4', 'S11.1', 'chart', 'Tháng 8/2022: 94,5 %.', 'mốc năm 16: Aug 2022, age 81: 94.5%.',
  {'august': '@S11.1:August', 'ninety': '@S11.1:ninety-four'}, ['tick'], 0.56, 'nặng', 'lùi máy'),
 ('d5', 'S12.1', 'chart', 'Séc đều (so với khởi điểm của nó) rơi tới mức đó sớm hơn nhiều.', 'đường séc đều vẽ năm 0 → 20.',
  {'level': '@S12.1:level', 'sooner': '@S12.1:sooner'}, ['data'], 0.48, 'so sánh', '—'),
 ('d6', 'S12.2', 'chart', 'Năm 5 đã còn khoảng 9/10.', 'chấm năm 5 + vạch mức cuối 90,4 %.',
  {'five': '@S12.2:five', 'nine': '@S12.2:nine'}, ['tick'], 0.5, 'hiểu', '—'),
 ('d7', 'S12.3', 'chart', 'Séc tăng của bà đứng ở đó bây giờ, sau 20 năm.', 'điểm cuối của séc tăng trên cùng vạch.',
  {'rising': '@S12.3:rising', 'twenty': '@S12.3:twenty'}, ['tick'], 0.5, 'suy nghĩ', '—'),
 ('d8', 'S12.4', 'chart', 'Quãng của Ruth có khác thường không?', '"?" lớn → MR1.',
  {'ruths': '@S12.4:Ruth', 'usually': '@S12.4:usually'}, [], 0.54, 'tò mò', 'MR1'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c9', 'mode', 'wRuth', 'cNear0', cue['d0']['twelve'], cue['d0']['anniv'], 1.0,
     'lời S09.1 đặt số (12 trong 15 kỷ niệm): số chỉ ở đồ thị (quy tắc 1); đoạn mở ≥ 5 s ở thế giới (quy tắc 7)', 'whoosh_mode', {'start': 5.05}),
    ('m_push', 'push', 'cNear0', 'cNear', cue['d1']['climbed'], cue['d2']['august'], 1.2, 'lời S10.1 đưa tới năm 15 (Aug 2021): đẩy máy về phía năm 15–20', 'whoosh_push', {}),
    ('m_pull', 'pull', 'cNear', 'cWide', S.at('@S11.1$'), cue['d5']['level'], 1.3, 'lời S12.1 đưa séc đều (rơi xa hơn nhiều): lùi máy, giãn trục y', 'whoosh_soft', {}),
])
Pr = K.P['ruth']
y15 = K.spread(cue['d0']['ruths'], S.at('@S09.1:fifteen'), 16)               # năm 0 … 15
draw = [[0, 0]] + [[round(t, 3), k] for k, t in enumerate(y15)] + [[round(cue['d3']['single'], 3), 15], [round(cue['d3']['fell'] + 0.1, 3), 16],
        [round(cue['d3']['caught'], 3), 16], [round(cue['d3']['since'] + 0.6, 3), 20]]
lvl = [[0, 0], [round(cue['d5']['level'], 3), 0], [round(cue['d5']['sooner'] + 0.3, 3), 20]]
ev = [{'t': round(t, 3), 'kind': 'data', 'v': round(min(1.0, Pr[k]), 3)} for k, t in enumerate(y15) if k in (1, 2, 3, 5, 7, 9, 12, 15)]
ev += [{'t': cue['d0']['twelve'], 'kind': 'tick', 'v': 0.45},   # hàng thùng loé (thế giới) {'t': cue['d1']['slipped'], 'kind': 'tick', 'v': 0.3},
       {'t': cue['d1']['climbed'], 'kind': 'tick', 'v': 0.55}, {'t': cue['d2']['august'], 'kind': 'tick', 'v': 0.6},
       {'t': cue['d3']['fell'], 'kind': 'data', 'v': Pr[16]}, {'t': round(cue['d3']['since'] + 0.3, 3), 'kind': 'data', 'v': Pr[20]},
       {'t': cue['d4']['ninety'], 'kind': 'tick', 'v': 0.5}, {'t': cue['d5']['level'], 'kind': 'data', 'v': 0.9},
       {'t': round(cue['d5']['sooner'], 3), 'kind': 'data', 'v': 0.6}, {'t': cue['d6']['five'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['d7']['twenty'], 'kind': 'tick', 'v': 0.5}]
MR = float(yaml.safe_load(open(os.path.join(K.EP, 'episode.yaml')))['midrolls'][0]['t']) - S.t0
assert MR - 0.65 > S.last['S12'] + 0.05 and S.total - MR <= 1.0 and S.total - (MR - 0.65) >= 1.0, ('MR1', MR, S.last['S12'], S.total)
SIL = [[round(MR - 0.65, 3), S.total]]
K.finish(HERE, S, 'ep006 C4 · C = S09–S12 (Hồi 1: năm theo năm, cú rơi, séc đều) + MR1', beats, moves, ev,
         {'draw': draw, 'level_draw': lvl, 'ruth_path': Pr, 'level_path': [v / 100 for v in K.GRID['ruth_level']],
          'mr1': round(MR, 3)},
         {'d0.anniv': 'at or above: 12 of the first 15', 'd2.august': 'Aug 2021, age 80: 100.3%', 'd4.august': 'Aug 2022, age 81: 94.5%',
          'd6.five': 'level check: about 9 in 10 by year 5', 'd7.twenty': 'rising check: there after 20 years', 'axis0': 'Aug 2006', 'axis20': 'Aug 2026'},
         ['d0.ruths', 'd0.twelve', 'd0.anniv', 'd1.slipped', 'd1.climbed', 'd2.august', 'd3.fell', 'd3.since', 'd4.august', 'd5.level', 'd6.five', 'd7.twenty', 'd8.ruths'],
         accents=[cue['d3']['fell']], anchors=['S11.1'], silences=SIL, rule7=True)
