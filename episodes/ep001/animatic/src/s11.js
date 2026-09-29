// S11 · A quarter point (signed SF4): division crosses the fees at month 38; counting what she still owes the curve
// comes close, never touches, and falls away before the old loan's last payment: "Never".
import { C, W, H, DATA, CL, text, chrome, line, dot, mark, ease, easeOut, mix } from './engine.js';
import { G, axes, yOf, xOfM, curve, ruler, rx, RU } from './plot.js';
export const uses3d = false;

export function build({ T }) {
  const tS = T.a('smaller'), tQ = T.a('q'), tD = T.a('d38'), tC = T.a('curve'), tN = T.a('never');
  const Q = DATA.q025, NM = Q.months;
  const xmax = (t) => mix(60, NM, ease(t, tN - 0.6, tN + 0.8));
  function overlay(ctx, t) {
    text(ctx, 'If her rate were cut only ' + CL('s025') + ' point', 96, 128, 'head', { alpha: easeOut(t, tQ, tQ + 0.4) });
    text(ctx, 'The smaller the cut…', 96, 128, 'head', { alpha: 1 - easeOut(t, tQ - 0.3, tQ) });
    ruler(ctx);
    const c = t < tS ? +CL('cut_today') : mix(+CL('cut_today'), 0.25, ease(t, tS + 0.3, tQ + 0.2));
    mark(ctx, 'nora', rx(c), RU.y, 18);
    text(ctx, CL('s025'), rx(0.25), RU.y + 62, 'label', { align: 'center', color: C.positive, alpha: easeOut(t, tQ + 0.2, tQ + 0.5) });
    const X = xmax(t), yF = axes(ctx, X);
    // division: savings only
    const mD = ease(t, tD - 1.0, tD + 0.3) * (G.VMAX / Q.sav);
    if (t > tD - 1.0) line(ctx, [[xOfM(0, X), yOf(0)], [xOfM(Math.min(mD, X), X), yOf(Math.min(mD, X) * Q.sav)]], C.ink, 6, { alpha: 1 - 0.6 * ease(t, tN - 0.6, tN) });
    const m38 = +CL('be_simple_025'), aX = easeOut(t, tD, tD + 0.4) * (1 - ease(t, tN - 0.6, tN - 0.2));
    dot(ctx, xOfM(m38, X), yF, 13, C.ink, aX);
    line(ctx, [[xOfM(m38, X), yF + 16], [xOfM(m38, X), G.YB]], C.ink, 2, { dash: [6, 8], alpha: aX });
    text(ctx, 'division: month ' + CL('be_simple_025'), xOfM(m38, X) + 16, G.YB - 30, 'label', { alpha: aX });
    // counting what she still owes
    const up = t < tN - 0.6 ? ease(t, tC, tN - 0.6) * 58 : 58 + ease(t, tN - 0.6, tN + 0.8) * (NM - 58);
    if (t > tC) curve(ctx, Q.net, up, X);
    const aC = easeOut(t, tC + 0.4, tC + 0.8);
    text(ctx, 'savings minus what she still owes', G.X0 + 20, G.YB - 30, 'label', { color: C.positive, alpha: aC * (1 - aX) });
    const aN = easeOut(t, tN + 0.6, tN + 1.0);
    line(ctx, [[G.X1, G.YB - 24], [G.X1, G.YB + 16]], C.muted, 3, { alpha: aN });
    text(ctx, CL('be_bal_025').replace(/^./, (s) => s.toUpperCase()), 1180, 620, 'hero', { align: 'center', color: C.negative, alpha: aN });
    text(ctx, "not before the old loan's last payment", 1180, 690, 'label', { align: 'center', color: C.ink, alpha: aN });
    text(ctx, 'savings minus what she still owes', G.X0 + 20, G.YB - 30, 'label', { color: C.positive, alpha: aN });
    chrome(ctx, { illus: 1, source: 'Nora (illustrative). Fees paid in cash. Dollars of the day.' });
  }
  return { update: () => {}, overlay, stripTimes: [tQ + 0.4, tD + 0.8, tC + 1.2, tC + 2.8, tN + 1.2, T.dur - 0.2] };
}
