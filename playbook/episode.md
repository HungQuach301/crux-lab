# Sổ tay chạy một tập (playbook v5, D-013, 13/10/2026)

Áp từ Tập 4 (`decisions/D-006.md`); v4 áp D-009 (chất lượng là ưu tiên tuyệt đối) và D-010 (thế giới 3D, 8 quy tắc hình–âm) từ Tập 5; **v5 áp D-013 (mô hình xưởng 6 mốc, tổng kết Tập 7) từ Tập 8, ở ranh giới sau G1 Tập 8**. Khung: `playbook/quality-framework.md`. Biên kịch: `playbook/story.md`. Một tập chạy bằng **một prompt mẫu**: `playbook/prompts/CHAY-TAP-N.md` ("Chạy Tập N." + câu trả lời cổng nếu có); mỗi chặng tới cổng kế là một phiên ngắn.

## 0. Mở phiên
`bash toolkit/verify.sh <nhánh-lệnh-ghi>`: kiểm công cụ, nhánh đúng lệnh (không tự đặt nhánh), `main` mới nhất. Trượt thì báo, không làm tiếp.

## 1. Sáu mốc, ba cổng, thẻ vai (D-013; thay "ba cổng, mỗi chặng một phiên" D-011)

**Nguyên tắc (chủ dự án 13/10):** chất lượng chỉ tăng; nâng từ tiền kỳ; kiểm–sửa có điểm dừng. Nâng cấp mới thử trên tập cũ trước, chỉ vào tập đang chạy ở ranh giới cổng.

| Mốc | Việc (vai) | Đầu ra | Cổng / dừng | Chủ dự án |
|---|---|---|---|---|
| **M1 Phát triển** | Việc 0 (dữ liệu, mô hình, kiểm độc lập) · C1 · C2 (WRITER, kiểm mù lời; `story.md` §1–§1c) · giao phiên K | kịch bản, bảng nhịp, chương, `numbers.md` | M1–M8 (`templates/check_script.py`), kiểm mù lời; ≤ 2 vòng | — |
| **M2 Tiền kỳ** | bản tầm nhìn (Đạo diễn sáng tạo) · bảng vật thể (Thiết kế hình) · animatic 540p xám (Previz) · bản đồ liền mạch (Giám sát liền mạch) · ngân sách (Line producer) · footage: dòng RIGHTS **trước khi** tải (`RIGHTS.md` §F) | `preprod/TAM-NHIN.md`, `preprod/BAN-DO-LIEN-MACH.md`, `preprod/animatic.mp4`, clip 3 s mỗi vật thể | nhận dạng mù + cổng gốc trên animatic; ≤ 2 vòng mỗi lỗi; REVIEWER gói G1 | **G1**: kịch bản + vật thể/animatic + tiêu đề nháp (≤ 3 câu, `templates/G1.md`). **C3 gộp vào đây** |
| **M3 Sản xuất nháp 540p** | nhà máy dựng thế giới, giọng (sinh một lần), nhạc bằng mã, SFX ghi âm thật, footage | nháp 540p theo cảnh | verify đoạn, đồng bộ ±0,2 s | — |
| **M4 Hậu kỳ** | Editor: J/L-cut, nhịp, lặng · màu theo hồi · mix | nháp 540p cả tập | nhịp trên nháp | — |
| **M5 Kiểm định trên nháp** | REVIEWER ý đồ (trước) · **checks đủ bộ, gồm bộ lấy mẫu trang** · cổng gốc · nhớ lại (Đạo diễn sáng tạo) · liền mạch (Giám sát) · lượt đạo diễn (chẩn đoán) · REVIEWER gói G2 | gói G2 + nháp 540p + 3 khung tĩnh 1080p của cảnh đinh | **≤ 2 vòng mỗi lỗi** (dưới) | **G2**: phiếu L3 trên nháp (`templates/L3.md`) |
| **M6 Giao** | **1080p một lần** + **1 Short** · L1 kỹ thuật trên 1080p (độ phân giải, loudness, C14, SSIM so nháp ≥ 0,97) · gói chữ (tiêu đề G1, mô tả, chương, tag) + **3 ảnh bìa** (D-015, §5) · giao hàng · merge `main` squash | master, Short, `HUONG-DAN-DANG.md` | lệch kỹ thuật thì sửa, không mở lại G2 | **G3** đăng |

- **Chủ dự án chạm G1, G2, G3** (+ lệnh "Chạy Tập N"). Ngoài cổng chỉ hỏi khi gặp ngoại lệ CHARTER §5. Mỗi lượt chạm ghi vào PLAN tập §5 kèm phút ước.
- **Mỗi chặng một phiên ngắn** (M1–M2 → G1; M3–M5 → G2; M6 → G3). Đóng chặng: PLAN tập ≤ 1 trang theo `templates/PLAN-tap.md` (mục 1 = mốc kế), commit, push, dừng. Phiên kế mở bằng "Chạy Tập N" — không viết prompt riêng. Tệp lớn ngoài git còn ở container thì chạy tiếp trong phiên đó sau `/compact` (sửa D-011, T6-3); không thì dựng lại theo `episode.yaml`.
- **Tập 8 (chuyển đổi):** P1 Tập 8 chạy theo mẫu cũ tới G1 — kiểm kịch bản bằng `check_script.py` bản `c7358285` (M2/M3 30 s, không M7/M8; kịch bản cũ không có vai `fact` nên M7 bản mới luôn trượt); công thức mở đầu D-013 áp từ kịch bản Tập 9 hoặc khi WRITER Tập 8 viết lại sau G1; sau G1 làm M2 (tiền kỳ) rồi M3–M6. G1 Tập 8 đã ghi "cần C3" thì kiểm tiền kỳ thay đúng chỗ C3 (không thêm chạm); không thì thêm 1 lượt chạm, chỉ ở Tập 8.

