#QUESTION 1.
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# if(a > b):
#     print(a," is greater than ",b)
# else:
#     print(b," is greater than ",a)    

#QUESTION 2.
# num = int(input("Enter the number : "))
# factorial = 1
# for i in range(1,num+1):
#     factorial *= i
# print("the factorial of the number :",num," is ",factorial)

#QUESTION 3.
# string = str(input("Enter the string : "))
# j = -1
# x = 0
# for i in string:
#     if(i != string[j]):
#         x = 1
#         break
#     j = j-1
# if(x == 0):
#     print("The string is palindrome.") 
# else:
#     print("The string is not palindrome.") 

#QUESTION 4.

string = str(input("Enter the string : "))
length = len(string)
k = 0

if(length%2 == 0):
    l1 = int(length//2)
    for i in string:
        if i != string[l1]:
            k = 1
            break
    l1 = l1 + 1
else:
    print("The input string is not symmetrical")

if( k == 0):
    print("The input string is symmetrical")
else:
    print("The input string is not symmetrical")


#QUESTION 5.
#QUESTION 6.
#QUESTION 7.
#QUESTION 8.
#QUESTION 9.
#QUESTION 10.

