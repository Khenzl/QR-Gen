#!/data/data/com.termux/files/usr/bin/bash

# ===============================
# QR-Gen Tool Installation Script
# by Khenzl
# ===============================

# Warna
G='\033[1;32m'
R='\033[1;31m'
W='\033[0m'

clear
echo -e "${G}╔═══════════════════════════════╗${W}"
echo -e "${G}║     QR-GEN INSTALL SCRIPT     ║${W}"
echo -e "${G}╚═══════════════════════════════╝${W}\n"

echo -e "${G}[•] Memulai proses instalasi...${W}\n"

echo -e "${G}[•] Update & Upgrade packages...${W}"
pkg update -y && pkg upgrade -y

echo -e "${G}[•] Menginstal package Termux...${W}"
pkg install python -y
pkg install git -y
pkg install bash -y
pkg install termux-api -y
pkg install libjpeg-turbo -y
pkg install freetype -y
pkg install libpng -y
pkg install clang -y
pkg install zbar -y

echo -e "${G}[•] Setup akses storage Termux...${W}"
termux-setup-storage

echo -e "${G}[•] Menginstal Python modules...${W}"
pip install --upgrade pip
pip install qrcode
pip install pillow
pip install requests
pip install numpy
pip install opencv-python-headless
pip install pyzbar

# Buat folder hasil
echo -e "${G}[•] Menyiapkan folder hasil...${W}"
mkdir -p results
mkdir -p results2
mkdir -p /storage/emulated/0/QR-Results

echo -e "\n${G}[✔] Instalasi selesai.${W}"
echo -e "${G}[✔] Jalankan tool dengan: ${W}python qr_gen.py"
