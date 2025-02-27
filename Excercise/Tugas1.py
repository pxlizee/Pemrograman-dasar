a = int(input("Masukkan bilangan bulat untuk a :"))
b = int(input("Masukkan bilangan bulat untuk b :"))
c = int(input("Masukkan bilangan bulat untuk c :"))

print(a, b, c)

if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c) :
    print("Kondisi terpenuhi")
else :
    print("Kondisi tidak terpenuhi") 
