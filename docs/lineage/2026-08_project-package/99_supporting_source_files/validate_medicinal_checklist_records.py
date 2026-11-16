import json
from collections import Counter
from pathlib import Path

path = Path('/home/ubuntu/anavaratha/source_files/medicinal_checklist_records_raw.jsonl')
records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

names = [r['updated_scientific_name'] for r in records]
families = [r['updated_family'] for r in records if r['updated_family']]
pages = [r['source_pdf_page'] for r in records]

print('record_count', len(records))
print('unique_updated_scientific_name_strings', len(set(names)))
print('duplicate_name_strings', sum(v-1 for v in Counter(names).values() if v > 1))
print('pages_with_records', len(set(pages)))
print('first_page', min(pages), 'last_page', max(pages))
print('family_labels_present', len(families))
print('blank_family_cells', sum(not r['updated_family'] for r in records))
for field in ['family_in_flora','scientific_name_in_flora','homotypic_synonyms','local_name_sinhala','status_2012','status_2020']:
    print('blank_' + field, sum(not r[field] for r in records))
print('status_2012_values', Counter(r['status_2012'] for r in records if r['status_2012']))
print('status_2020_values', Counter(r['status_2020'] for r in records if r['status_2020']))
print('sample_last_record', records[-1]['source_pdf_page'], records[-1]['updated_scientific_name'])
