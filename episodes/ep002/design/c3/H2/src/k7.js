// KEY-7 (S09.4-S10.3): a slider widens the head start; red drains out of both bins; the right bin (falling half) goes
// fully grey partway; the left bin (climbing half) always keeps a thin red layer; the extra block shrinks but never
// vanishes; sweeping back (smaller, none, reversed) both bins refill and the block grows.
import { C, DATA, CL, text, numWord, badge, line, rect, srect, negArea, diamond, ridgeGeom, drawRidge, binGeom,
  ease, mix, clamp, FIXED } from './engine.js';
export const duration = 10.0;
export const stripTimes = [0.5, 2.2, 3.8, 6.4, 8.3, 9.8];
const G = ridgeGeom(720, 1820, 210, 620, 16.5);
const B = binGeom(G);
const BY0 = 690, BY1 = 860;
const R = 260, PP = 80, SX = 240, BXx = 300; // rail y, px per point, slider x, bracket x
const BW = 230, BX = 200, BB = 1010, FH = 250;
const KEYS = [[0, 1.5], [1.0, 1.5], [3.0, 2.0], [4.4, 2.0], [5.8, 3.0], [7.0, 3.0], [9.2, -1.0], [10, -1.0]];
function gAt(t) { for (let i = 0; i < KEYS.length - 1; i++) { const [a, va] = KEYS[i], [b, vb] = KEYS[i + 1]; if (t <= b) return mix(va, vb, ease(t, a, b)); } return -1; }
const GS = [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3];
function at(g, key) { // piecewise-linear between the tested head starts (only exact stops are ever labelled)
  const i = Math.max(0, Math.min(GS.length - 2, Math.floor((g + 1) / 0.5))); const f = clamp((g - GS[i]) / 0.5);
  return mix(DATA.gap[String(GS[i])][key], DATA.gap[String(GS[i + 1])][key], f);
}
export function draw(ctx, t) {
  const g = gAt(t), by = R + g * PP;
  // slider track with ticks every half point; the rail is pinned
  line(ctx, [[SX, R - 1.2 * PP], [SX, R + 3.2 * PP]], C.muted, 4, { cap: 'butt' });
  for (const v of GS) line(ctx, [[SX - 18, R + v * PP], [SX, R + v * PP]], C.muted, 4, { cap: 'butt' });
  line(ctx, [[SX - 30, R], [470, R]], C.ink, 10, { cap: 'butt' });
  // bracket = head start (positive below the rail, warn when reversed)
  const colr = g > 0.03 ? C.positive : g < -0.03 ? C.warn : C.ink;
  if (Math.abs(g) > 0.06) line(ctx, [[BXx + 26, R], [BXx, R], [BXx, by], [BXx + 26, by]], colr, 10, { cap: 'butt' });
  else { line(ctx, [[BXx - 8, R - 15], [BXx + 26, R - 15]], colr, 8, { cap: 'butt' }); line(ctx, [[BXx - 8, R + 15], [BXx + 26, R + 15]], colr, 8, { cap: 'butt' }); }
  diamond(ctx, BXx + 56, by, 30);
  // the history and the two bins under its halves, as share bars (costlier part red, from the left)
  drawRidge(ctx, G, 1, 1);
  for (const [[x0, x1], key] of [[[B.L[0], B.L[1] - 10], 'early'], [[B.R[0] + 10, B.R[1]], 'late']]) {
    srect(ctx, x0 - 5, BY0 - 5, x1 - x0 + 10, BY1 - BY0 + 10, C.grid, 4);
    const sh = at(g, key) / 100, wr = (x1 - x0) * sh;
    rect(ctx, x0 + wr, BY0, x1 - x0 - wr, BY1 - BY0, C.muted, 0.55);
    negArea(ctx, x0, BY0, wr, BY1 - BY0, 1);
  }
  // interest blocks: fixed (grey) + worst extra (red) on top
  const eh = FH * at(g, 'worst') / DATA.fixInt;
  rect(ctx, BX, BB - FH, BW, FH, C.muted, 0.85);
  negArea(ctx, BX, BB - FH - eh, BW, eh, 1);
  // one number per moment, next to the bead
  const lx = BXx + 110;
  text(ctx, CL('gap_start'), lx, by + 22, 'label', { alpha: 1 - ease(t, 0.9, 1.2) });
  text(ctx, CL('spread2_share'), lx, by + 30, 'number', { alpha: Math.min(ease(t, 3.0, 3.3), 1 - ease(t, 4.2, 4.4)) });
  text(ctx, CL('spread3_share'), lx, by + 30, 'number', { alpha: Math.min(ease(t, 5.8, 6.1), 1 - ease(t, 6.8, 7.0)) });
  badge(ctx, 1);
}
