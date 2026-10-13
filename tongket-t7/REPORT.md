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
| P4 | 13/10 14:00 | ≥ 0,09 | ≥ 0,91 | ≥ 41,90 | **≥ 1,00** | `list_events(kinds=["result"])` phiên `session_01VsjkDmpFyRxwkeVDGhZy46`, tiến trình cuối: 20 lượt, ngữ cảnh lượt đầu 0,34 triệu, Opus $17,50 tính theo giá niêm yết (thuê bao, không phải Console) |
| **Tập 7 (P1–P4)** | | **≥ 0,58** | **≥ 2,22** | **≥ 371,05** | **≥ 2,79** | + headless ≥ 1,31 (P1 0,81 + P2 ≈ 0,5; P3 chưa cộng) → **≥ 4,1 triệu**; mức cảnh báo `lab` 15 triệu (log phiên + headless) → **dưới** |
| F-14 (nhà máy, song song) | 12/10 | 0,39 | 1,01 | 210,8 | **1,41** | `toolkit/factory/f14/REPORT.md` §v4 |
| Headless (thuê bao + Console) | | | | | P1 0,81 · P2 ≈ 0,5 · P3: 189 lượt (chưa cộng token) | PLAN §5 |

¹ Phiên (từ `list_sessions`): P1 `session_01UTALjtLsD1NKGK7DGGcHq1` · P2 `session_01X1ixSVAUdXqW3ZNBYE9qy9` · P3 `session_01PyBa4wV9BaBLVGdCDRJC6K` · P4 `session_01VsjkDmpFyRxwkeVDGhZy46` · F-14 `session_01AbWpo69adDsijFCpQoZehN`. "≥": log có tiến trình trước chưa lật hết (`has_more`). Cột trần cộng từng dòng đã làm tròn (2,79); cộng hai cột sinh ra + đầu vào mới ra 2,80.

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
| P4 | ≈ 5,8 | theo TONGKET-INPUT h: dựng lại 1080p ≈ 2,9 (2 lần trượt vì môi trường + 1 lần bị cắt) · lấy mẫu trang ≈ 2,9 · Python ≈ 0,3 (chi tiết cộng ra 6,1). `ledger.md` ghi dựng lại ≈ 1,9 h → 5,1. Lấy 5,8 |
| **Tập 7** | **≈ 36** (P2 chưa ghi) | mức cảnh báo `lab` ≈ 15 h → **≈ 2,4×**; ≈ 20 h trong số đó là 1080p chạy lại |
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
| **1** | **Vòng sửa C5 theo lời đạo diễn máy, sửa thẳng trên bản dựng cuối** | $25,93 + agent con; cổng gốc **16/21 (đã TRƯỢT, trong ±5 % quanh ngưỡng 17/21) → 5–7/21**, 10 nhịp tụt; chủ dự án đánh giá phần lớn là nhiễu người chấm (B11, B13, B19, B29 gần trùng hình) → **hồi quy thật chưa tách được** (A32); kéo theo 7 lần chạy 1080p; chủ dự án phải chạm thêm lần 6–7 | lời đạo diễn máy được dùng như danh sách việc phải sửa; sửa xong không đo lại trên nháp trước khi giữ; không có biên nhiễu (A32) để tách hồi quy thật khỏi nhiễu người chấm | 2 (M5: ≤ 2 vòng, chỉ giữ bản sửa vượt biên nhiễu), 3 |
| **2** | **1080p dựng lại nhiều lần** | ≈ 20 / 36 h máy; P4 dựng lại 2,9 h vì container mất (p) | dựng 1080p trước khi việc kiểm xong; trần 2 h; đĩa; thiếu đồ dùng ngoài git | 2 (M6: 1080p **một lần**), 6 |
| **3** | **Thiết kế hình giải quyết trong lúc dựng** (C3 → C4 4 vòng) | dựng C3 + C4 ≈ **$63** (C3 17,97 + C4 ≈ 45); S21 **7 vòng** `extra_layer_seen` 0/2, không đổi loại hình | chưa có tiền kỳ: vật thể và bố cục đi thẳng vào thế giới 3D, không qua animatic xám đo bằng cổng gốc | 2 (M2 tiền kỳ: Previz, Thiết kế hình) |
| **4** | **Phiên dài một tiến trình** | đọc cache ≥ 371 triệu; P3 26,4 h / 358 lượt; 14,5 h không push | prompt phiên dài tự viết + chạy tiếp trong container (D-011 sửa) không có điểm cắt | 3 (prompt mẫu "Chạy Tập N", mỗi mốc một phiên ngắn), 6 |
| **5** | **Kiểm định sau G2** | 4 CHẶN mới (C07, S02, S07, S09) lộ ra sau khi chủ dự án đã duyệt; +1 lượt chạm; lấy mẫu trang 2,9 h | bộ lấy mẫu trang chưa từng chạy trước G2; 3/4 CHẶN là luật bắt nhầm (A35–A37), 1 là lỗi thật (C07 cột tràn) | 2 (M5 chạy đủ bộ trên nháp), 3 (luật bắt nhầm → A35–A37, A40) |
| 6 | Seed lại giọng vì A14 | 5.839 ký tự EL (37 %), lỗi không hết | luật ASR small.en nghe sai tên riêng (A34) | 3 |
| 7 | REVIEWER ở các bước trung gian | C3 1,42 + 1,09 · C4 ý đồ 0,69 → ≈ $3,2. Có bắt lỗi: C3 5 CHÍNH (gói C3 gửi chủ dự án), C4 ý đồ 2 CHẶN + 4 CHÍNH (đã áp) | gói C3 là gói riêng chỉ vì C3 là cổng riêng | 3 (C3 gộp G1 → REVIEWER G1 phủ; giữ REVIEWER ý đồ kiểm định) |

