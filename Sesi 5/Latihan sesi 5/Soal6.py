input1 = int(input("Masukkan angka ke 1 :"))
operator = input("Masukkan Operator (+,-,*,/) :")
input2 = int(input("Masukkan angka ke 2 :"))

hasil = 0
if operator == "+":
    hasil = input1 + input2
elif operator == "-":
    hasil = input1 - input2
elif operator == "*":
    hasil = input1 * input2
elif operator == "/":
    hasil = input1 / input2
else:
    print('input error')
    
print("hasil dari perhitungan di atas adalah :", hasil)