### 1a. Thẻ vai — vai là một đầu bài (một lượt headless khoá Console hoặc lệnh máy, 0 agent con), không phải agent sống. Vai không có phép thử riêng thì không thêm.
| Vai | Đầu vào | Đầu ra | Phép thử riêng (ai đo) | Quyền / không được |
|---|---|---|---|---|
| **Đạo diễn sáng tạo** | logline, kịch bản, hồ sơ cầu, sổ gu | `TAM-NHIN.md` (câu hỏi của phim, 3 khoảnh khắc, màu lựa chọn/hồi, số neo + vật thể, chương, kết, footage) | **nhớ lại** trên nháp 540p (3 người headless, dải khung + lời): ≥ 2/3 người kể được ≥ 2/3 khoảnh khắc và đúng câu hỏi của phim — **chỉ báo cho tới khi hiệu chuẩn** (Tập 6/7, đối chứng âm Tập 1) | chọn trong phạm vi bản tầm nhìn đã duyệt ở G1; **không** đổi kịch bản, gu, nhạc |
| **Thiết kế hình** | bản tầm nhìn, `toolkit/visual-library/`, gen CHARTER §4 | bảng vật thể: ảnh 3 góc + clip 3 s ở trạng thái đổi; RIGHTS cho tài sản ngoài | **nhận dạng mù**: 2 người headless xem clip 3 s tắt tiếng, gọi đúng vật thể **và ý** (chiều đổi) ≥ 2/2; máy kiểm bảng màu kênh, không mặt, low-poly | thêm vật thể vào thư viện sau G1; **không** dùng vật thể trượt nhận dạng 2 vòng |
| **Previz** | kịch bản, bảng nhịp, bảng vật thể, timeline bản đọc thử | animatic 540p xám (khối, máy quay, thời điểm theo lời thật) | **cổng gốc tắt tiếng trên animatic** (`quality-framework.md` §4.7), đọc theo biên nhiễu A32 (chưa khoá: dùng tạm "≥ 2 lượt đọc lại đồng ý") | đổi bố cục, máy quay; **không** đổi lời |
| **Editor** | nháp 540p theo cảnh, stem, bản đồ liền mạch | danh sách cắt: J/L-cut ở chuyển hồi, nhịp, lặng, mid-roll | **nhịp trên nháp**: quãng có lời không đổi hình > 8 s = 0; freezedetect ≥ 3 s có lời ≤ 30 s/tập; kiểm mù "chỗ muốn tua": không đoạn nào ≥ 2/3 | đổi thứ tự shot trong cảnh, độ dài lặng; **không** đổi lời |
| **Giám sát liền mạch** | bản tầm nhìn, kịch bản, `numbers.md`, nháp | `BAN-DO-LIEN-MACH.md` → `map:`; báo cáo lệch | **máy đối chiếu nháp với bản đồ**: số neo/danh từ chính có vật thể ±1 s; chuyển hồi đúng kiểu khai; màu hồi và màu lựa chọn đúng; số trên hình = lời; footage có năm + nguồn (A41b, A39 — trước khi khoá: đối chiếu tay) | báo lệch cho vai sở hữu; **không** tự sửa hình |
| **Line producer** | trần theo format, ledger, `build-report.json`, log phiên | sổ chi theo mốc (PLAN tập §5) | **sổ chi khớp nguồn** ±2 % (`total_cost_usd`, `from_events.py`, `build-report.json`). Kèm luật ngắt: một mốc vượt 150 % ngân sách mốc → dừng mốc, báo trong gói; 1080p chạy lần 2 phải có lý do ghi trước | ngắt và báo; **không** quyết chi tiêu mới, **không** cắt bước chất lượng |
| WRITER | hồ sơ cầu, `story.md` | kịch bản, bảng nhịp, chương, 3 phương án mở | kiểm mù lời + M1–M8 | như cũ (§3) |
| K | `checks-appeal.md` | luật khoá + LOCK | selftest; 0 lệch tập cũ; luật CHẶN mới cần đối chứng dương thật (A40, D-013) | như cũ (§7) |
| Nhà máy | spine, thế giới, lời | nháp 540p, 1080p, Short | verify đoạn, đồng bộ, trùng byte so cache | như cũ |

- **REVIEWER** (headless) chỉ ở gói G1, ý đồ kiểm định trước M5, gói G2 — không ở bước trung gian (D-013).
- **Lượt đạo diễn máy là chẩn đoán** (D-010 §6). Lời phê chỉ thành việc sửa khi phép thử của vai sở hữu (Editor/Previz) **cũng trượt** ở đúng chỗ đó (tổng kết Tập 7: vòng sửa C5 theo lời phê trên bản cuối, cổng gốc đo 16/21 → 5–7/21).

### 1b'. Vòng sửa — ≤ 2 vòng mỗi lỗi (D-013; thay 3 vòng, lessons V1)
- Một lỗi ở một cảnh sửa tối đa **2 vòng**; hết 2 vòng → gói nêu **bản trước/sau** kèm số đo để chủ dự án chọn (D-009 E3).
- **Khoá nghĩa (V2):** một vòng chỉ được giữ khi điểm vượt bản tốt nhất **ngoài biên nhiễu** (A32; chưa khoá → "≥ 2 lượt đọc lại đồng ý"); có câu khuyên → tự loại, sửa tiếp từ bản tốt nhất.
- **Vòng 2 đổi loại hình (T6-7):** vòng 1 trượt với cùng câu trả lời người đọc → vòng 2 phải đổi loại hình (đếm → hàng có số thứ tự; vùng → vật thể riêng) hoặc hạ "ý cần đọc ra" về mức hình nói được (ghi `beats.md` trước khi chạy, nêu trong gói). Việc đổi loại hình làm ở **Previz trên animatic**, không trên bản dựng.
- Nhãn đè đúng vùng cần đọc (V11.plateOverGraphics > 0) → sửa trước vòng tiếp.
- **Duyệt theo lô:** G1 lô vẫn duyệt 3–4 đề tài + logline cho cả mùa (`topics/season.md`); G1 của tập sau chỉ còn kịch bản + tiền kỳ. Máy không tự chọn đề tài (D-004).

- **Giọng, nhạc, hướng hình** dùng mặc định đã chốt (Eric `eleven_v3`; nhạc bằng mã theo bản đồ căng, biên độ rộng; hướng hình "một thế giới, hai chế độ máy quay" D-010 + thư viện hình). Muốn đổi thì chủ dự án nêu ở G1.
- **Chất lượng trước (D-009):** lỗi CHÍNH **sửa trước phát hành** (ngoại lệ: sửa làm hỏng yếu tố chất lượng khác → gói nêu, kèm số đo/bản trước-sau, chủ dự án chọn). Cổng gốc trượt nghĩa → **sửa bằng hình trước**, nhãn là cách cuối. Token chỉ cảnh báo (§8). **Ngoại lệ phải hỏi:**
  - đổi kịch bản đã duyệt;
  - số không xác minh được nguồn;
  - rủi ro pháp lý/bản quyền;
  - chi tiêu mới (CHARTER §6).
- Mỗi tập một nhánh `epNNN` từ `main`. Chỉ phiên chặng M6 (sau G2) merge `main` squash (fetch trước; trong file dùng chung chỉ sửa phần của tập).
- **Bàn giao qua `episodes/epNNN/PLAN.md` ≤ 1 trang** theo `playbook/templates/PLAN-tap.md` (D-013): 1 mốc hiện tại · 2 việc tiếp (≤ 3) + việc treo · 3 quyết định đã có (trỏ `gates/*-answer.md`) · 4 đã sửa gì, vì sao · 5 sổ chi theo mốc (token 4 số + đọc cache + lượt + $ + giờ máy + EL + lượt chạm và phút chủ dự án) · 6 **phiên sau đọc ≤ 8 tệp** · 7 mở chặng kế bằng `prompts/CHAY-TAP-N.md`. Lịch sử → `episodes/epNNN/archive/PLAN-history.md`. `PLAN.md` gốc repo là **PLAN kênh** ≤ 1 trang — phiên M6 cập nhật khi merge.
  Phiên sau chỉ đọc các tệp ở mục 6 của PLAN tập.
