// KEY-2 (S03.5-S03.8): the bracket between rail and bead is what is measured: big, small, none, reversed.
import { C, CL, text, numWord, badge, line, poly, rect, diamond, plane, ease, back, mix, clamp, FIXED } from './engine.js';
export const duration = 9.0;
export const stripTimes = [0.5, 2.0, 4.3, 5.8, 6.9, 8.6];
const P = plane(560, 1720, 200, 940, 4.6, 12.0, 24);
// variable start rate over time
const KEYS = [[0, 7.5], [3.0, 7.5], [3.9, 6.0], [4.7, 6.0], [5.5, 8.4], [6.0, 8.4], [6.6, 9.0], [7.2, 9.0], [8.0, 10.1], [9, 10.1]];
function vAt(t) { for (let i = 0; i < KEYS.length - 1; i++) { const [a, va] = KEYS[i], [b, vb] = KEYS[i + 1]; if (t <= b) return mix(va, vb, ease(t, a, b)); } return KEYS[KEYS.length - 1][1]; }
export function draw(ctx, t) {
  const v = vAt(t), yR = P.Y(FIXED), bx = P.X(0), by = P.Y(v);
  // ruler (what is being measured): ticks every half point
  const RX = 400, ra = ease(t, 0.6, 1.0);
  line(ctx, [[RX, P.Y(5)], [RX, P.Y(11)]], C.muted, 4, { alpha: ra, cap: 'butt' });
  for (let r = 5; r <= 11.001; r += 0.5) line(ctx, [[RX, P.Y(r)], [RX + (r % 1 ? 18 : 34), P.Y(r)]], C.muted, 4, { alpha: ra, cap: 'butt' });
  // first months held level: the slab that the gap builds (positive below the rail, warn above)
  const slabN = ease(t, 1.3, 2.3) * 9;
  if (Math.abs(v - FIXED) > 0.02) poly(ctx, [[bx, yR], [bx, by], [P.X(slabN), by], [P.X(slabN), yR]], v < FIXED ? C.positive : C.warn, v < FIXED ? 0.55 : 0.72);
  line(ctx, [[bx, by], [P.X(slabN), by]], C.accent, 8, { alpha: slabN > 0.05 ? 1 : 0 });
  // rail
  line(ctx, [[P.x0 - 80, yR], [P.x1, yR]], C.ink, 10, { cap: 'butt' });
  if (v > FIXED) line(ctx, [[bx, yR], [P.X(slabN), yR]], C.warn, 16, { cap: 'butt' });
  // bracket: snaps in at 0.8 s
  const s = clamp(back(t, 0.7, 1.15), 0, 1.3), BX = 486;
  if (t > 0.7) {
    const colr = v < FIXED - 0.02 ? C.positive : v > FIXED + 0.02 ? C.warn : C.ink;
    const yb = mix(yR, by, Math.min(1, s)), arm = 30 * s;
    if (Math.abs(v - FIXED) > 0.06) {
      line(ctx, [[BX + arm, yR], [BX, yR], [BX, yb], [BX + arm, yb]], colr, 10, { cap: 'butt' });
    } else {
      line(ctx, [[BX - 10, yR - 16], [BX + 30, yR - 16]], colr, 8, { cap: 'butt' }); line(ctx, [[BX - 10, yR + 16], [BX + 30, yR + 16]], colr, 8, { cap: 'butt' });
    }
  }
  diamond(ctx, bx, by, 38);
  numWord(ctx, CL('gap_start'), '', bx + 60, by + 120, 'number', { alpha: Math.min(ease(t, 1.2, 1.6), 1 - ease(t, 3.0, 3.3)) });
  numWord(ctx, CL('fixed_rate'), 'fixed', P.x1, yR - 34, 'label', { align: 'right' });
  badge(ctx, 1);
}
