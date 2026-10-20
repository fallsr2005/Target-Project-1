"""Illustrative FCFF valuation; not a recommendation or a validated output."""
from copy import deepcopy
from datetime import date
from math import isfinite
from financial_engine import run_analysis


def fcff_from_operating(ebit,tax_rate,da,capex,increase_nwc):
    nopat=ebit-max(ebit,0)*tax_rate
    return nopat+da-capex-increase_nwc

def discount_cashflows(cashflows,years,wacc,g,terminal_cashflow):
    if len(cashflows)!=len(years) or not cashflows or not all(isfinite(x) for x in cashflows+years+[wacc,g,terminal_cashflow]):
        raise ValueError('Finite dated cash flows required')
    if wacc<=g or g<0 or wacc<=-1 or any(t<=0 for t in years): raise ValueError('Invalid discount/growth/time boundary')
    pv=[c/(1+wacc)**t for c,t in zip(cashflows,years)]
    terminal=terminal_cashflow/(wacc-g)
    terminal_pv=terminal/(1+wacc)**years[-1]
    return {'pv_cashflows':pv,'terminal_value':terminal,'terminal_pv':terminal_pv,'enterprise_value':sum(pv)+terminal_pv}

def equity_from_enterprise(ev,excess_cash,debt,shares,other=0):
    if shares<=0 or not all(isfinite(v) for v in (ev,excess_cash,debt,shares,other)):raise ValueError('Invalid equity bridge')
    eq=ev+excess_cash-debt+other
    return eq,eq/shares

def annual_wacc(config):
    v=lambda k:config[k]['value']
    rf,erp,beta,kd,tax,ew,dw=(v(k) for k in ('risk_free','equity_risk_premium','equity_beta','new_debt_cost','tax_shield_rate','equity_weight','debt_weight'))
    if not all(isfinite(x) for x in (rf,erp,beta,kd,tax,ew,dw)) or not 0<=tax<=1 or min(ew,dw,kd)<0 or abs(ew+dw-1)>1e-9: raise ValueError('Invalid WACC components or weights')
    ke=rf+beta*erp
    return {'risk_free':rf,'erp':erp,'beta':beta,'equity_cost':ke,'debt_cost_pretax':kd,'tax_shield_rate':tax,'equity_weight':ew,'debt_weight':dw,'wacc':ew*ke+dw*kd*(1-tax)}

