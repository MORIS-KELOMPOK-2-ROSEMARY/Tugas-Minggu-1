# ========================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama : Marissa Strachan
# NIM : 613260018
# Kelas : D3 TI 1A
# ========================================

print("========================================")
print(" Konversi Nilai Angka ke Huruf Mutu ")
print("========================================")

nilai = float(input("Masukkan Nilai Akhir Anda (0-100):"))

print("========================================")

if nilai < 0 or nilai > 100:
    print(f"Kesalahan: Nilai {nilai} berada di luar rentang 0-100!")
    print("Harap masukkan nilai angka yang valid.")
elif nilai >= 85:
    huruf = "A"
    keterangan = "LULUS"
elif nilai >= 70:
    huruf = "B"
    keterangan = "LULUS"
elif nilai >= 60:
    huruf = "C"
    keterangan = "LULUS"
elif nilai >= 50:
    huruf = "D"
    keterangan = "LULUS"
else:
    huruf = "E"
    keterangan = "TIDAK LULUS"
if 0 <= nilai <= 100:
    print("-----------------------------------------")
    print(f"Nilai : {nilai}")
    print(f"Huruf Mutu : {huruf}")
    print(f"Keterangan {keterangan}")
    print("-----------------------------------------")
    


