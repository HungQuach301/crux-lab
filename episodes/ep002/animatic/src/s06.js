// S06 · The cushion. S06.1-S06.4 = KEY-4: the signed K4 jar clip (with the C3d technical fix: jar empty, then filling in the
// first third of the beat), time-warped. S06.5: the same K4 drawing (lib.jarRun = k4.js draw, parameterised) for the falling
// stretch from August 1981; its jar has its own scale ($15,295 = full), stated in README.
import { easeOut, warp, shots } from './film.js';
import * as K4 from '../../design/c3/final/src/k4.js';
import { jarRun } from './lib.js';
export function build({ T }) {
  const k4 = warp([[0, 0.05], [0.9, T.a('fill0')], [2.5, T.a('full')], [2.5, T.a('climb')], [3.3, T.a('climb') + 1.6], [5.0, T.a('dry')], [8.8, T.a('years')], [10, T.a('years') + 1.2]]);
  const cF = T.a('cutFall');
  return { draw(ctx, t) { shots(ctx, t, [[0, (c, t) => K4.draw(c, k4(t))], [cF, (c, t) => jarRun(c, '1981-08', 119 * easeOut(t, cF + 0.25, cF + 2.8), { r0: 3.0, jarMax: 15295 })]]); } };
}
