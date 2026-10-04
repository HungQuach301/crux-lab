# C4 animatic — kiểm đọc được ở 25% (G-014)

Cách đo: với mỗi cảnh lấy **khung nhiều chữ nhất** trong các khung tự kiểm (mỗi khung thứ 6 + mọi khung dải; `check-report.json → hardTime`), thu nhỏ hộp 1280×720 → 480×270 (= 1920×1080 ở 25%). Ảnh: `work/25/Sxx.png`, tờ ghép `work/25/sheet-1..4.png` (không commit; dựng lại bằng `python3 src/check.py`). Chữ nhỏ nhất toàn phim là bậc `note`/`badge` 48 px @1080, tức 12 px ở 25% (chiều cao chữ hoa ≈ 8,7 px); sàn 40 px @1080 không bị chạm.

| Cảnh | Khung khó nhất (s) | Chữ nhỏ nhất @1080 | Đọc ở 480×270 | Ghi chú |
|---|---|---|---|---|
| S01 | 3,4 | 54 (caption 64, number 96) | đọc được | "July 1, 2026" + dòng Grad PLUS |
| S02 | 5,8 | 64 | đọc được | ba dòng chính sách, mỗi lúc một số |
| S03 | 14,9 | 48 (badge) | đọc được | "$50,000 over 10 years", hai khoản trả trên hai thẻ |
| S04 | 18,2 | 48 (năm, badge) | đọc được | năm trục (48) nhỏ nhất nhưng rõ; "US only" 54 |
| S05 | 7,6 | 48 | đọc được | "76.2%" + "went above the fixed rate" (64) |
| S06 | 0 | 48 (badge) | đọc được | chỉ "9% fixed" |
| S07 | 37,8 | 48 (năm) | đọc được | "August 1981" / "−$15,295" |
| S08 | 42,4 | 48 | đọc được | "43% more", "Starting April 1977"; "$26,005" là `label` 54 |
| S09 | 22 | 54 | đọc được | nhãn núm và cột 54 |
| S10 | 0 | 54 | đọc được | như S09 |
| S11 | 3 (lúc lộ dần) / thẻ đủ: `strips/S11-card-25pct.png` | 64 | **đọc được** | xem dưới |
| S12 | 0 | 54 | đọc được | năm nhãn quanh thẻ trống (54, `ink-muted` 7,5:1) |
| S13 | — | không có chữ | — | |

Chỗ yếu (không trượt): năm trục 1954/1981/"today" (48 px, `ink-muted`) là chữ nhỏ nhất; ở 25% vẫn đọc, nhưng mờ hơn số chính. Huy hiệu ILLUSTRATIVE 48 px đọc được.

## Thẻ phương pháp S11 (đo riêng)
- Nội dung: 1 tiêu đề + 8 dòng (`src/method_card.json`): T-bill thay chỉ số của bên cho vay · chỉ số hôm nay 3.72% · biên 3.78 points · Leah bắt đầu 7.5% so với 9% cố định · 753 tháng bắt đầu chồng nhau, không độc lập · January 1954 đến September 2016, mỗi lần 10 năm · chỉ số không dưới 0 · không ân hạn / phí / trần · US only · history, not a forecast. Mọi số qua claim (`index_today`, `margin`, `var_start`, `fixed_rate`, `n_starts`, `first_start`, `last_start`, `term`).
- Cỡ chữ: dòng 64 px @1080 (`caption`), tiêu đề 72 px (`head`) → ở 25%: 16 / 18 px, chiều cao chữ hoa 11,6 / 13,1 px. Ảnh `strips/S11-card-25pct.png` (480×270): cả 9 dòng đọc được, không vỡ nét. Tương phản 17,2:1 (`ink` trên `bg`), tiêu đề `ink-muted` 7,5:1. Không chữ nào ngoài vùng an toàn (kiểm máy).
- Thời gian hiện: 60 từ → cần ≥ 20,0 s. Thẻ lộ từng dòng (0,3 s/dòng) rồi đứng yên; **hiện đủ 21,0 s** (cảnh 24,0 s: lời 8,4 s + nghỉ, theo luật "kéo dài bằng nghỉ, không đổi lời"). `check-report.json → methodCard`.
