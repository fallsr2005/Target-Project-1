# Target Project 1: prompts for Codex in VS Code

This guide is based on all 17 files supplied with the request. Build the project locally in VS Code first; you will add the finished files to GitHub yourself when needed. A GitHub repository is not needed to begin. Step 0 organizes the local working files, then Steps 1-14 cover the analysis, application, validation, and submission. Paste one numbered prompt at a time. Review each result and complete the student work identified at that stage before proceeding.

**Project location:** Use a local working folder named `target-finance-ai-project` and open it in VS Code. It can be an ordinary folder with no Git setup. Throughout this guide, "project root," `docs/`, `data/`, `tests/`, `outputs/`, `README.md`, and application files refer to locations inside this Target folder. If you choose to work inside an existing repository, keep its other files and configuration intact. Repository creation, staging, and uploading are your later manual steps; Codex should not perform them as part of these build prompts. Required historical snapshots and validation records still need to be preserved at the time they occur; an eventual upload cannot retroactively establish a pre-run prediction.

The separate analytic rubric, Edition A checkpoint instructions, Week 2 contamination catalog, weekly known-answer fixtures, and detailed Weeks 5–6 lab instructions were referenced but not supplied. Obtain them from the course site and add them to `course-materials/`. The enforced deadline and checkpoint window come from Brightspace.

## Before using the project prompts

**Company-switch update, October 19, 2026:** The student reports that the instructor permits a new Target Edition A after the original Gallagher baseline. Use `Target-Edition-A.pdf` and its editable counterpart `Target-Edition-A.md` under that permission. The documents are titled "Target - Edition A" and open with the decision and initial view; preparation/status labels are omitted from the title area and footer. Preserve the actual file/version history and Gallagher's original submission and receipt; do not relabel the new Target baseline as an earlier AI-off submission or invent a Target receipt. Freeze the reviewed Target baseline before subsequent work and describe the switch transparently in research evolution. The general course rule below is retained for context; the instructor's actual approved company-switch terms govern this exception. The numbered project steps are unchanged.

The supplied AI Boundary Card requires a first successful Brightspace Edition A receipt before valuation-specific AI assistance. If you have that receipt, preserve the submitted PDF unchanged and record its actual receipt/attempt identifier and timestamp. If you do not, complete the checkpoint through the permitted non-generative route before using these prompts. If project-specific AI was used too early, the card's recovery route is to preserve the actual work, record the affected use, and contact the instructor/TA; a reconstructed supposedly earlier Edition A is not acceptable history.

Project 1 still requires PDFs. The shared checklist's Markdown-only exception and Project 2's opening announcements are expressly for Project 2/capstone as stated there; do not import them as Project 1 requirements. Keep content-equivalent records in the repository as well.

The finished project is a locally runnable, semi-adjustable valuation workbench for a buy-side team that holds no position in Target. Its decision is initiate, watch/defer, or do not initiate, supported by a defensible range, conditions, and reversal/monitoring triggers. A Streamlit app fits the supplied starter. Hosting and visual polish are optional.

## 0. Set up the local Target working folder

Open a local Target working folder in VS Code. Then paste the prompt below into Codex chat. It organizes local project files and reads the supplied sources from your computer. You will decide when to add the completed files to a repository later.

