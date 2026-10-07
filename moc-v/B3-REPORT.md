# B+3 — Báo cáo cuối Mốc V (06–07/10/2026)

Nhánh `moc-v`. Không sửa `checks/` (đề xuất ở `checks-appeal.md` A13–A19); không đụng `episodes/ep005/` (ca Tập 5 chạy trên bản sao chỉ đọc `moc-v/work/ep005-b1`, không commit). Không mua, không đăng ký dịch vụ nào; 0 ký tự ElevenLabs trong Phần B. So sánh nhánh dùng `origin/main` (ref `main` ở máy đã cũ).

**Tên phiên bản:** clip v3l = khoá mù `V3l2` (vòng #22); clip E5h = khoá `E5j` (vòng #10); clip **E5k** = E5h + chữ "slowest case" (vòng #11). L3 của chủ dự án chấm trên **v3k/E5g**; v3l/E5h/E5k là bản sửa khách quan sau L3, **chưa được chấm L3**.

## 1. Kết quả theo lệnh

| Việc | Đạt? | Bằng chứng |
|---|---|---|
| Clip chứng minh, hướng "một thế giới, hai chế độ máy quay" | **ĐẠT (L3)**: v3k 4·4·4·4·4·4 · E5g 4·4·4·4·4·4 | `decisions/D-010.md` §6 |
| (a) Tập 4: nhà ở đồ thị theo V3i | **ĐẠT** — cổng gốc K1 3/3 · K2 3/3 · 0 khuyên. **Lệch lệnh: 2 vòng, không phải 1** — vòng #21 (sửa hình) K1 0,5 × 3 (đọc đường thành giá trị nhà) → vòng #22 thêm tên đường "their gain on paper" gắn trên đường (nhãn, sau khi đã thử hình — E6) | `eval/v3-blind21-raw`, `eval/v3-blind22-raw`, `review/proof-a-ep004-v3l-540p.mp4` |
| (b) Sửa bằng hình chỗ gây lời khuyên | **ĐẠT** — Tập 4: câu "don't rush to sell" hết (vòng #22). Tập 5: **2 vòng** — #9 (E5i) còn 2 câu khuyên ở E1 ("buy only if able to stay 8+ years", "hold through a downturn") → #10 đổi màu đường chậm + nhãn thời lượng, tách nhãn → E1 3/3 · E2 3/3 · 0 khuyên | `eval/e5-blind9-raw`, `eval/e5-blind10-raw` |
| Sửa thêm theo REVIEWER (claim-risk) | **ĐẠT** — "slow cases ≈ 9 years" là số của ca chậm NHẤT (`maxB_months_to80` = 112 tháng ≈ 9,3 năm là một ca, không phải nhóm) → chữ "slowest case ≈ 9 years"; hình không đổi. Cổng gốc E1 lại: **3/3 · 0 khuyên** | `eval/e5-blind11-raw`, `review/proof-b-ep005-e5k-540p.mp4` |
| Đồng bộ lời–hình ±0,2 s | Tập 4 v3l **23/23**, Tập 5 E5k **11/11**; lời lệch trung vị 0,013 / 0,008 s | `eval/v3l-sync-ep004.json`, `eval/e5k-sync.json` |
| Quy tắc 1/2/3/7, cắt cứng (540p và 1080p) | cả hai đoạn: 0 · 0 · 0 · đúng · 0 | `b3/evidence/*.verify.json` |
| **C14 trên bản 1080p** | **ĐẠT** — Tập 4: 2.476 mẫu, 0 vi phạm; Tập 5: 1.074 mẫu, 0 vi phạm | `b3/evidence/ep00{4,5}-1080.mp4.verify.json` |
| **B+1** `voice_overrides` | **ĐẠT** — S18 seed 1006: ASR "illustrative" (seed 1005: "illustrated"); selftest 5/5; không khai → 20/20 cảnh cùng khoá/take/file như mã cũ | `b1/README.md` |
| **B+2** ≤ 2 số mới được nói mỗi cảnh | **Luật + bộ kiểm ĐẠT** — S03 trước: BLOCK 3 số; sau: 2 số, phạm vi Fannie Mae + 3 claim giữ; cả Tập 5 0 BLOCK; selftest 5/5; `spec.py` cảnh báo khi nhãn thay số không có trên hình. **Nhãn S03 mới ở dạng đặc tả trong `script.md`, chưa render** — phiên Tập 5 làm (cùng đọc lại giọng S03) | `b2/README.md` |
| Áp thiết kế vào nhà máy | **ĐẠT** — `toolkit/factory/world/`: dựng lại hai đoạn qua nhà máy → hình + tiếng trùng MD5 với clip **v3l/E5h**; spine trùng byte; cache trúng 5/5 → 0,9 s; selftest 8/8. **Chưa ghép vào master** (BACKLOG F-5; `spec.py` cảnh báo) | `b3/factory-proof.md`, `visual-library` §5 |
| Sửa CHARTER/playbook theo D-009/D-010 | **ĐÃ SỬA** — CHARTER v4 (gen §4 đúng chữ D-010 §3), quality-framework v3 (§10, C5 "Chính = 0", L3 ≥ 4, đạo diễn = chẩn đoán), episode.md v4, RUN/P1–P3, sổ gu. Trần 40 agent và EL 6.000 ký tự **giữ nguyên** (D-009 chỉ đổi trần token) | `decisions/D-009.md` "Đã sửa" |
| REVIEWER | vòng 1: TRƯỢT 9 CHÍNH + 6 tham khảo → đã sửa; vòng 2: TRƯỢT 1 CHÍNH (giờ render đếm trùng) + 3 tham khảo → đã sửa (mục 4) | — |

**Chỉ số sát ngưỡng (±5 %, nêu tên):** đồng bộ `b1.many` 0,196 s và `c2.schedule` 0,189 s (ngưỡng 0,2 s); B+2: S01, S03, S05, S08, S11, S12 của Tập 5 đúng bằng ngưỡng 2 số mới.
**Câu sát ranh giới lời khuyên** (rubric không tính, rubric không đổi từ vòng 1): "check whether you're near the limit before deciding to sell", "pay the loan down", "keep an emergency fund" — đáng xem lại khi lô K xử lý A9.

## 2. Token thực (cảnh báo dự kiến ≈ 2,5 triệu — **VƯỢT ≈ 4,4 lần**)
- **Phiên (harness, Phần A + B):** đầu vào mới 0,12 + ghi cache 6,48 + đầu ra 1,80 = **≈ 8,4 triệu token mới**; đọc cache 350 triệu. Harness ước ≈ $146 (số của harness, không phải hoá đơn).
- **Kiểm mù headless:** 228 lượt (đọc + chấm) = **2,35 triệu** (đầu vào 2,16 + đầu ra 0,19), cộng từ `tokens` trong `moc-v/eval/**`.
- REVIEWER: vòng 1 0,15 triệu, vòng 2 0,09 triệu (agent con). Các lượt đạo diễn (agent con) không có bộ đếm riêng ngoài harness.
- **Lý do:** ~12 vòng Tập 4 + ~10 vòng Tập 5, mỗi vòng cổng gốc 6 người đọc + lượt đạo diễn 2 người; D-009 không cho cắt. Chỗ tiết kiệm được ở Tập 5: lượt đạo diễn nay chỉ chẩn đoán (lời phê từng mâu thuẫn giữa các vòng).

## 3. Giờ render thực
- Đo từ file còn giữ, khử trùng theo nội dung (`b3/evidence/render-hours.json`; mỗi bản chỉ giữ lần cuối) + lần 1080p Tập 5 bị dừng (248 s, theo log): **3.010 s ≈ 0,84 h** máy. Ước cả mốc gồm các lần bị ghi đè (≈ 9 vòng Tập 4 + 6 vòng Tập 5 ở 540p có cache một phần, bản thử v1/v1b Gói A): **≈ 1,4–1,7 h** (4 lõi, SwiftShader). (Vòng 1 báo 1,18 h vì đếm hai lần 4 file trùng — REVIEWER vòng 2 bắt.)
- Nhịp (wall, 3 worker song song): 540p ≈ 1,9–2,3 s máy / s phim; **1080p ≈ 6,9–7,1 s/s** (Tập 4: 69,6 s → 481 s; Tập 5: 34 s → 240 s); cache trúng < 1 s; âm 9–18 s / đoạn. Trường `wall_per_film_s_rendered` trong `*.build.json` cộng thời gian của **từng worker** (≈ 3 × wall) nên lớn hơn.

## 4. Đã sửa sau REVIEWER vòng 1
Chữ "slowest case" + cổng gốc E1 lại; ghi lệch 2 vòng mù vào D-010 §6; A15 ghi đúng hình/nhãn; mọi chỗ "trùng MD5" ghi rõ v3l/E5h; B+2 ghi "luật đạt, nhãn chưa render"; nêu chỉ số sát ngưỡng; bằng chứng verify/build/giờ render chép vào `b3/evidence/`; `quality-framework` C5 "Chính = 0"; trả trần 40 agent / EL 6.000; `spec.py` cảnh báo F-5 và nhãn thiếu (test mới); PLAN cập nhật đường dẫn và trạng thái; bảng tên phiên bản; câu sát ranh giới. Vòng 2: khử trùng giờ render (0,84 h, không phải 1,18 h); C14 kiểm video 30 fps trước khi lấy khung n = 6k. Thêm: bộ kiểm C14 1080p đọc từng khung đúng chỉ số (bản cũ hết bộ nhớ ở 1080p và lấy khung lệch tới nửa khung → 5 vi phạm giả lúc nhãn vừa hiện).

## 5. Rủi ro và việc chưa xong (cho phiên Tập 5)
- **F-5** ghép đoạn thế giới vào master — cần trước C4 Tập 5.
- **S03 Tập 5:** áp B+2 vào nhánh `ep005` cần đọc lại giọng S03 và dựng nhãn "Fannie Mae: wait ≥ 2 years · loan ≤ 75%"; sau đó **kiểm mù lại đoạn S03 → S12** (người xem nay nghe "two years" lần đầu ở S12.3, mốc chờ 2 năm chỉ còn trên nhãn S03).
- v3l/E5h/E5k chưa được chủ dự án chấm L3 (thay đổi so với v3k/E5g: vị trí nhà ở đồ thị, tên đường, màu + nhãn đường chậm).
- Luật A13–A19 mới là đề xuất cho lô K. Tập 3 (đã phát hành) vượt B+2 ở 3 cảnh → chỉ cảnh báo (`LEGACY`).
