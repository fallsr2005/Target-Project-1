"""Assistant-operated follow-up, separate from the student's protected exercise."""
import json
from datetime import datetime
from pathlib import Path
from streamlit.testing.v1 import AppTest

root = Path(__file__).resolve().parent.parent
app = AppTest.from_file(str(root / 'app.py'), default_timeout=60).run()
app.slider(key='sales_growth').set_value(0.07).run()
changed = {'growth': app.slider(key='sales_growth').value,
           'valuation': [x.value for x in app.metric if x.label == 'Current conditional base']}
app.button[0].click().run()
reset = {'growth': app.slider(key='sales_growth').value,
         'valuation': [x.value for x in app.metric if x.label == 'Current conditional base'],
         'errors': [x.value for x in app.error],
         'exceptions': [x.message for x in app.exception]}
record = {'time_local': datetime.now().astimezone().isoformat(),
          'operator': 'Codex assistant',
          'scope': 'New follow-up replay; not evidence of reset immediately after the original student test.',
          'changed': changed, 'reset': reset}
(root / 'outputs' / 'followup-reset-check-after-fix.json').write_text(json.dumps(record, indent=2), encoding='utf-8')
print(json.dumps(record, indent=2))
assert changed['growth'] == 0.07 and reset['growth'] == 0.03
assert reset['valuation'] == ['$120.79'] and not reset['exceptions']
