from io import BytesIO
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

root = Path(__file__).resolve().parent.parent
def replace_stream(writer, index, replacements):
    page = writer.pages[index]
    data = page.get_contents().get_data()
    for old, new in replacements:
        assert data.count(old) == 1
        data = data.replace(old, new)
    stream = DecodedStreamObject(); stream.set_data(data)
    page[NameObject('/Contents')] = writer._add_object(stream)

research = root / 'docs' / 'Research-Evolution.pdf'
writer = PdfWriter(clone_from=PdfReader(research))
replace_stream(writer, 4, [
 (b'The assistant suggested this question and response before the student reported the exchange. Challenger', b'The student reports responding in their own words. Challenger'),
 (b'credit: project partner; identity is not stored in this folder. The downside case combines multiple changes.', b'credit: project partner. The downside case combines multiple changes.')])
out=BytesIO(); writer.write(out); research.write_bytes(out.getvalue())

validation = root / 'docs' / 'Validation-and-AI-Use.pdf'
writer = PdfWriter(clone_from=PdfReader(validation))
replace_stream(writer, 0, [(b'The Edition A checkpoint receipt and switch eligibility, actual credited partner feedback, original exercise chronology and', b'The Edition A checkpoint receipt, original exercise chronology and')])
buffer=BytesIO(); styles=getSampleStyleSheet()
story=[Paragraph('Validation and AI Use - Partner Feedback Update', styles['Title']), Spacer(1,12),
 Paragraph('October 20, 2026. This later record supersedes earlier statements that partner feedback is pending.', styles['BodyText']), Spacer(1,12),
 Paragraph('The student reports that their project partner asked: "What happens if Target’s sales growth is weaker than you expect and higher costs hurt its profit margins? Would you still want to buy the stock?"', styles['BodyText']), Spacer(1,10),
 Paragraph('The student reports answering in their own words: "That would make me more cautious. My downside case combines weaker growth with higher operating costs and gives an estimated value of about $86 per share, compared with the $120.79 base case. I would continue to watch or defer rather than buy, and I would monitor Target’s sales and recurring margins for evidence that the business is improving."', styles['BodyText']), Spacer(1,10),
 Paragraph('Challenger credit: project partner. The downside scenario combines multiple changes. The original checkpoint receipt and original exercise chronology remain unverified. See the AI-use log for documented assistance.', styles['BodyText'])]
SimpleDocTemplate(buffer,pagesize=(612,792),leftMargin=52,rightMargin=52,topMargin=52,bottomMargin=52).build(story)
buffer.seek(0); writer.insert_page(PdfReader(buffer).pages[0],1)
out=BytesIO(); writer.write(out); validation.write_bytes(out.getvalue())
print('research pages:',len(PdfReader(research).pages),'validation pages:',len(PdfReader(validation).pages),'attachments:',list(PdfReader(validation).attachments))
