#!/usr/bin/env python3
"""Colour self-check (lesson D3): CIEDE2000 between every pair of roles that must be told apart, under normal vision and
under protan / deutan simulation (Machado, Oliveira & Fernandes 2009, severity 1.0, applied in linear RGB), plus the
greyscale (relative-luminance) contrast of each pair. Writes ../work/cvd.json and prints a markdown table.
python3 src/cvd.py"""
import json, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
TOK = {'bg': '#0E1116', 'surface': '#171B22', 'grid': '#2A303B', 'ink': '#F2F4F7', 'ink-muted': '#9AA4B2',
       'accent': '#4C8DFF', 'warn': '#F2B441', 'positive': '#3FBF7F', 'negative': '#E5484D'}
# roles in H2 (role -> token)
ROLES = {'fixed rail (ink-muted)': 'ink-muted', 'T-bill ridge / variable line (accent)': 'accent',
         'rate above 9% (warn)': 'warn', 'costlier in total (negative)': 'negative', 'cushion / saving (positive)': 'positive',
         'Leah diamond (ink)': 'ink', 'not costlier token (ink-muted)': 'ink-muted'}
PAIRS = [('warn', 'negative'), ('positive', 'negative'), ('positive', 'warn'), ('accent', 'ink-muted'),
         ('ink-muted', 'negative'), ('accent', 'positive'), ('accent', 'warn'), ('accent', 'negative'), ('ink', 'warn'),
         ('ink', 'ink-muted'), ('ink', 'accent'), ('ink-muted', 'positive'), ('ink-muted', 'warn')]
MP = np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]])
MD = np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]])
def lin(c): c = np.asarray(c, float); return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
def unlin(c): c = np.clip(c, 0, 1); return np.where(c <= 0.0031308, 12.92 * c, 1.055 * c ** (1 / 2.4) - 0.055)
def rgb(h): return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)]) / 255
def sim(h, M): return unlin(M @ lin(rgb(h)))
def lab(c):
    l = lin(c); M = np.array([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]])
    x = M @ l / np.array([0.95047, 1.0, 1.08883])
    f = np.where(x > 216 / 24389, np.cbrt(x), (24389 / 27 * x + 16) / 116)
    return np.array([116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])])
def de2000(a, b):
    L1, a1, b1 = a; L2, a2, b2 = b
    C1, C2 = np.hypot(a1, b1), np.hypot(a2, b2); Cb = (C1 + C2) / 2
    G = 0.5 * (1 - np.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = np.hypot(a1p, b1), np.hypot(a2p, b2)
    h1p, h2p = np.degrees(np.arctan2(b1, a1p)) % 360, np.degrees(np.arctan2(b2, a2p)) % 360
    dL, dC = L2 - L1, C2p - C1p
    dh = h2p - h1p
    if C1p * C2p == 0: dh = 0
    elif dh > 180: dh -= 360
    elif dh < -180: dh += 360
    dH = 2 * np.sqrt(C1p * C2p) * np.sin(np.radians(dh / 2))
    Lb, Cbp = (L1 + L2) / 2, (C1p + C2p) / 2
    hb = h1p + h2p
    if C1p * C2p != 0:
        hb = (h1p + h2p + 360) / 2 if abs(h1p - h2p) > 180 else (h1p + h2p) / 2
    T = 1 - 0.17 * np.cos(np.radians(hb - 30)) + 0.24 * np.cos(np.radians(2 * hb)) + 0.32 * np.cos(np.radians(3 * hb + 6)) - 0.20 * np.cos(np.radians(4 * hb - 63))
    dth = 30 * np.exp(-((hb - 275) / 25) ** 2)
    RC = 2 * np.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    SL = 1 + 0.015 * (Lb - 50) ** 2 / np.sqrt(20 + (Lb - 50) ** 2); SC = 1 + 0.045 * Cbp; SH = 1 + 0.015 * Cbp * T
    RT = -np.sin(np.radians(2 * dth)) * RC
    return float(np.sqrt((dL / SL) ** 2 + (dC / SC) ** 2 + (dH / SH) ** 2 + RT * (dC / SC) * (dH / SH)))
def Y(c): l = lin(c); return float(0.2126 * l[0] + 0.7152 * l[1] + 0.0722 * l[2])
def cr(a, b): ya, yb = sorted([Y(a), Y(b)]); return (yb + 0.05) / (ya + 0.05)
rows = []
for p, q in PAIRS:
    A, B = TOK[p], TOK[q]
    r = {'pair': f'{p} {A} / {q} {B}', 'normal': de2000(lab(rgb(A)), lab(rgb(B))),
         'protan': de2000(lab(sim(A, MP)), lab(sim(B, MP))), 'deutan': de2000(lab(sim(A, MD)), lab(sim(B, MD))),
         'grey': cr(rgb(A), rgb(B))}
    rows.append(r)
os.makedirs(os.path.join(HERE, '..', 'work'), exist_ok=True)
json.dump(rows, open(os.path.join(HERE, '..', 'work', 'cvd.json'), 'w'), indent=1)
print('| pair | ΔE00 normal | protan | deutan | greyscale contrast |\n|---|---|---|---|---|')
for r in rows:
    print(f"| {r['pair']} | {r['normal']:.1f} | {r['protan']:.1f} | {r['deutan']:.1f} | {r['grey']:.2f}:1 |")
print('\ntext contrast on bg:', {k: round(cr(rgb(TOK[k]), rgb(TOK['bg'])), 2) for k in TOK})
print('bg text on warn badge:', round(cr(rgb(TOK['bg']), rgb(TOK['warn'])), 2))
