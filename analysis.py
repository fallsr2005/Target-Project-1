"""Analysis entry point shared by the app, exports and manual override runner."""
from financial_engine import run_analysis
from audit_analysis import build_bundle, export_bundle
if __name__=='__main__':
    import argparse,json
    from pathlib import Path
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputs')
    parser.add_argument('--valuation-inputs')
    parser.add_argument('--output')
    args=parser.parse_args();root=Path(__file__).resolve().parent
    if args.inputs or args.valuation_inputs:
        if not args.output:parser.error('Overrides require a separate --output; preserve the frozen base')
        S=json.loads(Path(args.inputs or root/'data/model-inputs-step6.json').read_text(encoding='utf-8-sig'))
        V=json.loads(Path(args.valuation_inputs or root/'data/model-inputs-step7.json').read_text(encoding='utf-8-sig'))
        if Path(args.output).resolve()==(root/'visible_output.json').resolve():parser.error('Override output must not replace frozen visible_output.json')
        result=build_bundle(S,V)
        Path(args.output).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    else:result=export_bundle()
    print('Model checks:',result['check_summary'],'| published answers:',result['known_answer']['passed'],'/',result['known_answer']['total'])
