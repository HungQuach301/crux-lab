// Tập 7 · C4 · ĐOẠN D = S16–S20. Hàng chồng theo tuần (đoạn c) tách bốn nhóm thập kỷ; trước mỗi nhóm một chồng điển hình (W2, bó của the stack);
// đường lãi 30 năm (accent) chạy qua hàng: lãi tụt mạnh vào 2010s trong khi chồng 2010s cao hơn 1990s (vạch nét đứt) → bốn ngoặc khoảng chênh
// (V6, cùng thang cột khoảng chênh của đoạn c) khớp chồng, không khớp đường lãi → 2020s gần ngang the stack của Tessa → về thế giới. Mốc giờ: spine.json.
import { setup, figure, gesture, figTag, WeekRow, theStack, stackSet, BUNDLE_TH, modeLook, followLight, chrome, label, seg2, vbrace, dip,
  show, pulse, C, ease, lin, mix, THREE } from '/episodes/ep007/world/c4kit.js';
import { Ribbon } from '/toolkit/factory/world/lib3d.js';

const SEG = '/episodes/ep007/world/c4/d-s16-s20/';
const RY = 0.35;

export async function boot(res) {
  const poses = {
    wD0: { pos: [-7.4, 2.9, 10.4], tgt: [1.8, 1.2, -0.8], fov: 46, chart: 0 },
    cD: { pos: [2.2, 3.0, 26], tgt: [2.2, 3.0, 0], fov: 20.6, chart: 1 },
    wEnd: { pos: [-7.6, 2.6, 7.6], tgt: [-2.4, 1.0, 0], fov: 38, chart: 0 },
  };
  const { S, D, G, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, X = S.x, N = S.weeks.length, W = X.x1 - X.x0, U = BUNDLE_TH / G.bundle_usd;
  const GS = G.stack_total * U / S.spread_now, dec = (i) => (i < S.rng[1][0] ? 0 : i < S.rng[2][0] ? 1 : i < S.rng[3][0] ? 2 : 3);
  const hm = figure(scene, { x: X.house }), tstack = theStack(scene, G, { x: X.stack });
  stackSet(tstack, G.stack_total);
  const row = WeekRow(scene, S.extra, { x0: X.x0, width: W, z: 0.05, depth: 0.22, unit: U });
  const xc = (k) => X.x0 + (S.rng[k][0] + S.rng[k][1]) / 2 / N * W, xw = (i) => X.x0 + (i + 0.5) * W / N;
  const stacks = [0, 1, 2, 3].map((k) => theStack(scene, G, { x: xc(k) + (k - 1.5) * X.split, z: X.zs }));
  stacks.forEach((s, k) => { s.userData.checks = { role: 'bar', series: 'era-median', key: `era-stack-${k}` }; });
  const l30 = Ribbon({ color: C.accent, z: 0.6, width: 0.055, maxPts: N }), l10 = Ribbon({ color: '#9CC0FF', z: 0.62, width: 0.11, maxPts: N });
  scene.add(l30, l10); l30.userData.checks = { role: 'series', series: 'r30', key: 'rate-30' };
  const LAB = [[D('era1991_span'), D('era1991_median_r30'), D('era1991_median_extra_total'), ['era1991_span', 'era1991_median_r30'], 'era1991_median_extra_total', D('era1991_median_spread'), 'era1991_median_spread'],
    [D('era2000_name'), D('era2000_median_r30'), D('era2000_median_extra_total'), ['era2000_name', 'era2000_median_r30'], 'era2000_median_extra_total', D('era2000_median_spread'), 'era2000_median_spread'],
    [D('era2010_name'), D('era2010_median_r30'), D('era2010_median_extra_total'), ['era2010_name', 'era2010_median_r30'], 'era2010_median_extra_total', D('era2010_median_spread'), 'era2010_median_spread'],
    [D('era2020_name'), null, D('era2020_median_extra_total'), ['era2020_name'], 'era2020_median_extra_total', D('era2020_median_spread'), 'era2020_median_spread']];
  const tagAt = [b.e1.fifteen, b.e2.fourteen, b.e3.twenty, b.e6.one], brAt = [b.e4.four, b.e4.four + 0.25, b.e4.seven, b.e4.seven + 0.25];
  const cW = new THREE.Color(C.warn), cWd = new THREE.Color('#4A3F2A');

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw); gesture(hm, t, S.gestures);
    const sp = ease(t, b.e0.decade - 0.05, b.e0.decade + 0.9), dx = (i) => (dec(i) - 1.5) * X.split * sp;
    // nhóm đang nói sáng; S19 cả bốn như nhau; sau S20 về thế giới cả hàng tối nhẹ
    const cur = t < S.up[0] ? -1 : t < S.up[1] ? 0 : t < S.up[2] ? 1 : t < b.e4.gap ? 2 : t < S.up[3] ? 9 : 3;
    row.set({ grow: 1, dx, color: (i, c) => { const d = dec(i), on = cur === -1 || cur === 9 ? 0.55 : d === cur ? 1 : 0.3; c.copy(cWd).lerp(cW, on); } });
    stacks.forEach((s, k) => stackSet(s, S.med[k] * ease(t, S.up[k], S.up[k] + 1.1)));
    // đường lãi 30 năm qua hàng (dời theo nhóm); đoạn 2010s loé ở "far" (lãi thấp hẳn) và "lower"
    const pts = [], p10 = []; for (let i = 0; i < N; i += 2) { const p = [xw(i) + dx(i), S.r30[i] * RY]; pts.push(p); if (dec(i) === 2) p10.push(p); }
    const rA = ease(t, b.e0.decade, b.e0.decade + 0.8) * (1 - ease(t, MV.m_w20.t0, MV.m_w20.t0 + 0.5));
    l30.set(pts); l30.visible = rA > 0.01; l30.material.opacity = rA * (0.75 + 0.25 * pulse(t, b.e5.lower, 1.0));
    const hA = rA * Math.max(pulse(t, b.e3.far, 1.6), pulse(t, b.e5.lower, 1.2)); l10.set(p10); l10.visible = hA > 0.01; l10.material.opacity = hA;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));
    figTag(O, hm);
    const sc = (x, y, z = 0) => O.toScreen(x, y, z), [, yF] = sc(X.x0, 0, X.zs), [xL] = sc(X.x0, 0, 0.05), [xR] = sc(X.x1, 0, 0.05), end = MV.m_w20.t0 - 0.05;
    const top = (k) => sc(stacks[k].position.x, S.med[k] * U, X.zs);
    log.roi['e0.decade'] = [xL, sc(0, 3.6)[1], xR, yF];
    // nhãn trên (thập kỷ đang nói) + thẻ trên mỗi chồng điển hình (giữ tới hết)
    for (let k = 0; k < 4; k++) {
      const [name, rate, usd, cl, cu, , ] = LAB[k], nx = k < 3 ? S.up[k + 1] - 0.1 : end, [x, y] = top(k);
      log.roi[['e1.typical', 'e2.y2000s', 'e3.y2010s', 'e6.twenty'][k]] = [x - 70, y - 20, x + 70, yF];
      if (k < 3) {
        label(O, `${name}: rate near ${rate}`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, tagAt[k], k === 2 ? b.e4.gap - 0.1 : nx), claims: cl });
        label(O, `typical stack ${usd}`, 960, 268, { align: 'center', kind: 'number', alpha: ok * show(t, tagAt[k], k === 2 ? b.e4.gap - 0.1 : nx), claims: [cu] });
        log.roi[['e1.fifteen', 'e2.fourteen', 'e3.twenty'][k]] = [500, 150, 1420, 290];
      }
      const ta = ok * show(t, tagAt[k], end), xt = Math.min(x, 1715);   // 2020s: thẻ không chạm mép phải vùng an toàn
      label(O, name, xt, y - 74, { align: 'center', kind: 'number', px: 48, alpha: ta, claims: [cl[0]] });
      label(O, usd, xt, y - 18, { align: 'center', kind: 'number', px: 48, alpha: ta, claims: [cu] });
    }
    // S18 "more": vạch nét đứt từ đỉnh chồng 1990s sang chồng 2010s
    { const [x0, y0] = top(0), [x2] = top(2), a = ok * show(t, b.e3.more, b.e4.gap - 0.1);
      seg2(O, x0 + 55, y0, mix(x0 + 55, x2 + 60, lin(t, b.e3.more, b.e3.more + 0.5)), y0, C.ink, 0.85 * a, 4, [14, 10]);
      log.roi['e3.more'] = [x0, y0 - 30, x2 + 70, y0 + 30]; log.roi['e3.far'] = [sc(xc(2) - 1.5, 0)[0], sc(0, 2.0)[1], sc(xc(2) + 1.5, 0)[0], sc(0, 1.0)[1]]; }
    // S19: bốn ngoặc khoảng chênh (accent) bên trái mỗi chồng điển hình + thẻ
    label(O, `typical gap: ${D('term_long')} minus ${D('term_short')} rate`, 960, 205, { align: 'center', kind: 'number', alpha: ok * show(t, b.e4.gap, S.up[3] - 0.1), claims: ['term_long', 'term_short'] });
    log.roi['e4.gap'] = [400, 150, 1520, 230];
    for (let k = 0; k < 4; k++) {
      const bx = stacks[k].position.x - 0.62, h = S.spd[k] * GS * (1 + 0.06 * Math.sin(12 * (t - b.e7.moved)) * pulse(t, b.e7.moved, 1.4));
      const [x, y0] = sc(bx, 0, X.zs), [, y1] = sc(bx, h, X.zs), a = ok * show(t, brAt[k], end);
      vbrace(O, x, y1, y0, C.accent, a * (0.8 + 0.2 * pulse(t, b.e5.wider, 1.0)), 6 + 3 * pulse(t, b.e5.wider, 1.0), -14);
      label(O, LAB[k][5], x - 18, (y0 + y1) / 2 + 16, { align: 'right', kind: 'number', px: 48, color: '#A9C6FF', alpha: a, claims: [LAB[k][6]] });
      if (k === 2) log.roi['e4.seven'] = [x - 300, y1 - 10, x + 20, y0];
      if (k === 0) log.roi['e4.four'] = [x - 300, y1 - 10, x + 20, y0];
    }
    log.roi['e5.lower'] = [xL, sc(0, 3.4)[1], xR, sc(0, 0.8)[1]]; log.roi['e5.wider'] = [xL, sc(0, 3.0, X.zs)[1], xR, yF];
    // S20: 2020s; vạch từ đỉnh the stack sang chồng 2020s (gần ngang); nhãn
    label(O, `${D('era2020_name')}: typical stack ${D('era2020_median_extra_total')}`, 960, 268, { align: 'center', kind: 'number', alpha: ok * show(t, b.e6.one, end), claims: ['era2020_name', 'era2020_median_extra_total'] });
    log.roi['e6.one'] = [500, 215, 1420, 290];
    { const [sx, sy] = sc(X.stack + 0.45, G.stack_total * U, 0), [x3] = top(3), a = ok * show(t, b.e6.tessa, end), [tx] = sc(X.stack, 0);
      seg2(O, sx, sy, mix(sx, x3 + 60, lin(t, b.e6.tessa, b.e6.tessa + 0.7)), sy, C.ink, 0.85 * a, 4, [14, 10]);
      seg2(O, tx, 352, tx, sy - 30, C.ink, 0.8 * a, 3);
      label(O, "Tessa's stack · ILLUSTRATIVE", 130, 335, { align: 'left', kind: 'name', alpha: a, char: 'Tessa' });
      log.roi['e6.tessa'] = [sx - 120, sy - 30, x3 + 70, sy + 30]; }
    // S20.2: dòng góc gạch chân ("history, not a forecast")
    { const c = O.ctx; c.save(); c.font = '600 54px Inter'; const w0 = c.measureText('US only · ').width, wAll = c.measureText('US only · history, not a forecast').width; c.restore();
      seg2(O, 96 + w0, 1024, 96 + wAll, 1024, C.ink, 0.9 * show(t, b.e7.history, MV.m_w20.t1), 4); log.roi['e7.history'] = [96 + w0 - 6, 960, 96 + wAll + 6, 1030]; }
    log.roi['e7.moved'] = [sc(stacks[0].position.x - 0.8, 0)[0], sc(0, 3.0, X.zs)[1], xR, yF];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
