"""Tập 5 · C4 · ĐOẠN D = S15–S20 (Hồi 3 · phương pháp · kết). Mở ở ba người mua (khung cuối đoạn C, c4kit.Buyers ở BX2).
  python3 episodes/ep005/world/c4/d-s15-s20/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
SPINE-PLAN §1 S15–S20 (ba làn; cùng gốc; mốc ~2 năm bằng VẠCH ĐỨNG + nhãn mô tả, không thẻ "your plan"; S19 thẻ V7 có danh sách "not modeled";
S20.3 "US only · history, not a forecast" giữ 2 s). Khác SPINE-PLAN: S18.6 kết ở thế giới (hai lối), S19 về khung đồ thị chính diện dưới thẻ V7
(số trên thẻ chỉ ở chế độ đồ thị — quy tắc 1), S20 trở lại hai lối."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); W5 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W5)
import c4kit as K
import spine as SV
S = K.Seg(['S15', 'S16', 'S17', 'S18', 'S19', 'S20'])
TOTAL, PAD = S.total, K.PAD
B = [
 ('g0', 'S15.1', 'world', 'Ba người mua minh hoạ cho thấy vì sao.', 'ba người không mặt cạnh ba nhà.', {'three': '@S15.1:Three', 'why': '@S15.1:why'}, [], 0.45, '', 'CHUYỂN CHẾ ĐỘ → đồ thị (làn Grace)'),
 ('g1', 'S15.2', 'chart', 'Grace: 6/2014, 4,16 %.', 'làn 1.', {'grace': '@S15.2:Grace', 'four': '@S15.2:at'}, [], 0.5, '', ''),
 ('g2', 'S15.3', 'chart', 'Tới 80 % trên giấy ở giữa phát lại.', 'đường trên giấy cắt 80 %.', {'eighty': '@S15.3:eighty', 'middle': '@S15.3:middle', 'typical': '@S15.3:typical'}, ['chime'], 0.5, '', ''),
 ('g3', 'S15.4', 'chart', 'Lịch của cô lâu hơn vài năm.', 'đường lịch tới kỳ 71.', {'schedule': '@S15.4:schedule', 'longer': '@S15.4:longer'}, [], 0.5, '', 'lia'),
 ('o0', 'S16.1', 'chart', 'Owen: 1/2004, giá đang lên nhanh.', 'làn 2: chỉ số dốc lên.', {'owen': '@S16.1:Owen', 'climbing': '@S16.1:climbing'}, ['data'], 0.6, '', ''),
 ('o1', 'S16.2', 'chart', '13 tháng, nhanh nhất.', 'đường trên giấy cắt 80 % gần như ngay.', {'thirteen': '@S16.2:thirteen', 'fastest': '@S16.2:fastest'}, ['chime'], 0.65, '', ''),
 ('o2', 'S16.3', 'chart', 'Giá làm phần lớn, không phải khoản trả.', '', {'rising': '@S16.3:Rising', 'payments': '@S16.3:payments'}, [], 0.6, '', 'lia'),
 ('v0', 'S17.1', 'chart', 'Victor: 10/2005, chậm nhất.', 'làn 3.', {'victor': '@S17.1:Victor', 'slowest': '@S17.1:slowest'}, [], 0.75, 'nặng', ''),
 ('v1', 'S17.2', 'chart', 'Giá lên chút rồi rơi nhiều năm; tới 80 % khi chỉ số vẫn dưới gốc.', 'chỉ số lên rồi rơi; đường trên giấy ở trên 80 % rất lâu.',
  {'prices': '@S17.2:Prices', 'fell': '@S17.2:fell', 'eighty': '@S17.2:eighty', 'below': '@S17.2:below'}, ['data', 'slide_down'], 0.85, 'đỉnh hồi 3', ''),
 ('v2', 'S17.3', 'chart', 'Lịch của anh chạm 80 % giá gốc trước, kỳ 90.', 'đường lịch cắt 80 % ở kỳ 90 (Burst).', {'schedule': '@S17.3:schedule', 'ninety': '@S17.3:ninety'}, ['chime'], 0.8, '',
  'CHUYỂN CHẾ ĐỘ → thế giới (nhà Victor, khiên)'),
 ('v3', 'S17.4', 'world', 'Bên cho vay có bỏ bảo hiểm không: dữ liệu không trả lời.', 'nhà Victor + khiên trên mái.', {'lender': '@S17.4:lender', 'show': '@S17.4:show'}, [], 0.5, '',
  'CHUYỂN CHẾ ĐỘ → đồ thị (ba làn cùng gốc)'),
 ('a0', 'S18.1', 'chart', 'Cùng luật, cùng chỉ số; khác tháng bắt đầu.', 'ba làn đặt cùng gốc.', {'same': '@S18.1:Same', 'started': '@S18.1:started', 'next': '@S18.1:next'}, [], 0.6, '', 'lùi máy'),
 ('a1', 'S18.2', 'chart', 'Hai mốc so sánh.', 'dải lịch + bó trên giấy.', {'plan': '@S18.2:plan', 'benchmarks': '@S18.2:benchmarks'}, [], 0.5, '', ''),   # C4 r2: vạch đứng "a plan" hiện ở "plan"
 ('a2', 'S18.3', 'chart', 'Lịch cố định từ đầu.', '', {'schedule': '@S18.3:schedule', 'decade': '@S18.3:decade'}, [], 0.5, '', ''),
 ('a3', 'S18.4', 'chart', 'Trên giấy: điển hình 23 tháng; ~2 năm khớp tháng điển hình.', 'vạch đứng ~24 tháng + nhãn mô tả.',
  {'history': '@S18.4:history', 'two': '@S18.4:two', 'slow': '@S18.4:slow', 'step': '@S18.4:step'}, [], 0.5, '', 'lia'),
 ('a4', 'S18.5', 'chart', '20 % trả trước: thêm $40,000.', 'đáy 10 % → 20 %.', {'twenty': '@S18.5:twenty', 'forty': '@S18.5:forty'}, ['rise'], 0.45, '', 'CHUYỂN CHẾ ĐỘ → thế giới (hai lối)'),
 ('a5', 'S18.6', 'world', 'Không cân với thuê hay chờ.', 'hai lối ngang nhau.', {'renting': '@S18.6:renting', 'measures': '@S18.6:measures'}, [], 0.35, '', 'CHUYỂN CHẾ ĐỘ → đồ thị (thẻ V7)'),
 ('m0', 'S19.1', 'chart', 'Cách biết + điều để ngoài: trên thẻ và mô tả.', 'thẻ V7.', {'card': '@S19.1:card', 'description': '@S19.1:description'}, [], 0.25, 'đọc', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('e0', 'S20.1', 'world', 'Bảo hiểm kéo dài bao lâu?', 'hai lối của S01.', {'insurance': '@S20.1:insurance', 'last': '@S20.1:last'}, [], 0.4, 'suy tư', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('e1', 'S20.2', 'chart', 'Lịch: cố định; trên giấy: ~1 năm tới hơn 9 năm; trên giấy ≠ đã gỡ.', 'dải lịch + bó.',
  {'schedule': '@S20.2:schedule', 'history': '@S20.2:history', 'nine': '@S20.2:nine', 'never': '@S20.2:never', 'removed': '@S20.2:removed'}, [], 0.45, '', ''),
 ('e2', 'S20.3', 'world', 'Chỉ Mỹ; lịch sử, không dự báo.', 'lớp bắt buộc giữ 2 s.', {'us': '@S20.3:U', 'history': '@S20.3:history'}, [], 0.2, '', '(hết)'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
w = K.window
MOVES = [
 ('m_g', 'mode', 'wBuyers', 'cLane1', cue['g1']['grace'], cue['g2']['eighty'], 0.9, 'lời "Grace bought in June 2014, at 4.16 percent": các số của cô → đồ thị (sau 5 s đầu đoạn — quy tắc 7 của build_seg)', 'whoosh_mode', False, 'fLane'),
 ('m_o', 'pan', 'cLane1', 'cLane2', cue['g3']['longer'], cue['o0']['owen'], 1.0, 'lời "Owen bought…": người mua thứ hai → lia', 'whoosh_push', False, None),
 ('m_v', 'pan', 'cLane2', 'cLane3', cue['o2']['payments'], cue['v0']['victor'], 1.0, 'lời "Victor bought the year after Owen": người mua thứ ba → lia', 'whoosh_push', False, None),
 ('m_vw', 'mode', 'cLane3', 'wVictor', cue['v2']['ninety'], cue['v3']['lender'], 0.9, 'lời "Whether a lender would have dropped his insurance": căn nhà + khiên → thế giới', 'whoosh_mode', False, 'fVic'),
 ('m_all', 'mode', 'wVictor', 'cAll', cue['v3']['show'], cue['a0']['same'], 0.9, 'lời "Same rule, same national index": ba làn cùng gốc → đồ thị', 'whoosh_mode', False, 'fAll'),
 ('m_bench', 'pull', 'cAll', 'cBench', cue['a0']['next'], cue['a1']['plan'], 0.9, 'lời "a plan can be measured against two benchmarks": mở khung cho hai mốc → lùi máy', 'whoosh_soft', False, None),
 ('m_down', 'pan', 'cBench', 'cDown', cue['a3']['step'], cue['a4']['twenty'], 1.1, 'lời "the other path, 20 percent down": về hai chồng giá → lia', 'whoosh_push', False, None),
 ('m_fork', 'mode', 'cDown', 'wFork', cue['a4']['forty'], cue['a5']['renting'], 1.0, 'lời "doesn\'t weigh that against renting or waiting": hai lối ngang nhau → thế giới', 'whoosh_mode', True, 'fFork'),
 ('m_card', 'mode', 'wFork', 'cCard', cue['a5']['measures'], cue['m0']['card'], 1.0, 'lời "How we know this … is on this card": thẻ phương pháp có số → đồ thị', 'whoosh_mode', False, 'fCard'),
 ('m_q', 'mode', 'cCard', 'wFork', cue['m0']['card'], cue['e0']['insurance'], 1.1, 'lời "So how long does the insurance last?": câu hỏi mở đầu trở lại → thế giới', 'whoosh_mode', True, 'fBack'),
 ('m_ans', 'mode', 'wFork', 'cAll2', cue['e0']['last'], cue['e1']['schedule'], 0.8, 'lời "On the schedule … on paper … from about a year to more than 9 years": số → đồ thị', 'whoosh_mode', False, 'fAns'),
 ('m_end', 'mode', 'cAll2', 'wHouse', cue['e1']['nine'], cue['e1']['never'], 1.0, 'lời "on paper is never the same as removed": khiên trên mái → thế giới', 'whoosh_mode', False, 'fEnd'),
]
moves = []
for mid, verb, a, b, after, before, dur, reason, snd, late, via in MOVES:
    t0, t1 = w(after, before, dur, late=late, start=5.05 if mid == 'm_g' else None)
    moves.append({'id': mid, 'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd, 'via': via})
FALLBACK = {}
moves = K.fly(moves, FALLBACK)
EV = [{'t': cue['g2']['middle'], 'kind': 'chime'}, {'t': cue['o1']['thirteen'], 'kind': 'chime'}, {'t': cue['v1']['fell'], 'kind': 'slide_down', 'dur': 0.8},
      {'t': cue['v2']['ninety'], 'kind': 'chime'}, {'t': cue['a4']['twenty'], 'kind': 'rise', 'dur': 0.8}]
EV += [{'t': round(cue['o0']['climbing'] - 0.4 + 0.25 * i, 3), 'kind': 'data', 'v': 0.4 + 0.15 * i} for i in range(4)]
EV += [{'t': round(cue['v1']['prices'] + (cue['v1']['below'] - cue['v1']['prices']) * i / 5, 3), 'kind': 'data', 'v': [0.5, 0.65, 0.4, 0.2, 0.15, 0.35][i]} for i in range(6)]
EV += SV.move_sounds(moves, lambda m: {'mode': 0.6, 'pan': 0.8, 'push': 0.8, 'pull': 1.0}[m['verb']])
EV.sort(key=lambda e: e['t'])
tension = [[0, 0.45]] + [[b['t0'], 0.2 + 0.6 * b['music']] for b in beats] + [[TOTAL, 0.05]]
errs = [e for e in SV.check_rules(beats, moves, PAD) if not e.startswith('quy tắc 7')]
spine = {'segment': 'ep005 C4 · D = S15–S20 (Hồi 3, phương pháp, kết)', 'version': 5, 'total': TOTAL, 'fps': 30, 'pad': PAD, 'episode_t0': S.t0, 'scenes': S.scenes,
         'takes': S.takes, 'words': S.words, 'beats': beats, 'moves': moves, 'fly_fallback': FALLBACK, 'music_plan': K.music_plan(S),
         'mix': {'music_db': K.music_db(S), 'data_db': 25.0}, 'events': EV, 'tension': tension, 'shots': SV.shots_for(moves, TOTAL),
         'label_cues': {'g1.four': 'Grace · June 2014 · 4.16%', 'g2.middle': 'on paper: 23 months', 'g3.schedule': 'schedule: 71',
                        'o0.owen': 'Owen · January 2004 · 5.71%', 'o1.thirteen': 'on paper: 13 months · schedule: 86', 'o2.rising': 'index +11.2%',
                        'v0.victor': 'Victor · October 2005 · 6.07%', 'v1.eighty': 'on paper: 112 months', 'v1.below': 'index still 3.3% below purchase',
                        'v2.schedule': 'schedule: 90 payments', 'v3.show': 'not in this data', 'a1.plan': 'a plan', 'v3.lender': '?', 'a2.schedule': 'schedule: fixed at the start',
                        'a3.history': 'on paper: typical 23 months · about 1 in 7 over 60', 'a4.forty': '20% down on $400,000: $40,000 more',
                        'a5.renting': 'keep renting, keep saving', 'e1.history': 'from about 1 year to more than 9 years · on paper', 'e1.never': 'on paper is not removed',
                        'e2.us': 'US only · history, not a forecast'},
         'visual_cues': ['g1.four', 'g2.middle', 'g3.schedule', 'o0.owen', 'o0.climbing', 'o1.thirteen', 'o2.rising', 'v0.victor', 'v1.fell', 'v1.eighty', 'v1.below',
                         'v2.schedule', 'v3.lender', 'v3.show', 'a1.plan', 'a2.schedule', 'a3.history', 'a3.two', 'a4.twenty', 'a4.forty', 'a5.renting', 'e1.history', 'e1.never', 'e2.us'],
         'checks': {'rule2_rule3': errs or 'OK', 'rule7': 'n/a (5 s đầu tập ở đoạn A)'}}
K.write(HERE, spine, ['episodes/ep005/world/claims.json', 'episodes/ep005/work/world-data/derived.json', 'episodes/ep005/world/c4kit.js'])
print('total', TOTAL, 'moves', [(m['id'], m['t0'], m['t1'], m.get('style')) for m in moves]); print('music_db', spine['mix']['music_db']); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
