from pathlib import Path
import pdfplumber

pdf_path = Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[9]
    chars = [c for c in page.chars if 228 <= c['x0'] <= 330 and 115 <= c['top'] <= 530]
for c in chars:
    print(f"{c['top']:6.1f} x={c['x0']:6.1f} {c['text']!r} font={c.get('fontname')} size={c.get('size')}")
