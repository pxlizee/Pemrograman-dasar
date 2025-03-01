def main():

    x = input("Masukkan nilai untuk x: ")
    y = input("Masukkan nilai untuk y: ")

  
    bool_x = bool(x)
    bool_y = bool(y)

   
    print(f"Nilai x dalam boolean: {bool_x}")
    print(f"Nilai y dalam boolean: {bool_y}")

    print(f"x AND y: {bool_x and bool_y}")
    print(f"x OR y: {bool_x or bool_y}")
    print(f"NOT x: {not bool_x}")
    print(f"x XOR y: {bool_x != bool_y}") 

if __name__ == "__main__":
    main()