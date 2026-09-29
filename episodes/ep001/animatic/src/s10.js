// S10 · Starting the clock over. Kết hợp: H3 a 30-year clock (one tick = one monthly payment): 35 ticks lit, then the
// hand spins back to 0 (a fresh 30-year clock); payment bars: the part that pays down the loan is thinner on the new
// loan -> H1 (signed SF3): the two "balance paid off" stacks grow to month 24, the new one shorter; the difference
// ($1,133, hatched) lifts onto the ream; six more bundles; break-even month 30.
import { C, W, H, DATA, CL, text, chrome, line, rect, dot, ease, easeOut, back, mix, clamp } from './engine.js';
import { makeTable } from './table.js';
import { PL } from './common.js';
export const uses3d = true;

export function build(ctx0) {
  const { T } = ctx0;
  const tC = T.a('clock'), tK = T.a('k35'), tE = T.a('each'), tR = T.a('reset'), tI = T.a('interest'), tSl = T.a('slow'), tG = T.a('gap'), tMv = T.a('move'), tMo = T.a('more'), t24 = T.a('from24'), t30 = T.a('be30');
  const tb = makeTable(ctx0);
  const k35 = DATA.k;
  // ---- H3 clock ----
  const CX = 560, CY = 590, RR = 290;
  const lit = (t) => t < tR ? ease(t, tK - 1.2, tK) * k35 : k35 * (1 - ease(t, tR, tR + 1.2));
  const sp = DATA.split;
  function clock(ctx, t) {
    text(ctx, 'A mortgage is a ' + CL('term30') + '-year clock', 96, 128, 'head', { alpha: easeOut(t, tC, tC + 0.4) });
    text(ctx, 'one tick = one monthly payment', 96, 190, 'note', { color: C.muted, alpha: easeOut(t, tC + 0.3, tC + 0.7) });
    const n = lit(t);
    for (let i = 0; i < 360; i++) {
      const a = -Math.PI / 2 + (i / 360) * Math.PI * 2, on = i < n, r0 = RR - (i % 12 === 0 ? 34 : 18);
      line(ctx, [[CX + Math.cos(a) * r0, CY + Math.sin(a) * r0], [CX + Math.cos(a) * RR, CY + Math.sin(a) * RR]], on ? C.positive : C.grid, on ? 5 : 3);
    }
    const ha = -Math.PI / 2 + (n / 360) * Math.PI * 2;
    line(ctx, [[CX, CY], [CX + Math.cos(ha) * (RR - 50), CY + Math.sin(ha) * (RR - 50)]], C.ink, 8);
    dot(ctx, CX, CY, 14, C.ink);
    const aK = easeOut(t, tK, tK + 0.4) * (1 - ease(t, tR, tR + 0.4));
    text(ctx, CL('k35') + ' payments made', CX, CY + RR + 90, 'label', { align: 'center', color: C.positive, alpha: aK });
    const aR = easeOut(t, tR + 0.8, tR + 1.2);
    text(ctx, 'new loan: the clock starts again', CX, CY + RR + 90, 'label', { align: 'center', color: C.warn, alpha: aR });
    // payment bars: dollars scale; interest (muted) | pays down the loan (green)
    const px = 0.28, BX = 950;
    const bar = (y, s, a, lab) => {
      if (a <= 0) return;
      text(ctx, lab, BX, y - 26, 'label', { alpha: a });
      rect(ctx, BX, y, s.interest * px * a, 70, C.muted, 0.55);
      rect(ctx, BX + s.interest * px, y, s.principal * px * ease(a, 0.6, 1), 70, C.positive, 0.95);
      rect(ctx, BX, y + 90, s.principal * 2.0 * ease(a, 0.6, 1), 26, C.positive, 0.95);
    };
    const aE = easeOut(t, tE, tE + 0.8), aI = easeOut(t, tI, tI + 0.8);
    bar(420, sp.old, aE, 'one payment, old loan');
    bar(740, sp.new, aI, 'one payment, new loan');
    text(ctx, 'goes to interest', BX + 20, 470, 'note', { color: C.ink, alpha: aE });
    text(ctx, 'green: pays down the loan (below: magnified)', BX, 600, 'note', { color: C.positive, alpha: aE });
    text(ctx, 'the new loan pays down less each month', BX, 900, 'label', { color: C.warn, alpha: easeOut(t, tI + 0.8, tI + 1.2) });
    chrome(ctx, { illus: 1 });
  }
  // ---- H1 table ----
  const month = (t) => t < tMo ? 24 : Math.min(30, 24 + (t - tMo) / Math.max(0.5, t30 - 0.3 - tMo) * 6);
  const landT = (i) => (i < 24 ? -1 : tMo + (i - 23) / 6 * Math.max(0.5, t30 - 0.3 - tMo));
  const st = (t) => ({ cam: ease(t, tSl, T.dur), billGrow: 1, level: 1, savLabel: 1, landT, month: month(t), paidMonth: 24 * ease(t, tSl, tSl + 3.0),
    paidOn: 1, paidQ: 0, owedGrow: easeOut(t, tG, tG + 0.8), owedMove: ease(t, tMv, tMv + 1.2), owedLabel: easeOut(t, tG + 0.3, tG + 0.7) * (1 - ease(t, tMv, tMv + 0.3)),
    onBill: easeOut(t, tMv + 1.0, tMv + 1.4), done: easeOut(t, t30, t30 + 0.4), ruler: 1, n24: 1, strike24: ease(t, t24, t24 + 0.4), letter: 0 });
  // the owed slab keeps growing with the month once it sits on the ream (month() drives the gap)
  return {
    mode: (t) => (t >= tSl ? '3d' : '2d'),
    update: (t) => tb.update(t, st(t)),
    overlay: (ctx, t, P, m) => {
      if (m !== '3d') return clock(ctx, t);
      tb.overlay(ctx, t, P, st(t));
      const aD = 1 - ease(t, t30 - 0.4, t30);
      text(ctx, 'By month ' + CL('be_simple_median') + ': old loan vs new loan', 96, 128, 'head', { alpha: aD * easeOut(t, tSl, tSl + 0.4) * (1 - ease(t, tG, tG + 0.3)) });
      text(ctx, 'Break-even: month ' + CL('be_bal_median'), 96, 150, 'number', { color: C.positive, alpha: easeOut(t, t30, t30 + 0.4) });
      text(ctx, 'not month ' + CL('be_simple_median'), 96, 226, 'label', { alpha: easeOut(t, t30 + 0.3, t30 + 0.7) });
      chrome(ctx, { illus: 1, source: 'Nora: illustrative. Fees: HMDA ' + CL('y2025') + ' median. Dollars of the day (before inflation).', plate: true });
    },
    stripTimes: [tK + 0.8, tE + 1.4, tI + 1.4, tSl + 3.4, tMv + 1.6, T.dur - 0.2],
  };
}
