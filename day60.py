'''GETTERS :-
        getters in python are methods that are used to access the values
        of an objects properties. They are used to return the cvalue of a specific property
        , and are typically defined usng the @property 
        decorator. Here is an example of a simple clss with a getter method: '''

# class Myclass:
#     def __init__(self,value):
#         self._value = value# (_value) is a private attribute it shows that it is meant to be protected or private,
#                             #but it does not stop's you from accessing it 

#     @property
#     def value(self):
#         return self._value#it also saves from infinite self recursion by choosing a different name.


'''In this example the Myclass has a single property ,value,
    which is initialized in the init method.The value method is defined as a getter 
    using the @property decorator, and is used to return the value of the value property.'''
'''to use the getter ,we can create an instance of the Myclass class,
    and then access the value property as if it were a attribute: '''

# obj = Myclass(10)
# print(obj._value)
# print(obj.value)
'''In Python, the single leading underscore (_value) is a naming convention that signals to developers that it's
    intended to be a private or protected attribute, but it does not prevent you from accessing it directly.
    When you do print(obj._value), you're accessing the actual attribute _value directly, bypassing the @property.
    Drawback: Directly accessing _value is discouraged because it breaks encapsulation. 
    You could unintentionally modify or expose the internal state of the object.'''

'''SETTERS :-
            It is important to note that the getters do not take any 
    parameter and we cannot set the value through getter
    method. For that we need setter nethod which can be added by 
    decorating method with @property_name.setter'''

class Myclass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def original_value(self):
        return self._value

    @property
    def ten_value(self):
        return 10*self._value

    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

a = Myclass(10)
# a._value  = 100
print(a.ten_value)# Outputs: 100 (10 times 10)

a.ten_value = 67#set value to 67
print(a.ten_value)# Outputs: 67.0 (10 times 6.7)
print(a.original_value)# Outputs: 6.7 (the original value)
a.show() # Outputs: Value is 6.7