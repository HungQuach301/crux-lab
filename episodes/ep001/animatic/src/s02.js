// S02 · The letter, and the promise. H1 (signed SF2): the letter lands, its bill line lights, the camera pulls back to
// three model houses (volume = loan) and the outline house "your loan?" (the viewer's own loan, no number).
import { THREE, C, W, H, DATA, CL, text, chrome, ease, easeOut, back, mix, mark, house, outlineHouse } from './engine.js';
import { kitchen, letter, PL } from './common.js';
export const uses3d = true;

export function build({ scene, camera, renderer, T }) {
  const tL = T.a('letter'), tR = T.a('refi'), tF = T.a('fees'), tP = T.a('pull'), tP1 = T.a('promise1'), tY = T.a('yours'), tS = T.a('smaller');
  kitchen(scene, renderer);
  const Lt = letter(scene, { rows: [{ label: 'Your rate now', value: CL('r_old') }, { label: 'New rate', value: CL('r_today') }, { label: 'Loan costs', value: CL('cost_median') }] });
  const LP = new THREE.Vector3(-1.7, 0.02, 0.25);
  const s = (loan) => Math.cbrt(loan / DATA.small.loan);
  const base = { w: 1.05, d: 0.9, h: 0.62, roof: 0.45 };
  const mk = (k, wall, roof) => house({ w: base.w * k, d: base.d * k, h: base.h * k, roof: base.roof * k, wall, roofCol: roof, lit: 0.4 });
  const Hs = [
    { g: mk(s(DATA.small.loan), '#CDBF9F', '#4A4036'), x: 0.45, t0: tP + 0.6 },
    { g: mk(s(DATA.median.loan), '#C9BBA4', '#3B3F48'), x: 2.0, t0: tP + 1.0 },
    { g: mk(s(DATA.large.loan), '#B9C3CC', '#3A404C'), x: 3.95, t0: tP + 1.4 },
  ];
  const HZ = -1.9;
  for (const h of Hs) { h.g.position.set(h.x, 0, HZ); h.g.traverse((o) => { if (o.isMesh) o.castShadow = o.receiveShadow = true; }); scene.add(h.g); }
  const ks = s(DATA.median.loan);
  const out = outlineHouse({ w: base.w * ks, d: base.d * ks, h: base.h * ks, roof: base.roof * ks, color: '#F2F4F7' });
  out.position.set(5.9, 0, HZ); scene.add(out);
  function update(t) {
    const land = easeOut(t, tL, tL + 1.1);
    Lt.mesh.position.set(LP.x + (1 - land) * 5, LP.y + (1 - land) * 0.3, LP.z); Lt.mesh.rotation.y = 0.08 + (1 - land) * 0.5;
    Lt.set([0, ease(t, tR, tR + 0.5) * (1 - ease(t, tF - 0.3, tF)), ease(t, tF, tF + 0.6)]);
    const p = ease(t, tP, tP + 2.8);
    const push = ease(t, 0, tP) * 0.25;
    camera.position.set(mix(LP.x + 1.3, 1.7, p), mix(4.4 - push, 3.6, p), mix(LP.z + 2.9 - push, 8.6, p));
    camera.lookAt(mix(LP.x + 1.15, 2.1, p), mix(0, 1.25, p), mix(LP.z - 0.15, -0.9, p));
    for (const h of Hs) { const u = back(t, h.t0, h.t0 + 0.6); h.g.scale.set(1, Math.max(0.001, u), 1); h.g.visible = t > h.t0; }
    Hs[0].g.userData.winMat.emissiveIntensity = 0.4 + 2.2 * ease(t, tS, tS + 0.5);
    Hs[0].g.position.y = 0.25 * Math.sin(Math.PI * ease(t, tS, tS + 1.2));
    out.userData.mat.opacity = easeOut(t, tY, tY + 0.8); out.visible = t > tY;
    out.position.x = mix(7.0, 5.9, easeOut(t, tY, tY + 1.0));
  }
  function overlay(ctx, t, P) {
    const aB = easeOut(t, tF + 0.2, tF + 0.6) * (1 - ease(t, tP, tP + 0.4));
    text(ctx, 'Loan costs:', 1180, 560, 'caption', { alpha: aB, plate: PL });
    text(ctx, CL('cost_median'), 1180, 680, 'hero', { alpha: aB, color: C.warn, plate: PL });
    text(ctx, 'the fees for the new loan', 1180, 770, 'label', { alpha: aB, plate: PL });
    const aR = easeOut(t, tR, tR + 0.4) * (1 - ease(t, tF - 0.3, tF));
    text(ctx, 'a new loan at a lower rate', 1180, 600, 'label', { alpha: aR, plate: PL });
    text(ctx, CL('r_old') + ' → ' + CL('r_today'), 1180, 700, 'number', { alpha: aR, plate: PL });
    const lr = P(new THREE.Vector3(LP.x + Lt.LW / 2, 0.02, LP.z + Lt.LH * 0.25));
    const aN = easeOut(t, tP + 1.6, tP + 2.0);
    text(ctx, 'fees ' + CL('cost_median'), lr.x + 30, lr.y + 20, 'label', { alpha: aN, shadow: true });
    const nh = P(new THREE.Vector3(Hs[1].x, 0, HZ + base.d * ks / 2 + 0.2));
    mark(ctx, 'nora', nh.x - 80, nh.y + 44, 16, aN);
    text(ctx, 'Nora', nh.x - 55, nh.y + 60, 'label', { alpha: aN, shadow: true });
    const sh = P(new THREE.Vector3(Hs[0].x, 0, HZ + 0.6)), lh = P(new THREE.Vector3(Hs[2].x, 0, HZ + 1.0));
    text(ctx, 'smaller loan', sh.x, sh.y + 60, 'note', { align: 'center', color: t > tS ? C.warn : C.muted, alpha: aN, shadow: true });
    text(ctx, 'larger loan', lh.x, lh.y + 60, 'note', { align: 'center', color: C.muted, alpha: aN, shadow: true });
    const ob = P(new THREE.Vector3(out.position.x, 0, HZ + 1.0));
    text(ctx, 'your loan?', ob.x, ob.y + 60, 'label', { align: 'center', alpha: easeOut(t, tY + 0.5, tY + 0.9), shadow: true });
    text(ctx, 'How big a rate cut makes that worth it for Nora —', W / 2, 200, 'caption', { align: 'center', alpha: easeOut(t, tP1, tP1 + 0.4), plate: 'rgba(14,17,22,0.72)', sent: true });
    text(ctx, 'and where would your own loan fall?', W / 2, 280, 'caption', { align: 'center', alpha: easeOut(t, tY, tY + 0.4), plate: 'rgba(14,17,22,0.72)', sent: true });
    text(ctx, 'And why would a smaller mortgage need a bigger cut?', W / 2, 360, 'caption', { align: 'center', alpha: easeOut(t, tS - 0.6, tS - 0.2), plate: 'rgba(14,17,22,0.72)', sent: true });
    chrome(ctx, { illus: aN, source: 'Fees: median ' + CL('y2025') + ' refinance bill (HMDA, US home-loan records). Nora: illustrative.', srcAlpha: easeOut(t, tF, tF + 0.4), plate: true });
  }
  return { update, overlay, stripTimes: [tL + 1.2, tR + 0.8, tF + 1.0, tP + 3.0, tY + 1.4, T.dur - 0.2] };
}
