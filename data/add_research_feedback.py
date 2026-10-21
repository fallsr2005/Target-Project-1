from io import BytesIO
from pathlib import Path
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from pypdf import PdfReader, PdfWriter

root = Path(__file__).resolve().parent.parent
path = root / 'docs/Research-Evolution.pdf'
buffer = BytesIO()
styles = getSampleStyleSheet()
story = [Paragraph('Research Evolution - Later Evidence', styles['Title']), Spacer(1, 12),
 Paragraph('October 20, 2026. This dated update supersedes the earlier pending-status statements concerning the partner feedback and post-test decision. The original Edition A pages remain unchanged.', styles['BodyText']), Spacer(1, 12),
 Paragraph('Partner challenge', styles['Heading2']),
 Paragraph('The student reports that their project partner asked: "What happens if Target’s sales growth is weaker than you expect and higher costs hurt its profit margins? Would you still want to buy the stock?"', styles['BodyText']), Spacer(1, 8),
 Paragraph('The student reports responding: "That would make me more cautious. My downside case combines weaker growth with higher operating costs and gives an estimated value of about $86 per share, compared with the $120.79 base case. I would continue to watch or defer rather than buy, and I would monitor Target’s sales and recurring margins for evidence that the business is improving."', styles['BodyText']), Spacer(1, 8),
 Paragraph('The assistant suggested this question and response before the student reported the exchange. Challenger credit: project partner; identity is not stored in this folder. The downside case combines multiple changes.', styles['BodyText']), Spacer(1, 12),
 Paragraph('Changed-input follow-up', styles['Heading2']),
 Paragraph('The student clarified after the original test that the intended operating profit and FCFF predictions were $100 million each. The original prediction remains unchanged. The student accepted watch/defer after the results. A later reset check after an app correction showed 0.03 growth and $120.79; it does not establish the state immediately after the original test. See the validation record for details.', styles['BodyText'])]
SimpleDocTemplate(buffer, pagesize=(612,792), leftMargin=52, rightMargin=52, topMargin=52, bottomMargin=52).build(story)
buffer.seek(0)
writer = PdfWriter(clone_from=PdfReader(path))
writer.add_page(PdfReader(buffer).pages[0])
out = BytesIO(); writer.write(out); path.write_bytes(out.getvalue())
print('pages:', len(PdfReader(path).pages))
