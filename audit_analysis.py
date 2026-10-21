"""Dated evidence, conditional market comparisons and reproducible export helpers."""
from copy import deepcopy
from datetime import date, datetime
from pathlib import Path
import json, math, hashlib
from functools import lru_cache
from financial_engine import run_analysis
from valuation_engine import run_valuation, reverse_dcf, discount_cashflows, fcff_from_operating, equity_from_enterprise, enterprise_bridge, present_value

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'/'audit-2026-10-20'

def load_inputs():
    return tuple(json.loads((ROOT/'data'/name).read_text(encoding='utf-8')) for name in ('model-inputs-step6.json','model-inputs-step7.json'))

@lru_cache(maxsize=1)
def historical_reference_bands():
    h=json.loads((ROOT/'data/historical-reported.json').read_text(encoding='utf-8'))
    def x(period,definition):
        r=[v['value'] for v in h if v['financial_period']==period and v['definition']==definition]
        if len(r)!=1:raise ValueError('Historical reference must have one sourced value')
        return r[0]
    years=['FY2023','FY2024','FY2025']; sales=[x(y,'Net sales') for y in years]
    values={'cost_ex_da_rate':[x(y,'Cost of sales')/s for y,s in zip(years,sales)],'sga_rate':[x(y,'Selling, general, and administrative expenses')/s for y,s in zip(years,sales)],'capex_rate':[-x(y,'Expenditures for property and equipment')/s for y,s in zip(years,sales)],'sales_growth':[sales[1]/sales[0]-1,sales[2]/sales[1]-1,51982/49057-1]}
    return {k:{'low':min(v),'high':max(v),'observations':v,'definition':'reported annual rate; sales also includes latest H1 growth; cost compared including model allocated D&A','source':'data/historical-reported.json; FY2023-FY2025 annual statements and H1 FY2026'} for k,v in values.items()}

@lru_cache(maxsize=3)
def company_facts(ticker):
    return json.loads((DATA/f'facts-{ticker}.json').read_text(encoding='utf-8'))

def fact(ticker,tag,end,start=None,unit='USD',required=True):
    data=company_facts(ticker)
    choices=[r for group in data['facts'].values() for r in group.get(tag,{}).get('units',{}).get(unit,[]) if r.get('end')==end and r.get('start')==start and r.get('filed','9999')<='2026-10-19' and r.get('form') in ('10-K','10-Q')]
    if not choices:
        if required:raise ValueError(f'Missing cutoff-eligible fact {ticker} {tag} {start} {end}')
        return None
    r=max(choices,key=lambda x:x['filed'])
    return {'value':r['val']/1e6,'unit':'USD millions' if unit=='USD' else 'million shares','tag':tag,'start':start,'end':end,'filed':r['filed'],'accession':r['accn'],'source':f'https://data.sec.gov/api/xbrl/companyfacts/CIK{ {"TGT":27419,"WMT":104169,"COST":909832}[ticker]:010}.json'}

@lru_cache(maxsize=4)
def close_observation(ticker):
    x=json.loads((DATA/f'prices-{ticker}.json').read_text())['chart']['result'][0]
    matches=[(i,t) for i,t in enumerate(x['timestamp']) if datetime.fromtimestamp(t).date()==date(2026,10,19)]
    if len(matches)!=1:raise ValueError('Unique October 19 market observation required')
    i,t=matches[0]
    return {'value':round(x['indicators']['quote'][0]['close'][i],2),'date':'2026-10-19','definition':'provider daily Close; chart timestamp marks session open, not the closing trade time','source':f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}','file':f'data/audit-2026-10-20/prices-{ticker}.json'}

