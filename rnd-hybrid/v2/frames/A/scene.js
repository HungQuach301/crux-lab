// R&D hình lai vòng 2 · KHUNG A "giấy trong 3D": 1931, hàng người trước ngân hàng đóng cửa, Walt lo lắng.
// Dựng bằng render_shots.js của nhà máy (--stills), không sửa nhà máy: scene.js + spine.json là một "đoạn" như mọi đoạn của tập.
// Ba lớp chiều sâu: (1) tiền cảnh Walt + cột đèn, (2) trung cảnh hàng người giấy + ngân hàng low-poly, (3) hậu cảnh dãy phố + đường chân trời trong sương.
import * as THREE from 'three';
import { CHARACTERS, POSES, blendPose } from '/rnd-hybrid/cutout/rig.js';
import { lightAct, charFigure, propFigure, Bank, Row, Street, Lamp, textPlate, caption, vignette, paperGrain } from '/rnd-hybrid/v2/paper3d.js';

const ACT_NOW = 'crisis1931';
// biến thể người xếp hàng: cùng rig Walt/Ruth, đổi màu áo (không thêm nhân vật có tên)
function variant(id, base, fills, extras) {
  const b = CHARACTERS[base], rig = JSON.parse(JSON.stringify(b.rig));
  for (const [k, v] of Object.entries(fills)) for (const part of v.parts) rig[part][k === 'skin' ? 'fill' : 'fill'] = v.c;
  CHARACTERS[id] = { ...b, rig, extras: extras || b.extras };
}
const SUIT = (c) => ({ parts: ['torso', 'uaL', 'uaR', 'faL', 'faR'], c });
variant('q1', 'walt', { a: SUIT('#4B5262') }, ['collar', 'tie', 'fedora']);
variant('q2', 'ruth', { a: SUIT('#8A6F5A') });
variant('q3', 'walt', { a: SUIT('#6B5E52') }, ['collar', 'vest', 'fedora']);
variant('q4', 'walt', { a: SUIT('#3E4A5C') }, ['collar', 'fedora']);
variant('q5', 'ruth', { a: SUIT('#5E6E86') });

export async function boot(res) {
  await document.fonts.load('700 48px Inter'); await document.fonts.load('600 48px Inter'); await document.fonts.load('400 48px Inter');
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
  const scene = new THREE.Scene();
  const L = lightAct(scene, ACT_NOW, { shadowBox: 14, target: [-1, 0, -9] });

  // ---- lớp 3: hậu cảnh (đường chân trời trong sương)
  Street(scene);
  scene.add(Row({ n: 14, x0: -48, step: 7.5, z: -46, seed: 11, hRange: [18, 40], colors: ['#3A3F4A', '#454B57', '#343944'], litP: 0.16 }));
  // ---- lớp 2: dãy phố + ngân hàng + hàng người giấy
  scene.add(Row({ n: 5, x0: -30, step: 4.6, z: -16.5, seed: 3, hRange: [8, 13], litP: 0.22 }));
  scene.add(Row({ n: 6, x0: 15, step: 4.6, z: -16.5, seed: 5, hRange: [9, 15], litP: 0.2 }));
  const bank = Bank({ closed: true }); bank.position.set(0, 0.16, -12.6); scene.add(bank);
  const notice = propFigure('note', { s: 1, label: 'CLOSED' }, { wPx: 360, hPx: 440, pxPerM: 330, rimPaper: L.A.rimPaper, thick: 0.006, rimWidth: 2 });
  notice.position.set(0.0, 0.16 + 0.88 + 1.05, -14.12); scene.add(notice);
  for (const [x, z] of [[-7.5, -6.2], [8.9, -11.0]]) { const l = Lamp({ on: true }); l.position.set(x, 0.16, z); scene.add(l); }   // đèn phố: vũng sáng ấm trên hàng người
  const cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 300);
  cam.position.set(13.2, 1.3, -0.6); const tgt = new THREE.Vector3(1.6, 3.6, -13.2); cam.lookAt(tgt);
  const face = (obj, twist = 0) => { obj.rotation.y = Math.atan2(cam.position.x - obj.position.x, cam.position.z - obj.position.z) + twist; };
  const opt = { rimPaper: L.A.rimPaper, rimWidth: 3, rimShift: [-5, -6] };
  const Q = [['q4', 'stand', 'neutral', 0.25, true], ['person'], ['q2', 'stand', 'worried', 0.3], ['q1', 'phone', 'sad', 0.25, true], ['person'], ['q3', 'stand', 'worried', 0.35], ['q5', 'slump', 'sad', 0.3, true]];
  Q.forEach(([id, pose, expr, tw = 0.1, flip], i) => {
    const f = id === 'person' ? propFigure('person', { s: 2.6 }, { ...opt, wPx: 360, hPx: 760, pxPerM: 400 })
      : charFigure({ id, pose: POSES[pose], expr, flip }, { ...opt, s: 1.0, wPx: 520, hPx: 780, pxPerM: 400 });
    const y = i < 1 ? 0.16 + 0.66 : 0.16;   // người đầu còn trên bậc thềm; hàng chạy dọc vỉa hè song song mặt tiền
    f.position.set(-0.2 + 1.25 * i, y, i < 1 ? -11.7 : -10.4 + 0.12 * i); face(f, tw); scene.add(f);
  });
  // ---- lớp 1: tiền cảnh — Walt lo lắng, nghiêng đầu, tay ôm sổ tiết kiệm (tờ giấy)
  const pose = { ...blendPose(POSES.stand, POSES.slump, 0.3), head: 9, uaR: 22, faR: 100, uaL: 14, faL: -20 };
  const walt = charFigure({ id: 'walt', pose, expr: 'worried' }, { s: 1.5, wPx: 820, hPx: 1152, pxPerM: 600, thick: 0.02, rimPaper: L.A.rimPaper, rimWidth: 4, rimShift: [-8, -9] });
  walt.position.set(10.9, 0.16, -4.6); face(walt, 0.42); scene.add(walt);
  const book = propFigure('note', { s: 0.55, label: ' ' }, { wPx: 220, hPx: 240, pxPerM: 600, thick: 0.01, rimPaper: L.A.rimPaper, rimWidth: 2 });
  book.position.set(0.02, 0.86, 0.035); book.rotation.z = -0.12; walt.add(book);   // sổ trên ngực, theo tấm giấy của Walt
  // đèn bù mặt (fill) ấm từ phía máy quay — giữ đọc được biểu cảm trong hồi tối
  const fill = new THREE.PointLight('#FFE3BF', 6, 14, 1.5); fill.position.set(12.5, 2.6, -2.2); scene.add(fill);

  // ---- ghép: 3D → khung 2D + vân giấy nhẹ + viền tối + chữ
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  function frame(t) {
    renderer.render(scene, cam);
    ctx.drawImage(renderer.domElement, 0, 0); paperGrain(ctx, W, H, 0.10); vignette(ctx, W, H, 0.42);
    caption(ctx, W, H, { title: 'New York, 1931', sub: 'A line outside a bank that closed its doors', tag: 'ILLUSTRATIVE' });
    return { violations: [] };
  }
  return { canvas: out, frame };
}
