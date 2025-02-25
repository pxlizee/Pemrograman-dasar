ipa = int(input("Masukkan nilai IPA :"))
ips = int(input("Masukkan nilai IPS :"))
mtk = int(input("Masukkan nilai MTK :"))
english = int(input("Masukkan nilai English :"))
indonesia = int(input("Masukkan nilai Indonesia :"))

rata_rata_1 = (ipa + ips + mtk + english + indonesia) / 5

nilai = (ipa, ips, mtk, english, indonesia)

print(f"Rata-rata nilai seorang siswa dari 5 mata pelajaran adalah {rata_rata_1}")

nilai_di_bawah_50 = 2 
if(ipa < 50):
    nilai_di_bawah_50 += 1
if(ips < 50):
    nilai_di_bawah_50 += 1
if(mtk < 50):
    nilai_di_bawah_50 += 1
if(english < 50):
    nilai_di_bawah_50 += 1
if(indonesia < 50):
    nilai_di_bawah_50 += 1


if (rata_rata_1 > 75):
    print("Lulus, karena rata - rata nilai lebih dari 75")
elif (nilai.count(100) >= 1):
    print("Lulus, karena mendapatkan nilai sempurna dari salah satu mata pelajaran")
elif (nilai_di_bawah_50 == 2 ):
    print("lulus, karena hanya 2 mata pelajaran yang nilai nya di bawah 50")
else:
    print("Tidak lulus, karena tidak memenuhi syarat")
