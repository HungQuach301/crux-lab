// Tập 5 · C4 · ĐOẠN D = S15–S20 (Hồi 3 · phương pháp · kết). Mốc giờ chỉ từ spine.json; hằng số = hình học + độ dài hiệu ứng chung.
// Khu (trục x): ba người mua BX2 (c4kit; khung đầu = khung cuối đoạn C) · ba làn L1–L3 · nhà Victor VX · ba làn cùng gốc XA (S18, S20.2) ·
// hai lối FX (nhà + khiên, căn hộ, người; S18.6, S20) · hai chồng giá XD (S18.5). Thẻ V7 (S19): lớp phủ 2D trên khung đồ thị chính diện của hai lối.
import * as THREE from 'three';
import { House, Stack, Beam, Person, Ribbon, Studio, Fan, Burst, Shield, Apartment, PALETTE, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, lin, ease, easeOut, mix } from '/toolkit/factory/world/core.js';
import { cues, moves, flyGuard, measure, followLight, Buyers, BX2, BCOL, POP, PLATE } from '/episodes/ep005/world/c4kit.js';

const SEG = '/episodes/ep005/world/c4/d-s15-s20/';
const L = [140, 154, 168], VX = 175.5, XA = 184, FX = 198, XD = 212, UP = 1e5;
const XL = (c, k) => c - 5 + 10 * k / 120, YR = (l) => 0.8 + (l - 0.8) * 5, YI = (v) => -0.2 + (v - 1) * 4.0;   // C4 r2: chỉ số ×2 (2,0 → 4,0), gốc −0,3 → −0,2 (trục năm không chạm dải chữ cố định, F-2) — −3,3 % của Victor ở tháng 112 thấy được (vòng 1: "dips and recovers")
const ORDER = ['grace', 'owen', 'victor'];

