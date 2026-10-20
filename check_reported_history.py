"""Check statement arithmetic; missing cells remain missing, not zero."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = json.loads((ROOT / 'historical-reported.json').read_text(encoding='utf-8'))
checks = []

def value(sid, statement, period, label):
    found = [r for r in rows if r['input_id'].startswith(sid + '-') and r['statement'] == statement and r['financial_period'] == period and r['definition'].replace('\u2019', "'") == label]
    if len(found) != 1 or found[0]['value'] is None:
        raise ValueError(f'Missing or ambiguous {sid} {statement} {period} {label}')
    return found[0]['value']

def test(name, expected, actual):
    diff = round(actual - expected, 6)
    checks.append({'check': name, 'expected_usd_millions': expected, 'actual_usd_millions': actual, 'difference_usd_millions': diff, 'status': 'pass' if abs(diff) < 0.01 else 'investigate'})

for sid, period in [('K25','FY2025'),('K25','FY2024'),('K25','FY2023'),('Q26','Q2 FY2026'),('Q26','Q2 FY2025'),('Q26','H1 FY2026'),('Q26','H1 FY2025')]:
    v = lambda label: value(sid, 'income', period, label)
    test(period+' income: sales less costs', v('Operating income'), v('Net sales')-v('Cost of sales')-v('Selling, general, and administrative expenses')-v('Depreciation and amortization (exclusive of depreciation included in cost of sales)'))
    other = 'Net other income' if sid == 'K25' else 'Net other expense / (income)'
    test(period+' income: pretax', v('Earnings before income taxes'), v('Operating income')-v('Net interest expense')-v(other))
    test(period+' income: net earnings', v('Net earnings'), v('Earnings before income taxes')-v('Provision for income taxes'))

for sid, period in [('K25','FY2025 year-end'),('K25','FY2024 year-end'),('K24','FY2023 year-end'),('Q26','Q2 FY2026 end'),('Q26','FY2025 year-end'),('Q26','Q2 FY2025 end')]:
    v = lambda label: value(sid, 'balance', period, label)
    test(period+' assets', v('Total assets'), sum(v(x) for x in ['Total current assets','Property and equipment, net','Operating lease assets','Other noncurrent assets']))
    test(period+' current assets', v('Total current assets'), sum(v(x) for x in ['Cash and cash equivalents','Inventory','Other current assets']))
    test(period+' current liabilities', v('Total current liabilities'), sum(v(x) for x in ['Accounts payable','Accrued and other current liabilities','Current portion of long-term debt and other borrowings']))
    test(period+' liabilities and equity', v("Total liabilities and shareholders' investment"), v('Total current liabilities')+v('Total noncurrent liabilities')+v("Total shareholders' investment"))
    test(period+' balance sheet', v('Total assets'), v("Total liabilities and shareholders' investment"))

for sid, period in [('K25','FY2025'),('K25','FY2024'),('K25','FY2023'),('Q26','H1 FY2026'),('Q26','H1 FY2025')]:
    v = lambda label: value(sid, 'cash_flow', period, label)
    movement = v('Cash provided by operating activities')+v('Cash used in investing activities')+v('Cash used in financing activities')
    test(period+' cash movement', v('Cash and cash equivalents at end of period'), v('Cash and cash equivalents at beginning of period')+movement)

(ROOT / 'historical-reconciliation.json').write_text(json.dumps(checks, indent=2)+'\n', encoding='utf-8')
print(f"{len(checks)} checks; {sum(c['status'] == 'pass' for c in checks)} pass; {sum(c['status'] != 'pass' for c in checks)} require investigation")
