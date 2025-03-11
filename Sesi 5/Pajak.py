jenis = str(input("Jenis Kendaraan (Mobil/Motor) :"))
njkb = int(input("Masukkan Harga Beli : "))
kepemilikan = int(input("Masukkan Kepemilikan : "))
swdkllj_jenis = jenis
swdkllj = 0

pkb = 0
if kepemilikan == 1:
    pkb += 1
elif kepemilikan == 2:
    pkb += 2
elif kepemilikan == 3:
    pkb += 3
elif kepemilikan == 4:
    pkb += 4

pajak = 0    
if pkb == 1:
    pajak = njkb*2 / 100
elif pkb == 2:
    pajak = njkb*2.5 / 100
elif pkb == 3:
    pajak = njkb*3 / 100
elif pkb == 4:
    pajak = njkb*3.5 / 100
elif pkb == 5:
    pajak = njkb*4 / 100

if swdkllj_jenis == str("Mobil") :
    swdkllj = int (143000)
else:
    swdkllj_jenis == str("Motor") 
    swdkllj = int (35000)

print("harga kedaraan anda adalah :", njkb)
print("kepemilikan kendaraan anda adalah ke :" , kepemilikan)
print("pajak yang harus anda bayar adalah : ", pajak)
print("biaya swadana kendaraan adalah : ", swdkllj)  #
print("total biaya yang harus dibayar adalah : ", pajak + swdkllj)
