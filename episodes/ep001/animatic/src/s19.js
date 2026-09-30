// S19 · What this does not tell you. H3: the three bars fade to ghosts; a scale of 2025 refinance bills appears with
// the middle half ($3,443 - $8,270) shaded and $5,124 inside it; around an outline house: your rate? your bill? your
// balance?; two chips: fees added to the loan / a shorter term -> different math.
import { C, W, H, DATA, CL, text, chrome, line, rect, srect, dot, mark, ease, easeOut, back, mix, roundRect, withObj, CHAR, nb } from './engine.js';
import { houseIcon, PL } from './common.js';
export const uses3d = false;

export function build({ T }) {
  const tF = T.a('fade'), t25 = T.a('p25'), t75 = T.a('p75'), tR = T.a('real'), tRo = T.a('roll'), tTe = T.a('term');
  const B = DATA.bills, X0 = 260, X1 = 1660, V0 = 1500, V1 = 11500, xOf = (v) => X0 + (v - V0) / (V1 - V0) * (X1 - X0), Y = 470;
  function chip(ctx, x, y, s, a) {
    if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = C.warn; ctx.lineWidth = 4; roundRect(ctx, x - 20, y - 50, 560, 76, 38); ctx.stroke(); ctx.restore();
    text(ctx, s, x + 260, y, 'label', { align: 'center', color: C.warn, alpha: a });
  }
  function overlay(ctx, t) {
    // ghost of the three bars (from S18), fading
    const g = (1 - 0.75 * ease(t, tF, tF + 1.2)) * (1 - ease(t, t25 - 0.8, t25 - 0.2));
    [[336, 1.12, C.warn, 'walt', 'Walt'], [860, 0.5, C.positive, 'nora', 'Nora'], [1466, 0.32, C.negative, 'anjali', 'Anjali']].forEach(([x, c, col, who, name]) => {
      withObj({ role: 'bar', chart: 's19-ghost', value: c, full: true, orient: 'v', char: CHAR[who] }, () => rect(ctx, x - 75, 690 - c * 300, 150, c * 300, col, 0.9 * g));
      mark(ctx, who, x - 40, 740, 14, g); text(ctx, name, x - 18, 755, 'label', { alpha: g });
    });
    text(ctx, 'rate cut needed, by loan size', 96, 820, 'note', { color: C.muted, alpha: g });
    text(ctx, 'What these numbers are', 96, 124, 'head');
    const aN = easeOut(t, tF, tF + 0.5);
    text(ctx, 'national average rates · median ' + CL('y2025') + ' bills · three illustrative borrowers', 96, 186, 'note', { color: C.muted, alpha: aN });
    text(ctx, 'Assumes: the offer matches the national average · ' + CL('oct2023') + ' rate · ' + CL('term30') + '-year term', 96, 232, 'note', { color: C.muted, alpha: aN });
    text(ctx, 'fees paid in cash · fees paid back within ' + CL('y3') + ' years', 96, 278, 'note', { color: C.muted, alpha: aN });
    // the bill scale
    const aS = easeOut(t, t25 - 0.6, t25);
    line(ctx, [[X0, Y], [X1, Y]], C.grid, 6, { alpha: aS });
    text(ctx, CL('y2025') + ' refinance bills' + nb(', in dollars of the day'), X0, Y - 130, 'label', { alpha: aS });
    const a25 = easeOut(t, t25, t25 + 0.4), a75 = easeOut(t, t75, t75 + 0.4);
    line(ctx, [[xOf(B.p25), Y - 60], [xOf(B.p25), Y + 40]], C.ink, 4, { alpha: a25 });
    text(ctx, CL('cost_p25'), xOf(B.p25), Y + 110, 'number', { align: 'center', alpha: a25 });
    line(ctx, [[xOf(B.p75), Y - 60], [xOf(B.p75), Y + 40]], C.ink, 4, { alpha: a75 });
    text(ctx, CL('cost_p75'), xOf(B.p75), Y + 110, 'number', { align: 'center', alpha: a75 });
    const fl = ease(t, t75, t75 + 1.0);
    rect(ctx, xOf(B.p25), Y - 50, (xOf(B.p75) - xOf(B.p25)) * fl, 100, C.accent, 0.25);
    text(ctx, 'half of all bills fall in here', (xOf(B.p25) + xOf(B.p75)) / 2, Y - 70, 'label', { align: 'center', color: C.accent, alpha: easeOut(t, t75 + 0.8, t75 + 1.2) });
    dot(ctx, xOf(B.p50), Y, 20, C.warn, fl);
    line(ctx, [[xOf(B.p50), Y + 22], [xOf(B.p50), Y + 136]], C.warn, 3, { alpha: fl });
    text(ctx, "Nora's " + CL('cost_median'), xOf(B.p50), Y + 180, 'note', { align: 'center', color: C.warn, alpha: fl });
    // the viewer's numbers will differ
    const aR = easeOut(t, tR, tR + 0.4);
    houseIcon(ctx, 400, 900, 1.5, null, aR, true);
    ['your rate?', 'your bill?', 'your balance?'].forEach((s, i) => text(ctx, s, 560, 780 + i * 60, 'label', { alpha: easeOut(t, tR + i * 0.35, tR + 0.3 + i * 0.35) }));
    chip(ctx, 900, 820, 'fees added to the loan', easeOut(t, tRo, tRo + 0.4));
    chip(ctx, 900, 930, 'a shorter term', easeOut(t, tTe, tTe + 0.4));
    text(ctx, '→ different math', 1466, 880, 'label', { align: 'left', color: C.ink, alpha: easeOut(t, tTe + 0.4, tTe + 0.8) });
    chrome(ctx, { illus: 1, source: 'HMDA ' + CL('y2025') + ' (US home-loan records): total loan costs. Not advice.' });
  }
  return { update: () => {}, overlay, stripTimes: [tF + 1.4, t25 + 0.8, t75 + 1.6, tR + 1.4, tRo + 1.0, T.dur - 0.2], hardTime: T.dur - 0.1 };
}
