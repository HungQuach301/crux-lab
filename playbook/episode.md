# Sổ tay chạy một tập (playbook v4, Mốc V, 06/10/2026)

Áp từ Tập 4 (`decisions/D-006.md`); v4 áp D-009 (chất lượng là ưu tiên tuyệt đối) và D-010 (thế giới 3D, 8 quy tắc hình–âm) từ Tập 5. Khung: `playbook/quality-framework.md`. Biên kịch: `playbook/story.md`. Prompt mẫu: `playbook/prompts/`. Một tập chạy bằng một dòng: **"Chạy Tập N, phiên P1"** (hoặc "…, đề tài #k, phiên P1"), rồi "… P3" (và "… P2" chỉ khi G1 ghi "cần C3").

## 0. Mở phiên
`bash toolkit/verify.sh <nhánh-lệnh-ghi>`: kiểm công cụ, nhánh đúng lệnh (không tự đặt nhánh), `main` mới nhất. Trượt thì báo, không làm tiếp.

## 1. Ba cổng, mỗi chặng một phiên (D-011)

**Từ Tập 6:** phiên điều phối mới ở mỗi điểm dừng chờ chủ dự án (G1, C3 nếu có, G2); phiên cũ đóng bằng PLAN tập ≤ 1 trang + prompt phiên kế (tên nhánh, chỗ dán câu trả lời) — `prompts/RUN.md` mục "Đóng phiên". Bảng dưới là các chặng; sau G2 (giao hàng → G3 → merge) là một phiên mới.

| Phiên | Việc | Kết thúc ở | Chủ dự án |
|---|---|---|---|
| **P1** | Việc 0 (dữ liệu, mô hình, kiểm độc lập) → C1 máy (≤ 3 đề tài + logline, kiểm mù kể lại) → C2 (kịch bản, móc, kiểm máy + kiểm mù lời) → giao phiên K → **G1** | G1 trả lời | **G1** (1 lần) |
| **P2** *(khi tập có hình mới: ký hiệu, vật thể 3D, hero object, mẫu chuyển cảnh)* | C3 hình mới (không trần số; cổng gốc; **clip có chuyển động và âm**) | C3 trả lời | C3 |
| **P3** | C4 animatic (TỰ ĐỘNG) → C5 render + L1 (TỰ ĐỘNG) → **G2** → giao hàng → **G3** | Chủ dự án đăng; merge `main` | **G2**, **G3** |

- **G1 sau C2** (D-006 Q2), một gói ≤ 3 câu:
  1. đề tài + logline;
  2. kịch bản: cấu trúc, cold open và móc đã chọn **dạng chữ**, kèm 2 phương án móc còn lại, mỗi phương án một dòng;
  3. tiêu đề nháp + danh sách hình mới (→ C3).
- **Duyệt theo lô:** một G1 được duyệt 3–4 đề tài + logline cho cả mùa (`topics/season.md`). Tập sau lấy đề tài kế tiếp trong danh sách; G1 của tập đó chỉ còn câu 2–3.
- **Chưa có danh sách mùa:** P1 viết C2 cho đề tài được khuyến nghị; G1 hiện hai ứng viên kia, mỗi ứng viên một dòng. Đánh đổi: chủ dự án đổi đề tài → C2 viết lại (≈ 1 lượt WRITER + 6 người đọc). Máy không tự chọn đề tài (D-004).
- **Giọng, nhạc, hướng hình** dùng mặc định đã chốt (Eric `eleven_v3`; nhạc bằng mã theo bản đồ căng, biên độ rộng; hướng hình "một thế giới, hai chế độ máy quay" D-010 + thư viện hình). Muốn đổi thì chủ dự án nêu ở G1.
- **Chất lượng trước (D-009):** lỗi CHÍNH **sửa trước phát hành** (ngoại lệ: sửa làm hỏng yếu tố chất lượng khác → gói nêu, kèm số đo/bản trước-sau, chủ dự án chọn). Cổng gốc trượt nghĩa → **sửa bằng hình trước**, nhãn là cách cuối. Token chỉ cảnh báo (§8). **Ngoại lệ phải hỏi:**
  - đổi kịch bản đã duyệt;
  - số không xác minh được nguồn;
  - rủi ro pháp lý/bản quyền;
  - chi tiêu mới (CHARTER §6).
