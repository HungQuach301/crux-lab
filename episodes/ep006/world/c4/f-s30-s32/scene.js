// Tập 6 · C4 · ĐOẠN F = S30–S32. Thang mức tăng V10 (thế giới: bậc thang → đồ thị: thanh = phần quãng theo kịp) · giới hạn (hàng thùng chung, quãng chồng
// nhau, hai séc "?") · thẻ phương pháp V7 (5 s) · về khung mở đầu: Ruth, séc, 9/10 thùng → đồ thị "about 9 in 10". Mốc giờ chỉ từ spine.json.
import * as THREE from 'three';
import { Crates, Check } from '/toolkit/factory/world/lib3d.js';
import { setup, column, showColumn, hideColumn, setCheck, checkLabel, nameTag, rowBox, Ladder, modeLook, followLight, chrome, brace, label, seg2, dip, kf, show, pulse,
  CHAR, C, ease, lin, mix, rgba, setOpacity } from '/episodes/ep006/world/c4kit.js';

const SEG = '/episodes/ep006/world/c4/f-s30-s32/';
const LX = 20, LEN = 8, AX1 = 40, AX2 = 49;                        // thang (x0, dài 100 %), khu giới hạn 1 (hàng thùng), khu 2 (hai séc)

export async function boot(res) {
  const poses = {
    wLadder: { pos: [17.0, 3.2, 12.5], tgt: [23.2, 1.6, 0], fov: 40, chart: 0 },   // FIX-R1: phối cảnh dịu hơn, cả thang (bậc → "all stretches") trong khung
    cLadder: { pos: [22.66, 1.75, 34.86], tgt: [22.66, 1.75, 0], fov: 14, chart: 1 },   // lùi đủ để nhãn bậc (trái) và "all stretches" (phải) nằm trong vùng an toàn: 128 px/đv
    cLim1: { pos: [AX1, 1.1, 20], tgt: [AX1, 1.1, 0], fov: 14, chart: 1 },     // FIX-R1: hàng thùng cao hơn dải chân trang (đối trọng 2 dòng)
    cLim2: { pos: [AX2 + 0.6, 0.85, 11], tgt: [AX2 + 0.6, 0.85, 0], fov: 14, chart: 1 },
    wRuth: { pos: [-3.0, 2.2, 7.8], tgt: [-0.7, 0.5, 0], fov: 35, chart: 0 },
    cRuth: { pos: [-0.8, 0.95, 24], tgt: [-0.8, 0.95, 0], fov: 14, chart: 1 },
  };
  const { S, cue, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const b = cue, L = S.label_cues;
  const lad = Ladder(scene, S.rungs, { x0: LX, y0: 0.3, step: 0.9, len: LEN });
  const row = Crates({ size: 0.5, gap: 0.1, name: 'basket' }); row.position.set(AX1, 0, 0); scene.add(row);
  const lvC = Check({ w: 0.5, base: 1.0, name: 'level-limits' }); lvC.position.set(AX2, 0, 0); scene.add(lvC);
  lvC.traverse((o) => { if (o.isMesh && o.material.color && o.material.color.getHexString() === 'f2f4f7') { o.material.color.set(C.muted); o.material.emissive.set(C.muted); o.material.emissiveIntensity = 0.12; } });
  const riC = Check({ w: 0.5, base: 0.75, name: 'rising-limits' }); riC.position.set(AX2 + 1.2, 0, 0); scene.add(riC);
  const ruth = column(scene, { x: 0, name: 'ruth' });   // P3c: séc đứng như vòng 2 — khoá nghĩa B32 (vòng 2 nghĩa 2/2; séc ngang + bước nấc ở vòng 3: 1/3)
  const grow = [[b.g1.forty, 1], [b.g2.half, 2], [b.g3.carls, 3]];
  // FIX-R1: mọi vật vẽ sau sàn trong suốt (vật đang hiện/mờ dần không bị sàn vẽ đè); mỗi khu chỉ hiện quanh lời của nó, hiện/mờ trong cú lia
  // (không còn hàng thùng / thanh / séc thò ở mép khung lúc chuyển 486, 500, 517 s, vật trắng ở mép phải thang 455–461 s)
  scene.traverse((o) => { if (o !== floor && o.isMesh) o.renderOrder = 2; });
  // S32 (nghĩa B32): khoản của Ruth là khoản TĂNG — "Twenty years ago" séc về khoản đầu (k = 0, 10 thùng), "Her answer: for fifteen years"
  // năm 1 → 15 (séc lớn dần, hàng gần đủ), năm 16 → 20 tới "eighty-five" (9 thùng), như khung mở đầu
  const P = S.ruth_path, W32 = MV.m_w32;
  const yr32 = (t) => t < b.i1.t0 ? 20 : t < b.i2.t0 ? 20 * (1 - ease(t, b.i1.t0, b.i1.ruth + 0.3)) : t < b.i2.yes ? 15 * lin(t, b.i2.t0 + 0.1, b.i2.yes) : 15 + 5 * lin(t, b.i2.yes + 0.3, b.i2.eighty + 0.3);

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    // thang: bậc 2 % hiện đủ khi vào đồ thị (kết quả hồi 2); ba bậc kia mọc đúng từ khoá
    const P31 = MV.m_pan31, P31b = MV.m_pan31b;
    const ladA = 1 - ease(t, P31.t0, P31.t0 + 0.6), rowA = ease(t, P31.t1 - 0.6, P31.t1) * (1 - ease(t, P31b.t0, P31b.t0 + 0.35));
    // R2 (khung chuyển máy): Ruth chỉ hiện khi máy gần dừng ở wRuth (trước: hiện từ đầu cú, cả cột ngoài khung ~0,9 s)
    // C5b (V11): hai séc tắt hẳn TRƯỚC khi thẻ phương pháp hiện — chữ thẻ không chồng séc 3D lúc thẻ còn mờ
    const chkA = ease(t, P31b.t1 - 0.4, P31b.t1) * (1 - ease(t, S.card[0] - 0.4, S.card[0])), ruA = ease(t, W32.t1 - 0.22, W32.t1 + 0.2);
    lad.set(0, S.rungs[0].share / 100 * ease(t, MV.m_c30.t0, MV.m_c30.t1), ladA);
    for (const [tt, i] of grow) lad.set(i, S.rungs[i].share / 100 * ease(t, tt - 0.6, tt + 0.1), ladA);   // FIX-R1: thanh tới đích ĐÚNG lúc lời đọc số
    for (let i = 0; i < 4; i++) { const r = lad.rungs[i]; const hi = i === 1 ? Math.max(pulse(t, b.g1.three, 1), show(t, b.g1.three, b.g2.three)) : i === 2 ? pulse(t, b.g2.three, 1) : i === 3 ? pulse(t, b.g3.every, 1) : 0;
      r.tread.material.color.set(hi > 0.05 ? C.ink : '#5B6573'); }   // bậc 3 % sáng từ "three" (thế giới) tới bậc 3,1 %
    row.set({ value: 1, pulse: pulse(t, b.h0.national, 1.2) }); setOpacity(row, rowA);
    lvC.set({ k: 0, appear: 1 }); riC.set({ k: 0, appear: 1 }); setOpacity(lvC, chkA); setOpacity(riC, chkA); lvC.userData.first.visible = riC.userData.first.visible = chkA > 0.5;
    const k32 = yr32(t), kf32 = Math.min(20, Math.max(0, k32)), j = Math.min(19, Math.floor(kf32));
    hideColumn(ruth, 1);
    ruth.row.set({ value: P[j] + (P[j + 1] - P[j]) * (kf32 - j), pulse: pulse(t, b.i2.nine, 0.9) + pulse(t, b.i1.ruth, 0.9) + pulse(t, b.i2.fifteen, 0.9) });
    ruth.card.set({ k: kf32 }); showColumn(ruth, ruA); if (ruA < 0.999) hideColumn(ruth, ruA);
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    dip(O, 1 - ease(t, 0, 0.4));   // P3c (C14 1080p): lớp mờ vào đầu đoạn vẽ TRƯỚC mọi chữ — chữ không mờ dưới lớp tối
    // S30 (cLadder): nhãn bậc bên trái; giá trị ở đầu thanh — TRONG thanh khi thanh đủ dài (≥ 25 %), ngoài khi ngắn (2,4 %): nhờ vậy vạch "half"
    // không cắt qua "42.4%" và "all · Carl's stretch" không tràn mép phải; vạch "half" / "all stretches"
    if (t < MV.m_pan31.t1) {
      const a = ok * (1 - show(t, MV.m_pan31.t0)), shownAt = [MV.m_c30.t1, b.g1.three, b.g2.three, b.g3.every], valAt = [MV.m_c30.t1, b.g1.forty, b.g2.half, b.g3.carls];
      for (let i = 0; i < 4; i++) {
        const r = lad.rungs[i], [xl, y] = O.toScreen(LX - 1.7, r.y, 0.5), [xe] = O.toScreen(LX + LEN * S.rungs[i].share / 100, r.y, 0.5);
        label(O, S.rungs[i].label, xl, y + 16, { align: 'right', kind: 'number', px: 52, alpha: a * show(t, shownAt[i]) });
        const inside = S.rungs[i].share >= 25;
        label(O, S.rungs[i].value, inside ? xe - 24 : xe + 24, y + 16, { align: inside ? 'right' : 'left', kind: i === 3 ? 'compare' : 'number', px: 48, alpha: a * show(t, i ? valAt[i] : valAt[i] + 0.8) });
        log.roi[['g1.three', 'g1.three', 'g2.half', 'g3.carls'][i]] = [xl - 200, y - 40, xe + 400, y + 40];
      }
      const [xh, yt] = O.toScreen(LX + LEN * 0.5, 3.4, 0.5), [xa] = O.toScreen(LX + LEN, 3.4, 0.5), [, yb] = O.toScreen(LX, 0, 0.5);
      seg2(O, xh, yt, xh, yb, C.muted, a * show(t, b.g2.half), 3, [8, 8]); seg2(O, xa, yt, xa, yb, C.muted, a * show(t, MV.m_c30.t1), 3, [8, 8]);
      // FIX-R1: hai nhãn tên của thang hiện từ "raise" ngay ở thế giới (loại 'name', không số) — thang 3D 5 s đầu không còn câm
      const nA = (1 - show(t, MV.m_pan31.t0)) * show(t, b.g0.raise);
      label(O, 'all stretches', xa, yb + 46, { align: 'center', kind: 'name', px: 48, w: 600, color: C.muted, alpha: nA });
      { const [xl0] = O.toScreen(LX - 1.7, 0, 0.5); label(O, 'raise a year', xl0, yb + 46, { align: 'right', kind: 'name', px: 48, w: 600, color: C.muted, alpha: nA }); }
      label(O, L['g2.median'], 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: a * show(t, b.g2.median, b.g3.every - 0.3) });
      log.roi['g1.forty'] = log.roi['g1.three']; log.roi['g2.median'] = [400, 170, 1520, 260];
    }
    // S31 giới hạn
    label(O, L['h0.national'], 960, 236, { align: 'center', kind: 'name', px: 52, w: 600, alpha: ok * show(t, b.h0.national, MV.m_pan31b.t0) });
    const oA = ok * show(t, b.h1.overlap, MV.m_pan31b.t0);
    if (oA > 0.01) {   // quãng 20 năm chồng nhau: 9 thanh lệch nhau một tháng (thanh dài 1 200 px = 240 tháng → 5 px/tháng)
      const c = O.ctx; c.save();
      for (let j = 0; j < 9; j++) { c.globalAlpha = oA * 0.55; c.fillStyle = j === 4 ? C.ink : C.muted; c.fillRect(360 + j * 5 * 3 * lin(t, b.h1.overlap, b.h1.overlap + 0.8), 330 + j * 14, 1200, 10); }
      c.restore();
      label(O, L['h1.overlap'], 960, 520, { align: 'center', kind: 'number', px: 52, alpha: oA });
      log.roi['h1.overlap'] = [340, 320, 1600, 540];
    }
    if (t > MV.m_pan31b.t0 && t < MV.m_w32.t1) {
      const qA = ok * show(t, b.h2.annuity, b.h3.card - 0.3);
      const [ax, ay] = O.toScreen(AX2 - 0.25, 1.0, 0.1), [bx, by] = O.toScreen(AX2 + 1.45, 0.75, 0.1);
      if (qA > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = qA; c.fillStyle = rgba(C.muted, 0.35); c.fillRect(ax, ay, bx - ax, by - ay); c.restore(); label(O, '?', bx + 30, (ay + by) / 2 + 30, { kind: 'title', px: 84, alpha: qA, plate: null }); }
      label(O, L['h2.dollars'], 960, 236, { align: 'center', kind: 'compare', px: 52, alpha: ok * show(t, b.h2.dollars, b.h3.card - 0.3) });
      log.roi['h2.dollars'] = [400, 170, 1520, 260];
    }
    // S31.4: thẻ V7 (≤ 6 dòng, 5 s) — nền thẻ trung tính, chữ ≥ 48 px; thẻ 110–1810 để dòng dài nhất (~1 655 px) nằm trong thẻ, không bị đẩy lệch lề
    const kA = ok * show(t, S.card[0], S.card[1]);
    if (kA > 0.01) {
      O.card(100, 190, 1722, 640, { fill: '#171B22', stroke: '#2A303B', lw: 3, alpha: kA * 0.96 });   // FIX-R1: dòng 1 cách mép phải thẻ ≥ 35 px
      label(O, L.card0, 130, 280, { kind: 'title', px: 60, alpha: kA, plate: null });
      for (let i = 1; i <= 5; i++) label(O, L['card' + i], 130, 290 + i * 92, { kind: 'number', px: 48, w: 600, alpha: kA, plate: null, color: i === 4 ? C.muted : C.ink });
      log.roi['h3.card'] = [100, 190, 1822, 830];
    }
    // S32: Ruth, séc, hàng (khung mở đầu) → đồ thị
    nameTag(O, ruth, ruA * (1 - cw));
    if (t > MV.m_c32.t0) {
      const R = rowBox(O, ruth, S.ruth_end);
      label(O, L['i2.eighty'], 120, 236, { kind: 'number', px: 52, w: 600, color: CHAR.ruth, alpha: ok * show(t, MV.m_c32.t1) });
      checkLabel(O, ruth, L['i2.check'], ok * show(t, MV.m_c32.t1), { dx: 14 });   // FIX-R1 (B32): khoản TĂNG, cùng nhãn khung mở đầu
      const nA = ok * show(t, b.i2.nine), tA = ok * show(t, b.i2.ten);
      brace(O, R.x0, R.xl, R.yb + 22, C.ink, nA, 5, -14);
      label(O, L['i2.nine'], (R.x0 + R.xl) / 2, R.yb + 86, { align: 'center', kind: 'number', px: 52, alpha: nA });
      brace(O, R.x0, R.x1, R.yb + 132, C.muted, tA, 5, -14);
      label(O, L['i2.ten'], (R.x0 + R.x1) / 2, R.yb + 196, { align: 'center', kind: 'number', px: 48, color: C.muted, alpha: tA });
      log.roi['i2.nine'] = [R.x0 - 10, R.yb, R.x1 + 10, R.yb + 110]; log.roi['i2.ten'] = [R.x0 - 10, R.yb + 110, R.x1 + 10, R.yb + 220];
      log.roi['i2.eighty'] = [100, 170, 900, 260];
    }
    // C5b (S08): huy hiệu từ "every" (khi nhãn bậc "6.38%" hiện), sớm 0,1 s — không còn khung số mà thiếu huy hiệu
    const illus = Math.max(show(t, b.g3.every - 0.1, MV.m_pan31.t0), show(t, MV.m_w32.t0));
    const cwA = show(t, b.g4.choose - 0.8, MV.m_pan31.t1 + 0.3);   // FIX-R1: đối trọng 8 từ ≥ 3 s
    chrome(O, illus, cwA > 0.01 ? L['g4.choose'] : null, cwA);
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
