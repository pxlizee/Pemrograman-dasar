import pandas as pd
from tabulate import tabulate
from datetime import datetime

# --- KONFIGURASI DAN DATA ---
AVAILABLE_ROOMS = {
    'A': {'floors': list(range(1, 6)), 'rooms': None},
    'B': {'floors': list(range(1, 7)), 'rooms': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']}
}
ALLOWED_DAYS = ['SENIN', 'SELASA', 'RABU', 'KAMIS', 'JUMAT']
MIN_TIME = datetime.strptime("08:00", "%H:%M").time()
MAX_TIME = datetime.strptime("20:00", "%H:%M").time()
BREAKS = [
    (datetime.strptime("12:00", "%H:%M").time(), datetime.strptime("13:00", "%H:%M").time()),
    (datetime.strptime("18:00", "%H:%M").time(), datetime.strptime("19:00", "%H:%M").time())
]

# --- FUNGSI UTAMA PROGRAM ---

def muat_data(nama_file):
    """Membaca data dan secara otomatis menambahkan kolom yang hilang jika file lama terdeteksi."""
    kolom_wajib = ['HARI', 'DOSEN', 'MATAKULIAH', 'KELAS', 'PRODI', 'GEDUNG', 'LANTAI', 'RUANGAN', 'MULAI', 'SELESAI', 'TANGGAL_DIBUAT']
    try:
        df = pd.read_excel(nama_file)
        print(f"✅ Berhasil memuat data dari '{nama_file}'.")
        
        # PERBAIKAN: Periksa dan tambahkan kolom yang hilang
        kolom_hilang = False
        for col in kolom_wajib:
            if col not in df.columns:
                print(f"⚠️ Peringatan: Kolom '{col}' tidak ditemukan di file Excel. Menambahkan kolom baru.")
                df[col] = '-' # Memberi nilai default
                kolom_hilang = True
        if kolom_hilang:
            print("ℹ️ Struktur file Excel telah diperbarui.")

    except FileNotFoundError:
        print(f"ℹ️ File '{nama_file}' tidak ditemukan. Membuat jadwal baru.")
        df = pd.DataFrame(columns=kolom_wajib)
    return df

# --- (Fungsi-fungsi lainnya tetap sama persis seperti jawaban sebelumnya) ---

def is_time_slot_valid(start_str, end_str):
    try:
        start_t = datetime.strptime(start_str, "%H:%M").time()
        end_t = datetime.strptime(end_str, "%H:%M").time()
    except (ValueError, TypeError):
        print("❌ Format waktu salah. Gunakan format HH:MM (contoh: 09:30).")
        return False
    if not (MIN_TIME <= start_t < MAX_TIME and MIN_TIME < end_t <= MAX_TIME and start_t < end_t):
        print(f"❌ Error: Waktu reservasi harus antara {MIN_TIME.strftime('%H:%M')} dan {MAX_TIME.strftime('%H:%M')}.")
        return False
    for break_start, break_end in BREAKS:
        if max(start_t, break_start) < min(end_t, break_end):
            print(f"❌ Error: Tidak boleh reservasi pada jam istirahat ({break_start.strftime('%H:%M')} - {break_end.strftime('%H:%M')}).")
            return False
    return True

def is_room_available(df, day, start_str, end_str, gedung, lantai, ruangan):
    start_t = datetime.strptime(start_str, "%H:%M").time()
    end_t = datetime.strptime(end_str, "%H:%M").time()
    bookings = df[
        (df['HARI'] == day) & 
        (df['GEDUNG'] == gedung) & 
        (df['LANTAI'] == int(lantai)) & 
        (df['RUANGAN'] == ruangan)
    ]
    for _, row in bookings.iterrows():
        booked_start = datetime.strptime(row['MULAI'], "%H:%M").time()
        booked_end = datetime.strptime(row['SELESAI'], "%H:%M").time()
        if max(start_t, booked_start) < min(end_t, booked_end):
            print(f"❌ Error: Lokasi ini sudah dipesan dari jam {row['MULAI']}-{row['SELESAI']}.")
            return False
    return True

def tampilkan_jadwal(df):
    if df.empty:
        print("\nJadwal reservasi masih kosong.")
    else:
        df_sorted = df.copy()
        df_sorted['MULAI_TIME'] = pd.to_datetime(df_sorted['MULAI'], format='%H:%M').dt.time
        df_sorted = df_sorted.sort_values(by=['HARI', 'LANTAI', 'MULAI_TIME']).drop(columns=['MULAI_TIME'])
        for hari, grup in df_sorted.groupby('HARI'):
            print(f"\n----- {hari.upper()} -----")
            print(tabulate(grup, headers='keys', tablefmt='plain', showindex=False))

def tambah_reservasi(df):
    print("\n--- 📝 Tambah Reservasi Ruangan Baru ---")
    dosen = input("Nama Dosen Pengampu: ")
    matakuliah = input("Nama Mata Kuliah: ")
    kelas = input("Kelas (Contoh: TI23): ").upper()
    prodi = kelas[:2]
    
    while True:
        hari = input(f"Hari (Senin-Jumat): ").upper()
        if hari not in ALLOWED_DAYS: print(f"❌ Error: Pilih hari dari Senin sampai Jumat."); continue
        mulai = input("Jam Mulai (HH:MM): ")
        selesai = input("Jam Selesai (HH:MM): ")
        if not is_time_slot_valid(mulai, selesai): continue
        gedung = input("Pilih Gedung (A/B): ").upper()
        if gedung not in AVAILABLE_ROOMS: print("❌ Error: Gedung hanya A atau B."); continue
        try:
            lantai = int(input(f"Pilih Lantai di Gedung {gedung} ({AVAILABLE_ROOMS[gedung]['floors']}): "))
            if lantai not in AVAILABLE_ROOMS[gedung]['floors']: print("❌ Error: Lantai tidak tersedia."); continue
        except ValueError: print("❌ Error: Lantai harus berupa angka."); continue
        ruangan = '-'
        if gedung == 'B':
            ruangan = input(f"Pilih Ruangan di Lantai {lantai} ({AVAILABLE_ROOMS['B']['rooms']}): ").upper()
            if ruangan not in AVAILABLE_ROOMS['B']['rooms']: print("❌ Error: Ruangan tidak tersedia."); continue
        if is_room_available(df, hari, mulai, selesai, gedung, lantai, ruangan):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_baru = pd.DataFrame([{'HARI': hari, 'DOSEN': dosen, 'MATAKULIAH': matakuliah, 'KELAS': kelas, 'PRODI': prodi, 'GEDUNG': gedung, 'LANTAI': lantai, 'RUANGAN': ruangan, 'MULAI': mulai, 'SELESAI': selesai, 'TANGGAL_DIBUAT': timestamp}])
            df = pd.concat([df, data_baru], ignore_index=True)
            print("\n✅ Reservasi berhasil ditambahkan!")
            return df
        else:
            print("Silakan pilih waktu atau lokasi lain.")

def edit_reservasi(df):
    if df.empty:
        print("\nJadwal kosong, tidak ada yang bisa diedit."); return df
    print("\n--- ✏️ Daftar Reservasi Saat Ini ---"); print(tabulate(df, headers='keys', tablefmt='grid', showindex=True))
    try:
        index_edit = int(input("\nMasukkan nomor baris (index) yang ingin diedit: "))
        if index_edit not in df.index: print("❌ Index tidak valid."); return df
    except ValueError: print("❌ Input tidak valid."); return df
    data_lama = df.loc[index_edit].copy()
    data_baru = data_lama.copy()
    df_tanpa_edit = df.drop(index_edit)
    print("\n--- Mengedit Reservasi (kosongkan jika tidak ingin diubah) ---")
    for kolom in [c for c in df.columns if c != 'TANGGAL_DIBUAT']:
        nilai_baru = input(f"{kolom} (sebelumnya: {data_lama[kolom]}): ")
        if nilai_baru:
            if kolom in ['HARI', 'GEDUNG', 'KELAS', 'RUANGAN', 'PRODI']:
                data_baru[kolom] = nilai_baru.upper()
            else:
                data_baru[kolom] = nilai_baru
    print("\nValidasi hasil editan...")
    if data_baru['HARI'] not in ALLOWED_DAYS:
        print(f"❌ Error Validasi: Hari harus di antara Senin sampai Jumat.")
        return df
    if (is_time_slot_valid(str(data_baru['MULAI']), str(data_baru['SELESAI'])) and
        is_room_available(df_tanpa_edit, data_baru['HARI'], str(data_baru['MULAI']), str(data_baru['SELESAI']), data_baru['GEDUNG'], data_baru['LANTAI'], data_baru['RUANGAN'])):
        df.loc[index_edit] = data_baru
        print("\n✅ Reservasi berhasil diperbarui!")
    else:
        print("\n❌ Edit dibatalkan karena data baru tidak valid atau bentrok.")
    return df

def hapus_reservasi(df):
    if df.empty:
        print("\nJadwal kosong, tidak ada yang bisa dihapus."); return df
    print("\n--- 🗑️ Daftar Reservasi Saat Ini ---"); print(tabulate(df, headers='keys', tablefmt='grid', showindex=True))
    try:
        index_hapus = int(input("\nMasukkan nomor baris (index) yang ingin dihapus: "))
        if index_hapus in df.index:
            df = df.drop(index_hapus).reset_index(drop=True)
            print("✅ Reservasi berhasil dihapus!")
        else:
            print("❌ Index tidak valid.")
    except ValueError: print("❌ Input tidak valid.")
    return df

def main():
    nama_file = 'reservasi_ruangan.xlsx'
    df_jadwal = muat_data(nama_file)
    while True:
        print("\n===== 🏛️ SISTEM RESERVASI RUANGAN =====")
        print("1. Tampilkan Semua Reservasi")
        print("2. Buat Reservasi Baru")
        print("3. Edit Reservasi")
        print("4. Hapus Reservasi")
        print("5. Simpan dan Keluar")
        print("========================================")
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1': tampilkan_jadwal(df_jadwal)
        elif pilihan == '2': df_jadwal = tambah_reservasi(df_jadwal)
        elif pilihan == '3': df_jadwal = edit_reservasi(df_jadwal)
        elif pilihan == '4': df_jadwal = hapus_reservasi(df_jadwal)
        elif pilihan == '5':
            df_jadwal.to_excel(nama_file, index=False)
            print(f"\n💾 Perubahan telah disimpan ke '{nama_file}'. Sampai jumpa!")
            break
        else: print("\n❌ Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()