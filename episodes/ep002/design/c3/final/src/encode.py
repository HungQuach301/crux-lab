#!/usr/bin/env python3
"""Read raw RGBA frames (W*H*4 bytes each) from stdin and encode H.264 (High, yuv420p, BT.709) with PyAV. CPU only.
   python3 encode.py out.mp4 W H FPS [crf]"""
import sys, av, numpy as np
out, W, H, FPS = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
crf = sys.argv[5] if len(sys.argv) > 5 else '18'
c = av.open(out, 'w')
st = c.add_stream('libx264', rate=FPS)
st.width, st.height, st.pix_fmt = W, H, 'yuv420p'
st.options = {'crf': crf, 'preset': 'slow', 'profile': 'high', 'colorprim': 'bt709', 'transfer': 'bt709', 'colormatrix': 'bt709'}
n, sz, buf = 0, W * H * 4, sys.stdin.buffer
while True:
    b = buf.read(sz)
    if len(b) < sz:
        break
    fr = av.VideoFrame.from_ndarray(np.frombuffer(b, np.uint8).reshape(H, W, 4)[:, :, :3].copy(), format='rgb24')
    for p in st.encode(fr):
        c.mux(p)
    n += 1
for p in st.encode():
    c.mux(p)
c.close()
print(f'encoded {n} frames -> {out}', file=sys.stderr)
