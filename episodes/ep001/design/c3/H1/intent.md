# H1 — "Vật thể thật": ý đồ từng khung (viết trước khi render)

Hướng H1 dựng **vật thể thật** bằng three.js, render trên CPU (Chromium headless, WebGL phần mềm SwiftShader). Mỗi vật thể **mang một số liệu**: chiều cao chồng giấy tỉ lệ với đô la, vị trí kim trên thước lãi đúng giá trị lãi, thể tích căn nhà tỉ lệ khoản vay. Không có ẩn dụ trừu tượng (bể nước, khối đá). Chữ quan trọng vẽ phẳng trong không gian màn hình (neo theo vị trí vật thể) để luôn sắc; chữ in trên giấy là phụ.

Thang đo chung: trong một khung, mọi chồng giấy dùng **một** thang đô la/chiều cao. Nhãn ILLUSTRATIVE luôn hiện cùng số của nhân vật; tiền danh nghĩa (nhãn "nominal $").

## F1 · Cold open: cửa sổ lỡ (~9 s)
**Người xem tắt tiếng phải hiểu:** lãi vay giảm xuống thấp một lúc; khi đó Nora có thể trả ít hơn $459 mỗi tháng; lãi đã lên lại, khoản đó không còn.

- Ngôi nhà của Nora ban đêm, đèn cửa sổ sáng. Trước nhà một **biển lãi** kiểu bảng giá ngân hàng: thước dọc 5%–8% có kim trượt, ô số và ô ngày. Một vạch đồng cố định "Nora's loan 7.62%" (ILLUSTRATIVE, tháng 10/2023).
- Kim trượt xuống; ô ngày "Feb 26, 2026", ô số "5.98%" và "lowest since Sept 2022". Khoảng giữa kim và vạch 7.62% sáng xanh (khoảng lãi thấp).
- Cùng lúc một **tấm séc "$459 / month"** bay lên từ hộp thư của Nora và lơ lửng sáng.
- Kim leo lại qua vạch đỏ 7%; ô số "7.03%", ô ngày "week ending Sep 24, 2026", "above 7% — first time since Jan 2025". Khoảng xanh tắt; tấm séc xám đi và rơi lại vào hộp thư.
- Giữa các mốc có claim, kim chỉ di chuyển (không hiện số trung gian) — đường đi giữa các mốc là nội suy, không phải dữ liệu tuần.
- Claim: `low2026`, `low2026_date`, `low2026_since`, `oct2023`, `r_old`, `sav_low2026_median`, `r_today`, `anchor_date`, `seven`, `first7_since`.

## F2 · Hoà vốn dời 24 → 30 tháng (~10 s)
**Người xem tắt tiếng phải hiểu:** một hoá đơn phí là một chồng giấy; mỗi tháng một tờ tiết kiệm $221 chồng lên cột bên cạnh; ở tháng 24 cột tưởng bằng hoá đơn, nhưng một phần nợ ẩn ($1,133) lộ ra làm hoá đơn cao thêm → cột phải lên tiếp tới tháng 30 mới bằng.

- Mặt bàn gỗ. Trái: chồng hoá đơn "Loan costs $5,124" (cao đúng 5,124/221 ≈ 23.2 tờ). Phải: cột trống. Sau lưng: lịch để bàn đếm tháng.
- Tháng 1→24: mỗi tháng một tờ "$221 saved" rơi vào cột. Ở 24 cột ngang hoá đơn; nhãn "$5,124 ÷ $221 = 24 months?".
- Một tờ đỏ "+$1,133 more owed at month 24" trượt vào dưới chồng hoá đơn, nâng nó lên; nhãn phép chia gạch đi.
- Tháng 25→30: phần đỏ vẫn dày thêm chút ít (dư nợ còn chênh), cột xanh thêm 6 tờ; ở tháng 30 hai cột bằng nhau → "Break-even: month 30".
- Claim: `cost_median`, `sav_median`, `be_simple_median`, `gap24`, `be_bal_median`. Độ dày phần đỏ sau tháng 24 là nội suy hình ảnh (chỉ số $1,133 ở tháng 24 là claim).

## F3 · Walt và Anjali (~9 s)
**Người xem tắt tiếng phải hiểu:** hai căn nhà chênh nhau nhiều (khoản vay $115,000 vs $655,000), nhưng hai chồng phí gần bằng nhau; tiền tiết kiệm mỗi tháng thì chênh theo khoản vay → sau 3 năm cột của Walt vẫn chưa lấp phí, của Anjali đã vượt xa → khoản nhỏ cần giảm lãi nhiều hơn (1.12 điểm vs ~1/3 điểm).

- Hai căn nhà cạnh nhau, **thể tích tỉ lệ khoản vay** (655/115 ≈ 5.7×). Trước mỗi nhà một chồng phí ($3,667 / $5,514) cùng thang.
- Bộ đếm tháng chạy 0→36; tờ tiết kiệm $68 (mỏng) và $387 (dày) rơi mỗi tháng vào cột của từng người. Cột Anjali vượt phí sớm; cột Walt tới tháng 36 vẫn thấp hơn phí.
- Kết: thẻ treo trên mỗi nhà "rate cut needed to break even in 3 years: 1.12 points" / "about 1/3 of a point".
- Claim: `loan_small`, `cost_small`, `sav_small`, `cut36_small`, `loan_large`, `cost_large`, `sav_large`, `cut36_large_words`, `hold36`/`y3`. Cột tiết kiệm = cộng đơn giản; không ghi số thiếu/dư.
