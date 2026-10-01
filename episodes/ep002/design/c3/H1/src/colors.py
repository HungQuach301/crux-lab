#!/usr/bin/env python3
"""D3 check: ΔE2000 between role colours that must be told apart, normal vision and simulated protanopia/deuteranopia
(Machado, Oliveira & Fernandes 2009, severity 1.0, applied in linear sRGB), plus greyscale contrast (WCAG luminance
ratio). Token hexes AND colours sampled from rendered frames (lit 3D surfaces).  python3 src/colors.py [sampled.json]"""
import json, math, sys

MACHADO = {
    'protan': [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    'deutan': [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
}
def h2rgb(h): return [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
def lin(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def delin(c): c = min(1, max(0, c)); return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
def sim(rgb, kind):
    if kind == 'normal': return rgb
    l = [lin(c) for c in rgb]; m = MACHADO[kind]
    return [delin(sum(m[i][j] * l[j] for j in range(3))) for i in range(3)]
def lab(rgb):
    r, g, b = [lin(c) for c in rgb]
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047; y = 0.2126 * r + 0.7152 * g + 0.0722 * b; z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    return 116 * f(y) - 16, 500 * (f(x) - f(y)), 200 * (f(y) - f(z))
def de2000(l1, l2):
    L1, a1, b1 = l1; L2, a2, b2 = l2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2); Cb = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7)))
    a1p, a2p = a1 * (1 + G), a2 * (1 + G); C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1 = math.degrees(math.atan2(b1, a1p)) % 360; h2 = math.degrees(math.atan2(b2, a2p)) % 360
    dL, dC = L2 - L1, C2p - C1p
    dh = 0 if C1p * C2p == 0 else (h2 - h1 if abs(h2 - h1) <= 180 else h2 - h1 - 360 if h2 > h1 else h2 - h1 + 360)
    dH = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dh / 2))
    Lb, Cbp = (L1 + L2) / 2, (C1p + C2p) / 2
    hb = h1 + h2 if C1p * C2p == 0 else ((h1 + h2) / 2 if abs(h1 - h2) <= 180 else (h1 + h2 + 360) / 2 if h1 + h2 < 360 else (h1 + h2 - 360) / 2)
    T = 1 - 0.17 * math.cos(math.radians(hb - 30)) + 0.24 * math.cos(math.radians(2 * hb)) + 0.32 * math.cos(math.radians(3 * hb + 6)) - 0.2 * math.cos(math.radians(4 * hb - 63))
    Sl = 1 + 0.015 * (Lb - 50) ** 2 / math.sqrt(20 + (Lb - 50) ** 2); Sc = 1 + 0.045 * Cbp; Sh = 1 + 0.015 * Cbp * T
    Rt = -2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7)) * math.sin(math.radians(60 * math.exp(-((hb - 275) / 25) ** 2)))
    return math.sqrt((dL / Sl) ** 2 + (dC / Sc) ** 2 + (dH / Sh) ** 2 + Rt * (dC / Sc) * (dH / Sh))
def Y(rgb): r, g, b = [lin(c) for c in rgb]; return 0.2126 * r + 0.7152 * g + 0.0722 * b
def gray_ratio(a, b): ya, yb = Y(a), Y(b); return (max(ya, yb) + 0.05) / (min(ya, yb) + 0.05)

ROLE = {  # role -> token hex (what the brief calls the role colour)
    'warn (rate above 9%: rail glow)': '#F2B441', 'negative (costlier: tiles, extra coins)': '#E5484D',
    'positive (cushion jar, head-start bracket)': '#3FBF7F', 'accent (T-bill ridge)': '#4C8DFF',
    'ink-muted (fixed rail steel tone, not-costlier tiles)': '#9AA4B2', 'ink (Leah: diamond bead)': '#F2F4F7',
}
PAIRS = [('warn', 'negative'), ('negative', 'ink-muted'), ('positive', 'negative'), ('positive', 'warn'), ('warn', 'ink-muted'),
         ('accent', 'positive'), ('accent', 'ink-muted'), ('ink (', 'ink-muted'), ('ink (', 'warn'), ('accent', 'negative')]
def run(colors, title):
    keys = list(colors)
    find = lambda p: next(k for k in keys if k.startswith(p))
    print(f'\n## {title}\n\n| pair | ΔE00 normal | ΔE00 protan | ΔE00 deutan | grey ratio |\n|---|---|---|---|---|')
    worst = []
    for a, b in PAIRS:
        try: ka, kb = find(a), find(b)
        except StopIteration: continue
        ca, cb = h2rgb(colors[ka]), h2rgb(colors[kb])
        d = [de2000(lab(sim(ca, k)), lab(sim(cb, k))) for k in ('normal', 'protan', 'deutan')]
        g = gray_ratio(ca, cb)
        worst.append((min(d[1:]), ka.split(' ')[0], kb.split(' ')[0]))
        print(f'| {ka.split(" (")[0]} {colors[ka]} vs {kb.split(" (")[0]} {colors[kb]} | {d[0]:.1f} | {d[1]:.1f} | {d[2]:.1f} | {g:.2f}:1 |')
    return worst
w = run(ROLE, 'Token colours')
if len(sys.argv) > 1:
    run(json.load(open(sys.argv[1])), 'Colours sampled from rendered frames (lit 3D)')
