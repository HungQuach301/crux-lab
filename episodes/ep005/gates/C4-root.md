# C4 — cổng gốc animatic 540p · kết quả

Ý đồ: `gates/C4-root-intent.md`. Dải: `review-c4/strips/`; dữ liệu `c4/root-r1/` (2/nhịp), `c4/root-r1x/` (người thứ 3, chấm riêng), `c4/voiced-r1/` (chốt chặn có lời).

## Vòng 1
| Nhịp | Đúng | Kết luận | Lỗi |
|---|---|---|---|
| B02 S02 | 2/2 | ĐẠT | |
| B03 S03 | 1/3 | **TRƯỢT** | vạch 75 % đọc thành "vạch dịch/nhân đôi"; thiếu ba bước |
| N1 S06 | nghĩa 2/2 | ĐẠT (ngoại lệ C3: cờ khuyên tắt tiếng không xét) | |
| B07 S07 | 2/2 | ĐẠT | |
| B08 S08 | 0/2 | **TRƯỢT** | khuyên: "not a reason to rule out buying" |
| B11 S11 | 2/2 | ĐẠT | |
| B12 S12 | 2/2 | ĐẠT | |
| N2 S13 | nghĩa 2/2 | ĐẠT (ngoại lệ C3) | |
| B14 S14 | 0/2 | **TRƯỢT** | đọc thước đo thành trả hết/hoà vốn; so với lịch 90 kỳ không rõ |
| B16 S16 | 2/2 | ĐẠT | |
| B17 S17 | 1/3 | **TRƯỢT** | khuyên "buy only if I can hold a decade"; chỉ số "dips and recovers" |
| B18 S18 | 0/2 | **TRƯỢT** | (đáp án cũ còn thẻ "your plan" đã bỏ ở spine v2 → sửa đáp án trước vòng 2, ghi trong spans.json) |
**7/12 = 58 % < 80 % → TRƯỢT vòng 1.** Token: người đọc 285.396 + 23.765, người chấm 41.824 + 8.308.

## Chốt chặn có lời (chủ dự án, C3)
| Cảnh | Đúng | Khuyên_tính |
|---|---|---|
| S06 (N1) | 3/3 | 0/3 |
| S13 (N2) | 3/3 | 0/3 |
**ĐẠT → N1/N2 giữ, không quay lại C3.** Token 70.796 + 12.315.

## Vòng 2 (`world/c4/FIX-R2.md`; người đọc mới `c4/root-r2/`, người thứ 3 B17 `c4/root-r2x/`)
| Nhịp | Đúng | Kết luận | Ghi chú |
|---|---|---|---|
| B03 | 2/2 | **ĐẠT** | vạch 75 % riêng, ba bước đọc ra |
| B08 | 0/2 | TRƯỢT | nghĩa đúng; khuyên dạng mới: "đừng chờ tự hết ở 78 %, theo dõi và xin huỷ ở 80 %" (suy từ quyền ghi trên hình — loại A21 "tự suy") |
| B14 | 2/2 | **ĐẠT** | |
| B17 | 1/3 | TRƯỢT | 1 lẫn 112 tháng với lịch; 1 khuyên |
| B18 | 2/2 | **ĐẠT** | |
**Tổng sau vòng 2: 10/12 = 83 % ≥ 80 % → cổng gốc C4 ĐẠT.** Theo D-009 vẫn sửa B08, B17 (vòng 3, cuối) cùng các nhận xét đạo diễn lặp. Token: 119.082 + 11.985, chấm 21.361 + 6.425.

## Vòng 3 (`world/c4/FIX-R3.md`; người đọc mới `c4/root-r3/`, người thứ 3 `c4/root-r3x/`, chốt chặn có lời `c4/voiced-r3/`)
Vòng cuối cho B08/B17; cùng lượt sửa 7 nhận xét đạo diễn lặp ở cả hai lượt độc lập + lỗi khách quan → mọi nhịp có hình đổi được kiểm lại (khoá nghĩa).
| Nhịp | Vòng 3 | Tốt nhất trước | Kết luận |
|---|---|---|---|
| B02 | 1/3 (khuyên "chỉ mua nếu ở lâu") | 2/2 (v1) | **thấp hơn → tự loại** (hoàn chỗ đổi 0:22) |
| B03 | 2/2 | 2/2 | ĐẠT |
| N1 S06 | nghĩa 2/2 | — | ĐẠT (ngoại lệ C3) |
| B07 | 2/2 | 2/2 | ĐẠT |
| **B08** | **2/2** | 0/2 | **ĐẠT** (vòng 3) |
| B12 | 2/2 | 2/2 | ĐẠT |
| N2 S13 | nghĩa 2/2 | — | (ngoại lệ C3) |
| B16 | 2/2 | 2/2 | ĐẠT |
| **B17** | **2/2** | 1/3 | **ĐẠT** (vòng 3) |
| B18 | 1/3 | 2/2 (v2) | **thấp hơn → tự loại** (hoàn khung tổng kết) |
**Chốt chặn có lời vòng 3:** S06 3/3, khuyên 0/3 → ĐẠT; **S13 khuyên 2/3 → TRƯỢT** (v1 0/3). Dải S13 v2 và v3 gần như giống hệt (chỉ dời nhãn "60 months") → chênh lệch nhiều khả năng do mẫu nhỏ; vẫn áp luật ghi trước: hoàn chỗ đổi S13 về v2. Ba chỗ hoàn (B02 0:22, S13 quanh vạch 60, B18 khung tổng kết) mang lại nhận xét đạo diễn cũ → G2 nêu trước/sau (`review-g2/revert-*.mp4`) để chủ dự án chọn.
Token: người đọc 237.047 + 23.705 + 70.735, chấm 37.806 + 8.290 + 12.500.

## Sau khoá nghĩa (hoàn 3 chỗ về v2) — kết quả cuối C4
Dải hoàn khớp v2: B02 SSIM 0,976 · S13 0,983 · B18 0,997 (`review-c4/strips/strips.json` `lock`). B11 (mốc dịch do take S04/S15 mới) kiểm lại 2/2 (`c4/root-b11/`, 23.601 + 7.831 token).
**12/12 nhịp loại 1 đạt** (B08, B17 ở v3; B02, B18, S13 ở v2; còn lại v1–v3). Chốt chặn có lời S06 (v3) 3/3 · S13 (v1/v2) 3/3, khuyên 0.
