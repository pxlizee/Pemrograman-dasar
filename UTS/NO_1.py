printer = int(input("Masukkan harga :"))
masa_manfaat = int(input("Berapa Tahun Masa Manfaatnya? :"))
sisa = int(input("Masukkan Perkiraan Nilai Sisa: "))

susut_tahun = printer - sisa
susut_tahun1 = susut_tahun / masa_manfaat
susut_tahun2 = susut_tahun1 * 2 
nilai_aset_sisa = printer - susut_tahun2

print (nilai_aset_sisa)
