// S18 · Back to the letter: a line for each loan size (G-013). Kết hợp: H1 the letter returns (bill line lit) -> H3
// the three-mark ruler (signed SF6): three separate bars by loan size, no line between them; the outline house
// "your loan?" slides along the axis and stops between marks with no value; the 1-point rule of thumb slides across
// and matches none.
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, mark, measure, ease, easeOut, back, mix, withObj, CHAR, basisNote, BASIS, NEAR } from './engine.js';
import { kitchen, letter, houseIcon, PL } from './common.js';
export const uses3d = true;
export const basisCorner = [1808, 256]; // BASIS_MODE corner: label position (right-aligned baseline) here: the subtitle runs to x 1690 on the badge line

export function build({ scene, camera, renderer, T }) {
  const tL = T.a('letter'), tQ = T.a('q'), tSz = T.a('size'), tW = T.a('walt'), tN = T.a('nora'), tA = T.a('anj'), tY = T.a('you'), tAs = T.a('assume'), tO = T.a('one');
  kitchen(scene, renderer);
  const Lt = letter(scene, { rows: [{ label: 'Your rate now', value: CL('r_old') }, { label: 'New rate', value: CL('r_today') }, { label: 'Loan costs', value: CL('cost_median') }] });
  const LP = new THREE.Vector3(-1.7, 0.02, 0.25); Lt.mesh.position.copy(LP); Lt.mesh.rotation.y = 0.08;
  function update(t) {
    const land = easeOut(t, tL, tL + 0.9);
    Lt.mesh.position.set(LP.x + (1 - land) * 4, LP.y, LP.z);
    Lt.set([0, 0, ease(t, tL + 0.6, tL + 1.1)]);
    const k = ease(t, tL, tQ); camera.position.set(LP.x + 1.2, mix(4.2, 3.8, k), LP.z + mix(2.9, 2.6, k)); camera.lookAt(LP.x + 1.1, 0, LP.z + 0.1);
  }
  function room(ctx, t) {
    text(ctx, 'Back to the letter', 1180, 560, 'caption', { alpha: easeOut(t, tL, tL + 0.4), plate: PL, sent: true });
    chrome(ctx, { source: 'Fees: median ' + CL('y2025') + ' refinance bill (HMDA, US home-loan records).', plate: true });
  }
  // ---- H3 three-mark ruler (SF6) ----
  const LMIN = 50000, LMAX = 720000, X0 = 200, X1 = 1600, YB = 690, PX = 300;
  const xOf = (L) => X0 + (L - LMIN) / (LMAX - LMIN) * (X1 - X0);
  const who = [
    { k: 'walt', name: 'Walt', loan: DATA.small.loan, cut: DATA.cuts.small, lab: CL('cut36_small') + ' points', sub: 'more than a full point', loanL: CL('loan_small'), col: C.warn, t0: tW },
    { k: 'nora', name: 'Nora', loan: DATA.median.loan, cut: DATA.cuts.median, lab: CL('cut36_median') + ' point', sub: 'half a point', loanL: CL('loan_median'), col: C.positive, t0: tN },
    { k: 'anjali', name: 'Anjali', loan: DATA.large.loan, cut: DATA.cuts.large, lab: null, loanL: CL('loan_large'), col: C.negative, t0: tA },
  ];
  function ruler(ctx, t) {
    const a0 = easeOut(t, tQ, tQ + 0.4);
    text(ctx, 'Rate cut needed, by loan size', 96, 124, 'head', { alpha: a0 });
    text(ctx, 'to pay back the fees within ' + CL('y3') + ' years · point = percentage point of the rate', 96, 186, 'note', { color: C.muted, alpha: a0 });
    const aX = easeOut(t, tSz, tSz + 0.5);
    line(ctx, [[X0 - 40, YB], [X1 + 40, YB]], C.grid, 4, { alpha: aX });
    for (const w of who) {
      const x = xOf(w.loan), s = Math.sqrt(w.loan / DATA.median.loan) * 0.95;
      const aH = aX * easeOut(t, tSz + 0.2 + who.indexOf(w) * 0.25, tSz + 0.6 + who.indexOf(w) * 0.25);
      houseIcon(ctx, x, YB + 18 + 46 * s + 34 * s, s, '#C9BBA4', aH, false);
      text(ctx, w.loanL, x, YB + 164, 'label', { align: 'center', alpha: aH });
      const wn = measure(ctx, w.name, 'note');
      mark(ctx, w.k, x - wn / 2 - 20, YB + 202, 14, aH); text(ctx, w.name, x - wn / 2 + 2, YB + 216, 'note', { color: C.ink, alpha: aH });
      const g = easeOut(t, w.t0, w.t0 + 0.9), hb = w.cut * PX * g;
      withObj({ role: 'bar', chart: 's18-cut', value: w.cut * g, full: g >= 1, orient: 'v', char: CHAR[w.k], case: CHAR[w.k] }, () => rect(ctx, x - 75, YB - hb, 150, hb, w.col, 0.95));
      const aL = easeOut(t, w.t0 + 0.8, w.t0 + 1.1);
      if (w.k === 'anjali') { text(ctx, 'about a third', x, YB - hb - 76, 'label', { align: 'center', alpha: aL }); text(ctx, 'of a point', x, YB - hb - 24, 'label', { align: 'center', alpha: aL }); }
      else text(ctx, w.lab, x, YB - hb - 24, 'number', { align: 'center', alpha: aL });
    }
    // the viewer's loan: outline house slides along the axis, stops between marks, no value
    const ox = mix(X0 - 60, (xOf(DATA.median.loan) + xOf(DATA.large.loan)) / 2 + 10, back(t, tY, tY + 1.8));
    const aO = easeOut(t, tY, tY + 0.3);
    houseIcon(ctx, ox, YB + 18 + 80 * 0.95, 0.95, null, aO, true);
    text(ctx, 'your loan?', ox, YB + 216, 'label', { align: 'center', alpha: easeOut(t, tY + 1.2, tY + 1.6) });
    // assumptions (fixed footnote)
    const aA = easeOut(t, tAs, tAs + 0.5);
    text(ctx, 'Assumes: fees paid back within ' + CL('y3') + ' years · median ' + CL('y2025') + ' bills · ' + CL('oct2023') + ' rate', W / 2, 962, 'note', { align: 'center', color: C.ink, alpha: aA, plate: PL });
    if (!NEAR) text(ctx, 'fees paid in cash · illustrative borrowers · not advice', W / 2, 1016, 'note', { align: 'center', color: C.ink, alpha: aA, plate: PL });
    else { // C5 S09: line 2 = 'fees paid in cash · ' + BASIS + ' · illustrative borrowers · not advice'; the basis piece shows with the loan sizes
      const L2 = 'fees paid in cash · ', R2 = ' · illustrative borrowers · not advice', wl = measure(ctx, L2, 'note'), wa = measure(ctx, 'amounts in ' + BASIS, 'note'), wr = measure(ctx, R2, 'note');
      const x0 = Math.min(900, 1822 - wr - wa / 2) - wa / 2 - wl; // the basis piece centred at x 900: within 300 px of all three loan labels (Walt 336 · Nora 860 · Anjali 1466)
      text(ctx, L2, x0, 1016, 'note', { color: C.ink, alpha: aA });
      basisNote(ctx, x0 + wl, 1016, { s: 'amounts in ' + BASIS, color: C.ink, alpha: aX });
      text(ctx, R2, x0 + wl + wa, 1016, 'note', { color: C.ink, alpha: aA }); // no plates: the flat chart needs none and plates would cover the neighbour's glyphs
    }
    // the 1-point rule of thumb: slides across, matches none, fades
    const sl = ease(t, tO, tO + 1.6), fade = 1 - 0.7 * ease(t, tO + 2.2, tO + 2.8), y1 = YB - PX * 1;
    if (t > tO) line(ctx, [[X0 - 40, y1], [mix(X0 - 40, X1 + 40, sl), y1]], C.ink, 4, { dash: [16, 12], alpha: fade });
    text(ctx, CL('s10') + '-point rule of thumb: fits none', X1 + 40, y1 - 24, 'label', { align: 'right', color: C.ink, alpha: easeOut(t, tO + 1.4, tO + 1.8) });
    chrome(ctx, { illus: 1 });
  }
  return {
    mode: (t) => (t < tQ ? '3d' : '2d'), update,
    overlay: (ctx, t, P, m) => (m === '3d' ? room(ctx, t) : ruler(ctx, t)),
    stripTimes: [tL + 1.6, tW + 1.4, tA + 1.4, tY + 2.2, tAs + 1.4, T.dur - 0.2],
    hardTime: T.dur - 0.1,
  };
}
