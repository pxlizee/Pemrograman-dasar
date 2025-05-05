input_angka = input("Masukkan angka: ")
list_angka = [float(angka) for angka in input_angka.split()]

jumlah_total = sum(list_angka)

rata_rata = jumlah_total / len(list_angka) if list_angka else 0

nilai_max = max(list_angka)
nilai_min = min(list_angka)

print("\nHasil perhitungan:")
print(f"List angka: {list_angka}")
print(f"Jumlah total: {jumlah_total}")
print(f"Rata-rata: {rata_rata}")
print(f"Nilai Terbesar: {nilai_max}")
print(f"Nilai Terkecil: {nilai_min}")

