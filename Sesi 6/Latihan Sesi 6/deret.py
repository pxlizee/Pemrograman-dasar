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
    
print("\n")
print ("Deret 3")

result2 = 40
add2 = -1

for y in range (8):
    print(result2,end=" ")
    result2 += add2
    add2 -= 2
    
    
print("\n")
print ("Deret 4")

result3 = 100
add3 = 1

for z in range (8):
    print(result3,end=" ")
    result3 -= add3
    add3 += 2
    

print("\n")
print ("Deret 5")

q = w = e = 1
for o in range (8):
    print(e,end=" ")
    if (o >= 1) :
        e = q + w
        
    q = w
    w = e