ĐẠT có sửa

# REVIEWER — G1 Tập 6 (độc lập, 2026-10-08)

Đọc: quality-framework §4, §6, §7; story §1, §2, §2b; episode §1, §3.9–3.10, §8; CHARTER §4–§5; `gates/G1.md`, `story/script.md`, `hooks.md`, `beats.md` (C2 v2), `numbers.md`, `topics-r1/machine/retire-1/claim-risk.md`, `gates/C1-*`, `C2-*`, `K-brief.md`, `ledger.md`, `review-g1/table-read.json`.
Tự chạy `python3 episodes/ep006/story/check_script.py --cast Ruth,Carl,Edna --g1-short` → ĐẠT, khớp nguyên văn bản dán ở `script.md:11–33`. **Chạy KHÔNG cờ `--g1-short` → TRƯỢT** (độ dài 466 s < 495 s) — xem CHÍNH-3.

Điều kiện "có sửa": CHẶN-1 sửa (WRITER mới, sửa giữ đúng nghĩa theo §6.5, liệt kê trong G1) **trước khi gửi G1**; CHÍNH-2…5 sửa trong G1 / kịch bản cùng lượt.

## 1. Chấm 3 phương án móc (story §1 + M1–M6)

| Móc | Chấm | Một dòng lý do |
|---|---|---|
| H-A câu hỏi | Đạt, yếu nhất về người | §1.1 câu hỏi người xem ✓; §1.2 lời hứa 27,6 s ✓; §1.3 ✓; M1–M6 ước ĐẠT; nhưng §1.4 / §2b.1: không có người trong 30 s (Ruth ≈ 0:33), HA.3 "latest stretch ended this August" là sự thật hiện tại yếu. |
| **H-B nghịch lý** | **Tốt nhất** | §1.1 nghịch lý trên sự thật đo được có claim (90,4 %, `guide_real_2pct_end_pct`; +2 %/năm `two_pct_growth_20y_pct`); người ở 0:00 (§1.4, §2b.1); lời hứa trước 0:30; ràng buộc sau lời hứa (§1.3); **duy nhất được đo trên bản đọc thật**: M1 3,6 · M2 27,5 · M3 13,9 · M4 6,06 · M5 33,3 · M6 0 s. |
| H-C cửa sổ 12 tháng | Kém nhất | 3,4 % cạnh 2 % trong 5 s đầu mời đọc thành dự báo (claim-risk.md:66); HC.3 (`hooks.md:32`) chèn ràng buộc "not a forecast" **giữa câu hỏi và lời hứa** → trái story §1.3; không có người trong 30 s. M1–M6 ước ĐẠT. |

**Kết luận: H-B đúng; tách được rõ** (H-C trượt luật §1.3 + claim-risk, H-A trượt §1.4) → không cần so cặp vòng tròn (episode §3).

## 2. Checklist REVIEWER (quality-framework §7)

| # | Mục | Kết quả |
|---|---|---|
| 1 | Khớp khung, ngưỡng ghi trước, không sửa ý đồ sau kết quả | Ngưỡng C1/C2 khớp `C1-intent`, `C2-intent` (495 s, ≥ 5/6, khuyên 0, < 4/6 mỗi loại khối, M1–M6). Không thấy ngưỡng đổi sau kết quả; đề xuất sửa định nghĩa khối M4 ghi "chưa áp" ✓. **Trượt một phần:** G1:32 báo kiểm máy "ĐẠT" nhờ cờ `--g1-short` chạy trước khi chủ dự án duyệt (CHÍNH-3). |
| 2 | Claim-risk | **Trượt:** S08.1 / S12.1–12.2 (CHẶN-1); S04.3 / S31.3 (CHÍNH-2). Mọi số trong lời, chữ trên hình và G1 khớp `numbers.md` (mục 4). |
| 3 | Chống Goodhart | Không thủ thuật; thiếu dòng nêu tên chỉ số trong ±5 % (CHÍNH-4). Bảng phân loại nhịp: 9/9 nhịp KEY loại 1 (≥ 60 %) ✓; SHA bảng chưa báo — chưa tới (trước kiểm mù hình C3). |
| 4 | Tự quyết trong §6 | Logline sửa sau kiểm mù, S30.5, dự phòng C2 đều nêu trong G1 ✓. Logline bản sửa chưa kiểm mù lại — G1 nói rõ ✓. |
| 5 | Không lệch giữa các phiên | Lệch nhỏ: ledger vs G1 (PHỤ-9); tiêu đề G1 vs hooks.md (PHỤ-11); K-brief luật 2–3 sẽ bắt chính kịch bản/hình (CHÍNH-2, CHÍNH-5). |
| 6 | Chất lượng trước (D-009) | Không bước nào cắt vì token ✓; người đọc model khác chưa chạy lại trên v2 (PHỤ-10). |
| 7 | Hình–âm (D-010) | Chưa áp ở G1 (chưa có đoạn dựng). |
| 8a | Dẫn đường trước 0:45, qua phương pháp, câu kết của người đó | ✓ Ruth 0:00 (S01.1); S13.2 "Ruth's is one of them", S13.3 "we asked Ruth's question"; câu cuối S32.3 "Her answer: …". |
| 8b | M6 ≤ 90 s | ✓ không có lời hứa nhân vật (M6 = 0); Carl/Edna không được hứa trước. |
| 8c | Vật cụ thể có claim | ✓ hàng 10 thùng = round(10 × sức mua) (`guide_real_2pct_end_pct` 90,4 → 9; 60,9 → 6). **Nhưng** đơn vị thùng bị dùng sai cho khoản đều (CHẶN-1). |
| 8d | Câu đỉnh ≤ 15 từ, một ý | ✓ S10.2 "Then(1) in(2) a(3) single(4) year(5) it(6) fell(7) below(8) and(9) it(10) hasn't(11) caught(12) up(13) since(14)" = **14 từ**, một ý (rơi xuống và không lên lại). Đúng claim: k=15 100,3 % → k=16 94,5 %, `guide_last_year_2pct_at_or_above_100` = 15. Cách ngưỡng 6,7 % (ngoài ±5 %). |
| 8e | Kết quay về câu hỏi nhân vật | ✓ S32.2 lặp câu hỏi S01.2 ("would 2 percent … keep up with prices"), S32.3 trả lời bằng thùng của bà, không khái quát. |

