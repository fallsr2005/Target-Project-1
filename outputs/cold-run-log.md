# Run and environment log

## Existing environment run

- Date: October 19, 2026, Eastern.
- Environment: project .venv; Python and dependency versions in docs/environment-versions.txt.
- Inputs: data/model-inputs-step6.json, data/model-inputs-step7.json; historical records listed in the Step 4 ledger.
- Base export command: .venv\Scripts\python.exe data/export_final_base.py.
- Result: completed; 90 selected arithmetic checks pass and zero fail; partial base $115.65/share. Wrote root visible_output.json and outputs/final-readable-review.md.
- Test command recorded in prior Step 7: .venv\Scripts\python.exe -m unittest discover -s tests -v; 13 tests passed. These are AI-assisted arithmetic tests, not the course fixture or protected exercise.
- App startup: .venv\Scripts\python.exe -m streamlit run app.py --server.headless true --server.port 8765; server started at localhost:8765 on October 19. Manual visual/control verification remains pending.
- Streamlit AppTest: AppTest.from_file('app.py').run() had zero script exceptions. Changing capex to 12%, revolver to $0m and reserve to $5,000m produced 5 actual failed model checks and blocked valuation. Clicking Reset restored all six sliders to base and cleared the error alert. This is an automated UI test; record the separate live demonstration in Video 3.

## Cold environment

Fresh isolated environment completed on October 19, 2026. The initial ensurepip and package-index attempts hit permission/network restrictions; elevated retries succeeded without changing requirements.

- Python 3.13.14; Streamlit 1.66.0, NumPy 2.5.4, pandas 2.3.3, Matplotlib 3.11.2, SciPy 1.18.1, yfinance 1.7.0. Full versions: outputs/cold-environment-versions.txt.
- .venv-cold\\Scripts\\python.exe -m pip check: no broken requirements.
- .venv-cold\\Scripts\\python.exe data/export_final_base.py: 90 checks passed, 0 failed; partial base $115.65/share.
- .venv-cold\\Scripts\\python.exe data/conditional_price_case.py: conditional provider-close metrics generated; acceptance pending.
- .venv-cold\\Scripts\\python.exe -m unittest discover -s tests -v: 13 passed.
- .venv-cold\\Scripts\\python.exe -m streamlit run app.py --server.headless true --server.port 8766 --browser.gatherUsageStats false: server started at localhost:8766 and stopped cleanly.

The clean run checks reproducibility and arithmetic; it does not complete the course fixture, independent source check, protected exercise or final student validation.

## Actual stress and recovery

Step 6's preserved synthetic funding stress set capex to 40% of sales and revolver capacity to zero. It produced seven liquidity/funding check failures. The new bounded UI stress produced five failures; resetting cleared them and restored all controls. Actual recording remains the student's task.
- Final AppTest rerun at 2026-10-19 23:48 Eastern: base 0 exceptions/0 alerts; bounded stress 5 actual check failures and valuation blocked; Reset restored six base values and 0 alerts.
- Fresh environment attempt: `python -m venv .venv-cold` first failed during ensurepip with a Windows temporary-folder permission error; elevated retry succeeded. Sandboxed `.venv-cold\Scripts\python.exe -m pip install -r requirements.txt` failed because package index access returned no available NumPy versions. Elevated retry succeeded; declared dependencies installed.




## October 20 final audit cold run

Actual run 2026-10-20T01:34:05.922462-04:00. New .venv-audit; Python3.12.14; unchangedrequirements.txt installed successfully; pipcheckclean;56historychecks,20tests,94modelchecks and12publishedanswers pass. FullStreamlitAppTestbase/stress/reset:0exceptions,7realfailedstresschecks,resetrestoredcontrols/frozenfileunchanged. Basecapexhistoricalreferenceflagremains. Currenttarget-audit-0870f62eb5fd2ff7; conditionalbase$120.79. NoHTTPhealthcheckclaimedforthisnewenv. Fullcommands/stdout/stderr/initialfailures:outputs/audit-check-log.json; exactversions:outputs/audit-environment-versions.txt;UI:outputs/audit-ui-check.json.


## Confirmed source response and policy synchronization

The current student-decisions.json records the reported filing count/date, qualified share correction and unchanged watch/defer, plus approval of the conditional assumptions/monitoring/entry policy. Current source snapshot target-audit-b7be55e9cbc05931. Re-execution used the existing audited environment; numerical valuation inputs/results are unchanged. Latest commands/tests/AppTest are in outputs/audit-check-log.json; this does not assert another environment was newly created during this metadata revision.
