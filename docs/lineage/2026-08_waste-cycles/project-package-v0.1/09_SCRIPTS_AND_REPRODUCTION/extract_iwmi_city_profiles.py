from pathlib import Path
import re

text = Path('/home/ubuntu/anavaratha/IWMI_SriLanka_20_city_waste_inventory_2020.txt').read_text(errors='ignore')
# Use the city-profile section only, beginning at the contents marker after the introduction.
text = text[text.find('CITY PROFILES'):]
pat = re.compile(r'(?m)^\s*(\d{1,2})\.\s*([A-Za-z][A-Za-z ]+?)\s*\n')
heads = list(pat.finditer(text))
for i,m in enumerate(heads):
    start=m.start(); end=heads[i+1].start() if i+1<len(heads) else len(text)
    name=m.group(2).strip()
    block=text[start:end]
    Path(f'/home/ubuntu/anavaratha/IWMI_profile_{m.group(1)}_{name.replace(" ","_")}.txt').write_text(block)
    print(m.group(1), name, len(block))
