"""Tập 8 · ĐOẠN A = S01–S03 + ident (cold open v3, chương 1 "Nina's door"). Lời + giờ = timeline của nhà máy (kit.Seg, 0 ký tự EL).
  [CRUX_GREY=1] python3 episodes/ep008/world/seg/a-s01-s03/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, lặng, 'land')
B01 (S01): phố-lưới lúc chạng vạng, MỌI nhà chưa sáng; máy đẩy dọc phố tới cửa căn hộ của Nina ở QUA CUỐI PHỐ (thế giới 5 s đầu) → đồ thị: hai chồng
cạnh Nina — tiền thuê của cô (renter, warn) thấp hơn tháng đầu của người mua (buyer, lit); nhãn tỉ lệ ở "smaller", mốc thấp nhất ở "replayed"; S01.3 hai chồng
tiền để dành (đặt cọc / chi phí đóng) + nhà $400,000. B02 (S02): lưới nhìn từ trên (cột = năm, hàng = tháng, dừng ở cột 2016): 72 ô 2002–2007 tối dần, 6 ô
sáng trong đó; rồi lưới 15 năm sáng hết; câu hỏi của Nina trên lưới. B03 (S03): mọi ô hiện ("every month since 1991"), hai ô cùng luật — April 2012 sáng,
June 2006 tối ("opposite answers"); lưới mọc thành phố (thế giới), dòng góc + "Not advice on whether to buy or rent"; máy đi dọc phố tới Nina + người song
sinh ở cửa; ident: thế giới tối dần."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W8 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W8)
import kit as K
SV = K.SV
S = K.Seg(['S01', 'S02', 'S03'])
B = [
 ('a0', 'S01.1', 'world', 'Tháng 9/2026: tiền thuê của Nina trông rẻ so với mua.', 'phố chạng vạng chưa sáng; đẩy máy tới cửa căn hộ của Nina qua cuối phố.',
  {'cheap': '@S01.1:cheap'}, ['lamp hum'], 0.3, 'nặng', 'đẩy máy'),
 ('a1', 'S01.2', 'chart', 'So với tháng đầu của người mua, tiền thuê của cô nhỏ hơn mọi tháng đã phát lại.', 'hai chồng: tiền thuê (warn) thấp hơn tháng đầu người mua (lit); nhãn tỉ lệ.',
  {'smaller': '@S01.2:smaller', 'replayed': '@S01.2:replayed'}, ['tick nhãn'], 0.42, 'bất an', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a2', 'S01.3', 'chart', 'Nina có tiền đặt cọc cho căn nhà $400,000.', 'hai chồng tiền để dành cạnh Nina; nhãn giá nhà.',
  {'down': '@S01.3:down', 'four': '@S01.3:four'}, ['bịch giấy ×2'], 0.46, 'tò mò', '—'),
 ('a3', 'S02.1', 'chart', '72 tháng liền, người mua chỉ hơn 6 lần.', 'lưới từ trên: khối 2002–2007 tối, 6 ô sáng.',
  {'seventy': '@S02.1:seventy-two', 'six': '@S02.1:six'}, ['chuỗi bịch trầm', 'tinh ×6'], 0.52, 'ngạc nhiên', 'lia máy → lưới'),
 ('a4', 'S02.2', 'chart', 'Nhưng giữ 15 năm, người mua lần nào cũng hơn.', 'lưới 15 năm: mọi ô sáng.',
  {'fifteen': '@S02.2:fifteen', 'every': '@S02.2:every'}, ['chuỗi tinh'], 0.58, 'nghi', '—'),
 ('a5', 'S02.3', 'chart', 'Câu hỏi: tiền thuê của cô có phí không?', 'câu hỏi trên lưới tắt.',
  {'wasted': '@S02.3:wasted'}, [], 0.5, 'lo', '—'),
 ('a6', 'S03.1', 'chart', 'Lời hứa: phát lại mọi tháng từ 1991; cùng luật, đáp án ngược nhau.', 'mọi ô hiện; hai ô cùng luật: một sáng, một tối.',
  {'every': '@S03.1:every', 'ten': '@S03.1:ten', 'same': '@S03.1:same'}, ['tick', 'tinh', 'bịch'], 0.54, 'tò mò', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('a7', 'S03.2', 'world', 'Lịch sử, không dự báo.', 'lưới mọc thành phố; dòng góc gạch chân; không phải lời khuyên.',
  {'history': '@S03.2:history'}, [], 0.4, 'bình thản', '—'),
 ('a8', 'S03.3', 'world', 'Một con phố đáp án, mỗi tháng một nhà.', 'máy đi dọc phố; nhà đầu tiên loé.',
  {'street': '@S03.3:street', 'house': '@S03.3:house'}, ['gõ gỗ'], 0.36, 'bình thản', 'lia máy'),
 ('a9', 'S03.4', 'world', 'Mỗi nhà cùng một cặp song sinh, cùng một lựa chọn.', 'Nina + người song sinh ở cửa.',
  {'twins': '@S03.4:twins'}, ['bước chân'], 0.36, 'ấm', 'ident'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
IDENT = [round(S.end['S03'] - 3.0, 3), S.end['S03']]
moves = K.moves_of([
    ('m_push', 'push', 'w0', 'wDoor', 0.0, cue['a0']['cheap'], 2.4, 'mở: dọc phố chưa sáng tới cửa của Nina (gần = áp lực)', 'whoosh_air', {}),
    ('m_c1', 'mode', 'wDoor', 'cStacks', cue['a0']['cheap'], cue['a1']['smaller'], 1.2, 'tỉ lệ chỉ hiện ở đồ thị (quy tắc 1) sau 5 s thế giới (quy tắc 7)', 'whoosh_mode', {'start': 5.0}),
    ('m_grid', 'pull', 'cStacks', 'cGrid', cue['a2']['four'], cue['a3']['seventy'], 1.5, 'S02 nói về các tháng đã phát lại: lùi máy lên lưới phố nhìn từ trên', 'whoosh_soft', {'late': True}),
    ('m_w', 'mode', 'cGrid', 'wStreet', cue['a6']['same'], cue['a7']['history'], 1.6, 'S03.2 lịch sử: lưới mọc lại thành phố (thế giới)', 'whoosh_mode', {'start': cue['a6']['same'] + 1.0}),
    ('m_pan', 'pan', 'wStreet', 'wNina', cue['a8']['house'], cue['a9']['twins'], 1.8, 'S03.4: dọc phố tới cửa của Nina, nơi cặp song sinh đứng', 'whoosh_soft', {}),
])
MV = {m['id']: m for m in moves}
ev = [{'t': cue['a1']['smaller'], 'kind': 'tick', 'v': 0.4}, {'t': cue['a1']['replayed'], 'kind': 'tick', 'v': 0.45},
      {'t': cue['a2']['down'], 'kind': 'data', 'v': 0.4},
      {'t': cue['a3']['seventy'], 'kind': 'data', 'v': 0.25}, {'t': cue['a3']['six'], 'kind': 'data', 'v': 0.6},
      {'t': cue['a4']['fifteen'], 'kind': 'rise', 'dur': 1.4}, {'t': cue['a4']['every'], 'kind': 'data', 'v': 0.8},
      {'t': cue['a6']['every'], 'kind': 'rise', 'dur': 1.2}, {'t': cue['a6']['same'], 'kind': 'data', 'v': 0.5},
      {'t': cue['a8']['house'], 'kind': 'tick', 'v': 0.35}, {'t': cue['a9']['twins'], 'kind': 'tick', 'v': 0.3}]
K.finish(HERE, S, 'ep008 · A = S01–S03 + ident (cold open, chương 1)', beats, moves, ev,
         {'ident': IDENT, 'chapter': [0.3, "Nina's door"], 'at': {k: S.at('@' + k) for k in ('S01.2:buyers', 'S01.2:rent', 'S01.3:payment', 'S03.1:one', 'S03.1:renting')}},
         {'a1.smaller': "rent ÷ buyer's first month: 56.8%", 'a1.replayed': 'lowest replayed: 57.9%', 'a2.down': '$80,000 down · $12,000 closing', 'a2.four': '$400,000 home',
          'a3.six': '72 start months in a row: 6 of 72', 'a4.every': '15 years: every one (100%)', 'a5.wasted': 'Is her rent money wasted?',
          'a6.ten': 'every start month since January 1991 · ten years each', 'a6.same': 'same rules · opposite answers'},
         ['a0.cheap', 'a1.smaller', 'a1.replayed', 'a2.down', 'a2.four', 'a3.seventy', 'a3.six', 'a4.fifteen', 'a4.every', 'a5.wasted', 'a6.every', 'a6.ten', 'a6.same',
          'a7.history', 'a8.street', 'a8.house', 'a9.twins'])
