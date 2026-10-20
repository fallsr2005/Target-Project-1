"""Conditional provider-price analysis never asserts student acceptance."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from audit_analysis import export_bundle
if __name__=='__main__':
    b=export_bundle()
    print(json.dumps({'price':b['market_price'],'conditional_reverse':b['conditional_reverse_dcf']},indent=2))
