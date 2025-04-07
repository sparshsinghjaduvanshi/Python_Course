'''the walrus operator is a new addition to the python 3.8
    and allows you to assign a valu to a varible wihtinan expression.
    this can be useful when you need to use a value multiple times in a loop, 
    but don't ant to repeat the calculation.
    
    this represented by := syntax 
    
    numbers = [1,2,3,4,5]
    while(n := len(numbers)) > 0: 
        print(numbers.pop())
'''
#printing false
# a = True
# a = False
# print(a)

# by walrus
# a = True
# print(a:=False)

# numbers = [1,2,3,4,5]
# while(n := len(numbers)) > 0: 
#     print(numbers.pop())

#EXAMPLE:-
# foods = list()
# while True:
#     food = input("what food you like : ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("what food you like : ")) != "quit":
    foods.append(food)


