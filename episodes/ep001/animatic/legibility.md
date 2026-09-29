# C4 animatic — Kiểm "đọc được ở 25%" (G-014, chữ ký C3)

ANIMATIC C4, 29/09/2026. Luật áp: mọi cỡ chữ giảm ~20% so với style frame C3, **sàn 40 px ở 1080p** (26,7 px ở 720p) — `src/tokens.json`: hero 120 · number 77 · head 58 · caption 51 · label 43 · note/badge 40. Hàm `text()` chỉ nhận 6 bậc này → không chuỗi nào < 40 px (`check-report.json`: `minTextPx1080` = 40 ở cả 20 cảnh; 0 chuỗi ra khỏi vùng an toàn; 0 số ngoài claim).

**Cách kiểm:** mỗi cảnh lấy khung khó nhất (khung có nhiều chữ nhất — thường là khung cuối; S20 lấy khung "+$8,093") từ bản render 1280×720, thu hộp (BOX) về **480×270** (= khung 1080p ở 25%), mở ảnh ở kích thước gốc và tự đọc từng chuỗi (`src/check.py` → `work/25/Sxx.png`, không commit). Ở 25%: chữ hoa của bậc nhỏ nhất (40 px) cao **7,3 px** (C3: 8,7 px với sàn 48) — thấp hơn C3 theo đúng quyết định của chủ dự án.

## Kết quả: 20/20 cảnh đọc được mọi chuỗi mang nghĩa; 5 chỗ trượt/yếu (cấp Chính, có giải thích)

| Cảnh | Đọc ở 480×270 | Ghi chú |
|---|---|---|
| S01 | Đạt | tiêu đề, 5.98%, 7.03%, "window closed", "Closed after the week ending July 23, 2026", "Back above 7%", "first time since January 2025", nhãn tháng, "1 percentage point below Nora's rate". |
| S02 | Đạt, **trượt 1** | câu hứa 3 dòng, "smaller loan / Nora / larger loan / your loan?", "fees $5,124", nguồn. **Trượt:** chữ in trên lá thư (vật 3D, xa máy) — xem (1). |
| S03 | Đạt | "Three in ten had a rate of 7% or more", "30-year home-purchase loans made in 2023", "Nora". |
| S04 | Đạt | "$375,000", "7.62%", "Signed October 2023", dấu "Dollars of the day"; "not adjusted for inflation" (bậc note) đọc được. |
| S05 | Đạt | "29 weeks in 2026 at least 1 point below", "last week: July 23, 2026", "?"/"next?", "History, not a forecast · US only". |
| S06 | Đạt, **trượt 1** | "$221 a month less", "at 7.03% instead of 7.62%"; khung thang lãi: "0.59 point", "1 point = one percentage point". Chữ trên lá thư nhỏ (1). |
| S07 | Đạt | "$5,124", "the median bill: half pay less, half pay more", "Nora's loan size is the median too: $375,000", "your letter?". |
| S08 | Đạt (yếu) | "NO/YES", "0.59", "short of the line", "about 24 months", "the bill: $5,124" (bị gạch — cố ý), "not counted". Yếu: nhãn "+ ?" trong ô nét đứt (bậc label, trong ô nhỏ) — đọc được nhưng sát. |
| S09 | Đạt, **trượt 1** | "$5,124 ÷ $221 a month = 24 months", "balance paid off / since refinancing", "old loan/new loan", "24". Chữ trên lá thư (1). |
| S10 | Đạt | "Break-even: month 30", "not month 24", "loan costs / + still owed", "24" gạch, "30". |
| S11 | Đạt | "Never", "not before the old loan's last payment", "0.25", "division: month 38" (trong strip). |
| S12 | Đạt | "month 18", "well inside 3 years", "3 years". |
| S13 | Đạt, **yếu 1** | "Half a point: paid back in exactly 3 years", "0.5 · Nora's line", "offer 0.59", "her offer (0.59): paid back within 3 years", "The same line for everyone?". **Yếu:** dấu "?" cạnh tam giác Walt nằm sát nhãn "1-point line" (chồng một phần) — xem (2). |
| S14 | Đạt | "Same offer: 7.62% → 7.03%", "Walt · $115,000 loan", "Nora · $375,000 loan", "bill $3,667 / bill $5,124", "only a little smaller bill". |
| S15 | Đạt | "$68 a month, against a $3,667 bill", "Break-even: month 75", "75", "loan costs / + still owed". Khung thanh: "his bill = about 3.2% of his loan". |
| S16 | Đạt | "1.12 points", "0.5 point", "Smaller loan, bigger cut needed", hai hàng "Bill: barely shrinks / Savings: shrink" và số. |
| S17 | Đạt (yếu) | "about a third / of a point"; mốc tham chiếu "1.12", "0.5" (bậc note, màu phụ) đọc được nhưng mờ nhất khung — cố ý là phụ. |
| S18 | Đạt | ba nhãn cột, ba khoản vay, tên, "your loan?", "1-point rule of thumb: fits none", hai dòng giả định (bậc note). |
| S19 | Đạt, **yếu 1** | "$3,443", "$8,270", "half of all bills fall in here", "your rate? / your bill? / your balance?", hai thẻ, "→ different math". **Yếu:** "Nora's $5,124" (note, cam trên dải xanh) — xem (3). |
| S20 | Đạt | "+$8,093 ahead", "if she stays 7 years", "3 years/7 years", tiêu đề. |

## Chỗ trượt / yếu và giải thích (cấp Chính)
1. **Chữ in trên vật 3D** (lá thư ở S02, S06, S07, S09, S18 khi máy lùi xa; nhãn "$3,667"/"$5,514" in trên xấp phí ở khung xa S14/S17): không đọc được ở 25% khi vật nhỏ trong khung. Theo hệ hình C3 (§2, §4.5), đây là chữ trang trí trên vật; mọi con số của vật đều có **bản chữ phẳng** trên màn hình ("fees $5,124", "bill $3,667", "bill $5,514", "New rate: 7.03%"). Khi máy cận vào lá thư (S02, S06, S07, S09, S18 đầu cảnh) chữ trên thư đọc được. Không sửa ở C4.
2. **S13 chồng một phần** dấu "?" của Walt với nhãn "1-point line": cả hai vẫn đọc được; sửa ở C5 (dời cụm Walt/Anjali "?" xuống dưới thước).
3. **S19 "Nora's $5,124"** (40 px, cam trên nền xanh 25%): đọc được nhưng tương phản thấp nhất tập; C5: thêm tấm nền `bg` dưới nhãn.
4. **Chung:** bậc note 40 px ở 25% chỉ còn chữ hoa 7,3 px — đọc được trên ảnh 480×270 nhưng là giới hạn; dòng nguồn (màu `ink-muted`) là chuỗi mờ nhất ở mọi cảnh. Chủ dự án đã chọn sàn này khi ký.
