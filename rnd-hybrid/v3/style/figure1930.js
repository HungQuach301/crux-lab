// R&D vòng 3 · khung phong cách: NGƯỜI LỚN 1930 vẽ bằng mã (không mô hình tải về). Tỉ lệ ~7,5 đầu; áo khoác dài tới gối, mũ phớt;
// nữ: váy dài tới mắt cá + áo khoác lửng + mũ chuông (cloche). Mặt trước có mắt/lông mày/miệng theo cảm xúc; mặt lưng không có mặt.
// Hai kiểu nét: 'paper' (mảng màu phẳng + viền mực + bán sắc nhẹ, cho P1) và 'engrave' (tranh khắc báo 1930: gạch chéo theo độ tối, màu trầm, cho P3).
// Tách lớp: o.only ⊂ ['backArm','backLeg','body','head','frontArm'] (P1 giấy nhiều lớp). Gốc = giữa hai bàn chân, trục y lên là âm. Cao ≈ 760 px.
import { hash } from '/rnd-hybrid/cutout/rig.js';

export const INK = '#17150F';
// mật độ gạch (tranh khắc): hệ số dãn khoảng cách nét; 1,67 = giảm ~40 % số nét so với bản khung phong cách đầu (chủ dự án 14/10)
export const HATCH = { spacing: 1.67 };
const SK = { light: '#E8C4A2', medium: '#C99470', tan: '#A9744F', dark: '#74482F', deep: '#4E3022' };
export const COATS = { charcoal: '#3F434A', brown: '#6B5442', navy: '#323C52', grey: '#6F737A', tweed: '#7A6A52', camel: '#9A7B55', plum: '#6A5470', green: '#4E6656' };

function rgbOf(c) { if (c[0] === '#') { const n = parseInt(c.slice(1), 16); return [n >> 16, (n >> 8) & 255, n & 255]; } return c.match(/\d+/g).slice(0, 3).map(Number); }
const hexOf = (a) => '#' + a.map((v) => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, '0')).join('');
function shade(c, k) { return hexOf(rgbOf(c).map((v) => v * k)); }
// tranh khắc báo: kéo màu về giấy báo sepia (màu trầm), giữ độ sáng tương đối
function sepia(c, k = 0.55) { const a = rgbOf(c), L = (a[0] * 0.3 + a[1] * 0.59 + a[2] * 0.11) / 255, s = [236, 222, 192].map((v) => v * (0.35 + 0.75 * L)); return hexOf(a.map((v, i) => v + (s[i] - v) * k)); }

// gạch chéo (tranh khắc): các đường song song trong vùng clip, mật độ theo độ tối d ∈ [0,1]; d > 0,55 thêm lớp chéo thứ hai
function hatch(g, box, d, ang = 0.75, gap = 7, lw = 1.3, color = INK) {
  if (d <= 0.02) return; const [x0, y0, x1, y1] = box, cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, R = Math.hypot(x1 - x0, y1 - y0) / 2 + 4;
  const pass = (a, sp) => { g.beginPath(); const ca = Math.cos(a), sa = Math.sin(a); for (let s = -R; s <= R; s += sp) { g.moveTo(cx + ca * -R - sa * s, cy + sa * -R + ca * s); g.lineTo(cx + ca * R - sa * s, cy + sa * R + ca * s); } g.stroke(); };
  g.save(); g.strokeStyle = color; g.lineWidth = lw * (0.5 + d); g.globalAlpha = Math.min(1, 0.35 + d); pass(ang, gap * HATCH.spacing / Math.max(0.25, d));
  if (d > 0.55) pass(ang + 1.3, gap * HATCH.spacing * 1.4 / (d - 0.4)); g.restore();
}
// một mảng: tô + (khắc: gạch theo độ tối) + viền
function part(g, path, fill, st, { dark = 0.3, box = null, lw = null } = {}) {
  g.save(); g.fillStyle = st.style === 'engrave' ? sepia(fill) : fill; g.fill(path);
  if (st.style === 'engrave' && box) { g.save(); g.clip(path); hatch(g, box, dark, st.hatchAng ?? 0.78, 6.5); g.restore(); }
  if (st.style === 'paper' && box && dark > 0.35) { g.save(); g.clip(path); g.globalAlpha = 0.18; g.fillStyle = '#000'; const [x0, y0, x1, y1] = box; g.fillRect(x0 + (x1 - x0) * 0.6, y0, (x1 - x0) * 0.4, y1 - y0); g.restore(); }
  g.lineJoin = 'round'; g.lineCap = 'round'; g.strokeStyle = INK; g.lineWidth = lw ?? (st.style === 'engrave' ? 2.6 : 4.2); g.stroke(path); g.restore();
}
const P = (d) => new Path2D(d);
const ell = (x, y, rx, ry) => `M${x - rx},${y} a${rx},${ry} 0 1,0 ${2 * rx},0 a${rx},${ry} 0 1,0 ${-2 * rx},0 Z`;

