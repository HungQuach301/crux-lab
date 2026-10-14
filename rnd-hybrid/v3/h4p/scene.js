// R&D vòng 3 · H4′ (chủ dự án chọn H4, thay người): người lớn Quaternius UBC [Standard] + UAL [Standard] (CC0), mặt rig.js chiếu lên đầu;
// đồ đạc Kenney CC0, ngân hàng v2, hậu kỳ toàn khung H4 giữ nguyên.
// Đoạn cắm vào render_shots.js của nhà máy (không sửa nhà máy). t: S1 [0,1), S2 [1,2), S3 [2,3), ORBIT [10,16).
import * as THREE from 'three';
import { Bank, Lamp } from '/rnd-hybrid/v2/paper3d.js';
import { prop, glb, toonMat, fedora } from '/rnd-hybrid/v3/lib/kenney.js';
import { adult } from '/rnd-hybrid/v3/lib/quat.js';
import { Post } from '/rnd-hybrid/v3/lib/post.js';
import { X2, X3, WALT, CAMS, orbitCam, closeCam, which, CROWD, payment } from '/rnd-hybrid/v3/lib/sets.js';

function toonify(obj) { obj.traverse((n) => { if (!n.isMesh) return; const m = n.material; n.material = toonMat({ color: m.color, map: m.map || null, emissive: m.emissive || new THREE.Color(0), emissiveIntensity: m.emissiveIntensity ?? 0 }); n.castShadow = n.receiveShadow = true; }); return obj; }
function label(text, { w = 2.4, h = 0.6, px = 120, bg = '#EDE4CF', fg = '#15171C', accent = null } = {}) {
  const c = document.createElement('canvas'); c.width = Math.round(w * 300); c.height = Math.round(h * 300); const g = c.getContext('2d');
  g.fillStyle = bg; g.fillRect(0, 0, c.width, c.height); if (accent) { g.fillStyle = accent; g.fillRect(0, 0, c.width, 22); }
  g.fillStyle = fg; g.font = `800 ${px}px Inter`; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(text, c.width / 2, c.height / 2 + 8);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.04), [toonMat({ color: bg }), toonMat({ color: bg }), toonMat({ color: bg }), toonMat({ color: bg }), toonMat({ map: t }), toonMat({ color: bg })]);
  m.castShadow = true; return m;
}
async function fit(path, height, o = {}) { const r = await prop(path, o); const b = new THREE.Box3().setFromObject(r); r.scale.multiplyScalar(height / (b.max.y - b.min.y)); return r; }

