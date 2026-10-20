# Step 8 provisional application — October 19, 2026

This dated application follows `peer-policy-original.md`. Candidate classifications below were written before any candidate multiples were calculated. Student review and acceptance are pending. A broad peer set cannot be defended under the evidence collected within this deadline; do not treat this as a completed peer range.

## Candidate screen before multiples

| Candidate | Provisional classification | Business evidence available by cutoff | Main comparability issue / reason |
|---|---|---|---|
| Walmart | Contextual, not core | FY2026 10-K and Q2 FY2027 10-Q: https://www.sec.gov/Archives/edgar/data/104169/000010416926000091/wmtfy26annualreport-final.pdf and https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm | Broad U.S. retail and store/digital fulfillment overlap, but materially larger, grocery-heavy, global and e-commerce/advertising economics differ. Potentially useful context; not interchangeable with Target. |
| Costco | Contextual, not core | FY2026 10-K filed October 7, 2026: https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm | Merchandise retail overlap, but membership fees, warehouse-only format, international exposure and different fiscal year make profit model distinct. |
| Kroger | Exclude from core; contextual for food retail | FY2026 Q2 10-Q filed September 18, 2026: https://www.sec.gov/Archives/edgar/data/56873/000110465926108926/kr-20260815x10q.htm | Grocery-centered mix, thin margins, fuel and different store/economics and seasonal calendar are materially different. |
| Dollar General | Exclude from core; possible contextual comparison | Candidate would require cutoff-eligible Q2 filing and market/lease reconciliation before use. | Small-box value format, merchandise mix, scale, labor and store economics differ materially; not assessed as a numerical peer in this run. |

No company is approved as a core valuation peer in this provisional application. The filings cited support a business-model screen only; they are not a substitute for a contemporaneous valuation-date market and claims ledger. The identified SEC filings were available by the stated cutoff (filing dates shown by SEC filing detail). No transactions were used: no deal was established with sufficiently comparable control, synergies, standalone financials and date evidence. This is an explained omission, not an implied transaction range.

## One focused Target price check

Stock Analysis' historical table reports **Close $153.29** for TGT on October 19, 2026 and labels the close as 4:00 p.m. EDT; it identifies S&P Global Market Intelligence as the data source and says historical data can be split-adjusted. Source: https://stockanalysis.com/stocks/tgt/history/ (retrieved October 20, 2026; historical row: Oct 19, 2026). A separate earlier provider observation in `data/supplemental-evidence.json` is $153.24. The first is a provider-reported close, not a verified NYSE closing-auction record. Preserve both and the $0.05 discrepancy. Student acceptance is pending; calculations below are conditional illustrations under $153.29 and the provider's stated Close convention.

## Target's own conditional market multiples (not peer benchmarks)

The calculations below describe Target alone. They do not satisfy a peer range. TTM is FY2025 plus H1 FY2026 less H1 FY2025, using source values in `data/historical-reported.json`, all public before cutoff:

| Measure | Calculation | Conditional result | Caution |
|---|---|---:|---|
| TTM diluted EPS | $8.13 + $5.83 − $4.32 | $9.64/share | Sum of reported EPS is approximate because quarterly weighted-average diluted shares differ. Reconcile to TTM net income / contemporaneous weighted shares before relying on it. |
| TTM diluted P/E | $153.29 / $9.64 | 15.90x | Provider-close convention; not student accepted; old EPS and cutoff shares may not match. Reported EPS, no normalization. |
| TTM operating profit | $5,117m + $3,695m − $2,789m | $6,023m | Reported operating income. |
| TTM total cash-flow D&A | $3,134m + $1,597m − $1,558m | $3,173m | Cash-flow D&A; includes amounts whose classification to operating EBITDA is not yet reconciled. |
| TTM EBITDA proxy | $6,023m + $3,173m | $9,196m | Proxy only; not a fully reconciled operating EBITDA denominator. |
| Illustrative cutoff EV | $153.29 × 456.491m + $15,357m estimated debt − ($5,778.94m estimated cash − $1,000m provisional operating reserve) | $80,553.6m | Shares, cash, debt and reserve are estimates/proxies. Unknown claims/assets omitted, not zero. |
| Illustrative EV / EBITDA proxy | $80,553.6m / $9,196m | 8.76x | Not defensible as a core multiple until D&A, lease and cutoff EV components reconcile. |

The arithmetic is reproducible, but because Target's EBITDA D&A presentation and as-of bridge remain incomplete, EV/EBITDA is explicitly an exploratory proxy. A normalized result is not calculated: adjustment recurrence and cross-company consistency are unresolved. No peer multiple is calculated because the core set is empty, peer diluted shares/claims and same-date closes were not assembled and verified, and lease reconciliation is incomplete. No average or blended valuation is produced.

## Conditional reverse DCF and method disagreement

Using the existing base model and a temporary provider-close input of $153.29 gives reverse terminal growth of **4.983%**, conditional on the provisional 8.344% WACC, 12% incremental ROIC, estimated cash/debt/shares, $1bn reserve and incomplete bridge. The engine's result remains labeled `solved, conditional on assumptions and incomplete bridge`; the stored official market price remains null and the student's acceptance remains pending. A narrow solution near the 5% search ceiling is especially sensitive to terminal assumptions and omitted claims. This is not a market-implied fact or unique explanation.

The DCF's base partial estimate is $115.65/share, versus the provider close $153.29, a conditional gap of −24.56% relative to that close. This is not an actionable downside conclusion because bridge adjustments, WACC, terminal assumptions, cutoff balances and price acceptance remain open. The DCF emphasizes long-run margins, reinvestment and discount rate; the standalone P/E and EV/EBITDA proxy summarize a current market quote against backward-looking earnings. Their periods and unresolved accounting bases differ. They are not averaged.

## Disposition

Step 8 is only partially complete: a dated policy and pre-multiple screen exist, the provider close is recorded with the conflict, and standalone Target metrics are shown for transparency. A defensible peer-multiple range remains pending student review and reconciled peer evidence. No final recommendation is selected.
