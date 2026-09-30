// SF6 · The three-mark ruler (S18, G-013). H3: x = loan size (three marks only: $115,000 · $375,000 · $655,000,
// with a house whose area follows the loan), y = rate cut needed to break even within 3 years. Three separate bars,
// NO line between them (no numbers exist for the loans in between). The 1-point rule of thumb slides across and
// matches none of them. An outline house ("your loan?") slides along the axis and stops between marks, with no value.
// Claims: loan_small loan_median loan_large cut36_small cut36_median cut36_large_words y3 oct2023 y2025 s10.
import { C, W, H, DATA, CL, text, measure, chrome, line, rect, mark, ease, easeOut, back, mix, clamp, rgba } from './engine.js';

export const uses3d = false;
const DUR = 11.0;

export function build() {
  const LMIN = 50000, LMAX = 720000, X0 = 200, X1 = 1600, YB = 700, PX = 300; // px per percentage point
  const xOf = (L) => X0 + (L - LMIN) / (LMAX - LMIN) * (X1 - X0);
  const who = [
    { k: 'walt', name: 'Walt', loan: DATA.small.loan, cut: DATA.cuts.small, lab: CL('cut36_small') + ' points', tier: 'number', loanL: CL('loan_small'), col: C.warn, t0: 1.4 },
    { k: 'nora', name: 'Nora', loan: DATA.median.loan, cut: DATA.cuts.median, lab: CL('cut36_median') + ' point', tier: 'number', loanL: CL('loan_median'), col: C.positive, t0: 2.4 },
    { k: 'anjali', name: 'Anjali', loan: DATA.large.loan, cut: DATA.cuts.large, lab: CL('cut36_large_words'), tier: 'label', loanL: CL('loan_large'), col: C.negative, t0: 3.4 },
  ];
  function houseIcon(ctx, cx, yb, s, fill, a, outline) { // 2D house: area ~ loan; (cx, yb) = bottom centre
    if (a <= 0) return;
    const w = 70 * s, h = 46 * s, rf = 34 * s;
    ctx.save(); ctx.globalAlpha = a; ctx.beginPath();
    ctx.moveTo(cx - w / 2, yb); ctx.lineTo(cx + w / 2, yb); ctx.lineTo(cx + w / 2, yb - h); ctx.lineTo(cx + w / 2 + 6 * s, yb - h);
    ctx.lineTo(cx, yb - h - rf); ctx.lineTo(cx - w / 2 - 6 * s, yb - h); ctx.lineTo(cx - w / 2, yb - h); ctx.closePath();
    if (outline) { ctx.setLineDash([10, 8]); ctx.strokeStyle = C.ink; ctx.lineWidth = 4; ctx.stroke(); }
    else { ctx.fillStyle = fill; ctx.fill(); }
    ctx.restore();
  }
  function overlay(ctx, t) {
    const a0 = easeOut(t, 0, 0.4);
    text(ctx, 'Rate cut needed, by loan size', 96, 124, 'caption', { alpha: a0 });
    text(ctx, 'to break even within ' + CL('y3') + ' years; point = percentage point of the rate', 96, 188, 'note', { color: C.muted, alpha: a0 });
    line(ctx, [[X0 - 40, YB], [X1 + 40, YB]], C.grid, 4);
    for (const w of who) {
      const x = xOf(w.loan), s = Math.sqrt(w.loan / DATA.median.loan) * 0.95;
      const aH = easeOut(t, w.t0 - 0.9, w.t0 - 0.5);
      houseIcon(ctx, x, YB + 18 + 46 * s + 34 * s, s, '#C9BBA4', aH, false);
      text(ctx, w.loanL, x, YB + 172, 'label', { align: 'center', alpha: aH });
      const wn = measure(ctx, w.name, 'note');
      mark(ctx, w.k, x - wn / 2 - 22, YB + 214, 16, aH); text(ctx, w.name, x - wn / 2 + 4, YB + 230, 'note', { color: C.ink, alpha: aH });
      // the bar grows to the rate cut (grow = an amount appears)
      const g = easeOut(t, w.t0, w.t0 + 0.8), hb = w.cut * PX * g;
      rect(ctx, x - 75, YB - hb, 150, hb, w.col, 0.95);
      const aL = easeOut(t, w.t0 + 0.7, w.t0 + 1.0);
      if (w.k === 'anjali') {
        text(ctx, 'about a third', x, YB - hb - 84, 'label', { align: 'center', alpha: aL });
        text(ctx, 'of a point', x, YB - hb - 26, 'label', { align: 'center', alpha: aL });
      } else text(ctx, w.lab, x, YB - hb - 26, w.tier, { align: 'center', alpha: aL });
    }
    // the 1-point rule of thumb: slides across, matches none, then fades back
    const sl = ease(t, 5.0, 6.4), fade = 1 - 0.65 * ease(t, 6.8, 7.3), y1 = YB - PX * 1;
    if (t > 5.0) line(ctx, [[X0 - 40, y1], [mix(X0 - 40, X1 + 40, sl), y1]], C.ink, 4, { dash: [16, 12], alpha: fade });
    text(ctx, CL('s10') + '-point rule of thumb', X1 + 40, y1 - 24, 'note', { align: 'right', color: C.ink, alpha: easeOut(t, 5.8, 6.2) * (1 - ease(t, 6.8, 7.3)) });
    // the viewer's loan: an outline house that slides along the axis and stops between marks, no value
    const ox = mix(X0 - 60, (xOf(DATA.median.loan) + xOf(DATA.large.loan)) / 2 + 10, back(t, 7.2, 8.8));
    const aO = easeOut(t, 7.2, 7.5);
    houseIcon(ctx, ox, YB + 18 + 80 * 0.95, 0.95, null, aO, true);
    text(ctx, 'your loan?', ox, YB + 230, 'label', { align: 'center', alpha: easeOut(t, 8.3, 8.7) });
    chrome(ctx, { illus: easeOut(t, 1.0, 1.4), source: 'Not advice. Assumes an ' + CL('oct2023') + ' rate and the median ' + CL('y2025') + ' bill.' });
  }
  return { duration: DUR, update: () => {}, overlay, stripTimes: [0.9, 2.2, 4.4, 5.9, 8.0, 10.9], hardTime: 10.95 };
}
