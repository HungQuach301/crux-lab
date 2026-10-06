# Mốc V · Hiện trạng Tập 1–4 (đo trên bản phát hành, 06/10/2026)

Nguồn video: Tập 1 `ep001-v2:episodes/ep001/review-c6/ep001-full-720p.mp4` · Tập 2 `episodes/ep002/review-c6/ep002-full-720p.mp4` · Tập 3 `episodes/ep003/review-c6/full-720p.mp4` · Tập 4 `ep004-delivery` (ghép 3 phần, SHA-256 `30090de0…` khớp `SHA256SUMS`).
Công cụ: `moc-v/measure/frames.py` (1 khung/giây: OCR tesseract + vùng đồ hoạ ngoài chữ + chuyển động ngoài chữ trong 0,5 s), `summary.py`; số thô `moc-v/measure/raw/`, `baseline-frames.jsonl`.
**Hiệu chuẩn bằng mắt:** 48 khung ngẫu nhiên (12/tập) — 46/48 xếp loại đúng; 2 sai ở Tập 4 (đường vừa bắt đầu vẽ, thang N2 mảnh → bị xếp "chỉ có chữ"). Sai lệch nghiêng về **đếm thừa** "chỉ có chữ" ở Tập 4 khoảng 2/12 khung → con số 40 % có thể là 30–40 %. Đối chiếu độc lập bằng timeline nhà máy Tập 4: mẫu `title` (thẻ chữ toàn màn hình) **131,6 s = 27 %**, `bignum` (số + chú thích, không hình) 28 s = 6 %, `method` + `endcard` 17,5 s = 4 % → **≈ 37 %** thời lượng là khung chữ/số không hình.

## Bảng

| | Tập 1 | Tập 2 | Tập 3 | Tập 4 |
|---|---|---|---|---|
| Thời lượng | 9:51 | 9:46 | 9:32 | 8:02 |
| **% thời lượng chỉ có chữ** (đo khung) | 2,2 % | 3,4 % | 7,3 % | **40,0 %** (timeline: ≈ 37 %) |
| Từ mới trên màn hình / phút (bền ≥ 2 s) | 128 (*) | 33 | 47 | **117** |
| Từ hiện trên khung (trung bình) | 31 | 10 | 26 | 24 |
| **% có đồ hoạ chuyển động** (cận trên của "mang nghĩa") | **35,9 %** | 21,0 % | 8,6 % | **10,4 %** |
| % đồ hoạ đứng yên | 61,9 % | 71,2 % | 83,9 % | 48,5 % |
| Vật thể thật (nhà, tiền, giấy tờ, lịch) | **có, 3D** (H1: nhà, cọc tiền, hoá đơn, đồng hồ) | không (hình học H2/H3) | không | không (chỉ hình người tĩnh S01/S04) |
| Nhân vật trên hình khi lời nhắc tên (hình người / vật hoặc dấu riêng của nhân vật) | 0/17 · **16/17** | 2/12 · ≈ 6/12 | 2/6 · 2/6 | 3/5 (thẻ người tĩnh) · 1/5 |
| Chuyển cảnh | 30 cắt, **mỗi cắt có lý do** (`transitions.json`) | 31 dip, có lý do | 12 cắt, có lý do | **36 cắt cứng, 0 lý do; 25 giữa hai mẫu khác nhau** (engine nhà máy không có chuyển cảnh) |
| Âm theo dữ liệu (sonify) | **có**, bảng S2 | có (1.985 sự kiện) | **không** (0 sự kiện) | **không** (nhà máy không có lớp này; L1 CHÍNH giải thích) |
| Hiệu ứng âm (sfx) | không (A11: 0) | không | không | không |
| Room tone + vào khoảng lặng (G-003) | có (−66 dBFS, τ 90 ms) | có | có | **không** (nhà máy chỉ trộn lời + nhạc) |
| Độ lặp nhạc | 29 % (T2) | 64,8 % → bản B 19,7 % | 57,6 % (T2 của checks) | **25 % cặp câu nhạc ≥ 0,90** (đo lại: `d_music_selfsim.py` trên nhạc sinh lại `bed_mr.py`, 56 cặp, TB 0,873) |
| Nhạc khớp căng–chùng (DX-R1) | có tension-map; nhạc C5 đổi theo hồi | có tension-map | tension-map có nhưng nhạc một mạch style C | **không**: một mạch style C 114 BPM suốt tập, chỉ hạ 0 quanh 2 mid-roll |
| **Phiếu L3** của chủ dự án | 4·5·4·4·4·4 | không chấm từng dòng (phát hành CÓ) | không chấm; *"mấy phút đầu chưa đủ thu hút"* | không chấm (G2 chọn (b) sửa nhãn) |
| Nhận xét chủ dự án | "hình tự mang ý nghĩa" = mục tiêu số 1 Tập 2 (C4); nhạc chậm, buồn → C (G-016) | cổng gốc 3/7 → sửa bằng nhãn → ngoại lệ (b) | móc yếu (hook 2/5) | cổng gốc 3/7 → sửa nhãn → 6/7; tóm tắt AI hook 2 · nhịp 3 |

