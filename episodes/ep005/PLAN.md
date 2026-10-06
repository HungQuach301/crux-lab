# PLAN — Tập 5 (ep005), một phiên điều phối (D-008)

Nhánh `ccr-a4da2518-3guqrl` (lệnh phiên) từ `main` @ `b1d3e79`. Format **`101`** (D-007 thí điểm #1). Đề tài khuyến nghị **#17 debt-2** (PMI với 10 % trả trước). Trần tập **3,0 triệu token** theo loại việc (`episode.md` §8), ≤ 40 agent, ≤ 120 lượt headless, EL ≤ 6.000.

## 1. Bảng cổng
| Cổng | Trạng thái | File | Ghi chú |
|---|---|---|---|
| Việc 0 | XONG | `data/fetch.py`, `model/model.py`, `model/statements.py`, `numbers.md`, `model/independent/` | SHA khớp hồ sơ; 17/17 câu; độc lập 55/55; tháng lãi mới nhất = tháng đủ tuần (2026-09) |
| C1 | ĐẠT | `gates/C1-*.md`, `c1/` | L1 2/2, L2 2/2, cờ 0 → L2 |
| C2 | ĐẠT (vòng 2) | `story/`, `gates/C2-*.md`, `gates/REVIEW-C2.md`, `c2/` | H-A; M1–M5 thật ĐẠT (M4 9,41 s); mù v2 6/6, khuyên 0, S18 3/6 |
| Giao phiên K | SẴN SÀNG khi G1 duyệt | `K-brief.md` | kind mới + lô A10–A12, A5, A7, A9 |
| **G1** | **CHỜ CHỦ DỰ ÁN** | `gates/G1.md`, `gates/REVIEW-G1.md` | ngoại lệ: nguồn mốc 75 % |
| C4 → C5 → Shorts → G2 | chưa | | sau G1 + K merge |

## 2. Phiên sau đọc (sau G1)
`CHARTER.md` · `playbook/episode.md` · `playbook/prompts/P3.md` · `episodes/ep005/PLAN.md` · `ledger.md` · `gates/G1.md` + trả lời G1 · `story/script.md` · `story/beats.md` · `episode.yaml` · `toolkit/factory/README.md`.

## 3. Việc treo
- **Nguồn mốc 75 % / 2 năm** (Fannie Mae B-8.1-04 / Freddie 8203.2): proxy chặn → G1 ngoại lệ (a)/(b).
- Phiên K (kind mới) phải merge `main` trước C4; `contract.json` theo kind K đặt.
- Hàng chờ G2 (CHÍNH không đổi nghĩa): `REVIEW-C2.md` K-3…K-14; câu 3 vòng 2 C2.
- `episode.yaml` chưa có `scenes/acts/midrolls/counterweights` cho nhà máy (thêm ở C4); `midrolls` theo giọng thật (ước ≈ 3:26 sau S09.4).
- So headless ↔ `Explore`: cảnh mất chú ý khác nhau → câu hỏi mở cho tổng kết Tập 5.

## 4. Điểm dừng an toàn + lệnh chạy tiếp
2026-10-06: **DỪNG ở G1.** Tái tạo: `python3 episodes/ep005/data/fetch.py --verify && python3 episodes/ep005/model/model.py && python3 episodes/ep005/model/statements.py --all && python3 episodes/ep005/story/check_script.py`. Đọc thử: `python3 episodes/ep005/story/table_read.py` (take ở `voice-takes/`, không sinh lại khi chữ không đổi; cần `pip install av==14.2.0` cho faster-whisper). Kiểm mù: `python3 episodes/ep005/blind.py read|grade …`.

## 5. KPI + token so trần (tới G1)
| Loại việc | Thực | Trần | Ghi chú |
|---|---|---|---|
| Kiểm mù | ≈ 0,30 tr (headless 0,19 + `Explore` so 0,11) | 0,6 | 26 lượt headless |
| Dựng | ≈ 0,25 tr | 0,75 | Việc 0 + bổ sung nguồn |
| WRITER | ≈ 0,31 tr | 0,4 | **78 %** — giai đoạn dựng chỉ còn ≈ 0,09 |
| REVIEWER | ≈ 0,12 tr + G1 | 0,45 | |
| Checks | ≈ 0,07 tr | 0,15 | kiểm độc lập |
| Điều phối | ≈ 0,3 tr | 0,5 | |
| **Cộng** | **≈ 1,45 tr** | 3,0 | agent 12/40; EL 1.644/6.000; chủ dự án: G1 |
