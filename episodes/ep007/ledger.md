# Ledger — Tập 7 (#13, 15 năm vs 30 năm trả trong 15)

| Ngày | Cổng | Loại việc | Lệnh / agent | Ra | Token / chi | Kết quả |
|---|---|---|---|---|---|---|
| 2026-10-11 | BƯỚC 0–1 | điều phối | merge `tongket-t6` → main (1a69c71); áp câu trả lời tổng kết (nhánh `tongket-t6-answer`, c586128) → main a6c2f93 | `tongket-t6/ANSWER.md`, `F14-brief.md` | — | verify.sh ep007 ĐẠT |
| 2026-10-11 | Việc 0 | dữ liệu | `data/fetch.py` | `data/sources.json` | — | PMMS 1.833 tuần ghép 1991-08-30 → 2026-10-08; đối chiếu OB 510/510 (≤ 0,5 điểm); ghim hồ sơ SHA khớp, +2 tuần |
| 2026-10-11 | Việc 0 | mô hình | `model/model.py`; calc.py hồ sơ trên ghim 18/18 | `out/model.json`, `numbers.md` | — | 57 đại lượng |
| 2026-10-11 | Việc 0 | kiểm độc lập | `toolkit/api.sh review briefs/independent.md` (Opus, khoá Console) | `model/independent/report.md` | $0,28 | **57/57 khớp** (5 do làm tròn → đô la nguyên) |
| 2026-10-11 | Việc 0 | EL | `GET /v1/user/subscription` → 401 (khoá thiếu quyền `user_read`); `GET /v1/usage/character-stats` đọc được | — | — | đã dùng 60 ngày 280.042 ký tự; tháng 10 đến 09/10: 71.409; giới hạn/ngày làm mới: không đọc được |
| 2026-10-11 | C1 | kiểm mù | `blind.py` 6 người đọc + 1 chấm (Sonnet headless, khoá Console) | `c1/r1/`, `gates/C1-logline.md` | xem C1-logline | L1 3/3 · L2 3/3 · khuyên 0 · overclaim 0 → **L1** (luật hoà) |
| 2026-10-11 | hồ sơ #13 | dữ liệu | bổ sung `model.json`, `statements.json`, `calc.py --statement` | `topics-r2/machine/debt-1/CHECK.md` | — | §4 ĐẠT, 11/11 True |
| 2026-10-11 | Tập 8 | hồ sơ #20 | `toolkit/api.sh build briefs/t8-dossier.md` (Opus) | `topics-r2/machine/rent-buy-1/` | $2,36 | §4 ĐẠT 4/4; 11/11 True (chạy lại); rủi ro: tiền thuê ban đầu giả định |
| 2026-10-11 | Tập 8 | C1 | `blind.py` 3 người đọc + chấm | `c1-t8/r1/` | ≈ 15 nghìn | logline 3/3, khuyên 0 |
| 2026-10-11 | C2 | WRITER | `toolkit/api.sh build briefs/writer-c2.md` (Opus) | `story/` v1 | $3,34 | checker ĐẠT 10:36 |
| 2026-10-11 | C2 | kiểm mù r1 | 6 Sonnet + chấm | `c2/r1/` | xem C2-blind | đúng 6/6 · khuyên 0/6 (đúng rubric 5/6) · phương pháp 6/6 |
| 2026-10-11 | C2 | WRITER mới r2 | `briefs/writer-c2-r2.md` | `story/` v2 | $0,91 | S32 rút; checker ĐẠT 10:05 |
| 2026-10-11 | C2 | kiểm mù r2 | 6 Sonnet + chấm | `c2/r2/` | 2 vòng ≈ 0,17 triệu, $0,60 | đúng 6/6 · khuyên 6/6 · số dày 3/6 |
| 2026-10-11 | C2 | REVIEWER | `briefs/reviewer-c2.md` (Opus) | `gates/REVIEW-C2.md` | $1,06 | ĐẠT có sửa: 1 CHẶN (gói), 6 CHÍNH → áp v3 (checker ĐẠT 9:53) |
| 2026-10-11 | G1 | bản đọc thử | `story/table_read.py` (EL Eric) | `review-g1/` | EL 973 + 260 | M2 30,6 → rút S02.2 → 29,8; M1–M6 ĐẠT |
| 2026-10-11 | G1 | tiêu đề | `blind.py` 3 người đọc | `c1/titles/r1/` | ≈ 15 nghìn | T2 3/3 |
| 2026-10-11 | việc treo | thị trường | discover/pull/classify/analyze/report (Haiku/Sonnet Console, YouTube ≈ 7.300 đv) | q01, q17, `market/REPORT.md` §4 (cherry-pick main 4e72338) | — | `analyze.all_videos` lọc kênh Crux; q17 khoảng trống vừa → cao; §4 ~15 phút (11–18) vs ~12 |
| 2026-10-11 | G1 | REVIEWER | `briefs/reviewer-g1.md` (Opus) | `gates/REVIEW-G1.md` | xem tệp | ĐẠT có sửa: 6 CHÍNH → áp |
| 2026-10-11 | G1 trả lời | điều phối | P2: verify.sh ep007; merge `origin/main` (2 commit) vào ep007; chép câu trả lời | `gates/G1-answer.md`, `taste-ledger.md`, `AUTHORSHIP.md`, CHARTER §5 dòng G2 | — | áp G1: #13 L1 · (a) kiểm mù vòng 3 rubric MỚI · mốc ngày thay "this week" · T2 · N1 duyệt |
| 2026-10-11 | G1 câu 2 | WRITER (điều phối, sửa máy) | mốc tuần dữ liệu thay "this week": S01.2 bỏ, S03.1 ngày đầy đủ, S07.2/S09.3/S12.2/S21.2/S23.2 "October 8", S33.3 ngày đầy đủ; hình B01/B03/B32/B33; checker miễn đúng ngày `last_week` | `story/`, `numbers.md` | — | checker ĐẠT, M2 ước 26,3 s, 10:01 |
| 2026-10-11 | C2 vòng 3 | kiểm mù | `blind.py` 6 Sonnet + 1 chấm (headless khoá Console), rubric MỚI, câu 8 nguồn khuyên | `c2/r3/`, `gates/C2-blind.md` | đọc 67.796 token + chấm | đúng 6/6 · `advice_stated` 0/6 → QUA · inferred 1/6 · số dày S21–S24 3/6 → S21.2/S23.2 số lên hình (ước 9:54) |
| 2026-10-11 | EL | hạn mức | `GET /v1/user/subscription` (quyền `user_read` đã bật) | — | — | creator: đã dùng 63.494 / 144.034 → **còn 80.540 ký tự**, làm mới 2026-11-01 06:57 UTC; đủ Tập 7 (≈ 8.600) + Tập 8 |
| 2026-10-11 | C3 | dựng | `toolkit/api.sh build briefs/builder-c3.md` (Opus, khoá Console) | `world/`, `review-c3/` | đang chạy | 5 đoạn: s01-stack, s06-stack, s21-track, s23-track, s25-bar |
