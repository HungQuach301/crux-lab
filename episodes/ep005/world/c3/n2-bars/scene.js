// Tập 5 · C3 · N2 cột phát lại (S13.1–S13.3) · vòng 3 (FIX-R3.md). Mốc giờ chỉ từ spine.json; hằng số = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { Beam, Studio, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, lin, ease, easeOut } from '/toolkit/factory/world/core.js';
import { Bars } from '/episodes/ep005/world/obj5.js';

const SEG = '/episodes/ep005/world/c3/n2-bars/';
const POP = 0.15, HB = 0.025;                                     // cột: đơn vị thế giới / tháng
const XB = (i, n) => -5.5 + 11 * i / (n - 1);                     // tháng mua thứ i (1991-01 → 2016-07)
// vòng 3: cột chậm màu TRUNG TÍNH (accent của kênh, không warn = báo động) — tiền lệ D-010 §6 (b) E5j: đổi màu đường chậm + nhãn thời lượng.
// Chỉ số quốc gia đổi sang muted (không trùng màu cột chậm); đoạn đỉnh → đáy đậm bằng ink.
const SLOW = C.accent, IXC = C.muted;

export async function boot(res) {
  const [S, D, CL] = await Promise.all([loadJSON(SEG + 'spine.json'), loadJSON('/episodes/ep005/work/world-data/derived.json'), loadJSON('/episodes/ep005/world/claims.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const mv = S.moves[0], [D0, D1] = S.index_draw;
  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor } = Studio(scene, { shadowBox: 14 });
  const poses = {
    wRow: { pos: [-9.0, 1.7, 6.2], tgt: [-1.2, 0.9, 0], fov: 35, chart: 0 },
    cBars: { pos: [0, 0.9, 35.2], tgt: [0, 0.9, 0], fov: 14, chart: 1 },     // vòng 2: khung hạ để trục tháng mua + dải chỉ số nằm DƯỚI cột
  };
  const CAM = Camera(poses, S.moves);
  const P = D.bars, n = P.length, bars = Bars({ n, d: 0.45 }); scene.add(bars);
  const med = CL.medianB_months_to80.value;
  const typ = Beam({ length: 11.4 }); typ.position.set(0, med * HB, 0.3); scene.add(typ);
  const cut60 = Beam({ length: 11.4 }); cut60.position.set(0, 60 * HB, 0.3); scene.add(cut60);
  const slowIdx = P.map((p, i) => (p.hit > 60 ? i : -1)).filter((i) => i >= 0), s0 = slowIdx[0], s1 = slowIdx[slowIdx.length - 1];
  // chỉ số giá quốc gia THEO THÁNG MUA: vòng 2 vẽ thành một dải mảnh nằm trong trục tháng mua (ngay dưới chân cột, trên hàng năm),
  // không còn là đường nổi phía trên cụm cột (vòng 1: người đọc thấy "giá rơi rồi hồi phục phía trên những người chờ lâu" → "ở lại cho qua đợt giảm").
  const IX = D.index.filter((x) => x.m <= P[n - 1].m), vmin = Math.min(...IX.map((x) => x.v)), vmax = Math.max(...IX.map((x) => x.v));
  const ST0 = 16, STH = 90;                                                  // dải: px dưới chân cột (không gian 1080p)
  const pk = IX.reduce((a, x, i) => (x.m < '2012-01-01' && x.v > IX[a].v ? i : a), 0), tr = IX.reduce((a, x, i) => (x.m > IX[pk].m && x.m < '2015-01-01' && x.v < IX[a].v ? i : a), pk + 1);

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam, b = cue;
    floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = 30 + 120 * cw; scene.fog.far = 80 + 220 * cw;
    const tl = easeOut(t, b.t0.tail - 0.05, b.t0.tail + 0.6);                 // đuôi: cột > 60 tháng sáng màu trung tính (vòng 3: accent) và nhô từ mức 60 lên đủ cao
    bars.set(P.map((p, i) => { const slow = p.hit > 60; const h = slow ? (60 + (p.hit - 60) * tl) * HB : p.hit * HB;
      return { x: XB(i, n), h, z: 0, color: slow && tl > 0.02 ? SLOW : '#C9CFD8' }; }));
    setOpacity(typ, 1 - ease(t, b.t0.tail, b.t0.tail + 0.4)); setOpacity(cut60, ease(t, mv.t1 - 0.3, mv.t1)); cut60.glow(t >= b.t1.years ? 1 - lin(t, b.t1.years, b.t1.years + 0.9) : 0);
    const k = Math.round(lin(t, D0, D1) * (IX.length - 1));
    const sl = ease(t, b.t2.slump - 0.05, b.t2.slump + POP);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, S2 = (x, y) => O.toScreen(x, y, 0.3); log.roi = {};
    { const [x0, y0] = O.toScreen(XB(s0, n), 112 * HB, 0), [x1, y1] = O.toScreen(XB(s1, n), 0, 0); log.roi['t0.tail'] = [Math.min(x0, x1) - 30, y0 - 30, Math.max(x0, x1) + 30, y1 + 10]; }
    { const [x0, y0] = S2(XB(s0, n), 3.2), [x1, y1] = S2(XB(s1, n), 2.6); log.roi['t2.together'] = [x0 - 20, y0 - 30, x1 + 20, y1 + 30]; }
    const yb = S2(0, 0)[1], ys0 = yb + ST0, ys1 = ys0 + STH, YS = (v) => ys1 - STH * (v - vmin) / (vmax - vmin), XS = (i) => S2(XB(i, n), 0)[0];
    log.roi['t2.national'] = [XS(0) - 10, ys0 - 10, XS(Math.round(n / 3)), ys1 + 130];   // dải chỉ số + nhãn 'national home price index' (bên trái)
    // thế giới: tên (không số)
    const wOut = 1 - ease(t, mv.t0, mv.t0 + 0.3);
    { const [x, y] = O.toScreen(-5.6, med * HB, 0.3); O.text('typical', x - 14, y + 16, 48, { align: 'right', alpha: wOut * ease(t, b.t0.typical - 0.05, b.t0.typical + POP) * (1 - ease(t, b.t0.tail, b.t0.tail + 0.4)), plate: '#0B0E13', plateA: 0.6 }); }
    { const [x, y] = O.toScreen(XB(s0, n), 112 * HB + 0.2, 0); O.text('a long tail', x, y - 20, 52, { align: 'center', alpha: wOut * ease(t, b.t0.tail - 0.05, b.t0.tail + POP), plate: '#0B0E13', plateA: 0.6 }); }
    // đồ thị
    const axA = ok * ease(t, mv.t1 - 0.2, mv.t1);
    O.text('one bar per purchase month', 960, 172, 52, { kind: 'compare', align: 'center', alpha: axA });   // tiêu đề trục tháng mua giữ suốt (vòng 2); vòng 3: chiều cao cột có nhãn riêng ngay cạnh cụm
    // cụm chậm: dải mờ màu cột chậm chạy dọc từ đỉnh cụm xuống hết trục tháng mua (nối cụm ↔ tháng mua ↔ đoạn chỉ số cùng tháng)
    const gA = ok * ease(t, b.t2.together - 0.05, b.t2.together + POP);
    if (gA > 0) { const c = O.ctx, [x0, y0] = S2(XB(s0, n), 112 * HB + 0.12); c.save(); c.globalAlpha = 0.12 * gA; c.fillStyle = SLOW; c.fillRect(x0 - 6, y0, XS(s1) - x0 + 12, ys1 + 8 - y0); c.restore(); }
    // dải chỉ số trong trục tháng mua: vẽ trái → phải (D0 → "national"); "slump": đoạn đỉnh → đáy đậm
    if (t >= D0 && ok) { const c = O.ctx; c.save(); c.globalAlpha = 0.9; c.strokeStyle = IXC; c.lineWidth = 4; c.lineJoin = 'round'; c.beginPath();
      for (let i = 0; i <= k; i++) { const x = XS(Math.min(i, n - 1)), y = YS(IX[i].v); i ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke();
      if (sl > 0) { c.globalAlpha = sl; c.strokeStyle = C.ink; c.lineWidth = 9; c.beginPath(); for (let i = pk; i <= tr; i++) { const x = XS(i), y = YS(IX[i].v); i > pk ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke(); }
      c.restore(); }
    for (const yy of [1991, 1995, 2000, 2005, 2010, 2016]) { const i = P.findIndex((p) => p.m.startsWith(String(yy))); O.text(String(yy), XS(i), ys1 + 46, 48, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: axA }); }
    { const [x, y] = S2(-5.5, 60 * HB); O.text('60 months', x, y - 16, 46, { kind: 'number', color: C.muted, alpha: axA }); }
    const pct = (100 * CL.shareB_over60.value).toFixed(1);
    { const [x, y] = S2(-5.5, 60 * HB + 1.1), pa = ok * ease(t, b.t1.years - 0.05, b.t1.years + POP); O.text('more than 60 months:', x, y, 52, { kind: 'compare', alpha: pa, plate: '#0B0E13', plateA: 0.75 }); O.text(`${pct}% (about 1 in 7)`, x, y + 66, 52, { kind: 'compare', alpha: pa, plate: '#0B0E13', plateA: 0.75 }); }
    if (gA > 0) { const [x0, y0] = S2(XB(s0, n), 112 * HB + 0.12), [x1] = S2(XB(s1, n), 0), c = O.ctx; c.save(); c.globalAlpha = gA; c.strokeStyle = SLOW; c.lineWidth = 5;
      c.beginPath(); c.moveTo(x0, y0 + 14); c.lineTo(x0, y0); c.lineTo(x1, y0); c.lineTo(x1, y0 + 14); c.stroke(); c.restore();
      O.text('one stretch of purchase months', (x0 + x1) / 2, y0 - 26, 50, { color: C.ink, align: 'center', alpha: ok * ease(t, b.t2.stretch - 0.05, b.t2.stretch + POP), plate: '#0B0E13', plateA: 0.7 }); }
    // vòng 3: nhãn thời lượng gắn vào cụm (nhãn mới duy nhất, 8 từ, 48 px, sự thật, không mệnh lệnh): chiều cao cột = số tháng TỚI 80 % trên giấy
    // (một phép đo trên giấy theo tháng mua), không phải thời gian giữ nhà. Thước dọc ở mép phải cụm: chân cột → đỉnh cột cao nhất.
    { const hA = axA, [xr] = S2(XB(s1, n), 0), xR = xr + 26, yT = S2(0, CL.maxB_months_to80.value * HB)[1], c = O.ctx;
      if (hA > 0) { c.save(); c.globalAlpha = 0.85 * hA; c.strokeStyle = C.ink; c.lineWidth = 3; c.beginPath(); c.moveTo(xR - 10, yT); c.lineTo(xR + 10, yT); c.moveTo(xR, yT); c.lineTo(xR, yb); c.moveTo(xR - 10, yb); c.lineTo(xR + 10, yb); c.stroke(); c.restore(); }
      O.text("each bar's height:", xR + 20, yT + 34, 48, { color: C.ink, alpha: hA, plate: '#0B0E13', plateA: 0.75 });
      O.text('months to 80% on paper', xR + 20, yT + 96, 48, { color: C.ink, alpha: hA, plate: '#0B0E13', plateA: 0.75 }); }
    O.text('national home price index', XS(0), ys1 + 116, 48, { color: IXC, alpha: ok * ease(t, b.t2.national - 0.05, b.t2.national + POP) });
    O.text('national price slump', XS(Math.round((pk + tr) / 2)), ys1 + 116, 52, { color: C.ink, align: 'center', alpha: ok * sl, plate: '#0B0E13', plateA: 0.75 });
    O.chrome({ src: ok ? 'Source: FHFA · Freddie Mac via FRED' : null, srcA: ok, hist: ok > 0, histA: ok, cw: ok ? 'Past buyers, measured · not a reason to buy, rent or wait' : null, cwA: ok });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
