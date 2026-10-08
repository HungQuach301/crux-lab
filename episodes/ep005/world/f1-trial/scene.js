// F-1 THỬ (bản sao seg-s01-s03): chuyển wFork→cSched kiểu 'fly' (spine.moves[1].style) — chỉ khác ở các dòng ghi 'F-1'.
// Tập 5 · cold open S01.1 → S03.2 — PORT của đoạn E5k (moc-v/seg/ep005/scene.js), chỉ đổi đường dẫn dữ liệu. Mốc giờ chỉ từ spine.json; hằng số = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { House, Stack, Beam, Person, Ribbon, Studio, Burst, Apartment, Shield, Fan, PALETTE, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, clamp, lin, ease, easeOut, mix, rgba } from '/toolkit/factory/world/core.js';

const FADE = 0.4, POP = 0.15;
const U = 1.25e5;                                     // $ / đơn vị — chồng tiền ở định nghĩa (c4)
const UW = 2e5;                                       // $ / đơn vị — chồng tiền ở thế giới (c0–c1, c5): cả nhà + chồng giá trong khung
const XM = (k) => -5 + 10 * k / 120;                  // đồ thị: tháng sau khi mua 0 → 120
const YL = (l) => (l - 0.75) * 11;                    // đồ thị: dư nợ ÷ giá trị 0,75 (trục) → 1,10 (đường cao nhất của bó)
const WX = -13;                                       // khu thế giới (bên trái mặt phẳng đồ thị, ngoài khung đồ thị)