- Mỗi tập một nhánh `epNNN` từ `main`. Chỉ phiên điều phối chặng cuối (sau G2) merge (fetch trước; trong file dùng chung chỉ sửa phần của tập).
- **Bàn giao qua `episodes/epNNN/PLAN.md` ≤ 1 trang** theo mẫu `playbook/templates/PLAN-tap.md` (tổng kết Tập 5 §3.7): 1 trạng thái · 2 việc tiếp (≤ 3) + việc treo · 3 quyết định đã có (trỏ `gates/*-answer.md`) · 4 đã sửa gì, vì sao · 5 mức cảnh báo + 4 số token mỗi phiên + giờ render · 6 **phiên sau đọc ≤ 8 tệp** · 7 prompt phiên kế (D-011). Bảng cổng chi tiết, lệnh cũ, giao file → `episodes/epNNN/archive/PLAN-history.md`; quyết định còn hiệu lực không chỉ nằm ở archive. `PLAN.md` gốc repo là **PLAN kênh** ≤ 1 trang (tập hiện hành, nhánh, việc treo, hàng chờ K) — phiên điều phối chặng cuối cập nhật khi merge.
  Phiên sau chỉ đọc các tệp ở mục 6 của PLAN tập.
- **Tối đa 3 vòng mỗi lỗi (lessons V1):** một lỗi ở một cảnh sửa tối đa **3 vòng**; hết 3 vòng → gói nêu **bản trước/sau** kèm số đo để chủ dự án chọn (D-009 E3). **Khoá nghĩa (V2):** bản mới có điểm cổng gốc thấp hơn bản tốt nhất trước đó, hoặc có câu khuyên, thì tự loại — sửa tiếp từ bản tốt nhất.
- **Lượt đạo diễn (bắt buộc, chẩn đoán — D-009 E5, D-010 §6):** trước render bản cuối, mỗi đoạn có hình mới qua một lượt đạo diễn trên bản 540p (`quality-framework.md` §10): 4 trục + lời phê theo mốc giây. Lời phê là việc nên xem, không phải ngưỡng; **chỉ sửa nhận xét lặp ở ≥ 2 lượt độc lập** (lessons V3); không mở vòng sửa thẩm mỹ chỉ vì điểm máy. Thước đo cuối là phiếu L3 ở G2 (≥ 4 mọi dòng).
- **Đoạn thế giới 3D:** khai `world:` trong `episode.yaml`; dựng và kiểm bằng `toolkit/factory/world/build_seg.py`. **Ghép vào master** bằng bước `splice` của nhà máy (BACKLOG F-5 xong 07/10, `toolkit/factory/world/splice.py`, test `test_world_splice.py`): hình thay khung các cảnh đoạn chiếm, tiếng đoạn vào stem tập, loudnorm chung; `spec.py` chặn cảnh không liên tiếp hoặc một cảnh nằm trong hai đoạn. Đoạn dựng (lint → spine → render theo cảnh có cache → âm → verify quy tắc 1/2/3/7); đồng bộ ±0,2 s bằng `sync_audit.py`; C14 trên bản 1080p.
- **Sửa nhà máy gom đầu tập (tổng kết Tập 5 §3.8):** việc nhà máy làm trên nhánh `factory-*` trước G1 hoặc sau G1 trước C3, merge `main` rồi mới dùng. Giữa tập (C3 → G2) chỉ sửa lỗi **chặn = CHẶN + CHÍNH** của tập đang làm; cải tiến khác ghi `toolkit/factory/BACKLOG.md`.
- **Số nói (B+2):** ≤ 2 số **mới** được nói mỗi cảnh (`toolkit/factory/numbers_said.py`, BLOCK trong `spec.py`); số thứ ba trở đi lên nhãn trên hình (người biên tập chọn), phạm vi không đổi.
- **Giọng theo cảnh (B+1):** `voice_overrides: {Sxx: {seed | settings | voice | model | take}}` trong `episode.yaml` khi một cảnh cần take khác (vd Tập 5 S18 seed 1006).
- Trước mỗi gói cổng và mỗi issue TỰ ĐỘNG: **REVIEWER** soát (`quality-framework.md` §7).
- **Agent dựng không chờ (tổng kết Tập 5 §1e.1, chủ dự án duyệt 08/10).** Tập 5: agent con dựng W4 + W5 tốn ≈ 71 triệu trần (83 % cả tập), W5 ghi cache 49,6 triệu so với sinh ra 0,36 triệu — phần lớn là agent ngồi chờ lượt 1080p (≈ 1,5 h) và checks (≈ 1,3 h), mỗi lần thức dậy nạp lại cả ngữ cảnh 0,4–0,65 triệu.
  1. Agent dựng **khởi chạy build/checks bằng công cụ chạy nền của phiên** (an toàn chạy nền: §11b) rồi **trả việc ngay** — không chờ, không hỏi trạng thái theo vòng.
  2. Phiên điều phối nhận thông báo lệnh nền xong, rồi giao **agent MỚI, đầu bài ngắn** đọc `out/factory/build-report.json` / `checks-runs/<run>/report.json` (ngữ cảnh ≈ 50–100 nghìn), quyết vòng sửa.
  3. **Một vòng sửa = một agent.** Không gọi lại agent cũ, không giữ agent sống qua một lượt render.
  4. Đầu bài agent mới **chép "đã sửa gì, vì sao"** của các vòng trước (≤ 10 dòng, lấy từ PLAN tập — mẫu `playbook/templates/PLAN-tap.md`) để không mất ngữ cảnh sửa: cảnh, lỗi (mã luật), cách sửa, kết quả đo, việc còn lại.
  Cùng lệnh dựng, cùng checks, cùng kiểm mù → chất lượng không đổi; số đo đối chiếu: CHẶN/CHÍNH và cổng gốc như C5c Tập 5. Kiểm ở Tập 6: đọc transcript một agent dựng, đếm lượt ghi cache > 0,3 triệu.

