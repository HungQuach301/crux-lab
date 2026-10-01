// KEY-4 fix round (gates/C3-K245-blind.md): v1 (three tracks + tanks) read as "three scenarios"; kept as k4_v1.js.
// Now ONE replay around the 9% line and ONE visible jar beside it, in sync month by month: while the rate is below
// 9% the jar fills (cushion stream in at the top); while above, it drains (warn stream out of the spout). Real replay
// of Leah's loan starting April 1976 (DATA.detail): a 2-month blip above 9% at months 21-22 barely dents the jar
// (~$1 of ~$1,036), then the long climb from month 25 drains it dry by month 40; from then on a costlier (#C72323,
// hatched) block appears under the jar and grows (own scale, see README).
import { C, DATA, CL, numWord, badge, line, rect, negArea, plane, replay, roundRect, ease, mix, clamp, FIXED } from './engine.js';
export const duration = 10.0;
const D = DATA.detail['1976-04'];
const SEG = [[0.8, 0], [3.6, 30], [6.0, 60], [8.8, 119]];
function nAt(t) { if (t <= SEG[0][0]) return 0; for (let i = 0; i < SEG.length - 1; i++) { const [a, ma] = SEG[i], [b, mb] = SEG[i + 1]; if (t <= b) return mix(ma, mb, (t - a) / (b - a)); } return 119; }
function tOf(m) { for (let i = 0; i < SEG.length - 1; i++) { const [a, ma] = SEG[i], [b, mb] = SEG[i + 1]; if (m <= mb) return a + (b - a) * (m - ma) / (mb - ma); } return 8.8; }
export const stripTimes = [tOf(12), tOf(21.6), tOf(33), tOf(44), tOf(85), 9.8].map((x) => +x.toFixed(2));
const P = plane(400, 1340, 300, 920, 5.0, 19.5, 120);
const J = { x: 1500, w: 210, top: 330, bot: 760 }, KJ = 380 / 1046, KB = 150 / 7577;
export function draw(ctx, t) {
  const n = nAt(t), k = Math.min(119, Math.floor(n)), v = n <= 0 ? 0 : D.cushion[k];
  const above = n > 0 && D.path[k] > FIXED, below = n > 0 && n < 119 && D.path[k] <= FIXED;
  replay(ctx, P, D.path, n, { beadR: 26, lw: 7, railW: 12 });
  numWord(ctx, CL('fixed_rate'), 'fixed', P.x0 - 30, P.Y(FIXED) + 20, 'label', { align: 'right' });
  // the jar: vessel + cushion liquid (in $; one scale)
  const lv = Math.max(0, v) * KJ;
  ctx.save(); roundRect(ctx, J.x, J.top, J.w, J.bot - J.top, 22); ctx.clip();
  rect(ctx, J.x, J.bot - lv, J.w, lv, C.cushion, 1); ctx.restore();
  // inflow (below 9%): a cushion stream into the jar mouth
  // inflow (below 9%): each month's saving flows from the gap under the rail into the jar (one curved stream)
  if (below && t < 8.8) {
    const bx = P.X(n), gy = (P.Y(D.path[k]) + P.Y(FIXED)) / 2, mx = J.x + J.w / 2, pts = [];
    for (let u = 0; u <= 1.0001; u += 0.04) { const cx = (bx + mx) / 2, cy = 170; pts.push([(1 - u) * (1 - u) * bx + 2 * u * (1 - u) * cx + u * u * mx, (1 - u) * (1 - u) * gy + 2 * u * (1 - u) * cy + u * u * (J.top - 10)]); }
    line(ctx, pts, C.cushion, 10, { alpha: 0.9 });
    line(ctx, [[mx, J.top - 10], [mx, J.bot - lv]], C.cushion, 10, { cap: 'butt', alpha: 0.9 });
  }
  // outflow (above 9% while cushion remains): spout at the bottom right, warn stream falling out
  line(ctx, [[J.x + J.w - 4, J.bot - 30], [J.x + J.w + 46, J.bot - 30], [J.x + J.w + 46, J.bot - 6]], C.muted, 10, { cap: 'butt' });
  if (above && v > 0 && t < 8.8) {
    line(ctx, [[J.x + J.w + 46, J.bot - 6], [J.x + J.w + 46, J.bot + 80]], C.warn, 12, { cap: 'butt' });
    line(ctx, [[J.x + 4, J.bot - lv], [J.x + J.w - 4, J.bot - lv]], C.warn, 10, { cap: 'butt' });
  }
  ctx.save(); ctx.strokeStyle = C.muted; ctx.lineWidth = 6; roundRect(ctx, J.x, J.top, J.w, J.bot - J.top, 22); ctx.stroke(); ctx.restore();
  // jar empty -> costlier block appears under it and grows with the extra interest
  if (v < 0) negArea(ctx, J.x, J.bot + 110, J.w, -v * KB, 1, 22);
  badge(ctx, 1);
}
