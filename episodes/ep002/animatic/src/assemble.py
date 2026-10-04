#!/usr/bin/env python3
"""Join work/scenes/Sxx.mp4 (1280x720, 30 fps, each exactly round(end*30)-round(start*30) frames, scene edges on frames) in
timing.json order into out/silent-720p.mp4 (no sound, for the blind check) and out/animatic-720p.mp4 (+ the temporary
narration work/narration.m4a from make_timing.py, AAC copied). Pattern: episodes/ep001/animatic/src/assemble.py (ffmpeg here).
Checks frame counts against timing.json and keeps each file < 50 MB (raises CRF if not)."""
import json, os, subprocess, time
HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE); WK = os.path.join(AN, 'work')
tm = json.load(open(os.path.join(AN, 'timing.json')))
os.makedirs(os.path.join(AN, 'out'), exist_ok=True)
frames = lambda f: int(subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', f], capture_output=True, text=True, check=True).stdout.strip())
rep = []
for s in tm['scenes']:
    want = round(s['end'] * 30) - round(s['start'] * 30); got = frames(os.path.join(WK, 'scenes', s['id'] + '.mp4'))
    rep.append({'scene': s['id'], 'frames': got, 'want': want}); assert got == want, (s['id'], got, want)
lst = os.path.join(WK, 'concat.txt')
open(lst, 'w').write(''.join(f"file '{os.path.join(WK, 'scenes', s['id'] + '.mp4')}'\n" for s in tm['scenes']))
silent, full = os.path.join(AN, 'out', 'silent-720p.mp4'), os.path.join(AN, 'out', 'animatic-720p.mp4')
t0 = time.time()
for crf in (23, 26, 29):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c:v', 'libx264', '-preset', 'medium', '-crf', str(crf), '-pix_fmt', 'yuv420p',
                    '-profile:v', 'high', '-g', '60', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', '-an', silent], check=True)
    if os.path.getsize(silent) < 46e6: break
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', silent, '-i', os.path.join(WK, 'narration.m4a'), '-map', '0:v', '-map', '1:a', '-c', 'copy', '-movflags', '+faststart', full], check=True)
dur = lambda f: float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True, check=True).stdout)
res = {'frames': sum(r['frames'] for r in rep), 'seconds': sum(r['frames'] for r in rep) / 30, 'crf': crf, 'wallSeconds': round(time.time() - t0, 1),
       'silentMB': round(os.path.getsize(silent) / 1e6, 2), 'animaticMB': round(os.path.getsize(full) / 1e6, 2), 'silentDur': dur(silent), 'animaticDur': dur(full),
       'narrationDur': dur(os.path.join(WK, 'narration.m4a')), 'scenes': rep}
json.dump(res, open(os.path.join(WK, 'assemble.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != 'scenes'}))
