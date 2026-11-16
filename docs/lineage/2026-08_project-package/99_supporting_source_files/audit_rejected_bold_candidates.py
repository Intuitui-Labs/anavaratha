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

def is_candidate(w):
    font=w.get('fontname','') or ''
    token=w['text'].lstrip('*')
    return 'Bold' in font and 'Italic' not in font and re.match(r'^[A-Z][A-Za-z-]*$',token)

shown=0
with pdfplumber.open(PDF) as pdf:
    for pnum in range(10,149):
        page=pdf.pages[pnum-1]
        words=page.extract_words(keep_blank_chars=False,use_text_flow=False,extra_attrs=['fontname'])
        lines=group([w for w in words if 104<=w['top']<=page.height-43])
        for li,line in enumerate(lines):
            sci=[w for w in line if ci(w['x0'])==2]
            if not sci: continue
            candidates=[(wi,w) for wi,w in enumerate(sci) if is_candidate(w)]
            if not candidates: continue
            # Only candidates that are not followed by a same-line lowercase epithet.
            for wi,w in candidates:
                next_same=sci[wi+1]['text'].lstrip('*') if wi+1<len(sci) else ''
                anchor=any(w2 for w2 in line if ci(w2['x0']) in (5,6,7))
                next_sci=[w2 for w2 in lines[li+1] if ci(w2['x0'])==2] if li+1<len(lines) else []
                next_cont=bool(next_sci) and re.match(r'^[a-z][A-Za-z-]*$',next_sci[0]['text'].lstrip('*'))
                if not re.match(r'^[a-z][A-Za-z-]*$',next_same) and not (anchor or next_cont):
                    print(pnum,round(line[0]['top'],1),repr(w['text']),'cell=',repr(' '.join(x['text'] for x in sci)),'anchor=',anchor,'next=',repr(' '.join(x['text'] for x in next_sci)))
                    shown+=1
                    if shown>=160: raise SystemExit
