// Tập 7 · C4 · ĐOẠN B = S04–S09. Hai thanh khoản trả (15 năm, 30 năm bắt buộc) → hộp đường lui (cushion, V6 có nhãn) → thế giới (đời Tessa) →
// S06 bản C3 + sửa: vạch mức 15 năm, đồ thị sớm, thanh 30 năm dâng qua vạch trước "two" (C5), một khung cB cả cảnh, lát tách ở "same", the stack dựng
// đều từ "Over" → thế giới: the stack → hai đường lãi khảo sát (V3) + ngoặc 0.67 → tháp lãi xếp bằng bó của the stack (W2 ×3) → khối 15 bó chênh
// nhấc lên cả khối, bay theo máy, chạm thành the stack cạnh nhà → thanh 15 năm + khối vàng ("plus") → MR1. Mốc giờ chỉ từ spine.json.
// C5 (c5/director-merged.md S04–S09): xem docstring spine.py — khung khoá S04, thanh 30 năm teal, nhãn chân, cờ lê + mốc 15 năm (S05), thanh dâng
// "finishing" → "two" (S06), chồng hoá khoảng giữa hai đường lãi + đẩy máy vào ngoặc (S07), tô bóng phần chênh (S08), nhãn trên tháp của nó (S09).
import { setup, figure, gesture, figTag, LoanTag, BundleTower, nameTag, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, vbrace, dip,
  kf, show, pulse, C, ease, lin, mix, rgba, THREE, setOpacity, PALETTE } from '/episodes/ep007/world/c4kit.js';
import { PayBar, TRACK } from '/episodes/ep007/world/obj7.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep007/world/c4/b-s04-s09/';
const SCALE = 1 / 980;            // USD/tháng → chiều cao thế giới (thanh khoản trả; đỉnh 3,01 > chồng 15 bó 2,55: chồng THẤP hơn đỉnh thanh)
const BAR_W = 0.8, BAR_D = 0.5, FLY_W = 0.9, FLY_D = 0.6, RY = 0.55;   // RY: điểm % → đơn vị (đường lãi, trục từ 0)

