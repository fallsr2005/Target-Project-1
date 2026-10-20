# Target Corporation - FIN43900 Project1

Current corrected snapshot: target-audit-b7be55e9cbc05931. Valuation cutoff October19,2026 16:00Eastern; audit run 2026-10-20T01:33:58.534139-04:00. Conditional base$120.79, operatingcases$86.04-$153.12, WACC8.09%. Technical checks pass; Watch/defer, conditional assumptions and policy are confirmed; source finding and output disposition are recorded. Protected validation and access remain open. Old Step6/7 outputs are retained historical records, superseded for current figures.

## Run

PowerShell from this folder:

```powershell
.\.venv-audit\Scripts\python.exe -m streamlit run app.py
```

Fresh setup if the supplied local environment is absent: create a Python3.12 virtual environment, install requirements.txt, then run the app. No API key required; all material inputs and reference data are cached. Requirements ranges are preserved; outputs/audit-environment-versions.txt records exact tested versions. Local venvs are ignored and not part of the repository.

```powershell
python -m venv .venv-audit
.\.venv-audit\Scripts\python.exe -m pip install -r requirements.txt
.\.venv-audit\Scripts\python.exe analysis.py
.\.venv-audit\Scripts\python.exe -m unittest discover -s tests -v
```

analysis.py exports the actual base to visible_output.json. Alternate --inputs/--valuation-inputs require a separate --output; exploratory app changes do not overwrite the frozen base. Stop Streamlit withCtrl+C. Bounded controls affect FY2027 only; history and accounting logic are not editable in the UI. A real failed state blocks valuation. Reset restores base; the capex historical-reference flag remains.

## Inspect without running

Root visible_output.json contains complete inputs, statements, FCFF, itemized bridge, cases, WACC/g grid, conditional reverseDCF, contextual peer cells, sensitivities, checks and source hashes. outputs/final-readable-review.md renders all statement lines and major results. docs/decision-memo.md, research-evolution.md, validation-and-ai-use.md and their PDFs are current. Original EditionA/peerpolicy and historical reports are preserved. docs/audit-financial-conventions.md resolves superseded conventions.

## Architecture and evidence

financial_engine.py: articulated statements. valuation_engine.py: FCFF/DCF/bridge primitives. audit_analysis.py: frozenanalysis, benchmarks, peers and stress. analysis.py: export. app.py: render/shared-engine calls. data/: reported ledger, source caches and configuration. tests/:20unittestcases. course-materials/: supplied documents, actual Brightspace rubric and published coursecase.

No secret or credential is required. .env and virtualenvironments are ignored; env.example contains no live credentials. User handlesGitHub; noGitpublication is claimed. Cached data is for reproduciblecoursework; no data-license grant is asserted.

## Current evidence and limitations

94modelchecks,20tests,56selectedhistoricalarithmeticchecks and12publishedDCFanswers pass. Fresh .venv-audit run and real7failure/reset evidence are saved in outputs/audit-check-log.json and audit-ui-check.json. These do not validate estimates. Cash/debt/share dates differ; carrying-valueclaims, assetlives/D&A, seasonalworkingcapital and refinancing/leases remain economicrisks. WMT/COST are contextual, not a corepeerfairvaluerange. Price153.29 is conditionaldailyClose, not verifiedauction; student accepts the disclosed provider convention for conditional use; this is not official-auction verification.

## Still required from the student

See docs/student-completion-checklist.md: AI-off locked record, actual credited partner feedback/checkpoint evidence as required, checkpointreceipt, threerecordings and correctedtranscripts, realrepository/video links, instructoraccess and actualsubmissionreceipt. Current PDFs show these pending honestly; update and re-export after actual evidence is added. This project is not certified as meeting every rubric requirement.