def enterprise_bridge(ev, cutoff, minimum_cash, dilution, other_claims=None):
    if not all(isfinite(x) for x in (ev,minimum_cash,dilution)) or minimum_cash<0 or dilution<0: raise ValueError('Invalid bridge inputs')
    bs=cutoff['balance_sheet']; cash=bs['cash']; debt=bs['debt_total']
    eligible=max(cash-minimum_cash,0.0); reserve=min(cash,minimum_cash)
    basic_shares=cutoff.get('schedules',{}).get('basic_shares_millions',454.291461)
    shares=basic_shares+dilution
    if shares<=0: raise ValueError('Valuation shares must be positive')
    equity=ev+eligible-debt
    if other_claims is not None:
        if not isfinite(other_claims): raise ValueError('Invalid other-claims adjustment')
        equity+=other_claims
    equity,per_share=equity_from_enterprise(ev,eligible,debt,shares,0 if other_claims is None else other_claims)
    source='https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm'
    items=[{'name':'eligible excess cash','signed_amount':eligible,'unit':'USD millions','as_of':'2026-10-19 estimated','definition':'estimated cutoff cash less the provisional operating cash reserve, limited to available cash','source':source,'locator':'p.3 August cash; Step 6 elapsed-period roll-forward','uncertainty':'estimated October cash and $1,000m reserve are unverified; no forecast ending cash added'},
           {'name':'debt including finance leases','signed_amount':-debt,'unit':'USD millions','as_of':'2026-10-19 estimated','definition':'total interest-bearing debt including finance leases once','source':source,'locator':'p.3 August current and noncurrent debt; Step 6 elapsed-period roll-forward','uncertainty':'carrying value, not market debt; August lease and cutoff changes uncertain'},
           {'name':'other claims and non-operating assets','signed_amount':other_claims,'unit':'USD millions','as_of':'2026-10-19','definition':'net nonoperating asset additions less non-common claims, not otherwise counted','source':source,'locator':'notes and balance sheet, classifications incomplete','uncertainty':'unknown; omitted from partial result rather than asserted zero'},
           {'name':'operating lease liability','signed_amount':None,'unit':'USD millions','as_of':'2026-10-19','definition':'not separately deducted under rent-in-EBIT/FCFF convention','source':source,'locator':'p.3 and p.21','uncertainty':'consistency with WACC and future peers must be reviewed'}]
    return {'enterprise_value':ev,'bridge_items':items,'cash_reported_august_1':5411.0,'debt_reported_august_1':15357.0,'cash_estimated_at_cutoff':cash,'estimated_operating_cash_retained':reserve,'estimated_eligible_excess_cash':eligible,'debt_estimated_at_cutoff':debt,'debt_adjustment':-debt,'other_claims_and_nonoperating_assets_adjustment':other_claims,'other_claims_status':'unresolved: illustrative partial bridge omits unknown items' if other_claims is None else 'provided net adjustment','operating_lease_adjustment':None,'operating_lease_policy':'rent remains in operating cash flows; no separate liability deduction under chosen policy','finance_lease_policy':'finance lease debt included once in total debt','equity_value_partial':equity,'shares_outstanding_august_millions':basic_shares,'incremental_dilution_proxy_millions':dilution,'estimated_diluted_shares_millions':shares,'shares_source':source+' cover and p.1; August 21 common shares plus Q2 diluted-less-basic weighted average as a proxy','shares_date':'August 21, 2026 cover count; October 19 estimate','shares_uncertainty':'award-based and subsequent share changes unverified','value_per_share_partial':per_share,'value_per_share':per_share,'equity_value':equity,'bridge_status':'conditional itemized carrying-value estimate' if other_claims is not None else 'incomplete'}

def model_fcff(statement, tax_rate):
    rows=[]
    for p in statement['periods']:
        if p['classification']!='future provisional forecast': continue
        i=p['income_statement']; cf=p['cash_flow_statement']; sched=p['schedules']
        ebit=i['operating_income']; op_tax=max(ebit,0)*tax_rate; nopat=ebit-op_tax
        da=sched['total_da']; capex=-cf['capex']; change_wc=-cf['working_capital_cash_change']
        fcff=fcff_from_operating(ebit,tax_rate,da,capex,change_wc)
        alternate=cf['operating_cash_flow']+i['interest']+i['tax']-op_tax-capex
        rows.append({'period':p['period'],'period_end':p['end'],'ebit':ebit,'operating_tax':op_tax,'nopat':nopat,'total_da':da,'capex':capex,'increase_operating_working_capital':change_wc,'fcff':fcff,'cash_flow_statement_reconciliation':alternate,'reconciliation_difference':fcff-alternate})
    return rows

def present_value(rows,wacc,g,roic,as_of):
    if not all(isfinite(x) for x in (wacc,g,roic)) or wacc<=g or wacc<=-1 or g<0 or roic<=0 or g>=roic: raise ValueError('Require WACC > growth >= 0 and incremental ROIC > growth')
    if len(rows)!=6: raise ValueError('Expected future stub and five full fiscal years')
    start=date.fromisoformat(as_of[:10]); discounted=[]
    for r in rows:
        days=(date.fromisoformat(r['period_end'])-start).days
        if days<=0: raise ValueError('Discounted periods must end after cutoff')
        years=days/365; discounted.append({'period':r['period'],'end':r['period_end'],'actual_days':days,'years_actual_365':years,'fcff':r['fcff'],'present_value':r['fcff']/(1+wacc)**years})
    last=rows[-1]
    if last['nopat']<=0: raise ValueError('Terminal NOPAT must be positive under this steady-state method')
    next_nopat=last['nopat']*(1+g); reinvestment=next_nopat*g/roic
    next_fcff=next_nopat-reinvestment
    calc=discount_cashflows([r['fcff'] for r in rows],[r['years_actual_365'] for r in discounted],wacc,g,next_fcff)
    tv=calc['terminal_value'];tv_pv=calc['terminal_pv'];ev=calc['enterprise_value']
    return {'discounted_periods':discounted,'terminal':{'measurement_date':last['period_end'],'growth':g,'incremental_roic':roic,'reinvestment_fraction':g/roic,'next_year_nopat':next_nopat,'next_year_reinvestment':reinvestment,'next_year_fcff':next_fcff,'terminal_value':tv,'present_value':tv_pv,'share_of_enterprise_value':tv_pv/ev if ev else None},'enterprise_value':ev}

