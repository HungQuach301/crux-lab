#!/usr/bin/env python3
"""rent-buy-1: rent vs buy a home, replayed from every purchase month since 1991.

Two ILLUSTRATIVE people start in the same month s with the same cash. The buyer
buys a house priced at P (scaled to $400,000; every dollar result is linear in P)
whose value follows the FHFA national purchase-only index (an index, not one
house): 20% down + 3% closing costs, 30-year fixed loan at the month-s average of
the weekly Freddie Mac PMMS rate, owner costs 2.5%/yr of current value (tax 1.0,
insurance 0.5, maintenance 1.0), 6% selling cost at the end. The renter pays rent
that starts at y(s)*P per year and grows with CPI "Rent of primary residence".
Both spend the same each month: whoever pays less keeps the difference in a pot
that also holds the renter's 23% upfront cash. Main case: the pot earns nothing
(cash). Robustness: the pot earns the 3-month T-bill rate.

Buyer advantage after H years = buyer net equity (0.94*value - loan balance)
                                 - renter pot.
Positive = the buyer ends ahead. History, not a forecast.

Usage:  python3 calc.py                  -> prints every quantity (result.json → numbers)
        python3 calc.py --statement N    -> prints True/False for statements.json[N]
        python3 calc.py --all            -> prints every statement check
        python3 calc.py --render         -> prints the statement texts rebuilt from data
"""
import csv, json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

PRICE = 400000.0
DOWN = 0.20
CLOSING = 0.03
OWNER_COST = 0.025      # per year, share of current value
SELL_COST = 0.06
TERM = 360
YIELD_ANCHOR = 0.05     # gross rent / price per year at the anchor month (ILLUSTRATIVE)
ANCHOR = "2026-07"      # last month of the house price index
FIRST = "1991-01"       # first month of the house price index
HORIZONS = (5, 10, 15)
MAIN_H = 10
ERAS = {"1990s": ("1991-01", "1999-12"),
        "2002-2007": ("2002-01", "2007-12"),
        "2009-2016": ("2009-01", "2016-07")}
CPI_FILL = "2025-10"    # not published (federal shutdown); geometric mean of neighbours


def load(sid):
    out = {}
    with open(os.path.join(DATA, sid + ".csv")) as f:
        for r in csv.DictReader(f):
            v = r[sid].strip()
            if v not in ("", "."):
                out[r["observation_date"][:7]] = float(v)
    return out