## 2. Model, effort, số agent

| Việc | Model | Effort |
|---|---|---|
| Điều phối, WRITER, REVIEWER, tổng kết | Opus | Medium |
| Người đọc kiểm mù, người chấm, so cặp | Sonnet **headless** (`toolkit/blind/headless.sh`, không agent con) | mặc định |
| Render, checks, mã hoá, sinh giọng | lệnh trực tiếp (không agent) | — |

Mỗi agent con tốn **≈ 32–49 nghìn token cố định** (Mốc B, Tập 4). Một lượt đọc mù headless tốn **≈ 9–10 nghìn** (chữ) và **≈ 11 nghìn** (ảnh, `--read`) — `tongket-t4/REPORT.md` §2a. Ý đồ mỗi cổng ghi trước số lượt dự kiến. Dùng lệnh trực tiếp thay agent khi không cần độc lập.

**Kiểm mù (Tập 5, lessons H2–H3):**
- **C1:** 3 người đọc mỗi logline (2 T + 1 G), không đối chứng, không so cặp tiêu đề; dừng khi 2 sai.
- **C2:** 6 người đọc + 1 người chấm, ≤ 2 vòng; dừng khi gặp khuyên_tính đầu tiên (A9) hoặc 2 sai; không dừng sớm khi đạt.
- **Cổng gốc (C3/C4):** chỉ nhịp loại 1; 2 người đọc mỗi nhịp, người thứ 3 chỉ khi chia; người chấm độc lập.
- **Không chạy:** tóm tắt AI ở G2, so cặp thumbnail, đối chứng trong tập thường (chỉ khi rubric mới, việc lô K), hiệu chuẩn so cặp móc (đã xong).
- **Headless là cách kiểm mù chính** (tổng kết Tập 5 §2a, chủ dự án duyệt 08/10): C2 Tập 5 so song song 6 headless + 3 `Explore` — đạt/trượt trùng (6/6, 3/3, 0 khuyên); khối mất chú ý nhiều nhất khác cảnh nhưng **cùng loại** (khối phương pháp: S19 thẻ 4/6 vs S10.1 3/3); headless ≈ 1/4 giá, mù thật. **Không dùng `Explore` cho kiểm mù.**
- **Câu mất chú ý** hỏi ở mọi kiểm mù lời (C2). Ngưỡng so/sửa đọc theo **loại khối**, không theo cảnh: *phương pháp / định nghĩa / số dày / nhân vật*. Một loại khối được **≥ 2/6** người đọc nêu → WRITER mới sửa khối đó (như Tập 5 v2: S19 còn 1 câu → S18 3/6).
- **Một lượt người đọc model khác ở C2 mỗi 3 tập** (Tập 6, 9, 12…): thêm 1–2 người đọc headless Opus hoặc Haiku (`headless.sh --model`) trên cùng gói lời, cùng người chấm; giảm điểm mù chung của Sonnet (người đọc cùng model tương quan cao, lessons H3). Ghi kết quả so với 6 người Sonnet vào ledger; lệch đạt/trượt hoặc lệch loại khối → nêu ở G1.

