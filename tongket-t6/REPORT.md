# Tổng kết Tập 6 + áp quyết định chủ dự án 11/10 (Phiên T6, 11/10/2026)

Nhánh `tongket-t6` (từ `main` f614e6b). Quyết định chủ dự án 11/10 ghi ở [`decisions/D-012.md`](../decisions/D-012.md). Không sửa `checks/` (đề xuất luật → `checks-appeal.md`). Việc nặng chạy headless bằng khoá Console, **0 agent con**.

Đã đọc: `CHARTER.md`, `decisions/D-009..D-011`, `playbook/lessons.md`, `playbook/episode.md`, `episodes/ep006/{PLAN.md, archive/PLAN-history.md, ledger.md, gates/*.md}`, `market/REPORT.md`, `market/CALIBRATION.md`, `playbook/templates/PACKAGING-BRIEF.md`, `toolkit/market/`.

## 1. Số thực Tập 6 theo phiên

**Cách đo.** Mỗi phiên: `list_events(kinds=["result"])` trang mới nhất → sự kiện `result` cuối có `modelUsage` tích luỹ của **tiến trình** (gồm agent con). Lưu ở `tongket-t6/logs/t6.jsonl`; tái tạo: `python3 toolkit/usage/token_log.py tongket-t6/logs/t6.jsonl`. **Trần = đầu vào mới (input + ghi cache) + sinh ra**; đọc cache báo riêng. Cột "giá niêm yết" = `total_cost_usd` của log. Phiên chạy bằng gói thuê bao nên đây là giá quy đổi, không phải tiền chi; chỉ khoá Console là chi thật.
**Sửa cách đo của tổng kết Tập 5:** `modelUsage` **không** cộng qua các lần khởi động lại. Phiên P3c có `process_turn_index` = 0 ở 11/10 03:53, và log chỉ còn 1,58 triệu trần cho tiến trình cuối. Vì vậy với P3c/P4 tôi lấy số của transcript cục bộ (`c5/session_tokens.py`, khử trùng theo mã tin nhắn, 2,67 + 0,14), lớn hơn số log. Các phiên khác không khởi động lại sau lượt cuối (`pti` > 0, hoặc K đọc lại toàn transcript).

### 1a. Theo phiên (triệu token)
| Phiên (mã) | Chặng | Sinh ra | Đầu vào mới | Đọc cache | **Trần** | Giá niêm yết | Agent con | Giờ máy | EL |
|---|---|---|---|---|---|---|---|---|---|
| P1 (`019BA5…`) | Việc 0 → C1 → C2 → G1 | 0,20 | 0,68 | 26,22 | **0,88** | $13,5 | 4 | 0 | 1.114 |
| P2 (`01VWvK…`) | C3 (thùng N1, nhạc hiệu) | 0,40 | 1,33 | 66,57 | **1,73** | $28,8 | 8 | 0,34 h | 1.332 |
| P3 (`01JVoR…`) | áp C3, giọng cả tập, F-12 | 0,07 | 0,32 | 15,07 | **0,39** | $6,4 | 1 | 0 | 5.253 |
| **P3b** (`01426Y…`) | merge F-12, contract, **C4 vòng 1** | **1,36** | **71,59** | 480,41 | **72,95** | **$485,5** | **10** | ≈ 2,5 h | 0 |
| P3c (`01QNrE…`) | C4 vòng 2–4 → C5–C5d → G2 | 0,48 | 2,19 | 109,11 | **2,67** | (log thiếu) | 0 | **≈ 18,0 h** (1080p 7,7 · checks 10,3) | 0 |
| P4 (trong P3c) | áp G2 → giao → merge | 0,03 | 0,11 | 7,71 | **0,14** | | 0 | 0 | 0 |
| K (`018m7H…`) | kind Tập 6 (K4.0.2) + K4.1 | 0,30 | 1,56 | 120,78 | **1,86** | $41,2 | 2 | ≈ 2,6 h (selftest, lấy mẫu trang, ASR) | 0 |
| Kiểm mù headless thuê bao (P1–P3b, 274 lượt) | | | | | **1,04** | | | | |
| Headless khoá Console (P3c: 6 lượt dựng Opus, REVIEWER G2, ≈ 30 lượt kiểm mù) | | | | | ≈ 1,4 (ước*) | **chi $25,5** | | | |
| **Cả tập** | | 2,84 | ≈ 80 | ≈ 826 | **≈ 83,4** | ≈ $606 niêm yết + **$25,5 chi** | **25** | **≈ 23,4 h** | **7.699** |

\* X/Y/Z có đủ 4 trường (trần 0,706 triệu, $13,49 → 0,052 triệu/$). Các lượt Console khác chỉ có số $, nên phần trần của chúng ước theo cùng tỉ lệ.
Agent con: ledger ghi 23. Log đếm 25 (P1 4 · P2 8 · P3 1 · P3b 10 · K 2); 2 agent của K không thuộc trần 40 của tập.

**Chủ dự án chạm ≈ 11 lượt.** Đếm từ `gates/*-answer.md`, ledger và lệnh mở phiên, không đếm từ log: mở P1 · G1 · C3 · quyền merge F-12 (mở P3b) · mở K + trả lời K4.1 · C4 chốt an toàn (rubric mới) · mở P3c với khoá Console · cho P3c chạy quá 300 nghìn ngữ cảnh · G2 + lệnh P4 · thumbnail ChatGPT. Tập 5 cũng ≈ 11.

