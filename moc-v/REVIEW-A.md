# Mốc V · Phần A — REVIEWER (06/10/2026)

Phạm vi: `decisions/D-009.md`, `moc-v/BASELINE.md`, `moc-v/RESULTS-A.md`, `moc-v/eval/ROOT-intent.md` + `blind1–5-raw/`, `director-*.md`, `sync-*.json`, `moc-v/measure/`, `moc-v/proto/` (spine.py, audio.py, A/a.js, B/b.js, C/c.js, lib2d.js, data.json, B/NOTES.md), `moc-v/assets/SOURCES.md`, `moc-v/PLAN.md`, diff nhánh, `moc-v/review/compare.mp4`.

## Kết luận: **ĐẠT, có điều kiện**

Không có lỗi CHẶN. Cụ thể:
- Không sửa `checks/` và không đụng `episodes/ep005/` (`git diff origin/main...HEAD` ngoài `moc-v/` chỉ có `.gitignore` và `D-009.md`).
- Không mua gì.
- Ý đồ kiểm mù được commit trước kết quả và không sửa sau đó.
- Không có chỗ nào gọi 0,5 là "đạt".
- Mọi số trên màn hình đều lấy từ claim của Tập 4.

Có **7 lỗi CHÍNH**. Theo tinh thần D-009 thì phải sửa trước khi gửi Gói A. Cả 7 đều là sửa chữ hoặc commit bằng chứng, không phải dựng lại.

## Đã kiểm và khớp

- **BASELINE, số đo khung hình.** Chạy lại `summary.py` trên `measure/raw/*.json` ra đúng `baseline-frames.jsonl` và bảng: 2,2/3,4/7,3/40,0 %; 128/33/47/117 từ/phút; 35,9/21,0/8,6/10,4 %.
- **BASELINE, timeline Tập 4** (tính lại từ `timeline.json`):
  - `title` 131,6 s = 27,3 %, 13 thẻ;
  - `bignum` 28,0 s = 5,8 %;
  - `method` + `endcard` 17,5 s;
  - 36 cắt, 25 cắt giữa hai mẫu khác nhau.
- **BASELINE, các nguồn khác.**
  - `transitions.json`: Tập 1 có 30 cắt, Tập 2 có 31, Tập 3 có 12.
  - L3 Tập 1 4·5·4·4·4·4 (sổ gu dòng 64).
  - Tập 3 "mấy phút đầu chưa đủ thu hút" (dòng 83).
  - Tập 4 cổng gốc 3/7 → 6/7 (`ep004/gates/C4-root-r2.md`).
- **Độ lặp nhạc** (chạy lại `d_music_selfsim.py`, tempo map 114 BPM):
  - nhạc nền Tập 4: 56 cặp, TB 0,873, 25 % cặp ≥ 0,90;
  - nhạc mã đoạn thử: 7 cặp, 0 %;
  - Eleven Music: 7 cặp, 0 %.
- **Cổng gốc.** Đối chiếu `key.json` × `grade-labels.json` × `grade.json` cho cả 5 vòng, khớp từng ô của RESULTS-A §Cổng gốc:
  - R: K1 1·1, K2 1·1;
  - A/C: K1 0,5·0,5 ở v1, v1b và vòng tham khảo; K2 1·1;
  - B v1: 0,5·0,5 cả hai nhịp;
  - B v2: K1 0,5·0,5, K2 1·1;
  - 0 cờ khuyên.
- **Thứ tự commit.** `ROOT-intent.md` nằm ở commit b9a3fad (14:39), trước grade vòng 1 (697c97d, 14:52), và không có lần sửa nào sau đó.
- **Đạo diễn.** Điểm R/A/B/C ở v1 và v2 khớp bảng cuối từng file `director-*.md`.
- **Đồng bộ.** `sync-A/B/C.json` cho 11/12, 8/12, 9/12. Các độ lệch của B là +0,37 / +0,24 / −0,21 s. C có max 0,081 s.
- **Âm.**
  - `spine.json` có 90 nốt dữ liệu và 24 sự kiện sfx.
  - Tổng ký tự của 4 take giọng: 50 + 276 + 482 + 209 = 1.017.
  - Audio report: lời trên nhạc 23,96 dB, −14,0 LUFS, −1,5 dBTP, âm dữ liệu −3,5 dB.
