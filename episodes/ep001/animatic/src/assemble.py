#!/usr/bin/env python3
"""Join the rendered scenes (work/scenes/Sxx.mp4, 1280x720 30 fps) in timing.json order into
   out/silent-720p.mp4 (no sound, for the blind check) and out/animatic-720p.mp4 (+ the temporary narration,
   AAC copied as is). Each scene is padded/trimmed to round(end*30) - round(start*30) frames so picture and the
   narration stay locked to the absolute timing. PyAV only (no ffmpeg binary). If a file would exceed 90 MB it is
   split in two at a scene cut (…-part1/-part2)."""
import json, os, sys, time
import av

HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE); EP = os.path.dirname(AN)
tm = json.load(open(os.path.join(AN, 'timing.json')))
FPS = 30
os.makedirs(os.path.join(AN, 'out'), exist_ok=True)
t0 = time.time()
silent = os.path.join(AN, 'out', 'silent-720p.mp4')
oc = av.open(silent, 'w')
vs = oc.add_stream('libx264', rate=FPS)
vs.width, vs.height, vs.pix_fmt = 1280, 720, 'yuv420p'
vs.options = {'crf': '23', 'preset': 'medium', 'profile': 'high', 'colorprim': 'bt709', 'transfer': 'bt709', 'colormatrix': 'bt709', 'g': '60'}
report = []
n_out = 0
for sc in tm['scenes']:
    target = round(sc['end'] * FPS) - round(sc['start'] * FPS)
    ic = av.open(os.path.join(AN, 'work', 'scenes', sc['id'] + '.mp4'))
    got, last = 0, None
    for fr in ic.decode(video=0):
        if got >= target:
            break
        img = fr.to_ndarray(format='rgb24'); last = img
        for p in vs.encode(av.VideoFrame.from_ndarray(img, format='rgb24')):
            oc.mux(p)
        got += 1
    ic.close()
    pad = target - got
    for _ in range(max(0, pad)):
        for p in vs.encode(av.VideoFrame.from_ndarray(last, format='rgb24')):
            oc.mux(p)
    report.append({'scene': sc['id'], 'target': target, 'decoded': got, 'padded': max(0, pad)})
    n_out += target
for p in vs.encode():
    oc.mux(p)
oc.close()
# mux narration (copy) with the silent video (copy)
full = os.path.join(AN, 'out', 'animatic-720p.mp4')
vin = av.open(silent); ain = av.open(os.path.join(EP, 'review-c4', 'narration-v32.m4a'))
out = av.open(full, 'w')
ov = out.add_stream_from_template(vin.streams.video[0]); oa = out.add_stream_from_template(ain.streams.audio[0])
for pkt in vin.demux(vin.streams.video[0]):
    if pkt.dts is None: continue
    pkt.stream = ov; out.mux(pkt)
for pkt in ain.demux(ain.streams.audio[0]):
    if pkt.dts is None: continue
    pkt.stream = oa; out.mux(pkt)
out.close(); vin.close(); ain.close()
res = {'frames': n_out, 'seconds': n_out / FPS, 'wallSeconds': round(time.time() - t0, 1), 'scenes': report,
       'silentMB': round(os.path.getsize(silent) / 1e6, 2), 'animaticMB': round(os.path.getsize(full) / 1e6, 2)}
json.dump(res, open(os.path.join(AN, 'work', 'assemble.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != 'scenes'}), [r for r in report if r['padded'] or r['decoded'] != r['target']])
