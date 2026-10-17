# Thị trường R2 — ba hướng series mới cho kênh Money Rerouted (17/10/2026)

**Phạm vi.** Đề xuất series/loại nội dung mới trên **cùng kênh** (khán giả tài chính cá nhân Mỹ). Máy không chọn — chủ dự án quyết (D-004). Nguồn: `market/REPORT.md`, `market/CHANNELS.md`, `market/topics/`, `audience/R1-PUBLIC.md` (nhánh `audience-r1`), cộng **38 cụm tìm kiếm mới** đo hôm nay qua YouTube Data API (`toolkit/market/mcommon.py`, không sửa toolkit). Số tổng hợp: `market/r2/demand.json` (từng cụm), `market/r2/scores.json` (điểm). Số từng video/kênh khác ở `~/market-cache/2026-10-17/r2/`, ngoài git (III.E.4). Mọi chỉ số là **tự tính, không phải chỉ số YouTube**.

**Cách đo cầu.** Mỗi cụm: 1 search (relevance, US, tiếng Anh, mọi thời lượng, 50 kết quả) + `videos.list`. Chỉ số chính: **trung vị lượt xem/ngày của 10 video đầu** (lượt xem trọn đời / tuổi). Phụ: tỉ lệ video < 1 năm trong top 20 (**độ mới**: cao = thuật toán đang đẩy video mới, kênh mới có cửa); số kênh trong `CHANNELS.md` lọt top 20; mức tập trung (một kênh chiếm bao nhiêu cụm); lượt xem/ngày trung vị của Short. Chi: **3.838 đơn vị, 38 search, 0 lệnh AI, 0 USD**.

**Bối cảnh kênh** (chủ dự án, Studio 15 ngày): CTR 1,02 % — **đề xuất 0,42 %, tìm kiếm 6,19 %**. Kênh đang sống bằng tìm kiếm, nên cụm từ tìm kiếm rõ là điều kiện cần. Video tốt nhất: PMI 10 % (12,3 lượt xem/ngày). Short kéo lượt xem/ngày ngang video dài (R1 §3).

## 1. Tóm tắt

| Hạng | Hướng | Cầu (trung vị các cụm, top 10, xem/ngày) | Độ mới top 20 | Kênh `CHANNELS.md` trong top 20 | Short (xem/ngày) | Định dạng đề xuất |
|---|---|---|---|---|---|---|
| **1** | **B. "Paid in Hours" — giá đời sống qua 60 năm, đo bằng giờ công** | **130** (cụm mạnh: 2.302 · 1.238 · 710 · 326) | **0,60** | **0** | **53** | **Short-first** + bản dài 6–8 phút |
| 2 | A. "Home Math, Replayed" — cụm nhà ở, kéo dài video PMI | 20 (cụm mạnh: 604 · 159 · 78 · 76) | 0,20 | 0 | 16 | `101` 7–9 phút + 1 Short |
| 3 | C. "Every Start Year" — nghỉ hưu kiểm trên mọi năm bắt đầu | 209 (cụm mạnh: 935 · 463 · 315 · 259) | 0,30 | 0,5 (4 ở cụm "4% rule") | 35 | `lab` 9–11 phút |
| so sánh | Giữ định hướng hiện tại, chỉ đổi đóng gói | 122 — **hai đỉnh**: 1.907 · 712 vs 6,6 · 20 | 0,20 | 1 | 29 | giữ `101`/`lab` |
| loại | D. Nợ (thẻ tín dụng, snowball/avalanche) | 17 | 0,10 | 0 | 30 | — |

**Khuyến nghị:** thử **B** dưới dạng **Short-first** (4 Short + 2 bản dài trong 2 tuần, chạy song song tập `101` hiện tại); song song **đổi đóng gói** cho tập đang làm (phương án so sánh — gần như miễn phí). A là đường an toàn nếu chủ dự án không muốn đổi định vị. C chờ: cầu lớn nhưng khoảng trống nhỏ, rủi ro lời khuyên và dữ liệu ngoài danh sách trắng.

