from pathlib import Path
from collections import defaultdict
import pdfplumber

pdf_path = Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[9]
    words = [w for w in page.extract_words(keep_blank_chars=False, use_text_flow=False) if w['top'] > 105 and w['bottom'] < 560]

lines = []
for word in sorted(words, key=lambda w: (w['top'], w['x0'])):
    placed = False
    for line in lines:
        if abs(line[0]['top'] - word['top']) <= 1.6:
            line.append(word)
            placed = True
            break
    if not placed:
        lines.append([word])

for line in sorted(lines, key=lambda line: min(w['top'] for w in line)):
    row = ' | '.join(f"{w['x0']:.1f}:{w['text']}" for w in sorted(line, key=lambda w: w['x0']))
    print(f"{min(w['top'] for w in line):6.1f} {row}")
