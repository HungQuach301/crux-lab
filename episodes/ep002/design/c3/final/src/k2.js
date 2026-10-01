// KEY-2 fix round (gates/C3-K245-blind.md): v1 (one bead sliding round a rail) read as "one balance over time"; kept
// as k2_v1.js. Now on the KEY-1 r2 motif that passed: one person, two cards at the same height, the 9% line unbroken
// across both. Only the variable card's START POINT changes, and it JUMPS between discrete offers: well below (3
// points) -> just below (1.5, Leah's) -> on the line (0) -> above (-1). Each jump flips the variable card like a new
// offer. Gap filled cushion when the start is below the line, warn when above. No path after the start point. Ends on
// the "above" state.
import { C, CL, text, numWord, badge, line, rect, diamond, ease, clamp } from './engine.js';
export const duration = 8.0;
export const stripTimes = [1.2, 1.92, 2.9, 4.5, 6.1, 7.85];
const CW = 680, CH = 470, CY = 196, LX = 130, RX = 1920 - 130 - CW;
const YR = CY + 236, PP = 64;                        // the 9% line; px per point (one scale)
const GX0 = RX + 70, GX1 = RX + 330;                 // start block on the variable card
const STATES = [[0.6, 3], [2.0, 1.5], [3.6, 0], [5.2, -1]]; // [jump time, head start in points]
function card(ctx, x, y, sx = 1) {
  ctx.save(); const cx = x + CW / 2; ctx.translate(cx, 0); ctx.scale(sx, 1); ctx.translate(-cx, 0); const f = 54;
  ctx.beginPath(); ctx.moveTo(x + 22, y); ctx.lineTo(x + CW - f, y); ctx.lineTo(x + CW, y + f); ctx.lineTo(x + CW, y + CH - 22);
  ctx.arcTo(x + CW, y + CH, x + CW - 22, y + CH, 22); ctx.lineTo(x + 22, y + CH); ctx.arcTo(x, y + CH, x, y + CH - 22, 22);
  ctx.lineTo(x, y + 22); ctx.arcTo(x, y, x + 22, y, 22); ctx.closePath();
  ctx.fillStyle = C.bg; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = C.muted; ctx.lineJoin = 'round'; ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x + CW - f, y); ctx.lineTo(x + CW - f, y + f); ctx.lineTo(x + CW, y + f); ctx.stroke();
  ctx.restore();
}
function person(ctx) {
  ctx.save(); ctx.fillStyle = C.ink; ctx.strokeStyle = C.ink; ctx.lineCap = 'round'; ctx.lineWidth = 34;
  for (const [sx, h] of [[858, [LX + CW - 18, CY + CH - 6]], [1062, [RX + 18, CY + CH - 6]]]) { ctx.beginPath(); ctx.moveTo(sx, 850); ctx.lineTo(h[0], h[1]); ctx.stroke(); ctx.beginPath(); ctx.arc(h[0], h[1], 26, 0, 7); ctx.fill(); }
  ctx.beginPath(); ctx.moveTo(812, 1080); ctx.lineTo(812, 900); ctx.bezierCurveTo(812, 810, 870, 772, 960, 772); ctx.bezierCurveTo(1050, 772, 1108, 810, 1108, 900); ctx.lineTo(1108, 1080); ctx.closePath(); ctx.fill();
  ctx.beginPath(); ctx.arc(974, 690, 66, 0, 7); ctx.fill();   // head turned toward the variable card
  ctx.fillStyle = C.bg; const cx = 960, cy = 920, r = 46;
  ctx.beginPath(); ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r * 0.78, cy); ctx.lineTo(cx, cy + r); ctx.lineTo(cx - r * 0.78, cy); ctx.closePath(); ctx.fill();
  ctx.restore();
}
export function draw(ctx, t) {
  const a = ease(t, 0, 0.4);
  // current offer and flip (squash to 0 and back over 0.36 s around each jump)
  let si = 0; for (let i = 0; i < STATES.length; i++) if (t >= STATES[i][0]) si = i;
  let sx = 1, shown = t >= STATES[0][0] ? si : -1;
  for (let i = 1; i < STATES.length; i++) { const tj = STATES[i][0], d = t - tj; if (d > -0.18 && d < 0.18) { sx = Math.max(0.02, Math.abs(d) / 0.18); shown = d < 0 ? i - 1 : i; } }
  ctx.save(); ctx.globalAlpha = a; person(ctx); card(ctx, LX, CY); card(ctx, RX, CY, sx); ctx.restore();
  // the 9% line, unbroken across both cards
  line(ctx, [[LX + 60, YR], [RX + CW - 50, YR]], C.muted, 14, { cap: 'butt', alpha: a });
  numWord(ctx, CL('fixed_rate'), 'fixed', LX + 44, CY + 92, 'label', { alpha: a });
  if (shown >= 0) {
    const g = STATES[shown][1], ys = YR + g * PP, cx = RX + CW / 2;
    const X = (x) => cx + (x - cx) * sx, pa = ease(t, STATES[0][0], STATES[0][0] + 0.2);
    if (Math.abs(g) > 0.01) rect(ctx, X(GX0), Math.min(YR, ys) + (g > 0 ? 7 : 0), (GX1 - GX0) * sx, Math.abs(ys - YR) - 7, g > 0 ? C.cushion : C.warn, pa);
    line(ctx, [[X(GX0), ys], [X(GX1), ys]], C.ink, 9, { cap: 'butt', alpha: pa });
    if (sx > 0.5) diamond(ctx, X(GX0), ys, 28, pa);
    text(ctx, 'variable', RX + 44, CY + 92, 'label', { color: C.muted, alpha: pa * (sx > 0.98 ? 1 : 0) });
    if (shown === 1 && sx > 0.98) text(ctx, CL('gap_start'), GX1 + 30, (YR + ys) / 2 + 20, 'label', { alpha: 1 });
  }
  badge(ctx, a);
}