def price_is_documented(price_info,as_of):
    return (isinstance(price_info,dict) and isinstance(price_info.get('source_url'),str)
        and price_info['source_url'].startswith('https://') and price_info.get('timestamp')==as_of
        and bool(price_info.get('definition')) and isinstance(price_info.get('value'),(float,int))
        and isfinite(price_info['value']) and price_info['value']>0)

def price_is_accepted(price_info,as_of):
    return price_is_documented(price_info,as_of) and price_info.get('accepted_by_student') is True

def reverse_dcf(rows,wacc,roic,as_of,cutoff,minimum_cash,dilution,price_info,other_claims=None,low=0.0,high=0.05,allow_conditional=False):
    accepted=price_is_accepted(price_info,as_of)
    documented=price_is_documented(price_info,as_of)
    if not accepted and not (allow_conditional and documented):
        return {'status':'pending: accepted cutoff market price and documentation required','solved_growth':None}
    if high<=low or high>=min(wacc,roic): raise ValueError('Reverse-DCF search bounds invalid')
    def per_share(g):return enterprise_bridge(present_value(rows,wacc,g,roic,as_of)['enterprise_value'],cutoff,minimum_cash,dilution,other_claims)['value_per_share_partial']
    a,b=per_share(low),per_share(high);target=price_info['value']
    if not min(a,b)<=target<=max(a,b):return {'status':'no solution in chosen growth interval','solved_growth':None,'endpoint_values':[a,b]}
    increasing=b>a
    if abs(b-a)<1e-12:return {'status':'non-identifiable across interval','solved_growth':None}
    for _ in range(100):
        mid=(low+high)/2
        if (per_share(mid)<target)==increasing:low=mid
        else:high=mid
    return {'status':'solved under conditional provider convention; student decision pending' if not accepted else 'solved under documented accepted convention','solved_growth':(low+high)/2,'student_price_acceptance':accepted,'search_bounds':[0,0.05],'fixed_inputs':['WACC','operating forecast','incremental ROIC','cash/debt/claims','diluted shares'],'solved_variable':'perpetual terminal growth'}

