# REVIEW C2 — Tập 5 (REVIEWER, 06/10/2026)

Đã đọc: `playbook/story.md`, `episode.md` §3 (M1–M5, "Móc do máy chọn"), CHARTER §4, `packaging.md` §2, `numbers.md`, `debt-2/claim-risk.md`, `gates/C1-blind.md`, `data/sources.json` (provisions), `story/script.md`, `hooks.md`, `beats.md`. Chạy `check_script.py`: **ĐẠT**, 1 cảnh báo mật độ (~9 s); ước 8:22; M1–M5 đạt cả 3 móc.

**Mốc trong ±5 % của ngưỡng (nêu tên, CHARTER §4):** M2 của H-A 28,8 s (ngưỡng 30, cách 4 %) · M4 9,6 s ở cả 3 móc (ngưỡng 10, cách 4 %; khối `define` S03.3 dùng chung) · khuôn tỉ lệ: cold open **+4,8 điểm** và Hồi 2 **−4,5 điểm** (ngưỡng ±5). Ngoài ±5 % nhưng sát: M1 của H-B 4,6 s (cách 8 %). Đo ở 2,4 từ/s: giọng thật chậm hơn là M2/M4 trượt, nên ưu tiên các sửa làm ngắn bên dưới.

## 1. Chọn móc

| Móc | §1.1 (5 s: được–mất / câu hỏi, sự thật hiện tại có ngày) | §1.2 lời hứa < 0:30 | §1.3 ràng buộc sau móc | §1.4 người trước số | M1–M5 (ước) | Lý do một dòng |
|---|---|---|---|---|---|---|
| **H-A** | Gần đạt: 3,3 s đầu là người + khoảnh khắc ("You've saved…"), câu hỏi xong ở 10,0 s; chưa có **ngày** (8 năm dựa trên lãi T9/2026 nhưng không nói/không hiện) | Đạt 28,8 s (sát ngưỡng) | Đạt | **Đạt** (duy nhất) | 3,3 · 28,8 · 10,0 · 9,6 · 39,6 | Câu hỏi đúng logline L2 đã qua C1, người trước số, 2 số/cảnh; lỗi duy nhất là HA.3 nói "8 năm bảo hiểm tới 80 %" (sai luật, xem C-1). |
| H-B | Đạt kiểu được–mất (4,6 s) nhưng cái giá không có số tiền (không có nguồn phí PMI), không ngày | Đạt 26,2 s, kém cụ thể ("how long it took on paper") | Đạt | Trượt (mở bằng "10 percent down") | 4,6 · 26,2 · 15,0 · 9,6 · 37,1 | Cái giá hứa mà tập không định giá được; HB.2 "often until … 80 percent" cùng lỗi luật như HA.3, thêm "often" không nguồn. |
| H-C | Cú sốc số, không phải câu hỏi của người xem; "23 months" là lịch sử trung vị, đứng cạnh "bảo hiểm" | Đạt 25,0 s | Đạt | Trượt (4 số trước người) | 2,5 · 25,0 · 15,0 · 9,6 · 35,8 | 4 số mới trong 9 s phạm story §3 (cảnh > 2 số mới); rủi ro overclaim cao nhất (người rời ở 0:05 nhớ "23 tháng"); buộc sửa S11.1. |

**Chọn H-A.** Tách được rõ (H-B và H-C trượt §1.4, H-C trượt thêm §3), **không cần so cặp vòng tròn**. Sửa HA.3 = S02.1 theo C-1 (vừa sửa luật, vừa bớt một số trong cửa sổ 8 s, vừa kéo M2 xuống ≈ 26 s).

## 2. Phát hiện trong kịch bản

### CHẶN

