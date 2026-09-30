// SF4 · A quarter point: "never" (S11). H3: x = months after refinancing (to the old loan's last payment), y = dollars.
// The fees are a flat line. Division stacks savings only: a straight line that crosses the fees at month 38.
// Counting what she still owes: savings minus the extra balance on the new loan. It rises, comes close, never touches
// the fees line, then falls away as the old loan would have been paid off: "never".
// Claims: s025 cost_median be_simple_025 be_bal_025 (never). Curve values from model/refi.py (data.js), not printed.
import { C, W, H, DATA, CL, text, chrome, line, rect, dot, ease, easeOut, mix, clamp } from './engine.js';

export const uses3d = false;
const DUR = 10.0;

export function build() {
  const Q = DATA.q025, NM = Q.months;
  const X0 = 200, X1 = 1500, YB = 820, YT = 300, VMAX = 6000;
  const xOf = (m) => X0 + (m / NM) * (X1 - X0);
  const yOf = (v) => YB - (v / VMAX) * (YB - YT);
  const clipY = (y) => Math.max(YT - 20, Math.min(YB + 40, y));
  const iPeak = Q.net.indexOf(Math.max(...Q.net));

  function overlay(ctx, t) {
    const a0 = easeOut(t, 0, 0.4);
    text(ctx, 'If her rate were cut only ' + CL('s025') + ' point', 96, 128, 'head', { alpha: a0 });
    text(ctx, 'point = one percentage point of the rate', 96, 196, 'note', { color: C.muted, alpha: a0 });
    // axis
    line(ctx, [[X0, YB], [X1, YB]], C.grid, 3);
    line(ctx, [[X1, YB], [X1, YB + 16]], C.grid, 3);
    text(ctx, 'months →', X1, YB + 64, 'note', { color: C.muted, align: 'right', alpha: a0 });
    text(ctx, 'not before the old', X1, 672, 'note', { color: C.ink, align: 'right', alpha: easeOut(t, 7.4, 7.9) });
    text(ctx, "loan's last payment", X1, 730, 'note', { color: C.ink, align: 'right', alpha: easeOut(t, 7.4, 7.9) });
    line(ctx, [[X1, YB - 24], [X1, YB + 16]], C.muted, 3, { alpha: easeOut(t, 7.2, 7.6) });
    // fees line
    const aF = easeOut(t, 0.2, 0.7), yF = yOf(Q.cost);
    line(ctx, [[X0, yF], [X0 + (X1 - X0) * aF, yF]], C.muted, 6);
    text(ctx, 'loan costs ' + CL('cost_median'), X1, yF + 66, 'label', { align: 'right', alpha: aF });
    // division: savings only (straight), draws to the top of the plot
    const mD = ease(t, 0.8, 2.6) * (VMAX / Q.sav);
    if (t > 0.8) line(ctx, [[xOf(0), yOf(0)], [xOf(mD), yOf(mD * Q.sav)]], C.ink, 6);
    const m38 = +CL('be_simple_025');
    const aX = easeOut(t, 2.0, 2.4);
    dot(ctx, xOf(m38), yF, 13, C.ink, aX);
    line(ctx, [[xOf(m38), yF + 16], [xOf(m38), YB]], C.ink, 2, { dash: [6, 8], alpha: aX });
    text(ctx, 'month ' + CL('be_simple_025'), xOf(m38), YB + 64, 'label', { align: 'center', alpha: aX });
    text(ctx, 'division: savings only', xOf(VMAX / Q.sav) + 20, YT - 4, 'note', { color: C.ink, alpha: easeOut(t, 2.4, 2.8) });
    // counting what she still owes: draws to the old loan's last payment, clipped at the axis
    const mC = ease(t, 3.0, 7.2) * NM;
    if (t > 3.0) {
      const pts = [];
      for (let m = 0; m <= Math.floor(mC); m++) { if (Q.net[m] < 0) { const f = Q.net[m - 1] / (Q.net[m - 1] - Q.net[m]); pts.push([xOf(m - 1 + f), YB]); break; } pts.push([xOf(m), yOf(Q.net[m])]); }
      if (pts.length > 1) line(ctx, pts, C.positive, 7);
      const h = pts[pts.length - 1]; dot(ctx, h[0], h[1], 10, C.positive);
    }
    const m0 = Q.net.findIndex((v) => v < 0), aZ = easeOut(t, 3.0 + 4.2 * (m0 / NM), 3.2 + 4.2 * (m0 / NM));
    if (aZ > 0) { const xz = xOf(m0); line(ctx, [[xz - 14, YB + 8], [xz, YB + 26], [xz + 14, YB + 8]], C.positive, 7, { alpha: aZ }); }
    const aC = easeOut(t, 3.6, 4.0);
    text(ctx, 'savings minus', 430, 690, 'label', { color: C.positive, alpha: aC });
    text(ctx, 'what she still owes', 430, 752, 'label', { color: C.positive, alpha: aC });
    // closest point: still short of the fees
    const aP = easeOut(t, 5.0, 5.4), xp = xOf(iPeak), yp = yOf(Q.net[iPeak]);
    line(ctx, [[xp, yp - 4], [xp, yF + 4]], C.negative, 5, { alpha: aP });
    text(ctx, 'closest: still short', xp + 20, yF - 24, 'note', { color: C.ink, alpha: aP });
    // never
    const aN = easeOut(t, 7.4, 7.9);
    text(ctx, CL('be_bal_025').replace(/^./, (c) => c.toUpperCase()), X1 - 10, 600, 'number', { align: 'right', color: C.negative, alpha: aN });
    text(ctx, 'Division: month ' + CL('be_simple_025') + '.  Counting what she owes: never.', W / 2, 972, 'label', { align: 'center', alpha: easeOut(t, 7.8, 8.2) });
    chrome(ctx, { illus: 1, source: 'Nora (illustrative). Fees paid in cash. Dollars of the day.' });
  }
  return { duration: DUR, update: () => {}, overlay, stripTimes: [0.6, 2.4, 4.2, 5.6, 7.4, 9.9], hardTime: 9.95 };
}
