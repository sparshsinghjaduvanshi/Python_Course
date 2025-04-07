'''In python ,is and == are both comparison operators that 
    can be used to check if two calues are equal. However,
    there are some important difference between the two that you should 
    be aware of.'''

'''This 'is' operator compares the identity of two objects, while
    the '==' operator compares the values of the objects. This 
    means that is will only return True if the objects being
    compared ae the eact same objects in memory ,while'==' 
    when return True if the objects have the same value.'''

# a = [1,2,3]
# b = [1,2,3]

# print(a is b)
# print(a == b)

a = 5
b = 5
print(a is b)
print(a == b)

'''if both the variables have the same data and alo are immutable then only 
    both the conditions are said to be True.'''