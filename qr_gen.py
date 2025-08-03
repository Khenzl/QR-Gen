import os
import sys
import time
import shutil
import qrcode
import requests
from PIL import Image
from datetime import datetime

# Warna
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
B = '\033[1;34m'
W = '\033[0m'

# =========================
# Banner
# =========================
def banner():
    os.system('clear')
    print(f"""
{C}
  ░██████   ░█████████            ░██████                        
 ░██   ░██  ░██     ░██          ░██   ░██                       
░██     ░██ ░██     ░██         ░██         ░███████  ░████████  
░██     ░██ ░█████████  ░██████ ░██  █████ ░██    ░██ ░██    ░██ 
░██     ░██ ░██   ░██           ░██     ██ ░█████████ ░██    ░██ 
 ░██   ░██  ░██    ░██           ░██  ░███ ░██        ░██    ░██ 
  ░██████   ░██     ░██           ░█████░█  ░███████  ░██    ░██ 
       ░██                                                       
        ░██ 
{B}            ╔════════════════════════════════════╗
            ║       {Y}QR-Code Tool by Khenzl{B}       ║
            ╠════════════════════════════════════╣
            ║{C} [1] {G}Generate QR dari Teks          {B}║
            ║{C} [2] {G}Generate QR dari File Teks     {B}║
            ║{C} [3] {G}Decode QR dari Gambar (Online) {B}║
            ║{C} [4] {G}Simpan Hasil ke Storage        {B}║
            ║{Y} [0] {R}Keluar                         {B}║
            ╚════════════════════════════════════╝{W}
""")


# QR Teks
def generate_qr_text():
    try:
        # Input data untuk QR
        data = input(f"{Y}[>] Masukkan teks (Enter kosong untuk batal): {W}\n")
        if data.strip() == "":
            print(f"{R}[!] Dibatalkan oleh pengguna.{W}")
            return
        
        # Menanyakan apakah ingin menyimpan gambar
        save_confirmation = input(f"\n{Y}[>] Apakah Anda ingin menyimpan gambar QR? (y/n): {W}")
        if save_confirmation.lower() != 'y':
            print(f"{R}[!] Gambar tidak disimpan.{W}")
            return
        
        # Menentukan folder penyimpanan
        folder = "results"
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Membuat nama file berdasarkan timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{folder}/qrcode_{timestamp}.png"
        
        # Membuat QR dan menyimpannya
        img = qrcode.make(data)
        img.save(filename)
        print(f"{G}[✓] QR-Code berhasil dibuat dan disimpan: {filename}{W}")
    
    except KeyboardInterrupt:
        print(f"\n{R}[!] Dibatalkan.{W}")

# QR dari file teks
def generate_qr_file():
    try:
        # Input path file
        path = input(f"{Y}[>] Masukkan path file teks: {W}\n")
        if not os.path.exists(path):
            print(f"{R}[!] File tidak ditemukan.{W}")
            return
        
        # Baca isi file
        with open(path, 'r') as f:
            data = f.read().strip()
        
        if data == "":
            print(f"{R}[!] File kosong, tidak bisa dibuat QR-Code.{W}")
            return

        # Konfirmasi simpan
        confirm = input(f"{Y}[>] Apakah Anda ingin menyimpan QR dari file ini? (y/n): {W}")
        if confirm.lower() != 'y':
            print(f"{R}[!] Dibatalkan. Gambar tidak disimpan.{W}")
            return

        # Buat folder jika belum ada
        folder = "results"
        os.makedirs(folder, exist_ok=True)

        # Buat nama file unik berdasarkan waktu
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{folder}/qrcode_file_{timestamp}.png"

        # Generate QR dan simpan
        img = qrcode.make(data)
        img.save(filename)
        print(f"{G}[✓] QR-Code berhasil dibuat dan disimpan: {filename}{W}")

    except KeyboardInterrupt:
        print(f"\n{R}[!] Dibatalkan.{W}")

# Decode QR secara online
def decode_qr_online():
    try:
        folder_qr = "/storage/emulated/0/QR-Results"
        
        # Ambil semua file gambar QR
        file_list = [f for f in os.listdir(folder_qr) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if not file_list:
            print(f"{R}[!] Tidak ada file gambar QR ditemukan di {folder_qr}.{W}")
            return

        # Tampilkan daftar file
        print(f"{Y}Daftar QR di {folder_qr}:{W}")
        for i, file in enumerate(file_list):
            print(f"{G}[{i+1}] {file}{W}")

        # Pilih file berdasarkan nomor
        pilih = input(f"\n{Y}[>] Pilih nomor file QR yang ingin didekode: {W}")
        if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(file_list):
            print(f"{R}[!] Nomor tidak valid.{W}")
            return
        
        filename = file_list[int(pilih)-1]
        path = os.path.join(folder_qr, filename)

        with open(path, 'rb') as img_file:
            files = {'file': img_file}
            print(f"{B}[•] Mengirim gambar ke API decode...{W}\n")
            response = requests.post('https://api.qrserver.com/v1/read-qr-code/', files=files)

            if response.status_code == 200:
                result = response.json()[0]['symbol'][0]['data']
                if result:
                    # Tampilkan ke layar
                    print(f"{G}[✓] Hasil Decode: {W}{result}")
                    
                    # Simpan ke file
                    os.makedirs("results2", exist_ok=True)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    result_file = f"results2/decode_result_{timestamp}.txt"
                    with open(result_file, 'w') as f:
                        f.write(result)
                    
                    print(f"{G}[✓] Hasil decode disimpan ke: {result_file}{W}")
                else:
                    print(f"{R}[!] Gagal membaca QR dari gambar.{W}")
            else:
                print(f"{R}[!] Gagal konek ke API (status: {response.status_code}){W}")

    except KeyboardInterrupt:
        print(f"\n{R}[!] Dibatalkan oleh pengguna.{W}")

# Simpan ke Storage
def simpan_ke_penyimpanan():
    try:
        hasil_folder = "results"
        penyimpanan_tujuan = "/storage/emulated/0/QR-Results"

        # Buat folder tujuan jika belum ada
        if not os.path.exists(penyimpanan_tujuan):
            os.makedirs(penyimpanan_tujuan)

        # Salin semua file dari 'results/' ke penyimpanan
        for file_nama in os.listdir(hasil_folder):
            sumber_path = os.path.join(hasil_folder, file_nama)
            tujuan_path = os.path.join(penyimpanan_tujuan, file_nama)
            shutil.copy2(sumber_path, tujuan_path)

        print(f"\n{G}[✓] Semua hasil QR telah disalin ke: {penyimpanan_tujuan}\n")
    except Exception as e:
        print(f"{Y}[!] Gagal menyalin hasil: {str(e)}")

# Main Program
def main():
    try:
        while True:
            banner()
            pilih = input(f"{B}[?] Pilih menu: {W}")
            if pilih == "1":
                generate_qr_text()
            elif pilih == "2":
                generate_qr_file()
            elif pilih == "3":
                decode_qr_online()
            elif pilih == "4":
                simpan_ke_penyimpanan()
            elif pilih == "0":
                print(f"{Y}[✓] Terima kasih telah menggunakan QR Generated!{W}")
                sys.exit()
            else:
                print(f"{R}[!] Pilihan tidak valid!{W}")
            input(f"{B}Tekan Enter untuk kembali ke menu...{W}")
    except KeyboardInterrupt:
        print(f"\n{R}[!] Keluar dari program...{W}")
        sys.exit()

if __name__ == "__main__":
    main()
