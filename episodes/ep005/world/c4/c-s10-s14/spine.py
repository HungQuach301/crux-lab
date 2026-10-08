"""Tập 5 · C4 · ĐOẠN C = S10–S14 (Hồi 2: phát lại). Mở ở phố (khung cuối đoạn B, c4kit.Street), kết ở ba người mua (khung đầu đoạn D, c4kit.Buyers).
  python3 episodes/ep005/world/c4/c-s10-s14/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
SPINE-PLAN §1 S10–S14; N3 gập (code C3 vòng 1), N2 cột (code C3 vòng 3) — cột đứng trên MỘT mặt đất (y = 0) cho cả N3 lẫn N2 (ghi chú khuôn C3).
Khác SPINE-PLAN (cửa sổ < 0,6 s theo giờ take thật): S12 về đồ thị sau "We also checked a larger" (giữa "paper" và "larger"); S14 về thế giới
giữa "rate" và "national"; S14→S15 'pan' về ba người mua nằm trong đuôi S14 (ranh giới đoạn C|D ở thế đứng yên)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); W5 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W5)
import c4kit as K
import spine as SV
S = K.Seg(['S10', 'S11', 'S12', 'S13', 'S14'])
TOTAL, PAD = S.total, K.PAD
B = [
 ('r0', 'S10.1', 'world', 'Mọi tháng mua từ 1/1991 tới 7/2016.', 'phố: mỗi nhà = một tháng mua, sáng dần trái → phải.',
  {'every': '@S10.1:every', 'month': '@S10.1:month', 'sixteen': '@S10.1:sixteen'}, ['tick'], 0.35, 'mở', 'lia'),
 ('r1', 'S10.2', 'world', 'Cùng khoản vay 10 %, lãi tháng đó.', 'khối trả trước trước mỗi nhà.', {'same': '@S10.2:same', 'loan': '@S10.2:loan', 'rate': '@S10.2:rate'}, [], 0.4, '', ''),
 ('r2', 'S10.3', 'world', 'Giá trị nhà đi theo chỉ số giá quốc gia.', 'đường chỉ số (accent) vẽ ngang phố.', {'value': '@S10.3:value', 'index': '@S10.3:index'}, ['data'], 0.45, '', 'đẩy máy'),
 ('r3', 'S10.4', 'world', 'Mỗi tháng so dư nợ với giá trị; dừng đồng hồ lần đầu ≤ 80 %.', 'N3: nhà trên chồng giá trị, chồng vay, vạch 80 %, lịch ngừng ở "less".',
  {'every': '@S10.4:Every', 'compare': '@S10.4:compare', 'value': '@S10.4:value', 'stop': '@S10.4:stop', 'eighty': '@S10.4:eighty', 'less': '@S10.4:less'}, ['tick', 'chime'], 0.5, 'chú ý',
  'CHUYỂN CHẾ ĐỘ → đồ thị: "Each bar here"'),
 ('r4', 'S10.5', 'chart', 'Mỗi cột một tháng mua; chiều cao = bao lâu.', 'N3: 307 đường gập thành 307 cột.', {'bar': '@S10.5:bar', 'month': '@S10.5:month', 'height': '@S10.5:height'}, ['swish', 'rise'], 0.55, 'hé lộ', ''),
 ('t0', 'S11.1', 'chart', 'Điển hình: 23 tháng.', 'vạch trung vị thấp.', {'typical': '@S11.1:typical', 'twenty': '@S11.1:twenty'}, ['chime'], 0.7, 'đỉnh', ''),
 ('t1', 'S11.2', 'chart', 'Nửa sớm hơn, nửa lâu hơn.', 'cột dưới/trên vạch đổi sáng.', {'half': '@S11.2:Half', 'longer': '@S11.2:longer'}, [], 0.65, '', ''),
 ('t2', 'S11.3', 'chart', '90,6 % không muộn hơn lịch.', 'sống lịch (muted) trên cột.', {'ninety': '@S11.3:ninety', 'schedule': '@S11.3:schedule'}, ['data'], 0.7, '', ''),
 ('t3', 'S11.4', 'chart', 'Khoảng cách giữa đường dài của lịch và điển hình.', 'ngoặc khoảng giữa sống lịch và trung vị.', {'gap': '@S11.4:gap', 'one': '@S11.4:one'}, [], 0.6, '',
  'CHUYỂN CHẾ ĐỘ → thế giới: "But that\'s on paper"'),
 ('k0', 'S12.1', 'world', 'Nhưng đó là trên giấy.', 'nhà, khiên vẫn trên mái.', {'paper': '@S12.1:paper'}, [], 0.45, 'tỉnh', 'CHUYỂN CHẾ ĐỘ → đồ thị (tập lớn hơn)'),
 ('k1', 'S12.2', 'chart', '403 tháng mua có 2 năm giá sau đó.', 'cột tập A (nợ ÷ giá trị ở 24 tháng).', {'larger': '@S12.2:larger', 'two': '@S12.2:two'}, [], 0.5, '', ''),
 ('k2', 'S12.3', 'chart', 'Hai năm sau mua chỉ 15,6 % ≤ 75 %.', 'lát mỏng dưới vạch 75 %.', {'fifteen': '@S12.3:fifteen', 'seventy': '@S12.3:seventy', 'fannie': '@S12.3:Fannie'}, ['chime'], 0.6, '', ''),
 ('k3', 'S12.4', 'chart', '80 % trong ~2 năm phổ biến; vạch sớm thì không.', '', {'common': '@S12.4:common', 'early': '@S12.4:early', 'not': '@S12.4:not'}, [], 0.55, '',
  'CHUYỂN CHẾ ĐỘ → thế giới: dãy cột nhìn nghiêng'),
 ('n0', 'S13.1', 'world', 'Điển hình che một đuôi dài.', 'N2: dãy cột nhìn nghiêng; đuôi nhô lên.', {'typical': '@S13.1:typical', 'tail': '@S13.1:tail'}, ['rise'], 0.6, 'bất ngờ', ''),
 ('n1', 'S13.2', 'world', 'Khoảng 1/7 mất hơn 5 năm.', '', {'seven': '@S13.2:seven', 'five': '@S13.2:five', 'years': '@S13.2:years'}, ['chime'], 0.75, '', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('n2', 'S13.3', 'chart', 'Nằm liền nhau quanh đợt giảm giá.', 'N2: ngoặc cụm; dải chỉ số; đỉnh→đáy.',
  {'together': '@S13.3:together', 'stretch': '@S13.3:stretch', 'national': '@S13.3:national', 'slump': '@S13.3:slump'}, ['tick', 'slide_down'], 0.85, 'đỉnh', 'đẩy máy'),
 ('z0', 'S14.1', 'chart', 'Chậm nhất: 10/2005, 112 tháng.', 'khung phóng dừng ở cột cao nhất.', {'october': '@S14.1:October', 'months': '@S14.1:months'}, ['chime'], 0.8, '', ''),
 ('z1', 'S14.2', 'chart', 'Lâu hơn lịch ở lãi tháng đó.', 'vạch lịch 90 kỳ cắt ngang cột; sống lịch của mọi tháng.', {'schedule': '@S14.2:schedule', 'rate': '@S14.2:rate'}, [], 0.7, '', 'giữ (r2)'),
 ('z2', 'S14.3', 'chart', 'Trung bình quốc gia; địa phương khác.', 'r2: GIỮ khung cột cao nhất; tên "national average, not one home".',
  {'national': '@S14.3:national', 'single': '@S14.3:single', 'local': '@S14.3:local'}, [], 0.5, '', ''),
 ('z3', 'S14.4', 'chart', 'Vì sao cùng luật lại khác nhau?', '', {'rule': '@S14.4:rule', 'answers': '@S14.4:answers'}, [], 0.45, 'câu hỏi', 'CHUYỂN CHẾ ĐỘ → thế giới: ba người mua'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
w = K.window
MOVES = [
 ('m_pan', 'pan', 'wStreet', 'wStreetR', cue['r0']['sixteen'], cue['r1']['same'], 0.9, 'lời "For each one, we set up the same … loan": đi dọc phố, từng tháng mua → lia', 'whoosh_push', True, None),
 ('m_push', 'push', 'wStreetR', 'wReplay', cue['r2']['index'], cue['r3']['every'], 1.0, 'lời "Every month after that, we compare…": một tháng mua cụ thể → đẩy máy', 'whoosh_push', True, None),
 ('m_fold', 'mode', 'wReplay', 'cBarsT', cue['r3']['less'], cue['r4']['bar'], 1.1, 'lời "Each bar here is one purchase month": mọi tháng mua trên một biểu đồ → đồ thị', 'whoosh_mode', False, 'fFold'),
 ('m_but', 'mode', 'cBarsT', 'wHouse', cue['t3']['one'], cue['k0']['paper'], 1.0, 'lời "But that\'s on paper": về căn nhà, khiên vẫn trên mái → thế giới', 'whoosh_mode', False, 'fBut'),
 ('m_tally', 'mode', 'wHouse', 'cTally', cue['k0']['paper'], cue['k1']['larger'], 1.1, 'lời "We also checked a larger set": 403 cột là số → đồ thị', 'whoosh_mode', True, 'fTally'),
 ('m_row', 'mode', 'cTally', 'wRow', cue['k3']['not'], cue['n0']['typical'], 1.1, 'lời "The typical case also hides a long tail": dãy cột nhìn nghiêng, đuôi nhô lên → thế giới', 'whoosh_mode', False, 'fRow'),
 ('m_bars', 'mode', 'wRow', 'cBars', cue['n1']['seven'], cue['n1']['five'], 1.0, 'lời "took more than five years": ngưỡng 60 tháng là số → đồ thị', 'whoosh_mode', False, 'fFive'),
 ('m_zoom', 'push', 'cBars', 'cZoom', cue['n2']['slump'], cue['z0']['october'], 0.9, 'lời "The slowest was October 2005": khung phóng vào cột cao nhất → đẩy máy', 'whoosh_push', False, None),
 # C4 r2: bỏ cảnh khu nhiều nhà (S14.3, wHood) — vòng 1 khung 4–6 trôi sang nhà, người đọc mất cột cao nhất; khung GIỮ ở cột cao nhất tới hết S14
 ('m_buy', 'mode', 'cZoom', 'wBuyers', cue['z3']['answers'], TOTAL, 1.2, 'lời "why did the same rule give such different answers?": câu trả lời là ba người mua → thế giới', 'whoosh_mode', False, 'fBuy'),
]
moves = []
for mid, verb, a, b, after, before, dur, reason, snd, late, via in MOVES:
    t0, t1 = w(after, before, dur, late=late)
    moves.append({'id': mid, 'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd, 'via': via})
FALLBACK = {}
moves = K.fly(moves, FALLBACK)
M = {m['id']: m for m in moves}
D = json.load(open(os.path.join(K.ROOT, 'episodes/ep005/work/world-data/derived.json')))
G = D['buyers']['grace']
MK = [[cue['r3']['every'], 0], [cue['r3']['less'], G['hit']]]
FOLD = [cue['r4']['bar'], round(cue['r4']['bar'] + 1.2, 3)]
IX = [x for x in D['index'] if x['m'] <= D['bars'][-1]['m']]
DRAW = [round(cue['n2']['stretch'] + 0.5, 3), cue['n2']['national']]
LIT = [cue['r0']['every'], cue['r0']['sixteen']]                       # S10.1: nhà sáng dần trái → phải
EV = [{'t': round(LIT[0] + (LIT[1] - LIT[0]) * i / 6, 3), 'kind': 'tick', 'v': 0.3 + 0.05 * i} for i in range(0, 7, 2)]
EV += [{'t': round(cue['r2']['index'] - 0.6 + 0.3 * i, 3), 'kind': 'data', 'v': 0.3 + 0.15 * i} for i in range(3)]
EV += [{'t': round(MK[0][0] + (MK[1][0] - MK[0][0]) * k / G['hit'], 3), 'kind': 'tick', 'v': 0.3} for k in range(4, G['hit'], 4)]
EV += [{'t': cue['r3']['less'], 'kind': 'chime'}, {'t': FOLD[0], 'kind': 'swish', 'to': FOLD[1]}, {'t': cue['r4']['height'], 'kind': 'rise', 'dur': 0.6},
       {'t': cue['t0']['twenty'], 'kind': 'chime'}, {'t': cue['t2']['ninety'], 'kind': 'data', 'v': 0.8},
       {'t': cue['k2']['fifteen'], 'kind': 'chime'}, {'t': cue['n0']['tail'], 'kind': 'rise', 'dur': 0.8}, {'t': cue['n1']['years'], 'kind': 'chime'},
       {'t': cue['n2']['together'], 'kind': 'tick', 'v': 0.6}, {'t': cue['n2']['slump'], 'kind': 'slide_down', 'dur': 0.6}, {'t': cue['z0']['october'], 'kind': 'chime'}]
vmin, vmax = min(x['v'] for x in IX), max(x['v'] for x in IX)
for i in range(0, len(IX), 48):
    EV.append({'t': round(DRAW[0] + (DRAW[1] - DRAW[0]) * i / (len(IX) - 1), 3), 'kind': 'data', 'v': round((IX[i]['v'] - vmin) / (vmax - vmin), 3)})
EV += SV.move_sounds(moves, lambda m: {'mode': 0.6, 'pan': 0.8, 'push': 0.8, 'pull': 1.0}[m['verb']])
EV.sort(key=lambda e: e['t'])
tension = [[0, 0.3]] + [[b['t0'], 0.2 + 0.6 * b['music']] for b in beats] + [[TOTAL, 0.3]]
errs = [e for e in SV.check_rules(beats, moves, PAD) if not e.startswith('quy tắc 7')]
spine = {'segment': 'ep005 C4 · C = S10–S14 (Hồi 2: phát lại)', 'version': 5, 'total': TOTAL, 'fps': 30, 'pad': PAD, 'episode_t0': S.t0, 'scenes': S.scenes,
         'takes': S.takes, 'words': S.words, 'beats': beats, 'moves': moves, 'fly_fallback': FALLBACK, 'music_plan': K.music_plan(S),
         'mix': {'music_db': K.music_db(S), 'data_db': 25.0}, 'month_kf': MK, 'fold': FOLD, 'index_draw': DRAW, 'lit': LIT,
         'events': EV, 'tension': tension, 'shots': SV.shots_for(moves, TOTAL),
         'label_cues': {'r0.every': 'every purchase month', 'r1.loan': "same loan, that month's rate", 'r2.index': 'national home price index',
                        'r3.compare': 'loan', 'r3.value': 'home value', 'r4.height': 'height = months to 80% on paper',
                        't0.twenty': 'median: 23 months on paper', 't2.ninety': '90.6% no later than the schedule', 't2.schedule': "schedule at each month's rate",
                        't3.gap': 'gap', 'k0.paper': 'insurance still on', 'k1.larger': 'at 24 months · 403 purchase months, January 1991 to July 2024',
                        'k1.two': 'at or under 80%: 58.6%', 'k2.fifteen': 'at or under 75%: 15.6%', 'k2.fannie': "Fannie Mae's early bar",
                        'n0.tail': 'a long tail', 'n1.years': 'more than 60 months:', 'n2.stretch': 'one stretch of purchase months', 'n2.slump': 'national price slump',
                        'z0.october': 'October 2005: 112 months (9 yr 4 mo)', 'z1.schedule': 'schedule at that rate: 90 payments', 'z2.single': 'national average, not one home'},
         'visual_cues': ['r0.every', 'r1.loan', 'r2.index', 'r3.compare', 'r3.value', 'r3.less', 'r4.bar', 'r4.height', 't0.twenty', 't1.half', 't2.ninety', 't2.schedule', 't3.gap',
                         'k0.paper', 'k1.larger', 'k1.two', 'k2.fifteen', 'k2.fannie', 'n0.tail', 'n1.years', 'n2.together', 'n2.stretch', 'n2.slump', 'z0.october',
                         'z1.schedule', 'z2.single'],
         'checks': {'rule2_rule3': errs or 'OK', 'rule7': 'n/a (5 s đầu tập ở đoạn A)'}}
K.write(HERE, spine, ['episodes/ep005/world/claims.json', 'episodes/ep005/work/world-data/derived.json', 'episodes/ep005/world/obj5.js', 'episodes/ep005/world/c4kit.js'])
print('total', TOTAL, 'moves', [(m['id'], m['t0'], m['t1'], m.get('style')) for m in moves]); print('music_db', spine['mix']['music_db']); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
