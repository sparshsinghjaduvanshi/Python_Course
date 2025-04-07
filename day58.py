'''A constructoe is a special method in a class used to create and initialize an object
    of a class . There are different types of constructors. Constructor is invokd automatically when an object
    of a class is created.'''

'''A constructor is a unique function that gets called automatically when
    an object is created of a class. The main purpose of 
    a contructor is to initialize or assign values to the data members of theat class.
    It cannot return any value other than None.'''

'''Syntax:-
            def __init__(self):
                #initializations'''

class person:
    def __init__(self,name,occupation):
        self.name = name
        self.occuption = occupation

    def info(self):
        print(f"{self.name} is a {self.occuption}")

a = person("Harry","Software Developer")
b = person("Sparsh","HR")
a.info()
b.info()

'''Types of constructor:- 
        1.. Parameterized constructor
        2.. Default constructor'''

'''Parameterized:-
            when the constructor accepts arguments along with self ,it is known
            as parameterized constructors.
            
            these arguments can be used inside the class to assin the valus to the data members.'''

'''Default:-
            when the constructor does't acept any arguments from the object
            and has only one argument, self ,in the constructor ,it is known as a Default consructor. '''

class person:
    def __init__(self):
        print("I study in curaj in rajasthan.")
a = person()        