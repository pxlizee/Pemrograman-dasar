
uang_100000 = uang_50000 = uang_20000 = uang_10000 = uang_5000 = uang_2000 = uang_1000 = uang_500 = 0
uang = int(input("Masukkan Jumlah Uang: "))

uang_100000 = uang // 100000
sisa_uang = uang % 100000

uang_50000 = sisa_uang // 50000
sisa_uang = sisa_uang % 50000

uang_20000 = sisa_uang // 20000
sisa_uang = sisa_uang % 20000

uang_10000 = sisa_uang // 10000
sisa_uang = sisa_uang % 10000

uang_5000 = sisa_uang // 5000
sisa_uang = sisa_uang % 5000

uang_2000 = sisa_uang // 2000
sisa_uang = sisa_uang % 2000

uang_1000 = sisa_uang // 1000
sisa_uang = sisa_uang % 1000

uang_500 = sisa_uang // 500

print("Uang 100000:", uang_100000, "lembar")
print("Uang 50000:", uang_50000, "lembar")
print("Uang 20000:", uang_20000, "lembar")
print("Uang 10000:", uang_10000, "lembar")
print("Uang 5000:", uang_5000, "lembar")
print("Uang 2000:", uang_2000, "lembar")
print("Uang 1000:", uang_1000, "lembar")
print("Uang 500:", uang_500, "lembar")
