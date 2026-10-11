// Tập 7 · C4 · ĐOẠN B = S04–S09. Hai thanh khoản trả (15 năm, 30 năm bắt buộc) → hộp đường lui (cushion, V6 có nhãn) → thế giới (đời Tessa) →
// S06 bản C3 + sửa: vạch mức 15 năm, đồ thị sớm, thanh 30 năm dâng qua vạch đúng "forty", đẩy máy vào đỉnh thanh, lát tách ở "same", the stack dựng
// từ "Over" → thế giới: the stack → hai đường lãi khảo sát (V3) + ngoặc 0.67 → tháp lãi xếp bằng bó của the stack (W2 ×3) → 15 bó chênh rời tháp,
// đáp lên đúng the stack cạnh nhà → hàng chồng mờ các tuần khác (câu hỏi hồi 2) → MR1. Mốc giờ chỉ từ spine.json.
import { setup, figure, gesture, figTag, LoanTag, BundleTower, nameTag, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, vbrace, dip,
  kf, show, pulse, C, ease, lin, mix, rgba, THREE, setOpacity, PALETTE } from '/episodes/ep007/world/c4kit.js';
import { PayBar, TRACK } from '/episodes/ep007/world/obj7.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep007/world/c4/b-s04-s09/';
const SCALE = 1 / 980;            // USD/tháng → chiều cao thế giới (thanh khoản trả; đỉnh 3,01 > chồng 15 bó 2,55: chồng THẤP hơn đỉnh thanh)
const BAR_W = 0.8, BAR_D = 0.5, FLY_W = 0.9, FLY_D = 0.6, RY = 0.55;   // RY: điểm % → đơn vị (đường lãi, trục từ 0)

