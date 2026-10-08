# Tổng kết Tập 5 — số thực, câu hỏi mở, bài học cine-lab, lô K, Tập 6 (Phiên T5, 08/10/2026)

Nhánh `tongket-t5` (từ `main` 6e0ae01, đã có merge ep005). Không sửa `checks/`. Không áp đề xuất nào: mọi mục dưới đây chờ chủ dự án duyệt (CHARTER §7, phiên tổng kết "không tự áp dụng khi chưa duyệt").

Đã đọc: `CHARTER.md` v4, `decisions/D-009.md`, `D-010.md`, `playbook/lessons.md` (V, T5), `episodes/ep005/{PLAN.md, ledger.md, gates/G2.md, gates/G2-answer.md}`. Từ `HungQuach301/cine-lab` (chỉ đọc): `reports/m3/BAI-HOC-LL.md`, `LO-3-5-TONG-KET.md`, `LO-6-8-G1.md`, `TAP6-G2-V2.md`, `playbook/PLAN-TAP-MAU.md`.

<!-- MỤC 1 -->

## 2. Các câu hỏi mở

### 2a. Kiểm mù: headless hay `Explore`? → **headless** (giữ như Tập 5 đã làm)
Dữ liệu duy nhất có đối chứng là C2 vòng 1 Tập 5: cùng gói lời (1.271 từ, `c2/r1/*.txt` giống nhau từng byte), cùng người chấm headless, mù nhãn (`c2/r1/label-key.json`).

| | Headless (`toolkit/blind/headless.sh`) | `Explore` (agent con) |
|---|---|---|
| Người đọc | 6 (R1–R3, R6–R8) | 3 (R4, R5, R9) |
| Đạt nghĩa / khuyên | 6/6 · 0 | 3/3 · 0 |
| Chỗ mất chú ý | S19 thẻ phương pháp/giới hạn **4/6**; S08.2 1; S17.4 1 | S10.1 đoạn mô tả cách phát lại **3/3** |
| Token/lượt (đo) | **7,5–9,0 nghìn** (Sonnet 4,8 vào + 0,9–2,1 ra; Haiku phụ 2,7) | không có số đo: tệp ghi 36.000 là số giữ chỗ; ledger ghi cả lô ≈ 108 nghìn (ước) |
| Người đọc có đọc hết? | có | có (cả 3 trả lời nhắc Victor, 112 tháng) |

- **Kết luận đạt/trượt: trùng** (ngưỡng thứ nhất của `tongket-t4` §2a đạt).
- **Cảnh mất chú ý nhiều nhất: khác chỗ, cùng loại.** Cả hai đều là khối *phương pháp* (S10.1 "We took every purchase month…" và thẻ S19 "How we know this…"). Ngưỡng thứ hai ghi chữ "cùng cảnh" nên theo chữ là **không đạt**; theo nghĩa thì cả hai chỉ cùng một bệnh. Tách theo cách chạy: headless thấy khối phương pháp *cuối tập*, `Explore` thấy khối *giữa tập* — một lần so 3 lượt không đủ để nói cách nào nhạy hơn.
- **Lý do chọn headless:** cùng kết luận với giá ≈ 1/4 (Tập 4 đo 8,7–10,1 nghìn so 32–47 nghìn); không có ngữ cảnh repo (mù thật); người chấm cũng headless. Sau C2, Tập 5 chạy **toàn bộ** kiểm mù bằng headless (C3 có ảnh, C4 12/12, C5 so đủ mẫu 24 lượt) mà không có cổng nào bị chủ dự án lật lại ở G2 (L3 4·4·4·4·4·4).
- **Đổi luật ghi:** "cùng cảnh mất chú ý" → "cùng **loại** khối mất chú ý (phương pháp / định nghĩa / số dày / nhân vật)". Mỗi tập vẫn hỏi câu mất chú ý; khối được ≥ 2/6 nêu thì WRITER sửa — như Tập 5 v2 đã làm (S19 còn 1 câu → S18 3/6).
- **Ưu:** rẻ, mù thật, đã chạy trọn một tập. **Nhược:** một model đọc (Sonnet) — người đọc cùng model tương quan cao (`tongket-t4` §2c). **Tác động:** kiểm mù Tập 6 ≈ cùng mức Tập 5 về token/lượt; không thêm `Explore`. **Rủi ro:** điểm mù chung của Sonnet; giảm bằng một lượt người đọc model khác (Haiku hoặc Opus headless) ở C2 mỗi 3 tập, không phải mỗi tập.

