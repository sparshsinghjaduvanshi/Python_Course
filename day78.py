#SINGLE INHERITANCE

'''the single inheritane is a type of inheritanc where a class inherts 
    properties and behaviour from a single parent class.This is the simplest 
    and most commn form of inheritance.'''

'''syntax:-
        class ChildClass(ParentClass): 
            #class body
'''

class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound make by the animal")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species = "dog")
        self.breed = breed
    def make_sound(self):
        print("bark!")

a = dog("dog", "doggerman")
print(a.species)
a.make_sound()

d = animal("dog", "pug")
d.make_sound()
print(d.species)