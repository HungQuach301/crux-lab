// Mốc V · Hướng B — "vật thể thật 3D": nhà của Rosa & Frank đứng trên chồng tiền (1 đơn vị thế giới = $100,000),
// vạch trần $500,000 là một thanh kính/thép cố định. Mọi trạng thái là hàm thuần của t (không đồng hồ, không ngẫu nhiên).
// ?house=code → nhà dựng bằng code; ?house=cc → obj_house1.dae (Mini Mike's Metro Minis, CC-BY-4.0, xem CREDITS.md).
import * as THREE from 'three';
import { ColladaLoader } from 'three/addons/loaders/ColladaLoader.js';
import { C, clamp, lin, ease, easeOut, easeBack, mix, rgba, loadAll, makeCtx, chrome, roundRect } from '../lib2d.js';

const W = 1920, H = 1080;
const U = 1e5;                      // $ trên một đơn vị thế giới
const BEAM_Y = 5;                   // $500,000
const PITCH = 0.25;                 // một xấp tiền = $25,000 → vạch trần = đúng 20 xấp, $200,000 = 8 xấp
const X = (q) => -7 + 14 * q / 105; // trục thời gian (q = quý 0..105)
const HOUSE_W = 1.6;
const easeIn = (t, a, b) => { const x = lin(t, a, b); return x * x * x; };

// ---------------------------------------------------------------- nhà
function codeHouse() {
  const g = new THREE.Group();
  const m = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, ...o });
  const w = HOUSE_W, d = 1.15, h = 0.95, roof = 0.72;
  const add = (mesh, x, y, z) => { mesh.position.set(x, y, z); mesh.castShadow = mesh.receiveShadow = true; g.add(mesh); return mesh; };
  add(new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m('#D9D4C7')), 0, h / 2, 0);
  const sh = new THREE.Shape(); sh.moveTo(-w / 2 - 0.1, 0); sh.lineTo(w / 2 + 0.1, 0); sh.lineTo(0, roof); sh.closePath();
  add(new THREE.Mesh(new THREE.ExtrudeGeometry(sh, { depth: d + 0.24, bevelEnabled: false }), m('#8A4B3A', { roughness: 0.7 })), 0, h, -d / 2 - 0.12);
  add(new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.42, 0.16), m('#6E4F3E')), w * 0.26, h + 0.42, -0.15);
  const win = m('#2B2F38', { emissive: new THREE.Color('#F6D58E'), emissiveIntensity: 0.9, roughness: 0.3 });
  for (const x of [-w * 0.29, w * 0.29]) {
    add(new THREE.Mesh(new THREE.BoxGeometry(0.34, 0.3, 0.04), m('#EDE6D6')), x, h * 0.58, d / 2 + 0.01);
    add(new THREE.Mesh(new THREE.BoxGeometry(0.27, 0.23, 0.03), win), x, h * 0.58, d / 2 + 0.03);
  }
  add(new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.5, 0.05), m('#3B4A5A')), 0, 0.25, d / 2 + 0.02);
  add(new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.06, 0.24), m('#8C8C88')), 0, 0.03, d / 2 + 0.12);
  return g;
}

async function ccHouse() {
  const url = '/moc-v/proto/vendor/node_modules/mmmm-models/collada/obj_house1.dae';
  const col = await new ColladaLoader().loadAsync(url);
  const inner = col.scene;
  inner.traverse((o) => {
    if (!o.isMesh) return;
    o.castShadow = o.receiveShadow = true;
    const ms = Array.isArray(o.material) ? o.material : [o.material];
    o.material = ms.map((mm) => {
      const s = new THREE.MeshStandardMaterial({ map: mm.map || null, color: mm.map ? 0xffffff : (mm.color || 0xcccccc), roughness: 0.85 });
      if (s.map) { s.map.magFilter = THREE.NearestFilter; s.map.minFilter = THREE.NearestFilter; s.map.generateMipmaps = false; s.map.colorSpace = THREE.SRGBColorSpace; }
      return s;
    });
    if (o.material.length === 1) o.material = o.material[0];
  });
  // chờ ảnh texture tải xong (ColladaLoader nạp ảnh bất đồng bộ) → khung đầu không thiếu nhà
  const imgs = [];
  inner.traverse((o) => { if (o.isMesh) for (const m of [].concat(o.material)) if (m.map && m.map.image) imgs.push(m.map); });
  for (let i = 0; i < 200 && imgs.some((t) => !(t.image.complete && t.image.naturalWidth > 0)); i++) await new Promise((r) => setTimeout(r, 25));
  for (const t of imgs) t.needsUpdate = true;
  inner.updateMatrixWorld(true);
  const box = new THREE.Box3().setFromObject(inner), size = box.getSize(new THREE.Vector3()), c = box.getCenter(new THREE.Vector3());
  const s = HOUSE_W / Math.max(size.x, size.z);
  const g = new THREE.Group(), pivot = new THREE.Group();
  pivot.add(inner); inner.position.set(-c.x, -box.min.y, -c.z); pivot.scale.setScalar(s);
  g.add(pivot);
  g.userData.ccRot = pivot;
  return g;
}

function cloneDeep(g) {
  const c = g.clone(true);
  c.traverse((o) => { if (o.isMesh) o.material = Array.isArray(o.material) ? o.material.map((m) => m.clone()) : o.material.clone(); });
  return c;
}
function setOpacity(g, a) {
  g.traverse((o) => {
    if (!o.isMesh) return;
    for (const m of Array.isArray(o.material) ? o.material : [o.material]) {
      m.transparent = true; m.opacity = a; m.depthWrite = a >= 0.999;
    }
    o.castShadow = a > 0.6;
  });
}

// ---------------------------------------------------------------- tiện ích
function glowTex() {
  const cv = document.createElement('canvas'); cv.width = cv.height = 128;
  const g = cv.getContext('2d'), gr = g.createRadialGradient(64, 64, 0, 64, 64, 64);
  gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(0.25, 'rgba(255,255,255,0.55)'); gr.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = gr; g.fillRect(0, 0, 128, 128);
  const t = new THREE.CanvasTexture(cv); t.colorSpace = THREE.SRGBColorSpace; return t;
}
function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

