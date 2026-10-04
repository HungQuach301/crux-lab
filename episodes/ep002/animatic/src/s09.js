// S09 · Moving the head start. S09.1: the signed K2 picture at Leah's 1.5 points. S09.2-S09.6 (+ S10.1-S10.3) = KEY-7: the
// signed K7 r2 clip time-warped (no sweep back, ends on the widest gap). Unspoken S09.5/S09.6 shares (8.8%, 4.5%) are not
// shown as overall shares ('of all starts') in the same K7 r2 layout (lib.k7At, the k7.js code with the gap given), one at a time.
import { ease, inout, mix, warp, shots } from './film.js';
import { k7At, k7Clip, overall } from './lib.js';
import * as K2 from '../../design/c3/final/src/k2.js';
import * as K7 from '../../design/c3/final/src/k7.js';
export function build({ T }) {
  const c = T.a('k7in');
  const k7 = warp([[0, c + 0.05], [1.0, T.a('hold')], [2.0, T.a('moving')], [2.8, T.a('leah')], [3.4, T.a('leahL')], [4.4, T.a('two') - 0.15], [5.0, T.a('two') + 0.45], [5.9, T.a('early20')]]);
  const e20 = T.a('early20'), th = T.a('three'), tf = T.a('tenfive');
  // from 'twenty point four' on: the same layout with the gap held/stepped explicitly, so the overall shares fit (one figure at a time)
  function held(ctx, t) {
    const g = 2 + 0.5 * ease(t, th - 0.3, th + 0.2) + 0.5 * ease(t, th + 0.5, th + 1.0);
    k7At(ctx, { g, l0: 1 - ease(t, e20, e20 + 0.3), l105: ease(t, tf - 0.1, tf + 0.2) });
    overall(ctx, 'spread2_share', inout(t, e20 + 0.3, e20 + 0.7, th - 0.6, th - 0.3));
    overall(ctx, 'spread3_share', inout(t, th + 1.1, th + 1.5, tf - 0.5, tf - 0.2));
  }
  return { draw(ctx, t) { shots(ctx, t, [[0, (c) => K2.draw(c, 2.9)], [c, (c, t) => (t < e20 ? k7Clip(c, k7(t)) : held(c, t))]]); } };
}
