"""Extract reported statement rows from preserved SEC HTML. No forecasts or valuations."""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
RETRIEVED = "2026-10-19"  # Date the downloaded evidence was actually retrieved.
SOURCES = {
    "K25": {"file": "source-fy2025-10k.html", "url": "https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm", "accession": "0000027419-26-000016", "published": "2026-03-11"},
    "K24": {"file": "source-fy2024-10k.html", "url": "https://www.sec.gov/Archives/edgar/data/27419/000002741925000018/tgt-20250201.htm", "accession": "0000027419-25-000018", "published": "2025-03-12"},
    "Q26": {"file": "source-q2-2026-10q.html", "url": "https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm", "accession": "0000027419-26-000042", "published": "2026-08-28"},
}
# A positional cell is the printed numeric column, not the duplicated formatting columns.
TABLES = [
    ("K25", "income", 119, "p. 45, Consolidated Statements of Operations", [(4,"FY2025","2026-01-31"),(7,"FY2024","2025-02-01"),(10,"FY2023","2024-02-03")]),
    ("K25", "balance", 125, "p. 47, Consolidated Statements of Financial Position", [(4,"FY2025 year-end","2026-01-31"),(7,"FY2024 year-end","2025-02-01")]),
    ("K25", "cash_flow", 128, "p. 48, Consolidated Statements of Cash Flows", [(4,"FY2025","2026-01-31"),(7,"FY2024","2025-02-01"),(10,"FY2023","2024-02-03")]),
    ("K24", "balance", 120, "p. 44, Consolidated Statements of Financial Position", [(7,"FY2023 year-end","2024-02-03")]),
    ("Q26", "income", 6, "p. 1, Consolidated Statements of Operations", [(4,"Q2 FY2026","2026-08-01"),(10,"Q2 FY2025","2025-08-02"),(16,"H1 FY2026","2026-08-01"),(22,"H1 FY2025","2025-08-02")]),
    ("Q26", "balance", 12, "p. 3, Consolidated Statements of Financial Position", [(4,"Q2 FY2026 end","2026-08-01"),(10,"FY2025 year-end","2026-01-31"),(16,"Q2 FY2025 end","2025-08-02")]),
    ("Q26", "cash_flow", 15, "p. 4, Consolidated Statements of Cash Flows", [(4,"H1 FY2026","2026-08-01"),(10,"H1 FY2025","2025-08-02")]),
]

def number(raw):
    if pd.isna(raw):
        return None, "blank"
    text = str(raw).strip().replace("\u00a0", " ")
    if text in {"—", "–", "-"}:
        return None, "reported dash; not interpreted as zero"
    cleaned = text.replace(",", "")
    if re.fullmatch(r"\(\d+(?:\.\d+)?\)", cleaned):
        return -float(cleaned[1:-1]), "parentheses interpreted as negative"
    if re.fullmatch(r"-?\d+(?:\.\d+)?", cleaned):
        return float(cleaned), "reported number; no scale conversion"
    return None, "non-numeric: " + text

def run():
    records = []
    cache = {}
    for sid, statement, index, locator, columns in TABLES:
        source = SOURCES[sid]
        if sid not in cache:
            cache[sid] = pd.read_html(str(ROOT / source["file"]), encoding="utf-8")
        table = cache[sid][index]
        for row_number, row in table.iterrows():
            if pd.isna(row.iloc[0]):
                continue
            label = " ".join(str(row.iloc[0]).replace("\u00a0", " ").split())
            if not label or "(millions" in label.lower():
                continue
            cells = [(column, period, end, row.iloc[column]) for column, period, end in columns]
            if not any(number(cell)[0] is not None or number(cell)[1].startswith("reported dash") for _,_,_,cell in cells):
                continue
            for column, period, end, cell in cells:
                value, transform = number(cell)
                if transform == "blank" or transform.startswith("non-numeric"):
                    continue
                unit = "USD millions"
                if "per share" in label.lower():
                    unit = "USD per share"
                elif label in {"Basic", "Diluted", "Antidilutive shares"}:
                    unit = "million shares"
                records.append({"input_id":f"{sid}-{statement}-r{row_number:02d}-c{column:02d}", "classification":"reported fact", "statement":statement, "definition":label, "value":value, "reported_cell":str(cell), "unit":unit, "financial_period":period, "period_end":end, "source_url":source["url"], "accession":source["accession"], "locator":locator+f"; extracted table {index}, row {row_number}", "publication_date":source["published"], "publication_time":"13:53:59 America/New_York" if sid == "Q26" else None, "market_timestamp":None, "retrieval_date":RETRIEVED, "transformation":transform, "verification_status":"extracted from original filing table; reconciliation and independent review as documented"})
    (ROOT / "historical-reported.json").write_text(json.dumps(records, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(f"Wrote {len(records)} reported statement records")

if __name__ == "__main__":
    run()
