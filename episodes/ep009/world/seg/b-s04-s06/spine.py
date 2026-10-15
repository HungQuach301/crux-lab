"""Tập 9 · ĐOẠN B = S04–S06 (chương 2 "The first house", hồi 1). Lời + giờ = timeline nhà máy (kit.Seg).
B07 (S04.1–S04.3, số neo S04.3, lặng 0,75 s): nhà January 1991 cận thấp → đồ thị chính diện: cọc vốn người mua (LIT) cao hơn hộp tiền mặt người thuê
→ đống cổ phiếu N6 vượt lên khỏi cả hai, cửa nhà tối. S04.4: chỉ đống đổi. B08 (S05.1): đường $1 → gần 5 lần (1991). S05.2–S05.3: đống = $92,000 + bó
mỗi tháng, chợ làm lớn cả bó. S05.4: về nhà đầu phố, cửa sáng → tối. B09 (S06.1): đường thẳng một mức tăng cố định cạnh bản ghi thật răng cưa, cùng đầu
cùng cuối. B10 (giữ 1,5 s + MR1): thẻ V7 "Same costs as before"."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W9 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W9)
import kit as K
SV = K.SV
S = K.Seg(['S04', 'S05', 'S06'])
B = [
 ('b0', 'S04.1', 'world', 'Nhà đầu tiên: January 1991.', 'cận thấp nhà đầu phố.', {'first': '@S04.1:first', 'january': '@S04.1:January'}, ['tinh'], 0.4, 'tò mò', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b1', 'S04.2', 'chart', 'Tiền mặt: người mua hơn $48,410.', 'cọc vốn người mua cao hơn hộp tiền mặt.', {'cash': '@S04.2:cash', 'ahead': '@S04.2:ahead'}, ['giấy'], 0.45, 'rõ', '—'),
 ('b2', 'S04.3', 'chart', 'Cổ phiếu: cùng người mua kém $485,063.', 'đống cổ phiếu vượt khỏi khung; cửa tối.', {'stocks': '@S04.3:stocks', 'behind': '@S04.3:behind'}, ['giấy dồn'], 0.75, 'bất ngờ', '—'),
 ('b3', 'S04.4', 'chart', 'Chỉ đống của người thuê đổi.', 'nhà, cọc, hộp đứng yên; đống sáng viền.', {'only': '@S04.4:only'}, [], 0.5, 'rõ', 'lia máy'),
 ('b4', 'S05.1', 'chart', '$1 trong cổ phiếu từ 1991 thành gần 5 lần.', 'đường $1 mọc tháng một.', {'dollar': '@S05.1:dollar', 'five': '@S05.1:five'}, ['rise'], 0.5, 'ngạc nhiên', 'lia máy'),
 ('b5', 'S05.2', 'chart', 'Đống = $92,000 ngày đầu + bó mỗi tháng.', 'khối đầu + bó rơi mỗi tháng.', {'day': '@S05.2:day', 'deposit': '@S05.2:deposit'}, ['giấy'], 0.45, 'rõ', '—'),
 ('b6', 'S05.3', 'chart', 'Chênh lệch tháng vào đống, chợ làm lớn cả phần đó.', 'đống mọc nhanh dần.', {'gap': '@S05.3:gap', 'grew': '@S05.3:grew'}, ['giấy'], 0.5, 'rõ', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('b7', 'S05.4', 'world', 'Một thay đổi: nhà đầu tiên từ sáng sang tối.', 'nhà đầu phố: sáng → tối.', {'lit': '@S05.4:lit', 'dark': '@S05.4:dark'}, ['bịch'], 0.5, 'vỡ lẽ', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b8', 'S06.1', 'chart', 'Một mức tăng cố định giấu thứ tự năm tốt/xấu; phát lại dùng tháng thật.', 'đường thẳng cạnh đường răng cưa, cùng đầu cùng cuối.',
  {'one': '@S06.1:one', 'actually': '@S06.1:actually'}, ['tick'], 0.45, 'rõ', 'MR1'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
MR, MRS = K.midroll(S, 0)
moves = K.moves_of([
    ('m_c1', 'mode', 'wHouse', 'cHouse', cue['b0']['january'], cue['b1']['cash'], 1.3, 'số chỉ ở đồ thị: nhà + cọc + hộp chính diện', 'whoosh_mode', {}),
    ('m_g', 'pan', 'cHouse', 'cLines', cue['b3']['only'], cue['b4']['dollar'], 1.4, 'vì sao: đường $1 trong cổ phiếu', 'whoosh_soft', {}),
    ('m_p', 'pan', 'cLines', 'cHouse', cue['b4']['five'], cue['b5']['day'], 1.4, 'đống của người thuê: khối đầu + bó mỗi tháng', 'whoosh_soft', {}),
    ('m_w', 'mode', 'cHouse', 'wHouse', cue['b6']['grew'], cue['b7']['lit'], 1.3, 'kết hồi: về nhà đầu phố (thế giới)', 'whoosh_mode', {}),
    ('m_c2', 'mode', 'wHouse', 'cLines', cue['b7']['dark'], cue['b8']['one'], 1.3, 'đối thủ: một mức tăng cố định vs bản ghi thật (đồ thị)', 'whoosh_mode', {}),
])
ANCH = ['S04.3']
ev = [{'t': cue['b0']['january'], 'kind': 'tick', 'v': 0.4}, {'t': cue['b1']['cash'], 'kind': 'data', 'v': 0.45}, {'t': cue['b1']['ahead'], 'kind': 'data', 'v': 0.55},
      {'t': cue['b2']['stocks'], 'kind': 'rise', 'dur': 1.4}, {'t': cue['b2']['behind'], 'kind': 'data', 'v': 0.2, 'over': True},
      {'t': cue['b4']['dollar'], 'kind': 'rise', 'dur': 2.0}, {'t': cue['b4']['five'], 'kind': 'data', 'v': 0.8},
      {'t': cue['b5']['deposit'], 'kind': 'tick', 'v': 0.35}, {'t': cue['b6']['grew'], 'kind': 'rise', 'dur': 1.2},
      {'t': cue['b7']['dark'], 'kind': 'data', 'v': 0.2}, {'t': cue['b8']['actually'], 'kind': 'data', 'v': 0.5}]
K.finish(HERE, S, 'ep009 · B = S04–S06 (chương 2, hồi 1)', beats, moves, ev,
         {'chapter': [0.3, 'The first house'], 'midroll': MR, 'card': [cue['b8']['actually'] + 1.2, S.total]},
         {'b0.january': 'January 1991', 'b1.ahead': 'with cash: $48,410 ahead', 'b2.behind': 'with stocks: $485,063 behind',
          'b4.five': '$1 in 1991 → almost 5 times', 'b5.day': '$92,000 on day one', 'b5.deposit': '+ a deposit every month',
          'b8.one': 'one fixed growth rate', 'b8.actually': 'the real record, month by month'},
         [f"{b['id']}.{c}" for b in beats for c in b['cues']], anchors=ANCH, silences=[MRS])
