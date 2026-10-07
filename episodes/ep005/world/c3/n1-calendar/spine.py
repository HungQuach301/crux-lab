"""Tập 5 · C3 · N1 LỊCH TRẢ NỢ trong ngữ cảnh — lời thật S06.1 + S06.3 (bỏ S06.2 để đoạn ≤ 15 s; ghi trong SPINE-PLAN).
  python3 episodes/ep005/world/c3/n1-calendar/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: người vay cạnh căn nhà, lịch đứng cạnh người; "monthly" = lật một trang. → ĐỒ THỊ (lời "the figure on screen": con số chỉ ở đồ thị):
chip "$2,362/month · principal + interest" gắn vào lịch; S06.3 lịch lật từng kỳ, chồng vay trượt theo thời gian, đỉnh chồng vẽ đường dư nợ
(chậm lúc đầu, nhanh về sau)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W5 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W5)
import wlib            # take hiện tại, cắt theo câu, đầu từ theo năng lượng
import spine as SV     # spine v2 nhà máy
PAD = 0.25
words, takes, lines, end = wlib.clip_voice([['S06.1'], ['S06.3']], lead=0.4, gap_same=0.4)
TOTAL = round(end + 0.75, 2)
A = SV.Anchors(words)
B = [
 ('a0', 'S06.1', 'world', 'Lãi tháng 9 và khoản trả mỗi tháng (vốn + lãi) của khoản vay minh hoạ.', 'người vay, căn nhà, lịch đứng; "monthly" lật một trang (một kỳ trả). Chuyển sang đồ thị trước "figure": chip $2,362 gắn vào lịch.',
  {'rate': '@S06.1:rate', 'monthly': '@S06.1:monthly', 'payment': '@S06.1:payment', 'figure': '@S06.1:figure'}, ['tick khi lật trang', 'chạm khi chip gắn'], 0.35, 'bình thản', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S06.3', 'chart', 'Mỗi kỳ trả giảm dư nợ một chút: chậm lúc đầu, nhanh về sau.', 'lịch lật liên tục; chồng vay (W2) trượt sang phải theo số kỳ, đỉnh chồng vẽ đường dư nợ (W5); "slowly" đường gần như nằm ngang, "faster" dốc xuống.',
  {'each': '@S06.3:Each', 'slowly': '@S06.3:slowly', 'faster': '@S06.3:faster', 'later': '@S06.3:later'}, ['nốt dữ liệu mỗi 5 năm (cao độ = dư nợ)'], 0.5, 'hiểu cơ chế', '(hết) giữ ≥ 1 s'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = []
for verb, a, b, after, before, dur, reason, snd in [
        ('mode', 'wDesk', 'cPay', cue['a0']['payment'], cue['a0']['figure'], 1.1, 'lời "the figure on screen": con số khoản trả chỉ hiện ở chế độ đồ thị (quy tắc 1) → đồ thị', 'whoosh_mode')]:
    t0, t1 = SV.window(after, before, dur, PAD, eps=0.01)
    moves.append({'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd})
# lịch trả nợ: kỳ k theo thời gian (0 lúc "Each" → 360 sau "later")
PAYK = [[cue['a1']['each'], 0], [cue['a1']['slowly'], 120], [cue['a1']['faster'], 240], [cue['a1']['later'] + 0.6, 360]]
D = json.load(open(os.path.join(wlib.ROOT, 'episodes/ep005/world/claims.json')))
r = D['rate_latest']['value'] / 1200
bal = lambda k: (1 + r) ** k - ((1 + r) ** k - 1) / (1 - (1 + r) ** -360)        # dư nợ / khoản vay ban đầu
interp = lambda kf, t: next((ka + (kb - ka) * (t - ta) / (tb - ta) for (ta, ka), (tb, kb) in zip(kf, kf[1:]) if ta <= t <= tb), kf[-1][1])
EV = [{'t': cue['a0']['monthly'], 'kind': 'tick', 'v': 0.5}, {'t': cue['a0']['figure'], 'kind': 'land', 'mode': False}]
for yr in range(0, 31, 5):
    k = 12 * yr; t = next(ta + (tb - ta) * (k - ka) / (kb - ka) for (ta, ka), (tb, kb) in zip(PAYK, PAYK[1:]) if ka <= k <= kb)
    EV.append({'t': round(t, 3), 'kind': 'data', 'v': round(bal(k), 3)})
EV += SV.move_sounds(moves, lambda m: 0.6)
EV.sort(key=lambda e: e['t'])
tension = [[0, 0.2], [beats[0]['t0'], 0.3], [beats[1]['t0'], 0.5], [TOTAL - 1.2, 0.3], [TOTAL, 0.1]]
errs = SV.check_rules(beats, moves, PAD)
spine = {'segment': 'ep005 C3 · N1 lịch (S06.1 + S06.3)', 'version': 3, 'total': TOTAL, 'fps': 30, 'pad': PAD, 'takes': takes, 'words': words,
         'beats': beats, 'moves': moves, 'pay_kf': PAYK, 'events': EV, 'tension': tension, 'shots': SV.shots_for(moves, TOTAL),
         'music_plan': wlib.music_plan_flat(TOTAL, [cue['a0']['figure'], cue['a1']['later']]), 'mix': {'music_db': 17.0, 'data_db': 25.0},
         'label_cues': {'a0.figure': '$2,362/month · principal + interest'},
         'visual_cues': ['a0.monthly', 'a0.figure', 'a1.each', 'a1.faster'], 'checks': {'rule2_rule3_rule7': errs or 'OK'}}
json.dump(spine, open(os.path.join(HERE, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(['episodes/ep005/world/claims.json', 'episodes/ep005/world/obj5.js'], open(os.path.join(HERE, 'inputs.json'), 'w'))
print('total', TOTAL, 'moves', [(m['verb'], m['t0'], m['t1']) for m in moves]); print(cue); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
