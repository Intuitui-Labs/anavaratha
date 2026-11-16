from pathlib import Path
import pdfplumber
from collections import defaultdict

PDF = Path('/home/ubuntu/anavaratha/source_files/medicinal_plant_checklist_2025.pdf')
BOUNDS = [56, 145, 231, 330, 416, 581, 690, 741, 790]

def ci(x):
    for i in range(8):
        if BOUNDS[i] <= x < BOUNDS[i+1]: return i
    return None

def group(words):
    lines=[]
    for w in sorted(words,key=lambda x:(x['top'],x['x0'])):
        for line in lines:
            if abs(line[0]['top']-w['top'])<=1.7:
                line.append(w); break
        else: lines.append([w])
    return lines

counts=defaultdict(int)
examples=[]
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
            first=sci[0]['text']
            font=sci[0].get('fontname','')
            key=('italic' if 'Italic' in font else 'plain', 'upper' if first[:1].isupper() else 'lower', first[:20])
            counts[key]+=1
            if 'Italic' in font and first[:1].isupper() is False and len(examples)<40:
                examples.append((pnum, line[0]['top'], [w['text'] for w in sci]))
print('line categories:')
for k,v in sorted(counts.items(), key=lambda kv:(kv[0][0],kv[0][1],kv[0][2])):
    print(v,k)
print('italic lowercase examples:')
for e in examples: print(e)
