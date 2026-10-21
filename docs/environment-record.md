# Local environment and starter check

Recorded 2026-10-19 for Step 2. This is a technical setup check, not a clean-room cold run or financial-model validation.

- Host: Windows, 64-bit Python 3.13.14; isolated environment: project-root `.venv`.
- Supplied `requirements.txt` ranges were preserved. The full observed package list, including transitive dependencies and pip, is in `docs/environment-versions.txt`; it records this installation rather than replacing supported ranges.
- Direct package versions: numpy 2.5.4, pandas 2.3.3, matplotlib 3.11.2, scipy 1.18.1, yfinance 1.7.0 and streamlit 1.66.0; pip 26.1.2.
- `python -m venv .venv` created the interpreter but its initial `ensurepip` failed due to a temporary-folder permission error. An approved elevated rerun of `.venv\Scripts\python.exe -m ensurepip --upgrade --default-pip` succeeded. The first sandboxed pip install could not find packages and reported temporary-folder permission errors; an approved elevated rerun of `pip install --no-cache-dir -r requirements.txt` succeeded.
- `python -m pip check` in the environment reported no broken requirements. Imports of all six direct dependencies succeeded. A sandboxed import also succeeded but logged Matplotlib cache and temporary-directory cleanup permission warnings; an elevated rerun completed without those errors.
- `python -m streamlit run app.py --server.headless true --server.address 127.0.0.1 --server.port 18501 --browser.gatherUsageStats false` started the server. The local `/_stcore/health` endpoint returned HTTP 200 and `ok`. Streamlit AppTest ran `app.py` without app exceptions and showed the expected warning that `visible_output.json` is absent. Its first sandboxed run reported a temporary-directory cleanup error; the approved elevated rerun completed with no cleanup error and the standard bare-mode context warning. The test server was stopped afterwards.
- No model, financial data, valuation output or financial validation was created. A future fresh-environment cold run remains required.
- `.env.example` contains no variable or secret. `.gitignore` covers `.env`, `.env.*` (except the example), `.venv`, other named environments, common key files and Streamlit secrets; future credential formats still require review before sharing.
- The Edition A PDF-to-Markdown comparison remains pending: no available PDF text reader was detected during the audit. The files were not edited.

Pending: precise instructor-approved company-switch terms and any receipt requirement, actual applicable receipt, Brightspace deadline, analytic rubric, checkpoint instructions, Week 2 contamination catalog, weekly known-answer fixtures and detailed Weeks 5–6 lab instructions. The student has confirmed instructor approval of the company switch; no receipt is inferred.
