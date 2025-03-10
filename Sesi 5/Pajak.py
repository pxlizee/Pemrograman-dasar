njkb = int(input("Masukkan Harga Beli : "))
jenis = str(input("Jenis Kendaraan (Mobil/Motor) :"))
kepemilikan = int(input("Masukkan Kepemilikan : "))
swdkllj = str(input("Jenis Kendaraan (Mobil/Motor) :"))
pajak = ()
pkb = 0
if kepemilikan == 1:
    pkb += 1
elif kepemilikan == 2:
    pkb += 2
elif kepemilikan < 3:
    pkb += 3
    
if pkb == 1:
    pajak = njkb / 2
elif pkb == 2:
    pajak = njkb / 2.5
elif pkb < 3:
    pajak = 