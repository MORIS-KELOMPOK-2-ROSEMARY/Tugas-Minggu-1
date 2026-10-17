print("====================================================")
print("     Tugas Mandiri Modul 1 - Program Percabangan")
print("     NAMA     : MARCEL ANDREYANA ")
print("     NIM      : 714260008   ")
print("     KELAS    : 11 - D4 TEKNIK INFORMATIKA")
print("     KELOMPOK : 2 - ROSEMARY")
print("=====================================================")

nilai=float(input("Masukkan nilai: "))

if nilai > 100 :
    print(f"Nilai {nilai} tidak valid. ")
    print("Masukan nilai yang benar dimulai dari 0-100.")
elif nilai >= 80:
    print(f"Nilai Anda {nilai}, setara dengan huruf mutu A.")
    print("Selamat anda dinyatakan lulus.")
elif nilai >= 70:
    print(f"Nilai Anda {nilai}, setara dengan huruf mutu B.")
    print("Selamat anda dinyatakan lulus.")
elif nilai >= 60:
    print(f"Nilai Anda {nilai}, setara dengan huruf mutu C.")
    print("Selamat anda dinyatakan lulus.")
elif nilai >= 50:
    print(f"Nilai Anda {nilai}, setara dengan huruf mutu D.")
    print("Anda dinyatakan belum lulus.")
elif nilai >= 0:
    print(f"Nilai Anda {nilai}, setara dengan huruf mutu E.")
    print("Anda dinyataklan belum lulus.")
else :
    print(f"Nilai {nilai} tidak valid. ")
    print("Masukan nilai yang benar dimulai dari 0-100.")

print("=====================================================")
print("Terima kasih telah menggunjungi situs ini.")