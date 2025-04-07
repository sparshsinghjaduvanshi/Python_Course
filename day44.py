#how import works?
'''importing in python is the process of loding code from sys import modules
from a python module into the current script.
This allows you to use the functions and variables defined in the module in your current script as well  as any additional modules
that the imported module may depend on '''

# from math import sqrt,pi

# result = sqrt(9) * pi
# print(result)

# from math import sqrt as s

# result = s(9) 
# print(result)

'''if we don't know the function the import we can use 
'dir' function '''
# import math
# print(dir(math))

# from sparsh import welcome,sparsh
# print(sparsh)
# welcome()

'''to import everything from the imported file we can use '*' function '''
from sparsh import *
welcome()
print(sparsh)