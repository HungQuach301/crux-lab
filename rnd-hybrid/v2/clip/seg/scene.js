// R&D hình lai vòng 2 · CLIP 45 s "trước 1934: vay 3–5 năm, trả dồn → 1930 ngân hàng đóng → 1934 FHA → 1954 30 năm".
// Phong cách chủ dự án chọn 14/10: A (giấy trong 3D) + chất in B trên mặt giấy + C (ảnh LoC) đứng riêng toàn khung ≤ 6 s, hoà về A.
// Mốc thời gian chỉ từ timeline.json (build.py, từ dấu thời gian lời). Mỗi cảnh: hồi đèn, tư thế máy (đầu → cuối, ease), vật hiện/ẩn.
import * as THREE from 'three';
import { POSES, blendPose } from '/rnd-hybrid/cutout/rig.js';
import { paperGrain, vignette } from '/rnd-hybrid/v2/paper3d.js';
import { lg } from '/rnd-hybrid/v2/illus2d.js';
import { Lights, buildWorld, Actor, card, printProp } from '/rnd-hybrid/v2/clip/seg/world.js';

const SEG = '/rnd-hybrid/v2/clip/seg/';
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const lin = (t, a, b) => clamp((t - a) / (b - a));
const ease = (t, a, b) => { const x = lin(t, a, b); return x * x * (3 - 2 * x); };
const backOut = (t, a, d = 0.35) => { if (t < a) return 0; const x = clamp((t - a) / d), c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const V = (...a) => new THREE.Vector3(...a);

export async function boot(res) {
  for (const wt of [400, 600, 700, 800]) await document.fonts.load(`${wt} 48px Inter`);
  const TL = await (await fetch(SEG + 'timeline.json')).json(), A = TL.a, SH = Object.fromEntries(TL.shots.map((s) => [s.id, s]));
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
  const scene = new THREE.Scene(), L = Lights(scene), Wd = buildWorld(scene);
  const cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 400);
  const HX = Wd.H0.x, TX = Wd.T0.x;

  // ---- diễn viên (một tấm giấy cho mỗi nét mặt/tư thế)
  const worriedPose = { ...blendPose(POSES.stand, POSES.slump, 0.3), head: 9, uaR: 22, faR: 100, uaL: 14, faL: -20 };
  const walt = Actor(scene, 'walt', { happy: { pose: POSES.stand, expr: 'happy' }, wave: { pose: POSES.wave, expr: 'happy' }, neutral: { pose: POSES.stand, expr: 'neutral' },
    shocked: { pose: POSES.shock, expr: 'shocked' }, worried: { pose: worriedPose, expr: 'worried' }, sad: { pose: POSES.slump, expr: 'sad' },
    hold: { pose: POSES.hold, expr: 'happy' }, relieved: { pose: POSES.cheer, expr: 'relieved' }, calm: { pose: POSES.stand, expr: 'relieved' } }, { s: 1.5, pxPerM: 600, thick: 0.02 });
  const ruth = Actor(scene, 'ruth', { happy: { pose: POSES.stand, expr: 'happy' }, worried: { pose: POSES.stand, expr: 'worried' }, relieved: { pose: POSES.stand, expr: 'relieved' } }, { s: 1.5, pxPerM: 640, thick: 0.02 });
  const sam = Actor(scene, 'sam', { happy: { pose: POSES.wave, expr: 'happy' } }, { s: 1.5, pxPerM: 600, thick: 0.02 });
  const passbook = printProp('note', { s: 0.55, label: ' ' }, { wPx: 220, hPx: 240, pxPerM: 600, thick: 0.01 }); passbook.position.set(0.02, 0.86, 0.035); passbook.rotation.z = -0.12;
  walt.g.add(passbook);

  // ---- thẻ giấy (số + nhãn): mỗi số có nguồn (dòng nguồn 2D khi thẻ hiện)
  const C = {
    half: card(['≈ HALF', 'THE PRICE'], { px: 120, sub: 'most a bank would lend', accent: '#F2B441', pxPerM: 380 }),
    years: card('3–5 YEARS', { w: 860, h: 260, px: 130, accent: '#F2B441', pxPerM: 520 }),
    due: card(['THE WHOLE', 'LOAN'], { w: 700, h: 760, px: 130, sub: 'DUE NOW', subPx: 96, accent: '#8E2B2B', fg: '#2A1A1A', pxPerM: 260 }),
    fha: card('FHA · 1934', { w: 900, h: 320, px: 140, sub: 'Federal Housing Administration', subPx: 54, accent: '#4C8DFF', pxPerM: 480 }),
    insured: card('INSURED', { w: 560, h: 200, px: 100, fg: '#1F3F7A', accent: '#4C8DFF', pxPerM: 760, rot: -6 }),
    eighty: card(['UP TO 80%', 'OF VALUE'], { w: 900, h: 400, px: 120, accent: '#4C8DFF', pxPerM: 560 }),
    twenty: card('UP TO 20 YEARS', { w: 1100, h: 240, px: 120, accent: '#4C8DFF', pxPerM: 560 }),
    thirty: card(['1954:', 'UP TO 30 YEARS'], { w: 1150, h: 400, px: 120, accent: '#3FBF7F', pxPerM: 560 }),
  };
  for (const c of Object.values(C)) scene.add(c);
  const cal = [1, 2, 3, 4, 5].map((k) => { const c = card(String(k), { w: 300, h: 300, px: 170, sub: 'yr', subPx: 54, accent: k >= 3 ? '#F2B441' : null, pxPerM: 520 }); scene.add(c); return c; });
  // 10 ô giá trị nhà (80 % = 8 ô xanh) và 20 bậc dư nợ trả dần (mỗi năm một bậc, cao = phần còn nợ)
  const slab = (w, h, color) => { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.04), new THREE.MeshStandardMaterial({ color, roughness: 0.95 })); m.castShadow = m.receiveShadow = true; scene.add(m); return m; };
  const val = Array.from({ length: 10 }, (_, i) => { const m = slab(0.42, 0.42, '#EDE4CF'); m.position.set(HX + 2.2 + i * 0.47, 1.25, -7.0); return m; });
  const steps = Array.from({ length: 30 }, (_, i) => { const h = Math.max(0.02, 1.3 * (1 - i / 20)), m = slab(0.3, 1, i < 20 ? '#EDE4CF' : '#BFE8D2');
    m.userData.h = i < 20 ? h : 0.02; return m; });
  const STX = HX + 6.0, STZ = -7.4;   // bậc trả dần đặt cạnh nhà
  steps.forEach((m, i) => { m.position.set(STX + i * 0.36, 0.16, STZ); });
  const ruler = Array.from({ length: 30 }, (_, i) => { const c = card(String(i + 1), { w: 220, h: 220, px: 110, accent: i >= 20 ? '#3FBF7F' : (i % 5 === 4 ? '#4C8DFF' : null), pxPerM: 700, rimWidth: 2 });
    c.position.set(TX - 7.6 + i * 0.52, 0.16, -6.4); scene.add(c); return c; });
  // đèn bù đi theo máy quay (sửa A: mặt giấy ở trung cảnh đủ sáng trong hồi tối/ngược sáng)
  const camFill = new THREE.PointLight('#FFF1DE', 0, 30, 1.2); scene.add(camFill);
  const FILL = { calm1929: 5, crisis1931: 7, relief1934: 5, today: 3 };

  // ---- ảnh tư liệu C (đứng riêng toàn khung): phủ tông kênh một lần
  const im = new Image(); im.src = '/rnd-hybrid/work/external/bank1931_crop.jpg'; await im.decode();
  const tone = new OffscreenCanvas(W, H), tg = tone.getContext('2d'); tg.filter = 'contrast(1.12)'; tg.drawImage(im, 0, 0, W, H); tg.filter = 'none';
  { const d = tg.getImageData(0, 0, W, H), lc = new OffscreenCanvas(256, 1), lx = lc.getContext('2d');
    lx.fillStyle = lg(lx, 0, 0, 256, 0, [[0, '#0E1116'], [0.45, '#4A5160'], [0.8, '#B9B3A4'], [1, '#EDE4CF']]); lx.fillRect(0, 0, 256, 1); const Lu = lx.getImageData(0, 0, 256, 1).data;
    for (let i = 0; i < d.data.length; i += 4) { const v = (d.data[i] * 0.299 + d.data[i + 1] * 0.587 + d.data[i + 2] * 0.114) | 0; d.data[i] = Lu[v * 4]; d.data[i + 1] = Lu[v * 4 + 1]; d.data[i + 2] = Lu[v * 4 + 2]; }
    tg.putImageData(d, 0, 0); }

  // ---- máy quay theo cảnh: [từ, đến] {pos, tgt, fov}
  const P = (pos, tgt, fov) => ({ pos, tgt, fov });
  const A_FRAME = P([13.2, 1.3, -0.6], [1.6, 3.6, -13.2], 36);
  const CAM = {
    A1: [P([HX + 4, 2.4, 3], [HX, 2.4, -10], 40), P([HX + 3, 1.9, 0.5], [HX - 0.5, 2.1, -10], 36)],
    A2: [P([HX + 0.6, 1.5, -3.2], [HX - 2.1, 1.3, -8.2], 34), P([HX + 0.4, 1.5, -3.6], [HX - 2.1, 1.3, -8.2], 32)],
    B: [P([10, 1.6, -1.5], [2, 2.6, -11], 40), P([9, 1.6, -2.5], [2, 2.5, -11], 37)],
    C: [P([HX + 5.6, 1.7, -0.6], [HX + 0.2, 1.4, -7.4], 40), P([HX + 5.0, 1.6, -1.2], [HX + 0.2, 1.4, -7.4], 38)],
    D: [P([HX + 2.2, 0.8, -2.0], [HX - 1.2, 2.3, -8.2], 44), P([HX + 2.0, 0.85, -2.6], [HX - 1.2, 2.4, -8.2], 42)],
    E: [P([7, 1.5, -2.5], [0.6, 2.5, -14], 40), P([6, 1.5, -3.4], [0.4, 2.5, -14], 37)],
    F: [P([HX + 3.5, 1.5, -1.5], [HX - 0.5, 1.8, -10], 42), P([HX + 3.0, 1.4, -2.2], [HX - 0.5, 1.7, -10], 40)],
    G: [P([16, 2.6, 2], [1.6, 3.6, -13.2], 40), P([14.2, 1.7, 0.3], [1.6, 3.6, -13.2], 37)],
    H: [P([3, 1.9, -6.0], [0, 2.7, -14.3], 34), P([1.6, 2.2, -8.8], [0, 2.7, -14.3], 30)],
    J: [A_FRAME, P([12.6, 1.3, -1.2], [1.6, 3.5, -13.2], 35)],
    K1: [P([13, 1.4, -1], [2, 3.4, -13], 36), P([16, 4.0, 4], [2, 3.6, -13], 38)],
    K2: [P([HX + 3, 1.8, -0.5], [HX - 0.5, 2.3, -9], 40), P([HX + 2.6, 1.8, -1.2], [HX - 0.5, 2.3, -9], 38)],
    L1: [P([HX + 0.6, 1.5, -4.2], [HX - 2.0, 1.4, -8.2], 34), P([HX + 0.4, 1.5, -4.6], [HX - 2.0, 1.4, -8.2], 32)],
    L2: [P([HX + 6.4, 1.9, -1.8], [HX + 3.2, 1.5, -7.6], 40), P([HX + 6.0, 1.8, -2.4], [HX + 3.2, 1.5, -7.6], 38)],
    M: [P([STX + 1.0, 2.0, -0.8], [STX + 2.8, 1.1, -7.4], 44), P([STX + 4.4, 1.9, -1.2], [STX + 4.2, 1.0, -7.4], 42)],
    N: [P([STX + 6.0, 1.3, -3.4], [STX + 6.4, 1.2, -8], 38), P([STX + 6.2, 1.3, -3.8], [STX + 6.4, 1.2, -8], 36)],
    O: [P([TX + 0.8, 1.6, -1.6], [TX + 0.2, 1.5, -6.6], 44), P([TX + 0.6, 1.6, -2.1], [TX + 0.2, 1.5, -6.6], 42)],
    P: [P([TX - 0.4, 1.4, -5.2], [TX - 1.6, 1.3, -8.2], 34), P([TX + 1.8, 1.8, -1.6], [TX - 1.0, 1.8, -9.5], 38)],
  };
  CAM.I = [CAM.H[1], CAM.H[1]];
  // ---- hồi đèn theo cảnh: [hồi đầu, hồi cuối, mục tiêu đèn]
  const ACTOF = { A1: ['calm1929'], A2: ['calm1929'], B: ['calm1929'], C: ['calm1929'], D: ['calm1929'], E: ['calm1929', 'crisis1931'], F: ['crisis1931'],
    G: ['crisis1931'], H: ['crisis1931'], I: ['crisis1931'], J: ['crisis1931'], K1: ['crisis1931', 'relief1934'], K2: ['relief1934'], L1: ['relief1934'], L2: ['relief1934'],
    M: ['relief1934'], N: ['relief1934'], O: ['relief1934', 'today'], P: ['today'] };
  const shotAt = (t) => TL.shots.find((s) => t >= s.t0 && t < s.t1) || TL.shots[TL.shots.length - 1];

  const face = (obj, twist = 0.3) => { const p = obj.getWorldPosition(new THREE.Vector3()); obj.rotation.y = Math.atan2(cam.position.x - p.x, cam.position.z - p.z) + twist; };
  const place = (o, x, y, z, s = 1, tw = 0.25) => { o.visible = s > 0.001; o.position.set(x, y, z); o.scale.setScalar(Math.max(0.001, s)); face(o, tw); };
  const hideAll = () => { for (const c of Object.values(C)) c.visible = false; cal.forEach((c) => (c.visible = false)); val.forEach((m) => (m.visible = false));
    steps.forEach((m) => (m.visible = false)); ruler.forEach((c) => (c.visible = false)); walt.show(null); ruth.show(null); sam.show(null);
    Wd.queue.forEach((q) => (q.visible = false)); Wd.closedSign.visible = false; Wd.housePivot.rotation.x = 0; };

  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  function render3d(t, sh, k) {
    const id = sh.id, [c0, c1] = CAM[id], act = ACTOF[id];
    const p = { pos: c0.pos.map((v, i) => v + (c1.pos[i] - v) * k), tgt: c0.tgt.map((v, i) => v + (c1.tgt[i] - v) * k), fov: c0.fov + (c1.fov - c0.fov) * k };
    cam.position.set(...p.pos); cam.fov = p.fov; cam.lookAt(...p.tgt); cam.updateProjectionMatrix(); cam.updateMatrixWorld();
    const ak = id === 'E' ? ease(t, A.noloan - 0.2, A.noloan + 0.6) : id === 'K1' ? ease(t, sh.t0 + 0.2, sh.t1 - 0.2) : id === 'O' ? ease(t, sh.t0, sh.t1) : 0;
    L.set(act[0], act[1] || act[0], ak, [p.tgt[0], 0, p.tgt[2]]);
    camFill.position.set(p.pos[0] + 0.5, p.pos[1] + 1.2, p.pos[2] + 0.5); camFill.intensity = FILL[act[0]] + (FILL[act[1] || act[0]] - FILL[act[0]]) * ak;
    hideAll(); stage(id, t, sh);
    renderer.render(scene, cam);
  }
  // doors: 0 = mở (xoay vào trong 80°), 1 = đóng
  const doors = (x) => Wd.doors.forEach(({ piv, sgn }) => { piv.rotation.y = sgn * (1 - x) * 1.4; });
  function stage(id, t, sh) {
    const W0 = [HX - 1.9, 0.16, -8.0], R0 = [HX - 3.2, 0.16, -8.3];
    doors(1);
    switch (id) {
      case 'A1': case 'A2':
        walt.show(t > A.home && id === 'A2' ? 'wave' : 'happy'); place(walt.g, ...W0); ruth.show('happy'); place(ruth.g, ...R0); break;
      case 'B': doors(0); walt.show(t > A.half + 0.3 ? 'neutral' : 'happy'); place(walt.g, 6.6, 0.16, -7.4, 1, 0.35);
        place(C.half, 3.6, 2.2, -8.0, backOut(t, A.half), 0.15); break;
      case 'C': walt.show('neutral'); place(walt.g, ...W0);
        cal.forEach((c, i) => place(c, HX - 0.2 + i * 0.75, 0.75 + (i % 2) * 0.06, -6.8, backOut(t, i < 3 ? A.three + i * 0.12 : A.five + (i - 3) * 0.12), 0.15));
        place(C.years, HX + 1.4, 1.75, -7.6, backOut(t, A.five + 0.3), 0.15); break;
      case 'D': { walt.show(t > A.whole + 0.25 ? 'shocked' : 'neutral'); place(walt.g, ...W0);
        const f = ease(t, A.whole - 0.1, A.once + 0.1); place(C.due, HX + 1.3, 0.16 + (1 - f) * 7, -7.7, 1, 0.1 - (1 - f) * 0.8); C.due.rotation.z = (1 - f) * 0.5; break; }
      case 'E': doors(ease(t, A.noloan, A.noloan + 0.8)); walt.show('worried'); place(walt.g, 2.2, 0.16, -8.6, 1, 0.5); break;
      case 'F': walt.show('sad'); place(walt.g, HX + 1.6, 0.16, -6.6, 1, 0.3); Wd.housePivot.rotation.x = -1.45 * ease(t, A.lose - 0.1, A.lose + 0.9); break;
      case 'G': break;
      case 'H': Wd.closedSign.visible = true; Wd.closedSign.scale.setScalar(Math.max(0.001, backOut(t, A.closed, 0.3))); break;
      case 'I': case 'J': Wd.closedSign.visible = true; Wd.closedSign.scale.setScalar(1); Wd.queue.forEach((q) => { q.visible = true; face(q, 0.25); });
        walt.show('worried'); place(walt.g, 10.9, 0.16, -4.6, 1, 0.42); break;
      case 'K1': Wd.closedSign.visible = true; Wd.closedSign.scale.setScalar(1); break;
      case 'K2': walt.show('calm'); place(walt.g, ...W0); ruth.show('relieved'); place(ruth.g, ...R0); place(C.fha, HX + 1.6, 2.2, -6.6, backOut(t, A.fha), 0.15); break;
      case 'L1': walt.show('hold'); place(walt.g, ...W0); ruth.show('happy'); place(ruth.g, ...R0); place(C.insured, HX - 1.0, 1.9, -7.0, backOut(t, A.insured + 0.1), 0.1); break;
      case 'L2': { walt.show('happy'); place(walt.g, ...W0);
        val.forEach((m, i) => { m.visible = true; m.material.color.set(t > A.eighty + i * 0.05 && i < 8 ? '#4C8DFF' : '#EDE4CF'); face(m, 0); });
        place(C.eighty, HX + 4.3, 2.45, -7.2, backOut(t, A.eighty + 0.2), 0.12); break; }
      case 'M': case 'N': { const n = id === 'N' ? 20 : Math.floor(clamp(lin(t, A.paid, A.twenty + 0.2)) * 20);
        steps.forEach((m, i) => { if (i >= 20) return; const s = i < n ? 1 : i === n ? lin(t, A.paid, A.twenty + 0.2) * 20 - n : 0;
          m.visible = s > 0.01; m.scale.y = m.userData.h * Math.max(0.01, s); m.position.y = 0.16 + m.userData.h * s / 2; });
        if (id === 'M') place(C.twenty, STX + 3.6, 2.0, -7.8, backOut(t, A.twenty), 0.1);
        if (id === 'N') { walt.show(t > A.bill ? 'relieved' : 'calm'); place(walt.g, STX + 8.0, 0.16, -7.0, 1, 0.3);
          const f = ease(t, A.bill - 0.1, A.bill + 0.7); place(C.due, STX + 6.2, 0.16, -8.4, 1, 0.1); C.due.rotation.x = -1.5 * f; C.due.visible = f < 0.99; }
        break; }
      case 'O': ruler.forEach((c, i) => place(c, TX - 2.25 + (i % 10) * 0.5, 0.16 + 1.0 - Math.floor(i / 10) * 0.5, -6.6, i < 20 ? 1 : backOut(t, A.thirty + (i - 20) * 0.06), 0.1));
        place(C.thirty, TX + 0.0, 2.15, -7.0, backOut(t, A.y1954), 0.08); break;
      case 'P': sam.show('happy'); place(sam.g, TX - 1.6, 0.16, -8.2, 1, 0.3); break;
    }
  }
  // ---- lớp phủ 2D: hồi năm (trái trên), ILLUSTRATIVE (phải trên), dòng nguồn (phải dưới)
  const YEAR = { A1: '1930', A2: '1930', B: '1930', C: '1930', D: '1930', E: '1930', F: '1930', G: 'December 1930', H: 'December 1930', I: '1931', J: '1931',
    K1: '1934', K2: '1934', L1: '1934', L2: '1934', M: '1934', N: '1934', O: '1954', P: 'Today' };
  const SRC = { B: 'Source: HUD, FHA history', C: 'Source: HUD, FHA history', D: 'Source: HUD, FHA history', G: 'Source: Federal Reserve History',
    H: 'Source: Federal Reserve History', I: 'Photo: Library of Congress (NYWT&S), 1931', K2: 'Source: HUD, FHA history', L2: 'Source: National Housing Act of 1934, §203',
    M: 'Source: National Housing Act of 1934, §203', O: 'Source: Federal Reserve Bank of St. Louis Review, Nov. 1955' };
  function overlay(id, t, archival) {
    const s = W / 1920; ctx.save(); ctx.scale(s, s);
    const pill = (txt, x, y, px, fg, bg, right) => { ctx.font = `600 ${px}px Inter`; const pw = ctx.measureText(txt).width + px * 0.9, ph = px * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px * 0.45, y + ph / 2 + px * 0.04); };
    pill(YEAR[id], 96, 54, 48, '#F2F4F7', 'rgba(14,17,22,0.72)');
    if (!archival) pill('ILLUSTRATIVE', 1824, 54, 40, '#0E1116', 'rgba(242,244,247,0.88)', true);
    const src = SRC[id]; if (src) { ctx.font = '400 40px Inter'; ctx.textAlign = 'right'; ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = 'rgba(14,17,22,0.75)'; ctx.fillText(src, 1826, 1018); ctx.fillStyle = 'rgba(242,244,247,0.94)'; ctx.fillText(src, 1824, 1016); }
    ctx.restore();
  }
  function photo(t, a) {   // Ken Burns chậm trong khung ảnh tư liệu
    const k = lin(t, TL.archival.in, TL.archival.out), z = 1.02 + 0.07 * k, w = W * z, h = H * z;
    ctx.save(); ctx.globalAlpha = a; ctx.drawImage(tone, (W - w) / 2 - W * 0.02 * k, (H - h) / 2 - H * 0.015 * k, w, h); ctx.restore();
  }
  function frame(t) {
    const sh = shotAt(t), id = sh.id, k = ease(t, sh.t0, sh.t1);
    const ai = TL.archival.in, ao = TL.archival.out, fin = 0.7, fout = 0.8;
    const arch = t >= ai && t < ao ? Math.min(ease(t, ai, ai + fin), 1 - ease(t, ao - fout, ao)) : 0;
    if (id === 'I' && arch > 0.999) { ctx.fillStyle = '#0E1116'; ctx.fillRect(0, 0, W, H); }
    else { render3d(t, id === 'I' ? { ...SH.H, id: 'H' } : sh, id === 'I' ? 1 : k); ctx.drawImage(renderer.domElement, 0, 0); paperGrain(ctx, W, H, 0.08); vignette(ctx, W, H, 0.4); }
    if (arch > 0) { photo(t, arch); if (arch > 0.5) { paperGrain(ctx, W, H, 0.2 * arch); vignette(ctx, W, H, 0.5 * arch); } }
    overlay(arch > 0.5 ? 'I' : id === 'I' ? 'H' : id, t, arch > 0.5);
    return { violations: [] };
  }
  return { canvas: out, frame };
}
