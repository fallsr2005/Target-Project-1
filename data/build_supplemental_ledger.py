"""Record source-note evidence and explicitly tentative market observations."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
k = 'https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm'
q = 'https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm'
spec = [
 ('N01',593,'USD millions','FY2025 settlement gain, net of legal fees','FY2025','2026-01-31',k,'0000027419-26-000016','pp. 32–33, Note 6 p. 53','2026-03-11'),
 ('N02',250,'USD millions','FY2025 transformation costs','FY2025','2026-01-31',k,'0000027419-26-000016','pp. 32–33, Note 7 p. 53','2026-03-11'),
 ('N03',441,'USD millions','FY2025 settlement gain after tax','FY2025','2026-01-31',k,'0000027419-26-000016','p. 32, adjustment table','2026-03-11'),
 ('N04',187,'USD millions','FY2025 transformation costs after tax','FY2025','2026-01-31',k,'0000027419-26-000016','p. 32, adjustment table','2026-03-11'),
 ('N05',4775,'USD millions','Company-reported adjusted operating income','FY2025','2026-01-31',k,'0000027419-26-000016','p. 33, non-GAAP reconciliation','2026-03-11'),
 ('N06',994,'USD millions','Tariff refunds received and credited to cost of sales','Q2 and H1 FY2026; same item in both periods','2026-08-01',q,'0000027419-26-000042','Note 3; pp. 13–14','2026-08-28'),
 ('N07',593,'USD millions','Settlement gain in H1 FY2025, same gain as annual FY2025','H1 FY2025','2025-08-02',q,'0000027419-26-000042','Note 4 and p. 13','2026-08-28'),
 ('N08',454291461,'shares','Common shares issued and outstanding','Q2 FY2026 end','2026-08-01',q,'0000027419-26-000042','p. 3, common stock footnote','2026-08-28'),
 ('N09',452840187,'shares','Common shares issued and outstanding','FY2025 year-end','2026-01-31',q,'0000027419-26-000042','p. 3, common stock footnote','2026-08-28'),
 ('N10',454396092,'shares','Common shares issued and outstanding','Q2 FY2025 end','2025-08-02',q,'0000027419-26-000042','p. 3, common stock footnote','2026-08-28'),
 ('N11',4000,'USD millions','New committed revolving credit capacity, not drawn debt','August 2026','2026-08-14',q,'0000027419-26-000042','MD&A liquidity; August facility','2026-08-28'),
 ('N12',1.16,'USD per common share','Declared quarterly dividend payable December 1','declaration','2026-09-23','https://corporate.target.com/press/release/2026/09/target-corporation-declares-regular-quarterly-dividend',None,'opening paragraph','2026-09-23'),
 ('N13',3733,'USD millions','Total current and noncurrent operating lease liabilities','Q2 FY2026 end','2026-08-01',q,'0000027419-26-000042','p. 21 ROIC table and footnote c','2026-08-28'),
 ('N14',131,'USD millions','Finance lease liability included in current debt','FY2025 year-end','2026-01-31',k,'0000027419-26-000016','Note 19, lease classification table p. 60','2026-03-11'),
 ('N15',1982,'USD millions','Finance lease liability included in noncurrent debt','FY2025 year-end','2026-01-31',k,'0000027419-26-000016','Note 19, lease classification table p. 60','2026-03-11'),
 ('N16',1700,'USD millions','Approximate extra-week net sales in 53-week FY2023','FY2023','2024-02-03',k,'0000027419-26-000016','p. 3, footnote a; source reports $1.7 billion','2026-03-11'),
 ('P01',153.29,'USD per share','Third-party historical close; official unadjusted auction price not confirmed','2026-10-19 regular session','2026-10-19','https://stockanalysis.com/stocks/tgt/history/',None,'historical price table, 2026-10-19','2026-10-19'),
 ('P02',153.24,'USD per share','Conflicting third-party historical close; adjustment basis not confirmed','2026-10-19 regular session','2026-10-19','https://chartexchange.com/symbol/nyse-tgt/historical/',None,'historical price table, 2026-10-19','2026-10-19'),
]
records=[]
for ident, val, unit, definition, period, end, url, acc, locator, published in spec:
    market = ident.startswith('P')
    records.append({'input_id':ident,'classification':'market observation, not verified' if market else 'reported fact','value':val,'unit':unit,'definition':definition,'financial_period':period,'period_end':end,'source_url':url,'accession':acc,'locator':locator,'publication_date':None if market else published,'availability_time':'third-party publication time not independently established' if market else 'before cutoff; exact time not recorded','market_timestamp':'2026-10-19 16:00 America/New_York (intended close; official match unverified)' if market else None,'retrieval_date':'2026-10-19','transformation':'$1.7 billion multiplied by 1000' if ident == 'N16' else 'none; reported source unit','verification_status':'conflicting secondary providers; official price and adjustment basis pending' if market else 'checked against original disclosure; independent student review pending'})
(root/'supplemental-evidence.json').write_text(json.dumps(records, indent=2, ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Wrote {len(records)} supplemental evidence records')
