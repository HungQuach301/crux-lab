# C3 Tập 7 — ý đồ cổng gốc (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-11 (phiên P2). Hình mới / vật thể trung tâm theo G1 lô câu 3: **N1 Month track** (vật thể 3D mới, `world/obj7.js`), **"the stack"** (W2 `Stack` cạnh nhà — dùng mới làm vật thể trung tâm của tập), **"the bar"** (W3 `Beam` = mốc lãi khoản vay — dùng mới). Năm đoạn thế giới có lời thật (Eric, take commit ở `voice-takes/`), đều nhịp **loại 1** trong `story/beats.md`:

| Đoạn | Nhịp | Cảnh | Vật thể |
|---|---|---|---|
| `s01-stack` | B01 · KEY-1 | S01 | W1 + W4 + W2 (the stack) |
| `s06-stack` | B06 · KEY-3 | S06 | V4 adapted + W2 + W1 (the stack đứng đủ cao) |
| `s21-track` | B21 · KEY-9 | S21 | **N1** + W1 + W4 |
| `s23-track` | B23 | S23 | **N1** |
| `s25-bar` | B25 · KEY-10 | S25 | W3 (the bar) + W1 |

- **Dải:** 6 khung **tắt tiếng, GIỮ chữ/số** từ clip 540p có chuyển động của mỗi đoạn (`toolkit/blind/strips.py`, mốc ở `world/c3/spans.json`); bản sao tên hex ở `c3/root/`.
- **Người đọc:** headless có ảnh (`toolkit/blind/headless.sh --read`, `c3/root_run.py`), mỗi lượt MỚI, chỉ mở một PNG; **2 người mỗi đoạn**; lệch → người thứ 3; đoạn đạt khi ≥ 2/3 (dừng khi 2 người đầu cùng kết quả).
- **Vai T** (= vai T của kiểm mù C2): "You are an American buying a home in an expensive city, with a mortgage of about $320,000 and a large monthly payment. You can just afford a 15-year payment, and you came wondering: should you pay extra on a mortgage, or invest the spare cash instead?"
- **Câu hỏi** (như C3 Tập 6, thêm câu 5 nguồn khuyên để chấm rubric mới): 1. What idea is this animation showing? 2. What changes over time across the frames? 3. What does it mean? 4. What advice, if any, would a viewer take from this? 5. Did the animation itself (picture or on-screen text) suggest this, or is it your own conclusion? If you gave no advice in 4, answer 'none'.
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" chép **nguyên văn** từ `beats.md` (`spans.json`). **Cờ khuyên theo rubric MỚI** (G1 câu 2, như Tập 6 C4): `advice_stated` (chính hình/chữ trên hình nêu/ngụ ý hành động: chọn 15/30 năm, trả thêm, đầu tư, trả tháng/năm, chờ/khoá lãi) → **trượt**; `advice_inferred` / `caution_only` chỉ báo, câu trích vào bảng. Người đọc đúng = nghĩa 1 và `advice_stated` false.
- **Ngưỡng mỗi đoạn:** ≥ 2/3 đúng, `advice_stated` 0. Trượt → **sửa bằng hình trước** (D-009; cảnh 3D trượt độ đọc → chế độ đồ thị), nhãn nghĩa là cách cuối và ghi lý do; ≤ 3 vòng mỗi đoạn; khoá nghĩa (bản sau không thấp hơn bản tốt nhất, không thêm cờ khuyên). Hết 3 vòng → gói C3 nêu trước/sau, chủ dự án chọn.
- **Lượt đạo diễn** (chẩn đoán, không ngưỡng): một lượt trên bản 540p của cả năm đoạn; chỉ sửa nhận xét lặp ở ≥ 2 lượt độc lập (lessons V3).
- **Khoá nhãn** (`label-key.json`) commit **trước** khi chấm (REVIEWER C2v3 Tập 6 CHÍNH-2).
