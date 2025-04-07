#OPERATOR OVERLOADING
'''OPERATOR OVERLOADING is a feature in python that allows developers
to redefine the behaviour of mathematical and comparison operator
for custom data types.This means that you can use the standard mathematical 
operators(+,-,*,/,etc.) and comparison operators (>,<,==,etc.) in yur own classes,
just as you would for built-in data types like int,float,ad str.'''

'''we need this because it allows you to create more readable and intuitive code.For instance
    ,consider a custom class that represents a point in 2D space.You could define a method called 'add' 
    to add two points together,but using the + operator makes the code more concise and readable : '''

class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
          return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
    
v1 = vector(2,2,2)
print(v1)

v2 = vector(1,1,1)
print(v2)

print(v1 + v2)#it itself found the__add__ method because we use __add__ and then type as v1 + v2 use + operator.

