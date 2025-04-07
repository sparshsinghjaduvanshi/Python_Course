marks = [1,2,"Harry",True]
# print(marks)
# print(type(marks))
# # print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])

# '''list is changable'''
# marks[0] = "sparsh"
# print(marks)

# if "Harry" in marks:
#     print("yes")
# else:
#     print("no")


'''same thing applied for strings as well'''
# if "PA" in "SPARSH":
#     print("yes")
# else:
#     print("no")

print(marks)
print(marks[1:-1])
print(marks[1:4])
print(marks[:])
print(marks[1:4:2])

lst = [i*i for i in range(10)]
print(lst)

lst1 = [i*i for i in range(10) if i%2 == 0]
print(lst1)

