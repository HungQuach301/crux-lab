// Mốc V · đoạn (a) Tập 4 — cảnh "một thế giới, hai chế độ máy quay". Mọi mốc từ spine.json (cues/moves/draw/ride/events);
// hằng số trong file chỉ là HÌNH HỌC (toạ độ, kích thước) và độ dài hiệu ứng chung (FADE…), không phải mốc giờ.
import * as THREE from 'three';
import { House, Stack, Beam, Person, Neighborhood, Ribbon, Studio, Burst, PALETTE, setOpacity } from '../../world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, clamp, lin, ease, easeOut, mix, rgba } from '../../world/core.js';

const FADE = 0.4, POP = 0.15;                       // độ dài hiệu ứng chung (giây)
const U = 1e5;                                      // $ / đơn vị thế giới (trục y)
const X = (q) => -9 + 18 * q / 105;                 // trục thời gian: quý 0 (2000 Q1) → 105 (2026 Q2)

export async function boot(res) {
  const [S, D] = await Promise.all([loadJSON('/moc-v/seg/ep004/spine.json'), loadJSON('/moc-v/proto/data.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const mv = S.moves, M = Object.fromEntries(S.moves.map((m) => [m.id, m]));
  const gain = D.gain.map((p) => p.y), at = (q) => { const i = Math.floor(clamp(q, 0, 105)), f = q - i; return i < 105 ? mix(gain[i], gain[i + 1], f) : gain[105]; };
  const valueAt = (q) => at(q) + 200000;
  const interp = (kf, t) => { if (t <= kf[0][0]) return kf[0][1]; for (let i = 1; i < kf.length; i++) if (t <= kf[i][0]) { const [a, x] = kf[i - 1], [b, y] = kf[i]; return x + (y - x) * (t - a) / (b - a); } return kf[kf.length - 1][1]; };
  const CL = (k) => D.claims[k].display;
  const qYear = (q) => 2000 + q / 4;
  const dataEv = S.events.filter((e) => e.kind === 'data'), pops = S.pops;

  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor } = Studio(scene);
  // ---- tư thế máy quay (hình học); chart = 1 → chế độ đồ thị chính diện (tele gần trực giao)
  const poses = {
    wHome: { pos: [-6.0, 3.4, 10.5], tgt: [-9, 2.7, 0], fov: 35, chart: 0 },
    wHood: { pos: [-6.4, 3.4, 12.0], tgt: [-8.6, 1.8, -1.6], fov: 35, chart: 0 },
    cFull: { pos: [0, 3.3, 64.2], tgt: [0, 3.3, 0], fov: 13.5, chart: 1 },        // v3d: trục năm nằm TRÊN hai dòng chú đáy
    wDemo: { pos: [15.8, 4.6, 29.0], tgt: [13.6, 3.4, 6], fov: 35, chart: 0 },   // v3g: thấy trọn chồng ×4 + mái
    wDemoNear: { pos: [15.3, 3.0, 16.6], tgt: [13.3, 1.75, 6], fov: 35, chart: 0 },
    wDemoClose: { pos: [14.85, 2.75, 14.6], tgt: [13.4, 1.6, 6], fov: 35, chart: 0 },   // v3f: đẩy vào nhà + chồng đủ thấy
    cZoom: { pos: [7.0, 5.4, 20.9], tgt: [7.0, 5.4, 0], fov: 12, chart: 1 },
    cTip: { pos: [9.15, 5.25, 16.0], tgt: [9.15, 5.25, 0], fov: 12, chart: 1 },   // v3h: "past the cap" trong vùng an toàn; vật lên cao khỏi dòng chú          // v3d: chừa chỗ cho hộp số dưới huy hiệu ILLUSTRATIVE
  };
  const CAM = Camera(poses, mv);

  // ---- vật thể (thư viện)
  const hero = House({ w: 1.5 }), heroStack = Stack({ unitUsd: U, bundleUsd: 25000, w: 1.0, d: 0.7 });
  const heroG = new THREE.Group(); heroG.add(heroStack, hero); scene.add(heroG);
  const rosa = Person({ h: 1.05, color: PALETTE.person1 }), frank = Person({ h: 1.12, color: PALETTE.person2 }); scene.add(rosa, frank);
  const beam = Beam({ length: 19.4 }); beam.position.set(0, 5, 0); scene.add(beam);
  const hood = Neighborhood({ n: 12, spanX: [-12.8, -5.2], z: -2.6, size: 0.85 }); scene.add(hood);
  const vRib = Ribbon({ color: C.accent }), gRib = Ribbon({ color: C.ink }); scene.add(vRib, gRib);
  // cảnh minh hoạ b4 (trước mặt, z = 5): nhà + chồng (đáy $200,000 tách được) + Rosa & Frank
  const demo = new THREE.Group(); demo.position.set(14, 0, 6); scene.add(demo);   // cảnh minh hoạ luôn có mặt trong cùng thế giới (ngoài khung đồ thị)
  const dHouse = House({ w: 1.5 }), dTop = Stack({ unitUsd: U, w: 1.0, d: 0.7 }), dSlab = Stack({ unitUsd: U, w: 1.0, d: 0.7 });
  const dRosa = Person({ h: 1.05, color: PALETTE.person1 }), dFrank = Person({ h: 1.12, color: PALETTE.person2 });
  demo.add(dHouse, dTop, dSlab, dRosa, dFrank); dRosa.position.set(-3.6, 0, 0.7); dFrank.position.set(-3.05, 0, 0.9); dRosa.rotation.y = dFrank.rotation.y = 0.5;
  // b11: hai chồng GIÁ TRỊ ở 2000 và 2026 Q2
  // b11: chồng GIÁ năm 2000 (= cái họ trả, teal) đứng cạnh chính nhà của họ ở 2026, khi khối teal trượt về đáy chồng (lãi → giá)
  const s2000 = Stack({ unitUsd: U, w: 1.0, d: 0.7 }); s2000.position.set(X(0), 0, 0); s2000.scale.set(0.55, 1, 0.55); scene.add(s2000);
  const h2000 = House({ w: 1.5 }); h2000.scale.setScalar(0.55); scene.add(h2000);
  const burst = Burst(); scene.add(burst);
  const ghostBeam = Beam({ length: 5 }); ghostBeam.position.set(X(0), 5, 0); ghostBeam.rotation.y = Math.atan2(3, 10.5); scene.add(ghostBeam);   // v3g: vuông góc hướng nhìn của wHome → PHẲNG trên màn

  // ---- âm ↔ hình: nhịp sáng ở mỗi nốt dữ liệu
  const pulseAt = (t) => { let p = 0; for (const e of dataEv) if (t >= e.t && t < e.t + 0.18) p = Math.max(p, 1 - (t - e.t) / 0.18); return p; };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    const b = cue;
    // thế giới mờ đi ở chế độ đồ thị
    floor.material.opacity = 1 - 0.85 * cw;
    scene.fog.near = mix(30, 150, cw); scene.fog.far = mix(80, 300, cw);   // v3d: sương thế giới KHÔNG phủ đồ thị (máy ở xa 64 đv → chồng tiền, đường bị tối)
    // ---------------- giai đoạn
    const qDraw = interp(S.draw, t), riding = t >= S.ride[0][0], qRide = riding ? interp(S.ride, t) : 0;
    const ride0 = S.ride[0][0], inDemo = t >= M.toDemo.t0 && t < ride0;
    const rb = ease(t, M.backChart.t0, ride0);                     // v3d: NHÀ của họ tua về 2000 trong lúc đổi chế độ (không nhảy ngang khung)
    const valueOff = ease(t, b.b3.cap, b.b3.cap + 0.8);   // v3d: tắt dịu hơn (lượt đạo diễn: "tắt đột ngột")          // b3: giá trị + nhà tắt khi trần vào
    // nhà chính
    let heroA = 1, hx = X(0), usd = 200000, hScale = 1;
    if (t < b.b2.quarter) { hx = X(0); usd = 200000; }
    else if (!riding) { hx = X(qDraw); usd = valueAt(qDraw); heroA = 1 - valueOff; }
    else { hx = X(qRide); usd = Math.max(0, at(qRide)); heroA = 1; }   // nhà minh hoạ đã tua về đúng chỗ này (2000, lãi 0) → thay nhau liền
    if (inDemo && !riding) heroA = 0;
    hScale = mix(1, 0.55, cw);
    const bump = 0;                                                    // v3e: nhà không còn ở trên đỉnh chồng ở chế độ đồ thị → không nảy
    const flashCap = t >= S.marks.hop_land ? 1 - lin(t, S.marks.hop_land, S.marks.hop_land + 0.6) : 0;   // chớp ở chỗ chồng xuyên xà, đúng tiếng chạm sau "cap"
    const out11 = 1 - ease(t, M.wide.t0, M.wide.t1);                  // b11: đại lượng đổi lãi → GIÁ: đường lãi, xà, nhãn trần tắt hẳn (logic b3)
    const off11 = 1 - ease(t, b.b11.t0, M.wide.t0 + 0.3);           // v3h: bắt đầu ở chữ "Phoenix" (rải dài hơn)            // v3f: đại lượng LÃI (xà, đường, nhãn trần) rời ngay đầu cú lùi — không cross-fade với khung giá
    const r11 = ease(t, b.b11.t0, b.b11.x + 0.3);                      // đường lãi NÂNG $200,000 từ chữ "Phoenix" (thấy ngay trong khung đầu nhà)               // cùng lúc: khối "what they paid" về đáy chồng 2026 — chồng lớn lên = GIÁ (khung luôn có chồng + nhà)
    const gone11 = 1 - ease(t, M.wide.t0, M.wide.t1);                  // b11: nhà lãi + người rời cảnh (nhường hai chồng giá trị)
    heroStack.scale.set(hScale, 1, hScale);
    const sh = t < b.b11.t0 ? heroStack.set({ usd, warnAboveUsd: riding ? 500000 : Infinity })
      : heroStack.set({ usd: usd + 200000 * r11, tintBelowUsd: 200000 * r11 + 1, tintA: 1, warnAboveUsd: off11 > 0.5 ? 500000 + 200000 * r11 : Infinity });   // b11: lãi + cái đã trả = giá 2026
    // v3e (lượt đạo diễn v3d): ở chế độ ĐỒ THỊ điểm dữ liệu là ĐỈNH CHỒNG — nhà đứng cạnh, mái không vượt điểm dữ liệu (không "vượt trần" sớm)
    const houseH = hero.userData.height * hScale, hOff = cw * (0.5 * hScale + 0.75 * hScale + 0.06);
    hero.scale.setScalar(hScale); hero.position.set(hOff, mix(sh, Math.max(0, Math.min(sh, mix(4.95, sh, ease(t, M.wide.t1 - 0.3, M.wide.t1 + 0.3))) - houseH - 0.05), cw), 0);   // v3g: ở đồ thị mái nhà cũng KHÔNG vượt xà (đạo diễn v3f: gợi "giá nhà vượt trần")
    const roofY = hero.position.y + houseH;
    heroG.position.set(hx, 0, 0);
    // khu phố (b1) bật biển đúng tick, gom về nhà chính lúc "sales"
    const gather = ease(t, b.b1.avg - 0.1, b.b1.avg + 0.9);
    hood.userData.items.forEach((it, k) => {
      const ap = ease(t, M.hood.t0 + 0.06 * k, M.hood.t1 + 0.06 * k) * (1 + 0.25 * Math.sin(Math.PI * lin(t, pops[k], pops[k] + 0.3))), g = gather;   // v3d: khu phố có mặt khi lùi máy; biển SOLD bật đúng tick
      it.it.position.lerpVectors(it.home, new THREE.Vector3(X(0), 1.8, 0), g); it.it.position.y += Math.sin(Math.PI * g) * 1.6; it.it.scale.setScalar(Math.max(0.001, ap * (1 - 0.7 * g)));
      setOpacity(it.it, (1 - ease(g, 0.82, 1)) * (1 - cw));
      it.sign.visible = it.it.visible && t >= pops[k]; it.sign.scale.setScalar(Math.max(0.001, 2.6 * easeOut(t, pops[k], pops[k] + 0.12)));   // biển to hơn (đọc được ở điện thoại), bật có nảy   // SAU setOpacity (nó bật visible cho mọi con) — biển SOLD bật đúng tick
    });
    // sương "can't see their house" (b1) → nhà mờ
    const fog = ease(t, b.b1.blur, b.b1.blur + FADE) * (1 - ease(t, b.b1.avg, b.b1.avg + 0.8));
    setOpacity(hero, heroA * (1 - 0.7 * fog)); setOpacity(heroStack, heroA);
    // người (b0) và (b9–b10) cạnh nhà ở đầu đường
    const pA0 = 1 - ease(t, b.b1.blur - 0.1, b.b1.blur + FADE);
    const pA9 = 0;   // v3e: ở chế độ đồ thị người không đứng lơ lửng cạnh điểm dữ liệu (nhãn "their gain on paper" mang "của họ")
    const pA = Math.max(pA0, pA9);
    const on9 = pA9 > pA0, ps = on9 ? 0.5 : 1, px = on9 ? hx - 0.5 : X(0) - 1.6, py = on9 ? Math.max(0, sh - 0.62) : 0;   // b9: đứng sau đường, đầu thấp hơn điểm dữ liệu
    rosa.position.set(px, py, on9 ? -0.6 : 0.5); frank.position.set(px + (on9 ? -0.3 : 0.55), py, on9 ? -0.5 : 0.7); rosa.scale.setScalar(ps); frank.scale.setScalar(ps);
    rosa.rotation.y = frank.rotation.y = 0.35; setOpacity(rosa, pA); setOpacity(frank, pA);
    // xà trần: bóng mờ b0; xà thật từ b3 (rơi + khoá); chỉ ở chế độ đồ thị (thế giới b4 ẩn để không so giá trị với trần)
    const gA = ease(t, b.b0.has, b.b0.has + FADE) * (1 - ease(t, b.b1.blur, b.b1.blur + FADE));
    setOpacity(ghostBeam, 0.5 * gA);
    const drop = easeOut(t, b.b3.cap, b.b3.cap + 0.55), ext = easeOut(t, b.b3.flat, b.b3.flat + 0.8);   // rơi thấy được, khoá đúng tiếng trầm
    beam.position.set(0, mix(10.5, 5, drop), 0); beam.scale.x = 1;   // v3h: xà ĐỦ dài ngay khi rơi; khoá đúng tiếng trầm; "flat" = vệt sáng quét dọc xà
    const end11 = 1 - ease(t, M.wide.t0, M.wide.t1);
    setOpacity(beam, t >= b.b3.cap ? cw * off11 : 0);
    { const d = Math.hypot(pose.pos[0] - pose.tgt[0], pose.pos[1] - pose.tgt[1], pose.pos[2] - pose.tgt[2]), ppu = 540 / (d * Math.tan(pose.fov * Math.PI / 360));
      const k = clamp(9 / (0.07 * ppu), 1, 3); beam.userData.core.scale.set(1, k, k); }   // xà dày ~9 px ở mọi khung đồ thị (lượt đạo diễn v3c: "vạch xám mảnh")
    const overNow = riding && at(qRide) > 500000;
    let glow = 0; if (t >= b.b6.cross) glow = Math.max(1 - lin(t, b.b6.cross, b.b6.cross + 0.8), overNow ? 0.3 : 0); if (t >= b.b10.past) glow = Math.max(glow, (0.45 + 0.55 * flashCap) * ease(t, b.b10.past, b.b10.past + 0.25) * off11);
    beam.glow(glow);
    // nhịp sáng chạy dọc xà ("same in every quarter")
    // đường GIÁ TRỊ (b2) — vệt đỉnh chồng tiền; tắt ở b3
    if (t >= b.b2.quarter && !riding) {
      const pts = []; for (let q = 0; q <= Math.min(105, qDraw) + 1e-6; q += 0.25) pts.push([X(Math.min(q, qDraw)), valueAt(Math.min(q, qDraw)) / U]);
      vRib.set(pts, 0.12, C.accent); vRib.material.opacity = cw * (1 - valueOff);   // v3h: TẮT hẳn ở "cap" (đạo diễn v3g: đường mờ vẫn cắt trần ~2019 → đọc nhầm)
    } else vRib.material.opacity = 0;
    // đường LÃI (b5–b11) — vệt đỉnh chồng tiền khi phát lại; đoạn trên trần = warn
    if (riding) {
      const pts = []; let pg = null; const lift = t >= b.b11.t0 ? 200000 * r11 : 0;   // v3g CẦU NỐI lãi → giá: cả đường LÃI nâng lên đúng $200,000 (cái đã trả) thành đường GIÁ (xanh)
      for (let q = 0; q <= qRide + 1e-6; q += 0.25) { const qq = Math.min(q, qRide), g = at(qq);
        if (t >= b.b11.t0) { pts.push([X(qq), (Math.max(0, g) + lift) / U, r11 > 0.5 ? C.accent : g > 500000 ? C.warn : C.ink]); continue; }
        if (pg !== null && (pg - 500000) * (g - 500000) < 0) { const xq = qq - 0.25 * (g - 500000) / (g - pg); pts.push([X(xq), 5, pg > 500000 ? C.warn : C.ink], [X(xq) + 1e-4, 5, g > 500000 ? C.warn : C.ink]); }
        pts.push([X(qq), Math.max(0, g) / U, g > 500000 ? C.warn : C.ink]); pg = g; }
      const v3 = new THREE.Vector3(), ys = pts.map((p) => { v3.set(p[0], p[1], 0.45).project(cam); return (1 - v3.y) * 540; }); let cut0 = 0; for (let i = 0; i < ys.length; i++) if (ys[i] > 840) cut0 = i + 1; const vis = pts.slice(Math.min(cut0, Math.max(0, pts.length - 2)));   // bỏ phần ĐẦU đường nằm dưới dải chân trang (không nối tắt qua khoảng trống)
      const ab = t >= b.b8.above ? 1 - lin(t, b.b8.above, b.b8.above + 0.7) : 0;     // "has stayed above": đường phình sáng
      gRib.set(vis, (CAM.poseAt(t).pos[2] < 30 ? 0.06 : 0.12) * (1 + 0.9 * ab)); gRib.material.opacity = cw;
    } else gRib.material.opacity = 0;
    // cảnh minh hoạ b4
    // cùng một thế giới: cảnh minh hoạ không mờ ra/vào — máy quay đi tới nó; lúc đổi về đồ thị, NHÀ + phần lãi tua về 2000 (lãi 0)
    const grow = easeOut(t, b.b4.grow, b.b4.grow + 0.9), slide = easeOut(t, b.b4.less, b.b4.less + 1.6);
    const vTop = mix(mix(200000, valueAt(105), grow), 200000, rb), gainH = (vTop - 200000) / U;
    const slabTint = ease(t, b.b4.two, b.b4.two + POP);
    demo.position.set(mix(14, X(0), rb), 0, mix(6, 0, rb));
    const ds = mix(1, 0.55, rb); dTop.scale.set(ds, 1, ds); dHouse.scale.setScalar(ds);
    dSlab.set({ usd: 200000, tintBelowUsd: 200000, tintA: slabTint }); dSlab.position.set(1.6 * slide, 0, 0.9 * slide);   // khối "what they paid" trượt ra phía PHẢI (bên trái là người + nhãn lãi)
    dTop.set({ usd: vTop, fromUsd: 200000 }); dTop.position.y = mix(2, 0, slide);
    dHouse.position.y = dTop.position.y + gainH;
    const dGone = t >= ride0 ? 0 : 1, dSide = (1 - ease(t, M.backChart.t0, M.backChart.t0 + 0.5)) * dGone;
    const dChart = t >= M.backChart.t0 ? 1 : 1 - cw;               // ở chế độ đồ thị (trước khi tua) cảnh minh hoạ không lấn vào khung
    for (const o of [dHouse, dTop]) setOpacity(o, dGone * dChart);
    for (const o of [dSlab, dRosa, dFrank]) setOpacity(o, dSide * dChart);
    // b11: chồng giá 2000 = cái họ trả (teal), mọc cùng lúc khối teal về đáy chồng 2026
    const a11 = ease(t, M.wide.t0, M.wide.t1);
    const h0 = s2000.set({ usd: 200000 * r11, tintBelowUsd: 200000 * r11 + 1, tintA: 1 });
    h2000.position.set(X(0) + 0.75, Math.max(0, h0 - h2000.userData.height * 0.55 - 0.05), 0);   // cạnh chồng, mái không vượt đỉnh (tỉ lệ ×1 : ×3,8 đọc bằng CHỒNG)
    for (const o of [s2000, h2000]) setOpacity(o, a11);
    // loé ở điểm cắt
    const fl = t >= b.b6.cross ? 1 - lin(t, b.b6.cross, b.b6.cross + 0.7) : 0;
    if (flashCap > 0) { burst.position.set(X(105), 5, 0.6); burst.scale.setScalar(0.3 + 1.2 * (1 - flashCap)); burst.material.opacity = flashCap * 0.8; }
    else { burst.position.set(X(S.crossQ), 5, 0.6); burst.scale.setScalar(0.5 + 2.5 * (1 - fl)); burst.material.opacity = fl; }
    // nhịp âm dữ liệu ↔ đỉnh chồng loé nhẹ
    const pu = pulseAt(t); hero.children[0].material.emissive = new THREE.Color(overNow ? C.warn : '#000000'); hero.children[0].material.emissiveIntensity = 0.25 * pu;

    renderer.render(scene, cam);
    // =============================== lớp phủ 2D (chữ sắc; số/so sánh chỉ khi chartW ≥ 0,95)
    const log = O.begin(t, cw, cam); log.roi = {};
    { const [ax0, ay0] = O.toScreen(-9.7, 5, 0), [ax1] = O.toScreen(9.7, 5, 0); log.roi['b3.flat'] = [Math.max(0, ax0), ay0 - 40, Math.min(1920, ax1), ay0 + 40]; }
    { const h0 = hood.userData.items[0].home, [px, py] = O.toScreen(h0.x, h0.y + 0.4, h0.z); log.roi['b1.pop0'] = [px - 80, py - 90, px + 80, py + 60]; }   // nhà đầu tiên bật SOLD
    const S2 = (x, y) => O.toScreen(x, y, 0.5);
    // trục năm (đồ thị)
    if (cw > 0.02) {
      const ctx = O.ctx; const aA = cw * (1 - 0.6 * (1 - out11));
      for (let yr = 2000; yr <= 2025; yr += 5) { const [sx, sy] = S2(X((yr - 2000) * 4), 0); const e11 = (yr === 2000 || yr === 2025) ? 1 - ease(t, M.wide.t0, M.wide.t1) : 1; if (sx > 60 && sx < 1860) O.text(String(yr), sx, sy + 50, 48, { kind: 'number', w: 600, color: C.muted, align: 'center', alpha: aA * e11 * (cw > 0.95 ? 1 : 0) }); }
      const [a0x, a0y] = S2(X(0), 0), [a1x] = S2(X(105), 0); ctx.save(); ctx.globalAlpha = aA; ctx.strokeStyle = C.grid; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(a0x - 20, a0y); ctx.lineTo(a1x + 20, a0y); ctx.stroke(); ctx.restore();
    }
    const ok = cw >= 0.95 ? 1 : 0;
    // b0: dấu hỏi
    const qA = ease(t, b.b0.q - 0.05, b.b0.q + 0.15) * (1 - ease(t, b.b1.blur, b.b1.blur + FADE));
    if (qA > 0) { const [sx, sy] = O.toScreen(X(0), 3.9, 0); O.text('?', sx, sy, 130, { color: C.warn, align: 'center', alpha: qA }); }
    const nmA = ease(t, 0.3, 0.9) * (1 - ease(t, b.b1.blur - 0.1, b.b1.blur + FADE));
    if (nmA > 0) { const [sx, sy] = O.toScreen(X(0) - 1.35, 0, 0.6); O.text('Rosa & Frank · Phoenix', sx, sy + 70, 52, { align: 'center', alpha: nmA, plate: '#0B0E13', plateA: 0.6 }); }
    // b1: "let its value rise" — mũi tên giá đi lên cạnh nhà mờ (không số)
    const upA = easeOut(t, b.b1.rise - 0.05, b.b1.rise + 0.15) * (1 - ease(t, b.b1.avg, b.b1.avg + FADE));
    { const [rx0, ry0] = O.toScreen(X(0) + 1.3, 2.4, 0); log.roi['b1.rise'] = [rx0 - 60, ry0 - 160, rx0 + 60, ry0 + 80]; }
    const upArrow = (ux, uy0, a, k = 1) => { const c = O.ctx; c.save(); c.globalAlpha = a; c.fillStyle = C.accent;
      c.beginPath(); c.moveTo(ux, uy0 - 60 * k); c.lineTo(ux - 32 * k, uy0 - 14 * k); c.lineTo(ux + 32 * k, uy0 - 14 * k); c.closePath(); c.fill(); c.fillRect(ux - 11 * k, uy0 - 16 * k, 22 * k, 70 * k); c.restore(); };
    if (upA > 0) { const [ux, uy0] = O.toScreen(X(0) + 1.3, 2.4 + 0.8 * easeOut(t, b.b1.rise, b.b1.rise + 1.2), 0); upArrow(ux, uy0, upA); }
    // b9 "if their home ROSE like the Phoenix average": cùng mũi tên của b1, cạnh nhà ở đầu đường (từ vựng hình lặp lại = cùng ý)
    { const [ax, ay] = O.toScreen(hx + hOff + 0.6, sh - 0.2, 0); log.roi['b9.rose'] = [ax - 70, ay - 170, ax + 70, ay + 90];
      const a9 = easeOut(t, b.b9.rose - 0.05, b.b9.rose + 0.15) * (1 - ease(t, b.b9.fly - 0.3, b.b9.fly)) * ok;
      if (a9 > 0) { const [, ay2] = O.toScreen(hx + hOff + 0.6, sh - 0.2 + 0.25 * easeOut(t, b.b9.rose, b.b9.rose + 0.9), 0); upArrow(ax, ay2, a9, 0.9); } }
    // b1: "many sales → one average" (chữ tên, không số)
    const mA = ease(t, b.b1.many - 0.1, b.b1.many + 0.3) * (1 - ease(t, b.b1.avg + 0.3, b.b1.avg + 0.8));
    if (mA > 0) O.text('many sales → one average', 960, 860, 56, { align: 'center', alpha: mA, plate: '#0B0E13', plateA: 0.6 });
    // b2: năm ở đầu đường
    if (t >= b.b2.quarter && t < b.b3.cap + FADE && !riding) {
      const q = Math.min(105, qDraw), [sx, sy] = S2(X(q) - 0.55, valueAt(q) / U);
      O.text(q >= 104.9 ? CL('sale_quarter') : String(Math.floor(qYear(q))), sx, sy, 60, { kind: 'number', color: C.accent, align: 'right', alpha: ok * (1 - valueOff) * ease(t, b.b2.y2000 + 0.1, b.b2.y2000 + 0.35) });
      const [lx, ly] = S2(X(Math.max(0, q - 30)), valueAt(Math.max(0, q - 30)) / U);
      O.text('home value', lx, ly - 40, 52, { color: C.accent, align: 'center', alpha: ease(t, b.b2.y2000, b.b2.y2000 + 0.4) * (1 - valueOff) * ok });
    }
    // b2: "quarter by quarter" — ba quý đầu, mỗi bước một nhãn (đồ thị chính diện)
    if (t >= b.b2.quarter - 0.05 && t < b.b2.y2000 + 0.3) {
      const k = Math.min(2, Math.floor((t - b.b2.quarter + 0.05) / ((S.draw[2][0] - S.draw[0][0]) / 2))), [sx, sy] = S2(X(k), valueAt(k) / U);
      O.text(`${CL('buy_year')} Q${k + 1}`, sx, sy - 120, 60, { kind: 'number', color: C.accent, align: 'center', alpha: ok * (1 - ease(t, b.b2.y2000, b.b2.y2000 + 0.3)) });
    }
    // b3: nhãn trần + nhịp chạy dọc
    if (t >= b.b3.cap) {
      // nhãn GẮN vào xà (toạ độ thế giới, trôi theo máy): bản trái ở 2000 (khung toàn cảnh), bản phải ở 2019 (khung phóng) — không nhảy
      const la = ease(t, b.b3.five, b.b3.five + POP) * ok * off11, capS = `${CL('excl_joint_limit_usd')} cap`;
      const [lx, ly] = S2(X(0), 5); O.text(capS, lx, ly - 26, 56, { kind: 'number', color: C.ink, alpha: la * clamp((lx - 70) / 120) * (1 - ease(t, M.zoom.t0, M.zoom.t0 + 0.5)) });
      const [zx, zy] = S2(X(76), 5); O.text(capS, zx, zy + 76, 56, { kind: 'number', color: C.ink, alpha: la * ease(t, M.zoom.t1 - 0.2, M.zoom.t1 + POP) * (1 - ease(t, M.tip.t0, M.tip.t0 + 0.4)) * clamp((zx - 70) / 120) });
      // khung đầu nhà (b9–b10): trần vẫn có TÊN + SỐ ngay trên xà, chỗ đường lãi đã ở hẳn phía trên (2024–2025) — "past the cap" đọc được là "qua $500,000"
      const [tx_, ty_] = S2(X(96), 5); O.text(capS, tx_, ty_ - 22, 48, { kind: 'number', color: C.ink, alpha: la * ease(t, M.tip.t0, M.tip.t0 + 0.4) });   // tên xà không đứt trong cú đẩy
      // "the same in every quarter": cột mốc cao BẰNG NHAU ở mỗi năm, sáng lần lượt theo nhịp chạy dọc xà
      const fw = lin(t, b.b3.flat, b.b3.flat + 0.6);   // "a flat line": vệt sáng quét dọc xà
      if (fw > 0 && fw < 1) { const [fx, fy] = S2(mix(X(0) - 0.6, X(105) + 0.6, fw), 5); O.ctx.fillStyle = rgba(C.ink, 0.85 * ok); O.ctx.fillRect(fx - 90, fy - 7, 180, 14); }
      const sw = lin(t, b.b3.same, b.b3.same + 1.4), postA = (1 - ease(t, M.toDemo.t0, M.toDemo.t0 + 0.4)) * ok;
      if (t >= b.b3.same && postA > 0) for (let yr = 0; yr <= 26; yr++) { const q = Math.min(105, yr * 4), [px0, py0] = S2(X(q), 0), [, py1] = S2(X(q), 5), on = lin(sw, yr / 27, yr / 27 + 0.04);
        if (on > 0) { O.ctx.save(); O.ctx.globalAlpha = postA * on * (0.35 + 0.5 * (1 - lin(sw, yr / 27, yr / 27 + 0.25))); O.ctx.strokeStyle = C.ink; O.ctx.lineWidth = 4; O.ctx.beginPath(); O.ctx.moveTo(px0, py0); O.ctx.lineTo(px0, py1); O.ctx.stroke(); O.ctx.restore(); } }
      if (sw > 0 && sw < 1) { const [sx, sy] = S2(mix(X(0), X(105), sw), 5); O.ctx.fillStyle = rgba(C.ink, 0.9 * ok); O.ctx.fillRect(sx - 60, sy - 13, 120, 26); }
    }
    // b4 (thế giới): không số; nhãn tên
    const dV = ease(t, M.toDemo.t0 + 0.3, M.toDemo.t1) * (1 - ease(t, M.backChart.t0, M.backChart.t0 + 0.5));   // nhãn cảnh minh hoạ chỉ khi máy quay đang nhìn nó
    if (dV > 0.05) { const dA = dV;
      O.ctx.font = '700 52px Inter'; const rw = O.ctx.measureText('Rosa & Frank').width;
      const [rx, ry] = O.toScreen(10.7, 1.4, 6.8); O.text('Rosa & Frank', Math.max(rx, 110 + rw / 2), ry, 52, { align: 'center', alpha: dA, plate: '#0B0E13', plateA: 0.6 });   // trên đầu họ
      // phần lãi: "= ?" tới chữ "paid", rồi NGOẶC đo đúng khối còn lại + nhãn (đáp án thấy được, không chỉ mất hai ký tự)
      // nhãn lãi ở BÊN TRÁI chồng (phía người), trên đầu họ; khối "what they paid" trượt sang phải
      const yTop0 = dTop.position.y, [gx, gy] = O.toScreen(13.35, yTop0 + Math.max(1.1, gainH * 0.5), 6.35), pA = ease(t, b.b4.paid, b.b4.paid + POP);
      O.text(t < b.b4.paid ? 'their gain on paper = ?' : 'their gain on paper', gx - 30 - 40 * pA, gy + 18, 52, { color: C.ink, align: 'right', alpha: dA * ease(t, b.b4.gain, b.b4.gain + POP), plate: '#0B0E13', plateA: 0.6 });
      if (pA > 0) { const [bx, by0] = O.toScreen(13.38, yTop0, 6.35), [, by1] = O.toScreen(13.38, yTop0 + gainH, 6.35); O.bracket(bx - 10, by0, by1, C.ink, pA * dA, -18, 5); }
      const [sx2, sy2] = O.toScreen(14.6 + 1.6 * slide, 1.0, 6.35 + 0.9 * slide);
      O.text('what they paid', sx2 + 20, sy2 + 18, 52, { color: C.cushion, alpha: dA * slabTint, plate: '#0B0E13', plateA: 0.6 });
    }
    // tên đường LÃI khi phát lại (cổng gốc: tránh đọc thành "giá nhà")
    if (riding) {
      const nA = ease(t, S.ride[0][0], S.ride[0][0] + POP) * (1 - ease(t, M.zoom.t0, M.zoom.t0 + 0.3)) * ok;
      const zA = ease(t, M.zoom.t1 - 0.2, M.zoom.t1 + POP) * (1 - ease(t, b.b9.fly - 0.4, b.b9.fly)) * ok;   // khung phóng: tiêu đề đường
      O.text('their gain on paper, 2021 → 2026', 960, 230, 52, { color: C.ink, align: 'center', alpha: zA });
      // đối trọng đứng suốt phần phát lại (bản phát hành G2: chặn câu khuyên "chờ/canh thời điểm bán")
      const mA = ease(t, S.ride[0][0], S.ride[0][0] + POP) * (1 - ease(t, b.b9.fly - 0.4, b.b9.fly)) * ok;   // → dòng chú đáy nhận lời đối trọng từ "this" (liên tục, không đổi giữa khoảnh khắc lặng)
      // v3e: lời đối trọng chuyển xuống dòng chú đáy (bớt một mảng chữ giữa khung)
      const qn = Math.max(0, qRide - 10), [nx, ny] = S2(X(qn), Math.max(0, at(qn)) / U);
      const [hdx, hdy] = S2(X(qRide), Math.max(0, at(qRide)) / U);   // tên đường đi PHÍA TRƯỚC đầu đường (vùng chưa vẽ), dưới ngoặc "well under"
      O.text('their gain on paper', hdx + 100, Math.min(760, hdy + 60), 52, { color: C.ink, alpha: nA, plate: '#0B0E13', plateA: 0.7 });
    }
    // b5: ngoặc "well under"
    const brA = ease(t, b.b5.under, b.b5.under + POP) * (1 - ease(t, b.b6.t0, b.b6.t0 + FADE)) * ok;
    if (brA > 0) { const [x0, y0] = S2(X(qRide) - 0.45, 5), [, y1] = S2(0, Math.max(0, at(qRide)) / U); O.bracket(x0, y0, y1, C.cushion, brA, 18); O.text('well under', x0 - 16, (y0 + y1) / 2 + 18, 52, { kind: 'compare', color: C.cushion, align: 'right', alpha: brA }); }
    // b6–b8: ba mốc, giữ tới khi số bay (trạng thái kết luận)
    const keep = 1 - ease(t, b.b9.fly - 0.4, b.b9.fly), keepOB = keep * (1 - ease(t, M.tip.t0, M.tip.t0 + 0.4));   // hai nhãn lịch sử rời trước khi đẩy máy (không bị cắt mép)
    const mark = (q, s, a, dx, dy, align) => { if (a <= 0) return; const [sx, sy] = S2(X(q), at(q) / U); O.ctx.fillStyle = rgba(C.warn, a); O.ctx.beginPath(); O.ctx.arc(sx, sy, 11, 0, 7); O.ctx.fill(); O.text(s, sx + dx, sy + dy, 52, { kind: 'number', color: '#1B1F26', plate: C.warn, plateA: 0.95, align, alpha: a }); };
    if (t >= b.b6.cross - 0.05) mark(S.crossQ, `Over: ${CL('cross_quarter_at_200k_phoenix')}`, ease(t, b.b6.cross, b.b6.cross + POP) * keepOB * ok, -40, -60, 'right');
    if (t >= b.b7.slips - 0.05) { const [, yy] = S2(X(91.6), at(91.6) / U); mark(91.6, 'Back under', ease(t, b.b7.slips, b.b7.slips + POP) * keepOB * ok, -40, Math.min(120, 820 - yy), 'right'); }
    if (t >= b.b8.lbl - 0.05) mark(93, `Stayed over since ${CL('stay_quarter_at_200k_phoenix')}`,   // cả nhãn hiện lúc NÓI NGÀY (vòng mù 14: tách hai bước → K1 hụt "stayed above")
      ease(t, b.b8.lbl, b.b8.lbl + POP) * keep * ok, 40, -150, 'left');
    // b9: số bay từ đỉnh chồng lên biển trên mái
    if (t >= b.b9.fly) {
      const [tx, ty] = S2(hx, Math.max(0, at(qRide)) / U), [rx, ry] = O.toScreen(hx + 0.3, 6.15, 0);   // v3h: số bay từ đầu đường LÊN thành bảng trên đỉnh chồng   // v3f: số BAY rõ (từ đỉnh chồng lên cao trên mái)
      const f = ease(t, b.b9.fly, b.b9.land), o = 1 - ease(t, b.b11.t0, b.b11.t0 + FADE);
      O.text(CL('gain_at_200k_phoenix'), mix(tx + 60, rx, f), mix(ty, ry, f), mix(60, 80, f), { kind: 'number', color: '#1B1F26', plate: '#E9E3D3', plateA: 0.95, align: 'center', alpha: o * ok * ease(t, b.b9.fly, b.b9.fly + POP) });
      O.text('their gain on paper', rx - 300, ry + 16, 48, { color: C.ink, align: 'right', alpha: ease(t, b.b9.land, b.b9.land + POP) * o * ok * gone11 });
    }
    // b10: ngoặc "past the cap"
    if (t >= b.b10.past - 0.05) {
      const a = ease(t, b.b10.past, b.b10.past + POP) * (1 - ease(t, b.b11.t0, b.b11.t0 + FADE)) * ok;
      const [x0, y0] = S2(X(105) + hOff + 0.55, 5), [, y1f] = S2(0, at(105) / U), y1 = mix(y0, y1f, easeOut(t, b.b10.past, S.marks.hop_land));   // ngoặc MỌC từ xà lên đỉnh, chạm đỉnh đúng tiếng chạm sau "cap"
      O.bracket(x0, y0, y1, C.warn, a, 18, 6 + 4 * flashCap); O.text('past the cap', x0 + 50, (y0 + y1f) / 2 + 22, 60, { kind: 'compare', color: C.warn, alpha: a, plate: '#0B0E13', plateA: 0.75 });   // bên PHẢI chồng: không đè lên đường lãi
    }
    // b11: ×3,8 + tiêu đề
    if (t >= M.wide.t0 + 0.3) {
      const a = ease(t, M.wide.t0 + 0.3, M.wide.t0 + 0.6) * ok;   // tiêu đề GIÁ thay tên đại lượng đúng lúc lời nói "Phoenix area prices"
      O.text('Phoenix-area prices since 2000', 960, 230, 60, { align: 'center', alpha: a });
      const ax = ease(t, b.b11.x, b.b11.x + POP) * ok;                 // ×3,8 = chiều cao 2026 ÷ chiều cao 2000, cả hai đo từ mặt đất
      const [x0, y0] = S2(X(105) - 0.75, 0), [, y1] = S2(0, valueAt(105) / U); O.bracket(x0, y0, y1, C.accent, ax, -18);
      O.text(CL('growth_phoenix'), x0 - 40, (y0 + y1) / 2 + 30, 96, { kind: 'compare', color: C.accent, align: 'right', alpha: ax });
      const [z0x, z0y] = S2(X(0) - 0.75, 0), [, z1y] = S2(0, 2); O.bracket(z0x, z0y, z1y, C.accent, ax, -18);
      O.text('×1', z0x - 30, (z0y + z1y) / 2 + 30, 84, { kind: 'compare', color: C.accent, align: 'right', alpha: ax });
      const [ex, ey] = S2(X(0), 0), [fx] = S2(X(105), 0);
      O.text(String(CL('buy_year')), ex, ey + 48, 44, { kind: 'number', color: C.ink, align: 'center', alpha: a });
      O.text(CL('sale_quarter'), fx, ey + 48, 44, { kind: 'number', color: C.ink, align: 'center', alpha: a });
    }
    // lớp bắt buộc (quy tắc 5)
    O.chrome({ illus: true, src: t >= b.b1.src ? 'Source: FHFA via FRED' : null, srcA: ease(t, b.b1.src, b.b1.src + POP),
      hist: t >= b.b1.avg, histA: ease(t, b.b1.avg, b.b1.avg + POP),
      cw: t >= b.b9.fly ? 'A measurement, not a tax bill or a next step' : riding ? 'A measurement, not a next step' : t >= S.marks.cw_home ? 'A home that rose like the Phoenix average' : null,
      cwA: t >= b.b9.fly ? ease(t, b.b9.fly, b.b9.fly + POP) : riding ? ease(t, S.ride[0][0], S.ride[0][0] + POP) : ease(t, S.marks.cw_home, S.marks.cw_home + POP) });
    st.compose();
    log.camMoving = CAM.moving(t);
    return log;
  }
  return { canvas: st.out, frame };
}
