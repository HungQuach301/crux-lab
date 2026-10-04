// KEY-2 (S03.5-S03.8): the head start is the thing measured. A green bracket snaps between rail (9%) and bead at the
// start line, then widens (bigger), narrows (smaller), closes (zero) and flips into a hollow grey outline when the bead
// starts above the rail (negative) - the rail turns amber there. A ruler with plain ticks (no numbers) stands beside it.
import { THREE, C, DATA, CL, text, numWords, badge, ease, easeOut, back, mix, canvasTex, mat, box } from './engine.js';
import { lights, table, rail, bead, bracket, gapGlow, wire } from './world.js';

const DUR = 10.0;
const KEYS = [[0, 1.5], [3.0, 3.0], [4.8, 0.5], [6.4, 0.0], [8.0, -1.0]]; // [time the move starts, gap in points]
const MOVE = 0.55;
const WORDS = [null, 'bigger', 'smaller', 'zero', 'negative'];
export function build({ scene, camera, renderer }) {
  renderer.toneMappingExposure = 1.0;
  lights(scene, { key: [-2, 8, 6], target: [0.5, 0.8, 0], power: 110 });
  table(scene, 14, 9, -1);
  const YR = 1.75, ZR = 0, KB = 0.3, XS = 0, X1 = 4.6;
  const R = rail(scene, 60, { posts: false });
  const B = bead(scene, 0.11), BR = bracket(scene, { arm: 0.34, th: 0.06 }), G = gapGlow(scene, 0.06);
  const T = wire(scene, C.accent, 0.022);
  // start-line post and a ruler with plain ticks
  const post = box(0.03, 2.9, 0.03, mat(C.muted, { roughness: 0.5 })); post.position.set(XS - 0.12, 1.45, ZR - 0.18);
  const rt = canvasTex(64, 1024, (g, w, h) => { g.fillStyle = C.paper; g.fillRect(0, 0, w, h); g.fillStyle = '#4A505B'; for (let i = 0; i <= 32; i++) { const y = 16 + i * (h - 32) / 32; g.fillRect(0, y - 2, i % 4 ? 26 : 50, 4); } });
  const ruler = new THREE.Mesh(new THREE.BoxGeometry(0.16, 2.6, 0.02), [mat(C.paper), mat(C.paper), mat(C.paper), mat(C.paper), new THREE.MeshStandardMaterial({ map: rt, roughness: 0.9 }), mat(C.paper)]);
  ruler.position.set(XS - 0.62, 1.5, ZR); ruler.castShadow = true; scene.add(ruler);
  const gapAt = (t) => { let g = KEYS[0][1]; for (let i = 1; i < KEYS.length; i++) g = mix(g, KEYS[i][1], ease(t, KEYS[i][0], KEYS[i][0] + MOVE)); return g; };
  function update(t) {
    const g = gapAt(t), yb = YR - g * KB;
    const above = g < -0.02;
    R.userData.place(XS - 0.9, X1, YR, ZR, (j) => { const x = XS - 0.9 + (j + 0.5) * (X1 - XS + 0.9) / 60; return above && x > XS - 0.35 && x < XS + 0.45 ? 1 : 0; });
    B.position.set(XS + 0.12, yb, ZR); B.rotation.y = t * 1.0;
    const pts = []; for (let j = 0; j <= 30; j++) { const x = XS + 0.12 + j * 0.14; pts.push(new THREE.Vector3(x, yb - 0.11 + Math.sin(j * 0.5) * 0.04 * (j / 30), ZR)); }
    T.userData.set(pts); T.material.opacity = 1;
    const s = back(t, 0.6, 1.2);
    BR.userData.set(XS - 0.22, yb, YR, ZR + 0.02, s);
    G.visible = false;
    const c = ease(t, 0, DUR);
    camera.fov = 36; camera.position.set(mix(2.0, 1.7, c), mix(2.5, 2.35, c), mix(5.6, 5.1, c)); camera.lookAt(0.9, 1.35, 0); camera.updateProjectionMatrix();
  }
  function overlay(ctx, t, proj) {
    const pb = proj(new THREE.Vector3(XS - 0.75, YR - 1.5 * KB / 2, ZR));
    numWords(ctx, CL('gap_start'), 'head start', 56, 610, { alpha: Math.min(ease(t, 1.2, 1.6), 1 - ease(t, 2.8, 3.0)) });
    for (let i = 1; i < KEYS.length; i++) {
      const a0 = KEYS[i][0] + MOVE, a1 = i + 1 < KEYS.length ? KEYS[i + 1][0] : DUR + 1;
      text(ctx, WORDS[i], 56, 610, 'head', { alpha: Math.min(ease(t, a0 - 0.1, a0 + 0.15), 1 - ease(t, a1 - 0.15, a1)) });
    }
    badge(ctx, 1);
  }
  return { duration: DUR, stripTimes: [0.4, 2.0, 4.2, 5.8, 7.4, 9.6], update, overlay };
}
