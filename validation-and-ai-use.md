# Validation and AI Use

## Version and decision boundary

Current source snapshot target-audit-b7be55e9cbc05931; actual run 2026-10-20T02:24:42.075724-04:00. Valuation cutoff October 19, 2026, 4 p.m. Eastern; the actual run and export dates are retained in the evidence logs. Recommendation: watch/defer, confirmed by the student in this conversation on October 20. No Git commit or submission receipt is claimed; the student has also accepted the existing assumptions for conditional use and the monitoring/entry policy. Economic estimates remain qualified; the protected exercise is separate. Current conditional base $120.79, WACC 8.09%, operating cases $86.04-$153.12.

## Actual validation evidence

| Claim | Observed outcome | Evidence and limit |
| --- | --- | --- |
| Reported history | 56 selected arithmetic checks pass | data/historical-reconciliation.json; data/check_reported_history.py. Not a verification of every extracted cell. |
| Statements and valuation | 94 model checks pass; 0 fail | visible_output.json. Cash, debt, equity, FCFF, timing, scenario feasibility and signed bridge. Selected arithmetic invariants, not economic proof. |
| Test suite | 20 tests pass | outputs/audit-check-log.json. Statement articulation, WACC/g boundaries, reverse solver, seasonal estimate, share/claim/peer definitions, published fixture. |
| Published training case | 12 of 12 answers within 0.0001 | outputs/known-answer-reconciliation.json; original official course Lab 5 text cached in course-materials/public-course/. |
| Week 2 mini-case | NOPAT 112.5; FCFF 77.5; equity 820; per-share 8.20 match | Same shared FCFF and signed equity-bridge functions as Target. Separate from protected student exercise. |
| Highest-risk liquidity failure | 7 real engine checks fail under automated stress; valuation display blocked | outputs/audit-ui-check.json. FY2027 capex 12%, available facility zero, minimum cash 5000. Not an invented UI badge. |
| Reset/recovery | Six controls restored; model failures clear; saved output unchanged | Same UI log. Zero app exceptions in base, stress and reset. Base capex historical-reference flag remains because 4.50% exceeds observed 4.47%. |
| Fresh environment | Fresh .venv-audit; Python 3.12.14; pip check clean; export, tests and AppTest pass | outputs/audit-check-log.json and audit-environment-versions.txt. Dependencies installed from unchanged requirements. AppTest is a real Streamlit render; no separate HTTP health check is claimed for this fresh environment. |
| Independent student source check | Source finding confirmed by student report | Q2 cover: 454,296,736 common shares at August 21; accepts correction but qualifies October timing and dilution. Verbatim response and receipt time in data/student-decisions.json; wording was assisted. |
| Pre-run directional and Locked Changed-Input Record | Original prediction and before/after evidence entered; completion qualified | Student verbatim text and source/base snapshot preserved; screenshots and observed changes recorded below. Post-test reset proof and separate actual-decision/magnitude reconciliation remain open. |
| Independent disposition of an AI output | Correction accepted; use qualified by student | Original Q2 cover supports newer disclosed count. October shares and dilution remain estimates. Isolated effect about -$0.0014/share; watch/defer unchanged. |
| Recommendation, assumptions and monitoring | Watch/defer; conditional assumptions and policy accepted | Student analyst reviews quarterly within five business days; sales/margin/inventory/failure triggers accepted; consider initiation at 20% below base only after validation. Credited partner feedback remains separate. |

## Published-case reconciliation

The official course Lab 5 case starts FCFF at 100, grows 8%, 6%, 5%, 4%, 3%, discounts at 10%, uses terminal growth 3%, cash 50, debt 300 and 50 shares. Published results include explicit PV 448.4408, terminal PV 1176.4277, EV 1624.8685, equity 1374.8685, value 27.4974 and terminal share 0.7240. All twelve published comparisons pass tolerance 0.0001. The Target engine and fixture use the same discount and signed-bridge primitives, while the Target terminal uses its separately documented NOPAT/reinvestment convention. Source: [official Week 3 Lab 5](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md). This fulfills a published arithmetic benchmark, not the student's protected exercise.