Ba phát hiện từ số đo:
1. **Video PMI thắng vì cụm của nó vắng, không phải vì cầu lớn.** Cụm "how to get rid of PMI": 10 video đầu chỉ có trung vị **6,6 xem/ngày**, 95 % video top 20 đã hơn 1 năm tuổi. Video PMI của mình đạt 12,3 — **gần gấp đôi trung vị cụm**. Với kênh 1 người đăng ký, **xếp hạng được** quan trọng ngang **cầu lớn**. Cụm "15 year vs 30 year mortgage" (20 xem/ngày, 95 % video cũ) và "rent vs buy" (1.907, nhưng 60 % video cũ và có kênh lớn chiếm chỗ) khó lên hơn. Khớp với việc tập 15 vs 30 (1,1 xem/ngày) và thuê/mua (3,2) chưa chạy.
2. **Hướng B có tổ hợp hiếm: cầu cao + độ mới cao + rời rạc.** Độ mới 0,60 là cao nhất trong các hướng (A 0,20, C 0,30, nợ 0,10). Không kênh nào chiếm quá 4/9 cụm; chỉ 2 kênh xuất hiện ở ≥ 3 cụm (A: 8 kênh, C: 7 kênh — Ramsey Show Highlights có mặt ở 7/10 cụm nhà ở). Người làm hiện tại là báo/đài (CNBC, NowThis), kênh hoài niệm (America Lookback), bình luận (Second Thought, Freddie Smith) — **gần như không ai làm bằng chuỗi dữ liệu công khai có nguồn**, đúng thế mạnh của nhà máy.
3. **Short có cầu thật ở B.** Trung vị Short trong kết quả của B là 53 xem/ngày (A 16, C 35). Ở cụm "what 100 dollars could buy", Short (1.872) gần bằng video dài. Kênh mình: Short 8–11 xem/ngày, ngang hoặc hơn video dài. Đủ để thử Short-first ở B, chưa đủ cho cả kênh.

**Lưu ý về "khoảng trống so với CHANNELS.md".** `CHANNELS.md` lấy kênh từ 21 đề tài kiểu "quyết định", nên gần như không có kênh nào của các cụm mới (0 ở A, B). Số 0 đó **không** có nghĩa là thị trường trống: A và C đầy kênh lớn có mặt người mà `market-r1` không gom (Ramsey Show Highlights, The Money Guy Show, Humphrey Yang, Ben Felix, Erin Talks Money). Vì vậy khoảng trống ở bảng điểm dùng **mức tập trung** + **tỉ lệ tiêu đề có lịch sử/dữ liệu**, không chỉ đếm kênh trong `CHANNELS.md`.

## 2. Bảng điểm (1–3 mỗi tiêu chí, `market/r2/scores.json`)

| Tiêu chí | B Paid in Hours | A Home Math | C Every Start Year | Giữ + đổi đóng gói |
|---|---|---|---|---|
| (1) Cầu tìm kiếm thật | 3 — 4/9 cụm > 300 xem/ngày; cụm hẹp theo năm cụ thể yếu (2–5) | 2 — 2/10 cụm > 150; nhiều cụm ngách < 20 nhưng dễ lên | 3 — 5/8 cụm > 150 | 2 — hai đỉnh |
| (2) Khoảng trống | 3 — độ mới 0,60, rời rạc, 0 kênh dữ liệu cùng khuôn | 2 — vắng ở cụm ngách, Ramsey/loan officer chiếm cụm lớn | 1 — "4% rule" có 4 kênh theo dõi + Ben Felix/CFP; "sequence risk" có 3 | 2 |
| (3) Hợp nhà máy | 3 — BLS/Census/FRED đều trong danh sách trắng nhóm 1; một chuỗi/tập; vật thể số liệu (tháp giá, đồng hồ giờ công) | 3 — đã có kinds nhà ở (PMI, 15/30, thuê/mua), `MORTGAGE30US` đã có quyền (D-FRED-1) | 1 — lợi suất cổ phiếu dài hạn cần Shiller/Yale hoặc dữ liệu S&P (**ngoài danh sách trắng**, S&P có bản quyền); SSA cũng ngoài danh sách | 3 |
| (4) Đóng gói | 3 — con số tò mò sẵn ("$100 in 1970", "2.1 → 6.8 years of pay") | 2 | 3 — "$1M enough?" | 2 |
| (5) Chi phí/tập | 3 — Short 30–60 giây từ một chuỗi; dài 6–8 phút | 2 — `101` 7–9 phút | 1 — video dài top 20 trung vị ~11 phút (16–19 ở cụm An sinh xã hội/sập thị trường), mô phỏng nhiều cửa sổ | 3 |
| **Tổng** | **15** | **11** | **9** | 12 |

