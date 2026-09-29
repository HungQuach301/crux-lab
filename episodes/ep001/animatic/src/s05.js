// S05 · The window, and the one-point line. H3 (SF1 window grammar): the test line slides down 1 point below Nora's
// rate; weeks under it light up (29 in 2026); the gap at the low grows into a 1.64-point bar; after July 23, 2026 the
// window is hatched "closed"; to the right of the latest week an empty dashed zone "?" = no forecast.
import { C, W, H, DATA, CL, text, chrome, line, rect, srect, dot, hatch, ease, easeOut, mix } from './engine.js';
import { rateLine, PL } from './common.js';
export const uses3d = false;

export function build({ T }) {
  const tD = T.a('draw'), tL = T.a('line'), tT = T.a('test'), tX = T.a('cross'), tW = T.a('weeks'), tG = T.a('gap'), tC = T.a('closed'), tF = T.a('future');
  const F = DATA.f1, wk = F.weeks, N = wk.length;
  const X0 = 200, X1 = 1330, YB = 780, R0 = 5.8, R1 = 7.9, YT = 260;
  const xOf = (i) => X0 + (i / (N - 1)) * (X1 - X0), yOf = (r) => YB - ((r - R0) / (R1 - R0)) * (YB - YT);
  const iLow = wk.findIndex((w) => w.d === F.low), iLast = wk.findIndex((w) => w.d === F.lastIn), iFirst = wk.findIndex((w) => w.in);
  const in26 = wk.map((w, i) => [w, i]).filter(([w]) => w.in && w.d.startsWith('2026')).map(([, i]) => i);
  function overlay(ctx, t) {
    text(ctx, 'US 30-year mortgage rate, weekly', 96, 128, 'head');
    line(ctx, [[X0, YB], [X1, YB]], C.grid, 3);
    for (const [m, s] of [['2025-08', 'Aug ' + CL('y2025')], ['2025-11', 'Nov'], ['2026-02', 'Feb 2026'], ['2026-05', 'May'], ['2026-08', 'Aug']]) {
      const i = wk.findIndex((w) => w.d.slice(0, 7) === m); const x = xOf(i); line(ctx, [[x, YB], [x, YB + 14]], C.grid, 3); text(ctx, s, x, YB + 60, 'note', { color: C.muted, align: 'center' });
    }
    // Nora's rate + the test line sliding down from it
    const yN = yOf(F.rOld), sl = ease(t, tL, tL + 1.4), yT = mix(yN, yOf(F.thr), sl);
    line(ctx, [[X0, yN], [X1, yN]], C.muted, 4, { dash: [14, 12] });
    dot(ctx, X0 + 16, yN - 40, 15, C.positive); text(ctx, 'Nora ' + CL('r_old'), X0 + 44, yN - 24, 'label');
    const aT = easeOut(t, tL, tL + 0.3);
    line(ctx, [[X0, yT], [X1, yT]], C.accent, 5, { dash: [6, 10], alpha: aT });
    text(ctx, CL('s10') + ' point below Nora', X1 + 24, yT + 14, 'label', { color: C.accent, alpha: easeOut(t, tL + 1.2, tL + 1.6) * (1 - ease(t, tW - 0.5, tW)) });
    text(ctx, '(our test value)', X1 + 24, yT + 64, 'note', { color: C.accent, alpha: easeOut(t, tT, tT + 0.4) * (1 - ease(t, tW - 0.5, tW)) });
    // the window fills over the in-window weeks (left to right), then closes
    const fill = ease(t, tX, tX + 2.5), closed = ease(t, tC, tC + 0.8);
    const xa = xOf(iFirst - 0.5), xb = mix(xa, xOf(iLast + 0.5), fill), yT1 = yOf(F.thr);
    if (fill > 0) { rect(ctx, xa, yT1, xb - xa, YB - yT1, C.accent, mix(0.22, 0.08, closed)); if (closed > 0) hatch(ctx, xa, yT1, xb - xa, YB - yT1, C.muted, 0.3 * closed, 22, 3); }
    const h = rateLine(ctx, wk, xOf, yOf, ease(t, tD, tD + 3.5) * (N - 1)); if (h) dot(ctx, h[0], h[1], 10, C.accent);
    // 29 weeks of 2026: one tick per week, lit in order, then the count
    const aw = ease(t, tW, tW + 2.2);
    in26.forEach((i, k) => { const on = aw * in26.length >= k + 1; rect(ctx, xOf(i) - 5, YB + 90, 10, 34, on ? C.accent : C.grid, easeOut(t, tW - 0.3, tW)); });
    text(ctx, CL('weeks_below_r_old_minus_1') + ' weeks in 2026 at least ' + CL('s10') + ' point below', mix(xOf(in26[0]), xOf(in26[in26.length - 1]), 0.5), YB + 180, 'label', { align: 'center', color: C.accent, alpha: easeOut(t, tW + 2.2, tW + 2.6) });
    // the gap at the low: a bar from the low up to Nora's rate
    const g = easeOut(t, tG, tG + 0.9), xl = xOf(iLow), yl = yOf(wk[iLow].r);
    if (g > 0) { rect(ctx, xl - 14, mix(yl, yN, g), 28, (yl - yN) * g, C.positive, 0.85); }
    text(ctx, CL('cut_low2026') + ' points', xl + 30, mix(yl, yN, 0.5) + 10, 'number', { alpha: easeOut(t, tG + 0.7, tG + 1.0) * (1 - closed), plate: PL });
    text(ctx, 'gap at the low (' + CL('low2026') + ')', xl + 30, mix(yl, yN, 0.5) + 70, 'note', { color: C.ink, alpha: easeOut(t, tG + 0.7, tG + 1.0) * (1 - closed), plate: PL });
    // closed after the last window week
    const xc = xOf(iLast + 0.5);
    line(ctx, [[xc, yT1 - 40], [xc, YB]], C.ink, 3, { alpha: closed });
    text(ctx, 'last week: ' + CL('cut1_last_2026'), xc, yT1 - 60, 'label', { align: 'center', alpha: closed, plate: PL });
    text(ctx, 'window closed', xOf(iFirst) + 20, YB - 28, 'label', { alpha: closed });
    // no forecast: empty zone after the latest week
    const aF = easeOut(t, tF, tF + 0.6), fx0 = X1 + 30, fx1 = 1780;
    srect(ctx, fx0, YT, fx1 - fx0, YB - YT, C.muted, 3, aF, [10, 10]);
    text(ctx, '?', (fx0 + fx1) / 2, (YT + YB) / 2 + 40, 'hero', { align: 'center', color: C.muted, alpha: aF });
    text(ctx, 'next?', (fx0 + fx1) / 2, YB - 30, 'label', { align: 'center', color: C.muted, alpha: aF });
    text(ctx, 'History, not a forecast · US only', 96, 200, 'caption', { alpha: easeOut(t, tF + 0.8, tF + 1.2), plate: PL });
    chrome(ctx, { illus: 1, source: t < tF ? 'Freddie Mac weekly survey, via FRED. Nora is illustrative.' : '' });
  }
  return { update: () => {}, overlay, stripTimes: [tL + 1.8, tX + 2.8, tW + 3.0, tG + 1.4, tC + 1.2, T.dur - 0.2], hardTime: T.dur - 0.1 };
}
