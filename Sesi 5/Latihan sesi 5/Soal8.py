print('Identifikasi Segitiga')

sisi1 = int(input('Masukkan panjang sisi ke 1 :'))
sisi2 = int(input('Masukkan panjang sisi ke 2 :'))
sisi3 = int(input('Masukkan panjang sisi ke 3 :'))

print(sisi1, sisi2, sisi3)

if sisi1 == sisi2 == sisi3 :
    print('Segitiga sama sisi')
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3 :
    print('Segitiga sama kaki')
else :
    print('segitiga sembarang')

