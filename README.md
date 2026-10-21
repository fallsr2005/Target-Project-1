# Target Corporation - FIN 43900 Project 1

This folder is the working project. Keep project documents, data, results and local recordings inside it, in the folders below.

## Start here

| To review | Open |
| --- | --- |
| Recommendation, valuation range and monitoring conditions | [Decision memo](docs/Decision-Memo.pdf) |
| Original Edition A and the Edition B comparison | [Research evolution](docs/Research-Evolution.pdf) |
| Sources, tests, AI use, student evidence and remaining limitations | [Validation and AI use](docs/Validation-and-AI-Use.pdf) |
| Saved executed inputs and full results, without running code | [Visible output](visible_output.json) |
| A readable summary of the saved statements and valuation | [Readable results](outputs/final-readable-review.md) |
| Required files, video links and submission status | [Submission manifest](project-submission-manifest.csv) |
| Work still to finish | [Student completion checklist](docs/student-completion-checklist.md) |

## Current analysis

- Decision: **watch/defer**, for a buy-side team with no current Target position and a 12-24 month horizon.
- Valuation cutoff: **October 19, 2026, 4 p.m. Eastern**.
- Conditional base estimate: **$120.79 per share**; operating cases **$86.04-$153.12**.
- Estimated WACC: **8.09%**.
- Source snapshot: **target-audit-b7be55e9cbc05931**.

These are conditional model estimates. Cutoff cash/debt, depreciation, seasonality, financing timing and dilution remain qualified. Passing arithmetic checks does not establish that forecast assumptions are correct. Earlier Step 6/7 reports are retained as dated history; use the current documents and visible output for current figures.

## Folder guide

| Folder | Contents | GitHub |
| --- | --- | --- |
| `docs/` | PDFs, Markdown records, scripts and transcript files | Include |
| `data/` | Reported figures, assumptions, source caches and student-decision records | Include |
| `outputs/` | Executed results, test logs and preserved screenshot evidence | Include |
| `tests/` | The three model test modules | Include |
| `course-materials/` | Supplied instructions, original starters and published benchmark material | Include |
| `recordings/` | Local MP4 recordings; save Video 3 here too | Local only; ignored |
| `.local/` | Preserved temporary installer files and test caches | Local only; ignored |

Python environments (`.venv`, `.venv-audit`, `.venv-cold`) and `__pycache__` are local only and ignored. The only environment example to include is `.env.example`; it contains no credentials.

## Run the app

From this project's folder in PowerShell, use the existing tested environment:

```powershell
.\.venv-audit\Scripts\python.exe -m streamlit run app.py
```

Open the local address printed by Streamlit. Keep the terminal open while using the app; press Ctrl+C to stop it.

For a fresh checkout, use Python 3.12, create the environment and install the unchanged dependency ranges first:

```powershell
python -m venv .venv-audit
.\.venv-audit\Scripts\python.exe -m pip install -r requirements.txt
```

The model uses cached evidence and requires no API key. Exact tested dependency versions are recorded in [the environment record](outputs/audit-environment-versions.txt).

## Code guide

| File | Role |
| --- | --- |
| `analysis.py` | Shared entry point and saved-output export |
| `financial_engine.py` | Connected income statement, balance sheet and cash-flow statement |
| `valuation_engine.py` | FCFF, discounting, terminal value and signed equity bridge |
| `audit_analysis.py` | Published benchmarks, peer comparisons and sensitivities |
| `app.py` | Interface that calls the shared engine |

Keep these code files, `requirements.txt` and `visible_output.json` at the project root. The engine loads inputs from `data/`; the folder layout is part of the runnable project.

## Validation evidence

The recorded local run has 94 passing model checks, 20 passing tests, 56 selected historical arithmetic checks and 12 published DCF-answer comparisons. The logs preserve an automated liquidity stress with seven real failures, recovery and a fresh-environment run. These checks are separate from the student's protected exercise.

To run the test suite in a working checkout:

```powershell
.\.venv-audit\Scripts\python.exe -B -m unittest discover -s tests -v
```

To reproduce a result in a separate output file while retaining the submitted base:

```powershell
.\.venv-audit\Scripts\python.exe analysis.py --inputs data/model-inputs-step6.json --valuation-inputs data/model-inputs-step7.json --output outputs/reproduced-analysis.json
```

## Recording and submission status

| Item | Status |
| --- | --- |
| Video 1 | Local recording in `recordings/`; 2:34.923, within the 3-minute limit |
| Video 2 | Local recording in `recordings/`; 4:17.763, within the 5-minute limit |
| Videos 1/2 transcripts | Text entered from the scripts the student confirmed reading as written; detailed timestamp indices and independent audio comparison unverified |
| Video 3 and its transcript | Pending; maximum 5 minutes, opening with the required live app demonstration |
| Video URLs and access | Pending in the manifest |
| Protected changed-input record | Original prediction/snapshot and before/after evidence preserved; post-test restoration evidence and separate actual-decision/magnitude reconciliation remain open |
| Checkpoint and credited feedback | Required receipt/company-switch and actual credited-feedback evidence remain unverified as documented |

Brightspace's final file attachments are the three PDFs, three corrected transcript files and the completed manifest. The manifest also carries the repository and video links. See [the completion checklist](docs/student-completion-checklist.md) and [GitHub upload steps](docs/github-upload-steps.md). No grade or full-rubric completion is certified by this README.

Material AI assistance and actual student dispositions are documented in the validation record and [AI-use log](docs/ai-use-log.md). Edition A and preserved historical evidence remain unchanged.
