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
| **Cả tập** | | 2,84 | ≈ 80 | ≈ 826 | **≈ 83,1** | ≈ $605 niêm yết + **$25,5 chi** | **25** | **≈ 23,4 h** | **7.699** |

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

## 2. Bài học → luật

Chi tiết từng mục (số đo, nguyên nhân gốc, luật) ở `playbook/lessons.md` T6-3 … T6-11. **ÁP** = đã sửa trong phiên này (không phải gu, không đụng luật khoá). **CHỜ** = cần quyền chủ dự án (gói §5 câu 1) hoặc phiên K.

| Mục | Số đo Tập 6 | Trạng thái | Sửa ở đâu |
|---|---|---|---|
| (a) không mở phiên mới khi tệp lớn đang ở container | P3 → P3b → P3c: mỗi PLAN chép "dựng lại ≈ 2,8 h nếu container mới"; P4 chạy trong P3c: 0,14 triệu | **CHỜ** (sửa D-011) | lessons T6-3 |
| (b) trần 2 h lệnh nền | checks 10,3 h · 1080p 7,7 h · 3 lần bị cắt | **ÁP** (tách chạy tiếp, cache theo cảnh, `K_JOBS=4`) + **CHỜ K** A29; biến môi trường **chưa xác minh** | `episode.md` §11b, `toolkit/checks_split.sh`, `checks-appeal.md` A29 |
| (c) hằng tốc độ | đọc 2,66 (hằng 2,75) · thời lượng 2,40 (hằng 2,52, −4,8 %) | **ÁP**: hằng mới 2,66/2,40; chạy lại kịch bản Tập 6 → ước 8:56 = thật 8:56,6 | `templates/check_script.py`, `toolkit/usage/measure_pace.py` |
| (d) nhịp hình | spine: 7 quãng tĩnh > 8 s (dài nhất 11,3 s; Tập 5: 6, dài nhất 16,4 s) · freezedetect 206 s / 51 đoạn · R07 70,3 % · "3%" trễ 1,26 s | **CHỜ** (gu hình D-010 + gen §4): F-14 làm ở nhà máy **trước** tập dài đầu tiên | `toolkit/factory/BACKLOG.md` F-14 |
| (e) B01/B15 hết 3 vòng | 0,5 · 0,5 qua 4 lượt; "none since" đè mép dải cảnh báo | **ÁP**: vòng 3 phải đổi loại hình hoặc hạ ý cần đọc | `episode.md` §1 |
| (f) phiếu L3 kèm mức gợi ý | G2 Tập 6 "≥ 4" không số | **CHỜ** (nguy cơ neo điểm) | `playbook/templates/L3.md` (nháp) |
| (g) khoá Console = chuẩn | $25,5 · ghi cache/lượt dựng ÷ 40 (§1d) | **CHỜ** (chi tiêu) | `toolkit/api.sh` (dời từ ep006, công cụ có sẵn) |
| (h) móc Shorts đo vùng an toàn khi viết | SH1/SH3 186 / 98 hộp ngoài vùng | **ÁP** (luật viết) + **CHỜ K** A30 | `episode.md` §5, `checks-appeal.md` A30 |
| (i) gói ChatGPT lệch video | "baskets" ≠ crates · ảnh chụp ≠ thế giới 3D · mỗi thumbnail một màu · tiêu đề ≠ T1 | **ÁP** qua mục 4 | `playbook/packaging.md` §7, `episode.md` §5c, `toolkit/package/` |

**Đo (d) trên Tập 6** (`python3 toolkit/indicators/spine_pace.py episodes/ep006/world/c4/*/spine.json --labels`): các quãng tĩnh có lời là 0:29–0:40 (11,2 s), 1:35–1:44, 1:47–1:56, 2:43–2:51, **3:41–3:53 (11,3 s)**, 4:40–4:50, 8:07–8:16. Thước này chưa hiệu chuẩn (A23: đối chứng dương 2/4), nên chỉ dùng làm chỉ báo. Đích của F-14 đo trên Tập 6 dựng lại, đối chứng là bản giao.

## 3. Độ dài mới: format `deep`

Theo D-012 mục 1: dải vượt trội có trung vị ~15–16 phút (`market/REPORT.md` §4; tứ phân vị ~12–19).

