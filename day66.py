'''Instance vs Class varibles'''

#In Python,varibles can be defines at the class level or at the instance
#leven.Understanding the differene between these types of varibles is 
#crucial for writing efficient and maintainable code.

'''Class Varibles:- 
        class varibles are defined at the class level and are shared among all instances
        of the class. They are defined outside of any method and are 
        usually used to store information that is common to all instances of the class. For example,
        a class varible can be usd to store the number of instances of a class that have been created.'''

class employee:
    companyname = "Apple"
    def __init__(self,name):
        self.name = name
        self.rates = 0.02


    def showdetails(self):
        print(f"The name of the employee is {self.name} and the rates amount in {self.companyname} is {self.rates}")

emp1 = employee("Harry")
emp1.rates = 0.3
emp1.companyname = "Apple India"
emp1.showdetails()
employee.companyname = "GOOGLE"
print(employee.companyname)

emp2 = employee("Rohan")
employee.companyname = "Nestle"
emp2.showdetails()
# employee.showdetails(emp1) this and emp1.showdetails() are both the same things.

'''in the above code rates are the instace variable and can be aceessed and changed
    but the companyname is a class varible and it is the same for all the class varibles.'''
'''First the compiler search for the instance name if it does not find any then it will
    show the class name.'''


'''Instance Vribles:- 
            instance varibles are defined at the instance level and are unique to 
            each instance of the class .They are defined inside
            the init method and are usually used to store information that is 
            specific to each instance of the class. For example, an instance varibles can be used to store
            the name of an employe in a class that represents an employee.'''