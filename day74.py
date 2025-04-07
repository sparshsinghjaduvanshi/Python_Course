#METHOD OVERRIDING


'''METHOD OVERRINDING IS A POWERFUL FEATURE IN oop that allows
you to redifine a method in a derived class. The method in 
the derived class is said to override the method in the basic class.
When you create an instance of the derived class is executed,
rather that the version in the base class.'''


# class shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y
    
# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
    
# a = shape(5,5)
# print(a.area())

# b = circle(5)
# print(b.area())

class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()
    
    
a = shape(5,5)
print(a.area())

b = circle(5)
print(b.area())

