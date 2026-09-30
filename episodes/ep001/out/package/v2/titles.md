# Tập 1 · Gói phát hành v2: tiêu đề, thumbnail, 2 dòng đầu mô tả (PACKAGING, 30/09/2026)

Yêu cầu chủ dự án: gói hiện tại đạt kỹ thuật nhưng chưa có sức hút. Tệp này chỉ đưa **phương án**; chủ dự án chọn phần gu. Mọi con số lấy từ `out/claims.json` (`display`). Không câu nào khuyên hay dự báo: đã quét bằng các regex ADVICE/FORECAST/FOUR/WE_BAD của S10 (`checks/py/r_content.py`, chỉ import, không sửa): 0 khớp. Số ký tự đếm bằng `len()` của Python (dấu cách và dấu câu đều tính).

Gói hiện hành (đối chứng): **T1** "How Big a Rate Cut Makes a Refinance Worth It?" (46 ký tự) + `../thumb-3.png`.

## 1. Tiêu đề: 6 phương án, 3 hướng móc (≤ 60 ký tự)

| # | Hướng | Tiêu đề | Ký tự | Claim dùng | Thumbnail đi kèm |
|---|---|---|---|---|---|
| a1 | (a) nghịch lý | Why a Smaller Loan Needs a Bigger Rate Cut to Be Worth It | 57 | `cut36_small` 1.12 > `cut36_median` 0.5 > `cut36_large` 0.32 (theo `loan_small` < `loan_median` < `loan_large`); "worth it" = phí về trong 3 năm (`hold36`, giả định ghi trong mô tả) | H |
| a2 | (a) nghịch lý | Same Rate Cut, Opposite Results for a Small and Big Mortgage | 60 | cùng đề nghị `r_old` 7.62% → `r_today` 7.03% (`cut_today` 0.59); sau 3 năm Walt thiếu `net36_small` $1,777, Anjali dư `net36_large` $5,250 | H |
| b1 | (b) chi phí ẩn | The Refinance Cost That Isn't in the Fees | 41 | `gap24` $1,133: dư nợ khoản mới cao hơn khoản cũ ở tháng 24 (S10.5–S10.6: "would come out of her sale money"); không in số | L |
| b2 | (b) chi phí ẩn | Refinance Break-Even: The $1,133 That Simple Division Misses | 60 | `gap24` $1,133 (Nora, ILLUSTRATIVE) ở đúng tháng 24 = `be_simple_median`; đếm cả nó thì hoà vốn tháng 30 (`be_bal_median`) | L |
| c1 | (c) "người như tôi" | Got a 2023 Mortgage? The 1-Point Rule May Not Fit Your Loan | 59 | `oct2023`; S18.9 "The one-point line fits none of them" (`s10` = 1 điểm; 1.12 / 0.5 / 0.32) | W |
| c2 | (c) "người như tôi" | Borrowed Over 7% in 2023? The Rate Cut a Refinance Needs | 56 | `r_old` 7.62% (trung bình tháng 10/2023), `ge7_threshold`, `purch23_words` (3/10 khoản mua nhà 2023 ≥ 7%) | W |

**Ghi chú về chữ (không tự đổi ý chủ dự án, chỉ đề xuất):**
- **"luật 1%" → "1-Point Rule".** Chủ dự án viết "luật 1%". Người Mỹ hay gọi là "the 1% rule", nhưng phim định nghĩa là *một điểm phần trăm* (S06.4 "when we say a point, we mean exactly that: one percentage point off the rate"). "1%" có thể bị đọc là giảm 1% tương đối (7.62% → 7.54%). Hai tiêu đề (c) dùng "1-Point"; nếu chủ dự án muốn móc từ khoá tìm kiếm "1% rule", nên để trong tags và mô tả, không trong tiêu đề.
- **"May Not Fit Your Loan"** thay vì "doesn't fit your loan": phim chỉ chứng minh luật một điểm không khớp **ba khoản vay minh hoạ**; với khoản vay của người xem, nó *có thể* không khớp. Khẳng định chắc chắn sẽ vượt claim.
- **b2 chứa $1,133 là số của nhân vật minh hoạ** (Nora, trung vị, tháng 24). Tiêu đề không mang huy hiệu ILLUSTRATIVE được. Chữ "Simple Division" giữ số gắn với phép tính của phim (không nói "your"), mô tả nói rõ nhân vật minh hoạ. b1 an toàn hơn vì không in số.
- **a2 "Opposite Results"**: đúng theo phép thử 3 năm (một người thiếu, một người dư). Với thời gian ở lại khác (7 năm), Walt cũng dư `net84_small` $386, nên "opposite" chỉ đúng trong phép thử 3 năm của phim.
- Không tiêu đề nào dùng "most calculators", "banks hide", "nobody tells you": chưa có nguồn.

## 2. Thumbnail: 3 concept, tài sản 3D H1 (1280×720)

Dựng bằng chính engine C3 đã ký (`design/c3/final/src/engine.js`: token, `house()`, `woodTable()`, `owedTex()`, three.js/SwiftShader), still 1920×1080 không chữ, rồi ghép chữ phẳng Inter ở 1280×720 (`preprod/thumbs_v2/render.js`). Hộp chữ đo trong trang, ghi ở `thumb-*.json`. Tự kiểm: `preprod/thumbs_v2/selfcheck.py` → `selfcheck.json`, `legibility-25.png` (ảnh 25% và 10%, 1:1).

