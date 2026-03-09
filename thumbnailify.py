from pathlib import Path
import os
for file in Path("public/gallery").glob("*.png"):
    fname = file.name
    base = fname.split(".")[0]

    os.system(f"magick {file} -resize 128x128 public/gallery/{base}_thumb.png")