Giữ + đổi đóng gói điểm cao hơn A vì gần như không tốn gì — nhưng nó **không thêm cầu**. A và giữ định hướng không loại trừ nhau: A là giữ định hướng nhưng dồn vào cụm nhà ở có thể xếp hạng.

## 3. Hướng 1 — B. "Paid in Hours" (giá đời sống qua 60 năm, đo bằng giờ công)

**Logline series:** *Mỗi tập lấy một thứ hộ gia đình Mỹ phải mua — căn nhà, chiếc xe, một học kỳ, giỏ đi chợ — rồi phát lại giá của nó qua 60 năm dữ liệu công khai, đo bằng **số giờ công** của người làm lương trung vị chứ không chỉ bằng đô la. Lịch sử, không phải dự báo.*

Giữ gen kênh: dữ liệu thật, nguồn trên hình, "US only", "history, not a forecast", không khuyên. Điểm khác so với video hoài niệm đang chiếm chỗ: **một con số đã chuẩn hoá** (giờ công, năm lương) thay cho giá danh nghĩa.

**Đề tài (8)** — cụm tìm kiếm · cầu top 10 (xem/ngày) · nguồn (danh sách trắng):
1. Nhà trung vị tính bằng năm lương, 1965 → nay — "house prices over time" · **1.238** · Census `MSPUS` + thu nhập hộ trung vị Census (qua FRED)
2. $100 năm 1970 mua được gì hôm nay, theo từng nhóm hàng — "what 100 dollars could buy" · **2.302** · BLS CPI-U theo nhóm
3. Lương tối thiểu và giá nhà: bao nhiêu giờ công cho một khoản trả trước — "minimum wage vs house prices" · **326** · DOL qua FRED (`FEDMINNFRWG`) + Census
4. Lạm phát theo thập kỷ: đồng đô năm 1975 co lại thế nào — "inflation over time explained" · **710** · BLS CPI-U
5. Giỏ đi chợ: trứng, sữa, bánh mì tính bằng phút công — "grocery prices then vs now" · 101 (Short **268**) · BLS Average Price Data
6. Xe mới tính bằng tuần lương — "car prices over time" · 130 · BLS CPI xe mới + thu nhập; **không** dùng giá KBB/Edmunds (bản quyền)
7. Một năm đại học công lập, khi đó và bây giờ — "college tuition cost over time" · 15 (video dài 194) · BLS CPI học phí; NCES nếu mở rộng danh sách trắng
8. Khoản trả góp hằng tháng cho căn nhà trung vị, mỗi năm từ 1971 — "mortgage rates history" · 6 (Short 148; phân bố rất lệch) · `MORTGAGE30US` (D-FRED-1) + `MSPUS` — cầu nối sang hướng A

**Tiêu đề mẫu (tiếng Anh, theo cụm tìm kiếm):**
- *House Prices Over Time: 60 Years Measured in Years of Pay*
- *What $100 Could Buy in 1970 vs Today (Real BLS Prices)*
- *Minimum Wage vs House Prices: How Many Hours for a Down Payment, 1968–2025*

Ảnh bìa: một con số tương phản ("2.1 → 6.8 YEARS") + vật thể số liệu (tháp giờ công cạnh căn nhà low-poly), ≤ 4 từ, không mặt người. Lưu ý: con số trong tiêu đề mẫu chỉ là chỗ trống, **phải tính lại từ dữ liệu** trước khi dùng.

**Ước cầu:** trung vị các cụm 130 xem/ngày cho video top 10 (A 20, C 209). Bốn cụm đầu bảng 326–2.302. Độ mới 0,60: trung vị các cụm, 60 % video top 20 dưới 1 năm tuổi. Tham chiếu hiệu chỉnh: video tốt nhất của mình đạt 12 xem/ngày ở cụm có trung vị 6,6. Ở cụm trăm–nghìn xem/ngày, một video lên được nửa dưới top 20 đã là bước nhảy, nhưng **chưa có bằng chứng kênh 1 người đăng ký lên được** — đây là thí nghiệm.

