"""Tập 8 · ĐOẠN C = S08–S14 (chương 3 "The street lights up", hồi 2 phần 1). Lời + giờ = timeline nhà máy (0 ký tự EL).
B08 (S08): lưới nhìn từ trên — mỗi tháng một ô/nhà mọc trái → phải (January 1991 → July 2016, 307 nhà, mười năm mỗi nhà); về thế giới: tháng của Nina ở qua
cuối phố, chưa có nhà; một nhà sáng (vốn người mua sau phí bán lớn hơn tiền mặt người thuê), một nhà cửa tối. B09: đi dọc phố từ 1991, cả thập niên 1990
sáng dần. B10: từ April 2001 cửa tối dần tới December 2007. B11 (đồ thị): 2002–2007 chỉ 6 trên 72. B12: sáng lại 2009 → 2016; nhìn toàn phố.
B13 (số neo 1, lặng 0,75 s trước câu): chính các ô sáng/tối được đếm tại chỗ — "about 3 in 4 (75.6%)", "75 of 307"; chi phí đã tính đủ. B14: đếm lịch sử,
không phải lời hứa; dải chênh lệch theo tháng (trung vị khoảng $157,000), độ trải rộng."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W8 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W8)
import kit as K
SV = K.SV
S = K.Seg(['S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14'])
B = [
 ('c0', 'S08.1', 'world', 'Bản ghi thật nói gì về hai người song sinh?', 'phố nhìn ngang.', {'record': '@S08.1:record'}, [], 0.34, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c1', 'S08.2', 'chart', 'Mỗi tháng bắt đầu một nhà giống hệt; trái 1991, phải 2016.', 'ô mọc trái → phải.', {'each': '@S08.2:Each', 'january': '@S08.2:January', 'right': '@S08.2:right'}, ['gõ gỗ nhanh dần'], 0.36, 'ngạc nhiên', '—'),
 ('c2', 'S08.3', 'chart', '307 nhà, mỗi nhà theo dõi mười năm.', 'nhãn số nhà.', {'three': '@S08.3:three', 'ten': '@S08.3:ten'}, ['tick'], 0.38, 'ngạc nhiên', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('c3', 'S08.4', 'world', 'Tháng của Nina ở qua cuối phố, chưa có nhà.', 'Nina ở bãi trống qua cột 2016.', {'past': '@S08.4:past', 'stands': '@S08.4:stands'}, ['đèn ù'], 0.42, 'ấm', '—'),
 ('c4', 'S08.5', 'world', 'Sau mười năm, nhà sáng khi vốn người mua (sau phí bán) lớn hơn tiền mặt người thuê.', 'một nhà nhô lên và sáng.', {'lights': '@S08.5:lights', 'cash': '@S08.5:cash'}, ['tinh'], 0.4, 'rõ', '—'),
 ('c5', 'S08.6', 'world', 'Tiền mặt lớn hơn → cửa tối.', 'một nhà nhô lên, cửa tối.', {'dark': '@S08.6:dark'}, ['bịch trầm'], 0.4, 'rõ', 'lia máy'),
 ('c6', 'S09.1', 'world', 'Đi dọc phố từ 1991: người mua hơn bao nhiêu lần?', 'máy đi dọc phố.', {'walking': '@S09.1:walking'}, [], 0.48, 'tò mò', '—'),
 ('c7', 'S09.2', 'world', 'Cả thập niên 1990 sáng.', 'các nhà 1991–1999 sáng lần lượt.', {'every': '@S09.2:every'}, ['tinh mỗi nhà'], 0.52, 'ấm', '—'),
 ('c8', 'S09.3', 'world', 'Giá tăng, dư nợ giảm; năm thứ mười vốn người mua hơn tiền mặt người thuê.', 'sáng tiếp tới đầu 2001.', {'start': '@S09.3:start'}, ['tinh'], 0.5, 'ấm', '—'),
 ('c9', 'S10.1', 'world', 'Từ April 2001 cửa bắt đầu tối.', 'cửa tối lan.', {'april': '@S10.1:April', 'dark': '@S10.1:dark'}, ['bịch trầm'], 0.56, 'bất an', '—'),
 ('c10', 'S10.2', 'world', 'Mọi nhà người thuê hơn nằm giữa April 2001 và December 2007.', 'dãy tối kết thúc ở 2007.', {'every': '@S10.2:Every', 'december': '@S10.2:December'}, ['chuỗi bịch'], 0.6, 'lạnh', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('c11', 'S11.1', 'chart', '72 tháng 2002–2007: người mua chỉ hơn 6.', 'khối 2002–2007 từ trên, 6 ô sáng.', {'seventy': '@S11.1:seventy-two', 'six': '@S11.1:six'}, ['tinh ×6'], 0.62, 'lạnh', '—'),
 ('c12', 'S11.2', 'chart', 'Những tháng đó gặp đợt giá nhà toàn quốc giảm.', 'khối tối giữ.', {'fall': '@S11.2:fall'}, [], 0.6, 'lạnh', '—'),
 ('c13', 'S12.1', 'chart', 'Phố sáng lại: 2009 → giữa 2016 người mua đều hơn.', 'ô sáng lại tới 2016.', {'again': '@S12.1:again', 'every': '@S12.1:every'}, ['tinh'], 0.54, 'nhẹ', '—'),
 ('c14', 'S12.2', 'chart', 'Họ bắt đầu từ giá thấp và lãi thấp.', 'giữ.', {'lower': '@S12.2:lower'}, [], 0.54, 'nhẹ', '—'),
 ('c15', 'S12.3', 'chart', 'Đếm dọc cả phố.', 'toàn lưới.', {'counted': '@S12.3:Counted'}, [], 0.58, 'rõ', '—'),
 ('c16', 'S13.1', 'chart', 'Khoảng 3/4 trong 307 tháng, người mua hơn.', 'ô sáng đếm tại chỗ (số neo 1).', {'three': '@S13.1:three'}, ['chuông mỗi trăm'], 0.7, 'rõ', '—'),
 ('c17', 'S13.2', 'chart', '75 tháng còn lại, người thuê hơn.', 'ô tối đếm.', {'seventy': '@S13.2:seventy-five'}, ['tick'], 0.6, 'rõ', '—'),
 ('c18', 'S13.3', 'chart', 'Đếm đã gồm mọi chi phí.', 'nhãn các khoản.', {'interest': '@S13.3:interest'}, [], 0.55, 'rõ', 'lia máy'),
 ('c19', 'S14.1', 'chart', 'Tỉ lệ sáng là đếm lịch sử, không phải lời hứa cho một tháng.', 'nhãn đối trọng.', {'lit': '@S14.1:lit'}, [], 0.5, 'tỉnh', '—'),
 ('c20', 'S14.2', 'chart', 'Tháng giữa: người mua hơn khoảng $157,000.', 'dải chênh lệch theo tháng, vạch trung vị.', {'middle': '@S14.2:middle', 'one': '@S14.2:one'}, ['tick'], 0.5, 'tỉnh', '—'),
 ('c21', 'S14.3', 'chart', 'Nhưng trải rộng.', 'dải tô hai đầu.', {'spread': '@S14.3:spread'}, [], 0.5, 'tỉnh', '—'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c1', 'mode', 'wSide', 'cGrid', cue['c0']['record'], cue['c1']['each'], 1.1, 'phố = trục thời gian: nhìn từ trên để đọc năm/tháng (nhãn ngày chỉ ở đồ thị)', 'whoosh_mode', {}),
    ('m_w1', 'mode', 'cGrid', 'wEnd', cue['c2']['ten'], cue['c3']['past'], 1.4, 'tháng của Nina ở qua cuối phố: về thế giới', 'whoosh_mode', {}),
    ('m_pair', 'pan', 'wEnd', 'wPair', cue['c3']['stands'], cue['c4']['lights'], 1.6, 'luật đèn: hai nhà ví dụ giữa phố', 'whoosh_soft', {}),
    ('m_walk', 'pan', 'wPair', 'wWalk0', cue['c5']['dark'], cue['c6']['walking'], 1.0, 'đi dọc phố từ đầu (1991)', 'whoosh_soft', {}),
    K.reframe(S, beats, 'm_r1', 'push', 'wWalk0', 'wWalk0~', 'S09.1:how', 'câu hỏi "bao nhiêu lần": lại gần dãy nhà đầu phố'),
    K.reframe(S, beats, 'm_r2', 'pull', 'wWalk0~', 'wWalk0', 'S09.3:Prices', 'giá tăng, dư nợ giảm: lùi thấy dãy sáng tiếp', dur=1.6),
    ('m_walk2', 'pan', 'wWalk0', 'wWalk1', cue['c8']['start'], cue['c9']['april'], 2.0, 'đi tiếp tới 2001: máy chậm lại (do dự)', 'whoosh_soft', {}),
    ('m_c2', 'mode', 'wWalk1', 'cGrid', cue['c10']['december'], cue['c11']['seventy'], 1.0, 'đếm cần nhìn toàn cảnh + số chỉ ở đồ thị', 'whoosh_mode', {}),
    ('m_adv', 'pan', 'cGrid', 'cAdv', cue['c19']['lit'], cue['c20']['middle'], 1.6, 'từ đếm sang độ lớn: dải chênh lệch theo tháng', 'whoosh_soft', {}),
])
ANCH = ['S13.1']
ev = [{'t': cue['c1']['each'], 'kind': 'rise', 'dur': 2.0}, {'t': cue['c2']['three'], 'kind': 'tick', 'v': 0.4}, {'t': cue['c4']['lights'], 'kind': 'data', 'v': 0.7},
      {'t': cue['c5']['dark'], 'kind': 'data', 'v': 0.2}, {'t': cue['c7']['every'], 'kind': 'rise', 'dur': 1.6}, {'t': cue['c9']['april'], 'kind': 'data', 'v': 0.25},
      {'t': cue['c10']['every'], 'kind': 'data', 'v': 0.2}, {'t': cue['c11']['six'], 'kind': 'data', 'v': 0.6}, {'t': cue['c13']['again'], 'kind': 'rise', 'dur': 1.6},
      {'t': cue['c16']['three'], 'kind': 'data', 'v': 0.75, 'over': True}, {'t': cue['c17']['seventy'], 'kind': 'data', 'v': 0.25}, {'t': cue['c20']['one'], 'kind': 'tick', 'v': 0.4}]
K.finish(HERE, S, 'ep008 · C = S08–S14 (chương 3, hồi 2 phần 1)', beats, moves, ev,
         {'chapter': [0.25, 'The street lights up']},
         {'c1.january': 'January 1991', 'c1.right': 'July 2016', 'c2.three': '307 start months · ten years each', 'c11.six': '2002 to 2007: 6 of 72 (8.3%)',
          'c13.every': 'lit again: every start 2009 to mid-2016', 'c16.three': 'buyer ahead: about 3 in 4 (75.6%)', 'c17.seventy': 'renter ahead: 75 of 307',
          'c18.interest': 'counted: interest · tax · insurance · repairs · buying and selling', 'c19.lit': 'a count of history, not a promise',
          'c20.one': 'middle start month: about $157,000 ahead'},
         [k for b in beats for k in [f"{b['id']}.{c}" for c in b['cues']]], anchors=ANCH)
