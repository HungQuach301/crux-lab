// Mốc V · THƯ VIỆN VẬT THỂ 3D CÓ THAM SỐ (D-010 §2 quy tắc 4) — dựng một lần, mọi tập dùng lại.
// Gen kênh (D-010 §3): thế giới 3D tối giản — low-poly, màu kênh, không chân thực ảnh, nhân vật không mặt, không chi tiết trang trí vô nghĩa.
// Đơn vị: trục y = đô la theo thang của cảnh (UNIT_USD / đơn vị); bó tiền có MỆNH GIÁ CỐ ĐỊNH (BUNDLE_USD) nên chiều cao chồng = số bó × độ dày bó.
// Mọi vật là hàm thuần của tham số; cảnh gọi .set(...) mỗi khung (không đồng hồ, không ngẫu nhiên không hạt).
import * as THREE from 'three';

export const PALETTE = { bg: '#0E1116', surface: '#171B22', grid: '#2A303B', ink: '#F2F4F7', muted: '#9AA4B2', accent: '#4C8DFF',
  warn: '#F2B441', costlier: '#C72323', cushion: '#269783',
  // màu vật liệu (không phải màu dữ liệu): tường, mái, tiền, sàn
  wall: '#D9D4C7', roof: '#8A4B3A', bill: '#5E8C6A', bill2: '#4E7A5A', strap: '#E9E3D3', floor: '#161B23', person1: '#E2D3C2', person2: '#C9D3E2' };

const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, transparent: true, ...o });
export function setOpacity(obj, a) { obj.traverse((o) => { if (o.isMesh) for (const m of [].concat(o.material)) { m.opacity = a; m.depthWrite = a > 0.98; } o.visible = a > 0.005; }); }

// ---------------------------------------------------------------- nhà (một tầng, mái dốc, cửa sổ sáng)
export function House({ w = 1.6, wall = PALETTE.wall, roof = PALETTE.roof, lit = true } = {}) {
  const g = new THREE.Group(), d = w * 0.72, h = w * 0.6, rh = w * 0.45;
  const add = (m, x, y, z) => { m.position.set(x, y, z); m.castShadow = m.receiveShadow = true; g.add(m); return m; };
  add(new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat(wall)), 0, h / 2, 0);
  const s = new THREE.Shape(); s.moveTo(-w / 2 - w * 0.06, 0); s.lineTo(w / 2 + w * 0.06, 0); s.lineTo(0, rh); s.closePath();
  add(new THREE.Mesh(new THREE.ExtrudeGeometry(s, { depth: d + w * 0.15, bevelEnabled: false }), mat(roof, { roughness: 0.7 })), 0, h, -d / 2 - w * 0.075);
  const win = mat('#2B2F38', { emissive: new THREE.Color('#F6D58E'), emissiveIntensity: lit ? 0.9 : 0, roughness: 0.3 });
  for (const x of [-w * 0.29, w * 0.29]) add(new THREE.Mesh(new THREE.BoxGeometry(w * 0.17, h * 0.3, 0.03), win), x, h * 0.58, d / 2 + 0.02);
  add(new THREE.Mesh(new THREE.BoxGeometry(w * 0.16, h * 0.52, 0.04), mat('#3B4A5A')), 0, h * 0.26, d / 2 + 0.02);
  g.userData.height = h + rh;
  return g;
}

