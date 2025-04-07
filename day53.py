'''In python, the map,filter,and reduce function are built-in functions the allow
    you to applya function to a sequence of elements and return a new sequence.
    these functions are lnown as higher -order functins ,as they take other
    functions as arguments.'''

'''MAP:-
        the map functin applies a functio to each element in a sequence and returns
         a new sequence containing the transformed elements. The map function has 
         the following syntax:'''

'''map(function,iterable)'''

'''The function argument is a functin that is applied to each element in the
    iterable argument.The iterable arguments can be a list, tuple, or any other 
     iterable object. '''

# def cube(x):
    # return x*x*x
# print(cube(2))

# l = [2,4,5,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))

# print(newl)#there is another way to do this with the help of map function

# newl = list(map(cube,l))
# print(newl)

'''the filter function filter a sequence of elements based on a given
    predicate {a function that returns a boolead value} and returns a new swquence containing 
     only the element that meet the predicate. The filter function had the following
      syntax: '''
'''filter(predicate,iterable)'''

'''the predicate argument is a functin that returns a boolean value and is applied 
    to each element in the iterable argument.The iterable argument can be a list,
    tuple,or any other iterable object.'''


# def filter_function(a):
    # return a>3 and a < 6

# newl = list(filter(filter_function,l))
# print(newl)

'''the reduce function is a higher-order function that applies a function
    to a sequence and returns a single value .It is a part of the functools
    module in python and has the following syntax:-'''

'''reduce(function,iterable)'''

'''the function argument is a function that takes in two arguments and returns a 
    single value.The iterable argument is a sequence of elements, such as a list or tuple.'''

'''the reduce function applies the function to the first two elements 
    in the iterable and then applies the function to the result and the next element , and so on.
    The reduce function returns the final result.'''

from functools import reduce
from tkinter import Y
l = [2,4,5,6,4,3]

# def mysum(x,y):
#     return x+y

# sum = reduce(mysum,l)
sum = reduce(lambda x,y:x+y,l)
print(sum)