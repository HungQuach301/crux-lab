// Thumbnail W (hook c, window/timing): a real window (H1: kitchen wall, wooden shutters) and, as the view through it, the
// SF1 chart grammar (H3): the weekly rate line (FRED MORTGAGE30US, weeks of data.js f1, July 2025 - September 24, 2026),
// shaded "window" only over the weeks at least 1 point below 7.62%, the 2026 low as a dot. The shutters are swinging shut
// over the right side (the weeks after the window closed). No text here; "5.98%" is laid on in compose.
import { THREE, C, DATA, mat, box, pm, canvasTex, rgba } from '/src/engine.js';
export const uses3d = true;
export function build({ scene, camera, renderer }) {
  const F = DATA.f1, wk = F.weeks, N = wk.length;
  scene.background = new THREE.Color(C.bg);
  renderer.toneMappingExposure = 1.05;
  scene.add(new THREE.HemisphereLight('#8FA3C8', '#1A1410', 0.7));
  const key = new THREE.SpotLight('#FFE2BC', 80, 30, 0.8, 0.6, 1.2); key.position.set(-3, 5, 7); key.target.position.set(0, 1.5, 0);
  key.castShadow = true; key.shadow.mapSize.set(2048, 2048); key.shadow.bias = -0.0005; scene.add(key, key.target);
  // wall with an opening
  const wallM = mat(C.wall, { roughness: 1 });
  const OW = 6.4, OH = 3.4, WY = 1.8; // opening size, centre height
  const wall = (w, h, x, y) => { const m = box(w, h, 0.3, wallM); m.position.set(x, y, 0); scene.add(m); };
  wall(30, 10, 0, WY + OH / 2 + 5); wall(30, 10, 0, WY - OH / 2 - 5); wall(10, OH, -OW / 2 - 5, WY); wall(10, OH, OW / 2 + 5, WY);
  // the view: chart canvas on a plane behind the opening
  const CW = 2048, CH = 1088;
  const X0 = 90, X1 = CW - 90, R0 = 5.7, R1 = 7.95, YT = 60, YB = CH - 60;
  const xOf = (i) => X0 + (i / (N - 1)) * (X1 - X0), yOf = (r) => YB - ((r - R0) / (R1 - R0)) * (YB - YT);
  const iLow = wk.findIndex((w) => w.d === F.low), iLast = wk.findIndex((w) => w.d === F.lastIn), iFirst = wk.findIndex((w) => w.in);
  const tex = canvasTex(CW, CH, (g) => {
    g.fillStyle = '#0B0E13'; g.fillRect(0, 0, CW, CH);
    g.strokeStyle = C.grid; g.lineWidth = 4; for (const r of [6, 7]) { g.beginPath(); g.moveTo(0, yOf(r)); g.lineTo(CW, yOf(r)); g.stroke(); }
    const xa = xOf(iFirst - 0.5), xb = xOf(iLast + 0.5), yT = yOf(F.thr);
    g.fillStyle = rgba(C.accent, 0.24); g.fillRect(xa, yT, xb - xa, YB - yT + 60);
    g.strokeStyle = C.accent; g.lineWidth = 16; g.lineJoin = 'round'; g.lineCap = 'round'; g.beginPath();
    wk.forEach((w, i) => (i ? g.lineTo(xOf(i), yOf(w.r)) : g.moveTo(xOf(i), yOf(w.r)))); g.stroke();
    g.fillStyle = C.ink; g.beginPath(); g.arc(xOf(iLow), yOf(wk[iLow].r), 30, 0, 7); g.fill();
  });
  const view = new THREE.Mesh(new THREE.PlaneGeometry(OW + 0.4, (OW + 0.4) * CH / CW), new THREE.MeshBasicMaterial({ map: tex, toneMapped: false }));
  view.position.set(0, WY, -0.6); scene.add(view);
  // frame + sill
  const frameM = mat('#E9E2D2', { roughness: 0.7 });
  const bar = (w, h, x, y, z = 0.02) => { const m = box(w, h, 0.36, frameM); m.position.set(x, y, z); scene.add(m); };
  bar(OW + 0.3, 0.16, 0, WY + OH / 2); bar(OW + 0.3, 0.16, 0, WY - OH / 2); bar(0.16, OH, -OW / 2, WY); bar(0.16, OH, OW / 2, WY);
  const sill = box(OW + 0.9, 0.14, 0.7, frameM); sill.position.set(0, WY - OH / 2 - 0.1, 0.3); scene.add(sill);
  // shutters: two leaves on the right hinge, swinging shut over the weeks after the window closed
  const wood = canvasTex(256, 512, (g, w, h) => { g.fillStyle = C.wood; g.fillRect(0, 0, w, h); for (let y = 0; y < h; y += 32) { g.fillStyle = '#4A3323'; g.fillRect(0, y, w, 6); } });
  const shM = new THREE.MeshStandardMaterial({ map: wood, roughness: 0.8 });
  const leafW = OW / 2 - (xOf(iLast + 0.5) / CW - 0.5) * (OW + 0.4); // covers the weeks after the last week in the window
  const leaf = (hx, ang, sgn, lw = leafW) => { const g = new THREE.Group(); const m = box(lw, OH - 0.1, 0.08, shM); m.position.x = sgn * lw / 2; g.add(m); g.position.set(hx, WY, 0.22); g.rotation.y = ang; scene.add(g); return g; };
  leaf(OW / 2, 0.12, -1);          // right leaf (almost) shut over the weeks since the window closed
  leaf(-OW / 2, -1.25, 1, OW * 0.3);        // left leaf still swung open
  function update() { camera.position.set(0.3, 2.0, 8.2); camera.lookAt(0.1, 1.85, 0); }
  function overlay(ctx, t, P) {
    const uv = (x, y) => P(new THREE.Vector3((x / CW - 0.5) * (OW + 0.4), WY + (0.5 - y / CH) * (OW + 0.4) * CH / CW, -0.6));
    window.ANCHORS = { low: uv(xOf(iLow), yOf(wk[iLow].r)), winTop: P(new THREE.Vector3(0, WY + OH / 2, 0)), winBot: P(new THREE.Vector3(0, WY - OH / 2, 0)), rightLeaf: P(new THREE.Vector3(OW / 2 - leafW, WY, 0.22)) };
  }
  return { duration: 1, update, overlay, stripTimes: [0], hardTime: 0 };
}
