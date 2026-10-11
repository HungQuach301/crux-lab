// Tập 7 · C4 · TIỆN ÍCH CHUNG cho bảy đoạn thế giới của tập (world/c4/<đoạn>/scene.js). Không đổi thư viện nhà máy (lib3d.js / core.js).
// Gốc: world/c3kit.js (Tessa + nhà, the stack, nhãn, lớp bắt buộc — C3 đã duyệt) + phần mới của C4: Tessa CỬ ĐỘNG (tay + nghiêng người, hàng chờ C4
// gates/C3.md §3 #1), vật khoản vay riêng gắn với nhà (LoanTag, S01), thẻ hai khoản (V4 adapted, S02–S03), dải tuần (V1 xem trước, S02), lớp bắt buộc
// có đối trọng, cảnh khung cho đoạn chưa dựng. Mốc giờ CHỈ từ spine.json của đoạn; hằng số ở đây = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { Studio, Stack, setOpacity, PALETTE } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, ease, lin, mix, rgba } from '/toolkit/factory/world/core.js';
import { home, nameTag, theStack, stackSet, BUNDLE_TH, label, brace, modeLook, FIG } from '/episodes/ep007/world/c3kit.js';

export const POP = 0.2, PLATE = '#0B0E13';
// màu nhận diện (không mang nghĩa dữ liệu) — contract.json characters: Tessa = PALETTE.person2 (C3), Leo = PALETTE.person1
export const CHAR = { tessa: FIG, leo: PALETTE.person1 };
export const kf = (k, t) => { if (!k || !k.length) return 0; if (t <= k[0][0]) return k[0][1];
  for (let i = 1; i < k.length; i++) if (t <= k[i][0]) { const [a, x] = k[i - 1], [b, y] = k[i]; return b > a ? x + (y - x) * (t - a) / (b - a) : y; }
  return k[k.length - 1][1]; };
// hiện từ mốc a (dốc POP), tắt từ mốc z (dốc 0,3 s) nếu có
export const show = (t, a, z = Infinity) => (a == null ? 0 : ease(t, a - 0.05, a + POP) * (1 - ease(t, z, z + 0.3)));
export const pulse = (t, a, d = 0.6) => (a == null || t < a ? 0 : Math.max(0, 1 - (t - a) / d));

