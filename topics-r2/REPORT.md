# topics-r2 — báo cáo vòng 2 (Mốc 3 v2)

Thẩm quyền: `decisions/D-004.md`. Thiết kế ghi trước: `DESIGN.md`. Đóng băng `b0b1e1f` trước mọi kiểm. Key SHA-256 `f8f9c830…` commit trước khi chấm, `key.json` commit sau khi nhận mã — SHA khớp. Bảng AI niêm phong `c042120`.

**Biến đổi so với vòng 1 (đúng một):** chủ dự án chọn đúng 9/18 thẻ thay cho thang 5.

## Kết luận — chủ dự án chốt (2026-10-04): **ĐẠT theo giá trị** (D-004 sửa đổi 1)

Chủ dự án đọc CHẶN theo giá trị: V3 12/12 (ba hồ sơ chỉ lệch định dạng ngày, có bằng chứng). Vòng 2 là **vòng đạt 1/2**; vòng 3 là vòng xác nhận, biến duy nhất: V3 so ngày đã chuẩn hoá; thêm V6 ở mức THAM KHẢO; chuẩn hồ sơ gắn sau đóng băng. Bảng dưới giữ nguyên số liệu lúc gửi gói.


| Cấp | Chỉ số | Ngưỡng | Kết quả | |
|---|---|---|---|---|
| CHÍNH-1 | Thẻ máy được chọn | ≥ 6/12 | **7/12 = 58,3 %** | đạt |
| CHÍNH-2 | Tỉ lệ chọn máy − đối chứng | ≥ +20 điểm | 58,3 % − 2/6 = 33,3 % → **+25 điểm** | đạt |
| CHẶN | Hồ sơ máy hợp lệ | ≥ 10/12 | **9/12 theo luật khoá** · 12/12 nếu so theo giá trị | **trượt (luật khoá)** |

- **Theo luật khoá: vòng 2 KHÔNG ĐẠT** vì CHẶN. Ba hồ sơ (debt-2, debt-3, debt-4) trượt V3 **chỉ vì cách viết ngày**: hồ sơ ghi `2006-08-01`, agent V3 ghi `2006-08` (cùng tháng); `close()` so chuỗi chính xác. Mọi giá trị số đều khớp. Luật không sửa sau khi thấy kết quả; cách đọc nào áp dụng là quyết định của chủ dự án.
- **Nếu tính theo giá trị (12/12): vòng 2 ĐẠT** — vòng đạt đầu tiên (cần 2 vòng liên tiếp).
- **Cửa sổ ±5 %:** không chỉ số nào sát ngưỡng (m = 7, không phải 6).
- **Xác suất ngẫu nhiên (ghi trước):** chọn 9/18 ngẫu nhiên cho m ≥ 7 với xác suất ≈ 31 %. m = 7 là mức thấp nhất để đạt.
- **Điều kiện dừng D-004 §5:** vòng 2 máy **hơn** đối chứng → không đủ "2 vòng máy không hơn đối chứng". Theo luật khoá: 2 vòng không đạt (dừng hẳn khi 3).

## Chọn của chủ dự án