- **Lượt đạo diễn (bắt buộc, chẩn đoán — D-009 E5, D-010 §6):** ở M5, mỗi đoạn có hình mới qua một lượt đạo diễn trên nháp 540p (`quality-framework.md` §10): 4 trục + lời phê theo mốc giây. Lời phê là việc nên xem, không phải ngưỡng; chỉ thành việc sửa khi phép thử của vai sở hữu cũng trượt ở đó (§1a); không mở vòng sửa thẩm mỹ chỉ vì điểm máy. Thước đo cuối là phiếu L3 ở G2 (≥ 4 mọi dòng).
- **Đoạn thế giới 3D:** khai `world:` trong `episode.yaml`; dựng và kiểm bằng `toolkit/factory/world/build_seg.py`. **Ghép vào master** bằng bước `splice` của nhà máy (BACKLOG F-5 xong 07/10, `toolkit/factory/world/splice.py`, test `test_world_splice.py`): hình thay khung các cảnh đoạn chiếm, tiếng đoạn vào stem tập, loudnorm chung; `spec.py` chặn cảnh không liên tiếp hoặc một cảnh nằm trong hai đoạn. Đoạn dựng (lint → spine → render theo cảnh có cache → âm → verify quy tắc 1/2/3/7); đồng bộ ±0,2 s bằng `sync_audit.py`; C14 trên bản 1080p.
- **Lớp ánh sáng điện ảnh `cine` (F-17; chủ dự án 15/10):** opt-in, TẮT mặc định (không khai = trùng byte, T1). Chỉ dùng cho **cảnh đinh ≤ 30 % thời lượng tập** (khai trong spine của đoạn; ghi tỉ lệ vào PLAN tập). **Lần dùng đầu (Tập 9): M5 chạy checks đủ bộ trên bản 1080p có lớp để đo V12** trước G2. Lệch đã biết: T6 viền phía xa đèn 12 % phía gần (> 10 %), chấp nhận. Chi tiết: `toolkit/factory/README.md` (F-17), `toolkit/factory/f17/REPORT.md`.
- **Sửa nhà máy gom đầu tập (tổng kết Tập 5 §3.8):** việc nhà máy làm trên nhánh `factory-*` trước G1 hoặc sau G1 trước M3, merge `main` rồi mới dùng; thử trên tập cũ trước (D-013). Giữa tập (M3 → G2) chỉ sửa lỗi **chặn = CHẶN + CHÍNH** của tập đang làm; cải tiến khác ghi `toolkit/factory/BACKLOG.md`.
- **Số nói (B+2):** ≤ 2 số **mới** được nói mỗi cảnh (`toolkit/factory/numbers_said.py`, BLOCK trong `spec.py`); số thứ ba trở đi lên nhãn trên hình (người biên tập chọn), phạm vi không đổi.
- **Giọng theo cảnh (B+1):** `voice_overrides: {Sxx: {seed | settings | voice | model | take}}` trong `episode.yaml` khi một cảnh cần take khác (vd Tập 5 S18 seed 1006).
- **REVIEWER** (headless, `quality-framework.md` §7) soát gói G1, ý đồ kiểm định trước M5 và gói G2 (D-013); không soát bước trung gian.
- **Agent dựng không chờ** (tổng kết Tập 5 §1e.1) — chỉ áp khi buộc dùng agent con (cách chuẩn là headless, §2): khởi chạy build/checks bằng công cụ chạy nền rồi trả việc ngay; một vòng sửa = một lượt mới, đầu bài chép PLAN tập mục 4. Chi tiết: `archive/prompts-v4/` và lessons T5.

## 1b. Dữ liệu thị trường trong quy trình (Phiên Thị trường `market-r1`, chủ dự án duyệt hướng 10–11/10) — KHÔNG thêm cổng, phiên hay lượt chạm
Nguồn: `market/` (`CHANNELS.md`, `topics/<đề tài>.md` = hồ sơ cầu, `REPORT.md`, `teardowns/`), công cụ `toolkit/market/` (README ở đầu mỗi tệp). Số liệu thô YouTube **chỉ** ở `~/market-cache/<ngày>/` ngoài git (YouTube API Developer Policies III.E.4); repo nhận nhãn (cao/vừa/thấp) và kết luận định tính; chỉ số tự tính ghi "tự tính, không phải chỉ số YouTube". Mọi bước dưới là việc máy trong chặng sẵn có; thiếu dữ liệu thì ghi "chưa có" và làm tiếp, không hỏi.
1. **P1 Việc 0:** hồ sơ cầu của đề tài (và 2–3 đề tài kế trong `topics/season.md` / hàng đợi) có dòng "Làm mới:" cũ hơn 30 ngày → `python3 toolkit/market/purge.py` rồi làm mới: `discover.py search --topics <id…>` (≤ 3 search/đề tài; hạn mức 10.000 đơn vị/ngày, ≤ 100 search) → `pull.py` cho kênh trong `market/CHANNELS.md` → `analyze.py tag outliers comments gap profile` → `report.py topics`. Đồng thời **quét video mới nổi** (30 ngày) của các đề tài đó; video vượt trội mới vào mục "Video đối thủ theo tập" của hồ sơ.
2. **C1:** logline **trả lời câu hỏi trọng số cao nhất** của hồ sơ cầu (câu 1 mục "Câu hỏi khán giả"); kiểm mù kể lại giữ nguyên.
3. **C2 (WRITER):** §3 mục 11. **REVIEWER:** `quality-framework.md` §7 mục 10 (trả lời ≥ 3/5 câu hỏi).
4. **Kiểm mù lời C2:** vai người đọc = **người hỏi** câu hỏi trọng số cao nhất, nhập vai từ một hoàn cảnh điển hình của hồ sơ (thay vai khán giả chung; câu hỏi cố định giữ nguyên, thêm một câu: *"Did the video answer the question you came with? Which part?"*). Ghi vào ý đồ `gates/C2-intent.md` trước khi chạy như mọi ý đồ.
5. **G1:** gói thêm **1 dòng bắt buộc "người xem lõi gặp câu hỏi này lúc nào"** (khán giả lõi CHARTER §1: người Mỹ 25–40 tuổi đang thuê hoặc sắp mua nhà, bắt đầu đầu tư; đề tài vòng ngoài ghi rõ "vòng ngoài") + **1 dòng** "trả lời câu hỏi X, Y, Z (hồ sơ cầu)" + **3 video vượt trội cùng đề tài** (liên kết, kênh, nhãn ≥ 3× / ≥ 5×) — không thêm câu hỏi cho chủ dự án (`templates/G1.md`). **Từ Tập 7 (D-012):** thêm dòng **"neo: …; khác biệt: …"** (`python3 toolkit/market/anchors.py anchors --topic <id> --question "<câu hỏi khán giả, không nêu phương pháp>"`, P1 Việc 0) và **tiêu đề chốt ở G1** theo cổng tiêu đề tìm kiếm (D-015, §5).
6. **M6:** mô tả + chương + tag do máy viết, kiểm `package_check.py` (§5); 3 ảnh bìa + 1 đối chứng mã theo cổng G3 (D-015, §5).
7. **Sau phát hành:** vòng tự hiệu chỉnh nhãn cầu §10.

## 2. Model, effort, số agent

| Việc | Model | Effort |
|---|---|---|
| Điều phối, WRITER, REVIEWER, tổng kết | Opus | Medium |
| Người đọc kiểm mù, người chấm, so cặp | Sonnet **headless** (`toolkit/blind/headless.sh`, không agent con) | mặc định |
| Render, checks, mã hoá, sinh giọng | lệnh trực tiếp (không agent) | — |

**Khoá Console là cách chuẩn (tổng kết Tập 6 câu 1g, chủ dự án duyệt 11/10; lessons T6-9):** việc nặng — dựng, vòng sửa, WRITER, REVIEWER, kiểm mù — chạy **headless bằng khoá Console** (`bash toolkit/api.sh <build|review> <đầu-bài.md> <log.jsonl>`; kiểm mù: `headless.sh` với `ANTHROPIC_API_KEY="$CONSOLE_API_KEY"`), **0 agent con** trừ khi việc cần công cụ của phiên. **Trần chi/tập (cảnh báo, §8):** `101` $35 · `lab` $45 · `deep` $60; ghi chi thật (`total_cost_usd`) vào PLAN tập mục 5. Mục "Agent dựng không chờ" ở §1 chỉ còn áp khi buộc dùng agent con.

Mỗi agent con tốn **≈ 32–49 nghìn token cố định** (Mốc B, Tập 4). Một lượt đọc mù headless tốn **≈ 9–10 nghìn** (chữ) và **≈ 11 nghìn** (ảnh, `--read`) — `tongket-t4/REPORT.md` §2a. Ý đồ mỗi cổng ghi trước số lượt dự kiến. Dùng lệnh trực tiếp thay agent khi không cần độc lập.

