"""Tập 9 · ĐOẠN D = S14–S18 (chương 4 "The pile that sank", hồi 2 phần 2). Lời + giờ = timeline nhà máy (kit.Seg). Số neo S14.3 (đỉnh) và S15.2 (lõi).
B18 (S14.1–S14.2): hàng 307 đống nhỏ (đáy thấp nhất của mỗi cửa sổ) trên kệ dài, vạch $92,000: 183 đống tụt dưới vạch. B19 (S14.3, đỉnh): kệ N6 ngang
tầm mắt, đống của tháng November 2007 tụt tới $54,310, người thuê song sinh (không mặt) vẫn đặt bó lên. B20 (S14.4–S14.5): giả định không bán. B21
(S15.1–S15.2): phố nhìn thẳng từ trên, cả phố hiện: nửa sáng. B22 (S15.3): 80 nhà đổi sáng → tối, không nhà nào tối → sáng. B23 (S16): April 2012 nhấc
lên, vẫn sáng; cọc vốn trên cả giá nhà. B24 (S17.1–S17.3): khối 2009–2016 sáng phần lớn. B24b (S17.4–S17.6): ba cột "ở 5 / 10 / 15 năm" tỉ lệ sáng
giảm dần. B25 (S18): phố 15 năm (247 nhà): tiền mặt sáng hết, cổ phiếu tắt gần hết. Giữ 1,5 s + MR2."""
import os, sys
HERE = globals().get('HERE_OVERRIDE') or os.path.dirname(os.path.abspath(__file__)); W9 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W9)
import kit as K
SV = K.SV
S = K.Seg(['S14', 'S15', 'S16', 'S17', 'S18'])
B = [
 ('d0', 'S14.1', 'chart', 'Cửa tối không có nghĩa người thuê đi đường êm.', 'hàng 307 đống nhỏ trên kệ dài.', {'easy': '@S14.1:easy'}, [], 0.55, 'nghiêm', '—'),
 ('d1', 'S14.2', 'chart', 'Hơn nửa số đống tụt dưới $92,000 ban đầu.', 'đống tụt xuống mức thấp nhất; 183 dưới vạch.', {'half': '@S14.2:many', 'dipped': '@S14.2:dipped'}, ['bịch ×n'], 0.65, 'lo', 'lia máy'),
 ('d2', 'S14.3', 'chart', 'Một đống tụt còn $54,310, và cô vẫn đầu tư.', 'kệ N6 ngang tầm mắt; đống tụt; người thuê vẫn đặt bó.', {'sank': '@S14.3:sank', 'kept': '@S14.3:kept'}, ['giấy'], 0.85, 'nể', '—'),
 ('d3', 'S14.4', 'chart', 'Phát lại giả định mọi người thuê làm vậy mỗi tháng.', 'bó rơi đều.', {'every': '@S14.4:every'}, [], 0.6, 'rõ', '—'),
 ('d4', 'S14.5', 'chart', 'Người bán lúc sập không có trên phố này.', 'nhãn giả định.', {'sells': '@S14.5:sells'}, [], 0.55, 'rõ', 'lia máy'),
 ('d5', 'S15.1', 'chart', 'Sau cả con phố, bao nhiêu nhà sáng?', 'phố nhìn thẳng từ trên, chưa sáng.', {'how': '@S15.1:how'}, [], 0.6, 'hồi hộp', '—'),
 ('d6', 'S15.2', 'chart', 'Sáng: 152 trên 307, khoảng một nửa.', 'cả phố hiện: nửa sáng, nửa tối.', {'lit': '@S15.2:Lit', 'half': '@S15.2:half'}, ['tinh ×n'], 0.85, 'vỡ lẽ', '—'),
 ('d7', 'S15.3', 'chart', '80 tháng đổi sang người thuê, không tháng nào đổi ngược.', '80 nhà loé sáng → tối.', {'eighty': '@S15.3:Every', 'not': '@S15.3:never'}, ['tắt ×n'], 0.7, 'rõ', '—'),
 ('d8', 'S15.4', 'chart', 'Nửa đó là đếm lịch sử, không phải lời hứa.', 'nhãn đối trọng.', {'count': '@S15.4:count'}, [], 0.55, 'tỉnh', 'lia máy'),
 ('d9', 'S16.1', 'chart', 'April 2012 vẫn sáng.', 'nhà April 2012 nhấc lên, sáng.', {'april': '@S16.1:brightest', 'glows': '@S16.1:glows'}, ['tinh'], 0.5, 'ấm', '—'),
 ('d10', 'S16.2', 'chart', 'Cổ phiếu: người mua vẫn hơn $237,632.', 'cọc vốn cao hơn đống.', {'ahead': '@S16.2:ahead'}, ['giấy'], 0.5, 'ấm', '—'),
 ('d11', 'S16.3', 'chart', 'Nhà tăng trên cả giá, không chỉ trên $92,000.', 'khung nhà lớn lên cả khối.', {'whole': '@S16.3:whole'}, [], 0.5, 'rõ', 'lia máy'),
 ('d12', 'S17.1', 'chart', '2009 → giữa 2016: gần 4/5 sáng.', 'khối cuối phố sáng phần lớn.', {'nine': '@S17.1:crash', 'four': '@S17.1:back'}, ['tinh'], 0.55, 'ấm', '—'),
 ('d13', 'S17.2', 'chart', 'Nửa không chia đều: cả đoạn sáng, một đoạn dài tối.', 'đoạn sáng / đoạn tối viền.', {'stretches': '@S17.2:stretches', 'dark': '@S17.2:dark'}, [], 0.5, 'rõ', '—'),
 ('d14', 'S17.3', 'chart', 'Giá thấp, lãi thấp giữ đèn sáng.', 'giữ.', {'lower': '@S17.3:lower'}, [], 0.5, 'rõ', '—'),
 ('d15', 'S17.4', 'chart', 'Ở nửa thời gian: người mua hơn hơi quá nửa.', 'cột "5 năm".', {'half': '@S17.4:half'}, ['tick'], 0.55, 'rõ', '—'),
 ('d16', 'S17.5', 'chart', 'Ở càng lâu, đống càng hay về trước.', 'cột 10, 15 năm thấp dần.', {'longer': '@S17.5:longer'}, ['tick ×2'], 0.6, 'vỡ lẽ', '—'),
 ('d17', 'S17.6', 'chart', 'Nửa phố sáng từng đoạn; giờ ở lâu hơn.', 'giữ.', {'stay': '@S17.6:stay'}, [], 0.5, 'chuyển', '—'),
 ('d18', 'S18.1', 'chart', 'Ở lâu hơn nữa, cổ phiếu tắt phần lớn.', 'phố rút còn 247 nhà.', {'longer': '@S18.1:longer'}, [], 0.6, 'lật', '—'),
 ('d19', 'S18.2', 'chart', 'Tiền mặt: cả 247 tháng 15 năm người mua hơn.', 'sáng hết.', {'cash': '@S18.2:cash', 'every': '@S18.2:every'}, ['tinh ×n'], 0.65, 'rõ', '—'),
 ('d20', 'S18.3', 'chart', 'Cổ phiếu: chỉ khoảng 1/5.', 'tắt gần hết.', {'stocks': '@S18.3:stocks', 'one': '@S18.3:one'}, ['tắt ×n'], 0.7, 'lật', '—'),
 ('d21', 'S18.4', 'chart', 'Ở lâu, đống có thời gian tích luỹ.', 'giữ.', {'compound': '@S18.4:compound'}, [], 0.55, 'rõ', '—'),
 ('d22', 'S18.5', 'chart', 'Còn một giả định: thẻ thuê.', 'giữ, nhãn chuyển.', {'tag': '@S18.5:tag'}, [], 0.5, 'chuyển', 'MR2'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
MR, MRS = K.midroll(S, 1)
t143 = S.at('@S14.3')
moves = K.moves_of([
    ('m_sh', 'pan', 'cBars', 'cShelf', cue['d1']['dipped'], t143 - 0.6, 1.3, 'từ hàng đống sang một đống: kệ N6 ngang tầm mắt', 'whoosh_soft', {}),
    ('m_g', 'pull', 'cShelf', 'cGrid', cue['d4']['sells'], cue['d5']['how'], 1.4, 'câu hỏi đếm: lùi lên nhìn thẳng cả phố', 'whoosh_soft', {}),
    ('m_12', 'pan', 'cGrid', 'c2012', cue['d8']['count'], cue['d9']['april'], 1.4, 'nhà sáng nhất lần trước: April 2012 nhấc lên', 'whoosh_soft', {}),
    ('m_g2', 'pull', 'c2012', 'cGrid', cue['d11']['whole'], cue['d12']['nine'], 1.4, 'về cả phố: khối 2009–2016', 'whoosh_soft', {}),
])
ANCH = ['S14.3', 'S15.2']
ev = [{'t': cue['d1']['dipped'], 'kind': 'data', 'v': 0.25}, {'t': cue['d2']['sank'], 'kind': 'data', 'v': 0.1, 'over': True}, {'t': cue['d2']['kept'], 'kind': 'tick', 'v': 0.45},
      {'t': cue['d6']['lit'], 'kind': 'rise', 'dur': 1.6}, {'t': cue['d6']['half'], 'kind': 'data', 'v': 0.5, 'over': True}, {'t': cue['d7']['eighty'], 'kind': 'data', 'v': 0.3},
      {'t': cue['d9']['glows'], 'kind': 'data', 'v': 0.8}, {'t': cue['d10']['ahead'], 'kind': 'data', 'v': 0.7}, {'t': cue['d12']['four'], 'kind': 'data', 'v': 0.75},
      {'t': cue['d15']['half'], 'kind': 'tick', 'v': 0.5}, {'t': cue['d16']['longer'], 'kind': 'data', 'v': 0.25}, {'t': cue['d19']['every'], 'kind': 'rise', 'dur': 1.2},
      {'t': cue['d20']['one'], 'kind': 'data', 'v': 0.2}]
K.finish(HERE, S, 'ep009 · D = S14–S18 (chương 4, hồi 2 phần 2)', beats, moves, ev,
         {'chapter': [0.3, 'The pile that sank'], 'midroll': MR},
         {'d1.dipped': '183 of 307 dipped below $92,000', 'd2.sank': 'lowest pile: $54,310', 'd3.every': 'assumption: invests every month, through every drop',
          'd4.sells': 'selling in a crash: not on this street', 'd6.lit': '152 of 307 lit', 'd6.half': 'about half', 'd7.not': '80 switched to the renter · none to the buyer',
          'd8.count': 'a count of what happened, not a promise', 'd10.ahead': 'April 2012 · with stocks: $237,632 ahead', 'd12.four': '2009 to mid-2016: nearly 4 in 5 lit',
          'd15.half': 'shorter stay (5 years) · stocks: 53.4%', 'd19.every': '247 fifteen-year starts · cash: every one', 'd20.one': 'stocks: about 1 in 5'},
         [f"{b['id']}.{c}" for b in beats for c in b['cues']], anchors=ANCH, silences=[MRS])
