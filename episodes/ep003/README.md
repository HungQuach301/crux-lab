# Tập 3 — Money You Won't Touch for 20 Years: Savings Bond or T-Bills?

Bản gốc (không lên git): `work/c5/video.mp4`, 1920×1080 30 fps, H.264 High CBR 17 Mb/s BT.709 tv, AAC 384 kb/s, 572.0 s,
**SHA-256 `103ff99ef637984f2438d7c46f6e604735fae096c57f123cd9ba4c6d5904cf27`** (checks khoá K3.7 `a20c6878…`: ĐẠT, `review-c5/checks-run5/`).
Bản tải YouTube (8 Mb/s, `toolkit/deliver/deliver.py`): `ep003-youtube.mp4` SHA-256 `1274f9f6f5df6d03bb29923e07e4ea8858a9eb226d533cbfe0a7635dc1424070`, nhánh tạm `ep003-delivery` (xoá khi chủ dự án tải xong).

## Dựng lại (từ gốc repo, `/home/user/crux-lab`)
```
python3 episodes/ep003/data/fetch.py --verify        # FRED ghim: TB3MS, CPIAUCNS (coed 2026-08-01), DTB3 (coed 2026-08-31); SHA phải trùng
mkdir -p topics-r1/machine/retire-4/data && cp episodes/ep003/data/raw/{TB3MS,CPIAUCNS}.csv topics-r1/machine/retire-4/data/   # model.py so với calc.py của hồ sơ
python3 episodes/ep003/model/model.py && python3 episodes/ep003/model/claims.py && python3 episodes/ep003/story/check_script.py
python3 episodes/ep003/animatic/voice.py             # lời theo cảnh: cắt từ review-c2/table-read.m4a; S02, S03 sinh lại (EL, seed ghi ở animatic/voice-report.json)
python3 episodes/ep003/design/c3/build_data.py
python3 -m http.server 8765 &                        # ở gốc repo
for r in "0 143" "143 286" "286 429" "429 572"; do set -- $r; NODE_PATH=$(npm root -g) node episodes/ep003/design/c3/render.js ANIM --1080 --from $1 --to $2 & done; wait
python3 episodes/ep003/audio_src/mix_full.py         # nhạc style C 114 BPM + lời → animatic/work/mix.wav, stem
bash episodes/ep003/design/c5/finish.sh              # ghép hình + tiếng → work/c5/video.mp4, bản xem 720p
python3 episodes/ep003/design/c5/artefacts.py --media
bash episodes/ep003/design/c5/checks.sh <thư mục tạm> --baseline episodes/ep003/review-c4/checks-run1/report.json
python3 toolkit/deliver/deliver.py episodes/ep003/out/video.mp4 --out episodes/ep003/work/delivery --name ep003 --branch ep003-delivery --push
```
ElevenLabs không tất định từng bit: sinh lại S02/S03 cho take khác chút ít (cùng chữ, cùng seed); hình và mọi số liệu tái lập chính xác.
Lịch sử cổng và quyết định: `PLAN.md`, `ledger.md`, `gates/`.
