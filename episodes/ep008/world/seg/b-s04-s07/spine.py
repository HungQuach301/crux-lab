"""Tập 8 · ĐOẠN B = S04–S07 (chương 2 "Two twins, one rent tag", hồi 1) → MR1 trong đuôi S07. Lời + giờ = timeline nhà máy (0 ký tự EL).
B04 (S04): hai người song sinh — căn hộ (thuê) và nhà (mua); người mua đặt cọc + chi phí đóng vào nhà, giấy vay; mỗi tháng chi phí rơi vào khe (nhãn chữ:
interest, property tax, insurance, repairs, cost of selling) → đồ thị "2.5% a year · cost of selling: 6%" → người thuê vào căn hộ, giữ cùng khoản để dành.
B05 (S05): hộp kính CASH (N4 v2): tiền để dành của người thuê nằm tiền mặt, không cổ phiếu (nhãn "cash, not stocks"); hai chồng đặt cọc/đóng bay vào hộp; mỗi
tháng một bó bay từ CỬA căn hộ vào hộp; biến thể T-bill = hộp ánh nhẹ; hộp thứ hai đóng, không nhãn ("invested? not measured here"); thẻ V7 những gì không tính.
B06 (S06): đồ thị: một đường giả định phẳng → bản ghi thật của Mỹ tích từng tháng (giá nhà, tiền thuê, lãi) — sửa điểm yếu đối thủ; mức tiền thuê khởi đầu = ô trống.
B07 (S07): thẻ RENT treo cửa căn hộ (5 %); "US only": bản đồ 48 bang dưới mặt đất (Natural Earth); đồ thị "starting rent: 5% a year (assumption) · $1,667 a
month"; thẻ quyết bao nhiêu tiền vào hộp mỗi tháng; thẻ lay ("the tag turns") → lặng 1,5 s MR1."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W8 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, W8)
import kit as K
SV = K.SV
S = K.Seg(['S04', 'S05', 'S06', 'S07'])
B = [
 ('b0', 'S04.1', 'world', 'Mỗi người song sinh thật sự trả gì?', 'căn hộ (thuê) và nhà (mua) hai bên Nina.', {'pay': '@S04.1:pay'}, [], 0.24, 'tập trung', 'lia máy'),
 ('b1', 'S04.2', 'world', 'Người mua trả đặt cọc + chi phí đóng, vay 30 năm cố định ở lãi trung bình tháng đó.', 'hai chồng bay vào nhà; giấy vay ở cửa nhà.',
  {'down': '@S04.2:down', 'closing': '@S04.2:closing', 'mortgage': '@S04.2:mortgage'}, ['bịch giấy ×2', 'tick'], 0.26, 'tập trung', '—'),
 ('b2', 'S04.3', 'world', 'Mỗi tháng: lãi, thuế, bảo hiểm, sửa chữa; cuối cùng: chi phí bán.', 'chi phí rơi vào khe nhà, mỗi khoản một nhãn chữ.',
  {'interest': '@S04.3:interest', 'owning': '@S04.3:owning', 'selling': '@S04.3:selling'},
  ['tích ×3'], 0.3, 'tập trung', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b3', 'S04.4', 'chart', 'Thuế + bảo hiểm + sửa chữa = 2,5 % giá trị nhà mỗi năm.', 'nhãn mức chi sở hữu + chi phí bán.', {'two': '@S04.4:two'}, ['tick'], 0.3, 'tập trung', '—'),
 ('b4', 'S04.5', 'chart', 'Người thuê vào căn hộ tương đương, giữ cùng khoản để dành.', 'người thuê bước vào cửa căn hộ; chồng để dành cạnh.',
  {'rents': '@S04.5:rents', 'savings': '@S04.5:savings'}, ['bước chân'], 0.3, 'tập trung', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('b5', 'S05.1', 'world', 'Tiền để dành của người thuê nằm tiền mặt, không cổ phiếu.', 'hộp kính CASH đóng; nhãn "cash, not stocks".',
  {'cash': '@S05.1:cash', 'stocks': '@S05.1:stocks'}, ['keng kính'], 0.32, 'bất ngờ', '—'),
 ('b6', 'S05.2', 'world', 'Đống tiền bắt đầu bằng đặt cọc + chi phí đóng không vào nhà.', 'hai chồng bay vào hộp.', {'down': '@S05.2:down'}, ['bịch giấy'], 0.32, 'rõ', '—'),
 ('b7', 'S05.3', 'world', 'Tiền thuê tiết kiệm mỗi tháng cộng vào cùng đống.', 'mỗi tháng một bó bay từ cửa căn hộ vào hộp.', {'month': '@S05.3:month'}, ['bịch nhỏ'], 0.32, 'rõ', '—'),
 ('b8', 'S05.4', 'world', 'Biến thể: tiền mặt có lãi T-bill, không hơn.', 'hộp ánh nhẹ.', {'treasury': '@S05.4:Treasury'}, [], 0.32, 'rõ', '—'),
 ('b9', 'S05.4', 'world', 'Đầu tư phần chênh: câu hỏi khác, tập này không trả lời.', 'hộp thứ hai đóng, không nhãn.', {'investing': '@S05.4:investing'}, [], 0.34, 'rõ', '—'),
 ('b10', 'S05.6', 'world', 'Vài khoản không tính, thẻ liệt kê.', 'thẻ V7.', {'card': '@S05.6:card'}, ['thẻ trượt'], 0.32, 'rõ', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b11', 'S06.1', 'chart', 'Phép tính quen: một tốc độ tăng cho giá, một cho tiền thuê, một đáp án.', 'một đường phẳng vẽ ra.', {'growth': '@S06.1:growth', 'single': '@S06.1:single'}, ['bút vạch'], 0.32, 'nghi', '—'),
 ('b13', 'S06.3', 'chart', 'Ở đây: giá, tiền thuê, lãi từ bản ghi tháng thật của Mỹ.', 'ba dải bản ghi thật tích từng tháng.',
  {'prices': '@S06.3:prices', 'rents': '@S06.3:rents', 'rates': '@S06.3:rates'}, ['tích từng tháng'], 0.38, 'chú ý', '—'),
 ('b14', 'S06.4', 'chart', 'Một thứ không lấy được từ bản ghi: mức tiền thuê khởi đầu.', 'ô trống "starting rent".', {'rent': '@S06.4:rent'}, ['tick'], 0.4, 'chú ý', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('b15', 'S07.1', 'world', 'Nó treo trên cửa căn hộ thành thẻ: tiền thuê khởi đầu 5 %/năm.', 'thẻ RENT 5 % trên cửa; bản đồ "US only" dưới mặt đất.',
  {'tag': '@S07.1:tag', 'five': '@S07.1:five'}, ['lật thẻ + vòng kim loại'], 0.44, 'chú ý', 'CHUYỂN CHẾ ĐỘ → đồ thị'),
 ('b16', 'S07.2', 'chart', 'Nhà $400,000 → $1,667/tháng hôm nay, lùi theo chỉ số tiền thuê.', 'nhãn tiền thuê.', {'one': '@S07.2:one', 'history': '@S07.2:history'}, ['tick'], 0.46, 'chú ý', 'CHUYỂN CHẾ ĐỘ → thế giới'),
 ('b17', 'S07.3', 'world', 'Thẻ quyết bao nhiêu tiền vào hộp mỗi tháng.', 'bó từ cửa vào hộp theo thẻ.', {'aside': '@S07.3:aside', 'grows': '@S07.3:grows'}, ['bịch nhỏ'], 0.48, 'chú ý', '—'),
 ('b18', 'S07.4', 'world', 'Sau này thẻ xoay, đáp án xoay theo.', 'thẻ lay.', {'turns': '@S07.4:turns'}, ['lật thẻ'], 0.4, 'mở', 'MR1'),
]
beats = SV.beats_from(B, S.A, S.lines)
cue = {b['id']: b['cues'] for b in beats}
MR, MRSIL = K.midroll(S, 0)
moves = K.moves_of([
    ('m_in', 'push', 'wWide', 'wTwins', 0.0, cue['b0']['pay'], 1.4, 'mở chương: hai người song sinh hai bên Nina', 'whoosh_air', {}),
    ('m_c1', 'mode', 'wTwins', 'cTwins', cue['b2']['selling'], cue['b3']['two'], 1.2, 'mức 2,5 % và 6 % chỉ ở đồ thị (quy tắc 1)', 'whoosh_mode', {}),
    ('m_w1', 'mode', 'cTwins', 'wBox', cue['b4']['savings'], cue['b5']['cash'], 1.6, 'S05: hộp tiền mặt của người thuê cần khung riêng (bài học C1)', 'whoosh_mode', {}),
    K.reframe(S, beats, 'm_r1', 'push', 'wBox', 'wBox~', 'S05.6:costs', 'các khoản không tính: lại gần hộp tiền mặt + thẻ'),
    ('m_c2', 'mode', 'wBox~', 'cRecord', cue['b10']['card'], cue['b11']['growth'], 1.2, 'S06 so một giả định với bản ghi thật: đồ thị', 'whoosh_mode', {}),
    ('m_w2', 'mode', 'cRecord', 'wDoor', cue['b14']['rent'], cue['b15']['tag'], 1.2, 'giả định duy nhất nằm trên cửa của Nina (thế giới)', 'whoosh_mode', {}),
    ('m_c3', 'mode', 'wDoor', 'cTag', cue['b15']['five'], cue['b16']['one'], 1.2, 'tiền thuê $1,667 chỉ ở đồ thị', 'whoosh_mode', {}),
    ('m_w3', 'mode', 'cTag', 'wFlow', cue['b16']['history'], cue['b17']['aside'], 1.4, 'thẻ → hộp: tiền thuê quyết phần để dành (thế giới)', 'whoosh_mode', {}),
])
ev = [{'t': cue['b1'][k], 'kind': 'data', 'v': v} for k, v in (('down', 0.4), ('closing', 0.3))]
ev += [{'t': cue['b2'][k], 'kind': 'tick', 'v': 0.35} for k in ('interest', 'owning', 'selling')]
ev += [{'t': cue['b3']['two'], 'kind': 'tick', 'v': 0.4}, {'t': cue['b5']['cash'], 'kind': 'tick', 'v': 0.5}, {'t': cue['b6']['down'], 'kind': 'data', 'v': 0.45},
       {'t': cue['b7']['month'], 'kind': 'data', 'v': 0.3}, {'t': cue['b10']['card'], 'kind': 'tick', 'v': 0.35}, {'t': cue['b11']['growth'], 'kind': 'tick', 'v': 0.3},
       {'t': cue['b13']['prices'], 'kind': 'rise', 'dur': 1.6}, {'t': cue['b15']['tag'], 'kind': 'tick', 'v': 0.45}, {'t': cue['b16']['one'], 'kind': 'tick', 'v': 0.45},
       {'t': cue['b17']['aside'], 'kind': 'data', 'v': 0.35}, {'t': cue['b18']['turns'], 'kind': 'tick', 'v': 0.4}]
K.finish(HERE, S, 'ep008 · B = S04–S07 (chương 2, hồi 1) → MR1', beats, moves, ev,
         {'chapter': [0.2, 'Two twins, one rent tag'], 'midroll': MR,
          'at': {k: S.at('@' + k) for k in ('S05.3:Whatever', 'S07.3:month', 'S06.3:record', 'S05.4:different')}},
         {'b3.two': '2.5% a year · cost of selling: 6%', 'b5.stocks': 'cash, not stocks', 'b9.investing': 'invested? not measured here',
          'b11.growth': 'one assumed growth rate', 'b13.prices': 'the real monthly US record', 'b14.rent': 'starting rent: ?',
          'b16.one': 'starting rent: 5% a year (assumption) · $1,667 a month'},
         ['b0.pay', 'b1.down', 'b1.closing', 'b1.mortgage', 'b2.interest', 'b2.owning', 'b2.selling', 'b3.two', 'b4.rents', 'b4.savings',
          'b5.cash', 'b5.stocks', 'b6.down', 'b7.month', 'b8.treasury', 'b9.investing', 'b10.card', 'b11.growth', 'b11.single', 'b13.prices',
          'b13.rents', 'b13.rates', 'b14.rent', 'b15.tag', 'b15.five', 'b16.one', 'b16.history', 'b17.aside', 'b17.grows', 'b18.turns'],
         silences=[MRSIL])
