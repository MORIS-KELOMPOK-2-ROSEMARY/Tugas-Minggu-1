# ==================================================================================
#Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : AHMAD DANIYAL BUKHORI
# NIM   : 714260029
# Kelas : 12 D4 TI
# ==================================================================================

nilai =float(input("Masukkan nilai akhir (0-100): "))
if nilai >= 90:
    Grade = "A"
    Kelulusan = "lulus"
elif nilai >= 80:
    Grade = "B"
    Kelulusan = "lulus"
elif nilai >= 70:
    Grade = "C"
    Kelulusan = "lulus bersyarat"
elif nilai >= 60:
    Grade = "D"
    Kelulusan = "tidak lulus"
elif nilai >= 50:
    Grade = "E"
    Kelulusan = "tidak lulus"
else:
    Grade = "F"
    Kelulusan = "tidak lulus"

print(f"nilai {nilai} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")