### 2b. Đạo diễn máy chấm cảm xúc 2–3 — nguyên nhân ở kịch bản và hướng sửa
Đạo diễn A (C4, animatic 540p): **cảm xúc 2**, truyện 3, hình 3, nhịp 3; đạo diễn B: 3·3·3·3 (trục khác tên). L3 của chủ dự án ở G2: cảm xúc **4**. Theo D-010 §6 đạo diễn máy chỉ chẩn đoán; nhưng lý do A nêu chỉ thẳng vào kịch bản, không chỉ vào hình:

| Nguyên nhân (trích kịch bản `story/script.md`) | Vì sao làm lạnh cảm xúc |
|---|---|
| **Người xem chỉ được gọi là "you" ở S01**; từ S04 đến S15 là luật và phép phát lại, không ai đi qua nó | 4 phút (≈ 1:00–5:20) không có người để thương |
| **Ba người mua được hứa ở S03.4** ("three illustrative buyers who got very different answers") **nhưng chỉ có tên ở S15–S17** (≈ 5:23) | Lời hứa 4,5 phút không được trả; A: "ba khối trụ giống nhau đứng im 11 s ở 0:44" |
| **Cái giá bị cấm nói** (R1: không nêu số tiền phí PMI, S04.3) và không có thay thế cụ thể | Cái được–mất chỉ còn là *thời gian trên giấy*; không có "mỗi tháng thêm một dòng trên hoá đơn" |
| **Đỉnh cảm xúc (Victor, S17.3) là câu dài nhất, rối nhất** ("He got there by paying the loan down, and his own schedule, at his lower rate of 6.07 percent, reached…") | Cả hai đạo diễn nêu; chủ dự án giữ chữ ở G2 |
| **Ba thẻ cảm xúc** cả tập (S01.2, S17.1, S20.1); kết bằng câu khái quát (S20.2 "history gave answers from about a year to more than 9 years") | Kết không quay về một người |

**Hướng sửa ở kịch bản (cho `story.md` và đầu bài WRITER Tập 6; không sửa Tập 5):**
1. **Một nhân vật dẫn đường từ cold open đến kết** (người điển hình — Tập 5 là Grace): xuất hiện trước 0:45 (M5 đã đo), đi qua phần phương pháp ("Grace's month is one of 307"), và câu kết là câu của chính người đó. Hai người còn lại là đối trọng, ra ở hồi 3.
2. **Lời hứa nhân vật phải trả trong ≤ 90 s** hoặc không hứa (thêm vào điều kiện móc §3.9: M6).
3. **Cái được–mất bằng vật cụ thể khi không được nêu số tiền:** số hoá đơn, số tháng, một vật trong thế giới 3D (chồng tiền mệnh giá cố định đã có trong thư viện) — "23 more bills" thay cho "$X".
4. **Câu ở đỉnh cảm xúc ≤ 15 từ, một ý một câu** (REVIEWER soát ở C2; Victor S17.3 là ví dụ trượt).
5. **Kết quay về câu hỏi của nhân vật**, không quay về khái quát.
- **Ưu:** sửa ở chữ, rẻ nhất (trước khi có giọng, hình). **Nhược:** thêm ràng buộc cho WRITER; format `101` vốn là "khái niệm → thí nghiệm" nên nhân vật dẫn đường làm dài thêm ≈ 15–25 s (cũng là chỗ thiếu ở 2c). **Tác động:** L3 dòng 1 (cảm xúc) là dòng duy nhất cả đạo diễn A lẫn khung chất lượng xếp đầu. **Rủi ro:** nhân vật minh hoạ được kể như người thật → ILLUSTRATIVE phải theo mọi khung (luật đã có); không hiệu chuẩn được "cảm xúc" bằng máy → đo bằng L3 + đạo diễn máy chỉ chẩn đoán.

### 2c. Độ dài thật lệch ước: 8:19 → 7:46
Đo trên `out/script.json` (từ) và `out/factory/timeline.json` (giây) của từng tập:

| | Tập 2 | Tập 3 | Tập 4 | Tập 5 |
|---|---|---|---|---|
| Từ nói (số đọc ra chữ, bỏ thẻ) | 1.376 | 1.421 | 1.219 | 1.167 |
| Giây có lời (tổng câu) | 497,2 | 492,1 | 447,3 | 423,7 |
| **Tốc độ đọc Eric (từ nói / giây lời)** | 2,77 | 2,89 | 2,72 | **2,75** |
| Tổng thời lượng | 585,6 | 572,0 | 481,6 | 465,7 |
| **Từ nói / giây thời lượng** | 2,35 | 2,48 | **2,53** | **2,51** |
| Phần ngoài lời (giữ, ident, đuôi cảnh) | 18 % | 16 % | 8 % | 10 % |

