from pathlib import Path
import pdfplumber

pdf_path = Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
settings = {
    'vertical_strategy': 'explicit',
    'explicit_vertical_lines': [56, 143, 230, 329, 416, 581, 690, 741, 787],
    'horizontal_strategy': 'text',
    'text_x_tolerance': 2,
    'text_y_tolerance': 2,
    'intersection_tolerance': 5,
}
with pdfplumber.open(pdf_path) as pdf:
    table = pdf.pages[9].extract_table(settings)
for i, row in enumerate(table or []):
    print(i, repr(row))
