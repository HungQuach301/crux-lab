// R&D vòng 3 · CLIP v3 (P3, chủ dự án chọn 14/10): chương lịch sử = TRANH IN BÁO 1930 (2.5D: tấm tranh khắc xếp lớp trong 3D, máy trượt tạo thị sai);
// phần "Today" = biến thể MÀU SẠCH cùng bộ người figure1930.js (kiểu 'paper', không gạch). Cùng lời/giọng/mốc với v2 (đã đối chiếu nguồn gốc: v2/CLAIMS.md).
// Sửa theo chủ dự án: (a) 7/19 cảnh cận nhân vật (A2, C, E, F, J, L1, N) + H trung cận; (b) cảnh cột trụ ~17,5 s có người ở cửa + Walt tiền cảnh;
// (c) cảnh đêm: giấy vẫn sáng, đêm bằng tông xanh nhạt + quầng đèn (độ sáng đo ở v3/REPORT.md); (d) thẻ "THE WHOLE LOAN" mang nhãn BEFORE 1934, không lặp ở ~35 s.
// Ảnh LoC toàn khung ≤ 6 s, phủ tông sepia + vân in khớp P3, hoà 0,7 s / 0,8 s. Sang "Today": chuyển cảnh chủ ý "mực → màu" (lau ngang có mép giấy).
import * as THREE from 'three';
import { drawFigure, crowdSpec, INK } from '/rnd-hybrid/v3/style/figure1930.js';
import { facade, bankFacade, sky, pavement } from '/rnd-hybrid/v3/style/street2d.js';
import { hash } from '/rnd-hybrid/cutout/rig.js';

const SEG = '/rnd-hybrid/v3/clip3/seg/';
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x)), lin = (t, a, b) => clamp((t - a) / (b - a));
const ease = (t, a, b) => { const x = lin(t, a, b); return x * x * (3 - 2 * x); };
const backOut = (t, a, d = 0.35) => { if (t < a) return 0; const x = clamp((t - a) / d), c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const mix = (a, b, k) => a + (b - a) * k;
const HX = -60, BX = 0, OX = 60, GX = 120, TX = 180;

// ---- tấm tranh: canvas vẽ ở hệ px → mặt phẳng (gốc giữa đáy), bóng in nhẹ dưới tấm
function tex(c) { const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t; }
function sheet(w, h, ppm, draw, { shadow = true } = {}) {
  const c = document.createElement('canvas'); c.width = Math.round(w * ppm); c.height = Math.round(h * ppm); draw(c.getContext('2d'), c.width, c.height);
  let src = c; if (shadow) { const s = document.createElement('canvas'); s.width = c.width; s.height = c.height; const sg = s.getContext('2d'); sg.filter = 'blur(6px)'; sg.drawImage(c, 7, 7); sg.filter = 'none';
    sg.globalCompositeOperation = 'source-in'; sg.fillStyle = 'rgba(40,30,15,0.33)'; sg.fillRect(0, 0, s.width, s.height); sg.globalCompositeOperation = 'source-over'; sg.drawImage(c, 0, 0); src = s; }
  const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: tex(src), transparent: true, alphaTest: 0.04 })); m.geometry.translate(0, h / 2, 0); m.userData.canvas = c; return m;
}
// người (tấm): cao 1,78 m mặc định; ppm theo cỡ xuất hiện lớn nhất
const FIG = new Map();
function person(o, { height = 1.78, ppm = 300 } = {}) { const key = JSON.stringify([o, height, ppm]); if (FIG.has(key)) return FIG.get(key).clone();
  const m = sheet(height * 0.62, height * 1.12, ppm, (g, W, H) => { g.translate(W / 2, H - 6); const s = (H - 12) / 830; g.scale(s, s); drawFigure(g, o); }); FIG.set(key, m); return m.clone(); }
