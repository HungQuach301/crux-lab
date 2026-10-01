// S04 · The promise. S04.1-S04.2 = KEY-5: signed K5 (h3/scenes.js) time-warped; 'US only' written as said (brief task 4).
// S04.3: the K6 coin piles (interest paid), fixed vs variable, the costlier block on top (heights from claims fixed_int and
// worst_diff, no number printed). S04.4: the signed K2 picture runs its four start points (3, 1.5, 0, above). S04.5: one blank
// offer card (K1/K2 card). S04.6: the ridge ends at today, empty space to its right + 'History, not a forecast' (task 4).
import { H2, H3, C, CL, ease, mix, warp, around, shots } from './film.js';
import { K5 } from '../../design/c3/final/src/h3/scenes.js';
import * as K2 from '../../design/c3/final/src/k2.js';
import { card, coins, ridgeToday } from './lib.js';
export function build({ T }) {
  const k5 = warp([[0, 0.05], [1.7, T.a('k5ride')], [2.9, T.a('k5tb')], [8.7, T.a('k5only')], [10, T.a('k5only') + 1.3]]);
  const tOnly = T.a('k5only'), cC = T.a('cutCoins'), tP = T.a('piles'), tW = T.a('worst'), c2 = T.a('cutK2'), cK = T.a('cutCard'), cR = T.a('cutRidge');
  const k2 = warp([[0, c2 + 0.05], [0.6, T.a('k2a')], [0.8, T.a('k2a') + 0.2], ...around(2.0, T.a('k2b')), ...around(3.6, T.a('k2c')), ...around(5.2, T.a('k2d')), [8.0, T.a('k2d') + 2.8]]);
  const FI = 26005.46, WD = 11218.65, SC = 380 / FI; // = claims fixed_int, worst_diff (values, not printed)
  function replay(ctx, t) { K5.draw(ctx, k5(t)); H2.text(ctx, "Leah's loan, replayed from every start month", 96, 1000, 'caption', { alpha: ease(t, 0.4, 0.9) }); H2.text(ctx, 'US only', 1824, 1000, 'label', { align: 'right', alpha: ease(t, tOnly, tOnly + 0.4) }); }
  function piles(ctx, t) {
    const g = ease(t, tP, tP + 1.0), r = ease(t, tW, tW + 1.0), base = 840;
    coins(ctx, 760, base, 380 * g, C.muted, ease(t, tP, tP + 0.2), 200, 20);
    const top = coins(ctx, 1160, base, 380 * g, C.muted, ease(t, tP, tP + 0.2), 200, 20);
    coins(ctx, 1160, top, WD * SC * r, C.costlier, 1, 200, 20);
    H2.line(ctx, [[600, base + 20], [1320, base + 20]], C.muted, 6, { cap: 'butt', alpha: ease(t, tP, tP + 0.3) });
    H2.numWord(ctx, CL('fixed_rate'), 'fixed', 760, base + 100, 'label', { align: 'center', alpha: ease(t, tP, tP + 0.4) });
    H2.text(ctx, 'variable', 1160, base + 100, 'label', { align: 'center', color: C.muted, alpha: ease(t, tP, tP + 0.4) });
    H2.badge(ctx, 1);
  }
  function blank(ctx, t) { const u = ease(t, cK, cK + 1.2); card(ctx, 620, mix(330, 250, u), 1, u); }
  function today(ctx, t) { ridgeToday(ctx, ease(t, cR, cR + 0.5)); H2.text(ctx, 'History, not a forecast', 960, 940, 'caption', { align: 'center', alpha: ease(t, cR + 0.2, cR + 0.7) }); }
  return { draw(ctx, t) { shots(ctx, t, [[0, replay], [cC, piles], [c2, (c, t) => K2.draw(c, k2(t))], [cK, blank], [cR, today]]); } };
}
