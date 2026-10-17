print("Halo saya Mahasiswa Moris IF 26")

nama = "Danil"
umur = 16 
kelas = "12 D4 TI"

print("Nama saya", nama)
print("Umur saya", umur)
print("Kelas saya", kelas)

panjang = float(input("Masukkan panjang(cm): "))
lebar = float(input("Masukkan lebar(cm): "))

print('Hitungan luas dan keliling persegi panjang')

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print("Luas persegi panjang:", luas, "cm")
print("Keliling persegi panjang:", keliling, "cm")

nilai = int(input("Masukkan nilai: "))
if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
else:
    print("Grade C")

    