// Tập 6 · C4 · ĐOẠN E = S24–S29 (Hồi 3). Ba cột [người][séc][hàng 10 thùng] (Edna · Ruth · Carl, như C3 s29) + hàng séc đều của Carl (S25).
// S24 Carl (port C3 s24 + lượt đạo diễn: thanh giá mọc ở "fastest") · S25 43,1 % / 29,0 % · S26 dải 1960s · S27 Edna (port C3 s27 + mốc năm, phần chồng
// accent) · S28 Ruth 85, một năm · S29 ba người (port C3 s29 + máy gần hơn, "month" loé). Mốc giờ chỉ từ spine.json.
import * as THREE from 'three';
import { setup, column, showColumn, hideColumn, setCheck, checkLabel, nameTag, rowBox, modeLook, followLight, chrome, brace, label, seg2, dip, kf, show, pulse,
  CHAR, NAME, C, ease, lin, mix, rgba } from '/episodes/ep006/world/c4kit.js';

const SEG = '/episodes/ep006/world/c4/e-s24-s29/';
const SZ = { size: 0.42, gap: 0.05, cw: 0.46, cbase: 0.8 };
const INSET = { x0: 1420, x1: 1800, y0: 220, y1: 400, v0: 0.88, v1: 1.06 };   // ô nhỏ S24.6 (thiết kế 1920×1080): năm 0 → 20, sức mua 88 % → 106 %
const AX = { y0: 1946, y1: 1989, x0: 200, x1: 1720, eY: 318, cY: 400, h: 36 };   // trục thời gian S27 (cBoth)

