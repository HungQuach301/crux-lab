// S08 · The worst stretch. S08.1-S08.7 = KEY-6: signed K6 (h3/scenes.js) time-warped. S08.8: the K6 end layout redrawn with
// the same H3 pieces (zoomed frame, coin piles) plus a ceiling line (rail-like, dashed ink-muted: the system has no "cap"
// object; listed in README) that lowers while the costlier block shrinks to the claimed worst case under a 15% then 12% cap.
import { H2, H3, C, CL, ease, mix, warp, shots } from './film.js';
import { K6 } from '../../design/c3/final/src/h3/scenes.js';
import { V, X, Y, ridge, frame, coins, SER, NM, WORST } from './lib.js';
const val = (id) => +CL(id).replace(/[^0-9.]/g, '');
export function build({ T }) {
  const k6 = warp([[0, 0.05], [1.0, T.a('april') - 0.4], [2.4, T.a('april') + 1.4], [2.6, T.a('ride')], [3.2, T.a('grows')], [5.0, T.a('peak')], [6.0, T.a('gone')], [6.1, T.a('coins') - 0.3],
    [6.5, T.a('coins')], [7.3, T.a('fixint')], [7.9, T.a('extra')], [8.6, T.a('more')], [10, T.a('more') + 1.6]]);
  const cC = T.a('cutCap'), tC = T.a('cap');
  const i = WORST, v = V({ m0: i - 22, m1: i + 126, Yt: 230, Yb: 860, X0: 96, X1: 1320 }), S = 330 / 26005.46;
  const W0 = 11218.65, W15 = val('cap15_worst'), W12 = val('cap12_worst');
  // owner C4c (a): what this picture is (bottom line, under the zoomed frame)
  function worstLabel(ctx, t) { H2.text(ctx, 'Worst replay: variable vs fixed interest', 96, 990, 'caption', { alpha: ease(t, 0.4, 0.9) }); }
  function cap(ctx, t) {
    ridge(ctx, v, { alpha: 0.2, to: i }); ridge(ctx, v, { from: i, to: i + 120, alpha: 1 });
    const f = frame(ctx, v, i, { ride: 120, tlw: 6, rlw: 7, br: 22 });
    const u1 = ease(t, cC + 0.3, cC + 1.3), u2 = ease(t, tC, tC + 1.2), u3 = ease(t, tC + 1.6, tC + 2.8);
    const capR = mix(mix(17.5, 15, u2), 12, u3), yC = Y(v, SER[i] + capR - 7.5);
    if (u1 > 0) { H3.line(ctx, [[f.x0, yC], [mix(f.x0, f.x1, u1), yC]], C.muted, 6, { dash: [18, 12], cap: 'butt' }); H2.text(ctx, 'rate cap', f.x1, 178, 'label', { align: 'right', color: C.muted, alpha: u1 }); }
    const extra = mix(mix(W0, W15, u2), W12, u3) * S;
    coins(ctx, 1500, 860, 330, C.muted, 1);
    const top = coins(ctx, 1700, 860, 330, C.muted, 1);
    coins(ctx, 1700, top, extra, C.costlier, 1);
    H3.line(ctx, [[1446, 900], [1554, 900]], C.muted, 6, { cap: 'butt' }); H3.diamond(ctx, 1700, 902, 18, C.ink, 1);
    H2.text(ctx, 'Starting ' + CL('worst_start'), 96, 140, 'caption');
    H2.badge(ctx, 1);
  }
  return { draw(ctx, t) { shots(ctx, t, [[0, (c, t) => { K6.draw(c, k6(t)); worstLabel(c, t); }], [cC, (c, t) => { cap(c, t); worstLabel(c, t); }]]); } };
}
