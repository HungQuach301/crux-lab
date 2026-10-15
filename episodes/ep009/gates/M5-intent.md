# M5 Tập 9 — ý đồ kiểm định (ghi TRƯỚC khi có nháp màu; REVIEWER soát trước khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-15, chặng sau G1 (trần **$15 cứng** Console). Main đã gộp: 5c8093ac (Tập 8, F-17 `cine`, F-18 J/L + `sfx_real` + `aac_true_peak`, LOCK K4.4.1 `eb6d0fce…`).
**Bản đo:** (a) nháp 540p MÀU = `CRUX_GREY=0` mười đoạn thế giới (`world/seg/a1 a2 b1 b2 c d1 d2 e f1 f2`: sáu đoạn chương, bốn chương tách ở cảnh đinh) → `build.sh episode.yaml` → `out/video.mp4` (`prod/build_inputs.py --out`); (b) **1080p có lớp `cine`** (cùng mã, `--res 1080`; dựng chạy tiếp được, cache cảnh) — lần dùng `cine` đầu tiên (`episode.md` §1, F-17): **checks ĐỦ BỘ chạy trên (b)** để đo V12; nếu G2 không đổi hình/lời, (b) là bản M6 (1080p một lần).
Thứ tự: (1) checks đủ bộ (b) → (2) cổng gốc trên (a) → (3) nhớ lại + chỗ muốn tua (a) → (4) nhịp + liền mạch (a) → (5) lượt đạo diễn (a, chẩn đoán) → sửa ≤ 2 vòng/lỗi → (6) gói G2 + REVIEWER.

## 1. L1 — checks ĐỦ BỘ gồm bộ lấy mẫu trang, LOCK `eb6d0fce…` (K4.4.1)
`EP=episodes/ep009 bash toolkit/checks_split.sh /home/user/chk-ep009` (`RESUME=1` khi bị cắt; `K_JOBS=4`). Không chạy song song với render.
- **CHẶN dự kiến do hợp đồng đã biết (ghi trước):** S01, S05 (`model.kind` `rent-buy-twin-replay` chưa có trong KINDS — khiếu nại A48 Tập 8 chưa xử lý ở lô K; thêm chế độ quỹ cổ phiếu mới). **Mọi CHẶN khác là trượt thật.** Không thêm `allowTerms`/ngoại lệ sau khi thấy kết quả.
- **V12 (nền sau chữ trên video có lớp)** + bước `cine` của build_seg (ΔE2000 màu dữ liệu ≤ 5, không đảo độ sáng): ghi riêng cho 4 đoạn có lớp (a1, b1, d1, f2). Trượt → sửa ở cảnh (≤ 2 vòng) hoặc tắt lớp ở cảnh đó (trước/sau vào G2).
- **L1 âm:** lời/tiếng dữ liệu 1–4 kHz p10 ≥ 20 dB với `data_db` 34 (luật Tập 9). **AAC true peak ≤ −2,0 dBTP** (`audio.aac_true_peak`). −14 LUFS ±0,5.
- Kết quả theo cấp → `gates/M5-checks.md`.

## 2. Cổng gốc tắt tiếng trên nháp — CHẨN ĐOÁN (luật chủ dự án 14/10, A32 = 1a; giữ cho Tập 9)
27 nhịp loại 1 (`story/beats.md`), cùng tham số dải như animatic M2 (`prod/root_gate.py`), 2 người đọc mới/nhịp, 2 người chấm mới, gộp thận trọng. Điểm = lượt đọc đầu. So với animatic xám M2: nhịp lật (đạt → trượt hoặc ngược) nêu ở G2 kèm khung trước/sau ghép cạnh. `advice_stated` > 0 → sửa (khuyên là lỗi, không phải chẩn đoán).

## 3. Nhớ lại + chỗ muốn tua (Đạo diễn sáng tạo, Editor — mù, headless)
3 người đọc mới: 4 tấm × 12 khung theo hồi + toàn văn lời có mốc giây. Nhớ lại: K1/K2/K3 của `preprod/TAM-NHIN.md` §1 + câu hỏi của phim (chỉ báo). Chỗ muốn tua: "Where would you skip ahead, if anywhere? Give the time." — **không cảnh nào ≥ 2/3** (phép thử Editor); trượt → sửa nhịp/hình (≤ 2 vòng), không đổi lời.

## 4. Nhịp (Editor) + liền mạch (Giám sát), máy + tay
- freezedetect (n 0,003, d 3 s) trên nháp: tổng giây đứng hình CÓ LỜI ≤ 30 s; quãng có lời không đổi hình > 8 s (spine `f14`) = 0 → liệt kê.
- J/L-cut: 7 chuyển khai (`kit.CUTS`: S05 L, S08 J, S14 J, S16 L, S19 J, S22 J, S25 L; offset 0,4 s ≤ 0,5 s) → `splice.py --transitions` → R09 chỉ báo; A/V lệch ngoài vùng J/L = 0 khung.
- 3 số neo (S04.3, S14.3, S15.2): vật thể đổi trong ±1 s; lặng trước số neo 0,7–1,0 s (take dẫn xuất `prod/anchor_gap.py`, không đổi lời).
- Màu lựa chọn: buyer = LIT, renter-cash = warn, renter-stocks = accent (N6, dòng/nhãn stocks) — đúng ở bảng điểm kết; cine ≤ 30 % thời lượng (ghi tỉ lệ thật).
- SFX thật (`sfx_real`, kho CC0 RIGHTS §G1): không tệp lặp trong 60 s, mật độ ≤ 4/10 s (thin_events).
- Nguồn trên hình: dòng nguồn góc (rút gọn) + câu nguồn cổ phiếu của chủ dự án 15/10 trên thẻ giới hạn S24.

