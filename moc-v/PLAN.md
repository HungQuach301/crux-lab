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