// thẻ chữ: giấy báo, viền mực, chữ serif đậm (không gạch trên chữ)
function card(lines, { sub = null, tag = null, accent = '#8E2B2B', w = 2.6, h = 1.0, px = 150, subPx = 70, color = false } = {}) {
  return sheet(w, h, 300, (g, W, H) => { g.fillStyle = color ? '#FBF7EE' : '#F1E8D3'; g.fillRect(6, 6, W - 12, H - 12); g.strokeStyle = INK; g.lineWidth = 8; g.strokeRect(6, 6, W - 12, H - 12);
    g.lineWidth = 2; g.strokeRect(22, 22, W - 44, H - 44); if (accent) { g.fillStyle = accent; g.fillRect(22, 22, W - 44, 18); }
    const L = [].concat(lines); let y = H / 2 - (L.length - 1) * px * 0.55 - (sub ? subPx * 0.55 : 0) + (tag ? subPx * 0.55 : 0);
    if (tag) { g.font = `800 ${subPx}px Georgia, serif`; const tw = g.measureText(tag).width + 40; g.fillStyle = '#8E2B2B'; g.fillRect(W / 2 - tw / 2, 52, tw, subPx * 1.3); g.fillStyle = '#F4EEDC'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(tag, W / 2, 52 + subPx * 0.68); }
    g.fillStyle = INK; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = `700 ${px}px Georgia, 'Times New Roman', serif`;
    const fit = Math.min(1, ...L.map((s) => (W - 90) / Math.max(1, g.measureText(s).width))); g.font = `700 ${Math.floor(px * fit)}px Georgia, 'Times New Roman', serif`; for (const s of L) { g.fillText(s, W / 2, y); y += px * 1.1; }   // co chữ cho vừa thẻ
    if (sub) { g.font = `italic 600 ${subPx}px Georgia, serif`; g.fillStyle = '#3A342A'; g.fillText(sub, W / 2, y - px * 0.25 + subPx * 0.35); } });
}
// nhà ở 1930 (dãy nhà gạch có bậc thềm), bằng facade 'office' + cửa/bậc
function rowHouse(seed, style) { return sheet(7, 10, 110, (g, W, H) => { facade(g, W, H, { kind: 'office', sign: null, awning: null, brick: ['#8A5A44', '#7A5040', '#86553F'][seed % 3], seed, style }); }); }
// nhà hôm nay (màu sạch): ván ốp ngang, cửa sổ lớn, gara, mái dốc
function modernHouse() { return sheet(12, 7, 120, (g, W, H) => { const st = (c) => c; g.fillStyle = '#C9D3DC'; g.beginPath(); g.moveTo(W * 0.04, H * 0.38); g.lineTo(W * 0.5, H * 0.04); g.lineTo(W * 0.96, H * 0.38); g.closePath(); g.fill(); g.strokeStyle = INK; g.lineWidth = 6; g.stroke();
  g.fillStyle = '#EDEFF1'; g.fillRect(W * 0.08, H * 0.38, W * 0.84, H * 0.62); g.strokeRect(W * 0.08, H * 0.38, W * 0.84, H * 0.62);
  g.strokeStyle = 'rgba(23,21,15,0.25)'; g.lineWidth = 2; for (let y = H * 0.42; y < H; y += 26) { g.beginPath(); g.moveTo(W * 0.08, y); g.lineTo(W * 0.92, y); g.stroke(); }
  g.fillStyle = '#7FA6C8'; g.fillRect(W * 0.14, H * 0.5, W * 0.26, H * 0.24); g.strokeStyle = INK; g.lineWidth = 5; g.strokeRect(W * 0.14, H * 0.5, W * 0.26, H * 0.24);
  g.fillStyle = '#D9DEE3'; g.fillRect(W * 0.56, H * 0.56, W * 0.32, H * 0.44); g.strokeRect(W * 0.56, H * 0.56, W * 0.32, H * 0.44); for (let y = H * 0.62; y < H; y += 30) { g.beginPath(); g.moveTo(W * 0.56, y); g.lineTo(W * 0.88, y); g.stroke(); }
  g.fillStyle = '#4C6E9E'; g.fillRect(W * 0.44, H * 0.6, W * 0.08, H * 0.4); g.strokeRect(W * 0.44, H * 0.6, W * 0.08, H * 0.4); }); }
function tree(color) { return sheet(3, 5, 100, (g, W, H) => { g.fillStyle = '#5A4330'; g.fillRect(W * 0.45, H * 0.55, W * 0.1, H * 0.45); g.strokeStyle = INK; g.lineWidth = 4; g.strokeRect(W * 0.45, H * 0.55, W * 0.1, H * 0.45);
  for (const [x, y, r] of [[0.5, 0.36, 0.34], [0.3, 0.5, 0.22], [0.7, 0.5, 0.24]]) { g.fillStyle = color; g.beginPath(); g.arc(W * x, H * y, W * r, 0, 7); g.fill(); g.stroke(); } }); }

