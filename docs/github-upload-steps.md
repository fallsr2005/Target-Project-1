# GitHub upload steps

Use this Target project as the main working folder. Its upload folders are `data`, `docs`, `outputs`, `tests` and `course-materials`. Videos belong in `recordings` locally, with actual viewing links entered in the manifest after upload to the course-accepted video location.

## Repair the GitHub folder layout

1. Keep the existing GitHub files while adding the correct folders.
2. Open the Target folder in File Explorer and https://github.com/fallsr2005/Target-Project-1 in your browser.
3. On GitHub choose **Add file > Upload files**.
4. Drag the **whole, closed `data` folder** from File Explorer into the upload area. Check for a path such as `data/model-inputs-step6.json`, then save/commit the upload.
5. Repeat with each whole folder: `docs`, `outputs`, `tests`, `course-materials`. Upload one folder at a time to stay below GitHub's 100-file web limit.
6. Replace the root `README.md`, `.gitignore` and `project-submission-manifest.csv` with the latest versions in this working folder.
7. Confirm the repository lists the five folders alongside the code files and `visible_output.json`. Leave the root code files at the root.

Local-only items: `recordings`, `.local`, all `.venv` folders and `__pycache__`. They are not upload material. Existing misplaced root duplicates can be reviewed for cleanup after the corrected folders are verified; clearing the repository is unnecessary.

Official instructions: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

## Brightspace files

Attach `docs/Decision-Memo.pdf`, `docs/Research-Evolution.pdf`, `docs/Validation-and-AI-Use.pdf`, the three completed `docs/transcript-video-N.txt` files and the root `project-submission-manifest.csv`. All three video links and student-reported timestamp indices are in the manifest; the final version, instructor access checks, original checkpoint receipt and submission receipt remain pending. This guide does not certify full rubric completion.