(*) Tập 1: OCR đọc cả chữ in trên vật thể 3D chuyển động (biển, hoá đơn) nên số "từ mới" bị thổi; số đáng tin là "chỉ có chữ 2,2 %".

## Nguyên nhân gốc

1. **Sửa cổng gốc bằng NHÃN CHỮ thay vì sửa HÌNH.** Từ Tập 2 C4c (KEY-2/5/6/7) tới Tập 4 G2 (S06, S09/S10, S11, S15): khi nhịp trượt nghĩa, đường sửa nằm trong danh sách đóng §6.6 là thêm nhãn ≤ 8 từ. Điểm cổng gốc lên (Tập 4: 3/7 → 6/7) nhưng hình không đổi; chữ dày thêm (Tập 4: 117 từ mới/phút).
2. **Lớp chữ bắt buộc thành THẺ toàn màn hình.** Đối trọng, giới hạn, "not a tax bill", "history, not a forecast", câu hỏi chuyển ý đều đi qua mẫu `title`: Tập 4 có 13 thẻ = 131,6 s (27 %). S02 cả cảnh 24 s là 4 dòng giới hạn; S17 3 thẻ liền.
3. **Nhà máy (Mốc B) bỏ 3D, bỏ sonify, bỏ sfx/room tone, bỏ chuyển cảnh.** Thư viện mẫu chỉ có 10 mẫu 2D tĩnh (`bignum`, `title`, `bars`, `line`, `person`…) + "đẩy máy 1,000 → 1,015"; `music.py` chỉ trộn lời + nhạc. Tập 1 (làm tay) có vật thể thật 3D, sonify S2, room tone, 30 chuyển cảnh có lý do; Tập 4 (nhà máy) mất cả bốn. Hồi quy chất lượng do tối ưu tốc độ không có số đo đối chứng.
4. **Các lớp làm riêng rẽ, không ai kiểm tổng thể.** Kịch bản (WRITER) → beats → hình (mẫu theo shot) → giọng → nhạc (một mạch, sinh theo tổng thời lượng) → checks từng lớp. Không có đặc tả chung "ý · lời · hành động hình · âm · trạng thái nhạc" cho mỗi nhịp; nhạc không biết nhịp căng; hình không có sự kiện âm; không có lượt xem tổng thể có tiếng trước render (lượt đạo diễn).
5. **Nguyên tắc tốc độ (D-006) + trần ký hiệu (≤ 2/tập) + trần token** đẩy lỗi CHÍNH vào hàng chờ và chặn hình mới; ngưỡng phát hành không đòi phiếu L3 → Tập 3, Tập 4 phát hành không chấm L3 từng dòng.