export async function boot(res) {
  // C5: wB1 khoá từ 0 s, nhìn gần dọc trục x → thanh 15 năm mọc ngay sau Tessa + nhà (không xa, không máy dời); cB 130 px/đơn vị: Tessa trong khung,
  // nhãn S04 + nhãn chồng S06 vừa bên phải; wB5 chính diện (góc xiên làm hộp cushion teo lại); cRates hai đường rộng 8 căn giữa; cRatesZ đẩy vào ngoặc
  const poses = {
    wB1: { pos: [-10.5, 2.0, 4.2], tgt: [-1.2, 1.3, 0], fov: 38, chart: 0 },
    cB: { pos: [1.25, 2.0, 22], tgt: [1.25, 2.0, 0], fov: 21.4, chart: 1 },
    wB5: { pos: [1.25, 2.6, 15], tgt: [1.25, 1.7, 0], fov: 31, chart: 0 },
    wStack: { pos: [-4.9, 1.9, 5.8], tgt: [-2.2, 1.1, 0], fov: 38, chart: 0 },
    cRates: { pos: [9.3, 2.3, 20], tgt: [9.3, 2.3, 0], fov: 22.2, chart: 1 },
    cRatesZ: { pos: [11.9, 3.75, 20], tgt: [11.9, 3.75, 0], fov: 8.6, chart: 1 },
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
  // C5 (đạo diễn S04: hai thanh cùng xám): thân thanh 30 năm teal (C.cushion), thanh 15 năm giữ ink; phần warn trên mức 15 năm (S06) không đổi
  const b30m = bar30.children[0].material; b30m.color.set(C.cushion); b30m.emissive.set(C.cushion); b30m.emissiveIntensity = 0.3;
  const barA = (g, a) => { for (const m of g.children) m.material.opacity = a; g.visible = a > 0.01; };   // thu hai thanh khi rời S06 (đạo diễn S07/S09 PHỤ)
  const top15 = G.pay15 * SCALE, top30 = G.pay30 * SCALE, sliver = (G.pay30on15 - G.pay15) * SCALE;
  // S05: khoảng đường lui = hộp cushion trong suốt trên thanh 30 năm, từ mức bắt buộc tới mức 15 năm (C5: teal sáng hơn thân thanh để tách hộp)
  const room = new THREE.Mesh(new THREE.BoxGeometry(BAR_W + 0.04, 1, BAR_D + 0.04), new THREE.MeshStandardMaterial({ color: '#4FD1B5', emissive: new THREE.Color('#4FD1B5'), emissiveIntensity: 0.75, transparent: true, depthWrite: false }));
  room.geometry.translate(0, 0.5, 0); room.position.set(X.bar30, top30, 0); scene.add(room); room.userData.checks = { role: 'mark', key: 'fallback-room', value: +(G.pay15 - G.pay30).toFixed(2) };
  // S05.2 "repair … squeeze" (C5): cờ lê ink-muted — hàm mở chúc xuống (gốc = đáy hàm), cán nghiêng; ép thanh 15 năm rồi ép hộp cushion
  const wMat = new THREE.MeshStandardMaterial({ color: C.muted, roughness: 0.4, metalness: 0.5, transparent: true }), wrench = new THREE.Group();
  for (const [w, h, x, y] of [[0.42, 0.12, 0, 0.24], [0.1, 0.22, -0.16, 0.11], [0.1, 0.22, 0.16, 0.11], [0.12, 1.0, 0, 0.8]]) {
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.08), wMat); m.position.set(x, y, 0); m.castShadow = true; wrench.add(m);
  }
  wrench.rotation.z = 0.22; wrench.position.z = 0.1; wrench.visible = false; scene.add(wrench); wrench.userData.checks = { role: 'mark', key: 'repair-wrench' };
  // S05.3 "paid off in fifteen years" (C5: cắm mốc 15 năm): 15 ô năm trên sàn trước nhà → phải, mọc lần lượt "paid" → "fifteen", cờ cắm ở ô 15
  const YT = 15, YX0 = -2.3, YDX = 0.3, YZ = 1.3, ytMat = new THREE.MeshStandardMaterial({ color: C.muted, transparent: true });
  const years = [...Array(YT)].map((_, i) => { const m = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.05, 0.3), ytMat); m.position.set(YX0 + YDX * i, 0.025, YZ); m.visible = false; scene.add(m); return m; });
  const fMat = new THREE.MeshStandardMaterial({ color: C.ink, emissive: new THREE.Color(C.ink), emissiveIntensity: 0.2, transparent: true }), flag = new THREE.Group();
  const pole = new THREE.Mesh(new THREE.BoxGeometry(0.035, 0.9, 0.035), fMat), pen = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.18, 0.02), fMat);
  pole.position.y = 0.45; pen.position.set(0.16, 0.8, 0); flag.add(pole, pen); flag.position.set(YX0 + YDX * (YT - 1), 0, YZ); flag.visible = false; scene.add(flag);
  flag.userData.checks = { role: 'mark', key: 'milestone-15y' };
  // S09.2 "the 15-year plus a fallback" (C5): khối vàng (cỡ lát $120/tháng của S06) rơi lên đỉnh thanh 15 năm mọc lại
  const gold = new THREE.Mesh(new THREE.BoxGeometry(BAR_W, 1, BAR_D), new THREE.MeshStandardMaterial({ color: TRACK.warn, emissive: new THREE.Color(TRACK.warn), emissiveIntensity: 0.35, transparent: true }));
  gold.scale.y = sliver; gold.position.x = X.bar15; gold.castShadow = true; gold.visible = false; scene.add(gold); gold.userData.checks = { role: 'mark', key: 'fallback-price-on-15' };
  // S05.3 "pays it like a short loan": bóng mờ thanh 30 năm tới mức trả trong 15 năm (chưa số)
  const ghost = new THREE.Mesh(new THREE.BoxGeometry(BAR_W + 0.02, 1, BAR_D + 0.02), new THREE.MeshStandardMaterial({ color: C.ink, transparent: true, opacity: 0.2, depthWrite: false }));
  ghost.geometry.translate(0, 0.5, 0); ghost.position.set(X.bar30, top30, 0); ghost.scale.y = (G.pay30on15 - G.pay30) * SCALE; scene.add(ghost);
  // S06: vạch mức 15 năm (ink-muted, đứng yên) trước mặt hai thanh, kéo qua cả hai
  const lx0 = X.bar15 - BAR_W / 2 - 0.15, lx1 = X.bar30 + BAR_W / 2 + 0.15, LZ = BAR_D / 2 + 0.02;
  const lvGeo = new THREE.BoxGeometry(1, 0.035, 0.02); lvGeo.translate(0.5, 0, 0);
  const level = new THREE.Mesh(lvGeo, new THREE.MeshBasicMaterial({ color: TRACK.mark, transparent: true })); level.position.set(lx0, top15, LZ); scene.add(level);
  level.userData.checks = { role: 'mark', key: 'level-15', value: G.pay15 };
  // lát / bó bay (S06): bắt đầu TRÙNG lát warn trên đỉnh thanh 30 năm, nhấc lên, RƠI xuống chồng ngay phải thanh 30 năm (C5: stack6, dưới lát mỏng)
  const flyMat = new THREE.MeshStandardMaterial({ color: TRACK.warn, roughness: 0.8, emissive: new THREE.Color(TRACK.warn), emissiveIntensity: 0.25 });
  const pool = (n) => [...Array(n)].map(() => { const m = new THREE.Mesh(new THREE.BoxGeometry(FLY_W, BUNDLE_TH, FLY_D), flyMat); m.castShadow = true; m.visible = false; scene.add(m); return m; });
  const flies = pool(5), HOVER = 0.32;
  const path = (k, p) => {   // p ∈ [0,1] (từ chỗ lơ lửng trên đỉnh thanh 30 năm) → đỉnh chồng (bó k)
    const ys = top15 + sliver / 2 + HOVER, ye = k * BUNDLE_TH + BUNDLE_TH / 2;
    return [X.bar30 + (X.stack6 - X.bar30) * p, ys + (ye - ys) * p ** 3 + 0.4 * Math.sin(Math.PI * p), 0.4 * Math.sin(Math.PI * p)];
  };
  // S07.2: hai đường lãi khảo sát 104 tuần tới tuần 8/10/2026, trục từ 0; C5 (đạo diễn: mỗi đường một màu): 30 năm accent, 15 năm ink
  const nR = S.rates.r30.length, RX0 = X.rates[0], RX1 = X.rates[1], rx = (i) => RX0 + (RX1 - RX0) * i / (nR - 1);
  const l30 = Ribbon({ color: C.accent, z: 0.2, width: 0.07, maxPts: nR }), l15 = Ribbon({ color: C.ink, z: 0.2, width: 0.06, maxPts: nR });
  scene.add(l30, l15);
  // C5 (đạo diễn S07 16 s: ngoặc quá nhỏ): sau khi đẩy máy vào, một lát chồng (warn) rơi vào ngoặc ở chữ "higher" thứ hai — cao đúng khoảng chênh
  const r30L = S.rates.r30[nR - 1], r15L = S.rates.r15[nR - 1], SLX = RX1 + 0.18, yGap = (r30L + r15L) / 2 * RY;
  const slab = new THREE.Mesh(new THREE.BoxGeometry(0.16, (r30L - r15L) * RY, 0.3), new THREE.MeshStandardMaterial({ color: C.warn, emissive: new THREE.Color(C.warn), emissiveIntensity: 0.35, transparent: true }));
  slab.position.set(SLX, yGap, 0.2); slab.visible = false; scene.add(slab); slab.userData.checks = { role: 'mark', key: 'spread-slice' };
  // C5 (đạo diễn S07 8,9 s: khung đen trống): chồng HOÁ khoảng giữa hai đường — mặt trước chồng chiếu bằng tư thế ở m_c7.t0 (wStack) là hình gốc,
  // lớp phủ warn nội suy từ hình đó tới đa giác giữa hai đường (xong ở "higher"); chồng 3D ẩn từ m_c7.t0
  const P0 = CAM.poseAt(MV.m_c7.t0), cam0 = new THREE.PerspectiveCamera(P0.fov, 16 / 9, 0.1, 400);
  cam0.position.set(...P0.pos); cam0.lookAt(...P0.tgt); cam0.updateProjectionMatrix(); cam0.updateMatrixWorld();
  const scr0 = (x, y, z) => { const v = new THREE.Vector3(x, y, z).project(cam0); return [(v.x + 1) * 960, (1 - v.y) * 540]; };
  const SH = 15 * BUNDLE_TH, SR = [scr0(X.stack - 0.45, SH, 0.3), scr0(X.stack + 0.45, SH, 0.3), scr0(X.stack + 0.45, 0, 0.3), scr0(X.stack - 0.45, 0, 0.3)];
  const zero = new THREE.Mesh(new THREE.BoxGeometry(RX1 - RX0 + 0.3, 0.03, 0.03), new THREE.MeshStandardMaterial({ color: C.grid, emissive: new THREE.Color(C.grid), emissiveIntensity: 0.6, transparent: true }));
  zero.position.set((RX0 + RX1) / 2, 0.02, 0.2); scene.add(zero);
  l30.userData.checks = { role: 'series', series: 'r30', key: 'rate-30' }; l15.userData.checks = { role: 'series', series: 'r15', key: 'rate-15' };
  // S08–S09: tháp lãi bằng bó của the stack
  const n = (usd) => usd / G.bundle_usd, T = S.towers;
  const tw = { full: BundleTower(scene, { x: X.full, n: n(T.full[2]), name: 'interest-30full' }), on15: BundleTower(scene, { x: X.on15, n: n(T.on15[2]), name: 'interest-30on15' }),
    y15: BundleTower(scene, { x: X.y15, n: n(T.y15[2]), name: 'interest-15' }) };
  const nC = n(T.y15[2]), nB = n(T.on15[2]), SEC0 = Math.floor(nC);   // 15 bó trên cùng của tháp 30-trong-15 = phần cao hơn tháp 15 năm
  // C4 r3: khối chênh (bó i = 0 đáy … 14 đỉnh) NHẤC LIFT cả khối ở sec_lift (máy đứng yên), rồi bay cả khối theo máy (p: m_w9.t0 → land9), đường
  // cong, đội hình 3 × 3 của tháp thu về một cột = đúng chỗ bó i của the stack
  const secFly = pool(15), LIFT = 0.9;
  const secPos = (i, u, p) => { const [x0, y0, z0] = tw.on15.posOf(SEC0 + i);
    return [mix(x0, X.stack, p), mix(y0 + LIFT * u, i * BUNDLE_TH + BUNDLE_TH / 2, p) + 1.4 * Math.sin(Math.PI * p), mix(z0, 0, p) + 0.5 * Math.sin(Math.PI * p)]; };
  const glow = new THREE.Mesh(new THREE.BoxGeometry(1.06, 15 * BUNDLE_TH + 0.1, 0.76), new THREE.MeshBasicMaterial({ color: C.warn, transparent: true, opacity: 0, depthWrite: false }));
  glow.position.set(X.stack, (15 * BUNDLE_TH + 0.1) / 2, 0); scene.add(glow);
  // S08.2 (C5 đạo diễn 15,4 s: khoản chênh hai tháp không có hình): hộp ink-muted trong mờ trên tháp 30-trong-15 tới đỉnh tháp 30 năm (không số)
  const yTopF = tw.full.topY(n(T.full[2])), yTopB = tw.on15.topY(nB);
  const gapBox = new THREE.Mesh(new THREE.BoxGeometry(2 * tw.on15.halfW + 0.1, 1, 2.0), new THREE.MeshStandardMaterial({ color: C.muted, transparent: true, opacity: 0, depthWrite: false }));
  gapBox.geometry.translate(0, 0.5, 0); gapBox.position.set(X.on15, yTopB, 0); gapBox.visible = false; scene.add(gapBox); gapBox.userData.checks = { role: 'mark', key: 'interest-gap-full-vs-on15' };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    tagMat.emissiveIntensity = 0.15 + 0.9 * pulse(t, b.b1.three, 0.9);
    // S05.2 (C5): cờ lê hiện ở "repair" trên thanh 15 năm, ép xuống đúng "squeeze" (thanh lún 7 %, loé), sang thanh 30 năm ép hộp cushion: hộp co
    // 60 % (hấp thụ), thân thanh 30 năm đứng yên; thu đi trước "house"
    const q = b.b4.squeeze, p1 = ease(t, q - 0.15, q + 0.1) * (1 - ease(t, q + 0.55, q + 0.75)), wm = ease(t, q + 0.75, q + 1.2);
    const p2 = ease(t, q + 1.2, q + 1.5) * (1 - ease(t, q + 2.0, q + 2.3)), wA = ease(t, b.b4.repair - 0.05, b.b4.repair + 0.3) * (1 - ease(t, q + 2.3, q + 2.7));
    // S04: thanh 15 năm dâng ở "fifteen-year" (thế giới, khung khoá), thanh 30 năm ở "thirty-year" (đồ thị); S06: 30 năm dâng tới $2,948;
    // C5: hai thanh thu đi khi về thế giới ở S07.1; thanh 15 năm mọc lại ở S09.2 "the fifteen-year" (thế giới), thu đi ở "normal"
    const back = t >= b.c4.fifteen - 0.05, aOut = 1 - ease(t, MV.m_w7.t0, MV.m_w7.t0 + 0.5);
    const u15 = G.pay15 * (back ? ease(t, b.c4.fifteen, b.c4.fifteen + S.bar_up) : ease(t, b.b1.fifteen, b.b1.fifteen + S.bar_up));
    bar15.set({ usd: u15 }); bar15.children[0].material.emissiveIntensity = 0.12 + 0.5 * pulse(t, b.b4.squeeze, 0.9); bar15.scale.y = 1 - 0.07 * p1;
    barA(bar15, back ? 1 - ease(t, b.c5.normal - 0.3, b.c5.normal + 0.3) : aOut); barA(bar30, aOut);
    const u30 = t < S.rise30[1][0] ? G.pay30 * ease(t, b.b2.thirty, b.b2.thirty + 0.9) : kf(S.rise30, t);
    bar30.set({ usd: u30, warnAbove: G.pay15, topA: Math.min(1, Math.max(0, (u30 - G.pay15) / (G.pay30on15 - G.pay15))) });
    bar30.children[1].material.emissiveIntensity = 0.3 + 0.9 * pulse(t, b.b7.one, 1.0);
    // C4 r3 (đạo diễn #1: hộp + ngoặc "fallback" gần như đen trên đen ở đầu S06): hộp cushion sáng hơn (0,6) và đứng tới khi thanh 30 năm bắt đầu dâng
    const rA = 0.6 * ease(t, b.b3.gap - 0.05, b.b3.gap + 0.5) * (1 - ease(t, S.rise30[1][0], S.rise30[1][0] + 0.5)), roomH = (top15 - top30) * ease(t, b.b3.gap - 0.05, b.b3.gap + 0.5) * (1 - 0.6 * p2);
    room.scale.y = Math.max(0.001, roomH); room.material.opacity = rA; room.visible = rA > 0.01; room.material.emissiveIntensity = 0.75 + 0.6 * p2;
    wMat.opacity = wA; wrench.visible = wA > 0.01;
    wrench.position.x = mix(X.bar15, X.bar30, wm); wrench.position.y = (wm < 0.5 ? top15 * (1 - 0.07 * p1) : top30 + roomH) + 0.55 * (1 - Math.max(p1, p2));
    // S05.3 (C5): ô năm mọc lần lượt "paid" → "fifteen", cờ rơi cắm ở ô 15 đúng "fifteen"; thu đi trước "finishing" (đồ thị S06)
    const yA = 1 - ease(t, b.b6.finishing - 0.3, b.b6.finishing);
    years.forEach((m, i) => { const a = mix(b.b5.paid, b.b5.fifteen - 0.15, i / (YT - 1)), g = ease(t, a, a + 0.15) * yA; m.scale.y = Math.max(0.001, g); m.visible = g > 0.01; });
    ytMat.opacity = yA; fMat.opacity = yA;
    const fd = ease(t, b.b5.fifteen - 0.2, b.b5.fifteen + 0.05); flag.position.y = 1.2 * (1 - fd); flag.visible = fd > 0.01 && yA > 0.01;
    // S09.2 (C5): khối vàng rơi lên đỉnh thanh 15 năm đúng "plus"
    const gd = ease(t, b.c4.plus - 0.3, b.c4.plus); gold.position.y = top15 + sliver / 2 + 1.4 * (1 - gd);
    gold.material.opacity = 1 - ease(t, b.c5.normal - 0.3, b.c5.normal + 0.3); gold.visible = t >= b.c4.plus - 0.3 && gold.material.opacity > 0.01;
    // C5 (đạo diễn S06 2,7 s: "thanh đã dâng sẵn"): bóng mờ thấp hơn và thu đi TRƯỚC "finishing" — thanh thật dâng sau đó
    ghost.material.opacity = 0.3 * show(t, b.b5.short, b.b6.finishing - 0.35); ghost.visible = ghost.material.opacity > 0.01;
    const lv = ease(t, S.level_t - 0.05, S.level_t + 0.5) * aOut; level.scale.x = Math.max(0.001, (lx1 - lx0) * lv); level.visible = lv > 0.01; level.material.opacity = aOut;
    // the stack: dựng ở stack6 (S06, phải thanh 30 năm), trượt về cạnh nhà khi máy về thế giới (m_w7); ẩn từ m_c7.t0 (lớp phủ hoá khoảng giữa hai
    // đường lãi) tới lúc khối chênh chạm (land9): khối chênh CHÍNH LÀ chồng
    stack.position.x = mix(X.stack6, X.stack, ease(t, MV.m_w7.t0 + 0.45, MV.m_w7.t1));   // trượt sau khi hai thanh đã thu (0,5 s)
    stackSet(stack, t >= MV.m_c7.t0 && t < S.land9 ? 0 : kf(S.stack, t));
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
    const sd = ease(t, b.c0.higher2 - 0.35, b.c0.higher2); slab.position.y = yGap + 1.2 * (1 - sd); slab.material.opacity = rAl; slab.visible = t >= b.c0.higher2 - 0.35 && rAl > 0.01;
    // S08.2 (C5): bóng phần trống dâng từ đỉnh tháp 30-trong-15 tới mức đỉnh tháp 30 năm ở "dollars"; thu khi đẩy máy vào đỉnh hai tháp (S09.1)
    const gg = ease(t, b.c2.gap - 0.05, b.c2.gap + 0.6), gA = gg * (1 - ease(t, MV.m_tops.t0, MV.m_tops.t0 + 0.6));
    gapBox.scale.y = Math.max(0.001, (yTopF - yTopB) * gg); gapBox.material.opacity = 0.2 * gA; gapBox.visible = gA > 0.01;
    // S08–S09: tháp lãi dâng tới tổng ở từ số; 15 bó chênh hoá warn ở "difference", NHẤC cả khối (sec_lift), bay cả khối về cạnh nhà = the stack
    const secU = ease(t, S.sec_lift[0], S.sec_lift[1]), secP = ease(t, MV.m_w9.t0, S.land9), secOn = t >= S.sec_lift[0] && t < S.land9;
    for (const k of ['full', 'on15', 'y15']) {
      // về thế giới (S09.2): tháp thu đi khi máy rời (tháp 15 năm đứng cạnh suốt lúc khối nhấc: thấy phần dôi)
      const [a, z, usd] = T[k], cnt = n(usd) * lin(t, a, z);
      tw[k].set({ count: cnt, a: 1 - ease(t, MV.m_w9.t0, MV.m_w9.t0 + 1.0),
        ...(k === 'on15' ? { warnFrom: t >= b.c3.difference - 0.05 ? SEC0 : Infinity, hideFrom: secOn || t >= S.land9 ? SEC0 : Infinity } : {}) });
    }
    for (let j = 0; j < 15; j++) {
      const f = secFly[j]; f.visible = secOn; if (!secOn) continue;
      f.position.set(...secPos(j, secU, secP)); f.scale.set(1, 0.92, 1);
    }
    // C5 (đạo diễn S09 PHỤ: hàng chồng mờ = rác hình): bỏ hàng chồng mờ; "normal" = chồng của Tessa loé (như "unusual")
    glow.material.opacity = 0.35 * Math.max(pulse(t, S.land9, 0.6), pulse(t, b.c4.price, 0.8), pulse(t, b.c5.normal, 0.9), pulse(t, b.c5.unusual, 0.9), pulse(t, b.b9.stack, 0.9));
    glow.visible = glow.material.opacity > 0.01;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 0.62 * (1 - ease(t, 0.0, 0.9)));   // hồi 1 sáng dần từ ident (đoạn a kết ở thế giới tối 0,62); vẽ TRƯỚC mọi chữ
    figTag(O, hm);
    const sc = (x, y, z = 0) => O.toScreen(x, y, z);
    { const [x, y] = sc(...tag.top()); log.roi['b1.three'] = [x - 70, y - 30, x + 70, y + 120]; }
    const [b15x0, y15] = sc(X.bar15 - BAR_W / 2, top15), [b15x1] = sc(X.bar15 + BAR_W / 2, top15), [b30x1, y30] = sc(X.bar30 + BAR_W / 2, top30), [, y30b] = sc(X.bar30, 0);
    log.roi['b1.fifteen'] = [b15x0 - 10, y15 - 20, b15x1 + 10, y30b]; log.roi['b2.thirty'] = [b30x1 - 140, y30 - 20, b30x1 + 10, y30b];
    // S04 (C5 đạo diễn 12,5 s: hai nhãn lệch nhau): hai nhãn CÙNG cột ngay phải thanh 30 năm, mỗi nhãn ở độ cao đỉnh thanh của nó (tên trên, số dưới);
    // nhãn 15 năm có vạch nét đứt từ đỉnh thanh 15 năm (qua trên thanh 30 năm thấp hơn); tắt ở "gap"
    const s4 = b.b3.gap - 0.1, lx4 = b30x1 + 20, a15 = ok * show(t, b.b1.two, s4), rq = ok * show(t, b.b2.two, s4);
    seg2(O, b15x1 + 6, y15, lx4 - 10, y15, '#C9D1DC', 0.8 * a15, 3, [10, 8]);
    label(O, `${D('term_short')}:`, lx4, y15 - 64, { kind: 'number', px: 48, alpha: a15, claims: ['term_short'] });
    label(O, D('pay15_month'), lx4, y15 - 6, { kind: 'number', alpha: a15, claims: ['pay15_month'] });
    log.roi['b1.two'] = [lx4 - 10, y15 - 110, lx4 + 420, y15 + 10];
    label(O, `${D('term_long')} required:`, lx4, y30 - 6, { kind: 'number', px: 48, alpha: rq, claims: ['term_long'] });
    label(O, D('pay30_now'), lx4, y30 + 52, { kind: 'number', alpha: rq, claims: ['pay30_now'] });
    log.roi['b2.two'] = [lx4 - 10, y30 - 50, lx4 + 500, y30 + 70];
    // C5 (đạo diễn S05 2,65 s: hai thanh không nhãn): tên hai thanh căn giữa dưới chân, suốt mọi lúc ở đồ thị từ S04 tới hết S06 (chữ, không số tiền)
    { const nA = ok * show(t, MV.m_c1.t1 - 0.05, MV.m_w7.t0 - 0.05), [x15, yf] = sc(X.bar15, 0, BAR_D / 2), [x30] = sc(X.bar30, 0, BAR_D / 2);
      label(O, D('term_short'), x15, yf + 50, { align: 'center', kind: 'number', px: 48, color: '#C9CED6', alpha: nA, claims: ['term_short'] });
      label(O, D('term_long'), x30, yf + 50, { align: 'center', kind: 'number', px: 48, color: '#C9CED6', alpha: nA, claims: ['term_long'] }); }
    // S05: ngoặc đường lui (cushion) cạnh thanh 30 năm + nhãn phía trên hai thanh
    // vòng bố cục 1 (đạo diễn: không thấy ngoặc ở khung giữa S05): ngoặc + vạch mức 15 năm ĐỨNG cả S05 — qua đời Tessa (thế giới, cùng hộp
    // cushion 3D) tới "finishing"; ở thế giới nhãn chữ "fallback" (không số) cạnh ngoặc thay nhãn số
    // C4 r3: ngoặc + vạch sáng (cushion sáng, không cushion gốc tối) và đứng tới khi máy đổi chế độ ở S06 (không mờ dần ngay "finishing")
    const s5 = MV.m_w5.t0 - 0.05, bA = show(t, b.b3.gap, MV.m_c6.t0 - 0.05);
    vbrace(O, b30x1 + 26, y15, y30, '#4FD1B5', bA, 6, 16);
    seg2(O, b15x0 + 0.5 * (b30x1 - b15x0) - 60, y15, b30x1 + 26, y15, '#C9D1DC', 0.9 * bA, 3, [10, 8]);
    label(O, 'fallback', b30x1 + 46, (y15 + y30) / 2 + 16, { kind: 'name', px: 48, color: '#7FD8C4', alpha: bA * (1 - cw) * show(t, MV.m_w5.t0 + 0.3) });
    const lxC = (b15x0 + b30x1) / 2;
    label(O, `fallback: ${D('fallback_gap_now')} lower`, lxC, y15 - 135, { align: 'center', kind: 'number', alpha: ok * show(t, b.b3.six, s5), color: '#7FD8C4', claims: ['fallback_gap_now'] });
    label(O, `the least the ${D('term_long')} asks`, lxC, y15 - 72, { align: 'center', kind: 'number', alpha: ok * show(t, b.b3.least, s5), claims: ['term_long'] });
    log.roi['b3.gap'] = [b30x1 - 140, y15 - 10, b30x1 + 50, y30 + 10]; log.roi['b3.six'] = [lxC - 520, y15 - 180, lxC + 520, y15 - 120]; log.roi['b3.least'] = [lxC - 400, y15 - 115, lxC + 400, y15 - 60];
    log.roi['b4.repair'] = [b15x0 - 40, y15 - 220, b15x1 + 40, y15 + 10]; log.roi['b4.squeeze'] = [b15x0 - 10, y15 - 60, b15x1 + 10, y30b];
    log.roi['b5.short'] = [b30x1 - 140, y15 - 40, b30x1 + 10, y30 + 10];
    { const [hx, hy] = sc(hm.person.position.x, hm.h, hm.person.position.z); log.roi['b5.house'] = [hx - 90, hy - 90, hx + 90, hy + 60]; }
    { const fx = YX0 + YDX * (YT - 1), [x0, y0] = sc(fx - 0.2, 1.3, YZ), [x1, y1] = sc(fx + 0.5, 0, YZ); log.roi['b5.fifteen'] = [x0, y0, x1, y1]; }
    // S06 (C3 + sửa): "$2,828 a month" ở đầu trái vạch, C5 giữ tới hết S06 (đạo diễn 18,9 s: chồng đè/làm mất nhãn — chồng giờ ở phải thanh 30 năm);
    // "30-year paid in 15: $2,948 a month" đúng "two" (đầu con số), trên hai thanh; "+$120 a month" cạnh lát (tắt ở "Over": chỗ cho nhãn chồng)
    const [vx, vy] = sc(lx0, top15, LZ);
    label(O, D('pay15_month'), vx - 14, vy + 16, { align: 'right', kind: 'number', alpha: ok * show(t, MV.m_c6.t1 - 0.05, MV.m_w7.t0 - 0.05), claims: ['pay15_month'] });
    log.roi['b6.finishing'] = [...sc(lx0, top15 + 0.15, LZ), ...sc(lx1, top15 - 0.15, LZ)];
    // một khung cB cả S06 (C4 r3): nhãn $2,948 căn giữa trên hai thanh
    const [x48, y48] = sc((X.bar15 + X.bar30) / 2, G.pay30on15 * SCALE), yl = y48 - 92;
    label(O, `${D('term_long')} paid ${D('paid_in_short')}: ${D('pay30on15_now')}`, x48, yl, { align: 'center', kind: 'number', alpha: ok * show(t, b.b6.two, MV.m_w7.t0 - 0.05),
      claims: ['term_long', 'paid_in_short', 'pay30on15_now'] });
    log.roi['b6.two'] = [x48 - 520, yl - 50, x48 + 520, y48 + 10];
    const [xs, ys] = sc(X.bar30 + BAR_W / 2, top15 + sliver / 2);
    label(O, `+${D('extra_vs15_month_now')}`, xs + 26, ys + 18, { kind: 'number', px: 56, alpha: ok * show(t, b.b7.one, b.b8.over), claims: ['extra_vs15_month_now'] });
    log.roi['b7.one'] = [xs - 140, ys - 50, xs + 420, ys + 40];
    { const [hx, hy] = sc(X.bar30, top15 + sliver + HOVER + 0.1); log.roi['b7.same'] = [hx - 120, hy - 40, hx + 120, hy + 50]; }
    if (trail && ok) {   // vệt đường bay của bó mới nhất (warn mờ, nét đứt): nối đỉnh thanh 30 năm với bó
      const c = O.ctx; c.save(); c.globalAlpha = 0.35 * (1 - ease(trail.p, 0.75, 1)); c.strokeStyle = TRACK.warn; c.lineWidth = 4; c.setLineDash([10, 10]); c.beginPath();
      for (let i = 0; i <= 16; i++) { const [x, y, z] = path(trail.k, (trail.p * i) / 16), [qx, qy] = sc(x, y, z); i ? c.lineTo(qx, qy) : c.moveTo(qx, qy); }
      c.stroke(); c.restore();
    }
    // nhãn chồng (C5): canh trái từ mép trái chồng stack6, hai dòng trên đỉnh chồng (không chạm thanh 30 năm bên trái)
    const [kx, ky] = sc(X.stack6 - 0.45, 15 * BUNDLE_TH), stA = ok * show(t, b.b8.twenty, MV.m_w7.t0 - 0.05);
    label(O, `the stack: ${D('extra_vs15_total_now')}`, kx, ky - 80, { kind: 'number', alpha: stA, claims: ['extra_vs15_total_now'] });
    label(O, `extra paid over ${D('term_short_years')}`, kx, ky - 22, { kind: 'number', px: 48, alpha: stA, claims: ['term_short_years'] });
    // "Over": vật phản ứng ở từ khoá = lát RỜI đỉnh thanh 30 năm (mỗi 0,16 s một lát) — đo ở chỗ rời, không ở chỗ chồng nhận bó (chạm sau 0,6 s;
    // sync_audit +0,45 khi vùng đo gồm cả chồng)
    log.roi['b8.over'] = [...sc(X.bar30 - 0.7, top15 + sliver + HOVER + 0.45), ...sc(X.bar30 + 0.55, top15 - 0.2)]; log.roi['b8.twenty'] = [kx - 10, ky - 130, kx + 650, ky - 10];
    // S07.1 (thế giới): tên vật — không số
    { const [x, y0] = sc(X.stack, 15 * BUNDLE_TH + 0.2), y = Math.max(250, y0);   // máy gần: đỉnh chồng sát mép trên → nhãn không vào dải góc trên
      label(O, 'the stack = the price of the fallback', Math.min(Math.max(x, 590), 1330), y - 30, { align: 'center', kind: 'name', px: 48, alpha: show(t, b.b9.stack, MV.m_c7.t0) * (1 - cw), color: C.warn });
      log.roi['b9.stack'] = [x - 460, y - 80, x + 460, y + 250]; }
    // S07.2: chồng → khoảng giữa hai đường (warn: giá của đường lui), mốc tuần cuối, ngoặc + nhãn, lát vàng trong ngoặc
    if (t >= MV.m_c7.t0 && rAl > 0.01) {
      const P30 = S.rates.r30.map((r, i) => sc(rx(i), r * RY, 0.2)), P15 = S.rates.r15.map((r, i) => sc(rx(i), r * RY, 0.2)), c = O.ctx, u = ease(t, MV.m_c7.t0, b.c0.higher);
      const at = (A, B, i) => [mix(A[0], B[0], i / (nR - 1)), mix(A[1], B[1], i / (nR - 1))];   // điểm i trên cạnh A → B của mặt chồng
      c.save(); c.globalAlpha = rAl * mix(0.95, 0.3, u); c.fillStyle = C.warn; c.beginPath();
      for (let i = 0; i < nR; i++) { const s0 = at(SR[0], SR[1], i), x = mix(s0[0], P30[i][0], u), y = mix(s0[1], P30[i][1], u); if (i) c.lineTo(x, y); else c.moveTo(x, y); }
      for (let i = nR - 1; i >= 0; i--) { const s0 = at(SR[3], SR[2], i); c.lineTo(mix(s0[0], P15[i][0], u), mix(s0[1], P15[i][1], u)); }
      c.closePath(); c.fill(); c.restore();
      if (dr > 0) {
        // C5 (đạo diễn 12,4 s: đường không nhãn): tên mỗi đường ở đầu trái, cùng màu đường, từ "thirty-year" tới khi đẩy máy vào ngoặc
        const nmA = ok * show(t, b.c0.thirty, MV.m_rz.t0);
        label(O, `${D('term_long')} rate`, P30[0][0], P30[0][1] - 24, { kind: 'number', px: 48, alpha: nmA, color: '#A9C6FF', claims: ['term_long'] });
        label(O, `${D('term_short')} rate`, P15[0][0], P15[0][1] + 52, { kind: 'number', px: 48, alpha: nmA, color: C.ink, claims: ['term_short'] });
        const [ex, e30] = P30[nR - 1], [, e15] = P15[nR - 1], [, e0] = sc(rx(nR - 1), 0, 0.2), [bxB] = sc(RX1 + 0.32, 0, 0.2), oA = ok * show(t, b.c0.october, MV.m_out8.t0);
        seg2(O, ex, e30 - 34, ex, e0, C.muted, 0.8 * oA, 3, [8, 8]);
        if (oA > 0.01) { c.save(); c.globalAlpha = oA; for (const [yy, col] of [[e30, C.accent], [e15, C.ink]]) { c.fillStyle = col; c.beginPath(); c.arc(ex, yy, 9, 0, 7); c.fill(); } c.restore(); }
        label(O, `${D('term_long')}: ${D('r30_now')}`, bxB + 30, e30 - 14, { kind: 'number', px: 48, alpha: oA, color: '#A9C6FF', claims: ['term_long', 'r30_now'] });
        label(O, `${D('term_short')}: ${D('r15_now')}`, bxB + 30, e15 + 44, { kind: 'number', px: 48, alpha: oA, color: C.ink, claims: ['term_short', 'r15_now'] });
        // ngoặc ngay phải lát vàng (chân hướng trái); nhãn chênh canh phải, phía trên đầu hai đường
        const zA = ok * show(t, b.c0.zero, MV.m_out8.t0);
        vbrace(O, bxB, e30, e15, C.ink, zA, 5, 12);
        label(O, `${D('term_long')} rate ${D('spread_now')} higher`, ex - 20, e30 - 60, { align: 'right', kind: 'number', px: 48, alpha: zA, claims: ['term_long', 'spread_now'] });
        log.roi['c0.thirty'] = [P30[0][0], e30 - 40, ex, e0]; log.roi['c0.higher'] = [P30[0][0], e30, ex, e15 + 120]; log.roi['c0.october'] = [ex - 30, e30 - 50, bxB + 420, e15 + 60];
        log.roi['c0.zero'] = [ex - 820, e30 - 110, bxB + 10, e15 + 10];
        { const [sx0, sy0] = sc(SLX - 0.1, yGap + 0.9, 0.2), [sx1, sy1] = sc(SLX + 0.1, yGap - 0.25, 0.2); log.roi['c0.higher2'] = [sx0, sy0, sx1, sy1]; }
      }
    }
    // S08–S09: nhãn tháp
    const tl = (k) => { const [x, y] = sc(tw[k].position.x, tw[k].topY(n(T[k][2]))); return [x, y]; };
    // tháp 30 năm: nhãn ngay phải đỉnh của nó (trên đỉnh không đủ chỗ dưới dải nguồn); C5: hạ dưới vạch nét đứt đỉnh tháp (bóng phần chênh S08.2)
    { const [ax, ay] = tl('full'), [ax1] = sc(X.full + tw.full.halfW, 0), aA = ok * show(t, b.c1.four, MV.m_tops.t0);
      label(O, `${D('term_long')} on its own schedule:`, ax1 + 24, ay + 60, { kind: 'number', px: 48, alpha: aA, claims: ['term_long'] });
      label(O, `${D('interest_30full_now')} interest`, ax1 + 24, ay + 118, { kind: 'number', alpha: aA, claims: ['interest_30full_now'] });
      log.roi['c1.thirty'] = [ax - 160, ay - 20, ax + 160, sc(0, 0)[1]]; log.roi['c1.four'] = [ax1, ay + 10, ax1 + 900, ay + 135]; }
    // C5 (đạo diễn S08 12 s: tháp thấp chưa nhãn; S09 2,8 s: nhãn chỉ sai tháp): nhãn 30-trong-15 căn giữa NGAY TRÊN tháp của nó, tên ("30-year /
    // paid in 15:") hiện ở "fifteen", số ở "two"; ba dòng hẹp, cao hơn nhãn tháp 15 năm bên phải (không chạm), dây xuống đỉnh; tắt trước "stack"
    { const [bx, by] = tl('on15'), nm = ok * show(t, b.c2.fifteen, b.c3.stack - 0.4), bA2 = ok * show(t, b.c2.two, b.c3.stack - 0.4), yl = by - 102;
      label(O, D('term_long'), bx, yl - 116, { align: 'center', kind: 'number', px: 48, alpha: nm, claims: ['term_long'] });
      label(O, `paid ${D('paid_in_short')}:`, bx, yl - 58, { align: 'center', kind: 'number', px: 48, alpha: nm, claims: ['paid_in_short'] });
      label(O, D('interest_30on15_now'), bx, yl, { align: 'center', kind: 'number', alpha: bA2, claims: ['interest_30on15_now'] });
      seg2(O, bx, yl + 18, bx, by - 8, C.muted, 0.85 * nm, 3);
      log.roi['c2.fifteen'] = [bx - 200, yl - 160, bx + 200, sc(0, 0)[1]]; log.roi['c2.two'] = [bx - 160, yl - 50, bx + 160, yl + 20];
      // S08.2 (C5): vạch nét đứt ở mức đỉnh tháp 30 năm, từ mép phải tháp đó qua hết tháp 30-trong-15 (đỉnh của bóng phần chênh)
      const [fx1, yF] = sc(X.full + tw.full.halfW, yTopF), [ox1] = sc(X.on15 + tw.on15.halfW, yTopF);
      seg2(O, fx1 + 4, yF, ox1, yF, C.muted, 0.8 * gA, 3, [10, 8]);
      { const [, yb] = sc(X.on15, yTopB); log.roi['c2.gap'] = [fx1, yF - 10, ox1 + 10, yb]; } }
    // tháp 15 năm: tên + số căn giữa ngay trên đỉnh của nó (hai dòng)
    { const [cx, cy] = tl('y15'), cA = ok * show(t, b.c3.one, MV.m_w9.t0);
      label(O, `${D('term_short')}:`, cx, cy - 82, { align: 'center', kind: 'number', px: 48, alpha: cA, claims: ['term_short'] });
      label(O, `${D('interest_15_now')} interest`, cx, cy - 24, { align: 'center', kind: 'number', alpha: cA, claims: ['interest_15_now'] });
      log.roi['c3.fifteen'] = [cx - 200, cy - 20, cx + 200, sc(0, 0)[1]]; log.roi['c3.one'] = [cx - 260, cy - 75, cx + 260, cy - 5]; }
    // vạch nét đứt ở mức tháp 15 năm đứng yên; ngoặc + nhãn "difference = the stack" ĐI CÙNG khối khi nhấc (C4 r3)
    { const [bx0, yB] = sc(X.on15 - tw.on15.halfW, tw.on15.topY(nB) + LIFT * secU), [, yC0] = sc(X.on15, nC / 9 * BUNDLE_TH), [, yC] = sc(X.on15, nC / 9 * BUNDLE_TH + LIFT * secU);
      const [cx0] = sc(X.y15 - tw.y15.halfW, 0), dA = ok * show(t, b.c3.difference, MV.m_w9.t0 + 0.2), [bxc] = sc(X.on15, 0);
      seg2(O, cx0, yC0, bx0 - 6, yC0, C.muted, 0.75 * dA, 3, [10, 8]);
      vbrace(O, bx0 - 14, yB, yC, C.warn, dA, 6, -14);
      label(O, `difference = the stack: ${D('extra_vs15_total_now')}`, bxc, yB - 64, { align: 'center', kind: 'number', alpha: ok * show(t, b.c3.stack, MV.m_w9.t0 + 0.2), claims: ['extra_vs15_total_now'] });
      log.roi['c3.difference'] = [bx0 - 40, yB - 10, bx0 + 600, yC0 + 10]; log.roi['c3.stack'] = [bxc - 520, yB - 110, bxc + 520, yB - 50]; }
    // đường bay của khối (tâm khối, nét đứt warn mờ) + tên "the stack" (không số) theo khối ở thế giới
    if (secOn && secP > 0.001) {
      const c = O.ctx; c.save(); c.globalAlpha = 0.45; c.strokeStyle = C.warn; c.lineWidth = 4; c.setLineDash([10, 10]); c.beginPath();
      for (let i = 0; i <= 20; i++) { const [qx, qy] = sc(...secPos(7, secU, secP * i / 20)); i ? c.lineTo(qx, qy) : c.moveTo(qx, qy); }
      c.stroke(); c.restore();
    }
    { const [x, y, z] = secOn ? secPos(14, secU, secP) : [X.stack, 15 * BUNDLE_TH, 0], [nx, ny] = sc(x, y + 0.45, z);
      label(O, 'the stack', Math.min(Math.max(nx, 300), 1620), Math.max(250, ny), { align: 'center', kind: 'name', px: 48, color: C.warn,
        alpha: (1 - cw) * (t > MV.m_w9.t0 ? 1 : 0) * (1 - ease(t, S.land9 + 1.4, S.land9 + 1.7)) }); }
    { const [x, y] = sc(X.stack, 15 * BUNDLE_TH + 0.2); log.roi['c4.price'] = [x - 200, y - 40, x + 200, sc(X.stack, 0)[1]]; log.roi['c5.unusual'] = log.roi['c4.price']; log.roi['c5.normal'] = log.roi['c4.price']; }
    { const [x0, y0] = sc(X.bar15 - 0.6, top15 + 1.7), [x1, y1] = sc(X.bar15 + 0.6, top15 - 0.2), [, yb] = sc(X.bar15, 0);
      log.roi['c4.plus'] = [x0, y0, x1, y1]; log.roi['c4.fifteen'] = [x0, y1, x1, yb]; }
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
