"""Tập 5 · C4 · ĐOẠN A = S01–S03 + ident (cold open, Hồi "cold-open"). Cảnh S01.1 → S03.2: PORT seg-s01-s03 (E5k, đã duyệt C3) + F-1 thử
(wFork→cSched bay qua fPass); thêm S03.3–S03.5 + ident 3 s theo SPINE-PLAN; lời + giờ = timeline của nhà máy (c4kit.Seg, 0 ký tự EL).
  python3 episodes/ep005/world/c4/a-s01-s03/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Khác seg-s01-s03: không lùi lời 0,4 s (take đặt đúng như master); mọi chuyển chế độ kiểu 'fly' (F-1) với tư thế via riêng; nhạc = lát nhạc nền F-3.
S03.3: về đồ thị định nghĩa — vạch 75 % hạ dưới vạch 80 % ở "seventy-five", nhãn B+2 `Fannie Mae: wait ≥ 2 years · loan ≤ 75%` ở "bar".
S03.4: ba người mua (W4 + W1 trên W2) — ILLUSTRATIVE. S03.5: `US only · history, not a forecast` ở "history", đối trọng ở "buy". Ident: dấu kênh,
thế giới tối dần (đoạn B mở từ tối) — ranh giới đoạn không cần khớp khung."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); W5 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W5)
import c4kit as K
import spine as SV
S = K.Seg(['S01', 'S02', 'S03'])
TOTAL, at, PAD = S.total, S.at, K.PAD
words = S.words

B = [
 ('c0', 'S01.1', 'world', 'Bạn đã để dành 10 % giá một căn nhà.', 'người xem cạnh căn nhà trên chồng giá; chồng nhỏ = 10 %.',
  {'saved': '@S01.1:saved', 'ten': '@S01.1:ten', 'price': '@S01.1:price'}, ['tick', 'land', 'rise'], 0.30, 'tò mò', 'ngã rẽ'),
 ('c1', 'S01.2', 'world', 'Mua ngay và trả bảo hiểm, hay thuê tiếp tới 20 %?', 'khiên rơi lên mái ("insurance"); căn hộ thuê, chồng lớn tới 20 % ("twenty").',
  {'buy': '@S01.2:buy', 'insurance': '@S01.2:insurance', 'renting': '@S01.2:renting', 'twenty': '@S01.2:twenty'}, ['land', 'rise'], 0.40, 'phân vân',
  'CHUYỂN CHẾ ĐỘ → đồ thị (bay qua căn hộ)'),
 ('c2', 'S02.1', 'chart', 'Theo lịch trả nợ, khoảng 8 năm mới được xin huỷ.', 'dư nợ ÷ giá từ 90 % chạm vạch 80 % ở "eight".',
  {'schedule': '@S02.1:schedule', 'cancel': '@S02.1:cancel', 'eight': '@S02.1:eight'}, ['data', 'chime'], 0.55, 'nặng', 'phát lại'),
 ('c3', 'S02.2', 'chart', 'Phát lại giá và lãi thật từng tháng.', 'bó 307 đường; điển hình ("typically"), chậm nhất ("slow").',
  {'replayed': '@S02.2:replayed', 'month': '@S02.2:month', 'paper': '@S02.2:paper', 'typically': '@S02.2:typically', 'slow': '@S02.2:slow'}, ['data'], 0.65, 'hé lộ', 'lia'),
 ('c4', 'S03.1', 'chart', '"Trên giấy" = khoản vay bằng 80 % giá trị nhà theo chỉ số.', 'hai chồng chính diện; "80% on paper" ở "eighty".',
  {'paper': '@S03.1:paper', 'eighty': '@S03.1:eighty', 'value': '@S03.1:value', 'index': '@S03.1:index'}, ['chime'], 0.55, 'hiểu',
  'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('c5', 'S03.2', 'world', 'Chạm 80 % trên giấy chưa phải là được gỡ bảo hiểm.', 'khiên VẪN trên mái; "insurance still on".',
  {'same': '@S03.2:same', 'removed': '@S03.2:removed'}, ['impact'], 0.40, 'tỉnh táo', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c6', 'S03.3', 'chart', 'Gỡ theo giá trị hôm nay là luật của chủ khoản vay; Fannie Mae: chờ + vạch 75 %.', 'đồ thị định nghĩa: vạch 75 % hạ dưới vạch 80 % ("seventy-five"); nhãn B+2 ("bar").',
  {'removal': '@S03.3:Removal', 'rule': '@S03.3:rule', 'fannie': '@S03.3:Fannie', 'seventy': '@S03.3:seventy', 'bar': '@S03.3:bar'}, ['slide_down', 'tick'], 0.50, 'chính xác',
  'CHUYỂN CHẾ ĐỘ → thế giới: ba người mua'),
 ('c7', 'S03.4', 'world', 'Ba người mua minh hoạ, ba câu trả lời khác nhau.', 'ba người không mặt cạnh ba căn nhà ("three").',
  {'three': '@S03.4:three', 'buyers': '@S03.4:buyers', 'different': '@S03.4:different'}, ['rise'], 0.45, 'mở', 'giữ'),
 ('c8', 'S03.5', 'world', 'Chỉ Mỹ, lịch sử, không dự báo; không khuyên mua hay chờ.', 'lớp bắt buộc + đối trọng cố định.',
  {'us': '@S03.5:U', 'history': '@S03.5:history', 'buy': '@S03.5:buy', 'wait': '@S03.5:wait'}, [], 0.30, 'bình thản', 'ident'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
IDENT = [round(S.end['S03'] - 3.0, 3), S.end['S03']]          # 3 s cuối S03 (đuôi): dấu kênh, thế giới tối dần → đoạn B mở từ tối

w = K.window
MOVES = [   # (id, verb, from, to, after, before, dur, reason, sound, late, via)
 ('m_pull', 'pull', 'wYou', 'wFork', cue['c0']['price'], cue['c1']['buy'], 1.0, 'lời "Do you buy now … or keep renting": cần thấy cả hai lối → lùi máy', 'whoosh_soft', True, None),
 ('m_c2', 'mode', 'wFork', 'cSched', cue['c1']['twenty'], cue['c2']['schedule'], 1.1, 'lời "On the schedule alone": lịch trả nợ là một đường theo thời gian → đồ thị', 'whoosh_mode', False, 'fPass'),
 ('m_pan', 'pan', 'cSched', 'cDef', cue['c3']['slow'], cue['c4']['paper'], 1.0, 'lời "On paper means…": định nghĩa cần hai chồng cạnh nhau → lia', 'whoosh_push', True, None),
 ('m_c5', 'mode', 'cDef', 'wHouse', cue['c4']['index'], cue['c5']['same'], 0.9, 'lời "…getting the insurance removed": bảo hiểm gắn với căn nhà → thế giới', 'whoosh_mode', False, 'fHome'),
 ('m_c6', 'mode', 'wHouse', 'cDef75', cue['c6']['removal'], cue['c6']['rule'], 1.1, 'lời "the loan owner\'s rule … a 75 percent bar": mức cố định thứ hai trên đúng đồ thị định nghĩa → đồ thị', 'whoosh_mode', False, 'fRule'),
 ('m_c7', 'mode', 'cDef75', 'wBuyers', cue['c6']['bar'], cue['c7']['three'], 1.1, 'lời "three illustrative buyers": là người → thế giới', 'whoosh_mode', False, 'fMeet'),
]
moves = []
for mid, verb, a, b, after, before, dur, reason, snd, late, via in MOVES:
    t0, t1 = w(after, before, dur, late=late)
    moves.append({'id': mid, 'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd, 'via': via})
FALLBACK = {}   # id → lý do giữ hoà tan (F-1 trượt quy tắc / F-2 / che > 60 % > 0,3 s)
moves = K.fly(moves, FALLBACK)

D = json.load(open(os.path.join(K.ROOT, 'episodes/ep005/work/world-data/derived.json')))
KT = next(k for k, l in enumerate(D['sched']) if l < 0.8 + 0.03)
SCHED = [[cue['c2']['schedule'], 0], [cue['c2']['eight'] - 0.15, KT], [cue['c2']['eight'], D['sched80']]]
FAN = [[cue['c3']['replayed'], 0], [cue['c3']['paper'], 1]]
EV = []
for k in range(0, D['sched80'] + 1, 12):
    tk_ = next(ta + (tb - ta) * (k - xa) / (xb - xa) for (ta, xa), (tb, xb) in zip(SCHED, SCHED[1:]) if xa <= k <= xb)
    EV.append({'t': round(tk_, 3), 'kind': 'data', 'v': (D['sched'][k] - 0.7) / 0.25})
EV += [{'t': cue['c0']['saved'], 'kind': 'tick', 'v': 0.5}, {'t': cue['c0']['ten'], 'kind': 'land', 'mode': False}, {'t': cue['c0']['price'], 'kind': 'rise', 'dur': 0.9},
       {'t': cue['c1']['insurance'], 'kind': 'land', 'mode': False}, {'t': cue['c1']['twenty'], 'kind': 'rise', 'dur': 0.9}, {'t': cue['c2']['eight'], 'kind': 'chime'},
       *[{'t': round(FAN[0][0] + (FAN[1][0] - FAN[0][0]) * y / 10, 3), 'kind': 'data', 'v': max(0.0, (sorted(p['p'][min(len(p['p']) - 1, 12 * y)] for p in D['paths'])[len(D['paths']) // 2] - 0.7) / 0.4)} for y in range(0, 11, 2)],
       {'t': cue['c3']['typically'], 'kind': 'data', 'v': 0.8}, {'t': cue['c3']['slow'], 'kind': 'data', 'v': 0.2},
       {'t': cue['c4']['eighty'], 'kind': 'chime'}, {'t': cue['c5']['removed'], 'kind': 'impact'},
       {'t': cue['c6']['seventy'], 'kind': 'slide_down', 'dur': 0.5},
       {'t': cue['c7']['three'], 'kind': 'rise', 'dur': 0.8},
       {'t': round(IDENT[0] + 0.2, 3), 'kind': 'gather'}]
GAIN = {'mode': 0.6, 'pan': 0.8, 'pull': 1.0}
EV += SV.move_sounds(moves, lambda m: GAIN[m['verb']])
EV.sort(key=lambda e: e['t'])
TEN = {'c0': 0.3, 'c1': 0.45, 'c2': 0.6, 'c3': 0.8, 'c4': 0.65, 'c5': 0.4, 'c6': 0.5, 'c7': 0.45, 'c8': 0.3}
tension = [[0, 0.15]] + [[b['t0'], TEN[b['id']]] for b in beats] + [[IDENT[0], 0.2], [TOTAL, 0.1]]
errs = SV.check_rules(beats, moves, PAD)
spine = {'segment': 'ep005 C4 · A = S01–S03 + ident (cold open: port E5k/seg-s01-s03 + F-1, S03.3–S03.5 mới)', 'version': 5, 'total': TOTAL, 'fps': 30, 'pad': PAD,
         'episode_t0': S.t0, 'scenes': S.scenes, 'takes': S.takes, 'words': words, 'beats': beats, 'moves': moves, 'fly_fallback': FALLBACK,
         'music_plan': K.music_plan(S), 'marks': {'ten_lit': round(at('@S01.1$') + 0.25, 3)}, 'ident': IDENT,
         'mix': {'music_db': K.music_db(S), 'data_db': 25.0},
         'sched_kf': SCHED, 'fan_kf': FAN, 'events': EV, 'tension': tension, 'shots': SV.shots_for(moves, TOTAL),
         'label_cues': {'c2.eight': 'about 8 years', 'c3.typically': 'typical ≈ 2 years', 'c3.slow': 'slowest case ≈ 9 years', 'c4.eighty': '80% on paper', 'c4.paper': '90%',
                        'c5.removed': 'insurance still on', 'c6.rule': "loan owner's rule", 'c6.bar': 'Fannie Mae: wait ≥ 2 years · loan ≤ 75%',
                        'c8.history': 'US only · history, not a forecast', 'c8.buy': "It won't say whether to buy or wait"},
         'visual_cues': ['c0.ten', 'c1.insurance', 'c1.twenty', 'c2.schedule', 'c2.eight', 'c3.replayed', 'c3.typically', 'c3.slow', 'c4.paper', 'c4.eighty', 'c5.removed',
                         'c6.rule', 'c6.seventy', 'c6.bar', 'c7.three', 'c8.history', 'c8.buy'],
         'checks': {'rule2_rule3_rule7': errs or 'OK'}}
K.write(HERE, spine, ['episodes/ep005/world/claims.json', 'episodes/ep005/work/world-data/derived.json', 'episodes/ep005/world/c4kit.js'])
print('total', TOTAL, 'moves', [(m['id'], m['t0'], m['t1'], m.get('style')) for m in moves]); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
