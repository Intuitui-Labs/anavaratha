from pathlib import Path
from PIL import Image
base=Path('/home/ubuntu/anavaratha')
# Use high-resolution rendered page generated separately.
src=base/'WMA_masterplan_page-050_300dpi.png'
out=base/'WMA_open_dump_map_crop_300dpi.png'
img=Image.open(src)
# Figure 2-10 occupies the upper-to-middle page; retain map, legend, and caption.
img.crop((250,180,2050,2450)).save(out)
print(img.size, out, Image.open(out).size)