| | Đề xuất (chờ duyệt con số, gói §5 câu 2) |
|---|---|
| Tên · thời lượng | **`deep` 14–17 phút**. Ước G1 ≥ 14:42 (sàn + 5 %, như `101`), tối đa cứng 17:00 |
| Cấu trúc | móc → khái niệm + **hai nhân vật** cùng xuất phát → phát lại nhiều cửa sổ → nhân vật 2 / ca đối chứng → **ACT 4 câu hỏi khán giả** → giới hạn. Khuôn tỉ lệ: 5 · 15 · 25 · 20 · 25 · 10 % |
| Mid-roll | 2–3 điểm (3 khi ≥ 15:30), mỗi điểm ở ranh giới hồi có lặng ≥ 1 s, ≥ 2 phút đầu/cuối, cách nhau ≥ 3 phút |
| Không độn | Chỉ chọn khi đủ cả ba: ≥ 3 cửa sổ lịch sử cho kết quả khác nhau · hai nhân vật · ≥ 3 câu hỏi khán giả, mỗi câu một nhịp. Mỗi phút thêm phải mang claim mới hoặc câu hỏi được trả lời |
| Nhà máy trước | Tập `deep` đầu tiên mở C3 chỉ khi F-14 đạt đích trên Tập 6 dựng lại (§2 d) |
| Trần (cảnh báo) | 20 triệu token · Console $60 · **EL ≈ 13.000–15.000 ký tự/tập** · giờ máy ≈ 22 h (35–40 h nếu chưa có A29) |

**Đã áp** (không phải gu; con số `deep` chờ duyệt nên ghi "chờ" ngay trong văn bản):
- `playbook/episode.md` §9: dòng `deep`, điều kiện không độn, mid-roll, "nhà máy trước".
- `playbook/episode.md` §8: mức cảnh báo theo format.
- `playbook/templates/check_script.py`: `LEN_LIMITS['deep']` (882, 1020); khuôn `deep`; ACT 4; mid-roll 2–3 và khoảng cách ≥ 180 s. Thử trên bản sao kịch bản Tập 6 khai `deep` → TRƯỢT độ dài (536 < 882 s, thiếu ≈ 830 từ) và TRƯỢT mid-roll (1 < 2). Kịch bản Tập 6 với `101` cho cùng kết quả như trước, trừ phần do hằng mới.
- `checks-appeal.md` A31: luật độ dài theo format cho lô K (F07 + mid-roll), chạy trước C4 Tập 7.

**ElevenLabs:** 2.120–2.450 từ nói × ≈ 5,9 ký tự/từ + ≈ 10 % sinh lại ≈ **13.000–15.000 ký tự/tập**, gấp ≈ 2 lần Tập 6 (7.699). Bốn tập/tháng ≈ 60.000 ký tự. **Chủ dự án cần kiểm hạn mức gói ElevenLabs.** Không đủ thì hoặc dùng `lab`, hoặc nâng gói (đó là chi tiêu mới).

**CHARTER §1 chưa sửa:** hiện ghi "hai định dạng". Phiên P1 Tập 7 sửa sau khi chủ dự án duyệt câu 2 (D-012 "Thay").

## 4. Đóng gói: khớp nội dung + xu hướng + đề xuất (D-012 mục 3)

Luật nằm ở `playbook/packaging.md` §7. Ngoài ra đã sửa `episode.md` §1b.5, §3.12, §5, §5c (thành đường dự phòng), §10.4–5, §11, cùng `templates/G1.md` mục 3 và `templates/PACKAGING-BRIEF.md`. Công cụ mới: `toolkit/market/anchors.py`, `toolkit/package/{text,thumbs,rescore}.py`. Chi trong phiên: YouTube API 1.212/10.000 đơn vị · Claude (Console) ≈ $0,13 · OpenAI ảnh ≈ $0,25.

