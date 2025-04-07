l = [4,3,6,22,1,8,1,1]
# print(l)

# l.append(1)
# print(l)

# l.sort()
# print(l)

# l.sort(reverse = True)
# print(l)

# l.reverse()
# print(l)

# print(l.index(22))#gives index of first index

# print(l.count(1))#tells you how many times it occurs
# print(l)

'''don't do it , it is pass by reference it change the original list as well,
      instead use copy funtion'''
# m = l
# m[0] = 0
# print(l)

# m = l.copy()
# m[0] = 0
# print(l)
# print(m)

# l.insert(1,42)#to insert at index use insert function first index and then the value.
# print(l)

m = [100,433,577,876]
l.extend(m)#add m at the end of l
print(l)
print(m)

'''for concatinat two lists'''
k = l + m
print(k) 