print("=================================================")
print("Tugas Mandiri Modul 1 - Program Percabangan")
print("NAMA : Ilham Muammar Nabil")
print("NIM: 714260005")
print("KELAS : IF-1A")
print("Kelompok : 2")
print("==================================================")
#Pengguna akan input untuk memasukkan nilai
nilai = float(input("Masukkan nilai: "))
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid. Masukkan nilai antara 0 hingga 100.")
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 60:
    print("Nilai D")
elif nilai >= 50:
    print("Nilai E")
else:
    print("Nilai F")
#Menentukan kelulusan berdasarkan nilai yang dimasukkan
if nilai < 0 or nilai > 100:
    if nilai < 65:
        print("Anda tidak lulus")
    else:
        print("Anda lulus")