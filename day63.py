import random

def check(comp,user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1):
        return -1
    if (comp == 1 and user == 2):
        return -1
    if (comp == 2 and user == 0):
        return -1

    return 1

comp = random.randint(0,2)
user = int(input("0 for 'Snake' , 1 for 'Water' ,2 for 'Gun' :-\n "))

print("computer : ",comp)
print("user     : ",user)

if (check(comp,user) == 0):
    print("DRAW.")    
if(check(comp,user) == 1):
    print("WIN.")
if(check(comp,user) == -1):
    print("LOSE.")