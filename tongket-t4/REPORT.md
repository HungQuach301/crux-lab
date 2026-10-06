# Tổng kết Tập 4 — chi phí sản xuất và cách hạ (Phiên T4, 06/10/2026)

Nhánh `tongket-t4` (từ `main` d706fda, đã có merge ep004). Không sửa `checks/`. Nguồn số: `episodes/ep00{2,3,4}/ledger.md`, `playbook/lessons.md` E13/F8/G2, `moc-b/TOKENS.md`, `gates/*`. Số đo mới của phiên: `tongket-t4/blind-measure/measurements.json`.

## 1. Bảng chi phí Tập 2–4

| | Tập 2 | Tập 3 | Tập 4 |
|---|---|---|---|
| Token cả tập | không đo (≈ 300 lượt × ~40 nghìn ≈ 12 triệu, **ước**) | không đo (≈ 6 triệu, **ước** 141 × 44 nghìn) | **≈ 6,3 triệu** (agent con 5,36 + điều phối ≈ 0,95), chưa tính phiên K |
| Số lượt agent | ≈ 300 (≈ 287 người đọc + chấm) | 141 | 102 (85 lượt kiểm mù) |
| Token trung bình / lượt | — | — | 53,6 nghìn (kiểm mù 36,6 · WRITER 188 · REVIEWER 109 · dựng 188) |
| Ký tự ElevenLabs | 9.436 | 5.551 | 11.702 (8.148 sinh lại vì mất cache khi đổi container) |
| Lượt chủ dự án tham gia | 11 cổng + giao hàng | 3 cổng + xác nhận tải | 5 (G1 · C3 · C4 · G2 · nới trần) + G3 |

**Tập 4 theo loại việc** (từ ledger từng dòng; cộng = 6,31 triệu, khớp KPI 6,3):

| Loại việc | Lượt | Token | % | Ghi chú |
|---|---|---|---|---|
| **Kiểm mù** (người đọc + người chấm) | 85 | **3,11 triệu** | **49 %** | cổng gốc C4 2 vòng 0,98 · C3 2 vòng 0,52 · C2 2 vòng 0,50 · móc (hiệu chuẩn + vòng tròn) 0,54 · C4 gộp đối chứng 0,28 · C1 0,23 · G2 tóm tắt AI + thumbnail 0,08 |
| **Dựng** (agent nhà máy C3/C4/C5/G2/C6) | 6 | **1,13 triệu** | **18 %** | mỗi lượt 105–288 nghìn |
| **Điều phối** (ngữ cảnh 3 phiên chính) | — | **≈ 0,95 triệu** | **15 %** | P1 0,4 · P2 0,2 · cuối 0,35 |
| WRITER | 3 | 0,56 triệu | 9 % | 1 lượt + 2 lần gọi lại (lessons G2) |
| REVIEWER | 4 | 0,44 triệu | 7 % | D-008: không cắt |
| Checks / kiểm độc lập / selftest | 2 | 0,11 triệu | 2 % | checks chạy bằng lệnh |

**Ba khoản tốn nhất:** (1) kiểm mù 3,11 triệu; (2) dựng 1,13 triệu; (3) điều phối 0,95 triệu.

## 2. Giảm chi phí kiểm mù

### 2a. Đo thật một mẫu (C2 vòng 2 Tập 4, lời 6,2 KB, 6 câu hỏi cố định)

| Cách | Token / lượt | Ghi chú |
|---|---|---|
| Agent con hiện tại (`Explore`, đọc file) | **32–47 nghìn** (ledger: C1 31,9 · C2 34,7 · C4 v2 ≈ 47) | lượt đo lại trong phiên: harness không trả số |
| Agent con, lời dán vào đầu bài, dặn không dùng công cụ | **49,3 nghìn** | vẫn gọi 1 công cụ; không rẻ hơn: phần cố định là chỉ dẫn hệ thống + định nghĩa công cụ của agent con |
| **Headless `claude -p --tools ""`** (Sonnet) | **8,7–10,1 nghìn** (Sonnet 6,0–7,4 + Haiku phụ 2,7) | 3 lượt; câu trả lời cùng chất lượng; chỉ ra đúng chỗ mất chú ý S18 như cổng thật (5/6) |
| Headless có ảnh (`--tools Read`, dải B08.png) | **11,2 nghìn** | trả lời đúng nghĩa + "no action" |

