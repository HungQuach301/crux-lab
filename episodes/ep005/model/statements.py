"""Tập 5 — kiểm câu diễn giải của hồ sơ topics-r2/machine/debt-2 (statements.json) trên dữ liệu tải lại (data/raw/).
Mỗi câu: tính lại các số từ dữ liệu (qua model.py, không dùng calc.py hồ sơ) và in True/False.
  python3 episodes/ep005/model/statements.py --statement N
  python3 episodes/ep005/model/statements.py --all"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


def quantities():
    hpi, wk = M.load('HPIPONM226N'), M.load('MORTGAGE30US')
    rate, rmonth, _ = M.monthly_rates(wk)
    r = {'rate_month_latest': rmonth, 'rate_latest': rate[rmonth],
         'sched80_months_latest': M.sched(rate[rmonth], 0.80), 'sched78_months_latest': M.sched(rate[rmonth], 0.78),
         'hpi_first': min(hpi), 'hpi_last': max(hpi)}
    res, A, B, hit, l24, ltv, first_hit = M.run(hpi, rate)
    r.update(res)
    r['_later75'] = all((first_hit(m, 0.75) is None) or first_hit(m, 0.75) >= hit[m] for m in B)
    months = sorted(hpi)
    r['_lastA_plus24'] = months[months.index(r['lastA']) + 24]
    return r


def r3(x):
    return round(x, 3)


CHECKS = {
    1: lambda q: q['rate_month_latest'] == '2026-09-01' and r3(q['rate_latest']) == 6.862 and q['sched80_months_latest'] == 99
       and q['sched78_months_latest'] == 114 and round(q['sched80_months_latest'] / 12) == 8 and q['sched78_months_latest'] / 12 == 9.5,
    2: lambda q: q['nB'] == 307 and q['firstB'] == '1991-01-01' and q['lastB'] == '2016-07-01' and q['medianB_months_to80'] == 23
       and r3(q['shareB_over60']) == 0.147 and q['maxB_start'] == '2005-10-01' and q['maxB_months_to80'] == 112,
    3: lambda q: r3(q['shareA_ltv24_le80']) == 0.586 and q['nA'] == 403 and q['firstA'][:4] == '1991' and q['lastA'][:4] == '2024'
       and r3(q['shareA_ltv24_le75']) == 0.156 and q['shareA_ltv24_le75'] < q['shareA_ltv24_le80'],
    4: lambda q: q['_lastA_plus24'] <= q['hpi_last'],                       # chỉ dùng tháng đã quan sát
    5: lambda q: 60 < q['sched80_months_latest'] <= 120,                     # "most of a decade" theo lịch
    6: lambda q: q['sched80_months_latest'] >= 96,                           # "8+ years"
    7: lambda q: abs(q['medianB_months_to80'] - 24) <= 3 and round(1 / q['shareB_over60']) == 7
       and q['shareA_ltv24_le75'] < q['shareA_ltv24_le80'],
    8: lambda q: q['minB_months_to80'] < q['medianB_months_to80'] < q['maxB_months_to80'],
    9: lambda q: q['maxB_months_to80'] > 60,                                  # có tháng chậm dù chỉ số quốc gia (đại diện cho "khác biệt")
    10: lambda q: q['_later75'],                                              # ngưỡng 75% không bao giờ đến sớm hơn 80%
    11: lambda q: q['sched80_months_latest'] < q['sched78_months_latest'],
    12: lambda q: q['medianB_months_to80'] == 23,
    13: lambda q: r3(q['shareA_ltv24_le75']) == 0.156,
    14: lambda q: q['maxB_start'] == '2005-10-01' and q['maxB_months_to80'] == 112 and r3(q['shareB_over60']) == 0.147,
    15: lambda q: q['sched80_months_latest'] < q['sched78_months_latest'],
    16: lambda q: q['lastB'] < q['lastA'] and q['nA'] > q['nB'] and q['_lastA_plus24'] == q['hpi_last'],
    17: lambda q: int(q['hpi_last'][:4]) - int(q['hpi_first'][:4]) >= 20,
}


if __name__ == '__main__':
    q = quantities()
    if '--all' in sys.argv:
        res = {n: bool(f(q)) for n, f in CHECKS.items()}
        for n, v in res.items():
            print(n, v)
        print('True', sum(res.values()), '/', len(res))
    else:
        print(bool(CHECKS[int(sys.argv[sys.argv.index('--statement') + 1])](q)))
