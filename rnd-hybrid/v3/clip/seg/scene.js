// R&D vòng 3 · CLIP v3 (H4′) — cùng lời/mốc với v2 (v2/clip/narration.json, đã đối chiếu nguồn gốc ở v2/CLAIMS.md).
// Sửa theo chủ dự án: (a) 8/19 cảnh cận/trung cận nhân vật (A2, C, E, F, H, J, L1, N); (b) cảnh cột trụ ~17,5 s có người gửi tiền ở cửa + Walt tiền cảnh;
// (c) cảnh đêm sáng hơn (đèn bù theo máy, hemi cao, viền tối nhẹ) — độ sáng trung bình ghi ở v3/REPORT.md; (d) thẻ "THE WHOLE LOAN" mang nhãn "BEFORE 1934",
// không xuất hiện lại ở ~35 s (cảnh N chỉ còn bậc trả dần + Walt nhẹ nhõm).
import * as THREE from 'three';
import { Post } from '/rnd-hybrid/v3/lib/post.js';
import { lg } from '/rnd-hybrid/v2/illus2d.js';
import { buildWorld, HX, OX, GX, TX } from '/rnd-hybrid/v3/clip/seg/world4.js';
import { WALT } from '/rnd-hybrid/v3/lib/sets.js';

const SEG = '/rnd-hybrid/v3/clip/seg/';
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const lin = (t, a, b) => clamp((t - a) / (b - a));
const ease = (t, a, b) => { const x = lin(t, a, b); return x * x * (3 - 2 * x); };
const backOut = (t, a, d = 0.35) => { if (t < a) return 0; const x = clamp((t - a) / d), c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const P = (pos, tgt, fov) => ({ pos, tgt, fov });

export async function boot(res) {
  for (const wt of [400, 600, 700, 800]) await document.fonts.load(`${wt} 48px Inter`);
  const TL = await (await fetch(SEG + 'timeline.json')).json(), A = TL.a, SH = Object.fromEntries(TL.shots.map((s) => [s.id, s]));
  const W = Math.round(res * 16 / 9), H = res;
  const renderer = new THREE.WebGLRenderer({ antialias: false, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(), post = Post(renderer, W, H);
  scene.background = new THREE.Color('#3B4556'); scene.fog = new THREE.Fog('#3B4556', 30, 95);
  const hemi = new THREE.HemisphereLight('#C9D6EA', '#3A3026', 1.1), key = new THREE.DirectionalLight('#FFF1DC', 2.4), fill = new THREE.PointLight('#FFF1DE', 0, 16, 1.2);
  key.castShadow = true; key.shadow.mapSize.set(2048, 2048); Object.assign(key.shadow.camera, { left: -12, right: 12, top: 12, bottom: -12, near: 0.5, far: 60 }); key.shadow.bias = -0.0006; key.shadow.normalBias = 0.03;
  scene.add(hemi, key, key.target, fill);
  const Wd = await buildWorld(scene), C = Wd.C, cam = new THREE.PerspectiveCamera(36, W / H, 0.1, 400);
  // hồi ánh sáng: [nền, hemi màu, hemi cường độ, key màu, key cường độ, hướng key, đèn bù]
  const ACT = { calm: ['#8C7A66', '#F3DDBB', 1.15, '#FFD9A0', 2.4, [-8, 12, 6], 2.5], crisis: ['#3B4556', '#B8C8E2', 1.35, '#C9D6EA', 1.7, [-8, 12, 6], 9],
    relief: ['#9FB3C8', '#E9F0FA', 1.2, '#FFF1DC', 2.4, [-6, 12, 8], 3], office: ['#B9A27E', '#FFF1DC', 1.1, '#FFE8C2', 2.0, [-4, 6, 6], 4], today: ['#CFE0F0', '#F4F8FF', 1.2, '#FFF6E6', 2.4, [-6, 12, 8], 2.5] };
  const W0 = [HX - 1.6, 0.16, -5.6], R0 = [HX - 2.6, 0.16, -5.9];
  const face = (o, cpos, tw = 0) => { o.rotation.y = Math.atan2(cpos[0] - o.position.x, cpos[2] - o.position.z) + tw; };
  // máy quay theo cảnh: [từ, đến]
  const CAM = {
    A1: [P([HX + 4, 2.2, 4], [HX - 1, 2.0, -10], 40), P([HX + 2.6, 1.8, 1.4], [HX - 1.6, 1.8, -9], 36)],
    A2: [P([HX - 0.7, 1.62, -3.6], [HX - 1.75, 1.55, -5.6], 32), P([HX - 0.75, 1.62, -3.9], [HX - 1.75, 1.55, -5.6], 30)],          // cận Walt
    B: [P([9, 1.7, -1.2], [1.5, 2.4, -11], 40), P([8, 1.7, -2.2], [1.2, 2.4, -11], 37)],
    C: [P([HX + 2.6, 1.6, -1.2], [HX + 0.2, 1.2, -6.0], 40), P([HX + 2.4, 1.6, -1.6], [HX + 0.2, 1.2, -6.0], 38)],                 // trung cận Walt + lịch
    D: [P([HX + 3.0, 1.0, -0.6], [HX + 0.2, 1.8, -5.6], 44), P([HX + 2.8, 1.0, -1.0], [HX + 0.2, 1.8, -5.6], 42)],
    E: [P([6.6, 1.68, -3.9], [5.2, 1.6, -6.2], 34), P([6.5, 1.66, -4.2], [5.1, 1.6, -6.2], 32)],                                     // cận Walt, cửa đóng sau lưng
    F: [P([HX + 0.9, 1.5, -2.8], [HX - 2.0, 1.4, -5.8], 36), P([HX + 0.7, 1.5, -3.2], [HX - 2.0, 1.4, -5.8], 34)],                   // trung cận Walt + Ruth
    G: [P([16, 2.8, 2.5], [1.2, 3.4, -12.5], 40), P([14.2, 2.0, 0.6], [1.2, 3.2, -12.5], 37)],
    H: [P([5.6, 1.9, -4.6], [0, 2.2, -13.5], 38), P([4.6, 1.95, -6.0], [0, 2.3, -13.8], 34)],                                         // cột trụ + người ở cửa + Walt tiền cảnh
    J: [P([WALT[0] + 0.7, 1.66, WALT[2] + 1.2], [WALT[0] - 0.1, 1.55, WALT[2]], 32), P([WALT[0] + 0.6, 1.66, WALT[2] + 1.05], [WALT[0] - 0.1, 1.55, WALT[2]], 30)], // cận Walt trong đám đông
    K1: [P([13, 1.5, -1], [2, 3.2, -13], 36), P([16, 4.0, 4], [2, 3.4, -13], 38)],
    K2: [P([OX + 1.2, 1.75, 1.6], [OX + 0.5, 1.7, -3.4], 38), P([OX + 0.9, 1.75, 1.2], [OX + 0.5, 1.7, -3.4], 36)],
    L1: [P([OX + 0.75, 1.25, 0.4], [OX + 0.05, 0.95, -1.75], 34), P([OX + 0.6, 1.25, 0.15], [OX + 0.05, 0.95, -1.75], 32)],         // trung cận ký hợp đồng
    L2: [P([HX + 6.0, 2.0, 0.6], [HX + 2.6, 1.5, -5.4], 40), P([HX + 5.6, 1.9, 0.0], [HX + 2.6, 1.5, -5.4], 38)],
    M: [P([GX - 1.0, 2.4, 4.4], [GX - 1.0, 0.8, -1.0], 44), P([GX + 0.6, 2.6, 5.2], [GX + 0.2, 0.8, -1.2], 44)],
    N: [P([GX + 3.6, 1.6, 1.6], [GX + 2.7, 1.45, -0.3], 32), P([GX + 3.5, 1.6, 1.4], [GX + 2.7, 1.45, -0.3], 30)],                   // cận Walt nhẹ nhõm cạnh cột cuối
    O: [P([GX + 1.5, 3.4, 7.5], [GX + 1.0, 0.8, -1.4], 46), P([GX + 2.5, 3.0, 6.8], [GX + 1.4, 0.8, -1.6], 44)],
    P: [P([TX + 0.4, 1.6, -2.4], [TX - 1.0, 1.5, -5.4], 34), P([TX + 2.6, 2.2, 1.8], [TX - 0.6, 2.0, -8.5], 40)],
  };
  CAM.I = [CAM.H[1], CAM.H[1]];
  const ACTOF = { A1: 'calm', A2: 'calm', B: 'calm', C: 'calm', D: 'calm', E: ['calm', 'crisis'], F: 'crisis', G: 'crisis', H: 'crisis', I: 'crisis', J: 'crisis',
    K1: ['crisis', 'relief'], K2: 'office', L1: 'office', L2: 'relief', M: 'relief', N: 'relief', O: ['relief', 'today'], P: 'today' };
  const mix = (a, b, k) => a + (b - a) * k, col = (a, b, k) => new THREE.Color(a).lerp(new THREE.Color(b), k);
  function light(id, t, sh, tgt) {
    const a = [].concat(ACTOF[id]), A0 = ACT[a[0]], A1 = ACT[a[1] || a[0]], k = a.length > 1 ? (id === 'E' ? ease(t, A.noloan - 0.2, A.noloan + 0.6) : ease(t, sh.t0, sh.t1)) : 0;
    scene.background.copy(col(A0[0], A1[0], k)); scene.fog.color.copy(scene.background); hemi.color.copy(col(A0[1], A1[1], k)); hemi.intensity = mix(A0[2], A1[2], k);
    key.color.copy(col(A0[3], A1[3], k)); key.intensity = mix(A0[4], A1[4], k); key.position.set(tgt[0] + A0[5][0], A0[5][1], tgt[2] + A0[5][2]); key.target.position.set(tgt[0], 0, tgt[2]); key.target.updateMatrixWorld();
    fill.intensity = mix(A0[6], A1[6], k);
  }
  const hideAll = () => { for (const c of Object.values(C)) c.visible = false; Wd.cal.forEach((c) => (c.visible = false)); Wd.val.forEach((m) => (m.visible = false));
    Wd.g20.forEach((c) => (c.visible = false)); Wd.g30.forEach((c) => (c.visible = false)); for (const p of [Wd.walt, Wd.waltBare, Wd.ruth, Wd.sam]) p.root.visible = false; };
  const show = (p, x, y, z, rotY, clip, ct, expr) => { p.root.visible = true; p.root.position.set(x, y, z); p.root.rotation.y = rotY; p.pose(clip, ct); if (expr) p.face(expr); };
  const place = (o, x, y, z, s, cpos, tw = 0.15) => { o.visible = s > 0.001; o.position.set(x, y, z); o.scale.setScalar(Math.max(0.001, s)); face(o, cpos, tw); };
  const doors = (x) => Wd.doors.forEach(({ piv, sgn }) => { piv.rotation.y = sgn * (1 - x) * 1.4; });
  const toCam = (x, z, cp, tw = 0) => Math.atan2(cp[0] - x, cp[2] - z) + tw;
  function stage(id, t, sh, cp) {
    const lt = t - sh.t0; doors(1); Wd.closed.visible = false;
    for (const c of Wd.crowd) c.p.pose(c.clip, t + c.off);
    switch (id) {
      case 'A1': case 'A2': show(Wd.walt, ...W0, toCam(W0[0], W0[2], cp, 0.2), 'Idle_Talking_Loop', t, 'happy');
        show(Wd.ruth, ...R0, toCam(R0[0], R0[2], cp, 0.35), 'Idle_Loop', t + 0.7, 'happy'); break;
      case 'B': { doors(0); const k = ease(t, sh.t0, A.half + 0.2), x = mix(8.5, 5.2, k), z = mix(-5.2, -8.2, k);
        show(Wd.walt, x, 0.16, z, Math.atan2(-3.3, -3.0), k < 0.98 ? 'Walk_Formal_Loop' : 'Idle_Loop', t, t > A.half ? 'neutral' : 'happy');
        place(C.half, 3.0, 1.4, -8.6, backOut(t, A.half), cp); break; }
      case 'C': show(Wd.walt, HX - 0.9, 0.16, -5.4, toCam(HX - 0.9, -5.4, cp, 0.2), 'Idle_Talking_Loop', t, 'neutral');
        Wd.cal.forEach((c, i) => place(c, HX + 0.1 + i * 0.7, 0.75, -5.6, backOut(t, i < 3 ? A.three + i * 0.12 : A.five + (i - 3) * 0.12), cp));
        place(C.years, HX + 1.5, 1.85, -6.6, backOut(t, A.five + 0.3), cp); break;
      case 'D': { show(Wd.walt, ...W0, toCam(W0[0], W0[2], cp, 0.3), t > A.whole + 0.25 ? 'Hit_Chest' : 'Idle_Loop', t > A.whole + 0.25 ? clamp(t - A.whole - 0.25, 0, 0.6) : t, t > A.whole + 0.25 ? 'shocked' : 'neutral');
        const f = ease(t, A.whole - 0.1, A.once + 0.1); place(C.due, HX + 0.9, 0.16 + (1 - f) * 7, -5.4, 1, cp, 0.1 - (1 - f) * 0.8); C.due.rotation.z = (1 - f) * 0.5; break; }
      case 'E': doors(ease(t, A.noloan, A.noloan + 0.8)); Wd.closed.visible = t > A.noloan + 0.6; show(Wd.walt, 5.2, 0.16, -6.2, toCam(5.2, -6.2, cp, 0.2), 'Idle_Talking_Loop', t, 'worried'); break;
      case 'F': show(Wd.walt, ...W0, toCam(W0[0], W0[2], cp, 0.2), 'Idle_Talking_Loop', t + 1.3, 'sad'); show(Wd.ruth, ...R0, toCam(R0[0], R0[2], cp, 0.3), 'Idle_Talking_Loop', t, 'worried'); break;
      case 'G': Wd.closed.visible = true; break;
      case 'H': Wd.closed.visible = true; Wd.closed.scale.setScalar(Math.max(0.001, backOut(t, A.closed, 0.3)));
        show(Wd.walt, 3.2, 0.16, -8.0, Math.atan2(-3.2, -5.6), 'Idle_Loop', t, 'worried'); break;   // Walt nhìn về cửa (tiền cảnh); đám đông ở bậc thềm
      case 'I': case 'J': Wd.closed.visible = true; Wd.closed.scale.setScalar(1); show(Wd.walt, WALT[0], WALT[1], WALT[2], toCam(WALT[0], WALT[2], cp, 0.25), 'Idle_Talking_Loop', t, 'worried'); break;
      case 'K1': Wd.closed.visible = true; break;
      case 'K2': place(C.fha, OX + 0.5, 2.0, -3.3, backOut(t, A.fha), cp, 0); W_sit(t, 'happy'); break;
      case 'L1': W_sit(t, 'happy'); place(C.insured, OX - 0.55, 1.55, -1.3, backOut(t, A.insured + 0.1), cp); break;
      case 'L2': show(Wd.walt, ...W0, toCam(W0[0], W0[2], cp, 0.2), 'Idle_Talking_Loop', t, 'happy');
        Wd.val.forEach((m, i) => { m.visible = true; m.material = m.material.clone(); m.material.color.set(t > A.eighty + i * 0.05 && i < 8 ? '#4C8DFF' : '#EDE4CF'); face(m, cp, 0); });
        place(C.eighty, HX + 3.8, 2.0, -5.8, backOut(t, A.eighty + 0.2), cp); break;
      case 'M': case 'N': case 'O': { const n20 = id === 'M' ? Math.floor(clamp(lin(t, A.paid, A.twenty + 0.2)) * 20) + 1 : 20;
        Wd.g20.forEach((c, i) => (c.visible = i < n20)); if (id !== 'N') place(C.twenty, GX - 1.6, 1.5, -0.4, id === 'M' ? backOut(t, A.twenty) : 1, cp, 0);
        if (id === 'O') { const n30 = Math.floor(clamp(lin(t, A.y1954, A.thirty + 0.4)) * 30) + 1; Wd.g30.forEach((c, i) => (c.visible = i < n30)); place(C.thirty, GX + 2.4, 1.75, -2.0, backOut(t, A.y1954), cp, 0); }
        if (id === 'N') show(Wd.walt, GX + 2.6, 0.1, 0.4, toCam(GX + 2.6, 0.4, cp, 0.2), 'Idle_Talking_Loop', t, t > A.bill ? 'relieved' : 'happy');
        if (id === 'M') show(Wd.walt, GX + 3.2, 0.1, 1.6, toCam(GX + 3.2, 1.6, cp, 0.4), 'Idle_Talking_Loop', t, 'happy'); break; }
      case 'P': show(Wd.sam, TX - 1.2, 0.16, -5.4, toCam(TX - 1.2, -5.4, cp, 0.3), 'Idle_Talking_Loop', t, 'happy'); break;
    }
  }
  function W_sit(t, expr) { show(Wd.waltBare, OX, 0.1, -1.95, 0, 'Sitting_Idle_Loop', 1.0 + (t % 3), expr); Wd.waltBare.pose('Sitting_Idle_Loop', 1.0 + (t % 3), { arm: 'Interact' }); Wd.clerk.pose('Idle_Talking_Loop', t); }

  // ---- ảnh tư liệu C toàn khung (≤ 6 s, hoà về A) — như v2
  const im = new Image(); im.src = '/rnd-hybrid/work/external/bank1931_crop.jpg'; await im.decode();
  const tone = new OffscreenCanvas(W, H), tg = tone.getContext('2d'); tg.filter = 'contrast(1.12)'; tg.drawImage(im, 0, 0, W, H); tg.filter = 'none';
  { const d = tg.getImageData(0, 0, W, H), lc = new OffscreenCanvas(256, 1), lx = lc.getContext('2d');
    lx.fillStyle = lg(lx, 0, 0, 256, 0, [[0, '#0E1116'], [0.45, '#4A5160'], [0.8, '#B9B3A4'], [1, '#EDE4CF']]); lx.fillRect(0, 0, 256, 1); const Lu = lx.getImageData(0, 0, 256, 1).data;
    for (let i = 0; i < d.data.length; i += 4) { const v = (d.data[i] * 0.299 + d.data[i + 1] * 0.587 + d.data[i + 2] * 0.114) | 0; d.data[i] = Lu[v * 4]; d.data[i + 1] = Lu[v * 4 + 1]; d.data[i + 2] = Lu[v * 4 + 2]; }
    tg.putImageData(d, 0, 0); }
  const out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  const YEAR = { A1: '1930', A2: '1930', B: '1930', C: '1930', D: '1930', E: '1930', F: '1930', G: 'December 1930', H: 'December 1930', I: '1931', J: '1931',
    K1: '1934', K2: '1934', L1: '1934', L2: '1934', M: '1934', N: '1934', O: '1954', P: 'Today' };
  const SRC = { B: 'Source: HUD, FHA history', C: 'Source: HUD, FHA history', D: 'Source: HUD, FHA history', G: 'Source: Federal Reserve History', H: 'Source: Federal Reserve History',
    I: 'Photo: Library of Congress (NYWT&S), 1931', K2: 'Source: HUD, FHA history', L2: 'Source: National Housing Act of 1934, §203', M: 'Source: National Housing Act of 1934, §203',
    O: 'Source: Federal Reserve Bank of St. Louis Review, Nov. 1955' };
  function overlay(id, archival) { const s = W / 1920; ctx.save(); ctx.scale(s, s);
    const pill = (txt, x, y, px, fg, bg, right) => { ctx.font = `600 ${px}px Inter`; const pw = ctx.measureText(txt).width + px * 0.9, ph = px * 1.45, x0 = right ? x - pw : x;
      ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(x0, y, pw, ph, ph / 2); ctx.fill(); ctx.fillStyle = fg; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(txt, x0 + px * 0.45, y + ph / 2 + px * 0.04); };
    pill(YEAR[id], 96, 54, 48, '#F2F4F7', 'rgba(14,17,22,0.72)'); if (!archival) pill('ILLUSTRATIVE', 1824, 54, 40, '#0E1116', 'rgba(242,244,247,0.88)', true);
    const src = SRC[id]; if (src) { ctx.font = '400 40px Inter'; ctx.textAlign = 'right'; ctx.textBaseline = 'alphabetic'; ctx.fillStyle = 'rgba(14,17,22,0.75)'; ctx.fillText(src, 1826, 1018); ctx.fillStyle = 'rgba(242,244,247,0.94)'; ctx.fillText(src, 1824, 1016); }
    ctx.restore(); }
  function photo(t, a) { const k = lin(t, TL.archival.in, TL.archival.out), z = 1.02 + 0.07 * k, w = W * z, h = H * z;
    ctx.save(); ctx.globalAlpha = a; ctx.drawImage(tone, (W - w) / 2 - W * 0.02 * k, (H - h) / 2 - H * 0.015 * k, w, h); ctx.restore(); }
  const shotAt = (t) => TL.shots.find((s) => t >= s.t0 && t < s.t1) || TL.shots[TL.shots.length - 1];
  function frame(t) {
    const sh0 = shotAt(t), id0 = sh0.id, sh = id0 === 'I' ? SH.H : sh0, id = id0 === 'I' ? 'H' : id0, k = id0 === 'I' ? 1 : ease(t, sh.t0, sh.t1);
    const ai = TL.archival.in, ao = TL.archival.out, arch = t >= ai && t < ao ? Math.min(ease(t, ai, ai + 0.7), 1 - ease(t, ao - 0.8, ao)) : 0;
    if (!(id0 === 'I' && arch > 0.999)) {
      const [c0, c1] = CAM[id], p = { pos: c0.pos.map((v, i) => mix(v, c1.pos[i], k)), tgt: c0.tgt.map((v, i) => mix(v, c1.tgt[i], k)), fov: mix(c0.fov, c1.fov, k) };
      cam.position.set(...p.pos); cam.fov = p.fov; cam.lookAt(...p.tgt); cam.updateProjectionMatrix(); cam.updateMatrixWorld();
      fill.position.set(p.pos[0] + 0.4, p.pos[1] + 1.0, p.pos[2] + 0.4);
      light(id, t, sh, p.tgt); hideAll(); stage(id, id0 === 'I' ? SH.H.t1 - 0.01 : t, sh, p.pos);
      post.render(scene, cam); ctx.drawImage(renderer.domElement, 0, 0);
    } else { ctx.fillStyle = '#0E1116'; ctx.fillRect(0, 0, W, H); }
    if (arch > 0) photo(t, arch);
    overlay(arch > 0.5 ? 'I' : id, arch > 0.5);
    return { violations: [] };
  }
  return { canvas: out, frame };
}
