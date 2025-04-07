#MULTIPLE INHERITANCE

'''it is a powerful feature in oop that allows a class to inherit attributes and methods from multiple parent 
classes .This can be useful in situations where a class needs to inherit
functionality from multiple sources.'''

'''syntax:-
        class chldclass(paentclass1,parentclass2,parentclass3):
            #class body
'''

class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class dancer:
    def __init__(self):
        self.dance = dancer
    def show(self):
        print(f"The dance is {self.dance}")

class danceremployee(employee,dancer):
    def __init__(self,name,dance):
        self.dance = dance
        self.name = name

o = danceremployee("Shivani","kathak")
print(o.name)
print(o.dance)
o.show()

'''in the programme both dancer and employee class have the show method but 
    firstly print will be from the class which is witten fist in the child class(danceremployee)
    example, in the above code employee class is written on first. '''
print(danceremployee.mro())#this shows the path which the compiler folows 
                           #by which it follows and serach for the lines or methods.