// S12 · Where an offer falls. S12.1: KEY-7 picture at Leah's 1.5 points. S12.2-S12.3: one blank offer card (K1/K2 card) with
// what the replay leaves out written around it (labels only: the system has no index/cap/hourglass/receipt/wallet objects;
// README). S12.4: KEY-7 final. S12.5: the ridge ends at today + 'History, not a forecast' (task 4).
import { H2, C, ease, mix, warp, shots } from './film.js';
import * as K7 from '../../design/c3/final/src/k7.js';
import { card, ridgeToday } from './lib.js';
export function build({ T }) {
  const a = Object.fromEntries(['blank', 'index', 'cap', 'grace', 'fees', 'budget', 'line', 'hist'].map((k) => [k, T.a(k)]));
  const k7 = warp([[3.7, T.a('leah')], [4.0, T.a('leah') + 0.5]]); // label '1.5 points' fully in, held
  function blank(ctx, t) {
    const u = ease(t, a.blank, a.blank + 1.0); card(ctx, 620, mix(330, 300, u), 1, u);
    const L = (k, s, x, y, al) => H2.text(ctx, s, x, y, 'label', { align: al, color: C.muted, alpha: ease(t, a[k], a[k] + 0.4) });
    L('index', "the lender's real index", 960, 240, 'center');
    L('cap', 'a rate cap', 1350, 470, 'left');
    L('grace', 'a grace period', 570, 470, 'right');
    L('fees', 'fees', 1350, 640, 'left');
    L('budget', 'your own budget', 960, 870, 'center');
  }
  function hist(ctx, t) { ridgeToday(ctx, ease(t, a.hist, a.hist + 0.5)); H2.text(ctx, 'History, not a forecast', 960, 940, 'caption', { align: 'center', alpha: ease(t, a.hist + 0.2, a.hist + 0.7) }); }
  return { draw(ctx, t) { shots(ctx, t, [[0, (c, t) => K7.draw(c, k7(t))], [a.blank, blank], [a.line, (c) => K7.draw(c, 10)], [a.hist, hist]]); } };
}
