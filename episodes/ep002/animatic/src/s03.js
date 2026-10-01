// S03 · Leah's loan and the head start. S03.1-S03.2: the signed two-card picture (K2 at 0.55 s, no start point yet) with the
// loan and the two first payments written on it (the system has no envelope object; numbers through claims). S03.3-S03.4:
// signed K1 r2 (the level line; the variable line that runs up and down). S03.5-S03.8 = KEY-2: signed K2 fix-round clip.
import { H2, C, CL, CLS, ease, inout, warp, around, shots } from './film.js';
import * as K1 from '../../design/c3/final/src/k1.js';
import * as K2 from '../../design/c3/final/src/k2.js';
export function build({ T }) {
  const tL = T.a('loan'), tV = T.a('pVar'), tF = T.a('pFix'), c1 = T.a('cutK1'), c2 = T.a('cutK2');
  const k2a = warp([[0, 0.05], [0.55, 0.6]]);
  const k1 = warp([[0, c1 + 0.05], [1.7, c1 + 0.7], [1.9, T.a('k1var')], [2.3, T.a('k1run')], [5.4, T.a('k1end')], [7.3, T.a('k1end') + 1.6]]);
  const k2 = warp([[0, c2 + 0.05], [0.6, T.a('k2big')], [0.8, T.a('k2big') + 0.2], ...around(2.0, T.a('k2leah')), ...around(3.6, T.a('k2zero')), ...around(5.2, T.a('k2neg')), [8.0, T.a('k2neg') + 2.8]]);
  // owner C4c (a): meaning labels over the KEY-2 picture (top line, above the cards): first what the cards are, then what the gap is
  const tLe = T.a('k2leah'), tEnd = T.dur;
  function keyLabel(ctx, t) {
    H2.text(ctx, 'Different offers', 96, 140, 'caption', { alpha: inout(t, c2 + 0.3, c2 + 0.7, tLe - 0.4, tLe - 0.1) });
    H2.text(ctx, 'Head start = fixed − variable', 96, 140, 'caption', { alpha: ease(t, tLe, tLe + 0.4) });
  }
  function offers(ctx, t) {
    K2.draw(ctx, k2a(t));
    const a = ease(t, tL, tL + 0.5);
    H2.text(ctx, CL('loan') + ' over ' + CLS('term', '10 years'), 960, 150, 'caption', { align: 'center', alpha: a });
    H2.numWord(ctx, CL('fixed_payment'), 'a month', 130 + 44, 196 + 380, 'label', { alpha: ease(t, tF, tF + 0.4) });
    H2.numWord(ctx, CL('var_first_payment'), 'a month', 1110 + 44, 196 + 380, 'label', { alpha: ease(t, tV, tV + 0.4) });
  }
  return { draw(ctx, t) { shots(ctx, t, [[0, offers], [c1, (c, t) => K1.draw(c, k1(t))], [c2, (c, t) => { K2.draw(c, k2(t)); keyLabel(c, t); }]]); } };
}
