"""Target research workbench; financial calculations live in shared analysis modules."""
import json
from copy import deepcopy
from pathlib import Path
import streamlit as st
from analysis import build_bundle
from audit_analysis import load_inputs, historical_reference_bands

ROOT=Path(__file__).resolve().parent
S,V=load_inputs()
st.set_page_config(page_title='Target Finance Workbench',layout='wide')
st.title('Target Finance Workbench')
st.warning('Recommendation: watch/defer. The source-check response, conditional assumptions and monitoring policy are confirmed. The protected exercise and other listed submission requirements remain open. Cutoff balances and several bridge/forecast inputs are estimates.')
st.caption('Valuation: October 19, 2026, 4 p.m. Eastern | USD millions; shares millions; per-share USD | User: buy-side committee, no current position | Decision horizon: 12-24 months')
keys=('sales_growth','cost_ex_da_rate','sga_rate','capex_rate','revolver_capacity','minimum_cash')
if st.button('Reset all controls to base'):
    for key in keys:st.session_state.pop(key,None)
    st.rerun()
work=deepcopy(S)
st.subheader('Operating assumptions')
st.caption('Forecast controls are stress exploration ranges, not statistically validated bounds. Baseline paths and their challenges are in the assumption record. Changes affect FY2027 only; dependent lines respond through the same engine.')
cols=st.columns(4)
controls=[('sales_growth','FY2027 sales growth',-.05,.10,.005),('cost_ex_da_rate','FY2027 cost excluding D&A / sales',.65,.80,.0025),('sga_rate','FY2027 SG&A / sales',.17,.24,.0025),('capex_rate','FY2027 capex / sales',.025,.12,.0025)]
for col,(key,label,low,high,step) in zip(cols,controls):
    with col:work['drivers'][key]['value'][1]=st.slider(label,low,high,float(S['drivers'][key]['value'][1]),step,key=key)
with st.expander('Liquidity stress controls'):
    work['drivers']['revolver_capacity']['value']=st.slider('Available revolver capacity, USD millions',0,4000,int(S['drivers']['revolver_capacity']['value']),100,key='revolver_capacity')
    work['drivers']['minimum_cash']['value']=st.slider('Required cash reserve, USD millions',0,5000,int(S['drivers']['minimum_cash']['value']),100,key='minimum_cash')
    st.caption('Demonstration: capex 12%, available revolver zero, required reserve 5000. Inspect genuine engine failures, then Reset. This demonstration is separate from the student AI-closed exercise.')
bands=historical_reference_bands()
for key,label,_,_,_ in controls:
    x=work['drivers'][key]['value'][1]
    if key=='cost_ex_da_rate':x+=work['drivers']['da_rate']['value'][1]*work['drivers']['da_in_cost_fraction']['value']
    band=bands[key]
    if not band['low']<=x<=band['high']:
        st.error(f"Historical reference flag: {label} is outside {100*band['low']:.2f}% to {100*band['high']:.2f}%. This is an assumption-review alert, not an accounting failure. Cost comparison includes allocated depreciation; observations and normalizations differ.")
st.caption('The base capex assumption of 4.50% is slightly above the FY2023-FY2025 reported maximum of 4.47%. The historical flag stays visible after Reset; passing arithmetic does not remove it.')
changed=work!=S
if changed:st.info('Exploratory controls differ from the frozen base. The saved visible_output.json is not overwritten.')
try:result=build_bundle(work,V,include_sensitivities=False)
except (ValueError,KeyError,ZeroDivisionError) as e:
    st.error('Current model state cannot be valued: '+str(e));st.stop()
failures=[c for c in result['checks'] if c['status']=='fail']
if failures:st.error(f'{len(failures)} actual model checks failed. Valuation is blocked until the state is corrected.')
else:st.success('Current accounting checks pass. This verifies arithmetic, not source assumptions or student approval.')
tabs=st.tabs(['Statements','Valuation & bridge','Comparisons & sensitivities','Sources & validation','Frozen base'])
with tabs[0]:
    st.caption('Elapsed estimate is displayed separately from the future FY2026 stub and five full forecast years. All financial lines are shown below.')
    periods=result['statements']['periods']
    for name,label in [('income_statement','Income statement'),('balance_sheet','Balance sheet'),('cash_flow_statement','Cash flow statement')]:
        st.subheader(label)
        fields=list(dict.fromkeys(k for p in periods for k in p[name]))
        st.dataframe([{'Line item':k,**{p['period']:p[name].get(k) for p in periods}} for k in fields],hide_index=True,width='stretch')
