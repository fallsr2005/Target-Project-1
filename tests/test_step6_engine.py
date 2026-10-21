"""Accounting and feasibility checks; these are not the AI-closed exercise."""
import copy
import json
import unittest
from pathlib import Path
from financial_engine import run_analysis

ROOT=Path(__file__).resolve().parents[1]
CONFIG=json.loads((ROOT/'data/model-inputs-step6.json').read_text(encoding='utf-8'))

class EngineChecks(unittest.TestCase):
    def setUp(self): self.base=run_analysis(copy.deepcopy(CONFIG))
    def test_base_accounting(self):
        self.assertTrue(all(c['status']=='pass' for c in self.base['checks']), [c for c in self.base['checks'] if c['status']!='pass'])
    def test_extra_week_does_not_persist(self):
        p=self.base['periods']; a=p[2]; b=p[3]; c=p[4]
        self.assertAlmostEqual(b['income_statement']['sales'],a['income_statement']['sales']*1.03*53/52)
        self.assertAlmostEqual(c['income_statement']['sales'],b['income_statement']['sales']*52/53*1.025)
    def test_cost_change_reaches_margin_and_cash(self):
        x=copy.deepcopy(CONFIG); x['drivers']['cost_ex_da_rate']['value'][1]+=.01
        other=run_analysis(x)
        before=self.base['periods'][2]; after=other['periods'][2]
        self.assertLess(after['income_statement']['operating_income'],before['income_statement']['operating_income'])
        self.assertLess(after['cash_flow_statement']['operating_cash_flow'],before['cash_flow_statement']['operating_cash_flow'])
    def test_liquidity_failure_and_recovery(self):
        x=copy.deepcopy(CONFIG); x['drivers']['capex_rate']['value']=[.40]*6; x['drivers']['revolver_capacity']['value']=0
        failed=run_analysis(x)
        self.assertTrue(any(c['status']=='fail' and 'funding capacity' in c['name'] for c in failed['checks']))
        self.assertTrue(all(c['status']=='pass' for c in run_analysis(copy.deepcopy(CONFIG))['checks']))
    def test_invalid_allocation_rejected(self):
        x=copy.deepcopy(CONFIG); x['drivers']['da_in_cost_fraction']['value']=1.1
        with self.assertRaises(ValueError): run_analysis(x)

if __name__=='__main__': unittest.main()