def trailing_earnings(ticker):
    periods={'TGT':[('2025-02-02','2026-01-31'),('2026-02-01','2026-08-01'),('2025-02-02','2025-08-02')],
             'WMT':[('2025-02-01','2026-01-31'),('2026-02-01','2026-07-31'),('2025-02-01','2025-07-31')],
             'COST':[('2025-09-01','2026-08-30')]}[ticker]
    tags={'revenue':'Revenues' if ticker=='WMT' else 'RevenueFromContractWithCustomerExcludingAssessedTax','ebit':'OperatingIncomeLoss','net_income_common':'NetIncomeLoss','diluted_shares':'WeightedAverageNumberOfDilutedSharesOutstanding'}
    signs=[1,1,-1] if len(periods)==3 else [1]
    evidence=[];values={}
    days=[(date.fromisoformat(e)-date.fromisoformat(s)).days+1 for s,e in periods]
    total_days=sum(a*b for a,b in zip(signs,days))
    for name,tag in tags.items():
        records=[fact(ticker,tag,e,s,'shares' if name=='diluted_shares' else 'USD') for s,e in periods]
        evidence.extend(records)
        values[name]=sum(sign*r['value']*(n if name=='diluted_shares' else 1) for sign,r,n in zip(signs,records,days))/(total_days if name=='diluted_shares' else 1)
    values.update(eps=values['net_income_common']/values['diluted_shares'],start=(date.fromisoformat(periods[0][1])+__import__('datetime').timedelta(days=1-total_days)).isoformat() if len(periods)==1 else ('2025-08-03' if ticker=='TGT' else '2025-08-01'),end=periods[-2][1] if len(periods)==3 else periods[0][1],days=total_days,evidence=evidence)
    return values

def peer_comparisons(S,V):
    target=trailing_earnings('TGT');reserve_ratio=S['drivers']['minimum_cash']['value']/target['revenue']
    results=[]
    for t,bdate,sdate in [('TGT','2026-08-01','2026-08-21'),('WMT','2026-07-31','2026-08-26'),('COST','2026-08-30','2026-09-29')]:
        earnings=target if t=='TGT' else trailing_earnings(t)
        evidence=[]
        def val(tag,required=True):
            r=fact(t,tag,bdate,required=required)
            if r:evidence.append(r)
            return r['value'] if r else None
        basic=fact(t,'EntityCommonStockSharesOutstanding',sdate,unit='shares');evidence.append(basic)
        qstart={'TGT':'2026-05-03','WMT':'2026-05-01','COST':'2025-09-01'}[t]
        diluted=fact(t,'WeightedAverageNumberOfDilutedSharesOutstanding',bdate,qstart,'shares')
        ordinary=fact(t,'WeightedAverageNumberOfSharesOutstandingBasic',bdate,qstart,'shares')
        delta=max(diluted['value']-ordinary['value'],0);shares=basic['value']+delta
        evidence.extend([diluted,ordinary])
        if t=='TGT':
            cash=5411;debt=15357;nci=0;investments=0;derivatives=106
            notes=['Cash/debt at August 1; share count August 21; cutoff changes not asserted known.','Primary comparison uses reported TTM EBIT; tariff refund increases it by 994.','Deferred-compensation/life-insurance/pension and opening tax classifications differ from the expanded DCF bridge; this conventional trading EV is a qualified contextual proxy, not the expanded bridge.']
        elif t=='WMT':
            cash=val('CashAndCashEquivalentsAtCarryingValue');debt=sum(val(k) for k in ['ShortTermBorrowings','LongTermDebtCurrent','LongTermDebtNoncurrent','FinanceLeaseLiabilityCurrent','FinanceLeaseLiabilityNoncurrent'])
            nci=val('MinorityInterest')+293;investments=4867;derivatives=1337
            notes=['Redeemable NCI 293 plus nonredeemable NCI; Note 4 investment assets 4867 and derivative liabilities 1337 from July filing.','NCI/debt use carrying proxies; geographic mix, growth, grocery and advertising differ materially from Target.','P/E uses net income attributable to Walmart; consolidated operating profit includes NCI.']
        else:
            cash=val('CashAndCashEquivalentsAtCarryingValue')+1094;debt=sum(val(k) for k in ['LongTermDebtCurrent','LongTermDebtNoncurrent','FinanceLeaseLiabilityCurrent','FinanceLeaseLiabilityNoncurrent'])
            nci=0;investments=0;derivatives=0
            notes=['Cash includes 1094 of short-term investments; no short-term borrowings at fiscal year end, per Note 4.','No separate NCI or preferred balance in the consolidated balance sheet.','Membership-funded economics and geographic mix make this contextual rather than a core Target peer.']
        reserve=reserve_ratio*earnings['revenue'];excess=max(0,cash-reserve);price=close_observation(t)
        equity=price['value']*shares
        ev=equity+debt+nci+derivatives-excess-investments
        results.append({'ticker':t,'classification':'target' if t=='TGT' else 'contextual comparison; not core valuation peer','price':price,'balance_date':bdate,'share_date':sdate,'basic_shares_m':basic['value'],'dilution_proxy_m':delta,'valuation_shares_proxy_m':shares,'equity_value_m':equity,'debt_including_finance_leases_m':debt,'nci_including_redeemable_m':nci,'derivative_claims_m':derivatives,'cash_and_short_investments_m':cash,'operating_reserve_m':reserve,'eligible_excess_cash_m':excess,'other_investment_assets_m':investments,'conventional_EV_proxy_m':ev,'EV_EBIT':ev/earnings['ebit'],'P_E':price['value']/earnings['eps'],'earnings':earnings,'evidence':evidence,'limitations':notes+['Operating lease liabilities excluded because rent stays in EBIT.','Current diluted valuation shares are a proxy from latest cover shares and period dilution; not an award-by-award treasury-stock calculation.','Other claims, fair-value effects and restricted resources are not comprehensively measured for these contextual EV proxies; do not treat them as a core fair-value range.']})
    return {'policy':'docs/peer-policy-audit-amendment-2026-10-20.md','reserve_convention':reserve_ratio,'rows':results,'qualification':'Reported-period contextual EV/EBIT and P/E calculations; no core peer range, no averaging with DCF','normalized_target_EBIT_ex_tariff_m':target['ebit']-994,'normalization':'Remove the documented 994 tariff refund; transformation spending is not automatically added back; reported cash remains unchanged.'}

