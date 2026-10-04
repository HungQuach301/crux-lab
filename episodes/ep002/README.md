# Tập 2 — "7.5% Variable or 9% Fixed? Grad Loans Through History" (tiêu đề nháp của hồ sơ)

Đề tài: `topics/queue.md` #1, hồ sơ **duy nhất** `topics-r1/machine/debt-2/` (không phải `topics-r2/machine/debt-2`). Đề tài do máy đề xuất (D-004): kết quả YouTube của tập là số đo **TRỄ** của D-004 (`audience.md`, sau C6).
Phiên điều phối P-ep002, nhánh `ep002` (từ `main` `e117c49`). Quy trình 6 cổng (`playbook/quality-framework.md`). Tập 1 chỉ là mẫu quy trình, không phải mẫu nội dung.

| File | Nội dung |
|---|---|
| `PLAN.md` | bảng cổng, điểm dừng an toàn, việc treo cần chủ dự án |
| `ledger.md` | sổ chạy (mỗi agent, mỗi cổng một dòng; ký tự ElevenLabs) |
| `amendments.md` | miễn trừ / thay đổi riêng của tập |
| `checks-notes.md` | ghi chú cho phiên kiểm (K3.5: `model.kind` mới) |
| `data/` | `fetch.py --verify` tải lại TB3MS + DTB3 (không commit dữ liệu thô) |
| `model/model.py` | mô hình (lõi = `calc.py` của hồ sơ + phạm vi (b)) → `out/model.json` |
| `gates/` | ý đồ kiểm mù, kết quả nguyên văn, gói quyết định |
| `numbers.md` | bảng số, claim ID |

Dựng lại số: `python3 episodes/ep002/data/fetch.py --verify && python3 episodes/ep002/model/model.py && python3 episodes/ep002/build_numbers.py`.

## Bản giao (C6, 04/10/2026)
- `out/video.mp4`: 1080p30, 585,6 s, 1.778.564.986 byte, **SHA-256 `fdfa3d47d6ee1069a23b30d52a4044fa2f9209e1b9a0c02852e059170e2480a4`**. Không commit (`.gitignore`). Nhạc **B** (bản bớt lặp, chủ dự án chọn ở C6).
- Checks cuối: khoá K3.6 `2fcc9fcc…` (bản sao `git archive origin/main checks`, LOCK tính lại khớp): Tập ĐẠT, CHẶN 29/29, CHÍNH 11/11 (`out/checks/report.md`).
- Gói: tiêu đề A1; thumbnail mặc định `out/package/thumb-1.png`; Test & Compare thumb-1, thumb-2 (= 2b), thumb-3 (= 3c). Bản gốc không đạt claim-risk giữ ở `thumb-2-orig`, `thumb-3-orig`.

### Dựng lại bản giao từ repo
```
python3 data/fetch.py --verify                       # dữ liệu FRED (không commit), kiểm SHA
python3 model/model.py && python3 build_numbers.py && python3 contract_build.py && python3 preprod/dossier_c5.py
python3 audio_src/mix.py --music alt                 # master nhạc B → out/audio/master-alt.wav (SHA trong out/audio/manifest.json)
cp out/audio/master-alt.wav out/audio/master.wav     # bản giao dùng nhạc B
cd animatic && npm ci && bash src/render_c5.sh       # hình 1080p theo cảnh (CPU, ~25 phút tường)
python3 src/assemble_c5.py                           # ghép hình + mux out/audio/master.wav → out/video.mp4
sha256sum ../out/video.mp4                           # phải ra fdfa3d47…
```
Ghi chú: video H.264 không bảo đảm trùng từng bit giữa các máy/phiên bản ffmpeg; nếu SHA khác, so khung bằng `ffmpeg -i out/video.mp4 -f framemd5` với bản đã giao.