- **Claim trên hình.** Tám claim trong `proto/data.json` trùng cả giá trị lẫn cờ `historical`/`illustrative` với `episodes/ep004/out/claims.json`.
  - Chuỗi lãi cắt mức $500k ở 2022-04, xuống dưới ở 2022-10, rồi ở trên từ 2023-04.
  - A, B, C đều in số qua `CL()` / `claims`.
  - Lớp ILLUSTRATIVE, "US only · history, not a forecast", nguồn và đối trọng đều có (`lib2d.chrome`).
  - Lời không khuyên, không dự báo; "we" là người phân tích.
- **Render.** `work/*.render.json`: A 1,08, C 1,02, B-code v2 8,68, B-cc 10,45 s máy / 1 s phim. B v1 12,79 (theo NOTES).
- **compare.mp4.** 360,6 s, 1280×720, H.264 + AAC, 30 fps, faststart. Có 5 phần R/A/B/C/C+AI, mỗi phần có thẻ tên.
- **`.gitignore`.** Bỏ qua `moc-v/proto/vendor/` (node_modules) và `moc-v/work/` (video nặng). Hợp lý, nhưng xem C5.

## Phát hiện

### CHÍNH

**C1 — RESULTS-A nói "mốc giờ không gõ tay", nhưng mã có hàng chục mốc gõ tay** (`moc-v/RESULTS-A.md:4`, `moc-v/proto/spine.py:4`).
- RESULTS-A viết: "mọi mốc giờ lấy từ alignment… đồng bộ do cấu trúc".
- Thực tế mã hình có nhiều giây gõ tay:
  - `A/a.js:107,228` (63.2, 64);
  - `C/c.js:33,99,116,120,209,215,222,223,232` (13.6, 56.4, 62.9, 63.0, 63.2…);
  - `B/b.js:328` (33.94, 38.9), `:431,451,488–526,558,574` (8.98, 13.0, 29.2, 40.0, 44.5, 55.0–57.5, 63.2, 64.2).
- Đây cũng có thể là một nguyên nhân khiến B chỉ đạt 8/12.
- **Sửa:** ghi đúng là "lịch nhịp lấy từ alignment; hình còn N mốc gõ tay (liệt kê)". Ở Phần B, chuyển các mốc này thành `cue` trong `spine.py`.

**C2 — `SOURCES.md` tự mâu thuẫn về việc gọi API sinh nội dung** (`moc-v/assets/SOURCES.md:3`).
- Dòng 3 viết: "No purchases, sign-ups, or content-generating API calls were made".
- Nhưng gói đã gọi `/v1/music` và commit `moc-v/assets/eleven-music/music.mp3`. RESULTS-A:63 ghi "≈ 1.050 credit".
- Thêm nữa, con số 1.050 là **ước tính** (900 credit/phút × 1,16 phút), không phải số đo.
- **Sửa:**
  - SOURCES.md:3 ghi rõ "1 lần gọi Eleven Music 69,6 s bằng credit của gói EL hiện có (không mua thêm)".
  - RESULTS-A:63 ghi "≈ 1.050 credit (ước tính theo bảng giá, chưa đối soát số dư)".

**C3 — Hướng B chạm gen được bảo vệ "không thế giới 3D" mà gói không nêu** (`CHARTER.md:37`; `decisions/D-009.md:29`; `moc-v/RESULTS-A.md:11,67`).
- B có sân phố, máy quay dolly/push-in, khu nhà 3D, tức là gần "thế giới 3D".
- G-012 chỉ mở đường cho **vật thể thật 3D**, và đó là phương án để chủ dự án chọn.
- Trong khi đó D-009:29 ghi gen được bảo vệ "không đổi".
- **Sửa:** thêm vào RESULTS-A (Đề xuất) và Gói A một dòng: "Chọn B = chủ dự án quyết về gen 'không thế giới 3D' (CHARTER §4, §6). Đề xuất đọc là cho phép *vật thể 3D* trên nền phẳng, không cho phép cảnh/thế giới 3D." Nếu chủ dự án đổi gen thì D-009 phải ghi thêm.

**C4 — Lớp bắt buộc không đọc được trên điện thoại, nhưng RESULTS-A viết nhẹ đi** (`moc-v/RESULTS-A.md:57`, `:19`).
- RESULTS-A viết "đọc khó ở 25 % theo cả bốn đạo diễn".
- Đạo diễn ghi nặng hơn:
  - `director-B-v2.md:93`: "cả năm lớp đều không đạt chuẩn đọc ở 25 %";
  - `director-A-v2.md:72–73`: ILLUSTRATIVE và history/US-only **"Không"**;
  - `director-C.md:82`: "Không đọc được".
