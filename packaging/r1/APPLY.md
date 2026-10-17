# APPLY — áp gói R1 trên YouTube Studio (chủ dự án làm; phiên không đổi gì trên YouTube)

Thứ tự theo kế hoạch đo `packaging/R1.md` §4: **ghi baseline trước → PMI + Test & Compare → Tập 9 khi đăng → các video khác cách ≥ 3 ngày**. Tập 3 **không đụng** tới 01/11 (đối chứng). Ảnh: `packaging/r1/final/` (JPEG 1280×720, < 200 KB, đạt giới hạn 2 MB của YouTube). Tờ duyệt: `packaging/r1/DUYET-AI.md`.

Tên tệp ảnh: `<tập>-<#>-ai<x>.jpg` = phương án AI #1–#3 (đề nghị #1 mặc định); `<tập>-0-ma<X>.jpg` = đối chứng dựng bằng mã.

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
4. **Thumbnail → Test & Compare** → tải lên 3 ảnh: `ep005-1-aia.jpg`, `ep005-2-aid.jpg`, `ep005-3-aic.jpg` (hoặc thay #3 bằng `ep005-0-maA.jpg` nếu muốn thử AI vs mã). Bắt đầu thử. Không dừng tay; YouTube báo kết quả (theo tỉ lệ thời gian xem) sau tối đa ~2 tuần.
5. **Save.** Ghi giờ đổi vào `packaging/r1/baseline-<ngày>.md`.

## Bước 2 — Tập 9, ngày đăng (sau M6)

1. **Trước khi đăng:** đối chiếu số với `episodes/ep009/numbers.md` bản sau M6: 155/307 (tiêu đề), 49,5 % (ảnh). Số đổi → báo phiên để sửa chữ trên ảnh (`packaging/r1/ai/final.py`, 1 lệnh, không tạo lại hình).
2. **Title:** `Rent and Invest vs Buy: Renter Ahead in 155 of 307 Months`
3. **Thumbnail → Test & Compare:** `ep009-1-aia.jpg`, `ep009-2-aib.jpg`, `ep009-3-aif.jpg`.
4. Mô tả theo gói M6 của tập (ghi công Origami, nguồn French).

## Bước 3 — Tập 7 và Tập 8, ≥ 3 ngày sau Bước 1

| Video | Title | Test & Compare |
|---|---|---|
| `p78Ca1OHTgM` | `15 Year vs 30 Year Mortgage Paid in 15: $120 a Month More` | `ep007-1-aia.jpg`, `ep007-2-aid.jpg`, `ep007-3-aib.jpg` |
| `26SfSIDPpzk` | `Is Renting a Waste of Money? Buying Led in 3 of 4 Months` | `ep008-1-aib.jpg`, `ep008-2-aia.jpg`, `ep008-3-aic.jpg` |

Dòng 1 mô tả Tập 8 (gợi ý): `In about 3 out of 4 of 307 start months since 1991, the twin who bought ended ten years ahead of the twin who rented — and the answer moved with the month and the rent you assume. History, not a forecast.`

## Bước 4 — Tập 1, 2, 6, ≥ 3 ngày sau Bước 3

| Video | Title | Test & Compare |
|---|---|---|
| `OEVfD-ywzLc` | `Should I Refinance? A $115,000 Loan Needed a 1.12-Point Cut` | `ep001-1-aic.jpg`, `ep001-2-aia.jpg`, `ep001-3-aid.jpg` |
| `-AwfRUE6UTI` | `Private Student Loans: Fixed or Variable? Since 1954` | `ep002-1-aic.jpg`, `ep002-2-aia.jpg`, `ep002-3-aib.jpg` |
| `dn6-0g2RvD0` | `Annuity With a 2% Raise: It Kept Up in 17 of 715 Stretches` | `ep006-1-aic.jpg`, `ep006-2-aia.jpg`, `ep006-3-aie.jpg` |

Dòng 1 mô tả Tập 1 (bắt buộc — tiêu đề có số kèm điều kiện): `"Needed" means the fees come back within three years: Walt (illustrative) has a $115,000 loan and a $3,667 bill, so his rate has to fall 1.12 points; Nora's $375,000 loan needs half a point.`

## Bước 5 — Short (sau khi phiên dựng bản cắt; chưa dựng)

Mỗi ngày tối đa 1 Short, Related video = video dài của tập; móc mới 2 Short cũ trước (`packaging/R1.md` §3a). Đăng lại Short đã có = tải bản mới, không xoá bản cũ trước khi có số so sánh.

## Bước 6 — Đo

- **01/11:** chép lại bảng Bước 0 (cùng chỉ số) → `packaging/r1/do-0111.md`; đọc kết quả Test & Compare PMI; Tập 3 đổi tiêu đề sau mốc này nếu chủ dự án muốn.
- **06/11:** lần 2 → `do-0611.md`; quyết theo ngưỡng ghi trước: **CTR ≥ 3 %** trên ≥ 100 lượt hiển thị → giữ; < 2 % trên ≥ 300 → đổi sang T2; < 100 lượt hiển thị → chưa kết luận. Video mới: lượt hiển thị về **hàng trăm** (≥ 300 trong 7 ngày). Short: xem trung bình ≥ 15 s.

Không làm: đổi nhiều video cùng ngày; dừng Test & Compare sớm; sửa tiêu đề lần hai trước 01/11.
