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
| 2026-10-06 | sau G1 | điều phối | phiên chính | áp lời chủ dự án S03.3, S12.3 (75 % = quy định Fannie Mae, theo giá trị hiện tại khi chủ vay yêu cầu, khác lịch luật) + S12.4 "that early bar" | — | check: S03 3 số mới (ngoại lệ, chữ chủ dự án) |
| 2026-10-06 | sau G1 | dựng | `voice_scenes.py --only S03,S12`, `table_read.py`, `s18_seeds.py` | sinh lại S03, S12; S18 seed 1006/1007 | — | EL 938 + 1.266; ASR 0 mất; M1 2,8 · M2 22,8 · M3 9,0 · **M4 9,71** · M5 29,2 s ĐẠT; S18 chọn seed 1006 |
| 2026-10-06 | chờ Mốc V | điều phối | phiên chính | merge `main` a870e80 (K3.9, LOCK d93276a4, kind `ltv-first-passage`) vào `ep005` | — | verify.sh ĐẠT |
| 2026-10-06 | chờ Mốc V | dựng | agent general-purpose | `contract.json` thật (K3.9); đổi tên người mua Owen/Grace/Victor (model, numbers, thẻ claim); checks LOCK mới | 164.885 | rename_check PASS (104 khoá, 68 trùng, 36 người mua trùng giá trị); checks: S01 PASS 104/0, S03 PASS, S04 PASS, S05 PASS 78/78 trên claims thử (chưa có claims.json thật), F11 FAIL (28 artefact chưa dựng), 85 MISSING (cần video/trang) |
| 2026-10-06 | chờ Mốc V | REVIEWER | agent general-purpose | R1 không nêu số tiền phí PMI (lời + nhãn hình + tiêu đề) | 65.970 | 0 vi phạm (`gates/REVIEW-R1.md`) |
| 2026-10-07 | B+2 S03 | điều phối | phiên chính | merge `main` 16d7e1f (Mốc V); áp diff `moc-v/b2/ep005-S03.diff` ("a waiting period" + nhãn); check_script bỏ qua `label:` | — | numbers_said S03 2 số mới ĐẠT |
| 2026-10-07 | B+2 S03 | dựng | `voice_scenes.py --only S03`, `table_read.py` | sinh lại S03 | — | EL **443**; ASR 0 mất; M1 2,8 · M2 22,8 · M3 9,0 · **M4 9,8** · M5 29,0 s ĐẠT (ước bằng chữ 10,4 — dùng số đo thật, §3.9) |
| 2026-10-07 | B+2 S03 | kiểm mù | headless 6 + người chấm ×2 | đoạn S03 → S12 | 45.965 + 16.247 + 16.666 | 6/6, khuyên 0 (chấm lại vì thiếu định nghĩa), 2 năm 6/6 → ĐẠT |
| 2026-10-07 | C3 | dựng | agent general-purpose | spine v2 cả tập, cold open E5k port, N1/N2/N3, clip C3 | 330.196 | verify 0 vi phạm; sync 25/25; render 0,10 h; EL 0 |
| 2026-10-07 | C3 | kiểm mù | headless có ảnh | cổng gốc vòng 1 (6 + chấm) | 70.080 + 13.886 | nghĩa 6/6; N3 ĐẠT; N1, N2 khuyên 2/2 |
| 2026-10-07 | C3 | dựng | agent general-purpose (mới) | sửa N1/N2 vòng 2 bằng hình | 173.397 | render ≈ 0,07 h |
| 2026-10-07 | C3 | kiểm mù | headless có ảnh | vòng 2 (5 + chấm ×2) | 58.099 + 22.269 | N1 0/3, N2 0/2 |
| 2026-10-07 | C3 | kiểm mù | headless có ảnh | cold open E1/E2 kiểm lại | 47.735 + 10.038 | 4/4, khuyên 0 |
| 2026-10-07 | C3 | dựng | agent general-purpose (mới) | sửa N1/N2 vòng 3 (hình + nhãn) | 146.806 | render ≈ 0,05 h |
| 2026-10-07 | C3 | kiểm mù | headless có ảnh | vòng 3 (5 + chấm ×2) | 58.465 + 17.280 | N1 1/3, N2 0/2 → hết 3 vòng, chủ dự án chọn |
| 2026-10-07 | C3 | REVIEWER | agent general-purpose | soát gói C3 + chữ trên hình clip (R1) | 126.041 | ĐẠT có sửa (6 sửa đã áp); R1 0; không CHẶN |
| 2026-10-07 | sau C3 | dựng | agent general-purpose | N1 thêm đối trọng | 96.721 | không đè nhãn; render 38 s |
| 2026-10-07 | sau C3 | dựng | agent general-purpose | F-5 ghép đoạn thế giới vào master | 130.766 | test 5/5, bộ 36/36 |
| 2026-10-07 | sau C3 | dựng | agent general-purpose | F-2 kiểm sfx + nhãn đè | 148.603 | test 5/5, bộ 41/41; Tập 5 0 BLOCK, cảnh báo N3 dày sfx, 5 nhấn 11–14 dB |
| 2026-10-07 | sau C3 | dựng | agent general-purpose | F-3 nhạc theo bản đồ căng | 184.391 | 9,0 LU yên→đỉnh; A07 20,01 dB; né 1–4 kHz 9,2 dB (đích 13); chốt ở "removed" S20.2 |
| 2026-10-07 | sau C3 | dựng | agent general-purpose | F-1 thử "fly" ở S02 | 165.942 | đạt mọi tiêu chí; render ×1,015; ống góc rộng làm nghiêng nhà (mắt) → giới hạn méo ở C4 |
| 2026-10-07 | C4 | dựng (lời) | `story/seed_check.py`, `story/asr_all.py` | ASR medium từng từ cả 20 cảnh | — | S04.2 take 1005 rơi "the lender if" (1006 cũng rơi) → seed 1007; S15 "Grace bought"→"gray spot" → seed 1006; EL 406 + 406 + 302 + 302 = **1.416** |
| 2026-10-07 | C4 | chẩn đoán | 2 agent đạo diễn độc lập (A, B) | animatic 540p | 136.388 + 161.371 | A: cảm xúc 2 · truyện 3 · hình 3 · nhịp 3; B: 3·3·3·3; 6 nhận xét lặp ở cả hai → sửa |
| 2026-10-07 | C5 | điều phối + dựng (lời) | phiên chính, `story/seed_check.py S05 1005` | S09 (a) chủ dự án duyệt: S05.1 thêm "in dollars of the day"; sinh lại S05 | — | EL **256**; ASR medium khớp từng từ |
| 2026-10-08 | C5b | dựng | agent general-purpose (vòng sửa C5) | S07/S08 sổ claim (+35 claim hằng/dẫn xuất/trục), S09 nhãn gốc cấp khung + lời S05.1, S10 nhãn lựa chọn, S14→không mid-roll (chủ dự án 08/10), S17 "on paper", V03/V08/V09/V11/V12, Shorts xếp chữ dọc, thumbnail; 3 lượt render 1080p (vòng 3 = bản giao) | — | checks run-c5b: CHẶN 35/35, CHÍNH 9/11 (F07 quyết định chủ dự án, V11 chỉ còn dương tính giả có nền), Tập ĐẠT; EL 0 (take S05 do điều phối sinh) |
