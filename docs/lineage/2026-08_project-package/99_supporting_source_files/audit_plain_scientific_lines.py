from pathlib import Path
import pdfplumber

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
n=0
with pdfplumber.open(PDF) as pdf:
    for pnum in range(10,149):
        page=pdf.pages[pnum-1]
        words=page.extract_words(keep_blank_chars=False,use_text_flow=False,extra_attrs=['fontname'])
        for line in group([w for w in words if 104<=w['top']<=page.height-43]):
            sci=[w for w in line if ci(w['x0'])==2]
            if sci and 'Italic' not in (sci[0].get('fontname','') or '') and sci[0]['text'][:1].isupper():
                print(pnum, round(line[0]['top'],1), repr(' '.join(w['text'] for w in sci)), sci[0].get('fontname'))
                n+=1
                if n>=100: raise SystemExit
