nama = "Ikbal"
total = len(nama)


for i in range(total-1,-1,-1):
    print(" " .join(nama[:i+1] + "*" *(total-1-i)))