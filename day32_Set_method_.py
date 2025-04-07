'''In sets order does not matter.'''
s1 = {1,4,8,6,7}
s2 = {2,3,4,5}
s3 = {1,4,7}
# print(s1.union(s2))#it won't make any changes in the original set
print(s1, s2, s3)

# s1.update(s2)# it changes the original initially set
# print(s1)

print(s1.intersection(s2))#it won't make any changes in the original set
s1.intersection_update(s2)
print(s1,s2)

# print(s1.symmetric_difference(s2))  #A union B minus A intersection B
#things that are not common in both sets.
# s1.symmetric_difference_update(s2)
# print(s1, s2)

# print(s1.difference(s2))#which are present in s1 not in s2.
# s1.difference_update(s2)
# print(s1, s2)

'''sets methods'''
'''1..isdisjoint():
        The isdishoint() method checks if items of given set are present in another set.
            This method returns False if items are present ,else it reurns True.'''

# print(s1.isdisjoint(s2))
'''2..issuperset:
        the issuperset() method checks if all the items of a particular set are present in the original set . 
            It returns True if all the items are present ,
                else it returns False. '''
# print(s1.issuperset(s2))

# print(s3.issubset(s1))#s3 is a subset of s1.

# s1.add(9)
# print(s1) #to add in the set.
# s1.remove(4) #to remove the item from the set.use remove() or discard()
# print(s1)#  remove raise error discard not. 

# item = s1.pop()  #to remove an item on random.

# print(item)
# print(s1)

''' "del" is not a method ,rather it is a keyword which deletes the set entirely. '''
# del s1

''' "clear" method clears all items in the set and prints an empty set. '''
# s1.clear()
# print(s1)

if 4 in s1:
    print("it is present.")
else:
    print("not present.")