## 2b. Thước chỉ báo chống tụt hình (tổng kết Tập 5 §3.2–3.3, từ Tập 6)
Chạy ở C4 (spine + animatic) và C5 (bản cuối), báo một bảng trong gói G2; **chỉ báo, không ngưỡng, không mở vòng sửa chỉ vì số** (CHARTER §4). Lệnh và trạng thái: `toolkit/indicators/README.md`; hiệu chuẩn 08/10 trên Tập 1 (đối chứng âm), Tập 4 v3k, Tập 5: `tongket-t5/indicators/CALIBRATION.md`.
- **Giữ:** nhịp trên spine (quãng có lời không cú máy/không vật đổi trạng thái > 8 s — **chưa hiệu chuẩn**, đối chứng dương 2/4); đa dạng khung nhìn theo máy quay (xếp đúng: Tập 1 cụm lớn nhất 58,5 %, Tập 5 6,8 %); mỗi vật thể đổi trạng thái có tiếng riêng (cine-lab Q28 c; Tập 1 0 % · v3k 52 % · Tập 5 40 % → chỉ báo, đích Tập 6 ≥ 80 %).
- **Bỏ (xếp sai):** chấm mù khung, xem liền mạch mù — người đọc headless xếp Tập 1 trên Tập 5 / coi chuyển chế độ D-010 là "đổi phong cách"; tông màu theo hồi (cine-lab Q30) — Tập 1 đổi tông nhiều hơn Tập 5. Gu hình đo bằng L3.
- Bên dựng thêm cờ `change: major|minor` cho mốc vật thể ở beat và `anchor: true` cho số neo để thước nhịp đo được "đổi mang nghĩa" (hiệu chuẩn lại sau Tập 6).

## 3. Đầu bài WRITER (C2)

WRITER **đọc `playbook/story.md` trước tiên**, rồi theo các luật sau:
1. **Từ khó ASR:**
   - không dải năm có gạch nối; không "minus", không số âm đọc lên; không ký hiệu ở chỗ phải đọc;
   - số tiền đọc rõ;
   - viết tắt có gạch nối ("T-bill") → dạng đầy đủ ở câu mang từ khoá (lessons E6, F7).
