// Tập 7 · C3 · s06-stack (B06, KEY-3) · vòng 2: vạch mức 15 năm (ink-muted) qua hai thanh; đồ thị thấy thanh 30 năm NGẮN hơn ("required") rồi dâng
// lên $2,948, vượt vạch một lát (warn); mỗi nhịp lát tách khỏi đỉnh thanh 30 năm, bay sang the stack (15 lần) → "the stack: $21,622 extra paid …".
import { setup, home, nameTag, theStack, stackSet, BUNDLE_TH, modeLook, chrome, label, kf, show, ease, C, THREE } from '/episodes/ep007/world/c3kit.js';
import { PayBar, TRACK } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s06-stack/';
const SCALE = 1 / 1230;   // USD/tháng → chiều cao thế giới (thanh khoản trả); chồng dùng thang bó riêng (BUNDLE_TH mỗi năm)
const BAR_W = 0.8, BAR_D = 0.5, FLY_W = 0.9, FLY_D = 0.6;

export async function boot(res) {
  const poses = {
    wS: { pos: [-4.4, 2.7, 8.4], tgt: [-0.6, 1.1, 0], fov: 38, chart: 0 },
    cS: { pos: [-0.3, 1.5, 20], tgt: [-0.3, 1.5, 0], fov: 19, chart: 1 },
  };
  const { S, CL, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  const G = CL._geom, b = cue;
  // trái → phải: nhà · the stack · thanh 15 năm · thanh 30 năm (chồng nằm giữa nhà và thanh: lát bay từ thanh 30 năm qua đỉnh thanh 15 năm vào chồng)
  const hm = home(scene, { x: -2.8 }), stack = theStack(scene, G, { x: -1.1 });
  const bar15 = PayBar({ w: BAR_W, d: BAR_D, scale: SCALE, name: '15-year' }), bar30 = PayBar({ w: BAR_W, d: BAR_D, scale: SCALE, name: '30-year' });
  bar15.position.set(0.2, 0, 0); bar30.position.set(1.4, 0, 0); scene.add(bar15, bar30);
  // vạch mức 15 năm: ink-muted, đứng yên, trước mặt hai thanh, kéo qua cả hai (hiện từ trái sang ở "finishing")
  const top15 = bar15.topY(G.pay15), lx0 = bar15.position.x - BAR_W / 2 - 0.15, lx1 = bar30.position.x + BAR_W / 2 + 0.15, LZ = BAR_D / 2 + 0.02;
  const lvGeo = new THREE.BoxGeometry(1, 0.035, 0.02); lvGeo.translate(0.5, 0, 0);
  const level = new THREE.Mesh(lvGeo, new THREE.MeshBasicMaterial({ color: TRACK.mark }));
  level.position.set(lx0, top15, LZ); level.userData.checks = { role: 'mark', key: 'level-15', value: G.pay15 }; scene.add(level);
  // lát đang bay (tối đa 2 cùng lúc: FLY 0,8 s, nhịp ~0,42 s): bắt đầu TRÙNG lát warn trên đỉnh thanh 30 năm, nhấc lên, vòng ra trước thanh 15 năm,
  // thành bó trên đỉnh chồng
  const flyMat = new THREE.MeshStandardMaterial({ color: TRACK.warn, roughness: 0.8, emissive: new THREE.Color(TRACK.warn), emissiveIntensity: 0.25 });
  const flies = [0, 1, 2].map(() => { const m = new THREE.Mesh(new THREE.BoxGeometry(FLY_W, BUNDLE_TH, FLY_D), flyMat); m.castShadow = true; scene.add(m); return m; });
  const sliver = (G.pay30on15 - G.pay15) * SCALE;
  const path = (k, p) => {   // p ∈ [0,1] (sau pha nhấc): toạ độ thế giới của lát k
    const ys = top15 + sliver / 2 + 0.22, ye = k * BUNDLE_TH + BUNDLE_TH / 2;
    return [bar30.position.x + (stack.position.x - bar30.position.x) * p, ys + (ye - ys) * p ** 4 + 0.4 * Math.sin(Math.PI * p), 0.75 * Math.sin(Math.PI * p)];
  };
  const LIFT = 0.18;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    bar15.set({ usd: G.pay15 });
    const u30 = kf(S.bar30, t); bar30.set({ usd: u30, warnAbove: G.pay15, topA: Math.min(1, Math.max(0, (u30 - G.pay15) / (G.pay30on15 - G.pay15))) });
    const lv = ease(t, S.level_t - 0.05, S.level_t + 0.5); level.scale.x = Math.max(0.001, (lx1 - lx0) * lv); level.visible = lv > 0.01;
    stackSet(stack, kf(S.stack, t));
    // lát bay: k rời đỉnh thanh drop_dur s trước khi chạm chồng
    let n = 0, trail = null; for (const f of flies) f.visible = false;
    for (let k = 0; k < S.drops.length && n < flies.length; k++) {
      const t1 = S.drops[k], t0 = t1 - S.drop_dur; if (t < t0 || t >= t1) continue;
      const u = (t - t0) / S.drop_dur, lift = Math.min(1, u / LIFT), p = Math.max(0, (u - LIFT) / (1 - LIFT)), f = flies[n++];
      let [x, y, z] = path(k, p); if (p === 0) y = top15 + sliver / 2 + 0.22 * lift;
      const s = Math.min(1, p * 1.6);   // lát (bề ngang/sâu thanh, dày = phần dôi) → bó
      f.position.set(x, y, z); f.scale.set((BAR_W / FLY_W) * (1 - s) + 0.85 * s, (sliver / BUNDLE_TH) * (1 - s) + 0.92 * s, (BAR_D / FLY_D) * (1 - s) + s); f.visible = true;
      if (p > 0 && (!trail || t0 > trail.t0)) trail = { k, p, t0 };
    }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm);
    // vệt đường bay của lát mới nhất (warn mờ): nối đỉnh thanh 30 năm với lát → thấy nguồn gốc
    if (trail && ok) {
      const c = O.ctx; c.save(); c.globalAlpha = 0.4 * (1 - ease(trail.p, 0.75, 1)); c.strokeStyle = TRACK.warn; c.lineWidth = 4; c.setLineDash([10, 10]); c.beginPath();
      for (let i = 0; i <= 16; i++) { const [x, y, z] = path(trail.k, (trail.p * i) / 16), [sx, sy] = O.toScreen(x, y, z); i ? c.lineTo(sx, sy) : c.moveTo(sx, sy); }
      c.stroke(); c.restore();
    }
    // tên thanh dưới chân; số: "$2,828 a month" ở đầu trái vạch mức 15 năm, "required: …" trên thanh 30 năm (tắt khi dâng), "30-year paid in 15"
    // trên cặp thanh (căn phải), "+$120" ngay phải lát warn, nhãn chồng cao nhất
    const [x15, f15] = O.toScreen(bar15.position.x, 0, 0.3), [x30, f30] = O.toScreen(bar30.position.x, 0, 0.3), [, y30] = O.toScreen(bar30.position.x, bar30.topY(G.pay30on15), 0);
    label(O, '15-year', x15, f15 + 52, { align: 'center', kind: 'name', px: 48, w: 240, alpha: ok });
    label(O, '30-year', x30, f30 + 52, { align: 'center', kind: 'name', px: 48, w: 240, alpha: ok });
    const [vx, vy] = O.toScreen(lx0, top15, LZ);
    label(O, D('pay15_month'), vx - 14, vy + 16, { align: 'right', kind: 'number', alpha: ok * show(t, 0, b.a1.same), claims: ['pay15_month'] });
    const [rx, ry] = O.toScreen(bar30.position.x - BAR_W / 2, bar30.topY(G.pay30), 0);
    label(O, `required: ${D('pay30_now')}`, rx, ry - 30, { kind: 'number', alpha: ok * show(t, 0, b.a0.forty), claims: ['pay30_now'] });
    label(O, `30-year paid in 15: ${D('pay30on15_now')}`, 1800, y30 - 95, { align: 'right', kind: 'number', alpha: ok * show(t, b.a0.forty), claims: ['pay30on15_now'] });
    const [xs, ys] = O.toScreen(bar30.position.x + BAR_W / 2, top15 + sliver / 2, 0);
    label(O, `+${D('extra_vs15_month_now')}`, xs + 26, ys + 18, { kind: 'number', px: 56, alpha: ok * show(t, b.a1.one), claims: ['extra_vs15_month_now'] });
    const [kx, ky] = O.toScreen(stack.position.x, 15 * BUNDLE_TH, 0), sy = Math.min(ky, y30) - 165;
    label(O, `the stack: ${D('extra_vs15_total_now')} extra paid over 15 years`, kx, sy, { align: 'center', kind: 'number', alpha: ok * show(t, b.a2.twenty), claims: ['extra_vs15_total_now'] });
    const [lsx0, lsy0] = O.toScreen(lx0, top15 + 0.15, LZ), [lsx1, lsy1] = O.toScreen(lx1, top15 - 0.15, LZ);
    log.roi['a0.finishing'] = [lsx0, lsy0, lsx1, lsy1];
    const [bx0, by0] = O.toScreen(bar30.position.x - 0.5, bar30.topY(G.pay30on15) + 0.3, 0), [bx1, by1] = O.toScreen(bar30.position.x + 0.5, bar30.topY(G.pay30) - 0.1, 0);
    log.roi['a0.forty'] = [Math.min(900, bx0), y30 - 150, 1810, by1];
    log.roi['a1.one'] = [xs, ys - 50, xs + 420, ys + 40];
    const [sx0, sy0] = O.toScreen(stack.position.x - 0.5, 15 * BUNDLE_TH + 0.5, 0), [sx1, sy1] = O.toScreen(bar30.position.x + 0.5, 0, 0);
    log.roi['a1.same'] = [sx0, sy0, sx1, sy1];
    log.roi['a2.twenty'] = [kx - 600, sy - 55, kx + 600, sy + 15];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
