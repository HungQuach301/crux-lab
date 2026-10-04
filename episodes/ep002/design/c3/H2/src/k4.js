// KEY-4 (S06.1-S06.5): the cushion. Three replays at once, one dollar scale: each month below the rail adds green
// area to the tank (fastest at the start, when the debt wedge is tallest); each month above the rail uses it up (the
// tank edge glows amber). Falling rates: tank brims. A short blip: a dent. A long climb: the tank empties and goes red.
import { C, DATA, CL, text, badge, line, poly, rect, srect, negArea, diamond, plane, replay, tank, slabs, ease, mix, clamp, lin, FIXED } from './engine.js';
export const duration = 10.0;
export const stripTimes = [0.6, 2.0, 3.6, 5.4, 7.4, 9.6];
const ROWS = ['1981-08', '1986-03', '1976-04'].map((k, i) => {
  const y0 = 196 + i * 290;
  return { d: DATA.detail[k], P: plane(250, 1420, y0 - 20, y0 + 196, 3.0, 19.6, 120), wedge: [y0 + 208, y0 + 250], y0 };
});
const KP = 150 / 15500; // tank px per $ (one scale for all three tanks)
const nAt = (t) => 120 * clamp((t - 0.8) / 7.6);
export function draw(ctx, t) {
  const n = nAt(t);
  ROWS.forEach((R, i) => {
    const { d, P } = R;
    const T = { x: 1560, w: 150, top: R.y0 - 6, yZero: R.y0 + 156, bottom: R.y0 + 250, k: KP };
    // debt wedge: Leah's balance month by month (tallest at the start)
    const wy = R.wedge[1], wh = R.wedge[1] - R.wedge[0];
    const pts = d.bal.map((b, k) => [P.X(k), wy - wh * b / 50000]);
    poly(ctx, [[P.x0, wy], ...pts, [P.X(120), wy]], C.muted, 0.32);
    // marker of "now" on the wedge
    if (n > 0 && n < 120) line(ctx, [[P.X(n), R.wedge[0] - 4], [P.X(n), wy]], C.muted, 3, { alpha: 0.8 });
    replay(ctx, P, d.path, Math.min(119, n), { beadR: 22, lw: 6, railW: 8 });
    const k = Math.min(119, Math.floor(n)), v = n < 0.01 ? 0 : d.cushion[k];
    tank(ctx, T, v);
    // while the bead is above the rail the cushion is being used up: the tank's moving edge glows amber
    if (n > 0.5 && n < 119.5 && d.path[k] > FIXED && v > 0) {
      const ye = T.yZero - v * T.k;
      line(ctx, [[T.x - 8, ye], [T.x + T.w + 8, ye]], C.warn, 12, { cap: 'butt' });
    }
  });
  badge(ctx, 1);
  text(ctx, 'still owed', 250, 196 + 250 + 62, 'note', { color: C.muted, alpha: Math.min(ease(t, 0.4, 0.8), 1 - ease(t, 3.0, 3.4)) });
}
