k1 = input("Apakah dia Tampan? (ya/tidak): ")
k2 = input("Apakah dia Kaya? (ya/tidak): ")
k3 = input("Apakah dia Sholeh? (ya/tidak): ")
k4 = input("Apakah dia Pinter? (ya/tidak): ")
k5 = input("Apakah dia Setia? (ya/tidak): ")

jumlah_yes = 0
if k1 == "ya":
    jumlah_yes += 1
if k2 == "ya":
    jumlah_yes += 1
if k3 == "ya":
    jumlah_yes += 1
if k4 == "ya":
    jumlah_yes += 1
if k5 == "ya":
    jumlah_yes += 1

print(jumlah_yes)
if jumlah_yes >= 3:
    print("Dia adalah Pria Ideal")
else:
    print("Ngaca")
