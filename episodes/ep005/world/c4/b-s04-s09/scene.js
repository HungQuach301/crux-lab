// Tập 5 · C4 · ĐOẠN B = S04–S09 (Hồi 1) + MR1. Mốc giờ chỉ từ spine.json; hằng số = hình học + độ dài hiệu ứng chung.
// Khu: HX nhà + khiên + người vay/cho vay + lịch (S04) · đồ thị giá (S05) · đồ thị khoản trả N1 (S06, code C3 vòng 3) · cùng đường đó phóng vào
// 0–10 năm (S07–S08) · căn nhà NGOÀI khung đồ thị (S08.3) → nhà trên chồng giá trị (S09.1) · hai chồng chính diện (S09.2–S09.4) · phố (MR1, c4kit).
import * as THREE from 'three';
import { House, Stack, Beam, Person, Ribbon, Studio, Shield, Burst, PALETTE, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, lin, ease, easeOut, mix } from '/toolkit/factory/world/core.js';
import { Calendar } from '/episodes/ep005/world/obj5.js';
import { cues, moves, flyGuard, measure, followLight, Street, POP, PLATE } from '/episodes/ep005/world/c4kit.js';

const SEG = '/episodes/ep005/world/c4/b-s04-s09/';
const HX = -13, UNIT = 9e4, UW = 2e5, UP = 1e5, UD = 1e5;
const XK = (k) => 6 + 9 * k / 360;                 // đồ thị khoản trả: kỳ 0 → 360
const CX = 4.4, VX = 17.6, DX = 24;                // lịch đồ thị · căn nhà ngoài khung · hai chồng (S09.2)

