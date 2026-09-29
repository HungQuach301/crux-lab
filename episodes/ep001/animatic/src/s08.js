// S08 · Two answers. H3. First: what "worth it" means on a time line (fees paid back before she sells or moves; test
// stay = 3 years). Then a split screen: LEFT the 1-point line (Nora's cut 0.59 stops short: NO); RIGHT the division
// 5,124 / 221 (month tiles flip to 24: YES). Both dim, "?": the left never looks at the bill (bill struck), the right
// leaves something out (dashed "+ ?").
import { C, W, H, DATA, CL, text, chrome, line, rect, srect, dot, mark, strike, ease, easeOut, back, mix, inout } from './engine.js';
import { houseIcon, cutRuler, PL } from './common.js';
export const uses3d = false;

export function build({ T }) {
  const tA = T.a('ask'), tWo = T.a('worth'), tSt = T.a('stay'), tTw = T.a('two'), tO = T.a('one'), tSh = T.a('short'), tDv = T.a('div'), tD24 = T.a('div24'), tN = T.a('neither'), tB = T.a('bill'), tOut = T.a('out');
  function overlay(ctx, t) {
    // ---- part 1: what "worth it" means (time line) ----
    const p1 = 1 - ease(t, tTw, tTw + 0.6);
    if (p1 > 0) {
      text(ctx, 'Is it worth paying?', 96, 128, 'head', { alpha: p1 * easeOut(t, tA, tA + 0.4) });
      const X0 = 300, X1 = 1640, Y = 640, M = 60, xOf = (m) => X0 + (m / M) * (X1 - X0);
      line(ctx, [[X0, Y], [X1, Y]], C.grid, 6, { alpha: p1 });
      text(ctx, 'time after refinancing →', X1, Y + 140, 'note', { align: 'right', color: C.muted, alpha: p1 });
      houseIcon(ctx, X0, Y - 8, 1.2, '#C9BBA4', p1 * easeOut(t, tA, tA + 0.4), false);
      text(ctx, 'refinance', X0, Y + 70, 'label', { align: 'center', alpha: p1 * easeOut(t, tA, tA + 0.4) });
      // flag = the day she sells or moves; slides in and stops at 3 years
      const fx = mix(X1 - 40, xOf(+CL('hold36')), back(t, tSt, tSt + 1.2)), aF = p1 * easeOut(t, tWo - 0.4, tWo);
      line(ctx, [[fx, Y], [fx, Y - 230]], C.ink, 5, { alpha: aF });
      ctx.save(); ctx.globalAlpha = aF; ctx.fillStyle = C.warn; ctx.beginPath(); ctx.moveTo(fx, Y - 230); ctx.lineTo(fx + 90, Y - 200); ctx.lineTo(fx, Y - 170); ctx.fill(); ctx.restore();
      text(ctx, 'she sells or moves', fx + 110, Y - 190, 'label', { alpha: aF });
      // green bracket: fees paid back before the flag
      const g = easeOut(t, tWo, tWo + 1.0);
      rect(ctx, X0, Y - 60, (fx - X0 - 20) * g, 30, C.positive, 0.85 * p1);
      text(ctx, 'fees paid back before that = worth it', X0 + 20, Y - 90, 'label', { color: C.positive, alpha: p1 * easeOut(t, tWo + 0.6, tWo + 1.0) });
      text(ctx, CL('y3') + ' years', xOf(+CL('hold36')), Y + 70, 'label', { align: 'center', alpha: p1 * easeOut(t, tSt + 1.0, tSt + 1.4) });
      text(ctx, 'we test a ' + CL('y3') + '-year stay (our choice, not a rule)', W / 2, 900, 'label', { align: 'center', color: C.ink, alpha: p1 * easeOut(t, tSt + 1.2, tSt + 1.6) });
    }
    // ---- part 2: split screen ----
    const p2 = ease(t, tTw, tTw + 0.6);
    if (p2 <= 0) { chrome(ctx, { illus: 1 }); return; }
    const dimL = 1 - 0.55 * ease(t, tN, tN + 0.5) * (1 - ease(t, tB - 0.3, tB)), dimR = 1 - 0.55 * ease(t, tN, tN + 0.5) * (1 - ease(t, tOut - 0.3, tOut));
    line(ctx, [[W / 2, 170], [W / 2, 1000]], C.grid, 3, { alpha: p2 });
    text(ctx, 'Two quick answers', 96, 128, 'head', { alpha: p2 });
    // LEFT: the 1-point line
    const aL = p2 * easeOut(t, tO, tO + 0.4) * dimL;
    text(ctx, 'The 1-point line', 480, 260, 'caption', { align: 'center', alpha: aL });
    const xOf = cutRuler(ctx, { x0: 200, x1: 820, y: 600, max: 1.25, alpha: aL, oneLabel: true, label: false });
    const sl = ease(t, tSh, tSh + 1.4), xd = mix(xOf(0), xOf(+CL('cut_today')), sl);
    mark(ctx, 'nora', xd, 600, 20, aL * easeOut(t, tSh - 0.2, tSh));
    text(ctx, CL('cut_today'), xOf(+CL('cut_today')), 540, 'label', { align: 'center', color: C.positive, alpha: aL * easeOut(t, tSh + 1.2, tSh + 1.5) });
    const aNo = aL * easeOut(t, tSh + 1.4, tSh + 1.8);
    text(ctx, 'short of the line', xOf(+CL('cut_today')), 700, 'note', { align: 'center', color: C.ink, alpha: aNo });
    text(ctx, 'NO', 480, 860, 'hero', { align: 'center', color: C.negative, alpha: aNo });
    // the bill it never looks at
    const aBi = p2 * easeOut(t, tB, tB + 0.4);
    const wb = text(ctx, 'the bill: ' + CL('cost_median'), 480, 930, 'label', { align: 'center', alpha: aBi });
    if (aBi > 0) strike(ctx, 480 - wb / 2 - 8, 916, 480 + wb / 2 + 8, C.negative, ease(t, tB + 0.3, tB + 0.7), 6);
    text(ctx, 'not counted', 480, 990, 'note', { align: 'center', color: C.negative, alpha: p2 * easeOut(t, tB + 0.5, tB + 0.9) });
    // RIGHT: division
    const aR = p2 * easeOut(t, tDv, tDv + 0.4) * dimR;
    text(ctx, 'Simple division', 1440, 260, 'caption', { align: 'center', alpha: aR });
    text(ctx, CL('cost_median') + ' ÷ ' + CL('sav_median'), 1420, 420, 'number', { align: 'center', alpha: aR });
    // month tiles flip (24 tiles, 2 rows of 12), unnumbered; the count appears when all have flipped
    const f = ease(t, tDv + 0.5, tD24);
    for (let i = 0; i < 24; i++) { const on = f * 24 >= i + 1; rect(ctx, 1110 + (i % 12) * 56, 500 + Math.floor(i / 12) * 70, 46, 56, on ? C.ink : C.grid, aR * (on ? 0.9 : 0.5)); }
    const aY = aR * easeOut(t, tD24, tD24 + 0.4);
    text(ctx, 'about ' + CL('be_simple_median') + ' months', 1440, 740, 'label', { align: 'center', alpha: aY });
    text(ctx, 'YES', 1440, 860, 'hero', { align: 'center', color: C.positive, alpha: aY });
    const aO = p2 * easeOut(t, tOut, tOut + 0.4);
    srect(ctx, 1700, 355, 130, 90, C.warn, 4, aO, [10, 8]);
    text(ctx, '+ ?', 1765, 420, 'label', { align: 'center', color: C.warn, alpha: aO });
    text(ctx, 'something left out', 1440, 980, 'label', { align: 'center', color: C.warn, alpha: aO, plate: PL });
    // neither
    const aQ = p2 * inout(t, tN, tN + 0.4, tB - 0.3, tB);
    text(ctx, '?', W / 2, 640, 'hero', { align: 'center', color: C.warn, alpha: aQ, plate: PL });
    text(ctx, 'Neither is quite right', W / 2, 180 + 0, 'caption', { align: 'center', alpha: p2 * easeOut(t, tN, tN + 0.4), plate: PL, sent: true });
    chrome(ctx, { illus: 1, source: 'Nora (illustrative). Fees: 2025 median (HMDA).' });
  }
  return { update: () => {}, overlay, stripTimes: [tWo + 1.2, tSt + 1.8, tSh + 2.0, tD24 + 0.6, tB + 1.0, T.dur - 0.2] };
}
