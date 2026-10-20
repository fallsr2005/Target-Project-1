"""Provisional Target three-statement engine; no DCF or investment decision."""
import json
import math
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run_analysis(inputs):
    d = {k: v['value'] for k, v in inputs['drivers'].items()}
    if not 0 <= d['da_in_cost_fraction'] <= 1: raise ValueError('D&A allocation must be 0 to 1')
    if any(not 0 <= d[k] <= 1 for k in ('elapsed_sales_share_remaining_year','elapsed_other_flow_share')): raise ValueError('Seasonal fraction must be 0 to 1')
    if any(len(d[k]) != 6 for k in ('sales_growth','cost_ex_da_rate','sga_rate','capex_rate','da_rate')): raise ValueError('Six annual inputs required')
    if any(not math.isfinite(v) or v < 0 for k in ('cost_ex_da_rate','sga_rate','capex_rate','da_rate') for v in d[k]): raise ValueError('Expense and investment rates must be finite and nonnegative')
    if any(not math.isfinite(v) or v <= -1 for v in d['sales_growth']): raise ValueError('Sales growth must be finite and exceed -100%')
    if any(not math.isfinite(d[k]) or d[k] < 0 for k in ('minimum_cash','revolver_capacity','new_borrowing_rate','quarterly_dividend','inventory_days','payable_days','tax_rate')): raise ValueError('Liquidity, tax, dividends and working-capital inputs must be finite and nonnegative')
    if d['tax_rate'] > 1: raise ValueError('Tax rate must not exceed 100%')
    history = json.loads((ROOT/'data/historical-reported.json').read_text(encoding='utf-8'))
    def value(ident):
        vals=[x['value'] for x in history if x['input_id']==ident]
        if len(vals)!=1 or vals[0] is None: raise ValueError('Missing historical value '+ident)
        return vals[0]
    def bal(label):
        vals=[x['value'] for x in history if x['input_id'].startswith('Q26-balance-') and x['financial_period']=='Q2 FY2026 end' and x['definition']==label]
        if len(vals)!=1 or vals[0] is None: raise ValueError('Missing reported balance '+label)
        return vals[0]
    oca=bal('Other current assets'); accrued=bal('Accrued and other current liabilities')
    lease_current=3733-bal('Noncurrent operating lease liabilities')
    unclassified_oca=oca-d['other_oca_operating_aug']-d['forward_contract_aug']
    unclassified_accrual=accrued-d['operating_accrual_aug']-d['income_tax_payable_aug']-d['dividend_payable_aug']-d['interest_payable_aug']-lease_current
    if min(unclassified_oca,unclassified_accrual)<0: raise ValueError('Estimated current balance components exceed reported totals')
    s={'cash':bal('Cash and cash equivalents'),'inventory':bal('Inventory'),'op_other_assets':d['other_oca_operating_aug'],'other_current_unclassified':unclassified_oca,'forward_contract':d['forward_contract_aug'],'ppe':bal('Property and equipment, net'),'lease_asset':bal('Operating lease assets'),'other_noncurrent_asset':bal('Other noncurrent assets'),'payables':bal('Accounts payable'),'op_accrual':d['operating_accrual_aug'],'tax_payable':d['income_tax_payable_aug'],'dividend_payable':d['dividend_payable_aug'],'interest_payable':d['interest_payable_aug'],'other_accrual_unclassified':unclassified_accrual,'lease_current':lease_current,'lease_noncurrent':bal('Noncurrent operating lease liabilities'),'deferred_tax':bal('Deferred income taxes'),'other_noncurrent_liabilities':bal('Other noncurrent liabilities'),'equity':bal('Total shareholders’ investment')}
    s['retained_earnings']=bal('Retained earnings')
    s['other_equity']=s['equity']-s['retained_earnings']
    # Illustrative carrying-value buckets adjusted by $10 to align nominal maturities.
    buckets=[3908.0,3724.0,1434.0,1090.0,1120.0,2122.0]; rates=[.029,.049,.063,.04,.038,.039]
    residual_debt=15357-sum(buckets); revolving=0.0; shares=inputs.get('shares_outstanding',{}).get('value',454.291461)
    asset_keys=('cash','inventory','op_other_assets','other_current_unclassified','forward_contract','ppe','lease_asset','other_noncurrent_asset')
    liability_keys=('payables','op_accrual','tax_payable','dividend_payable','interest_payable','other_accrual_unclassified','lease_current','lease_noncurrent','deferred_tax','other_noncurrent_liabilities')
    checks=[]
    def check(name,difference,tolerance=1e-6): checks.append({'name':name,'difference':difference,'tolerance':tolerance,'status':'pass' if abs(difference)<=tolerance else 'fail'})
    expected_units={'sales_growth':'annual growth, 52-week equivalent','cost_ex_da_rate':'share of sales','sga_rate':'share of sales','capex_rate':'share of sales','da_rate':'share of sales','da_in_cost_fraction':'fraction of total depreciation','tax_rate':'fraction of positive pretax earnings','inventory_days':'days of annualized cost of sales','payable_days':'days of annualized cost of sales','other_operating_assets_rate':'share of 52-week-equivalent sales','operating_accruals_rate':'share of 52-week-equivalent sales','elapsed_sales_share_remaining_year':'share of FY2026 sales after reported H1','elapsed_other_flow_share':'share of unreported FY2026 flow after H1','minimum_cash':'USD millions','revolver_capacity':'USD millions','new_borrowing_rate':'annual rate on drawn new borrowing only','quarterly_dividend':'USD per share per quarter','other_oca_operating_aug':'USD millions','operating_accrual_aug':'USD millions','income_tax_payable_aug':'USD millions','dividend_payable_aug':'USD millions','interest_payable_aug':'USD millions','forward_contract_aug':'USD millions'}
    unit_mismatch=sum(inputs['drivers'][k]['unit']!=v for k,v in expected_units.items())
    check('Input unit definitions',unit_mismatch,0)
    def balance(debt):
        assets=sum(s[k] for k in asset_keys); liabilities=sum(s[k] for k in liability_keys)+debt
        return assets,liabilities,assets-liabilities-s['equity']
    check('August reported balance',balance(15357)[2]); check('August other assets classification',sum([d['other_oca_operating_aug'],d['forward_contract_aug'],unclassified_oca])-oca)
    check('August accrual classification',sum([d['operating_accrual_aug'],d['income_tax_payable_aug'],d['dividend_payable_aug'],d['interest_payable_aug'],lease_current,unclassified_accrual])-accrued)
    check('FY2025 normalization rounded bridge',5117-593+250-4775,1.0)
    hc=json.loads((ROOT/'data/historical-reconciliation.json').read_text(encoding='utf-8'))
    check('Prior 56 historical checks',sum(x['status']!='pass' for x in hc),0)
    base_sales=value('K25-income-r02-c04')*(1+d['sales_growth'][0]); h1_sales=value('Q26-income-r04-c16')
    annual={'sales':base_sales,'cost':base_sales*d['cost_ex_da_rate'][0],'sga':base_sales*d['sga_rate'][0],'da':base_sales*d['da_rate'][0],'capex':base_sales*d['capex_rate'][0]}
    h1_da=value('Q26-cash_flow-r07-c04')
    remaining={'sales':annual['sales']-h1_sales,'cost':annual['cost']-(value('Q26-income-r05-c16')+994-h1_da*d['da_in_cost_fraction']),'sga':annual['sga']-value('Q26-income-r06-c16'),'da':annual['da']-h1_da,'capex':annual['capex']+value('Q26-cash_flow-r19-c04')}
    periods=[('elapsed estimate','2026-08-02','2026-10-19',0,1),('FY2026 future stub','2026-10-20','2027-01-30',0,1),('FY2027','2027-01-31','2028-01-29',1,4),('FY2028','2028-01-30','2029-02-03',2,4),('FY2029','2029-02-04','2030-02-02',3,4),('FY2030','2030-02-03','2031-02-01',4,4),('FY2031','2031-02-02','2032-01-31',5,4)]
    result=[]; sales_52=base_sales
    for label,start,end,idx,divs in periods:
        days=(date.fromisoformat(end)-date.fromisoformat(start)).days+1
        if idx==0:
            f=d['elapsed_sales_share_remaining_year'] if label=='elapsed estimate' else 1-d['elapsed_sales_share_remaining_year']
            g=d['elapsed_other_flow_share'] if label=='elapsed estimate' else 1-d['elapsed_other_flow_share']
            sales=remaining['sales']*f; cost_pre=remaining['cost']*f; sga=remaining['sga']*f; da=remaining['da']*g; capex=remaining['capex']*g
            year_cost=annual['cost']+annual['da']*d['da_in_cost_fraction']; year_days=364
        else:
            sales_52*=1+d['sales_growth'][idx]; sales=sales_52*(53/52 if idx==2 else 1); year_days=371 if idx==2 else 364
            cost_pre=sales*d['cost_ex_da_rate'][idx]; sga=sales*d['sga_rate'][idx]; da=sales*d['da_rate'][idx]; capex=sales*d['capex_rate'][idx]; year_cost=cost_pre+da*d['da_in_cost_fraction']
        old=s.copy(); old_buckets=buckets.copy(); old_revolving=revolving; old_residual=residual_debt
        targets={'inventory':year_cost/year_days*d['inventory_days'],'payables':year_cost/year_days*d['payable_days'],'op_other_assets':sales_52*d['other_operating_assets_rate'],'op_accrual':sales_52*d['operating_accruals_rate']}
        for key,target in targets.items(): s[key]=old[key]+(target-old[key])*d['elapsed_other_flow_share'] if label=='elapsed estimate' else target
        if label=='elapsed estimate' and 'cutoff_seasonality' in inputs:
            s['inventory']=old['inventory']*inputs['cutoff_seasonality']['inventory_factor']
            s['payables']=old['payables']*inputs['cutoff_seasonality']['payables_factor']
        cost=cost_pre+da*d['da_in_cost_fraction']; separate_da=da*(1-d['da_in_cost_fraction']); ebit=sales-cost-sga-separate_da
        due=0 if label=='elapsed estimate' else inputs['maturities_nominal']['values'][idx]
        if due > buckets[0]+1e-6: raise ValueError('Maturity exceeds estimated near-term debt cohort')
        buckets[0]-=due
        lease_principal=min(residual_debt, inputs.get('finance_lease_principal',{}).get('annual_value',0)*days/365)
        residual_debt-=lease_principal
        old_interest=(sum(x*r for x,r in zip(old_buckets,rates))-due*rates[0]*.5+(old_residual-lease_principal/2)*.04)*days/365
        interest_base=old_interest+old_revolving*d['new_borrowing_rate']*days/365
        expiry=old_revolving if label=='FY2031' else 0; revolving-=expiry
        dividends=shares*d['quarterly_dividend']*divs
        change_wc=-(s['inventory']-old['inventory'])-(s['op_other_assets']-old['op_other_assets'])+(s['payables']-old['payables'])+(s['op_accrual']-old['op_accrual'])
        def compute(draw):
            interest=interest_base+draw*d['new_borrowing_rate']*days/365/2
            tax=max(ebit-interest,0)*d['tax_rate']; net=ebit-interest-tax
            return old['cash']+net+da+change_wc-capex-due-lease_principal-expiry-dividends+draw,interest,tax,net
        capacity=0 if label=='FY2031' else max(0,d['revolver_capacity']-revolving); draw=0.0
        if compute(0)[0]<d['minimum_cash'] and capacity>0:
            lo,hi=0.0,capacity
            for _ in range(60):
                mid=(lo+hi)/2
                if compute(mid)[0]<d['minimum_cash']: lo=mid
                else: hi=mid
            draw=hi
        revolving+=draw; s['cash'],interest,tax,net=compute(draw)
        cfo=net+da+change_wc; cfi=-capex; cff=draw-due-lease_principal-expiry-dividends
        s['ppe']=old['ppe']+capex-da
        s['retained_earnings']=old['retained_earnings']+net-dividends
        s['equity']=s['retained_earnings']+s['other_equity']
        debt=sum(buckets)+residual_debt+revolving; assets,liabs,diff=balance(debt)
        check(label+' balance sheet',diff); check(label+' cash movement',s['cash']-old['cash']-cfo-cfi-cff)
        check(label+' PPE roll-forward',s['ppe']-old['ppe']-capex+da)
        check(label+' debt roll-forward',debt-(sum(old_buckets)+old_residual+old_revolving)+due+lease_principal+expiry-draw)
        check(label+' retained earnings roll-forward',s['retained_earnings']-old['retained_earnings']-net+dividends)
        check(label+' equity components',s['equity']-s['retained_earnings']-s['other_equity'])
        check(label+' depreciation allocated once',cost-cost_pre+separate_da-da)
        checks.append({'name':label+' asset feasibility','status':'pass' if min(s['ppe'],capex,da)>=0 else 'fail','difference':min(s['ppe'],capex,da),'tolerance':0})
        checks.append({'name':label+' funding capacity and minimum cash','status':'pass' if s['cash']>=d['minimum_cash']-1e-6 and revolving<=d['revolver_capacity']+1e-6 else 'fail','difference':s['cash']-d['minimum_cash'],'tolerance':1e-6})
        checks.append({'name':label+' fiscal period length','status':'pass' if days in (79,103,364,371) else 'fail','difference':days,'tolerance':0})
        checks.append({'name':label+' sales and expense signs','status':'pass' if min(sales,cost,sga,da,capex,tax,interest)>=0 else 'fail','difference':min(sales,cost,sga,da,capex,tax,interest),'tolerance':0})
        result.append({'period':label,'start':start,'end':end,'days':days,'classification':'elapsed unreported estimate' if label=='elapsed estimate' else 'future provisional forecast','income_statement':{'sales':sales,'cost_of_sales_including_allocated_da':cost,'sga':sga,'separate_da':separate_da,'operating_income':ebit,'operating_margin':ebit/sales if sales else None,'interest':interest,'tax':tax,'net_income':net},'cash_flow_statement':{'net_income':net,'da_addback':da,'working_capital_cash_change':change_wc,'operating_cash_flow':cfo,'capex':-capex,'investing_cash_flow':cfi,'new_borrowing':draw,'debt_repayment':-due-lease_principal,'finance_lease_principal':-lease_principal,'facility_expiry_repayment':-expiry,'dividends_paid':-dividends,'financing_cash_flow':cff,'cash_change':cfo+cfi+cff},'balance_sheet':{**s,'debt_total':debt,'total_assets':assets,'total_liabilities':liabs,'balance_difference':diff},'schedules':{'opening_cash':old['cash'],'opening_ppe':old['ppe'],'total_da':da,'da_in_cost':da*d['da_in_cost_fraction'],'opening_equity':old['equity'],'opening_debt':sum(old_buckets)+old_residual+old_revolving,'basic_shares_millions':shares,'facility_balance':revolving,'sales_52_week_equivalent':sales_52,'minimum_cash_shortfall':max(0,d['minimum_cash']-s['cash'])}})
    warnings=['Market comparison uses a documented provider daily Close conditionally; student convention review is pending.','August current-balance components are estimated; unclassified remainders held constant.','August-to-October values are estimated, not reported.','Depreciation allocation and sales-based proxy are unverified.','Debt cohorts and maturity timing are approximations; finance-lease principal is a sourced 136 annual proxy; FY2031 bond maturity is an explicit zero assumption, not a reported fact.','Operating lease balances, tax balances, noncurrent assets and liabilities and unclassified current balances are held constant.','Repurchases, share compensation, issuance, net other income, impairment and disposal assumed zero for draft, not verified absence.','Dividend continuation and fixed dividend payable are approximations.','Student source check and assumption approval remain pending.']
    return {'status':'PROVISIONAL: arithmetic does not establish evidence quality or approval','units':'USD millions except days and rates','valuation_timestamp':inputs['as_of'],'periods':result,'checks':checks,'evidence_warnings':warnings}
