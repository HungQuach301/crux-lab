// Tập 8 · THẾ GIỚI CHUNG của sáu đoạn (world/seg/<đoạn>/scene.js): một con phố-lưới 307 nhà (N1, cột = năm 1991 → 2016, hàng = tháng),
// căn hộ của Nina ở QUA CUỐI PHỐ (chỗ chưa có nhà nào — G1 câu 3, không sương N5), thẻ tiền thuê (N2) trên cửa, Nina + đèn riêng (N3, bản v2:
// đứng giữa, không bước về phía nào), hộp kính CASH (N4 v2 + nhãn "cash, not stocks"), nhà của người song sinh mua, chồng tiền theo màu lựa chọn.
// Màu (beats.md Colour roles, story-d013 §3): người MUA = LIT (ấm của cửa sổ sáng N1 đã duyệt) · người THUÊ = warn (cửa tối, hộp tiền mặt).
// M2 animatic xám: spine.grey = true → khung ra được chuyển sang độ sáng (không màu, không chất liệu) ngay sau compose; mọi hình học, máy quay, giờ
// giữ nguyên để M3 chỉ tắt cờ. Mốc giờ CHỈ từ spine.json của đoạn; hằng số ở đây = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { Studio, House, Apartment, Person, setOpacity, PALETTE } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, CK, ease, lin, mix } from '/toolkit/factory/world/core.js';

export { THREE, C, ease, lin, mix, setOpacity, PALETTE };
export const LIT = '#F6D58E', DARKW = '#8C5E14', LAMP = '#FFB86B', PLATE = '#0B0E13', FIG = PALETTE.person2, DIM = '#3A3E46';
export const POP = 0.2;
export const kf = (k, t) => { if (!k || !k.length) return 0; if (t <= k[0][0]) return k[0][1];
  for (let i = 1; i < k.length; i++) if (t <= k[i][0]) { const [a, x] = k[i - 1], [b, y] = k[i]; return b > a ? x + (y - x) * (t - a) / (b - a) : y; }
  return k[k.length - 1][1]; };
export const show = (t, a, z = Infinity) => (a == null ? 0 : ease(t, a - 0.05, a + POP) * (1 - ease(t, z, z + 0.3)));
export const pulse = (t, a, d = 0.6) => (a == null || t < a ? 0 : Math.max(0, 1 - (t - a) / d));
const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, transparent: true, ...o });

// ---------------------------------------------------------------- hình học phố (dùng chung mọi đoạn: cùng toạ độ → máy quay nối nhau)
export const GAP = 0.95, ROW = 0.95, HW = 0.55;
export const colOf = (s) => +s.slice(0, 4) - 1991, rowOf = (s) => +s.slice(5, 7) - 1;
export const xOf = (s) => colOf(s) * GAP, zOf = (s) => -rowOf(s) * ROW;
export const END_X = 25 * GAP + 2.4;              // căn hộ Nina: qua cột 2016, chỗ chưa có nhà
export const APT = { x: END_X + 1.2, z: -2.2 }, NINA = { x: END_X + 2.9, z: 0.6 }, BUY = { x: END_X + 5.0, z: -2.0 }, BOX = { x: END_X - 0.4, z: 0.5 };

