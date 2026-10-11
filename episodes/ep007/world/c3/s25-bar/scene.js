// Tập 7 · C3 · s25-bar (B25, KEY-10) · the bar: tờ đô la trả thêm đặt lên thanh (W3, ink-muted), thanh dâng cạnh nhà tới độ cao lãi khoản vay →
// đồ thị: "the bar: 7.40% a year, before taxes"; tờ thứ hai "any other use" đặt áp vào đầu thanh để so (không trèo qua); "not tested: …".
import { setup, home, nameTag, modeLook, chrome, label, kf, show, ease } from '/episodes/ep007/world/c3kit.js';
import { Beam } from '/toolkit/factory/world/lib3d.js';
import { Bill } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s25-bar/';
const PER_PCT = 0.3, BX = 0.6, BL = 3.0;   // độ cao thế giới mỗi điểm % lãi; tâm và chiều dài thanh

export async function boot(res) {
  const poses = {
    wB: { pos: [-4.6, 2.5, 7.6], tgt: [-0.4, 1.0, 0], fov: 38, chart: 0 },
    cB: { pos: [0.1, 1.45, 18], tgt: [0.1, 1.45, 0], fov: 19, chart: 1 },
  };
  const { S, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const b = cue, hm = home(scene, { x: -2.3 });
  const beam = Beam({ length: BL }); beam.scale.set(1, 2.2, 1.4); scene.add(beam); beam.userData.checks = { role: 'mark', series: 'bar', key: 'the-bar' };
  const d1 = Bill({ name: 'extra-dollar' }), d2 = Bill({ name: 'any-other-use' }); scene.add(d1, d2);
  const hand = [hm.person.position.x + 0.35, 0.62, hm.person.position.z + 0.15];

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const H = Math.max(0.06, kf(S.bar, t) * PER_PCT);
    beam.position.set(BX, H, 0); beam.userData.checks.value = +kf(S.bar, t).toFixed(3);
    // tờ 1: hiện trong tay Tessa → đặt ĐỨNG trên mặt thanh (mặt tờ hướng máy, cạnh dưới chạm thanh), cưỡi lên theo thanh
    const a1 = show(t, S.dollar1.appear), [p0, p1] = S.dollar1.place, x1 = ease(t, p0, p1), top = [BX - 0.5, H + 0.08 + 0.14, 0];
    d1.rotation.x = (Math.PI / 2) * Math.max(x1, 0.35);
    d1.position.set(hand[0] + (top[0] - hand[0]) * x1, hand[1] + (top[1] - hand[1]) * x1 + 1.7 * Math.sin(Math.PI * x1), hand[2] + (top[2] - hand[2]) * x1 + 1.0 * Math.sin(Math.PI * x1));   // cung đi trước mặt nhà, không xuyên mái
    d1.scale.setScalar(Math.max(0.001, a1)); d1.visible = a1 > 0.01;
    // tờ 2: hiện dưới đầu phải thanh, đứng thẳng, được ĐẶT ÁP vào đầu thanh ở đúng độ cao thanh (so, không vượt)
    const a2 = show(t, S.dollar2.appear), [q0, q1] = S.dollar2.hold, x2 = ease(t, q0, q1), endX = BX + BL / 2 + 0.36;
    d2.rotation.x = Math.PI / 2; d2.position.set(endX + 0.55 * (1 - x2), 0.75 + (H - 0.75) * x2, 0.05);
    d2.scale.setScalar(Math.max(0.001, a2)); d2.visible = a2 > 0.01;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm);
    const [bx0, by] = O.toScreen(BX - BL / 2, H, 0), [bx1] = O.toScreen(BX + BL / 2, H, 0), [, fy] = O.toScreen(BX, 0, 0), bc = (bx0 + bx1) / 2;
    const [hx, hy] = O.toScreen(...hand); log.roi['a0.dollar'] = [hx - 80, hy - 80, hx + 80, hy + 80];
    log.roi['a0.charged'] = [bx0 - 20, by - 40, bx1 + 20, fy + 10];
    label(O, `the bar: ${D('bar_now')}`, bc, by - 86, { align: 'center', kind: 'number', alpha: ok * show(t, b.a1.seven), claims: ['bar_now'] });
    log.roi['a1.seven'] = [bc - 520, by - 150, bc + 520, by - 70];
    // chiều cao thanh = lãi: vạch đo đứng ink-muted từ sàn tới thanh, ngay trái thanh (chỉ đồ thị; nét lớp phủ, không chữ)
    const [dx, dy0] = O.toScreen(BX - BL / 2 - 0.18, 0, 0), dA = ok; if (dA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = dA; c.strokeStyle = '#9AA4B2'; c.lineWidth = 4;
      c.beginPath(); c.moveTo(dx - 12, dy0); c.lineTo(dx + 12, dy0); c.moveTo(dx, dy0); c.lineTo(dx, by); c.moveTo(dx - 12, by); c.lineTo(dx + 12, by); c.stroke(); c.restore(); }
    // hai ý → hai dòng (visual-library §1), dưới thanh, bên phải tên Tessa
    const i2 = ok * show(t, b.a2.investment);
    label(O, 'interest no longer charged,', 960, by + 150, { kind: 'compare', px: 48, alpha: i2 });
    label(O, 'not an investment return', 960, by + 218, { kind: 'compare', px: 48, alpha: i2 });
    log.roi['a2.investment'] = [950, by + 100, 1640, by + 240];
    const [ux, uy] = O.toScreen(endX + 0.4, H, 0);
    label(O, 'any other use', ux, uy + 17, { kind: 'name', px: 48, alpha: show(t, b.a3.other) });
    log.roi['a3.other'] = [ux - 140, uy - 60, ux + 360, uy + 40]; log.roi['a3.measured'] = [ux - 160, uy - 120, ux, fy];
    label(O, 'not tested: whether any investment clears it', bc, by - 172, { align: 'center', kind: 'compare', alpha: ok * show(t, b.a4.whether) });
    log.roi['a4.whether'] = [bc - 620, by - 236, bc + 620, by - 156];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
