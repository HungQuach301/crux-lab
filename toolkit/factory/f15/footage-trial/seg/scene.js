// F-15 (f) · CLIP THỬ FOOTAGE 8 s (không thuộc tập nào): thế giới 3D → plate ảnh (Ken Burns quanh focus, tông kênh, chú thích/nguồn không đè chủ thể)
// → bản đồ South Atlantic (vùng tô theo phân vùng Census, nhãn neo vào mốc từ của words.json) → về thế giới 3D.
//   node toolkit/factory/world/render_shots.js toolkit/factory/f15/footage-trial/seg 540 <out.mp4>   (run.sh làm cả hai lượt)
// Chưa có plate.json (lượt 1 của run.sh): chỉ thế giới 3D, không chữ — tạo ảnh THAY THẾ khi ảnh LoC chưa tải được (mạng chặn loc.gov).
import * as THREE from 'three';
import { Stage, CK, loadJSON, fonts } from '/toolkit/factory/world/core.js';
import { Studio, House, Person, Neighborhood } from '/toolkit/factory/world/lib3d.js';
import { loadImage, toneImage, drawPlate, drawCredits, drawMap, envelope } from '/toolkit/factory/world/plate.js';

const SEG = '/toolkit/factory/f15/footage-trial/seg/';
const lerp = (a, b, u) => a.map((v, i) => v + (b[i] - v) * u);
const sm = (u) => { u = Math.max(0, Math.min(1, u)); return u * u * (3 - 2 * u); };

export async function boot(res) {
  const opt = async (u) => { const r = await fetch(u); return r.ok ? r.json() : null; };
  const [W, P, M] = await Promise.all([loadJSON(SEG + 'words.json'), opt(SEG + 'plate.json'), opt(SEG + 'map.json')]);
  const still = !P || !M;
  await fonts();
  const st = Stage(res), O = st.O, renderer = st.renderer, scene = new THREE.Scene();
  Studio(scene, { shadowBox: 10 });
  const house = House({ w: 1.7 }); house.position.set(0.4, 0, 0); scene.add(house);
  const person = Person({ h: 1.0 }); person.position.set(-1.0, 0, 0.6); scene.add(person);
  scene.add(Neighborhood({ n: 10, seed: 15, spanX: [-7, 7], z: -4.0, size: 0.55 }));
  const cam = new THREE.PerspectiveCamera(34, 16 / 9, 0.1, 200);
  const A = { pos: [-3.2, 2.4, 8.4], tgt: [0.0, 0.8, 0] }, B = { pos: [-2.4, 1.9, 6.6], tgt: [0.1, 0.9, 0] };
  let plate = null;
  if (P) { const img = await loadImage(P.src); plate = { ...P, src: toneImage(img, P.tone || {}) }; }
  const at = (w) => W.words.find((x) => x.w.replace(/[^A-Za-z]/g, '') === w).s;
  const reveal = {}, order = ['FL', 'GA', 'SC', 'NC', 'VA', 'WV', 'MD', 'DE', 'DC'];
  if (M) order.forEach((id, i) => { reveal[id] = at('South') + i * 0.12; });   // phân vùng tô dần từ "South" (theo bờ biển, nam → bắc)
  // nhãn neo vào từ; chỗ đặt không chồng nhau: tên phân vùng dưới bản đồ, "Maryland" lệch phải (bang nhỏ, sát mép trên)
  const labels = M ? [{ text: 'South Atlantic', at: at('South'), x: (M.focus_box[0] + M.focus_box[2]) / 2, y: M.focus_box[3] + 40, px: 56 },
    { id: 'FL', text: 'Florida', at: at('Florida') }, { id: 'MD', text: 'Maryland', at: at('Maryland'), x: M.features.find((f) => f.id === 'MD').label[0] + 190 }] : [];
  function frame(t) {
    const u = sm(t / 8), c = { pos: lerp(A.pos, B.pos, u), tgt: lerp(A.tgt, B.tgt, u) };
    cam.position.fromArray(c.pos); cam.lookAt(...c.tgt); cam.updateMatrixWorld(true);
    renderer.render(scene, cam);
    const log = O.begin(t, 0, cam);
    if (!still) {
      const p = plate ? drawPlate(O, plate, t) : { a: 0 };
      if (p.a > 0.01) drawCredits(O, log, p.subject, { caption: plate.caption, source: plate.source }, p.a);
      const ma = envelope(t, M.t0, M.t1, M.fade[0], M.fade[1]);
      const shown = drawMap(O, M, t, { a: ma, reveal, labels });
      if (ma > 0.01) { O.text(M.source_line, 1824, 1006, 40, { kind: 'chrome', w: 600, color: '#C9D1DC', align: 'right', alpha: ma }); log.map = { a: +ma.toFixed(3), labels: shown.map((s) => ({ text: s.text, at: s.at })) }; }
    }
    st.compose(); log.camMoving = true; return log;
  }
  return { canvas: st.out, frame };
}
