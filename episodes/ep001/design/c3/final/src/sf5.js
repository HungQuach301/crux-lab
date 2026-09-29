// SF5 · Walt and Anjali (S14-S17). H1: two houses (volume = loan size: $115,000 vs $655,000), the SAME offer
// (7.62% -> 7.03%). In front of each: a ream = loan costs (one dollar scale for the whole frame), a hatched slab on the
// ream that grows each month = what is still owed on the new loan vs the old one (the SF3 grammar), and a column of
// monthly-savings bundles that grows for 36 months. Anjali's column passes her ream + slab at month 18; Walt's is still
// short after 3 years. Answer: rate cut needed to break even within 3 years: 1.12 points vs about a third of a point.
// Claims: r_old r_today loan_small loan_large cost_small cost_large sav_small sav_large be_bal_large net36_small
//         net36_large y3 cut36_small cut36_large_words. Slab heights from model/refi.py (data.js), not printed.
import { THREE, C, W, H, DATA, CL, text, measure, chrome, mark, strike, ease, easeOut, back, mix, clamp, rng, canvasTex, ptxt, mat, box, pm,
  paperEdgeTex, owedTex, house } from './engine.js';

export const uses3d = true;
const DUR = 12.0;

export function build({ scene, camera, renderer }) {
  const S = DATA.small, L = DATA.large;
  scene.background = new THREE.Color('#1B2536');
  scene.fog = new THREE.Fog('#1B2536', 20, 44);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#B9C8EE', '#3A3A2E', 1.4));
  const sun = new THREE.DirectionalLight('#FFD9A8', 2.8); sun.position.set(-7, 9, 7); sun.castShadow = true;
  sun.shadow.mapSize.set(1024, 1024); Object.assign(sun.shadow.camera, { left: -10, right: 10, top: 9, bottom: -6, near: 1, far: 34 }); sun.shadow.bias = -0.0006; scene.add(sun);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(70, 40), mat('#34472F', { roughness: 1 })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const walk = new THREE.Mesh(new THREE.PlaneGeometry(70, 2.6), mat('#6B6E73', { roughness: 0.95 })); walk.rotation.x = -Math.PI / 2; walk.position.set(0, 0.004, 0.2); walk.receiveShadow = true; scene.add(walk);
  const r = rng(3);
  for (let i = 0; i < 12; i++) { const s = 0.7 + r() * 0.7, tr = new THREE.Mesh(new THREE.ConeGeometry(0.8 * s, 2.8 * s, 7), mat('#22352A')); tr.position.set(-15 + i * 2.7 + r(), 1.4 * s, -9 - r() * 3); tr.castShadow = true; scene.add(tr); }

  // houses: volume = loan -> linear scale (655/115)^(1/3)
  const LS = Math.cbrt(L.loan / S.loan);
  const base = { w: 2.1, d: 1.8, h: 1.25, roof: 0.9 };
  const walt = house({ ...base, wall: '#CDBF9F', roofCol: '#4A4036', lit: 0.2 }); walt.position.set(-2.95, 0, -2.8); scene.add(walt);
  const anj = house({ w: base.w * LS, d: base.d * LS, h: base.h * LS, roof: base.roof * LS, wall: '#B9C3CC', roofCol: '#3A404C', lit: 0.2 }); anj.position.set(2.25, 0, -4.3); scene.add(anj);
  for (const h of [walt, anj]) h.traverse((o) => { if (o.isMesh) o.castShadow = o.receiveShadow = true; });

  const K = 2.1 / 14000, FW = 1.0, FD = 0.8, Z = 0.2;
  const P0 = { wf: -3.65, ws: -2.3, af: 1.55, as: 2.9 };
  const edge = paperEdgeTex();
  function ream(cost, label) {
    const h = cost * K;
    const front = canvasTex(512, Math.max(64, Math.round(512 * h / FW)), (g, w, hh) => {
      g.fillStyle = C.paper; g.fillRect(0, 0, w, hh); for (let y = 0; y < hh; y += 6) { g.fillStyle = C.paperLine; g.fillRect(0, y, w, 2); }
      g.fillStyle = '#2E3440'; g.fillRect(0, hh * 0.12, w, hh * 0.76);
      ptxt(g, label, w / 2, hh * 0.5 + 40, { size: 118, weight: 700, color: '#FFFFFF', align: 'center' });
    });
    const m = box(FW, h, FD, [pm(edge), pm(edge), pm(edge), pm(edge), pm(front), pm(edge)]); m.userData.h = h; scene.add(m); return m;
  }
  const wRe = ream(S.cost, CL('cost_small')), aRe = ream(L.cost, CL('cost_large'));
  const ot = owedTex(); ot.repeat.set(1.5, 1);
  const owedM = new THREE.MeshStandardMaterial({ map: ot, roughness: 0.85 });
  const wOw = box(FW + 0.02, 1, FD + 0.02, owedM), aOw = box(FW + 0.02, 1, FD + 0.02, owedM); scene.add(wOw, aOw);
  const noteTex = canvasTex(256, 128, (g, w, h) => { g.fillStyle = '#D5E6D8'; g.fillRect(0, 0, w, h); g.strokeStyle = '#6FA383'; g.lineWidth = 6; g.strokeRect(8, 8, w - 16, h - 16); g.fillStyle = C.cashBand; g.fillRect(w / 2 - 36, 0, 72, h); });
  const cs = mat(C.cashSide, { roughness: 0.95 }), bandS = mat(C.cashBand, { roughness: 0.9 });
  function column(sav) {
    const th = sav * K, arr = [];
    const g = new THREE.BoxGeometry(FW * 0.92, th * 0.9, FD * 0.8);
    for (let i = 0; i < 36; i++) {
      const b = new THREE.Mesh(g, [cs, cs, pm(noteTex), cs, bandS, cs]); b.castShadow = b.receiveShadow = true;
      b.userData = { jx: Math.sin(i * 12.99 + sav) * 0.02, jr: Math.sin(i * 78.2 + sav) * 0.03, th }; scene.add(b); arr.push(b);
    }
    return arr;
  }
  const wCol = column(S.sav), aCol = column(L.sav);
  const lasers = [0, 1].map(() => { const l = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.02, 0.02), new THREE.MeshBasicMaterial({ color: '#FFFFFF', transparent: true, opacity: 0 })); scene.add(l); return l; });

  const monthAt = (t) => clamp((t - 2.6) / 4.8) * 36;
  const at = (arr, m) => { const a = Math.floor(m), b = Math.min(arr.length - 1, a + 1); return mix(arr[a], arr[b], m - a); };
  const beT = 2.6 + 4.8 * (L.be / 36); // time Anjali's column reaches ream + slab (month 18)

  function update(t) {
    const k = ease(t, 0, DUR);
    camera.position.set(-0.35, mix(2.5, 2.4, k), mix(9.6, 9.2, k)); camera.lookAt(-0.35, 1.45, -0.6);
    const mf = monthAt(t);
    for (const [re, x, t0] of [[wRe, P0.wf, 1.2], [aRe, P0.af, 1.45]]) { const d = easeOut(t, t0, t0 + 0.5); re.position.set(x, re.userData.h / 2 + (1 - d) * 3, Z); re.visible = t > t0; }
    for (const [ow, re, x, d] of [[wOw, wRe, P0.wf, S], [aOw, aRe, P0.af, L]]) {
      const g = Math.max(0.001, at(d.gap, mf) * K); ow.visible = mf > 0.05; ow.scale.y = g; ow.position.set(x, re.userData.h + g / 2, Z);
    }
    for (const [col, x] of [[wCol, P0.ws], [aCol, P0.as]]) {
      col.forEach((b, i) => {
        const land = easeOut(mf, i, i + 0.9); b.visible = mf > i;
        b.position.set(x + b.userData.jx, b.userData.th * (i + 0.5) + (1 - land) * 0.5, Z + b.userData.jx);
        b.rotation.y = b.userData.jr + (1 - land) * 0.3;
      });
    }
    [[wRe, P0.wf, P0.ws, S], [aRe, P0.af, P0.as, L]].forEach(([re, xf, xs, d], j) => {
      const l = lasers[j], top = re.userData.h + at(d.gap, mf) * K; l.position.set((xf + xs) / 2, top + 0.012, Z + FD / 2 + 0.03);
      l.material.opacity = ease(t, 2.3, 2.7);
      const full = d.sav * mf * K >= top - 1e-4; l.material.color.set(full ? C.positive : (mf >= 36 ? C.negative : '#FFFFFF'));
    });
  }

  function overlay(ctx, t, P) {
    const mf = monthAt(t);
    // header: the offer, then the answer
    const aH = easeOut(t, 0.1, 0.5) * (1 - ease(t, 7.9, 8.2));
    text(ctx, 'Same offer for both: ' + CL('r_old') + ' → ' + CL('r_today'), 96, 128, 'head', { alpha: aH });
    const aA = easeOut(t, 8.2, 8.6);
    text(ctx, 'Rate cut needed to break even', 96, 124, 'caption', { alpha: aA });
    text(ctx, 'within ' + CL('y3') + ' years · point = one percentage point of the rate', 96, 188, 'note', { color: C.muted, alpha: aA });
    // answers (end), one per borrower, over each pair
    const wx = P(new THREE.Vector3((P0.wf + P0.ws) / 2, 0, Z)).x, ax = P(new THREE.Vector3((P0.af + P0.as) / 2, 0, Z)).x;
    text(ctx, CL('cut36_small') + ' points', wx, 300, 'number', { align: 'center', color: C.warn, alpha: easeOut(t, 8.6, 9.0), plate: 'rgba(14,17,22,0.8)' });
    text(ctx, CL('cut36_large_words'), ax, 290, 'caption', { align: 'center', alpha: easeOut(t, 9.0, 9.4), plate: 'rgba(14,17,22,0.8)' });
    // base labels
    const lab = (x, s, col, al) => { const p = P(new THREE.Vector3(x, 0, Z + FD / 2)); text(ctx, s, p.x, p.y + 56, 'note', { align: 'center', color: col, alpha: al, shadow: true }); };
    const aB = easeOut(t, 1.8, 2.2), aS = easeOut(t, 2.4, 2.8);
    lab(P0.wf, 'loan costs', C.ink, aB); lab(P0.af, 'loan costs', C.ink, aB);
    lab(P0.ws, '+' + CL('sav_small') + '/mo', '#8FE0B5', aS); lab(P0.as, '+' + CL('sav_large') + '/mo', '#8FE0B5', aS);
    // names + loans: one row under each pair
    const a = easeOut(t, 0.2, 0.7);
    const nameRow = (who, name, loan, x) => {
      const s = name + ' · ' + loan + ' loan', w = measure(ctx, s, 'label');
      mark(ctx, who, x - w / 2 - 30, 944, 22, a); text(ctx, s, x - w / 2 + 6, 962, 'label', { alpha: a, shadow: true });
    };
    nameRow('walt', 'Walt', CL('loan_small'), wx); nameRow('anjali', 'Anjali', CL('loan_large'), ax);
    // outcomes
    const pa = P(new THREE.Vector3(P0.as, L.sav * Math.min(mf, 36) * K, Z)), pl = P(new THREE.Vector3(P0.af - FW / 2, 0, Z)).x - 30;
    const ya = clamp(pa.y + 20, 440, 720), aF = easeOut(t, beT, beT + 0.3);
    text(ctx, 'paid back', pl, ya, 'label', { align: 'right', color: C.positive, alpha: aF * (1 - ease(t, 7.6, 7.9)), plate: 'rgba(14,17,22,0.8)' });
    text(ctx, 'month ' + CL('be_bal_large'), pl, ya + 60, 'label', { align: 'right', color: C.positive, alpha: aF * (1 - ease(t, 7.6, 7.9)), plate: 'rgba(14,17,22,0.8)' });
    text(ctx, CL('net36_large') + ' ahead', pl, ya, 'label', { align: 'right', color: C.positive, alpha: easeOut(t, 7.7, 8.0), plate: 'rgba(14,17,22,0.8)' });
    text(ctx, 'after ' + CL('y3') + ' years', pl, ya + 60, 'note', { align: 'right', color: C.ink, alpha: easeOut(t, 7.7, 8.0), plate: 'rgba(14,17,22,0.8)' });
    const pw = P(new THREE.Vector3((P0.wf + P0.ws) / 2, wRe.userData.h + at(S.gap, mf) * K, Z));
    text(ctx, CL('net36_small') + ' short', pw.x, pw.y - 100, 'label', { align: 'center', color: '#FF8A8E', alpha: easeOut(t, 7.5, 7.9), plate: 'rgba(14,17,22,0.8)' });
    text(ctx, 'after ' + CL('y3') + ' years', pw.x, pw.y - 30, 'note', { align: 'center', color: C.ink, alpha: easeOut(t, 7.5, 7.9), plate: 'rgba(14,17,22,0.8)' });
    chrome(ctx, { illus: 1, source: 'Walt, Anjali: illustrative. House size is to scale with the loan.', plate: true });
  }

  return { duration: DUR, update, overlay, stripTimes: [0.8, 2.4, 4.4, 6.0, 7.8, 11.9], hardTime: 11.95 };
}