### 1b. So Tập 5
| | Tập 5 | **Tập 6** |
|---|---|---|
| Trần cả tập | ≈ 85,4 | **≈ 83,1** (−3 %) |
| Phiên | 1 điều phối + 1 K | 6 điều phối (P1, P2, P3, P3b, P3c+P4) + 1 K |
| Khoản lớn nhất | agent con dựng W4 + W5: 71,4 (84 %) | **P3b: 72,95 (87 %)**, cũng là agent con dựng C4 |
| Mức cảnh báo | 3,0 (đo cũ) | 15 → vượt **× 5,6** |
| EL | 10.850 | 7.699 |
| Thời lượng | 7:46, không mid-roll | **8:56,6, 1 mid-roll** |
| L3 | 4·4·4·4·4·4 | ≥ 4 cả 6 dòng |

D-011 (mỗi chặng một phiên) có tác dụng ở phía điều phối: P1, P2, P3, P3c, P4 cộng lại 5,8 triệu, so với 8,7 triệu luồng chính của Tập 5. Nhưng P3b dùng lại đúng mô hình agent con dựng của Tập 5 (luật "agent dựng không chờ" ở `episode.md` §1 **không cứu được**), nên tổng gần như không đổi.

### 1c. Ba khoản tốn nhất
1. **P3b — agent con dựng C4 vòng 1: 72,95 triệu (87 %), $485 niêm yết.** Ghi cache 71,55 triệu so với sinh ra 1,36 triệu (53 : 1). P3b có 10 agent: đầu vào animatic (ngữ cảnh cuối 0,56 triệu), 3 vòng F-2, 2 lượt đạo diễn đọc nhiều ảnh (0,16 và 0,35 triệu), 3 agent FIX-R1, 1 REVIEWER. Luồng chính cũng nạp lại ≈ 0,39 triệu mỗi lần thức (lượt cuối 12:08: ghi cache 391.865). Log tích luỹ không tách được agent với luồng chính. **Nguyên nhân:** mỗi agent mang ngữ cảnh 0,1–0,56 triệu, mỗi lần chờ render (3 lượt 720p ≈ 2,5 h) rồi thức lại phải nạp lại ngữ cảnh đó; luật "trả việc ngay" không chặn được việc agent ở lại sửa nhiều vòng.
2. **Giờ máy P3c: ≈ 18 h** (1080p 7,7 h qua 6 lần + checks 10,3 h qua 4 lượt), trong tổng ≈ 23,4 h. Có hai nguyên nhân. (i) Trần 2 h của lệnh nền: lượt 1080p thứ 2 dừng ở 7.135 s; P3b chạy checks hai lần đều bị cắt khi bộ lấy mẫu trang chưa xong. (ii) Lấy mẫu trang chạy lại mọi khung, kể cả cảnh không đổi. Không tốn token, nhưng kéo dài P3c sang 2 ngày và làm ngữ cảnh phiên lên ≈ 265 nghìn.
3. **Phiên K 1,86 triệu + P2 1,73 triệu.** K: 60 lượt trong một phiên, nạp lại ngữ cảnh ≈ 0,52 triệu (`first_request_input_tokens` 521.227). P2: 8 agent (WRITER, nhạc, 3 vòng N1, đạo diễn, REVIEWER). Hai phiên này cỡ bằng nhau và **nhỏ hơn P3b 40 lần**; ghi ra để thấy sau P3b không còn khoản nào lớn.

### 1d. Hiệu quả cách P3c (headless khoá Console, 0 agent con)
| | P3b (agent con) | **P3c (headless Console)** |
|---|---|---|
| Việc | C4 vòng 1: 1 đầu vào + 3 F-2 + 3 FIX-R1 + 2 đạo diễn + REVIEWER | C4 vòng 2–4 (X, Y, Z), C5b (A, B), thumbnail (C), REVIEWER G2, ≈ 30 lượt kiểm mù, 4 checks, 6 lượt 1080p |
| Token | 72,95 triệu trần | phiên 2,67 + Console ≈ 1,4 ≈ **4,1 triệu** |
| Một lượt dựng | ≈ 7 triệu ghi cache/agent (72 ÷ 10) | X: 83 lượt, ghi cache **0,16 triệu**, đọc cache 6,8 triệu, $4,01 |
| Tiền | $485 niêm yết (thuê bao) | **$25,5 chi thật** + phiên thuê bao (P3c+P4 ≈ $29 niêm yết ở tiến trình cuối) |
| Chất lượng | — | đạt: cổng gốc 21/23, checks Tập ĐẠT (CHẶN 36/36, CHÍNH 13/13), L3 ≥ 4 mọi dòng |

- **Ghi cache mỗi lượt dựng giảm ≈ 40 lần** (7 → 0,16–0,18 triệu). Lượt headless chạy một mạch rồi thoát, không ngồi chờ render, nên không có lượt nạp lại > 0,3 triệu nào. Đây là phép kiểm `episode.md` §1 hỏi: X, Y, Z mỗi lượt cộng cả 80–100 lượt gọi mới ghi 0,16–0,18 triệu.
- **Không phải đối chứng sạch:** P3c bỏ lượt đạo diễn (chủ dự án quyết 10/10), và đó là khoản đọc ảnh lớn của P3b. Sửa ở vòng sau nhỏ hơn vòng 1. Chất lượng không giảm theo thước cuối (L3 ≥ 4, checks ĐẠT, cổng gốc 87–91 %). Ước khi bỏ phần đạo diễn (0,5 triệu theo số công cụ báo, phần log còn lớn hơn): mỗi lượt dựng vẫn rẻ hơn ≥ 20 lần.
- **Giá:** một lượt dựng Opus ≈ $3,3–4,9; cả P3c tốn $25,5 trên trần $170.
