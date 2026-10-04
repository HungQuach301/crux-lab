# Policy context: federal grad borrowing, 2026-27 (ep002)

Retrieved 2026-10-01. This file covers only the facts the viewer needs before the private variable-vs-fixed decision. It is not a full summary of the law.

**How each source was read (V-level):**
- **V1, direct fetch.** Full regulatory text pulled with curl from the eCFR versioner API (`/api/versioner/v1/full/2026-09-29/title-34.xml?part=685&section=...`, `Accept: application/xml`, compressed). eCFR reported Title 34 as "up_to_date_as_of 2026-09-29". Quotes are exact.
- **V2, WebFetch.** Read through WebFetch, where a small model extracts the passage. The quotes are probably exact but should get one look from the owner before going on screen.
- **V3, search snippet only.** The primary page itself could not be read (studentaid.gov, fsapartners.ed.gov, ed.gov, congress.gov, govinfo.gov and uscode.house.gov were blocked by the proxy, and federalregister.gov page views redirected to unblock.federalregister.gov). Read via search snippet; needs owner verification.

---

## 1. Grad PLUS ends for new borrowers on July 1, 2026

| Item | Value | Source | V |
|---|---|---|---|
| Cutoff | Starting July 1, 2026, grad and professional students cannot borrow Direct PLUS | 34 CFR 685.200(b)(2)(i) | V1 |
| Who is excepted | Students who were **enrolled in a program as of June 30, 2026** and had **a Direct Loan made for that program before July 1, 2026** | 685.200(b)(2)(ii)(A)-(B) | V1 |
| How long the exception lasts | The student's "expected time to credential": the **lesser of three academic years** or the time left in the program | 34 CFR 685.102(b) definition | V1 |
| How it is lost | The exception ends if the student withdraws or otherwise stops being enrolled in that program | 685.200(b)(3) | V1 |
| Rule effective date | July 1, 2026 (RISE final rule, 91 FR 23768, May 1, 2026, FR doc 2026-08556) | FR API `dates` field | V1 (API metadata) |

Verbatim quotes:
- 685.200(b)(2)(i): "Beginning on July 1, 2026, a graduate student or professional student may not borrow a Direct PLUS Loan."
- 685.200(b)(2)(ii): "...shall not be applicable to student borrowers during the period of the student's expected time to credential, if— (A) the student is enrolled in a program of study at an institution as of June 30, 2026; and (B) a Direct Loan was made for such program of study prior to July 1, 2026."
- 685.102: "Expected time to credential: From July 1, 2026, the expected time for a student to complete a program that is equal to or the lesser of— (i) Three academic years, as defined in 34 CFR 668.3; or (ii) The period determined by calculating the difference between— (A) The program length ... and (B) The period of such program of study that such individual has completed..."
- FR API, doc 2026-08556: "This final rule is effective on July 1, 2026."

**Correction to the brief.** The regulation requires *a Direct Loan* (any type, for example a Direct Unsubsidized loan) made for that program before July 1, 2026. It does **not** require a prior Grad PLUS loan. The test is enrollment as of June 30, 2026 plus a prior loan for the same program. The rule does not test the first-disbursement date of the new loan.

Sources:
- https://www.ecfr.gov/current/title-34/subtitle-B/chapter-VI/part-685/subpart-B/section-685.200
- https://www.ecfr.gov/current/title-34/subtitle-B/chapter-VI/part-685/subpart-A/section-685.102
- https://www.federalregister.gov/documents/2026/05/01/2026-08556/reimagining-and-improving-student-education-federal-student-loan-program-final-regulations

## 2. Direct Unsubsidized limits for graduate and professional students

| Item | New value (periods of enrollment starting on or after July 1, 2026) | V | Old value | V |
|---|---|---|---|---|
| Annual limit, graduate student | **$20,500** | V2 (proposed rule) / V3 (final) | $20,500 ($8,500 base + $12,000 additional) | V1 |
| Annual limit, professional student | **$50,000** | V2 / V3 | $20,500 | V1 |
| Aggregate limit, graduate student | **$100,000** | V2 / V3 | $138,500, including undergrad loans | V1 |
| Aggregate limit, professional student | **$200,000** | V2 / V3 | $138,500 | V1 |
| Lifetime limit, all federal student loans | **$257,500** (excludes Parent PLUS taken out for a child) | V1 | none | V1 |

