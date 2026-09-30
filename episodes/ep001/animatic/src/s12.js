// S12 · A full point: same plot, first 48 months; the curve crosses the fees at month 18, well before the 3-year mark.
import { C, W, H, DATA, CL, text, chrome, line, rect, dot, mark, ease, easeOut, mix } from './engine.js';
import { G, axes, yOf, xOfM, curve, ruler, rx, RU } from './plot.js';
export const uses3d = false;
export const basisCorner = [1824, 1016]; // BASIS_MODE corner: label position (right-aligned baseline) here: the small cut ruler holds the top right

export function build({ T }) {
  const tF = T.a('full'), t18 = T.a('m18'), tI = T.a('inside');
  const X = 48, c = DATA.c10;
  function overlay(ctx, t) {
    text(ctx, 'If the cut were a full point', 96, 128, 'head');
    ruler(ctx);
    mark(ctx, 'nora', rx(mix(0.25, 1, ease(t, tF - 0.4, tF + 0.5))), RU.y, 18);
    const yF = axes(ctx, X);
    const m3 = +CL('hold36');
    line(ctx, [[xOfM(m3, X), G.YT - 10], [xOfM(m3, X), G.YB]], C.warn, 4, { dash: [14, 10] });
    text(ctx, CL('y3') + ' years', xOfM(m3, X), G.YT - 34, 'label', { align: 'center', color: C.warn });
    if (t > tF) curve(ctx, c.net, ease(t, tF, t18 + 0.2) * X, X);
    const aX = easeOut(t, t18, t18 + 0.3), x18 = xOfM(c.be, X);
    dot(ctx, x18, yF, 13, C.ink, aX);
    text(ctx, 'month ' + CL('be_bal_10'), x18, G.YB + 64, 'label', { align: 'center', alpha: aX });
    const aB = easeOut(t, tI, tI + 0.4);
    rect(ctx, x18, yF + 60, (xOfM(m3, X) - x18) * aB, 16, C.positive, 0.8);
    text(ctx, 'well inside ' + CL('y3') + ' years', (x18 + xOfM(m3, X)) / 2, yF + 130, 'label', { align: 'center', color: C.positive, alpha: aB });
    chrome(ctx, { illus: 1, source: 'Nora (illustrative). Counting what she still owes.' });
  }
  return { update: () => {}, overlay, stripTimes: [0.3, tF, tF + 0.9, t18 + 0.2, tI + 0.4, T.dur - 0.1] };
}