## Source definitions and normalization

Historical financials use USD millions and issuer fiscal years. Source cells include source URL, period, filed date, definition and transformation in historical-reported.json and SEC fact caches. FY2025 ends January 31, 2026; current H1 ends August 1, 2026. The August-to-October interval is estimated; only later cash flows enter the DCF. FY2028 contains 53 weeks; next-year comparable growth removes the extra week. Cash/debt, shares, earnings and price dates are shown separately rather than called contemporaneous.

Reported EBIT 5117 less settlement gain 593 plus transformation charge 250 equals 4774, versus the rounded displayed adjusted 4775: the $1m rounding difference is retained. The $994m tariff refund reduced Q2 cost of sales and was received in cash; historical cash is not deleted. Future recurring profit does not repeat it. Transformation cost is challenged for recurrence rather than automatically excluded. Sources: [Target FY2025 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm); [Target Q2 FY2026 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm).

The daily TGT Close is $153.29 from the cached provider series; the $153.24 observation was before the closing timestamp. Neither establishes an official auction print. The provider chart timestamp labels the session start, not the closing trade. The student has accepted the documented provider convention for conditional model use; accepted_by_student is now true. This approval does not establish an official auction print. Latest reported cover shares are 454,296,736 as of August 21; 2.2m Q2 dilution is a proxy, not an award-by-award October count.

Risk-free yield 5.09% is the October 16 Treasury 10-year prior-day proxy. ERP 4.20% is the October 1 Damodaran estimate; differing underlying risk-free basis and archival availability remain qualifications. Weekly adjusted-return beta is 0.900829, based on 260 observations versus SPY through October 16, R-squared 0.1814. Debt cost 6%, 24% tax and book-debt capital weight are assumptions/proxies. Full lineage and URLs: docs/audit-financial-conventions.md and data/audit-2026-10-20/.

## Bridge and multiple definitions

The bridge adds estimated cutoff excess cash after $1000m operating reserve, deducts interest-bearing debt including finance leases once, and adds net other assets/claims -$306m. Components: life insurance +600; forward asset +25; deferred compensation -650; nonqualified pension -37; swap -106; accrued interest -138. These are historical carrying estimates, not verified October fair values. Operating rent remains in EBIT; operating lease liabilities are not separately deducted. Qualified pension surplus is not assumed freely distributable. Current/noncurrent tax accruals stay operating float, avoiding a duplicate financing deduction. Other operating balances and goodwill stay in EV. Classification choices and uncertainty remain explicit.

Peer-policy-original.md and peer-policy.md are preserved. The October 20 amendment was saved before the new peer computations and explains using EV/EBIT rather than unreconciled EV/EBITDA. Conventional EV proxies use common share/dilution definitions, finance leases in debt, operating leases excluded, a consistent proportional cash reserve, disclosed investments/NCI where relevant. P/E uses common net earnings and reconstructed TTM diluted weighted-share exposure, not a sum of rounded EPS. WMT and COST remain contextual, with stale balance/share dates and incomplete fair-value claims explicitly qualified. No core-peer median or transaction range is invented. See data/audit-peer-comparisons.json.

## Failures, corrections and cold run

Initial desktop access to the Windows Store-based older environment failed; a newly created bundled-Python environment was used. The first ensurepip attempt failed in external Temp; a project-local temporary directory resolved it. Two legacy tests initially failed because they expected the superseded share count and no market-price object; expectations were updated to verified cover shares and the then-unaccepted documented quote. After the student accepted the conditional provider convention, the unaccepted-price test now explicitly creates an unaccepted test state, retaining its safeguard rather than depending on a live user preference. The initial failures and commands are retained in audit-check-log.json. Dependency ranges were not loosened.

The prior October 19 cold-run record remains intact. This October 20 fresh environment re-exported the final output, ran history checks and all tests, then exercised the full Streamlit app, stress and recovery. This is the current version's cold-run evidence. No student recording is claimed. The final base differs from both $115.65 in old Step 7 and the intermediate $119.08 audit estimate because source/model corrections and the operating-tax-float classification are now applied consistently.