2. **Claim-risk áp cho câu NÊU số;** câu nhắc lại gọi bằng lời. Mỗi tỉ lệ một dạng cố định (E5). **Ràng buộc claim-risk đặt sau móc** (story §1.3).
3. Câu đối trọng sau mỗi kết luận; không mệnh lệnh (E4).
4. Mật độ số và khoảng thở theo story §3; khuôn tỉ lệ thời lượng theo `format` (story §4, Tham khảo).
5. Đoạn phương pháp = 1 câu + thẻ V7 + mô tả.
6. **Bảng nhịp** có cột loại nhịp (1 "hình tự mang ý" + câu "ý người xem phải đọc ra" / 2 "minh hoạ lời"). Hình lấy từ thư viện; ký hiệu mới phải ghi lý do.
7. Gen được bảo vệ và gu đã chốt (CHARTER §4, `taste-ledger.md`). Không chép kịch bản tập cũ.
8. **Mỗi lần sửa kịch bản giao một agent WRITER MỚI với đầu bài ngắn** (file cần sửa + danh sách dòng cần đổi + lý do), **không gọi lại agent cũ**: gọi lại tốn bằng toàn bộ ngữ cảnh của agent đó (Tập 4: 3 lượt WRITER ≈ 0,56 triệu token; lessons G2).
9. **Điều kiện móc — TỰ ĐỘNG ở C2, đo trước G1** (lessons H4; Tập 4: móc kết thúc 8,1 s, câu hỏi người xem 1:34, AI hook 2/5). WRITER gắn vai mỗi câu trong 60 s đầu (`hook`/`promise`/`question`/`constraint`/`define`). Mốc thời gian lấy từ timeline nhà máy hoặc ASR table read của **bản đọc thử trước G1**:
   - **M1** câu móc kết thúc ≤ 5,0 s;
   - **M2** lời hứa kết thúc ≤ 30 s;
   - **M3** câu hỏi của người xem ≤ 30 s (được trùng M1);
   - **M4** 0:00–1:00 không khối `constraint`/`define` liền > 10 s (phần thừa lên nhãn hình, thẻ V7, mô tả);
   - **M5** nhân vật hoặc cái được–mất quay lại ≤ 0:45;
   - **M6** (từ Tập 6, `story.md` §2b.2) mọi lời hứa về nhân vật (vd "three buyers who got very different answers") được trả — nhân vật có tên và xuất hiện — **≤ 90 s** sau câu hứa; không trả được thì không hứa. Đo cả tập, không chỉ 60 s đầu; WRITER gắn vai `promise_character` cho câu hứa.
   Trượt → WRITER mới sửa (≤ 2 vòng), vẫn trượt → nêu ở G1. G1 báo 6 mốc thành một dòng.

10. **Năm luật nhân vật (`story.md` §2b, từ Tập 6):** một nhân vật dẫn đường từ cold open đến kết (trước 0:45, đi qua phần phương pháp, câu kết là câu của người đó); lời hứa nhân vật trả ≤ 90 s (M6); cái được–mất bằng vật cụ thể khi không được nêu số tiền ("23 more bills"); câu ở đỉnh cảm xúc ≤ 15 từ, một ý một câu; kết quay về câu hỏi của nhân vật. WRITER ghi trong bảng nhịp: tên nhân vật dẫn đường, câu đỉnh cảm xúc (số từ), câu kết.

**Móc do máy chọn (D-006 Q4):**
- WRITER viết **3 phương án 30 s đầu**, mỗi phương án một kiểu móc khác nhau (`packaging.md` §2). Cả ba đều theo story §1: 5 s đầu là được–mất hoặc câu hỏi trên sự thật hiện tại; lời hứa trước 0:30.
- **So cặp móc — ỨNG VIÊN, đã hiệu chuẩn chính thức (P1 Tập 4, `episodes/ep004/cal-hook/`, lessons G1):** chọn bản gốc 7/8, mỗi mẫu ≥ 3/4, mỗi vị trí ≥ 3/4 — **đạt đúng bằng ngưỡng** ở cả ba điều kiện; mẫu mới (Tập 1 + kịch bản mới), thứ tự X/Y cân bằng. **Mới chứng minh phân biệt "có móc / bỏ móc"**, chưa chứng minh chọn đúng giữa ba móc đều tốt (Tập 4: người đọc chọn vị trí Y 7/9 ở vòng tròn). Cách dùng (chủ dự án, G1 Tập 4):
  - **từ Tập 5:** REVIEWER chấm 3 phương án theo story §1 + điều kiện M1–M6 (§3.9); so cặp vòng tròn (headless, 3 lượt mỗi cặp, thứ tự xoay, báo lệch vị trí) **chỉ khi REVIEWER không tách được** (Tập 4: 9 người đọc, 0,29 triệu, H1/H2 không phân biệt);
  - **kèm WRITER + REVIEWER**: REVIEWER chấm 3 phương án theo story §1 (lý do một dòng); khi so cặp và REVIEWER lệch nhau, hoặc khi thắng thua chỉ do bản đứng cùng một vị trí, G1 nêu cả hai;
  - mỗi lần dùng ghi kết quả + lệch vị trí vào ledger; hiệu chuẩn lại khi đổi model người đọc. Thước đo thật vẫn là giữ chân YouTube.
