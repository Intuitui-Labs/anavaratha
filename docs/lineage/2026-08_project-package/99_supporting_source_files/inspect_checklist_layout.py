import json
from pathlib import Path
import pdfplumber

pdf_path = Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
out_path = Path('/home/ubuntu/anavaratha/source_files/checklist_page10_words.json')

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[9]
    words = page.extract_words(keep_blank_chars=False, use_text_flow=False)
    payload = {
        'page_number': 10,
        'width': page.width,
        'height': page.height,
        'words': words,
    }
out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'wrote {out_path} with {len(words)} words')