**Kiểm mù (Tập 5, lessons H2–H3):**
- **C1:** 3 người đọc mỗi logline (2 T + 1 G), không đối chứng, không so cặp tiêu đề; dừng khi 2 sai.
- **C2:** 6 người đọc + 1 người chấm, ≤ 2 vòng; dừng khi gặp khuyên_tính đầu tiên (A9) hoặc 2 sai; không dừng sớm khi đạt.
- **Cổng gốc (M2 trên animatic, M5 trên nháp):** chỉ nhịp loại 1; 2 người đọc mỗi nhịp, người thứ 3 chỉ khi chia; người chấm độc lập.
- **Không chạy:** tóm tắt AI ở G2, so cặp thumbnail, đối chứng trong tập thường (chỉ khi rubric mới, việc lô K), hiệu chuẩn so cặp móc (đã xong).
- **Headless là cách kiểm mù chính** (tổng kết Tập 5 §2a, chủ dự án duyệt 08/10): C2 Tập 5 so song song 6 headless + 3 `Explore` — đạt/trượt trùng (6/6, 3/3, 0 khuyên); khối mất chú ý nhiều nhất khác cảnh nhưng **cùng loại** (khối phương pháp: S19 thẻ 4/6 vs S10.1 3/3); headless ≈ 1/4 giá, mù thật. **Không dùng `Explore` cho kiểm mù.**
- **Câu mất chú ý** hỏi ở mọi kiểm mù lời (C2). Ngưỡng so/sửa đọc theo **loại khối**, không theo cảnh: *phương pháp / định nghĩa / số dày / nhân vật*. Một loại khối được **≥ 2/6** người đọc nêu → WRITER mới sửa khối đó (như Tập 5 v2: S19 còn 1 câu → S18 3/6).
- **Một lượt người đọc model khác ở C2 mỗi 3 tập** (Tập 6, 9, 12…): thêm 1–2 người đọc headless Opus hoặc Haiku (`headless.sh --model`) trên cùng gói lời, cùng người chấm; giảm điểm mù chung của Sonnet (người đọc cùng model tương quan cao, lessons H3). Ghi kết quả so với 6 người Sonnet vào ledger; lệch đạt/trượt hoặc lệch loại khối → nêu ở G1.

## 2b. Thước chỉ báo chống tụt hình (tổng kết Tập 5 §3.2–3.3, từ Tập 6)
Chạy ở M2 (spine + animatic) và M5 (nháp), báo một bảng trong gói G2; **chỉ báo, không ngưỡng, không mở vòng sửa chỉ vì số** (CHARTER §4). Lệnh và trạng thái: `toolkit/indicators/README.md`; hiệu chuẩn 08/10 trên Tập 1 (đối chứng âm), Tập 4 v3k, Tập 5: `tongket-t5/indicators/CALIBRATION.md`.
- **Giữ:** nhịp trên spine (quãng có lời không cú máy/không vật đổi trạng thái > 8 s — **chưa hiệu chuẩn**, đối chứng dương 2/4); đa dạng khung nhìn theo máy quay (xếp đúng: Tập 1 cụm lớn nhất 58,5 %, Tập 5 6,8 %); mỗi vật thể đổi trạng thái có tiếng riêng (cine-lab Q28 c; Tập 1 0 % · v3k 52 % · Tập 5 40 % → chỉ báo; không đặt đích — nếu cần, chủ dự án quyết ở G1 Tập 6).
- **Bỏ (xếp sai):** chấm mù khung, xem liền mạch mù — người đọc headless xếp Tập 1 trên Tập 5 / coi chuyển chế độ D-010 là "đổi phong cách". Gu hình đo bằng L3.
- **Chưa đo đúng định nghĩa:** tông màu theo hồi (cine-lab Q30 = đúng tông đã khai cho từng hồi; Crux chưa khai màu hồi) — khai `map.color` là việc gu, chủ dự án quyết.
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
8b. **Phần dựng trước kết quả đầu ≤ 60 s** (Tập 9 trở đi, chủ dự án G3 Tập 8 15/10, lessons T8-2): từ hết cold open tới câu nói con số kết quả đầu tiên ≤ 60 s; định nghĩa/chi phí/giả định dồn sau kết quả đầu hoặc lên thẻ.
9. **Điều kiện mở — TỰ ĐỘNG ở C2, đo trước G1** (lessons H4; D-013: công thức `story.md` §1). WRITER gắn vai mỗi câu trong 60 s đầu (`hook`/`fact`/`question`/`promise`/`constraint`/`define`). Mốc thời gian lấy từ timeline nhà máy hoặc ASR table read của **bản đọc thử trước G1**:
   - **M1** câu móc (tin thời sự / nghịch lý ở 0:00) kết thúc ≤ 5,0 s;
   - **M7** ≥ 3 câu `fact` (sự thật lật kỳ vọng), câu thứ 3 kết thúc ≤ 35 s;
   - **M3** câu hỏi của người xem ≤ 40 s;
   - **M2** lời hứa đáp án dạng nghịch lý ≤ 50 s;
   - **M8** ≤ 1 câu `constraint` (miễn trừ ≤ 1 vế) trong 0:00–1:00 — phần còn lại lên hình;
   - **M4** 0:00–1:00 không khối `constraint`/`define` liền > 10 s;
   - **M5** nhân vật hoặc cái được–mất xuất hiện lần đầu ≤ 0:45;
   - **M6** (`story.md` §2b.2) mọi lời hứa về nhân vật được trả ≤ 90 s sau câu hứa; WRITER gắn vai `promise_character`.
   Trượt → WRITER mới sửa (≤ 2 vòng), vẫn trượt → nêu ở G1. G1 báo 8 mốc thành một dòng. **Chương** (`story.md` §1b) và **kết** (§1c) ghi trong bảng nhịp: tên chương gợi hình, câu chốt cuối chương, bảng điểm 3–4 mục, hình mở đầu quay lại, câu chuyền tập kế. **Số nói bằng tỉ lệ con người, mỗi lựa chọn một màu** (`story.md` §3).

10. **Năm luật nhân vật (`story.md` §2b, từ Tập 6):** một nhân vật dẫn đường từ cold open đến kết (trước 0:45, đi qua phần phương pháp, câu kết là câu của người đó); lời hứa nhân vật trả ≤ 90 s (M6); cái được–mất bằng vật cụ thể khi không được nêu số tiền ("23 more bills"); câu ở đỉnh cảm xúc ≤ 15 từ, một ý một câu; kết quay về câu hỏi của nhân vật. WRITER ghi trong bảng nhịp: tên nhân vật dẫn đường, câu đỉnh cảm xúc (số từ), câu kết.

11. **Hồ sơ cầu (`market/topics/<đề tài>.md`, §1b):** nhân vật dẫn đường dựng từ **một hoàn cảnh điển hình** của hồ sơ (vẫn ILLUSTRATIVE); kịch bản **trả lời ≥ 3/5 câu hỏi khán giả** (ghi câu nào trả ở cảnh nào trong bảng nhịp); **một nhịp xử lý một điểm yếu đối thủ** của hồ sơ (vd "giả định lợi suất cố định" → phát lại lịch sử thật) mà không nêu tên kênh; **độ dài trong dải thời lượng vượt trội** của hồ sơ **và** trong khung `format` §9 — hai dải không giao nhau thì theo `format` và ghi một vế trong dòng **Độ dài** sẵn có của G1 (đổi khuôn là quyền chủ dự án).

12. **Video neo (D-012, `packaging.md` §7.1):** lời hứa trả lời trong **50 s đầu** (M2, D-013) đúng câu hỏi của video neo, và một nhịp lấp **đúng khoảng trống** của neo (dòng "khác biệt" ở G1, thường là phát lại lịch sử thật) — không nêu tên kênh, không chép tiêu đề.

