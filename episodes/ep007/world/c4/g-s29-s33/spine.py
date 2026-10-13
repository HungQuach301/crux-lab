"""Tập 7 · C4 · ĐOẠN G = S29–S33 (Hồi 3: Leo đối trọng, ngưỡng cho mọi người vay; giới hạn + thẻ phương pháp; câu trả lời của Tessa). Lời + giờ = timeline.
  python3 episodes/ep007/world/c4/g-s29-s33/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, 'land')
Ba cụm trên sàn, trái → phải: LEO (ILLUSTRATIVE, nhà + người màu riêng, BÊN TRÁI Tessa — contract.json side) · TESSA (the bar bên trái cô, nhà, the stack
bên phải nhà — khung cold open) · Ô THỨ BA trống (thanh trống, chồng trống). Mỗi cụm: thanh (W3, độ cao = lãi, 0,3/điểm), chồng (W2, bó của the stack),
hộp cushion trước nhà (đường lui, cao ∝ khoảng chênh khoản trả).
B29 (S29, KEY-11): thế giới — "illustrative" nhà + Leo TRƯỢT vào từ trái; "January" cắm cọc lịch (không chữ) cạnh nhà Leo. → ĐỒ THỊ: "lowest" =
  "Leo · Jan 2021 · 30-year at 2.65%"; "paid" chồng của Leo xếp TỪNG BÓ tới trước "cheaper" (dừng thấp hơn the stack); "cheaper" vạch nét đứt từ đỉnh
  chồng Leo sang the stack; "thirteen" = "Leo's stack: $13,231 ($74 a month)". Thanh của Tessa chỉ trồi ở S30.2 (C5: tấm xám trôi nổi).
B30 (S30, KEY-12; C5 đúng-số): "room" NGOẶC V6 cushion trên mái nhà Leo, độ rộng ∝ khoảng $793 dưới khoản 15 năm (rộng hơn ngoặc ~$613 của Tessa, cùng
  thang); "seven" = "about $793 a month below the 15-year" trên ngoặc (Tessa: "about $613 a month"); "bar" thanh của Leo trồi, thấp, XA đầu Leo; "two" =
  "bar 2.65%"; "Same" / "different" thẻ tuần trên hai ngoặc; S30.4 KHÔNG khối chữ: loé lần lượt chồng / thanh của Leo rồi của Tessa, "high" = "bar 7.40%".
B31 (S31, C4 r4 + C5): lia + dolly, ô thứ ba vào giữa khung; "Any" ô thứ ba hiện: đế nét đứt, người viền nét đứt, chồng trống + thanh trống (viền nét đứt)
  — thanh nằm sát sàn; "pair" ô loé; "bar" = "your bar = your loan's own rate"; "printed" tờ giấy trượt vào, NÂNG thanh lên; "stack" = "your stack = how
  far apart / the 15-year and 30-year offers sit", chồng trống co/giãn ở "how far apart" … "sit"; "dollar" tờ đô la từ tay Tessa bay vào cửa nhà;
  "hard" = "a dollar in the house is hard to get back" + khoá ở cửa, "back" tờ đô la bị khoá chặn; "fallback" ngoặc cushion + chồng của Tessa loé.
B32 (S32): "method" thẻ V7 đục "What this leaves out" + 6 dòng (giữ qua cả hai câu); "only"/"history" dòng góc gạch chân, "say" dòng cuối thẻ sáng.
B33 (S33, KEY-13): về khung cold open (thế giới, chỉ cụm Tessa; thanh dày): "tall" the stack loé, "high" the bar loé. → ĐỒ THỊ: "fifteen-year" thẻ
  "15-year mortgage", "thirty-year" thẻ "30-year paid in 15"; S33.3 "knows" Tessa nghiêng về thẻ, "thirty-year"/"fifteen-year" thẻ nảy, rồi hai thẻ TRƯỢT
  vào nhau thành MỘT thẻ ở "plus" ("30-year paid in 15 = 15-year + a fallback"), "fallback" dải cushion + thanh trượt vào cạnh chồng; "one" một tờ đô la
  rơi khỏi chồng, "week of Oct 8, 2026: $120 a month" dưới chân. Giữ tới hết (khúc đóng)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c4kit as K
SV, G = K.SV, K.G
M = json.load(open(os.path.join(K.EP, 'out', 'model.json')))
Q = {k: v['value'] for k, v in M['quantities'].items()}
S = K.Seg(['S29', 'S30', 'S31', 'S32', 'S33'])
B = [
 ('g0', 'S29.1', 'world', 'Leo (minh hoạ) vay 30 năm cùng cỡ ở tuần lãi thấp nhất, Jan 2021, cũng trả như 15 năm.', 'nhà + Leo mọc bên trái; nhãn; chồng của Leo xếp bó.',
  {'illustrative': '@S29.1:illustrative', 'january': '@S29.1:January', 'lowest': '@S29.1:lowest', 'paid': '@S29.1:paid'}, ['rise', 'tick', 'nốt dữ liệu mỗi bó'], 0.36, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('g1', 'S29.2', 'chart', 'Đường lui của Leo rẻ hơn: $13,231 qua 15 năm.', 'vạch từ đỉnh chồng Leo; nhãn.',
  {'cheaper': '@S29.2:cheaper', 'thirteen': '@S29.2:thirteen'}, ['tick', 'tick'], 0.4, 'hiểu', '—'),
 ('g2', 'S30.1', 'chart', 'Và rộng hơn: khoản bắt buộc thấp hơn khoản 15 năm ~$793.', 'hộp cushion Leo dâng; nhãn.',
  {'room': '@S30.1:room', 'seven': '@S30.1:seven'}, ['rise', 'tick'], 0.44, 'hiểu', '—'),
 ('g3', 'S30.2', 'chart', 'Nhưng the bar của Leo chỉ 2.65%.', 'thanh Leo trồi, thấp; nhãn.',
  {'bar': '@S30.2:bar', 'two': '@S30.2:two', 'earned': '@S30.2:earned'}, ['rise', 'nốt dữ liệu', 'tick'], 0.5, 'cân nhắc', '—'),
 ('g4', 'S30.3', 'chart', 'Cùng kế hoạch, khác tuần, ý nghĩa khác (đỉnh hồi 3).', 'hai cụm loé; thẻ tuần.',
  {'same': '@S30.3:Same', 'different': '@S30.3:different'}, ['nốt dữ liệu', 'tick'], 0.7, 'trầm ngâm', '—'),
 ('g5', 'S30.4', 'chart', 'Leo: chồng thấp, thanh thấp; Tessa: chồng cao, thanh cao.', 'loé lần lượt; nhãn Tessa.',
  {'short': '@S30.4:short', 'low': '@S30.4:low', 'tessa': '@S30.4:Tessa', 'tall': '@S30.4:tall', 'high': '@S30.4:high'}, ['nốt dữ liệu ×4', 'tick'], 0.62, 'trầm ngâm', 'lia ra'),
 ('h0', 'S31.1', 'chart', 'Người vay lãi cố định nào cũng đặt được cặp của mình cạnh cô.', 'ô thứ ba trống hiện (đế nét đứt + thanh trống + chồng trống), máy lia tới.',
  {'any': '@S31.1:Any', 'pair': '@S31.1:pair'}, ['nốt dữ liệu'], 0.46, 'mở', '—'),
 ('h1', 'S31.2', 'chart', 'Thanh = lãi của khoản vay; chồng = khoảng cách hai đề nghị 15 và 30 năm tuần đó.', 'thanh trống / chồng trống loé; hai nhãn.',
  {'bar': '@S31.2:bar', 'paper': '@S31.2:printed', 'stack': '@S31.2:stack', 'apart': '@S31.2:how', 'sit': '@S31.2:sit'}, ['tick', 'tick'], 0.46, 'rõ', '—'),
 ('h2', 'S31.3', 'chart', 'Vượt mốc chưa phải tất cả: đô la vào nhà khó lấy lại trong tháng khó.', 'nhà loé; nhãn; cushion của Tessa loé.',
  {'dollar': '@S31.3:dollar', 'house': '@S31.3:house', 'hard': '@S31.3:hard', 'back': '@S31.3:back', 'fallback': '@S31.3:fallback'}, ['tick', 'nốt dữ liệu'], 0.42, 'thận trọng', '—'),
 ('i0', 'S32.1', 'chart', 'Phần bỏ ngoài: trên thẻ phương pháp và mô tả.', 'thẻ V7.',
  {'method': '@S32.1:method'}, ['tick'], 0.3, 'bình thản', '—'),
 ('i1', 'S32.2', 'chart', 'Chỉ Mỹ, lịch sử, không dự báo; không nói chọn khoản vay nào.', 'dòng góc gạch chân; dòng cuối thẻ sáng.',
  {'only': '@S32.2:only', 'history': '@S32.2:history', 'say': '@S32.2:say'}, ['tick', 'tick'], 0.3, 'bình thản', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('j0', 'S33.1', 'world', 'Cạnh nhà Tessa giờ là một chồng cao và một thanh cao.', 'khung cold open; chồng loé, thanh loé.',
  {'tall': '@S33.1:tall', 'high': '@S33.1:high'}, ['nốt dữ liệu ×2'], 0.5, 'yên', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('j1', 'S33.2', 'chart', 'Cô hỏi: 15 năm, hay 30 năm trả trong 15?', 'hai thẻ khoản vay.',
  {'fifteen': '@S33.2:fifteen-year', 'thirty': '@S33.2:thirty-year'}, ['tick', 'tick'], 0.5, 'tò mò', '—'),
 ('j2', 'S33.3', 'chart', 'Câu trả lời: 30 năm trả trong 15 = 15 năm + đường lui; tuần 8/10/2026 đường lui giá $120/tháng.', 'hai thẻ nhập một; nhãn giá. Giữ.',
  {'knows': '@S33.3:knows', 'thirty': '@S33.3:thirty-year', 'fifteen': '@S33.3:fifteen-year', 'plus': '@S33.3:plus', 'fallback': '@S33.3:fallback', 'one': '@S33.3:one'}, ['rise', 'nốt dữ liệu', 'nốt dữ liệu'], 0.56, 'trầm ngâm', '(hết tập)'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c29', 'mode', 'wPair0', 'cPair', cue['g0']['illustrative'], cue['g0']['lowest'], 1.2,
     'lời S29–S30 đặt ngày, lãi, giá của Leo (số): đồ thị chính diện hai cụm, sau 5 s thế giới (quy tắc 7)', 'whoosh_mode', {'start': 5.0}),
    ('m_pan31', 'pan', 'cPair', 'cThree', cue['h0']['any'], cue['h0']['pair'], 1.6, 'lời S31.1 "Any fixed-rate borrower … their own pair beside hers": lia sang phải, máy hướng vào ô thứ ba khi nó hiện ("Any")', 'whoosh_soft', {}),
    ('m_w33', 'mode', 'cThree', 'wHome', cue['i1']['say'], cue['j0']['tall'], 1.5,
     'lời S33.1 "beside Tessa\'s house now stand…" (không số): về khung cold open, Tessa cạnh nhà', 'whoosh_mode', {}),
    ('m_c33', 'mode', 'wHome', 'cHome', cue['j0']['high'], cue['j1']['fifteen'], 1.2, 'lời S33.2–S33.3 đặt tên hai khoản vay + giá tuần (số): đồ thị chính diện', 'whoosh_mode', {}),
])
MV = {m['id']: m for m in moves}
assert MV['m_c29']['t0'] >= 5.0
nb = Q['leo_extra_vs15_total'] / G['bundle_usd']
bt = K.spread(cue['g0']['paid'], cue['g1']['cheaper'] - 0.3, 9)   # C5: từng bó (≈ 0,4 s/bó), xong trước vạch "cheaper"
leo_stack, ev = K.steps(bt, [min(Q['leo_extra_vs15_total'], G['bundle_usd'] * (k + 1)) if k < 8 else Q['leo_extra_vs15_total'] for k in range(9)],
                        ramp=0.08, v0=0.0, pitch=lambda v: 0.2 + 0.6 * v / G['stack_total'])
assert 8 < nb < 9.5
pitch = lambda r: round(0.15 + 0.07 * r, 3)
ev += [{'t': cue['g0']['illustrative'], 'kind': 'rise', 'dur': 1.0}, {'t': cue['g0']['lowest'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['g1']['cheaper'], 'kind': 'tick', 'v': 0.35}, {'t': cue['g1']['thirteen'], 'kind': 'tick', 'v': 0.5},
       {'t': cue['g2']['room'], 'kind': 'rise', 'dur': 0.8}, {'t': cue['g2']['seven'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['g3']['bar'], 'kind': 'rise', 'dur': 0.6}, {'t': cue['g3']['two'], 'kind': 'data', 'v': pitch(Q['leo_r30'])}, {'t': cue['g3']['earned'], 'kind': 'tick', 'v': 0.3},
       {'t': cue['g4']['same'], 'kind': 'data', 'v': 0.5}, {'t': cue['g4']['different'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['g5']['short'], 'kind': 'data', 'v': round(0.2 + 0.6 * Q['leo_extra_vs15_total'] / G['stack_total'], 3)}, {'t': cue['g5']['low'], 'kind': 'data', 'v': pitch(Q['leo_r30'])},
       {'t': cue['g5']['tessa'], 'kind': 'tick', 'v': 0.45}, {'t': cue['g5']['tall'], 'kind': 'data', 'v': 0.8}, {'t': cue['g5']['high'], 'kind': 'data', 'v': pitch(G['bar'])},
       {'t': cue['h0']['any'], 'kind': 'data', 'v': 0.5}, {'t': cue['h1']['bar'], 'kind': 'tick', 'v': 0.4}, {'t': cue['h1']['stack'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['h2']['hard'], 'kind': 'tick', 'v': 0.4}, {'t': cue['h2']['fallback'], 'kind': 'data', 'v': 0.45},
       {'t': cue['i0']['method'], 'kind': 'tick', 'v': 0.35}, {'t': cue['i1']['only'], 'kind': 'tick', 'v': 0.3}, {'t': cue['i1']['say'], 'kind': 'data', 'v': 0.35},   # dòng "Not advice…" sáng: nốt (không thêm sfx: ≤ 6 trong 10 s quanh hai lần đổi chế độ S33)
       {'t': cue['j0']['tall'], 'kind': 'data', 'v': 0.8}, {'t': cue['j0']['high'], 'kind': 'data', 'v': pitch(G['bar'])},
       {'t': cue['j1']['fifteen'], 'kind': 'tick', 'v': 0.4}, {'t': cue['j1']['thirty'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['j2']['plus'], 'kind': 'rise', 'dur': 0.8}, {'t': cue['j2']['fallback'], 'kind': 'data', 'v': 0.4},
       {'t': cue['j2']['one'], 'kind': 'data', 'v': 0.6, 'over': True}]
# ô thứ ba (C4 r4 + C5): người viền nét đứt bên trái, chồng trống giữa, thanh trống bên phải (dây dẫn của nhãn đi lề phải vào thanh, không cắt chồng);
# lot = đế [tâm x, rộng, sâu]. C5: Leo đứng sát nhà hơn, thanh của Leo xa đầu Leo; thẻ S33 cách xa nhau (thấy được cú trượt vào nhau)
X = {'leo_house': -4.2, 'leo_person': -5.35, 'leo_stack': -2.6, 'leo_bar': -6.75, 'leo_pin': -3.25, 'house': 1.1, 'stack': 2.75, 'bar': -1.3,
     'ghost': 3.75, 'blank_stack': 4.5, 'blank_bar': 5.6, 'lot': [4.8, 2.8, 1.6], 'cards': [-1.9, 4.3], 'merge': 1.2}
gestures = [{'t': cue['g4']['same'], 'kind': 'lean', 'to': X['leo_house'], 'hold': 1.4},
            {'t': cue['g5']['tessa'], 'kind': 'arm', 'to': X['stack'], 'hold': 1.4},
            {'t': cue['h0']['any'], 'kind': 'arm', 'to': X['lot'][0], 'hold': 2.0},
            {'t': cue['h2']['dollar'], 'kind': 'arm', 'to': X['house'], 'hold': 0.9},
            {'t': cue['h2']['hard'], 'kind': 'arm', 'to': X['house'], 'hold': 1.4},
            {'t': cue['h2']['fallback'], 'kind': 'lean', 'to': X['stack'], 'hold': 1.0},
            {'t': cue['j0']['tall'], 'kind': 'lean', 'to': X['stack'], 'hold': 1.0},
            {'t': cue['j0']['high'], 'kind': 'lean', 'to': X['bar'], 'hold': 1.0},
            {'t': cue['j2']['knows'], 'kind': 'lean', 'to': X['cards'][0], 'hold': 0.9},
            {'t': cue['j2']['thirty'], 'kind': 'arm', 'to': X['cards'][1], 'hold': 1.4},
            {'t': cue['j2']['plus'], 'kind': 'arm', 'to': X['merge'], 'hold': 1.8},
            {'t': cue['j2']['one'], 'kind': 'nod', 'hold': 0.6}]
leo_gestures = [{'t': cue['g0']['paid'], 'kind': 'arm', 'to': X['leo_stack'], 'hold': 1.4},
                {'t': cue['g3']['bar'], 'kind': 'lean', 'to': X['leo_bar'], 'hold': 1.2},
                {'t': cue['g5']['short'], 'kind': 'nod', 'hold': 0.5}]
K.finish(HERE, S, 'ep007 C4 · G = S29–S33 (Leo, ô thứ ba, thẻ phương pháp, câu trả lời của Tessa)', beats, moves, ev,
         {'x': X, 'gestures': gestures, 'leo_gestures': leo_gestures, 'leo_stack': leo_stack, 'leo_bar': Q['leo_r30'], 'gap': {'leo': Q['leo_fallback_gap'], 'tessa': Q['fallback_gap_now']},
          'leo_total': Q['leo_extra_vs15_total']},
         {'g0.lowest': 'Leo · Jan 2021 · 30-year at 2.65%', 'g1.thirteen': "Leo's stack: $13,231 ($74 a month)", 'g2.seven': 'about $793 a month below the 15-year',
          'g3.two': 'bar 2.65%', 'g4.different': 'Jan 2021', 'g5.high': 'bar 7.40%',
          'h1.bar': "your bar = your loan's own rate", 'h1.stack': 'your stack = how far apart', 'h2.hard': 'a dollar in the house is hard to get back',
          'i0.method': 'What this leaves out', 'j1.fifteen': '15-year mortgage', 'j1.thirty': '30-year paid in 15',
          'j2.plus': '30-year paid in 15 = 15-year + a fallback', 'j2.one': 'week of Oct 8, 2026: $120 a month'},
         ['g0.illustrative', 'g0.january', 'g0.lowest', 'g0.paid', 'g1.cheaper', 'g1.thirteen', 'g2.room', 'g2.seven', 'g3.bar', 'g3.two', 'g3.earned', 'g4.same', 'g4.different',
          'g5.short', 'g5.low', 'g5.tessa', 'g5.tall', 'g5.high', 'h0.any', 'h0.pair', 'h1.bar', 'h1.paper', 'h1.stack', 'h1.apart', 'h2.dollar', 'h2.house', 'h2.hard',
          'h2.back', 'h2.fallback', 'i0.method', 'i1.only', 'i1.history', 'i1.say', 'j0.tall', 'j0.high', 'j1.fifteen', 'j1.thirty', 'j2.knows', 'j2.thirty', 'j2.fifteen',
          'j2.plus', 'j2.fallback', 'j2.one'],
         accents=[cue['g4']['same'], cue['j2']['one']])
