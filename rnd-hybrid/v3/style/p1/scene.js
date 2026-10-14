// R&D vòng 3 · khung phong cách P1: GIẤY NHIỀU LỚP NÂNG CẤP. Người lớn 1930 vẽ tay bằng mã (figure1930.js, kiểu 'paper'), tách 5 lớp
// (tay sau · chân sau · thân + chân trước · đầu + mũ · tay trước), mỗi lớp một tấm giấy cong có mép dày, cách nhau 3 cm, đổ bóng lên nhau.
// Nhà: khối giấy gấp in mặt tiền 1930 (street2d.js); ngân hàng: mặt tiền in + cột giấy cuộn + bậc gấp thật. Đèn hồi khủng hoảng, bóng thật.
import * as THREE from 'three';
import { drawFigure, crowdSpec } from '/rnd-hybrid/v3/style/figure1930.js';
import { facade, bankFacade, pavement } from '/rnd-hybrid/v3/style/street2d.js';
import { foldBox, roll, paperMat, paperTex } from '/rnd-hybrid/v3/lib/paperfold.js';
import { paperGrain, vignette } from '/rnd-hybrid/v2/paper3d.js';

const LAYERS = [['backArm'], ['backLeg'], ['body'], ['head'], ['frontArm']];
function bent(w, h, bend) { const g = new THREE.PlaneGeometry(w, h, 12, 1), p = g.attributes.position; for (let i = 0; i < p.count; i++) { const x = p.getX(i) / (w / 2); p.setZ(i, -bend * x * x); } g.computeVertexNormals(); g.translate(0, h / 2, 0); return g; }
const edgeMat = new THREE.MeshStandardMaterial({ color: '#EFE6D2', roughness: 1 });
function figure(o, { height = 1.78, px = 300, gap = 0.03 } = {}) {
  const g = new THREE.Group(), wM = height * 0.62, hM = height * 1.08, cw = Math.round(wM * px), ch = Math.round(hM * px), s = (height * px) / 800;
  LAYERS.forEach((only, li) => {
    const c = document.createElement('canvas'); c.width = cw; c.height = ch; const x = c.getContext('2d'); x.translate(cw / 2, ch - 6); x.scale(s, s);
    drawFigure(x, { ...o, style: 'paper', only }); paperGrain(x, cw, ch, 0.0);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
    const geo = bent(wM, hM, 0.025 + (li === 3 ? 0.02 : 0));
    const m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map: t, alphaTest: 0.5, roughness: 0.92 })); m.castShadow = m.receiveShadow = true;
    m.customDepthMaterial = new THREE.MeshDepthMaterial({ depthPacking: THREE.RGBADepthPacking, map: t, alphaTest: 0.5 });
    const back = new THREE.Mesh(geo, edgeMat.clone()); back.material.map = t; back.material.alphaTest = 0.5; back.material.color.set('#D9C9A8'); back.position.z = -0.006; back.material.side = THREE.BackSide;
    const L = new THREE.Group(); L.add(m, back); L.position.z = (li - 2) * gap; L.position.y = -6 / px; g.add(L);
  });
  return g;
}
function printed(w, h, pxPerM, draw, side = '#B8AC96', depth = 0.3) {
  const c = document.createElement('canvas'); c.width = Math.round(w * pxPerM); c.height = Math.round(h * pxPerM); draw(c.getContext('2d'), c.width, c.height);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  const face = new THREE.MeshStandardMaterial({ map: t, roughness: 0.95 });
  const b = foldBox(w, h, depth, side, { faces: { 4: face }, sag: 0.006 }); b.position.y = h / 2; const grp = new THREE.Group(); grp.add(b); return grp;   // nhóm: position.y của nhóm = mặt đất
}

