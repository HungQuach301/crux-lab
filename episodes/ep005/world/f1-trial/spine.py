"""F-1 THỬ (BACKLOG F-1): bản sao của seg-s01-s03 — CHỈ khác: lần chuyển chế độ wFork→cSched (S02 "schedule") dùng kiểu 'fly'
(máy quay đi thật qua tư thế fPass, core.js flyPose); mọi mốc giờ, âm, nhãn giữ nguyên. Bản hoà tan: ../seg-s01-s03/.

Tập 5 · cold open S01.1 → S03.2 · PORT đoạn E5k (moc-v/seg/ep005/spine.py, spine v3 "một thế giới, hai chế độ máy quay", D-010).
  python3 episodes/ep005/world/seg-s01-s03/spine.py   → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Khác E5k: lời lấy từ take HIỆN TẠI của tập (review-g1/voice-scenes.json; S03 = take sinh lại 07/10, 220fafe7…), vị trí take
tính theo luật nhà máy (take + đuôi 1,0 s, wlib.episode_offsets) — không gõ tay; câu theo script.md (wlib.scene_words).
Nhịp, động tác, âm, nhãn: giữ nguyên E5k. S03 cắt sau S03.2.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import wlib                       # take + câu + đầu từ theo năng lượng (onset.refine)
import spine as SV                # spine v2 của nhà máy (toolkit/factory/world/spine.py)
ROOT = wlib.ROOT
PAD = 0.25
PRE = 0.4
OFF = wlib.episode_offsets()
TK = [('S01', ['S01.1', 'S01.2']), ('S02', ['S02.1', 'S02.2']), ('S03', ['S03.1', 'S03.2'])]
words, takes, lines = [], [], {}
for scene, sids in TK:
    W = wlib.scene_words(scene); off = OFF[scene]
    ws = [w for w in W['words'] if w['sid'] in sids]
    words += [{'w': x['w'], 's': round(float(x['s']) + off + PRE, 3), 'e': round(float(x['e']) + off + PRE, 3), 'sid': x['sid'], 's_tts': round(float(x['s_tts']) + off + PRE, 3)} for x in ws]
    lines.update({s: W['lines'][s] for s in sids})
    more = any(w['sid'] not in sids for w in W['words'])
    cut = round(float(ws[-1]['e']) + 0.25, 3) if more else None
    takes.append({'mp3': W['mp3'], 't': round(off + PRE, 3), 'cut': cut, 'take': W['hash']})
TOTAL = round(max(w['e'] for w in words) + 1.6, 2)


at = SV.Anchors(words).at


B = [
 ('c0', 'S01.1', 'world', 'Bạn đã để dành 10 % giá một căn nhà.', 'người xem (không mặt) cạnh căn nhà đứng trên chồng tiền MỜ = giá nhà; trong tay người xem một chồng nhỏ thật = 10 % chồng mờ.',
  {'saved': '@S01.1:saved', 'ten': '@S01.1:ten', 'price': '@S01.1:price'}, ['tick khi chồng nhỏ đặt xuống'], 0.30, 'tò mò, gần', 'ngã rẽ'),
 ('c1', 'S01.2', 'world', 'Mua ngay và trả bảo hiểm, hay thuê tiếp tới 20 %?', 'hai lối: khiên bảo hiểm rơi lên mái nhà (lúc "insurance"); bên kia căn hộ thuê, chồng của người xem lớn dần tới vạch 20 % mờ (lúc "twenty").',
  {'buy': '@S01.2:buy', 'insurance': '@S01.2:insurance', 'renting': '@S01.2:renting', 'twenty': '@S01.2:twenty'}, ['chạm khi khiên gắn', 'nốt đi lên khi chồng lớn'], 0.40, 'phân vân',
  'CHUYỂN CHẾ ĐỘ → đồ thị: "the schedule" là một đường theo thời gian'),
 ('c2', 'S02.1', 'chart', 'Theo lịch trả nợ, khoảng 8 năm mới được xin huỷ.', 'đồ thị: dư nợ ÷ giá từ 90 % đi xuống chậm, vạch 80 % cố định; đường chạm vạch ở ~8 năm (lúc "eight") + nhãn "about 8 years".',
  {'schedule': '@S02.1:schedule', 'cancel': '@S02.1:cancel', 'eight': '@S02.1:eight'}, ['âm dữ liệu: nốt theo năm', 'chạm ở 80 %'], 0.55, 'nặng, xa', 'phát lại thật'),
 ('c3', 'S02.2', 'chart', 'Phát lại giá và lãi thật từng tháng: bao lâu trên giấy, điển hình và chậm.', 'bó 307 đường mảnh (mỗi tháng mua một đường) hiện dần trái → phải (lúc "replayed"/"month"); đường điển hình sáng lúc "typically", đường chậm nhất warn lúc "slow".',
  {'replayed': '@S02.2:replayed', 'month': '@S02.2:month', 'paper': '@S02.2:paper', 'typically': '@S02.2:typically', 'slow': '@S02.2:slow'}, ['nốt dữ liệu mỗi 2 năm khi bó quét (cao độ = tỉ lệ trung vị)', 'nốt sáng (điển hình), nốt trầm (chậm)'], 0.65, 'hé lộ',
  'LIA MÁY sang định nghĩa "on paper"'),
 ('c4', 'S03.1', 'chart', '"Trên giấy" = khoản vay bằng 80 % giá trị nhà theo chỉ số giá quốc gia.', 'hai chồng chính diện: GIÁ TRỊ nhà (lớn theo chỉ số) và KHOẢN VAY (nhỏ dần); vạch 80 % của giá trị; khi chồng vay chạm vạch (lúc "eighty") → "80% on paper".',
  {'paper': '@S03.1:paper', 'eighty': '@S03.1:eighty', 'value': '@S03.1:value', 'index': '@S03.1:index'}, ['chạm khi hai chồng gặp vạch'], 0.55, 'hiểu định nghĩa',
  'CHUYỂN CHẾ ĐỘ → thế giới: "insurance removed" là chuyện của căn nhà'),
 ('c5', 'S03.2', 'world', 'Chạm 80 % trên giấy chưa phải là được gỡ bảo hiểm.', 'về căn nhà: khiên bảo hiểm VẪN ở trên mái dù chồng vay đã thấp; khiên rung nhẹ rồi đứng yên lúc "removed"; nhãn "insurance still on".',
  {'same': '@S03.2:same', 'removed': '@S03.2:removed'}, ['tiếng trầm có thân ở "removed" + nốt chốt', 'nhạc tắt ở "removed", hợp âm cuối'], 0.35, 'tỉnh táo', '(hết) giữ trạng thái kết luận ≥ 1 s'),
]
beats = SV.beats_from(B, SV.Anchors(words), lines)
cue = {b['id']: b['cues'] for b in beats}


window = lambda after, before, dur, late=False: SV.window(after, before, dur, PAD, late, eps=0.01)   # late: 'pan' giữ "slow cases" lâu hơn


MOVES = [
 ('pull', 'wYou', 'wFork', cue['c0']['price'], cue['c1']['buy'], 1.0, 'lời "Do you buy now … or keep renting": cần thấy cả hai lối (nhà và căn hộ) → lùi máy', 'whoosh_soft'),
 ('mode', 'wFork', 'cSched', cue['c1']['twenty'], cue['c2']['schedule'], 1.1, 'lời "On the schedule alone": lịch trả nợ là một đường theo thời gian → chế độ đồ thị', 'whoosh_mode'),
 ('pan', 'cSched', 'cDef', cue['c3']['slow'], cue['c4']['paper'], 1.0, 'lời "On paper means…": định nghĩa cần hai chồng đặt cạnh nhau → lia máy trong đồ thị', 'whoosh_push'),
 ('mode', 'cDef', 'wHouse', cue['c4']['index'], cue['c5']['same'], 0.9, 'lời "…getting the insurance removed": bảo hiểm gắn với căn nhà → chế độ thế giới', 'whoosh_mode'),
]
moves = []
for verb, a, b, after, before, dur, reason, snd in MOVES:
    t0, t1 = window(after, before, dur, late=(verb in ('pan', 'pull')))   # pull: trong khoảng nghỉ, sát câu hỏi
    moves.append({'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd})
FLY = {('wFork', 'cSched'): 'fPass'}   # F-1 thử trên MỘT lần chuyển: thế giới → đồ thị ở "schedule"; tư thế fPass khai ở scene.js
moves = [SV.with_style(m, 'fly', FLY[(m['from'], m['to'])]) if (m['from'], m['to']) in FLY else m for m in moves]

D = json.load(open(os.path.join(ROOT, 'episodes/ep005/work/world-data/derived.json')))
KT = next(k for k, l in enumerate(D['sched']) if l < 0.8 + 0.03)                # tháng đường còn RÕ trên vạch (bề dày dải ≈ 0,007)
SCHED = [[cue['c2']['schedule'], 0], [cue['c2']['eight'] - 0.15, KT], [cue['c2']['eight'], D['sched80']]]   # E5d: lơ lửng rồi CHẠM vạch đúng chữ "eight"   # chạm vạch ĐÚNG chữ "eight" (E5a: hình sớm hơn chime)
FAN = [[cue['c3']['replayed'], 0], [cue['c3']['paper'], 1]]                        # tỉ lệ bó đã hiện (theo tháng mua)
EV = []
for k in range(0, D['sched80'] + 1, 12):
    tk_ = next(ta + (tb - ta) * (k - xa) / (xb - xa) for (ta, xa), (tb, xb) in zip(SCHED, SCHED[1:]) if xa <= k <= xb)   # cùng lịch với hình
    EV.append({'t': round(tk_, 3), 'kind': 'data', 'v': (D['sched'][k] - 0.7) / 0.25})
EV += [{'t': cue['c0']['saved'], 'kind': 'tick', 'v': 0.5}, {'t': cue['c0']['ten'], 'kind': 'land', 'mode': False}, {'t': cue['c0']['price'], 'kind': 'rise', 'dur': 0.9},   # E5f: âm cho chồng đặt xuống / trượt vào / tháp mọc
       {'t': cue['c1']['insurance'], 'kind': 'land', 'mode': False},
       {'t': cue['c1']['twenty'], 'kind': 'rise', 'dur': 0.9},
       {'t': cue['c2']['eight'], 'kind': 'chime'},
       *[{'t': round(FAN[0][0] + (FAN[1][0] - FAN[0][0]) * y / 10, 3), 'kind': 'data', 'v': max(0.0, (sorted(p['p'][min(len(p['p']) - 1, 12 * y)] for p in D['paths'])[len(D['paths']) // 2] - 0.7) / 0.4)} for y in range(0, 11, 2)],   # E5f: phát lại có nốt (cao độ = tỉ lệ trung vị năm đó)
       {'t': cue['c3']['typically'], 'kind': 'data', 'v': 0.8},
       {'t': cue['c3']['slow'], 'kind': 'data', 'v': 0.2},
       {'t': cue['c4']['eighty'], 'kind': 'chime'},
       {'t': cue['c5']['removed'], 'kind': 'impact'}]   # E5e: chốt rõ hơn (tiếng trầm có thân)
GAIN = {'mode': 0.6, 'pan': 0.8, 'pull': 1.0}                 # bài học Tập 4 v3d: whoosh_mode quá to; chỉ đổi chế độ mới có tiếng chạm
EV += SV.move_sounds(moves, lambda m: GAIN[m['verb']])
EV.sort(key=lambda e: e['t'])
TEN = {'c0': 0.3, 'c1': 0.45, 'c2': 0.6, 'c3': 0.8, 'c4': 0.65, 'c5': 0.4}   # E5c: biên độ rộng hơn (đạo diễn: nhạc phẳng)
tension = [[0, 0.15]] + [[b['t0'], TEN[b['id']]] for b in beats] + [[TOTAL - 1.5, 0.25], [TOTAL, 0.1]]
shots = SV.shots_for(moves, TOTAL)
errs = SV.check_rules(beats, moves, PAD)
spine = {'segment': 'ep005 S01.1 → S03.2 (cold open) · F-1 thử: wFork→cSched kiểu fly', 'version': 3, 'total': TOTAL, 'fps': 30, 'pad': PAD, 'takes': takes, 'words': words,
         'beats': beats, 'moves': moves,
         'music_plan': {'stop': cue['c5']['removed'], 'tau': 0.15, 'release': cue['c5']['removed'] + 1.0, 'accents': [cue['c2']['eight'], cue['c4']['eighty'], cue['c5']['removed'] + 0.05]},
         'marks': {'ten_lit': round(at('@S01.1$') + 0.25, 3)},   # 10 % đáy chồng giá sáng trong khoảng nghỉ (móc 5 s đầu)
         'mix': {'music_db': 17.0, 'data_db': 25.0},   # E5g: nhạc nghe được hơn, nốt dữ liệu không đè lời
         'sched_kf': SCHED, 'fan_kf': FAN, 'events': EV, 'tension': tension, 'shots': shots,   # nhạc tắt ở "removed": kết bằng lặng + tiếng trầm
         'label_cues': {'c2.eight': 'about 8 years', 'c3.typically': 'typical ≈ 2 years', 'c3.slow': 'slowest case ≈ 9 years', 'c4.eighty': '80% on paper', 'c4.paper': '90%', 'c5.removed': 'insurance still on'},
         'visual_cues': ['c0.ten', 'c1.insurance', 'c1.twenty', 'c2.schedule', 'c2.eight', 'c3.replayed', 'c3.typically', 'c3.slow', 'c4.paper', 'c4.eighty', 'c5.removed'],
         'checks': {'rule2_rule3_rule7': errs or 'OK'}}
json.dump(spine, open(os.path.join(HERE, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(['episodes/ep005/world/claims.json', 'episodes/ep005/work/world-data/derived.json'], open(os.path.join(HERE, 'inputs.json'), 'w'))
print('total', TOTAL, 'moves', [(m['verb'], m['t0'], m['t1']) for m in moves]); print({b['id']: b['cues'] for b in beats}); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
