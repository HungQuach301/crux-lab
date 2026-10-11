#!/usr/bin/env bash
# Tập 6 · P4 việc 6: giao hàng (episode.md §6; lessons T5-3 — nhánh tạm + phần 90 MB, không thử GitHub Release).
# Master đã đạt (checks run-c5d) → giữ nguyên từng byte (deliver.py --skip-encode), kèm Shorts, thumbnail nhà máy,
# phụ đề, mô tả (cùng bộ file Tập 5). SHA256SUMS gồm cả file kèm. Commit lên nhánh mồ côi ep006-delivery, đẩy.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"; EP="$ROOT/episodes/ep006"; D="$EP/work/delivery"
cd "$ROOT"
rm -rf "$D"
python3 toolkit/deliver/deliver.py "$EP/out/video.mp4" --out "$D" --name ep006 --skip-encode
for n in 1 2 3; do cp "$EP/out/shorts/SH$n.mp4" "$D/ep006-short-SH$n.mp4"; cp "$EP/out/package/thumb-$n.png" "$D/ep006-thumb-$n.png"; done
cp "$EP/out/captions.srt" "$D/ep006-captions.srt"; cp "$EP/out/package/description.md" "$D/ep006-description.md"
( cd "$D" && sha256sum ep006-short-SH*.mp4 ep006-thumb-*.png ep006-captions.srt ep006-description.md >> SHA256SUMS )
python3 - "$ROOT" "$D" <<'PY'
import glob, os, sys
sys.path.insert(0, os.path.join(sys.argv[1], 'toolkit/deliver'))
import deliver
d = sys.argv[2]
files = sorted(glob.glob(f'{d}/ep006-youtube.mp4.part*')) + [f'{d}/SHA256SUMS', f'{d}/JOIN.md'] + \
        sorted(glob.glob(f'{d}/ep006-short-SH*.mp4') + glob.glob(f'{d}/ep006-thumb-*.png')) + \
        [f'{d}/ep006-captions.srt', f'{d}/ep006-description.md']
deliver.branch_free(sys.argv[1], 'ep006-delivery', remote=True)
sha = deliver.commit_branch(sys.argv[1], 'ep006-delivery', files, push=True,
                            message='ep006-delivery: master nguyên byte (phần 90 MB) + Shorts, thumbnail, phụ đề, mô tả (xoá nhánh sau khi tải)')
print(f'nhánh ep006-delivery @ {sha} (đã đẩy)')
PY
