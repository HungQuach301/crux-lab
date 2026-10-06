# B+3 — Báo cáo cuối Mốc V (06/10/2026)

Nhánh `moc-v`. Không sửa `checks/` (đề xuất ở `checks-appeal.md` A13–A19); không đụng `episodes/ep005/` (mọi ca Tập 5 chạy trên bản sao chỉ đọc `moc-v/work/ep005-b1`, không commit). Không mua, không đăng ký dịch vụ nào; 0 ký tự ElevenLabs trong Phần B.

## 1. Kết quả theo lệnh

| Việc | Đạt? | Bằng chứng |
|---|---|---|
| Hướng "một thế giới, hai chế độ máy quay" — clip chứng minh | **ĐẠT (L3 chủ dự án)**: Tập 4 v3k 4·4·4·4·4·4 · Tập 5 E5g 4·4·4·4·4·4 | `decisions/D-010.md` §6 |
| (a) Tập 4: nhà ở chế độ đồ thị theo V3i (đứng mặt đất cạnh chồng, chỉ chồng là dữ liệu, máy chừa dải đất) | **ĐẠT** — cổng gốc K1 3/3 · K2 3/3 · **0 khuyên** (1 vòng sửa + 1 sửa nhãn đường vì người đọc đọc nhầm đường) | `moc-v/eval/v3-blind22-raw`, clip `review/proof-a-ep004-v3l-540p.mp4` |
| (b) Sửa bằng hình chỗ gây lời khuyên ("don't rush to sell" V3k; "stay 8+ years" E5g) | **ĐẠT** — Tập 4 hết câu đó (blind #22); Tập 5 E1 3/3 · E2 3/3 · **0 khuyên** | `moc-v/eval/e5-blind10-raw`, clip `review/proof-b-ep005-e5h-540p.mp4` |
| Đồng bộ lời–hình ±0,2 s | Tập 4 v3l **23/23**, Tập 5 E5h **11/11**; lời lệch trung vị 0,013 / 0,008 s | `eval/v3l-sync-ep004.json`, `eval/e5h-sync.json` |
| Quy tắc 1/2/3/7, cắt cứng | cả hai đoạn: 0 · 0 · 0 · 0 · 5 s đầu ở thế giới | `.verify.json` (build_seg) |
| C14 (bản 1080p) | xem §4 | `moc-v/work/world/*-1080.mp4.verify.json` → `moc-v/b3/c14-1080.json` |
| **B+1** `voice_overrides` (Tập 5 S18 seed 1006 ra "illustrative") | **ĐẠT** — ASR "illustrative" (seed 1005 mặc định: "illustrated"); selftest 5/5; không khai → 20/20 cảnh cùng khoá/take/file như mã cũ | `moc-v/b1/README.md` |
| **B+2** ≤ 2 số MỚI được nói mỗi cảnh (Tập 5 S03) | **ĐẠT** — trước: S03 BLOCK 3 số; sau: 2 số ("eighty percent", "seventy-five percent"), "2 năm" lên nhãn `Fannie Mae: wait ≥ {value_removal_seasoning_years} years · loan ≤ {value_removal_ltv_early}`, phạm vi Fannie Mae giữ; cả Tập 5 0 BLOCK; selftest 5/5 | `moc-v/b2/README.md` |
| Áp thiết kế vào nhà máy (thư viện vật thể, spine v2, render theo cảnh có cache) | **ĐẠT** — `toolkit/factory/world/`; dựng lại hai đoạn qua nhà máy: hình + tiếng **trùng MD5** với clip đã duyệt; spine trùng byte; cache trúng 5/5 → 0,9 s; selftest 7/7 | `moc-v/b3/factory-proof.md`, `visual-library` §5 |
| Sửa CHARTER/playbook theo D-009/D-010 | **ĐÃ SỬA** — CHARTER v4 (gen §4 đúng chữ D-010), quality-framework v3 (§10 tám quy tắc, lượt đạo diễn = chẩn đoán, L3 ≥ 4), episode.md v4, RUN/P1–P3, sổ gu, `spec.py` ký hiệu > 2 → cảnh báo | `decisions/D-009.md` "Đã sửa 06/10" |
| Backlog nhà máy | F-1 máy quay đi thật thay hoà tan · F-2 kiểm mật độ sfx + nhãn đè · F-3 nhạc Tập 5 theo bản đồ căng · F-4 lint (**xong**) · **F-5 ghép đoạn thế giới vào master** (chưa làm, cần một tập thật) | `toolkit/factory/BACKLOG.md` |

## 2. Token thực (cảnh báo dự kiến ≈ 2,5 triệu — **VƯỢT**)
- **Phiên này (số harness, cả Phần A và B):** đầu vào mới 0,12 triệu + ghi cache 5,96 triệu + đầu ra 1,62 triệu = **≈ 7,7 triệu token mới**; đọc cache 282 triệu (giá thấp). Harness báo ≈ **$125** (đo của harness, không phải hoá đơn).
- **Kiểm mù headless (ngoài phiên):** 191 lượt đọc + 33 lượt chấm = **2,31 triệu** (đầu vào 2,12 + đầu ra 0,19), cộng từ `tokens` trong mọi `answer-*.json`/`grade.json` ở `moc-v/eval/`.
- Agent con (lượt đạo diễn, REVIEWER): không có bộ đếm riêng ngoài harness; nếu harness không gộp thì là phần chưa đếm.
- **Lý do vượt:** ~12 vòng Tập 4 (v3–v3l) và 8 vòng Tập 5 (E5a–E5h) mỗi vòng có cổng gốc 6 người đọc + lượt đạo diễn 2 người; theo D-009 không cắt bước chất lượng. Bài học: lời phê đạo diễn máy mâu thuẫn giữa các vòng (nay chỉ chẩn đoán) — đây là phần token có thể tiết kiệm ở Tập 5.

## 3. Giờ render thực
- Đo theo file còn giữ (`*.render.json`, mỗi bản chỉ giữ lần cuối): **3.442 s ≈ 0,96 h** máy. Ước cả mốc (mọi vòng, mọi bản thử, 1080p của Gói A và §4): **≈ 1,6–1,8 h** máy (4 lõi, SwiftShader).
- Nhịp: 540p ≈ 1,95–2,25 s máy / s phim (3 worker); 1080p xem §4; cache trúng < 1 s; âm 9–18 s / đoạn.

## 4. Bản 1080p + C14
(điền sau khi chạy xong — xem §4 cập nhật bên dưới)

## 5. Rủi ro và việc chưa xong
- **F-5:** nhà máy dựng + kiểm + chặn đoạn thế giới, nhưng **chưa ghép vào master** của tập. Tập 5 cần việc này trước C4.
- Sửa S03.3 Tập 5 mới ở bản sao; áp vào nhánh `ep005` cần đọc lại giọng 1 cảnh (S03) — phiên Tập 5 làm, chi tiêu EL nằm trong mức Tập 5.
- Luật mới (A13–A19) chỉ là đề xuất cho lô K; nhà máy đã chặn sớm B+2 và quy tắc 1/2/3/7 trong `build_seg`.
- Tập 3 (đã phát hành) vượt luật B+2 ở 3 cảnh → chỉ cảnh báo (danh sách `LEGACY`).