def add(m, k):
    y, mm = map(int, m.split("-"))
    t = y * 12 + mm - 1 + k
    return "%04d-%02d" % (t // 12, t % 12 + 1)


def load_all():
    hpi = load("HPIPONM226N")
    cpi = load("CUUR0000SEHA")
    tb = load("TB3MS")
    weeks = {}
    last_week = None
    with open(os.path.join(DATA, "MORTGAGE30US.csv")) as f:
        for r in csv.DictReader(f):
            v = r["MORTGAGE30US"].strip()
            if v in ("", "."):
                continue
            weeks.setdefault(r["observation_date"][:7], []).append(float(v))
            last_week = r["observation_date"]
    rate = {m: sum(v) / len(v) for m, v in weeks.items()}
    # latest complete rate month: the month of the last week is complete only if
    # the next weekly date (+7 days) falls in the following month
    y, mo, d = map(int, last_week.split("-"))
    import datetime
    nxt = datetime.date(y, mo, d) + datetime.timedelta(days=7)
    rate_month_latest = last_week[:7] if nxt.month != mo else add(last_week[:7], -1)
    assert CPI_FILL not in cpi and add(CPI_FILL, -1) in cpi and add(CPI_FILL, 1) in cpi
    cpi[CPI_FILL] = (cpi[add(CPI_FILL, -1)] * cpi[add(CPI_FILL, 1)]) ** 0.5
    return hpi, cpi, tb, rate, rate_month_latest, last_week


def payment(loan, pct):
    x = pct / 1200.0
    return loan * x / (1 - (1 + x) ** -TERM)


def rent_yield(s, hpi, cpi, anchor_yield=YIELD_ANCHOR):
    return anchor_yield * (cpi[s] / hpi[s]) / (cpi[ANCHOR] / hpi[ANCHOR])


def window(s, H, hpi, cpi, tb, rate, anchor_yield=YIELD_ANCHOR, tbills=False, fixed_yield=False):
    e = add(s, 12 * H)
    loan = (1 - DOWN) * PRICE
    pay = payment(loan, rate[s])
    x = rate[s] / 1200.0
    y = anchor_yield if fixed_yield else rent_yield(s, hpi, cpi, anchor_yield)
    rent0 = y * PRICE / 12
    bal = loan
    pot = (DOWN + CLOSING) * PRICE
    buy_out = rent_out = 0.0
    for k in range(12 * H):
        m = add(s, k)
        value = PRICE * hpi[m] / hpi[s]
        out = pay + OWNER_COST / 12 * value
        rent = rent0 * cpi[m] / cpi[s]
        buy_out += out
        rent_out += rent
        pot += out - rent
        if tbills:
            pot *= 1 + tb[m] / 1200.0
        bal = bal * (1 + x) - pay
    value_end = PRICE * hpi[e] / hpi[s]
    equity = value_end * (1 - SELL_COST) - bal
    return {"start": s, "end": e, "rate": rate[s], "rentYield": y,
            "buyerMonth1": pay + OWNER_COST / 12 * PRICE, "rentMonth1": rent0,
            "priceChange": hpi[e] / hpi[s] - 1, "rentChange": cpi[e] / cpi[s] - 1,
            "equity": equity, "pot": pot, "balance": bal,
            "buyerOutlay": buy_out, "rentPaid": rent_out, "advantage": equity - pot}


def starts(H, hpi, cpi, tb, rate, tbills=False):
    out = []
    s = FIRST
    while add(s, 12 * H) in hpi:
        need = [add(s, k) for k in range(12 * H)] + [add(s, 12 * H)]
        ok = s in rate and all(m in hpi and m in cpi for m in need)
        if tbills:
            ok = ok and all(m in tb for m in need[:-1])
        if ok:
            out.append(s)
        s = add(s, 1)
    return out


def ym(m):
    import calendar
    y, mo = m.split("-")
    return "%s %s" % (calendar.month_name[int(mo)], y)


def r0(v):
    return int(round(v))


def compute():
    hpi, cpi, tb, rate, rml, last_week = load_all()
    q = {}
    q["hpi_last"] = max(hpi)
    q["cpi_last"] = max(k for k in cpi if k != CPI_FILL)
    q["tb_last"] = max(tb)
    q["rate_last_week"] = last_week
    q["rate_month_latest"] = rml
    q["rate_latest"] = round(rate[rml], 2)
    runs = {}
    for H in HORIZONS:
        ss = starts(H, hpi, cpi, tb, rate)
        w = [window(s, H, hpi, cpi, tb, rate) for s in ss]
        for r in w:  # cash case: advantage = renter's rent - buyer's outlay - upfront cash + equity
            alt = r["rentPaid"] - r["buyerOutlay"] - (DOWN + CLOSING) * PRICE + r["equity"]
            assert abs(alt - r["advantage"]) < 1e-6 and r["balance"] > 0
        runs[H] = w
        adv = [r["advantage"] for r in w]
        best = max(w, key=lambda r: r["advantage"])     # max() keeps the earliest on ties
        worst = min(w, key=lambda r: r["advantage"])
        h = "%dy" % H
        q["n_" + h] = len(w)
        q["first_" + h] = ss[0]
        q["last_" + h] = ss[-1]
        q["share_buyer_ahead_" + h] = round(100 * sum(a > 0 for a in adv) / len(adv), 1)
        q["median_adv_" + h] = r0(statistics.median(adv))
        q["best_start_" + h] = best["start"]
        q["best_adv_" + h] = r0(best["advantage"])
        q["worst_start_" + h] = worst["start"]
        q["worst_adv_" + h] = r0(worst["advantage"])
        q["n_renter_ahead_" + h] = sum(a <= 0 for a in adv)
    w10 = {r["start"]: r for r in runs[MAIN_H]}
    for tag in ("best", "worst"):
        r = w10[q["%s_start_10y" % tag]]
        q[tag + "_rate_10y"] = round(r["rate"], 2)
        q[tag + "_price_change_10y"] = round(100 * r["priceChange"], 1)
        q[tag + "_rent_change_10y"] = round(100 * r["rentChange"], 1)
        q[tag + "_equity_10y"] = r0(r["equity"])
        q[tag + "_pot_10y"] = r0(r["pot"])
    for name, (a, b) in ERAS.items():
        ws = [r for s, r in w10.items() if a <= s <= b]
        adv = [r["advantage"] for r in ws]
        q["era_%s_n" % name] = len(ws)
        q["era_%s_share" % name] = round(100 * sum(x > 0 for x in adv) / len(adv), 1)
        q["era_%s_median" % name] = r0(statistics.median(adv))
    # renter-ahead run (10y): first and last start month with advantage <= 0
    neg = [s for s, r in sorted(w10.items()) if r["advantage"] <= 0]
    q["renter_first_10y"] = neg[0]
    q["renter_last_10y"] = neg[-1]
    q["yield_median_10y"] = round(100 * statistics.median(r["rentYield"] for r in w10.values()), 2)
    q["yield_max_renter_ahead_10y"] = round(100 * max(w10[s]["rentYield"] for s in neg), 2)
    # robustness (10y)
    ss = starts(MAIN_H, hpi, cpi, tb, rate, tbills=True)
    tw = [window(s, MAIN_H, hpi, cpi, tb, rate, tbills=True) for s in ss]
    q["share_tbills_10y"] = round(100 * sum(r["advantage"] > 0 for r in tw) / len(tw), 1)
    q["n_tbills_10y"] = len(tw)
    for lab, yy in (("4pct", 0.04), ("6pct", 0.06)):
        ss = starts(MAIN_H, hpi, cpi, tb, rate)
        ww = [window(s, MAIN_H, hpi, cpi, tb, rate, anchor_yield=yy) for s in ss]
        q["share_yield%s_10y" % lab] = round(100 * sum(r["advantage"] > 0 for r in ww) / len(ww), 1)
    ss = starts(MAIN_H, hpi, cpi, tb, rate)
    ww = [window(s, MAIN_H, hpi, cpi, tb, rate, fixed_yield=True) for s in ss]
    q["share_fixedyield_10y"] = round(100 * sum(r["advantage"] > 0 for r in ww) / len(ww), 1)
    # implied starting rent yield range (all 10y starts)
    ys = [r["rentYield"] for r in runs[MAIN_H]]
    q["yield_first_10y"] = round(100 * w10[q["first_10y"]]["rentYield"], 2)
    q["yield_worst_10y"] = round(100 * w10[q["worst_start_10y"]]["rentYield"], 2)
    q["yield_min_10y"] = round(100 * min(ys), 2)
    q["yield_max_10y"] = round(100 * max(ys), 2)
    # month-1 cash gap: rent as % of the buyer's monthly outlay
    ratio = {s: r["rentMonth1"] / r["buyerMonth1"] for s, r in w10.items()}
    q["rent_to_outlay_min_10y"] = round(100 * min(ratio.values()), 1)
    q["rent_to_outlay_min_start_10y"] = min(ratio, key=ratio.get)
    # today (illustrative): the anchor rent yield, the latest complete rate month
    pay_today = payment((1 - DOWN) * PRICE, rate[rml]) + OWNER_COST / 12 * PRICE
    rent_today = YIELD_ANCHOR * PRICE / 12
    q["today_buyer_month1"] = r0(pay_today)
    q["today_rent_month1"] = r0(rent_today)
    q["today_rent_to_outlay"] = round(100 * rent_today / pay_today, 1)
    q["price"] = r0(PRICE)
    q["yield_anchor_pct"] = round(100 * YIELD_ANCHOR, 1)
    q["anchor_month"] = ANCHOR
    return q, runs


def money(v):
    return ("-$" if v < 0 else "$") + "{:,}".format(abs(v))


def render(q):
    """Statement texts rebuilt from fresh numbers. statements.json must match exactly."""
    Q = dict(q)
    for k, v in q.items():
        if isinstance(v, int) and ("adv" in k or "median" in k or "equity" in k or "pot" in k
                                   or "month1" in k or k == "price"):
            Q[k + "$"] = money(abs(v))
        if isinstance(v, str) and len(v) == 7 and v[4] == "-":
            Q[k + "@"] = ym(v)
    S = [
        # 1 answer: headline
        ("Across {n_10y} purchase months from {first_10y@} to {last_10y@}, a buyer who held a home "
         "for 10 years ended ahead of an identical renter in {share_buyer_ahead_10y}% of them "
         "(median {median_adv_10y$} ahead on a {price$} home), with no investing of the difference.",
         lambda q: q["share_buyer_ahead_10y"] > 50 and q["median_adv_10y"] > 0),
        # 2 answer: worst
        ("The worst start was {worst_start_10y@}: the home index rose only {worst_price_change_10y}% "
         "in 10 years and the buyer ended {worst_adv_10y$} behind the renter.",
         lambda q: q["worst_adv_10y"] < 0),
        # 3 answer: best
        ("The best start was {best_start_10y@}, at a {best_rate_10y}% mortgage rate: the index rose "
         "{best_price_change_10y}% and the buyer ended {best_adv_10y$} ahead.",
         lambda q: q["best_adv_10y"] > 0),
        # 4 answer: eras
        ("By start period: 1990s buyers were ahead in {era_1990s_share}% of 10-year windows, "
         "2002-2007 buyers in {era_2002-2007_share}%, and 2009-2016 buyers in {era_2009-2016_share}%.",
         lambda q: q["era_2002-2007_share"] < 50 < q["era_1990s_share"]
         and q["era_2009-2016_share"] > 50),
        # 5 answer: horizons
        ("Holding period matters: the buyer was ahead in {share_buyer_ahead_5y}% of 5-year windows "
         "and {share_buyer_ahead_15y}% of 15-year windows (worst 15-year start {worst_start_15y@}, "
         "still {worst_adv_15y$} ahead).",
         lambda q: q["share_buyer_ahead_5y"] < q["share_buyer_ahead_10y"] <= q["share_buyer_ahead_15y"]
         and q["worst_adv_15y"] > 0),
        # 6 answer: sensitivity
        ("The result leans on the starting rent: with today's rent set at {yield_anchor_pct}% of the "
         "price a year the 10-year share is {share_buyer_ahead_10y}%; at 4% it is {share_yield4pct_10y}%, "
         "at 6% it is {share_yield6pct_10y}%; if the renter's savings earn 3-month T-bill rates it is "
         "{share_tbills_10y}%.",
         lambda q: q["share_yield4pct_10y"] < q["share_buyer_ahead_10y"] < q["share_yield6pct_10y"]
         and q["share_tbills_10y"] <= q["share_buyer_ahead_10y"]),
        # 7 guess
        ("Most people expect buying to win almost always, because rent is 'thrown away'; "
         "in this replay the renter still came out ahead in {n_renter_ahead_10y} of {n_10y} "
         "10-year windows.",
         lambda q: 0 < q["n_renter_ahead_10y"] < q["n_10y"]),
        # 8 changesDecision
        ("Every 10-year start where the renter came out ahead fell between {renter_first_10y@} and "
         "{renter_last_10y@}, when starting rent was low next to the price (at most "
         "{yield_max_renter_ahead_10y}% a year, against a median of {yield_median_10y}%).",
         lambda q: q["yield_max_renter_ahead_10y"] < q["yield_median_10y"]
         and all(q["renter_first_10y"] <= s <= q["renter_last_10y"] for s in [q["worst_start_10y"]])),
        # 9 changesDecision: today's starting gap
        ("At the {rate_month_latest@} average rate of {rate_latest}%, the buyer's first month costs "
         "{today_buyer_month1$} against {today_rent_month1$} rent, so rent is {today_rent_to_outlay}% "
         "of the buyer's outlay: lower than at any of the {n_10y} replayed start months (lowest "
         "{rent_to_outlay_min_10y}%, {rent_to_outlay_min_start_10y@}).",
         lambda q: q["today_rent_to_outlay"] < q["rent_to_outlay_min_10y"]),
        # 10 claim-risk: index not a house
        ("The home is the national FHFA index, not one house: in the worst window the national "
         "index rose {worst_price_change_10y}%; a single home or city can do much better or worse.",
         lambda q: True),
        # 11 claim-risk: history, not a forecast
        ("History, not a forecast: the last window used ends in {hpi_last@}, the last month of the "
         "price index.",
         lambda q: add(q["last_10y"], 120) == q["hpi_last"]),
    ]
    out = []
    for t, pred in S:
        out.append((fmt(t, Q), pred(q)))
    return out


def fmt(t, Q):
    import re
    def rep(m):
        return str(Q[m.group(1)])
    return re.sub(r"\{([^{}]+)\}", rep, t)


def main():
    q, runs = compute()
    rendered = render(q)
    if len(sys.argv) >= 2 and sys.argv[1] in ("--statement", "--all"):
        with open(os.path.join(HERE, "statements.json")) as f:
            st = json.load(f)
        ns = [int(sys.argv[2])] if sys.argv[1] == "--statement" else [s["n"] for s in st]
        for n in ns:
            item = next(s for s in st if s["n"] == n)
            text, pred = rendered[n - 1]
            ok = (item["text"] == text) and pred and all(u in q for u in item["uses"])
            print(("%d " % n if sys.argv[1] == "--all" else "") + str(ok))
        return
    if len(sys.argv) >= 2 and sys.argv[1] == "--render":
        for i, (t, p) in enumerate(rendered, 1):
            print(i, p, t)
        return
    print(json.dumps(q, indent=1))


if __name__ == "__main__":
    main()