Verbatim quotes:
- Old annual limit, 685.203(b)(2)(iii): "...beginning on or after July 1, 2012, and ending on or before June 30, 2026, ... may not exceed $8,500." 685.203(c)(2)(v): "In the case of a graduate or professional student for a period of enrollment through June 30, 2026, $12,000." Together these make $20,500. (V1)
- Old aggregate, 685.203(e)(3): "For a graduate or professional student for periods of enrollment beginning before July 1, 2026, $138,500, including any loans for undergraduate study..." (V1)
- Lifetime limit, 685.203(j)(2): "Effective July 1, 2026, the lifetime maximum aggregate amount of loans made, insured, or guaranteed under the Act that a student may borrow, shall be $257,500..." (V1) Under 685.203(j)(3), the same interim exception (enrolled as of June 30, 2026 plus a prior Direct Loan) applies to this cap during the expected time to credential.
- New limits, proposed rule 91 FR 4254 (Jan 30, 2026, doc 2026-01912), via WebFetch (V2): "...maintaining current borrowing limits of $20,500 for graduate students (but limiting borrowing to $100,000 in aggregate), and targeting higher loan limits of $50,000 annually ($200,000 in aggregate) to students enrolled in professional degree programs."
- New limits, final-rule wording, search snippet only (V3, needs owner verification): "A graduate student, who is not a professional student, for a period of enrollment beginning on or after July 1, 2026, may borrow up to $20,500 for any academic year under the Direct Unsubsidized Loan Program."

**Caveat (V1).** The live eCFR copy of 685.203 does **not** contain the new graduate or professional dollar amounts. Its Editorial Note says: "At 91 FR 23883, May 1, 2026, § 685.203 was amended in part by revising paragraphs (b)(2)(iv)(A)(1) through (C) and (e)(4) through (7); however, the amendment could not be completed because the paragraphs do not exist." The figures $20,500, $50,000, $100,000 and $200,000 are therefore confirmed only from the proposed-rule preamble (V2) and search snippets of the final rule (V3). The owner should check them against the FR PDF before they appear on screen: https://www.govinfo.gov/content/pkg/FR-2026-05-01/pdf/2026-08556.pdf (pages around 91 FR 23883).

Other points:
- Professional student classification, 685.203(l): a student in a program that awards both a graduate and a professional degree counts as a professional student if more than 50% of the credit hours count toward the professional degree. (V1)
- Schools may set lower limits, 685.203(m)(2)(i): "Beginning on July 1, 2026, an institution may limit the total amount of Direct Subsidized, Unsubsidized, and PLUS loans ... for a program of study for an academic year, as long as any such limit is applied consistently to all students enrolled in that program of study." (V1)
- Every federal loan is still capped by cost of attendance minus other aid, under 685.203(j)(1). (V1)
- The final rule's summary also mentions a less-than-full-time reduction of annual limits. The exact formula is UNKNOWN (not read).

## 3. Interest rate and fee for 2026-27

| Item | Value | Source | V |
|---|---|---|---|
| Direct Unsub (grad/prof) rate, first disbursed July 1, 2026 to June 30, 2027 | **8.07%, fixed for the life of the loan** | FR notice 91 FR 57581, Sept 10, 2026 (doc 2026-18493) | V2 |
| Treasury input | 10-year note auction on May 12, 2026; high yield 4.468%, rounded to 4.47% | same | V2 |
| Formula | 10-yr Treasury high yield at the last auction before June 1, **plus 3.6 points, capped at 9.5%** | 34 CFR 685.202(a)(8) | V1 |
| Check | 4.47 + 3.60 = 8.07 (below the 9.5% cap) | arithmetic | n/a |
| 2025-26 rate, for contrast | **7.94%** | table in the same FR notice | V2 |
| Direct PLUS 2026-27 (excepted borrowers only) | 9.07% (add-on 4.6, cap 10.5%) | same notice; 685.202(a)(9) | V2 / V1 |
| Origination fee, Direct Unsub | **1.057%** for loans first disbursed Oct 1, 2020 to before Oct 1, 2027 (the FY27 sequester fee equals FY26) | FSA electronic announcement, May 13, 2026 | V3 |

