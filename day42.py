marks = [9,8,7,6,5,4,3,2,1]


# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Sparsh, awesome!")
#     index += 1

'''using enumerate function = it is a function that allows you to loop over a sequence (such as loop , tuple, or string)
    and get the index and value of each element in the sequence at the same time'''  
    
for index,mark in enumerate(marks,start = 1):
    print(index,".. ",mark)
    if(index == 3):
        print("Sparsh, awesome!")

# for index,mark in enumerate(marks):
    # print(index,".. ",mark)