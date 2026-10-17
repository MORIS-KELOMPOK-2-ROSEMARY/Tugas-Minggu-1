print("================================")
print("   KALKULATOR SEDERHANA   ")
print("================================")
print("operasi tersedia: + - * /")
print("--------------------------------")
# --- Bagian masukan pengguna ---
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")
print("--------------------------------")
# --- Bagian proses ---
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil:.2f}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil:.2f}")
elif operator == "/":
    if angka2 == 0:
        print("kesalahan bilangan tidak dapat dibagi dengan 0")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil:.2f}")
else:
    print(f"Operator '{operator}' tidak dikenali")
    print("gunakan salah satu dari: + - * /")
print("================================")
print("Terima kasih telah menggunakan kalkulator sederhana ini!")
