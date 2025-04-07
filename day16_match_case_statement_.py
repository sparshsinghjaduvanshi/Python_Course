x = 4

match x:

    case 0:# if x is zero
        print("x is zero")

    case 8 if 4 % 2 == 0 : #case with if-condition
        print(" x % 2 is zero")

    case _ if x < 10: #empty case with fi_condition
        print(" x is less than 10") 

    case _ if x >= 10: #dafault case
        print(x)         

#CALCULATOR USING MATCH CASE:- 
# a = int(input("ENTER THE FIRST NUMBER : ")) 
# b = int(input("ENTER THE SECOND NUMBER : ")) 

# x = input("ENTER THE OPERATOR : ")

# match x:
#     case '+': 
#         print(a+b)
#     case '-': 
#         print(a-b)
#     case '*': 
#         print(a*b)
#     case '/': 
#         print(a/b)

# a = int(input("Enter you age : "))

# match a:
    
#     case 22 if(a>10):
#         print("Old")
#     case _ :
#         print("the default answer.")