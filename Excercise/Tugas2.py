def cek_tipe_input():
    input1 = input("Masukkan input (string) : ")
    input2 = input("Masukkan input (integer) : ")
    input3 = input("Masukkan input (float) : ")


    is_string = isinstance(input1, str)
    is_integer = False
    is_float = False

    try:
        int_input2 = int(input2)
        is_integer = True
    except ValueError:
        is_integer = False


    try:
        float_input3 = float(input3)
        is_float = True
    except ValueError:
        is_float = False

    if is_string and is_integer and is_float:
        return "Tipe input valid"
    else:
        return "Tipe input tidak valid"


hasil = cek_tipe_input()
print(hasil)