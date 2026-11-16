from pathlib import Path
import pdfplumber
import re

PDF=Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
BOUNDS=[56,145,231,330,416,581,690,741,790]
def ci(x):
    for i in range(8):
        if BOUNDS[i] <= x < BOUNDS[i+1]: return i

def group(words):
    lines=[]
    for w in sorted(words,key=lambda z:(z['top'],z['x0'])):
        for line in lines:
            if abs(line[0]['top']-w['top'])<=1.7: line.append(w); break
        else: lines.append([w])
    return lines

with pdfplumber.open(PDF) as pdf:
    for pnum in range(10,149):
        page=pdf.pages[pnum-1]
        words=page.extract_words(keep_blank_chars=False,use_text_flow=False,extra_attrs=['fontname'])
        for line in group([w for w in words if 104<=w['top']<=page.height-43]):
            cells=[[] for _ in range(8)]
            for w in line:
                i=ci(w['x0'])
                if i is not None: cells[i].append(w)
            sci=cells[2]
            if not sci: continue
            fonts=' '.join(w.get('fontname','') or '' for w in sci)
            text=' '.join(w['text'] for w in sci)
            anchor=any(cells[i] for i in (5,6,7))
            tokens=[w['text'].strip('*') for w in sci]
            binomial=bool(len(tokens)>=2 and re.match(r'^[A-Z][A-Za-z-]*$',tokens[0]) and re.match(r'^[a-z][A-Za-z-]*$',tokens[1]))
            if anchor and binomial and 'Italic' not in fonts and 'Bold' not in fonts:
                print(pnum, round(line[0]['top'],2), repr(text), '| local/status=', ' '.join(w['text'] for i in (5,6,7) for w in cells[i]))
