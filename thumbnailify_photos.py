from pathlib import Path
import os
for file in Path("public/photos").glob("*.jpg"):
    fname = file.name
    base = fname.split(".")[0]

    os.system(f"magick {file} -resize 128x128 public/photos/{base}_thumb.jpg")