| File | Hướng | Hình | Chữ (≤ 4 từ) | Claim | Cỡ chữ | Tương phản ở 10% (min) | Tỉ lệ màu token |
|---|---|---|---|---|---|---|---|
| `thumb-H.png` | (a) | Hai nhà cùng phố, thể tích theo khoản vay ($115,000 vs $655,000, như SF2/SF5); nhà nhỏ cần cắt nhiều hơn | "−1.12 pts" · "−0.32 pts" (+ huy hiệu ILLUSTRATIVE) | `cut36_small`, `cut36_large` | 104 px (huy hiệu 34 px) | 3.92 (huy hiệu); số 7.99–10.11 | 93.7% |
| `thumb-L.png` | (b) | Lá thư refinance (SF2) trên bàn bếp; từ dưới thư trượt ra tấm sọc "vẫn còn nợ" (SF3) | "$5,124" · "+$1,133" (+ huy hiệu) | `cost_median`, `gap24` | 108 / 110 px (huy hiệu 34 px) | 3.84 (huy hiệu); số 8.04–12.81 | 45.0% |
| `thumb-W.png` | (c) | Cửa sổ thật trên tường bếp; nhìn qua kính là đường lãi tuần (SF1: vùng "cửa sổ" tô accent chỉ ở các tuần ≥ 1 điểm dưới 7.62%), chấm đáy 5.98%; cánh chớp bên phải đã khép che các tuần sau 23/7/2026 | "5.98%" · "Missed it?" | `low2026` | 150 / 100 px | 10.28 | 87.7% |

Ở 25% (320×180) đọc được mọi chữ của cả ba, kể cả huy hiệu (8.5 px); ở 10% (128×72) đọc được các số, huy hiệu thành vệt vàng.

**Căng thẳng cần chủ dự án quyết (báo, không tự quyết):**
1. **−0.33% của chủ dự án không khớp claim.** `cut36_large` hiển thị **0.32** (phim nói "about a third of a point", `cut36_large_words`). 0.33 không có trong claims. Đã in **"−0.32 pts"**. Phương án khác: "−⅓ pt" (khớp lời phim nhưng bỏ chữ "about").
2. **"−1.12%" dễ đọc sai** thành giảm 1.12% tương đối (7.62% × 0.9888). Đúng là giảm 1.12 **điểm phần trăm**. Đã in "−1.12 pts". Nếu chủ dự án muốn dấu %, dạng đúng mà ngắn là "−1.12 pts" hoặc "7.62% → 6.50%" (6.50% không phải claim, cần DATA thêm claim).
3. **ILLUSTRATIVE (S08) và P01 kéo hai hướng.** Số của Walt/Anjali/Nora (1.12, 0.32, $1,133) là số nhân vật minh hoạ, nên theo tinh thần S08 cần huy hiệu. Huy hiệu 34 px < 90 px (P01, cấp THAM KHẢO, sẽ báo). Chữ cũng thành 5 "từ" nếu đếm huy hiệu. Bản C5 né bằng cách không in số (thumb-2). Đề xuất: giữ huy hiệu (đúng sự thật trước, luật đếm sau) và ghi P01 là ngoại lệ có lý do. Hoặc bỏ số khỏi H (chỉ hai nhà + "Why?") nếu chủ dự án muốn sạch P01.
4. **Tỉ lệ màu token ≥ 97% (P01) không hợp với ảnh 3D H1.** Gỗ, tường nhà, cỏ là vật liệu đã ký trong `design/c3/final/tokens.json → materials`, nhưng không có trong `design/tokens.json`, nên L chỉ đạt 45%. Chữ và mảng phẳng đều dùng màu token. Đề xuất cho Tập 2: đo tỉ lệ token **trên chữ và mảng phẳng**, không đo trên cả ảnh (xem `playbook/packaging.md`).
5. **"Cửa sổ đang đóng" → dữ liệu nói "đã đóng".** Tuần cuối có mức giảm ≥ 1 điểm là 23/7/2026 (`cut1_last_2026`). Hình W: cánh chớp phải đã khép che các tuần sau đó, cánh trái còn mở như hình ảnh của khoảnh khắc. Chữ "Missed it?" là câu hỏi, không khẳng định còn kịp (không dự báo). W không in số nhân vật nên không cần huy hiệu; ngưỡng cửa sổ dùng 7.62% (trung bình tháng 10/2023, số thật).
6. Chữ trên H lặp chiều của tiêu đề a1 ("smaller … bigger") nhưng không lặp chữ; L và W bổ sung số, không lặp tiêu đề.

## 3. Mô tả: hai dòng đầu (~150 ký tự, nói với người đang có lời mời refinance)

| # | Hai dòng đầu | Ký tự |
|---|---|---|
| **DA** | Got a refinance offer? Here is how big a rate cut it takes to earn back the fees within 3 years, and why the answer depends on your loan size. | 142 |
| **DB** | Holding a refinance offer on a 2023 mortgage? We find the rate cut that pays back the fees in 3 years, for small, typical and large loans. | 138 |

Cả hai chứa "refinance", lời hứa có đáp án (mức giảm lãi), điều kiện "within 3 years" (giả định `hold36`, nói lại ở mục giả định của mô tả). DA hợp với hướng (a)/(b); DB hợp với hướng (c). Bản đầy đủ: `description.md` (DA ở đầu, phần thân giữ bản đã duyệt D1, thêm link FHFA).

## 4. So cặp mù (THAM KHẢO)

Vật liệu ở `episodes/ep001/review-c6/pack-test/` (P2 chạy agent mù): 42 ảnh gói (7 gói × mọi cặp × 2 thứ tự) + 6 ảnh chỉ thumbnail (H/L/W cùng tiêu đề T1), tên hex ngẫu nhiên, `prompt.txt`, khoá `key.json`. Thẻ kết quả tìm kiếm của từng gói: `cards/card-*.png` (để chủ dự án xem, không đưa cho agent mù).
