// Tập 7 · C4 · ĐOẠN F = S25–S28. the bar (bản C3 s25-bar + sửa C4 + ghi chú đạo diễn C5): tờ đô la trả thêm từ tay Tessa chạm chỗ cạnh nhà đúng
// "charged", thanh (W3, ink-muted) trồi ra từ tường nhà sát sàn (trước mặt nhà) rồi dâng tới độ cao lãi, Tessa nghiêng nhìn theo → đồ thị: thước "zero"
// (sàn) → "7.40%" (độ cao thanh), "the bar: …", đồng lãi RỜI KHỎI NHÀ (trồi từ mái) rồi rơi xuống bị tờ đô la trên thanh chặn ("interest no longer
// charged"), bóng "any other use" + "not tested" đứng tách xa, lên xuống LIÊN TỤC qua độ cao thanh (không dừng ngang mép, KHÔNG vạch so ngang), nhãn đi
// theo bóng → lia sang lịch sử lãi 30 năm (cùng thang): CHÍNH thanh + tờ đô la co lại, trượt sang và cưỡi đầu đường, trục năm + vạch mờ 7.40%, thanh
// nhảy lên đỉnh 9.25% Nov 1994, xuống đáy 2.65% Jan 2021, về tuần cuối → vạch độ cao thanh của Tessa kẻ từ thanh qua cả lịch sử: đoạn cao hơn tô ấm,
// hình tỉ lệ 5 ô (≈ 1 tuần trong 5).
import { setup, figure, gesture, figTag, modeLook, followLight, chrome, SRC, SRC_SIM, label, seg2, dip,
  kf, show, pulse, C, ease, lin, mix, THREE, setOpacity } from '/episodes/ep007/world/c4kit.js';
import { Beam, Ribbon } from '/toolkit/factory/world/lib3d.js';
import { Bill } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c4/f-s25-s28/';
const PER_PCT = 0.3;                    // độ cao thế giới mỗi điểm % (C3)
const BOB = 0.45, BOB_T = 2.4;          // bóng: biên độ ĐỦ ngay từ đầu (đỉnh/đáy cách mép thanh ±1,5 điểm), chu kỳ
const RL = 0.7;                         // độ dài thanh khi cưỡi đường lịch sử (S26–S28)
const WARM = '#F5B971', DIM = '#2B4470';   // C5 S28: đoạn lãi cao hơn thanh (tô ấm) / phần còn lại; cùng hai màu cho hình tỉ lệ 5 ô

