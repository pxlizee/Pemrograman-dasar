uang_100000 = uang_50000 = uang_20000 = uang_10000 = uang_5000 = uang_2000 = uang_1000 = uang_500 = 0
uang = int(input("Masukkan Jumlah Uang :"))

sisa_uang_100000 = uang % 100000
uang_100000 = (uang - sisa_uang_100000) / 100000

sisa_uang_50000 = sisa_uang_100000 % 50000
uang_50000 = (uang_100000 - sisa_uang_50000) / 50000

sisa_uang_20000 = uang_50000 % 20000
uang_20000 = (uang_50000 - sisa_uang_20000) / 20000

sisa_uang_10000 = uang_20000 % 10000
uang_10000 = (uang_20000 - sisa_uang_10000) / 10000

sisa_uang_5000 = uang_10000 % 5000
uang_5000 = (uang_10000 - sisa_uang_5000) / 5000

sisa_uang_2000 = uang_5000 % 2000
uang_2000 = (uang_5000 - sisa_uang_2000) / 2000

sisa_uang_1000 = uang_2000 % 1000
uang_1000 = (uang_2000 - sisa_uang_1000) / 1000

sisa_uang_500 = uang_1000 % 500
uang_500 = (uang_1000 - sisa_uang_500) / 500

print ("Uang 100000 :" , int(uang_100000), "lembar")
print ("Uang 50000 :" , int(uang_50000), "lembar")
print ("Uang 20000 : ", int(uang_20000), "lembar")
print ("uang 10000 : ", int(uang_10000), "lembar")
print ("Uang 5000 : ", int(uang_5000), "lembar")
print ("Uang 2000 : ", int(uang_2000), "lembar")
print ("Uang 1000 : ", int(uang_1000), "lembar")
print ("Uang 500 : ", int(uang_500), "lembar")

