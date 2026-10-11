# F-14 · Ý đồ + ngưỡng ghi trước (viết 11/10/2026, TRƯỚC khi dựng lại hay đo bản F-14)

Phiên nhà máy F-14 (`tongket-t6/F14-brief.md`), nhánh `factory-f14` từ `main` @ `38fda7d`. Việc không phải tập (CHARTER §2.3): giúp Tập 7–8 —
`deep` của Tập 8 chỉ mở được khi F-14 đạt đích dưới đây trước C2 Tập 8 (`episode.md` §9).

## 1. Giả thuyết
Nhịp hình tụt ở Tập 6 (lessons T6-6) do ba nguyên nhân nhà máy, không do kịch bản: (1) khi máy đứng yên không gì sống — vật dữ liệu đổi bậc
trong 0,1–0,3 s rồi đứng; (2) không có cờ đo "thay đổi mang nghĩa" nên bước spine không cảnh báo được quãng dài; (3) quy tắc 7 (5 s đầu thế giới)
bị áp cho MỌI đoạn và quy tắc 1 (số chỉ ở đồ thị) giữ nhãn số chờ cú đổi chế độ → nhãn trễ lời (vd "3%" 1,26–1,29 s).
Sửa ở nhà máy (a)(b)(c) rồi dựng lại Tập 6 với cùng kịch bản, giọng, nhạc → bốn số đích đạt mà cổng gốc (nghĩa khi tắt tiếng) không tụt.

## 2. Đối chứng
Master bản giao `ep006-youtube.mp4`, SHA-256 `f96da0ea19e6426aa3b4bd37759f3e7c8fb9819e489a1fab317683fd5edcaa74` — lấy từ nhánh `ep006-delivery`
(`git fetch origin ep006-delivery`, ghép 13 phần, `sha256sum -c SHA256SUMS` → **OK**, 11/10). Số đối chứng đo lại trong phiên này bằng đúng
cách đo dùng cho bản F-14:

| Thước | Cách đo (một cách cho cả hai bản) | Đối chứng |
|---|---|---|
| quãng tĩnh có lời > 8 s | `toolkit/indicators/spine_pace.py <6 spine.json> --labels` (không sửa thước) | **7** (dài nhất 11,3 s); tính cả nhãn **4** |
| freezedetect ∩ lời | `toolkit/factory/f14/measure.py` = `qc.py freezes` (n=−60 dB, d=3) ∩ `qc.speech_spans(timeline.words)` | **206,01 s**, 51 quãng (qc bản giao 206,03) |
| R07 | `checks/` khoá `4d688acd`, `run.py` đủ bộ (bộ lấy mẫu trang + luật Python) | **70,3 %** (83/118, `run-c5d`) |
| nhãn "3%" | `textTrack` của bộ lấy mẫu trang checks: mẫu đầu có chữ "3%" − đầu từ "three" (cue `g1.three` + t0 đoạn f) | **1,29 s** (460,9 − 459,61; G2 ghi 1,26 s bằng cách khác) |
| cổng gốc (khoá nghĩa) | `episodes/ep006/c4/blind_c4.py` strips → read root → pack → grade (2 người chấm, gộp thận trọng), rubric MỚI (`gates/C4-answer.md`) | **20/23** ở bản giao (B01, B15, B04 0,5) |
| CHẶN | checks đủ bộ | **0 trượt** (36/36) |

## 3. Đích (không hạ sau khi đo)
| Thước | Đích | Vai trò |
|---|---|---|
| quãng tĩnh có lời > 8 s (spine) | **0**, và 0 khi tính cả nhãn | chỉ báo (thước chưa hiệu chuẩn, A23 đối chứng dương 2/4) |
| freezedetect ∩ lời | **< 60 s** | **số chính** |
| R07 | **≥ 90 %** | **số chính** |
| "3%" | **≤ 0,2 s** | số chính của (c) |
| cổng gốc | **≥ 20/23 và mọi nhịp ĐẠT ở bản giao vẫn ĐẠT**. Nhịp nào tụt: đọc lại một lượt 3 người; vẫn tụt → TRƯỢT | **số chính** (khoá nghĩa) |
| CHẶN | **0** | **số chính** |
Cùng phiên đọc lại cổng gốc trên dải của bản giao (cùng số người đọc/người chấm) để tách dao động người đọc khỏi thay đổi hình; bảng báo cả hai.
Báo thêm (không là đích): R08, V14, qc nhà máy, F-2 (sfx/nhãn đè), mọi nhãn số lệch > 0,2 s, giờ render, chi, token.
**Đạt = mọi số chính đạt.** Trượt một số → báo số, không hạ đích, không merge; phiên điều phối Tập 7 quyết.

## 4. Điều kiện dựng lại
- Từ `main` + mã F-14 của nhánh; **cùng kịch bản** (`story/script.md`, `c4/gen`), **cùng giọng** (30/30 take trong `voice-takes/`, 0 ký tự EL),
  **cùng nhạc** (`bed.py` sinh lại từ cùng timeline; ident/close A), cùng claim, 1080p, 30 fps — như bản giao.
- Bản F-14 của 6 đoạn nằm ở `toolkit/factory/f14/ep006/` (chồng lên bản sao làm việc `git worktree` ở thư mục tạm khi dựng):
  **`episodes/ep006/` trên nhánh không đổi** (bản giao là bằng chứng). Không chạm tệp Tập 7/8.