// ---------------------------------------------------------------- chồng tiền: bó mệnh giá cố định; .set({usd, warnAboveUsd, tintBelowUsd, tint})
export function Stack({ unitUsd = 1e5, bundleUsd = 25000, w = 1.1, d = 0.7, maxUsd = 1.2e6 } = {}) {
  const n = Math.ceil(maxUsd / bundleUsd), th = bundleUsd / unitUsd;
  const geo = new THREE.BoxGeometry(w, th * 0.92, d), m = new THREE.MeshStandardMaterial({ roughness: 0.8, transparent: true });
  const mesh = new THREE.InstancedMesh(geo, m, n); mesh.castShadow = mesh.receiveShadow = true;
  const strapG = new THREE.BoxGeometry(w * 0.16, th * 0.94, d * 1.02), strap = new THREE.InstancedMesh(strapG, mat(PALETTE.strap), n);
  const g = new THREE.Group(); g.add(mesh, strap);
  const M = new THREE.Matrix4(), col = new THREE.Color(), hide = new THREE.Matrix4().makeScale(0, 0, 0);
  g.userData = { bundleUsd, unitUsd, th, n };
  g.set = ({ usd = 0, fromUsd = 0, warnAboveUsd = Infinity, tintBelowUsd = 0, tint = PALETTE.cushion, tintA = 1 } = {}) => {
    const k0 = Math.floor(fromUsd / bundleUsd), k1 = usd / bundleUsd;
    for (let k = 0; k < n; k++) {
      const frac = Math.min(1, Math.max(0, k1 - k));
      if (k < k0 || frac <= 0.001) { mesh.setMatrixAt(k, hide); strap.setMatrixAt(k, hide); continue; }
      const y = (k - k0) * th + th * frac / 2;
      M.makeScale(1, frac, 1).setPosition(0, y, 0);
      mesh.setMatrixAt(k, M); strap.setMatrixAt(k, M);
      const usdK = (k + 0.5) * bundleUsd;
      if (usdK > warnAboveUsd) col.set(PALETTE.warn);
      else if (usdK < tintBelowUsd) col.set(PALETTE.bill).lerp(new THREE.Color(tint), tintA);
      else col.set(k % 2 ? PALETTE.bill : PALETTE.bill2);
      mesh.setColorAt(k, col);
    }
    mesh.instanceMatrix.needsUpdate = strap.instanceMatrix.needsUpdate = true; if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
    return Math.max(0, (k1 - k0)) * th;   // chiều cao thế giới
  };
  return g;
}

// ---------------------------------------------------------------- xà trần / vạch cố định (thanh kính-thép dài theo trục thời gian)
export function Beam({ length = 15, color = PALETTE.muted } = {}) {
  const g = new THREE.Group();
  const core = new THREE.Mesh(new THREE.BoxGeometry(length, 0.07, 0.07), mat(color, { emissive: new THREE.Color(color), emissiveIntensity: 0.35 }));
  const glass = new THREE.Mesh(new THREE.BoxGeometry(length, 0.1, 0.4), mat('#AFC3D9', { opacity: 0.14, roughness: 0.1, metalness: 0.2 }));
  g.add(glass, core); g.userData = { core, glass };
  g.glow = (a, c = PALETTE.warn) => { core.material.emissive.set(a > 0 ? c : color); core.material.emissiveIntensity = 0.35 + 1.2 * a; core.material.color.set(a > 0.5 ? c : color); };
  return g;
}

// ---------------------------------------------------------------- người minh hoạ không mặt (đầu cầu + thân viên nang)
export function Person({ h = 1.0, color = PALETTE.person1 } = {}) {
  const g = new THREE.Group(), m = mat(color, { roughness: 0.9 });
  const body = new THREE.Mesh(new THREE.CapsuleGeometry(h * 0.16, h * 0.42, 4, 10), m); body.position.y = h * 0.39; body.castShadow = true;
  const head = new THREE.Mesh(new THREE.SphereGeometry(h * 0.13, 16, 12), m); head.position.y = h * 0.86; head.castShadow = true;
  g.add(body, head); return g;
}

// ---------------------------------------------------------------- khu phố tối giản: n nhà nhỏ + biển SOLD (không chữ: biển trắng–đỏ)
export function Neighborhood({ n = 12, seed = 7, spanX = [-6, 6], z = -3.5, size = 0.55 } = {}) {
  let s = seed >>> 0; const R = () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296);
  const g = new THREE.Group(), items = [];
  for (let k = 0; k < n; k++) {
    const hs = House({ w: size * (0.85 + 0.3 * R()), wall: '#B8BFCA', roof: '#5F6B7A', lit: false });
    const sign = new THREE.Group();
    const post = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.4, 0.03), mat('#8C8C88')); post.position.y = 0.2;
    const plate = new THREE.Mesh(new THREE.BoxGeometry(0.34, 0.16, 0.02), mat('#F4F1EA')); plate.position.y = 0.42;
    const band = new THREE.Mesh(new THREE.BoxGeometry(0.34, 0.05, 0.025), mat(PALETTE.costlier)); band.position.y = 0.42;
    sign.add(post, plate, band); sign.position.set(size * 0.7, 0, size * 0.5);
    const it = new THREE.Group(); it.add(hs, sign);
    it.position.set(spanX[0] + (spanX[1] - spanX[0]) * (k + 0.5) / n + (R() - 0.5) * 0.3, 0, z + (R() - 0.5) * 1.6);
    g.add(it); items.push({ it, sign, home: it.position.clone() });
  }
  g.userData.items = items; return g;
}