export async function boot(res) {
  for (const wt of [400, 600, 700, 800]) await document.fonts.load(`${wt} 48px Inter`);
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: false, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(), post = Post(renderer, W, H);
  scene.background = new THREE.Color('#3B4556'); scene.fog = new THREE.Fog('#3B4556', 28, 90);
  const hemi = new THREE.HemisphereLight('#C9D6EA', '#3A3026', 1.1), key = new THREE.DirectionalLight('#FFF1DC', 2.4);
  key.castShadow = true; key.shadow.mapSize.set(2048, 2048); Object.assign(key.shadow.camera, { left: -12, right: 12, top: 12, bottom: -12, near: 0.5, far: 60 }); key.shadow.bias = -0.0006; key.shadow.normalBias = 0.03;
  scene.add(hemi, key, key.target);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(400, 200), toonMat({ color: '#5C5852' })); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);

  // ---- S1: phố + ngân hàng + đám đông
  const walk = new THREE.Mesh(new THREE.BoxGeometry(40, 0.16, 12), toonMat({ color: '#77716A' })); walk.position.set(0, 0.08, -9); walk.receiveShadow = true; scene.add(walk);
  const bank = toonify(Bank({ closed: true })); bank.position.set(0, 0.16, -12.6); scene.add(bank);
  const blds = ['building-a', 'building-c', 'building-e', 'building-g', 'building-b', 'building-d', 'building-f', 'building-h'];
  for (let i = 0; i < 8; i++) { const b = await fit('city-kit-commercial/' + blds[i] + '.glb', 9 + (i % 3) * 2.5); const left = i < 4;
    b.position.set(left ? -9.5 - (i % 4) * 5.2 : 9.5 + (i % 4) * 5.2, 0.16, -14.5); scene.add(b); }
  const lamp = toonify(Lamp({ on: true })); lamp.position.set(-6.5, 0.16, -5.2); scene.add(lamp);
  const closed = label('CLOSED', { w: 1.9, h: 0.7, px: 150, fg: '#8E2B2B', accent: '#8E2B2B' }); closed.position.set(0, 0.16 + 0.88 + 1.55, -14.25); scene.add(closed);
  // đám đông 1930: đa dạng màu da/tóc, áo khoác, mũ phớt, cà vạt, váy dài
  const PEOPLE = [
    { sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'brown', outfit: 'brown', clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'f', skin: 'dark', hair: 'Buns', hairColor: 'black', outfit: 'dressPlum', hat: false, clip: 'Idle_Talking_Loop', expr: 'sad' },
    { sex: 'm', skin: 'medium', hair: 'Buzzed', hairColor: 'black', outfit: 'grey', clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'm', skin: 'deep', hair: 'Buzzed', hairColor: 'black', outfit: 'navy', clip: 'Idle_Talking_Loop', expr: 'shocked' },
    { sex: 'f', skin: 'light', hair: 'Long', hairColor: 'auburn', outfit: 'dressGreen', hat: false, clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'm', skin: 'tan', hair: 'SimpleParted', hairColor: 'black', outfit: 'tweed', beard: true, clip: 'Idle_Loop', expr: 'sad' },
    { sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'grey', outfit: 'charcoal', clip: 'Idle_Talking_Loop', expr: 'worried' },
    { sex: 'f', skin: 'medium', hair: 'Buns', hairColor: 'brown', outfit: 'dressNavy', hat: false, clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'm', skin: 'dark', hair: 'Buzzed', hairColor: 'black', outfit: 'brown', clip: 'Idle_Loop', expr: 'sad' },
    { sex: 'f', skin: 'tan', hair: 'Long', hairColor: 'black', outfit: 'dressPlum', hat: false, clip: 'Idle_Talking_Loop', expr: 'shocked' },
    { sex: 'm', skin: 'medium', hair: 'SimpleParted', hairColor: 'blond', outfit: 'grey', clip: 'Idle_Loop', expr: 'worried' },
    { sex: 'f', skin: 'light', hair: 'Buns', hairColor: 'grey', outfit: 'dressGreen', hat: false, clip: 'Idle_Loop', expr: 'sad' },
  ];
  const crowd = [];
  for (let i = 0; i < CROWD.length; i++) { const [x, z, rot] = CROWD[i], P = PEOPLE[i]; const p = await adult(P);
    p.root.position.set(x, 0.16, z); p.root.rotation.y = THREE.MathUtils.degToRad(rot + 180); p.face(P.expr); scene.add(p.root); crowd.push({ p, clip: P.clip, off: (x * 7.3 + z * 3.1) % 2 }); }
  const walt = await adult({ sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'brown', outfit: 'charcoal' }); walt.root.position.set(...WALT); walt.root.rotation.y = THREE.MathUtils.degToRad(35); walt.face('worried'); scene.add(walt.root);

  // ---- S2: phòng ký hợp đồng 1934
  const floor2 = new THREE.Mesh(new THREE.BoxGeometry(9, 0.1, 7), toonMat({ color: '#8A6A4C' })); floor2.position.set(X2, 0.05, -1.5); floor2.receiveShadow = true; scene.add(floor2);
  const wall = new THREE.Mesh(new THREE.BoxGeometry(9, 3.4, 0.2), toonMat({ color: '#C9B99A' })); wall.position.set(X2, 1.7, -3.6); wall.receiveShadow = true; scene.add(wall);
  const win = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.3, 0.05), toonMat({ color: '#DCE8F4', emissive: new THREE.Color('#DCE8F4'), emissiveIntensity: 0.6 })); win.position.set(X2 - 2.2, 1.9, -3.48); scene.add(win);
  const plaque = label('FHA · 1934', { w: 1.5, h: 0.42, px: 90, accent: '#4C8DFF' }); plaque.position.set(X2 + 1.2, 2.1, -3.47); scene.add(plaque);
  const desk = await fit('furniture-kit/desk.glb', 0.72); desk.position.set(X2, 0.1, -0.9); scene.add(desk);
  const chair = await fit('furniture-kit/chairDesk.glb', 0.95); chair.position.set(X2, 0.1, -2.0); chair.rotation.y = Math.PI; chair.visible = false; scene.add(chair);   // ghế Kenney lệch gốc toạ độ → ẩn (người che)
  const shelf = await fit('furniture-kit/bookcaseClosed.glb', 2.0); shelf.position.set(X2 + 3.2, 0.1, -3.2); scene.add(shelf);
  const plant = await fit('furniture-kit/pottedPlant.glb', 1.0); plant.position.set(X2 - 3.4, 0.1, -2.9); scene.add(plant);
  const lampT = await fit('furniture-kit/lampSquareTable.glb', 0.45); lampT.position.set(X2 - 0.55, 0.82, -1.15); scene.add(lampT);
  const doc = (() => { const c = document.createElement('canvas'); c.width = 420; c.height = 560; const g = c.getContext('2d'); g.fillStyle = '#F4EEDC'; g.fillRect(0, 0, 420, 560);
    g.fillStyle = '#15171C'; g.font = '800 46px Inter'; g.textAlign = 'center'; g.fillText('MORTGAGE', 210, 78); g.font = '700 30px Inter'; g.fillStyle = '#2F4F8A'; g.fillText('INSURED · FHA', 210, 126);
    g.fillStyle = '#8A8070'; for (let i = 0; i < 9; i++) g.fillRect(50, 170 + i * 34, i % 3 === 2 ? 220 : 320, 8); g.fillStyle = '#15171C'; g.fillRect(60, 500, 200, 4);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; const m = new THREE.Mesh(new THREE.BoxGeometry(0.42, 0.004, 0.56), [0, 0, 1, 0, 0, 0].map((k) => k ? toonMat({ map: t }) : toonMat({ color: '#F4EEDC' }))); m.receiveShadow = true; return m; })();
  doc.position.set(X2 + 0.1, 0.1 + 0.725, -1.0); doc.rotation.y = Math.PI + 0.15; scene.add(doc);
  const signer = await adult({ sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'brown', outfit: 'charcoal', hat: false }); signer.root.position.set(X2, 0.1, -1.95); signer.root.rotation.y = 0; signer.face('happy'); scene.add(signer.root);
  const hatOnDesk = fedora('#2C3038'); hatOnDesk.scale.setScalar(0.25); hatOnDesk.position.set(X2 - 0.5, 0.83, -0.8); hatOnDesk.visible = false;   // gốc bàn Kenney lệch → mũ rơi ngoài bàn; ẩn scene.add(hatOnDesk);
  const clerk = await adult({ sex: 'f', skin: 'dark', hair: 'Buns', hairColor: 'black', outfit: 'dressNavy', hat: false }); clerk.root.position.set(X2 + 1.25, 0.1, -2.2); clerk.root.rotation.y = THREE.MathUtils.degToRad(-25); clerk.face('happy'); scene.add(clerk.root);

  // ---- S3: lưới trả dần 20 → 30 năm (mỗi cột = 1 năm, 12 ô = 12 kỳ trả; cao ô ∝ khoản trả tháng, minh hoạ)
  const floor3 = new THREE.Mesh(new THREE.BoxGeometry(22, 0.1, 10), toonMat({ color: '#DCD3BF' })); floor3.position.set(X3 + 2, 0.05, -1); floor3.receiveShadow = true; scene.add(floor3);
  const p20 = payment(20), p30 = payment(30), U = 0.075 / p20 * 0.0066;   // chuẩn hoá: ô của khoản 20 năm cao 0,075 m
  const tile = new THREE.BoxGeometry(0.26, 1, 0.26);
  const m20 = toonMat({ color: '#4C8DFF' }), m30 = toonMat({ color: '#3FBF7F' });
  const grid = (n, z, mat, h) => { const im = new THREE.InstancedMesh(tile, mat, n * 12), M = new THREE.Matrix4(); let k = 0;
    for (let y = 0; y < n; y++) for (let m = 0; m < 12; m++) { M.compose(new THREE.Vector3(X3 - 4.2 + y * 0.34, 0.1 + h / 2 + m * (h + 0.012), z), new THREE.Quaternion(), new THREE.Vector3(1, h, 1)); im.setMatrixAt(k++, M); }
    im.castShadow = im.receiveShadow = true; scene.add(im); };
  grid(20, -0.4, m20, p20 / p20 * 0.075); grid(30, -2.0, m30, p30 / p20 * 0.075);
  const l20 = label('1934: UP TO 20 YEARS', { w: 4.4, h: 0.5, px: 96, accent: '#4C8DFF' }); l20.position.set(X3 - 1.6, 1.55, -0.4); scene.add(l20);
  const l30 = label('1954: UP TO 30 YEARS', { w: 4.4, h: 0.5, px: 96, accent: '#3FBF7F' }); l30.position.set(X3 + 2.4, 1.75, -2.0); scene.add(l30);
  const guide = await adult({ sex: 'm', skin: 'light', hair: 'SimpleParted', hairColor: 'brown', outfit: 'charcoal' }); guide.root.position.set(X3 + 3.4, 0.1, 1.4); guide.root.rotation.y = THREE.MathUtils.degToRad(-35); guide.face('happy'); scene.add(guide.root);
  for (const [x, z] of [[X3 + 8.5, -4], [X3 - 6, -4.5]]) { const tr = await fit('city-kit-suburban/tree-large.glb', 3.2); tr.position.set(x, 0.1, z); scene.add(tr); }

  const cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 400);
  const S2P = { pos: [X2 + 1.1, 1.3, 0.6], tgt: [X2 + 0.3, 1.15, -1.8], fov: 34 };   // H4′: trung cận người ký
  const LIGHT = { S1: ['#3B4556', '#C9D6EA', '#FFE2B8', 1.6, [-8, 12, 6]], S2: ['#B9A27E', '#FFF1DC', '#FFE8C2', 2.0, [-4, 6, 6]], S3: ['#CFE0F0', '#F4F8FF', '#FFF6E6', 2.4, [-6, 12, 8]] };
  function frame(t) {
    const w = which(t), sc = w === 'ORBIT' || w === 'CLOSE' ? 'S1' : w, P = w === 'ORBIT' ? orbitCam(t) : w === 'CLOSE' ? closeCam() : CAMS[w], L = LIGHT[sc];
    cam.position.set(...P.pos); cam.fov = P.fov; cam.lookAt(...P.tgt); cam.updateProjectionMatrix();
    scene.background.set(L[0]); scene.fog.color.set(L[0]); hemi.color.set(L[1]); key.color.set(L[2]); key.intensity = L[3];
    key.position.set(P.tgt[0] + L[4][0], L[4][1], P.tgt[2] + L[4][2]); key.target.position.set(P.tgt[0], 0, P.tgt[2]); key.target.updateMatrixWorld();
    const tt = w === 'ORBIT' ? t - 10 : 0.8;
    for (const c of crowd) c.p.pose(c.clip, tt + c.off);
    walt.pose('Idle_Loop', tt + 0.3);
    signer.pose('Sitting_Idle_Loop', 1.0, { arm: 'Interact' }); clerk.pose('Idle_Talking_Loop', 0.6);
    guide.pose('Idle_Talking_Loop', 0.5);
    post.render(scene, cam);
    return { violations: [] };
  }
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  const YEAR = { S1: '1930', S2: '1934', S3: '1934 → 1954', ORBIT: '1930', CLOSE: '1930' };
  function overlay(w) { const s = W / 1920; ctx.save(); ctx.scale(s, s);
    const pill = (txt, x, y, px, fg, bg, right) => { ctx.font = `600 ${px}px Inter`; const pw = ctx.measureText(txt).width + px * 0.9, ph = px * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px * 0.45, y + ph / 2 + px * 0.04); };
    pill(YEAR[w], 96, 54, 48, '#F2F4F7', 'rgba(14,17,22,0.72)'); pill('ILLUSTRATIVE', 1824, 54, 40, '#0E1116', 'rgba(242,244,247,0.88)', true);
    if (w === 'S3') { ctx.font = '400 40px Inter'; ctx.textAlign = 'right'; ctx.fillStyle = 'rgba(14,17,22,0.8)'; ctx.fillText('Source: National Housing Act 1934 §203; St. Louis Fed Review, Nov. 1955', 1824, 1016); }
    ctx.restore(); }
  return { canvas: out, frame: (t) => { const r = frame(t); ctx.drawImage(renderer.domElement, 0, 0); overlay(which(t)); return r; } };
}