### 4a. Video neo cho G1 (`anchors.py anchors`; số thô ở `~/market-cache/`, repo chỉ nhận nhãn)
Chọn: cùng câu hỏi khán giả (Haiku xét), đăng 30–90 ngày, tốc độ lượt xem/ngày cao nhất đề tài. Không dùng `relatedToVideoId`.
| Đề tài | Neo (tốc độ tự tính so trung vị đề tài) | Khác biệt của Crux (máy viết, xem lại ở G1) |
|---|---|---|
| #12 (Tập 6, hồi tố) | Diamond NestEgg [qFuVEfm68ps](https://youtu.be/qFuVEfm68ps) · cao · giả định cố định | chiếu khoản COLA theo giả định; không phát lại lạm phát 20 năm thật |
| **#13 (Tập 7)** | Home Loan Education [9bTPEGduDww](https://youtu.be/9bTPEGduDww) · Real Estate The Ramsey Way [8Z5KjkQk5gk](https://youtu.be/8Z5KjkQk5gk) · James Johnson [BLgV27v3xlI](https://youtu.be/BLgV27v3xlI) — cả ba cao | giả định cố định / ý kiến; không đặt khoản vay 15 năm thật cạnh 30 năm trả trong 15; không có lịch sử lãi thật |
| **#20 (Tập 8)** | Logical Money [nkT_K8l1rEw](https://youtu.be/nkT_K8l1rEw) · HinExp [VSnf3GaGgMU](https://youtu.be/VSnf3GaGgMU) · Amuk Tamuk [8dBnUXzMaXQ](https://youtu.be/8dBnUXzMaXQ) — cả ba cao | hai người giả định tăng trưởng cố định; không có giá thuê/giá nhà lịch sử thật |
Đã ghi lại hai lỗi của cách chọn neo:
- Câu hỏi đưa vào mà có cả phương pháp ("…over real history") → Haiku loại mọi video, ra 0 neo. Câu hỏi phải là câu của khán giả.
- `regionCode=US` vẫn trả video Ấn Độ/Anh (₹, lakh, SIP) → đã thêm bộ lọc.

### 4b. Chữ do Claude viết (`toolkit/package/text.py`, Tập 6; $0,07, một lượt Opus headless)
| | |
|---|---|
| 3 tiêu đề | "Annuity inflation protection: did a 2% raise keep up?" · "Annuity 2% raise vs inflation: the 20-year scorecard" · "Retirement income annuity: a 2% raise kept up 17 of 715" |
| 2 dòng đầu mô tả | "Annuity inflation protection, replayed: a check rising 2% a year vs US prices. / Every 20-year stretch from 1947 to Aug 2006, 715 in all." |
| Chương | 6 chương giữ mốc timeline, tên có từ khoá ("Ruth's 2% annuity raise question" …) |
| Tag | 5 |
| Kiểm | **ĐẠT**: S21 PASS · claim-risk 0 · số có claim · chương khớp hồi · không có từ cấm (basket…) |
Tệp: `tongket-t6/package-ep006/{text.json, description.md}`. Có một tag lấy từ hồ sơ ("annuity cost of living rider") không khớp nội dung tập; REVIEWER G2 phải đọc cả tag.

### 4c. Thumbnail lai: OpenAI image API **chạy được** qua proxy
`images/edits` gpt-image-1, chất lượng medium, ≈ $0,063 và ≈ 23 s mỗi ảnh. Lần thử đầu với PNG 1,5 MB bị proxy trả **502**; gửi JPEG thì qua. Khoá do proxy gắn; không có biến `EMBEDDINGS_API_KEY` trong phiên.
| Ảnh (`tongket-t6/thumbs/`) | Khung | Chữ (bộ nhận diện) | Giữ vật thể | Lệch |
|---|---|---|---|---|
| api-1 | đoạn a 4,0 s (Ruth, séc, 10 thùng) | 20 YEARS / LATER | thùng, séc, nhân vật tím, low-poly ✓ | thùng thành 2 tầng |
| api-2 | đoạn e 140 s (Edna, Ruth, Carl, 3 hàng thùng) | 2% RAISE / ENOUGH? | 3 nhân vật đúng màu, thùng tối bên phải ✓ | lần 1: nhân vật phóng to, thùng mất → lần 2 (prompt "giữ khoảng cách máy") đạt. Chữ đè hàng thùng bên trái → luật: khung chừa góc dưới trái |
| api-3 | đoạn b 70,2 s (Ruth, séc lớn, thùng cuối tối) | BIGGER CHECK / BUYS LESS? | thùng, thùng cuối tối, séc ✓ | số thùng không còn đúng 10 |
Lớp chữ do máy vẽ (logo "M.", Inter Bold, vị trí cố định, màu trụ nghỉ hưu `#3FBF7F`), nên chữ đúng từng ký tự. **Model ảnh giữ được loại vật thể nhưng không giữ số lượng.** Bản cuối vì thế phải được người xem lại ở G2.

### 4d. P4: quét 7 ngày + chấm lại (`anchors.py trend`, `rescore.py`; Sonnet, ≈ $0,02)
- Mẫu đang lên của #12 trong 7 ngày (sau lọc): tiêu đề kiểu "thu nhập trọn đời / ngưỡng có đủ không"; thumbnail có người dẫn chỉ vào máy (Crux không dùng), biểu đồ, chia đôi; từ khoá "retirement income strategies", "lifetime retirement paycheck", "TIPS".
- Gợi ý tìm kiếm YouTube (`suggestqueries.google.com`): **proxy chặn (CONNECT 403)** → bỏ; ghi ở `packaging.md` §7.5.
- Giờ đăng gợi ý: thứ Hai 12–16 UTC (tín hiệu yếu).

