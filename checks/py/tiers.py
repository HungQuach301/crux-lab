"""Severity tier of every rule (K3). Only a BLOCK rule fails the episode; a MAJOR rule that does not pass needs the builder's written
explanation (out/explanations.json); a REFERENCE rule only reports its measurements.

    BLOCK     (CHẶN, L1)      numbers, claims, sources, terms of use, asset rights, file technique, loudness, true peak, key words heard (ASR)
    MAJOR     (CHÍNH)         the voice is clear (not covered), text does not collide, contrast, legible at 25%; owner (K3 approval): F07 length, A18 voice model
    REFERENCE (THAM KHẢO)     every craft or count target (anti-Goodhart: a count of techniques is a warning, not a goal)

Cine Lab, CINE-LAB-KHUNG-CHAT-LUONG.md §1 (3 layers; anti-Goodhart principle 5) and CINE-LAB-BAI-HOC-BRIEF-D.md W2, W3, N2, N3."""

BLOCK, MAJOR, REFERENCE = 'BLOCK', 'MAJOR', 'REFERENCE'
LABEL = {BLOCK: 'CHẶN', MAJOR: 'CHÍNH', REFERENCE: 'THAM KHẢO'}

_B = 'kỹ thuật file'
TIERS = {
    # file technique
    'F01': (BLOCK, _B), 'F02': (BLOCK, _B), 'F03': (BLOCK, _B), 'F04': (BLOCK, _B), 'F05': (BLOCK, _B), 'F06': (BLOCK, _B),
    'F07': (MAJOR, 'độ dài theo CHARTER §1 (8–15 phút); chủ dự án hạ CHÍNH: chặn độ dài dễ dẫn tới giãn thời gian'),
    'F08': (BLOCK, 'kỹ thuật file: banding do mã hoá'),
    'F09': (BLOCK, 'kỹ thuật file: phụ đề đúng lời, đúng quy cách'),
    'F10': (BLOCK, 'kỹ thuật file: chapters hợp lệ với YouTube (≥ 3, từ 0:00, mỗi chương ≥ 10 s)'),
    'F11': (BLOCK, 'kỹ thuật file: artefact phát hành đã giao'),
    'F12': (BLOCK, 'quyền tài sản'),
    # loudness, true peak, the master's audio technique
    'A01': (BLOCK, 'âm lượng'), 'A02': (BLOCK, 'true peak'),
    'A03': (REFERENCE, 'độ động (LRA) là lựa chọn nghề; nền tảng chỉ chuẩn hoá âm lượng tích hợp (A01)'),
    'A04': (BLOCK, 'kỹ thuật file: clip'), 'A05': (BLOCK, 'kỹ thuật file: pha'), 'A06': (BLOCK, 'kỹ thuật file: gộp mono'),
    'A07': (REFERENCE, 'tỉ lệ lời/nhạc là chỉ tiêu mix; độ rõ lời do L1 và A14 canh'),
    'A08': (REFERENCE, 'cách duck nhạc là tay nghề'),
    'A09': (REFERENCE, 'số lần dùng kỹ thuật (≥ 3 khoảng lặng)'),
    'A10': (REFERENCE, 'tay nghề: whoosh theo máy'), 'A11': (REFERENCE, 'tay nghề: pan theo vật'),
    'A12': (REFERENCE, 'tay nghề: điểm nhấn nhạc'), 'A13': (REFERENCE, 'tay nghề: giãn giọng'),
    'A14': (BLOCK, 'ASR không mất từ khoá'),
    'A15': (REFERENCE, 'chỉ tiêu tốc độ đọc'),
    'A16': (REFERENCE, 'cảnh báo: dấu ngắt giả trong văn bản gửi TTS'),
    'A17': (REFERENCE, 'cảnh báo: mật độ khoảng lặng giữa câu bất thường'),
    'A18': (MAJOR, 'đổi model giọng giữa tập; chủ dự án nâng CHÍNH: lỗi gốc của Tập 1 v1, trái G-010'),
    # numbers, claims, sources, terms
    'S01': (BLOCK, 'số liệu: tính lại mô hình'), 'S02': (BLOCK, 'claim: giả định của mô hình hiện trên màn hình'),
    'S03': (BLOCK, 'nguồn và điều khoản sử dụng dữ liệu'), 'S04': (BLOCK, 'số liệu: đối chiếu nguồn'),
    'S05': (BLOCK, 'claim khớp mô hình; ILLUSTRATIVE'), 'S06': (BLOCK, 'số liệu: hiện đủ mọi trường hợp đã hứa (không chọn lọc)'),
    'S07': (BLOCK, 'claim: mọi số có claim, công thức, nguồn'), 'S08': (BLOCK, 'claim: huy hiệu ILLUSTRATIVE'),
    'S09': (BLOCK, 'claim: thực/danh nghĩa'), 'S10': (BLOCK, 'claim: không khuyên, không dự báo (gen được bảo vệ, CHARTER §5)'),
    'S11': (REFERENCE, 'số lần dùng kỹ thuật (callback ≥ 3)'), 'S12': (REFERENCE, 'chỉ tiêu mật độ số'),
    'S13': (REFERENCE, 'chỉ tiêu độ dài câu'), 'S14': (REFERENCE, 'tay nghề: điểm chèn quảng cáo'),
    'S15': (REFERENCE, 'tay nghề: cấu trúc hồi, sàn tổng theo format (K3.8: bỏ trần cold open)'), 'S16': (REFERENCE, 'chỉ tiêu gắn số với nhân vật'),
    'S17': (BLOCK, 'claim: nhãn điều kiện trên mọi khung có claim conditional (K3.8, A1)'),
    'S18': (REFERENCE, 'giữ chân: mốc hook ≤ 5 s, promise ≤ 30 s (K3.8, A2)'),
    # Shorts 9:16 (K3.8, A5)
    'SH01': (BLOCK, 'kỹ thuật file: Short 1080×1920'), 'SH02': (BLOCK, 'kỹ thuật file: Short ≤ 180 s'),
    'SH03': (BLOCK, 'âm lượng: Short'), 'SH04': (BLOCK, 'true peak: Short'),
    'SH05': (BLOCK, 'claim: Short không khuyên, không dự báo (gen được bảo vệ)'),
    # rhythm
    'R01': (REFERENCE, 'luật nhịp'), 'R02': (REFERENCE, 'luật nhịp'), 'R03': (REFERENCE, 'luật nhịp'),
    'R04': (REFERENCE, 'luật nhịp'), 'R05': (REFERENCE, 'luật nhịp'), 'R06': (REFERENCE, 'luật nhịp'),
    # picture
    'V01': (REFERENCE, 'tay nghề: hồ sơ tiền kỳ'), 'V02': (REFERENCE, 'tay nghề: bố cục một phần ba'),
    'V03': (MAJOR, 'đọc được: chữ ngoài vùng an toàn bị giao diện trình phát che'),
    'V04': (REFERENCE, 'tay nghề: nhận diện nhân vật'), 'V05': (REFERENCE, 'tay nghề: chuyển động máy'),
    'V08': (MAJOR, 'tương phản'), 'V09': (MAJOR, 'tương phản: mù màu'),
    'V10': (REFERENCE, 'số lần dùng kỹ thuật (match cut, J/L-cut)'),
    'V11': (MAJOR, 'va chạm chữ'), 'V12': (MAJOR, 'đọc được: chữ nhân đôi, nhoè'),
    'V13': (REFERENCE, 'chỉ tiêu thời lượng cú máy'),
    'C01': (REFERENCE, 'tay nghề: lộ panel khác cảnh'),
    'C02': (MAJOR, 'va chạm: nền đè lên dữ liệu'),
    'C03': (REFERENCE, 'tay nghề: nhãn đường'), 'C04': (REFERENCE, 'tay nghề: trục và mốc'),
    'C05': (MAJOR, 'tương phản: nhấn mạnh trong thang xám'),
    'C06': (REFERENCE, 'tay nghề: màu số theo chuỗi'),
    'C07': (BLOCK, 'số liệu: cột bị cắt trục hoặc lệch tỉ lệ làm sai số liệu'),
    'C10': (REFERENCE, 'tay nghề: một chữ cấp 1'), 'C11': (REFERENCE, 'tay nghề: lặp bố cục'),
    'C12': (REFERENCE, 'tay nghề: thay đổi chia đôi khung'), 'C13': (REFERENCE, 'luật nhịp: số khớp lời ±250 ms'),
    'C14': (MAJOR, 'đọc được ở 25%'), 'C15': (REFERENCE, 'tay nghề: chỉ dùng token màu'),
    'P01': (REFERENCE, 'tay nghề: thumbnail'),
    # sound
    'T1': (REFERENCE, 'chỉ tiêu tay nghề: tiếng dữ liệu nghe thấy'), 'T2': (REFERENCE, 'chỉ tiêu tay nghề: nhạc không lặp'),
    'T3': (REFERENCE, 'chỉ tiêu tay nghề: vào khoảng lặng'),
    'L1': (MAJOR, 'độ rõ lời: tiếng dữ liệu không lấn lời'),
    # regression gate: blocks only on a BLOCK rule that regressed (run.regression)
    'REG': (BLOCK, 'cổng hồi quy của luật CHẶN (CHARTER §5)'),
}


def tier(rid):
    return TIERS[rid][0]