def training_case():
    cashflows=[];x=100
    for g in (.08,.06,.05,.04,.03):x*=1+g;cashflows.append(x)
    d=discount_cashflows(cashflows,[1,2,3,4,5],.10,.03,cashflows[-1]*1.03)
    equity,per_share=equity_from_enterprise(d['enterprise_value'],50,300,50)
    values={**{f'FCFF Year {i+1}':x for i,x in enumerate(cashflows)},'PV explicit FCFF':sum(d['pv_cashflows']),'Terminal value':d['terminal_value'],'PV terminal value':d['terminal_pv'],'Enterprise value':d['enterprise_value'],'Equity value':equity,'Per diluted share':per_share,'Terminal share':d['terminal_pv']/d['enterprise_value']}
    expected=[108,114.48,120.204,125.0122,128.7625,448.4408,1894.6486,1176.4277,1624.8685,1374.8685,27.4974,.7240]
    rows=[{'item':k,'published':e,'actual':a,'difference':a-e,'tolerance':.0001,'status':'pass' if abs(a-e)<.0001 else 'fail'} for (k,a),e in zip(values.items(),expected)]
    mini={'nopat':150*.75,'fcff':fcff_from_operating(150,.25,40,60,15),'equity':equity_from_enterprise(1000,100,250,100,-30)[0],'per_share':equity_from_enterprise(1000,100,250,100,-30)[1]}
    return {'source':'https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md','source_local':'course-materials/public-course/lessons/week-03/lab-05-dcf-build.md','checks':rows,'passed':sum(x['status']=='pass' for x in rows),'total':len(rows),'week_2_mini_case':mini,'qualification':'Uses the same discount_cashflows, fcff_from_operating and equity_from_enterprise primitives as the Target engine; published case differs from Target terminal reinvestment convention. Not the student AI-closed exercise.'}

