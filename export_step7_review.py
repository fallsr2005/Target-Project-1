"""Export provisional valuation from the same financial and valuation engines."""
import json
import sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root))
from valuation_engine import run_valuation

s=json.loads((root/'data/model-inputs-step6.json').read_text(encoding='utf-8'))
v=json.loads((root/'data/model-inputs-step7.json').read_text(encoding='utf-8'))
r=run_valuation(s,v)
(root/'outputs/step7-provisional-valuation.json').write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
base=r['scenarios']['base']; b=base['partial_equity_bridge']; d=base['dcf']; w=r['wacc_components']; t=d['terminal']
lines=['# Step 7 provisional valuation — for review only','','These are calculated illustrations with an incomplete equity bridge and unresolved evidence. They are not a decision-ready valuation, accepted price, or recommendation. Amounts in USD millions except per-share figures.','',f"Assumed CAPM: {w['risk_free']:.2%} risk-free + {w['beta']:.2f} beta × {w['erp']:.2%} equity risk premium = {w['equity_cost']:.2%} cost of equity. With {w['equity_weight']:.0%} equity, {w['debt_weight']:.0%} debt, {w['debt_cost_pretax']:.2%} pretax debt cost and {w['tax_shield_rate']:.0%} tax shield, WACC = **{w['wacc']:.2%}**. Beta, debt cost and weights are provisional; see `docs/step-7-source-ledger.md`.",'','## Cash flows from the statements','','| Period | EBIT | Operating tax | D&A | Capex | Change in operating WC | FCFF | PV of FCFF |','|---|---:|---:|---:|---:|---:|---:|---:|']
for f,p in zip(base['fcff'],d['discounted_periods']):
    lines.append(f"| {f['period']} | {f['ebit']:,.1f} | {f['operating_tax']:,.1f} | {f['total_da']:,.1f} | {f['capex']:,.1f} | {f['increase_operating_working_capital']:,.1f} | {f['fcff']:,.1f} | {p['present_value']:,.1f} |")
lines += ['',f"The elapsed August 2–October 19 estimate is excluded. Future cash flows are discounted from the cutoff to each fiscal period end using actual days/365. Terminal value is measured {t['measurement_date']}. At {t['growth']:.1%} growth and an assumed {t['incremental_roic']:.1%} incremental return, the model reinvests {t['reinvestment_fraction']:.1%} of next-period operating profit after tax; the PV of terminal value is {t['present_value']:,.1f}, or {t['share_of_enterprise_value']:.1%} of enterprise value.",'', '## Partial enterprise-to-equity bridge','',f"Enterprise value {b['enterprise_value']:,.1f} + estimated eligible excess cash {b['estimated_eligible_excess_cash']:,.1f} − estimated total debt {b['debt_estimated_at_cutoff']:,.1f} = **partial equity value {b['equity_value_partial']:,.1f}**. Estimated cutoff cash is {b['cash_estimated_at_cutoff']:,.1f}, of which {b['estimated_operating_cash_retained']:,.1f} is retained as operating cash. Reported August cash and debt were {b['cash_reported_august_1']:,.1f} and {b['debt_reported_august_1']:,.1f}. Unknown other claims and non-operating assets are omitted rather than established as zero. Finance leases are included in debt once; operating lease rent stays in operating cash flows.",f"Estimated shares {b['estimated_diluted_shares_millions']:,.3f} million produce a **partial illustrative value of ${b['value_per_share_partial']:,.2f} per share**. The 2.2 million incremental dilution is an EPS-weighted-average proxy, not a valuation-date award calculation.",'','## Operating scenarios','', '| Case | Partial illustrative value/share | Assumptions compared with base, FY2027–FY2031 |','|---|---:|---|']
descriptions={'low':'Sales growth −1 percentage point; merchandise cost +0.8 points; SG&A +0.3 points.','base':'Step 6 provisional assumptions.','high':'Sales growth +1 point; merchandise cost −0.8 points; SG&A −0.3 points; capex +0.5 points.'}
for name in ('low','base','high'):
    x=r['scenarios'][name]; lines.append(f"| {name.title()} | ${x['partial_equity_bridge']['value_per_share_partial']:,.2f} | {descriptions[name]} |")
lines += ['','Scenarios share the same estimated cutoff balance sheet and FY2026 stub, WACC and terminal assumptions. These are coherent stories to challenge, not probabilities or approved cases.','', '## WACC and terminal growth sensitivity','', '| WACC | g = 1% | g = 2% | g = 3% |','|---|---:|---:|---:|']
cells=r['wacc_growth_sensitivity']
for idx in range(0,9,3):
    group=cells[idx:idx+3]; lines.append(f"| {group[0]['wacc']:.2%} | "+' | '.join(f"${x['partial_value_per_share']:,.2f}" for x in group)+' |')
lines += ['', 'The values above remain partial because the other-claims bridge is unresolved. The accepted official closing price is pending, so upside/downside and market-implied reverse DCF are not calculated.','',f"FCFF and future-period checks: {sum(x['status']=='pass' for x in r['checks'])} pass and {sum(x['status']=='fail' for x in r['checks'])} fail. Arithmetic success does not verify assumptions.",'','## Material evidence warnings']
lines.extend('- '+x for x in r['evidence_warnings'])
(root/'outputs/step7-provisional-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Wrote provisional JSON and report; valuation checks:',sum(x['status']=='pass' for x in r['checks']),'pass;',sum(x['status']=='fail' for x in r['checks']),'fail')
