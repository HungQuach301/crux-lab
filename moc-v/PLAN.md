# Mốc V — kế hoạch và điểm dừng

Nhánh `moc-v` (từ `main` b1d3e79). Không sửa `checks/`, không đụng `episodes/ep005/`. Mở phiên: `bash toolkit/verify.sh moc-v` (ĐẠT trừ "cây sạch" khi đang làm).

## Phần A (làm ngay, rồi DỪNG chờ chủ dự án)
1. `decisions/D-009.md` (nháp, chờ duyệt).
2. Đo hiện trạng Tập 1–4: `moc-v/measure/` → `moc-v/BASELINE.md`.
3. Đoạn thử 69,6 s (Tập 4 S04.5 → S07.3), trục xương sống `moc-v/proto/spine.py` → 3 hướng A/B/C + bản phát hành, clip so sánh, đo, cổng gốc, lượt đạo diễn, thời gian render, so nguồn tài sản (`moc-v/assets/SOURCES.md`).
4. REVIEWER → Gói A (≤ 10 dòng) + issue nhắc @HungQuach301 → DỪNG.

## Phần B (chỉ sau khi chủ dự án chọn hướng) — gồm bổ sung của chủ dự án 06/10 (trong phiên)
5–9 như lệnh mở phiên, cộng:
- **B+1 `voice_overrides`:** công cụ dựng đọc `voice_overrides` trong `episode.yaml` (chọn seed hoặc take theo từng cảnh). Ca kiểm thật: **Tập 5, S18 seed 1006** phải dựng ra đúng chữ "illustrative" (kiểm bằng ASR). Thêm selftest; tập **không** khai `voice_overrides` phải cho kết quả **giống hệt trước** (so băm take/timeline).
- **B+2 luật ≤ 2 số mới được NÓI mỗi cảnh** trong spec mới (spine): số thứ ba chuyển thành nhãn trên hình. Ca đầu: **Tập 5 S03** — "two years" chuyển thành nhãn hình, lời vẫn đúng phạm vi Fannie Mae.
- **B+3 báo cáo cuối Mốc V** ghi rõ B+1, B+2 đạt hay chưa, kèm bằng chứng (ASR, selftest, so băm).
- Lưu ý: hai ca kiểm dùng dữ liệu Tập 5 (nhánh `ep005`) — chỉ ĐỌC, không sửa `episodes/ep005/` trên nhánh này trừ khi chủ dự án cho phép; kiểm trên bản sao trong `moc-v/`.

## Trả lời Gói A (06/10/2026, issue #45) → `decisions/D-010.md`
Hướng B + C "một thế giới, hai chế độ máy quay"; 8 quy tắc; gen 3D tối giản; D-009 + E1–E6 duyệt; không nguồn trả phí.
### Bước chứng minh (đang làm)
- V1. Thư viện vật thể 3D có tham số + bộ động tác máy quay hữu hạn + lớp phủ 2D ≥ 48 px (`moc-v/world/`).
- V2. Spine v2: thêm `mode` (world/chart), `camera` (động tác giữa nhịp), lý do chuyển chế độ + âm; mọi mốc từ spine.
- V3. Render theo cảnh: cache + resume; 540p xem trước; 1080p bản cuối một lần.
- V4. Đoạn (a) Tập 4 60 s (đối chứng R): cổng gốc K1, K2 bằng hình · đạo diễn ≥ 4 ×4 · đồng bộ ≥ 11/12 · C14 · 0 cắt không lý do. Lặp đến đạt.
- V5. Đoạn (b) mở đầu Tập 5 30–45 s (chỉ đọc `ep005`, bản sao trong `moc-v/`): cùng chuẩn.
- V6. REVIEWER → clip cho chủ dự án chấm L3 → DỪNG.
- Sau duyệt clip: B+1, B+2, B+3, áp nhà máy, CHARTER/playbook, hỏi "Duyệt Mốc V?".

## Trả lời clip chứng minh (06/10)
L3: Tập 4 v3k 4·4·4·4·4·4 · Tập 5 E5g 4·4·4·4·4·4 → ĐẠT; L3 là thước đo cuối, đạo diễn máy = chẩn đoán (D-010 §6 bổ sung). Dừng sửa thẩm mỹ.
Việc còn lại theo thứ tự: (a) Tập 4 nhà ở đồ thị theo V3i, cổng gốc 6/6 · 0 khuyên; (b) sửa bằng hình chỗ gây lời khuyên (V3k, E5g), 0/6; backlog nhà máy → `toolkit/factory/BACKLOG.md`; rồi B+1, B+2, áp vào nhà máy, CHARTER/playbook, REVIEWER, B+3, hỏi "Duyệt Mốc V?".

### Kết quả hai sửa khách quan (06/10)
- (a) Tập 4 v3l — nhà đứng mặt đất cạnh chồng ở đồ thị, khung phóng chừa dải mặt đất, tên đường gắn trên đường: cổng gốc **K1 3/3 · K2 3/3 · 0 khuyên** (`eval/v3-blind22-raw`). Không còn "don't rush to sell".
- (b) Tập 5 E5h — đường "slow cases" màu trung tính + nhãn thời lượng "≈ 9 years", bỏ nhãn 100 %, tách nhãn "typical"/"schedule": cổng gốc **E1 3/3 · E2 3/3 · 0 khuyên** (`eval/e5-blind10-raw`). Không còn "buy only if able to stay 8+ years".

## Áp thiết kế vào nhà máy (06/10)
Thư viện vật thể, spine v2, render theo cảnh có cache, âm theo spine, kiểm đoạn → `toolkit/factory/world/` (README nhà máy, `visual-library` §5 W1–W9).
Dựng lại hai đoạn chứng minh qua nhà máy: hình + tiếng trùng MD5 với clip v3l/E5h (bản sửa sau L3; L3 chấm trên v3k/E5g) (`moc-v/b3/factory-proof.md`). Ghép vào master: BACKLOG F-5.