### 4e. Sau đăng
Thành luật ở `episode.md` §10 mục 4–5: đổi/giữ ở mốc 48–72 giờ theo CTR + nguồn "video đề xuất"; hằng tháng gợi ý đổi tiêu đề video cũ khi đề tài lên lại. Chưa dựng công cụ; prompt Phiên Analytics để sau.

### 4f. Phép thử trên Tập 6
| | Thumbnail: trend · khớp · đọc ở 168×94 (Sonnet 1–5) | Ghi chú |
|---|---|---|
| **API lai** api-1 · api-2 · api-3 | 5·5·5 · 5·5·5 · 5·5·4 | đúng vật thể (crates), thế giới 3D, một màu kênh; số thùng lệch (api-1, api-3) |
| Nhà máy thumb-1 · 2 · 3 (G2) | 5·5·5 · 4·5·5 · 3·4·5 | thumb-3 (đối chứng 2D) thấp nhất ở trend |
| **ChatGPT của chủ dự án** ("20 YEARS LATER", "2% RAISE ENOUGH?", "BIGGER CHECK BUYS LESS?") | **chưa chấm**: ảnh không có trong repo/phiên | theo mô tả của chủ dự án thì trượt luật vật thể: "baskets" ≠ crates, ảnh chụp ≠ thế giới 3D, 3 màu khác nhau → theo thang thì "khớp" ≤ 2. Chạy lại khi có ảnh: `python3 toolkit/package/rescore.py … --thumb <ảnh ChatGPT>` |

| Tiêu đề | trend · khớp |
|---|---|
| Claude 1 "Annuity inflation protection: did a 2% raise keep up?" | 4 · 4 |
| Claude 2 "Annuity 2% raise vs inflation: the 20-year scorecard" | 4 · 5 |
| Claude 3 "Retirement income annuity: a 2% raise kept up 17 of 715" | 3 · 5 |
| T1 (G1) "Does a 2% Annuity Raise Really Keep Up With Prices?" | 3 · 4 |
| Tiêu đề ChatGPT | chưa chấm (chủ dự án chưa gửi nguyên văn) |

**Đọc kết quả:** Sonnet chấm rộng tay (gần như mọi ảnh 4–5) và không bắt được lỗi số thùng. Vì vậy nó chỉ là bộ lọc thô: nó loại được vật thể sai và ảnh chụp, nhưng không chọn được giữa các phương án tốt. Chênh lệch thật nằm ở luật cứng: đường API lai giữ đúng vật thể, thế giới và màu kênh theo cách làm; đường ChatGPT thì không (T6-11). Thước đo thật vẫn là Test & Compare và CTR sau đăng (§10.4).

## 5. Gói cho chủ dự án (≤ 3 câu, mỗi câu có khuyến nghị)

**Câu 1: duyệt các luật ở §2 cần quyền chủ dự án?**
- (a) **Sửa D-011.** Khi chặng sau cần tệp lớn ngoài git đang nằm ở container, chạy tiếp trong phiên đó sau `/compact` thay vì mở phiên mới. Vẫn đóng chặng bằng PLAN ≤ 1 trang + prompt, để mở phiên mới được nếu container mất.
- (d) **F-14 nhịp hình**, làm ở nhà máy trước tập dài đầu tiên: chuyển động nền liên tục **có nghĩa** khi máy đứng; mỗi ≤ 8 s một thay đổi mang nghĩa; nhãn neo vào từ. Đích đo trên Tập 6 dựng lại: 7 → 0 quãng tĩnh, freezedetect < 60 s, R07 ≥ 90 %, "3%" ≤ 0,2 s, cổng gốc không tụt.
- (f) **Phiếu L3** kèm số máy và mức gợi ý, đặt **sau** ô điểm của chủ dự án.
- (g) **Khoá Console là cách chuẩn** cho dựng, đọc và soát. Trần chi/tập: `101` $35 · `lab` $45 · `deep` $60.
- **Khuyến nghị: duyệt cả bốn.** (d) và (f) chạy thử 3 tập rồi hiệu chuẩn lại.

