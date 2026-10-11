// Tập 7 · C3 · s21-track (B21, KEY-9) · N1 đường tháng từ nhà Tessa: 180 ô, vạch 15 năm → đồ thị: 14,6 ô warn quá vạch ("about 195 months",
// "about 15 months late") → lớp trả thêm (cushion) phủ từng cột, ô trễ tắt, đường xong đúng ô 180 ("to finish in 180 months: +$733 a month").
import { setup, trackWorld, TRACK_POSES, nameTag, modeLook, chrome, label, kf, show, C } from '/episodes/ep007/world/c3kit.js';
import { MonthTrack } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s21-track/';

export async function boot(res) {
  const { S, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, TRACK_POSES);
  const { hm, track } = await trackWorld(scene, MonthTrack), b = cue, T = track.userData;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const late = kf(S.late, t);
    track.set({ lit: kf(S.lit, t), late, extra: kf(S.extra, t), markA: show(t, S.mark_t), pulse: show(t, b.a1.late) * (1 - show(t, b.a1.late + 0.6)) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm, 1, { dx: -40 - 60 * cw, dy: -200 * cw });
    const [gx0, gy0] = O.toScreen(track.colX(0, -1), T.th, track.backZ()), [gx1, gy1] = O.toScreen(track.colX(T.years + 1, 1), T.th, track.frontZ());
    const [mx] = O.toScreen(track.markWorldX(), 0, track.frontZ());
    log.roi['a0.pay'] = [gx0, gy0, gx1, gy1]; log.roi['a2.add'] = [gx0, gy0, mx, gy1];
    log.roi['a0.same'] = [mx - 30, gy0 - 10, mx + 30, gy1 + 10]; log.roi['a1.doesnt'] = [mx, gy0, gx1 + 10, gy1];
    const old = 1 - show(t, S.old_out);   // nhãn của trạng thái "trễ" tắt khi lớp trả thêm bắt đầu
    label(O, `pay ${D('pay15_now')} on the 30-year: ${D('months_at_pay15_now')}`, gx0, gy1 + 70, { kind: 'number', alpha: ok * show(t, b.a1.ends) * old,
      claims: ['pay15_now', 'months_at_pay15_now'] });
    log.roi['a1.ends'] = [gx0, gy1 + 20, gx0 + 1100, gy1 + 90];
    const [lx] = O.toScreen(track.colX(T.years + 1, 1), 0, track.backZ());
    label(O, D('months_late_at_pay15_now'), Math.min(1800, lx + 40), gy0 - 40, { align: 'right', kind: 'number', color: C.ink, alpha: ok * show(t, b.a1.late) * old, claims: ['months_late_at_pay15_now'] });
    log.roi['a1.late'] = [lx - 520, gy0 - 100, lx + 50, gy0 - 30];
    label(O, `to finish in ${D('monthly_extra_months')}: +${D('extra_principal_needed_now')}`, gx0, gy1 + 70, { kind: 'number', alpha: ok * show(t, b.a2.seven),
      claims: ['monthly_extra_months', 'extra_principal_needed_now'] });
    log.roi['a2.seven'] = [gx0, gy1 + 20, gx0 + 960, gy1 + 90];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
