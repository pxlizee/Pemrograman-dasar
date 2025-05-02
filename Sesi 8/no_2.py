buah = []
for i in range(5):
    nama_buah = input(f"Nama buah ke-{i+1}: ")
    buah.append(nama_buah)
    
print("Isi list buah:", buah)

print("buah pada index ke-2:", buah[2])

buah_baru = input("Masukkan nama buah yang ingin di tambahkan: ")
buah.append(buah_baru)

print("Isi list buah setelah ditambahkan:", buah)