## 3. Đối chiếu số G1.md ↔ numbers.md
Khớp hết: 90,4 · 60,9 · 94,5 (8/2022) · 100,3 (8/2021, trong beats) · 12/15, dưới ở năm 2, 5, 6 · 715 · 17 ≈ 1/42 · 9/1947–1/1949 · 80,7 · 54,3 · 25 năm 0/655 · Carl 1/1966 43,1 · Edna 1/1949 · 3,4 % (12 tháng tới 8/2026) · 3 % → 42,4 % · 3,1 % → một nửa · 12/12, 9/9, 43/43, 943/943 · EL 1.114. Độ dài 1.175/2,52 = 466 s = 7:46 ✓; 495 − 466 = 29 s ✓; 9:00 × 2,52 = 1.360 từ ✓. Không có cửa sổ bắt đầu sau 2006-08 trong lời/hình ("ran through the gentler 2000s and 2010s", S19.1 ✓). 3,1 % "not an expectation" (S30.3) ✓. "history, not a forecast" S03.3, S28.3, S32.1 ✓; US only S03.3, S32.1 ✓; CPI-U ≠ giỏ người về hưu S06.3, S31.1 ✓; ILLUSTRATIVE S03.2, S24.2, S27.1 + mọi khung ✓; "for 15 years" đã sửa thành "mostly yes" (S32.3) / "for most of the next 15 years" (G1:7) ✓.

## 4. Phát hiện