export async function boot(res) {
  const [S, CL] = await Promise.all([loadJSON(SEG + 'spine.json'), loadJSON('/episodes/ep005/world/claims.json')]);
  await fonts();
  const b = cues(S), M = moves(S);
  const r = CL.rate_latest.value / 1200, bal = (k) => Math.pow(1 + r, k) - (Math.pow(1 + r, k) - 1) / (1 - Math.pow(1 + r, -360));
  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor, key } = Studio(scene, { shadowBox: 16 });
  const ST = Street(scene);
  const poses = {
    wPMI: { pos: [HX + 0.9, 1.9, 10.8], tgt: [HX + 0.7, 1.2, 0], fov: 35, chart: 0 },
    wCal: { pos: [HX + 2.4, 1.55, 6.4], tgt: [HX + 2.4, 1.05, 0], fov: 35, chart: 0 },
    fEx: { pos: [HX + 7.5, 1.7, 9.0], tgt: [HX + 11.0, 1.5, 0], fov: 35, chart: 0 },
    cPrice: { pos: [0.9, 2.3, 34], tgt: [0.9, 2.3, 0], fov: 12, chart: 1 },
    cPay: { pos: [10.2, 2.9, 35.2], tgt: [10.2, 2.9, 0], fov: 16, chart: 1 },
    cSched80: { pos: [XK(62), 3.7, 12], tgt: [XK(62), 3.7, 0], fov: 8.4, chart: 1 },
    cWide: { pos: [11.4, 2.3, 40], tgt: [11.4, 2.3, 0], fov: 14, chart: 1 },
    fVal: { pos: [VX - 2.5, 1.9, 10.5], tgt: [VX + 0.5, 1.5, 0], fov: 35, chart: 0 },
    wValue: { pos: [VX + 2.2, 2.2, 8.2], tgt: [VX, 1.9, 0], fov: 35, chart: 0 },
    fShare: { pos: [VX + 5.5, 2.4, 11.0], tgt: [DX + 0.5, 2.2, 0], fov: 35, chart: 0 },
    cDef2: { pos: [DX + 2.5, 3.4, 40], tgt: [DX + 2.5, 3.4, 0], fov: 11, chart: 1 },
    fStreet: { pos: [DX + 12, 2.0, 14], tgt: [DX + 18, 1.2, 0], fov: 35, chart: 0 },
    ...ST.poses,
  };
  const CAM = Camera(poses, S.moves);
  // ---------- S04 thế giới: nhà + khiên, người vay, người cho vay, lịch, chồng 10 % dưới vạch 20 %
  const house = House({ w: 1.6 }); house.position.set(HX, 0, -0.4); scene.add(house);
  const shield = Shield({ size: 0.8 }); const roofY = house.userData.height * 0.86; shield.position.set(HX, roofY, -0.15); scene.add(shield);
  const you = Person({ h: 1.15, color: PALETTE.person2 }); you.position.set(HX + 1.6, 0, 0.6); you.rotation.y = -0.3; scene.add(you);
  const lender = Person({ h: 1.2, color: PALETTE.person1 }); lender.position.set(HX - 2.1, 0, 0.5); lender.rotation.y = 0.4; scene.add(lender);
  const cal = Calendar({ w: 1.0, h: 1.25 }); cal.position.set(HX + 3.2, 0, 0.3); cal.rotation.y = -0.2; scene.add(cal);
  const save = Stack({ unitUsd: UW, w: 0.8, d: 0.55 }); save.position.set(HX + 2.35, 0, 1.4); save.set({ usd: 40000, tintBelowUsd: 1e9, tint: C.cushion, tintA: 1 }); scene.add(save);
  const bar20 = Beam({ length: 1.1, color: C.muted }); bar20.position.set(HX + 2.35, 80000 / UW, 1.4); scene.add(bar20);
  const tabs = [0, 1, 2].map(() => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.26, 0.16, 0.02), new THREE.MeshStandardMaterial({ color: C.warn, emissive: new THREE.Color(C.warn), emissiveIntensity: 0.3, transparent: true })); scene.add(m); return m; });
  const tabT = [b.p1.month, b.p1.month + 0.75, b.p1.top];
  // ---------- S05 đồ thị giá
  const price = Stack({ unitUsd: UP, w: 1.1, d: 0.7 }); scene.add(price);
  const down = Stack({ unitUsd: UP, w: 1.1, d: 0.7 }); down.set({ usd: 40000, tintBelowUsd: 1e9, tint: C.cushion, tintA: 1 }); scene.add(down);
  const pHouse = House({ w: 1.3 }); pHouse.position.set(2.1, 0, 0); scene.add(pHouse);
  const med = Beam({ length: 2.0, color: C.muted }); med.position.set(0, CL.ex_price.value * 0 + 410700 / UP, 0); scene.add(med);
  // ---------- S06 đồ thị khoản trả (N1)
  const pcal = Calendar({ w: 1.2, h: 1.5 }); pcal.position.set(CX, 0, 0.2); scene.add(pcal);
  const loan = Stack({ unitUsd: UNIT, w: 0.75, d: 0.5, maxUsd: 4e5 }); scene.add(loan);
  const line = Ribbon({ color: C.ink, z: 0.42 }); scene.add(line);
  const sched = Ribbon({ color: C.muted, z: 0.4 }); scene.add(sched);
  const schedPts = []; for (let j = 0; j <= 360; j += 2) schedPts.push([XK(j), 360000 * bal(j) / UNIT]);
  const b80 = Beam({ length: XK(130) - XK(0), color: C.muted }); b80.position.set((XK(0) + XK(130)) / 2, 320000 / UNIT, 0.3); b80.scale.y = 0.35; scene.add(b80);
  const b78 = Beam({ length: XK(130) - XK(0), color: C.muted }); b78.position.set((XK(0) + XK(130)) / 2, 312000 / UNIT, 0.3); b78.scale.y = 0.35; scene.add(b78);
  const burst = Burst(); scene.add(burst);
  // ---------- S08.3–S09.1 căn nhà ngoài khung → trên chồng giá trị
  const vStackW = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); vStackW.position.set(VX, 0, 0); scene.add(vStackW);
  const vHouse = House({ w: 1.5 }); scene.add(vHouse);
  // ---------- S09.2 hai chồng chính diện
  const dV = Stack({ unitUsd: UD, w: 1.3, d: 0.8 }), dL = Stack({ unitUsd: UD, w: 1.3, d: 0.8 }); dV.position.set(DX, 0, 0); dL.position.set(DX + 3.0, 0, 0); scene.add(dV, dL);
  const d80 = Beam({ length: 5.6, color: C.ink }); d80.position.set(DX + 1.5, 0, 0.1); scene.add(d80);
  const dSch = Beam({ length: 5.6, color: C.muted }); dSch.position.set(DX + 1.5, 320000 / UD, 0.05); dSch.scale.y = 0.4; scene.add(dSch);
  const WORLD = { house, shield, you, lender, cal, save, vHouse, vStackW, pHouse, street: ST.g };

  function frame(t) {
    CAM.apply(t); const pose = flyGuard(CAM, S.moves, t), cw = CAM.poseAt(t).chart, cam = CAM.cam;
    followLight(key, pose.tgt);
    floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = mix(30, 150, cw); scene.fog.far = mix(80, 300, cw);
    // S04
    setOpacity(lender, ease(t, b.p1.lender - 0.05, b.p1.lender + 0.3)); setOpacity(bar20, ease(t, b.p0.twenty - 0.05, b.p0.twenty + POP));
    const fq = t < b.p3.measure ? -1 : t < b.p4.end ? ((t - b.p3.measure) / (b.p4.end - b.p3.measure)) * 6 : -1;   // S04.4 lật nhanh → dừng ở "end"
    let flip = 0; for (const tt of tabT) if (t >= tt - 0.1 && t < tt + 0.45) flip = lin(t, tt - 0.1, tt + 0.45);
    if (fq >= 0) flip = fq % 1;
    cal.set({ flip, pages: 1 - 0.1 * Math.min(6, Math.max(0, fq)) / 6, glow: 0 });
    tabs.forEach((m, i) => { const u = easeOut(t, tabT[i], tabT[i] + 0.7); m.visible = t >= tabT[i] && u < 1;
      m.position.set(mix(HX + 3.2, HX + 0.25, u), mix(0.9, roofY + 0.1, u) + Math.sin(Math.PI * u) * 0.8, mix(0.45, 0.0, u)); m.material.opacity = 1 - lin(t, tabT[i] + 0.55, tabT[i] + 0.7); });
    // S05
    const dn = easeOut(t, b.e1.ten - 0.05, b.e1.ten + 0.6);
    price.position.set(0, 40000 / UP, 0); price.set({ usd: 400000, fromUsd: 40000, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 });
    down.position.set(-1.45 * dn, 0, 0); const e5v = t < M.m_pay.t1 ? 1 : 0; setOpacity(price, e5v); setOpacity(down, e5v); setOpacity(pHouse, e5v); setOpacity(med, ease(t, b.e0.median - 0.05, b.e0.median + POP));
    // S06–S08: kỳ trả
    const k = t < b.y2.each ? 0 : Math.min(S.k_stop, S.k_stop * (t - S.pay_kf[0][0]) / (S.pay_kf[1][0] - S.pay_kf[0][0]));
    const pflip = t < b.y0.monthly ? 0 : t < b.y2.each ? (t < b.y0.monthly + 0.5 ? lin(t, b.y0.monthly - 0.1, b.y0.monthly + 0.4) : 0) : (k >= S.k_stop ? 0 : (k / 3) % 1);
    const p6v = t >= M.m_pay.t0 && t < M.m_val.t1 ? 1 : 0; setOpacity(pcal, p6v); setOpacity(vHouse, t >= M.m_wide.t0 ? 1 : 0);
    pcal.set({ flip: pflip, pages: 1 - k / 360 * 0.9, glow: 0 });
    const usd = 360000 * bal(k); loan.position.set(XK(k), 0, 0); loan.set({ usd, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 }); setOpacity(loan, p6v);
    const pts = []; for (let j = 0; j <= Math.floor(k); j += 2) pts.push([XK(j), 360000 * bal(j) / UNIT]); pts.push([XK(k), usd / UNIT]);
    line.set(pts, 0.07, C.ink); line.material.opacity = t >= b.y2.each && t < M.m_val.t1 ? 1 : 0;
    const np = Math.max(2, Math.round(lin(t, b.y2.each, b.y2.each + 0.6) * schedPts.length)); sched.set(schedPts.slice(0, np), 0.05, C.muted); sched.material.opacity = t >= b.y2.each && t < M.m_val.t1 ? 0.95 : 0;
    setOpacity(b80, ease(t, b.l0.eighty - 0.05, b.l0.eighty + POP) * (t < M.m_val.t1 ? 1 : 0)); setOpacity(b78, ease(t, b.a0.seventy - 0.05, b.a0.seventy + POP) * (t < M.m_val.t1 ? 1 : 0));
    const k99 = CL.sched80_months_latest.value, k114 = CL.sched78_months_latest.value;
    const fl = t >= b.l1.ninety && t < b.l1.ninety + 0.8 ? 1 - lin(t, b.l1.ninety, b.l1.ninety + 0.8) : t >= b.a1.nine && t < b.a1.nine + 0.8 ? 1 - lin(t, b.a1.nine, b.a1.nine + 0.8) : 0;
    const kb = t < b.a1.nine ? k99 : k114; burst.position.set(XK(kb), 360000 * bal(kb) / UNIT, 0.6); burst.scale.setScalar(0.15 + 0.5 * (1 - fl)); burst.material.opacity = fl * cw;
    // S08.3–S09.1: căn nhà ngoài khung; chồng giá trị mọc dưới nhà ở "value", lớn tiếp khi "prices rise"
    const vg = easeOut(t, b.v0.value - 0.05, b.v0.value + 0.8), vr = ease(t, b.v0.value + 0.9, M.m_def.t0 + 0.3);
    const vh = vStackW.set({ usd: (400000 + 60000 * vr) * vg, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 }); setOpacity(vStackW, vg > 0.01 ? 1 : 0); vHouse.position.set(VX, vh, 0);
    // S09.2: giá trị lên → 80 % của giá trị dâng lên gặp chồng vay (sớm hơn lịch); vạch lịch (80 % giá gốc) mờ
    const rr = ease(t, b.v1.same, b.v1.eighty), vU = mix(400000, 450000, rr), lU = mix(360000, 358000, rr);
    dV.set({ usd: vU, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 }); dL.set({ usd: lU, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 });
    const dA = t >= M.m_def.t0 ? 1 : 0; setOpacity(dV, dA); setOpacity(dL, dA); d80.position.y = 0.8 * vU / UD; setOpacity(d80, dA); setOpacity(dSch, dA);
    d80.glow(t >= b.v1.sooner ? Math.max(0, 1 - lin(t, b.v1.sooner, b.v1.sooner + 0.8)) : 0);
    for (const it of ST.g.userData.items) setOpacity(it.it, 1);
    renderer.render(scene, cam);
    // ======================= lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, S2 = (x, y, z = 0.5) => O.toScreen(x, y, z); log.roi = {};
    const wl = (txt, x, y, z, a, px = 48) => { if (a > 0.01) { const [sx, sy] = O.toScreen(x, y, z); O.text(txt, sx, sy, px, { align: 'center', alpha: a, plate: PLATE, plateA: 0.6 }); } };
    // S04 (thế giới: tên, không số)
    const w4 = 1 - ease(t, M.m_e.t0, M.m_e.t0 + 0.3);
    wl('mortgage insurance (PMI)', HX, roofY + 1.05, -0.15, w4 * ease(t, b.p0.private - 0.05, b.p0.private + POP) * (1 - ease(t, M.m_push.t0, M.m_push.t0 + 0.3)));
    wl('lender', HX - 2.1, 1.65, 0.5, w4 * ease(t, b.p1.lender - 0.05, b.p1.lender + POP) * (1 - ease(t, M.m_push.t0, M.m_push.t0 + 0.3)));
    wl('borrower', HX + 1.6, 1.55, 0.6, w4 * ease(t, b.p1.borrower - 0.05, b.p1.borrower + POP));
    wl('cost: not shown in this video', HX + 3.2, 1.75, 0.3, w4 * ease(t, b.p2.dollar - 0.05, b.p2.dollar + POP), 44);
    { const [x0, y0] = O.toScreen(HX + 3.2, 1.25, 0.3), [, y1] = O.toScreen(HX + 3.2, 0, 0.3); log.roi['p1.lender'] = [x0 - 420, y0 - 40, x0 - 100, y1 + 10]; }
    { const [x0, y0] = O.toScreen(HX + 2.35, 0.5, 1.4); log.roi['p0.twenty'] = [x0 - 70, y0 - 40, x0 + 70, y0 + 30]; }
    // S05 (đồ thị giá)
    const e5 = ok * (1 - ease(t, M.m_pay.t0, M.m_pay.t0 + 0.3));
    if (e5 > 0.01) {
      const [hx, hy] = S2(0, 4.4); O.text(`$${Math.round(CL.ex_price.value).toLocaleString('en-US')} home`, hx, hy - 20, 56, { kind: 'number', align: 'center', alpha: e5 * ease(t, b.e0.four - 0.05, b.e0.four + POP), plate: PLATE, plateA: 0.7 });
      const [mx, my] = S2(-1.1, 410700 / UP), mA = e5 * ease(t, b.e0.median - 0.05, b.e0.median + POP);
      O.text('median new home sold', mx - 20, my - 4, 46, { kind: 'name', align: 'right', color: C.muted, alpha: mA }); O.text('Q2 2026: $410,700', mx - 20, my + 50, 46, { kind: 'number', align: 'right', color: C.muted, alpha: mA });
      const [dx, dy] = S2(-1.45 - 0.7, 0.2); O.text('$40,000 down', dx, dy, 52, { kind: 'number', align: 'right', color: C.ink, alpha: e5 * ease(t, b.e1.ten - 0.05, b.e1.ten + POP), plate: PLATE, plateA: 0.7 });
      const [lx, ly] = S2(0.75, 2.4); O.text('$360,000 loan', lx, ly + 40, 52, { kind: 'number', alpha: e5 * ease(t, b.e1.loan - 0.05, b.e1.loan + POP), plate: PLATE, plateA: 0.7 });
    }
    { const [x0, y0] = S2(-2.4, 0.5), [x1] = S2(-0.6, 0); log.roi['e1.ten'] = [x0, y0 - 60, x1, y0 + 50]; }
    // S06 (đồ thị khoản trả, N1)
    const y6 = ok * ease(t, M.m_pay.t1, M.m_pay.t1 + POP) * (1 - ease(t, M.m_law.t0, M.m_law.t0 + 0.3));
    const [cx, cy] = O.toScreen(CX, 1.5, 0.3);
    if (y6 > 0.01) {
      O.text(`September 2026 average rate: ${CL.rate_latest.value.toFixed(2)}%`, 960, 205, 52, { kind: 'number', align: 'center', color: C.muted, alpha: y6 * ease(t, b.y0.six - 0.05, b.y0.six + POP) * (1 - ease(t, b.y2.each - 0.4, b.y2.each)) });
      const pay = Math.round(CL.ex_payment_pi.value).toLocaleString('en-US'), chipA = y6 * ease(t, b.y0.figure - 0.05, b.y0.figure + POP) * (1 - ease(t, b.y2.each - 0.2, b.y2.each + 0.2));
      if (chipA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = chipA; c.strokeStyle = C.chrome; c.lineWidth = 3; c.beginPath(); c.moveTo(cx, cy - 6); c.lineTo(cx, 352); c.stroke(); c.restore();
        O.text(`$${pay}/month · principal + interest`, cx - 60, 336, 52, { kind: 'number', alpha: chipA, plate: PLATE, plateA: 0.8 });
        O.text('taxes, home insurance and PMI on top', cx - 60, 270, 48, { kind: 'name', color: C.warn, alpha: chipA * ease(t, b.y1.taxes - 0.05, b.y1.taxes + POP), plate: PLATE, plateA: 0.8 }); }
      O.text('loan balance schedule · set on day one', 960, 205, 52, { kind: 'compare', align: 'center', alpha: y6 * ease(t, b.y2.each, b.y2.each + POP) });
      const axA = y6 * ease(t, b.y2.each - 0.3, b.y2.each);
      for (const kk of [0, 120, 240, 360]) { const [x, y] = S2(XK(kk), 0, 0.4); O.text(kk === 360 ? '360 payments' : String(kk), x, y + 52, 44, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: axA }); }
      if (t >= b.y2.each) { const [x, y] = S2(CX + 0.75, 0.5, 0.3); O.text(`payment ${Math.round(k)}`, x + 14, y, 48, { kind: 'number', alpha: axA, plate: PLATE, plateA: 0.7 }); }
      const [lx, ly] = S2(XK(0), 2.0, 0.4); O.text('$360,000 loan', lx + 70, ly + 10, 48, { kind: 'number', alpha: y6 * (1 - ease(t, b.y2.each, b.y2.each + 0.4)) });
      { const [x, y] = S2(XK(70), 360000 * bal(70) / UNIT, 0.4); O.text('slowly at first', x, y + 74, 52, { align: 'center', alpha: y6 * ease(t, b.y2.slowly - 0.05, b.y2.slowly + POP) }); }
      { const [x, y] = S2(XK(300), 360000 * bal(300) / UNIT, 0.4); O.text('faster later', x - 40, y + 90, 52, { align: 'right', alpha: y6 * ease(t, b.y2.faster - 0.05, b.y2.faster + POP), plate: PLATE, plateA: 0.6 }); }
    }
    log.roi['y2.each'] = [cx - 120, cy - 10, cx + 120, O.toScreen(CX, 0, 0.3)[1] + 10];
    // S07–S08 (cùng đường, phóng vào 10 năm đầu)
    const z7 = ok * ease(t, M.m_law.t1, M.m_law.t1 + POP) * (1 - ease(t, M.m_wide.t0, M.m_wide.t0 + 0.3));
    if (z7 > 0.01) {
      const [x8, y8] = S2(XK(2), 320000 / UNIT, 0.4); O.text('80% of original value = $320,000', x8, y8 - 22, 50, { kind: 'compare', alpha: z7 * ease(t, b.l0.eighty - 0.05, b.l0.eighty + POP), plate: PLATE, plateA: 0.75 });
      const [x9, y9] = S2(XK(k99), 360000 * bal(k99) / UNIT, 0.5); O.text('payment 99: may request', x9 - 30, y9 - 50, 50, { kind: 'number', align: 'right', alpha: z7 * ease(t, b.l1.ninety - 0.05, b.l1.ninety + POP), plate: PLATE, plateA: 0.75 });
      O.text('conditions: written request · current on payments', 960, 300, 48, { kind: 'name', align: 'center', color: C.muted, alpha: z7 * ease(t, b.l2.conditions - 0.05, b.l2.conditions + POP) * (1 - ease(t, b.a0.seventy - 0.4, b.a0.seventy)) });
      const [x7, y7] = S2(XK(2), 312000 / UNIT, 0.4); O.text('78% = $312,000', x7, y7 + 62, 50, { kind: 'compare', alpha: z7 * ease(t, b.a0.seventy - 0.05, b.a0.seventy + POP), plate: PLATE, plateA: 0.75 });
      const [xa, ya] = S2(XK(k114), 360000 * bal(k114) / UNIT, 0.5); O.text('payment 114 (9.5 years): ends automatically', xa + 20, ya + 70, 48, { kind: 'number', align: 'right', alpha: z7 * ease(t, b.a1.nine - 0.05, b.a1.nine + POP), plate: PLATE, plateA: 0.75 });
      { const c = O.ctx; c.save(); c.globalAlpha = 0.9 * z7; c.fillStyle = C.ink; for (const kk of [k99, k114]) { if ((kk === k99 && t < b.l1.ninety) || (kk === k114 && t < b.a1.nine)) continue; const [x, y] = S2(XK(kk), 360000 * bal(kk) / UNIT, 0.5); c.beginPath(); c.arc(x, y, 10, 0, 7); c.fill(); } c.restore(); }
    }
    // S08.3 (khung rộng: đường cả 360 kỳ, hai mốc; căn nhà đứng ngoài khung đồ thị)
    const w8 = ok * ease(t, M.m_wide.t1, M.m_wide.t1 + POP) * (1 - ease(t, M.m_val.t0, M.m_val.t0 + 0.3));
    if (w8 > 0.01) {
      const [ax, ay] = S2(XK(0) - 0.4, 4.6, 0.3), [bx, by] = S2(XK(360) + 0.4, -1.0, 0.3), c = O.ctx;
      c.save(); c.globalAlpha = 0.55 * w8; c.strokeStyle = C.muted; c.lineWidth = 3; c.setLineDash([12, 10]); c.beginPath(); c.moveTo(ax, ay); c.lineTo(bx, ay); c.lineTo(bx, by); c.lineTo(ax, by); c.lineTo(ax, ay); c.stroke(); c.restore();
      O.text('based on the schedule only', (ax + bx) / 2, ay - 26, 52, { kind: 'name', align: 'center', alpha: w8 * ease(t, b.a2.schedule - 0.05, b.a2.schedule + POP), plate: PLATE, plateA: 0.7 });
      for (const kk of [k99, k114]) { const [x, y] = S2(XK(kk), 360000 * bal(kk) / UNIT, 0.5); c.save(); c.globalAlpha = w8; c.fillStyle = C.ink; c.beginPath(); c.arc(x, y, 8, 0, 7); c.fill(); c.restore();
        O.text(String(kk), kk === k99 ? x - 14 : x + 14, y - 26, 44, { kind: 'number', align: kk === k99 ? 'right' : 'left', alpha: w8 }); }
      for (const kk of [0, 120, 240, 360]) { const [x, y] = S2(XK(kk), 0, 0.4); O.text(kk === 360 ? '360 payments' : String(kk), x, y + 52, 44, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: w8 }); }
      const [hx, hy] = O.toScreen(VX, 1.6, 0); O.text('the house', hx, hy - 30, 48, { align: 'center', alpha: w8, plate: PLATE, plateA: 0.6 });
    }
    // S09.1 (thế giới): tên
    wl('home value', VX, vh + 1.75, 0, (1 - ease(t, M.m_def.t0, M.m_def.t0 + 0.3)) * ease(t, b.v0.value - 0.05, b.v0.value + POP), 52);
    { const [x0, y0] = O.toScreen(VX, 0.8, 0.4); log.roi['v0.value'] = [x0 - 110, y0 - 120, x0 + 110, y0 + 80]; }
    // S09.2–S09.4 (đồ thị: hai chồng)
    const d9 = ok * ease(t, M.m_def.t1, M.m_def.t1 + POP) * (1 - ease(t, M.m_mr.t0, M.m_mr.t0 + 0.3));
    if (d9 > 0.01) {
      const [vx, vy] = S2(DX - 0.8, 1.8), [lx, ly] = S2(DX + 3.0, lU / UD);
      O.text('home value', vx, vy, 52, { align: 'right', alpha: d9 });
      O.text('loan', lx, ly - 30, 52, { align: 'center', alpha: d9 });
      const pct = Math.max(80, Math.round(100 * lU / vU));
      O.text(`${pct}%`, lx + 130, ly + 16, 60, { kind: 'compare', alpha: d9 * (1 - ease(t, b.v1.sooner, b.v1.sooner + POP)), color: pct <= 80 ? C.ink : C.muted });
      const [sx, sy] = S2(DX + 1.5 + 2.8, 320000 / UD, 0.1); O.text('schedule: 80% of original price', sx + 16, sy + 50, 42, { kind: 'compare', color: C.muted, alpha: d9 });
      const [ex, ey] = S2(DX + 1.5 + 2.8, 0.8 * vU / UD, 0.15);
      O.text('80% sooner, on paper', ex + 16, ey - 18, 56, { kind: 'compare', alpha: d9 * ease(t, b.v1.sooner - 0.05, b.v1.sooner + POP), plate: PLATE, plateA: 0.75 });
      O.text('on paper: loan ÷ value by a price index', 960, 232, 52, { kind: 'compare', align: 'center', alpha: d9 * ease(t, b.v1.paper - 0.05, b.v1.paper + POP) });
      O.text("lender's rule: request · appraisal · minimum time", 960, 300, 48, { kind: 'name', align: 'center', color: C.warn, alpha: d9 * ease(t, b.v2.request - 0.05, b.v2.request + POP) });
      const [qx, qy] = S2(DX + 1.5, 2.2, 0.1); O.text('?', qx, qy, 96, { kind: 'name', alpha: d9 * ease(t, b.v3.fast - 0.05, b.v3.fast + POP) });
    }
    // lớp bắt buộc
    const ch = Math.max(e5, y6, z7, w8, d9);
    if (ch > 0.01) O.chrome({ illus: true, illusA: ch, src: e5 > 0.01 ? 'Price: Census/HUD via FRED' : y6 > 0.01 ? 'Rate: Freddie Mac via FRED' : d9 > 0.01 ? 'FHFA via FRED · CFPB · Fannie Mae B-8.1-04' : 'Law: 12 U.S.C. 4902',
      srcA: ch, cw: 'A measurement, not a next step', cwA: ch });
    const dark = 1 - ease(t, 0, 0.5);   // mở từ tối (ident đoạn A)
    if (dark > 0.002) { const c = O.ctx; c.save(); c.globalAlpha = dark; c.fillStyle = C.bg; c.fillRect(0, 0, 1920, 1080); c.restore(); }
    Object.assign(log, measure(cam, WORLD));
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
