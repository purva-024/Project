# 🖼️ Image Resizer (File Size Based)

A simple Python tool that resizes/compresses an image to a target file size (e.g., 200 KB).  
Useful for generating web-optimized images, compressing large files, or preparing images for upload.

---

## 📦 Features

- Compresses images to a target size in **KB**
- Automatically finds the image in the `input/` folder
- Saves the compressed output to the `output/` folder
- Works best with **JPEG** and **WebP** formats
- Uses only `Pillow` (no heavy dependencies)

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/yourusername/ImageResizer.git
cd ImageResizer/image-resizer

python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

pip install pillow

python resize_images.py
```