with tabs[1]:
    if failures:st.write('Valuation blocked by actual checks. Reset to recover.')
    else:
        st.dataframe([{'Case':k,'Conditional value/share':v,'Status':'estimate; student review pending'} for k,v in result['low_base_high'].items()],hide_index=True,width='stretch')
        st.metric('Current conditional base',f"${result['low_base_high']['base']:.2f}")
        st.write('WACC, estimated inputs:',result['wacc'])
        st.write('Terminal contribution:',result['terminal'])
        st.write('Accepted monitoring policy:', result['monitoring_policy'])
        st.write('Accepted conditional entry screen:', result['entry_policy'])
        st.subheader('FCFF trace')
        st.dataframe(result['fcff'],hide_index=True,width='stretch')
        st.subheader('Enterprise-to-equity bridge')
        st.dataframe(result['equity_bridge']['bridge_items'],hide_index=True,width='stretch')
        st.dataframe(result['equity_bridge'].get('other_claim_details',[]),hide_index=True,width='stretch')
        st.write(result['equity_bridge'].get('classification_notes',[]))
        st.subheader('WACC / terminal-growth grid')
        st.dataframe(result['wacc_growth_sensitivity'],hide_index=True,width='stretch')
        st.subheader('Conditional provider-price comparison')
        st.write(result['market_price'])
        st.write('Conditional gap versus provider Close:',result['conditional_gap_vs_price'])
        st.write(result['conditional_reverse_dcf'])
        st.caption('Reverse DCF solves terminal growth with forecast, WACC, incremental return, bridge and shares fixed. It is one conditional solved expectation under the accepted provider convention.')
with tabs[2]:
    st.subheader('Contextual trading comparisons')
    peers=result['peer_comparisons']
    st.dataframe([{'Company':r['ticker'],'Class':r['classification'],'Close':r['price']['value'],'Earnings end':r['earnings']['end'],'Balance date':r['balance_date'],'EV/EBIT proxy':r['EV_EBIT'],'P/E':r['P_E']} for r in peers['rows']],hide_index=True,width='stretch')
    st.caption(peers['qualification'])
    for r in peers['rows']:
        with st.expander(r['ticker']+' definitions and limitations'):st.json(r)
    source=json.loads((ROOT/'visible_output.json').read_text(encoding='utf-8'))
    sensitivities=source.get('operating_sensitivities')
    if sensitivities:
        st.subheader('Frozen-base one-at-a-time operating sensitivities')
        st.caption('This table uses the saved base, independent of current exploratory controls. Each shock starts from that same base.')
        st.dataframe(sensitivities['rows'],hide_index=True,width='stretch')
        st.write('Range-dependent rankings:',sensitivities['rankings']);st.caption(sensitivities['range_basis'])
with tabs[3]:
    st.markdown('[Target FY2025 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm) | [Target Q2 FY2026 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm)')
    st.caption('Source cells and cutoff filing dates are retained in historical ledgers and cached audit data. The student source-check response and output disposition are recorded separately in data/student-decisions.json; source research and drafted wording were assisted.')
    st.dataframe(result['checks'],hide_index=True,width='stretch')
    st.subheader('Published course known-answer reconciliation')
    st.dataframe(result['known_answer']['checks'],hide_index=True,width='stretch')
    st.write('Pending student evidence:',result['pending_human_requirements'])
with tabs[4]:
    frozen=json.loads((ROOT/'visible_output.json').read_text(encoding='utf-8'))
    st.caption('Read-only saved export. Exploratory changes do not overwrite it.')
    st.write({'as_of':frozen['as_of'],'run_time':frozen['run_time'],'low_base_high':frozen['low_base_high'],'status':frozen['status']})
    st.download_button('Download frozen visible output',(ROOT/'visible_output.json').read_bytes(),file_name='visible_output.json',mime='application/json')
