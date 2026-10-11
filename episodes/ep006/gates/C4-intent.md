# C4 — ý đồ kiểm mù (ghi TRƯỚC khi có animatic; không sửa sau khi thấy kết quả)

Ngày 2026-10-09 (phiên P3b). Nguồn hình: animatic 720p cả tập (`out/video.mp4` của build C4). Người đọc headless (`toolkit/blind/headless.sh`, mỗi lượt MỚI, chỉ mở tệp tên hex). Vai T (như C3): *"You are an American aged 64, about to retire, looking at an income annuity quote that offers two payout options."*

**Câu hỏi cố định** (C3 + K4.1 A21; REVIEWER CHÍNH-5): 1. What idea is this showing? 2. What changes over time? 3. What does it mean? 4. What advice, if any, would a viewer take from this? 5. — **A** (tắt tiếng, nguyên văn §5.3): *Did the animation itself suggest this, or is it your own conclusion?* — **B/C/E** (có lời): *Did the video itself (picture, on-screen text or narration) suggest this, or is it your own conclusion?* — cả hai thêm: *If you gave no advice in 4, answer 'none'.* A và B/C/E dùng hai khoá riêng (`c4/root-*`, `c4/voiced-*`).
**Lượt và token ghi trước** (`episode.md` §2): A 46 lượt ảnh (+ người thứ 3) ≈ 0,5 triệu; B/C/E 3 + 3 + 3 + 3 (+ 3 kiểm tra phụ) lượt ≈ 0,2 triệu; chấm 2 người × 2 gói.

## A. Cổng gốc tắt tiếng (nhịp loại 1, `story/beats.md`)
- Mẫu: dải 6 khung đều trong khoảng cảnh của nhịp, **tắt tiếng, giữ chữ/số** (`toolkit/blind/strips.py`; mốc ở `review-c4/spans.json` sinh từ `out/timeline.json`). Nhịp loại 1: B01 B03 B04 B06 B07 B08 B09 B10 B12 B13 B14 B15 B16 B17 B19 B21 B22 B24 B25 B27 B29 B30 B32 (23). Loại 2 (B02 B05 B11 B23 B26 B28 B31) chỉ kiểm câu khuyên — **không chạy ở C4** trừ khi bản có lời (B) gặp khuyên ở cảnh đó.
- 2 người đọc mỗi nhịp; lệch → người thứ 3 (chấm riêng). Nhịp đạt khi ≥ 2/3 đúng (nghĩa 1, không khuyên). Nghĩa so với **"muted read" chép nguyên văn** `beats.md`.
- **Ngưỡng cổng: ≥ 80 % nhịp loại 1 đạt**, khuyên 0: đạt cần **19/23 (82,6 %)**; **18/23 (78,3 %) và 19/23 nằm trong ±5 % quanh ngưỡng → nêu tên** (§2.2). Tally chạy `--classes` (bảng phân loại `story/beats.md` cột loại, SHA-256 ghi kèm, §5.8).
- **Ngoại lệ C3 (chủ dự án 08/10):** B29/S29 ở A chỉ xét **nghĩa** (≥ 2/3 nghĩa 1); cờ khuyên của S29 ghi vào bảng nhưng **gỡ khỏi `advice_beats` bằng tay**; báo **cả hai** verdict: của `tally` và sau ngoại lệ. Cờ khuyên S29 được xét ở chốt (C).

## B. Chốt chặn bản có lời CẢ TẬP (chủ dự án C3 câu 3)
- Mẫu: **nguyên văn lời cả tập** (phụ đề `out/captions.srt` theo mốc giây, như người xem nghe) + **4 tấm ảnh** khung theo hồi (mỗi tấm 12 khung đều của hồi: cold open + hồi 1 · hồi 2 · hồi 3 · giới hạn + kết), đúng thứ tự giờ. Tấm 12 khung dựng bằng `sheet()` trong `c4/blind_c4.py` (mã mới, ghi SHA ảnh), không phải `strips.py` (cố định 6 khung). 3 người đọc (vai T), câu hỏi 1–5 trên toàn tập.
- **Ngưỡng: câu khuyên sản phẩm = 0 / 3** (chọn khoản đều, khoản tăng 2 %, khoản gắn CPI/COLA; mua/không mua niên kim; chọn công ty). "Hỏi công ty bảo hiểm / hỏi báo giá / tự kiểm số" = thận trọng chung, **không tính** (C3 câu 3).
- **B trượt** (≥ 1/3 câu khuyên theo rubric cũ) → **dừng, hỏi chủ dự án** kèm câu trích (như C); không mở vòng sửa (không được đổi lời).

