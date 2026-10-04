// KEY-7 (S09.4-S10.3): moving the head start. A slider at the front (ticks every 0.25 point, no numbers; Leah's
// diamond marks her 1.5) carries a green bracket whose height = the head start (hollow grey when negative). The trays
// show, for the head start under the knob, which starts cost more in total (data.js costlier[gap], real model, -1..3
// by 0.25). Right: fixed coin pile + red block = the worst replay's extra interest at that head start (worstAt[gap]).
// Bigger bracket -> red drains from both trays; the right tray goes fully grey at 2 points; the left tray always keeps
// a thin red layer; the red block shrinks but never vanishes. Sweeping back to -1: both trays refill, block grows.
import { source, THREE, C, DATA, CL, text, numWords, badge, ease, easeOut, mix, lin, clamp, mat, box, canvasTex } from './engine.js';
import { xOf, coinPile, bracket, Z, TILE } from './world.js';
import { history, NS } from './hist.js';

const DUR = 10.0, COIN = 500, CT = 0.026;
const PATH = [[0, 1.5], [1.2, 1.5], [2.4, 2.0], [3.4, 2.0], [4.4, 3.0], [5.8, 3.0], [8.6, -1.0], [10, -1.0]];
const gapAt = (t) => { for (let i = 1; i < PATH.length; i++) if (t <= PATH[i][0]) { const [t0, g0] = PATH[i - 1], [t1, g1] = PATH[i]; return mix(g0, g1, ease(t, t0, t1)); } return PATH[PATH.length - 1][1]; };
const GRID = Array.from({ length: 17 }, (_, i) => -1 + 0.25 * i);
const key = (g) => String(+g.toFixed(2)).replace(/^-0$/, '0');
export function build({ scene, camera, renderer }) {
  const Hs = history(scene);
  Hs.F.visible = false; Hs.FR.visible = false; Hs.WIRE.visible = false; Hs.B.visible = false; Hs.BR.visible = false;
  // slider
  const SX0 = -4.5, SX1 = 4.5, SZ = 5.0, sx = (g) => SX0 + (SX1 - SX0) * (g + 1) / 4;
  const track = box(SX1 - SX0 + 0.4, 0.06, 0.22, mat('#2A303B', { roughness: 0.7 })); track.position.set(0, 0.03, SZ); scene.add(track);
  for (const g of GRID) { const tk = box(0.025, 0.02, Number.isInteger(g) ? 0.42 : 0.26, mat(C.muted, { roughness: 0.6 })); tk.position.set(sx(g), 0.065, SZ + 0.2); scene.add(tk); }
  const lm = new THREE.Mesh(new THREE.OctahedronGeometry(0.14, 0), mat(C.ink, { flatShading: true, emissive: new THREE.Color('#C9D2E0'), emissiveIntensity: 0.3 })); lm.position.set(sx(1.5), 0.17, SZ + 0.5); scene.add(lm);
  const knob = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.22, 0.14, 24), mat(C.ink, { roughness: 0.4 })); knob.castShadow = true; scene.add(knob);
  const BR = bracket(scene, { arm: 0.42, th: 0.085 });
  const steel = mat(C.steel, { roughness: 0.35, metalness: 0.75 });
  const mrail = new THREE.Mesh(new THREE.CylinderGeometry(0.055, 0.055, 1.7, 16), steel); mrail.rotation.z = Math.PI / 2; mrail.castShadow = true; scene.add(mrail);
  const mbead = new THREE.Mesh(new THREE.OctahedronGeometry(0.17, 0), mat(C.ink, { flatShading: true, emissive: new THREE.Color('#C9D2E0'), emissiveIntensity: 0.35 })); mbead.castShadow = true; scene.add(mbead);
  const stem = box(0.03, 1, 0.03, steel); scene.add(stem);
  const amber = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.7, 12), new THREE.MeshBasicMaterial({ color: C.warn, toneMapped: false })); amber.rotation.z = Math.PI / 2; scene.add(amber);
  const fixC = coinPile(scene, 60, { r: 0.26, th: CT }), redC = coinPile(scene, 45, { r: 0.26, th: CT, color: C.negative });
  const XP = -6.3, ZP = 4.3;
  function update(t) {
    const g = gapAt(t);
    knob.position.set(sx(g), 0.12, SZ);
    // bracket on the knob: from y0 (the "rail" level) down by the head start; flips (hollow) when negative
    const y0 = 1.65, ky = 0.42, yb = y0 - g * ky;
    mrail.position.set(sx(g) + 0.5, y0, SZ); mbead.position.set(sx(g) + 0.3, yb, SZ); mbead.rotation.y = t;
    stem.position.set(sx(g), Math.min(y0, yb) / 2, SZ - 0.1); stem.scale.y = Math.min(y0, yb) - 0.1;
    amber.visible = g < -0.02; amber.position.set(sx(g) + 0.3, y0, SZ);
    BR.userData.set(sx(g) - 0.05, yb, y0, SZ, 1);
    const gl = Math.max(-1, Math.min(2.75, Math.floor((g + 1e-6) * 4) / 4)), gh = Math.min(3, gl + 0.25), fr = clamp((g - gl) / 0.25);
    const A = DATA.costlier[key(gl)], Bv = DATA.costlier[key(gh)];
    Hs.TR.userData.update((j) => { const r = mix(A[j], Bv[j], fr); return { y: 0, kind: r > 0.5 ? 'red' : 'grey', h: r, mixRed: r }; }, DATA.worstIdx, 0);
    const wa = mix(DATA.worstAt[key(gl)], DATA.worstAt[key(gh)], fr);
    const nf = Math.round(DATA.fixedInt / COIN);
    fixC.userData.set(XP, ZP, nf); redC.userData.set(XP, ZP, Math.round(wa / COIN), CT * nf);
    camera.fov = 45; camera.position.set(0.0, 7.4, 14.6); camera.lookAt(0.0, 0.5, 1.6); camera.updateProjectionMatrix();
  }
  function overlay(ctx, t, proj) {
    const pl = proj(new THREE.Vector3(sx(1.5), 0, SZ + 0.6));
    numWords(ctx, CL('gap_start'), 'Leah', pl.x, Math.min(690, pl.y + 58), { align: 'center', alpha: Math.min(ease(t, 0.2, 0.5), 1 - ease(t, 1.6, 1.9)) });
    const pr = proj(new THREE.Vector3((xOf(324) + xOf(752)) / 2, 3.6, -1.4)), pL = proj(new THREE.Vector3((xOf(0) + xOf(323)) / 2, 3.6, -1.4));
    numWords(ctx, CL('gap20_late'), 'starts 1981 on', pr.x, 150, { align: 'center', alpha: Math.min(ease(t, 2.4, 2.7), 1 - ease(t, 4.2, 4.5)) });
    numWords(ctx, CL('gap30_early'), 'starts 1954–1980', pL.x, 150, { align: 'center', alpha: Math.min(ease(t, 4.4, 4.7), 1 - ease(t, 6.0, 6.3)) });
    badge(ctx, 1);
    source(ctx, 'tl');
  }
  return { duration: DUR, stripTimes: [0.6, 2.9, 5.0, 6.8, 7.8, 9.6], update, overlay };
}
