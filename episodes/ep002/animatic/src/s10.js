// S10 · Other offers, and the answer. S10.1-S10.3: KEY-7 continues, held on K7's final state (signed rule: no sweep back;
// the S10.1 "smaller/reversed head start" figures are spoken only; README). S10.4: KEY-1 final state (the question).
// S10.5: K7 final. S10.6: K7 from 2 points (right clear, 0%) to 3 points (left keeps red, 10.5%). S10.7: ridge ends at today.
import { ease, warp, shots } from './film.js';
import * as K1 from '../../design/c3/final/src/k1.js';
import * as K7 from '../../design/c3/final/src/k7.js';
import { ridgeToday } from './lib.js';
export function build({ T }) {
  const tQ = T.a('q'), t2 = T.a('two'), tL = T.a('late'), tT = T.a('today');
  const k7 = warp([[5.5, tL + 0.05], [5.8, T.a('enough')], [7.6, T.a('early')], [8.0, T.a('notEnough')], [10, T.a('notEnough') + 2.0]]);
  return { draw(ctx, t) { shots(ctx, t, [[0, (c) => K7.draw(c, 10)], [tQ, (c) => K1.draw(c, 8)], [t2, (c) => K7.draw(c, 10)], [tL, (c, t) => K7.draw(c, k7(t))], [tT, (c, t) => ridgeToday(c, ease(t, tT, tT + 0.5))]]); } };
}
