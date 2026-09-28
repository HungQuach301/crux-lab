# Episode 1 — script template (M1b, after the owner's M1 review: sổ gu G-007, G-008)

Every number is a `{{claimId}}` filled by `episodes/ep001/build.py` from `out/claims.json` (DX-H1); no digit is typed by
hand in narration. Lines: `sceneId | text`. Acts start with `@act`. Maya, Dan and Priya are ILLUSTRATIVE characters whose
numbers come from the data (HMDA 2025 medians for their loan size, FRED rates).

@act cold-open
# picture first: Maya's card shows October 2023 and $375,000 before the first word (claims on screen, spoken in act 1)
co-maya | Maya locked in {{r_old}}.
co-today | This week's average: {{r_today}}.
co-cost | Refinancing costs {{cost_maya}}.
co-question | So when does that money come back?

@act ident

@act act1
a1-lab | This is a lab for money decisions: we run the numbers on public data, and show every assumption.
a1-scope | US only. The rates here are history, not a forecast.
a1-rehook | By the end, you will see the exact rate drop that pays back a refinance like Maya's within {{hold36}} months, and how every rate drop since {{y1971}} actually played out.
a1-maya | She borrowed {{loan_maya}} in {{oct2023}}, the month the {{term30}}-year rate peaked.
a1-you | And if your own rate starts with a {{seven}}, the question is yours as well.
a1-q | First: is Maya's bill unusual?
a1-median | No. In {{y2025}}, the median closing cost on a rate-and-term refinance was {{cost_maya}}.
a1-hmda | Lenders must report every mortgage they make, and since {{y2018}}, the total loan costs of each one.
a1-count | That is the middle of {{n31}} such loans that lenders reported under the Home Mortgage Disclosure Act.
a1-spread | Half of those borrowers paid between {{cost_p25}} and {{cost_p75}}.
a1-terms | The bill is the closing costs: origination charges, discount points, the appraisal, title insurance, and the rest.
a1-turn | But that bill barely grows with the loan, so it lands much harder on some borrowers than on others.
a1-dan | Take Dan, who borrowed {{loan_dan}} in the same month, at the same rate.
a1-dan2 | On loans under {{band150}}, the median bill was {{share_small}} of the amount borrowed.
a1-dan3 | For Dan, that is {{cost_dan}}: fewer dollars than Maya, but a far larger share of his loan.
a1-priya | Priya borrowed {{loan_priya}}.
a1-priya2 | On loans of {{band750}} and more, the bill was {{share_big}}.
a1-priya3 | For Priya, that is {{cost_priya}}: about Maya's bill, on a loan nearly three times the size.
a1-save | What the bill buys is a lower payment. At today's rate, Maya's payment falls by {{sav_maya}} a month.
a1-rule | Divide the bill by that saving, and you get the answer most calculators give: {{be_simple_maya}} months.
a1-payoff | By that count, the refinance has paid for itself. Or has it?

@act act2
a2-q | Here is what that division leaves out.
a2-old | Maya's old loan already has {{k35}} payments behind it.
a2-reset | A refinance starts a fresh {{term30}} years, so the new loan pays the balance down more slowly than the old one would have.
a2-why | Early payments are mostly interest. Maya's old loan was just starting to pay down real principal, and the new one starts that schedule over.
a2-owe | So count what she still owes on each loan, month by month.
a2-gap | After {{be_simple_maya}} months, the new loan leaves her owing {{gap24}} more than the old one would have.
a2-real | So, counting what she still owes, break-even is not {{be_simple_maya}} months. It is {{be_bal_maya}}.
a2-thesis | Most calculators stop at the monthly saving. The balance keeps the score for longer.
a2-small | The smaller the cut, the bigger that gap.
a2-s025 | At a cut of {{s025}} points, the division would promise {{be_simple_025}} months.
a2-s025b | Counting the balance, Maya never catches up before her old loan would have been paid off.
a2-cliff | Below {{s05}} points, the fresh start can swallow the savings entirely.
a2-s10 | At a cut of {{s10}} point, the two answers nearly meet.
a2-s10b | The division says {{be_simple_10}} months; the balance says {{be_bal_10}}.
a2-dan | Now Dan. At today's rate, his payment falls by only {{sav_dan}} a month.
a2-dan2 | The division says {{be_simple_dan}} months. Counting what he still owes, it is {{be_bal_dan}}.
a2-dan3 | If Dan sells after {{y3}} years, the refinance leaves him {{net36_dan}} behind.
a2-dan4 | After {{y7}} years, he is only {{net84_dan}} ahead.
a2-priya | Priya saves {{sav_priya}} a month, and is even after {{be_bal_priya}} months.
a2-priya2 | If she sells after {{y3}} years, she is {{net36_priya}} ahead; after {{y7}}, {{net84_priya}}.
a2-maya | And Maya, the middle case: {{net36_maya}} ahead after {{y3}} years, {{net84_maya}} after {{y7}}.
a2-sell | Put another way: a house sold before the break-even month turns the refinance into a loss, and one kept past it turns it into a gain.
a2-payoff | Same rate, same month. The answer depends on the size of the loan, how old it is, and how long the house is kept.

