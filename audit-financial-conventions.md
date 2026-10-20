# Financial conventions - October 20 audit addendum

Current authoritative addendum for target-audit-b7be55e9cbc05931. Earlier dated scope/Step 4/Step 6/Step 7 notes are historical; current inputs and this addendum control revised calculations. As-of October 19, 2026 16:00 Eastern; retrieval and repair October 20. USD millions; shares millions; value/share USD. Facts from filings available by cutoff; forecasts and unreported balances are separately classified.

## Primary source index

- [Target FY2025 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm); [Target Q2 FY2026 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm).
- [Target Q2 release](https://corporate.target.com/press/release/2026/08/target-corporation-reports-second-quarter-earnings).
- [Walmart Q2 filing](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm); [Walmart annual](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm).
- [Costco annual](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm).
- [Treasury par yields](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026); [Damodaran ERP](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm).
- Provider Close series: https://query1.finance.yahoo.com/v8/finance/chart/TGT (also WMT, COST, SPY); full request URL and hashes in data/audit-2026-10-20/retrieval-log.json. Daily Close is not a verified NYSE auction. Adjusted Close used for return regression includes split/dividend adjustments.
- [Official course Lab 5](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md); locally cached course files are not invented answer keys.

## Operating construction and timing

FY2026 full-year sales estimate minus reported H1 determines unreported H2. Prior-year Q3/H2 sales and elapsed 79/91-day fraction allocate 39.3692% of remaining sales to the elapsed estimate; merchandise and SG&A cash costs follow that sales split. D&A/capex use 79/182 time share. Prior-year seasonal inventory/payable ratios interpolated into Q3 produce estimated October inventory/payables, rather than moving directly toward year end. These remain assumptions; they are not current reported balances. Future stub ends January 30, 2027; five full years end FY2031. Actual/365 end-period discounting; elapsed cash flows excluded from future PV. FY2028 53-week increment does not permanently inflate later comparable growth.

Cost excluding D&A, SG&A and total D&A produce EBIT. One total D&A is allocated 16.5% to cost of sales and the rest separately; the allocation is a proxy, not a verified filing split. PP&E equals opening PP&E plus capex minus depreciation. No cohort asset-life schedule or separate amortization study has been completed. Other operating assets/accruals scale with comparable sales; unclassified residuals remain visible and held constant. Constant tax balances imply continuing operating tax float; no extra financing deduction.

Interest, tax, cash, debt and equity articulate. $136m annual finance-lease principal is an approximation from current debt less the remaining bond cohort, prorated by days, with no new finance leases. It is included within debt repayment, not a second cash outflow. Bond maturity groups and exact intra-year dates are approximations; FY2031 zero is an assumption for the undisclosed thereafter group. New borrowing, minimum cash and future dividends remain policies. Facility disclosed $4bn expires August 2031. Existing interest rates/lease allocation and 5% forecast revolver rate versus 6% WACC marginal cost are separate assumptions, not interchangeable observations. Repurchases assumed zero; no claim that future shares are known.

## Normalization

5117 - 593 + 250 = 4774 versus issuer displayed adjusted EBIT 4775 due rounding. Preserve the $1m gap. The settlement gain is removed for a recurring comparison; transformation is shown both ways and challenged for recurrence. Future cost ratios are assumptions, not a claim all restructuring vanishes. The Q2 tariff refund 994 reduces reported cost of sales and was received; remove a repeat from the forecast, not actual historical cash. TTM reported EBIT6023 minus994=5029 is a separate diagnostic, not a forecast or an after-tax normalized P/E.

## Cash, debt, claims and shares

| Bridge item | Signed USDm | Basis |
| --- | --- | --- |
| Company-owned life insurance | 600 | FY2025 10-K Note 13; January carrying value used as cutoff estimate; operating forecast excludes its investment returns |
| Prepaid forward asset | 25 | Q2 FY2026 10-Q Note 5; August fair-value asset; financing-linked deferred-compensation hedge |
| Deferred compensation | -650 | FY2025 10-K Notes 21 and 24; January claim estimate; cash settlement of opening earned compensation not separately forecast |
| Unfunded nonqualified/international pensions | -37 | FY2025 10-K Note 25; January shortfall, pretax carrying proxy; full deduction conservative to assumed tax shield |
| Net interest-rate swap liability | -106 | Q2 FY2026 10-Q Notes 5 and 8; August derivative liability separate from carrying debt; no duplicate derivative cash flow in FCFF |
| Accrued interest | -138 | FY2025 10-K Note 15; January estimate for opening accrued financing interest; future interest excluded from FCFF |

Net other asset/claim adjustment **-306**. Estimated cutoff cash 5421.205971, retain1000, excess 4421.205971; estimated debt 15327.564384. These start from August reported cash5411/debt15357. Current shares454.296736m are the latest reported August21 cover count; 2.2m Q2 incremental weighted-average diluted/basic difference is a proxy. Denominator456.496736m is an estimate; January awards and October issuance/exercises could differ.

Tax accruals440 current and340 noncurrent are continuing operating float under this forecast's constant-balance/cash-tax convention. An intermediate -1086 claim total deducted them as financing; final -306 removes that double deduction. Immediate settlement without replacement float would be a separate downside, approximately780/456.496736 per share, not base. Operating reserves/deferred occupancy/DTL remain operating; goodwill and operating assets stay inEV. Qualified pension surplus231 is restricted, no extra cash addition. Dividends payable belong to the same common owners; no separate non-common deduction. No preferred/NCI line is shown in Target consolidated statements. Operating rent remains inEBIT; no operating-lease debt deduction. Finance leases are in total debt once. Life-insurance carrying value and pension/compensation claims are historical pretax proxies; cash settlement/tax/fair-value uncertainty remains. The bridge is fully specified under these conventions, not all balances independently observed at cutoff.

## Discount, terminal and comparisons

Beta0.900829 from260 weekly Friday adjusted simple-return observations versusSPY throughOctober16; OLS intercept included, R-squared0.181423. RF5.09% October16 priorbusinessday, ERP4.20% October1 with differing underlyingRF convention, debtcost6% assumed, equityweight81.9321% using price timesbasicshares/bookdebt. WACC8.0941%. Terminalg2%, incrementalROIC12%, reinvestg/ROIC; checks requireWACC>g, positiveROIC andvalidrates. TerminalPV is75.1194% ofEV.

EV/EBIT usesreportedTTMEBIT; equityP/E usescommonNI dividedbyreconstructedweightedsharetime. Annual+currentinterim-priorinterim reconcilesTGT/WMTTTM; Costco latestannual52weeks. EV proxy addsdebt/financeleases,NCI/derivativeswherepresent, subtractseligiblecash/disclosedinvestmentassets. Targetreserve/salesratioappliedconsistently; reservedcashisnotmeasuredpeeroperatingneed. Additionalclaims/fairvaluesnotfullymappedacrossallthree; conventionalEVproxythereforedoesnotpretendtobecompleteDCFbridge. Earningsdatesandsharedatesdifferandarevisible. WMT/COSTcontextualonly; noforcedmedian. Noqualifyingtransactionvaluationwascompleted. Sourcefactcells,periods,accessionsandtransformationsareinpeerJSON.

## Data handling

Runs use cached inputs without API keys. Raw downloads and SHA256 retrieval logs preserve lineage; post-cutoff retrieval is disclosed, not backdated. No public-data redistribution license grant is asserted. Supplied files and templates remain in course-materials. Original Edition A and peer policy are preserved; current exports and historical step reports must not be confused. No Git or external publication was performed.
