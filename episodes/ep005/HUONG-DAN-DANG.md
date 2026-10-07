# Hướng dẫn đăng — Tập 5

Bản nháp C5 (bên dựng, 07/10/2026) theo `playbook/templates/HUONG-DAN-DANG.md`. **Chưa đăng được:** checks C5 còn 5 luật CHẶN trượt (S07, S08, S09, S10, S17 — xem "Chặn" dưới) và G2 chưa trả lời. Mục "File" điền lại sau giao hàng (`deliver.py`).

## File
- **Video:** `ep005-youtube.mp4` — ghép các phần trên nhánh tạm `ep005-delivery` theo `JOIN.md` (chưa giao). Bản gốc 1080p `out/video.mp4` SHA-256 `6306869610ffcdbc10a0685e2b3700229b296ab644bc2fe1d0489918d59c6692` (7:44,5; −14,0 LUFS, −1,9 dBTP). SHA bản 8 Mb/s ghi khi giao.
- **Tiêu đề:** **T1** "10% Down and Mortgage Insurance: How Long Did It Last?" (G1).
- **Mô tả và chương:** `episodes/ep005/out/package/description.md` — dán nguyên văn; 6 chương `m:ss Tiêu đề` từ 0:00 (0:00 · 0:58 · 3:07 · 5:20 · 7:13 · 7:24); nguồn FRED (MORTGAGE30US, HPIPONM226N, kiểm chéo OBMMIC30YF, CSUSHPINSA, MSPUS), 12 U.S.C. 4901/4902, Fannie Mae B-8.1-04 (chỉ khoản vay Fannie Mae), CFPB; "Not modeled"; "US only · history, not a forecast".
- **Phụ đề:** `episodes/ep005/out/captions.srt` (tiếng Anh).
- **Thumbnail:** đề xuất **thumb-1** ("23 months / on paper / is not the same as removed") mặc định; **Test & Compare:** thumb-1, thumb-3, thumb-2 (`out/package/thumb-1..3.png`, claim từng dòng chữ trong `thumb-N.json`). Không số tiền phí bảo hiểm (R1).
- **Mid-roll:** `out/adbreaks.json` **3:04 (184,3 s)** — ≥ 2 phút từ đầu/cuối; lưu ý checks S14 (THAM KHẢO): cách ranh giới hồi 187,8 s quá 1 s và không có lặng ≥ 1 s trong bản trộn 1080p (âm phòng/nhạc của đoạn thế giới lấp khoảng lặng C4).
- **Shorts:** `out/shorts/SH1..3.mp4` (không commit; dựng lại bằng `bash toolkit/build.sh episodes/ep005/episode.yaml`), tiêu đề trong `out/shorts/README.md`: SH1 S11 (22,7 s) · SH2 S13–S14 (37,8 s) · SH3 S16–S17 (43,5 s). Mỗi Short gắn link video chính (Related video).

## Trước khi bấm đăng: claim có hạn dùng
- **Lãi "tháng đủ tuần mới nhất" = September 2026 (6.86%)** và các số theo lãi đó (`sched80_months_latest` 99 kỳ ≈ 8 năm, `sched78_months_latest` 114, `ex_payment_pi` $2,362): hình và lời đều ghi tháng (September 2026) nên là số lịch sử có ngày, **giữ nguyên** dù đăng sau tháng 10/2026. Không cập nhật số.
- **Chỉ số FHFA** (dữ liệu tới 07/2026; FHFA sửa số cũ mỗi tháng): mô tả và thẻ phương pháp nói "history"; giữ nguyên.
- **12 U.S.C. 4902 / Fannie Mae B-8.1-04:** nếu luật hoặc Guide đổi trước ngày đăng → dừng, hỏi lại (sai nghĩa).

## Chặn (chưa đăng được) — `out/checks/run-c5/report.md`
- **S10** (câu khuyên trên hình: "buy now + mortgage insurance", "keep renting, keep saving" ở S01) · **S17** (34 khung S14 299–300 s: nhãn "October 2005: 112 months" thiếu "on paper") · **S09** (gốc $ "nominal" chưa nói trong lời + 580 khung thiếu nhãn gốc) · **S08** (89 khung: số "90" ở S01–S02 khớp claim minh hoạ `buyer_victor_sched80Months` mà không có ILLUSTRATIVE) · **S07** (102 số trên hình + 24 số trong lời chưa có claim: vạch trục, 10/20/78/80 percent, 1991/2016). Đều nằm trong hình/lời đã khoá nghĩa ở C4 hoặc sổ claim → chủ dự án/phiên K quyết.

## Giữ nguyên (CHÍNH có giải thích) — `out/explanations.json`
F07 (464,5 s < 480 s, 101 không độn) · V03 (chữ lệch vùng an toàn 2–85 px) · V08 (tương phản 3,35:1 nhãn "80%") · V09 (màu ba người mua) · V11 (nhãn chạm đồ hoạ) · V12 (3 mẫu chữ mờ khi máy bay) — đều là sửa hình sau khoá nghĩa, chờ chủ dự án chọn ở G2.

## Sau khi đăng (G3)
- Ghi link video, ngày đăng vào `episodes/ep005/audience.md`.
- Báo phiên đã tải xong → phiên merge `ep005` vào `main` và xoá `ep005-delivery` (proxy chặn xoá → chủ dự án xoá: GitHub → Branches → Delete).
- Mốc 7 ngày: một ảnh chụp YouTube Studio cho chat chiến lược (`playbook/templates/audience.md`).
