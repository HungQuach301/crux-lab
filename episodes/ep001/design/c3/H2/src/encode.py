#!/usr/bin/env python3
"""Encode a PNG frame sequence to H.264 MP4 (yuv420p, BT.709, 30 fps CFR) with PyAV. No ffmpeg binary needed.
usage: encode.py <frames dir> <out.mp4> [fps] [crf]"""
import sys, os, glob, time
import av
from fractions import Fraction

src, out = sys.argv[1], sys.argv[2]
fps = int(sys.argv[3]) if len(sys.argv) > 3 else 30
crf = sys.argv[4] if len(sys.argv) > 4 else '26'
files = sorted(glob.glob(os.path.join(src, 'f*.png')))
t0 = time.time()
o = av.open(out, 'w')
s = o.add_stream('libx264', rate=Fraction(fps, 1))
s.time_base = Fraction(1, fps)
s.codec_context.time_base = Fraction(1, fps)
s.width, s.height, s.pix_fmt = 1280, 720, 'yuv420p'
s.options = {'crf': crf, 'preset': 'slow', 'profile': 'high', 'movflags': '+faststart',
             'x264-params': 'colorprim=bt709:transfer=bt709:colormatrix=bt709:range=tv'}
for i, f in enumerate(files):
    with av.open(f) as c:
        fr = next(c.decode(video=0))
    fr = fr.reformat(width=1280, height=720, format='yuv420p', dst_colorspace='ITU709', src_colorspace='ITU709')
    fr.pts = i
    fr.time_base = Fraction(1, fps)
    for p in s.encode(fr):
        o.mux(p)
for p in s.encode():
    o.mux(p)
o.close()
print(f'encoded {len(files)} frames -> {out} ({os.path.getsize(out)/1e6:.2f} MB) in {time.time()-t0:.1f}s')
