#!/usr/bin/env bash
# R&D v4 · 2b: thử xử lý PHIM TƯ LIỆU công cộng (Prelinger Archives, archive.org "Financin1935", licenseurl publicdomain; RIGHTS §F7 X-RND-2).
#   bash rnd-hybrid/v4/hist/film/film.sh   (từ gốc repo; ffmpeg + libvidstab; tất định: 1 luồng, hạt nhiễu có hạt giống)
# Đoạn 36,0–39,8 s (phố Chicago + vỉa hè đông người, c. 1935). Chuỗi: ổn định (vidstab 2 lượt) → chỉnh tông (đường cong + hai tông giấy ấm / bóng
# lạnh = bảng màu K1) → hạt nhẹ → co 4:3 lên 1080 → viền giấy mảnh trên nền tối 1920×1080. Ra: clip xử lý (work/, không commit) + 2 ảnh so sánh.
set -euo pipefail
SRC=rnd-hybrid/work/external/prelinger/Financin1935.mp4; W=rnd-hybrid/work/v4film; OUT=rnd-hybrid/v4/out/hist; mkdir -p $W $OUT
echo "9e54d00f1401bbdcffc21ce6d77148fa13de3e76  $SRC" | sha1sum -c --quiet
T0=36.0; DUR=3.8
ffmpeg -loglevel error -y -ss $T0 -t $DUR -i $SRC -an -c:v libx264 -crf 12 -preset medium -threads 1 $W/raw.mp4
ffmpeg -loglevel error -y -threads 1 -i $W/raw.mp4 -vf "vidstabdetect=shakiness=6:accuracy=15:result=$W/t.trf" -f null -
TONE="format=gray,curves=all='0/0.03 0.2/0.14 0.5/0.5 0.82/0.86 1/0.96',format=rgb24,lutrgb=r='26+val*215/255':g='30+val*200/255':b='36+val*172/255'"
GRAIN="noise=c0s=7:c0f=t+u:all_seed=19350"
FRAME="scale=-2:930:flags=lanczos,unsharp=5:5:0.4,pad=1920:1080:(ow-iw)/2:(oh-ih)/2-12:color=0x0D0C0C,drawbox=x=(1920-1240)/2-5:y=(1080-930)/2-17:w=1250:h=940:color=0xE3D8C2@1:t=4"
ffmpeg -loglevel error -y -threads 1 -i $W/raw.mp4 -vf "vidstabtransform=input=$W/t.trf:smoothing=20:zoom=3:optzoom=0:interpol=bicubic,$TONE,$GRAIN,$FRAME" \
  -c:v libx264 -crf 16 -preset medium -threads 1 -pix_fmt yuv420p $W/processed.mp4
ffmpeg -loglevel error -y -ss 1.5 -i $W/raw.mp4 -frames:v 1 -vf "scale=-2:1080:flags=lanczos,pad=1920:1080:(ow-iw)/2:0:color=black" $OUT/film-raw-1080.png
ffmpeg -loglevel error -y -ss 1.5 -i $W/processed.mp4 -frames:v 1 $OUT/film-processed-1080.png
# độ rung: dịch chuyển trung bình giữa khung trước/sau ổn định (trf → biên độ chuyển động thô)
python3 - "$W/t.trf" <<'PY'
import re,sys,statistics as S
xs=[];ys=[]
for l in open(sys.argv[1]):
    m=re.findall(r'LM (-?\d+) (-?\d+)',l)
    if m: xs.append(S.median([int(a) for a,b in m])); ys.append(S.median([int(b) for a,b in m]))
print('trf frames',len(xs),'median |dx|',S.median(map(abs,xs)) if xs else None,'median |dy|',S.median(map(abs,ys)) if ys else None)
PY
sha256sum $W/raw.mp4 $W/processed.mp4