def operating_sensitivities(S,V):
    base=run_valuation(S,V);b=base['scenarios']['base'];op=b['fcff'][1]['ebit'];fc=b['fcff'][1]['fcff'];value=b['partial_equity_bridge']['value_per_share_partial'];rows=[]
    settings=[('sales_growth','Sales growth',.01,.02),('cost_ex_da_rate','Cost / sales',.01,.005),('sga_rate','SG&A / sales',.005,.01),('capex_rate','Capex / sales',.01,.005)]
    for key,label,span,altspan in settings:
        for label_range,shock in [('primary',span),('alternative justified asymmetry',altspan)]:
            for sign in (-1,1):
                x=deepcopy(S);x['drivers'][key]['value'][1]+=sign*shock
                r=run_valuation(x,V)['scenarios']['base'];new=r['partial_equity_bridge']['value_per_share_partial']
                rows.append({'driver':label,'key':key,'range_set':label_range,'change':sign*shock,'change_percentage_points':sign*shock*100,'EBIT_change_m':r['fcff'][1]['ebit']-op,'FCFF_change_m':r['fcff'][1]['fcff']-fc,'value_change_per_share':new-value,'absolute_value_change':abs(new-value),'state_valid':not r['statement_check_failures']})
    rankings={}
    for range_set in ('primary','alternative justified asymmetry'):
        scores={name:max(abs(r['value_change_per_share']) for r in rows if r['driver']==name and r['range_set']==range_set) for _,name,_,_ in settings}
        rankings[range_set]=sorted(scores.items(),key=lambda x:x[1],reverse=True)
    return {'rows':rows,'rankings':rankings,'ranking_metric':'maximum absolute per-share effect across each symmetric low/high range; depends on economic shock width','range_basis':'Sales +/-1pp then +/-2pp tests demand uncertainty; merchandise cost +/-1pp then +/-0.5pp tests margin; SG&A +/-0.5pp then +/-1pp tests wage/fulfillment pressure; capex +/-1pp then +/-0.5pp tests investment policy. These are explicit stress assumptions, not statistical intervals.','interpretation':'Changing relative range widths can change rankings; simply halving every shock is not an independent range-robustness argument.'}

