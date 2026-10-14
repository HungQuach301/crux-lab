"""Tập 8 · ĐOẠN F = S29–S33 (chương 6 "The end of the street", hồi 3 phần 2 + giới hạn + kết). Lời + giờ = timeline nhà máy (0 ký tự EL).
B29: Nina ở bãi trống qua cuối phố; lịch sử chỉ đặt được THÁNG ĐẦU của cô cạnh các tháng khác: hai chồng (tháng đầu người mua $2,933 lit, tiền thuê $1,667
warn) — đồ thị. B30: chấm tiền thuê ÷ chi người mua tháng đầu của 307 tháng + chấm của Nina thấp hơn mọi chấm; thấp nhất 57.9 % July 2006; chỉ tháng đầu,
không dự báo. B31: thẻ V7 giới hạn. B32: bảng điểm 4 dòng trên phố nhìn từ trên (mỗi lựa chọn đúng màu cả tập); về khung 0:00 — cùng phố, nay sáng/tối
bằng lịch sử; câu của Nina. B33: hộp tiền mặt + hộp thứ hai đóng ("invested? not measured here") — câu hỏi còn mở; tắt dần."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W8 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W8)
import kit as K
SV = K.SV
S = K.Seg(['S29', 'S30', 'S31', 'S32', 'S33'])
B = [
 ('f0', 'S29.1', 'world', 'Còn tháng của Nina, qua cuối phố?', 'Nina ở bãi trống qua cột 2016.', {'past': '@S29.1:past'}, ['bước chân'], 0.48, 'lặng', '—'),
 ('f1', 'S29.2', 'world', 'Lịch sử không kết thúc được tháng đó, chỉ đặt tháng đầu cạnh các tháng khác.', 'hai chồng tháng đầu hiện cạnh Nina.', {'first': '@S29.2:first'}, ['bịch giấy'], 0.48, 'lặng', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('f2', 'S29.3', 'chart', 'Lãi 6.86 % (trung bình 9/2026): tháng đầu người mua $2,933.', 'nhãn lãi + chồng người mua.', {'six': '@S29.3:six', 'two': '@S29.3:two'}, ['tick'], 0.52, 'lặng', '—'),
 ('f3', 'S30.1', 'chart', 'Tiền thuê giả định $1,667 = 56.8 % của số đó.', 'chồng tiền thuê + nhãn tỉ lệ.', {'rent': '@S30.1:rent', 'fifty': '@S30.1:fifty-six'}, ['tick'], 0.56, 'thận trọng', 'lia máy'),
 ('f4', 'S30.2', 'chart', 'Thấp hơn mọi tháng trên phố; thấp nhất 57.9 % July 2006.', 'chấm của Nina dưới mọi chấm.', {'lowest': '@S30.2:lowest'}, ['tick'], 0.56, 'thận trọng', '—'),
 ('f5', 'S30.3', 'chart', 'Chỉ so tháng đầu; không nói 2026 kết thúc ra sao, không biến 2026 thành 2006.', 'nhãn đối trọng.', {'compares': '@S30.3:compares', 'and': '@S30.3:and'}, [], 0.46, 'thận trọng', '—'),
 ('f6', 'S31.1', 'chart', 'Giới hạn trên thẻ, phương pháp ở mô tả: US only, history not a forecast.', 'thẻ V7.', {'card': '@S31.1:card'}, ['thẻ trượt'], 0.32, 'tỉnh', 'lia máy'),
 ('f7', 'S32.1', 'chart', 'Trở lại câu hỏi của Nina.', 'phố từ trên.', {'question': '@S32.1:question'}, [], 0.36, 'mở', '—'),
 ('f8', 'S32.2', 'chart', 'Bảng điểm: đa số sáng, dãy tối ở giữa, ở lâu ít cửa tối, đèn theo thẻ.', 'bảng điểm 4 dòng trên phố.', {'lit': '@S32.2:lit', 'stretch': '@S32.2:stretch', 'stays': '@S32.2:stays', 'tag': '@S32.2:tag'}, ['tick ×4'], 0.38, 'mở', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('f9', 'S32.3', 'world', 'Cùng con phố lúc đầu, nay sáng từng nhà bằng điều đã xảy ra.', 'khung 0:00: phố chạng vạng, nay sáng/tối.', {'same': '@S32.3:same', 'lit': '@S32.3:lit'}, ['cửa sổ xa bật'], 0.4, 'mở', '—'),
 ('f10', 'S32.4', 'world', 'Câu của Nina: không có luật; tuỳ tháng bắt đầu và tiền thuê giả định; đèn là lịch sử.', 'Nina + đèn; câu hỏi của cô.', {'answer': '@S32.4:answer', 'history': '@S32.4:history'}, ['đèn ù'], 0.44, 'mở', 'đẩy máy'),
 ('f11', 'S33.1', 'world', 'Một câu hỏi còn mở: nếu tiền mặt của người thuê được đầu tư?', 'hộp tiền mặt + hộp thứ hai đóng.', {'open': '@S33.1:open', 'invested': '@S33.1:invested'}, ['hộp kính ù'], 0.4, 'mở', 'tắt dần'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
moves = K.moves_of([
    ('m_c', 'mode', 'wEnd', 'cStacks', cue['f1']['first'], cue['f2']['six'], 1.0, 'số tháng đầu chỉ ở đồ thị', 'whoosh_mode', {}),
    ('m_dots', 'pan', 'cStacks', 'cDots', cue['f3']['fifty'], cue['f4']['lowest'], 1.6, 'đặt tháng đầu của Nina cạnh mọi tháng trên phố', 'whoosh_soft', {}),
    ('m_grid', 'pull', 'cDots', 'cGrid', cue['f6']['card'] + 3.0, cue['f7']['question'], 1.2, 'trở lại câu hỏi: cả phố từ trên', 'whoosh_soft', {'start': cue['f6']['card'] + 3.0, 'change': 'major'}),
    ('m_w', 'mode', 'cGrid', 'w0', cue['f8']['tag'], cue['f9']['same'], 0.9, 'về khung 0:00: cùng phố, đọc theo nghĩa mới', 'whoosh_mode', {}),
    ('m_door', 'push', 'w0', 'wDoor', cue['f9']['lit'], cue['f10']['answer'], 2.0, 'đẩy về cửa của Nina cho câu của cô', 'whoosh_push', {}),
    ('m_box', 'pan', 'wDoor', 'wBox', cue['f10']['history'], cue['f11']['open'], 1.8, 'câu hỏi còn mở: hộp tiền mặt chưa từng rời hộp', 'whoosh_soft', {}),
])
ev = [{'t': cue['f1']['first'], 'kind': 'data', 'v': 0.5}, {'t': cue['f2']['two'], 'kind': 'data', 'v': 0.6}, {'t': cue['f3']['fifty'], 'kind': 'data', 'v': 0.57},
      {'t': cue['f4']['lowest'], 'kind': 'tick', 'v': 0.58}, {'t': cue['f6']['card'], 'kind': 'tick', 'v': 0.35}]
ev += [{'t': cue['f8'][k], 'kind': 'tick', 'v': 0.35 + 0.05 * j} for j, k in enumerate(('lit', 'stretch', 'stays', 'tag'))]
ev += [{'t': cue['f9']['lit'], 'kind': 'tick', 'v': 0.3}, {'t': cue['f11']['invested'], 'kind': 'tick', 'v': 0.25}]
K.finish(HERE, S, 'ep008 · F = S29–S33 (chương 6, giới hạn + kết)', beats, moves, ev,
         {'chapter': [0.2, 'The end of the street']},
         {'f2.six': 'September 2026 average: 6.86%', 'f2.two': "buyer's first month: $2,933", 'f3.fifty': '$1,667 = 56.8% of $2,933',
          'f4.lowest': 'lowest replayed: 57.9%, July 2006', 'f5.compares': 'first months only, not a forecast',
          'f8.lit': 'most start months: buyer ahead (about 3 in 4)', 'f8.stretch': 'dark stretch: April 2001 to December 2007',
          'f8.stays': 'held fifteen years: no dark doors in the record', 'f8.tag': 'the answer moves with the rent tag', 'f10.answer': 'Is her rent money wasted?',
          'f11.invested': 'invested? not measured here'},
         [k for b in beats for k in [f"{b['id']}.{c}" for c in b['cues']]])