Verbatim quotes:
- 685.202(a)(8): "...determined on the June 1 preceding that period and is a fixed rate for the life of the loan. The interest rate is the lesser of— (i) A rate equal to the high yield of the 10-year Treasury note auctioned at the final auction held prior to the June 1 preceding the 12-month period, plus 3.6 percentage points, or (ii) 9.5 percent." (V1)
- FR 2026-18493 (V2): "On May 12, 2026, the United States Treasury Department held a 10-year Treasury note auction that resulted in a high yield of 4.468 percent, rounded to 4.47 percent." The table gives "8.07" for graduate/professional Direct Unsubsidized loans, and the prior-year row gives "7.94".
- The statutory fee in 685.202(c)(1)(vi) is "not to exceed 1 percent". The 1.057% figure includes the sequester add-on and was seen only in a search snippet (V3): https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2026-05-13/fy27-sequester-required-changes-title-iv-student-aid-programs

Sources:
- https://www.federalregister.gov/documents/2026/09/10/2026-18493/annual-notice-of-interest-rates-for-fixed-rate-federal-student-loans-made-under-the-william-d-ford
- https://www.ecfr.gov/current/title-34/subtitle-B/chapter-VI/part-685/subpart-B/section-685.202

## 4. Which dates decide who faces the choice

- **Interest rate: first-disbursement date** (685.202(a)(8)). A spring 2027 loan first disbursed in Jan 2027 falls in the July 1, 2026 to June 30, 2027 window, so the federal rate is 8.07% fixed. (V1 rule, V2 rate)
- **Loan limits and the end of Grad PLUS: period of enrollment and enrollment status.** The new limits apply to "periods of enrollment beginning on or after July 1, 2026" (685.203). A spring 2027 term starts after that date, so a **new** grad student (no exception) is capped at $20,500 per year in federal Unsub and has no Grad PLUS. (V1 framing; dollar amounts V2/V3)
- "New borrower" in practice means a student who either (a) was not enrolled in the program on June 30, 2026, or (b) had no Direct Loan made for that program before July 1, 2026. The rule does not define "new borrower" by the first-disbursement date of the new loan. (V1)
- How a loan period that straddles July 1, 2026 (for example, a summer 2026 period) is handled: UNKNOWN. The FSA Loan Limits FAQ PDF (fsapartners.ed.gov, May 2026) was blocked.

## Risky phrasings to avoid

- Do not say "Grad PLUS is gone for everyone." Continuing students with a pre-July 2026 Direct Loan for the same program keep it for up to 3 academic years, or less if fewer remain.
- Do not say "grad students are capped at $20,500 lifetime" or call $20,500 a new cut. It is the same annual figure as before. What changed is the aggregate (now $100,000) and the end of PLUS.
- Do not say "$50,000 for all grad students." That limit is for *professional* students only, and the eCFR text of the dollar limits has a codification gap (see Section 2 caveat).
- Do not imply "everyone now needs private loans." That is true only when cost of attendance minus other aid is above the federal limit, and schools or programs vary.
- Do not call the federal rate "variable." It is fixed for the life of the loan, and the rate resets yearly only for *new* loans.
- Do not compare 8.07% with a private APR without the 1.057% fee, and do not present 8.07% as an APR.
- Do not present the $257,500 lifetime cap as a graduate-only cap. It covers all federal student loans, minus Parent PLUS taken out for a child.
- Do not cite "studentaid.gov says..." for any figure here. None of these figures was read from studentaid.gov.
