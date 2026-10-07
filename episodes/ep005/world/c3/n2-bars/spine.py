"""Tập 5 · C3 · N2 CỘT PHÁT LẠI trong ngữ cảnh — lời thật S13.1–S13.3 (đuôi chậm).
  python3 episodes/ep005/world/c3/n2-bars/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
Thế giới: 307 cột đứng trên sàn như một dãy phố nhìn nghiêng; xà "điển hình" thấp; "tail" = các cột > 60 tháng sáng warn và nhô lên.
→ ĐỒ THỊ (lời "more than five years": số chỉ ở đồ thị): xà 60 tháng + nhãn "about 1 in 7"; "together/stretch" = ngoặc trên cụm warn;
"national price slump" = đường chỉ số giá quốc gia (W5, accent) vẽ trên cột, đoạn đỉnh→đáy đậm lên.
C3 vòng 2 (FIX-R2.md): chỉ số chuyển xuống thành dải mảnh trong trục tháng mua (dưới chân cột); tiêu đề trục giữ suốt; dải warn
nối cụm với tháng mua; nhãn "one stretch of purchase months". Cột = thời gian tới 80 % trên giấy, không phải thời gian giữ nhà."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W5 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W5)
import wlib
import spine as SV
PAD = 0.25
words, takes, lines, end = wlib.clip_voice([['S13.1', 'S13.2', 'S13.3']], lead=0.5)
TOTAL = round(end + 0.1, 2)
A = SV.Anchors(words)
B = [
 ('t0', 'S13.1', 'world', 'Trường hợp điển hình che một đuôi dài.', 'dãy cột nhìn nghiêng; xà "typical" thấp; ở "tail" các cột cao nhất sáng warn và nhô lên.',
  {'typical': '@S13.1:typical', 'tail': '@S13.1:tail'}, ['nốt đi lên khi đuôi sáng'], 0.45, 'bất ngờ', ''),
 ('t1', 'S13.2', 'world', 'Khoảng 1/7 số tháng mua mất hơn 5 năm.', 'vẫn thế giới tới hết "seven"; chuyển sang đồ thị trước "five": xà 60 tháng + nhãn "more than 60 months: 14.7% (about 1 in 7)".',
  {'seven': '@S13.2:seven', 'five': '@S13.2:five', 'years': '@S13.2:years'}, ['chạm khi xà 60 tháng khoá', 'chuông ở "years"'], 0.6, 'nặng',
  'CHUYỂN CHẾ ĐỘ → đồ thị: "more than five years" là một số'),
 ('t2', 'S13.3', 'chart', 'Các tháng chậm nằm liền nhau, ngay trước và trong đợt giảm giá nhà toàn quốc.', 'ngoặc trên cụm warn + dải warn mờ dọc cụm xuống trục tháng mua ("together"); nhãn "one stretch of purchase months" ("stretch"); chỉ số quốc gia (accent) là dải mảnh TRONG trục tháng mua, dưới chân cột (vòng 2), vẽ tới "national", đoạn đỉnh → đáy đậm ở "slump".',
  {'together': '@S13.3:together', 'stretch': '@S13.3:stretch', 'national': '@S13.3:national', 'slump': '@S13.3:slump'}, ['nốt dữ liệu theo chỉ số khi đường vẽ', 'trượt xuống ở "slump"'], 0.65, 'hiểu', '(hết)'),
]
beats = SV.beats_from(B, A, lines)
cue = {b['id']: b['cues'] for b in beats}
moves = []
for verb, a, b, after, before, dur, reason, snd in [
        ('mode', 'wRow', 'cBars', cue['t1']['seven'], cue['t1']['five'], 1.0, 'lời "took more than five years": ngưỡng 60 tháng và tỉ lệ là số → chế độ đồ thị (quy tắc 1)', 'whoosh_mode')]:
    t0, t1 = SV.window(after, before, dur, PAD, eps=0.01)
    moves.append({'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd})
D = json.load(open(os.path.join(wlib.ROOT, 'episodes/ep005/work/world-data/derived.json')))
IX = [x for x in D['index'] if x['m'] <= D['bars'][-1]['m']]
DRAW = [round(cue['t2']['stretch'] + 0.5, 3), cue['t2']['national']]   # đường chỉ số vẽ trái → phải sau "stretch", đủ ở "national"; "slump": đoạn đỉnh → đáy đậm lên
EV = [{'t': cue['t0']['tail'], 'kind': 'rise', 'dur': 0.8}, {'t': cue['t1']['years'], 'kind': 'chime'}, {'t': cue['t2']['together'], 'kind': 'tick', 'v': 0.6},
      {'t': cue['t2']['slump'], 'kind': 'slide_down', 'dur': 0.6}]
vmin, vmax = min(x['v'] for x in IX), max(x['v'] for x in IX)
for i in range(0, len(IX), 36):                                          # nốt dữ liệu mỗi 3 năm khi đường chỉ số vẽ (cao độ = chỉ số)
    EV.append({'t': round(DRAW[0] + (DRAW[1] - DRAW[0]) * i / (len(IX) - 1), 3), 'kind': 'data', 'v': round((IX[i]['v'] - vmin) / (vmax - vmin), 3)})
EV += SV.move_sounds(moves, lambda m: 0.6)
EV.sort(key=lambda e: e['t'])
tension = [[0, 0.35], [beats[0]['t0'], 0.45], [beats[1]['t0'], 0.6], [beats[2]['t0'], 0.7], [TOTAL - 0.8, 0.4], [TOTAL, 0.1]]
errs = SV.check_rules(beats, moves, PAD)
spine = {'segment': 'ep005 C3 · N2 cột phát lại (S13.1–S13.3)', 'version': 4, 'total': TOTAL, 'fps': 30, 'pad': PAD, 'takes': takes, 'words': words,
         'beats': beats, 'moves': moves, 'index_draw': DRAW, 'events': EV, 'tension': tension, 'shots': SV.shots_for(moves, TOTAL),
         'music_plan': wlib.music_plan_flat(TOTAL, [cue['t1']['years'], cue['t2']['slump']]), 'mix': {'music_db': 17.0, 'data_db': 25.0},
         'label_cues': {'t1.years': 'more than 60 months:', 't2.slump': 'national price slump', 't2.stretch': 'one stretch of purchase months'},
         'visual_cues': ['t0.tail', 't1.years', 't2.together', 't2.national', 't2.slump'], 'checks': {'rule2_rule3_rule7': errs or 'OK'}}
json.dump(spine, open(os.path.join(HERE, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(['episodes/ep005/world/claims.json', 'episodes/ep005/work/world-data/derived.json', 'episodes/ep005/world/obj5.js'], open(os.path.join(HERE, 'inputs.json'), 'w'))
print('total', TOTAL, 'moves', [(m['verb'], m['t0'], m['t1']) for m in moves]); print(cue); print('checks', errs or 'OK')
sys.exit(1 if errs else 0)
