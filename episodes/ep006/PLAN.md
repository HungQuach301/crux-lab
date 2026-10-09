# PLAN Tập 6 — Does a 2% Annuity Raise Really Keep Up With Prices?  (≤ 1 trang; viết lại khi đóng phiên)

**Nhánh:** `ep006` · **Đề tài:** #12 · **Format:** `101` · **Phiên vừa đóng:** P3b (`session_01426YSqdhTHTztxkQ5Ax1jg`) — đóng **giữa C4** theo lệnh chốt an toàn (hạn mức tuần ≈ 6 %) · lịch sử: `archive/PLAN-history.md`

## 1. Trạng thái
F-12 + K4.0.2 + K4.1 trên `main` (9f16de0) và `ep006`; LOCK `4d688acd` khớp. `contract.json` (kind `fixed-raise-vs-index-windows`, `index.name: cpiu`): S01 89/0, S05 45/45 + 8/8. **Animatic 720p cả tập** (6 đoạn thế giới a–f): **536,6 s = 8:56,6** (≤ 9:00, dư 3,4 s), MR1 208,15 s, giọng 30/30 cache, EL 0; vòng sửa 1 bố cục xong, dựng lại @ ddf5bf1 (6/6 verify). F-13 (mux `-shortest` rơi khung) sửa trên `ep006`, bằng chứng `c4/f13/EVIDENCE.md`. **Kiểm mù C4** (rubric MỚI theo `gates/C4-answer.md`): bản có lời cả tập 0/3 · S29 0/3 `advice_stated` → **chốt C3 ĐẠT**; cổng gốc vòng 0 (trên bản trước sửa): `advice_stated` chỉ B08; nghĩa 0,5 ở B01 B03 B15 B32. Checks lần 1: luật Python — CHẶN còn F01 (720p) và F11 (chốt ở C5); đủ bộ (gồm trang) trên bản sửa: xem §2.1.

## 2. Việc tiếp (≤ 3) và việc treo
1. **Checks đủ bộ lần 1** trên bản @ ddf5bf1: nếu chưa có `checks-runs`/báo cáo commit thì chạy lại khi máy rảnh: `bash episodes/ep006/c4/checks.sh <ngoài repo>/chk-c4 --first` (≈ 1–2 h, bộ lấy mẫu trang; chạy nền, không chạy song song việc nặng khác).
2. **Cổng gốc chỉ các nhịp B01 B03 B08 B15 B32** trên dải mới `review-c4/strips/` (đã sửa bằng hình vòng 1; luật 3 vòng, khoá nghĩa): `python3 c4/blind_c4.py read c4/root-r2 root --only B01,B03,B08,B15,B32` → `pack` → commit → `grade --graders 2` → tally `--advice-rubric new` (rubric cũ báo song song). Trượt → sửa bằng hình (vòng 2/3) → đọc lại; hết 3 vòng → G2 nêu trước/sau. Rồi lượt đạo diễn 2 lượt chỉ nếu đổi lớn.
3. **C5 → Shorts → G2**: `res: 1080` (C14, V11.plateOverGraphics cho REVIEWER), **F11 ĐẠT trên cây C5 thật** (trượt → báo, quay lại K2), `sync_audit.py` ±0,2 s, ≥ 8:00 và ≤ 9:00 đo lại sau mỗi lần dựng; Shorts SH1–SH3 (`episode.yaml shorts`, ghi `contract.json shorts`); gói G2 + REVIEWER; đóng phiên.
- Treo: lượt đạo diễn còn ghi — khung chuyển máy (đồ thị nửa ngoài khung ≤ 0,5 s), "44.3%" sớm 0,7 s, "3%" thang trễ 1,9 s (quy tắc 1 + 7), nhãn thêm "check: +2% a year" ở outro (B32). P4 merge **squash** `ep006` → `main` (gồm F-13). Lô K: `checks-appeal.md` A28 (mặc định rubric mới).

## 3. Quyết định đã có (chủ dự án)
G1 → `gates/G1-answer.md` · C3 → `gates/C3-answer.md` · 09/10 P3b: F-13 sửa trên `ep006` (điều kiện, bằng chứng) · **C4 rubric MỚI** → `gates/C4-answer.md` · Tập 4 không đăng, Tập 3/5 đã đăng (sổ gu).

