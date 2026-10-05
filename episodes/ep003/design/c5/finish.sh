#!/usr/bin/env bash
# Tập 3 · C5: ghép hình 1080p (4 đoạn render) + bản phối (style C) → bản gốc work/c5/video.mp4 (không commit), bản xem 720p cho C6.
# Mã hoá như toolkit/render/m3-encode-range.js: H.264 High, CBR 17 Mb/s (nal-hrd=cbr), BT.709 tv, 30 fps; audio AAC 384 kb/s 48 kHz stereo.
#   bash episodes/ep003/design/c5/finish.sh
set -euo pipefail
EP="$(cd "$(dirname "$0")/../.." && pwd)"; W="$EP/work/c5"; mkdir -p "$W"
ls "$EP"/design/c3/work/ANIM-1080-[0-9]*.mp4 | sort | sed "s/^/file '/; s/$/'/" > "$W/parts.txt"
ffmpeg -y -v error -f concat -safe 0 -i "$W/parts.txt" -c copy "$W/picture.mp4"
ffmpeg -y -v error -i "$W/picture.mp4" -i "$EP/animatic/work/mix.wav" -map 0:v -map 1:a \
  -c:v libx264 -profile:v high -preset medium -b:v 17M -minrate 17M -maxrate 17M -bufsize 17M -x264-params nal-hrd=cbr:force-cfr=1 \
  -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -r 30 -g 15 -bf 2 \
  -c:a aac -b:a 384k -ar 48000 -ac 2 -shortest -movflags +faststart "$W/video.mp4"
ffmpeg -y -v error -i "$W/video.mp4" -vf scale=1280:720 -c:v libx264 -preset medium -b:v 2500k -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -c:a aac -b:a 160k -movflags +faststart "$W/preview-720.mp4"
sha256sum "$W/video.mp4" | tee "$W/video.sha256"
