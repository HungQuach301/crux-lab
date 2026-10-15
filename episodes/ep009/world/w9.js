// Tập 9 · THẾ GIỚI CHUNG của sáu đoạn (world/seg/<đoạn>/scene.js). Dùng lại nguyên vật thể Tập 8 (w8.js: phố N1 307 nhà, thẻ thuê N2, Nina +
// đèn N3, hộp CASH N4, chồng tiền) — TAM-NHIN §8 "không vẽ lại" — và thêm vật thể MỚI N6 (đống cổ phiếu của người thuê trên kệ mở, vạch $92,000;
// nhận dạng mù M2 preprod/read-n6-r1) + cặp cột tăng trưởng (B01) + dải đồ thị.
// Màu lựa chọn (TAM-NHIN): buyer = LIT (cửa sổ sáng) · renter-cash = C.warn (hộp CASH, bóng so sánh) · renter-stocks = STK (đống N6, dòng stocks).
// M2 animatic xám: spine.grey → khung ra chuyển sang độ sáng ngay sau compose (như Tập 8); hình học, máy quay, giờ giữ nguyên cho M3.
import * as THREE from 'three';
import { Studio, Stack, Ribbon, Person, setOpacity, PALETTE } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, CK, ease, lin, mix } from '/toolkit/factory/world/core.js';
import { grade } from '/episodes/ep009/world/grade9.js';
import * as W8 from '/episodes/ep008/world/w8.js';

export { THREE, C, ease, lin, mix, setOpacity, PALETTE, Ribbon, Person };
export const { Street, Home8, figure, MoneyStack, GlassBox, label, nameTag, chapterCard, v7Card, seg2, dip, show, pulse, kf, followLight, modeLook,
  GAP, ROW, xOf, zOf, colOf, END_X, APT, NINA, BUY, BOX, LIT, DARKW, PLATE, FIG, byMonth } = W8;
export const STK = PALETTE.accent, CASH = C.warn;
export const SHELF = { x: END_X + 0.9, z: 1.9 };   // kệ N6 trước căn hộ Nina, cạnh hộp CASH (BOX)

export async function setup(seg, res, poses, { shadowBox = 30 } = {}) {
  const [S, CL, DATA] = await Promise.all([loadJSON(seg + 'spine.json'), loadJSON('/episodes/ep009/world/claims.json'), loadJSON('/episodes/ep009/world/data.json')]);
  await fonts();
  // đoạn con (kit._subset): nhịp + động tác ĐỦ của đoạn chương (dời giờ) ở S.ghost → logic cảnh và máy quay liền như đoạn chương
  const GB = S.ghost ? S.ghost.beats : S.beats, GM = S.ghost ? S.ghost.moves : S.moves;
  S.chapter = S.chapter || [-99, '']; S.ident = S.ident || [1e9, 1e9]; S.card = S.card || [1e9, 1e9];
  const cue = {}; for (const b of GB) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const MV = {}; for (const m of GM) MV[m.id] = m;
  const st = Stage(res), scene = new THREE.Scene(), { floor, key } = Studio(scene, { shadowBox });
  const grey = !!S.grey;
  const compose0 = st.compose.bind(st);
  st.compose = () => { compose0(); if (!grey || CK.on) return; const c = st.out.getContext('2d'), w = st.out.width, h = st.out.height, im = c.getImageData(0, 0, w, h), p = im.data;
    for (let i = 0; i < p.length; i += 4) { const y = 0.2126 * p[i] + 0.7152 * p[i + 1] + 0.0722 * p[i + 2]; p[i] = p[i + 1] = p[i + 2] = y; } c.putImageData(im, 0, 0); };
  for (const m of GM) for (const n of [m.from, m.to]) if (n.endsWith('~') && !poses[n]) {
    const b = poses[n.slice(0, -1)], f = 0.9; poses[n] = { ...b, pos: b.pos.map((v, j) => b.tgt[j] + (v - b.tgt[j]) * f) };
  }
  const CAM = Camera(poses, GM);
  if (!grey) { const apply0 = CAM.apply.bind(CAM); CAM.apply = (t) => { grade(scene, key, (S.episode_t0 || 0) + t); return apply0(t); }; }
  return { S, CL, D: (k) => CL[k].display, DATA, cue, MV, st, O: st.O, renderer: st.renderer, scene, floor, key, CAM, grey };
}