| Thẻ | Bên | Chọn | Giây | Tiêu đề |
|---|---|---|---|---|
| 01 | máy retire-2 | – | 99 | Help Your Kid Buy a Home Now or in 10 Years? |
| 02 | máy debt-1 | ✓ | 29 | 15-Year Mortgage or a 30-Year Paid in 15? The Real Price |
| 03 | máy debt-3 | ✓ | 67 | Stretching to 35% of Your Pay: How Long Until It's 28%? |
| 04 | đối chứng | – | 17 | Roth Conversion Window: Real or Mirage? |
| 05 | đối chứng | – | 4 | Old 401(k): IRA or New 401(k)? |
| 06 | máy tax-4 | – | 4 | Cash in a Roth IRA vs a Savings Account: Does Tax Matter? |
| 07 | máy tax-1 | – | 74 | TIPS in a Taxable Account: Still Inflation-Proof? |
| 08 | máy tax-2 | ✓ | 8 | $1,000 Emergency: Tap the 401(k) or Use the Card? |
| 09 | máy tax-3 | ✓ | 5 | Rental Losses on $130,000 of Wages: Still Deductible? |
| 10 | đối chứng | ✓ | 5 | Mortgage Recast vs Extra Principal |
| 11 | máy debt-2 | ✓ | 6 | 10% Down and Mortgage Insurance: How Long Did It Last? |
| 12 | đối chứng | – | 4 | Should You Bunch Charitable Giving? |
| 13 | máy retire-3 | – | 4 | Callable CD at 4.5% or a Locked 4%? We Replayed History |
| 14 | máy retire-4 | ✓ | 15 | Travel Early in Retirement or Wait? The Price Test |
| 15 | đối chứng | – | 3 | Dependent Care FSA or Child Care Credit? |
| 16 | máy debt-4 | ✓ | 8 | Waiting a Year for a Lower Car Loan Rate: Does It Pay Off? |
| 17 | máy retire-1 | – | 46 | Prepay Your Funeral or Save the Money? What History Says |
| 18 | đối chứng | ✓ | 6 | Lease Buyout or Finance the Next Car? |

- **Từng trụ:** vay nợ chọn **6/6** (máy 4/4, đối chứng 2/2); hưu trí 1/6 (máy 1/4, đối chứng 0/2); thuế 2/6 (máy 2/4, đối chứng 0/2). Trụ vay nợ giải thích phần lớn kết quả: chọn đủ trụ vay nợ đã cho 4 thẻ máy.
- **Chip lý do:** không có.
- **Thời gian (THAM KHẢO):** tổng 404 s (6 phút 44 giây), trung vị 7 s; nửa đầu 307 s, nửa sau 97 s (vẫn nhanh dần, như vòng 1). Lâu nhất: 01 (99 s), 07 (74 s), 03 (67 s), 17 (46 s) — ba trong bốn thẻ này không được chọn.
- **Ba thẻ được chọn mà trượt V3 theo luật khoá:** debt-2, debt-3, debt-4.

## Bảng AI tham khảo (6 vai, cùng ngân sách 9/18)

| Vai | Máy được chọn | Khớp với chủ dự án (/18) |
|---|---|---|
| chỉ tò mò | 9 | 12 |
| đang có lời mời refinance | 4 | 12 |
| sắp nghỉ hưu | 5 | 4 |
| mua nhà lần đầu | 6 | 14 |
| vay xe / nợ thẻ | 6 | 14 |
| làm tự do, lo thuế | 6 | 6 |

- 9 thẻ được bảng AI bầu nhiều nhất: 6 máy; khớp chủ dự án 12/18. Khớp tốt hơn vòng 1 (ngân sách làm hai bên cùng phải so sánh).
- Một vai chọn 8 thẻ ở lần đầu → gọi lại một lần theo luật sai khuôn (bản sai ở `panel-rejected/`).
- Chip AI lặp lại vòng 1: máy *not me* / *too narrow*; đối chứng *seen it* / *vague promise* / *not me*.

## Hợp lệ hồ sơ máy

V0, V1, V2, V4, V5: 12/12 đạt. V3: 9/12 theo luật khoá (debt-2, debt-3, debt-4 lệch cách viết ngày, số khớp). Phán trùng (agent mới): 0 trùng, 4 sát (giữ) — `dedup/verdict.json`. Mới lạ: 12/12 `answered-without-data`.

## Chỉ báo cáo: mới lạ của 12 thẻ đối chứng (không tính vào ngưỡng)

