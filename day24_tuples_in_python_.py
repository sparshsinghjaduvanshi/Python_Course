'''Tuples are ordered collection of data items. They store multiple items in a single variable.
   Tuple items are seperated by commas and enclosed within round brackets ().
   Tuples are unchangeble meaning we can not alter them after creation.'''

tup1 = (1,)
# print(type(tup1),tup1)

tup = (92,3,5,6,1,'string')
print(type(tup),tup)


tup3 = tup[1:4]#it does not make change in the real one instead it makes the new tuple
print(tup)
print(tup3)

print(tup[1:6:2])