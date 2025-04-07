'''Python decorators are a powerful and versatle tool that allows you
    to modify the behaviour of the function and methods .They 
    are a way to extend the functionality of a function or method modifuing 
    its source code.'''

'''A decorator is a functoin that takes another function as an argument and 
    returns a new function that modifiies the behaviour of the original 
    function .The new function is often referred to as a "decorated" 
    function. The basic syntax for using a decorator is the following:- '''

'''@decorator_function
   def my_function():
        pass'''

'''it is just a short hand for the:-
                    def my_function():
                        pass
                    my_function = sdecorator_function(my_function)'''
'''they are often used to add functionality to the function and methods ,
    such as logging,memorizing, and access control.'''

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx
    
# @greet
# def hello():
#     print("Hello World!")

# # greet(hello)()
# hello()

'''Practical use case:-
        One common use of decorators is to add logging to a function .For example,
        you could use a dcorators to log the arguments and return
        value of a function each time it is called : '''

import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args = {args},kwargs = {kwargs}")
        result = func(*args,**kwargs)
        logging.info(f"{func.__name__} returns {result}")
        return result
    return decorated

@log_function_call
def my_function(a,b):
    return a+ b

# log_function_call(my_function)(1,2)
print(my_function(1,2))

