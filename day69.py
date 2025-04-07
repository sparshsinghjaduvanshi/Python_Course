'''to define a class methid ,you simply use the "@classmehod" decorator before the method definition.The 
    first argument of the method should always be "cls", which
    represent the class itself .Here is an example of how to define a class method.'''

class employee:
    company = "Apple"

    def show(self):
        print(f"the name is {self.name} and company is {self.company}.  ")

    @classmethod
    def changecompany(cls,newcompany):
        cls.company = newcompany

e = employee()
e.name = "Sparsh"
e.show()
e.changecompany("Nestle") # it is making changes in the instance but under @classmethod decorator it change the class varible.
e.show()
print(employee.company)
print(e.company)
#to make change in the 
# e1 = employee()
# e1.name = "sparsh"
# e1.show()