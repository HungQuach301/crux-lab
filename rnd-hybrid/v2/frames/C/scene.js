// R&D hình lai vòng 2 · KHUNG C "ảnh tư liệu thật làm nền": LoC cph.3c17261 (NYWT&S, 1931; RIGHTS §F6 X-RND-1) phủ tông kênh
// (duotone nền kênh → giấy, hạt, mờ nhẹ để tách lớp) + Walt cắt giấy phía trước (rig.js) có bóng đổ như tờ giấy nhấc khỏi ảnh.
// Ảnh không làm bằng chứng cho claim số (§F4): khung không có số; năm + nguồn trên hình. Tệp ảnh ở work/external/ (ngoài git).
import { POSES, blendPose } from '/rnd-hybrid/cutout/rig.js';
import { caption, vignette, paperGrain } from '/rnd-hybrid/v2/paper3d.js';
import { inkChar, inkProp, lg } from '/rnd-hybrid/v2/illus2d.js';

const PHOTO = '/rnd-hybrid/work/external/bank1931_crop.jpg';   // cắt 16:9 từ 3c17261u.tif (SHA ghi ở RIGHTS §F6)
const TONE = [[0, '#0E1116'], [0.45, '#4A5160'], [0.8, '#B9B3A4'], [1, '#EDE4CF']];   // bg kênh → muted → giấy

function lut() { const c = new OffscreenCanvas(256, 1), g = c.getContext('2d'); g.fillStyle = lg(g, 0, 0, 256, 0, TONE); g.fillRect(0, 0, 256, 1); return g.getImageData(0, 0, 256, 1).data; }

export async function boot(res) {
  for (const w of [400, 600, 700]) await document.fonts.load(`${w} 48px Inter`);
  const W = Math.round(res * 16 / 9), H = res, out = document.createElement('canvas'); out.width = W; out.height = H; const ctx = out.getContext('2d');
  const im = new Image(); im.src = PHOTO; await im.decode();
  // phủ tông một lần: xám → LUT kênh, tương phản nhẹ
  const t = new OffscreenCanvas(W, H), tg = t.getContext('2d'); tg.filter = 'blur(1.2px) contrast(1.12)'; tg.drawImage(im, -W * 0.03, -H * 0.03, W * 1.06, H * 1.06); tg.filter = 'none';
  const d = tg.getImageData(0, 0, W, H), L = lut();
  for (let i = 0; i < d.data.length; i += 4) { const v = d.data[i] * 0.299 + d.data[i + 1] * 0.587 + d.data[i + 2] * 0.114 | 0; d.data[i] = L[v * 4]; d.data[i + 1] = L[v * 4 + 1]; d.data[i + 2] = L[v * 4 + 2]; }
  tg.putImageData(d, 0, 0);
  function paint() {
    ctx.drawImage(t, 0, 0); paperGrain(ctx, W, H, 0.22);
    ctx.fillStyle = lg(ctx, 0, 0, W, 0, [[0, 'rgba(14,17,22,0)'], [0.55, 'rgba(14,17,22,0.10)'], [1, 'rgba(14,17,22,0.55)']]); ctx.fillRect(0, 0, W, H);   // tối dần về phía Walt để tách lớp
    vignette(ctx, W, H, 0.55);
    ctx.save(); ctx.scale(W / 1920, H / 1080);
    // bóng đổ của tờ giấy Walt lên ảnh (nhấc khỏi mặt ảnh), rồi Walt có nét mực mỏng + vân giấy
    const pose = { ...blendPose(POSES.stand, POSES.slump, 0.3), head: 9, uaR: 22, faR: 100, uaL: 14, faL: -20 };
    ctx.save(); ctx.filter = 'blur(9px)'; ctx.globalAlpha = 0.6; ctx.translate(24, 16);
    inkChar(ctx, { id: 'walt', pose, expr: 'worried', s: 1.12 }, { x: 1520, y: 1130, w: 680, h: 940, pad: 20, flat: '#05070A' });
    ctx.restore();
    ctx.save(); ctx.globalCompositeOperation = 'source-over';
    inkChar(ctx, { id: 'walt', pose, expr: 'worried', s: 1.12 }, { x: 1520, y: 1130, w: 680, h: 940, pad: 20, outline: 4, light: [-0.8, -0.8], shade: 0.38, dots: 0.12, grain: 0.32 });
    inkProp(ctx, 'note', { s: 0.36, label: ' ' }, { x: 1516, y: 852, w: 200, h: 200, pad: 10, outline: 3, dots: 0.1, light: [-0.8, -0.8] });
    ctx.restore(); ctx.restore();
    caption(ctx, W, H, { title: 'New York, 1931', sub: 'Depositors gather outside a failed bank', tag: 'ILLUSTRATIVE figure',
      source: '' });
    // dòng nguồn ảnh (năm + nguồn trên hình §F4). Lệch §F3 (nguồn ảnh bên phải dải chú thích): dải phải bị Walt chiếm → đặt góc trên trái
    ctx.save(); ctx.scale(W / 1920, H / 1080); ctx.font = '400 40px Inter'; ctx.textAlign = 'left'; ctx.fillStyle = 'rgba(14,17,22,0.6)';
    const src = 'Photo: Library of Congress (NYWT&S), 1931'; ctx.fillText(src, 98, 104); ctx.fillStyle = 'rgba(242,244,247,0.92)'; ctx.fillText(src, 96, 102); ctx.restore();
  }
  return { canvas: out, frame: () => { paint(); return { violations: [] }; } };
}