export async function setup(seg, res, poses, { shadowBox = 16 } = {}) {
  const [S, CL] = await Promise.all([loadJSON(seg + 'spine.json'), loadJSON('/episodes/ep007/world/claims.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const MV = {}; for (const m of S.moves) MV[m.id] = m;
  const st = Stage(res), scene = new THREE.Scene(), { floor, key } = Studio(scene, { shadowBox });
  const D = (k) => CL[k].display;
  return { S, CL, D, G: CL._geom, cue, MV, st, O: st.O, renderer: st.renderer, scene, floor, key, CAM: Camera(poses, S.moves) };
}
// đèn chính theo điểm nhìn (bóng có ở mọi khu của đoạn dài)
export function followLight(key, tgt) {
  key.target.position.set(tgt[0], Math.max(0, tgt[1]), tgt[2]); key.position.set(tgt[0] - 6, Math.max(0, tgt[1]) + 14, tgt[2] + 10); key.target.updateMatrixWorld();
}

// ================================================================ Tessa có cử động (hàng chờ C4 #1: "đứng yên cả 5 đoạn ở chế độ đồ thị")
// Người W4 tròn xoay → quay đầu không thấy được từ chính diện. Cử động đọc được ở máy chính diện: (1) NGHIÊNG người về phía vật (xoay quanh trục
// nhìn), (2) GIƠ TAY (cánh tay viên nang cùng màu, buông dọc thân lúc nghỉ) về phía vật, (3) gật nhẹ (đầu hạ 0,03). Mỗi cử động = một sự kiện
// {t, kind: 'arm'|'lean'|'nod', to: x thế giới của vật, hold} trong spine (S.gestures) — đúng lúc vật chạm/dâng.
export function figure(scene, opts) {
  const hm = home(scene, opts), p = hm.person, h = hm.h;
  const body = p.children[0], head = p.children[1], m = body.material;
  const pivot = new THREE.Group(); pivot.position.set(0, h * 0.66, 0); p.add(pivot);
  const arm = new THREE.Mesh(new THREE.CapsuleGeometry(h * 0.045, h * 0.3, 4, 8), m); arm.position.y = -(h * 0.15 + h * 0.045); arm.castShadow = true; pivot.add(arm);
  hm.pivot = pivot; hm.head = head; hm.headY = head.position.y; hm.body = body;
  // cánh tay nghỉ: sát thân về phía vật gần nhất (bên phải nếu không có sự kiện)
  pivot.position.x = h * 0.17;
  return hm;
}
export function gesture(hm, t, G = []) {
  let lean = 0, arm = 0, nod = 0, side = 1;
  for (const g of G) {
    const a = ease(t, g.t - 0.12, g.t + 0.28) * (1 - ease(t, g.t + (g.hold ?? 1.2), g.t + (g.hold ?? 1.2) + 0.45));
    if (a <= 0) continue;
    const s = Math.sign((g.to ?? hm.person.position.x + 1) - hm.person.position.x) || 1;
    if (g.kind === 'arm') { if (a > arm) { arm = a; side = s; } lean = Math.max(lean, 0.35 * a); }
    else if (g.kind === 'lean') { if (a > lean) side = s; lean = Math.max(lean, a); }
    else nod = Math.max(nod, a);
  }
  const p = hm.person, h = hm.h;
  p.rotation.z = -side * 0.16 * lean;
  hm.pivot.position.x = side * h * 0.17;
  hm.pivot.rotation.z = side * (0.1 + 2.25 * arm);          // buông (0,1 rad ra ngoài) → giơ chéo lên về phía vật
  hm.head.position.y = hm.headY - 0.035 * Math.sin(Math.PI * Math.min(1, nod * 1.0));
}

// tên dưới chân Tessa chỉ khi người trong khung (c3kit.nameTag kẹp tâm x ≥ 330: người ngoài khung vẫn có tên ở mép → sai chỗ)
export function figTag(O, hm, a = 1) {
  const [x] = O.toScreen(hm.person.position.x, 0.5, hm.person.position.z), v = Math.min(1, Math.max(0, Math.min(x - 40, 1880 - x) / 80));
  return nameTag(O, hm, a * v);
}

// ================================================================ khoản vay $320,000 = VẬT RIÊNG gắn với nhà (hàng chờ C4 #2: chồng đọc thành "the loan is $720")
// Tấm giấy vay (khung ink-muted = vật cố định, mặt sáng, hai dòng chữ giả) trên cột ngắn trước góc phải nhà — cùng nhóm với nhà, không giống bó tiền
export function LoanTag(scene, hm) {
  const g = new THREE.Group(), w = hm.w;
  const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.8, transparent: true, ...o });
  const post = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.62, 0.05), mat('#8C93A0')); post.position.y = 0.31;
  const plate = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.36, 0.03), mat('#E6E9EE', { emissive: new THREE.Color('#E6E9EE'), emissiveIntensity: 0.15 })); plate.position.y = 0.74;
  const rim = new THREE.Mesh(new THREE.BoxGeometry(0.56, 0.42, 0.02), mat(C.muted)); rim.position.set(0, 0.74, -0.012);
  const lines = [0.08, 0, -0.08].map((dy, i) => { const l = new THREE.Mesh(new THREE.BoxGeometry(i === 2 ? 0.22 : 0.36, 0.022, 0.01), mat('#5B6573')); l.position.set(i === 2 ? -0.07 : 0, 0.74 + dy, 0.02); return l; });
  for (const m of [post, plate, rim, ...lines]) { m.castShadow = true; g.add(m); }
  g.position.set(hm.house.position.x + w * 0.5 + 0.12, 0, hm.house.position.z + w * 0.36 + 0.25); scene.add(g);
  g.userData.checks = { role: 'mark', key: 'loan-tag', series: 'principal' };
  g.set = (a) => { setOpacity(g, a); g.scale.setScalar(Math.max(0.001, 0.6 + 0.4 * a)); };
  g.top = () => [g.position.x, 0.95, g.position.z];
  g.set(0);
  return g;
}

// ================================================================ V4 adapted: thẻ hai khoản vay (B02–B03, B33) — mặt tối viền ink-muted, chữ ở lớp phủ (đồ thị)
export function OfferCard(scene, { x, y, z = 0, w = 1.7, h = 0.66 } = {}) {
  const g = new THREE.Group();
  const face = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.04), new THREE.MeshStandardMaterial({ color: '#1A1F28', roughness: 0.6, transparent: true }));
  const rim = new THREE.Mesh(new THREE.BoxGeometry(w + 0.06, h + 0.06, 0.03), new THREE.MeshStandardMaterial({ color: C.muted, emissive: new THREE.Color(C.muted), emissiveIntensity: 0.3, transparent: true }));
  rim.position.z = -0.02;
  const band = new THREE.Mesh(new THREE.BoxGeometry(w, 0.09, 0.05), new THREE.MeshStandardMaterial({ color: C.cushion, emissive: new THREE.Color(C.cushion), emissiveIntensity: 0.5, transparent: true }));
  band.position.set(0, -h / 2 + 0.07, 0.01);
  g.add(rim, face, band); g.position.set(x, y, z); scene.add(g);
  g.userData.checks = { role: 'mark', key: 'offer-card' };
  g.set = ({ a = 1, band: b = 0 } = {}) => { setOpacity(g, a); band.visible = a > 0.01 && b > 0.01; band.scale.x = Math.max(0.001, b); band.material.opacity = a; g.scale.setScalar(Math.max(0.001, 0.7 + 0.3 * a)); };
  g.w = w; g.h = h;
  g.set({ a: 0 });
  return g;
}