export async function setup(seg, res, poses, { shadowBox = 30 } = {}) {
  const [S, CL, DATA] = await Promise.all([loadJSON(seg + 'spine.json'), loadJSON('/episodes/ep008/world/claims.json'), loadJSON('/episodes/ep008/world/data.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const MV = {}; for (const m of S.moves) MV[m.id] = m;
  const st = Stage(res), scene = new THREE.Scene(), { floor, key } = Studio(scene, { shadowBox });
  const D = (k) => CL[k].display;
  const grey = !!S.grey;
  // M2 xám: khung ra → độ sáng (Rec. 709), sau lớp phủ — chữ vẫn đọc được, màu lựa chọn chưa có (chưa có chất liệu)
  const compose0 = st.compose.bind(st);
  st.compose = () => { compose0(); if (!grey || CK.on) return; const c = st.out.getContext('2d'), w = st.out.width, h = st.out.height, im = c.getImageData(0, 0, w, h), p = im.data;
    for (let i = 0; i < p.length; i += 4) { const y = 0.2126 * p[i] + 0.7152 * p[i + 1] + 0.0722 * p[i + 2]; p[i] = p[i + 1] = p[i + 2] = y; } c.putImageData(im, 0, 0); };
  return { S, CL, D, DATA, cue, MV, st, O: st.O, renderer: st.renderer, scene, floor, key, CAM: Camera(poses, S.moves), grey };
}
export function followLight(key, tgt) {
  key.target.position.set(tgt[0], Math.max(0, tgt[1]), tgt[2]); key.position.set(tgt[0] - 8, Math.max(0, tgt[1]) + 18, tgt[2] + 12); key.target.updateMatrixWorld();
}
export function modeLook(scene, floor, cw) { floor.material.opacity = 1 - 0.8 * cw; scene.fog.near = 40 + 120 * cw; scene.fog.far = 110 + 220 * cw; }

// ---------------------------------------------------------------- N1 the street: 307 nhà + ô lưới dưới mỗi nhà (đọc được khi nhìn thẳng xuống)
// set({lit: f(i)∈[0,1], dark: f(i)∈[0,1], hi: f(i)∈[0,1], vis: f(i)∈[0,1], cellA}) — lit = người mua hơn (ấm), dark = người thuê hơn (cửa warn)
export function Street(scene, starts, { name = 'street' } = {}) {
  const g = new THREE.Group(); scene.add(g);
  const roadM = mat('#232934');
  for (let c = 0; c < 26; c++) { const r = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.02, 12 * ROW), roadM); r.position.set(c * GAP + 0.42, 0.01, -5.5 * ROW); r.receiveShadow = true; g.add(r); }
  const front = new THREE.Mesh(new THREE.BoxGeometry(26 * GAP + 3.2, 0.02, 0.5), roadM); front.position.set(12.5 * GAP + 1.3, 0.011, 0.75); g.add(front);   // phố chung chạy tới căn hộ Nina
  const houses = starts.map((s) => {
    const h = House({ w: HW, lit: false }); h.rotation.y = 0; h.position.set(xOf(s), 0, zOf(s)); g.add(h);
    const parts = { wins: [], door: null, walls: [], roofs: [] };
    h.traverse((o) => { if (!o.isMesh) return; o.material = o.material.clone(); const hx = o.material.color.getHexString();
      if (o.material.emissive && o.geometry.parameters && o.geometry.parameters.depth === 0.03) parts.wins.push(o);
      else if (hx === '3b4a5a') parts.door = o; else if (hx === 'd9d4c7') parts.walls.push(o); else parts.roofs.push(o); });
    h.userData.checks = { role: 'series', series: 'start-months', case: s, year: +s.slice(0, 4), key: `house-${s}` };
    return { h, ...parts, s };
  });
  const cellG = new THREE.BoxGeometry(GAP * 0.86, 0.015, ROW * 0.86);
  const cells = new THREE.InstancedMesh(cellG, new THREE.MeshBasicMaterial({ transparent: true }), starts.length);   // ô không đổ bóng: màu đúng như khai (đọc được ở bản xám)
  cells.frustumCulled = false; g.add(cells);
  const M4 = new THREE.Matrix4(), col = new THREE.Color(), cLit = new THREE.Color(LIT), cWarn = new THREE.Color(C.warn), cDark = new THREE.Color(DARKW), cOff = new THREE.Color('#2A303B'), cHi = new THREE.Color(C.ink);
  const wall0 = new THREE.Color('#7E838C'), roof0 = new THREE.Color('#5B5F66'), roofLit = new THREE.Color('#C98A4E'), door0 = new THREE.Color('#3B4A5A'), dim = new THREE.Color(DIM), glow = new THREE.Color(LIT);
  const api = { g, houses, starts, n: starts.length, idx: Object.fromEntries(starts.map((s, i) => [s, i])),
    set({ lit = () => 0, dark = () => 0, hi = () => 0, vis = () => 1, cellA = 0, rise = () => 1, lift = () => 0, big = () => 1 } = {}) {
      houses.forEach((o, i) => {
        const a = lit(i), d = dark(i), v = vis(i), e = hi(i), r = rise(i);
        const L = lift(i), bg = big(i), hv = v * (1 - 0.97 * Math.min(1, cellA) * (L > 0.01 ? 0 : 1)); o.h.visible = hv > 0.01;   // nhìn từ trên: chỉ còn ô (trừ nhà đang nhấc lên)
        o.h.scale.set(bg, Math.max(0.001, r * hv * bg), bg); o.h.position.y = L;
        for (const m of o.wins) { m.material.emissiveIntensity = 1.6 * a + 0.8 * e; }
        for (const m of o.walls) { m.material.color.copy(wall0).lerp(glow, 0.55 * a).lerp(dim, 0.7 * d); m.material.emissive = glow; m.material.emissiveIntensity = 0.45 * a + 0.4 * e; }
        for (const m of o.roofs) { m.material.color.copy(roof0).lerp(roofLit, a).lerp(dim, 0.7 * d); }
        if (o.door) { o.door.material.color.copy(door0).lerp(cWarn, d); o.door.material.emissive = cWarn; o.door.material.emissiveIntensity = 0.6 * d; }
        const sc = cellA > 0.005 && v > 0.01 ? Math.min(1, v * 1.2) : 0;
        M4.makeScale(sc, 1, sc).setPosition(xOf(o.s), 0.02, zOf(o.s)); cells.setMatrixAt(i, M4);
        col.copy(cOff).lerp(cLit, a).lerp(cDark, d).lerp(cHi, 0.6 * e); cells.setColorAt(i, col);
      });
      cells.instanceMatrix.needsUpdate = true; if (cells.instanceColor) cells.instanceColor.needsUpdate = true;
      cells.material.opacity = cellA; cells.visible = cellA > 0.005;
    },
    pos: (s, y = 0.3) => [xOf(s), y, zOf(s)] };
  api.set({});
  return api;
}
// ô của tháng i trong mảng starts khác (5 năm / 15 năm) → giá trị theo tháng của phố 10 năm (true/false/null)
export const byMonth = (starts, arr) => { const m = {}; starts.forEach((s, i) => { m[s] = arr[i]; }); return m; };

// ---------------------------------------------------------------- căn hộ của Nina + thẻ tiền thuê N2 trên cửa (thẻ trắng ở thế giới, số chỉ đọc trên thẻ)
function tagTexture(text, head = 'RENT') {
  const c = document.createElement('canvas'); c.width = 512; c.height = 256; const x = c.getContext('2d');
  x.fillStyle = '#171B22'; x.fillRect(0, 0, 512, 256); x.strokeStyle = PALETTE.muted; x.lineWidth = 10; x.strokeRect(8, 8, 496, 240);
  x.fillStyle = PALETTE.ink; x.font = 'bold 64px Inter, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText(head, 256, 72);
  x.fillStyle = PALETTE.muted; x.font = 'bold 96px Inter, sans-serif'; x.fillText(text, 256, 170);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
export function Home8(scene) {
  const apt = Apartment({ w: 1.7, floors: 3 }); apt.position.set(APT.x, 0, APT.z); scene.add(apt);
  apt.userData.checks = { role: 'mark', key: 'nina-apartment' };
  const door = new THREE.Mesh(new THREE.BoxGeometry(0.34, 0.5, 0.04), mat('#3B4A5A')); door.position.set(APT.x, 0.25, APT.z + 0.62); scene.add(door);
  const card = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.25, 0.03), [mat('#171B22'), mat('#171B22'), mat('#171B22'), mat('#171B22'),
    new THREE.MeshStandardMaterial({ map: tagTexture('5%'), roughness: 0.6, transparent: true }), mat('#171B22')]);
  const tag = new THREE.Group(); tag.add(card); const cord = new THREE.Mesh(new THREE.CylinderGeometry(0.006, 0.006, 0.2), mat(PALETTE.muted)); cord.position.y = 0.22; tag.add(cord);
  tag.position.set(APT.x + 0.3, 0.62, APT.z + 0.66); scene.add(tag); tag.userData.checks = { role: 'mark', key: 'rent-tag', series: 'yield_anchor_pct' };
  let last = '5%';
  tag.set = ({ value = 5, swing = 0, a = 1 } = {}) => { const txt = `${Math.round(value)}%`;
    if (txt !== last) { card.material[4].map.dispose(); card.material[4].map = tagTexture(txt); card.material[4].needsUpdate = true; last = txt; }
    tag.rotation.z = swing; setOpacity(tag, a); };
  const house = House({ w: 1.5, lit: false }); house.position.set(BUY.x, 0, BUY.z); scene.add(house); house.userData.checks = { role: 'mark', key: 'buyer-twin-house' };
  const hw = []; house.traverse((o) => { if (o.isMesh && o.material.emissive && o.geometry.parameters && o.geometry.parameters.depth === 0.03) { o.material = o.material.clone(); hw.push(o); } });
  house.setLit = (a) => { for (const m of hw) m.material.emissiveIntensity = 1.4 * a; };
  return { apt, door, tag, house };
}