**Câu 2: format `deep` và format Tập 7–8?**
- `deep` 14–17 phút, ước G1 ≥ 14:42, 2–3 mid-roll (3 khi ≥ 15:30, các điểm cách nhau ≥ 3 phút).
- Ba điều kiện không độn: ≥ 3 cửa sổ lịch sử cho kết quả khác nhau · hai nhân vật · ≥ 3 câu hỏi khán giả.
- Trần cảnh báo: 20 triệu token, $60, ≈ 22 h máy.
- **ElevenLabs ≈ 13.000–15.000 ký tự/tập** (≈ 60.000/tháng nếu 4 tập). **Anh kiểm hạn mức gói ElevenLabs.**
- **Khuyến nghị:**
  - Tập 7 (#13) = `deep` nếu F-14 đạt đích trước C3. #13 có đủ ba điều kiện: nhiều năm bắt đầu theo lãi thật — lãi 15 năm có từ 1991 theo Freddie Mac PMMS, kiểm ở Việc 0 —, hai người cùng một căn nhà khác kỳ hạn, câu hỏi "trả sớm hay đầu tư" của khán giả. Nếu F-14 không đạt, hoặc gói EL không đủ → `lab` 11 phút.
  - Tập 8 (#20) xét cùng cách ở G1 lô.

**Câu 3: đường thumbnail?** Phép thử §4f trên Tập 6:
- **API lai** (khung 3D thật → OpenAI `images/edits` → lớp chữ máy) giữ đúng vật thể (thùng, không phải giỏ), giữ thế giới 3D và một màu kênh, ≈ $0,25/tập. Nó lệch số thùng ở 2/3 ảnh, nên người phải xem ở G2.
- **ChatGPT thủ công** lệch cả ba điểm (giỏ, ảnh chụp, 3 màu).
- Bộ nhận diện "M." (Inter Bold, chữ dưới trái, màu theo trụ; `packaging.md` §7.4) là gu, cần anh duyệt.
- **Khuyến nghị: API lai là đường chính, ChatGPT dự phòng; duyệt bộ nhận diện như ảnh `tongket-t6/thumbs/api-*.png`.** Vẫn render đối chứng 2D cho Test & Compare đến hết Tập 7.

**Trả lời gọn:** `1 a·d·f·g: duyệt/sửa … · 2 deep: duyệt/sửa …; Tập 7: deep/lab; EL: đủ/không · 3 API lai/ChatGPT; nhận diện: duyệt/sửa …`

## 6. Prompt P1 Tập 7 (G1 lô Tập 7–8) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 7, đề tài #13 (15-year mortgage vs a 30-year paid off in 15), phiên P1 — G1 LÔ Tập 7–8 (D-011 Q1, D-012). Nhánh ep007 từ main (sau khi tongket-t6 đã merge). Mở bằng `bash toolkit/verify.sh ep007`.
Đọc trước: CHARTER.md, decisions/D-012.md, tongket-t6/REPORT.md §2–§5, playbook/episode.md (§1b, §3.12, §5, §8, §9), playbook/packaging.md §7, playbook/prompts/P1.md, market/topics/q13-15-vs-30-mortgage.md, tongket-t6/anchors/q13-15-vs-30-mortgage.json.
Việc đầu tiên: chép câu trả lời tổng kết Tập 6 dưới đây vào tongket-t6/ANSWER.md, commit; áp phần được duyệt (D-011 sửa, F-14, phiếu L3, khoá Console, format deep → CHARTER §1 + episode.md §9 bỏ chữ "chờ", bộ nhận diện kênh). Câu 1 (d) được duyệt → F-14 trên nhánh factory-f14 TRƯỚC C3 Tập 7 (đo trên Tập 6 dựng lại, đối chứng bản giao f96da0ea).
Tập 7: P1 Việc 0 → C1 → C2 → G1 theo P1.md. Format theo câu 2. Video neo + ý tưởng tiêu đề/thumbnail chốt ở G1 (packaging.md §7.1). Việc nặng headless khoá Console (toolkit/api.sh), 0 agent con trừ khi cần công cụ phiên.
Tập 8 (#20 thuê vs mua, phát lại lịch sử thật; dự phòng #6): song song, chạy máy đề tài làm hồ sơ #20 (topic-dossier.md §4: quyền dữ liệu giá thuê/giá nhà); G1 lô có đề tài + logline + format + neo (tongket-t6/anchors/s1-rent-vs-buy-history.json) cho Tập 8. Hồ sơ #20 không qua §4 → #6.
Dừng ở G1 lô (đóng phiên theo D-011 / bản sửa nếu duyệt).
Câu trả lời tổng kết Tập 6:
<<DÁN CÂU TRẢ LỜI TỔNG KẾT TẬP 6 Ở ĐÂY>>
```
