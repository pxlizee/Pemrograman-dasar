nilai1_ipa = int(input ("Nilai ipa : "))
nilai1_ips = int(input ("Nilai ips : "))
nilai1_mtk = int(input ("Nilai mtk : "))
nilai1_eng = int(input ("Nilai inggris : "))
nilai1_ind = int(input ("Nilai indonesia : "))

list_nilai = (nilai1_mtk, nilai1_eng, nilai1_ind, nilai1_ipa, nilai1_ips)

jumlah_nilai = nilai1_ipa + nilai1_ips + nilai1_mtk + nilai1_eng + nilai1_ind
rata_rata = jumlah_nilai / 5

list_nilai_under50 = 0
if nilai1_eng <= 50 :
    list_nilai_under50 += 1
if nilai1_ind <= 50 :
    list_nilai_under50 += 1
if nilai1_ipa <= 50 :
    list_nilai_under50 += 1
if nilai1_ips <= 50 :
    list_nilai_under50 += 1
if nilai1_mtk <= 50 :
    list_nilai_under50 += 1
    
list_nilai_sempurna = 0
if nilai1_eng == 100 :
    list_nilai_sempurna += 1
if nilai1_ind == 100 :
    list_nilai_sempurna =+ 1
if nilai1_ipa == 100 :
    list_nilai_sempurna =+ 1
if nilai1_ips == 100 :
    list_nilai_sempurna =+ 1
if nilai1_mtk == 100 :
    list_nilai_sempurna =+ 1
    
    
Kelulusan = 
    




    
    