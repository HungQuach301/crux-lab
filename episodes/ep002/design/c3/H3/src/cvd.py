#!/usr/bin/env python3
"""Role colours of H3: CIEDE2000 between every pair of roles that must be told apart, normal vision and simulated
protanopia / deuteranopia (Machado, Oliveira & Fernandes 2009, severity 1.0, linear RGB); greyscale contrast (WCAG luminance)."""
import math, itertools
ROLES = {'warn (rate above 9%)': '#F2B441', 'negative (costlier in total)': '#E5484D', 'positive (cushion / saving)': '#3FBF7F',
         'accent (T-bill ridge)': '#4C8DFF', 'ink (Leah: diamond, track)': '#F2F4F7', 'ink-muted (fixed rail, coins)': '#9AA4B2',
         'grid (not costlier cell)': '#2A303B'}
PAIRS = [('warn', 'negative'), ('warn', 'positive'), ('positive', 'negative'), ('negative', 'grid'), ('warn', 'grid'),
         ('accent', 'warn'), ('accent', 'positive'), ('accent', 'negative'), ('ink', 'ink-muted'), ('negative', 'ink-muted'), ('warn', 'ink-muted'), ('positive', 'ink-muted')]
M = {'protan': [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
     'deutan': [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]]}
lin = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def rgb(h): return [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
def sim(h, m):
    l = [lin(c) for c in rgb(h)]
    return [min(1, max(0, sum(m[i][j] * l[j] for j in range(3)))) for i in range(3)]
def lab(l):
    X = 0.4124 * l[0] + 0.3576 * l[1] + 0.1805 * l[2]; Y = 0.2126 * l[0] + 0.7152 * l[1] + 0.0722 * l[2]; Z = 0.0193 * l[0] + 0.1192 * l[1] + 0.9505 * l[2]
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(X / 0.95047), f(Y), f(Z / 1.08883)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)
def de2000(a, b):
    L1, a1, b1 = a; L2, a2, b2 = b
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2); Cb = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7))); a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1 = math.degrees(math.atan2(b1, a1p)) % 360; h2 = math.degrees(math.atan2(b2, a2p)) % 360
    dL, dC = L2 - L1, C2p - C1p
    dh = 0 if C1p * C2p == 0 else (h2 - h1 if abs(h2 - h1) <= 180 else h2 - h1 - 360 if h2 > h1 else h2 - h1 + 360)
    dH = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dh / 2))
    Lb, Cbp = (L1 + L2) / 2, (C1p + C2p) / 2
    hb = h1 + h2 if C1p * C2p == 0 else ((h1 + h2) / 2 if abs(h1 - h2) <= 180 else (h1 + h2 + 360) / 2 if h1 + h2 < 360 else (h1 + h2 - 360) / 2)
    T = 1 - 0.17 * math.cos(math.radians(hb - 30)) + 0.24 * math.cos(math.radians(2 * hb)) + 0.32 * math.cos(math.radians(3 * hb + 6)) - 0.20 * math.cos(math.radians(4 * hb - 63))
    SL = 1 + 0.015 * (Lb - 50) ** 2 / math.sqrt(20 + (Lb - 50) ** 2); SC = 1 + 0.045 * Cbp; SH = 1 + 0.015 * Cbp * T
    RT = -2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7)) * math.sin(math.radians(60 * math.exp(-((hb - 275) / 25) ** 2)))
    return math.sqrt((dL / SL) ** 2 + (dC / SC) ** 2 + (dH / SH) ** 2 + RT * (dC / SC) * (dH / SH))
def Y(h): l = [lin(c) for c in rgb(h)]; return 0.2126 * l[0] + 0.7152 * l[1] + 0.0722 * l[2]
key = {k.split(' ')[0]: v for k, v in ROLES.items()}
print('| pair | normal ΔE00 | protan ΔE00 | deutan ΔE00 | greyscale contrast |'); print('|---|---|---|---|---|')
for a, b in PAIRS:
    n = de2000(lab([lin(c) for c in rgb(key[a])]), lab([lin(c) for c in rgb(key[b])]))
    p = de2000(lab(sim(key[a], M['protan'])), lab(sim(key[b], M['protan'])))
    d = de2000(lab(sim(key[a], M['deutan'])), lab(sim(key[b], M['deutan'])))
    ya, yb = Y(key[a]), Y(key[b]); g = (max(ya, yb) + 0.05) / (min(ya, yb) + 0.05)
    print(f'| {a} {key[a]} / {b} {key[b]} | {n:.1f} | {p:.1f} | {d:.1f} | {g:.2f}:1 |')
