// Tập 5 · C3 · N3 gập đường → cột (S10.4–S10.5), dùng N1 lịch + N2 cột. Mốc giờ chỉ từ spine.json; hằng số = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { House, Stack, Beam, Studio, Fan, Burst, PALETTE, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, lin, ease } from '/toolkit/factory/world/core.js';
import { Calendar, Bars, foldPath } from '/episodes/ep005/world/obj5.js';

const SEG = '/episodes/ep005/world/c3/n3-fold/';
const POP = 0.15, UW = 2e5, WX = -13;
const XM = (k) => -5 + 10 * k / 120;                    // đồ thị đường: tháng sau khi mua 0 → 120 (như E5k)
const YL = (l) => (l - 0.75) * 11;                      // đồ thị đường: dư nợ ÷ giá trị
const HB = 0.030;                                        // cột: đơn vị thế giới / tháng
const XB = (i, n) => -5.5 + 11 * i / (n - 1);            // cột: tháng mua thứ i (1991-01 → 2016-07)

export async function boot(res) {
  const [S, D] = await Promise.all([loadJSON(SEG + 'spine.json'), loadJSON('/episodes/ep005/work/world-data/derived.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const mv = S.moves[0], [F0, F1] = S.fold;
  const interp = (kf, t) => { if (t <= kf[0][0]) return kf[0][1]; for (let i = 1; i < kf.length; i++) if (t <= kf[i][0]) { const [a, x] = kf[i - 1], [b, y] = kf[i]; return x + (y - x) * (t - a) / (b - a); } return kf[kf.length - 1][1]; };
  const at = (arr, k) => { const i = Math.min(arr.length - 2, Math.floor(k)), f = k - i; return arr[i] + (arr[i + 1] - arr[i]) * f; };
  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor } = Studio(scene, { shadowBox: 20 });
  const poses = {
    wReplay: { pos: [WX + 1.6, 2.5, 8.4], tgt: [WX + 1.3, 1.5, 0], fov: 35, chart: 0 },
    cBars: { pos: [0, 2.15, 35.2], tgt: [0, 2.15, 0], fov: 12, chart: 1 },
  };
  const CAM = Camera(poses, S.moves);
  const G = D.buyers.grace;
  // ---- thế giới: một tháng mua
  const value = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); value.position.set(WX, 0, 0); scene.add(value);
  const house = House({ w: 1.4 }); scene.add(house);
  const loan = Stack({ unitUsd: UW, w: 1.0, d: 0.7 }); loan.position.set(WX + 1.25, 0, 0.1); scene.add(loan);
  const bar80w = Beam({ length: 1.5 }); bar80w.position.set(WX + 1.25, 0, 0.1); scene.add(bar80w);
  const cal = Calendar({ w: 1.1, h: 1.35 }); cal.position.set(WX + 2.75, 0, 0.3); cal.rotation.y = -0.25; scene.add(cal);
  const burstW = Burst(); scene.add(burstW);
  // ---- đồ thị: bó đường → cột
  const beam = Beam({ length: 11.4 }); beam.position.set(0, YL(0.8), 0); scene.add(beam);
  const fan = Fan(); scene.add(fan);
  const P = D.paths, n = P.length, bars = Bars({ n }); bars.position.z = 0.3; scene.add(bars);
  const tall = P.reduce((a, p, i) => (p.hit > P[a].hit ? i : a), 0);
  const target = P.map((p, i) => ({ x: XB(i, n), y0: YL(0.8), h: p.hit * HB }));
  const lineCol = new THREE.Color(C.bg).lerp(new THREE.Color(C.ink), 0.45).getStyle();

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam, b = cue;
    floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = 30 + 120 * cw; scene.fog.far = 80 + 220 * cw;
    // thế giới: tháng k sau khi mua; giá trị theo chỉ số, dư nợ theo lịch; lịch lật mỗi tháng, NGỪNG ở "less"
    const k = interp(S.month_kf, t), vUsd = 400000 * at(G.index, k), lUsd = 400000 * at(G.sched_line, k);
    const vh = value.set({ usd: vUsd, tintBelowUsd: 1e9, tint: '#C9D1DC', tintA: 0.55 }); house.position.set(WX, vh, 0);
    loan.set({ usd: lUsd, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 });
    bar80w.position.y = 0.8 * vUsd / UW; const hitA = t >= b.f0.less ? 1 - lin(t, b.f0.less, b.f0.less + 1.2) : 0; bar80w.glow(hitA);
    setOpacity(bar80w, ease(t, b.f0.eighty - 0.05, b.f0.eighty + POP) || (t >= b.f0.compare ? 0.6 : 0));
    const stopped = t >= b.f0.less;
    cal.set({ flip: stopped || t < b.f0.every ? 0 : k % 1, pages: 1 - 0.5 * k / G.hit, glow: hitA });
    burstW.position.set(WX + 1.25, 0.8 * vUsd / UW, 0.6); burstW.scale.setScalar(0.4 + 1.6 * (1 - hitA)); burstW.material.opacity = hitA * (1 - cw);
    // đồ thị: đường (u = 0) → cột (u = 1)
    const u = lin(t, F0, F1), barA = lin(t, F1 - 0.15, F1 + 0.1), fanA = Math.min(1, ease(t, mv.t0, mv.t1) * 1.4) * (1 - barA);
    if (fanA > 0.01) {
      const lc = t >= F0 ? '#E3E7ED' : lineCol, lines = P.map((p, i) => ({ color: lc, pts: foldPath(p.p.map((l, kk) => [XM(kk), YL(l)]), target[i], u) }));
      fan.set(lines); fan.material.opacity = fanA;
    } else fan.material.opacity = 0;
    const hl = ease(t, b.f1.height - 0.05, b.f1.height + POP);
    bars.set(P.map((p, i) => ({ x: target[i].x, y: target[i].y0, h: target[i].h, color: i === tall && hl > 0.5 ? C.ink : '#C9CFD8' })));
    setOpacity(bars, barA);
    setOpacity(beam, cw > 0.02 ? 1 : 0);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0, S2 = (x, y) => O.toScreen(x, y, 0.3); log.roi = {};
    { const [x, y] = O.toScreen(WX + 2.75, 1.35, 0.3), [x1, y1] = O.toScreen(WX + 2.75, 0, 0.3); log.roi['f0.every'] = [x - 110, y - 10, x + 110, y1 + 10]; }
    { const [x, y] = O.toScreen(WX + 1.25, 0.8 * vUsd / UW, 0.1); log.roi['f0.less'] = [x - 120, y - 60, x + 120, y + 60]; }
    { const [x0, y0] = S2(-5.5, 4.4), [x1, y1] = S2(5.5, 0.4); log.roi['f1.bar'] = [x0, y0, x1, y1]; }
    // thế giới: tên (không số)
    const wOut = 1 - ease(t, mv.t0, mv.t0 + 0.3);
    { const [x, y] = O.toScreen(WX - 0.65, 0.9, 0.4); O.text('home value', x, y, 48, { align: 'right', alpha: wOut * ease(t, b.f0.value - 0.05, b.f0.value + POP), plate: '#0B0E13', plateA: 0.6 }); }
    { const [x, y] = O.toScreen(WX + 1.25, lUsd / UW + 0.25, 0.1); O.text('loan', x, y - 18, 48, { align: 'center', alpha: wOut * ease(t, b.f0.compare - 0.05, b.f0.compare + POP), plate: '#0B0E13', plateA: 0.6 }); }
    // đồ thị trước khi gập
    const preA = ok * (1 - ease(t, F0 - 0.3, F0));
    O.text('Loan as % of home value · one line per purchase month, 1991–2016', 960, 232, 48, { kind: 'compare', align: 'center', alpha: preA });
    for (let yr = 0; yr <= 10; yr += 2) { const [x, y] = S2(XM(yr * 12), YL(0.8)); O.text(yr === 10 ? '10 years' : String(yr), x, y + 50, 44, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: preA }); }
    { const [x, y] = S2(-5.6, YL(0.8)); O.text('80%', x - 10, y + 16, 48, { kind: 'number', align: 'right', alpha: preA }); }
    // đồ thị sau khi gập
    const postA = ok * ease(t, F1 - 0.1, F1 + POP);
    O.text('Months to 80% on paper · one bar per purchase month', 960, 232, 48, { kind: 'compare', align: 'center', alpha: postA });
    const mA = ok * ease(t, b.f1.month - 0.05, b.f1.month + POP);
    for (const yy of [1991, 1995, 2000, 2005, 2010, 2016]) { const i = P.findIndex((p) => p.m.startsWith(String(yy))); const [x, y] = S2(target[i].x, YL(0.8)); O.text(String(yy), x, y + 50, 44, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: mA }); }
    if (hl > 0) { const [x, y0] = S2(target[tall].x + 0.12, target[tall].y0 + target[tall].h), [, y1] = S2(0, target[tall].y0); O.bracket(x + 6, y0, y1, C.ink, ok * hl, 16, 5);
      O.text('height = months to 80% on paper', x - 60, (y0 + y1) / 2 - 40, 52, { align: 'right', kind: 'compare', alpha: ok * hl, plate: '#0B0E13', plateA: 0.75 }); }
    const chOn = ok;
    O.chrome({ illus: cw < 0.5, illusA: 1 - ease(t, mv.t0, mv.t0 + 0.3), src: chOn ? 'Source: FHFA · Freddie Mac via FRED' : null, srcA: chOn,
      hist: chOn > 0, histA: chOn, cw: chOn ? 'Past buyers, measured · not a reason to buy, rent or wait' : null, cwA: chOn });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
