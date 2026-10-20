# Step 9 — operating sensitivities, provisional

Each one-factor case begins from a fresh copy of the same Step 6 base and runs through the financial and valuation engines. The shocks below change only FY2027. Operating profit uses the FY2027 statement; FCFF uses the same period. Valuation changes are partial per-share DCF changes with all other assumptions and the incomplete bridge held constant.

| One-at-a-time change | Units | Change in FY2027 operating profit ($m) | Change in FY2027 FCFF ($m) | Change in partial value/share ($) |
|---|---|---:|---:|---:|
| Sales growth +1.0 percentage point | percentage point | +56.7 | +61.6 | +1.39 |
| Cost ex D&A / sales +1.0 point | percentage point | −1,122.4 | −849.9 | −1.69 |
| SG&A / sales +0.5 point | percentage point | −561.2 | −426.5 | −0.84 |
| Capex / sales +1.0 point | percentage point | 0.0 | −1,122.4 | −2.22 |

The ranking metric is absolute change in partial value per share divided by the displayed input shock. It is a local ranking over these selected shocks, not a probability or universal importance score. Higher costs reduce operating profit, FCFF and value. Higher capex lowers FCFF/value without directly changing operating profit in the same year. Higher growth affects costs, margins, operating balances and investment together. Alternative shock sizes and ranges require evidence-based student review; no sensitivity validates the bounds.

An alternative narrower shock set (sales growth +0.5 point, cost ratio +0.5 point, SG&A +0.25 point, capex +0.5 point) was rerun. Ranking per one percentage point was unchanged: capex 2.22, SG&A 1.69, cost 1.69, sales growth 1.39 dollars/share. That unchanged local ranking follows near-linear model responses and does not establish that the tested ranges are economically justified. Values and actual inputs are in data/step9-sensitivities.json.

These one-at-a-time results are separate from the coherent low/base/high business scenarios and the WACC/terminal-growth grid. Results remain conditional because the base equity bridge, WACC, price and operating assumptions are unresolved.