// ================================================================ V1 xem trước (B02): dải tuần — 1.833 ô, trái → phải = Aug 1991 → Oct 2026, nằm sau nhà.
// set({grow, rise, values, lastA}): grow ∈ [0,1] ô hiện trái → phải (ink-muted, mỏng); rise ∈ [0,1] mỗi ô mọc thành cột theo giá của đường lui tuần
// đó (warn, thang hình riêng); ô cuối = tuần của Tessa, sáng (lastA).
export function WeekStrip(scene, values, { x0 = -9, width = 15, z = -3.2, depth = 0.5, tileH = 0.05, unit = 2.6 / 30000 } = {}) {
  const n = values.length, pitch = width / n;
  const geo = new THREE.BoxGeometry(pitch * 0.92, 1, depth); geo.translate(0, 0.5, 0);
  const mesh = new THREE.InstancedMesh(geo, new THREE.MeshStandardMaterial({ roughness: 0.8, transparent: true, emissive: new THREE.Color('#000000') }), n);
  mesh.frustumCulled = false; mesh.castShadow = true; mesh.receiveShadow = true; scene.add(mesh);
  const M4 = new THREE.Matrix4(), col = new THREE.Color(), cM = new THREE.Color(C.muted), cW = new THREE.Color(C.warn), cI = new THREE.Color(C.ink), hide = new THREE.Matrix4().makeScale(0, 0, 0);
  for (let i = 0; i < n; i++) mesh.setColorAt(i, cM);
  mesh.userData.checks = { role: 'series', key: 'week-strip', series: 'weeks' };
  const api = { mesh, n, pitch, x0, z, xOf: (i) => x0 + (i + 0.5) * pitch,
    set({ grow = 1, rise = 0, lastA = 0, a = 1 } = {}) {
      const L = grow * (n + 120);
      for (let i = 0; i < n; i++) {
        const g = Math.min(1, Math.max(0, (L - i) / 120));
        if (g <= 0.001) { mesh.setMatrixAt(i, hide); continue; }
        const r = Math.min(1, Math.max(0, rise * 1.25 - 0.25 * i / n));
        const hgt = Math.max(0.001, mix(tileH, values[i] * unit, r) * g);
        M4.makeScale(1, hgt, 1).setPosition(api.xOf(i), 0, z); mesh.setMatrixAt(i, M4);
        col.copy(cM).lerp(cW, r); if (i === n - 1) col.lerp(cI, lastA);
        mesh.setColorAt(i, col);
      }
      mesh.instanceMatrix.needsUpdate = true; mesh.instanceColor.needsUpdate = true;
      mesh.material.opacity = a; mesh.visible = a > 0.005;
    } };
  api.set({ grow: 0 });
  return api;
}

