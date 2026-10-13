// Tập 7 · C4 · TIỆN ÍCH CHUNG cho bảy đoạn thế giới của tập (world/c4/<đoạn>/scene.js). Không đổi thư viện nhà máy (lib3d.js / core.js).
// Gốc: world/c3kit.js (Tessa + nhà, the stack, nhãn, lớp bắt buộc — C3 đã duyệt) + phần mới của C4: Tessa CỬ ĐỘNG (tay + nghiêng người, hàng chờ C4
// gates/C3.md §3 #1), vật khoản vay riêng gắn với nhà (LoanTag, S01), thẻ hai khoản (V4 adapted, S02–S03), dải tuần (V1 xem trước, S02), lớp bắt buộc
// có đối trọng, cảnh khung cho đoạn chưa dựng. Mốc giờ CHỈ từ spine.json của đoạn; hằng số ở đây = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { Studio, Stack, setOpacity, PALETTE } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, CK, ease, lin, mix, rgba } from '/toolkit/factory/world/core.js';
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
  const body = p.children[0], head = p.children[1];
  // nhân vật thứ hai (Leo, S29–S33): màu nhận diện riêng (contract.json characters) + tên trong khai trang kiểm
  if (opts.color) { body.material = body.material.clone(); body.material.color.set(opts.color); head.material = body.material; }
  if (opts.char) p.userData.checks = { role: 'mark', char: opts.char, key: `person-${opts.char.toLowerCase()}` };
  hm.char = opts.char || 'Tessa';
  const m = body.material;
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
  if (hm.char && hm.char !== 'Tessa') {   // Leo: cùng chỗ (ngay dưới chân), cùng cỡ như c3kit.nameTag
    const [fx, fy] = O.toScreen(hm.person.position.x, 0, hm.person.position.z);
    return label(O, `${hm.char} · ILLUSTRATIVE`, Math.max(330, fx), Math.min(880, fy + 50), { align: 'center', kind: 'name', px: 48, w: 600, alpha: a * v, char: hm.char });
  }
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
// cảnh MÔ PHỎNG khoản vay của Tessa (S21–S25: tính trên lãi khảo sát của tuần 8/10/2026, không phải chuỗi lịch sử) — gates/C3.md §3 "xét tiêu đề nguồn":
// tiêu đề nói rõ là phép tính trên lãi của một tuần; dòng "US only · history, not a forecast" và ILLUSTRATIVE giữ nguyên (luật kênh)
export const SRC_SIM = (D) => `Loan math at the ${D('last_week_short')} survey rate`;
export function chrome(O, { illus = 1, cw = null, cwA = 1, src = SRC } = {}) {
  O.chrome({ illus: illus > 0.01, illusA: illus, src, hist: true, ...(cw && cwA > 0.01 ? { cw, cwA } : {}) });
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

// ================================================================ V1 lưới phát lại (B10): 1.833 ô, cột = một năm (1991 … 2026, trái → phải = thời gian), hàng = tuần trong
// năm (tuần đầu năm ở trên). Tường đứng sau trục thời gian chung của đoạn c. set({fill, lastA, wave, a}): fill = số tuần đã hiện (thực, theo thứ
// tự thời gian); lastA: ô cuối (tuần của Tessa) sáng ink + to ×1,6; wave = chỉ số tuần đang loé (sóng "hỏi câu của cô ở mọi tuần trước", phải → trái)
export function WeekGrid(scene, weeks, { x0, width, y0 = 0.3, height = 4.5, z = -0.6, name = 'replay-grid' } = {}) {
  const n = weeks.length, Y0 = +weeks[0].slice(0, 4), ncol = +weeks[n - 1].slice(0, 4) - Y0 + 1, col = [], row = [];
  let yr = -1, k = 0; for (const w of weeks) { const y = +w.slice(0, 4) - Y0; if (y !== yr) { yr = y; k = 0; } col.push(y); row.push(k++); }
  const nrow = Math.max(...row) + 1, cw = width / ncol, ch = height / nrow;
  const mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(cw * 0.86, ch * 0.76, 0.04), new THREE.MeshStandardMaterial({ roughness: 0.7, transparent: true }), n);
  mesh.frustumCulled = false; scene.add(mesh); mesh.userData.checks = { role: 'series', series: 'weeks', key: name };
  const M4 = new THREE.Matrix4(), c = new THREE.Color(), cE = new THREE.Color(C.grid), cM = new THREE.Color(C.muted), cI = new THREE.Color(C.ink), hide = new THREE.Matrix4().makeScale(0, 0, 0);
  const at = (i) => [x0 + (col[i] + 0.5) * cw, y0 + height - (row[i] + 0.5) * ch, z];
  const api = { mesh, n, at, cw, ch, x0, z, top: y0 + height,
    box: (i) => { const [x, y] = at(i); return [[x - cw * 0.43, y - ch * 0.38, z], [x + cw * 0.43, y + ch * 0.38, z]]; },
    set({ fill = n, lastA = 0, wave = null, waveW = 60, a = 1 } = {}) {
      for (let i = 0; i < n; i++) {
        const f = Math.min(1, Math.max(0, fill - i));
        if (f <= 0.001 || a <= 0.005) { mesh.setMatrixAt(i, hide); continue; }
        const [x, y] = at(i), last = i === n - 1 ? lastA : 0, s = (0.4 + 0.6 * f) * (1 + 0.6 * last);
        M4.makeScale(s, s, 1).setPosition(x, y, z); mesh.setMatrixAt(i, M4);
        const wv = wave == null ? 0 : Math.max(0, 1 - Math.abs(i - wave) / waveW);
        c.copy(cE).lerp(cM, f).lerp(cI, Math.max(last, 0.85 * wv)); mesh.setColorAt(i, c);
      }
      mesh.instanceMatrix.needsUpdate = true; if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
      mesh.material.opacity = a; mesh.visible = a > 0.005 && fill > 0;
    } };
  api.set({ fill: 0 });
  return api;
}