// tay: vai (sx,sy) → khuỷu → cổ tay theo tư thế; trả về path ống tay + vị trí bàn tay
function armPath(side, pose, fem) {
  const s = side, sx = s * (fem ? 74 : 92), sy = -612;
  const P0 = { down: [[s * 104, -470], [s * 106, -335]], clasp: [[s * 92, -470], [s * 26, -392]], chin: [[s * 70, -505], [s * 24, -646]], hat: [[s * 96, -470], [s * 30, -420]], point: [[s * 160, -560], [s * 245, -590]], pocket: [[s * 104, -470], [s * 82, -390]] }[pose] || [[s * 104, -470], [s * 106, -335]];
  const [[ex, ey], [wx, wy]] = P0, w = fem ? 15 : 18;
  const seg = (ax, ay, bx, by, ww) => { const dx = bx - ax, dy = by - ay, L = Math.hypot(dx, dy) || 1, nx = -dy / L * ww, ny = dx / L * ww; return [ax + nx, ay + ny, bx + nx, by + ny, bx - nx, by - ny, ax - nx, ay - ny]; };
  const a = seg(sx, sy, ex, ey, w + 3), b = seg(ex, ey, wx, wy, w);
  const d = `M${a[0]},${a[1]} L${a[2]},${a[3]} L${b[2]},${b[3]} L${b[4]},${b[5]} L${a[4]},${a[5]} L${a[6]},${a[7]} Z`;
  return { d, hand: [wx, wy], box: [Math.min(sx, ex, wx) - 22, sy - 10, Math.max(sx, ex, wx) + 22, Math.max(ey, wy) + 10] };
}

// mặt trước theo cảm xúc (đầu tâm (0,-700), rx 38, ry 48)
function face(g, expr, st) {
  const E = { neutral: [0, 0, 0], worried: [1, 0.2, -0.6], anxious: [1.2, 0.6, -0.2], sad: [0.8, 0, -1], relieved: [-0.4, 0, 1], happy: [-0.3, 0, 1] }[expr] || [0, 0, 0];
  const [brow, wide, mouth] = E; g.save(); g.strokeStyle = INK; g.fillStyle = INK; g.lineCap = 'round';
  for (const s of [-1, 1]) { g.beginPath(); g.ellipse(s * 15, -705, 4.2 + wide * 1.6, 5.2 + wide * 2.2, 0, 0, 7); g.fill();     // mắt
    g.lineWidth = 4; g.beginPath(); g.moveTo(s * 26, -722 + brow * 2); g.lineTo(s * 7, -722 - brow * 7); g.stroke(); }          // lông mày (đầu trong nhướng lên = lo)
  g.lineWidth = 2.6; g.beginPath(); g.moveTo(1, -702); g.lineTo(-3, -686); g.lineTo(3, -684); g.stroke();                        // mũi
  g.lineWidth = 3.6; g.beginPath(); if (mouth < -0.8) { g.moveTo(-11, -664); g.quadraticCurveTo(0, -672, 11, -664); } else if (mouth > 0.5) { g.moveTo(-12, -670); g.quadraticCurveTo(0, -660, 12, -670); }
  else { g.moveTo(-10, -667); g.bezierCurveTo(-4, -671, 4, -663, 10, -668); } g.stroke();
  // mặt: không gạch (đọc được trên điện thoại)
  g.restore();
}

