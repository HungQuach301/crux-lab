"""Tập 8 · ĐOẠN E = S23–S28 (chương 5 "Two neighbors, one tag", hồi 3 phần 1). Lời + giờ = timeline nhà máy (0 ký tự EL).
B23: hai hàng xóm minh hoạ trước hai nhà nhấc lên trên cùng phố — Marcus ở nhà tối (June 2006), Priya ở nhà sáng (April 2012); cùng thẻ, cùng chi phí,
chỉ khác tháng; ngày mua, không ai thấy đèn (đèn tắt). B24: thẻ trên cửa; tiền thuê cao hơn → bó vào hộp ít hơn; máy cẩu lên phố (nhân → quả).
B25 (số neo 3, lặng 0,75 s trước câu): thẻ lật 4 % → đèn cả phố tắt dần (64.2 %); B26: 6 % → sáng gần hết (92.2 %); "the share moves with the rent you assume".
B27: dải Census 4.83 %–5.59 %/năm trên thang thẻ, phố ở hai đầu dải (73.6 %–87.3 %), tham chiếu không phải tiền thuê của Nina. B28: biến thể T-bill: hộp
ánh, phố ≈ 2/3; đa số chỉ lật khi thẻ dưới ≈ 2.4 %; đèn theo thẻ; một tháng chưa có trên phố (bãi trống qua cuối phố)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W8 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W8)
import kit as K
SV = K.SV
S = K.Seg(['S23', 'S24', 'S25', 'S26', 'S27', 'S28'])
B = [
 ('e0', 'S23.1', 'world', 'Điều gì làm nhà này sáng, nhà kia tối?', 'hai nhà nhấc lên trên phố.', {'bright': '@S23.1:bright'}, [], 0.44, 'đồng cảm', '—'),
 ('e2', 'S23.3', 'world', 'Marcus mua ở nhà tối nhất, June 2006 (G2 câu 5d: S23.2 bỏ, S23.3–S23.4 gộp).', 'Marcus trước nhà cửa tối.', {'marcus': '@S23.3:Marcus', 'darkest': '@S23.3:darkest'}, ['bước chân'], 0.5, 'căng', 'lia máy'),
 ('e3', 'S23.3', 'world', 'Priya ở nhà sáng nhất, April 2012.', 'Priya trước nhà sáng.', {'priya': '@S23.3:Priya', 'brightest': '@S23.3:brightest'}, ['bước chân'], 0.5, 'căng', 'lia máy'),
 ('e4', 'S23.5', 'world', 'Cùng thẻ, cùng chi phí, cùng phố; chỉ khác tháng.', 'nhìn cả hai.', {'month': '@S23.5:month'}, [], 0.54, 'rõ', '—'),
 ('e5', 'S23.6', 'world', 'Ngày mua, không ai thấy mình đứng ở nhà nào.', 'đèn hai nhà tắt.', {'neither': '@S23.6:neither'}, ['tắt đèn'], 0.5, 'trầm', 'lia máy'),
 ('e6', 'S24.1', 'world', 'Đến giờ mọi nhà dùng cùng thẻ 5 %.', 'thẻ trên cửa.', {'tag': '@S24.1:tag'}, ['lật thẻ'], 0.52, 'căng', '—'),
 ('e7', 'S24.2', 'world', 'Tiền thuê khởi đầu cao hơn → người thuê để dành ít hơn mỗi tháng.', 'thẻ lên, bó vào hộp ít hơn.', {'higher': '@S24.2:higher', 'less': '@S24.2:less'}, ['bịch nhỏ'], 0.55, 'căng', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('e8', 'S24.3', 'chart', 'Phố đổi thế nào khi thẻ xoay?', 'cả phố từ trên + thẻ.', {'turns': '@S24.3:turns'}, [], 0.58, 'căng', '—'),
 ('e9', 'S25.1', 'chart', '4 %: người mua hơn ở 64.2 % số tháng.', 'thẻ 4 %, đèn tắt dần (số neo 3).', {'four': '@S25.1:four', 'sixty': '@S25.1:sixty-four'}, ['chuỗi bịch'], 0.7, 'căng', '—'),
 ('e10', 'S26.1', 'chart', '6 %: 92.2 %.', 'thẻ 6 %, đèn sáng gần hết.', {'six': '@S26.1:six', 'ninety': '@S26.1:ninety-two'}, ['chuỗi tinh'], 0.76, 'rõ', '—'),
 ('e11', 'S26.2', 'chart', 'Tỉ lệ đi theo tiền thuê giả định.', 'thẻ lắc qua lại, đèn theo.', {'share': '@S26.2:share'}, [], 0.62, 'rõ', '—'),
 ('e12', 'S27.1', 'chart', 'Số công khai của Census nằm trong dải đã xoay; tham chiếu, không phải tiền thuê của Nina.', 'dải Census trên thang thẻ.', {'census': '@S27.1:Census', 'range': '@S27.1:range', 'reference': '@S27.1:reference'}, ['thẻ trượt'], 0.52, 'vững', '—'),
 ('e13', 'S28.1', 'chart', 'Tiền mặt có lãi T-bill → ≈ 2/3.', 'phố theo biến thể T-bill.', {'treasury': '@S28.1:Treasury', 'two': '@S28.1:two'}, ['ánh hộp'], 0.5, 'đo', '—'),
 ('e14', 'S28.2', 'chart', 'Đèn theo thẻ; một tháng chưa có trên phố.', 'bãi trống qua cuối phố loé.', {'lights': '@S28.2:lights', 'month': '@S28.2:month'}, [], 0.48, 'trầm', '—'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_p1', 'pan', 'wPair', 'wMarcus', cue['e0']['bright'], cue['e2']['marcus'], 1.4, 'tới Marcus ở nhà June 2006', 'whoosh_soft', {}),
    ('m_p2', 'pan', 'wMarcus', 'wPriya', cue['e2']['darkest'], cue['e3']['priya'], 1.4, 'lia ngang sang Priya: cùng phố, khác tháng', 'whoosh_soft', {}),
    ('m_p3', 'pull', 'wPriya', 'wPair', cue['e3']['brightest'], cue['e4']['month'], 1.6, 'lùi lại nhìn cả hai: chỉ khác tháng', 'whoosh_soft', {}),
    ('m_tag', 'push', 'wPair', 'wTag', cue['e5']['neither'], cue['e6']['tag'], 2.0, 'về thẻ trên cửa của Nina', 'whoosh_push', {}),
    ('m_c', 'mode', 'wTag', 'cGrid', cue['e7']['less'], cue['e8']['turns'], 2.0, 'đẩy vào thẻ rồi cẩu lên phố trong một cú máy (nhân → quả); số chỉ ở đồ thị', 'whoosh_mode', {}),
])
ev = [{'t': cue['e2']['marcus'], 'kind': 'tick', 'v': 0.3}, {'t': cue['e5']['neither'], 'kind': 'data', 'v': 0.2}, {'t': cue['e6']['tag'], 'kind': 'tick', 'v': 0.45},
      {'t': cue['e7']['higher'], 'kind': 'tick', 'v': 0.55}, {'t': cue['e9']['four'], 'kind': 'data', 'v': 0.3}, {'t': cue['e9']['sixty'], 'kind': 'data', 'v': 0.64},
      {'t': cue['e10']['six'], 'kind': 'data', 'v': 0.7}, {'t': cue['e10']['ninety'], 'kind': 'data', 'v': 0.92}, {'t': cue['e12']['census'], 'kind': 'tick', 'v': 0.4},
      {'t': cue['e13']['treasury'], 'kind': 'data', 'v': 0.5}, {'t': cue['e14']['month'], 'kind': 'tick', 'v': 0.3}]
K.finish(HERE, S, 'ep008 · E = S23–S28 (chương 5, hồi 3 phần 1)', beats, moves, ev,
         {'chapter': [0.2, 'Two neighbors, one tag'], 'at': {'flip': S.at('@S28.1:falls')}},
         {'e9.sixty': 'rent tag 4%: buyer ahead in 64.2% of start months', 'e10.ninety': 'rent tag 6%: buyer ahead in 92.2%', 'e11.share': 'the share moves with the rent you assume',
          'e12.census': 'Census vacancy survey: 4.83% a year · 5.59% a year', 'e12.range': 'buyer ahead: 73.6% · 87.3%', 'e12.reference': "a reference, not Nina's own rent",
          'e13.two': 'Treasury bill interest: about 2 out of 3 (66.4%)', 'e14.month': 'one month not on the street yet'},
         [k for b in beats for k in [f"{b['id']}.{c}" for c in b['cues']]], anchors=['S25.1'])
