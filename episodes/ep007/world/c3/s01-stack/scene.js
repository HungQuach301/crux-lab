// Tập 7 · C3 · s01-stack (B01, KEY-1) · Tessa cạnh nhà; mỗi bó tiền (warn = giá của khoản dự phòng) đi RA TỪ CỬA NHÀ, bay sang the stack cạnh nhà
// → đồ thị: "price of the fallback: $120 a month" trên chồng (hiện đúng lúc bó đầu chạm), "$320,000 loan · week of Oct 8, 2026" trên nhà.
import { setup, home, nameTag, theStack, stackSet, BUNDLE_TH, modeLook, chrome, label, kf, show, ease, THREE } from '/episodes/ep007/world/c3kit.js';
import { TRACK } from '/episodes/ep007/world/obj7.js';

const SEG = '/episodes/ep007/world/c3/s01-stack/';
const FLY_W = 0.9 * 0.85, FLY_D = 0.6;   // bó bay = cỡ bó trong chồng

export async function boot(res) {
  const poses = {
    wS0: { pos: [-3.6, 2.7, 8.6], tgt: [0.3, 0.7, 0], fov: 35, chart: 0 },
    wS: { pos: [-2.5, 2.0, 6.6], tgt: [0.3, 0.75, 0], fov: 35, chart: 0 },
    cS: { pos: [0.3, 1.2, 18], tgt: [0.3, 1.2, 0], fov: 15, chart: 1 },
  };
  const { S, CL, D, cue, st, O, renderer, scene, floor, CAM } = await setup(SEG, res, poses);
  // chồng lùi sang phải (vòng 3): nhãn giá trên chồng không đè mép tường / mái nhà
  const hm = home(scene, { x: -0.3 }), stack = theStack(scene, CL._geom, { x: 1.85 });
  const b = cue;
  // bó bay: hộp warn + đai (như bó trong chồng); tối đa 2 cùng lúc
  const flyMat = new THREE.MeshStandardMaterial({ color: TRACK.warn, roughness: 0.8 }), strapMat = new THREE.MeshStandardMaterial({ color: '#E9E2CF', roughness: 0.8 });
  const flies = [0, 1].map(() => {
    const g = new THREE.Group(), m = new THREE.Mesh(new THREE.BoxGeometry(FLY_W, BUNDLE_TH * 0.92, FLY_D), flyMat), s = new THREE.Mesh(new THREE.BoxGeometry(FLY_W * 0.16, BUNDLE_TH * 0.94, FLY_D * 1.02), strapMat);
    m.castShadow = true; g.add(m, s); scene.add(g); return g;
  });
  const door = [hm.house.position.x, BUNDLE_TH / 2 + 0.02, 0.58 + FLY_D / 2 + 0.05];   // bậc cửa (trước cửa nhà, lib3d House: cửa giữa mặt trước)
  const path = (k, p) => {   // bậc cửa → đỉnh chồng (bó thứ k), vòng ra trước rồi hạ xuống
    const ye = k * BUNDLE_TH + BUNDLE_TH / 2, e = p * p * (3 - 2 * p);
    return [door[0] + (stack.position.x - door[0]) * e, door[1] + (ye - door[1]) * e + 0.55 * Math.sin(Math.PI * p), door[2] * (1 - e) + 0.35 * Math.sin(Math.PI * p)];
  };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    modeLook(scene, floor, cw);
    const h = stackSet(stack, kf(S.stack, t));
    let n = 0; for (const f of flies) f.visible = false;
    for (let k = 0; k < S.land.length && n < flies.length; k++) {
      const t1 = S.land[k], t0 = t1 - S.fly, f = flies[n];
      // bó 0 trồi ra ở bậc cửa từ "costs" (đợi ở đó tới lúc bay); các bó sau trồi ra cửa ngay lúc bay
      const born = k === 0 ? ease(t, S.out0, S.out0 + 0.35) : ease(t, t0 - 0.2, t0);
      if (born <= 0.01 || t >= t1) continue;
      const p = Math.min(1, Math.max(0, (t - t0) / S.fly)), [x, y, z] = path(k, p), s = 0.25 + 0.75 * born;
      f.position.set(x, y, z - (1 - born) * 0.3); f.scale.setScalar(s); f.visible = true; n++;
    }
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    nameTag(O, hm);
    const [dx, dy] = O.toScreen(...door); log.roi['a0.costs'] = [dx - 90, dy - 70, dx + 90, dy + 50];
    const [sx, sy] = O.toScreen(stack.position.x, Math.max(h, 0.2) + 0.12, 0), [sx0, sy0] = O.toScreen(stack.position.x - 0.5, 0, 0);
    // nhãn giá (hai dòng, căn giữa trên chồng; theo đỉnh chồng): hiện cùng lúc bó đầu chạm
    const pa = ok * show(t, b.a1.borrowing);
    label(O, 'price of the fallback:', sx, sy - 82, { align: 'center', kind: 'number', alpha: pa });
    label(O, D('extra_vs15_month_now'), sx, sy - 20, { align: 'center', kind: 'number', px: 60, alpha: pa, claims: ['extra_vs15_month_now'] });
    log.roi['a1.borrowing'] = [sx0 - 300, sy - 140, sx0 + 500, sy0 + 10];
    const [hx, hy] = O.toScreen(hm.house.position.x, 2.35, 0);
    label(O, `${D('principal')} loan · week of ${D('last_week_short')}`, hx + 60, hy, { align: 'center', kind: 'number', alpha: ok * show(t, b.a1.three), claims: ['principal', 'last_week_short'] });
    log.roi['a1.three'] = [hx - 500, hy - 60, hx + 620, hy + 20];
    chrome(O);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
