"""Mốc V · đoạn chứng minh (a) — Tập 4 S04.5 → S07.3 · ĐẶC TẢ NHỊP v3 "một thế giới, hai chế độ máy quay" (D-010).
  python3 moc-v/seg/ep004/spine.py   → moc-v/seg/ep004/spine.json   (thoát 1 nếu vi phạm quy tắc 2/3/7)
Một nguồn duy nhất cho mọi lớp: lời (take), hình (chế độ, tư thế máy, cửa sổ), âm dữ liệu, sfx, nhạc (bản đồ căng).
Mốc giờ: CHỈ từ alignment của take ("@câu:từ"); cửa sổ động tác máy quay tính từ hai từ khoá kề nhau (± ĐỆM).
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PAD = 0.25                                    # quy tắc 2: máy quay đứng yên trong ± PAD quanh mọi từ khoá
OFFSET = {'S04': 0.6, 'S05': 4.6, 'S06': 23.0, 'S07': 56.2}   # đầu mỗi take (khoảng nghỉ như bản phát hành)
TOTAL = 69.6
voice = json.load(open(os.path.join(ROOT, 'moc-v/proto/voice.json')))
words = []
for tk in voice:
    off = OFFSET[tk['sentences'][0]['id'][:3]]
    words += [{'w': w['w'], 's': round(w['s'] + off, 3), 'e': round(w['e'] + off, 3), 'sid': w['sid']} for w in tk['words']]
takes = [{'mp3': os.path.relpath(t['mp3'], ROOT), 't': OFFSET[t['sentences'][0]['id'][:3]], 'dur': t['duration']} for t in voice]
lines = {s['id']: s['spoken'] for t in voice for s in t['sentences']}


def at(ref, end=False):
    m = re.match(r'@(S\d\d\.\d)(?::([^$]+))?(\$)?$', ref)
    sid, wd, e = m.groups(); ws = [w for w in words if w['sid'] == sid]
    if e: return ws[-1]['e']
    if wd: return next(w['s'] for w in ws if re.sub(r'[^\w-]', '', w['w']).lower().startswith(wd.lower()))
    return next(w['s'] for w in ws if not w['w'].startswith('['))


# ---- nhịp: ý · lời · chế độ · hành động hình · âm · căng · cảm xúc · chuyển (cues = TỪ KHOÁ: máy quay đứng yên quanh chúng)
B = [
 ('b0', 'S04.5', 'world', 'Câu hỏi: lãi của Rosa & Frank đã qua trần chưa?', 'Rosa & Frank cạnh NHÀ trên chồng tiền $200,000 (2000); xà trần mờ hiện phía trên; dấu hỏi giữa mái và xà.',
  {'has': '@S04.5:Has', 'q': '@S04.5:cap'}, ['riser tới "cap?"'], 0.30, 'tò mò', 'nhà mờ đi'),
 ('b1', 'S05.1', 'world', 'Không thấy nhà thật → cho giá trị đi như chỉ số Phoenix (trung bình nhiều giao dịch).', 'nhà mờ trong sương + mũi tên giá lên; lùi máy thấy khu phố; mỗi nhà bật biển SOLD đúng một tick; các nhà bay vào chồng tiền của nhà chính (= trung bình).',
  {'blur': '@S05.1:see', 'rise': '@S05.1:rise', 'pop0': '@S05.1:Phoenix', 'src': '@S05.1:Federal', 'many': '@S05.1:average', 'avg': '@S05.1:sales'},
  ['whoosh mềm khi sương', 'tick mỗi nhà SOLD', 'hợp âm gom'], 0.35, 'rõ ràng, tin cậy', 'CHUYỂN CHẾ ĐỘ → đồ thị: "average of many sales" thành MỘT đường'),
 ('b2', 'S05.2', 'chart', 'Đi từng quý từ 2000 đến Q2 2026.', 'đồ thị chính diện: 3 quý đầu nhảy từng bước ("quarter by quarter"), rồi đường GIÁ TRỊ (vệt đỉnh chồng tiền) chạy tới 2026; nhãn năm theo đầu đường.',
  {'quarter': '@S05.2:quarter', 'y2000': '@S05.2:two', 'y2026': '@S05.2:twenty'}, ['âm dữ liệu: nốt theo giá trị'], 0.50, 'đà đi lên', 'đường giá trị tắt khi trần vào'),
 ('b3', 'S06.1', 'chart', 'Trần là đường phẳng $500,000, mọi quý như nhau.', 'đường giá trị + nhà TẮT (tránh đọc nhầm "giá nhà vượt trần"); xà trần rơi và khoá; nhãn "$500,000 cap"; nhịp sáng chạy dọc xà.',
  {'cap': '@S06.1:cap', 'flat': '@S06.1:flat', 'five': '@S06.1:five', 'same': '@S06.1:same'}, ['thud khi xà khoá', 'nhịp chạy dọc xà'], 0.45, 'chắc, cố định', 'CHUYỂN CHẾ ĐỘ → thế giới: "their gain" (về người)'),
 ('b4', 'S06.2', 'world', 'Lãi trên giấy = $200,000 lớn theo chỉ số − $200,000 đã trả.', 'cảnh minh hoạ trước mặt: nhà + Rosa & Frank; khối $200,000 dưới đáy chồng đổi màu (lúc "$200,000"); chồng lớn lên (lúc "grown"); khối đáy trượt ra phía họ, chồng hạ xuống (lúc "less") — phần còn lại = LÃI.',
  {'gain': '@S06.2:gain', 'two': '@S06.2:two', 'grow': '@S06.2:grown', 'less': '@S06.2:less', 'paid': '@S06.2:paid'},
  ['tick khi khối đổi màu', 'nốt đi lên khi chồng lớn', 'trượt xuống có cao độ khi trừ'], 0.55, 'hiểu cơ chế', 'CHUYỂN CHẾ ĐỘ → đồ thị: phát lại lãi theo năm so với trần'),
 ('b5', 'S06.3', 'chart', 'Phần lớn các năm lãi nằm dưới vạch xa.', 'nhà nhỏ cưỡi đường LÃI từ 2000 (vệt đỉnh chồng); ngoặc "well under" giữa đỉnh chồng và xà.',
  {'under': '@S06.3:under'}, ['âm dữ liệu thưa, trầm'], 0.45, 'yên', 'đầu đường tiến tới 2022'),
 ('b6', 'S06.4', 'chart', 'Q2 2022: vượt.', 'đỉnh chồng chạm và xuyên xà đúng chữ "crosses"; loé; nhãn "Over: Q2 2022".',
  {'q2022': '@S06.4:second', 'cross': '@S06.4:crosses'}, ['riser vào điểm cắt', 'chime đúng khung cắt'], 0.85, 'bất ngờ', 'ĐẨY MÁY vào 2021–2026: nhìn rõ nhịp tụt'),
 ('b7', 'S06.5', 'chart', 'Tụt lại dưới một thời gian.', 'trong khung phóng: đường tụt dưới xà (đoạn dưới đổi về ink); nhãn "Back under".',
  {'slips': '@S06.5:slips'}, ['âm dữ liệu đi xuống'], 0.65, 'lưỡng lự', 'lên lại'),
 ('b8', 'S06.6', 'chart', 'Từ Q2 2023 ở trên luôn.', 'đường lên lại; đoạn trên xà warn tới 2026; nhãn "Stayed over since Q2 2023"; ba nhãn giữ tới khi số bay (trạng thái kết luận).',
  {'stay': '@S06.6:From', 'lbl': '@S06.6:second', 'above': '@S06.6:above'}, ['nốt sáng giữ'], 0.85, 'chắc dần', 'Rosa & Frank đến cạnh nhà'),
 ('b9', 'S07.1', 'chart', 'Con số của câu mở đầu là lãi của họ.', 'Rosa & Frank đứng cạnh nhà ở đầu đường; số "≈ $558,100" hiện ở đỉnh chồng và bay lên biển trên mái (lúc "this" → "opening").',
  {'rose': '@S07.1:rose', 'fly': '@S07.1:this', 'land': '@S07.1:opening'}, ['swish theo đường bay', 'tick khi chạm biển'], 0.95, 'nhận ra', 'nhà nảy qua xà'),
 ('b10', 'S07.2', 'chart', 'Qua trần.', 'nhà nảy lên qua xà; ngoặc warn từ xà tới đỉnh chồng: "past the cap"; khoảng lặng ngắn sau "cap".',
  {'past': '@S07.2:past', 'cap': '@S07.2:cap'}, ['impact mềm SAU "cap"', 'nhạc nhả → lặng ~1 s'], 1.00, 'đỉnh căng', 'LÙI MÁY: cả 26 năm'),
 ('b11', 'S07.3', 'chart', 'Giá vùng Phoenix gần ×3,8 so với 2000.', 'đường lãi mờ; hai chồng GIÁ TRỊ dựng ở 2000 và 2026 Q2 trên cùng trục; ngoặc "×3.8" lúc "three"; tiêu đề "Phoenix-area prices since 2000".',
  {'x': '@S07.3:three', 'lvl': '@S07.3:level'}, ['âm dữ liệu lên một quãng'], 0.30, 'thả, hiểu', '(hết) giữ trạng thái kết luận ≥ 1 s'),
]
beats = []
for bid, sid, mode, idea, visual, cues, sound, ten, emo, nxt in B:
    beats.append({'id': bid, 'sid': sid, 'mode': mode, 'idea': idea, 'visual': visual, 'line': lines[sid], 'sound': sound, 'music': ten,
                  'emotion': emo, 'next': nxt, 't0': at('@' + sid), 't1': at('@' + sid + '$'), 'cues': {k: at(v) for k, v in cues.items()}})
cue = {b['id']: b['cues'] for b in beats}
CUES = sorted((t, f"{b['id']}.{k}") for b in beats for k, t in b['cues'].items())


def window(after, before, dur, late=False):
    """cửa sổ động tác giữa hai từ khoá: bắt đầu sau 'after'+PAD, kết thúc trước 'before'−PAD, dài tối đa dur (late: sát từ khoá sau)."""
    a, b = after + PAD, before - PAD
    if b - a < 0.6: raise SystemExit(f'cửa sổ quá ngắn giữa {after} và {before}')
    t0 = max(a, b - dur) if late else max(a, (a + b) / 2 - dur / 2); return [round(t0, 3), round(min(b, t0 + dur), 3)]


# ---- động tác máy quay hữu hạn (quy tắc 2) — mỗi lần có LÝ DO (câu lời / sự kiện dữ liệu) và ÂM (quy tắc 3)
MOVES = [
 ('hood', 'pull', 'wHome', 'wHood', cue['b1']['rise'], cue['b1']['pop0'], 1.1, 'lời "rise exactly like the … index" → lùi máy thấy khu phố (nhiều giao dịch)', 'whoosh_soft'),
 ('toChart', 'mode', 'wHood', 'cFull', cue['b1']['avg'], cue['b2']['quarter'], 1.05, 'lời "an average of many sales": nhiều nhà gom thành MỘT đường → chế độ đồ thị', 'whoosh_mode'),
 ('toDemo', 'mode', 'cFull', 'wDemoNear', cue['b3']['same'], cue['b4']['gain'], 1.0, 'lời "And here\'s THEIR gain": về người và nhà của họ → chế độ thế giới', 'whoosh_mode'),
 ('demoPull', 'pull', 'wDemoNear', 'wDemo', cue['b4']['two'], cue['b4']['grow'], 0.9, 'lời "grown with the index": chồng sắp cao gấp bốn → lùi máy để thấy trọn', 'whoosh_soft'),
 ('backChart', 'mode', 'wDemo', 'cFull', cue['b4']['paid'], cue['b5']['under'], 1.0, 'sự kiện dữ liệu: lãi vừa tách ra → phát lại theo năm so với trần → chế độ đồ thị', 'whoosh_mode'),
 ('zoom', 'push', 'cFull', 'cZoom', cue['b6']['q2022'], cue['b6']['cross'], 1.2, 'lời "Then, in the second quarter of 2022": sắp tới điểm cắt và nhịp tụt — đoạn 2021–26 quá nhỏ ở thang 26 năm → đẩy máy TRƯỚC khi cắt', 'whoosh_push'),
 ('tip', 'push', 'cZoom', 'cTip', cue['b8']['above'], cue['b9']['rose'], 2.2, 'lời "So, on paper, … THEIR home": con số sắp nói là của Rosa & Frank → đẩy chậm vào nhà ở đầu đường', 'whoosh_soft'),
 ('wide', 'pull', 'cTip', 'cFull', cue['b10']['cap'], cue['b11']['x'], 1.0, 'lời "Phoenix area prices … their 2000 level": cần cả hai đầu 2000 và 2026 → lùi máy', 'whoosh_soft'),
]
moves = []
for mid, verb, a, b, after, before, dur, reason, snd in MOVES:
    t0, t1 = window(after, before, dur, late=(mid == 'wide'))   # 'wide': giữ trạng thái "past the cap" lâu nhất có thể
    moves.append({'id': mid, 'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd})

# ---- lịch dữ liệu dùng chung cho hình VÀ âm (q = quý, 0 = 2000 Q1 … 105 = 2026 Q2)
data = json.load(open(os.path.join(ROOT, 'moc-v/proto/data.json')))
gain = [p['y'] for p in data['gain']]
crossQ = 88 + (500000 - gain[88]) / (gain[89] - gain[88])
DRAW = [[cue['b2']['quarter'], 0], [cue['b2']['quarter'] + 0.45, 1], [cue['b2']['quarter'] + 0.9, 2], [cue['b2']['y2000'], 3],
        [cue['b2']['y2026'] + 0.6, 105]]                                     # "quarter by quarter" = 3 bước; "2026" đến đầu đường
MV = {m['id']: m for m in moves}
RIDE = [[MV['backChart']['t1'] + 0.15, 0], [cue['b6']['cross'] - 0.9, 88], [cue['b6']['cross'], round(crossQ, 3)], [cue['b7']['slips'] + 0.1, 91],
        [cue['b8']['stay'] - 0.2, 92], [cue['b8']['lbl'], 93], [cue['b8']['above'], 105]]


def interp(kf, t):
    if t <= kf[0][0]: return kf[0][1]
    for (a, x), (b, y) in zip(kf, kf[1:]):
        if t <= b: return x + (y - x) * (t - a) / (b - a)
    return kf[-1][1]


def when(kf, q):
    for (a, x), (b, y) in zip(kf, kf[1:]):
        if x <= q <= y and y > x: return a + (b - a) * (q - x) / (y - x)


EV = []
for q in [0, 1, 2] + list(range(4, 106, 4)):
    EV.append({'t': round(when(DRAW, q), 3), 'kind': 'data', 'v': (gain[q] + 200000) / 800000, 'src': 'value'})
for q in range(0, 106):
    if q % 4 == 0 or q >= 86:                  # b5 thưa (lượt đạo diễn v3)
        EV.append({'t': round(when(RIDE, min(q, 105)), 3), 'kind': 'data', 'v': max(0, gain[q]) / 800000, 'src': 'gain', 'over': gain[q] > 500000})
pops = [round(cue['b1']['pop0'] + k * (cue['b1']['many'] - 0.3 - cue['b1']['pop0']) / 11, 3) for k in range(12)]
EV += [{'t': cue['b0']['has'], 'kind': 'riser', 'to': cue['b0']['q']},
       {'t': cue['b1']['blur'], 'kind': 'whoosh_soft'},
       *[{'t': p, 'kind': 'tick', 'pop': k, 'v': 0.3 + 0.05 * (k % 5)} for k, p in enumerate(pops)],
       {'t': cue['b1']['avg'], 'kind': 'gather'},
       {'t': cue['b3']['cap'] + 0.6, 'kind': 'thud'},
       {'t': cue['b4']['two'], 'kind': 'tick', 'v': 0.6},
       {'t': cue['b4']['grow'], 'kind': 'rise', 'dur': 0.9},
       {'t': cue['b4']['less'], 'kind': 'slide_down', 'dur': 1.6},
       {'t': cue['b6']['cross'] - 1.6, 'kind': 'riser', 'to': cue['b6']['cross']}, {'t': cue['b6']['cross'], 'kind': 'chime'},
       {'t': cue['b9']['fly'], 'kind': 'swish', 'to': cue['b9']['land']}, {'t': cue['b9']['land'], 'kind': 'tick', 'v': 0.7},
       {'t': cue['b10']['past'] + 0.2, 'kind': 'land', 'mode': False},   # chạm mềm khi nhà nảy qua xà (không impact to: giữ lặng sau "cap")
       {'t': cue['b9']['rose'], 'kind': 'rise', 'dur': round(cue['b9']['fly'] - 0.25 - cue['b9']['rose'], 3)},
       {'t': cue['b11']['x'] - 1.4, 'kind': 'rise', 'dur': 1.4}]
for m in moves:                                # quy tắc 3: mọi động tác có âm (whoosh + chạm khi tới)
    quiet = m['id'] == 'wide'                    # trong khoảng lặng sau "cap": chỉ gió rất nhẹ, không chạm
    EV.append({'t': m['t0'], 'kind': m['sound'], 'dur': round(m['t1'] - m['t0'], 3), 'gain': 0.35 if quiet else 1.0})
    if not quiet: EV.append({'t': m['t1'], 'kind': 'land', 'mode': m['verb'] == 'mode'})
EV.sort(key=lambda e: e['t'])

# ---- bản đồ căng (biên độ rộng: chủ dự án, Gói A §5)
tension = sorted([[0, 0.12]] + [[b['t0'], b['music']] for b in beats if b['id'] != 'b11'] + [[cue['b10']['cap'] + 0.3, 1.0], [cue['b11']['x'], 0.30], [TOTAL - 2.0, 0.2], [TOTAL, 0.1]])
# ---- cảnh render (cache theo cảnh, quy tắc 8): ranh giới = giữa các động tác máy quay
cuts = [0] + [m['t0'] for m in moves] + [TOTAL]
shots = [{'id': f's{i}', 't0': round(a, 3), 't1': round(b, 3)} for i, (a, b) in enumerate(zip(cuts, cuts[1:]))]

# ---- tự kiểm
errs = []
for m in moves:                                # quy tắc 2
    for t, name in CUES:
        if m['t0'] - PAD < t < m['t1'] + PAD: errs.append(f'quy tắc 2: từ khoá {name} @{t} trong cửa sổ máy quay {m["verb"]} {m["t0"]}–{m["t1"]}')
    if not m['reason'] or not m['sound']: errs.append(f'quy tắc 3: động tác {m} thiếu lý do/âm')
if beats[0]['mode'] != 'world' or moves[0]['t0'] < 5.0 and moves[0]['verb'] == 'mode': errs.append('quy tắc 7: 5 s đầu phải ở chế độ thế giới')
spine = {'segment': 'ep004 S04.5 → S07.3 (bản phát hành 93,44–163,60 s)', 'version': 3, 'total': TOTAL, 'fps': 30, 'pad': PAD,
         'takes': takes, 'words': words, 'beats': beats, 'moves': moves, 'draw': DRAW, 'ride': RIDE, 'crossQ': crossQ,
         'events': EV, 'tension': tension,
         'music_plan': {'stop': cue['b10']['cap'] + 0.32, 'release': cue['b11']['x'], 'accents': [cue['b3']['cap'] + 0.5, cue['b6']['cross']]},
         'label_cues': {'b2.quarter': '2000 Q1', 'b0.q': '?', 'b1.many': 'many sales → one average', 'b3.five': '$500,000 cap', 'b4.gain': 'their gain on paper = ?', 'b4.two': 'what they paid',
                        'b5.under': 'well under', 'b6.cross': 'Over: Q2 2022', 'b7.slips': 'Back under', 'b8.lbl': 'Stayed over since Q2 2023', 'b9.fly': '≈ $558,100',
                        'b10.past': 'past the cap', 'b11.x': '×3.8'},
         'visual_cues': ['b3.flat', 'b8.above', 'b9.rose', 'b0.q', 'b1.blur', 'b1.rise', 'b1.pop0', 'b1.many', 'b2.quarter', 'b3.cap', 'b3.five', 'b3.same', 'b4.gain', 'b4.two', 'b4.grow', 'b4.less', 'b5.under', 'b6.cross', 'b7.slips', 'b8.lbl', 'b9.fly', 'b10.past', 'b11.x'], 'shots': shots, 'checks': {'rule2_rule3_rule7': errs or 'OK'}}
json.dump(spine, open(os.path.join(HERE, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
world = sum(m['t1'] - m['t0'] for m in moves if m['verb'] == 'mode')
print('moves:', [(m['verb'], m['t0'], m['t1']) for m in moves]); print('shots:', [(s['t0'], s['t1']) for s in shots])
print('checks:', errs or 'OK')
sys.exit(1 if errs else 0)
