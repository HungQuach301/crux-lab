# Ledger — Tập 5 (ep005)

Mỗi dòng: một agent con hoặc một lô headless. Loại việc: kiểm mù · dựng · WRITER · REVIEWER · checks · điều phối · dự phòng (`episode.md` §8).

| Ngày | Cổng | Loại việc | Ai / lệnh | Việc | Token | Kết quả |
|---|---|---|---|---|---|---|
| 2026-10-06 | Việc 0 | dựng | agent general-purpose | fetch FRED (SHA khớp hồ sơ), model.py, statements 17/17, numbers.md, debt-2 model.json/statements.json | 131.754 | XONG; rủi ro tháng lãi mới nhất (2026-09 đủ tuần, không phải 2026-10 một tuần) |
| 2026-10-06 | C1 | kiểm mù | headless 6 người đọc + 1 người chấm | L1, L2 × (2 T + 1 G) | 40.294 | L1 2/2, L2 2/2, cờ 0 → L2 |
| 2026-10-06 | Việc 0 | checks | agent general-purpose (độc lập, không đọc model.py) | tính lại từ định nghĩa numbers.md | 72.315 | 55/55 khớp; làm rõ 3 định nghĩa (luật hoà người mua nhanh, tập B ≥ 120, ngưỡng điểm giữa) |
| 2026-10-06 | C2 | WRITER | agent general-purpose | kịch bản v1, hooks H-A/B/C, beats, check_script | 183.104 | 20 cảnh ≈ 8:22, check ĐẠT |
| 2026-10-06 | C2 | REVIEWER | agent general-purpose | chọn móc + soát kịch bản (`REVIEW-C2.md`) | 120.880 | H-A; ĐẠT có sửa (5 CHẶN → 4 sửa lời + nguồn) |
| 2026-10-06 | C2 | điều phối | phiên chính | áp nguyên văn 4 sửa lời REVIEWER (S02.1, S05.1, S10.1, S10.5) | — | check ĐẠT |
| 2026-10-06 | C2 | dựng (Việc 0 bổ sung) | agent general-purpose | nguồn luật PMI (4902(a), CFPB, điều lệ Fannie/Freddie), claim mới (tháng chậm, đường chỉ số Victor) | 117.169 | ĐẠT; nguồn gốc mốc 75 %/2 năm **CHỜ** (fanniemae/freddiemac bị proxy chặn) |
| 2026-10-06 | C2 | dựng | `story/table_read.py` (lệnh) | đọc thử S01–S04, EL Eric eleven_v3 | — | EL 1.234 + 410 ký tự; v1 M4 10,08 s TRƯỢT |
| 2026-10-06 | C2 | WRITER | agent general-purpose (mới) | sửa S03.3 (M4, "wait"→ASR) | 53.012 | v2 M1 2,8 · M2 22,8 · M3 9,0 · M4 9,41 · M5 29,3 s ĐẠT |
| 2026-10-06 | C2 | kiểm mù | headless 6 + 1 người chấm (9 nhãn) | vòng 1 | 53.369 + 24.744 | 6/6, khuyên 0; S19 4/6 mất chú ý → TRƯỢT, dự phòng |
| 2026-10-06 | C2 | kiểm mù | 3 agent `Explore` (so) | cùng mẫu | ≈ 108.054 | 3/3, khuyên 0; mất chú ý S10 3/3 |
| 2026-10-06 | C2 | WRITER | agent general-purpose (mới) | vòng 2: S19 → 1 câu + V7 + mô tả; S07.2, S09.3, S12.2–3, S17.3, S18.2 | 74.724 | check ĐẠT, ≈ 8:19 |
| 2026-10-06 | C2 | kiểm mù | headless 6 mới + 1 người chấm | vòng 2 | 56.363 + 17.586 | 6/6, khuyên 0, S18 3/6 → ĐẠT |
| 2026-10-06 | G1 | REVIEWER | agent general-purpose | soát gói G1 (`REVIEW-G1.md`) | 98.909 | ĐẠT có sửa, 8 sửa chữ đã áp |
| 2026-10-06 | sau G1 | dựng | `story/voice_scenes.py` (lệnh) | lời theo cảnh S05–S11, S13–S20 (S01/S02/S04 từ cache; S03, S12 giữ chờ câu 75 %) | — | EL **4.887** ký tự (cả tập 6.531/6.000, +9 %, nêu tên); 18 cảnh 367 s; ASR từ khoá 17/18 — S18.5 "illustrative" nghe "illustrated" (medium.en p 0,49) |
