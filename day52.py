'''In python, a Lambda function is a small anonymous function without a name.
it is defined using the lembda keyword and has the following syntax:'''

'''lambda argument : expression'''
''' Lambda functions arte often used in situations where a small function
    is required for a short period of time. They are commonly used as 
    arguments to higher-order functins, such as map, filter, and reduce.'''

# def double(x):
    # return x*2

# double = lambda x:x*2
# avg = lambda x,y: (x+y)/2

# print(double(5))
# print(avg(2,2))

'''we can also pass it as a function to a another function:-'''

def appl(fx,value):
    return 6+fx(value)
double = lambda x:x*2

# print(appl(double,2))
print(appl(lambda x: x*2,2))