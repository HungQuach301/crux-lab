#!/usr/bin/env python3
"""Patch a SCRATCH copy of the C4 animatic engine (git archive 86e5830 episodes/ep001/animatic); never the repo copy.
1) text(): every call records its box in window.TBOX (when set), like the C5 page's CHECKS.objects() text boxes (same
   formula: [x0, y-0.76px, x0+w, y+0.22px]), mapped to output-canvas pixels with the context's current transform.
   Nothing is drawn differently.
2) ptxt() (text printed into 3D canvas textures - letter, folder tab, house fronts; not in TBOX): when the page is loaded
   with window.MASKTEX = true, it paints a solid #FF00FF block over the glyph extent instead of the glyphs. grab.js renders
   each frame with and without it; pixels that differ = where texture text lands on screen (masked by finish.py).
Usage: patch_c4.py <copy>/src/engine.js"""
import sys
p = sys.argv[1]
s = open(p).read()
old = "  ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y);\n  ctx.restore();\n  if (alpha >= 0.2) {"
assert s.count(old) == 1, 'text() anchor not found'
s = s.replace(old, "  ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x, y);\n"
  "  if (window.TBOX) { const M = ctx.getTransform(), P = [[x0, top], [x0 + w, top], [x0, bot], [x0 + w, bot]].map(([u, v]) => [M.a * u + M.c * v + M.e, M.b * u + M.d * v + M.f]);\n"
  "    window.TBOX.push({ text: s, tier, fontPx: px, scale: Math.hypot(M.a, M.b), alpha, shadow: !!o.shadow, box: [Math.min(...P.map((q) => q[0])), Math.min(...P.map((q) => q[1])), Math.max(...P.map((q) => q[0])), Math.max(...P.map((q) => q[1]))] }); }\n"
  "  ctx.restore();\n  if (alpha >= 0.2) {")
old2 = "  g.font = `${weight} ${size}px Inter`; g.fillStyle = color; g.textAlign = align; g.textBaseline = 'alphabetic'; g.fillText(s, x, y);\n"
assert s.count(old2) == 1, 'ptxt() anchor not found'
s = s.replace(old2, "  g.font = `${weight} ${size}px Inter`; g.fillStyle = color; g.textAlign = align; g.textBaseline = 'alphabetic';\n"
  "  if (window.MASKTEX) { const m = g.measureText(s); g.save(); g.fillStyle = '#FF00FF'; g.fillRect(x - m.actualBoundingBoxLeft - 4, y - m.actualBoundingBoxAscent - 4, m.actualBoundingBoxLeft + m.actualBoundingBoxRight + 8, m.actualBoundingBoxAscent + m.actualBoundingBoxDescent + 8); g.restore(); return; }\n"
  "  g.fillText(s, x, y);\n")
open(p, 'w').write(s)
print('patched', p)