@act act3
a3-q | The division also assumes today's rate is the last one. What happened in the real drops?
a3-all | We found every fall of at least {{s10}} point in the {{term30}}-year rate since {{y1971}}: {{n_eps}} of them.
a3-rules | In each, someone like Maya borrows at the peak and refinances in the first month the rate is {{s10}} point lower.
a3-costs | Closing costs use each year's median share; before {{y2018}}, lenders did not report them, so a fixed share is used and marked illustrative.
a3-range | Counting what was still owed, break-even took between {{beh_min}} and {{beh_max}} months.
a3-simple | The simple division would have said between {{behs_min}} and {{behs_max}}.
a3-young | Nearly the same, because those loans were only months old when the rate fell, so the fresh start cost them little. Maya's loan is {{k35}} payments old.
a3-81 | The biggest fall began after the peak of {{peak}} in {{y1981}}.
a3-81b | A refinance {{m81}} months later paid back in {{be81}} months, and the rate kept falling.
a3-priya | For Priya's loan size, every one of those drops paid back within {{behp_max}} months.
a3-dan | For a loan like Dan's, with the bill a bigger share, the same drops took between {{behd_min}} and {{behd_max}} months.
a3-turn | But in {{n_further}} of those drops, the rate fell another {{s10}} point before the first refinance had paid for itself.
a3-twice | Those borrowers met the same question twice, and a second refinance starts a new clock with a new bill.
a3-example | In the drop that began in {{ex_peak}}, the refinance came in {{ex_refi}}.
a3-example2 | It needed {{ex_be}} months to pay back, and the next drop of {{s10}} point came {{ex_gap}} months later.
a3-quiet | In the other {{n_nofurther}}, the first refinance was the one that mattered.
a3-23 | Maya's own drop began in {{oct2023}}. A cut of {{s10}} point first arrived in {{r23}}.
a3-23be | Refinancing then would have paid back in {{be23}} months.
a3-answer | So, how far do rates have to fall before a refinance pays for itself?
a3-answer2 | For a loan like Maya's, counting what is still owed, a cut of {{cut36_maya}} points pays it back within {{hold36}} months.
a3-answer3 | Dan would need {{cut36_dan}} points. Priya, {{cut36_priya}}.
a3-today | Today's cut is {{cut_today}} points. For Maya, that means ahead after {{be_bal_maya}} months, and behind if the house is sold before then.
a3-limit | That answer has limits. It leaves out taxes and any return on the cash, and it assumes the bill is paid up front, not added to the loan.
a3-median | It uses medians: half of borrowers paid more than {{cost_maya}}, and an offered rate can differ from the survey average.
a3-history | And it is history, not a forecast: nothing here says where rates go next.
a3-close | What history does show is the shape of the trade: a known bill up front, against savings and a balance that settle month by month.

@act method
m-rates | Method. Rates are Freddie Mac's weekly survey via FRED, checked against the Optimal Blue index since {{y2017}}.
m-drops | A drop counts when the monthly average falls at least {{s10}} point from a peak before rising {{s10}} point from its low.
m-costs | Costs are HMDA loan-level data from {{y2018}} to {{y2025}}: originated refinances, first lien, {{term30}}-year term.
m-chars | Maya, Dan and Priya are illustrative: each one's loan and bill are the medians for that loan size.
m-assume | Break-even counts payment savings plus the difference in balance still owed. Closing costs paid in cash; no taxes. Every figure is listed in the description.

@act outro
o-recap | A small cut needs a long stay. A small loan needs a bigger cut. And a young loan loses less to the fresh start.
o-you | If the rate on your own statement starts with a {{seven}}, the same three questions apply: how big the cut, how old the loan, and how long the stay.
o-close | The monthly saving is only half of the answer. The other half, just as real, is what is still owed.
o-sources | The sources are linked in the description, and the next decision is already on the bench.
