angka_list = []

print("Masukkan 10 angka:")
for i in range(10):
    angka = int(input(f"Angka ke-{i+1}: "))
    angka_list.append(angka)
    
jumlah = sum(angka_list)

print("\nList angka :", angka_list)
print("Jumlah total angka :", jumlah)