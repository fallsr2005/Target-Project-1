"""AI-assisted tests: expectations recorded in docs/step-7-test-expectations.md."""
import copy
import json
import unittest
from pathlib import Path
from financial_engine import run_analysis
from valuation_engine import annual_wacc,enterprise_bridge,model_fcff,present_value,reverse_dcf,run_valuation

ROOT=Path(__file__).resolve().parents[1]
S=json.loads((ROOT/'data/model-inputs-step6.json').read_text(encoding='utf-8'))
V=json.loads((ROOT/'data/model-inputs-step7.json').read_text(encoding='utf-8'))

class ValuationChecks(unittest.TestCase):
    def setUp(self):
        self.statement=run_analysis(copy.deepcopy(S)); self.rows=model_fcff(self.statement,.24); self.cutoff=self.statement['periods'][0]
        self.w=annual_wacc(V)['wacc']; self.g=.02; self.roic=.12
    def test_fcff_reconciliation_and_exclusion(self):
        self.assertEqual(len(self.rows),6)
        self.assertNotIn('elapsed estimate',[r['period'] for r in self.rows])
        for r in self.rows: self.assertAlmostEqual(r['fcff'],r['cash_flow_statement_reconciliation'],places=7)
    def test_discount_timing(self):
        val=present_value(self.rows,self.w,self.g,self.roic,V['as_of'])
        self.assertEqual(val['discounted_periods'][0]['actual_days'],103)
        self.assertEqual(val['terminal']['measurement_date'],'2032-01-31')
        for r in val['discounted_periods']: self.assertAlmostEqual(r['present_value'],r['fcff']/(1+self.w)**(r['actual_days']/365))
    def test_wacc_monotonic_for_positive_cash_flows(self):
        self.assertTrue(all(x['fcff']>0 for x in self.rows))
        low=present_value(self.rows,self.w-.01,self.g,self.roic,V['as_of'])['enterprise_value']
        high=present_value(self.rows,self.w+.01,self.g,self.roic,V['as_of'])['enterprise_value']
        self.assertGreater(low,high)
    def test_growth_depends_on_return_on_capital(self):
        def tv(g,r): return present_value(self.rows,self.w,g,r,V['as_of'])['terminal']['terminal_value']
        self.assertGreater(tv(.03,.12),tv(.01,.12))
        self.assertLess(tv(.03,.06),tv(.01,.06))
    def test_bridge_signs_and_share_units(self):
        a=enterprise_bridge(10000,self.cutoff,1000,2.2)
        altered=copy.deepcopy(self.cutoff); altered['balance_sheet']['cash']+=1
        b=enterprise_bridge(10000,altered,1000,2.2)
        altered['balance_sheet']['debt_total']+=1
        c=enterprise_bridge(10000,altered,1000,2.2)
        self.assertAlmostEqual(b['equity_value_partial']-a['equity_value_partial'],1)
        self.assertAlmostEqual(c['equity_value_partial'],a['equity_value_partial'])
        self.assertAlmostEqual(a['value_per_share_partial'],a['equity_value_partial']/(454.296736+2.2))
    def test_invalid_inputs(self):
        for args in [(.02,.02,.12),(.08,-.01,.12),(.08,.03,.02)]:
            with self.assertRaises(ValueError): present_value(self.rows,*args,V['as_of'])
        bad=copy.deepcopy(V); bad['debt_weight']['value']=.3
        with self.assertRaises(ValueError): annual_wacc(bad)
        with self.assertRaises(ValueError): enterprise_bridge(1000,self.cutoff,1000,-500)
    def test_reverse_dcf_requires_price_and_recovers_synthetic(self):
        self.assertIsNone(reverse_dcf(self.rows,self.w,.12,V['as_of'],self.cutoff,1000,2.2,None)['solved_growth'])
        ev=present_value(self.rows,self.w,.025,.12,V['as_of'])['enterprise_value']
        synthetic=enterprise_bridge(ev,self.cutoff,1000,2.2)['value_per_share_partial']
        evidence={'value':synthetic,'accepted_by_student':True,'timestamp':V['as_of'],'source_url':'https://example.com/synthetic-test-only','definition':'unadjusted official regular-session closing auction'}
        solved=reverse_dcf(self.rows,self.w,.12,V['as_of'],self.cutoff,1000,2.2,evidence)
        self.assertAlmostEqual(solved['solved_growth'],.025,places=8)
    def test_scenarios_hold_bridge_common(self):
        r=run_valuation(copy.deepcopy(S),copy.deepcopy(V)); scenarios=r['scenarios']
        self.assertEqual(scenarios['low']['partial_equity_bridge']['cash_estimated_at_cutoff'],scenarios['high']['partial_equity_bridge']['cash_estimated_at_cutoff'])
        self.assertTrue(all(not x['statement_check_failures'] for x in scenarios.values()))
        self.assertEqual(r['market_price']['accepted_by_student'],V['market_price']['accepted_by_student'])
        if V['market_price']['accepted_by_student']: self.assertIsNotNone(r['reverse_dcf']['solved_growth'])
        else: self.assertIsNone(r['reverse_dcf']['solved_growth'])

if __name__=='__main__': unittest.main()
