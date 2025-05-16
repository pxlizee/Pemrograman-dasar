mahasiswa = {}

def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    if nim in mahasiswa:
        print("NIM sudah ada. Silakan masukkan NIM yang berbeda.")
        return
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    try:
        ipk = float(input("Masukkan IPK: "))
    except ValueError:
        print("IPK harus berupa angka. Silakan coba lagi.")
        return
    mahasiswa[nim] = {
        "Nama": nama,
        "Jurusan": jurusan,
        "IPK": ipk
    }
    print("Data mahasiswa berhasil ditambahkan.")
    
def tampilkan_semua():
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    print("Daftar Mahasiswa:")
    for nim, data in mahasiswa.items():
        print(f"NIM: {nim}, Nama: {data['Nama']}, Jurusan: {data['Jurusan']}, IPK: {data['IPK']}")
        
def cari_mahasiswa():
    nim = input("Masukkan NIM: ")
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print(f"NIM: {nim}, Nama: {data['Nama']}, Jurusan: {data['Jurusan']}, IPK: {data['IPK']}")
    else:
        print("Data mahasiswa tidak ditemukan.")
def hapus_mahasiswa():
    nim = input("Masukkan NIM: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_mahasiswa()
        elif pilihan == '2':
            tampilkan_semua()
        elif pilihan == '3':
            cari_mahasiswa()
        elif pilihan == '4':
            hapus_mahasiswa()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
menu()