```text
Build my Target finance project locally in the folder open in VS Code. I will add the finished files to GitHub myself later. Complete local file setup only in this stage.

Inspect the workspace path and applicable instructions. Use the opened Target working folder as the project root. If the workspace is actually my Gallagher project root, create a dedicated target-finance-ai-project subfolder for all new Target work rather than changing Gallagher files.

Keep all project writes inside the Target folder. Preserve other projects and any enclosing repository. Do not create a repository, initialize Git, change remotes or Git settings, stage files, commit, or upload. Do not make GitHub authentication a prerequisite for local work.

Create course-materials/, docs/, data/, tests/, and outputs/ inside the Target folder.

Copy these exact files from C:\Users\rocco\Downloads into course-materials/, preserving the originals:
env.example
gitignore.txt
README-template.md
analysis.py
app.py
requirements.txt
visible_output.example.json
decision-memo-template.md
project-submission-manifest-template.csv
project-transcript-template.txt
research-evolution-template.md
validation-and-ai-use-template.md
AI-BOUNDARY-CARD.md
STARTER-HELP-LADDER.md
major-project-student-checklist.md
project-1-annotated-exemplar-and-non-example.md
project-1-corporate-finance-application.md

Copy the working analysis.py, app.py, and requirements.txt to the Target project root. Copy gitignore.txt as the Target folder's .gitignore and env.example as its .env.example. Use README-template.md as the starting Target README.md, clearly marking the analysis as unfinished. Inspect existing files first and preserve meaningful existing work rather than overwriting it. Preserve original starter copies in course-materials/. Keep visible_output.example.json as an example; do not create a fake executed visible_output.json.

Copy Target-Edition-A.pdf and Target-Edition-A.md unchanged from:
C:\Users\rocco\Documents\Codex\2026-10-19\i-am-in-a-finance-and-27\outputs
into the Target project's docs/ folder. Also copy Target-Project-1-Codex-Prompt-Guide.md from that source folder into docs/ so I have the remaining prompts available.

If a named file is inaccessible or missing, list the specific path and required action. Do not substitute invented content or copy unrelated files from Downloads. Check that the Target folder's .env, credentials, and virtual environment are covered by its ignore rules. Do not change the parent repository's rules.

If the folder happens to be inside an existing repository, record its relative path for later run instructions and the submission manifest. Otherwise continue normally without Git. Leave repository creation and uploading to me.

Finish by showing the Target working folder, its file tree, and any missing inputs. Confirm which folder I should keep open in VS Code. Do not build the financial model yet.
```

After setup, stay in the Target working folder and continue with Step 1. Repository creation and uploading can wait until you are ready. Preserve dated evidence and required pre-run snapshots during the work rather than reconstructing them at the end.

## 1. Audit the assignment in the new project

Use the Target project folder organized in Step 0. The original course materials should now be in its `course-materials/`, working starters at its root, and current Target Edition A files in its `docs/`. Have Codex verify these locations rather than manually organizing the files again. Keep the original Gallagher submission and receipt separately, with private receipt details excluded from public sharing if needed.

Paste:

```text
I am completing FIN 43900 Project 1 using Target Corporation. Work one stage at a time inside the local Target project folder identified in Step 0. I will handle adding the finished project to GitHub later. Read the original materials in course-materials/, the current Target Edition A PDF/Markdown in docs/, and the starter code before editing. First verify that Step 0's local file setup is complete and report any missing files. Preserve all work outside the Target folder.

My instructor approved changing companies from Gallagher to Target. Preserve my current Target Edition A as the baseline for subsequent research. Treat its forecasts as provisional assumptions to investigate, not historical facts or a required final answer. Do not force the later model to match or differ from it.

First create docs/requirements-map.md. Map every requirement to its source, implementation location, required proof, and status. Cover all ten finance/product requirements, validation, Edition A/B, partner challenges, PDFs, three videos, corrected transcripts, access checks, and every manifest row.

Distinguish requirements, fictional examples, optional enhancements, and suggestions. Apply the Project 1 requirements; do not import Project 2/capstone exceptions. List referenced materials that are missing and leave their requirements pending.

Confirm that analysis.py currently raises NotImplementedError and app.py is only a JSON-display shell. Do not treat them as a completed model. Do not use the exemplar's fictional figures or assume visible_output.example.json is executed output.

Do not build the whole project in this stage. Report the audit and immediate next inputs needed.
```

Checkpoint: you have a traceable checklist, not an assurance that everything is already satisfied.

## 2. Set up the Target application and working rules

Paste:

```text
Set up a minimal Python/Streamlit project around the supplied starters, entirely inside the Target project folder. Use its data/, docs/, tests/, and outputs/ as needed, keeping visible_output.json beside the Target app.py. Preserve original templates in course-materials/. A parent Gallagher repository does not change the Target application's root. Do not initialize nested Git or change the parent project.

Create AGENTS.md recording these rules:
- Never invent data, citations, receipts, historical work, partner feedback, test outcomes, AI dispositions, or access checks.
- Preserve Edition A unchanged; corrections belong in a dated addendum or Edition B.
- Separate reported facts, normalizations, forecast assumptions, and computed outputs.
- Keep finance logic in analysis.py or modules it calls. app.py renders engine results and passes user inputs; it does not duplicate valuation formulas.
- Keep evidence, accounting rules, and checks locked; expose only documented assumption controls.
- Record material AI tasks and proposed outputs as work progresses. Use the actual exposed tool/model/version and interaction date. Leave my disposition pending until I make it.
- Never generate or revise my protected changed-input prediction, and do not assist during its AI-closed execution phase.
- Explain important code and finance choices so I can defend them.

Preserve the supplied supported dependency ranges. If a dependency is necessary, explain and document the change; record exact successful environment versions separately rather than replacing the supported ranges. Prefer the existing stack and standard-library testing where adequate.

Document environment setup. Keep .env and credentials ignored; use an empty .env.example only if credentials are actually needed. Do not add paid APIs or hosting requirements.
```

Checkpoint: the repository is organized and reproducible without making up financial results.

## 3. Define the investment question and date boundary

You choose the valuation date and investment horizon. Use the course-required date if one is specified.

Paste:

```text
Help me complete docs/project-scope.md with my approved valuation date and investment horizon. Ask only for unresolved student choices; continue independent setup while waiting.

The user is a buy-side analyst team with no current position in Target. The action choices are initiate, watch/defer, or do not initiate. Record the target/security, currency, units, basic-versus-diluted share convention, and material exclusions. Do not choose my action yet.

Create a convention ledger covering fiscal/calendar periods, discount timing, historical versus normalized base year, enterprise versus equity values, and share definitions. Distinguish period-end/current shares from historical weighted-average diluted EPS shares.

Establish the evidence cutoff: each item must have been publicly available by the valuation date. Record financial period end, filing/publication date, market-data timestamp, and retrieval date separately. Do not silently use later filings, later restatements, current share prices, or current consensus in a historical-date valuation.

Identify how the model will handle any gap between the historical base-year end and valuation date. Explain any stub-period approximation and its limitation.
```

Checkpoint: the intended decision and time boundary are explicit before collecting model inputs.

## 4. Build the source ledger and normalized base year

Paste:

```text
Build a source ledger and historical financial dataset for Target using filings and authoritative sources available by our cutoff. Open the actual sources rather than citing search snippets. If access is unavailable, list the exact documents/fields I need to obtain and leave gaps visible.

For each material input record an input ID, source URL, filing accession where applicable, page/table/note or XBRL concept, fiscal period, public availability date, value, units, definition, transformation, classification, and verification status.

As a practical research starting point, gather roughly three historical fiscal years and relevant interim information if available by the cutoff; this is a planning suggestion, not an assignment minimum. Use additional history when needed to justify driver bounds.

Reconstruct the reported income statement, balance sheet, and cash-flow statement. Investigate fiscal-week comparability, basis changes, one-time items, cash, debt, leases, working capital, and share counts. Apply the course contamination catalog when supplied. Do not assume an adjustment exists before checking evidence.

Preserve reported figures. Show an explicit reported-to-normalized bridge for every adjustment, including statement effects and rationale. A normalized figure need not equal the reported figure; its reconciliation must explain the difference.

Use secondary providers only with definition reconciliation. Never silently convert missing information to zero. Identify one load-bearing input for my independent source/definition check.
```

Your work: inspect the original source for consequential inputs and perform an independent check. Another AI answer is not independent evidence.

## 5. Propose and challenge Target-specific drivers

Paste:

```text
Using the verified history, propose a company-specific driver architecture for my review before implementing assumptions.

Investigate which supported drivers explain Target's revenue, operating costs/margins, inventory, payables, other working capital, capital expenditure, depreciation, taxes, and financing. Comparable sales, traffic/basket, store changes, mix, and fulfillment costs are research candidates, not pre-approved facts or required model inputs. Use only drivers we can source, defend, and avoid double-counting.

Create docs/assumption-challenge-record.md. For each load-bearing driver include its proposed value and five-year path, units, basis/source, causal link through the statements, strongest challenge, evidence that would change it, defensible lower/upper control bounds, and my approval status.

Propose causal low/base/high operating narratives with internally consistent assumptions. Do not apply an arbitrary identical percentage change to all inputs or label scenarios as probabilities without support.

Include fields for real Weeks 5–6 partner fresh-eyes feedback, challenger credit, my response, and resulting revision. Leave them pending until actual feedback occurs. Explain disagreements and ask for my material judgments without inventing them.
```

Checkpoint: you can explain the important assumptions and defend the control bounds. Preserve the original proposed values and subsequent changes.

## 6. Build and reconcile the five-year statements

Paste:

```text
Implement the approved five-year income statement, balance sheet, and cash-flow forecast through run_analysis(inputs). Explain the key schedules and accounting relationships before coding them.

Include transparent policies for operating working capital, fixed assets/depreciation, taxes, debt/interest, cash, dividends, repurchases, and equity. Handle material lease and other balances consistently with the source definitions. Disclose simplifications and any approved exclusions.

Do not conceal errors with an unexplained cash, debt, or equity plug. A debt revolver or cash-balancing mechanism is acceptable only as an explicit financing policy with constraints and roll-forwards. Make circularity handling and any financing infeasibility visible.

Implement checks for:
- reported base-year reconciliation and reported-to-normalized bridge;
- assets equaling liabilities plus equity every forecast year;
- beginning cash plus cash-flow movement equaling ending balance-sheet cash;
- relevant fixed-asset, debt, retained-earnings, and equity roll-forwards;
- missing data, signs, units, and infeasible input combinations.

Use documented numerical tolerances. Preserve full precision for checks and round only for display. Return useful check details to the interface, and prevent unvalidated values from being presented as approved results.

Add meaningful tests, execute them, preserve failures, and give me a way to verify one forecast year manually. Do not mark a test passed if it was not run.
```

Checkpoint: all three statements connect. A five-year sales/FCFF table alone does not satisfy this requirement.

## 7. Connect the DCF to the operating forecast

Paste:

```text
Build the five-year FCFF valuation from the pro-forma's operating forecast. Do not maintain a separate inconsistent growth forecast for the DCF.

Include FCFF from after-tax operating profit, depreciation/amortization, capital expenditure, and operating working-capital investment. Explain the operating tax convention and reconcile FCFF to statement schedules; do not mistake cash flow after financing for FCFF.

Build WACC from dated, sourced components with consistent currency, risk, tax, debt-cost, and capital-weight definitions. Record assumptions and methodology rather than taking an unexplained provider WACC.

Implement explicit discount timing, treatment of any stub period, terminal convention, WACC > terminal growth, and terminal assumptions consistent with sustainable operating performance and reinvestment.

Show enterprise value, each enterprise-to-equity adjustment, equity value, diluted share basis, and value per share. Make lease treatment consistent across operating cash flows, WACC/claims, and the bridge. Avoid double-counting cash, debt, leases, or other claims.

Report causal low/base/high values, the WACC–growth table, present value of terminal value as a share of enterprise value, and one reverse-DCF or market-implied expectation with a stated solved-for variable and limitations. Leave other inputs fixed as disclosed; do not claim a unique market expectation when many combinations could explain the price.

Test bridge arithmetic, invalid boundaries, and WACC/growth behavior under clearly stated economic conditions. Investigate surprises rather than forcing monotonic results. Leave the committee action for my judgment.
```

Checkpoint: every valuation cash flow traces to the statements, and the share-price bridge is visible.

## 8. Freeze peer policy, then select peers and calculate multiples

Paste:

```text
First draft docs/peer-policy.md without selecting peers or inspecting their multiples. Define business-mix, geography, profitability, scale, fiscal-period, accounting, and evidence-quality criteria. Identify unavoidable comparability limitations. Get my review of the policy and preserve its dated version before applying it.

After that review, apply the policy to candidates and document each inclusion/exclusion. Do not select firms because their multiples support a desired conclusion.

Calculate at least one enterprise-value multiple and one equity-value multiple using reconciled definitions and comparable time bases. EV/EBITDA and P/E are possible choices only if their denominators and accounting treatment are defensible. Show the calculations and explain exclusions for unusable denominators. Apply any EV-derived valuation through the same equity bridge.

Assess transaction evidence only when control, synergy, and deal-date context can be defended. If none is suitable, explain the evidence gap; do not force a transaction into the analysis.

Explain disagreement between DCF and multiples in terms of assumptions, economics, and comparability. Do not mechanically average methods or fabricate a required peer count.
```

Checkpoint: the policy predates peer selection, and both enterprise and equity multiples are covered.

## 9. Analyze the pro-forma's own sensitivities

Paste:

```text
Implement one-at-a-time sensitivities on our own Target pro-forma. Change one independent operating driver at a time from the same base; let dependent line items respond through the accounting engine. Restore the base between comparisons.

For each driver show the input range and units, effects on operating profit and FCFF in identified forecast periods, per-share value changes, and a causal explanation through the statements. State the metric used to rank effects.

Retest rankings with alternative justified ranges. Explain which rankings are stable and which depend on the ranges; a tornado chart is not a probability distribution.

Keep this distinct from causal low/base/high scenarios and the WACC–growth grid. Update the assumption-challenge record with real feedback and my decisions. Export the relevant tables and explanations for review without running the app.
```

Checkpoint: the model identifies what drives profit, cash flow, and value, and qualifies the ranking by the tested ranges.

## 10. Complete validation and prepare the protected exercise

Paste:

```text
Audit and complete the validation register using actual evidence. Cover:
- reconciliation to the weekly starter's published training-case known answers;
- one independent source/definition check on a load-bearing input;
- a directional changed-input test with its expectation recorded before execution;
- articulation, DCF boundaries/monotonicity, equity bridge, and peer/multiple consistency;
- a justified highest-risk failure test;
- one material AI output independently accepted, corrected, qualified, or rejected, with my reason and its effect.

If the official fixture is missing, leave that requirement pending. Supplementary synthetic tests help but do not establish reconciliation to unseen course answers. Preserve actual failed tests and their diagnoses.

Prepare a blank Locked Changed-Input Record and generic manual instructions for running the existing analysis with an input override and preserving before/after outputs. The ordinary runner must already work before I enter the protected phase.

Do not select my protected change, suggest its prediction, write my rationale, or execute the protected exercise. Its prediction and execution are AI closed under the supplied template. Do not claim an ordinary AI-assisted test fulfills it.
```

Then complete the protected exercise yourself, with generative assistance off:

1. Choose a material input change and write old/new values with units, expected output direction, and expected decision effect.
2. Preserve that prediction in an immutable commit/snapshot before the run. Record its timestamp and actual commit identifier. A file cannot contain its own final commit hash in advance; record that identifier separately after making the commit.
3. Run the test without AI help. Preserve base/changed outputs, actual direction, decision effect, and diagnosis or no-change reason.
4. Keep the original prediction unchanged even if wrong. Resume assistance only after the AI-closed exercise ends under your course instructions.

This guide does not choose the protected input or write that prediction for you.

## 11. Build the usable interface and genuine failure demonstration

Paste after the protected exercise is complete:

```text
Extend app.py into the required semi-adjustable Streamlit workbench. Use the validated analysis engine and approved driver bounds.

Provide bounded controls, evidence/bounds explanations, reset to base, five-year statements, scenarios, valuation range, WACC–growth sensitivity, operating-driver sensitivity, terminal-value share, reverse DCF, source traceability, and visible check details.

Reconcile the starter's frozen-output contract with the interactive requirement:
1. Generate root visible_output.json from the validated base analysis, including material inputs, units, as-of date, version, conditions, limitations, and checks.
2. Render that frozen base faithfully.
3. For changed controls, send overrides to the same engine, validate the returned results, and clearly label the exploratory scenario and differences from base.
4. Do not silently overwrite the frozen submission output, duplicate finance formulas in the UI, or hand-type computed material results.

Keep accounting, source history, and check logic locked. Show red alerts both for actual consistency failures and for leaving documented historical bands, with clear labels distinguishing those conditions. Do not imply a balanced model proves an assumption is justified. Block valuation use where required validity checks fail.

Make it possible to demonstrate a real incoherent input combination, its actual check failure, and recovery through the interface. Use a documented model constraint rather than fake red indicators, altered historical facts, or deliberately corrupted totals. A separate synthetic test is not a substitute for the required live incoherent-input demonstration.

Verify that reset restores the original base controls and numerical results. Show me how to run and operate the tool.
```

Checkpoint: a teammate can change a justified driver and understand the result without editing accounting code.

## 12. Run the cold check and make the committee judgment

Paste:

```text
Perform one clean end-to-end run in a fresh isolated environment following the Target README, using a preserved, identified source/input snapshot and declared dependencies rather than relying on an existing environment or hidden data cache. The project can be tested from a clean local copy before I upload it. If Target is inside another repository, run from the Target subfolder and preserve the other project's environment. Once I supply the final repository location, update the README with the actual checkout and subfolder instructions.

Record the actual environment versions, run commands, source/input version, first failure if any, resolution or remaining limitation, checks, and final outputs. Preserve a cold-run log and capture evidence as required by the course. If you cannot execute a step, mark it pending and give me the exact manual procedure.

Export the validated base to visible_output.json and a readable visible-output report with material inputs, source/as-of dates, units, assumptions, scenarios, equity bridge, sensitivities, checks, and limitations. A grader must be able to inspect material evidence without running the app. Clearly distinguish the source-code version used for a run from the later final submission commit.

Help me assess the evidence for initiate, watch/defer, or do not initiate. Ask for my judgment on the range, conditions, reversal triggers, and committee ask. Do not infer an action merely because a DCF point exceeds the market price.

Record my approved conditional action and monitoring policy as explicit inputs that the engine includes in exported results. Each trigger needs an observable metric, threshold or condition, evidence/review window, and resulting response. Keep exploratory model values distinct from my frozen recommendation unless I approve a documented decision rule.
```

Checkpoint: there is an actual reproducible run and a student-owned conditional recommendation.

## 13. Prepare Project 1's written submission and PDFs

Paste:

```text
Use the supplied templates and validated evidence to prepare:
- README.md;
- docs/decision-memo.md;
- docs/research-evolution.md;
- docs/validation-and-ai-use.md;
- project-submission-manifest.csv using the supplied columns and rows.

Write these files inside the Target project folder. If it lives inside the Gallagher repository, leave Gallagher's README and docs intact, point the manifest directly to the Target subfolder and its frozen version, and include the repository-relative path in run instructions.

Prepare Research-Evolution.pdf with the unchanged Edition A content, dated addendum only if needed, Edition B, and an A-to-B/no-material-change evidence table. Preserve the original Edition A PDF separately unchanged. Record its real receipt evidence. Distinguish course instruction, my analysis, peer challenge, AI, and mixed causes; do not invent a dramatic change or rewrite my baseline.

Prepare Decision-Memo.pdf of no more than two pages, leading with my action, defensible range, decision user, as-of date, material conditions, strongest evidence, sensitivities, risks, reversal triggers, committee ask, and next review. Reference the validation/AI-use record. A deck is an allowed alternative, not an extra requirement; if I choose it, use Decision-Deck.pdf with no more than eight main slides and a concise permitted appendix.

Prepare Validation-and-AI-Use.pdf with source/convention ledger, actual test results including failures, limitations, complete preserved Locked Changed-Input Record, and named material AI uses with independent checks and my actual dispositions.

Keep content-equivalent repository records. Render and inspect the PDFs for clipping, readability, tables, citations, and page limits. Do not claim PDF creation or inspection if unavailable. Leave missing student evidence visibly pending rather than inventing it.
```

