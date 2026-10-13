# Tổng kết Tập 7 + mô hình xưởng phim Crux — 13/10/2026

Nhánh `tongket-t7` từ `origin/main` @ `c735828`. Mở bằng `bash toolkit/verify.sh tongket-t7`: ĐẠT 17/17 (LOCK `dc4981b3…`, đĩa 26,8 GB).
Hướng do chủ dự án duyệt 13/10: **chất lượng chỉ tăng**, nâng chất lượng ngay từ tiền kỳ, vòng kiểm–sửa có điểm dừng. Từ Tập 8: 1 Short, không thumbnail. Cho phép footage ngoài, ưu tiên nguồn miễn phí. Nâng cấp đi hai đường: thử trên tập cũ trước, và chỉ đưa vào tập đang chạy ở ranh giới cổng.
**Phiên này chỉ đề xuất.** Chưa sửa `playbook/`, `CHARTER.md`, `RIGHTS.md` hay `checks/`; mọi bản sửa nằm ở `tongket-t7/de-xuat/`, chờ chủ dự án duyệt. Ngoại lệ: dọn `PLAN.md` kênh (mục 7) và ghi khiếu nại A38–A41 vào `checks-appeal.md`. Không chạm `ep008`: phiên P1 Tập 8 đang chạy song song (`session_01PgYotX9apRQ11gZoym31kJ`).

Nguồn đã đọc: `CHARTER.md` · `playbook/episode.md` · `playbook/lessons.md` · `episodes/ep007/TONGKET-INPUT.md` · `episodes/ep007/gates/G2.md` · cine-lab `reports/m3/CHUAN-KENH-LL.md` (§5, §9, §11) · `reports/m3/BAI-HOC-LL.md` · `.claude/agents/cine-worker.md`. Mục 1 cần số nên đọc thêm: `ep007/PLAN.md` §5, `ledger.md`, `gates/{G1,C3,C4,G2}-answer.md`, `toolkit/factory/f14/REPORT.md` §4. Log `result` của phiên P4 lấy qua `list_events`.

---

## 1. Số thật Tập 7 (P1–P4, F-14)

### 1a. Token: 4 số đọc từ log phiên (triệu; trần = đầu vào mới + sinh ra)
| Phiên | Đọc đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | **Trần** | Nguồn |
|---|---|---|---|---|---|---|
| P1¹ | 11/10 13:49 | 0,10 | 0,32 | 27,51 | **0,41** | `ep007/PLAN.md` §5 |
| P2 | 11/10 15:32 | ≥ 0,08 | ≥ 0,28 | ≥ 34,79 | **≥ 0,36** | như trên |
| P3 | 13/10 02:03 | ≥ 0,31 | ≥ 0,71 | ≥ 266,85 | **≥ 1,02** | `logs/usage/p3-result-page.json`; chỉ có tiến trình cuối (26,4 h, 358 lượt) |
| P4 | 13/10 14:00 | 0,09 | 0,91 | 41,90 | **≥ 1,00** | `list_events(kinds=["result"])` phiên `session_01VsjkDmpFyRxwkeVDGhZy46`, tiến trình cuối: 20 lượt, ngữ cảnh lượt đầu 0,34 triệu, Opus $17,50 tính theo giá niêm yết (thuê bao, không phải Console) |
| **Tập 7 (P1–P4)** | | **≥ 0,58** | **≥ 2,22** | **≥ 371,05** | **≥ 2,80** | mức cảnh báo `lab`: 15 triệu → **dưới** |
| F-14 (nhà máy, song song) | 12/10 | 0,39 | 1,01 | 210,8 | **1,41** | `toolkit/factory/f14/REPORT.md` §v4 |
| Headless (thuê bao + Console) | | | | | P1 0,81 · P2 ≈ 0,5 · P3: 189 lượt (chưa cộng token) | PLAN §5 |

¹ Phiên (từ `list_sessions`): P1 `session_01UTALjtLsD1NKGK7DGGcHq1` · P2 `session_01X1ixSVAUdXqW3ZNBYE9qy9` · P3 `session_01PyBa4wV9BaBLVGdCDRJC6K` · P4 `session_01VsjkDmpFyRxwkeVDGhZy46` · F-14 `session_01AbWpo69adDsijFCpQoZehN`. "≥": log có tiến trình trước chưa lật hết (`has_more`).

