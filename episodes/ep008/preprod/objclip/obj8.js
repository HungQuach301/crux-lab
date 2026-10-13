// Tập 8 · vật thể MỚI thử trước G1 (luật tạm 13/10 (c)) — dựng trên lib3d (W1 House, W4 Person, W9 Apartment, Studio).
// N1 Street: 307 nhà giống hệt dọc một con đường (trái → phải = tháng mua 1991 → 2016); đèn cửa sổ sáng = người mua hơn sau 10 năm,
//    tối + cửa warn = người thuê hơn. .set({lit: [0..1 mỗi nhà], doorWarn: [0..1]}).
// N2 RentTag: thẻ treo cửa căn hộ, mặt số giả định tiền thuê (ink-muted = mức giả định); .set({value}) xoay kim + đổi chữ (canvas).
// N3 NinaLamp: đèn ấm riêng của nhân vật dẫn đường (PointLight + quả cầu nhỏ), đi theo người; .set({on, t}) nhịp thở sáng.
import * as THREE from 'three';
import { PALETTE, House } from '/toolkit/factory/world/lib3d.js';

const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, transparent: true, ...o });
export const LAMP = '#FFB86B';

export function Street({ starts, gap = 0.95, rowGap = 0.95, w = 0.55 } = {}) {
  // lưới các tháng mua: cột = năm (trái → phải 1991 → 2016), hàng = tháng (Jan ở trước máy); mỗi nhà một tháng bắt đầu
  const g = new THREE.Group(), houses = [];
  const y0 = Number(starts[0].slice(0, 4)), ny = Number(starts[starts.length - 1].slice(0, 4)) - y0 + 1;
  for (let c = 0; c < ny; c++) {   // mỗi năm một con phố ngắn (dải đường dưới cột)
    const road = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.02, 12 * rowGap), mat('#232934'));
    road.position.set(c * gap + 0.42, 0.01, -5.5 * rowGap); road.receiveShadow = true; g.add(road);
  }
  starts.forEach((s, i) => {
    const c = Number(s.slice(0, 4)) - y0, r = Number(s.slice(5, 7)) - 1;
    const h = House({ w, lit: false }); h.rotation.y = Math.PI / 2; h.position.set(c * gap, 0, -r * rowGap);
    const wins = [], doors = [], walls = [], roofs = [];
    h.traverse((o) => { if (!o.isMesh) return; const hx = o.material.color.getHexString();
      if (o.material.emissive && o.geometry.parameters && o.geometry.parameters.depth === 0.03) wins.push(o);
      else if (hx === '3b4a5a') doors.push(o); else if (hx === 'd9d4c7') walls.push(o); else roofs.push(o); });
    for (const m of [...wins, ...doors, ...walls, ...roofs]) m.material = m.material.clone();
    houses.push({ wins, doors, walls, roofs }); g.add(h);
  });
  const warn = new THREE.Color(PALETTE.warn), door0 = new THREE.Color('#3B4A5A'), glow = new THREE.Color('#F6D58E');
  const neutral = new THREE.Color('#7E838C'), dim = new THREE.Color('#3A3E46'), roof0 = new THREE.Color('#5B5F66'), roofLit = new THREE.Color('#C98A4E');
  g.userData = { gap, rowGap, ny, y0,
    set({ lit = [], doorWarn = [] } = {}) {
      houses.forEach((o, i) => {
        const a = lit[i] || 0, d = doorWarn[i] || 0;
        for (const m of o.wins) m.material.emissiveIntensity = 1.5 * a;
        for (const m of o.walls) { m.material.color.copy(neutral).lerp(glow, a).lerp(dim, d); m.material.emissive = glow; m.material.emissiveIntensity = 0.55 * a; }
        for (const m of o.roofs) { m.material.color.copy(roof0).lerp(roofLit, a).lerp(dim, d); m.material.emissive = roofLit; m.material.emissiveIntensity = 0.35 * a; }
        for (const m of o.doors) { m.material.color.copy(door0).lerp(warn, d); m.material.emissive = warn; m.material.emissiveIntensity = 0.5 * d; }
      });
    } };
  return g;
}

function tagTexture(text, head = 'RENT') {
  const c = document.createElement('canvas'); c.width = 512; c.height = 256;
  const x = c.getContext('2d');
  x.fillStyle = '#171B22'; x.fillRect(0, 0, 512, 256);
  x.strokeStyle = PALETTE.muted; x.lineWidth = 10; x.strokeRect(8, 8, 496, 240);
  x.fillStyle = PALETTE.ink; x.font = 'bold 64px Inter, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle';
  x.fillText(head, 256, 72); x.fillStyle = PALETTE.muted; x.font = 'bold 96px Inter, sans-serif'; x.fillText(text, 256, 170);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}

export function RentTag({ w = 0.9, head = 'RENT', blank = false } = {}) {
  const g = new THREE.Group();
  const card = new THREE.Mesh(new THREE.BoxGeometry(w, w / 2, 0.03), [mat('#171B22'), mat('#171B22'), mat('#171B22'), mat('#171B22'),
    new THREE.MeshStandardMaterial({ map: tagTexture(blank ? '' : '5%', head), roughness: 0.6 }), mat('#171B22')]);
  g.add(card);
  const cord = new THREE.Mesh(new THREE.CylinderGeometry(0.008, 0.008, 0.35), mat(PALETTE.muted)); cord.position.set(0, w / 4 + 0.17, 0); g.add(cord);
  let last = null;
  g.userData = { set({ value = 5, swing = 0 } = {}) {
    const txt = value.toFixed(0) + '%';
    if (!blank && txt !== last) { card.material[4].map.dispose(); card.material[4].map = tagTexture(txt); card.material[4].needsUpdate = true; last = txt; }
    g.rotation.z = swing;
  } };
  return g;
}

