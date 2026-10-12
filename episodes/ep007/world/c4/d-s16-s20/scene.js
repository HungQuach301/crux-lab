// Tập 7 · C4 · ĐOẠN D = S16–S20. Hàng chồng theo tuần (đoạn c) tách bốn nhóm thập kỷ; trước mỗi nhóm một chồng điển hình (W2, bó của the stack);
// đường lãi 30 năm (accent, dải thấp sát sàn) chạy dọc hàng: lãi tụt mạnh vào 2010s trong khi chồng 2010s cao hơn 1990s (vạch nét đứt) → bốn ngoặc khoảng chênh
// (V6, cùng thang cột khoảng chênh của đoạn c) khớp chồng, không khớp đường lãi → 2020s gần ngang the stack của Tessa → giữ đồ thị tới hết đoạn. Mốc giờ: spine.json.
// C5 (vòng sửa đạo diễn): máy thế giới gần + chính diện hơn, khe nhóm rộng; chồng điển hình CÙNG SÀN với the stack (z = 0, hàng tuần lùi ra sau trong
// cú đổi chế độ); đường lãi (đúng số, có chú giải) vào cùng nhãn lãi đầu tiên ở S16 "fifteen"; ngoặc theo lời S19; chồng 2020s mọc ở S19; không về thế giới (đoạn e mở ở "Back").
import { setup, figure, gesture, figTag, WeekRow, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, vbrace, dip,
  show, pulse, C, ease, lin, mix, setOpacity, THREE } from '/episodes/ep007/world/c4kit.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep007/world/c4/d-s16-s20/';
// vòng bố cục 1 (verify CHẶN F-2: đường lãi xuyên thẻ thập kỷ): đường lãi nằm ở DẢI THẤP sát sàn (py ≈ 740–840 ở 1080, sau bốn chồng),
// thẻ thập kỷ là khối 3 dòng (tên · giá · khoảng chênh) PHÍA TRÊN chồng, ngoặc và vạch của Tessa → không đường nào đi qua chữ.
// C5: đường lãi ở z RZ (sau chồng điển hình z 0 ± 0,3, trước hàng tuần đã lùi về ROWZ ± 0,11) → chồng che đường, đường không xuyên chồng
const RB = 0.1375, RY = 0.133, RZ = -0.37, ROWZ = -0.55;
const cl = (x) => Math.min(1, Math.max(0, x)), bell = (t, a, d) => Math.sin(Math.PI * cl((t - a) / d));   // nhô một lần rồi về 0

