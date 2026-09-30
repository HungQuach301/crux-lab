#!/usr/bin/env python3
"""Compose episodes/ep001/review-c3/contract.mp4: 1 s title card before each style frame, 1280x720, 30 fps, H.264,
no audio. Inputs: ../SF1.mp4 .. ../SF6.mp4 (1920x1080) and ../work/card-*.png (cards.js). PyAV only (no ffmpeg)."""
import os, sys, av, numpy as np
from PIL import Image
FIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.normpath(os.path.join(FIN, '..', '..', '..', 'review-c3', 'contract.mp4'))
W, H, FPS = 1280, 720, 30
ORDER = ['SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6']
c = av.open(OUT, 'w')
st = c.add_stream('libx264', rate=FPS)
st.width, st.height, st.pix_fmt = W, H, 'yuv420p'
st.options = {'crf': '20', 'preset': 'slow', 'profile': 'high', 'colorprim': 'bt709', 'transfer': 'bt709', 'colormatrix': 'bt709'}
n = 0
def put(img):
    global n
    fr = av.VideoFrame.from_ndarray(np.asarray(img.convert('RGB').resize((W, H), Image.LANCZOS)), format='rgb24')
    for p in st.encode(fr): c.mux(p)
    n += 1
def card(name, secs=1.0):
    im = Image.open(os.path.join(FIN, 'work', f'card-{name}.png'))
    for _ in range(int(secs * FPS)): put(im)
card('0', 1.5)
for F in ORDER:
    card(F)
    with av.open(os.path.join(FIN, F + '.mp4')) as src:
        for fr in src.decode(video=0): put(fr.to_image())
for p in st.encode(): c.mux(p)
c.close()
print(f'{OUT}: {n} frames = {n / FPS:.1f} s, {os.path.getsize(OUT) / 1e6:.2f} MB')