// ---------------------------------------------------------------- người (W4, không mặt) + đèn riêng của Nina (N3)
export function figure(scene, { x, z, color = FIG, h = 0.95, char = 'Nina', lamp = false }) {
  const p = Person({ h, color }); p.position.set(x, 0, z); scene.add(p);
  p.userData.checks = { role: 'mark', char, shape: 'person', key: `person-${char.toLowerCase()}` };
  const out = { p, h, char, lamp: null };
  if (lamp) {
    const g = new THREE.Group(), bulb = new THREE.Mesh(new THREE.SphereGeometry(0.06, 12, 8), new THREE.MeshStandardMaterial({ color: LAMP, emissive: new THREE.Color(LAMP), emissiveIntensity: 2 }));
    const L = new THREE.PointLight(LAMP, 3, 3.4, 1.6); g.add(bulb, L); g.position.set(0.32, h * 0.72, 0.1); p.add(g);
    out.lamp = { g, bulb, L, set: (on, t) => { const k = on * (0.85 + 0.15 * Math.sin(t * 2.1)); L.intensity = 3 * k; bulb.material.emissiveIntensity = 2 * k; bulb.visible = on > 0.02; } };
  }
  // N3 v2: Nina đứng yên giữa, quay đầu/đèn về bên đang nhìn (look ∈ [−1, 1])
  out.look = (v) => { p.rotation.y = -0.6 * v; if (out.lamp) out.lamp.g.position.x = 0.32 * (v >= 0 ? 1 : -1); };
  return out;
}

