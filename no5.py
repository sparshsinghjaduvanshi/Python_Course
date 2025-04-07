r = int(input("Enter the number of rows : "))
sp = r-1

for i in range(1,r+1):
    for j in range(0,sp):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    sp = sp - 1
    print("")
    
for i in range(1,r+1):
    for j in range(0,sp):
        print("*",end="")
    for k in range(1,2*i):
        print(" ",end="")
    sp = sp - 1
    print("")
