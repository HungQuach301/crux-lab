// Tập 9 · ĐOẠN E = S19–S21 (chương 5 "Why the house holds half"). Khối nhà $400,000 cạnh đống $92,000 → cả hai lớn (đống nhanh hơn theo tỉ lệ, nhà thêm
// nhiều $ hơn) → bó mỗi tháng rơi vào đống → bó dừng → phố từ trên: sáng lại (chỉ $92,000: 2/3) → phí 1 %/năm: 55 %.
import { setup, Street, Home8, MoneyStack, StockPile, label, chrome, chapterCard, legend, followLight, modeLook, show, ease, lin, sweep,
  LIT, STK, C } from '/episodes/ep009/world/w9.js';

const SEG = `/${new URLSearchParams(location.search).get('seg')}/`;   // đoạn con (re-export) đọc spine.json của chính thư mục nó
const PS = 0.3, UNIT = 0.07 * 1e5 / PS, HX = -6.2, PX = -4.6, Z = 1.6;

export async function boot(res) {
  const poses = {
    cBase: { pos: [(HX + PX) / 2, 1.9, Z + 9.5], tgt: [(HX + PX) / 2, 1.6, Z], fov: 26, chart: 1 },
    cGrid: { pos: [11.9, 30, 3.0], tgt: [11.9, 0, -5.2], fov: 36, chart: 1 },
  };
  const { S, DATA, cue: b, MV, st, O, renderer, scene, floor, key, CAM } = await setup(SEG, res, poses);
  const st10 = DATA.starts10, street = Street(scene, st10), H = Home8(scene);
  const house = MoneyStack(scene, { x: HX, z: Z, color: LIT, unit: UNIT, name: 'house-base', max: 90, w: 1.0, d: 0.7 });
  const pile = StockPile(scene, { x: PX, z: Z, s: PS, name: 'pile-base' });
  // tăng trưởng 10 năm TRUNG VỊ trên 307 cửa sổ (data.json gH / gS): chỉ chiều cao minh hoạ, không nhãn số
  const med = (a) => [...a].sort((x, y) => x - y)[a.length >> 1], GH = med(DATA.gH), GS = med(DATA.gS);
  const AS = DATA.ahead10.stocks, AL = DATA.ahead10.lump, AF = DATA.ahead10.fee;

  function frame(t) {
    const pose = CAM.apply(t), cw = pose.chart, cam = CAM.cam;
    followLight(key, pose.tgt); modeLook(scene, floor, cw);
    const g = ease(t, b.e2.base - 0.2, b.e2.base + 1.8), dep = lin(t, b.e3.monthly, b.e4.nobody) * 12;
    const bA = show(t, 0, MV.m_g.t1);
    house.set({ usd: 400000 * ease(t, b.e1.four - 0.3, b.e1.four + 0.5) * (1 + (GH - 1) * g), a: bA });
    const pu = 92000 * ease(t, b.e1.ninety - 0.3, b.e1.ninety + 0.5) * (1 + (GS - 1) * g) + 6000 * Math.min(dep, 12);
    pile.set({ usd: Math.max(1, pu), a: bA, line: 0, dropK: t > b.e3.monthly - 0.3 && t < b.e4.nobody ? dep % 1 : -1 });
    let L = sweep(AS, AS, 1, st10);
    if (t > b.e5.two - 0.2 && t < b.e7.fees) L = sweep(AS, AL, lin(t, b.e5.two - 0.2, b.e5.two + 1.4), st10);
    else if (t >= b.e7.fees && t < b.e8.fifty - 0.2) L = sweep(AL, AS, lin(t, b.e7.fees, b.e7.fees + 1.0), st10);
    else if (t >= b.e8.fifty - 0.2) L = sweep(AS, AF, lin(t, b.e8.fifty - 0.2, b.e8.fifty + 1.2), st10);
    street.set({ ...L, cellA: cw * (t > MV.m_g.t1 - 0.3 ? 1 : 0) });
    H.tag.set({ value: 5 });
    renderer.render(scene, cam);
    const log = O.begin(t, cw, cam), ok = cw >= 0.95 ? 1 : 0; log.roi = {};
    chapterCard(O, S.chapter[1], t, S.chapter[0]);
    const a = ok * (t < MV.m_g.t0 + 0.2 ? 1 : 0), [hx, hy] = O.toScreen(HX, 0, Z), [px] = O.toScreen(PX, 0, Z);
    label(O, 'stocks grew more: 88.9% of start months', 960, 240, { align: 'center', kind: 'number', px: 50, alpha: a * show(t, Math.max(b.e0.stocks, S.chapter[0] + 2.7), b.e1.four - 0.2), claims: ['share_stocks_beat_house_10y_pct'] });
    label(O, '…yet the buyer ahead in about half', 960, 320, { align: 'center', kind: 'number', px: 48, alpha: a * show(t, b.e0.half, b.e1.four - 0.2), claims: ['share_buyer_ahead_stocks_10y'] });
    label(O, 'house: $400,000 base', hx + 40, Math.min(hy + 60, 800), { align: 'right', kind: 'number', px: 44, alpha: a * show(t, b.e1.four), color: LIT, claims: ['price'] });
    label(O, 'pile: $92,000 start', px - 20, Math.min(hy + 60, 800) + 70, { align: 'left', kind: 'number', px: 44, alpha: a * show(t, b.e1.ninety), color: STK, claims: ['savings_usd'] });
    label(O, 'slower growth on a bigger base', 960, 240, { align: 'center', kind: 'name', px: 52, alpha: a * show(t, b.e2.slower, b.e3.monthly - 0.2) });
    label(O, 'the renter catches up: the monthly gap + time', 960, 240, { align: 'center', kind: 'name', px: 52, alpha: a * show(t, b.e3.monthly, MV.m_g.t0) });
    log.roi['e1.four'] = [hx - 250, hy - 500, hx + 250, hy + 100]; log.roi['e1.ninety'] = [px - 200, hy - 300, px + 300, hy + 100];
    const gA = ok * (t > MV.m_g.t1 - 0.2 ? 1 : 0);
    label(O, 'only the $92,000 invested: about 2 in 3', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.e5.two, b.e7.fees - 0.2), claims: ['savings_usd', 'share_buyer_ahead_lump_10y'] });
    label(O, '1% a year in fees: 55.0% lit', 960, 230, { align: 'center', kind: 'number', alpha: gA * show(t, b.e8.fifty), claims: ['fee_pct', 'share_buyer_ahead_stocks_fee_10y'] });
    label(O, "each cost on the renter's side relights houses", 960, 320, { align: 'center', kind: 'name', px: 48, alpha: gA * show(t, b.e9.back) });
    log.roi['e5.two'] = [300, 180, 1620, 950]; log.roi['e8.fifty'] = [300, 180, 1620, 950];
    legend(O, gA);
    chrome(O, { illus: 1 });
    st.compose(); log.camMoving = CAM.moving(t); return log;
  }
  return { canvas: st.out, frame };
}