export async function boot(res) {
  for (const f of ['700 48px Georgia', '800 48px Georgia', '600 48px Inter']) await document.fonts.load(f);
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true }); renderer.setPixelRatio(1); renderer.setSize(W, H);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(); scene.background = new THREE.Color('#2E3646'); scene.fog = new THREE.Fog('#2E3646', 26, 80);
  scene.add(new THREE.HemisphereLight('#B9C6DC', '#3A3026', 1.05));
  const key = new THREE.DirectionalLight('#D8E2F2', 1.7); key.position.set(-9, 14, 8); key.castShadow = true; key.shadow.mapSize.set(2048, 2048);
  Object.assign(key.shadow.camera, { left: -16, right: 16, top: 16, bottom: -8, near: 0.5, far: 60 }); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02; key.target.position.set(0, 0, -8); scene.add(key, key.target);
  const fill = new THREE.PointLight('#FFE2BA', 10, 18, 1.2); scene.add(fill);
  for (const x of [-6.5, 7.5]) { const post = roll(0.07, 4.2, '#2A2F38'); post.position.set(x, 2.1, -5.2); scene.add(post);
    const lan = foldBox(0.36, 0.5, 0.36, '#F6D58E', { sag: 0 }); [].concat(lan.material).forEach((m) => { m.emissive = new THREE.Color('#F2B441'); m.emissiveIntensity = 1.1; }); lan.position.set(x, 4.5, -5.2); scene.add(lan);
    const L = new THREE.PointLight('#FFD08A', 22, 12, 1.4); L.position.set(x, 4.3, -5.2); scene.add(L); }
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(90, 50), paperMat('#6A645C', { draw: (g, w, h) => pavement(g, w, h, { style: 'paper' }), key: 'pave', w: 1024, h: 512, rep: [9, 5] }));
  ground.rotation.x = -Math.PI / 2; ground.position.z = -8; ground.receiveShadow = true; scene.add(ground);
  // dãy phố: khối giấy gấp in mặt tiền 1930
  const SIGNS = [['LUNCH', '#8E3B33', 'shop'], ['HATS', '#3E5A4A', 'shop'], [null, null, 'office'], ['DRUGS', '#7A5A2E', 'shop']];
  for (let i = 0; i < 4; i++) { const left = i < 2, [sign, awn, kind] = SIGNS[i], h = 13 + (i % 2) * 3;
    const b = printed(9, h, 100, (g, w, hh) => facade(g, w, hh, { kind, sign, awning: awn, seed: i + 2, style: 'paper', fire: i === 1 || i === 3 }), '#8A6E58', 6);
    b.position.set(left ? -21.5 + (i % 2) * 9.2 : 12.3 + (i % 2) * 9.2, 0, -21 - (i % 2) * 1.5); scene.add(b); }
  // ngân hàng: mặt tiền in + cột cuộn + bậc gấp
  const bank = printed(17, 14, 110, (g, w, h) => bankFacade(g, w, h, { style: 'paper', columns: false }), '#BDB29C', 7); bank.position.set(-0.4, 0, -19.5); scene.add(bank);
  for (let i = 0; i < 6; i++) { if (i === 2 || i === 3) continue; const c = roll(0.42, 8.8, '#E2DACA'); c.position.set(-0.4 - 8.5 + 17 * (0.1 + i * 0.16), 1.0 + 4.4, -15.4); c.traverse((m) => { if (m.isMesh) m.castShadow = true; }); scene.add(c); }
  for (let i = 0; i < 4; i++) { const st = foldBox(17.4 - i * 0.5, 0.24, 2.6 - i * 0.5, '#B9B2A3', { sag: 0.01 }); st.position.set(-0.4, 0.12 + i * 0.24, -15.6 - i * 0.5); scene.add(st); }
  // đám đông 5 lớp
  const rows = [[-13.6, 11, 3, 0.0], [-11.4, 10, 5, 0.6], [-9.2, 9, 7, -0.4], [-7.0, 7, 9, 0.3]];
  for (const [z, n, seed, dx] of rows) crowdSpec(n, seed).forEach((o, i) => { const f = figure(o, { height: 1.78 * o.s }); f.position.set(dx - 7.5 + 15 * (i + 0.5) / n + ((i * 37) % 7 - 3) * 0.06, 0, z + ((i * 13) % 5) * 0.12); f.rotation.y = o.view === 'back' ? 0 : 0.1; scene.add(f); });
  const man = figure({ sex: 'm', skin: 'light', coat: 'charcoal', hat: 'fedora', expr: 'worried', pose: { L: 'clasp', R: 'clasp' } }, { height: 1.8, px: 520, gap: 0.035 });
  man.position.set(1.0, 0, -2.6); man.rotation.y = -0.6; scene.add(man);
  const cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 300);
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  function frame(t) {
    const K1 = t < 1;
    if (K1) { cam.position.set(-0.2, 1.72, -0.2); cam.fov = 34; cam.lookAt(2.2, 1.6, -10); man.visible = true; }
    else { cam.position.set(1.2, 2.3, 3.2); cam.fov = 46; cam.lookAt(0.0, 3.2, -16); man.visible = false; }
    cam.updateProjectionMatrix(); fill.position.set(cam.position.x + 0.5, cam.position.y + 1, cam.position.z + 0.5);
    renderer.render(scene, cam); ctx.drawImage(renderer.domElement, 0, 0); paperGrain(ctx, W, H, 0.1); vignette(ctx, W, H, 0.35);
    const s = W / 1920; ctx.save(); ctx.scale(s, s); const pill = (txt, x, y, px2, fg, bg, right) => { ctx.font = `600 ${px2}px Inter`; const pw = ctx.measureText(txt).width + px2 * 0.9, ph = px2 * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px2 * 0.45, y + ph / 2 + px2 * 0.04); };
    pill('December 1930', 96, 54, 48, '#F2F4F7', 'rgba(14,17,22,0.75)'); pill('ILLUSTRATIVE', 1824, 54, 40, '#0E1116', 'rgba(242,244,247,0.9)', true); ctx.restore();
    return { violations: [] };
  }
  return { canvas: out, frame };
}
