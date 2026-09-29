// S07 · The bill. Kết hợp: H1 the letter's last line lights; a paper ream ($5,124) grows beside the lifted $221 slab,
// SAME dollar scale -> H3 a scale of 2025 refinance bills: the $5,124 dot slides in and stops at the median.
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, srect, dot, ease, easeOut, back, mix , measure } from './engine.js';
import { kitchen, letter, paymentStack, ream, PL } from './common.js';
export const uses3d = true;

export function build({ scene, camera, renderer, T }) {
  const tLa = T.a('last'), tRm = T.a('ream'), tCa = T.a('cash'), tRe = T.a('real'), tMd = T.a('median'), tSz = T.a('size'), tY = T.a('you');
  kitchen(scene, renderer, { w: 20, d: 9 });
  const Lt = letter(scene, { rows: [{ label: 'Your rate now', value: CL('r_old') }, { label: 'New rate', value: CL('r_today') }, { label: 'Loan costs', value: CL('cost_median') }] });
  const LP = new THREE.Vector3(-2.6, 0.02, 0.6); Lt.mesh.position.copy(LP); Lt.mesh.rotation.y = 0.08;
  const M = DATA.median;
  const st = paymentStack(scene, { total: M.oldPayment, slab: M.sav, x: -0.7, z: 0.1, height: 1.2 });
  st.set(1, 0.6, 0, 0.5);
  const R = ream(scene, { dollars: M.cost, K: st.K, FW: 1.5, FD: 1.0, label: CL('cost_median'), big: 150 });
  const RX = 1.0;
  function update(t) {
    Lt.set([0, 0, ease(t, tLa, tLa + 0.5)]);
    const p = ease(t, tRm - 0.6, tRm + 0.8);
    camera.position.set(mix(LP.x + 1.1, 0.7, p), mix(3.8, 3.4, p), mix(LP.z + 2.5, 10.2, p));
    camera.lookAt(mix(LP.x + 1.0, 0.6, p), mix(0, 1.5, p), mix(LP.z + 0.3, 0, p));
    st.base.visible = st.slab.visible = t > tRm - 0.6;
    const g = easeOut(t, tRm, tRm + 1.2); R.visible = t > tRm; R.scale.y = Math.max(0.001, g); R.position.set(RX, R.userData.h * g / 2, 0.1);
  }
  function room(ctx, t, P) {
    const aB = easeOut(t, tLa + 0.3, tLa + 0.7) * (1 - ease(t, tRm - 0.6, tRm - 0.2));
    text(ctx, 'the last line', 1200, 640, 'label', { alpha: aB, plate: PL });
    const s = P(new THREE.Vector3(st.x, st.slabY(1, 0.5) + st.hSlab / 2, st.z));
    const aS = easeOut(t, tRm, tRm + 0.4);
    text(ctx, CL('sav_median') + ' a month', s.x, s.y - 30, 'label', { align: 'center', color: '#8FE0B5', alpha: aS, shadow: true });
    const r = P(new THREE.Vector3(RX + 0.75, R.userData.h * 0.8, 0.1));
    text(ctx, 'loan costs ' + CL('cost_median'), Math.min(r.x + 30, 1824 - measure(ctx, 'loan costs ' + CL('cost_median'), 'number')), r.y, 'number', { alpha: easeOut(t, tRm + 0.9, tRm + 1.3), shadow: true });
    text(ctx, 'paid in cash at closing', r.x + 30, r.y + 64, 'label', { alpha: easeOut(t, tCa, tCa + 0.4), shadow: true });
    text(ctx, 'one scale for both', r.x + 30, r.y + 124, 'note', { color: C.muted, alpha: easeOut(t, tRm + 1.3, tRm + 1.7), shadow: true });
    chrome(ctx, { illus: aS, source: 'Nora is illustrative. Dollars of the day = not adjusted for inflation.', plate: true });
  }
  // H3: one scale of 2025 refinance bills (no tick numbers: only the claimed median is printed here)
  const B = DATA.bills, X0 = 260, X1 = 1660, V0 = 1500, V1 = 11500, xOf = (v) => X0 + (v - V0) / (V1 - V0) * (X1 - X0), Y = 600;
  function scale(ctx, t) {
    text(ctx, 'What refinancing cost in ' + CL('y2025'), 96, 128, 'head');
    text(ctx, 'loan costs of ' + CL('n31_approx') + ' refinances', 96, 190, 'label', { color: C.muted, alpha: easeOut(t, tMd, tMd + 0.4) });
    const a0 = easeOut(t, tRe, tRe + 0.4);
    line(ctx, [[X0, Y], [X1, Y]], C.grid, 6, { alpha: a0 });
    text(ctx, 'smaller bills', X0, Y + 70, 'note', { color: C.muted, alpha: a0 });
    text(ctx, 'larger bills', X1, Y + 70, 'note', { align: 'right', color: C.muted, alpha: a0 });
    const aB = easeOut(t, tRe + 0.4, tRe + 1.2);
    rect(ctx, xOf(B.p25), Y - 70, (xOf(B.p75) - xOf(B.p25)) * aB, 140, C.muted, 0.18);
    text(ctx, 'the middle half of bills', (xOf(B.p25) + xOf(B.p75)) / 2, Y - 100, 'note', { align: 'center', color: C.muted, alpha: aB });
    const sl = back(t, tMd, tMd + 1.4), xd = mix(X0, xOf(B.p50), sl), aD = easeOut(t, tMd, tMd + 0.2);
    dot(ctx, xd, Y, 26, C.warn, aD);
    line(ctx, [[xOf(B.p50), Y - 70], [xOf(B.p50), Y + 70]], C.warn, 4, { alpha: easeOut(t, tMd + 1.2, tMd + 1.5) });
    text(ctx, CL('cost_median'), xOf(B.p50), Y + 170, 'number', { align: 'center', alpha: easeOut(t, tMd + 1.2, tMd + 1.5) });
    text(ctx, 'the median bill: half pay less, half pay more', xOf(B.p50), Y + 236, 'label', { align: 'center', alpha: easeOut(t, tMd + 1.4, tMd + 1.8) });
    text(ctx, "Nora's loan size is the median too: " + CL('loan_median'), W / 2, 960, 'label', { align: 'center', color: C.positive, alpha: easeOut(t, tSz, tSz + 0.4) });
    // a letter like this: an outline letter slides in
    const aY = easeOut(t, tY, tY + 0.6), lx = mix(1640, 1500, back(t, tY, tY + 1.0));
    if (aY > 0) { srect(ctx, lx, 250, 170, 220, C.ink, 4, aY, [10, 8]); text(ctx, 'your letter?', lx + 85, 520, 'label', { align: 'center', alpha: aY }); }
    chrome(ctx, { source: 'HMDA ' + CL('y2025') + ' (US home-loan records), refinances: total loan costs.' });
  }
  return {
    mode: (t) => (t >= tRe ? '2d' : '3d'), update,
    overlay: (ctx, t, P, m) => (m === '3d' ? room(ctx, t, P) : scale(ctx, t)),
    stripTimes: [tLa + 1.0, tRm + 1.6, tCa + 1.2, tMd + 0.6, tSz + 1.0, T.dur - 0.2],
  };
}
