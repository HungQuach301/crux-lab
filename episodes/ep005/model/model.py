"""Tập 5 — mô hình (đặc tả topics-r2/machine/debt-2/model.json → newKindNeeds; tên kind do phiên K quyết).
Viết lại từ result.json của hồ sơ, không gọi calc.py. Đọc episodes/ep005/data/raw/*.csv (data/fetch.py), ghi out/model.json
{params, raw (chưa làm tròn), rounded}. Thêm cho bản 101: người mua minh hoạ (ILLUSTRATIVE), ví dụ đô la, luật nửa kỳ (12 U.S.C. 4902(c)),
và độ bền trên Case-Shiller (đối chiếu, không lên hình).
  python3 episodes/ep005/model/model.py"""
import csv, datetime, json, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
RAW = os.path.join(EP, 'data', 'raw')
P = dict(downShare=0.10, termMonths=360, requestLtv=0.80, autoLtv=0.78, lenderLtvEarly=0.75, lookMonthsA=24, minFollowB=120,
         slowCutMonths=60, illustrativePrice=400000, rateMonthRule='latest calendar month whose weeks are complete '
         '(the next weekly date falls in a later month); monthly rate = mean of the weekly values dated in that month')
EPS = 1e-12
NAMES = {'owen': 'Owen', 'grace': 'Grace', 'victor': 'Victor'}  # tên chốt ở C2 (numbers.md); khoá = buyers của contract.json


def load(sid):
    out = {}
    for r in list(csv.reader(open(os.path.join(RAW, sid + '.csv'))))[1:]:
        if len(r) > 1 and r[1] not in ('', '.'):
            out[r[0]] = float(r[1])
    return out


def balance(rate, k, loan=None):
    """Dư nợ sau k kỳ (phần của giá mua), khoản trả đều 30 năm ở lãi `rate` (%/năm)."""
    L0 = 1 - P['downShare'] if loan is None else loan
    x = rate / 1200
    pay = L0 * x / (1 - (1 + x) ** -P['termMonths'])
    return L0 * (1 + x) ** k - pay * ((1 + x) ** k - 1) / x


def payment(rate, loan):
    x = rate / 1200
    return loan * x / (1 - (1 + x) ** -P['termMonths'])


def sched(rate, thr):
    return next(k for k in range(P['termMonths'] + 1) if balance(rate, k) <= thr + EPS)


def monthly_rates(wk):
    by = {}
    for d, v in wk.items():
        by.setdefault(d[:7] + '-01', []).append(v)
    rate = {m: statistics.mean(v) for m, v in by.items()}
    last = max(wk)
    nxt = (datetime.date.fromisoformat(last) + datetime.timedelta(days=7)).isoformat()
    complete = last[:7] + '-01' if nxt[:7] != last[:7] else max(m for m in rate if m < last[:7] + '-01')
    return rate, complete, by


def run(hpi, rate):
    months = sorted(hpi)
    idx = {m: i for i, m in enumerate(months)}

    def ltv(s, k):
        return balance(rate[s], k) / (hpi[months[idx[s] + k]] / hpi[s])

    def first_hit(s, thr=P['requestLtv']):
        return next((k for k in range(len(months) - idx[s]) if ltv(s, k) <= thr + EPS), None)

    A = [m for m in months if m in rate and idx[m] + P['lookMonthsA'] < len(months)]
    B = [m for m in months if m in rate and idx[m] + P['minFollowB'] < len(months)]
    l24 = {m: ltv(m, P['lookMonthsA']) for m in A}
    hit = {m: first_hit(m) for m in B}
    assert all(h is not None for h in hit.values())
    hv = [hit[m] for m in B]
    worst = max(B, key=lambda m: (hit[m], -idx[m]))  # hoà → tháng sớm nhất
    r = {'nA': len(A), 'firstA': A[0], 'lastA': A[-1],
         'shareA_ltv24_le80': sum(v <= P['requestLtv'] + EPS for v in l24.values()) / len(A),
         'shareA_ltv24_le75': sum(v <= P['lenderLtvEarly'] + EPS for v in l24.values()) / len(A),
         'nB': len(B), 'firstB': B[0], 'lastB': B[-1], 'medianB_months_to80': statistics.median(hv),
         'shareB_over60': sum(h > P['slowCutMonths'] for h in hv) / len(B),
         'maxB_months_to80': hit[worst], 'maxB_start': worst, 'minB_months_to80': min(hv),
         'shareB_le_sched80': sum(hit[m] <= sched(rate[m], P['requestLtv']) for m in B) / len(B)}
    return r, A, B, hit, l24, ltv, first_hit


