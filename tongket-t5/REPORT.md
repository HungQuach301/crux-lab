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

(Tập 2 trước `speed: 0.9`; Tập 3–5 cùng `eleven_v3`, `stability 0.5`, `speed 0.9`. Theo cảnh, Tập 5: 2,55–3,13, trung vị 2,77, độ lệch 0,15.)

**Nguyên nhân:** `story/check_script.py` ước bằng **2,4 từ nói/giây + hold + ident 3 s** → 1.167/2,4 = 486 s lời + ≈ 13 s = 8:19. Eric thật đọc **2,75**, nhanh hơn 15 %: lời thật 424 s (−63 s). Nhà máy thêm 42 s ngoài lời (ước chỉ tính 13 s). Hai sai số ngược chiều, cộng lại −33 s.
**Sửa:** ước G1 = **từ nói / 2,52** (hai tập nhà máy, chênh nhau 0,8 %), hoặc tách: từ nói / 2,75 + 10 % ngoài lời. Kiểm ngược: Tập 4 → 484 s (thật 481,6, +0,5 %); Tập 5 → 463 s (thật 465,7, −0,6 %). Đích `101` 8:15 = 495 s cần **≈ 1.250 từ nói** (Tập 5 thiếu ≈ 80 từ ≈ 32 s). Áp vào đề xuất 3.1.

<!-- MỤC 3 -->

<!-- MỤC 4 -->

<!-- MỤC 5 -->