## C. Chốt chặn bản có lời S29 (chủ dự án C3 câu 1)
- Mẫu: dải 6 khung của S29 + lời S29 (và câu cuối S28 làm ngữ cảnh) **lấy từ `out/captions.srt`** theo khoảng giờ của cảnh, như người xem nghe. 3 người đọc (vai T). **Ngưỡng: câu khuyên sản phẩm (chọn khoản gắn CPI/COLA) = 0 / 3.** Không đạt → **dừng, hỏi chủ dự án** (không sửa thêm vòng).

## D. Chấm: hai rubric song song, 2 người chấm (K4.1 câu 3, chạy thử)
- Gói chấm `packets.py packet` (khoá nhãn commit trước khi chấm). **2 người chấm headless độc lập** chấm cùng gói; mỗi bản chấm ghi `score`, `advice_stated`, `advice_inferred`, `caution_only`, `quote` (trích nguyên văn).
- `packets.py tally --scores <chấm1> <chấm2>` gộp thận trọng (điểm thấp nhất; cờ nếu bất kỳ người chấm nào bật), **luôn báo cả hai rubric**: cũ (A9: mọi cờ khuyên = câu khuyên) và mới (chỉ `advice_stated`). **Cổng theo rubric cũ**; hai rubric lệch → giữ rubric cũ, ghi lệch vào ledger + `checks-appeal.md` cho K.
- Với (B) và (C) (không theo nhịp): đếm thẳng; "câu khuyên" theo rubric cũ là quyết định cổng, rubric mới báo song song.
- **Nghĩa (B):** chép nguyên văn "Đúng câu hỏi" + "Đúng đáp án" của `c2/rubric.md`. **Nghĩa (C, E):** muted read B29 nguyên văn + "cùng 2 %, kết quả do tháng bắt đầu".
- **Ranh giới khuyên** (chủ dự án C3 câu 3): "ask the insurer how much smaller the rising check starts" / "ask what an inflation-linked option would cost" = `caution_only`. "weigh / consider / prefer / compare and choose the inflation-adjusted (COLA) option" = câu khuyên. Cả hai người chấm nhận đúng đoạn này.
- **Báo bảng câu 5** (video / tự suy / none) theo từng mẫu. Mẫu dương bị chấm `advice_inferred` thay vì `advice_stated` → ghi "rubric mới hụt mẫu dương".

## E. Đối chứng hình thật (K4.1 câu 3) — chỉ để biết bộ đo phân biệt được, không tính vào cổng
- **Dương:** dải 6 khung **thật** của S29 + lời S29 **thêm một câu khuyên**: *"So if you are choosing today, take the payout that is tied to inflation."* — kỳ vọng `advice_stated` ở ≥ 2/3 người đọc theo cả hai rubric.
- **Âm (cặp khớp, REVIEWER CHẶN-1):** dải 6 khung thật của S29 + lời S29 + **một câu trung tính cùng độ dài, không hành động**: *"So the same raise ended in three different places, set by the month each one started."* Kỳ vọng `advice_stated` ≤ 1/3 người đọc. Cờ `advice_inferred` ở mẫu âm được ghi lại: rubric cũ bắt được mà rubric mới không bắt thì đó chính là chỗ hai rubric phân biệt. Mẫu Tập 5 S06 (lời C4, có lời 3/3 khuyên 0) chỉ chạy làm **kiểm tra phụ**, không thuộc điều kiện dùng rubric mới.
- Mỗi đối chứng 3 người đọc, chấm trong cùng gói (nhãn `ctrl:`). Rubric mới chỉ được dùng ở cổng sau này khi: dương bắt ≥ 2/3 **và** âm ≤ 1/3 **và** không lệch với rubric cũ ở bộ ứng viên. Không đạt → ghi "rubric mới chưa phân biệt", giữ rubric cũ.

## F. Sửa
- Nhịp trượt nghĩa/khuyên → sửa bằng hình trước (D-009 E6; cảnh 3D trượt độ đọc → chế độ đồ thị), nhãn là cách cuối; ≤ 3 vòng mỗi lỗi mỗi cảnh; khoá nghĩa (bản sau không thấp hơn bản tốt nhất, không thêm câu khuyên); hết vòng → G2 nêu trước/sau. **Không đổi lời** (đổi kịch bản đã duyệt = ngoại lệ phải hỏi; EL 7.699/7.700).
- **Độ dài:** mọi sửa đo lại tổng timeline; trần cứng 540,0 s.
- **Lượt đạo diễn** (chẩn đoán): trước render 1080p, 2 lượt độc lập trên bản 540p/720p; chỉ sửa nhận xét lặp ở cả hai.

_Sửa trước khi chạy theo REVIEWER (`gates/REVIEW-C4-intent.md`: 2 CHẶN, 5 CHÍNH, 4 PHỤ — áp đủ), 09/10, chưa có lượt đọc nào._