- Điều này có nghĩa là gen ILLUSTRATIVE / "history, not a forecast" có mặt về kỹ thuật nhưng không tới người xem.
- Con số "0 % chỉ có chữ" (dòng 19) đạt được một phần nhờ đẩy lớp chữ bắt buộc xuống chrome 40 px. Đây là rủi ro Goodhart (CHARTER §4).
- **Sửa:**
  - đổi thành "không đọc được ở 25 % (đạo diễn A v2, B v2, C v1)";
  - thêm chú thích dưới dòng 19 rằng 0 % đạt được nhờ chuyển lớp chữ bắt buộc vào chrome 40 px, lớp này chưa đạt chuẩn đọc;
  - ở Phần B đo lại sau khi phóng lớp này lên ≥ 48 px.

**C5 — Một số con số trong RESULTS và BASELINE không có bằng chứng trong repo.**
- **Render** (`RESULTS-A.md:33`):
  - các khoảng "0,93–1,08" (A) và "0,78–1,04" (C) không có file nào. `work/*.render.json` chỉ có 1,08 và 1,02;
  - mà `work/` lại bị `.gitignore`, nên cả số đã đo cũng không vào repo.
- **Âm và nhạc** (`audio-report.json`, kết quả selftest nhạc 0 %/25 %): chỉ nằm trong scratchpad phiên.
- **Hiệu chuẩn bằng mắt "48 khung, 46/48"** (`BASELINE.md:5`): không có file.
  - `measure/frames.py:18` còn trỏ tới `moc-v/measure/CALIBRATION.md` (ghi "40 khung"), file này **không tồn tại**.
- **Hàng "nhân vật khi lời nhắc tên"** (`BASELINE.md:18`): `char-hits.json` chỉ ở scratchpad.
- **Sửa:**
  - commit các JSON nhỏ vào `moc-v/measure/` hoặc `moc-v/eval/`: `render-*.json`, `audio-report-{code,ai}.json`, `selfsim-*.json`, `CALIBRATION.md`, `char-hits.json`;
  - hoặc bỏ các khoảng số không có nguồn (A ghi 1,08; C ghi 1,02).

**C6 — Thiếu dòng L3 cho các hướng** (`moc-v/RESULTS-A.md:15–33`).
- Lệnh (3) đòi "measurements of (2)", trong đó có "owner's L3 score and comments".
- Bảng số đo không có dòng L3. Gói A cũng chưa có phiếu L3 để chủ dự án chấm R/A/B/C trên `compare.mp4`.
- Theo D-009 (d), L3 ≥ 4 là ngưỡng mới, nên đây chính là dữ liệu quyết định hướng.
- **Sửa:**
  - thêm dòng "Phiếu L3 chủ dự án: chờ (chấm trên compare.mp4, §8 6 dòng × R/A/B/C)";
  - Gói A kèm phiếu trống.

**C7 — D-009 thêm luật ngoài lệnh mà không tách riêng** (`decisions/D-009.md:8,16,18,23,24`).
- Các điểm vượt lệnh:
  1. "Không có số đo thì coi như làm giảm" (dòng 8);
  2. ở (a), "chủ dự án chọn" khi có ngoại lệ (dòng 16). Lệnh chỉ đòi "nêu rõ";
  3. "không bỏ lượt đạo diễn" là bước chất lượng (dòng 18), và "thêm lượt đạo diễn trước render" vào `episode.md` (dòng 24). Lượt đạo diễn là bước mới của Mốc V, chưa có trong playbook;
  4. "cổng gốc sửa bằng hình trước, nhãn chữ là cách cuối" / sửa §6.6 (dòng 23). Điểm này rút từ nguyên nhân gốc, không có trong lệnh.
- Các ý có thể hợp lý, nhưng hiện chúng nằm lẫn trong bản "ghi lại lệnh của chủ dự án".
- **Sửa:** chuyển 1–4 sang mục mới "Đề xuất thêm của phiên (ngoài lệnh, chủ dự án duyệt riêng từng ý)". Phần "Thay" chỉ giữ đúng 4 điểm của lệnh.

### THAM KHẢO