export async function boot(res) {
  const poses = {
    wRuth: { pos: [-3.0, 2.2, 7.8], tgt: [-0.7, 0.5, 0], fov: 35, chart: 0 },
    wCarl: { pos: [3.0, 2.2, 7.8], tgt: [5.3, 0.5, 0], fov: 35, chart: 0 },
    cCarl: { pos: [6.7, 0.85, 26], tgt: [6.7, 0.85, 0], fov: 14, chart: 1 },     // FIX-R1: lùi + hạ tâm — nhãn dưới hàng cách dải chân trang ≥ 60 px, đỉnh thanh giá dưới dải nhãn góc
    cCarl2: { pos: [9.2, 1.1, 35], tgt: [9.2, 1.1, 0], fov: 14, chart: 1 },      // FIX-R1: người Carl → hàng séc đều trọn trong [96, 1824]
    wEdna: { pos: [-8.8, 2.2, 7.8], tgt: [-6.5, 0.5, 0], fov: 35, chart: 0 },
    cEdna: { pos: [-6.2, 1.0, 22], tgt: [-6.2, 1.0, 0], fov: 14, chart: 1 },     // FIX-R1: người Edna không còn cắt mép trái
    cBoth: { pos: [-0.2, 2.6, 47], tgt: [-0.2, 2.6, 0], fov: 14, chart: 1 },     // FIX-R1: người Edna → hàng Carl trọn trong [96, 1824]
    cRuth: { pos: [0.6, 1.05, 22], tgt: [0.6, 1.05, 0], fov: 14, chart: 1 },
    wThree: { pos: [-1.6, 2.3, 12.9], tgt: [-0.6, 0.8, 0], fov: 50, chart: 0 },  // S29 giữ ý hình C3; FIX-R1 chỉ sửa mép: tên/người Edna trong khung
    cThree: { pos: [-0.2, 2.74, 46.3], tgt: [-0.2, 2.74, 0], fov: 14, chart: 1 },
  };
  const { S, CL, X, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses, ['/episodes/ep006/world/grid.json']);
  const G = X[0], b = cue, L = S.label_cues;
  const cols = {
    edna: column(scene, { x: -5.6, name: 'edna', ...SZ }),
    ruth: column(scene, { x: 0.4, name: 'ruth', ...SZ }),
    carl: column(scene, { x: 6.4, name: 'carl', ...SZ }),
  };
  const lev = column(scene, { x: 13.2, name: 'carlLevel', who: 'carl', person: false, level: true, ...SZ });
  // FIX-R1: cột vẽ SAU sàn. Sàn trong suốt, xếp theo khoảng cách: cột đang hiện/mờ dần (không ghi độ sâu) ở xa hơn gốc sàn bị sàn vẽ đè mất
  // cả cột, chỉ còn bóng (khung gần trống 334 s, 386 s ở lượt C4)
  for (const c of [...Object.values(cols), lev]) for (const g of [c.row, c.card, c.person]) if (g) g.traverse((o) => { o.renderOrder = 2; });
  // S24.3: thanh GIÁ (accent) cạnh hàng của Carl — mọc ×(1 + 6,38 %)^20 trong câu "fastest price rise"
  const pg = new THREE.BoxGeometry(0.5, 1, 0.4); pg.translate(0, 0.5, 0);
  const price = new THREE.Mesh(pg, new THREE.MeshStandardMaterial({ color: C.accent, emissive: new THREE.Color(C.accent), emissiveIntensity: 0.3, roughness: 0.6, transparent: true }));
  price.position.set(9.4, 0, 0); price.castShadow = true; price.renderOrder = 2; scene.add(price); price.userData.checks = { role: 'bar', key: 'prices-carl', series: 'prices' };
  const starts = G.cpiu20.map((r) => r[0]), v20 = G.cpiu20.map((r) => r[1]), iC = starts.indexOf('1966-01');
  const cnt = (Y, t) => Y.filter((y) => t >= y).length;
  const yr = (y) => AX.x0 + (AX.x1 - AX.x0) * (y - AX.y0) / (AX.y1 - AX.y0);
  const ix = (k) => INSET.x0 + (INSET.x1 - INSET.x0) * k / 20, iy = (v) => INSET.y1 - (INSET.y1 - INSET.y0) * (v - INSET.v0) / (INSET.v1 - INSET.v0);
  const M = MV, R = S.reset;
  const six = S.words.find((w) => w.sid === 'S24.3' && w.w === 'six').s;   // lời đọc số 6.38%

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    // hiện/mờ từng cột theo cảnh (FIX-R1: cột không nói tới ẩn hẳn, mờ/hiện DẦN trong cú máy — không còn mẩu hàng 0,18 cắt mép khung):
    // Carl mọc trong cú lia S24 (không khung trống), Ruth tắt dần trong cú lia; Edna từ cú về thế giới S27; Ruth lướt qua giữa cú bay S26 → S27;
    // Edna/Carl tắt trong cú lia về Ruth (S28); S29 cả ba hiện dần trong cú về thế giới
    const fin = (m) => ease(t, m.t0, m.t1), fout = (m) => 1 - ease(t, m.t0, m.t1);
    const cA = ease(t, M.m_pan24.t0, b.b1.carl + 0.2), three = t >= M.m_w29.t0;
    const W7 = M.m_w27, pass = ease(t, W7.t0 + 0.15, W7.t0 + 0.45) * (1 - ease(t, W7.t1 - 0.35, W7.t1));
    const aR = three ? 1 : t < W7.t0 ? 1 - ease(t, M.m_pan24.t0 + 0.3, M.m_pan24.t1 + 0.2) : t < M.m_pan28.t0 ? pass : fin(M.m_pan28);
    const aE = three ? fin(M.m_w29) : t < M.m_w27.t0 ? 0 : fin(M.m_w27) * fout(M.m_pan28);
    const aC = three ? fin(M.m_w29) : t < W7.t1 ? cA * (1 - ease(t, W7.t0 + 0.4, W7.t1)) : ease(t, b.d3.carl - 0.05, b.d3.carl + 0.8) * fout(M.m_pan28);
    for (const [id, c] of Object.entries(cols)) {
      const a = id === 'ruth' ? aR : id === 'carl' ? aC : aE;
      // đặt lại hiện/ẩn mỗi khung: setOpacity ẩn cả lưới con khi a ≈ 0 mà không ai bật lại khi a về 1 — khung phụ thuộc thứ tự render
      // (worker render cảnh S27 sau một cảnh có Edna ẩn → thẻ + hàng Edna mất 394–404 s ở lượt C4)
      hideColumn(c, 1);
      c.row.set({ value: kf(S.rows[id], t), appear: id === 'carl' ? (t < M.m_pan24.t1 + 1 ? cA : 1) : 1,
        pulse: id === 'carl' ? pulse(t, b.b5.never, 0.8) + pulse(t, b.c2.helped, 0.8) + pulse(t, b.d4.start, 1.4) : id === 'edna' ? pulse(t, b.d4.end, 1.2) + pulse(t, b.f0.edna, 0.6) : pulse(t, b.e0.losing, 0.9) });
      setCheck(c, S, t, 1);
      showColumn(c, a); if (a < 0.999) hideColumn(c, a);
    }
    const lvA = show(t, b.c1.level, M.m_w27.t0);
    hideColumn(lev, 1);
    lev.row.set({ value: kf(S.rows.carlLevel, t), appear: lvA }); setCheck(lev, S, t, lvA); if (lvA < 0.999) hideColumn(lev, lvA);
    // FIX-R1: thanh giá mọc suốt "fastest price rise of any stretch" tới số ("six"), mang nhãn của nó cạnh đỉnh; tắt trước "less … before"
    const pgA = show(t, b.b2.fastest, b.b4.before - 0.35), pgh = ease(t, b.b2.fastest, six);
    price.scale.y = Math.max(0.001, SZ.cbase * Math.pow(S.price_growth, pgh)); price.material.opacity = pgA; price.visible = pgA > 0.01;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    // tên trên đầu (thế giới) — màu nhận diện
    for (const [id, c] of Object.entries(cols)) nameTag(O, c, (id === 'ruth' ? aR : id === 'carl' ? aC : aE) * (1 - cw));
    const Cc = cols.carl, RC = rowBox(O, Cc, kf(S.rows.carl, t));
    // ===== S24 (cCarl)
    const s24 = M.m_pan25.t0 - 0.1;
    // FIX-R1: "rising check: 43.1%" hiện ĐÚNG lúc lời đọc ("forty-three") ở chỗ dưới hàng của Carl và đi theo hàng suốt cú lia S25 (trước: tắt rồi
    // hiện lại sau cú lia, trễ 3 s); nhãn dưới hàng ở yb + 76 / yb + 166 — cách dải chân trang
    if (t < M.m_w27.t1) label(O, L['c0.forty'], (RC.x0 + RC.x1) / 2, RC.yb + 76, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.c0.forty, M.m_w27.t0) });
    if (t < M.m_pan25.t1) {
      label(O, L['b1.january'], 120, 330, { kind: 'number', px: 48, w: 600, color: CHAR.carl, alpha: ok * show(t, M.m_c24.t1, b.b5.ruths) });
      const [pxl, pyt] = O.toScreen(price.position.x - 0.25, price.scale.y, 0.2);
      label(O, L['b2.fastest'], pxl - 24, pyt + 36, { align: 'right', kind: 'number', px: 48, alpha: ok * show(t, six, b.b4.before - 0.35) });
      label(O, L['b4.before'], 120, 228, { kind: 'compare', px: 48, alpha: ok * show(t, b.b4.before, b.b5.never) });
      checkLabel(O, Cc, L['b3.check'], ok * show(t, b.b3.check, b.b4.every), { dx: 14 });
      const tA = ok * show(t, b.b3.first, b.c0.forty - 0.35);
      brace(O, RC.x0, RC.x1, RC.yb + 22, C.muted, tA, 5, -14);
      label(O, L['b3.first'], RC.x0, RC.yb + 76, { kind: 'number', px: 48, alpha: tA, color: C.muted });
      const k = cnt(S.years.carl, t);
      if (k >= 1 && t < b.b5.ruths) label(O, `year ${k}`, RC.x1, RC.yt - 30, { align: 'right', kind: 'number', px: 52, alpha: ok * (1 - show(t, b.b5.ruths - 0.3)) });
      const yA = ok * show(t, S.years.carl[19] + 0.25, b.c0.forty - 0.35);
      brace(O, RC.x0, RC.xl, RC.yb + 112, C.ink, yA, 5, -14);
      label(O, L['b4.y20'], RC.x0, RC.yb + 166, { kind: 'number', px: 48, alpha: yA });
      log.roi['b4.every'] = [RC.x0 - 10, RC.yt - 80, RC.x1 + 10, RC.yb + 10]; log.roi['b3.first'] = [RC.x0 - 10, RC.yb, RC.x1 + 10, RC.yb + 100];
      log.roi['b2.fastest'] = [pxl - 900, pyt - 10, pxl + 120, pyt + 60]; log.roi['c0.forty'] = [RC.x0 - 10, RC.yb + 30, RC.x1 + 10, RC.yb + 100];
      // ô nhỏ S24.6: vạch séc đầu + đường của Ruth — năm 1–15 đậm (lên lại), cuối mờ (lượt đạo diễn C3); FIX-R1: thanh giá đã tắt, bớt chữ trong ô
      const iA = ok * show(t, b.b5.ruths, s24), d = lin(t, b.b5.ruths, b.b5.ruths + 1.2);
      if (iA > 0.01) {
        const c = O.ctx, P = S.ruth_path, n = Math.max(1, Math.round(d * 20));
        seg2(O, ix(0), iy(1), ix(20), iy(1), C.muted, iA, 4);
        c.save(); c.lineCap = 'round';
        for (let j = 1; j <= n; j++) { c.globalAlpha = iA * (j <= 15 ? 1 : 0.35); c.strokeStyle = CHAR.ruth; c.lineWidth = j <= 15 ? 7 : 4;
          c.beginPath(); c.moveTo(ix(j - 1), iy(P[j - 1])); c.lineTo(ix(j), iy(P[j])); c.stroke(); }
        c.restore();
        label(O, 'Ruth · ILLUSTRATIVE:', INSET.x1, 470, { align: 'right', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: iA });
        label(O, 'back above in early years', INSET.x1, 530, { align: 'right', kind: 'compare', px: 48, alpha: iA });
        label(O, "Carl's: never", INSET.x1, 590, { align: 'right', kind: 'compare', px: 48, color: CHAR.carl, alpha: ok * show(t, b.b5.never, s24) });
        log.roi['b5.ruths'] = [INSET.x0 - 300, INSET.y0 - 20, INSET.x1 + 10, 545]; log.roi['b5.never'] = [RC.x0 - 10, RC.yt - 20, INSET.x1 + 10, 610];
      }
    }
    // ===== S25–S26 (cCarl2)
    if (t > M.m_pan25.t0 && t < M.m_w27.t1) {
      const RL = rowBox(O, lev, kf(S.rows.carlLevel, t));
      label(O, L['c1.twenty'], (RL.x0 + RL.x1) / 2, RL.yb + 76, { align: 'center', kind: 'number', px: 48, color: C.ink, alpha: ok * show(t, b.c1.twenty, M.m_w27.t0) });
      const hA = ok * show(t, b.c2.half, M.m_w27.t0);
      for (const r of [RC, RL]) seg2(O, (r.x0 + r.x1) / 2, r.yt - 30, (r.x0 + r.x1) / 2, r.yb + 10, C.muted, hA, 4, [8, 6]);
      label(O, L['c2.half'], (RC.x0 + RC.x1) / 2, RC.yt - 50, { align: 'center', kind: 'compare', px: 48, alpha: hA });
      checkLabel(O, lev, 'level check', ok * show(t, b.c1.level, M.m_w27.t0), { kind: 'name', w: 600, color: C.muted });
      log.roi['c1.level'] = [RL.x0 - 10, RL.yt - 20, RL.x1 + 10, RL.yb + 10]; log.roi['c1.twenty'] = [RL.x0 - 10, RL.yb + 20, RL.x1 + 10, RL.yb + 100];
      log.roi['c2.half'] = [RC.x0, RC.yt - 90, RL.x1, RL.yb + 10];
      // S26: dải nhỏ 715 quãng (đầu khung), thập niên 1960 sáng, thanh của Carl màu Carl
      const sA = ok * show(t, b.c3.sixties, M.m_w27.t0);
      if (sA > 0.01) {
        const c = O.ctx, x0 = 240, x1 = 1680, pw = (x1 - x0) / starts.length, base = 420, hS = 1.3;
        c.save(); c.globalAlpha = sA;
        v20.forEach((v, i) => { const s60 = starts[i] >= '1960' && starts[i] < '1970'; c.fillStyle = i === iC ? CHAR.carl : s60 ? C.warn : rgba(C.muted, 0.28); c.fillRect(x0 + i * pw, base - v * hS, Math.max(1, pw - 0.5), v * hS); });
        c.restore(); seg2(O, x0, base - 100 * hS, x1, base - 100 * hS, C.muted, sA, 2);
        label(O, L['c3.forty'], 960, 236, { align: 'center', kind: 'number', px: 52, alpha: ok * show(t, b.c3.forty - 1.0, M.m_w27.t0) });   // FIX-R1: sát lời "forty-four" (trước: sớm 2,4 s); 1 s trước để 5 từ đủ 2 s trước cú về thế giới
        log.roi['c3.sixties'] = [x0, base - 140, x1, base];
      }
    }
    // ===== S27 (cEdna → cBoth): port C3 s27-edna + mốc năm + phần chồng accent
    const Ec = cols.edna, RE = rowBox(O, Ec, kf(S.rows.edna, t)), u = ease(t, M.m_pull27.t0, M.m_pull27.t1);
    if (t > M.m_c27.t0 && t < M.m_pan28.t1) {
      const e0 = 1949, c0 = 1966, mA = ok * show(t, M.m_c27.t1, M.m_pan28.t0 - 0.2);
      label(O, L['d0.edna'], mix(120, AX.x0, u), mix(385, AX.eY - 28, u), { kind: 'number', px: 48, w: 600, color: CHAR.edna, alpha: mA });
      label(O, L['d0.kept'], 120, 228, { kind: 'compare', px: 48, alpha: ok * show(t, b.d0.kept, M.m_pull27.t0 - 0.3) });
      const kE = Math.max(cnt(S.years.edna, t), t >= S.years.edna_rep[0] ? 17 + cnt(S.years.edna_rep, t) : 0);
      const kA = ok * (kE >= 1 ? 1 : 0) * (1 - show(t, M.m_pull27.t0 - 0.3)) + ok * show(t, b.d4.end, M.m_pan28.t0 - 0.2);
      if (kE >= 1) label(O, `year ${kE}`, RE.x1, RE.yt - 30, { align: 'right', kind: 'number', px: 52, alpha: kA });
      const fA = ok * show(t, S.years.edna[19] + 0.2, M.m_pull27.t0 - 0.3), gA = ok * show(t, b.d4.end, M.m_pan28.t0 - 0.2);
      brace(O, RE.x0, RE.x1, RE.yb + 22, C.ink, Math.max(fA, gA), 5, -14);
      label(O, L['d1.y20'], RE.x0, RE.yb + 86, { kind: 'number', px: 48, alpha: fA });
      label(O, L['d4.lit'], RE.x0, RE.yb + 80, { kind: 'number', px: 48, alpha: gA });
      checkLabel(O, Ec, L['d1.check'], ok * show(t, b.d1.check, M.m_pull27.t0 - 0.3), { dx: 14 });
      log.roi['d1.twenty'] = [RE.x0 - 10, RE.yt - 90, RE.x1 + 10, RE.yb + 110]; log.roi['d1.check'] = [RE.x0 - 300, RE.yt - 300, RE.x0, RE.yb];
      // trục thời gian: thanh Edna 1949–1969 ("answer"), thanh Carl 1966–1986 ("Carl's"), phần chồng 1966–1969 (accent = giá, "same"), mốc năm
      const bA = ok * u * (1 - show(t, M.m_pan28.t0 - 0.1)), eW = lin(t, b.d2.answer, b.d2.answer + 0.8), cWd = lin(t, b.d3.carl, b.d3.carl + 0.8), sA = ok * show(t, b.d4.same, M.m_pan28.t0 - 0.1);
      if (bA > 0.01) {
        const c = O.ctx; c.save();
        if (sA > 0.01) { c.globalAlpha = sA; c.fillStyle = rgba(C.accent, 0.45); c.fillRect(yr(c0), AX.eY - 12, yr(e0 + 20) - yr(c0), AX.cY + AX.h - AX.eY + 24); }
        c.globalAlpha = bA; c.fillStyle = CHAR.edna; if (eW > 0) c.fillRect(yr(e0), AX.eY, (yr(e0 + 20) - yr(e0)) * eW, AX.h);
        c.fillStyle = CHAR.carl; if (cWd > 0) c.fillRect(yr(c0), AX.cY, (yr(c0 + 20) - yr(c0)) * cWd, AX.h);
        c.restore();
        O.shape({ role: 'bar', box: [yr(e0), AX.eY, yr(e0 + 20), AX.eY + AX.h], char: 'edna', opacity: bA * (eW > 0 ? 1 : 0) });
        O.shape({ role: 'bar', box: [yr(c0), AX.cY, yr(c0 + 20), AX.cY + AX.h], char: 'carl', opacity: bA * (cWd > 0 ? 1 : 0) });
        const tick = (y, row, a) => { if (a > 0.01) { seg2(O, yr(y), row - 8, yr(y), row + AX.h + 8, C.ink, a, 3); label(O, L['ax' + y], yr(y), row + AX.h + 52, { align: 'center', kind: 'number', px: 48, alpha: a }); } };
        tick(1949, AX.eY, bA * (eW > 0.99 ? 1 : 0) * (1 - sA)); tick(1969, AX.eY, bA * (eW > 0.99 ? 1 : 0));
        tick(1966, AX.cY, bA * (cWd > 0.99 ? 1 : 0)); tick(1986, AX.cY, bA * (cWd > 0.99 ? 1 : 0));
      }
      label(O, L['d3.carl'], AX.x1, AX.cY + AX.h + 116, { align: 'right', kind: 'number', px: 48, w: 600, color: CHAR.carl, alpha: ok * show(t, b.d3.carl, M.m_pan28.t0 - 0.2) });
      label(O, L['d4.same'], (yr(c0) + yr(e0 + 20)) / 2, 205, { align: 'center', kind: 'compare', px: 48, alpha: sA });
      log.roi['d2.answer'] = [AX.x0 - 10, AX.eY - 70, AX.x1 + 10, AX.cY + AX.h + 70]; log.roi['d4.same'] = log.roi['d2.answer'];
      const kC = cnt(S.years.carl27, t);
      if (kC >= 1) label(O, `year ${kC}`, RC.x1, RC.yt - 30, { align: 'right', kind: 'number', px: 52, alpha: ok * (1 - show(t, M.m_pan28.t0 - 0.2)) });
      log.roi['d4.start'] = [RC.x0 - 10, RC.yt - 90, RC.x1 + 10, RC.yb + 10]; log.roi['d4.end'] = [RE.x0 - 10, RE.yt - 90, RE.x1 + 10, RE.yb + 110];
    }
    // ===== S28 (cRuth): Ruth ở 85, hai thanh một năm
    if (t > M.m_pan28.t0 && t < M.m_w29.t1) {
      label(O, L['e0.eighty'], 120, 385, { kind: 'number', px: 48, w: 600, color: CHAR.ruth, alpha: ok * show(t, b.e0.eighty, M.m_w29.t0) });
      const bx = 1180, bw = 560, by0 = 200, g3 = ease(t, b.e1.three - 0.1, b.e1.three + 0.8), g2 = ease(t, b.e1.two - 0.1, b.e1.two + 0.6);
      const pA = ok * show(t, b.e1.three, M.m_w29.t0), rA = ok * show(t, b.e1.two, M.m_w29.t0), c = O.ctx;
      if (pA > 0.01) { c.save(); c.globalAlpha = pA; c.fillStyle = C.accent; c.fillRect(bx, by0 + 40, bw * g3, 40); c.restore(); label(O, L['e1.three'], bx + bw, by0 + 20, { align: 'right', kind: 'number', px: 48, alpha: pA }); }
      if (rA > 0.01) { c.save(); c.globalAlpha = rA; c.fillStyle = C.ink; c.fillRect(bx, by0 + 160, bw * (2 / S.yoy) * g2, 40); c.restore(); label(O, L['e1.two'], bx + bw, by0 + 140, { align: 'right', kind: 'number', px: 48, alpha: rA }); }
      log.roi['e1.three'] = [bx - 400, by0 - 30, bx + bw, by0 + 90]; log.roi['e1.two'] = [bx - 400, by0 + 90, bx + bw, by0 + 210];
      log.roi['e0.eighty'] = [100, 330, 800, 400];
    }
    // ===== S29 (wThree → cThree): port C3 s29-three
    if (three) {
      const mA = ok * show(t, M.m_c29.t1), hA = show(t, b.f2.month), hp = pulse(t, b.f2.month, 1.2);
      label(O, L['f1.crates'], 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: ok * show(t, b.f1.crates) });
      const sd = { edna: CL.kept_up_last_start_20y.display, ruth: CL.guide_start.display, carl: CL.worst_window_start_year_20y.display };
      const vals = { edna: [L['f1.full'], 'full'], ruth: [L['f1.nine'], 'nine'], carl: [L['f1.four'], 'four'] };
      for (const id of ['edna', 'ruth', 'carl']) {
        const c = cols[id], [xl] = O.toScreen(c.row.edgeX(0), 0, 0.4);
        label(O, `${NAME[id]} · ILLUSTRATIVE`, xl, 550, { kind: 'name', px: 48, w: 600, color: CHAR[id], alpha: mA });
        label(O, sd[id], xl, 610, { kind: 'number', px: 48 + 8 * hp, w: 600, color: hA > 0.5 ? CHAR[id] : C.muted, alpha: mA, emph: hA > 0.5 });
        label(O, vals[id][0], xl, 462, { kind: 'number', px: 72, alpha: ok * show(t, b.f1[vals[id][1]]) });
        const r = rowBox(O, c); log.roi[`f1.${vals[id][1]}`] = [r.x0 - 10, 390, r.x1 + 10, r.yb + 10];
        log.roi['f0.' + id] = [r.x0 - 10, r.yt - 20, r.x1 + 10, r.yb + 10];
      }
      log.roi['f2.month'] = [96, 560, 1824, 640];
    }
    const cwA = show(t, b.e2.t0, M.m_w29.t1 + 0.6);   // FIX-R1: đối trọng 7 từ ≥ 3 s (trước ~2,4 s)
    chrome(O, 1, cwA > 0.01 ? L['e2.history'] : null, cwA);
    dip(O, 1 - ease(t, 0, 0.4));
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