export async function boot(res) {
  const [S, D, CL] = await Promise.all([loadJSON(SEG + 'spine.json'), loadJSON('/episodes/ep005/work/world-data/derived.json'), loadJSON('/episodes/ep005/world/claims.json')]);
  await fonts();
  const b = cues(S), M = moves(S);
  const sf = (rate, k) => { const r = rate / 1200, a = Math.pow(1 + r, 360); return 0.9 * (a - Math.pow(1 + r, k)) / (a - 1); };
  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor, key } = Studio(scene, { shadowBox: 16 });
  const BU = Buyers(scene, BX2);
  const lane = (c) => ({ pos: [c, 0.7, 30], tgt: [c, 0.7, 0], fov: 14, chart: 1 });
  const poses = {
    ...BU.poses, cLane1: lane(L[0]), cLane2: lane(L[1]), cLane3: lane(L[2]),
    fLane: { pos: [BX2 + 9, 1.8, 13], tgt: [L[0] - 6, 1.0, 0], fov: 35, chart: 0 },
    fVic: { pos: [L[2] + 3, 1.6, 12], tgt: [VX + 1, 1.2, 0], fov: 35, chart: 0 },
    wVictor: { pos: [VX + 1.6, 2.0, 7.5], tgt: [VX, 1.6, 0], fov: 35, chart: 0 },
    fAll: { pos: [VX + 5, 1.8, 11], tgt: [XA - 1, 1.0, 0], fov: 35, chart: 0 },
    cAll: { pos: [XA, 0.7, 30], tgt: [XA, 0.7, 0], fov: 14, chart: 1 },
    cBench: { pos: [XA + 0.4, 0.8, 30], tgt: [XA + 0.4, 0.8, 0], fov: 16, chart: 1 },
    cAll2: { pos: [XA, 0.7, 30], tgt: [XA, 0.7, 0], fov: 15, chart: 1 },
    cDown: { pos: [XD, 2.3, 30], tgt: [XD, 2.3, 0], fov: 12, chart: 1 },
    fFork: { pos: [XD - 6, 1.8, 13], tgt: [FX + 1, 1.2, 0], fov: 35, chart: 0 },
    wFork: { pos: [FX + 0.8, 1.9, 10.5], tgt: [FX + 0.8, 1.2, 0], fov: 35, chart: 0 },
    fCard: { pos: [FX + 0.8, 2.2, 22], tgt: [FX + 0.8, 1.3, 0], fov: 30, chart: 0 },
    cCard: { pos: [FX + 0.8, 1.5, 40], tgt: [FX + 0.8, 1.5, 0], fov: 12, chart: 1 },
    fBack: { pos: [FX + 0.8, 1.9, 20], tgt: [FX + 0.8, 1.2, 0], fov: 30, chart: 0 },
    fAns: { pos: [FX - 5, 1.8, 13], tgt: [XA + 2, 0.9, 0], fov: 35, chart: 0 },
    fEnd: { pos: [XA + 7, 1.8, 13], tgt: [FX - 1, 1.2, 0], fov: 35, chart: 0 },
    wHouse: { pos: [FX + 0.6, 2.0, 10.6], tgt: [FX + 0.6, 1.35, 0], fov: 35, chart: 0 },   // C4 r3 (đạo diễn A+B 7:34–7:42): khung kết TRỌN bộ ba (nhà + khiên, người, căn hộ), giữ rồi tối dần
  };
  const CAM = Camera(poses, S.moves);
  // ---------- ba làn (mỗi làn: lịch muted, trên giấy ink, chỉ số accent, vạch 80 %)
  const lanes = ORDER.map((key_, i) => { const c = L[i], B_ = D.buyers[key_]; const o = { c, B: B_, key: key_,
    paper: Ribbon({ color: C.ink, z: 0.5 }), sched: Ribbon({ color: C.muted, z: 0.45 }), idx: Ribbon({ color: C.accent, z: 0.4 }), beam: Beam({ length: 10.4, color: C.muted }) };
    o.beam.position.set(c, YR(0.8), 0.2); scene.add(o.paper, o.sched, o.idx, o.beam); return o; });
  const burst = Burst(); scene.add(burst);
  const vHouse = House({ w: 1.4 }); vHouse.position.set(VX, 0, 0); scene.add(vHouse);
  const vShield = Shield({ size: 0.75 }); vShield.position.set(VX, vHouse.userData.height * 0.86, 0.25); scene.add(vShield);
  // C4 r2: bỏ người cạnh nhà Victor (vòng 1: nhà + người sau mười năm → "buy only if I can hold a decade"); nhà + khiên + "?" (dữ liệu không trả lời)
  // ---------- ba làn cùng gốc + bó trên giấy + dải lịch
  const allPaper = ORDER.map(() => Ribbon({ color: C.ink, z: 0.55 })), allSched = ORDER.map(() => Ribbon({ color: C.muted, z: 0.45 }));
  allPaper.forEach((r) => scene.add(r)); allSched.forEach((r) => scene.add(r));
  const fan = Fan(); scene.add(fan);
  const fanLines = D.paths.map((p) => ({ color: new THREE.Color(C.bg).lerp(new THREE.Color(C.ink), 0.2).getStyle(), pts: p.p.map((l, k) => [XL(XA, k), YR(l)]) }));
  fan.set(fanLines, 0.3);
  const A80 = Beam({ length: 10.4, color: C.muted }); A80.position.set(XA, YR(0.8), 0.2); scene.add(A80);
  const A75 = Beam({ length: 10.4, color: C.muted }); A75.position.set(XA, YR(0.75), 0.2); scene.add(A75);
  const plan = Beam({ length: 2.3, color: C.ink }); plan.rotation.z = Math.PI / 2; plan.position.set(XL(XA, 24), 1.05, 0.6); plan.scale.y = 2.2; scene.add(plan);   // C4 r2: dày ×2,2, cao hơn bó
  // ---------- hai chồng giá (S18.5)
  const price = Stack({ unitUsd: UP, w: 1.1, d: 0.7 }); price.position.set(XD - 0.8, 0, 0); scene.add(price);
  const pHouse = House({ w: 1.2 }); pHouse.position.set(XD + 1.4, 0, 0); scene.add(pHouse);
  // ---------- hai lối (S18.6, S20)
  const fHouse = House({ w: 1.5 }); fHouse.position.set(FX - 1.2, 0, 0); scene.add(fHouse);
  const fShield = Shield({ size: 0.8 }); fShield.position.set(FX - 1.2, fHouse.userData.height * 0.86, 0.25); scene.add(fShield);
  const apt = Apartment({ w: 1.5 }); apt.position.set(FX + 2.8, 0, -0.4); scene.add(apt);
  const you = Person({ h: 1.15, color: PALETTE.person2 }); you.position.set(FX + 0.8, 0, 0.8); scene.add(you);
  const WORLD = { vHouse, vShield, fHouse, fShield, apt, you, pHouse, ...Object.fromEntries(BU.items.flatMap((it, i) => [[`bHouse${i}`, it.house], [`bPerson${i}`, it.person]])) };
  const prog = (t, a, b_) => lin(t, a, b_);
  const lineTo = (arr, kmax, c, f) => { const pts = []; const K_ = Math.min(arr.length - 1, Math.floor(kmax)); for (let k = 0; k <= K_; k++) pts.push([XL(c, k), f(arr[k])]); if (pts.length < 2) pts.push([XL(c, 0.01), f(arr[0])]); return pts; };
  const schedArr = (B_, n) => { const a = []; for (let k = 0; k <= n; k++) a.push(sf(B_.rate, k)); return a; };
  const SCH = ORDER.map((k) => schedArr(D.buyers[k], 120));

  function frame(t) {
    CAM.apply(t); const pose = flyGuard(CAM, S.moves, t), cw = CAM.poseAt(t).chart, cam = CAM.cam;
    followLight(key, pose.tgt);
    floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = mix(30, 150, cw); scene.fog.far = mix(80, 300, cw);
    // làn: độ tiến theo lời
    const kG = 23 * prog(t, b.g1.four, b.g2.middle) + 6 * prog(t, b.g2.middle, b.g3.schedule), kGs = Math.max(kG, 71 * prog(t, b.g3.schedule, b.g3.longer));
    const kO = 13 * prog(t, b.o0.owen, b.o1.thirteen) + 6 * prog(t, b.o1.thirteen, b.o2.rising), kOs = Math.max(kO, 86 * prog(t, b.o2.rising, b.o2.payments));
    const kV = 14 * prog(t, b.v0.victor, b.v1.prices) + 98 * prog(t, b.v1.prices, b.v1.eighty), kVs = Math.max(Math.min(kV, 112), 0);   // C4 r3: vẽ từ "Victor" (vòng 2: 7 s đồ thị trống); 14 tháng đầu (giá "rose a little") tới "Prices", rồi tới tháng 112 ở "eighty"; dừng ở tháng 112
    const K = { grace: [kG, kGs], owen: [kO, kOs], victor: [kV, kVs] };
    lanes.forEach((o, i) => { const [kp, ks] = K[o.key], vis = t < M.m_vw.t1 ? 1 : 0;
      o.paper.set(lineTo(o.B.paper, kp, o.c, YR), 0.07, C.ink); o.paper.material.opacity = kp > 0.05 ? vis : 0;
      o.sched.set(lineTo(SCH[i], ks, o.c, YR), 0.05, C.muted); o.sched.material.opacity = ks > 0.05 ? vis : 0;
      o.idx.set(lineTo(o.B.index, o.key === 'victor' ? Math.min(kp, o.B.hit) : kp, o.c, YI), 0.05, C.accent); o.idx.material.opacity = kp > 0.05 ? vis : 0; setOpacity(o.beam, vis); });   // C4 r2: chỉ số của Victor dừng ở tháng 112 (tháng tới 80 % trên giấy) — vẽ tiếp 6 tháng làm cuối đường lên trên mức mua
    burst.material.opacity = 0;   // C4 r3: bỏ chớp ở mốc lịch 90 (không "phần thưởng"); hai mốc là hai VẬT khác nhau ở lớp phủ
    // cùng gốc
    const inAll = (t >= M.m_all.t0 && t < M.m_fork.t1) || t >= M.m_ans.t0 ? 1 : 0, aIn = inAll * ease(t, t >= M.m_ans.t0 ? M.m_ans.t0 : M.m_all.t0, (t >= M.m_ans.t0 ? M.m_ans.t1 : M.m_all.t1));
    ORDER.forEach((k, i) => { const B_ = D.buyers[k]; allPaper[i].set(lineTo(B_.paper, B_.paper.length - 1, XA, YR), 0.07, C.ink); allPaper[i].material.opacity = aIn;   // khoá nghĩa (sau vòng 3): khung tổng kết S18 về bản r2 (đường ink), xem FIX-R3.md
      allSched[i].set(lineTo(SCH[i], 120, XA, YR), 0.045, C.muted); allSched[i].material.opacity = aIn * 0.9; });
    fan.material.opacity = aIn * ease(t, t >= M.m_ans.t0 ? M.m_ans.t1 : b.a1.benchmarks - 0.05, (t >= M.m_ans.t0 ? M.m_ans.t1 : b.a1.benchmarks) + 0.4);   // khoá nghĩa: độ đậm bó nền như r2
    setOpacity(A80, aIn); setOpacity(A75, aIn);
    setOpacity(plan, inAll * (t < M.m_ans.t0 ? 1 : 0) * ease(t, b.a1.plan - 0.05, b.a1.plan + POP)); plan.glow(t >= b.a1.plan ? Math.max(0, 1 - lin(t, b.a1.plan, b.a1.plan + 0.8)) : 0, C.ink);   // C4 r2: vạch "a plan" đứng từ "plan" (S18.2), không đợi "two"
    // S18.5: đáy 10 % → 20 %
    price.set({ usd: 400000, tintBelowUsd: 40000 + 40000 * easeOut(t, b.a4.twenty - 0.05, b.a4.twenty + 0.6), tint: C.cushion, tintA: 1 });
    renderer.render(scene, cam);
    // ======================= lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, S2 = (x, y, z = 0.5) => O.toScreen(x, y, z); log.roi = {};
    const wl = (txt, x, y, z, a, px = 52) => { if (a > 0.01) { const [sx, sy] = O.toScreen(x, y, z); O.text(txt, sx, sy, px, { align: 'center', alpha: a, plate: PLATE, plateA: 0.6 }); } };
    const T = (txt, x, y, px, a, o = {}) => { if (a > 0.01) O.text(txt, x, y, px, { kind: 'compare', alpha: a, plate: PLATE, plateA: 0.7, ...o }); };
    // làn
    const laneA = (i, m0, m1) => ok * ease(t, m0, m0 + POP) * (m1 ? 1 - ease(t, m1, m1 + 0.3) : 1);
    const lA = [laneA(0, M.m_g.t1, M.m_o.t0), laneA(1, M.m_o.t1, M.m_v.t0), laneA(2, M.m_v.t1, M.m_vw.t0)];
    const ax = (c, a, r2 = false) => { if (a < 0.01) return; for (const yr of [0, 2, 4, 6, 8, 10]) { const [x, y] = S2(XL(c, yr * 12), YI(0.8) - 0.15); O.text(yr === 10 ? '10 years' : String(yr), x, y + 40, 42, { kind: 'number', role: 'axis-label', color: C.muted, align: 'center', w: 600, alpha: a }); }
      if (r2) { const [x8, y8] = S2(c - 4.9, YR(0.8)); O.text('80%', x8, y8 - 16, 44, { kind: 'number', alpha: a, plate: PLATE, plateA: 0.8 }); return; }   // khoá nghĩa: khung tổng kết S18 giữ nhãn 80 % của r2; C5b V08 (3,4:1 trên bó sáng): thêm nền
      const [x8, y8] = S2(c + 5.3, YR(0.8)); O.text('80%', x8, y8 + 14, 48, { kind: 'number', alpha: a, plate: PLATE, plateA: 0.75 }); };   // C4 r3: đầu PHẢI vạch (bên trái các đường xuất phát cắt chữ)
    ax(L[0], lA[0]); ax(L[1], lA[1]); ax(L[2], lA[2]);
    const legend = (a, n = 3, X0 = 1380, Y0 = 214, tri = false) => { if (a < 0.01) return; const c = O.ctx;   // légende cố định góc trên phải (tên đường, không số); tri: mẫu "on paper" ba màu người mua (r3)
      [['on paper', C.ink], ['schedule', C.muted], ['price index', C.accent]].slice(0, n).forEach(([nm, col], i) => { const y = Y0 + i * 54;
        c.save(); c.globalAlpha = a; c.lineWidth = 6;
        if (tri && i === 0) BCOL.forEach((bc, j) => { c.strokeStyle = bc; c.beginPath(); c.moveTo(X0 + 21 * j, y - 14); c.lineTo(X0 + 21 * j + 17, y - 14); c.stroke(); });
        else { c.strokeStyle = col; c.beginPath(); c.moveTo(X0, y - 14); c.lineTo(X0 + 60, y - 14); c.stroke(); } c.restore();
        O.text(nm, X0 + 76, y, 42, { color: col, alpha: a }); }); };
    legend(Math.max(...lA));
    const BC_ = (k, ...f) => f.map((x) => `buyer_${k}_${x}`);   // C5b (S07/S08): số của làn khớp claim của CHÍNH người mua đó (minh hoạ), không claim tập B trùng giá trị
    T('Grace · June 2014 · 4.16%', 120, 210, 54, lA[0] * ease(t, b.g1.four - 0.05, b.g1.four + POP), { color: BCOL[0], claims: BC_('grace', 'purchaseMonth', 'rate') });   // C4 r3: màu riêng của từng người mua
    wl('Grace', BX2 - 3.0 + 1.05, 1.55, 0.55, (t < M.m_g.t0 + 0.3 ? 1 - ease(t, M.m_g.t0, M.m_g.t0 + 0.3) : 0) * ease(t, b.g1.grace - 0.05, b.g1.grace + POP), 48);
    T('on paper: 23 months', 120, 290, 50, lA[0] * ease(t, b.g2.middle - 0.05, b.g2.middle + POP), { claims: BC_('grace', 'monthsTo80Index') });
    T('schedule: 71', 120, 360, 50, lA[0] * ease(t, b.g3.schedule - 0.05, b.g3.schedule + POP), { color: C.muted, claims: BC_('grace', 'sched80Months') });
    T('Owen · January 2004 · 5.71%', 120, 210, 54, lA[1] * ease(t, b.o0.owen - 0.05, b.o0.owen + POP), { color: BCOL[1], claims: BC_('owen', 'purchaseMonth', 'rate') });
    T('on paper: 13 months · schedule: 86', 120, 290, 50, lA[1] * ease(t, b.o1.thirteen - 0.05, b.o1.thirteen + POP), { claims: BC_('owen', 'monthsTo80Index', 'sched80Months') });
    T('index +11.2%', 120, 360, 50, lA[1] * ease(t, b.o2.rising - 0.05, b.o2.rising + POP), { color: C.accent, claims: BC_('owen', 'hpiChangeTo80Pct') });
    T('Victor · October 2005 · 6.07%', 120, 210, 54, lA[2] * ease(t, b.v0.victor - 0.05, b.v0.victor + POP), { color: BCOL[2], claims: BC_('victor', 'purchaseMonth', 'rate') });
    T('index still 3.3% below purchase', 120, 290, 50, lA[2] * ease(t, b.v1.below - 0.05, b.v1.below + POP), { color: C.accent, claims: BC_('victor', 'hpiChangeTo80Pct') });
    // C4 r3 (B17 vòng 2: "112 tháng trên giấy" đọc thành lịch): HAI LẦN CHẠM 80 % LÀ HAI VẬT KHÁC NHAU, khoảng cách giữa chúng thấy được
    //  · lịch (muted, mảnh): Ô VUÔNG RỖNG ở tháng 90 trên vạch 80 % + nhãn ngay dưới — hiện ở "schedule" (S17.3), trước "ninety";
    //  · trên giấy (ink, dày): CHẤM ĐẶC ở tháng 112 + nhãn TRÊN đường (lịch ở DƯỚI vạch, trên giấy ở TRÊN vạch) — hiện ở "eighty" (S17.2);
    //  · dải mờ trên vạch 80 % nối hai mốc (khoảng cách 90 → 112), không chữ, không chớp (không "phần thưởng" ở cuối).
    { const c = O.ctx, [x90, y8] = S2(XL(L[2], 90), YR(0.8)), [x112] = S2(XL(L[2], 112), YR(0.8));
      const pA = lA[2] * ease(t, b.v1.eighty - 0.05, b.v1.eighty + POP), sA = lA[2] * ease(t, b.v2.schedule - 0.05, b.v2.schedule + POP);
      if (pA * sA > 0.01) { c.save(); c.globalAlpha = 0.5 * pA * sA; c.fillStyle = C.ink; c.fillRect(x90, y8 - 8, x112 - x90, 16); c.restore(); }
      if (sA > 0.01) { c.save(); c.globalAlpha = sA; c.fillStyle = C.bg; c.fillRect(x90 - 15, y8 - 15, 30, 30); c.strokeStyle = C.muted; c.lineWidth = 5; c.strokeRect(x90 - 15, y8 - 15, 30, 30);
        c.lineWidth = 3; c.beginPath(); c.moveTo(x90, y8 + 16); c.lineTo(x90, y8 + 34); c.stroke(); c.restore();
        T('schedule: 90 payments', x90, y8 + 76, 50, sA, { align: 'center', color: C.muted, claims: BC_('victor', 'sched80Months') }); }
      if (pA > 0.01) { c.save(); c.globalAlpha = pA; c.fillStyle = C.ink; c.beginPath(); c.arc(x112, y8, 14, 0, 7); c.fill(); c.strokeStyle = C.ink; c.lineWidth = 3; c.beginPath(); c.moveTo(x112, y8 - 16); c.lineTo(x112, y8 - 88); c.stroke(); c.restore();
        T('on paper: 112 months', Math.min(x112, 1840 - 250), y8 - 106, 50, pA, { align: 'center', claims: BC_('victor', 'monthsTo80Index') }); } }   // nhãn TRÊN đường trên giấy (dưới légende), gạch dẫn xuống chấm
    { const [x, y] = S2(L[0] - 5, YI(0.8) - 0.2), [x1, y1] = S2(L[0] + 5, YR(0.95)); log.roi['o0.climbing'] = log.roi['v1.fell'] = [x, y1, x1, y + 10]; }
    // C4 r2 (S17): mức chỉ số LÚC MUA (đường gạch, accent) trên làn Victor + mốc tháng 112: đường trên giấy chạm 80 % khi chỉ số vẫn DƯỚI mức mua
    { const a = lA[2] * ease(t, b.v1.below - 0.05, b.v1.below + POP), V_ = D.buyers.victor, kh = V_.hit;
      if (a > 0.01) { const c = O.ctx, [x0, y0] = S2(XL(L[2], 0), YI(1.0)), [x1] = S2(XL(L[2], 120), YI(1.0)), [xh, yh] = S2(XL(L[2], kh), YI(V_.index[kh]));
        c.save(); c.globalAlpha = a; c.strokeStyle = C.accent; c.lineWidth = 3; c.setLineDash([12, 9]); c.beginPath(); c.moveTo(x0, y0); c.lineTo(x1, y0); c.stroke();
        c.setLineDash([]);   // (r2 thử: gạch dọc từ 80 % xuống chỉ số cắt nhãn "schedule: 90 payments" — F-2 BLOCK → bỏ)
        c.fillStyle = C.accent; c.beginPath(); c.arc(xh, yh, 9, 0, 7); c.fill(); c.strokeStyle = C.accent; c.lineWidth = 4; c.beginPath(); c.moveTo(xh + 18, y0); c.lineTo(xh + 18, yh); c.stroke(); c.restore(); } }
    const vwOut = 1 - ease(t, M.m_all.t0 - 0.3, M.m_all.t0);   // C5b (V12): tên ở nhà Victor rời TRƯỚC cú bay sang ba làn (không trượt nhoè trong cú bay)
    wl('?', VX, vShield.position.y + 0.1, 0.6, (t >= M.m_vw.t0 && t < M.m_all.t1 ? 1 : 0) * ease(t, b.v3.lender - 0.05, b.v3.lender + POP) * vwOut, 96);   // C4 r2: "?" trên khiên ở "lender"
    // nhà Victor
    wl('not in this data', VX, 2.6, 0.2, (t >= M.m_vw.t0 && t < M.m_all.t1 ? 1 : 0) * ease(t, b.v3.show - 0.05, b.v3.show + POP) * vwOut);
    // ba làn cùng gốc
    const aA = ok * inAll * (t < M.m_down.t0 + 0.3 ? 1 - ease(t, M.m_down.t0, M.m_down.t0 + 0.3) : t >= M.m_ans.t1 ? ease(t, M.m_ans.t1, M.m_ans.t1 + POP) * (1 - ease(t, M.m_end.t0 - 0.3, M.m_end.t0)) : 0);   // C5b (V12): chữ đồ thị rời TRƯỚC cú bay về căn nhà
    if (aA > 0.01) {
      ax(XA, aA, true); legend(aA, 2, 1500, 290); const [x75, y75] = S2(XA - 4.9, YR(0.75)); O.text('75%', x75, y75 + 46, 44, { kind: 'number', align: 'right', color: C.muted, alpha: aA });   // khoá nghĩa: bản r2
      const s1 = t < M.m_ans.t0;
      T('same rule, same index · lined up at purchase', 960, 200, 50, aA * (s1 ? ease(t, b.a0.same - 0.05, b.a0.same + POP) : 1), { align: 'center' });
      T('schedule: fixed at the start', 120, 270, 48, aA * (s1 ? ease(t, b.a2.schedule - 0.05, b.a2.schedule + POP) : ease(t, b.e1.schedule - 0.05, b.e1.schedule + POP)), { color: C.muted });
      if (s1) {
        T('on paper: typical 23 months · about 1 in 7 over 60', 120, 334, 48, aA * ease(t, b.a3.history - 0.05, b.a3.history + POP));
        const [px, py] = S2(XL(XA, 24), 2.05), pa = aA * ease(t, b.a3.two - 0.05, b.a3.two + POP);
        T('≈ 2 years matched the typical month —', px + 16, 430, 48, pa); T("not the slow ones, not the lender's step", px + 16, 490, 48, pa);   // khoá nghĩa: chú thích ở chỗ của r2
      } else T('from about 1 year to more than 9 years · on paper', 120, 334, 48, aA * ease(t, b.e1.history - 0.05, b.e1.history + POP));
      ORDER.forEach((k, i) => { const B_ = D.buyers[k], j = B_.paper.length - 1, [x, y] = S2(XL(XA, j), YR(B_.paper[j])); O.text(k[0].toUpperCase() + k.slice(1), x + 12, y + (k === 'owen' ? 40 : -12), 42, { alpha: aA * ease(t, b.a0.started - 0.05, b.a0.started + POP), plate: PLATE, plateA: 0.75 }); });   // C5b V11: nền sau tên (chữ đè đường 3D)   // khoá nghĩa: tên như r2
    }
    { const [x, y] = S2(XL(XA, 24), 2.0), [, y1] = S2(0, 0); log.roi['a3.two'] = [x - 40, y - 10, x + 40, y1]; }
    { const [px, py] = S2(XL(XA, 24), -0.1), pl = aA * (t < M.m_ans.t0 ? 1 : 0) * ease(t, b.a1.plan - 0.05, b.a1.plan + POP); T('a plan', px, py + 62, 56, pl, { kind: 'name', align: 'center' }); }   // C4 r2: tên vạch đứng (dưới chân vạch — trên đầu vạch là dòng "on paper: typical…")
    // hai chồng giá
    const dA = ok * ease(t, M.m_down.t1, M.m_down.t1 + POP) * (1 - ease(t, M.m_fork.t0, M.m_fork.t0 + 0.3));
    if (dA > 0.01) { const [x, y] = S2(XD - 0.8, 4.3); T('$400,000 home', x, y - 10, 54, dA, { align: 'center', kind: 'number' });
      T('20% down on $400,000: $40,000 more', 1300, 560, 46, dA * ease(t, b.a4.forty - 0.05, b.a4.forty + POP), { align: 'center' }); }
    { const [x, y] = S2(XD - 0.8, 0.8), [, y1] = S2(0, 0); log.roi['a4.twenty'] = [x - 90, y - 40, x + 90, y1 + 10]; }
    // hai lối (thế giới: tên)
    const fA = (t >= M.m_fork.t0 && t < M.m_card.t0 + 0.3 ? 1 - ease(t, M.m_card.t0, M.m_card.t0 + 0.3) : t >= M.m_q.t0 && t < M.m_ans.t0 + 0.3 ? 1 - ease(t, M.m_ans.t0, M.m_ans.t0 + 0.3) : 0);
    wl('buying now + mortgage insurance', FX - 1.7, 2.55, 0.25, fA * ease(t, b.a5.renting - 0.05, b.a5.renting + POP) * (t < M.m_q.t0 ? 1 : 0), 48);
    wl('still renting, still saving', FX + 3.3, 2.95, -0.4, fA * ease(t, b.a5.renting - 0.05, b.a5.renting + POP) * (t < M.m_q.t0 ? 1 : 0), 48);
    wl('on paper is not removed', FX - 1.2, 2.7, 0.25, (t >= M.m_end.t0 ? 1 : 0) * ease(t, b.e1.never - 0.05, b.e1.never + POP), 56);
    // thẻ V7 (S19)
    const cA = ok * ease(t, M.m_card.t1, M.m_card.t1 + 0.3) * (1 - ease(t, M.m_q.t0, M.m_q.t0 + 0.3));
    if (cA > 0.01) { O.card(110, 160, 1700, 720, { fill: '#10141B', stroke: C.grid, lw: 3, alpha: cA });   // C4 r3: nền thẻ ĐỤC (vòng 2: toà nhà 3D lộ qua chữ, 7:13); C5b: O.card = thẻ nền (V11 không tính chữ trên thẻ của chính nó)
      // C5b (S07): "Sep 2026" → "September 2026" (= claim rate_month_latest); dòng giữ trong thẻ nên bỏ "(FRED)" (nguồn FRED ở mô tả và dòng nguồn của S06)
      const lines = ['Rates: Freddie Mac 30-year, monthly mean · latest full month September 2026', 'Prices: FHFA purchase-only national index, not seasonally adjusted',
        "Loan: 10% down, 360-month fixed, each purchase month's rate", 'On paper: balance ≤ 80% of price × index change',
        '307 purchase months 1991–2016 · two-year check: 403 months to 2024', 'Law: 12 U.S.C. 4902 · request at 80%, automatic end at 78%',
        'Not modeled: insurance cost, appraisal fees, rent,', 'local prices, how fast savings grow, lender rules'];
      O.text('How we know this', 160, 240, 60, { kind: 'chrome', alpha: cA });
      lines.forEach((s, i) => O.text(s, 160, 322 + i * 66, 42, { kind: 'chrome', w: 600, color: i >= 6 ? C.warn : C.chrome, alpha: cA })); }
    // lớp bắt buộc
    const hist = Math.max(...lA, aA, cA), illus = Math.max(t < M.m_g.t0 + 0.3 ? 1 - ease(t, M.m_g.t0, M.m_g.t0 + 0.3) : 0, ...lA, aA, dA, (t >= M.m_vw.t0 && t < M.m_all.t0 ? 1 : 0));
    const hEnd = t >= M.m_end.t1 ? ease(t, b.e2.us - 0.05, b.e2.us + POP) : 0;
    O.chrome({ illus: illus > 0.01, illusA: illus, src: hist > 0.01 && cA < 0.01 ? 'Source: FHFA · Freddie Mac via FRED' : null, srcA: hist,
      hist: Math.max(hist, hEnd) > 0.01, histA: Math.max(hist, hEnd), cw: hist > 0.01 && cA < 0.01 ? 'Past buyers, measured · not a reason to buy, rent or wait' : dA > 0.01 ? 'A measurement, not a next step' : null, cwA: Math.max(hist * (1 - cA), dA),
      basis: dA > 0.01 ? 'nominal' : null, basisA: dA });   // C5b (S09): S18.5 ($400,000 · $40,000 more) mang nhãn gốc cấp khung
    // C4 r3 (đạo diễn A+B: kết dừng cụt 7:42): khung kết đứng yên rồi tối dần về đen trong 1,5 s cuối, cùng nốt nhạc cuối (bed.py tắt dần 1,5 s cuối)
    { const fb = ease(t, S.total - 1.6, S.total - 0.1); if (fb > 0.002) { const c = O.ctx; c.save(); c.globalAlpha = fb; c.fillStyle = '#000000'; c.fillRect(0, 0, 1920, 1080); c.restore();
      // C5: tấm đen phủ cả chữ → nhật ký/trang kiểm ghi độ hiện THẬT của chữ (× (1 − fb)); điểm ảnh không đổi (C14 1080p bắt chữ "đứng yên, đục" lúc đang tối dần)
      const k = 1 - fb; for (const x of log.texts) x.opacity = +(x.opacity * k).toFixed(3); for (const o of log.objects || []) if (o.kind === 'text') o.opacity = +(o.opacity * k).toFixed(3); } }
    Object.assign(log, measure(cam, WORLD));
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
