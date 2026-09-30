#!/usr/bin/env python3
"""C5 final picture + delivery file.
  1. the 20 scene intermediates work/c5/scenes/Sxx.mp4 (render.js, H.264 CRF 8, exact frame counts from timing.json) are
     checked (frame count per scene) and concatenated in order;
  2. ONE delivery encode -> work/c5/picture-1080.mp4: libx264 High, yuv420p, BT.709 limited range, 1920x1080, 30/1 CFR,
     GOP 2 s, rate mode below;
  3. mux with the audio master out/audio/master.wav (stream A) -> out/video.mp4: video copied, AAC-LC 48 kHz stereo 320 kb/s,
     no global metadata, NO chapters (the chapters live in out/package/description.md only), +faststart.
Rate mode (--mode): 'cbr' (default) = constant 24 Mb/s with x264 nal-hrd=cbr filler, because the checker's F04 measures the
video bitrate from packet sizes and needs >= 16 Mb/s, which a CRF encode of flat animation never reaches; the report
(work/c5/logs/assemble.json) also gives what CRF 16 would spend per scene (--probe-crf), to show CBR 24 is above it everywhere.
'crf' = CRF 16 (the owner's quality floor, CRF <= 18) for comparison.
   python3 assemble_c5.py [--mode cbr|crf] [--probe-crf]"""
import json, os, subprocess, sys, time
import av

HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE); EP = os.path.dirname(AN)
WK = os.path.join(EP, 'work', 'c5'); SC = os.path.join(WK, 'scenes'); LOG = os.path.join(WK, 'logs')
FF = subprocess.check_output([sys.executable, '-c', 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())']).decode().strip()
mode = sys.argv[sys.argv.index('--mode') + 1] if '--mode' in sys.argv else 'cbr'
timing = json.load(open(os.path.join(AN, 'timing.json')))
FPS = 30
scenes = [(s['id'], round((s['start'] + s['dur']) * FPS) - round(s['start'] * FPS)) for s in timing['scenes']]
total = sum(n for _, n in scenes)


def frames_of(p):
    with av.open(p) as c:
        st = c.streams.video[0]
        return sum(1 for _ in c.demux(st) if _.size), st.codec_context.width, st.codec_context.height


rep = {'mode': mode, 'scenes': [], 'totalFrames': total, 'date': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
bad = []
for sid, n in scenes:
    p = os.path.join(SC, sid + '.mp4')
    if not os.path.exists(p):
        bad.append(f'{sid} missing'); continue
    k, w, h = frames_of(p)
    rep['scenes'].append({'id': sid, 'frames': k, 'expected': n, 'size': f'{w}x{h}', 'bytes': os.path.getsize(p)})
    if k != n or (w, h) != (1920, 1080):
        bad.append(f'{sid} frames {k}/{n} size {w}x{h}')
if bad:
    print('NOT READY:', bad); sys.exit(1)

lst = os.path.join(WK, 'scenes.txt')
open(lst, 'w').write(''.join(f"file '{os.path.join(SC, sid + '.mp4')}'\n" for sid, _ in scenes))
tags = ['-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv']
venc = ['-c:v', 'libx264', '-preset', 'slow', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-tune', 'animation', '-g', '60', '-bf', '2']
if mode == 'cbr':
    venc += ['-b:v', '24M', '-minrate', '24M', '-maxrate', '24M', '-bufsize', '24M', '-x264-params', 'nal-hrd=cbr:force-cfr=1']
else:
    venc += ['-crf', '16']
pic = os.path.join(WK, 'picture-1080.mp4')
t0 = time.time()
subprocess.run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-an', '-r', '30', '-fps_mode', 'cfr', *venc, *tags,
                '-map_metadata', '-1', '-map_chapters', '-1', '-movflags', '+faststart', pic + '.part.mp4'], check=True)
os.replace(pic + '.part.mp4', pic)
rep['pictureSeconds'] = round(time.time() - t0, 1)
k, w, h = frames_of(pic)
rep['picture'] = {'path': 'work/c5/picture-1080.mp4', 'frames': k, 'bytes': os.path.getsize(pic), 'videoMbps': round(os.path.getsize(pic) * 8 / (k / FPS) / 1e6, 2)}
assert k == total, f'picture frames {k} != {total}'

wav = os.path.join(EP, 'out', 'audio', 'master.wav')
out = os.path.join(EP, 'out', 'video.mp4')
t0 = time.time()
subprocess.run([FF, '-v', 'error', '-y', '-i', pic, '-i', wav, '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'copy',
                '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-ac', '2', '-map_metadata', '-1', '-map_chapters', '-1',
                '-movflags', '+faststart', out + '.part.mp4'], check=True)
os.replace(out + '.part.mp4', out)
rep['muxSeconds'] = round(time.time() - t0, 1)
with av.open(out) as c:
    v, a = c.streams.video[0], c.streams.audio[0]
    vb = ab = 0; vn = 0
    for pk in c.demux():
        if pk.size == 0: continue
        if pk.stream.type == 'video': vb += pk.size; vn += 1
        else: ab += pk.size
    dv = vn / FPS
    rep['video'] = {'path': 'out/video.mp4', 'bytes': os.path.getsize(out), 'frames': vn, 'seconds': round(dv, 3), 'videoMbps': round(vb * 8 / dv / 1e6, 2),
                    'audioKbps': round(ab * 8 / dv / 1e3, 1), 'audioRate': a.codec_context.sample_rate, 'audioChannels': a.codec_context.layout.nb_channels if hasattr(a.codec_context, 'layout') else a.codec_context.channels,
                    'audioCodec': a.codec_context.name, 'profile': v.codec_context.profile, 'chapters': len(c.chapters()) if hasattr(c, 'chapters') else None}

if '--probe-crf' in sys.argv:  # what CRF 16 would spend, scene by scene (same encoder settings)
    pr = []
    for sid, n in scenes:
        tmp = os.path.join(WK, 'probe.mp4')
        subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(SC, sid + '.mp4'), '-an', '-c:v', 'libx264', '-preset', 'slow', '-profile:v', 'high',
                        '-pix_fmt', 'yuv420p', '-tune', 'animation', '-g', '60', '-crf', '16', tmp], check=True)
        pr.append({'id': sid, 'crf16Mbps': round(os.path.getsize(tmp) * 8 / (n / FPS) / 1e6, 2)})
        os.remove(tmp)
    rep['crf16PerScene'] = pr
json.dump(rep, open(os.path.join(LOG, 'assemble.json'), 'w'), indent=1)
print(json.dumps({k: rep[k] for k in ('picture', 'video', 'pictureSeconds', 'muxSeconds') if k in rep}, indent=1))
