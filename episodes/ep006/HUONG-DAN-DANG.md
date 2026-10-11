# Hướng dẫn đăng — Tập 6

**ĐƯỢC ĐĂNG** — G2 duyệt 11/10/2026 (L3: chủ dự án xác nhận ≥ 4 ở cả 6 dòng, không chấm số chi tiết; `gates/G2-answer.md`). Checks khoá `4d688acd` (`out/checks/run-c5d/`): **Tập ĐẠT**, CHẶN 36/36, CHÍNH 13/13.

## Giao file (G3, 11/10/2026)
- **Nhánh tạm `ep006-delivery` + phần 90 MB** (commit `d4d8c48`; lessons T5-3 — không thử GitHub Release).
- **Master 1080p giữ nguyên từng byte** (không mã hoá lại; `deliver.py --skip-encode`, `c5/deliver.sh`): `ep006-youtube.mp4` = `out/video.mp4`, 1.161.961.868 byte, 8:56,6, −14,0 LUFS / −1,8 dBTP.
- **Đã kiểm ngược:** tải lại cả 23 file từ link công khai dưới, ghép 13 phần, `sha256sum -c SHA256SUMS` → **22/22 OK** (11/10/2026).

Tải thẳng (link công khai): [`SHA256SUMS`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/SHA256SUMS) · [`JOIN.md`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/JOIN.md) (lệnh ghép Windows/Mac)