**Móc do máy chọn (D-006 Q4):**
- WRITER viết **3 phương án 50 s đầu**, mỗi phương án một kiểu mở khác nhau (tin thời sự / nghịch lý / được–mất). Cả ba đều theo `story.md` §1 (M1–M8).
- **So cặp móc — ỨNG VIÊN, đã hiệu chuẩn chính thức (P1 Tập 4, `episodes/ep004/cal-hook/`, lessons G1):** chọn bản gốc 7/8, mỗi mẫu ≥ 3/4, mỗi vị trí ≥ 3/4 — **đạt đúng bằng ngưỡng** ở cả ba điều kiện; mẫu mới (Tập 1 + kịch bản mới), thứ tự X/Y cân bằng. **Mới chứng minh phân biệt "có móc / bỏ móc"**, chưa chứng minh chọn đúng giữa ba móc đều tốt (Tập 4: người đọc chọn vị trí Y 7/9 ở vòng tròn). Cách dùng (chủ dự án, G1 Tập 4):
  - **từ Tập 5:** REVIEWER chấm 3 phương án theo story §1 + điều kiện M1–M8 (§3.9); so cặp vòng tròn (headless, 3 lượt mỗi cặp, thứ tự xoay, báo lệch vị trí) **chỉ khi REVIEWER không tách được** (Tập 4: 9 người đọc, 0,29 triệu, H1/H2 không phân biệt);
  - **kèm WRITER + REVIEWER**: REVIEWER chấm 3 phương án theo story §1 (lý do một dòng); khi so cặp và REVIEWER lệch nhau, hoặc khi thắng thua chỉ do bản đứng cùng một vị trí, G1 nêu cả hai;
  - mỗi lần dùng ghi kết quả + lệch vị trí vào ledger; hiệu chuẩn lại khi đổi model người đọc. Thước đo thật vẫn là giữ chân YouTube.
- G1 hiện móc đã chọn dạng chữ trong kịch bản + 2 phương án còn lại, mỗi phương án một dòng. Chủ dự án chỉ đổi khi muốn. **Không sinh giọng cho phương án không chọn.**

## 4. Song song sau C2
- Phiên K (§7).
- Phối nhạc style C, đo độ lặp T2 (Tham khảo).
- Lời theo cảnh: tên take theo hash chữ; kiểm từ khoá ASR ngay khi sinh; chỉ sinh lại cảnh đổi chữ.

## 5. Gói phát hành và Short (D-013: 1 Short; D-015: cổng đóng gói — tiêu đề theo tìm kiếm ở G1, 3 ảnh bìa ở G3)
- **Tiêu đề:** chốt ở G1 (so cặp một vòng, Tham khảo); M6 dùng đúng tiêu đề G1 trừ khi chủ dự án đổi ở G2.
- **Mô tả, chương, tag: máy viết ở M6** từ claims, `out/timeline.json` (chương = tên chương gợi hình, `story.md` §1b) và hồ sơ cầu; kiểm bằng `python3 toolkit/market/package_check.py episodes/epNNN --title "…" --description <tệp>` (S21, claim-risk, chương khớp timeline ±2 s, ≥ 10 s/chương) + REVIEWER không cần (gói không tới chủ dự án trước G3; lệch thì sửa trước G3). Khối `[METHOD AND SOURCES]` + ghi công CC BY (RIGHTS) trong mô tả.
- **Cổng đóng gói (D-015, chủ dự án 17/10 — thay "Không thumbnail" của D-013):**
  - **G1 — tiêu đề theo tìm kiếm:** 3 tiêu đề ≤ 60 ký tự; cụm tìm kiếm có bằng chứng (gợi ý tìm kiếm YouTube lưu kèm ngày, hoặc từ khoá hồ sơ cầu) nằm trong **40 ký tự đầu**; có số hoặc hệ quả cụ thể; không thuật ngữ khó; `package_check` (số có claim, khuyên/dự báo) = 0 lỗi; bảng xếp hạng + lý do. Tiêu đề có số kèm điều kiện → điều kiện ở **dòng 1 mô tả**. Mẫu: `packaging/R1.md` §1, `packaging/r1/titles.json`.
  - **G3 — duyệt 3 ảnh bìa:** 3 ảnh 1280×720 + 1 đối chứng dựng bằng mã. Phần hình: mô hình ảnh OpenAI vẽ **nền không chữ** theo STYLE chung của kênh (`packaging/r1/ai/prompts.json`: minh hoạ 3D đất sét/đồ chơi, 1 chủ thể ~40 % khung bên phải, sáng, tương phản mạnh) hoặc khung phim (`packaging/r1/make.py`); **chữ ≤ 4 từ (đối lập/câu hỏi có ngữ cảnh) + 1 con số + nhận diện kênh ghép bằng mã** (`packaging/r1/ai/compose.js` qua `final.py`/`round2.py`). Mỗi tập 6 phương án → Claude chấm bằng mắt ở 360 px + 168×94, giữ 3; **kiểm máy 168×94 ĐẠT** (chữ hoa ≥ 9 px, tương phản WCAG ≥ 4,5:1 chữ trắng và chữ màu trụ); **claim-risk 0**; chữ trên ảnh bổ sung, không lặp tiêu đề, số khớp tiêu đề.
  - **Cấm trên ảnh bìa:** người thật/nhận diện được, ảnh chụp chân thực người, logo thương hiệu, cảnh/hứa hẹn video không có, chữ do mô hình ảnh vẽ. **Không nhãn ILLUSTRATIVE trên ảnh bìa** (giữ trong video và mô tả). Video giữ quy tắc không nhà cung cấp video/ảnh AI.
  - **Sổ:** mỗi ảnh AI một dòng `RIGHTS.md` §H (công cụ, model, prompt, ngày, chi thật — `packaging/r1/ai/ledger.jsonl`); trần chi ảnh theo lệnh chặng. Chủ dự án chọn ảnh mặc định + thứ tự **Test & Compare** ở G3; `HUONG-DAN-DANG.md` ghi bộ 3 ảnh + dòng 1 mô tả. Luật checks P01 (token share) chờ khiếu nại A50.
- **Không tóm tắt AI ở G2.**
- **1 Short 9:16 mỗi tập**, cắt từ nhịp then chốt đã qua checks (thường là số neo hoặc nghịch lý mở đầu), dựng một lần ở M6:
  - ≤ 60 s;
  - chữ ≥ sàn dọc 56 px ở 1080×1920;
  - vùng an toàn dọc (trên 200 px, dưới 320 px);
  - ILLUSTRATIVE và "history, not a forecast" trên mọi khung có số;
  - **móc Short ≤ 1 dòng ở cỡ sàn 56 px** (≈ ≤ 26 ký tự Inter Bold trong bề rộng an toàn 960 px), đo bằng hộp chữ khi viết (bước spine Short; SH06, lessons T6-10).
  Short duyệt ở G2 dưới dạng mô tả + mốc giây (dựng sau G2, ở M6); lệch kỹ thuật sửa không mở lại G2.
- **Hướng dẫn đăng:** `episodes/epNNN/HUONG-DAN-DANG.md` theo `playbook/templates/HUONG-DAN-DANG.md`.
- **Đường ChatGPT (§5c cũ, Tập 7) bỏ từ Tập 8** — giữ ở `packaging.md` §7 làm tham chiếu.