// ================================================================ W2 tháp bó (S08–S09): ĐÚNG bó của the stack (mệnh giá cố định G.bundle_usd, dày BUNDLE_TH, cỡ 0,9 × 0,6),
// xếp mỗi tầng cols × rows bó → tổng lãi hàng trăm nghìn đô la vẫn vừa khung thường; phần trên cùng (warnFrom) tô warn; bó ≥ hideFrom không vẽ (đang
// bay). Gốc = tâm đáy. set({count (bó, thực), warnFrom, hideFrom, a}); posOf(k) = tâm bó k (thế giới); topY(count) = đỉnh tầng cao nhất
export function BundleTower(scene, { x, z = 0, n, cols = 3, rows = 3, bw = 0.9, bd = 0.6, gap = 0.04, name = 'tower' } = {}) {
  const cap = Math.ceil(n) + 1, th = BUNDLE_TH, per = cols * rows;
  const geo = new THREE.BoxGeometry(bw, th * 0.92, bd), mesh = new THREE.InstancedMesh(geo, new THREE.MeshStandardMaterial({ roughness: 0.8, transparent: true }), cap);
  const strap = new THREE.InstancedMesh(new THREE.BoxGeometry(bw * 0.16, th * 0.94, bd * 1.02), new THREE.MeshStandardMaterial({ color: PALETTE.strap, roughness: 0.85, transparent: true }), cap);
  const g = new THREE.Group(); g.add(mesh, strap); g.position.set(x, 0, z); scene.add(g);
  mesh.castShadow = mesh.receiveShadow = true; mesh.frustumCulled = strap.frustumCulled = false;
  const M4 = new THREE.Matrix4(), col = new THREE.Color(), hide = new THREE.Matrix4().makeScale(0, 0, 0);
  for (let k = 0; k < cap; k++) mesh.setColorAt(k, col.set(PALETTE.bill));
  const local = (k) => { const L = Math.floor(k / per), c = k % per; return [(c % cols - (cols - 1) / 2) * (bw + gap), L * th + th / 2, (Math.floor(c / cols) - (rows - 1) / 2) * (bd + gap)]; };
  g.userData.checks = { role: 'bar', series: name, key: `tower-${name}` };
  g.set = ({ count = 0, warnFrom = Infinity, hideFrom = Infinity, a = 1 } = {}) => {
    for (let k = 0; k < cap; k++) {
      const frac = Math.min(1, Math.max(0, count - k));
      if (frac <= 0.001 || k >= hideFrom) { mesh.setMatrixAt(k, hide); strap.setMatrixAt(k, hide); continue; }
      const [lx, ly, lz] = local(k);
      M4.makeScale(1, frac, 1).setPosition(lx, ly - th * (1 - frac) / 2, lz); mesh.setMatrixAt(k, M4); strap.setMatrixAt(k, M4);
      mesh.setColorAt(k, col.set(k >= warnFrom ? PALETTE.warn : Math.floor(k / per) % 2 ? PALETTE.bill : PALETTE.bill2));
    }
    mesh.instanceMatrix.needsUpdate = strap.instanceMatrix.needsUpdate = true; mesh.instanceColor.needsUpdate = true;
    mesh.material.opacity = strap.material.opacity = a; g.visible = a > 0.005 && count > 0.001;
    g.userData.checks.value = +count.toFixed(2);
  };
  g.posOf = (k) => { const [lx, ly, lz] = local(k); return [x + lx, ly, z + lz]; };
  g.topY = (count) => (Math.floor(Math.max(0, count - 1e-6) / per) + 1) * th;
  g.halfW = (cols * (bw + gap) - gap) / 2;
  g.set({ count: 0 });
  return g;
}

// ================================================================ lớp bắt buộc: ILLUSTRATIVE (mọi khung có Tessa/Leo) + nguồn + "US only · history, not a forecast"
// (mọi khung: mọi số của tập là lãi khảo sát đã qua) + đối trọng (cw) dòng trên history khi có
export const SRC = 'Freddie Mac weekly mortgage survey';
export function chrome(O, { illus = 1, cw = null, cwA = 1 } = {}) {
  O.chrome({ illus: illus > 0.01, illusA: illus, src: SRC, hist: true, ...(cw && cwA > 0.01 ? { cw, cwA } : {}) });
}
// đoạn thẳng lớp phủ (nét có ghi log.lines cho F-2)
export function seg2(O, x0, y0, x1, y1, color, a, lw = 4, dash = null) {
  if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = color; c.lineWidth = lw; if (dash) c.setLineDash(dash);
  c.beginPath(); c.moveTo(x0, y0); c.lineTo(x1, y1); c.stroke(); c.restore();
}
// ngoặc đứng (V6, nét lớp phủ): x, y0 (trên) → y1 (dưới), chân hướng trái (tick > 0 = về phía vật bên trái)
export function vbrace(O, x, y0, y1, color, a, lw = 6, tick = 16) {
  if (a <= 0.01) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.strokeStyle = color; c.lineWidth = lw;
  c.beginPath(); c.moveTo(x - tick, y0); c.lineTo(x, y0); c.lineTo(x, y1); c.lineTo(x - tick, y1); c.stroke(); c.restore();
}
// mở/kết đoạn: phủ nền tối dần (ranh giới đoạn; ident ở đoạn a). Vẽ TRƯỚC mọi chữ (chữ giữ tương phản)
export function dip(O, a) { if (a <= 0.005) return; const c = O.ctx; c.save(); c.globalAlpha = a; c.fillStyle = C.bg; c.fillRect(0, 0, 1920, 1080); c.restore(); }

// ================================================================ cảnh KHUNG cho đoạn chưa dựng (lượt 2): Tessa + nhà đứng yên, lớp bắt buộc
export async function stubScene(seg, res) {
  const poses = { w: { pos: [-3.4, 2.2, 7.6], tgt: [-0.6, 0.8, 0], fov: 35, chart: 0 } };
  const { S, st, O, renderer, scene, floor, CAM } = await setup(seg, res, poses);
  const hm = figure(scene, { x: 0 });
  function frame(t) {
    const pose = CAM.apply(t), cam = CAM.cam; modeLook(scene, floor, pose.chart); gesture(hm, t, S.gestures || []);
    renderer.render(scene, cam);
    const log = O.begin(t, pose.chart, cam); log.roi = {};
    figTag(O, hm); chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}

export { C, ease, lin, mix, rgba, THREE, Stack, setOpacity, PALETTE, home, nameTag, theStack, stackSet, BUNDLE_TH, label, brace, modeLook, FIG };