def run_valuation(statement_inputs,config):
    cap=annual_wacc(config); wacc=cap['wacc']; g=config['terminal_growth']['value']; roic=config['terminal_incremental_roic']['value']; asof=config['as_of']
    base_statement=run_analysis(statement_inputs); cutoff=base_statement['periods'][0]
    floor=statement_inputs['drivers']['minimum_cash']['value']; dilution=config['incremental_dilution']['value']; other=config['other_claims_and_nonoperating_assets']['value']
    tax=statement_inputs['drivers']['tax_rate']['value']
    scenarios={}
    for name in ('low','base','high'):
        inp=deepcopy(statement_inputs)
        if name!='base':
            # Alter full years only; keep the common as-of estimate and stub fixed.
            shift=1 if name=='low' else -1
            for j in range(1,6):
                inp['drivers']['sales_growth']['value'][j]+=(-.01 if name=='low' else .01)
                inp['drivers']['cost_ex_da_rate']['value'][j]+=shift*.008
                inp['drivers']['sga_rate']['value'][j]+=shift*.003
                inp['drivers']['capex_rate']['value'][j]+=.005 if name=='high' else 0.0
        st=base_statement if name=='base' else run_analysis(inp)
        rows=model_fcff(st,tax); valuation=present_value(rows,wacc,g,roic,asof)
        bridge=enterprise_bridge(valuation['enterprise_value'],cutoff,floor,dilution,other)
        bridge['other_claim_details']=config.get('bridge_claim_items',[])
        bridge['classification_notes']=config.get('bridge_classification_notes',[])
        failed=[x for x in st['checks'] if x['status']=='fail']
        scenario_changes={'FY2027_FY2031_sales_growth_shift':(-.01 if name=='low' else .01 if name=='high' else 0),'FY2027_FY2031_cost_rate_shift':(.008 if name=='low' else -.008 if name=='high' else 0),'FY2027_FY2031_sga_rate_shift':(.003 if name=='low' else -.003 if name=='high' else 0),'FY2027_FY2031_capex_rate_shift':(.005 if name=='high' else 0),'common_cutoff_and_FY2026_stub':True}
        scenarios[name]={'input_changes_from_base':scenario_changes,'fcff':rows,'dcf':valuation,'partial_equity_bridge':bridge,'statement_check_failures':failed,'scenario_status':'provisional; financing feasibility failures' if failed else 'conditional estimate; student accepts use with disclosed evidence limitations'}
    sensitivity=[]
    for rate in (wacc-.01,wacc,wacc+.01):
        row=[]
        for growth in (.01,.02,.03):
            r=present_value(scenarios['base']['fcff'],rate,growth,roic,asof)
            row.append({'wacc':rate,'growth':growth,'partial_value_per_share':enterprise_bridge(r['enterprise_value'],cutoff,floor,dilution,other)['value_per_share_partial']})
        sensitivity.extend(row)
    reverse=reverse_dcf(scenarios['base']['fcff'],wacc,roic,asof,cutoff,floor,dilution,config['market_price'],other)
    checks=[{'name':'FCFF reconciliation '+r['period'],'difference':r['reconciliation_difference'],'status':'pass' if abs(r['reconciliation_difference'])<1e-6 else 'fail'} for r in scenarios['base']['fcff']]
    checks.append({'name':'six future periods, elapsed excluded','difference':len(scenarios['base']['fcff'])-6,'status':'pass' if len(scenarios['base']['fcff'])==6 and all(r['period']!='elapsed estimate' for r in scenarios['base']['fcff']) else 'fail'})
    for name in ('low','high'):
        n=len(scenarios[name]['statement_check_failures'])
        checks.append({'name':name+' scenario feasibility','difference':n,'status':'pass' if n==0 else 'fail'})
    bridge=scenarios['base']['partial_equity_bridge']
    difference=bridge['equity_value']-(bridge['enterprise_value']+bridge['estimated_eligible_excess_cash']-bridge['debt_estimated_at_cutoff']+(other or 0))
    checks.append({'name':'enterprise-to-equity signed bridge','difference':difference,'status':'pass' if abs(difference)<1e-6 else 'fail'})
    if config.get('bridge_claim_items'):
        difference=sum(i['signed_amount'] for i in config['bridge_claim_items'])-other
        checks.append({'name':'itemized other-claims total','difference':difference,'status':'pass' if abs(difference)<1e-6 else 'fail'})
    return {'status':'CONDITIONAL MODEL ESTIMATE; assumptions accepted for use; protected validation pending','as_of':asof,'units':'USD millions and million shares; per-share values USD','valuation_inputs':config,'statement_input_reference':'data/model-inputs-step6.json','wacc_components':cap,'scenarios':scenarios,'wacc_growth_sensitivity':sensitivity,'reverse_dcf':reverse,'market_price':config.get('market_price'),'upside_downside':{'value':scenarios['base']['partial_equity_bridge']['value_per_share']/config['market_price']['value']-1,'basis':'provider daily Close, accepted for conditional use' if config['market_price'].get('accepted_by_student') else 'provider daily Close, acceptance pending'},'checks':checks,'evidence_warnings':base_statement['evidence_warnings']+['Incremental ROIC, beta, marginal debt cost and capital weights provisional.','Cutoff cash/debt are estimated; other assets and claims use explicit itemized carrying-value/classification assumptions.','Terminal steady state uses an assumed ROIC and reinvestment policy; detailed asset reconciliation remains pending.','The specified equity bridge remains conditional on stale claim estimates, dilution and cash-reserve judgments; sensitivity is required.']}
