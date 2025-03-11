print('Hitung BMI (Body Mass Index)')
print('--------------------------------')
berat = int(input('Masukkan Berat Badan Anda (kg) : '))
tinggi = float(input('Masukkan Tinggi Badan Anda (m) : '))

bmi = berat / (tinggi ** 2)

print("BMI Anda adalah : ", round(bmi, 2))

if bmi < 18.5:
    print('Berat Badan Anda Kurang')
elif bmi >= 18.5 and bmi < 25:
    print('Berat Badan Anda Normal')
elif bmi >= 25 and bmi < 30:
    print('Berat Badan Anda Kelebihan (diet dikit boss)')
else :
   print('Anda Obesitas awokawoka') 