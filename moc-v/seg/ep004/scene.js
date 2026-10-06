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
  const dataEv = S.events.filter((e) => e.kind === 'data'), pops = S.events.filter((e) => e.kind === 'tick' && e.pop !== undefined).map((e) => e.t);

  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor } = Studio(scene);
  // ---- tư thế máy quay (hình học); chart = 1 → chế độ đồ thị chính diện (tele gần trực giao)
  const poses = {
    wHome: { pos: [-6.0, 3.4, 10.5], tgt: [-9, 2.7, 0], fov: 35, chart: 0 },
    wHood: { pos: [-6.4, 3.4, 12.0], tgt: [-8.6, 1.8, -1.6], fov: 35, chart: 0 },
    cFull: { pos: [0, 3.9, 64.2], tgt: [0, 3.9, 0], fov: 12, chart: 1 },
    wDemo: { pos: [15.6, 5.4, 26.0], tgt: [13.6, 4.3, 6], fov: 35, chart: 0 },
    wDemoNear: { pos: [15.2, 2.9, 15.0], tgt: [13.4, 2.0, 6], fov: 35, chart: 0 },
    cZoom: { pos: [7.0, 5.4, 20.9], tgt: [7.0, 5.4, 0], fov: 12, chart: 1 },
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
  demo.add(dHouse, dTop, dSlab, dRosa, dFrank); dRosa.position.set(-2.9, 0, 0.7); dFrank.position.set(-2.35, 0, 0.9); dRosa.rotation.y = dFrank.rotation.y = 0.5;
  // b11: hai chồng GIÁ TRỊ ở 2000 và 2026 Q2
  const s2000 = Stack({ unitUsd: U, w: 0.9, d: 0.6 }), s2026 = Stack({ unitUsd: U, w: 0.9, d: 0.6 }); s2000.position.set(X(0), 0, 0); s2026.position.set(X(105), 0, 0); scene.add(s2000, s2026);
  const h2000 = House({ w: 1.0 }), h2026 = House({ w: 1.0 }); scene.add(h2000, h2026);
  const burst = Burst(); scene.add(burst); const spark = Burst({ color: C.ink }); scene.add(spark);
  const ghostBeam = Beam({ length: 5 }); ghostBeam.position.set(X(0), 5, 0); scene.add(ghostBeam);

  // ---- âm ↔ hình: nhịp sáng ở mỗi nốt dữ liệu
  const pulseAt = (t) => { let p = 0; for (const e of dataEv) if (t >= e.t && t < e.t + 0.18) p = Math.max(p, 1 - (t - e.t) / 0.18); return p; };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    const b = cue;
    // thế giới mờ đi ở chế độ đồ thị
    floor.material.opacity = 1 - 0.85 * cw;
    // ---------------- giai đoạn
    const qDraw = interp(S.draw, t), riding = t >= S.ride[0][0], qRide = riding ? interp(S.ride, t) : 0;
    const inDemo = t >= M.toDemo.t0 && t < M.backChart.t1;
    const valueOff = ease(t, b.b3.cap, b.b3.cap + FADE);          // b3: giá trị + nhà tắt khi trần vào
    // nhà chính
    let heroA = 1, hx = X(0), usd = 200000, hScale = 1;
    if (t < b.b2.quarter) { hx = X(0); usd = 200000; }
    else if (!riding) { hx = X(qDraw); usd = valueAt(qDraw); heroA = 1 - valueOff; }
    else { hx = X(qRide); usd = Math.max(0, at(qRide)); heroA = ease(t, S.ride[0][0] - 0.6, S.ride[0][0]); }
    if (inDemo && !riding) heroA = 0;
    hScale = mix(1, 0.55, cw);
    const bump = t >= b.b10.past ? Math.sin(Math.PI * lin(t, b.b10.past, b.b10.past + 0.35)) * 0.35 : 0;
    const out11 = 1 - 0.75 * ease(t, M.wide.t0, M.wide.t1);           // b11: lãi lùi về nền
    const gone11 = 1 - ease(t, M.wide.t0, M.wide.t1);                  // b11: nhà lãi + người rời cảnh (nhường hai chồng giá trị)
    heroStack.scale.set(hScale, 1, hScale);
    const sh = heroStack.set({ usd, warnAboveUsd: riding ? 500000 : Infinity });
    hero.scale.setScalar(hScale); hero.position.y = sh + bump;
    heroG.position.set(hx, 0, 0);
    // khu phố (b1) bật biển đúng tick, gom về nhà chính lúc "sales"
    const gather = ease(t, b.b1.avg - 0.1, b.b1.avg + 0.9);
    hood.userData.items.forEach((it, k) => {
      const ap = easeOut(t, pops[k] - 0.03, pops[k] + 0.12) * (1 + 0.25 * Math.sin(Math.PI * lin(t, pops[k], pops[k] + 0.3))), g = gather;
      it.it.position.lerpVectors(it.home, new THREE.Vector3(X(0), 1.8, 0), g); it.it.position.y += Math.sin(Math.PI * g) * 1.6; it.it.scale.setScalar(Math.max(0.001, ap * (1 - 0.7 * g)));
      it.sign.visible = t >= pops[k];
      setOpacity(it.it, (1 - ease(g, 0.82, 1)) * (1 - cw));
    });
    // sương "can't see their house" (b1) → nhà mờ
    const fog = ease(t, b.b1.blur, b.b1.blur + FADE) * (1 - ease(t, b.b1.avg, b.b1.avg + 0.8));
    setOpacity(hero, heroA * (1 - 0.7 * fog) * gone11); setOpacity(heroStack, heroA * gone11);
    // người (b0) và (b9–b10) cạnh nhà ở đầu đường
    const pA0 = 1 - ease(t, b.b1.blur - 0.1, b.b1.blur + FADE);
    const pA9 = ease(t, b.b9.t0, b.b9.t0 + 0.6) * gone11;
    const pA = Math.max(pA0, pA9);
    const on9 = pA9 > pA0, ps = on9 ? 0.5 : 1, px = on9 ? hx - 0.62 : X(0) - 1.6, py = on9 ? sh + 1.2 * (1 - easeOut(t, b.b9.t0, b.b9.t0 + 0.7)) : 0;
    rosa.position.set(px, py, 0.5); frank.position.set(px + (on9 ? -0.3 : 0.55), py, 0.7); rosa.scale.setScalar(ps); frank.scale.setScalar(ps);
    rosa.rotation.y = frank.rotation.y = 0.35; setOpacity(rosa, pA); setOpacity(frank, pA);
    // xà trần: bóng mờ b0; xà thật từ b3 (rơi + khoá); chỉ ở chế độ đồ thị (thế giới b4 ẩn để không so giá trị với trần)
    const gA = ease(t, b.b0.has, b.b0.has + FADE) * (1 - ease(t, b.b1.blur, b.b1.blur + FADE));
    setOpacity(ghostBeam, 0.5 * gA);
    const drop = easeOut(t, b.b3.cap, b.b3.cap + 0.5), ext = easeOut(t, b.b3.flat - 0.05, b.b3.flat + 0.8);
    beam.position.set(mix(X(0) + 1.9, 0, ext), mix(8.5, 5, drop), 0); beam.scale.x = mix(0.2, 1, ext);
    const end11 = 1 - ease(t, M.wide.t0, M.wide.t1);
    setOpacity(beam, t >= b.b3.cap ? cw * end11 : 0);
    const overNow = riding && at(qRide) > 500000;
    let glow = 0; if (t >= b.b6.cross) glow = Math.max(1 - lin(t, b.b6.cross, b.b6.cross + 0.8), overNow ? 0.3 : 0); if (t >= b.b10.past) glow = Math.max(glow, 0.6 * ease(t, b.b10.past, b.b10.past + 0.25) * out11);
    beam.glow(glow);
    // nhịp sáng chạy dọc xà ("same in every quarter")
    // đường GIÁ TRỊ (b2) — vệt đỉnh chồng tiền; tắt ở b3
    if (t >= b.b2.quarter && !riding) {
      const pts = []; for (let q = 0; q <= Math.min(105, qDraw) + 1e-6; q += 0.25) pts.push([X(Math.min(q, qDraw)), valueAt(Math.min(q, qDraw)) / U]);
      vRib.set(pts, 0.09, C.accent); vRib.material.opacity = cw * (1 - valueOff);
    } else vRib.material.opacity = 0;
    // đường LÃI (b5–b11) — vệt đỉnh chồng tiền khi phát lại; đoạn trên trần = warn
    if (riding) {
      const pts = []; let pg = null; for (let q = 0; q <= qRide + 1e-6; q += 0.25) { const qq = Math.min(q, qRide), g = at(qq);
        if (pg !== null && (pg - 500000) * (g - 500000) < 0) { const xq = qq - 0.25 * (g - 500000) / (g - pg); pts.push([X(xq), 5, pg > 500000 ? C.warn : C.ink], [X(xq) + 1e-4, 5, g > 500000 ? C.warn : C.ink]); }
        pts.push([X(qq), Math.max(0, g) / U, g > 500000 ? C.warn : C.ink]); pg = g; }
      gRib.set(pts, cam.fov < 20 && CAM.poseAt(t).pos[2] < 30 ? 0.06 : 0.09); gRib.material.opacity = cw * out11;
    } else gRib.material.opacity = 0;
    // cảnh minh hoạ b4
    const dA = 1;   // cùng một thế giới: cảnh minh hoạ không mờ ra/vào — máy quay đi tới nó
    const grow = easeOut(t, b.b4.grow, b.b4.grow + 0.9), slide = easeOut(t, b.b4.less, b.b4.less + 1.6);
    const vTop = mix(200000, valueAt(105), grow);
    const slabTint = ease(t, b.b4.two - 0.05, b.b4.two + POP);
    dSlab.set({ usd: 200000, tintBelowUsd: 200000, tintA: slabTint }); dSlab.position.set(-1.5 * slide, 0, 0.9 * slide);
    dTop.set({ usd: vTop, fromUsd: 200000 }); dTop.position.y = mix(2, 0, slide);
    dHouse.position.y = dTop.position.y + (vTop - 200000) / U;
    for (const o of [dHouse, dTop, dSlab, dRosa, dFrank]) setOpacity(o, dA);
    // b11: hai chồng giá trị
    const r11 = ease(t, M.wide.t0, b.b11.x);
    const a11 = ease(t, M.wide.t0, M.wide.t1);
    const h0 = s2000.set({ usd: 200000 * Math.min(1, r11 * 3) }), h1 = s2026.set({ usd: mix(0, valueAt(105), r11) });
    h2000.position.set(X(0), h0, 0); h2026.position.set(X(105), h1, 0); h2000.scale.setScalar(0.55); h2026.scale.setScalar(0.55);
    for (const o of [s2000, s2026, h2000, h2026]) setOpacity(o, a11);
    // b9 "rose like the Phoenix average": một đốm sáng chạy dọc đường lãi 2000 → 2026
    const sw9 = lin(t, b.b9.rose, b.b9.fly - 0.25);
    if (sw9 > 0 && sw9 < 1) { const qs = 86 + 19 * sw9; spark.position.set(X(qs), Math.max(0, at(qs)) / U, 0.7); spark.material.opacity = 1; spark.scale.setScalar(1.3); } else spark.material.opacity = 0;   // phần đường thấy được trong khung phóng (2021 → 2026)
    // loé ở điểm cắt
    const fl = t >= b.b6.cross ? 1 - lin(t, b.b6.cross, b.b6.cross + 0.7) : 0;
    burst.position.set(X(S.crossQ), 5, 0.6); burst.scale.setScalar(0.5 + 2.5 * (1 - fl)); burst.material.opacity = fl;
    // nhịp âm dữ liệu ↔ đỉnh chồng loé nhẹ
    const pu = pulseAt(t); hero.children[0].material.emissive = new THREE.Color(overNow ? C.warn : '#000000'); hero.children[0].material.emissiveIntensity = 0.25 * pu;

    renderer.render(scene, cam);
    // =============================== lớp phủ 2D (chữ sắc; số/so sánh chỉ khi chartW ≥ 0,95)
    const log = O.begin(t, cw, cam); log.roi = {};
    { const [ax0, ay0] = O.toScreen(-9.7, 5, 0), [ax1] = O.toScreen(9.7, 5, 0); log.roi['b3.flat'] = [Math.max(0, ax0), ay0 - 40, Math.min(1920, ax1), ay0 + 40]; }
    { const [sx9, sy9] = O.toScreen(X(86), at(86) / U, 0.7); log.roi['b9.rose'] = [sx9 - 90, sy9 - 90, sx9 + 90, sy9 + 90]; }
    const S2 = (x, y) => O.toScreen(x, y, 0.5);
    // trục năm (đồ thị)
    if (cw > 0.02) {
      const ctx = O.ctx; const aA = cw * (1 - 0.6 * (1 - out11));
      for (let yr = 2000; yr <= 2025; yr += 5) { const [sx, sy] = S2(X((yr - 2000) * 4), 0); const e11 = (yr === 2000 || yr === 2025) ? 1 - ease(t, M.wide.t0, M.wide.t1) : 1; if (sx > 60 && sx < 1860) O.text(String(yr), sx, sy + 48, 44, { kind: 'number', w: 600, color: C.muted, align: 'center', alpha: aA * e11 * (cw > 0.95 ? 1 : 0) }); }
      const [a0x, a0y] = S2(X(0), 0), [a1x] = S2(X(105), 0); ctx.save(); ctx.globalAlpha = aA; ctx.strokeStyle = C.grid; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(a0x - 20, a0y); ctx.lineTo(a1x + 20, a0y); ctx.stroke(); ctx.restore();
    }
    const ok = cw >= 0.95 ? 1 : 0;
    // b0: dấu hỏi
    const qA = ease(t, b.b0.q - 0.2, b.b0.q + 0.1) * (1 - ease(t, b.b1.blur, b.b1.blur + FADE));
    if (qA > 0) { const [sx, sy] = O.toScreen(X(0), 3.9, 0); O.text('?', sx, sy, 130, { color: C.warn, align: 'center', alpha: qA }); }
    const nmA = ease(t, 0.3, 0.9) * (1 - ease(t, b.b1.blur - 0.1, b.b1.blur + FADE));
    if (nmA > 0) { const [sx, sy] = O.toScreen(X(0) - 1.35, 0, 0.6); O.text('Rosa & Frank · Phoenix', sx, sy + 70, 52, { align: 'center', alpha: nmA, plate: '#0B0E13', plateA: 0.6 }); }
    // b1: "let its value rise" — mũi tên giá đi lên cạnh nhà mờ (không số)
    const upA = easeOut(t, b.b1.rise - 0.05, b.b1.rise + 0.15) * (1 - ease(t, b.b1.avg, b.b1.avg + FADE));
    { const [rx0, ry0] = O.toScreen(X(0) + 1.3, 2.4, 0); log.roi['b1.rise'] = [rx0 - 60, ry0 - 160, rx0 + 60, ry0 + 80]; }
    if (upA > 0) { const [ux, uy0] = O.toScreen(X(0) + 1.3, 2.4 + 0.8 * easeOut(t, b.b1.rise, b.b1.rise + 1.2), 0); const c = O.ctx; c.save(); c.globalAlpha = upA; c.fillStyle = C.accent;
      c.beginPath(); c.moveTo(ux, uy0 - 60); c.lineTo(ux - 32, uy0 - 14); c.lineTo(ux + 32, uy0 - 14); c.closePath(); c.fill(); c.fillRect(ux - 11, uy0 - 16, 22, 70); c.restore(); }
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
      const [lx, ly] = S2(X(0), 5); const la = ease(t, b.b3.five - 0.05, b.b3.five + POP) * ok * out11;
      if (lx >= 110) O.text(`${CL('excl_joint_limit_usd')} cap`, lx, ly - 26, 56, { kind: 'number', color: C.ink, alpha: la });
      else O.text(`${CL('excl_joint_limit_usd')} cap`, 1824, ly + 76, 56, { kind: 'number', color: C.ink, align: 'right', alpha: la });
      const sw = lin(t, b.b3.same, b.b3.same + 1.4);
      if (sw > 0 && sw < 1) { const [sx, sy] = S2(mix(X(0), X(105), sw), 5); O.ctx.fillStyle = rgba(C.ink, 0.9 * ok); O.ctx.fillRect(sx - 40, sy - 9, 80, 18); }
    }
    // b4 (thế giới): không số; nhãn tên
    const dV = ease(t, M.toDemo.t0 + 0.3, M.toDemo.t1) * (1 - ease(t, M.backChart.t0, M.backChart.t0 + 0.5));   // nhãn cảnh minh hoạ chỉ khi máy quay đang nhìn nó
    if (dV > 0.05) { const dA = dV;
      const [rx, ry] = O.toScreen(11.1, 0.6, 6.8); O.text('Rosa & Frank', rx - 20, ry, 52, { align: 'right', alpha: dA, plate: '#0B0E13', plateA: 0.6 });
      const [gx, gy] = O.toScreen(14.9, 2 + (vTop - 200000) / U * 0.5, 6);
      O.text(t < b.b4.less + 1.6 ? 'their gain on paper = ?' : 'their gain on paper', gx + 40, gy, 52, { color: C.ink, alpha: dA * ease(t, b.b4.gain - 0.05, b.b4.gain + POP) * (1 - ease(t, b.b4.less + 1.6, b.b4.less + 2.0)) + dA * ease(t, b.b4.less + 1.6, b.b4.less + 2.0), plate: '#0B0E13', plateA: 0.6 });
      const [sx2, sy2] = slide < 0.02 ? O.toScreen(14.6, 1.0, 6.35) : O.toScreen(14 - 1.5 * slide, 2.3, 6.35 + 0.9 * slide);
      O.text('what they paid', sx2 + (slide < 0.02 ? 20 : 0), sy2 - 10, 52, { align: slide < 0.02 ? 'left' : 'center', color: C.cushion, alpha: dA * slabTint, plate: '#0B0E13', plateA: 0.6 });
    }
    // b5: ngoặc "well under"
    const brA = ease(t, b.b5.under - 0.05, b.b5.under + POP) * (1 - ease(t, b.b6.t0, b.b6.t0 + FADE)) * ok;
    if (brA > 0) { const [x0, y0] = S2(X(qRide) + 0.75, 5), [, y1] = S2(0, Math.max(0, at(qRide)) / U); O.bracket(x0, y0, y1, C.cushion, brA); O.text('well under', x0 + 34, (y0 + y1) / 2 + 18, 52, { kind: 'compare', color: C.cushion, alpha: brA }); }
    // b6–b8: ba mốc, giữ tới khi số bay (trạng thái kết luận)
    const keep = 1 - ease(t, b.b9.fly - 0.4, b.b9.fly);
    const mark = (q, s, a, dx, dy, align) => { if (a <= 0) return; const [sx, sy] = S2(X(q), at(q) / U); O.ctx.fillStyle = rgba(C.warn, a); O.ctx.beginPath(); O.ctx.arc(sx, sy, 11, 0, 7); O.ctx.fill(); O.text(s, sx + dx, sy + dy, 52, { kind: 'number', color: '#1B1F26', plate: C.warn, plateA: 0.95, align, alpha: a }); };
    if (t >= b.b6.cross - 0.05) mark(S.crossQ, `Over: ${CL('cross_quarter_at_200k_phoenix')}`, ease(t, b.b6.cross - 0.05, b.b6.cross + POP) * keep * ok, -40, -60, 'right');
    if (t >= b.b7.slips - 0.05) { const [, yy] = S2(X(91.6), at(91.6) / U); mark(91.6, 'Back under', ease(t, b.b7.slips - 0.05, b.b7.slips + POP) * keep * ok, -40, Math.min(120, 820 - yy), 'right'); }
    if (t >= b.b8.lbl - 0.05) mark(93, `Stayed over since ${CL('stay_quarter_at_200k_phoenix')}`, ease(t, b.b8.lbl - 0.05, b.b8.lbl + POP) * keep * ok, 40, -150, 'left');
    // b9: số bay từ đỉnh chồng lên biển trên mái
    if (t >= b.b9.fly - 0.05) {
      const [tx, ty] = S2(hx, Math.max(0, at(qRide)) / U), [rx, ry0] = O.toScreen(hx, sh + hero.userData.height * hScale + bump, 0), ry = ry0 - 46;
      const f = easeOut(t, b.b9.fly, b.b9.land), o = out11 > 0.5 ? 1 - ease(t, M.wide.t0, M.wide.t0 + FADE) : 0;
      O.text(CL('gain_at_200k_phoenix'), mix(tx + 60, rx, f), mix(ty, ry, f), mix(60, 92, f), { kind: 'number', color: '#1B1F26', plate: '#E9E3D3', plateA: 0.95, align: 'center', alpha: o * ok });
      O.text('their gain on paper', rx - 300, ry + 16, 48, { color: C.ink, align: 'right', alpha: ease(t, b.b9.land, b.b9.land + POP) * o * ok * gone11 });
    }
    // b10: ngoặc "past the cap"
    if (t >= b.b10.past - 0.05) {
      const a = ease(t, b.b10.past - 0.05, b.b10.past + POP) * (1 - ease(t, M.wide.t0, M.wide.t0 + FADE)) * ok;
      const [x0, y0] = S2(X(105) - 0.5, 5), [, y1] = S2(0, at(105) / U); O.bracket(x0, y0, y1, C.warn, a, -18); O.text('past the cap', x0 - 34, (y0 + y1) / 2 + 18, 52, { kind: 'compare', color: C.warn, align: 'right', alpha: a, plate: '#0B0E13', plateA: 0.75 });
    }
    // b11: ×3,8 + tiêu đề
    if (t >= M.wide.t1 - 0.1) {
      const a = ease(t, M.wide.t1 - 0.1, M.wide.t1 + POP) * ok;
      O.text('Phoenix-area prices since 2000', 960, 230, 60, { align: 'center', alpha: a });
      const ax = ease(t, b.b11.x - 0.05, b.b11.x + POP) * ok;                 // ×3,8 = chiều cao 2026 ÷ chiều cao 2000, cả hai đo từ mặt đất
      const [x0, y0] = S2(X(105) - 0.75, 0), [, y1] = S2(0, valueAt(105) / U); O.bracket(x0, y0, y1, C.accent, ax, -18);
      O.text(CL('growth_phoenix'), x0 - 40, (y0 + y1) / 2 + 30, 96, { kind: 'compare', color: C.accent, align: 'right', alpha: ax });
      const [z0x, z0y] = S2(X(0) - 0.75, 0), [, z1y] = S2(0, 2); O.bracket(z0x, z0y, z1y, C.accent, ax, -18);
      O.text('×1', z0x - 30, (z0y + z1y) / 2 + 18, 52, { kind: 'compare', color: C.accent, align: 'right', alpha: ax });
      const [ex, ey] = S2(X(0), 0), [fx] = S2(X(105), 0);
      O.text(String(CL('buy_year')), ex, ey + 48, 44, { kind: 'number', color: C.ink, align: 'center', alpha: a });
      O.text(CL('sale_quarter'), fx, ey + 48, 44, { kind: 'number', color: C.ink, align: 'center', alpha: a });
    }
    // lớp bắt buộc (quy tắc 5)
    O.chrome({ illus: true, src: t >= b.b1.src ? 'Source: FHFA via FRED' : null, srcA: ease(t, b.b1.src, b.b1.src + POP),
      hist: t >= b.b1.avg, histA: ease(t, b.b1.avg, b.b1.avg + POP),
      cw: t >= b.b10.past ? 'A measurement, not a tax bill or a next step' : t >= b.b4.gain ? 'A home that rose like the Phoenix average' : null,
      cwA: t >= b.b10.past ? ease(t, b.b10.past, b.b10.past + POP) : ease(t, b.b4.gain, b.b4.gain + POP) });
    st.compose();
    log.camMoving = CAM.moving(t);
    return log;
  }
  return { canvas: st.out, frame };
}
