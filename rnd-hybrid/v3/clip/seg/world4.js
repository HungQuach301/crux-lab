// R&D vòng 3 · THẾ GIỚI clip v3 (H4′): người lớn Quaternius (CC0) + đồ đạc/nhà Kenney (CC0) + ngân hàng v2, vật liệu toon, hậu kỳ toàn khung (lib/post.js).
// Khu: phố ngân hàng (gốc) · nhà 1930 (x = −40) · văn phòng FHA (x = 60) · lưới trả dần (x = 120) · hôm nay (x = 180). Tất định.
import * as THREE from 'three';
import { Bank, Lamp } from '/rnd-hybrid/v2/paper3d.js';
import { prop, toonMat } from '/rnd-hybrid/v3/lib/kenney.js';
import { adult } from '/rnd-hybrid/v3/lib/quat.js';
import { CROWD, payment } from '/rnd-hybrid/v3/lib/sets.js';

export const HX = -40, OX = 60, GX = 120, TX = 180;
export function toonify(obj) { obj.traverse((n) => { if (!n.isMesh) return; const m = n.material; n.material = toonMat({ color: m.color, map: m.map || null, emissive: m.emissive || new THREE.Color(0), emissiveIntensity: m.emissiveIntensity ?? 0 }); n.castShadow = n.receiveShadow = true; }); return obj; }
async function fit(path, height, o = {}) { const r = await prop(path, o); const b = new THREE.Box3().setFromObject(r); r.scale.multiplyScalar(height / (b.max.y - b.min.y));
  const b2 = new THREE.Box3().setFromObject(r), c = b2.getCenter(new THREE.Vector3()); const g = new THREE.Group(); r.position.sub(new THREE.Vector3(c.x, b2.min.y, c.z)); g.add(r); return g; }   // gốc = tâm đáy
// thẻ chữ 3D (hộp mỏng, mặt trước in chữ) — chữ ≥ 90 px trên texture
export function card(lines, { w = 2.6, h = 0.9, px = 110, sub = null, subPx = 60, tag = null, bg = '#EDE4CF', fg = '#15171C', accent = null } = {}) {
  const c = document.createElement('canvas'); c.width = Math.round(w * 300); c.height = Math.round(h * 300); const g = c.getContext('2d');
  g.fillStyle = bg; g.fillRect(0, 0, c.width, c.height); if (accent) { g.fillStyle = accent; g.fillRect(0, 0, c.width, 24); }
  g.strokeStyle = '#15171C'; g.lineWidth = 8; g.strokeRect(4, 4, c.width - 8, c.height - 8);
  const L = [].concat(lines), y0 = c.height / 2 - (L.length - 1) * px * 0.55 - (sub ? subPx * 0.6 : 0) + (tag ? subPx * 0.5 : 0);
  if (tag) { g.font = `800 ${subPx}px Inter`; const tw = g.measureText(tag).width + 40; g.fillStyle = '#8E2B2B'; g.fillRect(c.width / 2 - tw / 2, 34, tw, subPx * 1.3); g.fillStyle = '#F4EEDC'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(tag, c.width / 2, 34 + subPx * 0.68); }
  g.fillStyle = fg; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = `800 ${px}px Inter`; L.forEach((s, i) => g.fillText(s, c.width / 2, y0 + i * px * 1.1));
  if (sub) { g.font = `600 ${subPx}px Inter`; g.fillStyle = '#4A5160'; g.fillText(sub, c.width / 2, y0 + L.length * px * 1.1 - px * 0.15 + subPx * 0.4); }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  const side = toonMat({ color: bg }), m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.05), [side, side, side, side, toonMat({ map: t }), side]); m.castShadow = true;
  const grp = new THREE.Group(); m.position.y = h / 2; grp.add(m); return grp;
}