**Kết luận mục 1:** chỗ tốn nhất **không phải** thiếu máy hay thiếu kiểm. Chỗ tốn nhất là **sửa muộn, trên bản đắt**. Thiết kế hình bị đẩy vào khâu dựng (hạng 3), lỗi chỉ được sửa sau khi đã có 1080p (hạng 1–2), và kiểm định chạy sau G2 (hạng 5). Đây đúng là hướng "nâng từ tiền kỳ" mà chủ dự án đặt ra ngày 13/10.

---

## 2. Mô hình xưởng: thẻ vai + quy trình 6 mốc

### 2a. Nguyên tắc
- **Vai là một đầu bài, không phải một agent sống.** Mỗi vai chạy bằng một lượt headless khoá Console (`toolkit/api.sh`, 0 agent con) hoặc bằng lệnh máy, rồi thoát. Không vai nào giữ ngữ cảnh qua lúc chờ render (lesson T6-9; hạng 4 ở mục 1).
- **Vai nào không có phép thử riêng thì không thêm.** Phép thử riêng nghĩa là một phép đo có thể trượt **độc lập** với phép đo của các vai khác, và do một bên khác đo (máy, người đọc mù, hoặc chủ dự án), không phải chính vai đó tự đo. Nếu phép thử của vai trùng với phép thử của một vai đã có thì gộp hai vai làm một.
- **Quyền:** không vai nào tự quyết gu, sửa luật khoá, hay đổi kịch bản đã duyệt (CHARTER §6). Vai chỉ chọn trong phạm vi **bản tầm nhìn** đã được duyệt ở G1.
- Mẫu theo cine-lab `cine-worker.md`: mỗi vai chỉ sửa trong thư mục của gói việc mình được giao. Vai không đọc mã `checks/`. Mỗi tài sản mới phải có dòng RIGHTS. Việc cần chủ dự án quyết thì ghi vào hàng chờ, không tự quyết.

### 2b. Thẻ vai
| Vai | Đầu vào | Đầu ra | **Phép thử riêng** (ai đo) | Quyền / không được |
|---|---|---|---|---|
| **Đạo diễn sáng tạo** | logline, kịch bản C2, hồ sơ cầu, sổ gu | **bản tầm nhìn** ≤ 1 trang (`TAM-NHIN.md`): câu hỏi của phim, 3 khoảnh khắc phải nhớ, cảm xúc theo hồi, màu hồi, 3 số neo + vật thể, chỗ đặt footage | **Kiểm mù nhớ lại** trên nháp 540p (headless, 3 người xem dải khung + lời): ≥ 2/3 người kể lại được **≥ 2/3 khoảnh khắc** đã ghi trong bản tầm nhìn, và nói đúng câu hỏi của phim. Phép thử này khác cổng gốc: cổng gốc đo nghĩa từng nhịp khi tắt tiếng, còn phép này đo cái người xem nhớ được sau cả tập (gần với L3 dòng 1 và 6) | chọn phương án trong phạm vi bản tầm nhìn; **không** đổi kịch bản, gu, nhạc |
| **Thiết kế hình** | bản tầm nhìn, thư viện hình, gen CHARTER §4 | **bảng vật thể**: mỗi vật thể (số neo, danh từ chính) có ảnh xoay 3 góc + clip 3 s ở trạng thái đổi, kèm RIGHTS cho tài sản ngoài | **Nhận dạng mù**: 2 người đọc headless chỉ xem clip 3 s (tắt tiếng), phải gọi đúng vật thể và chiều đổi (mọc/giảm/tách) ≥ 2/2. Máy kiểm gen (bảng màu kênh, không mặt, low-poly) | thêm vật thể vào thư viện sau G1; **không** dùng vật thể có ≥ 2 vòng trượt nhận dạng |
| **Previz** | kịch bản, bảng nhịp, bảng vật thể, timeline từ bản đọc thử | **animatic 540p xám** (khối, máy quay, thời điểm theo lời thật, chưa có chất liệu) | **Cổng gốc tắt tiếng trên animatic**, đọc theo biên nhiễu A32: mọi nhịp loại 1 đạt. Đây là thước đã dùng ở C3/C4, chỉ dời lên **trước khi** dựng đẹp. S21 Tập 7 lẽ ra lộ ở đây với ≈ $3, thay vì qua 7 vòng | đổi bố cục và máy quay; **không** đổi lời |
| **Editor** | nháp 540p theo cảnh, stem lời/nhạc/SFX, bản đồ liền mạch | **danh sách cắt**: J/L-cut ở ranh giới cảnh, nhịp, chỗ lặng, mid-roll | **Nhịp trên nháp**: quãng có lời mà không đổi hình > 8 s = 0; freezedetect ≥ 3 s có lời đè ≤ 30 s/tập. **Kiểm mù "chỗ muốn tua"**: không đoạn nào bị ≥ 2/3 người nêu | đổi thứ tự shot trong cảnh, độ dài lặng; **không** đổi lời |
| **Giám sát liền mạch** | bản tầm nhìn, kịch bản, `numbers.md`, nháp | **bản đồ liền mạch** (`BAN-DO-LIEN-MACH.md` → `map:` trong `episode.yaml`) + báo cáo lệch | **Máy đối chiếu nháp với bản đồ**: mỗi số neo có vật thể hiện trong ±1 s quanh từ đọc (cine Q29); mỗi chuyển hồi dùng đúng kiểu đã khai; tông màu trung bình mỗi hồi khớp màu đã khai; số trên hình = số trong lời (L1 có sẵn); footage có năm + nguồn trên hình | báo lệch, mở việc cho vai sở hữu; **không** tự sửa hình |
| **Line producer** | trần theo format, ledger, `build-report.json`, log phiên | **sổ chi theo mốc** ($ Console, giờ máy, EL, đọc cache, lượt chạm), mỗi mốc một dòng | **Sổ chi khớp nguồn** (máy): mỗi dòng sổ khớp `total_cost_usd` headless và 4 số `from_events.py` ±2 %; giờ máy khớp `build-report.json`. Kèm **luật ngắt** (không phải phép thử): chi một mốc vượt 150 % ngân sách mốc → dừng mốc, báo trong gói kế tiếp; 1080p chạy lần 2 phải có lý do ghi trước. **Không** cắt bước chất lượng (CHARTER §5) | ngắt và báo; **không** quyết chi tiêu mới |
| WRITER (có sẵn) | hồ sơ cầu, `story.md` | kịch bản, bảng nhịp, 3 móc | kiểm mù lời C2 (6 + 1) + M1–M6 | như cũ |
| K (có sẵn) | `checks-appeal.md` | luật khoá + LOCK | selftest; 0 lệch trên tập cũ; **mới (A40):** luật CHẶN phải bắt được ≥ 1 lỗi thật trên đối chứng và không báo sai trên 3 tập đã đăng | như cũ |
| Nhà máy (có sẵn) | spine, thế giới, lời | nháp 540p, 1080p, Shorts | verify đoạn, đồng bộ ±0,2 s, trùng byte so với cache | như cũ |

