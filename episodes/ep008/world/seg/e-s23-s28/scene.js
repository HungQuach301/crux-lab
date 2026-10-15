// Tập 8 · ĐOẠN E = S23–S28 (chương 5 "Two neighbors, one tag"). Marcus (nhà tối, June 2006) và Priya (nhà sáng, April 2012) trên cùng phố → đèn tắt:
// ngày mua không ai thấy → thẻ trên cửa; tiền thuê cao hơn → bó vào hộp ít hơn → cẩu lên phố: thẻ 4 % (số neo 3) đèn tắt dần, 6 % sáng gần hết → dải Census
// → biến thể T-bill → đèn theo thẻ; bãi trống qua cuối phố.
import { setup, Street, Home8, figure, GlassBox, nameTag, label, chrome, chapterCard, legend, seg2, followLight, modeLook, show, pulse, ease, lin,
  xOf, zOf, colOf, END_X, APT, NINA, BOX, LIT, DARKW, C, THREE } from '/episodes/ep008/world/w8.js';

const SEG = '/episodes/ep008/world/seg/e-s23-s28/';
const BX = xOf('2012-04'), BZ = zOf('2012-04'), DX = xOf('2006-06'), DZ = zOf('2006-06');

export async function boot(res) {
  const poses = {
    wPair: { pos: [(BX + DX) / 2, 3.0, 9.5], tgt: [(BX + DX) / 2, 0.8, -1.5], fov: 44, chart: 0 },
    wMarcus: { pos: [DX - 1.2, 1.7, 5.2], tgt: [DX, 0.9, -1.2], fov: 40, chart: 0 },
    wPriya: { pos: [BX - 1.2, 1.7, 5.2], tgt: [BX, 0.9, -1.2], fov: 40, chart: 0 },
    wTag: { pos: [APT.x - 1.6, 1.4, 4.0], tgt: [APT.x + 0.1, 0.7, -1.2], fov: 40, chart: 0 },
    cGrid: { pos: [11.9, 31, 4.5], tgt: [11.9, 0, -5.2], fov: 34, chart: 1 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, n = st10.length, street = Street(scene, st10), H = Home8(scene);
  const nina = figure(scene, { x: NINA.x, z: NINA.z, lamp: true }), box = GlassBox(scene, { x: BOX.x, z: BOX.z });
  const marcus = figure(scene, { x: DX + 0.1, z: 1.0, color: '#E2D3C2', char: 'Marcus' }), priya = figure(scene, { x: BX + 0.1, z: 1.0, color: '#D3E2C9', char: 'Priya' });
  const iB = st10.indexOf('2012-04'), iD = st10.indexOf('2006-06'), A = DATA.ahead10;
  // trạng thái phố theo thẻ: [giờ đổi, khoá ahead10, giá trị thẻ]
  const seq = [[0, '5', 5], [b.e9.four, '4', 4], [b.e10.six, '6', 6], [b.e12.census, 'hvs_yield_2025Q4', 4.83], [b.e12.census + 1.6, 'hvs_yield_2026Q1', 5.59],
    [b.e12.census + 3.2, 'hvs_yield_2025Q4', 4.83], [b.e12.census + 4.8, 'hvs_yield_2026Q1', 5.59], [b.e13.treasury, 'tbills', 5], [b.e14.lights, '5', 5]];
  const at = (t) => { let k = 0; for (let j = 0; j < seq.length; j++) if (t >= seq[j][0]) k = j; return k; };

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    nina.lamp.set(1, t); nina.look(-0.3);
    const k = at(t), cur = seq[k], prev = seq[Math.max(0, k - 1)], tr = (i) => ease(t, cur[0] + colOf(st10[i]) / 26 * 0.8, cur[0] + colOf(st10[i]) / 26 * 0.8 + 0.25);
    const on = (key_, i) => (A[key_][i] ? 1 : 0), off = show(t, b.e5.neither, MV.m_tag.t1);
    const up = show(t, 0.0, MV.m_tag.t0 + 0.6);
    street.set({
      lit: (i) => { const v = cw > 0.5 ? (on(prev[1], i) * (1 - tr(i)) + on(cur[1], i) * tr(i)) : A['5'][i] ? 1 : 0; return v * ((i === iB || i === iD) ? 1 - off : 1); },
      dark: (i) => { const v = cw > 0.5 ? ((1 - on(prev[1], i)) * (1 - tr(i)) + (1 - on(cur[1], i)) * tr(i)) : A['5'][i] ? 0 : 1; return v * ((i === iB || i === iD) ? 1 - off : 1); },
      lift: (i) => (i === iB || i === iD ? 0.9 * up : 0), big: (i) => (i === iB || i === iD ? 1 + 1.4 * up : 1), cellA: cw,
    });
    marcus.p.visible = priya.p.visible = t > MV.m_p1.t0 && t < MV.m_tag.t1;   // G2 câu 5d: S23.2 bỏ → hai người hiện khi máy tới
    // thẻ: 5 % → lên ở "higher" (thuê đắt hơn) → bó vào hộp ít hơn; ở đồ thị theo chuỗi seq
    const tagV = t < b.e7.higher ? 5 : t < MV.m_c.t0 ? 6 : cur[2];
    H.tag.set({ value: tagV, swing: 0.2 * pulse(t, b.e7.higher, 1.2) * Math.sin((t - b.e7.higher) * 8) + 0.05 * Math.sin(t * 1.3) });
    box.set({ n: 8 - 3 * ease(t, b.e7.higher + 0.3, b.e7.less + 0.4), a: 1, glow: show(t, b.e13.treasury, b.e14.lights) });
    renderer.render(scene, cam);
    // ---------------- lớp phủ
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    const wA = cw < 0.05 ? 1 : 0;
    nameTag(O, marcus, wA * show(t, b.e2.marcus - 0.2, MV.m_tag.t0)); nameTag(O, priya, wA * show(t, b.e3.priya - 0.2, MV.m_tag.t0));
    nameTag(O, nina, wA * (t > MV.m_tag.t1 ? 1 : 0));
    const [dx, dy] = O.toScreen(DX, 2.2, DZ), [bx, by] = O.toScreen(BX, 2.2, BZ);
    label(O, 'renter ahead', dx, dy - 30, { align: 'center', kind: 'name', px: 44, alpha: wA * show(t, b.e2.darkest, b.e5.neither), color: C.warn });
    label(O, 'buyer far ahead', bx, by - 30, { align: 'center', kind: 'name', px: 44, alpha: wA * show(t, b.e3.brightest, b.e5.neither), color: LIT });
    label(O, 'same tag · same costs · same street · different month', 960, 250, { align: 'center', kind: 'name', px: 48, alpha: wA * show(t, b.e4.month, b.e5.neither + 1.5) });
    label(O, 'on the day they bought: no light to see', 960, 250, { align: 'center', kind: 'name', px: 48, alpha: wA * show(t, b.e5.neither + 1.5, MV.m_tag.t0) });
    log.roi['e2.marcus'] = [dx - 300, dy - 80, dx + 300, dy + 500]; log.roi['e3.priya'] = [bx - 300, by - 80, bx + 300, by + 500]; log.roi['e5.neither'] = [300, 200, 1600, 800];
    const [tx, ty] = O.toScreen(APT.x + 0.3, 0.95, APT.z + 0.66), [ox, oy] = O.toScreen(...box.top());
    label(O, 'higher rent → less into the cash box', ox, oy - 40, { align: 'center', kind: 'name', px: 44, alpha: wA * show(t, b.e7.higher, MV.m_c.t0), color: C.warn });
    log.roi['e6.tag'] = [tx - 160, ty - 60, tx + 160, ty + 140]; log.roi['e7.higher'] = [ox - 300, oy - 100, tx + 200, ty + 200];
    // đồ thị: thẻ ở góc trái (số giả định) + thang 2 % → 7 % với dải Census
    const gA = ok * (t > MV.m_c.t1 ? 1 : 0), tv = cur[2];
    const tagTxt = tv === 5 ? '5%' : null, tagKey = tv === 4 ? 'yield4_tag' : tv === 6 ? 'yield6_tag' : 'yield5_tag';
    if (tagTxt) label(O, `rent tag: ${tagTxt}`, 140, 250, { align: 'left', kind: 'number', px: 56, alpha: gA * (t < b.e12.census || t > b.e14.lights ? 1 : 0), claims: [tagKey] });
    label(O, 'rent tag 4%: buyer ahead in 64.2% of start months', 960, 240, { align: 'center', kind: 'number', px: 56, alpha: gA * show(t, b.e9.sixty, b.e10.six - 0.2), claims: ['share_yield4pct_10y', 'yield4_tag'] });
    label(O, 'rent tag 6%: buyer ahead in 92.2%', 960, 240, { align: 'center', kind: 'number', px: 56, alpha: gA * show(t, b.e10.ninety, b.e11.share + 1.8), claims: ['share_yield6pct_10y', 'yield6_tag'] });
    label(O, 'the share moves with the rent you assume', 960, 330, { align: 'center', kind: 'name', px: 48, alpha: gA * show(t, b.e11.share, b.e12.census - 0.2) });
    const sx0 = 560, sx1 = 1360, sy = 930, X = (v) => sx0 + (v - 2) / 5 * (sx1 - sx0), sc = gA * show(t, b.e12.census - 0.2, b.e13.treasury - 0.2);
    if (sc > 0.01) {
      seg2(O, sx0, sy, sx1, sy, C.muted, sc, 4); for (const v of [2, 3, 4, 5, 6, 7]) seg2(O, X(v), sy - 10, X(v), sy + 10, C.muted, sc, 3);
      const c = O.ctx; c.save(); c.globalAlpha = 0.85 * sc; c.fillStyle = C.accent; c.fillRect(X(4.83), sy - 16, X(5.59) - X(4.83), 32); c.restore();
      seg2(O, X(cur[2]), sy - 30, X(cur[2]), sy + 30, C.ink, sc, 6);
    }
    label(O, 'Census vacancy survey: 4.83% a year · 5.59% a year', 960, 860, { align: 'center', kind: 'number', px: 44, alpha: sc, claims: ['hvs_yield_2025Q4', 'hvs_yield_2026Q1'] });
    label(O, 'buyer ahead: 73.6% · 87.3%', 960, 240, { align: 'center', kind: 'number', px: 64, alpha: gA * show(t, b.e12.range, b.e13.treasury - 0.2), claims: ['share_hvs_2025Q4_10y', 'share_hvs_2026Q1_10y'] });
    label(O, "a reference, not Nina's own rent", 960, 330, { align: 'center', kind: 'name', px: 48, alpha: gA * show(t, b.e12.reference, b.e13.treasury - 0.2) });
    label(O, 'majority flips only below about 2.4%', 960, 330, { align: 'center', kind: 'number', px: 48, alpha: gA * show(t, S.at.flip, b.e14.lights - 0.2), claims: ['flip_yield_10y'] });
    label(O, 'Treasury bill interest: about 2 out of 3 (66.4%)', 960, 240, { align: 'center', kind: 'number', px: 56, alpha: gA * show(t, b.e13.two, b.e14.lights - 0.2), claims: ['share_tbills_10y', 'share_tbills_10y_pct'] });
    const [ex, ey] = O.toScreen(END_X + 0.6, 0, -2), ring = gA * show(t, b.e14.month);
    if (ring > 0.01) { const c = O.ctx; c.save(); c.globalAlpha = ring; c.strokeStyle = C.ink; c.lineWidth = 5; c.setLineDash([12, 10]); c.beginPath(); c.arc(ex, ey, 70, 0, 7); c.stroke(); c.restore(); }
    label(O, 'one month not on the street yet', Math.min(1500, ex - 40), ey + 130, { align: 'right', kind: 'name', px: 44, alpha: ring });
    log.roi['e9.four'] = [100, 180, 1700, 900]; log.roi['e10.six'] = [100, 180, 1700, 900]; log.roi['e12.census'] = [500, 820, 1420, 960]; log.roi['e13.treasury'] = [300, 180, 1620, 900];
    log.roi['e14.month'] = [ex - 120, ey - 120, ex + 120, ey + 160];
    legend(O, gA);
    chrome(O, {});
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
