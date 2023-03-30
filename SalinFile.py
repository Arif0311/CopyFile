import shutil
import os

# Mendefinisikan path file asli dan direktori tujuan
source_file = r'C:/Users/Admin/Documents/Project-Asset/assets/Laptop/LP.md'
target_dir = "C:/Users/Admin/Documents/Project-Asset/assets/Laptop/"

# Membuat direktori tujuan jika belum ada
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Menyalin file ke direktori tujuan sebanyak 500 kali
for i in range(1,501):
    # mengonversi nomor file menjadi string dengan format "1", "2", "10", dsb.
    file_number = str(i).zfill(1)

    # menambahkan angka 0 di depan nomor file jika nomornya kurang dari 100
    if i >= 100:
        file_number = "0" + file_number

    # menambahkan angka 00 di depan nomor file jika nomornya lebih dari sama dengan 10 dan kurang dari 100
    if i >= 10 and i < 100:
        file_number = "00" + file_number

    # menambahkan angka 000 di depan nomor file jika nomornya kurang dari 10
    if i < 10:
        file_number = "000" + file_number

    # menentukan nama file dengan nomor yang ditambahkan di depan
    file_name = f"LP{file_number}.md"

    # copy file dari sumber file dan tujuan direktori dengan nama file yang diinginkan
    shutil.copy(source_file, os.path.join(target_dir, file_name))

#Print Jumlah file yg disalin dan tempat penyimpanan direktori tujuan
print("File berhasil disalin ke direktori sebanyak", i ,"file", target_dir)
