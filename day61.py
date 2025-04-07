'''Inheritance in Python:-
            When a class derives from another class. The child will inherit all the
            public and protected properites and methods from the parent class. In
            addition, it can have its own properties and methods ,this is called as inheritance.'''

'''class BaseClass:
        body of class
   class DerivedClass(BasClass):
        body of derived class
'''
'''derived class inherit features from the base class where new features can 
    be added to it. The results in re-usability of code.'''

'''Type of inheritance:-
        1. single inheritance
        2. multiple inheritance
        3. multilevel inheritance
        4. hierarchical inheritance
        5. hybrid inheritance'''

# class employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def showdata(self):
#         print(f"the name of employee : {self.id} is {self.name}")

# e1 = employee("Sparsh", 1111)
# e2 = employee("Shiva", 0000)

# e1.showdata()
# e2.showdata()


'''with the method of inheritance:- '''
class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showdata(self):
        print(f"the name of employee : {self.id} is {self.name}")
#making a new child class and giving all attribute of the previous class
        #by passing the parent class as an argument :-
class programmer(employee):
    def showlanguage(self):
        print("The default language is python.")
    

e1 = employee("Sparsh", 1111)
e2 = programmer("Shiva", 0000)

e1.showdata()
e2.showdata()
e2.showlanguage()
