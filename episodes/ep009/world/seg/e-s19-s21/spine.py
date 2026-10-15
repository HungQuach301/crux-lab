"""Tập 9 · ĐOẠN E = S19–S21 (chương 5 "Why the house holds half", hồi 3 phần 1). Lời + giờ = timeline nhà máy (kit.Seg).
B26 (S19): khối nhà $400,000 (LIT) cạnh đống $92,000 (STK); cả hai lớn lên — đống tăng nhanh hơn theo tỉ lệ, nhà tăng trên nền lớn; bó mỗi tháng rơi vào
đống (đuổi kịp bằng chênh lệch + thời gian). B27 (S20): bó mỗi tháng dừng; phố nhìn thẳng từ trên sáng lại (chỉ $92,000 đầu tư: khoảng 2/3). B28 (S21):
phí 1 %/năm: phố sáng thêm (55,0 %)."""
import os, sys
HERE = globals().get('HERE_OVERRIDE') or os.path.dirname(os.path.abspath(__file__)); W9 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W9)
import kit as K
SV = K.SV
S = K.Seg(['S19', 'S20', 'S21'])
B = [
 ('e0', 'S19.1', 'chart', 'Nghịch lý: cổ phiếu tăng hơn 9/10 mà người mua vẫn hơn ở nửa.', 'khối nhà và đống đứng cạnh nhau.', {'stocks': '@S19.1:stocks', 'half': '@S19.1:half'}, [], 0.5, 'tò mò', '—'),
 ('e1', 'S19.2', 'chart', 'Nhà tăng trên cả $400,000; đống bắt đầu từ $92,000.', 'khối nhà lớn; đống nhỏ.', {'four': '@S19.2:four', 'ninety': '@S19.2:ninety'}, ['giấy'], 0.55, 'vỡ lẽ', '—'),
 ('e2', 'S19.3', 'chart', 'Vay cho cái tăng chậm hơn một nền lớn hơn nhiều.', 'cả hai lớn: nhà thêm nhiều $ hơn.', {'slower': '@S19.3:slower', 'base': '@S19.3:base'}, ['rise'], 0.6, 'vỡ lẽ', '—'),
 ('e3', 'S19.4', 'chart', 'Người thuê đuổi kịp nhờ chênh lệch tháng và thời gian.', 'bó mỗi tháng rơi vào đống.', {'monthly': '@S19.4:monthly', 'time': '@S19.4:time'}, ['giấy'], 0.55, 'rõ', '—'),
 ('e4', 'S20.1', 'chart', 'Nếu không ai để dành chênh lệch?', 'bó ngừng rơi.', {'nobody': '@S20.1:nobody'}, [], 0.5, 'tò mò', 'lia máy'),
 ('e5', 'S20.2', 'chart', 'Người mua hơn khoảng 2/3.', 'phố sáng lại.', {'two': '@S20.2:two'}, ['tinh ×n'], 0.6, 'rõ', '—'),
 ('e6', 'S20.3', 'chart', 'Thói quen hằng tháng làm phần lớn việc đuổi kịp.', 'giữ.', {'habit': '@S20.3:habit'}, [], 0.5, 'rõ', '—'),
 ('e7', 'S21.1', 'chart', 'Đống không trả phí, không thuế.', 'về bản cổ phiếu.', {'fees': '@S21.1:fees'}, [], 0.5, 'rõ', '—'),
 ('e8', 'S21.2', 'chart', 'Trừ 1%/năm: sáng lên 55%.', 'phố sáng thêm.', {'one': '@S21.2:one', 'fifty': '@S21.2:fifty'}, ['tinh'], 0.55, 'rõ', '—'),
 ('e9', 'S21.3', 'chart', 'Mọi chi phí thật bên người thuê đẩy nhà về phía người mua.', 'giữ.', {'back': '@S21.3:back'}, [], 0.5, 'rõ', '—'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    K.reframe(S, beats, 'm_r1', 'push', 'cBase', 'cBase~', 'S19.3:The', 'nền lớn: lại gần khối nhà'),
    ('m_g', 'pull', 'cBase~', 'cGrid', cue['e4']['nobody'], cue['e5']['two'], 1.4, 'hệ quả trên cả phố: nhìn thẳng từ trên', 'whoosh_soft', {}),
])
ev = [{'t': cue['e1']['four'], 'kind': 'data', 'v': 0.7}, {'t': cue['e1']['ninety'], 'kind': 'data', 'v': 0.35}, {'t': cue['e2']['base'], 'kind': 'rise', 'dur': 1.6},
      {'t': cue['e3']['monthly'], 'kind': 'tick', 'v': 0.4}, {'t': cue['e5']['two'], 'kind': 'rise', 'dur': 1.4}, {'t': cue['e8']['fifty'], 'kind': 'data', 'v': 0.55}]
K.finish(HERE, S, 'ep009 · E = S19–S21 (chương 5, hồi 3 phần 1)', beats, moves, ev,
         {'chapter': [0.3, 'Why the house holds half']},
         {'e0.stocks': 'stocks grew more: 88.9% of start months', 'e1.four': 'house: $400,000 base', 'e1.ninety': 'pile: $92,000 start',
          'e5.two': 'only the $92,000 invested: about 2 in 3', 'e8.fifty': '1% a year in fees: 55.0% lit'},
         [f"{b['id']}.{c}" for b in beats for c in b['cues']])
