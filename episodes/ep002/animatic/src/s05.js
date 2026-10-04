// S05 · The contradiction. S05.1-S05.4 = KEY-3: signed K3 (h3/scenes.js) time-warped; after "April 1977" a ring marks the
// worst start's cell (h3 ring(), no number: K3's last number stays the only one). S05.5: the signed K2 picture at 1.5 points.
import { warp, shots } from './film.js';
import { K3 } from '../../design/c3/final/src/h3/scenes.js';
import * as K2 from '../../design/c3/final/src/k2.js';
import { ring, FULL, WORST } from './lib.js';
export function build({ T }) {
  const k3 = warp([[0, 0.05], [0.2, T.a('k3scan')], [2.75, T.a('k3above')], [4.3, T.a('k3cost')], [4.75, T.a('k3all')], [6.5, T.a('k3halves')], [6.75, T.a('k3early')], [8.35, T.a('k3late')], [10, T.a('k3late') + 1.65]]);
  const tW = T.a('worst'), cH = T.a('cutHS');
  function three(ctx, t) { K3.draw(ctx, k3(t)); if (t > tW) ring(ctx, FULL, WORST, Math.min(1, (t - tW) / 0.3) * (0.6 + 0.4 * Math.sin((t - tW) * 7))); }
  return { draw(ctx, t) { shots(ctx, t, [[0, three], [cH, (c) => K2.draw(c, 2.9)]]); } };
}
