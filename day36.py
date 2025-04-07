'''exception handling is the process of responding to unwanted or unexpected 
    events when a computer programme runs . Exception handling deals with these 
     events to avoid the programme or system crashing ,and without this process
      exceptions would disput the normal operation of a programme. '''

# a = input("enter the number: ")
# print(f"MUltiplication table of {a} is : ")

# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a) * i}")


a = input("enter the number: ")
print(f"MUltiplication table of {a} is : ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except:
    print("INVALID INPUT .")

print("some lines of code ")
print("end of programme.")