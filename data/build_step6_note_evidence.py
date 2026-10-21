"""Preserve filing-note observations separately from model assumptions."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
k='https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm'
q='https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm'
rows=[]
def add(prefix,loc,end,url,accession,published,items):
    for name,val in items:
        rows.append({'input_id':prefix+str(len(rows)+1).zfill(2),'definition':name,'value':val,'unit':'USD millions','financial_period_end':end,'source_url':url,'accession':accession,'locator':loc,'publication_date':published,'retrieval_date':'2026-10-19','transformation':'none; source-reported','verification_status':'checked in original filing; independent student review pending'})
add('S6-K','Note 11 p.55','2026-01-31',k,'0000027419-26-000016','2026-03-11',[('Accounts and other receivables',1265),('Vendor income receivable',542),('Prepaid expenses',223),('Other current assets, other',183)])
add('S6-K','Note 15 p.57','2026-01-31',k,'0000027419-26-000016','2026-03-11',[('Wages and benefits',1565),('Gift card liability',1197),('Real estate sales and other taxes payable',704),('Dividends payable',516),('Income tax payable',440),('Current operating lease liability',372),('Workers compensation and general liability',310),('Interest payable',138),('Other accrued liabilities',1236)])
add('S6-K','Note 9 p.54','2026-01-31',k,'0000027419-26-000016','2026-03-11',[('Book overdrafts included in accounts payable',221),('Book overdrafts included in accrued liabilities',7)])
add('S6-Q','Note 2 p.9','2026-08-01',q,'0000027419-26-000042','2026-08-28',[('Gift card liability in accrued liabilities',959),('Estimated returns liability',178)])
add('S6-Q','Note 5 p.10','2026-08-01',q,'0000027419-26-000042','2026-08-28',[('Prepaid forward contracts within other current assets',25)])
(root/'step6-source-note-evidence.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print('Saved',len(rows),'source-note observations')
