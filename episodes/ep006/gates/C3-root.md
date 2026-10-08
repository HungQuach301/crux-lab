# C3 — kết quả cổng gốc N1 "hàng 10 thùng" (ý đồ: `gates/C3-root-intent.md`)

## Vòng 1 · 2026-10-08 · bốn đoạn 540p (`world/c3/out/*.mp4`, dải `review-c3/strips/`)
Người đọc headless có ảnh, 2 mỗi đoạn (`c3/root/`; khoá nhãn commit trước khi chấm); người chấm độc lập (A9).

| Đoạn | Nghĩa | Khuyên_tính | Đúng | Kết luận |
|---|---|---|---|---|
| s07-ruth | 2/2 | 2/2 | 0/2 | trượt |
| s24-carl | 2/2 | 2/2 | 0/2 | trượt |
| s27-edna | 2/2 | 2/2 | 0/2 | trượt |
| s29-three | 2/2 | 2/2 | 0/2 | trượt |

- Câu khuyên cùng một kiểu ở cả 8: "so khoản đều với khoản gắn lạm phát / COLA; đừng chỉ nhìn séc đầu". Người đọc **tưởng hàng thùng là khoản đều không đổi** (s07: "a payout that stays the same each month loses real purchasing power"): dải tắt tiếng không cho thấy séc **tăng 2 %/năm**. Một phần do nội dung (vai người đọc đang cầm báo giá hai phương án, như N1/N2 Tập 5).
- **Vòng 2 = sửa bằng hình:** thêm tấm séc lớn lên mỗi kỷ niệm (×1,02^k) cạnh hàng thùng tối dần (S07.1 "Her check grew, but prices grew more") — `world/c3/FIX-R2.md`.
- Dựng: verify OK cả 4 (F-2 WARN: tick SNR ~12 dB trên "ten"/"Ruth's" ở s24; nhãn "Edna" chồng 17,8 s ở s27); render 534 s (0,15 h). Headless: đọc 85.837 + chấm 10.340.

## Vòng 2 · 2026-10-08 · séc lớn lên ×1,02^k cạnh hàng thùng (`world/c3/FIX-R2.md`; dải `review-c3/strips-r2/`; người đọc mới `c3/root-r2/`)
| Đoạn | Nghĩa | Khuyên_tính | Đúng | Kết luận |
|---|---|---|---|---|
| s07-ruth | 2/2 | 0/2 | 2/2 | **ĐẠT** (dừng sớm) |
| s24-carl | 2/2 | 0/2 | 2/2 | **ĐẠT** (dừng sớm) |
| s27-edna | 2/2 | 0/2 | 2/2 | **ĐẠT** (dừng sớm) |
| s29-three | 2/2 | 1/2 | 1/2 | **trượt** (câu khuyên → trượt ngay, §5.6): "an inflation-adjusted or COLA option deserves serious weight" |
- Sửa bằng hình đổi kết quả khuyên 8/8 → 1/8; nghĩa giữ 8/8 (khoá nghĩa: không thấp hơn vòng 1). Câu khuyên còn lại bám vào ca xấu nhất Carl ở cảnh ba người.
- **Vòng 3 chỉ s29-three:** sửa bằng hình — ba hàng đặt trên một trục tháng bắt đầu (1949 · 1966 · 2006) để khác biệt đọc ra là **tháng bắt đầu**, không phải loại khoản (S29.3 "What differed was the month each one started"); séc cùng cỡ của ba người kèm nhãn sự thật "same check: +2% a year" (B29 đã có "same 2% raise").
- Dựng: verify OK ×4, render 535 s (0,15 h). Headless: đọc 85.053 + chấm 11.194.
