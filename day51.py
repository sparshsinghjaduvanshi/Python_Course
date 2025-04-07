'''In python, the seek() and tell() functions are used to work 
    with file objects and their positions within a file. These
    functions are part of the built-in io module, which provides
    a consistent interface , such as files, pipes , and in- memory buffers. '''

'''the seel() function allows you to move the current position 
    within a file to a specific point. The position is specified in 
    bytes, and you can move either forward or vackward from the current position.
For example:-'''
with open("file1.txt",'r') as f:
    print(type(f))
    f.seek(5)#seek move to the fifth element of the data.

    data = f.read(5)#read after the pointer is moved
    print(data)

'''The tell() function return the current position within the file,
    in bytes. This can be useful for leping track of your
    location within the file or for seeking to a specific position
    relative to the current position. 
    For example:-'''

with open('file1.txt','r') as f:
    f.seek(10)
    current_position = f.tell()
    print(current_position)


'''when you open a file in python usin the oipen function, you
    can specify the mode in which you want to open the file. If
    you specify the mode as 'w' or 'a' , the file is opened in write
    mode and you can write to the file .However, if you want to truncate the file 
    to a specific size , you can use the truncate() function.'''

f = open('file1.txt', 'w')
f.write("Hello World!")
f.truncate(5)

f.close()