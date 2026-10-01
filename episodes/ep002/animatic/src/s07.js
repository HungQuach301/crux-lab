// S07 · Two kinds of history. Only H3 objects: the ridge with its two halves (dashed split at 1981), 10-year frames with
// Leah's bead, the jar (h3 K4 jar, one $ scale here: $16,000 = full; the costlier block under it uses the SAME scale), the
// 753-cell strip, the ring. Numbers: 16.3% (tb_peak), August 1981 (best_start), −$15,295 (best_diff), 28.4% (share_early).
import { H2, H3, C, CL, ease, inout, mix, clamp } from './film.js';
import { FULL, X, Y, ridge, split, years, frame, cells, ring, jar, cushionOf, sweepAt, SER, NM, SPLIT, WORST, BEST, JAR_MAX } from './lib.js';
export function build({ T }) {
  const a = Object.fromEntries(['ridge', 'left', 'peak', 'right', 'both', 'rideL', 'rideR', 'best', 'bestD', 'cells', 'worst', 'share'].map((k) => [k, T.a(k)]));
  const v = FULL, IL = 267, IR = 562;                       // April 1976 (the K4 replay) and November 2000 (a falling stretch)
  const pk = SER.indexOf(Math.max(...SER)), g15 = sweepAt(1.5).bits;
  const JT = 630, JB = 830, JW = 150, KJ = (JB - JT - 12) / JAR_MAX;
  function jarAt(ctx, i, k, al) {
    const cx = (X(v, i) + X(v, i + 120)) / 2, c = k < 0 ? 0 : cushionOf(i)[Math.min(119, Math.floor(k))];
    jar(ctx, cx - JW / 2, JT, JB, JW, Math.max(0, c), al);
    if (c < 0) H2.negArea(ctx, cx - JW / 2, JB + 16, JW, -c * KJ, al, 22);
    return cx;
  }
  return {
    draw(ctx, t) {
      const aR = ease(t, a.ridge, a.ridge + 0.6);
      const dimL = inout(t, a.right, a.right + 0.4, a.both, a.both + 0.4), dimR = inout(t, a.left, a.left + 0.4, a.both, a.both + 0.4) * (1 - ease(t, a.right, a.right + 0.4)) + 0;
      ridge(ctx, v, { to: SPLIT, alpha: aR * (1 - 0.7 * dimL) });
      ridge(ctx, v, { from: SPLIT, alpha: aR * (1 - 0.7 * dimR) });
      split(ctx, v, v.Yt - 40, 640, aR);
      years(ctx, v, 1010, { alpha: aR });
      // the summit
      const pa = inout(t, a.peak, a.peak + 0.4, a.both - 0.6, a.both - 0.2);
      if (pa > 0) { H3.srect(ctx, X(v, pk) - 14, Y(v, SER[pk]) - 14, 28, 28, C.ink, 4, pa); H2.text(ctx, CL('tb_peak'), X(v, pk) + 40, Y(v, SER[pk]) + 30, 'number', { alpha: pa }); }
      // two identical loans, one per half
      const fa = ease(t, a.both, a.both + 0.5), fL = fa * (1 - ease(t, a.best, a.best + 0.5)), cellA = ease(t, a.cells, a.cells + 0.6);
      const rideL = 120 * ease(t, a.rideL, a.rideL + 3.5), rideR = 120 * ease(t, a.rideR, a.rideR + 3.5);
      const iR = t < a.best ? IR : BEST, mv = ease(t, a.best, a.best + 0.6);
      frame(ctx, v, IL, { ride: rideL, alpha: fL });
      const iRf = Math.round(mix(IR, BEST, mv));
      frame(ctx, v, iRf, { ride: mv > 0 ? null : rideR, alpha: fa * (1 - ease(t, a.worst, a.worst + 0.4)) });
      frame(ctx, v, WORST, { ride: null, alpha: ease(t, a.worst, a.worst + 0.4) });
      const ja = 1 - cellA;
      if (t < a.best) { jarAt(ctx, IL, t < a.rideL ? -1 : rideL, fL * ja); jarAt(ctx, IR, t < a.rideR ? -1 : rideR, fa * ja); }
      else { jarAt(ctx, IL, rideL, fL * ja); const cx = jarAt(ctx, iRf, mv < 1 ? 0 : 119, fa * ja);
        H2.text(ctx, CL('best_diff'), cx + JW / 2 + 30, JT + 120, 'number', { alpha: inout(t, a.bestD, a.bestD + 0.4, a.cells - 0.3, a.cells) }); }
      H2.text(ctx, CL('best_start'), 96, 140, 'caption', { alpha: inout(t, a.best, a.best + 0.4, a.bestD - 0.3, a.bestD) });
      // the 753 starts, coloured by result at Leah's 1.5 points; rings: best, then worst
      if (cellA > 0) {
        cells(ctx, v, (i) => ({ c: g15[i] === '1' ? C.costlier : C.grid, a: cellA }));
        ring(ctx, v, BEST, cellA * (1 - ease(t, a.worst, a.worst + 0.3)));
        ring(ctx, v, WORST, ease(t, a.worst, a.worst + 0.3));
        H2.text(ctx, CL('worst_start'), 96, 140, 'caption', { alpha: inout(t, a.worst, a.worst + 0.4, a.share - 0.3, a.share) });
        H2.text(ctx, CL('share_early'), (X(v, 0) + X(v, SPLIT)) / 2, 935, 'number', { align: 'center', alpha: ease(t, a.share, a.share + 0.4) });
      }
      H2.badge(ctx, aR);
    },
  };
}
