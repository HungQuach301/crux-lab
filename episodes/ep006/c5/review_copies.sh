#!/usr/bin/env bash
# Tập 6 · C5 → G2: bản xem lại (không thay bản phát hành; mẫu episodes/ep005/c5/review_copies.sh). review-g2/full-720p.mp4 (+ .sha256),
# highlights.mp4 (≤ 3 phút: cold open, S06–S07 séc lớn/thùng tối, S14–S15 lưới 715, S29 ba tháng bắt đầu, S30 thang — mốc từ out/timeline.json),
# Shorts, thumbnail PNG, dải B01/B15 trước (C4 vòng 0, review-c4/r1) / sau (bản giao, review-c4/strips).
set -euo pipefail
EP="$(cd "$(dirname "$0")/.." && pwd)"; R="$EP/review-g2"; mkdir -p "$R"
V="$EP/out/video.mp4"
ffmpeg -y -loglevel error -i "$V" -vf scale=1280:720 -c:v libx264 -preset medium -crf 21 -c:a aac -b:a 192k -movflags +faststart "$R/full-720p.mp4"
( cd "$R" && sha256sum full-720p.mp4 > full-720p.mp4.sha256 && sha256sum "$V" | sed "s#$V#out/video.mp4 (master 1080p)#" >> full-720p.mp4.sha256 )
read -r -a SPANS <<< "$(python3 - "$EP" <<'PY'
import json, sys
t = {s['id']: s for s in json.load(open(sys.argv[1] + '/out/timeline.json'))['scenes']}
end = lambda k: t[k]['start'] + t[k]['dur']
sp = [(0, end('S03') - 3.0), (t['S06']['start'], end('S07')), (t['S14']['start'], end('S15')), (t['S29']['start'], end('S30'))]
assert sum(b - a for a, b in sp) <= 180, sp
print(' '.join(f'{a:.3f},{b:.3f}' for a, b in sp))
PY
)"
F=(); FC=""; i=0
for s in "${SPANS[@]}"; do a=${s%,*}; b=${s#*,}; F+=(-ss "$a" -to "$b" -i "$V")
  d=$(python3 -c "print(round($b-$a-0.4,3))")
  FC+="[$i:v]scale=1280:720,fade=t=in:d=0.4,fade=t=out:st=$d:d=0.4,setsar=1[v$i];[$i:a]afade=t=in:d=0.3,afade=t=out:st=$d:d=0.4[a$i];"; i=$((i+1)); done
for j in $(seq 0 $((i-1))); do FC+="[v$j][a$j]"; done; FC+="concat=n=$i:v=1:a=1[v][a]"
ffmpeg -y -loglevel error "${F[@]}" -filter_complex "$FC" -map '[v]' -map '[a]' -c:v libx264 -preset medium -crf 21 -c:a aac -b:a 192k -movflags +faststart "$R/highlights.mp4"
for n in 1 2 3; do cp "$EP/out/shorts/SH$n.mp4" "$R/short-SH$n.mp4"; cp "$EP/out/package/thumb-$n.png" "$R/thumb-$n.png"; done
for b in B01 B15; do cp "$EP/review-c4/r1/strips/$b.png" "$R/before-$b.png"; cp "$EP/review-c4/strips/$b.png" "$R/after-$b.png"; done
( cd "$R" && sha256sum full-720p.mp4 highlights.mp4 short-SH*.mp4 thumb-*.png > SHA256SUMS-review )
ls -la "$R"
