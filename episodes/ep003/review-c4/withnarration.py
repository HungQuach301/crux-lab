"""Tập 3 · C4: mẫu "clip có tiếng" cho câu hỏi khuyên (ý đồ `gates/C4-intent.md` §A) = dải 6 khung của `strips.py`
+ ngay dưới dải, nguyên văn lời đọc của đúng khoảng đó ("Narration heard during this clip: …"). ffmpeg drawtext, không thêm gì khác.
    python3 episodes/ep003/review-c4/withnarration.py STRIP.png NARRATION.txt OUT.png
"""
import os, subprocess, sys, tempfile, textwrap

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
PX, LH, MARGIN, WRAP = 30, 42, 24, 118


def main(strip, narr, out):
    w, h = map(int, subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', strip],
                                   capture_output=True, text=True, check=True).stdout.strip().split(','))
    body = open(narr, encoding='utf-8').read().strip()
    lines = ['Narration heard during this clip:'] + textwrap.wrap(body, WRAP)
    pad = MARGIN * 2 + LH * len(lines)
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write('\n'.join(lines)); tf = f.name
    vf = (f"pad={w}:{h + pad}:0:0:color=0x06080B,"
          f"drawtext=fontfile={FONT}:textfile={tf}:fontsize={PX}:line_spacing={LH - PX}:fontcolor=0xF2F4F7:x={MARGIN}:y={h + MARGIN}")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', strip, '-vf', vf, '-frames:v', '1', out], check=True)
    os.unlink(tf)


if __name__ == '__main__':
    main(*sys.argv[1:4])
