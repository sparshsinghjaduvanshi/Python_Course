#TIME MODULE
'''THE TIME MODULE IN PYTHON provides a set of function to work with time related
    operation ,such as timekeeping ,formating,and time conversions.This module is part of
    the python standard library and is available in all python installations,making it a convinient 
    and essential tool for wide range of apllication.'''

#time.time()
'''the time.time() function returns the current time as a floating-point
number,representing the number of seconds since the epoch(the point in time when the time module
was initialized). The returned value is based on the computer's system clock and is affected by time
adjustments made by the operating system ,such as daylight saving time.'''

# import time
# # print(time.time())

# def for_while():
#     i = 0
#     while i != 5000:
#         i = i+1
#         print(i)

# def for_for():
#     for i in range (5000):
#         print(i)

# init = time.time()
# for_for()
# t1 = time.time() - init

# init = time.time()
# for_while()
# t2 = time.time() - init
# print(t1)
# print(t2)

import time

# print(4)
# time.sleep(3)#in sec it makes the compiler wait for the given sec. to move futher
# print("Print after 3 seconds.")

'''the time.strtime() function formate a time value as a string based on a
    specified formate.This function is particularly useful for formatting 
    dates and times in a human-readable formate,such as for display in a GUI,
    a log fil,ort a report,'''
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)