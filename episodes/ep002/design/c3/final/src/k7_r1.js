// KEY-7 (S09.2-S10.3), base H3 (history timeline: the ridge + one cell per start month in two bins under its two
// halves) + the H2 head-start bracket swept into a WEDGE. Redesigned after the C3 blind read (strips ended on the sweep
// back to -1, so 2/3 readers saw "red growing"). Order is now one-way: start at the NARROW/REVERSED side (-1 point:
// both bins mostly red), then WIDEN only: -1 -> 1.5 (Leah) -> 2 (right half clears) -> 3 (left half keeps a thin red
// layer), and hold there. The clip and the strip END on the wide-gap state (red at its minimum); there is no sweep back.
// Under each half a small ladder keeps one bar per tested head start (bar = share costlier in that half), so every
// frame shows the trail: wedge wider -> bars shorter; right ladder hits zero, left ladder never does.
import { C, DATA, CL, text, badge, line, rect, srect, negArea, diamond, ridgeGeom, drawRidge, ridgeIndex, STARTS,
  SPLIT_J, ease, mix, clamp, inout } from './engine.js';
export const duration = 10.0;
export const stripTimes = [0.9, 2.3, 3.9, 5.8, 7.7, 9.8];
const G = ridgeGeom(110, 1810, 150, 390, 16.5);
const GS = [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3];
const KEYS = [[0, -1], [1.2, -1], [3.4, 1.5], [4.3, 1.5], [5.2, 2], [6.2, 2], [7.4, 3], [10, 3]];
function gAt(t) { for (let i = 0; i < KEYS.length - 1; i++) { const [a, va] = KEYS[i], [b, vb] = KEYS[i + 1]; if (t <= b) return mix(va, vb, ease(t, a, b)); } return 3; }
function seg(g) { const i = Math.max(0, Math.min(GS.length - 2, Math.floor((g + 1) / 0.5 + 1e-9))); return [i, clamp((g - GS[i]) / 0.5)]; }
const share = (g, half) => { const [i, f] = seg(g); return mix(DATA.gap[String(GS[i])][half], DATA.gap[String(GS[i + 1])][half], f); };
// cells: one per start month; column = start year (under that year of the ridge), row = month
const J0 = ridgeIndex(STARTS[0]), DX = (G.x1 - G.x0) / G.n, CY0 = 412, CHh = 14;
const XS = G.X(J0 + SPLIT_J);
const cellX = (j) => G.X(J0 + j - (j % 12)), cellY = (j) => CY0 + (j % 12) * CHh;
// ladders under the two halves
const LAD = { early: [G.x0 + 40, XS - 64], late: [XS + 64, XS + 64 + (XS - 64 - G.x0 - 40) * 1.25] };
const BASE = 822, BH = 220, RAIL = 874, PP = 38, BW = 34;
const lx = (half, g) => { const [a, b] = LAD[half]; return mix(a, b, (g + 1) / 4); };
function ladder(ctx, half, g, t, a) {
  const [x0, x1] = LAD[half];
  // the wedge = the head start swept so far (warn while the variable rate starts above 9%, cushion once below)
  const gm = Math.max(-1, g), pts = (from, to) => { const p = []; for (let k = 0; k <= 40; k++) { const v = mix(from, to, k / 40); p.push([lx(half, v), RAIL + v * PP]); } return p; };
  const negTo = Math.min(gm, 0);
  if (negTo > -1) { const p = pts(-1, negTo); ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.warn; ctx.beginPath(); ctx.moveTo(lx(half, -1), RAIL); p.forEach((q) => ctx.lineTo(...q)); ctx.lineTo(lx(half, negTo), RAIL); ctx.closePath(); ctx.fill(); ctx.restore(); }
  if (gm > 0) { const p = pts(0, gm); ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.cushion; ctx.beginPath(); ctx.moveTo(lx(half, 0), RAIL); p.forEach((q) => ctx.lineTo(...q)); ctx.lineTo(lx(half, gm), RAIL); ctx.closePath(); ctx.fill(); ctx.restore(); }
  line(ctx, [[x0 - BW, RAIL], [x1 + BW, RAIL]], C.muted, 8, { cap: 'butt', alpha: a }); // the 9% rail
  // bars: one per tested head start already reached; the live bar follows the slider
  for (const v of GS) {
    line(ctx, [[lx(half, v) - BW / 2 - 4, BASE + 1], [lx(half, v) + BW / 2 + 4, BASE + 1]], C.grid, 4, { cap: 'butt', alpha: a });
    if (v <= g + 1e-6) { const h = BH * DATA.gap[String(v)][half] / 100; negArea(ctx, lx(half, v) - BW / 2, BASE - h, BW, h, a, 16); }
  }
  const hl = BH * share(g, half) / 100; negArea(ctx, lx(half, g) - BW / 2, BASE - hl, BW, hl, a, 16);
  srect(ctx, lx(half, g) - BW / 2 - 7, BASE - Math.max(hl, 0) - 7, BW + 14, Math.max(hl, 0) + 14, C.ink, 4, a * (hl > 0.5 ? 1 : 0));
  // Leah's offer (1.5 points) stays marked by her diamond on the wedge edge once reached
  diamond(ctx, lx(half, Math.min(g, 1.5)), RAIL + Math.min(g, 1.5) * PP, 20, a * (g > -0.98 ? 1 : 0) * (g >= 1.5 ? 1 : 0.0) + a * (g < 1.5 && g > -0.98 ? 1 : 0));
}
export function draw(ctx, t) {
  const g = gAt(t), a = ease(t, 0, 0.6);
  drawRidge(ctx, G, a, 1);
  line(ctx, [[XS, G.y0 - 10], [XS, 1000]], C.muted, 3, { alpha: 0.75 * a, dash: [12, 12], cap: 'butt' });
  // the two bins of result cells (red = costlier in total at the current head start)
  const [i, f] = seg(g), A = DATA.gap[String(GS[i])].costlier, B = DATA.gap[String(GS[i + 1])].costlier;
  for (let j = 0; j < STARTS.length; j++) {
    const x = cellX(j) + 1.5, y = cellY(j) + 1.5, w = DX * 12 - 3, h = CHh - 3;
    rect(ctx, x, y, w, h, C.grid, a);
    const r = mix(A[j] === '1' ? 1 : 0, B[j] === '1' ? 1 : 0, f);
    if (r > 0.01) rect(ctx, x, y, w, h, C.costlier, r * a);
  }
  for (const [x0, x1, half] of [[cellX(0) - 8, XS - 6, 'early'], [XS + 6, cellX(STARTS.length - 1) + DX * 12 + 8, 'late']]) {
    const clear = share(g, half) < 0.05;
    srect(ctx, x0, CY0 - 8, x1 - x0, 12 * CHh + 16, clear ? C.ink : C.grid, 4, a);
  }
  ladder(ctx, 'early', g, t, a); ladder(ctx, 'late', g, t, a);
  // one number per moment (claims): Leah's head start; right half none at 2 points; left half still 10.5% at 3 points
  text(ctx, CL('gap_start'), lx('early', 1.5), 1040, 'label', { align: 'center', alpha: inout(t, 3.5, 3.8, 4.4, 4.7) });
  text(ctx, CL('gap20_late'), lx('late', 2) - 20, 760, 'number', { alpha: inout(t, 5.3, 5.6, 6.6, 6.9) });
  text(ctx, CL('gap30_early'), lx('early', 3) + BW / 2, 686, 'number', { align: 'right', alpha: ease(t, 7.5, 7.8) });
  badge(ctx, a);
}
