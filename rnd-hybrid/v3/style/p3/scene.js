// R&D vòng 3 · khung phong cách P3: TRANH IN BÁO 1930 (2.5D). Người và nền vẽ kiểu tranh khắc mực (gạch chéo theo độ tối), màu trầm sepia,
// xếp thành các tấm phẳng ở nhiều độ sâu trong 3D (máy lượn tạo thị sai). Không ánh sáng 3D: toàn bộ sắc độ nằm trong nét khắc.
// t = 0.5 → K1 (cận người đàn ông lo âu trước ngân hàng đóng cửa) · t = 1.5 → K2 (toàn cảnh đám đông).
import * as THREE from 'three';
import { drawFigure, crowdSpec, INK } from '/rnd-hybrid/v3/style/figure1930.js';
import { facade, bankFacade, sky, pavement } from '/rnd-hybrid/v3/style/street2d.js';

const STYLE = 'engrave';
function plane(w, h, pxPerM, draw, { shadow = true } = {}) {
  const c = document.createElement('canvas'); c.width = Math.round(w * pxPerM); c.height = Math.round(h * pxPerM); const g = c.getContext('2d');
  g.scale(pxPerM, pxPerM); draw(g, w, h);
  if (shadow) { // bóng in nhẹ dưới mép dưới tấm (cảm giác lớp giấy chồng)
    const s = document.createElement('canvas'); s.width = c.width; s.height = c.height; const sg = s.getContext('2d'); sg.filter = 'blur(6px)'; sg.drawImage(c, 8, 8);
    sg.filter = 'none'; sg.globalCompositeOperation = 'source-in'; sg.fillStyle = 'rgba(40,30,15,0.35)'; sg.fillRect(0, 0, s.width, s.height); sg.globalCompositeOperation = 'source-over'; sg.drawImage(c, 0, 0);
    const t = new THREE.CanvasTexture(s); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return mesh(t, w, h); }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return mesh(t, w, h);
}
function mesh(t, w, h) { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: t, transparent: true, alphaTest: 0.05 })); m.geometry.translate(0, h / 2, 0); return m; }
// hàng người: các hình 1930 đứng cạnh nhau (chủ yếu nhìn lưng về ngân hàng)
function row(spec, w, pxPerM, { front = false } = {}) {
  return plane(w, 2.3, pxPerM, (g) => { const n = spec.length; spec.forEach((o, i) => { g.save(); g.translate(0.6 + (w - 1.2) * (i + 0.5) / n + ((i * 37) % 7 - 3) * 0.04, 2.25);
    const s = o.s * 1.78 / 790; g.scale(s, s); drawFigure(g, { ...o, view: front ? 'front' : o.view, style: STYLE }); g.restore(); }); });
}