export const SRC = 'FHFA · BLS · Freddie Mac · K. R. French (CRSP)';   // dòng nguồn ngắn (F-2: bản dài đè nhãn ILLUSTRATIVE); tên đủ ở thẻ phương pháp + mô tả
export function chrome(O, o = {}) { W8.chrome(O, { src: SRC, ...o }); }

// ---------------------------------------------------------------- N6 đống cổ phiếu: kệ mở + bó cố định $10,000 (Stack lib3d), vạch $92,000; phần
// dưới vạch tô màu cảnh báo khi đống tụt. set({usd, a, line}) → chiều cao; top(usd) → [x, y, z] đỉnh đống (để bó rơi vào).
export function StockPile(scene, { x = SHELF.x, z = SHELF.z, s = 1, name = 'stocks' } = {}) {
  const g = new THREE.Group(); g.position.set(x, 0, z); g.scale.setScalar(s); scene.add(g);
  const m = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.6, transparent: true, ...o });
  const shelf = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.06, 1.0), m(STK)); shelf.position.y = 0.03; g.add(shelf);
  const post = new THREE.Mesh(new THREE.BoxGeometry(0.05, 4.2, 0.05), m(STK)); post.position.set(-0.85, 2.1, -0.45); g.add(post);
  const pile = Stack({ unitUsd: 1e5, bundleUsd: 10000, w: 1.1, d: 0.7, maxUsd: 1.6e6 }); pile.position.y = 0.06; g.add(pile);
  const line = new THREE.Mesh(new THREE.BoxGeometry(1.9, 0.025, 1.1), m(PALETTE.ink, { opacity: 0.85 })); line.position.y = 0.06 + 0.92; g.add(line);
  const drop = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.08, 0.24), m(PALETTE.bill)); g.add(drop);
  g.userData.checks = { role: 'bar', series: 'renter-stocks', key: `pile-${name}` };
  g.set = ({ usd = 92000, a = 1, line: la = 1, dropK = -1 } = {}) => {
    const h = pile.set({ usd, tintBelowUsd: 92000, tint: PALETTE.warn, tintA: usd < 92000 ? 0.6 : 0 });
    setOpacity(g, a); line.material.opacity = 0.85 * a * la; line.visible = a * la > 0.01;
    drop.visible = dropK >= 0 && dropK < 1 && a > 0.01; drop.position.set(0, 0.06 + h + (1 - Math.max(0, dropK)) * 1.2, 0);
    g.userData.checks.value = Math.round(usd); return h * s;
  };
  g.top = (usd) => [x, (0.06 + usd / 1e5) * s, z];
  g.lineY = () => (0.06 + 0.92) * s;
  g.set({});
  return g;
}

