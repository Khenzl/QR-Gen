# 🔳 QR-Gen - QR Code Toolkit by Khenzl

**QR-Gen** adalah tools QR Code multifungsi berbasis Python buatan Khenzl. Tools ini dapat digunakan untuk:
- Membuat QR Code dari teks atau file
- Mendekode QR Code dari gambar (via API online)
- Menyimpan hasil QR ke penyimpanan HP (khusus Android Termux)

---

## 🚀 Fitur Utama

✅ Generate QR dari teks  
✅ Generate QR dari isi file teks  
✅ Decode QR dari gambar (via online API)  
✅ Simpan hasil ke penyimpanan HP  
✅ Antarmuka CLI berwarna (ANSI Color)

---

## 📦 Instalasi

### Di Termux / Linux:
```
pkg update && pkg upgrade

pkg install git

termux-setup-storage

git clone https://github.com/khenzl/QR-Gen

cd QR-Gen

bash install.sh

python qr_gen.py