| # | Câu | Vấn đề | Sửa đề xuất |
|---|---|---|---|
| C-1 | **S02.1** (= HA.3) | "about 8 years of insurance, until the loan falls to 80 percent" → nghe như bảo hiểm tự hết ở 80 %. Theo luật (claim-risk.md ý 3; 12 U.S.C. 4901(2)(A)/(18)(A)): ở 80 % chỉ được **xin** huỷ; tự chấm dứt ở 78 % (≈ 9,5 năm). Cũng là chỗ cảnh báo mật độ (20 → 8 → 80 trong ~8 s); thiếu khoảng lặng sau số quyết định (DX-R3). | `S02.1 {hook} On the schedule alone, you can't even ask to cancel it for about 8 years. <!-- claims: sched80_months_latest, rate_latest; hold: 1 -->` (14 từ thay vì 21; "80 percent" để lần đầu ở S03.1 và trên hình B02). Sửa cùng chữ trong `hooks.md` HA.3. M2 ước ≈ 26,9 s kể cả hold. |
| C-2 | **S10.1** | "from 1991 through 2016": tập B dừng ở **7/2016** (`nB`, B10 ghi "January 1991 to July 2016"). Lời rộng hơn claim 5 tháng. | `S10.1 We took every purchase month from January 1991 to July 2016, the last month with ten full years of prices after it. <!-- claims: nB -->` (vế sau tuỳ chọn; nếu bỏ thì giữ "from January 1991 to July 2016"). |
| C-3 | **S03.3, S09.1, S12.2** (sổ claim, không phải WRITER) | Luật gỡ theo giá trị của bên cho vay/nhà đầu tư (thẩm định, thời gian tối thiểu, mốc 75 % những năm đầu) **không có nguồn** trong `data/sources.json`; chỉ có trong claim-risk.md. Mốc 75 % lại là tham số sinh ra 15,6 %. S03.3 đang gắn nhầm claim `shareA_ltv24_le75` (đó là tỉ lệ, không phải luật). | Việc 0/điều phối: thêm nguồn chính có trích nguyên văn (hướng dẫn servicing của Fannie Mae và Freddie Mac, mục chấm dứt MI theo giá trị hiện tại) vào `sources.json`; thêm claim luật (vd `lender_ltv_early_75`, "rule") vào `numbers.md`; đổi claim S03.3 sang ID đó. Lời giữ nguyên nếu nguồn khớp "often"; nếu nguồn ghi khác (số năm, 75/80) thì WRITER mới sửa đúng 3 câu này. |
| C-4 | **S07.1, S07.3** (sổ claim) | Quyền **xin** huỷ và điều kiện nằm ở 12 U.S.C. **4902(a)**, nhưng `provisions` chỉ có 4901(2)(A), 4901(18)(A), 4902(b), 4902(c). | Thêm trích 4902(a) (yêu cầu bằng văn bản, lịch sử trả tốt, đang trả đúng hạn, chứng minh giá trị nhà không giảm dưới giá gốc nếu chủ nợ đòi) vào `sources.json`. Không đổi lời (đổi lời S07.3 nằm ở hàng chờ). |
| C-5 | **S13.3, S17.2** (sổ claim) | Hai câu định tính rút từ dữ liệu của tập nhưng không có claim: (a) 45 tháng > 60 tháng đều mua 2005–2009, "just before and during the national price slump" (cần cả đỉnh/đáy chỉ số); (b) chỉ số của Victor "rose a little, then fell for years" (đỉnh ≈ +4 % ở tháng 18, đáy ≈ −17,5 % ở tháng 72). | Thêm claim (vd `slowB_years` 2005–2009 / 45 tháng; `hpi_peak_month`, `hpi_trough_month`; `buyer_slow_index_peak/trough`) vào `model.py` → `numbers.md` + 1 dòng `statements.py`. **Lời giữ nguyên**, chấp nhận được khi có claim (không đọc năm, đúng như WRITER làm). |

### CHÍNH — phải sửa ngay vì sai nghĩa / mô tả claim

| # | Câu | Vấn đề | Sửa đề xuất |
|---|---|---|---|
| K-1 | **S10.5** | Lời "each square … its color" nhưng B10/B11/B13 vẽ **cột, chiều cao** = số tháng. Hình và lời nói hai mã khác nhau. | `S10.5 Each bar here is one purchase month, and its height shows how long that took.` |
| K-2 | **S05.1** | MSPUS = giá trung vị **nhà mới** bán (Census/HUD New Residential Sales), quý; 2026-04-01 = **Q2 (tháng 4–6)**. "New homes" đúng; "this spring" không khớp quý (gồm tháng 6, không gồm tháng 3). | `S05.1 Here's an illustrative example: a $400,000 home, a little under the national median price of new homes sold from April through June.` |

### CHÍNH — hàng chờ G2 (không đổi nghĩa)