export async function boot(res) {
  const poses = {
    wB0: { pos: [-8.4, 3.2, 9.8], tgt: [-1.6, 1.3, 0], fov: 40, chart: 0 },
    wB1: { pos: [-7.2, 2.7, 8.4], tgt: [-1.4, 1.3, 0], fov: 40, chart: 0 },
    cB: { pos: [0.6, 1.7, 22], tgt: [0.6, 1.7, 0], fov: 19.6, chart: 1 },
    wB5: { pos: [-8.0, 2.5, 8.0], tgt: [-2.2, 1.2, 0], fov: 40, chart: 0 },
    // vòng bố cục 1: cTop không còn cắt chân hai thanh dưới dải chân trang — ≈ 200 px/đơn vị (lát ≈ 24 px ở 1080), sàn py ≈ 840, hai thanh lệch
    // trái để nhãn $2,948 và "+$120" đứng bên phải thanh 30 năm (không vào dải góc trên)
    cTop: { pos: [3.5, 1.5, 16], tgt: [3.5, 1.5, 0], fov: 19.16, chart: 1 },
    wStack: { pos: [-4.9, 1.9, 5.8], tgt: [-2.2, 1.1, 0], fov: 38, chart: 0 },
    cRates: { pos: [21.0, 2.6, 20], tgt: [21.0, 2.6, 0], fov: 16.6, chart: 1 },
    cTowers: { pos: [8.6, 3.3, 26], tgt: [8.6, 3.3, 0], fov: 20.5, chart: 1 },
    cTops: { pos: [10.15, 2.6, 24], tgt: [10.15, 2.6, 0], fov: 12.0, chart: 1 },
    wHouse: { pos: [-6.8, 2.6, 8.8], tgt: [-2.2, 1.2, 0], fov: 38, chart: 0 },
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, X = S.x;
  const hm = figure(scene, { x: X.house }), tag = LoanTag(scene, hm), stack = theStack(scene, G, { x: X.stack });
  tag.set(1);
  const tagMat = tag.children[1].material;
  const bar15 = PayBar({ w: BAR_W, d: BAR_D, scale: SCALE, name: '15-year' }), bar30 = PayBar({ w: BAR_W, d: BAR_D, scale: SCALE, name: '30-year' });
  bar15.position.set(X.bar15, 0, 0); bar30.position.set(X.bar30, 0, 0); scene.add(bar15, bar30);
  const top15 = G.pay15 * SCALE, top30 = G.pay30 * SCALE, sliver = (G.pay30on15 - G.pay15) * SCALE;
  // S05: khoảng đường lui = hộp cushion trong suốt trên thanh 30 năm, từ mức bắt buộc tới mức 15 năm
  const room = new THREE.Mesh(new THREE.BoxGeometry(BAR_W + 0.04, 1, BAR_D + 0.04), new THREE.MeshStandardMaterial({ color: C.cushion, emissive: new THREE.Color(C.cushion), emissiveIntensity: 0.4, transparent: true, depthWrite: false }));
  room.geometry.translate(0, 0.5, 0); room.position.set(X.bar30, top30, 0); scene.add(room); room.userData.checks = { role: 'mark', key: 'fallback-room', value: +(G.pay15 - G.pay30).toFixed(2) };
  // S05.3 "pays it like a short loan": bóng mờ thanh 30 năm tới mức trả trong 15 năm (chưa số)
  const ghost = new THREE.Mesh(new THREE.BoxGeometry(BAR_W + 0.02, 1, BAR_D + 0.02), new THREE.MeshStandardMaterial({ color: C.ink, transparent: true, opacity: 0.2, depthWrite: false }));
  ghost.geometry.translate(0, 0.5, 0); ghost.position.set(X.bar30, top30, 0); ghost.scale.y = (G.pay30on15 - G.pay30) * SCALE; scene.add(ghost);
  // S06: vạch mức 15 năm (ink-muted, đứng yên) trước mặt hai thanh, kéo qua cả hai
  const lx0 = X.bar15 - BAR_W / 2 - 0.15, lx1 = X.bar30 + BAR_W / 2 + 0.15, LZ = BAR_D / 2 + 0.02;
  const lvGeo = new THREE.BoxGeometry(1, 0.035, 0.02); lvGeo.translate(0.5, 0, 0);
  const level = new THREE.Mesh(lvGeo, new THREE.MeshBasicMaterial({ color: TRACK.mark })); level.position.set(lx0, top15, LZ); scene.add(level);
  level.userData.checks = { role: 'mark', key: 'level-15', value: G.pay15 };
  // lát / bó bay (S06): bắt đầu TRÙNG lát warn trên đỉnh thanh 30 năm, nhấc lên, vòng ra trước thanh 15 năm, thành bó trên đỉnh chồng
  const flyMat = new THREE.MeshStandardMaterial({ color: TRACK.warn, roughness: 0.8, emissive: new THREE.Color(TRACK.warn), emissiveIntensity: 0.25 });
  const pool = (n) => [...Array(n)].map(() => { const m = new THREE.Mesh(new THREE.BoxGeometry(FLY_W, BUNDLE_TH, FLY_D), flyMat); m.castShadow = true; m.visible = false; scene.add(m); return m; });
  const flies = pool(5), HOVER = 0.32;
  const path = (k, p) => {   // p ∈ [0,1] (từ chỗ lơ lửng trên đỉnh thanh 30 năm) → đỉnh chồng (bó k)
    const ys = top15 + sliver / 2 + HOVER, ye = k * BUNDLE_TH + BUNDLE_TH / 2;
    return [X.bar30 + (X.stack - X.bar30) * p, ys + (ye - ys) * p ** 3 + 0.5 * Math.sin(Math.PI * p), 0.8 * Math.sin(Math.PI * p)];
  };
  // S07.2: hai đường lãi khảo sát (accent) 104 tuần tới tuần 8/10/2026, trục từ 0
  const nR = S.rates.r30.length, RX0 = X.rates[0], RX1 = X.rates[1], rx = (i) => RX0 + (RX1 - RX0) * i / (nR - 1);
  const l30 = Ribbon({ color: C.accent, z: 0.2, width: 0.07, maxPts: nR }), l15 = Ribbon({ color: '#8DB5FF', z: 0.2, width: 0.05, maxPts: nR });
  scene.add(l30, l15);
  const zero = new THREE.Mesh(new THREE.BoxGeometry(RX1 - RX0 + 0.3, 0.03, 0.03), new THREE.MeshStandardMaterial({ color: C.grid, emissive: new THREE.Color(C.grid), emissiveIntensity: 0.6, transparent: true }));
  zero.position.set((RX0 + RX1) / 2, 0.02, 0.2); scene.add(zero);
  l30.userData.checks = { role: 'series', series: 'r30', key: 'rate-30' }; l15.userData.checks = { role: 'series', series: 'r15', key: 'rate-15' };
  // S08–S09: tháp lãi bằng bó của the stack
  const n = (usd) => usd / G.bundle_usd, T = S.towers;
  const tw = { full: BundleTower(scene, { x: X.full, n: n(T.full[2]), name: 'interest-30full' }), on15: BundleTower(scene, { x: X.on15, n: n(T.on15[2]), name: 'interest-30on15' }),
    y15: BundleTower(scene, { x: X.y15, n: n(T.y15[2]), name: 'interest-15' }) };
  const nC = n(T.y15[2]), nB = n(T.on15[2]), SEC0 = Math.floor(nC);   // 15 bó trên cùng của tháp 30-trong-15 = phần cao hơn tháp 15 năm
  const secFly = pool(15);
  const lift = (j) => MV.m_w9.t0 + S.lift_dt * j, landAt = (j) => S.land9 + S.land_dt * j;   // j = 0 là bó trên cùng (rời trước)
  const glow = new THREE.Mesh(new THREE.BoxGeometry(1.06, 15 * BUNDLE_TH + 0.1, 0.76), new THREE.MeshBasicMaterial({ color: C.warn, transparent: true, opacity: 0, depthWrite: false }));
  glow.position.set(X.stack, (15 * BUNDLE_TH + 0.1) / 2, 0); scene.add(glow);
  // S09.3: hàng chồng mờ của 12 tuần khác (cùng thang bó) sau nhà
  const ghosts = S.ghosts.map((usd, i) => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.55, 1, 0.4), new THREE.MeshStandardMaterial({ color: C.muted, transparent: true, opacity: 0, depthWrite: false }));
    m.geometry.translate(0, 0.5, 0); m.position.set(-9.2 + i * 1.0, 0, -3.0); m.userData.h = n(usd) * BUNDLE_TH; scene.add(m); return m; });

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    tagMat.emissiveIntensity = 0.15 + 0.9 * pulse(t, b.b1.three, 0.9);
    // S04: thanh 15 năm dâng ở "fifteen-year" (thế giới), thanh 30 năm ở "thirty-year" (đồ thị); S06: 30 năm dâng tới $2,948
    const u15 = G.pay15 * ease(t, b.b1.fifteen, b.b1.fifteen + 0.9);
    bar15.set({ usd: u15 }); bar15.children[0].material.emissiveIntensity = 0.12 + 0.5 * pulse(t, b.b4.squeeze, 0.9);
    const u30 = t < S.rise30[1][0] ? G.pay30 * ease(t, b.b2.thirty, b.b2.thirty + 0.9) : kf(S.rise30, t);
    bar30.set({ usd: u30, warnAbove: G.pay15, topA: Math.min(1, Math.max(0, (u30 - G.pay15) / (G.pay30on15 - G.pay15))) });
    bar30.children[1].material.emissiveIntensity = 0.3 + 0.9 * pulse(t, b.b7.one, 1.0);
    const rA = 0.42 * ease(t, b.b3.gap - 0.05, b.b3.gap + 0.5) * (1 - ease(t, b.b6.finishing, b.b6.finishing + 0.5));
    room.scale.y = Math.max(0.001, (top15 - top30) * ease(t, b.b3.gap - 0.05, b.b3.gap + 0.5)); room.material.opacity = rA; room.visible = rA > 0.01;
    ghost.material.opacity = 0.2 * show(t, b.b5.short) * (1 - ease(t, S.rise30[1][0], S.rise30[2][0])); ghost.visible = ghost.material.opacity > 0.01;
    const lv = ease(t, S.level_t - 0.05, S.level_t + 0.5); level.scale.x = Math.max(0.001, (lx1 - lx0) * lv); level.visible = lv > 0.01;
    stackSet(stack, kf(S.stack, t));
    // S06: lát lơ lửng ("same") = bó 0; mỗi bó rời đỉnh thanh ở leave[k], bay fly s
    for (const f of flies) f.visible = false;
    let nf = 0, trail = null;
    for (let k = 0; k < 15 && nf < flies.length; k++) {
      const t0 = S.leave[k], t1 = t0 + S.fly, f = flies[nf];
      if (k === 0 && t >= b.b7.same - 0.3 && t < t0) {   // tách khỏi đỉnh thanh, nhấc lên HOVER, lơ lửng tới "Over" (sync_audit +0,26 → sớm 0,25 s)
        const u = ease(t, b.b7.same - 0.3, b.b7.same + 0.05);
        f.position.set(X.bar30, top15 + sliver / 2 + HOVER * u, 0); f.scale.set(BAR_W / FLY_W, sliver / BUNDLE_TH, BAR_D / FLY_D); f.visible = true; nf++; continue;
      }
      if (t < t0 || t >= t1) continue;
      const p = (t - t0) / S.fly, [x, y, z] = path(k, p), s = Math.min(1, p * 1.6);
      f.position.set(x, k === 0 ? y : (p < 0.15 ? top15 + sliver / 2 + HOVER * p / 0.15 : y), z);
      f.scale.set((BAR_W / FLY_W) * (1 - s) + 0.85 * s, (sliver / BUNDLE_TH) * (1 - s) + 0.92 * s, (BAR_D / FLY_D) * (1 - s) + s); f.visible = true; nf++;
      if (!trail || t0 > trail.t0) trail = { k, p, t0 };
    }
    // S07.2: hai đường lãi vẽ trái → phải ở "thirty-year"; tắt khi lùi ra tháp
    const dr = lin(t, b.c0.thirty, b.c0.thirty + 1.0) * (nR - 1), rAl = 1 - ease(t, MV.m_out8.t0, MV.m_out8.t0 + 0.5);
    for (const [L, R] of [[l30, S.rates.r30], [l15, S.rates.r15]]) {
      const m = Math.floor(dr), pts = []; for (let i = 0; i <= m; i++) pts.push([rx(i), R[i] * RY]);
      if (m < nR - 1 && dr > m) pts.push([rx(dr), mix(R[m], R[m + 1], dr - m) * RY]);
      if (pts.length > 1) L.set(pts); L.visible = pts.length > 1 && rAl > 0.01; L.material.opacity = rAl;
    }
    zero.visible = dr > 0 && rAl > 0.01; zero.material.opacity = rAl;
    // S08–S09: tháp lãi dâng tới tổng ở từ số; 15 bó chênh hoá warn ở "difference", rời tháp từng bó (trên cùng trước) và đáp lên the stack
    for (const k of ['full', 'on15', 'y15']) {
      // về thế giới (S09.2): tháp thu đi — máy thế giới cắt tháp ở mép phải, dưới huy hiệu ILLUSTRATIVE (vòng bố cục 1); tháp 30-trong-15 đi
      // sau khi bó chênh cuối đã rời
      const [a, z, usd] = T[k], cnt = n(usd) * lin(t, a, z);
      if (k !== 'on15') { tw[k].set({ count: cnt, a: 1 - ease(t, MV.m_w9.t0, MV.m_w9.t0 + 1.0) }); continue; }
      let started = 0; for (let j = 0; j < 15; j++) if (t >= lift(j)) started++;
      tw.on15.set({ count: cnt, warnFrom: t >= b.c3.difference - 0.05 ? SEC0 : Infinity, hideFrom: started ? SEC0 + 15 - started : Infinity,
        a: 1 - ease(t, lift(14) + 0.1, lift(14) + 0.9) });
    }
    let gl = 0;
    for (let j = 0; j < 15; j++) {
      const f = secFly[j], a = lift(j), z = landAt(j); f.visible = t >= a && t < z; gl = Math.max(gl, pulse(t, z, 0.45));
      if (!f.visible) continue;
      const p = ease(t, a, z), [x0, y0, z0] = tw.on15.posOf(SEC0 + 14 - j), x1 = X.stack, y1 = (14 - j) * BUNDLE_TH + BUNDLE_TH / 2;
      f.position.set(mix(x0, x1, p), mix(y0, y1, p) + 1.6 * Math.sin(Math.PI * p), mix(z0, 0, p) + 0.6 * Math.sin(Math.PI * p)); f.scale.set(1, 0.92, 1);
    }
    glow.material.opacity = 0.35 * Math.max(gl, pulse(t, b.c4.price, 0.8), pulse(t, b.c5.unusual, 0.9), pulse(t, b.b9.stack, 0.9)); glow.visible = glow.material.opacity > 0.01;
    // sync_audit +0,57 → hàng chồng mờ bắt đầu mọc 0,3 s trước "normal", so le 0,03 s, mỗi chồng 0,6 s (đỉnh chuyển động quanh từ khoá)
    ghosts.forEach((m, i) => { const g = ease(t, b.c5.normal - 0.3 + 0.03 * i, b.c5.normal - 0.3 + 0.03 * i + 0.6); m.scale.y = Math.max(0.001, m.userData.h * g); m.material.opacity = 0.32 * g; m.visible = g > 0.01; });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 0.62 * (1 - ease(t, 0.0, 0.9)));   // hồi 1 sáng dần từ ident (đoạn a kết ở thế giới tối 0,62); vẽ TRƯỚC mọi chữ
    figTag(O, hm);
    const sc = (x, y, z = 0) => O.toScreen(x, y, z);
    { const [x, y] = sc(...tag.top()); log.roi['b1.three'] = [x - 70, y - 30, x + 70, y + 120]; }
    const [b15x0, y15] = sc(X.bar15 - BAR_W / 2, top15), [b30x1, y30] = sc(X.bar30 + BAR_W / 2, top30), [, y30b] = sc(X.bar30, 0);
    log.roi['b1.fifteen'] = [b15x0 - 10, y15 - 20, b15x0 + 140, y30b]; log.roi['b2.thirty'] = [b30x1 - 140, y30 - 20, b30x1 + 10, y30b];
    // S04: nhãn hai thanh (mỗi nhãn cạnh thanh của nó); tắt ở "gap"
    const s4 = b.b3.gap - 0.1;
    label(O, `${D('term_short')}: ${D('pay15_month')}`, b15x0 - 14, y15 + 16, { align: 'right', kind: 'number', alpha: ok * show(t, b.b1.two, s4), claims: ['term_short', 'pay15_month'] });
    log.roi['b1.two'] = [b15x0 - 720, y15 - 30, b15x0, y15 + 30];
    const rq = ok * show(t, b.b2.two, s4) + ok * show(t, MV.m_c6.t1 - 0.05, S.rise30[1][0] + 0.25);
    label(O, `${D('term_long')} required:`, b30x1 + 20, y30 - 6, { kind: 'number', px: 48, alpha: Math.min(1, rq), claims: ['term_long'] });
    label(O, D('pay30_now'), b30x1 + 20, y30 + 52, { kind: 'number', alpha: Math.min(1, rq), claims: ['pay30_now'] });
    log.roi['b2.two'] = [b30x1 + 10, y30 - 50, b30x1 + 520, y30 + 70];
    // S05: ngoặc đường lui (cushion) cạnh thanh 30 năm + nhãn phía trên hai thanh
    // vòng bố cục 1 (đạo diễn: không thấy ngoặc ở khung giữa S05): ngoặc + vạch mức 15 năm ĐỨNG cả S05 — qua đời Tessa (thế giới, cùng hộp
    // cushion 3D) tới "finishing"; ở thế giới nhãn chữ "fallback" (không số) cạnh ngoặc thay nhãn số
    const s5 = MV.m_w5.t0 - 0.05, bA = show(t, b.b3.gap, b.b6.finishing - 0.05);
    vbrace(O, b30x1 + 26, y15, y30, C.cushion, bA, 6, 16);
    seg2(O, b15x0 + 0.5 * (b30x1 - b15x0) - 60, y15, b30x1 + 26, y15, C.muted, 0.7 * bA, 3, [10, 8]);
    label(O, 'fallback', b30x1 + 46, (y15 + y30) / 2 + 16, { kind: 'name', px: 48, color: '#7FD8C4', alpha: bA * (1 - cw) * show(t, MV.m_w5.t0 + 0.3) });
    const lxC = (b15x0 + b30x1) / 2;
    label(O, `fallback: ${D('fallback_gap_now')} lower`, lxC, y15 - 135, { align: 'center', kind: 'number', alpha: ok * show(t, b.b3.six, s5), color: '#7FD8C4', claims: ['fallback_gap_now'] });
    label(O, `the least the ${D('term_long')} asks`, lxC, y15 - 72, { align: 'center', kind: 'number', alpha: ok * show(t, b.b3.least, s5), claims: ['term_long'] });
    log.roi['b3.gap'] = [b30x1 - 140, y15 - 10, b30x1 + 50, y30 + 10]; log.roi['b3.six'] = [lxC - 520, y15 - 180, lxC + 520, y15 - 120]; log.roi['b3.least'] = [lxC - 400, y15 - 115, lxC + 400, y15 - 60];
    log.roi['b4.squeeze'] = [b15x0 - 10, y15 - 10, b15x0 + 140, y30b]; log.roi['b5.short'] = [b30x1 - 140, y15 - 40, b30x1 + 10, y30 + 10];
    { const [hx, hy] = sc(hm.person.position.x, hm.h, hm.person.position.z); log.roi['b5.house'] = [hx - 90, hy - 90, hx + 90, hy + 60]; }
    // S06 (C3 + sửa): "$2,828 a month" ở đầu trái vạch (tắt khi đẩy máy vào đỉnh thanh); "30-year paid in 15: $2,948 a month" đúng "forty", trên
    // hai thanh; "+$120 a month" cạnh lát; nhãn chồng hai dòng trên chồng (lệch trái, không chạm thanh 15 năm)
    const [vx, vy] = sc(lx0, top15, LZ);
    label(O, D('pay15_month'), vx - 14, vy + 16, { align: 'right', kind: 'number', alpha: ok * show(t, MV.m_c6.t1 - 0.05, MV.m_top.t0), claims: ['pay15_month'] });
    log.roi['b6.finishing'] = [...sc(lx0, top15 + 0.15, LZ), ...sc(lx1, top15 - 0.15, LZ)];
    // cB: nhãn $2,948 căn giữa trên hai thanh; cTop (đẩy vào): trượt sang BÊN PHẢI thanh 30 năm, ngang đỉnh thanh (kT = phần đã đẩy vào)
    const [pcx] = sc((X.bar15 + X.bar30) / 2, 0), [, y48] = sc(X.bar30, G.pay30on15 * SCALE), kT = ease(t, MV.m_top.t0, MV.m_top.t1) * (1 - ease(t, MV.m_back.t0, MV.m_back.t1));
    const s48 = `${D('term_long')} paid ${D('paid_in_short')}: ${D('pay30on15_now')}`;
    { const c = O.ctx; c.save(); c.font = '700 52px Inter'; const w48 = c.measureText(s48).width; c.restore();
      const x48 = mix(pcx, Math.min(b30x1 + 26 + w48 / 2, 1810 - w48 / 2), kT), yl = mix(y48 - 92, y48 - 40, kT);
      label(O, s48, x48, yl, { align: 'center', kind: 'number', alpha: ok * show(t, b.b6.forty, MV.m_w7.t0 - 0.05), claims: ['term_long', 'paid_in_short', 'pay30on15_now'] });
      log.roi['b6.forty'] = [x48 - 520, yl - 50, x48 + 520, y48 + 10]; }
    const [xs, ys] = sc(X.bar30 + BAR_W / 2, top15 + sliver / 2);
    label(O, `+${D('extra_vs15_month_now')}`, xs + 26, ys + 18 + 12 * kT, { kind: 'number', px: 56, alpha: ok * show(t, b.b7.one, MV.m_w7.t0 - 0.05), claims: ['extra_vs15_month_now'] });
    log.roi['b7.one'] = [xs - 140, ys - 50, xs + 420, ys + 40];
    { const [hx, hy] = sc(X.bar30, top15 + sliver + HOVER + 0.1); log.roi['b7.same'] = [hx - 120, hy - 40, hx + 120, hy + 50]; }
    // S06: tên hai thanh ở chân (chữ, không số tiền) — người tắt tiếng biết thanh nào khi đẩy máy vào đỉnh; 15 năm bên trái, 30 năm bên phải
    { const nA = ok * show(t, MV.m_c6.t1 - 0.05, MV.m_w7.t0 - 0.05), [, yf] = sc(X.bar15, 0, BAR_D / 2);
      label(O, D('term_short'), b15x0 - 12, yf - 20, { align: 'right', kind: 'number', px: 48, color: '#C9CED6', alpha: nA, claims: ['term_short'] });
      label(O, D('term_long'), b30x1 + 12, yf - 20, { kind: 'number', px: 48, color: '#C9CED6', alpha: nA, claims: ['term_long'] }); }
    if (trail && ok) {   // vệt đường bay của bó mới nhất (warn mờ, nét đứt): nối đỉnh thanh 30 năm với bó
      const c = O.ctx; c.save(); c.globalAlpha = 0.35 * (1 - ease(trail.p, 0.75, 1)); c.strokeStyle = TRACK.warn; c.lineWidth = 4; c.setLineDash([10, 10]); c.beginPath();
      for (let i = 0; i <= 16; i++) { const [x, y, z] = path(trail.k, (trail.p * i) / 16), [qx, qy] = sc(x, y, z); i ? c.lineTo(qx, qy) : c.moveTo(qx, qy); }
      c.stroke(); c.restore();
    }
    const [kx, ky] = sc(X.stack - 0.3, 15 * BUNDLE_TH), stA = ok * show(t, b.b8.twenty, MV.m_w7.t0 - 0.05);
    label(O, `the stack: ${D('extra_vs15_total_now')}`, kx, ky - 90, { align: 'center', kind: 'number', alpha: stA, claims: ['extra_vs15_total_now'] });
    label(O, `extra paid over ${D('term_short_years')}`, kx, ky - 30, { align: 'center', kind: 'number', alpha: stA, claims: ['term_short_years'] });
    // "Over": vật phản ứng ở từ khoá = lát RỜI đỉnh thanh 30 năm (mỗi 0,16 s một lát) — đo ở chỗ rời, không ở chỗ chồng nhận bó (chạm sau 0,6 s;
    // sync_audit +0,45 khi vùng đo gồm cả chồng)
    log.roi['b8.over'] = [...sc(X.bar30 - 0.7, top15 + sliver + HOVER + 0.45), ...sc(X.bar30 + 0.55, top15 - 0.2)]; log.roi['b8.twenty'] = [kx - 420, ky - 140, kx + 420, ky - 10];
    // S07.1 (thế giới): tên vật — không số
    { const [x, y0] = sc(X.stack, 15 * BUNDLE_TH + 0.2), y = Math.max(250, y0);   // máy gần: đỉnh chồng sát mép trên → nhãn không vào dải góc trên
      label(O, 'the stack = the price of the fallback', Math.min(Math.max(x, 590), 1330), y - 30, { align: 'center', kind: 'name', px: 48, alpha: show(t, b.b9.stack, MV.m_c7.t0) * (1 - cw), color: C.warn });
      log.roi['b9.stack'] = [x - 460, y - 80, x + 460, y + 250]; }
    // S07.2: khoảng giữa hai đường (accent mờ), mốc tuần cuối, ngoặc + nhãn
    if (dr > 0 && rAl > 0.01) {
      const P30 = S.rates.r30.map((r, i) => sc(rx(i), r * RY, 0.2)), P15 = S.rates.r15.map((r, i) => sc(rx(i), r * RY, 0.2)), c = O.ctx, hA = ok * show(t, b.c0.higher, MV.m_out8.t0);
      if (hA > 0.01) { c.save(); c.globalAlpha = 0.16 * hA; c.fillStyle = C.accent; c.beginPath(); P30.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y)));
        for (let i = nR - 1; i >= 0; i--) c.lineTo(...P15[i]); c.closePath(); c.fill(); c.restore(); }
      const [ex, e30] = P30[nR - 1], [, e15] = P15[nR - 1], [, e0] = sc(rx(nR - 1), 0, 0.2), oA = ok * show(t, b.c0.october, MV.m_out8.t0);
      seg2(O, ex, e30 - 34, ex, e0, C.muted, 0.8 * oA, 3, [8, 8]);
      if (oA > 0.01) { c.save(); c.globalAlpha = oA; c.fillStyle = C.accent; for (const yy of [e30, e15]) { c.beginPath(); c.arc(ex, yy, 9, 0, 7); c.fill(); } c.restore(); }
      label(O, `${D('term_long')}: ${D('r30_now')}`, ex + 40, e30 + 4, { kind: 'number', px: 48, alpha: oA, color: '#A9C6FF', claims: ['term_long', 'r30_now'] });
      label(O, `${D('term_short')}: ${D('r15_now')}`, ex + 40, e15 + 40, { kind: 'number', px: 48, alpha: oA, color: '#A9C6FF', claims: ['term_short', 'r15_now'] });
      const zA = ok * show(t, b.c0.zero, MV.m_out8.t0);
      vbrace(O, ex + 20, e30, e15, C.ink, zA, 5, 12);
      label(O, `${D('term_long')} rate ${D('spread_now')} higher`, ex + 40, e30 - 70, { kind: 'number', px: 48, alpha: zA, claims: ['term_long', 'spread_now'] });
      log.roi['c0.thirty'] = [P30[0][0], e30 - 40, ex, e0]; log.roi['c0.higher'] = [P30[0][0], e30, ex, e15 + 120]; log.roi['c0.october'] = [ex - 30, e30 - 50, ex + 480, e15 + 60];
      log.roi['c0.zero'] = [ex, e30 - 120, ex + 900, e15 + 10];
    }
    // S08–S09: nhãn tháp
    const tl = (k) => { const [x, y] = sc(tw[k].position.x, tw[k].topY(n(T[k][2]))); return [x, y]; };
    { const [ax, ay] = tl('full'), [ax1] = sc(X.full + tw.full.halfW, 0), aA = ok * show(t, b.c1.four, MV.m_tops.t0);
      label(O, `${D('term_long')} on its own schedule:`, ax1 + 24, ay + 34, { kind: 'number', px: 48, alpha: aA, claims: ['term_long'] });
      label(O, `${D('interest_30full_now')} interest`, ax1 + 24, ay + 94, { kind: 'number', alpha: aA, claims: ['interest_30full_now'] });
      log.roi['c1.thirty'] = [ax - 160, ay - 20, ax + 160, sc(0, 0)[1]]; log.roi['c1.four'] = [ax1, ay - 20, ax1 + 900, ay + 110]; }
    // vòng bố cục 1 (đạo diễn: nhãn $210,691 nằm trên tháp $477,622): nhãn bắt đầu NGAY PHẢI tháp 30 năm, sát trên đỉnh tháp CỦA NÓ, dây dẫn xuống
    // đỉnh tháp đó; đẩy máy vào hai tháp (S09.1) thì nhãn lên cao như cũ (chỗ dưới cho "difference = the stack"), dây tắt
    { const [bx, by] = tl('on15'), [fx1] = sc(X.full + tw.full.halfW, 0), bA2 = ok * show(t, b.c2.two, MV.m_w9.t0), kS = ease(t, MV.m_tops.t0, MV.m_tops.t1), yl = by - 62 - 68 * kS;
      label(O, `${D('term_long')} paid ${D('paid_in_short')}: ${D('interest_30on15_now')}`, fx1 + 24, yl, { kind: 'number', alpha: bA2, claims: ['term_long', 'paid_in_short', 'interest_30on15_now'] });
      seg2(O, bx, yl + 18, bx, by - 8, C.muted, 0.85 * bA2 * (1 - kS), 3);
      log.roi['c2.fifteen'] = [bx - 200, by - 20, bx + 200, sc(0, 0)[1]]; log.roi['c2.two'] = [fx1 + 14, yl - 50, fx1 + 940, yl + 20]; }
    { const [cx, cy] = tl('y15'), cA = ok * show(t, b.c3.one, MV.m_w9.t0);
      label(O, `${D('term_short')}: ${D('interest_15_now')} interest`, cx, cy - 40, { align: 'center', kind: 'number', alpha: cA, claims: ['term_short', 'interest_15_now'] });
      log.roi['c3.fifteen'] = [cx - 200, cy - 20, cx + 200, sc(0, 0)[1]]; log.roi['c3.one'] = [cx - 420, cy - 90, cx + 420, cy - 25]; }
    { const [bx0, yB] = sc(X.on15 - tw.on15.halfW, tw.on15.topY(nB)), [, yC] = sc(X.on15, nC / 9 * BUNDLE_TH), [cx0] = sc(X.y15 - tw.y15.halfW, 0);
      const dA = ok * show(t, b.c3.difference, MV.m_w9.t0 + 0.2), [bxc] = sc(X.on15, 0);
      seg2(O, cx0, yC, bx0 - 6, yC, C.muted, 0.75 * dA, 3, [10, 8]);
      vbrace(O, bx0 - 14, yB, yC, C.warn, dA, 6, -14);
      label(O, `difference = the stack: ${D('extra_vs15_total_now')}`, bxc, yB - 64, { align: 'center', kind: 'number', alpha: ok * show(t, b.c3.stack, MV.m_w9.t0 + 0.2), claims: ['extra_vs15_total_now'] });
      log.roi['c3.difference'] = [bx0 - 40, yB - 10, bx0 + 600, yC + 10]; log.roi['c3.stack'] = [bxc - 520, yB - 110, bxc + 520, yB - 50]; }
    { const [x, y] = sc(X.stack, 15 * BUNDLE_TH + 0.2); log.roi['c4.plus'] = [x - 200, y - 40, x + 200, sc(X.stack, 0)[1]]; log.roi['c4.price'] = log.roi['c4.plus']; log.roi['c5.unusual'] = log.roi['c4.plus']; }
    { const [x0, y0] = sc(-9.5, 3.6, -3), [x1, y1] = sc(2.2, 0, -3); log.roi['c5.normal'] = [x0, y0, x1, y1]; }
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
