// KEY-1 round 2 (S01.2-S01.3), base H2. Round-1 blind read: 3/3 saw "one person, two options, one flat, one moving",
// 0/3 saw that the variable STARTS LOWER (cards at different heights, no shared scale). Round 2: both cards sit at the
// same height and NEVER move; ONE fixed-level line (the 9% rail) runs continuously across BOTH cards; on the right card
// the variable line starts clearly BELOW that line, with a filled cushion wedge (E2 alias of `positive`) between the
// rail and the line, and only then climbs, crosses the rail and moves up and down (real replay of Leah's loan, start
// 1962-12, DATA.k1). The person only turns her head (left, right). Leah = ink + diamond.
import { C, DATA, CL, numWord, badge, line, diamond, ease, mix, clamp, rateAt } from './engine.js';
export const duration = 8.0;
export const stripTimes = [0.7, 1.6, 2.5, 3.5, 4.7, 7.85];
const PATH = DATA.k1.path, FIX = 9.0, VAR0 = 7.5, CROSS = PATH.findIndex((r) => r > FIX);
const CW = 680, CH = 470, CY = 190, LX = 130, RX = 1920 - 130 - CW;
const HX = 960, HY = 690, HR = 66;
const PX0 = RX + 60, PX1 = RX + CW - 50;                 // variable path span inside the right card
const Y = (r) => CY + CH - 40 - (r - 6.8) * (300 / 6);    // ONE vertical scale for both cards
const MX = (k) => PX0 + (PX1 - PX0) * k / (PATH.length - 1);
function card(ctx, x, y) {
  ctx.save(); const f = 54;
  ctx.beginPath(); ctx.moveTo(x + 22, y); ctx.lineTo(x + CW - f, y); ctx.lineTo(x + CW, y + f); ctx.lineTo(x + CW, y + CH - 22);
  ctx.arcTo(x + CW, y + CH, x + CW - 22, y + CH, 22); ctx.lineTo(x + 22, y + CH); ctx.arcTo(x, y + CH, x, y + CH - 22, 22);
  ctx.lineTo(x, y + 22); ctx.arcTo(x, y, x + 22, y, 22); ctx.closePath();
  ctx.fillStyle = C.bg; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = C.muted; ctx.lineJoin = 'round'; ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x + CW - f, y); ctx.lineTo(x + CW - f, y + f); ctx.lineTo(x + CW, y + f); ctx.stroke();
  ctx.restore();
}
function person(ctx, dx) {
  ctx.save(); ctx.fillStyle = C.ink; ctx.strokeStyle = C.ink; ctx.lineCap = 'round'; ctx.lineWidth = 34;
  for (const [sx, h] of [[858, [LX + CW - 18, CY + CH - 6]], [1062, [RX + 18, CY + CH - 6]]]) { ctx.beginPath(); ctx.moveTo(sx, 850); ctx.lineTo(h[0], h[1]); ctx.stroke(); ctx.beginPath(); ctx.arc(h[0], h[1], 26, 0, 7); ctx.fill(); }
  ctx.beginPath(); ctx.moveTo(812, 1080); ctx.lineTo(812, 900); ctx.bezierCurveTo(812, 810, 870, 772, 960, 772); ctx.bezierCurveTo(1050, 772, 1108, 810, 1108, 900); ctx.lineTo(1108, 1080); ctx.closePath(); ctx.fill();
  ctx.beginPath(); ctx.arc(HX + dx, HY, HR, 0, 7); ctx.fill();
  ctx.fillStyle = C.bg; const cx = 960, cy = 920, r = 46;
  ctx.beginPath(); ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r * 0.78, cy); ctx.lineTo(cx, cy + r); ctx.lineTo(cx - r * 0.78, cy); ctx.closePath(); ctx.fill();
  ctx.restore();
}
export function draw(ctx, t) {
  const a = ease(t, 0, 0.4);
  ctx.save(); ctx.globalAlpha = a;
  // head turns: to the left card, then to the right card (cards never move)
  const w = clamp((t - 5.7) / 1.6), dx = -22 * Math.sin(2 * Math.PI * w) * Math.sin(Math.PI * w);
  person(ctx, dx); card(ctx, LX, CY); card(ctx, RX, CY);
  ctx.restore();
  // ONE fixed level, continuous across both cards
  const yF = Y(FIX), xA = LX + 60, xB = PX1;
  const pf = ease(t, 0.6, 1.7);
  if (pf > 0) line(ctx, [[xA, yF], [mix(xA, xB, pf), yF]], C.muted, 14, { cap: 'butt' });
  // variable: starts BELOW the level; cushion wedge between level and line until it first crosses
  const n = mix(0, PATH.length - 1, ease(t, 2.3, 5.4)), va = ease(t, 1.9, 2.2);
  if (va > 0) {
    const m = Math.min(n, CROSS), pts = [];
    for (let k = 0; k <= Math.floor(m); k++) pts.push([MX(k), Y(PATH[k])]);
    pts.push([MX(m), Y(Math.min(FIX, rateAt(PATH, m)))]);
    ctx.save(); ctx.globalAlpha = va; ctx.fillStyle = C.cushion; ctx.beginPath(); ctx.moveTo(MX(0), yF - 7 + 7);
    pts.forEach((p) => ctx.lineTo(p[0], p[1])); ctx.lineTo(pts[pts.length - 1][0], yF); ctx.closePath(); ctx.fill(); ctx.restore();
    // keep the start gap visible from the first moment: a cushion bar at the start
    line(ctx, [[MX(0), yF + 7], [MX(0), Y(VAR0)]], C.cushion, 14, { alpha: va, cap: 'butt' });
    const vp = []; for (let k = 0; k <= Math.floor(n); k++) vp.push([MX(k), Y(PATH[k])]); vp.push([MX(n), Y(rateAt(PATH, n))]);
    if (vp.length > 1) line(ctx, vp, C.ink, 9, { alpha: va });
    diamond(ctx, MX(n), Y(rateAt(PATH, n)), 26, va);
  }
  numWord(ctx, CL('fixed_rate'), 'fixed', LX + 44, CY + 92, 'label', { alpha: ease(t, 0.8, 1.1) });
  numWord(ctx, CL('var_start'), 'variable', RX + 44, CY + 92, 'label', { alpha: ease(t, 1.9, 2.2) });
  badge(ctx, ease(t, 0.8, 1.1));
}
