'''A class is a blueprint for creating objects providing initial values for state
    (members variables or attributes) and implementations of behaviour (member functions or methods).
    The user-defined objects are created using the class keyword.'''

# class person:
#     name = "Harry"
#     ocupation = "Software Developer"
#     networth = 10

# a = person()
# print(a.name)

# a.name = "sparsh"

# print(a.name)

'''self parameter:-
            the self parameter is a reference to the current instance of the class, and is 
                used to access variables that belongs to the class.
                
            it must provides as the extra parameter inside the method definition.'''
class person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        # print(f"{self.name} is a {self.occupation}")
        print(self.name," is a " ,self.occupation)

a = person()

a.info()