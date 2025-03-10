full_semester = input(str("Apakah biaya semseter sudah full ? (Y/N) : "))
nilai_ujian = input(str("Masukkan Nilai Rata - Rata Ujian : "))

if full_semester == str("Y"):
    full_semester = True
else:
    full_semester = False
if nilai_ujian == str("A") or nilai_ujian == str("B") or nilai_ujian == str("C") :  
    nilai_ujian = True
else:
    nilai_ujian = False
    
if full_semester and nilai_ujian == True:
    print("Selamat Anda Lulus")
else:
    print("Maaf, Anda belum memenuhi syarat")