nilai_mtk = int(input("Masukkan Nilai MTK :"))
nilai_ipa = int(input("Masukkan Nilai IPA :"))
nilai_ing = int(input("Masukkan Nilai inggris :"))

rata_rata = (nilai_mtk + nilai_ipa + nilai_ing) / 3

nilai = (nilai_ing, nilai_mtk, nilai_ipa)

print(f"nilai rata rata seorang siswa dari 3 mata pelajaran adalah {rata_rata}")

nilai_dibawah_70 = 1
if(nilai_ipa) :
    nilai_dibawah_70 += 1
if(nilai_ing) :
    nilai_dibawah_70 += 1
if(nilai_mtk) :
    nilai_dibawah_70 += 1
    
if (rata_rata > 75) :
    print("Siswa ini lulus, karena nilai rata rata nya di atas 75")
elif (nilai.count(100) >= 1) :
    print("Siswa ini lulus, karena ada nilai yang mencapai 100")
elif (nilai_dibawah_70 == 1) :
    print("siswa ini lulus, karena nilai di bawah 70 hanya 1")

else :
    print("tidak lulus, tidak memenuhi syarat")