Chạy bằng tài khoản Claude Code sẵn có của phiên: không có API trả phí mới, không có khoá mới. Lệnh: `toolkit/blind/headless.sh` (chạy từ thư mục trống nên không nạp CLAUDE.md hay skill của repo; lời chỉ nằm trong đầu bài nên vẫn mù). **Giảm khoảng 4 lần mỗi lượt.** Tập 4 chạy cách này thì 85 lượt ≈ 0,85 triệu thay vì 3,11 triệu.
Giới hạn: mới đo 4 lượt trên 1 tập. Tập 5 cho chạy song song headless và `Explore` trên **một** cổng (C2, 3 + 3 người đọc) rồi mới chuyển hẳn. Ngưỡng giữ: cùng kết luận đạt/trượt, cùng cảnh mất chú ý nhiều nhất.

### 2b. Vòng kiểm mù: giữ hay bỏ (bằng chứng: kết quả có đổi quyết định của chủ dự án không)

| Vòng | Tập 2 | Tập 3 | Tập 4 | Đổi quyết định | Đề xuất |
|---|---|---|---|---|---|
| **Logline C1** | B bị hiểu "thả nổi thường rẻ hơn" 3/5 → chọn A | A 5/5, B 4/5 → chọn A (24 người đọc, mọi người đọc cùng logline cho điểm giống hệt) | vai đích 0/5 → chủ dự án **bỏ qua**, không vòng 2 | 1/3 | **GIỮ, rút gọn:** 3 người đọc mỗi logline (2 T + 1 G), headless, bỏ đối chứng W và so cặp tiêu đề. Dừng sớm khi đã 2 sai |
| **Kịch bản C2** | 3 vòng; đoạn phương pháp mất chú ý 5/6 → chủ dự án ra lệnh sửa | 1 vòng đạt | v1 khuyên 1/6 → v2; S18 5/6 → dự phòng V7 | 2/3 (sửa kịch bản) | **GIỮ**, 6 người đọc headless + 1 người chấm headless; ≤ 2 vòng. Thêm điều kiện móc (§4) |
| **Cổng gốc C4** (và C3 ký hiệu mới) | KEY-2/4/7 trượt nhiều vòng → bỏ ký hiệu (hũ, hai cột) | C3 2 vòng, C4 1 | 3/7 → chủ dự án chọn (b) sửa nhãn → 6/7 | 3/3 | **GIỮ** (đổi hình thật), headless có ảnh; chỉ nhịp loại 1; 2 người đọc, người thứ 3 chỉ khi chia (Tập 4 vòng 2 đã làm vậy: 3/4 nhịp xong ở 2 người đọc) |
| Đối chứng gộp C4 (âm/dương, S18, A9) | — | hiệu chuẩn khuyên 1 lần | 0,28 triệu; S18 2/4 → giữ nguyên; A9 0/12 | 0/1 | **BỎ** khỏi tập thường; chỉ chạy khi rubric mới (việc của lô K, A9) |
| **Tóm tắt AI G2** | 1 lần (C6) | hook 2/5 → phát hành nguyên trạng | hook 2/5 → phát hành | 0/3 | **BỎ ở G2.** Thay bằng điều kiện móc đo trên kịch bản + table read ở C2 (§4), lúc còn sửa được |
| **So cặp thumbnail** | — | T1 4/4 = chủ dự án chọn T1 | T1 3/4 = chủ dự án chọn T1 | 0/2 | **BỎ.** Test & Compare của YouTube là số đo thật; chủ dự án chọn thứ tự T&C |
| Hiệu chuẩn so cặp móc + vòng tròn 3 móc | — | (Mốc B 18 người đọc, 0,89 triệu) | 0,54 triệu; H2 = lựa chọn cuối; H1/H2 chưa phân biệt | 0/1 | **BỎ hiệu chuẩn** (đã xong). Vòng tròn → **REVIEWER chấm 3 phương án theo story §1 + điều kiện móc §4**; so cặp chỉ khi REVIEWER không tách được (3 lượt headless) |

