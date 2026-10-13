// Tập 7 · C3 · s25-bar (B25, KEY-10) · the bar: tờ đô la trả thêm rời tay Tessa; thanh (W3, ink-muted) trồi lên từ sàn ngay dưới tờ đô la rồi dâng
// tới độ cao lãi khoản vay → đồ thị: "the bar: 7.40% a year, before taxes"; vòng 3: tờ thứ hai "any other use" là BÓNG nét đứt đứng TÁCH khỏi
// đầu thanh, lên xuống nhẹ quanh độ cao thanh, không dừng trên hay dưới (độ cao để mở); "not tested: how any investment compares, …".
import { setup, home, nameTag, modeLook, chrome, label, kf, show, ease, setOpacity } from '/episodes/ep007/world/c3kit.js';
import { Beam } from '/toolkit/factory/world/lib3d.js';
import { Bill } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s25-bar/';
const PER_PCT = 0.3, BX = 0.6, BL = 3.0;   // độ cao thế giới mỗi điểm % lãi; tâm và chiều dài thanh
const GX = BX + BL / 2 + 1.2, BOB = 0.32, BOB_T = 2.6;   // bóng đô la thứ hai: tách đầu thanh 1,2; biên độ / chu kỳ lên xuống

export async function boot(res) {
  const poses = {
    wB: { pos: [-4.6, 2.5, 7.6], tgt: [-0.4, 1.0, 0], fov: 38, chart: 0 },
    cB: { pos: [0.1, 1.45, 18], tgt: [0.1, 1.45, 0], fov: 19, chart: 1 },
  };
  const { S, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const b = cue, hm = home(scene, { x: -2.3 });
  const beam = Beam({ length: BL }); beam.scale.set(1, 2.2, 1.4); scene.add(beam); beam.userData.checks = { role: 'mark', series: 'bar', key: 'the-bar' };
  const d1 = Bill({ name: 'extra-dollar' }), d2 = Bill({ name: 'any-other-use' }); scene.add(d1, d2);
  setOpacity(d2, 0.28);   // bóng: cùng cỡ tờ thật, mờ + viền nét đứt ở lớp phủ
  const hand = [hm.person.position.x + 0.35, 0.62, hm.person.position.z + 0.15];
  const [land0, land1] = S.dollar1.place;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    // thanh: chưa có gì trên sàn; trồi lên từ dưới sàn ngay khi tờ đô la tới chỗ (0,25 s), rồi dâng tới độ cao lãi
    const up = ease(t, land1 - 0.1, land1 + 0.15), H = -0.12 + (0.12 + Math.max(0.06, kf(S.bar, t) * PER_PCT)) * up;
    beam.position.set(BX, H, 0); beam.visible = up > 0.01; beam.userData.checks.value = +kf(S.bar, t).toFixed(3);
    // tờ 1: hiện trong tay Tessa → bay vòng trước mặt nhà, ĐỨNG trên mặt thanh (cạnh dưới chạm thanh), cưỡi lên theo thanh
    const a1 = show(t, S.dollar1.appear), x1 = ease(t, land0, land1), top = [BX - 0.5, Math.max(H, 0.06) + 0.08 + 0.14, 0];
    d1.rotation.x = (Math.PI / 2) * Math.max(x1, 0.35);
    d1.position.set(hand[0] + (top[0] - hand[0]) * x1, hand[1] + (top[1] - hand[1]) * x1 + 1.0 * Math.sin(Math.PI * x1), hand[2] + (top[2] - hand[2]) * x1 + 1.0 * Math.sin(Math.PI * x1));
    d1.scale.setScalar(Math.max(0.001, a1)); d1.visible = a1 > 0.01;
    // tờ 2 (bóng): hiện tại chỗ, tách đầu thanh ("other"), lên xuống quanh độ cao thanh — biên độ lớn dần tới "measured" rồi giữ tới hết đoạn
    // (luôn chuyển động: không có khung nào bóng đứng yên ngang, trên hay dưới thanh)
    const a2 = show(t, S.dollar2.appear), [q0, q1] = S.dollar2.hold, Hb = kf(S.bar, t) * PER_PCT;
    const bob = BOB * Math.sin((2 * Math.PI * (t - S.dollar2.appear)) / BOB_T) * (0.35 + 0.65 * ease(t, q0, q1));
    const p2 = [GX, Hb + bob, 0.05];
    d2.rotation.x = Math.PI / 2; d2.position.set(...p2);
    d2.scale.setScalar(Math.max(0.001, a2)); d2.visible = a2 > 0.01;
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm);
    const [bx0, by] = O.toScreen(BX - BL / 2, Hb, 0), [bx1] = O.toScreen(BX + BL / 2, Hb, 0), [, fy] = O.toScreen(BX, 0, 0), bc = (bx0 + bx1) / 2;
    const [hx, hy] = O.toScreen(...hand); log.roi['a0.dollar'] = [hx - 80, hy - 80, hx + 80, hy + 80];
    log.roi['a0.charged'] = [bx0 - 20, by - 40, bx1 + 20, fy + 10];
    label(O, `the bar: ${D('bar_now')}`, bc, by - 118, { align: 'center', kind: 'number', alpha: ok * show(t, b.a1.seven), claims: ['bar_now'] });
    log.roi['a1.seven'] = [bc - 520, by - 182, bc + 520, by - 102];
    // chiều cao thanh = lãi: vạch đo đứng ink-muted từ sàn tới thanh, ngay trái thanh (chỉ đồ thị; nét lớp phủ, không chữ)
    const [dx, dy0] = O.toScreen(BX - BL / 2 - 0.18, 0, 0), dA = ok; if (dA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = dA; c.strokeStyle = '#9AA4B2'; c.lineWidth = 4;
      c.beginPath(); c.moveTo(dx - 12, dy0); c.lineTo(dx + 12, dy0); c.moveTo(dx, dy0); c.lineTo(dx, by); c.moveTo(dx - 12, by); c.lineTo(dx + 12, by); c.stroke(); c.restore(); }
    // viền nét đứt quanh bóng đô la (cùng cỡ tờ thật): "độ cao chưa biết", không phải phần nối dài của thanh
    if (a2 > 0.01) {
      const q = [[-0.31, -0.14], [0.31, -0.14], [0.31, 0.14], [-0.31, 0.14]].map(([u, v]) => O.toScreen(p2[0] + u * a2, p2[1] + v * a2, p2[2] + 0.02)), c = O.ctx;
      c.save(); c.globalAlpha = a2; c.strokeStyle = '#F2F4F7'; c.lineWidth = 3; c.setLineDash([9, 7]); c.beginPath();
      q.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.closePath(); c.stroke(); c.restore();
    }
    // chữ cột phải: hai ý → hai dòng (visual-library §1), dưới thanh; "not tested" hai dòng ngay dưới (bỏ chồng ba nhãn ở đỉnh khung);
    // "any other use" ngay dưới đáy hành trình của bóng (chữ đứng yên, không gợi độ cao nào)
    const XR = 820, i2 = ok * show(t, b.a2.investment);
    label(O, 'interest no longer charged,', XR, by + 215, { kind: 'compare', px: 48, alpha: i2 });
    label(O, 'not an investment return', XR, by + 280, { kind: 'compare', px: 48, alpha: i2 });
    log.roi['a2.investment'] = [XR - 10, by + 165, XR + 700, by + 300];
    const [ux, uy] = O.toScreen(GX, Hb - BOB - 0.22, 0);
    label(O, 'any other use', ux, uy + 44, { align: 'center', kind: 'name', px: 48, alpha: show(t, b.a3.other) });
    const [gx0, gy0] = O.toScreen(GX - 0.5, Hb + BOB + 0.3, 0), [gx1, gy1] = O.toScreen(GX + 0.5, Hb - BOB - 0.3, 0);
    log.roi['a3.other'] = log.roi['a3.measured'] = [gx0, gy0, gx1, gy1];
    const n4 = ok * show(t, b.a4.whether);
    label(O, 'not tested: how any investment compares,', XR, by + 365, { kind: 'compare', px: 48, alpha: n4 });
    label(O, 'once risk and taxes count', XR, by + 430, { kind: 'compare', px: 48, alpha: n4 });
    log.roi['a4.whether'] = [XR - 10, by + 315, 1840, by + 450];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
