daftar_belanja = []

print("masukkan 5 barang ke dalam daftar belanja")
for i in range(5):
    barang = input(f"Barang ke-{i+1}: ")
    daftar_belanja.append(barang)
    
print("\nDaftar belanja:", daftar_belanja)
for idx, barang in enumerate(daftar_belanja, start=1):
    print(f"Barang ke-{idx}: {barang}")
    
hapus_barang = input("Masukkan barang yang ingin dihapus: ")
if hapus_barang in daftar_belanja:
    daftar_belanja.remove(hapus_barang)
    print(f"Barang '{hapus_barang}' telah dihapus dari daftar belanja.")
else:
    print(f"Barang '{hapus_barang}' tidak ditemukan dalam daftar belanja.")
    
print("\nDaftar belanja setelah penghapusan:", daftar_belanja)
for idx, barang in enumerate(daftar_belanja, start=1):
    print(f"Barang ke-{idx}: {barang}")
    
    