// ================================================================ W2 hàng chồng theo tuần (B13–B20): 1.833 cột mảnh, cao = giá đường lui của tuần (extra_total) theo CÙNG
// thang của bó the stack (unit = BUNDLE_TH / bundle_usd → cột của tuần Tessa cao đúng bằng 15 bó). Gốc = mặt sàn. set({grow, rise, lit, hi, dx, a}):
// grow = phần tuần (trái → phải) đã mọc; rise ∈ [0,1] hệ số chiều cao; lit(i) ∈ [0,1] độ sáng (warn ↔ warn tối); hi(i) ∈ [0,1] → ink; dx(i) dời ngang (tách thập kỷ)
export function WeekRow(scene, values, { x0, width, z = 0, depth = 0.3, unit, name = 'weekly-stacks' } = {}) {
  const n = values.length, pitch = width / n;
  const geo = new THREE.BoxGeometry(pitch * 0.92, 1, depth); geo.translate(0, 0.5, 0);
  const mesh = new THREE.InstancedMesh(geo, new THREE.MeshStandardMaterial({ roughness: 0.8, transparent: true }), n);
  mesh.frustumCulled = false; mesh.castShadow = true; scene.add(mesh); mesh.userData.checks = { role: 'series', series: 'extra_total', key: name };
  const M4 = new THREE.Matrix4(), c = new THREE.Color(), cW = new THREE.Color(C.warn), cD = new THREE.Color('#4A3F2A'), cI = new THREE.Color(C.ink), hide = new THREE.Matrix4().makeScale(0, 0, 0);
  const api = { mesh, n, pitch, x0, z, unit, h: (i) => values[i] * unit, xOf: (i, dx = 0) => x0 + (i + 0.5) * pitch + dx,
    // span(i) → [y0, y1] thay chiều cao mặc định (cột "khoảng chênh" của đoạn c: từ hai đường lãi xuống trục, rồi thành chồng); color(i, c) tô thẳng
    set({ grow = 1, rise = 1, lit = null, hi = null, dx = null, span = null, color = null, a = 1 } = {}) {
      const L = grow * (n + 90);
      for (let i = 0; i < n; i++) {
        const g = Math.min(1, Math.max(0, (L - i) / 90)) * rise;
        if (g <= 0.001 || a <= 0.005) { mesh.setMatrixAt(i, hide); continue; }
        const [y0, y1] = span ? span(i) : [0, values[i] * unit];
        M4.makeScale(1, Math.max(0.001, (y1 - y0) * g), 1).setPosition(api.xOf(i, dx ? dx(i) : 0), y0, z); mesh.setMatrixAt(i, M4);
        if (color) color(i, c); else { c.copy(cD).lerp(cW, lit ? lit(i) : 1); if (hi) c.lerp(cI, hi(i)); }
        mesh.setColorAt(i, c);
      }
      mesh.instanceMatrix.needsUpdate = true; if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
      mesh.material.opacity = a; mesh.visible = a > 0.005 && grow > 0;
    } };
  api.set({ grow: 0 });
  return api;
}