(Tập 2 không đặt `speed`; Tập 3–5 cùng `eleven_v3`, `stability 0.5`, `speed 0.9`. Theo cảnh, Tập 5: 2,55–3,13, trung vị 2,77, độ lệch 0,15.)

**Nguyên nhân:** `story/check_script.py` ước bằng **2,4 từ nói/giây + hold + ident 3 s** → 1.167/2,4 = 486 s lời + ≈ 13 s = 8:19. Eric thật đọc **2,75**, nhanh hơn 15 %: lời thật 424 s (−63 s). Nhà máy thêm 42 s ngoài lời (ước chỉ tính 13 s). Hai sai số ngược chiều, cộng lại −33 s.
**Sửa:** ước G1 = **từ nói / 2,52** (hai tập nhà máy, chênh nhau 0,8 %), hoặc tách: từ nói / 2,75 + 10 % ngoài lời. Kiểm ngược: Tập 4 → 484 s (thật 481,6, +0,5 %); Tập 5 → 463 s (thật 465,7, −0,6 %). Đích `101` 8:15 = 495 s cần **≈ 1.250 từ nói** (Tập 5 thiếu ≈ 80 từ ≈ 32 s). Áp vào đề xuất 3.1.

## 3. Áp 8 bài học cine-lab (+ thumbnail thế giới 3D) — đề xuất, chờ duyệt