**Vai không thêm:**
- **REVIEWER trung gian**: không có phép thử riêng. Giữ REVIEWER (headless) ở gói G1 (nay gồm cả phần C3 cũ), **ý đồ kiểm định trước M5** (Tập 7: REVIEWER C4 ý đồ bắt 2 CHẶN + 4 CHÍNH) và gói G2 (mục 3).
- **"Đạo diễn máy" như một vai sửa**: lượt đạo diễn máy **đã là chẩn đoán** (CHARTER §4 L2, `episode.md` §1). Điều mới: lời phê chỉ thành việc sửa khi phép thử của vai sở hữu (Editor/Previz) **cũng trượt** ở đúng chỗ đó — ở C5 Tập 7, nhận xét lặp ở ≥ 2 lượt được sửa trên cả tập mà không phép thử nào trượt trước (hạng 1 ở mục 1).

### 2c. Quy trình 6 mốc
| Mốc | Việc (vai) | Đầu ra | Cổng / dừng | Chủ dự án |
|---|---|---|---|---|
| **M1 Phát triển** | Việc 0 (dữ liệu, mô hình, kiểm độc lập) · C1 · C2 (WRITER, kiểm mù lời) | kịch bản v-cuối, bảng nhịp, `numbers.md` | M1–M6, kiểm mù lời; ≤ 2 vòng | — |
| **M2 Tiền kỳ** | bản tầm nhìn (ĐDST) · bảng vật thể (TKH) · animatic 540p xám (Previz) · bản đồ liền mạch (GSLM) · ngân sách (LP) · footage: RIGHTS trước khi tải | `TAM-NHIN.md`, `BAN-DO-LIEN-MACH.md`, `preprod/animatic.mp4` | nhận dạng mù + cổng gốc animatic; ≤ 2 vòng/lỗi | **G1**: duyệt kịch bản + vật thể/animatic + tiêu đề nháp (một gói ≤ 3 câu). **Gộp C3** |
| **M3 Sản xuất nháp 540p** | nhà máy dựng thế giới, giọng (một lần), nhạc/SFX/footage | nháp 540p theo cảnh | verify đoạn, đồng bộ | — |
| **M4 Hậu kỳ** | Editor: J/L-cut, nhịp · màu theo hồi · mix | nháp 540p cả tập | nhịp trên nháp | — |
| **M5 Kiểm định trên nháp** | **L1 đủ bộ, gồm lấy mẫu trang** · cổng gốc · nhớ lại (ĐDST) · liền mạch (GSLM) · REVIEWER ý đồ (trước) + gói G2 | gói G2 + nháp 540p để xem + 3 khung tĩnh cảnh đinh render 1080p (≈ 5 phút máy) | **≤ 2 vòng mỗi lỗi**. Một vòng chỉ được giữ khi điểm vượt bản tốt nhất **ngoài biên nhiễu** (A32); hết 2 vòng → trước/sau cho chủ dự án | **G2**: phiếu L3 trên nháp |
| **M6 Giao** | **1080p một lần** + **1 Short** · L1 kỹ thuật trên 1080p (độ phân giải, loudness, C14, SSIM so với nháp ≥ 0,97) | master, Short, gói (tiêu đề, mô tả, tag; **không thumbnail**) | sai lệch kỹ thuật thì sửa mà không mở lại G2 | **G3** đăng |

**Chủ dự án chạm: G1, G2, G3** (+ lệnh "Chạy Tập N"). Ngoài cổng chỉ có các ngoại lệ phải hỏi của CHARTER §5.

### 2d. Đánh giá đề xuất 2
| | |
|---|---|
| **Ưu** | Lỗi hình lộ ra ở animatic, nơi một vòng tốn ≈ $3 và < 1 h thay vì một vòng C4/C5 tốn $13–26. Kiểm định đủ bộ chạy **trước** G2, nên lần chạm số 8 của mục 1 không còn. Bỏ được ≈ 20 h 1080p chạy lại. Mỗi vai có thước để biết khi nào xong, nên vòng lặp có điểm dừng. |
| **Nhược** | G1 đến muộn hơn ≈ 0,5 ngày vì phải đợi animatic. Nếu chủ dự án bác kịch bản ở G1 thì mất phần tiền kỳ (≈ $5–8, 2–3 h). Thêm 2 mẫu tài liệu. Phép thử "nhớ lại" và "nhận dạng" **chưa hiệu chuẩn**. |
| **Chất lượng** | Tăng: hình được thiết kế trước khi dựng. Có thêm phép đo cái người xem nhớ được. Không bỏ bước kiểm nào, chỉ dời lên sớm hơn. |
| **Thời gian / token** | Giờ máy ước ≈ −60 % (mục 6). Console ước ≈ −65 %. Token phiên: nhiều phiên ngắn thay cho một phiên 26 h, nên đọc cache giảm ≈ 5×, ước theo số lượt. |
| **Rủi ro** | (1) Nháp 540p giấu lỗi chỉ có ở 1080p (chữ nhỏ, răng cưa) → M6 có L1 kỹ thuật + SSIM; chữ đo theo hộp chữ ở spine, không đo trên ảnh. (2) Hai phép thử mới bị Goodhart → hiệu chuẩn trên Tập 6/7 trước khi dùng (đường 1 ở mục 6). (3) Chủ dự án chấm L3 trên nháp 540p có thể lệch với bản cuối → G2 kèm 3 khung tĩnh 1080p của cảnh đinh. (4) Phép thử Previz và luật giữ vòng dựa vào biên nhiễu cổng gốc **A32 đang mở** → cần lô K đo A32 trước Tập 8 M2; chưa có thì dùng tạm "≥ 2 lượt đọc lại đồng ý". |

