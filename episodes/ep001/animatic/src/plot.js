// Break-even plot (signed SF4 grammar), shared by S11-S13: x = months after refinancing, y = dollars.
// Fees = a flat line. "Division" = savings only (straight line). Green curve = savings minus what she still owes
// (model/refi.py via data.js; never printed). A small rate-cut ruler (top right) shows which cut is being tried.
import { C, W, H, DATA, CL, text, line, rect, dot, mark, ease, easeOut, mix, withObj } from './engine.js';

export const G = { X0: 200, X1: 1500, YB: 880, YT: 420, VMAX: 6000 };
export function axes(ctx, xmax, a = 1) {
  withObj({ role: 'axis', chart: 'breakeven' }, () => line(ctx, [[G.X0, G.YB], [G.X1, G.YB]], C.grid, 3, { alpha: a }));
  text(ctx, 'months after refinancing →', G.X1, G.YB + 64, 'note', { color: C.muted, align: 'right', alpha: a });
  const yF = yOf(DATA.median.cost);
  line(ctx, [[G.X0, yF], [G.X1, yF]], C.muted, 6, { alpha: a });
  text(ctx, 'loan costs ' + CL('cost_median'), G.X0 + 10, yF - 20, 'label', { alpha: a });
  text(ctx, 'dollars of the day', G.X0 + 10, yF - 76, 'note', { color: C.muted, alpha: a }); // C5 S09: basis next to the $
  return yF;
}
export const yOf = (v) => G.YB - (v / G.VMAX) * (G.YB - G.YT);
export const xOfM = (m, xmax) => G.X0 + (m / xmax) * (G.X1 - G.X0);
// draw a net curve up to month `upto` (fractional), clipped to the plot; returns head point
export function curve(ctx, net, upto, xmax, color = C.positive, lw = 7, a = 1) {
  const pts = [];
  for (let m = 0; m <= Math.min(Math.floor(upto), net.length - 1, Math.floor(xmax)); m++) {
    if (net[m] < 0 && m > 0) { const f = net[m - 1] / (net[m - 1] - net[m]); pts.push([xOfM(m - 1 + f, xmax), G.YB]); break; }
    if (net[m] > G.VMAX * 1.08) break;
    pts.push([xOfM(m, xmax), yOf(net[m])]);
  }
  if (pts.length > 1) withObj({ role: 'series', chart: 'breakeven' }, () => line(ctx, pts, color, lw, { alpha: a }));
  const h = pts[pts.length - 1]; if (h) dot(ctx, h[0], h[1], 10, color, a);
  return h;
}
// small rate-cut ruler, top right: 0 .. 1.25 points; the 1-point line dashed
export const RU = { x0: 1060, x1: 1760, y: 260, max: 1.25 };
export const rx = (c) => RU.x0 + (c / RU.max) * (RU.x1 - RU.x0);
export function ruler(ctx, a = 1) {
  withObj({ role: 'axis', chart: 'cut-ruler' }, () => line(ctx, [[RU.x0, RU.y], [RU.x1, RU.y]], C.grid, 5, { alpha: a }));
  line(ctx, [[rx(1), RU.y - 44], [rx(1), RU.y + 24]], C.ink, 3, { dash: [10, 8], alpha: a });
  text(ctx, CL('s10') + '-point line', rx(1), RU.y - 56, 'note', { align: 'center', alpha: a });
  text(ctx, 'rate cut', RU.x0 - 20, RU.y + 14, 'note', { align: 'right', color: C.muted, alpha: a });
}
