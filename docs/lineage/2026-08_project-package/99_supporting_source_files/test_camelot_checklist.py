from pathlib import Path
import camelot

pdf = Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
for flavor in ['stream']:
    tables = camelot.read_pdf(str(pdf), pages='10', flavor=flavor, strip_text='\n')
    print('flavor', flavor, 'tables', tables.n)
    for i, table in enumerate(tables):
        print('table', i, 'shape', table.df.shape, 'accuracy', table.parsing_report)
        print(table.df.to_string(index=False, header=False, max_rows=80))
