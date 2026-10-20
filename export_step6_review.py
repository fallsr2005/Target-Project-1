"""Run provisional engine and preserve a real stress failure and readable review."""
import copy
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from financial_engine import run_analysis

config=json.loads((ROOT/'data/model-inputs-step6.json').read_text(encoding='utf-8'))
base=run_analysis(config)
stress=copy.deepcopy(config)
stress['drivers']['capex_rate']['value']=[.40]*6
stress['drivers']['revolver_capacity']['value']=0
failed=run_analysis(stress)
recovered=run_analysis(copy.deepcopy(config))
artifact={'purpose':'AI-assisted mechanical funding stress, not protected changed-input exercise','input_changes':{'capex_rate':.40,'revolver_capacity_usd_millions':0},'stress_failed_checks':[x for x in failed['checks'] if x['status']=='fail'],'stress_periods':[{'period':x['period'],'cash':x['balance_sheet']['cash'],'shortfall':x['schedules']['minimum_cash_shortfall']} for x in failed['periods']],'base_recovery_failures':[x for x in recovered['checks'] if x['status']=='fail']}
(ROOT/'outputs/step6-failure-and-recovery.json').write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
p=base['periods'][2]; i=p['income_statement']; c=p['cash_flow_statement']; b=p['balance_sheet']; q=p['schedules']
lines=['# Step 6 draft: provisional statements and walkthrough','','USD millions unless otherwise noted. These figures are experimental forecasts, not approved inputs, a valuation or a recommendation. See the JSON for complete period statements, all checks and warnings.','', '| Period | Sales | Operating income | Net income | Operating cash flow | Ending cash | Assets | Liabilities | Equity |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for z in base['periods']:
    a=z['income_statement']; cf=z['cash_flow_statement']; bs=z['balance_sheet']
    lines.append(f"| {z['period']} | {a['sales']:,.1f} | {a['operating_income']:,.1f} | {a['net_income']:,.1f} | {cf['operating_cash_flow']:,.1f} | {bs['cash']:,.1f} | {bs['total_assets']:,.1f} | {bs['total_liabilities']:,.1f} | {bs['equity']:,.1f} |")
lines += ['', '## Example: FY2027',f"Sales {i['sales']:,.1f} less cost of sales {i['cost_of_sales_including_allocated_da']:,.1f}, SG&A {i['sga']:,.1f}, and separate depreciation {i['separate_da']:,.1f} gives operating income {i['operating_income']:,.1f}. After interest {i['interest']:,.1f} and tax {i['tax']:,.1f}, net income is {i['net_income']:,.1f}.",f"Add depreciation {c['da_addback']:,.1f} and the operating working-capital cash change {c['working_capital_cash_change']:,.1f} to net income to obtain operating cash flow {c['operating_cash_flow']:,.1f}. Add investing cash flow {c['investing_cash_flow']:,.1f} and financing cash flow {c['financing_cash_flow']:,.1f}; the change {c['cash_change']:,.1f} moves opening cash {q['opening_cash']:,.1f} to ending cash {b['cash']:,.1f}.",f"PP&E moves from {q['opening_ppe']:,.1f} plus capex {-c['capex']:,.1f} less depreciation {q['total_da']:,.1f} to {b['ppe']:,.1f}. Assets of {b['total_assets']:,.1f} equal liabilities {b['total_liabilities']:,.1f} plus equity {b['equity']:,.1f}, within calculation tolerance. This arithmetic equality does not verify the assumptions.",'',f"Base checks: {sum(x['status']=='pass' for x in base['checks'])} pass; {sum(x['status']=='fail' for x in base['checks'])} fail. Mechanical stress produced {len(artifact['stress_failed_checks'])} genuine failures; restoring the original configuration produced {len(artifact['base_recovery_failures'])} failures. This is not the protected exercise.",'','## Evidence warnings']
lines.extend('- '+x for x in base['evidence_warnings'])
(ROOT/'outputs/step6-provisional-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Saved review and stress evidence; stress failures:',len(artifact['stress_failed_checks']),'recovered failures:',len(artifact['base_recovery_failures']))
