isi = (1, 2, 3, 4, 5)

def hitung_ganjil(tup):
    count = 0
    for i in tup:
        if i % 2 != 0:
            count += 1
    return count
print("Jumlah elemen angka ganjil dalam tuple:", hitung_ganjil(isi))