Bối cảnh: cine-lab đi trước Crux một lô về cùng loại vấn đề — tối ưu token và nhịp làm tụt hình (`BAI-HOC-LL` "bài học gốc lô 6–8": khung nhìn 52 → 19, khung lặp 18 % → 46 %), token "ước" thấp hơn thực nhiều lần (#56). Mỗi mục: đề xuất cụ thể cho Crux · ưu · nhược · tác động (5 tiêu chí; chất lượng là ràng buộc, D-009) · rủi ro.

### 3.1 G1 đo độ dài trên timeline ước theo tốc độ đọc thật của Eric; đích `101` ≥ 8:15
- **Đề xuất:** `check_script.py` (mỗi tập có một bản) thay `WPS = 2,4` bằng hai hằng đo được ở §2c: **2,75 từ nói/giây lời** cho mốc móc M1–M5 (giây trong 60 s đầu) và **2,52 từ nói/giây thời lượng** cho độ dài cả tập (gồm phần nhà máy thêm). Hằng ghi kèm nguồn (Tập 4–5, `tongket-t5/measure_pace.py`); đo lại sau mỗi tập, đổi khi lệch > 2 %. Đích G1 `101`: **≥ 8:15 ước** (495 s ≈ 1.250 từ nói) — dư ≈ 15 s cho sai số (Tập 4–5 sai ±0,6 %; theo cảnh độ lệch 0,15 từ/s). Thay luật T5-1 "≥ 8:10" (đo giọng thật cả tập ở G1 tốn ≈ 6.000 ký tự EL trước khi kịch bản duyệt).
- **Ưu:** biết thiếu/đủ ngay khi viết, 0 ký tự EL; Tập 5 sẽ thấy thiếu ≈ 32 s ở C2 thay vì ở C5. **Nhược:** hằng của một giọng/một model (`eleven_v3`, speed 0.9); đổi giọng là đo lại. **Tác động:** chất lượng ↑ (không phải chọn giữa độn và F07/mid-roll ở cuối tập); tốc độ ↑; công chủ dự án ↓ (bỏ một quyết định G2); chi phí ↓ (EL). **Rủi ro:** WRITER độn để đủ 1.250 từ → giữ luật `101` "không độn": thiếu chất thì nêu ở G1 (ngắn hơn, bỏ mid-roll), đúng như cine-lab LO-6-8 §6.4; câu thêm phải là chất có nguồn, REVIEWER soát.

### 3.2 Luật nhịp đo trước render → `checks-appeal` cho lô K
- **Đề xuất (bên dựng đo trước, K hiệu chuẩn rồi mới thành luật — CHARTER §6):** đo trên `spine.json` + timeline ước, trước khi render 540p:
  1. **Tựa/móc:** đã có M1–M5 (§3.9); thêm M6 "lời hứa nhân vật trả ≤ 90 s" (§2b).
  2. **Quãng hình đứng yên ≤ 8 s** khi có lời: không máy quay di chuyển, không vật thể đổi trạng thái. Tập 5 có ít nhất 4 quãng > 15 s (đạo diễn A: 0:44–0:55, 1:09–1:25, 1:58–2:30, 4:07–4:38) — đúng chỗ A chấm nhịp 3.
  3. **Tỉ lệ khung chỉ chữ** — chính là A13 (≤ 15 %); đưa bộ đo lên trước render.
  4. **Mật độ số:** ≤ 2 số mới mỗi cảnh (A17, đã chặn ở `spec.py`) + số neo ≤ 3 cả tập (cine-lab #37: 27 → 15 số trên hình).
  Ghi thành **A23** ở `checks-appeal.md` (luật nhịp đo trên spine, cấp CHÍNH sau hiệu chuẩn trên Tập 4 v3k/Tập 5 — hai tập đã duyệt L3 4×6).
- **Ưu:** bắt lỗi nhịp khi sửa còn rẻ (chữ/spine), không phải render lại 1080p (Tập 5: một lượt 1080p sạch ≈ 1,5 h). cine-lab: thẻ giấy 75 % → 15 % trong 3 tập, lời không đổi. **Nhược:** ngưỡng 8 s là của cine-lab (khung 2D); thế giới 3D có cảnh "thở" chủ ý. **Tác động:** chất lượng ↑ (nhịp — dòng 4 của L3); tốc độ ↑. **Rủi ro:** Goodhart — đổi hình chỉ để qua 8 s (cine-lab #44: thêm `alive()` bụi/hạt cho qua Q1). Chống: "đổi" phải là đổi mang nghĩa theo quy tắc D-010 §2.2 (máy chỉ đi giữa hai nhịp), hiệu chuẩn trên hai clip đã duyệt trước khi khoá, ±5 % nêu tên.

### 3.3 Chống tụt hình: chấm mù khung so với chuẩn + đa dạng khung nhìn + xem liền mạch mù; hiệu chuẩn trên Tập 1/Tập 4 trước khi khoá
- **Đề xuất:** ba thước, đều **chỉ báo** ở Tập 6, chưa thành ngưỡng:
  1. **Chấm mù khung:** người đọc headless có ảnh chấm 1–10 một bộ khung (1 khung/20 s) của tập mới và của tập chuẩn, xáo trộn, không biết tập nào (cine-lab Q27: tập 6 v2 5,40 vs tập 1 5,03, 3/3 người chấm cùng chiều). Tập chuẩn của Crux: **Tập 4 v3k và Tập 5** (L3 4×6) — không dùng Tập 1 (thẻ chữ 2D, trước Mốc V, không còn là gu kênh; chỉ dùng làm đối chứng *âm*: thước phải xếp Tập 1 dưới Tập 4/5, không thì thước hỏng).
  2. **Đa dạng khung nhìn:** số khung nhìn khác nhau (vị trí + hướng máy quay từ `camera.json`/spine, không đo độ sáng — cine-lab #71: thước xám gộp mọi cảnh tối) và cụm lặp lớn nhất.
  3. **Xem liền mạch mù:** 3 người xem headless xem dải khung + lời ±2,5 s (cine-lab #73: cửa sổ ±6 s tự tạo lỗi giả), báo chỗ "đổi phong cách" / "đứng hình". Sửa điểm ≥ 2/3; kiểm trên khung thật trước khi sửa.
- **Ưu:** đo đúng thứ đã tụt ở cine-lab (đa dạng, liền mạch) mà checks khoá của Crux chưa đo. **Nhược:** thêm ≈ 6–9 lượt headless có ảnh mỗi tập (≈ 0,1 triệu token); thước mới phải hiệu chuẩn (CHARTER §4 chống Goodhart). **Tác động:** chất lượng ↑ (hình, liền mạch); chi phí ↑ nhẹ. **Rủi ro:** thước tự tạo lỗi (cine-lab #73, #71); người chấm cùng model ưa cùng kiểu hình. Hiệu chuẩn: chạy trên Tập 1 (đối chứng âm), Tập 4 v3k, Tập 5 trước Tập 6; thước nào không xếp đúng thứ tự thì bỏ.

### 3.4 Âm: nhạc hiệu mở/đóng, mỗi hồi một cue, lặng ~0,8 s trước số neo
- **Đề xuất:** (a) **nhạc hiệu kênh** 3 s ở ident (đã có chỗ: `IDENT_S = 3`) và một khúc đóng khác; (b) nhạc theo bản đồ căng (F-3, Tập 5 đã có: 9,0 LU yên → đỉnh, chốt V→I trên "removed") **thêm ràng buộc mỗi hồi một cue riêng, không lặp vòng**; (c) **lặng 0,7–0,9 s trước mỗi số neo** (tối đa 3 số neo/tập, §3.2.4) — Tập 5 dùng `hold` sau câu (S02.1 1 s, S16.2 1 s), chưa có lặng *trước* số. Gu nhạc là quyền chủ dự án (CHARTER §6): (a) cần chủ dự án duyệt một bản nhạc hiệu (C3 bằng clip có âm).
- **Ưu:** cine-lab Q28 đạt cả 4 điểm trên tập được duyệt lại; Crux đã có hạ tầng (F-3, sfx F-2). **Nhược:** lặng làm dài tập ≈ 2–3 s (có lợi cho `101`); nhạc hiệu là việc gu, thêm một lần chủ dự án chạm (một lần cho cả kênh). **Tác động:** chất lượng ↑ (âm, cảm xúc); công chủ dự án +1 lần (một lần duy nhất). **Rủi ro:** nhạc hiệu bằng mã nghe "máy"; F-2 đã cảnh báo sfx dày (đoạn a: 21,7 sự kiện/phút, 8 trong 10 s) — thêm cue không được tăng mật độ; số neo lặng trước nhưng sfx "land" trên chính từ khoá (F-2 cảnh báo SNR 11 dB) phải bỏ.

### 3.5 G1 theo lô 2–3 tập (chủ dự án quyết)
- **Đề xuất:** một G1 cho **Tập 6 + Tập 7** (đề tài, logline, kịch bản v1, tiêu đề nháp), dựng tuần tự, mỗi tập G2 riêng. Lô 2 chứ không 3: thư viện 3D còn mỏng, Tập 7 cần vật thể mới biết sau Tập 6.
- **Ưu:** chủ dự án chạm G1 một lần cho 2 tập; C2 hai tập dùng chung một lượt REVIEWER + kiểm mù (cine-lab: 1 subagent 3 vai cho 3 tập, 57 nghìn). **Nhược:** kịch bản Tập 7 viết trước khi có bài học Tập 6; sửa nhà máy giữa hai tập có thể đổi khả năng hình. **Tác động:** công chủ dự án ↓ (−1 lần/2 tập); tốc độ ↑. **Rủi ro:** CHARTER §2.2 "không mở chu kỳ mới khi tập trước chưa xong" — G1 lô không mở dựng Tập 7 trước G2 Tập 6, chỉ duyệt chữ trước; lời đã duyệt mà phải đổi (bài học Tập 6) → "đổi kịch bản đã duyệt" là ngoại lệ phải hỏi (CHARTER §5) — thêm một lần chạm nếu xảy ra.

### 3.6 Token đo bằng log phiên (như mục 1)
- **Đề xuất:** mỗi phiên khi đóng ghi vào PLAN mục 5 bốn số đọc từ log (sự kiện `result` của transcript: `usage`, `modelUsage` tích luỹ): **sinh ra · đầu vào mới (input + ghi cache) · đọc cache · trần = đầu vào mới + sinh ra**; ledger giữ số harness của agent con chỉ để phân loại việc. Công cụ: `tongket-t5/token_log.py` (đọc JSONL đã trích). Định nghĩa trần (sinh ra / đầu vào mới / tổng) là quyền chủ dự án — đề xuất **đầu vào mới + sinh ra** như cine-lab và như lệnh phiên này.
- **Ưu:** hết số "ước" (Tập 5 G2 ước ≈ 10 triệu — xem mục 1 để so). **Nhược:** trích log tốn công: transcript chỉ đọc được qua công cụ phiên, 100 sự kiện/lượt (phiên này: 5 agent quét). Headless (`claude -p`) không nằm trong log phiên → cộng từ `tokens` trong JSON đầu ra (đã có, `headless.sh`). **Tác động:** chi phí đo ↑ nhẹ, quyết định đúng ↑. **Rủi ro:** `headless.sh` gộp đọc cache vào `in` → không tách được đầu vào mới; sửa `headless.sh` ghi riêng 4 trường (việc nhỏ, không phải `checks/`).

### 3.7 PLAN tập ≤ 1 trang, "phiên sau đọc ≤ 8 tệp", lịch sử sang archive
- **Đề xuất:** mẫu `playbook/templates/PLAN-tap.md` theo `cine-lab/playbook/PLAN-TAP-MAU.md`: trạng thái · việc tiếp (≤ 3) · quyết định đã có (ngày, trỏ `gates/*-answer.md`) · mức cảnh báo · **phiên sau đọc ≤ 8 tệp** · lệnh chạy tiếp. Bảng cổng chi tiết, lệnh cũ, giao file → `episodes/epNNN/archive/PLAN-history.md`. Hiện trạng: `episodes/ep005/PLAN.md` 10,5 KB, danh sách đọc 12 tệp, mục 4 giữ 4 điểm dừng cũ; **`PLAN.md` gốc vẫn là PLAN Tập 1** (56 dòng, 30/09) — chuyển vào `archive/ep001-v1/` và thay bằng PLAN kênh 1 trang (tập hiện hành, nhánh, việc treo).
- **Ưu:** mỗi phiên mở đọc ít hơn → đầu vào mới ↓ ở mọi lượt (ngữ cảnh mang theo suốt phiên). **Nhược:** lịch sử cách một bước nhấp. **Tác động:** chi phí ↓, tốc độ ↑; chất lượng = (không bỏ thông tin, chỉ dời). **Rủi ro:** quyết định của chủ dự án lạc vào archive → luật: quyết định còn hiệu lực luôn ở PLAN hoặc `gates/*-answer.md`, không chỉ ở archive.

### 3.8 Sửa nhà máy gom về đầu tập/nhánh riêng; giữa tập chỉ sửa lỗi chặn
- **Đề xuất:** việc nhà máy (toolkit/factory, world, mẫu) làm trên **nhánh `factory-*` trước G1** hoặc ngay sau G1 trước C3, test + chứng minh trên đoạn cũ, merge `main`, rồi tập mới dùng. Giữa tập (C3 → G2) chỉ sửa lỗi **chặn** tập đang làm. Hiện trạng Tập 5: F-5, F-2, F-3, F-1 + "nhà máy page.json/F08/F11/Shorts" đều làm **giữa C3 và C4** (ledger: 0,63 + 0,49 triệu theo số harness), cùng lúc dựng tập.
- **Ưu:** sửa thư viện làm render lại cả tập (cine-lab #23, #70: mất ~2,5 h khung) — gom một lần thì render một lần; tập không đổi khả năng giữa chừng. **Nhược:** cải tiến tìm thấy giữa tập phải chờ tập sau (trừ khi chặn). **Tác động:** tốc độ ↑, chi phí ↓ (ít lượt render 1080p lặp); chất lượng = nếu "chặn" gồm cả lỗi CHÍNH theo D-009 (a). **Rủi ro:** định nghĩa "chặn" quá hẹp làm trái D-009 — đề xuất: **"chặn" = CHẶN + CHÍNH của tập đang làm**; cải tiến không gắn lỗi nào thì vào `toolkit/factory/BACKLOG.md`.

### 3.9 Thumbnail dùng hình thế giới 3D thay cho chữ + cột 2D
- **Đề xuất:** thumbnail = **một khung tĩnh của thế giới** (nhà, người không mặt, chồng tiền) render bằng chính `build_seg.py` ở 1280×720, cộng tối đa 3–4 từ lớn; bỏ cột 2D. Hiện `design/g2/thumbs.js` vẽ chữ + cột 2D. Ba phương án mỗi tập: (1) cảnh thế giới + 3 từ, (2) cảnh thế giới + 1 số "on paper", (3) như Tập 5 thumb-3 (đối chứng); chủ dự án chọn mặc định, T&C đo (episode.md §5).
- **Ưu:** thumbnail giống video (người bấm thấy đúng cái sẽ xem); dùng lại cảnh đã duyệt C3, không thêm tài sản. **Nhược:** khung 3D nhỏ ở 168×94 px có thể khó đọc hơn chữ + cột. **Tác động:** CTR chưa biết — đo bằng T&C, không bằng người đọc (so cặp thumbnail đã bỏ, 0/2 lần đổi quyết định). **Rủi ro:** claim-risk vẫn áp (ILLUSTRATIVE, "on paper", R1 không nêu phí); nhân vật không mặt khó tạo cảm xúc ở cỡ nhỏ → phương án (3) giữ làm đối chứng trong T&C ít nhất 2 tập.


## 4. Hàng chờ lô K: A13–A22 + F11/F12 + A9 (gom, đề xuất thứ tự)

Trạng thái K3.9 (`checks/README.md`): **chỉ thêm kind**; A9–A12 và mọi A13+ **chưa xử lý**. Trên Tập 5 cuối (`run-c5c`): **F11 PASS, F12 PASS** (nhà máy đã sinh đủ artefact và `page.json` ở C4 — A11 xong phía dựng), V11 CHÍNH được ngoại lệ chờ A22.

| Nhóm | Mục | Việc của K | Cần chủ dự án? | Bằng chứng có sẵn | Ưu tiên |
|---|---|---|---|---|---|
| **1. Sửa luật cũ đang gây ngoại lệ mỗi tập** | **A22** V11 tách glyph/plate | sửa V11, selftest 3 ca | **có** (sửa luật cũ) | Tập 5 C5b: 2.605 đếm, đè thật 0 | 1 |
| | **A10 + A16** F11/F12 đọc từ nhà máy (gồm sản phẩm `world:`) | viết lại nguồn danh sách; đối chứng xoá 1 file → trượt | **có** | Tập 5 PASS sau khi nhà máy sinh đủ artefact + `page.json` ở C4 (ledger) → viết lại để danh sách lấy từ nhà máy, không từ khai báo | 2 |
| | **A21** tách `advice_stated` / `advice_inferred` | sửa rubric + câu hỏi phụ; hiệu chuẩn 19 lượt N1/N2 + đối chứng dương | **có** (sửa rubric) | Tập 5 C3 | 3 |
| | **A9** rubric khuyên (thận trọng chung không tính) | hiệu chuẩn đối chứng cùng chủ đề | **có** | Tập 4 C3 12/12, C4 9/9 (ngoại lệ có ghi) | 3 (gộp với A21 — cùng rubric) |
| **2. Luật mới, chỉ thêm (tự merge theo D-008 §2 nếu selftest đạt)** | **A20** không nêu số tiền phí không nguồn | luật CHẶN mới; selftest 2 câu | không | Tập 5 R1 0 vi phạm | 4 |
| | **A17** ≤ 2 số mới nói mỗi cảnh | đưa `numbers_said.py` vào checks | không | selftest 5/5; Tập 3 có 3 cảnh vượt | 5 |
| | **A14** đồng bộ ±0,2 s ≥ 92 % | đưa `sync_audit.py` vào checks | không | Tập 4 23/23, Tập 5 11/11 (đoạn chứng minh); Tập 5 C3 25/25 | 5 |
| | **A18** bốn kiểm `verify_seg.py` cho đoạn `world:` | luật trang | không | Tập 5 mọi đoạn rule1–3 = 0, cắt cứng 0 | 5 |
| | **A13** khung chỉ chữ ≤ 15 % | luật mới; cần định nghĩa trên nhật ký trang | không, nhưng phải hiệu chuẩn | chưa đo trên Tập 5 cuối | 6 |
| | **A19** mật độ sfx + nhãn đè | bộ đo F-2 **đã có** (Tập 5: test 5/5; đoạn a WARN 21,7 sfx/phút) → hiệu chuẩn ngưỡng trên Tập 4/5 | không | `build-report.json` F2 | 6 |
| | **A23 (mới, §3.2)** luật nhịp trên spine | bên dựng đo trước; K hiệu chuẩn | không | đạo diễn A: 4 quãng > 15 s | 7 |
| | **A24 (mới, T5-2)** nhãn ≥ 1 s mỗi 3 từ | luật trang mới | không | Tập 5 nhãn Fannie Mae 9 từ/≈ 1 s | 6 |
| **3. Báo cáo, không phải luật máy** | **A15** ghi `fix: picture\|label` mỗi vòng | mẫu `gates/Cx-blind.md` + REVIEWER | không | Mốc V vòng #21/#22 | 8 |
| | **A12** README bỏ "chờ duyệt" | sửa chữ + LOCK | không | — | 8 |

- **Đề xuất cách chạy:** một phiên K, **hai lần merge**: (i) nhóm 2 (chỉ thêm) tự merge khi selftest đạt; (ii) nhóm 1 gửi chủ dự án một gói hỏi gộp (A22, A10+A16, A9+A21) — một lần chạm. Làm **trước C3 Tập 6** (đúng §3.8: sửa máy đầu tập), để Tập 6 không phải xin ngoại lệ V11 lần nữa.
- **Ưu:** bỏ 2–3 ngoại lệ lặp mỗi tập (V11, F11/F12 khai tay, khuyên suy ra). **Nhược:** phiên K lớn (≈ 12 mục); luật mới có thể làm Tập 5 "trượt" hồi tố (cine-lab #57) — chỉ báo, không sửa tập đã phát. **Tác động:** công chủ dự án ↓ (bớt ngoại lệ), chất lượng ↑ (đo đúng đè thật, khuyên thật). **Rủi ro:** A13/A19/A23/A24 chưa hiệu chuẩn → K chỉ khoá sau khi xếp đúng Tập 4 v3k/Tập 5 (đã duyệt) là đạt; thiếu đối chứng thì để THAM KHẢO.
- Đã ghi A23, A24 và thứ tự mới vào `checks-appeal.md` (chỉ thêm dòng hàng chờ; không sửa `checks/`).


## 5. Hai ứng viên đề tài Tập 6

Cân bằng trụ đến Tập 5: **vay và nợ 3** (Tập 1 tái cấp vốn, Tập 2 vay học, Tập 5 PMI) · **hưu trí 1** (Tập 3 trái phiếu) · **thuế 1** (Tập 4 nhà $500.000). Tập 6 nên là hưu trí hoặc thuế. Thư viện 3D hiện có (`toolkit/factory/world/lib3d.js`): `House`, `Stack` (chồng tiền mệnh giá cố định), `Beam`, `Person` (không mặt), `Neighborhood`, `Ribbon` (vệt dữ liệu), `Apartment`, `Shield`, `Studio`, `Fan`, `Burst`.

| | **A. #12 "Does a 2% Annuity Raise Really Keep Up With Prices?"** (`topics-r1/machine/retire-1/`) | **B. #2 "Overtime or a Second Job at $48 an Hour: Which Pays More?"** (`topics-r1/machine/tax-4/`) |
|---|---|---|
| Trụ | hưu trí (cân bằng 1 → 2) | thuế (1 → 2) |
| Câu chuyện | Người về hưu 65 tuổi chọn tấm séc cố định hay tấm séc tăng 2 %/năm; thử 2 % trên mọi chuỗi 20 năm giá Mỹ (CPI-U) | Người làm theo giờ $32 thêm 8 giờ/tuần: tăng ca $48 hay việc thứ hai $48; tính đủ thuế liên bang gồm khoản trừ tăng ca mới |
| Phát hiện | 2 % giữ được sức mua ở **17/715** chuỗi (2,4 %, chỉ khởi đầu 1947–49) — móc mạnh, có số đếm | Tăng ca hơn khoảng $1.408 (ví dụ), việc thứ hai cần ≈ $5/giờ hơn để bằng |
| Dữ liệu thật / "phòng thí nghiệm" | Có: 80 năm CPI, phát lại từng tháng — đúng định vị kênh | Yếu hơn: phép tính luật thuế cho một người ví dụ; dữ liệu thật chỉ là lương giờ AHETPI |
| Thư viện 3D | **Dùng lại nhiều:** `Person` (người về hưu), `Stack` (séc hằng tháng = chồng tiền; sức mua = cùng chồng mua được ít hơn), `Ribbon` (đường giá 20 năm), `House`/`Neighborhood` nền. Vật mới: **giỏ/kệ hàng** (giá) — 1 vật qua C3 | Dùng lại `Person`, `Stack` (phiếu lương). Vật mới: **đồng hồ chấm công**, **nơi làm thứ hai**, **tấm séc thuế/biểu thuế bậc** — 2–3 vật qua C3 |
| Hồ sơ | **Chưa có `model.json` + `statements.json`** → Việc 0 lớn hơn; kind mới (cửa sổ trượt sức mua) | Có `model.json` + `statements.json` + ERRATA đã áp (E1) → Việc 0 nhỏ; kind mới (tính thuế theo luật) |
| **Ưu** | Phát hiện bất ngờ, đếm được; dữ liệu thật dài; hình "cùng chồng tiền mua ít đi" là hình mang nghĩa đúng D-010 (số chỉ ở chế độ đồ thị); cảm xúc dễ (một người về hưu, một quyết định không làm lại được) — chữa đúng bệnh §2b | Thời sự (khoản trừ tăng ca 2025–2028); khán giả rộng; hồ sơ sẵn |
| **Nhược** | Không mô hình giá niên kim (séc 2 % khởi đầu thấp hơn) → không được nói "2 % là lựa chọn tệ"; 715 cửa sổ chồng lấp không độc lập; cần phiên K kind mới | Báo chí đã nói "chỉ phần trả thêm được trừ"; kết quả phụ thuộc bậc thuế/tình trạng hôn nhân → phần lớn tập là điều kiện; ít "phát lại lịch sử" hơn định vị kênh |
| **Tác động** | Trụ cân bằng; thư viện 3D thêm 1 vật dùng lại được (giỏ giá dùng cho mọi tập lạm phát); format `lab` hoặc `101` đều được | Trụ cân bằng; thêm 2–3 vật ít dùng lại; tập ngắn (`101`) |
| **Rủi ro** | claim-risk: không khuyên chọn phương án hay sản phẩm, không dự báo lạm phát, "history, not a forecast", CPI-U ≠ giỏ hàng người già; tháng 10/2025 CPI trống (cửa sổ chạm bị bỏ) | Luật mới có thể đổi/được IRS hướng dẫn thêm (FLSA overtime, ngưỡng MAGI $150.000, hết hiệu lực sau 2028) → kiểm nguồn lại lúc làm; "Overtime is tax-free" phải sửa mọi chỗ; không khuyên "nhận tăng ca"; số liệu luật 2026 cần nguồn toàn văn đọc được (kiểm truy cập ở Việc 0) |

**Khuyến nghị: A (#12, hưu trí)** — khớp định vị "phòng thí nghiệm trên dữ liệu thật", dùng lại thư viện 3D nhiều nhất, móc có số đếm, và có sẵn nhân vật cho hướng sửa cảm xúc §2b. B giữ cho Tập 7 (nếu chủ dự án duyệt G1 lô 2 tập, §3.5: A + B cân đúng hai trụ còn thiếu). Chọn đề tài là quyền chủ dự án (D-004 §1).

