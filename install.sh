#!/data/data/com.termux/files/usr/bin/bash

echo -e "\033[1;34m[•] Menginstal dependencies...\033[0m"

pkg update -y
pkg install python git -y
pip install qrcode pillow requests

mkdir -p results
mkdir -p results2
mkdir -p /storage/emulated/0/QR-Results

echo -e "\033[1;32m[✓] Instalasi selesai! Jalankan dengan: python qr_gen.py"
