# C2 — Kết quả kiểm máy + kiểm mù lời (ý đồ: `gates/C2-intent.md`)

## Vòng 1 · 2026-10-08 · kịch bản v1 (WRITER, Ruth dẫn đường, móc H-B)
- **(a) Máy:** `story/check_script.py` ĐẠT (claim 100 %, S10 0, "US only", "history, not a forecast", ASR, mật độ, mid-roll ≈ 3:09). 1.305 từ nói → ước **8:37** (2,52 từ/s). Khuôn: hook +1,9 · khái niệm +2,8 · thí nghiệm +0,3 · người −3,0 · giới hạn −1,9 điểm.
- **(b) Kiểm mù (`c2/r1/`, 6 Sonnet + 1 người chấm):** đúng **6/6**, câu khuyên **0/6**; khối mất chú ý **số dày 6/6** (S19–S20 thập kỷ 94,8 % / 99,5 % — 3/6; S22–S23 CPI-W / PCE 19,2 % so "none since 1959" — 3/6) → **TRƯỢT** ngưỡng "không loại khối nào ≥ 4/6".
- **Người đọc model khác (không tính ngưỡng):** Opus — đúng, **khuyên 1** (câu 6, tự ghi "outside the video: … a CPI-linked option … may be worth pricing"; kiểu `advice_inferred` của A21), khối số dày (PCE); Haiku — đúng, khuyên 0, không mất chú ý. **Lệch so với 6 Sonnet:** cờ khuyên (Opus) → nêu ở G1.
- **Dự phòng ghi trước:** khối số dày → 1 câu lời + nhãn hình / thẻ V7 / mô tả; WRITER MỚI (vòng 2).

## Móc đo trên bản đọc thật (ElevenLabs Eric `eleven_v3`, `story/table_read.py`, S01–S04)
M1 **3,6** · M2 **27,5** · M3 **13,9** · M4 **6,06** · M5 **33,3** · M6 **0** (không lời hứa nhân vật) s → ĐẠT cả 6. ASR khớp chữ (small.en). Clip lời cold open 47,2 s: `review-g1/cold-open.m4a`. EL 1.114 ký tự.
**Hiệu chuẩn M4 ở 2,75 từ/s:** Tập 6 ước 7,0 s / đo 6,06 s (ước cao 0,9 s); Tập 5 (mẫu `check_script.py` chạy lại trên `ep005/story/script.md`) ước **13,5 s TRƯỢT** / đo 9,8 s — bộ ước gộp khối qua ident 3 s (S03.5 + S04.1); cắt khối ở khoảng lặng > 1,5 s như `table_read.py` → ước 9,1 s (thấp 0,7 s). Kết luận: hằng 2,75 giữ; định nghĩa khối của bộ ước cần cắt ở khoảng lặng > 1,5 s (đề xuất sửa mẫu, chưa áp); sai số còn ±1 s → M4 ước ≥ 9,0 s phải đo bản đọc thật.

## Vòng 2 · 2026-10-08 · kịch bản v2 (WRITER mới: S18–S23 → 3 câu lời, số lên nhãn B19/B22, thẻ V7, mô tả; S30.5 đối trọng)
- **(a) Máy:** ĐẠT với `--g1-short` (chỉ độ dài trượt): 1.175 từ nói → ước **7:46** (thiếu ≈ 72 từ / 29 s so với 8:15) → **nêu ở G1**. Khuôn (THAM KHẢO): khái niệm **+5,8**, thí nghiệm **−7,4** điểm (> ±5, nêu tên); hook +2,9 · người −0,4 · giới hạn −0,9. M1–M6 ước như v1 (cold open không đổi → số đo bản đọc thật giữ nguyên).
- **(b) Kiểm mù (`c2/r2/`, 6 Sonnet mới + 1 người chấm):** đúng **6/6**, khuyên **0/6**; mất chú ý theo loại khối: **phương pháp 2/6** ("715 stretches overlap", S31.2) · **định nghĩa 2/6** (S03.1 "keeping up means…", S06.3 "national average…") · **số dày 2/6** (S09.1 "12 of its first 15 anniversaries", S12.2 "by year 5… 9 crates"). Không loại nào ≥ 4/6 → **ĐẠT** cổng. Đã hết 2 vòng: ba loại ở 2/6 (ngưỡng sửa `episode.md` §2) chuyển sang G1 / C4 (sửa bằng hình ở C3–C4: S31.2 lên thẻ V7, S09–S12 nhịp thùng).
