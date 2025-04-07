'''the super() leyword in python is used to refer to the parent class.
    It is especially useful when a class ingerits fro multiple parent 
    classes and you want to call a method from one of the parent classes
    
    When a class iherits from a parent class, it can override or extend the 
    method defined in the parent class. However ,sometimes you might want to use the parent
    class method in the child class. this .this is the  super() keyword comes in handy.'''

# class   parentclass:
#     def parent_method(self):
#         print("this is the parent method.")

# class childclass(parentclass):
    
#     def parent_method(self):
#         print("Sparsh Singh")
    
#     def child_method(delf):
#         print("this is the child method.")
#         super().parent_method()


# child = childclass()
# child.child_method()
# child.parent_method()

class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self,name,id,lan):
        super().__init__(name,id)  
        self.lan = lan

rohan = employee("Rohan", 1234)
shiva = programmer("SHIVA",1111,"Python")
print(shiva.name)
print(shiva.id)