- G1 hiện móc đã chọn dạng chữ trong kịch bản + 2 phương án còn lại, mỗi phương án một dòng. Chủ dự án chỉ đổi khi muốn. **Không sinh giọng cho phương án không chọn.**

## 4. Song song sau C2
- Phiên K (§7).
- Phối nhạc style C, đo độ lặp T2 (Tham khảo).
- Lời theo cảnh: tên take theo hash chữ; kiểm từ khoá ASR ngay khi sinh; chỉ sinh lại cảnh đổi chữ.

## 5. Gói phát hành và Shorts (G2)
- **Tiêu đề:** nháp ở G1 (so cặp một vòng, Tham khảo).
- **Thumbnail:** ở G2 chỉ đưa 3 thumbnail đã qua claim-risk; **không so cặp** (Tập 3–4: người đọc chọn trùng chủ dự án 2/2, lessons H2). Chủ dự án chọn mặc định + thứ tự Test & Compare; T&C là số đo thật.
- **Thumbnail bằng hình thế giới 3D (tổng kết Tập 5 §3.9, từ Tập 6):** thumbnail = **một khung tĩnh của thế giới** (nhà, người không mặt, chồng tiền) render bằng chính `build_seg.py` ở 1280×720 từ cảnh đã duyệt C3, cộng **tối đa 3–4 từ lớn**; bỏ chữ + cột 2D (`design/g2/thumbs.js` cũ). Ba phương án mỗi tập: (1) cảnh thế giới + 3 từ; (2) cảnh thế giới + 1 số "on paper"; (3) kiểu Tập 5 thumb-3 (chữ + cột 2D) làm **đối chứng trong Test & Compare ít nhất 2 tập**. Claim-risk áp như mọi khung (ILLUSTRATIVE, "on paper", không nêu số tiền phí khi tập cấm). Kiểm đọc được ở 168×94 px trước G2.
- **Không tóm tắt AI ở G2** (0/3 lần đổi quyết định); sức kéo của móc đo ở C2 (§3.9).
- **Shorts 2–3 cái 9:16 mỗi tập**, cắt từ nhịp then chốt đã qua checks:
  - ≤ 60 s;
  - chữ ≥ sàn dọc 56 px ở 1080×1920;
  - vùng an toàn dọc (trên 200 px, dưới 320 px);
  - ILLUSTRATIVE và "history, not a forecast" trên mọi khung có số.
  Dựng bằng thư viện mẫu khi phiên nhà máy xong (`moc-b/PLAN-FACTORY.md`). Trước đó cắt tay từ bản cuối.
- **Hướng dẫn đăng:** `episodes/epNNN/HUONG-DAN-DANG.md` theo mẫu `playbook/templates/HUONG-DAN-DANG.md`.

## 5b. Âm: nhạc hiệu, cue theo hồi, lặng trước số neo (tổng kết Tập 5 §3.4, từ Tập 6)
- **Nhạc hiệu kênh:** 3 s ở ident (`IDENT_S = 3`) và **một khúc đóng khác**; nhạc bằng mã (D-010 §5), dựng một lần cho cả kênh. Gu nhạc là quyền chủ dự án (CHARTER §6): **chủ dự án duyệt nhạc hiệu bằng clip có âm ở C3 Tập 6** (một lần cho cả kênh), sau đó dùng lại mọi tập.
- **Mỗi hồi một cue riêng, không lặp vòng:** nhạc vẫn theo bản đồ căng (F-3 Tập 5: dâng ở phần phát lại, chốt hợp âm đúng từ khoá), thêm ràng buộc cue khác nhau giữa các hồi và không lặp vòng trong hồi.
- **Lặng 0,7–0,9 s trước mỗi số neo** (≤ 3 số neo/tập, §3.2.4 của tổng kết; beat khai `anchor: true` trong spine). Tiếng hiệu ứng "land" đè đúng từ khoá số neo phải bỏ (F-2: sfx chỉ thấp hơn lời 11 dB).
- **Không tăng mật độ sfx** khi thêm cue (F-2 cảnh báo đoạn a Tập 5: 21,7 sự kiện/phút, 8 trong 10 s). Lặng trước số làm tập dài ≈ 2–3 s — tính vào ước độ dài.

