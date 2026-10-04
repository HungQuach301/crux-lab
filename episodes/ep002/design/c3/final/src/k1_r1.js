// KEY-1 (S01.2-S01.3), base H2 (rate plane), redesigned after the C3 blind read ("a lone diamond did not read as a
// person weighing two offers"). Muted reading wanted: ONE person holds TWO offer cards; the left card's rate is a level
// line, the right card's starts lower (cushion bracket under a faint copy of the left level) and then moves up and down
// (one real replay of Leah's loan, DATA.k1). Then she weighs them: the cards see-saw and her head turns to each.
// Leah = ink + diamond (diamond cut-out on the figure's chest; diamond at the head of her variable path).
import { C, DATA, CL, numWord, badge, line, rect, diamond, roundRect, ease, mix, clamp, rateAt } from './engine.js';
export const duration = 8.0;
export const stripTimes = [0.55, 1.25, 2.5, 4.1, 5.75, 7.85];
const PATH = DATA.k1.path, FIX = 9.0, VAR0 = 7.5;
const CW = 660, CH = 460, CY = 196, LX = 140, RX = 1920 - 140 - CW;
const HX = 960, HY = 668, HR = 66;           // head
function card(ctx, x, y, a) {
  if (a <= 0.01) return;
  ctx.save(); ctx.globalAlpha = a;
  const f = 54; // folded corner
  ctx.beginPath(); ctx.moveTo(x + 22, y); ctx.lineTo(x + CW - f, y); ctx.lineTo(x + CW, y + f); ctx.lineTo(x + CW, y + CH - 22);
  ctx.arcTo(x + CW, y + CH, x + CW - 22, y + CH, 22); ctx.lineTo(x + 22, y + CH); ctx.arcTo(x, y + CH, x, y + CH - 22, 22);
  ctx.lineTo(x, y + 22); ctx.arcTo(x, y, x + 22, y, 22); ctx.closePath();
  ctx.fillStyle = C.bg; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = C.muted; ctx.lineJoin = 'round'; ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x + CW - f, y); ctx.lineTo(x + CW - f, y + f); ctx.lineTo(x + CW, y + f); ctx.stroke();
  ctx.restore();
}
const X0 = 56, X1 = CW - 56;
const Y = (y, r) => y + CH - 42 - (r - 6.5) * (270 / 6.5);
const MX = (x, k) => x + X0 + (X1 - X0) * k / (PATH.length - 1);
function person(ctx, a, dx, la, ra) {
  if (a <= 0.01) return;
  ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.ink; ctx.strokeStyle = C.ink;
  // arms first (behind the torso): shoulder -> hand at the card's inner bottom corner
  ctx.lineCap = 'round'; ctx.lineWidth = 34;
  for (const [sx, h] of [[858, la], [1062, ra]]) if (h) { ctx.beginPath(); ctx.moveTo(sx, 842); ctx.lineTo(h[0], h[1]); ctx.stroke(); ctx.beginPath(); ctx.arc(h[0], h[1], 26, 0, 7); ctx.fill(); }
  // torso (bust), head
  ctx.beginPath(); ctx.moveTo(812, 1080); ctx.lineTo(812, 880); ctx.bezierCurveTo(812, 790, 870, 752, 960, 752); ctx.bezierCurveTo(1050, 752, 1108, 790, 1108, 880); ctx.lineTo(1108, 1080); ctx.closePath(); ctx.fill();
  ctx.beginPath(); ctx.arc(HX + dx, HY, HR, 0, 7); ctx.fill();
  ctx.restore();
  // Leah's mark: a diamond cut out of the chest
  ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = C.bg; const cx = 960, cy = 900, r = 46;
  ctx.beginPath(); ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r * 0.78, cy); ctx.lineTo(cx, cy + r); ctx.lineTo(cx - r * 0.78, cy); ctx.closePath(); ctx.fill(); ctx.restore();
}
export function draw(ctx, t) {
  const fa = ease(t, 0, 0.45), e = ease(t, 0.6, 1.5);
  // weighing: see-saw, head turns to the raised card
  const w = clamp((t - 5.2) / 2.0), env = Math.sin(Math.PI * w), s = Math.sin(2 * Math.PI * w) * env;
  const tilt = 44 * s;
  const lx = mix(800, LX, e), rx = mix(1120 - CW + CW, RX, e) - 0, ly = CY + mix(300, 0, e) - tilt, ry = CY + mix(300, 0, e) + tilt;
  const lxx = mix(860 - CW, LX, e), rxx = mix(1060, RX, e);
  const ca = e;
  const lHand = e > 0.02 ? [lxx + CW - 18, ly + CH - 6] : null, rHand = e > 0.02 ? [rxx + 18, ry + CH - 6] : null;
  person(ctx, fa, -20 * s, lHand, rHand);
  card(ctx, lxx, ly, ca); card(ctx, rxx, ry, ca);
  // LEFT: fixed, a level line
  const pf = ease(t, 1.8, 2.8);
  if (pf > 0) line(ctx, [[lxx + X0, Y(ly, FIX)], [lxx + mix(X0, X1, pf), Y(ly, FIX)]], C.muted, 14, { cap: 'butt', alpha: ca });
  numWord(ctx, CL('fixed_rate'), 'fixed', lxx + 44, ly + 92, 'label', { alpha: ease(t, 1.6, 1.9) * ca });
  // RIGHT: variable, starts lower (cushion bracket under a faint copy of the 9% level), then moves up and down
  const ga = ease(t, 2.8, 3.1) * ca;
  line(ctx, [[rxx + X0, Y(ry, FIX)], [rxx + X1, Y(ry, FIX)]], C.muted, 4, { cap: 'butt', alpha: 0.5 * ga, dash: [16, 14] });
  rect(ctx, rxx + X0 - 22, Y(ry, FIX), 16, Y(ry, VAR0) - Y(ry, FIX), C.cushion, ease(t, 2.9, 3.2) * ca);
  const n = mix(0, PATH.length - 1, ease(t, 3.1, 5.2));
  const pts = []; for (let k = 0; k <= Math.floor(n); k++) pts.push([MX(rxx, k), Y(ry, PATH[k])]);
  pts.push([MX(rxx, n), Y(ry, rateAt(PATH, n))]);
  if (t > 3.0) line(ctx, pts.length > 1 ? pts : [[rxx + X0, Y(ry, VAR0)], [rxx + X0 + 1, Y(ry, VAR0)]], C.ink, 9, { alpha: ga });
  diamond(ctx, MX(rxx, n), Y(ry, rateAt(PATH, n)), 24, ga);
  numWord(ctx, CL('var_start'), 'variable', rxx + 44, ry + 92, 'label', { alpha: ease(t, 2.8, 3.1) * ca });
  badge(ctx, ease(t, 1.5, 1.8));
}