## 5b. Âm: nhạc hiệu, cue theo hồi, lặng trước số neo (tổng kết Tập 5 §3.4, từ Tập 6)
- **Nhạc hiệu kênh:** 3 s ở ident (`IDENT_S = 3`) và **một khúc đóng khác**; nhạc bằng mã (D-010 §5), dựng một lần cho cả kênh. Gu nhạc là quyền chủ dự án (CHARTER §6): **chủ dự án duyệt nhạc hiệu bằng clip có âm ở C3 Tập 6** (một lần cho cả kênh), sau đó dùng lại mọi tập.
- **Mỗi hồi một cue riêng, không lặp vòng:** nhạc vẫn theo bản đồ căng (F-3 Tập 5: dâng ở phần phát lại, chốt hợp âm đúng từ khoá), thêm ràng buộc cue khác nhau giữa các hồi và không lặp vòng trong hồi.
- **Lặng 0,7–0,9 s trước mỗi số neo** (≤ 3 số neo/tập, §3.2.4 của tổng kết; beat khai `anchor: true` trong spine). Tiếng hiệu ứng "land" đè đúng từ khoá số neo phải bỏ (F-2: sfx chỉ thấp hơn lời 11 dB).
- **Không tăng mật độ sfx** khi thêm cue (F-2 cảnh báo đoạn a Tập 5: 21,7 sự kiện/phút, 8 trong 10 s). Lặng trước số làm tập dài ≈ 2–3 s — tính vào ước độ dài.
- **SFX ghi âm thật (D-013):** tiếng vật thể đổi trạng thái (giấy, kim loại, gỗ, tiền xu) dùng bản ghi âm thật **CC0 hoặc CC BY 4.0** (kho CC0 trong `toolkit/audio/sfx/` (F-18); không Freesound; **không** CC BY-NC, Sampling+, BBC RemArc, kho trả phí), thay tiếng tổng hợp khi đã có trong thư viện `toolkit/audio/sfx/` (mỗi tệp một dòng `RIGHTS.md`: URL, tác giả, giấy phép trích nguyên văn, ngày tải; CC BY → ghi công trong mô tả). Mật độ không tăng (dòng trên). Thử trên đoạn Tập 7 trước (đường thử tập cũ), vào tập đang chạy ở ranh giới cổng.
- **Tiếng dữ liệu dưới lời (Tập 9 trở đi, chủ dự án G3 Tập 8 15/10, lessons T8-1):** `data_db` mặc định **34** để L1 (lời/tiếng dữ liệu 1–4 kHz, phân vị 10) ≥ 20 dB; đo L1 trên nháp M5.
- **Nhạc giữ bằng mã** (D-010 §5; xét lại nhạc người sáng tác CC BY ở G1 Tập 9 — D-013). Không nhạc AI, không NC/ND, không YouTube Audio Library.

## 6. Giao hàng
- Lệnh: `python3 toolkit/deliver/deliver.py episodes/epNNN/out/video.mp4 --out episodes/epNNN/work/delivery --name epNNN --branch epNNN-delivery --push`
- Mã hoá: 1080p 8 Mb/s (24–30 fps), audio copy; phần 90 MB, `SHA256SUMS`, `JOIN.md`. Không gửi qua chat.
- Chủ dự án tải xong thì xoá nhánh (proxy chặn xoá → việc treo cho chủ dự án).
- **Git LFS trên nhánh `release-epNNN`: chưa thử** (chuyển sang phiên nhà máy). Phải kiểm hạn mức LFS của tài khoản trước; vượt thì giữ cách phần 90 MB.

## 7. Phiên K và hàng chờ luật
- K chạy **một lần mỗi tập**, ngay khi claim C2 chốt. Tên `model.kind`/params do K quyết.
- Mọi đề xuất đổi luật (của bên dựng, tổng kết, REVIEWER) ghi vào **`checks-appeal.md`**. K xử lý theo lô ở lần chạy của tập kế tiếp. Chỉ mở phiên K riêng khi cần **kind mới**.
- Checks khi dựng: chỉ luật liên quan cảnh vừa sửa. **Đủ bộ (gồm bộ lấy mẫu trang) ở M5 trên nháp, trước G2** (TONGKET Tập 7 o; A41a); trên 1080p ở M6 chỉ nhóm kỹ thuật + SSIM. Chạy trên bản sao khoá có server riêng (`episodes/ep003/design/c5/checks.sh` là mẫu).

## 8. KPI và trần token

**Mức cảnh báo D-013 (từ Tập 8; chỉ cảnh báo, D-009 c — vượt thì báo số thực trong gói, không cắt bước chất lượng).** Vai Line producer ghi theo mốc vào PLAN tập §5:
| | Tập 9+ `lab` (đích) | Tập 8 (chuyển đổi) | Tập 7 thực |
|---|---|---|---|
| Trần token (log phiên + headless) | 15 triệu (giữ) | 15 triệu | ≥ 4,1 |
| **Đọc cache** (log phiên, cộng các phiên) | **≤ 60 triệu/tập** | ≤ 60 triệu | ≥ 371 |
| **Lượt mỗi phiên** | **≤ 150** | ≤ 150 | P3: 358 |
| Console | $25–40 | $45–60 | $115,6 |
| Giờ máy | 8–12 h | 15–20 h | ≈ 36 h |
| Chủ dự án | G1 + G2 + G3 ≈ 1–1,5 h | + 1 chạm nếu không có C3 | 10 lần chạm |
- **Ghi lượt chạm + phút chủ dự án** mỗi lần chủ dự án quyết hay trả lời (PLAN tập §5 cột cuối; ledger loại việc "chủ dự án").
- Đọc cache và số lượt lấy cùng lúc với 4 số token (`from_events.py --close`: `modelUsage.cacheReadInputTokens`, `num_turns` — cộng các tiến trình của phiên). Phiên chạm 150 lượt → đóng chặng sớm (PLAN ≤ 1 trang, phiên mới "Chạy Tập N").
- Bảng KPI và mức cảnh báo dưới đây là lịch sử (Tập 2–7); phần còn hiệu lực: trần token theo format, EL theo format, giờ máy `deep`.

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

**Mức cảnh báo theo format (từ Tập 7, tổng kết Tập 6 §3; chỉ cảnh báo, D-009 c) — chủ dự án duyệt 11/10 (câu 1g: chi Console; câu 2: `deep`). Thay trần EL 6.000 và ≤ 40 agent ở trên từ Tập 7; agent con mặc định 0 (§2).** Gốc: Tập 6 thực ≈ 83,0 triệu, trong đó 72,95 là P3b (agent con dựng C4); làm theo cách P3c (headless khoá Console, 0 agent con) thì Tập 6 ≈ 11–12 triệu trần phiên + kiểm mù + ≈ $30 Console. `deep` ≈ 1,8 × thời lượng `101` → ≈ 1,6–1,8 × việc dựng/kiểm.
| | `101` | `lab` | **`deep`** |
|---|---|---|---|
| Trần token (log phiên + headless thuê bao) | 12 triệu | 15 triệu | **20 triệu** |
| Chi khoá Console (cách chuẩn — lessons T6-9, duyệt 11/10) | $35 | $45 | **$60** |
| ElevenLabs (ký tự; 6,0 ký tự/từ nói gồm sinh lại — Tập 6) | ≤ 6.000 (trần; Tập 6 thực 7.699 do duyệt ở C3) | ≈ 8.500 | **≈ 13.000–15.000** (2.120–2.450 từ nói × 6,0; sinh lại kiểu Tập 5 → ≈ 17.000) |
| Giờ máy (1080p + checks, gồm 1 lượt sửa) | ≈ 12 h | ≈ 15 h | **≈ 22 h**; ≈ 35–40 h nếu chưa có A29 (cache trang theo cảnh) |
- **EL cho `deep` vượt trần 6.000 ký tự/tập ở trên**: trần 6.000 là cho `101`. **P1 đọc hạn mức còn lại qua API** (`GET /v1/user/subscription`, khoá qua proxy; chỉ ghi ký tự còn/giới hạn + ngày làm mới, không ghi khoá) và nêu ở G1: 13.000–15.000 ký tự/tập × 4 tập/tháng ≈ 52.000–60.000 ký tự/tháng, chưa tính Shorts và đọc thử. Hạn mức không đủ → `lab`, hoặc nâng gói (chi tiêu mới, CHARTER §6).
- **Giờ máy:** 1080p không cache ≈ 2,8 h cho 536,6 s (Tập 6), nên `deep` 900–1.020 s ≈ 4,7–5,3 h một lượt đủ, vượt trần 2 h của lệnh nền → bắt buộc chạy tiếp được (§11b).