Mẫu (bản nháp, **chưa đưa vào playbook**): `tongket-t7/de-xuat/playbook/templates/TAM-NHIN.md`, `BAN-DO-LIEN-MACH.md`.

---

## 3. BỎ (mỗi mục bỏ đi kèm phần thêm thay vào)

| Bỏ | Thay bằng | Ưu | Nhược | Chất lượng / thời gian / token | Rủi ro |
|---|---|---|---|---|---|
| **C3, C4 là cổng riêng** (C3 là một lượt chạm riêng; C4 animatic dựng trên thế giới thật) | Phép thử của C3 (clip có chuyển động + âm, cổng gốc) **dời lên tiền kỳ M2**, gộp vào **G1**. C4 → animatic xám ở M2 + kiểm định trên nháp ở M5 | bớt 1 lượt chạm; lỗi loại S21 lộ trên animatic ≈ $3 thay vì 7 vòng | G1 nặng hơn: chủ dự án xem animatic ≈ 10 phút | chất lượng + (hình thiết kế trước khi dựng) · Tập 7 C3 + C4 ≈ $63 → ước ≈ $15–20 · −1 phiên | animatic xám đánh giá thấp vật thể đẹp → G1 kèm clip 3 s của từng vật thể (bảng vật thể) |
| **REVIEWER trung gian** (C3 ×2, issue tự động) | REVIEWER headless **ở gói G1 (gồm phần C3 cũ), ý đồ kiểm định trước M5, gói G2**. Soát số và soát gen giữa chặng giao cho L1 + Giám sát liền mạch | −$2,5/tập; −2 lượt chờ | mất đọc chéo ở gói C3 riêng → gói đó không còn | chất lượng ≈: 5 CHÍNH của REVIEWER C3 nằm ở gói gửi chủ dự án, nay REVIEWER G1 soát; 2 CHẶN + 4 CHÍNH của REVIEWER C4 ý đồ được giữ bằng lượt ý đồ M5 | lỗi chữ ở gói trung gian không ai đọc → gói trung gian không còn (không gửi chủ dự án) |
| **Prompt phiên dài tự viết** (PLAN tập §7, mỗi chặng 10–15 dòng, chép lại luật) | **Một prompt mẫu "Chạy Tập N"** (`de-xuat/playbook/prompts/CHAY-TAP-N.md`): chủ dự án dán 1 dòng + câu trả lời cổng; luật nằm ở playbook; mốc kế đọc từ PLAN tập mục 1 | chủ dự án không cần đọc/sửa prompt; luật không trôi giữa các bản chép; phiên ngắn theo chặng | phiên phải suy ra mốc từ PLAN (PLAN sai → chạy sai chặng) | token: luật đọc một lần từ playbook; phiên ngắn → đọc cache ↓ (mục 1a: 371 triệu chủ yếu do phiên dài) | PLAN mục 1 ghi sai mốc → `verify.sh` kiểm thêm "mốc PLAN khớp tệp gates/" (việc nhà máy nhỏ) |
| **Luật đo không bắt lỗi thật** | → `checks-appeal.md` **A40** (nguyên tắc: CHẶN bị chấp nhận giao ở ≥ 2 tập → sửa/hạ; CHẶN mới cần đối chứng dương thật + 0 báo sai trên 3 tập) cùng **A34–A37** đã mở. Ngoài `checks/`: lượt đạo diễn máy và thước nhịp F-14 **chỉ chẩn đoán**; lời phê chỉ thành việc sửa khi phép thử của vai sở hữu cũng trượt ở đó | Tập 7: 4/5 nhóm CHẶN lúc giao là thủ tục; bỏ được seed lại 5.839 ký tự và 1 lượt chạm | luật hạ cấp có thể bỏ sót lỗi thật về sau | chất lượng ≈/+ (sau vòng sửa C5 theo lời đạo diễn, cổng gốc đo 16/21 → 5–7/21; phần nhiễu chưa tách được, A32) | hạ nhầm một luật bắt lỗi thật hiếm → A40 chỉ xét luật bị chấp nhận giao ở ≥ 2 tập, K quyết, chủ dự án duyệt |
| **3 vòng mỗi lỗi** (`episode.md` §1, lessons V1) | **≤ 2 vòng mỗi lỗi** + chỉ giữ vòng vượt bản tốt nhất ngoài biên nhiễu (A32) | đúng nguyên tắc 13/10 "kiểm–sửa không thành vòng lặp vô tận"; S21 Tập 7 không đổi gì qua 7 vòng | lỗi khó cần vòng 3 đổi loại hình (T6-7) → dời việc đổi loại hình lên Previz (vòng 2 trên animatic là lúc đổi loại hình) | thời gian −; chất lượng ≈ (vòng 3 Tập 6/7 chưa từng đạt) | ít vòng hơn → nhiều trước/sau hơn ở G2 → đếm ở mục 6 (lượt chạm vẫn là G2) |
| **Thumbnail + Shorts 2–3** | **1 Short, 0 thumbnail** (chủ dự án 13/10) → **A38** (F11/P01/SH) | −2 h/Short dọc (Tập 7 > 2 h/lượt); không còn gói ChatGPT ảnh | ít điểm chạm Shorts; CTR phụ thuộc khung YouTube tự chọn | thời gian −; quyết định đã có | YouTube tự chọn khung → G3 ghi khung đề nghị (1 trong 3 khung 1080p đẹp nhất) để chủ dự án đặt nếu muốn |

