"""Executed frozen base export, using the same analysis as the app."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from audit_analysis import export_bundle
if __name__=='__main__':
    b=export_bundle()
    print('Wrote visible_output.json; checks',b['check_summary'],'known answers',b['known_answer']['passed'])
    print('Conditional cases',b['low_base_high'])
