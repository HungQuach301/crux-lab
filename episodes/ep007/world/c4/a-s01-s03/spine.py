"""Tập 7 · C4 · ĐOẠN A = S01–S03 + ident (cold open). Lời + giờ = timeline của nhà máy (c4kit.Seg, 0 ký tự EL).
  python3 episodes/ep007/world/c4/a-s01-s03/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, lặng, 'land')
B01 (S01, bản C3 s01-stack đã duyệt + hàng chờ C4 gates/C3.md §3 #1–#2): Tessa cạnh nhà; "costs" = bó đầu trồi ra ở bậc cửa (thế giới);
"borrowing" = TẤM GIẤY VAY (vật riêng gắn với nhà, LoanTag) hiện trước góc nhà — khoản vay không phải chồng; → ĐỒ THỊ từ 5,0 s (quy tắc 7), bó đầu
bay từ cửa, CHẠM chồng ở 5,94 s cùng lúc "price of the fallback: $120 a month" (C3 câu 3 = a), Tessa giơ tay về phía chồng; chồng DỪNG ở bó
đầu (không mọc trong lời "$320,000"; không bó nào ở lại cửa nhà); "dollars" = "$320,000 loan · week of Oct 8, 2026" trên tấm giấy vay.
B02 (S02): "fifteen-year" / "thirty-year" = hai thẻ khoản vay treo trên Tessa (V4 adapted), "kept" = dải cushion (đường lui) trên thẻ 30 năm;
lùi máy → "every" = dải 1.833 tuần sau nhà (V1 xem trước) "every week since Aug 1991"; "price" = mỗi ô mọc thành cột giá đường lui của tuần đó;
"extra" = một tờ đô la trong tay Tessa (xem trước the bar).
B03 (S03): đẩy máy về hai thẻ: "illustrative" tên Tessa loé; "October" = "week of Oct 8, 2026"; "six" / "seven" = lãi 6.73% / 7.40% trên hai thẻ;
về thế giới ở S03.2: "only", "history" = dòng góc "US only · history, not a forecast" gạch chân; "say" = đối trọng "Not advice on which loan, or
on investing"; ident 3 s: thế giới tối dần (nhạc hiệu A do music.post phát)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W7)
import c4kit as K
SV, G = K.SV, K.G
M = json.load(open(os.path.join(K.EP, 'out', 'model.json')))
S = K.Seg(['S01', 'S02', 'S03'])
B = [
 ('a0', 'S01.1', 'world', 'Đường lui trong khoản vay của Tessa có giá mỗi tháng.', 'Tessa cạnh nhà; bó tiền (warn) trồi ra ở bậc cửa ("costs").',
  {'costs': '@S01.1:costs', 'month': '@S01.1:month'}, ['nốt dữ liệu khi bó ra cửa'], 0.3, 'tò mò', '—'),
 ('a1', 'S01.2', 'chart', 'Vay $320,000; khoản trả là hoá đơn lớn nhất.', 'tấm giấy vay ("borrowing", thế giới) → đồ thị: bó đầu chạm chồng + nhãn giá (5,94 s); nhãn khoản vay ("dollars").',
  {'borrowing': '@S01.2:borrowing', 'dollars': '@S01.2:dollars'}, ['tick tấm giấy vay', 'nốt dữ liệu khi bó chạm', 'tick nhãn'], 0.45, 'tò mò', '—'),
 ('a2', 'S02.1', 'chart', 'Câu hỏi: khoản 15 năm, hay 30 năm trả xong trong 15 năm, giữ khoản trả thấp cho tháng khó?', 'hai thẻ khoản vay treo trên Tessa; dải cushion trên thẻ 30 năm.',
  {'fifteen': '@S02.1:fifteen-year', 'thirty': '@S02.1:thirty-year', 'kept': '@S02.1:kept'}, ['nốt dữ liệu mỗi thẻ', 'tick dải'], 0.5, 'tò mò', 'lùi máy'),
 ('a3', 'S02.2', 'chart', 'Lời hứa: phát lại mọi tuần khảo sát lãi Mỹ, định giá đường lui bằng đô la, và đô la trả thêm được gì.', 'dải 1.833 tuần mọc trái → phải; mỗi ô thành cột giá; tờ đô la trong tay Tessa.',
  {'every': '@S02.2:every', 'surveys': '@S02.2:surveys', 'price': '@S02.2:price', 'extra': '@S02.2:extra'}, ['rise', 'tick', 'rise', 'nốt dữ liệu'], 0.56, 'hé lộ', 'đẩy máy'),
 ('a4', 'S03.1', 'chart', 'Tessa minh hoạ, lãi thật tuần 8/10/2026: 15 năm 6,73 %, 30 năm 7,40 %.', 'hai thẻ: tuần + hai mức lãi.',
  {'illustrative': '@S03.1:illustrative', 'october': '@S03.1:October', 'six': '@S03.1:six', 'seven': '@S03.1:seven'}, ['tick', 'nốt dữ liệu mỗi lãi'], 0.42, 'bình thản', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('a5', 'S03.2', 'world', 'Chỉ Mỹ, lịch sử, không dự báo.', 'dòng góc gạch chân.',
  {'only': '@S03.2:only', 'history': '@S03.2:history'}, [], 0.36, 'bình thản', '—'),
 ('a6', 'S03.3', 'world', 'Không nói chọn khoản vay nào, có nên đầu tư không.', 'đối trọng "Not advice on which loan, or on investing".',
  {'say': '@S03.3:say'}, ['tick'], 0.34, 'bình thản', 'ident'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
LAND = 5.94                                    # C3 câu 3 = a: nhãn giá ở 5,94 s (sớm nhất mà "≥ 5 s đầu ở thế giới" + số chỉ ở đồ thị cho phép)
beats[1]['cues']['land'] = LAND; cue['a1']['land'] = LAND
# "seven" của "seven point four" là lần THỨ HAI trong S03.1 (lần đầu: "six point seven three") — Anchors.at lấy lần đầu, nên đặt tay theo đầu từ
SEVEN2 = [w['s'] for w in S.words if w['sid'] == 'S03.1' and w['w'].lower().startswith('seven')][1]
beats[4]['cues']['seven'] = SEVEN2; cue['a4']['seven'] = SEVEN2
IDENT = [round(S.end['S03'] - 3.0, 3), S.end['S03']]
moves = K.moves_of([
    ('m_push0', 'push', 'wS0', 'wS', 0.0, cue['a0']['costs'], 1.0, 'mở đoạn: máy lại gần Tessa và cửa nhà trước khi bó đầu ra ("costs")', 'whoosh_air', {}),
    ('m_c1', 'mode', 'wS', 'cS', cue['a1']['borrowing'], LAND, 0.52,   # 0,52 s: tiếng chạm (0,3 s) xong trước "twenty" (5,82), không đè nhãn giá
     'giá $120 chỉ hiện ở chế độ đồ thị (quy tắc 1) → đồ thị ngay sau 5 s thế giới (quy tắc 7), xong trước khi bó đầu chạm chồng', 'whoosh_mode', {'start': 5.0}),
    ('m_pull', 'pull', 'cS', 'cStrip', cue['a2']['kept'], cue['a3']['every'], 1.6,
     'lời S02.2 "we replayed every week": lùi máy cho chỗ dải mọi tuần sau nhà (V1 xem trước)', 'whoosh_soft', {}),
    ('m_push', 'push', 'cStrip', 'cCards', cue['a3']['extra'], cue['a4']['illustrative'], 1.3,
     'lời S03.1 đặt lãi thật của tuần lên hai khoản vay: đẩy máy về hai thẻ', 'whoosh_push', {}),
    ('m_w', 'mode', 'cCards', 'wEnd', cue['a4']['seven'], cue['a5']['only'], 1.2,
     'lời S03.2 "US only … history": lớp bắt buộc đứng riêng, về Tessa và nhà (thế giới)', 'whoosh_mode', {'start': SEVEN2 + 1.4}),
])
MV = {m['id']: m for m in moves}
assert MV['m_c1']['t0'] >= 5.0 and MV['m_c1']['t1'] <= LAND - K.PAD, MV['m_c1']
FLY = 0.6
OUT0 = cue['a0']['costs']
stack, ev = K.steps([LAND], [G['bundle_usd']], ramp=0.05, v0=0.0, pitch=lambda v: 0.45)      # ĐÚNG MỘT bó (dừng sau bó đầu)
ev += [{'t': round(OUT0, 3), 'kind': 'data', 'v': 0.2},
       {'t': cue['a1']['borrowing'], 'kind': 'tick', 'v': 0.35}, {'t': cue['a1']['dollars'], 'kind': 'tick', 'v': 0.5},
       {'t': cue['a2']['fifteen'], 'kind': 'data', 'v': 0.5}, {'t': cue['a2']['thirty'], 'kind': 'data', 'v': 0.62}, {'t': cue['a2']['kept'], 'kind': 'tick', 'v': 0.4},
       {'t': cue['a3']['every'], 'kind': 'rise', 'dur': 1.3}, {'t': cue['a3']['surveys'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['a3']['price'], 'kind': 'rise', 'dur': 1.4}, {'t': cue['a3']['extra'], 'kind': 'data', 'v': 0.7},
       {'t': cue['a4']['october'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['a4']['six'], 'kind': 'data', 'v': 0.673}, {'t': cue['a4']['seven'], 'kind': 'data', 'v': 0.74},
       {'t': cue['a6']['say'], 'kind': 'tick', 'v': 0.3}]                  # ident: không sfx (nhạc hiệu A phát ở 3 s cuối đuôi S03, music.post)
CARD_A, CARD_B, STACK_X = -1.65, 1.65, 1.85
gestures = [{'t': LAND, 'kind': 'arm', 'to': STACK_X, 'hold': 1.4},                       # bó chạm chồng (đồ thị): Tessa giơ tay về phía chồng
            {'t': S.at('@S01.2:biggest'), 'kind': 'nod', 'hold': 0.5},
            {'t': cue['a2']['thirty'], 'kind': 'lean', 'to': CARD_B, 'hold': 1.0},       # thẻ 30 năm hiện
            {'t': cue['a3']['extra'], 'kind': 'arm', 'to': 3.0, 'hold': 2.4},           # tờ đô la trả thêm trong tay
            {'t': cue['a4']['seven'], 'kind': 'lean', 'to': CARD_B, 'hold': 1.0}]        # lãi 30 năm lên thẻ
K.finish(HERE, S, 'ep007 C4 · A = S01–S03 + ident (cold open)', beats, moves, ev,
         {'stack': stack, 'land': LAND, 'fly': FLY, 'out0': round(OUT0, 3), 'ident': IDENT, 'gestures': gestures, 'cards': [CARD_A, CARD_B], 'stack_x': STACK_X,
          'weeks_extra': M['series']['extra_total']},
         {'a1.land': 'price of the fallback:','a1.dollars': '$320,000 loan · week of Oct 8, 2026', 'a2.fifteen': '15-year mortgage',
          'a2.thirty': '30-year paid in 15', 'a3.surveys': 'every week since Aug 1991', 'a4.october': 'week of Oct 8, 2026', 'a4.six': '6.73%',
          'a4.seven': '7.40%', 'a6.say': 'Not advice on which loan, or on investing'},
         ['a0.costs', 'a1.borrowing', 'a1.land', 'a1.dollars', 'a2.fifteen', 'a2.thirty', 'a2.kept', 'a3.every', 'a3.surveys', 'a3.price', 'a3.extra',
          'a4.illustrative', 'a4.october', 'a4.six', 'a4.seven', 'a5.only', 'a5.history', 'a6.say'],
         accents=[LAND])
