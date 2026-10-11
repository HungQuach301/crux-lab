# REVIEWER G2 — Tập 6 (headless chỉ đọc, khoá Console, `c5/briefs/REVIEW-G2.md`) · 2026-10-10

Kết luận: ĐẠT có sửa

## 1. Số trong G2.md so với nguồn
- Checks `run-c5c` khớp: Tập ĐẠT, CHẶN 36/36, CHÍNH 12/13 (V11 32 mẫu), F11 46/0, plateOverGraphics 2.518.
- Âm thanh khớp: 536,6 s, −14,0 LUFS, −1,8 dBTP. qc có 6 TRƯỢT: 4 đối trọng, freezedetect, loudness.
- Shorts khớp: 38,6 / 18,8 / 20,9 s, chữ ≥ 56 px, SH01–05 ĐẠT.
- Chương mô tả khớp `timeline.json`. MR1 = 208,15 s, nằm trong khoảng lặng 1,51 s (207,42–208,93 s).
- Cổng gốc 20/23 = 87 % đúng: B01, B15, B04 trượt. Nhưng `ROOT-SUMMARY-P3c.md` và `PLAN.md` §1 vẫn ghi 21/23 và "C5c đang dựng" → lệch §7 mục 5.
- Đồng bộ: `c5/sync` cho 88/118 ±0,2 s, p90 lớn nhất 0,217 s. Checks R07 trên master chỉ 83/118 = 70,3 % (ngưỡng 92 %). Gói không nêu số này.
- Chi API ≈ $23,5 cộng khớp: 21,68 + ≈1,8.
- Giờ máy 14,5 h (1080p 6,8 h) không có nguồn trong repo. PLAN §5 ghi P3c ≈ 3,9 h.
- **Tệp xem G2 chưa có.** `review-g2/` chỉ có `full-720p.mp4`, `.sha256` và `highlights.mp4`. Thiếu `short-SH*.mp4`, `thumb-*.png`, `before|after-B01/B15.png`, `SHA256SUMS-review`. Nguồn có đủ, nên `review_copies.sh` dừng ở dòng 25.

## 2. V11.plateOverGraphics (§7 mục 7)
- Giá trị 2.518 (run-c5b 2.550). Có 20 ví dụ, tổng 607 mẫu. G2 chỉ nêu số, **thiếu ví dụ** → trượt §7 mục 7.
- Ví dụ lớn: S12 "first check" 1.324 px × 117 mẫu; S13 "Ruth" 338 px × 14; S15 "none since" 269 px × 21; S03 "first check" 252 px × 62. Các nhãn 1966/1986 ở S14–S16 chỉ 10–12 px.
- Xem dải B15: "none since" và "first check" đặt trên đúng vạch/dải chúng gọi tên. Tấm nền che mép trên dải cảnh báo và vài đỉnh cột gần 1949. Không thấy chữ số hay dữ liệu nào bị che hẳn.
- Nghi vấn: B15 trượt vì người đọc "misses warn region". Tấm "none since" che đúng mép dải đó. Đáng nêu trong gói.
- Tôi không xem được khung S12/S13 (lệnh ffmpeg bị từ chối), nên hai ví dụ này chưa kiểm bằng mắt.

## 3. Ngoại lệ V11 S04: lập luận khoá nghĩa không đứng
- Có tấm nền (root-c5b): B04 0,5·0,5.
- Không tấm nền: vòng 4 1·1, đối chứng 1·0,5, **root-c5c 0,5·0,5·0,5**.
- Ở root-c5c, chính bản giữ lại cũng bị chê "misses the greyed gap" (R01, R02). Đó là lời chê từng dùng để kết tội tấm nền.
- Vậy chưa đo được tác hại của tấm nền. Cả hai bản cùng 0,5, n nhỏ. Theo D-009 (a), không có lý do đo được để bỏ bản sửa.
- G2 và `explanations.json` chỉ dẫn "1·1 → 0,5·0,5". Phải nêu đủ 3 bộ số, và để anh chọn giữa "sửa (V11 = 0)" và "chấp nhận" như hai phương án ngang nhau.

