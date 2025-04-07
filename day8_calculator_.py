# a = 50
# b = 3

# print("the value of ",a , " + ", 3, "is : ", a+b )
# print("the value of ",a , " - ", 3, "is : ", a-b )
# print("the value of ",a , " * ", 3, "is : ", a*b )
# print("the value of ",a , " / ", 3, "is : ", a/b )

#MAKING CALCULATOR :-
i = int(input("ENTER THE FIRST NUMBER YOU WANT TO CALCULATE : "))
s = int(input("ENTER THE SECOND NUMBER YOU WANT TO CALCULATE : "))

c = (input("ENTER THE OPERATION YOU WANT TO PERFORM FROM ('+','-','*','/') : "  ))

if(c == '+'):
    print("the value of ",i , " + ", s, "is : ", i+s )
elif(c == '-'):
    print("the value of ",i , " - ", s, "is : ", i-s )
elif(c == '*'):
    print("the value of ",i , " * ", s, "is : ", i*s )
else:
    print("the value of ",i , " / ", s, "is : ", i/s )