## 5. Lượt đạo diễn (chẩn đoán, D-010 §6) — 1 lượt headless, 4 tấm × 12 khung + lời; lời phê chỉ thành việc khi phép thử của vai sở hữu cũng trượt.

## 6. Điều kiện G2 ngoài máy (lệnh chặng)
- **Content ID "Origami":** phiên không có tài khoản YouTube → gói G2 nêu cách kiểm (tải bản nháp RIÊNG TƯ lên YouTube Studio, xem mục Copyright; trang "YT Content ID Claims" của tác giả nếu có claim) — **chủ dự án làm, trước G3**; ghi công đúng mẫu ở mô tả (M6).
- A14 S02 "3 in 4" → ASR "three and four" (2 seed) → câu hỏi G2 (đề xuất "3 out of 4", tiền lệ G2 Tập 8).
- Độ dài 8:44 < 9:00 `lab` (G1: không độn, `--g1-short`) → nêu một vế ở G2.

**Chi dự kiến (Console):** cổng gốc M2 ≈ $2,3 · REVIEWER ý đồ ≈ $0,7 · cổng gốc nháp ≈ $2,3 · nhớ lại + tua ≈ $0,5 · đạo diễn ≈ $0,3 · REVIEWER G2 ≈ $0,9 → ≈ $7; đã chi ≈ $1,1 (WRITER v5 + kiểm mù r5). **Ngắt:** tổng chặng chạm $13,5 → bỏ bước chẩn đoán còn lại (đạo diễn, cổng gốc nháp), giữ REVIEWER G2; chạm $15 → dừng hỏi.

## Sửa theo REVIEWER (`gates/REVIEW-M5-intent.md`: ĐẠT có sửa, 1 CHẶN + 5 CHÍNH + 7 PHỤ — áp đủ, TRƯỚC khi chạy; REVIEWER $0,37)
- **C1 (§6):** kiểm Content ID là **điều kiện G2**: gói G2 **chưa đạt** cho tới khi chủ dự án báo kết quả (0 claim, hoặc claim đã gỡ theo hướng dẫn tác giả). Bản tải riêng tư = (b) 1080p có nhạc "Origami". Gói G2 để sẵn ô kết quả.
- **CH2 (cine):** 5 cảnh đinh khai lớp (giờ lời thật 15/10): H1 S01–S02 (5,9 + 16,8 s), H2 S04 (32,4 s), H3 S14 (29,0 s), H4 S15 (19,8 s), H6 S25 (32,4 s) = **136,3 s = 26,0 % của 523,9 s** (≤ 30 % = 157 s; tính TRƯỚC khi dựng). Vượt → bỏ lớp ở cảnh trước khi dựng (b). (Đoạn có lớp: a1, b1, d1, f2.)
- **CH3 (§1):** CHẶN dự kiến theo A48 (ghi trước, theo ID luật): **S01, S05** (MISSING: kind `rent-buy-twin-replay` chưa có trong `r_model.py KINDS`), **S04** (MISSING: tính lại đối chiếu) và **S03** ("cross-check host") nếu cùng gốc A48. Luật khác trượt ở các cảnh đó = trượt thật.
- **CH4 (§4):** "có lời" = chồng vùng stem giọng > −45 dBFS. Quãng có lời không đổi hình > 8 s: **ngưỡng 0**, trượt → sửa ≤ 2 vòng (máy tiến/vật đổi trạng thái), không đổi lời.
- **CH5 (§4):** lặng trước số neo **0,7–0,9 s** (§5b).
- **CH6 (M6):** nếu (b) thành bản M6: SSIM so nháp ≥ 0,97 **chỉ cho cảnh không `cine`**; cảnh có `cine` đo bằng bước `cine` (ΔE2000 ≤ 5, không đảo độ sáng). Lý do ghi trước cho lần 1080p thứ hai: G2 đổi hình hoặc lời (Line producer).
- **P7:** §2–§3 đo trên (a) không lớp — giới hạn của phép đo, ghi ở G2. **P8:** nhịp ĐẠT ≥ 0,8 và không `advice_stated`; `beats.md` blob `4ee535630798`, `root_gate.py` blob `05baa2eb2e8e` (cùng cho M2 và M5). **P9:** liền mạch thêm "số trên hình = lời"; J/L: 7/7 đúng kiểu khai, offset trong ±0,5 s. **P10:** sửa V12/ΔE → chạy lại luật + bước `cine` trên cảnh sửa rồi mới G2. **P11:** câu nguồn S24 khớp nguyên văn câu chủ dự án 15/10; `sfx_fetch --verify`; mỗi tệp SFX có dòng RIGHTS §G. **P12:** đã chi thực tới đây: WRITER v5 $0,75 · kiểm mù r5 ≈ $0,3 · REVIEWER ý đồ $0,37; dự phòng vòng sửa ≈ $2; ngắt 150 % ngân sách mốc. **P13:** kiểm `data_db: 34` + `aac_true_peak` trong `episode.yaml` trước (a); G2 dùng `templates/L3.md` + 3 khung 1080p cảnh đinh.
