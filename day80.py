#MULTI-LEVEL INHERITANCE

'''multilevel inhertance is a type of ineitance in oop where a derived class inherits from another derived class.
    This type of  inheritance allows you to build a heirarchy of the classes where one class builds upon another
    ,leding to a more specialized class.'''

'''syntax:-
            class baseclass:
                #code
            class derivedclass1(baseclass):
                #code
            class derivedclass(drivedclass1):
                #code
'''

class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species = "dog")
        self.breed = breed

    def show(self):
        animal.show(self)
        print(f"Breed : {self.breed}")

class goldenretriver(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,breed = "goldenretriver")
        self.color = color

    def show(self):
        dog.show(self)
        print(f"Color : {self.color}")

o = goldenretriver("Toomy","Black")
o.show()
print(goldenretriver.mro())