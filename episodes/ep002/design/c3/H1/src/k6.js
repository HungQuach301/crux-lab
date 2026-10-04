// KEY-6 (S08.1-S08.7): the worst replay. The frame lands on the steepest climb of the left half (start April 1977).
// Leah's bead rides the ridge far above the frame's rail; the rail is amber for years; the jar fills a little and is
// emptied. Two coin piles grow month by month (one coin = $500 of interest; data.js runs['1977-04'].varInt and
// fixedIntM): fixed (silver) and variable. Once the variable pile passes the fixed one, the extra coins are red;
// at the end the red block is 43% of the fixed pile ($11,219 on $26,005).
import { source, THREE, C, DATA, CL, text, numWords, badge, ease, easeOut, mix, lin, clamp } from './engine.js';
import { lights, table, ridge, ridgeWire, rail, bead, gapGlow, frame, jar, coinPile, trays, xOf, KY, RIDGE, Z, startIdx } from './world.js';

const DUR = 10.0, M0 = 1.8, M1 = 7.8, CAP = 2000, COIN = 500;
export function build({ scene, camera, renderer }) {
  lights(scene, { key: [-3, 12, 9], target: [-1.5, 0.5, 0], power: 170, shadowSize: 2048 });
  table(scene, 26, 16, 0.5);
  ridge(scene);
  const k = startIdx('1977-04'), run = DATA.runs['1977-04'];
  const F = frame(scene), R = rail(scene, 120), Wi = ridgeWire(scene), B = bead(scene, 0.1), G = gapGlow(scene, 0.05);
  const J = jar(scene, { r: 0.4, h: 1.5 });
  const fixCoins = coinPile(scene, 60), varCoins = coinPile(scene, 60), redCoins = coinPile(scene, 30, { color: C.negative });
  const cumF = [], cumV = []; let a = 0, b = 0;
  for (let i = 0; i < 120; i++) { a += DATA.fixedIntM[i]; b += run.varInt[i]; cumF.push(a); cumV.push(b); }
  const peakM = run.rates.indexOf(Math.max(...run.rates));
  const XP = xOf(k + 120) + 0.9, ZP = 0.9;
  const mAt = (t) => 119 * lin(t, M0, M1);
  function update(t) {
    const m = mAt(t), j = Math.floor(m), f = m - j;
    const ry = KY * (RIDGE[k] + 1.5), la = easeOut(t, 0, 1.0);
    F.position.set(xOf(k), (1 - la) * 2.5, F.position.z); F.userData.alpha(la);
    R.userData.place(xOf(k), xOf(k + 119), ry, Z.rail + 0.02, (q) => (t >= M0 && q <= m && RIDGE[k + q] > RIDGE[k] + 1.5 ? 1 : 0), la);
    Wi.userData.set(k, 120, 0, Z.ridge1 + 0.03, Math.max(ease(t, 1.0, 1.6) * 0.999, 0.02)); Wi.visible = t > 1.0;
    const by = KY * mix(RIDGE[k + j], RIDGE[k + Math.min(119, j + 1)], f) + 0.1, bx = xOf(k + m);
    B.position.set(bx, by, Z.ridge1 + 0.06); B.rotation.y = t; B.visible = t > 1.0;
    G.userData.set(bx, by, ry, Z.ridge1 + 0.06, la);
    const c = t < M0 ? 0 : mix(run.cushion[j], run.cushion[Math.min(119, j + 1)], f);
    const d = j > 0 ? run.cushion[j] - run.cushion[j - 1] : run.cushion[0];
    J.position.set(xOf(k + 60), 0, 1.15); J.userData.set(Math.max(0, c) / CAP, t > M0 && t < M1 && d > 0 ? clamp(d / 60) : 0, 0);
    const nf = t < M0 ? 0 : Math.round(mix(cumF[j], cumF[Math.min(119, j + 1)], f) / COIN);
    const nv = t < M0 ? 0 : Math.round(mix(cumV[j], cumV[Math.min(119, j + 1)], f) / COIN);
    fixCoins.userData.set(XP, ZP, nf);
    varCoins.userData.set(XP + 0.62, ZP, Math.min(nv, nf));
    redCoins.userData.set(XP + 0.62, ZP, Math.max(0, nv - nf), varCoins.userData.th * nf);
    const cz = ease(t, 0, DUR);
    camera.fov = 38; camera.position.set(mix(-1.2, -1.0, cz), mix(4.3, 4.0, cz), mix(10.4, 9.8, cz)); camera.lookAt(-1.1, 1.45, -0.4); camera.updateProjectionMatrix();
  }
  function overlay(ctx, t, proj) {
    const pa = proj(new THREE.Vector3(xOf(k), 3.9, Z.ridge1));
    text(ctx, CL('worst_start'), pa.x - 10, pa.y - 18, 'head', { alpha: Math.min(ease(t, 1.0, 1.4), 1 - ease(t, 4.0, 4.3)) });
    const tp = mix(M0, M1, peakM / 119), pp = proj(new THREE.Vector3(xOf(k + peakM), KY * RIDGE[k + peakM] + 0.25, Z.ridge1));
    text(ctx, CL('worst_peak_rate'), pp.x + 22, pp.y - 6, 'number', { alpha: Math.min(ease(t, tp, tp + 0.3), 1 - ease(t, tp + 2.4, tp + 2.7)) });
    const pf = proj(new THREE.Vector3(XP + 0.31, 0, ZP + 0.3));
    numWords(ctx, CL('fixed_int'), 'fixed', pf.x, pf.y + 70, { align: 'center', alpha: ease(t, 8.0, 8.4) });
    const pv = proj(new THREE.Vector3(XP + 0.95, 2.6, ZP));
    text(ctx, CL('worst_diff'), pv.x + 4, pv.y, 'number', { color: C.ink, alpha: ease(t, 8.5, 8.9) });
    badge(ctx, 1);
    source(ctx, 'br');
  }
  return { duration: DUR, stripTimes: [0.6, 2.2, 3.6, 5.2, 6.8, 9.6], update, overlay };
}
