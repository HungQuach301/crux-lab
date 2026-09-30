# Read raw RGBA 1280x720 frames from stdin, encode H.264 (yuv420p, 30 fps) with PyAV. CPU only.
#   python3 encode.py out.mp4 [nframes]
import sys, av, numpy as np
W, H, FPS = 1280, 720, 30
out = av.open(sys.argv[1], 'w')
st = out.add_stream('libx264', rate=FPS)
st.width, st.height, st.pix_fmt = W, H, 'yuv420p'
st.options = {'crf': '18', 'preset': 'slow', 'profile': 'high', 'colorprim': 'bt709', 'transfer': 'bt709', 'colormatrix': 'bt709'}
n = 0
buf = sys.stdin.buffer
while True:
    b = buf.read(W * H * 4)
    if len(b) < W * H * 4: break
    a = np.frombuffer(b, np.uint8).reshape(H, W, 4)[:, :, :3]
    fr = av.VideoFrame.from_ndarray(np.ascontiguousarray(a), format='rgb24')
    for p in st.encode(fr): out.mux(p)
    n += 1
for p in st.encode(): out.mux(p)
out.close()
print(f'encoded {n} frames', file=sys.stderr)