// ---------------------------------------------------------------- dải đường dữ liệu (ribbon phẳng ở z cố định, nhìn rõ ở cả hai chế độ)
export function Ribbon({ maxPts = 600, width = 0.09, color = PALETTE.ink, z = 0.45 } = {}) {
  const geo = new THREE.BufferGeometry(), pos = new Float32Array(maxPts * 2 * 3), colA = new Float32Array(maxPts * 2 * 3);
  const idx = []; for (let i = 0; i < maxPts - 1; i++) { const a = 2 * i; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  geo.setIndex(idx); geo.setAttribute('position', new THREE.BufferAttribute(pos, 3)); geo.setAttribute('color', new THREE.BufferAttribute(colA, 3));
  const m = new THREE.MeshBasicMaterial({ vertexColors: true, transparent: true, side: THREE.DoubleSide, depthWrite: false });
  const mesh = new THREE.Mesh(geo, m); mesh.frustumCulled = false; mesh.renderOrder = 5;
  const c = new THREE.Color();
  // pts: [[x, y, colorHex?], ...]; width in world units
  mesh.set = (pts, w = width, col = color) => {
    const n = Math.min(pts.length, maxPts);
    for (let i = 0; i < n; i++) {
      const p = pts[i], q0 = pts[Math.max(0, i - 1)], q1 = pts[Math.min(n - 1, i + 1)];
      let dx = q1[0] - q0[0], dy = q1[1] - q0[1]; const L = Math.hypot(dx, dy) || 1; dx /= L; dy /= L;
      const nx = -dy * w / 2, ny = dx * w / 2;
      pos.set([p[0] + nx, p[1] + ny, z, p[0] - nx, p[1] - ny, z], 6 * i);
      c.set(p[2] || col); colA.set([c.r, c.g, c.b, c.r, c.g, c.b], 6 * i);
    }
    geo.setDrawRange(0, Math.max(0, (n - 1) * 6));
    geo.attributes.position.needsUpdate = geo.attributes.color.needsUpdate = true;
  };
  return mesh;
}

// ---------------------------------------------------------------- sàn + ánh sáng studio (mặc định của kênh)
export function Studio(scene, { shadowBox = 14 } = {}) {
  scene.background = new THREE.Color(PALETTE.bg);
  scene.fog = new THREE.Fog(PALETTE.bg, 30, 80);
  scene.add(new THREE.HemisphereLight('#C9D6EA', '#1A1F27', 0.9));
  const key = new THREE.DirectionalLight('#FFF1DC', 2.3); key.position.set(-6, 14, 10); key.castShadow = true;
  key.shadow.mapSize.set(1024, 1024); Object.assign(key.shadow.camera, { left: -shadowBox, right: shadowBox, top: shadowBox, bottom: -4, near: 1, far: 50 });
  key.shadow.bias = -0.0008; key.target.position.set(0, 3, 0); scene.add(key, key.target);
  const rim = new THREE.DirectionalLight('#8FB4FF', 0.6); rim.position.set(6, 6, -10); scene.add(rim);
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(160, 160), new THREE.MeshStandardMaterial({ color: PALETTE.floor, roughness: 0.95, transparent: true }));
  floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; scene.add(floor);
  return { key, rim, floor };
}

// ---------------------------------------------------------------- tia loé (sprite) ở một điểm sự kiện
export function Burst({ color = PALETTE.warn } = {}) {
  const cv = document.createElement('canvas'); cv.width = cv.height = 128;
  const g = cv.getContext('2d'), gr = g.createRadialGradient(64, 64, 0, 64, 64, 64);
  gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(0.3, 'rgba(255,255,255,0.5)'); gr.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = gr; g.fillRect(0, 0, 128, 128);
  const t = new THREE.CanvasTexture(cv);
  const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, color, transparent: true, depthWrite: false })); s.renderOrder = 9;
  return s;
}
