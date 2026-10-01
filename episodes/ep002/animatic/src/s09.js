// S09 · Moving the head start. S09.1: the signed K2 picture at Leah's 1.5 points. S09.2-S09.6 (+ S10.1-S10.3) = KEY-7: the
// signed K7 r2 clip time-warped (no sweep back, ends on the widest gap). Unspoken S09.5/S09.6 shares (8.8%, 4.5%) are not
// drawn: K7 r2 has no place for them (README).
import { warp, shots } from './film.js';
import * as K2 from '../../design/c3/final/src/k2.js';
import * as K7 from '../../design/c3/final/src/k7.js';
export function build({ T }) {
  const c = T.a('k7in');
  const k7 = warp([[0, c + 0.05], [1.0, T.a('hold')], [2.0, T.a('moving')], [2.8, T.a('leah')], [3.4, T.a('leahL')], [4.4, T.a('two') - 0.15], [5.0, T.a('two') + 0.45], [6.0, T.a('early20')],
    [6.4, T.a('three')], [7.6, T.a('three') + 1.0], [8.0, T.a('tenfive')], [10, T.a('tenfive') + 2.0]]);
  return { draw(ctx, t) { shots(ctx, t, [[0, (c) => K2.draw(c, 2.9)], [c, (c, t) => K7.draw(c, k7(t))]]); } };
}