### 2c. Dừng sớm và số người đọc
- **Người đọc cùng model tương quan rất cao:** C1 Tập 3 có 24 người đọc, cùng một logline thì 5 vai cho **điểm giống hệt** (6/6 hàng trùng). C2 v2 Tập 4: 6/6 cùng kết luận, 5/6 cùng cảnh mất chú ý. Sáu người đọc chỉ bằng khoảng 2–3 ý kiến độc lập.
- **Dừng sớm khi đã chắc trượt** (không đổi được kết luận): C1 dừng ở 2 sai; C2 dừng ở người đọc đầu tiên có khuyên_tính (A9) hoặc 2 sai; cổng gốc mỗi nhịp dừng khi 2 người đọc đầu cùng kết luận.
- **Không dừng sớm khi đạt** ở C2: lỗi hiếm (khuyên 1/6 ở C2 v1 Tập 4) chỉ một người đọc bắt được. Headless rẻ nên 6 lượt chỉ khoảng 60 nghìn token.
- **Người chấm:** giữ một người chấm độc lập mỗi vòng (headless khoảng 15 nghìn, thay cho 35–70 nghìn).
- **Ước Tập 5:** kiểm mù khoảng 0,5–0,6 triệu, thay cho 3,11 triệu.

## 3. ElevenLabs: take giọng vào git
- Nhà máy (`toolkit/factory/voice.py`, `build.py`): take `<băm16>.mp3` + `<băm16>.json` (băm SHA-256 của lời + voice + model + seed + settings, văn bản, alignment) nằm ở **`episodes/epNNN/voice-takes/` (commit)**. wav suy ra từ mp3 nên vẫn ở `work/`. Đổi container không phải sinh lại giọng.
- Thử: take có sẵn thì không gọi API (khoá `requests`), wav vào `work/`. Selftest móc ký hiệu 5/5.
- **Dung lượng:** mp3 128 kbps ≈ **16 KB/s lời** (S02 Tập 4: 21,6 s = 346 KB). Một tập 8 phút ≈ 7,7 MB, kể cả take thử khoảng 8–10 MB. Repo hiện 822 MB `.git`, 1.064 mp3 ≈ 110 MB. Tới khoảng 30 tập thì xét Git LFS.
- Tập 4 có cache sẽ tiết kiệm ≈ 8.148 ký tự (70 % ký tự của tập).

## 4. Móc mở đầu → điều kiện ở C2
**Bằng chứng luật `story.md` §1 chưa đủ.** Đo trên timeline nhà máy Tập 4 (`out/factory/timeline.json`):

| Mốc | Tập 4 | Luật |
|---|---|---|
| Câu móc S01.1 ($558,100) kết thúc | **8,1 s** | ≤ 5 s → **trượt, không ai đo** |
| Lời hứa S01.3 kết thúc | 24,7 s | ≤ 30 s → đạt |
| Ràng buộc liên tục S02.1–S02.4 | **25,1–48,6 s (23,5 s)** | "sau móc" → đạt theo chữ |
| Định nghĩa S03 | 49,4–76,0 s (26,6 s) | không có luật |
| Câu hỏi của người xem S04.5 "Is it? Has their gain passed the cap?" | **1:34** | không có luật |

