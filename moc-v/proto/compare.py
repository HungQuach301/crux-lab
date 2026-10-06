"""Mốc V · MỘT clip so sánh xem trên điện thoại: thẻ tên (2,5 s) + mỗi bản 69,6 s, 720p H.264 + AAC, −14 LUFS mỗi bản.
  python3 moc-v/proto/compare.py <out.mp4> <label1>=<video1> <label2>=<video2> ...
"""
import os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont
out = sys.argv[1]; items = [a.split('=', 1) for a in sys.argv[2:]]
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; F2 = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
tmp = tempfile.mkdtemp(); parts = []
for i, (lab, v) in enumerate(items):
    title, _, sub = lab.partition('|')
    im = Image.new('RGB', (1280, 720), (14, 17, 22)); d = ImageDraw.Draw(im)
    d.text((640, 300), title, font=ImageFont.truetype(F, 64), fill=(242, 244, 247), anchor='mm')
    d.text((640, 390), sub, font=ImageFont.truetype(F2, 34), fill=(154, 164, 178), anchor='mm')
    d.text((640, 640), f'{i + 1}/{len(items)} · Mốc V · cùng đoạn Tập 4 (S04.5 → S07.3), 69,6 s', font=ImageFont.truetype(F2, 24), fill=(154, 164, 178), anchor='mm')
    png = os.path.join(tmp, f'c{i}.png'); im.save(png)
    card = os.path.join(tmp, f'c{i}.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', '2.5', '-i', png, '-f', 'lavfi', '-t', '2.5', '-i', 'anullsrc=r=48000:cl=stereo',
                    '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-shortest', card], check=True)
    seg = os.path.join(tmp, f'v{i}.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', v, '-t', '69.6', '-vf', 'scale=1280:720:flags=lanczos,fps=30,format=yuv420p',
                    '-af', 'aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11', '-c:v', 'libx264', '-preset', 'medium', '-b:v', '1600k', '-maxrate', '2400k',
                    '-bufsize', '4800k', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', seg], check=True)
    parts += [card, seg]
lst = os.path.join(tmp, 'l.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c:v', 'libx264', '-preset', 'medium', '-b:v', '1600k',
                '-maxrate', '2400k', '-bufsize', '4800k', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out], check=True)
print(out, os.path.getsize(out) // 1_000_000, 'MB')
