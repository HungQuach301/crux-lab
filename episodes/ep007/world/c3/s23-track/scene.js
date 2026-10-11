// Tập 7 · C3 · s23-track (B23) · N1 đường tháng: lớp trả thêm mỏng trên mỗi ô gom thành MỘT khối trên ô thứ 12 mỗi cột-năm → đồ thị:
// "$8,792 once a year"; đường kết thúc muộn 4 ô warn ("ends in 184 months: 4 months later").
import { setup, trackWorld, TRACK_POSES, nameTag, modeLook, chrome, label, kf, show } from '/episodes/ep007/world/c3kit.js';
import { MonthTrack } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s23-track/';

export async function boot(res) {
  const { S, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, TRACK_POSES);
  const { hm, track } = await trackWorld(scene, MonthTrack), b = cue, T = track.userData;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const g = kf(S.gathered, t);
    track.set({ lit: T.n, late: kf(S.late, t), extra: T.years, gathered: g, yearly: g, pulse: show(t, b.a2.four) * (1 - show(t, b.a2.four + 0.6)) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm, 1, { dx: -40 - 60 * cw, dy: -200 * cw });
    const [gx0, gy0] = O.toScreen(track.colX(0, -1), T.th, track.backZ()), [gx1, gy1] = O.toScreen(track.colX(T.years + 1, 1), T.th, track.frontZ());
    const [c1x] = O.toScreen(track.colX(1, -1), 0, 0), [mx] = O.toScreen(track.markWorldX(), 0, track.frontZ());
    log.roi['a0.once'] = [gx0 - 10, gy0 - 40, c1x + 10, gy1 + 10];
    log.roi['a1.extra'] = [gx0, gy0 - 40, mx, gy1];
    log.roi['a2.ends'] = [mx, gy0, gx1 + 10, gy1 + 10];
    label(O, D('yearly_lump'), gx0, gy0 - 48, { kind: 'number', alpha: ok * show(t, b.a1.one), claims: ['yearly_lump'] });
    log.roi['a1.one'] = [gx0, gy0 - 100, gx0 + 560, gy0 - 30];
    label(O, `ends in ${D('yearly_lump_months')}: ${D('yearly_lump_late')}`, gx0, gy1 + 70, { kind: 'number', alpha: ok * show(t, b.a2.four),
      claims: ['yearly_lump_months', 'yearly_lump_late'] });
    log.roi['a2.four'] = [gx0, gy1 + 20, gx0 + 900, gy1 + 90];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
