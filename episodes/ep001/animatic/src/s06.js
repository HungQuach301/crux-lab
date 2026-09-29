// S06 · The offer. Kết hợp: H1 letter (new rate line lights) -> H3 one rate scale: 7.62 vs 7.03, the gap grows
// "0.59 point", a 1-point ruler set beside it (what "a point" means) -> H1 the payment stack: $221 lifts off.
import { THREE, C, W, H, DATA, CL, text, chrome, line, rect, dot, mark, ease, easeOut, mix } from './engine.js';
import { kitchen, letter, paymentStack, PL } from './common.js';
export const uses3d = true;

export function build({ scene, camera, renderer, T }) {
  const tL = T.a('letter'), tR = T.a('rate'), tW = T.a('week'), tG = T.a('gap'), tHf = T.a('half'), tU = T.a('unit'), tP = T.a('pay'), tLf = T.a('lift');
  kitchen(scene, renderer);
  const Lt = letter(scene, { rows: [{ label: 'Your rate now', value: CL('r_old') }, { label: 'New rate', value: CL('r_today') }, { label: 'Loan costs', value: CL('cost_median') }] });
  const LP = new THREE.Vector3(-1.7, 0.02, 0.25);
  const M = DATA.median;
  const st = paymentStack(scene, { total: M.oldPayment, slab: M.sav, x: 1.4, z: 0.1 });
  function update(t) {
    const land = easeOut(t, tL, tL + 1.0);
    Lt.mesh.position.set(LP.x + (1 - land) * 5, LP.y, LP.z); Lt.mesh.rotation.y = 0.08 + (1 - land) * 0.5;
    Lt.set([0, ease(t, tR, tR + 0.5), 0]);
    if (t < tP) { camera.position.set(LP.x + 1.2, 3.9, LP.z + 2.7); camera.lookAt(LP.x + 1.1, 0, LP.z + 0.1); }
    else { const k = ease(t, tP, T.dur); camera.position.set(mix(0.3, 0.2, k), mix(2.9, 2.8, k), mix(8.6, 8.1, k)); camera.lookAt(0.1, 0.95, 0); }
    st.set(easeOut(t, tLf, tLf + 0.8), easeOut(t, tLf, tLf + 0.6)); st.base.visible = st.slab.visible = t >= tP;
  }
  function room(ctx, t, P) {
    if (t < tP) {
      const aR = easeOut(t, tR, tR + 0.4);
      text(ctx, 'New rate: ' + CL('r_today'), 1180, 560, 'number', { alpha: aR, plate: PL });
      text(ctx, 'national average,', 1180, 650, 'label', { alpha: easeOut(t, tW, tW + 0.4), plate: PL });
      text(ctx, 'week ending ' + CL('anchor_date'), 1180, 716, 'label', { alpha: easeOut(t, tW, tW + 0.4), plate: PL });
      chrome(ctx, { source: 'Assumes the offer matches the national average (Freddie Mac).', plate: true });
      return;
    }
    const a1 = easeOut(t, tP, tP + 0.3);
    const bt = P(new THREE.Vector3(st.x, st.hBase + st.hSlab, st.z + st.SD / 2));
    text(ctx, "Nora's monthly payment", bt.x, 214, 'label', { align: 'center', alpha: a1 * (1 - ease(t, tLf, tLf + 0.3)), shadow: true });
    const sl = P(new THREE.Vector3(st.x - st.SW / 2, st.slabY(easeOut(t, tLf, tLf + 0.8)), st.z + st.SD / 2)), lx = sl.x - 40;
    const aS = easeOut(t, tLf + 0.3, tLf + 0.7);
    text(ctx, CL('sav_median') + ' a month less', lx, sl.y + 10, 'number', { align: 'right', color: C.positive, alpha: aS, shadow: true });
    text(ctx, 'at ' + CL('r_today') + ' instead of ' + CL('r_old'), lx, sl.y + 70, 'label', { align: 'right', alpha: aS, shadow: true });
    chrome(ctx, { illus: 1, source: 'Nora is an illustrative borrower. Dollars of the day.', plate: true });
  }
  // H3: one rate scale, 400 px per percentage point
  const Y0 = 900, R0 = 6.4, PX = 400, yOf = (r) => Y0 - (r - R0) * PX;
  function scale(ctx, t) {
    text(ctx, 'The offer, on one rate scale', 96, 128, 'head');
    text(ctx, 'point = one percentage point of the rate', 96, 190, 'note', { color: C.muted, alpha: easeOut(t, tU, tU + 0.4) });
    const XA = 760, XB = 1160, a0 = easeOut(t, tG, tG + 0.4);
    line(ctx, [[XA - 120, yOf(DATA.f1.rOld)], [XB + 120, yOf(DATA.f1.rOld)]], C.ink, 6, { alpha: a0 });
    dot(ctx, XA - 150, yOf(DATA.f1.rOld), 15, C.positive, a0);
    text(ctx, 'Nora now ' + CL('r_old'), XA - 180, yOf(DATA.f1.rOld) + 14, 'label', { align: 'right', alpha: a0 });
    const aO = easeOut(t, tG + 0.4, tG + 0.8);
    line(ctx, [[XA - 120, yOf(DATA.f1.rOld)], [XB + 120, yOf(DATA.f1.rOld)]].map(([x, y]) => [x, mix(y, yOf(7.03), aO)]), C.accent, 6, { alpha: aO });
    text(ctx, 'offer ' + CL('r_today'), XA - 180, yOf(7.03) + 14, 'label', { align: 'right', color: C.accent, alpha: aO });
    const g = easeOut(t, tG + 0.8, tG + 1.6);
    rect(ctx, XA + 120, yOf(DATA.f1.rOld), 200, (yOf(7.03) - yOf(DATA.f1.rOld)) * g, C.positive, 0.8);
    text(ctx, CL('cut_today') + ' point', XA + 220, yOf(7.03) + 90, 'number', { align: 'center', alpha: easeOut(t, tG + 1.4, tG + 1.8) });
    text(ctx, CL('cut_today_words'), XA + 220, yOf(7.03) + 150, 'label', { align: 'center', alpha: easeOut(t, tHf, tHf + 0.4) });
    // the 1-point ruler beside the gap
    const u = easeOut(t, tU, tU + 1.0), xu = 1440;
    rect(ctx, xu, yOf(DATA.f1.rOld), 60, PX * u, C.muted, 0.5);
    line(ctx, [[xu - 20, yOf(DATA.f1.rOld)], [xu + 80, yOf(DATA.f1.rOld)]], C.ink, 3, { alpha: u });
    line(ctx, [[xu - 20, yOf(DATA.f1.rOld) + PX * u], [xu + 80, yOf(DATA.f1.rOld) + PX * u]], C.ink, 3, { alpha: u });
    text(ctx, CL('s10') + ' point', xu + 110, yOf(DATA.f1.rOld) + PX / 2, 'number', { alpha: easeOut(t, tU + 0.8, tU + 1.2) });
    text(ctx, '= one percentage point', xu + 110, yOf(DATA.f1.rOld) + PX / 2 + 60, 'note', { color: C.ink, alpha: easeOut(t, tU + 0.8, tU + 1.2) });
    chrome(ctx, { source: 'Freddie Mac weekly survey, via FRED.' });
  }
  return {
    mode: (t) => (t >= tG && t < tP ? '2d' : '3d'), update,
    overlay: (ctx, t, P, m) => (m === '3d' ? room(ctx, t, P) : scale(ctx, t)),
    stripTimes: [tL + 1.0, tW + 1.2, tHf + 1.0, tU + 1.8, tLf + 1.2, T.dur - 0.2],
  };
}
