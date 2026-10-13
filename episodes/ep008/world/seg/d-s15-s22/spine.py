"""Tập 8 · ĐOẠN D = S15–S22 (chương 4 "The darkest house", hồi 2 phần 2) → MR2 trong đuôi S22. Lời + giờ = timeline nhà máy (0 ký tự EL).
B15–B16: nhà sáng nhất April 2012 nhô lên, chồng chênh lệch cao; lãi 3.91 %, giá nhà hơn gấp đôi; "một tháng ở đỉnh, không điển hình".
B16.3 → B17 (số neo 2 + đỉnh, lặng 0,75 s trước câu): lia ngược xuống June 2006 và dừng — nhà cửa tối; "$82,385 behind".
B18: hai chồng cạnh nhà: vốn người mua $115,374 (lit) thấp hơn tiền mặt người thuê $197,760 (warn, "cash, not stocks").
B19 (đồ thị): giá nhà toàn quốc gần như đứng yên 10 năm (+3.2 %), lãi khởi đầu 6.68 %; "chỉ số toàn quốc, không phải một căn".
B20–B22 (lưới từ trên): 5 năm (74.4 %), tệ nhất May 2006; 15 năm mọi tháng đều sáng (247), yếu nhất $79,829; 5 → 10 → 15 cửa tối thưa rồi hết;
về Nina qua cuối phố: phố không nói cô ở bao lâu; thẻ trên cửa chưa xoay → lặng 1,5 s MR2."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W8 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W8)
import kit as K
SV = K.SV
S = K.Seg(['S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22'])
B = [
 ('d0', 'S15.1', 'chart', 'Nhà sáng nhất April 2012: mười năm sau người mua hơn khoảng $484,000.', 'nhà April 2012 nhô lên, chồng cao.', {'april': '@S15.1:April', 'about': '@S15.1:about'}, ['ù cửa sổ'], 0.62, 'nâng', '—'),
 ('d1', 'S16.1', 'chart', 'Lãi 3.91 %, giá nhà toàn quốc hơn gấp đôi.', 'nhãn lãi + giá.', {'three': '@S16.1:three', 'doubled': '@S16.1:doubled'}, ['tick'], 0.52, 'nâng', '—'),
 ('d2', 'S16.2', 'chart', 'Một tháng ở đỉnh, không điển hình.', 'nhãn đối trọng.', {'top': '@S16.2:top'}, [], 0.5, 'thận trọng', 'lia máy'),
 ('d3', 'S16.3', 'chart', 'Nhà tối nhất: June 2006.', 'máy dừng ở nhà June 2006.', {'darkest': '@S16.3:darkest', 'june': '@S16.3:June'}, ['bịch cửa'], 0.62, 'lạnh', '—'),
 ('d4', 'S17.1', 'chart', 'Mười năm sau, người mua June 2006 kém $82,385.', 'nhà cửa tối + nhãn (số neo 2).', {'eighty': '@S17.1:eighty-two'}, [], 0.82, 'rơi lạnh', '—'),
 ('d5', 'S18.1', 'chart', 'Hai chồng: vốn người mua $115,374, tiền mặt người thuê $197,760.', 'chồng người thuê cao hơn.', {'equity': '@S18.1:equity', 'cash': '@S18.1:cash'}, ['bịch giấy ×2'], 0.7, 'lạnh', 'lia máy'),
 ('d6', 'S19.1', 'chart', 'Giá toàn quốc chỉ +3.2 % trong mười năm; người mua trả lãi, thuế, bảo hiểm, sửa chữa suốt.', 'dải chỉ số gần như phẳng.', {'three': '@S19.1:three', 'interest': '@S19.1:interest'}, ['bút'], 0.58, 'tỉnh', '—'),
 ('d7', 'S19.2', 'chart', 'Lãi khởi đầu 6.68 %.', 'nhãn lãi.', {'six': '@S19.2:six'}, ['tick'], 0.56, 'tỉnh', '—'),
 ('d8', 'S19.3', 'chart', 'Chỉ số toàn quốc, không phải một căn.', 'nhãn đối trọng.', {'national': '@S19.3:national'}, [], 0.46, 'tỉnh', 'lia máy'),
 ('d9', 'S20.1', 'chart', 'Thời gian ở có đổi bức tranh?', 'lưới từ trên.', {'stay': '@S20.1:stay'}, [], 0.44, 'tò mò', '—'),
 ('d10', 'S20.2', 'chart', '5 năm: 74.4 %.', 'lưới 5 năm, nhiều cửa tối hơn.', {'five': '@S20.2:five', 'seventy': '@S20.2:seventy-four'}, ['chuỗi tách'], 0.46, 'tò mò', '—'),
 ('d11', 'S21.1', 'chart', 'Tệ nhất 5 năm: May 2006, kém $149,392.', 'ô May 2006.', {'may': '@S21.1:May'}, ['bịch'], 0.54, 'tỉnh', '—'),
 ('d12', 'S21.2', 'chart', '5 năm ít thời gian bù chi phí mua + bán.', 'giữ.', {'little': '@S21.2:little'}, [], 0.5, 'tỉnh', '—'),
 ('d13', 'S22.1', 'chart', '15 năm: mọi tháng lịch sử cho phép đều người mua hơn.', 'lưới 15 năm sáng hết.', {'every': '@S22.1:every'}, ['chuỗi tinh'], 0.5, 'yên', '—'),
 ('d14', 'S22.2', 'chart', 'Yếu nhất vẫn hơn $79,829.', 'nhãn.', {'weakest': '@S22.2:weakest'}, ['tick'], 0.5, 'yên', '—'),
 ('d15', 'S22.3', 'chart', '5 → 10 → 15: cửa tối thưa rồi hết.', 'lưới đổi 5 → 10 → 15.', {'five': '@S22.3:five', 'ten': '@S22.3:ten', 'gone': '@S22.3:gone'}, ['tách ×3'], 0.56, 'yên', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('d16', 'S22.4', 'world', '15 năm là lâu; phố không nói Nina ở bao lâu.', 'Nina qua cuối phố.', {'nina': '@S22.4:Nina'}, ['đèn ù'], 0.46, 'yên', '—'),
 ('d17', 'S22.5', 'world', 'Tháng và thời gian ở đổi đèn; thẻ chưa xoay.', 'thẻ trên cửa, đứng yên.', {'tag': '@S22.5:tag'}, [], 0.42, 'yên', 'MR2'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
MR, MRSIL = K.midroll(S, 1)
moves = K.moves_of([
    ('m_dark', 'pan', 'cBright', 'cDark', cue['d2']['top'], cue['d3']['darkest'], 2.2, 'lia ngược xuống June 2006 và dừng hẳn (bước ngoặt của hồi)', 'whoosh_soft', {}),
    ('m_idx', 'pan', 'cDark', 'cIdx', cue['d5']['cash'] + 2.6, cue['d6']['three'], 1.0, 'vì sao tối: chỉ số giá cả nước trong mười năm đó', 'whoosh_soft', {'start': cue['d5']['cash'] + 2.6}),
    ('m_grid', 'pull', 'cIdx', 'cGrid', cue['d8']['national'], cue['d9']['stay'], 1.2, 'thời gian ở: cả lưới, đổi 5 / 10 / 15 năm', 'whoosh_soft', {'late': True}),
    ('m_w', 'mode', 'cGrid', 'wNina', cue['d15']['gone'], cue['d16']['nina'], 1.6, 'phố không nói Nina ở bao lâu: về Nina qua cuối phố', 'whoosh_mode', {}),
])
ev = [{'t': cue['d0']['about'], 'kind': 'data', 'v': 0.9}, {'t': cue['d3']['june'], 'kind': 'data', 'v': 0.15},
      {'t': cue['d5']['equity'], 'kind': 'data', 'v': 0.35}, {'t': cue['d5']['cash'], 'kind': 'data', 'v': 0.6}, {'t': cue['d6']['three'], 'kind': 'tick', 'v': 0.3},
      {'t': cue['d7']['six'], 'kind': 'tick', 'v': 0.67}, {'t': cue['d10']['five'], 'kind': 'data', 'v': 0.5}, {'t': cue['d11']['may'], 'kind': 'data', 'v': 0.1},
      {'t': cue['d13']['every'], 'kind': 'rise', 'dur': 1.4}, {'t': cue['d14']['weakest'], 'kind': 'tick', 'v': 0.4},
      {'t': cue['d15']['five'], 'kind': 'data', 'v': 0.5}, {'t': cue['d15']['ten'], 'kind': 'data', 'v': 0.6}, {'t': cue['d15']['gone'], 'kind': 'data', 'v': 0.8}]
K.finish(HERE, S, 'ep008 · D = S15–S22 (chương 4, hồi 2 phần 2) → MR2', beats, moves, ev,
         {'chapter': [cue['d4']['eighty'] - 3.2, 'The darkest house'], 'midroll': MR, 'at': {'cash2': S.at('@S18.1:cash') + 1.1, 'equity2': S.at('@S18.1:equity') + 0.8,
          'fifteen': S.at('@S22.3:fifteen')}},
         {'d0.april': 'April 2012', 'd0.about': 'about $484,000 ahead', 'd1.three': '3.91% rate', 'd1.doubled': 'prices more than doubled',
          'd3.june': 'June 2006', 'd4.eighty': '$82,385 behind', 'd5.equity': "buyer's equity $115,374", 'd5.cash': "renter's cash $197,760",
          'd6.three': 'prices up 3.2% in ten years', 'd7.six': '6.68% rate', 'd8.national': 'national index, not one house', 'd10.seventy': 'held five years: buyer ahead in 74.4%',
          'd11.may': 'May 2006 · $149,392 behind', 'd13.every': '15 years: every one (100%) · 247 start months', 'd14.weakest': 'weakest: $79,829 ahead'},
         [k for b in beats for k in [f"{b['id']}.{c}" for c in b['cues']]], anchors=['S17.1'], silences=[MRSIL])
