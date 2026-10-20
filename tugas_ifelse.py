# ===================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Hanif irham fadhillah
# NIM   : 613260007
# Kelas : 11 D3
# ===================================================

# Judul Program
print("===================================")
print("  KONVERSI NILAI ANGKA KE HURUF MUTU")
print("===================================")

# Mengambil input dari pengguna
nilai = float(input("Masukkan nilai akhir (0 - 100): "))

print("-----------------------------------")

# Validasi rentang nilai 0 - 100
if nilai < 0 or nilai > 100:
    print(f"Kesalahan: Nilai {nilai} berada di luar rentang 0 - 100!")
    print("Harap masukkan nilai angka yang valid.")

# Minimal menggunakan 4 elif untuk pengondisian huruf mutu (A, B, C, D, E)
elif nilai >= 85:
    print(f"Nilai Angka  : {nilai}")
    print("Huruf Mutu   : A")
    print("Keterangan   : Lulus (Sangat Baik)")

elif nilai >= 70:
    print(f"Nilai Angka  : {nilai}")
    print("Huruf Mutu   : B")
    print("Keterangan   : Lulus (Baik)")

elif nilai >= 55:
    print(f"Nilai Angka  : {nilai}")
    print("Huruf Mutu   : C")
    print("Keterangan   : Lulus (Cukup)")

elif nilai >= 40:
    print(f"Nilai Angka  : {nilai}")
    print("Huruf Mutu   : D")
    print("Keterangan   : Tidak Lulus (Kurang)")

else:
    print(f"Nilai Angka  : {nilai}")
    print("Huruf Mutu   : E")
    print("Keterangan   : Tidak Lulus (Sangat Kurang)")

# Pemisah dan pesan penutup
print("===================================")
print("Terima kasih telah menggunakan program ini.")