export function NinaLamp() {
  const g = new THREE.Group();
  const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.07, 12, 8), new THREE.MeshStandardMaterial({ color: LAMP, emissive: new THREE.Color(LAMP), emissiveIntensity: 2 }));
  const light = new THREE.PointLight(LAMP, 3, 3.2, 1.6);
  g.add(bulb); g.add(light);
  g.userData = { set({ on = 1, t = 0 } = {}) {
    const k = on * (0.85 + 0.15 * Math.sin(t * 2.1));
    light.intensity = 3 * k; bulb.material.emissiveIntensity = 2 * k; bulb.visible = on > 0.02;
  } };
  return g;
}

// N4 GlassBox: hộp kính đóng kín (cạnh căn hộ) chứa các bó tiền của người thuê; .set({n}) số bó (bó thứ n rơi vào trong 0,4 s)
export function GlassBox({ w = 1.2, h = 1.0, d = 0.8, max = 12 } = {}) {
  const g = new THREE.Group();
  const glass = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshPhysicalMaterial({ color: '#BFD3E6', transparent: true, opacity: 0.18, roughness: 0.05, metalness: 0, depthWrite: false }));
  glass.position.y = h / 2; g.add(glass);
  const edges = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(w, h, d)), new THREE.LineBasicMaterial({ color: PALETTE.muted }));
  edges.position.y = h / 2; g.add(edges);
  const plate = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.16, 0.02), new THREE.MeshStandardMaterial({ map: (() => { const c = document.createElement('canvas'); c.width = 256; c.height = 80; const x = c.getContext('2d'); x.fillStyle = '#171B22'; x.fillRect(0, 0, 256, 80); x.fillStyle = PALETTE.ink; x.font = 'bold 54px Inter, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText('CASH', 128, 42); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; })() }));
  plate.position.set(0, 0.12, d / 2 + 0.012); g.add(plate);
  const bundles = [];
  for (let i = 0; i < max; i++) {
    const b = new THREE.Mesh(new THREE.BoxGeometry(0.36, 0.11, 0.2), mat(i % 2 ? PALETTE.bill2 : PALETTE.bill));
    const col = i % 3, row = Math.floor(i / 3);
    b.userData.home = new THREE.Vector3(-0.38 + col * 0.38, 0.06 + row * 0.115, 0); b.castShadow = true; g.add(b); bundles.push(b);
  }
  g.userData = { set({ n = 0 } = {}) {
    bundles.forEach((b, i) => { const k = Math.min(1, Math.max(0, n - i)); b.visible = k > 0;
      b.position.copy(b.userData.home); b.position.y += (1 - k) * (h + 0.6); });
  } };
  return g;
}

// N5 Fog: bức sương cuối phố (các tấm mờ chồng nhau, trôi chậm); con đường đi tiếp vào trong, không có nhà
export function FogWall({ w = 14, h = 3, depth = 6, layers = 7 } = {}) {
  const g = new THREE.Group(), cv = document.createElement('canvas'); cv.width = cv.height = 128;
  const x = cv.getContext('2d'), gr = x.createRadialGradient(64, 64, 0, 64, 64, 64);
  gr.addColorStop(0, 'rgba(210,218,230,0.9)'); gr.addColorStop(0.6, 'rgba(210,218,230,0.45)'); gr.addColorStop(1, 'rgba(200,210,224,0)'); x.fillStyle = gr; x.fillRect(0, 0, 128, 128);
  const tex = new THREE.CanvasTexture(cv), planes = [];
  for (let i = 0; i < layers; i++) {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(w * 1.6, h * 1.8), new THREE.MeshBasicMaterial({ map: tex, transparent: true, opacity: 0.75, depthWrite: false, color: '#C3CCD8' }));
    m.position.set(i * depth / layers, h / 2 - 0.2, 0); m.rotation.y = -Math.PI / 2; m.renderOrder = 10; m.material.side = THREE.DoubleSide; g.add(m); planes.push(m);
  }
  g.userData = { set({ t = 0 } = {}) { planes.forEach((m, i) => { m.position.z = 0.5 * Math.sin(t * 0.4 + i); m.position.x = i * depth / layers + 0.2 * Math.sin(t * 0.3 + 2 * i); }); } };
  return g;
}

// N5b EmptyPlots: lô đất trống viền đứt (chưa xây) nối tiếp sau ngôi nhà cuối, chạy vào sương
export function EmptyPlots({ cols = 6, rows = 12, gap = 0.95, rowGap = 0.95, size = 0.55 } = {}) {
  const g = new THREE.Group(), m = new THREE.LineDashedMaterial({ color: PALETTE.muted, dashSize: 0.08, gapSize: 0.06, transparent: true, opacity: 0.8 });
  for (let c = 0; c < cols; c++) for (let r = 0; r < rows; r++) {
    const q = size / 2, pts = [[-q, -q], [q, -q], [q, q], [-q, q], [-q, -q]].map(([x, z]) => new THREE.Vector3(x, 0.02, z));
    const l = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), m); l.computeLineDistances(); l.position.set(c * gap, 0, -r * rowGap); g.add(l);
  }
  return g;
}
