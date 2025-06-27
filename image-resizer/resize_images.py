from PIL import Image
from pathlib import Path
import io

# === Folder Config ===
INPUT_FOLDER = Path("input")
OUTPUT_FOLDER = Path("output")
OUTPUT_FOLDER.mkdir(exist_ok=True)

# === Get the first .jpg or .jpeg image from input/ ===
input_images = list(INPUT_FOLDER.glob("*.jpg")) + list(INPUT_FOLDER.glob("*.jpeg"))
if not input_images:
    print("❌ No JPG/JPEG image found in 'input/' folder.")
    exit()

input_path = input_images[0]
img = Image.open(input_path)
img_format = img.format if img.format in ["JPEG", "WEBP"] else "JPEG"

# === Ask user for target size in KB ===
target_kb = input("📦 Enter target size in KB (e.g. 200): ")
try:
    target_kb = int(target_kb)
except ValueError:
    print("❌ Invalid number.")
    exit()

target_bytes = target_kb * 1024
quality = 95
step = 5
min_quality = 10

# === Compress by reducing quality ===
while quality >= min_quality:
    buffer = io.BytesIO()
    img.save(buffer, format=img_format, quality=quality, optimize=True)
    size = buffer.tell()

    if size <= target_bytes:
        output_path = OUTPUT_FOLDER / f"{input_path.stem}_{target_kb}KB.{img_format.lower()}"
        with open(output_path, "wb") as f:
            f.write(buffer.getvalue())
        print(f"✅ Compressed and saved: {output_path} ({round(size/1024)} KB, quality={quality})")
        break

    quality -= step
else:
    print("⚠️ Couldn't compress below target size without losing too much quality.")