| # | Cấp | Chỗ | Lỗi | Sửa (nguyên văn) |
|---|---|---|---|---|
| 1 | **CHẶN** | `script.md:112` (S08.1), `:132–133` (S12.1–12.2); `beats.md:35` (B08), `:39` (B12) | "Crates" được định nghĩa ở S07.2 = cái **khoản tăng đầu tiên của Ruth** mua được. Khoản đều khởi đầu LỚN hơn (S08.3), nên tính theo đúng đơn vị đó nó mua **hơn** 6 (và hơn 9 ở năm 5) — số tiền khởi đầu không mô hình hoá, nên "about 6 of those crates" / "about 9 crates" là số không có nguồn, và cặp 9 vs 6 thùng cạnh nhau mời đọc "khoản tăng mua nhiều hơn" — đúng suy diễn "which pays more" bị cấm. S12.1 "got to her rising check's level" cùng lỗi (mức tuyệt đối). | S08.1 → *"Measured against its own first check, the bigger level check she turned down would buy about 6 in 10 today."* · S12.1 → *"Measured against its own start, the level check she turned down fell that far much sooner."* · S12.2 → *"By year 5, it was already down to about 9 in 10."* · B08 hình: hàng khoản đều tách riêng, nhãn *"10 = the level check's own first check"*, không đặt thẳng hàng/cùng cỡ với hàng của Ruth. B12 giữ nhãn hiện có (đã theo phần trăm của chính mình). Nêu 3 câu đổi trong G1 (§6.5). |
| 2 | **CHÍNH** | `script.md:90` (S04.3), `:234` (S31.3) | Hai câu phủ định vẫn chứa đúng cụm cấm "pays more money (in total)"; K-brief luật 3 (`K-brief.md:20`, terms "more money", "pays more", "total") sẽ bắt chúng ở C5 → CHẶN muộn. | S04.3 → *"So it can't compare the dollars the two checks pay out over a lifetime."* · S31.3 → *"And because annuity pricing isn't modeled, nothing here compares the dollars the two checks pay out over a lifetime."* |
| 3 | **CHÍNH** | `G1.md:32`; `script.md:9–33` | Kiểm máy báo "ĐẠT" vì chạy `--g1-short` trước G1; dòng in ra "chủ dự án đã duyệt ở G1" chưa đúng. Không cờ: TRƯỢT (độ dài). Luật mẫu (`check_script.py:12–13`) đòi WRITER mới thêm chất ≤ 2 vòng trước khi nêu ở G1 — chưa thử (chỉ còn là phương án b). | G1:32 → *"kiểm máy kịch bản (regex S10 của khoá này): ĐẠT mọi luật trừ độ dài — không cờ `--g1-short` là TRƯỢT (466 s < 495 s); cờ chỉ hợp lệ sau khi anh chọn (a). Vòng WRITER thêm chất trước G1 chưa chạy (= phương án b)."* · script.md:9 thêm sau "exit 0": *"(chạy trước G1; dòng 'đã duyệt' chỉ đúng khi G1 chọn (a); không cờ: TRƯỢT độ dài)"*. |
| 4 | **CHÍNH** | `G1.md:18–20` | Thiếu dòng nêu tên chỉ số trong ±5 % quanh ngưỡng (quality-framework §2.2): khối constraint S04.2–S04.3 dài **9,04 s** bắt đầu ở **60,32 s** — ngoài cửa sổ M4 chỉ 0,32 s; độ dài 466 s cách sàn `101` 8:00 (480 s) **2,9 %** (G1 chỉ nêu đích 8:15 = sàn + 15 s dư); mất chú ý 2/6 ×3 = **đúng** ngưỡng sửa ≥ 2/6. | Thêm sau G1:18: *"**±5 % quanh ngưỡng:** M4 — khối constraint S04.2–S04.3 dài 9,04 s bắt đầu 60,32 s, ngay ngoài cửa sổ 0:00–1:00 (nếu vào cửa sổ vẫn ≤ 10 s); độ dài 466 s thiếu 2,9 % so với sàn `101` 8:00 (đích 8:15 = sàn + 15 s dư sai số); mất chú ý 2/6 ở ba loại khối = đúng ngưỡng sửa (≥ 2/6), sửa bằng hình ở C3–C4."* |
| 5 | **CHÍNH** | `beats.md:19`; `K-brief.md:19` | K-brief luật 2 đề xuất mọi khung nêu sức mua mang "CPI-U" hoặc "US consumer prices"; nhãn góc cố định chỉ có "US only" + "History, not a forecast" → khung thùng B01, B07, B08, B25, B29, B32 sẽ trượt luật đó ở C5. | beats.md:19 đổi nhãn góc thành *"US consumer prices · US only"* + *"History, not a forecast"* trên mọi khung lịch sử. |
| 6 | PHỤ | `script.md:197` (S25.3) | "His raise helped" mang sắc đánh giá lựa chọn. | *"His raise slowed the loss, and it still left him with less than half."* |
| 7 | PHỤ | `script.md:211` (S28.1) | "is still losing ground" (tiếp diễn) có thể nghe như dự báo; số chỉ phủ 12 tháng qua. | *"And Ruth, at 85, lost more ground this past year."* |
| 8 | PHỤ | `script.md:73` (S02.2), `:143` (S13.1) | "every 20-year stretch / every starting month" — một tháng (10/2005) bị bỏ do ô CPI 10/2025 trống (715 = 716 − 1). Đã nêu ở mô tả (B31) — chấp nhận; bảo đảm thẻ V7 hoặc mô tả ghi "one start skipped: October 2025 CPI blank". | Thêm vào mô tả B31: *"One start month (October 2005) is skipped because October 2025 CPI is blank in the source."* |
| 9 | PHỤ | `G1.md:35` vs `ledger.md` | G1 "agent con 4/40, headless 21"; ledger có 3 agent con và 7 + 9 + 7 = **23** lượt headless. | Sửa G1:35 theo ledger (*"Agent con 3/40 (+ REVIEWER); headless 23 lượt"*) hoặc bổ sung dòng ledger còn thiếu. |
| 10 | PHỤ | `G1.md:19` | "v2 thêm đối trọng S30.5" ngụ ý đã khử câu khuyên của Opus; người đọc Opus/Haiku không chạy lại trên v2. | Thêm: *"(Opus/Haiku chưa chạy lại trên v2; hiệu quả S30.5 chưa đo.)"* |
| 11 | PHỤ | `G1.md:27` vs `hooks.md:47–49` | T2/T3 trong G1 khác danh sách tiêu đề của WRITER; T3 "Almost Never Kept Up" thiếu mốc và số (claim-risk.md:59 đòi "since the late 1940s" + số đếm). | Thống nhất một danh sách; nếu giữ T3: *"The 2% Annuity Raise That Almost Never Kept Up Since the 1940s"*. |
| 12 | PHỤ | `script.md:166` (S17.2) | "sunk to where the rising check would end" — cùng kiểu so mức như CHẶN-1, nhưng S17.3 ngay sau đã nói "against each check's own start". | Tuỳ chọn: *"…had already sunk to the share of its start where the rising check would end, by about year 8."* |
