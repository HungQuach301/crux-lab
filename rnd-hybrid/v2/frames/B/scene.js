// R&D hình lai vòng 2 · KHUNG B "minh hoạ 2D giàu": cùng khoảnh khắc 1931 — nét mực, chuyển màu, vân giấy, bán sắc, nền vẽ chi tiết, mưa.
// Canvas 2D thuần (không three), cắm vào render_shots.js của nhà máy như một đoạn (scene.js + spine.json).
import { CHARACTERS, POSES, blendPose, hash } from '/rnd-hybrid/cutout/rig.js';
import { caption, vignette, paperGrain, ACT } from '/rnd-hybrid/v2/paper3d.js';
import { INK, lg, halftone, block, inkChar, inkProp, rain } from '/rnd-hybrid/v2/illus2d.js';

function variant(id, base, top, extras) { const b = CHARACTERS[base], rig = JSON.parse(JSON.stringify(b.rig));
  for (const k of ['torso', 'uaL', 'uaR', 'faL', 'faR']) rig[k].fill = top; CHARACTERS[id] = { ...b, rig, extras: extras || b.extras }; }
variant('q1', 'walt', '#4B5262', ['collar', 'tie', 'fedora']); variant('q2', 'ruth', '#8A6F5A'); variant('q3', 'walt', '#6B5E52', ['collar', 'vest', 'fedora']);
variant('q4', 'walt', '#3E4A5C', ['collar', 'fedora']); variant('q5', 'ruth', '#5E6E86');