| # | Câu | Vấn đề | Sửa đề xuất |
|---|---|---|---|
| K-3 | S06.1 | "the figure on screen": chấp nhận được như mẹo giữ ≤ 2 số/cảnh (đúng luật), nhưng người nghe không nhìn mất câu; câu cụt ý. | `At September's average 30-year rate, 6.86 percent, the principal and interest payment, shown here, stays the same every month.` (thêm ý "cố định" làm nền cho S06.3). |
| K-4 | B02 | Móc thiếu "sự thật hiện tại có ngày" (story §1.1). | Thêm nhãn hình B02: "at the September 2026 average rate" (không thêm lời). |
| K-5 | S03.3 | M4 9,6 s sát ngưỡng; "request · appraisal · minimum wait" đã có trên hình B03. | `S03.3 {define} Removal on value is the lender's rule, with an appraisal, a wait, and early on, often a 75 percent bar.` (chỉ áp nếu table read đo M4 > 9,5 s). |
| K-6 | S07.3 | Đúng nhưng thiếu điều kiện "giá trị không giảm" của 4902(a), đúng điều kiện mà Victor (chỉ số dưới giá gốc ở kỳ 90) có thể vướng. | `That request comes with conditions, such as being current on payments and, if the lender asks, showing the home hasn't lost value.` (sau khi có C-4). |
| K-7 | S09.3 | Câu khó hiểu ("the road behind the words on paper"). | `That's what on paper means, and the lender's rules from the opening still stand between it and removal.` |
| K-8 | S15.3 | "right at the middle of the replay" đọc được thành giữa giai đoạn 1991–2016. | `Her loan reached 80 percent on paper in exactly the typical time: she is the middle case from before.` |
| K-9 | S16.2 | 13 tháng là mức nhanh nhất nhưng **hoà 10 tháng** (2003-06, 2004-01…09). | `…in 13 months, tied for the fastest in the replay.` |
| K-10 | S17.1 | "the year after Owen" đúng theo năm lịch nhưng thực là 21 tháng; ý của tập là "thời điểm mua". | `Victor bought less than two years after Owen, in October 2005: the slowest month in the replay.` |
| K-11 | S18.2, S18.4 | "a pair of lines to sit against", "not the lender's step" mơ hồ. | S18.2 `So any plan has two lines to be measured against.` · S18.4 đuôi: `…matched the typical month, not the slow ones, and it still isn't the lender removing the insurance.` |
| K-12 | S19.1 | Thiếu giới hạn claim-risk "Data limits" ý 3: người mua sau 7/2016 không có trong phép thử dài. | Thêm vào S19.1: `…or buyers after mid 2016, who don't yet have ten years of prices.` |
| K-13 | S04.1 | Câu chung về thực hành cho vay ("usually require … less than 20 percent down"): **lời chấp nhận được** (có "usually", không số), không cần claim số; cần một dòng nguồn. | Gộp vào việc C-3 (cùng nguồn Fannie/Freddie hoặc trang CFPB về PMI), ghi trong mô tả. |
| K-14 | Khuôn tỉ lệ | Cold open +4,8 và Hồi 2 −4,5 (sát ±5, Tham khảo). | C-1 bớt ≈ 3 s cold open; không độn Hồi 2. |

### THAM KHẢO
- S04.2 "month after month": có PMI trả một lần/bên cho vay trả; thêm "usually" nếu sửa lại câu.
- Mốc giữa kỳ 4902(c) (180 tháng) không nói và không hiện, dù B07 liệt kê `midpoint_months`: nên ghi một dòng trong mô tả ("ở các mức lãi trong phép thử, mốc giữa kỳ chưa bao giờ đến trước"; `midpoint_binding_rate_min`), hoặc bỏ claim khỏi B07.
- HPA áp cho khoản vay từ 29/7/1999; phép thử từ 1991 chỉ đo "on paper" nên không sai, nhưng mô tả nên ghi.
- S19.2 "public data from FRED": PMMS là "Copyrighted: Citation Required"; nói "data published on FRED" an toàn hơn. "FRED" có rủi ro ASR (nghe thành tên người), đã có trên thẻ V7.
- S06.1/V7: "average mortgage rate" nên là "30-year fixed" (đã ở thẻ).
- Mid-roll và câu hỏi hồi 2/3 nằm cuối hồi trước; sau quảng cáo S10.1 vào thẳng, có thể nhắc câu hỏi bằng hình (nhãn "?") ở B10.
- S11.4 "the schedule's long road and the replay's typical one" hơi trừu tượng nhưng đúng vai lần gọi lại thứ 2 (so sánh).

**Gen được bảo vệ:** "we" chỉ người phân tích ✓ · không khuyên (S01.2 là câu hỏi; S18.6 đối trọng) ✓ · không dự báo ✓ · "US only" S03.5, S20.3 + tag góc ✓ · "history, not a forecast" S03.5, S20.3 + tag ✓ · ILLUSTRATIVE: lời S03.4, S05.1, S15.1, S18.5, nhãn hình ở mọi khung có nhân vật/$400,000 ✓ · không phí PMI ✓. Luật PMI: S07.1 (xin ở 80 % giá trị gốc theo lịch), S08.1 (tự hết ở 78 %, đang trả đúng hạn), S09.1 (gỡ theo giá trị là luật của bên cho vay/nhà đầu tư) khớp claim-risk; chỉ S02.1 sai (C-1).

## 3. Kết luận: **ĐẠT có sửa**

Phải sửa trước table read và kiểm mù (WRITER mới, một lượt, chỉ các dòng này):
1. **S02.1 + hooks.md HA.3** → C-1 (kèm `hold: 1`).
2. **S10.1** → C-2.
3. **S10.5** → K-1.
4. **S05.1** → K-2.

Việc sổ claim (điều phối/Việc 0, không WRITER, xong trước kiểm mù): **C-3** (nguồn luật gỡ theo giá trị + claim 75 %, đổi claim S03.3), **C-4** (trích 4902(a)), **C-5** (claim cho S13.3, S17.2). Nếu nguồn C-3 khác "often 75 % early" → WRITER sửa S03.3/S12.2 cho khớp.
Rồi chạy lại `check_script.py` (M2, M4, mật độ ~9 s phải hết cảnh báo). K-3…K-14 vào hàng chờ G2.
