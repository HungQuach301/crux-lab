# H2 — "Hồ sơ và bằng chứng" · ý đồ từng khung (viết TRƯỚC khi render)

DESIGNER H2, 29/09/2026. Hướng này lấy G-012b ("screenshot bài báo và bằng chứng tăng độ tin cậy") làm gốc, nhưng chỉ dùng loại bằng chứng an toàn về quyền (tài liệu liên bang public domain và thẻ trích dẫn dựng lại; xem `rights-options.md`).

**Ý tưởng hướng.** Cả tập là một mặt bàn làm việc nhìn từ trên xuống, hơi nghiêng: giấy tờ thật của một khoản vay (bản in dữ liệu lãi tuần, hồ sơ vay, Closing Disclosure, sổ ghi) nằm trên bàn; camera 2.5D trượt và dừng trên giấy. Bút dạ quang và bút đỏ đánh dấu đúng con số lời đang nói; con số đó **nhấc ra khỏi giấy** thành một biểu đồ đơn giản (cột, vạch) đặt ngay trên bàn. Nghĩa đến từ chuyển động: cái gì được khoanh, cái gì bị gạch, cái gì chen vào đẩy tổng đi.

Quy ước chung cho cả ba khung:
- Màu chỉ lấy từ token kênh. Giấy = `ink` #F2F4F7, chữ in trên giấy = `bg` #0E1116 / `grid` #2A303B; bàn = `bg`/`surface`. Bút lãi suất = `accent` (xanh dương, như đường lãi). Nora = `positive` (tròn), Walt = `warn` (tam giác), Anjali = `negative` (vuông). Bút đỏ `negative` chỉ dùng cho "gạch/ẩn" ở khung không có Anjali.
- Mọi số trên màn hình là một claim (ID ghi trong bảng dưới). Số không phải claim (các tuần khác trong bản in) bị **làm mờ theo độ sâu** (ngoài vùng nét), không đọc được — cố ý.
- Số của nhân vật có con dấu **ILLUSTRATIVE** ngay cạnh, hiện cùng lúc với số. Tiền ghi "nominal $" trên từng tờ.
- Nguồn in ở chân mỗi tờ ("Source: Freddie Mac via FRED", "Source: CFPB HMDA 2025").

## F1 · Cold open: cửa sổ lỡ (~9 s)

**Người xem tắt tiếng phải hiểu:** lãi đã có một đoạn xuống thấp; một người (Nora) lẽ ra bớt được một khoản mỗi tháng nếu vay lại lúc đó; đoạn thấp đã qua, khoản đó không còn.

Chuyển động:
1. Bản in "30-year fixed rate, weekly average" nằm trên bàn; đường lãi được "in" dần từ trái sang phải, đi xuống.
2. Chạm đáy: bút xanh khoanh điểm đáy và dòng "5.98% · week ending February 26, 2026 · lowest since September 2022". Đoạn đáy được tô dạ quang xanh lá (màu Nora) — "khoảng lãi thấp".
3. Camera trượt sang hồ sơ của Nora (kẹp giấy, dấu ILLUSTRATIVE): "Oct 2023 · 7.62%". Một mảnh giấy ghim trên hồ sơ: "Refinance at the February low: −$459 / month" (dạ quang xanh lá).
4. Camera lùi lại: đường lãi in tiếp, leo lên qua vạch đứt "7%", dừng ở "7.03% · week ending September 24, 2026 · first time above 7% since January 2025". Vùng dạ quang ở đáy đã ở phía sau.
5. Bút đỏ gạch ngang mảnh giấy "$459 / month". Giữ hình.

Claim: `low2026` 5.98%, `low2026_date`, `low2026_since`, `oct2023`, `r_old` 7.62%, `sav_low2026_median` $459 (ILL.), `seven` 7, `r_today` 7.03%, `anchor_date`, `first7_since`.

Kiểm mù đạt nếu người xem nói được: "rates dipped to a low, someone could have saved ~$459/month, rates went back up and the chance is gone (crossed out)".

## F2 · Điểm hoà vốn dời 24 → 30 tháng (~10 s)

**Người xem tắt tiếng phải hiểu:** có một hoá đơn phí; tiền tiết kiệm hằng tháng cộng dồn để lấp nó; một khoản ẩn (dư nợ cao hơn) chen vào làm hoá đơn cao lên, nên ngày lấp đầy trễ từ tháng 24 sang tháng 30.

