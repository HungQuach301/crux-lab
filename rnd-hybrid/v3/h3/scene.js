// R&D vòng 3 · H3 (đối chứng): đạo cụ giấy gấp 3D tự dựng + nhân vật giấy 5 lớp tách z (rig.js), ánh sáng thật + bóng, vân giấy.
// Cùng bố cục/máy quay với H4 (lib/sets.js). t: S1 [0,1), S2 [1,2), S3 [2,3), ORBIT [10,16).
import * as THREE from 'three';
import { POSES, blendPose } from '/rnd-hybrid/cutout/rig.js';
import { paperGrain, vignette } from '/rnd-hybrid/v2/paper3d.js';
import { variants } from '/rnd-hybrid/v2/clip/seg/world.js';
import { foldBox, roll, prism, printedPlane, paperMat, layered } from '/rnd-hybrid/v3/lib/paperfold.js';
import { X2, X3, WALT, CAMS, orbitCam, which, CROWD, payment } from '/rnd-hybrid/v3/lib/sets.js';

const txt = (text, { px = 120, fg = '#15171C', accent = null } = {}) => (g, W, H) => { if (accent) { g.fillStyle = accent; g.fillRect(0, 0, W, 22); }
  g.fillStyle = fg; g.font = `800 ${px}px Inter`; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(text, W / 2, H / 2 + 8); };
function windows(g, W, H) { g.fillStyle = 'rgba(30,34,42,0.85)'; const cols = 4, rows = Math.floor(H / 70); for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) g.fillRect(18 + c * (W - 30) / cols, 20 + r * 70, (W - 30) / cols - 18, 40); }

