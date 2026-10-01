// S10 · Other offers, and the answer. KEY-7 continues in the K7 r2 layout (lib.k7At = k7.js code with the gap given):
// S10.1 the variable bar JUMPS (K2-style flip, no sweep) to 1, 0, -1 point; both red layers jump up; ONE figure per step,
// the overall share, held >= 3 s with both columns on screen (owner C4; per-half figures + worst go to the description). S10.2: jump BACK to 3 points (the beat ends on the
// widest gap), ring + 'April 1977' (gap_worst_start_all) on the left red layer; S10.3: the left red that never clears pulses,
// '10.5%' (min_gap_early). S10.4: KEY-1 final (the question). S10.5: K7 final, pulsing. S10.6: K7 2 -> 3 points. S10.7: ridge.
import { H2, C, CL, ease, inout, mix, warp, shots } from './film.js';
import * as K1 from '../../design/c3/final/src/k1.js';
import * as K7 from '../../design/c3/final/src/k7.js';
import { ridgeToday, k7At, overall } from './lib.js';
export function build({ T }) {
  const tQ = T.a('q'), t2 = T.a('two'), tL = T.a('late'), tT = T.a('today');
  const J = [[T.a('j1'), 1, 'spread1_share', ['gap10_early', 'gap10_late', 'gap10_worst']], [T.a('j0'), 0, 'spread0_share', ['gap00_early', 'gap00_late', 'gap00_worst']],
    [T.a('jm'), -1, 'spreadm1_share', ['gapm10_early', 'gapm10_late', 'gapm10_worst']], [T.a('back'), 3, null, null]];
  const tA = T.a('april'), tN = T.a('never');
  const k7 = warp([[5.5, tL + 0.05], [5.8, T.a('enough')], [7.6, T.a('early')], [8.0, T.a('notEnough')], [10, T.a('notEnough') + 2.0]]);
  const pulse = (t) => 0.5 - 0.5 * Math.cos(2 * Math.PI * t / 2.2);
  function steps(ctx, t) {
    let si = -1; for (let i = 0; i < J.length; i++) if (t >= J[i][0]) si = i;
    const gOf = (i) => (i < 0 ? 3 : J[i][1]);
    let sx = 1, shown = si;
    for (let i = 0; i < J.length; i++) { const d = t - J[i][0]; if (d > -0.18 && d < 0.18) { sx = Math.max(0.02, Math.abs(d) / 0.18); shown = d < 0 ? i - 1 : i; } }
    const gc = si < 0 ? 3 : mix(gOf(si - 1), gOf(si), ease(t, J[si][0], J[si][0] + 0.3));
    const back = t >= J[3][0];
    k7At(ctx, { g: gOf(shown), gc, sx, l105: si < 0 ? 1 - ease(t, J[0][0] - 0.3, J[0][0]) : 0, pulse: back ? pulse(t) : 0,
      ring: ['early', back ? ease(t, tN, tN + 0.4) * (0.55 + 0.45 * pulse(t)) : 0] });
    for (let i = 0; i < 3; i++) {
      const a0 = J[i][0], a1 = J[i + 1][0], mid = (a0 + a1) / 2;
      overall(ctx, J[i][2], inout(t, a0 + 0.2, a0 + 0.45, a1 - 0.3, a1 - 0.1));   // owner C4: one figure per step, held >= 3 s
    }
    if (back) {   // the April 1977 marker on the left red layer (worst start at every gap), then the share that never clears
      const am = ease(t, tA, tA + 0.4), yR = 950 - 520 * 0.105;
      H2.srect(ctx, 735, yR - 6, 50, 950 - yR + 6, C.ink, 5, am * (0.55 + 0.45 * pulse(t + 1.1)));
      H2.text(ctx, CL('gap_worst_start_all'), 660, 945, 'label', { align: 'right', alpha: inout(t, tA, tA + 0.4, tN - 0.3, tN) });
      H2.text(ctx, CL('min_gap_early'), 690 + 170, yR - 54, 'number', { align: 'center', alpha: ease(t, tN + 0.2, tN + 0.6) });
    }
  }
  return { draw(ctx, t) { shots(ctx, t, [[0, steps], [tQ, (c) => K1.draw(c, 8)], [t2, (c, t) => k7At(c, { g: 3, l105: 1, pulse: pulse(t) })],
    [tL, (c, t) => K7.draw(c, k7(t))], [tT, (c, t) => ridgeToday(c, ease(t, tT, tT + 0.5))]]); } };
}
