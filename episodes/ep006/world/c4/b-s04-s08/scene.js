// Tập 6 · C4 · ĐOẠN B = S04–S08 (Hồi 1). Ruth giữa hai tấm séc (đều: cao, xám, không đổi · tăng: thấp, ×1,02 mỗi kỷ niệm) → đồ thị so cỡ đầu
// ("?" — không mô hình hoá) → mỗi séc về đầu hàng 10 thùng của nó → Ruth nhận séc tăng (Aug 2006, 65) → hai thanh cùng gốc (séc +48,6 %, giá +64,3 %)
// → S07 (C3 đã duyệt): séc lớn lên, hàng tối tới 0,904 → đồ thị 10 / about 9 → S08: hàng của séc đều tối tới 0,609. Mốc giờ chỉ từ spine.json.
import * as THREE from 'three';
import { Person } from '/toolkit/factory/world/lib3d.js';
import { setup, column, setCheck, checkLabel, rowBox, modeLook, followLight, chrome, brace, label, seg2, kf, show, pulse, setOpacity,
  CHAR, C, ease, mix, rgba, checkScale } from '/episodes/ep006/world/c4kit.js';
import { checkLook } from '/episodes/ep006/world/c4/checklook.js';

const SEG = '/episodes/ep006/world/c4/b-s04-s08/';
const BX = [12.6, 14.0], BU = 2.0;                                  // hai thanh S06 (phần TĂNG so với séc đầu / giá đầu, cùng gốc): x séc, x giá; +100 % = 2 đơn vị

