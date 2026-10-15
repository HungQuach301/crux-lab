"""Tập 9 · ĐOẠN A = S01–S03 + ident (cold open, chương 1 "Two piles, one street"). Lời + giờ = timeline nhà máy (kit.Seg; M2: take khô, 0 ký tự EL).
  [CRUX_GREY=1] python3 episodes/ep009/world/seg/a-s01-s03/spine.py → spine.json (thoát 1 nếu vi phạm quy tắc 2/3/7, lặng, 'land')
B01 (S01.1, thế giới 5 s đầu): phố chạng vạng chưa sáng; sau phố một bức tường 307 cặp cột mọc lên — cột cổ phiếu cao hơn cột giá nhà ở gần như mọi cặp
→ đồ thị chính diện bức tường, nhãn "about 9 in 10" (S02.1) → Nina + hộp CASH, "$92,000 saved". B03 (S02.2–S02.3): phố nhìn cao (chế độ đồ thị): hộp CASH
đặt cạnh, đèn sáng theo bản tiền mặt (3 in 4); hộp đổi thành đống cổ phiếu N6, đèn quét lại theo bản cổ phiếu (nửa). B04 (S03.1): phố rút còn 247 nhà
(15 năm): tiền mặt sáng hết → cổ phiếu tắt gần hết. B05 (S03.2): thế giới, Nina nhìn dọc phố, câu hỏi. S03.3 nghịch lý: bức tường cột + phố nửa sáng.
S03.4 gạch chân "history, not a forecast". B06 (S03.5–S03.7): phố hiện từng nhà, chú giải sáng/tối → đống N6: khối $92,000 + bó mỗi tháng, một tháng
đống tụt mà bó vẫn rơi vào. Ident: thế giới tối dần."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W9 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W9)
import kit as K
SV = K.SV
S = K.Seg(['S01', 'S02', 'S03'])
B = [
 ('a0', 'S01.1', 'world', 'Cổ phiếu tăng hơn giá nhà ở gần như mọi khoảng 10 năm.', 'phố chưa sáng; bức tường cặp cột mọc sau phố, cột cổ phiếu cao hơn.',
  {'stocks': '@S01.1:stocks', 'nine': '@S01.1:nine'}, ['rise'], 0.35, 'nghịch lý', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a1', 'S02.1', 'chart', 'Nên thuê có vẻ khôn; Nina thuê, có $92,000.', 'bức tường chính diện + nhãn; lia tới Nina, hộp CASH, nhãn tiền để dành.',
  {'so': '@S02.1:renting', 'saved': '@S02.1:saved'}, ['tick'], 0.4, 'tò mò', 'lia máy'),
 ('a2', 'S02.2', 'chart', 'Người thuê giữ tiền mặt → người mua hơn khoảng 3/4.', 'phố nhìn cao; hộp CASH; đèn sáng theo bản tiền mặt.',
  {'cash': '@S02.2:cash', 'ahead': '@S02.2:ahead'}, ['tinh ×n'], 0.45, 'ngạc nhiên', '—'),
 ('a3', 'S02.3', 'chart', 'Cùng tiền đó vào cổ phiếu → chỉ khoảng nửa.', 'hộp đổi thành đống cổ phiếu; đèn tắt quét nửa phố.',
  {'stocks': '@S02.3:stocks', 'half': '@S02.3:half'}, ['giấy', 'bịch'], 0.55, 'bất ngờ', '—'),
 ('a4', 'S03.1', 'chart', '15 năm: tiền mặt sáng hết; cổ phiếu khoảng 1/5.', 'phố rút còn 247 nhà; sáng hết → tắt gần hết.',
  {'fifteen': '@S03.1:fifteen', 'every': '@S03.1:every', 'stocks': '@S03.1:stocks'}, ['rise', 'bịch'], 0.6, 'lật', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('a5', 'S03.2', 'world', 'Câu hỏi của Nina: thuê và đầu tư phần chênh có hơn mua?', 'Nina ở cửa nhìn dọc phố, đèn của cô.',
  {'invests': '@S03.2:invests'}, [], 0.45, 'lo', '—'),
 ('a6', 'S03.3', 'world', 'Nghịch lý: cổ phiếu tăng hơn 9/10 mà mua vẫn hơn ở nửa.', 'bức tường cột sau phố nửa sáng.',
  {'outgrew': '@S03.3:outgrew', 'half': '@S03.3:half'}, ['tinh'], 0.5, 'nghịch lý', '—'),
 ('a7', 'S03.4', 'world', 'Lịch sử, không dự báo.', 'dòng góc gạch chân.', {'history': '@S03.4:history'}, [], 0.4, 'bình thản', '—'),
 ('a8', 'S03.5', 'world', 'Mỗi tháng từ 1991 là một nhà; sáng = người mua hơn, tối = không.', 'nhà hiện lần lượt; một nhà sáng, một nhà tối; chú giải.',
  {'replayed': '@S03.5:replayed', 'lit': '@S03.5:lit'}, ['gõ gỗ'], 0.4, 'rõ', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('a9', 'S03.6', 'chart', 'Đống của người thuê = $92,000 + chênh mỗi tháng.', 'kệ N6: khối $92,000, bó nhỏ mỗi tháng.',
  {'pile': '@S03.6:pile', 'plus': '@S03.6:plus'}, ['giấy'], 0.45, 'rõ', '—'),
 ('a10', 'S03.7', 'chart', 'Tất cả vào cổ phiếu Mỹ mỗi tháng, kể cả khi tụt.', 'đống lên xuống theo tháng; tụt mà bó vẫn rơi vào.',
  {'market': '@S03.7:market', 'drop': '@S03.7:drop'}, ['giấy'], 0.45, 'căng nhẹ', 'ident'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
IDENT = [round(S.end['S03'] - 3.0, 3), S.end['S03']]
moves = K.moves_of([
    ('m_push', 'push', 'w0', 'w0~', 0.0, cue['a0']['stocks'], 1.6, 'mở: đẩy nhẹ vào phố chưa sáng, tường cột đang mọc', 'whoosh_air', {}),
    ('m_c1', 'mode', 'w0~', 'cWall', cue['a0']['nine'], cue['a1']['so'], 0.75, 'tỉ lệ chỉ ở đồ thị (quy tắc 1), sau 5 s thế giới (quy tắc 7)', 'whoosh_mode', {'start': 5.0}),
    ('m_nina', 'pan', 'cWall', 'cNina', cue['a1']['so'], cue['a1']['saved'], 1.4, 'từ tường cột sang người: Nina và tiền để dành', 'whoosh_soft', {}),
    ('m_st', 'pull', 'cNina', 'cStreet', cue['a1']['saved'], cue['a2']['cash'], 1.4, 'lùi lên phố: tiền của Nina đặt cạnh con phố', 'whoosh_soft', {}),
    ('m_w', 'mode', 'cStreet', 'wNina', cue['a4']['stocks'], cue['a5']['invests'], 1.4, 'câu hỏi của Nina: về thế giới, ở cửa cô', 'whoosh_mode', {}),
    ('m_wall', 'pull', 'wNina', 'wWide', cue['a5']['invests'], cue['a6']['outgrew'], 1.6, 'nghịch lý: lùi thấy cả phố và tường cột phía sau', 'whoosh_soft', {}),
    ('m_c2', 'mode', 'wWide', 'cPile', cue['a8']['lit'], cue['a9']['pile'], 1.2, 'định nghĩa đống: số chỉ ở đồ thị, cận kệ N6', 'whoosh_mode', {}),
])
ev = [{'t': cue['a0']['stocks'], 'kind': 'rise', 'dur': 2.0}, {'t': cue['a0']['nine'], 'kind': 'data', 'v': 0.7},
      {'t': cue['a1']['saved'], 'kind': 'tick', 'v': 0.4}, {'t': cue['a2']['cash'], 'kind': 'data', 'v': 0.4}, {'t': cue['a2']['ahead'], 'kind': 'rise', 'dur': 1.4},
      {'t': cue['a3']['stocks'], 'kind': 'data', 'v': 0.5}, {'t': cue['a3']['half'], 'kind': 'data', 'v': 0.3},
      {'t': cue['a4']['every'], 'kind': 'data', 'v': 0.8}, {'t': cue['a4']['stocks'], 'kind': 'data', 'v': 0.2},
      {'t': cue['a6']['half'], 'kind': 'data', 'v': 0.5}, {'t': cue['a8']['replayed'], 'kind': 'rise', 'dur': 1.6},
      {'t': cue['a9']['plus'], 'kind': 'tick', 'v': 0.4}, {'t': cue['a10']['drop'], 'kind': 'data', 'v': 0.3}]
K.finish(HERE, S, 'ep009 · A = S01–S03 + ident (cold open, chương 1)', beats, moves, ev,
         {'ident': IDENT, 'chapter': [0.3, 'Two piles, one street']},
         {'a1.so': 'stocks grew more than home prices: about 9 in 10', 'a1.saved': '$92,000 saved', 'a2.ahead': 'with cash: buyer ahead about 3 in 4',
          'a3.half': 'with stocks: about half', 'a4.every': '15 years · cash: every one', 'a4.stocks': '15 years · stocks: about 1 in 5',
          'a5.invests': 'Rent and invest the difference?', 'a9.pile': '$92,000', 'a9.plus': '+ the monthly gap', 'a10.drop': 'every month, even in drops (assumption)'},
         [f"{b['id']}.{c}" for b in beats for c in b['cues']])