export async function boot(res) {
  for (const w of [400, 600, 700]) await document.fonts.load(`${w} 48px Inter`);
  const W = Math.round(res * 16 / 9), H = res, out = document.createElement('canvas'); out.width = W; out.height = H;
  const ctx = out.getContext('2d'), A = ACT.crisis1931;
  function paint() {
    ctx.save(); ctx.scale(W / 1920, H / 1080);
    // ---- trời + mây bán sắc
    ctx.fillStyle = lg(ctx, 0, 0, 0, 700, [[0, A.sky[0]], [0.7, A.sky[1]], [1, '#5E6472']]); ctx.fillRect(0, 0, 1920, 1080);
    halftone(ctx, 0, 0, 1920, 520, (x, y) => 0.55 * Math.max(0, Math.sin(x / 230 + 1.3) * 0.5 + 0.5) * (1 - y / 520), { step: 12, color: '#0B0E14', alpha: 0.35 });
    // ---- lớp xa: đường chân trời (bán sắc + nét mảnh)
    for (let i = 0; i < 18; i++) { const x = i * 112 - 20, w = 96 + 30 * hash(i + 2), h = 220 + 230 * hash(i * 5 + 1), y = 640 - h;
      ctx.fillStyle = lg(ctx, 0, y, 0, 640, [[0, '#3A4150'], [1, '#2B313D']]); ctx.fillRect(x, y, w, h);
      ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip(); halftone(ctx, x, y, w, h, (px) => 0.15 + 0.5 * (px - x) / w, { step: 7, color: '#1A1F29', alpha: 0.5 }); ctx.restore();
      ctx.strokeStyle = 'rgba(21,23,28,0.7)'; ctx.lineWidth = 2; ctx.strokeRect(x, y, w, h);
      for (let r = 0; r < Math.floor(h / 34); r++) for (let c = 0; c < 3; c++) if (hash(i * 97 + r * 7 + c) < 0.16) { ctx.fillStyle = 'rgba(246,213,142,0.75)'; ctx.fillRect(x + 14 + c * 28, y + 16 + r * 34, 12, 16); } }
    ctx.fillStyle = 'rgba(38,44,55,0.45)'; ctx.fillRect(0, 380, 1920, 300);   // sương giữa lớp xa và lớp giữa
    // ---- lớp giữa trái: dãy nhà gạch, phào, cửa sổ sáng/tối, ống thoát hiểm
    const bld = [[-30, 230, 250, '#6E5A4C'], [220, 300, 210, '#7D6656'], [430, 260, 160, '#5F5148']];
    for (const [x, y, w, col] of bld) {
      block(ctx, x, y, w, 820 - y, col, '#3A302A');
      ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, 820 - y); ctx.clip();
      for (let r = 0; r < 40; r++) { ctx.strokeStyle = 'rgba(21,23,28,0.18)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(x, y + r * 14); ctx.lineTo(x + w, y + r * 14); ctx.stroke(); }   // gạch
      halftone(ctx, x, y, w, 820 - y, (px) => (px - x) / w * 0.9, { step: 8, alpha: 0.4 }); ctx.restore();
      ctx.fillStyle = '#4A3E36'; ctx.fillRect(x - 8, y - 18, w + 16, 22); ctx.strokeStyle = INK; ctx.lineWidth = 3; ctx.strokeRect(x - 8, y - 18, w + 16, 22);
      const cols = Math.floor(w / 62); for (let r = 0; (r + 1) * 92 < 820 - y - 60; r++) for (let c = 0; c < cols; c++) {
        const wx = x + 22 + c * (w - 30) / cols, wy = y + 40 + r * 92, lit = hash(x * 3 + r * 11 + c) < 0.3;
        if (lit) { const gl = ctx.createRadialGradient(wx + 16, wy + 26, 4, wx + 16, wy + 26, 60); gl.addColorStop(0, 'rgba(246,213,142,0.35)'); gl.addColorStop(1, 'rgba(246,213,142,0)'); ctx.fillStyle = gl; ctx.fillRect(wx - 44, wy - 34, 120, 120); }
        ctx.fillStyle = lit ? lg(ctx, 0, wy, 0, wy + 52, [[0, '#F6D58E'], [1, '#D9A75A']]) : lg(ctx, 0, wy, 0, wy + 52, [[0, '#2B3140'], [1, '#1A1F29']]);
        ctx.fillRect(wx, wy, 32, 52); ctx.strokeStyle = INK; ctx.lineWidth = 2.5; ctx.strokeRect(wx, wy, 32, 52); ctx.beginPath(); ctx.moveTo(wx, wy + 26); ctx.lineTo(wx + 32, wy + 26); ctx.stroke();
        ctx.fillStyle = '#3A302A'; ctx.fillRect(wx - 4, wy + 52, 40, 6); }
    }
    // ---- ngân hàng (chính diện): bậc, 6 trụ có rãnh, dầm chữ BANK, trán tường, cửa đóng + giấy CLOSED
    const bx0 = 600, bx1 = 1380, base = 820;
    block(ctx, bx0 + 20, 300, bx1 - bx0 - 40, base - 300 - 60, '#D3CCBC', '#9C9586');
    for (let i = 0; i < 4; i++) block(ctx, bx0 - 30 + i * 18 - 20, base - 60 + i * 20 - 20, bx1 - bx0 + 60 - i * 36 + 40, 22, '#C9C2B2', '#A39C8D', { lw: 2.5 });
    ctx.fillStyle = '#20252E'; ctx.fillRect(930, 520, 120, 220); ctx.strokeStyle = INK; ctx.lineWidth = 3; ctx.strokeRect(930, 520, 120, 220);
    block(ctx, 938, 528, 50, 212, '#6B5038', '#3E2E20', { lw: 2.5 }); block(ctx, 992, 528, 50, 212, '#6B5038', '#3E2E20', { lw: 2.5 });
    inkProp(ctx, 'note', { s: 0.32, label: 'CLOSED' }, { x: 990, y: 650, w: 140, h: 160, pad: 10, outline: 3, dots: 0.3 });
    for (const x of [700, 1260]) block(ctx, x - 40, 470, 80, 160, '#2B3140', '#1A1F29');
    for (let i = 0; i < 6; i++) { const cx = 650 + i * 136, cw = 62;
      ctx.fillStyle = lg(ctx, cx - cw / 2, 0, cx + cw / 2, 0, [[0, '#F1EBDD'], [0.45, '#D7D0C0'], [1, '#8F887A']]); ctx.fillRect(cx - cw / 2, 360, cw, 400);
      ctx.strokeStyle = 'rgba(21,23,28,0.35)'; ctx.lineWidth = 1.5; for (let f = 1; f < 5; f++) { ctx.beginPath(); ctx.moveTo(cx - cw / 2 + f * cw / 5, 362); ctx.lineTo(cx - cw / 2 + f * cw / 5, 758); ctx.stroke(); }
      ctx.save(); ctx.beginPath(); ctx.rect(cx, 360, cw / 2, 400); ctx.clip(); halftone(ctx, cx, 360, cw / 2, 400, (px) => (px - cx) / (cw / 2), { step: 6, alpha: 0.45 }); ctx.restore();
      ctx.lineWidth = 3; ctx.strokeStyle = INK; ctx.strokeRect(cx - cw / 2, 360, cw, 400);
      block(ctx, cx - 44, 340, 88, 22, '#D9D2C2', '#B0A999', { lw: 2.5 }); block(ctx, cx - 44, 756, 88, 22, '#D9D2C2', '#B0A999', { lw: 2.5 }); }
    block(ctx, bx0 - 10, 262, bx1 - bx0 + 20, 80, '#D9D2C2', '#ADA696');
    ctx.fillStyle = '#2A303B'; ctx.font = '700 52px Inter'; ctx.textAlign = 'center'; ctx.letterSpacing = '22px'; ctx.fillText('BANK', 990 + 11, 320); ctx.letterSpacing = '0px';
    ctx.beginPath(); ctx.moveTo(bx0 - 30, 262); ctx.lineTo(990, 140); ctx.lineTo(bx1 + 30, 262); ctx.closePath();
    ctx.fillStyle = lg(ctx, 0, 140, 0, 262, [[0, '#E3DDCF'], [1, '#B7B0A0']]); ctx.fill(); ctx.lineWidth = 3.5; ctx.strokeStyle = INK; ctx.stroke();
    ctx.save(); ctx.clip(); halftone(ctx, 990, 140, 420, 122, () => 0.4, { step: 7, alpha: 0.35 }); ctx.restore();
    // ---- lớp giữa phải: nhà cao + cột đèn với quầng sáng
    block(ctx, 1430, 160, 520, 660, '#4E5563', '#2B303B');
    ctx.save(); ctx.beginPath(); ctx.rect(1430, 160, 520, 660); ctx.clip(); halftone(ctx, 1430, 160, 520, 660, (px, py) => 0.2 + (py - 160) / 900, { step: 8, alpha: 0.4 }); ctx.restore();
    for (let r = 0; r < 7; r++) for (let c = 0; c < 6; c++) { const lit = hash(500 + r * 13 + c) < 0.22, wx = 1460 + c * 80, wy = 190 + r * 86;
      ctx.fillStyle = lit ? '#F6D58E' : '#1E232D'; ctx.fillRect(wx, wy, 40, 56); ctx.strokeStyle = INK; ctx.lineWidth = 2.5; ctx.strokeRect(wx, wy, 40, 56); }
    // ---- vỉa hè: lát gạch phối cảnh, vệt phản chiếu ướt
    ctx.fillStyle = lg(ctx, 0, 820, 0, 1080, [[0, '#4E4B47'], [1, '#26262A']]); ctx.fillRect(0, 820, 1920, 260);
    ctx.strokeStyle = 'rgba(21,23,28,0.5)'; ctx.lineWidth = 2;
    for (let i = -12; i < 30; i++) { ctx.beginPath(); ctx.moveTo(960 + i * 90, 820); ctx.lineTo(960 + i * 260 - 600, 1080); ctx.stroke(); }
    for (const y of [850, 895, 955, 1030]) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(1920, y); ctx.stroke(); }
    ctx.lineWidth = 4; ctx.strokeStyle = INK; ctx.beginPath(); ctx.moveTo(0, 820); ctx.lineTo(1920, 820); ctx.stroke();
    for (const [x, c, w] of [[1340, 'rgba(246,213,142,0.32)', 40], [990, 'rgba(211,204,188,0.16)', 220], [700, 'rgba(211,204,188,0.12)', 50]]) {
      ctx.fillStyle = lg(ctx, 0, 822, 0, 1060, [[0, c], [1, 'rgba(0,0,0,0)']]); ctx.fillRect(x - w / 2, 822, w, 240); }
    // cột đèn
    const lx = 1340; const glow = ctx.createRadialGradient(lx, 420, 10, lx, 420, 420); glow.addColorStop(0, 'rgba(246,190,90,0.55)'); glow.addColorStop(1, 'rgba(246,190,90,0)');
    ctx.fillStyle = glow; ctx.fillRect(lx - 420, 0, 840, 840);
    block(ctx, lx - 8, 440, 16, 390, '#2A2F38', '#14171C', { lw: 2.5 }); block(ctx, lx - 26, 372, 52, 70, '#FBE3A6', '#E6A84B', { lw: 3 }); block(ctx, lx - 34, 360, 68, 14, '#2A2F38', '#14171C', { lw: 2.5 });
    // ---- hàng người (lớp giữa): từ cửa ngân hàng sang phải
    const Q = [['q4', 'neutral', 0, true], ['q2', 'worried', 0], ['q1', 'sad', 0, true], ['q3', 'worried', 0], ['q5', 'sad', 0, true], ['q1', 'worried', 0]];
    Q.forEach(([id, expr, _, flip], i) => { const x = 1060 + i * 74, y = 846 + (i % 2) * 6, pose = i === 2 ? POSES.phone : i === 4 ? POSES.slump : POSES.stand;
      inkChar(ctx, { id, pose, expr, flip, s: 0.36 }, { x, y, w: 230, h: 310, pad: 12, outline: 3, dots: 0.18, shade: 0.3, light: [1, -0.6] }); });
    // ---- tiền cảnh: Walt lo lắng, cầm sổ
    const pose = { ...blendPose(POSES.stand, POSES.slump, 0.3), head: 9, uaR: 22, faR: 100, uaL: 14, faL: -20 };
    inkChar(ctx, { id: 'walt', pose, expr: 'worried', s: 1.12 }, { x: 1530, y: 1130, w: 680, h: 940, pad: 20, outline: 7, light: [0.9, -0.7], shade: 0.5, dots: 0.6 });
    inkProp(ctx, 'note', { s: 0.36, label: ' ' }, { x: 1526, y: 852, w: 200, h: 200, pad: 10, outline: 4, dots: 0.3, light: [0.9, -0.7] });
    // ---- mưa, vân giấy, viền tối, chữ
    rain(ctx, 1920, 1080, { n: 520 });
    ctx.restore();
    paperGrain(ctx, W, H, 0.26); vignette(ctx, W, H, 0.45);
    caption(ctx, W, H, { title: 'New York, 1931', sub: 'A line outside a bank that closed its doors', tag: 'ILLUSTRATIVE' });
  }
  return { canvas: out, frame: () => { paint(); return { violations: [] }; } };
}
