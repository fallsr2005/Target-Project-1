"""Make one targeted Edition B wording correction; preserve Edition A pages."""
from io import BytesIO
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject

root = Path(__file__).resolve().parent.parent
path = root / 'docs' / 'Research-Evolution.pdf'
original = path.read_bytes()
reader = PdfReader(BytesIO(original))
before = [p.get_contents().get_data() for p in reader.pages[:2]]
writer = PdfWriter(clone_from=reader)
page = writer.pages[2]
data = page.get_contents().get_data()
old = b'Checkpoint receipt and eligibility for the company switch remain unverified. The student has confirmed watch/defer as the'
new = b'The original checkpoint receipt remains unverified. The student has confirmed watch/defer as the'
assert data.count(old) == 1
stream = DecodedStreamObject()
stream.set_data(data.replace(old, new))
page[NameObject('/Contents')] = writer._add_object(stream)
result = BytesIO()
writer.write(result)
check = PdfReader(BytesIO(result.getvalue()))
assert [p.get_contents().get_data() for p in check.pages[:2]] == before
assert 'eligibility for the company switch' not in ''.join(p.extract_text() or '' for p in check.pages)
(root / 'outputs' / 'Research-Evolution-before-wording-correction.pdf').write_bytes(original)
path.write_bytes(result.getvalue())
print('Edition A page contents unchanged; updated PDF pages:', len(check.pages))