// ---------------------------------------------------------------- chồng tiền theo MÀU LỰA CHỌN (bó mệnh giá cố định trong một cảnh)
export function MoneyStack(scene, { x, z = 0, color = LIT, unit, w = 0.6, d = 0.4, max = 40, name = 'stack' }) {
  const th = 0.07, geo = new THREE.BoxGeometry(w, th * 0.9, d), mesh = new THREE.InstancedMesh(geo, mat(color, { emissive: new THREE.Color(color), emissiveIntensity: 0.12 }), max);
  const strap = new THREE.InstancedMesh(new THREE.BoxGeometry(w * 0.14, th * 0.92, d * 1.02), mat('#E9E3D3'), max);
  mesh.frustumCulled = strap.frustumCulled = false; mesh.castShadow = true;
  const g = new THREE.Group(); g.add(mesh, strap); g.position.set(x, 0, z); scene.add(g); g.userData.checks = { role: 'bar', series: name, key: `stack-${name}` };
  const M4 = new THREE.Matrix4(), hide = new THREE.Matrix4().makeScale(0, 0, 0);
  g.set = ({ usd = 0, a = 1 } = {}) => { const k1 = usd / unit;
    for (let k = 0; k < max; k++) { const f = Math.min(1, Math.max(0, k1 - k)); if (f <= 0.001) { mesh.setMatrixAt(k, hide); strap.setMatrixAt(k, hide); continue; }
      M4.makeScale(1, f, 1).setPosition(0, k * th + th * f / 2, 0); mesh.setMatrixAt(k, M4); strap.setMatrixAt(k, M4); }
    mesh.instanceMatrix.needsUpdate = strap.instanceMatrix.needsUpdate = true; setOpacity(g, a); g.visible = a > 0.005 && usd > 0; g.userData.checks.value = +usd.toFixed(0);
    return k1 * th; };
  g.top = (usd) => usd / unit * th;
  g.set({ usd: 0 });
  return g;
}

