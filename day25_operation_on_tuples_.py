'''because we cannot make any direct changes in the tuple ,
   we use substitue to make it a list first then we make the changes ,
   and then we overwrite the tuple by list.'''
countries = ("spain","italy","india","england","germany")
# print(type(countries))
# print(countries)


temp = list(countries)
# print(temp)

# temp.append("russia")  #add item
# print(temp)
# print(countries)
# print(type(temp),type(countries))


# temp.pop(3)            #remove item
# print(type(temp),type(countries))
# print(temp)

# temp[2] = "finland"    #chande item

# countries = tuple(temp)
# print(countries)

# print(type(temp),type(countries))

'''concatination'''
# countries = ("pakistan","afghanistan","bangladesh","shrilanka")
# countries2 = ("veitnam","indian","china")

# southeastasia = countries + countries2
# print(southeastasia)

tup = (1,2,3,4,4,5,5,5,6,)

res = tup.count(5)
print("the occurence of 5 in the tuple is : ",res)

print(tup.index(5))
print(tup.index(5,1,7))#shows the index of 5 between index 1 to 7
print(len(tup))