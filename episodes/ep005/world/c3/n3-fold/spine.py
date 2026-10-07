"""Tập 5 · C3 · N3 GẬP ĐƯỜNG → CỘT (dùng N1 lịch, N2 cột) trong ngữ cảnh — lời thật S10.4 + S10.5.
  python3 episodes/ep005/world/c3/n3-fold/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới (S10.4): một tháng mua minh hoạ (tháng điển hình): nhà trên chồng GIÁ TRỊ (theo chỉ số), chồng VAY bên cạnh, vạch 80 % của giá trị
nằm trên chồng vay; lịch lật mỗi tháng; "stop the clock … eighty percent or less" = lịch NGỪNG khi đỉnh chồng vay chạm vạch.
→ ĐỒ THỊ (lời "Each bar here"): 307 đường phát lại (W6) — mỗi đường GẬP thành cột của chính tháng mua đó (N3); cột = N2, chiều cao = số tháng."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W5 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W5)
import wlib
import spine as SV
PAD = 0.25
words, takes, lines, end = wlib.clip_voice([['S10.4', 'S10.5']], lead=0.3, pre=0.1)
TOTAL = round(end + 0.1, 2)
A = SV.Anchors(words)
B = [
 ('f0', 'S10.4', 'world', 'Mỗi tháng so dư nợ với giá trị; dừng đồng hồ lần đầu khoản vay ≤ 80 %.', 'nhà trên chồng giá trị (theo chỉ số), chồng vay cạnh, vạch 80 % của giá trị; lịch lật mỗi tháng; ngừng lật đúng lúc đỉnh chồng vay chạm vạch ("less").',
  {'every': '@S10.4:Every', 'compare': '@S10.4:compare', 'value': '@S10.4:value', 'stop': '@S10.4:stop', 'eighty': '@S10.4:eighty', 'less': '@S10.4:less'},
  ['tick mỗi 2 tháng lịch lật', 'chạm + chuông khi dừng'], 0.45, 'chú ý', 'CHUYỂN CHẾ ĐỘ → đồ thị: "Each bar here" là một biểu đồ'),
 ('f1', 'S10.5', 'chart', 'Mỗi cột là một tháng mua; chiều cao = bao lâu mới tới 80 % trên giấy.', '307 đường phát lại gập thành 307 cột (thời gian nằm ngang → chiều cao); trục đổi từ "năm sau khi mua" sang "tháng mua 1991–2016"; "height": ngoặc chiều cao trên cột cao nhất.',
  {'bar': '@S10.5:bar', 'month': '@S10.5:month', 'height': '@S10.5:height'}, ['swish khi gập', 'nốt đi lên ở "height"'], 0.55, 'hé lộ', '(hết)'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = []
for verb, a, b, after, before, dur, reason, snd in [
        ('mode', 'wReplay', 'cBars', cue['f0']['less'], cue['f1']['bar'], 1.1, 'lời "Each bar here is one purchase month": từ một tháng mua sang mọi tháng mua trên một biểu đồ → chế độ đồ thị', 'whoosh_mode')]:
    t0, t1 = SV.window(after, before, dur, PAD, eps=0.01)
    moves.append({'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd})
D = json.load(open(os.path.join(wlib.ROOT, 'episodes/ep005/work/world-data/derived.json')))
G = D['buyers']['grace']
MK = [[cue['f0']['every'], 0], [cue['f0']['less'], G['hit']]]          # tháng sau khi mua (thế giới)
FOLD = [cue['f1']['bar'], round(cue['f1']['bar'] + 1.2, 3)]             # gập: bắt đầu ở "bar", xong trước "month"
assert FOLD[1] < cue['f1']['month'] - 0.1
EV = [{'t': round(MK[0][0] + (MK[1][0] - MK[0][0]) * k / G['hit'], 3), 'kind': 'tick', 'v': 0.3} for k in range(2, G['hit'], 2)]
EV += [{'t': cue['f0']['less'], 'kind': 'chime'}, {'t': cue['f0']['less'], 'kind': 'land', 'mode': False},
       {'t': FOLD[0], 'kind': 'swish', 'to': FOLD[1]}, {'t': cue['f1']['height'], 'kind': 'rise', 'dur': 0.6}]
EV += SV.move_sounds(moves, lambda m: 0.6)
EV.sort(key=lambda e: e['t'])
tension = [[0, 0.3], [beats[0]['t0'], 0.45], [beats[1]['t0'], 0.6], [TOTAL - 0.8, 0.35], [TOTAL, 0.1]]
errs = SV.check_rules(beats, moves, PAD)
spine = {'segment': 'ep005 C3 · N3 gập đường → cột (S10.4–S10.5)', 'version': 3, 'total': TOTAL, 'fps': 30, 'pad': PAD, 'takes': takes, 'words': words,
         'beats': beats, 'moves': moves, 'month_kf': MK, 'fold': FOLD, 'events': EV, 'tension': tension, 'shots': SV.shots_for(moves, TOTAL),
         'music_plan': wlib.music_plan_flat(TOTAL, [cue['f0']['less'], cue['f1']['height']]), 'mix': {'music_db': 17.0, 'data_db': 25.0},
         'label_cues': {'f0.compare': 'loan', 'f0.value': 'home value', 'f1.height': 'height = months to 80% on paper'},
         'visual_cues': ['f0.compare', 'f0.value', 'f0.less', 'f1.bar', 'f1.height'], 'checks': {'rule2_rule3_rule7': errs or 'OK'}}   # 'every' ở 0,4 s: sync_audit không có nền trước đó để đo → không đưa vào
json.dump(spine, open(os.path.join(HERE, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(['episodes/ep005/world/claims.json', 'episodes/ep005/work/world-data/derived.json', 'episodes/ep005/world/obj5.js'], open(os.path.join(HERE, 'inputs.json'), 'w'))
print('total', TOTAL, 'moves', [(m['verb'], m['t0'], m['t1']) for m in moves]); print(cue); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
