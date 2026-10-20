"""Reproducible operating sensitivity export; no protected student exercise."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from audit_analysis import load_inputs,operating_sensitivities
if __name__=='__main__':
    r=operating_sensitivities(*load_inputs())
    (ROOT/'data/step9-sensitivities.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(r['rankings'])