Chuyển động:
1. Camera trên trang Closing Disclosure (dựng lại theo bố cục mẫu CFPB, số của Nora): mục "D. TOTAL LOAN COSTS" — bút dạ quang quét qua "$5,124". Thẻ trích dẫn dựng lại (CFPB, public domain) nằm cạnh: "A Closing Disclosure is a five-page form that provides final details about the mortgage loan you have selected."
2. Con số $5,124 nhấc khỏi giấy, trở thành một vạch ngang "bill" trên tờ giấy kẻ ô bên cạnh (cột rỗng có vạch $5,124).
3. Sổ ghi bên trái: mỗi tháng một dòng "+ $221" được viết thêm; mỗi dòng đổ một khối xanh lá vào cột. Bộ đếm tháng chạy; cột chạm vạch ở tháng 24 → khoanh "24".
4. Một mẩu giấy đỏ "balance +$1,133" trượt vào, **chen giữa** các dòng sổ; vạch bill bị đẩy lên thêm một đoạn gạch sọc đỏ; chữ "24" bị gạch.
5. Sổ tiếp tục thêm dòng "+ $221", cột lên tiếp, chạm vạch mới ở tháng 30 → khoanh "30". Giữ hình.

Claim: `cost_median` $5,124, `sav_median` $221 (ILL.), `be_simple_median` 24 (ILL.), `gap24` $1,133 (ILL.), `be_bal_median` 30 (ILL.). Chiều cao cột tỉ lệ với tiền (đáy 0 có vạch); phần dư nợ tăng dần theo tháng (tháng 24 = $1,133; tới tháng 30 cột 30 × $221 chạm đúng vạch — quy ước dựng, không phải một claim mới).

Kiểm mù đạt nếu người xem nói được: "monthly savings add up to cover the fee; a hidden extra ($1,133 balance) pushes the payback from month 24 to month 30".

## F3 · Walt và Anjali (~9 s)

**Người xem tắt tiếng phải hiểu:** hai hồ sơ vay chênh nhau rất xa về số tiền vay, nhưng phí gần như bằng nhau; tiết kiệm mỗi tháng thì chênh theo khoản vay → khoản nhỏ cần giảm lãi nhiều hơn nhiều.

Chuyển động:
1. Hai hồ sơ đặt cạnh nhau trên bàn: Walt (tam giác vàng, trái) và Anjali (vuông đỏ, phải), cùng một mẫu hồ sơ, dấu ILLUSTRATIVE.
2. Camera trượt xuống từng dòng, ba nhịp; mỗi nhịp bút dạ quang quét dòng tương ứng ở cả hai hồ sơ, rồi số được rút ra thành cặp cột trên dải giấy phía dưới (mỗi dòng một thang riêng, có đáy 0):
   - "Loan": $115,000 vs $655,000 → cột chênh gần 6 lần.
   - "Loan costs": $3,667 vs $5,514 → hai cột **gần bằng** (chữ "about the same").
   - "Saves per month": $68 vs $387 → cột chênh xa.
3. Kết: một thước dọc "rate cut needed to get the fees back within 36 months": dấu tam giác ở 1.12, dấu vuông ở 0.32 ("about a third of a point"). Giữ hình.

Claim: `loan_small` $115,000, `cost_small` $3,667, `sav_small` $68, `cut36_small` 1.12, `loan_large` $655,000, `cost_large` $5,514, `sav_large` $387, `cut36_large` 0.32 / `cut36_large_words`, `hold36` 36 (ILL.).

Kiểm mù đạt nếu người xem nói được: "loans very different, fees about the same, monthly savings very different, so the small loan needs a much bigger rate cut (1.12 vs ~0.32)".

## Không làm
- Không chụp màn hình bài báo thật; không logo, không tên báo thật. Nếu minh hoạ loại (3), dùng bài báo giả ghi rõ MOCKUP (không có trong 3 khung).
- Không dùng biểu mẫu thật có dữ liệu người thật; Closing Disclosure là bản dựng lại theo bố cục mẫu công khai của CFPB, số là của Nora (ILLUSTRATIVE, trừ phí là trung vị HMDA).
