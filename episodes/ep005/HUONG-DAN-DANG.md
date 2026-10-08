# Hướng dẫn đăng — Tập 5

**ĐƯỢC ĐĂNG** — G2 duyệt 08/10/2026 (L3 4·4·4·4·4·4; `gates/G2-answer.md`). Checks khoá `d93276a4` (`out/checks/run-c5c/`): **Tập ĐẠT**, CHẶN 35/35; CHÍNH 9/11 (F07, V11 — chủ dự án chấp nhận, xem dưới).

## Giao file (G3, 08/10/2026)
- **GitHub Release `ep005-v1`: không tạo được.** Thử một lần (`POST /repos/HungQuach301/crux-lab/releases`) → **HTTP 403** "Creating, editing, or deleting releases is not permitted for this session type" (giới hạn của loại phiên, không phải quyền repo). Theo lệnh: quay về ngay **nhánh tạm `ep005-delivery` + phần 90 MB** như Tập 4 (commit `85bdb4d`).
- **Master 1080p giữ nguyên từng byte** (không mã hoá lại; `deliver.py --skip-encode`): `ep005-youtube.mp4` = `out/video.mp4`, 1.008.459.555 byte, 7:45,7, −14,0 LUFS / −1,9 dBTP.
- **Đã kiểm ngược:** tải lại cả 20 file từ link công khai dưới, ghép 12 phần, `sha256sum -c SHA256SUMS` → **21/21 OK** (08/10/2026).

Tải thẳng (link công khai): [`SHA256SUMS`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/SHA256SUMS) · [`JOIN.md`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/JOIN.md) (lệnh ghép Windows/Mac)

