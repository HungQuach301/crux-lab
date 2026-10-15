#!/usr/bin/env bash
# Tập 8 · M6 giao hàng (chủ dự án G3 câu 2, 15/10; mẫu episodes/ep007/c5/deliver.sh): master 1080p giữ nguyên từng byte (deliver.py --skip-encode,
# phần ≤ 90 MB), Short SH1, phụ đề, mô tả, tag (không thumbnail), bản xem trước 720p ≈ 2,5 Mbps chia 3 phần TỰ XEM ĐƯỢC (GitHub chặn file > 100 MB).
# Nhánh mồ côi ep008-delivery, đẩy.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"; EP="$ROOT/episodes/ep008"; D="$EP/work/delivery"
cd "$ROOT"
rm -rf "$D"
python3 toolkit/deliver/deliver.py "$EP/out/video.mp4" --out "$D" --name ep008 --skip-encode
cp "$EP/out/shorts/SH1.mp4" "$D/ep008-short-SH1.mp4"
cp "$EP/out/captions.srt" "$D/ep008-captions.srt"; cp "$EP/out/package/description.md" "$D/ep008-description.md"; cp "$EP/out/package/tags.txt" "$D/ep008-tags.txt"
# xem trước: cắt theo khung khoá (không mã hoá lại) thành 3 phần mỗi phần mở được riêng
ffmpeg -v error -y -i "$EP/work/review/review-720p.mp4" -c copy -map 0 -f segment -segment_time 205 -reset_timestamps 1 -segment_start_number 1 "$D/ep008-review-720p-%d.mp4"
( cd "$D" && sha256sum ep008-short-SH1.mp4 ep008-captions.srt ep008-description.md ep008-tags.txt ep008-review-720p-*.mp4 >> SHA256SUMS )
python3 - "$ROOT" "$D" <<'PY'
import glob, os, sys
sys.path.insert(0, os.path.join(sys.argv[1], 'toolkit/deliver'))
import deliver
d = sys.argv[2]
big = [f for f in glob.glob(f'{d}/*') if os.path.getsize(f) > 90 * 1024 * 1024]
assert not big, f'file > 90 MB: {big}'
files = sorted(glob.glob(f'{d}/ep008-youtube.mp4.part*')) + [f'{d}/SHA256SUMS', f'{d}/JOIN.md', f'{d}/ep008-short-SH1.mp4'] + \
        sorted(glob.glob(f'{d}/ep008-review-720p-*.mp4')) + [f'{d}/ep008-captions.srt', f'{d}/ep008-description.md', f'{d}/ep008-tags.txt']
deliver.branch_free(sys.argv[1], 'ep008-delivery', remote=True)
sha = deliver.commit_branch(sys.argv[1], 'ep008-delivery', files, push=True,
                            message='ep008-delivery: master 1080p nguyên byte (phần 90 MB) + SHA256SUMS + Short SH1, phụ đề, mô tả, tag, xem trước 720p 3 phần (xoá nhánh sau khi tải)')
print(f'nhánh ep008-delivery @ {sha} (đã đẩy)')
PY