## 4. Mô tả
- Chương: 6 chương, đầu 0:00, chương ngắn nhất 31 s. ĐẠT.
- Số: mọi số có claim (715, 17, 80.7 %, 655, 2.9 %, 19.2 %, các tháng). Không khuyên, có "Not advice." "We" chỉ kênh, không chỉ người xem. Chính tả ổn.
- **Thiếu cam kết REVIEW-G1 #8.** "Starting months January 1947 to August 2006: 715" ngầm là 716 tháng. Tháng 10/2005 bị bỏ vì CPI 10/2025 trống, mà mô tả không nói.

## 5. Thumbnail
- Mọi chữ có claim. "+48.6%" = `two_pct_growth_20y_pct`. thumb-3 "17 of 715" có claim.
- thumb-1 và thumb-2 có ILLUSTRATIVE (có Ruth); thumb-3 không có Ruth nên không cần. Cả ba có "US only · history, not a forecast".
- Không số tiền, không "total", không khuyên. ĐẠT.
- Hồi quy nhỏ so với run-c5b (THAM KHẢO): P01 token share 100 → 98,7 %; số chữ < 90 px 4 → 5.

## 6. advice_stated
- Bằng 0 ở cả 18 lượt (root-c5b 8, đối chứng 4, root-c5c 6). Mọi câu `advice_inferred` đều do người đọc tự nhận là kết luận riêng.
- Câu sát biên: root-c5c R01 (B04) "The animation only suggested the general idea of that trade-off". Câu này nói về sự đánh đổi, không nói hành động, nên chấp nhận được. Nên trích trong gói.

## 7. Gói bỏ sót
- Không có CHẶN ẩn.
- Luật REG báo "first version: nothing to compare", tức không so với run-c5b. So tay: chỉ V11 (0 → 32) và P01 đổi.
- Cam kết C3/G1 "C5 ≥ 8:00 và mid-roll hợp lệ" đã giữ: 8:56,6; MR1 cách đầu và cuối > 2 phút, lặng 1,51 s.
- freezedetect đè lời 206 s / 51 đoạn. Gói chỉ ghi "giống Tập 5", không nêu số.
- Phụ đề và lời vẫn nói "every starting month … January 1947 to August 2006".

## Sửa (cũ → mới)
1. "B04 tụt từ 1·1 xuống 0,5·0,5 → giữ hình C4. Cần anh chấp nhận ngoại lệ." → "Có tấm nền 0,5·0,5 (n = 2). Không tấm nền 1·1, 1·0,5, rồi 0,5·0,5·0,5 ở C5c. Chưa đo được tác hại. Anh chọn: sửa (V11 = 0) hoặc chấp nhận."
2. "V11.plateOverGraphics 2.518 (chỉ báo)." → "2.518 (C5b 2.550); ví dụ: S12 'first check' 1.324 px × 117; S13 'Ruth' 338 × 14; S15 'none since' 269 × 21 (đè mép dải cảnh báo B15)."
3. "cue hình 88/118 trong ±0,2 s" → "88/118 theo sync_audit từng đoạn; 83/118 = 70,3 % theo checks R07 trên master (THAM KHẢO, ngưỡng 92 %)."
4. "Giờ máy ≈ 14,5 h …" → ghi nguồn đo (log hoặc commit), hoặc sửa PLAN §5 cho khớp (hiện ≈ 3,9 h).
5. Danh sách tệp xem → chạy lại `c5/review_copies.sh` cho đủ Shorts, thumb, dải trước/sau và `SHA256SUMS-review` trước khi gửi.
6. Mô tả, "Starting months January 1947 to August 2006: 715 stretches" → thêm "One start month (October 2005) is skipped because October 2025 CPI is blank in the source."
7. "freezedetect" → "freezedetect: 206 s đứng yên ≥ 3 s đè lời (51 đoạn)".
8. `ROOT-SUMMARY-P3c.md` 21/23 và PLAN §1/§4 "đang dựng" → cập nhật 20/23, C5c xong, cho khớp G2.