**Đã ghi:** `checks-appeal.md` A38–A41 (mục 5 hàng chờ). **Chưa áp:** `episode.md` §1 (3 → 2 vòng), `prompts/` (RUN/P1–P3 → CHAY-TAP-N), CHARTER §5 (bảng cổng: bỏ dòng C3; dòng G2 còn ghi thumbnail + ChatGPT), CHARTER §1 ("kèm 2–3 Shorts mỗi tập" → 1 Short) — hai chỗ CHARTER này trái quyết định 13/10 (1 Short, 0 thumbnail), sửa cùng lượt áp. Các mục này chờ chủ dự án duyệt (gói, câu 1).

---

## 4. Nâng hình–âm (giữ gen CHARTER §4: low-poly, màu kênh, không chân thực ảnh, nhân vật không mặt, không trang trí vô nghĩa)

Mọi mục dưới đây được **thử trước trên tập cũ** (đường 1: dựng lại một đoạn Tập 7 ở nháp 540p trên nhánh `factory-*`, so trước/sau bằng phép thử của vai sở hữu). Chỉ khi thử đạt mới đưa vào tập đang chạy, và chỉ ở ranh giới cổng (đường 2). Giờ máy dưới đây là **ước**, tính theo Tập 6–7 (1080p không cache ≈ 2,8 h cho 537 s) và cine-lab #88 (nháp 0,3 s/khung so với 2,9 s/khung ở 1080p).

