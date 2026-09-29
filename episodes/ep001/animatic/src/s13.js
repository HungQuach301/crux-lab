// S13 · Half a point: the curve for 0.5 crosses the fees exactly at month 36 (the 3-year mark) -> Nora's line is
// half a point (a fixed tick on the ruler); her real offer (0.59) sits past it and pays back sooner. Then Walt's
// triangle and Anjali's square appear on the ruler with "?".
import { C, W, H, DATA, CL, text, chrome, line, rect, dot, mark, ease, easeOut, mix } from './engine.js';
import { G, axes, yOf, xOfM, curve, ruler, rx, RU } from './plot.js';
import { PL } from './common.js';
export const uses3d = false;

export function build({ T }) {
  const tB = T.a('between'), tH = T.a('half'), t36 = T.a('m36'), tA = T.a('answer'), tR = T.a('real'), tP = T.a('pays'), tE = T.a('everyone');
  const X = 48, c5 = DATA.c05, cr = DATA.creal;
  function overlay(ctx, t) {
    text(ctx, 'Where is her line?', 96, 128, 'head', { alpha: 1 - ease(t, tH - 0.3, tH) });
    text(ctx, 'Half a point: paid back in exactly ' + CL('y3') + ' years', 96, 128, 'head', { alpha: easeOut(t, t36, t36 + 0.4) });
    ruler(ctx);
    // the dot swings between a quarter and a full point, then settles on 0.5
    const sw = t < tH ? 0.625 + 0.375 * Math.sin((t - tB) * 2.2) : mix(0.625 + 0.375 * Math.sin((tH - tB) * 2.2), 0.5, easeOut(t, tH, tH + 0.6));
    mark(ctx, 'nora', rx(t < tB ? 1 : sw), RU.y, 18);
    // fixed tick: Nora's line
    const aA = easeOut(t, tA, tA + 0.4);
    line(ctx, [[rx(0.5), RU.y - 40], [rx(0.5), RU.y + 30]], C.positive, 6, { alpha: aA });
    text(ctx, CL('cut36_median') + " · Nora's line", rx(0.5), RU.y + 70, 'label', { align: 'center', color: C.positive, alpha: aA });
    // real offer 0.59
    const aR = easeOut(t, tR, tR + 0.4);
    dot(ctx, rx(+CL('cut_today')), RU.y, 14, C.ink, aR);
    text(ctx, 'offer ' + CL('cut_today'), rx(+CL('cut_today')) + 40, RU.y + 124, 'note', { align: 'center', color: C.ink, alpha: aR });
    const yF = axes(ctx, X), m3 = +CL('hold36');
    line(ctx, [[xOfM(m3, X), G.YT - 10], [xOfM(m3, X), G.YB]], C.warn, 4, { dash: [14, 10] });
    text(ctx, CL('y3') + ' years', xOfM(m3, X), G.YT - 34, 'label', { align: 'center', color: C.warn });
    if (t > tH) curve(ctx, c5.net, ease(t, tH, t36 + 0.2) * X, X, C.positive, 7, 1 - 0.5 * ease(t, tP, tP + 0.4));
    const aX = easeOut(t, t36, t36 + 0.3);
    dot(ctx, xOfM(c5.be, X), yF, 15, C.ink, aX);
    text(ctx, 'month ' + CL('be_bal_05'), xOfM(c5.be, X) - 20, yF - 34, 'label', { align: 'right', alpha: aX * (1 - ease(t, tP, tP + 0.4)), plate: PL });
    // the real offer's curve (0.59) crosses sooner
    if (t > tP) curve(ctx, cr.net, ease(t, tP, tP + 1.4) * X, X, C.ink, 5);
    const aP = easeOut(t, tP + 1.2, tP + 1.6);
    dot(ctx, xOfM(cr.be, X), yF, 13, C.ink, aP);
    text(ctx, 'her offer (' + CL('cut_today') + '): paid back within ' + CL('y3') + ' years', G.X0 + 20, yF + 80, 'label', { alpha: aP, plate: PL });
    // is half a point the line for everyone?
    const aE = easeOut(t, tE, tE + 0.5);
    mark(ctx, 'walt', rx(1.12) + 20, RU.y - 90, 18, aE * 0.8); mark(ctx, 'anjali', rx(0.25), RU.y - 90, 18, aE * 0.8);
    text(ctx, '?', rx(1.12) + 60, RU.y - 72, 'label', { color: C.warn, alpha: aE }); text(ctx, '?', rx(0.25) + 40, RU.y - 72, 'label', { color: C.warn, alpha: aE });
    text(ctx, 'The same line for everyone?', W / 2, 1036, 'caption', { align: 'center', alpha: aE, plate: PL, sent: true });
    chrome(ctx, { illus: 1, source: t < tE ? 'Nora (illustrative). Counting what she still owes.' : '' });
  }
  return { update: () => {}, overlay, stripTimes: [tB + 1.0, t36 + 0.6, tA + 0.8, tR + 0.8, tP + 1.8, T.dur - 0.2] };
}
