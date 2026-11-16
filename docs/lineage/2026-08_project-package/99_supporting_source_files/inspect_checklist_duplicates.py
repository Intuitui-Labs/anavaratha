import json
from collections import defaultdict
from pathlib import Path

records=[json.loads(x) for x in Path('/home/ubuntu/anavaratha/source_files/medicinal_checklist_records_raw.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
by=defaultdict(list)
for r in records: by[r['updated_scientific_name']].append(r)
for name, rows in sorted(by.items()):
    if len(rows)>1:
        print('NAME:',name)
        for r in rows:
            print(' ',r['source_pdf_page'],r['visual_start_top'],r['local_name_sinhala'],r['status_2012'],r['status_2020'])