export async function boot(res) {
  const [S, D, CLm] = await Promise.all([loadJSON('/episodes/ep005/world/f1-trial/spine.json'), loadJSON('/episodes/ep005/work/world-data/derived.json'), loadJSON('/episodes/ep005/world/claims.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const mv = S.moves.filter((m) => m.verb !== 'pull' || m.from !== 'wYou'), all = S.moves;   // mv[0] = đồ thị, mv[1] = lia, mv[2] = về thế giới
  const interp = (kf, t) => { if (t <= kf[0][0]) return kf[0][1]; for (let i = 1; i < kf.length; i++) if (t <= kf[i][0]) { const [a, x] = kf[i - 1], [b, y] = kf[i]; return x + (y - x) * (t - a) / (b - a); } return kf[kf.length - 1][1]; };
  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor } = Studio(scene, { shadowBox: 22 });
  const poses = {
    wYou: { pos: [WX + 2.0, 2.3, 7.8], tgt: [WX + 0.85, 1.75, 0.3], fov: 35, chart: 0 },   // E5d: chặt vào nhà + bạn; lùi máy mới mở ra căn hộ (lý do của cú pull)
    wFork: { pos: [WX + 2.6, 3.0, 11.8], tgt: [WX + 2.1, 1.6, 0], fov: 35, chart: 0 },
    cSched: { pos: [0, 2.0, 35.2], tgt: [0, 2.0, 0], fov: 12, chart: 1 },
    cDef: { pos: [16.8, 2.6, 40.0], tgt: [16.8, 2.6, 0], fov: 12, chart: 1 },
    wHouse: { pos: [WX + 3.4, 3.4, 12.2], tgt: [WX + 1.1, 2.0, 0.2], fov: 35, chart: 0 },
    // F-1: điểm giữa đường bay (x = 0,5) — máy lướt sát mặt trước căn hộ, nhìn về vạch 80 % đang chờ; fov do flyPose tính (dolly-zoom)
    fPass: { pos: [WX + 6.6, 2.2, 6.4], tgt: [WX + 9.0, 1.2, 0], fov: 35, chart: 0 },
  };
  const FLY = S.moves.some((m) => m.style === 'fly');   // F-1: vật thế giới (vạch 20 %, khung đích) KHÔNG mờ khi máy rời — máy đi qua chúng
  // động tác thêm ở thế giới c0 → c1 (lùi máy): giữa "ten" và "buy" — lấy từ spine (cửa sổ tính như spine.window)
  const CAM = Camera(poses, all);
  // ---- vật thể
  // nhà ĐỨNG TRÊN chồng giá của nó (cùng từ vựng hình Tập 4); chồng của người xem = 10 % chồng giá, đặt cạnh để so bằng mắt
  const price = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); price.position.set(WX, 40000 / UW, 0); const priceH = price.set({ usd: 400000, fromUsd: 40000, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 }) + 40000 / UW; scene.add(price);   // E5d: chồng GIÁ = khung mờ …
  const priceBase = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); priceBase.position.set(WX, 0, 0); priceBase.set({ usd: 40000, tintBelowUsd: 40001, tint: C.cushion, tintA: 1 }); scene.add(priceBase);   // … với 10 % đáy ĐẶC (= số bạn đã để dành)
  const loanW = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); loanW.position.set(WX - 1.2, 0, 0.2); scene.add(loanW);   // c5: khoản vay (xám) đã xuống 80 % giá   // E5c: 10 % đáy chồng giá sáng lên trong khoảng nghỉ sau câu 1 (= chồng của bạn)
  const house = House({ w: 1.5 }); house.position.set(WX, priceH, 0); scene.add(house);   // c0: nhà bị NÂNG lên khi tháp giá mọc (chữ "price")
  const mine = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); mine.position.set(WX + 1.15, 0, 0); scene.add(mine);   // sát chồng giá, cùng đáy: 10 % so bằng mắt
  const you = Person({ h: 1.15, color: PALETTE.person2 }); you.position.set(WX + 2.1, 0, 0.6); you.rotation.y = -0.4; scene.add(you);
  const apt = Apartment({ w: 1.6 }); apt.position.set(WX + 4.4, 0, -0.6); scene.add(apt);
  const shield = Shield({ size: 0.95 }); scene.add(shield);
  let roofY = priceH + house.userData.height * 0.86;
  const target = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); target.position.set(WX + 3.1, 0, 0.4); scene.add(target);
  const rentStack = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); rentStack.position.set(WX + 3.1, 0, 0.4); scene.add(rentStack);   // lối thuê: cạnh căn hộ
  const tick20 = new THREE.Mesh(new THREE.BoxGeometry(1.3, 0.06, 0.06), new THREE.MeshBasicMaterial({ color: C.warn, transparent: true })); tick20.position.set(WX + 3.1, 80000 / UW, 0.4); scene.add(tick20);
  // đồ thị
  const bar80 = Beam({ length: 10.8 }); bar80.position.set(0, YL(0.8), 0); scene.add(bar80);
  const sched = Ribbon({ color: C.muted, z: 0.5 }), typ = Ribbon({ color: C.ink, z: 0.6 }), slow = Ribbon({ color: C.warn, z: 0.6 }); scene.add(sched, typ, slow);
  const fan = Fan(); scene.add(fan);
  const burst = Burst(); scene.add(burst);
  // định nghĩa (c4): chồng GIÁ TRỊ và chồng VAY chính diện
  const vStack = Stack({ unitUsd: U, w: 1.3, d: 0.8 }), lStack = Stack({ unitUsd: U, w: 1.3, d: 0.8 }); vStack.position.set(15.2, 0, 0); lStack.position.set(18.4, 0, 0); scene.add(vStack, lStack);
  const vHouse = House({ w: 1.2 }); scene.add(vHouse);
  const bar80b = Beam({ length: 6.0, color: C.muted }); bar80b.position.set(16.8, 0, 0); scene.add(bar80b);
  const paths = D.paths, nP = paths.length, typP = paths.find((p) => p.m === D.typical), slowP = paths.find((p) => p.m === D.slow);
  const fanCol = new THREE.Color(C.bg).lerp(new THREE.Color(C.ink), 0.2).getStyle();   // E5c: bó dịu hơn, một nửa số tháng (đạo diễn: "mảng lưới trắng")

  // F-1 đo che khung: mỗi vật thế giới → hộp bao 3D (Box3, InstancedMesh tính lại theo bó đang hiện) chiếu ra màn hình, cắt theo khung;
  // tỉ lệ diện tích hình chữ nhật bao = CHẶN TRÊN của phần khung vật đó che. Góc nằm sau máy (w ≤ 0) → coi như che cả khung.
  const WORLD = { house, price, mine, you, apt, shield, rentStack, target, loanW }, bx = new THREE.Box3(), b1 = new THREE.Box3(), cv = new THREE.Vector4();
  function cover() {
    let best = { f: 0, obj: null };
    for (const [name, o] of Object.entries(WORLD)) {
      bx.makeEmpty(); o.updateMatrixWorld(true);
      o.traverse((m) => {   // chỉ phần đang hiện (setOpacity ẩn mesh ở độ mờ ≈ 0)
        if (!m.isMesh || !m.visible) return;
        if (m.isInstancedMesh) m.computeBoundingBox(); else if (!m.geometry.boundingBox) m.geometry.computeBoundingBox();
        bx.union(b1.copy(m.isInstancedMesh ? m.boundingBox : m.geometry.boundingBox).applyMatrix4(m.matrixWorld));
      });
      if (bx.isEmpty()) continue;
      let x0 = 1, x1 = -1, y0 = 1, y1 = -1, behind = false;
      for (let i = 0; i < 8; i++) {
        cv.set(i & 1 ? bx.max.x : bx.min.x, i & 2 ? bx.max.y : bx.min.y, i & 4 ? bx.max.z : bx.min.z, 1).applyMatrix4(CAM.cam.matrixWorldInverse).applyMatrix4(CAM.cam.projectionMatrix);
        if (cv.w <= 1e-6) { behind = true; break; }
        const x = cv.x / cv.w, y = cv.y / cv.w; x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y);
      }
      const f = behind ? 1 : Math.max(0, Math.min(1, x1) - Math.max(-1, x0)) * Math.max(0, Math.min(1, y1) - Math.max(-1, y0)) / 4;
      if (f > best.f) best = { f: +f.toFixed(4), obj: name };
    }
    return best;
  }

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam, b = cue;
    floor.material.opacity = 1 - 0.85 * cw;
    scene.fog.near = mix(30, 150, cw); scene.fog.far = mix(80, 300, cw);   // sương thế giới không phủ đồ thị (bài học Tập 4 v3d)
    // ---------- thế giới: c0–c1, c5
    const worldA = 1;   // E5b: vật thế giới KHÔNG mờ đi — máy quay đi khỏi chúng (đạo diễn E5a: đổi chế độ thành fade)
    for (const o of [house, apt, you]) setOpacity(o, worldA); setOpacity(priceBase, 0);   // E5f: đáy 10 % = CHÍNH chồng của bạn trượt vào (không vẽ hai lần)
    // E5e móc 0–5 s: dải 10 % (teal) hiện ở "ten"; tháp GIÁ (xám) mọc ở "price" và nâng ngôi nhà lên — tiền của bạn nhỏ thế nào so với giá
    const bA = easeOut(t, b.c0.ten, b.c0.ten + 0.3), pG = easeOut(t, b.c0.price, b.c0.price + 0.9);
    const bH = 40000 / UW * bA;   // chồng của bạn (40k) trượt từ tay bạn vào dưới nhà ở chữ "ten"
    price.position.y = bH; const pH = price.set({ usd: 40000 + 360000 * pG, fromUsd: 40000, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 });
    house.position.y = bH + pH; roofY = house.position.y + house.userData.height * 0.86;
    setOpacity(price, 1.0);   // đặc, xám nhạt (bản mờ không hiện được với InstancedMesh trong suốt)   // khung mờ: giá của căn nhà, không phải tiền của bạn
    const lw = ease(t, b.c5.t0, b.c5.same); loanW.set({ usd: 320000 * lw, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 });   // cùng màu chồng vay ở đồ thị
    setOpacity(loanW, lw > 0.01 ? 1 : 0);
    mine.set({ usd: 40000 * easeOut(t, b.c0.saved, b.c0.saved + 0.25), tintBelowUsd: 1e9, tint: C.cushion, tintA: 1 }); setOpacity(mine, t >= b.c0.saved ? worldA : 0);
    mine.position.set(mix(WX + 1.15, WX, bA), 0, 0);   // "ten percent of a home's price": tiền của bạn = đáy chồng giá
    // lối THUÊ (c1): ở căn hộ, khoản để dành mới lớn từ 10 % tới 20 % (chữ "twenty")
    const rentA = ease(t, b.c1.renting, b.c1.renting + POP);
    rentStack.set({ usd: 40000 + 40000 * easeOut(t, b.c1.twenty, b.c1.twenty + 0.9), tintBelowUsd: 1e9, tint: C.cushion, tintA: 1 }); setOpacity(rentStack, rentA);
    const wOut = FLY ? 1 : 1 - ease(t, mv[0].t0, mv[0].t0 + 0.3);   // F-1
    tick20.material.opacity = worldA * ease(t, b.c1.renting, b.c1.renting + POP) * wOut;
    target.set({ usd: 80000 }); setOpacity(target, 0.28 * ease(t, b.c1.renting, b.c1.renting + POP) * wOut);   // đích 20 %: khung mờ
    // khiên rơi lên mái lúc "insurance", ở lại (c5 rung nhẹ lúc "same" rồi đứng yên lúc "removed")
    const sd = easeOut(t, b.c1.insurance - 0.05, b.c1.insurance + 0.25), wob = t >= b.c5.same && t < b.c5.removed + 0.3 ? Math.sin((t - b.c5.same) * 18) * 0.12 * (1 - lin(t, b.c5.removed - 0.2, b.c5.removed + 0.3)) : 0;
    shield.position.set(WX, mix(roofY + 2.2, roofY, sd), 0.25); shield.rotation.z = wob; setOpacity(shield, worldA * (t >= b.c1.insurance - 0.05 ? 1 : 0));
    // ---------- đồ thị c2: lịch trả nợ
    const kS = interp(S.sched_kf, t), chartA = cw;
    if (t >= b.c2.schedule) {
      const pts = []; for (let k = 0; k <= Math.min(120, kS) + 1e-6; k += 1) pts.push([XM(Math.min(k, kS)), YL(D.sched[Math.min(120, Math.round(Math.min(k, kS)))])]);
      sched.set(pts, 0.08, C.muted); sched.material.opacity = chartA * (1 - ease(t, b.c3.replayed, b.c3.replayed + 0.6));   // E5f: đường minh hoạ RỜI khi dữ liệu thật vào (vạch gióng + nhãn 8 năm ở lại)
    } else sched.material.opacity = 0;
    setOpacity(bar80, (t >= mv[0].t0 && t < mv[2].t1) ? 1 : 0);   // vạch 80 % có mặt khi máy tới (không khung trống), rời sau cú lia
    bar80.glow(t >= b.c2.eight ? Math.max(0, 1 - lin(t, b.c2.eight, b.c2.eight + 0.8)) : 0);
    // c3: bó phát lại
    const f = interp(S.fan_kf, t);
    if (t >= b.c3.replayed - 0.05 && t < mv[2].t1) {
      const lines = [], kk = Math.round(f * 120);   // E5b: PHÁT LẠI = mọi tháng mua cùng chạy theo thời gian sau khi mua (quét trái → phải, khớp tick mỗi năm)
      for (let i = 0; i < nP; i += 2) { const pp = paths[i].p.slice(0, kk + 1); if (pp.length > 1) lines.push({ color: fanCol, pts: pp.map((l, k) => [XM(k), YL(l)]) }); }
      fan.set(lines); fan.material.opacity = Math.max(0.35, 1 - ease(t, mv[1].t1 - 0.4, mv[1].t1)) * (t < mv[2].t1 ? 1 : 0);   // E5g: bó còn mờ trong khung khi máy lướt về (không khung đen)
    } else fan.material.opacity = 0;
    const tA = ease(t, b.c3.typically - 0.05, b.c3.typically + POP) * chartA, sA = ease(t, b.c3.slow - 0.05, b.c3.slow + POP) * chartA;
    typ.set(typP.p.map((l, k) => [XM(k), YL(l)]), 0.12, C.ink); typ.material.opacity = tA * (1 - ease(t, mv[1].t1 - 0.4, mv[1].t1));
    slow.set(slowP.p.map((l, k) => [XM(k), YL(l)]), 0.12, C.accent); slow.material.opacity = sA * (1 - ease(t, mv[1].t1 - 0.4, mv[1].t1));   // (b) màu trung tính (vàng cảnh báo gợi "rủi ro → lời khuyên"). PORT ep005: E5k để lệnh opacity TRONG chú thích → đường chậm hiện từ c2; sửa lại đúng ý (hiện ở "slow")
    const fl = t >= b.c2.eight ? 1 - lin(t, b.c2.eight, b.c2.eight + 0.7) : 0;
    burst.position.set(XM(D.sched80), YL(0.8), 0.7); burst.scale.setScalar(0.5 + 2 * (1 - fl)); burst.material.opacity = fl * chartA;
    // c4: định nghĩa "on paper"
    const dA = ease(t, mv[1].t0, mv[1].t1) * (1 - ease(t, mv[2].t1 - 0.2, mv[2].t1));   // chữ của định nghĩa rời khi máy đã về
    const r = lin(t, b.c4.paper, b.c4.eighty);              // tỉ lệ đi từ 90 % xuống 80 %, CHẠM 80 đúng chữ "eighty" (E5a: sớm 0,55 s)
    const vUsd = mix(400000, 440000, r), lUsd = mix(360000, 352000, r);
    const vh = vStack.set({ usd: vUsd, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 }), lh = lStack.set({ usd: lUsd, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 });   // E5e: cùng mã màu với thế giới (giá = xám nhạt, vay = xám đậm)
    vHouse.scale.setScalar(0.001); setOpacity(vHouse, 0);   // E5g: đồ thị chỉ có chồng (nhà là vật thế giới — cùng quy tắc Tập 4)   // đồ thị: đỉnh chồng là điểm dữ liệu — nhà đứng cạnh, mái thấp hơn
    bar80b.position.y = 0.8 * vUsd / U;
    for (const o of [vStack, lStack]) setOpacity(o, dA > 0.01 ? 1 : 0); setOpacity(bar80b, dA * ease(t, b.c4.eighty - 0.05, b.c4.eighty + POP));

    renderer.render(scene, cam);
    // ======================= lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, S2 = (x, y) => O.toScreen(x, y, 0.5); log.roi = {};
    log.cover = cover();   // F-1: che khung khi máy đi qua (chỉ ghi nhật ký, không đổi điểm ảnh)
    { const [x0, y0] = O.toScreen(WX, 0.1, 0); log.roi['c0.ten'] = [x0 - 90, y0 - 70, x0 + 90, y0 + 50]; }   // chồng 10 % đặt xuống
    { const [x0, y0] = O.toScreen(WX + 3.1, 0.3, 0.4); log.roi['c1.twenty'] = [x0 - 70, y0 - 60, x0 + 70, y0 + 50]; }          // chồng của người xem lớn tới 20 %
    { const [lx0, ly0] = O.toScreen(18.4, 3.0, 0); log.roi['c4.paper'] = [lx0 - 90, ly0 - 80, lx0 + 260, ly0 + 80]; }   // đỉnh chồng vay + bộ đếm %
    { const [x0, y0] = O.toScreen(XM(0), YL(0.9), 0.5), [x1, y1] = O.toScreen(XM(30), YL(0.85), 0.5); log.roi['c2.schedule'] = [x0 - 20, y0 - 40, x1 + 20, y1 + 40]; }   // đầu đường lịch trả nợ
    // c0–c1 (thế giới, không số)
    const youA = ease(t, b.c0.t0, b.c0.t0 + POP) * (1 - ease(t, mv[0].t0, mv[0].t0 + FADE));   // "You've…" = nhãn You ngay chữ đầu
    if (youA > 0) { const [x, y] = O.toScreen(WX + 2.1, 1.45, 0.6); O.text('You', x, y - 20, 56, { align: 'center', alpha: youA, plate: '#0B0E13', plateA: 0.6 }); }
    const lOut = 1 - ease(t, mv[0].t0, mv[0].t0 + 0.3);           // nhãn thế giới rời TRƯỚC khi máy đổi chế độ (không chồng nhau giữa đường)
    const iA = ease(t, b.c1.insurance - 0.05, b.c1.insurance + POP) * worldA * lOut;
    if (iA > 0 && t < mv[0].t1) { const [x, y] = O.toScreen(WX, roofY + 0.75, 0.2); O.text('buy now + mortgage insurance', x, y - 20, 48, { align: 'center', alpha: iA, plate: '#0B0E13', plateA: 0.6 }); }
    const rA = ease(t, b.c1.renting - 0.05, b.c1.renting + POP) * worldA * lOut;
    if (rA > 0 && t < mv[0].t1) { const [x, y] = O.toScreen(WX + 4.4, 2.35, -0.6); O.text('keep renting, keep saving', x, y - 20, 48, { align: 'center', alpha: rA, plate: '#0B0E13', plateA: 0.6 }); }
    // c2 (đồ thị)
    if (cw > 0.02 && t < mv[1].t1) {
      const aA = ok * (1 - ease(t, mv[1].t0, mv[1].t0 + FADE));
      for (let yr = 0; yr <= 10; yr += 2) { const [x, y] = S2(XM(yr * 12), 0); O.text(yr === 10 ? '10 years' : String(yr), x, y + 48, 44, { kind: 'number', w: 600, color: C.muted, align: 'center', alpha: aA }); }
      for (const l of [0.9, 0.8]) {   // (b) bỏ nhãn 100 % (gợi "nợ nhiều hơn giá nhà")
        const [x, y] = S2(XM(0), YL(l)); O.text(`${Math.round(l * 100)}%`, x - 24, y + 16, 48, { kind: 'number', color: l === 0.8 ? C.ink : C.muted, align: 'right', alpha: aA * (l === 1.0 ? ease(t, b.c3.replayed - 0.05, b.c3.replayed + POP) : 1) }); }
      O.text('loan as a share of the price · on the schedule', 960, 230, 52, { kind: 'compare', align: 'center', color: C.muted, alpha: aA * (1 - ease(t, b.c3.replayed - 0.3, b.c3.replayed - 0.05)) });
      O.text('Loan as % of home value · one line per purchase month, 1991–2016', 960, 230, 48, { kind: 'compare', align: 'center', color: C.ink, alpha: aA * ease(t, b.c3.replayed, b.c3.replayed + POP) });
      const eA = ease(t, b.c2.eight, b.c2.eight + POP) * aA;
      if (eA > 0) { const [x, y] = S2(XM(D.sched80), YL(0.8)); O.ctx.save(); O.ctx.globalAlpha = eA; O.ctx.setLineDash([10, 8]); O.ctx.strokeStyle = C.muted; O.ctx.lineWidth = 3; O.ctx.beginPath(); O.ctx.moveTo(x, y); O.ctx.lineTo(x, S2(0, 0)[1]); O.ctx.stroke(); O.ctx.restore();
        O.text(t < b.c3.replayed ? 'about 8 years' : 'schedule ≈ 8 years', t < b.c3.replayed ? x - 16 : S2(XM(120), 0)[0], y + 70, 56, { kind: 'number', color: C.ink, align: 'right', alpha: eA, plate: '#0B0E13', plateA: 0.7 }); }   // dưới vạch, trái đường gióng (đường chậm đi xuống ở bên phải)
      if (tA > 0) { const k = typP.p.length - 1, [x, y] = S2(XM(k), YL(typP.p[k])); O.text(`typical ≈ ${Math.round(CLm.medianB_months_to80.value / 12)} years`, x + 20, y + 64, 60, { kind: 'compare', color: C.ink, alpha: ok * tA / Math.max(cw, 1e-3) * (1 - ease(t, mv[1].t0, mv[1].t0 + FADE)) }); }
      if (sA > 0) { const k = slowP.p.indexOf(Math.max(...slowP.p)), [x, y] = S2(XM(k), YL(slowP.p[k])); O.text(`slowest case ≈ ${Math.round(CLm.maxB_months_to80.value / 12)} years`, x, y - 40, 52, { kind: 'compare', color: C.accent, align: 'center', alpha: ok * sA / Math.max(cw, 1e-3) * (1 - ease(t, mv[1].t0, mv[1].t0 + FADE)) }); }
    }
    // c4 (đồ thị: định nghĩa)
    if (dA > 0.02) {
      const a = dA * ok;
      const [vx, vy] = S2(15.2, (vUsd / U) + 0.45), [lx, ly] = S2(18.4, lUsd / U);
      const vA = a * ease(t, b.c4.value, b.c4.value + POP);   // E5e: chữ theo lời ("the home's value by a national price index")
      O.text('home value', vx, vy - 74, 52, { color: C.ink, align: 'center', alpha: vA });
      O.text('by a national price index', vx, vy - 16, 48, { color: C.ink, w: 600, align: 'center', alpha: vA });   // vòng mù Tập 5 #1: E2 hụt "theo chỉ số giá" → nhãn đứng cùng "home value"
      O.text('loan', lx, ly - 30, 52, { color: C.ink, align: 'center', alpha: a * ease(t, b.c4.paper, b.c4.paper + POP) });
      const pct = t < b.c4.paper + POP ? 90 : t < b.c4.eighty ? Math.max(81, Math.round(100 * lUsd / vUsd)) : 80;
      O.text(`${pct}%`, lx + 120, ly + 16, 60, { kind: 'compare', color: pct <= 80 ? C.ink : C.muted, alpha: a * ease(t, b.c4.paper, b.c4.paper + POP) * (1 - ease(t, b.c4.eighty, b.c4.eighty + POP)) });   // bộ đếm bật ĐÚNG "on paper" rồi chạy tới 80
      const [bx, by] = S2(18.4 + 0.9, 0.8 * vUsd / U);
      O.text('80% on paper', bx + 10, by + 16, 60, { kind: 'compare', color: C.ink, alpha: a * ease(t, b.c4.eighty - 0.05, b.c4.eighty + POP), plate: '#0B0E13', plateA: 0.7 });
    }
    // E5g: lối thuê lớn tới 20 % — mũi tên đi lên trên chồng ở căn hộ (cùng từ vựng hình "rise" của Tập 4)
    { const ua = ease(t, b.c1.twenty, b.c1.twenty + POP) * (1 - ease(t, mv[0].t0, mv[0].t0 + 0.3));
      if (ua > 0.01) { const [ux, uy] = O.toScreen(WX + 3.1, 0.55 + 0.35 * easeOut(t, b.c1.twenty, b.c1.twenty + 0.9), 0.4), c = O.ctx; c.save(); c.globalAlpha = ua; c.fillStyle = C.accent;
        c.beginPath(); c.moveTo(ux, uy - 54); c.lineTo(ux - 28, uy - 12); c.lineTo(ux + 28, uy - 12); c.closePath(); c.fill(); c.fillRect(ux - 10, uy - 14, 20, 60); c.restore(); } }
    // c5 (thế giới)
    const kA = ease(t, b.c5.removed - 0.05, b.c5.removed + POP) * worldA;
    if (kA > 0) { const [x, y] = O.toScreen(WX, roofY + 0.75, 0.2); O.text('insurance still on', x, y - 20, 56, { align: 'center', alpha: kA, plate: '#0B0E13', plateA: 0.7 }); }
    const chOut = 1 - ease(t, mv[2].t0, mv[2].t0 + 0.4);   // E5e: lớp chữ của đồ thị rời khi về cảnh thế giới
    const illA = Math.max(ease(t, b.c2.schedule, b.c2.schedule + POP) * (1 - ease(t, b.c3.replayed - 0.3, b.c3.replayed)), ease(t, mv[1].t1, mv[1].t1 + POP)) * chOut;   // minh hoạ: lịch giả định (c2), hai chồng (c4); KHÔNG trên dữ liệu thật (c3)
    O.chrome({ illus: illA > 0.01, illusA: illA, src: t >= b.c2.schedule ? 'Source: FHFA · Freddie Mac via FRED' : null, srcA: ease(t, b.c2.schedule, b.c2.schedule + POP) * chOut,
      hist: t >= b.c3.replayed, histA: ease(t, b.c3.replayed, b.c3.replayed + POP) * chOut,
      cw: t >= b.c3.replayed ? 'Past buyers, measured · not a reason to buy, rent or wait' : t >= b.c2.schedule ? 'A measurement, not a next step' : null,
      cwA: (t >= b.c3.replayed ? ease(t, b.c3.replayed, b.c3.replayed + POP) : ease(t, b.c2.schedule, b.c2.schedule + POP)) * chOut });   // đối trọng kênh; vòng mù Tập 5 #2: E1 vẫn khuyên "ở đủ lâu mới mua" → câu rõ hơn (vòng mù #1: E1 có câu khuyên "chỉ mua nếu…")
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
