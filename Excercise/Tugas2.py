input1_string = str(input("Masukkan Input ke 1 (string):"))
input2_integer = int(input("Masukkan Input ke 2 (integer):"))
input3_float = float(input("Masukkan Input ke 3 (float):"))

print(input1_string, input2_integer, input3_float)

if type(input1_string) == str:
    print("Tipe Input valid")
elif type(input2_integer) == int:
    print("Tipe Input valid")
elif type(input3_float) == float:
    print("Tipe Input valid")
else :
    print("Tipe Input tidak valid")