export async function boot(res) {
  for (const f of ['700 48px Georgia', 'italic 600 48px Georgia', '800 48px Georgia', '600 48px Inter', '400 48px Inter']) await document.fonts.load(f);
  const TL = await (await fetch(SEG + 'timeline.json')).json(), A = TL.a, SH = Object.fromEntries(TL.shots.map((s) => [s.id, s]));
  const W = Math.round(res * 16 / 9), H = res, E = 'engrave';
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true }); renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(); scene.background = new THREE.Color('#E4D8BE'); scene.fog = new THREE.Fog('#E4D8BE', 18, 70);
  const at = (o, x, y, z, ry = 0) => { o.position.set(x, y, z); o.rotation.y = ry; scene.add(o); return o; };
  const skyTex = (() => { const c = document.createElement('canvas'); c.width = 2100; c.height = 560; sky(c.getContext('2d'), 2100, 560, { style: E }); return tex(c); })();
  const paveTex = (() => { const c = document.createElement('canvas'); c.width = 2048; c.height = 1024; pavement(c.getContext('2d'), 2048, 1024, { style: E }); const t = tex(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(5, 2.5); return t; })();
  const ground = (x, map, color) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(56, 40), new THREE.MeshBasicMaterial(map ? { map } : { color })); m.rotation.x = -Math.PI / 2; m.position.set(x, 0, -6); scene.add(m); };
  const skyAt = (x, t) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(150, 40), new THREE.MeshBasicMaterial({ map: t, fog: false })); m.position.set(x, 20, -60); scene.add(m); };
  for (const x of [HX, BX, GX]) { skyAt(x, skyTex); ground(x, paveTex); }
  // ---- HOME: dãy nhà 1930
  for (let i = 0; i < 5; i++) at(rowHouse(i + 1, E), HX - 14.6 + i * 7.3, 0, -13 - (i % 2) * 0.8);
  at(tree('#7D8462'), HX - 5.2, 0, -9.5); at(tree('#6E7658'), HX + 5.6, 0, -10);
  // ---- BANK: phố + ngân hàng + đám đông (thưa / đông)
  const SIGNS = [['LUNCH', '#8E3B33', 'shop'], ['HATS', '#3E5A4A', 'shop'], [null, null, 'office'], ['DRUGS', '#7A5A2E', 'shop']];
  for (let i = 0; i < 4; i++) { const left = i < 2, [sign, awn, kind] = SIGNS[i], h = 13 + (i % 2) * 3;
    at(sheet(9, h, 110, (g, w, hh) => facade(g, w, hh, { kind, sign, awning: awn, seed: i + 2, style: E, fire: i === 1 || i === 3 })), left ? -21.5 + (i % 2) * 9.2 : 12.3 + (i % 2) * 9.2, 0, -20 - (i % 2) * 1.5); }
  const bank = at(sheet(13, 10.7, 150, (g, w, h) => bankFacade(g, w, h, { style: E, closed: true })), BX - 0.4, 0, -16.5);
  const bankOpen = at(sheet(13, 10.7, 150, (g, w, h) => bankFacade(g, w, h, { style: E, closed: false })), BX - 0.4, 0, -16.49);
  const crowd = [], sparse = [];
  for (const [z, n, seed, dx] of [[-14.6, 11, 3, 0.0], [-12.6, 10, 5, 0.6], [-10.6, 9, 7, -0.4], [-8.6, 8, 9, 0.3]]) crowdSpec(n, seed).forEach((o, i) => {
    crowd.push(at(person({ ...o, style: E }, { height: 1.78 * o.s, ppm: 160 }), BX + dx - 7.4 + 14.8 * (i + 0.5) / n + ((i * 37) % 7 - 3) * 0.05, 0, z + ((i * 13) % 5) * 0.1)); });
  crowdSpec(5, 21).forEach((o, i) => sparse.push(at(person({ ...o, view: i % 2 ? 'front' : 'back', expr: 'neutral', style: E }, { height: 1.78 * o.s, ppm: 160 }), BX - 9 + i * 4.3, 0, -9 - (i % 3) * 1.6)));
  // ---- OFFICE 1934: tường ốp gỗ, cửa sổ, bảng FHA, bàn
  at(sheet(16, 6, 110, (g, w, h) => { g.fillStyle = '#C9B99A'; g.fillRect(0, 0, w, h); g.strokeStyle = INK; for (let x = 0; x < w; x += 140) { g.lineWidth = 3; g.strokeRect(x + 16, h * 0.45, 108, h * 0.5); }
    g.globalAlpha = 0.35; g.lineWidth = 1.2; for (let y = 4; y < h * 0.42; y += 9) { g.beginPath(); g.moveTo(0, y); g.lineTo(w, y); g.stroke(); } g.globalAlpha = 1;
    g.fillStyle = '#E8E2D2'; g.fillRect(w * 0.08, h * 0.14, w * 0.18, h * 0.4); g.lineWidth = 6; g.strokeRect(w * 0.08, h * 0.14, w * 0.18, h * 0.4); g.beginPath(); g.moveTo(w * 0.17, h * 0.14); g.lineTo(w * 0.17, h * 0.54); g.moveTo(w * 0.08, h * 0.34); g.lineTo(w * 0.26, h * 0.34); g.stroke(); }, { shadow: false }), OX, 0, -4);
  const floorO = new THREE.Mesh(new THREE.PlaneGeometry(20, 12), new THREE.MeshBasicMaterial({ color: '#B9A684' })); floorO.rotation.x = -Math.PI / 2; floorO.position.set(OX, 0.001, -1); scene.add(floorO);
  const desk = sheet(3.2, 1.05, 200, (g, w, h) => { g.fillStyle = '#7A5A3A'; g.fillRect(0, h * 0.14, w, h * 0.86); g.fillStyle = '#9A7650'; g.fillRect(0, 0, w, h * 0.16); g.strokeStyle = INK; g.lineWidth = 6; g.strokeRect(3, 3, w - 6, h - 6);
    g.lineWidth = 3; g.strokeRect(w * 0.08, h * 0.3, w * 0.36, h * 0.24); g.strokeRect(w * 0.56, h * 0.3, w * 0.36, h * 0.24); g.globalAlpha = 0.4; for (let x = 10; x < w; x += 9) { g.beginPath(); g.moveTo(x, h * 0.62); g.lineTo(x - 30, h); g.stroke(); } g.globalAlpha = 1;
    g.fillStyle = '#F4EEDC'; g.save(); g.translate(w * 0.42, h * 0.02); g.rotate(-0.04); g.fillRect(0, 0, w * 0.2, h * 0.11); g.restore(); });
  // ---- GRID: sổ cái trả dần (vẽ lại mỗi khung theo số cột hiện)
  const led = document.createElement('canvas'); led.width = 3000; led.height = 1500; const ledT = tex(led);
  const ledger = new THREE.Mesh(new THREE.PlaneGeometry(10, 5), new THREE.MeshBasicMaterial({ map: ledT })); ledger.geometry.translate(0, 2.5, 0); at(ledger, GX, 0.3, -6);
  const PAY = (n) => { const r = 0.05 / 12, N = n * 12; return r / (1 - Math.pow(1 + r, -N)); };
  let ledKey = '';
  function drawLedger(n20, n30) { const k = n20 + '|' + n30; if (k === ledKey) return; ledKey = k; const g = led.getContext('2d'), w = 3000, h = 1500;
    g.fillStyle = '#EFE6D0'; g.fillRect(0, 0, w, h); g.strokeStyle = INK; g.lineWidth = 10; g.strokeRect(8, 8, w - 16, h - 16);
    g.lineWidth = 1.5; g.globalAlpha = 0.25; for (let y = 60; y < h; y += 40) { g.beginPath(); g.moveTo(30, y); g.lineTo(w - 30, y); g.stroke(); } g.globalAlpha = 1;
    const cell = (x, y, cw, ch, fill) => { g.fillStyle = fill; g.fillRect(x, y, cw, ch); g.strokeStyle = INK; g.lineWidth = 2.5; g.strokeRect(x, y, cw, ch); };
    const h20 = 30, h30 = 30 * PAY(30) / PAY(20), cw = 80, x0 = 140;
    for (let c = 0; c < n20; c++) for (let m = 0; m < 12; m++) cell(x0 + c * 90, 700 - (m + 1) * (h20 + 4), cw, h20, '#6E8FBF');
    for (let c = 0; c < n30; c++) for (let m = 0; m < 12; m++) cell(x0 + c * 90, 1400 - (m + 1) * (h30 + 4), cw, h30, '#7FA88A');
    g.fillStyle = INK; g.font = '700 86px Georgia, serif'; g.textAlign = 'left'; g.fillText('1 column = 1 year · 1 box = 1 monthly payment', 140, 110);
    ledT.needsUpdate = true; }
  // ---- TODAY (màu sạch)
  const groundT = (() => { const m = new THREE.Mesh(new THREE.PlaneGeometry(56, 40), new THREE.MeshBasicMaterial({ color: '#B8C4A0' })); m.rotation.x = -Math.PI / 2; m.position.set(TX, 0, -6); scene.add(m); })();
  const skyT = new THREE.Mesh(new THREE.PlaneGeometry(150, 40), new THREE.MeshBasicMaterial({ color: '#BFD6EA', fog: false })); skyT.position.set(TX, 20, -60); scene.add(skyT);
  at(modernHouse(), TX - 1, 0, -12); at(tree('#6FA06A'), TX - 9, 0, -10.5); at(tree('#5E9460'), TX + 8.5, 0, -11);
  // ---- người chính (tấm theo cảm xúc/tư thế)
  const WALT = (expr, pose = { L: 'down', R: 'down' }, ppm = 520) => person({ sex: 'm', skin: 'light', coat: 'charcoal', hat: 'fedora', expr, pose, style: E }, { ppm });
  const RUTH = (expr) => person({ sex: 'f', skin: 'medium', coat: 'plum', hat: 'cloche', expr, style: E }, { height: 1.66, ppm: 400 });
  const pool = new THREE.Group(); scene.add(pool);
  const use = (m, x, y, z, ry = 0, s = 1) => { m.position.set(x, y, z); m.rotation.y = ry; m.scale.setScalar(Math.max(0.001, s)); m.visible = s > 0.001; pool.add(m); return m; };
  // thẻ (số có nguồn: v2/CLAIMS.md)
  const C = { half: card(['≈ HALF', 'THE PRICE'], { sub: 'the most a bank would lend', accent: '#B8862F', h: 1.25 }), years: card('3–5 YEARS', { accent: '#B8862F', h: 0.75 }),
    due: card(['THE WHOLE', 'LOAN'], { sub: 'due at the end', tag: 'BEFORE 1934', h: 1.9, w: 3.0, px: 140, subPx: 64 }), fha: card('FHA · 1934', { sub: 'Federal Housing Administration', accent: '#2F4F8A', h: 1.05, w: 3.0 }),
    insured: card('INSURED', { accent: '#2F4F8A', h: 0.6, w: 1.7, px: 120 }), eighty: card(['UP TO 80%', 'OF VALUE'], { accent: '#2F4F8A', h: 1.2 }),
    twenty: card('1934: UP TO 20 YEARS', { accent: '#2F4F8A', h: 0.62, w: 4.4, px: 130 }), thirty: card('1954: UP TO 30 YEARS', { accent: '#3E7A52', h: 0.62, w: 4.4, px: 130 }) };
  const cal = [1, 2, 3, 4, 5].map((k) => card(String(k), { sub: 'year', accent: k >= 3 ? '#B8862F' : null, h: 0.7, w: 0.6, px: 170, subPx: 50 }));
  const val = [...Array(10)].map((_, i) => [card('', { accent: null, w: 0.42, h: 0.42 }), sheet(0.42, 0.42, 200, (g, w, h) => { g.fillStyle = '#6E8FBF'; g.fillRect(4, 4, w - 8, h - 8); g.strokeStyle = INK; g.lineWidth = 6; g.strokeRect(4, 4, w - 8, h - 8); })]);
  const cache = new Map(); const get = (k, mk) => { if (!cache.has(k)) cache.set(k, mk()); return cache.get(k); };
  const Wt = (expr, pose, ppm) => get(['W', expr, JSON.stringify(pose), ppm].join(), () => WALT(expr, pose, ppm)), Rt = (expr) => get('R' + expr, () => RUTH(expr));
  const clerk = get('clerk', () => person({ sex: 'f', skin: 'dark', coat: 'navy', hat: 'none', hair: '#1A1612', expr: 'happy', pose: { L: 'down', R: 'point' }, style: E }, { height: 1.66, ppm: 400 }));
  const sam = get('sam', () => person({ sex: 'm', era: 'today', skin: 'tan', coat: '#4C6E9E', hair: '#1A1612', expr: 'happy', style: 'paper' }, { ppm: 420 }));
  const kid = get('kid', () => person({ sex: 'f', era: 'today', skin: 'dark', coat: '#9E5A4C', hair: '#1A1612', expr: 'happy', style: 'paper' }, { height: 1.6, ppm: 420 }));

  // ---- máy quay theo cảnh [từ, đến]: pos, tgt, fov
  const P = (pos, tgt, fov) => ({ pos, tgt, fov });
  const CAM = {
    A1: [P([HX + 2.5, 1.9, 4], [HX, 2.6, -12], 40), P([HX + 1.6, 1.8, 1.5], [HX - 0.4, 2.2, -12], 36)],
    A2: [P([HX - 0.9, 1.66, -4.3], [HX - 1.3, 1.62, -12], 32), P([HX - 0.95, 1.66, -4.55], [HX - 1.3, 1.62, -12], 30)],   // cận
    B: [P([BX + 4.5, 1.8, 2.5], [BX, 3.4, -16], 42), P([BX + 3.2, 1.8, 0.8], [BX, 3.4, -16], 40)],
    C: [P([HX + 1.4, 1.55, -1.6], [HX + 0.6, 1.4, -12], 38), P([HX + 1.3, 1.55, -2.0], [HX + 0.6, 1.4, -12], 36)],      // trung cận
    D: [P([HX + 1.5, 1.2, -2.0], [HX + 0.4, 1.9, -12], 42), P([HX + 1.4, 1.2, -2.4], [HX + 0.4, 1.9, -12], 40)],
    E: [P([BX + 1.6, 1.68, -2.8], [BX + 1.0, 1.7, -16], 32), P([BX + 1.55, 1.68, -3.1], [BX + 1.0, 1.7, -16], 30)],       // cận, cửa đóng sau lưng
    F: [P([HX - 1.6, 1.55, -3.6], [HX - 1.7, 1.5, -12], 34), P([HX - 1.65, 1.55, -3.9], [HX - 1.7, 1.5, -12], 32)],      // trung cận Walt + Ruth (đêm)
    G: [P([BX + 1.5, 2.6, 4.0], [BX, 3.6, -16], 44), P([BX + 0.8, 2.2, 1.0], [BX, 3.4, -16], 42)],
    H: [P([BX + 2.6, 1.9, -5.4], [BX - 0.4, 3.0, -16.5], 40), P([BX + 2.2, 1.95, -6.6], [BX - 0.4, 3.0, -16.5], 36)],    // cột trụ + người ở cửa + Walt tiền cảnh
    J: [P([BX + 0.55, 1.68, -0.55], [BX + 0.5, 1.72, -10], 34), P([BX + 0.5, 1.68, -0.8], [BX + 0.5, 1.72, -10], 32)],    // cận (K1)
    K1: [P([BX + 0.8, 2.1, -1.0], [BX, 3.2, -16], 44), P([BX + 1.6, 3.2, 3.0], [BX, 3.6, -16], 44)],
    K2: [P([OX + 0.8, 1.8, 3.2], [OX + 0.4, 2.0, -4], 40), P([OX + 0.6, 1.8, 2.6], [OX + 0.4, 2.0, -4], 38)],
    L1: [P([OX - 0.2, 1.55, 0.6], [OX - 0.2, 1.45, -4], 32), P([OX - 0.2, 1.55, 0.35], [OX - 0.2, 1.45, -4], 30)],       // cận ký
    L2: [P([HX + 2.6, 1.7, -1.6], [HX + 1.8, 1.6, -12], 40), P([HX + 2.4, 1.7, -2.0], [HX + 1.8, 1.6, -12], 38)],
    M: [P([GX - 0.6, 3.0, 4.2], [GX, 3.1, -6], 46), P([GX + 0.2, 3.0, 3.6], [GX, 3.1, -6], 44)],
    N: [P([GX + 3.6, 1.68, -0.6], [GX + 3.4, 1.7, -8], 32), P([GX + 3.55, 1.68, -0.85], [GX + 3.4, 1.7, -8], 30)],       // cận nhẹ nhõm
    O: [P([GX + 0.4, 3.0, 4.2], [GX, 3.1, -6], 46), P([GX - 0.2, 3.0, 3.8], [GX, 3.1, -6], 44)],
    P: [P([TX + 0.4, 1.66, -1.8], [TX + 0.6, 1.6, -12], 34), P([TX + 1.2, 2.2, 3.0], [TX, 2.6, -12], 42)],
  };
  CAM.I = [CAM.H[1], CAM.H[1]];
  const NIGHT = { E: [0, 1], F: 1, G: 1, H: 1, I: 1, J: 1, K1: [1, 0] };   // E: hoàng hôn → đêm; K1: đêm → rạng sáng
  const shotAt = (t) => TL.shots.find((s) => t >= s.t0 && t < s.t1) || TL.shots[TL.shots.length - 1];

  function stage(id, t, sh) {
    pool.clear(); for (const c of crowd) c.visible = false; for (const s of sparse) s.visible = false; bank.visible = true; bankOpen.visible = false;
    const lt = t - sh.t0;
    switch (id) {
      case 'A1': use(Wt('happy'), HX - 0.7, 0, -7.2); use(Rt('happy'), HX - 1.9, 0, -7.4); break;
      case 'A2': use(Wt(t > A.home ? 'happy' : 'neutral', { L: 'down', R: t > A.home ? 'point' : 'down' }), HX - 1.25, 0, -6.6); use(Rt('happy'), HX - 2.4, 0, -7.0); break;
      case 'B': bank.visible = false; bankOpen.visible = true; sparse.forEach((s) => (s.visible = true)); use(Wt(t > A.half + 0.3 ? 'neutral' : 'happy'), BX + 2.2, 0, -8.5);
        use(C.half, BX - 1.4, 1.2, -8.8, 0, backOut(t, A.half)); break;
      case 'C': use(Wt('neutral', { L: 'down', R: 'chin' }), HX - 0.1, 0, -6.6); cal.forEach((c, i) => use(c, HX + 0.5 + i * 0.66, 0.3, -6.4, 0, backOut(t, i < 3 ? A.three + i * 0.12 : A.five + (i - 3) * 0.12)));
        use(C.years, HX + 1.7, 1.75, -7.0, 0, backOut(t, A.five + 0.3)); break;
      case 'D': { use(Wt(t > A.whole + 0.25 ? 'anxious' : 'neutral', t > A.whole + 0.25 ? { L: 'chin', R: 'down' } : undefined), HX - 0.6, 0, -6.6);
        const f = ease(t, A.whole - 0.1, A.once + 0.1); const d = use(C.due, HX + 1.6, (1 - f) * 5, -8.2, 0, 1); d.rotation.z = (1 - f) * 0.4; break; }
      case 'E': use(Wt('worried', { L: 'clasp', R: 'clasp' }), BX + 1.0, 0, -5.4); sparse.forEach((s, i) => (s.visible = i < 2)); break;
      case 'F': use(Wt('sad'), HX - 1.4, 0, -6.6); use(Rt('worried'), HX - 2.35, 0, -6.9); break;
      case 'G': crowd.forEach((c) => (c.visible = true)); break;
      case 'H': crowd.forEach((c) => (c.visible = true)); use(Wt('worried', { L: 'clasp', R: 'clasp' }), BX + 1.3, 0, -8.1, 0.15); break;
      case 'I': case 'J': crowd.forEach((c) => (c.visible = true)); use(Wt('worried', { L: 'clasp', R: 'clasp' }), BX + 1.15, 0, -2.6); break;
      case 'K1': crowd.forEach((c, i) => (c.visible = hash(i + 3) < 1 - ease(t, sh.t0, sh.t1) * 0.7)); break;
      case 'K2': use(C.fha, OX + 0.4, 2.0, -3.9, 0, backOut(t, A.fha)); use(clerk, OX + 1.8, 0, -2.8); use(desk, OX - 0.2, 0, -1.8); use(Wt('relieved', undefined, 400), OX - 1.6, 0, -2.9); break;
      case 'L1': use(Wt('happy', { L: 'down', R: 'write' }), OX - 0.2, -0.3, -2.4); use(desk, OX - 0.2, 0, -1.6); use(C.insured, OX + 0.85, 1.55, -3.0, 0, backOut(t, A.insured + 0.1)); break;
      case 'L2': use(Wt('happy'), HX - 0.4, 0, -7.0); val.forEach(([a, b], i) => use(t > A.eighty + i * 0.05 && i < 8 ? b : a, HX + 0.8 + i * 0.47, 1.05, -6.2));
        use(C.eighty, HX + 3.0, 1.8, -6.6, 0, backOut(t, A.eighty + 0.2)); break;
      case 'M': drawLedger(Math.floor(clamp(lin(t, A.paid, A.twenty + 0.2)) * 20) + 1, 0); use(C.twenty, GX - 2.6, 5.45, -5.85, 0, backOut(t, A.twenty)); use(Wt('happy', { L: 'down', R: 'point' }), GX + 5.6, 0, -5.4); break;
      case 'N': drawLedger(20, 0); use(Wt(t > A.bill ? 'relieved' : 'happy'), GX + 3.4, 0, -4.4); break;
      case 'O': drawLedger(20, Math.floor(clamp(lin(t, A.y1954, A.thirty + 0.4)) * 30) + 1); use(C.thirty, GX + 2.6, 5.45, -5.85, 0, backOut(t, A.y1954)); use(C.twenty, GX - 2.6, 5.45, -5.9, 0, 1); break;
      case 'P': use(sam, TX + 0.75, 0, -4.8); use(kid, TX - 0.35, 0, -5.1); break;
    }
  }
  // ---- ảnh tư liệu LoC (phủ tông sepia + vân in khớp P3)
  const im = new Image(); im.src = '/rnd-hybrid/work/external/bank1931_crop.jpg'; await im.decode();
  const tone = new OffscreenCanvas(W, H), tg = tone.getContext('2d'); tg.filter = 'contrast(1.1)'; tg.drawImage(im, 0, 0, W, H); tg.filter = 'none';
  { const d = tg.getImageData(0, 0, W, H), stops = [[0, [23, 21, 15]], [0.45, [94, 84, 70]], [0.8, [184, 169, 140]], [1, [236, 226, 203]]];
    const lut = (v) => { const x = v / 255; for (let i = 1; i < stops.length; i++) if (x <= stops[i][0]) { const [a, ca] = stops[i - 1], [b, cb] = stops[i], k = (x - a) / (b - a); return ca.map((c, j) => c + (cb[j] - c) * k); } return stops[3][1]; };
    for (let i = 0; i < d.data.length; i += 4) { const v = d.data[i] * 0.299 + d.data[i + 1] * 0.587 + d.data[i + 2] * 0.114, c = lut(v); d.data[i] = c[0]; d.data[i + 1] = c[1]; d.data[i + 2] = c[2]; }
    tg.putImageData(d, 0, 0); tg.strokeStyle = 'rgba(23,21,15,0.10)'; tg.lineWidth = Math.max(1, H / 900); for (let y = 0; y < H; y += Math.max(3, H / 270)) { tg.beginPath(); tg.moveTo(0, y); tg.lineTo(W, y); tg.stroke(); } }
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  const YEAR = { A1: '1930', A2: '1930', B: '1930', C: '1930', D: '1930', E: '1930', F: '1930', G: 'December 1930', H: 'December 1930', I: '1931', J: '1931', K1: '1934', K2: '1934', L1: '1934', L2: '1934', M: '1934', N: '1934', O: '1954', P: 'Today' };
  const SRC = { B: 'Source: HUD, FHA history', C: 'Source: HUD, FHA history', D: 'Source: HUD, FHA history', G: 'Source: Federal Reserve History', H: 'Source: Federal Reserve History',
    I: 'Photo: Library of Congress (NYWT&S), 1931', K2: 'Source: HUD, FHA history', L2: 'Source: National Housing Act of 1934, §203', M: 'Source: National Housing Act of 1934, §203', O: 'Source: Federal Reserve Bank of St. Louis Review, Nov. 1955' };
  function chrome(id, archival) { const s = W / 1920; ctx.save(); ctx.scale(s, s);
    const pill = (txt, x, y, px, fg, bg, right) => { ctx.font = `600 ${px}px Inter`; const pw = ctx.measureText(txt).width + px * 0.9, ph = px * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px * 0.45, y + ph / 2 + px * 0.04); };
    pill(YEAR[id], 96, 54, 48, '#F2F4F7', 'rgba(23,21,15,0.82)'); if (!archival) pill('ILLUSTRATIVE', 1824, 54, 40, '#17150F', 'rgba(242,236,220,0.92)', true);
    const src = SRC[id]; if (src) { ctx.font = '400 40px Inter'; ctx.textAlign = 'right'; ctx.textBaseline = 'alphabetic'; ctx.fillStyle = 'rgba(242,236,220,0.85)'; ctx.fillText(src, 1826, 1018); ctx.fillStyle = 'rgba(23,21,15,0.95)'; ctx.fillText(src, 1824, 1016); }
    ctx.restore(); }
  // đêm: tông xanh xám nhân (multiply) + quầng đèn — giấy vẫn đủ sáng
  function night(k) { if (k <= 0) return; ctx.save(); ctx.globalCompositeOperation = 'multiply'; ctx.fillStyle = `rgba(120,134,160,${0.55 * k})`; ctx.fillRect(0, 0, W, H); ctx.restore();
    ctx.save(); ctx.globalCompositeOperation = 'screen'; for (const [x, y] of [[0.12, 0.3], [0.88, 0.32]]) { const g = ctx.createRadialGradient(W * x, H * y, 4, W * x, H * y, H * 0.5); g.addColorStop(0, `rgba(255,214,140,${0.35 * k})`); g.addColorStop(1, 'rgba(255,214,140,0)'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); } ctx.restore(); }
  function render3d(id, t, sh, k) {
    const [c0, c1] = CAM[id], p = { pos: c0.pos.map((v, i) => mix(v, c1.pos[i], k)), tgt: c0.tgt.map((v, i) => mix(v, c1.tgt[i], k)), fov: mix(c0.fov, c1.fov, k) };
    const cam = render3d.cam || (render3d.cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 300)); cam.position.set(...p.pos); cam.fov = p.fov; cam.lookAt(...p.tgt); cam.updateProjectionMatrix();
    const today = id === 'P'; scene.fog.color.set(today ? '#DDE7EF' : '#E4D8BE'); scene.background.set(today ? '#DDE7EF' : '#E4D8BE');
    stage(id, t, sh); renderer.render(scene, cam); ctx.drawImage(renderer.domElement, 0, 0);
    const n = NIGHT[id]; night(n === undefined ? 0 : Array.isArray(n) ? mix(n[0], n[1], ease(t, sh.t0 + 0.2, sh.t1 - 0.2)) : n);
  }
  let oEnd = null;   // khung cuối cảnh O (mực), dùng cho chuyển cảnh mực → màu
  function frame(t) {
    const sh0 = shotAt(t), id0 = sh0.id, ai = TL.archival.in, ao = TL.archival.out, arch = t >= ai && t < ao ? Math.min(ease(t, ai, ai + 0.7), 1 - ease(t, ao - 0.8, ao)) : 0;
    if (id0 === 'I' && arch > 0.999) { ctx.fillStyle = '#17150F'; ctx.fillRect(0, 0, W, H); }
    else if (id0 === 'I') render3d('H', SH.H.t1 - 0.01, SH.H, 1);
    else render3d(id0, t, sh0, ease(t, sh0.t0, sh0.t1));
    if (arch > 0) { const k = lin(t, ai, ao), z = 1.02 + 0.07 * k, w = W * z, h = H * z; ctx.save(); ctx.globalAlpha = arch; ctx.drawImage(tone, (W - w) / 2 - W * 0.02 * k, (H - h) / 2 - H * 0.015 * k, w, h); ctx.restore(); }
    // chuyển cảnh chủ ý sang Today: lau ngang 0,9 s, phần mực (khung cuối O) bị gạt sang phải, mép giấy có nét mực
    if (id0 === 'P' && t < sh0.t0 + 0.9) {
      if (!oEnd) { const keep = document.createElement('canvas'); keep.width = W; keep.height = H; const kc = keep.getContext('2d'); kc.drawImage(out, 0, 0);
        render3d('O', SH.O.t1 - 0.01, SH.O, 1); chrome('O', false); oEnd = document.createElement('canvas'); oEnd.width = W; oEnd.height = H; oEnd.getContext('2d').drawImage(out, 0, 0); ctx.drawImage(keep, 0, 0); }
      const x = W * ease(t, sh0.t0, sh0.t0 + 0.9); ctx.save(); ctx.beginPath(); ctx.rect(x, 0, W - x, H); ctx.clip(); ctx.drawImage(oEnd, 0, 0); ctx.restore();
      ctx.save(); ctx.fillStyle = 'rgba(40,30,15,0.25)'; ctx.fillRect(x - 18, 0, 18, H); ctx.strokeStyle = INK; ctx.lineWidth = Math.max(3, H / 240); ctx.beginPath(); for (let y = 0; y <= H; y += H / 24) ctx.lineTo(x + Math.sin(y * 0.05) * H * 0.004, y); ctx.stroke(); ctx.restore();
    }
    chrome(arch > 0.5 ? 'I' : id0 === 'I' ? 'H' : id0, arch > 0.5);
    return { violations: [] };
  }
  return { canvas: out, frame };
}
