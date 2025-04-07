#DUNDER METHODS

'''__init__method:-
        the init method is a special method that is automatically invoked 
        when you create a new instance of a class. This method is responsible
        for setting up the objects initial state, and it is where you would 
        typically define any instance varibles that you need .Also called
        "constructor" ,we have descussed this method already.'''

'''__str__ and __repr__ methods:-
            this str and repr methods are both used to convert an object to a 
            string representation.The str method is used when you want to
            print out an object, while the repr method is used when you wwant to get a 
            string representation of an obect that can be used to recreate the object.'''

'''__len__method:-
        the len methtod is used to get the length of an object .This is useful
        when you want to be able to find the size of a data structure ,such as 
        list or dictionary.'''

'''the call method is used to make an object callable,meaning that you can
    pass it as a parameter to a function and it will be executed when the function 
    is called. This is an incredibly powerful tool that allows you to create objects that
    behave like functions.
    
    these are just a few of the many magic methods available in python.
    They are incredibly powerful tools that allows you to customize the behaviour of your objects,and 
    can make your code much cleaner and easier to understand.'''

from main import employee

e = employee("Sparsh")
# print(str(e))
# print(repr(e))

# print(e.name)
# print(len(e))
# print(e)
e()