| File | SHA-256 |
|---|---|
| `ep005-youtube.mp4` (ghép từ 12 phần dưới) | `d2a04ca70015ec4d211f28495c0bd3d34bc979cb7ca7a8279cbc47cea0dc653a` |
| [`ep005-youtube.mp4.part01`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part01) | `3ec643cece126ca343fa0339f923a7463a87fa11e84a73c2f2d791eec07e18ce` |
| [`ep005-youtube.mp4.part02`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part02) | `69a79b7ec6588d3270a5b00449c1b11a2ca5c3ad66dbd3d21177e3ffa0abad09` |
| [`ep005-youtube.mp4.part03`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part03) | `99557c8f42498dd601edeef07fc8ba745f98c07059d4c9449bfbc53bdbfd3ae1` |
| [`ep005-youtube.mp4.part04`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part04) | `55c79ca8d652b85f93badf3c55ec1660716ac55af84d49d0698d842ed8290644` |
| [`ep005-youtube.mp4.part05`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part05) | `2e4d59154777e9636d581891149ffc02106203c547f6228eb667b4899b17cd56` |
| [`ep005-youtube.mp4.part06`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part06) | `0804ce829ea61ccbb9a572fac3618f3e320d9dc489f2171141dc7d7d68f10e29` |
| [`ep005-youtube.mp4.part07`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part07) | `64a853de549d34c852671e940aa6cfc5f6b8fc41afb1afb6c06697b245d4b779` |
| [`ep005-youtube.mp4.part08`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part08) | `c8d6ee091a8b732de86f32284019fa91b57351db80c0b657d37107d9c00e3bd4` |
| [`ep005-youtube.mp4.part09`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part09) | `0d4c1f063901a6276c383348277a19ad26984a0bd9c4cb7df2b8c85ef1990330` |
| [`ep005-youtube.mp4.part10`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part10) | `05f6c08c71fd630793e7665a232a012ab93fdb10c1ac5155231f18d641bea04d` |
| [`ep005-youtube.mp4.part11`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part11) | `e6c8f70205641aa710c149ee08d8bd635ce3fa9094514daffa8202bd74550933` |
| [`ep005-youtube.mp4.part12`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-youtube.mp4.part12) | `607cf36d9f70db48f84658da6176cddf7c86244016ebf71bfafcee7ebb0acc2e` |
| [`ep005-short-SH1.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-short-SH1.mp4) | `4dc30f964b56a650b80e097dd7a7f1ac66adbf91c2d0606d74d496bef5819cd8` |
| [`ep005-short-SH2.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-short-SH2.mp4) | `44db22b1ea8ea776dc0d7fa6f75554c746f779b2f884ce499bed50887bff9a23` |
| [`ep005-short-SH3.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-short-SH3.mp4) | `d8f445b79bedfc809dd7b2d924c6752ab5952146b3de5ebfc7f3b0a3e3cf5c78` |
| [`ep005-thumb-1.png`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-thumb-1.png) | `f75f7fd86845e02c3cc392fb4571a64ec6088691ff4920ec3e85e3974a2aff6c` |
| [`ep005-thumb-2.png`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-thumb-2.png) | `3be5e32a0f4da2134c0ee7f358a63a174bdb8a166a9307cf631811436d3bf38e` |
| [`ep005-thumb-3.png`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-thumb-3.png) | `d07c3da66293f42ab572b65c0613ba331de6a949af144fc49b1f381c8d888fbc` |
| [`ep005-captions.srt`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-captions.srt) | `6793b31647413810c0548cacdadf8dc211d2409977903a17d74d26e7f9b685a0` |
| [`ep005-description.md`](https://github.com/HungQuach301/crux-lab/raw/ep005-delivery/ep005-description.md) | `645ea44b0f36724ae4d0da8cbff1443964debf28469b9094115ae6ec5f25c0d3` |

Ghép master: tải 12 file `ep005-youtube.mp4.partNN` + `SHA256SUMS` vào một thư mục → Mac/Linux `cat ep005-youtube.mp4.part* > ep005-youtube.mp4 && shasum -a 256 -c SHA256SUMS` · Windows `copy /b ep005-youtube.mp4.part01 + … + ep005-youtube.mp4.part12 ep005-youtube.mp4` rồi `certutil -hashfile ep005-youtube.mp4 SHA256` (đầy đủ trong `JOIN.md`). Mã phải là `d2a04ca7…dc653a`.

## Đăng video chính
- **Tiêu đề:** **T1** "10% Down and Mortgage Insurance: How Long Did It Last?" (G1).
- **Mô tả và chương:** `ep005-description.md` — dán nguyên văn. 6 chương: 0:00 · 0:58 · 3:09 · 5:21 · 7:14 · 7:25. Nguồn FRED (MORTGAGE30US, HPIPONM226N, kiểm chéo OBMMIC30YF, CSUSHPINSA, MSPUS), 12 U.S.C. 4901/4902, Fannie Mae B-8.1-04 (chỉ khoản vay Fannie Mae), CFPB; "Not modeled"; "US only · history, not a forecast".
- **Phụ đề:** `ep005-captions.srt` (tiếng Anh).
- **Thumbnail:** mặc định **thumb-3**; **Test & Compare: 3, 1, 2** (chủ dự án chọn ở G2). Claim từng dòng chữ: `out/package/thumb-N.json`; mọi số kèm "on paper"; không nêu số tiền phí bảo hiểm (R1).
- **Mid-roll: không** (`out/adbreaks.json` rỗng). Tập 7:46 < 8:00; chủ dự án quyết 08/10 (bài học T5-1).

## Shorts (G2: OK)
Mỗi Short gắn link video chính (Related video). Tiêu đề:
- `ep005-short-SH1.mp4` (22,7 s): *How long did mortgage insurance last at 10% down? The typical case, on paper*
- `ep005-short-SH2.mp4` (37,8 s): *The long tail: when reaching 80% on paper took more than five years*
- `ep005-short-SH3.mp4` (43,5 s): *Fastest vs slowest: two illustrative buyers, a year apart*

## Trước khi bấm đăng: claim có hạn dùng
- **Lãi "tháng đủ tuần mới nhất" = September 2026 (6.86%)** và các số theo lãi đó (`sched80_months_latest` 99 kỳ ≈ 8 năm, `sched78_months_latest` 114, `ex_payment_pi` $2,362): hình và lời đều ghi tháng (September 2026) nên là số lịch sử có ngày, **giữ nguyên** dù đăng sau tháng 10/2026.
- **Chỉ số FHFA** (dữ liệu tới 07/2026; FHFA sửa số cũ mỗi tháng): mô tả và thẻ phương pháp nói "history"; giữ nguyên.
- **12 U.S.C. 4902 / Fannie Mae B-8.1-04:** nếu luật hoặc Guide đổi trước ngày đăng → dừng, hỏi lại (sai nghĩa).

## Ngoại lệ đã duyệt (G2) — `out/explanations.json`, `gates/G2.md`
- **F07** (465,7 s < 480 s): giữ độ dài, không mid-roll.
- **V11**: chữ còn đếm là chữ nằm trên tấm nền của chính nó; chấp nhận, chờ `checks-appeal.md` A22 (lô K).
- Nhãn `Fannie Mae: wait ≥ 2 years · loan ≤ 75%` hiện ≈ 1 s (giữ; từ Tập 6 luật 1 s/3 từ, T5-2). S17.3 giữ chữ.

## Sau khi đăng
- Ghi link video, ngày đăng vào `episodes/ep005/audience.md`.
- Báo phiên đã tải xong → phiên merge `ep005` vào `main` (P3) và xoá `ep005-delivery` (proxy chặn xoá → chủ dự án xoá: GitHub → Branches → Delete).
- Mốc 7 ngày: một ảnh chụp YouTube Studio cho chat chiến lược (`playbook/templates/audience.md`).
