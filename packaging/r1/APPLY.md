# APPLY — áp gói R1 trên YouTube Studio (chủ dự án làm; phiên không đổi gì trên YouTube)

Thứ tự theo kế hoạch đo `packaging/R1.md` §4: **ghi baseline trước → PMI + Test & Compare → Tập 9 khi đăng → các video khác cách ≥ 3 ngày**. Tập 3 **không đụng** tới 01/11 (đối chứng). Ảnh: `packaging/r1/final/` (JPEG 1280×720, < 200 KB, đạt giới hạn 2 MB của YouTube). Tờ duyệt: `packaging/r1/DUYET-AI.md`.

Tên tệp ảnh: **vòng 2 (dùng cho Tập 1, 5, 6, 7, 8):** `<tập>-tc1..3.jpg` = bộ Test & Compare, tc1 = mặc định. **Tập 2, 9** (vòng 1): `<tập>-<#>-ai<x>.jpg` (#1 mặc định); `<tập>-0-ma<X>.jpg` = đối chứng dựng bằng mã.

## Bước 0 — Baseline (ngày bắt đầu, TRƯỚC mọi thay đổi; ≈ 5 phút)

Studio → **Analytics → Advanced mode** → tab **Content**, khoảng "Since published", chọn chỉ số **Impressions, Impressions click-through rate, Views, Average view duration** (+ "Traffic source" cho PMI). Chép vào `packaging/r1/baseline-<ngày>.md` (hoặc gửi ảnh chụp cho phiên sau chép):

| Video | ID | Impressions | CTR | Views | Avg view duration | Ghi chú |
|---|---|---|---|---|---|---|
| Tập 1 refi | `OEVfD-ywzLc` | | | | | |
| Tập 2 vay học | `-AwfRUE6UTI` | | | | | |
| Tập 3 EE (đối chứng) | `2ErffZBHggE` | | | | | không đổi tới 01/11 |
| Tập 5 PMI | `1o-2RJ-DdfE` | | | | | + nguồn: search / suggested / browse |
| Tập 6 annuity | `dn6-0g2RvD0` | | | | | |
| Tập 7 15/30 | `p78Ca1OHTgM` | | | | | |
| Tập 8 rent/buy | `26SfSIDPpzk` | | | | | |
| Short PMI | `vCExC7CoImY` | — | — | | | + "Viewed vs swiped away" |
| Short 15/30 | `Lj6PBFl5tDI` | — | — | | | + "Viewed vs swiped away" |

## Bước 1 — PMI (Tập 5), cùng ngày baseline

1. Studio → **Content** → `1o-2RJ-DdfE` → **Details**.
2. **Title:** `When Does PMI Go Away With 10% Down? 8 Years by Schedule`
3. **Description, dòng 1** (giữ phần còn lại): `On the payment schedule the law uses, a 10% down loan reaches the point where you can ask to cancel PMI after about 8 years (payment 99); by home prices, it got to 80% on paper in a typical 23 months — on paper is not the same as removed.`
4. **Thumbnail → Test & Compare** → tải lên 3 ảnh **vòng 2**: `ep005-tc1.jpg` (PMI FOR 8 YEARS?), `ep005-tc2.jpg` (PMI FOR 8 YEARS?), `ep005-tc3.jpg` (ON PAPER? 23 MONTHS — giữ để đo số lệch/khớp tiêu đề). Bắt đầu thử. Không dừng tay; YouTube báo kết quả (theo tỉ lệ thời gian xem) sau tối đa ~2 tuần.
5. **Save.** Ghi giờ đổi vào `packaging/r1/baseline-<ngày>.md`.

## Bước 2 — Tập 9, ngày đăng (sau M6)

1. **Trước khi đăng:** đối chiếu số với `episodes/ep009/numbers.md` bản sau M6: 155/307 (tiêu đề), 49,5 % (ảnh). Số đổi → báo phiên để sửa chữ trên ảnh (`packaging/r1/ai/final.py`, 1 lệnh, không tạo lại hình).
2. **Title:** `Rent and Invest vs Buy: Renter Ahead in 155 of 307 Months`
3. **Thumbnail → Test & Compare (vòng 4, 18/10 — chữ khớp số tiêu đề):** `ep009-tc1.jpg` (đồng xu, COIN FLIP? 155–152, mặc định), `ep009-tc2.jpg` (bập bênh, 155–152), `ep009-tc3.jpg` (đồng xu, COIN FLIP? 49.5% — bản cũ, giữ để đo). Bộ vòng 1 `ep009-1/2/3-ai*.jpg` thay thế.
4. Mô tả theo gói M6 của tập (ghi công Origami, nguồn French).

## Bước 3 — Tập 7 và Tập 8, ≥ 3 ngày sau Bước 1

| Video | Title | Test & Compare |
|---|---|---|
| `p78Ca1OHTgM` | `15 Year vs 30 Year Mortgage Paid in 15: $120 a Month More` | `ep007-tc1.jpg`, `ep007-tc2.jpg`, `ep007-tc3.jpg` (15 OR 30?) |
| `26SfSIDPpzk` | `Is Renting a Waste of Money? Buying Led in 3 of 4 Months` | `ep008-tc1.jpg` (RENT = WASTED?), `ep008-tc2.jpg` (WORST CASE -$82,385), `ep008-tc3.jpg` (RENT = WASTED?) |

Dòng 1 mô tả Tập 8 (gợi ý): `In about 3 out of 4 of 307 start months since 1991, the twin who bought ended ten years ahead of the twin who rented — and the answer moved with the month and the rent you assume. History, not a forecast.`

## Bước 4 — Tập 1, 2, 6, ≥ 3 ngày sau Bước 3

| Video | Title | Test & Compare |
|---|---|---|
| `OEVfD-ywzLc` | `Should I Refinance? A $115,000 Loan Needed a 1.12-Point Cut` | `ep001-tc1.jpg` (RATE DROP NEEDED: 1.12), `ep001-tc2.jpg` (WORTH IT? $5,124 IN FEES), `ep001-tc3.jpg` (FEES BACK? MONTH 30) |
| `-AwfRUE6UTI` | `Private Student Loans: Fixed or Variable? Since 1954` | `ep002-1-aic.jpg`, `ep002-2-aia.jpg`, `ep002-3-aib.jpg` |
| `dn6-0g2RvD0` | `Annuity With a 2% Raise: It Kept Up in 17 of 715 Stretches` | `ep006-tc1.jpg` (minh hoạ), `ep006-tc2.jpg` (nền nghiêm/thực tế) — BUYING POWER LOSES 19%?; `ep006-tc3.jpg` (STILL BUYS 80.7%) |

Dòng 1 mô tả Tập 6 (**bắt buộc** khi dùng ảnh "LOSES 19%?"): `In the typical 20-year stretch since 1947, an annuity check rising 2% a year ended up buying 80.7% of what its first check bought — about 19% of its buying power lost to US consumer prices. History, not a forecast.`

Dòng 1 mô tả Tập 1 (bắt buộc — tiêu đề có số kèm điều kiện): `"Needed" means the fees come back within three years: Walt (illustrative) has a $115,000 loan and a $3,667 bill, so his rate has to fall 1.12 points; Nora's $375,000 loan needs half a point.`

## Bước 5 — Short (sau khi phiên dựng bản cắt; chưa dựng)

Mỗi ngày tối đa 1 Short, Related video = video dài của tập; móc mới 2 Short cũ trước (`packaging/R1.md` §3a). Đăng lại Short đã có = tải bản mới, không xoá bản cũ trước khi có số so sánh.

## Bước 6 — Đo

- **01/11:** chép lại bảng Bước 0 (cùng chỉ số) → `packaging/r1/do-0111.md`; đọc kết quả Test & Compare PMI; Tập 3 đổi tiêu đề sau mốc này nếu chủ dự án muốn.
- **06/11:** lần 2 → `do-0611.md`; quyết theo ngưỡng ghi trước: **CTR ≥ 3 %** trên ≥ 100 lượt hiển thị → giữ; < 2 % trên ≥ 300 → đổi sang T2; < 100 lượt hiển thị → chưa kết luận. Video mới: lượt hiển thị về **hàng trăm** (≥ 300 trong 7 ngày). Short: xem trung bình ≥ 15 s.

Không làm: đổi nhiều video cùng ngày; dừng Test & Compare sớm; sửa tiêu đề lần hai trước 01/11.
