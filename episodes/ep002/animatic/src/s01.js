// S01 · Cold open (CO-A). S01.1: the dated context (text only: the system has no calendar/form object; see README).
// S01.2-S01.3 = KEY-1: the signed K1 r2 clip (design/c3/final/src/k1.js) unchanged, time-warped onto the anchors.
import { H2, C, CL, ease, inout, warp, shots } from './film.js';
import * as K1 from '../../design/c3/final/src/k1.js';
export function build({ T }) {
  const tCut = T.a('cut'), tD = T.a('date'), tP = T.a('plus'), tE = T.e('1');
  const k1 = warp([[0, tCut + 0.05], [0.8, T.a('k1fixed')], [1.9, T.a('k1var')], [2.3, T.a('k1path')], [5.4, T.a('k1risk')], [7.3, T.a('k1end')], [8.0, T.a('k1end') + 0.7]]);
  function context(ctx, t) {
    const a = inout(t, tD, tD + 0.5, tE + 0.1, tCut);
    H2.text(ctx, CL('ctx_plus_end'), 960, 500, 'number', { align: 'center', alpha: a });
    H2.text(ctx, 'Grad PLUS ends for new graduate students', 960, 610, 'caption', { align: 'center', color: C.muted, alpha: Math.min(a, ease(t, tP, tP + 0.5)) });
  }
  return {
    draw(ctx, t) { shots(ctx, t, [[0, context], [tCut, (c, t) => K1.draw(c, k1(t))]]); },
  };
}