// ---------------------------------------------------------------- N4 hộp kính CASH (tiền để dành của người thuê, không đầu tư)
export function GlassBox(scene, { x, z, w = 1.0, h = 0.9, d = 0.7, max = 12 } = {}) {
  const g = new THREE.Group(); g.position.set(x, 0, z); scene.add(g);
  const glass = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshPhysicalMaterial({ color: '#BFD3E6', transparent: true, opacity: 0.18, roughness: 0.05, depthWrite: false }));
  glass.position.y = h / 2; g.add(glass);
  const edges = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(w, h, d)), new THREE.LineBasicMaterial({ color: PALETTE.muted, transparent: true })); edges.position.y = h / 2; g.add(edges);
  const bundles = [];
  for (let i = 0; i < max; i++) { const b = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.1, 0.2), mat(C.warn, { emissive: new THREE.Color(C.warn), emissiveIntensity: 0.1 }));
    b.userData.home = new THREE.Vector3(-0.32 + (i % 3) * 0.32, 0.06 + Math.floor(i / 3) * 0.105, 0); b.castShadow = true; g.add(b); bundles.push(b); }
  g.userData.checks = { role: 'mark', key: 'cash-box', series: 'renter-cash' };
  g.set = ({ n = 0, a = 1, glow = 0 } = {}) => { bundles.forEach((b, i) => { const k = Math.min(1, Math.max(0, n - i)); b.visible = k > 0 && a > 0.01;
      b.position.copy(b.userData.home); b.position.y += (1 - k) * (h + 0.6); b.material.emissiveIntensity = 0.1 + 0.6 * glow; });
    glass.material.opacity = 0.18 * a; edges.material.opacity = a; edges.visible = glass.visible = a > 0.01; };
  g.top = () => [x, h + 0.15, z];
  g.set({ n: 0 });
  return g;
}

