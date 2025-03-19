print ("Deret 1 ")

result = 50
add = -2

for i in range (8):
    print(result,end=" ")
    result += add
    add -= 2
    
print("\n")   
print ("Deret 2")

a = 2
b = 3 
for x in range (8):
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    