"""Tập 9 · ĐOẠN F = S22–S25 (chương 6 "The tag on her door", hồi 3 phần 2 + giới hạn + kết). Lời + giờ = timeline nhà máy (kit.Seg).
B29 (S22.1–S22.2): cận thẻ thuê trên cửa Nina, phố phía sau; mỗi lần thẻ lật (4% → 6% → 5%) đèn quét dọc phố; ở 5%: nửa. B30 (S22.3–S22.4): điểm lật
≈ 5,1 %; thẻ lật sang hai mốc Census 4,83 % và 5,59 % — đèn quét hai phía. B31 (S23): đèn của Nina trong cửa sổ; những thứ phố không đếm. B32 (S24):
thẻ giới hạn V7 (+ câu nguồn cổ phiếu của chủ dự án 15/10). B33 (S25.1–S25.2): bảng điểm 4 dòng theo màu lựa chọn. B34 (S25.3): đúng khung 0:00,
nay nửa sáng. B35 (S25.4): lô trống của Nina qua cuối phố. B36 (S25.5): Nina cạnh cửa, thẻ đung đưa — câu trả lời của cô."""
import os, sys
HERE = globals().get('HERE_OVERRIDE') or os.path.dirname(os.path.abspath(__file__)); W9 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W9)
import kit as K
SV = K.SV
S = K.Seg(['S22', 'S23', 'S24', 'S25'])
B = [
 ('f0', 'S22.1', 'chart', 'Thẻ thuê trên cửa Nina.', 'cận thẻ, phố phía sau; thẻ lật 4% → 6%, đèn quét.', {'tag': '@S22.1:tag'}, ['xu'], 0.55, 'tò mò', '—'),
 ('f1', 'S22.2', 'chart', 'Ở 5%: phố chia gần đúng nửa.', 'thẻ về 5%; nửa sáng.', {'five': '@S22.2:five', 'half': '@S22.2:half'}, ['xu', 'tinh'], 0.6, 'rõ', '—'),
 ('f2', 'S22.3', 'chart', 'Điểm lật ≈ 5,1%; dữ liệu Census nằm hai phía.', 'thẻ 5.1%; lật 4.83% / 5.59%, đèn quét hai phía.', {'five': '@S22.3:five', 'census': '@S22.3:Census', 'both': '@S22.3:both'}, ['xu ×2'], 0.7, 'vỡ lẽ', '—'),
 ('f3', 'S22.4', 'chart', 'Đáp án nằm trên thẻ, và thẻ là giả định.', 'thẻ đung đưa; dấu "assumption".', {'tag': '@S22.4:tag', 'assumption': '@S22.4:assumption'}, [], 0.6, 'rõ', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('f4', 'S23.1', 'world', 'Không xếp hạng cổ phiếu hay nhà.', 'cửa Nina, đèn trong cửa sổ.', {'none': '@S23.1:None'}, [], 0.45, 'lắng', '—'),
 ('f5', 'S23.2', 'world', 'Ổn định, quyền tự quyết không đếm được.', 'đèn của Nina; nhãn những thứ không đo.', {'stability': '@S23.2:stability'}, [], 0.4, 'ấm', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('f6', 'S24.1', 'chart', 'Giới hạn trên thẻ.', 'thẻ giới hạn V7.', {'card': '@S24.1:card', 'taxes': '@S24.1:taxes', 'renters': '@S24.1:renters'}, [], 0.35, 'bình thản', '—'),
 ('f7', 'S25.1', 'chart', 'Về câu hỏi của Nina.', 'bảng điểm hiện.', {'back': '@S25.1:back'}, [], 0.45, 'lắng', '—'),
 ('f8', 'S25.2', 'chart', 'Tiền mặt: phần lớn sáng; cổ phiếu: nửa; 15 năm: phần lớn tối.', 'các dòng bảng điểm theo màu.', {'cash': '@S25.2:cash', 'stocks': '@S25.2:stocks', 'fifteen': '@S25.2:fifteen'}, ['tick ×3'], 0.55, 'rõ', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('f9', 'S25.3', 'world', 'Cùng con phố lúc mở đầu, đọc lại với đống trong thị trường.', 'khung 0:00, nay nửa sáng.', {'same': '@S25.3:same'}, [], 0.45, 'vòng lại', 'lia máy'),
 ('f10', 'S25.4', 'world', 'Phố không cho biết Nina sẽ ở bao lâu.', 'lô trống của Nina qua cuối phố, đèn.', {'how': '@S25.4:how'}, [], 0.4, 'mở', 'lia máy'),
 ('f11', 'S25.5', 'world', 'Câu trả lời của Nina: một lần tung đồng xu, thẻ thuê nghiêng nó.', 'Nina cạnh cửa, thẻ đung đưa.', {'answer': '@S25.5:answer', 'coin': '@S25.5:coin'}, [], 0.4, 'trầm', 'kết'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_w', 'mode', 'cTag', 'wDoor', cue['f3']['assumption'], cue['f4']['none'], 0.8, 'giới hạn của số: về cửa Nina (thế giới)', 'whoosh_mode', {}),
    ('m_c', 'mode', 'wDoor', 'cGrid', cue['f5']['stability'], cue['f6']['card'], 1.3, 'thẻ giới hạn + bảng điểm (đồ thị)', 'whoosh_mode', {}),
    ('m_w2', 'mode', 'cGrid', 'w0', cue['f8']['fifteen'], cue['f9']['same'], 1.4, 'quay lại khung 0:00 (thế giới)', 'whoosh_mode', {}),
    ('m_lot', 'pan', 'w0', 'wLot', cue['f9']['same'], cue['f10']['how'], 1.6, 'chuyền: lô trống của Nina qua cuối phố', 'whoosh_soft', {}),
    ('m_door', 'pan', 'wLot', 'wDoor', cue['f10']['how'], cue['f11']['answer'], 1.4, 'câu cuối là của Nina: ở cửa cô', 'whoosh_soft', {}),
])
ev = [{'t': cue['f0']['tag'], 'kind': 'tick', 'v': 0.4}, {'t': cue['f1']['half'], 'kind': 'data', 'v': 0.5}, {'t': cue['f2']['five'], 'kind': 'tick', 'v': 0.5},
      {'t': cue['f2']['census'], 'kind': 'data', 'v': 0.45}, {'t': cue['f2']['both'], 'kind': 'data', 'v': 0.6},
      {'t': cue['f8']['cash'], 'kind': 'tick', 'v': 0.4}, {'t': cue['f8']['stocks'], 'kind': 'tick', 'v': 0.45}, {'t': cue['f8']['fifteen'], 'kind': 'tick', 'v': 0.3}]
K.finish(HERE, S, 'ep009 · F = S22–S25 (chương 6 + giới hạn + kết)', beats, moves, ev,
         {'chapter': [0.3, 'The tag on her door']},
         {'f1.five': '5%: about half lit', 'f2.five': 'flip point: about 5.1%', 'f2.both': 'Census range: 4.83% to 5.59% a year · 47.2% to 58.3% lit',
          'f3.assumption': 'the tag is an assumption', 'f5.stability': 'not measured: stability, control, family', 'f6.card': 'Limits',
          'f8.cash': 'cash: buyer ahead about 3 in 4 · 15 years: every one', 'f8.stocks': 'stocks: about half (152 of 307) · 15 years: about 1 in 5'},
         [f"{b['id']}.{c}" for b in beats for c in b['cues']])
