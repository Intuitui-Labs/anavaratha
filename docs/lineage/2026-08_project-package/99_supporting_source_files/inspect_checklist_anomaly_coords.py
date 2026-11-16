from pathlib import Path
import pdfplumber

PDF=Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
for pnum, y0, y1 in [(17,315,335),(26,295,360),(28,420,458),(37,145,220),(71,325,380)]:
    print(f'--- page {pnum} y {y0}-{y1} ---')
    with pdfplumber.open(PDF) as pdf:
        page=pdf.pages[pnum-1]
        for w in page.extract_words(keep_blank_chars=False,use_text_flow=False,extra_attrs=['fontname']):
            if y0 <= w['top'] <= y1:
                print(f"top={w['top']:.2f} x0={w['x0']:.2f} x1={w['x1']:.2f} text={w['text']!r} font={w.get('fontname')}")
