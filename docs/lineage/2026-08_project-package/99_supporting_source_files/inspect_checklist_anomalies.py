import json
from pathlib import Path

path=Path('/home/ubuntu/anavaratha/source_files/medicinal_checklist_records_raw.jsonl')
allowed={'LC','VU','NT','EN','DD','CR','CR (PE)','CR(PE)','EW','EX','NE','NA','Data Deficient','Critically Endangered','Endangered','Vulnerable','Near Threatened','Least Concern'}
shown=0
for line in path.read_text(encoding='utf-8').splitlines():
    r=json.loads(line)
    if (r['status_2012'] and r['status_2012'] not in allowed) or (r['status_2020'] and r['status_2020'] not in allowed):
        print(json.dumps({k:r[k] for k in ['source_pdf_page','updated_scientific_name','local_name_sinhala','status_2012','status_2020','raw_visual_lines']}, ensure_ascii=False, indent=2))
        shown+=1
        if shown>=20: break
print('shown',shown)