export async function boot(res) {
  for (const f of ['700 48px Georgia', '800 48px Georgia', '600 48px Inter']) await document.fonts.load(f);
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true }); renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(); scene.background = new THREE.Color('#E4D8BE'); scene.fog = new THREE.Fog('#E4D8BE', 18, 70);
  const skyP = plane(150, 40, 14, (g, w, h) => sky(g, w * 14, h * 14, { style: STYLE }) || 0, { shadow: false }); skyP.material.map.needsUpdate = true;
  // (sky vẽ ở hệ px: dựng lại cho đúng tỉ lệ)
  { const c = document.createElement('canvas'); c.width = 2100; c.height = 560; sky(c.getContext('2d'), 2100, 560, { style: STYLE }); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; skyP.material.map = t; }
  skyP.position.set(0, 0, -60); scene.add(skyP);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(80, 40), new THREE.MeshBasicMaterial({ map: (() => { const c = document.createElement('canvas'); c.width = 2048; c.height = 1024; pavement(c.getContext('2d'), 2048, 1024, { style: STYLE }); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(5, 2.5); return t; })() }));
  ground.rotation.x = -Math.PI / 2; ground.position.set(0, 0, -6); scene.add(ground);
  const px = (w, h, pxPerM, fn) => plane(w, h, pxPerM, (g) => { g.save(); g.scale(1 / pxPerM, 1 / pxPerM); fn(g, w * pxPerM, h * pxPerM); g.restore(); });
  const SIGNS = [['LUNCH', '#8E3B33', 'shop'], ['HATS', '#3E5A4A', 'shop'], [null, null, 'office'], ['DRUGS', '#7A5A2E', 'shop']];
  for (let i = 0; i < 4; i++) { const left = i < 2, [sign, awn, kind] = SIGNS[i], h = 13 + (i % 2) * 3;
    const f = px(9, h, 110, (g, w, hh) => facade(g, w, hh, { kind, sign, awning: awn, seed: i + 2, style: STYLE, fire: i === 1 || i === 3 }));
    f.position.set(left ? -21.5 + (i % 2) * 9.2 : 12.3 + (i % 2) * 9.2, 0, -20 - (i % 2) * 1.5); scene.add(f); }
  const bank = px(13, 10.7, 150, (g, w, h) => bankFacade(g, w, h, { style: STYLE })); bank.position.set(-0.4, 0, -16.5); scene.add(bank);   // ngân hàng nhỏ lại: người/ngân hàng ≈ 1:6
  // đám đông: 4 hàng nhìn lưng về cửa ngân hàng; vài người quay mặt
  const rows = [[-14.6, 11, 3, 0.0], [-12.6, 10, 5, 0.6], [-10.6, 9, 7, -0.4], [-8.6, 8, 9, 0.3]];
  for (const [z, n, seed, dx] of rows) { const r = row(crowdSpec(n, seed), 16, 150); r.position.set(dx, 0, z); scene.add(r); }
  // tiền cảnh K1: người đàn ông lo âu, chính diện, hai tay vò vành mũ… (tay chắp trước ngực)
  const man = px(1.6, 2.1, 520, (g, w, h) => { g.translate(w / 2, h - 10); const s = h / 830; g.scale(s, s);
    drawFigure(g, { sex: 'm', skin: 'light', coat: 'charcoal', hat: 'fedora', expr: 'worried', pose: { L: 'clasp', R: 'clasp' }, style: STYLE }); });
  man.position.set(1.15, 0, -2.6); scene.add(man);
  const cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 300);
  // vùng kiểm (cổng nén giả YouTube): hộp màn hình của chữ/mặt, chiếu từ toạ độ trên tấm phẳng (u,v: 0..1, v từ trên xuống)
  const roiOf = (m, w, h, u0, v0, u1, v1) => { m.updateMatrixWorld(); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (const [u, v] of [[u0, v0], [u1, v0], [u0, v1], [u1, v1]]) { const p = new THREE.Vector3((u - 0.5) * w, (1 - v) * h, 0).applyMatrix4(m.matrixWorld).project(cam);
      const X = (p.x + 1) / 2 * W, Y = (1 - p.y) / 2 * H; x0 = Math.min(x0, X); y0 = Math.min(y0, Y); x1 = Math.max(x1, X); y1 = Math.max(y1, Y); } return [x0, y0, x1, y1].map(Math.round); };
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  function frame(t) {
    const K1 = t < 1;
    if (K1) { cam.position.set(0.55, 1.68, -0.55); cam.fov = 34; cam.lookAt(0.5, 1.72, -10); man.visible = true; }
    else { cam.position.set(0.8, 2.1, -1.0); cam.fov = 44; cam.lookAt(0.0, 3.2, -16); man.visible = false; }
    cam.updateProjectionMatrix(); cam.updateMatrixWorld(); renderer.render(scene, cam); ctx.drawImage(renderer.domElement, 0, 0);
    window.ROI = { CLOSED: roiOf(bank, 13, 10.7, 0.41, 0.585, 0.59, 0.675), BANK: roiOf(bank, 13, 10.7, 0.36, 0.215, 0.64, 0.28) };
    if (K1) { const fx = (416 - 50) / 832, fy = (161 - 63) / 1092; window.ROI.FACE = roiOf(man, 1.6, 2.1, fx, fy, 1 - fx, (161 + 63) / 1092); }
    // chrome kênh
    const s = W / 1920; ctx.save(); ctx.scale(s, s); const pill = (txt, x, y, px2, fg, bg, right) => { ctx.font = `600 ${px2}px Inter`; const pw = ctx.measureText(txt).width + px2 * 0.9, ph = px2 * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px2 * 0.45, y + ph / 2 + px2 * 0.04); };
    pill('December 1930', 96, 54, 48, '#F2F4F7', 'rgba(23,21,15,0.82)'); pill('ILLUSTRATIVE', 1824, 54, 40, '#17150F', 'rgba(242,236,220,0.92)', true); ctx.restore();
    return { violations: [] };
  }
  return { canvas: out, frame };
}