def main():
    hpi, wk, cs, mspus = load('HPIPONM226N'), load('MORTGAGE30US'), load('CSUSHPINSA'), load('MSPUS')
    rate, rmonth, weeks = monthly_rates(wk)
    raw = {'hpi_first': min(hpi), 'hpi_last': max(hpi), 'rate_last_week': max(wk), 'rate_last_week_value': wk[max(wk)],
           'rate_month_latest': rmonth, 'rate_latest': rate[rmonth], 'rate_weeks_latest': len(weeks[rmonth])}
    partial = max(rate)
    raw['rate_month_partial'] = partial if partial != rmonth else None
    raw['rate_partial'] = rate[partial] if partial != rmonth else None
    raw['rate_weeks_partial'] = len(weeks[partial]) if partial != rmonth else None
    r_now = rate[rmonth]
    raw['sched80_months_latest'] = sched(r_now, P['requestLtv'])
    raw['sched78_months_latest'] = sched(r_now, P['autoLtv'])
    raw['midpoint_months'] = P['termMonths'] // 2            # 12 U.S.C. 4902(c): giữa kỳ khấu hao
    raw['midpoint_end_month'] = P['termMonths'] // 2 + 1     # "first day of the month immediately following"
    raw['sched78_before_midpoint'] = raw['sched78_months_latest'] < raw['midpoint_months']
    res, A, B, hit, l24, ltv, first_hit = run(hpi, rate)
    raw.update(res)
    s80 = [sched(rate[m], P['requestLtv']) for m in A]
    raw.update({'sched80_min_A': min(s80), 'sched80_max_A': max(s80),
                'rate_min_A': min(rate[m] for m in A), 'rate_max_A': max(rate[m] for m in A)})
    # luật nửa kỳ có bao giờ ràng buộc? (lịch 78% muộn hơn tháng 180 ở lãi nào trong dữ liệu)
    bind = [m for m in rate if sched(rate[m], P['autoLtv']) > raw['midpoint_months']]
    raw['n_months_sched78_after_midpoint'] = len(bind)   # mọi tháng có lãi PMMS (1971+), không chỉ tập A/B
    raw['midpoint_binding_rate_min'] = min(rate[m] for m in bind) if bind else None
    raw['midpoint_binding_last_month'] = max(bind) if bind else None
    # C-5: các tháng tập B > 60 tháng (S13.3) và đỉnh/đáy chỉ số quốc gia quanh đợt giảm giá
    months = sorted(hpi)
    slowB = [m for m in B if hit[m] > P['slowCutMonths']]
    raw.update({'slowB_n': len(slowB), 'slowB_first': slowB[0], 'slowB_last': slowB[-1],
                'slowB_years': sorted({int(m[:4]) for m in slowB})})
    pk = max((m for m in months if m < '2012-01-01'), key=lambda m: (hpi[m], m))       # đỉnh trước 2012
    tr = min((m for m in months if pk < m < '2015-01-01'), key=lambda m: (hpi[m], m))  # đáy sau đỉnh
    raw.update({'hpi_peak_month': pk, 'hpi_peak': hpi[pk], 'hpi_trough_month': tr, 'hpi_trough': hpi[tr],
                'hpi_peak_to_trough_pct': 100 * (hpi[tr] / hpi[pk] - 1)})
    # luật gỡ theo giá trị (bên cho vay/nhà đầu tư) và mốc 80% của điều lệ GSE: tham số luật, không tính
    raw.update({'value_removal_ltv_early': P['lenderLtvEarly'], 'value_removal_seasoning_years': 2,
                'gse_charter_ltv_max_uninsured': P['requestLtv']})
    # người mua minh hoạ (ILLUSTRATIVE), đều trong tập B (đủ >120 tháng theo dõi)
    med = raw['medianB_months_to80']
    owen = min(B, key=lambda m: (hit[m], -int(m[:4]), m))           # nhanh nhất (min); hoà → năm muộn nhất, rồi tháng sớm nhất
    grace = max((m for m in B if hit[m] == med), key=lambda m: m)     # đúng trung vị, tháng muộn nhất
    victor = raw['maxB_start']                                        # chậm nhất (max); hoà → sớm nhất
    buyers = {}
    for key, m in (('owen', owen), ('grace', grace), ('victor', victor)):
        buyers[key] = {'name': NAMES[key], 'purchaseMonth': m, 'rate': rate[m], 'monthsTo80Index': hit[m],
                       'sched80Months': sched(rate[m], P['requestLtv']), 'sched78Months': sched(rate[m], P['autoLtv']),
                       'ltvIndexAt24': l24.get(m), 'hpiChangeTo80Pct': 100 * (hpi[sorted(hpi)[sorted(hpi).index(m) + hit[m]]] / hpi[m] - 1),
                       'balanceAt80Share': balance(rate[m], hit[m])}
        i0 = months.index(m)
        path = [(k, 100 * (hpi[months[i0 + k]] / hpi[m] - 1)) for k in range(1, hit[m] + 1)]  # tới tháng đạt 80%
        kp, vp = max(path, key=lambda x: (x[1], -x[0]))
        kt, vt = min(path, key=lambda x: (x[1], x[0]))
        buyers[key].update({'indexPeakPct': vp, 'indexPeakMonth': kp, 'indexTroughPct': vt, 'indexTroughMonth': kt})
        for f, v in buyers[key].items():
            if f != 'name':
                raw[f'buyer_{key}_{f}'] = v
    # ví dụ đô la (ILLUSTRATIVE): giá ~ MSPUS mới nhất, làm tròn $400,000
    price = P['illustrativePrice']; loan = price * (1 - P['downShare'])
    raw.update({'mspus_quarter': max(mspus), 'mspus_latest': mspus[max(mspus)], 'ex_price': price, 'ex_down': price * P['downShare'],
                'ex_loan': loan, 'ex_payment_pi': payment(r_now, loan), 'ex_balance_at_sched80': balance(r_now, raw['sched80_months_latest'], loan),
                'ex_target80': price * P['requestLtv'], 'ex_target78': price * P['autoLtv'],
                'ex_extra_down_for_20': price * (1 - P['requestLtv']) - price * P['downShare'],
                'ex_sched80_years': raw['sched80_months_latest'] / 12, 'ex_sched78_years': raw['sched78_months_latest'] / 12})
    # độ bền trên Case-Shiller (cùng tháng mua 1991+, cùng luật); không lên hình
    cs91 = {m: v for m, v in cs.items() if m >= min(hpi) and m <= max(hpi)}
    rc = run(cs91, rate)[0]
    for k in ('medianB_months_to80', 'shareB_over60', 'maxB_months_to80', 'maxB_start', 'shareA_ltv24_le80', 'shareA_ltv24_le75', 'nA', 'nB'):
        raw['robust_cs_' + k] = rc[k]
    rounded = {}
    for k, v in raw.items():
        if isinstance(v, float):
            if k.startswith(('share', 'robust_cs_share')):
                v = round(v, 3)
            elif 'rate' in k:
                v = round(v, 3)
            elif k.startswith(('ex_', 'mspus')):
                v = round(v, 2) if 'payment' in k or 'balance' in k else round(v, 2)
            else:
                v = round(v, 4)
        rounded[k] = v
    out = {'params': P, 'raw': raw, 'rounded': rounded, 'buyers': buyers,
           'data': {'hpi': 'data/raw/HPIPONM226N.csv', 'rate': 'data/raw/MORTGAGE30US.csv', 'price': 'data/raw/MSPUS.csv',
                    'robust': 'data/raw/CSUSHPINSA.csv'}}
    os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
    json.dump(out, open(os.path.join(EP, 'out', 'model.json'), 'w'), indent=1, default=str)
    return out


if __name__ == '__main__':
    o = main()
    print(json.dumps(o['rounded'], indent=0, default=str))
