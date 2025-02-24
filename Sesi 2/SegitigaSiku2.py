alas = float(input("masukkan panjang alas : "))
tinggi = float(input("masukkan tinggi : "))

luas = 0.5 * alas * tinggi

sisi_miring = (alas**2 + tinggi**2)**0.5

keliling = alas + tinggi + sisi_miring

print("luas segitiga siku siku adalah " , luas)
print("keliling segitiga siku siku adalah: ", keliling)  