export async function boot(res) {
  for (const wt of [400, 600, 700, 800]) await document.fonts.load(`${wt} 48px Inter`);
  variants();
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping;
  const scene = new THREE.Scene(); scene.background = new THREE.Color('#3B4556'); scene.fog = new THREE.Fog('#3B4556', 28, 90);
  const hemi = new THREE.HemisphereLight('#C9D6EA', '#3A3026', 1.0), key = new THREE.DirectionalLight('#FFF1DC', 2.4);
  key.castShadow = true; key.shadow.mapSize.set(2048, 2048); Object.assign(key.shadow.camera, { left: -12, right: 12, top: 12, bottom: -12, near: 0.5, far: 60 }); key.shadow.bias = -0.0005; key.shadow.normalBias = 0.02;
  const fill = new THREE.PointLight('#FFF1DE', 0, 30, 1.2); scene.add(hemi, key, key.target, fill);   // đèn bù theo máy quay (bài học v2)
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(400, 200), paperMat('#5C5852', { rep: [60, 30] })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const at = (o, x, y, z) => { o.position.set(x, y, z); scene.add(o); return o; };

  // ---- S1: ngân hàng giấy gấp + dãy nhà gấp + đám đông giấy 5 lớp
  at(foldBox(40, 0.16, 12, '#77716A', { sag: 0 }), 0, 0.08, -9);
  const B = new THREE.Group(); B.position.set(0, 0.16, -12.6); scene.add(B);
  for (let i = 0; i < 4; i++) { const st = foldBox(13.6 - i * 0.5, 0.22, 2.2 - i * 0.45, '#B9B2A3', { sag: 0.02 }); st.position.set(0, 0.11 + i * 0.22, -i * 0.42); B.add(st); }
  const wallB = foldBox(12, 6.9, 6, '#D3CCBC'); wallB.position.set(0, 0.88 + 3.45, -4.8); B.add(wallB);
  for (let i = 0; i < 6; i++) { const c = roll(0.36, 5.9, '#E8E1D2'); c.position.set(-5.1 + i * 2.04, 0.88 + 0.25 + 2.95, -1.2); B.add(c); }
  const ent = printedPlane(12.6, 0.9, txt('B A N K', { px: 150, fg: '#2A303B' }), { px: 120 }); ent.position.set(0, 0.88 + 6.85, -0.6); B.add(ent);
  const entB = foldBox(12.6, 0.9, 1.6, '#C6BFAF'); entB.position.set(0, 0.88 + 6.85, -1.42); B.add(entB);
  const ped = prism(12.8, 1.7, 1.5, '#D9D2C2'); ped.position.set(0, 0.88 + 7.3, -1.4); B.add(ped);
  const door = foldBox(2.5, 3.4, 0.12, '#6B5038', { sag: 0.03 }); door.position.set(0, 0.88 + 1.7, -1.75); B.add(door);
  const closed = printedPlane(1.9, 0.7, txt('CLOSED', { px: 150, fg: '#8E2B2B', accent: '#8E2B2B' })); closed.position.set(0, 0.88 + 1.55, -1.62); B.add(closed);
  for (let i = 0; i < 8; i++) { const left = i < 4, h = 9 + (i % 3) * 2.5, w = 4.6, col = ['#7D7066', '#8A7C6C', '#6E6258', '#9A8C78'][i % 4];
    const face = paperMat(col, { draw: windows, key: col + 'win' + h, w: 256, h: Math.round(256 * h / w) });
    const b = foldBox(w, h, 5, col, { faces: { 4: face } }); at(b, left ? -9.5 - (i % 4) * 5.2 : 9.5 + (i % 4) * 5.2, 0.16 + h / 2, -15.5); }
  const post = at(roll(0.07, 4.4, '#2A2F38'), -6.5, 0.16 + 2.2, -5.2); const lan = foldBox(0.4, 0.5, 0.4, '#F6D58E', { sag: 0 }); lan.material.forEach?.((m) => { m.emissive = new THREE.Color('#F2B441'); m.emissiveIntensity = 1.2; }); at(lan, -6.5, 4.8, -5.2);
  const lampL = new THREE.PointLight('#FFD08A', 18, 12, 1.4); at(lampL, -6.5, 4.6, -5.2);
  const ID = { 'male-a': 'walt', 'male-b': 'q1', 'male-c': 'q3', 'male-d': 'q4', 'male-e': 'q1', 'male-f': 'q3', 'female-a': 'ruth', 'female-b': 'q2', 'female-c': 'q5', 'female-d': 'q2', 'female-e': 'ruth', 'female-f': 'q5' };
  const face = (o, x, z, tw = 0) => { o.rotation.y = Math.atan2(CAMS.S1.pos[0] - x, CAMS.S1.pos[2] - z) + tw; };
  for (const [x, z, , file, , , clip, expr] of CROWD) { const id = ID[file], pose = clip === 'emote-no' ? POSES.shock : clip === 'holding-right' ? POSES.phone : POSES.stand;
    const f = layered({ id, pose, expr }, { s: 0.95, pxPerM: 400, dots: 0 });   // đám đông: bỏ bán sắc (khởi động trang < 180 s) at(f, x, 0.16, z); face(f, x, z, 0.15); }
  const wPose = { ...blendPose(POSES.stand, POSES.slump, 0.3), head: 9, uaR: 22, faR: 100, uaL: 14, faL: -20 };
  const walt = layered({ id: 'walt', pose: wPose, expr: 'worried' }, { s: 1.0, pxPerM: 400, wPx: 720, hPx: 980 }); at(walt, ...WALT); face(walt, WALT[0], WALT[2], 0.25);

  // ---- S2: phòng ký hợp đồng (giấy gấp)
  at(foldBox(9, 0.1, 7, '#8A6A4C', { sag: 0 }), X2, 0.05, -1.5);
  at(foldBox(9, 3.4, 0.2, '#C9B99A', { sag: 0.004 }), X2, 1.7, -3.6);
  const win = printedPlane(1.6, 1.3, (g, w, h) => { g.fillStyle = '#DCE8F4'; g.fillRect(14, 14, w - 28, h - 28); g.fillStyle = '#8A6A4C'; g.fillRect(w / 2 - 5, 0, 10, h); g.fillRect(0, h / 2 - 5, w, 10); });
  win.material.emissive = new THREE.Color('#DCE8F4'); win.material.emissiveIntensity = 0.25; at(win, X2 - 2.2, 1.9, -3.48);
  at(printedPlane(1.5, 0.42, txt('FHA · 1934', { px: 90, accent: '#4C8DFF' })), X2 + 1.2, 2.1, -3.48);
  const desk = new THREE.Group(); { const top = foldBox(1.5, 0.06, 0.8, '#C49A6C', { sag: 0.01 }); top.position.set(0, 0.72, 0); desk.add(top); }
  for (const [dx, dz] of [[-0.68, -0.34], [0.68, -0.34], [-0.68, 0.34], [0.68, 0.34]]) { const l = foldBox(0.08, 0.7, 0.08, '#A57E55', { sag: 0 }); l.position.set(dx, 0.35, dz); desk.add(l); }
  const front = foldBox(1.44, 0.5, 0.04, '#B98C5E', { sag: 0.02 }); front.position.set(0, 0.42, 0.38); desk.add(front);
  at(desk, X2, 0.1, -0.9);
  const doc = printedPlane(0.42, 0.56, (g, w, h) => { g.fillStyle = '#15171C'; g.font = '800 46px Inter'; g.textAlign = 'center'; g.fillText('MORTGAGE', w / 2, 78); g.font = '700 30px Inter'; g.fillStyle = '#2F4F8A'; g.fillText('INSURED · FHA', w / 2, 126);
    g.fillStyle = '#8A8070'; for (let i = 0; i < 9; i++) g.fillRect(50, 170 + i * 34, i % 3 === 2 ? 220 : 320, 8); }, { px: 1000 });
  doc.rotation.x = -Math.PI / 2; doc.rotation.z = 0.15; at(doc, X2 + 0.1, 0.1 + 0.765, -1.0);
  const hat = new THREE.Group(); { const b = new THREE.Mesh(new THREE.CylinderGeometry(0.26, 0.27, 0.02, 20), paperMat('#2C3038')); const c = roll(0.15, 0.18, '#2C3038'); c.position.y = 0.1; const top = new THREE.Mesh(new THREE.CircleGeometry(0.15, 18), paperMat('#2C3038')); top.rotation.x = -Math.PI / 2; top.position.y = 0.19; hat.add(b, c, top); hat.traverse((o) => { if (o.isMesh) o.castShadow = true; }); }
  at(hat, X2 - 0.5, 0.1 + 0.77, -0.75);
  const signPose = { ...POSES.hold, head: 8 };
  const signer = layered({ id: 'walt', pose: signPose, expr: 'happy' }, { s: 1.0, pxPerM: 400, wPx: 720, hPx: 980 }); at(signer, X2, 0.1 - 0.35, -1.55);
  signer.rotation.y = Math.atan2(CAMS.S2.pos[0] - X2, CAMS.S2.pos[2] + 1.55);
  const clerk = layered({ id: 'q2', pose: POSES.point, expr: 'happy', flip: true }, { s: 1.0, pxPerM: 400 }); at(clerk, X2 + 1.25, 0.1, -2.2); clerk.rotation.y = -0.2;

  // ---- S3: lưới trả dần (khối giấy gấp nhỏ), nhãn in
  at(foldBox(22, 0.1, 10, '#DCD3BF', { sag: 0 }), X3 + 2, 0.05, -1);
  const p20 = payment(20), p30 = payment(30), h20 = 0.075, h30 = 0.075 * p30 / p20;
  const tileGeo = (h) => foldBox(0.26, h, 0.26, '#fff', { sag: 0.05 }).geometry;
  const mk = (n, z, color, h) => { const geo = tileGeo(h), mat = paperMat(color, { draw: (g, W, Hh) => { g.strokeStyle = 'rgba(20,20,30,0.5)'; g.lineWidth = 8; g.strokeRect(3, 3, W - 6, Hh - 6); }, key: color + 'tile' });
    for (let y = 0; y < n; y++) for (let m = 0; m < 12; m++) { const t = new THREE.Mesh(geo, mat); t.castShadow = t.receiveShadow = true; at(t, X3 - 4.2 + y * 0.34, 0.1 + h / 2 + m * (h + 0.012), z); } };
  mk(20, -0.4, '#4C8DFF', h20); mk(30, -2.0, '#3FBF7F', h30);
  at(printedPlane(4.4, 0.5, txt('1934: UP TO 20 YEARS', { px: 96, accent: '#4C8DFF' })), X3 - 1.6, 1.55, -0.4);
  at(printedPlane(4.4, 0.5, txt('1954: UP TO 30 YEARS', { px: 96, accent: '#3FBF7F' })), X3 + 2.4, 1.75, -2.0);
  const guide = layered({ id: 'walt', pose: POSES.point, expr: 'happy', flip: true }, { s: 1.0, pxPerM: 400, wPx: 720, hPx: 980 }); at(guide, X3 + 3.4, 0.1, 1.4); guide.rotation.y = Math.atan2(CAMS.S3.pos[0] - X3 - 3.4, CAMS.S3.pos[2] - 1.4);
  for (const [x, z] of [[X3 + 8.5, -4], [X3 - 6, -4.5]]) { const tr = new THREE.Group(); const tk = roll(0.12, 1.6, '#6B5038'); tk.position.y = 0.8; tr.add(tk);
    const cn = new THREE.Mesh(new THREE.ConeGeometry(0.9, 2.2, 7), paperMat('#4C7A58')); cn.position.y = 2.4; cn.castShadow = true; tr.add(cn); at(tr, x, 0.1, z); }

  const cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 400);
  const LIGHT = { S1: ['#3B4556', '#C9D6EA', '#FFE2B8', 1.8, [-8, 12, 6]], S2: ['#B9A27E', '#FFF1DC', '#FFE8C2', 2.0, [-4, 6, 6]], S3: ['#CFE0F0', '#F4F8FF', '#FFF6E6', 2.4, [-6, 12, 8]] };
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  const YEAR = { S1: '1930', S2: '1934', S3: '1934 → 1954', ORBIT: '1930' };
  function frame(t) {
    const w = which(t), sc = w === 'ORBIT' ? 'S1' : w, P = w === 'ORBIT' ? orbitCam(t) : CAMS[w], L = LIGHT[sc];
    cam.position.set(...P.pos); cam.fov = P.fov; cam.lookAt(...P.tgt); cam.updateProjectionMatrix();
    fill.position.set(P.pos[0] + 0.5, P.pos[1] + 1.2, P.pos[2] + 0.5); fill.intensity = sc === 'S1' ? 9 : 3;
    scene.background.set(L[0]); scene.fog.color.set(L[0]); hemi.color.set(L[1]); key.color.set(L[2]); key.intensity = L[3];
    key.position.set(P.tgt[0] + L[4][0], L[4][1], P.tgt[2] + L[4][2]); key.target.position.set(P.tgt[0], 0, P.tgt[2]); key.target.updateMatrixWorld();
    if (w === 'ORBIT') walt.rotation.y = Math.atan2(cam.position.x - WALT[0], cam.position.z - WALT[2]) + 0.25;   // giấy luôn hướng về máy (+ xoay nhẹ để thấy lớp)
    renderer.render(scene, cam);
    ctx.drawImage(renderer.domElement, 0, 0); paperGrain(ctx, W, H, 0.12); vignette(ctx, W, H, 0.4);
    const s = W / 1920; ctx.save(); ctx.scale(s, s);
    const pill = (txt, x, y, px, fg, bg, right) => { ctx.font = `600 ${px}px Inter`; const pw = ctx.measureText(txt).width + px * 0.9, ph = px * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px * 0.45, y + ph / 2 + px * 0.04); };
    pill(YEAR[w], 96, 54, 48, '#F2F4F7', 'rgba(14,17,22,0.72)'); pill('ILLUSTRATIVE', 1824, 54, 40, '#0E1116', 'rgba(242,244,247,0.88)', true);
    if (w === 'S3') { ctx.font = '400 40px Inter'; ctx.textAlign = 'right'; ctx.fillStyle = 'rgba(14,17,22,0.8)'; ctx.fillText('Source: National Housing Act 1934 §203; St. Louis Fed Review, Nov. 1955', 1824, 1016); }
    ctx.restore();
    return { violations: [] };
  }
  return { canvas: out, frame };
}
