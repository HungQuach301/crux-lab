# PLAN Tập {N} — {tiêu đề}  (≤ 1 trang; phiên cập nhật sau mỗi bước, viết lại khi đóng chặng)

Mẫu từ tổng kết Tập 5 §3.7, sửa theo D-013 (6 mốc, prompt "Chạy Tập N"). Lịch sử (vòng cũ, lệnh cũ, giao file) → `episodes/ep{NNN}/archive/PLAN-history.md`. **Quyết định còn hiệu lực luôn ở mục 3 hoặc `gates/*-answer.md`, không chỉ ở archive.**

**Nhánh:** `ep{NNN}` · **Đề tài:** #{k} · **Format:** `101`/`lab`/`deep` · **Phiên vừa đóng:** `session_…`

## 1. Mốc hiện tại (phiên "Chạy Tập N" đọc dòng này để biết chặng kế)
**Mốc:** <M1 | M2 | G1 chờ | M3 | M4 | M5 | G2 chờ | M6 | G3 chờ | xong> — một dòng: đã đạt gì, số đo chính (CHẶN/CHÍNH, cổng gốc, nhận dạng, nhớ lại, M1–M8, độ dài ước).

## 2. Việc tiếp (≤ 3) và việc treo
1. …
- Treo: … (ai, chờ gì)

## 3. Quyết định đã có (chủ dự án)
- {dd/mm} {cổng}: … → `gates/{cổng}-answer.md`

## 4. Đã sửa gì, vì sao (≤ 2 vòng mỗi lỗi; ≤ 10 dòng — chép nguyên vào đầu bài lượt headless kế, `episode.md` §1)
| Vòng | Cảnh | Lỗi (mã luật / phép thử vai) | Vai | Sửa | Kết quả đo (so bản tốt nhất, biên nhiễu) | Còn |
|---|---|---|---|---|---|---|

## 5. Sổ chi theo mốc (vai Line producer, `episode.md` §8)
Mức cảnh báo (`lab`): trần 15 triệu (log phiên + headless) · **đọc cache ≤ 60 triệu/tập** · **≤ 150 lượt/phiên** · Console $25–40 · giờ máy 8–12 h · EL ≈ 8.500.
| Mốc / phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Lượt | Console $ | Giờ máy | EL | Chủ dự án chạm (phút ước) |
|---|---|---|---|---|---|---|---|---|---|---|
Token: `python3 toolkit/usage/from_events.py --session <id> --close trang*.json`; $: `total_cost_usd` headless; giờ máy: `build-report.json`.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `playbook/story.md` 4. `episodes/ep{NNN}/PLAN.md` (tệp này) 5. `episodes/ep{NNN}/preprod/TAM-NHIN.md` 6. <gói cổng gần nhất> 7. <tệp câu trả lời> 8. <tệp của chặng kế>

## 7. Mở chặng kế
Chủ dự án dán prompt mẫu `playbook/prompts/CHAY-TAP-N.md` ("Chạy Tập {N}." + câu trả lời cổng nếu có). Không viết prompt riêng.