## 6. Giao hàng
- Lệnh: `python3 toolkit/deliver/deliver.py episodes/epNNN/out/video.mp4 --out episodes/epNNN/work/delivery --name epNNN --branch epNNN-delivery --push`
- Mã hoá: 1080p 8 Mb/s (24–30 fps), audio copy; phần 90 MB, `SHA256SUMS`, `JOIN.md`. Không gửi qua chat.
- Chủ dự án tải xong thì xoá nhánh (proxy chặn xoá → việc treo cho chủ dự án).
- **Git LFS trên nhánh `release-epNNN`: chưa thử** (chuyển sang phiên nhà máy). Phải kiểm hạn mức LFS của tài khoản trước; vượt thì giữ cách phần 90 MB.

## 7. Phiên K và hàng chờ luật
- K chạy **một lần mỗi tập**, ngay khi claim C2 chốt. Tên `model.kind`/params do K quyết.
- Mọi đề xuất đổi luật (của bên dựng, tổng kết, REVIEWER) ghi vào **`checks-appeal.md`**. K xử lý theo lô ở lần chạy của tập kế tiếp. Chỉ mở phiên K riêng khi cần **kind mới**.
- Checks khi dựng: chỉ luật liên quan cảnh vừa sửa. Đủ bộ hai lần: cuối C4 và ở C5, trên bản sao khoá có server riêng (`episodes/ep003/design/c5/checks.sh` là mẫu).

## 8. KPI và trần token

| KPI | Tập 2 | Tập 3 | Đích Tập 4 |
|---|---|---|---|
| Chủ dự án tham gia | 11 cổng + giao hàng | 3 cổng + xác nhận tải | **2 cổng (G1, G2) + G3 đăng**; +1 nếu cần C3 |
| Vòng mỗi cổng | C2 3 · C3 ~6 · C4 3 | C2 1 · C3 2 · C4 1 · C5 2 | TỰ ĐỘNG ≤ 2; từ Tập 5 lỗi CHÍNH cũng sửa (D-009) |
| Số agent | ≈ 300 | 141 | **≤ 60** |
| Ký tự ElevenLabs | 9.436 | 5.551 | ≤ 6.000 (gồm Shorts: dùng lại lời tập) |
| Thời gian P1 → G2 | 3 ngày | ~1,5 ngày | ≤ 1 ngày làm máy |
| Token | không đọc được | ≈ 6 triệu (ước theo 141 × 44 nghìn) | **trần 3 triệu** (3,5 khi có P2) |

**Thực Tập 4:** ≈ 6,3 triệu, 102 agent, EL 11.702, chủ dự án 5 lượt (+G3); kiểm mù 49 % (lessons H1).

**Trần token (từ Tập 6, tổng kết Tập 5 §3.6, chủ dự án duyệt 08/10):** **trần = đầu vào mới (input + ghi cache) + sinh ra**, đọc từ **log phiên** (sự kiện `result` của transcript: `usage` của lượt, `modelUsage` tích luỹ cả phiên gồm agent con); đọc cache báo riêng. Số công cụ báo cho mỗi agent con (ledger) là cỡ ngữ cảnh cuối, **không phải** đầu vào mới (Tập 5 ước ≈ 10 triệu, log 85,4) — ledger chỉ giữ nó để phân loại việc.

**Mức cảnh báo Tập 6 = 15 triệu (chỉ cảnh báo, D-009 c):** vượt thì báo số thực trong gói; **không cắt bước chất lượng** (kiểm mù đủ người đọc, lượt đạo diễn, REVIEWER). Ước khi áp §1 "Agent dựng không chờ" và D-011 (mỗi chặng một phiên):

| Loại việc | Mức cảnh báo (triệu, trần log) | Tập 5 thực |
|---|---|---|
| Dựng (agent dựng, nhà máy, vòng sửa) | ≈ 10 | 72,25 |
| Điều phối (luồng chính các phiên) | ≈ 2,5 | 8,71 |
| Kiểm mù (headless, cộng từ JSON đầu ra) | ≈ 1,5 | ≤ 2,31 |
| Khác (WRITER, REVIEWER, Việc 0, kiểm độc lập, phiên K) | ≈ 1 | 2,12 |
| **Cộng** | **15** | **≈ 85,4** |

