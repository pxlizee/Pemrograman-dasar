nilai_mtk = int(input("Masukkan Nilai MTK :"))
nilai_ipa = int(input("Masukkan Nilai IPA :"))
nilai_ing = int(input("Masukkan Nilai inggris :"))

rata_rata = (nilai_mtk + nilai_ipa + nilai_ing) / 3

nilai = (nilai_ing, nilai_mtk, nilai_ipa)

print(f"nilai rata rata seorang siswa dari 3 mata pelajaran adalah {rata_rata}")

nilai_dibawah_70 = 