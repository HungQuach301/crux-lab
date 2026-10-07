// Tập 5 · C4 · ĐOẠN C = S10–S14 (Hồi 2: phát lại). Mốc giờ chỉ từ spine.json; hằng số = hình học + độ dài hiệu ứng chung.
// Khu (trục x): phố SX (c4kit, khung đầu = khung cuối đoạn B) · tháng mua minh hoạ RX (N3, cũng là căn nhà + khiên của S12.1) · cột phát lại tập B
// quanh BC (N3 gập → N2) · cột tập A (24 tháng) quanh TC · (r2: bỏ khu nhiều nhà HD của S14.3; HD còn là điểm đi qua của cú bay) · ba người mua BX2 (c4kit, khung cuối = khung đầu đoạn D).
import * as THREE from 'three';
import { House, Stack, Beam, Studio, Fan, Burst, Shield, Ribbon, PALETTE, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, lin, ease, easeOut, mix } from '/toolkit/factory/world/core.js';
import { Calendar, Bars, foldPath } from '/episodes/ep005/world/obj5.js';
import { cues, moves, flyGuard, measure, followLight, Street, Buyers, SX, BX2, POP, PLATE, interp } from '/episodes/ep005/world/c4kit.js';

const SEG = '/episodes/ep005/world/c4/c-s10-s14/';
const UW = 2e5, RX = 60, BC = 75, TC = 92, HD = 108, HB = 0.025, HT = 5;
const XM = (k) => BC - 5 + 10 * k / 120, YL = (l) => (l - 0.75) * 11;          // đường phát lại (N3, trước khi gập)
const XB = (i, n) => BC - 5.5 + 11 * i / (n - 1), XT = (i, n) => TC - 5.5 + 11 * i / (n - 1);
const SLOW = C.accent, IXC = C.muted, BASE = '#C9CFD8', DIM = '#59606B';

