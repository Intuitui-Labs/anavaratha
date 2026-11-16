import csv
import json
import re
from pathlib import Path
from collections import defaultdict
import pdfplumber

PDF = Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
OUT_JSONL = Path('/home/ubuntu/anavaratha/source_files/medicinal_checklist_records_raw.jsonl')
OUT_CSV = Path('/home/ubuntu/anavaratha/source_files/medicinal_checklist_records_raw.csv')

# The source table is laid out on a fixed-width page. These boundaries were
# checked visually against PDF pages 10-15. The output retains raw visual lines
# so that any uncertain grouping can be audited against the original PDF.
BOUNDS = [56, 145, 231, 330, 416, 581, 690, 741, 790]
COLS = ['updated_family', 'family_in_flora', 'updated_scientific_name',
        'scientific_name_in_flora', 'homotypic_synonyms', 'local_name_sinhala',
        'status_2012', 'status_2020']
START_Y_MIN = 104
BOTTOM_MARGIN = 43


def clean(text):
    text = re.sub(r'\s+', ' ', text or '').strip()
    return text


def col_index(x0):
    for i in range(len(BOUNDS) - 1):
        if BOUNDS[i] <= x0 < BOUNDS[i + 1]:
            return i
    return None


def group_lines(words):
    lines = []
    for word in sorted(words, key=lambda w: (w['top'], w['x0'])):
        placed = False
        for line in lines:
            if abs(line['top'] - word['top']) <= 1.7:
                line['words'].append(word)
                placed = True
                break
        if not placed:
            lines.append({'top': word['top'], 'words': [word]})
    return sorted(lines, key=lambda x: x['top'])


STATUS_TOKENS = {'LC', 'VU', 'NT', 'EN', 'DD', 'CR', 'EX', 'EW', 'NE', 'NA', '(PE)', 'CR(PE)'}


def line_cells(line):
    cells = [[] for _ in range(8)]
    for w in sorted(line['words'], key=lambda x: x['x0']):
        x0 = w['x0']
        token = w['text'].strip()
        # The local-name column is allowed to run past its nominal right edge
        # when a Sinhala/English name is long. Status values are short, stable
        # tokens positioned near the two status anchors, so classify them by
        # token and anchor rather than by a hard x cutoff alone.
        if x0 >= 581 and token in STATUS_TOKENS:
            idx = 6 if x0 < 730 else 7
        else:
            idx = col_index(x0)
            if x0 >= 690 and token not in STATUS_TOKENS:
                idx = 5
        if idx is not None:
            cells[idx].append(w)
    texts = [clean(' '.join(w['text'] for w in cell)) for cell in cells]
    return texts, cells


def is_header_or_front_matter(texts):
    joined = ' '.join(texts).lower()
    if 'updated family' in joined or 'family name in' in joined:
        return True
    if 'appendix 1:' in joined or 'the updated list of medicinal plants' in joined:
        return True
    if texts[2].strip().lower() in {'name', 'updated scientific'}:
        return True
    if texts[0].strip().lower() == 'updated family':
        return True
    return False


def is_scientific_genus_word(word):
    font = word.get('fontname', '') or ''
    token = word['text'].lstrip('*')
    # Ordinary taxa are italic; endemic taxa are often bold rather than
    # bold-italic in the embedded PDF font metadata.
    return ('Italic' in font or 'Bold' in font) and re.match(r'^[A-Z][A-Za-z-]*$', token)