export async function boot(res) {
  const poses = {
    wB: { pos: [-4.6, 2.5, 7.6], tgt: [-0.4, 1.0, 0], fov: 38, chart: 0 },
    cB: { pos: [0.1, 1.45, 18], tgt: [0.1, 1.45, 0], fov: 19, chart: 1 },
    cH: { pos: [3.7, 2.2, 27.5], tgt: [3.7, 2.2, 0], fov: 20, chart: 1 },
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  // GX: bóng đứng tách xa đầu thanh (C4 r3: xa hơn — thước đứng giữa đầu thanh và bóng); WALL: tường phải của nhà (thanh trồi ra từ đó); BZ: thanh
  // trước mặt nhà (C5: máy thế giới thấy thanh trồi từ sàn sát tường)
  const b = cue, X = S.x, BX = X.bx, BL = X.bl, BZ = X.bz, GX = BX + BL / 2 + 2.3, N = S.r30.length;
  const hm = figure(scene, { x: X.house }), WALL = X.house + hm.w / 2;
  // S25.3: đồng lãi (costlier, đứng mặt về máy) — rời khỏi nhà, rơi xuống tờ đô la trên thanh, bị tờ chặn
  const coin = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.16, 0.04, 24), new THREE.MeshStandardMaterial({ color: C.costlier, emissive: new THREE.Color(C.costlier), emissiveIntensity: 0.45, transparent: true }));
  coin.rotation.x = Math.PI / 2; coin.castShadow = true; scene.add(coin); coin.userData.checks = { role: 'mark', key: 'interest-coin' };
  const beam = Beam({ length: BL }); beam.scale.set(1, 2.2, 1.4); scene.add(beam); beam.userData.checks = { role: 'mark', series: 'bar', key: 'the-bar' };
  const d1 = Bill({ name: 'extra-dollar' }), d2 = Bill({ name: 'any-other-use' }); scene.add(d1, d2);
  setOpacity(d2, 0.28);
  const hand = [hm.person.position.x + 0.35, 0.62, hm.person.position.z + 0.15], [land0, land1] = S.dollar1.place;
  const hx = (i) => X.h0 + (i + 0.5) * (X.h1 - X.h0) / N, RP = (i) => [hx(i), S.r30[i] * PER_PCT];
  // C5 S26 (PHỤ 5,8 s) / S27: thanh nhảy theo lời — lên đỉnh ở "nine", xuống đáy ở "low", về tuần cuối sau "two" (trước lặng số neo S28)
  const HOPS = [[b.b1.nine, S.i.max], [b.b2.low, S.i.min], [b.b2.two + 1.4, N - 1]];
  const line = Ribbon({ color: C.accent, z: 0.1, width: 0.06, maxPts: N }); scene.add(line); line.userData.checks = { role: 'series', series: 'r30', key: 'rate-30-history' };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    // thanh (C4 r3): TRỒI RA TỪ TƯỜNG NHÀ sát sàn (0,33 s, xong ngay trước "charged" để tờ chạm), rồi dâng dọc tường tới độ cao lãi ở "rate"
    // C5: ở máy thế giới thanh đứng trước mặt nhà (BZ); về z 0 trong lúc đổi chế độ (máy đang chạy) → bố cục đồ thị giữ nguyên như C4 r4
    const up = ease(t, b.a0.charged - 0.35, b.a0.charged - 0.02), Hb = kf(S.bar, t) * PER_PCT, H = Math.max(0.06, Hb), BZt = BZ * (1 - ease(t, MV.m_c25.t0, MV.m_c25.t1));
    // C5 S26: CHÍNH thanh này (cùng tờ đô la) co lại và trượt sang đầu đường lịch sử trong lúc lia (không còn thanh đứng yên bên trái), cưỡi đầu
    // đường lúc vẽ, rồi nhảy theo lời (HOPS)
    const sl = ease(t, MV.m_pan.t0, b.b0.moves), dr = lin(t, b.b0.moves, b.b0.moves + 1.4) * (N - 1), m = Math.floor(dr);
    const cr = Math.min(N - 1, dr), ry = (Math.floor(cr) < N - 1 ? mix(S.r30[Math.floor(cr)], S.r30[Math.ceil(cr)], cr - Math.floor(cr)) : S.r30[N - 1]) * PER_PCT;
    let rp = [hx(cr), ry], rv = ry / PER_PCT;
    if (t >= b.b0.moves + 1.4) {
      let fr = N - 1, to = N - 1, hk = 1;
      for (const [tt, i] of HOPS) if (t >= tt) { fr = to; to = i; hk = ease(t, tt, tt + 0.5); }
      const [x0, y0] = RP(fr), [x1, y1] = RP(to);
      rp = [mix(x0, x1, hk), mix(y0, y1, hk) + 0.6 * Math.sin(Math.PI * hk)]; rv = S.r30[hk < 0.5 ? fr : to];
    }
    const bxC = mix(WALL + BL * up / 2, rp[0], sl), byC = mix(H, rp[1], sl), bzC = mix(BZt, 0.12, sl);
    beam.scale.x = Math.max(0.001, up * mix(1, RL / BL, sl)); beam.position.set(bxC, byC, bzC); beam.visible = up > 0.01;
    beam.userData.checks.value = +mix(kf(S.bar, t), rv, sl).toFixed(3);
    // C5 S28 (PHỤ): loé mạnh hơn, lâu hơn ở "Tessa's"
    beam.glow(Math.max(0.6 * Math.max(pulse(t, b.a3.bar, 1.0), 0.6 * pulse(t, b.a3.measured, 0.9), pulse(t, b.b0.taken, 1.0)), pulse(t, b.b3.tessa, 1.6)), C.ink);
    // tờ 1: trong tay Tessa → bay vòng, CHẠM mặt thanh đúng "charged", cưỡi theo thanh (cả khi thanh trượt sang lịch sử)
    const a1 = show(t, S.dollar1.appear), x1 = ease(t, land0, land1), top = [mix(BX - 0.5, rp[0], sl), byC + 0.22, bzC];
    d1.rotation.x = (Math.PI / 2) * Math.max(x1, 0.35);
    d1.position.set(mix(hand[0], top[0], x1), mix(hand[1], top[1], x1) + 1.0 * Math.sin(Math.PI * x1), mix(hand[2], top[2], x1) + 1.0 * Math.sin(Math.PI * x1));
    d1.scale.setScalar(Math.max(0.001, a1)); d1.visible = a1 > 0.01;
    // đồng lãi (C5: rời khỏi nhà, hết vệt đỏ 14,5 s do đồng bắt đầu ngoài khung): trồi từ trong mái nhà ở coin[0] ("return"), bay vòng lên qua đầu thanh
    // rồi rơi xuống, CHẠM đỉnh tờ đô la trên thanh ở coin[1] ("interest", nảy nhẹ), nằm đó, mờ ở "pays"
    const cP = [top[0], H + 0.52, BZt + 0.05], cS = [X.house + 0.3, 1.2, 0], cu = lin(t, S.coin[0], S.coin[1]);
    const ca = ease(t, S.coin[0] - 0.05, S.coin[0] + 0.15) * (1 - ease(t, S.coin[2], S.coin[2] + 0.5));
    coin.position.set(mix(cS[0], cP[0], cu), mix(cS[1], cP[1], cu) + 1.1 * Math.sin(Math.PI * cu) + 0.08 * Math.sin(Math.PI * Math.min(1, Math.max(0, (t - S.coin[1]) / 0.25))),
      mix(cS[2], cP[2], Math.min(1, 3 * cu)));
    coin.material.opacity = ca; coin.visible = ca > 0.01;
    // tờ 2 (bóng): hiện tại chỗ ở "other", lên xuống LIÊN TỤC với biên độ đủ ngay từ đầu (qua độ cao thanh ở tốc độ lớn nhất, đứng lại chỉ ở đỉnh/đáy
    // cách mép ±1,5 điểm); mờ đi khi lia sang lịch sử — vẫn đang chuyển động
    const a2 = show(t, S.dollar2.appear) * (1 - ease(t, MV.m_pan.t0, MV.m_pan.t0 + 0.8)), bob = BOB * Math.sin((2 * Math.PI * (t - S.dollar2.appear)) / BOB_T);
    const p2 = [GX, Hb + bob, BZt + 0.05];
    d2.rotation.x = Math.PI / 2; d2.position.set(...p2); d2.scale.setScalar(Math.max(0.001, a2)); d2.visible = a2 > 0.01;
    // S26: lịch sử lãi 30 năm (cùng thang 0,3/điểm), vẽ ở "moves"; S28 đoạn cao hơn thanh tô ấm (C5), phần còn lại tối
    const fw = t > b.b3.only + 0.4;
    const pts = []; for (let i = 0; i <= m; i += 2) pts.push([hx(i), S.r30[i] * PER_PCT, fw ? (S.r30[i] >= G.bar - 1e-9 ? WARM : DIM) : C.accent]);
    if (m < N - 1 && dr > m) pts.push([hx(dr), mix(S.r30[m], S.r30[m + 1], dr - m) * PER_PCT]);
    if (pts.length > 1) line.set(pts); line.visible = pts.length > 1;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));   // mở hồi 3 sau khoảng giữ MR2
    figTag(O, hm);
    const sc = (x, y, z = 0) => O.toScreen(x, y, z), s25 = MV.m_pan.t0 - 0.05;
    const [bx0, by] = sc(BX - BL / 2, Hb, BZt), [bx1] = sc(BX + BL / 2, Hb, BZt), [, fy] = sc(BX, 0, BZt), bc = (bx0 + bx1) / 2;
    { const [x, y] = sc(...hand); log.roi['a0.dollar'] = [x - 80, y - 80, x + 80, y + 80]; }
    log.roi['a0.charged'] = [bx0 - 20, by - 40, bx1 + 20, fy + 10];
    // THƯỚC (C4 r3, đạo diễn #2): vạch đo đứng ink-muted ở đầu PHẢI thanh, từ sàn tới thanh; khắc "zero" ở sàn và MỘT khắc "7.40%" đúng độ cao thanh
    { const [dx] = sc(BX + BL / 2 + 0.22, 0, BZt), a = ok * (t < s25 + 0.3 ? 1 - ease(t, s25, s25 + 0.3) : 0), c = O.ctx;
      if (a > 0.01) { c.save(); c.globalAlpha = a; c.strokeStyle = C.muted; c.lineWidth = 4; c.beginPath(); c.moveTo(dx, fy); c.lineTo(dx, by);
        c.moveTo(dx - 18, fy); c.lineTo(dx + 18, fy); c.moveTo(bx1 + 4, by); c.lineTo(dx + 18, by); c.stroke(); c.restore(); }
      label(O, 'zero', dx + 26, fy + 16, { kind: 'name', px: 48, color: C.muted, alpha: a });
      label(O, D('r30_now'), dx + 26, by + 16, { kind: 'number', px: 48, alpha: a, claims: ['r30_now'] });
      log.roi['a1.scale'] = [dx - 30, by - 10, dx + 30, fy + 10]; }
    // khối 1: the bar (trên thanh; tắt khi đồng lãi bắt đầu bay qua chỗ đó); khối 2: MỘT dòng dưới nửa phải thanh
    const L1x = bc - 120, L1y = by - 150;
    label(O, `the bar: ${D('bar_now')}`, L1x, L1y, { align: 'center', kind: 'number', alpha: ok * show(t, b.a1.seven, S.coin[0] - 0.1), claims: ['bar_now'] });
    log.roi['a1.seven'] = [L1x - 520, L1y - 64, L1x + 520, L1y + 16];
    // C4 r3b: dưới nửa phải thanh, trái thước (verify F-2: nhãn cũ ở phải-trên bị viền bóng 'any other use' cắt khi bóng lên)
    label(O, 'interest no longer charged', bx1 - 10, by + 74, { align: 'right', kind: 'compare', px: 48, alpha: ok * show(t, b.a2.investment, s25) });
    log.roi['a2.investment'] = [bx1 - 700, by + 20, bx1 - 10, by + 90];
    { const [x0, y0] = sc(...cS), [x1, y1] = sc(...cP), [, ya] = sc((cS[0] + cP[0]) / 2, (cS[1] + cP[1]) / 2 + 1.1, cP[2]);
      log.roi['a2.return'] = [x0 - 60, y0 - 60, x0 + 60, y0 + 60];
      log.roi['a2.interest'] = [Math.min(x0, x1) - 40, ya - 40, Math.max(x0, x1) + 40, Math.max(y0, y1) + 40]; log.roi['a2.pays'] = [x1 - 50, y1 - 50, x1 + 50, y1 + 50]; }
    log.roi['a3.bar'] = [bx0 - 20, by - 40, bx1 + 20, by + 40];
    // bóng: viền nét đứt (cùng cỡ tờ thật) + nhãn "any other use" ĐI THEO bóng (ngay dưới bóng); "not tested" ngay dưới nhãn đó ở "How" (cue whether)
    const [gx, gy] = sc(...p2), n4 = ok * show(t, b.a4.whether, s25);
    if (a2 > 0.01) {
      const q = [[-0.31, -0.14], [0.31, -0.14], [0.31, 0.14], [-0.31, 0.14]].map(([u, v]) => sc(p2[0] + u * a2, p2[1] + v * a2, p2[2] + 0.02)), c = O.ctx;
      c.save(); c.globalAlpha = a2; c.strokeStyle = C.ink; c.lineWidth = 3; c.setLineDash([9, 7]); c.beginPath();
      q.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.closePath(); c.stroke(); c.restore();
    }
    label(O, 'any other use', 1810, gy + 76, { align: 'right', kind: 'name', px: 48, alpha: a2 });
    label(O, 'not tested', 1810, gy + 136, { align: 'right', kind: 'compare', px: 48, color: C.muted, alpha: n4 * Math.min(1, a2 / 0.9) });
    log.roi['a4.whether'] = [1300, gy + 30, 1810, gy + 150];
    { const [x0, y0] = sc(GX - 0.5, Hb + BOB + 0.3, BZt), [x1, y1] = sc(GX + 0.5, Hb - BOB - 0.3, BZt); log.roi['a3.other'] = [x0, y0, x1, y1];
      // "measured": KHÔNG vạch so ngang (C4 r2, C3 câu 5: vạch ngang độ cao thanh mời đọc "phải vượt mốc") — cue hình = thanh loé nhẹ, bóng vẫn lên xuống
      log.roi['a3.measured'] = [bx0 - 20, y0, x1, y1]; }
    // S26–S28: lịch sử
    const [h0x, hy0] = sc(X.h0, 0, 0.1), [h1x] = sc(X.h1, 0, 0.1), [, gy7] = sc(X.h0, G.bar * PER_PCT, 0.1);
    log.roi['b0.moves'] = [h0x, sc(0, 3.0)[1], h1x, hy0]; log.roi['b0.taken'] = log.roi['b0.moves'];
    // C5 S26/S28: trục năm ở sàn của lịch sử — khắc không chữ mỗi 5 năm (dài hơn ở năm chẵn chục), chữ chỉ ở hai đầu (claim); vạch mờ ở độ cao thanh
    // của Tessa + "7.40%" bên trái (mốc để đọc đường lãi, không phải vạch "phải vượt")
    { const a = ok * show(t, b.b0.moves), c = O.ctx;
      if (a > 0.01) { c.save(); c.globalAlpha = 0.7 * a; c.strokeStyle = C.muted; c.lineWidth = 3; c.beginPath(); c.moveTo(h0x, hy0); c.lineTo(h1x, hy0);
        for (const [i, big] of [[0, true], ...S.yt, [N - 1, true]]) { const [x] = sc(hx(i), 0, 0.1); c.moveTo(x, hy0); c.lineTo(x, hy0 + (big ? 18 : 10)); }
        c.stroke(); c.restore(); }
      label(O, D('first_week_short'), h0x, hy0 + 70, { kind: 'number', px: 48, color: C.muted, alpha: a, claims: ['first_week_short'] });
      label(O, D('last_week_month'), h1x, hy0 + 70, { align: 'right', kind: 'number', px: 48, color: C.muted, alpha: a, claims: ['last_week_month'] });
      seg2(O, h0x, gy7, h1x, gy7, C.muted, 0.3 * a, 2, [6, 10]);
      label(O, D('r30_now'), h0x - 16, gy7 + 16, { align: 'right', kind: 'number', px: 48, color: C.muted, alpha: a, claims: ['r30_now'] }); }
    const mk = (i, at, z, s, cl, lx, ly, align) => {
      const [x, y] = sc(hx(i), S.r30[i] * PER_PCT, 0.1), a = ok * show(t, at, z), c = O.ctx;
      if (a > 0.01) { c.save(); c.globalAlpha = a; c.fillStyle = C.ink; c.beginPath(); c.arc(x, y, 10, 0, 7); c.fill(); c.restore(); }
      seg2(O, x, y + (ly < y ? -14 : 14), x, ly + (ly < y ? 14 : -50), C.ink, 0.8 * a, 3);
      return [x, y];
    };
    { const [x, y] = mk(S.i.max, b.b1.high, b.b3.only - 0.1, '', null, 0, 410);
      // C5 S27 (PHỤ): nhãn đỉnh lùi xuống (mờ bớt) khi lời sang đáy, để không tranh mắt
      label(O, `highest: ${D('r30_max')} · ${D('r30_max_week_short')}`, Math.max(500, x), 392, { align: 'center', kind: 'number', alpha: ok * show(t, b.b1.nine, b.b3.only - 0.1) * (1 - 0.55 * ease(t, b.b2.low, b.b2.low + 0.4)), claims: ['r30_max', 'r30_max_week_short'] });
      log.roi['b1.high'] = [x - 30, y - 30, x + 30, y + 30]; log.roi['b1.nine'] = [x - 380, 340, x + 380, 410]; }
    { const [x, y] = mk(S.i.min, b.b2.low, b.b3.only - 0.1, '', null, 0, 800);
      label(O, `lowest: ${D('r30_min')} · ${D('r30_min_week_short')}`, 1810, 790, { align: 'right', kind: 'number', alpha: ok * show(t, b.b2.two, b.b3.only - 0.1), claims: ['r30_min', 'r30_min_week_short'] });
      log.roi['b2.low'] = [x - 30, y - 30, x + 30, y + 30]; log.roi['b2.two'] = [1100, 740, 1810, 805]; }
    // S28: vạch độ cao thanh của Tessa kẻ TỪ THANH (đã về tuần cuối) sang trái qua cả lịch sử, xong trong 0,4 s (C5 PHỤ: vẽ xong trước 0,6 s)
    { const [ex, ey] = sc(hx(N - 1) - RL / 2, G.bar * PER_PCT, 0.1), a = ok * show(t, b.b3.only);
      seg2(O, ex - 4, ey, mix(ex - 4, h0x, lin(t, b.b3.only, b.b3.only + 0.4)), ey, C.muted, 0.9 * a, 4, [14, 10]);
      log.roi['b3.only'] = [h0x, ey - 40, ex, ey + 40]; }
    label(O, `weeks with a bar this high: ${D('share_r30_ge_now')}`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, b.b3.one), claims: ['share_r30_ge_now'] });
    log.roi['b3.one'] = [300, 150, 1620, 230];
    // C5 S28: "1 in 5" bằng hình — năm ô tuần ngay dưới nhãn, ô đầu sáng ấm (cùng màu đoạn cao hơn thanh) ở "five"
    { const a = ok * show(t, b.b3.one), lit = ease(t, b.b3.five - 0.05, b.b3.five + 0.25), W = 46, GP = 14, x0 = 960 - (5 * W + 4 * GP) / 2, y0 = 240, c = O.ctx;
      if (a > 0.01) { c.save(); c.globalAlpha = a; c.strokeStyle = C.muted; c.lineWidth = 2;
        for (let k = 0; k < 5; k++) { const x = x0 + k * (W + GP); c.fillStyle = DIM; c.fillRect(x, y0, W, W); c.strokeRect(x, y0, W, W); }
        c.globalAlpha = a * lit; c.fillStyle = WARM; c.fillRect(x0, y0, W, W); c.restore(); }
      log.roi['b3.five'] = [x0, y0, x0 + 5 * W + 4 * GP, y0 + W]; }
    { const [x, y] = sc(bxC, byC, bzC); log.roi['b3.tessa'] = [x - 200, y - 40, x + 200, y + 40]; }
    chrome(O, { src: t < MV.m_pan.t0 ? SRC_SIM(D) : SRC });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
