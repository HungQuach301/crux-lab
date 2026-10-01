// KEY-4 (S06.1-S06.5): the cushion. Three real replays run side by side on the same ridge, same scale:
//   left  frame 1956-05: one short jump above 9% (amber blip) only dents the jar;
//   middle frame 1976-06: rates climb early and stay high -> the jar fills a little, then is drained dry;
//   right frame 1989-03: rates drift down -> the jar keeps filling.
// Jar level = running sum of (fixed interest - variable interest) for that replay (data.js runs[].cushion), one scale
// for the three jars ($14,000 = full jar, no number printed). A green stream pours in while the bead is under the
// rail (thickness = that month's saving); a paper stack beside each jar = balance still owed (tallest at the start).
import { source, THREE, C, DATA, text, badge, ease, easeOut, mix, lin, clamp } from './engine.js';
import { lights, table, ridge, ridgeWire, rail, bead, gapGlow, frame, jar, paperStack, xOf, KY, RIDGE, Z, startIdx } from './world.js';

const DUR = 10.0, M0 = 1.3, M1 = 8.6, CAP = 14000;
const LANES = ['1956-05', '1976-06', '1989-03'];
export function build({ scene, camera, renderer }) {
  lights(scene, { key: [-3, 12, 9], target: [0, 0.5, 0], power: 170, shadowSize: 2048 });
  table(scene, 26, 16, 0.5);
  ridge(scene);
  const L = LANES.map((ym) => {
    const k = startIdx(ym), run = DATA.runs[ym];
    return { ym, k, run, F: frame(scene), R: rail(scene, 120), Wi: ridgeWire(scene), B: bead(scene, 0.085), G: gapGlow(scene, 0.05),
      J: jar(scene, { r: 0.42, h: 1.6 }), P: paperStack(scene, { w: 0.6, d: 0.42 }) };
  });
  const mAt = (t) => 119 * lin(t, M0, M1);
  function update(t) {
    const m = mAt(t), j = Math.floor(m), f = m - j;
    for (const l of L) {
      const ry = KY * (RIDGE[l.k] + 1.5), a = easeOut(t, 0, 0.8);
      l.F.position.set(xOf(l.k), (1 - a) * 2, l.F.position.z); l.F.userData.alpha(a);
      l.R.userData.place(xOf(l.k), xOf(l.k + 119), ry, Z.rail + 0.02, (q) => (q <= m && RIDGE[l.k + q] > RIDGE[l.k] + 1.5 ? 1 : 0), a);
      l.Wi.userData.set(l.k, 120, 0, Z.ridge1 + 0.03, Math.max(0.02, m / 119));
      const by = KY * mix(RIDGE[l.k + j], RIDGE[l.k + Math.min(119, j + 1)], f) + 0.085, bx = xOf(l.k + m);
      l.B.position.set(bx, by, Z.ridge1 + 0.05); l.B.rotation.y = t;
      l.G.userData.set(bx, by + 0.02, ry, Z.ridge1 + 0.05, a);
      const cs = l.run.cushion, c = j < 1 && t < M0 ? 0 : mix(cs[j], cs[Math.min(119, j + 1)], f);
      const d = j > 0 ? cs[j] - cs[j - 1] : cs[0];
      const xc = xOf(l.k + 60);
      l.J.position.set(xc + 0.35, 0, 1.1);
      l.J.userData.set(Math.max(0, c) / CAP, t > M0 && t < M1 && d > 0 ? clamp(d / 160) : 0, 0);
      const bal = l.run.balance[Math.min(119, j)] / 50000;
      l.P.userData.set(xc - 0.75, 1.15, t < M1 + 0.1 ? 1.1 * bal : 1.1 * l.run.balance[119] / 50000);
    }
    camera.fov = 36; camera.position.set(-2.7, 5.4, 12.6); camera.lookAt(-2.7, 1.05, -0.3); camera.updateProjectionMatrix();
  }
  function overlay(ctx, t, proj) {
    const p = proj(new THREE.Vector3(xOf(L[0].k + 60) + 0.35, 1.7, 1.1));
    text(ctx, 'the cushion', p.x, p.y - 16, 'label', { align: 'center', alpha: Math.min(ease(t, 1.6, 2.0), 1 - ease(t, 4.4, 4.7)) });
    badge(ctx, 1);
    source(ctx, 'br');
  }
  return { duration: DUR, stripTimes: [0.6, 2.4, 4.0, 5.6, 7.4, 9.6], update, overlay };
}