- Chỉ đổi hình theo (a)(b)(c). Không đổi lời, thứ tự cảnh, giờ cảnh, số trên hình, máy quay ở từ khoá (quy tắc 2 vẫn kiểm), lượng sfx.

## 5. Chống Goodhart (ghi trước)
- **Chuyển động nền (a)** khai ở khoá `life` của spine — KHÔNG ở `visual_cues`, `*_kf`, `draw`, `ride` — nên **không** được `spine_pace.py`/R08
  đếm là thay đổi. Quãng tĩnh trên spine chỉ hết khi có **thay đổi trạng thái dữ liệu thật** gắn vào một từ được nói (cue có `change: major`).
- Mỗi track `life` phải nói được nó biểu diễn đại lượng nào của câu (năm trôi, thùng mờ theo sức mua, séc lớn theo số kỷ niệm, dải quét theo
  tháng bắt đầu…) — giá trị ở mỗi từ khoá trùng giá trị cũ (đích không đổi, chỉ đường đi liên tục thay bậc + đứng). Không lắc/thở/trôi trang trí
  (gen CHARTER §4). Track không giải thích được bằng một dòng = bỏ.
- Nhãn không tính là thay đổi hình (thước giữ nguyên).
- Không sửa `checks/` (LOCK `4d688acd`); đề xuất (nếu có) → `checks-appeal.md`.

## 6. Ngân sách
Trần chi cảnh báo **$45** (Console: cổng gốc 2 bản ≈ $3, REVIEWER ≈ $1–2). Việc nặng chạy headless khoá Console (`toolkit/api.sh`),
0 agent con. Render 1080p ≈ 1–3 h máy, checks đủ bộ ≈ 5–10 h máy: tách lệnh chạy tiếp được (`toolkit/factory/f14/rebuild.sh <bước>`, episode.md §11b).

## 7. Bổ sung trước khi đo (11/10, trước lần đo đầu tiên của bản F-14)
Bản F-14 thêm cue hình MỚI (vd ba mục giỏ "rent / medical care / gasoline", nhãn giá trị của bậc thang) → mẫu số R07 đổi. Để cue dễ đo không thổi
phồng tỉ lệ: **R07 báo hai cách và đích ≥ 90 % phải đạt ở CẢ HAI**: (1) toàn bộ cue của bản F-14; (2) **chỉ 118 cue của bản giao** (cùng tên cue,
cùng cách đo). Cue đổi tên/bỏ khỏi `visual_cues` = tính là trượt ở cách (2). Tương tự, thước spine báo cả "chỉ cue cũ".

## 8. v4 — ghi trước (12/10, chủ dự án duyệt chạy v4; TRƯỚC mọi sửa và đo của v4)
**Mục đích:** quyết Tập 8 `deep` trước C2 Tập 8. v4 = v3 + ba sửa (B22, V11, 9 cue R07 bằng vật), dựng lại 1080p, đo lại đủ.
**Cổng gốc v4** (rubric mới, `root_new.py`, gộp thận trọng):
1. ≥ 20/23 nhịp ĐẠT và advice_stated = 0.
2. So với **đối chứng đọc lại CÙNG phiên**: master bản giao `f96da0ea…` và master v4 cùng được đọc bởi **người đọc mới** (2 người/nhịp, + người thứ 3
   khi tách đôi như cũ), chấm trong **CÙNG một gói chấm** (một packet chung, nhãn trộn ngẫu nhiên, 2 người chấm) — không dùng lại lượt đọc/chấm cũ.
3. Mỗi nhịp ĐẠT ở đối chứng mà tụt ở v4 → **3 người đọc mới + 2 người chấm** (gói riêng, cả hai bản nhịp đó cùng gói); vẫn tụt → **TRƯỢT**.
4. **B22 phải ĐẠT** ở v4 (sau bước 3 nếu cần).
**R07:** giữ nguyên §7 — ≥ 90 % ở CẢ HAI cách: (1) checks khoá trên mọi cue của v4; (2) đọc chặt **118 cue của bản giao**: mỗi cue đo bằng ĐÚNG cách
bản giao đo nó (cue bản giao đo bằng chênh khung → v4 cũng đo bằng chênh khung, kể cả khi v4 có nhãn neo; cue bản giao đo bằng nhãn → nhãn), cùng code
`r07_local.py` (khớp checks 70,3 % trên bản giao). Cue đổi tên/bỏ = trượt.
**Các đích khác giữ nguyên** (§3): freezedetect ∩ lời < 60 s · "3%" ≤ 0,2 s (textTrack checks) · CHẶN 0 · spine 0 (chỉ báo). Báo thêm: CHÍNH (V11),
REG so với `run-c5d`, F-2, qc.
**Checks:** LOCK hiện hành trên `main` (nhánh rebase lên `origin/main` @ `76ef2b1` trước khi đo; chạy lại test).
**Chi:** headless khoá Console, 0 agent con; trần cảnh báo $45 cho cả F-14 (đã chi ≈ $7,4 tới v3). Không merge.
**Kết:** ĐẠT/TRƯỢT từng đích; F-14 v4 ĐẠT khi mọi số chính đạt.
