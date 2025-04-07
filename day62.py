'''Access Specifiers/Modifiers:- 
            access specifiers or access modifiers in pythonprogeamming are 
            used to limit the access of class cariables and class methods outside of the class while
            implementing the concept of inheritance.'''

'''Types:- '''

'''1. Public ccess modifiers:-
                all the varibles and methods (member functions) in python are by default
                public. Any instance varibles in a class followed by the 'self' keyword ie.
                self.car_name are public accessed.'''

# class student:
#         def __init__(self,name):
#                 self.name = name 

# a = student("sparsh")
# print(a.name)

'''2. Private access modifiers:-
                By definition, private members of a class (variables or methods) are those
                members which are only accessible inside the class. We cannot use 
                private memberrs outside of class.
                
                In Python , there is no strict conccept of "private" access modifiers
                like in some other programming languages.However a convention has been
                established to indicate that a varible or method should be considered
                private by prefixing its name with a doble underscore (__) .This is known as
                a "weak internal use indicator" and it is a convention only ,
                not a strict rule.Code outside the class can still access ther "private" 
                varibles and methods , but it is generally understood that they should not be 
                accessed or modified.'''
# class student:
#         def __init__(self,name):
#                 self.__name = name 

# a = student("sparsh")
# # print(a.__name)#cannot access directly
# print(a._student__name)# called name mangling
# print(a.__dir__()) # shows what actiond we can perform on this class.
'''Name Mangling :-
                NAME MANGKING IN PYTHON IS A TECHNOQUE USED TO PROTECT CLASS-PRIVATE AND 
                SUPERCLASS-PRIVATE ATTRIBUTE from being accidentally overwritten by 
                subclass. Names of class-private and superclass-private attrubutes are
                transformed by the addition of a single leading underscore and a double 
                leading inderscore respectively.'''


'''3. Protected access modifiers:- 
            In OOP the term "protected" is used to describe a member of a class that is intended 
            to be accessed only by the class itself and its subclass.In python the convention
            for indecating that a member is protected is to prefix its name with a single 
            underscore(_) .For example, if a class has a method called _my_method, it is indicating that the 
            method should only be accessed by the class itself and its subclasses.
            
            it's important to note that the single underscore is just a nameing convention, and 
            does not actually provide any protection or 
            restrict access to the member .The syntax we follow to make any
            varible protected is to write varible name followed by a single
            underscore(_) ie. _varName'''

class student:
        def __init__(self):
               self._name =  "Harry"

        def _funtime(self): # protected method
               return "Code With Harry!"

class subject(student): # inhereted class
        pass

a = student()
a1 = subject()
print
print(a._name)
print(a._funtime())

print(a1._funtime())
print(a1._name)
