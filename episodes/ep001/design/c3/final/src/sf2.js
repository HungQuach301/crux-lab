// SF2 · The letter, and the promise (S02). H1: Nora's kitchen table. A refinance letter slides in; its last line,
// "Loan costs $5,124", lights up. The camera pulls back: three model houses on the table (small, Nora's, large; volume
// = loan size, no numbers yet) and a fourth house drawn only as an outline, no number: the viewer's own loan.
// Claims: cost_median (the letter), r_old not shown. Loan sizes are NOT printed here (S14-S17 name them).
import { THREE, C, W, H, DATA, CL, text, chrome, ease, easeOut, back, mix, clamp, canvasTex, ptxt, mat, box, pm, woodTable, house, outlineHouse, mark } from './engine.js';

export const uses3d = true;
const DUR = 11.0;

export function build({ scene, camera, renderer }) {
  scene.background = new THREE.Color(C.bg);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', 0.6));
  const key = new THREE.SpotLight('#FFE2BC', 90, 26, 0.75, 0.55, 1.3); key.position.set(-1.5, 9, 4); key.target.position.set(0.8, 0, -0.6);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0005; scene.add(key, key.target);
  const rim = new THREE.DirectionalLight('#A9B6CF', 0.35); rim.position.set(5, 4, -4); scene.add(rim);
  woodTable(scene, 18, 9);

  // ---- the letter ----
  const LW = 2.2, LH = LW * 11 / 8.5;
  let lit = -1;
  const letterTex = canvasTex(1100, 1424, drawLetter(0));
  function drawLetter(k) {
    return (g, w, h) => {
      g.fillStyle = '#F7F4EC'; g.fillRect(0, 0, w, h);
      g.fillStyle = '#2E3440'; g.fillRect(0, 0, w, 190);
      ptxt(g, 'REFINANCE OFFER', 70, 128, { size: 92, weight: 700, color: '#FFFFFF' });
      ptxt(g, 'A new loan at a lower rate', 70, 300, { size: 62, weight: 600, color: '#20242C' });
      ptxt(g, 'pays off your current loan.', 70, 380, { size: 62, weight: 600, color: '#20242C' });
      g.fillStyle = '#CFC9BB'; for (let i = 0; i < 7; i++) g.fillRect(70, 470 + i * 70, 900 - (i % 3) * 170, 22);
      const y0 = 1000;
      if (k > 0) { g.fillStyle = `rgba(242,180,65,${0.55 * k})`; g.fillRect(40, y0 - 20, w - 80, 360); }
      g.strokeStyle = '#20242C'; g.lineWidth = 6; g.strokeRect(40, y0 - 20, w - 80, 360);
      ptxt(g, 'Loan costs', 80, y0 + 90, { size: 80, weight: 700, color: '#20242C' });
      ptxt(g, CL('cost_median'), w - 80, y0 + 290, { size: 170, weight: 700, color: '#20242C', align: 'right' });
    };
  }
  const letter = box(LW, 0.012, LH, [mat('#EDE8DC'), mat('#EDE8DC'), pm(letterTex), mat('#EDE8DC'), mat('#EDE8DC'), mat('#EDE8DC')]);
  scene.add(letter);
  const LP = new THREE.Vector3(-1.7, 0.02, 0.25);

  // ---- three model houses (volume = loan size) + the outline house ----
  const s = (loan) => Math.cbrt(loan / DATA.small.loan);
  const base = { w: 1.05, d: 0.9, h: 0.62, roof: 0.45 };
  const mk = (k, wall, roof) => house({ w: base.w * k, d: base.d * k, h: base.h * k, roof: base.roof * k, wall, roofCol: roof, lit: 1.4 });
  const Hs = [
    { g: mk(s(DATA.small.loan), '#CDBF9F', '#4A4036'), x: 0.45, t0: 4.6 },
    { g: mk(s(DATA.median.loan), '#C9BBA4', '#3B3F48'), x: 2.0, t0: 5.0 },
    { g: mk(s(DATA.large.loan), '#B9C3CC', '#3A404C'), x: 3.95, t0: 5.4 },
  ];
  const HZ = -1.9;
  for (const h of Hs) { h.g.position.set(h.x, 0, HZ); h.g.traverse((o) => { if (o.isMesh) o.castShadow = o.receiveShadow = true; }); scene.add(h.g); }
  const ks = s(DATA.median.loan);
  const out = outlineHouse({ w: base.w * ks, d: base.d * ks, h: base.h * ks, roof: base.roof * ks, color: '#F2F4F7' });
  out.position.set(5.9, 0, HZ); scene.add(out);

  function update(t) {
    // letter slides in from the right, lands
    const land = easeOut(t, 0.0, 1.1);
    letter.position.set(LP.x + (1 - land) * 5, LP.y + (1 - land) * 0.3, LP.z); letter.rotation.y = 0.08 + (1 - land) * 0.5;
    const k = ease(t, 1.8, 2.5); if (Math.abs(k - lit) > 0.02) { letterTex.userData.redraw(drawLetter(k)); lit = k; }
    // camera: close over the letter, then pull back to show the houses
    const p = ease(t, 3.2, 6.0);
    camera.position.set(mix(LP.x + 1.3, 1.7, p), mix(4.4, 3.6, p), mix(LP.z + 2.9, 8.6, p));
    camera.lookAt(mix(LP.x + 1.15, 2.1, p), mix(0, 1.25, p), mix(LP.z - 0.15, -0.9, p));
    for (const h of Hs) { const u = back(t, h.t0, h.t0 + 0.6); h.g.scale.set(1, Math.max(0.001, u), 1); h.g.visible = t > h.t0; }
    out.userData.mat.opacity = easeOut(t, 7.4, 8.2); out.visible = t > 7.4;
    out.position.x = mix(7.0, 5.9, easeOut(t, 7.4, 8.4));
  }

  function overlay(ctx, t, P) {
    const p = ease(t, 3.2, 6.0);
    // the bill line, flat and large, while the camera is on the letter
    const aB = easeOut(t, 2.0, 2.4) * (1 - ease(t, 3.4, 3.8));
    text(ctx, 'Loan costs:', 1180, 560, 'caption', { alpha: aB, plate: 'rgba(14,17,22,0.8)' });
    text(ctx, CL('cost_median'), 1180, 690, 'hero', { alpha: aB, color: C.warn, plate: 'rgba(14,17,22,0.8)' });
    text(ctx, 'the fees for the new loan', 1180, 790, 'label', { alpha: aB, plate: 'rgba(14,17,22,0.8)' });
    // after the pull-back: fee tag on the letter, house labels, the promise
    const lb = P(new THREE.Vector3(LP.x, 0.02, LP.z + LH / 2));
    const lr = P(new THREE.Vector3(LP.x + LW / 2, 0.02, LP.z + LH * 0.25));
    text(ctx, 'fees ' + CL('cost_median'), lr.x + 30, lr.y + 20, 'label', { alpha: easeOut(t, 5.6, 6.0), shadow: true });
    const nh = P(new THREE.Vector3(Hs[1].x, 0, HZ + base.d * ks / 2 + 0.2));
    const aN = easeOut(t, 5.6, 6.0);
    mark(ctx, 'nora', nh.x - 88, nh.y + 44, 18, aN);
    text(ctx, 'Nora', nh.x - 60, nh.y + 62, 'label', { alpha: aN, shadow: true });
    const sh = P(new THREE.Vector3(Hs[0].x, 0, HZ + 0.6)), lh = P(new THREE.Vector3(Hs[2].x, 0, HZ + 1.0));
    text(ctx, 'smaller loan', sh.x, sh.y + 62, 'note', { align: 'center', color: C.muted, alpha: aN, shadow: true });
    text(ctx, 'larger loan', lh.x, lh.y + 62, 'note', { align: 'center', color: C.muted, alpha: aN, shadow: true });
    const oh = P(new THREE.Vector3(out.position.x, base.h * ks + base.roof * ks, HZ));
    const aO = easeOut(t, 7.9, 8.4);
    const ob = P(new THREE.Vector3(out.position.x, 0, HZ + 1.0));
    text(ctx, 'your loan?', ob.x, ob.y + 62, 'label', { align: 'center', alpha: aO, shadow: true });
    // the promise (on-screen form of the owner's line)
    text(ctx, 'How big a rate cut makes it worth it for Nora?', W / 2, 226, 'caption', { align: 'center', alpha: easeOut(t, 6.4, 6.8), plate: 'rgba(14,17,22,0.72)' });
    text(ctx, 'And where does a loan your size fall?', W / 2, 316, 'caption', { align: 'center', alpha: easeOut(t, 8.2, 8.6), plate: 'rgba(14,17,22,0.72)' });
    chrome(ctx, { illus: easeOut(t, 5.6, 6.0), source: 'Fees: median 2025 refinance bill (HMDA). Nora is illustrative.', srcAlpha: easeOut(t, 1.0, 1.4), plate: true });
  }

  return { duration: DUR, update, overlay, stripTimes: [0.6, 2.4, 4.4, 6.2, 8.2, 10.9], hardTime: 10.95 };
}