**Mỗi phiên khi đóng ghi 4 số đọc từ log vào PLAN tập mục 5:** sinh ra · đầu vào mới · đọc cache · trần. Cách lấy: `list_events(session_id=<phiên này>, kinds=["result"], limit=100)` — bộ lọc chạy sau khi đọc trang nên trang có thể không có `result`: lật trang bằng `before_id` tới khi gặp — → lưu trang JSON → `python3 toolkit/usage/from_events.py --session <id> --close trang*.json`. Sự kiện `result` chỉ có khi một lượt kết thúc → số ghi được là **đến lượt trước**; lượt đóng cộng vào ở phiên sau (ghi "đến <giờ>"). Headless không nằm trong log phiên: cộng bốn trường `tokens` của JSON đầu ra (`toolkit/blind/headless.sh`). Bảng cả tập: `python3 toolkit/usage/token_log.py <jsonl…> [--windows …]`. Ghi thêm **giờ render thực** (`build-report.json`, `<đoạn>.build.json`).

<details><summary>Mức cảnh báo Tập 5 (cũ, 3,0 triệu theo số công cụ báo — thực đo bằng log 85,4)</summary>

Kiểm mù 0,6 · dựng 0,75 · WRITER 0,4 · REVIEWER 0,45 · checks 0,15 · điều phối 0,5 · dự phòng 0,15 (`tongket-t4/REPORT.md` §7). So với log: `tongket-t5/REPORT.md` §1b.
</details>

## 9. Định dạng tập (`episode.yaml` → `format`)
| `format` | Thời lượng | Cấu trúc | Mid-roll |
|---|---|---|---|
| `lab` | 9–11 phút | móc → bối cảnh/nhân vật → hành trình (phép thử) → đáp án + ngưỡng → giới hạn | 2, ở ranh giới hồi |
| `101` | 8–9 phút | khái niệm → thí nghiệm nhỏ trên dữ liệu thật → khác nhau ở 2–3 người → giới hạn | 1, ở ranh giới hồi, trong khoảng lặng |
| **`deep`** *(D-012; chủ dự án duyệt 11/10, câu trả lời tổng kết Tập 6 câu 2)* | **14–17 phút** (ước G1 ≥ 14:42 = sàn + 5 %; tối đa cứng 17:00) | móc → khái niệm + **hai nhân vật** cùng xuất phát → phát lại **nhiều cửa sổ lịch sử** → nhân vật 2 / ca đối chứng → **câu hỏi khán giả** (ACT 4) → giới hạn | **2–3**, mỗi điểm ở ranh giới hồi có lặng ≥ 1 s, ≥ 2 phút đầu/cuối, cách nhau ≥ 3 phút |

- **Luật chung:** mid-roll không đặt trong 2 phút đầu hay 2 phút cuối, luôn ở khoảng lặng ≥ 1 s.
- **`101` không độn nội dung:** thiếu chất thì ngắn hơn hoặc gộp khái niệm. Thời lượng tối thiểu là mềm; tối đa là cứng.
- **Độ dài `101` và mid-roll (lessons T6-1, chủ dự án 08/10):** YouTube chỉ cho mid-roll khi video **≥ 8:00** — tập dưới 8:00 **không được ghi là có mid-roll**. Ba chốt: **G1 ≥ 8:25 ước** (≥ 1.212 từ nói ÷ 2,40 từ/s — hằng Tập 6, lessons T6-5; trước: 1.275 ÷ 2,52; `check_script.py` CHẶN dưới 505 s; dư ≈ 5 % cho sai số hằng, cắt chữ sau G1, sinh lại giọng) → **≥ 8:10 thật trên timeline sau khi sinh lời** (thiếu → sửa trước render) → **≥ 8:00 ở C5** kèm chỗ mid-roll hợp lệ. Ngắn hơn chỉ khi chủ dự án chọn ở G1, và khi đó tập không có mid-roll.
- **Mọi gói G1 có một dòng mid-roll** (mẫu `playbook/templates/G1.md`): *"mid-roll: đủ điều kiện / không đủ (độ dài ước m:ss, cần ≥ 8:00 thật; mốc m:ss ≥ 2 phút đầu/cuối; lặng ≥ 1 s)"*.
- Khuôn đã thiết kế, **chưa dựng tập 101**. Kiểm khuôn tự động nằm trong `build.sh` (phiên nhà máy).
- **`deep` — điều kiện không độn (D-012 mục 1; kiểm ở C1–C2, nêu ở G1):** chỉ chọn `deep` khi hồ sơ đề tài có **đủ cả ba**: (1) **≥ 3 cửa sổ/thời kỳ lịch sử cho kết quả khác nhau** (mỗi cửa sổ một kết quả mới, không lặp kết luận); (2) **hai nhân vật** ILLUSTRATIVE cùng xuất phát, khác một lựa chọn (khuôn "Same start, different choice", `market/REPORT.md` §3); (3) **≥ 3 câu hỏi khán giả** của hồ sơ cầu, mỗi câu một nhịp trả lời riêng (ACT 4). WRITER ghi cạnh mỗi phút thêm (so với `lab`) claim mới hoặc câu hỏi được trả lời; phút không có cả hai là độn → cắt. Kiểm mù lời C2: không loại khối nào bị ≥ 2/6 người đọc nêu mất chú ý (như mọi format). Thiếu một trong ba → `lab`/`101`, ghi một vế ở dòng **Độ dài** của G1.
- **`deep` — mid-roll:** 2 điểm khi độ dài < 15:30, 3 điểm khi ≥ 15:30; chỉ ở ranh giới hồi (sau móc ≥ 2:00, trước 2 phút cuối), lặng ≥ 1 s, cách nhau ≥ 3:00. `check_script.py` mẫu kiểm trên độ dài **ước** (số điểm theo 15:30, khoảng cách, ACT 4 bắt buộc); chốt lại trên độ dài thật sau khi sinh lời; checks khoá: đề xuất A31 (lô K Tập 7, trước C4).
- **`deep` — nhà máy trước:** tập chỉ được chọn `deep` khi F-14 đạt đích **trước G1** của tập đó (Tập 7: không đạt → `lab` 11 phút; Tập 8 xét cùng cách ở G1 lô — chủ dự án 11/10); tập `deep` đầu tiên chỉ mở C3 khi F-14 (nhịp hình, `toolkit/factory/BACKLOG.md`) đã đạt đích đo trên Tập 6 dựng lại (D-012 mục 1, lessons T6-6).

## 10. Sau phát hành
Ở mốc 7 ngày: `episodes/epNNN/audience.md` theo mẫu `playbook/templates/audience.md`. Chủ dự án gửi **một** ảnh chụp YouTube Studio cho chat chiến lược. Điểm rời lớn nhất → nhịp kịch bản tương ứng → `lessons.md` / `story.md`.