## 4. Đã sửa gì, vì sao
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C4 l1 | c, f | F-2 chữ × chữ/đường | dời nhãn trục; số vào thanh | 104 → 0; 177 → 0 | — |
| C4 l2 | c, f | quy tắc 7 | mở 5 s ở thế giới | verify OK | — |
| F-13 | nhà máy | mux `-shortest` rơi 2–4 khung | bỏ `-shortest` | splice OK; Tập 5 trùng byte hình | vào `main` P4 |
| C4 r1 | a–f | cắt mép, đè chân trang, chồng nhãn, ident đen, Edna mất (hideColumn), khung tĩnh dài | `c4/FIX-R1.md` | F-2 0, mép 0 (phát lại) | đọc lại B01 B03 B08 B15 B32 |

## 5. Mức cảnh báo, token, giờ render (`episode.md` §8)
Mức cảnh báo tập **15** triệu. EL **7.699/7.700** (P3b: 0). Agent con P3b: **10** (cộng tập 23/40).
| Phiên | Đến (UTC) | Sinh ra | Đầu vào mới | Đọc cache | Trần | Headless (trần) | Giờ render |
|---|---|---|---|---|---|---|---|
| P3b | 2026-10-09 10:08 | **1,35** | **71,18** | 475,72 | **72,52** | 0,64 (126 lượt) | ≈ 2,5 h |
**Vượt mức cảnh báo ≈ 4,8 lần** (D-009: chỉ cảnh báo) — gần hết là agent con dựng/đạo diễn đọc nhiều ảnh (đạo diễn A 3.731 lượt công cụ). Cộng tập ≈ 75,5 / 15 triệu.

## 6. Phiên sau đọc (≤ 8 tệp)
1. `CHARTER.md` 2. `playbook/episode.md` 3. `episodes/ep006/PLAN.md` 4. `episodes/ep006/ledger.md` 5. `episodes/ep006/gates/C4-answer.md` 6. `episodes/ep006/gates/C4-intent.md` 7. `episodes/ep006/c4/FIX-R1.md` 8. `playbook/prompts/P3.md`

**Tệp lớn ngoài git** (mất container → dựng lại): `data/raw/*.csv` (CPIAUCNS `f79e3a78…`, CPIAUCSL `f8ecddf5…`, CWUR0000SA0 `27ceaacf…`, PCEPI `0f416a34…`) ← `python3 episodes/ep006/data/fetch.py --verify` · `out/video.mp4` 720p `0267f00e…` (1,1 GB), `out/audio/stems/*.flac`, `work/factory/world/{a…f}-720.mp4` (a `6006c569…` b `77b8afaf…` c `048b5b88…` d `54978488…` e `b45fc385…` f `57fdc9c9…`), `work/factory/music/bed.wav` `47ff2d28…`, `work/factory/SH{1,2,3}.mp4` ← `python3 episodes/ep006/world/derive.py && python3 episodes/ep006/c4/build_inputs.py --timeline && bash toolkit/build.sh episodes/ep006/episode.yaml` (nền, ≈ 1,5 h không cache) `&& python3 episodes/ep006/c4/build_inputs.py --out`. Checks cần `av` < 15 (`pip install "av>=12,<15"`; av 19 làm A12–A15, S18, R03, R07, V10, L1 ERROR).

## 7. Prompt phiên kế (D-011) — chủ dự án dán nguyên khối vào phiên mới
```
Chạy Tập 6, phiên P3c. Nhánh ep006 (@ SHA đóng P3b hoặc mới hơn). Mở bằng `bash toolkit/verify.sh ep006`; đọc mục 6 của episodes/ep006/PLAN.md.
C4 dở: animatic 720p đã sửa vòng 1 (536,6 s); cổng khuyên dùng rubric MỚI (gates/C4-answer.md) — bản có lời cả tập + S29 ĐẠT. Container mới thì dựng lại theo PLAN §6 "Tệp lớn ngoài git" trước.
Việc: (1) checks đủ bộ lần 1 nếu chưa có báo cáo; (2) cổng gốc chỉ B01 B03 B08 B15 B32 (luật 3 vòng, khoá nghĩa); (3) C5 (1080p, ≥ 8:00, ≤ 9:00, mid-roll hợp lệ; REVIEWER đọc V11.plateOverGraphics; F11 phải ĐẠT trên cây C5 thật, trượt thì báo) → Shorts → G2 (đóng phiên theo playbook/prompts/RUN.md "Đóng phiên").
Việc nặng chạy nền rồi giao agent MỚI đầu bài ngắn; không chạy song song checks với render/kiểm mù.
Ghi chú thêm của chủ dự án (nếu có):
<<DÁN GHI CHÚ Ở ĐÂY>>
```
