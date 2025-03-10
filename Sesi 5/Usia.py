umur = int(input('Masukkan Umur (Dalam Tahun) :'))

if int(umur) <= 2:
    print('Anda Bayi')
elif int(umur) <= 5:
    print('Anda Balita')
elif int(umur) <= 12:
    print('Anda Anak-Anak')
elif int(umur) <= 18:
    print('Anda Remaja')
else :
    print('Anda Dewasa')  