// ---------------------------------------------------------------- dựng cảnh
export async function boot(variant) {
  const D = await loadAll();
  const { cue, interp, gain, value, at } = D;
  const gainAt = (q) => at(gain, q), valueAt = (q) => at(value, q);

  const gl = document.createElement('canvas'); gl.width = W; gl.height = H;
  const renderer = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(1); renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  const out = document.createElement('canvas'); document.body.appendChild(out);
  const K = makeCtx(out), ctx = K.ctx;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(C.bg);
  scene.fog = new THREE.Fog(C.bg, 26, 62);
  const camera = new THREE.PerspectiveCamera(35, W / H, 0.1, 200);

  // ánh sáng studio
  scene.add(new THREE.HemisphereLight('#C9D6EA', '#1A1F27', 0.9));
  const key = new THREE.DirectionalLight('#FFF1DC', 2.4); key.position.set(-6, 14, 10); key.castShadow = true;
  key.shadow.mapSize.set(1024, 1024); Object.assign(key.shadow.camera, { left: -14, right: 14, top: 14, bottom: -4, near: 1, far: 50 });
  key.shadow.bias = -0.0008; key.target.position.set(0, 3, 0); scene.add(key, key.target);
  const rim = new THREE.DirectionalLight('#8FB4FF', 0.7); rim.position.set(6, 6, -10); scene.add(rim);

  // sàn studio
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(120, 120), new THREE.MeshStandardMaterial({ color: '#171C24', roughness: 0.95 }));
  floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; scene.add(floor);

  // trục năm trên sàn (vạch mảnh trước chồng tiền)
  const axisMat = new THREE.MeshBasicMaterial({ color: '#4A5363', transparent: true });
  const axis = new THREE.Group(); scene.add(axis);
  const axLine = new THREE.Mesh(new THREE.BoxGeometry(14.2, 0.015, 0.03), axisMat); axLine.position.set(0, 0.01, 1.05); axis.add(axLine);
  for (let yr = 0; yr <= 26; yr++) {
    const tk = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.015, yr % 10 === 0 ? 0.35 : 0.18), axisMat);
    tk.position.set(X(yr * 4), 0.012, 1.05 + (yr % 10 === 0 ? 0.17 : 0.09)); axis.add(tk);
  }

  // ---- nhà chính
  const hero = variant === 'cc' ? await ccHouse() : codeHouse();
  setOpacity(hero, 1);   // vật liệu luôn transparent (đổi cờ transparent cần biên dịch lại shader) → chỉ đổi opacity
  scene.add(hero);
  const twin = cloneDeep(hero);           // nhà năm 2000 ở b11 (dùng chung vật liệu; lúc đó hero đặc)
  scene.add(twin);
  // khu phố: 14 nhà nhỏ có biển SOLD (cùng kiểu nhà)
  const R = rng(7), hood = [];
  const tagMat = new THREE.MeshStandardMaterial({ color: '#F4F1EA', roughness: 0.6 }), tagBand = new THREE.MeshStandardMaterial({ color: '#C72323', roughness: 0.6 }), postMat = new THREE.MeshStandardMaterial({ color: '#8C8C88' });
  const ticks = D.spine.events.filter((e) => e.kind === 'tick' && e.t < 14).map((e) => e.t);
  for (let i = 0; i < ticks.length; i++) {
    const g = new THREE.Group(), h = cloneDeep(hero); h.scale.setScalar(0.5); g.add(h);
    const post = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.55, 0.03), postMat); post.position.set(0.62, 0.27, 0.45); g.add(post);
    const tag = new THREE.Mesh(new THREE.BoxGeometry(0.42, 0.24, 0.03), tagMat); tag.position.set(0.62, 0.5, 0.47); g.add(tag);
    const band = new THREE.Mesh(new THREE.BoxGeometry(0.42, 0.07, 0.035), tagBand); band.position.set(0.62, 0.55, 0.47); g.add(band);
    const col = i % 5, row = Math.floor(i / 5);
    g.position.set(-10.6 + col * 2.05 + (R() - 0.5) * 0.6 + (row % 2) * 0.9, 0, -4.2 - row * 2.2 + (R() - 0.5) * 0.5);
    g.rotation.y = (R() - 0.5) * 0.5;
    g.traverse((o) => { if (o.isMesh) o.castShadow = o.receiveShadow = true; });
    scene.add(g); hood.push({ g, t: ticks[i], base: g.position.clone() });
  }
  // nền khu phố (đường phố mảnh)
  const district = new THREE.Group(); scene.add(district);
  const dMat = new THREE.MeshStandardMaterial({ color: '#1E242E', roughness: 0.95, transparent: true });
  const dPlane = new THREE.Mesh(new THREE.PlaneGeometry(12.5, 8), dMat); dPlane.rotation.x = -Math.PI / 2; dPlane.position.set(-6.2, 0.005, -7.0); dPlane.receiveShadow = true; district.add(dPlane);
  const stMat = new THREE.MeshBasicMaterial({ color: '#2E3644', transparent: true });
  for (const z of [-5.3, -7.5, -9.7]) { const s = new THREE.Mesh(new THREE.PlaneGeometry(12.5, 0.18), stMat); s.rotation.x = -Math.PI / 2; s.position.set(-6.2, 0.01, z); district.add(s); }

  // Rosa & Frank: hai hình người không mặt
  const figs = new THREE.Group(); scene.add(figs);
  const mkFig = (color, hgt, x) => {
    const g = new THREE.Group(), m = new THREE.MeshStandardMaterial({ color, roughness: 0.7, transparent: true });
    const body = new THREE.Mesh(new THREE.CapsuleGeometry(0.2, hgt * 0.45, 6, 14), m); body.position.y = hgt * 0.42; body.castShadow = true; g.add(body);
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.15, 20, 14), m); head.position.y = hgt * 0.42 + hgt * 0.225 + 0.32; head.castShadow = true; g.add(head);
    g.position.set(x, 0, 0.9); g.userData.x0 = x; figs.add(g); figG.push(g); return m;
  };
  const figG = [];
  const figMats = [mkFig('#E7B9A0', 1.05, -5.55), mkFig('#AFC3DA', 1.15, -4.95)];

  // chồng tiền (instanced): xấp + đai giấy
  const NB = 44;
  const bundle = new THREE.InstancedMesh(new THREE.BoxGeometry(1.25, 1, 0.8), new THREE.MeshStandardMaterial({ color: '#ffffff', roughness: 0.8 }), NB);
  const strap = new THREE.InstancedMesh(new THREE.BoxGeometry(0.24, 1, 0.82), new THREE.MeshStandardMaterial({ color: '#ffffff', roughness: 0.7 }), NB);
  bundle.castShadow = bundle.receiveShadow = strap.castShadow = true;
  bundle.material.transparent = strap.material.transparent = true;
  bundle.frustumCulled = strap.frustumCulled = false;   // hộp bao instanced chỉ tính một lần → tắt cull
  scene.add(bundle, strap);
  const cMoney = new THREE.Color('#5F8A63'), cStrap = new THREE.Color('#E9E2CC'), cWarn = new THREE.Color(C.warn), cAcc = new THREE.Color(C.accent);
  const tmpM = new THREE.Matrix4(), tmpC = new THREE.Color();

  // vạch trần: thanh kính + lõi sáng (106 đoạn để chạy xung "mọi quý như nhau")
  const beam = new THREE.Group(); scene.add(beam);
  const glassMat = new THREE.MeshStandardMaterial({ color: '#CFD8E3', roughness: 0.15, metalness: 0.3, transparent: true, opacity: 0.32, depthWrite: false });
  const glass = new THREE.Mesh(new THREE.BoxGeometry(16.6, 0.16, 0.9), glassMat); beam.add(glass);
  const capMat = new THREE.MeshStandardMaterial({ color: '#8E99A8', roughness: 0.35, metalness: 0.7, transparent: true });
  for (const x of [-8.35, 8.35]) { const cap = new THREE.Mesh(new THREE.BoxGeometry(0.14, 0.3, 1.0), capMat); cap.position.x = x; cap.castShadow = true; beam.add(cap); }
  const NS = 106;
  const core = new THREE.InstancedMesh(new THREE.BoxGeometry(16.6 / NS * 0.92, 0.045, 0.05), new THREE.MeshBasicMaterial({ color: '#ffffff', transparent: true }), NS);
  for (let i = 0; i < NS; i++) { tmpM.makeTranslation(-8.3 + 16.6 * (i + 0.5) / NS, 0, 0.47); core.setMatrixAt(i, tmpM); }
  core.frustumCulled = false; beam.add(core);
  // tấm "dưới vạch" (b5), màu cushion rất nhạt
  const underMat = new THREE.MeshBasicMaterial({ color: C.cushion, transparent: true, opacity: 0, depthWrite: false });
  const under = new THREE.Mesh(new THREE.PlaneGeometry(16.6, BEAM_Y), underMat); under.position.set(0, BEAM_Y / 2, -1.1); scene.add(under);
  // cột mốc Q2 2022
  const markMat = new THREE.MeshBasicMaterial({ color: C.warn, transparent: true, opacity: 0 });
  const mark = new THREE.Mesh(new THREE.BoxGeometry(0.03, BEAM_Y, 0.03), markMat); mark.position.set(X(89), BEAM_Y / 2, -0.75); scene.add(mark);

  // vệt sáng (ribbon) giá trị / lãi theo thời gian
  const MAXP = 120;
  const tPos = new Float32Array(MAXP * 2 * 3), tCol = new Float32Array(MAXP * 2 * 3), idx = [];
  for (let i = 0; i < MAXP - 1; i++) { const a = 2 * i; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  const trailGeo = new THREE.BufferGeometry();
  trailGeo.setAttribute('position', new THREE.BufferAttribute(tPos, 3)); trailGeo.setAttribute('color', new THREE.BufferAttribute(tCol, 3)); trailGeo.setIndex(idx);
  const trailMat = new THREE.MeshBasicMaterial({ vertexColors: true, transparent: true, side: THREE.DoubleSide, toneMapped: false });
  const trail = new THREE.Mesh(trailGeo, trailMat); trail.frustumCulled = false; scene.add(trail);
  // bóng của đường giá trị ở chỗ cũ trong lúc trừ $200,000 (b4): thấy được khoảng rơi
  const gPos = new Float32Array(MAXP * 6), gCol = new Float32Array(MAXP * 6), ghostGeo = new THREE.BufferGeometry();
  ghostGeo.setAttribute('position', new THREE.BufferAttribute(gPos, 3)); ghostGeo.setAttribute('color', new THREE.BufferAttribute(gCol, 3)); ghostGeo.setIndex(idx);
  const ghostMat = new THREE.MeshBasicMaterial({ vertexColors: true, transparent: true, side: THREE.DoubleSide, toneMapped: false });
  const ghostTrail = new THREE.Mesh(ghostGeo, ghostMat); ghostTrail.frustumCulled = false; scene.add(ghostTrail);
  function ribbon(geo, pos, col, pts) {
    let n = 0;
    for (const [x, y, c] of pts) {
      if (n >= MAXP) break;
      const prev = pts[Math.max(0, n - 1)], next = pts[Math.min(pts.length - 1, n + 1)];
      let dx = next[0] - prev[0], dy = next[1] - prev[1]; const L = Math.hypot(dx, dy) || 1; dx /= L; dy /= L;
      const w = 0.045;
      pos.set([x + dy * w, y - dx * w, TZ, x - dy * w, y + dx * w, TZ], n * 6);
      col.set([c.r, c.g, c.b, c.r, c.g, c.b], n * 6);
      n++;
    }
    geo.setDrawRange(0, Math.max(0, (n - 1) * 6)); geo.attributes.position.needsUpdate = geo.attributes.color.needsUpdate = true;
    return n;
  }
  const TZ = -0.7;
  const XT = (q) => X(q) - 0.68;   // vệt đi sát mép trái chồng tiền → đầu vệt luôn thấy được

  // điểm sáng (chỉ số trung bình / đầu vệt / tia ở điểm cắt)
  const gt = glowTex();
  const mkGlow = (color) => { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: gt, color, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false, toneMapped: false })); scene.add(s); return s; };
  const orb = mkGlow(C.accent), spark = mkGlow(C.warn);
  const orbCore = new THREE.Mesh(new THREE.SphereGeometry(0.12, 20, 14), new THREE.MeshBasicMaterial({ color: '#BFD5FF', transparent: true, toneMapped: false })); scene.add(orbCore);

  // lịch treo tường: bảng + trang (texture năm), một trang lật
  const cal = new THREE.Group(); cal.position.set(-2.6, 8.3, -2.6); scene.add(cal);
  const calBoard = new THREE.Mesh(new THREE.BoxGeometry(2.5, 2.3, 0.08), new THREE.MeshStandardMaterial({ color: '#2E3440', roughness: 0.8 })); calBoard.castShadow = true; cal.add(calBoard);
  const texCache = {};
  const pageTex = (key) => {
    if (texCache[key]) return texCache[key];
    const cv = document.createElement('canvas'); cv.width = 512; cv.height = 448; const g = cv.getContext('2d');
    g.fillStyle = '#F4F1EA'; g.fillRect(0, 0, 512, 448);
    g.fillStyle = '#3B4A5A'; g.fillRect(0, 0, 512, 70);
    g.fillStyle = '#F4F1EA'; for (const x of [130, 382]) { g.beginPath(); g.arc(x, 35, 13, 0, 7); g.fill(); }
    const [yr, qq] = key.split(' ');
    g.fillStyle = '#0E1116'; g.font = '700 190px Inter'; g.textAlign = 'center'; g.textBaseline = 'alphabetic';
    g.fillText(yr, 256, qq ? 300 : 330);
    if (qq) { g.font = '700 96px Inter'; g.fillStyle = '#3B4A5A'; g.fillText(qq, 256, 410); }
    const t = new THREE.CanvasTexture(cv); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; texCache[key] = t; return t;
  };
  const pageGeo = new THREE.PlaneGeometry(2.3, 2.0); pageGeo.translate(0, -1.0, 0);
  const pageA = new THREE.Mesh(pageGeo, new THREE.MeshStandardMaterial({ roughness: 0.9 })); pageA.position.set(0, 1.0, 0.05); cal.add(pageA);
  const pageB = new THREE.Mesh(pageGeo, new THREE.MeshStandardMaterial({ roughness: 0.9, side: THREE.DoubleSide })); pageB.position.set(0, 1.0, 0.07); cal.add(pageB);
  for (let y = 2000; y <= 2026; y++) pageTex(String(y)); pageTex('2026 Q2');

  // ------------------------------------------------------------ máy quay (khoá theo t, nội suy smoothstep)
  const A0 = { p: [-5.0, 3.9, 12.0], l: [-6.2, 2.95, 0] }, A1 = { p: [-5.3, 3.8, 11.0], l: [-6.3, 2.95, 0] };
  const Bn = { p: [-2.6, 6.0, 12.5], l: [-5.6, 2.0, -3.4] };
  const Wd = { p: [0, 6.2, 21.2], l: [0, 4.46, 0] };
  const W4 = { p: [0.8, 6.2, 20.6], l: [0.8, 4.46, 0] };
  const Rd = { p: [0, 5.0, 18.6], l: [0, 3.7, 0] };
  const R2 = { p: [0.8, 5.0, 18.4], l: [0.8, 3.8, 0] };
  const Nn = { p: [3.4, 5.9, 10.4], l: [5.4, 5.4, 0] };
  const Pp = { p: [4.4, 5.6, 7.8], l: [5.6, 5.3, 0] };
  const T1 = { p: [5.6, 2.9, 11.5], l: [5.6, 1.9, 0] };
  const T2 = { p: [5.6, 4.7, 18.0], l: [5.6, 3.65, 0] };
  const shots = [[0, A0], [4.7, A1], [5.1, A1], [7.6, Bn], [14.6, Bn], [16.9, Wd], [28.9, Wd], [32.5, W4], [38.9, W4], [40.5, Rd], [46.5, Rd], [50.0, R2], [55.2, R2], [59.4, Nn], [61.25, Nn], [62.3, Pp], [62.8, Pp], [63.75, T2]];
  function setCam(t) {
    let a = shots[0], b = shots[0];
    for (let i = 0; i < shots.length; i++) { if (shots[i][0] <= t) { a = shots[i]; b = shots[Math.min(i + 1, shots.length - 1)]; } }
    const x = a === b ? 0 : ease(t, a[0], b[0]);
    const p = a[1].p.map((v, i) => mix(v, b[1].p[i], x)), l = a[1].l.map((v, i) => mix(v, b[1].l[i], x));
    // rung nhẹ khi vạch khoá (23.71) và va chạm (61.958)
    let sh = 0; for (const [ti, amp] of [[cue.b3.cap + 0.35, 0.09], [cue.b10.past, 0.05]]) { const k = t - ti; if (k > 0 && k < 0.45) sh += amp * Math.sin(k * 55) * (1 - k / 0.45); }
    camera.position.set(p[0], p[1] + sh, p[2]); camera.lookAt(l[0], l[1] + sh * 0.6, l[2]);
    camera.updateMatrixWorld(); camera.updateProjectionMatrix();
  }
  const V = new THREE.Vector3();
  const P = (x, y, z) => { V.set(x, y, z).project(camera); return { x: (V.x + 1) / 2 * W, y: (1 - V.y) / 2 * H }; };

  // ------------------------------------------------------------ trạng thái theo t
  const DRAW0 = D.spine.draw[0][0], DRAW1 = D.spine.draw[1][0];
  const RIDE0 = D.spine.ride[0][0], RIDE1 = D.spine.ride[D.spine.ride.length - 1][0];
  const CROSS = cue.b6.cross, B11 = cue.b11.t0, RISE = cue.b11.x;
  const LESS = cue.b4.less, SLIDE0 = LESS, SLIDE1 = SLIDE0 + 0.7, DROP1 = SLIDE0 + 1.6;   // rút $200,000 bắt đầu đúng cue less
  const REW0 = cue.b5.t0 - 0.75, REW1 = cue.b5.t0 + 0.15;   // trượt ngược theo đường lãi, không nhảy
  const GROW0 = 63.8, HIDE0 = B11, HIDE1 = B11 + 0.4;
  
  function state(t) {
    const s = {};
    // q hiện tại (lịch + vị trí nhà)
    if (t < DRAW0) s.q = 0;
    else if (t < REW0) s.q = interp(D.spine.draw, t);
    else if (t < RIDE0) s.q = 105 * (1 - ease(t, REW0, REW1));
    else s.q = interp(D.spine.ride, t);
    s.phase = t < LESS ? 'value' : t < REW0 ? 'drop' : 'gain';
    s.drop = 2 * mix(0, 1, Math.pow(lin(t, SLIDE1, DROP1), 2));                      // $200,000 = 2 đơn vị
    if (s.phase === 'value') s.H = valueAt(s.q) / U;
    else if (s.phase === 'drop') s.H = valueAt(105) / U - s.drop;
    else {
      s.H = Math.max(0, gainAt(s.q) / U);
      // chạm vạch đúng khung "crosses" rồi đẩy xuyên qua
      const g88 = gainAt(88) / U;
      if (t >= 46.98 && t < CROSS) s.H = mix(g88, BEAM_Y, ease(t, 46.98, CROSS));
      else if (t >= CROSS && t < CROSS + 0.35) s.H = mix(BEAM_Y, gainAt(s.q) / U, easeOut(t, CROSS, CROSS + 0.35));
    }
    // b10: chồng tiền nảy lên xuyên vạch đúng "past"
    if (t >= cue.b10.past && t < cue.b10.past + 0.6) s.H += 0.28 * Math.sin(Math.PI * lin(t, cue.b10.past, cue.b10.past + 0.6));
    // b11: chồng tiền chìm xuống sàn
    s.sink = ease(t, B11, B11 + 0.7);
    s.H *= 1 - s.sink;
    s.x = X(s.q);
    s.over = s.phase === 'gain' && s.H > BEAM_Y + 0.001;
    return s;
  }

  function updateScene(t) {
    const s = state(t);
    setCam(t);
    // ---- chồng tiền
    const slabDx = -2.1 * easeOut(t, SLIDE0, SLIDE1), slabZ = 0.0, slabGone = ease(t, 40.0, 40.5);
    let k = 0;
    const put = (y0, hgt, x, col, scl = 1) => {
      if (k >= NB || hgt <= 0.01 || scl <= 0.01) return;
      tmpM.compose(V.set(x, y0 + hgt / 2, 0), new THREE.Quaternion(), new THREE.Vector3(scl, hgt, scl)); bundle.setMatrixAt(k, tmpM); bundle.setColorAt(k, col);
      tmpM.compose(V.set(x, y0 + hgt / 2, 0), new THREE.Quaternion(), new THREE.Vector3(scl, hgt + 0.004, scl)); strap.setMatrixAt(k, tmpM); strap.setColorAt(k, cStrap);
      k++;
    };
    const hl = ease(t, 33.94, 34.4) * (1 - ease(t, 38.9, 39.3));  // xấp $200,000 sáng lên ("the two hundred thousand dollars")
    if (s.phase === 'drop' || (s.phase === 'value' && t > 30)) {
      // 8 xấp đáy = $200,000 đã trả, phần trên rơi xuống sau khi rút ra
      for (let i = 0; i < 8; i++) put(i * PITCH, PITCH - 0.03, s.x + slabDx, tmpC.copy(cMoney).lerp(cAcc, 0.55 * hl), 1 - slabGone);
      const top = s.H + (s.phase === 'drop' ? s.drop : 0);   // chiều cao trước khi rơi
      for (let i = 8; i * PITCH < top - 0.001; i++) { const y0 = i * PITCH, hh = Math.min(PITCH - 0.03, top - y0 - 0.005); put(y0 - (s.phase === 'drop' ? s.drop : 0), hh, s.x, cMoney); }
    } else {
      for (let i = 0; i * PITCH < s.H - 0.001; i++) {
        const y0 = i * PITCH, hh = Math.min(PITCH - 0.03, s.H - y0 - 0.005);
        const warn = s.phase === 'gain' && y0 >= BEAM_Y - 1e-6;
        put(y0, hh, s.x, warn ? cWarn : cMoney);
      }
    }
    bundle.count = strap.count = k;
    bundle.instanceMatrix.needsUpdate = strap.instanceMatrix.needsUpdate = true;
    if (bundle.instanceColor) bundle.instanceColor.needsUpdate = true; if (strap.instanceColor) strap.instanceColor.needsUpdate = true;
    const ghost = ease(t, cue.b1.blur, cue.b1.blur + 0.8) * (1 - ease(t, DRAW0, cue.b2.y2000));
    bundle.material.opacity = 1 - 0.6 * ghost; bundle.material.depthWrite = ghost < 0.001; strap.material.opacity = bundle.material.opacity; strap.material.depthWrite = bundle.material.depthWrite;

    // ---- nhà chính
    const rise = easeOut(t, GROW0, RISE);   // b11: cao ×3.79, xong đúng cue x
    const growth = D.data.claims.growth_phoenix.value;
    hero.position.set(t >= B11 ? mix(s.x, X(105), 1) : s.x, s.H, 0);
    hero.scale.set(1, 1 + (growth - 1) * rise, 1);
    setOpacity(hero, 1 - 0.78 * ghost);
    // nhà 2000 (b11)
    const tw = easeBack(t, 63.75, 64.15);
    twin.visible = t > 63.75; twin.position.set(4.0, 0, 0); twin.scale.setScalar(Math.max(0.001, tw));
    // ---- Rosa & Frank
    // b0 ở sàn; từ b9 đứng trên vạch cạnh chồng tiền (con số là của họ); b11 đứng cạnh nhà hôm nay
    let fa = 1 - ease(t, cue.b1.blur, cue.b1.blur + 0.6), fy = 0, fsc = 1, fx = (g) => g.userData.x0, fz = 0.9;
    if (t >= cue.b9.t0 && t < B11 + 0.3) { fa = ease(t, cue.b9.t0, cue.b9.t0 + 0.5) * (1 - ease(t, B11, B11 + 0.3)); fy = BEAM_Y + 0.08; fsc = 0.62; fx = (g) => X(105) - 1.05 - (g.userData.x0 + 4.95) * -0.75 - 0.45; fz = 0.25; }
    else if (t >= B11 + 0.3) { fa = ease(t, 63.6, 64.0); fy = 0; fsc = 1; fx = (g) => X(105) + 1.55 + (g.userData.x0 + 5.55) * 1.0; fz = 0.6; }
    figs.visible = fa > 0.01; for (const m of figMats) m.opacity = fa;
    for (const g of figG) { g.position.set(fx(g), fy, fz); g.scale.setScalar(fsc); }
    // ---- khu phố
    for (const h of hood) {
      const pop = easeBack(t, h.t - 0.05, h.t + 0.3), gat = ease(t, cue.b1.avg, cue.b1.avg + 0.55);
      const sc = pop * (1 - gat);
      h.g.visible = sc > 0.01; h.g.scale.setScalar(Math.max(0.001, sc));
      h.g.position.lerpVectors(h.base, V.set(-5.6, 3.6, -6.4), gat);
    }
    const da = ease(t, 6.0, 7.6) * (1 - ease(t, 15.4, 16.6));
    district.visible = da > 0.01; dMat.opacity = da; stMat.opacity = da;
    // ---- quả cầu chỉ số: gom ở P, bay vào đỉnh chồng tiền, rồi thành đầu vệt
    const gAt = V.set(-5.6, 3.6, -6.4).clone();
    let orbA = 0, orbPos = gAt, orbS = 0;
    if (t >= cue.b1.avg) {
      orbA = ease(t, cue.b1.avg + 0.1, cue.b1.avg + 0.5); orbS = 0.9 + 0.4 * ease(t, cue.b1.avg + 0.3, cue.b1.avg + 0.6);
      const fly = ease(t, 14.95, 15.6);
      orbPos = gAt.clone().lerp(new THREE.Vector3(s.x - 0.68, s.H, TZ), fly);
      if (t > 15.6) orbPos = new THREE.Vector3(s.x - 0.68, s.H, TZ);
      if (t > 15.6) orbS = 0.75;
      orbA *= 1 - ease(t, HIDE0, HIDE1);
    }
    orb.position.copy(orbPos); orb.scale.setScalar(orbS * 1.4); orb.material.opacity = orbA * 0.9;
    orbCore.position.copy(orbPos); orbCore.material.opacity = orbA; orbCore.visible = orbA > 0.01;
    orb.visible = orbA > 0.01;

    // ---- vạch trần
    const hint = ease(t, cue.b0.cap_hint, cue.b0.cap_hint + 0.8) * (1 - ease(t, cue.b1.blur, cue.b1.blur + 0.6));
    const dropB = easeIn(t, cue.b3.cap, cue.b3.cap + 0.35);
    let by = BEAM_Y, ba = 0;
    if (t < cue.b3.cap) { by = BEAM_Y; ba = hint * 0.45; }
    else { by = mix(13, BEAM_Y, dropB) + (t > cue.b3.cap + 0.35 ? 0.06 * Math.sin((t - cue.b3.cap - 0.35) * 30) * Math.max(0, 1 - (t - cue.b3.cap - 0.35) / 0.3) : 0); ba = 1; }
    ba *= 1 - ease(t, HIDE0, HIDE1);
    beam.position.y = by; beam.visible = ba > 0.01;
    glassMat.opacity = 0.32 * ba; capMat.opacity = ba; capMat.transparent = ba < 0.999; core.material.opacity = ba;
    // lõi: xung chạy dọc (mọi quý như nhau) + màu warn khi lãi ở trên
    const overGlow = s.over ? clamp((s.H - BEAM_Y) / 0.15) : 0;
    const flatK = t >= cue.b3.flat && t < cue.b3.flat + 2.2 ? (t - cue.b3.flat) / 1.6 : -1;
    for (let i = 0; i < NS; i++) {
      const u = i / (NS - 1);
      let c = tmpC.set(t < cue.b3.cap ? C.warn : '#E8EEF6');
      if (flatK >= 0) { const d = Math.abs(u - flatK); c = c.clone().lerp(cAcc, clamp(1 - d / 0.08) * 0.9); }
      const near = Math.abs(X(s.q) - (-8.3 + 16.6 * u)) < 1.1;
      if (overGlow > 0 && near) c = c.clone().lerp(cWarn, overGlow);
      core.setColorAt(i, c);
    }
    core.instanceColor.needsUpdate = true;
    // tia ở điểm cắt
    const sp = Math.max(t >= CROSS ? Math.exp(-(t - CROSS) * 2.2) : 0, t >= cue.b10.past ? Math.exp(-(t - cue.b10.past) * 2.5) * (t < B11 ? 1 : 0) : 0, t >= 51.41 && t < 53 ? Math.exp(-(t - 51.41) * 3) * 0.6 : 0);
    spark.visible = sp > 0.02; spark.position.set(s.x, BEAM_Y, 0.5); spark.scale.setScalar(1.2 + 2.4 * sp); spark.material.opacity = sp;
    // tấm dưới vạch, cột mốc
    underMat.opacity = 0.09 * ease(t, cue.b5.under - 0.3, cue.b5.under + 0.3) * (1 - ease(t, 55, 56.5));
    markMat.opacity = 0.7 * ease(t, cue.b6.q, cue.b6.q + 0.4) * (1 - ease(t, 49.5, 50.5));
    // ---- trục năm
    const axA = ease(t, 15.4, 16.6) * (1 - ease(t, 55.0, 55.6)); axis.visible = axA > 0.01; axisMat.opacity = axA;
    // ---- vệt
    const pts = trailPoints(t, s);
    const n = ribbon(trailGeo, tPos, tCol, pts);
    // bóng đường giá trị ở chỗ cũ trong lúc trừ (less → hết b4)
    const gA = ease(t, LESS, LESS + 0.3) * (1 - ease(t, 40.0, 40.5));
    ghostTrail.visible = gA > 0.01; ghostMat.opacity = gA;
    if (ghostTrail.visible) { const gp = []; for (let q = 0; q <= 105; q++) gp.push([XT(q), value[q] / U, cGhost]); ribbon(ghostGeo, gPos, gCol, gp); }
    trailMat.opacity = 1 - ease(t, HIDE0, HIDE1); trail.visible = n > 1 && trailMat.opacity > 0.01;
    // ---- lịch
    const year = 2000 + Math.floor(s.q / 4 + 1e-6), fr = s.q / 4 - Math.floor(s.q / 4 + 1e-6);
    const keyNow = s.q >= 104.5 ? '2026 Q2' : String(Math.min(2026, year));
    pageA.material.map = pageTex(keyNow); pageA.material.needsUpdate = true;
    const flip = year > 2000 ? clamp(fr / 0.2) : 1;
    pageB.visible = flip < 1 && t > DRAW0; pageB.material.map = pageTex(String(year - 1)); pageB.material.needsUpdate = true;
    pageB.rotation.x = -Math.PI * 0.49 * ease(flip, 0, 1);
    const ca = ease(t, 15.2, 16.4) * (1 - ease(t, 55.0, 55.6)) * (1 - ease(t, cue.b4.gain - 0.3, cue.b4.gain) * (1 - ease(t, REW0, REW0 + 0.3))); cal.visible = ca > 0.01;
    return s;
  }

  const cVal = new THREE.Color(C.accent), cDim = new THREE.Color('#38414F'), cBg = new THREE.Color(C.bg), cGhost = new THREE.Color(C.accent).lerp(new THREE.Color(C.bg), 0.7);
  function trailPoints(t, s) {
    const pts = [];
    if (t < DRAW0) return pts;
    if (t < REW0) {
      // giá trị nhà (b2–b4), rơi đúng $200,000 ở b4
      // từ lúc vạch khoá tới "grown": đường giá trị mờ còn ~25 % (đừng đọc thành "giá trị nhà vượt trần");
      // ở "grown" độ sáng quét từ 2000 sang phải
      const qe = s.q, off = s.phase === 'drop' ? s.drop : 0;
      const vd = 0.75 * ease(t, cue.b3.cap + 0.35, cue.b3.cap + 0.8), sw = lin(t, cue.b4.grow, cue.b4.grow + 1.2) * 1.1 - 0.05;
      const cq = (q) => (vd > 0 && q / 105 > sw ? cVal.clone().lerp(cBg, vd) : cVal);
      for (let q = 0; q < qe; q++) pts.push([XT(q), value[q] / U - off, cq(q)]);
      pts.push([XT(qe), valueAt(qe) / U - off, cq(qe)]);
      return pts;
    }
    // đường lãi: phần đã đi sáng, phần chưa đi mờ; trên vạch = warn
    const qe = s.q, dimOld = 0.85 * ease(t, 55.5, 57.0), ahead = ease(t, RIDE0, RIDE0 + 0.6);
    for (let q = 0; q <= 105; q++) {
      if (q > qe && q - 1 < qe) pts.push([XT(qe), s.H, colFor(s.H, true)]);
      const y = Math.max(0, gain[q] / U), lit = q <= qe;
      let c = lit ? colFor(y, true) : cVal.clone().lerp(cDim, ahead);
      if (q < 88 && dimOld > 0) c = c.clone().lerp(cDim, dimOld);   // b9–b10: phần cũ lùi lại, không cắt qua chân trang
      pts.push([XT(q), y, c]);
    }
    return pts;
  }
  const colFor = (y, lit) => (y > BEAM_Y + 0.001 ? cWarn : cVal);

  // ------------------------------------------------------------ lớp chữ 2D (sắc, ≥ 40 px)
  const label = (s, x, y, px, o = {}) => K.text(s, x, y, px, { plate: C.bg, plateA: 0.72, ...o });
  function bracket(x, y0, y1, color, a, side = 1, lw = 5) {
    if (a <= 0.01) return;
    ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(x - 16 * side, y0); ctx.lineTo(x, y0); ctx.lineTo(x, y1); ctx.lineTo(x - 16 * side, y1); ctx.stroke(); ctx.restore();
  }
  function overlay(t, s) {
    const CL = D.CL;
    // b0: Rosa & Frank, dấu hỏi
    const fa = ease(t, 0.3, 0.9) * (1 - ease(t, cue.b1.blur, cue.b1.blur + 0.5));
    { const p = P(-5.25, 1.75, 0.9); label('Rosa & Frank', p.x, p.y - 24, 44, { align: 'center', alpha: fa, w: 600 }); }
    const qa = easeBack(t, cue.b0.q, cue.b0.q + 0.4) * (1 - ease(t, cue.b1.blur, cue.b1.blur + 0.4));
    if (qa > 0.01) { const p = P(X(0), (s.H + 2.1 + BEAM_Y) / 2 + 0.45, 0); K.text('?', p.x, p.y + 40, 140 * Math.max(0.3, qa), { w: 700, color: C.warn, align: 'center', alpha: clamp(qa) }); }
    // b1 "rise": mũi tên giá trị đi lên cạnh chồng tiền mờ
    const ra = ease(t, cue.b1.rise, cue.b1.rise + 0.25) * (1 - ease(t, 12.6, 13.1));
    if (ra > 0.01) {
      const g = easeOut(t, cue.b1.rise, cue.b1.rise + 1.2), b0 = P(X(0) + 1.0, 0.3, 0.6), b1 = P(X(0) + 1.0, mix(0.3, 3.4, g), 0.6);
      ctx.save(); ctx.globalAlpha = ra; ctx.strokeStyle = C.accent; ctx.fillStyle = C.accent; ctx.lineWidth = 8; ctx.lineCap = 'round';
      ctx.beginPath(); ctx.moveTo(b0.x, b0.y); ctx.lineTo(b1.x, b1.y + 10); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(b1.x, b1.y - 14); ctx.lineTo(b1.x - 20, b1.y + 16); ctx.lineTo(b1.x + 20, b1.y + 16); ctx.closePath(); ctx.fill(); ctx.restore();
      label('value rises with the index', b1.x + 30, b1.y + 20, 44, { color: C.accent, alpha: ra * ease(t, cue.b1.rise + 0.2, cue.b1.rise + 0.5) });
    }
    // b1: Phoenix area, many sales, average
    const hoodLbl = P(-6.0, 2.2, -9.5);
    label('Phoenix area', hoodLbl.x, hoodLbl.y - 10, 44, { align: 'center', color: C.muted, alpha: ease(t, 8.98, 9.4) * (1 - ease(t, 13.0, 13.45)) });
    label('many sales', hoodLbl.x, hoodLbl.y - 10, 44, { align: 'center', alpha: ease(t, cue.b1.many, cue.b1.many + 0.3) * (1 - ease(t, cue.b1.avg + 0.2, cue.b1.avg + 0.5)) });
    { const p = P(-5.6, 3.6, -6.4); label('Phoenix-area average', p.x, p.y - 60, 44, { align: 'center', color: C.accent, alpha: ease(t, cue.b1.avg + 0.3, cue.b1.avg + 0.6) * (1 - ease(t, 15.0, 15.4)) }); }
    // trục năm
    const axA = ease(t, 16.0, 16.8) * (1 - ease(t, 55.0, 55.5));
    if (axA > 0.01) for (const [q, s2] of [[0, '2000'], [40, '2010'], [80, '2020'], [105, '2026 Q2']]) { const p = P(X(q), 0, 1.4); K.text(s2, p.x, p.y + 46, 40, { align: 'center', color: C.muted, w: 400, alpha: axA }); }
    // vệt: "home value" → "gain on paper"
    const lq = 4;
    if (t > DRAW0 && t < B11) {
      const isGain = t > DROP1 - 0.2;
      const y = isGain ? Math.max(0, gain[lq] / U) : value[lq] / U - (s.phase === 'drop' ? s.drop : 0);
      const p = P(XT(lq), y, TZ);
      const a1 = ease(t, cue.b2.y2000 + 0.3, cue.b2.y2000 + 0.7) * (1 - ease(t, DROP1 - 0.5, DROP1 - 0.2)) * (1 - 0.6 * ease(t, cue.b3.cap + 0.35, cue.b3.cap + 0.8) * (1 - ease(t, cue.b4.grow, cue.b4.grow + 0.4)));
      const a2 = ease(t, DROP1 - 0.2, DROP1 + 0.3) * (1 - ease(t, 55.2, 55.8));
      label('home value', p.x, p.y - 50, 44, { align: 'center', color: C.accent, alpha: a1 });
      label('gain on paper', p.x + 40, p.y - 46, 44, { align: 'center', color: C.accent, alpha: a2 });
    }
    // b3: nhãn trần
    // nhãn trần ở lại suốt cảnh đẩy máy (55–63): neo dịch dần về đoạn vạch còn trong khung, xuống dưới vạch
    const capA = ease(t, cue.b3.lbl, cue.b3.lbl + 0.3) * (1 - ease(t, HIDE0, HIDE1)), cm = ease(t, 55.2, 57.5);
    { const p = P(mix(-8.3, 1.6, cm), BEAM_Y, 0.45); label(CL('excl_joint_limit_usd') + ' cap', p.x + 4, p.y + mix(-34, 72, cm), 48, { color: C.ink, alpha: capA, w: 700 }); }
    // "same in every quarter"
    { const p = P(-1.0, BEAM_Y, 0.45); label('same in every quarter', p.x, p.y - 34, 44, { align: 'center', color: C.muted, alpha: ease(t, cue.b3.flat, cue.b3.flat + 0.3) * (1 - ease(t, 29.2, 29.8)), w: 400 }); }
    // b4: "their gain on paper = ?" → "$200,000" → "$200,000, grown with the index" → trừ → "$200,000 paid"
    const P200 = CL('illustrative_price_200k_usd');
    { const p = P(-0.5, BEAM_Y + 1.5, 0); label('their gain on paper = ?', p.x, p.y, 52, { align: 'center', w: 700, alpha: ease(t, cue.b4.gain, cue.b4.gain + 0.3) * (1 - ease(t, cue.b4.two - 0.3, cue.b4.two)) }); }
    const slabA = ease(t, cue.b4.two, cue.b4.two + 0.3) * (1 - ease(t, 40.0, 40.4));
    if (slabA > 0.01) {
      const p = P(X(105) - 2.1 * easeOut(t, SLIDE0, SLIDE1) - 0.62, 1.0, 0.4);
      const s2 = t >= cue.b4.paid ? P200 + ' paid' : P200;
      label(s2, p.x - 24, p.y + 16, 48, { align: 'right', alpha: slabA * (1 - 0.6 * ease(t, cue.b4.grow, cue.b4.grow + 0.3) * (1 - ease(t, LESS, LESS + 0.2))), w: 700, color: t >= LESS ? C.ink : C.accent });
    }
    { const p = P(X(105) - 0.9, valueAt(105) / U, 0.4);
      label(P200 + ', grown with the index', p.x - 20, p.y + 60, 48, { align: 'right', w: 700, color: C.accent, alpha: ease(t, cue.b4.grow, cue.b4.grow + 0.3) * (1 - ease(t, LESS - 0.1, LESS + 0.2)) }); }
    // trừ: ngoặc giữa bóng đường giá trị và đường đã rơi (ở 2003)
    const da2 = ease(t, LESS + 0.3, LESS + 0.6) * (1 - ease(t, 40.0, 40.4));
    if (da2 > 0.01) { const a = P(XT(30), value[30] / U, TZ), b = P(XT(30), value[30] / U - s.drop, TZ); bracket(a.x - 14, a.y, b.y, C.ink, da2, 1, 4); }
    // b5: ngoặc khoảng cách tới vạch
    const ua = ease(t, cue.b5.under - 0.2, cue.b5.under + 0.2) * (1 - ease(t, 44.5, 45.0));
    if (ua > 0.01 && s.H < BEAM_Y - 0.3) { const a = P(s.x + 0.95, s.H, 0.4), b = P(s.x + 0.95, BEAM_Y, 0.4); bracket(a.x, a.y, b.y, C.cushion, ua, -1, 8); label('well under', a.x + 22, (a.y + b.y) / 2 + 16, 48, { color: C.cushion, w: 700, alpha: ua }); }
    // b6: chớp sáng vòng tròn ở điểm cắt
    if (t >= CROSS && t < CROSS + 0.7) { const c = P(X(89), BEAM_Y, 0.45), k = lin(t, CROSS, CROSS + 0.7);
      ctx.save(); ctx.globalAlpha = 1 - k; ctx.strokeStyle = C.warn; ctx.lineWidth = 10 * (1 - k) + 2;
      for (const r0 of [0, 0.25]) { const kk = clamp(k - r0); if (kk > 0) { ctx.beginPath(); ctx.arc(c.x, c.y, 20 + 200 * kk, 0, Math.PI * 2); ctx.stroke(); } }
      ctx.restore(); }
    // b6: Over: Q2 2022 ; b8: Stayed over since Q2 2023
    { const p = P(X(89), BEAM_Y, 0.45); label('Over: ' + CL('cross_quarter_at_200k_phoenix'), p.x - 110, p.y - 40, 48, { align: 'right', color: C.warn, w: 700, alpha: ease(t, CROSS, CROSS + 0.25) * (1 - 0.35 * ease(t, cue.b7.slip, cue.b7.slip + 0.4) * (1 - ease(t, cue.b8.lbl, cue.b8.lbl + 0.3))) * (1 - ease(t, cue.b9.fly - 0.3, cue.b9.fly)) }); }
    { const p = P(X(93), BEAM_Y, 0.45); label('Stayed over since ' + CL('stay_quarter_at_200k_phoenix'), p.x - 110, p.y - 104, 48, { align: 'right', color: C.warn, w: 700, alpha: ease(t, cue.b8.lbl, cue.b8.lbl + 0.3) * (1 - ease(t, cue.b9.fly - 0.3, cue.b9.fly)) }); }
    // b9: thẻ giá ≈ $558,100 → bay lên thành số lớn
    const G = CL('gain_at_200k_phoenix');
    const tagA = ease(t, cue.b9.fly - 0.05, cue.b9.fly + 0.08) * (1 - ease(t, B11, B11 + 0.4));
    if (tagA > 0.01) {
      const src = P(X(105) + 1.15, BEAM_Y + 0.29, 0.4), dst = { x: 620, y: 250 };
      const f = easeOut(t, cue.b9.fly, cue.b9.land), arc = Math.sin(f * Math.PI) * -90;   // bay ngay ở cue fly, chậm dần tới land
      const x = mix(src.x + 20, dst.x, f), y = mix(src.y + 18, dst.y, f) + arc, px = mix(48, 112, f);
      label(G, x, y, px, { align: f > 0.5 ? 'center' : 'left', w: 700, alpha: tagA, plateA: 0.6 });
      label('gain on paper', dst.x, dst.y - 100, 44, { align: 'center', color: C.muted, w: 600, alpha: tagA * ease(t, cue.b9.land - 0.2, cue.b9.land + 0.2) });
      if (t > cue.b9.land) { // tick khi chạm: gạch chân warn ngắn
        const k = easeOut(t, cue.b9.land, cue.b9.land + 0.35);
        ctx.save(); ctx.globalAlpha = tagA; ctx.fillStyle = C.warn; ctx.fillRect(dst.x - 230 * k, dst.y + 26, 460 * k, 6); ctx.restore();
      }
    }
    // b10: ngoặc warn phần vượt vạch
    const pa = ease(t, cue.b10.past, cue.b10.past + 0.3) * (1 - ease(t, B11, B11 + 0.4));
    if (pa > 0.01) {
      const a = P(X(105) + 0.8, BEAM_Y, 0.4), b = P(X(105) + 0.8, s.H, 0.4);
      bracket(a.x, a.y, b.y, C.warn, pa, -1, 7);
      label('past the cap', a.x + 26, (a.y + b.y) / 2 + 16, 48, { color: C.warn, w: 700, alpha: pa });
    }
    // b11: 2000 / 2026 Q2, ×3.8, chú thích
    const ta = ease(t, 64.2, 64.5);
    if (ta > 0.01) {
      const l = P(4.0, 0, 0.9), r = P(X(105), 0, 0.9);
      K.text(CL('buy_year'), l.x, l.y + 56, 44, { align: 'center', color: C.muted, alpha: ta });
      K.text(CL('sale_quarter'), r.x, r.y + 56, 44, { align: 'center', color: C.muted, alpha: ta });
      // ngoặc chiều cao: nhà 2000 vs nhà hôm nay
      const xa = ease(t, GROW0, GROW0 + 0.3);
      const hh = 1.0 + 0.72 + 0.0; // chiều cao xấp xỉ nhà code (dùng hộp bao thực bên dưới)
      const top = heroTop(), topL = twinTop();
      const pL = P(4.0 - 1.15, topL, 0.6), pR = P(X(105) + 1.1, top, 0.6), pR0 = P(X(105) + 1.1, 0, 0.6);
      bracket(pR.x, pR0.y, pR.y, C.ink, xa * 0.9, -1, 4);
      ctx.save(); ctx.globalAlpha = xa * 0.6; ctx.setLineDash([10, 10]); ctx.strokeStyle = C.muted; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(pL.x, pL.y); ctx.lineTo(pR.x - 30, pL.y); ctx.stroke(); ctx.restore();
      K.text(CL('growth_phoenix'), pR.x + 26, (pR.y + pR0.y) / 2 + 30, 96, { w: 700, color: C.ink, alpha: ease(t, RISE, RISE + 0.3) });
      
    }
    label('Phoenix-area prices since 2000', 960, 210, 56, { align: 'center', w: 600, alpha: ease(t, 63.2, 63.5) });
    // chrome bắt buộc
    const cw = t >= cue.b10.t1 ? 'A measurement, not a tax bill or a next step' : t >= cue.b4.t0 ? 'A home that rose like the Phoenix average' : null;
    const cwA = t >= cue.b10.t1 ? ease(t, cue.b10.t1, cue.b10.t1 + 0.4) : ease(t, cue.b4.t0, cue.b4.t0 + 0.4) * (1 - ease(t, cue.b10.t1 - 0.3, cue.b10.t1));
    chrome(K, { illus: true, hist: t >= cue.b1.t0, src: t >= cue.b1.src, srcA: ease(t, cue.b1.src, cue.b1.src + 0.3), cw, cwA });
  }
  const box3 = new THREE.Box3();
  const heroTop = () => { hero.updateMatrixWorld(true); box3.setFromObject(hero); return box3.max.y; };
  const twinTop = () => { twin.updateMatrixWorld(true); box3.setFromObject(twin); return box3.max.y; };

  function frame(t) {
    const s = updateScene(t);
    renderer.render(scene, camera);
    ctx.clearRect(0, 0, W, H);
    ctx.drawImage(gl, 0, 0);
    const vg = ctx.createRadialGradient(W / 2, H / 2, H * 0.4, W / 2, H / 2, H * 1.0);
    vg.addColorStop(0, 'rgba(14,17,22,0)'); vg.addColorStop(1, 'rgba(14,17,22,0.5)'); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
    // màn mờ dưới chân trang / trên dòng nguồn: chữ chrome luôn đọc được khi vật thể đi qua
    const sb = ctx.createLinearGradient(0, 960, 0, 1080); sb.addColorStop(0, 'rgba(14,17,22,0)'); sb.addColorStop(0.45, 'rgba(14,17,22,0.78)'); sb.addColorStop(1, 'rgba(14,17,22,0.85)');
    ctx.fillStyle = sb; ctx.fillRect(0, 960, W, 120);
    const st = ctx.createLinearGradient(0, 0, 0, 140); st.addColorStop(0, 'rgba(14,17,22,0.7)'); st.addColorStop(1, 'rgba(14,17,22,0)');
    ctx.fillStyle = st; ctx.fillRect(0, 0, W, 140);
    overlay(t, s);
  }
  // làm nóng: biên dịch shader + texture trước khi báo READY
  frame(0); frame(30); frame(66);
  return { canvas: out, frame };
}
