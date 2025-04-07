'''The finally code  block is also a part of excepton handling .
    when we handle exception using the try and except block,
    we can include a finally block ar the end.  The finally block is always executed ,
    so it is generally used for doing the concludin tasks like closing file resources or closing
    database connection or may be ending the proframe 
    execution with a delightful message. '''

def func():
    try:
        l = [1,5,6,7]
        i = int(input("enter the index : "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("I am always executed.")

x = func()
print(x)
