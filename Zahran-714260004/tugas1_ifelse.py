
print("====== Kenalan ======")
print("-------------------------------")

nama = "Zahran Al Kautsar"
npm = "714260004"
kelas = "D4 Teknik Informatika 11"
kelompok = "RoseMery"

print("Nama     : ", nama)
print("NPM      : ", npm)
print("Kelas    : ", kelas)
print("Kelompok : ", kelompok)

print("-------------------------------")

nilai = float(input("Masukkan nilai akhir (0-100) : "))

if nilai < 0 or nilai > 100:
    print("ERROR: Nilai harus berada dalam rentang 0-100!")
else:
    if nilai >= 80:
        huruf = "A"
    elif nilai >= 70:
        huruf = "B"
    elif nilai >= 60:
        huruf = "C"
    elif nilai >= 50:
        huruf = "D"
    elif nilai >= 40:
        huruf = "E"
    else:
        huruf = "F"

    if nilai >= 60:
        keterangan = "LULUS"
    else:
        keterangan = "TIDAK LULUS"

    print(f"Nilai {nilai} setara dengan huruf mutu {huruf}")
    print("Keterangan :", keterangan)