| Thẻ | Kết luận | Quyết định |
|---|---|---|
| r1-debt-c1 | answered-with-data | Refinance the 7% mortgage to 6.5%, or keep the loan? |
| r1-debt-c2 | answered-without-data | Take the 0% transfer with a 4% fee, or stay on the old card? |
| r1-retire-c1 | answered-without-data | Should you pause 401(k) contributions beyond the match to pay cards faster? |
| r1-retire-c2 | answered-with-data | Should you claim Social Security early or wait? |
| r1-tax-c1 | answered-with-data | Should you spend 529 money before claiming a college tax credit? |
| r1-tax-c2 | answered-with-data | Should you make pre-tax Solo 401(k) contributions instead of Roth contributions? |
| r2-debt-c1 | answered-without-data | Should you ask the lender for a recast or just pay extra principal? |
| r2-debt-c2 | answered-with-data | Should you buy out the lease or turn it in and finance another car? |
| r2-retire-c1 | answered-with-data | Should you roll the old 401(k) into an IRA or the new 401(k)? |
| r2-retire-c2 | answered-with-data | Should you convert pre-tax IRA money to Roth IRA before retirement? |
| r2-tax-c1 | answered-with-data | Use the dependent care FSA or skip it and claim the child care credit? |
| r2-tax-c2 | answered-with-data | Bunch donations this tax year or spread gifts as usual? |

- **answered-with-data: 9/12 = 75 %** (vòng 1: 4/6; vòng 2: 5/6). Hồ sơ máy giữ lại: 0/24 (máy tự loại các ý tưởng `answered-with-data` ngay lúc sinh — một phần trong 37 + 36 ứng viên bị loại ở hai vòng). Lưu ý: kiểm trên thẻ đối chứng do agent khác làm sau khi chấm; độ nghiêm có thể khác agent sinh.
- Thẻ đối chứng chủ dự án ưa thích cũng có đáp án dữ liệu sẵn: vòng 1 thẻ 5 điểm (refinance, r1-debt-c1) và vòng 2 thẻ được chọn r2-debt-c2 (lease buyout); r2-debt-c1 (recast) là `answered-without-data`.
- Đọc: đối chứng cho ý tưởng người xem nhận ra ngay, nhưng 3/4 đã có người trả lời bằng dữ liệu; máy lọc được điều này. Đây là bằng chứng cho giá trị máy ở khâu kiểm mới lạ (DESIGN §b).

## Sinh và chi phí

- Máy: 3 agent, 48 ứng viên, loại 36 (debt 12/16, retire 12/16, tax 12/16 — `machine/*-discards.md`). Lần mở đầu bị dừng sau vài giây vì lệnh lỡ thêm một câu gợi ý ngoài thiết kế; chạy lại sạch (`PLAN.md`).
- Đối chứng: GPT-5.5, 3 lệnh, 6/6 đạt khuôn ở lệnh đầu, ~5,9 nghìn token (< 0,1 USD).
- Agent con: máy ~626 nghìn token (30 phút), V3 ~666 nghìn, bảng AI ~355 nghìn, phán trùng ~49 nghìn, mới lạ đối chứng (xem trên). Phút của chủ dự án: chọn 6 phút 44 giây.

## Bước 2

7 thẻ máy được chọn → hồ sơ ≤ 5 dòng: https://claude.ai/artifact/QYcBDBJwSkbDhaeucsxr9a (`step2/`). Chủ dự án chọn **Có 7/7** (`step2/step2-code.txt`) → `topics/queue.md` dòng 13–19 (cột "Vòng" = 2, đường dẫn đầy đủ `topics-r2/…`).

## Đề xuất MỘT biến cho vòng 3 (ghi trước; chưa chạy)

**Sửa bộ đo V3: so ngày theo tháng/ngày đã chuẩn hoá** (`YYYY-MM` ≡ `YYYY-MM-01`), không đổi gì khác. Lý do: vòng 2 trượt CHẶN chỉ vì cách viết ngày, không vì số sai; bộ đo đổi qua chủ dự án duyệt (CHARTER §7.1). Nếu chủ dự án tính vòng 2 theo giá trị (12/12 → ĐẠT), vòng 3 là vòng xác nhận: đạt lần nữa thì qua (xác suất ngẫu nhiên cho cả hai vòng ≈ 9,6 %).