- **T1. Ghi lý do tách vòng "tham khảo"** (`RESULTS-A.md:43`). B v2 (blind5) được tính chính thức, còn A v2 / C v2 (blind4) chỉ là "tham khảo". Lý do có lẽ là giới hạn tối đa 2 vòng (CHARTER §5), vì A và C đã có v1 + v1b. Nên ghi rõ lý do này, nếu không người đọc sẽ thấy hai cách đối xử khác nhau. `ROOT-intent.md` cũng không ghi trước số vòng; Phần B nên ghi.
- **T2. Nêu thẳng kết quả cổng gốc** (`RESULTS-A.md:35–45`). Nên có một câu tóm: "Theo ngưỡng ghi trước, **không hướng nào đạt**. Bản phát hành R đạt cả K1, K2, vì R dùng nhãn chữ."
- **T3. Đồng bộ ±0,2 s cần đặt cạnh nhận xét của đạo diễn** (`RESULTS-A.md:32`).
  - Đạo diễn v2 vẫn thấy lệch 0,3–1,7 s ở A và C (nhãn Q2 2022 +1,7 s, thud/impact +0,3 s), vì `sync_audit` chỉ đo 12 sự kiện chọn trước.
  - Cột R dùng phương pháp khác (đạo diễn), không so được trực tiếp với A/B/C.
  - B còn 1 sự kiện không đo được (b11.x), chưa ghi.
- **T4. Dòng "% đồ hoạ chuyển động" là cận trên** (`RESULTS-A.md:21`). Nên ghi "cận trên của 'mang nghĩa'" như BASELINE. Ngoài ra, 0 % lặp trên 7 cặp không so được về thống kê với 25 % trên 56 cặp của cả tập.
- **T5. So nhà 3D lệch phiên bản.** `B-cc.mp4` vẫn là v1, còn `B-code` là v2 (`proto/B/NOTES.md:33`). `compare.mp4` không có B-cc. Nhánh so mô hình 3D có giấy phép với bản mã chỉ có ảnh `work/B-cmp.png`, không vào repo. Bản so nhạc (C với C+AI) thì đủ. Nên ghi điều này.
- **T6. Quyền Starter là cách hiểu, chưa xác minh** (`SOURCES.md:59`). Câu "Starter has no rights to music streaming platforms (not relevant for YouTube)" là cách hiểu, không phải điều khoản nguyên văn. Docs EL (dòng 94) cũng nói "film and television", trái với bảng "except film, TV". RESULTS-A:63 nên ghi "cần xác nhận YouTube không thuộc 'streaming platform' ở gói Starter".
- **T7. Nhận xét Tập 4 không phải của chủ dự án** (`BASELINE.md:26`). Ô "Nhận xét chủ dự án" của Tập 4 ghi "hook 2 · nhịp 3". Đó là điểm của **tóm tắt AI** (`ep004/gates/G2.md:6`), nên ghi rõ. Tập 2 "phát hành CÓ, không chấm từng dòng" nên dẫn nguồn `episodes/ep002/ledger.md:80`.
- **T8. Câu trích trong D-009 chưa có nguồn** (`D-009.md:16`). Câu trích "không cần quá hoàn hảo" không tìm thấy trong repo. Cần dẫn nguồn (issue hoặc lệnh) hoặc bỏ ngoặc trích.
- **T9. Hai điểm D-009 chưa nói tới.**
  - Trần **agent** (D-008, "≤ 25 agent") và D-008 §4 ("vượt trần → chat chiến lược") có cũng chỉ là cảnh báo không.
  - D-009 "có hiệu lực từ Tập 5" trong khi Tập 5 đang chạy (K3.9 đã merge), vậy có áp cho các cổng Tập 5 đã qua không.
  - Hàng 5 của phiếu L3 ("Giọng") không có tham chiếu, nên "so với ba tham chiếu" ở (d) cần nói rõ cách hiểu.
- **T10. Nhánh chậm hơn main.** Nhánh `moc-v` thiếu 3 commit của `origin/main` (K3.9, `verify.sh`: "main mới nhất TRƯỢT"). Diff hai chấm `origin/main..HEAD` vì vậy hiện cả `checks/`, nhưng đó là thay đổi phía main. Diff ba chấm xác nhận nhánh này không đụng `checks/`. Cần merge main trước Phần B.
- **T11. Chưa báo token.** Gói A chưa báo token / agent đã dùng so với trần (CHARTER §8). D-009 (c) cũng yêu cầu ghi số thực.
- **T12. Đoạn thử dài 69,6 s** so với "~60 s" trong lệnh. Chấp nhận được (trọn câu S04.5 → S07.3), nên ghi lý do một dòng.

## Những gì lệnh đòi mà Phần A còn thiếu
- Phiếu L3 cho các hướng (C6).
- Gói A (≤ 10 dòng) và issue nhắc chủ dự án (PLAN bước 4). Đây là bước tiếp sau REVIEWER, chưa phải lỗi.
- Các mục còn lại của lệnh (1), (2), (3) đều có mặt.
