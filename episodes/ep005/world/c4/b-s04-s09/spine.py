"""Tập 5 · C4 · ĐOẠN B = S04–S09 (Hồi 1: bảo hiểm là gì, khoản vay minh hoạ, hai mốc luật, con đường giá trị) + MR1.
  python3 episodes/ep005/world/c4/b-s04-s09/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
SPINE-PLAN §1 S04–S09; N1 lịch (code C3 vòng 3 + chip "$2,362/month · principal + interest" GẮN vào lịch, REVIEWER R1 B06).
Khác SPINE-PLAN (cửa sổ < 0,6 s theo giờ take thật): S04 'push' giữa "lender" và "borrower"; bỏ 'pull' S04.5 — S05 bay thẳng từ lịch sang
đồ thị giá trong "Here's an illustrative example" (đuôi S04); S09 về đồ thị sau "If prices rise" (thế giới thấy chồng giá trị lớn lên trước).
MR1: sau S09.4 máy bay về phố (Hồi 2), chạm rồi LẶNG (nhạc nền F-3 về 0 quanh MR1; không sfx) tới hết cảnh. Đoạn mở từ tối (ident của đoạn A)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); W5 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W5)
import c4kit as K
import spine as SV
S = K.Seg(['S04', 'S05', 'S06', 'S07', 'S08', 'S09'])
TOTAL, PAD = S.total, K.PAD
B = [
 ('p0', 'S04.1', 'world', 'PMI: bên cho vay đòi khi trả trước < 20 %.', 'nhà + khiên; chồng 10 % dưới vạch 20 % (không số).',
  {'private': '@S04.1:Private', 'lenders': '@S04.1:lenders', 'twenty': '@S04.1:twenty'}, [], 0.25, 'bình thản', ''),
 ('p1', 'S04.2', 'world', 'Bảo vệ bên cho vay; người vay trả hằng tháng.', 'người cho vay; lịch lật, thẻ nhỏ bay tới khiên.',
  {'lender': '@S04.2:lender', 'borrower': '@S04.2:borrower', 'month': '@S04.2:month', 'top': '@S04.2:top'}, ['tick'], 0.3, 'rõ', 'đẩy máy'),
 ('p2', 'S04.3', 'world', 'Không nêu phí.', 'nhãn "cost: not shown in this video".', {'costs': '@S04.3:costs', 'dollar': '@S04.3:dollar'}, [], 0.25, 'thẳng', ''),
 ('p3', 'S04.4', 'world', 'Đo được: kéo dài bao lâu.', 'lịch lật nhanh.', {'measure': '@S04.4:measure', 'lasts': '@S04.4:lasts'}, ['data'], 0.35, 'tò mò', ''),
 ('p4', 'S04.5', 'world', 'Khi nào hết?', 'lịch dừng.', {'end': '@S04.5:end'}, [], 0.35, 'câu hỏi', 'CHUYỂN CHẾ ĐỘ → đồ thị (ví dụ là số)'),
 ('e0', 'S05.1', 'chart', 'Nhà minh hoạ $400,000; trung vị nhà mới $410,700.', 'chồng giá chính diện; vạch trung vị.',
  {'four': '@S05.1:four', 'median': '@S05.1:median'}, ['land'], 0.35, 'cụ thể', ''),
 ('e1', 'S05.2', 'chart', '10 % trả trước → khoản vay $360,000.', 'đáy 10 % tách ra.', {'ten': '@S05.2:ten', 'loan': '@S05.2:loan'}, ['land'], 0.35, 'cụ thể', 'lia'),
 ('y0', 'S06.1', 'chart', 'Lãi tháng 9: 6,86 %; khoản trả vốn + lãi.', 'chip lãi; chip $2,362 gắn vào lịch.',
  {'six': '@S06.1:six', 'monthly': '@S06.1:monthly', 'figure': '@S06.1:figure'}, ['tick', 'land'], 0.35, 'bình thản', ''),
 ('y1', 'S06.2', 'chart', 'Thuế, bảo hiểm nhà, PMI cộng thêm.', 'chip xếp trên chip trả; thẻ warn trên trang lịch.', {'taxes': '@S06.2:Taxes'}, [], 0.35, '', ''),
 ('y2', 'S06.3', 'chart', 'Chậm lúc đầu, nhanh về sau.', 'lịch dư nợ in sẵn; chồng trượt theo kỳ.',
  {'each': '@S06.3:Each', 'slowly': '@S06.3:slowly', 'faster': '@S06.3:faster'}, ['data'], 0.45, 'cơ chế', 'đẩy máy'),
 ('l0', 'S07.1', 'chart', 'Luật: được xin huỷ khi lịch về 80 % giá gốc ($320,000).', 'phóng vào 0–10 năm; vạch 80 %.',
  {'law': '@S07.1:law', 'eighty': '@S07.1:eighty', 'three': '@S07.1:three'}, ['chime'], 0.5, 'chính xác', ''),
 ('l1', 'S07.2', 'chart', 'Kỳ 99.', 'trang "99" ghim ở giao điểm.', {'ninety': '@S07.2:ninety'}, ['tick'], 0.55, '', ''),
 ('l2', 'S07.3', 'chart', 'Có điều kiện.', 'nhãn điều kiện.', {'conditions': '@S07.3:conditions'}, [], 0.5, '', ''),
 ('a0', 'S08.1', 'chart', 'Tự hết ở 78 %.', 'vạch 78 % thứ hai.', {'seventy': '@S08.1:seventy', 'current': '@S08.1:current'}, ['chime'], 0.6, 'đỉnh hồi 1', ''),
 ('a1', 'S08.2', 'chart', 'Khoảng 9,5 năm.', 'mốc 114.', {'nine': '@S08.2:nine'}, ['tick'], 0.6, '', 'lùi máy'),
 ('a2', 'S08.3', 'chart', 'Cả hai mốc chỉ từ lịch; bỏ qua giá trị nhà.', 'khung mở: căn nhà ngoài khung đồ thị.',
  {'both': '@S08.3:Both', 'schedule': '@S08.3:schedule', 'worth': '@S08.3:worth'}, [], 0.5, 'nhận ra', 'CHUYỂN CHẾ ĐỘ → thế giới (căn nhà)'),
 ('v0', 'S09.1', 'world', 'Bên cho vay có thể bỏ theo giá trị hiện tại.', 'nhà trên chồng giá trị lớn dần.',
  {'lenders': '@S09.1:Lenders', 'value': '@S09.1:value'}, ['rise'], 0.45, 'mở', ''),
 ('v1', 'S09.2', 'chart', 'Giá lên → cùng dư nợ thành phần nhỏ hơn → 80 % sớm hơn, trên giấy.', 'hai chồng chính diện; vạch 80 % của giá trị dâng lên gặp chồng vay.',
  {'same': '@S09.2:same', 'eighty': '@S09.2:eighty', 'sooner': '@S09.2:sooner', 'paper': '@S09.2:paper'}, ['chime'], 0.55, 'hiểu', ''),
 ('v2', 'S09.3', 'chart', 'Vẫn cần yêu cầu, thẩm định, thời gian tối thiểu.', 'nhãn luật bên cho vay.', {'request': '@S09.3:request'}, [], 0.45, '', ''),
 ('v3', 'S09.4', 'chart', 'Giá lên đã đưa người mua 10 % tới đó nhanh tới đâu?', '"?" trên khoảng hở.', {'fast': '@S09.4:fast', 'there': '@S09.4:there'}, [], 0.5, 'câu hỏi',
  'CHUYỂN CHẾ ĐỘ → thế giới (phố: mỗi nhà một tháng mua), rồi MR1'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
w = K.window
MOVES = [
 ('m_push', 'push', 'wPMI', 'wCal', cue['p1']['lender'], cue['p1']['borrower'], 1.0, 'lời "the borrower pays for it, month after month": người vay + lịch → đẩy máy', 'whoosh_push', False, None),
 ('m_e', 'mode', 'wCal', 'cPrice', cue['p4']['end'], cue['e0']['four'], 1.2, 'lời "Here\'s an illustrative example": ví dụ là các con số → đồ thị', 'whoosh_mode', True, 'fEx'),
 ('m_pay', 'pan', 'cPrice', 'cPay', cue['e1']['loan'], cue['y0']['six'], 1.0, 'lời "At September\'s average mortgage rate": khoản vay → khoản trả theo kỳ → lia', 'whoosh_push', False, None),
 ('m_law', 'push', 'cPay', 'cSched80', cue['y2']['faster'], cue['l0']['law'], 1.0, 'lời "By federal law … once the schedule says…": mốc nằm ở mười năm đầu của chính đường này → đẩy máy', 'whoosh_push', False, None),
 ('m_wide', 'pull', 'cSched80', 'cWide', cue['a1']['nine'], cue['a2']['both'], 0.75, 'lời "Both dates come from the schedule alone": cả đường + căn nhà ngoài khung → lùi máy', 'whoosh_soft', True, None),
 ('m_val', 'mode', 'cWide', 'wValue', cue['a2']['worth'], cue['v0']['lenders'], 0.9, 'lời "based on the home\'s current value": giá trị là của căn nhà → thế giới', 'whoosh_mode', False, 'fVal'),
 ('m_def', 'mode', 'wValue', 'cDef2', cue['v0']['value'], cue['v1']['same'], 1.1, 'lời "the same balance becomes a smaller share": tỉ lệ là số → đồ thị', 'whoosh_mode', True, 'fShare'),
 ('m_mr', 'mode', 'cDef2', 'wStreet', cue['v3']['there'], round(cue['v3']['there'] + 1.55, 3), 1.1, 'hết Hồi 1, câu hỏi "how fast … buyers there?": phố (mỗi nhà một tháng mua) → thế giới, rồi MR1 lặng', 'whoosh_mode', False, 'fStreet'),
]
moves = []
for mid, verb, a, b, after, before, dur, reason, snd, late, via in MOVES:
    t0, t1 = w(after, before, dur, late=late)
    moves.append({'id': mid, 'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd, 'via': via})
FALLBACK = {}
moves = K.fly(moves, FALLBACK)
M = {m['id']: m for m in moves}
CL = json.load(open(os.path.join(K.ROOT, 'episodes/ep005/world/claims.json')))
KSTOP = CL['sched78_months_latest']['value']
PAYK = [[cue['y2']['each'], 0], [cue['y2']['faster'], KSTOP]]
r = CL['rate_latest']['value'] / 1200
bal = lambda k: (1 + r) ** k - ((1 + r) ** k - 1) / (1 - (1 + r) ** -360)
FLIP = [cue['p3']['measure'], cue['p4']['end']]                     # S04.4: lịch lật nhanh; dừng ở "end"
EV = [{'t': cue['p1']['month'], 'kind': 'tick', 'v': 0.4}, {'t': round(cue['p1']['month'] + 0.75, 3), 'kind': 'tick', 'v': 0.45}, {'t': cue['p1']['top'], 'kind': 'tick', 'v': 0.5}]
EV += [{'t': round(FLIP[0] + (FLIP[1] - FLIP[0]) * i / 5, 3), 'kind': 'data', 'v': 0.3 + 0.08 * i} for i in range(6)]
EV += [{'t': cue['e0']['four'], 'kind': 'land', 'mode': False}, {'t': cue['e1']['ten'], 'kind': 'land', 'mode': False},
       {'t': cue['y0']['monthly'], 'kind': 'tick', 'v': 0.5}, {'t': cue['y0']['figure'], 'kind': 'land', 'mode': False}]
for k in list(range(0, KSTOP, 24)) + [KSTOP]:
    t = PAYK[0][0] + (PAYK[1][0] - PAYK[0][0]) * k / KSTOP
    EV.append({'t': round(t, 3), 'kind': 'data', 'v': round(bal(k), 3)})
EV += [{'t': cue['l0']['eighty'], 'kind': 'chime'}, {'t': cue['l1']['ninety'], 'kind': 'tick', 'v': 0.6},
       {'t': cue['a0']['seventy'], 'kind': 'chime'}, {'t': cue['a1']['nine'], 'kind': 'tick', 'v': 0.7},
       {'t': cue['v0']['value'], 'kind': 'rise', 'dur': 0.8}, {'t': cue['v1']['sooner'], 'kind': 'chime'}]
EV += SV.move_sounds(moves, lambda m: {'mode': 0.6, 'pan': 0.8, 'push': 0.8, 'pull': 1.0}[m['verb']])
EV.sort(key=lambda e: e['t'])
SIL = [round(M['m_mr']['t1'] + 0.5, 3), TOTAL]                       # MR1: lặng (không sfx/âm dữ liệu sau tiếng chạm); nhạc nền về 0 quanh MR1
assert all(e['t'] < SIL[0] - 0.4 for e in EV), 'sfx trong khoảng lặng MR1'
tension = [[0, 0.2]] + [[b['t0'], 0.2 + 0.5 * b['music']] for b in beats] + [[TOTAL, 0.0]]
errs = SV.check_rules(beats, moves, PAD, rule3=True)
errs = [e for e in errs if not e.startswith('quy tắc 7')]          # quy tắc 7 = 5 s đầu TẬP (đoạn A); đoạn B mở ở thế giới (ident tối dần)
spine = {'segment': 'ep005 C4 · B = S04–S09 (Hồi 1) + MR1', 'version': 5, 'total': TOTAL, 'fps': 30, 'pad': PAD, 'episode_t0': S.t0, 'scenes': S.scenes,
         'takes': S.takes, 'words': S.words, 'beats': beats, 'moves': moves, 'fly_fallback': FALLBACK, 'music_plan': K.music_plan(S),
         'mix': {'music_db': K.music_db(S), 'data_db': 25.0}, 'pay_kf': PAYK, 'flip': FLIP, 'k_stop': KSTOP, 'mr1_silence': SIL,
         'events': EV, 'tension': tension, 'shots': SV.shots_for(moves, TOTAL),
         'label_cues': {'p2.dollar': 'cost: not shown in this video', 'e0.four': '$400,000 home', 'e0.median': 'Q2 2026: $410,700', 'e1.ten': '$40,000 down', 'e1.loan': '$360,000 loan',
                        'y0.figure': '$2,362/month · principal + interest', 'y1.taxes': 'taxes, home insurance and PMI on top', 'y2.slowly': 'slowly at first',
                        'y2.faster': 'faster later', 'l0.eighty': '80% of original value = $320,000', 'l1.ninety': 'payment 99: may request',
                        'l2.conditions': 'conditions: written request · current on payments', 'a0.seventy': '78% = $312,000',
                        'a1.nine': 'payment 114 (9.5 years): ends automatically', 'a2.schedule': 'based on the schedule only',
                        'v1.sooner': '80% sooner, on paper', 'v1.paper': 'on paper: loan ÷ value by a price index', 'v2.request': "lender's rule: request · appraisal · minimum time"},
         'visual_cues': ['p0.twenty', 'p1.lender', 'p2.dollar', 'e0.four', 'e1.ten', 'e1.loan', 'y0.figure', 'y1.taxes', 'y2.each', 'y2.faster', 'l0.eighty', 'l1.ninety',
                         'l2.conditions', 'a0.seventy', 'a1.nine', 'a2.schedule', 'v0.value', 'v1.sooner', 'v1.paper', 'v2.request'],
         'checks': {'rule2_rule3': errs or 'OK', 'rule7': 'n/a (5 s đầu tập ở đoạn A)'}}
K.write(HERE, spine, ['episodes/ep005/world/claims.json', 'episodes/ep005/world/obj5.js', 'episodes/ep005/world/c4kit.js'])
print('total', TOTAL, 'moves', [(m['id'], m['t0'], m['t1'], m.get('style')) for m in moves]); print('silence', SIL, 'music_db', spine['mix']['music_db']); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