// người: o = { sex:'m'|'f', skin, coat, hat:'fedora'|'cloche'|'none', view:'front'|'back', pose:{L,R}, expr, style, only, seed }
export function drawFigure(g, o) {
  const st = { style: o.style || 'paper', hatchAng: o.hatchAng }, fem = o.sex === 'f', skin = SK[o.skin || 'light'], coat = COATS[o.coat || 'charcoal'] || o.coat,
    hairC = o.hair || '#2A211B', front = (o.view || 'front') === 'front', only = o.only ? new Set(o.only) : null, has = (k) => !only || only.has(k);
  const poseL = (o.pose && o.pose.L) || 'down', poseR = (o.pose && o.pose.R) || 'down';
  const trousers = shade(coat, 0.7), shoes = '#211A15';
  // ---- lớp chân sau / chân trước (nam: quần + giày; nữ: cổ chân + giày dưới váy)
  const leg = (s) => { const x = s * 24; return fem ? `M${x - 9},-60 L${x + 9},-60 L${x + 8},-14 L${x - 8},-14 Z` : `M${x - 21},-250 L${x + 21},-250 L${x + 19},-16 L${x - 19},-16 Z`; };
  const shoe = (s) => ell(s * 24 + (front ? 0 : 0), -10, fem ? 15 : 22, 10);
  if (has('backLeg')) { part(g, P(leg(-1)), fem ? skin : trousers, st, { dark: 0.55, box: [-50, -250, 0, -14] }); part(g, P(shoe(-1)), shoes, st, { dark: 0.8, box: [-50, -24, 4, 2] }); }
  // ---- tay sau
  const back = front ? -1 : 1;   // tay "sau" là tay trái khi nhìn trước
  const drawArm = (side, pose) => { const A = armPath(side, pose, fem); part(g, P(A.d), coat, st, { dark: 0.5, box: A.box });
    part(g, P(ell(A.hand[0], A.hand[1] + 6, fem ? 12 : 15, fem ? 13 : 16)), skin, st, { dark: 0, box: [A.hand[0] - 16, A.hand[1] - 12, A.hand[0] + 16, A.hand[1] + 24] });
    const cuff = new Path2D(); cuff.moveTo(A.hand[0] - 16, A.hand[1] - 8); cuff.lineTo(A.hand[0] + 16, A.hand[1] - 8); g.save(); g.strokeStyle = INK; g.lineWidth = 3; g.stroke(cuff); g.restore(); };
  if (has('backArm')) drawArm(back, front ? poseL : poseR);
  // ---- thân: áo khoác (nam: dài tới gối, hai hàng cúc, ve áo; nữ: váy dài + áo khoác lửng)
  if (has('body')) {
    if (has('backLeg')) {} // (đã vẽ)
    part(g, P(leg(1)), fem ? skin : trousers, st, { dark: 0.45, box: [0, -250, 50, -14] }); part(g, P(shoe(1)), shoes, st, { dark: 0.8, box: [0, -24, 50, 2] });
    if (fem) { const dress = shade(coat, 0.85);
      part(g, P(`M-62,-470 C-70,-330 -96,-160 -104,-58 L104,-58 C96,-160 70,-330 62,-470 Z`), dress, st, { dark: 0.4, box: [-106, -470, 106, -56] });
      for (const x of [-40, 0, 40]) { g.save(); g.strokeStyle = INK; g.globalAlpha = 0.55; g.lineWidth = 2.4; g.beginPath(); g.moveTo(x * 0.6, -420); g.quadraticCurveTo(x * 0.9, -240, x * 1.3, -62); g.stroke(); g.restore(); }   // nếp váy
      part(g, P(`M-74,-618 Q0,-640 74,-618 L84,-470 Q86,-410 70,-370 L-70,-370 Q-86,-410 -84,-470 Z`), coat, st, { dark: 0.45, box: [-86, -640, 86, -368] });
      if (front) { part(g, P(`M-24,-628 L24,-628 L0,-560 Z`), '#E9E1CC', st, { dark: 0.05, box: [-24, -628, 24, -560] }); g.save(); g.fillStyle = INK; for (const y of [-520, -470, -420]) { g.beginPath(); g.arc(0, y, 4.5, 0, 7); g.fill(); } g.restore(); }
    } else {
      part(g, P(`M-94,-622 Q0,-646 94,-622 L104,-470 L102,-330 Q110,-262 116,-232 L-116,-232 Q-110,-262 -102,-330 L-104,-470 Z`), coat, st, { dark: 0.45, box: [-118, -646, 118, -230] });
      if (front) { part(g, P(`M-26,-632 L26,-632 L0,-520 Z`), '#E9E1CC', st, { dark: 0.05, box: [-26, -632, 26, -520] });
        part(g, P(`M-6,-626 L6,-626 L9,-548 L0,-532 L-9,-548 Z`), o.tie || '#7A3B33', st, { dark: 0.4, box: [-10, -626, 10, -532] });
        g.save(); g.strokeStyle = INK; g.lineWidth = 3.6; g.beginPath(); g.moveTo(-30, -634); g.lineTo(-4, -500); g.lineTo(-48, -560); g.moveTo(30, -634); g.lineTo(4, -500); g.lineTo(48, -560); g.stroke();   // ve áo
        g.fillStyle = INK; for (const y of [-470, -410, -350]) for (const x of [-22, 22]) { g.beginPath(); g.arc(x, y, 4.5, 0, 7); g.fill(); }
        g.lineWidth = 2.4; g.beginPath(); g.moveTo(-70, -420); g.lineTo(-40, -420); g.moveTo(40, -420); g.lineTo(70, -420); g.stroke(); g.restore(); }   // nắp túi
      else { g.save(); g.strokeStyle = INK; g.lineWidth = 3; g.beginPath(); g.moveTo(0, -600); g.lineTo(0, -300); g.lineTo(0, -232); g.moveTo(-60, -400); g.lineTo(60, -400); g.stroke(); g.restore(); }   // đường may lưng + đai
    }
  }
  // ---- đầu: cổ, tai, tóc, mặt, mũ
  if (has('head')) {
    part(g, P(`M-15,-655 L15,-655 L17,-618 L-17,-618 Z`), skin, st, { dark: 0.15, box: [-17, -655, 17, -618] });
    if (front) { for (const s of [-1, 1]) part(g, P(ell(s * 38, -700, 7, 11)), skin, st, { dark: 0, box: [s * 38 - 8, -712, s * 38 + 8, -688] }); }
    part(g, P(ell(0, -700, 38, 48)), skin, st, { dark: front ? 0.0 : 0.3, box: [-38, -748, 38, -652] });
    if (front) { // tóc dưới vành mũ
      if (fem) { part(g, P(`M-40,-716 Q-46,-670 -32,-660 L-30,-700 Z M40,-716 Q46,-670 32,-660 L30,-700 Z`), hairC, st, { dark: 0.7, box: [-46, -720, 46, -660] }); }
      else part(g, P(`M-38,-722 Q-40,-706 -36,-694 L-34,-722 Z M38,-722 Q40,-706 36,-694 L34,-722 Z`), hairC, st, { dark: 0.7, box: [-40, -724, 40, -690] });
      face(g, o.expr || 'neutral', st);
    } else part(g, P(fem ? `M-38,-712 Q0,-760 38,-712 Q44,-670 30,-656 Q0,-650 -30,-656 Q-44,-670 -38,-712 Z` : `M-38,-716 Q0,-756 38,-716 Q40,-694 34,-680 Q0,-672 -34,-680 Q-40,-694 -38,-716 Z`), hairC, st, { dark: 0.7, box: [-44, -760, 44, -650] });
    const hat = o.hat || (fem ? 'cloche' : 'fedora'), hc = o.hatColor || shade(coat, 0.75);
    if (hat === 'fedora') { part(g, P(`M-70,-728 Q0,-746 70,-728 Q72,-718 60,-716 Q0,-730 -60,-716 Q-72,-718 -70,-728 Z`), hc, st, { dark: 0.7, box: [-72, -748, 72, -714] });
      part(g, P(`M-40,-734 C-44,-770 -34,-790 -14,-792 Q0,-782 14,-792 C34,-790 44,-770 40,-734 Z`), hc, st, { dark: 0.6, box: [-44, -794, 44, -732] });
      part(g, P(`M-41,-748 L41,-748 L40,-736 L-40,-736 Z`), INK, st, { dark: 0.9, box: [-42, -750, 42, -734], lw: 2 }); }
    else if (hat === 'cloche') { part(g, P(`M-48,-704 C-52,-770 -26,-790 0,-790 C26,-790 52,-770 48,-704 Q30,-722 0,-724 Q-30,-722 -48,-704 Z`), hc, st, { dark: 0.55, box: [-52, -792, 52, -700] });
      g.save(); g.strokeStyle = INK; g.lineWidth = 3; g.beginPath(); g.moveTo(-46, -730); g.quadraticCurveTo(0, -744, 46, -730); g.stroke(); g.restore(); }
  }
  if (has('frontArm')) drawArm(-back, front ? poseR : poseL);
}

// nhóm hàng người (đám đông) — tất định theo seed
export function crowdSpec(n, seed = 1) {
  const coats = Object.keys(COATS), skins = Object.keys(SK), out = [];
  for (let i = 0; i < n; i++) { const r = (k) => hash(seed * 977 + i * 31 + k), fem = r(1) < 0.38;
    out.push({ sex: fem ? 'f' : 'm', skin: skins[Math.floor(r(2) * skins.length)], coat: fem ? ['plum', 'green', 'navy', 'brown'][Math.floor(r(3) * 4)] : coats[Math.floor(r(3) * 6)],
      hat: fem ? 'cloche' : 'fedora', hair: ['#2A211B', '#4A3222', '#1A1612', '#6B4A2E', '#7A7470'][Math.floor(r(4) * 5)], view: r(5) < 0.85 ? 'back' : 'front',
      expr: ['worried', 'sad', 'anxious', 'worried'][Math.floor(r(6) * 4)], pose: { L: r(7) < 0.3 ? 'pocket' : 'down', R: r(8) < 0.25 ? 'hat' : 'down' }, s: 0.92 + r(9) * 0.14 }); }
  return out;
}
