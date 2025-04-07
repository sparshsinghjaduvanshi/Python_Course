# for i in range(12):
#     if(i == 10):
#         print("skip the iteration")
#         continue
#     print("5 X",i+1,"=",5*(i+1))

# for i in range(12):
#     if(i == 10):
#         print("skip the iteration")
#         break
#     print("5 X",i+1,"=",5*(i+1))

i = 55   #emulating the do-while loop
# while True:
#     print(i)
#     i = i+1
#     if(i%10 == 0):
#         break#it will not stop untill the break works because there is no false statement in the loop itself,and true is always true.

count = 5
while(count > 0):
    print(count)
    count = count - 1
    if(count < 2 ):
        break
else:
    print("I am inside else")