// ---------------------------------------------------------------- nhãn, tên, lớp bắt buộc
export function label(O, s, x, y, o = {}) { return O.text(s, x, y, o.px || 52, { plate: PLATE, plateA: 0.72, ...o }); }
export function nameTag(O, fig, a = 1, o = {}) {
  const [fx, fy] = O.toScreen(fig.p.position.x, 0, fig.p.position.z), v = Math.min(1, Math.max(0, Math.min(fx - 40, 1880 - fx) / 80));
  return label(O, `${fig.char} · ILLUSTRATIVE`, Math.min(1500, Math.max(330, fx + (o.dx || 0))), Math.min(880, fy + 50 + (o.dy || 0)), { align: 'center', kind: 'name', px: 48, w: 600, alpha: a * v, char: fig.char });
}
export const SRC = 'FHFA home prices · BLS rents · Freddie Mac rates';
export function chrome(O, { illus = 1, cw = null, cwA = 1, src = SRC } = {}) {
  O.chrome({ illus: illus > 0.01, illusA: illus, src, hist: true, ...(cw && cwA > 0.01 ? { cw, cwA } : {}) });
}
export function seg2(O, x0, y0, x1, y1, color, a, lw = 4) {
  if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = color; c.lineWidth = lw; c.beginPath(); c.moveTo(x0, y0); c.lineTo(x1, y1); c.stroke(); c.restore();
}
export function dip(O, a) { if (a <= 0.005) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.fillStyle = C.bg; c.fillRect(0, 0, 1920, 1080); c.restore(); }
// thẻ chương (story-d013 §1b): tên chương gợi hình, góc trên trái dưới dòng nguồn, 2,2 s từ đầu chương (không chữ số)
export function chapterCard(O, name, t, t0, a = 1) {
  const k = ease(t, t0, t0 + 0.4) * (1 - ease(t, t0 + 2.2, t0 + 2.6)) * a; if (k <= 0.01) return;
  label(O, name, 960, 300, { align: 'center', kind: 'title', px: 72, w: 700, alpha: k, role: 'title' });
}
// thẻ phương pháp / giới hạn (V7): tấm nền trung tính + các dòng
export function v7Card(O, title, lines, a, { x = 300, y = 210, w = 1320 } = {}) {
  if (a <= 0.01) return; const h = 110 + 66 * lines.length;
  O.card(x, y, w, h, { fill: '#141922', stroke: C.muted, lw: 3, alpha: 0.94 * a });
  label(O, title, x + 48, y + 80, { kind: 'title', px: 56, w: 700, alpha: a, plate: null, role: 'title' });
  lines.forEach((s, i) => label(O, s, x + 48, y + 150 + 66 * i, { kind: /\d/.test(s) ? 'number' : 'name', px: 48, w: 600, alpha: a, plate: null, color: '#D5DAE2' }));
}

// ---------------------------------------------------------------- "US only": đường viền 48 bang (Natural Earth, phạm vi công cộng; usmap.json) nằm trên mặt đất,
// hoà vào/ra (footage duy nhất Tập 8, G1 câu 3; RIGHTS.md M-NE-ADM1). set(a); nguồn + năm ghi trên hình ở lớp phủ (mapCredit)
export async function USMap(scene, { x = 0, z = 0, s = 1 } = {}) {
  const M = await loadJSON('/episodes/ep008/world/usmap.json'), pts = [];
  for (const p of M.polys) for (let i = 0; i < p.length; i++) { const a = p[i], b = p[(i + 1) % p.length]; pts.push(a[0] * s + x, 0.03, a[1] * s + z, b[0] * s + x, 0.03, b[1] * s + z); }
  const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
  const line = new THREE.LineSegments(geo, new THREE.LineBasicMaterial({ color: PALETTE.muted, transparent: true, opacity: 0 })); scene.add(line);
  line.userData.checks = { role: 'mark', key: 'us-map', footage: 'M-NE-ADM1' };
  line.set = (a) => { line.material.opacity = 0.85 * a; line.visible = a > 0.01; };
  line.set(0); return line;
}
export function mapCredit(O, a) { if (a > 0.01) label(O, 'Map: Natural Earth (public domain)', 1824, 180, { align: 'right', kind: 'name', px: 40, w: 600, alpha: a, color: C.muted, plate: null }); }

// ---------------------------------------------------------------- chú giải đèn (cổng gốc M2 r1: người đọc thấy sáng/tối nhưng không biết nghĩa) — mọi khung có phố
// sáng/tối: ô mẫu + chữ (không số → hợp lệ cả ở thế giới), góc phải dưới, trên dòng nguồn
export function legend(O, a = 1) {
  if (a <= 0.01) return; const x = 1820, y = 890, c = O.ctx;
  for (const [k, col, s] of [[0, LIT, 'lit: buyer ahead after ten years'], [1, DARKW, 'dark: renter ahead']]) {
    const yy = y + 56 * k; c.save(); c.globalAlpha = a; c.fillStyle = col; c.fillRect(x - 36, yy - 32, 30, 30); c.restore();
    label(O, s, x - 50, yy - 6, { align: 'right', kind: 'name', px: 40, w: 600, alpha: a, plate: PLATE });
  }
}
