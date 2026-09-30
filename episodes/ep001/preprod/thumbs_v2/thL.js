// Thumbnail L (hook b, hidden cost): the refinance letter of SF2 (H1) on Nora's kitchen table; from under it slides the
// hatched "still owed" slab of SF3 (owedTex = the signed "owed" pattern). The letter's bill box is left blank here: the
// number ($5,124, cost_median) and the slab's number (+$1,133, gap24) are flat text laid on in compose.
import { THREE, C, mat, box, pm, canvasTex, woodTable, owedTex } from '/src/engine.js';
export const uses3d = true;
export function build({ scene, camera, renderer }) {
  scene.background = new THREE.Color(C.bg);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', 0.6));
  const key = new THREE.SpotLight('#FFE2BC', 95, 26, 0.7, 0.6, 1.3); key.position.set(-1.8, 8, 3.5); key.target.position.set(0.2, 0, 0);
  key.castShadow = true; key.shadow.mapSize.set(2048, 2048); key.shadow.bias = -0.0005; scene.add(key, key.target);
  const rim = new THREE.DirectionalLight('#A9B6CF', 0.35); rim.position.set(5, 4, -4); scene.add(rim);
  woodTable(scene, 18, 9);
  // letter (US letter 8.5x11), same look as SF2 but without words: header bar, grey body lines, boxed bill area
  const LW = 2.6, LH = LW * 11 / 8.5;
  const tex = canvasTex(1100, 1424, (g, w, h) => {
    g.fillStyle = '#F7F4EC'; g.fillRect(0, 0, w, h);
    g.fillStyle = '#2E3440'; g.fillRect(0, 0, w, 190);
    g.fillStyle = '#CFC9BB'; for (let i = 0; i < 8; i++) g.fillRect(70, 280 + i * 70, 940 - (i % 3) * 190, 22);
    g.strokeStyle = '#20242C'; g.lineWidth = 8; g.strokeRect(40, 900, w - 80, 420);
  });
  const edge = mat('#EDE8DC');
  const letter = box(LW, 0.012, LH, [edge, edge, pm(tex), edge, edge, edge]);
  letter.position.set(-0.55, 0.03, 0.1); letter.rotation.y = 0.10; scene.add(letter);
  // the "owed" slab, sliding out from under the letter's lower right corner
  const ot = owedTex(); ot.repeat.set(2.2, 1);
  const slabW = 2.4, slabD = 0.8;
  const slab = box(slabW, 0.03, slabD, new THREE.MeshStandardMaterial({ map: ot, roughness: 0.85 }));
  slab.position.set(1.55, 0.016, 1.35); slab.rotation.y = -0.30; scene.add(slab);
  function update() { camera.position.set(0.35, 5.6, 4.6); camera.lookAt(0.2, 0, 0.35); }
  function overlay(ctx, t, P) {
    // bill box centre on the letter: texture y 900..1320 of 1424 -> local z
    const loc = (u, v) => { const p = new THREE.Vector3((u - 0.5) * LW, 0.02, (v - 0.5) * LH); p.applyEuler(letter.rotation); return P(p.add(letter.position)); };
    const sl = (u, v) => { const p = new THREE.Vector3((u - 0.5) * slabW, 0.04, (v - 0.5) * slabD); p.applyEuler(slab.rotation); return P(p.add(slab.position)); };
    window.ANCHORS = { billL: loc(0.07, 0.77), billR: loc(0.93, 0.77), billC: loc(0.5, 0.78), letterTop: loc(0.5, 0), slabC: sl(0.62, 0.5), slabR: sl(1, 0.5), slabL: sl(0.3, 0.5) };
  }
  return { duration: 1, update, overlay, stripTimes: [0], hardTime: 0 };
}
