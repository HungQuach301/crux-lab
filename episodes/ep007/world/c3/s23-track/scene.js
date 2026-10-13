// Tập 7 · C3 · s23-track (B23) · N1 đường tháng: 12 lớp trả thêm (ink) của mỗi cột-năm TRƯỢT về ô thứ 12, chồng thành MỘT khối 12 lớp (cùng tổng)
// → đồ thị, máy giữ góc 3/4: "$8,792 once a year"; đường kết thúc muộn 4 ô warn ("ends in 184 months: 4 months later than monthly").
import { setup, trackWorld, TRACK_POSES, nameTag, modeLook, chrome, label, kf, show, ease } from '/episodes/ep007/world/c3kit.js';
import { MonthTrack } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s23-track/';

export async function boot(res) {
  // đồ thị ở góc 3/4 (vòng 3, REVIEW-C3 CHÍNH-5 + đạo diễn #2): nhìn thẳng xuống làm khối năm thành ô vuông phẳng — mất "một khối dày = 12 lớp"
  // máy ở phía trước lưới (trục năm vẫn trái → phải), cao ~32°: vạch 15 năm không che ô trễ phía sau nó
  const poses = { ...TRACK_POSES, cQ: { pos: [2.1, 6.2, 7.8], tgt: [2.1, 0.1, -2.3], fov: 41, chart: 1 } };
  const { S, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const { hm, track } = await trackWorld(scene, MonthTrack), b = cue, T = track.userData;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const gp = S.gather.map(([a, z]) => ease(t, a, z));
    track.set({ lit: T.n, late: kf(S.late, t), extra: T.years, gathered: gp, pulse: show(t, b.a2.four) * (1 - show(t, b.a2.four + 0.6)) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm);
    const [gx0, gy0] = O.toScreen(track.colX(0, -1), T.th, track.backZ()), [gx1, gy1] = O.toScreen(track.colX(T.years + 1, 1), T.th, track.frontZ());
    const [fx0, fy0] = O.toScreen(track.colX(0, -1), T.th, track.frontZ()), [mx, my] = O.toScreen(track.markWorldX(), 0, track.frontZ());
    const [c1x, c1y] = O.toScreen(track.colX(1, 1), 0, track.frontZ());
    const [bx0, by0] = O.toScreen(...track.blockTop(0)), [bx1, by1] = O.toScreen(...track.blockTop(T.years - 1));
    log.roi['a0.once'] = [Math.min(gx0, fx0) - 10, by0 - 30, c1x + 10, c1y + 10];
    log.roi['a1.extra'] = [Math.min(gx0, fx0), Math.min(by0, by1) - 30, mx, my];
    log.roi['a2.ends'] = [mx - 10, gy0, gx1 + 20, gy1 + 10];
    label(O, D('yearly_lump'), bx0, Math.min(by0, by1) - 40, { kind: 'number', alpha: ok * show(t, b.a1.one), claims: ['yearly_lump'] });
    log.roi['a1.one'] = [bx0, Math.min(by0, by1) - 92, bx0 + 560, Math.min(by0, by1) - 22];
    const ly = Math.max(fy0, gy1) + 70;
    label(O, `ends in ${D('yearly_lump_months')}: ${D('yearly_lump_late')} than monthly`, 1820, ly, { align: 'right', kind: 'number', alpha: ok * show(t, b.a2.four),
      claims: ['yearly_lump_months', 'yearly_lump_late'] });
    log.roi['a2.four'] = [660, ly - 50, 1820, ly + 20];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
