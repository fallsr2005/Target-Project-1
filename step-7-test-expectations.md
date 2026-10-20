# Step 7 test expectations recorded before execution

October 19, 2026. These AI-assisted implementation tests are not the student's protected exercise and do not replace the missing course known-answer fixture.

1. Each future FCFF should reconcile to operating cash flow minus capex plus modeled interest and the difference between income-statement tax and unlevered operating tax. Financing cash flows should not enter FCFF.
2. The elapsed estimate should have no present-value entry; each period-end exponent should equal actual calendar days after October 19 divided by 365, including the stub.
3. With all FCFF and terminal cash flows positive and fixed, increasing WACC should reduce enterprise value. This is conditional, not a claim for negative-cash-flow cases.
4. With positive sustainable NOPAT and terminal return on new capital greater than WACC, higher terminal growth should raise terminal value; when return on new capital is below WACC, growth may decrease value because the extra reinvestment outweighs growth. Inspect rather than force this result.
5. Increasing eligible cash by one USD million should increase equity value by one USD million; increasing debt by one USD million should decrease it by one USD million, with shares fixed. USD millions divided by million shares produces USD per share.
6. Reject invalid WACC/growth or reinvestment boundaries and nonpositive shares. A reverse calculation without an accepted, dated market price should report pending. With a documented test-only synthetic price generated from a known growth input, the solver should recover that input within tolerance; it must not be labeled an observed market expectation.
7. Low/base/high scenarios must rerun the same statement engine with a fixed common cutoff bridge and disclose changes. A scenario with failed financial feasibility checks must be flagged, not presented as validated.