Tập 3: câu hỏi ở 0:37, lời hứa ở 1:04. Cả hai tập: tóm tắt AI chấm hook **2/5**; Tập 4 AI ghi "bỏ được 0:08–1:08". Luật §1 viết bằng chữ, không có số đo trên âm thanh thật. WRITER làm đúng chữ (ràng buộc đặt sau lời hứa) mà vẫn tạo ra 70 s không có gì để mất.

**Đề xuất: điều kiện TỰ ĐỘNG ở C2, đo trên kịch bản + table read trước G1** (`episode.md` §3.9). Mỗi câu trong 60 s đầu được gắn vai `hook / promise / question / constraint / define`. Mốc thời gian lấy từ timeline nhà máy hoặc ASR table read.
- M1: câu móc (được–mất hoặc câu hỏi) **kết thúc ≤ 5,0 s**.
- M2: lời hứa **kết thúc ≤ 30 s**.
- M3: câu hỏi trung tâm của người xem **≤ 30 s** (được trùng câu móc).
- M4: trong 0:00–1:00 **không khối ràng buộc/định nghĩa nào liền > 10 s**. Phần thừa chuyển lên nhãn hình, thẻ V7 hoặc mô tả.
- M5: nhân vật hoặc cái được–mất quay lại trước **0:45**.

Trượt → WRITER mới, đầu bài ngắn, sửa trước G1 (≤ 2 vòng); vẫn trượt → nêu ở G1. Đây là luật của tập, không phải `checks/`. A2 ở `checks-appeal.md` vẫn là đường cho luật kênh.

## 5. Hàng chờ lô K
Đã ghi vào `checks-appeal.md`: A10 (F11/F12 viết lại cho nhà máy), A11 (nhà máy xuất `page.json`), A12 (README K3.8 bỏ chữ "chờ duyệt"), cùng thứ tự xử lý A10 → A11 → A12 → A5 → A7 → A9.

## 6. Tài liệu
`lessons.md` mục H · `episode.md` §2, §3.9, §5, §8 · `prompts/RUN.md` · `CHARTER.md` §4 (một dòng) · `toolkit/visual-library` thêm V9 (N1), V10 (N2).

## 7. Trần Tập 5: ≤ 3 triệu token cả tập

| Loại việc | Trần | Cách |
|---|---|---|
| Kiểm mù | 0,6 triệu | headless; C1 3×2 + C2 ≤ 2×7 + cổng gốc ≤ 2 vòng × ≤ 20 lượt; không tóm tắt AI, không thumbnail, không hiệu chuẩn |
| Dựng (nhà máy) | 0,75 triệu | ≤ 4 lượt agent; take giọng commit nên dựng lại không sinh giọng |
| WRITER | 0,4 triệu | 1 + ≤ 2 agent mới đầu bài ngắn |
| REVIEWER | 0,45 triệu | ≤ 4 (không cắt, D-008) |
| Checks, kiểm độc lập | 0,15 triệu | lệnh + 1 agent kiểm mô hình |
| Điều phối | 0,5 triệu | ≤ 2 phiên; đọc tóm tắt, không đọc file nặng |
| Dự phòng | 0,15 triệu | |
| **Cộng** | **3,0 triệu** | ≤ 40 agent con + ≤ 120 lượt headless. Vượt > 25 % → dừng hỏi |

Ký tự ElevenLabs: ≤ 6.000 (cache sống). Chủ dự án: G1, G2, G3.

## 8. Token của phiên T4 (trần 0,6 triệu, ≤ 6 agent)
| Mục | Token |
|---|---|
| Ngữ cảnh phiên chính (bộ đếm phiên) | ≈ 0,19 triệu |
| Agent con: `Explore` (đo 2a, cách 1) | ≈ 35 nghìn (harness không trả số; theo ledger cùng loại) |
| Agent con: general-purpose (đo 2a, cách 2) | 49.260 |
| Headless: 5 lượt (4 chữ, 1 ảnh), có 1 lượt chạy song song bị hỏng | ≈ 50 nghìn |
| **Cộng** | **≈ 0,32 triệu ≈ 54 % trần**; 2 agent con |
