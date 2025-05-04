import statistics


input_angka = input("Masukkan minimal 5 angka, pisah dengan spasi: ")
list_angka = list(map(float, input_angka.split()))

if len(list_angka) < 5:
    print("Jumlah angka kurang dari 5. Silakan coba lagi.")
else:
    nilai_min = min(list_angka)
    nilai_max = max(list_angka)
    rata_rata = sum(list_angka) / len(list_angka)
    median = statistics.median(list_angka)
    
    angka_urut = sorted(list_angka)
    
    print("\nHasil perhitungan:")
    print(f"List angka: {list_angka}")
    print(f"List angka setelah diurutkan: {angka_urut}")
    print(f"Nilai Terbesar: {nilai_max}")
    print(f"Nilai Terkecil: {nilai_min}")
    print(f"Rata-rata: {rata_rata}")
    print(f"Median: {median}")
    
    