def build_bundle(S=None,V=None,include_sensitivities=True):
    if S is None:S,V=load_inputs()
    statements=run_analysis(S);valuation=run_valuation(S,V);base=valuation['scenarios']['base'];cutoff=statements['periods'][0]
    conditional=reverse_dcf(base['fcff'],valuation['wacc_components']['wacc'],V['terminal_incremental_roic']['value'],V['as_of'],cutoff,S['drivers']['minimum_cash']['value'],V['incremental_dilution']['value'],V['market_price'],V['other_claims_and_nonoperating_assets']['value'],allow_conditional=True)
    checks=statements['checks']+valuation['checks']
    result={'status':'CONDITIONAL ANALYSIS; watch/defer and conditional policies confirmed; protected validation pending','as_of':V['as_of'],'run_time':datetime.now().astimezone().isoformat(),'units':'USD millions; shares millions; per-share USD','material_inputs':{'statements':S,'valuation':V},'statements':statements,'valuation':valuation,'fcff':base['fcff'],'wacc':valuation['wacc_components'],'equity_bridge':base['partial_equity_bridge'],'partial_equity_bridge':base['partial_equity_bridge'],'low_base_high':{k:v['partial_equity_bridge']['value_per_share_partial'] for k,v in valuation['scenarios'].items()},'terminal':base['dcf']['terminal'],'wacc_growth_sensitivity':valuation['wacc_growth_sensitivity'],'conditional_reverse_dcf':conditional,'market_price':V['market_price'],'conditional_gap_vs_price':base['partial_equity_bridge']['value_per_share_partial']/V['market_price']['value']-1,'peer_comparisons':peer_comparisons(S,V),'known_answer':training_case(),'checks':checks,'check_summary':{'pass':sum(c['status']=='pass' for c in checks),'fail':sum(c['status']=='fail' for c in checks)},'student_action':json.loads((ROOT/'data/student-decisions.json').read_text(encoding='utf-8'))['recommendation'],'pending_human_requirements':['protected pre-run prediction/execution','actual credited partner-feedback evidence','Edition A receipt/switch evidence','recordings/transcripts/repository/video access']}
    if include_sensitivities:result['operating_sensitivities']=operating_sensitivities(S,V)
    combined=[]
    for case,scenario in valuation['scenarios'].items():
        for rate in (valuation['wacc_components']['wacc']-.01,valuation['wacc_components']['wacc']+.01):
            for growth in (.01,.03):
                ev=present_value(scenario['fcff'],rate,growth,V['terminal_incremental_roic']['value'],V['as_of'])['enterprise_value']
                per_share=enterprise_bridge(ev,cutoff,S['drivers']['minimum_cash']['value'],V['incremental_dilution']['value'],V['other_claims_and_nonoperating_assets']['value'])['value_per_share_partial']
                combined.append({'operating_case':case,'wacc':rate,'growth':growth,'value_per_share':per_share})
    result['combined_stress_envelope']={'low':min(x['value_per_share'] for x in combined),'high':max(x['value_per_share'] for x in combined),'cases':combined,'interpretation':'Combined operating/WACC/growth stress, not a probability interval; ranges are chosen modeling assumptions.'}
    result['historical_reference_bands']=historical_reference_bands()
    result['proposed_monitoring_policy']=[{'metric':'reported comparable-sales growth','condition':'non-positive for two consecutive reports','window':'quarterly, within five business days of release','owner':'coverage analyst, assignment pending','response':'revisit recovery growth and watch/defer recommendation','student_approved':False},{'metric':'recurring operating margin after a disclosed normalization bridge','condition':'below 4.5% for two consecutive quarters','window':'quarterly','owner':'coverage analyst, assignment pending','response':'rerun downside case and reconsider initiation eligibility','student_approved':False},{'metric':'inventory growth versus sales growth in matching seasonal periods','condition':'inventory growth exceeds sales growth by over 5 percentage points for two consecutive quarters','window':'quarterly, same seasonal period','owner':'coverage analyst, assignment pending','response':'review markdown exposure, turnover assumptions and liquidity','student_approved':False},{'metric':'required accounting/source checks','condition':'any required reconciliation fails or a load-bearing source cannot be reproduced','window':'each filing/model update','owner':'coverage analyst, assignment pending','response':'stop reliance on valuation until corrected','student_approved':False}]
    decisions=json.loads((ROOT/'data/student-decisions.json').read_text(encoding='utf-8'))
    result['student_source_check']=decisions['source_check']
    result['student_ai_output_review']=decisions['ai_output_review']
    result['student_assumptions']=decisions['assumptions']
    result['monitoring_policy']=decisions['monitoring_policy']
    result['proposed_monitoring_policy']=decisions['monitoring_policy']['rules']
    result['entry_policy']={**decisions['entry_policy'],'current_base_value':result['low_base_high']['base'],'entry_screen':result['low_base_high']['base']*(1-decisions['entry_policy']['discount_to_current_base'])}
    version_files=['financial_engine.py','valuation_engine.py','audit_analysis.py','analysis.py','app.py','data/model-inputs-step6.json','data/model-inputs-step7.json','data/student-decisions.json']
    result['source_version']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in version_files}
    result['version_id']='target-audit-'+hashlib.sha256(json.dumps(result['source_version'],sort_keys=True).encode()).hexdigest()[:16]
    return result

def export_bundle():
    b=build_bundle();(ROOT/'visible_output.json').write_text(json.dumps(b,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (ROOT/'outputs'/'known-answer-reconciliation.json').write_text(json.dumps(b['known_answer'],indent=2),encoding='utf-8')
    (ROOT/'data'/'audit-peer-comparisons.json').write_text(json.dumps(b['peer_comparisons'],indent=2),encoding='utf-8')
    (ROOT/'data'/'step9-sensitivities.json').write_text(json.dumps(b['operating_sensitivities'],indent=2),encoding='utf-8')
    return b