export async function boot(res) {
  const [S, D, CL] = await Promise.all([loadJSON(SEG + 'spine.json'), loadJSON('/episodes/ep005/work/world-data/derived.json'), loadJSON('/episodes/ep005/world/claims.json')]);
  await fonts();
  const b = cues(S), M = moves(S);
  const at = (arr, k) => { const i = Math.min(arr.length - 2, Math.floor(k)), f = k - i; return arr[i] + (arr[i + 1] - arr[i]) * f; };
  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor, key } = Studio(scene, { shadowBox: 16 });
  const ST = Street(scene), BU = Buyers(scene, BX2);
  const P = D.bars, n = P.length, A = D.setA, nA = A.length;
  const tall = P.reduce((a, p, i) => (p.hit > P[a].hit ? i : a), 0);
  const poses = {
    ...ST.poses, ...BU.poses,
    wReplay: { pos: [RX + 1.6, 2.0, 8.4], tgt: [RX + 1.3, 1.5, 0], fov: 35, chart: 0 },
    fFold: { pos: [RX + 7.5, 1.9, 13], tgt: [BC - 3, 1.4, 0], fov: 35, chart: 0 },
    cBars: { pos: [BC, 0.9, 35.2], tgt: [BC, 0.9, 0], fov: 14, chart: 1 },
    cBarsT: { pos: [BC, 1.6, 35.2], tgt: [BC, 1.6, 0], fov: 15, chart: 1 },
    fBut: { pos: [RX + 7.0, 2.4, 13], tgt: [RX + 1.0, 2.2, 0], fov: 35, chart: 0 },
    wHouse: { pos: [RX + 2.0, 2.6, 8.0], tgt: [RX + 0.3, 2.2, 0], fov: 35, chart: 0 },
    fTally: { pos: [RX + 12, 2.2, 14], tgt: [TC - 8, 1.6, 0], fov: 35, chart: 0 },
    cTally: { pos: [TC, 1.2, 35], tgt: [TC, 1.2, 0], fov: 13, chart: 1 },
    fRow: { pos: [TC - 10, 2.0, 12], tgt: [BC + 2, 1.0, 0], fov: 35, chart: 0 },
    wRow: { pos: [BC - 9.0, 1.7, 6.2], tgt: [BC - 1.2, 0.9, 0], fov: 35, chart: 0 },
    fFive: { pos: [BC - 5.0, 1.6, 14], tgt: [BC - 0.5, 1.0, 0], fov: 35, chart: 0 },
    cZoom: { pos: [XB(tall, n), 1.5, 15], tgt: [XB(tall, n), 1.5, 0], fov: 20, chart: 1 },   // C4 r2: fov 16 → 20, hạ khung: chân cột nằm trên dải chữ cố định
    fBuy: { pos: [HD, 2.4, 15], tgt: [BX2 - 4, 1.4, 0], fov: 35, chart: 0 },   // C4 r2: cột cao nhất → ba người mua (bỏ khu nhiều nhà S14.3)
  };
  const CAM = Camera(poses, S.moves);
  // ---------- S10.1–S10.3 phố
  const items = ST.g.userData.items, nI = items.length;
  const winMats = items.map((it) => { const ms = []; it.it.traverse((o) => { if (o.isMesh && o.material.emissive && o.material.color.getHexString() === '2b2f38') ms.push(o.material); }); return ms; });
  const downs = items.map((it) => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.34, 0.12, 0.24), new THREE.MeshStandardMaterial({ color: C.cushion, transparent: true })); m.position.set(it.home.x - 0.2, 0.06, it.home.z + 0.55); scene.add(m); return m; });
  const ixLine = Ribbon({ color: C.accent, z: -2.4 }); scene.add(ixLine);
  const IXs = D.index.filter((x) => x.m <= P[n - 1].m), ixMin = Math.min(...IXs.map((x) => x.v)), ixMax = Math.max(...IXs.map((x) => x.v));
  const ixPts = IXs.map((x, i) => [SX - 8 + 16 * i / (IXs.length - 1), 1.3 + 1.1 * (x.v - ixMin) / (ixMax - ixMin)]);
  // ---------- S10.4 một tháng mua (N3) + khiên (S12.1)
  const G = D.buyers.grace;
  const value = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); value.position.set(RX, 0, 0); scene.add(value);
  const house = House({ w: 1.4 }); scene.add(house);
  const shield = Shield({ size: 0.75 }); scene.add(shield);
  const loan = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); loan.position.set(RX + 1.25, 0, 0.1); scene.add(loan);
  const bar80w = Beam({ length: 1.5 }); bar80w.position.set(RX + 1.25, 0, 0.1); scene.add(bar80w);
  const cal = Calendar({ w: 1.1, h: 1.35 }); cal.position.set(RX + 2.75, 0, 0.3); cal.rotation.y = -0.25; scene.add(cal);
  const burstW = Burst(); scene.add(burstW);
  // ---------- S10.5–S11, S13–S14 cột tập B (một mặt đất y = 0)
  const beamF = Beam({ length: 11.4 }); beamF.position.set(BC, YL(0.8), 0); scene.add(beamF);
  const fan = Fan(); scene.add(fan);
  const bars = Bars({ n, d: 0.45 }); scene.add(bars);
  const target = P.map((p, i) => ({ x: XB(i, n), y0: 0, h: p.hit * HB }));
  const lineCol = new THREE.Color(C.bg).lerp(new THREE.Color(C.ink), 0.45).getStyle();
  const med = Beam({ length: 11.4 }); med.position.set(BC, CL.medianB_months_to80.value * HB, 0.3); scene.add(med);
  const cut60 = Beam({ length: 11.4 }); cut60.position.set(BC, 60 * HB, 0.3); scene.add(cut60);
  const ridge = Ribbon({ color: C.muted, z: 0.35 }); scene.add(ridge);
  const ridgePts = P.map((p, i) => [XB(i, n), p.sched * HB]);
  const zs = Beam({ length: 0.5, color: C.muted }); zs.position.set(XB(tall, n), D.buyers.victor.sched * HB, 0.35); scene.add(zs);
  const slowIdx = P.map((p, i) => (p.hit > 60 ? i : -1)).filter((i) => i >= 0), s0 = slowIdx[0], s1 = slowIdx[slowIdx.length - 1];
  const pk = IXs.reduce((a, x, i) => (x.m < '2012-01-01' && x.v > IXs[a].v ? i : a), 0), tr = IXs.reduce((a, x, i) => (x.m > IXs[pk].m && x.m < '2015-01-01' && x.v < IXs[a].v ? i : a), pk + 1);
  // ---------- S12 cột tập A: chiều cao = nợ ÷ giá trị ở 24 tháng
  const tbars = Bars({ n: nA, w: 0.02, d: 0.4 }); scene.add(tbars);
  const T80 = Beam({ length: 11.4, color: C.ink }); T80.position.set(TC, (0.8 - 0.5) * HT, 0.3); scene.add(T80);
  const T75 = Beam({ length: 11.4, color: C.muted }); T75.position.set(TC, (0.75 - 0.5) * HT, 0.3); scene.add(T75);
  // ---------- S14.3: C4 r2 — không còn khu nhiều nhà; "national average, not one home" là tên trên khung cột cao nhất
  const WORLD = { street: ST.g, value, house, loan, cal, shield,
    ...Object.fromEntries(BU.items.flatMap((it, i) => [[`bHouse${i}`, it.house], [`bPerson${i}`, it.person]])) };

  function frame(t) {
    CAM.apply(t); const pose = flyGuard(CAM, S.moves, t), cw = CAM.poseAt(t).chart, cam = CAM.cam;
    followLight(key, pose.tgt);
    floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = mix(30, 150, cw); scene.fog.far = mix(80, 300, cw);
    // phố: cửa sổ sáng lần lượt (mỗi nhà một tháng mua), khối trả trước ở "same", đường chỉ số ở "value" → "index"
    items.forEach((it, i) => { const a = ease(t, mix(S.lit[0], S.lit[1], i / (nI - 1)) - 0.05, mix(S.lit[0], S.lit[1], i / (nI - 1)) + 0.25); for (const m of winMats[i]) m.emissiveIntensity = 0.9 * a; });
    downs.forEach((m, i) => { const a = ease(t, b.r1.same + 0.05 * i, b.r1.same + 0.05 * i + 0.25); m.material.opacity = a; m.visible = a > 0.01; });
    const nx = Math.max(2, Math.round(lin(t, b.r2.value, b.r2.index) * ixPts.length)); ixLine.set(ixPts.slice(0, nx), 0.06, C.accent); ixLine.material.opacity = t >= b.r2.value ? 1 : 0;
    // tháng mua minh hoạ (N3)
    const k = interp(S.month_kf, t), vUsd = 400000 * at(G.index, k), lUsd = 400000 * at(G.sched_line, k);
    const vh = value.set({ usd: vUsd, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 }); house.position.set(RX, vh, 0);
    const roofY = vh + house.userData.height * 0.86, wob = t >= b.k0.paper - 0.1 && t < b.k0.paper + 0.6 ? Math.sin((t - b.k0.paper) * 18) * 0.1 * (1 - lin(t, b.k0.paper, b.k0.paper + 0.6)) : 0;
    shield.position.set(RX, roofY, 0.25); shield.rotation.z = wob;
    loan.set({ usd: lUsd, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 });
    bar80w.position.y = 0.8 * vUsd / UW; const hitA = t >= b.r3.less ? 1 - lin(t, b.r3.less, b.r3.less + 1.2) : 0; bar80w.glow(hitA);
    setOpacity(bar80w, Math.max(ease(t, b.r3.eighty - 0.05, b.r3.eighty + POP), t >= b.r3.compare ? 0.6 : 0));
    cal.set({ flip: t >= b.r3.less || t < b.r3.every ? 0 : k % 1, pages: 1 - 0.5 * k / G.hit, glow: hitA });
    burstW.position.set(RX + 1.25, 0.8 * vUsd / UW, 0.6); burstW.scale.setScalar(0.4 + 1.6 * (1 - hitA)); burstW.material.opacity = hitA * (1 - cw);
    // cột tập B: đường (u = 0) → cột (u = 1); đuôi (S13) nhô lên và đổi màu trung tính
    const [F0, F1] = S.fold, u = lin(t, F0, F1), barA = lin(t, F1 - 0.15, F1 + 0.1), fanA = Math.min(1, ease(t, M.m_fold.t0, M.m_fold.t1) * 1.4) * (1 - barA);
    if (fanA > 0.01) { const lc = t >= F0 ? '#E3E7ED' : lineCol; fan.set(D.paths.map((p, i) => ({ color: lc, pts: foldPath(p.p.map((l, kk) => [XM(kk), YL(l)]), target[i], u) }))); fan.material.opacity = fanA; } else fan.material.opacity = 0;
    setOpacity(beamF, t >= M.m_fold.t0 && t < F1 + 0.3 ? 1 - lin(t, F1, F1 + 0.3) : 0);
    const hl = ease(t, b.r4.height - 0.05, b.r4.height + POP) * (1 - ease(t, b.t0.typical, b.t0.typical + 0.3));
    const half = ease(t, b.t1.half - 0.05, b.t1.half + POP) * (1 - ease(t, b.t2.ninety - 0.3, b.t2.ninety));
    const tl = t >= M.m_row.t0 ? easeOut(t, b.n0.tail - 0.05, b.n0.tail + 0.6) : 0, medH = CL.medianB_months_to80.value;
    bars.set(P.map((p, i) => { const slow = p.hit > 60 && tl > 0.02; let col = BASE;
      if (i === tall && hl > 0.5) col = C.ink;
      if (half > 0.5) col = p.hit <= medH ? C.ink : DIM;
      if (slow) col = SLOW;
      if (t >= M.m_zoom.t0) col = i === tall ? C.ink : DIM;
      return { x: target[i].x, y: 0, h: target[i].h, color: col }; }));
    setOpacity(bars, barA);
    setOpacity(med, ease(t, b.t0.twenty - 0.05, b.t0.twenty + POP) * (1 - ease(t, M.m_but.t0, M.m_but.t0 + 0.3)) + (t >= M.m_row.t0 ? ease(t, b.n0.typical - 0.05, b.n0.typical + POP) * (1 - ease(t, b.n0.tail, b.n0.tail + 0.4)) : 0));
    setOpacity(cut60, t >= M.m_bars.t0 && t < M.m_zoom.t0 ? ease(t, M.m_bars.t1 - 0.3, M.m_bars.t1) : 0); cut60.glow(t >= b.n1.years ? 1 - lin(t, b.n1.years, b.n1.years + 0.9) : 0);
    const rA = t < M.m_but.t1 ? ease(t, b.t2.ninety - 0.05, b.t2.ninety + 0.4) : 0;
    const rZ = t >= M.m_zoom.t0 && t < M.m_buy.t1 ? ease(t, b.z1.schedule - 0.05, b.z1.schedule + POP) : 0;   // C4 r2: ở khung phóng, sống lịch (mốc lịch CỦA TỪNG tháng) hiện lại ở "schedule"
    ridge.set(ridgePts, t >= M.m_zoom.t0 ? 0.03 : 0.045, C.muted); ridge.material.opacity = 0.9 * Math.max(rA, rZ);
    setOpacity(zs, rZ); zs.glow(t >= b.z1.schedule ? Math.max(0, 1 - lin(t, b.z1.schedule, b.z1.schedule + 0.8)) : 0, C.ink);
    // cột tập A (S12)
    const k80 = ease(t, b.k1.two - 0.05, b.k1.two + POP), k75 = ease(t, b.k2.fifteen - 0.05, b.k2.fifteen + POP);
    tbars.set(A.map((a, i) => ({ x: XT(i, nA), y: 0, h: Math.max(0.02, (a.l24 - 0.5) * HT), color: a.l24 <= 0.75 && k75 > 0.5 ? C.accent : a.l24 <= 0.8 && k80 > 0.5 ? C.ink : BASE })));
    setOpacity(tbars, t >= M.m_tally.t0 && t < M.m_row.t1 ? 1 : 0); setOpacity(T80, t >= M.m_tally.t0 && t < M.m_row.t1 ? 1 : 0); setOpacity(T75, t >= M.m_tally.t0 && t < M.m_row.t1 ? 1 : 0);
    T75.glow(t >= b.k2.seventy ? Math.max(0, 1 - lin(t, b.k2.seventy, b.k2.seventy + 0.8)) : 0, C.accent);
    renderer.render(scene, cam);
    // ======================= lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, S2 = (x, y, z = 0.3) => O.toScreen(x, y, z); log.roi = {};
    const wl = (txt, x, y, z, a, px = 48, col = C.ink) => { if (a > 0.01) { const [sx, sy] = O.toScreen(x, y, z); O.text(txt, sx, sy, px, { align: 'center', alpha: a, color: col, plate: PLATE, plateA: 0.6 }); } };
    // S10 thế giới (tên, không số)
    const wS = 1 - ease(t, M.m_push.t0, M.m_push.t0 + 0.3);
    wl('every purchase month', SX - 1.0, 2.2, -1.2, wS * ease(t, b.r0.every - 0.05, b.r0.every + POP) * (1 - ease(t, M.m_pan.t0, M.m_pan.t0 + 0.3)), 52);
    wl("same loan, that month's rate", SX + 5.0, 2.2, -1.2, wS * ease(t, b.r1.loan - 0.05, b.r1.loan + POP) * (1 - ease(t, b.r2.value - 0.3, b.r2.value)), 52);
    wl('national home price index', SX + 5.0, 2.75, -2.4, wS * ease(t, b.r2.index - 0.05, b.r2.index + POP), 52, C.accent);
    { const [x0, y0] = O.toScreen(SX - 8, 0.8, -1.2), [x1, y1] = O.toScreen(SX + 1, 0, -1.2); log.roi['r0.every'] = [x0, y0 - 40, x1, y1 + 20]; }
    const wR = 1 - ease(t, M.m_fold.t0, M.m_fold.t0 + 0.3);
    wl('home value', RX - 0.85, 0.9, 0.4, wR * ease(t, b.r3.value - 0.05, b.r3.value + POP), 48);
    wl('loan', RX + 1.25, lUsd / UW + 0.3, 0.1, wR * ease(t, b.r3.compare - 0.05, b.r3.compare + POP), 48);
    { const [x, y] = O.toScreen(RX + 1.25, 0.8 * vUsd / UW, 0.1); log.roi['r3.less'] = [x - 120, y - 60, x + 120, y + 60]; }
    // S10.5–S11 đồ thị cột (tập B)
    const c1 = ok * (t < M.m_but.t0 + 0.3 ? 1 - ease(t, M.m_but.t0, M.m_but.t0 + 0.3) : 0);
    const preA = c1 * (1 - ease(t, F0 - 0.3, F0)), postA = c1 * ease(t, F1 - 0.1, F1 + POP);
    if (c1 > 0.01) {
      O.text('Loan as % of home value · one line per purchase month, 1991–2016', 960, 180, 48, { kind: 'compare', align: 'center', alpha: preA });
      O.text('Months to 80% on paper · one bar per purchase month', 960, 180, 48, { kind: 'compare', align: 'center', alpha: postA });
      const yb = S2(BC, 0)[1], mA = c1 * ease(t, b.r4.month - 0.05, b.r4.month + POP);
      for (const yy of [1991, 1995, 2000, 2005, 2010, 2016]) { const i = P.findIndex((p) => p.m.startsWith(String(yy))); O.text(String(yy), S2(target[i].x, 0)[0], yb + 50, 44, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: mA }); }
      if (hl > 0) { const [x, y0] = S2(target[tall].x + 0.12, target[tall].h), [, y1] = S2(0, 0); O.bracket(x + 6, y0, y1, C.ink, c1 * hl, 16, 5);
        O.text('height = months to 80% on paper', x - 60, (y0 + y1) / 2 - 40, 52, { align: 'right', kind: 'compare', alpha: c1 * hl, plate: PLATE, plateA: 0.75 }); }
      const [mx, my] = S2(BC - 5.4, medH * HB); O.text('median: 23 months on paper', mx, my + 58, 48, { kind: 'compare', align: 'left', alpha: c1 * ease(t, b.t0.twenty - 0.05, b.t0.twenty + POP), plate: PLATE, plateA: 0.75 });
      O.text(`${(100 * CL.shareB_le_sched80.value).toFixed(1)}% no later than the schedule`, 960, 250, 52, { kind: 'compare', align: 'center', alpha: c1 * ease(t, b.t2.ninety - 0.05, b.t2.ninety + POP), plate: PLATE, plateA: 0.7 });
      const [rx, ry] = S2(BC - 5.4, P[0].sched * HB); O.text("schedule at each month's rate", rx, ry - 22, 46, { kind: 'compare', color: C.muted, alpha: c1 * ease(t, b.t2.schedule - 0.05, b.t2.schedule + POP) });
      const gA = c1 * ease(t, b.t3.gap - 0.05, b.t3.gap + POP);
      if (gA > 0) { const [gx, gy0] = S2(BC + 5.75, 95 * HB), [, gy1] = S2(0, medH * HB); O.bracket(gx, gy0, gy1, C.ink, gA, 18, 6); O.text('gap', gx + 34, (gy0 + gy1) / 2 + 16, 56, { alpha: gA, plate: PLATE, plateA: 0.7 }); }
    }
    { const [x0, y0] = S2(BC - 5.5, 3.0), [x1, y1] = S2(BC + 5.5, 0); log.roi['r4.bar'] = [x0, y0, x1, y1]; log.roi['t1.half'] = log.roi['r4.bar']; }
    // S12.1 thế giới
    wl('insurance still on', RX, roofY + 0.8, 0.2, (t >= M.m_but.t0 ? 1 : 0) * ease(t, b.k0.paper - 0.05, b.k0.paper + POP) * (1 - ease(t, M.m_tally.t0, M.m_tally.t0 + 0.3)), 56);
    // S12.2–S12.4 cột tập A
    const c2 = ok * ease(t, M.m_tally.t1, M.m_tally.t1 + POP) * (1 - ease(t, M.m_row.t0, M.m_row.t0 + 0.3));
    if (c2 > 0.01) {
      O.text(`at 24 months · ${CL.nA.value} purchase months, January 1991 to July 2024`, 960, 186, 46, { kind: 'compare', align: 'center', alpha: c2 * ease(t, b.k1.larger - 0.05, b.k1.larger + POP) });
      O.text(`at or under 80%: ${(100 * CL.shareA_ltv24_le80.value).toFixed(1)}%`, 120, 262, 54, { kind: 'compare', alpha: c2 * k80, plate: PLATE, plateA: 0.75 });
      O.text(`at or under 75%: ${(100 * CL.shareA_ltv24_le75.value).toFixed(1)}%`, 120, 330, 54, { kind: 'compare', color: C.accent, alpha: c2 * k75, plate: PLATE, plateA: 0.75 });
      O.text("Fannie Mae's early bar", 120, 392, 48, { kind: 'name', color: C.muted, alpha: c2 * ease(t, b.k2.fannie - 0.05, b.k2.fannie + POP) });
      const [x80, y80] = S2(TC + 5.6, 0.3 * HT), [x75, y75] = S2(TC + 5.6, 0.25 * HT);
      O.text('80%', x80 - 4, y80 - 12, 44, { kind: 'number', align: 'right', alpha: c2 }); O.text('75%', x75 - 4, y75 + 44, 44, { kind: 'number', align: 'right', color: C.muted, alpha: c2 });
      const yb = S2(TC, 0)[1]; for (const yy of [1991, 2000, 2010, 2024]) { const i = A.findIndex((a) => a.m.startsWith(String(yy))); O.text(String(yy), S2(XT(i, nA), 0)[0], yb + 50, 44, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: c2 }); }
      O.text('bar height = loan ÷ value on paper, 2 years after purchase', 960, 812, 44, { kind: 'compare', align: 'center', color: C.muted, alpha: c2 });
    }
    { const [x0, y0] = S2(TC - 5.5, 0.35 * HT), [x1, y1] = S2(TC + 5.5, 0); log.roi['k1.two'] = [x0, y0, x1, y1]; }
    // S13 (N2, vòng 3)
    const wRw = (t >= M.m_row.t0 ? 1 : 0) * (1 - ease(t, M.m_bars.t0, M.m_bars.t0 + 0.3));
    wl('typical', BC - 5.9, medH * HB + 0.15, 0.3, wRw * ease(t, b.n0.typical - 0.05, b.n0.typical + POP) * (1 - ease(t, b.n0.tail, b.n0.tail + 0.4)));
    wl('a long tail', XB(s0, n), 112 * HB + 0.35, 0, wRw * ease(t, b.n0.tail - 0.05, b.n0.tail + POP), 52);
    { const [x0, y0] = O.toScreen(XB(s0, n), 112 * HB, 0), [x1, y1] = O.toScreen(XB(s1, n), 0, 0); log.roi['n0.tail'] = [Math.min(x0, x1) - 30, y0 - 30, Math.max(x0, x1) + 30, y1 + 10]; }
    const c3 = ok * (t >= M.m_bars.t0 ? 1 : 0) * (1 - ease(t, M.m_zoom.t0, M.m_zoom.t0 + 0.3));
    const D0 = S.index_draw[0], D1 = S.index_draw[1], sl = ease(t, b.n2.slump - 0.05, b.n2.slump + POP);
    const yb = S2(BC, 0)[1], ys0 = yb + 16, ys1 = ys0 + 90, YS = (v) => ys1 - 90 * (v - ixMin) / (ixMax - ixMin), XS = (i) => S2(XB(i, n), 0)[0];
    log.roi['n2.together'] = [XS(s0) - 20, S2(0, 3.2)[1] - 30, XS(s1) + 20, S2(0, 2.6)[1] + 30];
    if (c3 > 0.01) {
      O.text('one bar per purchase month', 960, 172, 52, { kind: 'compare', align: 'center', alpha: c3 });
      const gA = c3 * ease(t, b.n2.together - 0.05, b.n2.together + POP), [x0s, y0s] = S2(XB(s0, n), 112 * HB + 0.12);
      if (gA > 0) { const c = O.ctx; c.save(); c.globalAlpha = 0.12 * gA; c.fillStyle = SLOW; c.fillRect(x0s - 6, y0s, XS(s1) - x0s + 12, ys1 + 8 - y0s); c.restore();
        c.save(); c.globalAlpha = gA; c.strokeStyle = SLOW; c.lineWidth = 5; c.beginPath(); c.moveTo(x0s, y0s + 14); c.lineTo(x0s, y0s); c.lineTo(XS(s1), y0s); c.lineTo(XS(s1), y0s + 14); c.stroke(); c.restore();
        O.text('one stretch of purchase months', (x0s + XS(s1)) / 2, y0s - 26, 50, { align: 'center', alpha: c3 * ease(t, b.n2.stretch - 0.05, b.n2.stretch + POP), plate: PLATE, plateA: 0.7 }); }
      const kk = Math.round(lin(t, D0, D1) * (IXs.length - 1));
      if (t >= D0) { const c = O.ctx; c.save(); c.globalAlpha = 0.9 * c3; c.strokeStyle = IXC; c.lineWidth = 4; c.lineJoin = 'round'; c.beginPath();
        for (let i = 0; i <= kk; i++) { const x = XS(Math.min(i, n - 1)), y = YS(IXs[i].v); i ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke();
        if (sl > 0) { c.globalAlpha = sl * c3; c.strokeStyle = C.ink; c.lineWidth = 9; c.beginPath(); for (let i = pk; i <= tr; i++) { const x = XS(i), y = YS(IXs[i].v); i > pk ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke(); }
        c.restore(); }
      for (const yy of [1991, 1995, 2000, 2005, 2010, 2016]) { const i = P.findIndex((p) => p.m.startsWith(String(yy))); O.text(String(yy), XS(i), ys1 + 46, 48, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: c3 }); }
      { const [x, y] = S2(BC - 5.5, 60 * HB); O.text('60 months', x, y - 16, 46, { kind: 'number', color: C.muted, alpha: c3 }); }
      { const [x, y] = S2(BC - 5.5, 60 * HB + 1.1), pa = c3 * ease(t, b.n1.years - 0.05, b.n1.years + POP); O.text('more than 60 months:', x, y, 52, { kind: 'compare', alpha: pa, plate: PLATE, plateA: 0.75 });
        O.text(`${(100 * CL.shareB_over60.value).toFixed(1)}% (about 1 in 7)`, x, y + 66, 52, { kind: 'compare', alpha: pa, plate: PLATE, plateA: 0.75 }); }
      { const [xr] = S2(XB(s1, n), 0), xR = xr + 26, yT = S2(0, CL.maxB_months_to80.value * HB)[1], c = O.ctx;
        c.save(); c.globalAlpha = 0.85 * c3; c.strokeStyle = C.ink; c.lineWidth = 3; c.beginPath(); c.moveTo(xR - 10, yT); c.lineTo(xR + 10, yT); c.moveTo(xR, yT); c.lineTo(xR, yb); c.moveTo(xR - 10, yb); c.lineTo(xR + 10, yb); c.stroke(); c.restore();
        O.text("each bar's height:", xR + 20, yT + 34, 48, { alpha: c3, plate: PLATE, plateA: 0.75 }); O.text('months to 80% on paper', xR + 20, yT + 96, 48, { alpha: c3, plate: PLATE, plateA: 0.75 }); }
      O.text('national home price index', XS(0), ys1 + 116, 48, { color: IXC, alpha: c3 * ease(t, b.n2.national - 0.05, b.n2.national + POP) });
      O.text('national price slump', XS(Math.round((pk + tr) / 2)), ys1 + 116, 52, { align: 'center', alpha: c3 * sl, plate: PLATE, plateA: 0.75 });
    }
    // S14.1–S14.4 phóng vào cột cao nhất — C4 r2: khung GIỮ tới hết S14 (không sang khu nhiều nhà); thước chiều cao = tháng tới 80 % trên giấy;
    // mốc lịch của chính tháng đó (90 kỳ) cắt ngang cột + sống lịch của mọi tháng; "national average, not one home" thành tên trên khung đồ thị
    const c4 = ok * ease(t, M.m_zoom.t1, M.m_zoom.t1 + POP) * (1 - ease(t, M.m_buy.t0, M.m_buy.t0 + 0.3));
    if (c4 > 0.01) {
      const [x, y] = S2(XB(tall, n), CL.maxB_months_to80.value * HB), [, yb0] = S2(0, 0);
      O.text('October 2005: 112 months (9 yr 4 mo)', x, y - 92, 54, { kind: 'compare', align: 'center', alpha: c4 * ease(t, b.z0.october - 0.05, b.z0.october + POP), plate: PLATE, plateA: 0.75 });
      const hA = c4 * ease(t, b.z0.months - 0.05, b.z0.months + POP);
      if (hA > 0.01) { O.bracket(x + 22, y, yb0, C.ink, hA, 16, 5); O.text('height = months to 80% on paper', x + 52, (y + yb0) / 2 + 16, 52, { kind: 'compare', alpha: hA, plate: PLATE, plateA: 0.75 }); }
      const [sx, sy] = S2(XB(tall, n) - 0.3, D.buyers.victor.sched * HB), sA = c4 * ease(t, b.z1.schedule - 0.05, b.z1.schedule + POP);
      if (sA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = sA; c.strokeStyle = C.muted; c.lineWidth = 3; c.setLineDash([8, 6]); c.beginPath(); c.moveTo(120, sy); c.lineTo(x - 8, sy); c.stroke(); c.restore();
        O.text('schedule at that rate: 90 payments', 120, sy - 26, 50, { kind: 'compare', color: C.muted, alpha: sA, plate: PLATE, plateA: 0.75 }); }
      O.text('national average, not one home', 960, 880, 52, { align: 'center', alpha: c4 * ease(t, b.z2.single - 0.05, b.z2.single + POP), plate: PLATE, plateA: 0.75 });
    }
    // lớp bắt buộc
    const hist = Math.max(c1 * ease(t, M.m_fold.t1, M.m_fold.t1 + POP), c2, c3, c4);
    const illus = Math.max(wR * (t >= b.r3.every - 0.05 ? 1 : 0), c4 * ease(t, b.z1.schedule - 0.05, b.z1.schedule + POP), (t >= M.m_buy.t1 ? 1 : 0));
    if (hist > 0.01 || illus > 0.01) O.chrome({ illus: illus > 0.01, illusA: illus, src: hist > 0.01 ? (c2 > 0.01 ? 'FHFA · Freddie Mac via FRED · Fannie Mae B-8.1-04' : 'Source: FHFA · Freddie Mac via FRED') : null, srcA: hist,
      hist: hist > 0.01, histA: hist, cw: hist > 0.01 ? 'Past buyers, measured · not a reason to buy, rent or wait' : null, cwA: hist });
    Object.assign(log, measure(cam, WORLD));
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