export async function boot(res) {
  const poses = {
    wFig0: { pos: [0.3, 2.0, 7.0], tgt: [0, 0.7, 0], fov: 35, chart: 0 },
    cCards: { pos: [0, 0.95, 17], tgt: [0, 0.95, 0], fov: 14, chart: 1 },        // vòng sửa 1: lùi + hạ — nhãn hai séc trong mép, chữ trên không đè đầu Ruth
    // vòng sửa 2 (séc ngang: séc đều lớn hơn, séc tăng lớn về phía Ruth): cCols lùi 42 → 46, cRise/wRise dời trái — người, séc, hàng trong mép
    cCols: { pos: [-0.2, 1.0, 46], tgt: [-0.2, 1.0, 0], fov: 14, chart: 1 },       // vòng sửa 1: lùi thêm — séc đều trái + đuôi hàng séc tăng phải trong mép
    cRise: { pos: [3.8, 0.95, 21.5], tgt: [3.8, 0.95, 0], fov: 14, chart: 1 },
    cBars: { pos: [13.9, 1.0, 22], tgt: [13.9, 1.0, 0], fov: 14, chart: 1 },      // vòng sửa 1: hai thanh giữa khung, nhãn gốc dưới thanh
    wRise: { pos: [1.0, 2.2, 7.8], tgt: [3.3, 0.5, 0], fov: 35, chart: 0 },
    cRise2: { pos: [5.4, 0.5, 22], tgt: [5.4, 0.5, 0], fov: 14, chart: 1 },       // vòng sửa 1: hàng của séc tăng giữa khung (nhãn 90.4% trong mép)
  };
  const { S, CL, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue;
  // vòng sửa 2 (B04 "two stacks of papers", "about the same length"): hai TẤM SÉC ngang (checklook.js) — séc đều lớn hơn rõ (1,25 × 0,68, nét phẳng),
  // séc tăng nhỏ hơn (0,86 × 0,44 = séc của Ruth ở đoạn a/c, nét nhích lên)
  const lev = column(scene, { x: -4.6, name: 'level', who: 'ruth', person: false, level: true, cw: 1.25, cbase: 0.68 }); checkLook(lev);
  const ris = column(scene, { x: 4.6, name: 'rise', who: 'ruth', person: false, cw: 0.86, cbase: 0.44 }); checkLook(ris);
  const ruth = Person({ h: 1.45, color: CHAR.ruth }); ruth.position.set(0, 0, -0.25); scene.add(ruth);
  ruth.userData.checks = { role: 'mark', char: 'ruth', shape: 'person', fill: CHAR.ruth, key: 'person-ruth' };
  const lx1 = lev.card.position.x, rx1 = ris.card.position.x;
  // S06: hai thanh cùng gốc = séc đầu / giá đầu (vạch gốc ink-muted); thanh = phần tăng sau 20 năm: séc ink, giá accent
  const box = (c, e = 0.25) => { const g = new THREE.BoxGeometry(1.1, 1, 0.6); g.translate(0, 0.5, 0); const m = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ color: c, emissive: new THREE.Color(c), emissiveIntensity: e, roughness: 0.7, transparent: true })); m.castShadow = true; scene.add(m); return m; };
  const bars = BX.map((x, i) => { const lo = box(C.muted, 0.1), hi = box(i ? C.accent : C.ink); lo.position.x = hi.position.x = x; lo.scale.set(1.25, 0.04, 1.1); lo.position.y = -0.02; return { lo, hi }; });
  bars[0].hi.userData.checks = { role: 'bar', key: 'bar-check', series: 'rising' }; bars[1].hi.userData.checks = { role: 'bar', key: 'bar-prices', series: 'prices' };
  const gC = S.growth.check, gP = S.growth.prices;
  // vòng sửa 1 (S06 đứng yên ~25 s): hai thanh mọc THEO NĂM — séc ×1,02 mỗi năm ("twenty" → "forty"), giá theo chỉ số giá năm của Ruth
  // (giá năm k = séc năm k / sức mua năm k = 1,02^k / ruth_path[k]; năm 20 = 1,486 / 0,904 = +64,3 %) ("Ruth's" → "sixty")
  const PR = S.ruth_path, yrC = (k) => 1.02 ** k - 1, yrP = (k) => 1.02 ** k / PR[k] - 1;
  const byYear = (f, u) => { const k = Math.min(19, Math.floor(u * 20)), r = u * 20 - k; return u >= 1 ? f(20) : mix(f(k), f(k + 1), ease(r, 0, 0.6)); };
  const tw = (s, px = 48) => { const c = O.ctx; c.save(); c.font = `700 ${px}px Inter`; const w = c.measureText(s).width; c.restore(); return w; };
  const inX = (x, s, px = 48) => { const h = tw(s, px) / 2 + 20; return Math.min(1824 - h, Math.max(96 + h, x)); };   // tâm nhãn giữa trong mép an toàn (cả nền chữ)   // +48,6 % (two_pct_growth_20y_pct) · +64,3 % (latest_window_price_rise_pct), out/model.json raw

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    // séc trượt về đầu hàng của nó ở "each"; hàng mọc
    const sl = ease(t, b.b3.each - 0.05, b.b3.each + 0.8);
    lev.card.position.x = mix(-1.0, lx1, sl); ris.card.position.x = mix(1.0, rx1, sl);
    const rA = ease(t, b.b3.each, b.b3.each + 0.9);
    // Ruth: giữa hai séc → cạnh séc tăng ở "took" (chừa chỗ séc năm 20 lớn về phía bà); séc đều + hàng của nó mờ từ "took", sáng lại ở S08 "level"
    ruth.position.x = mix(0, rx1 + ris.cw / 2 - ris.cw * checkScale(20) - 0.11, ease(t, b.b4.took - 0.05, b.b4.took + 0.8));
    const lvA = 1 - 0.7 * ease(t, b.b4.took, b.b4.took + 0.8) * (1 - ease(t, b.c2.first - 0.2, b.c2.first + 0.4));
    lev.row.set({ value: kf(S.rows.level, t), appear: rA, pulse: pulse(t, b.c2.six, 0.8) });
    ris.row.set({ value: kf(S.rows.rise, t), appear: rA, pulse: pulse(t, b.c1.nine, 0.6) + pulse(t, b.c3.slowed, 0.9) });
    const lA = ease(t, b.b0.bigger - 0.05, b.b0.bigger + 0.5), sA = ease(t, b.b0.smaller - 0.05, b.b0.smaller + 0.5);
    setCheck(lev, S, t, lA); setCheck(ris, S, t, sA);
    if (lvA < 0.999) { setOpacity(lev.row, lvA * (rA > 0.002 ? 1 : 0)); setOpacity(lev.card, lvA * lA); }
    // S06 thanh: hiện từ cú lia, mọc ở "forty" / "sixty"; tắt khi về thế giới
    const bA = t >= MV.m_pan.t0 && t < MV.m_w.t1 ? 1 - ease(t, MV.m_w.t0, MV.m_w.t0 + 0.3) : 0;   // vòng sửa 2: tắt trong 0,3 s đầu cú về thế giới (không nửa ngoài khung)
    const u1 = Math.min(1, Math.max(0, (t - b.b7.twenty) / (b.b7.forty - b.b7.twenty))), u2 = Math.min(1, Math.max(0, (t - b.b8.ruths) / (b.b8.sixty - b.b8.ruths)));
    const hC = byYear(yrC, u1), hP = byYear(yrP, u2), g1 = hC / gC;
    bars[0].hi.scale.y = Math.max(0.001, BU * hC); bars[1].hi.scale.y = Math.max(0.001, BU * hP);   // cùng gốc y = 0; năm 20 đúng lúc lời nói số
    for (const q of bars) { setOpacity(q.lo, bA * ease(t, b.b7.twenty - 0.05, b.b7.twenty + 0.5)); setOpacity(q.hi, bA); }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    { const [x, y] = O.toScreen(ruth.position.x, 1.57, ruth.position.z), gA = t > MV.m_w.t0 && t < MV.m_w.t1 + 0.2 ? ease(t, MV.m_w.t1 - 0.1, MV.m_w.t1 + 0.2) : 1;   // không hiện tên khi máy còn lia qua
      label(O, 'Ruth', x, y - 24, { align: 'center', kind: 'name', px: 48, w: 600, color: CHAR.ruth, alpha: (1 - cw) * gA }); }
    const L = S.label_cues;
    // S04 (cCards): nhãn hai séc, khoảng chênh cỡ đầu "?", không mô hình hoá; S04.3 không so tiền
    const s4 = MV.m_pull.t0 - 0.2;
    if (t < MV.m_pull.t1) {
      // vòng sửa 2: nhãn trên mỗi séc (séc đều: canh phải theo mép phải séc · séc tăng: canh trái theo mép trái séc) — không chồng Ruth ở giữa
      const yL = O.toScreen(0, lev.cbase + 0.3, 0)[1], [lx] = O.toScreen(lev.card.position.x + lev.cw / 2, 0, 0), [rx] = O.toScreen(ris.card.position.x - ris.cw / 2, 0, 0);
      label(O, L['b0.never'], Math.max(lx, 96 + tw(L['b0.never']) + 20), yL, { align: 'right', kind: 'compare', px: 48, color: C.muted, alpha: ok * show(t, MV.m_c1.t1, s4) });
      label(O, L['b0.rises'], Math.min(rx, 1824 - tw(L['b0.rises']) - 20), yL, { kind: 'number', px: 48, alpha: ok * show(t, MV.m_c1.t1, s4) });
      // "starts": phần séc tăng THIẾU so với cỡ đầu của séc đều = ô xám trên séc tăng (từ đỉnh séc tăng lên tới mức đỉnh séc đều) + "?" — không đo
      const gA = ok * show(t, b.b1.starts, s4);
      if (gA > 0.01) {
        const [ax, ay] = O.toScreen(lev.card.position.x + lev.cw / 2, lev.cbase, 0.1), [bx0, by] = O.toScreen(ris.card.position.x - ris.cw / 2, ris.cbase, 0.1), [bx] = O.toScreen(ris.card.position.x + ris.cw / 2, 0, 0.1), c = O.ctx;
        c.save(); c.globalAlpha = gA; c.fillStyle = rgba(C.muted, 0.35); c.fillRect(bx0, ay, bx - bx0, by - ay); c.restore();
        seg2(O, ax, ay, bx, ay, C.muted, gA * 0.7, 3, [10, 8]); seg2(O, bx0, ay, bx, ay, C.muted, gA, 3);
        label(O, '?', bx + 30, (ay + by) / 2 + 30, { kind: 'title', px: 84, alpha: gA, plate: null });
      }
      label(O, L['b1.model'], 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: ok * show(t, b.b1.model, MV.m_pull.t1 - 0.3) });
      label(O, L['b2.dollars'], 960, 312, { align: 'center', kind: 'compare', px: 52, color: C.muted, alpha: ok * show(t, b.b2.dollars, MV.m_pull.t1 - 0.3) });
      log.roi['b1.starts'] = [700, 300, 1220, 800]; log.roi['b1.model'] = [400, 170, 1520, 260]; log.roi['b2.dollars'] = [400, 250, 1520, 330];
    }
    // S04.4 (cCols): "measured: buying power vs its own first check"; mỗi hàng một ngoặc "its own first check"
    const lv = kf(S.rows.level, t), rv = kf(S.rows.rise, t), RL = rowBox(O, lev, lv), RR = rowBox(O, ris, rv);
    const m4 = ok * show(t, b.b3.buying, MV.m_push.t0 - 0.1);
    label(O, L['b3.buying'], 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: m4 });
    const oA = ok * show(t, b.b3.each + 0.6, MV.m_push.t0 - 0.1);   // từ lúc mỗi séc về đầu hàng của nó (≥ 1 s mỗi 3 từ)
    brace(O, RL.x0, RL.x1, RL.yb + 22, C.muted, oA, 4, -12); brace(O, RR.x0, RR.x1, RR.yb + 22, C.muted, oA, 4, -12);
    label(O, 'its own first check', (RL.x0 + RL.x1) / 2, RL.yb + 80, { align: 'center', kind: 'name', px: 48, w: 600, color: C.muted, alpha: oA });
    label(O, 'its own first check', (RR.x0 + RR.x1) / 2, RR.yb + 80, { align: 'center', kind: 'name', px: 48, w: 600, color: C.muted, alpha: oA });
    log.roi['b3.each'] = [RL.x0 - 10, RL.yt - 20, RR.x1 + 10, RR.yb + 100];
    // S05 (cRise): nhãn Ruth, lý lẽ, +2% a year
    const s5 = MV.m_pan.t0 - 0.1;
    label(O, L['b4.august'], 960, 236, { align: 'center', kind: 'number', px: 52, color: CHAR.ruth, alpha: ok * show(t, b.b4.august, s5) });
    label(O, L['b5.prices'], 960, 312, { align: 'center', kind: 'name', px: 52, w: 600, alpha: ok * show(t, b.b5.prices, s5) });
    if (t > MV.m_push.t1 && t < MV.m_pan.t1) checkLabel(O, ris, L['b6.two'], ok * show(t, b.b6.two, s5), { dx: 14 });
    log.roi['b4.august'] = [400, 170, 1520, 260]; log.roi['b5.prices'] = [400, 250, 1520, 330];
    // S06 (cBars): séc +48.6% · giá +64.3%; vạch nét đứt ở đỉnh séc kéo qua thanh giá; nhãn chỉ số
    if (bA > 0.01) {
      const [xr] = O.toScreen(BX[1] + 0.55, 0, 0.3), [, cy] = O.toScreen(BX[0], BU * hC, 0.3), [, py] = O.toScreen(BX[1], BU * gP, 0.3), [bx0, by0] = O.toScreen(BX[0] - 0.7, 0, 0.3), [bxm] = O.toScreen((BX[0] + BX[1]) / 2, 0, 0.3);
      label(O, L['b7.forty'], xr + 30, cy + 16, { align: 'left', kind: 'number', px: 48, alpha: ok * bA * show(t, b.b7.forty) });
      label(O, L['b8.sixty'], xr + 30, py + 16 - 18, { align: 'left', kind: 'number', px: 48, color: C.accent, alpha: ok * bA * show(t, b.b8.sixty) });
      seg2(O, bx0, cy, xr + 10, cy, C.ink, ok * bA * show(t, b.b8.sixty + 0.9), 3, [10, 8]);
      label(O, 'first check · first price', bxm, by0 + 60, { align: 'center', kind: 'name', px: 48, w: 600, color: C.muted, alpha: ok * bA * show(t, b.b7.twenty) });   // gốc chung, dưới hai thanh
      label(O, L['b8.ruths'], bxm, by0 + 128, { align: 'center', kind: 'number', px: 48, alpha: ok * bA * show(t, b.b8.ruths) });
      label(O, L['b9.national'], 960, 236, { align: 'center', kind: 'name', px: 52, w: 600, alpha: ok * bA * show(t, b.b9.national) });
      label(O, L['b9.own'], 960, 312, { align: 'center', kind: 'name', px: 52, w: 600, color: C.muted, alpha: ok * bA * show(t, b.b9.own) });
      log.roi['b7.forty'] = [bx0, cy - 40, xr + 700, by0]; log.roi['b8.sixty'] = [bx0, py - 60, xr + 700, by0]; log.roi['b9.national'] = [400, 170, 1520, 330];
    }
    // S07 (cRise2, C3 s07-ruth): séc "+2% a year" ở "check", ngoặc 10 chỗ ở "ten", phần sáng + about 9 in 10 ở "nine"
    const s7 = MV.m_pull8.t1 + 1.8;   // vòng sửa 1: nhãn 8 từ "today: about 9 in 10 crates (90.4%)" ≥ 3 s
    if (t > MV.m_c7.t0 && t < s7 + 0.4) {
      checkLabel(O, ris, L['b6.two'], ok * show(t, b.c1.check, s7), { dx: 14 });
      const tA = ok * show(t, b.c1.ten, MV.m_pull8.t0), nA = ok * show(t, b.c1.nine, s7);
      brace(O, RR.x0, RR.x1, RR.yb + 22, C.muted, tA, 5, -14);
      label(O, L['c1.ten'], (RR.x0 + RR.x1) / 2, RR.yb + 86, { align: 'center', kind: 'number', color: C.muted, alpha: tA });
      brace(O, RR.x0, RR.xl, RR.yb + 132, C.ink, nA, 5, -14);
      label(O, L['c1.nine'], inX((RR.x0 + RR.xl) / 2, L['c1.nine']), RR.yb + 196, { align: 'center', kind: 'number', alpha: nA });
      log.roi['c1.ten'] = [RR.x0 - 10, RR.yb, RR.x1 + 10, RR.yb + 110]; log.roi['c1.nine'] = [RR.x0 - 10, RR.yb + 110, RR.x1 + 10, RR.yb + 220];
    }
    // S08 (cCols): hàng của séc đều tối tới 0,609; nhãn mỗi hàng; đối trọng; hai cỡ đầu
    if (t > MV.m_pull8.t0) {
      const a8 = ok * show(t, s7 + 0.3);
      // vòng sửa 1: hai nhãn dài không vừa một hàng ngang (≈ 940 + 820 px) → nhãn séc tăng xuống hàng dưới, cả hai giữ trong mép an toàn
      label(O, L['c2.rising'], inX((RR.x0 + RR.x1) / 2, L['c2.rising']), RR.yb + 152, { align: 'center', kind: 'number', px: 48, alpha: a8 });
      brace(O, RL.x0, RL.x1, RL.yb + 22, C.muted, ok * show(t, b.c2.first), 4, -12);
      label(O, L['c2.first'], inX((RL.x0 + RL.x1) / 2, L['c2.first']), RL.yb + 86, { align: 'center', kind: 'number', px: 48, color: C.muted, alpha: ok * show(t, b.c2.first, b.c2.six - 0.3) });
      label(O, L['c2.six'], inX((RL.x0 + RL.x1) / 2, L['c2.six']), RL.yb + 86, { align: 'center', kind: 'number', px: 48, alpha: ok * show(t, b.c2.six) });
      label(O, L['c4.model'], 960, 236, { align: 'center', kind: 'compare', px: 52, color: C.muted, alpha: ok * show(t, b.c4.bigger + 0.3) });   // từ "bigger" (≥ 1 s mỗi 3 từ trước hết đoạn)
      const bg = pulse(t, b.c4.bigger, 1.2);
      if (bg > 0.01) for (const col of [lev, ris]) { const [x, y] = O.toScreen(col.card.position.x, col.cbase, 0.2); seg2(O, x - 40, y, x + 40, y, C.warn, ok * bg, 5); }
      log.roi['c2.six'] = [RL.x0 - 10, RL.yb + 20, RL.x1 + 10, RL.yb + 120]; log.roi['c2.level'] = [RL.x0 - 10, RL.yt - 20, RL.x1 + 10, RL.yb + 10];
      log.roi['c4.model'] = [400, 170, 1520, 260];
    }
    const cwA = show(t, b.c4.own);
    chrome(O, 1, cwA > 0.01 ? L['c4.own'] : null, cwA);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
