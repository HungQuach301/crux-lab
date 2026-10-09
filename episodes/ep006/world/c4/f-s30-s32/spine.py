"""Tập 6 · C4 · ĐOẠN F = S30–S32 (mức tăng nào đã theo kịp · giới hạn + thẻ phương pháp V7 · kết). Lời + giờ = timeline của nhà máy (0 ký tự EL).
  python3 episodes/ep006/world/c4/f-s30-s32/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7)
B30 (V10 thang, c4kit.Ladder): thế giới — bốn bậc (2 %, 3 %, 3,1 %, 6,38 %) như bậc thang, "three" (S30.2) = bậc 3 % sáng ở thế giới; → ĐỒ THỊ
từ 5,05 s (quy tắc 7: đoạn mở ≥ 5 s ở thế giới), xong trước "forty-two": thanh của mỗi bậc = phần quãng 20 năm theo kịp:
2 %: 2.4% (từ hồi 2) · "forty" = 3 %: 42.4% · "half" = 3.1%: half (+ "a median of the past, not an expectation") · "Carl's" = 6.38%: all;
"choose" = đối trọng "Not advice on which check or raise".
B31: giới hạn — "national" = hàng 10 thùng chung + "a national average, not one retiree's basket"; "overlap" = các thanh 20 năm chồng nhau
"overlapping stretches, not 715 separate tests"; "dollars" = hai séc + "?" "dollars paid out: not compared"; "card" = thẻ V7 (≤ 6 dòng, giữ 5 s).
B32: về khung mở đầu (thế giới): Ruth, séc, 9/10 thùng; "fifteen" = séc loé; → đồ thị ở "eighty-five": "Ruth · ILLUSTRATIVE · age 85", ngoặc
"about 9 in 10" ở "nine", ngoặc 10 ở "ten"; khúc đóng A chạm 0,6 s sau chữ cuối (bed.py), máy đứng yên."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W6 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W6)
import c4kit as K
SV = K.SV
S = K.Seg(['S30', 'S31', 'S32'])
B = [
 ('g0', 'S30.1', 'world', 'Vậy mức tăng nào đã theo kịp, trong lịch sử này?', 'bậc thang bốn mức tăng.',
  {'raise': '@S30.1:raise', 'history': '@S30.1:history'}, ['rise'], 0.48, 'tò mò', '—'),
 ('g1', 'S30.2', 'chart', 'Tăng 3 %/năm theo kịp ở 42,4 % số quãng.', 'bậc 3 % sáng (thế giới) → đồ thị; thanh bậc 3 % tới 42,4 %.',
  {'three': '@S30.2:three', 'forty': '@S30.2:forty-two'}, ['data'], 0.58, 'chú ý', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('g2', 'S30.3', 'chart', 'Khoảng 3,1 % theo kịp một nửa — trung vị quá khứ, không phải kỳ vọng.', 'thanh bậc 3,1 % tới nửa; nhãn trung vị.',
  {'three': '@S30.3:three', 'half': '@S30.3:half', 'median': '@S30.3:median'}, ['data'], 0.6, 'thận trọng', '—'),
 ('g3', 'S30.4', 'chart', 'Theo kịp mọi quãng cần mức của những năm của Carl.', 'thanh bậc 6,38 % tới hết.',
  {'every': '@S30.4:every', 'carls': '@S30.4:Carl'}, ['data'], 0.66, 'nặng', '—'),
 ('g4', 'S30.5', 'chart', 'Các mức này mô tả giá đã làm gì; video không nói chọn séc/mức nào.', 'đối trọng.',
  {'describe': '@S30.5:describe', 'choose': '@S30.5:choose'}, [], 0.42, 'thận trọng', 'lia → giới hạn'),
 ('h0', 'S31.1', 'chart', 'Chỉ số là trung bình quốc gia, không phải giỏ của người về hưu.', 'hàng 10 thùng chung + nhãn.',
  {'national': '@S31.1:national', 'health': '@S31.1:health'}, [], 0.24, 'thận trọng', '—'),
 ('h1', 'S31.2', 'chart', '715 quãng chồng nhau, không phải 715 phép thử riêng.', 'các thanh 20 năm chồng nhau.',
  {'overlap': '@S31.2:overlap', 'separate': '@S31.2:separate'}, [], 0.24, 'thận trọng', 'lia'),
 ('h2', 'S31.3', 'chart', 'Giá niên kim không mô hình hoá: không so tiền hai séc.', 'hai séc + "?".',
  {'annuity': '@S31.3:annuity', 'dollars': '@S31.3:dollars'}, [], 0.22, 'thận trọng', '—'),
 ('h3', 'S31.4', 'chart', 'Phương pháp: trên thẻ này và trong mô tả.', 'thẻ V7 giữ 5 s.',
  {'card': '@S31.4:card'}, [], 0.22, 'bình thản', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('i0', 'S32.1', 'world', 'Chỉ Mỹ, lịch sử, không dự báo.', 'Ruth + séc + hàng thùng (khung mở đầu).',
  {'only': '@S32.1:only'}, [], 0.3, 'suy nghĩ', '—'),
 ('i1', 'S32.2', 'world', 'Hai mươi năm trước Ruth hỏi 2 %/năm có theo kịp giá.', 'Ruth loé.',
  {'ruth': '@S32.2:Ruth', 'keep': '@S32.2:keep'}, [], 0.36, 'ấm', '—'),
 ('i2', 'S32.3', 'world', 'Câu trả lời: 15 năm phần lớn có; ở 85, séc mua khoảng 9 thùng trên 10.', 'đồ thị: about 9 in 10.',
  {'fifteen': '@S32.3:fifteen', 'yes': '@S32.3:yes', 'eighty': '@S32.3:eighty-five', 'nine': '@S32.3:nine', 'ten': '@S32.3:ten'}, ['tick'], 0.42, 'trầm', '(hết)'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c30', 'mode', 'wLadder', 'cLadder', cue['g1']['three'], cue['g1']['forty'], 1.2,
     'lời S30.2 đặt số (42,4 %): số chỉ ở đồ thị (quy tắc 1); bậc 3 % đã sáng ở thế giới ("three"), đồ thị từ 5 s (quy tắc 7)', 'whoosh_mode', {'start': 5.05}),
    ('m_pan31', 'pan', 'cLadder', 'cLim1', S.at('@S30.5$'), cue['h0']['national'], 1.2, 'lời S31.1 giới hạn của chỉ số (giỏ quốc gia): lia sang hàng thùng chung', 'whoosh_soft', {}),
    ('m_pan31b', 'pan', 'cLim1', 'cLim2', S.at('@S31.2:tests'), cue['h2']['annuity'], 0.75, 'lời S31.3 "annuity pricing isn\'t modeled": lia sang hai séc', 'whoosh_soft', {}),
    ('m_w32', 'mode', 'cLim2', 'wRuth', S.at('@S31.4$'), cue['i0']['only'], 1.2, 'lời S32 quay về câu hỏi của Ruth: về khung mở đầu (thế giới), sau 5 s thẻ V7', 'whoosh_mode', {'late': True}),
    ('m_c32', 'mode', 'wRuth', 'cRuth', cue['i2']['yes'], cue['i2']['eighty'], 0.9, 'lời S32.3 đặt số (85, about 9 of 10): số chỉ ở đồ thị (quy tắc 1)', 'whoosh_mode', {}),
])
card = [round(cue['h3']['card'], 3), round(moves[3]['t0'] - 0.1, 3)]
assert card[1] - card[0] >= 5.0, ('thẻ V7 < 5 s', card)
ev = [{'t': cue['g0']['raise'], 'kind': 'rise', 'dur': 1.2}, {'t': cue['g1']['forty'], 'kind': 'data', 'v': 0.424},
      {'t': cue['g2']['half'], 'kind': 'data', 'v': 0.5}, {'t': cue['g3']['carls'], 'kind': 'data', 'v': 1.0},
      {'t': cue['i2']['nine'], 'kind': 'tick', 'v': 0.5}]
K.finish(HERE, S, 'ep006 C4 · F = S30–S32 (thang mức tăng · giới hạn + V7 · kết)', beats, moves, ev,
         {'card': card, 'ruth_end': K.P['ruth'][-1],
          'rungs': [{'id': 'r2', 'label': '2%', 'share': K.GRID['raise_grid']['0.020'], 'value': '2.4%'},
                    {'id': 'r3', 'label': '3%', 'share': K.GRID['raise_grid']['0.030'], 'value': '42.4%'},
                    {'id': 'r31', 'label': '3.1%', 'share': 50.0, 'value': 'half'},
                    {'id': 'r638', 'label': '6.38%', 'share': 100.0, 'value': "all · Carl's stretch"}]},
         {'g2.median': 'a median of the past, not an expectation', 'g4.choose': 'Not advice on which check or raise',
          'h0.national': "a national average, not one retiree's basket", 'h1.overlap': 'overlapping stretches, not 715 separate tests',
          'h2.dollars': 'dollars paid out: not compared', 'i2.eighty': 'Ruth · ILLUSTRATIVE · age 85', 'i2.nine': 'about 9 in 10',
          'i2.ten': 'first check: 10 crates', 'card0': 'How we know this',
          'card1': 'Prices: CPI-U all items, US city average (FRED CPIAUCNS), to Aug 2026',
          'card2': '715 overlapping 20-year stretches, Jan 1947 to Aug 2006',
          'card3': 'Check rises 2% once a year; measured against its first check',
          'card4': 'Not modeled: annuity pricing, taxes, insurer risk, own basket',
          'card5': 'Also run: CPI-W 21 of 715 · PCE 19.2% (description)'},
         ['g0.raise', 'g1.three', 'g1.forty', 'g2.half', 'g2.median', 'g3.carls', 'g4.choose', 'h0.national', 'h1.overlap', 'h2.dollars', 'h3.card',
          'i1.ruth', 'i2.fifteen', 'i2.eighty', 'i2.nine', 'i2.ten'],
         accents=[cue['g1']['forty'], cue['i2']['nine']], rule7=True)
