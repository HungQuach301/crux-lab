// KEY-1 (S01.2-S01.3): a level rail (9% fixed) vs a bead on a wavy track that starts just below it (7.5% variable);
// the track ahead of the bead wavers (three faint branches that keep changing); gap bead-rail glows green; rail goes
// amber where the bead is above it. Two offer cards (level line / wavy line, no words) and Leah's diamond between them.
// Track = the real replay starting January 2002 (data.js runs['2002-01'].rates), no number is printed from it.
import { THREE, C, W, H, DATA, CL, text, numWords, badge, ease, easeOut, back, mix, clamp } from './engine.js';
import { lights, table, rail, bead, gapGlow, wire, offerCard, leah } from './world.js';

const DUR = 8.0;
export function build({ scene, camera, renderer }) {
  renderer.toneMappingExposure = 1.05;
  lights(scene, { key: [-1.5, 9, 6], target: [0, 0.6, 0], power: 120 });
  table(scene, 16, 9, -0.5);
  const P = DATA.runs['2002-01'].rates;
  const X0 = -3.4, X1 = 3.4, YR = 1.55, ZR = 0.4, KB = 0.3;
  const xm = (k) => X0 + (X1 - X0) * k / 119, yr = (r) => YR + (r - 9) * KB;
  const R = rail(scene, 120, { posts: true });
  const B = bead(scene, 0.1), G = gapGlow(scene, 0.06);
  const T = wire(scene, C.accent, 0.022);
  const ghosts = [0, 1, 2].map(() => wire(scene, C.accent, 0.014, { opacity: 0.33 }));
  const cardL = offerCard(scene, 'level', { w: 2.0, d: 1.3 }), cardR = offerCard(scene, 'wavy', { w: 2.0, d: 1.3 });
  const L = leah(scene);
  const MON = (t) => (t < 2.6 ? 0 : Math.min(96, (t - 2.6) / 4.6 * 96)); // months travelled
  function update(t) {
    const a = easeOut(t, 0.0, 0.8);
    cardL.position.set(-1.9, 0.01, -1.3 + (1 - a) * 0.4); cardR.position.set(1.9, 0.01, -1.3 + (1 - a) * 0.4);
    cardL.rotation.y = 0.06; cardR.rotation.y = -0.06;
    // Leah weighs: tilts toward one card then the other
    L.position.set(0.0, 0, 1.9); const sw = Math.sin(t * 1.6) * 0.35 * (1 - ease(t, 6.6, 7.6));
    L.rotation.z = sw * 0.5; L.userData.d.rotation.y = t * 0.6;
    const grow = ease(t, 0.8, 2.2);
    R.userData.place(X0, mix(X0 + 0.01, X1, grow), YR, ZR, (j) => (j <= MON(t) && P[j] > 9 ? 1 : 0));
    const m = MON(t), k = Math.floor(m), f = m - k;
    const pts = []; for (let j = 0; j <= Math.min(k, 119); j++) pts.push(new THREE.Vector3(xm(j), yr(P[j]), ZR));
    const by = k < 119 ? mix(yr(P[k]), yr(P[k + 1]), f) : yr(P[119]), bx = xm(m);
    pts.push(new THREE.Vector3(bx, by, ZR));
    const tg = ease(t, 1.4, 2.4);
    if (pts.length < 3) { pts.length = 0; pts.push(new THREE.Vector3(X0 - 0.01, yr(7.5), ZR), new THREE.Vector3(X0 + 0.02 + 0.2 * tg, yr(7.5), ZR)); }
    T.userData.set(pts); T.visible = tg > 0.01;
    B.position.set(bx, by + 0.105, ZR); B.rotation.y = t * 1.2; B.visible = tg > 0.01; B.scale.setScalar(Math.max(0.01, back(t, 1.4, 2.2)));
    G.userData.set(bx, by + 0.105, YR, ZR, ease(t, 2.0, 2.6));
    // the unknown ahead: three faint branches that keep changing shape
    ghosts.forEach((gw, i) => {
      const n = 26, pts2 = [new THREE.Vector3(bx, by, ZR)];
      for (let s = 1; s <= n; s++) {
        const u = s / n, xx = bx + u * 2.2; if (xx > X1 + 0.6) break;
        const wob = Math.sin(u * 5.2 + t * (1.3 + i * 0.4) + i * 2.1) * 0.55 * u + Math.sin(u * 11 + t * 2.7 + i) * 0.12 * u + (i - 1) * 0.35 * u;
        pts2.push(new THREE.Vector3(xx, by + wob, ZR - 0.02 * i));
      }
      gw.userData.set(pts2); gw.visible = tg > 0.5 && pts2.length > 2; gw.material.opacity = 0.33 * ease(t, 2.0, 2.8);
    });
    const c = ease(t, 0, 8);
    camera.fov = 38; camera.position.set(mix(0.5, 0.3, c), mix(3.9, 3.6, c), mix(7.6, 6.9, c)); camera.lookAt(0, 0.95, -0.2); camera.updateProjectionMatrix();
  }
  function overlay(ctx, t, proj) {
    const ta = ease(t, 2.2, 2.7);
    const pr = proj(new THREE.Vector3(X1, YR, ZR));
    numWords(ctx, CL('fixed_rate'), 'fixed', pr.x - 6, pr.y - 30, { align: 'right', alpha: ta });
    const pb = proj(new THREE.Vector3(X0, yr(7.5), ZR));
    numWords(ctx, CL('var_start'), 'variable, starts lower', pb.x - 10, pb.y + 150, { alpha: ta });
    const pl = proj(new THREE.Vector3(0.0, 0, 1.9));
    text(ctx, 'Leah', pl.x + 48, pl.y - 40, 'label', { alpha: ease(t, 0.6, 1.1) });
    badge(ctx, ease(t, 0.6, 1.1));
  }
  return { duration: DUR, stripTimes: [0.5, 2.2, 3.6, 5.0, 6.4, 7.9], update, overlay };
}
