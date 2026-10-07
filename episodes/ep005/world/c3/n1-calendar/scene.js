// Tập 5 · C3 · N1 lịch trả nợ (S06.1 + S06.3) · vòng 2 (FIX-R2.md). Mốc giờ chỉ từ spine.json; hằng số = hình học + độ dài hiệu ứng chung.
import * as THREE from 'three';
import { House, Stack, Person, Ribbon, Studio, Shield, PALETTE, setOpacity } from '/toolkit/factory/world/lib3d.js';
import { Camera, Stage, loadJSON, fonts, C, lin, ease, easeOut } from '/toolkit/factory/world/core.js';
import { Calendar } from '/episodes/ep005/world/obj5.js';

const SEG = '/episodes/ep005/world/c3/n1-calendar/';
const POP = 0.15, UNIT = 9e4;                                 // $ / đơn vị (chồng vay ở đồ thị: $360,000 = 4 đơn vị)
const XK = (k) => -4.2 + 9 * k / 360;                          // đồ thị: kỳ trả 0 → 360
const CX = -6.0;                                               // lịch: mép trái khung đồ thị, cạnh người vay ở thế giới

export async function boot(res) {
  const [S, CL] = await Promise.all([loadJSON(SEG + 'spine.json'), loadJSON('/episodes/ep005/world/claims.json')]);
  await fonts();
  const cue = {}; for (const b of S.beats) cue[b.id] = { ...b.cues, t0: b.t0, t1: b.t1 };
  const mv = S.moves[0];
  const interp = (kf, t) => { if (t <= kf[0][0]) return kf[0][1]; for (let i = 1; i < kf.length; i++) if (t <= kf[i][0]) { const [a, x] = kf[i - 1], [b, y] = kf[i]; return x + (y - x) * (t - a) / (b - a); } return kf[kf.length - 1][1]; };
  const r = CL.rate_latest.value / 1200, bal = (k) => Math.pow(1 + r, k) - (Math.pow(1 + r, k) - 1) / (1 - Math.pow(1 + r, -360));
  const st = Stage(res), { renderer, O } = st;
  const scene = new THREE.Scene(); const { floor } = Studio(scene, { shadowBox: 16 });
  const poses = {
    wDesk: { pos: [-7.2, 2.7, 9.8], tgt: [-7.4, 1.6, 0], fov: 35, chart: 0 },
    cPay: { pos: [-0.6, 2.25, 35.2], tgt: [-0.6, 2.25, 0], fov: 14, chart: 1 },
  };
  const CAM = Camera(poses, S.moves);
  const house = House({ w: 1.6 }); house.position.set(-10.2, 0, -0.4); scene.add(house);
  const shield = Shield({ size: 0.8 }); shield.position.set(-10.2, house.userData.height * 0.86, -0.15); scene.add(shield);
  const you = Person({ h: 1.15, color: PALETTE.person2 }); you.position.set(-8.0, 0, 0.6); you.rotation.y = 0.35; scene.add(you);
  const cal = Calendar({ w: 1.3, h: 1.6 }); cal.position.set(CX, 0, 0.2); scene.add(cal);
  const loan = Stack({ unitUsd: UNIT, w: 0.9, d: 0.6, maxUsd: 4e5 }); scene.add(loan);
  const line = Ribbon({ color: C.ink, z: 0.42 }); scene.add(line);            // đoạn chồng đã đi (đậm)
  const sched = Ribbon({ color: C.muted, z: 0.4 }); scene.add(sched);         // cả lịch 360 kỳ in sẵn (mảnh) — lịch cố định từ đầu
  const late = Ribbon({ color: C.chrome, z: 0.41 }); scene.add(late);         // "faster": đoạn cuối dốc của đường in sáng lên
  const [P0, P1] = S.print_draw, KS = S.k_stop;
  const schedPts = []; for (let j = 0; j <= 360; j += 3) schedPts.push([XK(j), 360000 * bal(j) / UNIT]);
  const latePts = schedPts.filter(([x]) => x >= XK(240) - 1e-6);

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam, b = cue;
    floor.material.opacity = 1 - 0.85 * cw; scene.fog.near = 30 + 120 * cw; scene.fog.far = 80 + 220 * cw;
    // người + nhà chỉ ở thế giới: rời khung khi sang đồ thị (đồ thị là lịch của khoản vay, không phải "bạn ở trong nhà bao lâu")
    setOpacity(house, 1 - cw); setOpacity(shield, 1 - cw); setOpacity(you, 1 - cw);
    const k = interp(S.pay_kf, t);                             // kỳ trả hiện tại (0 trước "Each")
    // lịch: "monthly" lật một trang; S06.3 lật liên tục theo kỳ (cứ 3 kỳ một vòng lật cho mắt theo kịp; bộ đếm ghi đúng kỳ)
    const flip = t < b.a1.each ? lin(t, b.a0.monthly - 0.12, b.a0.monthly + 0.38) * (t < b.a0.monthly + 0.38 ? 1 : 0) : (k >= KS ? 0 : (k / 3) % 1);
    cal.set({ flip, pages: 1 - k / 360 * 0.9, glow: 0 });
    // chồng vay trượt theo kỳ; đỉnh chồng vẽ đường dư nợ
    const usd = 360000 * bal(k); loan.position.set(XK(k), 0, 0); loan.set({ usd, tintBelowUsd: 1e9, tint: '#5B6573', tintA: 0.9 });
    setOpacity(loan, 1);
    const pts = []; for (let j = 0; j <= Math.floor(k); j += 2) pts.push([XK(j), 360000 * bal(j) / UNIT]); pts.push([XK(k), usd / UNIT]);
    line.set(pts, 0.08, C.ink); line.material.opacity = t >= b.a1.each ? 1 : 0;
    const np = Math.max(2, Math.round(lin(t, P0, P1) * schedPts.length));
    sched.set(schedPts.slice(0, np), 0.04, C.muted); sched.material.opacity = t >= P0 ? 0.9 : 0;
    late.set(latePts, 0.065, C.chrome); late.material.opacity = ease(t, b.a1.faster - 0.05, b.a1.faster + POP);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    const [cx, cy] = O.toScreen(CX, 1.6, 0.3), [cbx, cby] = O.toScreen(CX, 0.0, 0.3);
    log.roi['a0.monthly'] = [cx - 110, cy - 10, cx + 110, cby + 10]; log.roi['a1.each'] = log.roi['a0.monthly'];
    { const [x0, y0] = O.toScreen(XK(240), 4.2, 0.4), [x1, y1] = O.toScreen(XK(360), 0, 0.4); log.roi['a1.faster'] = [x0 - 40, y0, x1 + 40, y1 + 10]; }
    // chip gắn vào lịch (đồ thị): $2,362/month · principal + interest
    const pay = Math.round(CL.ex_payment_pi.value).toLocaleString('en-US');
    const chipA = ok * ease(t, b.a0.figure - 0.05, b.a0.figure + POP) * (1 - ease(t, b.a1.each - 0.2, b.a1.each + 0.2));   // chip vốn + lãi chỉ trong S06.1
    if (chipA > 0) {
      const c = O.ctx; c.save(); c.globalAlpha = chipA; c.strokeStyle = C.chrome; c.lineWidth = 3; c.beginPath(); c.moveTo(cx, cy - 6); c.lineTo(cx, cy - 46); c.stroke(); c.restore();
      O.text(`$${pay}/month · principal + interest`, cx - 60, cy - 66, 54, { kind: 'number', alpha: chipA, plate: '#0B0E13', plateA: 0.8 });
    }
    const rA = ok * ease(t, mv.t1, mv.t1 + POP);
    O.text(`September 2026 average rate: ${CL.rate_latest.value.toFixed(2)}%`, 960, 232, 52, { kind: 'number', align: 'center', color: C.muted, alpha: rA * (1 - ease(t, b.a1.each - 0.4, b.a1.each)) });
    O.text('loan balance · on the schedule', 960, 232, 52, { kind: 'compare', align: 'center', color: C.muted, alpha: ok * ease(t, b.a1.each, b.a1.each + POP) });
    // trục kỳ trả + bộ đếm trên lịch (đồ thị)
    const axA = ok * ease(t, b.a1.each - 0.3, b.a1.each);
    for (const kk of [0, 120, 240, 360]) { const [x, y] = O.toScreen(XK(kk), 0, 0.4); O.text(kk === 360 ? '360 payments' : String(kk), x, y + 52, 44, { kind: 'number', color: C.muted, align: 'center', w: 600, alpha: axA }); }
    if (t >= b.a1.each) { const [x, y] = O.toScreen(CX + 0.75, 0.5, 0.3); O.text(`payment ${Math.round(k)}`, x + 14, y, 48, { kind: 'number', color: C.ink, alpha: axA, plate: '#0B0E13', plateA: 0.7 }); }
    const [lx, ly] = O.toScreen(XK(0), 4.0, 0.4);
    O.text('$360,000 loan', lx + 70, ly + 10, 48, { kind: 'number', color: C.ink, alpha: ok * ease(t, mv.t1, mv.t1 + POP) * (1 - ease(t, b.a1.each, b.a1.each + 0.4)) });
    const sA = ok * ease(t, b.a1.slowly - 0.05, b.a1.slowly + POP), fA = ok * ease(t, b.a1.faster - 0.05, b.a1.faster + POP);
    { const [x, y] = O.toScreen(XK(70), 360000 * bal(70) / UNIT, 0.4); O.text('slowly at first', x, y + 74, 52, { color: C.ink, align: 'center', alpha: sA }); }
    { const [x, y] = O.toScreen(XK(300), 360000 * bal(300) / UNIT, 0.4); O.text('faster later', x - 40, y + 90, 52, { color: C.ink, align: 'right', alpha: fA }); }
    O.chrome({ illus: true, illusA: 1, src: cw > 0.5 ? 'Rate: Freddie Mac via FRED' : null, srcA: ok });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
