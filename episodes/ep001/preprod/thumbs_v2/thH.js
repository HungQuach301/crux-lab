// Thumbnail H (hook a, paradox): two houses from the signed H1 system (engine.house; volume = loan size, as SF2/SF5),
// small (Walt, $115,000) and large (Anjali, $655,000), same street. No text here: the flat text is laid on in compose
// (render.js). Anchors (screen px at 1920x1080) are published on window.ANCHORS for the compose step.
import { THREE, C, DATA, mat, house, rng } from '/src/engine.js';
export const uses3d = true;
export function build({ scene, camera, renderer }) {
  const S = DATA.small, L = DATA.large;
  scene.background = new THREE.Color('#141B27');
  scene.fog = new THREE.Fog('#141B27', 16, 40);
  renderer.toneMappingExposure = 1.0;
  scene.add(new THREE.HemisphereLight('#9FB2DA', '#2A2A22', 1.0));
  const sun = new THREE.DirectionalLight('#FFD9A8', 3.0); sun.position.set(-6, 8, 7); sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048); Object.assign(sun.shadow.camera, { left: -10, right: 10, top: 9, bottom: -6, near: 1, far: 34 }); sun.shadow.bias = -0.0006; scene.add(sun);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(70, 40), mat('#2C3B28', { roughness: 1 })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const walk = new THREE.Mesh(new THREE.PlaneGeometry(70, 2.2), mat('#5E6166', { roughness: 0.95 })); walk.rotation.x = -Math.PI / 2; walk.position.set(0, 0.004, 1.2); walk.receiveShadow = true; scene.add(walk);
  const r = rng(5);
  for (let i = 0; i < 12; i++) { const s = 0.7 + r() * 0.7, tr = new THREE.Mesh(new THREE.ConeGeometry(0.8 * s, 2.8 * s, 7), mat('#1E2F25')); tr.position.set(-15 + i * 2.7 + r(), 1.4 * s, -8 - r() * 3); tr.castShadow = true; scene.add(tr); }
  const LS = Math.cbrt(L.loan / S.loan); // volume = loan
  const base = { w: 1.9, d: 1.6, h: 1.15, roof: 0.85 };
  const walt = house({ ...base, wall: '#CDBF9F', roofCol: '#4A4036', lit: 0.9 }); walt.position.set(-3.1, 0, -0.6); scene.add(walt);
  const anj = house({ w: base.w * LS, d: base.d * LS, h: base.h * LS, roof: base.roof * LS, wall: '#B9C3CC', roofCol: '#3A404C', lit: 0.9 }); anj.position.set(2.6, 0, -1.6); scene.add(anj);
  for (const h of [walt, anj]) h.traverse((o) => { if (o.isMesh) o.castShadow = o.receiveShadow = true; });
  function update() { camera.position.set(-0.2, 1.7, 9.2); camera.lookAt(-0.2, 1.75, -0.8); }
  function overlay(ctx, t, P) {
    const top = (g, hh, rf) => P(new THREE.Vector3(g.position.x, hh + rf, g.position.z));
    const bot = (g, dd) => P(new THREE.Vector3(g.position.x, 0, g.position.z + dd / 2));
    window.ANCHORS = {
      waltTop: top(walt, base.h, base.roof), anjTop: top(anj, base.h * LS, base.roof * LS),
      waltBase: bot(walt, base.d), anjBase: bot(anj, base.d * LS),
    };
  }
  return { duration: 1, update, overlay, stripTimes: [0], hardTime: 0 };
}
