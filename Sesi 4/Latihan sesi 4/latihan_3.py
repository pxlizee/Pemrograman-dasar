total_belanjaan = int(input("Harga total belanjaan : "))

diskon_10 = (total_belanjaan * 10) / 100
diskon_5 = (total_belanjaan * 5) / 100

if total_belanjaan >= 100000:
    total_bayar = total_belanjaan - diskon_10
    print("anda mendapatkan diskon sebesar 10 % :" , diskon_10)
    print("Total bayar dengan diskon 10% : ", total_bayar)
elif total_belanjaan >= 50000:
    total_bayar = total_belanjaan - diskon_5
    print("anda mendapatkan diskon sebesar 5% : ", diskon_5)
    print("Total bayar dengan diskon 5% : ", total_bayar)
else:
    print("Kamu tidak mendapatkan diskon")
  