| Mục | Làm gì | Tài sản / công cụ | Quyền | Giờ máy · $ Console (ước) | Vai · phép thử | Ưu / nhược / rủi ro |
|---|---|---|---|---|---|---|
| **4a Cảnh đinh 3D** | 4–6 cảnh/tập (mở, ngoặt, số neo, kết), dựng riêng; không dùng lại bố cục của tập trước (cine §11.3). Ánh sáng có nguồn, vật liệu có vân phẳng theo bảng màu (cine #97: nội thất khối thô và tối bị chấm thấp lặp lại) | three.js đã có (`toolkit/factory/world/vendor`); mô hình low-poly **CC0**: Kenney, Quaternius; Poly Pizza (CC0 hoặc CC BY, đọc từng mẫu). Tô lại theo token màu kênh | CC0: dòng RIGHTS; CC BY: dòng RIGHTS + ghi công trong mô tả. **Không** dùng mẫu chân thực ảnh hay mẫu có mặt người | nháp +10–15 phút; 1080p +0,5–1 h/tập (cảnh đinh nặng gấp ≈ 2–3 lần cảnh thường) · +$3–5 (lượt Thiết kế hình + dựng cảnh đinh) | Thiết kế hình · nhận dạng mù + kiểm mù nhớ lại K1–K3 | **Ưu:** khoảnh khắc nhớ được (L3 dòng 1, 6). **Nhược:** +1 lượt Thiết kế hình ở M2 (≈ $3–5). **Rủi ro:** trôi khỏi gen (chi tiết thừa) → máy kiểm bảng màu + "mỗi chi tiết mang nghĩa" ở bảng vật thể |
| **4b Đa dạng khung nhìn** | Bản tầm nhìn khai khung nhìn chủ đạo theo hồi; không khung nào > 20 % thời lượng; ≤ 2 cảnh liền cùng bố cục (cine Q26). Một bối cảnh không quá 25 % hoặc 90 s liền (cine #96) | thước chỉ báo có sẵn (`toolkit/indicators/`, cụm lớn nhất %: Tập 5 6,8 %) | — | 0 (đo trên spine/nháp) · ≈ $0 (lệnh máy) | Previz (trên animatic) · Giám sát liền mạch (trên nháp) | **Ưu:** đo được ngay từ animatic. **Nhược:** thước gộp cảnh tối cùng bố cục (cine #71) → báo cả hai số. **Rủi ro:** Goodhart (đổi góc vô nghĩa) → chỉ báo, không ngưỡng cho tới khi hiệu chuẩn |
| **4c Vật thể thật cho số neo** | ≤ 3 số neo, mỗi số một vật thể đã đặt tên trong lời ("the stack", "the bar") hiện trong ±1 s quanh từ đọc; lặng 0,7–0,9 s trước số | thư viện vật thể của kênh (tự dựng) | tự làm | ≈ 0 · ≈ $1 (nhận dạng mù 2 người đọc/vật thể) | Thiết kế hình (nhận dạng) · Giám sát liền mạch (±1 s, A41b) | **Ưu:** số neo nằm trong cổng gốc tắt tiếng. **Nhược:** vật thể chỉ nói chiều, không nói giá trị chi tiết (T6-7, T6-13) → giá trị nằm trên nhãn đồ thị, vật thể không mang giá trị trung gian. **Rủi ro:** vật thể đọc sai nghĩa (S25 "the bar" bị đọc thành "phải vượt") → nhận dạng mù hỏi cả **ý**, không chỉ hỏi tên |
| **4d J/L-cut + màu theo hồi** | Editor đặt J/L-cut ở mọi chuyển hồi (tiếng cảnh sau vào trước 0,3–1,0 s); mỗi hồi một màu chủ đạo trong bảng màu kênh (khai ở bản tầm nhìn; **gu → chủ dự án duyệt ở G1**) | `splice.py` cần cho tiếng lệch biên đoạn (đoạn sau lấn sang đoạn trước) → **việc nhà máy** `factory-*` (BACKLOG, đầu Tập 8 hoặc trước Tập 9); màu hồi = token màu theo `map.color` | — | ≈ 0 (mix lại) · $0/tập; phát triển một lần ≈ 1 phiên nhà máy (≈ $5–10) | Editor · Giám sát liền mạch (A41b) | **Ưu:** liền mạch giữa hồi, Vox-like. **Nhược:** đụng nhà máy giữa tập → chỉ làm ở ranh giới. **Rủi ro:** lời đè lời ở J-cut → luật lời không chồng ±0,2 s (có sẵn: đồng bộ) |
| **4e SFX ghi âm thật** | Thay tiếng tổng hợp (whoosh, land) bằng tiếng ghi âm thật cho vật thể đổi trạng thái (giấy, kim loại, gỗ, tiền xu); không tăng mật độ (F-2: ≤ 21,7 sự kiện/phút đã là cảnh báo) | Freesound (lọc **CC0** / **CC BY 4.0**; bỏ CC BY-NC, Sampling+); Sonniss/BBC **không** dùng (giấy phép không phải CC0/CC BY; BBC RemArc là phi thương mại) | mỗi tệp một dòng RIGHTS (URL, tác giả, giấy phép trích nguyên văn, ngày tải); CC BY → ghi công trong mô tả | tải + chuẩn hoá ≈ 0,5 h lần đầu, sau đó dùng lại thư viện · ≈ $0,5–1 (tìm + kiểm quyền headless) | Editor · phép thử "mỗi vật đổi trạng thái có tiếng riêng" (chỉ báo cine Q28c đã có) | **Ưu:** âm nghề thật, người nghe tin hơn. **Nhược:** tốn công tìm/cắt lần đầu. **Rủi ro:** Wikimedia/Freesound chặn proxy (cine #82) → tải qua API có khoá hoặc chủ dự án tải tay một lần |
| **4f Nhạc do người sáng tác, CC BY** (không nhạc AI) | Nhạc hiệu + 3 cue theo hồi của một tác giả có giấy phép **CC BY 4.0**, cắt theo bản đồ căng (thay nhạc bằng mã của D-010 §5) | ứng viên cần **đọc giấy phép lúc tải**: Kevin MacLeod (incompetech), Scott Buckley, Chris Zabriskie; Free Music Archive (lọc CC BY) | dòng RIGHTS + ghi công trong mô tả; **không** NC/ND, không YouTube Audio Library (cine §5.4), không nhạc AI | ≈ 0 · ≈ $0,5 (chọn + cắt cue theo bản đồ căng) | Editor · cue đổi theo hồi, không lặp > 60 s (cine Q28) | **Ưu:** chất lượng nhạc vượt nhạc bằng mã. **Nhược:** không chốt hợp âm đúng từ khoá như nhạc bằng mã → cắt theo câu nhạc; **đổi D-010 §5 = gu → chủ dự án quyết**. **Rủi ro:** Content ID (bên thứ ba đăng ký nhầm bản CC BY) → giữ bản lưu giấy phép để kháng nghị; chọn tác giả không đăng ký Content ID; thử đăng không công khai trước G3 |

**Chi phí cộng thêm mỗi tập khi đã vào nếp (ước):** +$5–8 Console (Thiết kế hình, Previz), +0,5–1,5 h giờ máy (cảnh đinh). Phần này nằm trong đích ở mục 6 vì đã bỏ được các vòng sửa muộn.

---

## 5. Chính sách footage ngoài: đề xuất sửa CHARTER §4 + RIGHTS.md

Bản nháp đầy đủ: `tongket-t7/de-xuat/CHARTER-s4.md` (thêm 2 dòng vào §4, CHARTER vẫn < 2 trang) và `tongket-t7/de-xuat/RIGHTS-sF.md` (§F1–F5). Tóm tắt:
- **Danh sách trắng, theo thứ tự ưu tiên:** (1) tác phẩm của chính phủ liên bang Mỹ, phạm vi công cộng (trừ ảnh của nhà thầu, ảnh được tặng, phù hiệu) → (2) Natural Earth / TIGER / **dữ liệu** OSM do kênh tự vẽ (ODbL, ghi công; không dùng tile vì phần đồ hoạ tile là BY-SA) → (3) CC0 / PDM → (4) Pexels / Pixabay, **đọc giấy phép lúc tải**, lưu bản chụp có băm → (5) CC BY.
- **Danh sách cấm:** NC, ND, BY-SA cho hình, quyền không rõ, logo/nhãn hiệu, người thật trong vai nhân vật, ảnh AI trình bày như tư liệu.
- **Trần:** ≤ 20 % thời lượng, **Tập 8 thử ≤ 15 %**, mỗi lần ≤ 6 s liền, không ở 5 s đầu.
- **Giữ ngôn ngữ hình:** luôn có chuyển động, `focus` nằm trên dải chú thích (#49), phủ tông kênh, hoà từ cảnh 3D nối tiếp (#93); ưu tiên đặt ảnh **trong thế giới**; nguồn ảnh bên phải, nguồn số bên trái (#50).
- **Trung thực:** ảnh minh hoạ không làm bằng chứng; tư liệu ghi năm + nguồn trên hình.
- **Máy kiểm:** `checks-appeal.md` **A39** (CHẶN khi thiếu hồ sơ quyền, giấy phép cấm hoặc vượt trần; CHÍNH khi thiếu chữ năm + nguồn).

| | |
|---|---|
| **Ưu** | Thêm chất thật: nơi chốn, thời kỳ, con người thật làm bối cảnh. Đỡ phải dựng 3D cho những cảnh chỉ có vai trò bối cảnh. Nguồn miễn phí, quyền rõ ràng. |
| **Nhược** | Mỗi tệp phải kiểm quyền (≈ 5–10 phút). Có rủi ro "đổi chất liệu" (cine #93 đo 2/3). Phải sửa gen được bảo vệ, việc này thuộc quyền chủ dự án. |
| **Chất lượng** | + nếu đặt ảnh trong thế giới hoặc hoà từ 3D. − nếu dùng toàn khung và cắt thẳng (cine #93). Trần 15 % ở Tập 8 giới hạn phần rủi ro. |
| **Thời gian / token** | Tìm + kiểm quyền ≈ 0,5–1 h/tập (vai Thiết kế hình, headless ≈ $1–2). Giờ máy ≈ 0, ảnh rẻ hơn cảnh 3D. |
| **Rủi ro** | Pháp lý: ảnh liên bang do nhà thầu chụp, giấy phép Pexels/Pixabay đổi theo thời gian → bản chụp giấy phép có băm, A39 chặn. Trung thực: người xem đọc ảnh minh hoạ như bằng chứng → nhãn + không đi cùng claim. Proxy chặn Wikimedia (cine #82) → nguồn bậc 1 tải qua API của cơ quan. |

---

## 6. Đích kinh tế mặc định

### 6a. Tập 9 trở đi (`lab`): 8–12 h máy · Console $25–40 · chủ dự án ≈ 1–1,5 h/tập
| Mốc | Console (ước) | Giờ máy (ước) | Tập 7 thực (để so) |
|---|---|---|---|
| M1 Phát triển | $6–8 (Việc 0, WRITER 1–2 lượt, kiểm mù C1/C2) | ≤ 0,5 | P1 $8,9 |
| M2 Tiền kỳ | $6–10 (Thiết kế hình, Previz animatic, nhận dạng + cổng gốc, REVIEWER G1) | 1–1,5 (animatic 540p xám) | C3 + C4: ≈ $63, giờ chưa ghi |
| M3 Nháp 540p | $6–10 (dựng thế giới 1–2 lượt headless) | 1,5–2 | — (Tập 7 dựng thẳng 720p/1080p) |
| M4 Hậu kỳ | $2–3 | ≤ 0,5 | — |
| M5 Kiểm định trên nháp | $5–8 (cổng gốc, nhớ lại, ≤ 2 vòng sửa, REVIEWER ý đồ + G2; 3 khung tĩnh 1080p) | 2–3 (đủ bộ, gồm lấy mẫu trang; ít hơn khi A29 qua K) | sửa C5 $25,93 + kiểm $10,8; checks sau G2 2,9 h |
| M6 1080p + 1 Short | ≤ $1 | 3–4 (1080p một lần ≈ 2,8–3 h + Short + L1 kỹ thuật) | 1080p ≈ 20 h (7 + 3 lần chạy) |
| **Cộng** | **$25–40** | **8–12 h** | **$115,6 · ≥ 36 h** |

**Chủ dự án:** G1 30–40 phút (kịch bản + animatic + vật thể) · G2 25–35 phút (xem nháp 540p + 3 khung 1080p + phiếu L3) · G3 10–15 phút → **≈ 1–1,5 h**. Tập 7: 10 lần chạm, ước ≥ 3–4 h.
**Token:** **giữ** mức cảnh báo trần 15 triệu (log phiên + headless; Tập 7 ≥ 4,1, dưới). **Thêm hai mức cảnh báo mới:** **đọc cache ≤ 60 triệu/tập** (Tập 7 ≥ 371) và **≤ 150 lượt/phiên** (P3: 358). Hai thước này bắt đúng chỗ tốn của Tập 7, thước trần thì không bắt được (mục 1a).
**EL:** ≤ 8.500 ký tự chữ/tập `lab` (giữ mức cũ). Giọng sinh một lần ở M3; sinh lại chỉ khi lời đổi (Tập 7 có 5.839 ký tự seed lại vì A14).
**Ghi mới vào PLAN tập §5 (vai Line producer):** $ theo mốc · giờ máy theo mốc · đọc cache · số lượt · **số lần chủ dự án chạm + phút ước**.

### 6b. Tập 8 là tập chuyển đổi: 15–20 h máy · Console $45–60
- **Ranh giới:** P1 Tập 8 đang chạy theo mẫu cũ (phiên song song, không chạm). Mô hình mới vào **sau G1 Tập 8**: chặng kế làm phần tiền kỳ M2 (bản tầm nhìn, bảng vật thể, animatic, bản đồ liền mạch, footage ≤ 15 %), rồi M3–M6. Nếu G1 Tập 8 đã ghi "cần C3" thì bước kiểm tiền kỳ thay đúng chỗ của C3, **không thêm lượt chạm**. Nếu không có C3, chủ dự án chạm thêm 1 lần, chỉ ở Tập 8.
- **Lý do Tập 8 tốn hơn:** lần đầu tải và kiểm quyền SFX/nhạc/footage (≈ 1–2 h), lần đầu viết bản tầm nhìn và bản đồ liền mạch, và hai phép thử mới chạy song song với cổng cũ để so.
- **Đường 1 (thử trên tập cũ, trước hoặc song song P1→G1 Tập 8, nhánh `factory-t7lab`, không chạm `ep008`):**
  1. animatic xám của S21/S25 Tập 7 + cổng gốc: animatic có bắt được lỗi mà C3–C5 mất 7 vòng mới thấy không;
  2. hiệu chuẩn "nhớ lại" trên Tập 6/7 bản giao, đối chứng âm là Tập 1;
  3. J/L-cut + màu hồi + SFX thật trên một đoạn nháp của Tập 7;
  4. chạy checks đủ bộ trên nháp 540p và trên 1080p của Tập 7 rồi so (A41a).

  Ước ≈ $8–12, 6–8 h máy. Phần này tính vào việc không phải tập (CHARTER §2.3 cho tối đa 20 %). Thử nào trượt thì không đưa mục đó vào Tập 8, và Tập 8 làm theo cách cũ cho mục đó.

| | |
|---|---|
| **Ưu** | Đích bám đúng các chỗ mất đã đo ở mục 1. Có thêm hai thước (đọc cache, lượt chạm) bắt được thứ thước trần bỏ sót. Tập 8 không phải đánh cược vì mọi mục đã thử trên tập cũ trước. |
| **Nhược** | Đích của Tập 9 dựa trên ước, chưa có tập nào chạy theo mô hình 6 mốc. Tập 8 tốn hơn Tập 9 khoảng $15–20. |
| **Chất lượng** | Không đổi lấy chi phí: mọi bước kiểm giữ nguyên, chỉ dời lên sớm hơn. Vượt đích thì báo trong gói, **không** cắt bước chất lượng (CHARTER §5). |
| **Rủi ro** | Đích sai do ước → sau Tập 8 và 9 đo lại theo mốc rồi sửa đích ở tổng kết Tập 9. Nháp 540p không đủ để chấm L3 → G2 kèm 3 khung tĩnh 1080p của cảnh đinh (mục 2d). |

---

## 7. Dọn PLAN.md kênh (đã làm)
`PLAN.md` gốc giảm từ 30 dòng còn 29 dòng, nhưng nội dung đổi hẳn: bảng tập chỉ còn trạng thái hiện hành; mục "Tiếp" giữ 4 việc (gói này, lô K Tập 8, lấy mẫu trang trước G2, đường thử trên tập cũ); việc treo chỉ giữ những việc còn mở; hàng chờ K trỏ về `checks-appeal.md` (A29, A32–A41). Bỏ những dòng đã xong hoặc lỗi thời: nhạc hiệu C3 Tập 6, M4 hiệu chuẩn G1 Tập 6, K4.0–K4.2, phiên K lô tongket-t5. Bản cũ giữ nguyên văn ở `archive/PLAN-kenh-history.md`.
**Rủi ro:** P1 Tập 8 chạy song song có thể sửa `PLAN.md` → phiên merge giữ bản này và thêm dòng trạng thái Tập 8 của P1.

---

## 8. Gói gửi chủ dự án (≤ 3 câu)

**Câu 1 — Mô hình xưởng 6 mốc** (mục 2–3): 6 vai có phép thử riêng; tiền kỳ có animatic và được duyệt ở G1 (gộp C3); kiểm định đủ bộ trên nháp trước G2, ≤ 2 vòng mỗi lỗi; 1080p một lần; 1 Short; chủ dự án chạm G1/G2/G3; bỏ C3/C4 cổng riêng, REVIEWER trung gian, prompt dài (→ "Chạy Tập N"); A40 cho luật bắt nhầm; sửa CHARTER §1/§5 cho khớp 1 Short, 0 thumbnail.
(a) duyệt cả gói, vào Tập 8 sau G1 · (b) duyệt nhưng giữ 3 vòng mỗi lỗi · (c) chỉ thử trên tập cũ, Tập 8 làm theo mẫu cũ.
**Khuyến nghị (a).** Chỗ mất hạng 1–3 của Tập 7 (≈ $90 Console, ≈ 20 h máy 1080p chạy lại, S21 qua 7 vòng) đều do sửa muộn trên bản đắt. Đánh đổi: G1 muộn hơn ≈ 0,5 ngày, và hai phép thử mới phải hiệu chuẩn trên tập cũ trước.

**Câu 2 — Footage ngoài + âm thanh** (mục 4–5): sửa CHARTER §4 (thêm 2 dòng) + RIGHTS §F (danh sách trắng 5 bậc, danh sách cấm, ≤ 15 % ở Tập 8, năm + nguồn trên hình); SFX ghi âm thật CC0/CC BY; nhạc do người sáng tác, CC BY, thay nhạc bằng mã (đổi D-010 §5, đây là gu).
(a) duyệt cả hai · (b) duyệt footage + SFX, giữ nhạc bằng mã · (c) hoãn.
**Khuyến nghị (b) cho Tập 8, xét nhạc ở G1 Tập 9.** Footage và SFX đã có thủ tục quyền và luật A39. Nhạc CC BY có rủi ro Content ID và không chốt hợp âm đúng từ khoá; anh nên nghe thử clip 2 cue (đường thử trên tập cũ) trước khi đổi gu. Đánh đổi: giữ nhạc bằng mã thì chất nhạc Tập 8 không tăng; footage tốn +0,5–1 h/tập kiểm quyền.

**Câu 3 — Đích kinh tế** (mục 6): Tập 9+ đặt đích 8–12 h máy, $25–40, chủ dự án ≈ 1–1,5 h; Tập 8 chuyển đổi 15–20 h, $45–60. Thêm hai mức cảnh báo: đọc cache ≤ 60 triệu/tập và ≤ 150 lượt/phiên. Ghi thêm số lần chạm + phút chủ dự án.
(a) duyệt · (b) duyệt đích, chưa thêm mức cảnh báo mới.
**Khuyến nghị (a).** Ở Tập 7, thước trần (2,79 triệu, đạt) không bắt được chỗ tốn thật (đọc cache ≥ 371 triệu). Vượt đích chỉ là cảnh báo, không cắt bước chất lượng. Đánh đổi: thêm cột ghi sổ cho mỗi mốc; đích Tập 9 là ước, chưa có tập nào kiểm chứng.

**Trả lời gọn:** `1 a/b/c · 2 a/b/c · 3 a/b`

REVIEWER (headless, khoá Console): `tongket-t7/review/REVIEW-r1.md` (ĐẠT có sửa, $1,67; đã áp) · `REVIEW-r2.md`.