**Đọc bảng:** trần phiên **không còn là chỗ tốn**. Tốn nằm ở **đọc cache**, ≥ 371 triệu: mỗi lượt của một phiên dài nạp lại cả ngữ cảnh. P3 là một tiến trình chạy 26,4 h với 358 lượt và đã đọc 266,85 triệu. Riêng tiến trình cuối của P3 đã ≈ $65 tính theo giá niêm yết; tiến trình cuối của P4 chỉ 20 lượt nhưng mở đầu với ngữ cảnh 0,34 triệu nên tới $17,50. Thước "trần ≤ 15 triệu" không bắt được chỗ này (đề xuất ở mục 6: thêm **đọc cache/phiên** và **số lượt/phiên** vào mức cảnh báo).

### 1b. Chi Console (khoá API, `total_cost_usd`)
| Chặng | $ | Gồm |
|---|---|---|
| P1 | 8,9 | kiểm độc lập 0,28 · WRITER 3,34 + 0,91 · REVIEWER C2 1,06 + G1 · kiểm mù C1/C2 · hồ sơ Tập 8 2,36 |
| P2 (C3) | 22,3 | dựng C3 8,76 · sửa S06 1,67 · sửa r3 7,54 · REVIEWER C3 1,42 + 1,09 · cổng gốc + đạo diễn ≈ 1,6 |
| P3 (C4 → G2) | **83,5** | **dựng/sửa C4 ≈ 45** (14,61 + 13,48 + 4,39 + 2,83 + 7,43 + vòng 4) · **sửa C5 vòng 1 = 25,93** (12,03 + 13,90, có agent con) · kiểm mù + đạo diễn 10,8 · REVIEWER 1,7 |
| P4 | 0,86 | xu hướng 0,01 · REVIEWER gói 0,85 |
| **Tập 7** | **≈ 115,6** | trần cảnh báo `lab` $45 → **2,6×** |
| F-14 | ≈ 12,8 | `f14/REPORT.md` §4 + §v4 |

### 1c. Giờ máy
| Chặng | Giờ | Ghi chú |
|---|---|---|
| P1 | < 1 (ước) | dữ liệu, bản đọc thử; ledger không ghi giờ |
| P2 | chưa ghi | 5 đoạn 540p + 2 lượt sửa (ledger không ghi giờ render) |
| P3 | **≈ 30** | 720p 4 vòng; **1080p 7 lần chạy** (trần 2 h, đĩa đầy 1 lần, cache hỏng 4 cảnh); Shorts dọc S21/S25 > 2 h mỗi lượt |
| P4 | ≈ 5,8 | dựng lại 1080p ≈ 2,9 (2 lần trượt vì môi trường + 1 lần bị cắt) · lấy mẫu trang ≈ 2,9 · Python ≈ 0,3 |
| **Tập 7** | **≥ 36** | mức cảnh báo `lab` ≈ 15 h → **≥ 2,4×**; ≈ 20 h trong số đó là 1080p chạy lại |
| F-14 | ≈ 10 | 1080p 1 h 55 + dựng lại ≈ 1 h 45 · nháp 7 × 15 phút · checks v3 2 h 12 + v4 2 h 48 |

