// S02 · Why private loans. Policy context: the system has no form/calendar object, so S02.1-S02.3 are text (claims) plus one
// plain cost outline with a neutral federal block (grid) and an ink "rest" slice (listed in README "Cần chủ dự án xem").
// S02.4 cuts to the signed K2 picture (person + two offer cards, 9% line across both) before any start point is shown.
import { H2, C, CL, CLS, ease, inout, mix, warp, shots } from './film.js';
import * as K2 from '../../design/c3/final/src/k2.js';
export function build({ T }) {
  const tK = T.a('keep'), tY = T.a('years'), tO = T.a('out1'), tB = T.a('bar'), tA = T.a('annual'), tT = T.a('total'), tP = T.a('prof'), tR = T.a('rest'), tC = T.a('cut');
  const ex = CL('ctx_plus_exception'), [who, howLong] = ex.split(': ');
  const k2 = warp([[0, tC + 0.05], [0.55, tC + 0.6]]);
  const BX = 1250, BW = 330, BT = 230, BB = 930, FED = 0.42; // cost outline; federal block = lower 42% (schematic, no scale)
  function policy(ctx, t) {
    const a1 = inout(t, tK, tK + 0.5, tO, tO + 0.4);
    H2.text(ctx, 'Grad PLUS stays for students', 96, 400, 'caption', { color: C.muted, alpha: a1 });
    H2.text(ctx, CLS('ctx_plus_exception', who), 96, 500, 'caption', { alpha: a1 });
    H2.text(ctx, CLS('ctx_plus_exception', howLong), 96, 640, 'number', { alpha: Math.min(a1, ease(t, tY, tY + 0.4)) });
    // the federal loan inside the cost of a program
    const b = ease(t, tB, tB + 0.6), fh = (BB - BT) * FED;
    if (b > 0) {
      H2.srect(ctx, BX, BT, BW, BB - BT, C.muted, 5, b);
      H2.rect(ctx, BX + 8, BB - fh * b + 8, BW - 16, fh * b - 16, C.grid, b);
      H2.text(ctx, 'Direct Unsubsidized loan', 96, 400, 'caption', { color: C.muted, alpha: b });
      const aA = inout(t, tA, tA + 0.4, tT - 0.2, tT), aT = ease(t, tT, tT + 0.4);
      H2.text(ctx, CL('ctx_unsub_annual'), 96, 530, 'number', { alpha: aA });
      H2.text(ctx, CL('ctx_unsub_aggregate'), 96, 530, 'number', { alpha: aT });
      H2.text(ctx, 'higher in professional programs', 96, 640, 'label', { color: C.muted, alpha: ease(t, tP, tP + 0.5) });
      const r = ease(t, tR, tR + 0.5);
      if (r > 0) { H2.srect(ctx, BX + 8, BT + 8, BW - 16, BB - BT - fh - 16, C.ink, 5, r); H2.text(ctx, 'private lender', BX + BW / 2, BT - 30, 'label', { align: 'center', alpha: r }); }
    }
  }
  return { draw(ctx, t) { shots(ctx, t, [[0, policy], [tC, (c, t) => K2.draw(c, k2(t))]]); } };
}
