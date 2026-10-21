"""Prepend a dated correction to the existing validation PDF, preserving attachments."""
from io import BytesIO
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from pypdf import PdfReader, PdfWriter

root = Path(__file__).resolve().parent.parent
path = root / 'docs' / 'Validation-and-AI-Use.pdf'
buffer = BytesIO()
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleSmall', parent=styles['Title'], fontSize=15, leading=19, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name='BodySmall', parent=styles['BodyText'], fontSize=9.3, leading=13, spaceAfter=8))
styles.add(ParagraphStyle(name='SubSmall', parent=styles['Heading2'], fontSize=11, leading=14, spaceBefore=4, spaceAfter=5, textColor=colors.HexColor('#25405e')))
doc = SimpleDocTemplate(buffer, pagesize=(612, 792), leftMargin=52, rightMargin=52, topMargin=40, bottomMargin=40)
P = lambda t: Paragraph(t, styles['BodySmall'])
H = lambda t: Paragraph(t, styles['SubSmall'])
story = [Paragraph('Validation and AI Use - Dated Addendum', styles['TitleSmall']),
 P('<b>October 20, 2026.</b> This addendum updates the earlier pages where their status statements differ. The original protected prediction and evidence are preserved; it does not certify AI-off authorship, checkpoint receipt, or full assignment completion.'),
 H('Prediction and observed results'),
 P('The original recorded prediction was that FY2031 operating profit and FCFF would each increase by $1,000 million, and estimated value by $5 per share. After the test, the student clarified that the intended financial predictions were $100 million each. This later clarification is not evidence that $100 million was recorded before the run.'),
 P('Observed increases were $275.5849 million in operating profit, $176.9527 million in FCFF, and $5.7842 per share. Relative to the clarified $100 million figures, the first two exceeded the prediction by $175.5849 million and $76.9527 million, respectively.'),
 H('Actual decision after the test'),
 P('The student accepted an assistant-proposed watch/defer decision and reasoning: increasing assumed FY2027 growth from 3% to 7% raised the model value from $120.79 to $126.58 per share, still below the $153.29 reference market price. The higher growth is an assumption; stronger sales and margins or a lower price would be sought before considering a purchase. This actual decision differs from the original predicted buy action.'),
 H('Reset evidence and correction'),
 P('The student was uncertain whether Reset was used immediately after the original test. A subsequent browser check initially displayed 0.07 while showing $120.79. The assistant changed the reset code; the student then reported setting 0.07 and pressing Reset. The new screenshot shows 0.03, $120.79 and passing accounting checks; the capex historical-reference alert remains. This later check does not establish the original test\'s immediate reset.'),
 P('Evidence: outputs/changed-input-evidence/followup-student-reset/ and data/protected-changed-input-record.json. The original screenshot evidence remains attached to the earlier PDF. The newer screenshot is in the repository folder, not in that original attachment.'),
 H('Still outstanding'),
 P('The Edition A checkpoint receipt and switch eligibility, actual credited partner feedback, original exercise chronology and immediate reset, Video 3 and its transcript, video links/access, final repository freeze and Brightspace receipt remain unverified or incomplete. AI assisted the wording, documentation and reset-code correction; see docs/ai-use-log.md.')]
doc.build(story)
buffer.seek(0)
reader = PdfReader(path)
writer = PdfWriter(clone_from=reader)
writer.insert_page(PdfReader(buffer).pages[0], 0)
output = BytesIO()
writer.write(output)
path.write_bytes(output.getvalue())
print('pages:', len(PdfReader(path).pages), 'attachment names:', list(PdfReader(path).attachments))
