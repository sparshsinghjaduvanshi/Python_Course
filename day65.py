'''Static methods in python are methods that belongs to a class rather 
    than an instace of the class. They are defined using the @staticmethod
    decorattor and do not have access to the instance of the class(i.e. self) .Thy are called on the class itself , not on an 
    instance of the class. Static methods are often used to create utility
    function that don't need acess to instance data.'''

class Math:
   
    def __init__(self,num):
        self.num = num
   
    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a+b

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(a.add(7,2)) # both are possible.
print(Math.add(7,2))