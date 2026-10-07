"""Mốc V · đoạn thử: TRỤC XƯƠNG SỐNG — một đặc tả nhịp duy nhất cho mọi lớp (hình, lời, âm dữ liệu, sfx, nhạc).
  python3 moc-v/proto/spine.py   →  moc-v/proto/spine.json
Mỗi nhịp: ý · câu lời · hành động hình (động từ) · sự kiện âm · trạng thái nhạc (căng 0–1) · cảm xúc · chuyển sang nhịp sau.
Mốc giờ KHÔNG gõ tay: lấy từ alignment của take giọng (moc-v/proto/voice.json) qua "@câu:từ" như nhà máy.
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OFFSET = {'S04': 0.6, 'S05': 4.6, 'S06': 23.0, 'S07': 56.2}   # đầu mỗi take trong đoạn (khoảng nghỉ như bản phát hành)
TOTAL = 69.6
voice = json.load(open(os.path.join(HERE, 'voice.json')))
words = []
for take in voice:
    off = OFFSET[take['sentences'][0]['id'][:3]]
    for w in take['words']:
        words.append({'w': w['w'], 's': round(w['s'] + off, 3), 'e': round(w['e'] + off, 3), 'sid': w['sid']})
takes = [{'wav': t['wav'], 'mp3': os.path.relpath(t['mp3'], ROOT), 't': OFFSET[t['sentences'][0]['id'][:3]], 'dur': t['duration']} for t in voice]


def at(ref):
    """'@S06.4:crosses' → start of that word; '@S06.4$' → end of sentence; '+x' offset."""
    m = re.match(r'@(S\d\d\.\d)(?::([^$+]+))?(\$)?(?:\+([\d.]+))?$', ref)
    sid, wd, end, plus = m.groups()
    ws = [w for w in words if w['sid'] == sid]
    if end:
        t = ws[-1]['e']
    elif wd:
        t = next(w['s'] for w in ws if re.sub(r'[^\w-]', '', w['w']).lower().startswith(wd.lower()))
    else:
        t = next(w['s'] for w in ws if not w['w'].startswith('['))
    return round(t + float(plus or 0), 3)


B = [
 dict(id='b0', sid='S04.5', idea='Câu hỏi của tập, gắn vào Rosa & Frank: lãi của họ đã qua trần chưa?',
      visual='Rosa & Frank đứng trước NHÀ (hero object); vạch trần $500,000 hạ xuống phía trên mái; dấu hỏi.',
      cues={'cap_hint': '@S04.5:Has', 'q': '@S04.5:cap'}, sound=['riser nhẹ tới "cap?"'], music=0.35, emotion='tò mò, hơi lo',
      next='nhà mờ đi (không thấy nhà thật) → nhiều nhà nhỏ'),
 dict(id='b1', sid='S05.1', idea='Không thấy nhà thật → cho giá trị đi đúng như chỉ số giá nhà Phoenix (trung bình nhiều giao dịch).',
      visual='nhà mờ thành bóng; nhiều nhà nhỏ bật lên (nhiều giao dịch) rồi gom về một ĐƯỜNG chỉ số; thẻ nguồn FHFA via FRED.',
      cues={'blur': '@S05.1:see', 'rise': '@S05.1:rise', 'pop0': '@S05.1:Phoenix', 'many': '@S05.1:average', 'avg': '@S05.1:sales', 'src': '@S05.1:Federal'},
      sound=['tick mềm mỗi nhà nhỏ (âm dữ liệu)', 'hợp âm gom khi về một đường'], music=0.4, emotion='rõ ràng, tin cậy',
      next='đường chỉ số bắt đầu vẽ từ 2000'),
 dict(id='b2', sid='S05.2', idea='Đi từng quý từ 2000 đến Q2 2026.',
      visual='nhà nhỏ cưỡi đầu đường, vẽ quý theo quý; trục năm lật như lịch; giá trên nhà tăng.',
      cues={'draw0': '@S05.2:follow', 'y2000': '@S05.2:two', 'y2026': '@S05.2:twenty', 'draw1': '@S05.2:latest'}, sound=['âm dữ liệu: mỗi quý một nốt, cao độ theo giá trị (bảng S2)'],
      music=0.5, emotion='đà đi lên', next='vạch trần đập xuống cắt ngang khung'),
 dict(id='b3', sid='S06.1', idea='Trần là một đường phẳng $500,000, mọi quý như nhau.',
      visual='vạch trần rơi xuống và khoá ngang (đứng yên suốt đoạn); nhãn "$500,000 cap" đúng lúc "five hundred thousand".',
      cues={'cap': '@S06.1:cap', 'lbl': '@S06.1:five', 'flat': '@S06.1:same'}, sound=['thud trầm khi vạch khoá', 'drone nhẹ của trần (giữ)'],
      music=0.45, emotion='chắc, cố định', next='đường giá trị trượt xuống thành đường lãi'),
 dict(id='b4', sid='S06.2', idea='Lãi trên giấy = $200,000 lớn theo chỉ số − $200,000 đã trả.',
      visual='thẻ giá $200,000 lớn theo đường; rồi CẢ ĐƯỜNG trượt xuống đúng $200,000 (phép trừ thấy được) → thành đường LÃI.',
      cues={'gain': '@S06.2:gain', 'two': '@S06.2:two', 'grow': '@S06.2:grown', 'less': '@S06.2:less', 'paid': '@S06.2:paid'},
      sound=['whoosh xuống có cao độ khi đường trượt (trừ)'], music=0.5, emotion='hiểu ra cơ chế', next='camera lùi xem cả đường dưới vạch'),
 dict(id='b5', sid='S06.3', idea='Phần lớn các năm, lãi nằm dưới vạch xa.',
      visual='vùng dưới vạch tô nhạt; khoảng cách tới vạch hiện thành ngoặc lớn.', cues={'under': '@S06.3:under'},
      sound=['âm dữ liệu trầm, thưa'], music=0.4, emotion='yên', next='đầu đường tiến về 2022'),
 dict(id='b6', sid='S06.4', idea='Q2 2022: vượt.', visual='đầu đường chạm và XUYÊN vạch; tia sáng ở điểm cắt; nhãn "Q2 2022".',
      cues={'cross': '@S06.4:crosses', 'q': '@S06.4:second'}, sound=['chime sáng đúng khung cắt (±1 khung)'], music=0.8, emotion='bất ngờ',
      next='đường tụt lại'),
 dict(id='b7', sid='S06.5', idea='Tụt lại dưới một thời gian.', visual='đầu đường trượt xuống dưới vạch; phần vượt tắt màu.',
      cues={'slip': '@S06.5:slips'}, sound=['âm dữ liệu đi xuống'], music=0.6, emotion='lưỡng lự', next='đường lên lại và ở trên'),
 dict(id='b8', sid='S06.6', idea='Từ Q2 2023 ở trên luôn.', visual='đường lên lại, đoạn trên vạch tô màu warn kéo dài tới 2026; nhãn "since Q2 2023".',
      cues={'stay': '@S06.6:From', 'lbl': '@S06.6:second', 'above': '@S06.6:above'}, sound=['nốt giữ sáng (âm dữ liệu)'], music=0.75,
      emotion='chắc dần', next='số ở đầu đường bay ra'),
 dict(id='b9', sid='S07.1', idea='Đây là con số của câu mở đầu (callback).', visual='số $558,100 BAY từ đầu đường vào biển trên nhà của Rosa & Frank.',
      cues={'fly': '@S07.1:this', 'land': '@S07.1:opening'}, sound=['swish có cao độ theo đường bay, chạm = tick'], music=0.85,
      emotion='nhận ra', next='chồng lãi đẩy qua vạch'),
 dict(id='b10', sid='S07.2', idea='Qua trần.', visual='chồng tiền lãi dưới nhà đẩy XUYÊN vạch trần; phần vượt đổi màu warn.',
      cues={'past': '@S07.2:past', 'cap': '@S07.2:cap'}, sound=['va chạm mềm + khoảng lặng ngắn sau "cap" (nhạc nhả, room tone giữ sàn)'],
      music=1.0, emotion='đỉnh căng', next='thả: giá nhân 3,8'),
 dict(id='b11', sid='S07.3', idea='Giá vùng Phoenix gần ×3,8 so với 2000.', visual='nhà 2000 nhỏ → nhà hôm nay cao ×3,8 (chiều cao ∝ chỉ số).',
      cues={'x': '@S07.3:three', 'lvl': '@S07.3:level'}, sound=['âm dữ liệu đi lên một quãng'], music=0.45, emotion='thả, hiểu',
      next='(hết đoạn) giữ trạng thái kết luận ≥ 1 s'),
]
for b in B:
    b['t0'] = at('@' + b['sid'])
    b['t1'] = at('@' + b['sid'] + '$')
    b['line'] = next(s['spoken'] for t in voice for s in t['sentences'] if s['id'] == b['sid'])
    b['cues'] = {k: at(v) for k, v in b['cues'].items()}
# Lịch dữ liệu dùng chung cho hình VÀ âm (đồng bộ do cấu trúc, không căn tay): chỉ số quý q (0 = 2000 Q1 … 105 = 2026 Q2) theo thời gian.
cue = {b['id']: b['cues'] for b in B}
DRAW = [[cue['b2']['draw0'], 0], [cue['b2']['y2000'], 2], [cue['b2']['y2026'], 105]]   # b2: đường GIÁ TRỊ vẽ quý theo quý; năm khoá theo lời (lượt đạo diễn v1)
RIDE = [[B[5]['t0'] + 0.15, 0], [cue['b6']['cross'] - 0.9, 88], [cue['b6']['cross'], 89], [cue['b7']['slip'] + 0.1, 91],
        [cue['b8']['stay'] - 0.2, 92], [cue['b8']['lbl'], 93], [cue['b8']['above'], 105]]   # b5–b8: con trỏ cưỡi đường LÃI
data = json.load(open(os.path.join(HERE, 'data.json')))
gain = [p['y'] for p in data['gain']]


def interp(kf, t):
    if t <= kf[0][0]: return kf[0][1]
    for (a, x), (b, y) in zip(kf, kf[1:]):
        if t <= b: return x + (y - x) * (t - a) / (b - a)
    return kf[-1][1]


def when(kf, q):
    for (a, x), (b, y) in zip(kf, kf[1:]):
        if x <= q <= y and y > x: return a + (b - a) * (q - x) / (y - x)


EV = []
for q in range(0, 106, 4):                                                       # b2: một nốt mỗi năm, cao độ = giá trị nhà
    EV.append({'t': round(when(DRAW, q), 3), 'kind': 'data', 'v': (gain[q] + 200000) / 800000, 'src': 'value'})
for q in range(0, 106):                                                          # b5–b8: mỗi quý con trỏ đi qua, cao độ = lãi
    if q % 2 == 0 or q >= 86:
        EV.append({'t': round(when(RIDE, q), 3), 'kind': 'data', 'v': max(0, gain[q]) / 800000, 'src': 'gain', 'over': gain[q] > 500000})
EV += [{'t': cue['b0']['cap_hint'], 'kind': 'riser', 'to': cue['b0']['q']},
       {'t': cue['b1']['blur'], 'kind': 'whoosh_soft'},
       *[{'t': round(cue['b1']['pop0'] + k * (cue['b1']['many'] - 0.3 - cue['b1']['pop0']) / 11, 3), 'kind': 'tick', 'pop': k, 'v': 0.3 + 0.05 * (k % 5)} for k in range(12)],   # mỗi nhà SOLD bật = một tick
       {'t': cue['b1']['avg'], 'kind': 'gather'},
       {'t': cue['b3']['cap'] + 0.35, 'kind': 'thud'}, {'t': cue['b3']['cap'] + 0.35, 'kind': 'drone_on', 'until': cue['b4']['less']},
       {'t': cue['b4']['less'], 'kind': 'slide_down', 'dur': 1.6},
       {'t': cue['b6']['cross'] - 1.6, 'kind': 'riser', 'to': cue['b6']['cross']}, {'t': cue['b6']['cross'], 'kind': 'chime'},
       {'t': cue['b9']['fly'], 'kind': 'swish', 'to': cue['b9']['land']}, {'t': cue['b9']['land'], 'kind': 'tick', 'v': 0.7},
       {'t': cue['b10']['cap'] + 0.32, 'kind': 'impact'},   # sau chữ 'cap' (lượt đạo diễn: impact đè lời)
       {'t': cue['b11']['x'], 'kind': 'rise', 'dur': 2.2}]
EV.sort(key=lambda e: e['t'])
spine = {'segment': 'ep004 S04.5 → S07.3 (bản phát hành 93,8–163,5 s)', 'total': TOTAL, 'fps': 30, 'takes': takes, 'words': words, 'beats': B,
         'draw': DRAW, 'ride': RIDE, 'events': EV, 'tension': [[0, 0.3]] + [[b['t0'], b['music']] for b in B] + [[TOTAL - 1.5, 0.35], [TOTAL, 0.2]]}
json.dump(spine, open(os.path.join(HERE, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
for b in B:
    print(b['id'], b['t0'], b['t1'], b['cues'])