| File | SHA-256 |
|---|---|
| `ep006-youtube.mp4` (ghép từ 13 phần dưới) | `f96da0ea19e6426aa3b4bd37759f3e7c8fb9819e489a1fab317683fd5edcaa74` |
| [`ep006-youtube.mp4.part01`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part01) | `06afbe5c085cbf6fe7bf339d9fb3048f421c9cfa2e9ca056079a358d2c8b0046` |
| [`ep006-youtube.mp4.part02`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part02) | `01396b266c88e08955393fa27d8687cba71ffdba2c282e1dcfa5d468d9f21ec4` |
| [`ep006-youtube.mp4.part03`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part03) | `1539cc51f23e6b1558fbcae90052575f754ad23a39d1dfaa5f1d924e3135849c` |
| [`ep006-youtube.mp4.part04`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part04) | `b84b489d9a3e14eba4b2cfa11241e7cda199fb3e7ffa3407bb071270fd45cf42` |
| [`ep006-youtube.mp4.part05`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part05) | `dfe84816bf0dbb05183ec6c56b1cb672e532bbc8073b2b00bf3a13cbe59db094` |
| [`ep006-youtube.mp4.part06`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part06) | `1d1f8f49cf95d8cb38cdbe84394f8ac6429b3909688240dfac4a4ce1e85a7ac2` |
| [`ep006-youtube.mp4.part07`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part07) | `58b9758222b55966a5f3db19ae5ad19e05911e851467f9dd3d70208a4a0266f3` |
| [`ep006-youtube.mp4.part08`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part08) | `7d1ff80569e20374907fc42bfd01277aa8f61024750e60cca0ec87f78c0870a7` |
| [`ep006-youtube.mp4.part09`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part09) | `f1a48b63d7bb5180dca02af0c42500cfe87d5d6c821a2e58532e2462aa5c8eb4` |
| [`ep006-youtube.mp4.part10`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part10) | `2ec19592b3f2accc66b970cf38871bf309c5ffee982c443b100456eaa1ec15ae` |
| [`ep006-youtube.mp4.part11`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part11) | `aa6adaa15e9224f86e847f3c8e181d445cc0167c3923264425cfa09079594860` |
| [`ep006-youtube.mp4.part12`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part12) | `f4565d0e89000977e16b76f62ceeec664a9e1fd88a89eaee49a2d94f76bd54bd` |
| [`ep006-youtube.mp4.part13`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-youtube.mp4.part13) | `29753c716bd4614dde590542bb26a62f4bbaa319eefe553f2d228cbbd8a48d5e` |
| [`ep006-short-SH1.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-short-SH1.mp4) | `607e5a13cd09601ff8087799d2f26e2d80cd91f8105b8632593c1217d0be6aa3` |
| [`ep006-short-SH2.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-short-SH2.mp4) | `dda7950a8f895ecabec3c167f7377e979c71ee7537cebe484111a2351e5ab54d` |
| [`ep006-short-SH3.mp4`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-short-SH3.mp4) | `dd8cf7012860ef4ff3e933e4d68d5faeea26aac0144abfaa335d3850f51daa71` |
| [`ep006-thumb-1.png`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-thumb-1.png) | `e43b990ad68e6feb87ef8966633a0ed6e5cfd53604cfebaf2e72cfcc0d44c390` |
| [`ep006-thumb-2.png`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-thumb-2.png) | `c71027b2061a4c51a744cc0d5b753506eb7e63b5aec8b78f0508e247c7a33dc5` |
| [`ep006-thumb-3.png`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-thumb-3.png) | `83cafaed9350bbe26043737b480594980f0df59de395681b3a9851ea56ee0a29` |
| [`ep006-captions.srt`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-captions.srt) | `d01ef80b862fd72e48234641b567afcae4ae52e33a16815e69629db12536c983` |
| [`ep006-description.md`](https://github.com/HungQuach301/crux-lab/raw/ep006-delivery/ep006-description.md) | `c1841840355293a0c34ee4f4e5e02aa7278701eb32fc316213a2f63d99ffc9ab` |

Ghép master: tải 13 file `ep006-youtube.mp4.partNN` + `SHA256SUMS` vào một thư mục → Mac/Linux `cat ep006-youtube.mp4.part* > ep006-youtube.mp4 && shasum -a 256 -c SHA256SUMS` · Windows `copy /b ep006-youtube.mp4.part01 + … + ep006-youtube.mp4.part13 ep006-youtube.mp4` rồi `certutil -hashfile ep006-youtube.mp4 SHA256` (đầy đủ trong `JOIN.md`). Mã phải là `f96da0ea…5edcaa74`.

## Đăng video chính
- **Tiêu đề:** **T1** "Does a 2% Annuity Raise Really Keep Up With Prices?" (G1).
- **Mô tả và chương:** `ep006-description.md` — dán nguyên văn. 6 chương: 0:00 · 0:51 · 3:28 · 5:29 · 8:05 · 8:36. Nguồn FRED (CPIAUCNS, kiểm chéo CPIAUCSL; CWUR0000SA0, PCEPI), "Not modeled", "US only · history, not a forecast. Not advice."
- **Phụ đề:** `ep006-captions.srt` (tiếng Anh).
- **Thumbnail:** **chủ dự án tự làm trên ChatGPT**, nền tham khảo `ep006-thumb-1.png` (khung thế giới đoạn b, 70,2 s). Gửi ảnh cho phiên → phiên kiểm chữ trên ảnh: không số tiền, không khuyên, có **ILLUSTRATIVE** khi có nhân vật, có **"US only · history, not a forecast"** → báo đạt/không. Nếu dùng bộ nhà máy: mặc định thumb-1, **Test & Compare 1, 2, 3** (claim từng dòng chữ: `out/package/thumb-N.json`; số duy nhất "+48.6% on paper" = claim `two_pct_growth_20y_pct`).
- **Mid-roll: 1 mốc 3:28** (`out/adbreaks.json` 208,15 s; đầu chương "Every 20-year stretch since 1947"). Không mốc nào trong 2 phút đầu hay 2 phút cuối. Tập 8:56,6 ≥ 8:00 (G1 (b)).

## Shorts (G2: OK)
Mỗi Short gắn link video chính (Related video). Tiêu đề đề xuất (móc trên hình; chủ dự án sửa được, giữ luật: không số tiền, không khuyên):
- `ep006-short-SH1.mp4` (38,6 s, S06–S07): *A 2% raise every year, and the check still buys less*
- `ep006-short-SH2.mp4` (18,8 s, S14–S15): *How often did a 2% raise keep up with US prices since 1947?*
- `ep006-short-SH3.mp4` (20,9 s, S29): *One 2% raise, three start months, three different outcomes*

## Trước khi bấm đăng: claim có hạn dùng
- **Dữ liệu CPI "through August 2026"** (cửa sổ gần nhất Aug 2006 → Aug 2026; Ruth ILLUSTRATIVE kết thúc Aug 2026): hình, lời và mô tả đều ghi tháng nên là số lịch sử có ngày — **giữ nguyên** dù BLS đã công bố CPI tháng 9/2026 trở đi.
- **Ô CPI tháng 10/2025 trống trong nguồn** (mô tả: bỏ tháng bắt đầu October 2005): nếu FRED điền ô này trước ngày đăng, câu vẫn đúng với dữ liệu đã dùng (tải 2026-10-08) — giữ nguyên.
- Lời không có số "hiện tại" (lạm phát năm nay); không có claim hết hạn khác.

## Giữ nguyên (đã quyết ở G2)
- `out/explanations.json` không còn mục CHÍNH nào (run-c5d CHÍNH 13/13).
- **B01, B15** (cổng gốc tắt tiếng nghĩa 0,5 sau 3 vòng): giữ bản sau (chủ dự án 11/10).
- qc nhà máy 6 mục TRƯỢT cùng loại Tập 5 đã đăng (đối trọng master đọc ở đoạn thế giới, freezedetect, true peak −1,8 dBTP) — ghi ở `gates/G2.md`.

## Sau khi đăng (G3)
- Ghi link video, ngày đăng vào `episodes/ep006/audience.md`.
- Báo phiên đã đăng và tải xong → phiên xoá nhánh `ep006-delivery` (proxy chặn xoá → chủ dự án xoá: GitHub → Branches → Delete).
- Mốc 7 ngày: một ảnh chụp YouTube Studio cho chat chiến lược (`playbook/templates/audience.md`).