**Rủi ro.** *Lời khuyên tài chính:* thấp (mô tả lịch sử). *Chính trị:* lương tối thiểu và giá nhà dễ kéo bình luận phe phái — giữ trung tính, không kết luận chính sách. *Quyền dữ liệu:* BLS/Census/DOL là phạm vi công cộng, FRED cần ghi nguồn (mẫu D-FRED-1); tránh Case-Shiller (S&P), Zillow, KBB. *Phương pháp:* chỉ số giá ≠ giá một món cụ thể; giờ công trung vị là **đại lượng thay thế** — ghi rõ trên hình như `topic-source-map.md` §111.

| Ưu | Nhược | Tác động (dự kiến) | Rủi ro |
|---|---|---|---|
| cầu cao + độ mới cao + rời rạc; dữ liệu nhóm 1; một chuỗi/tập → rẻ, hợp Short; con số đóng gói sẵn | **lệch định vị** "phòng thí nghiệm quyết định" (CHARTER §1) — không trả lời một quyết định; cụm hẹp theo năm cụ thể ("1980") cầu gần 0; khán giả hoài niệm có thể không ở lại xem tập quyết định | cao nếu Short lên; mở cửa đề xuất (bìa con số dễ nhấp hơn bìa quyết định) | đổi định vị cần quyết định của chủ dự án (D-xxx, sửa CHARTER §1); bão hoà nhanh vì độ mới cao cũng nghĩa là nhiều người mới nhảy vào |

**Cách giảm lệch định vị:** kết mỗi tập bằng một câu nối sang quyết định ("vậy 28 % lương còn hợp lý không?" → tập A tương ứng). Định vị thành "lịch sử giá là đầu vào cho quyết định".

## 4. Hướng 2 — A. "Home Math, Replayed" (cụm nhà ở, kéo dài video PMI)

**Logline series:** *Những câu hỏi người mua nhà lần đầu gõ vào YouTube — mua nổi bao nhiêu, khi nào refinance, ARM hay cố định, khi nào hết PMI — được trả lời bằng cách phát lại 35 năm lãi suất và giá nhà thật, không bằng một giả định cố định.*

