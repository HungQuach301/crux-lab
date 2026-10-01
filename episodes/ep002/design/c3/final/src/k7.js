// KEY-7 round 2 (S09.2-S10.3). Round-1 blind read: red shrinking read the right way (3/3) but credited to TIME
// ("debt paid down"); halves differing 1/3. Round 2 (coordinator brief): no cell grid, no wedge, no T-bill terrain.
// TOP = the knob, large: two horizontal bars, the fixed rate (ink-muted) and where the variable rate starts (ink, Leah's
// diamond at its end); the cushion-filled gap between them widens stop by stop 0 -> 1 -> 1.5 -> 2 -> 2.5 -> 3 and stays
// at 3 (no sweep back). BELOW = the result: TWO LARGE COLUMNS side by side, left = starts before 1981, right = starts
// from 1981; the red (costlier, hatched) part of each shrinks in lockstep with the gap. Right reaches 0 at 2 points;
// left still holds red at 3 points (final frames).
import { C, DATA, CL, USED, text, numWord, badge, line, rect, srect, negArea, diamond, ease, mix, clamp, inout } from './engine.js';
export const duration = 10.0;
export const stripTimes = [0.6, 2.4, 3.9, 5.5, 6.7, 9.8];
const GS = [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3];
const KEYS = [[0, 0], [1.0, 0], [2.0, 1], [2.8, 1], [3.4, 1.5], [4.4, 1.5], [5.0, 2], [5.9, 2], [6.4, 2.5], [7.0, 2.5], [7.6, 3], [10, 3]];
function gAt(t) { for (let i = 0; i < KEYS.length - 1; i++) { const [a, va] = KEYS[i], [b, vb] = KEYS[i + 1]; if (t <= b) return mix(va, vb, ease(t, a, b)); } return 3; }
const share = (g, half) => { const i = Math.max(0, Math.min(GS.length - 2, Math.floor((g + 1) / 0.5 + 1e-9))), f = clamp((g - GS[i]) / 0.5);
  return mix(DATA.gap[String(GS[i])][half], DATA.gap[String(GS[i + 1])][half], f); };
// knob
const KX0 = 760, KX1 = 1400, FY = 132, BHt = 24, PP = 56;
// columns
const COLS = [['early', 690, 'n_early', 'before 1981'], ['late', 1130, 'n_late', 'from 1981']];
const CWd = 340, CT = 430, CB = 950, CHt = CB - CT;
export function draw(ctx, t) {
  const g = gAt(t), a = ease(t, 0, 0.4);
  // --- the knob: fixed bar, variable-start bar, the gap between them filled cushion
  const vy = FY + BHt + g * PP;
  rect(ctx, KX0, FY + BHt, KX1 - KX0, vy - FY - BHt, C.cushion, a);
  rect(ctx, KX0, FY, KX1 - KX0, BHt, C.muted, a);
  rect(ctx, KX0, vy, KX1 - KX0, BHt, C.ink, a);
  diamond(ctx, KX1 + 34, vy + BHt / 2, 26, a);
  numWord(ctx, CL('fixed_rate'), 'fixed', KX0 - 30, FY + BHt / 2 + 20, 'label', { align: 'right', alpha: a });
  text(ctx, 'variable', KX0 - 30, vy + BHt / 2 + 20, 'label', { align: 'right', color: C.muted, alpha: a * (g > 0.7 ? 1 : ease(g, 0.4, 0.7)) });
  text(ctx, CL('gap_start'), KX1 + 84, FY + BHt + 1.5 * PP / 2 + 20, 'label', { alpha: inout(t, 3.4, 3.7, 4.3, 4.6) });
  // --- the two result columns (outline = 100% of that half's start months; red hatched = share costlier)
  for (const [half, x, cid, lab] of COLS) {
    const s = share(g, half), h = CHt * s / 100, clear = s < 0.05;
    srect(ctx, x, CT, CWd, CHt, clear ? C.ink : C.grid, clear ? 6 : 4, a);
    negArea(ctx, x + 6, CB - h, CWd - 12, h - (h > 6 ? 0 : 0), a, 26);
    line(ctx, [[x - 20, CB], [x + CWd + 20, CB]], C.muted, 6, { cap: 'butt', alpha: a });
    USED.add(cid); text(ctx, lab, x + CWd / 2, CB + 74, 'label', { align: 'center', color: C.muted, alpha: a });
  }
  text(ctx, CL('gap20_late'), 1130 + CWd / 2, CT + CHt / 2, 'number', { align: 'center', alpha: inout(t, 5.0, 5.3, 6.1, 6.3) });
  text(ctx, CL('gap30_early'), 690 + CWd / 2, CB - CHt * 0.105 - 54, 'number', { align: 'center', alpha: ease(t, 7.7, 8.0) });
  badge(ctx, a);
}