export async function boot(res) {
  const poses = {
    // C5 CHÍNH S16 1,1 s ("không thấy bốn nhóm"): gần + chính diện hơn (cũ: xiên 50°, hàng thu nhỏ về một góc) — Tessa, nhà, the stack và cả bốn nhóm vừa khung
    wD0: { pos: [-3.1, 4.3, 15.2], tgt: [1.0, 2.05, 0], fov: 36, chart: 0 },
    // lùi nhẹ + dời phải (≈ 110 px/đơn vị ở chồng, sàn py ≈ 899): khối thẻ 2020s và 2010s không chạm nhau, chồng 2020s trong vùng an toàn
    cD: { pos: [2.6, 3.264, 26], tgt: [2.6, 3.264, 0], fov: 22.39, chart: 1 },
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, X = S.x, N = S.weeks.length, W = X.x1 - X.x0, U = BUNDLE_TH / G.bundle_usd, H = S.hot;
  const GS = G.stack_total * U / S.spread_now, dec = (i) => (i < S.rng[1][0] ? 0 : i < S.rng[2][0] ? 1 : i < S.rng[3][0] ? 2 : 3);
  const hm = figure(scene, { x: X.house }), tstack = theStack(scene, G, { x: X.stack });
  stackSet(tstack, G.stack_total);
  const row = WeekRow(scene, S.extra, { x0: X.x0, width: W, z: 0.05, depth: 0.22, unit: U });
  const xc = (k) => X.x0 + (S.rng[k][0] + S.rng[k][1]) / 2 / N * W, xw = (i) => X.x0 + (i + 0.5) * W / N;
  // tách nhóm (= spine.py xc): nhóm k dời k·split, cả hàng nén lại trong [x0, x1] → khe rộng mà đầu trái không lấn the stack
  const shift = (x, k) => k * X.split - (x - X.x0) * 3 * X.split / W, xg = (k) => xc(k) + shift(xc(k), k);
  const stacks = [0, 1, 2, 3].map((k) => theStack(scene, G, { x: xg(k), z: X.zs }));
  stacks.forEach((s, k) => { s.userData.checks = { role: 'bar', series: 'era-median', key: `era-stack-${k}` }; s.children[0].material.emissive = new THREE.Color(C.warn); });
  const l30 = Ribbon({ color: C.accent, z: RZ, width: 0.055, maxPts: N }), l10 = Ribbon({ color: '#9CC0FF', z: RZ + 0.02, width: 0.11, maxPts: N });
  scene.add(l30, l10); l30.userData.checks = { role: 'series', series: 'r30', key: 'rate-30' };
  const LAB = [[D('era1991_span'), D('era1991_median_r30'), D('era1991_median_extra_total'), ['era1991_span', 'era1991_median_r30'], 'era1991_median_extra_total', D('era1991_median_spread'), 'era1991_median_spread'],
    [D('era2000_name'), D('era2000_median_r30'), D('era2000_median_extra_total'), ['era2000_name', 'era2000_median_r30'], 'era2000_median_extra_total', D('era2000_median_spread'), 'era2000_median_spread'],
    [D('era2010_name'), D('era2010_median_r30'), D('era2010_median_extra_total'), ['era2010_name', 'era2010_median_r30'], 'era2010_median_extra_total', D('era2010_median_spread'), 'era2010_median_spread'],
    [D('era2020_name'), null, D('era2020_median_extra_total'), ['era2020_name'], 'era2020_median_extra_total', D('era2020_median_spread'), 'era2020_median_spread']];
  // thẻ (tên · giá) ở từ số; số khoảng chênh ở "seven"/"four"; NGOẶC đi trước theo lời (S.brk: "against" · "zero" lần 2 · "2010s" · "2020s")
  const tagAt = [b.e1.fifteen, b.e2.fourteen, b.e3.twenty, b.e6.one], brAt = [b.e4.four, b.e4.four + 0.25, b.e4.seven, b.e4.seven + 0.25];
  const cW = new THREE.Color(C.warn), cWd = new THREE.Color('#4A3F2A');

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    // tách ở "decade" (bắt đầu sớm 0,3 s: đã rõ bốn nhóm ở ~1,1 s); hàng tuần lùi ra sau trong cú đổi chế độ (5 s đầu không đổi)
    const sp = ease(t, b.e0.decade - 0.3, b.e0.decade + 0.35), dx = (i) => shift(xw(i), dec(i)) * sp;
    row.mesh.position.z = ROWZ * ease(t, MV.m_c16.t0, MV.m_c16.t1);
    // nhóm đang nói sáng (1990s từ chữ "1990s"), nhóm khác tối hẳn (C5 PHỤ S17: nền tranh mắt); thế giới: tông xen kẽ theo nhóm; S19 cả bốn như nhau
    const cur = t < H.y1990s ? -1 : t < S.up[1] ? 0 : t < S.up[2] ? 1 : t < b.e4.gap ? 2 : t < b.e6.twenty ? 9 : 3;
    // từ S19 ý là BỐN CHỒNG + ngoặc: hàng tuần mờ hẳn (nền sạch cho thẻ, ngoặc) tới hết đoạn
    const rowA = 1 - 0.85 * ease(t, b.e4.gap - 0.3, b.e4.gap + 0.5);
    row.set({ grow: 1, dx, a: rowA, color: (i, c) => { const d = dec(i), on = cur === -1 ? 0.55 + 0.2 * sp * (d % 2 ? -1 : 1) : cur === 9 ? 0.55 : d === cur ? 1 : 0.18; c.copy(cWd).lerp(cW, on); } });
    // chồng điển hình dâng ở từ khoá; 2010s dâng tới mức 2000s, ĐỨNG, vượt lên ở "more" (C5 CHÍNH S18); "wider" chồng 2010s/2020s chỉ SÁNG (cao = số)
    const wb = bell(t, b.e5.wider, 1.4);
    stacks.forEach((s, k) => stackSet(s, (k === 2 ? S.med[1] * ease(t, S.up[2], S.up[2] + 1.1) + (S.med[2] - S.med[1]) * ease(t, b.e3.more, b.e3.more + 0.7)
      : S.med[k] * ease(t, S.up[k], S.up[k] + 1.1))));
    stacks.forEach((s, k) => { s.children[0].material.emissiveIntensity = k >= 2 ? 0.55 * wb : 0; });   // "wider": chồng 2010s/2020s SÁNG lên, cao giữ đúng số
    // the stack của Tessa không nhãn ở đồ thị → mờ còn 30 % tới "Tessa's" (C5 PHỤ S17)
    setOpacity(tstack, 1 - 0.7 * cw * (1 - ease(t, b.e6.tessa - 0.1, b.e6.tessa + 0.4)));
    // đường lãi 30 năm, dải thấp sát sàn (dời theo nhóm), LUÔN đúng số (chỉ vẽ dần + loé, không dời điểm). Đoạn 1990s vào CÙNG nhãn "rate near" ở S16
    // "fifteen" (chữ lãi không đứng một mình); S17 "lower" vẽ tiếp đoạn 2000s (loé); S18 "far" vẽ nhanh đoạn 2010s = đường RƠI DỐC xuống mức thật (C5 CHÍNH);
    // 2020s vào cùng ngoặc 2020s; S19 "lower" đoạn 2010s loé dày (nhấn, không nhúng); tắt ở S20 "twenty"
    const pr = [lin(t, b.e1.fifteen, b.e1.fifteen + 0.5), lin(t, b.e2.lower, b.e2.lower + 0.6), lin(t, b.e3.far, b.e3.far + 0.5), lin(t, b.e4.b2020, b.e4.b2020 + 0.4)];
    const hd = t < b.e2.t0 ? 0 : t < b.e3.t0 ? 1 : 2, pts = [], ph = [];
    for (let i = 0; i < N; i += 2) {
      const d = dec(i); if ((i - S.rng[d][0]) / (S.rng[d][1] - S.rng[d][0]) > pr[d]) break;
      const p = [xw(i) + dx(i), RB + S.r30[i] * RY]; pts.push(p); if (d === hd) ph.push(p);
    }
    const rA = ease(t, b.e1.fifteen - 0.05, b.e1.fifteen + 0.2) * (1 - ease(t, b.e6.twenty - 0.2, b.e6.twenty + 0.4));
    l30.set(pts); l30.visible = rA > 0.01 && pts.length > 1; l30.material.opacity = rA * (0.75 + 0.25 * pulse(t, b.e5.lower, 1.0));
    const hA = rA * [pulse(t, b.e1.fifteen, 1.6), pulse(t, b.e2.lower, 1.6), Math.max(pulse(t, b.e3.far, 1.6), bell(t, b.e5.lower, 1.6))][hd];
    l10.set(ph, 0.11 + 0.07 * bell(t, b.e5.lower, 1.6)); l10.visible = hA > 0.01 && ph.length > 1; l10.material.opacity = hA;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));
    figTag(O, hm);
    const sc = (x, y, z = 0) => O.toScreen(x, y, z), [, yF] = sc(X.x0, 0, X.zs), [xL] = sc(X.x0, 0, 0.05), [xR] = sc(X.x1, 0, 0.05), end = S.total + 1;
    const top = (k) => sc(stacks[k].position.x, S.med[k] * U, X.zs);
    // khung bố cục (px 1080, chỉ đọc khi ở đồ thị): ngoặc k = cạnh TRÁI chồng k (0,62), lề ×1,07 trên đỉnh ngoặc; đường của Tessa = đỉnh the stack.
    // Đáy khối thẻ k (anchor) = trên đỉnh chồng, đỉnh ngoặc và vạch của Tessa → ba dòng (tên y−142 · giá y−86 · khoảng chênh y−30) không bị
    // đường nào cắt; dây dẫn mảnh từ đáy khối xuống đỉnh chồng (chồng thấp: khối nổi cao hơn đỉnh)
    const bxOf = (k) => stacks[k].position.x - 0.62, [sx, sy] = sc(X.stack + 0.45, G.stack_total * U, 0), [tx] = sc(X.stack, 0);
    const anchor = (k) => Math.min(top(k)[1], sc(bxOf(k), S.spd[k] * GS * 1.07, X.zs)[1], sy - 14) - 8;
    const tagX = (k) => { const x = top(k)[0]; return k === 0 ? x + 30 : k === 3 ? Math.min(x, 1684) : x; };   // 1990s: xa dây nối của Tessa; 2020s: trong vùng an toàn
    const [, rTop] = sc(0, RB + 9.5 * RY, RZ), [, rBot] = sc(0, RB + 2.5 * RY, RZ);
    log.roi['e0.decade'] = [xL, sc(0, 3.6)[1], xR, yF];
    // nhãn trên (thập kỷ đang nói: tên + lãi) + khối thẻ trên mỗi chồng điển hình (giữ tới hết). Bỏ dòng "typical stack …" trên cùng: giá đã ở thẻ (C5 PHỤ S16/S18)
    for (let k = 0; k < 4; k++) {
      const [name, rate, usd, cl3, cu] = LAB[k], nx = k < 3 ? S.up[k + 1] - 0.1 : end, [x, y] = top(k), ay = anchor(k), xt = tagX(k);
      log.roi[['e1.typical', 'e2.y2000s', 'e3.y2010s', 'e6.twenty'][k]] = [x - 70, y - 20, x + 70, yF];
      if (k < 3) {
        // 2010s tắt hẳn trước khi "typical gap…" hiện cùng chỗ (verify WARN 29 s: hai nhãn chồng lúc chuyển)
        const z = k === 2 ? b.e4.gap - 0.4 : nx;
        label(O, `${name}: rate near ${rate}`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, tagAt[k], z), claims: cl3 });
        log.roi[['e1.fifteen', 'e2.fourteen', 'e3.twenty'][k]] = [500, 150, 1420, 230];
      }
      const ta = ok * show(t, tagAt[k], end);
      label(O, name, xt, ay - 142, { align: 'center', kind: 'number', px: 48, alpha: ta, claims: [cl3[0]] });
      label(O, usd, xt, ay - 86, { align: 'center', kind: 'number', px: 48, alpha: ta, claims: [cu] });
      seg2(O, x, ay - 4, x, y - 6, C.muted, 0.6 * ta, 2);
    }
    // vạch nét đứt ở đỉnh chồng 1990s (dưới mọi khối thẻ): S17 "same" nối sang đỉnh chồng 2000s (≈ bằng, C5 CHÍNH); S18 "yet" kéo tiếp tới chồng 2010s
    // (chồng đang đứng ở mức 2000s, dưới vạch), "more" chồng vượt vạch
    { const [x0, y0] = top(0), [x1] = top(1), [x2] = top(2), a = ok * show(t, b.e2.same, b.e4.gap - 0.1);
      const xe = t < b.e3.yet ? mix(x0 + 55, x1 + 60, lin(t, b.e2.same, b.e2.same + 0.5)) : mix(x1 + 60, x2 + 60, lin(t, b.e3.yet, b.e3.yet + 0.5));
      seg2(O, x0 + 55, y0, xe, y0, C.ink, 0.85 * a, 4, [14, 10]);
      log.roi['e2.same'] = [x0, y0 - 30, x1 + 70, y0 + 30]; log.roi['e3.yet'] = [x1, y0 - 30, x2 + 70, y0 + 30]; log.roi['e3.more'] = [x2 - 70, y0 - 60, x2 + 70, y0 + 30];
      log.roi['e2.lower'] = [xL, rTop - 10, sc(xg(1) + 2.6, 0)[0], rBot + 10];
      log.roi['e3.far'] = [sc(xg(2) - 1.5, 0)[0], rTop - 10, sc(xg(2) + 1.5, 0)[0], rBot + 10]; }
    // chú giải đường lãi (C5 CHÍNH S16: đường không chú giải) — góc dưới phải, TRÊN dải tối chân trang (C14 1080p: ở y 990 bị dải chân che còn 2:1)
    { const a = ok * Math.min(1, 20 * rA); seg2(O, 1380, 863, 1440, 863, C.accent, a, 6);   // C5 1080 C14: chú giải đi theo độ mờ của đường (đường cố ý mờ) → 2,0:1; chú giải hiện đủ khi đường còn thấy
      label(O, `${D('term_long')} rate`, 1460, 880, { align: 'left', kind: 'number', px: 48, alpha: a, claims: ['term_long'] }); }
    // S19: bốn ngoặc khoảng chênh (accent) sát cạnh trái mỗi chồng điển hình, hiện theo lời; số khoảng chênh = dòng thứ ba của khối thẻ (cùng màu ngoặc)
    label(O, `typical gap: ${D('term_long')} minus ${D('term_short')} rate`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, b.e4.gap, b.e6.twenty - 0.1), claims: ['term_long', 'term_short'] });
    log.roi['e4.gap'] = [400, 150, 1520, 230];
    for (let k = 0; k < 4; k++) {
      // cao ngoặc = đúng khoảng chênh (dữ liệu): "moved" rung NGANG, "wider" (C5 CHÍNH S19) ngoặc 2010s/2020s NỞ = nét dày + chân dài, chồng sáng cùng lúc
      const w2 = k >= 2 ? wb : 0, bx = bxOf(k), h = S.spd[k] * GS, jx = 5 * Math.sin(12 * (t - b.e7.moved)) * pulse(t, b.e7.moved, 1.4);
      const [x0, y0] = sc(bx, 0, X.zs), [, y1] = sc(bx, h, X.zs), x = x0 + jx, a = ok * show(t, S.brk[k], end), aL = ok * show(t, brAt[k], end), ay = anchor(k), xt = tagX(k);
      vbrace(O, x, y1, y0, C.accent, a * (0.8 + 0.2 * Math.max(w2, pulse(t, b.e5.wider, 1.0))), 6 + 6 * w2, -14 - 12 * w2);
      label(O, LAB[k][5], xt, ay - 30, { align: 'center', kind: 'number', px: 48, color: '#A9C6FF', alpha: aL, claims: [LAB[k][6]] });
      if (k !== 1) log.roi[['e4.against', , 'e4.b2010', 'e4.b2020'][k]] = [x - 20, y1 - 10, x + 120, y0];   // ngoặc 2000s: mốc 'zero' lần 2 (S.brk), không cue
      if (k === 2) log.roi['e4.seven'] = [x - 20, ay - 80, xt + 150, y0];
      if (k === 0) log.roi['e4.four'] = [x - 20, ay - 80, xt + 150, y0];
    }
    log.roi['e5.lower'] = [xL, rTop - 10, xR, rBot + 10]; log.roi['e5.wider'] = [xL, sc(0, 3.0, X.zs)[1], xR, yF];
    // S20: 2020s; vạch từ đỉnh the stack sang chồng 2020s (gần ngang, dưới mọi khối thẻ). Bỏ tiêu đề "2020s: typical stack …" (lặp số, C5 PHỤ)
    log.roi['e6.one'] = [tagX(3) - 120, anchor(3) - 180, tagX(3) + 120, anchor(3) - 60];
    { const [x3] = top(3), a = ok * show(t, b.e6.tessa, end);
      seg2(O, sx, sy, mix(sx, x3 + 60, lin(t, b.e6.tessa, b.e6.tessa + 0.7)), sy, C.ink, 0.85 * a, 4, [14, 10]);
      seg2(O, tx, 367, tx, sy - 30, C.ink, 0.8 * a, 3);
      label(O, "Tessa's stack · ILLUSTRATIVE", 130, 350, { align: 'left', kind: 'name', alpha: a, char: 'Tessa' });
      log.roi['e6.tessa'] = [sx - 120, sy - 30, x3 + 70, sy + 30]; }
    // S20.2: dòng góc gạch chân ("history, not a forecast")
    { const c = O.ctx; c.save(); c.font = '600 54px Inter'; const w0 = c.measureText('US only · ').width, wAll = c.measureText('US only · history, not a forecast').width; c.restore();
      seg2(O, 96 + w0, 1024, 96 + wAll, 1024, C.ink, 0.9 * show(t, b.e7.history, end), 4); log.roi['e7.history'] = [96 + w0 - 6, 960, 96 + wAll + 6, 1030]; }
    log.roi['e7.moved'] = [sc(stacks[0].position.x - 0.8, 0)[0], sc(0, 3.0, X.zs)[1], xR, yF];
    // "where it goes" (C5 CHÍNH S20): ngoặc MA sau đầu phải hàng (chưa có tuần) — nét đứt mờ, cao dao động giữa khoảng chênh 2000s và 2010s (không biết trước)
    { const g = 0.55 * ok * show(t, b.e7.where), bx = X.x1 + 0.35, hh = mix(S.spd[1], S.spd[2], 0.5 + 0.5 * Math.sin(2 * Math.PI * (t - b.e7.where) / 1.6)) * GS;
      const [x, y0] = sc(bx, 0, X.zs), [, y1] = sc(bx, hh, X.zs);
      seg2(O, x - 14, y1, x, y1, C.accent, g, 5); seg2(O, x, y1, x, y0, C.accent, g, 5, [10, 10]); seg2(O, x - 14, y0, x, y0, C.accent, g, 5);
      log.roi['e7.where'] = [x - 30, sc(bx, S.spd[2] * GS * 1.1, X.zs)[1], x + 20, y0]; }
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