**Đề tài (8)** — cụm · cầu top 10 · độ mới:
1. Mua nổi bao nhiêu: khoản trả so với lương, mỗi năm từ 1990 — "how much house can I afford" · **159** · 0,25
2. "House poor" là bao nhiêu % lương, và kéo dài bao lâu — "house poor" · **604** · 0,85 (top 20 dài ~20 phút, kiểu bình luận) — giáp đề tài #14
3. Khi nào refinance đáng: mọi đợt giảm lãi từ 1990 — "when to refinance mortgage" · 76 · 0,15
4. Lỗi người mua lần đầu, đo bằng đô la qua lịch sử — "first time home buyer mistakes" · 78 · 0,20
5. ARM hay cố định: ai thắng, mỗi năm từ 1984 — "ARM vs fixed rate mortgage" · 10 · 0,30 (cầu nhỏ, dễ lên như PMI) — cần chuỗi ARM của Freddie Mac (`MORTGAGE5US` đã ngừng 2022 → kiểm lại)
6. Trả trước 10 % vs 20 %: chờ để đủ 20 % tốn bao nhiêu — "20 percent down payment" · 20 · 0,25 (nối PMI)
7. Trả hai tuần một lần thực sự tiết kiệm bao nhiêu — "biweekly mortgage payments" · 13 · 0,20
8. Trả nợ nhà sớm hay đầu tư (đề tài #11 có sẵn) — "pay off mortgage early or invest" · **712** · 0,50

**Tiêu đề mẫu:**
- *How Much House Can I Afford? 35 Years of Payments vs Paychecks*
- *When to Refinance a Mortgage: Every Rate Drop Since 1990, Tested*
- *ARM vs Fixed Rate Mortgage: Who Won, Every Year Since 1984*

**Ước cầu:** trung vị 20 xem/ngày; hai cụm lớn (604, 712) và sáu cụm nhỏ (10–160). Cụm nhỏ giống cụm PMI (6,6), nơi video của mình đã vượt trung vị — chiến lược là **nhiều cụm ngách xếp hạng được** hơn là một cụm lớn.

**Rủi ro.** *Lời khuyên:* vừa — refinance/ARM gần với khuyên; giữ "not advice", nhân vật ILLUSTRATIVE. *Quyền dữ liệu:* `MORTGAGE30US` đã có (D-FRED-1); FHFA HPI không nằm trong danh sách trắng (Fed/BLS/Census) → dùng Census `MSPUS`; phí PMI không có nguồn trắng (`topic-source-map.md` §57). *Cạnh tranh:* Ramsey Show Highlights ở 7/10 cụm, loan officer (Javier Vidana, Win The House You Love).

| Ưu | Nhược | Tác động | Rủi ro |
|---|---|---|---|
| giữ định vị; dùng lại kinds và dữ liệu nhà ở; có bằng chứng duy nhất của kênh (PMI); cụm ngách xếp hạng được | cầu nhỏ ở đa số cụm; cụm lớn bị kênh mặt người chiếm; độ mới thấp (0,20) — video cũ bám chặt | vừa, ổn định; tăng chậm qua nhiều cụm nhỏ | lặp chủ đề với tập 5/7/8; "Home" làm hẹp kênh |

## 5. Hướng 3 — C. "Every Start Year" (nghỉ hưu kiểm trên mọi năm bắt đầu)

**Logline series:** *Mỗi quy tắc nghỉ hưu ai cũng nghe — 4 %, "$1 triệu là đủ", nhận An sinh xã hội ở 62 hay 70 — được kiểm trên **mọi năm bắt đầu** trong lịch sử, để thấy nó sống sót ở đâu và gãy ở đâu.*

**Đề tài (7):** quy tắc 4 % qua mọi năm nghỉ hưu ("4% rule retirement", 259, có 4 kênh theo dõi) · $1 triệu có đủ ("is 1 million enough to retire", 160; dài 308) · cần bao nhiêu để nghỉ hưu ("how much do I need to retire", **463**) · 62 hay 70: hoà vốn theo năm sinh ("social security at 62 vs 70", **935**, độ mới 0,60, dài ~16 phút) · lịch sử sập thị trường: mỗi lần mất bao lâu để hồi ("stock market crash history", 315; dài 1.020) · trung bình giá hay bỏ một lần ("dollar cost averaging vs lump sum", 69) · rủi ro thứ tự lợi suất ("sequence of returns risk", 38; 3 kênh theo dõi). Tránh "if you invested 1000 in s&p 500" (1,2 — cụm chết).

**Tiêu đề mẫu:** *The 4% Rule, Tested on Every Retirement Year Since 1928* · *Is $1 Million Enough to Retire? Every Start Year, Replayed* · *Stock Market Crash History: How Long Each Recovery Really Took*

**Ước cầu:** trung vị 209, cao nhất nếu chỉ xét cầu; nhưng 7 kênh lớn xuất hiện ở ≥ 3 cụm (Money Guy, PeakFP, Erin, Ben Felix, Humphrey Yang).

**Rủi ro.** *Lời khuyên:* **cao** — mức rút và thời điểm nhận An sinh xã hội là quyết định YMYL; "history, not a forecast" phải nặng tay. *Quyền dữ liệu:* lợi suất cổ phiếu dài hạn không có trong danh sách trắng (FRED chỉ có S&P 500 10 năm, có bản quyền; Shiller/Yale và SSA cần mở rộng danh sách trắng bằng quyết định riêng). *Chi phí:* video dài top 20 trung vị ~11 phút, 16–19 ở hai cụm lớn, mô phỏng nhiều cửa sổ → `lab`, không phải định dạng ngắn.

| Ưu | Nhược | Tác động | Rủi ro |
|---|---|---|---|
| cầu cao nhất; khớp đúng câu hỏi khán giả số 2 ("đổi năm bắt đầu thì sao?", REPORT §5); đóng gói mạnh | cạnh tranh dày, nhiều CFP có uy tín; dữ liệu ngoài danh sách trắng; dài, đắt | cao nếu lọt; khó lọt với kênh mới | lời khuyên; quyền dữ liệu S&P |

## 6. Phương án so sánh — giữ định hướng hiện tại, chỉ đổi đóng gói

**Việc cụ thể:** (a) tiêu đề **bắt đầu bằng đúng cụm người Mỹ gõ** (vd "How to Get Rid of PMI…", "15 Year vs 30 Year Mortgage…"), vì tìm kiếm (CTR 6,19 %) đang là nguồn sống; (b) bìa một con số + ≤ 4 từ (REPORT §3) để cứu CTR đề xuất 0,42 %; (c) Short mỗi tập dẫn về video dài; (d) chọn đề tài trong hàng đợi theo **độ vắng của cụm**, không chỉ theo nhãn cầu.

**Số đo:** 6 cụm của các đề tài hiện tại có trung vị 122 nhưng **hai đỉnh**: "rent vs buy" 1.907 và "pay off mortgage early or invest" 712, so với "how to get rid of PMI" 6,6 và "15 year vs 30 year mortgage" 20. Độ mới 0,20 — video cũ chiếm chỗ. 0/6 tiêu đề top 20 có lịch sử/dữ liệu → điểm khác biệt "phát lại lịch sử" vẫn là khoảng trống, nhưng người tìm không gõ chữ "history".

| Ưu | Nhược | Tác động | Rủi ro |
|---|---|---|---|
| gần như 0 chi phí; không đổi CHARTER/nhà máy; áp ngay cho tập kế; đo được ở mốc 01/11 và 06/11 | không thêm cầu — đa số đề tài hàng đợi có cầu thấp/vừa (REPORT §1); CTR đề xuất có thể do hiển thị ít chứ không do bìa (API công khai không phân biệt được, R1 §4) | thấp–vừa; tốt nhất để tách biến "đóng gói" khỏi "đề tài" | đổi tiêu đề video đã đăng làm lẫn số đo hiệu chỉnh `CALIBRATION.md` — chỉ áp cho video mới |

## 7. Đề xuất cách thử (chủ dự án quyết)
1. **Tuần 1–2:** giữ nhịp tập hiện tại + đổi đóng gói (§6) cho video mới. Song song **4 Short hướng B** (đề tài 1, 2, 4, 5) — mỗi Short một chuỗi, một vật thể số liệu, 30–60 giây.
2. **Mốc đo 01/11 và 06/11** (trùng `CALIBRATION.md`): so Short B với 2 Short cũ (8–11 xem/ngày) và video dài. Nếu Short B ≥ 3× Short cũ → làm 2 bản dài 6–8 phút (đề tài 1 và 2), và mở quyết định định vị (CHARTER §1).
3. **A** thay hàng đợi nhà ở hiện có từ G1 lô kế; **C** chỉ mở sau khi có quyết định mở rộng danh sách trắng (Shiller/SSA).

## 8. Giới hạn
- Thứ hạng relevance của API **không trùng** trang tìm kiếm thật (cá nhân hoá, Short shelf). Lượt xem/ngày trọn đời thiên về video cũ có đuôi dài.
- Không có lượng tìm kiếm thật (Google Trends/Keyword Planner không dùng ở phiên này). "Cầu" là **cung đã được xem**, tức đại lượng thay thế.
- Một search/cụm, một ngày; cụm chọn tay (38) — một cụm khác cách viết có thể lệch nhiều (vd "how much did a house cost in 1980" 2,0 vs "house prices over time" 1.238).
- Short: chỉ những Short API trả trong 50 kết quả relevance; không đo Short shelf/feed.
- Điểm 1–3 là máy chấm, có thể sai; không phải dự báo lượt xem.

**Làm lại:** script trong phiên gọi `mcommon.yt('search', …)` + `mcommon.videos()` cho 38 cụm ở `market/r2/demand.json` (`method`), ~3.840 đơn vị; thô ghi `~/market-cache/<ngày>/r2/`, tổng hợp ghi `market/r2/demand.json`. Không đổi `toolkit/`, `checks/`, `episodes/`.
