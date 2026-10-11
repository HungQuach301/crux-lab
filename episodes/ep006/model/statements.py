"""Tập 6 — kiểm câu diễn giải của hồ sơ topics-r1/machine/retire-1 (statements.json) trên dữ liệu tải lại (data/raw/).
Mỗi câu: tính lại các số từ dữ liệu qua model.py (không dùng calc.py hồ sơ), in True/False.
  python3 episodes/ep006/model/statements.py --statement N
  python3 episodes/ep006/model/statements.py --all"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

q = M.run()
r1 = lambda x: round(x, 1)  # noqa: E731
CHECKS = {
    1: lambda: q['windows_20y'] == 715 and q['first_start_20y'] == '1947-01-01' and q['last_start_20y'] == '2006-08-01'
       and r1(q['share_2pct_kept_up_20y_pct']) == 2.4 and q['windows_2pct_kept_up_20y'] == 17
       and q['kept_up_first_start_20y'][:4] == '1947' and q['kept_up_last_start_20y'][:4] == '1949',
    2: lambda: q['windows_25y'] == 655 and r1(q['share_2pct_kept_up_25y_pct']) == 0.0,
    3: lambda: round(q['median_inflation_20y_pct_per_year'], 1) == 3.1 and r1(q['median_real_value_2pct_payment_after_20y_pct']) == 80.7
       and r1(q['median_real_value_level_payment_after_20y_pct']) == 54.3,
    4: lambda: r1(q['worst_real_value_2pct_payment_after_20y_pct']) == 43.1 and q['worst_window_start_year_20y'] == 1966,
    5: lambda: q['latest_start'] == '2006-08-01' and q['latest_end'] == '2026-08-01'
       and r1(q['latest_window_real_value_2pct_payment_pct']) == 90.4 and r1(q['latest_window_real_value_level_payment_pct']) == 60.9,
    6: lambda: all(w['real_2pct_pct'] < 100 for w in q['windows'] if w['start'] > q['kept_up_last_start_20y'])
       and all(w['real_2pct_pct'] > w['real_level_pct'] for w in q['windows']),
    7: lambda: q['by_decade']['1990']['kept'] == 0 and q['by_decade']['2000']['kept'] == 0 and q['by_decade']['1990']['median_inflation_pct'] < 3
       and q['by_decade']['2000']['median_inflation_pct'] < 3,
    8: lambda: q['windows_2pct_kept_up_20y'] == 17 and q['kept_up_last_start_20y'] < '1950-01-01',
    9: lambda: round(q['median_inflation_20y_pct_per_year'], 1) == 3.1,
}

if __name__ == '__main__':
    st = json.load(open(os.path.join(M.EP, '..', '..', 'topics-r1', 'machine', 'retire-1', 'statements.json')))
    ns = [int(sys.argv[sys.argv.index('--statement') + 1])] if '--statement' in sys.argv else [s['n'] for s in st]
    ok = True
    for n in ns:
        v = bool(CHECKS[n]())
        ok &= v
        print(n, v) if '--all' in sys.argv else print(v)
    if '--all' in sys.argv:
        print(f'{sum(bool(CHECKS[n]()) for n in ns)}/{len(ns)} True')
    sys.exit(0 if ok else 1)
