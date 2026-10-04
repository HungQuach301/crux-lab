// KEY-3 (S05.2-S05.4): amber on the rail in most replays (row A fills amber), yet only a few red cells in row B,
// far more under the climbing half; then each bin sorts into a share bar. Amber and red never share an object.
import { C, DATA, CL, text, numWord, badge, line, rect, srect, negArea, diamond, plane, replay, ridgeGeom, drawRidge,
  replayPath, startRidgeIdx, STARTS, SPLIT_J, binGeom, ease, easeOut, mix, clamp, FIXED } from './engine.js';
export const duration = 10.0;
export const stripTimes = [0.8, 2.6, 4.6, 6.2, 8.3, 9.8];
const P = plane(560, 1500, 140, 470, 3.0, 21.0, 120);
const G0 = ridgeGeom(200, 1720, 560, 790, 16.5);
const B = binGeom(G0);
const NJ = STARTS.length;
const ABOVE = DATA.above, COST = DATA.gap['1.5'].costlier;
const WORST = STARTS.indexOf(DATA.claims.worst_start === 'April 1977' ? '1977-04' : '');
function jAt(t) { const u = clamp((t - 0.3) / 5.2); return Math.min(NJ - 1, Math.floor((NJ - 1) * Math.pow(u, 1.5))); }
// sorted position (inside its own bin) of cell i in a row with flags f
function sortedX(f, i) {
  const inL = i < SPLIT_J, lo = inL ? 0 : SPLIT_J, hi = inL ? SPLIT_J : NJ;
  let rank = 0; const mine = f[i] === '1';
  for (let k = lo; k < hi; k++) { if (k === i) continue; const fk = f[k] === '1'; if (mine ? (fk && k < i) : (fk || k < i)) rank++; }
  return B.xs[lo] + rank * B.cw;
}
const SA = [], SB = [];
for (let i = 0; i < NJ; i++) { SA.push(sortedX(ABOVE, i)); SB.push(sortedX(COST, i)); }
export function draw(ctx, t) {
  const j = jAt(t);
  // after the sweep the bins move up and grow so the two shares can be compared
  const e = ease(t, 6.3, 7.3), rowH = 42 + 66 * e, ra0 = 826 - 330 * e;
  const RA = [ra0, ra0 + rowH], RB = [ra0 + rowH + 32, ra0 + 2 * rowH + 32];
  const G = ridgeGeom(200, 1720, 560 - 330 * e, 790 - 330 * e, 16.5);
  drawRidge(ctx, G, 1, 1);
  const fw = G.X(120) - G.X(0), fx = G.X(startRidgeIdx(j));
  const sweep = t < 5.9 ? 1 : 1 - ease(t, 5.9, 6.3);
  srect(ctx, fx, G.y0 - 20, fw, G.y1 - G.y0 + 20, C.ink, 5, sweep);
  // bins (two rows each)
  for (const [x0, x1] of [B.L, B.R]) for (const [y0, y1] of [RA, RB]) srect(ctx, x0 - 4, y0 - 4, x1 - x0 + 8, y1 - y0 + 8, C.grid, 4);
  // cells: row A amber if the rate went above 9% at some month; row B red if costlier in total (grey otherwise)
  const so = ease(t, 6.3, 7.4);
  for (let i = 0; i <= j; i++) {
    const xa = mix(B.xs[i], SA[i], so), xb = mix(B.xs[i], SB[i], i === WORST ? 0 : so), w = Math.max(B.cw, 2.2);
    rect(ctx, xa, RA[0], w, RA[1] - RA[0], ABOVE[i] === '1' ? C.warn : C.muted, ABOVE[i] === '1' ? 1 : 0.55);
    rect(ctx, xb, RB[0], w, RB[1] - RB[0], COST[i] === '1' ? C.negative : C.muted, COST[i] === '1' ? 1 : 0.55);
  }
  // once sorted, each bin's red cells read as one costlier block (hatched: second channel vs amber/green)
  if (so >= 1) for (const [lo, hi] of [[0, SPLIT_J], [SPLIT_J, NJ]]) {
    let nr = 0; for (let i = lo; i < hi; i++) if (COST[i] === '1' && i !== WORST) nr++;
    negArea(ctx, B.xs[lo], RB[0], nr * B.cw, RB[1] - RB[0], 1, 18);
  }
  // the worst start: a dark token that stays in place in the left bin
  if (j >= WORST) { const x = B.xs[WORST]; srect(ctx, x - 9, RB[0] - 9, 20, RB[1] - RB[0] + 18, C.ink, 4); }
  // plane: current replay, rail glows amber where the bead is above 9%
  if (sweep > 0) replay(ctx, P, replayPath(startRidgeIdx(j)), 119, { alpha: sweep, beadR: 28 });
  else { line(ctx, [[P.x0, P.Y(FIXED)], [P.x1, P.Y(FIXED)]], C.ink, 10, { cap: 'butt', alpha: 1 - ease(t, 6.0, 6.4) }); }
  // one number at a time (ink), each next to the row / bin it belongs to
  const NX = 1556;
  text(ctx, CL('share_rate_above_fixed'), NX, RA[1] + 4, 'number', { alpha: Math.min(ease(t, 2.4, 2.8), 1 - ease(t, 4.6, 4.9)) });
  text(ctx, CL('share_all'), NX, RB[1] + 22, 'number', { alpha: Math.min(ease(t, 5.0, 5.4), 1 - ease(t, 7.2, 7.5)) });
  text(ctx, CL('share_early'), (B.L[0] + B.L[1]) / 2, RB[1] + 104, 'number', { align: 'center', alpha: Math.min(ease(t, 7.5, 7.9), 1 - ease(t, 8.7, 9.0)) });
  text(ctx, CL('share_late'), (B.R[0] + B.R[1]) / 2, RB[1] + 104, 'number', { align: 'center', alpha: ease(t, 9.0, 9.3), color: C.ink });
  badge(ctx, 1);
}