export async function buildWorld(scene) {
  const W = {};
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(600, 200), toonMat({ color: '#5C5852' })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const walk = new THREE.Mesh(new THREE.BoxGeometry(48, 0.16, 12), toonMat({ color: '#77716A' })); walk.position.set(0, 0.08, -9); walk.receiveShadow = true; scene.add(walk);
  // ---- phố ngân hàng: cửa có bản lề (mở → đóng), tờ CLOSED, đám đông, đèn phố
  const bank = toonify(Bank({ closed: false })); bank.position.set(0, 0.16, -12.6); scene.add(bank);
  const dm = toonMat({ color: '#5A4330' });
  W.doors = [-1, 1].map((sgn) => { const piv = new THREE.Group(); piv.position.set(sgn * 1.27, 0.16 + 0.88 + 1.7, -14.37);
    const d = new THREE.Mesh(new THREE.BoxGeometry(1.25, 3.4, 0.12), dm); d.position.x = -sgn * 0.63; d.castShadow = d.receiveShadow = true; piv.add(d); scene.add(piv); return { piv, sgn }; });
  W.closed = card('CLOSED', { w: 1.9, h: 0.72, px: 150, fg: '#8E2B2B', accent: '#8E2B2B' }); W.closed.position.set(0, 0.16 + 0.88 + 1.2, -14.24); scene.add(W.closed);
  const blds = ['building-a', 'building-c', 'building-e', 'building-g', 'building-b', 'building-d', 'building-f', 'building-h'];
  for (let i = 0; i < 8; i++) { const b = await fit('city-kit-commercial/' + blds[i] + '.glb', 9 + (i % 3) * 2.5); const left = i < 4;
    b.position.set(left ? -10.5 - (i % 4) * 5.4 : 10.5 + (i % 4) * 5.4, 0.16, -15.5); scene.add(b); }
  for (const x of [-7.5, 8.5]) { const l = toonify(Lamp({ on: true })); l.position.set(x, 0.16, -5.6); scene.add(l); }
  const PEOPLE = [
    { sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'brown', outfit: 'brown', clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'f', skin: 'dark', hair: 'Buns', hairColor: 'black', outfit: 'dressPlum', hat: false, clip: 'Idle_Talking_Loop', expr: 'sad' },
    { sex: 'm', skin: 'medium', hair: 'Buzzed', hairColor: 'black', outfit: 'grey', clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'm', skin: 'deep', hair: 'Buzzed', hairColor: 'black', outfit: 'navy', clip: 'Idle_Talking_Loop', expr: 'shocked' },
    { sex: 'f', skin: 'light', hair: 'Long', hairColor: 'auburn', outfit: 'dressGreen', hat: false, clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'm', skin: 'tan', hair: 'SimpleParted', hairColor: 'black', outfit: 'tweed', beard: true, clip: 'Idle_Loop', expr: 'sad' },
    { sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'grey', outfit: 'charcoal', clip: 'Idle_Talking_Loop', expr: 'worried' },
    { sex: 'f', skin: 'medium', hair: 'Buns', hairColor: 'brown', outfit: 'dressNavy', hat: false, clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'm', skin: 'dark', hair: 'Buzzed', hairColor: 'black', outfit: 'brown', clip: 'Idle_Loop', expr: 'sad' },
    { sex: 'f', skin: 'tan', hair: 'Long', hairColor: 'black', outfit: 'dressPlum', hat: false, clip: 'Idle_Talking_Loop', expr: 'shocked' },
    { sex: 'm', skin: 'medium', hair: 'SimpleParted', hairColor: 'blond', outfit: 'grey', clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'f', skin: 'light', hair: 'Buns', hairColor: 'grey', outfit: 'dressGreen', hat: false, clip: 'Idle_Loop', expr: 'sad' },
  ];
  W.crowd = [];
  for (let i = 0; i < CROWD.length; i++) { const [x, z, rot] = CROWD[i], P = PEOPLE[i], p = await adult(P);
    p.root.position.set(x, 0.16, z); p.root.rotation.y = THREE.MathUtils.degToRad(rot + 180); p.face(P.expr); scene.add(p.root); W.crowd.push({ p, clip: P.clip, off: Math.abs(x * 7.3 + z * 3.1) % 2 }); }
  // ---- nhân vật chính
  W.walt = await adult({ sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'brown', outfit: 'charcoal' }); scene.add(W.walt.root);
  W.waltBare = await adult({ sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'brown', outfit: 'charcoal', hat: false }); scene.add(W.waltBare.root);   // trong nhà: bỏ mũ
  W.ruth = await adult({ sex: 'f', skin: 'medium', hair: 'Buns', hairColor: 'brown', outfit: 'dressPlum', hat: false }); scene.add(W.ruth.root);
  W.clerk = await adult({ sex: 'f', skin: 'dark', hair: 'Buns', hairColor: 'black', outfit: 'dressNavy', hat: false }); W.clerk.root.position.set(OX + 1.25, 0.1, -2.2); W.clerk.root.rotation.y = -0.45; W.clerk.face('happy'); scene.add(W.clerk.root);
  W.sam = await adult({ sex: 'm', skin: 'tan', hair: 'Buzzed', hairColor: 'black', outfit: 'navy', hat: false }); W.sam.face('happy'); scene.add(W.sam.root);
  // ---- khu nhà 1930
  for (const [dx, dz, f, s] of [[0, -14, 'building-type-a', 4.8], [-9.5, -15.5, 'building-type-c', 4.4], [9.5, -15, 'building-type-f', 4.6], [-18, -17, 'building-type-a', 4.2], [18, -17, 'building-type-c', 4.2]]) {
    const h = await fit('city-kit-suburban/' + f + '.glb', s); h.position.set(HX + dx, 0.16, dz); scene.add(h); if (dx === 0) W.house = h; }
  for (const [dx, dz] of [[-5.2, -10.5], [5.6, -10.8], [-12.5, -13], [13, -12.5]]) { const t = await fit('city-kit-suburban/tree-large.glb', 4.2); t.position.set(HX + dx, 0.16, dz); scene.add(t); }
  // 10 ô giá trị nhà (80 % = 8 ô xanh)
  W.val = Array.from({ length: 10 }, (_, i) => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.42, 0.42, 0.08), toonMat({ color: '#EDE4CF' })); m.castShadow = true; m.position.set(HX + 1.6 + i * 0.47, 1.25, -5.4); scene.add(m); return m; });
  W.cal = [1, 2, 3, 4, 5].map((k) => { const c = card(String(k), { w: 0.6, h: 0.6, px: 170, sub: 'yr', subPx: 54, accent: k >= 3 ? '#F2B441' : null }); c.position.set(HX + 0.6 + (k - 1) * 0.72, 0.62, -6.4); scene.add(c); return c; });
  // ---- văn phòng FHA
  const floor2 = new THREE.Mesh(new THREE.BoxGeometry(9, 0.1, 7), toonMat({ color: '#8A6A4C' })); floor2.position.set(OX, 0.05, -1.5); floor2.receiveShadow = true; scene.add(floor2);
  const wall = new THREE.Mesh(new THREE.BoxGeometry(9, 3.4, 0.2), toonMat({ color: '#C9B99A' })); wall.position.set(OX, 1.7, -3.6); wall.receiveShadow = true; scene.add(wall);
  const win = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.3, 0.05), toonMat({ color: '#DCE8F4', emissive: new THREE.Color('#DCE8F4'), emissiveIntensity: 0.6 })); win.position.set(OX - 2.4, 1.9, -3.48); scene.add(win);
  const desk = await fit('furniture-kit/desk.glb', 0.74); desk.position.set(OX, 0.1, -1.0); scene.add(desk);
  const shelf = await fit('furniture-kit/bookcaseClosed.glb', 2.0); shelf.position.set(OX + 3.2, 0.1, -3.1); scene.add(shelf);
  const plant = await fit('furniture-kit/pottedPlant.glb', 1.0); plant.position.set(OX - 3.4, 0.1, -2.9); scene.add(plant);
  const lampT = await fit('furniture-kit/lampSquareTable.glb', 0.45); lampT.position.set(OX - 0.6, 0.84, -1.15); scene.add(lampT);
  const doc = (() => { const c = document.createElement('canvas'); c.width = 420; c.height = 560; const g = c.getContext('2d'); g.fillStyle = '#F4EEDC'; g.fillRect(0, 0, 420, 560);
    g.fillStyle = '#15171C'; g.font = '800 46px Inter'; g.textAlign = 'center'; g.fillText('MORTGAGE', 210, 78); g.font = '700 30px Inter'; g.fillStyle = '#2F4F8A'; g.fillText('INSURED · FHA', 210, 126);
    g.fillStyle = '#8A8070'; for (let i = 0; i < 9; i++) g.fillRect(50, 170 + i * 34, i % 3 === 2 ? 220 : 320, 8); g.fillStyle = '#15171C'; g.fillRect(60, 500, 200, 4);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; const m = new THREE.Mesh(new THREE.BoxGeometry(0.42, 0.004, 0.56), [0, 0, 1, 0, 0, 0].map((k) => k ? toonMat({ map: t }) : toonMat({ color: '#F4EEDC' }))); m.receiveShadow = true; return m; })();
  doc.position.set(OX + 0.05, 0.1 + 0.745, -0.95); doc.rotation.y = Math.PI + 0.15; scene.add(doc);
  // ---- lưới trả dần: mỗi cột 1 năm, 12 ô = 12 kỳ trả; cao ô ∝ khoản trả tháng (minh hoạ 5 %/năm, không ghi số)
  const floor3 = new THREE.Mesh(new THREE.BoxGeometry(24, 0.1, 10), toonMat({ color: '#DCD3BF' })); floor3.position.set(GX + 2, 0.05, -1); floor3.receiveShadow = true; scene.add(floor3);
  const p20 = payment(20), p30 = payment(30), h20 = 0.075, h30 = 0.075 * p30 / p20, tile = new THREE.BoxGeometry(0.26, 1, 0.26);
  const grid = (n, z, color, h) => { const mat = toonMat({ color }), cols = [];
    for (let y = 0; y < n; y++) { const col = new THREE.Group(); for (let m = 0; m < 12; m++) { const b = new THREE.Mesh(tile, mat); b.scale.y = h; b.position.y = 0.1 + h / 2 + m * (h + 0.012); b.castShadow = b.receiveShadow = true; col.add(b); }
      col.position.set(GX - 4.2 + y * 0.34, 0, z); scene.add(col); cols.push(col); } return cols; };
  W.g20 = grid(20, -0.4, '#4C8DFF', h20); W.g30 = grid(30, -2.0, '#3FBF7F', h30);
  for (const [x, z] of [[GX + 9, -4], [GX - 6.5, -4.5]]) { const tr = await fit('city-kit-suburban/tree-large.glb', 3.6); tr.position.set(x, 0.1, z); scene.add(tr); }
  // ---- hôm nay
  for (const [dx, dz, f, s] of [[0, -14, 'building-type-f', 5.0], [-9.5, -15.5, 'building-type-a', 4.4], [9.5, -15, 'building-type-c', 4.6]]) { const h = await fit('city-kit-suburban/' + f + '.glb', s); h.position.set(TX + dx, 0.16, dz); scene.add(h); }
  for (const [dx, dz] of [[-5.2, -10.5], [5.6, -10.8]]) { const t = await fit('city-kit-suburban/tree-small.glb', 3.0); t.position.set(TX + dx, 0.16, dz); scene.add(t); }
  // ---- thẻ (số có nguồn: v2/CLAIMS.md)
  W.C = {
    half: card(['≈ HALF', 'THE PRICE'], { w: 2.4, h: 1.2, px: 120, sub: 'most a bank would lend', accent: '#F2B441' }),
    years: card('3–5 YEARS', { w: 2.3, h: 0.7, px: 130, accent: '#F2B441' }),
    due: card(['THE WHOLE', 'LOAN'], { w: 2.4, h: 2.7, px: 130, sub: 'DUE AT THE END', subPx: 80, tag: 'BEFORE 1934', accent: '#8E2B2B', fg: '#2A1A1A' }),
    fha: card('FHA · 1934', { w: 2.6, h: 0.95, px: 140, sub: 'Federal Housing Administration', subPx: 52, accent: '#4C8DFF' }),
    insured: card('INSURED', { w: 1.6, h: 0.55, px: 100, fg: '#1F3F7A', accent: '#4C8DFF' }),
    eighty: card(['UP TO 80%', 'OF VALUE'], { w: 2.4, h: 1.1, px: 120, accent: '#4C8DFF' }),
    twenty: card('1934: UP TO 20 YEARS', { w: 4.4, h: 0.6, px: 110, accent: '#4C8DFF' }),
    thirty: card('1954: UP TO 30 YEARS', { w: 4.4, h: 0.6, px: 110, accent: '#3FBF7F' }),
  };
  for (const c of Object.values(W.C)) scene.add(c);
  return W;
}