## Confirmed source finding and policy

The student reported the following source comparison in this conversation: “The cover reports 454,296,736 common shares outstanding as of August 21, 2026. I accept the correction from the older August 1 count because August 21 is the more recent disclosed date. However, I would qualify its use in the valuation: it is not an exact October 19 count, and it is not a diluted share count. The model’s additional dilution remains an estimate. This small correction does not change my watch/defer recommendation.”

The response was received on October 20; the exact time of opening the filing was not separately supplied. Source: Q2 Form 10-Q cover, linked above. The wording was prepared with assistance and then submitted by the student. This record preserves the reported finding and disposition without asserting independent authorship. The share-only effect, holding equity fixed, is approximately -$0.0014 per share and does not explain other audit valuation changes.

The student accepted the current assumptions as conditional estimates, not as proven facts or validated bounds. The accepted owner is the student analyst; reviews occur within five business days of quarterly release. Triggers are comparable sales non-positive twice, recurring margin below 4.5% twice, inventory growth exceeding sales by over 5 percentage points for two matching-season quarters, or any required accounting/source failure. The entry screen is 20% below updated base value, currently $96.63, with validation complete and operating evidence supportive; reaching that price alone does not justify buying.

## Protected Changed-Input Record - submitted student evidence

### Selected input and original snapshot

Student-selected input: FY2027 annual sales growth, 0.03 to 0.07 (3% to 7%; four percentage points). The user supplied the before and after screenshots; the assistant did not operate the slider for this exercise. All financial statement amounts below use USD millions; per-share values use USD/share.

Original student message preserved at **2026-10-20T03:55:12-04:00**. The source/input/base-output snapshot is **Target-Student-Prediction-and-Base-20261020-035512.zip**, SHA256 **636616b02d0444f397dbce978a015199b040fe9875abca98ccd058ba18cbe89e**. This is the actual archive-preservation time, not an invented earlier prediction or execution time. The archive and original text remain unchanged. No Git commit or instructor acceptance of this snapshot method is asserted.

### Original student prediction and explanation - verbatim

“i said that operating profit, fcff, and value per share should increase because sales increases and you should buy the stock now and wait to sell it until 2031 because all of those values are going to be higher with higher sales. i think operating profit will go up by 1000, i think that fcff will go up by 1000 and i think the share price will increase by 5 dollars all because sales grow”

The student later confirmed the intended financial amount as $1 billion and the per-share amount as $5 of estimated value, and clarified: “Operating profit, as originally written.” Those clarifications were received with/after the changed-run screenshots and are preserved separately; they were not inserted into or backdated over the original prediction.

The supplied reasoning is retained as stated: “all because sales grow.” The user subsequently asked for this existing explanation and evidence to be entered. No new explanation or numerical prediction has been authored on the student's behalf.

### Observed results from supplied screenshots

| Metric | Before | After | Observed change | Student predicted change | Units |
| --- | --- | --- | --- | --- | --- |
| FY2031 operating profit | 7096.3109 | 7371.8958 | 275.5849 | 1000 | USD millions |
| FY2031 FCFF | 4556.5304 | 4733.4831 | 176.9527 | 1000 | USD millions |
| Estimated value per share | 120.7930 | 126.5772 | 5.7842 | 5 | USD/share |

These are screenshot transcriptions and subtraction of displayed values, not a rerun or the student's own explanation of the prediction error. The displayed per-share headlines round to $120.79 and $126.58; the table uses the more precise displayed table values. The shown FY2031 accounting rows report pass. The images do not certify every hidden check or full-precision control value. The repeated course known-answer screenshots are retained as separate benchmark evidence, not as the changed-input outcome.

### Decision effect and remaining evidence

The student's predicted changed-case action was “buy the stock now and wait to sell it until 2031.” That statement is preserved as part of the exercise; it does not overwrite the separately confirmed base-case watch/defer recommendation or its 12-24 month horizon. A separately documented actual decision reconciliation and explanation of the magnitude differences have not been supplied. No assistant-generated conclusion is substituted for those fields.