**Vòng tự hiệu chỉnh dữ liệu thị trường (Phiên Thị trường bước 8; máy làm, không hỏi):**
1. **Sau mỗi tập:** ghi vào `market/CALIBRATION.md` một dòng: tập, đề tài, nhãn cầu lúc chọn (cao/vừa/thấp), nhãn khoảng trống, **lượt xem 28 ngày** của tập (kênh mình — số của Crux, được ghi). Số 28 ngày lấy cùng ảnh YouTube Studio ở mốc 7 ngày khi có, không thì ở tổng kết tập kế.
2. **Sau mỗi 3 tập có nhãn:** nếu trung vị lượt xem 28 ngày của các tập nhãn "cao" **không hơn** các tập nhãn "vừa" → nhãn cầu sai: sửa cách tính trong `toolkit/market/analyze.py` (`cmd_profile`: trọng số lượt xem/ngày, số video vượt trội, số bình luận yêu cầu) trên nhánh `market-*`, chạy lại `report.py topics`, ghi lý do vào `market/CALIBRATION.md`. Chưa đủ 3 tập "cao" và 3 "vừa" → ghi "chưa đủ mẫu", không sửa.
3. **Hằng tháng khi có Analytics kênh mình:** kênh nằm trong nguồn lưu lượng "video đề xuất" (suggested videos) của Crux → thêm/giữ ở `market/CHANNELS.md` (vòng tương ứng, lý do "nguồn đề xuất"); kênh trong danh sách 3 tháng liền không xuất hiện và không có video nổ → bỏ. Danh sách mới nổi hết hạn thử việc 90 ngày được xét cùng lúc.
4. **Sau đăng 48–72 giờ (luật D-012; công cụ chưa dựng — Phiên Analytics sau):** đọc **tỷ lệ nhấp (CTR) lượt hiển thị** và tỷ trọng nguồn **"video đề xuất"** (suggested) + "duyệt qua" của tập. CTR dưới trung vị 5 tập gần nhất của kênh **và** nguồn đề xuất < nguồn tìm kiếm → đề xuất **đổi** thumbnail sang phương án Test & Compare kế tiếp / tiêu đề T2 (chủ dự án duyệt, một dòng). CTR ≥ trung vị → **giữ**. Ghi quyết định + số vào `audience.md`.
5. **Hằng tháng:** chạy `anchors.py trend` cho đề tài của các tập đã đăng; đề tài có video mới đang lên (tốc độ "cao") → gợi ý **đổi tiêu đề video cũ** theo cụm tìm kiếm đang lên (không đổi nghĩa, không số mới, claim-risk như P4); chủ dự án duyệt.

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
| Kiểm rảnh trước build | `python3 toolkit/factory/guard.py` (thoát 3 khi còn build/render) |
| Chú thích nuốt mã + cú pháp | `python3 toolkit/tests/comment_guard.py [thư mục …]` |
| Thước chỉ báo | `toolkit/indicators/README.md` |
| Thị trường: làm mới / hồ sơ cầu | `toolkit/market/{purge,discover,pull,analyze,report}.py` (§1b) |
| Brief đóng gói ChatGPT (đường chính, P4) · kiểm gói P4 | `python3 toolkit/market/brief.py …` · `python3 toolkit/market/package_check.py …` (§5c) |
| Token phiên (đóng phiên) | `python3 toolkit/usage/from_events.py --session <id> --close trang*.json` |
| Video neo (G1) · xu hướng 7 ngày (P4) | `python3 toolkit/market/anchors.py anchors --topic <id> --question "…"` · `… trend --topic <id> --days 7` |
| Chấm lại P4 (bộ lọc thô) · công cụ phụ: chữ gói (Claude), thumbnail lai | `python3 toolkit/package/rescore.py …` · `text.py …` · `thumbs.py …` (`packaging.md` §7.5) |
| Headless khoá Console (dựng/đọc — cách chuẩn, §2) | `bash toolkit/api.sh <build\|review> <đầu-bài.md> <log.jsonl>` |
| Checks đủ bộ chạy tiếp được | `EP=episodes/epNNN bash toolkit/checks_split.sh <thư mục ngoài repo>` (`RESUME=1`, `KEEP=1`) |
| Tốc độ đọc thật theo tập | `python3 toolkit/usage/measure_pace.py <tập…>` |

## 11b. An toàn chạy nền (tổng kết Tập 5 mục 12; cine-lab BAI-HOC-LL #38, #67, #70)
- **Trần 2 h của lệnh nền (lessons T6-4; Tập 6: checks 10,3 h, 1080p 7,7 h, ba lần bị cắt).** Việc ước > 1,5 h phải **chạy tiếp được**: `build.sh` (cache đoạn/cảnh) và `EP=episodes/epNNN bash toolkit/checks_split.sh <thư mục ra cố định ngoài repo>` (`RESUME=1` khi bị cắt; `KEEP=1` giữ cache trang theo cảnh giữa các lượt → cảnh không đổi trúng cache (chỉ đầy đủ khi A29 qua K: khoá cache hiện gồm cả tệp trang của tập, đổi trang là lấy mẫu lại cả tập); `K_JOBS=4`). Bị cắt → chạy lại **đúng lệnh đó**, không bắt đầu lại từ đầu. Đoạn thế giới dựng song song khi máy rảnh; **không** chạy checks song song với render. Biến môi trường nới trần (`BASH_MAX_TIMEOUT_MS`) **chưa xác minh** có tác dụng với lệnh nền — thử ở BƯỚC 0 P3, ghi kết quả vào lessons, không dựa vào khi chưa đo.
- **Build, checks, render, lượt headless chạy bằng công cụ chạy nền của phiên** (Bash `run_in_background`; thông báo về khi xong). **Không `&`, không `nohup`** tự do: tiến trình `&` không được theo dõi, mất khi phiên/máy khởi động lại (cine-lab #38: tập 4 mất giữa render), và phiên tưởng build đã dừng.
- **Trước mỗi build: không còn tiến trình build/render nào** — `python3 toolkit/factory/guard.py` (`ps`, bỏ qua chính shell của lệnh và các tiến trình cha/con của nó). `build.sh`, `build.py`, `build_seg.py` tự gọi và **từ chối, thoát 3** nếu còn (cine-lab #67: hai build ghi chồng một thư mục, x264 hỏng tệp thống kê). Thử 08/10: build thứ hai trên đoạn Tập 4 v3k khi build thứ nhất đang render → thoát 3, `build.sh` → thoát 3.
- **Mã lỗi qua `PIPESTATUS`:** mọi lệnh `… | tee log` đọc `${PIPESTATUS[0]}` (mã của lệnh dựng, không phải của `tee`); `build.sh` đã làm vậy, log ở `<tập>/work/factory/build.log`.
- **Lưu ý:** bước `spine` vẫn ghi `spine.json` thẳng vào thư mục đoạn (nguồn, có trong git) — build trượt sau bước spine để spine mới cạnh mp4 cũ; xem `git diff` của đoạn trước khi dựng lại.
- **Đoạn thế giới dựng vào thư mục tạm** `<thư mục ra>/.staging-<tên>-<pid>/`, **chỉ thay bản cũ khi cả 6 bước đạt**; trượt → bản cũ giữ nguyên, báo cáo `<out>.build.failed.json` (cine-lab #70: xoá trước khi dựng, lỗi giữa chừng → mất 2,5 h khung). Cache cảnh của `render_shots.js` vốn ghi `.part` rồi đổi tên, không xoá.
- **Đầu mỗi build:** `toolkit/tests/comment_guard.py` (mục 13; cine-lab #42, #76) — chú thích chèn giữa dòng nuốt mã + `node --check` (mô-đun ES qua `.mjs`) / `py_compile` mọi mã thế giới của tập và thư viện; lỗi → dừng trước khi dựng. Không chèn chú thích vào giữa dòng mã; đặt chú thích ở dòng riêng hoặc cuối dòng sau khi đã kiểm.
