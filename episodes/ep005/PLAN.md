# PLAN — Tập 5 (ep005), một phiên điều phối (D-008)

Nhánh **`ep005`** (chủ dự án, G1; trước đó `ccr-a4da2518-3guqrl` @ `906f8be`) từ `main` @ `b1d3e79`. **D-009: chất lượng là ưu tiên tuyệt đối.** **TẠM DỪNG trước dựng hình, chờ Mốc V merge `main`.** Format **`101`** (D-007 thí điểm #1). Đề tài khuyến nghị **#17 debt-2** (PMI với 10 % trả trước). Trần tập **3,0 triệu token** theo loại việc (`episode.md` §8), ≤ 40 agent, ≤ 120 lượt headless, EL ≤ 6.000.

## 1. Bảng cổng
| Cổng | Trạng thái | File | Ghi chú |
|---|---|---|---|
| Việc 0 | XONG | `data/fetch.py`, `model/model.py`, `model/statements.py`, `numbers.md`, `model/independent/` | SHA khớp hồ sơ; 17/17 câu; độc lập 55/55; tháng lãi mới nhất = tháng đủ tuần (2026-09) |
| C1 | ĐẠT | `gates/C1-*.md`, `c1/` | L1 2/2, L2 2/2, cờ 0 → L2 |
| C2 | ĐẠT (vòng 2) | `story/`, `gates/C2-*.md`, `gates/REVIEW-C2.md`, `c2/` | H-A; M1–M5 thật ĐẠT (M4 9,41 s); mù v2 6/6, khuyên 0, S18 3/6 |
| Giao phiên K | SẴN SÀNG (G1 duyệt) — chủ dự án mở khi muốn; cần trước C4 | `K-brief.md` | kind mới + lô A10–A12, A5, A7, A9 |
| **G1** | **XONG** (issue #43; `gates/G1-answer.md`) | `gates/G1.md`, `gates/REVIEW-G1.md` | #17 · L2 · H-A · T1 · 75 % (a): nguyên văn B-8.1-04, phạm vi Fannie Mae |
| Lời theo cảnh | XONG trừ S03, S12 (chờ câu 75 %) | `story/voice_scenes.py`, `voice-takes/`, `review-g1/voice-scenes.json` | ASR từ khoá theo cảnh |
| **Mốc V** | **CHỜ — chủ dự án mở** | — | Tập 5 dừng ở đây |
| Chuyển kịch bản sang đặc tả nhịp Mốc V → C4 → C5 → Shorts → G2 | chưa | | sau Mốc V merge + K merge |

## 2. Phiên sau đọc (sau Mốc V merge)
`decisions/D-009.md` · đặc tả nhịp Mốc V (README/playbook do Mốc V ghi) · `CHARTER.md` · `playbook/episode.md` · `playbook/prompts/P3.md` · `episodes/ep005/PLAN.md` · `ledger.md` · `gates/G1.md` + trả lời G1 · `story/script.md` · `story/beats.md` · `episode.yaml` · `toolkit/factory/README.md`.

## 3. Việc treo
- **Câu 75 % (hỏi chủ dự án, đổi câu đã duyệt):** nguồn đã có (B-8.1-04, chỉ khoản vay Fannie Mae) nhưng lời S03.3 "Removal on value is lender policy: request, appraisal, minimum time, and early on, a 75 percent bar." và S12.3 "…the 75 percent bar that lenders often use early on." nói như quy định chung của bên cho vay. Đề xuất:
  - **(i) khuyến nghị — sửa lời:** S03.3 → "Removal on value is the loan owner's rule; for Fannie Mae loans, that's two years and a 75 percent bar." (≈ 18 từ đọc; đo lại M4 ≤ 10 s) · S12.3 → "…at or below the 75 percent bar Fannie Mae sets for its loans in the early years." Sinh lại S03, S12 (≈ 0,8 nghìn ký tự), đo lại M1–M5.
  - (ii) giữ lời, nhãn hình cạnh mọi khung có 75 %: "Fannie Mae rule, its loans only".
  Có thể gộp vào lượt chuyển kịch bản sang đặc tả Mốc V.
- **S18.5 giọng:** ASR (small.en và medium.en) nghe "illustrative" thành "illustrated" (p 0,49) — khả năng giọng đọc chưa rõ; cùng chữ + cùng seed thì cache trả lại đúng take cũ, nên xử lý ở lượt chuyển kịch bản Mốc V (đổi chữ hoặc nghe lại bằng tai). Từ được bảo vệ (ILLUSTRATIVE) → không bỏ qua.
- Freddie Mac Guide 8203.2 chưa kiểm (proxy chặn); claim chỉ dựa B-8.1-04.
- Phiên K (kind mới) phải merge `main` trước C4; `contract.json` theo kind K đặt.
- Hàng chờ G2 (CHÍNH không đổi nghĩa): `REVIEW-C2.md` K-3…K-14; câu 3 vòng 2 C2.
- `episode.yaml` chưa có `scenes/acts/midrolls/counterweights` cho nhà máy (thêm ở C4); `midrolls` theo giọng thật (ước ≈ 3:26 sau S09.4).
- So headless ↔ `Explore`: cảnh mất chú ý khác nhau → câu hỏi mở cho tổng kết Tập 5.

## 4. Điểm dừng an toàn + lệnh chạy tiếp
2026-10-06 (sau G1): **DỪNG chờ Mốc V.** Nhánh `ep005`. Lời theo cảnh: `python3 episodes/ep005/story/voice_scenes.py --skip S03,S12` (cache theo băm chữ; chỉ sinh cảnh đổi chữ; báo cáo `review-g1/voice-scenes.json`). Khi chủ dự án chọn câu 75 %: sửa S03.3/S12.3 (WRITER mới) → `voice_scenes.py --only S03,S12` → `story/table_read.py` (M1–M5).
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

**Sau G1 (2026-10-06):** lời theo cảnh 18/20 cảnh trong `voice-takes/` (≈ 6:07 lời); EL cả tập **6.531/6.000 (+9 %)** — D-009: không cắt chất lượng vì trần; nêu tên. Agent 12/40 (không thêm agent sau G1).
