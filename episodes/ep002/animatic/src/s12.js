// S12 · Where an offer falls. S12.1: KEY-7 picture at Leah's 1.5 points. S12.2-S12.3: one blank offer card (K1/K2 card) with
// what the replay leaves out written around it (labels only: the system has no index/cap/hourglass/receipt/wallet objects;
// README). S12.4: KEY-7 final. S12.5: the ridge ends at today + 'History, not a forecast' (task 4).
import { H2, C, ease, mix, warp, shots } from './film.js';
import * as K7 from '../../design/c3/final/src/k7.js';
import { card, ridgeToday, k7At } from './lib.js';
export function build({ T }) {
  const a = Object.fromEntries(['blank', 'index', 'cap', 'grace', 'fees', 'budget', 'line', 'hist'].map((k) => [k, T.a(k)]));
  T.a('leah'); // S12.1 starts on the K7 layout at 1.5 points (slow pulse on the red layers)
  function blank(ctx, t) {
    const u = ease(t, a.blank, a.blank + 1.0); card(ctx, 620, mix(330, 300, u), 1, u);
    const L = (k, s, x, y, al) => H2.text(ctx, s, x, y, 'label', { align: al, color: C.muted, alpha: ease(t, a[k], a[k] + 0.4) });
    L('index', "the lender's real index", 960, 240, 'center');
    L('cap', 'no rate cap', 1350, 470, 'left');
    L('grace', 'repayment starts at once', 960, 870, 'center');
    L('fees', 'fees', 1350, 640, 'left');
    L('budget', 'your own budget', 570, 470, 'right');
  }
  function hist(ctx, t) { ridgeToday(ctx, ease(t, a.hist, a.hist + 0.5)); H2.text(ctx, 'History, not a forecast', 960, 940, 'caption', { align: 'center', alpha: ease(t, a.hist + 0.2, a.hist + 0.7) }); }
  return { draw(ctx, t) { shots(ctx, t, [[0, (c, t) => k7At(c, { g: 1.5, l15: 1, pulse: 0.5 - 0.5 * Math.cos(2 * Math.PI * t / 2.2) })], [a.blank, blank], [a.line, (c, t) => k7At(c, { g: 3, l105: 1, pulse: 0.5 - 0.5 * Math.cos(2 * Math.PI * t / 2.2) })], [a.hist, hist]]); } };
}
