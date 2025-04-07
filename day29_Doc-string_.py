'''Docstrings in python are the string literals that appear right after ,
   the defination of a function ,method ,class, or module.'''

def square(n):
    '''takes in a number n, 
                returns the square of n'''
    print(n**2)

square(5)
print(square.__doc__)

'''PYTHON COMMENTS:
    comments are descriptions that help programmers better understand the intent and functionality of the programe.
        they are completely ignored by the python interpreter.'''

'''PYTHON DOCSTRINGS:
    As mentioned above.python docstrings are strings used right after definition of a function,method,class, module.
        they are used to document our code.
            we can acccess these docstrings using the doc attribute.'''