// ---------------------------------------------------------------- B01 cặp cột tăng trưởng: mỗi tháng bắt đầu hai cột mảnh (nhà = ink-muted, cổ phiếu = STK),
// x = tháng (trái 1991 → phải 2016), cao = $1 thành bao nhiêu sau 10 năm. set({k ∈ [0,1] phần đã mọc, hiS: tô cột cổ phiếu cao hơn, a})
export function GrowthPairs(scene, gS, gH, { x0 = -30, w = 14, z = -2, unit = 0.55, name = 'growth' } = {}) {
  const n = gS.length, bw = w / n * 0.42, geo = new THREE.BoxGeometry(bw, 1, 0.12);
  const mk = (c) => { const im = new THREE.InstancedMesh(geo, new THREE.MeshStandardMaterial({ color: c, roughness: 0.7, transparent: true }), n); im.frustumCulled = false; scene.add(im); return im; };
  const H = mk('#9AA4B2'), Sx = mk(STK), M4 = new THREE.Matrix4(), col = new THREE.Color();
  const X = (i) => x0 + w * i / (n - 1);
  const g = { H, Sx, X, top: (v) => v * unit, n };
  H.userData.checks = { role: 'bar', series: 'house-growth', key: `${name}-house` }; Sx.userData.checks = { role: 'bar', series: 'stock-growth', key: `${name}-stocks` };
  g.set = ({ k = 1, a = 1, hiS = 0 } = {}) => {
    for (let i = 0; i < n; i++) {
      const f = ease(k * 1.15 - i / n * 0.15, 0, 1);
      M4.makeScale(1, Math.max(1e-3, gH[i] * unit * f), 1).setPosition(X(i) - bw * 0.55, gH[i] * unit * f / 2, z); H.setMatrixAt(i, M4);
      M4.makeScale(1, Math.max(1e-3, gS[i] * unit * f), 1).setPosition(X(i) + bw * 0.55, gS[i] * unit * f / 2, z); Sx.setMatrixAt(i, M4);
      col.set(STK).lerp(new THREE.Color('#FFFFFF'), gS[i] > gH[i] ? 0.35 * hiS : 0).lerp(new THREE.Color('#3A3E46'), gS[i] > gH[i] ? 0 : 0.6 * hiS); Sx.setColorAt(i, col);
    }
    H.instanceMatrix.needsUpdate = Sx.instanceMatrix.needsUpdate = true; if (Sx.instanceColor) Sx.instanceColor.needsUpdate = true;
    for (const im of [H, Sx]) { im.material.opacity = a; im.visible = a > 0.01; }
  };
  g.set({ k: 0, a: 0 });
  return g;
}

// ---------------------------------------------------------------- một đường đồ thị (Ribbon) theo mảng giá trị, x đều trong [x0, x0 + w], y = y0 + v·sy
export function Line(scene, vals, { x0, w, y0, sy, z = -2, color = C.ink, width = 0.05 }) {
  const r = Ribbon({ maxPts: vals.length, width, color, z }); scene.add(r);
  const P = (i) => [x0 + w * i / (vals.length - 1), y0 + vals[i] * sy];
  r.draw = (k, a = 1) => { const n = Math.max(2, Math.floor(vals.length * Math.min(1, k))); r.set(vals.slice(0, n).map((v, i) => [...P(i), color])); r.visible = a > 0.01 && k > 0; r.material.opacity = a; };
  r.P = P; r.draw(0, 0); return r;
}

// ---------------------------------------------------------------- chú giải đèn (Tập 9: tối = quỹ người thuê lớn hơn)
export function legend(O, a = 1, { what = 'buyer ahead after ten years', dark = "renter's pile bigger" } = {}) {
  if (a <= 0.01) return; const c = O.ctx, y = 168, t1 = `lit: ${what}`, t2 = `dark: ${dark}`;
  c.save(); c.font = '600 36px Inter'; const w2 = c.measureText(t2).width, w1 = c.measureText(t1).width; c.restore();
  const x2 = 1820 - w2, x1 = x2 - 56 - w1 - 40;
  for (const [x, col] of [[x1 - 38, LIT], [x2 - 38, DARKW]]) { c.save(); c.globalAlpha = a; c.fillStyle = col; c.fillRect(x, y - 28, 28, 28); c.restore(); }
  label(O, t1, x1, y, { align: 'left', kind: 'name', px: 36, w: 600, alpha: a, plate: null, color: '#D5DAE2' });
  label(O, t2, x2, y, { align: 'left', kind: 'name', px: 36, w: 600, alpha: a, plate: null, color: '#D5DAE2' });
}

