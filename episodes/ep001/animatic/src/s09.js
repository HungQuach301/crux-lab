// S09 · What break-even means. H1 (signed SF3, first half): the ream of loan costs, a level line from its top, $221
// bundles land one per month until level at month 24; then the two "balance paid off" stacks appear with a "?".
import { C, W, CL, text, chrome, ease, easeOut, mix } from './engine.js';
import { makeTable } from './table.js';
export const uses3d = true;

export function build(ctx0) {
  const { T } = ctx0;
  const tL = T.a('letter'), tLv = T.a('level'), tS = T.a('stack'), t24 = T.a('m24'), tO = T.a('owes');
  const tb = makeTable(ctx0);
  const landT = (i) => tS + (i + 1) / 24 * (t24 - tS);
  const month = (t) => t < tS ? 0 : Math.min(24, (t - tS) / (t24 - tS) * 24);
  const st = (t) => ({ cam: ease(t, 0, T.dur), billGrow: easeOut(t, tL + 1.0, tL + 2.0), level: ease(t, tLv, tLv + 0.4), savLabel: easeOut(t, tS - 0.4, tS),
    landT: (i) => (i < 24 ? landT(i) : 1e9), month: month(t), paidMonth: 24 * ease(t, tO, tO + 1.5), paidOn: easeOut(t, tO, tO + 0.4), paidQ: easeOut(t, tO + 1.2, tO + 1.6),
    owedGrow: 0, owedMove: 0, owedLabel: 0, onBill: 0, done: 0, ruler: easeOut(t, tS - 0.4, tS), n24: easeOut(t, t24, t24 + 0.3), strike24: 0,
    letter: 1, letterHl: ease(t, tL, tL + 0.5), letterCam: 1 - ease(t, tL + 0.9, tLv - 0.2) });
  return {
    update: (t) => tb.update(t, st(t)),
    overlay: (ctx, t, P) => {
      tb.overlay(ctx, t, P, st(t));
      text(ctx, 'Break-even: savings stack up to the bill', 96, 128, 'head', { alpha: easeOut(t, tLv, tLv + 0.4) });
      const aD = easeOut(t, t24, t24 + 0.4);
      text(ctx, CL('cost_median') + ' ÷ ' + CL('sav_median') + ' a month = ' + CL('be_simple_median') + ' months', 96, 196, 'label', { alpha: aD });
      chrome(ctx, { illus: 1, source: 'Nora: illustrative. Fees: HMDA ' + CL('y2025') + ' median. Dollars of the day (before inflation).', plate: true });
    },
    stripTimes: [tL + 1.2, tLv + 1.0, mix(tS, t24, 0.5), t24 + 0.6, tO + 1.8, T.dur - 0.2],
  };
}
