#!/usr/bin/env bash
# Tập 7 · P4 giao hàng (episode.md §6; mẫu episodes/ep006/c5/deliver.sh): master giữ nguyên từng byte (deliver.py --skip-encode, phần 90 MB),
# kèm Shorts SH1/SH2 (G2 duyệt; SH3 bỏ), 3 thumbnail + mô tả + tag (Claude viết, chủ dự án 13/10), phụ đề. Nhánh mồ côi ep007-delivery, đẩy.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"; EP="$ROOT/episodes/ep007"; D="$EP/work/delivery"
cd "$ROOT"
rm -rf "$D"
python3 toolkit/deliver/deliver.py "$EP/out/video.mp4" --out "$D" --name ep007 --skip-encode
for n in 1 2; do cp "$EP/work/factory/SH$n.mp4" "$D/ep007-short-SH$n.mp4"; done
for n in 1 2 3; do cp "$EP/out/package/thumb-$n.png" "$D/ep007-thumb-$n.png"; done
cp "$EP/out/captions.srt" "$D/ep007-captions.srt"; cp "$EP/out/package/description.md" "$D/ep007-description.md"; cp "$EP/out/package/tags.txt" "$D/ep007-tags.txt"
( cd "$D" && sha256sum ep007-short-SH*.mp4 ep007-thumb-*.png ep007-captions.srt ep007-description.md ep007-tags.txt >> SHA256SUMS )
python3 - "$ROOT" "$D" <<'PY'
import glob, os, sys
sys.path.insert(0, os.path.join(sys.argv[1], 'toolkit/deliver'))
import deliver
d = sys.argv[2]
files = sorted(glob.glob(f'{d}/ep007-youtube.mp4.part*')) + [f'{d}/SHA256SUMS', f'{d}/JOIN.md'] + \
        sorted(glob.glob(f'{d}/ep007-short-SH*.mp4') + glob.glob(f'{d}/ep007-thumb-*.png')) + \
        [f'{d}/ep007-captions.srt', f'{d}/ep007-description.md', f'{d}/ep007-tags.txt']
deliver.branch_free(sys.argv[1], 'ep007-delivery', remote=True)
sha = deliver.commit_branch(sys.argv[1], 'ep007-delivery', files, push=True,
                            message='ep007-delivery: master nguyên byte (phần 90 MB) + Shorts SH1/SH2, 3 thumbnail, phụ đề, mô tả, tag (xoá nhánh sau khi tải)')
print(f'nhánh ep007-delivery @ {sha} (đã đẩy)')
PY
