"""Published course-case and provenance checks; not the student protected exercise."""
import unittest
from audit_analysis import training_case, load_inputs, peer_comparisons
from financial_engine import run_analysis
from valuation_engine import run_valuation, reverse_dcf, fcff_from_operating, equity_from_enterprise

class AuditChecks(unittest.TestCase):
    def test_twelve_published_course_answers(self):
        r=training_case();self.assertEqual(r['passed'],12,r['checks'])
    def test_week_two_published_bridge_case(self):
        self.assertEqual(fcff_from_operating(150,.25,40,60,15),77.5)
        self.assertEqual(equity_from_enterprise(1000,100,250,100,-30),(820,8.2))
    def test_conditional_price_is_never_student_acceptance(self):
        S,V=load_inputs();V['market_price']['accepted_by_student']=False;st=run_analysis(S);r=run_valuation(S,V)
        args=(r['scenarios']['base']['fcff'],r['wacc_components']['wacc'],.12,V['as_of'],st['periods'][0],1000,2.2,V['market_price'],V['other_claims_and_nonoperating_assets']['value'])
        self.assertIsNone(reverse_dcf(*args)['solved_growth'])
        result=reverse_dcf(*args,allow_conditional=True)
        self.assertFalse(result['student_price_acceptance']);self.assertIsNotNone(result['solved_growth'])
        self.assertFalse(V['market_price']['accepted_by_student'])
    def test_itemized_claims_match_bridge_and_sign(self):
        S,V=load_inputs();r=run_valuation(S,V)['scenarios']['base']['partial_equity_bridge']
        self.assertAlmostEqual(sum(i['signed_amount'] for i in V['bridge_claim_items']),r['other_claims_and_nonoperating_assets_adjustment'])
        self.assertAlmostEqual(r['enterprise_value']+r['estimated_eligible_excess_cash']-r['debt_estimated_at_cutoff']+r['other_claims_and_nonoperating_assets_adjustment'],r['equity_value'])
    def test_tax_over_100_percent_rejected(self):
        S,V=load_inputs();S['drivers']['tax_rate']['value']=1.01
        with self.assertRaises(ValueError):run_analysis(S)
    def test_seasonal_inventory_is_not_year_end_level(self):
        S,V=load_inputs();r=run_analysis(S)
        self.assertGreater(r['periods'][0]['balance_sheet']['inventory'],13249)
        self.assertGreater(r['periods'][0]['balance_sheet']['payables'],13306)
        self.assertEqual(r['periods'][0]['end'],'2026-10-19')
    def test_contextual_comparisons_have_cutoff_sources_and_consistent_ev(self):
        S,V=load_inputs()
        for r in peer_comparisons(S,V)['rows']:
            self.assertTrue(all(e['filed']<='2026-10-19' for e in r['evidence']+r['earnings']['evidence']))
            self.assertGreater(r['P_E'],0);self.assertGreater(r['EV_EBIT'],0)
            ev=r['equity_value_m']+r['debt_including_finance_leases_m']+r['nci_including_redeemable_m']+r['derivative_claims_m']-r['eligible_excess_cash_m']-r['other_investment_assets_m']
            self.assertAlmostEqual(ev,r['conventional_EV_proxy_m'])
            self.assertAlmostEqual(r['P_E'],r['price']['value']/(r['earnings']['net_income_common']/r['earnings']['diluted_shares']))

if __name__=='__main__':unittest.main()