// ================================================================ N1 Month track, BẢN C4 (S21–S24) — sửa lỗi CHÍNH của C3 (C3-answer câu 1: "lớp trả thêm không thấy bằng hình")
// bằng ĐỔI LOẠI HÌNH (không chỉ độ sáng): lớp trả thêm là TẤM NỔI có độ dày (0,075 ≈ ô bắt buộc), phủ 86 % mặt ô, cạnh bên thấy được từ góc 3/4,
// phát quang ink; mỗi cột-năm có tấm RƠI từ trên cao xuống (drop[c] ∈ [0,1], một nốt mỗi cột); ô bắt buộc TỐI HẲN xuống (ink-muted → xám đậm) khi
// tấm của cột tới (cover[c]) → tương phản tấm sáng / ô tối. Gom năm (S23): 12 tấm của cột trượt về ô thứ 12 và chồng thành khối 12 lớp CÓ KHE
// (SG = 0,03 giữa hai lớp → đếm được); màu lưới không đổi khi gom. Ô trễ (warn) to ×1,2 và cao ×2,5; vách 15 năm thấp (0,18) và trong mờ → không
// che ô trễ. Bóng lịch 30 năm (ghost): 15 cột mờ quá vách = phần khoản 30 năm còn chạy nếu chỉ trả mức bắt buộc (S22.1 "ends sooner").
export const TRK = { req: '#9AA4B2', dark: '#343A44', warn: '#F2B441', ink: '#F2F4F7', empty: '#2A303B' };
export function TrackC4({ n = 180, cols = 12, spare = 2, tile = 0.34, gap = 0.08, th = 0.07, slab = 0.075, SG = 0.03, SF = 0.86, DROP = 1.3, name = 'tessa' } = {}) {
  const g = new THREE.Group(), pitch = tile + gap, years = Math.ceil(n / cols), nmax = n + spare * cols;
  const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.8, transparent: true, ...o });
  const tiles = new THREE.InstancedMesh(new THREE.BoxGeometry(tile, th, tile), mat('#FFFFFF'), nmax);
  const slabs = new THREE.InstancedMesh(new THREE.BoxGeometry(tile * SF, slab, tile * SF), mat(TRK.ink, { emissive: new THREE.Color(TRK.ink), emissiveIntensity: 0.85 }), n);
  const ghost = new THREE.InstancedMesh(new THREE.BoxGeometry(tile, 0.014, tile), mat(TRK.req, { opacity: 0.3, depthWrite: false }), n);
  for (const m of [tiles, slabs]) { m.castShadow = m.receiveShadow = true; m.frustumCulled = false; g.add(m); }
  ghost.frustumCulled = false; g.add(ghost);
  const markX = years * pitch - gap / 2, depth = cols * pitch - gap;
  const mark = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.18, depth + 0.5), mat(TRK.req, { emissive: new THREE.Color(TRK.req), emissiveIntensity: 0.4, depthWrite: false }));
  mark.position.set(markX, 0.09, -depth / 2 + tile / 2); g.add(mark);
  const pos = (i) => [Math.floor(i / cols) * pitch + tile / 2, -(i % cols) * pitch];
  const M = new THREE.Matrix4(), col = new THREE.Color(), K = { req: new THREE.Color(TRK.req), dark: new THREE.Color(TRK.dark), warn: new THREE.Color(TRK.warn), ink: new THREE.Color(TRK.ink), empty: new THREE.Color(TRK.empty) };
  const hide = new THREE.Matrix4().makeScale(0, 0, 0), cl = (x) => Math.min(1, Math.max(0, x)), sm = (u) => u * u * (3 - 2 * u);
  tiles.userData.checks = { role: 'mark', series: name, key: `track-${name}-tiles` };
  slabs.userData.checks = { role: 'mark', series: name, key: `track-${name}-extra` };
  mark.userData.checks = { role: 'mark', series: name, key: `track-${name}-mark` };
  g.userData = { n, cols, pitch, tile, th, years, nmax, markX, depth, slab, SG };
  const zEnd = pos(cols - 1)[1], arr = (v, c) => (Array.isArray(v) ? v[c] || 0 : typeof v === 'function' ? v(c) : cl(v - c));
  // lit, late: như obj7 (số ô thực); flash/cover/drop/gathered: mảng theo cột (hoặc số thực "số cột từ trái"); lift = {i, a}: tấm tháng i nhấc lên (S22.3);
  // bob(i) → độ nảy của tấm tháng i (S23: sóng "mỗi tháng một lớp"); ghost = số cột bóng 30 năm (thực), ghostA; markA
  g.set = ({ lit = n, late = 0, flash = 0, cover = 0, drop = 0, gathered = 0, lift = null, bob = null, ghost: gc = 0, ghostA = 0, markA = 1, pulse = 0 } = {}) => {
    for (let i = 0; i < nmax; i++) {
      const [x, z] = pos(i), isLate = i >= n, c = Math.floor(i / cols), a = isLate ? cl(late - (i - n)) : cl(lit - i);
      if (a <= 0.002) { tiles.setMatrixAt(i, hide); continue; }
      if (isLate) { M.makeScale(1.2, 2.5, 1.2).setPosition(x, th * 2.5 / 2, z); col.copy(K.empty).lerp(K.warn, a * (0.85 + 0.15 * pulse)); }
      else { M.makeScale(1, a, 1).setPosition(x, th * a / 2, z); col.copy(K.req).lerp(K.dark, arr(cover, c)).lerp(K.ink, 0.8 * arr(flash, c)); }
      tiles.setMatrixAt(i, M); tiles.setColorAt(i, col);
    }
    for (let i = 0; i < n; i++) {
      const c = Math.floor(i / cols), r = i % cols, d = arr(drop, c) * cl(lit - i), [x, z] = pos(i);
      if (d <= 0.002) { slabs.setMatrixAt(i, hide); continue; }
      const k = cols - 1 - r, dl = 0.35 * k / (cols - 1), e = sm(cl((arr(gathered, c) - dl) / (1 - dl))), fall = sm(d);
      const y0 = th + slab / 2 + 0.004, y1 = th + 0.004 + k * (slab + SG) + slab / 2;
      let y = y0 + (y1 - y0) * e + 0.08 * Math.sin(Math.PI * e) + (1 - fall) * DROP;
      if (bob) y += bob(i); if (lift && lift.i === i) y += 1.1 * lift.a;
      M.makeScale(1, 1, 1).setPosition(x, y, z + (zEnd - z) * e); slabs.setMatrixAt(i, M);
    }
    for (let i = 0; i < n; i++) {
      const c = Math.floor(i / cols), a = cl(gc - c) * ghostA;
      if (a <= 0.002) { ghost.setMatrixAt(i, hide); continue; }
      const [x, z] = pos(i + n); M.makeScale(1, 1, 1).setPosition(x, 0.007, z); ghost.setMatrixAt(i, M);
    }
    for (const m of [tiles, slabs, ghost]) m.instanceMatrix.needsUpdate = true;
    if (tiles.instanceColor) tiles.instanceColor.needsUpdate = true;
    ghost.material.opacity = 0.3 * Math.min(1, ghostA); ghost.visible = ghostA > 0.01 && gc > 0;
    mark.material.opacity = 0.5 * markA; mark.visible = markA > 0.01;
    tiles.userData.checks.level = +Math.min(n, lit).toFixed(2); tiles.userData.checks.late = +late.toFixed(2);
  };
  g.blockTop = (c) => { const [x, z] = pos(c * cols + cols - 1); return [g.position.x + x, g.position.y + th + cols * (slab + SG), g.position.z + z]; };
  g.tileAt = (i) => { const [x, z] = pos(i); return [g.position.x + x, g.position.y + th, g.position.z + z]; };
  g.colX = (c, side = 0) => g.position.x + c * pitch + (side < 0 ? 0 : side > 0 ? tile : tile / 2);
  g.frontZ = () => g.position.z + tile / 2;
  g.backZ = () => g.position.z - (cols - 1) * pitch - tile / 2;
  g.markWorldX = () => g.position.x + markX;
  g.set({});
  return g;
}