≤ 40 agent con. EL ≤ 6.000 ký tự (gần với chi tiêu: vượt → hỏi chủ dự án). Hai trần này **không đổi**. Ledger ghi cột **loại việc** cho mỗi dòng.

**Mỗi phiên khi đóng ghi 4 số đọc từ log vào PLAN tập mục 5:** sinh ra · đầu vào mới · đọc cache · trần. Cách lấy: `list_events(session_id=<phiên này>, kinds=["result"], limit=100)` → lưu trang JSON → `python3 toolkit/usage/from_events.py --session <id> --close trang*.json`. Sự kiện `result` chỉ có khi một lượt kết thúc → số ghi được là **đến lượt trước**; lượt đóng cộng vào ở phiên sau (ghi "đến <giờ>"). Headless không nằm trong log phiên: cộng bốn trường `tokens` của JSON đầu ra (`toolkit/blind/headless.sh`). Bảng cả tập: `python3 toolkit/usage/token_log.py <jsonl…> [--windows …]`. Ghi thêm **giờ render thực** (`build-report.json`, `<đoạn>.build.json`).

<details><summary>Mức cảnh báo Tập 5 (cũ, 3,0 triệu theo số công cụ báo — thực đo bằng log 85,4)</summary>

Kiểm mù 0,6 · dựng 0,75 · WRITER 0,4 · REVIEWER 0,45 · checks 0,15 · điều phối 0,5 · dự phòng 0,15 (`tongket-t4/REPORT.md` §7). So với log: `tongket-t5/REPORT.md` §1b.
</details>

## 9. Định dạng tập (`episode.yaml` → `format`)
| `format` | Thời lượng | Cấu trúc | Mid-roll |
|---|---|---|---|
| `lab` | 9–11 phút | móc → bối cảnh/nhân vật → hành trình (phép thử) → đáp án + ngưỡng → giới hạn | 2, ở ranh giới hồi |
| `101` | 8–9 phút | khái niệm → thí nghiệm nhỏ trên dữ liệu thật → khác nhau ở 2–3 người → giới hạn | 1, ở ranh giới hồi, trong khoảng lặng |

- **Luật chung:** mid-roll không đặt trong 2 phút đầu hay 2 phút cuối, luôn ở khoảng lặng ≥ 1 s.
- **`101` không độn nội dung:** thiếu chất thì ngắn hơn hoặc gộp khái niệm. Thời lượng tối thiểu là mềm; tối đa là cứng.
- Khuôn đã thiết kế, **chưa dựng tập 101**. Kiểm khuôn tự động nằm trong `build.sh` (phiên nhà máy).

## 10. Sau phát hành
Ở mốc 7 ngày: `episodes/epNNN/audience.md` theo mẫu `playbook/templates/audience.md`. Chủ dự án gửi **một** ảnh chụp YouTube Studio cho chat chiến lược. Điểm rời lớn nhất → nhịp kịch bản tương ứng → `lessons.md` / `story.md`.

## 11. Công cụ
| Việc | Lệnh |
|---|---|
| Mở phiên | `bash toolkit/verify.sh <nhánh>` |
| Dải kiểm mù | `python3 toolkit/blind/strips.py VIDEO SPANS.json OUTDIR` |
| Chia mẫu, gói chấm, gộp điểm, dừng sớm | `python3 toolkit/blind/packets.py deal / packet / tally / next` (như v2) |
| Giao hàng | `python3 toolkit/deliver/deliver.py …` (§6) |
| Test công cụ | `python3 -m unittest discover -s toolkit/tests` |
| Dựng một lệnh | `bash toolkit/build.sh episodes/epNNN/episode.yaml` (`toolkit/factory/README.md`) |
| Đoạn thế giới 3D | `python3 toolkit/factory/world/build_seg.py <thư mục đoạn> --res 540\|1080` |
| Số nói mỗi cảnh | `python3 toolkit/factory/numbers_said.py episodes/epNNN/story/script.md` |