Checkpoint: memo, model, visible output, research evolution, and validation agree on dates, figures, conditions, and version.

## 14. Record the three videos, correct transcripts, and audit the package

Paste before recording:

```text
Prepare evidence-based recording outlines, preserving the course limits:
- Video 1: research evolution, maximum 3:00.
- Video 2: code/validation, maximum 5:00.
- Video 3: committee presentation, maximum 5:00.

For each outline, identify the actual project artifact to show and the claim it supports. Suggested timing is a rehearsal aid, not proof of a recorded duration.

Video 3 must open with the live product demo. In roughly the first minute I will move a bounded driver, read and explain its effect against the restored base, show a real check failing on incoherent inputs, and recover. Then I defend my conditional recommendation with the product still on screen.

For Video 1 use the actual Edition A/B evidence and causes of changed or unchanged views. For Video 2 prioritize source-to-output traceability, important engine logic, and actual validation/failure evidence. Do not invent extra rubric requirements we have not received.

Create blank transcript files using project-transcript-template.txt. Do not fabricate completed transcripts, speaker statements, uploaded links, or recording evidence.
```

Your work: record and upload the videos, check durations, and obtain their actual transcripts. Correct material finance terms, figures, tickers/names, attribution, and evidence timestamps. Supply real stable URLs. Give the instructional team access to a private repository if applicable; test unlisted-video access logged out.

Paste after recording:

```text
Use my actual recordings/transcripts to help correct substantive errors and add accurate timestamp indices. Do not replace my spoken argument with a different script presented as a transcript. Record actual durations and frozen versions.

Audit the final package against requirements-map.md, all supplied course documents, and the analytic rubric if available. Check every manifest row, stable link, required PDF, transcript, visible-output artifact, environment instruction, and validation record.

Report exact locations of unsupported claims, missing evidence, inconsistent dates/figures, placeholders, missing receipts/feedback, exposed credentials, unverified access, and failed checks. Distinguish complete, failed, and pending items; do not claim all requirements passed when a required input is unavailable.

After corrections, record the frozen local document/source versions. I will add the project to GitHub myself. Once I supply the repository URL and final commit, update the manifest with those actual values; do not invent them or upload on my behalf. Keep the analysis run's source version distinct where appropriate. Material changes after recording require updating affected output, documents, and recording evidence. Leave submission and access confirmations pending until they actually occur.
```

## Final deliverable inventory

| Item | What establishes completion |
|---|---|
| Edition A baseline | Original PDF preserved; actual first successful Brightspace receipt and timestamp |
| Research-Evolution.pdf | Unchanged A content, B, addendum if needed, evidence-supported comparison |
| Accessible repository | Runnable source, README, dependency/environment record, declared inputs, docs, tests, source/assumption records |
| Visible executed output | Validated material inputs and results, as-of dates, units, range, action, conditions, version, limitations; readable without execution |
| Decision-Memo.pdf or Decision-Deck.pdf | Memo at most 2 pages, or deck at most 8 main slides with permitted concise appendix |
| Validation-and-AI-Use.pdf | Real test evidence, protected changed-input record, independent checks, material AI uses/dispositions, limitations |
| Video 1 and transcript-video-1.txt | Research evolution; actual duration at most 3:00; corrected transcript |
| Video 2 and transcript-video-2.txt | Code/validation; actual duration at most 5:00; corrected transcript |
| Video 3 and transcript-video-3.txt | Committee defense opening with live product demo; actual duration at most 5:00; corrected transcript |
| Submission manifest | Supplied 12-row structure, required links and locations, actual durations/as-of dates, indices, access confirmation, frozen versions; deployment optional |
| Final checks and Brightspace submission | Instructor repository access, logged-out unlisted-video checks, no credentials, consistent frozen package, actual submission receipt |

The course estimates 18–25 hours across Weeks 2–8. Use its published schedule and deadline. Do not substitute interface polish, commit counts, or framework complexity for decision evidence and your ability to defend the work.