// ================================================================ S22.2 một khoản trả bắt buộc tách hai phần (lãi dưới, ink-muted đậm · gốc trên, ink): tổng cao CỐ ĐỊNH
// (khoản bắt buộc không đổi), phần lãi co lại theo tháng khi trả thêm → "next month's interest ↓, payment fixed". set({share, a}) share = phần lãi ∈ [0,1]
export function SplitBar({ x, z, h = 2.0, w = 0.55, d = 0.4 } = {}) {
  const g = new THREE.Group(), mk = (c, e) => new THREE.Mesh(new THREE.BoxGeometry(w, 1, d), new THREE.MeshStandardMaterial({ color: c, roughness: 0.7, transparent: true, emissive: new THREE.Color(c), emissiveIntensity: e }));
  const lo = mk(TRK.dark, 0.05), hi = mk(TRK.ink, 0.35); lo.castShadow = hi.castShadow = true; g.add(lo, hi); g.position.set(x, 0, z);
  lo.userData.checks = { role: 'bar', series: 'interest-part', key: 'split-interest' }; hi.userData.checks = { role: 'bar', series: 'principal-part', key: 'split-principal' };
  g.h = h;
  g.set = ({ share = 0.9, a = 1 } = {}) => {
    const hl = Math.max(0.001, h * share), hh = Math.max(0.001, h - hl);
    lo.scale.y = hl; lo.position.y = hl / 2; hi.scale.y = hh; hi.position.y = hl + hh / 2;
    setOpacity(g, a); lo.userData.checks.value = +share.toFixed(3);
  };
  g.set({ a: 0 });
  return g;
}

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

export { C, CK, ease, lin, mix, rgba, THREE, Stack, setOpacity, PALETTE, home, nameTag, theStack, stackSet, BUNDLE_TH, label, brace, modeLook, FIG };
