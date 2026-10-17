
print("===================================")
print("KALKULATOR KONSOL SEDERHANA")
print("===================================")
print("Operasi yang tersedia: + - * /")
print("-----------------------------------")

angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

print("-----------------------------------")

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
        print("kesalahan: bilangan tidak dapat dibagi dengan nol")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil:.2f}")

else:
    print(f"Operator '{operator}' tidak di kenali.")
    print("Silahkan gunakan salah satu dari: +, -, *, /.")

print("===================================")
print("Terima kasih telah menggunakan kalkulator ini.")