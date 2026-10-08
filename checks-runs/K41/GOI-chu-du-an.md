# Gói hỏi chủ dự án — lô K nhóm 1 (K4.1, sửa luật cũ; CHƯA merge)

Phiên K 08/10 (nhánh `claude/phase-k-after-episode-5-frjcpw`). Nhóm 2 đã tự merge `main` theo D-008 §2: **K4.0 → K4.0.1** (LOCK `79aeec0d…`, `main` @ `2c5eacf`). Nhóm 1 dưới đây sửa luật cũ nên chờ anh duyệt. REVIEWER soát: K4.0 **ĐẠT có sửa** (2 CHÍNH đã sửa ở K4.0.1); nhóm 1 **chưa đạt** ở lần soát đầu (3 CHÍNH), đã sửa cả ba; kết quả soát cuối ở cuối tệp.

Trả lời mỗi câu: **Có / Không / Có, nhưng …**.

## Câu 1 — A22: V11 chỉ đếm nét chữ (glyph) đè đồ hoạ; tấm nền của chữ không tính
- **Đổi gì:** chữ được đo bằng nét glyph; đồ hoạ nằm dưới tấm nền (plate/pill) của chính chữ đó không tính là va chạm; chữ–chữ chỉ so nét. Đồ hoạ bị tấm nền che vẫn được **đếm riêng** (`V11.plateOverGraphics`, chỉ báo).
- **Bằng chứng:** selftest trang: chữ không nền bị đường cắt → vẫn trượt; nhãn trục trên trục, chữ đè chữ → vẫn trượt; hai pill giao nhau nhưng nét rời → đạt. Tập 5 C5c dựng lại: V11 cũ **2.612** → mới ****359** (−86 %; 2.462 mẫu đồ hoạ dưới tấm nền chuyển sang số đếm riêng)** (`checks-runs/K41/a22/ep005-V11-before-after.json`; mọi luật trang khác trùng). Còn 359 chưa về 0: 6/8 chữ nằm trên **dải đối trọng hoặc thẻ phương pháp S19 phủ hình 3D** — dải/thẻ không phải tấm nền riêng của chữ; 1 nhãn "75%" S17–S18 (153 px) cần xem tay. Về 0 cần bên dựng ghi dải chrome thành đối tượng `card` rồi lô K sau bỏ hình 3D dưới `card`.
- **Ưu:** đo đúng đè thật; Tập 6 không phải xin ngoại lệ V11 lần nữa; thêm tấm nền (cách chống đè) không còn làm số tăng.
- **Nhược:** ca cũ `V11-badge-on-series` đổi từ TRƯỢT sang ĐẠT: pill ILLUSTRATIVE che một đường dữ liệu không còn là lỗi V11. Nó chỉ hiện ở số đếm riêng `plateOverGraphics`.
- **Tác động:** V11 vẫn là CHÍNH. Công chủ dự án ↓ (bớt một ngoại lệ mỗi tập). Chất lượng = hoặc ↑.
- **Rủi ro:** đường vẽ **trên** tấm nền cũng bị bỏ qua, vì lớp ảnh không mang thứ tự vẽ (điểm mù đã ghi). Thời gian lấy mẫu trang tăng (Tập 5: 42,6 → 59,4 phút, +39 %).
- **Khuyến nghị: Có.** Kèm điều kiện: REVIEWER đọc `plateOverGraphics` ở mỗi C5. Nếu muốn, lô sau nâng nó thành luật riêng.

## Câu 2 — A10 + A16: F11 lấy danh sách phát hành từ nhà máy
- **Đổi gì:** khi nhà máy dựng chính phim này (tổng `build-report` = `timeline` ± 0,5 s), F11 không còn đòi danh sách 28 tệp của pipeline cũ. Nó đòi:
  - lõi: video, phụ đề, mô tả, 3 thumbnail, timeline, script, claims, takes, adbreaks, rights, visual-assets, stem voice/music;
  - mọi stem mà mix đã ghi;
  - camera/sonify/page nếu bước artefacts có chạy;
  - mỗi đoạn thế giới: video + `.build.json` / `.verify.json` / `.log.json` (A16).

  `artefacts.M3` chỉ còn để báo. Bản trích (Tập 3) vẫn chấm theo kiểu K2.
- **Bằng chứng:** selftest 8/8. Xoá một tệp nhà máy thật sinh (sonify-events, `.verify.json`) → trượt; tệp cũ của pipeline khai trong M3 mà thiếu → không trượt. `checks-runs/K41/F11-evidence.md`: Tập 4, Tập 5 chỉ còn thiếu media bị `.gitignore`. **Chưa chạy trên cây C5 có đủ media**, vì không có trong phiên này.
- **Ưu:** bỏ ngoại lệ F11 lặp lại ở Tập 4 (14 tệp "chưa khai" + page.json).
- **Nhược:** danh sách bắt buộc do chính báo cáo của nhà máy quyết. Ba tệp `out/model.json`, `data/sources.json`, `design/tokens.json` rời khỏi F11; S01, S03 vẫn đòi hai tệp đầu.
- **Tác động:** công chủ dự án ↓. Chất lượng = (S01, S03, F12 vẫn canh).
- **Rủi ro:** nhà máy bỏ sót một bước thì F11 cũng không đòi tệp của bước đó.
- **Khuyến nghị: Có**, với điều kiện xác nhận F11 ĐẠT trên cây C5 thật của Tập 6 trước G2. Trượt thì quay lại K2.

## Câu 3 — A9 + A21: rubric câu khuyên tách "video nói" và "người đọc tự suy"
- **Đổi gì:** ba cờ, người chấm phải trích câu của người đọc:
  - `advice_stated`: hình, chữ hoặc lời của video nêu hay ngụ ý một hành động. **Chặn.**
  - `advice_inferred`: người đọc tự suy. **Chỉ báo.**
  - `caution_only`: tự kiểm số, hỏi chuyên gia. **Không tính.**

  Thêm câu phụ *"Did the animation itself suggest this, or is it your own conclusion?"*. `packets.py` đọc được bản chấm cũ, và từ chối cờ không có trích dẫn.
- **Bằng chứng:** `checks-runs/K41/advice/RESULT.md`, một người chấm mù, 16/18 đúng kỳ vọng:
  - đối chứng dương 2/2;
  - thận trọng chung 2/2;
  - N1/N2 Tập 5: cờ cũ chặn 13/14, rubric mới chặn 2/14. Hai ca này người đọc viết "the animation implies extra principal payments".
- **Ưu:** cổng gốc đo cái hình nói, không đo cái người đọc tự kết luận. Bớt vòng sửa hình vô ích (Tập 5 N1/N2: 3 vòng).
- **Nhược:** hiệu chuẩn còn mỏng: một người chấm, 14/19 lượt còn tệp, đối chứng dương là câu viết sẵn (chưa phải hình "Stay put to save"), câu phụ chưa được thử.
- **Tác động:** công chủ dự án ↓ (bớt ngoại lệ khuyên). Gen "không khuyên" vẫn chặn khi video nói.
- **Rủi ro:** người chấm gán nhầm "video nói" (2/14) hoặc ngược lại. Lời khuyên ngầm của hình có thể lọt qua dưới nhãn `inferred`.
- **Khuyến nghị: Có, chạy thử ở C3 Tập 6.** Ở đó chạy cả hai rubric song song, 2 người chấm, thêm đối chứng hình thật. Lệch thì giữ rubric cũ.

---
REVIEWER (soát cuối): {REVIEWER_FINAL}
