import pandas as pd

# ----------------------------------------------------------------------
# GANTI FUNGSI updateScore LAMA ANDA DENGAN FUNGSI DI BAWAH INI
# ----------------------------------------------------------------------
def updateScore(score): # Nama fungsi dan parameter sama dengan kode Anda
    BATAS_WAJAR_ATAS = 80

    skor_baru = score # Inisialisasi skor_baru dengan skor awal

    if score < BATAS_WAJAR_ATAS:
        # Skor di bawah "batas wajar", perlu ditambahkan.
        # Tujuannya: skor sangat rendah (misal 15) naik ke 60/70-an (Grade D/C).
        # Skor lain di bawah 80 juga dinaikkan.
        # Hasil akhir penambahan tidak boleh melebihi BATAS_WAJAR_ATAS (80).

        kandidat_skor_baru = 0
        if score < 30:  # Untuk skor sangat rendah (misalnya 0-29)
            # Ditingkatkan signifikan ke level Grade C
            # Contoh: skor 15 akan menjadi 68
            kandidat_skor_baru = 68
        elif score < 50:  # Untuk skor rendah (misalnya 30-49)
            # Ditingkatkan ke level Grade D tinggi atau C rendah
            # Contoh: skor 35 menjadi 35 + 25 = 60
            # Contoh: skor 49 menjadi 49 + 25 = 74
            kandidat_skor_baru = score + 25
        elif score < 65:  # Untuk skor di rentang Grade D (misalnya 50-64)
            # Ditingkatkan ke level Grade C atau D tinggi
            # Contoh: skor 50 menjadi 50 + 15 = 65
            # Contoh: skor 64 menjadi 64 + 15 = 79
            kandidat_skor_baru = score + 15
        else:  # Untuk skor antara 65 dan 79 (sudah Grade C atau B)
            # Diberikan penambahan yang lebih kecil
            # Contoh: skor 65 menjadi 65 + 10 = 75
            # Contoh: skor 79 menjadi 79 + 10 = 89 (akan dibatasi oleh BATAS_WAJAR_ATAS)
            kandidat_skor_baru = score + 10

        # Terapkan batasan: "tapi jangan lebih dari batas wajar"
        skor_baru = min(kandidat_skor_baru, BATAS_WAJAR_ATAS)

    else:  # score >= BATAS_WAJAR_ATAS (misalnya 80 atau lebih)
        # Skor sudah masuk "batas wajar".
        # Mengikuti logika dari gambar Anda sebelumnya (jika score >= 80: return score + 5).
        # Jika Anda ingin skor >= 80 tidak diubah, baris ini bisa menjadi: skor_baru = score
        skor_baru = score + 5

    return skor_baru
# ----------------------------------------------------------------------
# AKHIR DARI FUNGSI updateScore YANG BARU
# ----------------------------------------------------------------------

def grade(score): # Fungsi grade Anda tetap sama
    if score >= 85:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    else:
        return "D"

# Bagian skrip Anda yang lain tetap sama
file_path = 'Sesi_13/score.xlsx'
try:
    score_df = pd.read_excel(file_path) # Mengganti nama variabel 'score' menjadi 'score_df' agar tidak bentrok dengan parameter fungsi

    # Pastikan file Excel Anda memiliki kolom bernama 'Score' yang berisi nilai awal
    # Jika nama kolomnya berbeda, sesuaikan 'Score' di bawah ini
    if 'Score' in score_df.columns:
        score_df['New Score'] = score_df['Score'].apply(updateScore)
        score_df['Grade'] = score_df['New Score'].apply(grade)
        
        output_file_path = 'Sesi_13/updated_score.xlsx'
        score_df.to_excel(output_file_path, index=False)
        print(f"File '{output_file_path}' berhasil disimpan dengan skor yang telah diperbarui.")
    else:
        print(f"Error: Kolom 'Score' tidak ditemukan di file '{file_path}'.")
        print(f"Kolom yang tersedia adalah: {score_df.columns.tolist()}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")