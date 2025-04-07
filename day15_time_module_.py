import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp1 = int(time.strftime('%H'))
print(timestamp1)

timestamp2 = (time.strftime('%M'))
print(timestamp2)

timestamp3 = (time.strftime('%S'))
print(timestamp3)

# if(timestamp1 < 11):
#     print("Good Morning")
# elif(timestamp1 < 12):
#     print("Good Noon")
# elif(timestamp1 < 18):
#     print("Good Afternoon")
# else:
#     print("Good Evening")

if(timestamp1 >= 0 and timestamp1 < 12):
    print("Good Morning Sir !")
elif(timestamp1 >= 12 and timestamp1 < 16):
    print("Good Afternoon Sir !")
elif(timestamp1 >= 16 or timestamp1 < 20):
    print("Good Evening Sir !")
else:
    print("Good Night Sir !")
