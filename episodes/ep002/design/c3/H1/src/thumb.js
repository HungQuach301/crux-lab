// Concept thumbnail (packaging.md §5): the hero is ONE readable object group at 10%: the 10-year frame on the 1977
// climb with Leah's bead far above the amber rail, and the two interest piles with the red extra block.
// <= 4 words. The ILLUSTRATIVE badge sits in its reserved top-right zone at 32 px (type.badge 48 @1080 scaled).
// No result number is printed.
import { THREE, C, DATA, text, badge, mix } from './engine.js';
import { lights, table, ridge, ridgeWire, rail, bead, frame, coinPile, xOf, KY, RIDGE, Z, startIdx } from './world.js';

export function build({ scene, camera, renderer }) {
  renderer.toneMappingExposure = 1.08;
  lights(scene, { key: [-2, 11, 8], target: [-1.5, 0.8, 0], power: 190, shadowSize: 2048 });
  table(scene, 26, 16, 0.5);
  ridge(scene);
  const k = startIdx('1977-04'), run = DATA.runs['1977-04'];
  const F = frame(scene), R = rail(scene, 120, { r: 0.05 }), Wi = ridgeWire(scene), B = bead(scene, 0.17);
  const peakM = 49; // bead placed on the climb toward the window's high point
  let a = 0, b = 0; for (let i = 0; i < 120; i++) { a += DATA.fixedIntM[i]; b += run.varInt[i]; }
  const nf = Math.round(a / 500), nv = Math.round(b / 500);
  const XP = xOf(k + 120) + 0.8, ZP = 0.6;
  const fixC = coinPile(scene, 60, { r: 0.3, th: 0.042 }), varC = coinPile(scene, 60, { r: 0.3, th: 0.042 }), redC = coinPile(scene, 30, { r: 0.3, th: 0.042, color: C.negative });
  function update() {
    const ry = KY * (RIDGE[k] + 1.5);
    F.position.x = xOf(k); F.userData.alpha(1);
    R.userData.place(xOf(k), xOf(k + 119), ry, Z.rail + 0.02, (q) => (RIDGE[k + q] > RIDGE[k] + 1.5 ? 1 : 0));
    Wi.userData.set(k, 120, 0, Z.ridge1 + 0.03, 1);
    B.position.set(xOf(k + peakM), KY * RIDGE[k + peakM] + 0.17, Z.ridge1 + 0.08);
    B.rotation.y = 0.5;
    fixC.userData.set(XP, ZP, nf); varC.userData.set(XP + 0.75, ZP, nf); redC.userData.set(XP + 0.75, ZP, nv - nf, 0.042 * nf);
    camera.fov = 34; camera.position.set(-1.0, 3.3, 7.4); camera.lookAt(-1.4, 1.65, -0.6); camera.updateProjectionMatrix();
  }
  function overlay(ctx) {
    text(ctx, 'Variable', 52, 140, 'hero');
    text(ctx, 'or fixed?', 52, 252, 'hero');
    badge(ctx, 1);
  }
  return { duration: 2 / 30, stripTimes: [], update, overlay };
}
