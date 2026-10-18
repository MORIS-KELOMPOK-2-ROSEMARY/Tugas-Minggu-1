# ==================================================================================
#Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : AHMAD DANIYAL BUKHORI
# NIM   : 714260029
# Kelas : 12 D4 TI
# ==================================================================================

print("===================================")
print("Program Penentuan Grade dan Kelulusan")
print("===================================")

nilai =float(input("Masukkan nilai akhir (0-100): "))
if nilai >= 90:
    Grade = "A"
    Kelulusan = "lulus"
    if nilai >= 100:
            print("Nilai yang dimasukkan tidak valid.")
    else:
        print(f"nilai {nilai} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai >= 80:
    Grade = "B"
    Kelulusan = "lulus"
    print(f"nilai {nilai} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai >= 70:
    Grade = "C"
    Kelulusan = "lulus bersyarat"
    print(f"nilai {nilai} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai >= 60:
    Grade = "D"
    Kelulusan = "tidak lulus"
    print(f"nilai {nilai} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
elif nilai >= 50:
    Grade = "E"
    Kelulusan = "tidak lulus"
    if nilai >= 0:
        print("Nilai yang dimasukkan tidak valid.")
    else:
        print(f"nilai {nilai} setara dengan grade {Grade} dan status kelulusan {Kelulusan}.")
else:
    print("Nilai yang dimasukkan tidak valid. Silakan masukkan nilai antara 0 hingga 100.")

print("===================================")
print("Terima kasih telah menggunakan program ini.")
print("===================================")