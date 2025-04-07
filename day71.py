x  = [1,2,3]
# print(dir(x))
# x.__add__
# x.reverse()
# print(x)

'''dic attribute'''

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = person("sparsh",19)
# print(p.__dict__)

'''and help function is used to make documentation for an object ,including a description of its attributes and methods.'''
print(help(x))