def is_record_start(texts, cells, next_texts=None, next_cells=None):
    sci = texts[2]
    if not sci:
        return False
    words = cells[2]
    if not words:
        return False
    next_words = (next_cells or [[] for _ in range(8)])[2]
    next_text = (next_texts or ['' for _ in range(8)])[2]
    # In a small number of PDF lines, a plain author-citation fragment from one
    # record shares a baseline with the italic genus of the next record. Detect
    # the first italic uppercase genus anywhere in the cell, not only at x=232.
    for wi, word in enumerate(words):
        if is_scientific_genus_word(word):
            font = word.get('fontname', '') or ''
            token = word['text'].lstrip('*')
            # Bold-only taxonomic starts are accepted when the following token
            # is a lowercase epithet; this excludes isolated bold author names
            # such as Wight, Thwaites, or Alston.
            if 'Bold' in font and 'Italic' not in font:
                next_token = words[wi + 1]['text'].lstrip('*') if wi + 1 < len(words) else ''
                has_row_anchor = any(texts[i] for i in (5, 6, 7))
                next_line_continuation = bool(next_words) and bool(re.match(r'^[a-z][A-Za-z-]*$', next_words[0]['text'].lstrip('*'))) and any(('Italic' in (w.get('fontname', '') or '') or 'Bold' in (w.get('fontname', '') or '')) for w in next_words)
                # A bold genus may be the only scientific-name token on its
                # baseline because the epithet wraps to the next line. Accept
                # that case when the same line carries local/status data or
                # the next visual line is a lower-case taxonomic continuation;
                # reject isolated bold author surnames.
                if next_token in {'ex', '&', 'and'}:
                    continue
                if not re.match(r'^[a-z][A-Za-z-]*$', next_token) and not has_row_anchor and not next_line_continuation:
                    continue
            return True
    # A small embedded-text OCR anomaly lowercases the I in lndigofera.
    # Keep this fallback explicit and narrow; broad anchor-based fallbacks
    # misclassify bold author citations as taxa.
    has_row_anchor = any(texts[i] for i in (5, 6, 7))
    return has_row_anchor and any(w['text'].lower().startswith('lndigo') for w in words)


def page_records(page_number, page):
    words = page.extract_words(keep_blank_chars=False, use_text_flow=False,
                               extra_attrs=['fontname'])
    lines = group_lines([w for w in words if START_Y_MIN <= w['top'] <= page.height - BOTTOM_MARGIN])
    visual = []
    for line in lines:
        texts, cells = line_cells(line)
        if not any(texts):
            continue
        if is_header_or_front_matter(texts):
            continue
        # Exclude running footer/header remnants and page number lines.
        joined = ' '.join(texts)
        if 'Ceylon Journal of Science' in joined or joined.startswith('Rajakaruna'):
            continue
        visual.append({'top': round(line['top'], 2), 'texts': texts, 'cells': cells})

    starts = []
    for i, line in enumerate(visual):
        next_line = visual[i + 1] if i + 1 < len(visual) else None
        if is_record_start(line['texts'], line['cells'], next_line['texts'] if next_line else None, next_line['cells'] if next_line else None):
            starts.append(i)
    records = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(visual)
        chunk = visual[start:end]
        values = ['' for _ in range(8)]
        raw_lines = []
        for line_index, line in enumerate(chunk):
            raw_lines.append({'top': line['top'], 'cells': line['texts']})
            for j, text in enumerate(line['texts']):
                if text:
                    # If a line begins with a plain citation fragment and then
                    # contains the next italic genus, retain only the portion
                    # from that genus for the new record's scientific-name cell.
                    if line_index == 0 and j == 2:
                        sci_words = line['cells'][2]
                        for wi, word in enumerate(sci_words):
                            token = word['text'].lstrip('*')
                            if is_scientific_genus_word(word):
                                text = clean(' '.join(w['text'] for w in sci_words[wi:]))
                                break
                    values[j] = clean((values[j] + ' ' + text).strip())
        # Keep only records with a plausible updated scientific name.
        if values[2]:
            records.append({
                'source_pdf_page': page_number,
                'source_printed_page': page_number + 63,
                'source_table': 'Appendix 1',
                'visual_start_top': chunk[0]['top'],
                **dict(zip(COLS, values)),
                'raw_visual_lines': raw_lines,
                'review_status': 'machine_extracted_visual_validation_required',
            })
    return records


all_records = []
with pdfplumber.open(PDF) as pdf:
    for page_number in range(10, 149):
        all_records.extend(page_records(page_number, pdf.pages[page_number - 1]))

with OUT_JSONL.open('w', encoding='utf-8') as f:
    for record in all_records:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
    fields = ['record_id', 'source_pdf_page', 'source_printed_page', 'source_table',
              'updated_family', 'family_in_flora', 'updated_scientific_name',
              'scientific_name_in_flora', 'homotypic_synonyms', 'local_name_sinhala',
              'status_2012', 'status_2020', 'review_status']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for n, record in enumerate(all_records, 1):
        row = {k: record.get(k, '') for k in fields}
        row['record_id'] = f'MCL25-A1-{n:04d}'
        writer.writerow(row)

print(f'extracted_records={len(all_records)}')
print(f'jsonl={OUT_JSONL}')
print(f'csv={OUT_CSV}')
