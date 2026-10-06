# Ledger — Tập 4

Mỗi agent con, mỗi cổng: một dòng. Token = số harness của agent con.

| Ngày | Bước | Agent / việc | Model | Token | Kết quả |
|---|---|---|---|---|---|
| 2026-10-05 | Mở phiên | `verify.sh ep004` | lệnh | — | ĐẠT hết (LOCK a20c6878) |
| 2026-10-05 | Việc 0 | fetch + SHA | lệnh | — | 14/14 khớp hồ sơ tax-2; calc.py 34/34 khớp; câu diễn giải 24/24 True |
| 2026-10-05 | Việc 0 | kiểm độc lập (#1) | sonnet | 48.018 | 116/116 đại lượng chung trùng tuyệt đối; 3 chỗ mơ hồ (tên khoá min/max, hoà, stay null) không đổi số |
| 2026-10-05 | §6 tự quyết | thêm đại lượng hành trình (gain/cross/stay ở $200k/$300k) | — | — | việc 1 & 4 danh sách đóng (kỹ thuật mô hình cho phần hành trình); claim vào numbers.md, kiểm độc lập phủ |
| 2026-10-05 | ý đồ | REVIEWER #1 (cal-hook, C1) | opus | 86.079 | TRƯỢT cả hai → sửa đúng các dòng (bản 2) trước khi chạy |
| 2026-10-05 | hiệu chuẩn móc | 8 người đọc (Explore) | sonnet | 8 × ~31.6k = 252.934 | **ĐẠT** 7/8 (A 3/4, B 4/4; gốc ở X 4/4, ở Y 3/4) — sát ngưỡng, nêu tên |
| 2026-10-05 | C1 | 6 người đọc (Explore) | sonnet | 6 × ~31.9k = 191.137 | — |
| 2026-10-05 | C1 | người chấm độc lập | sonnet | 35.618 | T đúng 0/5 (G 1/1) → CHƯA ĐẠT (5/6 cờ khuyên "hỏi chuyên gia thuế"); hiểu 5/6; không vòng 2 — **việc ngoài §6**, nêu ở G1 (lý do `gates/C1-blind.md`) |
| 2026-10-05 | ý đồ | REVIEWER #1 (gọi lại: C2-intent + bản 2) | opus | 110.076 | bản 2 cal-hook + C1 ĐẠT; C2 máy TRƯỢT 6 dòng → check_script v2 |
| 2026-10-05 | C2 | WRITER bản 1 | opus | 179.048 | 1.231 từ; 3 móc; 2 ký hiệu mới |
| 2026-10-05 | §6.5 tự quyết | sửa giữ nghĩa để qua CHẶN | — | — | "minus"→"less" (S03.1, S06.2); "two of them"→"both" (S04.3); S08.1 thành câu hỏi (S10 ADVICE); S02.2 thêm "US only"; gắn claim còn thiếu; thêm claim `illustrative_price_*`, `metro_count` |
| 2026-10-05 | kiểm máy | check_script v3 | — | — | nới "like … average" từ theo câu sang theo cảnh SAU lần chạy đầu (luật theo câu ép lặp cụm từ; 5/6 người đọc C2 vòng 1 thấy nặng) — **việc ngoài §6**, xin duyệt ở G1 |
| 2026-10-05 | chọn móc | 9 người đọc so cặp vòng tròn | sonnet | 286.509 | H2 5/6, H1 3/6, H3 1/6; tiêu đề T1 6/6 (tham khảo) |
| 2026-10-05 | C2 v1 | 6 người đọc + người chấm | sonnet | 209.601 + 40.712 | đúng 5/6, khuyên 1/6 → trượt |
| 2026-10-05 | C2 v2 | WRITER gọi lại ×2 (sửa + beats) | opus | 189.715 + 194.859 | S01 = H2; đối trọng; bớt lặp |
| 2026-10-05 | C2 v2 | 6 người đọc + người chấm | sonnet | 207.976 + 39.579 | đúng 6/6, khuyên 0/6, S18 5/6 → dự phòng V7 (§6.7) |
| 2026-10-05 | G1 | clip cold open | lệnh | — | 46,2 s (sau "paper profit"); tổng 821 ký tự EL (4 lần sinh S01, 1 S02); ASR thiếu "Glen" |
| 2026-10-05 | tổng P1 (trước REVIEWER G1) | 41 agent | — | **2.071.861** | + ngữ cảnh điều phối ≈ 0,4 triệu |
| 2026-10-05 | G1 | REVIEWER #2 | opus | 103.126 | TRƯỢT 7 dòng → sửa cả 7; §6.5 thêm S01.1 "paper profit" |
| 2026-10-05 | **tổng P1** | **42 agent** | — | **2.174.987** | + ngữ cảnh điều phối ≈ 0,4 triệu ⇒ ≈ 2,6 triệu (+ 84 % trần P1) |
| 2026-10-05 | G1 | **chủ dự án duyệt** | — | — | #3, L1b, H2, T1, C3; 2 việc ngoài §6 duyệt; trần tập 4,5 triệu (P2, P3 ≤ 1 triệu); `gates/G1-answer.md` |
| 2026-10-05 | sau G1 | thử tên ASR (4 tên × 2 seed) | lệnh | — | đều đạt → **Frank**; 936 ký tự EL |
| 2026-10-05 | sau G1 | §6.5 + lệnh G1: "Glen" → "Frank" (script, hooks, beats); clip cold open sinh lại | lệnh | — | 0 từ khoá mất; 170 ký tự EL; **tổng EL P1 1.927** |
| 2026-10-06 | P2 mở | merge `main` a291ef7 (nhà máy) vào ep004 | lệnh | — | `7c24f94`; `checks-k38` chưa có trên remote → C4 chờ |
| 2026-10-06 | C3 | dựng N1/N2 bằng nhà máy (agent mới) | opus | 177.913 | qc 12/12, 0 CHẶN; EL 1.157 ký tự; móc nạp ký hiệu +7/−3 |
| 2026-10-06 | C3 v1 | 6 người đọc (Explore) + người chấm | sonnet | 211.263 + ≈ 30k | nghĩa B08 2/2, B13 1/2, B14 0/2; khuyên 6/6 → trượt cả 3 |
| 2026-10-06 | C3 v2 | thêm nhãn (agent mới) | opus | 104.782 | qc 12/12; 0 EL |
| 2026-10-06 | C3 v2 | 7 người đọc (1 thay do sai đường dẫn) + người chấm | sonnet | 244.385 + ≈ 30k | nghĩa 6/6; khuyên 6/6 → cổng trượt theo luật; gói C3 → chủ dự án |
| 2026-10-06 | **tổng P2** | **21 agent** | — | **≈ 0,80 triệu** | + điều phối ≈ 0,2 triệu ⇒ ≈ 1,0 triệu (trần P2); REVIEWER gói C3 bỏ vì trần |
