'''in OOP the term constructor refers to a special type of method that is automatically executed when an 
    object is created from a class. The purpose of a constructor is to initialize
    the object attribute allowing the object to be fully functional and ready to use.'''

# class employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

# e1 = employee("harry",12000)
# print(e1.name)
# print(e1.salary)

# string = "Harry-12000"
# e2 = employee(string.split("-")[0] , string.split("-")[1])
# print(e2.name)
# print(e2.salary)

#METHOD TWO TO DO THE SAME THING BUT WITH CLASS:-

# class employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def fromstr(cls,string):
#         return cls(string.split("-")[0] , string.split("-")[1])

# e1 = employee("harry",12000)
# print(e1.name)
# print(e1.salary)

# string = "Harry-12000"
# e2 = employee.fromstr(string)
# print(e2.name)
# print(e2.salary)

#another example:-
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,string):
        name,age = string.split(',')
        return cls(name,int(age))

person = person.from_string("sparsh,19")