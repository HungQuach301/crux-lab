// KEY-7 round 3 = owner option (A), intent pre-registered in episodes/ep002/gates/C3-K7-intent-r3.md.
// Three STATIC panels side by side, appearing one after another (left -> right); nothing grows or fills: each panel
// pops in complete (0.25 s fade) and stays. Top of each panel: the KEY-1 r2 motif - the 9% fixed line (ink-muted) and
// the variable starting point (ink line + Leah's diamond) BELOW it by the head start, gap filled cushion; one scale for
// all three panels (0 / 1.5 / 3 points). Under each panel: KEY-3's two token bins (left 1954-1980, right from 1981),
// 20 tokens per bin; red (costlier #C72323) tokens = share costlier in that half, rounded to 20 tokens (README).
// Round 2 is kept as k7_r2.js.
import { C, DATA, CL, USED, text, badge, line, rect, srect, diamond, roundRect, ease } from './engine.js';
export const duration = 9.0;
export const stripTimes = [1.2, 2.6, 3.6, 5.0, 6.0, 8.8];
const NT = 20, COLS = 5, TS = 36, TG = 7;
// [gap, gap-label claim, early claim, late claim, appear time]
const PANELS = [[0, 'gap00_early', 'gap00_early', 'gap00_late', 0.6], [1.5, 'gap_start', 'gap15_early', 'gap15_late', 3.0], [3, 'gap30_early', 'gap30_early', 'gap30_late', 5.4]];
const PW = 560, PX = [75, 680, 1285], RAIL = 268, PP = 70;
export const RED = PANELS.map(([g]) => ['early', 'late'].map((h) => Math.round(NT * DATA.gap[String(g)][h] / 100)));
function panel(ctx, x, g, labClaim, a) {
  if (a <= 0.01) return;
  ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = C.grid; ctx.lineWidth = 4; roundRect(ctx, x, 150, PW, 830, 22); ctx.stroke(); ctx.restore();
  // motif: 9% line, variable start below it by g, cushion between
  const x0 = x + 60, x1 = x + PW - 50, yv = RAIL + g * PP;
  if (g > 0) rect(ctx, x0, RAIL, x1 - x0, yv - RAIL, C.cushion, a);
  line(ctx, [[x + 30, RAIL], [x + PW - 30, RAIL]], C.muted, 14, { cap: 'butt', alpha: a });
  line(ctx, [[x0, yv], [x1, yv]], C.ink, 9, { cap: 'butt', alpha: a });
  diamond(ctx, x0, yv, 28, a);
  // gap label (claim: the tested head start of this panel)
  USED.add(labClaim);
  text(ctx, g === 1.5 ? CL('gap_start') : `${g} points`, x + PW - 40, 222, 'label', { align: 'right', alpha: a });
}
function bin(ctx, x, y, nRed, a) {
  const w = COLS * TS + (COLS - 1) * TG, rows = NT / COLS, h = rows * TS + (rows - 1) * TG;
  ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = C.muted; ctx.lineWidth = 4; roundRect(ctx, x - 14, y - 14, w + 28, h + 28, 14); ctx.stroke(); ctx.restore();
  for (let k = 0; k < NT; k++) { // red tokens settle at the bottom, filled left to right
    const r = rows - 1 - Math.floor(k / COLS), c = k % COLS;
    ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = k < nRed ? C.costlier : C.grid; roundRect(ctx, x + c * (TS + TG), y + r * (TS + TG), TS, TS, 7); ctx.fill(); ctx.restore();
  }
  return w;
}
export function draw(ctx, t) {
  PANELS.forEach(([g, labClaim, ce, cl, t0], i) => {
    const a = ease(t, t0, t0 + 0.25), x = PX[i];
    panel(ctx, x, g, labClaim, a);
    if (a <= 0.01) return;
    USED.add(ce); USED.add(cl); USED.add('n_early'); USED.add('n_late');
    const by = 610, bw = COLS * TS + (COLS - 1) * TG, bxL = x + 32, bxR = x + PW - 32 - bw;
    bin(ctx, bxL, by, RED[i][0], a); bin(ctx, bxR, by, RED[i][1], a);
    text(ctx, '1954–1980', bxL + bw / 2, 920, 'note', { align: 'center', color: C.muted, alpha: a });
    text(ctx, 'from 1981', bxR + bw / 2, 920, 'note', { align: 'center', color: C.muted, alpha: a });
  });
  badge(ctx, 1);
}
