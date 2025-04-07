'''In default argument : 
   if the value is already provided in the function call ,
   then the function will consider that value doesn't matter if the value is provided in the default function or not,
   if the value is not provided in the function then it will consider the value provided in the function.'''

# def default(a = 2, b = 4):
#     print("average",(a+b)/2)

# default(2,2)

''''In Keyword argument:
    while calling the function irrespective of the sequence by assigning the value in the function call ,
    we can tell the function to what value it has to consider for which parameter. '''

# default(b = 2, a = 6)

'''In Required argument :
    if don't pass the keyword of default argument then it is neccessory to give value in sequencial order.'''

# default(2,2)

'''In Variable Length argument :
    sometimes we may need to pass more argument than those defined in the actual function .
    this can be done using variable length arguments.
    
    there are two ways to achieve tis :
    1.. Arbetary Arguments:
                            while creatung a function pass a '*' before the parameter name while defining the function .
    The function access the argument by prcessing them in the for of tuple.'''

# def average(*number):
#     print(type(number))
#     sum = 0 
#     for i in number:#accessing the element  in the tuple 'number'.
#         sum = sum + i 
#     # print("average is : ", sum/(len(number)))
#     return sum

# c = average(5,6,1)#it makes a kind of list and then proceed.
# print(c)

'''2..Keyword Arbitary Arguments:
                                while creating a function pass a '**' before the parameter name while defining. The function accesses
                                the argument by processing them in the form of dictionary.'''

def name(**name):
    print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"])

name(mname="Buchanan",fname="Barnes",lname="James")