angka1 = int(input("Masukkan Angka ke 1 :"))
angka2 = int(input("Masukkan Angka ke 2 :"))
angka3 = int(input("Masukkan Angka ke 3 :"))

total = (angka1, angka2, angka3)
if angka1 > angka2 or angka1 > angka3 or angka2 > angka3 or angka3 > angka2 or angka3 > angka1:
    print("Angka yang terbesar adalah : ", max(total))
else:
    print('null')