// ---------------------------------------------------------------- tiện: tháng ↔ chỉ số; đèn của phố theo một mảng ahead (true = sáng)
export const mIdx = (s) => (+s.slice(0, 4)) * 12 + (+s.slice(5, 7));
export function lights(ahead, rev = () => 1) { return { lit: (i) => (ahead[i] ? rev(i) : 0), dark: (i) => (ahead[i] ? 0 : rev(i)) }; }
// chuyển mượt giữa hai trạng thái đèn (A → B) theo k ∈ [0,1], quét trái → phải (theo cột năm)
export function sweep(A, B, k, starts) {
  const f = (i) => ease(k * 1.25 - colOf(starts[i]) / 26 * 0.25, 0, 1);
  return { lit: (i) => mix(A[i] ? 1 : 0, B[i] ? 1 : 0, f(i)), dark: (i) => mix(A[i] ? 0 : 1, B[i] ? 0 : 1, f(i)) };
}

// ---------------------------------------------------------------- một nhà mẫu riêng (luật đèn, B12): set(lit ∈ [0,1], dark ∈ [0,1])
import { House } from '/toolkit/factory/world/lib3d.js';
export function DemoHouse(scene, { x, z, w = 1.2 } = {}) {
  const h = House({ w, lit: false }); h.position.set(x, 0, z); scene.add(h);
  const wins = [], door = []; h.traverse((o) => { if (!o.isMesh) return; o.material = o.material.clone(); const hx = o.material.color.getHexString();
    if (o.material.emissive && o.geometry.parameters && o.geometry.parameters.depth === 0.03) wins.push(o); else if (hx === '3b4a5a') door.push(o); });
  const d0 = new THREE.Color('#3B4A5A'), dk = new THREE.Color('#0E1014');
  h.userData.checks = { role: 'mark', key: `demo-house-${x}` };
  h.set = ({ lit = 0, dark = 0, a = 1 } = {}) => { for (const m of wins) m.material.emissiveIntensity = 1.6 * lit; for (const m of door) m.material.color.copy(d0).lerp(dk, dark); setOpacity(h, a); };
  h.set({}); return h;
}

// ---------------------------------------------------------------- thẻ thuê N2 có số lẻ (S22: 5.1%, 4.83%, 5.59%) — cùng hình thẻ của w8 Home8 (ẩn thẻ gốc khi dùng)
function tagTex(text) {
  const c = document.createElement('canvas'); c.width = 512; c.height = 256; const x = c.getContext('2d');
  x.fillStyle = '#171B22'; x.fillRect(0, 0, 512, 256); x.strokeStyle = PALETTE.muted; x.lineWidth = 10; x.strokeRect(8, 8, 496, 240);
  x.fillStyle = PALETTE.ink; x.font = 'bold 64px Inter, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText('RENT', 256, 72);
  x.fillStyle = PALETTE.muted; x.font = 'bold 92px Inter, sans-serif'; x.fillText(text, 256, 170);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
export function RentTag(scene, { x = APT.x + 0.3, y = 0.62, z = APT.z + 0.66 } = {}) {
  const side = new THREE.MeshStandardMaterial({ color: '#171B22', transparent: true }), face = new THREE.MeshStandardMaterial({ map: tagTex('5%'), roughness: 0.6, transparent: true });
  const card = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.25, 0.03), [side, side, side, side, face, side]);
  const g = new THREE.Group(); g.add(card); g.position.set(x, y, z); scene.add(g); g.userData.checks = { role: 'mark', key: 'rent-tag', series: 'yield_anchor_pct' };
  let last = '5%';
  g.set = ({ text = '5%', swing = 0, flip = 0 } = {}) => { if (text !== last) { face.map.dispose(); face.map = tagTex(text); face.needsUpdate = true; last = text; }
    g.rotation.z = swing; g.rotation.y = Math.PI * 2 * flip; };
  return g;
}
