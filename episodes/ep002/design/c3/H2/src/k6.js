// KEY-6 (S08.1-S08.7): the worst replay. The frame lands on the steepest climb of the left half; the bead climbs far
// above the rail; amber for years; the tank fills a little, empties, sinks deep red; the red folds into a block that
// sits on top of the fixed loan's interest block: a bit under half its height (43%).
import { C, DATA, CL, text, numWord, badge, line, poly, rect, srect, negArea, diamond, plane, replay, tank, ridgeGeom, drawRidge,
  startRidgeIdx, STARTS, ridgeIndex, rateAt, ease, easeOut, back, mix, clamp, lin, FIXED } from './engine.js';
export const duration = 10.0;
export const stripTimes = [0.6, 1.9, 3.6, 5.2, 7.4, 9.8];
const d = DATA.detail['1977-04'];
const P = plane(200, 1200, 190, 760, 3.0, 20.5, 120);
const G = ridgeGeom(200, 1200, 860, 1010, 16.5);
const T = { x: 1300, w: 150, top: 190, yZero: 290, bottom: 760, k: 440 / 11500 };
const nAt = (t) => 120 * clamp((t - 1.7) / 4.6);
// interest blocks (area = interest paid): fixed $26,005, extra $11,219 on top
const BW = 200, BX = 1620, BB = 960, FH = 520, EH = FH * DATA.base[STARTS.indexOf('1977-04')] / DATA.fixInt;
export function draw(ctx, t) {
  const n = nAt(t), k = Math.min(119, Math.floor(n));
  // ridge with the frame sliding in from the left and landing on April 1977
  drawRidge(ctx, G, 1, 1);
  const sTarget = ridgeIndex('1977-04'), sFrom = ridgeIndex('1962-01');
  const s = Math.round(mix(sFrom, sTarget, easeOut(t, 0.0, 1.4)));
  const fw = G.X(120) - G.X(0), land = back(t, 1.2, 1.6);
  srect(ctx, G.X(s), G.y0 - 18 - 24 * (1 - clamp(land, 0, 1)), fw, G.y1 - G.y0 + 18, C.ink, 5);
  // plane
  replay(ctx, P, d.path, Math.max(0, Math.min(119, n)), { beadR: 30, lw: 7, railW: 12, aWarn: 0.75 });
  // tank: fills a little, then drains below zero
  const ta = 1 - ease(t, 6.6, 7.0);
  const v = n <= 0 ? 0 : d.cushion[k];
  if (ta > 0) {
    srect(ctx, T.x, T.top, T.w, T.bottom - T.top, C.grid, 4, ta);
    line(ctx, [[T.x - 14, T.yZero], [T.x + T.w + 14, T.yZero]], C.ink, 5, { alpha: ta, cap: 'butt' });
    if (v > 0) { rect(ctx, T.x + 2, T.yZero - v * T.k, T.w - 4, v * T.k, C.positive, ta); if (d.path[k] > FIXED && n < 119.5) line(ctx, [[T.x - 8, T.yZero - v * T.k], [T.x + T.w + 8, T.yZero - v * T.k]], C.warn, 12, { cap: 'butt', alpha: ta }); }
  }
  // red: in the tank, then it folds into a block and moves onto the fixed interest block
  const mv = ease(t, 6.8, 8.0);
  if (v < 0) {
    const h0 = -v * T.k;
    const x = mix(T.x + 2, BX, mv), w = mix(T.w - 4, BW, mv), y = mix(T.yZero, BB - FH - EH, mv), h = mix(h0, EH, mv);
    negArea(ctx, x, y, w, h, 1);
  }
  // fixed interest block grows up from the base line
  const fg = ease(t, 6.5, 7.3);
  if (fg > 0) { rect(ctx, BX, BB - FH * fg, BW, FH * fg, C.muted, 0.85); }
  // labels: one number per moment
  text(ctx, CL('worst_start'), G.X(sTarget) + fw + 24, G.y0 + 30, 'label', { alpha: Math.min(ease(t, 1.4, 1.8), 1 - ease(t, 3.4, 3.7)) });
  const kp = d.path.indexOf(Math.max(...d.path));
  text(ctx, CL('worst_peak_rate'), P.X(kp) - 36, P.Y(d.path[kp]) - 8, 'number', { align: 'right', alpha: n >= kp ? Math.min(ease(t, 1.7 + 4.6 * kp / 120, 2.0 + 4.6 * kp / 120), 1 - ease(t, 6.5, 6.8)) : 0 });
  text(ctx, CL('fixed_int'), BX - 26, BB - FH / 2 + 20, 'label', { align: 'right', color: C.muted, alpha: ease(t, 7.4, 7.8) });
  text(ctx, CL('worst_diff'), BX - 26, BB - FH - EH / 2 + 34, 'number', { align: 'right', alpha: ease(t, 8.2, 8.6) });
  numWord(ctx, CL('fixed_rate'), 'fixed', P.x1, P.Y(FIXED) + 64, 'label', { align: 'right', alpha: 1 - ease(t, 1.5, 1.8) });
  badge(ctx, 1);
}