### 1d. ElevenLabs (ký tự chữ gửi đi, theo ledger)
P1 1.233 (bản đọc thử 973 + 260) · P2 1.843 (C3 1.493 + S21 350) · P3 12.856 (cả tập 6.256 + lời mới 761 + seed A14 5.839) → **≈ 15.932** chữ. Mức cảnh báo `lab` là ≈ 8.500, tức **1,9×**. Riêng **seed A14 chiếm 37 %** để sửa một lỗi ASR mà về sau được xác định là luật nghe sai (A34). Số tính tiền thật thấp hơn: lượt C4 gửi 6.256 chữ nhưng chỉ bị tính 2.754, tỉ lệ ≈ 0,44 (cine-lab #103 cũng đo 0,44). Số dư tài khoản đi từ 80.540 (11/10) xuống **66.164** / 144.034 (13/10); khoản giảm này gồm cả ≥ 7.484 ký tự của một dự án khác dùng chung khoá. Làm mới 01/11.

### 1e. Số lần chủ dự án chạm
| # | Khi | Việc | Theo thiết kế? |
|---|---|---|---|
| 1 | 11/10 | lệnh "Chạy Tập 7" (P1) | có |
| 2 | 11/10 | **G1** (lô Tập 7–8) | có |
| 3 | 11/10 | **C3** (vật thể; S21 = CHÍNH) | có (khi có hình mới) |
| 4 | 12/10 | giữa chặng C4/C5: lời S25/S31, phạm vi C5, A29 (AskUserQuestion) | **không** |
| 5 | 12/10 | F-14 đóng TRƯỢT → Tập 8 `lab` | ngoài tập |
| 6 | 13/10 | chen giữa chặng: **tự đo 14,5 h không push**, A34, S25, dừng theo PID, bỏ SH3, gửi G2 ngay | **không** |
| 7 | 13/10 | **G2** (tự so khung C4/C5 để bác hồi quy) | có |
| 8 | 13/10 | P4: 4 CHẶN mới sau G2 → giao + A35–A37 | **không** |
| 9 | 13/10 | gói phát hành không chờ ChatGPT | **không** |
| 10 | 13/10 | **G3** đăng | có |
→ **10 lần chạm: 5 theo thiết kế, 4 ngoài cổng, 1 ngoài tập.** Đích D-006 là 2 cổng + G3 (+C3). Thời gian chủ dự án bỏ ra không có số đo; ước ≥ 3–4 h, gồm xem 720p, so khung C4↔C5 và đo khoảng push. Mục 6 đề xuất ghi số này.

### 1f. Xếp hạng chỗ mất (gộp $, giờ máy, chất lượng, lượt chạm)
| Hạng | Chỗ mất | Số đo | Gốc | Sửa ở (mục) |
|---|---|---|---|---|
| **1** | **Vòng sửa C5 theo lời đạo diễn máy, sửa thẳng trên bản dựng cuối** | $25,93 + agent con; cổng gốc **16 → 5–7/21**, hồi quy 10 nhịp; kéo theo 7 lần chạy 1080p; chủ dự án phải chạm thêm lần 6–7 | lời đạo diễn máy được dùng như danh sách việc phải sửa; sửa xong không đo lại trên nháp trước khi giữ; không có biên nhiễu (A32) để tách hồi quy thật khỏi nhiễu người chấm | 2 (M5: ≤ 2 vòng, chỉ giữ bản sửa vượt biên nhiễu), 3 |
| **2** | **1080p dựng lại nhiều lần** | ≈ 20 / 36 h máy; P4 dựng lại 2,9 h vì container mất (p) | dựng 1080p trước khi việc kiểm xong; trần 2 h; đĩa; thiếu đồ dùng ngoài git | 2 (M6: 1080p **một lần**), 6 |
| **3** | **Thiết kế hình giải quyết trong lúc dựng** (C3 → C4 4 vòng) | dựng C3 + C4 ≈ **$64**; S21 **7 vòng** `extra_layer_seen` 0/2, không đổi loại hình | chưa có tiền kỳ: vật thể và bố cục đi thẳng vào thế giới 3D, không qua animatic xám đo bằng cổng gốc | 2 (M2 tiền kỳ: Previz, Thiết kế hình) |
| **4** | **Phiên dài một tiến trình** | đọc cache ≥ 371 triệu; P3 26,4 h / 358 lượt; 14,5 h không push | prompt phiên dài tự viết + chạy tiếp trong container (D-011 sửa) không có điểm cắt | 3 (prompt mẫu "Chạy Tập N", mỗi mốc một phiên ngắn), 6 |
| **5** | **Kiểm định sau G2** | 4 CHẶN mới (C07, S02, S07, S09) lộ ra sau khi chủ dự án đã duyệt; +1 lượt chạm; lấy mẫu trang 2,9 h | bộ lấy mẫu trang chưa từng chạy trước G2; 3/4 CHẶN là luật bắt nhầm (A35–A37), 1 là lỗi thật (C07 cột tràn) | 2 (M5 chạy đủ bộ trên nháp), 3 (luật bắt nhầm → A35–A37, A40) |
| 6 | Seed lại giọng vì A14 | 5.839 ký tự EL (37 %), lỗi không hết | luật ASR small.en nghe sai tên riêng (A34) | 3 |
| 7 | REVIEWER ở các bước trung gian | C3 1,42 + 1,09 · C4 ý đồ 0,69 → ≈ $3,2; chưa lần nào đổi quyết định cổng | soát gói không đi tới chủ dự án | 3 |

**Kết luận mục 1:** chỗ tốn nhất **không phải** thiếu máy hay thiếu kiểm. Chỗ tốn nhất là **sửa muộn, trên bản đắt**. Thiết kế hình bị đẩy vào khâu dựng (hạng 3), lỗi chỉ được sửa sau khi đã có 1080p (hạng 1–2), và kiểm định chạy sau G2 (hạng 5). Đây đúng là hướng "nâng từ tiền kỳ" mà chủ dự án đặt ra ngày 13/10.