Post-test Reset/restored-base screenshots have not yet been supplied. The earlier reset screenshots establish the starting baseline and are not relabeled as a later restoration. Exact execution/reset times are not reconstructed from attachment receipt times.

### Evidence locations and assistance

Original before images, after images, student clarification, index and preserved prediction/source archive: **outputs/changed-input-evidence/**. Machine-readable record: **data/protected-changed-input-record.json**. The same screenshot package is embedded as a ZIP attachment in this PDF; it is also available in the repository because some PDF previews do not expose attachments.

Assistant role for this entry: preserve original files/text, transcribe screenshots, subtract displayed numbers, organize this record and export the PDF. The assistant did not generate the student's prediction, run the selected change, supply the missing student outcome explanation or certify that the protected AI-off requirement is fully complete.

## AI-use and independent disposition register

| Surface/date | Material assistance | Evidence / student disposition |
| --- | --- | --- |
| Codex conversation, October 19 | Target Edition A preparation, research organization, model, tests, UI, analysis/document/recording drafts. VS Code screenshot shows GPT-6-Luna medium for the displayed turn only; earlier exact builds unverified. | Target A is preserved; this does not certify an early AI-off checkpoint. Student acceptance and original receipt pending. |
| Codex desktop, October 20; exact model build not exposed | Audit of local saved files, official course/filing retrieval, price/share/beta corrections, seasonality/lease/claim updates, tests and fresh run, app expansion, Assumption Review, updated documents/scripts/PDFs. | Actual role is material assistance. Assumption Review is not a classmate conversation; actual student response pending. |
| Corrected output: price/share acceptance | Old price logic did not require genuine student acceptance and used a superseded share count. | Evidence: Q2 cover August 21 count. Student accepts the share correction and qualifies October timing/dilution; provider Close is separately accepted for conditional use. Verbatim response retained in data/student-decisions.json. |
| Corrected output: benchmark and bridge | Missing published fixture found in official repo; same shared primitives tested. Tax accruals removed from financing deductions under continuing operating float. | 12 published answers pass; itemized signed bridge reconciles. Student independent judgment/disposition: PENDING. |

No partner identity, quotation, approval, student check, protected prediction, receipt, recording or instructor-access result has been fabricated. The neutral review heading does not alter this required provenance record. The student has supplied a corrected/qualified share-output disposition supported by the original filing. This records the student's reported comparison and decision; the response used the assisted example wording. It is not an assertion of unassisted authorship or completion of the protected exercise.

## Remaining requirements and limits

Watch/defer, conditional assumptions, monitoring owner/thresholds and entry screen are confirmed. The student source-check response and corrected/qualified output disposition are recorded. Remaining items: protected-record reset proof and separately documented actual-decision/magnitude reconciliation; actual credited partner-feedback evidence; checkpoint receipt/switch eligibility; Video 3 and its corrected transcript; detailed segment timestamp indices and video upload links for Videos 1/2; repository/video/PDF access; final manifest links and submission receipt. The actual rubric is now stored in course-materials/brightspace-project-1-rubric-provided.txt, replacing the old claim it was missing. The original long Step 5 record was overwritten before this audit; the dated reconstruction is not falsely described as original. No grade or complete compliance is guaranteed by these checks.


## Videos 1 and 2 - local recording evidence

The user supplied local MP4 recordings and confirmed that both updated scripts were read as written. Windows media metadata reports Video 1 at 154.923 seconds (2:34.923) and Video 2 at 257.763 seconds (4:17.763), within the respective 3- and 5-minute limits. Both files report 1920x1080 video and two-channel, 48 kHz audio. Their hashes, locations and measured durations are preserved in outputs/video-1-2-recording-check.json.

Transcript text was entered from the scripts on the basis of the student's explicit confirmation. The audio and on-screen content were not independently transcribed or audited. Detailed segment timestamps have not been reconstructed or invented. Local recordings do not establish uploaded video links or instructor access. Video 3 and its corrected transcript remain pending. The raw MP4s stay in the supplied FIN_43900 folder and are not added to the GitHub upload package.
